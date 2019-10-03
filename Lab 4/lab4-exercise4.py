#!/usr/bin/env python3
import sqlite3
#some initial data
id = 4;
sid = 0;
temperature = 0.0;
date = '2014-01-05';
#connect to database file
dbconnect = sqlite3.connect("my.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();

#lab ex4
cursor.execute('create table sensors (sensorID integer, type text, zone text);')
types = ["door", "temperature", "door", "motion", "temperature"]
zone = ["kitchen", "kitchen", "garage", "garage","garage"]
for i in range(5):
    #execute insert statement
    sid += 1;
    typed = types[i];
    zoned = zone[i];
    cursor.execute('''insert into sensors values (?, ?, ?)''',
    (sid, typed, zoned));
dbconnect.commit();
#execute simple select statement
print("zone = kitchen")
cursor.execute('SELECT * FROM sensors where zone = "kitchen"');
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] );
    
print("type = door")
cursor.execute('SELECT * FROM sensors where type = "door"');
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] );
    
print("zone = kitchen and type = door")
cursor.execute('SELECT * FROM sensors where zone = "kitchen" AND type = "door"');
for row in cursor:
    print(row['sensorID'],row['type'],row['zone'] );

#end of ex4 modifications


for i in range(10):
    #execute insert statement
    id += 1;
    temperature += 1.1;
    cursor.execute('''insert into temperature values (?, ?, ?)''',
    (id, temperature, date));
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temperature');
#print data
for row in cursor:
    print(row['id'],row['temp'],row['date'] );
#close the connection
dbconnect.close();
