# here we will define how turns work and how games are won.
# games are dependent on players and decks
# when called by main.py, a winner will be returned
# main.py can call multiple games inorder to simulate a tournament
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


# Usage
generator = UniqueRandomGenerator(1, 99)

# Generate some numbers
for _ in range(2):  # Change the range or use a different loop depending on your needs
    print(generator.generate_unique())

# This will keep generating unique numbers between 1 and 99 until all possibilities are exhausted.
