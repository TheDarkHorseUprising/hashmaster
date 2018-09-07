#imports
import sys
import hashmaster

#argc
argc=len(sys.argv)

#return password
if argc == 4:
    print(hashmaster.crack(sys.argv[1],sys.argv[2],sys.argv[3]))
else:
    print("usage: "+sys.argv[0]+" <algorthm> <hash> <wordlist>")
