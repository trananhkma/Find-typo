#!/bin/bash

grep -rn "  judgement \| juction \| jewlrey \| judical \| Japanes \| juntion \| Juadaism \| Juadism \| Jharkand \| journy \| jewlery \| juniour \| jsut \| Johanine \| Jospeh \| jurisdication \| juvinile \| Jersualem \| judisuary \| Janusry \| jeapardy \| jorunal \| jstu \| jewler \| Japaneese \| Janaury \| journies \| Janurary \| junoir \| judgment \| Jamacia  " |grep 'rst\|md'|grep -v java|grep -v css| grep -v 'js:'| grep -v tox| grep -v json |grep -v html | grep "  judgement \| juction \| jewlrey \| judical \| Japanes \| juntion \| Juadaism \| Juadism \| Jharkand \| journy \| jewlery \| juniour \| jsut \| Johanine \| Jospeh \| jurisdication \| juvinile \| Jersualem \| judisuary \| Janusry \| jeapardy \| jorunal \| jstu \| jewler \| Japaneese \| Janaury \| journies \| Janurary \| junoir \| judgment \| Jamacia "