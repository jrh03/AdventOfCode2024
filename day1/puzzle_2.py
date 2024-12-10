from puzzle_1 import get_lists
from collections import Counter

"""
Used the input from puzzle_1 to get the input. Each list (left, right) is counted and stored in a list of Counters.
Iterated through the left input, checking for matches in the right input.
When a match is found, we add the similarity score to our total counter.
Would like to see if there is a more efficient way to do this.
"""


def count_list():
    lists = get_lists()
    return [Counter(lists[0]), Counter(lists[1])]

def get_sim_score(counter: list[Counter]) -> int:
    num = 0

    for key, value in counter[0].items():
        if counter[1].get(key):
            num += key * value * counter[1][key]

    return num

def main():
    print(get_sim_score(count_list()))

if __name__ == "__main__":
    main()
