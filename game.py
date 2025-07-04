import pandas as pd 
import random
import time

def load_existing():
    team_name = input("What is your team name?\n")

    try:
        df = pd.read_excel(f"{team_name}.xlsx")
        pg = df.iloc[-1]['PG']
        sg = df.iloc[-1]['SG']
        pf = df.iloc[-1]['PF']
        sf = df.iloc[-1]['SF']
        c = df.iloc[-1]['C']
    except FileNotFoundError:
        print("Error Can't Find Team")
    return df, team_name, pg, sg, sf, pf, c

def create_new():
    team_name = input("What is your team name?\n")
    time.sleep(1)
    df = pd.DataFrame([[2025,0,0,0,0,0,0,0,0,0,0,0,0]], columns=['Year','Games Won', 'Games Lost', 'First Round',
                                                                 'Confrence Semi-Finals', 'Confrence Finals', 
                                                                'NBA Finals', 'Champions', 'PG', 'SG', 'SF', 'PF', 'C'])
    print(f"Welcome {team_name}! Now it's time for the 2025 NBA Expansion Draft!")
    time.sleep(3)
    pg = random.randint(1,6)
    df.at[0, 'PG'] = pg
    print(f"In the first round of the 2025 NBA Expansion Draft the {team_name} select a {pg} overall Point Guard!")
    time.sleep(3)
    sg = random.randint(1,6)
    df.at[0, 'SG'] = sg
    print(f"In the second round of the 2025 NBA Expansion Draft the {team_name} select a {sg} overall Shooting Guard!")
    time.sleep(3)
    sf = random.randint(1,6)
    df.at[0, 'SF'] = sf
    print(f"In the third round of the 2025 NBA Expansion Draft the {team_name} select a {sf} overall Small Forward!")
    time.sleep(3)
    pf = random.randint(1,6)
    df.at[0, 'PF'] = pg
    print(f"In the four round of the 2025 NBA Expansion Draft the {team_name} select a {pf} overall Power Forward")
    time.sleep(3)
    c = random.randint(1,6)
    df.at[0, 'C'] = c
    print(f"In the fifth round of the 2025 NBA Expansion Draft the {team_name} select a {c} overall Center!")
    time.sleep(3)
    print("That concludes the 2025 NBA Expansion Draft!")
    return df,team_name,pg,sg,sf,pf,c

