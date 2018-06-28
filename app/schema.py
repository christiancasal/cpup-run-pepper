import graphene
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Posts as PostsModel

class Posts(MongoengineObjectType):
    class Meta:
        model = PostsModel

class Query(graphene.ObjectType):
    posts = graphene.List(Posts)

    def resolve_posts(self, args):
        return list(PostsModel.objects.all())

schema = graphene.Schema(query=Query, types=[Posts])
