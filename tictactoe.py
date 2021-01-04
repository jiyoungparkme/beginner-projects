
class Tictactoe():   
    
    def __init__(self):
        self.positions = {"t1" : " ",
                        "t2" : " ",
                        "t3" : " ",
                        "m1" : " ",
                        "m2" : " ",
                        "m3" : " ",
                        "b1" : " ",
                        "b2" : " ",
                        "b3" : " "} 
        
        # for find winner                      
        self.positions_value = {"t1" : 0,
                        "t2" : 0,
                        "t3" : 0,
                        "m1" : 0,
                        "m2" : 0,
                        "m3" : 0,
                        "b1" : 0,
                        "b2" : 0,
                        "b3" : 0}  
    
    def basic(self):
        """
        basic grid of tictactoe game
        """ 
        self.status = self.positions.values()   
        print("\t %s | %s | %s \n\t---+---+---\n\t %s | %s | %s \n\t---+---+---\n\t %s | %s | %s "  
    % tuple(self.status))
    
    def ready(self):
        print("**** Welcome to TICTACTOE Game! ****")
        self.status = ("T1", "T2", "T3", "M1", "M2", "M3", "B1", "B2", "B3")
        print("\t%s |%s |%s \n\t---+---+---\n\t%s |%s |%s \n\t---+---+---\n\t%s |%s |%s "  
    % self.status)
        
        

    def player1(self):
        player1 = input("player1>>>>> ").lower()
        self.positions[str(player1)]="O"
        self.basic()
        self.positions_value[str(player1)] = 1
        
        
    def player2(self):
        player2 = input("player2>>>>> ").lower()
        self.positions[str(player2)]="X"
        self.basic()
        self.positions_value[str(player2)] = 4
     

    def play(self):
        print("\nLet's start the game!")
        print("Player1 : O     Player2 : X")
        print("write a position!\n")
        for i in range(1,10):
            win = self.win()
            if 3 in win:
                print("Player1 WIN!")
                break
            elif 12 in win:
                print("Player2 WIN!")
                break
            elif i == 9:
                if i % 2 == 0:
                    self.player2()
                else:
                    self.player1()
                print("The game ended in a tie.")
            else:
                if i % 2 == 0:
                    self.player2()
                else:
                    self.player1()

        
    def win(self):
        self.p = list(self.positions_value.values()) # for convenience 
        
        # row match case
        self.r_match = [self.p[i]+self.p[i+1]+self.p[i+2] for i in [0,3,6]]

        # column match case
        self.c_match = [self.p[i]+self.p[i+3]+self.p[i+6] for i in [0,1,2]]

        # diagonal match case
        self.d_match = [self.p[0]+self.p[4]+self.p[8], self.p[2]==self.p[4]==self.p[6]]

        self.result = self.r_match + self.c_match+ self.d_match
        return self.result

a = Tictactoe()
while True:

    a.ready()
    answer = input("Do you wanna play? y/n >> ").lower()
    if answer == "y":    
        a.play()
    else:
        print("Bye!")
        break


    