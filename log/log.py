"""
    Copyright (C) 2024 All rights reserved.
    Author: songzhuhuan
    Time: 2024/4/26
    File: log.py
    Description: 日志模块
"""

import os
import logging
import logging.handlers


def init_log(log_path, name=None, level=logging.DEBUG, when="D", backup=7,
             format="%(name)s:%(levelname)s:%(asctime)s:%(filename)s:%(lineno)d * %(thread)d %(message)s",
             datefmt="%m-%d %H:%M:%S"):
    """
        新增日志模块
    """
    formatter = logging.Formatter(format, datefmt)
    logger = logging.getLogger(name)
    logger.setLevel(level)

    dir = os.path.dirname(log_path)
    if not os.path.isdir(dir):
        os.makedirs(dir)

    # 输出info以上的信息
    handler = logging.handlers.TimedRotatingFileHandler(filename=log_path + ".log", when=when, backupCount=backup)
    handler.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # 输出warning以上的信息
    handler = logging.handlers.TimedRotatingFileHandler(filename=log_path + ".log.wf", when=when, backupCount=backup)
    handler.setLevel(logging.WARNING)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # 标准输出流
    # stdout_handler = logging.StreamHandler(stream=sys.stdout)
    # stdout_handler.setLevel(level)
    # stdout_handler.setFormatter(formatter)
    # logger.addHandler(stdout_handler)

    return logger


logger = init_log("./log/spider_blockchain", "spider_blockchain")


if __name__ == "__main__":
    logger.info("info")
    logger.warning("warn")
    logger.error("error")
