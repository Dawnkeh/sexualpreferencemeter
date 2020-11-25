import os
def func(pref, name):
    try:
        if int(pref) > 0 and int(pref) < 5:
            print('Liar ' + name.capitalize() + ' is gay.')
        if int(pref) > 4 and int(pref) < 11:
            print(name.capitalize() + ' is gay.')
        if int(pref) > 10 or int(pref) < 0:
            print(name.capitalize() + ' didn\'t follow the scale which is pretty gay.')
        else:
            print(' ')
    except ValueError:
        print(name.capitalize() + " is a gay asshole idiot who doesn't know what a number is.")
        funk()
def funk():
    os.system('color 03')
    name = input('''What is your name
    ''')
    pref = input('''How Gay are you 1-10?
    ''')
    func(pref, name)    
funk()
os.system('pause')