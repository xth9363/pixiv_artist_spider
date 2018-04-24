# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from Pzhan.items import PzhanItem
import re
import _asd
import json


class NewArtSpider(scrapy.Spider):
    # 这里需要填写
    # 画师ID
    artis_id = 648285
    # 可用的P站账号
    login_account = '123@qq.com'
    # 该账号的密码
    login_pwd = '123456'

    name = 'new_art'
    allowed_domains = ['pixiv.net']
    start_urls = ['https://www.pixiv.net/bookmark.php']

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4",
        "Referer": "https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index",
        'Host': 'accounts.pixiv.net',
        'Origin': 'https://accounts.pixiv.net',
        'Cookie': 'p_ab_id=3; p_ab_id_2=5; user_language=zh; c_type=24; a_type=0; b_type=1; device_token=61862d21a20d2ecd9c719f27173e436f; module_orders_mypage=[{"name":"recommended_illusts","visible":true},{"name":"everyone_new_illusts","visible":true},{"name":"following_new_illusts","visible":true},{"name":"mypixiv_new_illusts","visible":true},{"name":"fanbox","visible":true},{"name":"featured_tags","visible":true},{"name":"contests","visible":true},{"name":"user_events","visible":true},{"name":"sensei_courses","visible":true},{"name":"spotlight","visible":true},{"name":"booth_follow_items","visible":true}]; __utma=235335808.1272705403.1503209995.1510793447.1510797554.15; __utmz=235335808.1510797554.15.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmcct=/link; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=5174309=1^9=p_ab_id=3=1^10=p_ab_id_2=5=1^11=lang=zh=1; _td=61db3ab3-fb5f-43f2-a585-a7aa18997f9c; PHPSESSID=8df12eedbff10cefb943450a0eacc771; _gat=1; _gat_UA-76252338-4=1; __utma=75212034.2078753273.1510793488.1510793488.1510821192.2; __utmb=75212034.4.7.1510821200795; __utmc=75212034; __utmz=75212034.1510821192.2.2.utmcsr=pixiv.net|utmccn=(referral)|utmcmd=referral|utmcct=/; _ga=GA1.2.1272705403.1503209995; _gid=GA1.2.1939517424.1510793490; _ga=GA1.3.1272705403.1503209995; _gid=GA1.3.1939517424.1510793490; login_bc=1',
        'X-Requested-With': 'XMLHttpRequest'
    }

    # 这里填用户的作品页面
    # artistUrl = 'https://www.pixiv.net/member_illust.php?id=4147414'
    artistUrl = 'https://www.pixiv.net/member_illust.php?id=%s' % str(artis_id)

    # 开始请求登录页面
    def start_requests(self):
        # return [Request("https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index",
        #                 meta={'cookiejar': 1}, callback=self.post_login)]
        return [Request("https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index",
                        callback=self.post_login)]

    # 提交登录表单 模拟登陆
    def post_login(self, response):
        # 先去拿隐藏的表单参数authenticity_token
        authenticity_token = response.xpath('//input[@name="post_key"]/@value').extract_first()
        print(authenticity_token)
        # FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        # 登陆成功后, 会调用after_login回调函数，如果url跟Request页面的一样就省略掉
        return [FormRequest.from_response(response,
                                          url='https://accounts.pixiv.net/api/login?lang=zh',
                                          # meta={'cookiejar': response.meta['cookiejar']},
                                          headers=self.headers,  # 注意此处的headers
                                          formdata={
                                              'post_key': authenticity_token,
                                              # 模拟登陆
                                              # 账号
                                              'pixiv_id': self.login_account,
                                              # 密码
                                              'password': self.login_pwd,
                                              'source': 'pc',
                                              'ref': 'wwwtop_accounts_index',
                                              'return_to': 'https://www.pixiv.net/bookmark.php',
                                          },
                                          callback=self.after_login,
                                          dont_filter=True
                                          )]

    # 登陆后爬取页面
    def after_login(self, response):
        # from myFunc.ff import getDir
        # getDir(response)
        # startpage = 20
        # endpage = 27
        url = 'https://www.pixiv.net/bookmark.php'
        print("登陆成功！")
        # body=response.text
        # print(body)
        # for i in range(startpage, endpage + 1):
        #     # time.sleep(0.5)
        #     # print("爬取第"+str(i)+"页:")
        #     yield Request(url + "?type=user&rest=show&p=" + str(i), meta={'cookiejar': response.meta['cookiejar']})

        # yield Request(url=self.artistUrl, meta={'cookiejar': response.meta['cookiejar']}, callback=self.parse2)
        yield Request(url=self.artistUrl, callback=self.parse2, headers=response.headers, )
        # yield Request(url="https://www.pixiv.net/member_illust.php?mode=medium&illust_id=64860518", callback=self.test,headers=response.headers,)





        # def test(self,response):
        #     item = PzhanItem()
        #     item["name"] = response.xpath('//section[@class="work-info"]/h1[1]/text()').extract()[0]
        #     item["size"] = response.xpath('//ul[@class="meta"][1]/li[2]/text()').extract()[0]
        #     item["artist"] = response.xpath('//a[@class="user-name"]/text()').extract()[0]
        #     item["tags"] = response.xpath('//ul[@class="tags"]/li/a[@class="text"]/text()').extract()
        #     item["referer"] = response.url
        #     pLink = response.xpath('//div[contains(@class,"_layout-thumbnail")]/img/@src').extract()
        #     print(item)
        #     print(pLink)



        # 获取每一页的图片详情页

    def parse2(self, response):
        # 获取画师一共有多少作品
        # 然后算出有多少页
        # 再根据页数，循环遍历
        # 获取了画师本页的作品
        picNums = response.xpath('//span[@class="count-badge"]/text()').extract()[0]
        # 获取总页数
        realNum = round(int(re.sub("\D", "", picNums)) / 20)
        # 如果只有一页,就设定为一页
        if realNum == 0:
            realNum = 1
        print("总作品数:", picNums)
        print("总页数:", realNum + 1)
        for i in range(1, realNum + 1):
            # print(response.url+"&type=all&p="+str(i))
            yield Request(url=response.url + "&type=all&p=" + str(i),
                          # headers=Logedheaders,
                          headers=response.headers,
                          # meta={'cookiejar': response.meta['cookiejar']},
                          callback=self.parse3)

    def parse3(self, response):
        artistPics = response.xpath('//ul[@class="_image-items"]/li/a[1]/@href').extract()
        for each in artistPics:
            # print(each)
            yield Request(url="https://www.pixiv.net" + each,
                          # headers=Logedheaders,
                          headers=response.headers,
                          # meta={'cookiejar': response.meta['cookiejar']},
                          callback=self.parse4)

    def parse4(self, response):

        t_html = response.body.decode('utf-8')
        pid = _asd.get_url_var_div(response.url, "illust_id")
        # print(pid)
        try:
            data = re.findall('"%s":(.*?),"isBookmarkable' % pid, t_html)[0]
            # if not data[-1] == '}':
            data += "}"
            j_data = json.loads(data)
            # print(j_data)
            # print(j_data['url'])
            # print(j_data['illustTitle'])
            # print(j_data['tags'])
            # print(j_data['pageCount'])
            reee = "/img-master/(.*?)_master1200"
            # 获取中间参数部分
            oL = re.compile(reee).findall(j_data['url'])[0]
            pic_num = int(j_data['pageCount'])
            artist = re.findall('"userName":"(.*?)"}', t_html)[0].encode('utf-8').decode('unicode_escape')

            # artist="{'\u0061\u0072\u0074\u0069\u0073\u0074':'"++"'}"
            # print(artist)
            # artist=json.loads(artist)['artist']
            # 因为单图和多图的refer网站不一样,只能分开判断是单图还是多图
            if not pic_num > 1:
                # 单图的情况
                item = PzhanItem()
                item['name'] = j_data['illustTitle']
                item["referer"] = "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=%s" % pid
                item["tags"] = "_".join(j_data['tags'])
                item['p_oLink'] = ("https://i.pximg.net/img-original/" + oL[:-1:] + str(0) + ".jpg")
                item['artist'] = artist
                item['aid'] = j_data['userId']
                item['pid'] = j_data['illustId']
                item['size'] = str(j_data['width']) + "x" + str(j_data['height'])
                # print(item)
                # print(item['artist'])
                # print(item)
                yield item
                pass
            else:
                for i in range(int(j_data['pageCount'])):
                    item = PzhanItem()
                    item['name'] = j_data['illustTitle'] + "_" + str(i)
                    item["referer"] = "https://www.pixiv.net/member_illust.php?mode=manga_big&page=%d&illust_id=%s" % (
                        i, pid)
                    item["tags"] = "_".join(j_data['tags'])
                    item['p_oLink'] = ("https://i.pximg.net/img-original/" + oL[:-1:] + str(i) + ".jpg")
                    item['artist'] = artist
                    item['aid'] = j_data['userId']
                    item['pid'] = j_data['illustId']
                    item['size'] = "plus_images"
                    # print(item)
                    # print(item['artist'])
                    yield item
                    # pass

        except IndexError as ie:
            # print(response.url)
            print('获取作品信息失败')
        except Exception as e:
            # print(response.url)
            # print(data)
            print(e.args)
            # item["name"] = response.xpath('//section[@class="work-info"]/h1[1]/text()').extract()[0]
            # item["size"] = response.xpath('//ul[@class="meta"][1]/li[2]/text()').extract()[0]
            # item["artist"] = response.xpath('//a[@class="user-name"]/text()').extract()[0]
            # item["tags"] = response.xpath('//ul[@class="tags"]/li/a[@class="text"]/text()').extract()
            # item["referer"] = response.url
            # pLink = response.xpath(
            #     '//div[contains(@class,"_layout-thumbnail")]/img/@src').extract()  # 包含_layout-thumbnai类的情况的情况
            # # 有些多张图一起的，会造成pLink为空 ??什么情况?  已解决,为多图时候,div标签的class不同引起的
            # if len(pLink) < 1:  # 为多图的情况
            #     item["pLink"] = response.xpath('//meta[@property="og:image"]/@content').extract()[0]
            #     item["image_urls"] = response.xpath('//meta[@property="og:image"]/@content').extract()[0]
            # else:
            #     item["pLink"] = pLink[0]
            #     item["image_urls"] = pLink[0]
            #
            #     # print(response.url+"已成功爬取,转送管道……")
