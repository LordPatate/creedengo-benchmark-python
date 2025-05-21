import pyperf
from helpers import *

from random import randint


LOOPS = 512
RAND_ARRAY_SIZE = 20
RANDOM_NUMBERS = [randint(-1024, 1024) for _ in range(RAND_ARRAY_SIZE)]


def repeat(func):
    def f():
        for i in range(LOOPS):
            _ = func(i)

    return f


@repeat
def pattern_matching(i):
    index = RANDOM_NUMBERS[i % RAND_ARRAY_SIZE]
    nb = i % 101
    match nb:
        case 0:
            nb = index
        case 1:
            nb = index
        case 2:
            nb = index
        case 3:
            nb = index
        case 4:
            nb = index
        case 5:
            nb = index
        case 6:
            nb = index
        case 7:
            nb = index
        case 8:
            nb = index
        case 9:
            nb = index
        case 10:
            nb = index
        case 11:
            nb = index
        case 12:
            nb = index
        case 13:
            nb = index
        case 14:
            nb = index
        case 15:
            nb = index
        case 16:
            nb = index
        case 17:
            nb = index
        case 18:
            nb = index
        case 19:
            nb = index
        case 20:
            nb = index
        case 21:
            nb = index
        case 22:
            nb = index
        case 23:
            nb = index
        case 24:
            nb = index
        case 25:
            nb = index
        case 26:
            nb = index
        case 27:
            nb = index
        case 28:
            nb = index
        case 29:
            nb = index
        case 30:
            nb = index
        case 31:
            nb = index
        case 32:
            nb = index
        case 33:
            nb = index
        case 34:
            nb = index
        case 35:
            nb = index
        case 36:
            nb = index
        case 37:
            nb = index
        case 38:
            nb = index
        case 39:
            nb = index
        case 40:
            nb = index
        case 41:
            nb = index
        case 42:
            nb = index
        case 43:
            nb = index
        case 44:
            nb = index
        case 45:
            nb = index
        case 46:
            nb = index
        case 47:
            nb = index
        case 48:
            nb = index
        case 49:
            nb = index
        case 50:
            nb = index
        case 51:
            nb = index
        case 52:
            nb = index
        case 53:
            nb = index
        case 54:
            nb = index
        case 55:
            nb = index
        case 56:
            nb = index
        case 57:
            nb = index
        case 58:
            nb = index
        case 59:
            nb = index
        case 60:
            nb = index
        case 61:
            nb = index
        case 62:
            nb = index
        case 63:
            nb = index
        case 64:
            nb = index
        case 65:
            nb = index
        case 66:
            nb = index
        case 67:
            nb = index
        case 68:
            nb = index
        case 69:
            nb = index
        case 70:
            nb = index
        case 71:
            nb = index
        case 72:
            nb = index
        case 73:
            nb = index
        case 74:
            nb = index
        case 75:
            nb = index
        case 76:
            nb = index
        case 77:
            nb = index
        case 78:
            nb = index
        case 79:
            nb = index
        case 80:
            nb = index
        case 81:
            nb = index
        case 82:
            nb = index
        case 83:
            nb = index
        case 84:
            nb = index
        case 85:
            nb = index
        case 86:
            nb = index
        case 87:
            nb = index
        case 88:
            nb = index
        case 89:
            nb = index
        case 90:
            nb = index
        case 91:
            nb = index
        case 92:
            nb = index
        case 93:
            nb = index
        case 94:
            nb = index
        case 95:
            nb = index
        case 96:
            nb = index
        case 97:
            nb = index
        case 98:
            nb = index
        case 99:
            nb = index
        case _:
            nb = index
    return nb


