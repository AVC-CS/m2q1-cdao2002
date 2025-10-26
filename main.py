def getPivot(number):
    n = len(number)
    if n == 0:
        raise ValueError("number must not be empty")
    
    avg = sum(number) / n
    pivot_idx = 0
    best_dist = abs(number[0] - avg)
    
    for i, x in enumerate(number):
        d = abs(x - avg)
        if d < best_dist or (d == best_dist and i > pivot_idx):
            pivot_idx = i
    return pivot_idx

def split(number):

    idx = getPivot(number)
    pivot = number[idx]

    left  = [x for i, x in enumerate(number) if i != idx and x <= pivot]
    right = [x for i, x in enumerate(number) if i != idx and x > pivot]

    return left + [pivot] + right


def main():
    # number = list(map(int, input().split()))
    number = [65, 15, 10, 20, 40, 55]
    number = split(number)
    print(number)


if __name__ == '__main__':
    main()
