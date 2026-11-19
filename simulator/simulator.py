skewb = "ABCDUV124"
# Solved skewb tag state in simulated puzzle

rmap = {'2': '5','5': '6', '6': '2', 'C': 'T', 'T': 'G', 'G': 'C', 'J': 'O', 'O': 'U', 'U': 'J', 'M': 'W', 'W': 'L', 'L': 'M','K': 'P', 'P': 'V', 'V': 'K'}
r1map = {'5': '2','6': '5', '2': '6', 'T': 'C', 'G': 'T', 'C': 'G', 'O': 'J', 'U': 'O', 'J': 'U', 'W': 'M', 'L': 'W', 'M': 'L', 'P': 'K', 'V': 'P', 'K': 'V'}
Rmap = {'2': '1','1': '5', '5': '2', 'B': 'P', 'P': 'I','I': 'B', 'N': 'K', 'K': 'D', 'D': 'N', 'Q': 'V', 'V': 'F', 'F': 'Q', 'J': 'C', 'C': 'M', 'M': 'J'}
R1map = {'1': '2','5': '1', '2': '5', 'P': 'B', 'I': 'P','B': 'I', 'K': 'N', 'D': 'K', 'N': 'D', 'V': 'Q', 'F': 'V', 'Q': 'F', 'C': 'J', 'M': 'C', 'J': 'M'}
bmap = {'5': '4','4': '6', '6': '5', 'B': 'H', 'H': 'K', 'K': 'B', 'N': 'S', 'S': 'V', 'V': 'N', 'Q': 'X', 'X': 'P', 'P': 'Q', 'O': 'T', 'T': 'W', 'W': 'O'}
b1map = {'4': '5','6': '4', '5': '6', 'H': 'B', 'K': 'H', 'B': 'K', 'S': 'N', 'V': 'S', 'N': 'V', 'X': 'Q', 'P': 'X', 'Q': 'P', 'T': 'O', 'W': 'T', 'O': 'W'}
Bmap = {'1': '4', '4': '5', '5': '1', 'C': 'R', 'R': 'O', 'O': 'C', 'J': 'E', 'E': 'W', 'W': 'J', 'M': 'A', 'A': 'T', 'T': 'M','B': 'Q', 'Q': 'N', 'N': 'B'}
B1map = {'4': '1', '5': '4', '1': '5', 'R': 'C', 'O': 'R', 'C': 'O', 'E': 'J', 'W': 'E', 'J': 'W', 'A': 'M', 'T': 'A', 'M': 'T','Q': 'B', 'N': 'Q', 'B': 'N'}
z2map = {'A': 'U', 'U': 'A', 'B': 'V', 'V': 'B', 'C': 'W', 'W': 'C', 'D': 'X', 'X': 'D', 'E': 'G', 'G': 'E', 'F': 'H', 'H': 'F', 'M': 'O', 'O': 'M', 'N': 'P', 'P': 'N', 'I': 'S', 'S': 'I', 'J': 'T', 'T': 'J', 'K': 'Q', 'Q': 'K', 'L': 'R', 'R': 'L', '1': '6', '6': '1', '2': '4', '4': '2'}
# These dictionaries show the mapping of characters for each move, and how they uniquely affect the state tag representing the skewb. These were found by hand based on the state tag.


def r(s):
    return ''.join(rmap.get(c, c) for c in s)
def r1(s):
    return ''.join(r1map.get(c, c) for c in s)
def R(s):
    return ''.join(Rmap.get(c, c) for c in s)
def R1(s):
    return ''.join(R1map.get(c, c) for c in s)
def b(s):
    return ''.join(bmap.get(c, c) for c in s)
def b1(s):
    return ''.join(b1map.get(c, c) for c in s)
def B(s):
    return ''.join(Bmap.get(c, c) for c in s)
def B1(s):
    return ''.join(B1map.get(c, c) for c in s)
def z2(s):
    return ''.join(z2map.get(c, c) for c in s)
# These functions define the moves of the skewb, using the dictionaries to create functions that actually can change a string in the ways outlined.

def reverse_moves(moves):
    reversed_moves = []
    for move in reversed(moves.split()):
        if move.endswith("'"):
            reversed_moves.append(move[:-1])
        else:
            reversed_moves.append(move + "'")

    return " ".join(reversed_moves)
# This function takes a string of moves and applies them backwards, switching every move that's a prime move to clockwise, and vice versa. This has the inverse effect on the cube state of the original moves inputted.


MOVES = {
    'r': r, "r'": r1,
    'R': R, "R'": R1,
    'b': b, "b'": b1,
    'B': B, "B'": B1,
    'z2': z2
}
# This dictionary maps the move names as they'd be shown in a move input to the functions used for them, so that you can input a string of moves and it will do them to the cube state.


def apply_moves(tempstate, moves):
    for move in moves.split():
        tempstate = MOVES[move](tempstate)
    return tempstate
# This uses the MOVES dictionary to take an input of moves and the starting state, to output the new state.


if __name__ == "__main__":
    state = "ABCDUV124"
    print(state)
    while True:
        entry = input()
        if entry == "quit":
            break
        if entry == "reset":
            state = "ABCDUV124"
            entry = ""
        state = apply_moves(state, entry)
        print(state)
        #state_2 = z2(state)
        #print(state_2)
        # These were to test the z2 function, not needed now. 
# This function allows us to play with the skewb in the terminal by inputting moves and getting an output state.

# With these functions defined, we can now use the apply_moves function in all files from here on, to successfully simulate and manipulate a virtual skewb.