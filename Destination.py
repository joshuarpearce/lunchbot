from Rating import Rating
import time

class Destination():
    def __init__(self):
        self.rating = Rating()
        self.history = []

    def add_visit(self, when = None):
        when_resolved = when
        if when_resolved is None:
            when_resolved = time.time()
        self.history.append(when_resolved)
