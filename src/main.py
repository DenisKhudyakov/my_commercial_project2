from src.utils import filter_reports, materials_for_purchase, gen_new_df, write_exel
from src.read_exel_files import read_files
from data.config import STATION_REPORT


if __name__ == '__main__':
    write_exel(gen_new_df(materials_for_purchase(filter_reports(read_files(STATION_REPORT)))))
