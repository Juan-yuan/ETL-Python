import time

# ######### -- Configure the log output path ######### #
log_root_path = "/Users/kityua/PycharmProjects-gaoji/ETL-Python/logs/"

# ######### --Configure the log output filename ######### #
log_name = f'pyetl-{time.strftime("%Y-%m-%d %H", time.localtime(time.time()))}.log'
# print(log_name)  # 2023-07-08 14:09:43

# ######### Configure with process JSON file ######### #
json_data_root_path = "/Users/kityua/PycharmProjects-gaoji/ETL-Python/json"

# ######### -- csv configure -- ######### #
# csv and retail configure
retail_output_csv_root_path = "/Users/kityua/PycharmProjects-gaoji/ETL-Python/output/retail-csv/"
# orders，csv file name
retail_orders_output_csv_file_name = f'orders-{time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))}.csv'
# orders detail，csv file name
retail_orders_detail_output_csv_file_name = f'orders-detail-{time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))}.csv'

# ######## Configure with DB ####### #
metadata_host = "localhost"
metadata_user = "root"
metadata_password = "Shanjun@007"
metadata_port = 3306
mysql_charset = "utf8"

metadata_db_name = "metadata"
metadata_file_monitor_table_name = "file_monitor"
metadata_file_monitor_table_create_cols = """
    id INT PRIMARY KEY AUTO_INCREMENT,
    file_name VARCHAR(255) UNIQUE NOT NULL COMMENT 'Processed file names',
    process_lines INT COMMENT 'Processed lines',
    process_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Processing time'
"""

# barcode monitor table
metadata_barcode_table_name = "barcode_monitor"
metadata_barcode_table_create_cols = "id INT PRIMARY KEY AUTO_INCREMENT COMMENT 'Auto increment ID', " \
                                     "time_record TIMESTAMP NOT NULL COMMENT 'max time'," \
                                     "gather_line_count INT NULL COMMENT 'processed lines' "

# Target data
target_host = metadata_host
target_user = metadata_user
target_password = metadata_password
target_port = metadata_port
target_db_name = 'retail'

# After collecting JSON data, write it into MySQL to store tables related to orders
target_orders_table_name = 'orders'
# orders table create table SQL
target_orders_table_create_cols = \
    f"order_id VARCHAR(255) PRIMARY KEY, " \
    f"store_id INT COMMENT 'Store ID', " \
    f"store_name VARCHAR(30) COMMENT 'Store name', " \
    f"store_status VARCHAR(10) COMMENT 'Store status(open, close)', " \
    f"store_own_user_id INT COMMENT 'Owner id', " \
    f"store_own_user_name VARCHAR(50) COMMENT 'Owner name', " \
    f"store_own_user_tel VARCHAR(30) COMMENT 'Owner number', " \
    f"store_category VARCHAR(10) COMMENT 'Store category(normal, test)', " \
    f"store_address VARCHAR(255) COMMENT 'Store address', " \
    f"store_shop_no VARCHAR(255) COMMENT 'Store pay id', " \
    f"store_province VARCHAR(10) COMMENT 'Store province', " \
    f"store_city VARCHAR(10) COMMENT 'Store city', " \
    f"store_district VARCHAR(10) COMMENT 'Store district', " \
    f"store_gps_name VARCHAR(255) COMMENT 'Store gps name', " \
    f"store_gps_address VARCHAR(255) COMMENT 'Store gps address', " \
    f"store_gps_longitude VARCHAR(255) COMMENT 'Store gps longitude', " \
    f"store_gps_latitude VARCHAR(255) COMMENT 'Store gps latitude', " \
    f"is_signed TINYINT COMMENT 'Store signed(0,1)', " \
    f"operator VARCHAR(10) COMMENT 'Operator', " \
    f"operator_name VARCHAR(50) COMMENT 'Operator name', " \
    f"face_id VARCHAR(255) COMMENT 'Customer face ID', " \
    f"member_id VARCHAR(255) COMMENT 'Customer ID', " \
    f"store_create_date_ts TIMESTAMP COMMENT 'Store create date', " \
    f"origin VARCHAR(255) COMMENT 'Origin details', " \
    f"day_order_seq INT COMMENT 'Today's order', " \
    f"discount_rate DECIMAL(10, 5) COMMENT 'Discount rate', " \
    f"discount_type TINYINT COMMENT 'Discount category', " \
    f"discount DECIMAL(10, 5) COMMENT 'Discount', " \
    f"money_before_whole_discount DECIMAL(10, 5) COMMENT 'Full price', " \
    f"receivable DECIMAL(10, 5) COMMENT 'receivable price', " \
    f"erase DECIMAL(10, 5) COMMENT 'Discount price', " \
    f"small_change DECIMAL(10, 5) COMMENT 'Change amount', " \
    f"total_no_discount DECIMAL(10, 5) COMMENT 'Total price', " \
    f"pay_total DECIMAL(10, 5) COMMENT 'Payment', " \
    f"pay_type VARCHAR(10) COMMENT 'Payment method', " \
    f"payment_channel TINYINT COMMENT 'Payment way', " \
    f"payment_scenarios VARCHAR(15) COMMENT 'Payment description', " \
    f"product_count INT COMMENT 'Total buy in this order', " \
    f"date_ts TIMESTAMP COMMENT 'Order time', " \
    f"INDEX (receivable), INDEX (date_ts)"

