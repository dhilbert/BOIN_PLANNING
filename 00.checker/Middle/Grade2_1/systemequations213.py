import numpy as np
import random
from fractions import Fraction

answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
}


def bool_jo(num):
    if type(num) == int:
        num = int(str(num)[-1])

        lee_nums = [0, 1, 3, 6, 7, 8]
        if num in lee_nums:
            return True
        else:
            return False
    else:
        num = str(num)[-1]
        num = ord(num)
        check = (num - 44032) % 28
        if check:
            return True
        return False


def proc_jo(num, check=0):
    if check < 0:
        # 은는
        if bool_jo(num):
            return "은"
        return "는"
    elif check == 0:
        # 이가
        if bool_jo(num):
            return "이"
        return "가"
    elif check == 2:
        # 와과
        if bool_jo(num):
            return "과"
        return "와"
    elif bool_jo(num):
        # 을를
        return "을"
    return "를"

def made_answer_cand_1(a):
    return [a-2,a-1,a,a+1,a+2]

def made_answer_cand_2(a1,a2):
    c=[]
    if   abs(a2)==1:
        return made_answer_cand_1(a1)
    for i in range(-2,3,1):
        if a1-i==0 or a2-i==0:
            c.append("$$수식$${}$$/수식$$".format(0))
        elif a2-i==1:
            c.append("$$수식$${}$$/수식$$".format(a1-i))
        else:
            c.append("$$수식$${} OVER {}$$/수식$$".format(a1-i,a2-i))
    return c

def made_answer_cand_3(a):
    return[a-10,a-5,a,a+5,a+10]
    

def gcd(a, b): 
    if a < b: (a, b) = (b, a) 
    while b != 0: 
        (a, b) = (b, a % b) 
    return a
def made_string(a):
    string=a[0]
    for i in range(len(a)):
        if i==0:
            continue
        else:
            string=string+", "+a[i]
    return string

def made_sign_string(a):
    if a<0:
        return "-`{}".format(abs(a))
    else:
        return "+`{}".format(a)

def made_fraction_string(a):
    if str(type(a))=="<class 'int'>":
        return a
    if a<0:
        return "`-`{}over{}".format(abs(a.numerator),abs(a.denominator))
    else:
        return "{}over{}".format(a.numerator,a.denominator)

#2-1-3-01
def systemequations213_Stem_001():
    stem = "다음 중 함수가 아닌 것은? \n\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n\n"
    answer = "(답)\n{a1}\n"
    comment = "(해설)\n" \
              "① {c1}\n" \
              "② {c2}\n" \
              "③ {c3}\n" \
              "④ {c4}\n" \
              "⑤ {c5}\n\n"

    
    cand1=["반지름의 길이가 $$수식$$ x`` rm cm`$$/수식$$인 원의 둘레의 길이 $$수식$$ y`` rm cm`$$/수식$$","(원의 둘레의 길이)$$수식$$`=`2` TIMES ` pi ` TIMES `$$/수식$$(반지름의 길이)에서$$수식$$ y`=2 pi x` $$/수식$$"]
    cand2_answer=["$$수식$$y`$$/수식$$는 자연수 $$수식$$ x` $$/수식$$의 배수의 개수","자연수 $$수식$$3$$/수식$$의 양의 배수의 개수는 알 수 없다.",1]##정답인 후보는 길이가3인 리스트
    cand3=["밑변의 길이가 $$수식$$rm 12``cm`$$/수식$$이고, 높이가 $$수식$$x`` rm cm`$$/수식$$인 평행사변형의 넓이 $$수식$$y`` rm cm ^{2} `$$/수식$$","(평행사변형의 넓이)$$수식$$=$$/수식$$(밑변의 길이)$$수식$$TIMES $$/수식$$(높이)에서$$수식$$y`=`12x`$$/수식$$"]
    cand4=["$$수식$$y`$$/수식$$는 자연수 $$수식$$x`$$/수식$$를 $$수식$$5$$/수식$$로 나눈 나머지","자연수 $$수식$$x`$$/수식$$를 $$수식$$5$$/수식$$로 나눈 나머지는 각각 하나로 정해진다."]
    cand5=["우유 $$수식$$rm 80``L`$$/수식$$를 $$수식$$x`$$/수식$$명에게 똑같이 나누어 줄 때, 한 사람이 받는 우유의 양 $$수식$$y`` rm L`$$/수식$$","$$수식$$y= {80} over {x}$$/수식$$"]
    cand6=["반지름의 길이가 $$수식$$ x`` rm cm`$$/수식$$인 원의 넓이 $$수식$$y`` rm cm ^{2} `$$/수식$$","(원의 넓이)$$수식$$=` pi ` TIMES `$$/수식$$(반지름의 길이)제곱에서 $$수식$$ y`=pix^2`$$/수식$$"]
    cand7=["밑변의 길이가 $$수식$$rm 16``cm`$$/수식$$이고, 높이가 $$수식$$x`` rm cm`$$/수식$$인 삼각형의 넓이 $$수식$$y`` rm cm ^{2} `$$/수식$$","(삼각형의 넓이)$$수식$$=$$/수식$$$$수식$$`{1}OVER{2}` TIMES `$$/수식$$(밑변의 길이)$$수식$$TIMES $$/수식$$(높이)에서$$수식$$y`=`{1}OVER{2} TIMES 16x = 8x`$$/수식$$"]
    cand8_answer=["절댓값이 $$수식$$ x`$$/수식$$인수 $$수식$$y`$$/수식$$","하나의 $$수식$$x$$/수식$$에 대하여 2개의 $$수식$$y$$/수식$$값이 존재할 수 있으므로 함수가 아니다",1]
    cand9=["한개에 $$수식$$x`$$/수식$$원인 음료수$$수식$$4`$$/수식$$개 의 값 $$수식$$y`$$/수식$$원","$$수식$$y``=``4x`$$/수식$$"]
    cand10=["사과주스 $$수식$$rm 30``L`$$/수식$$를 $$수식$$x`$$/수식$$명에게 똑같이 나누어 줄 때, 한 사람이 받는 사과주스의 양 $$수식$$y``rm L`$$/수식$$","$$수식$$y= {30} over {x}$$/수식$$"]
    cand11_answer=["어떤 수 $$수식$$x`$$/수식$$의$$수식$$4`$$/수식$$배는 $$수식$$y`$$/수식$$보다 크다","$$수식$$4x`&gt;`y`$$/수식$$(부등식)",1]
    cand_list=[cand1,cand3,cand4,cand5,cand6,cand7,cand9,cand10]
    answer_cand_list=[cand2_answer,cand8_answer,cand11_answer]
    list_1=random.sample(cand_list,4)
    answer_list=random.sample(answer_cand_list,1)
    list_1.append(answer_list[0])
    random.shuffle(list_1)
    for i in range(5):
        if len(list_1[i])==3:
            a1=answer_dict[i]
            break
    
    c1,c2,c3,c4,c5=list_1[0][1],list_1[1][1],list_1[2][1],list_1[3][1],list_1[4][1]
    x1,x2,x3,x4,x5=list_1[0][0],list_1[1][0],list_1[2][0],list_1[3][0],list_1[4][0]

    stem=stem.format(x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a1=a1)
    comment=comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)

    return stem,answer,comment

#2-1-3-02
def systemequations213_Stem_002():
    stem= "함수 $$수식$$f LEFT ( x RIGHT ) `=`{a1}x`-`1$$/수식$$   에 대하여$$수식$$ {a2}`f LEFT ( {a3} RIGHT ) ``-{a4}`f LEFT ( {a5} RIGHT ) `$$/수식$$  의 값은? \n\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n\n"
    answer= "(답)\n{an}\n"
    comment = "(해설)\n"\
              "$$수식$${a2}`f LEFT ( {a3} RIGHT ) `-`{a4}`f LEFT ( {a5} RIGHT ) `=`{a2}` TIMES ` LEFT ( {a1}` TIMES `{a3}`-`1 RIGHT ) `-`{a4}` TIMES ` LEFT ( {a1}` TIMES `{a5}`-`1 RIGHT )$$/수식$$\n" \
              "$$수식$$=`{c1}`-`{c2}`=`{a}$$/수식$$\n" \
              "따라서 구하는 값은 $$수식$${a}$$/수식$$ 이다.\n\n" 
    a1=random.randint(2,10)
    a2=random.randint(2,7)
    a3=random.randint(2,8)
    a4=random.randint(2,7)
    a5=random.randint(2,6)
    c1=a2*(a1*a3-1)
    c2=a4*(a1*a5-1)
    a=c1-c2
    can=made_answer_cand_1(a)
    random.shuffle(can)
    x1,x2,x3,x4,x5=can[0],can[1],can[2],can[3],can[4]
    for i in range(5):
        if a==can[i]:
            an=answer_dict[i]
            break
        

    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(an=an)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,a=a)

    return stem,answer,comment

#2-1-3-03
def systemequations213_Stem_003():
    stem= "다음 중 $$수식$$y`$$/수식$$가 $$수식$$x`$$/수식$$의 함수인 것은 모두 몇 개 인가?\n\n$$표$$㈀ 자연수 $$수식$$x`$$/수식$$를 $$수식$${x1}$$/수식$$(으)로 나눈 나머지 $$수식$$y`$$/수식$$\n㈁ 자연수$$수식$$x`$$/수식$$ 보다 작은 자연수$$수식$$y`$$/수식$$\n㈂ $$수식$$x`$$/수식$$보다 $$수식$${x2}$$/수식$$만큼 큰 수$$수식$$y`$$/수식$$\n㈃ 몸무게가 $$수식$$x`` rm km`$$/수식$$인 사람의 키$$수식$$y`` rm cm`$$/수식$$\n㈄ 시계의 긴 바늘이 $$수식$$x`$$/수식$$분 동안 회전한 각의 크기$$수식$$y DEG$$/수식$$\n㈅ 시속 $$수식$${x3} rm ``km`$$/수식$$로 달리는 승용차가 $$수식$$x`$$/수식$$시간 동안 달린 거리$$수식$$y rm``km`$$/수식$$\n㈆ 한 권에 $$수식$${x4}$$/수식$$원 하는 공책$$수식$$x`$$/수식$$ 권을 살 때 지불하는 금액 $$수식$$y`$$/수식$$원\n$$/표$$\n①$$수식$${a1}$$/수식$$개	②$$수식$${a2}$$/수식$$ 개	③$$수식$${a3}$$/수식$$ 개\n④$$수식$${a4}$$/수식$$ 개	⑤$$수식$${a5}$$/수식$$ 개\n"
    answer="(정답)\n{a}"
    comment= "(해설)\n"\
             "㈀ 자연수 $$수식$$x`$$/수식$$를 $$수식$${x1}$$/수식$$로 나누면 나머지 는 {c1}중 하나로 정해지므로 $$수식$$y`$$/수식$$는$$수식$$x`$$/수식$$ 의 함수이다.\n"\
             "㈁ $$수식$$x`=`4`$$/수식$$  일 때 $$수식$$4`$$/수식$$보다 작은 자연수 는 $$수식$$1$$/수식$$,$$수식$$2$$/수식$$,$$수식$$3$$/수식$$ 이다. 즉,$$수식$$x`$$/수식$$ 의 값이 $$수식$$4`$$/수식$$일 때 $$수식$$y`$$/수식$$의 값이 하나로 정해지지 않으므로 $$수식$$y`$$/수식$$는 $$수식$$x`$$/수식$$의 함수가 아니다.\n"\
             "㈂$$수식$$y`=`x`+`{x2}`$$/수식$$\n"\
             "㈃ 몸무게가 $$수식$$x``rm kg`$$/수식$$인 사람의 키$$수식$$y``rm cm$$/수식$$ 가 $$수식$$2`$$/수식$$개 이상 정해지는 경우도 있으므로 $$수식$$y`$$/수식$$는 $$수식$$x`$$/수식$$의 함수가 아니다.\n"\
             "㈄$$수식$$y`=`6x`$$/수식$$   ㈅ $$수식$$ y`=`{x3}x`$$/수식$$    ㈆$$수식$$y`=`{x4}x`$$/수식$$\n"\
             "따라서 $$수식$$y`$$/수식$$가 $$수식$$x`$$/수식$$의 함수인 것은 ㈀, ㈂, ㈄, ㈅, ㈆의 $$수식$$5`$$/수식$$개이다.\n\n"
    x1=random.randint(1,10)
    x2=random.randint(1,5)
    x3=random.randint(100,150)
    x4=random.randrange(300,500,50)
    c1=""
    for i in range(x1):
        c1=c1+","+"$$수식$$`{i}$$/수식$$ ".format(i=i)
    a_list=made_answer_cand_1(5)
    random.shuffle(a_list)
    for j in range(5):
        if a_list[j]==5:
            a=answer_dict[j]

    a1,a2,a3,a4,a5=a_list[0],a_list[1],a_list[2],a_list[3],a_list[4]    

    stem=stem.format(x1=x1,x2=x2,x3=x3,x4=x4,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
    answer=answer.format(a=a)
    comment=comment.format(x1=x1,x2=x2,x3=x3,x4=x4,c1=c1)

    return stem,answer,comment

#2-1_3_04
def systemequations213_Stem_004():
    stem= "다음 중 $$수식$$y`$$/수식$$가 $$수식$$x`$$/수식$$의 함수가 아닌 것은?\n\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "① {c1}\n" \
             "② {c2}\n" \
             "③ {c3}\n" \
             "④ {c4}\n\n" \
             "⑤ {c5}\n\n"\
             "따라서  $$수식$$y`$$/수식$$가 $$수식$$x`$$/수식$$의 함수가 아닌 것은 {a}이다.\n\n"
    a1=random.randint(2,9)
    a2=2*a1
    cc1=""
    for i in range(a2):
        if i==0:
            pass
        elif i==1:
            cc1=cc1+"$$수식$${i}$$/수식$$".format(i=i)
        else:
            cc1=cc1+","+"$$수식$${i}$$/수식$$".format(i=i)
    a3=random.randint(20,100)
    a4=random.randrange(400,800,50)
    a5=random.randint(20,50)
    s1="자연수 $$수식$$`x$$/수식$$의 $$수식$${a1}$$/수식$$배 보다 작은 자연수 $$수식$$y`$$/수식$$".format(a1=a1)
    s2="$$수식$$x`=`2$$/수식$$  일 때,$$수식$$2$$/수식$$ 의 $$수식$${a1}$$/수식$$배인 $$수식$${a2}$$/수식$$보다 작은 자연수 $$수식$$y`$$/수식$$는 $$수식$${cc1}$$/수식$$이다. 즉$$수식$$x`$$/수식$$ 의 값이 $$수식$$2$$/수식$$일 때 $$수식$$y`$$/수식$$의 값이 하나로 정해지지 않으므로 $$수식$$y`$$/수식$$는 $$수식$$x`$$/수식$$의 함수가 아니다.".format(a1=a1,a2=a2,cc1=cc1)  
    cand1_answer=[s1,s2,1]
        
    s3="시속$$수식$${a3}``rm km $$/수식$$로 $$수식$$x`$$/수식$$시간 동안 걸은 거리$$수식$$y``rm km`$$/수식$$ ".format(a3=a3)
    s4="$$수식$$y`=`{a3}x$$/수식$$".format(a3=a3)
    cand2=[s3,s4]
        
    cand3=["한 변의 길이가 $$수식$$x``rm cm`$$/수식$$인 정삼각형의 둘레의 길이 $$수식$$y``rm cm`$$/수식$$","$$수식$$y`=`3x$$/수식$$"]
        
    s5="연필 한 자루의 가격이 $$수식$${a4}$$/수식$$원일 때, 연필$$수식$$x`$$/수식$$자루의 가격 $$수식$$y`$$/수식$$원".format(a4=a4)
    s6="$$수식$$y`=`{a4}x`$$/수식$$".format(a4=a4)
    cand4=[s5,s6]
        
    s7="넓이가$$수식$${a5}``rm cm^{tmp}$$/수식$$ 인 평행사변형의 밑변의 길이가 $$수식$$x``rm cm$$/수식$$일 때, 높이$$수식$$y``rm cm$$/수식$$ ".format(a5=a5,tmp=2)
    s8="$$수식$$y`=`{a5}OVER{x}$$/수식$$".format(a5=a5,x="x")
    cand5=[s7,s8]
        
    cand6=["한개에 $$수식$$x`$$/수식$$원인 음료수$$수식$$4`$$/수식$$개 의 값 $$수식$$y`$$/수식$$원","$$수식$$y``=``4x`$$/수식$$"]
    cand7=["반지름의 길이가 $$수식$$ x`` rm cm`$$/수식$$인 원의 넓이 $$수식$$y`` rm cm ^{2} `$$/수식$$","(원의 넓이)$$수식$$=` pi ` TIMES `$$/수식$$(반지름의 길이)제곱에서 $$수식$$ y`=pix^2`$$/수식$$"] 
    cand8_answer=["$$수식$$y`$$/수식$$는 자연수 $$수식$$ x` $$/수식$$의 배수의 개수","자연수 $$수식$$3$$/수식$$의 양의 배수의 개수는 알 수 없다.",1]
    cand_list=[cand2,cand3,cand4,cand5,cand6,cand7]
    answer_list=[cand1_answer,cand8_answer]
    list1=random.sample(cand_list,4)
    list2=random.sample(answer_list,1)
    list1.append(list2[0])
    random.shuffle(list1)
    for i in range(5):
        if len(list1[i])==3:
            a=answer_dict[i]
            break
    c1,c2,c3,c4,c5=list1[0][1],list1[1][1],list1[2][1],list1[3][1],list1[4][1]
    x1,x2,x3,x4,x5=list1[0][0],list1[1][0],list1[2][0],list1[3][0],list1[4][0]

    stem=stem.format(x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,a=a)
    return stem,answer,comment


#2-1-3-05
def systemequations213_Stem_005():
    stem= "함수 $$수식$$f(x)$$/수식$$  가 $$수식$$f(x)`=`{x1}x`-`{x2}`$$/수식$$      일 때, $$수식$${{f LEFT ({x3} RIGHT )`-`f LEFT ( {x4} RIGHT )}}over{h}$$/수식$$        의 값은?\n\n"\
          "①$$수식$${a1}$$/수식$$  ②$$수식$${a2}$$/수식$$  ③$$수식$${a3}$$/수식$$\n④$$수식$${a4}$$/수식$$  ⑤$$수식$${a5}$$/수식$$\n\n "
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$f(x)`=`{x1}x`-`{x2}`$$/수식$$      에서\n"\
             "$$수식$${{f LEFT ( {x3} RIGHT )-f LEFT ( {x4} RIGHT )}}over{h}`=`{{{x1}` TIMES `{x3}`-`{x2}`-`  ( {x1}` TIMES ` {x4} `-`{x2} )}} over {h} `$$/수식$$\n"\
             "$$수식$${{{r1}`-`{r2}}}over{h}`=`{r3}$$/수식$$\n\n"
             
    
    x1=random.randrange(2,6,2)
    x2=random.randrange(2,8,2)
    x3=random.randint(1,5)
    x4=random.randint(1,5)
    if x3==x4:
        while 1:
            x4=random.randint(1,5)
            if x3!=x4:
                break
    r1=x1*x3-x2
    r2=x1*x4-x2
    r3=int((r1-r2)/2)
    ans_li=made_answer_cand_1(r3)
    random.shuffle(ans_li)
    for i in range(5):
        if ans_li[i] == r3:
            a=answer_dict[i]
            break
    a1,a2,a3,a4,a5=ans_li[0],ans_li[1],ans_li[2],ans_li[3],ans_li[4]
    
    stem=stem.format(x1=x1,x2=x2,x3=x3,x4=x4,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,h=2)
    answer=answer.format(a=a)
    comment=comment.format(x1=x1,x2=x2,x3=x3,x4=x4,h=2,r1=r1,r2=r2,r3=r3)

    return stem,answer,comment    

#2-1-3-06
def systemequations213_Stem_006():
    stem= "함수$$수식$$x`$$/수식$$ 를 {a1}로 나누었을 때의 나머지를 $$수식$$y`$$/수식$$라 하고$$수식$$y`=`f LEFT ( x RIGHT )$$/수식$$ 로 나타낼 때,$$수식$${a2}f LEFT ( {a3} RIGHT )`TIMES`f LEFT ( {a4} RIGHT ) $$/수식$$ 의 값은?\n"\
          "①$$수식$${x1}$$/수식$$ 	②$$수식$${x2}$$/수식$$ 	③$$수식$${x3}$$/수식$$ \n④$$수식$${x4}$$/수식$$ 	⑤$$수식$${x5}$$/수식$$\n\n "
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${a3}`=`{a1}`TIMES`{c1}`+`{c2}$$/수식$$이므로$$수식$$f LEFT ( {a3} RIGHT )`=`{c3}$$/수식$$\n"\
             "$$수식$${a4}`=`{a1}`TIMES`{c4}`+`{c5}$$/수식$$이므로$$수식$$f LEFT ( {a4} RIGHT )`=`{c6}$$/수식$$\n"\
             "$$수식$$THEREFORE ~{a2}f({a3})`TIMES`f({a4})`=`{a2}`TIMES`{c3}`TIMES`{c6}`=`{c7}$$/수식$$\n"\
             "따라서 구하는 값은 $$수식$${c7}$$/수식$$이다.\n\n"
    
    a1=random.sample([2,4,7,8,9],1)[0]
    a2=random.randint(2,10)
    a3=random.randint(6,12)
    a4=random.randint(6,12)
    if a3==a4:
        while 1:
            a4=random.randint(6,12)
            if a3!=a4:
                break
    c1=a3//a1
    c2=a3%a1
    c3=c2
    c4=a4//a1
    c5=a4%a1
    c6=c5
    c7=a2*c3*c6

    a_li=made_answer_cand_1(c7)
    random.shuffle(a_li)
    x1,x2,x3,x4,x5=a_li[0],a_li[1],a_li[2],a_li[3],a_li[4]
    tmp=a_li.index(c7)
    a=answer_dict[tmp]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7)
    return stem,answer,comment

#2-1-3-07
def systemequations213_Stem_007():
    stem= "함수 $$수식$$f LEFT ( x RIGHT )`=`{a1}OVER{x}$$/수식$$에 대하여$$수식$$f LEFT ( {t}OVER{a2} RIGHT )`=`a$$/수식$$,$$수식$$f LEFT ( {a3} RIGHT )`=`b$$/수식$$ 라 할 때,$$수식$$f LEFT ( a`+`b RIGHT )$$/수식$$ 의 값은?\n"\
          "①$$수식$${x1}$$/수식$$ 	②$$수식$${x2}$$/수식$$ 	③$$수식$${x3}$$/수식$$ \n④$$수식$${x4}$$/수식$$ 	⑤$$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$f LEFT ( x RIGHT )`=`{a1}OVER{x}$$/수식$$에서\n\n"\
             "$$수식$$f LEFT ( {t}OVER{a2} RIGHT )`=`{a1}`DIVIDE`{{{t}OVER{a2}}}`=`{a1}`TIMES`{a2}`=`{c1}$$/수식$$\n\n"\
             "$$수식$$THEREFORE ~ a`=`{c1}$$/수식$$\n"\
             "$$수식$$f LEFT ( {a3} RIGHT )`=`{a1}OVER{a3}`=`{c2}`THEREFORE ~b`=`{c2}$$/수식$$\n\n"\
             "$$수식$$THEREFORE ~ f LEFT ( a`+`b RIGHT )`=`f LEFT ({c1}+({c2}) RIGHT )$$/수식$$\n"\
             "$$수식$$=f LEFT ( {c3} RIGHT )`=`{a1}OVER{c3}`=`$$/수식$${c4}\n\n"\
             "따라서 구하는 값은 $$수식$${c4}$$/수식$$이다.\n\n"

    a1=random.randrange(8,20,4)
    a2=random.randrange(2,8,2)
    a3=random.randrange(-4,4,2)
    t=random.randint(1,2)
    if a3==0:
        while 1:
            a3=random.randrange(-4,4,2)
            if a3!=0:
                break
    c1=a1*a2
    c2=int(a1/a3)
    c3=c1+c2
    if a1/c3!=0:
        g=gcd(a1,c3)
        a_tmp=int(a1/g)
        c_tmp=int(c3/g)
    c4="$$수식$${} OVER {}$$/수식$$".format(a_tmp,c_tmp)
    a_li=made_answer_cand_2(a_tmp,c_tmp)
    random.shuffle(a_li)
    a=answer_dict[a_li.index(c4)]
    x1,x2,x3,x4,x5=a_li[0],a_li[1],a_li[2],a_li[3],a_li[4]
    t=1
    stem=stem.format(a1=a1,a2=a2,a3=a3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,t=t,x="x")
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,c1=c1,c2=c2,c3=c3,c4=c4,t=t,x="x")

    return stem,answer,comment
    
#2-1-3-08
def systemequations213_Stem_008():
    stem= "함수 $$수식$$f LEFT ( x RIGHT )`=`{a1}`TIMES`$$/수식$$(자연수 $$수식$$x`$$/수식$$를 $$수식$${a2}$$/수식$$로 나눈 나머지)라 할 때,$$수식$$f(1)`+`f(2)`+`f(3)`+`` CDOTS ``+`f({a3m1})`+`f({a3})`$$/수식$$              의 값은? \n"\
          "①$$수식$${x1}$$/수식$$ 	  ②$$수식$${x2}$$/수식$$ 	  ③$$수식$${x3}$$/수식$$ \n④$$수식$${x4}$$/수식$$ 	  ⑤$$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "{c1}\n"\
             "$$수식$$THEREFORE~f(1)`+`f(2)`+`f(3)`+`` CDOTS ``+`f({a3m1})`+`f({a3})`$$/수식$$\n"\
             "$$수식$$`=`{{10}}TIMES{a1}TIMES({{1`+`2`+`}}CDOTS{a2m1})$$/수식$$\n"\
             "따라서 구하는 값은 $$수식$${c2}$$/수식$$\n\n"
    a1=random.randint(2,5)
    a2=random.sample([2,4,5,7,8,9],1)[0]
    a3=10*a2
    a2m1=a2-1
    a3m1=a3-1
    c1=""
    for i in range(1,a2+1):
        if i==a2:
            c1=c1+"\n$$수식$$f({one})`+`f({two})`+`f({th})`=`CDOTS`=`f({ni})`=`{a1}TIMES{pl1}$$/수식$$".format(one=i,two=i+1*a2,th=i+2*a2,ni=i+9*a2,a1=a1,pl1=0)
        else:
            c1=c1+"\n$$수식$$f({one})`+`f({two})`+`f({th})`=`CDOTS`=`f({ni})`=`{a1}TIMES{pl1}$$/수식$$".format(one=i,two=i+1*a2,th=i+2*a2,ni=i+9*a2,a1=a1,pl1=i)
    c2=10*a1*int((a2-1)*a2/2)
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a3m1=a3m1,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a2m1=a2m1,a3m1=a3m1,c1=c1,c2=c2)
    return stem,answer,comment

#2-1-3-09
def systemequations213_Stem_009():
    stem= "$$수식$$f(x)`=`{a1}x`-`a$$/수식$$      에 대하여가$$수식$$f({a2})`=`{a3}$$/수식$$    일 때,\n"\
          "$$수식$${a4}f({a5})`+`f({a6})`=`f(k)$$/수식$$          이다. 이때 $$수식$${a1}k$$/수식$$  의 값을 구하시오\n\n"
    answer= "(정답)\n{a}"
    comment= "(해설)\n"\
             "$$수식$$f({a2})`=`{c1}`-`a`=`{a3}$$/수식$$       이므로 $$수식$$a`=`{c2}$$/수식$$\n"\
             "즉,$$수식$$f(x)`=`{a1}x`-`{c2}$$/수식$$      이다.\n"\
             "$$수식$${a4}f({a5})`+`f({a6})`=`f(k)$$/수식$$           에서\n"\
             "$$수식$$f({a5})`=`{a1}`TIMES`{a5}`-`{c2}={c3}`,~f({a6})`=`{a1}`TIMES`{a6}`-`{c2}`=`{c4}$$/수식$$\n"\
             "$$수식$$f(k)={a1}k`-`{c2}$$/수식$$      이므로 \n"\
             "$$수식$${a4}`TIMES`{l3}{c3}{r3}`+`{l4}{c4}{r4}`=`{a1}k`-`{c2}$$/수식$$      이므로\n"\
             "$$수식$$THEREFORE ~{c5}`+`{c2}`=`{a1}k$$/수식$$\n"\
             "(힌트) $$수식$$f({a2})`=`{a3}$$/수식$$      {proa3} 이용하여 a의 값을 구한 다음, $$수식$$f({a5})`,~f({a6})$$/수식$$       의 값을 각각 구한다.\n\n"
    a1=random.randint(3,5)
    a2=random.randint(3,5)
    a3=random.randint(5,7)
    a4=random.randint(2,5)*a1
    a5=random.randint(6,7)
    a6=random.randint(6,7)
    while a2==a5 or a2==a6 or a5==a6:
        a1=random.randint(3,5)
        a2=random.randint(3,5)
        a3=random.randint(5,9)
        a4=random.randint(2,5)*a1
        a5=random.randint(2,4)
        a6=random.randint(2,5)
    c1=a1*a2
    c2=c1-a3
    c3=a1*a5-c2
    c4=a1*a6-c2
    c5=a4*c3
    a=c5+c2
    proa3=proc_jo(a3,3)
    if c3<0:
        l3="("
        r3=")"
    else:
        l3=""
        r3=""
    if c4<0:
        l4="("
        r4=")"
    else:
        l4=""
        r4=""
    
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,l3=l3,r3=r3,l4=l4,r4=r4,proa3=proa3)

    return stem,answer,comment
#2-1-3-10
def systemequations213_Stem_010():
    stem= "함수$$수식$$y=f(x)$$/수식$$    는 자연수$$수식$$a,~b``$$/수식$$  에 대하여$$수식$$f(a`+`b)`=`f(a)`+`f(b)`+`ab$$/수식$$            를 만족시킨다. $$수식$$f(1)`=`{a1}$$/수식$$     일 때,\n"\
          "$$수식$$f(1)`+`f(2)`+``CDOTS``+`f({a2})$$/수식$$        의 값은?\n"\
          "①$$수식$${x1}$$/수식$$ 	②$$수식$${x2}$$/수식$$ 	③$$수식$${x3}$$/수식$$ \n④$$수식$${x4}$$/수식$$ 	⑤$$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$f(1)={a1}$$/수식$$    이므로\n"\
             "{c1}\n"\
             "{c2}\n"\
             "{c3}\n"\
             "(힌트)주어진 식을 만족시킬 수 있도록 $$수식$$f(1),f(2),CDOTS`,f({a2})$$/수식$$      의 값을 차례로 구한다.\n\n"

    a1=random.randint(1,3)
    a2=random.randint(7,10)
    c1=""
    tmp=a1
    score=a1
    c3="$$수식$$=`{a1}$$/수식$$".format(a1=a1)
    for i in range(2,a2+1):
        tmp=tmp+a1+i-1
        score=score+tmp
        c1=c1+"$$수식$$f({})`=`f(1`+`{})`=`f(1)`+`f({})`+`{}`=`{}$$/수식$$\n".format(i,i-1,i-1,i-1,tmp)
        c3=c3+"$$수식$$`+`{tmp}$$/수식$$".format(tmp=tmp)
    c2="$$수식$$THEREFORE ~f(1)`+`f(2)`+`f(3)`+``CDOTS``f({a2})$$/수식$$".format(a2=a2)
    c3=c3+"$$수식$$`=`{score}$$/수식$$".format(score=score)
    a_li=made_answer_cand_3(score)
    random.shuffle(a_li)
    a=answer_dict[a_li.index(score)]
    x1,x2,x3,x4,x5=a_li[0],a_li[1],a_li[2],a_li[3],a_li[4]
    stem=stem.format(a1=a1,a2=a2,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,c1=c1,c2=c2,c3=c3)

    return stem,answer,comment




