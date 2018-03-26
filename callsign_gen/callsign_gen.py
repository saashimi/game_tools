"""A script to parse known callsigns by aircraft type"""

import os
import re
import json


def hornet_parser(ac_in):
    """
    Handles all the wonderful naming variations the F/A-18 hornet
    """
    ac_in = 'F/A-18'
    return ac_in


def strip_model(ac_in, line_in):
    """
    Strip model designations from aircraft types
    e.g. ac_in = F-15A
    output = F-15
    """
    letter_desig = '^.*?-'
    regex = '(?<=-)(\d+)(\D+)'
    leader = re.search(letter_desig, ac_in)
    trailer = re.search(regex, ac_in)
    try:
        generic_ac = leader.group(0) + trailer.group(1)
        return generic_ac
    except AttributeError:
        # This catches ac_types that are already without a model designation
        # e.g., `F-15` vs `F-15A`
        try:
            regex = '(?<=-)(\d+)'
            trailer = re.search(regex, ac_in)
            generic_ac = leader.group(0) + trailer.group(1)
            return generic_ac
        except AttributeError:
            print(line_in, ac_in, "Not a valid aircraft type!")
            return


def callsign_handler(dict_in, lst_in, index, line_no_in):
    """
    Adds one-word callsigns to aircraft dictionary
    Args:
        dict_in: an aircraft dictionary
        lst_in: a temporary list of strings from the aircraft callsign input
                file
        index: The index position of the aircraft type designation
        line_no_in: The current line number in the raw callsign input file
    returns: None
    """
    lst_in[index] = lst_in[index].replace(',', '')
    lst_in[index] = strip_model(lst_in[index], line_no_in)
    if index == 1:
        if lst_in[1] in dict_in:
            dict_in[lst_in[1]].append(lst_in[0])
        else:
            dict_in[lst_in[1]] = [lst_in[0]]
    if index == 2:
        if lst_in[2] in dict_in:
            dict_in[lst_in[2]].append(lst_in[0])
        else:
            dict_in[lst_in[2]] = [''.join(lst_in[0] + ' ' + lst_in[1])]


def main():
    ac_dict = {}
    line_no = 0
    file = os.path.join(os.path.dirname(__file__), 'callsign_data.txt')
    writefile = os.path.join(os.path.dirname(__file__), 'ac_callsigns.json')
    with open(file, encoding='utf8') as src:
        for line in src:
            line_no += 1
            temp_list = line.split()         
            try:
                if '-' in temp_list[2]:
                    type_index = 2
                    callsign_handler(ac_dict, temp_list, type_index, line_no)
                    """
                    if 'F' in temp_list[2] and '18' in temp_list[2]:
                    """

                elif '-' in temp_list[1]:
                    type_index = 1
                    callsign_handler(ac_dict, temp_list, type_index, line_no)

            except IndexError:
                print("Skip line due to index error")
                continue

    for ac in ac_dict:
        ac_dict[ac] = set(ac_dict[ac])  # Remove duplicate entries
        ac_dict[ac] = [set_item for set_item in ac_dict[ac]]

    with open(writefile, 'w') as writeout:
        json.dump(ac_dict, writeout)

    src.close()


if __name__ == '__main__':
    main()
