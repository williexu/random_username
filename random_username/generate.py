import os
import random

class UsernameGenerator(object):
    _instance = None
    _adjectives = []
    _nouns = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UsernameGenerator, cls).__new__(cls)
            directory_path = os.path.dirname(__file__)
            with open(os.path.join(directory_path, 'data', 'adjectives.txt'), 'r') as file_adjective:
                with open(os.path.join(directory_path, 'data', 'nouns.txt'), 'r') as file_noun:
                    for line in file_adjective:
                        cls._adjectives.append(line.strip())
                    for line in file_noun:
                        cls._nouns.append(line.strip())
        return cls._instance

    def generate_username(self):
        adjective = random.choice(self._adjectives)
        noun = random.choice(self._nouns).capitalize()
        number = str(random.randrange(10))
        return adjective + noun + number

    def generate_usernames(self, num_results=1):
        return [self.generate_username() for _ in range(num_results)]
