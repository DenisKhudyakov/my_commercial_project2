from data.config import STATION_REPORT, OUTPUT_FILE
from src.read_exel_files import read_files
from typing import Generator
import pandas as pd


def filter_reports(reports_station: Generator) -> list:
    """Функция, которая формирует список ТМЦ без признака min-max"""
    return list(filter(lambda x: x['Unnamed: 5'] != 'Да', reports_station))


def materials_for_purchase(list_with_materials: list) -> list:
    """метод, который выводит товары к заказу"""
    for material in list_with_materials:
        try:
            if material['Unnamed: 6'] - material['Unnamed: 9'] > 0:
                yield material
        except TypeError:
            continue
        except ValueError:
            continue


def gen_new_df(data_list: Generator) -> pd.DataFrame:
    """Функция генерации датаФрейма"""
    df1 = pd.DataFrame(filter_reports(read_files(STATION_REPORT))[:1])
    df2 = pd.DataFrame(list(data_list))
    result = pd.concat([df1, df2]).replace(0, None)
    return result

def write_exel(df: pd.DataFrame) -> None:
    """Функиця, которая записывает датафрейм в файл"""
    with pd.ExcelWriter(OUTPUT_FILE) as writer:
        df.to_excel(writer, index=False, header=False)


if __name__ == '__main__':
    pass
    # print(filter_reports(read_files(STATION_REPORT))[:1])
    # print(list(materials_for_purchase(filter_reports(read_files(STATION_REPORT)))))
    # print(gen_new_df(materials_for_purchase(filter_reports(read_files(STATION_REPORT)))))
    # write_exel(gen_new_df(materials_for_purchase(filter_reports(read_files(STATION_REPORT)))))
