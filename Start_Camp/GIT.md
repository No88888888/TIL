1. **GIT** 분산 버전관리 프로그램

   - GITHUB
   - GITLAB

2. **마크다운(markdown)** - 개발문서의 시작과 끝

   - 문서의 구조와 내용을 같이 쉽고 빠르게 적고자 탄생
   - 선택한 언어의 highlight syntax
   - 깃허브 생성 시 repository 생성 → README.md에 해당 repository에 대한 설명 작성(공식문서)
     - README.md
       - 프로젝트에 대한 설명 문서
       - 깃허브에서 가장 먼저 보는 문서
       - 일반적으로 소프트웨어와 함께 배포
       - 작성 형식은 따로 없으나, 일반적으로 마크다운을 이용해 작성
       - `특정` 버전으로 남긴다 = `커밋` 한다

3. **Repository** - 특정 디렉토리를 버전 관리하는 저장소

   - git init 명령어로 로컬 저장소를 생성

     1. working Dir : 내가 작업하고 있는 `실제 디렉토리`  - untracked

     2. Staging Area: 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳 - Staged

     3. Repository: 커밋들이 저장되는 곳 - Commited

        `untracked`   →  `Staged`   →  `Commited`
                           git add       git commit

## GIT Remote Repository 연결하기

### Remote Repo 생성하기

	#### GITHUB
	
	1. 기본 브랜치 이름 master로 변경하기
	2. new Repo 생성 버튼 눌러서
	 	1. 이름 설정
	 	2. 만들기!

#### LOCAL

 	1. 새로운 디렉토리 생성
 	 	1. mkdir
 	 	2. cd
 	 	3. git init
 	 	4. git remote add origin {원격 레포지토리 url}
 	 	5. git remote : origin 이름으로 remote 추가 된 것 확인
 	 	6. touch README.md
 	2. 버전 남기기(remote repository로 push하기 전에 반드시 Commit이 있어야 한다)
 	 	1. git add(파일명, 확장자 파일명, 확장자 파일명, 확장자 파일명, 확장자)
 	     - git add . 현재 위치한 w.d의 모든 수정 사항
 	 	2. git commit -m 'first commit'
 	 	3. git push origin master
 	     * git push -u origin master 
 	       다음에 push할때 git push만 해도 된다

### GIT

----

#### 협업 복구 백업

 | Git과 Github는 다르다

|git은 분산 버전 관리 시스템 github는 git을 통해 이용하는 cloud서비스다



#### Git 기본 명령어(로컬 레포지토리)



1. Local Repository를 생성할 때 : `git init`
2. Working Directory에 생긴 변화 사항 (파일생성, 삭제, 수정 등...)을 버전으로 관리하고자, Staging Area에 올리는 명령어: `git add (file.확장자)`
   현재 경로를 의미하는 `git add . ` : 현재 WD에 생긴 모든 변경 사항을 한번에 Staging Area에 올리는 명령어
3. 버전을 기록할 때, Commit을 남길 때 : `git commit -m '커밋 내용(최대한 상세하게)'`
4. file의 상태:
   1. `untracked` : git이 아직 관리하지 않다. (최초 생성 시)
   2. add 명령어를 통해서 Staging Area 올라간 파일 : `Tracked`
5. git status : 현재 Local Repository의 상태를 확인하는 명령어(습관처럼 입력해야한다)


#### TIL Remote Repository

1. 원격 레포지토리 생성
2. 로컬 레포지토리 샐성
   1. 리드미 파일 만들기
   2. 내용 기입
3. 리모트와 로컬 연결
4. Push 명령어로 리드미 파일 업로드
5. 
---

#### 협업과 복구 및 백업

##### 원격 저장소 연결

1. github에 원격 저장소를 생성합니다
2. 로컬 저장소(Repository) 생성합니다
3. **원격 저장소에 push 하기 전에 반드시 최소 하나 이상의 Commit을 가져야한다**

##### 원격 저장소 연결 명령어

1. git remote add origin (repository Url)
2. git remote -v : origin (http://www.github.com/)  : 등록한 Remote Repository 정보 확인
3. git push -u origin master : 로컬에서 생긴 커밋 내역을 업로드
   - git push
4. git pull origin master : 원격 저장소의 변화 사항을 다운로드
5. git clone (git Repository Url) : 원격 저장소를 복제 해온다(원격 -> 로컬) : 다운로드

#### gitignore
   * gitignore는 git으로 관리하고 싶지 않은 파일들을 따로 관리할 때 사용
      - .gitignore 형태이며 보통 보안과 관련된 사항들을 관리할 때 사용
      - 한번 commit하고 난 후에는 gitignore할 수 없음을 명심