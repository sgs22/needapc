from django.test import TestCase

class ViewTest(TestCase):
    def test_view_render(self):
        """
        Test to see if the page renders correctly and doenst give a 404 but 200.
        """
        response = self.client.get('blog:blog') #change to page wanting to request
        self.assertEqual(response.status_code, 200)