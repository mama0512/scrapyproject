

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class JdphonePipeline:
    def process_item(self, item, spider):

        # 连接数据库并创建游标，本文中的test.db为笔者自行创建的数据库文件,结构见本代码后的图片
        conn = sqlite3.connect("/Users/malizhi/Desktop/ma/git_codes/scrapyproject/sql/test.db")
        cursor = conn.cursor()


        title = item["title"]
        link = item["url"]
        comment = item["comment_num"]
        price = item["price"]
        info = item["info"]



        # 构造SQL语句并通过游标执行
        sql = "insert into phone(title,link,comment,price,info) VALUES('"+title+"','"+link+"','"+comment+"','"+price+"','"+info+"')"
        cursor.execute(sql)
        # 注意必须要提交事件才能够使数据库修改操作生效
        conn.commit()
        # 输出爬取的内容
        # print(title)
        # print(link)
        # print(comment)

        # 关闭游标以及数据库连接

        cursor.close()
        conn.close()
        print(item)
        return item

