

class Board(object):
    """Represents a board in a game of dots"""
    def __init__(self, board_size):
        self.board_size = board_size
        self.added_connections = []
        self._setup_squares_and_connections()
        

    def _setup_squares_and_connections(self):
        self.possible_connections = []
        self.squares = []
        for row_num in range(0, self.board_size-1):
            for col_num in range(0, self.board_size-1):
                additions = [(0,0,0,1), (1,0,1,1), (0,0,1,0), (0,1,1,1)]
                square = [None, None, None, None, None]
                for index in range(len(additions)):
                    addition = additions[index]
                    square[index] = ((row_num + addition[0], col_num + addition[1]), (row_num + addition[2], col_num + addition[3]))
                    if ((row_num + addition[0], col_num + addition[1]), (row_num + addition[2], col_num + addition[3])) not in self.possible_connections:
                        self.possible_connections.append(((row_num + addition[0], col_num + addition[1]), (row_num + addition[2], col_num + addition[3])))
                self.squares.append(square)


board = Board(7)



    
        




