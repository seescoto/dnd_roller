import Attribute


class Character:

    strength: Attribute
    dexterity: Attribute
    constitution: Attribute
    intelligence: Attribute
    wisdom: Attribute
    charisma: Attribute

    proficiency_bonus: int
    initiative_bonus: int

    proficiencies: list[str] = []

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
        self.strength = Attribute(strength)

    def set_dexterity(self, dexterity: int) -> None:
        self.dexterity = Attribute(dexterity)

    def set_constitution(self, constitution: int) -> None:
        self.constitution = Attribute(constitution)

    def set_intelligence(self, intelligence: int) -> None:
        self.intelligence = Attribute(intelligence)

    def set_wisdom(self, wisdom: int) -> None:
        self.wisdom = Attribute(wisdom)

    def set_charisma(self, charisma: int) -> None:
        self.charisma = Attribute(charisma)

    def set_proficiency_bonus(self, proficiency_bonus: int) -> None:
        self.proficiency_bonus = proficiency_bonus

    def set_initiative_bonus(self, initiative_bonus: int) -> None:
        self.initiative_bonus = initiative_bonus

    def add_proficiency(self, skill: str) -> None:
        self.proficiencies.append(skill)
