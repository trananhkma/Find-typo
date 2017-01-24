#!/usr/bin/python
import json
import os
import string


def make_dict_from_file(fname):
    DICT = {}
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if line.startswith('('):
                continue
            key = ' ' + line.split('(')[0]
            value = line.split('(')[1].split(')')[0]
            DICT[key] = value
    return DICT


def make_json():
    lst = []
    for name in string.lowercase:
        DICT = make_dict_from_file(name + '.txt')
        fname = '%s.json' % name
        with open(fname, 'w') as f:
            json.dump(DICT, f, sort_keys=True)
        lst.append(fname)
    return lst


def make_grep(result):
    with open(result) as f:
        d = json.load(f)
    keys = ''
    for key in d:
        keys += key + '\|'
    keys = keys[:-2]
    grep = """grep -rn " """ + keys + """ " |grep 'rst\|md'|grep -v java|grep -v css| grep -v 'js:'| grep -v tox| grep -v json |grep -v html | grep " """ + keys + '"'
    name = 'grep_%s.sh' % result
    with open(name, 'w') as f:
        f.write('#!/bin/bash\n\n')
        f.write(grep)


def main():
    lst = make_json()
    for f in lst:
        make_grep(f)


if __name__ == '__main__':
    main()
