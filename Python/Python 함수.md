# 함수

### **제어문**

---

파이썬은 기본적으로 위에서부터 아래로 차례대로 명령 수행

1. **조건문**
   
   - If 조건 형태 : 조건식에 따라 작동
     - 복수조건문 : elif 사용
     - 중첩조건문 : if 안에 if 중첩
   
   조건 표현식 - 삼항 연산자
   
   - 'true인 경우 값 *if 조건 else* false인 경우 값' 형태 - 왼참오거

2. **반복문**
   
   - While문 : 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야함
   - for문 : 반복가능한 객체(iterable)를 모두 순회하면 종료
     - 문자열  순회
     - 딕셔너리 순회
     - enumerate 순회
       - enumerate() : 인덱스와 객체를 쌍으로 담은 열거형 객체 반환
       - 
         
     - list comprehension
     - 
   
   반복문 제어
   
   - break : 반복문 종료
   
   - continue : continue이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
   
   - for-else : 끝까지 반복문을 실행한 이후에 else문 실행
   
   - pass : 아무것도 하지 않음, 문법상 오류가 나서 필요한 경우, 코드리뷰 시에 사용

### **함수**

---

특정한 기능을 하는 코드의 묶음

**함수의 종료**

1. 내장 함수 : 파이썬 기본 함수

2. 외장 함수 : import문 통해 사용, 외부 라이브러리에서 제공

3. 사용자 정의 함수 : 직접  만드는 함수

**함수의 정의**

 def function_name(farameter) 형태

    함수명() 형태로 함수 호출

**값에 따른 함수의 종류**

- void function : 명시적인 return갑이 없는 경우, None을 반환하고 종료

- value returning function : 함수 실행 후, return문을 통해 값 반환
  
  
  ##### ***<U>주의</U>** - print와 return의 차이점
  
     print를 사용하면 호출될 때마다 값이 출력됨
     데이터 처리를 위해서는 return 사용

---

### Python의 범위(scope)

- scope
  
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  
  - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능

- variable
  
  - global variable : global scope에 정의된 변수
  
  - local variable : local scope에 정의된 변수

- 이름 검색 규칙
  
  - LEGB

pip 설치해서 import로 불러쓴다

***enumerate()**

시험 출제 빈도 높음

iterable(객체)

for문 한줄로 코딩하는 법 시험에 나올수도 있지만 평소에 그렇게 효율적이진 않다
