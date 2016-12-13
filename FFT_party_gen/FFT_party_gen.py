from males import male_names
from females import female_names
from monsters import monster_names, monster_types
import random

job_classes = ['Squire', 'Chemist', 'Black Mage', 'Time Mage', 'Summoner', 'White Mage',
    'Mystic', 'Orator', 'Arithmetician', 'Bard', 'Archer', 'Thief', 'Dragoon', 
    'Knight', 'Monk', 'Geomancer', 'Samurai', 'Ninja', 'Dancer', 'Dark Knight', 
    'Mime', 'Onion Knight']

rare_job_classes = ['Holy Knight', 'Machinist', 'Skyseer', 'Netherseer',
    'Divine Knight', 'Sword Saint', 'Knight Templar', 'Dragonkin', 'SOLDIER', 
    'Sky Pirate', 'Game Hunter']

party = []


def print_helper(member_in):
    """
    Correctly places 'a' or 'an' before appropriate monster type
    """
    vowels = ['A', 'E', 'I', 'O', 'U']
    if member_in[1][0] in vowels:
        print('{0}, an {1}.'.format(member_in[0], member_in[1]))
    else:
        print('{0}, a {1}.'.format(member_in[0], member_in[1]))

def main(): 
    for member in range(10):
        # Names should be unique
        random.shuffle(male_names)
        random.shuffle(female_names)
        random.shuffle(monster_names)
        random.shuffle(monster_types)
        random.shuffle(job_classes)
        random.shuffle(rare_job_classes)
        randomizer = random.randint(1, 10)
        if randomizer == 1: 
            character = (male_names[0], 'male', rare_job_classes[0])
        if randomizer == 2:
            character = (female_names[0], 'female', rare_job_classes[0])
        if randomizer in range(3, 9, 2):
            character = (male_names[0], 'male', job_classes[0])
        if randomizer in range(4, 9, 2):
            character = (female_names[0], 'female', job_classes[0])
        if randomizer == 9 or randomizer == 10:
            character = (monster_names[0], monster_types[0])
        party.append(character)

    for member in party:
        try:
            print('{0}, a {1} {2}.'.format(member[0], member[1], member[2]))
        except:
            print_helper(member)



if __name__=='__main__':
    main()
