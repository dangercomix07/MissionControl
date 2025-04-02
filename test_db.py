import psycopg2

# Database connection details
DB_NAME = "missioncontrol"
DB_USER = "postgres"
DB_PASSWORD = "hello"  # Replace with your actual password
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("✅ Database connection successful!")

    # Create a cursor
    cur = conn.cursor()

    # Test Query: Fetch all tasks
    cur.execute("SELECT * FROM tasks;")
    rows = cur.fetchall()
    print("📌 Tasks Table Data:", rows)

    # Close the connection
    cur.close()
    conn.close()
except Exception as e:
    print("❌ Database connection failed:", e)
