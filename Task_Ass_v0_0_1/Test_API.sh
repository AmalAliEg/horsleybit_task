#!/bin/bash

# API Testing Script with Dynamic IDs

BASE_URL="http://localhost:8000/api/users"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "========================================="
echo "Testing Django REST API"
echo "========================================="

# Test 1: GET all users and store the response
echo -e "\n${GREEN}Test 1: Getting all users${NC}"
echo "GET $BASE_URL/"
USERS_RESPONSE=$(curl -s -X GET "$BASE_URL/" -H "Content-Type: application/json")
echo $USERS_RESPONSE | python -m json.tool
echo -e "\n"

# Extract first user ID using python
FIRST_USER_ID=$(echo $USERS_RESPONSE | python -c "import sys, json; data = json.load(sys.stdin); print(data[0]['id']) if data else print('none')")

if [ "$FIRST_USER_ID" != "none" ]; then
    echo -e "${YELLOW}Found first user ID: $FIRST_USER_ID${NC}"
else
    echo -e "${RED}No users found in database${NC}"
fi

# Test 2: POST new user
echo -e "\n${GREEN}Test 2: Creating a new user${NC}"
echo "POST $BASE_URL/"
NEW_USER_RESPONSE=$(curl -s -X POST "$BASE_URL/" \
     -H "Content-Type: application/json" \
     -d '{
       "username":"api_test_user",
       "Phone_num":9876543210,
       "email":"apitest@example.com",
       "Gender":"Female",
       "birthday":"1990-12-25"
     }')
echo $NEW_USER_RESPONSE | python -m json.tool
NEW_USER_ID=$(echo $NEW_USER_RESPONSE | python -c "import sys, json; print(json.load(sys.stdin)['id'])")
echo -e "${YELLOW}Created new user with ID: $NEW_USER_ID${NC}\n"

# Test 3: GET specific user (using actual ID)
if [ "$FIRST_USER_ID" != "none" ]; then
    echo -e "\n${GREEN}Test 3: Getting user with ID $FIRST_USER_ID${NC}"
    echo "GET $BASE_URL/$FIRST_USER_ID/"
    curl -s -X GET "$BASE_URL/$FIRST_USER_ID/" -H "Content-Type: application/json" | python -m json.tool
    echo -e "\n"
fi

# Test 4: PUT update user (using the newly created user)
echo -e "\n${GREEN}Test 4: Updating user with ID $NEW_USER_ID${NC}"
echo "PUT $BASE_URL/$NEW_USER_ID/"
curl -s -X PUT "$BASE_URL/$NEW_USER_ID/" \
     -H "Content-Type: application/json" \
     -d '{
       "username":"updated_api_user",
       "Phone_num":1111111111,
       "email":"updated_api@example.com",
       "Gender":"Male",
       "birthday":"1985-06-15"
     }' | python -m json.tool
echo -e "\n"

# Test 5: Show all users again
echo -e "\n${GREEN}Test 5: Showing all users after update${NC}"
curl -s -X GET "$BASE_URL/" -H "Content-Type: application/json" | python -m json.tool
echo -e "\n"

# Test 6: DELETE the newly created user
echo -e "\n${GREEN}Test 6: Deleting user with ID $NEW_USER_ID${NC}"
echo "DELETE $BASE_URL/$NEW_USER_ID/"
curl -s -X DELETE "$BASE_URL/$NEW_USER_ID/" -H "Content-Type: application/json"
echo -e "${YELLOW}User deleted successfully${NC}\n"

# Test 7: Verify deletion
echo -e "\n${GREEN}Test 7: Final user list${NC}"
curl -s -X GET "$BASE_URL/" -H "Content-Type: application/json" | python -m json.tool

echo -e "\n========================================="
echo "API Testing Complete"
echo "========================================="