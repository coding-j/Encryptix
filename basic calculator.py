def calculate():
    while True:
        calc_input= input('''enter mathematical operation':
                      ''')
        try:
            print(eval(calc_input))
            break
        except:
            print('invalid input')
            continue
if __name__ == '__main__':
    calculate()