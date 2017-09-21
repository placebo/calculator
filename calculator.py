#!/usr/bin/env python

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y


print 'Welcome to my Calculator Program.'
print 'You will be able to do basic calculations.'
print 'Such as addition, subtraction, multiplication and division.'
print ' '

name = raw_input('Please Enter Your Name: ')

print ' '
print ("Hello %s, welcome to the calculator!") % name
print ' '

while True:
    print 'For addition press 1: '

    print 'For subtraction press 2: '

    print 'For multiplication press 3: '

    print 'For division press 4: '
    print ' '

    choice = raw_input('Please enter your operation 1-4: ')


    if choice == '1':
        print ' '
        print "Welcome to Addition!"

        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))


        print num1, '+', num2, '=', addition(num1,num2)
        print ' '
        print ' '
        choice = raw_input('Press Enter to continue / q to quit: ')
        if choice == 'q':
            exit()
        print ' '

                
    if choice == '2':
        print 'Welcome %s to Subtraction' % name
        print ' '
                
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        print ' '
        print num1, '-', num2, '=', subtraction(num1, num2)
        print ' '
        print ' '
        choice = raw_input('Press Enter to continue / q to quit: ')
        if choice == 'q':
            exit()
        print ' '

    if choice == '3':
        print 'Welcome %s to multiplication' % name
        print ' '

        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        print ' '
        print num1, '*', num2, '=', multiplication(num1, num2)
        print ' '
        print ' '
        choice = raw_input('Press Enter to continue / q to quit: ')
        if choice == 'q':
            exit()
        print ' '

    if choice == '4':
        print 'Welcome %s to division' % name
        print ' '

        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        print ' '
        print num1, '/', num2, '=', division(num1, num2)
        print ' '
        print ' '
        choice = raw_input('Press Enter to continue / q to quit: ')
        if choice == 'q':
            exit()
        print ' '

    


            

                