#2-1-3-11
def systemequations213_Stem_011():
    stem= "다음중 $$수식$$y`$$/수식$$가$$수식$$x`$$/수식$$에 대한 일차함수인 것은?\n"\
          "① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n\n"
    answer= "(정답)\n{a}"
    comment= "(해설)\n" \
             "① {c1}\n\n" \
             "② {c2}\n\n" \
             "③ {c3}\n\n" \
             "④ {c4}\n\n" \
             "⑤ {c5}\n\n"
    a1=random.randint(2,5)
    a2=random.randint(2,6)
    s1="한 자루에 $$수식$$x`$$/수식$$원인 볼펜 $$수식$${a1}$$/수식$$자루와 한 자루에 $$수식$$y`$$/수식$$원인 연필 $$수식$${a2}$$/수식$$자루의 값의 합".format(a1=a1,a2=a2)
    col1="$$수식$${a1}x`+`{a2}y$$/수식$$   (다항식)".format(a1=a1,a2=a2)
    cand1=[s1,col1]

    a3=random.randint(2,5)
    s2="어떤 직사각형의 가로의 길이를 $$수식$$x``rm cm`$$/수식$$, 세로의 길	이를 $$수식$$y``rm cm`$$/수식$$라 할 때, 세로의 길이는 가로의 길이보다 $$수식$${a3} rm cm`$$/수식$$가 길다. ".format(a3=a3)
    col2="$$수식$$y`=`x`+`{a3}$$/수식$$".format(a3=a3)
    cand2_answer=[s2,col2]

    a4=random.randint(10,15)
    a5=100*a4
    s3="$$수식$$x``%`$$/수식$$  의 소금물 $$수식$$y``rm g`$$/수식$$속에 들어있는 소금의 양은 $$수식$${a4}``rm g`$$/수식$$이다.".format(a4=a4)
    col3="$$수식$${a4}OVER{h}`TIMES`{t}`=`x THEREFORE~y`=`{a5}OVER{l}$$/수식$$".format(a4=a4,a5=a5,h="y",t="x",l="x")
    cand3=[s3,col3]

    a6=random.randint(2,5)
    s4="어떤 수 $$수식$$x`$$/수식$$의 $$수식$${a6}$$/수식$$배는 $$수식$$y`$$/수식$$보다 작다. ".format(a6=a6)
    col4="$$수식$${a6}x`&lt;`y$$/수식$$   (부등식)".format(a6=a6)
    cand4=[s4,col4]

    a7=random.randrange(2500,5000,500)
    s5="한 권에 $$수식$$x`$$/수식$$원인 공책 $$수식$$y`$$/수식$$권의 값은 $$수식$${a7}$$/수식$$ 원이다. ".format(a7=a7)
    col5="$$수식$$xy`=`{a7} THEREFORE~ y`=`{a7}OVER{t}$$/수식$$".format(a7=a7,t="x")
    cand5=[s5,col5]
    cand=[cand1,cand2_answer,cand3,cand4,cand5]
    random.shuffle(cand)
    a=answer_dict[cand.index(cand2_answer)]
    x1,x2,x3,x4,x5=cand[0][0],cand[1][0],cand[2][0],cand[3][0],cand[4][0]
    c1,c2,c3,c4,c5=cand[0][1],cand[1][1],cand[2][1],cand[3][1],cand[4][1]

    stem=stem.format(x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    return stem,answer,comment

#2-1-3-12
def systemequations213_Stem_012():
    stem= "일차함수$$수식$$f(x)`=`ax`+`b$$/수식$$      에서 $$수식$$f(x`+`{a1})`-`f(x)`=`{a2}$$/수식$$         이고,$$수식$$f({a3})`=`{a4}$$/수식$$      일 때,\n $$수식$$a`+`b$$/수식$$    의 값은? (단,$$수식$$a$$/수식$$ ,$$수식$$b$$/수식$$ 는 상수이다.)\n"\
          "①$$수식$${x1}$$/수식$$ 	②$$수식$${x2}$$/수식$$ 	③$$수식$${x3}$$/수식$$ \n④$$수식$${x4}$$/수식$$ 	⑤$$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$f(x)`=`ax`+`b$$/수식$$     에서\n"\
             "$$수식$$f({a3})`=`{a3}a`+`b={a4}``CDOTS CDOTS ㉠$$/수식$$\n"\
             "$$수식$$f(x`+`{a1})`=`a(x`+`{a1})`+`b$$/수식$$            ,$$수식$$f(x)`=`ax`+`b$$/수식$$     이므로\n"\
             "$$수식$$f(x`+`{a1})`-`f(x)`=`ax`+`{a1}a`+`b`-`(ax`+`b)`=`{a1}a={a2}``CDOTS CDOTS㉡$$/수식$$\n"\
             "㉠, ㉡에서 $$수식$$a`=`{c1},b`=`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`+`b`=`{c3}$$/수식$$\n\n"
    a1=random.randrange(3,7)
    tmp=random.randint(2,5)
    a2=tmp*a1
    a3=random.randint(-5,10)
    a4=random.randint(1,10)
    c1=tmp
    c2=a4-a3*tmp
    c3=c1+c2
    a_li=made_answer_cand_1(c3)
    random.shuffle(a_li)
    a=answer_dict[a_li.index(c3)]
    x1,x2,x3,x4,x5=a_li[0],a_li[1],a_li[2],a_li[3],a_li[4]

    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3)
    return stem,answer,comment

#2-1-3-13
def systemequations213_Stem_013():
    stem ="다음 중 $$수식$$y`$$/수식$$가 $$수식$$x`$$/수식$$에 대한 일차함수가 아닌 것을 모두 고르면? (정답 $$수식$$2$$/수식$$개)\n"\
          "① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n\n"
    answer= "(정답)\n{a}, {b}\n"
    comment= "(해설)\n" \
             "① {c1}\n\n" \
             "② {c2}\n\n" \
             "③ {c3}\n\n" \
             "④ {c4}\n\n" \
             "⑤ {c5}\n\n"
    a1=random.randint(2,6)
    s1="밑변의 길이가 $$수식$$x``rm cm`$$/수식$$이고 높이가 $$수식$${a1}``rm cm`$$/수식$$인 삼각형의 넓이는$$수식$$y``rm cm^{t}$$/수식$$ 이다.".format(a1=a1,t=2)
    col1="$$수식$$y`=`{{{t1}over{t2}}}TIMES{a1}x$$/수식$$".format(t1=1,t2=2,a1=a1)
    cand1=[s1,col1]
    
    
    a2=random.randint(15,30)
    s2="넓이가 $$수식$${a2}``rm cm^{t}`$$/수식$$인 직사각형의 가로의 길이가 $$수식$$x``rm cm`$$/수식$$일 때, 세로의 길이는$$수식$$y``rm cm`$$/수식$$ 이다. ".format(a2=a2,t=2)
    col2="$$수식$$xy`=`{a2}$$/수식$$".format(a2=a2)
    cand2_answer=[s2,col2,1]


    s3="한 변의 길이가 $$수식$$x``rm cm`$$/수식$$인 정삼각형의 둘레의 길이는 $$수식$$y``rm cm`$$/수식$$이다. "
    col3="$$수식$$y`=`3x$$/수식$$"
    cand3=[s3,col3]


    a3=random.randrange(200,500,100)
    a4=random.randrange(300,600,100)
    a5=random.randrange(1800,5000,100)
    s4="한 권에 $$수식$${a3}$$/수식$$원 하는 노트 $$수식$$x`$$/수식$$권과 한 자루에 $$수식$${a4}$$/수식$$원 하는 연필 $$수식$$y`$$/수식$$자루의 값은 $$수식$${a5}$$/수식$$원이다.".format(a3=a3,a4=a4,a5=a5)
    col4="$$수식$${a3}x`+`{a4}y`=`{a5}$$/수식$$".format(a3=a3,a4=a4,a5=a5)
    cand4=[s4,col4]


    a6=random.randrange(100,200,10)
    s5="시속 $$수식$$x``rm km`$$/수식$$로 달리는 자동차가 $$수식$$y`$$/수식$$시간 동안 달리는 거리는 $$수식$${a6}``rm km`$$/수식$$이다.".format(a6=a6)
    col5="$$수식$$xy={a6}$$/수식$$".format(a6=a6)
    cand5_answer=[s5,col5,1]

    a_li=[cand1,cand2_answer,cand3,cand4,cand5_answer]
    random.shuffle(a_li)
    a=answer_dict[a_li.index(cand2_answer)]
    b=answer_dict[a_li.index(cand5_answer)]
    if a_li.index(cand2_answer)>a_li.index(cand5_answer):
        a,b=b,a

    x1,x2,x3,x4,x5=a_li[0][0],a_li[1][0],a_li[2][0],a_li[3][0],a_li[4][0]
    c1,c2,c3,c4,c5=a_li[0][1],a_li[1][1],a_li[2][1],a_li[3][1],a_li[4][1]

    stem=stem.format(x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a,b=b)
    comment=comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)

    return stem,answer,comment

#2-1-3-14
def systemequations213_Stem_014():
    stem= "고도가 $$수식$$rm 1``km`$$/수식$$씩 높아질 때마다 기온은 $$수식$$rm {a1}`` CENTIGRADE$$/수식$$씩 내려간다고 한다. 지면의 기온이 $$수식$$rm {a2}``CENTIGRADE$$/수식$$일 때, 고도가 $$수식$$x``rm km`$$/수식$$인 지점의 기온을 $$수식$$y``rm CENTIGRADE$$/수식$$라 하자. 옳은 것을 보기에서 모두 고른 것은? \n"\
          "$$표$$보기\n"\
          "(ㄱ){d1}\n(ㄴ){d2}\n(ㄷ){d3}\n(ㄹ){d4}$$/표$$\n"\
          "① {x1}		② {x2}	③ {x3}\n④ {x4} ⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "{c1}\n"\
             "{c2}\n"\
             "{c3}\n\n"
             
    a1=random.randint(3,6)
    a2=random.randrange(20,50,10)
    a3=random.sample([3*a1,a2-3*a1,a2+3*a1],1)[0]
    d1=" 고도가$$수식$$x``rm km`$$/수식$$ 인 지점의 기온은 지면의 기온보다 $$수식$${a1}x``CENTIGRADE$$/수식$$만큼 낮다.".format(a1=a1)
    d2=" $$수식$$x`$$/수식$$와  $$수식$$y`$$/수식$$사이의 관계를 식으로 나타내면 $$수식$$y`=`{a1}x`+`{a2}$$/수식$$    이다.".format(a1=a1,a2=a2)
    d3=" $$수식$$y`$$/수식$$는 $$수식$$x`$$/수식$$에 대한 일차함수이다."
    d4=" 고도가 $$수식$$rm3``km`$$/수식$$인 지점의 기온은 $$수식$${a3}``CENTIGRADE$$/수식$$이다.".format(a3=a3)
    c1="(ㄴ)$$수식$$y`=`-{a1}x`+`{a2}$$/수식$$".format(a1=a1,a2=a2)
    c2="(ㄹ)$$수식$$x`=`3$$/수식$$ 일 때,$$수식$$y`=`{c1}$$/수식$$  이므로 고도가 $$수식$$rm``3 km`$$/수식$$인\n 지점의 기온은$$수식$$rm``{c2} CENTIGRADE$$/수식$$이다.".format(c1=a2-a1*3,c2=a2-3*a1)
    c3="따라서 옳은것은 (ㄱ),(ㄷ)이다."

    an=["(ㄱ), (ㄴ)","(ㄱ), (ㄷ)","(ㄷ), (ㄹ)","(ㄱ), (ㄴ), (ㄷ)","(ㄱ), (ㄴ), (ㄷ), (ㄹ)"]
    random.shuffle(an)
    a=answer_dict[an.index("(ㄱ), (ㄷ)")]
    x1,x2,x3,x4,x5=an[0],an[1],an[2],an[3],an[4]

    stem=stem.format(a1=a1,a2=a2,d1=d1,d2=d2,d3=d3,d4=d4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(c1=c1,c2=c2,c3=c3)

    return stem,answer,comment

#2-1-3-15
def systemequations213_Stem_015():
    stem= "$$수식$$y`=`{a1}x(ax`-`{a2})`+`bx`-`{a3}$$/수식$$         이 $$수식$$x`$$/수식$$에 대한 일차함수가 되도록 하는 상수 $$수식$$a,b$$/수식$$  의 조건으로 옳은 것은?\n"\
          "① {x1}		② {x2}	    ③ {x3}\n④ {x4}           ⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`=`{a1}x(ax`-`{a2})`+`bx`-`{a3}$$/수식$$         에서\n"\
             "$$수식$$y`=`{a1}ax^{t}`+`(b-{c1})x`-`{a3}$$/수식$$\n"\
             "위의 함수가 일차함수이려면\n"\
             "$$수식$${a1}a`=`0,~b-{c1}`!=`0$$/수식$$\n"\
             "$$수식$$THEREFORE~a`=`0,~b`!=`{c1}$$/수식$$\n\n"
    a1=random.randint(2,5)
    a2=random.randint(3,5)
    a3=random.randint(3,5)
    c1=a1*a2
    s1="$$수식$$a`=`0,~b`!=`{c1}$$/수식$$".format(c1=c1)
    s2="$$수식$$a`!=0`,~b`!=`{c1}$$/수식$$".format(c1=c1)
    s3="$$수식$$a`!=`0,~b`=`{c1}$$/수식$$".format(c1=c1)
    a_li=["$$수식$$a`=`0,~b`=`0$$/수식$$","$$수식$$a`!=`0,~b`=`0$$/수식$$",s1,s2,s3]
    random.shuffle(a_li)
    a=answer_dict[a_li.index(s1)]
    x1,x2,x3,x4,x5=a_li[0],a_li[1],a_li[2],a_li[3],a_li[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,t=2,c1=c1)

    return stem,answer,comment

#2-1-3-16
def systemequations213_Stem_016():
    stem= "일차함수$$수식$$f LEFT ( x RIGHT )`=`ax`+`{a1}$$/수식$$   에서$$수식$$~f LEFT ( {a2} RIGHT )`=`{a3}$$/수식$$   일 때, $$수식$$f LEFT ( {a4} RIGHT )`{sa5}f LEFT ( {a6} RIGHT )$$/수식$$    의 값은?\n"\
          "① {x1}		② {x2}	   ③ {x3}\n④ {x4}        ⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$f LEFT ( x RIGHT )`=`ax`+`{a1}$$/수식$$   에서\n"\
             "$$수식$$f LEFT ( {a2} RIGHT )`=`{l2}{a2}{r2}TIMES{aaa}`+`{a1}`=`{a3}~THEREFORE ~ a={c1}$$/수식$$\n"\
             "$$수식$$f LEFT ( x RIGHT )`=`{c1}x`+`{a1}$$/수식$$    에서\n"\
             "$$수식$$f LEFT ( {a4} RIGHT )`=`{c1}TIMES{l4}{a4}{r4}+{a1}`=`{c2}$$/수식$$\n"\
             "$$수식$$f LEFT ( {a6} RIGHT )`=`{c1}TIMES{a6}+{a1}`=`{c3}$$/수식$$\n"\
             "$$수식$$THEREFORE~f LEFT ( {a4} RIGHT )`{sa5}f LEFT ( {a6} RIGHT )`=`{c2}`+`{l3}{c3}{r3}TIMES{l5}{a5}{r5}`=`{c4}$$/수식$$\n\n"
    a2=random.randint(2,3)
    a1=random.randint(1,2)*a2
    a3=random.randint(4,6)*a2
    a4=random.randint(-2,2)
    a5=random.randint(-5,5)
    a6=random.randint(2,5)
    while a4==0 or a5==0 or abs(a5)==1:
        a4=random.randint(-2,2)
        a5=random.randint(-5,5)
    c1=int((a3-a1)/a2)
    c2=c1*a4+a1
    c3=c1*a6+a1
    while c2==0 or c3==0:
        a2=random.randint(2,3)
        a1=random.randint(1,2)*a2
        a3=random.randint(4,6)*a2
        a4=random.randint(-2,2)
        a5=random.randint(-5,5)
        a6=random.randint(2,5)
        while a4==0 or a5==0 or abs(a5)==1:
            a4=random.randint(-2,2)
            a5=random.randint(-5,5)
        c1=int((a3-a1)/a2)
        c2=c1*a4+a1
        c3=c1*a6+a1
    
    c4=c2+a5*c3
    sa5=made_sign_string(a5) 
    if a2<0:
        l2="("
        r2=")"
    else:
        l2=""
        r2=""
    if c3<0:
        l3="("
        r3=")"
    else:
        l3=""
        r3=""
    if a4<0:
        l4="("
        r4=")"
    else:
        l4=""
        r4=""
    if a5<0:
        l5="("
        r5=")"
    else:
        l5=""
        r5=""
    a_li=made_answer_cand_1(c4)
    random.shuffle(a_li)
    a=answer_dict[a_li.index(c4)]
    x1,x2,x3,x4,x5=a_li[0],a_li[1],a_li[2],a_li[3],a_li[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,sa5=sa5,l5=l5,r5=r5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,sa5=sa5,a6=a6,l5=l5,r5=r5,c1=c1,c2=c2,c3=c3,c4=c4,aaa="a",l2=l2,r2=r2,l3=l3,r3=r3,l4=l4,r4=r4)
    return stem,answer,comment
#2-1-3-17
def systemequations213_Stem_017():
    stem= "일차함수$$수식$$f LEFT ( x RIGHT )`=`{a1}x`+`b$$/수식$$     에서$$수식$$f LEFT ( {a2} RIGHT )`=`{a3}$$/수식$$  이고,$$수식$$f LEFT ( a RIGHT )`=`{a4}$$/수식$$   일 때,$$수식$$b`-`a$$/수식$$  의 값은?\n"\
          "① {x1}		② {x2}	    ③ {x3}\n④ {x4}         ⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$f LEFT ( {a2} RIGHT )`=`{c1}`+`b`=`{a3}$$/수식$$      이므로 $$수식$$b`=`{c2}$$/수식$$\n"\
             "$$수식$$f LEFT ( a RIGHT )`=`{a1}a`+`{l2}{c2}{r2}={a4}$$/수식$$      이므로 $$수식$$a`=`{c3}$$/수식$$\n"\
             "$$수식$$THEREFORE~b`-`a`=`{c2}`-`{l3}{c3}{r3}`=`{c4}$$/수식$$\n\n"
    a1=random.randint(-5,5)
    while a1==0:
        a1=random.randint(-5,5)
    a2=random.randint(-3,3)
    a3=random.randint(-3,3)*a1
    a4=random.randint(-5,5)*a1
    c1=a1*a2
    c2=a3-c1
    c3=int((a4-c2)/a1)
    if c2<0:
        l2="("
        r2=")"
    else:
        l2=""
        r2=""
    if c3<0:
        l3="("
        r3=")"
    else:
        l3=""
        r3=""
    c4=c2-c3
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,c4=c4,l2=l2,r2=r2,l3=l3,r3=r3)

    return stem,answer,comment

#2-1-3-18
def systemequations213_Stem_018():
    stem= "상수 $$수식$$a`,b`,c`,d`$$/수식$$   에 대하여 $$수식$${a1}x LEFT ( {a2}`+`{a3}ax RIGHT )`+`{a4}bx`-`cy`+`d`=`0$$/수식$$       이 일차함수가 되도록 하는 $$수식$$a`,b`,c`$$/수식$$  의 조건으로 옳은 것은?\n"\
          "① {x1}		\n② {x2}	  \n③ {x3}\n④ {x4}   \n⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${a1}x LEFT ( {a2}`+`{a3}ax RIGHT )`+`{a4}bx`-`cy`+`d`=`0$$/수식$$\n"\
             "$$수식$$cy`=`{c1}a{t}^{h}`+` LEFT ({c2}`+`{a4}b RIGHT )x`+`d$$/수식$$      이 식이 일차함수이려면\n"\
             "$$수식$${c1}a`=`0,{a4}b`+`{c2}`!=`0,c`!=`0$$/수식$$\n"\
             "$$수식$$THEREFORE~a`=`0,b`!=`{c3},c`!=`0$$/수식$$\n"\
             "(힌트)상수$$수식$$p,~q,~r$$/수식$$     에 대하여 함수\n"\
             "$$수식$$y`=`p{t}^{h}`+`qx`+`r$$/수식$$     가 $$수식$$x`$$/수식$$에 대한 일차함수이려면\n"\
             "$$수식$$p`=`0,~q`!=`0$$/수식$$     이어야 한다.\n\n"
    a1=random.randint(2,5)
    a2=random.randint(2,6)
    a3=random.randint(3,5)
    a4=random.sample([a1,a2],1)[0]
    c1=a1*a3
    c2=a1*a2
    c3=int(-c2/a4)
    s1="$$수식$$a`=`0$$/수식$$"
    s1_1="$$수식$$a`!=`0$$/수식$$"
    s2="$$수식$$b`=`{c3}$$/수식$$".format(c3=c3)
    s2_2="$$수식$$b`!=`{c3}$$/수식$$".format(c3=c3)
    s3="$$수식$$c`=`0$$/수식$$"
    s3_3="$$수식$$c`!=`0$$/수식$$"
    sp="   , "
    b1=s1+sp+s2+sp+s3
    b2=s1+sp+s2_2+sp+s3
    b3=s1+sp+s2_2+sp+s3_3
    b4=s1_1+sp+s2+sp+s3
    b5=s1_1+sp+s2_2+sp+s3_3
    l=[b1,b2,b3,b4,b5]
    random.shuffle(l)
    a=answer_dict[l.index(b3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    t="x"
    h=2
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,t=t,h=h)
    return stem,answer,comment

#2-1-3-19
def systemequations213_Stem_019():
    stem= "다음 중 일차함수$$수식$$y`=`{a1}x`{sa2}$$/수식$$     의 그래프 위의 점이 아닌 것은?\n"\
          "① {x1}		            ② {x2}	  \n\n③ {x3}                     ④ {x4}  \n\n⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "{c1}\n\n"
    a1=random.randint(-5,5)
    while abs(a1)==1:
        a1=random.randint(-5,5)

    a2=random.randint(-3,3)
    while a2==0:
        a2=random.randint(-3,3)
    
    n1=Fraction(1,2)
    n2=Fraction(1,4)
    n3=Fraction(1,5)
    n4=3
    n=[n1,n2,n3]
    l=[]
    l1,r1="",""
    if a1<0:
        l1,r1="(",")"
    for i in n:
        if (a1*i+a2).denominator==1:
            s="$$수식$$LEFT ({}OVER{}`,~`{} RIGHT )$$/수식$$".format(i.numerator,i.denominator,(a1*i+a2))
            l.append(s)
        
        else:
            s="$$수식$$LEFT ({}OVER{}`,~`{}OVER{} RIGHT )$$/수식$$".format(i.numerator,i.denominator,(a1*i+a2).numerator,(a1*i+a2).denominator)
            l.append(s)
    s2="$$수식$$LEFT ({}`,~`{} RIGHT )$$/수식$$".format(n4,a1*n4+a2)
    l.append(s2)
    nn=2
    s1="$$수식$$LEFT ({}`,~`{} RIGHT )$$/수식$$".format(nn,(a1*nn+a2)*3)
    l.append(s1)
    random.shuffle(l)
    a=answer_dict[l.index(s1)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    c4=(a1*nn+a2)*3
    re=a1*nn+a2
    sa2=made_sign_string(a2)
    c1="$$수식$${nn}`TIMES`{l1}{a1}{r1}``{sa2}`=`{re}`!=`{c4}$$/수식$$".format(a1=a1,sa2=sa2,l1=l1,r1=r1,nn=nn,re=re,c4=c4)
    
    
    stem=stem.format(a1=a1,sa2=sa2,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(c1=c1)

    return stem,answer,comment

#2-1-3-20
def systemequations213_Stem_020():
    stem= "일차함수$$수식$$y`=`{sa1}`a`x`+`b`+`{a2}$$/수식$$      의 그래프를 $$수식$$y`$$/수식$$   축 방향으로 $$수식$${sa3}$$/수식$$     만큼 \n\n평행이동하면 $$수식$$y`=`{a4}x`+`{l5}{sa5}{r5}$$/수식$$        의 그래프와 일치할 때, 상수$$수식$$a,b`$$/수식$$ 에 대하여 $$수식$${b}^{t}`-`{ast}^{t}$$/수식$$ \n\n  의 값은?\n"\
              "① {x1}	② {x2}	  ③ {x3}\n④ {x4}     ⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "평행이동한 그래프의 일차함수 식은\n"\
             "$$수식$$y`=`{sa1}`a`x`+`b`+`{a2}`+`{l3}{sa3}{r3}`=`{sa1}`a` x`+`b`+`{sc1}$$/수식$$                이므로\n\n"\
             "$$수식$${sa1}`a`=`{a4},b`+`{sc1}`=`{sa5}$$/수식$$\n\n"\
             "따라서 $$수식$$a`=`{c2}, b`=`{sc3}$$/수식$$          이므로\n\n"\
             "$$수식$${b}^{t}`-`{ast}^{t}`=`{sc5}`-`{c6}`=`{sc7}$$/수식$$\n\n"
    ast="a"
    b="b"
    t=2
    tmp=random.sample([3,5,7],1)[0]
    a1=Fraction(tmp,2)
    sa1=made_fraction_string(a1)
    a2=random.randint(1,3)
    a3=Fraction(random.sample([1,3,5],1)[0],2)
    sa3=made_fraction_string(a3)
    a4=tmp
    a5=Fraction(random.sample([1,3,5,7],1)[0],2)
    sa5=made_fraction_string(a5)
    c1=a2+a3
    while c1==a5:
        a5=Fraction(random.sample([1,3,5,7],1)[0],2)
        sa5=made_fraction_string(a5)
    sc1=made_fraction_string(c1)
    c2=int(a4/a1)
    c3=int(a5-c1)
    if abs(c3.denominator)==1:
        c3=int(c3)
    sc3=made_fraction_string(c3)
    c5=int(c3*c3)
    sc5=made_fraction_string(c5)
    c6=c2*c2
    c7=c5-c6
    sc7=made_fraction_string(c7)
    l3=""
    r3=""
    l5=""
    r5=""
    if a3<0:
        l3="("
        r3=")"
    if a5<0:
        l5="("
        r5=")"
    
    l=made_answer_cand_1(c7)
    a=answer_dict[l.index(c7)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(sa1=sa1,a2=a2,sa3=sa3,a4=a4,sa5=sa5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,t=t,ast=ast,b=b,l5=l5,r5=r5)
    answer=answer.format(a=a)
    comment=comment.format(sa1=sa1,a2=a2,sa3=sa3,a4=a4,sa5=sa5,sc1=sc1,c2=c2,sc3=sc3,t=t,sc5=sc5,c6=c6,sc7=sc7,ast=ast,b=b,l3=l3,r3=r3)

    return stem,answer,comment
#2-1-3-21
def systemequations213_Stem_021():
    stem= "일차함수 $$수식$$y`=`{a1}x$$/수식$$  의 그래프를 $$수식$$y`$$/수식$$ 축의 방향으로 $$수식$${a2}`$$/수식$$만큼 평행이동하면 점$$수식$$(p`,~0 )$$/수식$$   을 지난다. 이때 $$수식$$p`$$/수식$$의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`=`{a1}x`{sa2}$$/수식$$      의 그래프가 점$$수식$$(p`,~0)`$$/수식$$    을 지나므로\n"\
             "$$수식$$0`=`{a1}p`{sa2}~`~THEREFORE~p`=`{sc1}$$/수식$$\n\n"
    a1=random.randint(2,5)
    a2=random.randint(-3,3)
    
    while a2==0:
        a2=random.randint(-3,3)
    sa2=made_sign_string(a2)
    if a2<0:
        l2="("
        r2=")"
    c1=Fraction(-a2,a1)
    sc1=made_fraction_string(c1)
    l=made_answer_cand_1(c1)
    random.shuffle(l)
    a=answer_dict[l.index(c1)]
    for i in range(5):
        l[i]=made_fraction_string(l[i])
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    
    stem=stem.format(a1=a1,a2=a2,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,sa2=sa2,sc1=sc1)

    return stem,answer,comment
#2-1-3-22
def systemequations213_Stem_022():
    stem= "일차함수 $$수식$$y`=`ax`+`{a1}$$/수식$$    의 그래프가 두 점$$수식$$LEFT ({a2},~ {one}OVER{a3} RIGHT )$$/수식$$,$$수식$$LEFT ( {a4}b`+`{a5}`,~{{b}}over{a6} RIGHT )$$/수식$$     를 지난다. 이때 $$수식$$b`$$/수식$$의 값은? (단, $$수식$$a`$$/수식$$  는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${one}over{a3}`=`{a2}a`+`{a1}$$/수식$$     이므로$$수식$$a`=`{sc1}`$$/수식$$\n\n"\
             "즉, $$수식$$y`=`{sc1}`x`+`{a1}$$/수식$$     의 그래프가 점\n\n"\
             "$$수식$$LEFT ( {a4}b`+`{a5},~{{b}}OVER{a6} RIGHT )$$/수식$$    를 지나므로\n\n"\
             "$$수식$$ {{b}}OVER{a6} `=`{sc1}`TIMES`({a4}b`+`{a5})+{a1}$$/수식$$\n\n"\
             "$$수식$$THEREFORE~b`=`{sc2}$$/수식$$\n\n"
    a1=random.randint(1,5)
    a2=random.randint(3,4)
    a3=random.randint(2,4)
    a4=random.randint(2,4)
    a5=random.randint(1,3)
    a6=random.randint(2,4)
    xy=Fraction(1,a3)
    by=Fraction(1,a6)
    c1=Fraction((xy-a1)/a2)
    c2=Fraction((a1+c1*a5)/(by-c1*a4))
    if (by-c1*a4)%(a1+c1*a5)==0:
        c2=int(c2)
    sc1=made_fraction_string(c1)
    sc2=made_fraction_string(c2)
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    for i in range(5):
        l[i]=made_fraction_string(l[i])
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,one=1,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(one=1,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,sc1=sc1,sc2=sc2)
    return stem,answer,comment

#2-1-3-23
def systemequations213_Stem_023():
    stem= "일차함수 $$수식$$y`=`ax`+`{a1}$$/수식$$   의 그래프가 두 점  $$수식$$LEFT ({a2}`,~{a3} RIGHT)`,~ LEFT ({a4}p{a5}`,~p RIGHT )$$/수식$$를 지날 때, $$수식$$p`$$/수식$$의 값은? (단, $$수식$$a`$$/수식$$는 상수이다.)\n"\
           "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n" 
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "점$$수식$$LEFT ({a2}`,~{a3} RIGHT)$$/수식$$ 이 $$수식$$y`=`ax`+`{a1}$$/수식$$    의 그래프 위의 점 이므로\n "\
             "$$수식$${a3}`=`{a2}`a`+`{a1}THEREFORE~a`=`{c1}$$/수식$$\n"\
             "또  $$수식$$LEFT ({a4}p{a5}`,~p RIGHT )$$/수식$$   이 $$수식$$y`=`x`+`{a1}$$/수식$$    위의 점 이므로\n"\
             "$$수식$$p`=`({a4}p{a5})`+`{a1},~p`=`{c2}p`{sc3}$$/수식$$\n"\
             " $$수식$$THEREFORE~p`=`{c4}$$/수식$$\n\n"
    a2=random.randint(1,3)
    tmp=random.randint(1,2)
    a1=a2*tmp
    a3=a2*(tmp+1)
    c1=int((a3-a1)/a2)
    a4=random.randint(2,4)
    a5=-1*tmp*a2*a4
    a6=1
    c2=c1*a4
    c3=c1*a5+a1
    c4=int(c3/(1-c2))
    sc3=made_sign_string(c3)
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,sc3=sc3,c4=c4)
    return stem,answer,comment


#2-1-3-24
def systemequations213_Stem_024():
    stem= "다음 보기 중 일차함수$$수식$$y`=`{a1}x$$/수식$$    의 그래프를 $$수식$$y`$$/수식$$축의 방향으로 $$수식$${a2}$$/수식$$만큼 평행이동한 그래프에 대한 설명으로 옳은 것을 모두 고른 것은?\n"\
          "$$표$$ 보기 \n"\
          "㈀ $$수식$$x`$$/수식$$의 값의 증가량에 대한 $$수식$$y`$$/수식$$의 값의 증가량의 비율은 $$수식$${a3}$$/수식$$이다.\n"\
          "㈁ 제{a4}사분면을 지난다.\n"\
          "㈂ 점 $$수식$$LEFT ( {a5}, {a6} RIGHT )$$/수식$$   {proa6} 지난다.\n" \
          "㈃ 오른쪽 아래로 향하는 직선이다.\n㈄ $$수식$$y`=`{a7}x`+`4$$/수식$$     의 그래프와 일치한다.$$/표$$\n"\
          "① {x1}	② {x2}	  ③ {x3}\n④ {x4}     ⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "{c1}\n\n"
    a1=random.randint(-5,5)
    while a1==0 or a1==1 or a1==-1:
        a1=random.randint(-5,5)
    a2=random.randint(-3,3)
    while a2==0:
        a2=random.randint(-3,3)
    a3=random.randint(-5,5)
    a4=random.randint(1,4)
    a7=-a1
    answer_list=[]
    
    if a1==a3:
        answer_list.append("ㄱ")
    if a1>0:
        if a2>0 and (a4==1 or a4==2 or a4==3):
            answer_list.append("ㄴ")
        elif a2<0 and (a4==1 or a4==3 or a4==4):
            answer_list.append("ㄴ")
    if a1<0:
        if a2>0 and (a4==1 or a4==2 or a4==4):
            answer_list.append("ㄴ")
        elif a2<0 and (a4==2 or a4==3 or a4==4):
            answer_list.append("ㄴ")
    a5=random.randint(2,3)
    a6=a1*a5+a2
    answer_list.append("ㄷ")
    if a1<0:
        answer_list.append("ㄹ")
    a_list=["ㄱ","ㄴ","ㄷ","ㄹ","ㅁ"]
    b=[0,0,0,0]
    d=[]
    answer_string=answer_list[0]
    for i in range(len(answer_list)):##정답인 애들 스트링 타입으로 만들기
        if i==0:
            pass
        else:
            answer_string=answer_string+", "+answer_list[i]
    for i in range(4):##선지 만들기
        b[i]=random.sample(a_list,i+1)
        while b[i]==a_list:
            b[i]=random.sample(a_list,i+1)
        d.append(made_string(sorted(b[i])))
    x1,x2,x3,x4,x5=d[0],d[1],d[2],d[3],answer_string
    a=answer_dict[4]
    c2=""
    c3=""
    if a2>0:
        c2="$$수식$$y`=`{a1}x`+`{a2}$$/수식$$".format(a1=a1,a2=a2)
        c3="`+`{a2}".format(a1=a1,a2=a2)
    else:
        c2="$$수식$$y`=`{a1}x`{a2}$$/수식$$".format(a1=a1,a2=a2)
        c3="{a2}".format(a1=a1,a2=a2)
    c1= "$$수식$$y`=`{a1}x$$/수식$$    의 그래프를 $$수식$$y`$$/수식$$축의 방향으로 $$수식$${a2}$$/수식$$만큼\n평행이동하면$$수식$${c2}$$/수식$$     이다.\n"\
        "(ㄱ)기울기가 $$수식$${a1}$$/수식$$이므로 $$수식$$x`$$/수식$$의 값의 증가량에 대한\n$$수식$$y`$$/수식$$의 값의 증가량의 비율은 $$수식$${a1}$$/수식$$이다.\n"\
        "(ㄷ)$$수식$${a6}={a1}`TIMES`{a5}{c3}$$/수식$$\n"\
        "(ㅁ)기울기가 다르므로 직선이 일치 할 수 없다.\n"\
        "따라서 옳은 것은 {c4}이다."
    proa6=proc_jo(a6,3)
    c1=c1.format(a1=a1,a2=a2,c2=c2,c3=c3,a5=a5,a6=a6,c4=answer_string)
    stem=stem.format(proa6=proa6,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(c1=c1)
    return stem,answer,comment

#2-1-3-25
def systemequations213_Stem_025():
    stem= "일차함수$$수식$$y`=`ax`+`{a1}$$/수식$$   의 그래프는 점 $$수식$$LEFT ( {a2}, {a3} RIGHT )$$/수식$$  을 지나고, 이 그래프를 $$수식$$y`$$/수식$$축의 방향으로 $$수식$$b`$$/수식$$만큼 평행이동하면 점$$수식$$LEFT ( {a4}, {a5} RIGHT )$$/수식$$ 을 지난다. 이때 상수 $$수식$$a`,~b`$$/수식$$  에 대하여 $$수식$${{b}}over{{a}}$$/수식$$  의 값은? (단, $$수식$$a`$$/수식$$는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`=`ax`+`{a1}$$/수식$$    의 그래프가 점 $$수식$$LEFT ( {a2}, {a3} RIGHT )$$/수식$$  을 지나므로\n"\
             "$$수식$${a3}`=`{a2}a`+`{a1} THEREFORE~a`=`{c1}$$/수식$$\n"\
             "따라서 $$수식$$y`=`{c1}x`+`{a1}+`b`$$/수식$$    의 그래프가 점$$수식$$LEFT ( {a4}, {a5} RIGHT )$$/수식$$   을 지나므로\n"\
             "$$수식$${a5}`=`{c1}TIMES{a4}`+`{a1}`+`b THEREFORE~b`=`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE$$/수식$$$$수식$${{b}}over{{a}}`=`{c2}`TIMES`{sc3}`=`{c4}$$/수식$$\n\n"
    
    a2=random.randint(2,6)
    a1=a2*2
    a3=a2*4
    c1=int((a3-a1)/a2)
    a4=random.randint(2,3)
    a5=random.randrange(10,12,2)
    c2=a5-a1-c1*a4
    c3=Fraction(1/c1)
    sc3=made_fraction_string(c3)
    c4=int(c2*c3)
    l=made_answer_cand_1(c4)
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,sc3=sc3,c4=c4)

    return stem,answer,comment

#2-1-3-26
def systemequations213_Stem_026():
    stem= "일차함수 $$수식$$y`=`{a1}x`-`{a2}$$/수식$$    의 그래프를 $$수식$$y`$$/수식$$ 축의 방향으로 $$수식$$p`$$/수식$$ 만큼 평행이동하면 점$$수식$$LEFT ( {a3}, {a4} RIGHT ) $$/수식$$ {proa4} 지난다. 이때 $$수식$$p`$$/수식$$ 의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`$$/수식$$축의 방향으로 $$수식$$p`$$/수식$$만큼 평행이동하면 $$수식$$y`=`{a1}x`-`{a2}`+`p`$$/수식$$    가 그래프가 점 $$수식$$LEFT ( {a3}, {a4} RIGHT ) $$/수식$$ {proa4} 지나므로\n  "\
             "$$수식$${a4}`=`{a1}TIMES{a3}`-`{a2}`+`p$$/수식$$\n"\
             "$$수식$$THEREFORE~p`=`{c1}$$/수식$$\n\n"
    a1=random.randint(2,6)
    a2=random.randint(2,5)
    a3=random.randint(2,3)
    a4=random.randint(2,8)
    c1=a4-a1*a3+a2
    l=made_answer_cand_1(c1)
    proa4=proc_jo(a4,3)
    random.shuffle(l)
    a=answer_dict[l.index(c1)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]

    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa4=proa4)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,proa4=proa4)

    return stem,answer,comment

