from flask import Flask, render_template, request, redirect, url_for
import datetime
import os
from models import UserInfo, Spectacles
from __init__ import db, app

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
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
    return render_template('usr_register.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    result = None
    power_res = None
    if request.method == 'POST' and request.form['cust_id'] != '':
        customer_id = request.form['cust_id']
        res = UserInfo.query.filter(UserInfo.user_id == customer_id)
        val = Spectacles.query.filter(Spectacles.user_spec_id == customer_id)
        for each in val:
            if each:
                power_res = val
        for each in res:
            if each:
                result = each
        if result is None:
            result = "No Customer with that id"
    return render_template('usr_search.html', output=result, power_info=power_res)


@app.route('/search_user', methods=['POST', 'GET'])
def search_user():
    customer_id = request.form['cust_id']
    result = UserInfo.query.filter(user_id=customer_id)
    return render_template('search_result.html', output=result)


@app.route('/details')
def details():
    result = UserInfo.query.all()
    return render_template('usr_details.html', data=result)


@app.route('/shop_more', methods=['POST'])
def shop_more():
    user_id = request.form['user_id']
    left_power = request.form['left_power']
    right_power = request.form['right_power']
    price = request.form['price']
    date = datetime.date.today()
    me = Spectacles(user_spec_id=user_id, left_power=left_power, right_power=right_power, purchased_date=date, price=price)
    db.session.add(me)
    db.session.commit()
    return redirect(url_for('search'))


@app.route('/save_edit_info', methods=['POST'])
def save_edit_info():
    user_id = request.form['user_id']
    fname = request.form['fname']
    lname = request.form['lname']
    phone = request.form['phone']
    email = request.form['email']
    gender = request.form['gender']
    dob = request.form['dob']
    address = request.form['address']
    UserInfo.query.filter_by(user_id=user_id).update(dict(first_name=fname, last_name=lname, mobile=phone, email=email, gender=gender, dob=dob, address=address, user_id=user_id))
    db.session.commit()
    return redirect(url_for('search'))


@app.route('/add_user', methods=['POST'])
def add_user():
    fname = request.form['fname']
    lname = request.form['lname']
    phone = request.form['phone']
    email = request.form['email']
    gender = request.form['gender']
    left_power = request.form['left_power']
    right_power = request.form['right_power']
    dob = request.form['dob']
    address = request.form['address']
    price = request.form['price']
    date = datetime.date.today()
    me = UserInfo(first_name=fname, last_name=lname, mobile=phone, email=email, gender=gender, dob=dob, address=address)
    db.session.add(me)
    db.session.flush()
    sp = Spectacles(user_spec_id=me.user_id, left_power=left_power, right_power=right_power, purchased_date=date, price=price)
    db.session.add(sp)
    db.session.commit()
    print "Registered"
    return redirect(url_for('register'))


if __name__ == '__main__':
    app.run(debug=True)