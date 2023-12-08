print("CS112: Computer Programming 1 \nCreated by: Clyde Joshua C.Belongilot")

print("GUIDELINES:")
print('[1] If [start range] is a negative number. The program will prompt a message: "Enter a non-negative number"')
print('[2] If [end range] is less than [start range]. The program will prompt a message: "Enter a number greater than [start range]"')
print('[3] If the user enters the number "0", the program will terminate.')
print("------------------------------------------------------------------")

while True:
    
    start = int(input("Enter a number[Start]:"))

    if start == 0:
        print("Program Terminated")
        break
    elif start < 0:
        print("Enter a non-negative number")
    else:
        end = int(input("Enter a number[End]:"))

        if end == 0:
            print("Program Terminated")
            break
        elif end < start:
            print("Enter a number greater than", start)
        elif end > start:
            print('Prime numbers between the range', start, 'and', end, 'are: ')

            for prime in range(start, end + 1):

                if prime > 1:

                    for i in range(2, prime):

                        if (prime % i) == 0:
                            break

                    else:
                        print(prime, end=' ')

    print()
    print("------------------------------------------------------")
    
            

                    
