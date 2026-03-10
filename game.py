import random
import time

print("Welcome to Our Kahoots!")

# add a score
score=0
#take users input to get their name

name=input("What is your name?: ").strip()
print(f"Hello {name}.Let's start our game!")

letters=["A","B","C","D"]

#Lets create a dictionary with all of our questions inside of it. That we can access it randomly

questions={
    #question1:answer1
    "What language this code is written?":{
        "options":["Python","JS","C++","Ruby"],
        "answer":"A"},
    "what symbol is used to write command in python":{
        "options":["#","//","&","~"],
        "answer":"A"},
    "what function is used to display text in our terminal":{
        "options":["display","print","touch","write"],
        "answer":"B"},
    "What is the correct file extension":{
        "options":[".txt",".py",".json",".pdf"],
        "answer":"B"
    }

}

#randomize the question into a list
question_list=list(questions.keys())
# print(question_list)
random.shuffle(question_list)

#add a score variable to what our current score is

for question in question_list:
    print(question)
    options=questions[question]["options"]

    for letter,option in enumerate(options):
        print(letters[letter],option)
    
    start_time=time.time()
    #print(start_time)

    answer=input("Your answer: ").strip().upper()

    end_time=time.time()
    #print(end_time)

    time_taken=round(end_time-start_time)
    #print(time_taken)

    print("You took", time_taken,"seconds")

    if time_taken>10:
        print("Too slow! No points for this round!")
        print("Your score this round is",score)
    
    elif answer==questions[question]["answer"]:
        print("Correct! score+1")
   #update score if it's correct
        score=score+1
   
    else:
        print("Wrong answer")
    print("You answered:",answer)

print("Your Score is:",score)

percentage=round((score/len(questions))*100)

print("You got", percentage,"% correct!")
