
<img src="img/0 Majority Elements Pie Chart.png">

## Problem: Find Majority Element in a List of Strings

- Given a list of strings, your task is to find the majority element. The majority element is defined as the string that appears more than half of the time in the given list. If there is no majority element, return None.

###  Function Signature:

```python
def find_majority(strings: List[str]) -> Optional[str]:
    """
    Finds the majority element in a list of strings.

    Parameters:
    - strings (List[str]): A list of strings.

    Returns:
    - Optional[str]: The majority element if it exists, otherwise None.
    """

```
### Examples:

1. String
```py
strings_list = ["apple", "banana", "apple", "orange", "apple"]
result = find_majority(strings_list)
# Output: "apple"

strings_list = ["apple", "banana", "orange", "grape"]
result = find_majority(strings_list)
# Output: None

```
2. Integer

```py
numbers_list = [1, 2, 2, 2, 3, 2, 4, 2, 2]
result = find_majority(numbers_list)
# Output: 2

numbers_list = [1, 2, 3, 4, 5]
result = find_majority(numbers_list)
# Output: None

```
The function should return the majority element if it exists; otherwise, it should return None.


## Visualization:

<img src="img/1 Majority Elements Pie Chart avg express.png">
<img src="img/2 Majority Elements Pie Chart min express.png">
<img src="img/3 Majority Elements Pie Chart mid express.png">
<img src="img/4 Majority Elements Pie Chart max express.png">

