# API
----------


## Get all dingke
Request:

	GET /all_dingke

Response:

	# key	ke_name
	1 广论
	2 心经

## Get My dingke

Request:

	GET /my_dingke/<user_id>

Response:

	# key ke_name
	2 心经

## Summary a day

Request:

	GET /summary/<yyyymmdd>

Response:

	# user_name: ke_name, count unit;kename, count unit;
	徐xx： 心经， 3 遍； 广论， 60 分钟；	

## Get My summary 

Request:

	GET /summary/<user_id>

Response:

	#today:
	# user_name: ke_name, count unit;kename, count unit;
	徐xx： 心经， 3 遍； 广论， 60 分钟；	
	#this week
	# user_name: ke_name, count unit;kename, count unit;
	徐xx： 心经， 15 遍； 广论， 160 分钟；	
	#this month
	# user_name: ke_name, count unit;kename, count unit;
	徐xx： 心经， 45 遍； 广论， 360 分钟；
	#this year
	# user_name: ke_name, count unit;kename, count unit;
	徐xx： 心经， 1145 遍； 广论， 1360 分钟；	

## 	Add my dingke

Request

	POST /my_dingke/<user_id>/<key>

Response
	
	# redirect to GET /dingke/<user_id>

## Delete my dingke

Request

	DELETE /my_dingke/<user_id>/<key>

## Submit dingke of today

Request

	POST /kingke_progress/<user_id>
	post-data
	date=<epoch time>
	p1=<key>,<count>
	p2=<key>,<count>

Response

	# 200 OK


	

	
