from model import Creature

_creatures = [
    Creature(
        name='Vampire',
        country='Africa',
        area='Amazone',
        description='vampires feed on the living to remain immortal',
        aka='Immortal'

    ),
    Creature(
        name='Zombie',
        country='UK',
        area='London',
        description='these shambling corpses have only one desire: to consume human flesh.',
        aka='Haitian folklore'
    )
]

def get_creatures() -> list[Creature]:
    return _creatures