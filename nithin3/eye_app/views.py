from flask import Flask, render_template, request, redirect, url_for
import datetime
import os
from models import UserInfo, Spectacles, UserSpec
from __init__ import db, app
import sqlite3

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
default_filename = 'appenv_settings.py'
# Read environment-specific settings from file defined by OS environment variable 'ENV_SETTINGS_FILE'
env_settings_file = os.environ.get('ENV_SETTINGS_FILE', default_filename)
app.config.from_pyfile(env_settings_file)
# Initialize SQL Alchemy _after_ app.config has been read
db.init_app(app)


@app.route('/')
def main():
    result = UserInfo.query.all()
    return render_template('index.html', data=result)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('usr_register.html', response={"status_code": 200})


@app.route('/search', methods=['POST', 'GET'])
def search():
    result = None
    power_res = None
    if request.method == 'POST' and request.form['phone'] != '':
        customer_phone = request.form['phone']
        res = UserInfo.query.filter(UserInfo.mobile == customer_phone)
        for each in res:
            if each:
                val = Spectacles.query.filter(Spectacles.user_spec_id == each.user_id)
                for e in val:
                    if e:
                        power_res = val
                result = each
        if result is None:
            result = "No Customer with that Mobile number"
    return render_template('usr_search.html', output=result, power_info=power_res)


@app.route('/search_user', methods=['POST', 'GET'])
def search_user():
    customer_phone = request.form['phone']
    result = UserInfo.query.filter(user_id=customer_phone)
    return render_template('search_result.html', output=result)


@app.route('/details')
def details():
    result = UserInfo.query.all()
    return render_template('usr_details.html', data=result)


@app.route('/shop_more', methods=['POST'])
def shop_more():
    user_id = request.form['user_id']
    lbrand = request.form['lbrand']
    left_power = request.form['left_power']
    right_power = request.form['right_power']
    price = request.form['price']
    paid = request.form['paid']
    date = datetime.date.today()
    me = Spectacles(user_spec_id=user_id, lens_brand=lbrand, left_power=left_power, right_power=right_power, purchase_date=date, price=price, paid=paid)
    db.session.add(me)
    db.session.commit()
    return redirect(url_for('search'))
    #return {"status_code": 200}

import json
@app.route('/save_edit_info', methods=['POST'])
def save_edit_info():
    user_id = request.form['user_id']
    fname = request.form['fname']
    phone = request.form['phone']
    email = request.form['email']
    gender = request.form['gender']
    age = request.form['age']
    address = request.form['address']
    UserInfo.query.filter_by(user_id=user_id).update(dict(first_name=fname, mobile=phone, email=email, gender=gender, age=age, address=address, user_id=user_id))
    db.session.commit()
    return redirect(url_for('search'))
    #return json.dumps({"status_code": 200})


@app.route('/add_user', methods=['POST'])
def add_user():
    fname = request.form['fname']
    lbrand = request.form['lbrand']
    phone = request.form['phone']
    email = request.form['email']
    gender = request.form['gender']
    left_power = request.form['left_power']
    right_power = request.form['right_power']
    age = request.form['age']
    paid = request.form['paid']
    address = request.form['address']
    price = request.form['price']
    date = datetime.date.today()
    #valdate = datetime.datetime.strptime(age,"%Y-%m-%d").date()
    me = UserInfo(first_name=fname, mobile=phone, email=email, gender=gender, age=age, address=address)
    db.session.add(me)
    db.session.flush()
    sp = Spectacles(user_spec_id=me.user_id, lens_brand=lbrand, left_power=left_power, right_power=right_power, purchase_date=date, price=price, paid=paid)
    db.session.add(sp)
    db.session.commit()
    print("Registered")
    return redirect(url_for('register'))

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
 
    return None
@app.route('/tcust', methods=['GET'])
def tcust():
    print("todays customers")
    conn = create_connection("db.sqlite3")
    cur = conn.cursor()
    today = datetime.date.today()
    cur.execute("select * from user_info as u join spectacles as s on u.user_id = s.user_spec_id where purchase_date=?", (today,))
    result = cur.fetchall() 
    #result = UserSpec.query.filter(purchased_date=today)
    #result = UserSpec.query.all()
    return render_template('search_result.html', customers=result)

@app.route('/export_to_excel', methods=['POST'])
def export_to_excel():
    from xlsxwriter.workbook import Workbook
    user_workbook = Workbook('user_info.xlsx')
    spec_workbook = Workbook('spec_info.xlsx')
    user_worksheet = user_workbook.add_worksheet()
    spec_worksheet = spec_workbook.add_worksheet()
    users = UserInfo.query.all()
    spec = Spectacles.query.all()
    for row in users:
        print(row)
        user_worksheet.write(0, 0, row[0])
    user_workbook.close()
    for row in spec:
        print(row)
        spec_worksheet.write(0, 0, row[0])
    spec_workbook.close()

if __name__ == '__main__':
    app.run(debug=True)
