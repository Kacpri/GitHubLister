from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
from RepoLister import list_repos, sort_repos_by_stars

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


@app.route('/', methods=['GET', 'POST'])
def home():
    form = GitHubForm(request.form)
    if not form.name.data:
        return render_template('index.html', form=form)

    else:
        print(form.name.data)

        try:
            repos = list_repos(form.name.data, form.type.data)
        except Exception:
            error_message = 'Organizacja' if form.type.data == '0' else 'Użytkownik'
            error_message += ' nie istnieje'
            return render_template('index.html', form=form, error_message=error_message)

        if not repos:
            if form.type.data == '0':
                error_message = 'Organizacja nie posiada repozytoriów lub istnieje użytkownik o tej nazwie'
            else:
                error_message = 'Użytkownik nie posiada repozytoriów'
            return render_template('index.html', form=form, error_message=error_message)

        repos = sort_repos_by_stars(repos, True)
        return render_template('table.html', form=form, repos=repos)


if __name__ == '__main__':
    app.run()
