def contacts():
    chosen_action = None
    a=0
    reqd_file = 'contact_list.txt'
    try:
        with open(reqd_file,'r'):
            pass 
    except:
        with open(reqd_file,'w') as f:
            f.write('''''')
    def access_contacts():
        nonlocal chosen_action
        chosen_action = int(input('''
                                  Choose Your Action and enter its serial no
                                  1 add contact
                                  2 delete contact
                                  3 see all contacts 
                                  4 search a contact '''))
    access_contacts()
    match chosen_action:
        case 1:
            try:
                with open(reqd_file,'a') as f:
                    f.write('\n'+ input('enter phone no of contact to add') +5*' ' +input('enter name of contact to add') )
                    print('contact added')
            except:
                print('please retry')
        case 2:
            try:
                with open(reqd_file,'r+') as f :
                    x = f.readlines()
                    chosen_contact =  input('enter contact no to be deleted ')+5*' ' +input('enter contact name  to be deleted') +'\n'
                    for i in range(1,len(x)):
                        if x[i]== chosen_contact :
                            x.pop(i)
                    print('contact deleted')
                    f.seek(0)
                    f.truncate()
                    
                    for i in x:
                        f.write(i)
            except:
                print('please retry')
        case 3:
            try:
                with open(reqd_file) as f :
                    x = f.readlines()
                    print('contact        Name')
                    for i in range(1,len(x)):
                        print(x[i]+'\n')
            except:
                print('please retry')
        case 4:
            try:
                with open(reqd_file)as f:
                    x = f.readlines()
                    reqd_cont= input('enter name of contact to search')
                    for i in range(1,len(x)):
                        if x[i][15:].lower() == reqd_cont.lower() or x[i][15:].upper() == reqd_cont.upper():
                            print(x[i],'is required contact')
                        else :
                            a+=1
                    if a== len(x)-1:
                        print('contact not found')
            except:
                print('please retry')
if __name__ == '__main__':
    contacts()