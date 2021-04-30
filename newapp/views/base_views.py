# [21/04/23] views.py 모듈 분리
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from newapp.models import Question
# from ..models import Question랑 같은 표현

# [21/04/28] 검색기능 구현을 위한 Q 모델
from django.db.models import Q

def index(request):
    # 조회 [21/04/15]
    # get('page','1'): 페이지의 파라미터가 없는 URL 을 위해서 기본값을 지정 해 줬음
    page = request.GET.get('page', '1')

    # [21/04/28] 검색 기능 구현하기 위한 기본값 지정
    kw = request.GET.get('kw', '')

    # ---------------------- [edit 21/04/13 ]  ----------------- #
    # 게시판 출력 : create_date 를 기준으로 정렬
    question_list = Question.objects.order_by('-create_date')
    # print(type[question_list])
    # print("question_list': question_list")

    # [21/04/28] 검색 기능 구현
    # distinct 중복제거, .filter 는 조건에 맞는 여러 값을 출력 할때 사용
    # .filter 와 연계해서 사용하는 keyword
    # __icontains 는 해해당컬럼의 값이 지정한 문자열을 포함하는 자료를 검색 할때 사용.
    # 예) like '%디장%' => subject__icontains ='디장' 제목에서 '디장' 을 의미 (db의 like 와 같은 기능)

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | Q(content__icontains=kw)
        ).distinct()

    # [21/04/15]
    # Paginator class 는  조회해온 값(question_list)을 페이징 객체(인스턴스)로 변환
    # 변환한 내용을 pagenator 객체(인스터스)에 저장
    # Paginator 클래스를 호출 하면서 두번재 인수에 페이지당 보여줌

    # 게시물 개수(5개씩 보여줌)을 기재
    pagenator = Paginator(question_list, 5)
    # Paginator class 를 이용한 객체에 쓸 수 있는 속성

    page1 = pagenator.get_page(page)
    context = {'question_list1': page1, 'page': page, 'kw': kw}

    # context = {'question_list1': question_list}
    # print("context : ",context)

    # setting 후 서버 접속 잘되는지 확인 하기위해 게시판에 출력해 봄
    # return HttpResponse("http://localhost:8000/newapp/ 에서 확인하세요")

    # return render(request, 'newapp/base.html', context)
    # return render(request, 'newapp/question_list.html', context)
    return render(request, 'newapp/main.html')

# 21/04/23 상품 전체 page 추가
def infoIndex(request):
    return render(request, 'newapp/infoIndex.html')

# 21/04/26 상품 상세 top,jean,outer page 추가
def infoTop(request):
    return render(request, 'newapp/infoTop.html')

def infoJean(request):
    return render(request, 'newapp/infoJean.html')

def infoOuter(request):
    return render(request, 'newapp/infoOuter.html')

# 21/04/27 단일 상품 top,jean,outer page 추가
def topInfo(request):
    return render(request, 'newapp/topInfo.html')

def jeanInfo(request):
    return render(request, 'newapp/jeanInfo.html')

def outerInfo(request):
    return render(request, 'newapp/outerInfo.html')

# 상품가이드 page 생성 [21/04/29]
def shoppingGuide(request):
    return render(request, 'newapp/admin/shoppingGuide.html')

def openMenu(request):
    return render(request, 'newapp/admin/openMenu.html')

def qna(request):
    # 조회 [21/04/15]
    # get('page','1'): 페이지으 파라미터가 없는 URL을 위해서 기본값을 지정해 줬음
    page = request.GET.get('page', '1')
    # ---------------------- [edit 21/04/13 ]  ----------------- #
    # 게시판 출력
    question_list = Question.objects.order_by('-create_date')
    # print(type[question_list])
    # print("question_list': question_list")

    # [21/04/15]
    # Paginator class는  조회해온 값(question_list)을 페이징 객체(인스턴스)로 변환
    # 변환한 내용을 pagenator 객체(인스터스)에 저장
    # Paginator 클래스를 호출 하면서 두번재 인수에 페이지당 보여줄
    # 게시물 개수(5개씩 보여줌)을 기재
    pagenator = Paginator(question_list, 5)
    # Paginator class를 이용한 객체에 쓸 수 있는 속성
    # .count : 게시물의 개수(전체)
    # .per_page : 페이지당 보여줄 게시물 개수
    # .page_range : 페이지의 범위
    # .number : 현재 페이지 번호
    # .previous_page_number : 이전 페이지 번호
    # .next_page_number : 다음 페이지 번호
    # .start_index : 헌재 페이지 시작 인덱스
    # .end_index : 헌재 페이지 끝 인덱
    # .has_previous : 이전 페이지 유,무
    # .has_next : 다음 페이지 유,무
    page1 = pagenator.get_page(page)
    context = {'question_list1': page1}

    # context = {'question_list1': question_list}
    # print("context : ",context)

    # setting 후 서버 접속 잘되는지 확인 하기위해 게시판에 출력해 봄
    # return HttpResponse("http://localhost:8000/newapp/ 에서 확인하세요")

    # return render(request, 'newapp/base.html', context)
    return render(request, 'newapp/question_list.html', context)

# urls.py 에서 넘어온 detail()
def detail(request,question_id):
    # models.py 에 있는 Question
    # urls.py의 question_id와 question.html의 question.id는 같다.
    # 즉 question_id or question.id 사용해도 된다.
    # question = Question.objects.get(id=question_id)
    #  404 에러를 실행  (py 이므로 줄바꿈 주의!!)
    question = get_object_or_404(Question, pk=question_id)

    context = {'question1': question}
    # render는 함수 (from django.shortcuts import render 해서 사용)
    # context 안에 있는 데이터를 해당 html파일 안에 request한다는 의미
    return render(request, 'newapp/question_detail.html', context)

    # 404 페이지
    # 요청하는 페이지가 없거나 서버에서 오류가 발생하면 반환되는 응답코드
    # 기본적으로 정상처리 되면 200을 반환
    # 서버오류는 500을 띄우기도 함.