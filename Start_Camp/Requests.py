import requests

# 요청 보낼 URL
url ='http://api.agify.io/?name=isaac'

#url로 요청을 보내는 방법
# requests.get(' url ')

response = requests.get(url).json()
# print(response)
name = response.get('name')
age = response.get('age')
print(f'안녕하세요 {name}({age})님, 환영합니다')