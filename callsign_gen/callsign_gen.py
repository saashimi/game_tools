"""A script to parse known callsigns by aircraft type"""

import os
import pprint


def callsign_one_word(dict_in, lst_in):
    """
    Adds one-word callsigns to aircraft dictionary
    Args:
        dict_in: an aircraft dictionary
        lst_in: a temporary list of strings from the aircraft callsign input
                file
    returns: None
    """
    if lst_in[1] in dict_in:
        dict_in[lst_in[1]].append(lst_in[0])
    else:
        dict_in[lst_in[1]] = [lst_in[0]]


def callsign_two_words(dict_in, lst_in):
    """
    Adds two-word callsigns to aircraft dictionary
    Args:
        dict_in: an aircraft dictionary
        lst_in: a temporary list of strings from the aircraft callsign input
                file
    returns: None
    """
    if lst_in[2] in dict_in:
        dict_in[lst_in[2]].append(lst_in[0])
    else:
        dict_in[lst_in[2]] = [''.join(lst_in[0] + ' ' + lst_in[1])]


def main():
    ac_dict = {}

    file = os.path.join(os.path.dirname(__file__), 'callsign_data.txt')
    with open(file, encoding='utf8') as src:
        for line in src:
            temp_list = line.split()
            try:
                if '-' in temp_list[1]:
                    temp_list[1] = temp_list[1].replace(',', '')
                    callsign_one_word(ac_dict, temp_list)

                elif '-' in temp_list[2]:
                    temp_list[2] = temp_list[2].replace(',', '')
                    callsign_two_words(ac_dict, temp_list)
            except IndexError:
                print("There was an index error")
                continue

    for ac in ac_dict:
        ac_dict[ac] = set(ac_dict[ac])

    src.close()
    pprint.pprint(ac_dict)


if __name__ == '__main__':
    main()
