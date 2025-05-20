from src.Rolls import roll_d20


class CharAttribute:

    score: int
    modifier: int

    def __init__(self, score: int) -> None:
        self.set_score(score)

    def set_score(self, score: int) -> None:
        self.score = score
        self.modifier = (self.score - 10)//2

    def roll(self) -> tuple[int]:
        roll = roll_d20()
        total = roll + self.modifier
        return (roll, total)
