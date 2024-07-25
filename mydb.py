import mysql.connector



dataBase = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Multimed93-',  # Replace with your actual password
        )

# Prepare a cursofr object 
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
