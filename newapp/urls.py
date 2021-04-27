# ---------------------- [edit] ----------------- #
from django.urls import path
# ----------------------------------------------- #
from . import views
# ---------------------- [edit] ----------------- #
# url 에 별칭 부여하기(name='')
# 실제 주소명 /newapp/은 index 라는 URL 별칭으로 변경
# 실제 주소명 /newapp/question_id/는 detail 라는 URL 별칭으로 변경
# --------[네임 스페이스 : 각각의 앱이 관리 하는 공간] --------- #
# 네임스페이스 변수를 만든다면 저장되는 문자열값은 앱 이름과 동일하게 하는것이 편하다.
app_name = 'newapp'
# ------------------------------------------------------- #


urlpatterns = [
# 앱(newapp)을 추가할때 다른 앱(config/urls.py)하고 url 별칭이 중복되면 안된댜
    path('', views.index, name='index'),
# 2021.04.13 전은주 게시글 클릭시 들어갈 페이지 추가
    path('question/qna/<int:question_id>/', views.detail, name='detail'),
# 게시글 답변작성 페이지 추가 (한 후 views.py에 함수 만든다)
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
# 2021.04.14 전은주
    path('question/create/', views.question_create, name='question_create'),
# 2021.04.21 질문의 수정부분
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),

    # 2021.04.22 질문과 답변 분리(댓글이 없거나 아이디가 없을경우)
    path('comment/create/question/<int:question_id>/', views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_question, name='comment_delete_question'),

    path('comment/create/answer/<int:answer_id>/', views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer, name='comment_delete_answer'),

# 질문게시판 만들기
   path('question/qna/', views.qna, name='qna'),

# 전제 상품 리스트 page [21/04/26]
   path('infoIndex/',views.infoIndex, name='infoIndex'),

#  세부 상품 리스트 page [21/04/26]
   path('infoTop/',views.infoTop, name='infoTop'),
   path('infoJean/',views.infoJean, name='infoJean'),
   path('infoOuter/',views.infoOuter, name='infoOuter'),

#  단일 상품 리스트 page [21/04/26]
   path('infoTop/topInfo/',views.topInfo, name='topInfo'),
   path('infoJean/jeanInfo/', views.jeanInfo, name='jeanInfo'),
   path('infoOuter/outerInfo/', views.outerInfo, name='outerInfo'),

]
