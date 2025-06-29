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

def offseason():
    print("f")

def playoffs(new_row,seed, team_overall):
    print(f"Welcome to the {new_row['Year']} playoffs")
    new_row['First Round'] = 1
    print("Welcome to the first round")


def season(df,pg,sg,sf,pf,c):
    new_row = {
        'Year': df.iloc[-1]['Year'] + 1,
        'Games Won': 0,
        'Games Lost': 0,
        'First Round': 0,
        'Confrence Semi Finals': 0,
        'Confrence Finals': 0,
        'NBA Finals': 0,
        'Champions': 0,
        'PG': pg,
        'SG': sg,
        'SF': sf,
        'PF': pf,
        'C': c}
    
    team_overall = new_row['PG'] + new_row['SG'] + new_row['PF'] + new_row['SF'] + new_row['C']
    

    for i in range(1,82):
        opponent_overall = random.randint(5,50)
        if team_overall > opponent_overall:
            print(f"Congrats you won the game {i}!")
            new_row['Games Won'] = new_row['Games Won'] + 1
        else:
            print(f"Sorry you lost game {i}")
            new_row['Games Lost'] = new_row['Games Lost'] + 1
    
    Percentage = new_row['Games Won'] / 82
    print(f" You won {new_row['Games Won']} and lost {new_row['Games Lost']}")

    if Percentage > 0.80:
        seed = random.randint(1,2)
        print(f"Congrats you've made the playoffs as a {seed} seed")
        playoffs(new_row,seed, team_overall)
    elif Percentage > 0.60:
        seed = random.randint(3,6)
        print(f"Congrats you've made the playoffs as a {seed} seed")
        playoffs(new_row,seed, team_overall)
    elif Percentage > 0.50:
        seed = random.randint(7,8)
        print(f"Congrats you've made the playoffs as a {seed} seed")
        playoffs(new_row,seed, team_overall)
    else:
        print("You missed the playoffs!")
        offseason()
        
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
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
            df = season(df,pg,sg,sf,pf,c)
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