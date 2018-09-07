'''
hashmaster module example
usage:
    inmaster.py
'''
#import
import hashmaster

#return password

print("\n"+hashmaster.crack(input("algorithm: "),input("hash: "),input("wordlist: ")))
