# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import sqlite3;

class AmazonedaPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
        #self.ids_seen=set()
        
    def create_connection(self):
        self.conn=sqlite3.connect("amazon.db")
        self.curr=self.conn.cursor()
    
    def create_table(self):
         self.curr.execute("""DROP TABLE IF EXISTS amazon_tb""")
         self.curr.execute("""create table amazon_tb(
                           model_name text,
                           model_price text,
                           delivery_type text
                            )""")
                        
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self,item):
        self.curr.execute("""insert into amazon_tb values (?,?,?)""",(
            item['model_name'],
            item['model_price'],
            item['delivery_type']
        ))
        self.conn.commit()
