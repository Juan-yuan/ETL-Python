import time

# ######### -- Configure the log output path ######### #
log_root_path = "/Users/kityua/PycharmProjects-gaoji/ETL-Python/logs/"

# ######### --Configure the log output filename ######### #
log_name = f'pyetl-{time.strftime("%Y-%m-%d %H", time.localtime(time.time()))}.log'
# print(log_name)  # 2023-07-08 14:09:43

# ######### --Configure with process JSON file ######### #
json_data_root_path = "/Users/kityua/PycharmProjects-gaoji/ETL-Python/json"

# ######## == Configure with DB ####### #
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
