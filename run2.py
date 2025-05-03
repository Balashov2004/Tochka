import sys

import collections


# Константы для символов ключей и дверей
keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]

def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]



def solve(data):
    m = len(data)
    n = len(data[0])
    starts = []
    counter = 0

    for i in range(m):
        for j in range(n):
            char = data[i][j]
            if char == "@":
                starts.append((i, j))
            elif char in keys_char:
                counter += 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = set()
    state = (tuple(starts), tuple([]))
    visited.add(state)

    queue = collections.deque()
    queue.append((starts, [], 0))

    while queue:
        positions, keys, steps = queue.popleft()

        if len(keys) == counter:
            return steps

        for i in range(4):
            x, y = positions[i]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                char = data[nx][ny]
                if char == '#':
                    continue

                if char in doors_char and char.lower() not in keys:
                    continue

                new_keys = keys.copy()
                if char in keys_char and char not in new_keys:
                    new_keys.append(char)

                new_positions = list(positions)
                new_positions[i] = (nx, ny)

                state = (tuple(new_positions), tuple(new_keys))
                if state not in visited:
                    visited.add(state)
                    queue.append((new_positions, new_keys, steps + 1))

    return -1



def main():
    data = get_input()
    result = solve(data)
    print(result)


if __name__ == '__main__':
    main()