import psycopg2

def InitializeDatabase():
    #Connects to the database (database="your_database", user="your_username", password="your_password", host="your_host", port="your_port")

    conn = psycopg2.connect(database="test",
                        host="localhost",
                        user="postgres",
                        password="admin@123",
                        port="5432")

    cur = conn.cursor()

     # Reading the SQL file content
    with open("databaseinit.sql", "r") as f:
       sql_statements = f.read()

        # Execute the SQL statements to create tables (assuming they don't exist)
    cur.execute(sql_statements)
    conn.commit()

    # Close the connection
    cur.close()
    conn.close()
