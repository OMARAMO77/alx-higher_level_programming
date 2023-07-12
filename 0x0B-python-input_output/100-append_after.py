#!/usr/bin/python3
"""append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each
    line containing a specific string
	
    Args:
        filename (str): name of file
        search_string (str): string to be searched
        new_string (str): string to be appended
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        content = "".join(lines)
        f.write(content)
