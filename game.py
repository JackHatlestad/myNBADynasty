import pandas as pd
import random

team_name = input("Welcome to the NBA, What is your expansion teams name?")

try:
    df = pd.read_excel(f"{team_name}.xlsx")
except FileNotFoundError:
    df = pd.DataFrame([[2025,0,0,0,0,0,0,0,0,0,0,0,0,0]],columns = ['Year','Games Won', 'Games Lost', 'First Round', 'Confrence Semi-Finals', 
                                                        'Conference Finals', 'NBA Finals', 'Champions', 'PG', 'SG', 'SF', 'PF', 
                                                        'C', '6M'])
    point_guard = random.randint(0,10)
    shooting_guard = random.randint(0,10)
    small_foward = random.randint(0,10)
    power_foward = random.randint(0,10)
    center = random.randint(0,10)
    six_man = random.randint(0,10)

    print("Let's go to the expansion draft.")
    print(f"In the First Round the {team_name} select a {point_guard} overall Point Guard!")
    print(f"In the second Round the {team_name} select a {shooting_guard} overall Shooting Guard!")
    print(f"In the third Round the {team_name} select a {small_foward} overall Small foward!")
    print(f"In the fourth Round the {team_name} select a {power_foward} overall power foward!")
    print(f"In the five Round the {team_name} select a {center} overall Center!")
    print(f"In the sixth Round the {team_name} select a {six_man} overall Sixth Man!")

team_overall = point_guard + shooting_guard + small_foward + power_foward + center + six_man   

print(f"Welcome to the season")
for i in range(82):
    opponent_overall = random.randint(0,10) + random.randint(0,10)  + random.randint(0,10)  + random.randint(0,10) + random.randint(0,10) + random.randint(0,10) 
    if team_overall > opponent_overall: 
        print("Congrats you win!")
        df['Games Won'] = df['Games Won'] + 1
    else:
        print("Sorry you lost!")
        df['Games Lost'] = df['Games Lost'] + 1

if df.loc[0,'Games Won'] > 41:
     print("Congrats you made the playoffs!")
     




    

    
    
    

                                                        
                                                        
                                                        
