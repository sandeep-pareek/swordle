#!/usr/bin/env python3

import json, random
import requests
from colored import fg, bg, attr
import enum
from typing import Counter

class Color(enum.Enum):
    grey = 242
    yellow = 11
    green = 28

def compare_words(r,w1):
    fr = [{'char':l, 'state': Color.grey} for l in w1]

    ly = Counter(r)

    for rr, rl, c in zip(fr, r, w1):
        if rl == c:
            rr['state'] = Color.green
            ly[rl] -= 1

    for rr, c in zip(fr, w1):
        if (c in ly and ly[c] > 0):
            rr['state'] = Color.yellow
            ly[c] -= 1

    return fr

def display_swordle(wordle):
    for word in wordle:
        for char in word:
            print('%s%s {0} %s'.format(char.get('char')) 
            % (fg('white'), bg(char.get("state").value), attr('reset')) , end = " ")
        print()

def rem(string):
    return "".join(string.split())

def valid_word(w, vw):
    tf = open("words.txt", "r")
    fc = tf.read()
    # just to handle if there are lower case letters returned from file, eg treat
    cl = [x.lower() for x in fc.split("\n")]
    tf.close()

    if (w in cl and w not in vw):
        return True
    else:
        return False

if __name__ == "__main__":
    rr = requests.get("https://api.datamuse.com/words?sp=?????")
    w = json.loads(rr.text)
    r = random.choice([k['word'] for k in w])

    found = False
    swordle = []
    aw = []

    i = 1
    while(True):
        if (i>6):
            break
        w1 = input("Enter swordle {0} ".format(str(i)))
        if(len(rem(w1).strip()) !=5 or not valid_word(w1, aw)):
            print("Please enter a valid non-repeated 5 letter english dictionary word, without spaces")
            continue
        
        fr = compare_words(r, w1)
        swordle.append(fr)
        aw.append(w1)
        display_swordle(swordle)
        if (w1 == r):
            found = True
            a = i
            break
        i=i+1

    if (found):
        print("Viola!! Word '{0}' found in {1} attempts!!".format(r, a))
    else:
        print("Was '{0}' so difficult? :-D ".format(r))
