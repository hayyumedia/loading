import sys, os, random, time
from time import sleep
def load(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(random.random() * 0.4)
print ('Hallo nama saya alfin')
load ('assalamualaikum')