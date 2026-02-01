from Rewrite import *
import time

print(fetchGonogo())
print(fetchMajorConcerns())

structTime = time.strptime("1 1 1970 0 0 10", "%d %m %Y %H %M %S")
isDate = False
inputTime = convertEpoch(structTime, isDate)

onHold = False
for returned in countdownTime(inputTime, onHold):
    print(returned)

# Time Tell launch
# input in

# Date Time
#current time - epoch