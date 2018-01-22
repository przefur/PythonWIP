with open('Task6_input.txt', 'r') as f:
    data = f.read()


def redistribution(input_string):
    s = input_string.split('\t')
    results = list(map(int, s))
    current = tuple(results)
    seen = set()
    while current not in seen:
        index = results.index(max(results))
        iterator = results[index]
        results[index] = 0
        for i in range(0, iterator):
            results[(index + i + 1) % len(results)] += 1
        seen.add(current)
        current = tuple(results)
    return len(seen)


def redistribution2(input_string):
    s = input_string.split('\t')
    results = list(map(int, s))
    current = tuple(results)
    seen = set()
    while current not in seen:
        index = results.index(max(results))
        iterator = results[index]
        results[index] = 0
        for i in range(0, iterator):
            results[(index + i + 1) % len(results)] += 1
        seen.add(current)
        current = tuple(results)
    seen.clear()
    while current not in seen:
        index = results.index(max(results))
        iterator = results[index]
        results[index] = 0
        for i in range(0, iterator):
            results[(index + i + 1) % len(results)] += 1
        seen.add(current)
        current = tuple(results)
    return len(seen)


print(redistribution(data))
print(redistribution2(data))
