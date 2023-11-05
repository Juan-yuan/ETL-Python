'''
    Retail Order Model
    * A data model solely related to orders (1-to-1 class model)
    * Data models related to orders and products (1-to-many class model)
'''


import json
from util import time_util, str_util

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
