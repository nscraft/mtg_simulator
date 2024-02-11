import random


class UniqueRandomGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.generated = set()

    def generate_unique(self):
        if len(self.generated) == (self.end - self.start + 1):
            raise Exception("All possible numbers have been generated.")

        while True:
            number = random.randint(self.start, self.end)
            if number not in self.generated:
                self.generated.add(number)
                return number
