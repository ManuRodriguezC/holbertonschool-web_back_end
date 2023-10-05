#!/usr/bin/env python3
"""Filtered logger"""
from dotenv import load_dotenv
from typing import List
import mysql.connector
import logging
import os
import re

PII_FIELDS = ("name", "email", "phone", "password", "ssn")


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


def get_logger() -> logging.Logger:
    """Return a object of type logging.Logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    This method connecto to database
    """
    load_dotenv()
    db = mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD'),
        host=os.getenv('PERSONAL_DATA_DB_HOST'),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )
    return db


def main():
    """"""
    db = get_db()

    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")

    logger = get_logger()

    redac = RedactingFormatter.REDACTION
    separ = RedactingFormatter.SEPARATOR

    for row in cursor:
        date = ""
        for key, value in row.items():
            date += f"{key}={value};"
        logger.info(filter_datum(PII_FIELDS, redac, date, separ))


if __name__ == '__main__':
    main()
