# tryton-demo/party_custom/__init__.py
from trytond.pool import Pool

from . import party

__all__ = ['register']

def register(module):
    Pool.register(
        party.Party,
        module=module, 
        type_='model')