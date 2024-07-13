"""Blogly application."""

from flask import Flask, render_template, redirect, request
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'verysecret'

debug = DebugToolbarExtension(app)
connect_db(app)
db.create_all()

@app.route('/')
def homepage():
    """ Homepage redirects to list of users"""

    return redirect('/users')

@app.route('/users')
def show_users():
    """ Shows all users """

    users = User.query.all()
    return render_template('users-list.html', users=users)

@app.route('/users/new')
def new_user_form():
    """ Shows a form to add new users """

    return render_template('create-user.html')

@app.route('/users/new', methods=['POST'])
def create_user():
    """ Handles form submission to create new user """

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route( '/<int:user_id>' ) 
def show_user_details(user_id):
    """ Shows info on a specific user """

    user = User.query.get_or_404(user_id)
    return render_template('user-detail.html', user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """  Shows a form to edit user info """

    user = User.query.get_or_404(user_id)
    return render_template('edit-user.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):
    """ handles form submission to update user info """

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """ Handles form submission to delete a user """

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')