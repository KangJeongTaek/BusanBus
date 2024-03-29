import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

노선정류소조회URL = 'http://apis.data.go.kr/6260000/BusanBIMS/busInfoByRouteId'
정류소_도착정보_조회URL = 'http://apis.data.go.kr/6260000/BusanBIMS/stopArrByBstopid'


# 정거장 이름으로 위치 검색하기
def busStop ():
    url = 'http://apis.data.go.kr/6260000/BusanBIMS/busStopList'
    params ={'serviceKey' : 'l2SER5UdFnVMTCfW/75Op1w1xj0ZVJyWjxZCA4s2qcMkJIjXonsQeorj8k35mmylOV0ywqc75RoXXtagwXuUnQ==',
              'pageNo' : '1', 
              'numOfRows' : '11', 
              'bstopnm' : '부산시청' }

    response = requests.get(url, params=params)
    decodecontent = response.content.decode('utf-8') 
    xmlParser = BeautifulSoup(decodecontent,'xml')
    items= xmlParser.select("item")
    item = items[0].text.split('\n')
    return item


    ## content[0] == 요청한 첫번 째 정보
    ## 정류소 아이디
    ## 정류소 명
    ## 정류소 번호
    ## GPS X좌표, GPS Y좌표
    ## 정류장 구분 순으로 데이터 정제


print(busStop())


# 버스 번호로 노선 검색하기
# def busLine():
#     url = 'http://apis.data.go.kr/6260000/BusanBIMS/busInfo'
#     params ={'serviceKey' : 'l2SER5UdFnVMTCfW/75Op1w1xj0ZVJyWjxZCA4s2qcMkJIjXonsQeorj8k35mmylOV0ywqc75RoXXtagwXuUnQ==', 
#             'lineno' : '179' }

#     response = requests.get(url, params=params)
#     decodecontent = response.content.decode('utf-8') 
#     xmlParser = BeautifulSoup(decodecontent,'xml')
#     contents =  xmlParser.find('items')

#     return contents

# # print(busLine())


# 노선 ID를 통한 노선 정보 및 실시간 버스 위치 정보 제공
# def buslineId():
#     url = 'http://apis.data.go.kr/6260000/BusanBIMS/busInfoByRouteId'
#     params ={'serviceKey' : 'l2SER5UdFnVMTCfW/75Op1w1xj0ZVJyWjxZCA4s2qcMkJIjXonsQeorj8k35mmylOV0ywqc75RoXXtagwXuUnQ==',
#              'lineid' : '5200179000' }

#     response = requests.get(url, params=params)
#     decodecontent = response.content.decode('utf-8') 
#     xmlParser = BeautifulSoup(decodecontent,'xml')
#     contents =  xmlParser.find_all('item')
#     # 1번 인덱스 방향
#     # 2번 인덱스 

#     return contents

# # print(buslineId())

# # 정류소ID를 검색조건으로 실시간 버스 도착정보를 제공
# def busArrive():
#     url = 'http://apis.data.go.kr/6260000/BusanBIMS/stopArrByBstopid'
#     params ={'serviceKey' : 'l2SER5UdFnVMTCfW/75Op1w1xj0ZVJyWjxZCA4s2qcMkJIjXonsQeorj8k35mmylOV0ywqc75RoXXtagwXuUnQ==',
#              'bstopid' : '505780000' }

#     response = requests.get(url, params=params)
#     decodecontent = response.content.decode('utf-8') 
#     xmlParser = BeautifulSoup(decodecontent,'xml')
#     return xmlParser

# # print(busArrive())