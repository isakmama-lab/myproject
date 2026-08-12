import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# CSRF 토큰 생성을 위한 비밀키 추가
# SECRET_KEY = "dev"

# Render 환경 변수에서 SECRET_KEY를 가져오고, 없으면 기본값 'dev' 사용
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')