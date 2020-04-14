# This program calculates the valume of three different objects : a sphere, a cube, and a cone. It also asks the
# the user to input the parameters for those objects.

import os

PI = 3.14

def clear():
    os.system('clear') # cls on windows

def print_menu():
    clear()
    print("Please type a number to continue:")
    print("1 - Calculate volume of a cone")
    print("2 - Calculate volume of a cube")
    print("3 - Calculate volume of a sphere")
    print("0 - quit")

def read_option():
    ret = -1
    op = input("Your choice is: ")
    try:
        ret = int(op)
    except ValueError:
        print("Please select a Number")
    return ret

def cal_cone_volume(radius, height):
    return 1/3 * PI * (radius*radius) * height

def cone_volume():
    clear()
    try:
        radius = float(input("What is the radius of your cone? "))
        height = float (input("What is the height of your cone? "))
    except ValueError:
        print("Invalid number")
        input()
        return
    vol = cal_cone_volume(radius, height)
    print("The volume of a cone with radius %f and height %f is %f"%(radius, height, vol))
    input()

def cal_cube_volume(length):
    return length * length * length

def cube_volume():
    clear()
    try:
        length = float(input("What is the length of your cube? "))
    except ValueError:
        print("Invalid number")
        input()
        return
    vol = cal_cube_volume(length)
    print("The volume of a cube of length %f is %f"%(length, vol))
    input()

def cal_sphere_volume(radius):
    return 4/3 * PI * (radius**3)

def sphere_volume():
    clear()
    try:
        radius = float(input("What is the radius of your sphere? "))
    except ValueError:
        print("Invalid number")
        input()
        return
    vol = cal_sphere_volume(radius)
    print("The volume of a sphere with radius %f is %f"%(radius, vol))
    input()

def main():
    end = False
    while not end:
        print_menu()
        op = read_option()
        if op == 0:
            end = True
        elif op == 1:
            cone_volume()
        elif op == 2:
            cube_volume()
        elif op == 3:
            sphere_volume()
        else:
            print("Sorry please type a number 1,2 ,3 or 0 to quit")
            input()

    print("bye")

if __name__ == '__main__':
    main()