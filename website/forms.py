from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

class ContactForm(FlaskForm):
    name = StringField(label="Il tuo nome:")
    email = StringField(label="La tua email")
    subject = StringField(label="Subject")
    message = TextAreaField(label="Il tuo messaggio")
    submit = SubmitField("Send")
