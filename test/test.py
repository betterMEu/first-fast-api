def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))

import psycopg

try:
    conn = psycopg.connect(
        host="localhost",
        port=5432,
        database="fastapi",
        user="postgres",
        password="123456",
    )
    print("Database connection successful")
except Exception as e:
    print(f"Connection failed: {e}")
