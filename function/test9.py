from typing import Optional, Union
scores: list[int] = [95,98,97]
user_data: dict[str, str] = {"name":"홍길동"}

def find_user(user_id: int) -> Optional[dict[str, int]]:
    if user_id > 0:
        return {"name":"치이카와","age":7}
    return None