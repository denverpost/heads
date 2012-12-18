#!/usr/bin/python
# Convert text files, one entry per line, into
# javascript arrays. Concatenate arrays into
# per-property files. Properties are defined 
# by directory.

import os
import fnmatch


def txt_to_js(targets, *args, **kwargs):
    """Take a directory and convert text files inside into js arrays."""
    target_slugs = []
    for target in targets:
        target_slug = target.rsplit('.')[0].replace('-','_')
        target_slugs.append(target_slug)

        # Open the file, turn it into a javascript array, write the javascript
    

if __name__ == '__main__':
    os.chdir('/home/joe/work/heads/lists/denverpost/')
    targets = [item for item in os.listdir('.') if item.find('.txt') != -1]
    txt_to_js(targets)
