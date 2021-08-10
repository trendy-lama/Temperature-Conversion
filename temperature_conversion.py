print('What units are you conveting from?')
units = str(input('Type Fahrenheit or Celcius: ')) 
temp = float(input('Type the temperature in those units: '))

def conversion(units, temp):
    if units == 'Fahrenheit':
        c = (temp-32)*(5/9)
        if c == 0:
            print('Freezing point for water!')
        elif c == 100:
            print('Boiling point for water!')
        return print('The temperature in celcius is ' + str(c))
    elif units == 'Celcius':
        f = (temp * (9/5))+32
        if f == 32:
            print('Freezing point for water!')
        elif f == 212:
            print('Boiling point for water!')
        return print('The temperature in Fahrenheit is ' + str(f))

conversion(units, temp)