import scrapy
from scrapy.http import Request
from spider.items import SpiderItem
import re

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['suning.com']
    # 设置起始URL为商品第一页
    start_urls = ['https://search.suning.com/手机/']
    # def start_requests(self):
        # cookies="isg=BIKCcAVWVow8cEpN8mxPLTeo0Y7kU4Zt-9oDc8yWt_W8HyqZteNsfR6dz5tjVP4F; l=eBS5MxdnjexmxwWzBO5Cnurza77TgdOcckPzaNbMiInca1khwwcUCNCBh_gwkdtfgtfbieKP8qXwPRFWJEUZwJdQP8KrCyCkVc9wG; tfstk=cOkdBgs0ehIpgjt_oXdMNROlDtodC4ATz6aceHo6RNsWvtDrEf1m5r4V8stQcbNwX; uc1=cookie21=VFC%2FuZ9ainBZ&cookie14=Uoe2ySRFkdZTSQ%3D%3D&existShop=false&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&pas=0; mt=ci=6_1; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; _nk_=tb124198345; _tb_token_=effaf3604e51f; cookie1=VAjFzBqEYifxZiigbESyveTY4LuHNAWrEOXUTimGJjM%3D; cookie17=VyyY4IdDCD%2Fejg%3D%3D; cookie2=1406f8e7d8c298e4e6c520505572ffdb; csg=70155c3e; dnk=tb124198345; existShop=MTYyNDMzMDcxNA%3D%3D; lgc=tb124198345; sg=57f; sgcookie=E10063tjRSvWYpnWn2%2FyNp6jmAdtsxlgRZRXarip8YrnvjueTPu6x3grnmieMTH1H%2B%2F3Uv9xUTASI2Qz1bbvO7bQhQ%3D%3D; skt=437c19b1c4a88b64; t=535a29980bfefde4ac379f4c13c6477a; tracknick=tb124198345; uc3=nk2=F5REPEVPHGDoTMw%3D&id2=VyyY4IdDCD%2Fejg%3D%3D&lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dCuw1cGpSrGZr%2FtIE%3D; uc4=nk4=0%40FY4PbhL67b9kIcKpqXOXUzn9k%2BiixQ%3D%3D&id4=0%40VXtXC87yUEESkuKVaeSGmwiGNpNB; unb=4090092387; cna=AP1SGVfGJEgCAbaVxqygXNoV; _samesite_flag_=true; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=5f0adfbe996908c5d310d5ab352059bc_1624337199202; _m_h5_tk_enc=f13ec79ed01efb8f8fd0dc38c6600c5e; xlly_s=1; thw=cn; enc=hjLTqoh2kCLGuYKex01RCT1Lz2quWWGNTwGemXzZ4MoRoYIaQliPqaFxe41VDzx%2FBFzpWACoQb%2Bd%2Bcw3isDv1w%3D%3D"
        # cookies ="isg=BGpqxeV8_vRKQHIFKvTXZZ-wudYM2-41I9IbO_Qj0L1IJwvh3GuPRbzRt9M7zGbN; l=eBS5MxdnjexmxjmaBO5CEurza77tEIR08kPzaNbMiInca1R51FOr-NCBh1c2RdtfgtCvjetP8qXwPRFeJhzawJdQP8L5cbu8ex7d.; tfstk=cz75BNZwd9QqFD0E9_NqY3UgXLYOZ1uWg79cNGcBwfxQlCB5if2wI5NNtxC67I1..; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=V32FPkk%2FgPzW&cookie14=Uoe2ySRFk9t%2FUw%3D%3D&existShop=false&cookie15=UtASsssmOIJ0bQ%3D%3D&pas=0; mt=ci=6_1; _cc_=W5iHLLyFfA%3D%3D; _l_g_=Ug%3D%3D; _nk_=tb124198345; _tb_token_=effaf3604e51f; cookie1=VAjFzBqEYifxZiigbESyveTY4LuHNAWrEOXUTimGJjM%3D; cookie17=VyyY4IdDCD%2Fejg%3D%3D; cookie2=1406f8e7d8c298e4e6c520505572ffdb; csg=70155c3e; dnk=tb124198345; existShop=MTYyNDMzMDcxNA%3D%3D; lgc=tb124198345; sg=57f; sgcookie=E10063tjRSvWYpnWn2%2FyNp6jmAdtsxlgRZRXarip8YrnvjueTPu6x3grnmieMTH1H%2B%2F3Uv9xUTASI2Qz1bbvO7bQhQ%3D%3D; skt=437c19b1c4a88b64; t=535a29980bfefde4ac379f4c13c6477a; tracknick=tb124198345; uc3=nk2=F5REPEVPHGDoTMw%3D&id2=VyyY4IdDCD%2Fejg%3D%3D&lg2=UtASsssmOIJ0bQ%3D%3D&vt3=F8dCuw1cGpSrGZr%2FtIE%3D; uc4=nk4=0%40FY4PbhL67b9kIcKpqXOXUzn9k%2BiixQ%3D%3D&id4=0%40VXtXC87yUEESkuKVaeSGmwiGNpNB; unb=4090092387; cna=AP1SGVfGJEgCAbaVxqygXNoV; _samesite_flag_=true; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=5f0adfbe996908c5d310d5ab352059bc_1624337199202; _m_h5_tk_enc=f13ec79ed01efb8f8fd0dc38c6600c5e; xlly_s=1; thw=cn; enc=hjLTqoh2kCLGuYKex01RCT1Lz2quWWGNTwGemXzZ4MoRoYIaQliPqaFxe41VDzx%2FBFzpWACoQb%2Bd%2Bcw3isDv1w%3D%3D"
        # cookies ={i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        # yield scrapy.Request(
        #     self.start_urls[0],
        #     callback=self.parse,
        #     cookies=cookies
        # )

    def parse(self, response):
        # print(re.findall("马马马马0512",response.body.decode()))
        item = SpiderItem()
        # 设定爬取的XPath表达式
        lists = response.xpath('//*[@id="product-list"]/ul/li')
        for i in lists:
            item["title"] = i.xpath("./div/div/div[2]/div[2]/a/@title").get()
            item["link"] = i.xpath("./div/div/div[2]/div[2]/a/@title").get()
            item["comment"] = i.xpath("./div/div/div[2]/div[2]/a/@title").get()
            yield item
        # 设置爬取前10页
        # for i in range(3,2,-1):
        #     # 构造商品URL
        #
        #
        #     url = "https://s.taobao.com/search?q=手机&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.21814703.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=" + str(i*44)
        #     # yield Request(url, callback=self.parse)
        #
        #     yield scrapy.Request(url=url, callback=self.parse)
