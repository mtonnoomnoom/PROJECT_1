from src.utils.database_manage import DatabaseManager

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    database = DatabaseManager()
    query = "tuýet"
    print("S-Bert Model: ", database.query_collection(query))