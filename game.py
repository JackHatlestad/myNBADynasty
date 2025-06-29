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
    pg = random.randint(1,6)
    df.at[0, 'PG'] = pg
    print(f"In the first round of the 2025 NBA Expansion Draft the {team_name} select a {pg} overall Point Guard!")
    time.sleep(5)
    sg = random.randint(1,6)
    df.at[0, 'SG'] = sg
    print(f"In the second round of the 2025 NBA Expansion Draft the {team_name} select a {sg} overall Shooting Guard!")
    time.sleep(5)
    sf = random.randint(1,6)
    df.at[0, 'SF'] = sf
    print(f"In the third round of the 2025 NBA Expansion Draft the {team_name} select a {sf} overall Small Forward!")
    time.sleep(5)
    pf = random.randint(1,6)
    df.at[0, 'PF'] = pg
    print(f"In the four round of the 2025 NBA Expansion Draft the {team_name} select a {pf} overall Power Forward")
    time.sleep(5)
    c = random.randint(1,6)
    df.at[0, 'C'] = c
    print(f"In the fifth round of the 2025 NBA Expansion Draft the {team_name} select a {c} overall Center!")
    time.sleep(5)
    print("That concludes the 2025 NBA Expansion Draft!")
    return df,team_name,pg,sg,sf,pf,c

def offseason(df):
    last_row = df.iloc[-1]
    pg, sg, sf, pf, c = last_row['PG'], last_row['SG'], last_row['SF'], last_row['PF'], last_row['C']
    print(f"Welcome to the {last_row['Year']} Offseaon!")
    time.sleep(5)
    print(f"Your current roster: \n 1. PG: {pg}\n2. SG: {sg}\n 3. SF: {sf}\n 4. PF: {pf} \n 5. C : {c}")
    time.sleep(5)
    draft_choice = input("Welcome to the NBA Draft! What position do you want to draft?")
    new_value = random.randint(1, 10)
    
    if draft_choice.lower() == 'pg':
        print(f"You drafted a {new_value} overall PG")
        pg = new_value
    elif draft_choice.lower() == 'sg':
        print(f"You drafted a {new_value} overall SG")
        sg = new_value
    elif draft_choice.lower() == 'sf':
        print(f"You drafted a {new_value} overall SF")
        sf = new_value
    elif draft_choice.lower() == 'pf':
        print(f"You drafted a {new_value} overall PF")
        pf = new_value
    elif draft_choice.lower() == 'c':
        print(f"You drafted a {new_value} overall C")
        c = new_value
    else:
        print("Invalid choice. No upgrade this offseason.")
    time.sleep(1)
    print("Welcome to NBA Free Agency")
    time.sleep(1)
    chance = random.randint(1,10)
    pg_chance = random.randint(1,10)
    sg_chance = random.randint(1,10)
    pf_chance = random.randint(1,10)
    sf_chance = random.randint(1,10)
    c_chance = random.randint(1,10)
    if chance == pg_chance:
        print("Sorry your Point Guard Left in Free Agency!")
        time.sleep(1)
        new_rating = random.randint(1,10)
        pg = new_rating
        print(f"Your new Point Guard is a {pg} overall!")
    if chance == sg_chance:
        print("Sorry your Shooting Guard Left in Free Agency!")
        time.sleep(1)
        new_rating = random.randint(1,10)
        sg = new_rating
        print(f"Your new Shooting Guard is a {sg} overall!")
    if chance == pf_chance:
        print("Sorry your Power Foward Left in Free Agency!")
        time.sleep(1)
        new_rating = random.randint(1,10)
        pf = new_rating
        print(f"Your new Power Foward is a {pf} overall!")
    if chance == sf_chance:
        print("Sorry your Small Foward Left in Free Agency!")
        time.sleep(1)
        new_rating = random.randint(1,10)
        sf = new_rating
        print(f"Your new Small Foward is a {sf} overall!")
    if chance == c_chance:
        print("Sorry your Center Left in Free Agency!")
        time.sleep(1)
        new_rating = random.randint(1,10)
        c = new_rating
        print(f"Your new Center is a {c} overall!")

    return pg, sg, sf, pf, c

