from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(Not(AKnight),And(AKnight,AKnave)),
    Or(Not(AKnave),Not(And(AKnight,AKnave))),
    Or(And(Not(AKnave),AKnight),And(Not(AKnight),AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(Not(AKnight),And(AKnave,BKnave)),
    Or(Not(AKnave),Not(And(AKnave,BKnave))),
    Or(And(Not(AKnave),AKnight),And(Not(AKnight),AKnave)),
    Or(And(Not(BKnave),BKnight),And(Not(BKnight),BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(Not(AKnight),Or(And(AKnave,BKnave),And(AKnight,BKnight))),
    Or(Not(AKnave),Not(Or(And(AKnave,BKnave),And(AKnight,BKnight)))),
    Or(Not(BKnight),Or(And(Not(AKnave),BKnave),And(Not(AKnight),BKnight))),
    Or(Not(BKnave),Not(Or(And(Not(AKnave),BKnave),And(Not(AKnight),BKnight)))),
    Or(And(Not(AKnave),AKnight),And(Not(AKnight),AKnave)),
    Or(And(Not(BKnave),BKnight),And(Not(BKnight),BKnave))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(Not(AKnight),Or(AKnight,AKnave)),
    Or(Not(AKnave),Not(Or(AKnight,AKnave))),
    Not(BKnight),
    Or(Not(BKnight),CKnave),
    Or(Not(BKnave),Not(CKnave)),
    Or(And(Not(AKnave),AKnight),And(Not(AKnight),AKnave)),
    Or(And(Not(BKnave),BKnight),And(Not(BKnight),BKnave)),
    Or(And(Not(CKnave),CKnight),And(Not(CKnight),CKnave))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