def offseason(df):
    last_row = df.iloc[-1]
    pg, sg, sf, pf, c = last_row['PG'], last_row['SG'], last_row['SF'], last_row['PF'], last_row['C']
    print(f"Welcome to the {last_row['Year']} Offseaon!")
    time.sleep(5)
    print(f"Your current roster: \n 1. PG: {pg}\n2. SG: {sg}\n 3. SF: {sf}\n 4. PF: {pf} \n 5. C : {c}")
    time.sleep(5)
    draft_choice = input("Welcome to the NBA Draft! What position do you want to draft?\n")
    new_value = random.randint(1, 10)
    time.sleep(3)
    if draft_choice.lower() == 'pg':
        print(f"You drafted a {new_value} overall PG\n")
        pg = new_value
    elif draft_choice.lower() == 'sg':
        print(f"You drafted a {new_value} overall SG\n")
        sg = new_value
    elif draft_choice.lower() == 'sf':
        print(f"You drafted a {new_value} overall SF\n")
        sf = new_value
    elif draft_choice.lower() == 'pf':
        print(f"You drafted a {new_value} overall PF\n")
        pf = new_value
    elif draft_choice.lower() == 'c':
        print(f"You drafted a {new_value} overall C\n")
        c = new_value
    else:
        print("No players drafted this season\n")
    time.sleep(3)
    print("Welcome to NBA Free Agency")
    time.sleep(3)
    chance = random.randint(1,3)
    pg_chance = random.randint(1,3)
    sg_chance = random.randint(1,3)
    pf_chance = random.randint(1,3)
    sf_chance = random.randint(1,3)
    c_chance = random.randint(1,3)
    if chance == pg_chance:
        time.sleep(3)
        print("Sorry your Point Guard Left in Free Agency!")
        time.sleep(3)
        new_rating = random.randint(1,10)
        pg = new_rating
        print(f"Your new Point Guard is a {pg} overall!")
    if chance == sg_chance:
        time.sleep(3)
        print("Sorry your Shooting Guard Left in Free Agency!")
        time.sleep(3)
        new_rating = random.randint(1,10)
        sg = new_rating
        print(f"Your new Shooting Guard is a {sg} overall!")
    if chance == pf_chance:
        time.sleep(3)
        print("Sorry your Power Foward Left in Free Agency!")
        time.sleep(3)
        new_rating = random.randint(1,10)
        pf = new_rating
        print(f"Your new Power Foward is a {pf} overall!")
    if chance == sf_chance:
        time.sleep(3)
        print("Sorry your Small Foward Left in Free Agency!")
        time.sleep(3)
        new_rating = random.randint(1,10)
        sf = new_rating
        print(f"Your new Small Foward is a {sf} overall!")
    if chance == c_chance:
        time.sleep(3)
        print("Sorry your Center Left in Free Agency!")
        time.sleep(3)
        new_rating = random.randint(1,10)
        c = new_rating
        print(f"Your new Center is a {c} overall!")

    free_agent = input("What position do you want to pursue in Free Agency?\n")
    free_agent_chance = random.randint(1,2)
    your_chance = random.randint(1,2)
    free_agent_ranking = random.randint(1,10)
    if free_agent.lower() == 'pg':
        if free_agent_chance == your_chance:
            decision = input(f"A {free_agent_ranking} overall Point Guard wants to join your team. Do you want to sign him?")
            if decision.lower() == 'yes':
                print("Congrats on the point guard signing")
                pg = free_agent_ranking
            else:
                print("Free Agentcy is Over")
        else:
            print("Sorry no Point Guards want to join your team")
    elif free_agent.lower() == 'sg':
        if free_agent_chance == your_chance:
            decision = input(f"A {free_agent_ranking} overall Shooting Guard wants to join your team. Do you want to sign him?")
            if decision.lower() == 'yes':
                print("Congrats on the Shooting Guard signing")
                sg = free_agent_ranking
            else:
                print("Free Agentcy is Over")
        else:
            print("Sorry no Shooting Guards want to join your team")
    
    elif free_agent.lower() == 'sf':
        if free_agent_chance == your_chance:
            decision = input(f"A {free_agent_ranking} overall Small Foward wants to join your team. Do you want to sign him?")
            if decision.lower() == 'yes':
                print("Congrats on the Small Foward signing")
                sf = free_agent_ranking
            else:
                print("Free Agentcy is Over")
        else:
            print("Sorry no Small Fowards want to join your team")
    elif free_agent.lower() == 'pf':
        if free_agent_chance == your_chance:
            decision = input(f"A {free_agent_ranking} overall Power Foward wants to join your team. Do you want to sign him?")
            if decision.lower() == 'yes':
                print("Congrats on the Poward Foward signing")
                pf = free_agent_ranking
            else:
                print("Free Agentcy is Over")
        else:
            print("Sorry no Poward Fowards want to join your team")
    elif free_agent.lower() == 'c':
        if free_agent_chance == your_chance:
            decision = input(f"A {free_agent_ranking} overall Center wants to join your team. Do you want to sign him?")
            if decision.lower() == 'yes':
                print("Congrats on the Center signing")
                c = free_agent_ranking
            else:
                print("Free Agentcy is Over")
        else:
            print("Sorry no Centers want to join your team")
    else:
        print("Free Agency is Over!")

    return pg, sg, sf, pf, c

def NBA_Finals(new_row):
    time.sleep(3)
    new_row['NBA Finals'] = 1
    print(f"Welcome to the NBA Finals! You will now play Rock Paper Scissors to win\n")
    player_wins = 0
    computer_wins = 0

    while True:
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
    time.sleep(3)
    new_row['Confrence Finals'] = 1
    print(f"Welcome to the Confrence Finals!")
    player_wins = 0
    opponent_wins = 0
    games = 1
    while True:
        time.sleep(3)
        opponent_overall = random.randint(35,50)
        if team_overall > opponent_overall:
            print(f"Congrats you won Game {games} of the Confrence Finals!")
            player_wins = player_wins + 1
            games = games + 1
        else:
            print(f"Sorry you lost Games {games} of the Confrence Finals!")
            opponent_wins = opponent_wins + 1
            games = games + 1
        
        if player_wins == 4:
            time.sleep(3)
            print("Congrats you won the series and advance to NBA Finals")
            NBA_Finals(new_row)
            break
        if opponent_wins == 4:
            time.sleep(3)
            print("Sorry you lost the series")
            break

