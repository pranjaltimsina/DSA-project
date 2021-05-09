import curses
from curses import wrapper
import sys
import fuzzy
import trie

import timeit
import datetime

"""
NOTE: All coordinates are in the format (y, x) because that's how curses works)
"""


def validate_key(c: int):
    invalids = [
            10,
            263,
            262,
            360,
            331,
            339,
            330,
            338,
            258,
            259,
            260,
            261,
            410,
            343,
            575,
            580,
            579,
            577
            ]
    invalids += range(265, 275)
    decoded = curses.keyname(c).decode('utf-8')
    if (c in invalids or decoded.startswith('^') and not decoded.startswith('^[')):
        return False
    else:
        return True


def main(s):
    '''
    * s is the whole screen as an object
    * Main function wrapped by wrapper so that terminal doesn't get messed up
    * by accident
    '''

    # Accept path as command line argument
    try:
        path = sys.argv[1]
    except IndexError:
        path = None 

    # Make the trie
    # trie.main returns list of all possible paths
    file_list = trie.main(path)

    sh, sw = s.getmaxyx()  # Get the height, and width of the terminal

    s.clear()  # Clear the terminal
    curses.raw()  # Get raw input from the keyboard
    curses.echo()  # Echo the input keys to the screen
    curses.nl()  # Set enter to correspond to new line

    # Create a title box with height 2 rows and width 100%, starting at 1, 0
    title_box = s.subwin(2, sw-7, 1, 3)
    title_box.addstr('Directory searching using Trie, fuzzysearch and DFS', curses.A_REVERSE)
    title_box.chgat(-1, curses.A_REVERSE)  # That sweet background on the title
    title_box.hline(1, 0, '-', sw-7)

    # Create a search box of height 2 rows, width 100 at 3, 0
    search_box = s.subwin(2, sw, 3, 0)
    search_box.addstr('   Search: ')
    search_box.hline(1, 3, '-', sw-7)

    # The output box that covers the rest of the screen
    output_box = s.subwin(sh-5, sw-3, 5, 3)
    output_box.addstr('Results:\nTo find, you must seek')

    # Instructions the bottom of the screen
    s.addstr(sh-1, 3, 'Start typing to search! Press <ESC> to exit.')

    input_x = 11  # The x coordinate of the cursor
    full_string = ""  # full_string is the search query

    # Store the output here, edit line 86 to format things appropriately

    # Main loop
    while True:
        # Get a character from the keyboard
        c = s.getch(3, input_x)
        if (c in [263, 127] and not input_x == 11):
            # Check if backspace and not empty string
            input_x -= 1  # Decrement cursors x-coordinate
            full_string = full_string[:-1]  # Remove last char of search query
            s.delch(3, input_x)  # Remove the character from the screen
            output_box.clear()  # Clear the output box
        elif not validate_key(c):
            continue

        elif not chr(c) == "\n":
            # Add the chr to the search query and increment cursor position
            full_string += chr(c)
            input_x += 1

        counter = 0
        matches = []

        start_time = timeit.default_timer()
        # Performing fuzzy search on each file in file system
        for file in file_list:
            file_name = file.split('/')[-1]
            if ('.' in file_name):
                out = fuzzy.fuzzy_match(full_string, file_name)
                if out[0]:
                    counter += 1
                    matches.append((out[1], file_name,
                                    "/".join(file.split('/')[:-1])))
        end_time = timeit.default_timer()
        time_taken = f"{counter} matches in {(end_time - start_time) * 1000} ms"
        if counter > sh - 8:
            matches = matches[:sh-7]
        if (not full_string == "" and not matches == []):
            # Clear the output box and add the matches
            output_box.clear()
            with open('log.txt', 'a') as log:
                for match in matches:
                    log.write(f"| {datetime.datetime.now():>20} | {match[0]:>4} | {match[1]}")
                    try:
                        output_box.addstr(f'{match[0]:>4} | {match[1]}\n')
                        log.write(f"\n")
                    except:
                        log.write(f" | FAILED\n")

            output_box.addstr(time_taken)

        elif (full_string == ""):
            # Message if there is no input
            output_box.clear()
            output_box.addstr('To find, you must seek')

        else:
            # Message if there are no matches
            output_box.clear()
            output_box.addstr('What you seek for lies beyond the realms of possibility')

        # refreesh all boxes
        search_box.refresh()
        output_box.refresh()
        s.refresh()

        # since everything cleared, the message at bottom needs to be written
        s.addstr(sh-1, 3, 'Start typing to search! Press <ESC> twice to exit.')

        if (c == 27):
            # Quit if <ESC> is pressed
            curses.endwin()
            break


wrapper(main)
