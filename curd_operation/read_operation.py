#!/usr/bin/env python
def getval()
 import MySQLdb
 cnx = MySQLdb.connect(user='root', passwd= 'mother',db='vehicle_database')
 cursor = cnx.cursor()

 query = ("SELECT PlateNo, Name, AddressId FROM owner_detail")
 cursor.execute(query)

 # print the rows
 #for row in cursor :
 #    print(row[1])
 
 result_set= cursor.fetchall()
 #for row in result_set:
 #    print(row)

 #cursor.execute(queryfor ( PlateNo, Name, AddressId) in cursor:
 #print {}.format(cursor)
 #print {}{}{}.format(PlateNo,Name,AddressId)

 cursor.close()
 cnx.close()
 return result_set