#2-1-3-27
def systemequations213_Stem_027():
    stem= "일차함수 $$수식$$y`=`ax`+`b`$$/수식$$    의 그래프를 $$수식$$y`$$/수식$$ 축의 방향으로 $$수식$${a1}$$/수식$$ 만큼 평행이동한 그래프가 두 점 $$수식$$LEFT ( {a2}, ~{a3} RIGHT ), LEFT ( {a4},~{a5} RIGHT )$$/수식$$     {proa5} 지난다고 할 때, 상수 $$수식$$a`,~b`$$/수식$$  에 대하여 $$수식$$ab`$$/수식$$의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`=`ax`+`b`+`{a1}$$/수식$$    의 그래프가 두 점 $$수식$$LEFT ( {a2},~{a3} RIGHT ),~LEFT ( {a4},~{a5} RIGHT )$$/수식$$    {proa5} 지나므로 \n"\
             "$$수식$${a3}`=`{a2}a`+`b+`{a1} ,~ {a5}`=`{a4}a`+`b`+`{a1}$$/수식$$\n"\
             "즉, $$수식$${a2}a`+`b`=`{c1}  ,~ {a4}a`+`b`=`{c2}$$/수식$$\n"\
             "연립방정식을 풀면 $$수식$$a`=`{c3},~b`=`{c4}$$/수식$$\n"\
             "$$수식$$THEREFORE~ab`=`{c3}TIMES{l4}{c4}{r4}`=`{c5}$$/수식$$\n\n"
    a1=random.randrange(3,5)
    a4=random.randint(6,10)
    a2=2*a4
    while a2==0:
        a2=2*a4
    a3=random.randint(1,5)*a4
    a5=random.randint(1,5)*a4
    proa5=proc_jo(a5,3)
    while a3==a5:
        a3=random.randint(1,5)*a4
        a5=random.randint(1,5)*a4
    c1=a3-a1
    c2=a5-a1
    c3=int((c1-c2)/(a2-a4))
    c4=int((a4*a3-a2*a5)/(a4-a2)-a1)
    c5=c3*c4
    l4=""
    r4=""
    if c4<0:
        l4="("
        r4=")"
    l=made_answer_cand_1(c5)
    random.shuffle(l)
    a=answer_dict[l.index(c5)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa5=proa5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,l4=l4,proa5=proa5,r4=r4)

    return stem,answer,comment
#2-1-3-28
def systemequations213_Stem_028():
    stem= "좌표평면 위의 점$$수식$$A({a1}`,~{a2})$$/수식$$    {proa2} $$수식$$x`$$/수식$$축에 대칭인 점을 B라 할 때, 일차함수 $$수식$$y`=`{sa3}`x`$$/수식$$  의 그래프를 $$수식$$y`$$/수식$$축의 방향으로 $$수식$$a`$$/수식$$만큼 평행이동하면 점 B를 지난다. 이때 \n\n$$수식$$a`$$/수식$$의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	    ② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "두 점 $$수식$$A`$$/수식$$와 $$수식$$B`$$/수식$$가 $$수식$$x`$$/수식$$축에 대칭이므로\n"\
             "$$수식$$B({a1}`,~`-`{a2})$$/수식$$\n"\
             "한편 일차함수$$수식$$y`=`{sa3}`x`$$/수식$$    의 그래프를 $$수식$$y`$$/수식$$축의 방향으로 $$수식$$a`$$/수식$$만큼 평행이동 하면\n\n"\
             "$$수식$$y`=`{sa3}`x`+`a`$$/수식$$\n\n"\
             "$$수식$$y`=`{sa3}`x`+`a$$/수식$$    의 그래프가 점$$수식$$B({a1}`,~`-`{a2})$$/수식$$     {proa2} 지나므로\n\n"\
             "$$수식$$`-`{a2}`=`{sa3}`TIMES`{a1}`+`a$$/수식$$\n\n"\
             "$$수식$$THEREFORE~a`=`{c1}$$/수식$$\n\n"
    a1=random.randint(3,10)
    a2=random.randint(3,6)
    proa2=proc_jo(a2,3)
    a3=Fraction(1,a1)
    sa3=made_fraction_string(a3)
    c1=-a2-a3*a1
    l=made_answer_cand_1(c1)
    random.shuffle(l)
    a=answer_dict[l.index(c1)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,sa3=sa3,proa2=proa2,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,sa3=sa3,proa2=proa2,c1=c1)
    return stem,answer,comment

#2-1-3-29
def systemequations213_Stem_029():
    stem= "점 $$수식$$LEFT ( {a1},~{a2} RIGHT )$$/수식$$  {proa2} 지나는 일차함수 $$수식$$y`=`ax`+`b$$/수식$$   의 그래프를  $$수식$$y`$$/수식$$축의 방향으로  $$수식$${a3}`$$/수식$$    만큼 평행이동하면 점 $$수식$$LEFT ( {a4},~{a5} RIGHT )$$/수식$$ {proa5} 지난다. 일차함수  $$수식$$y`=`ax`-`b$$/수식$$    의 그래프 위의 점 중에서 $$수식$$y`$$/수식$$좌표가  $$수식$$x`$$/수식$$좌표의 $$수식$${a6}$$/수식$$배가 되는 점의  $$수식$$x`$$/수식$$좌표는? (단 $$수식$$a`,~b`$$/수식$$  는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "일차함수 $$수식$$y`=`ax`+`b$$/수식$$   의 그래프가 점$$수식$$LEFT ( {a1},~{a2} RIGHT )$$/수식$$ {proa2} 지나므로\n"\
             "$$수식$${a2}`=`{a1}a`+`b CDOTS CDOTS ㉠$$/수식$$\n"\
             "일차함수 $$수식$$y`=`ax`+`b$$/수식$$   의 그래프를  $$수식$$y`$$/수식$$축의 방향으로  $$수식$${a3}$$/수식$$   만큼 평행이동 하면\n"\
             "$$수식$$y`=`ax`+`b`+`{a3}$$/수식$$    이고 이 그래프가 점 $$수식$$LEFT ( {a4},~{a5} RIGHT )$$/수식$$  {proa5} 지나므로\n"\
             "$$수식$${a5}`=`{a4}a`+`b`+`{a3} CDOTS CDOTS ㉡$$/수식$$\n"\
             "㉠, ㉡를 연립해서 풀면  $$수식$$a`=`{c1},~b`=`{c2}$$/수식$$\n"\
             "$$수식$$y`=`{c1}x{sc2}$$/수식$$    의 그래프위의 점 중에서  $$수식$$y`$$/수식$$   좌표가  $$수식$$x`$$/수식$$  좌표의  $$수식$${a6}$$/수식$$  배가 되는 점의 좌표를 $$수식$$LEFT ( c,~{a6}c RIGHT )$$/수식$$   라 하면\n"\
             "$$수식$${a6}c`=`{c1}c{sc2} ~THEREFORE~c`=`{c3}$$/수식$$\n"\
             "따라서 구하는  $$수식$$x`$$/수식$$좌표는  $$수식$${c3}$$/수식$$ 이다.\n\n"
    while 1:
        a1=random.randint(1,3)
        a2=random.randint(1,3)*a1
        a3=random.randint(4,5)*a1
        a4=2*a1
        a5=random.randint(6,7)*a1
        while a5==a2+a3:
            a5=random.randint(6,7)*a1
        c1=int((a5-a2-a3)/(a4-a1))
        c2=int((a5*a1-a4*a2-a1*a3)/(a1-a4))
        if c1!=1 and c2!=1 and c1!=-1:
            break
    a6=random.randint(2,3)
    while a6==c1:
        a6=random.randint(2,3)
    c3=int(-c2/(a6-c1))
    if c2<0:
        sc2="`+`{}".format(-c2)
    else:
        sc2="`-`{}".format(c2)
    proa2=proc_jo(a2,3)
    proa5=proc_jo(a5,3)
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa2=proa2,proa5=proa5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,c1=c1,c2=c2,c3=c3,sc2=sc2,proa2=proa2,proa5=proa5)
    return stem,answer,comment

#2-1-3-30
def systemequations213_Stem_030():
    stem= "일차함수 $$수식$$y`=`ax`{sa1}$$/수식$$    의 그래프의 $$수식$$x`$$/수식$$절편이$$수식$${a2}`$$/수식$$, $$수식$$y`$$/수식$$절편이 $$수식$$b`$$/수식$$일 때, 일차함수$$수식$$y`=`ax`+`(b`-`a)$$/수식$$      의 그래프의 $$수식$$x`$$/수식$$절편과 $$수식$$y`$$/수식$$절편의 차의 절댓값은? (단$$수식$$a`,~b$$/수식$$  는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"  
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$x`$$/수식$$  절편이$$수식$$`{a2}`$$/수식$$ 이면 $$수식$$LEFT ( {a2}, 0 RIGHT )$$/수식$$  을 지나므로\n"\
             "$$수식$$a`=`{c1}$$/수식$$   , $$수식$$y`$$/수식$$절편은 $$수식$${a1}$$/수식$$  이므로 $$수식$$b`=`{a1}$$/수식$$\n"\
             "따라서 $$수식$$y`=`ax`+`(b-a)`=`{c1}x`{sc2}~~$$/수식$$           의 \n$$수식$$x`$$/수식$$ 절편은 $$수식$$`{c3}`$$/수식$$ , $$수식$$y`$$/수식$$절편은$$수식$$`{c4}`$$/수식$$\n"\
             "이므로 구하는 값은 $$수식$${c5}$$/수식$$\n\n"

    a2=random.randint(-3,3)
    a1=random.randint(2,5)*a2
    while a2==0 or abs(a2)==1:
        a2=random.randint(-3,3)
        a1=random.randint(2,5)*a2
    sa1=made_sign_string(a1)
    c1=int(-a1/a2)
    c2=a1-c1
    sc2=made_sign_string(c2)
    c4=c2
    c3=int(-c2/c1)
    c5=abs(c4-c3)
    l=made_answer_cand_1(c5)
    random.shuffle(l)
    a=answer_dict[l.index(c5)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(sa1=sa1,a2=a2,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,c1=c1,sc2=sc2,c3=c3,c4=c4,c5=c5)
    return stem,answer,comment

#2-1-3-31
def systemequations213_Stem_031():
    stem= "일차함수$$수식$$y`=`{a1}x`{sa2}$$/수식$$   의 그래프를 $$수식$$y`$$/수식$$축의 방향으로 $$수식$${a3}$$/수식$$  만큼 평행이동한 그래프의 $$수식$$x`$$/수식$$절편을 $$수식$$a`$$/수식$$, $$수식$$y`$$/수식$$절편을 $$수식$$b`$$/수식$$라 할 때, $$수식$${a4}ab`$$/수식$$ 의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`=`{a1}x`{sa2}$$/수식$$   의 그래프를 $$수식$$y`$$/수식$$축의 방향으로 $$수식$${a3}$$/수식$$만큼 평행이동한 그래프의 식은\n$$수식$$y`=`{a1}x`{sa2}`+`{a3}$$/수식$$ \n즉, $$수식$$y`=`{a1}x`+`{c1}$$/수식$$\n"\
             "이 그래프의 $$수식$$x`$$/수식$$절편은$$수식$${c2}$$/수식$$ , $$수식$$y`$$/수식$$절편은 $$수식$${c3}$$/수식$$이므로\n"\
             "$$수식$$THEREFORE~a={c2},~b={c3}$$/수식$$\n"\
             "$$수식$$THEREFORE~{a4}ab`=`{a4}TIMES{l2}{c2}{r2}TIMES{c3}`=`{c4}$$/수식$$\n\n"
    a1=random.randint(2,5)
    a2=random.randint(-2,2)*a1
    if a2<0:
        sa2="-`{}".format(-a2)
    else:
        sa2="+`{}".format(a2)
    a3=random.randint(4,6)*a1
    a4=random.randint(3,4)
    c1=a2+a3
    c2=int(-c1/a1)
    l2,r2="",""
    if c2<0:
        l2,r2="(",")"
    c3=c1
    c4=a4*c2*c3
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,sa2=sa2)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,sa2=sa2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,c4=c4,l2=l2,r2=r2)
    return stem,answer,comment


#2-1-3-32
def systemequations213_Stem_032():
    stem= "두 일차함수$$수식$$y`=`{a1}x`+`{a2}, y`=`{a3}x`+`k$$/수식$$         의 그래프가 $$수식$$x`$$/수식$$축 위에서 만날 때, 상수 $$수식$$k`$$/수식$$의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "두 그래프가 $$수식$$x`$$/수식$$축 위에서 만나므로 두 그래프의 $$수식$$x`$$/수식$$절편이 같다.\n"\
             "$$수식$$y`=`{a1}x`+`{a2}$$/수식$$    의 그래프의 절편은 $$수식$${c1}$$/수식$$ 이므로\n"\
             "$$수식$$y`=`{a3}x`+`k$$/수식$$    에$$수식$$x`=`{c1},~y`=`0$$/수식$$      을 대입하면\n"\
             "$$수식$$0`=`{a3}TIMES{l1}{c1}{r1}`+`k$$/수식$$\n"\
             "$$수식$$THEREFORE~k`=`{c2}$$/수식$$\n\n"
    a1=random.randint(-3,3)
    while a1==0 or a1==1 or a1==-1:
        a1=random.randint(-3,3)
    a2=random.randint(2,4)*abs(a1)
    c1=int(-a2/a1)
    l1,r1="",""
    if c1<0:
        l1,r1="(",")"
        a3=random.randint(2,4)
    else:
        a3=-random.randint(2,4)
    c2=-a3*c1
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4] 
    stem=stem.format(a1=a1,a2=a2,a3=a3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,l1=l1,r1=r1,c1=c1,c2=c2)
    return stem,answer,comment

#2-1-3-33
def systemequations213_Stem_033():
    stem= "일차함수 $$수식$$y`=`{sa1}`x`+`{a2}`$$/수식$$의 그래프의 $$수식$$x`$$/수식$$절편과 일차함수 $$수식$$y`=`{sa3}`x`+`{a4}{sa5}b`$$/수식$$  의\n\n 그래프의 $$수식$$y`$$/수식$$절편이 서로 같을 때, 상수 $$수식$$b`$$/수식$$의 값은?\n\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`=`{sa1}`x`+`{a2}$$/수식$$    의 그래프의 $$수식$$x`$$/수식$$절편은 $$수식$${c1}$$/수식$$ ,\n\n"\
             "$$수식$$y`=`{sa3}`x`+`{a4}{sa5}b`$$/수식$$    의 그래프의 $$수식$$y`$$/수식$$절편은 $$수식$${a4}{sa5}b $$/수식$$\n\n"\
             "이므로\n"\
             "$$수식$${c1}`=`{a4}{sa5}b~THEREFORE~b`=`{c2}$$/수식$$\n\n"
    a2=random.randrange(3,11,2)
    a1=Fraction(a2,(2*a2-1))
    sa1="{}over{}".format(a1.numerator,a1.denominator)
    a5=random.sample([-2,2],1)[0]
    if a5<0:
        sa5="`-`{}".format(-a5)
    else:
        sa5="`+`{}".format(a5)
    a4=random.randrange(1,7,2)
    c1=-(2*a2-1)
    a3=Fraction(1,3)
    sa3="{}over{}".format(a3.numerator,a3.denominator)
    c2=int((c1-a4)/a5)
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(sa1=sa1,a2=a2,sa3=sa3,a4=a4,sa5=sa5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(sa1=sa1,a2=a2,c1=c1,sa3=sa3,a4=a4,sa5=sa5,c2=c2)

    return stem, answer, comment
#2-1-3-34
def systemequations213_Stem_034():
    stem= "일차함수 $$수식$$y`=`px`+`q$$/수식$$    의 그래프의 $$수식$$x`$$/수식$$절편이 $$수식$${a1}$$/수식$$이고, 그 그래프가 점$$수식$$LEFT ( {a2}`,~{a3} RIGHT )$$/수식$$  {proa3} 지날 때, 상수 $$수식$$p`,~q$$/수식$$   에 대하여 $$수식$${{q}}OVER{{p}}$$/수식$$  의 값은?\n\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             " $$수식$$y`=`px`+`q$$/수식$$    의 그래프의 $$수식$$x`$$/수식$$절편이 $$수식$${a1}$$/수식$$이므로\n"\
             "$$수식$$0`=`{a1}p`+`q CDOTS CDOTS ㉠$$/수식$$\n"\
             "그래프가 점$$수식$$LEFT ( {a2}`,~{a3} RIGHT )$$/수식$$  {proa3} 지나므로\n"\
             "$$수식$${a3}`=`{a2}p`+`q CDOTS CDOTS ㉡$$/수식$$\n"\
             "㉠, ㉡를 연립하여 풀면 $$수식$$p`=`{c1},~q`=`{c2}`$$/수식$$\n"\
             "$$수식$$THEREFORE~{{q}}OVER{{p}}`=`{c3}$$/수식$$\n\n"
    a1=random.randint(-2,4)
    a2=random.randint(2,6)
    while a1==a2 or a1==0 or abs(a1)==1:
        a1=random.randint(-2,4)
        a2=random.randint(2,6)
    a3=random.randint(1,3)*(a2-a1)
    proa3=proc_jo(a3,3)
    c1=int(a3/(a2-a1))
    c2=-a1*c1
    c3=int(c2/c1)
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa3=proa3)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,c1=c1,c2=c2,c3=c3,proa3=proa3)
    return stem,answer,comment

#2-1-3-36
def systemequations213_Stem_035():
    stem= "기울기가 같은 두 일차함수$$수식$$y`=`ax`+`{a1}`,~y`=`{a2}x`+`b`$$/수식$$        의 그래프가 $$수식$$x`$$/수식$$축과 만나는 점을 각각 $$수식$$P`,~Q$$/수식$$   라 하자. $$수식$${{bar{{rm PQ it}}}}`=`{a3}$$/수식$$        일 때, 두 상수 $$수식$$a`,~b$$/수식$$  에 대하여 $$수식$${a4}a`+`b$$/수식$$   의 값은? (단, $$수식$$a`&gt;`b$$/수식$$   ) \n"\
          "① $$수식$${x1}$$/수식$$	    ② $$수식$${x2}$$/수식$$	    ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$        ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "두 일차함수의 기울기가 같으므로 $$수식$$a`=`{a2}$$/수식$$\n"\
             "또한 두 그래프가 $$수식$$x`$$/수식$$축과 만나는 점이 각각$$수식$$P`,~Q$$/수식$$  이므로 \n"\
             "$$수식$$P LEFT ({c1}`,~0 RIGHT )`,~Q LEFT ( {c2}`,~0 RIGHT )$$/수식$$\n\n"\
             "이때 $$수식$${{bar{{rm PQ it}}}}`=`{a3}$$/수식$$        이므로 \n\n"\
             "$$수식$${c1}{c2}`=`{a3} $$/수식$$ 또는 $$수식$${c2}`{c1}`=`{a3}$$/수식$$\n\n"\
             "$$수식$$THEREFORE~b`=`{c3}$$/수식$$또는 $$수식$$`~b`=`{c4}$$/수식$$\n\n"\
             "그런데 $$수식$$a`&gt;`b $$/수식$$   이므로 $$수식$$b`=`{c5}$$/수식$$\n"\
             "$$수식$$THEREFORE~{a4}a`+`b`=`{a4}TIMES{a2}`+`{l5}{c5}{r5}`=`{c6}$$/수식$$\n\n"
    a2=random.randint(3,5)
    a1=random.randint(2,5)*a2
    c1=int(-a1/a2)
    c2="`-`{{b}}over{k}".format(k=a2)
    a3=random.randint(2,8)
    c3=(c1-a3)*a2
    c4=(a3+c1)*a2
    a4=random.randint(3,5)
    if a2>c3:
        c5=c3
    elif a2>c4:
        c5=c4
    l5,r5="",""
    if c5<0:
        l5,r5="(",")"
    c6=a4*a2+c5
    l=made_answer_cand_1(c6)
    random.shuffle(l)
    a=answer_dict[l.index(c6)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,l5=l5,r5=r5)
    return stem,answer,comment

#2-1-3-38
def systemequations213_Stem_036():
    stem= "일차함수 $$수식$$y`=`f LEFT (x RIGHT )$$/수식$$ 에 대하여$$수식$${{f({a1})-f({a2})}}over{a3}`=`{a4}$$/수식$$                {proa4} 성립할 때, 일차함수  $$수식$$y`=`f LEFT (x RIGHT )$$/수식$$ 의 그래프의 기울기는?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${{f({a1})-f({a2})}}over{a3}`=`{{f({a1})-f({a2})}}over{c1}`=`(기울기)`=`{a4}$$/수식$$\n\n"
    a1=random.randint(4,8)
    a2=random.randint(-3,3)
    while a2==0:
        a2=random.randint(-3,3)
    l2,r2="",""
    if a2<0:
        l2,r2="(",")"
    a3=a1-a2
    a4=random.randint(4,10)
    proa4=proc_jo(a4,0)
    c1="{{{a1}`-`{l2}{a2}{r2}}}".format(a1=a1,a2=a2,l2=l2,r2=r2)
    l=made_answer_cand_1(a4)
    random.shuffle(l)
    a=answer_dict[l.index(a4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa4=proa4)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1)
    return stem,answer,comment

#2-1-3-39
def systemequations213_Stem_037():
    stem= "세 점 $$수식$$({a1},~{a2})`,~({a3},~{a4})`,~(m, n)$$/수식$$                이 한 직선 위에 있을 때, $$수식$${a5}$$/수식$$         의 값은?\n\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "세 점이 한 직선 위에 있으므로\n"\
             "$$수식$${c1}`=`{c2}$$/수식$$                  에서\n\n"\
             "$$수식$${c3}`,~{c5}$$/수식$$\n\n"\
             "$$수식$$THEREFORE~{a5}`=`{c6}`=`{c7}$$/수식$$\n\n"
    a1=random.randint(2,4)
    a2=random.randint(6,8)
    a3=random.randint(4,7)
    a4=random.randint(8,12)
    while a1==a3 or a2==a4 or a3*a2<=a4*a1 or abs(a2-a4)==1 or abs(a3-a1)==1:
        a3=random.randint(2,6)
        a4=random.randint(6,10)
    a5="{{{k}n}}over{{{l}m`+`{p}}}".format(k=a3-a1,l=a4-a2,p=a3*a2-a4*a1)
    c1="{{{a4}`-`{a2}}}over{{{a3}`-`{a1}}}".format(a1=a1,a2=a2,a3=a3,a4=a4)
    c2="{{n`-`{a4}}}over{{m`-`{a3}}}".format(a4=a4,a3=a3)
    c3="{}m`-`{}`=`{}n`-`{}".format(a4-a2,a3*(a4-a2),a3-a1,a4*(a3-a1))
    c5="{l}m`+`{p}`=`{k}n".format(k=a3-a1,l=a4-a2,p=a3*a2-a4*a1)
    c6="{{{k}n}}over{{{k}n}}".format(k=a3-a1)
    c7=1
    l=made_answer_cand_3(c7)
    random.shuffle(l)
    a=answer_dict[l.index(c7)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(c1=c1,c2=c2,c3=c3,a5=a5,c6=c6,c7=c7,c5=c5)
    return stem,answer,comment

#2-1-3-40
def systemequations213_Stem_038():
    stem= "일차함수 $$수식$$y`=`ax`+`{a1}$$/수식$$   의 그래프가 점$$수식$$LEFT ( {a2},~{a3} RIGHT )$$/수식$$  {proa3} 지날 때, 이 그래프의 기울기는 $$수식$$p`$$/수식$$이고, $$수식$$x`$$/수식$$절편은 $$수식$$q`$$/수식$$이다. 이때 $$수식$$pq`$$/수식$$의 값은? (단, $$수식$$a`$$/수식$$는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	        ② $$수식$${x2}$$/수식$$	        ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$         ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`=`ax`+`{a1}$$/수식$$    의 그래프가 점$$수식$$LEFT ( {a2},~{a3} RIGHT )$$/수식$$  {proa3} 지나므로\n"\
             "$$수식$${a3}`=`{a2}a`+`{a1}~THEREFORE~a`=`{c1}$$/수식$$\n"\
             "$$수식$$THEREFORE~p`=`{c1}$$/수식$$\n"\
             "따라서 $$수식$$y`=`{c1}x`+`{a1}$$/수식$$    의 그래프의 $$수식$$x`$$/수식$$절편이 $$수식$$q`$$/수식$$ 이므로\n"\
             "$$수식$$0`=`{c1}q`+`{a1}~THEREFORE~q={c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~pq`=`{c1}TIMES({c2})`=`{c3}$$/수식$$\n\n"
    a2=random.randint(2,5)
    tmp=random.randint(3,5)
    a1=tmp*a2
    a3=2*tmp*a2
    proa3=proc_jo(a3,3)
    c1=int((a3-a1)/a2)
    c2=int(-a1/c1)
    c3=c1*c2
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa3=proa3)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,c1=c1,c2=c2,c3=c3,proa3=proa3)

    return stem,answer,comment
