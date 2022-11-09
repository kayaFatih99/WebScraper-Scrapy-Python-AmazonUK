from pyexcel.cookbook import merge_all_to_a_book
import glob

csv_file = 'baby'
xlsx_file = 'baby'

merge_all_to_a_book(glob.glob(f"output/{csv_file}.csv"), f"output/{xlsx_file}.xlsx")