# my_skp_project
- 컨테이너 기반 구조 조정
- 도커 컴포즈 프로젝트 세팅됨
- web <-> was <-> db
- db는 현재 포지션만 차지하고 있음. 실제 사용x
- 전제조건
    - 컨테이너 기반 이미지를 저장 할 저장소 및 공유 플랫폼 필요
        - 현재 hub.docker.com 활용
        - 차후 AWS ECR 활용
    - EC2 서버에 Docker 설치되어 있어야 함
        - 도커 설치
        - 스펙 상향
            - t3.micro 인스턴스 유형, 2cpu 1Rem, 30Gib
            - 메모리 증설 → 스왑메모리 4G 증가 처리
    - deploy.yml
        - ci/cd 설정 파일 업그레이드(수정)

# usage
```
    uvicorn main:app --reload
```

# 구조
my_skp_project/
│
└ main.py
└ temlates/                 ← html 위치
│    └ index.html
└ static/                   ← 정적 데이터 위치:css, js, 리소스
    └ assets
    │    └ *.jpg|png
    └ css
    │   └ *.css
    └  JS
        └ *.js