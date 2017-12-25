
import mysql.connector 

cnx = mysql.connector.connect(user='root', password= 'mother',database='vehicle_database') #create connection with mysql sever
cursor = cnx.cursor()

query = ("SELECT PlateNo, Name, AddressId FROM owner_detail")
cursor.execute(query)

# print the rows
#for row in cursor :
#    print(row[1])
 
result_set= cursor.fetchall()
for row in result_set:
    print(row[0])

#cursor.execute(queryfor ( PlateNo, Name, AddressId) in cursor:
    #print {}.format(cursor)
    #print {}{}{}.format(PlateNo,Name,AddressId)

cursor.close()
cnx.close()