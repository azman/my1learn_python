# howto: print text with no newline
# howto: delay execution

# need this to enable python3 print feature in python2
from __future__ import print_function
import sys
import time

print("This... ",end='')
sys.stdout.flush()
time.sleep(1)
print("is... ",end='')
sys.stdout.flush()
time.sleep(1)
print("legend (wait for it)... ",end='')
sys.stdout.flush()
time.sleep(1)
print("ary!")
