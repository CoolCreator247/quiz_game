print("welcome to Quiz_game")
print("to start pelease select the quiz to play")
while True:
    print("[1] Tech ")
    print("[2] Science")
    select = input(">")
    if select == "1":
        import time
        print("you get 10 secs for part of the Quiz")
        print(" ready ")
        time.sleep(1)
        print(" set ")
        time.sleep(1)
        print("Go!")
        quiz_part = input(">")
        print("The first laptop")
        print("[1] ibm")
        print("[2] Obsorn 1")
