# Requests
### Requests란 API에서 필요한 데이터를 요청하여 가져오는 것
## * 다음과 같이 .py를 작성

import requests

#요청 보낼 URL

url ='http://api.agify.io/?name=isaac'

#url로 요청을 보내는 방법

#requests.get(' url ')

response = requests.get(url).json()
#print(response)

name = response.get('name')

age = response.get('age')

print(f'안녕하세요 {name}({age})님, 환영합니다')