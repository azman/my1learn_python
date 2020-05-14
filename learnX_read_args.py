# howto: get command-line text

import sys

print('Number of arguments:'+str(len(sys.argv))+'arguments.')
print('Argument String:'+str(sys.argv));

step=0
for that in sys.argv:
  step = step + 1
  print("#"+str(step)+": "+that)
