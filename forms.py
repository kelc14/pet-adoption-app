from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, RadioField, TextAreaField

from wtforms.validators import NumberRange, Optional, URL, InputRequired, Length

class PetForm(FlaskForm):
    """Form for adding new pets."""

    name = StringField("Pet Name", 
                       validators=[InputRequired()])
    species = SelectField("Pet Species", 
                          choices=[('', 'Select Pet Species'),("Cat", 'Cat'), ('Dog', 'Dog'), ('Porcupine', 'Porcupine')], 
                          validators=[InputRequired()])
    photo_url = StringField("Pet Photo (URL)", 
                            validators=[Optional(), URL()])
    age = IntegerField("Pet Age", 
                       validators=[Optional(), NumberRange(min=0, max=30, message="Please enter the age in years.")])
    notes = TextAreaField("Pet Notes")
    available=RadioField('Available', 
                         choices=[('t','Yes'),('f','No')])

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Pet Photo (URL)", 
                            validators=[Optional(), URL()])
    notes = TextAreaField("Pet Notes", validators=[Optional(), Length(min=10)])
    available=RadioField('Available', 
                         choices=[('t','Yes'),('f','No')])
