import time

from util.logging_util import init_logger
from util import file_util as fu
from config import project_config as conf
from util.mysql_util import MySQLUtil, get_processed_files
from model.retail_order_model import OrdersModel, OrderDetailModel

# check the process time
# print(time.strftime("%H:%M:%S", time.localtime(time.time())))
# 13:59:30

# Step 1, Handle files are need to process
logger = init_logger()
logger.info("Processing JSON data, the program has started...")

# identify which files need to be processed
files = fu.get_dir_files_list(conf.json_data_root_path)
print(files)
logger.info(f"Inspecting the JSON folder, the following files are found: {files}")

# Check which of these files can be processed and which ones have already been processed.
# Read the MySQL database to find the records of files that have already been processed for comparison
metadata_db_util = MySQLUtil()

# Target db instance
target_db_util = MySQLUtil(conf.target_host, conf.target_user, conf.target_password, conf.target_port)

processed_files = get_processed_files(metadata_db_util)
logger.info(f"After query MySQL, found below files already processed: ${processed_files}")

need_to_process_files = fu.get_new_by_compare_lists(processed_files, files)
logger.info(f"We found files need to be process after compared with MySQL：{need_to_process_files}")

# Step 2: Start to process files
global_count = 0
for file in need_to_process_files:
    order_model_list = []
    order_detail_model_list = []

    for line in open(file, "r", encoding="UTF-8"):
        line = line.replace("\n", "")
        order_model = OrdersModel(line)
        order_detail_model = OrderDetailModel(line)
        order_model_list.append(order_model)
        order_detail_model_list.append(order_detail_model)
    '''
    Filter Data
    Within the data, there is a field called "receivable" that indicates how much money the order has sold for.
    There is a lot of test data in the dataset, and the amounts in the "receivable" field are very large. 
    We will perform a simple assessment: we won't include data where the "receivable" amount is greater than 10,000.
    '''
    reserved_models = []
    for model in order_model_list:
        if model.receivable <= 10000:
            reserved_models.append(model)

    # 1. Write CSV and store to MySQL (retail and retail orders)
    order_csv_writer_f = open(
        conf.retail_output_csv_root_path + conf.retail_orders_output_csv_file_name,
        "a",
        encoding="UTF-8"
    )
    order_detail_csv_write_f = open(
        conf.retail_output_csv_root_path + conf.retail_orders_detail_output_csv_file_name,
        "a",
        encoding="UTF-8"
    )
    # Process order
    for model in reserved_models:
        csv_line = model.to_csv()
        order_csv_writer_f.write(csv_line)
        order_csv_writer_f.write("\n")
    order_csv_writer_f.close()
    # Process order detail
    for model_detail in order_detail_model_list:
        for single_product_model in model_detail.products_detail:
            csv_line = single_product_model.to_csv()
            order_detail_csv_write_f.write(csv_line)
            order_detail_csv_write_f.write("\n")
    order_detail_csv_write_f.close()
# logger.info(f"完成了csv备份文件的写出，写出到了: {conf.retail_output_csv_root_path}")

    # 2. Store orders and order details data to MySQL db
    # create table
    target_db_util.check_table_exists_and_create(
        conf.target_db_name,
        conf.target_orders_table_name,
        conf.target_orders_table_create_cols
    )
    target_db_util.check_table_exists_and_create(
        conf.target_db_name,
        conf.target_orders_detail_table_name,
        conf.target_orders_detail_table_create_cols
    )
    # insert data
    for model in reserved_models:
        insert_sql = model.generate_insert_sql()
        target_db_util.select_db(conf.target_db_name)
        target_db_util.execute(insert_sql)
    # insert order detail data
    for model in order_detail_model_list:
        insert_sql = model.generate_insert_sql()
        target_db_util.select_db(conf.target_db_name)
        target_db_util.execute(insert_sql)

logger.info(f"Finished CSV back up，write to：{conf.retail_output_csv_root_path}")
logger.info(f"Finished store data to MySQL "
            f"Processed ：{len(reserved_models)} data")
# check the process time
# print(time.strftime("%H:%M:%S", time.localtime(time.time())))
# 13:59:30



