# Reach w2 from w1: each move adds/removes one letter, ops alternate, no repeats.
#
# 1. Reachability -> BFS from w1.
# 2. Legality depends on the last op, so a node is (word, last_op), not just word.
# 3. Neighbor = one-edit add/remove: lengths differ by 1, 
# longer == shorter + one extra char (two pointers, allow <= 1 mismatch).
# 4. Move valid if op != last_op (first move: either) and (word, op) unvisited.
#
# w: number of words, L: max word length
# T: O(w^2 * L) - O(w) states, each scans all w words with an O(L) neighbor check
# S: O(w) - visited set + queue hold the (word, op) states

from collections import deque


def word_ladder_game(w1, w2, words):
    def is_neighbor(w1, w2):
        if abs(len(w1) - len(w2)) != 1:
            return False
        longer, shorter = (w1, w2) if len(w1) > len(w2) else (w2, w1)
        p1, p2, count = 0, 0, 0
        while p1 < len(longer) and p2 < len(shorter):
            if longer[p1] != shorter[p2]:
                count += 1
                if count > 1:
                    return False
            else:
                p2 += 1
            p1 += 1
        return True

    start = (w1, None)
    visited = {start}
    queue = deque([start])
    while queue:
        word, last_op = queue.popleft()
        if word == w2:
            return True
        for nbr in words:
            if is_neighbor(word, nbr):
                op = "add" if len(nbr) > len(word) else "remove"
                node = (nbr, op)
                if ((last_op is None or op != last_op) and 
                    node not in visited):
                    visited.add(node)
                    queue.append(node)
    return False


# # Word Ladder Game Variation

# Two friends are playing a game. The first one says a word. Then, the other friend has to form another word by adding or removing a letter. The first friend then needs to find a new word (repetitions are not allowed) by doing the **opposite** operation (addition or removal). The game goes on, with each friend finding a new word and alternating additions and removals.

# These are two examples of games:

# - `leap, lap, slap, sap, soap, sop, shop, hop`
# - `car, care, are, fare, far, fart, art, cart`

# However, these are not valid games:

# - `bounce, ounce, once` (we removed a letter twice in a row)
# - `hung, hug, hung` (we repeated a word)
# - `car, race` (we reordered the letters)
# - `vibes, vibess` (`vibess` is not a real word)

# Given two words (strings), `word1` and `word2`, and a list of valid words, `words`, which contains `word1` and `word2`, return whether it is possible to start the game at `word1` and get to `word2` using only words from `words`.

# Example 1:
# word1 = "leap"
# word2 = "hop"
# words = [
#    "fare", "hug", "car", "vibes", "once", "sop", "far", "ounce", "slap",
#     "sap", "cart", "hung", "art", "shop", "fart", "lap", "soap", "are",
#    "hop", "care", "leap", "bounce", "beyond", "cracking"
# ]
# Output: True
# The game can proceed as:
# leap -> lap -> slap -> sap -> soap -> sop -> shop -> hop

# Example 2:
# word1 = "car"
# word2 = "cart"
# words = [
#    "fare", "hug", "car", "vibes", "once", "sop", "far", "ounce", "slap",
#     "sap", "cart", "hung", "art", "shop", "fart", "lap", "soap", "are",
#    "hop", "care", "leap", "bounce", "beyond", "cracking"
# ]
# Output: True
# The game can proceed as:
# car -> care -> are -> fare -> far -> fart -> art -> cart

# Example 3:
# word1 = "bounce"
# word2 = "once"
# words = [
#    "fare", "hug", "car", "vibes", "once", "sop", "far", "ounce", "slap",
#     "sap", "cart", "hung", "art", "shop", "fart", "lap", "soap", "are",
#    "hop", "care", "leap", "bounce", "beyond", "cracking"
# ]
# Output: False

# Constraints:

# - All words contain only lowercase English letters
# - All the words in `words` are unique
# - `1 <= words.length <= 1000`
# - `1 <= words[i].length <= 30`
# - `word1` and `word2` are in `words`
# - `word1` and `word2` are different