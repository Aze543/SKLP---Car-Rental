from flask import Flask, render_template, redirect, url_for, request, session
from sqlalchemy import create_engine, Column, Integer, String
from message import company_car_form, client_car_form, company_concern_form, req_confirmation
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from functools import wraps
import datetime as dt
import smtplib
import os

load_dotenv()
app = Flask(__name__)

if not os.path.exists(app.instance_path):
    os.makedirs(app.instance_path)
    
app.config['SECRET_KEY'] = os.getenv('SEC_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] =  f'sqlite:///{os.path.join(app.instance_path, "cars.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

admin_cre = {
    "password": os.getenv('ADMIN_PWD'), 
    "role": "admin",
}

class Cars(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, nullable=False)
    car_name = Column(String(80), nullable=False)
    car_type = Column(String(80), nullable=False)
    capacity = Column(Integer, nullable=False)
    transmission = Column(String(80), nullable=False)
    gasoline = Column(String(80), nullable=False)
    car_status = Column(String(80), nullable=False)
    return_date = Column(String(80), nullable=True)
    return_time = Column(String(80), nullable=True)
    pickup_date = Column(String(80), nullable=False)
    pickup_time = Column(String(80), nullable=False)
    
class CustomerRequest(Base):
    __tablename__ = 'customer_requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone_number = Column(String(15), nullable=False)
    pickup_date = Column(String(80), nullable=False)
    pickup_time = Column(String(80), nullable=False)
    return_date = Column(String(80), nullable=False)
    return_time = Column(String(80), nullable=False)
    car_type = Column(String(80), nullable=False)

Base.metadata.create_all(engine)

def dynamic_date():
    time = dt.datetime.now()
    return time.year

def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get('role') != 'admin':
            return  f"<h1>ACCESS PROHIBITED</h1><p>you don't have the credentials to access this part of the website</p><a href={url_for('home')}>go back</a>" 
        return func(*args, **kwargs)
    return decorated_function

def create_car(data):
    return Cars(
            id = len(data)+1, 
            car_name = request.form["car-name"],
            car_type = request.form["car-type"],
            capacity = request.form["capacity"],
            transmission = request.form["transmission"],
            gasoline = request.form["gasoline"],
            car_status = request.form["status"],
            pickup_date = request.form.get("pickup_date"),
            pickup_time = request.form.get("pickup_time"),
            return_date = request.form.get("return_date"),
            return_time = request.form.get("return_time"),
        )
    
def create_request(data, car):
    return CustomerRequest(
            id = len(data)+1, 
            name = request.form["name"],
            email = request.form["email"],
            phone_number = request.form["phone"],
            pickup_date = request.form["pickup-date"],
            pickup_time = request.form["pickup-time"],
            return_date = request.form["return-date"],
            return_time = request.form["return-time"],
            car_type = car
        )
   
def rearrange_car_ids():
    sql_session = Session()
    cars = sql_session.query(Cars).order_by(Cars.id).all()
    for index, car in enumerate(cars, start=1):
        car.id = index
    sql_session.commit()
    sql_session.close() 
    
def rearrange_req_ids():
    sql_session = Session()
    reqs = sql_session.query(CustomerRequest).order_by(CustomerRequest.id).all()
    for index, req in enumerate(reqs, start=1):
        req.id = index
    sql_session.commit()
    sql_session.close() 
    
def send_concern():
    my_gmail = os.getenv('PAS_GM')
    pw_gmail = os.getenv('PAS_PW')
    details = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "concern": request.form["concern"],
    }
    html = company_concern_form(details=details)
    msg = MIMEMultipart("alternative")
    html_mime = MIMEText(html, "html")
    msg.attach(html_mime)
    msg["Subject"] = f"SKLP Car Rental - New Customer Concern Received"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=pw_gmail)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="pythonaze543@gmail.com",
            msg=msg.as_string()
        )
    
