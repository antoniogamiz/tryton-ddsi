from trytond.pool import Pool

from . import party

def register(module):
    Pool.register(
        party.Party,
        module=module, 
        type_='model')