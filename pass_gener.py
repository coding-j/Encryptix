import random 
def pass_generate():
    len_pass = int(input('enter length of desired output'))
    password = ""
    to_chose_from = ['1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', ': ', '; ', '< ', '= ', '> ', '? ', '@ ', 'A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ', 'I ', 'J ', 'K ', 'L ', 'M ', 'N ', 'O ', 'P ', 'Q ', 'R ', 'S ', 'T ', 'U ', 'V ', 'W ', 'X ', 'Y ', 'Z ', '[ ', '\ '-' '+'\ ' -' ', '] ', '^ ', '_ ', '` ', 'a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h ', 'i ', 'j ', 'k ', 'l ', 'm ', 'n ', 'o ', 'p ', 'q ', 'r ', 's ', 't ', 'u ', 'v ', 'w ', 'x ', 'y ', 'z ', '{ ', '| ', '} ', '~ ',' '] 
    for i in range(len_pass):
        password += random.choice(to_chose_from)
    print(password)
if __name__ =='__main__':
    pass_generate()