import asyncio
from collections import Counter
from typing import List, Optional
import math
import random
import pandas as pd



async def find_majority_async(arr: List[int]) -> Optional[int]:
    c = Counter(arr)
    n = len(arr)
    mid = n // 2
    maj_elem, max_count = c.most_common(1)[0]

    # Add your logic here
    mask = max_count > mid
    if mask:
        return maj_elem
    else:
        return None

async def create_nums_async(size: int, diapazon: tuple[int, int]) -> List[int]:
    return [random.randint(*diapazon) for _ in range(size)]

async def print_result_async(arr: List[int]) -> Optional[int]:
    maj_elem = await find_majority_async(arr)
    return maj_elem

async def generate_and_print_results(idx: int) -> dict:
    arr = await create_nums_async(7, (1, 10))
    maj_elem = await print_result_async(arr)
    if maj_elem is not None:
        return {
            'idx': idx,
            'arr': arr,
            'maj': maj_elem}
    else:
        return

async def main():
    result = await asyncio.gather(*(generate_and_print_results(idx) for idx in range(1000)))
    return result
    
results = []
for _ in range(100):
    result = await main()
    result = list(filter(lambda row: row is not None, result))
    size = len(result)
    df = pd.DataFrame(result)
    mid_size = df.maj.value_counts().size // 2
    avg = math.ceil(df.maj.mean())
    min_maj = df['maj'].value_counts().keys()[-1]
    mid_maj = df['maj'].value_counts().keys()[mid_size]
    max_maj = df['maj'].value_counts().keys()[0]
    # or Counter
    # max_c = Counter(([n['maj'] for n in result])).most_common()[0][0] # first row with most common
    # min_c = Counter(([n['maj'] for n in result])).most_common()[-1][0] # first row with most common
    
    results.append({
        'size': size,
        'maj': {
            'avg': avg,
            'min': min_maj,
            'mid': mid_maj,
            'max': max_maj
        },
        'result': result,
    })


results




