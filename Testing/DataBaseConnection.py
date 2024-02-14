import TestingHelpingClasses.DatabaseString as dbs
import psycopg2 


print("hello world")
try:
    conn = psycopg2.connect(
        user=dbs.db_user,
        password=dbs.db_password,
        host=dbs.db_host,
        port=dbs.db_port,
        database=dbs.db_name
    )
    print("Connected to the database successfully!")
except (Exception, psycopg2.Error) as error:
    print(f"Error connecting to the database: {error}")
finally:
    if conn:
        conn.close()