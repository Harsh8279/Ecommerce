from django.test import TestCase
from store.models import Product

class ModelTest(TestCase):

    def testProductModel(self):
        product = Product.objects.create(name="ToyCar", price=800)
        self.assertEquals(str(product), 'ToyCar')
        print("IsInstance : ",isinstance(product,Product))
        self.assertTrue(isinstance(product,Product))
        # here str() will call __str__ and in that we have return name of the toy
        # so we have compare it with name
