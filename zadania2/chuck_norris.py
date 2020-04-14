import chucknorris.quips as q
import random

class ChuckNorris:
    def __init__(self, names):
        self.names = names
    
    def generate(self):
        return q.random(self.names[random.randint(0, len(self.names)-1)])