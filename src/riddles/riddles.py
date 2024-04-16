import random

class RiddleSource:
    """Class to manage riddle data with caching."""
    def __init__(self, data) -> None:
        """Initialize with riddle data and a cache for storing riddles."""
        self.data = data
        self.cache = []
        self.cache_index = 0

    def get_riddle(self) -> dict:
        """Randomly select and return a single riddle as a dictionary."""
        if self.cache_index < len(self.cache):
            riddle = self.cache[self.cache_index]
            self.cache_index += 1
            return riddle
        else:
            question, answer = random.choice(list(self.data.items()))
            return {'question': question, 'answer': answer}

    def get_riddles(self, count: int) -> list[dict]:
        """Retrieve multiple riddles, with caching and limit checking."""
        if count > len(self.data):
            raise ValueError("Requested count exceeds available number of unique riddles.")

        if self.cache_index + count <= len(self.cache):
            riddles = self.cache[self.cache_index:self.cache_index + count]
            self.cache_index += count
            return riddles
        else:
            self.cache = random.sample(list(self.data.items()), min(2 * count, len(self.data)))
            self.cache = [{'question': q, 'answer': a} for q, a in self.cache]
            self.cache_index = 0
            return self.get_riddles(count)

