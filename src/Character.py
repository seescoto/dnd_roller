from src.CharAttribute import CharAttribute
from src.Rolls import roll_d20


class Character:

    strength: CharAttribute
    dexterity: CharAttribute
    constitution: CharAttribute
    intelligence: CharAttribute
    wisdom: CharAttribute
    charisma: CharAttribute

    proficiency_bonus: int
    initiative_bonus: int

    proficiencies: list[str]

    def __init__(self) -> None:
        self.proficiencies = []

    def set_attributes(self,
                       strength: int,
                       dexterity: int,
                       constitution: int,
                       intelligence: int,
                       wisdom: int,
                       charisma: int) -> None:
        self.set_strength(strength)
        self.set_dexterity(dexterity)
        self.set_constitution(constitution)
        self.set_intelligence(intelligence)
        self.set_wisdom(wisdom)
        self.set_charisma(charisma)

    def set_strength(self, strength: int) -> None:
        self.strength = CharAttribute(strength)

    def set_dexterity(self, dexterity: int) -> None:
        self.dexterity = CharAttribute(dexterity)

    def set_constitution(self, constitution: int) -> None:
        self.constitution = CharAttribute(constitution)

    def set_intelligence(self, intelligence: int) -> None:
        self.intelligence = CharAttribute(intelligence)

    def set_wisdom(self, wisdom: int) -> None:
        self.wisdom = CharAttribute(wisdom)

    def set_charisma(self, charisma: int) -> None:
        self.charisma = CharAttribute(charisma)

    def set_proficiency_bonus(self, proficiency_bonus: int) -> None:
        self.proficiency_bonus = proficiency_bonus

    def set_initiative_bonus(self, initiative_bonus: int) -> None:
        self.initiative_bonus = initiative_bonus

    def set_proficiencies(self, proficiencies: dict[str, bool]) -> None:
        prof_strings = ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics',
                        'Deception', 'History', 'Insight', 'Intimidation',
                        'Investigation', 'Medicine', 'Nature', 'Perception',
                        'Performance', 'Persuasion', 'Religion', 'Sleight of Hand',
                        'Stealth', 'Survival',
                        'Strength', 'Dexterity', 'Constitution', 'Intelligence',
                        'Wisdom', 'Charisma']
        for prof in prof_strings:
            has_prof = proficiencies.get(prof, False)  # default value is false
            if has_prof:
                self.add_proficiency(prof)

    def add_proficiency(self, skill: str) -> None:
        self.proficiencies.append(skill)

    def roll_skill(self, skill: str) -> tuple[int]:
        str_skills = ['Athletics', 'Strength']
        dex_skills = ['Acrobatics', 'Sleight of Hand', 'Stealth', 'Dexterity']
        con_skills = ['Constitution']
        int_skills = ['Arcana', 'History',
                      'Investigation', 'Nature', 'Religion', 'Intelligence']
        wis_skills = ['Animal Handling', 'Insight',
                      'Medicine', 'Perception', 'Survival', 'Wisdom']
        cha_skills = ['Deception', 'Intimidation',
                      'Performance', 'Persuasion', 'Charisma']

        bonus = 0
        if skill in str_skills:
            bonus = self.strength.modifier
        elif skill in dex_skills:
            bonus = self.dexterity.modifier
        elif skill in con_skills:
            bonus = self.constitution.modifier
        elif skill in int_skills:
            bonus = self.intelligence.modifier
        elif skill in wis_skills:
            bonus = self.wisdom.modifier
        elif skill in cha_skills:
            bonus = self.charisma.modifier

        if skill in self.proficiencies:
            bonus += self.proficiency_bonus

        roll = roll_d20()
        return (roll, roll+bonus)

    def roll_ability(self, ability: str) -> tuple[int]:
        if ability == "Strength":
            bonus = self.strength.modifier
        elif ability == "Dexterity":
            bonus = self.dexterity.modifier
        elif ability == "Constitution":
            bonus = self.constitution.modifier
        elif ability == "Intelligence":
            bonus = self.intelligence.modifier
        elif ability == "Wisdom":
            bonus = self.wisdom.modifier
        elif ability == "Charisma":
            bonus = self.charisma.modifier
        else:
            bonus = 0  # Default case

        roll = roll_d20()
        return (roll, roll + bonus)

    def roll_initiative(self):
        roll = roll_d20()
        return (roll, roll + self.initiative_bonus)

    def get_ability_score(self, ability: str) -> int:
        if ability == "Strength":
            bonus = self.strength.score
        elif ability == "Dexterity":
            bonus = self.dexterity.score
        elif ability == "Constitution":
            bonus = self.constitution.score
        elif ability == "Intelligence":
            bonus = self.intelligence.score
        elif ability == "Wisdom":
            bonus = self.wisdom.score
        elif ability == "Charisma":
            bonus = self.charisma.score
        else:
            bonus = 0  # Default case

        return bonus


def create_character(stats: dict[str, int], proficiencies: list[str]) -> Character:
    char = dict_to_character(stats)
    for prof in proficiencies:
        char.add_proficiency(prof)

    return char


def character_to_dict(char: Character) -> dict[str, int]:
    d = {}
    d["strength"] = char.strength.score
    d["dexterity"] = char.dexterity.score
    d["constitution"] = char.constitution.score
    d["intelligence"] = char.intelligence.score
    d["wisdom"] = char.wisdom.score
    d["charisma"] = char.charisma.score

    d["proficiency_bonus"] = char.proficiency_bonus
    d["initiative_bonus"] = char.initiative_bonus

    return d


def dict_to_character(d: dict[str, int]) -> Character:
    char = Character()
    char.set_attributes(d["strength"], d["dexterity"], d["constitution"],
                        d["intelligence"], d["wisdom"], d["charisma"])
    char.set_proficiency_bonus(d["proficiency_bonus"])
    char.set_initiative_bonus(d["initiative_bonus"])

    return char
