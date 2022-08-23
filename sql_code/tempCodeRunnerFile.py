parser = argparse.ArgumentParser()
parser.add_argument("table_name", help="テーブル名")
parser.add_argument("csv_path", help="読み込むCSVファイルのパス")
args = parser.parse_args()