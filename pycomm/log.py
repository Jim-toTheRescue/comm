#! /bin/python
#-*-coding: utf-8-*-
def Log(msg, color = "info"):
    colorMap = {
        "red": 31,
        "green": 32,
        "yello": 33,
        "info": 37,
        }
    if not isinstance(color, str):
        raise
    color = color.lower()
    colorNum = colorMap.get(color, 37)
    print "\033[1;%dm%s\033[m"%(colorNum, msg)

