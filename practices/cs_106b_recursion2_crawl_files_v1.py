#-*- coding: utf-8 -*-
"""
https://www.youtube.com/watch?v=XYubfcyLrBY&index=10&list=PLnfg8b9vdpLn9exZweTJx44CII1bYczuk
"""
import os
def rec(path, depth = 0):
    #print("rec(%s)" % path)
    for p in os.listdir(path):
        #print("miso1(%s)" % os.path.join(path, p))
        if os.path.isdir(os.path.join(path, p)):
            print("%s%s" % ("    "*depth, p))
            rec(os.path.join(path, p), depth + 1)
        else:
            print("%s%s" % ("    "*depth, p))




def crawl_files(path):
    rec(path)
    print("\n-----------")

path = "/Users/makoto.kitayama/projects/my/jg19/aoj"
crawl_files(path)


