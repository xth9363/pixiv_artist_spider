import re

# # ree = '^[a-zA-z][a-zA-Z0-9_]{2,9}$'
# totalCount = re.sub("\D\W", "", '種火集めのブレエリちゃんo(*≥▽≤)ツ')
# print(totalCount)

# pUrl='https://i.pximg.net/img-master/img/2017/01/23/22/24/05/61080401_p0_master1200.jpg'
# reee = "/img-master/(.*?)_master1200"
# oL = re.compile(reee).findall(pUrl)[0]
# print(oL)
#
# float_number="12313.234"
#
# value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
# result = value.match(float_number)
# if result:
#     print(float(float_number))
#
# xx="123.123123ssafd"
# if is_number(xx):
#     print(float(xx))

import json
import re

htmlss = '''
{
token: "8b90f6ce257e44dae58eeec66a6891e7",
isMobile: false,oneSignalAppId: "b2af994d-2a00-40ba-b1fa-684491f6760a",
publicPath: "https:\/\/source.pixiv.net\/www\/js\/spa\/",commonResourcePath: "https:\/\/source.pixiv.net\/common\/",development: false,userData: {id: "5174309",name: "\u5730\u7344\u8a69\u4eba",profileImg: "https:\/\/source.pixiv.net\/common\/images\/no_profile_s.png",premium: false,xRestrict: 2,adult: true,},premium: {},preload: {timestamp: "2018-04-23T11:25:44+09:00",illust: { 68214520: {"illustId":"68214520","illustTitle":"\u2605","illustType":0,"illustComment":"","createDate":"2018-04-13T15:00:18+00:00","uploadDate":"2018-04-13T15:00:18+00:00","restrict":0,"xRestrict":0,"urls":{"mini":"https:\/\/i.pximg.net\/c\/48x48\/img-master\/img\/2018\/04\/14\/00\/00\/18\/68214520_p0_square1200.jpg","small":"https:\/\/i.pximg.net\/c\/540x540_70\/img-master\/img\/2018\/04\/14\/00\/00\/18\/68214520_p0_master1200.jpg","regular":"https:\/\/i.pximg.net\/img-master\/img\/2018\/04\/14\/00\/00\/18\/68214520_p0_master1200.jpg","original":"https:\/\/i.pximg.net\/img-original\/img\/2018\/04\/14\/00\/00\/18\/68214520_p0.png"},"tags":{"authorId":"6996493","isLocked":false,"tags":[{"tag":"\u30aa\u30ea\u30b8\u30ca\u30eb","locked":true,"deletable":false,"userId":"6996493","romaji":"orijinaru","userName":"\u308f\u3044\u3063\u3057\u3085"},{"tag":"\u5973\u306e\u5b50","locked":false,"deletable":true,"romaji":"onnnanoko"}],"writable":true},"storableTags":["RTJMXD26Ak","Lt-oEicbBr"],"userId":"6996493","userIllusts":{"68324034":null,"68309339":null,"68288114":{"illustId":"68288114","illustTitle":"LOL","illustType":0,"xRestrict":0,"url":"https:\/\/i.pximg.net\/c\/240x240\/img-master\/img\/2018\/04\/18\/16\/30\/00\/68288114_p0_master1200.jpg","tags":["VOCALOID","\u521d\u97f3\u30df\u30af","LOL","\u30ed\u30ea\u30dd\u30c3\u30d7(\u30e2\u30b8\u30e5\u30fc\u30eb)","VOCALOID10000users\u5165\u308a"],"userId":"6996493","width":670,"height":942,"pageCount":1,"isBookmarkable":true,"bookmarkData":null},"68214520":{"illustId":"68214520","illustTitle":"\u2605","illustType":0,"xRestrict":0,"url":"https:\/\/i.pximg.net\/c\/240x240\/img-master\/img\/2018\/04\/14\/00\/00\/18\/68214520_p0_master1200.jpg","tags":["\u30aa\u30ea\u30b8\u30ca\u30eb","\u5973\u306e\u5b50"],"userId":"6996493","width":594,"height":1000,"pageCount":6,"isBookmarkable":true,"bookmarkData":null},"68201395":{"illustId":"68201395","illustTitle":"Bride","illustType":0,"xRestrict":0,"url":"https:\/\/i.pximg.net\/c\/240x240\/img-master\/img\/2018\/04\/13\/00\/00\/09\/68201395_p0_master1200.jpg","tags":["Fate\/GrandOrder","\u30bb\u30a4\u30d0\u30fc\u30fb\u30d6\u30e9\u30a4\u30c9","\u5ac1\u30bb\u30a4\u30d0\u30fc","\u30cd\u30ed\u30fb\u30af\u30e9\u30a6\u30c7\u30a3\u30a6\u30b9","Fate\/GO5000users\u5165\u308a"],"userId":"6996493","width":1000,"height":1087,"pageCount":1,"isBookmarkable":true,"bookmarkData":null},"67874621":null,"67874620":null,"67641523":null,"67322753":null,"67269335":null,"67181096":null,"66981073":null,"66807249":null,"66600419":null,"66439339":null,"66375143":null,"66304218":null,"66190869":null,"66151045":null,"65912770":null,"65802121":null,"65646636":null,"65558476":null,"65493127":null,"65493112":null,"65293876":null,"65179751":null,"65179726":null,"64936066":null,"64886310":null,"64706910":null,"64670384":null,"64619515":null,"64619506":null,"64335547":null,"64285588":null,"64265573":null,"64100803":null,"64100802":null,"64042205":null,"63957933":null,"63911847":null,"63852184":null,"63810730":null,"63640977":null,"63485552":null,"63485476":null,"63326061":null,"63069362":null,"63069358":null,"62859195":null,"62743924":null,"62624126":null,"62622496":null,"62565160":null,"62551039":null,"62457185":null,"62451318":null,"62395426":null,"62242652":null,"62119118":null,"62118971":null,"61900842":null,"61823368":null,"61791949":null,"61711043":null,"61674038":null,"61577957":null,"61477714":null,"61369480":null,"61369479":null,"61232882":null,"61231351":null,"61229914":null,"61070509":null,"61070029":null,"61002380":null,"61002379":null,"60960270":null,"60777932":null,"60777891":null,"60697983":null,"60600656":null,"60581780":null,"60514190":null,"60503345":null,"60503005":null,"60384957":null,"60384956":null,"60342186":null,"60181109":null,"60181027":null,"60040975":null,"59842188":null,"59842139":null,"59708509":null,"59688673":null,"59688628":null,"59679440":null,"59652643":null,"59639555":null,"59561984":null,"59513189":null,"59497027":null,"59417201":null,"59410270":null,"59301639":null,"59291925":null,"59158837":null,"59158803":null,"58990171":null,"58990124":null,"58938916":null,"58904237":null,"58828804":null,"58828765":null,"58746422":null,"58665988":null,"58562464":null,"58513310":null,"58462144":null,"58317252":null,"58204812":null,"58196099":null,"58091042":null,"57926538":null,"57881432":null,"57695209":null,"57592236":null,"57559152":null,"57559146":null,"57410885":null,"57362392":null,"57229365":null,"57229257":null,"57156833":null,"57156822":null,"57082832":null,"56949893":null,"56949723":null,"56756558":null,"56756527":null,"56557197":null,"56557179":null,"56375052":null,"56375049":null,"56118001":null,"56037267":null,"55983784":null,"55808865":null,"55728522":null,"55714478":null,"55634094":null,"55526803":null,"55353092":null,"55283034":null,"55134927":null,"55134761":null,"55013127":null,"54951629":null,"54880292":null,"54827555":null,"54821272":null,"54742255":null,"54742169":null,"54675067":null,"54654235":null,"54547151":null,"54547141":null,"54514501":null,"54280460":null,"54242979":null,"54161896":null,"54025580":null,"54010113":null,"53895687":null,"53832959":null,"53783148":null,"53732389":null,"53732316":null,"53679751":null,"53596537":null,"53496302":null,"53496279":null,"53395297":null,"53383315":null,"53344470":null,"53280732":null,"53261328":null,"53214360":null,"53113485":null,"53113467":null,"53017490":null,"52944451":null,"52937521":null,"52882869":null,"52882860":null,"52790383":null,"52790370":null,"52704612":null,"52653071":null,"52653053":null,"52585962":null,"52580486":null,"52580481":null,"52526606":null,"52519412":null,"52495230":null,"52486676":null,"52373857":null,"52289922":null,"52241977":null,"52145825":null,"52145539":null,"52046940":null,"52006756":null,"51884612":null,"51869682":null,"51851530":null,"51791011":null,"51766265":null,"51762744":null,"51629939":null,"51629895":null,"51585847":null,"51468775":null,"51468310":null,"51359918":null,"51273780":null,"51259674":null,"51118503":null,"51090866":null,"51013577":null,"50968697":null,"50906430":null,"50892619":null,"50856328":null,"50842087":null,"50771931":null,"50765220":null,"50680378":null,"50592577":null,"50549190":null,"50508908":null,"50486735":null,"50391953":null,"50227705":null,"50169473":null,"50056468":null,"50035793":null,"50019810":null,"50008626":null,"49963495":null,"49919661":null,"49766586":null,"49766534":null,"49536766":null,"49251299":null,"49171421":null,"48856765":null,"48823580":null,"48659359":null,"48643048":null,"48257254":null,"48016942":null,"47966627":null,"47807076":null,"47771288":null,"47699525":null,"47661941":null,"47648479":null,"47623162":null,"47572575":null,"47473623":null,"46985456":null,"46948986":null,"46923382":null,"46884332":null,"46873832":null,"46825404":null,"46010964":null,"45988239":null,"45690152":null,"45509455":null,"45140891":null,"44993580":null,"44855667":null,"44160230":null,"44121791":null,"44075287":null,"44040391":null,"43992847":null,"43985320":null,"43909158":null,"43867974":null,"43756849":null,"43719296":null,"43706109":null,"43685568":null,"43680506":null,"43641560":null,"43634994":null,"43629623":null,"43539313":null,"43501420":null,"43499737":null,"43433633":null,"43390114":null,"43384470":null,"43332164":null,"43282957":null,"43240650":null,"43240136":null,"43201197":null,"43196587":null,"43126958":null,"43122806":null,"43103686":null,"43025309":null,"43017783":null,"42968919":null,"42902512":null,"42840217":null,"42807742":null,"42753239":null,"42702619":null,"42660010":null,"42591266":null,"42569528":null,"42478118":null,"42426770":null,"42419778":null,"42110912":null,"42082195":null,"42026877":null,"42009279":null,"41321591":null,"41026738":null},"likeData":false,"width":594,"height":1000,"pageCount":6,"bookmarkCount":11622,"likeCount":10530,"commentCount":69,"responseCount":0,"stampCount":[{"id":303,"count":7},{"id":302,"count":7},{"id":304,"count":5},{"id":202,"count":3},{"id":407,"count":2},{"id":203,"count":2},{"id":406,"count":2},{"id":204,"count":1},{"id":105,"count":1},{"id":207,"count":1}],"viewCount":84491,"isHowto":false,"isOriginal":true,"imageResponseOutData":[],"imageResponseData":[],"imageResponseCount":0,"pollData":null,"seriesNavData":null,"descriptionBoothId":null,"comicPromotion":null,"contestBanners":[],"factoryGoods":{"integratable":false,"integrated":false},"isBookmarkable":true,"bookmarkData":null} },user: { 6996493: {"userId":"6996493","name":"Lpip","image":"https:\/\/i.pximg.net\/user-profile\/img\/2018\/01\/24\/21\/39\/05\/13734740_04fc12dff317d369693b05814cde32d9_50.png","premium":true,"isFollowed":true,"background":{"color":"EDF0F5","extra":{"user_account":"lpmya","user_bg_user_id":"6996493","user_bg_color":"EDF0F5","user_bg_useimg":"0","user_bg_repeat":"","user_bg_fixed":"0","user_bg_filename":"","user_bg_ext":""}}} },},mute: [],}
'''
# htmlss = '''
# {"illustId":"53895687","illustTitle":"\u25cc\u0b82","illustType":0,"xRestrict":0,"url":"https:\/\/i.pximg.net\/c\/240x240\/img-master\/img\/2015\/12\/05\/21\/08\/43\/53895687_p0_master1200.jpg","tags":["
# VOCALOID","\u521d\u97f3\u30df\u30af","\u6d99\u30df\u30af","\u4f53\u80b2\u5ea7\u308a","VOCALOID10000users\u5165\u308a"],"userId":"6996493","width":800,"height":963,"pageCount":1,"isBookmarkable":true,"boo
# kmarkData":{"id":"2401902137","private":false}
#
# '''
# json_arr_str = """[{ "name": "cxh", "sex": "1","website":"http://www.bejson.com" },{ "name": "我的", "sex": "1","website":"http://www.bejson.com" }]"""

try:
    # data = re.findall('"68214520":(.*?)},', htmlss)[0]
    data = re.findall('"%s":(.*?),"isBookmarkable' % "68214520", htmlss)[0]
    userName = re.findall('"userName":"(.*?)"}', htmlss)
    print(userName)

    # data = htmlss
    j_data = json.loads(data+"}")
    print(j_data)
    reg = r'.+/(\d+)_p'
    pid = re.findall(reg, j_data['url'])[0]
    print(pid)
    reee = "/img-master/(.*?)_master1200"
    oL = re.compile(reee).findall(j_data['url'])[0]
    print(oL)
    result = ("https://i.pximg.net/img-original/" + oL[:-1:] + str(5) + ".jpg")
    print(result)

    artist = re.findall('"userName":"(.*?)"}', htmlss)[0]
    print(type(artist))
except IndexError as ie:
    print('获取作品信息失败')
except Exception as e:
    print(e.args)

# def businesshours(value):
#     try:
#         return 9 <= value < 17
#     except AttributeError:
#         return ''
#
#
# print(businesshours(8))
