# fastchess

A high-performance chess library written in C with Python bindings. Designed as a fast drop-in replacement for `python-chess` in data pipelines and machine learning workflows.

## Installation

```bash
pip install fastchess
```

Requires a C compiler and NumPy. On most systems `pip` will handle this automatically.

## Usage

```python
import fastchess

board = fastchess.Board()                  # start position
board = fastchess.Board("rnbqkbnr/...")    # from FEN

# Move generation
moves = board.legal_moves_uci()           # ['e2e4', 'd2d4', ...]

# Apply moves
board.push_uci("e2e4")
board.push_san("e5")

# Board state
print(board.fen())
print(board.turn)                         # fastchess.WHITE or fastchess.BLACK
print(board.is_check())

# Tensor for ML (18 x 8 x 8 numpy array)
tensor = board.to_tensor(canonical=True)

# Mirroring
mirrored = board.mirror()
```

## API

### `fastchess.Board(fen=None)`

| Method | Description |
|---|---|
| `copy()` | Return a copy of the board |
| `mirror()` | Return a vertically mirrored copy with swapped colors |
| `push_uci(uci)` | Apply a UCI move (e.g. `"e2e4"`) |
| `push_san(san)` | Apply a SAN move; returns the UCI string |
| `legal_moves_uci()` | List all legal moves as UCI strings |
| `piece_at(sq)` | `(piece_type, color)` at square index, or `None` |
| `is_check()` | True if the side to move is in check |
| `has_kingside_castling_rights(color)` | Castling rights query |
| `has_queenside_castling_rights(color)` | Castling rights query |
| `has_legal_en_passant()` | True if a legal en passant capture exists |
| `to_tensor(canonical=False)` | Board as `(18, 8, 8)` numpy array |
| `fen()` | Current FEN string |

### Constants

`WHITE`, `BLACK`, `PAWN`, `KNIGHT`, `BISHOP`, `ROOK`, `QUEEN`, `KING`

## License

MIT
