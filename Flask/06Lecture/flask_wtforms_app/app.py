from flask import Flask, render_template
from forms import UserForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    name = None
    email = None

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        form.name.data = ''
        form.email.data = ''
    
    return render_template('index.html', form=form, name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)




# https://flask-wtf.readthedocs.io/en/1.2.x/