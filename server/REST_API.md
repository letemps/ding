# API
----------


## Get all dingke
Request:

	GET /dingke?user_id=all

Response:

	# key	ke_name
	1 广论
	2 心经

## Get My dingke

Request:

	GET /dingke?user_id=<user id>

Response:

	# key ke_name
	2 心经

## Summary a day

Request:

	GET /summary?type=list&date=<epoch_time>

Response:

	# user_name: ke_name, count unit;kename, count unit;
	徐xx： 心经， 3 遍； 广论， 60 分钟；	

## Get My summary 

Request:

	GET /summary?type=user

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

	POST /dingke?user_id=<user_id>
	post-data
	# key
	keys=3,	5

Response
	
	# redirect to GET /dingke?user_id=<user id>

## Submit dingke of today

Request

	POST /kingke_progress?user_id=<user_id>
	post-data
	date=<epoch time>
	p1=<key>,<count>
	p2=<key>,<count>

Response

	# 200 OK


	

	
