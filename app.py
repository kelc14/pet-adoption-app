"""Pet Adoption application."""

from flask import Flask, redirect, render_template, flash
from models import db, connect_db, Pet
from sqlalchemy import desc

from forms import PetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = 'secret123!'
debug = DebugToolbarExtension(app)


@app.route('/')
def show_home():
    """Display ALL Pets on Homepage"""
    pets = Pet.query.order_by(desc(Pet.available)).all()
    
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def show_add_form():
    """Show Add Pet Form and handle updating database"""
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        available=form.available.data
        available = False if available == 'f' else True 

      
            
        pet = Pet(name=name, species=species, photo_url = photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        flash(f"Added {name}!")
        return redirect('/')

    else:
        return render_template('add_pet.html', form=form)
    
@app.route('/<int:id>', methods=["GET", "POST"])
def display_and_edit_pet(id):
    """display pet information and edit form for pet info"""
    pet = Pet.query.get_or_404(id)
    
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        available=form.available.data
        pet.available = False if available == 'f' else True 
        
        db.session.add(pet)
        db.session.commit()
        flash(f"Added {pet.name}!")
        return redirect('/')
    
    else:
        return render_template('edit_pet.html', form=form, pet=pet)