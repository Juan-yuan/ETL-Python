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

# Instance of target db
target_db_util = MySQLUtil(
    host=conf.target_host,
    user=conf.target_user,
    password=conf.target_password,
    port=conf.target_port
)

# TODO: Step 2: Read data from source data db, if table is not exist, then exit
if not source_db_util.check_table_exists(conf.source_db_name, conf.source_barcode_data_table_name):
    logger.error(f"source data db: {conf.source_db_name} doesn't have table: {conf.source_barcode_data_table_name}，"
                 f"exit process.")
    sys.exit(1)  # sys.exit()  parameter: 0 means reasonable exit, parameter: 1 means force exit

target_db_util.check_table_exists_and_create(
    conf.target_db_name,
    conf.target_barcode_table_name,
    conf.target_barcode_table_create_cols
)

# Select metadata
last_update_time = None
metadata_db_util.select_db(conf.metadata_db_name)

if not metadata_db_util.check_table_exists(conf.metadata_db_name, conf.metadata_barcode_table_name):
    metadata_db_util.check_table_exists_and_create(
        conf.metadata_db_name,
        conf.metadata_barcode_table_name,
        conf.metadata_barcode_table_create_cols
    )
else:
    query_sql = f"SELECT time_record FROM {conf.metadata_barcode_table_name} ORDER BY time_record DESC LIMIT 1"
    result = metadata_db_util.query(query_sql)
    # Check if it has value
    if len(result) != 0:
        last_update_time = str(result[0][0])

if last_update_time:
    sql = f"SELECT * FROM {conf.source_barcode_data_table_name} WHERE updateAt >= '{last_update_time}'" \
          f"ORDER BY updateAt"
else:
    sql = f"SELECT * FROM {conf.source_barcode_data_table_name} ORDER BY updateAt"

source_db_util.select_db(conf.source_db_name)
result = source_db_util.query(sql)
# print(result)

# TODO: Step 3: create data model to insert data
