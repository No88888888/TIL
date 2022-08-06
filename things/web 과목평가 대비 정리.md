# HTML

`Hyper Text` Markup Language

### HTML 기본구조

- html: 문서의 최상위 요소
- head: 문서 메타데이터 요소
    - title
    - meta
    - link
    - script
    - style
- body: 문서 본문 요소
    
    ### 요소
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/61f4e689-c2d1-4273-847a-fcfc31b1eef5/Untitled.png)
    
    - 내용이 없는 태그들도 존재(닫는 태그가 없음)
        - br, hr, img 등
    - 요소는 중첩 될 수 있음
    
    ### 속성
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a40476f-17c4-4dfe-989e-ea21102a673e/Untitled.png)
    
    ### 시맨틱 태그
    
    - HTML 태그가 특정 목적, 의미적 가치를 가지는 것
    - Non semantic 요소: div, span
    - semantic 요소: a, form, table, header, nav, aside, section, article, footer
    
    ### 시맨틱 태그 사용 이유
    
    - 의미 있는 정보의 그룹을 태그로 표현
    - 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수하기 쉬움
    
    ### DOM 트리
    
    - HTML문서를 브라우저에서 랜더링하기 위한 구조
    

## HTML 문서 구조화

- 인라인 / 블록 요소
    - 인라인: 글자 취급
    - 블록: 한 줄 모두 사용
- 텍스트 요소
    - <a>,<span>,<br>,<img>
- 그룹 컨텐츠
    - <ol>,<ul>, <div>
- form
    - 정보를 서버에 제출하기 위해 사용하는 태그
- input
    - 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
- input label
    - label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
    

# CSS

cascading style sheets 

스타일을 지정하기 위한 언어

### CSS 정의 방법

- 인라인 - 실수 많음 중복, 찾기 어려움
- 내부참조 - <style> 코드 길어짐
- 외부 참조 - 분리된 css파일

### CSS 선택자

- 기본 선택자
    - 전체 선택자: *
    요소 선택자: h1
    - 클래스 선택자: .h1
    아이디 선택자: #h1
    속성 선택자
- 결합자
    - 자손 결합자: .box p
    자식 결합자: .box > p
    - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소

### CSS 적용 우선순위

- `!important > 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element > CSS 파일 로딩 순서`

### CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다
    - 상속 되는 것 예
        - font, color, text-align, opacity, visibility 등
    - 상속 되지 않는 것 예
        - width, height, margin, padding, border, box-sizing, display
        position, top/right/bottom/left 등
        

### 크기 단위

- px
- %
- em: 상속 영향 받음
        요소에 지정된 사이즈에 상대적인 사이즈 가짐
- rem: 상속 영향 안받음
         최상위(html) 사이즈를 기준으로 배수 단위 가짐
- viewport
    - 디바이스 화면 기준으로 결정
    - vw, vh, vmin, vmax
    

### 색상 단위

- RGB
- HSL
- a는 투명도

# CSS 결합자

- 자손 결합자(공백)
    - 선택자A 하위의 모든 선택자B 요소
- 자식 결합자(>)
    - 선택자A 바로 아래의 선택자B 요소
- 일반 형제 결합자(~)
    - 선택자A의 형테 요소 중 뒤에 위치하는 선택자B 요소 모두 선택
- 인접 형제 결합자(+)
    - 선택자A의 형제 요소 중 바로 뒤에 위치하는 선택자B 요소 선택
    

# CSS Box model

### CSS 원칙 1

`모든 요소는 네모(박스모델) 이고, 위에서부터 아래로 왼쪽에서 오른쪽을 쌓인다`

- 가로 - inline direstion
세로 -block direction
normal flow

### Box model

- box 구성영역
    - margin -배경색 지정 X
    - border
    - padding -배경색 지정 O
    - content

### Box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box

### CSS 원칙 2

`display에 따라 크기와 배치가 달라진다`

### CSS display

- display : block
    - 줄 바꿈이 일어나는 요소
    - 가로 폭 모두 차지
    - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
- display: inline
    - 줄 바꿈이 일어나지 않는 행의 일부 요소
    - content 너비만큼 가로 폭 차지
    - width, height, margin-top, margin-bottom 지정 X
    - 상하 여백은 line-height로 지정
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a1d2fc21-b047-46fe-8644-6e06930e6694/Untitled.png)
    
- display: inline -block
    - block과 inline레벨 요소의 특징을 모두 가짐
    - inline처럼 한줄에 표시할 수 있고, block처럼 width,height,margin 속성을 모두 지정할 수 있음
- display: none
    - 해당 요소를 화면에 표시하지도 공간 부여도 하지 않음
    - visibility:hidden은 해당 요소가 공간은 차지, 화면에 표시하진 않음
    

### CSS postition

