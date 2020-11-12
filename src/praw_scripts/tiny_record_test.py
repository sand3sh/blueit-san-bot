from tinydb import TinyDB, where, Query
from tinyrecord import transaction

db = TinyDB('db.json').table('table')
with transaction(db) as tr:
    # insert a new record
    tr.insert({'id': 'someid1'})
    # update records matching a query

postSubmitted = db.search(Query().id == 'someid1')
if len(postSubmitted) > 0:
    print('[ALREADY SUBMITTED] '+postSubmitted[0]['id'])

#print(db.all())