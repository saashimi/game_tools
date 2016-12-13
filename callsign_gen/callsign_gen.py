with open('callsign_data.txt', 'r') as src:
    with open('sorted_callsigns.txt', 'w') as dest:
        F_15 = []
        F_16 = []
        FA_18 = []
        for line in src:
            #Parse fighters
            if "F-15" in line:
                cleaned = line.rstrip('\n')
                F_15.append(cleaned)
            if "F/A" in line:
                cleaned = line.rstrip('\n')
                FA_18.append(cleaned)
            if "F-16" in line:
                cleaned = line.rstrip('\n')
                F_16.append(cleaned)
        print(F_15, F_16, FA_18)
src.close()
dest.close()
        #dest.write("\'{0}\',\n".format(line.rstrip('\n')))