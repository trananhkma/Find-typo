#!/bin/bash

grep -rn "  XBox \| X-Box  " |grep 'rst\|md'|grep -v java|grep -v css| grep -v 'js:'| grep -v tox| grep -v json |grep -v html | grep "  XBox \| X-Box "