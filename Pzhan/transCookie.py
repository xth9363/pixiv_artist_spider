# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


if __name__ == "__main__":
    cookie = 'p_ab_id=3; p_ab_id_2=5; _ga=GA1.2.1272705403.1503209995; login_ever=yes; c_type=24; a_type=0; b_type=1; PHPSESSID=5174309_b5904bfb6a58f986aa74fca877e342d1; module_orders_mypage=[{"name":"recommended_illusts","visible":true},{"name":"everyone_new_illusts","visible":true},{"name":"following_new_illusts","visible":true},{"name":"mypixiv_new_illusts","visible":true},{"name":"fanbox","visible":true},{"name":"featured_tags","visible":true},{"name":"contests","visible":true},{"name":"user_events","visible":true},{"name":"sensei_courses","visible":true},{"name":"spotlight","visible":true},{"name":"booth_follow_items","visible":true}]; is_sensei_service_user=1; __utmt=1; __utma=235335808.1272705403.1503209995.1510301044.1510753240.12; __utmb=235335808.2.9.1510753240; __utmc=235335808; __utmz=235335808.1510753240.12.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmcct=/link; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=5174309=1^9=p_ab_id=3=1^10=p_ab_id_2=5=1^11=lang=zh=1; _td=61db3ab3-fb5f-43f2-a585-a7aa18997f9c'
    trans = transCookie(cookie)
    print(trans.stringToDict())
