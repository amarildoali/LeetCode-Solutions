from typing import List


def restoreString(s: str, indices: List[int]) -> str:
    M = dict()
    for i in range(len(s)):
        M[indices[i]] = s[i]
    S = {k: v for k, v in sorted(M.items(), key=lambda item: item[0])}.values()
    return "".join(S)
