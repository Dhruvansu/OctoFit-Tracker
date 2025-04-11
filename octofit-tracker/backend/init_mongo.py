from pymongo import MongoClient

try:
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    print("Connected to MongoDB successfully.")

    # Initialize the database
    db = client["octofit_db"]

    # Create collections
    collections = ["users", "teams", "activity", "leaderboard", "workouts"]
    for collection in collections:
        db.create_collection(collection)
        print(f"Collection '{collection}' created successfully.")

    # Create unique index for the users collection
    db["users"].create_index("email", unique=True)
    print("Unique index on 'email' field created successfully for 'users' collection.")

except Exception as e:
    print(f"An error occurred: {e}")
