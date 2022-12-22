from math import floor
from collections import Counter

all_items = []
all_items_mapped = []
operations = []
tests_divisible = []
throw_if_true = []
throw_if_false = []
next_key = 0
with open("input.txt") as f:
    while True:
        if not f.readline():
            break

        line = f.readline()[18:-1]
        monkey_items = []
        monkey_items_mapped = []
        for num in map(int, line.split(",")):
            monkey_items.append(num)
            monkey_items_mapped.append(next_key)
            next_key += 1

        operation = eval("lambda old: " + f.readline()[19:-1])  # remove "Operation: new = "
        test_divisible = int(f.readline()[21:-1])  # remove "Test: divisible by "
        if_true = int(f.readline()[29:-1])  # remove "If true: throw to monkey "
        if_false = int(f.readline()[30:-1])  # remove "If false: throw to monkey "
        f.readline()  # ignore empty line

        all_items.append(monkey_items)
        all_items_mapped.append(monkey_items_mapped)
        operations.append(operation)
        tests_divisible.append(test_divisible)
        throw_if_true.append(if_true)
        throw_if_false.append(if_false)

# map every item to a position on all clocks
clocks = [{} for _ in tests_divisible]
mapping_key = 0
for monkey_items in all_items:
    for item in monkey_items:
        for idx, divide_num in enumerate(tests_divisible):
            clocks[idx][mapping_key] = item % divide_num
        mapping_key += 1


counter = Counter()
for _ in range(10000):
    for monkey_idx, monkey_items in enumerate(all_items_mapped):
        while monkey_items:
            counter[monkey_idx] += 1
            worry_level_key = monkey_items.pop(0)

            for clock, mod in zip(clocks, tests_divisible):
                current_value = clock[worry_level_key]
                new_value = operations[monkey_idx](current_value) % mod
                clock[worry_level_key] = new_value

            remainder = clocks[monkey_idx][worry_level_key]

            throw_monkey_idx = throw_if_true[monkey_idx] if remainder == 0 else throw_if_false[monkey_idx]
            all_items_mapped[throw_monkey_idx].append(worry_level_key)


most_common = counter.most_common(2)
print(most_common[0][1] * most_common[1][1])
