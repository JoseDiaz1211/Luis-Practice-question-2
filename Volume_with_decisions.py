# This program calculates the volume of three different objects : a sphere, a cube, and a cone. It also asks the
# the user to input the parameters for those objects.

if __name__ == '__main__':

    def cone_volume(radius=False, height=False):
        radius = float(input('What is the radius of your cone? '))
        height = float(input('What is the height of your cone? '))
        return 1/3 * 3.14 * (radius*radius) * height

    def cube_volume(area=False):
        area = float(input('What is the area of your cube? '))
        return area*area*area

    def sphere_volume(radius=False):
        radius = float(input('What is the radius of your sphere? '))
        return 4/3 * 3.14 * (radius**3)

    while True:
        choice = (input('''Please type a number to continue:
                       1 - Calculate volume of a cone
                       2 - Calculate volume of a cube
                       3 - calculate volume of a sphere
                       0 - quit
                       Your choice is '''))
        if choice == '1':
            print(cone_volume())
        elif choice == '2':
            print(cube_volume())
        elif choice == '3':
            print(sphere_volume())
        elif choice == '0':
            print('Thank you for using our program. Good bye!')
            break
        else:
            print('Sorry please type a number 1,2 ,3 or 0 to quit')
