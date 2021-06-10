

class Board(object):
    """Represents a board in a game of dots"""
    def __init__(self, board_size):
        self.board_size = board_size
        self.added_connections = []
        self._setup_squares_and_connections()
        

    def _setup_squares_and_connections(self):
        """Sets up possible_connections and squares list which is needed for the game"""
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


    def add_connection(self, connection, colour):
        """Adds a connection to the game board and fills in a square if one filled.
        Connection is tuple containing 2 tuples with a point in each.
        Returns a bool indication if specified connection could be added"""
        if connection in self.added_connections:
            return False
        elif connection not in self.possible_connections:
            return False
        self.added_connections.append(connection)
        for square in self.squares:
            if connection in square:
                if square[4] == None:
                    completed = True
                    for line_index in range(0,4):
                        if square[line_index] not in self.added_connections:
                            completed = False
                    if completed:
                        square[4] = colour
                
        
        


board = Board(7)
print("--------------")
print(board.added_connections)
print("--------------")
board.add_connection(((0,0),(0,1)), 'blue')
print(board.added_connections)
print(board.squares[0])
print("--------------")
board.add_connection(((1,0),(1,1)), 'orange')
print(board.added_connections)
print(board.squares[0])
print("--------------")
board.add_connection(((0,0),(1,0)), 'blue')
print(board.added_connections)
print(board.squares[0])
print("--------------")
board.add_connection(((0,1),(1,1)), 'orange')
print(board.added_connections)
print(board.squares[0])
print("--------------")
board.add_connection(((0,1),(0,2)), 'blue')
print(board.added_connections)
print(board.squares[1])
print("--------------")
board.add_connection(((1,1),(1,2)), 'orange')
print(board.added_connections)
print(board.squares[1])
print("--------------")
board.add_connection(((0,2),(1,2)), 'blue')
print(board.added_connections)
print(board.squares[1])
print("--------------")


    
        




