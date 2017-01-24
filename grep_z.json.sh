#!/bin/bash

grep -rn "  zeebra \| Ziegfield Follies  " |grep 'rst\|md'|grep -v java|grep -v css| grep -v 'js:'| grep -v tox| grep -v json |grep -v html | grep "  zeebra \| Ziegfield Follies "