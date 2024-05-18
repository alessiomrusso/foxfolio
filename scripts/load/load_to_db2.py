import ibm_db
import ibm_db_dbi
import configparser

def load_data(df, table_name):
    # Read database credentials from config file
    config = configparser.ConfigParser()
    config.read('db_credentials.ini')

    db_credentials = {
        "DRIVER": config['db2']['DRIVER'],
        "DATABASE": config['db2']['DATABASE'],
        "HOSTNAME": config['db2']['HOSTNAME'],
        "PORT": config['db2']['PORT'],
        "PROTOCOL": config['db2']['PROTOCOL'],
        "UID": config['db2']['UID'],
        "PWD": config['db2']['PWD'],
        "SECURITY": config['db2']['SECURITY']
    }

    # Connect to DB2 database   
    dsn = (
        "DRIVER={0};"
        "DATABASE={1};"
        "HOSTNAME={2};"
        "PORT={3};"
        "PROTOCOL={4};"
        "UID={5};"
        "PWD={6};"
        "SECURITY={7};"
    ).format(*db_credentials.values())
    
    print(dsn)
    
    options = { ibm_db.SQL_ATTR_AUTOCOMMIT:  ibm_db.SQL_AUTOCOMMIT_ON }
    
    try:
        conn = ibm_db.connect(dsn, "", "", options)
        print ("Connected to database.")
    except:
        print ("Unable to connect: ", ibm_db.conn_errormsg() )
        
    # Load data into the table
    columns = 'Symbol,Date,Open,Close'
    insertSQL = 'Insert into STOCKS(' + columns + ') values(?,?,?,?)'
    stmt = ibm_db.prepare(conn, insertSQL)
    
    print(df.head())
    
    for n in range(len(df)) :
        ibm_db.bind_param(stmt,1,str(df.at[n,'Symbol']))
        ibm_db.bind_param(stmt,2,str(df.at[n,'Date']))
        ibm_db.bind_param(stmt,3,str(df.at[n,'Open']))
        ibm_db.bind_param(stmt,4,str(df.at[n,'Close']))
        
        ibm_db.execute(stmt)
    
    print('Data was loaded correctly')
    
    # Close connection
    ibm_db.close(conn)