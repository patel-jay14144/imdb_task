from flask_restful import Resource


class AddMoviesResource(Resource):

    def get(self):
        return "Hello World"
