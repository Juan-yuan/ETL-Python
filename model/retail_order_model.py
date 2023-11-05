'''
    Retail Order Model
    * A data model solely related to orders (1-to-1 class model)
    * Data models related to orders and products (1-to-many class model)
'''


import json
from util import time_util, str_util
from config import project_config as conf

class OrdersModel:
    def __init__(self, data: str):
        data_dict = json.loads(data)  # dictionary = json.loads（string）

        self.discount_rate = data_dict['discountRate']
        self.store_shop_no = data_dict['storeShopNo']
        self.day_order_seq = data_dict['dayOrderSeq']
        self.store_district = data_dict['storeDistrict']
        self.is_signed = data_dict['isSigned']
        self.store_province = data_dict['storeProvince']
        self.origin = data_dict['origin']
        self.store_gps_longitude = data_dict['storeGPSLongitude']
        self.discount = data_dict['discount']
        self.store_id = data_dict['storeID']
        self.product_count = data_dict['productCount']
        self.operator_name = data_dict['operatorName']
        self.operator = data_dict['operator']
        self.store_status = data_dict['storeStatus']
        self.store_own_user_tel = data_dict['storeOwnUserTel']
        self.pay_type = data_dict['payType']
        self.discount_type = data_dict['discountType']
        self.store_name = data_dict['storeName']
        self.store_own_user_name = data_dict['storeOwnUserName']
        self.date_ts = data_dict['dateTS']
        self.small_change = data_dict['smallChange']
        self.store_gps_name = data_dict['storeGPSName']
        self.erase = data_dict['erase']
        self.store_gps_address = data_dict['storeGPSAddress']
        self.order_id = data_dict['orderID']
        self.money_before_whole_discount = data_dict['moneyBeforeWholeDiscount']
        self.store_category = data_dict['storeCategory']
        self.receivable = data_dict['receivable']
        self.face_id = data_dict['faceID']
        self.store_own_user_id = data_dict['storeOwnUserId']
        self.payment_channel = data_dict['paymentChannel']
        self.payment_scenarios = data_dict['paymentScenarios']
        self.store_address = data_dict['storeAddress']
        self.total_no_discount = data_dict['totalNoDiscount']
        self.payed_total = data_dict['payedTotal']
        self.store_gps_latitude = data_dict['storeGPSLatitude']
        self.store_create_date_ts = data_dict['storeCreateDateTS']
        self.store_city = data_dict['storeCity']
        self.member_id = data_dict['memberID']

    def check_and_transform_area(self):
        if str_util.check_null(self.store_province):
            self.store_province = "missing province value"
        if str_util.check_null(self.store_city):
            self.store_city = "missing city value"
        if str_util.check_null(self.store_district):
            self.store_district = "missing sub value"

    def to_csv(self, sep=","):
        self.check_and_transform_area()

        csv_line = \
            f"{self.order_id}{sep}" \
            f"{self.store_id}{sep}" \
            f"{self.store_name}{sep}" \
            f"{self.store_status}{sep}" \
            f"{self.store_own_user_id}{sep}" \
            f"{self.store_own_user_name}{sep}" \
            f"{self.store_own_user_tel}{sep}" \
            f"{self.store_category}{sep}" \
            f"{self.store_address}{sep}" \
            f"{self.store_shop_no}{sep}" \
            f"{self.store_province}{sep}" \
            f"{self.store_city}{sep}" \
            f"{self.store_district}{sep}" \
            f"{self.store_gps_name}{sep}" \
            f"{self.store_gps_address}{sep}" \
            f"{self.store_gps_longitude}{sep}" \
            f"{self.store_gps_latitude}{sep}" \
            f"{self.is_signed}{sep}" \
            f"{self.operator}{sep}" \
            f"{self.operator_name}{sep}" \
            f"{self.face_id}{sep}" \
            f"{self.member_id}{sep}" \
            f"{time_util.ts13_to_date_str(self.store_create_date_ts)}{sep}" \
            f"{self.origin}{sep}" \
            f"{self.day_order_seq}{sep}" \
            f"{self.discount_rate}{sep}" \
            f"{self.discount_type}{sep}" \
            f"{self.discount}{sep}" \
            f"{self.money_before_whole_discount}{sep}" \
            f"{self.receivable}{sep}" \
            f"{self.erase}{sep}" \
            f"{self.small_change}{sep}" \
            f"{self.total_no_discount}{sep}" \
            f"{self.payed_total}{sep}" \
            f"{self.pay_type}{sep}" \
            f"{self.payment_channel}{sep}" \
            f"{self.payment_scenarios}{sep}" \
            f"{self.product_count}{sep}" \
            f"{time_util.ts13_to_date_str(self.date_ts)}"
        return csv_line

    def generate_insert_sql(self):
        sql = f"INSERT IGNORE INTO {conf.target_orders_table_name} (" \
              f"order_id, store_id, store_name, store_status, store_own_user_id," \
              f"store_own_user_name, store_own_user_tel, store_category," \
              f"store_address, store_shop_no, store_province, store_city," \
              f"store_district, store_gps_name, store_gps_address," \
              f"store_gps_longitude, store_gps_latitude, is_signed," \
              f"operator, operator_name, face_id, member_id, store_create_date_ts," \
              f"origin, day_order_seq, discount_rate, discount_type, discount," \
              f"money_before_whole_discount, receivable, erase, small_change," \
              f"total_no_discount, pay_total, pay_type, payment_channel," \
              f"payment_scenarios, product_count, date_ts" \
              f") VALUES (" \
              f"'{self.order_id}', " \
              f"{self.store_id}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_name)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_status)}, " \
              f"{self.store_own_user_id}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_own_user_name)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_own_user_tel)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_category)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_address)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_shop_no)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_province)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_city)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_district)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_name)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_address)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_longitude)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.store_gps_latitude)}, " \
              f"{self.is_signed}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.operator)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.operator_name)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.face_id)}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.member_id)}, " \
              f"'{time_util.ts13_to_date_str(self.store_create_date_ts)}', " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.origin)}, " \
              f"{self.day_order_seq}, " \
              f"{self.discount_rate}, " \
              f"{self.discount_type}, " \
              f"{self.discount}, " \
              f"{self.money_before_whole_discount}, " \
              f"{self.receivable}, " \
              f"{self.erase}, " \
              f"{self.small_change}, " \
              f"{self.total_no_discount}, " \
              f"{self.payed_total}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.pay_type)}, " \
              f"{self.payment_channel}, " \
              f"{str_util.check_str_null_and_transform_to_sql_null(self.payment_scenarios)}, " \
              f"{self.product_count}, " \
              f"'{time_util.ts13_to_date_str(self.date_ts)}')"
        return sql
