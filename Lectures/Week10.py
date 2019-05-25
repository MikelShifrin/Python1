#Exceptions

def main():
    loop = True
    while loop:
        try:
            hours = int(input('How many hours did you work?'))
        except IOError:
            print('ERROR: Hours')
        except ValueError as a:
            print('Value Error')
            print(a)
        except:
            print('ERROR: Hours worked must be valid')
        else:
            loop = False
        finally:
            print('finally')
    
main()

#IOError
#ValueError
