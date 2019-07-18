# howto: print text with no newline
# howto: delay execution

# need this to enable python3 print feature
#from __future__ import print_function
#print("This... ",end='')
#print("is... ",end='')
#print("legend (wait for it)... ",end='')
#print("ary!")

import time
import sys

print "This...",
sys.stdout.flush()
time.sleep(1)
print "is...",
sys.stdout.flush()
time.sleep(1)
print "legend (wait for it)...",
sys.stdout.flush()
time.sleep(1)
print "ary!"
