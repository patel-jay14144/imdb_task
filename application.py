from api import db
from create_app import create_app

application = create_app()

if __name__ == "__main__":
    application.run()
