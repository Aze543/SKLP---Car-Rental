from functions import *

#USER SIDE
@app.route('/')
def home():
    year = dynamic_date()
    return render_template('index.html', year=year)

@app.route('/rent')
def car_list():
    year = dynamic_date()
    return render_template('list.html', year=year)

@app.route('/about-us')
def about_us():
    year = dynamic_date()
    return render_template('about.html', year=year)

@app.route('/<string:car>-form', methods=["GET", "POST"])
def car_form(car):
    car = car
    sql_session = Session()
    year = dynamic_date()
    if request.method == "POST":
        try:
            send_request(car)
        except Exception as e:
            return f"ERROR:{e}"
        else:
            data = sql_session.query(CustomerRequest).all()
            new_request = create_request(data=data, car=car)
            sql_session.add(new_request)
            sql_session.commit()
            sql_session.close()
            return redirect(url_for('car_list',success=True))
    return render_template('car-form.html', car=car, year=year)

@app.route('/contacts',methods=["GET", "POST"])
def contact_form():
    year = dynamic_date()
    if request.method == "POST":
        try:
            send_concern()
        except Exception as e:
            return f"ERROR:{e}"
        else:
            return redirect(url_for('home',success=True))
    
    return render_template('contacts.html', year=year)

#ADMIN SIDE
@app.route('/admin', methods=["GET", "POST"])
def admin():
    year = dynamic_date()
    if request.method == "POST":
        pwd = request.form['password']
        if pwd == admin_cre['password']:
            session['role'] = admin_cre['role']
            return redirect(url_for('car_manage'))
        else:
            return redirect(url_for('admin', failed=True))
        
    return render_template('admin.html', year=year)

@app.route('/car-management')
@admin_required
def car_manage():
    sql_session = Session()
    c_data = sql_session.query(Cars).all()
    req_len = len(sql_session.query(CustomerRequest).all())
    return render_template('car-manage.html', car_data=c_data, req_len=req_len)

@app.route('/car-management/add-car', methods=["GET", "POST"])
@admin_required
def add_car():
    sql_session = Session()
    if request.method == "POST":
        data = sql_session.query(Cars).all()
        new_car = create_car(data)   
        sql_session.add(new_car)
        sql_session.commit()
        sql_session.close()
        return redirect(url_for('car_manage'))
    return render_template('add-car.html')

@app.route('/car-management/edit-car<int:id>', methods=["GET", "POST"])
@admin_required
def edit_car(id):
    sql_session = Session()
    car_data = sql_session.get(Cars, id)
    if request.method == "POST":
        car_data.car_name = request.form["car-name"]
        car_data.car_type = request.form["car-type"]
        car_data.capacity = request.form["capacity"]
        car_data.transmission = request.form["transmission"]
        car_data.gasoline = request.form["gasoline"]
        car_data.car_status = request.form["status"]
        car_data.pickup_date = request.form.get("pickup_date")
        car_data.pickup_time = request.form.get("pickup_time")
        car_data.return_date = request.form.get("return_date")
        car_data.return_time = request.form.get("return_time")
        sql_session.commit()
        sql_session.close()
        return redirect(url_for('car_manage'))
    ec_dropdowns = {
        "car-type": car_type_picker(car_data.car_type),
        "car-transmission": car_transmission_picker(car_data.transmission),
        "car-status": car_status_picker(car_data.car_status)
    }
    return render_template('edit-car.html', car=car_data, web_drd=ec_dropdowns)

@app.route('/request')
@admin_required
def car_requests():
    sql_session = Session()
    data = sql_session.query(CustomerRequest).all()
    return render_template('car-requests.html', req_data=data)

@app.route('/request/<int:id>', methods=["GET", "POST"])
@admin_required
def review_request(id):
    sql_session = Session()
    r_data = sql_session.get(CustomerRequest, id)
    c_data = sql_session.query(Cars).filter(Cars.car_type == r_data.car_type, Cars.car_status == "available").all()
    if request.method == "POST":
        car = sql_session.get(Cars, request.form["car_id"])
        car.car_status = "in-use"
        car.pickup_date = request.form.get("pickup_date")
        car.pickup_time = request.form.get("pickup_time")
        car.return_date = request.form.get("return_date")
        car.return_time = request.form.get("return_time")
        confirm_client(car, r_data)
        sql_session.delete(r_data)
        sql_session.commit()
        sql_session.close()
        rearrange_req_ids()  
        return redirect(url_for('car_requests', success=True))      
    return render_template('review-request.html', req=r_data, cars=c_data)

@app.route('/remove/all')
@admin_required
def remove_requests():
    sql_session = Session()
    sql_session.query(CustomerRequest).delete()
    sql_session.commit()
    sql_session.close()
    return redirect(url_for('car_requests'))      
       
@app.route('/remove/<int:id>')
@admin_required
def remove_single_req(id):
    sql_session = Session()
    req = sql_session.get(CustomerRequest, id)
    sql_session.delete(req)
    sql_session.commit()
    sql_session.close()
    rearrange_req_ids() 
    return redirect(url_for('car_requests'))    

@app.route('/remove-car<int:id>')
@admin_required
def remove_car(id):
    sql_session = Session()
    car_data = sql_session.get(Cars, id)
    sql_session.delete(car_data)
    sql_session.commit()
    sql_session.close()
    rearrange_car_ids()
    return redirect(url_for('car_manage'))

@app.route('/logout')
@admin_required
def logout():
    if session['role'] != admin_cre['role']:
        return redirect(url_for('home'))
    session.clear()
    return redirect(url_for('home'))
    

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
    
    