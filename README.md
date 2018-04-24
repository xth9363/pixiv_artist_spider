# pixiv_artist_spider
* 使用Scrapy框架
* 针对P站新的UI写的爬虫,可以爬取指定用户的所有作品,暂时只能爬jpg和png
* 爬取的图片都是原图画质

# 使用方法
* python环境和scrapy等必要前置都应该已经正确安装
* 修改new_art.py 中 把artis_id的值改成想要爬取的画师的ID
* 修改new_art.py 中 把login_account的值改成可用的P站账号
* 修改new_art.py 中 把login_pwd的值改成该账号的密码
* 终端中执行 scrapy crawl new_art 即可

# 需要填写一个可用的P站账号密码
* 用于模拟登录
* 因为P站要求登录用户才能看到所有其他用户的作品

# 无法直接访问P站的情况
* 需要修改HOST文件
* 或者如果路由器允许,可以直接设置路由器的HOST
* HOST内容已经在项目中名为p_host.txt
* 不建议没有任何了解的朋友修改HOST

# 请限制爬取速度
* 本爬虫的编写不是为了爬取整站,只用于更方便的获取喜欢的画师的所有公开作品
* 不排除因爬取过快账号甚至IP被封禁的可能性
* 按照默认设置未被封号或者封IP

# 运行部分截图
!['p1'](https://raw.githubusercontent.com/xth9363/pixiv_artist_spider/master/Pzhan/images/33.png)

!['p2'](https://raw.githubusercontent.com/xth9363/pixiv_artist_spider/master/Pzhan/images/22.png)


!['p3'](https://raw.githubusercontent.com/xth9363/pixiv_artist_spider/master/Pzhan/images/11.png)
