# -*- coding: utf-8 -*-

import re
from operator import truediv
from Request_and_Soup import request_then_soup


def calculate_price_per_guest(full_wish_url, dic):

    soup_wish = request_then_soup(full_wish_url, dic)
    price_wish = str(soup_wish.findAll('span', {'data-pricerate': 'true'})).encode('utf-8')  # price of each host in wish list
    wish_data = (re.compile(r'\"\d*\"\>\d*(?=\<\/span\>)')).findall(price_wish)
    guest_wish = str(soup_wish.findAll('span', {'class': 'detailWithoutWrap_basc2l'})).decode('unicode_escape').encode(
        'utf-8')
    guest_data = (re.compile(r'\"\d*\"\>\d*(?=位房客)')).findall(guest_wish)

    data_guest = []
    data_wish = []
    for i in range(len(wish_data)):
        id_guest_i = int(re.search(r'\"(\d+)*\"', guest_data[i]).group(1))
        guest_i = int(re.search(r'\>(\d+)', guest_data[i]).group(1))
        data_guest.append([id_guest_i, guest_i])
        id_wish_i = int(re.search(r'\"(\d+)*\"', wish_data[i]).group(1))
        wish_i = int(re.search(r'\>(\d+)', wish_data[i]).group(1))
        data_wish.append([id_wish_i, wish_i])

    # print('data_guest: ' + str(data_guest))
    # print('data_wish: ' + str(data_wish))
    data_guest.sort()
    data_wish.sort()
    final_data_guest = []
    final_wish_guest = []
    for i in range(len(wish_data)): final_data_guest.append(data_guest[i][1])
    for i in range(len(wish_data)): final_wish_guest.append(data_wish[i][1])
    # print('final_data_guest: ' + str(final_data_guest))
    # print('final_wish_guest: ' + str(final_wish_guest))

    price_per_guest = map(truediv, final_wish_guest,
                          final_data_guest)  # TODO: Maybe can be faster in other ways: http://stackoverflow.com/questions/1975250/when-should-i-use-a-map-instead-of-a-for-loop
    # print('price_per_guest: ' + str(price_per_guest))
    # print 'price_wish: '
    # print price_wish  # Example: [<span data-pricerate="true" data-reactid="67">262</span>, <span data-pricerate="true" data-reactid="156">637</span>, <span data-pricerate="true" data-reactid="209">361</span>]
    # print 'guest_wish: '
    # print guest_wish
    # print guest_data

    return price_per_guest
