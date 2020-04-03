import sys

classes = []

class Application:
    def __init__(self, name=None):
        self.name = name or __name__
    
    def run(self):
        print(f"Welcome to {self.name}")
        return 0

def get_name():
    return __name__

