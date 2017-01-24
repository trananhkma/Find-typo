#!/usr/bin/python
import json
import os
import string


DICT = {}


def make_dict_from_file(fname):
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if line.startswith('('):
                continue
            key = line.split('(')[0].strip()
            value = line.split('(')[1].split(')')[0]
            DICT[key] = value


def make_json():
    for name in string.lowercase:
        make_dict_from_file(name + '.txt')
    
    with open('result.json', 'w') as f:
        json.dump(DICT, f, sort_keys=True)


def make_grep(result):
    with open(result) as f:
        d = json.load(f)
    keys = ''
    for key in d:
        keys += key + '\|'
    keys = keys[:-2]
    grep = """grep -rn " """ + keys + """ " |grep 'py\|rst\|md'| grep " """ + keys + '"'
    with open('grep_cmd.sh', 'w') as f:
        f.write('#!/bin/bash\n\n')
        f.write(grep)


def main():
    if not os.path.isfile('result.json'):
        make_json()
    make_grep('result.json')


if __name__ == '__main__':
    main()
