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


class OrderDetailModel:
    def __init__(self, data):
        data_dict = json.loads(data)
        self.order_id = data_dict['orderID']
        self.products_detail = []
        order_products_list = data_dict["product"]

        # if len(order_products_list) > 0:
        for single_product in order_products_list:
            self.products_detail.append(SingleProductSoldModel(self.order_id, single_product))

    def generate_insert_sql(self):
        sql = f"INSERT IGNORE INTO {conf.target_orders_detail_table_name}(" \
              f"order_id, barcode, name, count, price_per, retail_price, trade_price, category_id, unit_id) VALUES"
        for model in self.products_detail:
            sql += "("
            sql += f"'{model.order_id}', " \
                   f"{model.barcode}, " \
                   f"{str_util.check_str_null_and_transform_to_sql_null(model.name)}, " \
                   f"{model.count}, " \
                   f"{model.price_per}, " \
                   f"{model.retail_price}, " \
                   f"{model.trade_price}, " \
                   f"{model.category_id}, " \
                   f"{model.unit_id}"
            sql += "), "
        sql = sql[:-2]  # There has an empty space after ',', so it's -2
        return sql

    def to_csv(self, sep=","):
        csv_line = ""
        for model in self.products_detail:
            csv_line += model.to_csv()
            csv_line += "\n"
        return csv_line


class SingleProductSoldModel:
    def __init__(self, order_id, product_dict):
        self.order_id = order_id
        self.count = product_dict["count"]
        self.name = product_dict["name"]
        self.unit_id = product_dict["unitID"]
        self.barcode = product_dict["barcode"]
        self.price_per = product_dict["pricePer"]
        self.retail_price = product_dict["retailPrice"]
        self.trade_price = product_dict["tradePrice"]
        self.category_id = product_dict["categoryID"]

    def to_csv(self, sep=","):
        csv_line = \
            f"{self.order_id}{sep}" \
            f"{self.barcode}{sep}" \
            f"{self.name}{sep}" \
            f"{self.count}{sep}" \
            f"{self.price_per}{sep}" \
            f"{self.retail_price}{sep}" \
            f"{self.trade_price}{sep}" \
            f"{self.category_id}{sep}" \
            f"{self.unit_id}"
        return csv_line

# json_str = '{"discountRate": 1,"storeShopNo": "None","dayOrderSeq": 37,"storeDistrict": "fu rong","isSigned": 0,"storeProvince": "湖南省","origin": 0,"storeGPSLongitude": "undefined","discount": 0,"storeID": 1766,"productCount": 1,"operatorName": "OperatorName","operator": "NameStr","storeStatus": "open","storeOwnUserTel": "12345678910","payType": "cash","discountType": 2,"storeName": "亿户超市郭---食品店","storeOwnUserName": "storeOwnUserName","dateTS": 1542436490000,"smallChange": 0,"storeGPSName": "None","erase": 0,"product": [{"count": 1,"name": "南京特醇","unitID": 8,"barcode": "6901028300056","pricePer": 12,"retailPrice": 12,"tradePrice": 11,"categoryID": 1},{"count": 2,"name": "特醇2","unitID": 8,"barcode": "6901028300056","pricePer": 120,"retailPrice": 120,"tradePrice": 110,"categoryID": 2}],"storeGPSAddress": "None","orderID": "154244364898517662217","moneyBeforeWholeDiscount": 12,"storeCategory": "normal","receivable": 12,"faceID": "","storeOwnUserId": 1694,"paymentChannel": 0,"paymentScenarios": "OTHER","storeAddress": "storeAddress","totalNoDiscount": 12,"payedTotal": 12,"storeGPSLatitude": "undefined","storeCreateDateTS": 1540793134000,"storeCity": "长沙市","memberID": "0"}'
# model = OrderDetailModel(json_str)
# print(model.generate_insert_sql())


# da_model = OrderDetailModel(json_str)
# for xiao_model in da_model.products_detail:
#     print(xiao_model.to_csv())

# da_model = OrderDetailModel(json_str)
# print(da_model.to_csv())
