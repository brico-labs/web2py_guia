# -*- coding: utf-8 -*-

db.define_table('provider',
    Field('id', 'integer'),
    Field('name', 'string'),
    Field('cif', 'string'),
    Field('email', 'string'),
    Field('phone', 'string'),
    migrate = True);


db.define_table('thing',
    Field('id', 'integer'),
    Field('name', 'string', requires = IS_NOT_EMPTY(error_message='cannot be empty')),
    Field('description', 'string'),
    Field('qty', 'integer', default=1, label=T('Quantity')),
    Field('picture', 'upload'),
    Field('created_on', 'datetime'),
    Field('provider_id', 'reference provider',
          requires=IS_EMPTY_OR(IS_IN_DB(db, 'provider.id', '%(name)s'))),
    format='%(name)s',
    migrate = True);
