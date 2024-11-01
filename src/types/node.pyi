from datetime import datetime
from typing import Optional

class Node:
    name: str
    parent: Optional["Node"]
    created_at: datetime
    updated_at: datetime

    def __init__(
        self,
        name: str,
        parent: Optional["Node"] = None,
        created_at: Optional[datetime] = None,
    ) -> None: ...
    def rename(self, new_name: str) -> None: ...
    def get_path(self) -> str: ...
