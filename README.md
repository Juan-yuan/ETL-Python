# ETL-Python
### Data to be collected:
1. Order data (information about user purchases sent to the backend through the internet)
  * Stored in a JSON file.
2. Product catalog data (stores information about products)
  * Stored in the backend MySQL database.
3. Backend log data (records information about backend access)
  * Stored in backend log files.

##### For the above three types of data, after collection, two tasks need to be completed:
1. Write data to MySQL warehouse.
2. Write data to CSV fil.

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
   1. Execute processSQL under config folder to create source_data db and sys_barcode table.
   2. Processing data from MySQL db.
   3. Store data to MySQL.
   4. Out put to CSV (for DA analysis)

## databases:
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




        