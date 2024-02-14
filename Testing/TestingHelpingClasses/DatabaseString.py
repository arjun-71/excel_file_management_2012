from sqlalchemy import create_engine

# Replace the placeholders with your actual database connection details
db_user = ""
db_password = ""
db_host = ""  # Usually "localhost" if it's on your local machine
db_port = ""  # PostgreSQL default port is 5432
db_name = "a"
table_name = ""
# Construct the PostgreSQL connection URL
db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"