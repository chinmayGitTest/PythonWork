from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField    #using StirngFiled password entity is shown #using PasswordField password filed is not shown #SubmitFiled is used to submit form
from wtforms.validators import DataRequired

# using flask form
class LoginForm(FlaskForm):
    email = StringField(label='Email')#validators=[DataRequired])
    password = PasswordField(label='Password')#validators=[DataRequired])       #Entity will be change
    submit = SubmitField(label="Log In")                                        #Submit button is working

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap(app)   #initialise bootstrap-flask

# flask index.html file
@app.route("/")
def home():
    return render_template('index.html')

# flask login.html file on server
@app.route("/login", methods=["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "123456789":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    # if login_form.validate_on_submit():
    #     print(login_form.email.data)
    return render_template('login.html',form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
