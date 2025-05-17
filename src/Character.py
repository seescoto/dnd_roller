from mimetypes import init
from xml.dom.minidom import Attr
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
                       charisma: int):
        self.set_strength(strength)
        self.set_dexterity(dexterity)
        self.set_constitution(constitution)
        self.set_intelligence(intelligence)
        self.set_wisdom(wisdom)
        self.set_charisma(charisma)

    def set_strength(self, strength: int):
        self.strength = Attribute(strength)

    def set_dexterity(self, dexterity: int):
        self.dexterity = Attribute(dexterity)

    def set_constitution(self, constitution: int):
        self.constitution = Attribute(constitution)

    def set_intelligence(self, intelligence: int):
        self.intelligence = Attribute(intelligence)

    def set_wisdom(self, wisdom: int):
        self.wisdom = Attribute(wisdom)

    def set_charisma(self, charisma: int):
        self.charisma = Attribute(charisma)

    def set_proficiency_bonus(self, proficiency_bonus: int):
        self.proficiency_bonus = proficiency_bonus

    def set_initiative_bonus(self, initiative_bonus: int):
        self.initiative_bonus = initiative_bonus

    def add_proficiency(self, skill: str):
        self.proficiencies.append(skill)
