from math import floor
from collections import Counter

all_items = []
operations = []
tests_divisible = []
throw_if_true = []
throw_if_false = []
with open("input.txt") as f:
    while True:
        if not f.readline():
            break

        starting_items = list(map(int, f.readline()[18:-1].split(",")))  # remove "Starting items:" and map items to list
        operation = eval("lambda old: " + f.readline()[19:-1])  # remove "Operation: new = "
        test_divisible = int(f.readline()[21:-1])  # remove "Test: divisible by "
        if_true = int(f.readline()[29:-1])  # remove "If true: throw to monkey "
        if_false = int(f.readline()[30:-1])  # remove "If false: throw to monkey "
        f.readline()  # ignore empty line

        all_items.append(starting_items)
        operations.append(operation)
        tests_divisible.append(test_divisible)
        throw_if_true.append(if_true)
        throw_if_false.append(if_false)


counter = Counter()
for _ in range(20):
    for monkey_idx, monkey_items in enumerate(all_items):
        while monkey_items:
            counter[monkey_idx] += 1
            worry_level = monkey_items.pop(0)

            new_value = floor(operations[monkey_idx](worry_level) / 3)
            remainder = new_value % tests_divisible[monkey_idx]

            throw_monkey_idx = throw_if_true[monkey_idx] if remainder == 0 else throw_if_false[monkey_idx]
            all_items[throw_monkey_idx].append(new_value)


most_common = counter.most_common(2)
print(most_common[0][1] * most_common[1][1])
