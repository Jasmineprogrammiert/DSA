# Problem 39.5 - Thesaurusly
# Given a sentence and a synonyms map (word -> list of synonyms), return all
# possible sentences by replacing words with their synonyms. Words without
# synonyms stay unchanged.
#
# Example:
# sentence = "one does not simply walk into mordor"
# synonyms = {"walk": ["stroll","hike","wander"], "simply": ["just","merely"]}
# Output: 6 sentences with all combinations of synonyms
#
# Example 2: sentence = "walk", synonyms = {"walk": ["stroll"]} -> ["stroll"]
#
# Constraints:
# - sentence length <= 500, at most 100 words
# - synonyms map at most 8 entries, each list at most 6
# - Each word at most 10 characters