from django.test import TestCase

from onlyProfits_app.forms import *


class UserFormTestCase(TestCase):
    
    def test_form_fields(self):
        form = UserForm()
        self.assertEqual(form.fields["username"].label, "Username")
        self.assertEqual(form.fields["password"].label, "Password")
        self.assertEqual(form.fields["email"].label, "Email")