def send_request(car):
    my_gmail = os.getenv('PAS_GM')
    pw_gmail = os.getenv('PAS_PW')
    details = {
        "name": request.form["name"],
        "email": request.form["email"],
        "car_type": car,
        "phone": request.form["phone"],
        "pickup_date": request.form["pickup-date"],
        "pickup_time": request.form["pickup-time"],
        "return_date": request.form["return-date"],
        "return_time": request.form["return-time"],
    }
    html = client_car_form(details=details)
    msg = MIMEMultipart("alternative")
    html_mime = MIMEText(html, "html")
    msg.attach(html_mime)
    msg["Subject"] = f"SKLP Car Rental - Car Rental Request Pending - {request.form["name"]}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=pw_gmail)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=request.form["email"],
            msg=msg.as_string()
        )
        
    html = company_car_form(details=details)
    msg = MIMEMultipart("alternative")
    html_mime = MIMEText(html, "html")
    msg.attach(html_mime)
    msg["Subject"] = f"SKLP Car Rental - New Car Rental Request - {request.form["name"]}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=pw_gmail)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="pythonaze543@gmail.com",
            msg=msg.as_string()
        )
        
def confirm_client(data, client):
    my_gmail = os.getenv('PAS_GM')
    pw_gmail = os.getenv('PAS_PW')
    details = {
        "name": client.name,
        "car_name": data.car_name,
        "car_type": data.car_type,
        "capacity": data.capacity,
        "transmission": data.transmission,
        "gasoline": data.gasoline,
        "pickup_date": data.pickup_date,
        "pickup_time": data.pickup_time,
        "return_date": data.return_date,
        "return_time": data.return_time,
    }
    html = req_confirmation(details=details)
    msg = MIMEMultipart("alternative")
    html_mime = MIMEText(html, "html")
    msg.attach(html_mime)
    msg["Subject"] = f"SKLP Car Rental - Car Rental Pickup Confirmation"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=pw_gmail)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=client.email,
            msg=msg.as_string()
        )       
 
def car_type_picker(car_type):
    if car_type == 'Sedan':
        return '''<option value="Sedan" selected>Sedan</option>
                  <option value="Van">Van</option>
                  <option value="AUV">AUV</option>
                  <option value="SUV">SUV</option>
                  <option value="Truck">Truck</option>'''
    elif car_type == 'Van':
        return '''<option value="Sedan">Sedan</option>
                  <option value="Van" selected>Van</option>
                  <option value="AUV">AUV</option>
                  <option value="SUV">SUV</option>
                  <option value="Truck">Truck</option>'''
    elif car_type == 'AUV':
        return '''<option value="Sedan">Sedan</option>
                  <option value="Van">Van</option>
                  <option value="AUV" selected>AUV</option>
                  <option value="SUV">SUV</option>
                  <option value="Truck">Truck</option>'''
    elif car_type == 'SUV':
        return '''<option value="Sedan">Sedan</option>
                  <option value="Van">Van</option>
                  <option value="AUV">AUV</option>
                  <option value="SUV" selected>SUV</option>
                  <option value="Truck">Truck</option>'''
    elif car_type == 'Truck':
        return '''<option value="Sedan">Sedan</option>
            <option value="Van">Van</option>
            <option value="AUV">AUV</option>
            <option value="SUV">SUV</option>
            <option value="Truck" selected>Truck</option>'''
                  
def car_transmission_picker(car_transmission):
    if car_transmission == 'Automatic':
        return '''<option value="Automatic" selected>Automatic</option>
                  <option value="Manual">Manual</option>'''
    elif car_transmission == 'Manual':
        return '''<option value="Automatic">Automatic</option>
                  <option value="Manual" selected>Manual</option>'''
            
def car_status_picker(car_status):
    if car_status == 'available':
        return '''<option value="available" selected>Available</option>
                  <option value="in-use">In-Use</option>
                  <option value="out-of-order">Out of Order</option>'''
    elif car_status == 'in-use':
        return '''<option value="available">Available</option>
                  <option value="in-use" selected>In-Use</option>
                  <option value="out-of-order">Out of Order</option>''' 
    elif car_status == 'out-of-order':
        return '''<option value="available">Available</option>
                  <option value="in-use">In-Use</option>
                  <option value="out-of-order" selected>Out of Order</option>'''
