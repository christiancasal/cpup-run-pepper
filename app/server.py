from flask import Flask, redirect, url_for
from flask_graphql import GraphQLView
from schema import schema
from db import init_db, db

app = Flask(__name__)

@app.route('/')
def redirect_to_graphQL():
    return redirect(url_for('graphql'))

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.close()

if __name__ == '__main__':
    app.run()
