'''
backend logs simulator
'''
import datetime
import random
import time


single_log_lines = 1024  # lines of generated file
generate_files = 5 # amount of generated files

output_path = "/Users/kityua/PycharmProjects-gaoji/ETL-Python/backend_logs/"
log_level_array = ['WARN', 'WARN', 'WARN', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO'
                   'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO',
                   'ERROR']

backend_files_name = ['barcode_service.py', 'barcode_service.py', 'barcode_service.py',
                      'orders_service.py', 'orders_service.py', 'orders_service.py', 'orders_service.py',
                      'orders_service.py', 'orders_service.py',
                      'shop_manager.py', 'shop_manager.py',
                      'user_manager.py', 'user_manager.py', 'user_manager.py',
                      'goods_manager.py', 'goods_manager.py', 'goods_manager.py', 'goods_manager.py',
                      'goods_manager.py', 'goods_manager.py',
                      'base_network.py', 'base_network.py',
                      'event.py', 'event.py', 'event.py', 'event.py', 'event.py', 'event.py', 'event.py']

visitor_areas = {
    'Beijing': ['Haidian', 'Daxing', 'Fengtai', 'Chaoyang District', 'Changping District', 'Haidian District', 'Huairou District'],
    'Shanghai': ['Jinan', 'Huangpu', 'Xuhui District', 'Putuo District', 'Yangpu District', 'Baoshan District', 'Pudong New Area'],
    'Chongqing': ['Wanzhou', 'Beiling District', 'Peilin District', 'Hanzhong District', 'Shapingba District', 'Jiulongpo District', 'Nan an District'],
    'Jiangsu': ['Nanjing', 'Suzhou', 'Wuxi', 'Changzhou', 'Suqian', 'Zhangjiagang'],
    'Anhui': ['Fuyang', 'Lu an', 'Hefei', 'Chizhou', 'Tongling', 'Wuhu'],
    'Shandong': ['Jinan', 'Qingdao', 'Heze'],
    'Hubei': ['Wuhan', 'Wuhan', 'Wuhan', 'Shiyan', 'Jingzhou', 'Enshi Tujia'],
    'Guangdong': ['Guangzhou', 'Guangzhou', 'Guangzhou', 'Shenzhen', 'Shenzhen', 'Shenzhen', 'Zhuhai'],
    'Tianjin': ['Heping District', 'Hedong District', 'Hexi District', 'Wuqing District', 'Baodi District'],
    'Hunan': ['Changsha', 'Changsha', 'Changsha', 'Changsha', 'Changsha', 'Changsha', 'Changsha', 'Zhuzhou', 'Zhangjiajie', 'Changde', 'Yiyang'],
    'Zhejiang': ['Hangzhou', 'Hangzhou', 'Huzhou', 'Shaoxing', 'Zhoushan', 'Jinhua', 'Jiaxing', 'Lishui']
}

visitor_province = ['Beijing', 'Shanghai', 'Chongqing', 'Jiangsu', 'Anhui', 'Shandong', 'Hubei', 'Guangdong', 'Tianjin', 'Hunan', 'Zhejiang']


response_flag = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
response_for_error_flag = [1, 1, 1, 1, 1, 0]

for j in range(0, generate_files):
    write_file_path = f'{output_path}{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'
    with open(write_file_path, 'w', encoding="UTF-8") as f:
        for i in range(single_log_lines):
            date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            log_level = log_level_array[random.randint(0, len(log_level_array) - 1)]
            file_name = backend_files_name[random.randint(0, len(backend_files_name) - 1)]
            if not log_level == "ERROR":
                if response_flag[random.randint(0, len(response_flag) - 1)] == 1:
                    response_time = random.randint(0, 1000)
                else:
                    response_time = random.randint(1000, 9999)
            else:
                if response_for_error_flag[random.randint(0, len(response_for_error_flag) - 1)] == 1:
                    response_time = random.randint(0, 1000)
                else:
                    response_time = random.randint(1000, 9999)

            province = visitor_province[random.randint(0, len(visitor_province) - 1)]
            city = visitor_areas[province][random.randint(0, len(visitor_areas[province]) - 1)]

            log_str = f"{date_str}\t[{log_level}]\t{file_name}\tresponse time:{response_time}ms\t{province}\t{city}\t" \
                      f"Here is the log details..."

            f.write(log_str)
            f.write("\n")
    fileAmount = j + 1
    print(f"Finished: {fileAmount} file{'' if fileAmount == 1 else 's'}, file path is: {write_file_path}, lines: {single_log_lines}")
    time.sleep(1)
