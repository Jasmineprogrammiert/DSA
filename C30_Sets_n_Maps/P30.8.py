# ***** The map is keyed by desks (better) *****
# 1. Build Map<desk, index> using enumerate(), skip students with correct answers
# 2. For each student, check desk+1 neighbor:
#       - Existence in map + on the same row ((desk-1) // m) -> compare answers
#       - Identical answers => add [id, id] to res = []
# 3. Return res [[id, id]]

# n: number of students
# k: number of questions
# T: O(n * k) - both loops iterate n times, each with an O(k) answer comparison
# S: O(n) - desk_to_index map stores up to n entries

def cheater_detection(solution, m, students):
    res = []
    desk_to_index = {}
    
    for i, [id, desk, answers] in enumerate(students):
        if answers != solution:
            desk_to_index[desk] = i
       
    def same_row(desk1, desk2):
        # converting 1-based desks to 0-based groups
        return (desk1 - 1) // m == (desk2 - 1) // m 
    
    for id, desk, answers in students:
        r_desk = desk + 1
        if r_desk in desk_to_index and same_row(desk, r_desk):
            r_student = students[desk_to_index[r_desk]]
            if r_student[2] == answers: # compare the answers of both students
                res.append([id, r_student[0]])
    return res

# ***** The map is keyed by answers *****
# 1. Group students by answers -> Map<tuple(answers), [(id, desk)]>
# 2. Remove correct-answer key -> del map[tuple(answers)]
# 3. For each group, find adjacent pairs -> same row: math.ceil() + desk diff +- 1
# 4. Return student IDs -> [[id, id]]

# import math

# def cheater_detection(answer, m, students):
#     groups = {}
#     res = []
    
#     for id, desk, answers in students:
#         student_ans = tuple(answers)
        
#         if student_ans not in groups:
#             groups[student_ans] = []
#         groups[student_ans].append((id, desk))
        
#     if tuple(answer) in groups:
#         del groups[tuple(answer)]
    
#     for group in groups.values():
#         for i in range(len(group)):
#             for j in range(i + 1, len(group)):
#                 id1, desk1 = group[i]
#                 id2, desk2 = group[j]
#                 row1 = math.ceil(desk1 / m)
#                 row2 = math.ceil(desk2 / m)
#                 if row1 == row2 and abs(desk1 - desk2) == 1:
#                     res.append([id1, id2])
#     return res
    
# print(cheater_detection(
#     ['a', 'b', 'c', 'c'], 
#     5, 
#     [# student ID, desk, answers
#         (4, 10, ['a', 'b', 'c', 'd']),
#         (1, 6,  ['a', 'b', 'c', 'd']),
#         (3, 8,  ['a', 'b', 'd', 'd']),
#         (5, 11, ['a', 'b', 'c', 'd']),
#         (9, 7,  ['a', 'b', 'c', 'd']),
#         (6, 16, ['a', 'b', 'd', 'd'])
#     ]
# ))



# # Cheater Detection

# You are given an array, `answers`, with the answers of a multi-choice test. The list has `k` characters (`'a'`, `'b'`, `'c'`, or `'d'`), where `k` is the number of questions in the exam.

# You are also given an array, `students`, of students' answers for the test. Each entry is a tuple `[student_id, desk, answers]`, where:

# - Student IDs are unique positive integers.
# - Desks are unique positive integers. Desks are arranged in rows of `m` desks, starting with desks `1` to `m` in the first row, `m+1` to `2m` in the second row, and so on. Not all desks may be occupied. E.g., there may be a student at desk `2` but none at desk `1`.
# - For each student, `answers` is an array of `k` characters (`'a'`, `'b'`, `'c'`, or `'d'`).

# Two students are considered _suspect_ if they have made **identical mistakes** and **sit next to each other** in the same row (we don't care about students in the front or behind one another).

# Return a list of all pairs of suspect students in any order (the order of the two students in a pair also doesn't matter).

# Example 1: answers = ['a', 'b', 'c', 'c'], m = 5, students = [
#     # student ID, desk, answers
#     (4, 10, ['a', 'b', 'c', 'd']),
#     (1, 6,  ['a', 'b', 'c', 'd']),
#     (3, 8,  ['a', 'b', 'd', 'd']),
#     (5, 11, ['a', 'b', 'c', 'd']),
#     (9, 7,  ['a', 'b', 'c', 'd']),
#     (6, 16, ['a', 'b', 'd', 'd'])
# ]
# Output: [[1, 9]]. Students 1 and 9 made the same mistakes and sit next to each other.

# Example 2: answers = ['a', 'b'], m = 2, students = [
#     (1, 1, ['a', 'b']),
#     (2, 2, ['a', 'b'])
# ]
# Output: []. Perfect scores are not suspicious.

# Example 3: answers = ['a', 'b'], m = 2, students = [
#     (1, 1, ['b', 'b']),
#     (2, 2, ['b', 'b'])
# ]
# Output: [[1, 2]]. Both students made the same mistake and sit next to each other.

# Constraints:

# - The length of `answers` is at most `10^5`
# - The length of `students` is at most `10^5`
# - All `answers` are 'a', 'b', 'c', or 'd'
# - All student IDs are unique positive integers
# - All desks are unique positive integers
# - `m` is a positive integer less than `10^5`