import PacemakerDatabase as database
import unittest

## Database testing
db = database.PacemakerDatabase.get_instance()

def database_test1():
    # Test commands
    print("Test 1")
    db.create_account_table()
    for i in range(5):
        db.add_user(f"user{i}", "password")
    db.get_all_users()
    db.add_user("Jay", "jaysPassword")
    db.get_all_users()
    db.delete_user("Jay")
    db.get_all_users()
    db.get_user("user1")
    for i in range(5):
        db.add_user(f"user{i+5}", "password")
    db.get_all_users()
    print("expecting 10 user limit error for next operation:")
    db.add_user("user11", "password")
    print("make sure program still works:")
    db.get_all_users()
    db.drop_account_table()
    
database_test1()