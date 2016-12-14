def generate():

    ac_type = ['A-10', 'AH-64', 'B-1', 'B-2', 'C-17', 'C-130', 'E-4', 'F-5', 
                'F-15', 'F-16', 'F-22', 'KC-135',  'P-3', 'RC-12', 'T-6', 'T-38',
                ]

    for ac in ac_type:
        with open('callsign_data.txt', 'r') as src:
            with open('{0}.py'.format(ac), 'w') as dest:
                for line in src:
                    #Parse AC Type
                    if ac in line:
                        dest.write("\'{0}\',\n".format(line.rstrip('\n')))

    src.close()
    dest.close()

generate()
    