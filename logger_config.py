import logging
import os

def setup_logger(log_file_name="game_log.txt"):
    # 日志文件的目录
    log_dir = os.path.join(os.getcwd(), 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file_path = os.path.join(log_dir, log_file_name)

    # 创建一个fileHandler
    file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    # 创建一个 handler，用于写入控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # 设置 handler 的级别

    # 创建一个formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 获取根logger或创建一个新的logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # 添加file_handler到logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# 初始化并返回配置好的logger
#logger = setup_logger()
