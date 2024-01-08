from pathlib import Path

root_path = Path(__file__).parent
STATION_REPORT = root_path.joinpath('2141 отчет.xlsx')
LIMIT_FENCE_CARD = root_path.joinpath('2141-2143, часть 3.1, ЭОМшк,ЩСН, ЛЗК+.xlsx')
OUTPUT_FILE = root_path.joinpath('output.xlsx')