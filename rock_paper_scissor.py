import random
def game():
    n_round = int(input('enter no of rounds to play'))
    user_choice='' 
    machine_choice= ''
    user_score =0
    machine_score = 0
    def round():
        nonlocal user_score
        nonlocal machine_score
        machine_choice = random.choice(['paper','rock','scissor'])
        print(machine_choice)
        user_choice = input('enter your choice valid inputs are rock,paper,scissor')
        if user_choice ==machine_choice:
            print('this round is draw')
        elif user_choice =='rock':
            if machine_choice=='paper':
                print('i win this round ')
                machine_score+=1
            else :
                print('you win this round ')
                user_score+=1
        elif user_choice =='paper':
            if machine_choice=='scissor':
                print('i win this round ')
                machine_score+=1
            else :
                print('you win this round ')
                user_score+=1
        elif user_choice =='scissor':
            if machine_choice=='rock':
                print('i win this round ')
                machine_score+=1
            else :
                print('you win this round ')
                user_score+=1
    for i in range (n_round):
        round()
    if user_score>machine_score:
        print('you win ')
    elif user_score== machine_score:
        print('A draw')
    else:
        print('you\'re a loser')
    print(
        f'''stats
          Your score:{user_score}
          my_score:{machine_score}'''
        )
if __name__ =='__main__':
    game()