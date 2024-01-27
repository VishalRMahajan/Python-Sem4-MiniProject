from app import app
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv('.env')
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'wraptalentauthentication@gmail.com'  # replace with your email

app.config['MAIL_PASSWORD'] =  'vjtchrdezeddxrvu'
mail = Mail(app)


def send_otp(email, otp):
    msg = Message('OTP for your account', sender='wraptalentauthentication@gmail.com', recipients=[email])
    msg.body = f'Your OTP is {otp}'
    mail.send(msg)