# -*- coding: utf-8 -*-

import re
from time import sleep, time
from Calculate import calculate_price_per_guest
from Request_and_Soup import request_then_soup


def control_spider(q, id_d_reviewer_id, iplist):
    current_list = []

    p = re.compile(r'(\d*)\$(\d*)')
    id = p.search(id_d_reviewer_id).group(1)
    reviewer_id = p.search(id_d_reviewer_id).group(2)

    # write current id and reviewer_id in output file
    current_list.append(id + '\t')
    current_list.append(reviewer_id + '\t')

    ticksA = time()
    countip = 0
    while 1:
        ip = iplist[0]
        del iplist[0]
        countip += 1
        try:
            # print "*********listip\n"+ ip
            # print {'http': ip, 'https': ip}
            # print("Trying ip(" + str(countip) + "):" + ip)

            try:
                dic = {'http': ip, 'https': ip}
                url = 'https://zh.airbnb.com/users/show/' + reviewer_id
                soup = request_then_soup(url, dic)
                # get users sign-up time
                re_sign_time = re.compile(r'注册时间：(.*)')
                data_sign_time = re_sign_time.search(str(soup)).group(1).decode('string_escape')
                print("Success at " + ip)
                # write users sign-up time
                # except:
                #     current_list.append('\t')
                #     print 'Failed @ write users sign-up time'
                #     pass
                break
            except:
                continue

        except Exception, e:
            print Exception, ":", e
            ticksB = time.time()
            if ticksB - ticksA > 90:
                break
            if len(iplist) == 0:
                print("All ip have been used")
                break

    current_list.append(str(data_sign_time) + '\t')


    # get users sign-up time
    try:
        re_sign_time = re.compile(r'注册时间：(.*)')
        data_sign_time = re_sign_time.search(str(soup)).group(1).decode('string_escape')
        current_list.append(str(data_sign_time) + '\t')  # write users sign-up time
    # except:
    #     current_list.append('\t')
    #     print 'Failed @ write users sign-up time'
    #     pass
    except Exception, e:
        print Exception, ":", e

    # get number of wish lists and host reviews, maybe contain guest reviews
    try:
        mydivs = soup.findAll('div', {'class': 'social_connections_and_reviews'})
        re_wish_and_review = re.compile(r'\d*(?=\)<\/small>)')
        data_wish_and_review = re_wish_and_review.findall(str(mydivs))
        current_list.append(str(data_wish_and_review) + '\t')  # write number of wish lists and host reviews
    except:  # TODO: improve output by re
        current_list.append('Error\t')
        # f.write('\t')
        print 'Failed @ write number of wish lists and host reviews'
        pass

    # get wish list url List TODO: only get 3 urls for now, others are hidden in html
    try:
        re_wish_url = re.compile('\/wishlists\/\d*')
        wish_url = re_wish_url.findall(str(soup.findAll(href=re_wish_url)))
        # Example: ['/wishlists/179659793', '/wishlists/182048270', '/wishlists/182235459']
        current_list.append(str(wish_url) + '\t')  # write wish list url
    except:
        current_list.append('Error\t')
        print 'Failed @ write wish list url'
        pass

    # calculate mean price in wish lists, CNY/person, currency depends on your country
    # try:
    if wish_url:

        price_per_guest = []
        for suburl_wish in wish_url:
            # sleep(0.5)
            full_wish_url = 'https://zh.airbnb.com' + suburl_wish
            price_per_guest.extend(calculate_price_per_guest(full_wish_url, dic))
        wishlist_price_per_guest = sum(price_per_guest) / len(price_per_guest)
        current_list.append(str(price_per_guest) + '\t')  # write mean price for each wish lists
        current_list.append(str(wishlist_price_per_guest) + '\t')  # write mean price in wish lists
        ipf = open('ipf.txt', 'a+')
        ipf.write(ip + '\n')
        ipf.close()
    else:
        current_list.append('\t')
        current_list.append('\t')
        pass
    # except:
    #     current_list.append('Error\t')
    #     current_list.append('Error\t')
    #     print 'Failed @ calculate mean price in wish lists'
    #     print Exception, ":", e
    #     pass
    # except Exception, e:
    #     print Exception, ":", e
    #     print 'Failed @ calculate mean price in wish lists'
    #     current_list.append('Error\t')
    #     current_list.append('Error\t')
    #     pass

    # url List of hosts who reviewed on this guest page TODO: only get 10 urls for now, others are hidden in html
    try:
        re_hostreview_url = re.compile('\/users\/show\/\d*')
        hostreview_url = re_hostreview_url.findall(
            str(soup.findAll('div', {'class': 'avatar-wrapper'})))  # url List of hosts who reviewed on this guest page
        # ['/users/show/60594796', '/users/show/102996772', '/users/show/822444', '/users/show/87357']
        current_list.append(str(hostreview_url) + '\tFinished\n')  # write the url List
    except:
        current_list.append('\tFinished\n')
        print 'Failed @ url List of hosts who reviewed on this guest page'
        pass

    q.put(current_list)
    print 'Put reviewer_id ' + str(id_d_reviewer_id) + ' to queue'
