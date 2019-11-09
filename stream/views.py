from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests

@login_required
def create_stream(request):

  url = "https://api.mux.com/video/v1/live-streams"

  payload = ""
  headers = {
      'Content-Type': "application/x-www-form-urlencoded",
      'Authorization': "Basic MzEwMzczOTMtMGM5ZS00ZjNjLWEzMDYtYTdhODE5YjhiZjE2OkdnQmpwYmNHTURyaTE0T2VJWXhCWE4ydzNGTXltMkFhQ1dmMzNuTW5ob25LRWFIaDJST1N5UzBJSTBpSzYrQ042Qys2cnZRRmRMSA==",
      'User-Agent': "PostmanRuntime/7.16.3",
      'Accept': "*/*",
      'Cache-Control': "no-cache",
      'Postman-Token': "074f8a0c-ca31-46d8-a4ca-bfa801e1f2c1,17217454-6f02-4e30-b8b9-579e31b0ebec",
      'Host': "api.mux.com",
      'Accept-Encoding': "gzip, deflate",
      'Content-Length': "58",
      'Connection': "keep-alive",
      'cache-control': "no-cache"
      }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

  return render(request, 'stream/index.html' , context={'response':response.text})