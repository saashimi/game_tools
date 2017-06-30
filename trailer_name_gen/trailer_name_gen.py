from trailer_names import names
import random

selected_names = []

def main(): 
    for number in range(21):
        # Names should be unique
        random.shuffle(names)
        selected_names.append(names[0])
    for name in selected_names:
        print name

main()