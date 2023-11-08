import sys
from util.logging_util import init_logger
from util.mysql_util import MySQLUtil
from config import project_config as conf

logger = init_logger()
logger.info("Start processing MySQL data ...")

# TODO: Step 1: Create metadata db util
metadata_db_util = MySQLUtil()
source_db_util = MySQLUtil(
    host=conf.source_host,
    user=conf.source_user,
    password=conf.source_password,
    port=conf.source_port
)

# TODO: Step 2: Read data from source data db, if table is not exist, then exit
if not source_db_util.check_table_exists(conf.source_db_name, conf.source_barcode_data_table_name):
    logger.error(f"source data db: {conf.source_db_name} doesn't have table: {conf.source_barcode_data_table_name}，"
                 f"exit process.")
    sys.exit(1)  # sys.exit()  parameter: 0 means reasonable exit, parameter: 1 means force exit
