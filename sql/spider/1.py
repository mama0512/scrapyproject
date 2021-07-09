# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import re
# import time
# import pymongo
# from sn_config import *
# from selenium.webdriver.common.keys import Keys
# from pyquery import PyQuery as pq
#
# MONGO_URL = 'locallost'
# MOGODB = 'SUNING'
# # browser = webdriver.PhantomJS(service_args=SERVICE_ASK)  # 无可视化的浏览器,需安装插件
# # browser = webdriver.Chrome() # 可视化浏览器
# connect = pymongo.MongoClient(MONGO_URL)  # 连接数据库
# db = connect[MONGODB]
#
#
# def search():
#     # 请求苏宁易购首页
#     browser.get('https://www.suning.com/')
#     # 找到输入的搜索框
#     _input = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '#searchKeywords'))
#     )
#     # 找到搜索按钮
#     submit = WebDriverWait(browser, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "#searchSubmit")))
#     _input.send_keys(keyword)
#     submit.click()
#     # 找到总页数
#     target = browser.find_element_by_css_selector('#bottom_pager > div > span.page-more')
#     browser.execute_script("arguments[0].scrollIntoView();", target)
#     time.sleep(3)
#     total = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '#bottom_pager > div > span.page-more')))
#     # 对找到的总页数进行正则处理，并返回int类型的页数
#     _total = total.text
#     # print(_total)
#     pattern = re.compile('\S\S(\d+).*?')
#     result = re.search(pattern, _total)
#     parse_html()
#     return int(result.group(0)[1:])
#
#
# def next_page(page):
#     print('正在翻页', page)
#     try:
#         # 找到页数的输入框
#         time.sleep(1)
#         inputs = WebDriverWait(browser, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, '#bottomPage')))
#         time.sleep(1)
#         inputs.clear()
#         # 找到确定的按钮
#         submit = WebDriverWait(browser, 10).until(
#             EC.element_to_be_clickable(
#                 (By.CSS_SELECTOR, "#bottom_pager > div > a.page-more.ensure")))
#         inputs.send_keys(page)
#         submit.send_keys(Keys.ENTER)
#         target = browser.find_element_by_css_selector('#bottom_pager > div > span.page-more')
#         browser.execute_script("arguments[0].scrollIntoView();", target)  # 将页面下拉至底部休息3秒等待数据加载
#         time.sleep(3)
#         # 进行判定：高亮下的页数是否和输入框的一致
#         WebDriverWait(browser, 10).until(
#             EC.element_to_be_clickable(
#                 (By.CSS_SELECTOR, '#bottom_pager > div > a.cur')), str(page))
#         parse_html()
#     except Exception as e:
#         print(e.args)
#         next_page(page)
#
#
# def parse_html():
#     try:
#         # 选择整个展示框
#         WebDriverWait(browser, 20).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, '#product-list .item-wrap')))
#         # product-list
#         html = browser.page_source
#         doc = pq(html)
#         # 拿到所有的item，进行迭代，拿到所有商品的数据
#         items = doc('#product-list .item-wrap').items()
#         for item in items:
#             proucts = {
#                 'price': item.find('.def-price').text().replace('\n', ' '),
#                 'description': item.find('.title-selling-point').text().strip().replace('\n', ' '),
#                 'shop': item.find('.store-stock').text(),
#             }
#             if db[MONGO_TABLE].insert(proucts):
#                 print('正在保存', proucts.get('description'))
#     except TimeoutError:
#         parse_html()
#
#
# def main():
#     try:
#         total = search()  # 得到的总页数
#         for i in range(2, total + 1):
#             next_page(i)
#             time.sleep(2)
#     except Exception as e:
#         print(e.args)
#     finally:
#         browser.close()
#
#
# if __name__ == '__main__':
#     main()
#
#
# # from PySide.QtGui import *
# # from PySide.QtWebKit import *
# # from PySide.QtCore import *
# #
# # import sys
# # import time
# #
# # class BrowserRender(QWebView):
# #     def __init__(self, show=True):
# #         self.app = QApplication(sys.argv)
# #         QWebView.__init__(self)
# #         if show:
# #             self.show()
# #    def download(self, url, timeout=60):
# #         loop = QEventLoop()
# #         timer = QTimer()
# #         timer.setSingleShot(True)
# #         timer.timeout.connect(loop.quit)
# #         self.loadFinished.connect(loop.quit)
# #         self.load(QUrl(url))
# #         timer.start(timeout * 1000)
# #         loop.exec_()
# #         if timer.isActive():
# #             timer.stop()
# #             return self.html()
# #         else:
# #             print "Request time out: " + url
# #    def html(self):
# #        return self.page().mainFrame().toHtml()
# #
# #    def find(self, pattern):
# #        return self.page().mainFrame().findAllElements(pattern)
# #
# #    def attr(self, pattern, name, value):
# #        for e in self.find(pattern):
# #            e.setAttribute(name, value)
# #
# #    def text(self, pattern, value):
# #        for e in self.find(pattern):
# #            e.setPlainText(value)
# #
# #    def click(self, pattern):
# #        for e in self.find(patter):
# #            e.evaluateJavaScript("this.click()")
# #
# #    """
# #    def wait_load(self, pattern, timeout=60):
# #         deadline = time.time() + timeout
# #         while time.time() < deadline:
# #             self.app.processEvents()
# #             matches = self.find(pattern)
# #             if matches:
# #                 return matches
# #         print "wait load time out"
# #     """
# #
# # if __name__=="__main__":
# #     br = BrowserRender(show=False)
# #     br.download("https://product.suning.com/0000000000/152709847.html? \
# #      srcpoint=index3_homepage1_32618213038_prod02")
# #     price = br.find("span.mainprice" )
# #     print (price[0].toPlainText().encode("utf-8").strip()) #如果不加encode("utf-8")会出现UnicodeEncodeError：gbk无法对u'\xa5'进行编码的错误