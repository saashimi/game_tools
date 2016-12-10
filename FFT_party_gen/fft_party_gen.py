files = ['female', 'male', 'monster']

for file in files:
    with open('{0}.txt'.format(file), 'r') as src:
        with open('{0}.txt'.format(file + '_edit'), 'w') as dest:
            for line in src:
                dest.write("\'{0}\',\n".format(line.rstrip('\n')))
