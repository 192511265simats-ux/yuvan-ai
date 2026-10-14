"""
Day 1 - Program 4: Crypt-Arithmetic Problem (CO2)
Solves   SEND + MORE = MONEY   by trying digit permutations.
Each letter maps to a unique digit, and leading letters cannot be 0.
"""
from itertools import permutations


def solve(word1, word2, result):
    letters = sorted(set(word1 + word2 + result))
    if len(letters) > 10:
        return None

    leading = {word1[0], word2[0], result[0]}

    def to_num(word, mapping):
        return int("".join(str(mapping[ch]) for ch in word))

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if any(mapping[ch] == 0 for ch in leading):
            continue
        if to_num(word1, mapping) + to_num(word2, mapping) == to_num(result, mapping):
            return mapping
    return None


if __name__ == "__main__":
    w1, w2, res = "SEND", "MORE", "MONEY"
    print(f"Solving: {w1} + {w2} = {res}\n")

    mapping = solve(w1, w2, res)
    if mapping:
        print("Letter -> Digit mapping:")
        for ch in sorted(mapping):
            print(f"  {ch} = {mapping[ch]}")
        n1 = "".join(str(mapping[c]) for c in w1)
        n2 = "".join(str(mapping[c]) for c in w2)
        nr = "".join(str(mapping[c]) for c in res)
        print(f"\n  {n1}\n+ {n2}\n------\n {nr}")
    else:
        print("No solution found.")
