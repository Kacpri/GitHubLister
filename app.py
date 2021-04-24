from flask import Flask, render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='secret_key',
    CSRF_ENABLED=True,
))


class GitHubForm(FlaskForm):
    name = StringField(validators=[DataRequired()],
                       id='nameInput',
                       render_kw={'placeholder': 'Podaj nazwę'})

    type = RadioField(choices=[(0, 'Organizacja'), (1, 'Użytkownik')],
                      default=0,
                      validators=[DataRequired()],
                      id='typeInput')

    submit = SubmitField(label="Szukaj")


@app.route('/')
def home():
    form = GitHubForm(request.form)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
