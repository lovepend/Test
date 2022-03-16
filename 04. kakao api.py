#REST API = ddcfd4509dc2ec690ebb764199ff2247
#code = https://kauth.kakao.com/oauth/authorize?client_id=ddcfd4509dc2ec690ebb764199ff2247&redirect_uri=https://example.com/oauth&response_type=code&scope=talk_message,friends
#code = 'iXurIJ-hAeIMCo9nXZEtNgVvC9JKn4vuiss4A_RRNXCbN65W5ZBaYQmU6E27eBlAIZctDQo9c00AAAF_izJq_Q'

import requests
import json

# 카카오톡 메시지 API
def access_token():
    url = "https://kauth.kakao.com/oauth/token"

    data = {
        "grant_type" : "authorization_code",
        "client_id" : "ddcfd4509dc2ec690ebb764199ff2247",
        "redirect_url" : "https://localhost:3000",
        "code" : "{코드}"
    }
    response = requests.post(url, data=data)
    tokens = response.json()
    print(tokens)

# 카카오톡 메시지 API
def refresh_token():
    url = "https://kauth.kakao.com/oauth/token"

    data = {
        "grant_type": "refresh_token",
        "client_id": "ddcfd4509dc2ec690ebb764199ff2247",
        "refresh_token": "{refresh_token}"
    }
    response = requests.post(url, data=data)
    tokens = response.json()

    # kakao_code.json 파일 저장
    with open("kakao_token.json", "w") as fp:
        json.dump(tokens, fp)
    

def kakao_message():
        
    with open("kakao_token.json","r") as fp:
        tokens = json.load(fp)
    # print(tokens)
    # print(tokens["access_token"])

    friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

    # GET /v1/api/talk/friends HTTP/1.1
    # Host: kapi.kakao.com
    # Authorization: Bearer {ACCESS_TOKEN}

    headers={"Authorization" : "Bearer " + tokens["access_token"]}

    result = json.loads(requests.get(friend_url, headers=headers).text)

    print(type(result))
    print("=============================================")
    print(result)
    print("=============================================")
    friends_list = result.get("elements")
    print(friends_list)
    # print(type(friends_list))
    print("=============================================")
    print(friends_list[0].get("uuid"))
    friend_id = friends_list[0].get("uuid")
    print(friend_id)


    send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

    data={
        'receiver_uuids': '["{}"]'.format(friend_id),
        "template_object": json.dumps({
            "object_type":"text",
            "text":"test",
            "link":{
                "web_url":"www.daum.net",
                "web_url":"www.naver.com"
            },
            "button_title": "바로 확인"
        })
    }

    response = requests.post(send_url, headers=headers, data=data)
    response.status_code

kakao_message()