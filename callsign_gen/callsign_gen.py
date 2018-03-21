import os


def main():
    ac_dict = {}
    ac_type = []

    file = os.path.join(os.path.dirname(__file__), 'callsign_data.txt')
    with open(file, encoding='utf8') as src:
        for line in src:
            temp_list = line.split()
            try:
                if '-' in temp_list[1]:
                    try:
                        if temp_list[1] in ac_dict:
                            ac_dict[temp_list[1]].append(temp_list[0])
                        else:
                            ac_dict[temp_list[1]] = [temp_list[0]]
                    except KeyError:
                        continue
                elif '-' in temp_list[2]:
                    ac_type.append(temp_list[2])
            except IndexError:
                continue
            # Parse AC Type
            # if ac in line:
                # dest.write("\'{0}\',\n".format(line.rstrip('\n')))

    src.close()
    # dest.close()
    ac_type = set(ac_type)
    print(ac_dict)


if __name__ == '__main__':
    main()