@repeat
def chained_ifs(i):
    index = RANDOM_NUMBERS[i % RAND_ARRAY_SIZE]
    nb = i % 101
    if nb == 0:
        nb = index
    elif nb == 1:
        nb = index
    elif nb == 2:
        nb = index
    elif nb == 3:
        nb = index
    elif nb == 4:
        nb = index
    elif nb == 5:
        nb = index
    elif nb == 6:
        nb = index
    elif nb == 7:
        nb = index
    elif nb == 8:
        nb = index
    elif nb == 9:
        nb = index
    elif nb == 10:
        nb = index
    elif nb == 11:
        nb = index
    elif nb == 12:
        nb = index
    elif nb == 13:
        nb = index
    elif nb == 14:
        nb = index
    elif nb == 15:
        nb = index
    elif nb == 16:
        nb = index
    elif nb == 17:
        nb = index
    elif nb == 18:
        nb = index
    elif nb == 19:
        nb = index
    elif nb == 20:
        nb = index
    elif nb == 21:
        nb = index
    elif nb == 22:
        nb = index
    elif nb == 23:
        nb = index
    elif nb == 24:
        nb = index
    elif nb == 25:
        nb = index
    elif nb == 26:
        nb = index
    elif nb == 27:
        nb = index
    elif nb == 28:
        nb = index
    elif nb == 29:
        nb = index
    elif nb == 30:
        nb = index
    elif nb == 31:
        nb = index
    elif nb == 32:
        nb = index
    elif nb == 33:
        nb = index
    elif nb == 34:
        nb = index
    elif nb == 35:
        nb = index
    elif nb == 36:
        nb = index
    elif nb == 37:
        nb = index
    elif nb == 38:
        nb = index
    elif nb == 39:
        nb = index
    elif nb == 40:
        nb = index
    elif nb == 41:
        nb = index
    elif nb == 42:
        nb = index
    elif nb == 43:
        nb = index
    elif nb == 44:
        nb = index
    elif nb == 45:
        nb = index
    elif nb == 46:
        nb = index
    elif nb == 47:
        nb = index
    elif nb == 48:
        nb = index
    elif nb == 49:
        nb = index
    elif nb == 50:
        nb = index
    elif nb == 51:
        nb = index
    elif nb == 52:
        nb = index
    elif nb == 53:
        nb = index
    elif nb == 54:
        nb = index
    elif nb == 55:
        nb = index
    elif nb == 56:
        nb = index
    elif nb == 57:
        nb = index
    elif nb == 58:
        nb = index
    elif nb == 59:
        nb = index
    elif nb == 60:
        nb = index
    elif nb == 61:
        nb = index
    elif nb == 62:
        nb = index
    elif nb == 63:
        nb = index
    elif nb == 64:
        nb = index
    elif nb == 65:
        nb = index
    elif nb == 66:
        nb = index
    elif nb == 67:
        nb = index
    elif nb == 68:
        nb = index
    elif nb == 69:
        nb = index
    elif nb == 70:
        nb = index
    elif nb == 71:
        nb = index
    elif nb == 72:
        nb = index
    elif nb == 73:
        nb = index
    elif nb == 74:
        nb = index
    elif nb == 75:
        nb = index
    elif nb == 76:
        nb = index
    elif nb == 77:
        nb = index
    elif nb == 78:
        nb = index
    elif nb == 79:
        nb = index
    elif nb == 80:
        nb = index
    elif nb == 81:
        nb = index
    elif nb == 82:
        nb = index
    elif nb == 83:
        nb = index
    elif nb == 84:
        nb = index
    elif nb == 85:
        nb = index
    elif nb == 86:
        nb = index
    elif nb == 87:
        nb = index
    elif nb == 88:
        nb = index
    elif nb == 89:
        nb = index
    elif nb == 90:
        nb = index
    elif nb == 91:
        nb = index
    elif nb == 92:
        nb = index
    elif nb == 93:
        nb = index
    elif nb == 94:
        nb = index
    elif nb == 95:
        nb = index
    elif nb == 96:
        nb = index
    elif nb == 97:
        nb = index
    elif nb == 98:
        nb = index
    elif nb == 99:
        nb = index
    else:
        nb = index
    return nb


