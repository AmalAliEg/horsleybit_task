from django.db import connections

with connections['users_db'].cursor() as c:     # ← قاعدة x_Users_db
    c.execute("INSERT INTO ex_users (username,email) VALUES "
              "('alice','alice@mail.com'),"
              "('bob','bob@mail.com');")

with connections['default'].cursor() as c:      # ← قاعدة Int_db
    c.execute("INSERT INTO wallet_table (user_id,currency,balance) VALUES "
              "(1,'BTC',0.5),(1,'USD',200),(2,'ETH',3);")
    c.execute("INSERT INTO transaction_table "
              "(transaction_hash,sender_user_id,receiver_user_id,amount,status)"
              "VALUES ('tx123',1,2,50,'completed');")
print("✅ جداول ex_users / wallet_table / transaction_table اتملّت بنجاح!")
