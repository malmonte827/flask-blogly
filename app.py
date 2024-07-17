"""Blogly application."""

from flask import Flask, render_template, redirect, request
from models import db, connect_db, User, Post, Tag, PostTag
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

################################################################################################
# User Routes

@app.route('/users')
def show_users():
    """ Shows all users """

    users = User.query.all()
    return render_template('users/users-list.html', users=users)

@app.route('/users/new')
def new_user_form():
    """ Shows a form to add new users """

    return render_template('users/create-user.html')

@app.route('/users/new', methods=['POST'])
def create_user():
    """ Handles form submission to create new user """
    new_user = User(
    first_name = request.form['first_name'],
    last_name = request.form['last_name'],
    image_url = request.form['image_url'] or None)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route( '/users/<int:user_id>' ) 
def show_user_details(user_id):
    """ Shows info on a specific user """

    user = User.query.get_or_404(user_id)
    return render_template('users/user-detail.html', user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """  Shows a form to edit user info """

    user = User.query.get_or_404(user_id)
    return render_template('users/edit-user.html', user=user)

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


################################################################################################
# Post Routes


@app.route('/users/<int:user_id>/posts/new')
def show_new_post_form(user_id):
    """ Shows a form to add new post """

    user = User.query.get_or_404(user_id)
    tags = Tag.query.all()
    return render_template('posts/new-post.html', user=user, tags=tags)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def new_post(user_id):
    """ Handles form submission for new post """

    user = User.query.get_or_404(user_id)
    tag_ids = [int(num) for num in request.form.getlist('tags')]
    tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
    new_post = Post(
    title = request.form['title'],
    content = request.form['content'],
    user=user,
    tags=tags)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/users/{user_id}')

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """ Shows post of specific user """

    post = Post.query.get_or_404(post_id)
    return render_template('posts/user-post.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    """ Shows a form to edit post """

    post = Post.query.get_or_404(post_id)
    tags = Tag.query.all()
    return render_template('posts/edit-post.html', post=post, tags=tags)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def update_post(post_id):
    """ Handles from submission to update post"""

    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    tag_ids = [int(num) for num in request.form.getlist('tags')]
    post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()

    db.session.add(post)
    db.session.commit()

    return redirect(f'/users/{post.user_id}')

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    """ Handles submission for deleting a post """

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(f'/users/{post.user_id}')

############################################################################################
# Tag Routes

@app.route('/tags')
def show_tags():
    """ Shows list of tags """

    tags = Tag.query.all()
    return render_template('tags/show.html', tags=tags)

@app.route('/tags/<int:tag_id>')
def show_tag_detail(tag_id):
    """ show posts associated with tag """

    tag = Tag.query.get_or_404(tag_id)
    return render_template('/tags/detail.html', tag=tag)

@app.route('/tags/new')
def show_new_tag_form():
    """ Shows form to create new tag """

    posts = Post.query.all()
    return render_template('tags/new-tag.html', posts=posts)

@app.route('/tags/new', methods=['POST'])
def new_tag():
    """ Handles submission for creating new tag """

    post_ids = [int(num) for num in request.form.getlist('posts')]
    posts = Post.query.filter(Post.id.in_(post_ids)).all()
    new_tag = Tag(name=request.form['name'],posts=posts)

    db.session.add(new_tag)
    db.session.commit()

    return redirect('/tags')

@app.route('/tags/<int:tag_id>/edit')
def edit_form(tag_id):
    """ Shows form to edit tag """

    tag = Tag.query.get_or_404(tag_id)
    posts = Post.query.all()
    
    db.session.add(tag)
    db.session.commit()

    return render_template('/tags/edit-tag.html', tag=tag, posts=posts)

@app.route('/tags/<int:tag_id>/edit', methods=['POST'])
def update_tag(tag_id):
    """ Handles submission of updated tag """

    tag = Tag.query.get_or_404(tag_id)
    tag.name = request.form['name']
    post_ids = [int(num) for num in request.form.getlist("posts")]
    tag.posts = Post.query.filter(Post.id.in_(post_ids)).all()

    db.session.add(tag)
    db.session.commit()

    return redirect('/tags')

@app.route('/tags/<int:tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):

    """ Handles submission for deleting a tag """

    tag = Tag.query.get_or_404(tag_id)

    db.session.delete(tag)
    db.session.commit()

    return redirect('/tags')