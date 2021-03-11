class TaTeTi():
    def __init__(self,board=" "):
        self.valid = ['1.1', '1.2', '1.3',
                      '2.1', '2.2', '2.3',
                      '3.1', '3.2', '3.3']
        #self.piece = piece
        self.board = [" " for _ in range(9)]
        if board != " ":
            self.board = board

    def full(self):
        for i in self.board:
            if i == " ":
                return False 
        return True 

    def win(self):
        if self.board[0] == "x" and self.board[1] == "x" and self.board[2] == "x":
            return True
        if self.board[3] == "x" and self.board[4] == "x" and self.board[5] == "x":
            return True
        if self.board[6] == "x" and self.board[7] == "x" and self.board[8] == "x":
            return True
        if self.board[0] == "x" and self.board[3] == "x" and self.board[6] == "x":
            return True
        if self.board[0] == "x" and self.board[4] == "x" and self.board[8] == "x":
            return True
        if self.board[1] == "x" and self.board[4] == "x" and self.board[7] == "x":
            return True
        if self.board[2] == "x" and self.board[5] == "x" and self.board[8] == "x":
            return True
        if self.board[2] == "x" and self.board[4] == "x" and self.board[6] == "x":
            return True         

        if self.board[0] == "o" and self.board[1] == "o" and self.board[2] == "o":
            return True
        if self.board[3] == "o" and self.board[4] == "o" and self.board[5] == "o":
            return True
        if self.board[6] == "o" and self.board[7] == "o" and self.board[8] == "o":
            return True
        if self.board[0] == "o" and self.board[3] == "o" and self.board[6] == "o":
            return True
        if self.board[0] == "o" and self.board[4] == "o" and self.board[8] == "o":
            return True
        if self.board[1] == "o" and self.board[4] == "o" and self.board[7] == "o":
            return True
        if self.board[2] == "o" and self.board[5] == "o" and self.board[8] == "o":
            return True
        if self.board[2] == "o" and self.board[4] == "o" and self.board[6] == "o":
            return True
        return False
        
    def validate(self,pos):
        if self.board[pos-1] == " ":
            return True
        return False

    def assign(self,pos,piece):
        if self.board[pos-1] != " ":
            raise Exception
        self.board[pos-1] = piece  

    def draw_board(self):
        lista = [" " for _ in range(9)]
        for i in range(9):
            if self.board[i] == " ":
                lista[i] = i+1
                continue
            lista[i] = self.board[i]
        display = '\n {} | {} | {} \n---+---+---\n {} | {} | {} \n---+---+---\n {} | {} | {} \n'.format(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8])
        return display
    




