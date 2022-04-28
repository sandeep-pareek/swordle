#!/usr/bin/env python3

import json, random
import requests
from colored import fg, bg, attr

rr = requests.get("https://api.datamuse.com/words?sp=?????")
w = json.loads(rr.text)

r = random.choice([k['word'] for k in w])
# print("Random 5 digit valid english word is : "+r)

def print_swordle(w):
    for wr in w:
        fw =''
        # ll = ''.join(map(str, wr))
        ll = [f for f in wr]
        # print(ll)
        for ww in ll:
            if (r.find(ww) == wr.find(ww)):
                # print("match of index " + ww)
                print('%s%s {0} %s'.format(ww) % (fg('white'), bg(28), attr('reset')) , end = " ")
            elif (r.find(ww) >=0):
                # print("char found in word!! " + ww)
                print('%s%s {0} %s'.format(ww) % (fg('white'), bg(11), attr('reset')) , end = " ")
            else:
                # print("greyed oout:: " + ww)
                print('%s%s {0} %s'.format(ww) % (fg('white'), bg(242), attr('reset')) , end = " ")

        print(fw)

def rem(string):
    return "".join(string.split())

def validWord(w):
    tf = open("words.txt", "r")
    fc = tf.read()
    # just to handle if there are lower case letters returned from file, eg treat
    cl = [x.lower() for x in fc.split("\n")]
    tf.close()
    # print("The list is: ", cl)

    if (w in cl):
        # print("found")
        return True
    else:
        # print("not found")
        return False


found = False
swordle = []
i = 1
while(True):
    # print(i)
    if (i>6):
        break
    w1 = input("Enter swordle {0} ".format(str(i)))
    if(len(rem(w1).strip()) !=5 or not validWord(w1)):
        # i=i-1
        print("Plese enter valid englist dictionary word, without spaces and of 5 chars")
        continue
    
    # print(w1)
    swordle.append(w1)
    if (w1 == r):
        found = True
        a = i
        break
    else:
        print_swordle(swordle)
    i=i+1

if (found):
    print_swordle(swordle)
    print("Viola!! Word '{0}' found in {1} attempts!!".format(r, a))
else:
    print("Was that so difficult? :-D " + r)
