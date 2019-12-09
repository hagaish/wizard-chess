class PlayerCommand:
    def __init__(self, piece, file, rank):
        if not piece:
            raise Exception("Command piece is not defined")
        
        if not file:
            raise Exception("Command file is not deined")
        
        if not rank:
            raise Exception("Command rank is not defined")
        
        
        self.piece: str = piece_to_letter(piece)
        self.file: str = file.lower()
        self.rank: int = int(rank)
        
    def __repr__(self):
        return f"Piece: {self.piece} {self.file}{self.rank}"
    

def piece_to_letter(piece: str) -> str:
    piece_lower = piece.lower()
    
    matcher = {
        'king': 'K',
        'queen': 'Q',
        'knight': 'N',
        'rook': 'R',
        'bishop': 'B'
    }
    
    if piece_lower in matcher:
        return matcher[piece_lower]    
    raise Exception(f"Command piece unkown: {piece_lower}")
    
