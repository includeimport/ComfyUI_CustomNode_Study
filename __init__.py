
# ==================================================
# _01_create_customNode
# from으로 경로 설정, *과 import으로 모두 불러옴
# 패키지, 모듈명은 알파벳이나 _으로 시작해야한다
# 초기 실행 시 실행 여부 확인

from .test._01_create_customNode import *

NODE_CLASS_MAPPINGS = {
    "Print Hello World" : PrintHelloWorld,
    }

# + 글자에 색상 추가 -> ANSI 이스케이프 시퀀스 사용됨
# \033[34m : 파란색
# \033[92m : 초록색
# \033[0m : 스타일 초기화
print("\033[34mComfyUI Tutorial Nodes: \033[92m_01_create_customNode Loaded\033[0m")

# ==================================================
# _02_create_route

try:
    from .test import _02_create_route
    from .test._02_create_route import WebTest
    import os
    
    routes = _02_create_route.routes

    api = WebTest()
    api.add_routes(routes)

    print("\033[34m_02_create_route : \033[92mSuccess\033[0m")

except Exception as e:
    print("실행 실패: ", e)

# ==================================================




# ==================================================