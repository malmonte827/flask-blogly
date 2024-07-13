from unittest import TestCase

from app import app
from models import db, User

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgreql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class UserViewsTestCase(TestCase):
    """ Tests for views for Users """

    def setUp(self):
        """ add sample user """
        User.query.delete()

        user = User(first_name='Bill', last_name='Cipher', image_url="https://www.freeiconspng.com/uploads/name-people-person-user-icon--icon-search-engine-1.png")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id
    
    def tearDown(self):
        """ Clean up any failed insertions """
        db.session.rollback()
    
    def test_show_users(self):
        with app.test_client() as client:
            res = client.get('/users')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('Bill', html)

    def test_show_user_details(self):
        with app.test_client() as client:
            res = client.get(f"/{self.pet_id}")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Bill Cipher</h1>', html)

    def test_create_user(self):
        with app.test_client() as client:
            info = {'first_name': 'Peter', 'last_name': 'Parker', 'image_url': 'https://www.freeiconspng.com/uploads/name-people-person-user-icon--icon-search-engine-1.png'}
            res = client.post('/users/new', data=info, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('Peter Parker', html)