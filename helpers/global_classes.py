from dataclasses import dataclass
from typing import Optional


__all__ = ["LinkItem"]


@dataclass
class LinkItem:
    title: str
    url: str
    type: Optional[str] = None
