from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms import TextField
from wtforms.validators import Email
from wtforms.validators import Required


class LoginForm(FlaskForm):
    email = TextField('E-mail', [Email(),
                                 Required(message = 'Esqueceu seu e-mail')])
    password = PasswordField('Senha', [
                                 Required(message = 'Senha é obrigatória')])
