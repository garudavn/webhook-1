# -*- coding: utf-8 -*-

# from rest_framework.views import APIView
# from rest_framework.request import Request
# from rest_framework.response import Response
import requests
import json

# class Test(APIView):
#     # def post(self, request):
#     #     # req = request.data['req']
#     #     resp = {'response': 'ok'}
#     #     print(resp)
#     #     return Response(resp, content_type='application/json; charset=utf-8')


#     def post(self, request):
#         headers = {'content-type': 'application/json'}
#         url = 'https://valuation.homify.com.vn/RealEstatePriceService/landprice/'
#         req = {'cuoi':'','dau':'','diadiem':'HN','dientich':'80','duong':'Cầu Giấy','loaiBDS':'D','loaiduong':'D','mattien':'','nam':'2016','phuong':'Quan Hoa','quan':'Cầu Giấy'}
#         response = requests.post(url,params=req,headers=headers)
#         print(response.status_code)
#         # resp_json = response.json()
#         # print(resp_json)
#         return Response(response)
# headers = {'content-type': 'application/json'}

url = 'https://valuation.homify.com.vn/RealEstatePriceService/landprice/'
req = json.dumps({'cuoi':'','dau':'','diadiem':'HN','dientich':'80','duong':'Cầu Giấy','loaiBDS':'D','loaiduong':'D','mattien':'','nam':'2016','phuong':'Quan Hoa','quan':'Cầu Giấy'})
response = requests.post(url,data=req)
j2 = response.status_code
j3 = response.json()
print j3







