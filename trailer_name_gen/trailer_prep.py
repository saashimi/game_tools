"""
trailer_prep.py - A helper script to clean a list of trailer names
"""

def clean():
    with open('raw_names.txt', 'r') as src:
        with open('cleaned_names.txt', 'w') as dest:
            for line in src:
                dest.write('\"{0}\",\n'.format(line.rstrip('\n')))