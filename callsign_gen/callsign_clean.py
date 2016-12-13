F_15 = []
F_16 = []
FA_18 = []

def generate():

    with open('callsign_data.txt', 'r') as src:
        with open('sorted_callsigns.txt', 'w') as dest:

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
            
    return(F_15, F_16, FA_18)
    src.close()
    dest.close()

generate()
        #dest.write("\'{0}\',\n".format(line.rstrip('\n')))