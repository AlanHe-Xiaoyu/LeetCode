# Chess Valid Move

## Prompt

Note: This question requires that the candidate be somewhat familiar with the
game of chess.

- Given a chess board, a starting position, and an ending position, write a
  function `isValidMove` that will return true or false. The function signature
  will be: `isValidMove(board, start, end, color)`.
- Lettered values indicate pieces. Uppercase is one color, lower case is the
  other.
- Values with `.` are empty spaces.
- Some special chess-rules to consider:
  - Pawns can move two spaces on their first turn.
  - When the King is in check, certain rules apply to pieces around him:
    - They are "pinned" if their move would put the king in danger.
    - The move is only valid if it blocks the check or kills the threatening
      pieces.

### Extra credit rules

- Promotion of a pawn upon reaching the end of the board.
- Castling.
- En passant.

## Moves

### Pawns (P)

- Can move directly forward two spaces on their first turn, one after that.
- Can move diagonally forward only when capturing an opponent's piece.

### Rook (R)

- Can move straight in any direction, forward, backward, side to side, as long
  as it's not obstructed by any other piece.

### Knight/Horse (H)

- This piece moves in an uppercase "L" shape:
- Forward, backward, left or right two squares, and must then move one square in
  either perpendicular direction.
- The knight can skip over any other pieces to reach its destination.

### Bishop (B)

- Can move in any diagonal direction so long as its not obstructed by another
  piece.
- Cannot move past any piece that is obstructing its path, but may capture any
  piece within its bounds of movement.

### Queen (Q)

- Can move in any direction on a straight or diagonal path.
- Cannot "jump" over any other piece on the board.

### King (K)

- Can move one single square in any direction.
- Cannot move onto a square occupied by a piece from its own team.
- Cannot move to any square that puts them in "check", aka "immediate danger
  from the opposing team".

## Rubric (Coding)

#### Characteristics of Unfamiliar

- Can consider movement of a single piece
- Rudimentary handling of turns
- Messy code
- Lots of manual array math
- Needlessly complex modeling (tons of classes)

#### Characteristics of Familiar

- Can consider movements of multiple pieces
- Handles turns
- Tests
- Messy code
- Lots of manual array math
- Needlessly complex modeling (tons of classes)
- Doesn't factor similarities between pieces into shared logic

#### Characteristics of Proficient

- Handles check, first turn pawns, and/or movement for all pieces
- Clean code
- Simple modeling
- Factors similarities between pieces into shared logic
- Tests

#### Characteristics of Master

- Handles check
- Handles first turn pawns
- Handles movement for all pieces
- Clean code
- Simple modeling
- Factors similarities between pieces into shared logic
- Tests
- Handles extra credit rules
