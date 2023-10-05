#!/usr/bin/env python3
"""Filtered logger"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        This method init the class, add give one parameter
        fields, this contein the dates that you need to hide.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        This method format the loggin dates.
        """
        record.msg = filter_datum(self.fields,
                                  self.REDACTION,
                                  record.msg,
                                  self.SEPARATOR)
        return super().format(record)


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
