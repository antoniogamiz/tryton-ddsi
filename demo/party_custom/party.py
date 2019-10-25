# tryton-demo/party_custom/party.py
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Party']

class Party(metaclass=PoolMeta):
    __name__= 'party.party'
    tumfield = fields.Char("TUM field")