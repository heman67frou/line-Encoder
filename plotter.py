import random
import sys
from traceback import print_tb
import turtle
import tkinter as tk

def check_consecutive_zeros(i, signal, size):
    for j in range(size):
        if signal[i+j] != '0':
            return False
    return True


class NRZ_I:

    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50

    def draw(self):
        t.sety(self.logic_high) 
        count = 0
        for i in self.signal:
            if i == '0':
                self.zero()
            elif i == '1':
                count += 1
                self.one(count)

    def zero(self):
        t.forward(self.distance)

    def one(self, count):
        if count%2 == 1:
            t.sety(self.logic_low)
            t.forward(self.distance)
        else:
            t.sety(self.logic_high)
            t.forward(self.distance)


class NRZ_L:

    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50

    def draw(self):
        for i in self.signal:
            if i == '0':
                self.zero()
            elif i == '1':
                self.one()

    def zero(self):
        t.sety(self.logic_high)
        t.forward(self.distance)

    def one(self):
        t.sety(self.logic_low)
        t.forward(self.distance)


class Manchester:

    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50
        self.base = 0

    def draw(self):
        for i in self.signal:
            if i == '0':
                self.zero()
            elif i == '1':
                self.one()

    def zero(self):
        t.sety(self.logic_high)
        t.forward(self.distance)
        setTurtle(*invisiline)
        t.write('0', False, 'right', ("Arial", 12, "normal"))
        setTurtle(*default_settings)
        t.sety(self.logic_low)
        t.forward(self.distance)

    def one(self):
        t.sety(self.logic_low)
        t.forward(self.distance)
        t.sety(self.logic_high)
        setTurtle(*invisiline)
        t.write('1', False, 'right', ("Arial", 12, "normal"))
        setTurtle(*default_settings)
        t.forward(self.distance)


class diff_Manchester:

    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50
        self.base = 0

    def draw(self):
        prev_num = 2  
        for i in self.signal:
            if i == '0':
                self.pattern(prev_num, '0')
            elif i == '1':
                num = 1 if prev_num == 2 else 2
                self.pattern(num, '1')
                prev_num = num

    def pattern(self, num, write):
        if num == 1:
            t.sety(self.logic_high)
            t.forward(self.distance)
            setTurtle(*invisiline)
            t.write(write, False, 'right', ("Arial", 12, "normal"))
            setTurtle(*default_settings)
            t.sety(self.logic_low)
            t.forward(self.distance)
        elif num == 2:
            t.sety(self.logic_low)
            t.forward(self.distance)
            t.sety(self.logic_high)
            setTurtle(*invisiline)
            t.write(write, False, 'right', ("Arial", 12, "normal"))
            setTurtle(*default_settings)
            t.forward(self.distance)


class AMI_HDB3:

    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50
        self.base = 0

    def draw(self):
        list = []
        count = 0
        prev_bit = -1
        i = 0
        while i < len(self.signal):
            if self.signal[i] == '1':
                count += 1
            if ((i+3)<len(self.signal)) and check_consecutive_zeros(i, self.signal, 4):
                a = []
                if count%2==0:
                    prev_bit *= -1
                    a = [prev_bit,0,0,prev_bit]
                    count += 2
                else:
                    a = [0,0,0,prev_bit]
                    count += 1
                for j in range(4):
                    list.append(a[j])
                i += 4
            else:
                if self.signal[i] == '1':
                    prev_bit *= -1
                    list.append(prev_bit)
                else:
                    list.append(0)
                i += 1
        
        t.sety(self.logic_high) 
        for i in list:
            if i == 0:
                self.zero()
            elif i == 1:
                self.one()
            else:
                self.negative_one()

    def zero(self):
        t.sety(self.base)
        t.forward(self.distance)

    def one(self):
        t.sety(self.logic_high)
        t.forward(self.distance)

    def negative_one(self):
        t.sety(self.logic_low)
        t.forward(self.distance)


