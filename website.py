from flask import Flask
from flask import url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime




app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///student_inquiries'
app.config['SECRET_KEY']="something"
db=SQLAlchemy(app)
app.app_context().push() #need to add this for some reason




     

class StudentIqs(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    last_name=db.Column(db.String(200),nullable=False)
    first_name=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(200),nullable=False,unique=True)
    date_added=db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self):
        return '<Name %r>'% self.name



class NameForm(FlaskForm):
    name=StringField("What is your name?",validators=[DataRequired()])
    submit=SubmitField("Submit")



class StudentInquiryForm(FlaskForm):
    first_name=StringField("FIRST NAME",validators=[DataRequired()])
    last_name=StringField("LAST NAME",validators=[DataRequired()])
    email=StringField("EMAIL",validators=[DataRequired()])    
    submit=SubmitField("Submit")




@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/our_services')
def ourServices():
    return render_template("our_services.html")

@app.route('/results')
def results():
    return render_template("results.html")



@app.route('/new_student', methods=['GET','POST'])
def newStudents():
    last_name=None
    first_name=None
    email=None
    
    form=StudentInquiryForm()
    
    if form.validate_on_submit():
        last_name=form.last_name.data
        form.last_name.data=''
        
        first_name=form.first_name.data
        form.first_name.data=''
        
        email=form.email.data
        form.email.data=''
        
    return render_template('new_student.html',
    last_name=last_name,first_name=first_name, email=email,form=form)


