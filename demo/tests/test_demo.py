import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class DemoTestCase(ModuleTestCase):
    'Test Demo module'
    module = 'demo'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            DemoTestCase))
    return suite
