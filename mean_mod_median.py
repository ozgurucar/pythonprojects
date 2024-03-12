def mean(data):
    return sum(data) / len(data)


def median(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return data[(n + 1) // 2 - 1]
    else:
        return data[n // 2 - 1] + data[n // 2 + 1 - 1] / 2


def mode(data):
    counts = {}
    for value in data:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    max_counts = max(counts.values())
    mode(value for value, count in counts.items() if count == max_counts)
    return mode


if __name__ == "__main__":
    data = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5]
    print(f"Mean = {mean(data)}")
    print(f"Median = {median(data)}")
    print(f"Mode = {mode(data)}")
