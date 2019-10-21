from trytond.model import ModelView, ModelSQL, fields

# list of all classes in the file
__all__ = ['Book']


class Book(ModelSQL, ModelView):
    # description (mandatory on first declaration)
    'Book'

    # Internal class name. Always used as a reference inside Tryton
    # default: '<module_name>.<class_name>' on Tryton
    # becomes '<module_name>_<class_name>' in the database
    __name__ = 'library.book'

    title = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    subject = fields.Char('Subject')
    abstract = fields.Text('Abstract')