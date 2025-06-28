import pandas as pd 
import random
import time

def load_existing():
    team_name = input("What is your team name?\n")

    try:
        df = pd.read_excel(f"{team_name}.xlsx")
    except FileNotFoundError:
        print("Error Can't Find Team")
    return df, team_name

def create_new():
    team_name = input("What is your team name?\n")
    df = pd.DataFrame([[2025,0,0,0,0,0,0,0,0,0,0,0,0]], columns=['Year','Games Won', 'Games Lost', 'First Round',
                                                                 'Confrence Semi-Finals', 'Confrence Finals', 
                                                                'NBA Finals', 'Champions', 'PG', 'SG', 'SF', 'PF', 'C'])
    print(f"Welcome {team_name}! Now it's time for the 2025 NBA Expansion Draft!")
    time.sleep(5)
    pg = random.randint(1,10)
    df.at[0, 'PG'] = pg
    print(f"In the first round of the 2025 NBA Expansion Draft the {team_name} select a {pg} overall Point Guard!")
    time.sleep(5)
    sg = random.randint(1,10)
    df.at[0, 'SG'] = sg
    print(f"In the first round of the 2025 NBA Expansion Draft the {team_name} select a {sg} overall Shooting Guard!")
    time.sleep(5)
    sf = random.randint(1,10)
    df.at[0, 'SF'] = sf
    print(f"In the first round of the 2025 NBA Expansion Draft the {team_name} select a {sf} overall Small Forward!")
    time.sleep(5)
    pf = random.randint(1,10)
    df.at[0, 'PF'] = pg
    print(f"In the first round of the 2025 NBA Expansion Draft the {team_name} select a {pf} overall Power Forward")
    time.sleep(5)
    c = random.randint(1,10)
    df.at[0, 'C'] = c
    print(f"In the first round of the 2025 NBA Expansion Draft the {team_name} select a {c} overall Center!")
    time.sleep(5)
    print("That concludes the 2025 NBA Expansion Draft!")
    return df,team_name,pg,sg,sf,pf,c

def season(df):
    team_overall = df.iloc[-1]['PG'] + df.iloc[-1]['SG'] + df.iloc[-1]['SF'] + df.iloc[-1]['PF'] + df.iloc[-1]['C']

    for i in range(1,82):
        opponent_overall = random.randint(5,50)
        if team_overall > opponent_overall:
            print(f"Congrats you won the game {i}!")
            df.iloc[-1]['Games Won'] = df.iloc[-1]['Games Won'] + 1
        else:
            print(f"Sorry you lost game {i}")
            df.iloc[-1]['Games Lost'] = df.iloc[-1]['Games Lost'] + 1
    
    Percentage = df.iloc[-1]['Games Won'] / 82

    if Percentage > 0.80:
        seed = random.randint(1,2)
        print(f"Congrats you've made the playoffs as a {seed} seed")
    elif Percentage > 0.60:
        seed = random.randint(3,6)
        print(f"Congrats you've made the playoffs as a {seed} seed")
    elif Percentage > 0.50:
        seed = random.randint(7,8)
        print(f"Congrats you've made the playoffs as a {seed} seed")
    else:
        print("You missed the playoffs!")
        return df

def main():
    choose_team = int(input("Welcome to the NBA!\n 1. Load Existing Team\n 2. Create Expansion Team\n"))
    if choose_team == 1:
        df,team_name = load_existing()
    elif choose_team == 2:
        df,team_name,pg,sg,sf,pf,c = create_new()
    
    while True:
        choose_mode = int(input("Do you want to:\n 1. Play a season\n 2. View Stats\n 3. Exit\n"))
        if choose_mode == 1:
            season(df)
            print("Let's Play")
        elif choose_mode == 2:
            print(df[['Year','Games Won', 'Games Lost', 'First Round', 'Confrence Semi-Finals', 'Confrence Finals','NBA Finals', 
                      'Champions' ]])
        elif choose_mode == 3:
            print("Thanks for playing!")
            break
        else:
            print("Error")

if __name__ == "__main__":
    main()