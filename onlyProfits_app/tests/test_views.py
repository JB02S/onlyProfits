from django.test import TestCase

class ViewTestCase(TestCase):
    @classmethod
    def setUp(self):
        pass
    
    def test_url_exists(self):
        # self.assertEquals(self.client.get(reverse("onlyProfits:/")).status_code, 200)
        self.assertEquals(self.client.get("onlyProfits:/").status_code, 200)
    
    def test_check_template(self):
        self.assertTemplateUsed(self.client.get("onlyProfits:/"), "templates/onlyProfits.html")
    
    def test_context_dictionary(self):
        # TODO: Write test to check context dictionary
        pass