#2-1-3-41
def systemequations213_Stem_039():
    stem= "일차함수 $$수식$$y`=`{a1}x$$/수식$$    의 그래프에서 $$수식$$x`$$/수식$$의 값이 $$수식$${a3}$$/수식$$에서 $$수식$$k`$$/수식$$까지 변화할 때, $$수식$$y`$$/수식$$의 값이 $$수식$${a4}$$/수식$$ 에서 $$수식$${a5}$$/수식$$ 까지 변화한다. 이때 의 $$수식$$k`$$/수식$$값은?\n"\
          "① $$수식$${x1}$$/수식$$	    ② $$수식$${x2}$$/수식$$	    ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$        ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$(기울기)`=`{a1}`=`{{{a5}`-`{l4}{a4}{r4}}}over{{k`-`{a3}}}$$/수식$$\n\n"\
             "$$수식$${a1}(k`-`{a3})`=`{c1}$$/수식$$\n"\
             "$$수식$$THEREFORE~k`=`{c2}$$/수식$$\n\n"
    a1=random.randint(-5,5)
    while a1==0 or a1==1 or a1==-1:
        a1=random.randint(-5,5)
    a2=random.randint(3,9)
    a3=random.randint(2,5)
    a4=a1*a3
    l4,r4="",""
    if a4<0:
        l4,r4="(",")"
    a5=a1*random.randint(4,6)
    while a4==a5:
        a5=a1*random.randint(4,6)
    c1=a5-a4
    c2=int((c1+a1*a3)/a1)
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,l4=l4,r4=r4)
    return stem,answer,comment

#2-1-3-43
def systemequations213_Stem_040():
    stem= "기울기가 $$수식$${a1}`$$/수식$$인 일차함수의 그래프가 두 점 $$수식$$LEFT ({a2},~{a3} RIGHT )`,~LEFT ( {a4},~ a RIGHT)$$/수식$$를 지날 때 ,$$수식$$a`$$/수식$$ 의 값은?\n"\
            "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "두 점 $$수식$$LEFT ({a2},~{a3} RIGHT ),~LEFT ( {a4},~ a RIGHT)$$/수식$$를 지나는\n"\
             "일차함수의 기울기가 $$수식$${a1}$$/수식$$  이므로\n"\
             "(기울기)$$수식$$`=`{{a`-`{a3}}}over{{{a4}`-`{a2}}}`=`{a1}$$/수식$$\n\n"\
             "$$수식$${a1}TIMES{c1}`=`a`-`{a3}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`=`{c2}$$/수식$$\n\n"
    a1=random.randint(3,5)
    a2=random.randint(2,4)
    a3=random.randint(2,4)
    a4=random.randint(5,7)
    c1=(a4-a2)
    c2=c1*a1+a3
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2)
    return stem,answer,comment
#2-1-3-45
def systemequations213_Stem_041():
    stem = "두 점$$수식$$LEFT   ( {a1},~{a2} RIGHT ),~ LEFT ( k`,~`{a3}k`+`1 RIGHT )$$/수식$$       을 지나는 직선 위에 점$$수식$$LEFT ( {a4}`,~{a5} RIGHT )$$/수식$$ {proa5} 있을 때, $$수식$$k`$$/수식$$의 값은?\n"\
           "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${{{a5}`-`{a2}}}over{{{a4}`-`{a1}}}`=`{{({a3}k+1)`-`{a2}}}over{{k`-`{a1}}}$$/수식$$                       이므로\n\n"\
             "$$수식$${c1}(k`-`{a1})`=`{c2}({a3}k+1`-`{a2})$$/수식$$\n"\
             "$$수식$$THEREFORE~k`=`{sc3}$$/수식$$\n\n"
    a1=random.randrange(2,4,2)
    a2=random.randrange(4,8,2)
    a3=random.randrange(2,6,2)
    a4=random.randrange(6,10,2)
    a5=random.randrange(2,6,2)
    while a2==a5:
        a5=random.randrange(2,6,2)
    proa5=proc_jo(a5,0)
    c1=a5-a2
    c2=a4-a1
    c3=Fraction((c1*a1-c2*a2+c2),(c1-c2*a3))
    if (c1*a1-c2*a2+c2)%(c1-c2*a3)==0:
        c3=int(c3) 
    sc3=made_fraction_string(c3)
    l=made_answer_cand_2(c3.numerator,c3.denominator)
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    a=answer_dict[2]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa5=proa5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,sc3=sc3)
    return stem,answer,comment

#2-1-3-46
def systemequations213_Stem_042():
    stem= "일차함수 $$수식$$y`=`{a1}x`+`{a2}$$/수식$$    의 그래프의 $$수식$$y`$$/수식$$절편을 $$수식$$a`$$/수식$$, $$수식$$y`=`{a3}x`+`{a4}$$/수식$$    의 그래프의 기울기를 $$수식$$b`$$/수식$$라 할 때, $$수식$$y`=`ax`+`b$$/수식$$     의 그래프의$$수식$$x`$$/수식$$절편은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n" 
    comment= "(해설)\n"\
             "$$수식$$y`=`{a1}x`+`{a2}$$/수식$$   의  $$수식$$y`$$/수식$$절편은 $$수식$${a2}$$/수식$$이므로\n"\
             "$$수식$$THEREFORE~a`=`{a2}$$/수식$$\n"\
             "$$수식$$y`=`{a3}x`+`{a4}$$/수식$$    의 그래프의 기울기는 $$수식$${a3}$$/수식$$이므로\n"\
             "$$수식$$THEREFORE~b`=`{a3}$$/수식$$\n"\
             "따라서 $$수식$$y`=`{a2}x`+`{a3}$$/수식$$    의 $$수식$$x`$$/수식$$절편은 \n"\
             "$$수식$${c1}$$/수식$$이다.\n\n"
    a1=random.randint(3,5)
    a2=random.randint(2,7)
    a3=random.randint(3,8)*a2
    a4=random.randint(2,5)
    c1=int(-a3/a2)
    l=made_answer_cand_1(c1)
    random.shuffle(l)
    a=answer_dict[l.index(c1)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1)
    return stem,answer,comment

#2-1-3-47
def systemequations213_Stem_043():
    stem= "일차함수 $$수식$$y`=`ax`+`b$$/수식$$    의 그래프는 $$수식$$y`=`{a1}x`+`{a2}$$/수식$$    의 그래프와 $$수식$$x`$$/수식$$ 축 위에서 만나고, 일차함수 $$수식$$y`=`{a3}x`+`{a4}$$/수식$$    의 그래프와 $$수식$$y`$$/수식$$축 위에서 만난다. 이때 $$수식$$y`=`ax`+`b$$/수식$$      의 그래프의 기울기는? (단, $$수식$$a`,~b$$/수식$$  는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`=`{a1}x`+`{a2}$$/수식$$    의$$수식$$x`$$/수식$$절편이$$수식$$ LEFT ( {c1}`,~0 RIGHT )$$/수식$$\n"\
             "$$수식$$y`=`{a3}x`+`{a4}$$/수식$$    의$$수식$$y`$$/수식$$절편이$$수식$$ LEFT ( 0`,~{c2} RIGHT )$$/수식$$\n"\
             "이므로 $$수식$$y`=`ax`+`b$$/수식$$    의 $$수식$$x`$$/수식$$ 절편과 $$수식$$y`$$/수식$$ 절편은\n"\
             "각각 $$수식$$x`=`{c1}`,`y`=`{c2}$$/수식$$      이다.\n"\
             "$$수식$$THEREFORE~a`=`{{{c2}`-`0}}over{{0`-`{l1}{c1}{r1}}}`=`{c3}$$/수식$$\n\n"
    a1=random.randint(-3,3)
    while a1==0 or abs(a1)==1:
        a1=random.randint(-3,3)
    tmp=random.randint(1,3)
    a2=abs(tmp*a1)
    a3=random.randint(2,5)
    a4=tmp*random.randint(2,3)
    c1=int(-a2/a1)
    l1,r1="",""
    if c1<0:
        l1,r1="(",")"
    c2=a4
    c3=int(c2/(-c1))
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,l1=l1,r1=r1)
    return stem, answer, comment

