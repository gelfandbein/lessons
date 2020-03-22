#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:03:17 2020

@author: boris
"""

def main(filename):
    with open(filename) as f:
        l = 0
        w = 0
        le = 0
        for line in f:
            l += 1
            le = len(line.strip("!"))
            print(f"line: {l}, letters: {le}")
        for letter in line:
            pos = 'out'
            if letter != ' ' and pos == 'out':
                if letter != ' a ':
                    w += 1
                    pos = 'in'
            elif letter == ' ':
                pos = 'out'
                
        print("words: ", w)
        f.close()
        #main2(filename)
        
def main2(filename):
    with open(filename) as f2:
        for line in f2:
            f = line
            print(f"line: {f}".strip())
            

        
if __name__ == "__main__":
    # _test()
    main("./text.txt")
else:
    print("\nWrong execution!")