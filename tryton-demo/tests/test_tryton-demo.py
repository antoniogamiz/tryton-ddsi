import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class Tryton-DemoTestCase(ModuleTestCase):
    'Test Tryton-Demo module'
    module = 'tryton-demo'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            Tryton-DemoTestCase))
    return suite
