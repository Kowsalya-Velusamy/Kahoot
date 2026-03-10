import random

print("Welcome to Our Kahoots!")

# add a score
score=0
#take users input to get their name

name=input("What is your name?: ").strip()
print(f"Hello {name}.Let's start our game!")

#Lets create a dictionary with all of our questions inside of it. That we can access it randomly

questions={
    #question1:answer1
    "What language this code is written?":{
        "options":["Python","JS","C++","Ruby"],
        "answer":"python"},
    "what symbol is used to write command in python":{
        "options":["#","//","&","~"],
        "answer":"#"},
    "what function is used to display text in our terminal":{
        "options":["display","print","touch","write"],
        "answer":"print"},
    "What is the correct file extension":{
        "options":[".txt",".py",".json",".pdf"],
        "answer":".py"
    }

}

#randomize the question into a list
question_list=list(questions.keys())
# print(question_list)
randomQ=random.shuffle(question_list)

#add a score variable to what our current score is

for question in question_list:
    print(question)
    options=questions[question]["options"]

    for option in options:
        print(option)

    answer=input("Your answer: ").strip().lower()
    if answer==questions[question]["answer"]:
        print("Correct! score+1")
   #update score if it's correct
        score=score+1
   
    else:
        print("Wrong answer")
    print("You answered:",answer)

print("Your Score is:",score)

percentage=round((score/len(questions))*100)

print("You got", percentage,"% correct!")
