secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("guess:"))
    guess_count+=1
    if(guess==secret_number):
        print("answer is write but you won nothing!")
        break
    else:
        print(f"sorry {guess_count} chances completed!")
        if(guess_count==3):
            print("you are out")

