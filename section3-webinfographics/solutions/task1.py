import mysql.connector

cnx = mysql.connector.connect(user='root', password='pass',
                              host='127.0.0.1',
                              database='museum')

cursor = cnx.cursor()
query = ("select e.id, e.name, d.idEntity, " +
         "d.restorationStart, d.restorationEnd " +
         "from entities as e, dates as d " +
         "where e.id = d.idEntity " +
         "and e.departmentId = 1 " +
         "order by d.restorationEnd desc " +
         "limit 250;")

print(query)
cursor.execute(query)
result = cursor.fetchall()


_ = 1
for (e_id, e_name, e_did,  d_start, d_end) in result:
    print(f"{_} | {e_id} \t {e_did} \t start: {d_start} \t end: {d_end} \t name: {e_name}")
    _ += 1

cursor.close()
cnx.close()