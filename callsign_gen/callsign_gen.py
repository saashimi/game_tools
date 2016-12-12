with open('callsign_data.txt', 'r') as src:
    with open('sorted_callsigns.txt', 'w') as dest:
        for line in src:
            #Parse fighters
            if "F/A" in line:
                dest.write("\'{0}\',\n".format(line.rstrip('\n')))


# Unit Tests 