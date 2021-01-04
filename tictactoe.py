
class Tictactoe():
    
    
    def __init__(self):
        self.position_values = {"t1" : " ",
                        "t2" : " ",
                        "t3" : " ",
                        "m1" : " ",
                        "m2" : " ",
                        "m3" : " ",
                        "b1" : " ",
                        "b2" : " ",
                        "b3" : " "}       
           
    def basic(self):
        """
        basic grib of tictactoe game
        """ 
        self.status = self.position_values.values()   
        print("\t %s | %s | %s \n\t---+---+---\n\t %s | %s | %s \n\t---+---+---\n\t %s | %s | %s "  
    % tuple(self.status))
    
    def ready(self):
        print("**** Welcome to TICTACTOE Game! ****")
        self.status = ("T1", "T2", "T3", "M1", "M2", "M3", "B1", "B2", "B3")
        print("\t %s | %s | %s \n\t---+---+---\n\t %s | %s | %s \n\t---+---+---\n\t %s | %s | %s "  
    % self.status)
        print("\nLet's start the game!")
        print("Player1 : O     Player2 : X")
        print("write a position!\n")

    def player1(self):     
        player1 = input("player1>>>>> ").lower()
        self.position_values[str(player1)]="O"
        self.basic()
        
    def player2(self):
        player2 = input("player2>>>>> ").lower()
        self.position_values[str(player2)]="X"
        self.basic()
    
    def play(self):
        for i in range(1,10):
            if i % 2 == 0:
                self.player2()
            else:
                self.player1()
    
    def win(self):
        self.p = list(self.position_values.values()) # for convenience 
        
        # row match case
        self.r_match = [self.p[i]==self.p[i+1]==self.p[i+2] for i in [0,3,6]]

        # column match case
        self.c_match = [self.p[i]==self.p[i+3]==self.p[i+6] for i in [0,1,2]]

        # diagonal match case
        self.d_match = [self.p[0]==self.p[4]==self.p[8], self.p[2]==self.p[4]==self.p[6]]

        self.result = self.r_match + self.c_match+ self.d_match
        print(self.result)
a = Tictactoe()
a.ready()
a.play()
a.win()


    