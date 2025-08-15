import random

QuestionsDic = {
    "Which animal barks?": {
        "options": ["cat", "dog", "lion", "fish"],
        "answer": "dog"
        },
    "What color is made by mixing blue and yellow?": {
        "options": ["blue", "red", "green", "yellow"],
        "answer": "green"
        },
    "Which one is a vegetable?": {
        "options": ["apple", "banana", "grape", "carrot"],
        "answer": "carrot"
        },
    "Which planet do we live on?": {
        "options": ["earth", "mars", "venus", "pluto"],
        "answer": "earth"
        },
    "Which language is also a snake?": {
        "options": ["python", "java", "ruby", "perl"],
        "answer": "python"
        },
    "What food is Italian?": {
        "options": ["sushi", "burger", "pizza", "salad"],
        "answer": "pizza"
        },
    "Who is from Krypton?": {
        "options": ["batman", "superman", "spiderman", "flash"],
        "answer": "superman"
        },
    "What city is in Germany?": {
        "options": ["paris", "rome", "london", "berlin"],
        "answer": "berlin"
        },
    "What season comes after winter?": {
        "options": ["summer", "winter", "spring", "autumn"],
        "answer": "spring"
        },
    "What metal is most valuable?": {
        "options": ["silver", "gold", "bronze", "iron"],
        "answer": "gold"
        }
}

def randomlist(D): #my own list randomiser so ofc not efficient 
    list1 = []
    list2 = []
    for i in D:
        list1.append(i)
    while list1:
        temp = random.randint(0, len(list1) - 1)
        list2.append(list1.pop(temp))
    return list2

def answercheck(ans,dic,i):  #this one checks answer as the name suggest
    global correct,wrong,catch1
    if ans in Shuffled_Options and ans == dic[i]["answer"]:
        correct += 1
        print("its correct :> +1")
        return 0 
    elif ans in Shuffled_Options and ans != dic[i]["answer"]:
        wrong += 1
        print("its wrong :< +1")
        return 0
    else:
        catch1 += 1
        if catch1 == 5:
            print(f"You've Typed None of the options {catch1} times \nI'm marking it as wrong")
            wrong += 1
            return 1
        print(f"You've entered none of the options {catch1} times")

wrong = 0
correct = 0
question_list = randomlist(list(QuestionsDic.keys()))  

input('''Here are the rules to play this Game:
It is a gambling game.
Every correct answer doubles your money.
Every wrong answer deducts 200% of your Starting amount from your Winning Amount.
If your balance goes negative, you'll owe us the amount!
Press Enter to continue...''')    #here is the start of my code

start_money = int(input("\nSo how much money would you gamble : ")) #initial amount

for i in question_list:
    print(f"\nHere's the question vvvv\n{i}")

    Shuffled_Options = randomlist(QuestionsDic[i]["options"])           #now a contains a list of answers (randomised) from Questiondic
    temp = 0
    for j in Shuffled_Options:
        temp+=1
        print(f"{temp}).{j.title()}",end="         ")  #shows options in a nice way :D
        print()

    catch1 = 0           #just fun lil element of tell user oh you typed none this many times
    catch2 = 0           #same as above
    while True:
        answer = input("Enter the Your answer : ").lower()
        try:            #this one here is if user types the number of the answer if does not get converted to int it goes normally
            if int(answer)-1 not in range(len(Shuffled_Options)):         #just a failsafe if they type option 100 or smth
                print("Bro there is no option like that redo")
                catch2 += 1
                print(f"You've entered none of the options {catch2} times")
                if catch2 == 5:
                    print(f"You've Typed None of the options {catch2} times \nI'm marking it as wrong")
                    wrong += 1
                    break
                continue

            answer = Shuffled_Options[int(answer)-1]            #real sht
            checked = answercheck(answer,QuestionsDic,i)        #easily understandable sooo yeahhhh
            if checked == 0:
                break
            elif checked == 1:
                break
            else:
                continue

        except ValueError:          #same as above but if user types the answer
            checked = answercheck(answer,QuestionsDic,i)
            if checked == 0:            
                break
            elif checked == 1:
                break
            else:
                continue

print(f"\nYour total correct answer = {correct}")
print(f"Your total wrong answer = {wrong}")

if correct != 0:
    money = (2**(correct-1)*start_money)-(2*start_money*wrong)
else:
    money = -2*start_money*wrong

if money > 0:
    print(f"\nCongrats youve won {money}")
else:
    print(f"\nSadly you owe us {-1*money}")

input("\nPress enter to close :> ")