#2-1-3-48
def systemequations213_Stem_044():
    stem= "일차함수 $$수식$$y`=`ax`+`b$$/수식$$    의 그래프 위의 두 점$$수식$$LEFT ( p , f LEFT ( p RIGHT ) RIGHT)$$/수식$$ ,$$수식$$LEFT ( q , f LEFT ( q RIGHT ) RIGHT)$$/수식$$\n 에 대하여 $$수식$${{f(q)`-`f(p)}}over{{q`-`p}}`=`{a1}`,~f LEFT ({a2} RIGHT )`=`{a3}$$/수식$$\n\n일 때, $$수식$$f LEFT ({a4} RIGHT )$$/수식$$  의 값은? (단,$$수식$$a`,~b$$/수식$$  는 상수이다.)\n\n"\
          "① $$수식$${x1}$$/수식$$  	    ② $$수식$${x2}$$/수식$$	     ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$         ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "(기울기)$$수식$$`=`{{f(q)`-`f(p)}}over{{q`-`p}}`=`{a1}$$/수식$$      이므로 $$수식$$a`=`{a1}$$/수식$$\n\n"\
             "$$수식$$y`=`{a1}x`+`b$$/수식$$    에서 $$수식$$f LEFT ({a2} RIGHT )`=`{a1}TIMES{a2}`+`b`=`{a3}$$/수식$$\n"\
             "$$수식$$THEREFORE~b`=`{c1}$$/수식$$\n"\
             "$$수식$$THEREFORE~ f(x)`=`{a1}x`+`{l1}{c1}{r1}$$/수식$$이므로\n"\
             "$$수식$$f({a4})`=`{a1}TIMES{l4}{a4}{r4}`+`{l1}{c1}{r1}`=`{c2}$$/수식$$\n"\
             "(힌트) 두 점$$수식$$LEFT ( p , f LEFT ( p RIGHT ) RIGHT)$$/수식$$ ,$$수식$$LEFT ( q , f LEFT ( q RIGHT ) RIGHT)$$/수식$$를 지나는\n"\
             "일차함수 $$수식$$y`=`f(x)$$/수식$$    의 그래프의 기울기는\n"\
             "$$수식$${{f(q)`-`f(p)}}over{{q`-`p}}`$$/수식$$             임을 이용한다.\n\n"
    a1=random.randint(-5,5)
    while a1==0 or abs(a1)==1:
        a1=random.randint(-5,5)
    a2=random.randint(2,4)
    a3=random.randint(4,10)
    a4=random.randint(-6,6)
    c1=a3-a1*a2
    l1,r1,l4,r4="","","",""
    if c1<0:
        l1,r1="(",")"
    if a4<0:
        l4,r4="(",")"
    c2=a1*a4+c1
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,l1=l1,r1=r1,l4=l4,r4=r4)
    return stem,answer,comment
#2-1-3-50
def systemequations213_Stem_045():
    stem= "다음 일차함수의 그래프 중 제$$수식$$2`,~3`,~4`$$/수식$$    사분면을 모두 지나는 것은?\n"\
          "① $$수식$${x1}$$/수식$$	    ② $$수식$${x2}$$/수식$$	    ③ $$수식$${x3}$$/수식$$\n\n④ $$수식$${x4}$$/수식$$          ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "일차함수의 그래프가 제$$수식$$2`,~3`,~4`$$/수식$$    사분면을 모두 지나려면 (기울기) $$수식$$`&lt;`0~$$/수식$$  ,  ($$수식$$y`$$/수식$$절편 )$$수식$$`&lt;`0$$/수식$$\n이어야 한다.\n"\
             "따라서 구하는 일차함수의 그래프는 {a}이다.\n\n"
    tm1="y`=`{a1}`x`{sa2}"
    tm2="y`=`{a3}`x`{sa4}"##정답
    tm3="y`=`{sa5}`x`{sa6}"
    tm4="y`=`{sa7}`x`{sa8}"
    tm5="y`=`{a9}`x`{sa10}"
    a1=random.randint(-5,5)
    while abs(a1)==1 or a1==0:
        a1=random.randint(-5,5)
    a2=random.randint(1,10)
    sa2=made_sign_string(a2)

    a3=random.randint(-5,-2)
    a4=random.randint(-10,-1)
    sa4=made_sign_string(a4)

    tmp1=random.randint(4,6)
    tmp2=random.randint(1,3)
    while tmp1==0 or abs(tmp1)==1 or tmp1==tmp2:
        tmp1=random.randint(4,6)
    a5=Fraction(tmp2,tmp1)
    a6=random.randint(-3,3)
    while a6==0:
        a6=random.randint(-3,3)
    sa5=made_fraction_string(a5)
    sa6=made_sign_string(a6)

    tmp3=random.randint(-5,-1)
    tmp4=random.randint(1,3)
    
    a8=random.randint(2,5)
    
    while abs(tmp3)==1 or abs(tmp4)==abs(tmp3):
        tmp3=random.randint(-5,-1)
    a7=Fraction(tmp4,tmp3)
    sa7=made_fraction_string(a7)
    sa8=made_sign_string(a8)

    a9=random.randint(2,10)
    a10=random.randint(5,10)
    sa10=made_sign_string(a10)

    tm1=tm1.format(a1=a1,sa2=sa2)
    tm2=tm2.format(a3=a3,sa4=sa4)
    tm3=tm3.format(sa5=sa5,sa6=sa6)
    tm4=tm4.format(sa7=sa7,sa8=sa8)
    tm5=tm5.format(a9=a9,sa10=sa10)

    l=[tm1,tm2,tm3,tm4,tm5]
    random.shuffle(l)
    a=answer_dict[l.index(tm2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]

    stem=stem.format(x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a=a)
    
    return stem,answer,comment

#2-1-3-60
def systemequations213_Stem_046():
    stem= "일차함수 $$수식$$y`=`ax`+`b$$/수식$$    의 그래프에 대한 다음 설명 중 옳지 않은 것은? (단,$$수식$$a`,~b`$$/수식$$  는 상수이다.)\n"\
          "① {x1}	\n② {x2}	  \n③ {x3}\n④ {x4}     \n⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "{c1}\n\n"
    
    
    c2="기울기는 $$수식$$a`$$/수식$$, $$수식$$y`$$/수식$$절편은 $$수식$$b`$$/수식$$이다."
    c3_1="$$수식$$a`&gt;`0$$/수식$$    이면 오른쪽 위로 향하는 직선이다."
    c3_2="$$수식$$a`&gt;`0$$/수식$$    일 때, x값이 증가하면 y값도 증가한다."
    c4_1="$$수식$$a`&lt;`0$$/수식$$    이면 오른쪽 아래로 향하는 직선이다."
    c4_2="$$수식$$a`&lt;`0$$/수식$$    일 때, x값이 증가하면 y값은 감소한다"
    c5="$$수식$$y`=`ax$$/수식$$  의 그래프를 $$수식$$y`$$/수식$$ 축의 방향으로 $$수식$$b`$$/수식$$ 만큼 평행이동 한 것이다."
    ac6="$$수식$$a`&gt;`0`,~b`&lt;`0`$$/수식$$      이면 제$$수식$$1`,~2`,~3`$$/수식$$    사분면을 지난다."
    ac7="$$수식$$a`&gt;`0`,~b`&gt;`0`$$/수식$$      이면 제$$수식$$1`,~3`,~4`$$/수식$$    사분면을 지난다."
    c3=random.sample([c3_1,c3_2],1)[0]
    c4=random.sample([c4_1,c4_2],1)[0]
    ac=random.sample([ac6,ac7],1)[0]
    l=[ac,c2,c3,c4,c5]
    random.shuffle(l)
    a=answer_dict[l.index(ac)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    
    ac6_1="{a} $$수식$$a`&gt;`0`,~b`&lt;`0`$$/수식$$      이면 제$$수식$$1`,~3`,~4`$$/수식$$    사분면을 지난다.".format(a=a)
    ac7_1="{a} $$수식$$a`&gt;`0`,~b`&gt;`0`$$/수식$$      이면 제$$수식$$1`,~2`,~3`$$/수식$$    사분면을 지난다.".format(a=a)
    
    if ac==ac6:
        c1=ac6_1
    elif ac==ac7:
        c1=ac7_1
    stem=stem.format(x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(c1=c1)
    
    return stem,answer,comment
#2-1-3-61
def systemequations213_Stem_047():
    stem= "일차함수$$수식$$y`=`{a1}x`$$/수식$$   의 그래프를 $$수식$$y`$$/수식$$축 방향으로 $$수식$${a2}`$$/수식$$만큼 평행 이동한 그래프에 대한 설명으로 옳은 것은?\n"\
          "$$표$$\n보기\n"\
          "(ㄱ){tm1}\n(ㄴ){tm2}\n(ㄷ){tm3}\n(ㄹ){tm4}\n(ㅁ){tm5}\n$$/표$$\n"\
          "① {x1}	② {x2}	  ③ {x3}\n④ {x4}     ⑤ {x5}\n\n"

    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "(ㄱ) 기울기는 $$수식$${a1}`$$/수식$$이다.\n"\
             "(ㄹ) $$수식$$y`$$/수식$$축과 만나는 점의 좌표는 $$수식$$LEFT ( 0,~{a2} RIGHT )$$/수식$$  이다.\n"\
             "따라서 옳은 것은 {aa}이다.\n\n"
    a1=random.randint(-3,3)
    a3=random.randint(-3,3)
    while abs(a1)==1 or a1==0 or abs(a3)==1 or a3==0:
        a1=random.randint(-3,3)
        a3=random.randint(-3,3)
    a2=random.randint(-5,5)*a1
    while a2==0:
        a2=random.randint(-5,5)
    a4=random.randint(1,4)
    a5=int(-a2/a1)
    tm1=" 기울기는 $$수식$${a3}`$$/수식$$이다.".format(a3=a3)
    tm2=" 제$$수식$${a4}`$$/수식$$사분면을 지나지 않는다.".format(a4=a4)
    tmp1=random.sample(["아래로","위로"],1)[0]
    tm3=" 오른쪽 {} 향하는 직선이다.".format(tmp1)
    tm4=" $$수식$$y`$$/수식$$축과 만나는 점의 좌표는 $$수식$$LEFT ( 0,~{a2} RIGHT )$$/수식$$  이다.".format(a2=a2)
    tm5=" $$수식$$x`$$/수식$$ 절편은 $$수식$${a5}`$$/수식$$이다.".format(a5=a5)
    x1,x2,x3,x4=tm1,tm2,tm3,tm4
    answer_list=[]
    if a3==a1:
        answer_list.append("(ㄱ)")
    if a1>0:
        if a2>0 and a4==4: 
            answer_list.append("(ㄴ)")
        if a2<0 and a4==2:
            answer_list.append("(ㄴ)")
        
        if tmp1=="위로":
            answer_list.append("(ㄷ)")
    else:
        if a2>0 and a4==3:
            answer_list.append("(ㄴ)")
        if a2<0 and a4==1:
            answer_list.append("(ㄴ)")
        if tmp1=="아래로":
            answer_list.append("(ㄷ)")
    answer_list.append("(ㄹ)")
    answer_list.append("(ㅁ)")
    aa=made_string(answer_list)
    t1="(ㄱ), (ㅁ)"
    t2="(ㄱ), (ㄴ)"
    t3="{}".format(aa)
    t4="(ㄱ), (ㄷ)"
    t5="(ㄱ), (ㄴ), (ㄷ)"
    l=[t1,t2,t3,t4,t5]
    random.shuffle(l)
    a=answer_dict[l.index(t3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,tm1=tm1,tm2=tm2,tm3=tm3,tm4=tm4,tm5=tm5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,aa=aa)
    return stem, answer,comment

#2-1-3-62
def systemequations213_Stem_048():
    stem= "다음중 일차함수 중 그 그래프가 $$수식$$x`$$/수식$$축에 가장 가까운 것은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"       
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "기울기의 절댓값이 작을수록 $$수식$$x`$$/수식$$축에 가깝다.\n"\
             "{c1}\n\n"\
             "이므로 그래프가 $$수식$$x`$$/수식$$축에 가장 가까운 것은 {a}이다.\n\n"
    term1="$$수식$${sa1}`x$$/수식$$"
    term2="$$수식$${sa3}`x$$/수식$$"
    term3="$$수식$${sa5}`x$$/수식$$"
    term4="$$수식$${sa7}`x$$/수식$$"
    term5="$$수식$${sa9}`x$$/수식$$"
    a1,a3,a5,a7,a9=0,0,0,0,0
    al=[a1,a3,a5,a7,a9]
    for i in range(5):
        tmp1=random.randint(-30,30)
        tmp2=random.randint(-50,50)
        while tmp1==0 or tmp2==0 or abs(tmp2)==1 or abs(tmp1)==abs(tmp2) or abs(gcd(tmp1,tmp2))!=1:
            tmp1=random.randint(-30,30)
            tmp2=random.randint(-50,50)
        al[i]=Fraction(tmp1,tmp2)
        if i!=0:
            for k in range(i):
                while al[k]==al[i]:
                    tmp1=random.randint(-30,30)
                    tmp2=random.randint(-50,50)
                    while tmp1==0 or tmp2==0 or abs(tmp2)==1 or abs(tmp1)==abs(tmp2) or abs(gcd(tmp1,tmp2))!=1:
                        tmp1=random.randint(-30,30)
                        tmp2=random.randint(-50,50)
                    al[i]=Fraction(tmp1,tmp2)
    sa1,sa3,sa5,sa7,sa9=made_fraction_string(al[0]),made_fraction_string(al[1]),made_fraction_string(al[2]),made_fraction_string(al[3]),made_fraction_string(al[4])
    ab1,ab2,ab3,ab4,ab5=abs(al[0]),abs(al[1]),abs(al[2]),abs(al[3]),abs(al[4])
    ab=[ab1,ab2,ab3,ab4,ab5]
    ab.sort()
    al2=al[:]
    al2.sort()
    tmp=0
    for i in range(5):
        if ab[0]==abs(al[i]):
            tmp=i
    a=answer_dict[tmp]
    term1=term1.format(sa1=sa1)
    term2=term2.format(sa3=sa3)
    term3=term3.format(sa5=sa5)
    term4=term4.format(sa7=sa7)
    term5=term5.format(sa9=sa9)
    x1,x2,x3,x4,x5=term1,term2,term3,term4,term5
    s="$$수식$${}$$/수식$$".format(made_fraction_string(ab[0]))
    for i in range(5):
        if i==0:
            continue
        s=s+"$$수식$$`&lt;` {} $$/수식$$ ".format(made_fraction_string(ab[i]))
    stem=stem.format(x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(c1=s,a=a)
    return stem,answer,comment


#2-1-3-64
def systemequations213_Stem_049():
    stem= "다음 중 아래 조건을 모두 만족시키는 직선을 그래프로 하는 일차함수의 식은?\n"\
          "$$표$$\n(가) 오른쪽 위로 향하는 직선이다.\n"\
          "(나) $$수식$$y`=`{a1}`x`+`3$$/수식$$  의 그래프보다 $$수식$$x`$$/수식$$축에 가깝다.\n\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"  
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "조건 (가)에서 기울기가 양수이고 조건 (나)에서 \n"\
             "기울기의 절댓값이 $$수식$$LEFT | {c1} RIGHT |$$/수식$$,즉$$수식$$ {c2}$$/수식$$보다 작아야\n\n"\
             "한다.\n"\
             "따라서 조건을 만족시키는 일차함수 식은\n"\
             "{a}이다.\n\n"
    tmp1=random.randint(-10,10)
    tmp2=random.randint(-10,10)
    while abs(gcd(tmp1,tmp2))!=1 or tmp1*tmp2==0 or abs(tmp1)==1:
        tmp1=random.randint(-10,10)
        tmp2=random.randint(-10,10)
    a1=Fraction(tmp2,tmp1)
    c1=made_fraction_string(a1)
    c2=made_fraction_string(abs(a1))
    
    tmp3=random.randint(-50,50)
    tmp4=random.randint(-30,30)
    while abs(gcd(tmp3,tmp4))!=1 or tmp3*tmp4==0 or abs(tmp4)==1:
        tmp3=random.randint(-50,50)
        tmp4=random.randint(-30,30)
    atan=Fraction(tmp4,tmp3)
    while abs(a1) <= abs(atan):
        tmp3=random.randint(-50,50)
        tmp4=random.randint(-30,30)
        while abs(gcd(tmp3,tmp4))!=1 or tmp3*tmp4==0 or abs(tmp4)==1:
            tmp3=random.randint(-50,50)
            tmp4=random.randint(-30,30)
        atan=Fraction(tmp4,tmp3)
    wtan=[0,0,0,0]
    
    for i in range(4):
        tmp5=random.randint(-50,50)
        tmp6=random.randint(-30,30)
        while abs(gcd(tmp5,tmp6))!=1 or tmp5*tmp6==0 or abs(tmp5)==1:
            tmp5=random.randint(-50,50)
            tmp6=random.randint(-30,30)
        wtan[i]=Fraction(tmp6,tmp5)
        while abs(wtan[i]) <= abs(a1):
            tmp5=random.randint(-50,50)
            tmp6=random.randint(-30,30)
            while abs(gcd(tmp5,tmp6))!=1 or tmp5*tmp6==0 or abs(tmp5)==1:
                tmp5=random.randint(-50,50)
                tmp6=random.randint(-30,30)
            wtan[i]=Fraction(tmp6,tmp5)
    for j in range(4):
        for k in range(4):
            if j!=k and wtan[j]==wtan[k]:
                while wtan[j]==wtan[k]:
                    tmp5=random.randint(-50,50)
                    tmp6=random.randint(-30,30)
                    while abs(gcd(tmp5,tmp6))!=1 or tmp5*tmp6==0 or abs(tmp5)==1:
                        tmp5=random.randint(-50,50)
                        tmp6=random.randint(-30,30)
                    wtan[k]=Fraction(tmp6,tmp5)
    l=["","","",""]                
    for n in range(4):
        l[n]="y`=`{}`x`+`3".format(made_fraction_string(wtan[n]))
    a_string="y`=`{}`x`+3".format(made_fraction_string(atan))
    l.append(a_string)
    random.shuffle(l)
    a=answer_dict[l.index(a_string)]
    a1=made_fraction_string(a1)
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,c1=c1,c2=c2,a=a)
    return stem,answer,comment
        

#2-3-1-65
def systemequations213_Stem_050():
    stem= "$$수식$$a`&lt;`0`,`b`&gt;`0$$/수식$$     일 때, 그래프가 제 $$수식$${sa1}$$/수식$$  사분면을 지나는 일차함수를 보기에서 모두 고르면?\n"\
          "$$표$$\n보기\n"\
          "(ㄱ) $$수식$$y`=`ax`+`ab$$/수식$$      (ㄴ) $$수식$$y`=`abx`-`b$$/수식$$\n"\
          "(ㄷ) $$수식$$y`=`-ax`-`b$$/수식$$      (ㄹ) $$수식$$y`=`-a`+`ab$$/수식$$\n$$/표$$"\
          "① (ㄱ), (ㄴ)	② (ㄴ), (ㄷ)	  ③ (ㄷ), (ㄹ)\n④ (ㄱ), (ㄴ), (ㄷ)     ⑤ (ㄱ), (ㄴ), (ㄷ), (ㄹ)\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "(ㄱ) $$수식$$a`&lt;`0`,`ab`&lt;`0`$$/수식$$      이므로 제$$수식$$2`,`3`,`4`$$/수식$$   사분면을 지난다.\n"\
             "(ㄴ) $$수식$$ab`&lt;`0`,`-b`&lt;`0`$$/수식$$      이므로 제$$수식$$2`,`3`,`4`$$/수식$$   사분면을 지난다\n."\
             "(ㄷ) $$수식$$-a`&gt;`0`,`-b`&lt;`0$$/수식$$      이므로 제$$수식$$1`,`3`,`4`$$/수식$$   사분면을 지난다.\n"\
             "(ㄹ) $$수식$$-a`&gt;`0`,`ab`&lt;`0$$/수식$$      이므로 제$$수식$$1`,`3`,`4`$$/수식$$   사분면을 지난다.\n"\
             "따라서 그래프가$$수식$${sa1}$$/수식$$   사분면을 지나는 일차"\
             "함수는 {c1}이다.\n\n"
    a_1=[2,3,4]
    a_2=[1,3,4]
    a1=random.sample([a_1,a_2],1)[0]
    a1.sort()
    sa1="{}`,`{}`,`{}".format(a1[0],a1[1],a1[2])
    if a1==a_1:
        a=answer_dict[0]
        c1="(ㄱ), (ㄴ)"
    else:
        a=answer_dict[2]
        c1="(ㄷ), (ㄹ)"
    stem=stem.format(sa1=sa1)
    answer=answer.format(a=a)
    comment=comment.format(sa1=sa1,c1=c1)
    
    return stem,answer,comment

#2-1-3-69
def systemequations213_Stem_051():
    stem= "일차함수$$수식$$y`=`ax`{sa1}$$/수식$$   의 그래프는 일차함수 $$수식$$y`=`{a2}x`{sa3}$$/수식$$    의 그래프와 평행하고 점 $$수식$$LEFT ( p`,~{a4}  RIGHT )$$/수식$$  {proa4} 지난다. 이때 $$수식$$a`+`p$$/수식$$  의 값은? (단, $$수식$$a`$$/수식$$는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`=`ax`{sa1}$$/수식$$    와 $$수식$$y`=`{a2}x`{sa3}$$/수식$$    의 그래프가 평행하므로\n$$수식$$a`=`{a2}$$/수식$$\n"\
             "$$수식$$y`=`{a2}x`{sa1}$$/수식$$    의 그래프가 점 $$수식$$LEFT ( p`,~{a4}  RIGHT )$$/수식$$  {proa4} 지나므로\n"\
             "$$수식$${a4}`=`{a2}p`{sa1}$$/수식$$\n"\
             "$$수식$$THEREFORE~p`=`{c1}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`+`p`=`{c2}$$/수식$$\n\n"
    a2=random.randint(2,3)
    a4=random.randint(4,6)*a2
    a1=random.randint(1,3)*a2
    a3=random.randint(-10,10)
    while a3==0:
        a3=random.randint(-10,10)
    proa4=proc_jo(a4,3)
    sa1=made_sign_string(a1)
    sa3=made_sign_string(a3)
    c1=int((a4-a1)/a2)
    c2=c1+a2
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(sa1=sa1,a2=a2,sa3=sa3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa4=proa4)
    answer=answer.format(a=a)
    comment=comment.format(sa1=sa1,a2=a2,sa3=sa3,a4=a4,c1=c1,c2=c2,proa4=proa4)
    return stem,answer,comment

#2-1-3-70
def systemequations213_Stem_052():
    stem= "두 일차함수 $$수식$$y`=ax`{sa1}$$/수식$$    와 $$수식$$y`=`{a2}x`+`b$$/수식$$    의 그래프가 일치할 때, 상수$$수식$$a`,`b`$$/수식$$ 에 대하여 $$수식$$a`+`b$$/수식$$  의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$a`=`{a2}`,`b`=`{sa1}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`+`b`=`{c1}$$/수식$$\n\n"
    a1=random.sample([2,4,5,9],1)[0]
    sa1=made_sign_string(a1)
    a2=random.randint(2,5)
    c1=a1+a2
    l=made_answer_cand_1(c1)
    random.shuffle(l)
    a=answer_dict[l.index(c1)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(sa1=sa1,a2=a2,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(sa1=a1,a2=a2,c1=c1)
    return stem,answer,comment

#2-1-3-72
def systemequations213_Stem_053():
    stem= "일차함수$$수식$$y`=`ax`{sa1}$$/수식$$   의 그래프는 일차함수 $$수식$$y`=`{a2}x`{sa3}$$/수식$$   의 그래프와 평행하고 점 $$수식$$LEFT ( {a4}`,~b  RIGHT )$$/수식$$  를 지난다. 이때 $$수식$$ab`$$/수식$$ 의 값은? (단, $$수식$$a`$$/수식$$는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`=`ax`{sa1}$$/수식$$    와 $$수식$$y`=`{a2}x`{sa3}$$/수식$$    의 그래프가 평행하므로\n$$수식$$a`=`{a2}$$/수식$$\n"\
             "$$수식$$y`=`{a2}x`{sa1}$$/수식$$    의 그래프가 점 $$수식$$LEFT ( {a4}`,~b  RIGHT )$$/수식$$  를 지나므로\n"\
             "$$수식$$b`=`{a2}TIMES{a4}`{sa1}`=`{c1}$$/수식$$\n"\
             "$$수식$$THEREFORE~ab`=`{c2}$$/수식$$\n\n"
             
    a2=random.randint(4,6)
    a4=random.randint(5,7)
    a1=random.randint(2,4)
    a3=random.randint(-10,10)
    while a3==0:
        a3=random.randint(-10,10)
    sa1=made_sign_string(a1)
    sa3=made_sign_string(a3)
    c1=a2*a4+a1
    c2=c1*a2
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(sa1=sa1,a2=a2,sa3=sa3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(sa1=sa1,a2=a2,sa3=sa3,a4=a4,c1=c1,c2=c2)
    return stem,answer,comment



#2-1-3-73
def systemequations213_Stem_054():
    stem= "다음 조건을 모두 만족시키는 상수 $$수식$$a`,~b`$$/수식$$ 에 대하여 $$수식$$a`+`b$$/수식$$  의 값은?\n"\
          "$$표$$\n(가) 두 일차함수 $$수식$$y`=`{a1}x{sa2}$$/수식$$    {proa2} $$수식$$y`=`ax`+`{a3}a$$/수식$$    의 그래프는 평행하다.\n"\
          "(나) 두 일차함수$$수식$$y`=`{a4}x-a`+`{a5}$$/수식$$     {proa5} $$수식$$y`=`{a4}x`+`{a6}b`+`{a7}$$/수식$$       의 그래프는 일치한다. \n$$/표$$\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "조건 (가)에서 $$수식$$a`=`{c1}$$/수식$$\n"\
             "조건 (나)에서 $$수식$$-a`+`{a5}`=`{a6}b`+`{a7}$$/수식$$      이므로\n"\
             "$$수식$${a6}b`=`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~b`=`{c3}$$/수식$$\n"\
             "$$수식$$THEREFORE~ a`+`b`=`{c4}$$/수식$$\n\n"
    
    
    a6=random.randint(2,4)
    a1=random.randint(-2,2)*a6
    while abs(a1)==1 or a1==0:
        a1=random.randint(-5,5)
    c1=a1
    a2=random.randint(-10,10)
    a3=random.randint(2,5)
    while a2==a1*a3:
        a2=random.randint(-10,10)
    sa2=made_sign_string(a2)
    
   
    a4=random.randint(-10,10)
    while abs(a4)==1 or a4==0:
        a4=random.randint(-10,10)
    a5=random.randint(2,4)*a6
    proa2=proc_jo(a2,2)
    proa5=proc_jo(a5,2)
    a7=random.randint(3,5)*a6
    c2=a5-c1-a7
    c3=int(c2/a6)
    c4=c1+c3

    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,sa2=sa2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa2=proa2,proa5=proa5)
    answer=answer.format(a=a)
    comment=comment.format(a5=a5,a6=a6,a7=a7,c1=c1,c2=c2,c3=c3,c4=c4)
    return stem,answer,comment

#2-1-3-74
def systemequations213_Stem_055():
    stem= "두 일차함수 $$수식$$y`=`({a1}m`{sa2})x`+`{a3}m`+`{a4}n`,~y`=`({a5}n`+`{a6}m)x`+`{a7}n`+`{a8}$$/수식$$\n의 그래프가 일치할 때, 상수 $$수식$$m`,~n`$$/수식$$  에 대하여 $$수식$$m`+`n$$/수식$$   의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${a1}m{sa2}`=`{a5}n`+`{a6}m`,~{a3}m`+`{a4}n`=`{a7}n`+`{a8}$$/수식$$\n"\
             "이므로\n"\
             "$$수식$${c1}m`{sa5}n`=`{a2}`,`{c2}n`+`{a3}m`=`{a8}$$/수식$$\n"\
             "두 식을 연립하여 풀면 $$수식$$m`=`{c3}`,~n`=`{c4}`$$/수식$$\n"\
             "$$수식$$THEREFORE~m`+`n`=`{c5}$$/수식$$\n\n"
    a1=random.randint(2,5)
    a6=random.randint(3,10)
    a7=random.randint(5,10)
    a4=random.randint(3,6)
    while a1==a6 or a7==a4 or abs(a6-a1)==1 or abs(a7-a4)==1:
        a1=random.randint(2,5)
        a6=random.randint(3,10)
        a7=random.randint(5,10)
        a4=random.randint(3,6)
    k=random.randint(2,4)
    p=random.randint(3,5)
    l=p*k-1
    q=l*random.randint(2,5)
    a5=k*(a1-a6)
    a2=l*(a1-a6)
    a3=p*(a7-a4)
    a8=q*(a7-a4)
    sa2=made_sign_string(a2)
    sa5=made_sign_string(a5)
    c1=a6-a1
    c2=a4-a7
    c3=int((q*k+l)/(p*k-1))
    c4=int((p*l+q)/(k*p-1))
    c5=c3+c4
    l=made_answer_cand_1(c5)
    random.shuffle(l)
    a=answer_dict[l.index(c5)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,sa2=sa2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,sa2=sa2,a2=a2,a3=a3,a4=a4,a5=a5,sa5=sa5,a6=a6,a7=a7,a8=a8,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    return stem,answer,comment
#2-1-3-78
def systemequations213_Stem_056():
    stem= "일차함수 $$수식$$y`=`{a1}ax`+`{a2}$$/수식$$    의 그래프는 일차함수 $$수식$$y`=`{a3}x`+`{a4}$$/수식$$     의 그래프와 만나지 않고, \n일차함수 $$수식$$y`=`{a5}bx`+`(c`{sa6})$$/수식$$     의 그래프와 $$수식$$x`$$/수식$$축, $$수식$$y`$$/수식$$축 위에서 만난다. 이때 상수 $$수식$$a`,~b`,~c`$$/수식$$   에 대하여 $$수식$$a`+`b`+`c$$/수식$$   의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "두 일차함수 $$수식$$y`=`{a1}ax`+`{a2}$$/수식$$    , $$수식$$y`=`{a3}x`+`{a4}$$/수식$$   의 그래프가만나지 않으므로,\n즉 평행하므로 두 그래프의 기울기가 같다.\n"\
             "$$수식$${a1}a`=`{a3}$$/수식$$   에서 $$수식$$a`=`{c1}$$/수식$$\n"\
             "두 일차함수의 그래프가 $$수식$$2`$$/수식$$개 이상의 점에서 만나면 두 그래프는 일치한다.\n두 일차함수 $$수식$$y`=`{a3}x`+`{a2}$$/수식$$    와 $$수식$$y`=`{a5}bx`+`(c`{sa6})$$/수식$$       의 그래프가\n$$수식$$x`$$/수식$$축, $$수식$$y`$$/수식$$축 위의 두 점에서 만나므로 두 그래프는 일치하고 일차함수의 식은 같다.\n"\
             "$$수식$${a3}`=`{a5}b`$$/수식$$   에서 $$수식$$b`=`{c2}$$/수식$$\n"\
             "$$수식$${a2}`=`c`{sa6}$$/수식$$   에서 $$수식$$c`=`{c3}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`+`b`+`c={c4}$$/수식$$\n"\
             "(힌트)일차함수와 만나지 않을 때와 축 위에서 만날 때를 먼저 생각한다.\n\n"
    a1=random.randint(3,4)
    a5=random.randint(2,3)

    a3=random.randint(2,4)*a1*a5
    a2=random.randint(3,5)
    a4=random.randint(6,7)
    a6=random.randint(1,2)
    sa6=made_sign_string(a6)
    c1=int(a3/a1)
    c2=int(a3/a5)
    c3=a2-a6
    c4=c1+c2+c3
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,sa6=sa6,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,sa6=sa6,c1=c1,c2=c2,c3=c3,c4=c4)
    return stem,answer,comment

#2-1-3-81
def systemequations213_Stem_057():
    stem= "두 점 $$수식$$LEFT ( {a1}`,~{a2} RIGHT )$$/수식$$, $$수식$$LEFT ( {a3}`,~{a4} RIGHT )$$/수식$$  을 지나는 일차함수의 그래프의 기울기를 $$수식$$a`$$/수식$$, $$수식$$y`$$/수식$$절편을 $$수식$$b`$$/수식$$, $$수식$$x`$$/수식$$절편을 $$수식$$c`$$/수식$$라 할 때, $$수식$$a`+`b`+`c$$/수식$$   의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "두 점 $$수식$$LEFT ( {a1}`,`{a2} RIGHT )$$/수식$$, $$수식$$LEFT ( {a3}`,`{a4} RIGHT )$$/수식$$  을 지나는 일차함수의 그래프의 기울기는\n"\
             "$$수식$${{{a4}`-`{a2}}}over{{{a3}`-`{a1}}}`=`{c1}$$/수식$$\n\n"\
             "$$수식$$THEREFORE~a`=`{c1}$$/수식$$\n"\
             "$$수식$$y`$$/수식$$절편이 $$수식$$b`$$/수식$$ 이므로 일차함수의 식을 "\
             "$$수식$$y`=`{c1}x`+`b$$/수식$$   라 하자.\n"\
             "이 그래프가 점 $$수식$$LEFT ( {a1}`,~{a2} RIGHT )$$/수식$$ 을 지나므로 "\
             "$$수식$${a2}`=`{c2}`+`b$$/수식$$\n"\
             "$$수식$$THEREFORE~b`=`{c3}$$/수식$$\n"\
             "따라서 일차함수 $$수식$$y`=`{c1}x`{sc3}$$/수식$$    의 그래프의 $$수식$$x`$$/수식$$절편이 $$수식$${c4}$$/수식$$이므로\n"\
             "$$수식$$c`=`{c4}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`+`b`+`c`=`{c5}$$/수식$$\n\n"
    a1=random.randint(2,5)
    a3=a1+1
    a2=random.randint(3,5)
    a4=2*a2
    c1=int((a4-a2)/(a3-a1))
    c2=c1*a1
    c3=a2-c2
    sc3=made_sign_string(c3)
    c4=int(-c3/c1)
    c5=c1+c3+c4
    l=made_answer_cand_1(c5)
    random.shuffle(l)
    a=answer_dict[l.index(c5)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,sc3=sc3,c4=c4,c5=c5)
    return stem,answer,comment
#2-1-3-82
def systemequations213_Stem_058():
    stem= "일차함수 $$수식$$y`=`{a1}x`+`{a2}`$$/수식$$  의 그래프와 평행하고, 연립부등식 $$수식$$cases{{``{a6}`&lt;`{a7}`x`#``{a3}x`+`{a4}`&lt;`{a5}$$/수식$$\n\n{proa5} 만족시키는 가장 큰 정수를 $$수식$$y`$$/수식$$절편으로 하는 직선이 있다. 이 직선을 그래프로 하는 일차함수의 식은?\n"\
          "① $$수식$${x1}$$/수식$$	    ② $$수식$${x2}$$/수식$$	    ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$        ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "일차함수 $$수식$$y`=`{a1}x`+`{a2}$$/수식$$    의 그래프와 평행하므로\n"\
             "기울기는 $$수식$${a1}$$/수식$$이다.\n"\
             "연립부등식 $$수식$$cases{{``{a6}`&lt;`{a7}x`#{a3}x`+`{a4}`&lt;`{a5}$$/수식$${proa5} 만족시키는 $$수식$$x`$$/수식$$값의 범위는\n\n"\
             "$$수식$${c3}`&lt;`{{x}}`&lt;`{c1}$$/수식$$      이므로 가장 큰 정수는 {c2}이다\n"\
             "$$수식$$THEREFORE~(y`절편)`=`{c2}$$/수식$$\n"\
             "따라서 구하는 일차함수의 식은$$수식$$y`=`{a1}x`+`{c2}$$/수식$$\n\n"
    a1=random.randint(2,5)
    a2=random.randint(3,10)
    a3=random.randint(2,3)
    a4=random.randint(2,5)*a3
    a5=random.randint(6,8)*a3
    c1=int((a5-a4)/a3)
    a7=random.randint(3,5)
    a6=-random.randint(2,5)*a7
    while c1==1:
        a4=random.randint(2,3)*a3
        a5=random.randint(4,5)*a3
        c1=int((a5-a4)/a3)
    proa5=proc_jo(a5,3)
    c2=c1-1
    c3=int(a6/a7)
    x1="y`=`-`{a1}x`+`{c2}".format(a1=a1,c2=c2)
    x2="y`=`-`{a1}x`-`{c2}".format(a1=a1,c2=c2)
    x3="y`=`{a1}x`-`{c2}".format(a1=a1,c2=c2)
    x4="y`=`{a1}x`+`{c2}".format(a1=a1,c2=c2)
    x5="y`=`{tt}x`+`{c2}".format(tt=2*a1,c2=c2)
    a=answer_dict[3]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa5=proa5,a6=a6,a7=a7)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,proa5=proa5,a6=a6,a7=a7,c3=c3)
    return stem,answer,comment

#2-1-3-83
def systemequations213_Stem_059():
    stem= "일차함수 $$수식$$y`=`f(x)`$$/수식$$    가 $$수식$${{f(2b)`-`f(4a)}}over{{4a`-`2b}}`=`{a1}$$/수식$$                   {proa1} 만족시키고 그 그래프가 \n\n점$$수식$$LEFT ( {a2}`,~{a3} RIGHT )$$/수식$$   을 지날 때, 일차함수의 식을 $$수식$$y`=`mx`+`n$$/수식$$   의 꼴로 나타내면? \n(단, $$수식$$m`$$/수식$$, $$수식$$n`$$/수식$$은 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	        ② $$수식$${x2}$$/수식$$	        ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$            ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$m`=`{{f(2b)`-`f(4a)}}over{{2b`-`4a}}`=`-`{{f(2b)`-`f(4a)}}over{{4a`-`2b}}`=`{c1}$$/수식$$\n\n"\
             "$$수식$$y`=`{c1}x`+`n$$/수식$$    에 점$$수식$$LEFT ( {a2}`,~{a3} RIGHT )$$/수식$$  을 대입하면 $$수식$$n`=`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~y`=`{c1}x`+`{c2}$$/수식$$\n\n"
    a1=random.randint(4,7)
    a2=random.randint(2,5)
    a3=random.sample([1,3,6,7,8,10,11,13,16],1)[0]
    c1=-a1
    c2=a3-c1*a2
    proa1=proc_jo(a1,3)
    xa="y`=`{c1}x`+`{c2}".format(c1=c1,c2=c2)
    x1="y`=`{c1}x`-`{c2}".format(c1=c1,c2=c2)
    x2="y`=`{c1}x`+`{c2}".format(c1=-c1,c2=c2)
    x3="y`=`{c1}x`-`{c2}".format(c1=-c1,c2=c2)
    x4="y`=`{tt}x`+`{c2}".format(tt=2*c1,c2=c2)
    xl=[xa,x1,x2,x3,x4]
    random.shuffle(xl)
    a=answer_dict[xl.index(xa)]
    x1,x2,x3,x4,x5=xl[0],xl[1],xl[2],xl[3],xl[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa1=proa1)
    answer=answer.format(a=a)
    comment=comment.format(a2=a2,a3=a3,c1=c1,c2=c2)
    return stem,answer,comment

#2-1-3-84
def systemequations213_Stem_060():
    stem= "일차함수 $$수식$$y`=`ax`+`b$$/수식$$   의 그래프는 점 $$수식$$LEFT ( {a1}`,~{a2} RIGHT )$$/수식$$  {proa2} 지나고, $$수식$$x`$$/수식$$의 값이 $$수식$${a3}`$$/수식$$만큼 증가할 때 $$수식$$y`$$/수식$$의 값은 $$수식$${a4}`$$/수식$$만큼 증가한다. 이때 $$수식$${a5}ab$$/수식$$ 의 값은? (단, $$수식$$a`,`b$$/수식$$ 는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	    ② $$수식$${x2}$$/수식$$	    ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$        ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$a`=`{a4}over{a3}`=`{c1}$$/수식$$\n\n"\
             "$$수식$$y`=`{c1}x`+`b$$/수식$$    에 점 $$수식$$LEFT ( {a1}, {a2} RIGHT )$$/수식$$  {proa2} 대입하면\n$$수식$$b`=`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~{a5}ab`=`{c3}$$/수식$$\n\n"
    a3=random.randint(2,6)
    a4=a3*2
    a1=random.randint(3,5)
    a2=2*a1+random.randint(1,3)
    
    c1=int(a4/a3)
    c2=a2-c1*a1
    a5=random.randint(2,4)
    
    proa2=proc_jo(a2,3)
    c3=c1*c2*a5
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa2=proa2)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,c3=c3,proa2=proa2)
    return stem,answer,comment


#2-1-3-85
def systemequations213_Stem_061():
    stem= "$$수식$$x`$$/수식$$의 값이 $$수식$${a1}$$/수식$$만큼 증가할 때 $$수식$$y`$$/수식$$의 값도 $$수식$${a2}$$/수식$$만큼 증가하고, 일차방정식 $$수식$${a3}x`+`{a4}y`+`{a5}`=`0$$/수식$$     의 그래프와 $$수식$$x`$$/수식$$축 위에서 만나는 직선을 그래프로 하는 일차함수의 식은?\n"\
          "① $$수식$${x1}$$/수식$$	    ② $$수식$${x2}$$/수식$$	    ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$        ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "기울기는 $$수식$${a2}over{a1}`=`{c1}$$/수식$$이므로 $$수식$$y`=`{c1}x`+`b$$/수식$$\n\n한편, 일차방정식 $$수식$${a3}x`+`{a4}y`+`{a5}`=`0$$/수식$$     의 그래프가 $$수식$$x`$$/수식$$축 과 만나는 점의 좌표가$$수식$$LEFT ( {c2}`,~0 RIGHT )$$/수식$$  이므로 $$수식$$x`=`{c2}`,~y`=`0`$$/수식$$      을 $$수식$$y`=`{c1}x`+`b$$/수식$$   에 대입하면\n"\
             "$$수식$$0`=`{c1}TIMES({c2})`+`b`~THEREFORE~b`=`{c3}$$/수식$$\n"\
             "$$수식$$THEREFORE~y`=`{c1}x`+`{c3}$$/수식$$\n\n"
    a1=random.randint(2,4)
    a2=random.randint(2,3)*a1
    c1=int(a2/a1)
    a3=random.randint(2,5)
    a4=random.randint(5,9)
    a5=random.randint(2,3)*a3
    c2=int(-a5/a3)
    c3=-c1*c2
    xa="y`=`{c1}x`+`{c3}".format(c1=c1,c3=c3)
    x1="y`=`{c1}x`-`{c3}".format(c1=c1,c3=c3)
    x2="y`=`{c1}x`+`{c3}".format(c1=-c1,c3=c3)
    x3="y`=`{c1}x`-`{c3}".format(c1=-c1,c3=c3)
    x4="y`=`{tt}x`+`{c3}".format(tt=2*c1,c3=c3)
    xl=[xa,x1,x2,x3,x4]
    random.shuffle(xl)
    a=answer_dict[xl.index(xa)]
    x1,x2,x3,x4,x5=xl[0],xl[1],xl[2],xl[3],xl[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,c3=c3)
    return stem,answer,comment

#2-1-3-86
def systemequations213_Stem_062():
    stem= "일차함수 $$수식$$y`=`f(x)$$/수식$$     에서 $$수식$$x`$$/수식$$의 값의 증가량에 대한 $$수식$$y`$$/수식$$의 값의 증가량의 비율이 $$수식$${a1}`$$/수식$$이고 $$수식$$f({a2})`=`{a3}$$/수식$$     일 때, $$수식$$f(k)`=`{a4}$$/수식$$    을 만족시키는 $$수식$$k`$$/수식$$의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$f(x)`=`{a1}x`+`b$$/수식$$      라 하면$$수식$$f({a2})`=`{a3}`$$/수식$$     이므로\n"\
             "$$수식$${a1}TIMES{a2}`+`b`=`{a3}~THEREFORE~b`=`{c1}$$/수식$$\n"\
             "따라서 $$수식$$f(x)`=`{a1}x`{sc1}$$/수식$$      이므로\n"\
             "$$수식$$f(k)`=`{a4}$$/수식$$     에서\n"\
             "$$수식$${a1}k`{sc1}`=`{a4}~THEREFORE~k`=`{c2}$$/수식$$\n\n"
    a1=random.randint(2,5)
    a2=random.randint(3,6)
    a3=random.randint(3,5)*a1
    while a3==a1*a2:
        a1=random.randint(2,5)
        a2=random.randint(3,6)
        a3=random.randint(3,5)*a1
    c1=a3-a1*a2
    sc1=made_sign_string(c1)
    a4=random.randint(2,4)*a1
    while a4==abs(c1):
        a4=random.randint(2,4)*a1
    c2=int((a4-c1)/a1)
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,sc1=sc1)
    return stem,answer,comment

#2-1-3-87
def systemequations213_Stem_063():
    stem= "일차함수 $$수식$$y`=`ax`+`b$$/수식$$   의 그래프는 일차함수 $$수식$$y`=`{a1}x`+`{a2}$$/수식$$   의 그래프와 평행하고,\n일차함수$$수식$$y`=`{a3}x`{a4}$$/수식$$   의 그래프와 $$수식$$x`$$/수식$$축에서 만난다. 이때 상수 $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$에 대하여 $$수식$$a`-`b$$/수식$$  의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "일차함수 $$수식$$y`=`{a1}x`+`{a2}$$/수식$$   의 그래프와 평행하므로\n"\
             "$$수식$$a`=`{a1}$$/수식$$\n"\
             "일차함수$$수식$$y`=`{a3}x`{a4}$$/수식$$   의 그래프의 $$수식$$x`$$/수식$$절편이\n"\
             "$$수식$${c1}$$/수식$$이므로 $$수식$$y`=`{a1}x`+`b$$/수식$$   의 $$수식$$x`$$/수식$$절편도\n"\
             "$$수식$${c1}$$/수식$$이다.\n"\
             "즉, $$수식$$0`=`{a1}TIMES{c1}`+`b$$/수식$$\n"\
             "$$수식$$THEREFORE~b`=`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`-`b`={c3}$$/수식$$\n\n"
    a1=random.randint(2,5)
    a2=random.randint(1,6)
    a3=random.randint(3,6)
    a4=-1*random.randint(2,5)*a3
    c1=int(-a4/a3)
    c2=-a1*c1
    c3=a1-c2
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3)
    return stem,answer,comment

#2-1-3-88
def systemequations213_Stem_064():
    stem= "일차함수 $$수식$$y`=`ax`+`b`$$/수식$$   의 그래프를 재홍이는 기울기를 잘못 보고 그려서 두 점$$수식$$LEFT ( {a1}`,~{a2} RIGHT )$$/수식$$ , $$수식$$LEFT ( {a3}`,~{a4} RIGHT )$$/수식$$  {proa4} 지나고, 미현이는 $$수식$$y`$$/수식$$절편을 잘못 보고 그려서 두 점$$수식$$LEFT ( {a5}`,~{a6} RIGHT )$$/수식$$ , $$수식$$LEFT ( {a7}`,~{a8} RIGHT )$$/수식$$  {proa8} 지난다고 한다. 일차함수 $$수식$$y`=`ax`+`b`$$/수식$$   의 그래프가 점 $$수식$$LEFT ( 2`,~k RIGHT )$$/수식$$ 를 지날 때, $$수식$$k`$$/수식$$의 값은? (단, $$수식$$a`,~b`$$/수식$$  는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	        ② $$수식$${x2}$$/수식$$	    ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$            ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "재홍이는 $$수식$$y`$$/수식$$ 절편을 제대로 보았고, 미현이는 기울기를 제대로 보았으므로\n"\
             "(기울기) $$수식$$= {{{{{a8}`-`{a6}}}}}over{{{{{a7}`-`{a5}}}}}`=`{c1}$$/수식$$\n\n"\
             "($$수식$$y`$$/수식$$절편) = $$수식$${a2}`-`{{{{{a4}`-`{a2}}}}}over{{{{{a3}`-`{a1}}}}}TIMES{a1}`=`{c2}$$/수식$$\n\n"\
             "따라서 일차함수의 식은 $$수식$$y`=`{c1}x`{sc2}$$/수식$$    이고,\n"\
             "점 $$수식$$LEFT ( 2`,~k RIGHT )$$/수식$$  를 지나므로\n"\
             "$$수식$$k`=`{c1}TIMES{{2}}`{sc2}`=`{c3}$$/수식$$\n"\
             "(힌트) 재홍이는 $$수식$$y`$$/수식$$절편을 제대로 보았고, 미현이는 기울기를 제대로 보았다.\n\n"
    a1=random.randint(2,5)
    a2=random.randint(3,6)
    a3=a1+1
    a4=random.randint(7,10)
    while a4==a2 or 2*a2==a4:
        a4=random.randint(5,10)
    tmp2=random.randint(3,5)
    a5=random.randint(2,5)
    a6=tmp2*a5
    a7=random.randint(6,7)
    a8=tmp2*a7
    proa4=proc_jo(a4,3)
    proa8=proc_jo(a8,3)
    while a7==a5:
        tmp2=random.randint(3,5)
        a5=random.randint(2,5)
        a6=tmp2*a5
        a7=random.randint(6,7)
        a8=tmp2*a7

    c1=int((a8-a6)/(a7-a5))
    c2=a2-int((a4-a2)/(a3-a1))*a1

    sc2=made_sign_string(c2)
    c3=2*c1+c2
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa4=proa4,proa8=proa8)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,c1=c1,c2=c2,sc2=sc2,c3=c3)
    return stem,answer,comment

#2-1-3-90
def systemequations213_Stem_065():
    stem= "일차함수 $$수식$$y`=`ax`+`b$$/수식$$    의 그래프의 $$수식$$x`$$/수식$$절편이 $$수식$${a1}`$$/수식$$, $$수식$$y`$$/수식$$절편이 $$수식$${a2}`$$/수식$$ 일 때, 일차함수 $$수식$$y`=`abx`+`(a`+`b)$$/수식$$       의 그래프의 기울기와 $$수식$$y`$$/수식$$절편의 차는? (단,$$수식$$a`,~b$$/수식$$    는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$x`$$/수식$$절편이 $$수식$${a1}`$$/수식$$, $$수식$$y`$$/수식$$절편이 $$수식$${a2}`$$/수식$$ 인 일차함수의 식은\n"\
             "$$수식$$y`=`{c1}x`{sa2}~ THEREFORE~a`=`{c1}`,`b`=`{a2}$$/수식$$\n"\
             "따라서 $$수식$$ab`=`{c2}`,~`a`+`b`=`{c3}$$/수식$$          이므로\n"\
             "$$수식$${c2}`-`{l3}{c3}{r3}`=`{c4}$$/수식$$\n\n"
    a1=random.randint(2,4)
    a2=random.randint(-3,-2)*a1
    c1=int(-a2/a1)
    sa2=made_sign_string(a2)
    c2=c1*a2
    c3=c1+a2
    c4=c2-c3
    l3,r3="",""
    if c3<0:
        l3,r3="(",")"
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,c1=c1,c2=c2,c3=c3,c4=c4,sa2=sa2,l3=l3,r3=r3)
    return stem,answer,comment

#2-1-3-91
def systemequations213_Stem_066():
    stem= "다음 중 $$수식$$x`$$/수식$$절편이 $$수식$${a1}`$$/수식$$이고 $$수식$$y`$$/수식$$절편이 $$수식$${a2}`$$/수식$$인 직선 위에 있지 않은 점은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$x`$$/수식$$절편이 $$수식$${a1}$$/수식$$이고 $$수식$$y`$$/수식$$절편이 $$수식$${a2}$$/수식$$인 일차함수 식은\n"\
             "$$수식$$y`=`{c1}x`+`{a2}$$/수식$$    이다.\n"\
             "{c2} 이므로 {a}가 직선위에 있지 않다.\n\n"
    a1=random.randint(-4,-1)
    a2=random.randint(2,3)*abs(a1)
    c1=int(-a2/a1)
    x1,x2,x3,x4="","","",""
    tmp=5*c1+a2+3
    x5="LEFT ( 5 `, ~{} RIGHT )".format(tmp)
    c2="$$수식$${tmp}`!=`{c1}TIMES{{5}}`+`{a2}$$/수식$$".format(tmp=tmp,c1=c1,a2=a2)
    l=[x1,x2,x3,x4,x5]
    for i in range(4):
        l[i]="LEFT ( {}`, ~{} RIGHT )".format(i,i*c1+a2)
    random.shuffle(l)
    a=answer_dict[l.index(x5)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,c1=c1,c2=c2,a=a)
    return stem,answer,comment
