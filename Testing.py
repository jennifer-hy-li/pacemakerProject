import PacemakerDatabase as pd

## Database testing

database = pd.PacemakerDatabase.get_instance()

def database_test1():
    # Test commands
    print("Test 1")
    database.create_account_table()
    for i in range(5):
        database.add_user(f"user{i}", "password")
    database.get_all_users()
    database.add_user("Jay", "jaysPassword")
    database.get_all_users()
    database.delete_user("Jay")
    database.get_all_users()
    database.get_user("user1")
    for i in range(5):
        database.add_user(f"user{i+5}", "password")
    database.get_all_users()
    print("expecting 10 user limit error for next operation:")
    database.add_user("user11", "password")
    print("make sure program still works:")
    database.get_all_users()
    database.drop_account_table()

def database_test2():
    # Test commands
    print("\n\nTest 2")
    database2 = database.get_instance()
    database.create_account_table()
    for i in range(5):
        database.add_user(f"user{i}", "password")
    database2.get_all_users()
    database.drop_account_table()


database_test1()
database_test2()