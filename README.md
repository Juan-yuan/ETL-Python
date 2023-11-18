# ETL-Python
### Data to be collected:
1. Order data (information about user purchases sent to the backend through the internet)
  * Stored in a JSON file.
2. Product catalog data (stores information about products)
  * Stored in the backend MySQL database.
3. Backend log data (records information about backend access)
  * Stored in backend log files. 
  * (A `simulator` folder to generate backend log file), when you're using it, please remember to change the path accordingly

##### For the above three types of data, after collection, two tasks need to be completed:
1. Write data to MySQL warehouse.
2. Write data to CSV fil.

### Method with optimize process performance
1. Clear the buffer and write the content to the CSV file in every 1000 lines data
```python
count = 0
for x in xx:
    count += 1
    if count % 1000 == 0:
        x.flush()
```

2. Commit once if is 1000 lines of data
```python
count = 0
for x in xx:
    x.execute_without_autocommit(`sql`)
    count += 1
    if count % 1000 == 0:
        x.conn.commit()
x.conn.commit()
```

3. Compare max_last_update_time and current_data_time to avoid duplicate insert data process
```python
max_last_update_time = "2020-01-01 00:00:00"
for x in xx:
    current_data_time = table.update_at
    if current_data_time > max_last_update_time:
        max_last_update_time = current_data_time
    insert_sql = """"""
```

## ETL Files Agenda:
### json_service: 
   1. Processing JSON files, this JSON file will intermittently generate a new file within a specific folder. 
   2. Our program will execute periodically (e.g., every 5 minutes, 10 minutes)。
#### What we need to do is：
   1. Read JSON files through the program and then process them. 
   2. Generate logs file (logs for debugging).
   3. Out put to MySQL db (data warehouse).
   4. Out put to CSV file (for DA analysis).
##### Note: Files that have already been processed should not be processed again.
   
### mysql_service file: 
###### Note: The timestamp from the previous query will be recorded in MySQL. 
###### Each time, before new process, we need to check the update_at to determine from which time to start the current query
   1. Execute processSQL under config folder to create source_data db and sys_barcode table first.
   2. Processing data from MySQL db.
   3. Store data to MySQL.
   4. Out put to CSV (for DA analysis)
##### Tips:
   1. Use `replace into` in generate_insert_sql data model to avoid process error (from the data which only processed half from last insert query). 

## Databases:
    1. etl_python: testing purpose
    2. metadata: table (file_monitor) to use update_at to record the last process time
    3. retail: table (orders and orders_detail)
    4. source_data: table (sys_barcode) records streaming data

## Create 4 Python packages
    1. config: ETL configuration
    2. model: data model
    3. test: unit tests
    4. util: util functions

## Create logging 
    1. ERROR = 40
    2. WARNING = 30
    3. INFO = 20
    4. DEBUG = 10
    5. NOTEST = 0

### logging format reference:
    1. %(name)s : Name of the logger
    2. %(module)s : Module (name portion of filename)
    3. %(created)f : Time when the LogRecord was created (time.time() return value)
    4. %(msecs)d :  Millisecond portion of the creation time
    5. %(message)s : The result of record.getMessage(), computed just as the record is emitted
    6. %(asctime)s : Time of out put log
    7. %(levelname)s : Level of the log
    8. %(filename)s : The file name of the out put log
    9. %(lineno)d : The line of the out put log
### Example of a log:
    * 2023-05-14 17:05:38,681 - [INFO] - json_service.py[line:15]: Start processing json file...
    * %(asctime)s - [%(levelname)s] - %(filename)s[%[lineno]d]: %(message)s
### Code of above example:
```python
import logging
logger = logging.getLogger()
stream_handler = logging.StreamHandler()

fmt = logging.Formatter(
    "%(asctime)s - [%(levelname)s] - %(filename)s[%[lineno]d]: %(message)s"
)

stream_handler.setFormatter(fmt)
logger.addHandler(stream_handler)

logger.setLevel(10)
logger.debug("debug info~")
logger.info("info details~")
logger.warning("warning details~")
```

# ETL Python project workflow
1. Read which files are in the folder.
2. Query from the MySQL metadata database to find out which files have been processed.
3. Compare the results of 1 and 2 to identify files that have not been processed, prepare for local collection.
4. Read each line of the file.
5. Convert each line into a model.
6. Invoke the model to generate SQL statements and insert them into MySQL.
7. Invoke the model's to_csv method to write out the data as a CSV file.
8. Record metadata indicating which local files have been processed.




        