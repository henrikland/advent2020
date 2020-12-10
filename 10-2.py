import sys

input = sorted(map(lambda line: int(line), sys.stdin.read().split("\n")))

adapters = [
    0,
    *input,
    input[-1] + 3
]

cache_paths = [None for i in range(len(adapters))]


def pathsForIndex(path_index):
    if cache_paths[path_index] is not None:
        # We have already checked this item
        return cache_paths[path_index]

    if path_index == len(adapters) - 2:
        # We are at the second last item, there is only 1 possible path to the end
        return 1

    paths_for_adapter = sum(
        map(
            lambda a: pathsForIndex(a),
            filter(
                lambda a: adapters[a] - adapters[path_index] < 4,
                range(path_index + 1, min(path_index + 4, len(adapters)))
            )
        )
    )

    cache_paths[path_index] = paths_for_adapter
    return paths_for_adapter


print(pathsForIndex(0))
