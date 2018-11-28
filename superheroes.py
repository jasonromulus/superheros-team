import random

class Hero:
    def __init__(self, name, health = 100):
        # Initialize starting values
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense.
        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """
        total_defense = 0
        for armor in self.armors:
            total_defense += armor.defend()
        if self.health == 0:
            total_defense = 0
        return total_defense

    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the hero's health.
        If the hero dies update number of deaths.
        """
        self.health = self.health - damage_amt
        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        self.kills += num_kills

        """
        This method should add the number of kills to self.kills
        """


    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_attack = 0
        if self.abilities != None:
            for ability in self.abilities:
                print("hero attack function: ")
                print(ability)
                total_attack += ability.attack()
        return total_attack
        # total_attack = 0
        # for add_attack in self.abilities:
        #     total_attack += add_attack.attack()
        # return total_attack
        # test by unit
class Ability:
    def __init__(self, name, attack_strength): # Initalize starting values
        # Set Ability name
        self.name = name
        # Set attack strength
        self.attack_strength = attack_strength

    def attack(self): # Return attack value
        # Calculate lowest attack value as an integer
        lowest_attack_value = self.attack_strength // 2
        # Use random.randit(a, b) to select a random attack value.
        attack_strength = random.randint(lowest_attack_value, self.attack_strength)
        # Return attack value between 0 and the full attack
        return attack_strength

    def update_attack(self, attack_strength): # Update attack value
        self.attack_strength = attack_strength
    

class Weapon(Ability):
    def attack(self):
        """
        This method should return a random value between 0
        and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """

        return random.randint(0, self.attack_strength)
class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength. """
        self.name = name
        self.defense = defense

    def defend(self):
        """
        Return a random value between 0 and the
        initialized defend strength.
        """
        return random.randint(0, self.defense)

class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()
        self.team_kills = 0
        self.team_health = 0

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)
        self.team_health += Hero.health

    def remove_hero(self, name):
        """
          Remove hero from heroes list.
          If Hero isn't found return 0.
        """
        if len(self.heroes) == 0:
            return 0
        else:
            for hero in self.heroes:
                if hero.name == name:
                    self.heroes.remove(hero)
                else:
                    return 0

      
        

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.
        It should call add_kill() on each hero with the number of kills made.
        """
        total_attack = 0
        for hero in self.heroes:
            total_attack += hero.attack()

        other_team_defense = other_team.defend(total_attack)
        for hero in self.heroes:
            hero.add_kill(other_team_defense)

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
        Return number of heroes killed in attack.
        """
        total_defense = 0
        for hero in self.heroes:
            total_defense += hero.defend()
        excess_damage = damage_amt - total_defense

        if excess_damage > 0:
            self.team_health -= excess_damage
            return self.deal_damage(excess_damage)
        else:
            return 0

    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heroes that died in attack.
        """
        total_damage = damage // len(self.heroes)
        total_deaths = 0
        for hero in self.heroes:
            hero.take_damage(total_damage)
            if hero.health <=0:
                total_deaths += 1
        return total_deaths

    def revive_heroes(self, health = 100):
        self.team_health = 0
        """
        This method should reset all heroes health to their original starting value.
        """
        for hero in self.heroes:
            hero.health = hero.start_health
            self.team_health += hero.health
    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.
        This data must be output to the terminal.
        """
        print("cats")
        for kill in self.heroes:
            print(kill.name + "Kills: " + str(kill.kills) + " Deaths:" + str(kill.deaths))

    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """
        for hero in self.heroes:
            if hero.add_kill:
                print(hero + " has killed a member of the other team!")


    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """

        if self.heroes != None:
            for hero in self.heroes:
                if name == hero.name:
                    return hero
                else:
                    return 0
        else:
            return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            name = hero.name
            print(name)

class Arena:
    def __init__(self, team_size=1):

        self.team_one = None
        self.team_two = None
        self.team_size = team_size



    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        self.team_one = Team(input("Please name the first team: "))
        print("It's time to play! Both teams have " + str(self.team_size) + " players")
        for i in range(self.team_size):
            print("Hero number {}. ".format(i))
            self.team_one.add_hero(create_hero())

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        self.team_two = Team(input("Please name the second team: "))
        print("It's time to play! Both teams have " + str(self.team_size) + " players")
        for i in range(self.team_size):
            print("Hero number {}. ".format(i))
            self.team_two.add_hero(create_hero())

    def team_battle(self):
        """
        This method should continue to battle teams until one or both teams are dead.
        """
        print("loo loo lemon")
        print(self.team_one.team_health)
        print(self.team_two.team_health)
        while(self.team_one.team_health>0 and self.team_two.team_health>0):
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)
            print("hi")
            self.show_stats()
        if(self.team_one.heroes[0].deaths==1):
            return self.team_one.name
        return self.team_two.name


    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        self.team_one.stats()
        self.team_two.stats()

def create_hero():
    hero = Hero(input("Please name your hero: "))

    print("Please give your hero abilities: ")
    i = None
    while(i != "done".lower()):
        hero.add_ability(create_ability())
        i = input("Add more abilities? Press enter to keep adding or type 'done' to finish adding heroes. ")

    print("Please give your hero weapons: ")
    i = None
    while(i != "done".lower()):
        hero.add_ability(create_weapon())
        i = input("Add more weapons? Press enter to keep adding or type 'done' to finish adding weapons. ")

    print("Please give your hero armor: ")
    i = None
    while(i != "done".lower()):
        hero.add_armor(create_armor())
        i = input("Add more armor? Press enter to keep adding or type 'done' to finish adding armor. ")
    print("Your hero is ready!! It's time to play!")
    return hero

def create_ability():
    ability = Ability(input("What is the name of the ability? "), int(input("What is the strength level of the ability? ")))
    return ability

def create_weapon():
    weapon = Weapon(input("What is the name of the weapon? "), int(input("What is the strength level of the weapon? ")))
    return weapon

def create_armor():
    armor = Armor(input("What is the name of the armor? "), int(input("What is the strength level of the armor? ")))
    return armor



if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
