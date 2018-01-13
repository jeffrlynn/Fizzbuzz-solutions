#Program will prompt user to input the power they would like e raised to, then give them the result.


number = int(input("What power of e would you like to see?\nEnter any number from 0 to 50:  "));

from math import e
def CalcE(number):
    if number == 0:
        return 1.0
    if 0 < number < 50:
        return e**number;
    else:
        return "Too powerful!";

print (CalcE(number));
