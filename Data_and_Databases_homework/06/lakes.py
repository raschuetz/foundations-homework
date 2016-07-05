import pg8000
import decimal
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/lakes')
def give_lakes():
    conn = pg8000.connect(database = 'mondial', user = 'rebeccaschuetz')
    cursor = conn.cursor()
    sort = request.args.get('sort', 'name')
    type_param = request.args.get('type', None)

    # to get rid of not valid type_params:
    cursor.execute('SELECT name, elevation, area, type FROM lake WHERE type = %s LIMIT 1', [type_param])
    if not cursor.fetchone():
        lakes_list = []

    if type_param:
        if sort == 'elevation' or sort == 'area':
            cursor.execute('SELECT name, elevation, area, type FROM lake WHERE type = %s ORDER BY ' + sort + ' desc', [type_param])
        else:
            sort = 'name'
            cursor.execute('SELECT name, elevation, area, type FROM lake WHERE type = %s ORDER BY ' + sort, [type_param])
    else:
        if sort == 'elevation' or sort == 'area':
            cursor.execute('SELECT name, elevation, area, type FROM lake ORDER BY ' + sort + ' desc')
        else:
            sort = 'name'
            cursor.execute('SELECT name, elevation, area, type FROM lake ORDER BY ' + sort)
    lakes_list = []
    for item in cursor.fetchall():

        def decimal_to_int(x):
            if isinstance(x, decimal.Decimal):
                return int(x)
            else:
                return None

        # elevation = item[1]
        # if elevation:
        #     elevation = int(elevation)
        # area = item[2]
        # if area:
        #     area = int(area)
        # lakes_dict = {'name': item[0],
        #              'elevation': elevation,
        #              'area': area,
        #              'type': item[3]}

        lakes_dict = {'name': item[0],
                     'elevation': decimal_to_int(item[1]),
                     'area': decimal_to_int(item[2]),
                     'type': item[3]}

        lakes_list.append(lakes_dict)
    for dictionary in lakes_list:
        print(dictionary)
    return jsonify(lakes_list)

app.run()
