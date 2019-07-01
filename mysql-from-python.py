import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database. **It's a connection object**
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='123',
                             db='Chinook')

try:
    # Run a SQL query
    with connection.cursor() as cursor:
        list_of_names = ['Alexander','Alexander']
        # Prepare a string with the same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names)) 
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names) # %s unpacks the tuple in affected row                        
                        
        connection.commit()
finally:
    # Important to CLOSE the connection, regardless of whether or not the above was successful
    connection.close()

