import random as rnd
import numpy as np

class NumLock:
    
    def __init__(self, pw):
        self.password = [num for num in pw]
        self.numpad = list(range(0,10))
        self.pospassword = [''] * len(self.password)
        
    def shufflepad(self):
        rnd.shuffle(self.numpad)
        for i in range(len(self.password)):
            curr = ord(self.password[i]) - ord('0')
            pos = self.numpad.index(curr)
            self.pospassword[i] = str(pos)
        
    def printpad(self):
        for i in range(0,9,3):
            print("{}  {}  {}".format(self.numpad[i], self.numpad[i+1], self.numpad[i+2]))
        print("   {}   ".format(self.numpad[9]))
        
    def test(self, input):
        if input == ''.join(self.pospassword):
            return True
        return False

pw = str(input("Input PIN you would like to use: "))
pass1 = NumLock(pw)
pass1.shufflepad()
print("Using the following number pad, please input the pattern in which you would hit the buttons:")
pass1.printpad()
print("(Assume top right is the number 0 and the bottom number is position 9)")
inpass = str(input("PIN (based on positioning): "))
n = 0
while (not pass1.test(inpass) and n < 100):
    print("Incorrect input, try again.")
    pass1.printpad()
    inpass = str(input("PIN (based on positioning): "))
    n += 1
print("Correct Input!")