#2-1-3-93
def systemequations213_Stem_067():
    stem= "일차함수 $$수식$$y`=`f(x)`$$/수식$$   에 대하여 $$수식$${{f(2b)`-`f(3b)}}over{{3a`-`2b}}`=`{a1}$$/수식$$                     이고 그 그래프는 \n\n점 $$수식$$LEFT ( {a2}`,~{a3} RIGHT )$$/수식$$  {proa3} 지난다. $$수식$$f(x)`=`mx`+`n$$/수식$$      일 때, $$수식$$m`-`n$$/수식$$  의 값을 구하시오. (단, $$수식$$a`,`b`,`m`,`n$$/수식$$   은 상수이고, $$수식$$3a`!=`2b$$/수식$$   이다.)\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "(기울기)$$수식$$`=`m`=`-{{f(2b)`-`f(3b)}}over{{3a`-`2b}}`=`-`({a1})`=`{c1}$$/수식$$          이므로\n\n"\
             "$$수식$$f(x)`=`{c1}x`+`n$$/수식$$\n"\
             "또한, 점 $$수식$$LEFT ( {a2}`,~{a3} RIGHT )$$/수식$$  {proa3} 지나므로\n"\
             "$$수식$${a3}`=`{c1}TIMES{a2}`+`n~THEREFORE~n`=`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~m`-`n`=`{c3}$$/수식$$\n"\
             "(힌트)$$수식$${{f(b)`-`f(a)}}over{{b`-`a}}$$/수식$$             의 값은 함수$$수식$$y`=`f(x)`$$/수식$$"\
             "   의 그래프 위의 두 점 $$수식$$(a, f(a))$$/수식$$    , $$수식$$(b, f(b))$$/수식$$      \n\n를 지나는"\
             "직선의 기울기와 같다.\n\n"
    a1=random.randint(-5,-2)
    c1=-a1
    a2=random.randint(2,3)
    a3=random.randint(1,3)
    c2=a3-c1*a2
    c3=c1-c2
    proa3=proc_jo(a3,3)
    a=c3
    stem=stem.format(a1=a1,a2=a2,a3=a3,proa3=proa3)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,c1=c1,c2=c2,c3=c3,proa3=proa3)
    return stem,answer,comment

#2-1-3-94
def systemequations213_Stem_068():
    stem= "일차함수 $$수식$$y`=`ax{sa1}$$/수식$$    의 그래프가 상수$$수식$$a`$$/수식$$의 값에 관계없이 항상 지나는 점을 $$수식$$A`$$/수식$$라 하고, 일차함수 $$수식$$y`=`{a2}x`+`{a3}$$/수식$$    의 그래프와 평행한 일차함수$$수식$$y`=`bx`{sa4}$$/수식$$    의 그래프가 $$수식$$x`$$/수식$$축과 만나는 점을 $$수식$$B`$$/수식$$라 하자. 이때 두 점 $$수식$$A`$$/수식$$, $$수식$$B`$$/수식$$를 지나는 그래프가 나타내는 일차함수의 식은?\n"\
          "① $$수식$${x1}$$/수식$$	    ② $$수식$${x2}$$/수식$$	    ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$        ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "일차함수 $$수식$$y`=`ax{sa1}$$/수식$$    의 그래프는 기울기$$수식$$a`$$/수식$$ "\
             "와 관계없이 $$수식$$y`$$/수식$$절편 $$수식$$LEFT ( 0`,~{a1} RIGHT )$$/수식$$  를 지나므로 "\
             "$$수식$$A LEFT ( 0`,~{a1} RIGHT )$$/수식$$   이다.\n"\
             "두 일차함수 $$수식$$y`=`{a2}x`+`{a3}$$/수식$$   , $$수식$$y`=`bx`{sa4}$$/수식$$    의 그래프가 평행하므로 "\
             "$$수식$$b`=`{a2}$$/수식$$\n"\
             "따라서 주어진 식은 $$수식$$y`=`{a2}x`{sa4}$$/수식$$    이고 이 식의 $$수식$$x`$$/수식$$절편은 $$수식$${c1}`$$/수식$$이므로\n"\
             "$$수식$$B LEFT ( {c1}`, ~0 RIGHT )$$/수식$$   이다.\n"\
             "따라서 두 점$$수식$$A`$$/수식$$, $$수식$$B`$$/수식$$를 지나는 직선을 $$수식$$y`=`mx`+`n$$/수식$$     이라고 하면\n"\
             "(기울기)$$수식$$`=`m`=`{{0`-`({a1})}}over{{{c1}`-`0}}`=`{c2}$$/수식$$\n\n"\
             "($$수식$$y`$$/수식$$절편)$$수식$$`=n`=`{a1}`$$/수식$$\n"\
             "따라서 구하는 함수식은 "\
             "$$수식$$y`=`{c2}x`{sa1}$$/수식$$\n\n"
    a2=random.randint(2,5)
    tmp=random.randint(3,5)
    a4=-tmp*a2
    a1=-tmp*random.randint(2,5)
    sa1=made_sign_string(a1)
    a3=random.randint(5,15)
    c1=int(-a4/a2)
    c2=int(-a1/c1)
    sa4=made_sign_string(a4)
    xa="y`=`{c2}x`{sa1}".format(c2=c2,sa1=sa1)
    x1="y`=`{c2}x`+`{sa1}".format(c2=c2,sa1=abs(a1))
    x2="y`=`{c2}x`{sa1}".format(c2=-c2,sa1=sa1)
    x3="y`=`{c2}x`+`{sa1}".format(c2=-c2,sa1=abs(a1))
    x4="y`=`{tt}x`{sa1}".format(tt=2*c2,sa1=sa1)
    xl=[xa,x1,x2,x3,x4]
    random.shuffle(xl)
    a=answer_dict[xl.index(xa)]
    x1,x2,x3,x4,x5=xl[0],xl[1],xl[2],xl[3],xl[4]
    stem=stem.format(sa1=sa1,a2=a2,a3=a3,sa4=sa4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(sa1=sa1,a1=a1,a2=a2,a3=a3,sa4=sa4,c1=c1,c2=c2)
    return stem,answer,comment

#2-1-3-95
def systemequations213_Stem_069():
    stem= "온도가 $$수식$${a1}CENTIGRADE$$/수식$$인 물을 공기 중에 놓아두면 $$수식$${a2}$$/수식$$분이 지날 때마다 온도가 $$수식$${a3}CENTIGRADE$$/수식$$씩 내려가서 $$수식$$x`$$/수식$$분 후에는 $$수식$$y`CENTIGRADE$$/수식$$가 된다고 한다. 이때 물의 온도가 $$수식$${a4}``CENTIGRADE$$/수식$$가 되는 것은 몇 분 후인가?\n"\
          "① $$수식$${x1}$$/수식$$ 분 후	    ② $$수식$${x2}$$/수식$$ 분 후	    ③ $$수식$${x3}$$/수식$$ 분 후\n④ $$수식$${x4}$$/수식$$ 분 후        ⑤ $$수식$${x5}$$/수식$$ 분 후\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${a2}$$/수식$$분마다 $$수식$${a3}CENTIGRADE$$/수식$$씩 내려가므로, $$수식$$1`$$/수식$$분마다 $$수식$${c1}CENTIGRADE$$/수식$$씩 "\
             "내려간다.\n"\
             "따라서 $$수식$$x`$$/수식$$분 후에는 $$수식$${c1}x`CENTIGRADE$$/수식$$가 내려가므로 "\
             "$$수식$$y`=`{c2}x`+`{a1}$$/수식$$\n"\
             "$$수식$${a4}`=`{c2}x`+`{a1} THEREFORE~x`=`{c3}$$/수식$$\n"\
             "따라서 물의 온도가$$수식$${a4}CENTIGRADE$$/수식$$가 되는 것은 $$수식$${c3}$$/수식$$분 후이다.\n\n"
    
    a2=random.sample([10,20],1)[0]
    a3=random.sample([1,2,4,5],1)[0]
    a1=a3*100
    a4=random.randint(3,5)*a3
    c1=a3/a2
    c2=-c1
    c3=int((a4-a1)/c2)
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3)
    return stem,answer,comment

#2-1-3-96
def systemequations213_Stem_070():
    stem= "길이가 $$수식$${a1}``rm cm`$$/수식$$인 용수철은 $$수식$$rm  {a2}``g`$$/수식$$무게가 인 물건을 달 때마다 용수철의 길이가 $$수식$${a3}``rm cm$$/수식$$씩 늘어난다고 한다. 이 용수철에 $$수식$$rm  {a4}``g`$$/수식$$무게가 인 물건을 달았을 때, 용수철의 길이는?\n"\
          "① $$수식$${x1}``rm cm`$$/수식$$	② $$수식$${x2}``rm cm`$$/수식$$	  ③ $$수식$${x3}``rm cm`$$/수식$$\n④ $$수식$${x4}``rm cm`$$/수식$$     ⑤ $$수식$${x5}``rm cm`$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "용수철의 길이를$$수식$$y``rm cm`$$/수식$$ , 물건의 무게를 $$수식$$rm x``g`$$/수식$$이라"\
             "하면 무게가 $$수식$$rm  {a2}``g`$$/수식$$인 물건을 달았을 때 용수철의"\
             "길이가  $$수식$${a3}``rm cm$$/수식$$늘어났으므로 무게가 $$수식$$rm  1``g`$$/수식$$인"\
             "물건을 달면 용수철의 길이는 $$수식$${c1}rm``cm`$$/수식$$ 늘어난다.\n"\
             "$$수식$$THEREFORE~y`=`{c1}x`+`{a1}$$/수식$$\n"\
             "$$수식$$x=`{a4}`$$/수식$$  {proa4} 대입하면\n"\
             "$$수식$$y`=`{c1}TIMES{a4}`+`{a1}`=`{c2}$$/수식$$"
    a1=random.randrange(40,101,10)
    a2=random.randrange(10,71,20)
    a3=int(a2/10)*random.sample([2,5],1)[0]
    a4=random.randint(10,50)
    proa4=proc_jo(a4,3)
    c1=int(a2/a3)
    c2=c1*a4+a1
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,proa4=proa4)
    return stem,answer,comment

#2-1-3-97
def systemequations213_Stem_071():
    stem= "석유가  $$수식$$rm  {a1}``L`$$/수식$$들어 있는 석유난로가 있다. 이 난로는 $$수식$${a2}$$/수식$$분마다 $$수식$$rm {a3}``L`$$/수식$$씩 석유가 소모된다고 한다. 난로를 켠 지 몇 분 후에 석유가 $$수식$$rm{a4}``L`$$/수식$$가 남는가?\n"\
          "① $$수식$${x1}`$$/수식$$분	② $$수식$${x2}`$$/수식$$분	  ③ $$수식$${x3}`$$/수식$$분\n④ $$수식$${x4}`$$/수식$$분     ⑤ $$수식$${x5}`$$/수식$$분\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${a2}$$/수식$$분마다 $$수식$$rm {a3}``L`$$/수식$$씩의 석유가 소모되면"\
             "$$수식$$1`$$/수식$$분에 $$수식$$rm  {c1}``L`$$/수식$$씩 소모되므로"\
             "$$수식$$x`$$/수식$$분에는 $$수식$${c1}x``rm L$$/수식$$씩 소모된다.\n"\
             "따라서 난로를 켠 지 $$수식$$x`$$/수식$$분 후에 석유가 남아 있는 양을 $$수식$$y``rm  L`$$/수식$$라 하면\n"\
             "$$수식$$y`=`{a1}`-`{c1}x`$$/수식$$\n"\
             "따라서 $$수식$${a4}`=`{a1}`-`{c1}x`$$/수식$$     인 $$수식$$x`$$/수식$$를 구하면\n"\
             "$$수식$$THEREFORE~x`=`{c2}$$/수식$$(분)"
    a2=random.sample([10,20,40],1)[0]
    a3=int(a2/10)*random.sample([2,5],1)[0]
    c1=a3/a2
    a1=a3*50
    a4=a3*random.randrange(5,10)
    c2=int((a1-a4)/c1)
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2)
    return stem,answer,comment

#2-1-3-98
def systemequations213_Stem_072():
    stem= "서울에서 $$수식$${a1}``rm km`$$/수식$$떨어진 제주도 남쪽 해상에 있는 태풍이 계속해서 한 시간에 $$수식$${a2}``rm km`$$/수식$$의 속력으로 서해상을 따라 서울 쪽으로 북상하고 있다. $$수식$$x`$$/수식$$시간 후의 태풍과 서울 사이의 거리를 $$수식$$y``rm km`$$/수식$$라 할 때, $$수식$$y`$$/수식$$를 $$수식$$x`$$/수식$$에 대한 식으로 나타내고, 태풍이 서울에 도착하는 것은 제주도 남쪽 해상을 출발한 지 몇 시간 후인가?\n"\
          "① $$수식$${x1}$$/수식$$	\n② $$수식$${x2}$$/수식$$	  \n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     \n⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$x`$$/수식$$시간 동안 태풍이 북상한 거리는 $$수식$$rm``{a2}x``km`$$/수식$$이므로\n"\
             "$$수식$$y`=`{a1}`-`{a2}x`$$/수식$$\n"\
             "$$수식$$0`LEQ`y`LEQ`{a1} $$/수식$$에서 $$수식$$0`LEQ`{a1}`-`{a2}x`LEQ`{a1}$$/수식$$\n $$수식$$THEREFORE~0`LEQ`x`LEQ`{c1}$$/수식$$\n"\
             "태풍이 서울에 도착하면 태풍과 서울 사이의 거리는 $$수식$$0`$$/수식$$이므로\n"\
             "$$수식$$THEREFORE~x`=`{c1}$$/수식$$(시간)\n\n"
    a2=random.randrange(20,61,20)
    a1=a2*random.sample([16,32,48],1)[0]
    c1=int(a1/a2)
    x1,x2,x3,x4,xa="","","","",""
    x1="y`=`{a1}`-`{a2}x`({{0}}`LEQ`x`LEQ`{c1h})`,~{c1h}시간 후".format(a1=a1,a2=a2,c1h=int(c1/2))
    x2="y`=`{a1}`+`{a2}x`({{0}}`LEQ`x`LEQ`{c1h})`,~{c1h}시간 후".format(a1=a1,a2=a2,c1h=int(c1/2))
    xa="y`=`{a1}`-`{a2}x`({{0}}`LEQ`x`LEQ`{c1})`,~{c1}시간 후".format(a1=a1,a2=a2,c1=c1)
    x3="y`=`{a1}`+`{a2}x`({{0}}`LEQ`x`LEQ`{c1})`,~{c1}시간 후".format(a1=a1,a2=a2,c1=c1)
    x4="y`=`{a1}`-`{a2}x`({{0}}`LEQ`x`LEQ`{c1d})`,~{c1d}시간 후".format(a1=a1,a2=a2,c1d=2*c1)
    xl=[xa,x1,x2,x3,x4]
    random.shuffle(xl)
    a=answer_dict[xl.index(xa)]
    x1,x2,x3,x4,x5=xl[0],xl[1],xl[2],xl[3],xl[4]
    stem=stem.format(a1=a1,a2=a2,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,c1=c1)
    return stem,answer,comment

#2-1-3-100
def systemequations213_Stem_073():
    stem= "알코올 램프로 물을 데우면$$수식$$`{a1}`$$/수식$$ 분마다 온도가 $$수식$${a2}`CENTIGRADE$$/수식$$씩 올라가고 바닥에 내려놓으면 $$수식$${a3}`$$/수식$$분마다 온도가 $$수식$$`{a4}`CENTIGRADE$$/수식$$씩 내려간다고 한다. $$수식$$`{a5}CENTIGRADE$$/수식$$의 물을 $$수식$${a6}`CENTIGRADE$$/수식$$까지 데웠다가 바닥에 내려놓아 $$수식$${a7}`CENTIGRADE$$/수식$$까지 식히는 데 몇 분이 걸리는가?\n"\
          "① $$수식$${x1}`$$/수식$$분	② $$수식$${x2}`$$/수식$$분	  ③ $$수식$${x3}`$$/수식$$분\n④ $$수식$${x4}`$$/수식$$분     ⑤ $$수식$${x5}`$$/수식$$분\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "(ⅰ)$$수식$$x`$$/수식$$분 동안 물을 데웠을 때의 온도를 $$수식$$y`CENTIGRADE$$/수식$$라"\
             "하면\n"\
             "   물을 끓이면 1분에 $$수식$${c1}`CENTIGRADE$$/수식$$씩 온도가 상승하므로,\n"\
             "   $$수식$$y`=`{a5}`+`{c1}x`$$/수식$$ 이다.\n"\
             "   물을 $$수식$${a6}`CENTIGRADE$$/수식$$까지 데우는데 걸리는 시간은\n"\
             "   $$수식$${a6}`=`{a5}`+`{c1}x`$$/수식$$     인 $$수식$$x`$$/수식$$\n"\
             "   $$수식$$THEREFORE~x`=`{c2}$$/수식$$\n"\
             "(ⅱ)$$수식$$x`$$/수식$$분 동안 물을 바닥에 내려놓았을 때의 온도를"\
             "$$수식$$y`CENTIGRADE$$/수식$$라 하면\n"\
             "   바닥에 내려놓으면 1분에$$수식$${c3}`CENTIGRADE$$/수식$$씩 온도가 내려가므로,\n"\
             "   $$수식$$y`=`{a6}`-`{c3}x`$$/수식$$\n"\
             "   물을 $$수식$${a7}`CENTIGRADE$$/수식$$까지 식혀야 하므로 걸리는 시간은\n"\
             "   $$수식$${a7}`=`{c2}`-`{c2}x`$$/수식$$     인 $$수식$$x`$$/수식$$\n"\
             "   $$수식$$THEREFORE~x`=`{c4}$$/수식$$\n"\
             "(ⅰ), (ⅱ)에서 전체 걸린 시간은 $$수식$${c2}`+`{c4}`=`{c5}$$/수식$$    (분)"
    a1=random.randint(2,5)
    a2=random.randint(2,4)*a1
    a3=random.randint(2,5)
    a4=random.randint(2,3)*a3
    a5=random.randint(2,3)*a2
    a7=random.randint(2,3)*a4
    a6=a2*a4*random.randint(2,3)
    c1=int(a2/a1)
    c2=int((a6-a5)/c1)
    c3=int(a4/a3)
    c4=int((a6-a7)/c3)
    c5=c2+c4
    l=made_answer_cand_1(c5)
    random.shuffle(l)
    a=answer_dict[l.index(c5)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a5=a5,a6=a6,a7=a7,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    return stem,answer,comment

#2-1-3-101
def systemequations213_Stem_074():
    stem= "길이가 $$수식$${a1}``rm cm`$$/수식$$인 막대기 모양의 얼음을 실온에 두면 $$수식$${a2}`$$/수식$$분마다 길이가 $$수식$${a3}``rm cm`$$/수식$$씩 짧아진다고 한다. 실온에 둔 지 $$수식$$x`$$/수식$$분 후의 얼음의 길이를 $$수식$$rm y``cm`$$/수식$$라 할 때, 다음 설명 중 옳은 것은?\n"\
          "① {x1}	\n② {x2}	  \n③ {x3}\n④ {x4}     \n⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "① {c1}\n"\
             "② {c2}\n"\
             "③ {c3}\n"\
             "④ {c4}\n"\
             "⑤ {c5}\n\n"
    a2=random.randint(2,5)
    a3=random.randint(3,4)*a2
    a1=random.randint(3,5)*a3
    ra=a3*2
    coa=int(a3/a2)
    tt=random.randint(6,10)
    xa="녹은 얼음의 길이가 $$수식$$rm``{thtt} cm`$$/수식$$ 이 되는것은 $$수식$${ans}$$/수식$$분 후 이다.".format(thtt=int(a3/a2)*tt,ans=tt)
    ca="얼음의 길이는 1분마다 $$수식$$rm``{div} cm`$$/수식$$씩 녹으므로\n $$수식$${thtt}`=`{div}TIMES{tt}$$/수식$$".format(div=int(a3/a2),thtt=int(a3/a2)*tt,tt=tt)
    tmp=random.randint(5,20)
    rs=a1-int(a3/a2)*tmp
    while rs<=0:
        tmp=random.randint(5,20)
        rs=a1-int(a3/a2)*tmp
    x1="{tmp}분 후 얼음의 길이는 $$수식$$rm``{wrs} cm`$$/수식$$이다.".format(tmp=tmp,wrs=rs+random.randint(2,5))
    c1="{tmp}분 후 얼음의 길이는 $$수식$${a1}-{div}TIMES{tmp}`=`{rs}$$/수식$$".format(a1=a1,div=int(a3/a2),tmp=tmp,rs=rs)

    x2="얼음의 길이는 1분마다 $$수식$$rm``{} cm`$$/수식$$씩 짧아진다.".format(int(a3/a2)+3)
    c2="얼음의 길이는 1분마다 $$수식$$rm``{} cm`$$/수식$$씩 짧아진다.".format(int(a3/a2))

    x3="얼음이 다 녹는 데 걸리는 시간은{}분 이다.".format(int(a1/coa)+random.randint(2,5))
    c3="$$수식$$0`=`{a1}`-`{coa}x 이므로$$/수식$$\n$$수식$$THEREFORE~x`=`{div}$$/수식$$\n즉,얼음이 다 녹는 데 걸리는 시간은{div}분 이다.".format(a1=a1,coa=coa,div=int(a1/coa))

    ra2=int((a1-ra)/coa)

    x4="얼음의 길이가$$수식$$rm``{ra} cm`$$/수식$$이 되는것은 실온에 둔 지{wra2}분 후 이다.".format(ra=ra,wra2=ra2+random.randint(2,5))
    c4="$$수식$${ra}`=`{a1}`-`{coa}x`$$/수식$$   에서\n$$수식$$x`=`{ra2}$$/수식$$   이므로\n얼음의 길이가$$수식$$rm``{ra} cm`$$/수식$$이 되는것은 실온에 둔 지{ra2}분 후 이다.".format(a1=a1,ra=ra,coa=coa,ra2=ra2)

    xal=[xa,ca]
    x1l=[x1,c1]
    x2l=[x2,c2]
    x3l=[x3,c3]
    x4l=[x4,c4]

    xl=[xal,x1l,x2l,x3l,x4l]
    random.shuffle(xl)

    a=answer_dict[xl.index(xal)]

    x1,x2,x3,x4,x5=xl[0][0],xl[1][0],xl[2][0],xl[3][0],xl[4][0]
    c1,c2,c3,c4,c5=xl[0][1],xl[1][1],xl[2][1],xl[3][1],xl[4][1]

    stem=stem.format(a1=a1,a2=a2,a3=a3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    return stem,answer,comment

#2-1-3-102
def systemequations213_Stem_075():
    stem= "A, B 두 물통이 있다.$$수식$$A`$$/수식$$  물통에는 $$수식$$rm``{a1}  L`$$/수식$$, $$수식$$B`$$/수식$$물통에는 $$수식$$rm``{a2}  L`$$/수식$$의 물이 들어 있는데 $$수식$$A`$$/수식$$ 물통에는 매분 $$수식$$rm``{a3}  L`$$/수식$$의 물을 넣고, $$수식$$B`$$/수식$$ 물통에는 매분 $$수식$$rm``{a4}  `L$$/수식$$의 물을 빼낸다.$$수식$$x`$$/수식$$ 분 후의 물의 양을 $$수식$$y`rm``  L`$$/수식$$라 할 때, 두 물통의 물의 양이 같아지는 것은 몇 분 후인가?\n"\
          "① $$수식$${x1}`$$/수식$$분 후	② $$수식$${x2}`$$/수식$$분 후	  ③ $$수식$${x3}`$$/수식$$분 후\n④ $$수식$${x4}`$$/수식$$분 후     ⑤ $$수식$${x5}`$$/수식$$분 후\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$A`$$/수식$$ 물통에는 $$수식$$rm``{a1}  L`$$/수식$$의 물이 들어 있는데 매분 $$수식$$rm``{a3}  L`$$/수식$$의 물을 넣으므로 $$수식$$x`$$/수식$$분 후의  물통의 물의 양은 $$수식$$LEFT ({a1}`+`{a3}x RIGHT )`rm`` L`$$/수식$$이다.\n"\
             "또, $$수식$$B`$$/수식$$ 물통에는 $$수식$$rm``{a2}  L`$$/수식$$의 물이 들어 있는데 매분  $$수식$$rm``{a4}  `L$$/수식$$의 물을 빼내므로 $$수식$$x`$$/수식$$분 후의  물통의 물의 양은$$수식$$LEFT ( {a2}`-`{a4}x RIGHT )`rm`` L`$$/수식$$ 이다.\n"\
             "$$수식$$x`$$/수식$$분 후에 두 물통의 물의 양이 같아지므로\n"\
             "$$수식$${a1}`+`{a3}x`=`{a2}`-`{a4}x$$/수식$$\n"\
             "$$수식$$THEREFORE~x`=`{c1}$$/수식$$\n"\
             "따라서 두 물통의 물의 양이 같아지는 것은 $$수식$${c1}$$/수식$$분 \n후 이다.\n\n"
    a3=random.randint(2,5)
    a4=random.randint(2,3)
    a1=(a3+a4)*random.randint(1,2)
    a2=(a3+a4)*random.randint(5,8)
    c1=int((a2-a1)/(a3+a4))
    l=made_answer_cand_1(c1)
    random.shuffle(l)
    a=answer_dict[l.index(c1)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1)
    return stem,answer,comment


#2-1-3-104
def systemequations213_Stem_076():
    stem= "찬호와 서연이가 직선 도로를 따라 달리기를 하는데 서연이가 찬호보다 $$수식$${a1}`rm``m`$$/수식$$앞에서 출발하였다. 두 사람이 동시에 출발하여 찬호는 초속$$수식$${a2}`rm``m`$$/수식$$, 서연이는 초속 $$수식$${a3}`rm``m`$$/수식$$로 달릴 때, 찬호가 서연이를 따라잡는 데 걸리는 시간은?\n"\
          "① $$수식$${x1}$$/수식$$초 후	② $$수식$${x2}$$/수식$$초 후	  ③ $$수식$${x3}$$/수식$$초 후\n④ $$수식$${x4}$$/수식$$초 후     ⑤ $$수식$${x5}$$/수식$$초 후\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "출발한 지 $$수식$$x`$$/수식$$초 후의 출발선에서부터 찬호의 위치까지의 거리는 $$수식$${a2}x`rm``m`$$/수식$$이고, 서연이의 위치까지의 거리는 $$수식$$LEFT ( {a1}`+`{a3}x RIGHT )`rm``m`$$/수식$$이므로 두 사람 사이의 거리를 $$수식$$y`$$/수식$$라 하면\n"\
             "$$수식$$y`=`{a1}`+`{a3}x`-`{a2}x`$$/수식$$    , 즉 $$수식$$y`=`{a1}`-`{c1}x`$$/수식$$\n"\
             "$$수식$$0`=`{a1}`-`{c1}x`$$/수식$$    에서 $$수식$$x`=`{c2}$$/수식$$    이므로\n"\
             "찬호가 서연이를 따라잡는 데 걸리는 시간은 $$수식$${c2}$$/수식$$초 이다.\n\n"
    a2=random.randint(5,10)
    a3=random.randint(2,4)
    a1=(a2-a3)*random.randint(5,10)
    c1=abs(a3-a2)
    c2=int(a1/c1)
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,c1=c1,c2=c2)
    return stem,answer,comment

#2-1-3-106
def systemequations213_Stem_077():
    stem= "민혁이가 어느 음원 사이트에서 $$수식$${a1}`$$/수식$$  원을 내면 $$수식$${a2}$$/수식$$곡을 내려 받을 수 있고, $$수식$${a2}`$$/수식$$곡을 초과하는 경우 한 곡당 $$수식$${a3}`$$/수식$$  원을 내는 상품에 가입하였다. 민혁이가 $$수식$${a4}`$$/수식$$ 원으로 몇 곡을 내려 받을 수 있는가?\n"\
          "① $$수식$${x1}`$$/수식$$곡	② $$수식$${x2}`$$/수식$$곡	  ③ $$수식$${x3}`$$/수식$$곡\n④ $$수식$${x4}`$$/수식$$곡     ⑤ $$수식$${x5}`$$/수식$$곡\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$x`(x`&gt;`{a2})$$/수식$$    곡을 내려 받을 때 내야 하는 금액을 $$수식$$y`$$/수식$$원이라 하면\n"\
             "$$수식$$y`=`{a1}`+`{{(x`-`{a2})}}TIMES{a3}$$/수식$$\n"\
             "즉,$$수식$$y`=`{a3}x`{sc1}$$/수식$$\n"\
             "$$수식$$y`=`{a4}$$/수식$$    을 대입하면 $$수식$${a4}`=`{a3}x`{sc1}$$/수식$$\n"\
             "$$수식$$THEREFORE~x`=`{c2}$$/수식$$\n"\
             "따라서 민혁이는 $$수식$${c2}`$$/수식$$곡을 내려 받을 수 있다.\n\n"
    a3=random.randrange(300,501,10)
    a2=random.randrange(100,201,10)
    a1=random.randrange(30,51,10)*a3
    a4=random.randrange(100,201,10)*a3
    c1=a1-a2*a3
    sc1=made_sign_string(c1)
    c2=int((a4-c1)/a3)
    l=made_answer_cand_1(c2)
    random.shuffle(l)
    a=answer_dict[l.index(c2)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,sc1=sc1,c2=c2)
    return stem,answer,comment

#2-1-3-108
def systemequations213_Stem_078():
    stem= "주전자에 물을 끓이면$$수식$${a1}`$$/수식$$ 분에 온도가 $$수식$${a2}`CENTIGRADE$$/수식$$씩 올라가고 불을 끄면 $$수식$${a3}$$/수식$$분에 온도가 $$수식$${a4}`CENTIGRADE$$/수식$$씩 내려간다고 한다. $$수식$${a5}CENTIGRADE$$/수식$$의 물을 $$수식$${a6}`CENTIGRADE$$/수식$$까지 데웠다가 불을 껐더니 몇 분 후에 $$수식$${a7}`CENTIGRADE$$/수식$$가 되었다. $$수식$${a7}`CENTIGRADE$$/수식$$의 물을 얻기 위해 걸린 시간은 모두 몇 분인가?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "물을 끓이면 1분에 $$수식$${c1}`CENTIGRADE$$/수식$$씩 온도가 상승하므로,\n"\
             "$$수식$$x`$$/수식$$분 후 물의 온도를 $$수식$$y`CENTIGRADE$$/수식$$라고 하면\n"\
             "$$수식$$y`=`{a5}`+`{c1}x`$$/수식$$    이다.\n"\
             "따라서 물의 온도가 $$수식$${a6}`CENTIGRADE$$/수식$$까지 올라가는데 걸리는 시간은\n"\
             "$$수식$${a6}`=`{a5}`+`{c1}x`~THEREFORE~x`=`{c2} CDOTS CDOTS(1)$$/수식$$\n"\
             "불을 끄면 1분에$$수식$${c3}`CENTIGRADE$$/수식$$씩 온도가 내려가므로,\n"\
             "$$수식$$x`$$/수식$$분 후 물의 온도를 $$수식$$y`CENTIGRADE$$/수식$$라고 하면\n"\
             "$$수식$$y`=`{a6}`-`{c3}x`$$/수식$$    이다.\n"\
             "따라서 물의 온도가 $$수식$${a7}`CENTIGRADE$$/수식$$까지 내려가는데 걸리는 시간은\n"\
             "$$수식$${a7}`=`{a6}`-`{c3}x`~THEREFORE~x`=`{c4} CDOTS CDOTS(2)$$/수식$$\n"\
             "(1), (2)에 의해서 총 걸린 시간은\n$$수식$${c5}$$/수식$$  (분)\n\n"
    a1=random.randint(1,5)
    a3=random.randint(1,5)
    while a1==a3:
        a3=random.randint(1,5)
    a2=random.randint(3,5)*a1
    a4=random.randint(3,5)*a3
    while a2==a4:
        a4=random.randint(3,5)*a3
    c1=int(a2/a1)
    c3=int(a4/a3)
    a5=random.randint(3,4)*a2
    a7=random.randint(3,4)*a4
    a6=random.randint(3,4)*a2*a4
    c2=int((a6-a5)/c1)
    c4=int((a6-a7)/c3)
    c5=c2+c4
    l=made_answer_cand_1(c5)
    random.shuffle(l)
    a=answer_dict[l.index(c5)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    return stem,answer,comment

#2-1-3-110
def systemequations213_Stem_079():
    stem= "물이 들어 있는 원기둥 모양의 물통이 있다. 이 물통에 일정한 속도로 물을 채우기 시작한 지 $$수식$${a1}$$/수식$$분 후의 물의 높이는 $$수식$${a2}``rm cm`$$/수식$$이고, $$수식$${a3}$$/수식$$분 후의 물의 높이는 $$수식$${a4}``rm cm`$$/수식$$이었다. 처음에 들어 있던 물의 높이는?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${c1}$$/수식$$분 동안 물의 높이가 $$수식$${c2}`rm``cm`$$/수식$$높아졌으므로 1 분마다 $$수식$${c3}`rm``cm`$$/수식$$씩 높아진다. 처음에 들어 있던 물의 높이를 $$수식$$k`rm``cm`$$/수식$$ , $$수식$$x`$$/수식$$분 후의 물의 높이를 $$수식$$y`rm``cm`$$/수식$$라 하면\n"\
             "$$수식$$y`=`k`+`{c3}x`$$/수식$$\n"\
             "$$수식$$x`=`{a1}$$/수식$$    을 대입하면$$수식$$y`=`{a2}$$/수식$$    이므로\n"\
             "$$수식$${a2}`=`k`+`{c3}TIMES{a1}$$/수식$$\n"\
             "$$수식$$THEREFORE~k`=`{c4}$$/수식$$\n"\
             "따라서 처음에 들어 있던 물의 높이는 $$수식$${c4}`rm``cm`$$/수식$$이다.\n\n"
    a1=random.randrange(10,31,10)
    a3=random.randint(50,80)
    a2=random.randint(2,3)*(a3-a1)
    a4=random.randint(5,8)*(a3-a1)
    while a2*a3-a4*a1<=0:
        a1=random.randrange(10,31,10)
        a3=random.randint(35,40)
        a2=random.randint(2,3)*(a3-a1)
        a4=random.randint(5,8)*(a3-a1)
    c1=a3-a1
    c2=a4-a2
    c3=int(c2/c1)
    c4=a2-c3*a1
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,c4=c4)
    return stem,answer,comment

#2-1-3-112
def systemequations213_Stem_080():
    stem= "기온이 $$수식$$0`CENTIGRADE$$/수식$$일 때, 공기 중에서 소리의 속력은 초속$$수식$$331`rm``m`$$/수식$$ 이고, 기온이  $$수식$${a1}`CENTIGRADE$$/수식$$오를 때마다 속력은 초속 $$수식$${a2}`rm``m`$$/수식$$씩 증가한다고 한다. 기온이 $$수식$${a3}`CENTIGRADE$$/수식$$인 어느 날 소현이는 친구와 등산을 하고 산 정상에 올라가 앞의 절벽을 향해 ‘야호’하고 소리를 지른 다음 $$수식$${a4}`$$/수식$$초 후에 메아리 소리를 들었다. 이때 산 정상과 절벽 사이의 거리는 몇 $$수식$$rm`m`$$/수식$$인지 구하시오. (단, 소리의 이동 경로는 산 정상과 절벽 사이의 직선거리이다.)\n\n"
    answer= "(정답)\n{a}$$수식$$rm`m`$$/수식$$\n"
    comment= "(해설)\n"\
             "기온이 $$수식$$x`CENTIGRADE$$/수식$$일 때의 소리의 속력을 초속 $$수식$$y``rm`m`$$/수식$$라 하면\n"\
             "$$수식$$y`=`331`+`{c1}x`$$/수식$$\n"\
             "기온이 $$수식$${a3}`CENTIGRADE$$/수식$$이므로 소리의 속력은\n "\
             "$$수식$$y`=`331`+`{c1}TIMES{a3}`=`{c2}$$/수식$$\n"\
             "즉, 초속 $$수식$${c2}`rm``m`$$/수식$$이다. 소현이가 소리를 지른 다음 메아리 소리를 들을 때까지 $$수식$${a4}`$$/수식$$초가 걸렸으므로 소리가 산 정상에서 절벽까지 도달하는 데는 $$수식$${c3}$$/수식$$초가 걸렸다.\n"\
             "따라서 산 정상과 절벽 사이의 거리는\n"\
             "$$수식$${c2}TIMES{c3}`=`{c4}$$/수식$$\n\n"
    a1=random.randint(1,5)
    a2=random.randint(1,3)*a1
    a3=random.randrange(20,31,10)
    a4=random.randrange(2,7,2)
    c1=int(a2/a1)
    c2=331+c1*a3
    c3=int(a4/2)
    c4=c2*c3
    a=c4
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,c4=c4)
    return stem,answer,comment

#2-1-3-114
def systemequations213_Stem_081():
    stem= "다음 중 일차방정식 $$수식$${a1}x`+`{a2}y`{sa3}`=`0$$/수식$$    의 그래프에 대한 설명으로 옳지 않은 것은?\n"\
          "① {x1}	\n② {x2}	  \n③ {x3}\n④ {x4}     \n⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${a1}x`+`{a2}y`{sa3}`=`0$$/수식$$     에서 $$수식$$y`$$/수식$$를 $$수식$$x`$$/수식$$의 식으로 나타내면\n"\
             "$$수식$$y`=`{c1}x`{sc2}$$/수식$$\n"\
             "{a} {c3}\n\n"
    a2=random.randint(2,5)
    tmp=random.randint(3,4)
    a1=tmp*a2
    a3=random.randint(-2,2)*a2*tmp
    while a3==0:
        a3=random.randint(-2,2)*a2*tmp
    c1=int(-a1/a2)
    sa3=made_sign_string(a3)
    x_in=int(-a3/a1)
    y_in=int(-a3/a2)
    sc2=made_sign_string(y_in)
    cord=random.sample([2,4],1)[0]
    y_in_add=made_sign_string(y_in+random.randint(3,7))
    x1="기울기는 {c1}이다.".format(c1=c1)
    x2="$$수식$$x`$$/수식$$절편은 $$수식$${x_in}$$/수식$$이고, $$수식$$y`$$/수식$$절편은 $$수식$${y_in}$$/수식$$이다.".format(x_in=x_in,y_in=y_in)
    x3="제$$수식$${cord}$$/수식$$사분면을 지난다.".format(cord=cord)
    x4="$$수식$$y`=`{c1}x`{y_in_add}$$/수식$$    의 그래프와 평행하다.".format(c1=c1,y_in_add=y_in_add)
    cc1=random.randint(2,3)
    cc2=cc1*abs(c1)
    xa="$$수식$$x`$$/수식$$값이 $$수식$${cc1}$$/수식$$만큼 증가할때, $$수식$$y`$$/수식$$의 값은 $$수식$${cc2}$$/수식$$ 만큼 증가한다.".format(cc1=cc1,cc2=cc2)
    c3="기울기가 {c1}이므로 의 $$수식$$x`$$/수식$$값이 $$수식$${cc1}$$/수식$$만큼 증가할 때, $$수식$$y`$$/수식$$의 값은 $$수식$${cc2}$$/수식$$만큼 감소한다.".format(c1=c1,cc1=cc1,cc2=cc2)
    xl=[x1,x2,x3,x4,xa]
    random.shuffle(xl)
    x1,x2,x3,x4,x5=xl[0],xl[1],xl[2],xl[3],xl[4]
    a=answer_dict[xl.index(xa)]
    stem=stem.format(a1=a1,a2=a2,sa3=sa3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,sa3=sa3,c1=c1,sc2=sc2,c3=c3,a=a)
    return stem,answer,comment

#2-1-3-115
def systemequations213_Stem_082():
    stem= "일차방정식 $$수식$${a1}x`+`y`=`{a2}$$/수식$$    의 그래프가 점$$수식$$LEFT ( a`,~{a3}a`{sa4} RIGHT )$$/수식$$    {proa4} 지날 때, $$수식$$a`$$/수식$$의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$x`=`a`,~y`=`{a3}a`{sa4}$$/수식$$       {proa4} $$수식$${a1}x`+`y`=`{a2}$$/수식$$      에 대입하면\n"\
             "$$수식$${a1}a`+`{a3}a`{sa4}`=`{a2},~{c1}a`=`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`=`{c3}$$/수식$$"
    a1=random.randint(-5,5)
    a3=random.randint(2,5)
    while abs(a1)==1 or a1+a3==0 or a1==0:
        a1=random.randint(-5,5)
        a3=random.randint(2,5)
    a2=random.randint(4,5)*(a1+a3)
    a4=random.randint(2,3)*(a1+a3)
    sa4=made_sign_string(a4)
    proa4=proc_jo(a4,3)
    c1=a1+a3
    c2=a2-a4
    c3=int(c2/c1)
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,sa4=sa4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa4=proa4)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,sa4=sa4,c1=c1,c2=c2,c3=c3,proa4=proa4)
    return stem,answer,comment

