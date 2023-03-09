from flask import Flask
from blueprints.user_routes import user_pages

app = Flask(__name__)
app.register_blueprint(user_pages)



if __name__ == '__main__':
    app.run()
    