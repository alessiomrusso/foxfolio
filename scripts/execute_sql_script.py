import ibm_db
import configparser

def execute_sql_script(sql_file_path):
    
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
    
    try:
        conn = ibm_db.connect(dsn, "", "")
        print ("Connected to database.")
    except:
        print ("Unable to connect: ", ibm_db.conn_errormsg() )

    # Read SQL script from file
    with open(sql_file_path, 'r') as file:
        sql_script = file.read()

    # Execute SQL script
    stmt = ibm_db.exec_immediate(conn, sql_script)

    # Close connection
    ibm_db.close(conn)