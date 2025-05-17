class Attribute:

    score: int
    modifier: int

    def __init__(self, score: int) -> None:
        self.set_score(score)

    def set_score(self, score: int) -> None:
        self.score = score
        self.modifier = score//2

    def get_score(self) -> int:
        return self.score

    def get_modifier(self) -> int:
        return self.modifier
