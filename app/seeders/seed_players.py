from ..database import insert_data

# Sample data to insert
sample_data = {"key": "value"}

# Call the insert_data function to insert data into the database
inserted_data = insert_data(sample_data, "players")

# Print the inserted ID
print(f"Data inserted with ID: {inserted_data.inserted_id}")
