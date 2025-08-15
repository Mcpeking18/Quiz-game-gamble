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

# for i in QuestionsDic:
#     SetDic.add(i)   #using the unordered ness of sets :>

def randomlist(D):
    l = []
    l2 = []
    s=[]
    for i in D:
        l.append(i)
    while l:
        idx = random.randint(0, len(l) - 1)
        l2.append(l.pop(idx))
    return l2

def answercheck(ans,dic,i):
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

input('''Here are the rules to play this Game:
It is a gambling game.
Every correct answer doubles your money.
Every wrong answer deducts 200% of your Starting amount from your Winning Amount.
If your balance goes negative, you'll owe us the amount!
Press Enter to continue...''')

wrong = 0
correct = 0
start_money = int(input("\nSo how much money would you gamble : "))
question_list = randomlist(list(QuestionsDic.keys()))

for i in question_list:
    print(f"\nHere's the question vvvv\n{i}")
    # print(f"Here's the choices for your question : ")
    Shuffled_Options = randomlist(QuestionsDic[i]["options"]) #now a contains a list of answers (randomised) from Questiondic
    temp = 0
    for j in Shuffled_Options:
        temp+=1
        print(f"{temp}). {j}",end="         ")
    print()
    catch1 = 0
    catch2 = 0
    while True:
        answer = input("\nEnter the Your answer : ").lower()
        try:
            if (int(answer)-1) not in range(len(Shuffled_Options)):
                print("Bro there is no option like that redo")
                catch2 += 1
                print(f"You've entered none of the options {catch2} times")
                if catch2 == 5:
                    print(f"You've Typed None of the options {catch2} times \nI'm marking it as wrong")
                    wrong += 1
                    break
                continue

            answer = Shuffled_Options[int(answer)-1]
            checked = answercheck(answer,QuestionsDic,i)
            if checked == 0:
                break
            elif checked == 1:
                break
            else:
                continue
        except ValueError:
            checked = answercheck(answer,QuestionsDic,i)
            if checked == 0:            
                break
            elif checked == 1:
                break
            else:
                continue

print(f"your total correct answer = {correct}")
print(f"your total wrong answer = {wrong}")

if correct != 0:
    money = (2**(correct-1)*start_money)-(2*start_money*wrong)
else:
    money = -2*start_money*wrong

if money > 0:
    print(f"\nCongrats youve won {money}")
else:
    print(f"\nSadly you owe us {-1*money}")

input("\nPress enter to close :> ")