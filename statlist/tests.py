from statlist.views import home, profile, details, country, club
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
# Create your tests here.


# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)

    def test_club_url_resolves(self):
        url = reverse('club')
        self.assertEqual(resolve(url).func, club)

    def test_country_url_resolves(self):
        url = reverse('country')
        self.assertEqual(resolve(url).func, country)


class TestOtherUrls(TestCase):

    def test_details_url_resolves(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('profile')
        self.club_url = reverse('club')
        self.country_url = reverse('country')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statlist/profile.html')

    def test_club_GET(self):
        response = self.client.get(self.club_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statlist/club.html')

    def test_country_GET(self):
        response = self.client.get(self.country_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statlist/country.html')
