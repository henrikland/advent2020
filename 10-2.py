import sys

input = sorted(map(lambda line: int(line), sys.stdin.read().split("\n")))

adapters = [
    0,
    *input,
    input[-1] + 3
]

cache_paths = [None for _ in range(len(adapters))]


def pathsForIndex(adapter_index):
    if cache_paths[adapter_index] is not None:
        # We have already checked this item
        return cache_paths[adapter_index]

    if adapter_index == len(adapters) - 2:
        # We are at the second last item, there is only 1 possible path to the end
        return 1

    paths_for_adapter = sum(
        map(
            lambda a: pathsForIndex(a),
            filter(
                lambda a: adapters[a] - adapters[adapter_index] < 4,
                range(adapter_index + 1, min(adapter_index + 4, len(adapters)))
            )
        )
    )

    cache_paths[adapter_index] = paths_for_adapter
    return paths_for_adapter


print(pathsForIndex(0))
