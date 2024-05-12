import time

string = str(input("Enter the phrase you want to brute force: "))
output = [''] * len(string)
for i in range(len(string)):
    curr = 'a'
    if ord(string[i]) < 97:
        curr = 'A'
    signal = 1
    while(signal):
        if string[i].isalpha() == False:
            output[i] = string[i]
            signal = 0
        elif string[i] == curr:
            output[i] = curr
            signal = 0
        else:
            output[i] = curr
            print(''.join(output))
            curr = chr(ord(curr)+1)
        time.sleep(0.06)
    print(''.join(output))