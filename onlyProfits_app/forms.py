from django import forms
from django.forms import fields as django_fields

class UserForm(forms.ModelForm):
    def test_user_form_fields(self):
        form = UserForm()
        fields = form.fields
        expected_fields = {'username': django_fields.CharField, 'email': django_fields.EmailField, 'password': django_fields.CharField}

        for field in expected_fields:
            expected_field = expected_fields[field]
            self.assertTrue(field in fields.keys())
            self.assertEqual(expected_field, type(fields[field]))
