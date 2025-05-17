class Attribute:

    score: int
    modifier: int

    def __init__(self, score: int):
        self.set_score(score)

    def set_score(self, score: int):
        self.score = score
        self.modifier = score//2

    def get_score(self):
        return self.score

    def get_modifier(self):
        return self.modifier
