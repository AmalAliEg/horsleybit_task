from django.db import connections

# Ex_Users_db resides in external database alias 'users_db'

def get_user_by_username(username: str):
    """Return user row as dict from Ex_Users_db."""
    with connections['users_db'].cursor() as cur:
        cur.execute(
            "SELECT id, username, email, is_active FROM ex_users WHERE username = %s",
            [username],
        )
        row = cur.fetchone()
    return (
        dict(id=row[0], username=row[1], email=row[2], is_active=row[3]) if row else None
    )

# Internal database alias 'default' (Int_db)

def get_wallet(user_id: int, currency: str):
    with connections['default'].cursor() as cur:
        cur.execute(
            "SELECT id, user_id, currency, balance FROM wallet_table WHERE user_id = %s AND currency = %s",
            [user_id, currency],
        )
        row = cur.fetchone()
    return (
        dict(id=row[0], user_id=row[1], currency=row[2], balance=row[3]) if row else None
    )

def create_transaction(tx_hash: str, sender_id: int, receiver_id: int, amount):
    """Insert a P2P transaction and return its primary key."""
    with connections['default'].cursor() as cur:
        cur.execute(
            """
            INSERT INTO transaction_table
            (transaction_hash, sender_user_id, receiver_user_id, amount, status)
            VALUES (%s, %s, %s, %s, 'pending')
            RETURNING id
            """,
            [tx_hash, sender_id, receiver_id, amount],
        )
        new_id = cur.fetchone()[0]
    return new_id


def fetch_transaction(pk: int):
    with connections['default'].cursor() as cur:
        cur.execute(
            "SELECT * FROM transaction_table WHERE id = %s",
            [pk],
        )
        row = cur.fetchone()
    return dict(zip([col[0] for col in cur.description], row)) if row else None


def create_user(username, email):
    with connections['users_db'].cursor() as cur:
        cur.execute(
            'INSERT INTO ex_users (username, email, is_active) VALUES (%s, %s, TRUE) RETURNING id',
            [username, email],
        )
        return cur.fetchone()[0]

def create_wallet(user_id, currency, balance):
    with connections['default'].cursor() as cur:
        cur.execute(
            '''
            INSERT INTO wallet_table (user_id, currency, balance)
            VALUES (%s, %s, %s) RETURNING id
            ''',
            [user_id, currency, balance],
        )
        return cur.fetchone()[0]
