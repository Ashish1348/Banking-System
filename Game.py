import random as r
print("\n\t\tShadow Spell game\n")
name = input("Enrer your charecter name : ")
if name == "" :
    name = "Warrior"
print("Welcome to the Shadow Spell Gane",name,"\n")

while True :
    
    inp = input("Are you redy for play the game?\nEnter 'yes' or 'no' : ")

    if inp == "yes" :
        print("\n\t\tEnjoy the game\n")
    elif inp == "no" :
        print("\nThank you",name,"\n")
        break
    else :
        print("\nInvalid input\nTry agin",name,"\n")
        continue

    class cha :
        def __init__(self):
            self.health = 100
            self.enemy = input("Enter enemy name ither press enter : ")
            
            if self.enemy == "":
                self.enemy = "Enemy"
            
            self.enemy_health = 100
            self.power = ("Fireboll"," ","Thunder","Iceblast")
            self.score = 0
            self.damage = 0
            self.damage2 = 0

        def show (slef) :
            print("\n\t\t//////////Status//////////\n")
            print("Charecter name :",name,"\tEnemy name :",slef.enemy,"\tScore :",slef.score)
            print("Charecter health :",slef.health,"\tEnemy health :",slef.enemy_health,"\n")

    class player (cha) :
        def attack (self):

            while True :
                if self.health == 0 and self.enemy_health == 0 :
                    print("\nMatch Draw")
                    print("Thank you",name,"for play the game\n")
                    break
                elif self.health == 0:
                    print(name,"you are eliminate\nGame over!!\n",name,"you lost the game")
                    print("\nThank you",name,"For play the game\n")
                    break
                elif self.enemy_health == 0:
                    print(self.enemy,"is eliminate\nweldone",name,"\nYou won the match")
                    print("Thank you",name,"for play the game\n")
                    break
                elif self.health == 100:
                    print("\nLet's fight",name,"\n")
                elif self.health > 10 :
                    print("\nCome on",name,"attack agin\n")
                elif self.health <= 10 :
                    print("\nAlsh!",name,"you are knocked\n")
                elif self.enemy_health <= 10 :
                    print("\nGreat",name,"you knocked the",self.enemy,"\n")
                
                print(name,"choice a optio and attack to the enemy - \n(1) Fireboll\n(2) Thunder\n(3) Iceblast")
                choice = input("Enter your choice : ")
                
                if choice == "1" :
                    print("\n",name,"attack with Fireboll")
                    self.damage = 30
                    self.score += 30
                elif choice == "2" :
                    print("\n",name,"attack with Thunder")
                    self.damage = 20
                    self.score += 20
                elif choice == "3" :
                    print("\n",name,"attack with Iceblast")
                    self.damage = 25
                    self.score += 25
                else :
                    print("\n",name,"you enter invalid option !!\nTry agin\n")

                self.enemy_health = max(0, self.enemy_health - self.damage)
                print(self.enemy,"health :",self.enemy_health)
                print("Score :",self.score)
                self.enemy_attack()

    class enemy (player) :
        def enemy_attack (self) :
            en_att = r.choice(self.power)

            if en_att == "Fireboll" :
                self.damage2 = 30
            elif en_att == "Thunder" :
                self.damage2 = 20
            elif en_att == "Iceblast" :
                self.damage2 = 25
            else :
                en_att = "Nothing"
                self.damage2 = 0
            
            print("\n",self.enemy,"attack with",en_att)
            self.health = max(0, self.health - self.damage2)
            print("Charecter health :",self.health,"\n")
    

    def save_csore():
        game_score = open("Game Score.txt","a")
        game_score.write("\nCharecter name :" +" "+ name + "\n" + "Score :" +" "+ str(c.score) + "\n___________\n")
        game_score.close()
        print("\n",name,"your score is save\n")

    def show_score():
        game_score = open("Game Score.txt","r")
        print(game_score.read())
        game_score.close()
        
    c = enemy()
    c.show()
    c.attack()
    c.show()
    save_csore()
    show_score()
    
    