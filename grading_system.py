a = int(input("Marks? : "))

if a > 101:
    print("Max value is 100!")
if 90 < a and a < 101:
    print("You get an A grade!")
if a > 80 and 90 > a:
    print("You get an B grade!")
if a > 70 and 80 > a:
    print("You get an C grade!")
if a > 60 and 70 > a:
    print("You get an C grade!")
if a < 60:
    print("You got an E grade!")
if a < 0:
    print("Alexa, play coffin dance!")
