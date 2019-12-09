import chess

from src.commands import request_command, PlayerCommand

class ChessGame:
    
    def __init__(self):
        self.board = chess.Board()
    
    def play(self, san_move: str):
        
        # if san_move in self.board.legal_moves:
        print(san_move)
        self.board.push_san(san_move)
        return True
        # else:
            # print("Move is not valid")
            # return False
    

def command_to_move(command: PlayerCommand) -> chess.Move:
    return f"{command.piece}{command.file}{command.rank}"
    
if __name__ == "__main__":
    game = ChessGame()
    
    while True:
        command = None
        while True:
            command = request_command()
            if command:
                break
            print("can't understard, try again")
                
        move = command_to_move(command)
        
        game.play(move)
        print(game.board)