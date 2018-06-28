from mongoengine import connect, connection
from models import Posts
db = connect(
    db='test',
    host='localhost',
    port=27017
)

def init_db():
    posts = Posts(title="hello", content="world")
    posts.save()
