#!/usr/bin/env python3
"""funvtions to help with pagination
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index rage fetch
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
