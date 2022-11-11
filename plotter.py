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
        for i in self.signal:
            if i == '0':
                self.zero()
            elif i == '1':
                self.one()

    def zero(self):
        t.forward(self.distance)

    def one(self):
        posx, posy = t.pos()
        if self.logic_low - 1 < posy < self.logic_low + 1:
            t.sety(self.logic_high)
        elif self.logic_high - 1 < posy < self.logic_high + 1:
            t.sety(self.logic_low)
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


class RZ:

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
        t.sety(self.logic_low)
        t.forward(self.distance)
        t.sety(self.base)
        setTurtle(*invisiline)
        t.write('0', False, 'right', ("Arial", 12, "normal"))
        setTurtle(*default_settings)
        t.forward(self.distance)

    def one(self):
        t.sety(self.logic_high)
        t.forward(self.distance)
        t.sety(self.base)
        setTurtle(*invisiline)
        t.write('1', False, 'right', ("Arial", 12, "normal"))
        setTurtle(*default_settings)
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

if __name__=="__main__":
    print('Input Signal to be plotted (1s and 0s)')
    signal = input()
    print('\nEncode in format:\n1. NRZ-I\n2. NRZ-L\n3. RZ\n4. Manchester\n5. Diff Manchester\n6. AMI\n')
    encoding = int(input())
    if encoding == 6:
        print('\nChoose scrambling format:\n1. HDB3\n2. B8ZS\n')
        encoding2 = int(input())
        if encoding2 == 1:
            encoding = 6
        else:
            encoding = 7

    root = tk.Tk()
    root.title('Line Encoder')
    root.geometry('1000x300')
    cv = turtle.ScrolledCanvas(root, width=1000)  
    cv.pack()

    len_X, len_Y = 5000, 350
    default_settings = (2, 'green', 'slowest', False)
    invisiline = (1, 'black', 'fastest', False)
    map = {1: NRZ_I(signal), 2: NRZ_L(signal), 3: RZ(signal), 4: Manchester(signal),
        5: diff_Manchester(signal), 6: AMI_HDB3(signal), 7: AMI_B8ZS(signal)}

    screen = turtle.TurtleScreen(cv)
    screen.screensize(len_X, len_Y)
    t = turtle.RawTurtle(screen)

    drawAxes()
    setTurtle(*default_settings)
    map[encoding].draw()

    root.mainloop()