import PacemakerDatabase as database
import unittest

## Database testing
db = database.PacemakerDatabase.get_instance()

def database_test1():
    """Tests the functionality for the account table."""
    # Test account table
    print("Test 1 - accounts table")
    db.create_and_populate()
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
    db.drop_all_tables()

def database_test2():
    """Tests the SQL functionality for the parameters table."""
    print("Test 2 - parameters table")
    db.create_and_populate()
    db.get_parameters()
    db.drop_all_tables()

def database_test3():
    """Tests the SQL functionality for the modes table."""
    print("Test 3 - modes table")
    db.create_and_populate()
    db.get_all_modes()
    db.drop_all_tables()

def database_test4():
    """Tests the SQL functionality for the mode parameters table."""
    print("\nTest 4 - mode parameters")
    db.create_and_populate()
    modes = db.get_all_modes()
    print(len(modes), "modes")
    for mode in modes:
        parameters = db.get_parameters(mode = mode[0])
        print(parameters)
    # attempt to get parameters from a mode that does not exist
    print("Should return empty list:", db.get_parameters(mode = 'fake'))
    db.drop_all_tables()

database_test1()
database_test2()
database_test3()
database_test4()