HARDCODED_SWITCH = {     
    1: 42,
    2: 42,
    3: 42,
    4: 42,
    5: 42,
    6: 42,
    7: 42,
    8: 42,
    9: 42,
    10: 42,
    11: 42,
    12: 42,
    13: 42,
    14: 42,
    15: 42,
    16: 42,
    17: 42,
    18: 42,
    19: 42,
    20: 42,
    21: 42,
    22: 42,
    23: 42,
    24: 42,
    25: 42,
    26: 42,
    27: 42,
    28: 42,
    29: 42,
    30: 42,
    31: 42,
    32: 42,
    33: 42,
    34: 42,
    35: 42,
    36: 42,
    37: 42,
    38: 42,
    39: 42,
    40: 42,
    41: 42,
    42: 42,
    43: 42,
    44: 42,
    45: 42,
    46: 42,
    47: 42,
    48: 42,
    49: 42,
    50: 42,
    51: 42,
    52: 42,
    53: 42,
    54: 42,
    55: 42,
    56: 42,
    57: 42,
    58: 42,
    59: 42,
    60: 42,
    61: 42,
    62: 42,
    63: 42,
    64: 42,
    65: 42,
    66: 42,
    67: 42,
    68: 42,
    69: 42,
    70: 42,
    71: 42,
    72: 42,
    73: 42,
    74: 42,
    75: 42,
    76: 42,
    77: 42,
    78: 42,
    79: 42,
    80: 42,
    81: 42,
    82: 42,
    83: 42,
    84: 42,
    85: 42,
    86: 42,
    87: 42,
    88: 42,
    89: 42,
    90: 42,
    91: 42,
    92: 42,
    93: 42,
    94: 42,
    95: 42,
    96: 42,
    97: 42,
    98: 42,
    99: 42,
}


@repeat
def hardcoded_switch(i):
    index = RANDOM_NUMBERS[i % RAND_ARRAY_SIZE]
    nb = i % 101
    nb = HARDCODED_SWITCH.get(nb, index)
    return nb


@repeat
def dict_switch_at_runtime(i):
    index = RANDOM_NUMBERS[i % RAND_ARRAY_SIZE]
    nb = i % 101
    switch = {
        1: index,
        2: index,
        3: index,
        4: index,
        5: index,
        6: index,
        7: index,
        8: index,
        9: index,
        10: index,
        11: index,
        12: index,
        13: index,
        14: index,
        15: index,
        16: index,
        17: index,
        18: index,
        19: index,
        20: index,
        21: index,
        22: index,
        23: index,
        24: index,
        25: index,
        26: index,
        27: index,
        28: index,
        29: index,
        30: index,
        31: index,
        32: index,
        33: index,
        34: index,
        35: index,
        36: index,
        37: index,
        38: index,
        39: index,
        40: index,
        41: index,
        42: index,
        43: index,
        44: index,
        45: index,
        46: index,
        47: index,
        48: index,
        49: index,
        50: index,
        51: index,
        52: index,
        53: index,
        54: index,
        55: index,
        56: index,
        57: index,
        58: index,
        59: index,
        60: index,
        61: index,
        62: index,
        63: index,
        64: index,
        65: index,
        66: index,
        67: index,
        68: index,
        69: index,
        70: index,
        71: index,
        72: index,
        73: index,
        74: index,
        75: index,
        76: index,
        77: index,
        78: index,
        79: index,
        80: index,
        81: index,
        82: index,
        83: index,
        84: index,
        85: index,
        86: index,
        87: index,
        88: index,
        89: index,
        90: index,
        91: index,
        92: index,
        93: index,
        94: index,
        95: index,
        96: index,
        97: index,
        98: index,
        99: index,
    }
    nb = switch.get(nb, index)
    return nb


def main():
    runner = pyperf.Runner(processes=40)
    benchmarks = []

    for f_name, func in zip(
        (
            "pattern_matching",
            "chained_ifs",
            "hardcoded_switch",
            "dict_switch_at_runtime",
        ),
        (
            pattern_matching,
            chained_ifs,
            hardcoded_switch,
            dict_switch_at_runtime,
        ),
    ):
        res = runner.bench_func(f_name, func, inner_loops=LOOPS)
        if res:
            benchmarks.append(res)

    suite = pyperf.BenchmarkSuite(benchmarks)
    save_bench_result(suite)


if __name__ == "__main__":
    main()
