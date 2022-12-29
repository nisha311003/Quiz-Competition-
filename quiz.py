name = input("What's your name? ")
print("Welcome to a Quiz Competition!")
print("This is a True or False type quiz competition.")
quiz = {
    1 : {
        "question" : "Python is a high level language?",
        "answer" : "True"
    },
    2 : {
        "question" : "int(input()) is used to get string inputs? ",
        "answer" : "False"
    },
    3 : {
        "question" : "await is a keyword?",
        "answer" : "True"
    },
    4 : {
        "question" : "set is not a data type?",
        "answer" : "False"
    },
    5 : {
        "question" : "in is a membership operator?",
        "answer" : "True"
    }
}
def check_ans(question, answer, attempts, score):
    if quiz[question]["answer"].lower() == answer.lower() :
        print(f"Congratulations! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer")
        return False

score = 0
for question in quiz:
    attempts = 1
    while attempts > 0 :
        print(quiz[question]["question"])
        answer = input("Enter your answer: ")
        check = check_ans(question, answer, attempts,score)
        if check:
            score += 1
            break
        attempts -= 1










































