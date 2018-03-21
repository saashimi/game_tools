"""A script to parse known callsigns by aircraft type"""
import os
import pprint


def main():
    ac_dict = {}

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
                """
                elif '-' in temp_list[2]:
                    part1, part2 = temp_list[0], temp_list[1]
                    ac_dict[temp_list[2]] = ''.join(part1 + part2)
                """
            except IndexError:
                continue

    for ac in ac_dict:
        ac_dict[ac] = set(ac_dict[ac])

    src.close()
    pprint.pprint(ac_dict)


if __name__ == '__main__':
    main()
