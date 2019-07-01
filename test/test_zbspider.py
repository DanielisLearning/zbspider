"""
对 zbspider 进行测试
"""
import unittest
from config import TestConfig
from zbspider.spider import Spider
from zbspider.mode.sqlmanager import SQLManager


class TestZBSpider(unittest.TestCase):
    """ test class zbspider """

    def setUp(self):
        self.verifyString = 'test'
        self.config = TestConfig()

    def test_config(self):
        self.assertTrue(self.config.TESTING)
        self.assertTrue(self.config.DEBUG)

    def test_spider_get(self):
        spider = Spider(self.config.URL, **self.config.SPIDER)
        result = spider.get()
        self.assertIsInstance(result, str)
        self.assertIn('中国招标与采购网', result)
        self.assertIn('福建', result)

    def test_table_name(self):
        sql = SQLManager(self.config.DATABASE)
        self.assertEqual("zbtable", sql.__tablename__)
        sql.close()

    def test_last_one_title(self):
        sql = SQLManager(self.config.DATABASE)
        last_one_title = sql.get_last_one_title()
        self.assertIsInstance(last_one_title, dict)
        sql.close()
