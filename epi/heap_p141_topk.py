from typing import List
from itertools import islice
def top_k(k: int, stream: List[str]) -> List[str]:

    for s in islice(stream, k):
        print (s)
    return stream



print(top_k(3, ["elecom", "miso", "soup", "conference"]))