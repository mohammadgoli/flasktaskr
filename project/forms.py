# _*_ coding: utf-8 _*_
from flask_wtf import Form
from wtforms import TextField, IntegerField, SelectField, PasswordField, StringField
from wtforms_html5 import DateRange, DateField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from datetime import date


class AddTaskForm(Form):
    task_id = IntegerField('Priority')
    name = TextField('Task Name', validators=[DataRequired()])
    due_date = DateField(
        'Date Due (mm/dd/yyyy)',
        validators=[DataRequired(), DateRange(
            min=date(2000, 1, 1),
            max=date(2100, 10, 10)
        )]
    )
    priority = SelectField(
        'Priority',
        validators=[DataRequired()],
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                 ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')
                 ]
    )
    status = IntegerField('Status')

class RegistrationForm(Form):
    u = u'باید وارد شود!'
    name = StringField(
        'Username',
        validators=[DataRequired(message=u), Length(min=6, max=25)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(), EqualTo('password', message='Passwords')]
    )

class LoginForm(Form):
    name = StringField(
        'Username',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )