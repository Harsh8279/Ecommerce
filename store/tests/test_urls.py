from django.test import TestCase
from django.urls import reverse, resolve
from store.views import cart


# Create your tests here.

class UrlTest(TestCase):

    def testHomePage(self):
        # here we are going to check by using response code

        response = self.client.get('/')
        print(response)

        # if this type of url exists then it give that response 200 or else gives 404 status code

        self.assertEqual(response.status_code, 200)


    def testCartPage(self):
        # here we are going to check by using reverse and resolve

        url = reverse('cart')

        # printing the resolve method

        print("Resolve : ", resolve(url))

        # now we aew going to check fun name

        self.assertEquals(resolve(url).func, cart)