def NBA_Finals(new_row):
    new_row['NBA Finals'] = 1
    player_wins = 0
    computer_wins = 0

    while True:
        time.sleep(5)
        computer_choice = random.randint(0,2)
        player_choice = input("What is your choice?\n")

        if player_choice.lower() == 'rock':
            if computer_choice == 0:
                print("The computer choose rock, it's a tie.")
                print(f"The series is {player_wins} to {computer_wins}!")

            elif computer_choice == 1:
                print("The computer choose paper, you lose!")
                computer_wins = computer_wins + 1
                print(f"The series is {player_wins} to {computer_wins}!")
            elif computer_choice == 2:
                print("The computer choose scissors, you win!")
                player_wins = player_wins + 1
                print(f"The series is {player_wins} to {computer_wins}!")

        elif player_choice.lower() == 'paper':
            if computer_choice == 0:
                print("The computer choose rock, you win!")
                player_wins = player_wins + 1
                print(f"The series is {player_wins} to {computer_wins}!")
            elif computer_choice == 1:
                print("The computer choose paper, it's a tie.")
                print(f"The series is {player_wins} to {computer_wins}!")
            elif computer_choice == 2:
                print("The computer choose scissors, you lose!")
                computer_wins = computer_wins + 1
                print(f"The series is {player_wins} to {computer_wins}!")

        elif player_choice.lower() == 'scissors':
            if computer_choice == 0:
                print("The computer choose rock, you lose!")
                computer_wins = computer_wins + 1
                print(f"The series is {player_wins} to {computer_wins}!")

            elif computer_choice == 1:
                print("The computer choose paper, you win!")
                player_wins = player_wins + 1
                print(f"The series is {player_wins} to {computer_wins}!")

            elif computer_choice == 2:
                print("The computer choose scissors, it's a tie.")
                print(f"The series is {player_wins} to {computer_wins}!")
        else:
            print("Error please choose Rock, Paper, or Scissors")
    
        if player_wins == 4:
            print("Congratulations" + "! You won the NBA Finals!") 
            new_row['Champions'] = 1
            break
            
        if computer_wins == 4:
            print("Sorry you lost the NBA Finals!")
            break

def Confrence_Finals(new_row,team_overall):
    new_row['Confrence Finals'] = 1
    print(f"Welcome to the Confrence Finals!")
    player_wins = 0
    opponent_wins = 0
    while True:
        time.sleep(5)
        opponent_overall = random.randint(35,50)
        if team_overall > opponent_overall:
            print(f"Congrats you won game of the First Round!")
            player_wins = player_wins + 1
        else:
            print(f"Sorry you lost game  of the First Round!")
            opponent_wins = opponent_wins + 1
        
        if player_wins == 4:
            print("Congrats you won the series and advance to Confrence Fiansl")
            NBA_Finals(new_row)
            break
        if opponent_wins == 4:
            print("Sorry you lost the series")
            break

def Semi_Finals(new_row, team_overall):
    new_row['Confrence Semi-Finals'] = 1
    print(f"Welcome to the Confrence Semi Finals!")
    player_wins = 0
    opponent_wins = 0
    while True:
        time.sleep(5)
        opponent_overall = random.randint(30,50)
        if team_overall > opponent_overall:
            print(f"Congrats you won game of the First Round!")
            player_wins = player_wins + 1
        else:
            print(f"Sorry you lost game  of the First Round!")
            opponent_wins = opponent_wins + 1
        
        if player_wins == 4:
            print("Congrats you won the series and advance to Confrence Fiansl")
            Confrence_Finals(new_row, team_overall)
            break
        if opponent_wins == 4:
            print("Sorry you lost the series")
            break

    print("Congrats")

def first_round(new_row,seed, team_overall):
    print(f"Welcome to the {new_row['Year']} playoffs")
    new_row['First Round'] = 1
    player_wins = 0
    opponent_wins = 0
    while True:
        time.sleep(5)
        opponent_overall = random.randint(20,50)
        if team_overall > opponent_overall:
            print(f"Congrats you won game of the First Round!")
            player_wins = player_wins + 1
        else:
            print(f"Sorry you lost game  of the First Round!")
            opponent_wins = opponent_wins + 1
        
        if player_wins == 4:
            print("Congrats you won the series and advance to Confrence Semi Fiansl")
            Semi_Finals(new_row, team_overall)
            break
        if opponent_wins == 4:
            print("Sorry you lost the series")
            break
        
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
    

    for i in range(1,83):
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
        first_round(new_row,seed, team_overall)
    elif Percentage > 0.60:
        seed = random.randint(3,6)
        print(f"Congrats you've made the playoffs as a {seed} seed")
        first_round(new_row,seed, team_overall)
    elif Percentage > 0.50:
        seed = random.randint(7,8)
        print(f"Congrats you've made the playoffs as a {seed} seed")
        first_round(new_row,seed, team_overall)
    else:
        print("You missed the playoffs!")
        
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
            pg,sg,sf,pf,c =  offseason(df)
        elif choose_mode == 2:
            print(df[['Year','Games Won', 'Games Lost', 'First Round', 'Confrence Semi-Finals', 'Confrence Finals','NBA Finals', 
                      'Champions']])
        elif choose_mode == 3:
            print("Thanks for playing!")
            df.to_excel(f"{team_name}.xlsx", index=False)
            break
        else:
            print("Error")

if __name__ == "__main__":
    main()