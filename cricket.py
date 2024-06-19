import random
import time
import os

def Banner():
    print(
    """
    ░█████╗░██████╗░██╗░█████╗░██╗░░██╗███████╗████████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
    ██╔══██╗██╔══██╗██║██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝
    ██║░░╚═╝██████╔╝██║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░  ██║░░██╗░███████║██╔████╔██║█████╗░░
    ██║░░██╗██╔══██╗██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
    ╚█████╔╝██║░░██║██║╚█████╔╝██║░╚██╗███████╗░░░██║░░░  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
    ░╚════╝░╚═╝░░╚═╝╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
    """)

print("loading...........")
time.sleep(0.5)
os.system('clear')
print("Welcome To Cricket Game")
time.sleep(0.5)
Banner()
time.sleep(0.5)
print("Start Gaming.....\n")
time.sleep(0.5)

player1 = input("1.India\n2.Australia\n3.England\n4.Pakistan\nSelect any above country for 1st team: ")
comp = random.choice(["India", "Australia", "Engalnd", "Pakistan"])
time.sleep(0.5)

while player1 == comp:
    comp = random.choice(["India", "Australia", "Engalnd", "Pakistan"])

os.system('clear')
Banner()
print("*"*50+f"\nYour Team is {player1} and Computer teams is {comp}\n"+"*"*50)

if player1 in ["India", "Australia", "Engalnd", "Pakistan"]:
    player1_toss = input("Heads or Tails(heads/tails): ")
    comp_toss = random.choice(["heads", "tails"])
    TOSS = random.choice(["heads", "tails"])
    time.sleep(0.3)
    os.system('clear')
    Banner()
    print("*"*50+f"\nToss is {TOSS}\n"+"*"*50)
    if TOSS == player1_toss:
        os.system('clear')
        Banner()
        time.sleep(0.2)
        print("*"*50+f"\n{player1} Won the Toss\n"+"*"*50)
        BATTING = player1
        BOWLING = comp
        tmp = False
    else :
        os.system('clear')
        Banner()
        time.sleep(0.2)
        print("*"*50+f"\n{comp} Won the Toss\n"+"*"*50)
        BATTING = comp
        BOWLING = player1
        tmp = True
else:
    print("No Team with that name")

def p_score(score, wickets, overs):
    print("*"*50)
    print(f"Score: {score}\tWickets: {wickets}\t Overs:{overs}")
    print("*"*50)


def play(Bat, Overs, Wickets):
    Ball = 1
    Score = 0
    while Overs != 0 and Wickets != 0:
        while Ball != 6:
            if Bat == comp:
                time.sleep(0.2)
                x = int(input("Start Bowling(1,2,3,4,6): "))
                y = random.choice([1,2,3,4,6])
                if x > y:
                    Score += 0
                    os.system('clear')
                    Banner()
                    time.sleep(0.2)
                    print("No Score for this Ball")
                    time.sleep(0.2)
                    Ball += 1
                    p_score(Score, Wickets, Overs)
                elif x < y :
                    Score += y
                    Ball += 1
                    os.system('clear')
                    Banner()
                    time.sleep(0.2)
                    print(f"{y} runs for this ball")
                    time.sleep(0.2)
                    p_score(Score, Wickets, Overs)
                    
                elif x == y :
                    os.system('clear')
                    Banner()
                    time.sleep(0.2)
                    print("*"*50+"\n------ OUT ---------\n"+"*"*50)
                    Wickets -= 1
                    Ball += 1
                    os.system('clear')
                    Banner()
                    time.sleep(0.2)
                    p_score(Score, Wickets, Overs)
                    
            else :
                x = int(input("Start Batting(1,2,3,4,6): "))
                y = random.choice([1,2,3,4,6])
                if x < y:
                    Score += 0
                    os.system('clear')
                    Banner()
                    time.sleep(0.2)
                    print("No Score for this Ball")
                    time.sleep(0.2)
                    Ball += 1
                    os.system('clear')
                    Banner()
                    time.sleep(0.2)
                    print(f"{y} runs for this ball")
                    p_score(Score, Wickets, Overs)
                elif x > y :
                    Score += y
                    os.system('clear')
                    Banner()
                    time.sleep(0.2)
                    print(f"{y} runs for this ball")
                    time.sleep(0.2)
                    Ball += 1
                    os.system('clear')
                    Banner()
                    time.sleep(0.2)
                    print(f"{y} runs for this ball")
                    time.sleep(0.2)
                    p_score(Score, Wickets, Overs)
                elif x == y :
                    os.system('clear')
                    Banner()
                    time.sleep(0.2)
                    print("*"*50+"\n------ OUT ---------\n"+"*"*50)
                    time.sleep(0.2)
                    Wickets -= 1
                    Ball += 1
                    os.system('clear')
                    Banner()
                    time.sleep(0.2)
                    print(f"{y} runs for this ball")
                    time.sleep(0.2)
                    p_score(Score, Wickets, Overs)

        Overs -= 1
        Ball = 1
    return Score

BAT = play(BATTING,2,10)
time.sleep(0.2)
os.system('clear')
Banner()
print("*"*50+"\nFirst Innings Completed\n"+"*"*50)
time.sleep(0.2)
BOWL = play(BOWLING,2,10)

if BAT < BOWL:
    os.system('clear')
    Banner()
    print("*"*50+f"\n{BATTING} Won the GAME\n"+"*"*50)
else :
    os.system('clear')
    Banner()
    print("*"*50+f"\n{BOWLING} Won the GAME\n"+"*"*50)
