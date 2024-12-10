from puzzle_1 import get_lists
from collections import Counter

"""
Used the input from puzzle_1 to get the input. Each list (left, right) is counted and stored in a list of Counters.
Iterated through the left input, checking for matches in the right input.
When a match is found, we add the similarity score to our total counter.
Note: You can recognize from the problem that each time we find a match from left to right, we add the product of the
numer and the right list. We do this as many times as it is in the left list. Hence, we can just do this once by 
counting the left list and multiplying by it.
"""


def count_list(lists):
    return [Counter(lists[0]), Counter(lists[1])]

def get_sim_score(counter: list[Counter], shared_vals: set[int]) -> int:
    return sum(num*counter[0][num]*counter[1][num] for num in shared_vals)

def get_shared_vals(lists: list[list[int]]) -> set[int]:
    return set(lists[0]) & set(lists[1])

def main():
    lists = get_lists()
    print(get_sim_score(count_list(lists), get_shared_vals(lists)))

if __name__ == "__main__":
    main()
