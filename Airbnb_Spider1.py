# -*- coding: utf-8 -*-

import csv
import re
from Calculate import calculate_price_per_guest
from Request_and_Soup import request_then_soup

def download(mydict, data_list, outfile):
    count = 0
    for key, value in mydict.iteritems():
        url = 'https://zh.airbnb.com/users/show/' + value
        # print 'url: '
        # print url

        soup = request_then_soup(url)

        # 爬取注册时间
        try:
            re_sign_time = re.compile(r'注册时间：(.*)')
            data_sign_time = re_sign_time.search(str(soup)).group(1).decode('string_escape')
            # print 'data_sign_time: '
            # print data_sign_time
            data_list[int(key)+1][4] = data_sign_time  # 输出注册时间
            # print 'data_list: '
            # print data_list
        except:
            print '失败 @ 爬取注册时间'
            pass

        # 爬取心愿单数及房东评论数，有可能还有房客评论数
        try:
            mydivs = soup.findAll('div', {'class': 'social_connections_and_reviews'})
            # print 'mydivs: '
            # print mydivs
            re_wish_and_review = re.compile(r'\d*(?=\)<\/small>)')
            data_wish_and_review = re_wish_and_review.findall(str(mydivs))
            data_list[int(key)+1][5] = data_wish_and_review  # 输出心愿单数及房东评论数，有可能还有房客评论数 TODO: 正则表达式优化格式
        except:
            print '失败 @ 爬取心愿单数及房东评论数'
            pass

        # 形成心愿单链接List TODO: 目前只能爬取前3个心愿单，之后的心愿单被隐藏了
        try:
            re_wish_url = re.compile('\/wishlists\/\d*')
            wish_url = re_wish_url.findall(str(soup.findAll(href=re_wish_url)))  # 心愿单链接
            # print 'wish_url: '
            # print wish_url  # Example: ['/wishlists/179659793', '/wishlists/182048270', '/wishlists/182235459']
            data_list[int(key)+1][6] = str(wish_url)
        except:
            print '失败 @ 形成心愿单链接List'
            pass

        # 计算心愿单内房源的均价，价格/人，注意货币单位
        try:
            if wish_url:

                price_per_guest = []
                for suburl_wish in wish_url:
                    full_wish_url = 'https://zh.airbnb.com' + suburl_wish
                    price_per_guest.extend(calculate_price_per_guest(full_wish_url))
                    # print 'price_per_guest: '
                    # print price_per_guest
                wishlist_price_per_guest = sum(price_per_guest)/len(price_per_guest)
                # print int(key)
                data_list[int(key)+1][7] = str(price_per_guest)
                data_list[int(key)+1][8] = wishlist_price_per_guest

            else:
                pass
        except:
            print '失败 @ 计算心愿单内房源的均价'
            pass

        # 房东评价的房东资料主页List TODO: 目前只能爬取前10个心愿单，之后的房东链接被隐藏了
        try:
            re_hostreview_url = re.compile('\/users\/show\/\d*')
            hostreview_url = re_hostreview_url.findall(
                str(soup.findAll('div', {'class': 'avatar-wrapper'})))  # 房东评价的房东资料主页
            # print 'hostreview_url: '
            # print hostreview_url  # ['/users/show/60594796', '/users/show/102996772', '/users/show/822444', '/users/show/87357']
            data_list[int(key)+1][9] = str(hostreview_url)
        except:
            print '失败 @ 房东评价的房东资料主页List'
            pass
        count += 1
        print('已完成' + str(count) + '条数据，ID = ' + data_list[int(key)+1][1] )

    csv_writer = csv.writer(outfile)
    csv_writer.writerows(data_list)
    outfile.close()

