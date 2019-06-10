"""
配置文件
"""
import os
# 根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config():
    """基础配置"""
    # 数据库位置
    DATABASE = os.path.join(BASE_DIR, "database/sqlite.db")
    # email 配置
    EMAIL = {
        'host':'smtp.fjiti.com',
        'user':'xf@fjiti.com',
        'pass':'hegexinfu123',
        'sender':'xf@fjiti.com',
        'receivers':'grq@fjiti.com'
    }