import sys
from model.barcode_model import BarcodeModel
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

# TODO: Step 3: create data model
barcode_models = []
for single_line_result in result:
    # single_line_result is a tuple
    code = single_line_result[0]
    name = single_line_result[1]
    spec = single_line_result[2]
    trademark = single_line_result[3]
    addr = single_line_result[4]
    units = single_line_result[5]
    factory_name = single_line_result[6]
    trade_price = single_line_result[7]
    retail_price = single_line_result[8]
    update_at = str(single_line_result[9])
    wholeunit = single_line_result[10]
    wholenum = single_line_result[11]
    img = single_line_result[12]
    src = single_line_result[13]

    model = BarcodeModel(
        code=code,
        name=name,
        spec=spec,
        trademark=trademark,
        addr=addr,
        units=units,
        factory_name=factory_name,
        trade_price=trade_price,
        retail_price=retail_price,
        update_at=update_at,
        wholeunit=wholeunit,
        wholenum=wholenum,
        img=img,
        src=src
    )
    barcode_models.append(model)

