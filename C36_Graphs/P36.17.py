# Problem 36.17 - Word Ladder Game Variation
# Two friends play a word game alternating between adding and removing a letter.
# Given word1, word2, and a list of valid words, return whether you can get
# from word1 to word2 following the rules (no repeats, alternating add/remove).
#
# Example 1:
# word1 = "leap", word2 = "hop"
# words = ["fare","hug","car","vibes","once","sop","far","ounce","slap",
#          "sap","cart","hung","art","shop","fart","lap","soap","are",
#          "hop","care","leap","bounce","beyond","cracking"]
# Output: True (leap->lap->slap->sap->soap->sop->shop->hop)
#
# Example 2: word1 = "car", word2 = "cart" -> True
# Example 3: word1 = "bounce", word2 = "once" -> False
#
# Constraints:
# - All words lowercase English letters
# - All words unique
# - 1 <= words.length <= 1000
# - 1 <= words[i].length <= 30