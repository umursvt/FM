import random
from goalkeeper import goalkeeper
from defenders import defenders
from midfielders import midfielders
from forwards import forwards


class FootballTeam:
    def __init__(self, team_name, formation):
        self.team_name = team_name
        self.formation = formation
        self.players = self.create_team()

    def create_team(self):
        positions = {
            "4-4-2": {"Kaleci": 1, "Defans": 4, "Orta Saha": 4, "Forvet": 2},
            "4-3-3": {"Kaleci": 1, "Defans": 4, "Orta Saha": 3, "Forvet": 3},
            "3-5-2": {"Kaleci": 1, "Defans": 3, "Orta Saha": 5, "Forvet": 2},
            "4-3-3":{"Kaleci": 1, "Defans": 4, "Orta Saha": 3, "Forvet": 3},
            "3-4-3":{"Kaleci": 1, "Defans": 3, "Orta Saha": 4, "Forvet": 3},
            "5-2-3-1":{"Kaleci": 1, "Defans": 5, "Orta Saha": 4, "Forvet": 1},
        }
        if self.formation not in positions:
            raise ValueError("Invalid formation")
        else:
            self.team_list =[]
            # Determine selected formation
            formation_selected=positions[self.formation]

            # To select a random goally
            self.goalkeeper_selected = []
            random_goalkeeper = random.choice(goalkeeper)
            self.goalkeeper_selected.append(random_goalkeeper)
            self.goally_name = self.goalkeeper_selected[0]['player_name']

            #  To select random defenders  
            self.defenders_selected=[]
            number_of_defenders = formation_selected['Defans']
            random_defenders = random.sample(defenders,number_of_defenders)
            self.defenders_selected.extend(random_defenders)
            
            self.defenders_name=[]
            for i in self.defenders_selected:
                name = i['player_name']
                self.defenders_name.append(name)

            # To select random midfielder
            self.midfielder_selected = []
            number_of_midfielder = formation_selected["Orta Saha"]
            random_midfielder = random.sample(midfielders,number_of_midfielder)
            self.midfielder_selected.extend(random_midfielder)

            self.midfielders_name = []
            for i in self.midfielder_selected:
                name = i['player_name']
                self.midfielders_name.append(name)

            # To select random forwards/forward
            self.forward_selected = []
            number_of_forward = formation_selected['Forvet']
            random_forwards = random.sample(forwards,number_of_forward)
            self.forward_selected.extend(random_forwards)

            self.forwards_name = []
            for i in self.forward_selected:
                name = i['player_name']
                self.forwards_name.append(name)

            # Add players to team list
            self.team_list.extend(self.goalkeeper_selected)
            self.team_list.extend(self.defenders_selected)
            self.team_list.extend(self.midfielder_selected)
            self.team_list.extend(self.forward_selected)

    def team_power(self):
        # Age effect.
        self.ages =[]
        for i in self.team_list:
            if i['yaş'] == 'RIP':
                age=['yaş'] == 0.5
                self.ages.append(age)
            else:
                age = (1/int(i['yaş']))*100
                self.ages.append(age)
        self.team_power_num = 0
        for i in self.ages:
            self.team_power_num +=i
        

        nation_list=[]
        self.unique_nation_list = []
        for i in self.team_list:
            nation = i['nation']
            nation_list.append(nation)
            if i['nation'] not in self.unique_nation_list:
                self.unique_nation_list.append(i['nation'])
        self.difference = (len(nation_list)-len(self.unique_nation_list))*7.5
        self.team_power_num += self.difference

        for i in self.team_list:
            yas = i.get('yaş',None)
            if yas =='RIP':
                self.team_power_num += 10
            elif int(yas) <= 23:
                self.team_power_num+=5
            elif 23<int(yas)<31:
                self.team_power_num +=2.5
            else:
                self.team_power_num -=1
        club_list=[]
        self.unique_club_list = []
        for i in self.team_list:
            club = i['club']
            club_list.append(club)
            if i['club'] not in self.unique_club_list:
                self.unique_club_list.append(i['club'])
        self.difference = (len(club_list)-len(self.unique_club_list))*5
        self.team_power_num += self.difference
        self.team_power_num = round(self.team_power_num,2)

        if self.team_power_num > 100:
            self.team_power_num = 100

        return  self.team_power_num

    def __str__(self):
        return f"""
        Team Name: {self.team_name}
        Formation: {self.formation}\n
        Goal Keeper:[{self.goally_name}]\n\n
        Defence: {self.defenders_name}\n\n
        Midfielder: {self.midfielders_name}\n\n
        Forward: {self.forwards_name}\n
        TEAM POWER: {self.team_power()}\n\n\n
        TEAM NATIONS: {self.unique_nation_list}

        """

team_home = FootballTeam("Lions of Coding","3-5-2")

team_away =FootballTeam("Sarıspor","4-4-2")

print(
    f"""
********************************************************************************************************
HOME:{team_home}
********************************************************************************************************
////////////////////////////////////////////////////////////////////////////////////////////////////////
********************************************************************************************************
AWAY:{team_away}
********************************************************************************************************
"""
)