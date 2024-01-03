#!/bin/sh
curl "http://www.atnf.csiro.au/people/mcalabre/WCS/wcslib/" 2>/dev/null |grep "<title>" |sed -e 's,.*WCSLIB ,,;s, .*,,;' |head -n1