- 요소의 위치를 지정
    - static: 모든 태그의 기본 값
    - realative: 상대위치
        - 자기 자신의 static 위치를 기준으로 이동
        - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음
        - normal flow 유지
    - absolute: 절대위치
        - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
        - normal flow 벗어남
    - fixed : 고정위치
        - 요소응 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지않음
        - vp 기준으로 이동
    - sticky : 스크롤에 따라 static - > fixed로 변경
    

### CSS 원칙 3

`position으로 위치의 기준을 변경`

- relative: 본인의 원래 위치
- absolute: 특정 부모의 위치
- fixed: 화면의 위치
- sticky: 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경

# 개발자 도구

- HTML DOM 조작 가능
- styles, computed 확인 가능

---

# CSS layout

### Float

- 박스를 왼쪽 혹은 오른쩍으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 래핑하도록 함

# Flexbox

### CSS flexible box layout

- 축
    - main axis : row row-reverse column column-reverse
    - cross axis
- 구성 요소
    - Flex Container 부모요소
        - display속성을 flex혹은 inline-flex로 지정
    - Flex Item 자식요소
    

### Flexbox 사용 이유

- `float, position 이용 시 수직정렬, 아이템 너비 높이 간격 동일 배치 어려움`

### Flex 속성

- 배치 속성
    - flex-direction: Main axis 방향 설정
    - flex-wrap:아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
    - flex-flow
        - flex-direction 과 flex-wrap의 숏핸드
        - 예 flex-flow: row nowrap;
        
- 공간 나누기
    - justify-content (main axis)
        - main axis 기준으로 공간 배분
        - flex-start / flex-end
        - center
        - space-between
        - space-around 와 space-evenly의 차이
            - space-around는 아이템 두러싼 영역을 듄일하게 분배
            - space-evenly는 전체 영역에서 아이템 간 간격릏 균일하게 분배
    - align-content (cross axis)
        - cross axis를 기준으로 공간 배분
    
- 정렬
    - align-items
        - 모든 아이템들을 cross axis기준으로 정렬
        - stretch
        - flex-start / flex-end
        - center
        - baseline
    - align-self (개별 아이템)

# Bootstrap

### CDN - content delivery network

### spacing(margin and padding)

          {property}{side}-{size} 형태

- property
    - m - margin
    - p - padding
- side
- 
    - t - top
    - b - bottom
    - s - start
    - e - end
    - x - left,right
    - y - top, bottom
- size
    - 0 ~ 5
    - auto

# Components

- buttons
- dropdown
- form
- navbar
- carousel
- modal
    - 제거하지 않고 배경화면 눌러도 사라짐
- card > grid card

# Grid system(반응형 웹)

`요소들의 디자인과 배치에 도움을 주는 시스템`

- 기본 요소
    - column : 실제 컨텐츠를포함하는 부분
    - gutter: 칼럼과 칼럼 사이 공간
    - container : column들을 담고 있는 공간
        - 12개의  column
        - 6개의 grid breakpoints
        

---

1. HTML 개념
각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오.
    1. 웹 표준을 만드는 곳은 Mozilla 재단이다. - 파이퍼폭스 만든곳
    2. 표(table) 을 만들 때에는 반드시 <tr> 태그를 사용해야 한다.
    3. 제목(Heading) 태그는 제목 이외에는 사용하지 않는 것이 좋다.
    4. 리스트를 나열하기 위해서는 <ul>태그만 사용할 수 있다.
    5. HTML의 태그는 반드시 별도의 닫는 태그가 필요하다.

-답:

1. F - W3C(www만든재단)
2. F - 반드시는 아니다
3. T - 시맨틱 태그
4. F - ul과 ol
5. F - img br 태그같은거

1. CSS 개념
각 문항을 읽고 맞으면 T, 틀리면 F를 작성 하시오.
    1. HTML과 CSS는 각자 문법을 갖는 별개의 언어이다.
    2. 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 작동한다.
    3. 자식 요소 프로퍼티는 부모의 프로퍼티를 모두 상속 받는다.
    4. 디바이스마다 화면의 크기가 다른 것을 고려하여 상대 단위인 %를 사용한다.
    5. id 값은 유일해야 하므로 중복되어서는 안된다

답:

1. T - 한 파일안에 작성할 수 있는 특성일 뿐 별개의 언어이다
2. T - reset CSS가 적용되어있다
3. F - 상속 받는것 안받는것 있다
4. F - 디바이스 고려는 vw, vh
5. T

CSS 우선순위
CSS는 우선 적용되는 순서가 존재 한다. 우선순위가 높은 순으로 나열 하시오
요소 선택자, Inline Style, 소스 순서,
!important, id 선택자, class 선택자

답:
!important -> Inline Style -> id 선택자 -> class 선택자 -> 요소 선택자 ->소스 순서