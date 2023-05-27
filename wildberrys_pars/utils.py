from typing import List


def join_request(request: List[str]) -> str:

    if len(request) > 1:
        return " ".join(request)
    return request[0]
