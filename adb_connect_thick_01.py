import oracledb
from pathlib import Path

# thick mode connection to oracle autonomous database example
# unzip the wallet file
# edit sqlnet.ora, setting the DIRECTORY param to the correct location
user = "admin"
password = "abc"
dsn = 'gn8obzxm3k3gooa6_high'
wallet_location = Path('C:/users/abc/Wallet_GN8OBZXM3K3GOOA6')
config_dir = Path('C:/users/abc/Wallet_GN8OBZXM3K3GOOA6')
instantclient_loc = Path("C:/users/abc/instantclient-basic-windows.x64-23.26.0.0.0/instantclient_23_0")

oracledb.init_oracle_client(lib_dir = str(instantclient_loc), config_dir = str(config_dir))

pool = oracledb.create_pool(
    user = user
    , password = password
    , dsn = dsn
)

con = pool.acquire()
cur = con.cursor()
cur.execute("select * from dual")
A = cur.fetchall()
print(A)
# [('X',)]
con.close()
