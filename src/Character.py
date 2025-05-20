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
        str_skills = ['Athletics']
        dex_skills = ['Acrobatics', 'Sleight of Hand', 'Stealth']
        int_skills = ['Arcana', 'History',
                      'Investigation', 'Nature', 'Religion']
        wis_skills = ['Animal Handling', 'Insight',
                      'Medicine', 'Perception', 'Survival']
        cha_skills = ['Deception', 'Intimidation', 'Performance', 'Persuasion']

        bonus = 0
        if skill in str_skills:
            bonus = self.strength.modifier
        elif skill in dex_skills:
            bonus = self.dexterity.modifier
        elif skill in int_skills:
            bonus = self.intelligence.modifier
        elif skill in wis_skills:
            bonus = self.wisdom.modifier
        elif skill in cha_skills:
            bonus = self.charisma.modifier

        if skill in self.proficiencies:
            bonus += self.proficiency_bonus

        roll = roll_d20
        return (roll, roll+bonus)
