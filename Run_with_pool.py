# -*- coding: utf-8 -*-

import re
from multiprocessing import Pool, Queue, Process, Manager
from Control import control_spider
from time import sleep
from meancut import meancut
import requests
import datetime


def main(nameList):
    countm = 0
    manager = Manager()
    q = manager.Queue()
    while 1:
        np = 30
        pool = Pool(processes=np)

        while 1:
            try:
                url0 = 'http://tpv.daxiangdaili.com/ip/'
                payload = {'tid': '557064921442104',
                           'num': '50000',
                           'protocol': 'https',
                           'longlife': '1',
                           'foreign': 'none'}
                r = requests.get(url0, params=payload)
                p = re.compile('[\r\n]')
                listip = p.split(r.text)
                listip = [x.encode('utf-8') for x in listip if x != '']

                ipList = meancut(listip, np)
                break
            except:
                sleep(10)
                continue

        for obs in range(np):
            # print nameList
            try:
                iplist = ipList[obs]
                # print nameList[countm * 2 + obs]
                pool.apply_async(control_spider, args=(q, nameList[countm * np + obs], iplist,))
                sleep(0.1)
            except:
                pass
        countm += 1
        begin = datetime.datetime.now()
        begin.strftime('%Y-%m-%d %H:%M:%S')
        print str(begin) + " now: " + str(countm) + " loop at: " + str(countm * np + obs) + " End point: " + str(
            len(nameList)) + " ***********************************"
        if len(nameList) < (countm * np):
            break
        # print('Pool ' + str(countm) + ' Start')
        pool.close()
        pool.join()
        # print('Pool ' + str(countm) + ' End')
        write(q)


def write(q):
    fw = open('output.txt', 'a+')
    countw = 0
    while not q.empty():
        try:
            value = q.get()
            for element in value:
                fw.write(element)
            countw += 1
            print(str(countw) + " observations have been written\n")
        except:
            print(str(countw) + " observations written failed\n")
            break


if __name__ == '__main__':

    # ###############################################################################################
    # read reviewer_id in .csv file, save dic{id: reviewer_id} and list[reviewer_id]
    p = re.compile('[^\t]+[\t|\n]')
    fr = open('input.csv', 'r')
    count = 0
    name_list = []
    f_dic = {}
    while 1:
        count += 1
        line = fr.readline()
        if count == 1:  # skip the header
            continue
        if line:
            listA = p.findall(line)
            listA = [i[:-1] for i in listA]  # delete \t or \n at the end
            id_D_reviewer_id = listA[1] + "$" + listA[2]  # save as id$reviewer_id
            name_list.append(id_D_reviewer_id)
            f_dic[listA[1]] = listA[2]
        else:
            break
    fr.close()

    sum = 0
    fo = open('output.txt', 'r')
    while 1:
        line = fo.readline()
        if line:
            listB = p.findall(line)
            listB = [i[:-1] for i in listB]
            if f_dic.has_key(listB[0]):  # check whether "id" is in f_dic, if yes,
                name_list.remove(
                    (listB[0] + "$" + listB[1]))  # delete corresponding key in f_dic and reviewer_id in name_list.
                del f_dic[listB[0]]
                sum += 1
        else:
            break
    print("Finished " + str(sum) + " \'reviewer_id\'s")
    fo.close()

    # ###############################################################################################

    # print name_list
    main(name_list)
