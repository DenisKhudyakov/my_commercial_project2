from data.config import LIMIT_FENCE_CARD, STATION_REPORT
import pandas as pd
from pathlib import Path


def read_files(path: Path) -> dict:
    """Функция-генератор чтения таблицы"""
    materials_data = pd.read_excel(path).fillna(0)
    for i in materials_data.iterrows():
        yield i[1].to_dict()




if __name__ == '__main__':
    # print(list(read_files(STATION_REPORT)))
    for i in read_files(STATION_REPORT):
        print(i)

