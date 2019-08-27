# Airbnb-crawler<br> (last update on Mar 24, 2017)
**中文版 Readme 见后半部分**<br>A web crawler that can collect users data on Airbnb.
- - -

## Attention
* This crawler is originally used for collecting data for academic purposes. To avoid unnecessary burden on the Airbnb server, please do not abuse this crawler. You can find tons of Airbnb data at [Inside Airbnb](http://insideairbnb.com/), which may meet your needs.

* This project is developed with Python 2.7.12:

## What is it?
This is a multiprocessing Python web crawler using `requests` and `bs4` packages. With input data of user ID, it collects data of each user including:
* Date of signing up
* Number of wish lists
* URLs of wish lists
* Number of host reviews
* URLs of hosts' page
* Average price in each wish list

And the output will be written into a text file (`output.txt`).

## A glimpse into data
The input dataset (has been organized into table from .csv file) is as following:
<div style="white-space:nowrap" border="1" align=center>
	<table>
		<thead>
			<tr>
				<th>listing_id</th>
				<th>id</th>
				<th>reviewer_id</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>7369</td>
				<td>3721</td>
				<td>20217</td>
			</tr>
			<tr>
				<td>7369</td>
				<td>4700</td>
				<td>21786</td>
			</tr>
			<tr>
				<td>10385</td>
				<td>12159</td>
				<td>38278</td>
			</tr>
		</tbody>
	</table>
</div>

where `listing_id` is ID of Airbnb homestay, `id` is ID of observations in dataset, `reviewer_id` is ID of reviewers who has been in corresponding homestay.

Next is output dataset (has been organized into table from text file):

<div style="overflow:auto;overflow-y:hidden;white-space:nowrap" border="1" align=center>
	<table>
		<thead>
			<tr>
				<th>id</th>
				<th>reviewer_id</th>
				<th>sign_in_date</th>
				<th>sign_in_date</th>
				<th>wishlists_and_reviews</th>
				<th>wishlists_url</th>
				<th>average_price_each_wishlists</th>
				<th>wishlists_average_price</th>
				<th>hosts_url</th>
				<th>check</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>12361</td>
				<td>36408</td>
				<td>2009年9月</td>
				<td>2009年9月</td>
				<td>['1', '', '1', '']</td>
				<td>['/wishlists/183497057']</td>
				<td>[149.0, 105.42857142857143, 73.33333333333333, 127.75, 104.5, 83.25, 92.25]</td>
				<td>105.073129252</td>
				<td>['/users/show/36408']</td>
				<td>Finished</td>
			</tr>
			<tr>
				<td>16174</td>
				<td>50201</td>
				<td>2009年10月</td>
				<td>2009年10月</td>
				<td>['3', '', '3', '']</td>
				<td>['/wishlists/127123772', '/wishlists/172508908', '/wishlists/172508912']</td>
				<td>[496.5, 620.5, 620.5]</td>
				<td>579.166666667</td>
				<td>['/users/show/236228', '/users/show/35749', '/users/show/35749']</td>
				<td>Finished</td>
			</tr>
			<tr>
				<td>58458</td>
				<td>136698</td>
				<td>2010年6月</td>
				<td>2010年6月</td>
				<td>['1', '', '4', '']</td>
				<td>['/wishlists/161291543']</td>
				<td>[223.5, 160.2, 125.33333333333333]</td>
				<td>169.677777778</td>
				<td>['/users/show/76161100', '/users/show/6661557', '/users/show/165119', '/users/show/19425']</td>
				<td>Finished</td>
			</tr>
		</tbody>
	</table>
</div>

## How it works?

This web crawler firstly open a user's Airbnb page via his/her ID (`reviewer_id` in input dataset). Then it collects the data on his/her page, including variables noted in output dataset above.

What each Python file does:
* `Run_with_pool.py`: Read unfinished task in *input.csv*, establish IP pool, control multiprocessing web crawling tasks (`Control.py`) and write results into *output.txt*.
* `Control.py`: Crawl data in each page and write them to a list.
* `meancut.py`: Divide IP pool to equal parts.
* `Request_and_Soup.py`: Request and parse HTML page.
* `Calculate.py`: Calculate average price of each wish list.

**Please note that the speed of crawling mainly depends on the quality of your IP pool, your network speed and anti-scraping strategy of Airbnb.**

## Contact me

gaofangshu@foxmail.com

* * *

# Airbnb-crawler

收集 Airbnb 用户数据的网络爬虫。

## 注意

* 本爬虫起初用于学术数据采集目的，请不要滥用以免对 Airbnb 服务器造成不必要负担。[Inside Airbnb](http://insideairbnb.com/) 有海量Airbnb数据，也许能满足你的需求。

* 本爬虫的开发环境为 Python 2.7.12：

## 功能介绍
这是一个基于 `requests` 和 `bs4` 包的 Python 多进程爬虫。读取用户 ID，它可以爬取以下用户数据：
* 注册日期
* 心愿单个数
* 心愿单网址
* 房东评论个数
* 房东主页网址
* 每个心愿单的房源均价

以上数据均被写入文本文档中（`output.txt`）。

## 数据预览
输入的数据集（已从csv文件整理为表格）如下：
<div style="white-space:nowrap" border="1" align=center>
	<table>
		<thead>
			<tr>
				<th>listing_id</th>
				<th>id</th>
				<th>reviewer_id</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>7369</td>
				<td>3721</td>
				<td>20217</td>
			</tr>
			<tr>
				<td>7369</td>
				<td>4700</td>
				<td>21786</td>
			</tr>
			<tr>
				<td>10385</td>
				<td>12159</td>
				<td>38278</td>
			</tr>
		</tbody>
	</table>
</div>

其中 `listing_id` 每个 Airbnb 房源的 ID，`id` 是数据集每个观测值的ID，`reviewer_id` 是在对应房源上评论的用户的ID。

接下来是输出数据集（已从txt文件整理为表格）：

<div style="overflow:auto;overflow-y:hidden;white-space:nowrap" border="1" align=center>
	<table>
		<thead>
			<tr>
				<th>id</th>
				<th>reviewer_id</th>
				<th>sign_in_date</th>
				<th>sign_in_date</th>
				<th>wishlists_and_reviews</th>
				<th>wishlists_url</th>
				<th>average_price_each_wishlists</th>
				<th>wishlists_average_price</th>
				<th>hosts_url</th>
				<th>check</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>12361</td>
				<td>36408</td>
				<td>2009年9月</td>
				<td>2009年9月</td>
				<td>['1', '', '1', '']</td>
				<td>['/wishlists/183497057']</td>
				<td>[149.0, 105.42857142857143, 73.33333333333333, 127.75, 104.5, 83.25, 92.25]</td>
				<td>105.073129252</td>
				<td>['/users/show/36408']</td>
				<td>Finished</td>
			</tr>
			<tr>
				<td>16174</td>
				<td>50201</td>
				<td>2009年10月</td>
				<td>2009年10月</td>
				<td>['3', '', '3', '']</td>
				<td>['/wishlists/127123772', '/wishlists/172508908', '/wishlists/172508912']</td>
				<td>[496.5, 620.5, 620.5]</td>
				<td>579.166666667</td>
				<td>['/users/show/236228', '/users/show/35749', '/users/show/35749']</td>
				<td>Finished</td>
			</tr>
			<tr>
				<td>58458</td>
				<td>136698</td>
				<td>2010年6月</td>
				<td>2010年6月</td>
				<td>['1', '', '4', '']</td>
				<td>['/wishlists/161291543']</td>
				<td>[223.5, 160.2, 125.33333333333333]</td>
				<td>169.677777778</td>
				<td>['/users/show/76161100', '/users/show/6661557', '/users/show/165119', '/users/show/19425']</td>
				<td>Finished</td>
			</tr>
		</tbody>
	</table>
</div>

## 运行原理

本爬虫首先根据用户 ID（输入数据集里的 `reviewer_id`）打开每个用户的主页，然后爬取主页上的数据，即输出数据集所展示的那些变量。

以下是每个 Python 文件的功能：
* `Run_with_pool.py`: 读取 *input.csv* 中未完成的任务、建立 IP 池、控制多进程爬虫任务（`Control.py`）、将结果写入 *output.txt*。
* `Control.py`: 爬取每一页面的数据，并将它们写入一个 list 中。
* `meancut.py`: 平均分割 IP 池。
* `Request_and_Soup.py`: 请求并解析 HTML 页面。
* `Calculate.py`: 计算每个心愿单的房源均价。

**注意，本爬虫的爬取速度取决于 IP 池的质量、网络速度以及 Airbnb 的反爬虫策略。**

## 联系作者

gaofangshu@foxmail.com
