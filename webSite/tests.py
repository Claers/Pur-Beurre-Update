"""
Tests for the webSite app
"""

from django.core import mail
from django.urls import reverse, NoReverseMatch
from django.test import TestCase, Client
from .models import Product, Category
from django.contrib.auth.models import User

# Create your tests here.


class ProductModelTest(TestCase):
    """
    Tests for the product model
    """

    def test_string_representation(self):
        """
        Test the return of the product model
        """
        product = Product(productName="Pizza")
        self.assertEqual(str(product), product.productName)


class TestSearch(TestCase):
    """
    Tests for the searchs functionnalities
    """

    def test_search_one_object(self):
        """
        Test one object search
        """
        client = Client()
        Product.objects.create(productName="Test")
        response = client.post(
            '/search', {"product_name": "Test"}, follow=True)
        self.assertContains(response, "Test")

    def test_find_substitute(self):
        """
        Test substitute search in the same category
        """
        client = Client()
        obj1 = Product.objects.create(
            productName="Test", productURL="http://test.com")
        obj2 = Product.objects.create(
            productName="Test2", productURL="http://test2.com")
        category = Category.objects.create(categoryName="categoryTest")
        category.products.add(obj1)
        category.products.add(obj2)
        response = client.post(
            '/search', {"product_name": "Test2"}, follow=True)
        self.assertEqual(
            response.context['products_by_category']['categoryTest'][0], obj1)


class TestAuth(TestCase):
    """
    Tests for the auth functionnalities
    """

    def setUp(self):
        """The set up for tests
        """

        self.client = Client()
        User.objects.create_user(username="test",
                                 password="test",
                                 email="test@test.com")

    def test_create_account(self):
        """
        Test for create a account
        """

        self.client.post(
            '/connexion', {"username": "teste", "email": "test@test.com",
                           "password": "teste"}, follow=True)
        assert (self.client.session['_auth_user_id'])

    def test_logout(self):
        """
        Test for logout user
        """
        self.client.post(
            '/deconnexion', follow=True
        )
        self.assertRaises(
            KeyError, lambda: self.client.session['_auth_user_id'])

    def test_login(self):
        """
        Test for login user
        """
        self.client.post(
            '/connexion', {"username": "test", "password": "test",
                           "connect": "true"}, follow=True)
        assert (self.client.session['_auth_user_id'])

    def test_login_error(self):
        """
        Test for error in loggin with a bad password
        """

        self.client.post(
            '/connexion', {"username": "test", "password": "testesfqsf",
                           "connect": "true"}, follow=True)
        self.assertRaises(
            KeyError, lambda: self.client.session['_auth_user_id'])

    def test_password_reset_mail_send(self):
        """
        Test for email sending
        """
        response = self.client.post('/password_reset/',
                                    {"email": "test@test.com"}, follow=True)
        self.assertContains(response, "mot de passe")
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject,
                         'PurBeurre Recuperation du mot de passe')

    def test_password_reset(self):
        """
        Test for email sending
        """
        response = self.client.post('/password_reset/',
                                    {"email": "test@test.com"}, follow=True)
        self.assertEqual(len(mail.outbox), 1)
        url = mail.outbox[0].body.split()[15]
        uidb64 = url.split('/')[4]
        token = url.split('/')[5]
        response = self.client.get(
            reverse(
                "password_reset_confirm", args=(uidb64, token)), follow=True)
        self.assertContains(response, "Changer votre mot de passe")
        response = self.client.post(reverse(
            "password_reset_confirm", args=(uidb64, "set-password")),
            {"new_password1": "retest1234",
             "new_password2": "retest1234"},
            follow=True)
        self.assertContains(response, "mot de passe à été réinitialisé")
        self.client.post(
            '/connexion', {"username": "test", "password": "retest1234",
                           "connect": "true"}, follow=True)
        assert (self.client.session['_auth_user_id'])
