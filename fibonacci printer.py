#Program will prompt user to input the number of Fibonacci digits they want to see, then give them the result.


number = int(input("How many Fibonacci numbers would you like to see?\nEnter any number from 0 to 50:  "));

def PrintFib(number):
    a,b = 1,1
    seq = [0, 1]
    if number == 0:
        return "Then we're done here.";
    if number == 1:
        return [0];
    if number == 2:
        return seq
    if 2 < number <= 50:
        for i in range(number - 2):
            a,b = b, (a + b)
            seq.append(a)
        return seq

print (PrintFib(number))