# After collecting JSON data,write it into MySQL to store tables related to orders_detail
target_orders_detail_table_name = 'orders_detail'
target_orders_detail_table_create_cols = \
    f"order_id VARCHAR(255) COMMENT 'Order ID', " \
    f"barcode VARCHAR(255) COMMENT 'Product barcode', " \
    f"name VARCHAR(255) COMMENT 'Product name', " \
    f"count VARCHAR(255) COMMENT 'Product amount', " \
    f"price_per VARCHAR(255) COMMENT 'Product per price', " \
    f"retail_price VARCHAR(255) COMMENT 'Product retail price', " \
    f"trade_price VARCHAR(255) COMMENT 'Product trade price', " \
    f"category_id VARCHAR(255) COMMENT 'Product category ID', " \
    f"unit_id VARCHAR(255) COMMENT 'Product unit ID', " \
    f"PRIMARY KEY (order_id, barcode)"

# Table name: barcode for record barcode data
target_barcode_table_name = "barcode"
target_barcode_table_create_cols = '''
    `code` varchar(50) PRIMARY KEY COMMENT 'productBarcode',
    `name` varchar(200) DEFAULT '' COMMENT 'productName',
    `spec` varchar(200) DEFAULT '' COMMENT 'productSize',
    `trademark` varchar(100) DEFAULT '' COMMENT 'productTrademark',
    `addr` varchar(200) DEFAULT '' COMMENT 'productAddr',
    `units` varchar(50) DEFAULT '' COMMENT 'productUnits',
    `factory_name` varchar(200) DEFAULT '' COMMENT 'productFactoryName',
    `trade_price` varchar(20) DEFAULT '0.0000' COMMENT 'productTradePrice',
    `retail_price` varchar(20) DEFAULT '0.0000' COMMENT 'productRetailPrice',
    `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'productUpdateAt',
    `wholeunit` varchar(50) DEFAULT NULL COMMENT 'wholeunit',
    `wholenum` int(11) DEFAULT NULL COMMENT 'wholenum',
    `img` varchar(500) DEFAULT NULL COMMENT 'productImg',
    `src` varchar(20) DEFAULT NULL COMMENT 'productSrc'
'''
# ######## Configure with backend logs ####### #
# backend logs and create table details
target_backend_logs_table_name = "backend_logs_monitor"
target_backend_logs_table_create_cols = '''
                id INT PRIMARY KEY AUTO_INCREMENT,
                file_name VARCHAR(255) NOT NULL COMMENT 'processed file name',
                process_lines INT NULL COMMENT 'processed file line',
                process_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'processed file time'
'''
# backend files - target backend create table and column details
target_backend_logs_store_table_name = "backend_logs"
target_backend_logs_store_table_create_cols = '''
                id int PRIMARY KEY AUTO_INCREMENT COMMENT 'auto increased ID',
                log_time Timestamp(6) comment 'log time',
                log_level VARCHAR(10) COMMENT 'log level',
                log_module VARCHAR(50) COMMENT 'log module name',
                response_time INT COMMENT 'response time',
                province VARCHAR(30) COMMENT 'user province',
                city VARCHAR(30) COMMENT 'user city',
                log_text VARCHAR(255) COMMENT 'log text'
'''

# Source DB configuration
source_host = metadata_host
source_user = metadata_user
source_password = metadata_password
source_port = metadata_port
source_db_name = "source_data"
source_barcode_data_table_name = "sys_barcode"

# ######### --Barcode config start-- ######### #
# barcode，csv file path
barcode_output_csv_root_path = "/Users/kityua/PycharmProjects-gaoji/ETL-Python/output/barcode-csv/"
# barcode，csv file name
barcode_orders_output_csv_file_name = f'barcode-{time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))}.csv'
