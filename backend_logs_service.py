'''
1. Read which files are in the folder.
2. Query from the MySQL metadata database to find out which files have been processed.
3. Compare the results of 1 and 2 to identify files that have not been processed, prepare for local collection.
4. Read each line of the file.
5. Convert each line into a model.
6. Invoke the model to generate SQL statements and insert them into MySQL.
7. Invoke the model's to_csv method to write out the data as a CSV file.
8. Record metadata indicating which local files have been processed.
'''

from util import file_util as fu
from util.mysql_util import MySQLUtil, get_processed_files
from config import project_config as conf
from model.backend_logs_model import BackendLogsModel

# TODO 1: Read all the files in backend_logs folder
files = fu.get_dir_files_list("/Users/kityua/PycharmProjects-gaoji/ETL-Python/backend_logs/")

# TODO 2: Read mysql metadata
metadata_db_util = MySQLUtil()

# Create target db_util
target_db_util = MySQLUtil(
    conf.target_host,
    user=conf.target_user,
    password=conf.target_password,
    port=conf.target_port,
    charset=conf.mysql_charset,
    autocommit=False
)

target_db_util.check_table_exists_and_create(
    conf.target_db_name,
    conf.target_backend_logs_store_table_name,
    conf.target_backend_logs_store_table_create_cols
)

processed_files = get_processed_files(
    db_util=metadata_db_util,
    db_name=conf.metadata_db_name,
    table_name=conf.target_backend_logs_table_name,
    create_cols=conf.target_backend_logs_table_create_cols
)

# TODO 3: Compare the files and find the files that have not been processed
need_to_process_files = fu.get_new_by_compare_lists(processed_files, files)

# TODO 4: Read each line in the file and process data
for file in need_to_process_files:
    for line in open(file, "r", encoding="UTF-8"):
        line = line.replace("\n", "")
        # TODO Step 5: Instance data modelling
        model = BackendLogsModel(line)

        # TODO Step 6: Write into sql
        insert_sql = model.generate_insert_sql()
        target_db_util.select_db(conf.target_db_name)
        target_db_util.execute_without_autocommit(insert_sql)

