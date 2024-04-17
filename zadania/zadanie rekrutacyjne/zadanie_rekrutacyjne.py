import statistics
from datetime import datetime
from typing import Union


def first_sunday(date: str) -> int:
    day = datetime.strptime(f"{date}-01", "%Y-%m-%d")
    iso_day = day.isoweekday()
    return 8 - iso_day


def solution(data: dict) -> Union[None, int]:
    cash = []
    for date, days in data.items():
        for day, exp in days.items():
            if int(day) <= first_sunday(date):
                for prices in exp.values():
                    for price in prices:
                        if isinstance(price, (int, float)):
                            cash.append(price)
    if cash:
        return statistics.median(cash)

    return None
