# 함수

### **제어문**

---

1. **조건문**
   
   - If문 : 조건식에 따라 작동, 순차대로 작동

2. **반복문**
   
   - While문 : 특정 조건 만족할 때까지 반복
   
   반복문 제어
   
   - break : 반복문 종료
   
   - continue : continue이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
   
   - for-else : 끝까지 반복문을 실핼한 이후에 else문 실행
   
   - pass : 아무것도 하지 않음, 문법상 오류가 나서 필요한 경우, 코드리뷰 시에 사용

### **함수**

---

특정한 기능을 하는 코드의 묶음

**함수의 종료**

1. 내장 함수 : 파이썬 기본 함수

2. 외장 함수 : import문 통해 사용

3. 사용자 정의 함수 : 직접  만드는 함수

**함수의 정의**

 def function_name(farameter) 형태

    함수명() 형태로 함수 호출

**값에 따른 함수의 종류**

- void function

- value returning function

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

iterable

for문 한줄로 코딩하는 법 시험에 나올수도 있지만 평소에 그렇게 효율적이진 않다
