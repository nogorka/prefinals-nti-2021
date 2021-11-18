# Ваша задача найти экспонат по дате окончания реставрации из категории «The american wing».
# Подсказка: посмотрите как работают условия для sql запросов по ключевому параметру.

# В ответе вам необходимо написать название экспоната, время начала реставрации и время окончания реставрации.
# Ответ: 154 Brooch 2017-09-07 00:00:00 2022-01-24 00:00:00

import mysql.connector

cnx = mysql.connector.connect(user='root', password='6493',
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


# def select_with_cause(fields, table, cause):
#     query = f"select {fields} from {table} where {cause};"
#     print (query)

#     cursor.execute(query)
#     return cursor.fetchall()

# fields = 'id, name'
# table = 'entities'
# expr = 'departmentId = 1'

# # get id and name from entities where department = The american wing
# entities = select_with_cause(fields, table, expr)

# # reshape result from list [[id, name], ..] to dict {id:name, ..}
# entities_dict = {}
# for (id, name) in entities:
#     entities_dict[id] = name

# # get dates from dates where entityid = entityid from previous table
# fields2 = '*'
# table2 = 'dates'

# keys = entities_dict.keys()
# entities = select_with_cause(fields, table, expr)
