try:
    from trytond.modules.tryton-demo.tests.test_tryton-demo import suite
except ImportError:
    from .test_tryton-demo import suite

__all__ = ['suite']
