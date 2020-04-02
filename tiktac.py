
class Tiktoc:
    # class_variable = "Dummy"
    def __init__(self):# constructor
        """
        initialize the 3 x 3array & two symbol's symbols
        symbol1 = X
        symbol2 = O
        """
        self.rows, self.cols =(3,3)
        self.arr = [[""]*self.cols for r in range(self.rows)]
        self.symbol1 = 'X'
        self.symbol2 = 'O'

    def print_array(self):
        """
        print the array
        """
        for row in self.arr: 
            print(row) 


    def move_turn(self, curr_symbol):
        """
        return the other symbol symbol
        """
        if curr_symbol== self.symbol1:
            return self.symbol2
        else:
            return self.symbol1
        

    def accept_input(self, curr_symbol):
        '''
        accept and store the input from symbol
        '''
        while(True):
            state = "please enter space separate location of %s: "%(curr_symbol)
            raw = input(state) # "0 1"
            raw = raw.split(" ") #["0", "1"]
            try:
                row= int(raw[0])
            except Exception:
                print ("wrong input!! please enter  valid number")
            try:
                col = int(raw[1])
            except Exception:
                print ("wrong input!! please enter  valid number")
            if (0 <= row <=2 )and (0 <= col <=2 ):
                self.arr[row][col] = curr_symbol
                break
            else:
                print ("wrong input!! please enter  valid number")


    def check_current_symbol_won(self, curr_symbol):
        """
        return bool
        """
        if self.arr[0][0]==self.arr[0][1]==self.arr[0][2]==curr_symbol:
            return True
        elif self.arr[1][0]==self.arr[1][1]==self.arr[1][2]==curr_symbol:
            return True
        elif self.arr[2][0]==self.arr[2][1]==self.arr[2][2]==curr_symbol:
            return True
        elif self.arr[0][0]==self.arr[1][0]==self.arr[2][0]==curr_symbol:
            return True
        elif self.arr[0][0]==self.arr[0][1]==self.arr[0][2]==curr_symbol:
            return True
        elif self.arr[0][1]==self.arr[1][1]==self.arr[2][1]==curr_symbol:
            return True
        elif self.arr[0][2]==self.arr[1][2]==self.arr[2][2]==curr_symbol:
            return True
        elif self.arr[0][0]==self.arr[1][1]==self.arr[2][2]==curr_symbol:
            return True
        elif self.arr[0][2]==self.arr[1][1]==self.arr[2][0]==curr_symbol:
            return True
        else:
            return False


    def run(self):
        """
        """
        empty_spaces=9
        curr_symbol= self.symbol1
        while(True):
            self.print_array()
            self.accept_input(curr_symbol)
            empty_spaces-=1 
            if  self.check_current_symbol_won(curr_symbol):
                print("congrats!! you won the game", curr_symbol)  
                break  
            if empty_spaces==0:
                print("nobody won")  
                break         
            curr_symbol=self.move_turn(curr_symbol)
            # self.print_array()
if __name__ == "__main__":
    tt = Tiktoc()
    tt.run()