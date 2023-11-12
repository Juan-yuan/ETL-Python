from util import str_util
from config import project_config as conf

class BarcodeModel():
    def __init__(self, code, name, spec, trademark,
                 addr, units, factory_name, trade_price,
                 retail_price, update_at, wholeunit,
                 wholenum, img, src):
        self.code = code
        self.name = str_util.clean_str(name)
        self.spec = str_util.clean_str(spec)
        self.trademark = str_util.clean_str(trademark)
        self.addr = str_util.clean_str(addr)
        self.units = str_util.clean_str(units)
        self.factory_name = str_util.clean_str(factory_name)
        self.trade_price = trade_price
        self.retail_price = retail_price
        self.update_at = update_at
        self.wholeunit = str_util.clean_str(wholeunit)
        self.wholenum = wholenum
        self.img = img
        self.src = src

    def generate_insert_sql(self):
        # Use `REPLACE INTO`， force replace the data which only processed half from last insert query
        sql = f"REPLACE INTO {conf.target_barcode_table_name} (" \
              f"code, name, spec, trademark, addr, units, factory_name, trade_price, retail_price," \
              f"update_at, wholeunit, wholenum, img, src) VALUES(" \
              f"'{self.code}', " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.name)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.spec)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.trademark)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.addr)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.units)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.factory_name)}, " \
              f"{str_util.check_number_null_and_transform_to_sql_null(self.trade_price)}, " \
              f"{str_util.check_number_null_and_transform_to_sql_null(self.retail_price)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.update_at)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.wholeunit)}, " \
              f"{str_util.check_number_null_and_transform_to_sql_null(self.wholenum)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.img)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.src)})"
        return sql