import mysql.connector

cnx = mysql.connector.connect(user='root', password='pass',
                              host='127.0.0.1',
                              database='museum')

cursor = cnx.cursor()
query = ("select e.id, e.name, " +
         "m.impressionTotal, m.visualFeedback, m.descriptionInformative " +
         "from entities as e, metrics as m " +
         "where e.id = m.idEntity;")

cursor.execute(query)
result = cursor.fetchall()

dct = {}
for (e_id, e_name, m_impression, m_feedback, m_description) in result:
    if e_id in dct:
        pass
    else:
        dct[e_id] = {'feedback': 0, 'impression': 0, 'description': 0,
                     'total': 0, 'name': e_name}

    dct[e_id]['feedback'] += m_feedback
    dct[e_id]['impression'] += m_impression
    dct[e_id]['description'] += m_description
    dct[e_id]['total'] += 1

dct = dict(sorted(dct.items(), key=lambda item: item[1]['total']))



avg_dct = {}
for line in dct.values():
    avg_dct[line['name']] = line['impression'] / line ['total']

avg_dct = dict(sorted(avg_dct.items(), key=lambda item: item[1]))

for line in list(avg_dct.items())[-10:]:
    print (line)

cursor.close()
cnx.close()
