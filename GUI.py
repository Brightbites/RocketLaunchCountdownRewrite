from Rewrite import *
import time

link = ""
fetchGonogo()
fetchMajorConcerns()

print(updateGonogo())
print(updateMajorConcerns())

#T and L toggle
#Scrub

structTime = time.strptime("29 January 2026 20 21 0", "%d %B %Y %H %M %S")
getLaunchTime(structTime)
while True:
    t1 = time.monotonic()
    print(updateCountdown())
    t2 = time.monotonic()
    sleep(1.0 - (t2 - t1))