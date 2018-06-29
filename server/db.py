from mongoengine import connect

db = connect(
    db='test',
    host='localhost',
    port=27017
)
