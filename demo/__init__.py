# tryton-demo/__init__,py
from trytond.pool import Pool

from . import party_custom

__all__ = ['register']

def register():
    party_custom.register('demo')
