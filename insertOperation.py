from mysql.connector import MySQLConnection, Error
#from python_mysql_dbconfig import read_db_config

def insert_vehicle_database(ownerdetails):
    query = "INSERT INTO owner_detail(Plateno,Name,addressid) " \
        "VALUES(%s,%s,%s)"
 
    try:
       # db_config = read_db_config()
        conn = MySQLConnection(user='root', password= 'mother',database='vehicle_database')

        cursor = conn.cursor()
        cursor.executemany(query, ownerdetails)

        conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()

def main():
    ownerdetails = [('uk200', 'ee','200'),
             ('uk210', 'ff','210'),
             ('uk240', 'gg','240')]
    insert_vehicle_database(ownerdetails)

if __name__ == '__main__':
    main()