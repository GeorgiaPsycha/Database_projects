#pip install  psycopg2
import psycopg2
import matplotlib.pyplot as plt

# Update connection string information
host = "student-database-exercise-server.postgres.database.azure.com"
dbname = "ProjectDB"
user = "betterzeta@student-database-exercise-server"
password = "pass"
sslmode = "require"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()
cursor.execute("select distinct userid , count(rating) from ratings group by userid order by userid;")
rows = cursor.fetchall()

zip(rows)
plt.plot(*zip(*rows))
plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.show()

# Clean up
conn.commit()
cursor.close()
conn.close()


