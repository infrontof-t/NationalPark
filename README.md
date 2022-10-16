# 1차 미니프로젝트
## 주제: 한국의 국립공원 정보 웹사이트 구현하기

- 목적 : Django의 기능들을 활용한 웹페이지 제작하기

- 사용된 기술스택 : Python, Django, MySQL

## 기획의도 : 코로나가 유행하며 집에서 생활하는 시간이 많아져 답답함을 해소하기 위해 국립공원을 찾는 사람들이 많아졌다. 국립공원의 정보와 그 주변의 편의시설 등의 정보를 제공할 수 있는 사이트를 제작하는 프로젝트를 진행하였다.

## API 정의 : 
![API정보](https://user-images.githubusercontent.com/108378151/196024527-825e3785-038c-4a7a-a457-d73118582240.png)

## 홈페이지 홈 화면
- 홈 화면에서는 지역 리스트를 확인할 수 있다.
![image](https://user-images.githubusercontent.com/108312272/196022321-477914a2-d208-463c-b0d8-df4ba3ed37a6.png)

## 공원 리스트 화면
- 총 22개의 국립공원 리스트를 확인할 수 있다.
![image](https://user-images.githubusercontent.com/108312272/196022342-41d3e4ad-f94d-46c5-9a6c-f80797d02ab5.png)

## 공원 정보 화면
- 간략한 공원 정보와 국립공원 사이트로 갈 수 있는 링크가 포함되어있다.
![image](https://user-images.githubusercontent.com/108312272/196022372-dfb1099e-709d-45b2-b182-b75ec04844cd.png)
![image](https://user-images.githubusercontent.com/108312272/196022384-5b583de8-ec71-49a5-81f6-73f8114a9126.png)

## 회원가입 기능 구현 화면
- 우측 상단의 회원가입 버튼을 클릭하면 회원가입 페이지로 접속하며 입력칸에 정보를 입력하고 생성하기 클릭한다.
![image](https://user-images.githubusercontent.com/108312272/196023693-41a54b1d-8f69-40cf-870b-56a8546f2fee.png)
- 회원가입이 완료되면 로그인 페이지로 이동하게 된다.
![image](https://user-images.githubusercontent.com/108312272/196023479-cccc8c76-5e14-4d5e-aa86-e90bb9df2917.png)

## 로그인, 로그아웃 기능 구현 화면
- 우측 상단의 로그인 버튼을 클릭하여 로그인 페이지로 진입할 수도 있다.
![image](https://user-images.githubusercontent.com/108312272/196022446-1eb3dab9-c38a-40fb-adb9-54c6dd9e51c7.png)
- 사용자ID 와 비밀번호를 입력 후 로그인
![image](https://user-images.githubusercontent.com/108312272/196023700-f662c003-f949-4f09-86b8-650d53249331.png)
- 로그인 완료 화면
![image](https://user-images.githubusercontent.com/108312272/196023729-26874a0e-c07f-4381-82f1-40772bc45be2.png)
- 사용자ID 옆의 로그아웃 버튼을 클릭하면 로그아웃된다.
![image](https://user-images.githubusercontent.com/108312272/196023749-1839cc62-f617-4da9-8519-cd886baba0ca.png)

## 문의사항 기능 구현 화면
- 네비게이션 바의 CONTACT 버튼을 누르면 문의사항 화면으로 넘어온다.
![콘택트구동1](https://user-images.githubusercontent.com/108378151/196024290-62b3779e-7d3a-44d8-9c33-de5493abea73.png)
- 사용자의 이메일과 문의 내용을 입력한 후 발송을 누른다.
![콘택트구동2](https://user-images.githubusercontent.com/108378151/196024300-b64ee694-83dc-4fb7-ab80-211569325c00.png)
- 관리자의 이메일로 문의사항이 전송된 것을 확인할 수 있다.
![콘택트구동3](https://user-images.githubusercontent.com/108378151/196024314-22a3f234-c0be-4693-be6a-7feaaf7dd03d.png)

## 편의시설 화면
