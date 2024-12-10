def get_input() -> list:
    with open("puzzle_input.txt", "r") as file:
        return [line.strip('\n').split('  ') for line in file.readlines()]

def get_lists() -> list:
    input = get_input()
    list1 = [int(num[0]) for num in input]
    list2 = [int(num[1]) for num in input]
    list1.sort()
    list2.sort()
    return [list1, list2]

def list_difference(list1: list, list2: list) -> int:
    return sum([abs(pair[0] - pair[1]) for pair in zip(list1, list2)])

def main():
    lists = get_lists()
    print(list_difference(lists[0], lists[1]))

if __name__ == "__main__":
    main()