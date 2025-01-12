import argparse


def add_numbers(x: int, y: int) -> int:
    """Add two numbers together.

    Args:a
      x (int): a number
      y (int): a number

    Returns:
      (int). The sum of the two numbers.
    """
    return x + y


def subtract_numbers(x: int, y: int) -> int:
    return x - y


def main():
    parser = argparse.ArgumentParser(
        description='compute the entry with the most occurrence and the least occurrence form a file')
    parser.add_argument('fname', metavar='N', type=str,
                        help='filename to compute the histogram')
    args = parser.parse_args()
    counter = {}
    max_key = None
    max_counter = 0
    min_key = None
    min_counter = 0

    # fill up histogram
    with open(args.fname, 'r') as f:
        for line in f:
            line = line.strip()
            if line in counter:
                counter[line] += 1
            else:
                counter[line] = 0

    # find max key
    for k, v in counter.items():
        if max_key is None or v > max_counter:
            max_key = k
            max_counter = v
        if min_key is None or v < min_counter:
            min_key = k
            min_counter = v

    print(f'Min Key = {min_key} with count = {min_counter}')
    print(f'Max Key = {max_key} with count = {max_counter}')


if __name__ == '__main__':
    main()
