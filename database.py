import pyodbc


# =========================================================
# DATABASE CONFIGURATION
# =========================================================

SERVER = r"LAPTOP-9T226DAT\OMKARSQLSERVER"
DATABASE = "RMS_DB"

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
)


# =========================================================
# DATABASE CONNECTION
# =========================================================

def connect_database():

    try:

        connection = pyodbc.connect(
            CONNECTION_STRING
        )

        return connection

    except Exception as e:

        print("Database Connection Error:")
        print(e)

        return None