def Semi_Finals(new_row, team_overall):
    time.sleep(3)
    new_row['Confrence Semi-Finals'] = 1
    print(f"Welcome to the Confrence Semi Finals!")
    player_wins = 0
    opponent_wins = 0
    games = 1
    while True:
        time.sleep(3)
        opponent_overall = random.randint(30,50)
        if team_overall > opponent_overall:
            print(f"Congrats you won Game {games} of the Confrence Semi Finals!")
            player_wins = player_wins + 1
            games = games + 1
        else:
            print(f"Sorry you lost Game {games} of the Confrence Semi Finals!")
            opponent_wins = opponent_wins + 1
            games = games + 1
        
        if player_wins == 4:
            time.sleep(3)
            print("Congrats you won the series and advance to Confrence Finals!")
            Confrence_Finals(new_row, team_overall)
            break
        if opponent_wins == 4:
            time.sleep(3)
            print("Sorry you lost the series")
            break

def first_round(new_row,seed, team_overall):
    print(f"Welcome to the {new_row['Year']} playoffs")
    new_row['First Round'] = 1
    player_wins = 0
    opponent_wins = 0
    games = 1
    while True:
        time.sleep(3)
        opponent_overall = random.randint(20,50)
        if team_overall > opponent_overall:
            print(f"Congrats you won Game {games} of the First Round")
            player_wins = player_wins + 1
            games = games + 1
        else:
            print(f"Sorry you lost Game {games} of the First Round!")
            opponent_wins = opponent_wins + 1
            games = games + 1
        
        if player_wins == 4:
            time.sleep(3)
            print("Congrats you won the series and advance to Confrence Semi-Finals!")
            Semi_Finals(new_row, team_overall)
            break
        if opponent_wins == 4:
            time.sleep(3)
            print("Sorry you lost the series and are elimated from the playoffs")
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
    
    time.sleep(3)
    for i in range(1,42):
        opponent_overall = random.randint(15,50)
        if team_overall > opponent_overall:
            new_row['Games Won'] = new_row['Games Won'] + 1
        else:
            new_row['Games Lost'] = new_row['Games Lost'] + 1

    print(f"Welcome to the NBA Trade Deadline! Halfway through the seasom your record is {new_row['Games Won']}:{new_row['Games Lost']}")
    trade_prob = random.randint(1,3)
    trade_prob_yes = random.randint(1,3)
    trade_pos = random.randint(1,5)
    trade_overall = random.randint(1,10)
    if trade_prob == trade_prob_yes:
        if trade_pos == 1:
            trade = int(input("A Team wants to trade a PG with you.\n 1. Accept Trade \n 2. Decline Trade"))
            if trade == 1:
                print(f"Congrats on the new {trade_overall} overall PG")
                pg = trade_overall 
            else:
                print(f"You declined the trade for a {trade_overall} overall PG")  
        elif trade_pos == 2:
            trade = int(input("A Team wants to trade a SG with you.\n 1. Accept Trade \n 2. Decline Trade"))
            if trade == 1:
                print(f"Congrats on the new {trade_overall} overall SG")
                sg = trade_overall 
            else:
                print(f"You declined the trade for a {trade_overall} overall SG")  
        
        elif trade_pos == 3:
            trade = int(input("A Team wants to trade a SF with you.\n 1. Accept Trade \n 2. Decline Trade"))
            if trade == 1:
                print(f"Congrats on the new {trade_overall} overall SF")
                sf = trade_overall 
            else:
                print(f"You declined the trade for a {trade_overall} overall SF")  

        elif trade_pos == 4:
            trade = int(input("A Team wants to trade a PF with you.\n 1. Accept Trade \n 2. Decline Trade"))
            if trade == 1:
                print(f"Congrats on the new {trade_overall} overall PF")
                pf = trade_overall 
            else:
                print(f"You declined the trade for a {trade_overall} overall PF")  

        else:
            trade = int(input("A Team wants to trade a C with you.\n 1. Accept Trade \n 2. Decline Trade"))
            if trade == 1:
                print(f"Congrats on the new {trade_overall} overall C")
                c = trade_overall 
            else:
                print(f"You declined the trade for a {trade_overall} overall C")  
    else:
        print("No Team wants to trade with you")
    
    time.sleep(2)

    for i in range(1,42):
        opponent_overall = random.randint(15,50)
        if team_overall > opponent_overall:
            new_row['Games Won'] = new_row['Games Won'] + 1
        else:
            new_row['Games Lost'] = new_row['Games Lost'] + 1
    
    Percentage = new_row['Games Won'] / 82
    print(f" Your record was {new_row['Games Won']}:{new_row['Games Lost']}")
    time.sleep(3)
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
        df,team_name,pg,sg,sf,pf,c = load_existing()
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