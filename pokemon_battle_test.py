import random

def faintcheck():
    if dmg_counter >= enemy[3]:
        print("Enemy " + str(enemy[0]) + " fainted!")
        print("You gained " + str(enemy[4]/2) + " XP!")
        

# Tuples will have values Name/Attack/Defense/HP/XP
creature_list = [
    ("Pikachu", 10, 8, 100, 400),
    ("Pidgey", 8, 10, 100, 300),
    ("Snorlax", 15, 20, 400, 800),
    ("Charizard", 40, 30, 700, 1200),
    ("Mewtwo", 80, 60, 1000, 1500),
    ]

dmg_counter = 0
defend_counter = 0


#Selects a random creature to battle
enemy = creature_list[(random.randint(0,4))]
print(enemy)

                      
#Battle Begins
print("A wild " + str(enemy[0]) + " appears!")

#First Choice
while dmg_counter < enemy[3]:
    print("What is your next move? \n- Attack \n- Defend \n- Run")
    move = ""
    dmg = 0
    defend_counter = 0
    move = input()
    
    #Attack Code
    if move == "Attack":
        print("\nWhat kind of attack? \nDash \nThunderbolt")
        attack = input()
        if attack == "Dash":
            dmg = random.randint(1,5)
            dmg_counter += dmg
            print("Dealt " + str(dmg) + " damage!")
            faintcheck()
        if attack == "Thunderbolt":
            dmg = random.randint(5,10)
            dmg_counter += dmg
            print("Dealt " + str(dmg) + " damage!")
            faintcheck()
        if attack == "Kill":
            dmg = 1000
            dmg_counter += dmg
            print("Dealt " + str(dmg) + " damage!")
            faintcheck()

    #Defend Code
    if move == "Defend":
        defend_counter = random.randint(2,5)
        print("Defending for " + str(defend_counter) + " points.")

    #Run Code
    if move == "Run":
        print("You ran from the battle!")
        break
