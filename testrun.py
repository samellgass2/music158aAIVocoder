from harmonizer import *

def main():
    majorHarmonizer = minorCounterPointHarmonizer(key=0, voices=4)
    testprog = [0, 2, 4, 5, 2, 11, 7, 2, 0]
    for note in testprog:
        nextchord = majorHarmonizer.harmonize(note)
        print(majorHarmonizer.currchord)
        print(nextchord)

main()