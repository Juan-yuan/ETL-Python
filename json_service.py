from util.logging_util import init_logger
from util import file_util as fu
from config import project_config as conf
from util.mysql_util import MySQLUtil, get_processed_files
from model.retail_order_model import OrdersModel

# Step 1, Handle files are need to process
logger = init_logger()
logger.info("Processing JSON data, the program has started...")

# identify which files need to be processed
files = fu.get_dir_files_list(conf.json_data_root_path)
print(files)
logger.info(f"Inspecting the JSON folder, the following files are found: {files}")

# Check which of these files can be processed and which ones have already been processed.
# Read the MySQL database to find the records of files that have already been processed for comparison
db_util = MySQLUtil()
processed_files = get_processed_files(db_util)

need_to_process_files = fu.get_new_by_compare_lists(processed_files, files)
logger.info(f"We found files need to be process after compared with MySQL：{need_to_process_files}")

# Step 2: Start to process files
global_count = 0
for file in need_to_process_files:
    for line in open(file, "r", encoding="UTF-8"):
        line = line.replace("\n", "")
        order_model = OrdersModel(line)
        print(order_model.order_id)
        break
