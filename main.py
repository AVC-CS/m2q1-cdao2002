def getPivot(number):
    n = len(number)
    if n == 0:
        raise ValueError("number must not be empty")
    
    avg = sum(number) / n
    pivot_idx = 0
    best_dist = abs(number[0] - avg)
    

def split(number):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():
    # number = list(map(int, input().split()))
    number = [65, 15, 10, 20, 40, 55]
    number = split(number)
    print(number)


if __name__ == '__main__':
    main()
