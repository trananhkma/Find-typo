#!/bin/bash

grep -rn "  yera \| yuonger \| yeasr \| yaht \| ytou \| yeild \| yelow \| Yorkhire \| ya'll \| youre \| yuo \| yaer \| yhe \| yersa \| yatch \| younge \| youself \| Yementite \| yeras  " |grep 'rst\|md'|grep -v java|grep -v css| grep -v 'js:'| grep -v tox| grep -v json |grep -v html | grep "  yera \| yuonger \| yeasr \| yaht \| ytou \| yeild \| yelow \| Yorkhire \| ya'll \| youre \| yuo \| yaer \| yhe \| yersa \| yatch \| younge \| youself \| Yementite \| yeras "