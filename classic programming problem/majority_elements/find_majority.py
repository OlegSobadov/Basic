from typing import List, Optional
import random
from collections import Counter

def find_majority(arr: List[int]) -> Optional[int]:
    counter = Counter(arr)
    n = len(arr)
    majority_element, max_count = counter.most_common(1)[0]

    if max_count > n // 2:
        return majority_element
    else:
        return None

def generate_random_array(size: int, diapazon: tuple[int, int]) -> List[int]:
    lower_bound, upper_bound = diapazon
    return [random.randint(*diapazon) for _ in range(size)]

def print_array_and_majority(arr: List[int]) -> None:
    print(f"Array: {arr}")
    majority_element = find_majority(arr)
    
    if majority_element is not None:
        print(f"Majority Element: {majority_element}")
    else:
        print("No Majority Element")

def print_separator_line(length: int) -> None:
    print(length * "-")

# Run the function three times with different random arrays
for _ in range(3):
    diapazon = (1, 10)
    random_array = generate_random_array(size=3, diapazon=diapazon)
    print_array_and_majority(random_array)
    print_separator_line(len(random_array))
