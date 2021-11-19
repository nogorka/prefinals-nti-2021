from flask import Flask
from flask import jsonify
import mysql.connector
from flask_cors import CORS, cross_origin
import csv


app = Flask(__name__)
CORS(app, support_credentials=True)


def get_data_from_db(query):

    cnx = mysql.connector.connect(user='root', password='6493',
                                  host='127.0.0.1',
                                  database='museum')

    cursor = cnx.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    cnx.close()

    return result


@app.route('/task1')
@cross_origin(supports_credentials=True)
def task1():

    query = ("select e.id, e.name, " +
             "m.impressionTotal, m.visualFeedback, m.descriptionInformative " +
             "from entities as e, metrics as m " +
             "where e.id = m.idEntity;")

    result = get_data_from_db(query)

    dct = {}
    for (e_id, e_name, m_impression, m_feedback, m_description) in result:
        if e_id in dct:
            pass
        else:
            dct[e_id] = {'visualFeedback': 0, 'impressionTotal': 0, 'descriptionInformative': 0,
                         'totalAmount': 0, 'name': e_name}

        dct[e_id]['visualFeedback'] += m_feedback
        dct[e_id]['impressionTotal'] += m_impression
        dct[e_id]['descriptionInformative'] += m_description
        dct[e_id]['totalAmount'] += 1

    dct = dict(sorted(dct.items(), key=lambda item: item[1]['totalAmount']))

    return jsonify(dct)


@app.route('/task2')
@cross_origin(supports_credentials=True)
def task2():

    query = ("select e.id, e.name, e.countryId, " +
             "c.id, c.name " +
             "from entities as e, countries as c " +
             "where c.id = e.countryId;")

    result = get_data_from_db(query)

    dct = {}
    for (e_id, e_name, e_countryId, c_id, c_name) in result:
        if c_id in dct:
            pass
        else:
            dct[c_id] = {'totalAmount': 0, 'name': c_name}

        dct[c_id]['totalAmount'] += 1

    dct = dict(sorted(dct.items(), key=lambda item: item[1]['totalAmount']))

    return jsonify(dct)


@app.route('/task3')
@cross_origin(supports_credentials=True)
def task3():

    query = ("select e.id, e.name, e.accessionYear, " +
             "m.impressionTotal, m.visualFeedback, m.descriptionInformative " +
             "from entities as e, metrics as m " +
             "where e.id = m.idEntity and e.departmentId = 3 and e.accessionYear > 1800;")

    result = get_data_from_db(query)

    dct = {}
    for (e_id, e_name, e_year, m_impression, m_feedback, m_description) in result:
        if e_id not in dct:
            dct[e_id] = {'visualFeedback': 0, 'impressionTotal': 0, 'descriptionInformative': 0,
                         'totalAmount': 0, 'name': e_name, 'accessionYear': e_year}

        dct[e_id]['visualFeedback'] += m_feedback
        dct[e_id]['impressionTotal'] += m_impression
        dct[e_id]['descriptionInformative'] += m_description
        dct[e_id]['totalAmount'] += 1

    dct = dict(sorted(dct.items(), key=lambda item: item[1]['accessionYear']))

    year_dct = {}
    for row in dct.values():
        cur_year = row['accessionYear']
        if cur_year not in year_dct:
            year_dct[cur_year] = {'sumVisualFeedback': 0, 'sumImpressionTotal': 0, 'sumDescriptionInformative': 0,
                                  'totalAmount': 0, 'names': []}

        year_dct[cur_year]['totalAmount'] += 1
        year_dct[cur_year]['names'].append(row['name'])
        year_dct[cur_year]['sumVisualFeedback'] += row['visualFeedback'] / row['totalAmount']
        year_dct[cur_year]['sumImpressionTotal'] += row['impressionTotal'] / row['totalAmount']
        year_dct[cur_year]['sumDescriptionInformative'] += row['descriptionInformative'] / row['totalAmount']

    return jsonify(year_dct)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