#2-1-3-116
def systemequations213_Stem_083():
    stem= "일차방정식 $$수식$${a1}x`+`{a2}y`{a3}`=`0`$$/수식$$     의 그래프의 기울기를 $$수식$$a`$$/수식$$, $$수식$$x`$$/수식$$절편을 $$수식$$b`$$/수식$$, $$수식$$y`$$/수식$$절편을 $$수식$$c`$$/수식$$라 할 때, $$수식$${a4}abc`$$/수식$$ 의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${a1}x`+`{a2}y`{a3}`=`0`$$/수식$$     에서 $$수식$$y`=`{c1}x`+`{c2}$$/수식$$\n"\
             "따라서 기울기 $$수식$$a`$$/수식$$  는 $$수식$${c1}`$$/수식$$, $$수식$$x`$$/수식$$ 절편 $$수식$$b`$$/수식$$  는 $$수식$${c3}$$/수식$$\n"\
             "$$수식$$y`$$/수식$$ 절편 $$수식$$c`$$/수식$$  는 $$수식$${c2}`$$/수식$$ 이다.\n"\
             "$$수식$$THEREFORE~{a4}abc`=`{a4}TIMES{c1}TIMES({c3})TIMES{c2}`=`{c4}$$/수식$$\n\n"
    a2=random.randint(2,4)
    tmp=random.randint(-6,-4)
    a1=tmp*a2
    a3=random.randint(-3,-2)*a2*abs(tmp)
    a4=random.randint(2,5)
    c1=int(-a1/a2)
    c2=int(-a3/a2)
    c3=int(-a3/a1)
    c4=a4*c1*c2*c3
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,c4=c4)
    return stem,answer,comment


#2-1-3-117
def systemequations213_Stem_084():
    stem= "두 일차방정식 $$수식$$y`=`ax`+`{a1}$$/수식$$    {proa1} $$수식$${a2}x`+`{a3}y=`{a4}$$/수식$$    의 그래프가 만나지 않을 때, 다음 중 직선 $$수식$$y`=`ax`+`{a1}$$/수식$$   위의 점이 아닌 것은? (단,$$수식$$a`$$/수식$$ 는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${a2}x`+`{a3}y=`{a4}$$/수식$$      {proa4} $$수식$$y`$$/수식$$ 에 대하여 정리하면\n"\
             "$$수식$$y`=`{c1}x`+`{c2}`$$/수식$$\n"\
             "두 직선이 만나지 않으려면 평행해야 하므로 기울기가 같아야 한다.\n"\
             "즉, $$수식$$a`=`{c1}$$/수식$$\n"\
             "$$수식$$THEREFORE~y`=`{c1}x`+`{a1}$$/수식$$\n"\
             "일차함수 $$수식$$THEREFORE~y`=`{c1}x`+`{a1}$$/수식$$에 점의 좌표를\n"\
             "대입하여 등식이 성립하지 않는 것을 찾으면\n"\
             "{a} {c3}\n\n"
    a1=random.randint(2,5)
    a3=random.randint(2,5)
    a2=random.randint(-4,-2)*a3
    a4=random.randint(2,3)*a3
    c1=int(-a2/a3)
    c2=int(a4/a3)
    proa1=proc_jo(a1,2)
    proa4=proc_jo(a4,3)
    x1,x2,x3,x4,xa="","","","",""
    l=[x1,x2,x3,x4]
    for i in range(4):
        l[i]="LEFT ( {i},~{re} RIGHT )".format(i=i,re=i*c1+a1)
    xa="LEFT ( 4,~{wre} RIGHT )".format(wre=4*c1-a1)
    l.append(xa)
    random.shuffle(l)
    a=answer_dict[l.index(xa)]
    c3="$$수식$${wre}`!=`{c1}TIMES{cc4}+{a1}`=`{re}$$/수식$$".format(wre=4*c1-a1,c1=c1,a1=a1,re=4*c1+a1,cc4=4)
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa1=proa1)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,a=a,proa4=proa4)
    return stem,answer,comment

#2-1-3-118
def systemequations213_Stem_085():
    stem= "일차방정식 $$수식$$y`=`{a1}x`+`{a2}$$/수식$$    의 그래프와 $$수식$$x`$$/수식$$축 위에서 만나고, $$수식$$y`$$/수식$$절편이 $$수식$${a3}`$$/수식$$인 직선을 그래프로 하는 일차방정식을 $$수식$$ax`+`by`+`{a4}`=`0$$/수식$$    이라 할 때, 두 상수 $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$에 대하여 $$수식$$ab`$$/수식$$의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "일차방정식 $$수식$$y`=`{a1}x`+`{a2}$$/수식$$    의 그래프와 $$수식$$x`$$/수식$$축 위에서 만나므로"\
             "$$수식$$x`$$/수식$$절편이 같다.\n"\
             "$$수식$$y`=`{a1}x`+`{a2}$$/수식$$    의 $$수식$$x`$$/수식$$절편은 "\
             "$$수식$$0`=`{a1}x`+`{a2}$$/수식$$    에서 $$수식$$x`=`{c1}$$/수식$$\n"\
             "즉 $$수식$$x`$$/수식$$ 절편이 $$수식$${c1}`$$/수식$$, $$수식$$y`$$/수식$$ 절편이 $$수식$${a3}$$/수식$$  인 "\
             "일차방정식의 그래프 이므로\n"\
             "$$수식$$y`=`{c2}x`+`{a3}$$/수식$$    에서\n"\
             "$$수식$${c3}x`{c4}y`+`{a4}`=`0$$/수식$$\n"\
             "$$수식$$THEREFORE~a`=`{c3}`,`b`=`{c4}`$$/수식$$\n"\
             "$$수식$$THEREFORE~ab`=`{c5}$$/수식$$\n\n"
    a1=random.randint(2,5)
    a2=random.randint(2,4)*a1
    a3=random.randint(2,5)*a2
    a4=a2*a3
    c1=int(-a2/a1)
    while abs(c1)==a3:
        a1=random.randint(2,5)
        a2=random.randint(2,4)*a1
        a3=random.randint(2,5)
        a4=a2*a3
        c1=int(-a2/a1)
    c2=int(-a3/c1)
    c3=a1*a3
    c4=-a2
    c5=c3*c4
    l=made_answer_cand_1(c5)
    random.shuffle(l)
    a=answer_dict[l.index(c5)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    return stem,answer,comment
    
#2-1-3-119
def systemequations213_Stem_086():
    stem= "일차방정식 $$수식$$({a1}a`+`{a2})`x`-`by`+`{a3}`=`0$$/수식$$        의 그래프의 기울기가 $$수식$${a4}`$$/수식$$, $$수식$$y`$$/수식$$절편이 $$수식$${a5}`$$/수식$$일 때, 상수 $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$에 대하여 $$수식$$a`-`b$$/수식$$    의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"    
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$({a1}a`+`{a2})`x`-`by`+`{a3}`=`0$$/수식$$        에서\n"\
             "$$수식$$y`=`{{({a1}a`+`{a2})}}over{be}`x`+`{a3}over{be}$$/수식$$\n\n\n"\
             "따라서 $$수식$${{({a1}a`+`{a2})}}over{be}`=`{a4}` ,~{a3}over{be}`=`{a5}$$/수식$$\n\n\n"\
             "$$수식$$a`=`{c1}`,~b`=`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`-`b`=`{c1}`-`{c2}`=`{c3}$$/수식$$\n\n"
    a1=random.randint(3,5)
    a2=random.randint(2,3)*a1
    a5=random.randint(4,6)
    a3=random.randint(2,3)*a5
    a4=random.randint(3,5)*a1
    while a3*a4-a2*a5==0:
        a1=random.randint(3,5)
        a2=random.randint(2,3)*a1
        a5=random.randint(4,6)
        a3=random.randint(2,3)*a5
        a4=random.randint(3,5)*a1
    be="b"
    c2=int(a3/a5)
    c1=int((a4*c2-a2)/a1)
    c3=c1-c2  
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,be=be,c1=c1,c2=c2,c3=c3)
    return stem,answer,comment

#2-1-3-120
def systemequations213_Stem_087():
    stem= "두 점 $$수식$$({a1}`,~{a2})$$/수식$$    , $$수식$$({a3}`,~{a4})$$/수식$$    {proa4} 지나는 직선과 일차방정식 $$수식$$ax`+`{a5}y`+`{a6}`=`0`$$/수식$$      의 그래프가 서로 평행할 때, 상수 $$수식$$a`$$/수식$$의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "주어진 두 점을 지나는 직선의 기울기는\n"\
             "$$수식$${{{a4}`-`{a2}}}over{{{a3}`-`{a1}}}`=`{c1}$$/수식$$\n\n\n"\
             "$$수식$$ax`+`{a5}y`+`{a6}`=`0`$$/수식$$      에서 $$수식$$y`=`-`{{a}}over{a5}`x`{c2}$$/수식$$\n\n\n"\
             "따라서 $$수식$${c1}`=`-`{{a}}over{a5}$$/수식$$      이므로$$수식$$a`=`{c3}$$/수식$$\n\n "
    a1=random.randint(2,3)
    a3=random.randint(4,7)
    a2=random.randint(2,4)*(a3-a1)
    a4=(a3-a1)*random.randint(5,6)
    c1=int((a4-a2)/(a3-a1))
    a5=random.randint(3,5)
    a6=random.randint(2,3)*a5
    c2=int(-a6/a5)
    c3=-a5*c1
    proa4=proc_jo(a4,3)
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa4=proa4)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,c1=c1,c2=c2,c3=c3)
    return stem,answer,comment

#2-1-3-121
def systemequations213_Stem_088():
    stem= "일차방정식 $$수식$${a1}x`-`ay`+`{a2}`=`0$$/수식$$      의 그래프가 일차함수 $$수식$$y`=`{a3}x`+`{a4}$$/수식$$      의 그래프와 평행하고, 점 $$수식$$`({a5}`,~b)`$$/수식$$    를 지날 때, $$수식$$a`+`b`$$/수식$$    의 값은? (단,$$수식$$a`$$/수식$$ 는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${a1}x`-`ay`+`{a2}`=`0$$/수식$$      에서 $$수식$$y`=`{a1}over{{a}}`x`+`{a2}over{{a}}$$/수식$$\n\n\n"\
             "따라서 $$수식$${a3}`=`{a1}over{{a}}$$/수식$$    이므로 $$수식$$a`=`{c1}$$/수식$$\n\n\n"\
             "$$수식$$y`=`{a3}x`+`{c2}$$/수식$$    의 그래프가 점 $$수식$$`({a5}`,~b)`$$/수식$$    를 지나므로\n"\
             "$$수식$$b`=`{c1}TIMES{a5}`+`{c2}`~THEREFORE~b`=`{c3}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`+`b`=`{c4}$$/수식$$\n\n"
    a3=random.randint(3,5)
    tmp=random.randint(2,3)
    a1=tmp*a3
    a2=tmp*random.randint(6,7)
    a4=random.randint(1,3)
    a5=random.randint(2,4)
    c1=int(a1/a3)
    c2=int(a2/c1)
    c3=c1*a5+c2
    c4=c1+c3
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,c3=c3,c4=c4)
    return stem,answer,comment

#2-1-3-122
def systemequations213_Stem_089():
    stem= "일차함수 $$수식$$y`=`ax`+`{a1}$$/수식$$    의 그래프와 일차방정식 $$수식$${a2}x`-`by`+`{a3}`=`0$$/수식$$      의 그래프가 서로 일치할 때, $$수식$$a`+`b$$/수식$$  의 값은? (단, $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$는 $$수식$$0`$$/수식$$이 아닌 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "일차방정식 $$수식$${a2}x`-`by`+`{a3}`=`0$$/수식$$      에서\n"\
             "$$수식$$y`=`{a2}over{{b}}`x`+`{a3}over{{b}}$$/수식$$\n\n\n"\
             "두 일차함수의 그래프가 일치 하므로,\n"\
             "$$수식$${a1}`=`{a3}over{{b}}$$/수식$$  , $$수식$$a`=`{a2}over{{b}}$$/수식$$\n\n\n"\
             "$$수식$$THEREFORE~b`=`{c1}`,~a`=`{c2}`$$/수식$$\n"\
             "$$수식$$THEREFORE~a`+`b`=`{c3}$$/수식$$"
    a1=random.randint(3,5)
    tmp=random.randint(4,6)
    a2=tmp*random.randint(2,4)
    a3=a1*tmp
    c1=int(a3/a1)
    c2=int(a2/c1)
    c3=c1+c2
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,c1=c1,c2=c2,c3=c3)
    return stem,answer,comment

#2-1-3-123
def systemequations213_Stem_090():
    stem= "다음 중 일차방정식 $$수식$$ax`+`by`+`{a1}`=`0$$/수식$$      의 그래프에 대한 설명으로 옳지 않은 것은? (단, $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$  는 상수이다.)\n"\
          "① {x1}	\n② {x2}	  \n③ {x3}\n④ {x4}     \n⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "일차방정식 $$수식$$ax`+`by`+`{a1}`=`0$$/수식$$      에서 $$수식$$b`!=`0$$/수식$$    일 때,\n"\
             "$$수식$$y`=`-`{{a}}over{{b}}`x`-`{a1}over{{b}}`$$/수식$$        이다.\n\n\n"\
             "{a} {c1}\n\n"
    a1=random.randint(1,5)

    l1=["$$수식$$a`&gt;`0,~b`&gt;`0$$/수식$$","제$$수식$$2$$/수식$$, $$수식$$3$$/수식$$, $$수식$$4$$/수식$$  사분면을 지난다."]
    l2=["$$수식$$a`&gt;`0,~b`&lt;`0$$/수식$$","제$$수식$$1$$/수식$$, $$수식$$2$$/수식$$, $$수식$$3$$/수식$$  사분면을 지난다."]
    l3=["$$수식$$a`&lt;`0,~b`&gt;`0$$/수식$$","제$$수식$$1$$/수식$$, $$수식$$3$$/수식$$, $$수식$$4$$/수식$$  사분면을 지난다."]
    l4=["$$수식$$a`&lt;`0,~b`&lt;`0$$/수식$$","제$$수식$$1$$/수식$$, $$수식$$2$$/수식$$, $$수식$$4$$/수식$$  사분면을 지난다."]
    l5=["$$수식$$a`=`0,~b`!=`0$$/수식$$","$$수식$$x`$$/수식$$축에 평행한 직선이다."]
    l6=["$$수식$$a`!=`0,~b`=`0$$/수식$$","$$수식$$y`$$/수식$$축에 평행한 직선이다."]
    li1=[l1,l2,l3,l4]
    li2=[l5,l6]
    samp=random.sample([1,2],1)[0]
    l=[]
    if samp==1:
        re=random.sample(li1,2)
        re.append(li2[0])
        re.append(li2[1])
        li1.remove(re[0])
        li1.remove(re[1]) 
        wrx=li1[0][0]+"      이면 "+li1[1][1]
        for i in range(4):
            l.append(re[i][0]+"      이면 "+re[i][1])
        l.append(wrx)
        c1=li1[0][0]+"      이면 "+li1[0][1]
       
    else:
        re=li1[:]
        tmp=random.sample(li2,1)[0]
        li2.remove(tmp)
        wrx=tmp[0]+"      이면 "+li2[0][1]
        c1=tmp[0]+"     이면 "+tmp[1]
        for i in range(4):
            l.append(re[i][0]+"      이면 "+re[i][1])
        l.append(wrx)
    random.shuffle(l)
    a=answer_dict[l.index(wrx)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,c1=c1,a=a)
    return stem,answer,comment

#2-1-3-124
def systemequations213_Stem_091():
    stem= "두 점 $$수식$$({a1}a`+`{a2}`,~{a3})$$/수식$$     ,$$수식$$({a4}a`+`{a5}`,~{a6})$$/수식$$      {proa6} 지나는 직선이 $$수식$$y`$$/수식$$축에 평행할 때, $$수식$$a`$$/수식$$의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`$$/수식$$축에 평행한($$수식$$x`$$/수식$$축에 수직인) 직선이므로\n"\
             "$$수식$${a1}a`+`{a2}`=`{a4}a`+`{a5}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`=`{c1}$$/수식$$\n"\
             "(힌트)$$수식$$y`$$/수식$$축에 평행하면 두 점의 $$수식$$x`$$/수식$$좌표가 같다.\n\n"
    a3=random.randint(2,4)
    a6=random.randint(5,7)
    a4=random.randint(4,6)
    a1=random.randint(2,3)
    a2=(a4-a1)*random.randint(5,7)
    a5=(a4-a1)*random.randint(2,4)
    proa6=proc_jo(a6,3)
    c1=int((a2-a5)/(a4-a1))
    l=made_answer_cand_1(c1)
    random.shuffle(l)
    a=answer_dict[l.index(c1)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa6=proa6)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a5=a5,a4=a4,c1=c1)
    return stem,answer,comment


#2-1-3-125
def systemequations213_Stem_092():
    stem= "일차방정식 $$수식$$ax`-`by`+`{a1}`=`0`$$/수식$$      의 그래프가 $$수식$$y`$$/수식$$축에 수직이고, 제$$수식$${a2}`$$/수식$$사분면과 제$$수식$${a3}`$$/수식$$사분면을 지나기 위한 조건은?\n"\
          "① {x1}	\n② {x2}	  \n③ {x3}\n④ {x4}     \n⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$ax`-`by`+`{a1}`=`0`$$/수식$$      의 그래프가 $$수식$$y`$$/수식$$축에 수직이므로\n"\
             "$$수식$$a`=`0,~~THEREFORE~y`=`{a1}over{{b}}$$/수식$$\n\n\n"\
             "이 그래프가 제$$수식$${a2}`$$/수식$$사분면과 제$$수식$${a3}`$$/수식$$사분면을 지나려면\n"\
             "{c1}\n\n"
    a1=random.randint(1,10)
    bp=[1,2]
    bm=[3,4]
    cord=[bp,bm]
    tmp=random.sample(cord,1)[0]
    re=tmp
    a2=re[0]
    a3=re[1]
    x1="$$수식$$a`&gt;`0`,~b`=`0`$$/수식$$"
    x2="$$수식$$a`&lt;`0`,~b`=`0$$/수식$$"
    x3="$$수식$$a`&lt;`0`,~b`&gt;`0`$$/수식$$"

    if tmp==bp:
        c1="$$수식$${a1}over{{b}}`&gt;`0`~~THEREFOREb`&gt;`0$$/수식$$".format(a1=a1)
        xa="$$수식$$a`=`0`,~b`&gt;`0$$/수식$$"
        x4="$$수식$$a`=`0`,~b`&lt;`0$$/수식$$"
    else:
        c1="$$수식$${a1}over{{b}}`&lt;`0`~~THEREFOREb`&lt;`0$$/수식$$".format(a1=a1)
        xa="$$수식$$a`=`0`,~b`&lt;`0$$/수식$$"
        x4="$$수식$$a`=`0`,~b`&gt;`0$$/수식$$"
    l=[x1,x2,x3,x4,xa]
    random.shuffle(l)
    a=answer_dict[l.index(xa)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,c1=c1)
    return stem,answer,comment

#2-1-3-126
def systemequations213_Stem_093():
    stem= "선희와 경훈이가 기울기와 $$수식$$y`$$/수식$$절편이 주어진 직선의 방정식을 구하는데 선희는 기울기를 잘못 보아 $$수식$${a1}x`{a2}y`+{a3}`=`0$$/수식$$     으로 구했고, 경훈이는 $$수식$$y`$$/수식$$절편을 잘못 보아 $$수식$${a4}x`{a5}y`+`{a6}`=`0`$$/수식$$     으로 구했다. 처음 직선의 방정식은?\n"\
          "① {x1}	\n② {x2}	  \n③ {x3}\n④ {x4}     \n⑤ {x5}\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${a1}x`{a2}y`+{a3}`=`0$$/수식$$       에서 $$수식$$y`=`{c1}x`+`{c2}`$$/수식$$\n"\
             "선희는 $$수식$$y`$$/수식$$  절편을 제대로 보았으므로 처음 직선의\n"\
             "$$수식$$y`$$/수식$$  절편은 $$수식$${c2}$$/수식$$  이다.\n"\
             "$$수식$${a4}x`{a5}y`+`{a6}`=`0`$$/수식$$      에서 $$수식$$y`=`{c3}x`+`{c4}$$/수식$$\n"\
             "경훈이는 기울기를 제대로 보았으므로 처음\n"\
             "직선의 기울기는 $$수식$${c3}$$/수식$$  이다.\n"\
             "따라서 구하는 직선의 방정식은\n"\
             "$$수식$$y`=`{c3}x`+`{c2}`$$/수식$$\n\n"
    a2=random.randint(-6,-4)
    a1=abs(a2)*random.randint(2,3)
    a3=abs(a2)*random.randint(5,8)
    c1=int(-a1/a2)
    c2=int(-a3/a2)
    a5=random.randint(-3,-2)
    a4=abs(a5)*random.randint(2,4)
    a6=abs(a5)*random.randint(3,4)
    c3=int(-a4/a5)
    c4=int(-a6/a5)
    while c1==c3 or c2==c4:
        a2=random.randint(-6,-4)
        a1=abs(a2)*random.randint(2,3)
        a3=abs(a2)*random.randint(5,8)
        c1=int(-a1/a2)
        c2=int(-a3/a2)
        a5=random.randint(-3,-2)
        a4=abs(a5)*random.randint(2,4)
        a6=abs(a5)*random.randint(3,4)
        c3=int(-a4/a5)
        c4=int(-a6/a5)
    x1="$$수식$$y`=`{c1}x`+`{c2}`$$/수식$$".format(c1=c1,c2=c2)
    x2="$$수식$$y`=`{c1}x`+`{c4}`$$/수식$$".format(c1=c1,c4=c4)
    xa="$$수식$$y`=`{c3}x`+`{c2}`$$/수식$$".format(c3=c3,c2=c2)
    x3="$$수식$$y`=`{c3}x`+`{c4}`$$/수식$$".format(c3=c3,c4=c4)
    x4="$$수식$$y`=`{wc3}x`+`{c2}`$$/수식$$".format(wc3=-c3,c2=c2)
    l=[x1,x2,x3,x4,xa]
    random.shuffle(l)
    a=answer_dict[l.index(xa)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,c1=c1,c2=c2,c3=c3,c4=c4)
    return stem,answer,comment

#2-1-3-127
def systemequations213_Stem_094():
    stem= "직선 $$수식$$y`=`{a1}$$/수식$$    {proa1} 두 직선 $$수식$$y`=`{a2}x`+`{a3}`$$/수식$$   , $$수식$$y`=`{a4}x`+`{a5}$$/수식$$    {proa5} 만나는 점을 각각 A, B라 할 때, 선분 AB의 길이는?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$y`=`{a1}$$/수식$$    {proa1_2} $$수식$$y`=`{a2}x`+`{a3}`$$/수식$$    에 대입 하면\n"\
             "$$수식$${a1}`=`{a2}x`+`{a3}`,~x`=`{c1}$$/수식$$\n"\
             "$$수식$$THEREFORE~A({c1},~{a1})$$/수식$$\n"\
             "$$수식$$y`=`{a1}$$/수식$$    {proa1_2}  $$수식$$y`=`{a4}x`+`{a5}$$/수식$$    에 대입 하면\n"\
             "$$수식$${a1}`=`{a4}x`+`{a5}`,~x`=`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~B({c2},~{a1})$$/수식$$\n"\
             "점 A, B의 $$수식$$y`$$/수식$$  좌표가 같으므로\n"\
             "$$수식$$rm bar{{AB}}`=`$$/수식$$(두 점의 $$수식$$x`$$/수식$$  좌표의 차)\n"\
             "$$수식$$`=`LEFT | {c1}`-`{c2} RIGHT |`=`{c3}$$/수식$$\n\n"
    a2=random.randint(4,6)
    a4=random.randint(2,4)
    a1=a2*a4
    a3=random.randint(2,4)*a2
    a5=random.randint(2,4)*a4
    proa1=proc_jo(a1,0)
    proa1_2=proc_jo(a1,3)
    proa5=proc_jo(a5,2)
    c1=int((a1-a3)/a2)
    c2=int((a1-a5)/a4)
    while c1==c2:
        a2=random.randint(4,6)
        a4=random.randint(2,4)
        a1=a2*a4
        a3=random.randint(2,4)*a2
        a5=random.randint(2,4)*a4
        c1=int((a1-a3)/a2)
        c2=int((a1-a5)/a4)
    c3=abs(c1-c2)
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa1=proa1,proa5=proa5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,c3=c3,proa1_2=proa1_2)
    return stem,answer,comment

