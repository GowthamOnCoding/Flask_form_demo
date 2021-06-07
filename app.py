from flask import Flask,redirect,url_for,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app=Flask(__name__)
app.config['SECRET_KEY'] = 'Mysecretkey'

class InforForm(FlaskForm):
    breed = StringField("What Breed are you?")
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def home():
    form = InforForm()
    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ''
        return render_template('index.html',form=form,breed=breed)
    return render_template('index.html',form=form)

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)