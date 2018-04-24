# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import re
import urllib
import urllib.request
import os
import re
import socket
from scrapy.pipelines.images import ImagesPipeline
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy import log


# 主要在用的
def get_referer(url):
    reference = "http://www.pixiv.net/member_illust.php?mode=manga_big&illust_id="
    reg = r'.+/(\d+)_p0'
    return reference + re.findall(reg, url)[0] + "&page=0"


def mk_dir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path + ' 目录已存在')
        return False


def validate_title(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title


class PzhanPipeline(object):
    # 本地的保存目录
    LOCAL_PATH = 'D:\\PzhanResult\\artist\\'

    def artDownLoadPic(self, url, name, size, artist, referer, pid, tags):
        path = self.LOCAL_PATH + artist + '\\'
        mk_dir(path)
        path = path.replace('\\', '/')
        self.downLoadPic(url=url, name=name, size=size, artist=artist, referer=referer, pid=pid, path=path, tags=tags)

    def downLoadPic(self, url, name, size, artist, referer, pid, path, tags):
        # print("准备下载的图片地址：" + url)
        # filename="D:/spiderResultPzhan/"+pid+"__"+name+"__"+artist+"__"+size+".jpg"
        filename = path + pid + "__" + name + "__" + artist + "__" + size + '__' + tags + ".jpg"

        # filename = "D:/spiderResultPzhan/" + pid + "___" + size + ".jpg"
        headers = {"Connection": "keep-alive",
                   "User-Agent": "Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4",
                   'Referer': referer}

        try:
            url1 = url
            req = urllib.request.Request(url1, None, headers)
            res = urllib.request.urlopen(req)
            # print(res.code)
            # rstream = res.read()
            # res.close()
            # with open("%s.jpg" % name, "wb") as f:
            #     f.write(res.read())
        except urllib.error.HTTPError:
            # print("出错.转换")
            url2 = url.replace('.jpg', '.png')
            filename = filename.replace('.jpg', '.png')

            req = urllib.request.Request(url2, None, headers)
            res = urllib.request.urlopen(req)
            # print("png:", res.code)
        except Exception as e:
            print("请求时出错")
            print(e.args)
            # rstream = res.read()
            # res.close()
            # with open("%s.jpg" % name, "wb") as f:
            #     f.write(res.read())
        # 写到本地
        # with as 的写法
        if not os.path.exists(filename):
            # print(res.read())
            try:
                with open(filename, "wb") as f:
                    f.write(res.read())
                    print(filename)
                    # pass
            except Exception as e:
                print("下载时出错",filename)

                print(e.args)
                # 普通的写法
                # f = open(filename, 'wb')
                # f.write(rstream)
                # f.close()

    def process_item(self, item, spider):

        fname = validate_title(item["name"]).strip()
        fartist = validate_title(item["artist"]).strip()
        tags = validate_title(item["tags"]).strip()
        if fname == '':  # 如果全都是非法字符构成的
            fname = item["pid"]  # 就用ID代替名字吧
        if fartist == '':  # 同上
            fartist = item["aid"]  # 就用ID代替名字吧
        pool = ThreadPoolExecutor(5)
        pool.submit(self.artDownLoadPic, url=item['p_oLink'], name=fname, size=item["size"], artist=fartist,
                    referer=item["referer"], pid=item["pid"], tags=tags)
        # self.artDownLoadPic(url=oLinks[i], name=fname + str(i + 1), size=trueSize, artist=fartist,
        #                     referer=item["referer"], pid=pid, tags=tags)

        return item

# scrapy 自带的,暂时可不用的
# class PzhanImgPipeline(ImagesPipeline):
#     ARTIST = ''
#
#     def validateTitle(self, title, replace=None):
#         # rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
#         # new_title = re.sub(rstr, "_", title)  # 替换为下划线
#         new_title = re.sub("\D\W", "", title)
#         if new_title.strip() == '':  # 如果全都是非法字符构成的
#             new_title = replace  # 就用ID代替名字吧
#         return new_title
#
#     def get_media_requests(self, item, info):
#         oLinks = []
#         image_url = item['image_urls']
#         referer = item['referer']
#         pUrl = item["pLink"]
#         reee = "/img-master/(.*?)_master1200"
#         oL = re.compile(reee).findall(pUrl)[0]
#         self.ARTIST = self.validateTitle(item['artist'])
#         headers = {"Connection": "keep-alive",
#                    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) \AppleWebKit/537.36 (KHTML, like Gecko)Chrome/55.0.2883.87 Safari/537.36",
#                    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 \
#                    (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4",
#                    'Referer': referer}
#
#         if "P" in item["size"]:
#             # print("多张投稿")
#             rea = "一次性投稿多张作品 (.*?)P"
#             picNum = re.compile(rea).findall(item["size"])[0]
#             for i in range(0, int(picNum)):
#                 oLinks.append("https://i.pximg.net/img-original/" + oL[:-1:] + str(i) + ".jpg")
#                 # yield Request(oLink, headers=headers)
#         else:
#
#             oLinks.append("https://i.pximg.net/img-original/" + oL + ".jpg")
#             # yield Request(row_img, headers=headers)
#         for links in oLinks:
#             try:
#                 print(links)
#                 yield Request(links, headers=headers)
#             except Exception as e:
#                 url2 = links.replace('.jpg', '.png')
#                 # print("JPG不存在,尝试PNG", )
#                 yield Request(url2, headers=headers)
#
#     def file_path(self, request, response=None, info=None):
#         image_guid = request.url.split('/')[-1]
#         filename = self.validateTitle(image_guid)
#         return '%s/%s' % (self.ARTIST, filename)
#
#     def item_completed(self, results, item, info):
#         # print(results)
#         image_paths = [x['path'] for ok, x in results if ok]
#         if not image_paths:
#             raise DropItem("Item contains no images")
#         item['image_paths'] = image_paths
#         return item