#2-1-3-128
def systemequations213_Stem_095():
    stem= "점 $$수식$$(3, 5)`$$/수식$$  를 지나는 직선의 방정식에 대한 다음 보기의 설명 중 옳은 것을 모두 고른 것은?\n"\
          "$$표$$\n보기\n"\
          "(ㄱ){a1}\n"\
          "(ㄴ){a2}\n"\
          "(ㄷ){a3}\n$$/표$$\n"\
          "① (ㄱ)	  ② (ㄴ)	  ③ (ㄷ)\n④ (ㄴ), (ㄷ)     ⑤ (ㄱ), (ㄴ), (ㄷ)\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "(ㄱ){c1}\n"\
             "(ㄴ){c2}\n"\
             "(ㄷ){c3}\n\n"
    x_ver=["$$수식$$x`$$/수식$$축에 수직이면 직선의 방정식은"," $$수식$$x`=`3$$/수식$$  이다.","점$$수식$$(3,~5)$$/수식$$   를 지나는 직선이$$수식$$x`$$/수식$$축에 수직 이므로 $$수식$$y`$$/수식$$축에 평행하다.\n 따라서$$수식$$x`=`3$$/수식$$    이다."]
    x_hori=["$$수식$$x``$$/수식$$축에 평행하면 직선의 방정식은"," $$수식$$y`=`5$$/수식$$  이다.","점$$수식$$(3,~5)$$/수식$$   를 지나는 직선이$$수식$$x`$$/수식$$축에 평행 하므로 $$수식$$y`$$/수식$$축에 수직이다.\n따라서 $$수식$$y`=`5$$/수식$$   이다."]
    y_ver=["$$수식$$y`$$/수식$$축에 수직이면 직선의 방정식은"," $$수식$$y`=`5$$/수식$$  이다.","점$$수식$$(3,~5)$$/수식$$   를 지나는 직선이$$수식$$y`$$/수식$$축에 수직 이므로 $$수식$$x`$$/수식$$축에 평행하다.\n따라서 $$수식$$y`=`5$$/수식$$    이다."]
    y_hori=["$$수식$$y`$$/수식$$축에 평행하면 직선의 방정식은"," $$수식$$x`=`3$$/수식$$  이다.","점$$수식$$(3,~5)$$/수식$$   를 지나는 직선이$$수식$$y`$$/수식$$축에 평행 하므로 $$수식$$x`$$/수식$$축에 수직이다.\n따라서 $$수식$$x`=`3$$/수식$$    이다."]
    aa1=random.randint(4,6)
    aa2=(aa1-3)*random.randint(3,5)+5
    tan=int((aa2-5)/(aa1-3))
    proaa2=proc_jo(aa2,3)
    thr_string="점$$수식$$({aa1},`~{aa2})$$/수식$$    {proaa2} 지나면 직선의 방정식은".format(aa1=aa1,aa2=aa2,proaa2=proaa2)
    thr_string_re=" $$수식$$y`=`{tan}(x`-`{aa1})`+`{aa2}`$$/수식$$      이다.".format(tan=tan,aa1=aa1,aa2=aa2)
    come_thr="두 점$$수식$$(3, 5)`,~({aa1},`~{aa2})$$/수식$$          {proaa2} 지나는 직선의 기울기는\n$$수식$${{{aa1}`-`3}}over{{{aa2}`-`5}}`=`{tan}$$/수식$$\n\n 따라서 직선의 방정식은$$수식$$y`=`{tan}`(x`-`{aa1})`+`{aa2}`$$/수식$$".format(aa1=aa1,aa2=aa2,tan=tan,proaa2=proaa2)
    thr_l=[thr_string,thr_string_re,come_thr]
    cand_l=[x_ver,x_hori,y_hori,y_ver,thr_l]
    l=random.sample(cand_l,3)
    a1=l[0][0]+l[0][1]
    a2=l[1][0]+l[1][1]
    a3=l[2][0]+l[2][1]
    a=answer_dict[4]
    
    c1=l[0][2]
    c2=l[1][2]
    c3=l[2][2]
    stem=stem.format(a1=a1,a2=a2,a3=a3,c1=c1,c2=c2,c3=c3)
    answer=answer.format(a=a)
    comment=comment.format(c1=c1,c2=c2,c3=c3)
    return stem, answer, comment

#2-1-3-129
def systemequations213_Stem_096():
    stem= "점 $$수식$$({a1},~{a2})$$/수식$$    {proa2} 지나면서 직선 $$수식$$y`=`{a3}`x`+`{a4}0$$/수식$$      에 수직인 직선의 방정식이 \n\n\n$$수식$$ax`-`by`+`{a5}`=`0$$/수식$$      일 때, 두 상수 $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$ 에 대하여 $$수식$$a`+`b$$/수식$$    의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	    ② $$수식$${x2}$$/수식$$	    ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$        ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$$ax`-`by`+`{a5}`=`0$$/수식$$      에서 $$수식$$y`=`{{a}}over{{b}}`x`+`{a5}over{{b}}$$/수식$$  이므로 기울기는 $$수식$${{a}}over{{b}}$$/수식$$    이다.\n\n\n"\
             "$$수식$$x`,`y`$$/수식$$     축에 수직인 두 직선의 기울기의 곱은 $$수식$$`-1`$$/수식$$    이므로\n"\
             "$$수식$${a3}`TIMES({{a}}over{{b}})`=`-1`,~THEREFORE~{{a}}over{{b}}`=`{c1}`$$/수식$$\n\n\n"\
             "한편 점 $$수식$$({a1},~{a2})$$/수식$$    를 지나므로  $$수식$${a2}`=`{c1}TIMES{a1}`+`{a5}over{{b}}$$/수식$$\n\n\n"\
             "$$수식$$THEREFORE~b`=`{c2}$$/수식$$\n"\
             "$$수식$$b`=`{c2}$$/수식$$  이므로 $$수식$$a`=`{c3}`$$/수식$$\n"\
             "$$수식$$THEREFORE~a`+`b`=`{c4}$$/수식$$\n\n"\
    
    a1=random.randint(3,5)
    a2=random.randint(2,5)
    tmp=random.randint(3,5)
    a4=random.randint(2,6)
    t2=Fraction(1,tmp)
    a3=made_fraction_string(t2)
    proa2=proc_jo(a2,3)
    c1=-tmp
    a5=(a2+tmp*a1)*random.randint(3,5)
    c2=int(a5/(a2+tmp*a1))
    c3=c1*c2
    c4=c3+c2
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proa2=proa2)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,c3=c3,c4=c4)
    return stem,answer,comment

#2-1-3-130
def systemequations213_Stem_097():
    stem= "다음 네 방정식의 그래프로 둘러싸인 도형의 넓이가 $$수식$${a1}`$$/수식$$일 때, 양수 $$수식$$p`$$/수식$$  의 값은?\n"\
          "$$표$$$$수식$$ x`=`p`$$/수식$$    , $$수식$$x`=`{a2}p`$$/수식$$    , $$수식$$y`=`{a3}$$/수식$$   ,  $$수식$$y`=`{a4}`$$/수식$$  $$/표$$\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "그래프로 둘러싸인 도형의 넓이를 구하면\n"\
             "$$수식$$LEFT | {a2}p`-`p` RIGHT |`TIMES`LEFT |{a3}`-`{a4} RIGHT |`=`{a1}$$/수식$$\n"\
             "$$수식$$THEREFORE~p`=`{c1}`$$/수식$$\n\n"
    a2=random.randint(3,5)
    a4=random.randint(5,7)
    a3=random.randint(3,6)
    while a4==a3:
        a4=random.randint(5,7)
        a3=random.randint(3,6)
    a1=random.randint(3,5)*(a2-1)*abs(a4-a3)
    c1=int(a1/((a2-1)*abs(a4-a3)))
    l=made_answer_cand_1(c1)
    random.shuffle(l)
    a=answer_dict[l.index(c1)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1)
    return stem,answer,comment

#2-1-3-134
def systemequations213_Stem_098():
    stem= "점 $$수식$$({a1},~{a2})`$$/수식$$    을 지나면서 $$수식$$x`$$/수식$$축에 평행한 직선과 점 $$수식$$({a3},~{a4})$$/수식$$    를 지나면서 $$수식$$y`$$/수식$$축에 평행한 직선의 교점의 좌표를 $$수식$$(p,~q)$$/수식$$     라 할 때, $$수식$$p`+`q$$/수식$$   의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "점 $$수식$$({a1},~{a2})`$$/수식$$    을 지나면서 $$수식$$x`$$/수식$$축에 평행한 직선의 방정식은 $$수식$$y`=`{a2}$$/수식$$\n"\
             "점 $$수식$$({a3},~{a4})$$/수식$$     를 지나면서 $$수식$$y`$$/수식$$축에 평행한 직선의 방정식은 $$수식$$x`=`{a3}$$/수식$$\n"\
             "따라서 두 직선의 교점의 좌표는 $$수식$$({a3},~{a2})`$$/수식$$    이므로\n"\
             "$$수식$$p`=`{a3}`,~q`=`{a2}$$/수식$$\n"\
             "$$수식$$THEREFORE~p`+`q`=`{a3}`+`{a2}`=`{c1}$$/수식$$\n\n"
    a1=random.randint(-10,10)
    a3=random.randint(-10,10)
    a2=random.sample([1,3,6,7,8,10],1)[0]
    a4=random.sample([2,4,5,9],1)[0]
    c1=a3+a2
    l=made_answer_cand_1(c1)
    random.shuffle(l)
    a=answer_dict[l.index(c1)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1)
    return stem,answer,comment
             
#2-1-3-135
def systemequations213_Stem_099():
    stem= "두 직선 $$수식$$y`=`{a1}x`{a2}$$/수식$$    , $$수식$$y`=`kx`+`{a3}$$/수식$$    의 교점이 제$$수식$$1`$$/수식$$사분면에 있을 때 상수 $$수식$$k`$$/수식$$ 의 값의 범위는?\n"\
          "① $$수식$${x1}$$/수식$$	     ② $$수식$${x2}$$/수식$$	   ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$      ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "두 직선 $$수식$$y`=`{a1}x`{a2}$$/수식$$    , $$수식$$y`=`kx`+`{a3}$$/수식$$      의 교점을 구하면\n"\
             "$$수식$${a1}x`{a2}`=`kx`+`{a3}$$/수식$$      에서\n"\
             "$$수식$$x`=`{c1}over{{{a1}`-`k}}$$/수식$$\n\n"\
             "$$수식$$x`=`{c1}over{{{a1}`-`k}}$$/수식$$    이므로\n\n"\
             "$$수식$$y`=`{a1}`TIMES`{c1}over{{{a1}`-`k}}`{a2}$$/수식$$\n\n"\
             "두 직선의 교점이 제$$수식$$1`$$/수식$$사분면에 있으려면 $$수식$$x`,`y$$/수식$$  좌표 모두 양수이어야 한다.\n"\
             "$$수식$${a1}`-`k``&gt;`0`$$/수식$$    , $$수식$${a1}`TIMES`{c1}over{{{a1}`-`k}}`{a2}`&gt;`0$$/수식$$\n\n\n"\
             "$$수식$${a1}`&gt;`k`$$/수식$$    , $$수식$$k`&gt;`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~{c2}`&lt;`k`&lt;`{a1}$$/수식$$\n\n"
    a2=random.randint(-4,-2)
    a1=random.randint(3,5)*abs(a2)
    a3=random.randint(2,4)
    c1=a3-a2
    c2=int((a1*c1+a1*a2)/a2)
    x1="k`&lt;`{a1}".format(a1=a1)
    x2="{c2}`&gt;`k".format(c2=c2)
    xa="{c2}`&lt;`k`&lt;`{a1}".format(a1=a1,c2=c2)
    x3="k`&gt;`{wa1}".format(wa1=-a1*2)
    x4="k`&lt;`{wc2}".format(wc2=-c2*2)
    l=[x1,x2,x3,x4,xa]
    random.shuffle(l)
    a=answer_dict[l.index(xa)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,c1=c1,c2=c2)
    return stem,answer,comment

#2-1-3-136
def systemequations213_Stem_100():
    stem= "두 직선  $$수식$$ax`-`y`+`{a1}a`=`0$$/수식$$    , $$수식$${a2}x`-`{a3}y`+`{a4}b`=`0$$/수식$$      의 교점이 $$수식$$2`$$/수식$$개 이상일 때, 상수 $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$ 에 대하여 $$수식$${a5}ab`$$/수식$$  의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "두 직선의 교점이 $$수식$$2`$$/수식$$개 이상이므로 두 직선은 일치한다.\n"\
             "$$수식$$ax`-`y`+`{a1}`a`=`0$$/수식$$     에서 $$수식$$y`=`ax`+`{a1}`a$$/수식$$      이고,\n"\
             "$$수식$${a2}x`-`{a3}y`+`{a4}b`=`0$$/수식$$      에서  $$수식$$y`=`{c1}x`+`{c2}b$$/수식$$      이므로\n"\
             "$$수식$$a`=`{c1}$$/수식$$  ,  $$수식$${a1}a`=`{c2}b$$/수식$$\n"\
             "$$수식$$THEREFORE~a`=`{c1}`,~b`=`{c3}$$/수식$$\n"\
             "$$수식$$THEREFORE~{a5}ab`=`{a5}TIMES{c1}TIMES{c3}`=`{c4}$$/수식$$"
    a3=random.randint(3,5)
    a2=random.randint(2,4)*a3
    a4=random.randint(5,6)*a3
    a1=a4*random.randint(2,3)
    a5=random.randint(3,5)
    c1=int(a2/a3)
    c2=int(a4/a3)
    c3=int(c1*a1/c2)
    c4=a5*c1*c3
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,c3=c3,c4=c4)
    return stem,answer,comment

#2-1-3-137
def systemequations213_Stem_101():
    stem= "두 직선 $$수식$$y`=`{a1}x`+`{a2}$$/수식$$    , $$수식$$y`=`{a3}x`+`a`$$/수식$$    의 교점이 제$$수식$$2`$$/수식$$사분면에 있을 때 상수 $$수식$$a`$$/수식$$  의 값의 범위는?\n"\
          "① $$수식$${x1}$$/수식$$	     ② $$수식$${x2}$$/수식$$	    ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$        ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "두 직선 $$수식$$y`=`{a1}x`+`{a2}$$/수식$$    , $$수식$$y`=`{a3}x`+`a$$/수식$$      의 교점을 구하면\n"\
             "$$수식$${a1}x`+`{a2}`=`{a3}x`+`a$$/수식$$      에서\n"\
             "$$수식$$x`=`{{{a2}`-`a}}over{{{a3}`-`{a1}}}`=`{{{a2}`-`a}}over{c1}$$/수식$$      이므로\n\n"\
             "$$수식$$y`=`{a1}`TIMES`{{{a2}`-`a}}over{c1}`+`{a2}`=`{{{a2}`-`a}}`+`{a2}`=`{c2}`-`a`$$/수식$$    \n\n"\
             "두 직선의 교점이 제$$수식$$2`$$/수식$$사분면에 있으려면 $$수식$$x`$$/수식$$좌표는 음수 $$수식$$y`$$/수식$$좌표는 양수이어야 한다.\n"\
             "$$수식$${{{a2}`-`a}}over{c1}`&lt;`0`$$/수식$$            ,  $$수식$${c2}`-`a`&gt;`0$$/수식$$\n\n"\
             "$$수식$${a2}`&lt;`a`$$/수식$$    , $$수식$$a`&lt;`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~{a2}`&lt;`a`&lt;`{c2}$$/수식$$\n\n"
    a1=random.randint(2,6)
    a2=random.randint(3,6)
    a3=2*a1
    c1=a3-a1
    c2=2*a2
    x1="a`&gt;`{a2}".format(a2=a2)
    x2="{c2}`&gt;`a".format(c2=c2)
    xa="{a2}`&lt;`a`&lt;`{c2}".format(a2=a2,c2=c2)
    x3="a`&gt;`{wa2}".format(wa2=a2*2)
    x4="a`&lt;`{wc2}".format(wc2=c2*2)
    l=[x1,x2,x3,x4,xa]
    random.shuffle(l)
    a=answer_dict[l.index(xa)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,c1=c1,c2=c2)
    return stem,answer,comment

#2-1-3-138
def systemequations213_Stem_102():
    stem= "연립방정식 $$수식$$cases{{``ay`=`{a1}x`+`{a2}#``{a3}y`-`{a4}x`=`b}}$$/수식$$의 해가 무수히 많을 때, \n\n두 직선  $$수식$$y`=`ax`+`b`$$/수식$$   ,$$수식$$bx`-`ky`=`{a5}$$/수식$$   가 서로 평행하다고 한다. 이때 양수 $$수식$$k`$$/수식$$의 값은? (단, $$수식$$a`$$/수식$$ , $$수식$$b`$$/수식$$는 상수이다.)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "연립방정식 $$수식$$cases{{``ay`-`{a1}x`-`{a2}`=`0#``{a3}y`-`{a4}x`-`b`=`0}}$$/수식$$의 해가 무수히 많으므로\n\n"\
             "$$수식$${{a}}over{a3}`=`{a1}over{a4}`=`{a2}over{{b}}~~THEREFORE~a`=`{c1}`,~b`=`{c2}$$/수식$$\n\n"\
             "한편, 직선 $$수식$$bx`-`ky`=`{a5}$$/수식$$      의 기울기는 $$수식$${{b}}over{{k}}`=`{c2}over{{k}}$$/수식$$          이고\n\n"\
             "이 직선은 직선 $$수식$$y`=`{c1}x`+`{c2}$$/수식$$    와 평행하므로\n"\
             "$$수식$${c2}over{{k}}`=`{c1}$$/수식$$\n\n"\
             "$$수식$$THEREFORE~k`=`{c2}over{c1}`=`{c3}$$/수식$$\n\n"
    tmp=random.randint(2,4)
    a1=random.randint(2,3)
    a2=tmp*a1*a1*random.randint(2,3)
    a4=random.randint(2,4)
    a3=tmp*a4*a4
    a5=random.randint(2,10)
    c1=int(a3*(a1/a4))
    c2=int((a4*a2)/a1)
    c3=int(c2/c1)
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2,c3=c3)
    return stem,answer,comment

#2-1-3-139
def systemequations213_Stem_103():
    stem= "다음 조건을 모두 만족시키는 세 수 $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$, $$수식$$c`$$/수식$$에 대하여 $$수식$$a`+`b`+`c$$/수식$$   의 값은?\n"\
          "$$표$$\n"\
          "(가)두 직선 $$수식$$y`=`{a1}x`+`{a2}$$/수식$$      ,$$수식$$y`=`ax`+`b$$/수식$$   의 교점의 좌표가$$수식$$({a3},~c)$$/수식$$    이다.\n"\
          "(나)직선 $$수식$$y`=`ax`-`b$$/수식$$     의 $$수식$$y`$$/수식$$절편은 $$수식$${a4}`$$/수식$$  이다.\n"\
          "$$표/$$\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "조건 (가)에서 두 직선의 교점의 좌표가 $$수식$$({a3},~c)$$/수식$$    이므로\n"\
             "$$수식$$c`=`{a1}TIMES{a3}`+`{a2}`=`{c1}$$/수식$$    이고\n"\
             "$$수식$${c1}`=`{a3}a`+`b$$/수식$$\n"\
             "조건 (나)에서 $$수식$$y`=`ax`-`b$$/수식$$      의 $$수식$$y`$$/수식$$  절편이 $$수식$${a4}$$/수식$$ 이므로\n"\
             "$$수식$$b`=`{c2}$$/수식$$\n"\
             "$$수식$$THEREFORE~a={c3}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`+`b`+`c`=`{c3}`+`{c2}`+`{c1}`=`{c4}$$/수식$$\n\n"
    a3=random.randint(3,5)
    a1=random.randint(2,5)
    a2=random.randint(2,4)*a3
    a4=random.randint(-7,-5)*a3
    c1=a1*a3+a2
    c2=-a4
    while c1==c2:
        a3=random.randint(3,5)
        a1=random.randint(2,5)
        a2=random.randint(2,4)*a3
        a4=random.randint(-7,-5)*a3
        c1=a1*a3+a2
        c2=-a4
    c3=int((c1-c2)/a3)
    c4=c1+c2+c3
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3,c4=c4)
    return stem,answer,comment

#2-1-3-140
def systemequations213_Stem_104():
    stem= "연립방정식 $$수식$$cases{{``{a1}x`+`{a2}y`=`{a3}#``ax`+`{a4}y`=`b`$$/수식$$    의 해가 무수히 많을 때, 일차함수 \n\n$$수식$$y`=`ax`+`b`$$/수식$$      의 그래프가 $$수식$$x`$$/수식$$축과 만나는 점의 좌표는? (단, $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$는 상수)\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "$$수식$${{a}}over{a1}`=`{a4}over{a2}`=`{{b}}over{a3}`,~~THEREFORE~a`=`{c1}`,`b`=`{c2}$$/수식$$\n\n"\
             "따라서 $$수식$$y`=`{c1}x`+`{c2}$$/수식$$      의 $$수식$$x`$$/수식$$  절편을 구하면\n"\
             "$$수식$$0`=`{c1}x`+`{c2}$$/수식$$    에서\n"\
             "$$수식$$THEREFORE~x`=`{c3}$$/수식$$\n\n"
    a2=random.randint(2,6)
    a1=random.randint(3,7)
    a4=random.randint(3,5)*a2
    a3=random.randint(3,6)*a1
    c1=int(a1*a4/a2)
    c2=int(a3*a4/a2)
    c3=int(-c2/c1)
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,c1=c1,c2=c2,c3=c3)
    return stem,answer,comment

#2-1-3-142
def systemequations213_Stem_105():
    stem= "두 일차함수 $$수식$$y`=`{a1}x`+`{a2}$$/수식$$    , $$수식$$y`=`{a3}x`+`{a4}$$/수식$$      의 그래프의 교점과 점 $$수식$$({a5}`,~{a6})$$/수식$$    {proc1} 지나는 직선을 그래프로 하는 일차함수의 식이 $$수식$$y`=`ax`+`b$$/수식$$      일 때, 상수 $$수식$$a`,~b`$$/수식$$     에 대하여 $$수식$$a`+`b`$$/수식$$  의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "연립방정식 $$수식$$cases{{``y`=`{a1}x`+`{a2}#``y`=`{a3}x`+`{a4}$$/수식$$    의 해는$$수식$$x`=`{c1}`,~y`=`{c2}$$/수식$$\n\n"\
             "따라서 두 점$$수식$$({a5}`,~{a6})`,~({c1}`,~{c2})`$$/수식$$           {proc2}지나는 직선의 기울기는\n"\
             "$$수식$${{{c2}`-`{a6}}}over{{{c1}`-`{a5}}}`=`{c3}$$/수식$$\n\n"\
             "따라서 직선의 방정식은 $$수식$$y`=`{c3}(x`-`{a5})`+`{a6}$$/수식$$        에서\n"\
             "$$수식$$a`=`{c3}`,~b`=`{c4}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`+`b`=`{c5}$$/수식$$\n\n"
    a1=random.randint(2,6)
    a3=a1+1
    a2=random.randint(7,15)
    a4=random.randint(2,4)
    a5=random.randint(3,8)
    while a5>a2-a4:
        a5=random.randint(3,8)
    a6=random.randint(3,10)
    while a6>a2*a3-a1*a4:
        a6=random.randint(3,10)
    c1=int((a2-a4)/a3-a1)
    c2=int((a2*a3-a1*a4)/(a3-a1))
    c3=int((c2-a6)/(c1-a5))
    c4=a6-c3*a5
    c5=c3+c4
    proc1=proc_jo(a6,3)
    proc2=proc_jo(c2,3)
    l=made_answer_cand_1(c5)
    random.shuffle(l)
    a=answer_dict[l.index(c5)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,proc1=proc1)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,proc2=proc2)
    return stem,answer,comment

#2-1-3-143
def systemequations213_Stem_106():
    stem= "세 직선   $$수식$$x`+`{a1}y`=`{a2}`,~{a3}x`+`{a4}y`=`a`,~{a5}x`+`{a6}y`=`{a7}$$/수식$$               에 의하여 삼각형이 만들어지지 않을 때, 상수 $$수식$$a`$$/수식$$  의 값은?\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "세 직선   $$수식$$x`+`{a1}y`=`{a2}`,~{a3}x`+`{a4}y`=`a`,~{a5}x`+`{a6}y`=`{a7}$$/수식$$               중 어느 두 직선도\n"\
             "평행하지 않으므로 세 직선에 의하여 삼각형이 만들어지지 않는 경우는 세 직선이 한 점에서 만날 때이다.\n"\
             "연립방정식 $$수식$$cases{{``x`+`{a1}y`=`{a2}#``{a5}x`+`{a6}y`=`{a7}$$/수식$${proa7} 풀면 $$수식$$x`=`{c1}`,~y`=`{c2}$$/수식$$\n\n"\
             "따라서 $$수식$${a3}x`+`{a4}y`=`a`$$/수식$$      가 $$수식$$({c1}`,~{c2}`)$$/수식$$      {proc2} 지나므로\n"\
             "$$수식$${a3}TIMES({c1})`+`{a4}TIMES{c2}`=`a$$/수식$$\n"\
             "$$수식$$THEREFORE~a`=`{c3}$$/수식$$\n\n"
    a1=random.randint(2,4)
    a2=random.randint(5,7)
    a3=random.randint(2,3)
    a4=random.randint(2,4)
    a5=random.randint(3,5)
    a6=a1*a5-1
    a7=random.randint(4,7)
    while 1/a1==a3/a4 or 1/a1==a5/a6 or a3/a4==a5/a6:
        a1=random.randint(2,4)
        a2=random.randint(5,7)
        a3=random.randint(2,3)
        a4=random.randint(2,4)
        a5=random.randint(3,5)
        a6=a1*a5-1
        a7=random.randint(4,7)
    while a6<a7:
        a7=random.randint(4,7)
    proa7=proc_jo(a7,3)
    c1=a1*a7-a2*a6
    c2=a2*a5-a7
    proc2=proc_jo(c2,3)
    c3=a3*c1+a4*c2
    l=made_answer_cand_1(c3)
    random.shuffle(l)
    a=answer_dict[l.index(c3)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,proa7=proa7,proc2=proc2,c1=c1,c2=c2,c3=c3)
    return stem,answer,comment

#2-1-3-144
def systemequations213_Stem_107():
    stem= "연립방정식 $$수식$$cases{{``{a1}x`+`{a2}ay`=`{a3}#``{a4}x`+`{a5}y`=`b$$/수식$$의 해가 존재하지 않도록 하는 \n\n상수 $$수식$$a`$$/수식$$  , $$수식$$b`$$/수식$$의 조건으로 옳은 것은?\n"\
          "① $$수식$${x1}$$/수식$$	  ② $$수식$${x2}$$/수식$$	    ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$       ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "연립방정식의 해가 없으므로\n"\
             "$$수식$${a1}over{a4}`=`{{{a2}a}}over{a5}`!=`{a3}over{{b}}$$/수식$$\n\n"\
             "$$수식$$THEREFORE~a`=`{c1}`,~b`!=`{c2}$$/수식$$\n\n"
    tmp=random.randint(2,5)
    a4=random.randint(2,4)
    a1=tmp*a4
    a3=random.randint(2,6)*tmp
    a2=random.randint(2,4)
    a5=random.randint(2,5)*a2
    c1=int(a1*a5/(a4*a2))
    c2=int(a4*a3/a1)
    x1="a`=`{a1}`,~b`=`{c1}".format(a1=a1,c1=c1)
    x2="a`=`{c1}`,~b`=`{c2}".format(c1=c1,c2=c2)
    xa="a`=`{c1}`,~b`!=`{c2}".format(c1=c1,c2=c2)
    x3="a`!=`{c1}`,~b`=`{c2}".format(c1=c1,c2=c2)
    x4="a`!=`{c1}`,~b`!=`{c2}".format(c1=c1,c2=c2)
    l=[x1,x2,x3,x4,xa]
    random.shuffle(l)
    a=answer_dict[l.index(xa)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2)
    return stem,answer,comment
#2-1-3-150
def systemequations213_Stem_108():
    stem= "다음 네 직선이 한 점에서 만날 때, 상수 $$수식$$a`$$/수식$$ , $$수식$$b`$$/수식$$에 대하여 $$수식$$a`+`b$$/수식$$   의 값은?\n"\
          "$$표$$\n"\
          "$$수식$${a1}x`+`ay`+`b`+`{a2}`=`0$$/수식$$      , $$수식$$x`+`{a3}y`=`{a4}$$/수식$$\n"\
          "$$수식$$ax`+`{a5}y`-`b`+`{a6}`=`0$$/수식$$      , $$수식$$x`+`{a7}y`=`{a8}$$/수식$$\n"\
          "$$/표$$\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "주어진 네 직선이 만나는 점의 좌표는\n"\
             "연립방정식 $$수식$$cases{{``x`+`{a3}y`=`{a4}#``x`+`{a7}y`=`{a8}$$/수식$$의 해와 같다.\n\n"\
             "$$수식$$THEREFORE~x`=`{c1}`,~y`=`{c2}$$/수식$$\n"\
             "따라서 두 직선 $$수식$${a1}x`+`ay`+`b`+`{a2}`=`0$$/수식$$       , $$수식$$ax`+`{a5}y`-`b`+`{a6}`=`0$$/수식$$      이\n"\
             "점 $$수식$$(`{c1}`,~{c2}`)$$/수식$$      {proc2} 지나므로\n"\
             "$$수식$${a1}TIMES({c1})`+`{{a}}TIMES{c2}`+`b`+`{a2}`=`0~~THEREFORE~{c2}a`+`b`=`{c3}`$$/수식$$\n"\
             "$$수식$${{a}}TIMES({c1})`+`{a5}TIMES{c2}`-`b`+`{a6}`=`0~~THEREFORE~{c1}a`-`b`=`{c4}$$/수식$$\n"\
             "따라서 연립방정식 $$수식$$cases{{``{c2}a`+`b`=`{c3}#``{c1}a`-`b`=`{c4}$$/수식$${proc4} 풀면\n\n"\
             "$$수식$$a`=`{c5}`,~b`=`{c6}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`+`b`=`{c7}$$/수식$$\n\n"
    a3=random.randint(4,6)
    a7=a3-1
    a8=random.randint(-5,-2)
    a6=-a8
    a4=random.randint(3,5)
    k=a4-a8
    a1=random.randint(2,6)
    a2=a1*k
    a5=a7-1
    c1=a8-a7*k
    c2=k
    proc2=proc_jo(c2,3)
    c3=-a2-a1*c1
    c4=-a5*c2-a6
    proc4=proc_jo(c4,3)
    c5=1-a1
    c6=-k-a1*(a8-a7*k)
    c7=c5+c6
    l=made_answer_cand_1(c7)
    random.shuffle(l)
    a=answer_dict[l.index(c7)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,proc2=proc2,proc4=proc4)
    return stem,answer,comment

#2-1-3-151
def systemequations213_Stem_109():
    stem= "상수 $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$에 대하여 일차방정식 $$수식$$ax`-`y`-`b`=`0$$/수식$$      의 그래프가 일차방정식 $$수식$${a1}x`+`{a2}y`=`{a3}$$/수식$$       의 그래프와 평행하고, 일차방정식 $$수식$${a4}x`+`{a5}y`=`{a6}`$$/수식$$      의 그래프와 $$수식$$y`$$/수식$$축 위에서 만난다. 이때 $$수식$$a`+`b$$/수식$$  의 값은? (단,$$수식$$a`!=`0$$/수식$$  )\n"\
          "① $$수식$${x1}$$/수식$$	② $$수식$${x2}$$/수식$$	  ③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$     ⑤ $$수식$${x5}$$/수식$$\n\n"
    answer= "(정답)\n{a}\n"
    comment= "(해설)\n"\
             "두 일차방정식 $$수식$$ax`-`y`-`b`=`0$$/수식$$      의 그래프가 일차방정식 $$수식$${a1}x`+`{a2}y`=`{a3}$$/수식$$       의 그래프와 평행하므로\n"\
             "$$수식$${{a}}over{a1}`=`{{-1}}over{a2}`!=`{{b}}over{a3}$$/수식$$                     에서"\
             "$$수식$$a`=`{c1}$$/수식$$\n\n"\
             "또한, 두 일차방정식   $$수식$${c1}x`-`y`-`b`=`0$$/수식$$      , $$수식$${a4}x`+`{a5}y`=`{a6}`$$/수식$$      의 그래프와 $$수식$$y`$$/수식$$축 위에서\n"\
             "만나므로 두 그래프의 $$수식$$y`$$/수식$$절편이 같다.\n"\
             "$$수식$${a4}x`+`{a5}y`=`{a6}$$/수식$$     의 $$수식$$y`$$/수식$$절편이 $$수식$${c2}$$/수식$$    이므로\n"\
             "$$수식$$`-`b`=`{c2}`,~THEREFORE~b`=`{c3}$$/수식$$\n"\
             "$$수식$$THEREFORE~a`+`b`=`{c4}$$/수식$$\n\n"
    a2=random.randint(3,5)
    a1=random.randint(-5,-2)*a2
    a5=random.randint(2,7)
    a6=random.randint(-5,-3)*a5
    a3=random.randint(5,10)
    a4=random.randint(5,20)
    c1=int(-a1/a2)
    c2=int(a6/a5)
    c3=-c2
    c4=c1+c3
    l=made_answer_cand_1(c4)
    random.shuffle(l)
    a=answer_dict[l.index(c4)]
    x1,x2,x3,x4,x5=l[0],l[1],l[2],l[3],l[4]
    stem=stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer=answer.format(a=a)
    comment=comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,c1=c1,c2=c2,c3=c3,c4=c4)
    return stem,answer,comment

