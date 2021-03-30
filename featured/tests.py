from django.test import TestCase
from .models import FeaturedPost

class FeaturedTestCase(TestCase):
    def setUp(self):
        FeaturedPost.object.create(title="testFeatured",price="99", slug="testfeatured")

    def test_featured_status(self):
        """Make sure status isnt published"""
        featuredPost = FeaturedPost.objects.get(title="testFeatured")
        self.assertEqual(featuredPost.status(), 0)