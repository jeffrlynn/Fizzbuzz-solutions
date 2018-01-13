#Program will prompt user to input the number of pi decmimals they would like to see, then give them the result.


number = int(input("How many decimals of pi would you like to see?\nEnter any number from 0 to 50:  "));

from math import pi
def CalcPi(number):
    if number == 0:
        return 3
    if 0 < number < 50:
        return format(pi, '.' + str(number) + 'f');
    else:
        return "Too many digits requested.";

print (CalcPi(number));