class AMI_B8ZS:

    def __init__(self, signal: str):
        self.signal = signal
        self.logic_high = 50
        self.logic_low = -50
        self.distance = 50
        self.base = 0

    def draw(self):
        list = []
        prev_bit = -1
        i = 0
        while i < len(self.signal):
            if ((i+7)<len(self.signal)) and check_consecutive_zeros(i, self.signal, 8):
                a = []
                if prev_bit == 1:
                    a = [0,0,0,1,-1,0,-1,1]
                    prev_bit = 1
                else:
                    a = [0,0,0,-1,1,0,1,-1]
                    prev_bit = -1
                for j in range(8):
                    list.append(a[j])
                i += 8
            else:
                if self.signal[i] == '1':
                    if prev_bit == 1:
                        prev_bit = -1
                        list.append(prev_bit)
                    else:
                        prev_bit = 1
                        list.append(prev_bit)
                else:
                    list.append(0)
                i += 1
        
        t.sety(self.logic_high) 
        for i in list:
            if i == 0:
                self.zero()
            elif i == 1:
                self.one()
            else:
                self.negative_one()

    def zero(self):
        t.sety(self.base)
        t.forward(self.distance)

    def one(self):
        t.sety(self.logic_high)
        t.forward(self.distance)

    def negative_one(self):
        t.sety(self.logic_low)
        t.forward(self.distance)


def drawAxes():

    def drawLineAndBack(distance):
        for i in range(distance // 50):
            t.forward(50)
            t.dot(5)
        t.backward(distance)

    t.hideturtle()
    t.speed('fastest')
    t.setx(-len_X // 2 + 100)
    drawLineAndBack(len_X)
    t.rt(90)
    drawLineAndBack(100)
    t.rt(180)
    drawLineAndBack(100)
    t.rt(90)


def setTurtle(size, colour, speed, visibility):
    t.pensize(size)
    t.pencolor(colour)
    t.speed(speed)
    if not visibility:
        t.hideturtle()

def rand_key(p, zero_size):
    key = ""
    if p == zero_size:
        for i in range(p):
            key += "0"
    else:
        k = random.randint(0, p-zero_size+1)
        for i in range(p):
            if i >= k and i < k+zero_size:
                key += "0"
            else:
                temp = str(random.randint(0, 1))
                key += temp
    return(key)

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

def longestPalindromicSequence(st, n):
    rev = reverse(st)
    P = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                P[i][j] = 0
            elif st[i-1] == rev[j-1]:
                P[i][j] = P[i-1][j-1] + 1
            else:
                P[i][j] = max(P[i-1][j], P[i][j-1])
    str = ""
    i = n
    j = n
    while i > 0 and j > 0:
        if st[i-1] == rev[j-1]:
            str += st[i-1]
            i -= 1
            j -= 1
        elif P[i-1][j] > P[i][j-1]:
            i -= 1
        else:
            j -= 1
    str = str[::-1]
    print("Longest Paindromic Sub-Sequence of " + st + " is " + str)

if __name__=="__main__":
    print('\nChoose Encoding Format:\n1. NRZ-I\n2. NRZ-L\n3. Manchester\n4. Diff Manchester\n5. AMI\n')
    encoding = int(input())
    if encoding == 5:
        print('\nChoose Scrambling format:\n1. HDB3\n2. B8ZS\n')
        encoding2 = int(input())
        if encoding2 == 1:
            encoding = 5
        else:
            encoding = 6

    print('Length of binary string required')
    size = int(input())
    zero_size = 0
    if encoding == 5:
        print('Total No Of subsequent 0s')
        zero_size = int(input())
    if zero_size > size:
        print('Total length of string is less than total 0s required')
        sys.exit(0)
    signal = rand_key(size, zero_size)
    print('Your generated signal : ' + signal)

    root = tk.Tk()
    root.title('Line Encoder')
    root.geometry('1000x300')
    cv = turtle.ScrolledCanvas(root, width=1000)  
    cv.pack()

    len_X, len_Y = 5000, 350
    default_settings = (2, 'green', 'slowest', False)
    invisiline = (1, 'black', 'fastest', False)
    map = {1: NRZ_I(signal), 2: NRZ_L(signal), 3: Manchester(signal),
        4: diff_Manchester(signal), 5: AMI_HDB3(signal), 6: AMI_B8ZS(signal)}

    screen = turtle.TurtleScreen(cv)
    screen.screensize(len_X, len_Y)
    t = turtle.RawTurtle(screen)

    drawAxes()
    setTurtle(*default_settings)
    map[encoding].draw()

    root.mainloop()
    x = reverse(signal)
    longestPalindromicSequence(signal, size)

    sys.exit(0)
