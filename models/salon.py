from framework.models import Model


class Salon(Model):
    file = "salon.json"

    def __init__(self, id, location, name, director_id):
        self.id = id
        self.location = location
        self.name = name
        self.director_id = director_id
