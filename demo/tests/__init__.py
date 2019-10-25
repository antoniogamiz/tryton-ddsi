try:
    from trytond.modules.demo.tests.test_demo import suite
except ImportError:
    from .test_demo import suite

__all__ = ['suite']
