from django.test import TestCase
from django.urls import reverse


class ViewTestCase(TestCase):
    
    def test_check_template(self):
        self.assertTemplateUsed(self.client.get("onlyProfits:/"), "onlyProfits_app/onlyProfits.html")
    
    def test_context_dictionary(self):
        # TODO: Write test to check context dictionary
        pass
