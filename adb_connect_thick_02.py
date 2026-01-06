import oracledb
import os
import sys

# Path to your Oracle Instant Client
INSTANT_CLIENT_DIR = r"C:\Users\abc\instantclient-basic-windows.x64-23.26.0.0.0\instantclient_23_0"

# Path to your wallet directory (unzipped wallet files)
WALLET_DIR = r"C:\users\abc\Wallet_GN8OBZXM3K3GOOA6"

# '''# set WALLET_LOCATION in sqlnet.ora:
# WALLET_LOCATION = (SOURCE = (METHOD = file) (METHOD_DATA = (DIRECTORY="C:\users\abc\Wallet_GN8OBZXM3K3GOOA6")))
# '''

# Database credentials
DB_USER = "admin"
DB_PASSWORD = "abc"
DB_SERVICE = 'gn8obzxm3k3gooa6_high'  # Could be adb_low, adb_medium, etc.


try:
    # Initialize Thick mode
    oracledb.init_oracle_client(lib_dir=INSTANT_CLIENT_DIR)
    # Set TNS_ADMIN so Oracle knows where to find tnsnames.ora and sqlnet.ora
    os.environ["TNS_ADMIN"] = WALLET_DIR
    # Create connection
    connection = oracledb.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        dsn=DB_SERVICE
    )
    print("✅ Connected to Autonomous Database in Thick mode!")
    # Example query
    with connection.cursor() as cursor:
        cursor.execute("SELECT sysdate FROM dual")
        for row in cursor:
            print("Database time:", row[0])
except oracledb.Error as e:
    print("❌ Database connection failed:", e)
    sys.exit(1)
