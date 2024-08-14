# 베이스 이미지 선택
FROM python:3.8-slim

# Docker Image Repository에 있는 애플리케이션 코드를 컨테이너 내부의 /app 경로로 복사
COPY . /app

# 명령어 실행
RUN pip3 install flask 

# 작업 디렉토리 설정
WORKDIR /app

# 컨테이너 실행 시 실행되는 명령어 설정
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]