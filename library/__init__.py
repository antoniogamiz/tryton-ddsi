from trytond.pool import Pool
from .library import Book

def register():
    Pool.register(
        Book,
        module='library', type_='model'
    )