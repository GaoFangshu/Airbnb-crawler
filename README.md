# Airbnb-crawler
***中文版 Readme 见后半部分***
A web crawler that can collect users data on Airbnb. 
- - -

## Attention
* This crawler is originally used for collecting data for academic purposes. To avoid unnecessary burden on the Airbnb server, please do not abuse this crawler. You can find tons of Airbnb data at [Inside Airbnb](http://insideairbnb.com/), which may meet your needs.

* This project is developed with:

 > Python 2.7.12
 > PyCharm Community Edition 2016.3.2




## What is this web crawler?
This is a multiprocessing Python web crawler using `requests` and `bs4` packages. With input data of user id, it collects data of each user including:
* Date of signing up
* Number of wish lists
* Number host reviews
* Average price in each wish list

And the output will be written into a text file.

## Data Screenshots
The input dataset (has been organized into table from .csv file) is as following:
<table border="1" align=center>
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
<tr>
<td>10385</td>
<td>12361</td>
<td>36408</td>
</tr>
<tr>
<td>25002</td>
<td>39798</td>
<td>73959</td>
</tr>
</tbody>
</table>

where `listing_id` is ID of Airbnb homestay, `id` is ID of observations in dataset, `reviewer_id` is ID of reviewers who has been in corresponding homestay.

Next is output dataset (has been organized into table from text file):
<div style="overflow:auto;overflow-y:hidden" border="1" align=center>
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

* * *

# Airbnb-crawler

收集Airbnb用户数据的网络爬虫。

## 注意

* 本爬虫起初用于学术数据采集目的，请不要滥用以免对Airbnb服务器造成不必要负担。[Inside Airbnb](http://insideairbnb.com/) 有许多Airbnb数据，也许能满足你的需求。

* 本爬虫的开发环境为：
 > Python 2.7.12
 > PyCharm Community Edition 2016.3.2
