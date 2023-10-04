#!/usr/bin/env python3
"""Filtered logger"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    This function contein four arguments
    fields: Is the keys of the data to hide
    redaction: The value that sream in page of replace
    message: The message ofr to modify, dates of the user
    separator: The character of separed of the message
    """
    for fiel in fields:
        pattern = f"({separator})(?:{fiel})=.*?(?={separator})"
        modify_msm = re.sub(pattern, r'\1' + f"{fiel}={redaction}", message)
        message = modify_msm
    return modify_msm
