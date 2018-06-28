from mongoengine import Document, queryset_manager
from mongoengine.fields import (
    DateTimeField, StringField
)
from datetime import datetime

class Posts(Document):
    meta = {'collection': 'posts'}
    title = StringField()
    content = StringField()
    date = DateTimeField(default=datetime.utcnow)
