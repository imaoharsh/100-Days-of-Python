class GamePlayer:
    power=None
    health=100
    level=0
    
    def Attack1(self):
        if(self.level >3):
            print("Level Unlocked you can use this attack")
        
        else:
            print("Not able to attack right now kindly unlock the level",self.level)
            
    def DisplayPlayerProfile(self):
        print(self.power,self.health,self.level)

print('-'*30)
Player1=GamePlayer()
Player1.power="Magician"
Player1.health="Strong"
Player1.level=4

Player1.DisplayPlayerProfile();
Player1.Attack1();

print('-'*30)

Player2=GamePlayer()
Player2.power="Technician"
Player2.health="Medium"
Player2.level=2

Player2.DisplayPlayerProfile();
Player2.Attack1();