# encoding:utf-8

import json

#  1、天气预报查询
import requests

param = {}
param["appkey"] = "891c9f4f2e41dff2"
param["city"] = "北京"
# param["cityid"] = "111"  # 任选
# param["citycode"] = "101260301"  # 任选


response = requests.post("http://api.jisuapi.com/weather/query", data=param)


weatherJson = response.json()

print(weatherJson)

# if weatherJson["status"] != u"0":
#     print
#     weatherJson["msg"]
#     exit()
# result = weatherJson["result"]
# print
# result["city"], result["cityid"], result["citycode"], result["date"], result["week"], result["weather"], result["temp"]
# print
# result["temphigh"], result["templow"], result["img"], result["humidity"], result["pressure"], result["windspeed"], \
# result["winddirect"]
# print
# result["windpower"], result["updatetime"]
# print
# "指数:"
# for i in result["index"]:
#     if i.has_key("ivalue"):
#         print
#         i["iname"], i["ivalue"], i["detail"]
#     else:
#         print
#         i["iname"], i["index"], i["detail"]
#
# print
# "空气质量指数："
# aqi = result["aqi"]
# print
# aqi["so2"], aqi["so224"], aqi["no2"], aqi["no224"], aqi["co"]
# print
# aqi["co24"], aqi["o3"], aqi["o38"], aqi["o324"], aqi["pm10"]
# print
# aqi["pm1024"], aqi["pm2_5"], aqi["pm2_524"], aqi["iso2"], aqi["ino2"]
# print
# aqi["ico"], aqi["io3"], aqi["io38"], aqi["ipm10"], aqi["ipm2_5"]
# print
# aqi["aqi"], aqi["primarypollutant"], aqi["quality"], aqi["timepoint"]
# print
# aqi["aqiinfo"]["level"], aqi["aqiinfo"]["color"], aqi["aqiinfo"]["affect"], aqi["aqiinfo"]["measure"]
#
# print
# "未来几天天气："
# for daily in result["daily"]:
#     print
#     daily["date"], daily["week"], daily["sunrise"], daily["sunset"]
#     print
#     daily["night"]["weather"], daily["night"]["templow"], daily["night"]["img"], daily["night"]["winddirect"], \
#     daily["night"]["windpower"]
#     print
#     daily["day"]["weather"], daily["day"]["img"], daily["day"]["winddirect"], daily["day"]["windpower"]
#
# print
# "未来几小时天气："
# for hourly in result["hourly"]:
#     print
#     hourly["time"], hourly["weather"], hourly["temp"], hourly["img"]
