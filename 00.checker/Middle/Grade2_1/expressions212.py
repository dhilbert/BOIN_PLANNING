import numpy as np
import random
import math

answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
}
def problm(vv1, vv2):
    return  "{cases{" + vv1 + "`cdotscdots`" + problm1() + "#" + vv2 + "`cdotscdots`" + problm2() + "}}"
def problm1():
    return "㉠"
def problm2():
    return "㉡"
def inequality(b, c, x, list1):
    if " &lt; " in list1:
        if x + b < c * (x):
            list1 = list1 + " (참)"
        else:
            list1 = list1 + " (거짓)"
    elif " &gt; " in list1:
        if x + b > c * (x):
            list1 = list1 + " (참)"
        else:
            list1 = list1 + " (거짓)"
    elif " ≤ " in list1:
        if x + b <= c * (x):
            list1 = list1 + " (참)"
        else:
            list1 = list1 + " (거짓)"
    else:
        if x + b >= c * (x):
            list1 = list1 + " (참)"
        else:
            list1 = list1 + " (거짓)"

    return list1
def inequality_check(a, b, d):
    if " &lt; "==d:
        return a <b
    elif " &gt; " == d:
        return a >b
    elif " ≤ "==d:
        return a <=b
    else:
        return a>= b


def inequality2(a, b, c, x, list1):
    if " &lt; " in list1:
        if a*x + b < c:
            list1 = list1 + " (참)"
        else:
            list1 = list1 + " (거짓)"
    elif " &gt; " in list1:
        if a*x + b > c:
            list1 = list1 + " (참)"
        else:
            list1 = list1 + " (거짓)"
    elif " ≤ " in list1:
        if a*x + b <= c:
            list1 = list1 + " (참)"
        else:
            list1 = list1 + " (거짓)"
    else:
        if a*x + b >= c:
            list1 = list1 + " (참)"
        else:
            list1 = list1 + " (거짓)"

    return list1


answer_kodict = {
    0: "㉠",
    1: "㉡",
    2: "㉢",
    3: "㉣",
    4: "㉤"
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
    elif check == 3:
        #이(라고)
        if bool_jo(num):
            return "이"
        return ""
    elif bool_jo(num):
        # 을를
        return "을"
    return "를"

def gcd (a, b):
    if b == 0:
        return a
    else :
        if a < b:
            a, b = b, a
        return gcd(b, a % b)





def lcm(a, b):
    return a * b // gcd(a, b)



#중2-1-2-02
def expressions212_Stem_001():
    stem = "\n다음 중 문장을 부등식으로 나타낸 것으로 옳지\n" \
           "않은 것은?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
             "{ans} \n"
    comment = "(해설)\n" \
              "{ans} {sol}"

    bb =[]
    d = np.random.randint(2, 5)
    e = np.random.randint(2,10)
    k = "x에서 " +  str(d) + proc_jo(d, 4) +" 뺀 수는 x의 " + str(e) +"배보다 작다. ➩\n" \
                                                                "x - " + str(d) + " &lt; " +  str(e) +"x"
    bb.append(k)
    d = np.random.randint(2, 5)
    e = np.random.randint(2, 10)
    k = "한 개에 x원인 사과 " + str(d) + "의 값은 것은 한 통에\n" \
                                  + str(e*1000) + "원인 수박 한 통의 값보다 싸다. ➩\n" \
                                                +str(d) + "x ≥ " + str(e*1000)
    bb.append(k)
    d = np.random.randint(2, 5)
    e = np.random.randint(30, 50)
    k = "가로의 길이가 x cm, 세로의 길이가 "+ str(d) +"cm인\n" \
                                          "직사각형의 둘레의 길이는 " +str(e)+ "cm 미만이다. ➩\n" \
                                                                   "2( x + " +str(d) +") &lt;" +str(e)
    bb.append(k)
    d = np.random.randint(2, 5)
    e = np.random.randint(10, 50)
    k = str(d) +"명이 각각 x원씩 내면 총액은 " + str(e*1000) +"원 이하\n" \
                                                   "이다.➩\n" \
                                                   + str(d) +"x ≤ " + str(e*1000)
    bb.append(k)
    d = np.random.randint(2, 5)
    e = np.random.randint(10, 50)
    k = "시속 " + str(d) +"km로 x시간 동안 달린 거리는 " + str(e) +"km\n" \
                                                       "이상이다. ➩\n" \
                                                       +str(d) + "x &lt; " + str(e)
    bb.append(k)
    sol = str(d) + "x ≥ " + str(e)

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = bb[4]
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = bb[4]
        x1 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
        x5 = bb[0]
    elif rande == 3:
        ans = "③"
        x3 = bb[4]
        x1 = bb[3]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[0]
    elif rande == 4:
        ans = "④"
        x4 = bb[4]
        x1 = bb[2]
        x2 = bb[3]
        x3 = bb[1]
        x5 = bb[0]
    else:
        ans = "⑤"
        x5 = bb[4]
        x1 = bb[0]
        x2 = bb[3]
        x3 = bb[2]
        x4 = bb[1]

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(ans=ans, sol=sol)

    return stem, answer, comment


#중2-1-2-03
def expressions212_Stem_002():
    stem = "\n다음 중 [ ] 안의 수가 부등식의 해인 것은?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
             "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${list}$$/수식$$\n" \

    inequality = ["&lt;", "&gt;", "≤", "≥"]
    pluse =["+", "-"]
    bb =[]
    cc=[]
    while len(cc)<1:
        d = np.random.randint(2, 5)
        e = 1
        k = "-x " + "+ " + str(d) + "&gt;" + str(e)
        op = np.random.randint(5, 10)
        if d-op <= e:
            cc.append(k + "[ " + str(op) + " ]")
            bb.append( " -" + str(op) + "+ " + str(d) + " = " + str((-1*op)+d) + "&gt;" + str(e) + " (거짓)\n")

    while len(cc)<2:
        d = np.random.randint(2, 5)
        e = np.random.randint(20, 30)
        k = str(d) + "x -" + str(1) + "&gt;" + str(e)
        op = np.random.randint(2,5 )
        if 2*d+op-1<=e:
            cc.append(k + "[ " + str(op) + " ]")
            bb.append( str(d)  + "$$수식$$TIMES$$/수식$$" +   str(op) + " - " + str(1) + " = " + str(d*op-1) + "&gt;" + str(e) + " (거짓)\n")

    d = np.random.randint(2, 5)
    k = str(d) + " - x ≤ $$수식$$1 over "+str(d)+"$$/수식$$"
    op =0
    cc.append(k + "[ " + str(op) + " ]")
    bb.append(str(d) + " - " + str(op) + " = " + str(d) + "≤" + "$$수식$$1 over "+str(d)+"$$/수식$$ (거짓)\n")

    d = np.random.randint(2, 5)
    k = " - " + str(d) + "x ≥ - " + str(d*2)
    op = 3
    cc.append(k + "[ " + str(op) + " ]")
    bb.append(" -" + str(d) + "$$수식$$TIMES$$/수식$$" + str(op) + " = " + str((-1*d)*op) + "≥  - " + str(d*2) + " (거짓)\n")

    while len(cc)<5:
        d = np.random.randint(2, 5)
        e = np.random.randint(2, 10)
        k = "x " + "+ "+ str(d) + inequality[0] + str(e)
        op = np.random.randint(0, 10)
        if op + d < e:
            cc.append(k + "[ " + str(op) + " ]")
            bb.append(str(op) + "+ "+ str(d) + " = " + str(op+d) + inequality[0] + str(e) + " (참)\n")

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = cc[4]
        x2 = cc[0]
        x3 = cc[1]
        x4 = cc[2]
        x5 = cc[3]

    elif rande == 2:
        ans = "②"
        x2 = cc[4]
        x1 = cc[0]
        x3 = cc[1]
        x4 = cc[2]
        x5 = cc[3]
    elif rande == 3:
        ans = "③"
        x3 = cc[4]
        x1 = cc[0]
        x2 = cc[1]
        x4 = cc[2]
        x5 = cc[3]
    elif rande == 4:
        ans = "④"
        x4 = cc[4]
        x1 = cc[0]
        x2 = cc[1]
        x3 = cc[2]
        x5 = cc[3]
    else:
        ans = "⑤"
        x5 = cc[4]
        x1 = cc[0]
        x2 = cc[1]
        x3 = cc[2]
        x4 = cc[3]

    liste = ""
    if rande == 1:
        liste = "①" + bb[4] + "②" + bb[0] + "③" + bb[1] + "④" + bb[2] + "⑤" + bb[3]
    elif rande == 2:
        liste = "①" + bb[0] + "②" + bb[4] + "③" + bb[1] + "④" + bb[2] + "⑤" + bb[3]
    elif rande == 3:
        liste = "①" + bb[0] + "②" + bb[1] + "③" + bb[4] + "④" + bb[2] + "⑤" + bb[3]
    elif rande == 4:
        liste = "①" + bb[0] + "②" + bb[1] + "③" + bb[2] + "④" + bb[4] + "⑤" + bb[3]
    else:
        liste = "①" + bb[0] + "②" + bb[1] + "③" + bb[2] + "④" + bb[3] + "⑤" + bb[4]

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=liste)

    return stem, answer, comment


#중2-1-2-04
def expressions212_Stem_003():
    stem = "\n다음 보기에서 부등식인 것은 모두 몇 개인가?\n" \
           "$$표$$\n" \
           "㉠ $$수식$${eq1}$$/수식$$\n" \
           "㉡ $$수식$${eq2}$$/수식$$\n" \
           "㉢ $$수식$${eq3}$$/수식$$\n" \
           "㉣ $$수식$${eq4}$$/수식$$\n" \
           "㉤ $$수식$${eq5}$$/수식$$\n" \
           "㉥ $$수식$${eq6}$$/수식$$\n" \
           "$$/표$$\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
             "{ans} \n"
    comment = "(해설)\n" \
              "{eql} 등식   {none} 다항식\n" \
              "따라서 부등식은 것은 {answ1}의 {answ}이다."



    bb =[]
    eql = []
    answ1=[]
    none=[]
    answ=0
    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ ", " = ", " + ", " - "]

    d = np.random.randint(2, 5)
    e = np.random.randint(1, 10)
    p = inequality[np.random.randint(0,7)]
    eq1 = str(d) + "x" + p + str(e)
    if p == " = ":
        eql.append("㉠")
    elif p == " &lt; " or p == " &gt; " or p == " ≤ " or p== " ≥ ":
        answ1.append("㉠")
        answ+=1
    else:
        none.append("㉠")


    d = np.random.randint(2, 5)
    e = np.random.randint(1, 10)
    f = np.random.randint(1, 10)
    p = inequality[np.random.randint(0, 7)]
    eq2 = str(d) + "x" + p + str(e) + " + " + str(f)
    if p == " = ":
        eql.append("㉡")
    elif p == " &lt; " or p == " &gt; " or p == " ≤ " or p == " ≥ ":
        answ1.append("㉡")
        answ += 1
    else:
        none.append("㉡")


    d = np.random.randint(2, 5)
    p = inequality[np.random.randint(0, 7)]
    eq3 = "$$수식$$1 over "+ str(d) + "$$/수식$$x" + p  + "1"
    d = np.random.randint(2, 5)
    e = np.random.randint(1, 10)
    f = np.random.randint(1, 10)

    if p == " = ":
        eql.append("㉢")
    elif p == " &lt; " or p == " &gt; " or p == " ≤ " or p == " ≥ ":
        answ1.append("㉢")
        answ += 1
    else:
        none.append("㉢")
    p = inequality[np.random.randint(0, 7)]
    eq4 = "$$수식$$x over "+ str(d) + "$$/수식$$" + p  + str(f) + " - " + str(e)
    d = np.random.randint(2, 5)
    e = np.random.randint(1, 10)
    f = np.random.randint(1, 10)

    if p == " = ":
        eql.append("㉣")
    elif p == " &lt; " or p == " &gt; " or p == " ≤ " or p == " ≥ ":
        answ1.append("㉣")
        answ += 1
    else:
        none.append("㉣")



    p = inequality[np.random.randint(0, 7)]
    eq5 = str(d) +"x" + inequality[np.random.randint(0,7)] + str(e+f)
    d = np.random.randint(2, 5)
    e = np.random.randint(1, 10)
    f = np.random.randint(1, 10)
    if p == " = ":
        eql.append("㉤")
    elif p == " &lt; " or p == " &gt; " or p == " ≤ " or p == " ≥ ":
        answ1.append("㉤")
        answ += 1
    else:
        none.append("㉤")
    p = inequality[np.random.randint(0, 7)]
    eq6 = "y = " + str(d) +"x + " + str(e)
    eql.append("㉥")

    eq1_str =""
    if len(eq1)>0:
        for i in range(len(eql)-1):
            eq1_str = eq1_str + eql[i] + ", "
        eq1_str = eq1_str + eql[-1]
    none_str =""
    if len(none) >0:
        for i in range(len(none) - 1):
            none_str = none_str + none[i] + ", "
        none_str = none_str + none[-1]

    answ1_str=""
    if len(answ1)>0:
        for i in range(len(answ1) - 1):
            answ1_str = answ1_str + answ1[i] + ", "
        answ1_str = answ1_str + answ1[-1]
    bb = []
    while len(bb) < 4:
        k = answ + np.random.randint(0, 20)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq1=eq1,eq2=eq2,eq3=eq3,eq4=eq4,eq5=eq5,eq6=eq6, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eql=eq1_str, none=none_str, answ=answ, answ1=answ1_str)

    return stem, answer, comment

#중2-1-2-05
def expressions212_Stem_004():
    stem = "\n다음 중 문장을 부등식으로 나타낸 것으로 옳은\n" \
           "것을 모두 고르면? (정답 2개)\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${list}$$/수식$$" \

    bb=[]
    cc=[]
    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ ", " = ", " + ", " - "]

    d = np.random.randint(2, 10)
    e = np.random.randint(2, 10)
    k = "한 자루에 x원인 연필 " + str(d) + "자루의 가격은 " + str(e*1000) + "원을 넘는다. ➩\n" \
                                                               +  str(d) + "x ≥ " + str(e*1000)
    list0 = str(d) + "x &gt; " + str(e*1000) +"\n"
    bb.append(k)
    d = np.random.randint(2, 5)
    e = np.random.randint(2, 20)
    k = "A반 학생 " + str(d) + "명 중에서 남학생이 x명일 때,\n여학생은 " + str(e) + "명보다 많다.➩\n" \
        + str(d) + " - x &gt; " + str(e)
    bb.append(k)
    d = np.random.randint(10, 15)
    e = np.random.randint(30, 50)
    f = np.random.randint(1, 3)
    g = np.random.randint(100, 200)
    k = "한 개에 " + str(d*100) + "원인 복숭아 x개와 한 개에 " + str(e*100) + "원인 참외 " + str(f)+"개의 총 가격은 " + str(g*100) +"원 미만이다.➩\n" \
                                                                       + str(d*100) + "x + " + str(e*100) + " &lt; " + str(g*100)
    list2 = str(d*100) + "$$수식$$TIMES$$/수식$$ x + " + str(e*100) +"$$수식$$TIMES$$/수식$$" + str(f) + " &lt; " + str(g*100) +"\n" \
                                                                                                                                "∴ " + str(d*100) + "x + " + str(e*100*f) + " &lt; " + str(g*100) +"\n"
    bb.append(k)
    d = np.random.randint(2, 5)
    e = np.random.randint(10, 50)
    k = "밑변의 길이가 " + str(d) + "cm, 높이가 x cm인 삼각형\n의 넓이는 " + str(e) + "$$수식$$cm ^2$$/수식$$ 이상이다.➩\n" \
        + str(d) + "x ≥ " + str(e)

    bb.append(k)
    d = np.random.randint(2, 5)
    e = np.random.randint(2, 10)
    k = "농도가 x %인 소금물 " + str(d*100) + " g에 들어 있는 소\n금의 양은 " + str(e) + " g보다 적다. ➩\n" \
        + str(d) + "x &lt; " + str(e)
    bb.append(k)
    list4 = "$$수식$$x over 100$$/수식$$ $$수식$$TIMES$$/수식$$ " + str(d*100)+" &lt; " + str(e) + "\n∴"+ str(d)+" &lt; " + str(e) + "\n"

    rande = np.random.randint(1, 4)
    if rande == 1:
        ans = "③, ⑤"
        x1 = bb[4]
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
        liste = "① " + list4 + "② " + list0 + "④ " + list2

    elif rande == 2:
        ans = "①, ②"
        x2 = bb[1]
        x1 = bb[3]
        x3 = bb[0]
        x4 = bb[4]
        x5 = bb[2]
        liste = "③ " + list0 + "④ " + list4 + "⑤ " + list2
    elif rande == 3:
        ans = "①, ④"
        x3 = bb[2]
        x1 = bb[1]
        x2 = bb[4]
        x4 = bb[3]
        x5 = bb[0]
        liste = "② " + list4 + "③ " + list2 + "⑤ " + list0


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=liste)

    return stem, answer, comment

#중2-1-2-06
def expressions212_Stem_005():
    stem = "\nx의 값이 -2, -1 , 0, 1, 2일 때, 부등식\n" \
           "$$수식$${eq}$$/수식$$    의 해를 모두 고른 것은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "주어진 x의 값을 부등식 $$수식$${eq}$$/수식$$에 x 대\n" \
              "신 대입하면\n" \
              "x = -2일 때,\n" \
              "$$수식$${list1}$$/수식$$\n" \
              "x = -1일 때,\n" \
              "$$수식$${list2}$$/수식$$\n" \
              "x = 0일 때,\n" \
              "$$수식$${list3}$$/수식$$\n" \
              "x = 1일 때,\n" \
              "$$수식$${list4}$$/수식$$\n" \
              "x = 2일 때,\n" \
              "$$수식$${list5}$$/수식$$\n"


    b = np.random.randint(1, 5)
    c = np.random.randint(1, 5)
    tr=[]
    inequality1 = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    d = inequality1[np.random.randint(0,4)]
    eq = "x + " +str(b) + d + " - " + str(c) +"x"
    list1 = "-2 + " +str(b) + " = " + str(b-2) + d + " - " + str(c) +"$$수식$$TIMES$$/수식$$ (- 2) = " + str((-c)*(-2))
    list1 = inequality(b, -c, -2, list1)

    list2 = "-1 + " + str(b) + " = " + str(b - 1) + d + " - " + str(c) + "$$수식$$TIMES$$/수식$$ (- 1) = " + str((-c) * (-1))

    list2 = inequality(b, -c, -1, list2)

    list3 = "0 + " + str(b) + " = " + str(b) + d + " - " + str(c) + "$$수식$$TIMES$$/수식$$ 0 = " + str((-c)* (0))
    list3 = inequality(b, -c, 0, list3)
    list4 = "1 + " + str(b) + " = " + str(b+1) + d + " - " + str(c) + "$$수식$$TIMES$$/수식$$ 1 = " + str((-c)* (1))
    list4 = inequality(b, -c, 1, list4)
    list5 = "2 + " + str(b) + " = " + str(b+2) + d + " - " + str(c) + "$$수식$$TIMES$$/수식$$ 2 = " + str((-c)* (2))
    list5 = inequality(b, -c, 2, list5)
    op = [list1, list2,list3,list4,list5]
    answs =[]
    if "(참)" in list1:
        answs.append(-2)
    if "(참)" in list2:
        answs.append(-1)
    if "(참)" in list3:
        answs.append(0)
    if "(참)" in list4:
        answs.append(1)
    if "(참)" in list5:
        answs.append(2)

    answ=""
    if len(answs)>0:
        for i in range(len(answs)-1):
            answ = answ + str(answs[i]) + " , "
        answ = answ + str(answs[-1])
    bb=[]
    p=[-2,-1,0,1,2]
    while len(bb)<4:
        cc = []
        for i in range(np.random.randint(1,5)):
            r = p[np.random.randint(0,5)]
            if r not in cc:
                cc.append(r)
                cc.sort()
        if len(cc)!=len(answs):
            t=""
            for i in range(len(cc)-1):
                t = t + str(cc[i]) + " , "
            t = t + str(cc[-1])
            if t not in bb:
                bb.append(t)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, list1=list1,list2=list2,list3=list3,list4=list4,list5=list5)

    return stem, answer, comment



#중2-1-2-07
def expressions212_Stem_006():
    stem = "\nx의 값이 -1 , 0, 1, 2일 때, 부등식\n" \
           "$$수식$${eq}$$/수식$$  $$수식$$``$$/수식$${temp}$$수식$$``$$/수식$$ 참이 되게 하는 x의 값들의 합\n" \
           "은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "x = -1일 때," \
              "$$수식$${list1}$$/수식$$\n" \
              "x = 0일 때," \
              "$$수식$${list2}$$/수식$$\n" \
              "x = 1일 때," \
              "$$수식$${list3}$$/수식$$\n" \
              "x = 2일 때," \
              "$$수식$${list4}$$/수식$$\n" \
              "따라서 구하는 합은 $$수식$${ad_}$$/수식$$\n" \

    a = np.random.randint(2, 20)
    b = np.random.randint(1, 20)
    c = np.random.randint(1, 20)
    tr=[]
    inequality1 = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    d = inequality1[np.random.randint(0,4)]
    eq = str(a)+"x + " +str(b) + d +  str(c)

    list1 = str(a)+" $$수식$$TIMES$$/수식$$ (-1) + " + str(b) + " = " + str(b-a) + d  + str(c)
    list1 = inequality2(a, b, c, -1, list1)

    list2 = str(a)+" $$수식$$TIMES$$/수식$$ 0 + " + str(b) + " = " + str(b) + d  + str(c)
    list2 = inequality2(a, b, c, 0, list2)
    list3 =  str(a)+" $$수식$$TIMES$$/수식$$ 1 + " + str(b) + " = " + str(a+b) + d  + str(c)
    list3 = inequality2(a, b, c, 1, list3)
    list4 = str(a)+" $$수식$$TIMES$$/수식$$ 2 + " + str(b) + " = " + str((2*a)+b) + d  + str(c)
    list4 = inequality2(a, b, c, 2, list4)
    temp = proc_jo(c, 4)
    answs = []
    if "(참)" in list1:
        answs.append(-1)
    if "(참)" in list2:
        answs.append(0)
    if "(참)" in list3:
        answs.append(1)
    if "(참)" in list4:
        answs.append(2)

    answ = 0
    for x in answs:
        answ = answ + x
    ad_=""
    if len(answs) > 0:
        for i in range(len(answs)-1):
            ad_ = ad_ + str(answs[i]) + " + "
        ad_ = ad_ + str(answs[-1]) + " = " + str(answ)
    else:
        ad_ = str(0)
    cc = [ -1, 2, 0, 3, 1]
    bb=[]
    for x in cc:
        if x != answ:
            bb.append(x)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[3]
        x3 = bb[0]
        x4 = bb[2]
        x5 = bb[1]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[2]
        x2 = bb[1]
        x4 = bb[0]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[1]
        x2 = bb[0]
        x3 = bb[3]
        x5 = bb[2]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[3]
        x2 = bb[2]
        x3 = bb[1]
        x4 = bb[0]


    stem = stem.format(eq=eq, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(ad_=ad_, eq=eq, list1=list1,list2=list2,list3=list3,list4=list4)

    return stem, answer, comment


#중2-1-2-08
def expressions212_Stem_007():
    stem = "\n다음 부등식 중 방정식 $$수식$${eq}$$/수식$$ $$수식$$``$$/수식$${temp}$$수식$$``$$/수식$$ 만족시키\n" \
           "는 x의 값을 해로 갖는 것은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$    에서 $$수식$${eq2}$$/수식$$\n" \
              "∴ x = $$수식$${x}$$/수식$$\n" \
              "{ans} $$수식$${eq3}$$/수식$$"

    a = np.random.randint(1, 20)
    b = np.random.randint(1, 20)
    e = np.random.randint(1, 5)
    inequality1 = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    eq=""
    if a==1:
        eq = "- x + "  + str(b) + " = " + " -" + str(b-(a*e))
    else:
        eq = "-" + str(a) + "x + " + str(b) + " = " +  str(b-(a*e))
    eq2 = "-" + str(a) + "x = " +  "-" + str(a*e)
    x=e
    temp = proc_jo((b-a)*e, 4)
    op1=""
    a = np.random.randint(1, 20)
    b = np.random.randint(1, 20)
    g =  np.random.randint(1, 20)
    c = np.random.randint(1, 20)
    d = inequality1[np.random.randint(0, 4)]
    if b == 1:
        op1 = str(a) + " - x + " + str(g) + d + str(c)
    else:
        op1 = str(a) + " - " + str(b) + "x + "+ str(g)  + d + str(c)
    while inequality_check(a-(b*e)+g,c ,d):
        a = np.random.randint(1, 20)
        b = np.random.randint(1, 20)
        c = np.random.randint(1, 20)
        d = inequality1[np.random.randint(0, 4)]
        if b == 1:
            op1 = str(a) + " - x + " + str(g) + d + str(c)
        else:
            op1 = str(a) + " - " + str(b) + "x + " + str(g) + d + str(c)



    a = np.random.randint(1, 20)
    b = np.random.randint(1, 20)
    c = np.random.randint(1, 20)
    d = inequality1[np.random.randint(0, 4)]
    op2 = ""
    if a == 1:
        op2 = "(x + " +str(b) + ") " + d + str(c)
    else:
        op2 = str(a) + "(x + " +str(b) + ") " + d + str(c)

    while inequality_check(a*(e+b),c,d):
        a = np.random.randint(1, 20)
        b = np.random.randint(1, 20)
        c = np.random.randint(1, 20)
        d = inequality1[np.random.randint(0, 4)]
        if a == 1:
            op2 = "$$수식$$$$/수식$$(x + " + str(b) + ") " + d + str(c)
        else:
            op2 = str(a) + "(x + " +str(b) + ") " + d + str(c)

    a = np.random.randint(1, 20)
    b = np.random.randint(1, 20)
    c = np.random.randint(1, 20)
    d = inequality1[np.random.randint(0, 4)]
    op3 = ""
    if a == 1:
        op3 = "-x + " + str(b)  + d + " -" + str(c)
    else:
        op3 = "-" + str(a) + "x + " + str(b)  + d + " -" + str(c)
    while inequality_check((a*(-e)+b), -c, d):
        a = np.random.randint(1, 20)
        b = np.random.randint(1, 20)
        c = np.random.randint(1, 20)
        d = inequality1[np.random.randint(0, 4)]
        if a == 1:
            op3 = "-x + " + str(b)  + d + " -" + str(c)
        else:
            op3 = "-" + str(a) + "x + " + str(b)  + d + " -" + str(c)


    a = np.random.randint(1, 20)
    b = np.random.randint(1, 20)
    c = np.random.randint(1, 20)
    d = inequality1[np.random.randint(0, 4)]
    op4 = ""
    if a == 1:
        op4 = "-x + " + str(b)  + d + str(c)
    else:
        op4 = "-"  + str(a) + "x + " + str(b)  + d + str(c)
    while inequality_check((a * (-e) + b), c, d):
        a = np.random.randint(1, 20)
        b = np.random.randint(1, 20)
        c = np.random.randint(1, 20)
        d = inequality1[np.random.randint(0, 4)]
        if a == 1:
            op4 = "-x + " + str(b) +  d + str(c)
        else:
            op4 = "-"  +  str(a) + "x + " + str(b)  + d  + str(c)

    a = np.random.randint(1, 20)
    b = np.random.randint(1, 20)
    c = np.random.randint(1, 20)
    d = inequality1[np.random.randint(0, 4)]
    op5 = str(a/10) + "x + " + str(b) + d + str(c)
    while not inequality_check((a/10)*e + b, c, d):
        a = np.random.randint(1, 20)
        b = np.random.randint(1, 20)
        c = np.random.randint(1, 20)
        d = inequality1[np.random.randint(0, 4)]
        op5 = str(a / 10) + "x + " + str(b) + d + str(c)
    eq3 = str(a/10) + "$$수식$$TIMES$$/수식$$" + str(e)  + " + " + str(b) + " = " + str((a/10)*e + b) + d + str(c) + " (참)"
    bb =[op1, op2, op3, op4, op5]


    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = bb[4]
        x2 = bb[3]
        x3 = bb[0]
        x4 = bb[2]
        x5 = bb[1]

    elif rande == 2:
        ans = "②"
        x2 = bb[4]
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = bb[4]
        x1 = bb[2]
        x2 = bb[1]
        x4 = bb[0]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = bb[4]
        x1 = bb[1]
        x2 = bb[0]
        x3 = bb[3]
        x5 = bb[2]
    else:
        ans = "⑤"
        x5 = bb[4]
        x1 = bb[3]
        x2 = bb[2]
        x3 = bb[1]
        x4 = bb[0]

    stem = stem.format(eq=eq, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(ans=ans, x=x, eq=eq, eq2=eq2, eq3=eq3)

    return stem, answer, comment


#중2-1-2-09
def expressions212_Stem_008():
    stem = "\n다음 문장을 중 방정식으로 바르게 나타내면?\n" \
           "$$표$$\n" \
           "{name}$$수식$$``$$/수식$$는 집에서 a km 떨어진 $$수식$$``$$/수식$${location}$$수식$$``$$/수식$$에 가는데\n" \
           "처음 x km (단 x &lt; a)까지는 시속 $$수식$${speed1}$$/수식$$km로 걷\n" \
           "다가 나중에 시속 $$수식$${speed2}$$/수식$$km로 걸어서 미술관에 $$수식$${hour}$$/수식$$\n" \
           "시간 $$수식$${minute}$$/수식$$분 이내에 도착하려고 한다.\n" \
           "$$/표$$" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "시속 $$수식$${speed1}$$/수식$$km로 x km(단 x &lt; a)를 가고, 시속\n" \
              "$$수식$${speed2}$$/수식$$km로 (a-x) km를 가는데 $$수식$${hour}$$/수식$$시간 $$수식$${minute}$$/수식$$분 이내\n" \
              "로 도착하므로 $$수식$$rm x over {speed1}$$/수식$$ + $$수식$$rm a-x over {speed2}$$/수식$$ ≤ $$수식$${hour}$$/수식$$ + $$수식$${minute} over 60$$/수식$$\n" \
              "    ∴ $$수식$$rm x over {speed1}$$/수식$$ + $$수식$$rm a-x over {speed2}$$/수식$$ ≤ $$수식$${top} over {bottom}$$/수식$$\n"


    nameList = ["경희", "민철이", "수진이", "철수"]
    name = nameList[np.random.randint(0, 4)]
    locationList = ["미술관", "학교","집", "학원","병원"]
    location = locationList[np.random.randint(0, 5)]
    speed1 = np.random.randint(2, 7)
    speed2 = np.random.randint(2, 7)
    while speed1 == speed2:
        speed2 = np.random.randint(2, 7)

    hour = np.random.randint(1, 3)
    minute = np.random.randint(1, 6)*10
    top = hour*60 + minute
    gcd1 = gcd(top, 60)
    top = int(top/gcd1)
    bottom = int(60/gcd1)
    inequality1 = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    op1 = "$$수식$$rm x over {"+str(speed1)+"}$$/수식$$ + $$수식$$rm a-x over {"+str(speed2)+"}$$/수식$$ ≤ $$수식$${"+str(bottom)+"} over {"+str(top)+"}$$/수식$$"
    op2 = "$$수식$$rm x over {"+str(speed1)+"}$$/수식$$ - $$수식$$rm a-x over {"+str(speed2)+"}$$/수식$$ ≤ $$수식$${"+str(bottom)+"} over {"+str(top)+"}$$/수식$$"
    op3 = "$$수식$$rm x over {"+str(speed1)+"}$$/수식$$ + $$수식$$rm a-x over {"+str(speed2)+"}$$/수식$$ ≥ $$수식$${"+str(top)+"} over {"+str(bottom)+"}$$/수식$$"
    op4 = "$$수식$$rm x over {"+str(speed1)+"}$$/수식$$ - $$수식$$rm a-x over {"+str(speed2)+"}$$/수식$$ ≥ $$수식$${"+str(top)+"} over {"+str(bottom)+"}$$/수식$$"
    answ ="$$수식$$rm x over {"+str(speed1)+"}$$/수식$$ + $$수식$$rm a-x over {"+str(speed2)+"}$$/수식$$ ≤ $$수식$${"+str(top)+"} over {"+str(bottom)+"}$$/수식$$"

    bb = [op1, op2, op3, op4]
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(name=name, location=location, speed1=speed1, speed2=speed2, hour=hour, minute=minute, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(speed1=speed1, speed2=speed2,hour=hour, minute=minute, top=top, bottom=bottom)

    return stem, answer, comment

#중2-1-2-10
def expressions212_Stem_009():
    stem = "\na &lt; b일 때, 다음 중 옳은 것은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${list}$$/수식$$\n" \

    cc=[]
    a = np.random.randint(1, 20)
    op1 = "a + " + str(a) +" &gt; " + "b + " + str(a)
    cc.append("a + " + str(a) +" &lt; " + "b + " + str(a))
    a = np.random.randint(1, 20)
    op2 = "a - " + str(a) +" &gt; " + "b - " + str(a)
    cc.append("a - " + str(a) +" &lt; " + "b - " + str(a))
    a = np.random.randint(2, 20)
    op3 = str(a) +"a &gt; " + str(a) +"b"
    cc.append(str(a) +"a &lt; " + str(a) +"b")
    a = np.random.randint(2, 20)
    op4 = "$$수식$$rm a over {"+str(a)+"}$$/수식$$ &gt; $$수식$$rm b over {"+str(a)+"}$$/수식$$"
    cc.append("$$수식$$rma over {"+str(a)+"}$$/수식$$ &lt; $$수식$$rm b over {"+str(a)+"}$$/수식$$")
    a = np.random.randint(2, 20)
    answ = "-$$수식$$rm a over {" + str(a) + "}$$/수식$$ &gt; -$$수식$$rm b over {" + str(a) + "}$$/수식$$"

    bb = [op1, op2, op3, op4]
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    liste=""
    if rande == 1:
        liste = "\n②" + cc[0] + "\n③" + cc[1] + "\n④" + cc[2] + "\n⑤" + cc[3]
    elif rande == 2:
        liste = "\n①" + cc[0] + "\n③" + cc[1] + "\n④" + cc[2] + "\n⑤" + cc[3]
    elif rande == 3:
        liste = "\n①" + cc[0] + "\n②" + cc[1] + "\n④" + cc[2] + "\n⑤" + cc[3]
    elif rande == 4:
        liste = "\n①" + cc[0] + "\n②" + cc[1] + "\n③" + cc[2] +  "\n⑤" + cc[3]
    else:
        liste = "\n①" + cc[0] + "\n②" + cc[1] + "\n③" + cc[2] + "\n④" + cc[3]

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=liste)

    return stem, answer, comment


#중2-1-2-11
#box sign
def expressions212_Stem_010():
    stem = "\n다음 중 ☐ 안에 들어갈 부등호의 방향이 나머지\n" \
           "넷과 다른 하나는?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "{list}$$수식$$``$$/수식$$ " \

    bb=[]
    inequality1 = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    endd = "$$수식$$``$$/수식$$이면$$수식$$``$$/수식$$    a ☐ b$$수식$$``$$/수식$$"
    a = np.random.randint(1, 20)
    op1 = "a + " + str(a) +" &lt; " + "b + " + str(a) + endd
    lis = "a + " + str(a) +" &lt; " + "b + " + str(a) + "$$수식$$``$$/수식$$에서$$수식$$``$$/수식$$ a &lt; b\n"
    bb.append(lis)


    a = np.random.randint(1, 20)
    b = np.random.randint(2, 20)
    gcd1 = gcd(a, b)
    a = int(a/gcd1)
    b = int(b/gcd1)
    while b==1:
        a = np.random.randint(1, 20)
        b = np.random.randint(2, 20)
        gcd1 = gcd(a, b)
        a = int(a / gcd1)
        b = int(b / gcd1)
    op2 = "$$수식$$``$$/수식$$-a + $$수식$${" + str(a) +"} over {"+str(b)+"}$$/수식$$ &gt; " + "-b + $$수식$${" + str(a)+ "} over {"+str(b)+"}$$/수식$$$$수식$$``$$/수식$$" + endd
    lis ="$$수식$$``$$/수식$$-a + $$수식$${" + str(a) +"} over {"+str(b)+"}$$/수식$$ &gt; -b + $$수식$${" + str(a)+ "} over {"+str(b)+"}$$/수식$$$$수식$$``$$/수식$$에서$$수식$$``$$/수식$$-a &gt; -b$$수식$$``$$/수식$$\n∴ a &lt; b$$수식$$``$$/수식$$\n"
    bb.append(lis)


    a = np.random.randint(2, 20)
    b = np.random.randint(1, 20)
    op3 = str(a) + "a - " + str(b) + " &lt; " + str(a) + "b - "  + str(b) + endd
    lis = "$$수식$$``$$/수식$$" +str(a) + "a - " + str(b) + " &lt; " + str(a) + "b - "  + str(b) +"$$수식$$``$$/수식$$에서$$수식$$``$$/수식$$"+str(a) + "a &lt; " + str(a) + "b\n∴ a &lt; b\n"
    bb.append(lis)


    a = np.random.randint(2, 20)
    b = np.random.randint(1, 20)
    op4 = "$$수식$$rm a over {" + str(a) + "}$$/수식$$- " + str(b) +" &lt; $$수식$$rm b over {" + str(a) + "}$$/수식$$ - " + str(b) + endd
    lis = "$$수식$$``$$/수식$$" +"$$수식$$rm a over {" + str(a) + "}$$/수식$$- " + str(b) +" &lt; $$수식$$rm b over {" + str(a) + "}$$/수식$$ - " + str(b) +"$$수식$$``$$/수식$$에서$$수식$$``$$/수식$$$$수식$$rm a over {" + str(a) + "}$$/수식$$ &lt; $$수식$$rm b over {" + str(a) + "}$$/수식$$\n∴ a &lt; b\n"
    bb.append(lis)

    a = np.random.randint(2, 20)
    b = np.random.randint(1, 20)
    answ = "-" + str(a) + "a + " + str(b) + " &lt; -" + str(a) + "b + "  + str(b) + endd
    lis = "$$수식$$``$$/수식$$-" + str(a) + "a + " + str(b) + " &lt; -" + str(a) + "b + "  + str(b) +"$$수식$$``$$/수식$$에서$$수식$$``$$/수식$$-" + str(a) + "a &lt; -"+ str(a) + "b\n∴ a &gt; b\n"
    bb.append(lis)

    cc=[op1, op2, op3, op4]

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = cc[0]
        x3 = cc[1]
        x4 = cc[2]
        x5 = cc[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = cc[0]
        x3 = cc[1]
        x4 = cc[2]
        x5 = cc[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = cc[0]
        x2 = cc[1]
        x4 = cc[2]
        x5 = cc[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = cc[0]
        x2 = cc[1]
        x3 = cc[2]
        x5 = cc[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = cc[0]
        x2 = cc[1]
        x3 = cc[2]
        x4 = cc[3]
    liste = ""
    if rande == 1:
        liste = "①" + bb[4] + "②" + bb[0] + "③" + bb[1] + "④" + bb[2] + "⑤" + bb[3]
    elif rande == 2:
        liste = "①" + bb[0] + "②" + bb[4] + "③" + bb[1] + "④" + bb[2] + "⑤" + bb[3]
    elif rande == 3:
        liste = "①" + bb[0] + "②" + bb[1] + "③" + bb[4] + "④" + bb[2] + "⑤" + bb[3]
    elif rande == 4:
        liste = "①" + bb[0] + "②" + bb[1] + "③" + bb[2] + "④" + bb[4] + "⑤" + bb[3]
    else:
        liste = "①" + bb[0] + "②" + bb[1] + "③" + bb[2] + "④" + bb[3] + "⑤" + bb[4]

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=liste)

    return stem, answer, comment


#중2-1-2-12
def expressions212_Stem_011():
    stem = "\na$$수식$$``$$/수식$${inequality1}$$수식$$``$$/수식$$b$$수식$$``$$/수식$${inequality1}$$수식$$``$$/수식$$0, ac {inequality2} bc일 때, 다음 수를 작은 것부터\n" \
           "순서대로 나열하시오." \
           "$$표$$$$수식$$``$$/수식$$\n" \
           "$$수식$${list}$$/수식$$\n" \
           "$$/표$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n$$수식$$``$$/수식$$" \
              "a {inequality1} b {inequality1} 0이므로 $$수식$$``$$/수식$${temp1}$$수식$$``$$/수식$$"\
              "{temp2}$$수식$$``$$/수식$$" \
              "따라서 $$수식$$``$$/수식$${liste}$$수식$$``$$/수식$$이므로 작은\n" \
              "것부터 순서대로 나열하면$$수식$$``$$/수식$$\n" \
              "{ans}"

    inequality = [" &lt; ", " &gt;" ]
    inequality1 = inequality[np.random.randint(0, 2)]
    if inequality1 ==" &lt; ":
        temp1 = "$$수식$$``$$/수식$$- a &gt; -b &gt; 0\n∴$$수식$$``$$/수식$$0 &lt; -b &lt; -a &lt; -a - b$$수식$$``$$/수식$$\n"
        inequality2 =  "$$수식$$``$$/수식$$&gt;$$수식$$``$$/수식$$"
        temp2 = "a &lt; b, ac &gt; bc이므로 c &lt; 0\n"
        liste = "c &lt; -b &lt; -a &lt; -a-b"
        ans = "c, -b, -a, -a-b$$수식$$``$$/수식$$"
        list ="rm - a, -b, c, -a-b"
    else:
        temp1 = "- a &lt; -b &lt; 0\n∴ 0 &gt; -b &gt; -a &gt; -a - b\n"
        inequality2 = " &lt;"
        temp2 = "a &gt; b, ac &lt; bc이므로 c &lt; 0\n"
        liste = "-a-b &lt; -a &lt; -b &lt; -c"
        ans = "-a-b, -a, -b, -c"
        list = "-rm a, -b, -c, -a-b"

    stem = stem.format(list=list, inequality1=inequality1, inequality2=inequality2)
    answer = answer.format(ans=ans)
    comment = comment.format( inequality1=inequality1, inequality2=inequality2, temp1=temp1, temp2=temp2, liste=liste, ans=ans)

    return stem, answer, comment


#중2-1-2-13
def expressions212_Stem_012():
    stem = "\n다음 중 항상 옳은 것은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "{list}$$수식$$``$$/수식$$" \

    op1 = "ac &lt; bc이면 a &lt; b이다."
    op2 =  "a-c >b +c이면 a >b이다."
    op3 =  "$$수식$$1 over a$$/수식$$ &lt; $$수식$$1 over b$$/수식$$이면 a &gt; b이다."
    op4 = "$$수식$$rm a over c$$/수식$$ &lt; $$수식$$rm b over c$$/수식$$이면 a &lt; b이다."
    answ = "$$수식$$rm a over c$$/수식$$ &gt; $$수식$$rm b over c$$/수식$$이면 ac &gt; bc이다."

    cc=[op1, op2, op3, op4]
    bb=[]
    lis = "c &lt; 0이면a &gt; b이다.\n"
    bb.append(lis)
    lis = "a = 1, b = 2, c = -3일 때, 1 + 3 &gt; 2 - 3\n이지만1 &lt; 2이다.\n"
    bb.append(lis)
    lis = "a = -1, b = 1일 때, $$수식$$1 over -1$$/수식$$ &lt; $$수식$$1 over 1$$/수식$$이지만\n -1 &lt; 1이다.\n"
    bb.append(lis)

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = cc[0]
        x3 = cc[1]
        x4 = cc[2]
        x5 = cc[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = cc[0]
        x3 = cc[1]
        x4 = cc[2]
        x5 = cc[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = cc[2]
        x2 = cc[1]
        x4 = cc[0]
        x5 = cc[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = cc[0]
        x2 = cc[1]
        x3 = cc[3]
        x5 = cc[2]
    else:
        ans = "⑤"
        x5 = answ
        x1 = cc[2]
        x2 = cc[1]
        x3 = cc[0]
        x4 = cc[3]

    liste = ""
    if rande == 1:
        liste = "②, ⑤ " + bb[0] + "③ " + bb[1] + "④ " + bb[2]
    elif rande == 2:
        liste = "①, ⑤ " + bb[0] +  "③ " + bb[1] + "④ " + bb[2]
    elif rande == 3:
        liste = "① " + bb[2] + "② " + bb[1] +  "④, ⑤ " + bb[0]
    elif rande == 4:
        liste = "①, ③ " + bb[0] + "② " + bb[1] + "⑤ " + bb[2]
    else:
        liste = "① " + bb[2] + "② " + bb[1] + "③, ④ " + bb[0]


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=liste)

    return stem, answer, comment



#중2-1-2-14
def expressions212_Stem_013():
    stem = "\n$$수식$${low}$$/수식$$ ≤ x &lt; $$수식$${high}$$/수식$$이고 A = $$수식$${eq}$$/수식$$  일 때, A의 값의\n" \
           "범위는 a ≤ A &lt; b이다. 이때, a + b의 값은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${low}$$/수식$$ ≤ x &lt; $$수식$${high}$$/수식$$에서 $$수식$${mul}$$/수식$$\n" \
              " ∴ $$수식$${eq2}$$/수식$$        $$수식$$` , `$$/수식$$즉 $$수식$${A}$$/수식$$\n" \
              "따라서 a = $$수식$${ae}$$/수식$$, b = $$수식$${b}$$/수식$$이므로\n" \
              "a + b = $$수식$${answ}$$/수식$$" \


    inequality1 = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    low = np.random.randint(1, 6) * -1
    high = np.random.randint(1, 6)

    c = np.random.randint(2, 6)
    d = np.random.randint(1, 6)
    eq = str(c) + "x - " + str(d)
    mul = str(low*c) + " ≤ " + str(c) +"x &lt; " + str(high*c)
    a = low*c - d
    b = high*c - d
    eq2  = str(a) + " ≤ " + str(c) +"x - " + str(d) +" &lt; " + str(b)
    A = str(a) + " ≤ A &lt; " + str(b)
    answ = a+b

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(low=low, high=high, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(low=low, high=high, mul=mul, eq2=eq2, ae=a, b=b, A=A, answ=answ)

    return stem, answer, comment

#중2-1-2-15
def expressions212_Stem_014():
    stem = "\n$$수식$${low}$$/수식$$ &lt; x ≤ $$수식$${high}$$/수식$$이고 A = $$수식$${eq}$$/수식$$  일 때, A의 값의\n" \
           "범위를 만족시키는 A의 값 중 가장 큰 정수는?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${low}$$/수식$$ ≤ x &lt; $$수식$${high}$$/수식$$에서 $$수식$${mul}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$       이므로\n" \
              "$$수식$${A}$$/수식$$\n" \
              "따라서 A의 값 중 가장 큰 정수는 {answ}이다."

    low = np.random.randint(1, 6) * -1
    high = np.random.randint(1, 6)

    c = np.random.randint(2, 6)
    d = np.random.randint(1, 6)
    eq = str(d) + " - " + str(c) +"x"
    mul = str(high * c*-1) + " &lt; " + str(-1*c) + "x ≤ " + str(low * c*-1)
    a = high * c*-1 + d
    b = low * c*-1 + d
    eq2 = str(a) + " &lt; " + str(d) + " - " + str(c) +"x ≤ " + str(b)
    A = str(a) + " &lt; A ≤ " + str(b)
    answ = b

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, answ*2)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(low=low, high=high, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(low=low, high=high, mul=mul, eq2=eq2, ae=a, b=b, A=A, answ=answ)

    return stem, answer, comment

#중2-1-2-16
def expressions212_Stem_015():
    stem = "\n$$수식$${low}$$/수식$$ &lt; x &lt; $$수식$${high}$$/수식$$이고 A = $$수식$${eq}$$/수식$$  일 때, A의 값의\n" \
           "범위를 만족시키는 정수 A의 개수는?\n" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${low}$$/수식$$ ≤ x &lt; $$수식$${high}$$/수식$$에서 $$수식$${mul}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$       이므로\n" \
              "$$수식$${A}$$/수식$$\n" \
              "따라서 A의 값의 범위를 만족시키는 정수 A의\n" \
              "개수는 {list} 의 {answ}이다."

    low = np.random.randint(1, 6) * -1
    high = np.random.randint(1, 6)

    c = np.random.randint(2, 6)
    d = np.random.randint(1, 6)
    eq = str(c) + "x + " + str(d)
    mul = str(low * c) + " &lt; " + str(c) + "x &lt; " + str(high * c)
    a = low * c + d
    b = high * c + d
    eq2 = str(a) + " &lt; " + str(c) + "x + " + str(d) + " &lt; " + str(b)
    A = str(a) + " &lt; A &lt; " + str(b)
    answ = abs(b -a) -1
    list = str(a+1) +", " + str(a+2) +", " + str(a+3) +", " +"$$수식$$CDOTS$$/수식$$, " + str(b-2) +", " +str(b-1)

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(low=low, high=high, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=list, low=low, high=high, mul=mul, eq2=eq2, ae=a, b=b, A=A, answ=answ)

    return stem, answer, comment



#중2-1-2-17
def expressions212_Stem_016():
    stem = "\n$$수식$${low}$$/수식$$ &lt; x &lt; $$수식$${high}$$/수식$$  일 때, $$수식$${eq}$$/수식$$   $$수식$$``$$/수식$${temp}$$수식$$``$$/수식$$만족시키는 y\n" \
           "의 값의 범위는?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$   에서 $$수식$${eq2}$$/수식$$\n" \
              "∴ $$수식$${simplified}$$/수식$$\n" \
              "$$수식$${low}$$/수식$$ &lt; x &lt; $$수식$${high}$$/수식$$에서 $$수식$${ineq}$$/수식$$\n" \
              "∴ $$수식$${ans_eq}$$/수식$$ $$수식$$`, `$$/수식$$즉 ∴ $$수식$${answ}$$/수식$$"

    low = np.random.randint(2, 6) * -1
    high = low*-1

    c = np.random.randint(2, 10)
    d = high
    while c==d:
        c = np.random.randint(2, 10)
    e = np.random.randint(2, 5)*high
    eq = str(c) + "x + " + str(d) +"y = " +  str(e)
    eq2 = str(d) +"y = " + str(e) +" - " + str(c) +"x"
    gcd1 = gcd(d, e)
    simplified = "y = " + str(int(e/gcd1))
    gcd2 = gcd(d, c)
    if d ==gcd2:
        simplified = simplified + " - " + str(int(c/gcd2)) + "x"
        ineq = str(int(c/gcd2)*low) +" &lt; -" +str(int(c/gcd2)) + "x &lt; " + str(int(c/gcd2)*high)
        ans_eq = str(int(c/gcd2)*low+int(e/gcd1)) +" &lt; " +str(int(e/gcd1)) + " - " + str(int(c/gcd2)) + "x &lt; " + str(int(c/gcd2)*high+int(e/gcd1)) + "$$수식$$``$$/수식$$"
    else:
        simplified = simplified + " - $$수식$${"+str(int(c/gcd2))+"} over {"+str(int(d/gcd2))+"}$$/수식$$x"
        ineq = str(int((c / gcd2 * low)/(d/gcd2))) + " &lt; - $$수식$${"+str(int(c/gcd2))+"} over {"+str(int(d/gcd2))+"}$$/수식$$x &lt; " + str(int((c / gcd2 * high)/(d/gcd2)))
        ans_eq = str(int(((c / gcd2 * low)/(d/gcd2)) +(e / gcd1))) + " &lt; " + str(int(e / gcd1)) + " - $$수식$${"+str(int(c/gcd2))+"} over {"+str(int(d/gcd2))+"}$$/수식$$x &lt; " + str(int(((c / gcd2 * high)/(d/gcd2))+ int(e / gcd1))) +  "$$수식$$``$$/수식$$"

    low_bound = int(c / gcd2) * low + int(e / gcd1)
    high_bound = int(c / gcd2) * high + int(e / gcd1)
    answ = str(low_bound) + " &lt; y &lt; " + str(high_bound)
    temp = proc_jo(e, 4)
    bb = []
    lohi = []
    while len(bb) < 4:
        k = np.random.randint(0, abs(low_bound-10))
        p = np.random.randint(0, high_bound+10)
        o = [-1*k,p]
        if o not in lohi and k!= low_bound or p!=high_bound:
            lohi.append(o)
            j =str(-1*k) + " &lt; y &lt; " + str(p)
            bb.append(j)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(temp=temp, low=low, high=high, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(low=low, high=high, eq=eq, simplified=simplified, answ=answ, ans_eq=ans_eq, ineq=ineq,eq2=eq2)

    return stem, answer, comment



#중2-1-2-18
def expressions212_Stem_017():
    stem = "\n다음 조건을 모두 만족시키는 모든 x의 값의 합\n" \
           "은?\n" \
           "$$표$$\n" \
           "(가) x는 정수이다.\n" \
           "(나) x를 $$수식$${num1}$$/수식$$로 나누어 $$수식$${num2}$$/수식$$$$수식$$``$$/수식$${temp2}$$수식$$``$$/수식$$더하면 음수이다.\n" \
           "(다) x에서 $$수식$${num3}$$/수식$$$$수식$$``$$/수식$${temp3}$$수식$$``$$/수식$$ 뺀 다음 $$수식$${num4} over {num5}$$/수식$$배를 하면 $$수식$${low}$$/수식$$보다 크\n" \
           "고 $$수식$${high}$$/수식$$보다 크지 않다.\n" \
           "$$/표$$\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "(i) 조건 (나)를 부등식으로 나타내면\n" \
              "$$수식$$rm x over {num1}$$/수식$$ + $$수식$${num2}$$/수식$$ &lt; 0이므로 $$수식$$rm x over {num1}$$/수식$$←$$수식$${num2}$$/수식$$ ∴ x &gt; $$수식$${low_bound}$$/수식$$\n" \
              "이때 조건 (가)에서 x는 정수이므로 x의 값으로\n" \
              "가능한 값은 $$수식$${list}$$/수식$$  이다.\n" \
              "(ii) 조건 (다)를 부등식으로 나타내면\n" \
              "$$수식$${low}$$/수식$$ &lt; $$수식$${num4} over {num5}$$/수식$$(x - $$수식$${num3}$$/수식$$) ≤ $$수식$${high}$$/수식$$이므로\n" \
              "$$수식$${simplifed}$$/수식$$      ∴ $$수식$${ineq}$$/수식$$\n" \
              "이때 조건 (가)에서 x는 정수이므로 x의 값으로\n" \
              "가능한 값은 $$수식$${list2}$$/수식$$  이다.\n" \
              "(i), (ii)에서 조건을 모두 만족시키는 모든 x의\n" \
              "값은 $$수식$${list3}$$/수식$$  이므로 그 합은\n" \
              "$$수식$${ans_eq}$$/수식$$"

    num1 = np.random.randint(2, 10) * -1
    num2 = np.random.randint(2, 10)
    low_bound = num1 * num2 * -1
    temp2 = proc_jo(num2, 4)
    list = ""
    liste = []
    for i in range(low_bound + 1, low_bound + 3):
        liste.append(i)
        list = list + str(i) + "$$수식$$` , `$$/수식$$"
    list = list + str(low_bound + 3) + "$$수식$$CDOTS$$/수식$$"
    num3 = np.random.randint(1, 10)
    num4 = np.random.randint(1, 10)
    num5 = np.random.randint(2, 10)
    while num4 == num5:
        num5 = np.random.randint(2, 10)
    gcd1 = gcd(num4, num5)
    num4 = int(num4 / gcd1)
    num5 = int(num5 / gcd1)
    low = np.random.randint(1, 3) * num4
    high = np.random.randint(2, 4) * num4
    while low >= high:
        high = np.random.randint(2, 4) * num4
    a = int(low * (num5 / num4))
    b = int(high * (num5 / num4))
    simplifed = str(a) + " &lt; x - " + str(num3) + " ≤ " + str(b)
    ineq = str(a + num3) + " &lt; x ≤ " + str(b + num3)
    liste2 = []
    list2 = ""
    for i in range(a + num3 + 1, b + num3):
        liste2.append(i)
        list2 = list2 + str(i) + "$$수식$$` , `$$/수식$$"
    list2 = list2 + str(b + num3) + "$$수식$$$$/수식$$"




    while low_bound < a+num3 or low_bound >= b+num3:
        num1 = np.random.randint(2, 10) * -1
        num2 = np.random.randint(2, 10)
        low_bound = num1 * num2 * -1
        temp2 = proc_jo(num2, 4)
        list=""
        liste =[]
        for i in range(low_bound+1, low_bound+3):
            liste.append(i)
            list  = list + str(i) + "$$수식$$` , `$$/수식$$"
        list = list + str(low_bound+3) + "$$수식$$CDOTS$$/수식$$"
        num3 = np.random.randint(1, 10)
        num4 = np.random.randint(1, 10)
        num5 = np.random.randint(2, 10)
        while num4 == num5:
            num5 = np.random.randint(2, 10)
        gcd1 = gcd(num4, num5)
        num4 = int(num4/gcd1)
        num5 = int(num5/gcd1)
        low = np.random.randint(1, 3)*num4
        high = np.random.randint(2, 4)*num4
        while low >= high:
            high = np.random.randint(2, 4) * num4
        a = int(low*(num5/num4))
        b = int(high*(num5/num4))
        simplifed = str(a) +" &lt; x - " + str(num3) + " ≤ " + str(b)
        ineq = str(a+num3) +" &lt; x ≤ " + str(b+num3)
        liste2=[]
        list2 =""
        for i in range(a+num3+1, b+num3):
            liste2.append(i)
            list2 = list2 + str(i) + "$$수식$$` , `$$/수식$$"
        list2 = list2 + str(b+num3)+ "$$수식$$$$/수식$$"
    temp3 =proc_jo(num3,4)
    ans_eq =""
    list3=""
    answ= 0
    for i in range(low_bound+1, b+num3):
        list3 = list3 + str(i) +  "$$수식$$` , `$$/수식$$"
        ans_eq = ans_eq + str(i) +  " + "
        answ = answ + i
    answ = answ + b+num3
    list3 = list3 + str(b+num3)+ "$$수식$$$$/수식$$"
    ans_eq = ans_eq + str(b+num3) + " = " + str(answ) + "$$수식$$$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(temp2=temp2, num1=num1, num2=num2, num3=num3, num4=num4, num5=num5, temp3=temp3, low=low, high=high, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num1=num1, num2=num2, num3=num3, num4=num4, num5=num5, low=low, high=high, simplifed=simplifed, answ=answ, ans_eq=ans_eq,low_bound=low_bound,list=list, list2=list2, list3=list3,ineq=ineq )

    return stem, answer, comment

#중2-1-2-19
def expressions212_Stem_018():
    stem = "\n$$수식$${low}$$/수식$$ &lt; x ≤ $$수식$${high}$$/수식$$이고 A = $$수식$${eq}$$/수식$$    일 때, A의 값\n" \
           "중에서 가장 큰 정수를 M, 가장 작은 정수를 m\n" \
           "이라 하자. 이 때, M + m의 값은?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "A = $$수식$${eq}$$/수식$$    $$수식$$`=`$$/수식$$  $$수식$${eq2}$$/수식$$\n" \
              "$$수식$${low}$$/수식$$ &lt; x ≤ $$수식$${high}$$/수식$$에서 $$수식$${new_ineq}$$/수식$$\n" \
              "∴ $$수식$${eq3}$$/수식$$  $$수식$$`, `$$/수식$$즉 $$수식$${A}$$/수식$$\n" \
              "따라서 M = $$수식$${M}$$/수식$$, m = $$수식$${m}$$/수식$$  이므로\n" \
              "M + m = $$수식$${answ}$$/수식$$\n"

    low = np.random.randint(2, 6) * -1
    high = low * -1

    c = np.random.randint(2, 10)
    d = np.random.randint(1, 10)
    e = np.random.randint(2, 10)
    while c == d:
        c = np.random.randint(2, 10)
    e = np.random.randint(2, 5) * high
    eq = str(c) + "(" + str(d) +" -" + str(e) +"x)"
    eq2 = str(d*c) +" -" + str(e*c) +"x"
    new_ineq = str(low*e*c) + " ← " + str(e*c)+"x ≤ " +  str(high*e*c)
    eq3 = str(low*e*c+d*c) + " &lt;"+str(d*c)+" - " + str(e*c)+"x ≤ " +  str(high*e*c+d*c) + "$$수식$$$$/수식$$"
    A =  str(low*e*c+d*c) + " &lt; A ≤ " +  str(high*e*c+d*c)
    M = high*e*c+d*c
    m =low*e*c+d*c
    answ = M + m

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(eq=eq, low=low, high=high, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, low=low, high=high, A=A, eq3=eq3, eq2=eq2, M=M, m=m, answ=answ, new_ineq=new_ineq)

    return stem, answer, comment

#중2-1-2-20
def expressions212_Stem_019():
    stem = "\nx + y = $$수식$${num1}$$/수식$$일 때 x의 대한 부등식\n" \
           "$$수식$${eq}$$/수식$$       의 해는?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "x + y = $$수식$${num1}$$/수식$$에서 y = - x + $$수식$${num1}$$/수식$$\n" \
              "이것을 $$수식$${eq}$$/수식$$       에 대입하면\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$\n" \
              "$$수식$${eq4}$$/수식$$       ∴ $$수식$${answ}$$/수식$$"

    num1 = np.random.randint(1, 10)
    low = np.random.randint(1, 10)
    high = np.random.randint(low+3, 20)
    d = np.random.randint(2, 15)
    eq = str(low) + " &lt; " + str(d) +"x - y ≤ " + str(high)
    a = d+1
    b = low+num1
    c = high+num1
    while b % a !=0 or c% a!=0 or b<=a or c<=a:
        num1 = np.random.randint(1, 10)
        low = np.random.randint(1, 10)
        high = np.random.randint(low + 3, 20)
        d = np.random.randint(2, 15)
        eq = str(low) + "&lt;" + str(d) + "x - y ≤ " + str(high)
        a = d + 1
        b = low + num1
        c = high + num1
    loww = int(b/a)
    highh = int(c/a)
    eq2 = str(low) + " &lt; " + str(d) +"x - ( -x + "+str(num1) +") ≤ " + str(high)
    eq3 =  str(low) + " &lt; " + str(a) +"x - "+str(num1) +" ≤ " + str(high)
    eq4 = str(b) + " &lt; " + str(a) +"x ≤ " + str(c)
    answ = str(loww) + " &lt; x ≤ " + str(highh)

    bb = []
    lohi = []
    while len(bb) < 4:
        k = np.random.randint(0, abs(loww - 10))
        p = np.random.randint(0, highh + 10)
        o = [k, p]
        if k+3<=p or o not in lohi and k != loww or p != highh:
            lohi.append(o)
            j = str(k) + " &lt; x ≤ " + str(p)
            bb.append(j)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(num1=num1, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, num1=num1, eq4=eq4, eq3=eq3, eq2=eq2, answ=answ)

    return stem, answer, comment


#중2-1-2-21
def expressions212_Stem_020():
    stem = "\n다음 중 일차부등식은 것은?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "{list}"

    bb=[]
    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    c = np.random.randint(2, 6)
    d = np.random.randint(1, 6)
    ine = inequality[np.random.randint(0,4)]
    op1 = "x " + ine + "$$수식$${" + str(c) + "} over x$$/수식$$ + " + str(d)
    bb.append(" 분모에 문자가 있으므로 일차부등식이 아니다.\n")

    c = np.random.randint(2, 6)
    ine = inequality[np.random.randint(0, 4)]
    op2 = "x(x + " +str(c ) + ")" + ine  + "x"
    lis = " 정리하면 $$수식$$x ^2$$/수식$$" + ine + str(0) +"이므로 일차부등식이 아니다.\n"
    bb.append(lis)

    c = np.random.randint(1, 6)
    d = np.random.randint(1, 6)
    if c>=d:
        ine = " ≥ "
    else:
        ine = " &lt; "
    op3 = "x + " + str(c) + ine + "x + " + str(d)
    lis = " 정리하면 " + str(c) + ine +str(d) + "이므로 일차부등식이 아니다.\n"
    bb.append(lis)

    c = np.random.randint(2, 6)
    d = np.random.randint(1, 6)
    while d>= c:
        c = np.random.randint(2, 6)
        d = np.random.randint(1, 6)
    e = np.random.randint(2, 6)
    ine = inequality[np.random.randint(0, 4)]

    op4 = str(c) + " - $$수식$$x ^2$$/수식$$" +ine + str(d) + " + x -" +  str(e)+"$$수식$$x ^2$$/수식$$"
    lis = " 정리하면 " + str(e-1) + "$$수식$$x ^2$$/수식$$" + " - x + " + str(c-d) + ine + str(0) + "이므로 일차부등식\n" \
                                                                                            "이 아니다.\n"
    bb.append(lis)

    a = np.random.randint(2, 6)
    b = np.random.randint(1, 6)
    c = np.random.randint(2, 6)
    d = np.random.randint(1, 6)
    if a==c:
        c = np.random.randint(2, 6)
    ine = inequality[np.random.randint(0, 4)]

    answ = str(a) +"(x + " + str(b) +")" + ine + str(c) +"(x + " + str(d) +")"
    cc = [op1, op2, op3,op4]

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = cc[3]
        x3 = cc[0]
        x4 = cc[2]
        x5 = cc[1]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = cc[0]
        x3 = cc[1]
        x4 = cc[2]
        x5 = cc[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = cc[2]
        x2 = cc[1]
        x4 = cc[0]
        x5 = cc[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = cc[1]
        x2 = cc[2]
        x3 = cc[3]
        x5 = cc[0]
    else:
        ans = "⑤"
        x5 = answ
        x1 = cc[3]
        x2 = cc[2]
        x3 = cc[1]
        x4 = cc[0]
    liste = ""
    if rande == 1:
        liste = "②" + bb[3] + "③" + bb[0] + "④" + bb[2] + "⑤" + bb[1]
    elif rande == 2:
        liste = "①" + bb[0] + "③" + bb[1] + "④" + bb[2] + "⑤" + bb[3]
    elif rande == 3:
        liste = "①" + bb[2] + "②" + bb[1] + "④" + bb[0] + "⑤" + bb[3]
    elif rande == 4:
        liste = "①" + bb[1] + "②" + bb[2] + "③" + bb[3] + "⑤" + bb[0]
    else:
        liste = "①" + bb[3] + "②" + bb[2] + "③" + bb[1] + "④" + bb[0]


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=liste)

    return stem, answer, comment


#중2-1-2-22
def expressions212_Stem_021():
    stem = "\n일차부등식 $$수식$${eq}$$/수식$$      의 해는?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$      에서 $$수식$${eq2}$$/수식$$\n" \
              "$$수식$${ineq}$$/수식$$     ∴ $$수식$${answ}$$/수식$$"

    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    a = np.random.randint(2, 10)
    c = np.random.randint(1, 10)
    d = np.random.randint(1, 10)
    e = np.random.randint(2, 10)
    ine = inequality[np.random.randint(0, 4)]
    while True:
        a = np.random.randint(2, 10)
        c = np.random.randint(1, 10)
        d = np.random.randint(1, 10)
        e = np.random.randint(2, 10)
        if c+d > a-e and  a>e and (c+d) % (a-e) ==0 and a-e!=1:
            break
    eq = str(a) +"x - " +str(c) + ine + str(d) + " + " + str(e) +"x"
    eq2 =  str(a) +"x - " + str(e) +"x"+ ine + str(d) + " + " + str(c)
    ineq = str(a-e) +"x" + ine + str(d+c)
    answ = "x" + ine + str(int((d+c)/(a-e)))
    ch = int((d+c)/(a-e))
    bb=[]
    dd=[]
    k=""
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = ch + k
        else:
            k = abs(ch - k)
        if k not in dd and k != ch and k!=0:
            dd.append(k)
            t = "x" + ine + str(k)
            bb.append(t)

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, ineq=ineq, answ=answ)

    return stem, answer, comment


#중2-1-2-24
def expressions212_Stem_022():
    stem = "\n다음 중 문장을 부등식으로 나타낼 때, 일차부등\n" \
           "식이 아닌 것은?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "{list}"


    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    cc=[]
    a = np.random.randint(50, 70)
    b = np.random.randint(50, 70)
    op1 = "x와 " + str(a) +"의 평균은 " + str(b )+"보다 크다."
    lis = " $$수식$${x+"+str(a)+"} over 2$$/수식$$ &gt; " + str(b) + "    ∴ $$수식$$rm x over 2$$/수식$$ - $$수식$${"+str(2*b-a)+"} over 2$$/수식$$ &gt; " + str(0) + "\n"
    cc.append(lis)


    a = np.random.randint(2, 10)
    b = np.random.randint(2, 10)*1000
    op2 = "한 장에 x원인 스티커 " + str(a) +"장의 가격은 " +  str(b) +"원\n미만이다."
    lis = " " + str(a) + "$$수식$$TIMES$$/수식$$ x &lt; " +str(b) + "    ∴ "+ str(a) +"x - " +str(b) + " &lt; " + str(0) +"\n"
    cc.append(lis)


    a = np.random.randint(50, 70)
    b = np.random.randint(0, 6)
    op3 = "x km의 거리를 시속 " + str(a) +"km로 가면 " + str(b) +"시간 이\n상 걸린다."
    lis = " $$수식$$rm x over {"+str(a)+"}$$/수식$$ ≥ " + str(b) + "    ∴ $$수식$$rm x over {"+str(a)+"}$$/수식$$ - " + str(b) +" ≥ " + str(0)+"\n"
    cc.append(lis)

    a = np.random.randint(2, 5)
    b = np.random.randint(1, 10)
    c = np.random.randint(2, 4)
    while a==c:
        c = np.random.randint(2, 4)

    op4 = "x의 " + str(a) +"의 배수에 " + str(b) + proc_jo(b, 4) + "$$수식$$``$$/수식$$더한 수는 x의 " + str(c) +"배보다\n작거나 같다."
    if a-c==1:
        lis = " " + str(a) + "x + " + str(b) + " ≤ " + str(c) + "x    ∴ x + " + str(b) + " ≤ " + str(0) + "\n"
    elif a-c == -1:
        lis = " " + str(a) + "x + " + str(b) + " ≤ " + str(c) + "x    ∴ -x + " + str(b) + " ≤ " + str(0) + "\n"
    else:
        lis = " " + str(a) + "x + " + str(b) + " ≤ " + str(c) + "x    ∴ " + str(a - c) + "x + " + str(b) + " ≤ " + str(0) + "\n"
    cc.append(lis)

    a = np.random.randint(2, 5)*100
    answ = "한 변의 길이가 x cm인 정사각형의 넓이는\n" + str(a) + "$$수식$$rm cm ^2$$/수식$$ 보다 크지 않다."

    lis = " x $$수식$$TIMES$$/수식$$ x ≤ " + str(a) + "    ∴ $$수식$$rm x ^2$$/수식$$ - " + str(a) + " ≤ " + str(0)+"\n"
    cc.append(lis)
    bb=[op1, op2, op3, op4]

    t=""

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[2]
        x4 = bb[3]
        x5 = bb[1]
        t = "①" + cc[4] + "②" + cc[0] + "③" + cc[2] + "④" + cc[3] + "⑤" + cc[1]
    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
        t = "①" + cc[0] + "②" + cc[4] + "③" + cc[1] + "④" + cc[2] + "⑤" + cc[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[3]
        x2 = bb[0]
        x4 = bb[1]
        x5 = bb[2]
        t = "①" + cc[3] + "②" + cc[0] + "③" + cc[4] + "④" + cc[1] + "⑤" + cc[2]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[2]
        x2 = bb[1]
        x3 = bb[0]
        x5 = bb[3]
        t = "①" + cc[2] + "②" + cc[1] + "③" + cc[0] + "④" + cc[4] + "⑤" + cc[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[1]
        x2 = bb[0]
        x3 = bb[2]
        x4 = bb[3]
        t = "①" + cc[1] + "②" + cc[0] + "③" + cc[2] + "④" + cc[3] + "⑤" + cc[4]

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=t)

    return stem, answer, comment



#중2-1-2-25
def expressions212_Stem_023():
    stem = "\n부등식 ax + $$수식$${b}$$/수식$$x + $$수식$${c}$$/수식$$ {d} $$수식$${eq}$$/수식$$$$수식$$``$$/수식$${temp1}$$수식$$``$$/수식$$ x에 대한 일차\n" \
           "부등식이 되게 하는 상수 a의 조건은?\n"\
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "ax + $$수식$${b}$$/수식$$x + $$수식$${c}$$/수식$$ {d} $$수식$${eq}$$/수식$$$$수식$$``$$/수식$${temp2}$$수식$$``$$/수식$$정리하면\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "이때 일차부등식이 되려면 $$수식$${key}$$/수식$$     이어야 한다.\n" \
              "∴ $$수식$${answ}$$/수식$$"

    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    d = inequality[np.random.randint(0, 4)]


    b = np.random.randint(2, 10)
    c = np.random.randint(2, 10)
    e = np.random.randint(2, 10)
    f = np.random.randint(2, 10)
    while e>= b:
        b = np.random.randint(2, 10)
        e = np.random.randint(2, 10)
    eq = str(e) +"x - " +str(f)
    temp1 =  proc_jo(f, 0)
    temp2 = proc_jo(f, 4)
    ans11 = e-b
    eq2 = "(a + " + str(b-e) +")x +" + str(c+f) + d +  str(0)
    key = "a + " + str(b-e) + " ≠ " +  str(0)
    answ = "a ≠ " +  str(ans11)

    dd=[]
    bb=[]
    while len(bb) <2:
        h = np.random.randint(0,5)
        if h not in dd and h!=answ:
            dd.append(h)
            t = "a ≠ " + str(h)
            bb.append(t)
    while len(bb) <4:
        h = np.random.randint(0,5)
        if (-1*h) not in dd and (-1*h)!=answ:
            dd.append(-1*h)
            t = "a ≠ " + str(-1*h)
            bb.append(t)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(temp1=temp1, b=b, c=c, d=d, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(b=b, c=c, d=d, eq=eq, eq2=eq2, key=key, answ=answ,temp2=temp2)

    return stem, answer, comment



#중2-1-2-26
def expressions212_Stem_024():
    stem = "\n부등식 $$수식$${a}$$/수식$$$$수식$$x ^2$$/수식$$ + ax {ine} $$수식$${eq}$$/수식$$$$수식$$``$$/수식$${temp1}$$수식$$``$$/수식$$ x에 대한 일\n" \
           "차부등식이 되도록 하는 상수 a, b의 조건은?\n"\
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "부등식 $$수식$${a}$$/수식$$$$수식$$x ^2$$/수식$$ + ax {ine} $$수식$${eq}$$/수식$$에서\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "이 부등식이 일차부등식이 되려면\n" \
              "$$수식$${keys}$$/수식$$        ∴ $$수식$${answ}$$/수식$$"

    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    ine = inequality[np.random.randint(0, 4)]

    bb=[]
    a = np.random.randint(2, 10)
    b = np.random.randint(2, 10)
    while a==b:
        b = np.random.randint(2, 10)

    c= np.random.randint(2, 10)
    eq = "b$$수식$$x ^2$$/수식$$ - " + str(b) +"x + " + str(c) + "$$수식$$$$/수식$$"
    eq2 = "(" + str(a) +" - b)$$수식$$x ^2$$/수식$$ + (a + " + str(b) +")x - " + str(c) + ine + str(0)
    keys ="a + " + str(b) + " ≠ " + str(0) +"  ,   " + str(a) + " - b = " + str(0)
    answ = "a ≠ " + str(-b) +", b = " + str(a)
    bb.append("a ≠ " + str(b) +", b = " + str(a))
    bb.append("a ≠ " + str(-b) +", b = " + str(-a))
    bb.append("a ≠ " + str(b) +", b = " + str(b))
    bb.append("a ≠ " + str(b) +", b = " + str(-a))
    temp = proc_jo(c, 0)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(a=a, eq=eq, ine=ine, temp1=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, a=a, eq2=eq2, keys=keys,ine=ine,answ=answ)

    return stem, answer, comment

#중2-1-2-27
def expressions212_Stem_025():
    stem = "\n방정식 $$수식$${eq}$$/수식$$       의 해가 x = a일 때,\n" \
           "x에 대한 일차부등식 $$수식$${eq2}$$/수식$$      의 해는?\n"\
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$      에서 $$수식$${eq3}$$/수식$$\n" \
              "$$수식$${x_eq}$$/수식$$   ∴ x = $$수식$${x}$$/수식$$\n" \
              "따라서 a = $$수식$${x}$$/수식$$이므로 주어진 일차부등식은\n" \
              "$$수식$${eq4}$$/수식$$\n" \
              "$$수식$${answ}$$/수식$$"


    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    ine = inequality[np.random.randint(0, 2)]

    bb = []
    a = np.random.randint(2, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)
    d = np.random.randint(1, 10)
    mul_x = d-c+(b*a)
    while mul_x % a !=0:
        a = np.random.randint(2, 10)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 10)
        d = np.random.randint(1, 10)
        mul_x = d - c + (b * a)
    eq = str(a) +"(x - " + str(b) +") + " + str(c) +" = " + str(d)
    eq3 = str(a) +"x - " + str(b*a) +" + " + str(c) +" = " + str(d)
    x_eq = str(a)+"x = "+ str(mul_x)
    x = int(mul_x/a)

    a = np.random.randint(1, 10)
    b = np.random.randint(2, 10)
    c = np.random.randint(2, 10)
    while (c*x+a)%(1-b)!=0:
        a = np.random.randint(1, 10)
        b = np.random.randint(2, 10)
        c = np.random.randint(2, 10)
    eq2 = "x - " + str(a) + ine + str(b) +"x + " + str(c) +"a"
    eq4 = "x - " + str(a) + ine + str(b) +"x + " + str(c*x)
    if 1-b==-1:
        eq4 = eq4 + "   ,  -x" + ine
    else:
        eq4 = eq4 + "   ,  "+ str(1-b) +"x" + ine
    eq4 = eq4 + str(c*x+a)
    ans11 = int((c*x+a)/(1-b))


    temp =""
    if ine ==" &lt; ":
        temp =" &gt; "
    else:
        temp = " &lt; "
    answ = "x" + temp + str(ans11)

    bb.append("x" + ine + str(ans11))
    bb.append("x" + temp + str(-ans11))
    bb.append("x" + ine + str(-ans11))
    bb.append("x" + ine + str(0))


    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[3]
        x4 = bb[2]
        x5 = bb[1]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[2]
        x4 = bb[1]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[3]
        x2 = bb[1]
        x4 = bb[0]
        x5 = bb[2]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[2]
        x2 = bb[3]
        x3 = bb[1]
        x5 = bb[0]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, eq2=eq2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq,eq3=eq3, x_eq=x_eq, x=x, eq4=eq4, answ=answ, eq2=eq2)

    return stem, answer, comment



#중2-1-2-29
def expressions212_Stem_026():
    stem = "\n일차부등식 $$수식$${eq}$$/수식$$    {ine} $$수식$${eq2}$$/수식$$     의 해는?\n"\
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$    {ine} $$수식$${eq2}$$/수식$$     에서 괄호를 풀면\n" \
              "$$수식$${eq3}$$/수식$$\n" \
              "$$수식$${x}$$/수식$$     ∴ $$수식$${answ}$$/수식$$"

    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    ine = inequality[np.random.randint(2, 4)]

    bb = []
    a = np.random.randint(2, 10)
    b = np.random.randint(2, 10)
    c = np.random.randint(1, 10)
    eq = str(a) +"(" + str(b) +"x + " + str(c) +")"
    ff = b*a
    gg = c*a
    eq3 = str(b*a) +"x + " + str(c*a) + ine

    a = np.random.randint(2, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)
    eq2 = str(a) +"(x - " + str(b) +") + " + str(c)
    eq3 =  eq3 + str(a) +"x - " + str(b*a) +" + " + str(c)
    x = str(ff-a) + "x" + ine + str((c-b*a)-gg)
    while ff<=a or ((c-b*a)-gg) % (ff-a) !=0 or (c - b * a)==gg:
        a = np.random.randint(2, 10)
        b = np.random.randint(2, 10)
        c = np.random.randint(1, 10)
        eq = str(a) + "(" + str(b) + "x + " + str(c) + ")"
        ff = b * a
        gg = c * a
        eq3 = str(b * a) + "x + " + str(c * a) + ine

        a = np.random.randint(2, 10)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 10)
        eq2 = str(a) + "(x - " + str(b) + ") + " + str(c)
        eq3 = eq3 + str(a) + "x - " + str(b * a) + " + " + str(c)
    if ff-a ==1:
        x = "x" + ine + str((c - b * a) - gg)
    else:
        x = str(ff - a) + "x" + ine + str((c - b * a) - gg)

    ans11 = int(((c - b * a) - gg)/(ff-a))
    answ = "x" + ine + str(ans11)
    temp = ""
    if ine == " ≤ ":
        temp = " ≥ "
    else:
        temp = " ≤ "

    bb.append("x" + ine + str(-ans11))
    bb.append("x" + temp + str(ans11))
    bb.append("x" + temp + str(-ans11))
    bb.append("x &lt; " + str(-ans11))

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[3]
        x4 = bb[2]
        x5 = bb[1]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[2]
        x4 = bb[1]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[3]
        x2 = bb[1]
        x4 = bb[0]
        x5 = bb[2]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[2]
        x2 = bb[3]
        x3 = bb[1]
        x5 = bb[0]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(eq=eq, ine=ine, eq2=eq2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(ine=ine, eq=eq, eq3=eq3,  x=x, answ=answ, eq2=eq2)

    return stem, answer, comment


#중2-1-2-30
def expressions212_Stem_027():
    stem = "\n일차부등식 $$수식$${eq}$$/수식$$    {ine} $$수식$${eq2}$$/수식$$     를 만족시키는\n" \
           "x에 대하여 A = $$수식$${eq3}$$/수식$$    일 때, 가장 작은 정수\n" \
           "A의 값을 구하시오."
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$    {ine} $$수식$${eq2}$$/수식$$      에서\n" \
              "$$수식$${simplified}$$/수식$$\n" \
              "$$수식$${mul_x}$$/수식$$     ∴$$수식$${x}$$/수식$$\n" \
              "$$수식$${x}$$/수식$$  에서 $$수식$${range}$$/수식$$\n" \
              "∴$$수식$${eq33}$$/수식$$      ,즉 A {temp} $$수식$${poi}$$/수식$$\n" \
              "따라서 가장 작은 정수 A의 값은 $$수식$${ans}$$/수식$$ 이다."

    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    ine = " &lt; "
    a = np.random.randint(2, 10)
    b = np.random.randint(1, 10)
    eq = str(a) + "(x - " + str(b) + ")"

    c = np.random.randint(1, 10)
    eq2 = "-(x - " + str(c) +")"

    d = np.random.randint(2, 10)
    e = np.random.randint(2, 10)
    eq3 = "-" + str(d) +" + " +  str(e)

    simplified = str(a) +"x - " + str(a*b) + ine +"-x + " + str(c)
    mul_x = str(a+1) +"x" + ine + str(c+(b*a))
    x= "x" + ine + str(int((c+(b*a))/(a+1)))
    temp = ""
    if ine == " &lt; ":
        temp = " &gt; "
    else:
        temp = " &lt; "
    range = "-" +  str(d) +"x" + temp + str(int((c+(b*a))/(a+1))*-d)
    eq33 = "-" +  str(d) +"x + " + str(e) + temp + str(int((c+(b*a))/(a+1))*(-d)+e)
    answ1 = int((c+(b*a))/(a+1))*(-d)+e
    poi = answ1
    if temp == " &gt; ":
        ans =  answ1+1
    else:
        ans = answ1 - 1

    while (c + (b*a)) % (a + 1) != 0 or temp==" &lt; ":
        a = np.random.randint(2, 10)
        b = np.random.randint(1, 10)
        eq = str(a) + "(x - " + str(b) + ")"

        c = np.random.randint(1, 10)
        eq2 = "-(x - " + str(c) + ")"

        d = np.random.randint(2, 10)
        e = np.random.randint(2, 10)
        eq3 = "-" + str(d) + "x + " + str(e)

        simplified = str(a) + "x - " + str(a * b) + ine + "-x + " + str(c)
        mul_x = str(a + 1) + "x" + ine + str(c + (b*a))
        x = "x" + ine + str(int((c + (b*a)) / (a + 1)))
        temp = ""
        if ine == " &lt; ":
            temp = " &gt; "
        else:
            temp = " &lt; "
        range = "-" + str(d) + "x" + temp + str(int((c + (b*a)) / (a + 1)) * -d)
        eq33 = "-" + str(d) + "x + " + str(e) + temp + str(int((c + (b*a)) / (a + 1)) * (-d) + e)
        answ1 = int((c + (b*a)) / (a + 1)) * (-d) + e
        poi =answ1
        if temp == " &gt; ":
            ans = answ1 + 1
        else:
            ans = answ1 - 1


    stem = stem.format(eq=eq, ine=ine, eq2=eq2, eq3=eq3)
    answer = answer.format(ans=ans)
    comment = comment.format(temp=temp, eq33=eq33, mul_x=mul_x, simplified=simplified, range=range,poi=poi,  ine=ine, eq=eq, eq3=eq3, x=x, ans=ans, eq2=eq2)

    return stem, answer, comment

#중2-1-2-31
def expressions212_Stem_028():
    stem = "\n일차부등식 $$수식$${eq}$$/수식$$를 만족시키는\n" \
           "x의 값 중에서 가장 큰 정수를 a, 일차부등식\n" \
           "$$수식$${eq2}$$/수식$$ $$수식$$``$$/수식$${temp2}$$수식$$``$$/수식$$ 만족시키는 x의 값 중\n" \
           "에서 가장 작은 정수를 b라 할 때, ab의 값을 구\n" \
           "하시오."
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서\n" \
              "$$수식$${eq3}$$/수식$$\n" \
              "∴$$수식$${x1}$$/수식$$    ∴ a = $$수식$${a}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$ 에서\n" \
              "$$수식$${eq4}$$/수식$$\n" \
              "∴$$수식$${x2}$$/수식$$    ∴ b = $$수식$${b}$$/수식$$\n" \
              "∴ ab = $$수식$${ans}$$/수식$$"


    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    ine = inequality[np.random.randint(0, 2)]

    a = np.random.randint(2, 5)
    b = np.random.randint(2, 10)
    c = a
    d = np.random.randint(1, 10)
    e = a
    gcd1 = gcd(d,e)
    d = int(d/gcd1)
    e = int(e/gcd1)
    while e==1:
        a = np.random.randint(2, 5)
        b = np.random.randint(2, 10)
        c = a
        d = np.random.randint(1, 10)
        e = a
        gcd1 = gcd(d, e)
        d = int(d / gcd1)
        e = int(e / gcd1)

    eq = "$$수식$$x over {"+str(a)+"}$$/수식$$ - " + str(b)+"(x + $$수식$$1 over {"+str(c)+"}$$/수식$$)" + ine + "$$수식$${"+str(d)+"} over {"+str(e)+"}$$/수식$$x $$수식$$$$/수식$$ "
    eq3 = "x - " + str(a*b) +"x - " + str(b) +  ine + str(d) +"x"
    if 1-a*b-d !=1:
        eq3 = eq3 + " , " + str(1 - a * b - d) + "x" + ine + str(b)
    else:
        eq3 = eq3 + " , x" + ine + str(b)
    if ine == " &lt; ":
        temp = " &gt; "
    else:
        temp = " &lt; "
    n =1-a*b-d
    gcd2 = gcd(b,n*-1)
    n = int(n/gcd2)
    b = int(b/gcd2)
    x1 = "x" + temp + "$$수식$${"+str(b)+"} over {"+str(n)+"}$$/수식$$"
    if temp == " &gt; ":
        a = int(b/n+1)
    else:
        a = int(b/n-1)
    if n<0:
        x1 = "x" + temp + "-$$수식$${" + str(b) + "} over {" + str(n*-1) + "}$$/수식$$"
    elif b<0:
        x1 = "x" + temp + "-$$수식$${" + str(b*-1) + "} over {" + str(n) + "}$$/수식$$"
    elif n<0 and b<0:
        x1 = "x" + temp + "$$수식$${" + str(b * -1) + "} over {" + str(n) + "}$$/수식$$"


    b = np.random.randint(2, 5)
    c = np.random.randint(1, 10)
    d = np.random.randint(2, 5)
    e = np.random.randint(2, 5)
    f = np.random.randint(2, 5)
    g = np.random.randint(2, 5)
    ine = inequality[np.random.randint(0, 2)]

    eq2="-$$수식$${"+str(b)+"x - " + str(c) +"} over {"+str(d)+"}$$/수식$$    " +  ine + str(e) + " + $$수식$${"+str(f) +" - x} over {"+str(g)+"}$$/수식$$"
    lcm1 = lcm(d, g)
    b = int(lcm1/d)*b
    c = int(lcm1/d)*c
    e= e*lcm1
    f = int(lcm1/g)*f
    q = int(lcm1/g)
    while b<=q:
        b = np.random.randint(2, 5)
        c = np.random.randint(1, 10)
        d = np.random.randint(2, 5)
        e = np.random.randint(2, 5)
        f = np.random.randint(2, 5)
        g = np.random.randint(2, 5)
        ine = " &lt; "

        eq2 = "-$$수식$${" + str(b) + "x - " + str(c) + "} over {" + str(d) + "}$$/수식$$    " + ine + str(
            e) + " + $$수식$${" + str(f) + " - x} over {" + str(g) + "}$$/수식$$"
        lcm1 = lcm(d, g)
        b = int(lcm1 / d) * b
        c = int(lcm1 / d) * c
        e = e * lcm1
        f = int(lcm1 / g) * f
        q = int(lcm1 / g)
    eq4 = "-" + str(b) +"x + " +str(c) + ine + str(e) + " + " + str(f) + " - "
    if b==1:
        eq4 = "-x + " +str(c) + ine + str(e) + " + " + str(f) + " - "
    if q==1:
        eq4 = eq4 + "x"
    else:
        eq4 = eq4 + str(q) +"x"
    if -b+q==1:
        eq4 = eq4 + " , x" + ine  + str(e + f - c)
    else:
        eq4 = eq4 + " , " + str(-b+q) + "x" + ine + str(e+f-c)
    while -b+q==0 or e+f-c==0:
        b = np.random.randint(2, 5)
        c = np.random.randint(1, 10)
        d = np.random.randint(2, 5)
        e = np.random.randint(2, 5)
        f = np.random.randint(2, 5)
        g = np.random.randint(2, 5)
        ine = inequality[np.random.randint(0, 2)]

        eq2 = "-$$수식$${" + str(b) + "x - " + str(c) + "} over {" + str(d) + "}$$/수식$$   " + ine + str(
            e) + " + $$수식$${" + str(f) + " - x} over {" + str(g) + "}$$/수식$$"
        lcm1 = lcm(d, g)
        b = int(lcm1 / d) * b
        c = int(lcm1 / d) * c
        e = e * lcm1
        f = int(lcm1 / g) * f
        q = int(lcm1 / g)
        eq4 = "-" + str(b) + "x + " + str(c) + ine + str(e) + " + " + str(f) + " - " + str(q) + "x"
        if -b + q != 1:
            eq4 = eq4 + " , " + str(-b + q) + "x" + ine + str(e + f - c)
        else:
            eq4 = eq4 + " , x" + ine + str(e + f - c)
    temp = ine
    m=0
    n=0

    temp = " &gt; "

    if (e+f-c)%(-b+q) ==0:
        m = (e+f-c)
        n = (-b+q)
        x2 = "x" + temp+ str(int((e+f-c)/(-b+q)))
    else:
        gcd3=0
        m = e+f-c
        n = -b+q
        if n<0:
            if m>0:
                gcd3 = gcd(m,n*-1)
            elif m<0:
                gcd3 = gcd(m*-1, n * -1)
        else:
            if m>0:
                gcd3 = gcd(m, n)
            elif m<0:
                gcd3 = gcd(m * -1, n)

        m = int(m/gcd3)
        n = int(n/gcd3)
        if m<0:
            if n<0:
                x2 = "x" + temp + "$$수식$${"+str(m)+"} over {"+str(n)+"}$$/수식$$"
            else:
                x2 = "x" + temp + "-$$수식$${" + str(m*-1) + "} over {" + str(n) + "}$$/수식$$"
        else:
            if n < 0:
                x2 = "x" + temp + "-$$수식$${" + str(m) + "} over {" + str(n*-1) + "}$$/수식$$"
            else:
                x2 = "x" + temp + "$$수식$${" + str(m) + "} over {" + str(n) + "}$$/수식$$"
    if n!=0:
        if temp == " &gt; ":
            b = int(m/n+1)
        else:
            b = int(m/n-1)
    temp2 = proc_jo(f,4)

    ans = a*b


    stem = stem.format(eq=eq, eq2=eq2, temp2=temp2)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, eq3=eq3, x1=x1, x2=x2, a=a, b=b, eq4=eq4, ans=ans)

    return stem, answer, comment


#중2-1-2-32
def expressions212_Stem_029():
    stem = "\nx에 대한 일차부등식\n" \
           "$$수식$${eq}$$/수식$$\n{temp}$$수식$$``$$/수식$$ 만족시키는\n" \
           "모든 자연수 x의 값을 구하시오."
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$           에서\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "이때 $$수식$${ab}$$/수식$$  에서 $$수식$${ab2}$$/수식$$    이므로\n" \
              "$$수식$${x_eq}$$/수식$$     ∴ $$수식$${x}$$/수식$$\n" \
              "따라서 주어진 부등식을 만족시키는 모든 자연수\n" \
              "x의 값은 {ans}"

    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    ine = inequality[1]

    a = np.random.randint(2, 15)
    b = np.random.randint(1, 15)
    c = np.random.randint(2, 15)
    d = np.random.randint(1, 15)
    while (c-b)%a!=0 or ((c-b)/a) != (d-c) or c==b or c>=d or d-c<=1:
        a = np.random.randint(2, 15)
        b = np.random.randint(1, 15)
        c = np.random.randint(2, 15)
        d = np.random.randint(1, 15)
    eq = "a(" + str(a) +"x + " + str(b) +") - " + str(c) +"(a + b)" + ine +"b(x -" + str(d) +")"
    temp = proc_jo(d,4)
    eq2 = "(" + str(a) +"a - b" +")x" + ine + str(c-b) +"a - " + str(d-c) + "b"
    ee=""
    if ine == " &gt; ":
        ee = " &lt; "
    else:
        ee =" &gt; "
    ab = str(a) +"a" + ee + "b"
    ab2 = str(a)+"a - b" + ee + str(0)
    x_eq = "x" + ee + "$$수식$${"+str(d-c)+"("+str(a)+"a - b)} over {("+str(a)+"a - b)}$$/수식$$"
    x = "x" + ee + str(d-c)

    dd=[]
    answ=""
    for i in range(1, d-c):
        dd.append(i)
    for i in range(len(dd)-1):
        answ = answ + str(dd[i]) + " , "
    ans = answ + str(dd[-1])


    stem = stem.format(eq=eq,temp=temp)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, x_eq=x_eq, ab=ab, ab2=ab2, x=x, ans=ans)

    return stem, answer, comment



#중2-1-2-33
def expressions212_Stem_030():
    stem = "\n[a]를 a보다 크지 않은 최대의 정수라 할 때, 부\n" \
           "등식 $$수식$${eq}$$/수식$$        $$수식$$``$$/수식$${temp}$$수식$$``$$/수식$$ 만족시키는 가장\n" \
           "큰 정수 x의 값을 구하시오."
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "[$$수식$${num1}$$/수식$$] =  $$수식$${num11}$$/수식$$ , [$$수식$${num2}$$/수식$$  ] =  $$수식$${num22}$$/수식$$이므로 주어진 부등식\n" \
              "은\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "∴ {ans_eq}\n" \
              "따라서 가장 큰 정수 x의 값은 {ans}이다."


    inequality = [" &lt; ", " ≤ "]
    ine = inequality[random.randint(0,1)]
    num1 = random.randint(101, 400)/100
    num2 = random.randint(201, 400)/100*-1
    num3 = random.randint(1, 10)
    eq = "["+str(num1)+"] - ["+str(num2)+"]x" + ine + str(num3)
    num11 = int(num1)
    num22 = int(num2)-1
    while num3<=num11:
        num1 = random.randint(101, 400) / 100
        num2 = random.randint(201, 400) / 100 * -1
        num3 = random.randint(1, 10)
        eq = "[" + str(num1) + "] - [" + str(num2) + "]x" + ine + str(num3)
        num11 = int(num1)
        num22 = int(num2)-1
    eq2 = str(num11) +" - (" + str(num22) +") $$수식$$TIMES$$/수식$$ x" + ine + str(num3) +" ,  " + str(num22*-1) +"x" + ine +str(num3-num11)

    ans_eq=""
    if (num3-num11)%num22 ==0:
        ans_eq = "x" + ine +  str(int((num3-num11)/num22*-1))
    else:
        a = num3-num11
        b = num22*-1
        gcd1 = gcd(a,b)
        a = int(a/gcd1)
        b = int(b/gcd1)
        ans_eq = "x" + ine + "$$수식$${"+str(a)+"} over {"+str(b)+"}$$/수식$$ = " + str(a/b)
        if (a/b*10000)%1!=0 :
            ans_eq = "x" + ine + "$$수식$${" + str(a) + "} over {" + str(b) + "}$$/수식$$ = " + str(round(a / b, 3)) + "$$수식$$CDOTS$$/수식$$"
    temp = proc_jo(num3, 4)
    ans=int((num3-num11)/num22*-1)
    if ine == " &lt; " and (num3-num11)%num22 ==0:
        ans = int((num3 - num11) / num22 * -1) -1


    stem = stem.format(eq=eq, temp=temp)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, num1=num1, num2=num2, num11=num11, num22=num22,ans_eq=ans_eq, eq2=eq2, ans=ans)

    return stem, answer, comment



#중2-1-2-34
def expressions212_Stem_031():
    stem = "\n일차부등식 $$수식$${eq}$$/수식$$의 해는?\n" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$의 양변에 $$수식$${lcm1}$$/수식$$을 곱하면\n" \
              "$$수식$${eq2}$$/수식$$      ∴ {answ} " \


    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    ine = inequality[random.randint(0, 3)]
    a = random.randint(1, 10)/10
    b = random.randint(1, 10)/10
    c = random.randint(2, 5)
    d = random.randint(1, 15)
    eq = str(a) +"x + " + str(b) + ine + "$$수식$$1 over {"+str(c)+"}$$/수식$$x - " + str(d)
    lcm1 = lcm(10, c)
    a = int(a *lcm1)
    b = int(b*lcm1)
    c = int(lcm1/c)
    d = d*lcm1

    while a-c <=0 or (-d-b)%(a-c)!=0:
        a = random.randint(1, 10) / 10
        b = random.randint(1, 10) / 10
        c = random.randint(2, 5)
        d = random.randint(1, 15)
        eq = str(a) + "x + " + str(b) + ine + "$$수식$$1 over {" + str(c) + "}$$/수식$$x - " + str(d) + "$$수식$$$$/수식$$"
        lcm1 = lcm(10, c)
        a = int(a * lcm1)
        b = int(b * lcm1)
        c = int(lcm1 / c)
        d = d * lcm1

    eq2 = str(a) + "x + " + str(b) + ine + str(c) + "x - " + str(d)
    answ = str(a-c) +"x" + ine + str(-d-b)
    a = int((-d-b)/(a-c))
    answ = "x" + ine + str(a)
    ee = ""
    if ine == " &gt; ":
        ee = " &lt; "
    elif ine ==" &lt; " :
        ee = " &gt; "
    elif ine ==" ≤ ":
        ee =  " ≥ "
    else:
        ee =" ≤ "
    cc=[]
    cc.append("x" + ine + str(-a))
    cc.append("x" + ee + str(a))
    cc.append("x" + ee + str(-a))
    cc.append("x" + ine + str(lcm1))

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = cc[3]
        x3 = cc[0]
        x4 = cc[2]
        x5 = cc[1]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = cc[0]
        x3 = cc[1]
        x4 = cc[2]
        x5 = cc[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = cc[2]
        x2 = cc[1]
        x4 = cc[0]
        x5 = cc[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = cc[1]
        x2 = cc[2]
        x3 = cc[3]
        x5 = cc[0]
    else:
        ans = "⑤"
        x5 = answ
        x1 = cc[3]
        x2 = cc[2]
        x3 = cc[1]
        x4 = cc[0]

    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, answ=answ, lcm1=lcm1)

    return stem, answer, comment

#중2-1-2-35
def expressions212_Stem_032():
    stem = "\nx에 대한 일차부등식 $$수식$${eq}$$/수식$$의 해가\n" \
           "$$수식$${ineq}$$/수식$$일 때, 상수 a의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서 $$수식$${eq2}$$/수식$$\n" \
              "이때 해가 $$수식$${ineq}$$/수식$$이므로 $$수식$${a_ineq}$$/수식$$이다.\n" \
              "즉, $$수식$${x_ineq}$$/수식$$  이므로 $$수식$${ans_eq}$$/수식$$\n" \
              "∴ a = $$수식$${a}$$/수식$$"

    inequality = [" &lt; ", " &gt; ", " ≤ ", " ≥ "]
    ine = inequality[random.randint(0, 3)]
    a = random.randint(1, 15)
    b = random.randint(1, 15)
    c = random.randint(2, 15)
    while (a+b)%c !=0:
        a = random.randint(1, 15)
        b = random.randint(1, 15)
        c = random.randint(2, 15)
    eq = "ax + " + str(a) + ine + str(b*-1) +"$$수식$$$$/수식$$"
    eq2 = "ax" + ine + str(-b-a)+"$$수식$$$$/수식$$"
    ee = ""
    if ine == " &gt; ":
        ee = " &lt; "
    elif ine == " &lt; ":
        ee = " &gt; "
    elif ine == " ≤ ":
        ee = " ≥ "
    else:
        ee = " ≤ "
    ineq = "x" + ee +  str(c)+"$$수식$$$$/수식$$"
    a_ineq = "a" + ee +str(0)+"$$수식$$$$/수식$$"
    x_ineq = "x"+ ee + "-$$수식$${"+str(b+a)+"} over a$$/수식$$"
    ans_eq = "-$$수식$${"+str(b+a)+"} over a$$/수식$$ = " +  str(c) +" , " +"$$수식$$$$/수식$$"
    ans_eq =ans_eq+ str(c) +"a = " + str(-b-a)+"$$수식$$$$/수식$$"
    answ = int((-b-a)/c)
    a = answ

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, ineq=ineq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, ineq=ineq, x_ineq=x_ineq, a_ineq=a_ineq, a=a, ans_eq=ans_eq, eq2=eq2, answ=answ)

    return stem, answer, comment

#중2-1-2-36
def expressions212_Stem_033():
    stem = "\n다음 x에 대한 두 일차부등식의 해가 서로 같을\n" \
           "때, 상수 a의 값은?$$표$$\n" \
           "$$수식$${eq}$$/수식$$, $$수식$${eq2}$$/수식$$ $$/표$$" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "(i) $$수식$${eq1}$$/수식$$에서 $$수식$${ineq1}$$/수식$$\n" \
              "(ii) $$수식$${eq2}$$/수식$$에서\n" \
              "$$수식$${eq3}$$/수식$$,\n" \
              "$$수식$${ineq2}$$/수식$$\n" \
              "(i), (ii)에서 $$수식$${a_eq}$$/수식$$\n" \
              "∴ a = $$수식$${answ}$$/수식$$"

    inequality = [" &lt; ", " &gt;"]
    ine = inequality[random.randint(0, 1)]
    z= 2
    y = 5
    ans11=0
    while (z+ans11)%y!=0:
        a = random.randint(2, 15)
        b = random.randint(1, 15)
        c = random.randint(1, 15)
        while (b-c)%a!=0:
            a = random.randint(2, 15)
            b = random.randint(1, 15)
            c = random.randint(1, 15)
        eq1 = str(a) +"x + "+str(b) +  ine + str(c) + "$$수식$$$$/수식$$"
        ineq1 = str(a)+"x" + ine + str(b-c) + " , x" + ine + str(int((b-c)/a)) + "$$수식$$$$/수식$$"
        ans11 = int((b-c)/a)
        d = random.randint(2, 9)/10
        e = random.randint(2, 9)/10
        f = random.randint(1, 15)
        while ((f*10)%((-d-e)*10))!=0 or (10%((-d-e)*10))!=0:
            d = random.randint(1, 9) / 10
            e = random.randint(1, 9) / 10
            f = random.randint(1, 15)
        inequality = [" &lt; ", " &gt;"]
        ine = inequality[random.randint(0, 1)]
        eq2 = "a - " +str(d) +"x" +ine + str(e) +"x + " + str(f) + "$$수식$$$$/수식$$"
        eq3 = "10a - "+str(int(d*10)) +"x" +ine + str(int(e*10)) +"x + " + str(int(f*10)) +"$$수식$$$$/수식$$"
        ee=""
        if ine == " &gt;":
            ee = " &lt; "
        elif ine == " &lt; ":
            ee = " &gt;"
        elif ine == " ≤ ":
            ee = " ≥ "
        elif ine == " ≥ ":
            ee = " ≤ "
        if int(10/((d+e)*10))!=1:
            ineq2 = str(int((-d-e)*10)) +"x" + ine + str(int(f*10)) + " - 10a"
            ineq2 =ineq2 + ", x" + ee + str(int(10/((d+e)*10))) +"a - " +  str(int((f*10)/((d+e)*10)))  +"$$수식$$$$/수식$$"
            a_eq = str(int(10/((d+e)*10))) +"a - " +  str(int((f*10)/((d+e)*10))) +" = " + str(ans11)+"$$수식$$$$/수식$$"
        else:
            ineq2 = str(int((-d - e) * 10)) + "x" + ine + str(int(f * 10)) + " - 10a"
            ineq2 = ineq2 + ", x" + ee +  "a - " + str(int((f * 10) / ((d + e) * 10))) + "$$수식$$$$/수식$$"
            a_eq =  "a - " + str(int((f * 10) / ((d + e) * 10))) + " = " + str(ans11) + "$$수식$$$$/수식$$"
        z = int((f*10)/((-d-e)*10))
        y = int(10/((d+e)*10))
        a_eq = a_eq + ", " + "a = " + str(int((-z+ans11)/y))

    answ = int((-z+ans11)/y)

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(eq=eq1, eq2=eq2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq1=eq1, eq2=eq2, ineq1=ineq1, ineq2=ineq2, eq3=eq3, a_eq=a_eq, answ=answ)

    return stem, answer, comment




#중2-1-2-37
def expressions212_Stem_034():
    stem = "\nx에 대한 일차부등식 $$수식$${eq}$$/수식$$의 해 중 가장\n" \
           "큰 수가 $$수식$${num}$$/수식$$일 때, 상수 a의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서 $$수식$${eq2}$$/수식$$\n" \
              "∴ x $$수식$${x}$$/수식$$\n" \
              "따라서 $$수식$${fra}$$/수식$$ = $$수식$${num}$$/수식$$이므로 $$수식$${eq4}$$/수식$$\n" \
              "∴ a = $$수식$${a}$$/수식$$"

    inequality = [" &gt; ", " ≥ "]
    ine = inequality[random.randint(0, 1)]

    a = random.randint(1, 15)
    b = random.randint(2, 5)
    eq = str(a) +" - " + str(b) +"x" + ine +"a" + "$$수식$$$$/수식$$"
    num= random.randint(1, 10)
    eq2 = str(-b) +"x" + ine +"a - " + str(a)+ "$$수식$$$$/수식$$"
    ee=""
    if ine == " &gt;":
        ee = " &lt; "
    elif ine == " &lt; ":
        ee = " &gt; "
    elif ine == " ≤ ":
        ee = " ≥ "
    elif ine == " ≥ ":
        ee = " ≤ "
    fra = "$$수식$${"+str(a)+" - a} over {"+str(b)+"}$$/수식$$"
    x = ee + fra
    eq4 = str(a) +" - a = " + str(num*b)+ "$$수식$$$$/수식$$"
    a = (num*b-a)*-1
    answ = a

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(num=num, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(x=x, eq = eq, fra=fra, num=num, a=a, eq2=eq2, eq4=eq4, answ=answ)

    return stem, answer, comment



#중2-1-2-38
def expressions212_Stem_035():
    stem = "\n일차부등식 $$수식$${eq}$$/수식$$의 해를 x {ee} a라 하\n" \
           "고, 일차부등식 $$수식$${eq2}$$/수식$$의 해를\n" \
           "x {ine1} b라 할 때, $$수식$${ab}$$/수식$$의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서 $$수식$${eq11}$$/수식$$\n" \
              "$$수식$${eq12}$$/수식$$\n" \
              "∴ x {ee} $$수식$${x11}$$/수식$$ ∴ a = $$수식$${x11}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$에서 $$수식$${eq21}$$/수식$$\n" \
              "$$수식$${eq22}$$/수식$$\n" \
              "∴ x {ine1} $$수식$${x22}$$/수식$$ ∴ b = $$수식$${x22}$$/수식$$\n" \
              "∴ $$수식$${ab}$$/수식$$ = $$수식$${ab1}$$/수식$$"

    inequality = [" &gt;", " &lt; "]
    ine = inequality[random.randint(0, 1)]
    a = random.randint(2, 15)
    b = random.randint(1, 10)
    c = a* random.randint(2, 5)
    eq = "$$수식$$1 over {"+str(a)+"}$$/수식$$ - $$수식$${x - "+str(b)+"} over {"+str(c)+"}$$/수식$$" + ine +"x" + "$$수식$$$$/수식$$"
    ee=""
    if ine == " &gt;":
        ee = " &lt; "
    elif ine == " &lt; ":
        ee = " &gt; "
    elif ine == " ≤ ":
        ee = " ≥ "
    elif ine == " ≥ ":
        ee = " ≤ "
    lcm1 = lcm(a,c)
    eq11 = str(int(lcm1/a)) +" - (x - "+ str(b)+")" + ine + str(lcm1) +"x" + "$$수식$$$$/수식$$"
    eq12 = str(int(lcm1/a)) +" - x + "+ str(b) + ine + str(lcm1) +"x, " + str(-1-c) +"x" + ine + str(-1*(b + int(lcm1/a)))+ "$$수식$$$$/수식$$"
    top = -1*(b + int(lcm1/a))
    bottom = -1-c
    gcd1 = gcd(abs(top), abs(bottom))
    top = int(top/gcd1)
    bottom = int(bottom/gcd1)
    x11=0
    if top%bottom ==0:
        x11 = int(top/bottom)
    else:
        x11 = "$$수식$${"+str(top*-1)+"} over {"+str(bottom*-1)+"}$$/수식$$"

    inequality = [" &gt; ", " &lt; "]
    ine1 = inequality[random.randint(0, 1)]
    a = random.randint(20, 50)/100
    b = random.randint(1, 10)/10
    c = random.randint(1, 5)/10
    d =random.randint(20, 50)/100
    while a<=c or (d+b)%(a-c)!=0:
        a = random.randint(20, 50) / 100
        b = random.randint(1, 10) / 10
        c = random.randint(1, 5) / 10
        d = random.randint(20, 50) / 100

    eq2 = str(a) +"x - " + str(b) + ine1 +str(c) +"x + " + str(d)+ "$$수식$$$$/수식$$"
    a = int(a*100)
    b = int(b*100)
    c = int(c*100)
    d = int(d*100)
    eq21 = str(a) + "x - " + str(b) + ine1 + str(c) + "x + " + str(d)+ "$$수식$$$$/수식$$"
    eq22 = str(a-c) +"x" +  ine + str(d+b)
    x22 = int((d+b)/(a-c))
    ab = str(bottom) +"a + b" + "$$수식$$$$/수식$$"
    answ = top +  x22
    ab1 = str(bottom) + "$$수식$$TIMES$$/수식$$" +  str(x11) +" + " + str(x22) +" = " +  str(answ) + "$$수식$$$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(ee=ee, ine1=ine1, ab=ab, eq2=eq2, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(ab=ab, ab1=ab1, ee=ee,eq=eq, ine1=ine1, eq12=eq12, eq11=eq11, eq22=eq22, eq21=eq21, x22=x22, x11=x11, eq2=eq2, answ=answ)

    return stem, answer, comment



#중2-1-2-39
def expressions212_Stem_036():
    stem = "다음 중 일차부등식 $$수식$${eq}$$/수식$$\n의" \
           "해인 것은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$$$수식$$``$$/수식$$에서\n" \
              "$$수식$${eq2}$$/수식$$, $$수식$${eq3}$$/수식$$\n" \
              "$$수식$${x_eq}$$/수식$$, $$수식$${x}$$/수식$$\n" \
              "따라서 해인 것은 {ans}이다."\


    inequality = [" ≤ ", " ≥ "]
    mm = random.randint(0,1)
    ine = inequality[mm]
    a1 = 6
    c1 = 6
    d1 = 2
    b1 = 4
    eq=""
    eq2=""
    a = random.randint(2, 6)
    b = random.randint(1, 10)
    c = a*random.randint(2,5)
    d = a*random.randint(2, 5)
    e = random.randint(2, 10)
    f =  random.randint(2, 9)/10
    while (-d1+b1)==0 or (a1-c1)<=0:
        while c%a!=0 or d%a!=0 or b>=c or a/d <f:
            a = random.randint(2, 6)
            b = random.randint(1, 10)
            c = a * random.randint(2, 5)
            d = a * random.randint(2, 5)
            e = random.randint(2, 10)
            f = random.randint(2, 9) / 10
        gcd1 = gcd(b,c)
        b = int(b/gcd1)
        c = int(c/gcd1)
        eq =  str(a) +"($$수식$${"+str(b)+"} over {"+str(c)+"}$$/수식$$x - "
        if c==1:
            str(a) +"(" + str(b) +"x - "
        eq = eq + "$$수식$$1 over {"+str(d)+"}$$/수식$$  )" + ine  +  "$$수식$$1 over {"+str(e)+"}$$/수식$$x - " + str(f)
        c = c/a
        d = d/a
        gcd1 = gcd(b, c)
        b = int(b / gcd1)
        c = int(c / gcd1)
        lcm1 = lcm(lcm(c, e), d) * 10
        eq2 = "$$수식$${"+str(b)+"} over {"+str(int(c))+"}$$/수식$$x - $$수식$$1 over {"+str(int(d))+"}$$/수식$$" + ine  +  "$$수식$$1 over {"+str(e)+"}$$/수식$$x - $$수식$${"+str(int(f*10))+"} over 10$$/수식$$ $$수식$$$$/수식$$"

        if c==1:
            eq2 = str(b) +"x - $$수식$$1 over {"+str(int(d))+"}$$/수식$$" + ine  +  "$$수식$$1 over {"+str(e)+"}$$/수식$$x - $$수식$${"+str(int(f*10))+"} over 10$$/수식$$ $$수식$$$$/수식$$"
            if b==1:
                eq2 = "x - $$수식$$1 over {"+str(int(d))+"}$$/수식$$" + ine  +  "$$수식$$1 over {"+str(e)+"}$$/수식$$x - $$수식$${"+str(int(f*10))+"} over 10$$/수식$$ $$수식$$$$/수식$$"
        a1 = int(b*(lcm1/c))
        b1 = int(lcm1/d)
        c1 = int(lcm1/e)
        d1 = int(lcm1*f)
    eq3 = str(a1) +"x - " + str(b1) + ine + str(c1)+"x - " + str(d1) + "$$수식$$$$/수식$$"

    x_eq = str(a1-c1) +"x" + ine + str(-d1+b1)+ "$$수식$$$$/수식$$"
    answ = (-d1+b1)/(a1-c1)
    x = "x" + ine + str(int(answ))
    gcd2 = gcd(abs(-d1+b1),abs(a1-c1))
    top = int((-d1+b1)/gcd2)
    bot = int((a1-c1)/gcd2)
    if (-d1+b1)%(a1-c1) !=0:
        x = "x" + ine + "$$수식$${"+str(top)+"} over {"+str(bot)+"}$$/수식$$"
    while bot>50:
        mm = random.randint(0, 1)
        ine = inequality[mm]
        a1 = 6
        c1 = 6
        d1 = 2
        b1 = 4
        eq = ""
        eq2 = ""
        a = random.randint(2, 6)
        b = random.randint(1, 10)
        c = a * random.randint(2, 5)
        d = a * random.randint(2, 5)
        e = random.randint(2, 10)
        f = random.randint(2, 9) / 10
        while (-d1 + b1) == 0 or (a1 - c1) <= 0:
            while c % a != 0 or d % a != 0 or b >= c or a / d < f:
                a = random.randint(2, 6)
                b = random.randint(1, 10)
                c = a * random.randint(2, 5)
                d = a * random.randint(2, 5)
                e = random.randint(2, 10)
                f = random.randint(2, 9) / 10

            gcd1 = gcd(b, c)
            b = int(b / gcd1)
            c = int(c / gcd1)
            eq = str(a) + "($$수식$${" + str(b) + "} over {" + str(c) + "}$$/수식$$x - "
            if c == 1:
                str(a) + "(" + str(b) + "x - "
            eq = eq + "$$수식$$1 over {" + str(d) + "}$$/수식$$  )" + ine + "$$수식$$1 over {" + str(
                e) + "}$$/수식$$x - " + str(f)
            c = c / a
            d = d / a
            gcd1 = gcd(b, c)
            b = int(b / gcd1)
            c = int(c / gcd1)
            lcm1 = lcm(lcm(c, e), d) * 10
            eq2 = "$$수식$${" + str(b) + "} over {" + str(int(c)) + "}$$/수식$$x - $$수식$$1 over {" + str(
                int(d)) + "}$$/수식$$" + ine + "$$수식$$1 over {" + str(e) + "}$$/수식$$x - $$수식$${" + str(
                int(f * 10)) + "} over 10$$/수식$$ $$수식$$$$/수식$$"
            if c == 1:
                eq2 = str(b) + "x - $$수식$$1 over {" + str(int(d)) + "}$$/수식$$" + ine + "$$수식$$1 over {" + str(
                    e) + "}$$/수식$$x - $$수식$${" + str(int(f * 10)) + "} over 10$$/수식$$ $$수식$$$$/수식$$"
                if b == 1:
                    eq2 = "x - $$수식$$1 over {" + str(int(d)) + "}$$/수식$$" + ine + "$$수식$$1 over {" + str(
                        e) + "}$$/수식$$x - $$수식$${" + str(int(f * 10)) + "} over 10$$/수식$$ $$수식$$$$/수식$$"
            a1 = int(b * (lcm1 / c))
            b1 = int(lcm1 / d)
            c1 = int(lcm1 / e)
            d1 = int(lcm1 * f)

        eq3 = str(a1) + "x - " + str(b1) + ine + str(c1) + "x - " + str(d1) + "$$수식$$$$/수식$$"

        x_eq = str(a1 - c1) + "x" + ine + str(-d1 + b1) + "$$수식$$$$/수식$$"
        answ = (-d1 + b1) / (a1 - c1)
        x = "x" + ine + str(int(answ))
        gcd2 = gcd(abs(-d1 + b1), abs(a1 - c1))
        top = int((-d1 + b1) / gcd2)
        bot = int((a1 - c1) / gcd2)
        if (-d1 + b1) % (a1 - c1) != 0:
            x = "x" + ine + "$$수식$${" + str(top) + "} over {" + str(bot) + "}$$/수식$$"

    bb=[]
    dd=[]
    while len(bb)<4:
        if mm==0:
            y = (-d1+b1) + random.randint(2, 50)
            z = a1 - c1
            s = y / z
            if s not in dd  and abs(s) > answ:
                dd.append(s)
                gcd0 = gcd(abs(y),abs(z))
                y = int(y/gcd0)
                z = int(z/gcd0)
                if z==1:
                    bb.append(str(y))
                else:
                    bb.append("$$수식$${" + str(y) + "} over {" + str(z) + "}$$/수식$$" + "$$수식$$$$/수식$$")
        elif mm==1:
            y = (-d1+b1) - random.randint(2, 50)
            while y==0:
                y = (-d1+b1) - random.randint(2, 50)
            z = (a1 - c1)
            s = y / z

            if s not in dd and s < answ:
                dd.append(s)
                gcd0 = gcd(abs(y), abs(z))
                y = int(y / gcd0)
                z = int(z / gcd0)
                if z == 1:
                    bb.append(str(y))
                elif y<0:
                    bb.append("-$$수식$${" + str(abs(y)) + "} over {" + str(z) + "}$$/수식$$" + "$$수식$$$$/수식$$")
                else:
                    bb.append("$$수식$${" + str(y) + "} over {" + str(z) + "}$$/수식$$" + "$$수식$$$$/수식$$")
    if ine == " ≤ " and top!=1:
        gcd1 = gcd(abs(top-1), abs(bot))
        top = int((top-1)/gcd1)
        bot = int(bot/gcd1)
        answ ="$$수식$${"+str(top)+"} over {"+str(bot)+"}$$/수식$$" + "$$수식$$$$/수식$$"
        if bot==1:
            answ = str(top)
    elif ine == " ≤ " and top==1:
        gcd1 = gcd(abs(top), abs(bot+1))
        top = int((top) / gcd1)
        bot = int((bot+1) / gcd1)
        answ = "$$수식$${" + str(top) + "} over {" + str(bot+1) + "}$$/수식$$" + "$$수식$$$$/수식$$"
    if ine == " ≥ ":
        gcd1 = gcd(abs(top+1), abs(bot))
        top = int((top+1)/gcd1)
        bot = int(bot/gcd1)
        answ = "$$수식$${" + str(top) + "} over {" + str(bot) + "}$$/수식$$"+ "$$수식$$$$/수식$$"
        if bot==1:
            answ = str(top)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, x_eq=x_eq, x=x, eq3=eq3, ans=ans)

    return stem, answer, comment

#중2-1-2-40
def expressions212_Stem_037():
    stem = "\n두 상수 a, b에 대하여 a {ine1} b일 때, x에 대한\n" \
           "일차부등식 $$수식$${eq}$$/수식$$의 해는?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서\n" \
              "$$수식$${eq1}$$/수식$$, $$수식$${eq2}$$/수식$$\n" \
              "이 때, a {ine1} b에서 a - b {ine1} 0이므로 $$수식$${x}$$/수식$$\n" \
              "∴ {answ}" \

    inequality = [" ≤ ", " ≥ "]
    inequality1 = [" &gt; ", " &lt; "]
    m=np.random.randint(0,2)
    ine = inequality[m]
    a = random.randint(2, 10)
    eq ="ax - " + str(a) +"a" + ine +"bx - " + str(a) +"b" +"$$수식$$$$/수식$$"
    eq1 = "ax - bx" + ine + str(a) +"a - " + str(a) +"b"+"$$수식$$$$/수식$$"
    eq2 = "(a - b)x" + ine + str(a) +"(a - b)" +"$$수식$$$$/수식$$"


    mm = np.random.randint(0,2)
    ine1 = inequality1[mm]
    x=""
    answ=""
    temp=""

    if mm==0:
        if m == 0:
            temp = " ≥ "
        else:
            temp = " ≤ "
        x = "x" +  ine +"$$수식$${"+str(a)+"(a - b)} over {(a - b)}$$/수식$$"+"$$수식$$$$/수식$$"
        answ = "x" + ine + str(a)
    else:
        if m==0:
            temp =" ≥ "
            x = "x" + " ≥ " + "$$수식$${"+str(a)+"(a - b)} over {(a - b)}$$/수식$$"+"$$수식$$$$/수식$$"
            answ = "x" + temp + str(a)
        else:
            temp = " ≤ "
            x = "x" + " ≤ " + "$$수식$${"+str(a)+"(a - b)} over {(a - b)}$$/수식$$"+"$$수식$$$$/수식$$"
            answ = "x" + temp + str(a)


    bb=[]
    bb.append( "x" + temp + str(-a)+"$$수식$$$$/수식$$")
    bb.append("x" + temp + str(0)+"$$수식$$$$/수식$$")
    bb.append( "x" + ine + str(0)+"$$수식$$$$/수식$$")
    bb.append( "x" + ine + str(-a)+"$$수식$$$$/수식$$")

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(ine1=ine1, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq1=eq1, eq=eq, ine1=ine1,  eq2=eq2,  x=x,  answ=answ)

    return stem, answer, comment



#중2-1-2-41
def expressions212_Stem_038():
    stem = "\na {ine} $$수식$${num}$$/수식$$일 때, x에 대한 일차부등식\n" \
           "$$수식$${eq}$$/수식$$$$수식$$``$$/수식$${temp}$$수식$$``$$/수식$$ 만족시키는 가장 큰 정수 x\n" \
           "의 값은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서\n" \
              "$$수식$${eq1}$$/수식$$, $$수식$${eq2}$$/수식$$\n" \
              "a {ine} $$수식$${num}$$/수식$$에서 $$수식$${a_eq}$$/수식$$이므로 $$수식$${x}$$/수식$$\n" \
              "따라서 주어진 부등식을 만족시키는 가장 큰 정수\n" \
              "x의 값은 $$수식$${answ}$$/수식$$이다."

    inequality = [" &gt; ", " &lt; "]
    con = np.random.randint(0,2)
    ine = inequality[con]
    ine1=""
    if con==0:
        ine1 = " &lt; "
    elif con==1:
        ine1 =" &gt; "
    num = np.random.randint(2,10)
    mul  = np.random.randint(2,5)
    a = num*mul
    eq = "ax - " +str(mul)+"a" + ine1 + str(num) +"(x - "+str(mul)+")" + "$$수식$$$$/수식$$"
    eq1 = "ax -"+str(mul)+" a" + ine1 + str(num) +"x - " +  str(a)  + "$$수식$$$$/수식$$"
    eq2 = "(a - "+str(num) +")x" + ine1 + str(mul)  +"a - "+ str(a)+ "$$수식$$$$/수식$$"
    a_eq = "a - " + str(num) + ine +str(0)+ "$$수식$$$$/수식$$"

    x = "x &lt; " + str(mul)
    answ =mul-1
    temp = proc_jo(mul, 4)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(num=num, ine=ine, temp=temp, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, a_eq=a_eq, ine=ine, eq1=eq1, eq=eq, ine1=ine1, eq2=eq2, x=x, answ=answ)

    return stem, answer, comment

#중2-1-2-42
def expressions212_Stem_039():
    stem = "\na {ine1} 0 {ine1} b일 때, x에 대한 일차부등식\n" \
           "$$수식$${eq}$$/수식$$를 풀면?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서 $$수식$${eq2}$$/수식$$\n" \
              "a {ine1} 0 {ine1} b에서 a - 2b {ine1} 0이므로\n" \
              "$$수식$${x}$$/수식$$     ∴$$수식$${answ}$$/수식$$"



    inequality = [" &gt; ", " &lt; "]
    con = np.random.randint(0,2)
    ine = inequality[con]

    a = np.random.randint(1, 6)
    c = a*2
    d = np.random.randint(2, 6)
    b = d*2
    while a==d or d%a !=0 or a>d:
        a = np.random.randint(1, 6)
        c = a * 2
        d = np.random.randint(2, 6)
        b = d * 2
    eq = "ax + " + str(b) + "b" + ine + str(c) +"bx + " +  str(d) +"a" +"$$수식$$$$/수식$$"
    eq2 = "(a - 2b)x" + ine + str(d)+ "(a - 2b)"+"$$수식$$$$/수식$$"
    if a!=1:
        eq = str(a) + "ax + " + str(b) + "b" + ine + str(c) + "bx + " + str(d) + "a"+"$$수식$$$$/수식$$"
        eq2 = str(a) + "(a - 2b)x" + ine + str(d)+ "(a - 2b)"+"$$수식$$$$/수식$$"

    ab = np.random.randint(0,2)
    ine1 = inequality[ab]
    temp=""
    x=""
    answ=""
    ans11 = int(d/a)
    if con==1 and ab==1:
        temp = " &lt; "
        ine111 = " &gt; "
        x = "x &gt; $$수식$${"+str(d)+"(a - b)} over {"+str(a)+"(a - b)}$$/수식$$"
        if a==1:
            x = "x &gt; $$수식$${"+str(d)+"(a - b)} over {(a - b)}$$/수식$$"
        answ ="x &gt; " + str(ans11)
    elif con==0 and ab==1:
        temp = " &gt; "
        ine111 = " &lt; "
        x = "x &lt; $$수식$${" + str(d) + "(a - b)} over {" + str(a) + "(a - b)}$$/수식$$"
        if a == 1:
            x = "x &lt; $$수식$${" + str(d) + "(a - b)} over {(a - b)}$$/수식$$"
        answ = "x &lt; " + str(ans11)
    else:
        temp = inequality[con-1]
        ine111 = ine
        x= "x" + ine111 +"$$수식$${" + str(d) + "(a - b)} over {" + str(a) + "(a - b)}$$/수식$$"
        if a==1:
           x= "x" + ine111 + "$$수식$${" + str(d) + "(a - b)} over {(a - b)}$$/수식$$"
        answ = answ ="x " + ine + str(ans11)

    bb=[]
    bb.append("x" +ine111 + str(-ans11))
    bb.append("x" + temp + str(ans11))
    bb.append("x" + temp + str(-ans11))
    bb.append("x" +ine111 + str(0))

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(ine1=ine1, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, ine1=ine1, eq2=eq2, x=x, answ=answ)

    return stem, answer, comment

#중2-1-2-43
def expressions212_Stem_040():
    stem = "\nx에 대한 일차부등식 $$수식$${eq}$$/수식$$의 해가\n" \
           "$$수식$${ineq}$$/수식$$일 때, 상수 a의 값은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서\n" \
              "$$수식$${eq1}$$/수식$$, $$수식$${eq2}$$/수식$$\n" \
              "$$수식$${x_eq}$$/수식$$, 즉 $$수식$${comb}$$/수식$$이므로\n" \
              "$$수식$${v}$$/수식$$     ∴ $$수식$${answ}$$/수식$$"

    inequality = [" &gt; ", " &lt; "]
    con = np.random.randint(0, 2)
    ine = inequality[con]

    a = np.random.randint(2, 15)
    b = np.random.randint(2, 15)
    c = np.random.randint(2, 15)
    while a<=b:
        a = np.random.randint(2, 15)
        b = np.random.randint(2, 15)
        c = np.random.randint(2, 15)
    num1 = np.random.randint(0, 10)

    eq= str(a) +"x + a" + ine +str(b)+"(x + " + str(c) +")" +"$$수식$$$$/수식$$"
    ineq= "x" + ine + str(num1) +"$$수식$$$$/수식$$"
    eq1 = str(a) +"x + a" + ine +str(b)+"x + " + str(c*b) +"$$수식$$$$/수식$$"
    eq2 = str(a-b) +"x" + ine + str(c*b) + " - a" +"$$수식$$$$/수식$$"  +"$$수식$$$$/수식$$"
    x_eq = "x" + ine+ "$$수식$${"+str(c*b)+" - a} over {"+str(a-b)+"}$$/수식$$"  +"$$수식$$$$/수식$$"
    comb = "$$수식$${"+str(c*b)+" - a} over {"+str(a-b)+"}$$/수식$$   = " + str(num1) +"$$수식$$$$/수식$$"
    v = str(c*b)+" - a = " + str(num1*(a-b))
    f = num1*(a-b)
    g = c*b
    answ = g-f

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(ineq=ineq, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq2=eq2, eq=eq, eq1=eq1, x_eq=x_eq, v=v, comb=comb,  answ=answ)

    return stem, answer, comment



#중2-1-2-44
def expressions212_Stem_041():
    stem = "\nx에 대한 일차부등식 $$수식$${eq}$$/수식$$의 해가\n" \
           "$$수식$${ineq}$$/수식$$일 때, 상수 a의 값은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서 $$수식$${eq2}$$/수식$$\n" \
              "이 부등식의 해가 $$수식$${ineq}$$/수식$$  이므로 $$수식$${ineq2}$$/수식$$\n" \
              "따라서 $$수식$${x_eq}$$/수식$$    이므로 $$수식$${comb}$$/수식$$\n" \
              "$$수식$${v}$$/수식$$          ∴ a = $$수식$${answ}$$/수식$$"

    inequality = [" ≤ ", " ≥ "]
    con = 1
    ine = inequality[con]

    a = np.random.randint(2, 15)
    b = np.random.randint(2, 15)
    c = np.random.randint(2, 15)
    d = np.random.randint(2, 15)
    num1 = np.random.randint(1, 10)
    while (d-b+c*num1)==0 or (d-b+c*num1)%(a*num1)!=0 or b==d or (d-b)%num1!=0:
        a = np.random.randint(2, 15)
        b = np.random.randint(2, 15)
        c = np.random.randint(2, 15)
        d = np.random.randint(2, 15)
        num1 = np.random.randint(1, 10)

    eq = str(a) +"ax + " + str(b) + ine + str(c) + "x + " + str(d)+"$$수식$$$$/수식$$"
    eq2 ="("+ str(a) +"a - " + str(c) +")x" + ine + str(d-b)+"$$수식$$$$/수식$$"

    ineq = "x" + ine + str(num1)+"$$수식$$$$/수식$$"
    ineq2=""
    if con==1:
        ineq2 = str(a) +"a - " + str(c) + " &gt; " + str(int((d-b)/num1))+"$$수식$$$$/수식$$"
    else:
        ineq2 = str(a) + "a - " + str(c) + " &lt; " + str(int((d-b)/num1))+"$$수식$$$$/수식$$"
        ine = inequality[con-1]

    x_eq = "x" + ine +"$$수식$${"+str(d-b)+"} over {"+str(a)+"a - "+str(c)+"}$$/수식$$"+ "$$수식$$$$/수식$$"
    comb = "$$수식$${"+str(d-b)+"} over {"+str(a)+"a - "+str(c)+"}$$/수식$$      $$수식$$`=`$$/수식$$" + str(num1)+ "$$수식$$$$/수식$$"
    if d-b<0:
        x_eq = "x" + ine + "- $$수식$${" + str((d - b)*-1) + "} over {" + str(a) + "a - " + str(c) + "}$$/수식$$" + "$$수식$$$$/수식$$"
        comb = "- $$수식$${" + str((d - b)*-1) + "} over {" + str(a) + "a - " + str(c) + "}$$/수식$$      $$수식$$`=`$$/수식$$" + str(num1) + "$$수식$$$$/수식$$"

    v = str(a*num1)+"a - "+str(c*num1)+ " = " + str(d-b)+" $$수식$$`, `$$/수식$$ "
    v= v + str(a*num1)+"a = " + str(d-b+c*num1)+"$$수식$$$$/수식$$"
    answ = int((d-b+c*num1)/(a*num1))

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(ineq=ineq, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq2=eq2, eq=eq, ineq2=ineq2,ineq=ineq, x_eq=x_eq, v=v, comb=comb, answ=answ)

    return stem, answer, comment


#중2-1-2-45
def expressions212_Stem_042():
    stem = "\nx에 대한 일차부등식 $$수식$${eq}$$/수식$$,\n" \
           "$$수식$${eq2}$$/수식$$의 해가 서로 같을 때, 상수 a의 \n값은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서 $$수식$${eq11}$$/수식$$\n" \
              "∴ $$수식$${x11}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$에서 $$수식$${eq22}$$/수식$$\n" \
              "∴ $$수식$${x22}$$/수식$$\n" \
              "따라서 $$수식$${comb}$$/수식$$이므로 $$수식$${a}$$/수식$$\n" \
              "∴ a = $$수식$${answ}$$/수식$$"

    inequality = [" &gt; ", " &lt; "]
    con = np.random.randint(0, 2)
    ine = inequality[con]

    a = np.random.randint(2, 15)
    b = np.random.randint(1, 15)
    c = np.random.randint(2, 15)
    d = np.random.randint(1, 15)
    while a==c or (-d-b)%(a-c)!=0:
        a = np.random.randint(2, 15)
        b = np.random.randint(1, 15)
        c = np.random.randint(2, 15)
        d = np.random.randint(1, 15)
    eq = str(a) +"x + " + str(b) +  ine +  str(c) +"x - " +  str(d) +"$$수식$$$$/수식$$"
    eq11 =  str(a-c) +"x" +  ine + str(-d-b)+"$$수식$$$$/수식$$"
    if a-c==1:
        eq11 = "x" + ine + str(-d - b)+"$$수식$$$$/수식$$"
    elif a-c ==-1:
        eq11 = "-x" + ine + str(-d - b) + "$$수식$$$$/수식$$"
    if a-c<0:
        ine = inequality[con-1]
    x11 = "x" + ine + str(int((-d-b)/(a-c)))+"$$수식$$$$/수식$$"
    ans11 = int((-d-b)/(a-c))

    a = np.random.randint(2, 15)
    b = np.random.randint(1, 15)
    c = np.random.randint(2, 15)
    while a<=c:
        a = np.random.randint(2, 15)
        c = np.random.randint(2, 15)

    eq2 = str(a) +"x - a" + ine +str(b) + " - " + str(c) + "x"+"$$수식$$$$/수식$$"
    eq22 = str(a+c) +"x" + ine +"a + " + str(b)+"$$수식$$$$/수식$$"
    x22 = "x" + ine + "$$수식$${a + "+str(b)+"} over {"+str(a+c)+"}$$/수식$$"
    comb = "$$수식$${a + "+str(b)+"} over {"+str(a+c)+"}$$/수식$$    = " + str(ans11)+"$$수식$$$$/수식$$"
    h = "a + " + str(b) + " = " + str((a+c)*ans11)
    answ = (a+c)*ans11 -b

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(eq2=eq2, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq2=eq2, eq=eq, a=h, eq11=eq11, x11=x11, x22=x22, eq22=eq22, comb=comb, answ=answ)

    return stem, answer, comment



#중2-1-2-46
def expressions212_Stem_043():
    stem = "\n일차부등식 $$수식$${eq}$$/수식$$$$수식$$``$$/수식$${temp}$$수식$$``$$/수식$$ 만족시키는 x의 값 중\n" \
           "가장 큰 값이 $$수식$${num}$$/수식$$일 때, 상수 a의 값은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서 $$수식$${eq2}$$/수식$$\n" \
              "이 부등식의 해가 x {ineq11} $$수식$${num12}$$/수식$$이어야 하므로\n" \
              "$$수식$${a_eq}$$/수식$$\n" \
              "따라서 {x_eq} 이므로 {a_eq1}\n" \
              "∴ a = $$수식$${answ}$$/수식$$"
    ee1 = ["작은", "큰"]
    ineq1 = [" ≤ ", " ≥ "]
    con = 1

    ee = "$$수식$$``$$/수식$$"+ee1[con] + "$$수식$$``$$/수식$$"
    ineq11 = " ≤ "

    ran = " ≤ "
    ine = " ≥ "


    a = np.random.randint(2, 15)
    b = np.random.randint(2, 15)
    num = (b-a) * -1
    while b-a<=0:
        a = np.random.randint(2, 15)
        b = np.random.randint(2, 15)
        num = (b-a) * -1 * np.random.randint(1, 7)
    temp = proc_jo(b, 4)
    eq=""
    eq2=""
    a_eq=""
    num12= int(num/(a-b))
    if con ==1:
        eq = str(a) + " - ax" + ine + str(b)+"$$수식$$$$/수식$$"
        eq2 = " - ax" + ine + str(b-a)+"$$수식$$$$/수식$$"
        a_eq = "- a &lt; " + str(0) +"$$수식$$$$/수식$$"
        num12 = num
    else:
        eq = str(a) + " + ax" + ine + str(b)+"$$수식$$$$/수식$$"
        eq2 = "ax" + ine + str(b - a)+"$$수식$$$$/수식$$"
        a_eq = "a &lt; " + str(0)+"$$수식$$$$/수식$$"

    x_eq =""
    a_eq1 =""
    a_eq1 = ""
    answ = int(num/(a-b))
    if con ==1:
        x_eq = "x" + ineq11 + "$$수식$${"+str(a-b)+"} over a$$/수식$$"
        a_eq1 = "$$수식$${"+str(a-b)+"} over a$$/수식$$ = "
        a_eq1 = a_eq1 + str(num) + "$$수식$$$$/수식$$"
        answ = int(num/(a-b))
    elif b-a<0 and con==0:
        x_eq = "x" + ine + " - {" + str(a - b) + "} over a"
        a_eq1 = " -$$수식$${" + str(a - b) + "} over a$$/수식$$ = "
        a_eq1 = a_eq1 + str(num) + "$$수식$$$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(temp=temp, ee=ee, num=num, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, ineq11=ineq11, num=num,num12=num12, eq2=eq2, a_eq=a_eq,a_eq1=a_eq1, x_eq=x_eq, answ=answ)

    return stem, answer, comment



#중2-1-2-49
def expressions212_Stem_044():
    stem = "\nx = $$수식$${num}$$/수식$$$$수식$$``$$/수식$${temp}$$수식$$``$$/수식$$ x에 대한 일차부등식\n" \
           "$$수식$${eq1}$$/수식$$$$수식$$``$$/수식$${ine}$$수식$$``$$/수식$$$$수식$${eq2}$$/수식$$$$수식$$``$$/수식$$의 해가 아닐 때, 상수\n" \
           "a의 값의 범위는?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "x = $$수식$${num}$$/수식$$$$수식$$``$$/수식$${temp}$$수식$$``$$/수식$$$$수식$${eq1}$$/수식$$$$수식$$``$$/수식$${ine1}$$수식$$``$$/수식$$$$수식$${eq2}$$/수식$$$$수식$$``$$/수식$$의 해이므\n" \
              "로\n" \
              "$$수식$${eq3}$$/수식$$, $$수식$${eq4}$$/수식$$\n" \
              "$$수식$${a_eq}$$/수식$$    ∴$$수식$${answ}$$/수식$$"

    ineq1 = [" ≤ ", " ≥ "]
    inequality = [" &gt; ", " &lt; "]
    con = np.random.randint(0, 2)
    ine1 =""
    if con==0:
        ine1 = " ≤ "
    else:
        ine1 = " ≥ "
    ine = inequality[con]
    pp=1
    oo=1
    d=1
    num=1
    a=lcm1=e=0
    eq1=""
    eq2=""
    eq3=""
    b=1
    aaaa=101
    bbbb = 101
    while pp>=(d*num*oo) or bbbb>100:
        num = np.random.randint(1, 4)*-1
        a = np.random.randint(1, 5)
        b = np.random.randint(1, 8)
        c = np.random.randint(2, 8)
        d = np.random.randint(2, 8)
        e = np.random.randint(1, 8)
        f = c*np.random.randint(2, 5)
        while b+num==0 or c==1:
            num = np.random.randint(1, 4) * -1
            b = np.random.randint(1, 10)
        eq1 = str(a) +"x - " + "$$수식$${a(x + "+str(b)+")} over {"+str(c)+"}$$/수식$$"
        eq2 = "$$수식$${"+str(d)+"ax + "+str(e)+"} over {"+str(f)+"}$$/수식$$"
        gcd1 = gcd(abs(num+b), c)
        gg = int((num+b)/gcd1)
        c = int(c/gcd1)
        eq3 = str(a*num) + " - $$수식$${"+str(gg)+"a} over {"+str(c)+"}$$/수식$$"+"  $$수식$$$$/수식$$"
        if gg==1:
            eq3 = str(a * num) + " - $$수식$$a over {" + str(c) + "}$$/수식$$" + "  $$수식$$$$/수식$$"
        elif gg==-1:
            eq3 = str(a * num) + " - $$수식$$-a over {" + str(c) + "}$$/수식$$" + "  $$수식$$$$/수식$$"
        if d*num==1:
            eq3 = eq3 + ine1 + "$$수식$${a + " + str(e) + "} over {" + str(f) + "}$$/수식$$" + "   $$수식$$`, `$$/수식$$  "
        else:
            eq3 = eq3 + ine1 + "$$수식$${" + str(d * num) + "a + " + str(e) + "} over {" + str(f) + "}$$/수식$$" + "    $$수식$$`, `$$/수식$$  "

        lcm1 = lcm(abs(c),abs(f))
        pp = int(gg*lcm1/c)
        oo = int(lcm1/f)
        aaaa = pp * -1 - d * num * oo
        bbbb = e * oo - a * num * lcm1
    temp = proc_jo(num,0)
    eq4 = str(a*num*lcm1) +" + " + str(pp*-1) +"a" + ine1  +  str(d*num*oo) + "a + " + str(e*oo) +"$$수식$$$$/수식$$"
    aaaa = pp*-1 - d*num*oo
    bbbb = e*oo - a*num*lcm1
    a_eq = str(aaaa) +"a" + ine1 + str(bbbb)+"$$수식$$$$/수식$$"
    answ=""
    if bbbb%aaaa==0:
        answ = "a" + ine1 + str(int(bbbb/aaaa))+"$$수식$$$$/수식$$"
    else:
        gcd2 = gcd(abs(bbbb), abs(aaaa))
        bbbb = int(bbbb/gcd2)
        aaaa = int(aaaa/gcd2)
        answ = "a" + ine1 + "$$수식$${"+str(bbbb)+"} over {"+str(aaaa)+"}$$/수식$$"

    dd=[bbbb/aaaa]
    bb=[]
    while len(bb)<4:
        tem1 = np.random.randint(1, 200)
        tem2 = np.random.randint(2, 40)
        if tem1/tem2 not in dd:
            dd.append(tem1/tem2)
            gcd_t = gcd(tem1, tem2)
            tem1 = int(tem1/gcd_t)
            tem2 = int (tem2/gcd_t)
            if tem1<100 and tem2<100:
                if tem2!=1:
                    bb.append("a" + ine1 + "$$수식$${"+str(tem1)+"} over {"+str(tem2)+"}$$/수식$$")
                else:
                    bb.append("a" + ine1 + str(tem1))



    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(temp=temp, eq1=eq1, ine=ine, eq2=eq2, num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(ine1=ine1, num=num, eq1=eq1, eq2=eq2, ine=ine, eq3=eq3, a_eq=a_eq, eq4=eq4, temp=temp, answ=answ)

    return stem, answer, comment



#중2-1-2-50
def expressions212_Stem_045():
    stem = "\nm◎n = $$수식$${num1}$$/수식$$m - $$수식$${num2}$$/수식$$n이라 할 때, x의 대한 일차부등\n" \
           "식 $$수식$${eq}$$/수식$$$$수식$$``$$/수식$${temp}$$수식$$``$$/수식$$만족시키는 x의 값\n" \
           "중 가장 큰 값이 $$수식$${ans11}$$/수식$$이다. 이 때 상수 a의 값을\n" \
           "구하시오."
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서 \n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$,\n" \
              "$$수식$${x_eq}$$/수식$$\n" \
              "∴$$수식$${x}$$/수식$$\n" \
              "따라서 $$수식$${comb}$$/수식$$이므로\n" \
              "$$수식$${a_eq}$$/수식$$, $$수식$${aa}$$/수식$$\n" \
              "∴ a = $$수식$${ans}$$/수식$$"

    num1 = np.random.randint(2, 5)
    num2 = np.random.randint(2, 5)
    ans11 = np.random.randint(0, 5)*-1
    while num1==num2:
        num2 = np.random.randint(2, 5)

    inequality = [" ≤ ", " ≥ "]
    con = np.random.randint(0, 2)
    ine1 =""
    ine = inequality[con]
    a = np.random.randint(1, 15)
    b = np.random.randint(2, 15)
    c = np.random.randint(2, 15)
    if con==1:
        while num1==num2 or num1>=(num2*b)  or ((num1 - b * num2)*ans11 - (c+a * num1))%num2!=0:
            num1 = np.random.randint(2, 6)
            num2 = np.random.randint(2,6)
            ans11 = np.random.randint(0, 5) * -1
            a = np.random.randint(1, 15)
            b = np.random.randint(2, 15)
            c = np.random.randint(2, 15)
            if con == 0:
                ine1 = " ≥ "
            else:
                ine1 = " ≤ "
    else:
        while num1==num2 or num1<=(num2*b)  or ((num1 - b * num2)*ans11 - (c+a * num1))%num2!=0:
            num1 = np.random.randint(2, 6)
            num2 = np.random.randint(2, 6)
            ans11 = np.random.randint(0, 5) * -1
            a = np.random.randint(1, 15)
            b = np.random.randint(2, 15)
            c = np.random.randint(2, 15)
            ine1 = ine
    eq= "(x - " + str(a) +")◎("+str(b) +"x + a)" + ine + str(c) + "$$수식$$$$/수식$$"

    eq2 = str(num1) + "(x - " + str(a) +")- " + str(num2)+"("+str(b) +"x + a)" + ine + str(c) + "$$수식$$$$/수식$$"
    eq3 = str(num1) + "x - " + str(a*num1) +" - "+str(b*num2) +"x - " + str(num2) +"a" + ine + str(c) + "$$수식$$$$/수식$$"
    x_eq = str(num1-b*num2) +"x" + ine +str(num2) +"a + " + str(c+a*num1) + "$$수식$$$$/수식$$"

    x = "x"  + ine1
    comb=""
    if num1-b*num2<0:
        x = x + "- $$수식$${"+str(num2) +"a + " + str(c+a*num1) +"} over {"+str(-1*(num1-b*num2))+"}$$/수식$$"
        comb = "- $$수식$${"+str(num2) +"a + " + str(c+a*num1) +"} over {"+str(-1*(num1-b*num2))+"}$$/수식$$   = " +  str(ans11) +"$$수식$$$$/수식$$"
    elif num1-b*num2>0:
        x = x + "$$수식$${" + str(num2) + "a + " + str(c+a*num1) + "} over {" + str((num1 - b * num2)) + "}$$/수식$$"+ "$$수식$$$$/수식$$"
        comb = "$$수식$${" + str(num2) + "a + " + str(c+a*num1) + "} over {" + str((num1 - b * num2)) + "}$$/수식$$   = " + str(ans11) + "$$수식$$$$/수식$$"

    if num1-b*num2==1:
        x_eq = "x" + ine + str(num2) + "a + " + str(c+a*num1) + "$$수식$$$$/수식$$"
        x = "x"  + ine1  + str(num2) + "a + " + str(c+a*num1)  + "$$수식$$$$/수식$$"
        comb =  str(num2) + "a + " + str(c+a*num1)  + "$$수식$$$$/수식$$   = " + str(ans11*((num1-b*num2))) + "$$수식$$$$/수식$$"
    elif num1-b*num2==-1:
        x_eq = "- x" + ine + str(num2) + "a + " + str(c+a*num1) + "$$수식$$$$/수식$$"
        x = "x" + ine1 + " -" + str(num2) + "a - " + str(c+a*num1) + "$$수식$$$$/수식$$"
        comb = "-" + str(num2) + "a - " + str(c+a*num1) + "$$수식$$$$/수식$$   = " + str(ans11*((num1-b*num2))) + "$$수식$$$$/수식$$"

    a_eq =str(num2) + "a + " + str(c+a*num1) + " = " + str((num1 - b * num2)*ans11) + "$$수식$$$$/수식$$"
    w = (num1 - b * num2)*ans11 - (c+a*num1)
    ans = int(w/num2)
    aa = str(num2) + "a = " + str(w)+ "$$수식$$$$/수식$$"

    temp = proc_jo(c,4)

    stem = stem.format(num2=num2, num1=num1,eq=eq, temp=temp, ans11=ans11)
    answer = answer.format(ans=ans)
    comment = comment.format(ine1=ine1, num1=num1, num2=num2, eq=eq, eq2=eq2, ine=ine, eq3=eq3, x_eq=x_eq, x=x, a_eq=a_eq, ans=ans,aa=aa, comb=comb)

    return stem, answer, comment


#중2-1-2-51
def expressions212_Stem_046():
    stem = "\nx에 대한 일차부등식 $$수식$${eq}$$/수식$$$$수식$$``$$/수식$${temp1}$$수식$$``$$/수식$$ 만족시\n" \
           "키는 x의 값 중에서 $$수식$${num}$$/수식$$$$수식$$``$$/수식$${temp2}$$수식$$``$$/수식$$ 서로소인 자연수가 $$수식$${many}$$/수식$$개\n" \
           "일 때, a의 값 중 가장 큰 정수를 A, 가장 작은\n" \
           "정수를 B라 한다. 이 때 A + B의 값을 구하시오."
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서\n" \
              "$$수식$${eq2}$$/수식$$, $$수식$${eq3}$$/수식$$\n" \
              "∴ $$수식$${x}$$/수식$$\n" \
              "이때 $$수식$${num}$$/수식$$$$수식$$``$$/수식$${temp2}$$수식$$``$$/수식$$ 서로소인 자연수를 작은 것부터 크기순\n" \
              "으로 나열하면\n" \
              "$$수식$${list}$$/수식$$\n" \
              "이므로 주어진 일차부등식을 만족시키는 x의 값\n" \
              "중에서 $$수식$${num}$$/수식$$$$수식$$``$$/수식$${temp2}$$수식$$``$$/수식$$ 서로소인 자연수 $$수식$${many}$$/수식$$개는 $$수식$${ans_list}$$/수식$$이다.\n" \
              "즉, $$수식$${complic}$$/수식$$이므로 $$수식$${complic_ineq}$$/수식$$\n" \
              "$$수식$${complic_ineq2}$$/수식$$ ∴ $$수식$${complic_ineq3}$$/수식$$\n" \
              "$$수식$${bound1}$$/수식$$, $$수식$${bound2}$$/수식$$\n" \
              "A = $$수식$${A}$$/수식$$, B = $$수식$${B}$$/수식$$\n" \
              "∴ A + B = $$수식$${AB}$$/수식$$ = $$수식$${answ}$$/수식$$"

    inequality = [" ≤ ", " ≥ "]
    con = np.random.randint(0, 2)
    ine = inequality[0]
    num = np.random.randint(5, 20)
    liste=[]
    list=""
    for i in range(1, 10000):
        if gcd(i,num)==1:
            liste.append(i)
            list = list + str(i)+"$$수식$$$$/수식$$" + ", " + "$$수식$$$$/수식$$"
        if len(liste)==6:
            break
    list = list + "$$수식$$CDOTS$$/수식$$"
    many = np.random.randint(2, 10)
    while many>= len(liste)-1:
        many = np.random.randint(2, 10)

    a = np.random.randint(1, 15)
    b = np.random.randint(2, 10)
    c =  np.random.randint(2, 10)
    while (liste[many-1] * (c + b) - a)==0 or ((liste[many]*(c+b)-a))==0:
        a = np.random.randint(1, 15)
        b = np.random.randint(2, 10)
        c = np.random.randint(2, 10)
    eq="x - a" +  ine +"$$수식$${"+str(a)+" - "+str(b)+"x} over {"+str(c)+"}$$/수식$$"+"$$수식$$$$/수식$$"
    eq2 = str(c) +"x - " + str(c) + "a" +ine +str(a)+" - "+str(b)+"x $$수식$$$$/수식$$"
    eq3 = str(c+b) +"x" + ine + str(c) +"a + " + str(a) +"$$수식$$$$/수식$$"
    x = "x"+ine +"$$수식$${" + str(c) +"a + " + str(a) +"} over {"+str(c+b)+"}$$/수식$$"
    ans_list =""
    if many>1:
        for i in range(many-1):
            ans_list = ans_list + str(liste[i]) +" , " + "$$수식$$$$/수식$$"
    ans_list = ans_list + str(liste[many-1])
    complic = str(liste[many-1]) + ine  + "$$수식$${" + str(c) +"a + " + str(a) +"} over {"+str(c+b)+"}$$/수식$$ &lt; " + str(liste[many])+ "$$수식$$$$/수식$$"
    complic_ineq =  str(liste[many-1]*(c+b)) + ine + str(c) +"a + " + str(a) + " &lt; " + str(liste[many]*(c+b))+ "$$수식$$$$/수식$$"
    complic_ineq2 =  str(liste[many-1]*(c+b)-a) + ine + str(c) +"a" +  " &lt; " + str(liste[many]*(c+b)-a)+ "$$수식$$$$/수식$$"
    complic_ineq3 =""
    j = int((liste[many-1] * (c + b) - a) / c)
    if (liste[many-1] * (c + b) - a) / c<0:
        j = int((liste[many-1] * (c + b) - a) / c) -1
    k = int((liste[many]*(c+b)-a)/c)
    gcd1 = gcd(abs(liste[many-1] * (c + b) - a), abs(c))
    t = int((liste[many-1] * (c + b) - a) / gcd1)
    u = int(c/gcd1)
    gcd2 = gcd(abs(liste[many] * (c + b) - a), abs(c))
    t1 = int((liste[many] * (c + b) - a) / gcd2)
    u1 = int(c/gcd2)
    if (liste[many-1]*(c+b)-a)%c ==0:
        complic_ineq3 = str(j) + ine + "a &lt; $$수식$${" + str(t1) +"} over {"+str(u1)+"}$$/수식$$"+ "$$수식$$$$/수식$$"
        if u1==1:
            complic_ineq3 = str(j) + ine + "a &lt; " + str(t1)
    elif (liste[many]*(c+b)-a)%c ==0:
        complic_ineq3 = "$$수식$${" + str(t) + "} over {" + str(u) + "}$$/수식$$" + ine + "a &lt; " + str(k)+ "$$수식$$$$/수식$$"
        if u==1:
            complic_ineq3 =  str(t) + ine + "a &lt; " + str(k) + "$$수식$$$$/수식$$"
    elif (liste[many-1]*(c+b)-a)%c ==0 and (liste[many]*(c+b)-a)%c ==0:
        complic_ineq3 = str(j) + ine + "a &lt; " + str(k)+ "$$수식$$$$/수식$$"
    else:
        complic_ineq3 = "$$수식$${" + str(t) + "} over {" + str(u) + "}$$/수식$$" + ine + "a &lt; "
        if u==1:
            complic_ineq3 =  str(t)  + ine + "a &lt; "
        if u1!=1:
            complic_ineq3 = complic_ineq3 + "$$수식$${" + str(t1) +"} over {"+str(u1)+"}$$/수식$$"+ "$$수식$$$$/수식$$"
        else:
            complic_ineq3 = complic_ineq3 + str(t1)
    lp=1
    bound1 = str(j) + "&lt; " +  "$$수식$${" + str(t) + "} over {" + str(u) + "}$$/수식$$" + " &lt; " + str(j+lp)+"$$수식$$$$/수식$$"
    if u==1:
        lp = 1
        while j>=t:
            j = j-1
        while t>=j+lp:
            lp+=1
        bound1 = str(j) + "&lt; " + str(t) + " &lt; " + str(j + lp) + "$$수식$$$$/수식$$"

    pp=1
    bound2 = str(k) + " &lt; $$수식$${" + str(t1) +"} over {"+str(u1)+"}$$/수식$$ &lt; " +  str(k+pp)+"$$수식$$$$/수식$$"
    if u1==1:
        pp = 1
        while k >= t1:
             k = k - 1
        while t1 >= k + pp:
            pp += 1
        bound2 = str(k) + " &lt; " + str(t1) + " &lt; " + str(k + pp) + "$$수식$$$$/수식$$"

    A = k
    B = j+lp
    AB = str(A) +" + " + str(B) +"$$수식$$$$/수식$$"
    answ = A+B

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    temp1 = proc_jo(c, 4)
    temp2 = proc_jo(num, 2)

    stem = stem.format(eq=eq, temp1=temp1, num=num, temp2=temp2, many=many)
    answer = answer.format(ans=answ)
    comment = comment.format(eq=eq, eq2=eq2, eq3=eq3, num=num, temp2=temp2, list=list, ans_list=ans_list, many=many,
                             complic=complic, complic_ineq=complic_ineq, complic_ineq2=complic_ineq2,
                             complic_ineq3=complic_ineq3, x=x, answ=answ,
                                                                    bound1=bound1, bound2=bound2, A=A, B=B, AB=AB)

    return stem, answer, comment


#중2-1-2-52
def expressions212_Stem_047():
    stem = "\nx에 대한 일차부등식 $$수식$${eq}$$/수식$$$$수식$$``$$/수식$${temp1}$$수식$$``$$/수식$$ 만족시\n" \
           "키는 자연수 x가 $$수식$${num}$$/수식$$개 이상일 때, 상수 a의 값의\n" \
           "범위는?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서 $$수식$${eq2}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$    $$수식$${simp}$$/수식$$\n" \
              "이 부등식을 만족시키는 자연수 x가 $$수식$${num}$$/수식$$개 이상이\n" \
              "려면 $$수식$${ans_e}$$/수식$$, $$수식$${ans_eq}$$/수식$$      ∴ {answ}"

    inequality = [" ≤ ", " ≥ "]
    con = np.random.randint(0, 2)
    ine = inequality[con]
    a = np.random.randint(2, 15)
    b = np.random.randint(2, 15)
    c = np.random.randint(1, 15)
    num = np.random.randint(1, 10)
    lcm1 = lcm(a, b)
    p = int(lcm1 / a)
    g = int(lcm1 / b)
    if con==1:
        while a<=b or  p%(p-g)!=0 or (num - (-1*(lcm1*c)/(a-b)))%(-p/(p-g))!=0:
            a = np.random.randint(2, 15)
            b = np.random.randint(2, 15)
            c = np.random.randint(1, 15)
            num = np.random.randint(1, 10)
            lcm1 = lcm(a, b)
            p = int(lcm1 / a)
            g = int(lcm1 / b)
    else:
        while a>=b or p%(p-g)!=0 or (num - (-1*(lcm1*c)/(a-b)))%(-p/(p-g))!=0:
            a = np.random.randint(2, 15)
            b = np.random.randint(2, 15)
            c = np.random.randint(1, 15)
            num = np.random.randint(1, 10)
            lcm1 = lcm(a, b)
            p = int(lcm1 / a)
            g = int(lcm1 / b)
    eq = "$$수식$${rm x + rm a} over {" + str(a) + "}$$/수식$$" + ine + "$$수식$$rm x over {" + str(b) + "}$$/수식$$ - " + str(c) + "$$수식$$$$/수식$$"
    a= p
    b=g


    temp1 = proc_jo(c,4)
    eq2 = str(a) +"(x + a)" + ine + str(b) +"x - " + str(lcm1*c) +  "$$수식$$$$/수식$$"
    eq3 = str(a) +"x + " + str(a) + "a" + ine + str(b) +"x - " + str(lcm1*c) +  "$$수식$$$$/수식$$"
    simp = "x" + " ≤ " + str(int(-a/(a-b))) +"a + " + str(int(-1*(lcm1*c)/(a-b)))+  "$$수식$$$$/수식$$"
    if int(-1*(lcm1*c)/(a-b))<0:
        simp = "x" + " ≤ " + str(int(-a / (a - b))) + "a - " + str(int((lcm1 * c) / (a - b))) + "$$수식$$$$/수식$$"
    if int(-a / (a - b))==1:
        simp = "x" + " ≤ " + "a - " + str(int((lcm1 * c) / (a - b))) + "$$수식$$$$/수식$$"
        if ((lcm1 * c) / (a - b)) <0:
            simp = "x" + " ≤ " + "a + " + str(int((lcm1 * c) / (a - b))) + "$$수식$$$$/수식$$"
    if a==1:
        eq2 = "(x + a)" + ine + str(b) +"x - " + str(lcm1*c) +  "$$수식$$$$/수식$$"
        eq3 = "x + a" + ine + str(b) +"x - " + str(lcm1*c) +  "$$수식$$$$/수식$$"
    elif a==-1:
        eq2 = "- (x + a)" + ine + str(b) + "x - " + str(lcm1 * c) + "$$수식$$$$/수식$$"
        eq3 = " -x - a" + ine + str(b) + "x - " + str(lcm1 * c) + "$$수식$$$$/수식$$"


    ans_e= str(int(-a/(a-b))) +"a + " + str(int(-1*(lcm1*c)/(a-b)))+ " ≥ " + str(num) + "$$수식$$$$/수식$$"
    if (-1 * (lcm1 * c) / (a - b)) < 0:
        ans_e = str(int(-a/(a-b))) +"a - " + str(int((lcm1 * c) / (a - b))) + " ≥ " + str(num) + "$$수식$$$$/수식$$"
    if int(-a/(a-b))==1:
        ans_e ="a + " + str(int(-1 * (lcm1 * c) / (a - b))) + " ≥ " + str(num) + "$$수식$$$$/수식$$"
        if (-1 * (lcm1 * c) / (a - b))<0:
            ans_e = "a - " + str(int((lcm1 * c) / (a - b))) + " ≥ " + str(num) + "$$수식$$$$/수식$$"
    elif int(-a/(a-b))==-1:
        ans_e ="- a + " + str(int(-1 * (lcm1 * c) / (a - b))) + " ≥ " + str(num) + "$$수식$$$$/수식$$"
        if (-1 * (lcm1 * c) / (a - b)) < 0:
            ans_e = "- a - " + str(int((lcm1 * c) / (a - b))) + " ≥ " + str(num) + "$$수식$$$$/수식$$"
    aaa = num - (-1*(lcm1*c)/(a-b))
    aaa= int(aaa)
    bbb = int(-a/(a-b))
    yyy = aaa-bbb
    ans_eq = str(int(-a/(a-b))) +"a ≥ " +  str(aaa)
    if int(-a/(a-b))==1:
        ans_eq = "a ≥ " +  str(aaa)
    elif int(-a/(a-b))==-1:
        ans_eq = "-a ≥ " + str(aaa)
    ans11 = int(aaa/bbb)
    answ = "a ≥ " + str(ans11)
    if int(-a/(a-b))<0:
        ine = " ≤ "
        answ = "a ≤ " + str(ans11)
    dd=[]
    bb=[]
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = ans11 + k
        else:
            k = abs(ans11 - k)
        aaaa = k
        rr = np.random.randint(0, 1)
        if rr==1:
            aaaa = aaaa*-1
        if aaaa!=ans11 and aaaa not in dd:
            dd.append(aaaa)
            bb.append("a ≤ " + str(aaaa))

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, temp1=temp1, num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=answ)
    comment = comment.format(eq=eq, eq3=eq3, eq2=eq2, simp=simp, num=num, ans_e=ans_e, ans_eq=ans_eq, answ=answ)

    return stem, answer, comment

#중2-1-2-53
def expressions212_Stem_048():
    stem = "\n어떤 자연수를 $$수식$${num1}$$/수식$$배하여 $$수식$${num2}$$/수식$$$$수식$$``$$/수식$${temp1}$$수식$$``$$/수식$$ 뺐더니 처음 자연수\n" \
           "를 $$수식$${num3}$$/수식$$배하여 $$수식$${num4}$$/수식$$$$수식$$``$$/수식$${temp2}$$수식$$``$$/수식$$ 더한 것보다 작았다. 이를 만족시\n" \
           "키는 자연수들의 합은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "어떤 자연수를 x라 하면\n" \
              "$$수식$${eq}$$/수식$$, $$수식$${x}$$/수식$$\n" \
              "따라서 자연수 x는 $$수식$${list}$$/수식$$이므로 구하\n" \
              "는 합은\n" \
              "$$수식$${add}$$/수식$$"

    num1 = np.random.randint(2, 7)
    num2 = np.random.randint(1, 7)
    num3 = np.random.randint(2, 7)
    num4 =  np.random.randint(1, 7)
    while num3>=num1 or (num4+num2)%(num1-num3)!=0:
        num1 = np.random.randint(2, 7)
        num2 = np.random.randint(1, 7)
        num3 = np.random.randint(2, 7)
        num4 = np.random.randint(1, 7)
    temp1 = proc_jo(num2, 4)
    temp2 = proc_jo(num4, 4)

    eq = str(num1) + "x - " + str(num2) + " &lt; " + str(num3) +"x + "+ str(num4) + "$$수식$$$$/수식$$"
    o = (num4+num2)/(num1-num3)
    o = int(o)
    x = "x &lt; " + str(o)
    list=""
    add=""
    answ=0
    for i in range(1,o-1):
        add = add + str(i) + " + "
        list = list + str(i) +"$$수식$$`, `$$/수식$$"
        answ = i + answ
    answ = answ + o -1
    add = add +  str(o-1) +" = " + str(answ)
    list = list + str(o-1) +"$$수식$$$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(temp1=temp1, temp2=temp2, num1=num1, num2=num2, num3=num3, num4=num4, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, answ=answ, list=list, x=x, add=add)

    return stem, answer, comment


#중2-1-2-56
def expressions212_Stem_049():
    stem = "\n어느 주차장의 주차요금은 $$수식$${min}$$/수식$$분까지는 $$수식$${in_cost}$$/수식$$원이\n" \
           "고, $$수식$${min}$$/수식$$이 지나면 1분마다 $$수식$${ad_cost}$$/수식$$원씩 요금이 추가\n" \
           "된다고 한다. 주차요금이 $$수식$${total}$$/수식$$원 이하게 되게 하\n" \
           "려면 최대 몇 분 동안 주차할 수 있는가?" \
           "\n① $$수식$${x1}분\n② {x2}분\n③ {x3}분\n④ {x4}분\n⑤ {x5}분\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "x분 동안 주차한다고 하면(단, 60초 미만은 올림\n" \
              "한다.)\n" \
              "$$수식$${eq}$$/수식$$,\n" \
              "$$수식$${eq2}$$/수식$$,\n" \
              "$$수식$${eq3}$$/수식$$  ∴ x ≤ $$수식$${answ}$$/수식$$\n" \
              "따라서 최대 $$수식$${answ}$$/수식$$분 동안 주차할 수 있다."

    mins = [15, 30]
    min= mins[ np.random.randint(0,2)]
    in_cost = np.random.randint(1,5)*1000
    ad_cost = np.random.randint(1,5)*100
    total = np.random.randint(6,10)*1000
    while (total+min*ad_cost-in_cost)%ad_cost!=0:
        min = mins[np.random.randint(0, 2)]
        in_cost = np.random.randint(1, 5) * 1000
        ad_cost = np.random.randint(1, 5) * 100
        total = np.random.randint(6, 10) * 1000
    eq = str(in_cost) +" + " + str(ad_cost) +"(x - " + str(min) +")" + " ≤ " +  str(total) + "$$수식$$$$/수식$$"
    eq2 = str(in_cost) +" + " + str(ad_cost) +"x - " + str(min*ad_cost) + " ≤ " +  str(total) + "$$수식$$$$/수식$$"
    eq3 =  str(ad_cost) +"x" + " ≤ " + str(total+min*ad_cost-in_cost)+ "$$수식$$$$/수식$$"
    hh = (total+min*ad_cost-in_cost)/ad_cost
    hh = int(hh)
    answ = hh

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(min=min, ad_cost=ad_cost, in_cost=in_cost, total=total, x1=x1, x2=x2, x3=x3, x4=x4,x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq,eq2=eq2, eq3=eq3,answ=answ)

    return stem, answer, comment


#중2-1-2-60
def expressions212_Stem_050():
    stem = "\n삼각형의 세 변의 길이가 각각 $$수식$${eq}$$/수식$$, $$수식$${eq2}$$/수식$$,\n" \
           "$$수식$${eq3}$$/수식$$일 때, x의 값의 범위는?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "가장 긴 변의 길이가 $$수식$${eq3}$$/수식$$이므로\n" \
              "(i)($$수식$${eq}$$/수식$$) + ($$수식$${eq2}$$/수식$$) &gt; $$수식$${eq3}$$/수식$$에서\n" \
              "$$수식$${comb1}$$/수식$$  ,  $$수식$${x11}$$/수식$$\n" \
              "(ii) $$수식$${eq}$$/수식$$ &gt; 0에서 $$수식$${x22}$$/수식$$\n" \
              "따라서 (i), (ii)에서 $$수식$${answ}$$/수식$$"
    a = np.random.randint(1, 6)
    b = np.random.randint(1, 6)
    c = np.random.randint(2, 6)
    while b>=c or a==b or (-a+b)>=c:
        a = np.random.randint(1, 6)
        b = np.random.randint(1, 6)
        c = np.random.randint(2, 6)
    eq = "x - " + str(a) + "$$수식$$$$/수식$$"
    eq2 = "x + "+str(b) + "$$수식$$$$/수식$$"
    eq3 = "x + " + str(c) + "$$수식$$$$/수식$$"
    comb1 = "2x "
    if a>b:
        comb1 = comb1 + " - " +str(a-b) + "$$수식$$$$/수식$$"
    if a<b:
        comb1 = comb1 + " + " + str(b-a) + "$$수식$$$$/수식$$"
    comb1 = comb1 + " &gt; " + eq3+ "$$수식$$$$/수식$$"
    x11= "x &gt; " + str(c-(b-a))
    x22 = "x &gt; " + str(a)
    answ1 = max(c-(b-a), a)
    answ = "x &gt; " + str(answ1)

    bb = []
    dd=[]
    while len(bb) < 4:
        k = np.random.randint(1, answ1*3)
        if k not in dd and k != answ1:
            dd.append(k)
            bb.append("x &gt; " + str(k))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, eq2=eq2, eq3=eq3, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq3=eq3, eq=eq, eq2=eq2, comb1=comb1, x11=x11, x22=x22,  answ=answ)

    return stem, answer, comment


#중2-1-2-61
def expressions212_Stem_051():
    stem = "\n주사위를 던져 나온 눈의 수의 $$수식$${num1}$$/수식$$배에서 $$수식$${num2}$$/수식$$$$수식$$``$$/수식$${temp1}$$수식$$``$$/수식$$ 뺀\n" \
           "값은 그 눈의 수의 $$수식$${num3}$$/수식$$배에 $$수식$${num4}$$/수식$$$$수식$$``$$/수식$${temp2}$$수식$$``$$/수식$$ 더한 값보다 크다\n" \
           "고 한다. 이를 만족시키는 주사위의 모든 눈의 수\n" \
           "의 합은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "주사위를 던져 나온 눈의 수를 x라 하면\n" \
              "$$수식$${eq}$$/수식$$, $$수식$${eq2}$$/수식$$\n" \
              "∴ $$수식$${x}$$/수식$$\n" \
              "따라서 모든 눈의 수의 합은 $$수식$${list}$$/수식$$"

    num1 = np.random.randint(2, 6)
    num2 = np.random.randint(1, 6)
    num3 = np.random.randint(2, 6)
    num4 =  np.random.randint(1, 6)
    while num3>=num1 or (num4+num2)%(num1-num3)!=0 or (num4+num2)/(num1-num3)>=6:
        num1 = np.random.randint(2, 6)
        num2 = np.random.randint(1, 6)
        num3 = np.random.randint(2, 6)
        num4 = np.random.randint(1, 6)

    eq = str(num1) + "x - " + str(num2) + " &gt; " + str(num3) + "x + " + str(num4) + "$$수식$$$$/수식$$"
    eq2 = str(num1-num3) +"x &gt; " + str(num4+num2)+ "$$수식$$$$/수식$$"
    if num1-num3==1:
        eq2 = "x &gt; " + str(num4 + num2) + "$$수식$$$$/수식$$"
    ans1 = (num4+num2)/(num1-num3)
    x ="x &gt; " + str(int(ans1))+ "$$수식$$$$/수식$$"
    list=""
    answ=0
    for i in range(1,6):
        if i> ans1:
            answ = i + answ
            list = list + str(i) + " + "
    answ = answ + 6
    list = list + str(6) + " = " + str(answ)
    if ans1==5:
        list = str(6)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    temp1 = proc_jo(num2, 4)
    temp2 = proc_jo(num4, 4)

    stem = stem.format(temp1=temp1, temp2=temp2, num1=num1, num2=num2, num3=num3, num4=num4, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, x=x, list=list)

    return stem, answer, comment



#중2-1-2-62
def expressions212_Stem_052():
    stem = "\n연속하는 세 개의 $$수식$${num1}$$/수식$$의 배수의 합이 $$수식$${low}$$/수식$$보다 크다\n" \
           "다고 한다. 이와 같은 세 수 중 가장 작은 수를 x\n" \
           "라 할 떼, x의 값이 될 수 있는 가장 작은 수는?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "연속하는 세 개의 $$수식$${num1}$$/수식$$의 배수를 x, x + $$수식$${a}$$/수식$$, x + $$수식$${b}$$/수식$${temp}\n" \
              "라 하면\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$    ∴ x &gt; $$수식$${aa}$$/수식$$\n" \
              "따라서 x는 $$수식$${num1}$$/수식$$의 배수이므로 x의 값이 될 수 있\n" \
              "는 가장 작은 수는 $$수식$${answ}$$/수식$${temp3}다."

    num1 = np.random.randint(2, 6)
    a = num1
    b = num1*2
    temp = proc_jo(b, 3)
    low = np.random.randint(30, 100)
    while low-a-b<=0 or (low-a-b)%3!=0:
        num1 = np.random.randint(2, 6)
        a = num1
        b = num1 * 2
        low = np.random.randint(20, 100)
    eq = "x + (x + " + str(a) +") + (x + " + str(b) +") &gt; " + str(low) + "$$수식$$$$/수식$$"
    eq2 = "3x &gt; " + str(low-a-b) + "$$수식$$$$/수식$$"
    v =(low-a-b)
    aa = int(v/3)
    answ=0
    for i in range (aa, 10000):
        if i%num1==0 and i>aa:
            answ = i
            break
    bb=[]
    while len(bb)<4:
        c = np.random.randint(2, 10)
        if c*num1!=answ and c*num1 not in bb:
            bb.append(c*num1)
    temp3 = proc_jo(answ,3)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(num1=num1, low=low,  x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp3=temp3, answ=answ, temp=temp, num1=num1, aa=aa, a=a, b=b, eq=eq, eq2=eq2)

    return stem, answer, comment



#중2-1-2-63
#분수에 곱하기 넣는 방법을 모름
def expressions212_Stem_053():
    stem = "\n남학생이 $$수식$${boy}$$/수식$$명, 여학생이 $$수식$${girl}$$/수식$$명인 학급에서 여학생\n" \
           "의 영어 점수의 평균은 $$수식$${g_score}$$/수식$$점이다. 전체 학생들의\n" \
           "평균 점수가 $$수식$${ave}$$/수식$$점 이상이 되려면 남학생의 평균\n" \
           "점수는 몇 점 이상이 되어야 하는가?"\
           "\n① $$수식$${x1}점 이상\n② {x2}점 이상\n③ {x3}점 이상\n④ {x4}점 이상\n⑤ {x5}점 이상\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "남학생의 평균 점수를 x점이라 하면\n" \
              "$$수식$${compl}$$/수식$$, $$수식$${eq}$$/수식$$,\n" \
              "$$수식$${eq2}$$/수식$$, $$수식$${eq3}$$/수식$$\n" \
              "따라서 남학생의 평균은 $$수식$${answ}$$/수식$$점 이상이어야 한다." \

    boy = np.random.randint(3, 7) *5
    girl = np.random.randint(3, 7) *5
    while boy==girl:
        girl = np.random.randint(3, 7) *5

    g_score = np.random.randint(14, 20)*5
    ave = np.random.randint(13, 14)*5
    compl = "$$수식$${"+str(boy)+"x + "+str(girl)+" TIMES "+str(g_score)+"} over {"+str(boy)+" + "+str(girl)+"}$$/수식$$"+ "$$수식$$$$/수식$$"
    compl = compl + "       " + "$$수식$$``$$/수식$$    ≥" + str(ave) + "$$수식$$$$/수식$$"
    eq = str(boy)+"x + "+str(girl*g_score)  + " ≥ " + str(ave*(girl+boy))+"$$수식$$$$/수식$$"
    dd = (ave*(girl+boy))-(girl*g_score)
    eq2 = str(boy)+"x" + " ≥ " + str(int(dd)) +"$$수식$$$$/수식$$"
    eq3 = "x ≥ " + str(round(dd/boy,1))+"$$수식$$$$/수식$$"
    answ = round(dd/boy,1)
    if dd%boy==0:
        eq3 = "x ≥ " + str(int(dd / boy)) + "$$수식$$$$/수식$$"
        answ = int(dd / boy)

    bb = []
    while len(bb) < 4:
        c = np.random.randint(350, 500)
        if c%5==0:
            c = int(c/5)
        else:
            c = c/5
        if c!= answ:
            bb.append(c)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(boy=boy, girl=girl, g_score=g_score, ave=ave, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(compl=compl, eq=eq, eq2=eq2, eq3=eq3, answ=answ)

    return stem, answer, comment

#중2-1-2-64
def expressions212_Stem_054():
    stem = "\n전체 학생이 $$수식$${pop}$$/수식$$명인 {clas}반에서 두 번에 걸쳐 모의\n" \
           "시험을 시행한 결과 $$수식$${num}$$/수식$$명의 학생은 1회 시험에 비\n" \
           "해 2회 시험에서 평균 $$수식$${rise}$$/수식$$점이 올랐고 나머지 학생\n" \
           "들의 점수에는 변화가 없었다. 이 {clas}반 전체 학생\n" \
           "의 2회 모의 시험 점수 평균이 $$수식$${ave}$$/수식$$점 이상일 때,\n" \
           "1회 모의 시험의 평균은 최소 몇 점인지 구하시\n" \
           "오.(단, 학생 수는 변하지 않는다.)"
    answer = "(답): \n" \
            "{ans} 점\n"
    comment = "(해설)\n" \
              "1회 모의 시험 점수 평균을 x점이라 하면 2회\n" \
              "모의 시험 점수의 총점은 $$수식$${eq}$$/수식$$점이므로\n" \
              "$$수식$${compl}$$/수식$$     ≥ $$수식$${ave}$$/수식$$, $$수식$${eq2}$$/수식$$\n" \
              "∴ x ≥ $$수식$${ans}$$/수식$$\n" \
              "따라서 1회 모의 시험 점수의 평균은 최소 $$수식$${ans}$$/수식$$점\n" \
              "이다."
    classe = ["A", "B", "C", "D", "E", "F" ]
    clas = classe[np.random.randint(0, 6)]
    pop = np.random.randint(20, 40)
    num = np.random.randint(2, 10)
    rise = np.random.randint(2, 10)
    ave = np.random.randint(68, 100)
    while (rise*num)%pop!=0:
        pop = np.random.randint(20, 40)
        num = np.random.randint(2, 10)
        rise = np.random.randint(2, 10)
        ave = np.random.randint(68, 100)

    eq = "(" + str(pop) +"x + " + str(num) + "$$수식$$TIMES$$/수식$$" + str(rise)+ ")$$수식$$$$/수식$$"
    compl = "$$수식$${"+str(pop)+"x + "+str(num)+" TIMES "+str(rise)+"} over {"+str(pop)+"}$$/수식$$"+ "$$수식$$$$/수식$$"
    ss = (rise*num)/pop
    ss = int(ss)
    eq2 = "x + " + str(ss) + " ≥ " + str(ave)
    ans = ave-ss

    stem = stem.format(clas=clas, pop=pop, num=num, rise=rise, ave=ave)
    answer = answer.format(ans=ans)
    comment = comment.format(clas=clas,ave=ave, eq=eq, compl=compl, ans=ans, eq2=eq2)

    return stem, answer, comment


#중2-1-2-65
def expressions212_Stem_055():
    stem = "\n{name}는 꽃집에서 한 송이에 $$수식$${flow}$$/수식$$ 원인 장미를 여\n" \
           "러 송이 구입하여 포장하려고 한다. 포장하는 가\n" \
           "격이 $$수식$${new_cost}$$/수식$$ 원일 때, {name}는 $$수식$${new_cost1}$$/수식$$ 원으로 장미를\n" \
           "{ee} 몇 송이까지 구입하여 포장할 수 있는가?" \
           "\n① $$수식$${x1}송이\n② {x2}송이\n③ {x3}송이\n④ {x4}송이\n⑤ {x5}송이\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "장미를 x송이 구입한다고 하면\n" \
              "$$수식$${eq}$$/수식$$,\n" \
              "$$수식$${eq2}$$/수식$$, x {ine} $$수식$${answ}$$/수식$$\n" \
              "따라서 장미를 {ee} $$수식$${answ}$$/수식$$송이{eeee} 구입할 수 있다." \

    u = ["최대", "최소"]
    inequality = [" ≤ ", " ≥ "]
    w = ["까지",""]
    con = 0
    ee = u[con]
    ine = inequality[con]
    eeee = w[con]



    nameList = ["경희", "민철이", "수진이", "철수","영대","선주"]
    o = np.random.randint(0, 6)
    name1 = nameList[o]

    flow = np.random.randint(10, 20)*100
    new_cost = np.random.randint(10, 30)*100
    new_cost1 = np.random.randint(10, 30)*1000
    while flow>=new_cost or (new_cost1-new_cost)%flow!=0:
        flow = np.random.randint(10, 20) * 100
        new_cost = np.random.randint(10, 30) * 100
        new_cost1 = np.random.randint(10, 30) * 1000

    eq = str(flow)+"x + " + str(new_cost) + ine + str(new_cost1)+ "$$수식$$$$/수식$$"
    eq2 = str(flow)+"x" + ine + str(new_cost1-new_cost)+ "$$수식$$$$/수식$$"
    f = (new_cost1-new_cost)/flow
    answ = int(f)

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(ee=ee, name=name1,flow=flow, new_cost=new_cost, new_cost1=new_cost1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, ee=ee, eeee=eeee, ine=ine,answ=answ, eq2=eq2)

    return stem, answer, comment


#중2-1-2-66
def expressions212_Stem_056():
    stem = "\n최대 $$수식$${num1}$$/수식$$톤까지 실을 수 있는 엘리베이터를 이용\n" \
           "하여 몸무게의 합이 $$수식$${total}$$/수식$$kg인 두 사람이 한 개의\n" \
           "무게가 $$수식$${weight}$$/수식$$kg인 물건을 운반하려고 한다. 한 번에\n" \
           "최대 몇 개의 상자를 운반할 수 있는지 구하시오.\n" \
           "(단, 두 사람은 동시에 엘리베이터에 탑승한다.)\n"
    answer = "(답): \n" \
            "{answ} 개\n"
    comment = "(해설)\n" \
              "두 사람이 한 번에 x개의 상자를 운반한다고 하면\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$    ∴ x ≤ $$수식$${ans11}$$/수식$$\n" \
              "따라서 한 번에 최대 $$수식$${answ}$$/수식$$개의 상자를 운반할 수 있\n" \
              "다."

    num1 = np.random.randint(11, 20)/10
    total = np.random.randint(100, 150)
    weight =  np.random.randint(20, 50)
    while (num1*1000+total)%weight!=0:
        num1 = np.random.randint(11, 20) / 10
        total = np.random.randint(100, 150)
        weight = np.random.randint(20, 50)
    eq = str(total) + " + " + str(weight) +"x ≤ " + str(int(num1*1000))
    eq2 = str(weight) + "x ≤ " +  str(int(num1*1000-total))
    ans11 = round((num1*1000-total)/weight, 1)
    answ = int(ans11)


    stem = stem.format(weight=weight, num1=num1, total=total)
    answer = answer.format(answ=answ)
    comment = comment.format(eq=eq, eq2=eq2, answ=answ, ans11=ans11)

    return stem, answer, comment


#중2-1-2-67
def expressions212_Stem_057():
    stem = "\n어느 물류센터에서 의류 상자 $$수식$${num}$$/수식$$ 개를 배송하려\n" \
           "고 한다. 한 번에 $$수식$${larg}$$/수식$$개의 상자를 싣는 대형 화물\n" \
           "차와 $$수식$${small}$$/수식$$개의 사아를 싣는 소형 화물차를 합하여\n" \
           "$$수식$${tot}$$/수식$$대를 사용할 때, 사용할 수 있는 소형 화물차는\n" \
           "최댜 몇 대인지 구하시오.\n"
    answer = "(답): \n" \
            "{answ} 대\n"
    comment = "(해설)\n" \
              "소형 화물차를 x대 사용한다고 하면 대형 화물차\n" \
              "는 ($$수식$${tot}$$/수식$$ - x)대 사용할 수 있으므로\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$, $$수식$${eq3}$$/수식$$\n" \
              "$$수식$${ineq}$$/수식$$\n" \
              "따라서 사용할 수 있는 소형 화물차는 최대 $$수식$${answ}$$/수식$$대이\n" \
              "다."

    num = np.random.randint(11, 20)*100
    larg =np.random.randint(2, 10)*10
    small = np.random.randint(1, 6)*10
    tot = np.random.randint(5, 20)
    while larg<=small or num-(tot*larg)>=0 or (num-(tot*larg))/(small-larg)<1:
        num = np.random.randint(11, 20) * 100
        larg = np.random.randint(2, 10) * 10
        small = np.random.randint(1, 6) * 10
        tot = np.random.randint(5, 20)
    eq = str(larg) +"(" + str(tot) +" - x) + " + str(small) +"x ≥ " + str(num) +"$$수식$$$$/수식$$"
    eq2 = str(tot*larg) +" - " + str(larg-small) +" x ≥ " + str(num) +"$$수식$$$$/수식$$"
    eq3 = str(small-larg) +" x ≥ " + str(num-(tot*larg))+"$$수식$$$$/수식$$"
    ineq =""
    answ=0
    if (num-(tot*larg))%(small-larg)==0:
        aa =(num-(tot*larg))/(small-larg)
        aa = int(aa)
        ineq = "x ≤ " + str(abs(aa))
        answ = abs(aa)
    else:
        aa = (num - (tot * larg))
        bb = (small - larg)
        gcd1 = gcd(abs(aa),abs(bb))
        aa = aa/gcd1
        bb = bb/gcd1
        aa =abs(int(aa))
        bb= abs(int(bb))
        ineq = "x ≤ $$수식$${"+str(aa)+"} over {"+str(bb)+"}$$/수식$$   = " + str(round(aa/bb,1))
        answ = int(aa/bb)

    stem = stem.format(larg=larg, small=small, num=num, tot=tot)
    answer = answer.format(answ=answ)
    comment = comment.format(tot=tot, eq=eq, eq2=eq2, answ=answ, eq3=eq3, ineq=ineq)

    return stem, answer, comment


#중2-1-2-68
def expressions212_Stem_058():
    stem = "\n어느 음원사이트는 한 달 기본요금이 $$수식$${pay}$$/수식$$ 이고\n" \
           "한 곡을 내려 받을 때마다 $$수식$${sin}$$/수식$$ 원을 내야 한다. 한\n" \
           "달 사용 요금이 $$수식$${month}$$/수식$$ 원을 넘지 않게 하려면 최대\n" \
           "몇 곡까지 내려 받을 수 있는가?" \
           "\n① $$수식$${x1}곡\n② {x2}곡\n③ {x3}곡\n④ {x4}곡\n⑤ {x5}곡\n   $$/수식$$"
    answer = "(답): \n" \
            "{answ} 곡\n"
    comment = "(해설)\n" \
              "x곡을 내려 받는다고 하면\n" \
              "$$수식$${eq}$$/수식$$, $$수식$${eq2}$$/수식$$\n" \
              "∴ x ≤  $$수식$${answ}$$/수식$$\n" \
              "따라서 최대 $$수식$${answ}$$/수식$$곡까지 내려 받을 수 있다."

    pay =np.random.randint(1, 7) * 1000
    sin =np.random.randint(2, 7) * 100
    month = np.random.randint(40, 90) * 100
    while month<=pay or (month-pay)%sin!=0:
        pay = np.random.randint(1, 7) * 1000
        sin = np.random.randint(2, 7) * 100
        month = np.random.randint(40, 90) * 100

    eq = str(pay) + " + " + str(sin) +"x ≤ " + str(month) +"$$수식$$$$/수식$$"
    eq2 = str(sin) +"x ≤ " + str(month-pay)
    answ = (month-pay)/sin
    answ = int(answ)

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, pay=pay, sin=sin, month=month)
    answer = answer.format(answ=ans)
    comment = comment.format(eq=eq, eq2=eq2, answ=answ)

    return stem, answer, comment


#중2-1-2-69
def expressions212_Stem_059():
    stem = "\n스티커 사진 $$수식$${num}$$/수식$$장을 인화하는 데 드는 가격은\n" \
           "$$수식$${pay}$$/수식$$ 원이고 $$수식$${num}$$/수식$$장을 초과하면 한 장당 $$수식$${ad_pay}$$/수식$$원씩 추\n" \
           "가된다고 한다. 스티커 사진 한 장당 가격이 $$수식$${hope}$$/수식$$\n" \
           "원 이하가 되게 하려면 스티커 사진을 몇 장 이상\n" \
           "인화해야 하는가?" \
           "\n① $$수식$${x1}장\n② {x2}장\n③ {x3}장\n④ {x4}장\n⑤ {x5}장\n   $$/수식$$"
    answer = "(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "스티커 사진을 x장 인화한다고 하면\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq1}$$/수식$$, $$수식$${eq2}$$/수식$$\n" \
              "∴ x ≥ $$수식$${answ}$$/수식$$"


    num= np.random.randint(5, 20)
    pay = np.random.randint(1, 8)*1000
    ad_pay = np.random.randint(2, 6)*100
    hope = np.random.randint(2, 7)*100
    while hope<=ad_pay:
        ad_pay = np.random.randint(2, 6) * 100
        hope = np.random.randint(2, 7) * 100
    aa = ((num*ad_pay)-pay) /(ad_pay-hope)
    while (pay-(num*ad_pay))%(hope-ad_pay)!=0 or aa<=0:
        num = np.random.randint(5, 20)
        pay = np.random.randint(1, 8) * 1000
        ad_pay = np.random.randint(2, 6) * 100
        hope = np.random.randint(2, 7) * 100
        while hope <= ad_pay:
            ad_pay = np.random.randint(2, 6) * 100
            hope = np.random.randint(2, 7) * 100
        aa = ((num * ad_pay) - pay) / (ad_pay - hope)
    eq= str(pay) + " + " + str(ad_pay) + "(x - " + str(num) + ")  ≤ " + str(hope)+"x" + "$$수식$$$$/수식$$"
    eq1 = str(ad_pay) + "x + " + str(pay-(num*ad_pay)) + " ≤ " + str(hope)+"x" + "$$수식$$$$/수식$$"
    eq2 = str(ad_pay-hope)+"x ≤ " + str((num*ad_pay)-pay)
    aa = int(aa)
    answ = aa

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5,num=num, pay=pay, hope=hope, ad_pay=ad_pay)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq,eq1=eq1, eq2=eq2, answ=answ)

    return stem, answer, comment

#중2-1-2-70
def expressions212_Stem_060():
    stem = "\n현재 {name1}는 $$수식$${input}$$/수식$$ 원을 예금했고, {name2}는\n" \
           "$$수식$${input1}$$/수식$$ 원을 예금했다. 앞으로 {name1}는 매월\n" \
           "$$수식$${sav1}$$/수식$$ 원씩, {name2}는 매월 $$수식$${sav2}$$/수식$$ 원씩 예금한다고\n" \
           "할 때, {name1}의 예금액이 {name2}의 예금액의 $$수식$${mul}$$/수식$$배\n" \
           "보다 많아지는 것은 최소 몇 개월 후부터인가?" \
           "\n① $$수식$${x1}개월 후\n② {x2}개월 후\n③ {x3}개월 후\n④ {x4}개월 후\n⑤ {x5}개월 후\n   $$/수식$$"
    answer = "(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "x개월 후부터 {name1}의 예금액이 {name2}의 예금\n" \
              "액의 $$수식$${mul}$$/수식$$배보다 많아진다고 하면\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$     ∴x &gt; $$수식$${ans11}$$/수식$$\n" \
              "따라서 최소 $$수식$${answ}$$/수식$$개월 후부터 {name1}의 예금액이\n" \
              "{name2}의 예금액보다 $$수식$${mul}$$/수식$$배보다 많아진다."

    nameList = ["경희", "민철이", "수진이", "철수", "영대","수현이","준형이"]
    o = np.random.randint(0, 7)
    name1 = nameList[o]
    o1 = np.random.randint(0, 7)
    name2 = nameList[o1]
    while o == o1:
        o1 = np.random.randint(0, 7)
        name2 = nameList[o1]

    input =  np.random.randint(20, 40)*1000
    input1 = np.random.randint(30, 60)*1000
    sav1 = np.random.randint(40, 80)*100
    sav2 = np.random.randint(30, 50)*100
    mul = np.random.randint(2, 4)

    while input>=input1 or sav2*mul>=sav1 or (input1*mul-input)%(sav1-(sav2*mul))!=0 or (input1*mul-input)/(sav1-(sav2*mul))>70:
        input = np.random.randint(20, 40) * 1000
        input1 = np.random.randint(30, 60) * 1000
        sav1 = np.random.randint(40, 80) * 100
        sav2 = np.random.randint(30, 50) * 100
        mul = np.random.randint(2, 4)

    eq =str(input) +" + " + str(sav1) +"x &gt; " + str(mul) +"(" + str(input1)+ " + " + str(sav2) +"x)"+ "$$수식$$$$/수식$$"
    eq2 = str(input) +" + " + str(sav1) +"x &gt; " +str(input1*mul)+ " + " + str(sav2*mul) +"x"+ "$$수식$$$$/수식$$"
    eq3 = str(sav1-(sav2*mul)) +"x &gt; " + str(input1*mul-input)+ "$$수식$$$$/수식$$"
    ans11 = (input1*mul-input)/(sav1-(sav2*mul))
    ans11 = int(ans11)
    answ = ans11+1
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u==1:
            k = answ +k
        else:
            k = abs(answ-k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, name1=name1, name2=name2, sav1=sav1, sav2=sav2, mul=mul,
                       input=input, input1=input1)
    answer = answer.format(ans=ans)
    comment = comment.format(mul=mul, name1=name1, name2=name2, eq=eq, eq2=eq2, eq3=eq3, ans11=ans11, answ=answ)

    return stem, answer, comment



#중2-1-2-72
def expressions212_Stem_061():
    stem = "\n$$수식$${pop}$$/수식$$명 이상의 단체 관람객은 한 사람당 $$수식$${cost}$$/수식$$ 원인\n" \
           "입장료의 $$수식$${percent}$$/수식$$ %를 할인해 주는 동물원이 있다. $$수식$${pop}$$/수식$$\n" \
           "명 미만의 단체는 몇 명 이상부터 $$수식$${pop}$$/수식$$명의 단체 입\n" \
           "장권을 사는 것이 유리한가?" \
           "\n① $$수식$${x1}명\n② {x2}명\n③ {x3}명\n④ {x4}명\n⑤ {x5}명\n   $$/수식$$"
    answer = "(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "관람객 수를 x라 하면\n" \
              "$$수식$${eq}$$/수식$$    ∴ x &gt; $$수식$${ans11}$$/수식$$\n" \
              "따라서 $$수식$${answ}$$/수식$$명 이상부터 $$수식$${pop}$$/수식$$명의 단체 입장권을 사\n" \
              "는 것이 유리하다."

    pop = np.random.randint(15, 40)
    percent = np.random.randint(1, 4)/10
    percentt = int(percent*100)
    cost = np.random.randint(4, 8)*1000
    while (percent*pop)%1!=0:
        percent = np.random.randint(1, 4) / 10
        percentt = int(percent * 100)
        pop = np.random.randint(15, 40)
    eq = str(cost) + "$$수식$$TIMES$$/수식$$" + str(1-percent) +  "$$수식$$TIMES$$/수식$$" + str(pop) +" &lt; " + str(cost) +"x" + "$$수식$$$$/수식$$"
    ans11 = int((1-percent)*pop)
    answ = ans11+1
    bb=[]
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u==1:
            k = answ +k
        else:
            k = abs(answ-k)
        if k not in bb and k != answ and k<pop:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, pop=pop, cost=cost, percent=percentt)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, ans11=ans11, answ=answ, pop=pop)

    return stem, answer, comment


#중2-1-2-73
def expressions212_Stem_062():
    stem = "\n어느 {place} 입장료는 한 사람당 $$수식$${cost}$$/수식$$ 원이\n" \
           "고 $$수식$${pop}$$/수식$$명 이상의 단체인 경우에는 입장료의 $$수식$${percent}$$/수식$$ %\n" \
           "를 할인해 준다고 한다. $$수식$${pop}$$/수식$$명 미만의 단체는 몇 \n" \
           "명 이상부터 $$수식$${pop}$$/수식$$명의 단체 입장권을 사는 것이 유\n" \
           "리한가?" \
           "\n① $$수식$${x1}명\n② {x2}명\n③ {x3}명\n④ {x4}명\n⑤ {x5}명\n   $$/수식$$"
    answer = "(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "입장객 수를 x를 하면\n" \
              "$$수식$${eq}$$/수식$$     ∴ x &gt; $$수식$${ans11}$$/수식$$\n" \
              "따라서 $$수식$${answ}$$/수식$$명 이상부터 $$수식$${pop}$$/수식$$명의 단체 입장권을 사\n" \
              "는 것이 유리하다."

    places =["놀이공원","수영장","노래방","박물관","콘서트"]
    place = places[np.random.randint(0, 5)]
    pop = np.random.randint(20, 60)
    percent = np.random.randint(1, 4) / 10
    percentt = int(percent * 100)
    cost = np.random.randint(10, 15) * 1000
    while (percent*pop)%1!=0:
        percent = np.random.randint(1, 4) / 10
        percentt = int(percent * 100)
        pop = np.random.randint(15, 40)
    eq = str(cost) + "$$수식$$TIMES$$/수식$$" + str(1 - percent) + "$$수식$$TIMES$$/수식$$" + str(pop) + " &lt; " + str(
        cost) + "x" + "$$수식$$$$/수식$$"
    ans11 = int((1 - percent) * pop)
    answ = ans11 + 1

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k<pop:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(place=place, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, pop=pop, cost=cost, percent=percentt)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, ans11=ans11, answ=answ, pop=pop)

    return stem, answer, comment

#중2-1-2-74
def expressions212_Stem_063():
    stem = "\n어느 {item}에 원가의 $$수식$${percent}$$/수식$$%의 이익을 붙여서 정\n" \
           "가를 정하였다. 이 {item}{temp} 정가에서 x % 할인\n" \
           "하여 판매하려고 한다. 손해를 보지 않고 판매하\n" \
           "려고 할 때, x의 값이 될 수 있는 가장 큰 수는?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "원가를 A원이라 하면\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "A &gt; 0이므로 양변을 A를 나누면\n" \
              "$$수식$${eq2}$$/수식$$, $$수식$${eq5}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$   ∴x ≤ $$수식$${answ}$$/수식$$\n" \
              "따라서 x의 값이 될 수 있는 가장 큰 수는 $$수식$${answ}$$/수식$$이\n" \
              "다."

    itemList = ["운동화","장난감","핸드폰", "컴퓨터","자켓"]
    item = itemList[np.random.randint(0,5)]
    f = 3

    percent = np.random.randint(10,40)
    percentt = percent/100 +1
    gcd1 = gcd(percentt * 100, 100)
    a = (percentt * 100) / gcd1
    b = 100 / gcd1
    a = int(a)
    b = int(b)
    f = a - b
    while 100 % b != 0:
        percent = np.random.randint(10, 40)
        percentt = percent / 100 + 1
        gcd1 = gcd(percentt * 100, 100)
        a = (percentt * 100) / gcd1
        b = 100 / gcd1
        a = int(a)
        b = int(b)
        f = a - b
    eq = str(round(percentt,2)) + "$$수식$$TIMES$$/수식$$ A $$수식$$TIMES$$/수식$$ (1 - $$수식$$rm x over 100$$/수식$$) ≥ A"
    eq2 = str(round(percentt,2)) + "$$수식$$TIMES$$/수식$$ (1 - $$수식$$rm x over 100$$/수식$$) ≥ 1 $$수식$$$$/수식$$"
    eq5 = str(1) + " - $$수식$$rm x over 100$$/수식$$ ≥ $$수식$${"+str(b)+"} over {"+str(a)+"}$$/수식$$" +"$$수식$$$$/수식$$"
    eq3 = " - $$수식$$rm x over 100$$/수식$$ ≥ - $$수식$${"+str(f)+"} over {"+str(a)+"}$$/수식$$" +"$$수식$$$$/수식$$"
    answ = int(100/b)
    answ = answ*f

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    temp= proc_jo(item, 4)
    stem = stem.format(temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5,percent=percent, item=item)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, eq5=eq5, eq3=eq3, answ=answ)

    return stem, answer, comment

#중2-1-2-75
def expressions212_Stem_064():
    stem = "\n가로의 길이와 세로의 길이의 비가 $$수식$${percent}$$/수식$$인 직사\n" \
           "각형 모양의 엽서를 만들려고 한다. 이 옆서의 가\n" \
           "로의 길이를 $$수식$${length}$$/수식$$ cm 이상으로 할 때, 세로의 길이\n" \
           "는 최소 몇 cm로 해야 하는가?" \
           "\n① $$수식$${x1} cm\n② {x2} cm\n③ {x3} cm\n④ {x4} cm\n⑤ {x5} cm\n   $$/수식$$"
    answer = "(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "가로의 길이와 세로의 길이의 비가 $$수식$${percent}$$/수식$${temp}므로\n" \
              "가로의 길이와 세로의 길이를 각각 $$수식$${percentt}$$/수식$$ (단,\n" \
              "x &gt; 0)이라 하면\n" \
              "이 엽서의 가로의 길이가 $$수식$${length}$$/수식$$ cm 이상이므로\n" \
              "$$수식$${eq}$$/수식$$    ∴ x ≥ $$수식$${x}$$/수식$$\n" \
              "세로의 길이는 $$수식$${width}$$/수식$$이므로 $$수식$${w_eq}$$/수식$$\n" \
              "따라서 세로의 길이는 $$수식$${fr}$$/수식$$  $$수식$${answ}$$/수식$$ (cm) 이상으로\n" \
              "해야 한다."

    a = np.random.randint(2, 6)
    b = np.random.randint(1, 5)
    while b>=a:
        a = np.random.randint(3, 6)
        b = np.random.randint(1, 5)
    temp = proc_jo(b,3)
    percent = str(a) +" : " + str(b) +"$$수식$$$$/수식$$"
    length = np.random.randint(5, 15)
    percentt = str(a) +"x, " +str(b) +"x"
    if b==1:
        percentt = str(a) + "x, x"
    eq = str(a) +"x ≥ " + str(length)
    gcd1 = gcd(a, length)
    a = int(a/gcd1)
    length = int(length/gcd1)
    x = "$$수식$${"+str(int(length))+"} over {"+str(a)+"}$$/수식$$"
    if a==1:
        x = str(int(length))
    width = str(b)+"x"
    if b==1:
        width = "x"
    cc = b*length
    gcd1 = gcd(a, cc)
    a = int(a / gcd1)
    cc = int(cc / gcd1)
    w_eq = width + " ≥ $$수식$${"+str(cc)+"} over {"+str(a)+"}$$/수식$$"
    if a==1:
        w_eq = width +" ≥ " +str(cc)
    answ = round(cc/a,1)
    if cc%a==0:
        answ = int(cc / a)
    fr = "$$수식$${"+str(cc)+"} over {"+str(a)+"}$$/수식$$ = "+"$$수식$$$$/수식$$"
    if a==1:
        fr =str(cc) +" = "+"$$수식$$$$/수식$$"
    if cc%a==0:
        fr =""
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 20)/10
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(round(k,1))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]



    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, percent=percent, length=length)
    answer = answer.format(ans=ans)
    comment = comment.format(x=x, eq=eq, temp=temp, fr=fr, percent=percent, percentt=percentt, length=length, width=width, w_eq=w_eq,answ=answ)

    return stem, answer, comment


#중2-1-2-76
def expressions212_Stem_065():
    stem = "\n도화지를 이용하여 밑변의 길이가 $$수식$${length}$$/수식$$ cm이고, 넓\n" \
           "이가 $$수식$${area}$$/수식$$ $$수식$$rm cm ^2$$/수식$$ {choooe}인 삼각형을 만들려고 할 때,\n" \
           "높이는 최소 몇 cm {choooe}이어야 하는지 구하시오."
    answer = "(답): \n" \
            "{ans} cm\n"
    comment = "(해설)\n" \
              "삼각형의 높이를 x cm라 하면\n" \
              "밑변의 길이가 $$수식$${length}$$/수식$$ cm인 삼각형의 넓이가 $$수식$${area}$$/수식$$ $$수식$$rm cm ^2$$/수식$$\n" \
              "{choooe}이므로\n" \
              "$$수식$${eq}$$/수식$$   ∴ x {ineq} $$수식$${ans}$$/수식$$\n" \
              "따라서 높이는 $$수식$${ans}$$/수식$$ cm {choooe}이어야 한다."
    chose =["이하","이상"]
    inee = [" ≤ "," ≥ "]

    d = np.random.randint(0, 2)
    choooe = chose[d]
    ineq = inee[d]

    length = np.random.randint(8, 30)
    answ = np.random.randint(8, 30)
    while length==answ or (length*answ)%2!=0:
        length = np.random.randint(8, 30)
        answ = np.random.randint(8, 30)
    area = answ*length*.5
    area = int(area)
    eq ="$$수식$$1 over 2$$/수식$$ $$수식$$TIMES$$/수식$$ " + str(length) + " $$수식$$TIMES$$/수식$$ x" + ineq + str(area) + " $$수식$$$$/수식$$ "
    stem = stem.format(length=length, area=area, choooe=choooe)
    answer = answer.format(ans=answ)
    comment = comment.format(eq=eq, length=length, choooe=choooe, ineq=ineq,  area=area, ans=answ)

    return stem, answer, comment

#중2-1-2-77
def expressions212_Stem_066():
    stem = "\n아랫변의 길이, 윗변의 길이, 높이가 각각 $$수식$${low}$$/수식$$ cm,\n" \
           "$$수식$${high}$$/수식$$ cm, $$수식$${height}$$/수식$$ cm인 사다리꼴을 만들었다. 아랫변의 길\n" \
           "이만 변화시켜 넓이가 처음 사다리꼴의 넓이보다\n" \
           "$$수식$${mul}$$/수식$$ $$수식$$rm cm ^2$$/수식$$ 이상 늘어나게 하려면 아랫변의 길이를\n" \
           "x cm 이상으로 바꾸어야 한다. x의 최솟값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "(사다리꼴의 넓이) = $$수식$$1 over 2$$/수식$$ $$수식$$TIMES$$/수식$$$$수식$$``$$/수식$$$$수식$${eq1}$$/수식$$$$수식$$``$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$$$수식$$``$$/수식$$$$수식$$TIMES$$/수식$$ (높이)이므로 처음 사다리꼴의 넓이\n" \
              "는\n" \
              "$$수식$$1 over 2$$/수식$$ $$수식$$TIMES$$/수식$$ $$수식$${ac_eq}$$/수식$$ ($$수식$$rm cm ^2$$/수식$$)\n" \
              "이때 아랫변의 길이를 x cm 이상으로 바꾸면 넓\n" \
              "이가 $$수식$${mul}$$/수식$$ $$수식$$rm cm ^2$$/수식$$ 이상 늘어나므로\n" \
              "$$수식$$1 over 2$$/수식$$ $$수식$$TIMES$$/수식$$ $$수식$${act_eq}$$/수식$$\n" \
              "∴ x ≥ $$수식$${answ}$$/수식$$\n" \
              "따라서 x의 최솟값은 $$수식$${answ}$$/수식$$이다."

    low =  np.random.randint(3, 10)
    high = np.random.randint(3, 10)
    height = np.random.randint(3, 10)
    mul =np.random.randint(2, 15)
    area = ((low+high)/2)*height
    while height%2!=0 or low==high or low==height or high==height or (area+mul)%height!=0:
        low = np.random.randint(3, 10)
        high = np.random.randint(3, 10)
        height = np.random.randint(3, 10)
        mul = np.random.randint(2, 15)
        area = ((low + high) / 2) * height
    area= int(area)
    eq1 = "$$수식$$``$$/수식$${(윗변의 길이) + (아랫" + "$$수식$$``$$/수식$$"
    eq2 = "변의 길이)}" +"$$수식$$$$/수식$$"
    ac_eq = "(" +  str(high) + " + " + str(low) + ") $$수식$$TIMES$$/수식$$ " +  str(height) + " = " + str(area) + "$$수식$$$$/수식$$"
    act_eq= "(" +  str(high) + " + " + "x) $$수식$$TIMES$$/수식$$ " +  str(height) + " ≥ " + str(area) + " + " + str(mul) + "$$수식$$$$/수식$$"
    s = height/2
    dd = int((area+ mul)/s)
    act_eq = act_eq + " ,  x + " + str(high) + " ≥ " +  str(dd)+ "$$수식$$$$/수식$$"
    answ = dd- high

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k >low:
            bb.append(round(k,1))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(low=low, high=high, height=height, mul=mul, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq1=eq1, eq2=eq2, mul=mul, ac_eq=ac_eq, act_eq=act_eq, answ=answ)

    return stem, answer, comment

#중2-1-2-80
def expressions212_Stem_067():
    stem = "\n어느 지역에서 1년 동안 배출하는 음식물 쓰레기\n" \
           "의 양은 $$수식$${ton}$$/수식$$톤이고, 음식물 쓰레기를 처리하는 비\n" \
           "용은 1톤당 $$수식$${price}$$/수식$$만 원이라고 한다. 이 지역의 1년\n" \
           "동안의 음식물 쓰레기 처리 비용이 $$수식$${total}$$/수식$$ 만 원 이\n" \
           "하가 되게 하려면 음식물 쓰레기의 양을 전체의\n" \
           "몇 % 이상 줄여야 하는지 구하시오."
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "줄여야 하는 음식물 쓰레기의 양을 전체의 x %라\n" \
              "하면\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "∴ x ≥ $$수식$${answ}$$/수식$$\n" \
              "따라서 음식물 쓰레기의 양을 전체의 $$수식$${answ}$$/수식$$ % 이상\n" \
              "줄여야 한다."


    ton =  np.random.randint(35, 70)
    price = np.random.randint(10, 30)
    total = np.random.randint(100, 500)
    while (ton*price)%100!=0 or (ton*price)<=total or (total-(ton*price))%((ton*price)/100)!=0:
        ton = np.random.randint(35, 70)
        price = np.random.randint(10, 30)
        total = np.random.randint(100, 500)
    eq = str(ton) + " $$수식$$TIMES$$/수식$$ (1 - $$수식$$rm x over 100$$/수식$$) $$수식$$TIMES$$/수식$$ " + str(price) + " ≤ " + str(total) + "$$수식$$$$/수식$$"
    aa = int((ton*price)/100)
    dd = (total-(ton*price))

    eq2 = str(ton*price) + " - " + str(aa) + "x ≤ " + str(total) + "$$수식$$$$/수식$$, "
    eq2 = eq2 + " - " + str(aa) + "x ≤ " + str(dd) + "$$수식$$$$/수식$$"
    answ = int(dd/aa) *-1

    stem = stem.format(ton=ton, price=price, total=total)
    answer = answer.format(ans=answ)
    comment = comment.format(eq=eq,eq2=eq2, answ=answ)

    return stem, answer, comment


#중2-1-2-81
def expressions212_Stem_068():
    stem = "\n일의 자리의 숫자가 십의 자리의 숫자보다 $$수식$${num1}$$/수식$$만큼\n" \
           "큰 두 자리 자연수가 있다. 이 자연수의 십의 자\n" \
           "리의 숫자와 일의 자리의 숫자를 바꾼 수는 처음\n" \
           "수의 $$수식$${mul}$$/수식$$배에 $$수식$${add}$$/수식$${temp} 더한 수보다 크다고 할 때, 처음\n" \
           "자연수 중 가장 큰 자연수를 구하시오."
    answer = "\n(답): \n" \
            "{ans} \n"
    comment = "(해설)\n" \
              "구하는 자연수의 십의 자리의 숫자를 x라 하면\n" \
              "일의 자리의 숫자는 x + $$수식$${num1}$$/수식$$이므로\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$, $$수식$${eq3}$$/수식$$\n" \
              "∴ x &lt; $$수식$${ans11}$$/수식$$ $$수식$${deci}$$/수식$$\n" \
              "이때 x는 자연수이므로 x는 $$수식$${list}$$/수식$$이다.\n" \
              "따라서 구하는 자연수는 $$수식$${ans}$$/수식$$이다."

    num1 = np.random.randint(1, 6)
    mul = np.random.randint(2, 4)
    add = np.random.randint(1, 10)
    while num1==add or ((num1*2+add)-(num1*10))>=0:
        num1 = np.random.randint(1, 6)
        mul = np.random.randint(2, 4)
        add = np.random.randint(1, 10)
    temp = proc_jo(add,4)
    eq = "10(x + " +  str(num1) +") + x &gt; " + str(mul) +"{10x + (x + " + str(num1)+")} + " +  str(add)+ "$$수식$$$$/수식$$"
    eq2 = "11x + " + str(num1*10) + " &gt; 22x + " + str(num1*2+add)+ "$$수식$$$$/수식$$"
    eq3 = "-11x &gt; " + str((num1*2+add)-(num1*10))
    aa = (num1*2+add)-(num1*10)
    bb = -11
    gcd1 = gcd(abs(aa),abs(bb))
    aa = int(aa/gcd1)*-1
    bb = int(bb/gcd1)*-1

    ans11 = "$$수식$${"+str(aa)+"} over {"+str(bb)+"}$$/수식$$"+ "$$수식$$$$/수식$$"
    deci = " = " + str(round(aa/bb,2)) + "$$수식$$CDOTS$$/수식$$"
    if bb==1:
        ans11 = str(aa)
    if aa%bb==0:
        deci = ""

    cc = int(aa/bb)
    list =""
    for i in range(1, cc):
        list = list + str(i) +", "
    list = list + str(cc)+ "$$수식$$$$/수식$$"
    ans = str(cc) + str(cc+num1)


    stem = stem.format(num1=num1, mul=mul, add=add, temp=temp)
    answer = answer.format(ans=ans)
    comment = comment.format(ans11=ans11, ans=ans, list=list, deci=deci, eq=eq, eq2=eq2, eq3=eq3,num1=num1)

    return stem, answer, comment

#중2-1-2-82

def expressions212_Stem_069():
    stem = "\n형은 $$수식$${num1}$$/수식$$ 개, 동생은 $$수식$${num2}$$/수식$$ 개의 초콜릿을 각자의 상\n" \
           "자에 가지고 있다. 형이 자신의 상자에서 한 번에\n" \
           "$$수식$${pick}$$/수식$$개의 초콜릿을 꺼내 먹는 동시에 동생은 자신의\n" \
           "상자에서 한 번에 $$수식$${pick2}$$/수식$$개의 초콜릿을 꺼내 한 개는\n" \
           "자신이 먹고 다른 한 개는 형의 상자에 넣는다고\n" \
           "한다. 동생이 가지고 있는 초콜릿의 개수가 형이\n" \
           "가지고 있는 초콜릿의 개수의 $$수식$${mul}$$/수식$$배보다 처음으로\n" \
           "많아지는 것은 형이 초콜릿을 몇 번째 꺼내 먹었\n" \
           "을 때인지 구하시오."
    answer = "\n(답): \n" \
            "{ans} 번째\n"
    comment = "(해설)\n" \
              "형이 초콜릿을 x번 꺼내 먹었다고 하면\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$\n" \
              "$$수식$${eq4}$$/수식$$   ∴ x &gt; $$수식$${ans11}$$/수식$$\n" \
              "따라서 동생이 가지고 있는 초콜릿의 개수가 형이\n" \
              "가지고 있는 초콜릿의 개수의 $$수식$${mul}$$/수식$$배보다 처음으로\n" \
              "많아지는 것은 형이 초콜릿을 $$수식$${ans}$$/수식$$번째 꺼내 먹었을\n" \
              "때이다."

    num1 = np.random.randint(9, 20)*10
    num2 = np.random.randint(9, 20)*10
    pick = np.random.randint(2, 10)
    pick2 = np.random.randint(1, 10)
    mul =np.random.randint(2, 5)
    while (-1*((pick-1)*mul)+pick2)>=0 or (num2 -mul*num1)%(-1*((pick-1)*mul)+pick2)!=0:
        num1 = np.random.randint(9, 20) * 10
        num2 = np.random.randint(9, 20) * 10
        pick = np.random.randint(2, 10)
        pick2 = np.random.randint(1, 10)
        mul = np.random.randint(2, 5)
    eq=str(mul) +"{(" + str(num1) +" - " + str(pick) + "x) + x} &lt; "
    if pick==1:
        eq = str(mul) + "{(" + str(num1) + " - x) + x} &lt; "
    eq2=str(mul) +"$$수식$$$$/수식$$(" + str(num1) +" - " + str(pick-1) + "x) &lt; "
    if pick-1==1:
        eq2 = str(mul) + "$$수식$$$$/수식$$(" + str(num1) + " - x) &lt; "
    eq3 = str(mul*num1) + " - " + str((pick-1)*mul) +"x &lt; "
    if pick2!=1:
        eq = eq + str(num2) + " - " + str(pick2) + "x" +"$$수식$$$$/수식$$"
        eq2 = eq2 + str(num2) + " - " + str(pick2) + "x"+"$$수식$$$$/수식$$"
        eq3 = eq3 + str(num2) + " - " + str(pick2) + "x"+"$$수식$$$$/수식$$"
    else:
        eq =eq + str(num2) + " - x" + "$$수식$$$$/수식$$"
        eq2 = eq2 + str(num2) + " - x" + "$$수식$$$$/수식$$"
        eq3 = eq3 + str(num2) + " - x" + "$$수식$$$$/수식$$"
    eq4 = str(-1*((pick-1)*mul)+pick2) + "x &lt; " + str(num2 -mul*num1)+"$$수식$$$$/수식$$"
    ans11 = (num2 -mul*num1)/(-1*((pick-1)*mul)+pick2)
    ans11 = int(ans11)
    ans = ans11+1
    while ans>=num1 or ans>=num2:
        num1 = np.random.randint(9, 20) * 10
        num2 = np.random.randint(9, 20) * 10
        pick = np.random.randint(2, 10)
        pick2 = np.random.randint(1, 10)
        mul = np.random.randint(2, 5)
        while (-1 * ((pick - 1) * mul) + pick2) >= 0 or (num2 - mul * num1) % (-1 * ((pick - 1) * mul) + pick2) != 0:
            num1 = np.random.randint(9, 20) * 10
            num2 = np.random.randint(9, 20) * 10
            pick = np.random.randint(2, 10)
            pick2 = np.random.randint(1, 10)
            mul = np.random.randint(2, 5)
        eq = str(mul) + "{(" + str(num1) + " - " + str(pick) + "x) + x} &lt; "
        if pick == 1:
            eq = str(mul) + "{(" + str(num1) + " - x) + x} &lt; "
        eq2 = str(mul) + "$$수식$$$$/수식$$(" + str(num1) + " - " + str(pick - 1) + "x) &lt; "
        if pick - 1 == 1:
            eq2 = str(mul) + "$$수식$$$$/수식$$(" + str(num1) + " - x) &lt; "
        eq3 = str(mul * num1) + " - " + str((pick - 1) * mul) + "x &lt; "
        if pick2 != 1:
            eq = eq + str(num2) + " - " + str(pick2) + "x" + "$$수식$$$$/수식$$"
            eq2 = eq2 + str(num2) + " - " + str(pick2) + "x" + "$$수식$$$$/수식$$"
            eq3 = eq3 + str(num2) + " - " + str(pick2) + "x" + "$$수식$$$$/수식$$"
        else:
            eq = eq + str(num2) + " - x" + "$$수식$$$$/수식$$"
            eq2 = eq2 + str(num2) + " - x" + "$$수식$$$$/수식$$"
            eq3 = eq3 + str(num2) + " - x" + "$$수식$$$$/수식$$"
        eq4 = str(-1 * ((pick - 1) * mul) + pick2) + "x &lt; " + str(num2 - mul * num1) + "$$수식$$$$/수식$$"
        ans11 = (num2 - mul * num1) / (-1 * ((pick - 1) * mul) + pick2)
        ans11 = int(ans11)
        ans = ans11 + 1

    stem = stem.format(num1=num1, num2=num2, pick=pick, pick2=pick2, mul=mul)
    answer = answer.format(ans=ans)
    comment = comment.format(ans11=ans11, ans=ans, eq=eq, eq2=eq2, eq3=eq3, eq4=eq4,mul=mul )

    return stem, answer, comment


#중2-1-2-83
def expressions212_Stem_070():
    stem = "\n어느 도서 대여점에서 책을 빌리는 데 기본 $$수식$${num1}$$/수식$$권에\n" \
           "$$수식$${price}$$/수식$$ 원을 받고, $$수식$${num1}$$/수식$$권을 초과하면 $$수식$${num2}$$/수식$$권째부터는 한\n" \
           "권당 $$수식$${price2}$$/수식$$ 원씩을 받는다. 전체적으로 빌리는 값이\n" \
           "한 권당 $$수식$${total}$$/수식$$ 원 이하가 되게 하려면 책을 최소 몇\n" \
           "권 이상 빌려야 하는가?\n" \
           "\n① $$수식$${x1}권\n② {x2}권\n③ {x3}권\n④ {x4}권\n⑤ {x5}권\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "책을 x권 빌린다고 하면(단, x &gt; $$수식$${num1}$$/수식$$)\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "∴ x ≥ $$수식$${answ}$$/수식$$\n" \
              "따라서 최소 $$수식$${answ}$$/수식$$권 이상 빌려야 한다."

    num1 = np.random.randint(2, 10)
    num2 = num1+1
    price = np.random.randint(3, 8)*1000
    price2 = np.random.randint(3, 8)*100
    total = np.random.randint(3, 8)*100
    while price2>=total or((price2*num1)-price)%(price2-total)!=0 or ((price2*num1)-price)/(price2-total)<=0:
        num1 = np.random.randint(2, 10)
        num2 = num1 + 1
        price = np.random.randint(3, 8) * 1000
        price2 = np.random.randint(3, 8) * 100
        total = np.random.randint(3, 8) * 100

    eq = str(price) + " + " + str(price2) +"(x - " + str(num1) +") ≤ " +  str(total) +"x" + "$$수식$$$$/수식$$,"
    eq2 =   str(price2-total) +"x" + " ≤ " + str((price2*num1)-price)
    answ = ((price2*num1)-price)/(price2-total)
    answ = int(answ)

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k!=0:
            bb.append(round(k, 1))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(x1=x1, x2=x2,x3=x3,x4=x4,x5=x5,num1=num1, price=price, price2=price2, total=total, num2=num2)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, answ=answ, num1=num1)

    return stem, answer, comment



#중2-1-2-84
def expressions212_Stem_071():
    stem = "\n{name1}네 학교에서는 불우 이웃 돕기 기금을 마련하\n" \
           "기 위해 $$수식$${day}$$/수식$$일 동안 $$수식$${price}$$/수식$$ 원짜리 {item}{temp} 팔기로 하였\n" \
           "다. 판매가의 $$수식$${percent}$$/수식$$ %가 원가이고 원가를 제외한 전\n" \
           "액을 기금으로 사용하기로 하였다. 기금의 목표액\n" \
           "이 $$수식$${goal}$$/수식$$만 원 이상일 때, 하루 평균 몇 개 이상의\n" \
           "{item}{temp} 팔아야 하는가?" \
           "\n① $$수식$${x1}개\n② {x2}개\n③ {x3}개\n④ {x4}개\n⑤ {x5}개\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "하루 동안 파는 {item}의 평균 개수를 x라 하면\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "∴ x ≥ $$수식$${fra}$$/수식$$ $$수식$${deci}$$/수식$$\n" \
              "따라서 하루 평균 {answ}개 이상의$$수식$$``$$/수식$${item}$$수식$$``$$/수식$${temp}$$수식$$``$$/수식$$팔아야 한\n" \
              "다."

    nameList = ["경희", "민철이", "수진이", "철수","영대","준호"]
    o = np.random.randint(0, 6)
    name1 = nameList[o]
    itemList =["빵","팽이","장난감","떡","편지지"]
    o = np.random.randint(0, 5)
    item = itemList[o]
    temp = proc_jo(item, 4)

    price = np.random.randint(1, 6) * 1000
    day = np.random.randint(1, 7)
    percent = np.random.randint(1, 5)*10
    goal = np.random.randint(4, 11)*10
    eq = str(price) + " $$수식$$TIMES$$/수식$$ " +str(percent/100) + " $$수식$$TIMES$$/수식$$ x" + " $$수식$$TIMES$$/수식$$ "+ str(day) + " ≥ " +  str(goal*10000) + "$$수식$$$$/수식$$"
    aa = price*(percent/100)*day
    bb= goal*10000
    gcd1 = gcd(aa,bb)
    aa = int(aa/gcd1)
    bb = int(bb/gcd1)
    fra = "$$수식$${"+str(bb)+"} over {"+str(aa)+"}$$/수식$$" +"$$수식$$$$/수식$$"
    deci = " = " + str(round(bb/aa,1)) + "$$수식$$CDOTS$$/수식$$" + "$$수식$$``$$/수식$$"
    answ = int(bb / aa)+1
    if aa==1:
        fra = str(bb)
        deci=""
        answ = int(bb/aa)

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0:
            bb.append(round(k, 1))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(item=item,x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, price=price, goal=goal, percent=percent, day=day, temp=temp, name1=name1)
    answer = answer.format(ans=ans)
    comment = comment.format(temp=temp, item=item, eq=eq,answ=answ, fra=fra, deci=deci)

    return stem, answer, comment

#중2-1-2-85
def expressions212_Stem_072():
    stem = "\n어느 {location}의 입장료는 어른이 $$수식$${price}$$/수식$$ 원, 어린이\n" \
           "가 $$수식$${price2}$$/수식$$ 원이고 어른이 $$수식$${adult}$$/수식$$명 이상일 때 어른 요금\n" \
           "의 $$수식$${percent}$$/수식$$ %를 할인해 준다고 한다. 어른이 $$수식$${adult}$$/수식$$명 미\n" \
           "만이면서 어른과 어린이를 합하여 $$수식$${pop}$$/수식$$명이 입장하\n" \
           "려고 할 때, 어른이 몇 명 이상하면 어른 $$수식$${adult}$$/수식$$명의\n" \
           "입장료를 내는 것이 유리한가?" \
           "\n① $$수식$${x1}명\n② {x2}명\n③ {x3}명\n④ {x4}명\n⑤ {x5}명\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "입장하는 어른을 x명이라 하면 어린이는\n" \
              "($$수식$${pop}$$/수식$$ - x)명이므로\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$\n" \
              "∴ x &gt; $$수식$${ans11}$$/수식$$\n" \
              "따라서 어른이 $$수식$${answ}$$/수식$$명 이상이면 어른 $$수식$${adult}$$/수식$$명의 입장\n" \
              "료를 내는 것이 유리하다."

    locationList =["미술관","박물관","놀이동산"]
    location =  locationList[np.random.randint(0, 3)]
    price = np.random.randint(5, 10)*1000
    price2 = np.random.randint(1, 5)*1000
    adult = np.random.randint(10, 30)
    percent = np.random.randint(10, 30)
    pop = np.random.randint(20, 50)
    aa =(price*(1-(percent/100))*adult) +(price2*(pop-adult))
    bb= (price2*pop)-aa
    cc = (price-price2)*-1
    while bb%cc!=0 or price2>=price or bb>0:
        price = np.random.randint(5, 10) * 1000
        price2 = np.random.randint(1, 5) * 1000
        adult = np.random.randint(10, 30)
        percent = np.random.randint(10, 30)
        pop = np.random.randint(20, 50)
        aa = (price * (1 - (percent / 100)) * adult) + (price2 * (pop - adult))
        aa = int(aa)
        bb = (price2 * pop) - aa
        cc = (price - price2) * -1

    eq = str(price) + " $$수식$$TIMES$$/수식$$ " + str(round(1-(percent/100),2)) + " $$수식$$TIMES$$/수식$$ " + str(adult) + " + " + str(price2) + " $$수식$$TIMES$$/수식$$ " + str(pop-adult)
    eq = eq + " &lt; " + str(price) + "x + " + str(price2) +"(" + str(pop) +" - x)"
    eq2 = str(aa) + " &lt; " + str(price-price2) + "x + " + str(price2*pop)
    eq3 = str(cc) +"x &lt; " + str(bb)
    ans11 = int(bb/cc)
    answ = ans11+1

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0:
            bb.append(round(k, 1))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format( x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, location=location, price=price, price2=price2, adult=adult, pop=pop,percent=percent,)
    answer = answer.format(ans=ans)
    comment = comment.format(pop=pop, adult=adult, eq=eq, eq2=eq2, eq3=eq3, ans11=ans11, answ=answ)

    return stem, answer, comment

#중2-1-2-86
def expressions212_Stem_073():
    stem = "\n어떤 일을 끝마치는데 남자 한 명이 하면 $$수식$${day}$$/수식$$일, 여\n" \
           "자 한 명이 하면 $$수식$${day2}$$/수식$$일이 걸린다고 한다. 이 일을\n" \
           "남녀 $$수식$${together}$$/수식$$명이 함께하여 하루 이내에 끝내려고 한다\n" \
           "면 남자는 최소 몇 명이 필요하겠는가?" \
           "\n① $$수식$${x1}명\n② {x2}명\n③ {x3}명\n④ {x4}명\n⑤ {x5}명\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "어떤 일의 양을 1이라 하면 그 일을 남자 1명, 여\n" \
              "자 1명이 하는데 각각 $$수식$${day}$$/수식$$일, $$수식$${day2}$$/수식$$일 만에 끝나므로\n" \
              "하루에 하는 일의 양은 각각 $$수식$$1 over {day}$$/수식$$, $$수식$$1 over {day2}$$/수식$$이다.\n" \
              "이 일을 남녀 $$수식$${together}$$/수식$$명이 함께하여 하루 이내에 끝내\n" \
              "려고 하므로\n" \
              "남자 수를 x명이라 하면 여자 수는 ($$수식$${together}$$/수식$$ - x)명이\n" \
              "고, 남자 x명이 하루에 하는 일의 양은 $$수식$$1 over {day}$$/수식$$x, 여\n" \
              "자 ($$수식$${together}$$/수식$$ - x)명이 하루에 하는 일의 양은\n" \
              "$$수식$$1 over {day2}$$/수식$$($$수식$${together}$$/수식$$ - x)이다.\n" \
              "$$수식$$1 over {day}$$/수식$$x + $$수식$$1 over {day2}$$/수식$$($$수식$${together}$$/수식$$ - x) ≥ 1에서\n" \
              "$$수식$${eq}$$/수식$$이므로\n" \
              "$$수식$${eq2}$$/수식$$   ∴ x ≥ $$수식$${answ}$$/수식$$\n" \
              "따라서 남자는 최소 $$수식$${answ}$$/수식$$명이 필요하다."

    day = np.random.randint(5, 20)
    day2 = np.random.randint(5, 20)
    while day==day2:
        day2 = np.random.randint(5, 20)
    together = np.random.randint(5, 20)
    lcm1 = lcm(day, day2)
    a = int(lcm1/day)
    b = int(lcm1/day2)
    while a<=b or (lcm1-(together*b))<=0 or  (lcm1-(together*b))%(a-b)!=0 or (lcm1-(together*b))/(a-b)>=together:
        day = np.random.randint(5, 20)
        day2 = np.random.randint(5, 20)
        while day == day2:
            day2 = np.random.randint(5, 20)
        together = np.random.randint(5, 20)
        lcm1 = lcm(day, day2)
        a = int(lcm1 / day)
        b = int(lcm1 / day2)
    eq = str(a)+"x + " +  str(b) + "(" + str(together) +" - x) ≥ "+str(lcm1) +"$$수식$$$$/수식$$"
    eq2 = str(a)+"x + " + str(together*b) +" - " +str(b) +"x ≥ "+str(lcm1)+"$$수식$$$$/수식$$"
    answ = int((lcm1-(together*b))/(b-a))*-1
    bb=[]
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0 and k<together:
            bb.append(round(k, 1))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, day=day, day2=day2, together=together)
    answer = answer.format(ans=ans)
    comment = comment.format(day=day, day2=day2, together=together, eq=eq,eq2=eq2, answ=answ)

    return stem, answer, comment

#중2-1-2-87
def expressions212_Stem_074():
    stem = "\n배식처가 하나인 어느 학교 학생 식당에서 $$수식$${together}$$/수식$$명이\n" \
           "줄을 서서 배식을 기다리고 있고, 매분 $$수식$${min}$$/수식$$명씩 다\n" \
           "른 반 학생들이 줄을 선다고 한다. $$수식$${time}$$/수식$$분 만에 줄\n" \
           "서 있는 학생들이 모두 배식을 받는다고 할 때, 만\n" \
           "약 $$수식$${que}$$/수식$$분 만에 줄 서는 학생들이 없도록 하려면 배\n" \
           "식처가 최소 몇 곳 이상 있어야 하는지 구하시오."
    answer = "\n(답): \n" \
            "{ans} 곳\n"
    comment = "(해설)\n" \
              "배식처 하나에서 1분에 배식이 가능한 학생의 수\n" \
              "를 k명이라 하면\n" \
              "처음에 $$수식$${together}$$/수식$$명이 줄을 서서 배식을 기다리고 있고,\n" \
              "매분 $$수식$${min}$$/수식$$명의 새로운 학생이 줄을 선다고 하는데\n" \
              "$$수식$${time}$$/수식$$분 만에 줄 서는 사람이 모두 배식을 받으므로\n" \
              "$$수식$${eq}$$/수식$$      ∴ k = $$수식$${ans11}$$/수식$$\n" \
              "배식처의 개수를 x개라 하면\n" \
              "$$수식$${que}$$/수식$$분 동안에 배식 받을 수 있는 학생의 수는\n" \
              "x $$수식$$TIMES$$/수식$$ $$수식$${que}$$/수식$$ $$수식$$TIMES$$/수식$$ $$수식$${ans11}$$/수식$$ = $$수식$${ans12}$$/수식$$x (명)\n" \
              "$$수식$${que}$$/수식$$분간 배식 받을 학생의 수는 이미 줄 서 있는\n" \
              "$$수식$${together}$$/수식$$명의 학생과 $$수식$${que}$$/수식$$분 동안 새로 줄 서는 학생의\n" \
              "수를 합한 것이므로 $$수식$${together}$$/수식$$ + $$수식$${min}$$/수식$$ $$수식$$TIMES$$/수식$$ $$수식$${que}$$/수식$$ = $$수식$${ans13}$$/수식$$ (명)\n" \
              "$$수식$${que}$$/수식$$분 만에 줄 서는 학생이 없으려면 10분 동안\n" \
              "배식 받을 수 잇는 학생의 수가 $$수식$${que}$$/수식$$분 동안 줄 서\n" \
              "는 학생의 수보다 많거나 같으면 되므로\n" \
              "$$수식$${eq2}$$/수식$$   ∴ x ≥ $$수식$${fra}$$/수식$$\n" \
              "따라서 $$수식$${fra}$$/수식$$ {deci} 이므로 배식처는 최소 $$수식$${ans}$$/수식$$곳\n" \
              "이상이어야 한다."

    together = np.random.randint(30,90)
    min = np.random.randint(10,40)
    time = np.random.randint(10,40)
    que = np.random.randint(10,40)
    while (together+(min*time))%time!=0:
        together = np.random.randint(30, 90)
        min = np.random.randint(10, 40)
        time = np.random.randint(10, 40)
        que = np.random.randint(10, 40)
    eq = str(together) + " + " +  str(min) + " $$수식$$TIMES$$/수식$$ " + str(time) + " = k " +"$$수식$$TIMES$$/수식$$ " + str(min) +"$$수식$$$$/수식$$"
    ans11 = int((together+(min*time))/time)
    ans12 = que*ans11
    ans13 = together +(min*que)
    eq2 =  str(ans12) +"x ≥ " + str(ans13) + "$$수식$$$$/수식$$"
    gcd1 = gcd(ans12, ans13)
    aa = int(ans12/gcd1)
    bb = int(ans13/gcd1)
    fra = "$$수식$${"+str(bb)+"} over {"+str(aa)+"}$$/수식$$"
    deci = " = " + str(round(bb/aa,2)) + "$$수식$$CDOTS$$/수식$$"
    ans = int(bb / aa) + 1
    if aa==1:
        fra = str(bb)
        deci = ""
        ans = int(bb/aa)
    while ans<=1:
        together = np.random.randint(30, 90)
        min = np.random.randint(10, 40)
        time = np.random.randint(10, 40)
        que = np.random.randint(10, 40)
        while (together + (min * time)) % time != 0:
            together = np.random.randint(30, 90)
            min = np.random.randint(10, 40)
            time = np.random.randint(10, 40)
            que = np.random.randint(10, 40)
        eq = str(together) + " + " + str(min) + " $$수식$$TIMES$$/수식$$ " + str(
            time) + " = k " + "$$수식$$TIMES$$/수식$$ " + str(min) + "$$수식$$$$/수식$$"
        ans11 = int((together + (min * time)) / time)
        ans12 = que * ans11
        ans13 = together + (min * que)
        eq2 = str(ans12) + "x ≥ " + str(ans13) + "$$수식$$$$/수식$$"
        gcd1 = gcd(ans12, ans13)
        aa = int(ans12 / gcd1)
        bb = int(ans13 / gcd1)
        fra = "$$수식$${" + str(bb) + "} over {" + str(aa) + "}$$/수식$$"
        deci = " = " + str(round(bb / aa, 2)) + "$$수식$$CDOTS$$/수식$$"
        ans = int(bb / aa) + 1
        if aa == 1:
            fra = str(bb)
            deci = ""
            ans = int(bb / aa)
    stem = stem.format(min=min, que=que,time=time, together=together)
    answer = answer.format(ans=ans)
    comment = comment.format(fra=fra, deci=deci, min=min, que=que,time=time, together=together, eq=eq, eq2=eq2, ans=ans, ans11=ans11, ans12=ans12, ans13=ans13)

    return stem, answer, comment

#중2-1-2-89
def expressions212_Stem_075():
    stem = "\n$$수식$${per}$$/수식$$ %의 {liquid}{temp} $$수식$${per2}$$/수식$$ %의 {liquid}{temp2} 섞어서 농도가\n" \
           "$$수식$${que}$$/수식$$ %이상인 {liquid} $$수식$${weight}$$/수식$$ g을 만들려고 할 때,\n" \
           "$$수식$${per}$$/수식$$ %의 {liquid}{temp3} 최대 몇 g까지 섞을 수 있는가?" \
           "\n① $$수식$${x1}g\n② {x2}g\n③ {x3}g\n④ {x4}g\n⑤ {x5}g\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${per}$$/수식$$ %의 {liquid}{temp2} x g 섞었다고 하면 $$수식$${per2}$$/수식$$ %의 {liquid}\n" \
              "{temp3} ($$수식$${weight}$$/수식$$ - x) g 섞어야 하므로\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$     ∴ x ≤ $$수식$${answ}$$/수식$$\n" \
              "따라서 $$수식$${per}$$/수식$$ %의 {liquid}{temp3} 최대 $$수식$${answ}$$/수식$$ g까지 섞을 수\n" \
              "있다. "

    liquids=["설탕물","소금물","알코올","화학물"]
    liquid = liquids[np.random.randint(0,4)]
    temp = proc_jo(liquid,2)
    temp2 = proc_jo(liquid, 4)
    temp3 = proc_jo(liquid, -1)

    per = np.random.randint(3,10)
    per2 = np.random.randint(6,20)
    que = np.random.randint(6,20)
    weight = np.random.randint(3,10)*100
    while per>=per2 or per2==que or per==que or ((int((weight)*que))-(weight*per2))>=0 or((int((weight)*que))-(weight*per2))%(per-per2)!=0 or weight-5<=abs(int(((int((weight)*que))-(weight*per2))/(per-per2))):
        per = np.random.randint(3, 10)
        per2 = np.random.randint(6, 20)
        que = np.random.randint(6, 20)
        weight = np.random.randint(3, 10) * 100

    eq = "$$수식$${"+str(per)+"} over 100$$/수식$$ $$수식$$TIMES$$/수식$$ x + $$수식$${"+str(per2)+"} over 100$$/수식$$ $$수식$$TIMES$$/수식$$ ($$수식$${"+str(weight)+"}$$/수식$$   - x)"
    eq = eq + " ≥ $$수식$${"+str(que)+"} over 100$$/수식$$ $$수식$$TIMES$$/수식$$ " +  str(weight)
    eq2 =  str(per)+"x + " + str(weight*per2) + " - " + str(per2) +"x ≥ " + str(int((weight)*que)) +"$$수식$$$$/수식$$"
    eq3 = str(per-per2) + "x ≥ " + str((int((weight)*que))-(weight*per2))+"$$수식$$$$/수식$$"
    answ = abs(int(((int((weight)*que))-(weight*per2))/(per-per2)))

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0 and k<weight:
            bb.append(round(k, 1))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(liquid=liquid, temp=temp, temp2=temp2, temp3=temp3, per=per, per2=per2,  weight=weight, que=que, x1=x1,x2=x2,x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(liquid=liquid, temp=temp, temp2=temp2, temp3=temp3, weight=weight, per=per,per2=per2, eq=eq, eq2=eq2, eq3=eq3, answ=answ)

    return stem, answer, comment

#중2-1-2-90
def expressions212_Stem_076():
    stem = "\n{name1}가 집에서 $$수식$${dist}$$/수식$$ km 떨어진 삼촌 댁까지 가는데\n" \
           "처음에는 자전거를 타고 시속 $$수식$${speed}$$/수식$$ km로 달리다가\n" \
           "도중에 자전거가 고장 나서 그 지점에서부터 시속\n" \
           "$$수식$${speed2}$$/수식$$ km로 걸어갔더니 $$수식$${hour}$$/수식$$시간 이내에 도착하였다. 자\n" \
           "전거가 고장 난 지점은 집에서 몇 km 이상 떨어\n" \
           "진 곳인가?" \
           "\n① $$수식$${x1} km\n② {x2} km\n③ {x3} km\n④ {x4} km\n⑤ {x5} km\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "자전거가 고장 난 지점을 집에서 x km 떨어진 곳\n" \
              "이라 하면 그 지점에서 삼촌 댁까지의 거리는\n" \
              "($$수식$${dist}$$/수식$$ - x) km이므로\n" \
              "$$수식$${eq}$$/수식$$, $$수식$${eq2}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$, $$수식$${eq4}$$/수식$$\n" \
              "∴ x ≥ $$수식$${answ}$$/수식$$\n" \
              "따라서 자전거가 고장 난 지점은 집에서 $$수식$${answ}$$/수식$$ km\n" \
              "이상 떨어진 곳이다."

    nameList = ["경희", "민철이", "수진이", "철수", "영대", "준호","현호"]
    o = np.random.randint(0, 7)
    name1 = nameList[o]
    dist =np.random.randint(10, 35)
    speed = np.random.randint(10, 20)
    speed2 = np.random.randint(2, 10)
    hour =np.random.randint(1, 4)

    lcm1 = lcm(speed, speed2)
    a = int(lcm1/speed)
    b = int(lcm1/speed2)
    c = lcm1*hour
    while (c-(b*dist))>=0 or(a-b)>=0 or (c-(b*dist))%(a-b)!=0 or (c-(b*dist))/(a-b)>=dist:
        dist = np.random.randint(10, 35)
        speed = np.random.randint(10, 20)
        speed2 = np.random.randint(2, 10)
        hour = np.random.randint(1, 4)
        lcm1 = lcm(speed, speed2)
        a = int(lcm1 / speed)
        b = int(lcm1 / speed2)
        c = lcm1 * hour
    eq = "$$수식$$rm x over {" + str(speed) + "}$$/수식$$ + $$수식$${" + str(dist) + " - x} over {" + str(speed2) + "}$$/수식$$    ≤ " + str(hour) + "$$수식$$$$/수식$$"
    eq2 = str(a) +"x + " + str(b) +"(" + str(dist) + " - x) ≤ " + str(c) + "$$수식$$$$/수식$$"
    eq3 = str(a-b) +"x + " + str(b*dist) + " ≤ " + str(c) + "$$수식$$$$/수식$$"
    eq4 =str(a-b) +"x ≤ " + str(c-(b*dist))  +  "$$수식$$$$/수식$$"
    answ = int((c-(b*dist))/(a-b))
    if a==1:
        eq2 = "x + " + str(b) + "(" + str(dist) + " - x) ≤ " + str(c) + "$$수식$$$$/수식$$"
    if a-b==-1:
        eq3 = "-x + " + str(b * dist) + " ≤ " + str(c) + "$$수식$$$$/수식$$"
        eq4 = "-x ≤ " + str(c - (b * dist)) + "$$수식$$$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 20)*.5
        u = np.random.randint(0, 2)
        if k%1==0:
            k = int(k)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0 and k<dist:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(name1=name1,dist=dist, speed=speed, speed2=speed2,hour=hour, x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, eq=eq, eq2=eq2, eq3=eq3, eq4=eq4,dist=dist)

    return stem, answer, comment

#중2-1-2-92
def expressions212_Stem_077():
    stem = "\n등산을 하는데 올라갈 때는 시속 $$수식$${speed}$$/수식$$ km로 걷고,\n" \
           "$$수식$${breake}$$/수식$$분 쉬다가 내려올 때에는 같은 길을 시속\n" \
           "$$수식$${dist}$$/수식$$km로 걸어서 $$수식$${hour}$$/수식$$시간 $$수식$${min}$$/수식$$분 이내로 등산을 마치\n" \
           "려고 한다. 이때 최대 몇 km가지 올라갔다 내려\n" \
           "올 수 있는가?" \
           "\n① $$수식$${x1} km\n② {x2} km\n③ {x3} km\n④ {x4} km\n⑤ {x5} km\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x km까지 올라갔다 내려온다고 하면\n" \
              "$$수식$${eq}$$/수식$$, $$수식$${eq2}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$      ∴ x ≤ $$수식$${answ}$$/수식$$\n" \
              "따라서 최대 $$수식$${answ}$$/수식$$ km까지 올라갔다 내려올 수 있\n" \
              "다."

    speed=np.random.randint(1, 7)
    breake = np.random.randint(1, 5)*10
    dist = np.random.randint(5, 10)
    hour = np.random.randint(1, 5)
    min = np.random.randint(1, 6)*10
    a = hour*60+min
    b=60
    gcd1 = gcd(a, 60)
    a = int(a/gcd1)
    b = int(b/gcd1)
    lcm1 = lcm(lcm(lcm(60, speed), b), dist)
    aa = int(lcm1/speed) +  int(lcm1/dist)
    bb = int((lcm1/60)*breake)
    cc = int((a/b)*lcm1)
    while cc-bb<=0 or ((cc-bb)*10)%aa!=0:
        speed = np.random.randint(1, 7)
        breake = np.random.randint(1, 5) * 10
        dist = np.random.randint(5, 10)
        hour = np.random.randint(1, 5)
        min = np.random.randint(1, 6) * 10
        a = hour * 60 + min
        gcd1 = gcd(a, 60)
        a = int(a / gcd1)
        b = int(60/ gcd1)
        lcm1 = lcm(lcm(lcm(60, speed), b), dist)
        aa = int(lcm1 / speed) + int(lcm1 / dist)
        bb = int((lcm1 / 60) * breake)
        cc = int((a / b) * lcm1)
    eq = "$$수식$$rm x over {" + str(speed) + "}$$/수식$$ + $$수식$${" + str(breake) + "} over 60$$/수식$$ + $$수식$$rm x over {" + str(dist) + "}$$/수식$$" +"$$수식$$$$/수식$$"
    eq = eq + " ≤ " + "$$수식$${" + str(a) + "} over {" + str(b) + "}$$/수식$$"+"$$수식$$$$/수식$$"
    eq2 = str(aa)+"x + " + str(bb) +" ≤ " + str(cc)+"$$수식$$$$/수식$$"
    eq3 = str(aa)+"x ≤ " +  str(cc-bb)+"$$수식$$$$/수식$$"
    answ = (cc-bb)/aa
    if (cc-bb)%aa==0:
        answ = int(answ)

    bb = []
    dd=[]
    while len(bb) < 4:
        k = np.random.randint(1, 30)/10
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k % 1 == 0:
            k = int(k)
        if k not in dd and k != answ and k != 0:
            dd.append(k)
            bb.append(round(k,1))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(speed=speed, dist=dist, min=min, breake=breake, hour=hour, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, eq=eq, eq2=eq2, eq3=eq3)

    return stem, answer, comment


#중2-1-2-96
def expressions212_Stem_078():
    stem = "\n$$수식$${per}$$/수식$$ %의 {liquid} $$수식$${weight}$$/수식$$ g이 있다. 이 {liquid}에서 물을\n" \
           "증발시켜서 농도가 $$수식$${per2}$$/수식$$ % 이상이 되게 하려고 할\n" \
           "때, 최소 몇 g의 물을 증발시켜야 하는가?" \
           "\n① $$수식$${x1}g\n② {x2}g\n③ {x3}g\n④ {x4}g\n⑤ {x5}g\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "물을 x g 증발시킨다고 하면\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "∴ x ≥ $$수식$${answ}$$/수식$$\n" \
              "따라서 최소 $$수식$${answ}$$/수식$$ g의 물을 증발시켜야 한다."

    liquids = ["설탕물", "소금물", "알코올", "화학물"]
    liquid = liquids[np.random.randint(0, 4)]

    per = np.random.randint(3, 10)
    per2 = np.random.randint(6, 20)
    weight = np.random.randint(1, 6) * 100
    while per>=per2 or ((per2*weight)-(per*weight))<=0 or ((per2*weight)-(per*weight))%(per2)!=0 or int(((per2*weight)-(per*weight))/per2)>=weight:
        per = np.random.randint(3, 10)
        per2 = np.random.randint(6, 20)
        weight = np.random.randint(1, 6) * 100
    eq = "$$수식$${" + str(per) + "} over 100$$/수식$$ $$수식$$TIMES$$/수식$$ " + str(weight) +" ≥ " + "$$수식$${" + str(per2) + "} over 100$$/수식$$ $$수식$$TIMES$$/수식$$ ("+str(weight) +" - x)" +"$$수식$$$$/수식$$"
    eq2 = str(per*weight)+" ≥ "+ str(per2*weight) + " - " + str(per2) + "x" +"$$수식$$$$/수식$$, "
    eq2 = eq2 + str(per2) + "x ≥ " + str((per2*weight)-(per*weight))+"$$수식$$$$/수식$$"
    answ = int(((per2*weight)-(per*weight))/per2)

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0 and k<weight:
            bb.append(round(k,1))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(liquid=liquid, weight=weight, per=per, per2=per2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, eq=eq, eq2=eq2)

    return stem, answer, comment


#중2-1-2-97
def expressions212_Stem_079():
    stem = "\n{name1}가 두 지점 A, B 사이를 자전거로 왕복하는\n" \
           "데 갈 때에는 시속 $$수식$${speed}$$/수식$$ km, 올 때는 같은 길을 시\n" \
           "속 $$수식$${speed2}$$/수식$$ km로 달렸더니 갈 때와 올 때 소요된 시간\n" \
           "의 차이가 $$수식$${min}$$/수식$$분보다 작았다. 이때 두 지점 A, B\n" \
           "사이의 거리는 몇 km 미만이어야 하는가?" \
           "\n① $$수식$${x1} km\n② {x2} km\n③ {x3} km\n④ {x4} km\n⑤ {x5} km\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "두 지점 A, B 사이의 거리를 x km라 하면\n" \
              "$$수식$${eq}$$/수식$$, $$수식$${eq2}$$/수식$$\n" \
              "∴ x &lt; $$수식$${answ}$$/수식$$\n" \
              "따라서 두 지점 A, B 사이의 거리는 $$수식$${answ}$$/수식$$km 미\n" \
              "만이어야 한다."

    nameList = ["경희", "민철이", "수진이", "철수", "영대", "수현이", "준형이","소희"]
    o = np.random.randint(0, 8)
    name1 = nameList[o]
    speed = np.random.randint(10, 30)
    speed2 =np.random.randint(10, 30)
    mine = np.random.randint(5, 40)
    lcm1 = lcm(lcm(speed, speed2), 60)
    a = int(lcm1/speed2)
    b = int(lcm1/speed)
    c = int(lcm1/60)*mine

    while speed<=speed2 or c%(a-b)!=0:
        speed = np.random.randint(10, 30)
        speed2 = np.random.randint(10, 30)
        mine = np.random.randint(5, 40)
        lcm1 = lcm(lcm(speed, speed2), 60)
        a = int(lcm1 / speed2)
        b = int(lcm1 / speed)
        c = int(lcm1 / 60)*mine
    eq = "$$수식$$rm x over {" + str(speed2) + "}$$/수식$$ - $$수식$$rm x over {" + str(speed) + "}$$/수식$$ &lt; $$수식$${" + str(mine) + "} over 60$$/수식$$ $$수식$$$$/수식$$"
    eq2 = str(a) +"x - " + str(b) +"x &lt; " + str(c)
    answ = int(c/(a-b))

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(speed=speed, speed2=speed2, min=mine, name1=name1,  x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, eq=eq, eq2=eq2)

    return stem, answer, comment


#중2-1-2-99
def expressions212_Stem_080():
    stem = "\nA 그릇에는 $$수식$${per}$$/수식$$ %의 {liquid}{temp} 들어 있고, B 그릇에\n" \
           "는 $$수식$${per2}$$/수식$$ %의 {liquid}{temp} 들어 있다. A 그릇에서 {liquid}\n" \
           "$$수식$${cup}$$/수식$$컵을 덜어내고, 같은 크기의 컵으로 B 그릇에\n" \
           "서 {liquid} $$수식$${cup2}$$/수식$$컵을 덜어내어 $$수식$${weight}$$/수식$$ g의 물이 들어 있\n" \
           "는 C 그릇에 부어 섞었을 때, C 그릇의 {liquid}의\n" \
           "농도가 $$수식$${que}$$/수식$$ % 이상이 되게 하려면 A 그릇에서 최소\n" \
           "몇 g의 {liquid}{temp2} 덜어내야 하는지 구하시오."
    answer = "\n(답): \n" \
            "{ans} g\n"
    comment = "(해설)\n" \
              "한 컵의 양을 x g이라 하면 A 그릇에서 덜어낸\n" \
              "{liquid}의 양은 $$수식$${cup}$$/수식$$x, B 그릇에서 덜어낸 {liquid}의\n" \
              "양은 $$수식$${cup2}$$/수식$$x g이므로\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "∴ x ≥ $$수식$${ans11}$$/수식$$\n" \
              "따라서 $$수식$${cup}$$/수식$$x ≥ $$수식$${answ}$$/수식$$이므로 A 그릇에서 최소 $$수식$${answ}$$/수식$$ g의\n" \
              "{liquid}{temp2} 덜어내야 한다."

    liquids = ["설탕물", "소금물", "알코올", "화학물"]
    liquid = liquids[np.random.randint(0, 4)]
    temp = proc_jo(liquid, 0)
    temp2 =  proc_jo(liquid, 4)

    per = np.random.randint(1, 10)
    per2 = np.random.randint(1, 10)
    que = np.random.randint(1, 10)
    cup = np.random.randint(2, 5)
    cup2 = np.random.randint(2, 5)
    weight = np.random.randint(1, 5)*100
    while(per*cup+per2*cup2)<=(cup*que+cup2*que) or per==per2 or cup==cup2  or (que*weight)%((per*cup+per2*cup2)-(cup*que+cup2*que))!=0:
        per = np.random.randint(1, 10)
        per2 = np.random.randint(1, 10)
        que = np.random.randint(1, 10)
        cup = np.random.randint(2, 5)
        cup2 = np.random.randint(2, 5)
        weight = np.random.randint(1, 5) * 100

    eq = "$$수식$${" + str(per) + "} over 100$$/수식$$ $$수식$$TIMES$$/수식$$ " +str(cup) +"x + $$수식$${" + str(per2) + "} over 100$$/수식$$ $$수식$$TIMES$$/수식$$ " +str(cup2) +"x"
    eq = eq + " ≥ " + "$$수식$${" + str(que) + "} over 100$$/수식$$ $$수식$$TIMES$$/수식$$ (" + str(weight) + " + " +str(cup) +"x + " +str(cup2) +"x)" + "$$수식$$$$/수식$$"
    eq2 = str(per*cup+per2*cup2) +"x" + " ≥ " + str(que*weight) + " + " + str(cup*que+cup2*que) + "x"+ "$$수식$$$$/수식$$, "
    eq2 = eq2 + str((per*cup+per2*cup2)-(cup*que+cup2*que)) +"x ≥ " +  str(que*weight)+ "$$수식$$$$/수식$$"
    ans11 = int((que*weight)/((per*cup+per2*cup2)-(cup*que+cup2*que)))
    answ = ans11*cup


    stem = stem.format(liquid=liquid, temp=temp, temp2=temp2, weight=weight, per=per, per2=per2, que=que, cup=cup, cup2=cup2)
    answer = answer.format(ans=answ)
    comment = comment.format(cup=cup, cup2=cup2, answ=answ, eq=eq, eq2=eq2, ans11=ans11, liquid=liquid, temp2=temp2)

    return stem, answer, comment


#중2-1-2-100
def expressions212_Stem_081():
    stem = "\n{liquid} $$수식$${weight}$$/수식$$ g에서 물 $$수식$${water}$$/수식$$ g을 증발시킨 후에 {component}\n" \
           "$$수식$${new_weight}$$/수식$$ g을 더 녹였더니 처음 농도의 $$수식$${mul}$$/수식$$배 이상의 {liquid}\n" \
           "{temp} 되었다. 처음 {liquid}의 농도는 약 몇 %\n" \
           "이하이었는가? (단, 소수점 아래 둘째 자리에서 반\n올림한다." \
           "\n① $$수식$${x1} %\n② {x2} %\n③ {x3} %\n④ {x4} %\n⑤ {x5} %\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "처음 {liquid}의 농도를 x %라 하면 x %의 {liquid}\n" \
              "$$수식$${weight}$$/수식$$ g에 들어 있는 {component}의 양은\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "이때 물 $$수식$${water}$$/수식$$ g을 증발시킨 후에 {component} $$수식$${new_weight}$$/수식$$ g을 더\n" \
              "녹이면\n" \
              "{liquid}의 양은 $$수식$${eq2}$$/수식$$\n" \
              "{component}의 양은 $$수식$${eq3}$$/수식$$\n" \
              "한편, 물 $$수식$${water}$$/수식$$ g을 증발시킨 후에 {component} $$수식$${new_weight}$$/수식$$ g을 더\n" \
              "녹이면 처음 농도의 $$수식$${mul}$$/수식$$배 이상의 {liquid}{temp} 되므로\n" \
              "$$수식$${eq4}$$/수식$$\n" \
              "$$수식$${eq5}$$/수식$$   ∴ x ≤ $$수식$${fra}$$/수식$$\n" \
              "따라서 $$수식$${fra}$$/수식$$ {deci}이므로 처음 {liquid}의 농도\n" \
              "는 약 $$수식$${answ}$$/수식$$ %이하였다."


    liquids = ["설탕물", "소금물", "화학물"]
    components=["설탕","소금","화학물질"]
    r= np.random.randint(0, 3)
    liquid = liquids[r]
    component = components[r]
    temp = proc_jo(liquid, 0)
    weight = np.random.randint(1, 5) * 100
    water =  np.random.randint(1, 10) * 10
    new_weight = water
    mul = np.random.randint(2, 6)
    aa = int((weight - water + new_weight) / 100)
    while (weight/100)-(mul*aa)>=0:
        weight = np.random.randint(1, 5) * 100
        water = np.random.randint(1, 10) * 10
        new_weight = water
        mul = np.random.randint(2, 6)
        aa = int((weight - water + new_weight) / 100)
    eq = "$$수식$$rm x over 100$$/수식$$ $$수식$$TIMES$$/수식$$ " + str(weight) + " = " + str(int(weight/100)) + "x (g) $$수식$$$$/수식$$"
    eq2 = str(weight) + " - " + str(water) + " + " + str(new_weight) + " = " +  str(weight-water+new_weight) + " (g)$$수식$$$$/수식$$"
    eq3 =  str(int(weight/100))+"x + "  + str(new_weight) + " (g)$$수식$$$$/수식$$"
    eq4 = "$$수식$${"+str(int(weight/100))+"x + "+str(int(new_weight))+"} over {"+str(weight-water+new_weight)+"}$$/수식$$ $$수식$$TIMES$$/수식$$ 100 ≥ x $$수식$$TIMES$$/수식$$ " + str(mul)+ "$$수식$$$$/수식$$"
    aa = int((weight-water+new_weight)/100)
    eq4 = eq4 +  " , "  + str(int(weight/100))+"x + "  + str(new_weight) +  " ≥ " + str(mul*aa) + "x"
    eq5 = str(abs(int(weight/100)-(mul*aa))) +" ≤ " + str(new_weight)
    dd = abs(int(weight/100)-(mul*aa))
    gcd1 = gcd(dd, new_weight)
    dd = int(dd/gcd1)
    aa = int(new_weight/gcd1)
    fra = "$$수식$${"+str(aa)+"} over {"+str(dd)+"}$$/수식$$"
    deci = " = " + str(round(aa/dd,2)) + "$$수식$$CDOTS$$/수식$$"
    answ = round(aa/dd,1)
    if (aa*10)%dd==0 or(aa*100%dd==0):
        deci = " = " + str(round(aa / dd, 2))

    if dd==1:
        fra = aa
        deci =""
        answ = aa

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 15)/10
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        k = round(k, 1)
        if k%1==0:
            k = int(k)
        if k not in bb and k != answ and k != 0:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(component=component, liquid=liquid, temp=temp,  weight=weight, new_weight=new_weight, water=water, mul=mul, x1=x1, x2=x2,x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(water=water, new_weight=new_weight, weight=weight, component=component,answ=answ, eq=eq, eq2=eq2, eq3=eq3, eq4=eq4, eq5=eq5, mul=mul, liquid=liquid, temp=temp,fra=fra, deci=deci)

    return stem, answer, comment


#중2-1-2-102
#not equal sign ≠
def expressions212_Stem_082():
    stem = "\n다음 일차방정식 중 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp} 해로 갖는\n" \
           "것은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "각 일차방정식에서 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp} 대입하면\n" \
              "{list}"

    x = np.random.randint(1, 5)*-1
    y = np.random.randint(1, 5)
    temp = proc_jo(y,4)
    bb=[]
    cc=[]
    while len(cc)<4:
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 10)
        r =np.random.randint(0, 2)
        if r==0:
            c = c*-1
        e = np.random.randint(0, 2)
        if e==0 and (x*a + b*y)!=c:
            pp = str(a) +"x + " + str(b) +"y = " + str(c)
            ss = str(a) + " $$수식$$TIMES$$/수식$$ (" + str(x) +") + " + str(b) + " $$수식$$TIMES$$/수식$$ " + str(y) +" = " + str(x*a + b*y) + " ≠ " + str(c) +"$$수식$$$$/수식$$"
            if a==1:
                pp = "x + " + str(b) +"y = " + str(c)
                ss = str(x) +" + " + str(b) + " $$수식$$TIMES$$/수식$$ " + str(y) +" = " + str(x*a + b*y) + " ≠ " + str(c) +"$$수식$$$$/수식$$"
            if b==1:
                pp = str(a) +"x + y = " + str(c)
                ss = str(a) + " $$수식$$TIMES$$/수식$$ (" + str(x) +") + "  + str(y) +" = " + str(x*a + b*y) + " ≠ " + str(c) +"$$수식$$$$/수식$$"
            if a==1 and b==1:
                pp = "x + y = " + str(c)
                ss = str(x) + " + " + str(y) +" = " + str(x*a + b*y) + " ≠ " + str(c) +"$$수식$$$$/수식$$"
            bb.append(pp)
            cc.append(ss)
        elif e==1 and (x*a - b*y)!=c:
            pp = str(a) + "x - " + str(b) + "y = " + str(c)
            ss = str(a) + " $$수식$$TIMES$$/수식$$ (" + str(x) + ") - " + str(b) + " $$수식$$TIMES$$/수식$$ " + str(y) + " = " + str(x * a - b * y) + " ≠ " + str(c) + "$$수식$$$$/수식$$"
            if a == 1:
                pp = "x + " + str(b) + "y = " + str(c)
                ss = str(x) + " - " + str(b) + " $$수식$$TIMES$$/수식$$ " + str(y) + " = " + str(x * a - b * y) + " ≠ " + str(c) + "$$수식$$$$/수식$$"
            if b == 1:
                pp = str(a) + "x + y = " + str(c)
                ss = str(a) + " $$수식$$TIMES$$/수식$$ (" + str(x) + ") - " + str(y) + " = " + str(x * a - b * y) + " ≠ " + str(c) + "$$수식$$$$/수식$$"
            if a == 1 and b == 1:
                pp = "x + y = " + str(c)
                ss = str(x) + " - " + str(y) + " = " + str(x * a - b * y) + " ≠ " + str(c) + "$$수식$$$$/수식$$"
            bb.append(pp)
            cc.append(ss)
    answ=""
    while answ=="":
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 10)
        r = np.random.randint(0, 2)
        if r == 0:
            c = c * -1
        e = np.random.randint(0, 2)
        if e == 0 and (x * a + b * y) == c:
            answ = str(a) + "x + " + str(b) + "y = " + str(c)
            ss = str(a) + " $$수식$$TIMES$$/수식$$ (" + str(x) + ") + " + str(b) + " $$수식$$TIMES$$/수식$$ " + str(y) + " = " + str(x * a + b * y) + "$$수식$$$$/수식$$"
            if a == 1:
                answ = "x + " + str(b) + "y = " + str(c)
                ss = str(x) + " + " + str(b) + " $$수식$$TIMES$$/수식$$ " + str(y) + " = " + str(x * a + b * y) +  "$$수식$$$$/수식$$"
            if b == 1:
                answ = str(a) + "x + y = " + str(c)
                ss = str(a) + " $$수식$$TIMES$$/수식$$ (" + str(x) + ") + " + str(y) + " = " + str(x * a + b * y) +  "$$수식$$$$/수식$$"
            if a == 1 and b == 1:
                answ = "x + y = " + str(c)
                ss = str(x) + " + " + str(y) + " = " + str(x * a + b * y) +  "$$수식$$$$/수식$$"
            cc.append(ss)
            break
        elif e == 1 and (x * a - b * y) == c:
            answ = str(a) + "x - " + str(b) + "y = " + str(c)
            ss = str(a) + " $$수식$$TIMES$$/수식$$ (" + str(x) + ") - " + str(b) + " $$수식$$TIMES$$/수식$$ " + str(y) + " = " + str(x * a - b * y) +  "$$수식$$$$/수식$$"
            if a == 1:
                answ = "x + " + str(b) + "y = " + str(c)
                ss = str(x) + " - " + str(b) + " $$수식$$TIMES$$/수식$$ " + str(y) + " = " + str(x * a - b * y) + "$$수식$$$$/수식$$"
            if b == 1:
                answ = str(a) + "x + y = " + str(c)
                ss = str(a) + " $$수식$$TIMES$$/수식$$ (" + str(x) + ") - " + str(y) + " = " + str(x * a - b * y) +  "$$수식$$$$/수식$$"
            if a == 1 and b == 1:
                answ = "x + y = " + str(c)
                ss = str(x) + " - " + str(y) + " = " + str(x * a - b * y) +  "$$수식$$$$/수식$$"
            cc.append(ss)
            break
    t=""
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
        t = "① " + cc[4] + "\n② " + cc[0] + "\n③ " + cc[1] + "\n④ " + cc[2] + "\n⑤ " + cc[3]
    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
        t = "① " + cc[0] + "\n② " + cc[4] + "\n③ " + cc[1] + "\n④ " + cc[2] + "\n⑤ " + cc[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
        t = "① " + cc[0] + "\n② " + cc[1] + "\n③ " + cc[4] + "\n④ " + cc[2] + "\n⑤ " + cc[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
        t = "① " + cc[0] + "\n② " + cc[1] + "\n③ " + cc[2] + "\n④ " + cc[4] + "\n⑤ " + cc[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
        t = "① " + cc[0] + "\n② " + cc[1] + "\n③ " + cc[2] + "\n④ " + cc[3] + "\n⑤ " + cc[4]

    stem = stem.format(temp=temp, x=x, y=y, x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=t, temp=temp, x=x, y=y)

    return stem, answer, comment


#중2-1-2-103
def expressions212_Stem_083():
    stem = "\n$$수식$${eq}$$/수식$${temp} 미지수가 2개\n" \
           "인 일차방정식일 때, 상수 a의 값이 될 수 없는\n" \
           "것은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$\n" \
              "이 식이 미지수가 2개인 일차방정식이려면\n" \
              "$$수식$${eq4}$$/수식$$   ∴ a  ≠ $$수식$${answ}$$/수식$$"

    a = np.random.randint(1, 10)
    b = np.random.randint(2, 10)
    c = np.random.randint(1, 10)
    d = np.random.randint(1, 10)
    e = np.random.randint(2, 10)
    f = np.random.randint(1, 10)
    temp = proc_jo(f, 0)
    while a==d or b==e:
        d = np.random.randint(1, 10)
        e = np.random.randint(2, 10)
    eq=str(a) +"x + "
    eq2=str(a) +"x + "
    if a==1:
        eq ="x + "
        eq2 = "x + "
    eq = eq + "(a - " + str(b) + ")y  + " + str(c) + " = "
    eq2 = eq2 + "ay - " + str(b) + "y  + "+ str(c) + " = "
    if d==1:
        eq = eq + " x - "
        eq2 =eq2 + " x - "
    else:
        eq = eq + str(d) +"x - "
        eq2 = eq2 + str(d) + "x - "
    eq = eq + str(e) +"y + " + str(f) + "$$수식$$$$/수식$$"
    eq2 = eq2 + str(e) +"y + " + str(f) + "$$수식$$$$/수식$$"
    eq3 = str(a-d) +"x + (a "
    if a-d==1:
        eq3 = "x + (a "
    elif a-d==-1:
        eq3 = "-x + (a "
    eq4=""
    if -b+e>0:
        eq3 = eq3 + " + " + str(-b+e) + ")y "
        eq4 = "a + " + str(-b+e) + " ≠ " + str(0) + "$$수식$$$$/수식$$"
    elif -b+e<0:
        eq3 = eq3 + " - " + str(abs(-b + e)) + ")y "
        eq4 = "a - " + str(abs(-b + e)) + " ≠ " + str(0) + "$$수식$$$$/수식$$"
    answ = b - e
    if c-f>0:
        eq3 = eq3 + " + " + str(c-f) + " = " + str(0)
    elif c-f<0:
        eq3 = eq3 + " - " + str(abs(c-f)) + " = " + str(0)
    elif c-f==0:
        eq3 = eq3 + " = " + str(0)+ "$$수식$$$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(temp=temp, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, eq3=eq3, eq4=eq4, answ=answ)

    return stem, answer, comment

#중2-1-2-104
def expressions212_Stem_084():
    stem = "\n등식 $$수식$${eq}$$/수식$${temp} 미지수가 2개\n" \
           "인 일차방정식일 되기 위한 상수 a,b의 값이 또는\n" \
           "조건으로 옳은 것은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$${temp2} 정리하면\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "따라서 이 식이 미지수가 2개인 일차방정식이 되\n" \
              "려면\n" \
              "$$수식$${eq3}$$/수식$$      $$수식$$  $$/수식$$,즉 {answ}이어\n" \
              "야 한다."

    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)
    d = np.random.randint(1, 10)
    temp = proc_jo(d, 3)
    temp2 = proc_jo(d,4)
    eq ="ax - " + str(a) +"y + " + str(b) + " = "
    if a==1:
        eq = "ax - y + " + str(b) + " = "
    if c==1:
        eq = eq + "x + by - " + str(d)+ "$$수식$$$$/수식$$"
    else:
        eq = eq + str(c)+ "x + by - " + str(d)+ "$$수식$$$$/수식$$"
    eq2 = "(a - " + str(c) +")x - (b + " +str(a) +")y + " + str(b+d) + " = " + str(0) + "$$수식$$$$/수식$$"
    eq3 = "a - " + str(c) + " ≠ " +  str(0)+ "$$수식$$$$/수식$$, b + "+ str(a) + " ≠ " +  str(0)+ "$$수식$$$$/수식$$"
    answ = "a ≠ " + str(c) +" , b ≠ " + str(-a)
    bb=[]
    bb.append("a ≠ " + str(c) +" , b ≠ " + str(a))
    bb.append("a ≠ " + str(-c) +" , b ≠ " + str(-a))
    bb.append("a ≠ " + str(-c) +" , b ≠ " + str(a))
    bb.append("a = " + str(c) +" , b = " + str(-a))

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[3]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[0]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[3]
        x2 = bb[2]
        x4 = bb[0]
        x5 = bb[1]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[2]
        x2 = bb[3]
        x3 = bb[1]
        x5 = bb[0]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[1]
        x2 = bb[2]
        x3 = bb[0]
        x4 = bb[3]

    stem = stem.format(temp=temp, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, eq3=eq3, temp2=temp2, answ=answ)

    return stem, answer, comment

#중2-1-2-105
def expressions212_Stem_085():
    stem = "\nx %의 {liquid} $$수식$${weight}$$/수식$$ g과 y %의 {liquid} $$수식$${weight2}$$/수식$$ g을\n" \
           "섞었더니 $$수식$${per}$$/수식$$ %의 {liquid} $$수식$${total}$$/수식$$ g이 되었다. 이를\n" \
           "미지수가 2개인 일차방정식으로 나타내면?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "∴ $$수식$${answ}$$/수식$$"


    liquids = ["설탕물", "소금물", "화학물"]
    r = np.random.randint(0, 3)
    liquid = liquids[r]
    weight = np.random.randint(1, 4)*100
    weight2 = np.random.randint(1, 4)*100
    while weight==weight2:
        weight2 = np.random.randint(1, 4) * 100
    total = weight+weight2
    per = np.random.randint(5, 20)
    eq = "$$수식$$rm x over 100$$/수식$$ $$수식$$TIMES$$/수식$$ " + str(weight) + " + $$수식$$rm y over 100$$/수식$$ $$수식$$TIMES$$/수식$$ " + str(weight2)
    eq = eq + " = $$수식$${"+str(per)+"} over 100$$/수식$$ $$수식$$TIMES$$/수식$$ " + str(total) + "$$수식$$$$/수식$$"
    a = int(weight/100)
    b = int(weight2/100)
    c = int(total/100)*per
    answ = str(a) +"x + " + str(b) + "y = " + str(c)
    if a==1 and b==1:
        answ = "x + y = " + str(c)
    elif a==1:
        answ = "x + " + str(b) + "y = " + str(c)
    elif b==1:
        answ = str(a) + "x + y = " + str(c)
    bb=[]
    aa=""
    dd=""
    if a==1:
        aa=""
    else:
        aa= str(a)
    if b==1:
        dd=""
    else:
        dd=str(b)
    bb.append(aa + "x - " +dd + "y = " + str(c))
    bb.append(dd +"x + " +aa + "y = " + str(c*2))
    bb.append(dd +"x - " + aa + "y = " + str(c))
    bb.append(aa +"x + " + dd + "y = " + str(c*2))

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[3]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[0]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[3]
        x2 = bb[2]
        x4 = bb[0]
        x5 = bb[1]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[2]
        x2 = bb[3]
        x3 = bb[1]
        x5 = bb[0]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[1]
        x2 = bb[2]
        x3 = bb[0]
        x4 = bb[3]

    stem = stem.format(liquid=liquid, weight=weight, per=per, weight2=weight2, total=total, x1=x1, x2=x2, x3=x3, x4=x4,
                       x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, answ=answ)

    return stem, answer, comment

#중2-1-2-106
#korean ㈀ ㈁ ㈂ ㈃ ㈄
def expressions212_Stem_086():
    stem = "\n일차방정식 $$수식$${eq}$$/수식$$의 해인 것을 보기에서\n" \
           "모두 고른 것은? $$표$$\n" \
           "㈀ {op1}                            \n㈁ {op2}\n" \
           "㈂ {op3}                            \n㈃ {op4}\n" \
           "㈄ {op5}                            \n㈅ {op6}\n$$/표$$"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "{list}" \
              "따라서 $$수식$${eq}$$/수식$$의 해인 것은 {answ}\n" \
              "이다."

    a = np.random.randint(2,10)
    b = 1
    c = a*np.random.randint(2,5)
    eq= str(a) +"x - " + str(b) + "y = " + str(c) +"$$수식$$$$/수식$$"
    if a==1 and b==1:
        eq ="x - y = " + str(c)+"$$수식$$$$/수식$$"
    elif a==1:
        eq = "x - " +  str(b) + "y = " + str(c)+"$$수식$$$$/수식$$"
    elif b==1:
        eq = str(a) +"x - y = " + str(c)+"$$수식$$$$/수식$$"
    bb=[]
    cc=[]
    while len(bb)<2:
        f = np.random.randint(0, 10)
        tt = np.random.randint(0,2)
        if tt==0:
            f = f*-1
        g = np.random.randint(0, 10)
        xx = np.random.randint(0, 2)
        if xx == 0:
            g = g * -1
        if f*a -g*b ==c:
            bb.append("(" + str(f) +", " + str(g) +")")
            pie = str(a) + " $$수식$$TIMES$$/수식$$ " + str(f) + " - " + str(b) + "$$수식$$TIMES$$/수식$$ " + str(g) + " = " + str(c)+"\n"
            if b==1 and g<0:
                pie =  str(a) + " $$수식$$TIMES$$/수식$$ " + str(f) + " - ("+ str(g) + ") = " + str(c)+"\n"
            elif b==1 and g>0:
                pie = str(a) + " $$수식$$TIMES$$/수식$$ " + str(f) + " - " + str(g) + " = " + str(c)+"\n"
            cc.append(pie)
    ll=[]
    if len(bb)<4:
        xx = "($$수식$$1 over {"+str(a)+"}$$/수식$$, " + str(-(c-1))+")"
        bb.append(xx)
        mm = str(a) + " $$수식$$TIMES$$/수식$$ $$수식$$1 over {"+str(a)+"}$$/수식$$ - ("+ str(-(c-1)) + ") = " + str(c) +"\n"
        cc.append(mm)
    length = len(bb)
    while len(bb)<6:
        s = np.random.randint(2, 10)
        z = np.random.randint(2, 10)*-1
        hh = np.random.randint(0, 2)
        if hh==1 and (1/s)*a-(z*b)!=c and (1/s)*a-(z*b) not in ll:
            nn = "($$수식$$1 over {"+str(s)+"}$$/수식$$, - " + str(abs(z))+")"
            ll.append((1/s)*a-(z*b))
            bb.append(nn)
        elif  hh==0 and ((1/s)*a)-((1/z)*b)!=c and ((1/s)*a)-((1/z)*b) not in ll:
            nn = "($$수식$$1 over {" + str(s) + "}$$/수식$$, - $$수식$$1 over {" + str(abs(z)) + "}$$/수식$$)"
            ll.append(((1/s)*a)-((1/z)*b))
            bb.append(nn)
    answ=""
    list=""
    gg = np.random.randint(0, 4)
    if gg==0:
        op1 = bb[0]
        op2 = bb[1]
        op3 = bb[2]
        op4 = bb[3]
        op5 = bb[4]
        op6 = bb[5]
        answ = "㈀, ㈁, ㈂"
        ans ="①"
        x1 = answ
        x2 ="㈁, ㈃, ㈄"
        x3="㈃, ㈄, ㈅"
        x4="㈂, ㈄, ㈅"
        x5="㈀, ㈂, ㈄, ㈅"
        list = "㈀ " + cc[0] + "㈁ " + cc[1] + "㈂ " + cc[2]
    elif gg==1:
        op1 = bb[4]
        op2 = bb[5]
        op3 = bb[3]
        op4 = bb[2]
        op5 = bb[0]
        op6 = bb[1]
        ans = "③"
        answ = "㈃, ㈄, ㈅"
        x1 = "㈀, ㈁, ㈂"
        x2 = "㈁, ㈃, ㈄"
        x3 = answ
        x4 = "㈁, ㈂, ㈃, ㈅"
        x5 = "㈀, ㈂, ㈄, ㈅"
        list = "㈃ " + cc[2] + "㈄ " + cc[0] + "㈅ " + cc[1]
    elif gg==2:
        op1 = bb[3]
        op2 = bb[1]
        op3 = bb[4]
        op4 = bb[0]
        op5 = bb[2]
        op6 = bb[5]
        ans = "②"
        answ = "㈁, ㈃, ㈄"
        x1 = "㈀, ㈁, ㈂"
        x2 = answ
        x3 = "㈃, ㈄, ㈅"
        x4 = "㈁, ㈂, ㈄, ㈅"
        x5 = "㈀, ㈂, ㈃, ㈅"
        list = "㈁ " + cc[1] + "㈃ " + cc[0] + "㈄ " + cc[2]

    else:
        op1 = bb[3]
        op2 = bb[4]
        op3 = bb[1]
        op4 = bb[5]
        op5 = bb[2]
        op6 = bb[0]
        ans="④"
        answ = "㈂, ㈄, ㈅"
        x1 =  "㈁, ㈃, ㈄"
        x2 = "㈃, ㈄, ㈅"
        x3 =  "㈂, ㈃, ㈄"
        x4 = answ
        x5 = "㈀, ㈂, ㈃, ㈅"
        list = "㈂ " + cc[1] + "㈄ " + cc[2] + "㈅ " + cc[0]

    stem = stem.format(eq=eq, op1=op1, op2=op2, op3=op3, op4=op4, op5=op5, op6=op6, x1=x1, x2=x2, x3=x3, x4=x4,
                       x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, list=list, answ=answ)

    return stem, answer, comment

#중2-1-2-107
def expressions212_Stem_087():
    stem = "\nx, y가 자연수일 때, 일차방정식 $$수식$${eq}$$/수식$$\n" \
           "의 해의 개수를 a, 일차방정식 $$수식$${eq2}$$/수식$$    의\n" \
           "해의 개수를 b라 하자. ab의 값은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x, y가 자연수일 때, $$수식$${eq}$$/수식$$    의 해는\n" \
              "{list}의 $$수식$${aa}$$/수식$$개   ∴ a = $$수식$${aa}$$/수식$$\n" \
              "$$수식$${eq2}$$/수식$$    의 해는 {list2}의 $$수식$${ww}$$/수식$$개  \n" \
              "∴ b = $$수식$${ww}$$/수식$$ \n" \
              "∴ ab = $$수식$${answ}$$/수식$$"

    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 20)
    eq = str(a) +"x + " + str(b) +"y = " + str(c)
    if a==1:
        eq = "x + " + str(b) +"y = " + str(c)
    if b==1:
        eq = str(a) +"x + y = " + str(c)
    if a==1 and b==1:
        eq = "x + y = " + str(c)
    ee=[]
    for i in range(c+1):
        for j in range(c+1):
            if (i*a+j*b)==c:
                ee.append([i,j])
    aa = len(ee)
    list=""
    if len(ee)>0:
        for i in range(len(ee)-1):
            list = list +"(" + str(ee[i][0]) +", " + str(ee[i][1]) +") , "
        list = list +"(" + str(ee[-1][0]) +", " + str(ee[-1][1]) +")"

    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 20)
    eq2 = str(a) +"x + " + str(b) +"y = " + str(c)
    if a==1:
        eq2 = "x + " + str(b) +"y = " + str(c)
    if b==1:
        eq2 = str(a) +"x + y = " + str(c)
    if a==1 and b==1:
        eq2 = "x + y = " + str(c)
    ee = []
    for i in range(c + 1):
        for j in range(c + 1):
            if (i * a + j * b) == c:
                ee.append([i, j])
    ww = len(ee)
    list2 = ""
    if len(ee) > 0:
        for i in range(len(ee) - 1):
            list2 = list2 + "(" + str(ee[i][0]) + ", " + str(ee[i][1]) + ") , "
        list2 = list2 + "(" + str(ee[-1][0]) + ", " + str(ee[-1][1]) + ")"
    answ = aa*ww
    while answ==0:
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 20)
        eq = str(a) + "x + " + str(b) + "y = " + str(c)
        if a == 1:
            eq = "x + " + str(b) + "y = " + str(c)
        if b == 1:
            eq = str(a) + "x + y = " + str(c)
        if a == 1 and b == 1:
            eq = "x + y = " + str(c)
        ee = []
        for i in range(c + 1):
            for j in range(c + 1):
                if (i * a + j * b) == c:
                    ee.append([i, j])
        aa = len(ee)
        list = ""
        if len(ee) > 0:
            for i in range(len(ee) - 1):
                list = list + "(" + str(ee[i][0]) + ", " + str(ee[i][1]) + ") , "
            list = list + "(" + str(ee[-1][0]) + ", " + str(ee[-1][1]) + ")"

        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 20)
        eq2 = str(a) + "x + " + str(b) + "y = " + str(c)
        if a == 1:
            eq2 = "x + " + str(b) + "y = " + str(c)
        if b == 1:
            eq2 = str(a) + "x + y = " + str(c)
        if a == 1 and b == 1:
            eq2 = "x + y = " + str(c)
        ee = []
        for i in range(c + 1):
            for j in range(c + 1):
                if (i * a + j * b) == c:
                    ee.append([i, j])
        ww = len(ee)
        list2 = ""
        if len(ee) > 0:
            for i in range(len(ee) - 1):
                list2 = list2 + "(" + str(ee[i][0]) + ", " + str(ee[i][1]) + ") , "
            list2 = list2 + "(" + str(ee[-1][0]) + ", " + str(ee[-1][1]) + ")"
        answ = aa * ww
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, eq2=eq2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, list2=list2, aa=aa, ww=ww, list=list, answ=answ)

    return stem, answer, comment

#중2-1-2-108
def expressions212_Stem_088():
    stem = "\n일차방정식 $$수식$${eq}$$/수식$$   에 대하여 옳은 것만을\n" \
           "보기에서 있는 대로 고른 것은?$$표$$\n" \
           "㈀ x,y가 자연수인 해는 $$수식$${num}$$/수식$$개이다.\n" \
           "㈁ x, y가 자연수일 때, x &gt; y인 해는 없\n다.\n" \
           "㈂ x = $$수식$${x}$$/수식$$일 때, y = $$수식$${y}$$/수식$$이다." \
           "$$/표$$"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "㈀ {list1}의 $$수식$${aa}$$/수식$$개이다.\n" \
              "㈁ x &gt; y인 해는 {list2}의 $$수식$${bb}$$/수식$$개이다.\n" \
              "㈂ x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$$$수식$$``$$/수식$${temp} 대입하면\n" \
              "$$수식$${eqq}$$/수식$$\n" \
              "따라서 옳은 것은 {answ}이다."

    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 20)
    eq = str(a) +"x + " + str(b) +"y = " + str(c)
    if a==1:
        eq = "x + " + str(b) +"y = " + str(c)
    if b==1:
        eq = str(a) +"x + y = " + str(c)
    if a==1 and b==1:
        eq = "x + y = " + str(c)
    ee=[]
    for i in range(c+1):
        for j in range(c+1):
            if (i*a+j*b)==c:
                ee.append([i,j])
    aa = len(ee)
    list1 = ""
    list2=""
    bb=0
    if len(ee) > 0:
        for i in range(len(ee) - 1):
            list1 = list1 + "(" + str(ee[i][0]) + ", " + str(ee[i][1]) + ") , "
            if ee[i][0]>ee[i][1]:
                bb+=1
                list2 = list2 + "(" + str(ee[i][0]) + ", " + str(ee[i][1]) + ") , "

        list1 = list1 + "(" + str(ee[-1][0]) + ", " + str(ee[-1][1]) + ")"
        if ee[-1][0]>ee[-1][1]:
            bb += 1
            list2 = list2 + "(" + str(ee[-1][0]) + ", " + str(ee[-1][1]) + ")"

    rande = np.random.randint(1, 4)
    if bb!=0 and rande==1:
        ans = "①"
        num = aa
        x= ee[-1][0]+3
        y = ee[-1][1]
        x1 = "㈀"
        answ = x1
        x2 = "㈁"
        x3 = "㈂"
        x4 = "㈀, ㈁"
        x5 = "㈁, ㈂"
    elif bb==0 and bb==0:
        ans = "②"
        num = aa
        if len(ee)>0:
            x = ee[-1][0] + 3
            y = ee[-1][1]
        else:
            x=3
            y=5
        x2 = "㈀, ㈁"
        x1 = "㈁"
        answ = x2
        x3 = "㈀, ㈂"
        x4 = "㈁, ㈂"
        x5 = "㈀, ㈁, ㈂"
    elif bb!=0 and rande==2:
        ans = "③"
        num = aa + 4
        x = ee[-1][0]
        y = ee[-1][1]
        x2 = "㈁"
        x1 = "㈀"
        x3 = "㈂"
        answ=x3
        x4 = "㈁, ㈂"
        x5 = "㈀, ㈁, ㈂"
    elif rande == 3 and bb==0:
        ans = "④"
        num = aa +4
        x = ee[-1][0]
        y = ee[-1][1]
        x4 = "㈁, ㈂"
        answ = x4
        x1 = "㈁"
        x2 = "㈂"
        x3 = "㈀, ㈂"
        x5 = "㈀, ㈁, ㈂"
    elif rande == 3 and b!=0:
        ans = "④"
        x4 ="㈀, ㈂"
        answ = x4
        num = aa
        x = ee[-1][0]
        y = ee[-1][1]
        x1 = "㈁"
        x2 = "㈂"
        x5 = "㈀, ㈁, ㈂"
        x3 ="㈁, ㈂"
    eqq =str(a) + " $$수식$$TIMES$$/수식$$ " + str(x) +" + " + str(b) +  " $$수식$$TIMES$$/수식$$ " + str(y) + " = " + str(a*x+b*y)
    temp = proc_jo(y, 4)
    stem = stem.format(eq=eq, num=num, x=x, y=y ,x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, list1=list1, aa=aa, bb=bb, temp=temp, list2=list2, x=x, y=y,eqq=eqq )

    return stem, answer, comment

#중2-1-2-109
def expressions212_Stem_089():
    stem = "\n순서쌍 (a, b)가 일차방정식 $$수식$${eq}$$/수식$$의\n" \
           "해일 때, $$수식$${x}$$/수식$$의 값은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x = a, y = b를 $$수식$${eq}$$/수식$$에 대입하면\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "∴ $$수식$${eq3}$$/수식$$"

    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 20)*-1
    d=np.random.randint(1, 10)
    eq = str(a) + "x + " + str(b) + "y = " + str(c) +"$$수식$$$$/수식$$"
    eq2 = str(a) + "a + " + str(b) + "b = " + str(c) +"$$수식$$$$/수식$$"
    x =  str(a) + "a + " + str(b) + "b  + " + str(d) +"$$수식$$$$/수식$$"
    if a == 1:
        eq = "x + " + str(b) + "y = " + str(c)+"$$수식$$$$/수식$$"
        eq2 = "a + " + str(b) + "b = " + str(c) + "$$수식$$$$/수식$$"
        x = "a + " + str(b) + "b  + " + str(d) + "$$수식$$$$/수식$$"
    if b == 1:
        eq = str(a) + "x + y = " + str(c)+"$$수식$$$$/수식$$"
        eq2 = str(a) + "a + b = " + str(c) + "$$수식$$$$/수식$$"
        x = str(a) + "a + b + " + str(d) + "$$수식$$$$/수식$$"
    if a == 1 and b == 1:
        eq = "x + y = " + str(c)+"$$수식$$$$/수식$$"
        eq2 = "a + b = " + str(c) + "$$수식$$$$/수식$$"
        x = "a + b + " + str(d) + "$$수식$$$$/수식$$"
    eq3 = x +" = " + str(c) + " + " +  str(d) + " = " +  str(c+d)
    answ = c+d
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0:
            bb.append(round(k, 1))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    stem = stem.format(eq=eq, x=x, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, eq3=eq3)

    return stem, answer, comment

#중2-1-2-111
def expressions212_Stem_090():
    stem = "\nx = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp} x, y에 대한 일차방정식\n" \
           "$$수식$${eq}$$/수식$$의 해일 때, 일차방정식\n" \
           "$$수식$${eq2}$$/수식$$$$수식$$``$$/수식$$     를 만족시키는 x, y에 대하여\n" \
           "$$수식$${qe}$$/수식$$의 값을 구하시오. (단, a, b는 상수이고,\n" \
           "ab ≠ 0 이다.)"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp2} $$수식$${eq}$$/수식$$에 대\n" \
              "입하면\n" \
              "$$수식$${eq3}$$/수식$$\n" \
              "$$수식$${eq4}$$/수식$$  ∴ a = {bes}\n" \
              "a = {bes}$$수식$$``$$/수식$$를 {eq2}에 대입하면\n" \
              "$$수식$${eq5}$$/수식$$\n" \
              "∴ $$수식$${qe}$$/수식$$ = $$수식$${answ}$$/수식$$"

    x = np.random.randint(1, 5)
    y = np.random.randint(1, 5)
    while x==y:
        y = np.random.randint(1, 5)
    c = np.random.randint(2, 5)
    while x*c-y!=1:
        x = np.random.randint(1, 5)
        y = np.random.randint(1, 5)
        while x == y:
            y = np.random.randint(1, 5)
        c = np.random.randint(2, 5)
    temp = proc_jo(y, 0)
    temp2 = proc_jo(y, 4)

    eq = "("+ str(c)+"a + b)x - (a - b)y = 0 $$수식$$$$/수식$$"
    eq3 = str(x) + "("+ str(c)+"a + b) - "
    eq4 = str(x*c) +"a + " + str(x) + "b - "
    if x==1:
        eq3 = "(" + str(c) + "a + b) - "
        eq4 = str(x * c) + "a + b - "
    if y!=1:
        eq3 =eq3 + str(y) + "(a - b) = 0 $$수식$$$$/수식$$"
        eq4 = eq4 + str(y) +"a + " + str(y) +"b = 0 $$수식$$$$/수식$$"
    else:
        eq3 = eq3 + "(a - b) = 0 $$수식$$$$/수식$$"
        eq4 = eq4 + "a + b = 0 $$수식$$$$/수식$$"
    bes = str(-y-x) +"b $$수식$$$$/수식$$"

    p = np.random.randint(2, 9)
    pp = np.random.randint(2, 9)
    eq2 ="ax - " + str(p) +"b = " + str(pp) +"by - a"
    eq5 = str(-y-x) +"bx - " + str(p) +"b = " + str(pp) +"by +"+ str(y+x) +"b $$수식$$$$/수식$$ , "
    eq5 = eq5 + str(y+x) +"bx + "+ str(pp) +"by = " + str(((y+x)-(-p))*-1) +"b $$수식$$$$/수식$$"
    qe =  str(y+x) +"x + "+ str(pp) +"y $$수식$$$$/수식$$"
    answ = (((y+x)-(-p))*-1)

    stem = stem.format(eq=eq, x=x, y=y, temp=temp, eq2=eq2, qe=qe)
    answer = answer.format(ans=answ)
    comment = comment.format(eq2=eq2, x=x, y=y, temp2=temp2, bes=bes, eq4=eq4, eq5=eq5, answ=answ,eq3=eq3, qe=qe, eq=eq)

    return stem, answer, comment

#중2-1-2-112
def expressions212_Stem_091():
    stem = "\n일차방정식 $$수식$${eq}$$/수식$$의 한 해가\n" \
           "x = $$수식$${x}$$/수식$$, y = a일 때, 상수 a의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$에서 $$수식$${eq2}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$$, y = a를 $$수식$${eq3}$$/수식$$에 대입하면\n" \
              "$$수식$${eq4}$$/수식$$   ∴ a = $$수식$${answ}$$/수식$$"

    a = np.random.randint(3, 6)/10
    b = np.random.randint(11, 20)/10
    c = np.random.randint(11, 20)/10
    eq = str(a) +"x + " + str(b) + "y = " + str(c) + "$$수식$$$$/수식$$"
    eq2 = "$$수식$${"+str(int(a*10))+"} over 10$$/수식$$x + $$수식$${"+str(int(b*10))+"} over 10$$/수식$$y = $$수식$${"+str(int(c*10))+"} over 10$$/수식$$"
    eq3 = str(int(a*10)) + "x + " + str(int(b*10)) + "y = " + str(int(c*10))+ "$$수식$$$$/수식$$"
    a=int(a*10)
    b= int(b*10)
    c = int(c*10)
    x=y=0
    for i in range(int((c+1)/a)):
        for j in range(int((c+1)/b)):
            if a*i + b*j ==c:
                x = i
                y = j
        if x!=0 or y!=0:
            break
    if x==0 and y==0:
        x = np.random.randint(1, 5)
        while c - a*x<=0:
            x = np.random.randint(1, 5)
        bb = c - a*x
        gcd1 = gcd(int(bb*10), int(b*10))
        bb = int((bb*10)/gcd1)
        aa = int((b*10)/gcd1)
        y = "$$수식$${"+str(bb)+"} over {"+str(aa)+"}$$/수식$$"
    answ = y
    eq4 = str(a*x) + " + " + str(b) +"a = " + str(c)

    bb=[]
    dd=[]
    while len(bb)<4:
        f = np.random.randint(2, 20)
        g = np.random.randint(2, 20)
        if a*x +b*(f/g) !=c and f/g not in dd:
            gcd1 = gcd(f,g)
            f = int(f/gcd1)
            g = int(g/gcd1)
            dd.append(f/g)
            t = "$$수식$${"+str(f)+"} over {"+str(g)+"}$$/수식$$"
            if g==1:
                t = str(f)
            bb.append(t)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    stem = stem.format(eq=eq, x=x, x1=x1, x2=x2, x3=x3, x4=x4,x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, eq2=eq2, eq3=eq3, x=x, eq4=eq4, answ=answ)

    return stem, answer, comment

#중2-1-2-115
#(가)를 넣으면 에러
def expressions212_Stem_092():
    stem = "\n어느 중학교의 작년 학생 수는 $$수식$${num}$$/수식$$명이었다. 올해\n" \
           "에는 남학생은 작년보다 $$수식$${per}$$/수식$$ % 증가하고, 여학생은\n" \
           "$$수식$${per2}$$/수식$$ % 감소하여 전체적으로 $$수식$${de}$$/수식$$명이 감소하였다. 작\n" \
           "년 남학생 수를 x명, 여학생 y명으로 놓고 연립\n" \
           "방정식을 세우면$$수식$${eq}$$/수식$$              일 때, 다음 중\n\n" \
           "(가)에 알맞은 식은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "올해에 증가한 남학생의 수는 x $$수식$$TIMES$$/수식$$ {fra1} (명)\n" \
              "올해에 감소한 여학생의 수는 y $$수식$$TIMES$$/수식$$ {fra2} (명)\n" \
              "전체적으로 $$수식$${de}$$/수식$$명이 감소하였으므로\n" \
              "{answ}"

    num =np.random.randint(300, 700)
    per = np.random.randint(1, 10)
    per2 = np.random.randint(1, 10)
    while per==per2:
        per2 = np.random.randint(1, 10)
    de = np.random.randint(1, 10)
    tt="(가)"
    eq ="{cases{x + y = " + str(num) + "#`" + tt +"`}}"
    answ = "$$수식$${"+str(per)+"} over 100$$/수식$$   x - $$수식$${"+str(per2)+"} over 100$$/수식$$   y = " +str(-1*de)
    bb=[]
    bb.append("$$수식$${"+str(per)+"} over 100$$/수식$$   x - $$수식$${"+str(per2)+"} over 100$$/수식$$   y = " +str(de))
    bb.append("$$수식$${" + str(per) + "} over 100$$/수식$$   x + $$수식$${" + str(per2) + "} over 100$$/수식$$   y = " + str(-1 * de))
    bb.append("$$수식$${" + str(per2) + "} over 100$$/수식$$   x - $$수식$${" + str(per) + "} over 100$$/수식$$   y = " + str(-1*de))
    bb.append("$$수식$${" + str(per2) + "} over 100$$/수식$$   x + $$수식$${" + str(per) + "} over 100$$/수식$$   y = " + str(de))
    fra1 = "$$수식$${"+str(per)+"} over 100$$/수식$$"
    fra2 = "$$수식$${"+str(per2)+"} over 100$$/수식$$"
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(de=de, eq=eq, per=per, per2=per2, num=num,x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(fra1=fra1,fra2=fra2, de=de, answ=answ)

    return stem, answer, comment

#중2-1-2-116
def expressions212_Stem_093():
    stem = "\nx, y가 자연수일 때, 일차방정식 $$수식$${eq}$$/수식$$의\n" \
           "해의 개수를 a, 일차방정식 $$수식$${eq2}$$/수식$$의 해의\n" \
           "개수를 b, 연립방정식 $$수식$${aaa}$$/수식$$      $$수식$$``$$/수식$$     의 해의 개\n\n" \
           "수를 c라 하자. 이때 a + b + c의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x, y가 자연수일 때, $$수식$${eq3}$$/수식$$의 해는\n" \
              "{list}의 $$수식$${aa}$$/수식$$개  ∴ a = $$수식$${aa}$$/수식$$\n" \
              "$$수식$${eq4}$$/수식$$    의 해는\n" \
              "{list2}의 $$수식$${bb}$$/수식$$개  \n" \
              "∴ b = $$수식$${bb}$$/수식$$\n" \
              "연립방정식 $$수식$${aaa}$$/수식$$       $$수식$$``$$/수식$$   의 해는 {list3}의 $$수식$${cc}$$/수식$$개\n\n" \
              "∴ c = $$수식$${cc}$$/수식$$\n" \
              "∴ a + b + c = $$수식$${dd}$$/수식$$"\

    a = np.random.randint(2, 10)
    b= np.random.randint(1, 10)
    c=np.random.randint(1, 10)
    while b==c:
        c = np.random.randint(1, 10)
    list=""
    liste=[]
    for i in range(b+1):
        for j in range(b+1):
            if i +a*j ==b:
                liste.append([i,j])
    if len(liste) > 0:
        for i in range(len(liste) - 1):
            list = list + "(" + str(liste[i][0]) + ", " + str(liste[i][1]) + ") ,"
        list = list + "(" + str(liste[-1][0]) + ", " + str(liste[-1][1]) + ")"
    aa= len(liste)
    eq="x + " + str(a) +"y = " + str(b)+"$$수식$$$$/수식$$"
    eqq1 = "x + " + str(a) +"y = " + str(b)
    d = np.random.randint(2, 10)
    e= np.random.randint(1, 10)
    f = np.random.randint(1, 10)
    while e == f:
        f = np.random.randint(1, 10)
    eq2 =str(d) +"x + y = " + str(e) +"$$수식$$$$/수식$$"
    eqq2 =str(d) +"x + y = " + str(e)
    list2 = ""
    liste = []
    for i in range(e + 1):
        for j in range(e + 1):
            if d*i + j == e:
                liste.append([i,j])

    if len(liste) > 0:
        for i in range(len(liste) - 1):
            list2 = list2 + "(" + str(liste[i][0]) + ", " + str(liste[i][1]) + ") ,"
        list2 = list2 + "(" + str(liste[-1][0]) + ", " + str(liste[-1][1]) + ")"
    ff= len(liste)

    aaa ="{cases{" + eqq1 + "#" + eqq2 + "}}"
    eq3 = eqq1
    eq4 = eqq2
    list3 = ""
    liste = []
    for i in range(max(b + 1, e + 1)):
        for j in range(max(b + 1, e + 1)):
            if i + a * j == b and d*i +j==e:
                liste.append([i,j])

    if len(liste) > 0:
        for i in range(len(liste) - 1):
            list3 = list3 + "(" + str(liste[i][0]) + ", " + str(liste[i][1]) + ") ,"
        list3 = list3 + "(" + str(liste[-1][0]) + ", " + str(liste[-1][1]) + ")"
    cc = len(liste)
    answ = aa+ff+cc
    dd = str(aa) +" + " + str(ff) + " + " + str(cc) + " = " + str(answ)

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, eq2=eq2, aaa=aaa, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(aaa=aaa, eq3=eq3, list=list, aa=aa, eq4=eq4, list2=list2, bb=ff, list3=list3, cc=cc, answ=answ, dd=dd)

    return stem, answer, comment

#중2-1-2-117
def expressions212_Stem_094():
    stem = "\n주사위를 모두 $$수식$${num}$$/수식$$번 던져 $$수식$${side1}$$/수식$$의 눈이 x번, $$수식$${side2}$$/수식$$의 눈\n" \
           "이 $$수식$${time2}$$/수식$$번, $$수식$${side3}$$/수식$$의 눈이 y번, $$수식$${side4}$$/수식$$의 눈이 $$수식$${time4}$$/수식$$번 나왔고,\n" \
           "$$수식$${side5}$$/수식$$의 눈과 $$수식$${side6}$$/수식$$의 눈이 나오지 않았다. 나온 눈의 수\n" \
           "합이 $$수식$${total}$$/수식$$라 할 때, 연립방정식을 이용하여 해를\n" \
           "구하면?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$이므로 $$수식$${eq2}$$/수식$$\n" \
              "$$수식$${eq3}$$/수식$$이므로\n" \
              "$$수식$${eq4}$$/수식$$\n" \
              "∴ $$수식$${aa}$$/수식$$\n\n" \
              "x, y는 자연수이므로 $$수식$${eq2}$$/수식$$의 해는\n" \
              "$$수식$${list}$$/수식$$\n" \
              "$$수식$${eq4}$$/수식$$    의 해는 $$수식$${list2}$$/수식$$\n" \
              "따라서 연립방정식의 해는 {list2}\n" \
              "따라서 연립방정식의 해는 {list2}이다."

    sides =[1,2,3,4,5,6]
    picked = []
    while len(picked)<4:
        dd = sides[np.random.randint(0, 6)]
        if dd not in picked:
            picked.append(dd)
    picked.sort()
    side1 = picked[0]
    side2 = picked[1]
    side3 = picked[2]
    side4 = picked[3]

    side5= side6=0
    for x in sides:
        if x not in picked:
            side5 = x
            break
    for x in sides:
        if x not in picked and x!=side5:
            side6 = x
            break
    x= np.random.randint(1, 5)
    time2 = np.random.randint(1, 5)
    y = np.random.randint(1, 5)
    time4 = np.random.randint(1, 5)
    num = x+y+time2+time4
    eq = "x + " + str(time2) +"+ y + " + str(time4) + " = " + str(num) + "$$수식$$$$/수식$$"
    eq2 = "x + y = " + str(num-time2-time4) +"$$수식$$$$/수식$$"
    total = picked[0]*x + picked[1]*time2 + picked[2]*y +  picked[3]*time4
    eq3 = str(picked[0]) +"x + " + str(picked[1]) + "$$수식$$TIMES$$/수식$$" + str(time2) + " + " + str(picked[2]) +"y + " + str(picked[3]) +"$$수식$$TIMES$$/수식$$" + str(time4) + " = " + str(total) + "$$수식$$$$/수식$$"
    total2 = total -  picked[1]*time2 -picked[3]*time4
    eq4 = str(picked[0]) +"x + " + str(picked[2]) +"y = " + str(total2)
    if picked[0] == 1:
        eq3 = "x + " + str(picked[1]) + "$$수식$$TIMES$$/수식$$" + str(time2) + " + " + str(picked[2]) + "y + " + str(
            picked[3]) + "$$수식$$TIMES$$/수식$$" + str(time4) + " = " + str(total) + "$$수식$$$$/수식$$"
        eq4 = "x + " + str(picked[2]) +"y = " + str(total2)

    liste = []
    for i in range(1,num-time2-time4):
        for j in range(1, num-time2-time4):
            if i+j ==num-time2-time4:
                liste.append([i,j])
    list=""
    if len(liste)>0:
        for i in range(len(liste)-1):
            list = list + "(" + str(liste[i][0]) +", " + str(liste[i][1]) +") ,"
        list = list + "(" + str(liste[-1][0]) +", " + str(liste[-1][1]) +")"

    list2 = "(" + str(x) + ", " + str(y) +")"
    answ = list2
    case = "{cases{" + eq2 + "#" + eq4 + "}}"
    bb=[]

    dd=[[liste[-1][0],liste[-1][1]]]
    num = liste[-1][0] + liste[-1][1] + time2 + time4
    while len(bb)<4:
        v = np.random.randint(1, 13+x)
        h = np.random.randint(1, 13+y)
        if [v,h] not in dd and v+h<=num:
            dd.append([v,h])
            bb.append("(" + str(v) + ", " + str(h) +")")

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    aa = "{cases{x + y = " + str(num-time2-time4) +"#" + eq4 +"}}"

    stem = stem.format(num=num, side1=side1, time2=time2, side2=side2, side3=side3, side4=side4, time4=time4, total=total,
                       side6=side6, side5=side5, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(aa=aa, eq=eq, eq2=eq2, eq3=eq3, eq4=eq4, list=list, list2=list2, answ=answ)

    return stem, answer, comment


#중2-1-2-118
def expressions212_Stem_095():
    stem = "\n순서쌍 {eq}   {temp} x, y에 대한 연립방정식\n" \
           "$$수식$${aa}$$/수식$$         $$수식$$``$$/수식$$    의 해일 때, a - b의 값은? (단,\n\n" \
           "b는 상수이다.)" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x = {eq1}, y = {eq2}$$수식$$``$$/수식$${temp2} {aa1}  에 대입\n" \
              "하면\n" \
              "{eq3}\n" \
              "{eq4}  ∴ a =  $$수식$$``$$/수식$$  $$수식$${aaaa}$$/수식$$\n" \
              "따라서 해가 {ansss}$$수식$$``$$/수식$$이므로 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp3}\n" \
              "{aa2}에 대입하면\n" \
              "{b1}   ∴ b = $$수식$${bbbb}$$/수식$$\n" \
              "∴ a - b = {ans11}"

    l = np.random.randint(1, 5)
    ll = np.random.randint(1, 5)
    while l==ll:
        ll = np.random.randint(1, 5)
    a = np.random.randint(1, 10) * -1
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)
    aaaa = int((c + b * ll - a * l) / ((a * -1) + (b)))
    while (c+b*ll-a*l)%((a * -1) +(b))!=0 or aaaa==l or aaaa==ll:
        l = np.random.randint(1, 5)
        ll = np.random.randint(1, 5)
        while l == ll:
            ll = np.random.randint(1, 5)
        a = np.random.randint(1, 10) * -1
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 10)
        aaaa = int((c + b * ll - a * l) / ((a * -1) + (b)))

    eq1 = str(l) + " - a" + "$$수식$$$$/수식$$"
    eq2 = "a - " + str(ll)
    temp = proc_jo(ll,0)
    temp2 = proc_jo(ll, 4)
    eq = "$$수식$$("+eq1 +", " +eq2+"     )$$/수식$$"


    aa1 = str(a) +"x + "
    eq3 = str(a) +"(" + eq1 +") + "
    eq4 = str(a*l) + " + " + str(a*-1) +"a + "
    if a==-1:
        aa1 = "x + "
        eq3 ="-(" + eq1 +") + "
        eq4 = str(a * l) + " + a + "
    if b!=1:
        aa1 = aa1 + str(b) +"y = " + str(c)
        eq3 = eq3 + str(b) +"(" + eq2+"$$수식$$``$$/수식$$   ) = " + str(c)+ "$$수식$$$$/수식$$"
        eq4 = eq4 + str(b) +"a - " + str(b*ll) + " = " + str(c)+ "$$수식$$$$/수식$$"
    else:
        aa1 = aa1 +  " y = " + str(c)
        eq3 = eq3 +  "(" + eq2 + "$$수식$$``$$/수식$$   ) = " + str(c)+ "$$수식$$$$/수식$$"
        eq4 = eq4 + "a - " + str(ll) + " = " + str(c)+ "$$수식$$$$/수식$$"

    x = l - aaaa
    y = aaaa - ll
    temp3 = proc_jo(y, 4)
    ansss ="(" + str(x) +", " + str(y) + ")"+ "$$수식$$$$/수식$$"

    p = np.random.randint(1, 10)
    q = np.random.randint(1, 10)*-1
    while ((q - p * x )% y) != 0:
        p = np.random.randint(1, 10)
        q = np.random.randint(1, 10) * -1
    aa2 = str(p) +"x - by = " + str(q)
    b1 = str(p*x) +" - " + str(y) +"b = " + str(q)+ "$$수식$$$$/수식$$"
    g=y
    if y<0:
        g = y*-1
        b1 = str(p*x) +" + " + str(g) +"b = " + str(q)
        if y==-1:
            b1 = str(p * x) + " + b = " + str(q)
    if y==1:
        b1 = str(p * x) + " - b = " + str(q) + "$$수식$$$$/수식$$"

    bbbb = int((q-p*x)/g)
    answ = aaaa-bbbb
    ans11 = str(aaaa) + " - " + str(bbbb) + " = " + str(answ)+ "$$수식$$$$/수식$$"
    if bbbb<0:
        ans11 = str(aaaa) + " - (" + str(bbbb) + ") = " + str(answ)+ "$$수식$$$$/수식$$"
    aa = "{cases{" +aa1 +"#" + aa2 +"}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    aaaa = "$$수식$$$$/수식$$"+str(aaaa)
    stem = stem.format(eq=eq, aa=aa, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(b1=b1, eq1=eq1, eq2=eq2, temp2=temp2, aa1=aa1, aa2=aa2, eq3=eq3, eq4=eq4, ansss=ansss, temp3=temp3,aaaa=aaaa, bbbb=bbbb, ans11=ans11,x=x, y=y )

    return stem, answer, comment


#중2-1-2-119
#    eq2 = "{cases{" +aa1 +"CDOTS #" + aa2 +"CDOTS}}" ㉠ ㉡ 넣으면 에러뜸
def expressions212_Stem_096():
    stem = "\nx, y에 대한 연립방정식 $$수식$${eq}$$/수식$$    $$수식$$``$$/수식$$      의 해가\n\n" \
           "x = $$수식$${x}$$/수식$$, y = b일 때, a + b의 값은? (단, a는 상\n" \
           "수이다.)" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${eq2}$$/수식$$\n\n" \
              "㉠에  ($$수식$${x}$$/수식$$, b)를 대입하면\n" \
              "$$수식$${eq3}$$/수식$$,  $$수식$${b1}$$/수식$$   ∴ b = $$수식$${bbbb}$$/수식$$\n" \
              "㉡에 $$수식$${tru}$$/수식$${temp} 대입하면\n" \
              "$$수식$${eq4}$$/수식$$    ∴ a = $$수식$${aaaa}$$/수식$$\n" \
              "∴ a + b = $$수식$${aaaa}$$/수식$$ + $$수식$${bbbb1}$$/수식$$ = ∴ $$수식$${answ}$$/수식$$"

    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)
    x= np.random.randint(1, 5)
    while c==a*x or (c-a*x)%b!=0:
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 10)
        x = np.random.randint(1, 5)
    aa1 = str(a) +"x + "
    if a==1:
        aa1 = "x + "
    if b==1:
        aa1 = aa1 + "y = " + str(c)
    else:
        aa1 = aa1 + str(b) +"y = " + str(c)
    eq3 = str(a) +"$$수식$$TIMES$$/수식$$" + str(x) + " + " + str(b) +"$$수식$$TIMES$$/수식$$ b = " + str(c) + "$$수식$$$$/수식$$"
    b1 = str(b) +"b = " + str(c-a*x)
    bbbb = int((c-a*x)/b)
    temp = proc_jo(bbbb, 4)
    tru = "(" + str(x) +", " + str(bbbb)+")"+ "$$수식$$$$/수식$$"
    a = np.random.randint(1, 10)
    b = np.random.randint(10, 50)
    while (b-(bbbb*a))%x!=0:
        a = np.random.randint(1, 10)
        b = np.random.randint(10, 50)
    aa2 = "ax + " + str(b) +"y = " + str(b)
    if b==1:
        aa2 = "ax + y = " + str(b)

    eq4 = "a $$수식$$TIMES$$/수식$$ "+str(x) +" + " + str(a) + " $$수식$$TIMES$$/수식$$ " + str(bbbb) + " = " + str(b)+ "$$수식$$$$/수식$$"
    aaaa = int((b-(bbbb*a))/x)
    answ = aaaa+bbbb
    eq= "{cases{" +aa1 +"#" + aa2 +"}}"
    eq2 = "{cases{" +aa1 +"CDOTS`CDOTS`"+problm1()+"#" + aa2 +"CDOTS`CDOTS`"+problm2()+ "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    bbbb1=""
    if bbbb<0:
        bbbb1 = "(" + str(bbbb)+")"
    temp = proc_jo(bbbb, 4)
    stem = stem.format(eq=eq, x=x, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(bbbb1=bbbb1, temp=temp, tru=tru, eq2=eq2, eq3=eq3, eq4=eq4, x=x, aaaa=aaaa, bbbb=bbbb, answ=answ, b1=b1)

    return stem, answer, comment

#중2-1-2-120.... stem_166


#중2-1-2-121
def expressions212_Stem_097():
    stem = "\nx, y에 대한 연립방정식 $$수식$${aa}$$/수식$$ $$수식$$``$$/수식$$             의 해\n\n" \
           "가 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$일 때, 상수 a, b에 대하여\n" \
           "a + b의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp} $$수식$${aa}$$/수식$$$$수식$$``$$/수식$$             에 대입하면\n" \
              "$$수식$${vv}$$/수식$$\n\n" \
              "㉠ $$수식$$TIMES$$/수식$$ $$수식$${mul}$$/수식$$ - ㉡을 하면 $$수식$${cal}$$/수식$$     ∴ b = $$수식$${bbbb}$$/수식$$\n" \
              "b = $$수식$${bbbb}$$/수식$${temp2} ㉠에 대입하면 $$수식$${cal2}$$/수식$$    ∴ a = $$수식$${aaaa}$$/수식$$\n" \
              "∴ a + b = $$수식$${answ}$$/수식$$"


    aaaa = np.random.randint(1, 10)
    bbbb = np.random.randint(1, 10)
    x = np.random.randint(1, 4)
    y = np.random.randint(1, 10)
    a = aaaa*x - bbbb*y
    b = np.random.randint(2, 4)
    c = np.random.randint(1, 10)
    d = b*aaaa*x + c*bbbb*y
    mul = b
    while (-mul*y-c*y)==0 or a==0 or (a*mul-d)%(-mul*y-c*y)!=0 or (a+(y*bbbb))%a!=0:
        aaaa = np.random.randint(1, 10)
        bbbb = np.random.randint(1, 10)
        x = np.random.randint(1, 4)
        y = np.random.randint(1, 10)
        a = aaaa * x - bbbb * y
        b = np.random.randint(2, 4)
        c = np.random.randint(1, 10)
        d = b * aaaa * x + c * bbbb * y
        mul = b


    aa1 = "ax - by = " + str(a)
    vv1 = str(x)+"a - "
    if x==1:
        vv1 = "a - "
    if y!=1:
        vv1 = vv1 + str(y)+"b = "+ str(a)
    else:
        vv1 = vv1 +"b = "+ str(a)

    aa2 = str(b)+"ax + "
    vv2 = str(b*x)+"a + "
    if b==1:
        aa2 = "ax + "
    if c==1:
        aa2 = aa2 +"by = " + str(d)
    else:
        aa2 = aa2 +str(c)+"by = " + str(d)
    if b*x==1:
        vv2 = "a + "
    if c*y!=1:
        vv2 = vv2 +str(c*y) + "b = " + str(d)
    else:
        vv2 = vv2 + "b = " + str(d)


    cal = str(-mul*y-c*y) +"b = " + str((a*mul-d))
    cal2 = str(x) + "a - "+str(y*bbbb) +" = " + str(a)
    if x==1:
        cal2 = "a - "+str(y*bbbb) +" = " + str(a)
    answ = aaaa+bbbb
    temp = proc_jo(y, 4)
    aa = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + vv1 + "#" + vv2 + "}}"
    temp2= proc_jo(x, 4)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(aa=aa, x=x, y=y, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, x=x, y=y, aa=aa, vv=vv, mul=mul, temp=temp, temp2=temp2, cal=cal, cal2=cal2,
                             aaaa=aaaa, bbbb=bbbb)

    return stem, answer, comment

#중2-1-2-122
# ㉠, ㉡ 에러
def expressions212_Stem_098():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$    $$수식$$``$$/수식$$              의 해가\n\n" \
           "x = a, y = b일 때, a + b의 값은?"   \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "㉠에서 y를 x의 식으로 나타내면\n" \
              "{eq1} CDOTS $$수식$$``$$/수식$$㉢" \
              "\n㉢을 ㉡에 대입하면 {eq2}\n" \
              "{eq3}   ∴ x = $$수식$${x}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$${temp} ㉢에 대입하면 y = $$수식$${y}$$/수식$$\n" \
              "따라서 a = $$수식$${x}$$/수식$$, b = $$수식$${y}$$/수식$$이므로 a + b = $$수식$${answ}$$/수식$$"

    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    a = np.random.randint(1, 10)*-1
    b = a*x - y
    while b==1 or b==0:
        x = np.random.randint(1, 10)
        y = np.random.randint(1, 10)
        a = np.random.randint(1, 10) * -1
        b = a * x - y
    aa1 = "y - " + str(-1*b) +" = " + str(a) +"x CDOTS`CDOTS`"+ problm1()
    eq1 = str(a) +"x + " + str(-1*b) + "$$수식$$$$/수식$$"
    if a==-1:
        eq1 = "- x + " + str(-1*b) + "$$수식$$$$/수식$$"
    temp = proc_jo(x, 4)
    c = np.random.randint(1, 10)
    d = np.random.randint(1, 10)
    e = x*c + y*d
    aa2 = str(c) +"x + " + str(d) +"y = " + str(e) +"CDOTS`CDOTS`"+ problm2()
    eq2 =  str(c) +"x + " + str(d) + "(" + str(a) +"x + " + str(-1*b) + ") = "+ str(e)
    eq3 = str(d*a+c) + "x = " + str((e-(-1*b)*d))
    answ = x+y
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp=temp, answ=answ, eq1=eq1, x=x,y=y, eq2=eq2, eq3=eq3)

    return stem, answer, comment

#중2-1-2-123
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_099():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$  $$수식$$``$$/수식$$              의 해가 x, y의 순서쌍\n\n" \
           "(a,b)일 때, ab의 값은?"   \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${vv}$$/수식$$\n\n" \
              "㉠+㉡$$수식$$TIMES$$/수식$$$$수식$${mul}$$/수식$${temp} 하면 $$수식$${eq2}$$/수식$$    ∴ y = $$수식$${y}$$/수식$$\n" \
              "y = $$수식$${y}$$/수식$${temp2} ㉡에 대입하면 $$수식$${eq3}$$/수식$$    ∴ x = $$수식$${x}$$/수식$$\n" \
              "따라서 연립ㄹ방정식의 해가 (a,b)이므로\n" \
              "a = $$수식$${x}$$/수식$$, b = $$수식$${y}$$/수식$$\n" \
              "∴ ab = $$수식$${answ}$$/수식$$"

    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    mul =np.random.randint(2, 5)
    d = np.random.randint(1, 4) *-1
    a = d*mul*-1
    b = np.random.randint(1, 10)
    c = a*x + b*y
    aa1 = str(a) +"x + "
    if a==1:
        aa1 = "x + "
    if b==1:
        aa1 = aa1 + "y = " + str(c)
    else:
        aa1 = aa1 +str(b)+"y = " + str(c)


    e = np.random.randint(1, 10)
    f = d * x + e * y
    aa2 = str(d) +"x + "
    eq3=str(d) +"x + "
    if d==-1:
        aa2 = "-x + "
        eq3 ="x + "
    if e==1:
        aa2 = aa2 + "y = " + str(f)
    else:
        aa2 = aa2 + str(e)+"y = " + str(f)
    eq3 = eq3 + str(y*e) + " = " + str(f)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + aa1 + "`CDOTS`CDOTS`"+ problm1()+"#" + aa2 + "`CDOTS`CDOTS`"+ problm2()+"}}"
    temp = proc_jo(mul, 4)
    eq2 = str(b+(mul*e)) +"y = " + str(c+mul*f)

    answ = x*y
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    temp2 = proc_jo(y, 4)
    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp2=temp2, mul=mul, temp=temp, answ=answ, eq=eq, vv=vv, x=x, y=y, eq2=eq2, eq3=eq3)

    return stem, answer, comment
#중2-1-2-124
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_100():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$ 에서 x 또는 y\n\n" \
           "를 소거할 때 필요한 식을 보기에서 모두 고른 것\n은?$$표$$\n" \
           "㈀ {op1}\n" \
           "㈁ {op2}\n" \
           "㈂ {op3}\n" \
           "㈃ {op4}\n" \
           "㈄ {op5}\n$$/표$$"   \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "{list}{temp} 하면 $$수식$${eq1}$$/수식$$\n" \
              "\t즉, x가 소거된다.\n" \
              "{list2}{temp2} 하면 $$수식$${eq2}$$/수식$$\n" \
              "\t즉, y가 소거된다.\n" \
              "따라서 필요한 식은 {answ}이다."

    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = a-b
    aa1 = str(a)+"x`-`"
    if a==1:
        aa1 = "x`-`"
    if b==1:
        aa1 = aa1 + "`y`=`"+str(c)
    else:
        aa1 =aa1 + str(b) +"`y`=`" + str(c)
    aa1 = aa1 +"`cdots`cdots`"+ problm1()

    d = np.random.randint(1, 10)
    e = np.random.randint(1, 10)
    f = d+e
    aa2 = str(d) + "``x`+`"
    if d == 1:
        aa2 = "``x`+`"
    if e == 1:
        aa2 = aa2 + "`y`=`" + str(f)
    else:
        aa2 = aa2 + str(e) + "`y`=`" + str(f)
    aa2 = aa2 + "`cdots`cdots`" + problm2()
    eq = "cases{``" + aa1 + "#" + aa2 + "}"
    lcm1 = lcm(a, d)
    lcm2 = lcm(b, e)
    pp1 = int(lcm1/a)
    pp2 = int(lcm1/d)
    rr1 = int(lcm2/b)
    rr2 = int(lcm2/e)
    eq1 = str((pp1*b*-1)-(pp2*e)) +"y = " + str(pp1*c-pp2*f)
    eq2 = str((rr1*a+rr2*d)) +"x = " + str(rr1*c+rr2*f)
    temp = proc_jo(pp2, 4)
    temp2 = proc_jo(rr2, 4)
    bb=[]
    ans11="㉠$$수식$$TIMES$$/수식$$" + str(pp1) +"-㉡$$수식$$TIMES$$/수식$$" + str(pp2)
    ans12 = "㉠$$수식$$TIMES$$/수식$$" + str(rr1) +"+㉡$$수식$$TIMES$$/수식$$" + str(rr2)
    bb.append(ans11)
    bb.append(ans12)
    while len(bb)<5:
        gg = np.random.randint(1, 10)
        ggg = np.random.randint(1, 10)
        if gg*a !=ggg*d and gg*b != ggg*e:
            bb.append("㉠$$수식$$TIMES$$/수식$$" + str(gg) +"-㉡$$수식$$TIMES$$/수식$$" + str(ggg))
            bb.append("㉠$$수식$$TIMES$$/수식$$" + str(gg) + "+㉡$$수식$$TIMES$$/수식$$" + str(ggg))
    gg = np.random.randint(0, 4)
    if gg == 0:
        op1 = bb[0]
        op2 = bb[1]
        op3 = bb[2]
        op4 = bb[3]
        op5 = bb[4]
        answ = "㈀, ㈁"
        ans = "①"
        x1 = answ
        x2 = "㈁, ㈃"
        x3 = "㈃, ㈄"
        x4 = "㈂, ㈄"
        x5 = "㈀, ㈂"
        list = "㈀ " + bb[0]
        list2 = "㈁ " + bb[1]
    elif gg == 1:
        op1 = bb[4]
        op2 = bb[2]
        op3 = bb[3]
        op4 = bb[0]
        op5 = bb[1]
        ans = "③"
        answ = "㈃, ㈄"
        x1 = "㈀, ㈁"
        x2 = "㈁, ㈃"
        x3 = answ
        x4 = "㈂, ㈃"
        x5 = "㈀, ㈂"
        list = "㈃ " + bb[0]
        list2 = "㈄ " + bb[1]
    elif gg == 2:
        op1 = bb[3]
        op2 = bb[0]
        op3 = bb[4]
        op4 = bb[1]
        op5 = bb[2]
        ans = "②"
        answ = "㈁, ㈃"
        x1 = "㈀, ㈁"
        x2 = answ
        x3 = "㈃, ㈄"
        x4 = "㈁, ㈄"
        x5 = "㈂, ㈃"
        list = "㈁ " + bb[0]
        list2 = "㈃ " + bb[1]

    else:
        op1 = bb[3]
        op2 = bb[4]
        op3 = bb[0]
        op4 = bb[1]
        op5 = bb[5]
        ans = "④"
        answ = "㈂, ㈃"
        x1 = "㈁, ㈃"
        x2 = "㈃, ㈄"
        x3 = "㈀, ㈄"
        x4 = answ
        x5 = "㈀, ㈂"
        list = "㈂ " + bb[0]
        list2 = "㈃ " + bb[1]


    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, op1=op1, op2=op2, op3=op3, op4=op4, op5=op5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=list, list2=list2, temp=temp, temp2=temp2, eq1=eq1, eq2=eq2, answ=answ)

    return stem, answer, comment

#중2-1-2-125
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_101():
    stem = "\nx, y에 대한 연립방정식 $$수식$${eq}$$/수식$$  $$수식$$``$$/수식$$             의 해가\n\n" \
           "x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$일 때, 상수 a, b에 대하여 a - b\n" \
           "의 값은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp} $$수식$${eq}$$/수식$$  $$수식$$``$$/수식$$             에 대입하면\n\n" \
              "$$수식$${mm}$$/수식$$  $$수식$$``$$/수식$$             ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "㉠-㉡을 하면 $$수식$${b1}$$/수식$$      ∴ b = $$수식$${bbbb}$$/수식$$\n" \
              "b = $$수식$${bbbb}$$/수식$${temp2} ㉠에 대입하면\n" \
              "{a1}      ∴ a = $$수식$${aaaa}$$/수식$$\n" \
              "∴ a - b = $$수식$${aaaa}$$/수식$$ - ($$수식$${bbbb}$$/수식$$) = $$수식$${answ}$$/수식$$"

    aaaa = np.random.randint(0, 10)
    bbbb = np.random.randint(0, 10)*-1
    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    a = aaaa*x + bbbb*y
    gcd1 = gcd(gcd(x, abs(a)), y)
    pp1 = int(x / gcd1)
    pp2 = int(y / gcd1)
    pp3 = int(a / gcd1)
    
    b = np.random.randint(2, 10)
    c = np.random.randint(2, 10)
    d = b * aaaa * x + c * bbbb * y
    gcd2 = gcd(gcd(abs(x * b), c * y), abs(d))
    mm3 = int(x*b/gcd2)
    mm4 = int(c*y/gcd2)
    mm5 = int(d/gcd2)
    while mm3!=pp1 or mm4==pp2:
        aaaa = np.random.randint(1, 10)
        bbbb = np.random.randint(1, 10) * -1
        x = np.random.randint(1, 10)
        y = np.random.randint(1, 10)
        a = aaaa * x + bbbb * y
        while a==0:
            x = np.random.randint(1, 10)
            y = np.random.randint(1, 10)
            a = aaaa * x + bbbb * y
        gcd1 = gcd(gcd(x, abs(a)), y)
        pp1 = int(x / gcd1)
        pp2 = int(y / gcd1)
        pp3 = int(a / gcd1)

        b = np.random.randint(2, 10)
        c = np.random.randint(2, 10)
        d = b * aaaa * x + c * bbbb * y
        while d==0:
            b = np.random.randint(2, 10)
            c = np.random.randint(2, 10)
            d = b * aaaa * x + c * bbbb * y
        gcd2 = gcd(gcd(abs(x * b), c * y), abs(d))
        mm3 = int(x * b / gcd2)
        mm4 = int(c * y / gcd2)
        mm5 = int(d / gcd2)
        
    aa1 = "ax + by = " +str(a)
    mm1 = str(x) + "a + "
    if x==1:
        mm1 = "a + "
    if y==1:
        mm1 = mm1 + "b = " + str(a)
    else:
        mm1 = mm1 + str(y) + "b = " + str(a)

    vv1 = str(pp1) +"a + "
    if pp1==1:
        vv1 = "a + "
    if pp2==1:
        vv1 = vv1 + "b = " + str(pp3) + problm1()
    else:
        vv1 = vv1 + str(pp2) + "b = " + str(pp3)+ problm1()


    aa2 = str(b) +"ax + " + str(c) + "by = " + str(d)
    mm2 = str(x*b) + "a + " + str(c*y) +"b = " + str(d)

    vv2 = str(mm3) + "a + "
    if mm3==1:
        vv2 = "a + "
    if mm4==1:
        vv2 =vv2 + "b = " + str(mm5) + problm2()
    else:
        vv2 = vv2 + str(mm4) + "b = " + str(mm5)+ problm2()

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    mm = "{cases{" + mm1 + "#" + mm2 + "}}"
    vv = "{cases{" + vv1 + "#" + vv2 + "}}"
    b1 = str(pp2-mm4) +"b = " + str(pp3-mm5)
    if pp2-mm4==-1:
        b1 = "-b = " + str(pp3-mm5)
    elif pp2-mm4==1:
        b1 = "b = " + str(pp3 - mm5)

    a1 = "a - " + str(abs(pp2*bbbb)) + " = " +str(pp3)
    answ = aaaa-bbbb

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    temp = proc_jo(y, 4)
    temp2 = proc_jo(bbbb,4)
    stem = stem.format(eq=eq, x=x, y=y, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(x=x, y=y, temp=temp, temp2=temp2, b1=b1, a1=a1, aaaa=aaaa, bbbb=bbbb, vv=vv, mm=mm,eq=eq, answ=answ)

    return stem, answer, comment

#중2-1-2-126
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_102():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$  $$수식$$``$$/수식$$             의 해가 x = a, y = b일\n\n" \
           "때, $$수식$$a ^2$$/수식$$ + $$수식$$b ^2$$/수식$$의 값은?\n"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "연립방정식 $$수식$${vv}$$/수식$$  $$수식$$``$$/수식$$             에서 ㉠을 ㉡에\n" \
              "대입하면\n" \
              "{eq2}\n" \
              "∴ y = $$수식$${y}$$/수식$$\n" \
              "y = $$수식$${y}$$/수식$${temp} ㉠에 대입하면 {xx1}\n" \
              "따라서 a = $$수식$${x}$$/수식$$, b = $$수식$${y}$$/수식$$이므로 $$수식$$a ^2$$/수식$$ + $$수식$$b ^2$$/수식$$ = $$수식$${answ}$$/수식$$"

    x = np.random.randint(1, 10)
    y =  np.random.randint(1, 10)
    a= np.random.randint(1, 10)
    b = a*y-x
    while b<=0:
        x = np.random.randint(1, 10)
        y = np.random.randint(1, 10)
        a = np.random.randint(1, 10)
        b = a * y - x
    aa1 = "x = " + str(a) +"y - " + str(abs(b))
    if a==1:
        aa1 = "x = y - " + str(abs(b))

    c = np.random.randint(2, 10)
    d = np.random.randint(1, 10)
    e = c*x - d*y
    aa2 = str(c) +"x - "
    eq2 = str(c) +"("+ str(a) +"y - " + str(abs(b))+") - "
    if a==1:
        eq2 = str(c)+"(y - " + str(abs(b))+") - "
    if d==1:
        aa2 = aa2 + "y = " + str(e)
        eq2 = eq2 + "y = " + str(e)
    else:
        aa2 = aa2 + str(d) +"y = " + str(e)
        eq2 = eq2 + str(d) +"y = " + str(e)
    eq2 = eq2 + " , " + str(c * a) + "y - " + str(abs(c * b)) + " - "
    if d==1:
        eq2 = eq2 + "y = " + str(e)
    else:
        eq2 = eq2 + str(d) +"y = "+ str(e)
    xx1 = "x = " +  str(a*y) +" - " + str(abs(b)) + " = " + str(x)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + aa1 + "`cdots`cdots`"+problm1()+"#" + aa2 + "`cdots`cdots`"+problm2()+"}}"
    answ = x**2 +y**2
    temp = proc_jo(y, 4)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(x=x, y=y, temp=temp, xx1=xx1, eq2=eq2, vv=vv, eq=eq, answ=answ)

    return stem, answer, comment

#중2-1-2-127
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_103():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$  $$수식$$``$$/수식$$             의 해가 일차방\n\n" \
           "정식 {eq2}을 만족시킬 때, 상수 a의\n" \
           "값은?\n"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "㉠에서 x를 y의 식으로 나타내면\n" \
              "{eq3} $$수식$$CDOTS CDOTS$$/수식$$ ㉢\n" \
              "㉢을 ㉡에 대입하면 {eq4}\n" \
              "{y1}     ∴ y = $$수식$${yy}$$/수식$$\n" \
              "y = $$수식$${yy}$$/수식$${temp} ㉢에 대입하면 x = $$수식$${xx}$$/수식$$\n" \
              "x = $$수식$${xx}$$/수식$$, y = $$수식$${yy}$$/수식$${temp} {eq2}에 대입하면\n" \
              "{eq5}           ∴ a = $$수식$${answ}$$/수식$$"

    x = 1/np.random.randint(2, 5)*-1
    y = 1/np.random.randint(2, 5)*-1
    a = np.random.randint(1, 10)
    while (x-y*a)%1!=0:
        a = np.random.randint(1, 10)
        x = 1 / np.random.randint(2, 5) * -1
        y = 1/np.random.randint(2, 5) * -1
    b = int(x-y*a)
    aa1 = "x - " + str(a) +"y = " + str(b)
    eq0 = str(a) +"y + " + str(b)
    if a==1:
        aa1 = "x - y = " + str(b)
        eq0 = "y + " + str(b)
    eq3 = "x = " + eq0
    c = np.random.randint(1, 10)
    d = np.random.randint(1, 10)
    while (c*x-d*y)%1!=0:
        c = np.random.randint(1, 10)
        d = np.random.randint(1, 10)
    e = int(c*x-d*y)
    aa2 = str(c) +"x - "
    eq4 = str(c) +"(" + eq0 +") - "
    if c==1:
        aa2 = "x - "
        eq4 = "(" + eq0 +") - "
    if d==1:
        aa2 = aa2 + "y = " + str(e)
        eq4 = eq4 + "y = " + str(e)
    else:
        aa2 = aa2 +str(d) +"y = " + str(e)
        eq4 = eq4 +str(d) +"y = " + str(e)
    y1 = str(c*a-d) +"y = " + str(e-c*b)
    yy = "-$$수식$$1 over {"+str(abs(int(1/y)))+"}$$/수식$$"
    xx = "-$$수식$$1 over {"+str(abs(int(1/x)))+"}$$/수식$$"
    temp = proc_jo(int(1/y),4)

    h = np.random.randint(1, 10)
    answ = np.random.randint(1, 10)*-1
    while (h*x + answ*y)==0 or (h*x + answ*y)%1!=0:
        h = np.random.randint(1, 10)
        answ = np.random.randint(1, 10)
    eq2 = str(h) +"x + ay + " + str(abs(int(h*x + answ*y))) + " = " + str(0)
    if h==1:
        eq2 = "x + ay + " + str(abs(int(h*x + answ*y))) + " = " + str(0)
    j = x*h
    eq5 = str(int(j)) + " - $$수식$$1 over {"+str(abs(int(1/y)))+"}$$/수식$$a + " + str(int(abs(h*x + answ*y))) + " = " +str(0)
    if j%1!=0:
        gcd1 = gcd(abs(int(1/x)), abs(h))
        t = int(1/x/gcd1)
        tt = int(h/gcd1)
        eq5 = "-$$수식$${"+str(tt)+"} over {"+str(abs(int(t)))+"}$$/수식$$ - $$수식$$1 over {"+str(abs(int(1/y)))+"}$$/수식$$a + " + str(int(abs(h*x + answ*y))) + " = " +str(0)

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    eq = "{cases{" + aa1 + "`cdots`cdots`"+problm1()+"#" + aa2 + "`cdots`cdots`"+problm2()+"}}"

    stem = stem.format(eq=eq, eq2=eq2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(y1=y1, eq4=eq4, eq5=eq5,eq2=eq2,  temp=temp, eq3=eq3, yy=yy, xx=xx, eq=eq, answ=answ)

    return stem, answer, comment

#중2-1-2-128
def expressions212_Stem_104():
    stem = "\n다음 일차방정식 중 연립방정식 $$수식$${eq}$$/수식$$  $$수식$$``$$/수식$$             의\n\n" \
           "해를 한 해로 갖지 않는 것을 모두 고르면? (정답\n" \
           "2개)"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "{aa1}{temp} {aa2}에 대입하면\n" \
              "{eq2}     ∴ y = $$수식$${y}$$/수식$$\n" \
              "y = $$수식$${y}$$/수식$${temp2} {aa1}에 대입하면 x = $$수식$${x}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp2} 각 식의 좌변에 대입하면\n" \
              "{list}"

    x = np.random.randint(1, 15)*-1
    y = np.random.randint(1, 15)*-1
    a = y-x
    while a==0:
        x = np.random.randint(1, 15) * -1
        y = np.random.randint(1, 15) * -1
        a = y - x
    temp = proc_jo(a, 4)
    temp2 = proc_jo(y, 4)
    aa1 ="x = y - " + str(abs(a))
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)
    d = x*b-c*y
    aa2 = str(b) +"x - "
    eq2 = str(b) +"(y - " + str(abs(a))+") - "
    if b==1:
        aa2 = "x - "
        eq2 ="(y - " + str(abs(a)) + ") - "
    if c==1:
        aa2 = aa2 + "y = " + str(d)
        eq2 = eq2 + "y = " + str(d)
    else:
        aa2 = aa2 +str(c) +"y = " + str(d)
        eq2 = eq2 + str(c) + "y = " + str(d)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    bb=[]
    cc=[]
    while len(bb)<2:
        oo = np.random.randint(0, 2)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 10)
        d = np.random.randint(1, 10)
        if d != b*x+c*y and oo==1:
            t = str(b) +"x + "
            if b==1:
                t = "x + "
            if c==1:
                t = t + "y = " + str(d)
            else:
                t = t + str(c) +"y = " + str(d)
            v = str(b*x) + " - " + str(abs(c*y)) + " = " + str(b*x+c*y) + " ≠ "+str(d)
            bb.append(t)
            cc.append(v)
        if d != b * x - c * y and oo==0:
            t = str(b) + "x - "
            if b == 1:
                t = "x - "
            if c == 1:
                t = t + "y = " + str(d)
            else:
                t = t + str(c) + "y = " + str(d)
            bb.append(t)
            v = str(b * x) + " + " + str(abs(c * y)) + " = " + str(b * x - c * y) + " ≠ " + str(d)
            cc.append(v)

    while len(bb) < 5:
        oo = np.random.randint(0, 2)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 10)
        if oo==1:
            d = b*x+c*y
            t = str(b) + "x + "
            if b == 1:
                t = "x + "
            if c == 1:
                t = t + "y = " + str(d)
            else:
                t = t + str(c) + "y = " + str(d)
            bb.append(t)
        else:
            d = b * x - c * y
            t = str(b) + "x - "
            if b == 1:
                t = "x - "
            if c == 1:
                t = t + "y = " + str(d)
            else:
                t = t + str(c) + "y = " + str(d)
            bb.append(t)


    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①, ②"
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
        x5 = bb[4]
        list = "① " +cc[0] +"\n② " +cc[1] +"\n"

    elif rande == 2:
        ans = "②, ⑤"
        x2 = bb[0]
        x1 = bb[4]
        x3 = bb[3]
        x4 = bb[2]
        x5 = bb[1]
        list = "② " + cc[0] + "\n⑤ " + cc[1] +"\n"
    elif rande == 3:
        ans = "④, ⑤"
        x3 = bb[2]
        x1 = bb[4]
        x2 = bb[3]
        x4 = bb[0]
        x5 = bb[1]
        list = "④ " + cc[0] + "\n⑤ " + cc[1] + "\n"
    elif rande == 4:
        ans = "③, ④"
        x4 = bb[1]
        x1 = bb[3]
        x2 = bb[4]
        x3 = bb[0]
        x5 = bb[2]
        list = "③ " + cc[0] + "\n④ " + cc[1] + "\n"
    else:
        ans = "①, ④"
        x5 = bb[4]
        x1 = bb[0]
        x2 = bb[3]
        x3 = bb[2]
        x4 = bb[1]
        list = "① " + cc[0] + "\n④ " + cc[1] + "\n"

    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp=temp, list=list, x=x, y=y, eq2=eq2, temp2=temp2, aa1=aa1, aa2=aa2)

    return stem, answer, comment

#중2-1-2-129
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_105():
    stem = "\n다음을 만족시키는 x, y에 대하여 $$수식$${eq}$$/수식$$  의\n" \
           "값은? (단, k ≠ 0) $$표$$\n" \
           "{aa1}, {aa2}\n" \
           "$$/표$$"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${aa}$$/수식$$\n\n" \
              "㉠$$수식$$TIMES$$/수식$$ $$수식$${mul}$$/수식$$+㉡을 하면 {k_eq}     ∴ {k_x}\n" \
              "{k_x}를 ㉠에 대입하면\n" \
              "{k_eq2}    ∴ {k_y}\n" \
              "{k_x}, {k_y}를 $$수식$${eq}$$/수식$$     에 대입하면\n" \
              "{fra} = $$수식$${answ}$$/수식$$"

    x =np.random.randint(1, 6)
    y = np.random.randint(1, 6)
    k = lcm(x,y)
    xx = int(k/x)
    yy = int(k/y)
    k_x = "x = " + str(xx)+"k"
    k_y = "y = " + str(yy)+"k"
    if xx==1:
        k_x = "x = k"
    if yy==1:
        k_y = "y = k"
    a = np.random.randint(2, 6)
    b = mul= np.random.randint(2, 6)
    aa1 = str(a) +"x - y = " + str(a*xx-yy) +"k"
    aa2 = "x + " + str(b) +"y = " + str(xx+b*yy)+"k"
    k_eq = str(a*mul+1)+"x = " + str((a*xx-yy)*mul+(xx+b*yy))
    k_eq2 = str(xx*a) +"x - y = " + str(a*xx-yy) +"k"
    aa = "{cases{" + aa1 + "`cdots`cdots`"+problm1()+"#" + aa2 + "`cdots`cdots`"+problm2()+"}}"
    f = np.random.randint(1, 6)
    g =np.random.randint(1, 6)
    s = np.random.randint(1, 6)
    l = np.random.randint(1, 6)
    while (f*xx-g*yy)==0 or  (f*xx-g*yy)%(s*xx+l*yy)!=0:
        f = np.random.randint(1, 6)
        g = np.random.randint(1, 6)
        s = np.random.randint(1, 6)
        l = np.random.randint(1, 6)

    eq = "$$수식$${"+str(f)+"x - "
    if f==1:
        eq = "$$수식$${x - "
    if g!=1:
        eq = eq + str(g)+"y} over "
    else:
        eq = eq + "y} over "
    if s!=1:
        eq = eq + "{"+str(s)+"x - "
    else:
        eq = eq + "{x - "
    if l!=1:
        eq =eq + str(l)+"y}$$/수식$$ $$수식$$$$/수식$$"
    else:
        eq =eq + "y}$$/수식$$ $$수식$$$$/수식$$"
    top =str(f*xx)+"k - "
    if f*xx==1:
        top = "k - "
    if g*yy!=1:
        top = top + str(g*yy) +"k"
    else:
        top = top + "k"

    bottom = str(s*xx) +"k + "
    if s*xx== 1:
        bottom = "k + "
    if l*yy != 1:
        bottom = bottom  + str(l*yy)+"k"
    else:
        bottom = bottom + "k"

    fra = "$$수식$${"+top+"} over {"+bottom+"}$$/수식$$ $$수식$$  $$/수식$$  "
    fra= fra + " = $$수식$${"+str(f*xx-g*yy)+"k} over {"+str(s*xx+l*yy)+"k}$$/수식$$"
    answ = int((f*xx-g*yy)/(s*xx+l*yy))

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    stem = stem.format(aa1=aa1, aa2=aa2, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, k_eq2=k_eq2, aa1=aa1, aa2=aa2, aa=aa, fra=fra, k_eq=k_eq, k_x=k_x, k_y=k_y, mul=mul, answ=answ)

    return stem, answer, comment

#중2-1-2-130
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_106():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$    $$수식$$``$$/수식$$              {temp} 풀면?\n\n" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "주어진 연립방정식을 정리하면\n" \
              "$$수식$${vv}$$/수식$$\n\n" \
              "㉠+㉡$$수식$$TIMES$$/수식$$$$수식$${mul}$$/수식$${temp2} 하면 {eq2}     ∴ x = $$수식$${x}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$${temp3} ㉠에 대입하면 {eq3}   ∴ y = $$수식$${y}$$/수식$$"


    x = np.random.randint(0, 10)
    temp3 = proc_jo(x, 4)
    f = np.random.randint(2, 5)
    mul = np.random.randint(2, 5)
    y = np.random.randint(0, 10)
    a = f*mul
    b = np.random.randint(1, 10)
    c = x +a*(y-b)
    aa1 ="x + " + str(a) +"(y - " + str(b) +") = " + str(c)
    vv1 = "x + " + str(a) +"y = " + str(c+b*a)
    d = np.random.randint(2, 10)
    e = np.random.randint(1, 10)

    temp2 = proc_jo(mul, 4)

    g = d*(x+e)-(f*y)
    aa2 = str(d)+"(x + " + str(e)+") - " + str(f) +"y = " + str(g)
    vv2 = str(d)+"x - " + str(f) +"y = " + str(g-d*e)
    if f==1:
        aa2 = str(d) + "(x + " + str(e) + ") - y = " + str(g)
    temp = proc_jo(g, 4)
    eq2 = str(1+mul*d) +"x = " + str((c+b*a)+ mul*(g-d*e))
    eq3 = str(a) +"y = " + str((c+b*a)-x)
    answ = "x = " + str(x) +", y = " + str(y)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + vv1 + "`cdots`cdots`"+problm1()+"#" + vv2 + "`cdots`cdots`"+problm2()+"}}"
    bb=[]
    dd=[]
    while len(bb)<4:
        aa = np.random.randint(1, 15)
        ff = np.random.randint(1, 15)
        pp = np.random.randint(0, 2)
        if pp==1:
            aa =aa*-1
        if aa!=x and ff!=y and [aa,ff] not in dd:
            dd.append([aa,ff])
            bb.append("x = " + str(aa) +", y = " + str(ff))

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    stem = stem.format(temp=temp, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp3=temp3, eq2=eq2, temp2=temp2, vv=vv, mul=mul, x=x, y=y, eq3=eq3)

    return stem, answer, comment

#중2-1-2-131
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_107():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$    $$수식$$``$$/수식$$                을 만\n\n" \
           "족시키는 x, y에 대하여 y - x의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "㉠$$수식$$TIMES$$/수식$$ 10을 하면 {eq2} $$수식$$cdots cdots``$$/수식$$㉢\n" \
              "㉡$$수식$$TIMES$$/수식$$ 100을 하면 {eq3} $$수식$$cdots cdots``$$/수식$$㉣\n" \
              "㉢-㉣을 하면 {eq4}    ∴ y = $$수식$${y}$$/수식$$\n" \
              "y = $$수식$${y}$$/수식$${temp} ㉢에 대입하면 {eq5}     ∴ x = $$수식$${x}$$/수식$$\n" \
              "∴ y - x = $$수식$${y}$$/수식$$ - $$수식$${x}$$/수식$$ = $$수식$${answ}$$/수식$$"

    x= np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    temp = proc_jo(y,4)
    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = a*x + b*y
    d = np.random.randint(2, 10)
    e = a*x + d*y

    aa1 = str(a/10) + "x + " + str(b/10) + "y = " + str(c/10)
    aa2 = str(a/100) +"x + " + str(d/100) +"y = " + str(e/100)
    eq3 = str(a) +"x + " +str(d)+"y = " + str(e)
    eq2 = str(a) +"x + "
    if a==1:
        eq2 ="x + "
        eq3 ="x + " +str(d)+"y = " + str(e)
    if b==1:
        eq2 = eq2 + "y = " + str(c)
    else:
        eq2 = eq2 +str(b) +"y = " + str(c)

    eq4 = str(b-d) + "y = " + str(c-e)
    if b-d==1:
        eq4 ="y = " + str(c-e)
    elif b-d==-1:
        eq4 = "-y = " + str(c - e)
    eq5 =  str(a) + "x + " + str(b*y) + " = " + str(c)
    if a==1:
        eq5 = "x + " + str(b*y) + " = " + str(c)
    eq = problm(aa1, aa2)
    answ = y-x
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq5=eq5, eq4=eq4, eq2=eq2, temp=temp, eq3=eq3, x=x, y=y, answ=answ)

    return stem, answer, comment

#중2-1-2-132
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_108():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$의 해가\n\n" \
           "x = a, y = b일 때, a + b의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "㉠$$수식$$TIMES$$/수식$$$$수식$${mul}$$/수식$${temp} 하면 {eq2}\n" \
              "∴ {eq3}    $$수식$$cdots`cdots$$/수식$$  ㉢\n" \
              "㉡$$수식$$TIMES$$/수식$$$$수식$${mul2}$$/수식$${temp2} 하면 {eq33} $$수식$$cdots`cdots$$/수식$$  ㉣\n" \
              "㉢$$수식$$TIMES$$/수식$$$$수식$${mul3}$$/수식$$-㉣을 하면 {eq4}    ∴ x = $$수식$${x}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$${temp3} ㉢에 대입하면 {eq5}   ∴ y = $$수식$${y}$$/수식$$\n" \
              "따라서 a = $$수식$${x}$$/수식$$, b = $$수식$${y}$$/수식$$이므로 a + b = $$수식$${answ}$$/수식$$"

    x =  np.random.randint(1, 10)
    y =  np.random.randint(1, 10)
    a = np.random.randint(1, 10)
    b = mul = np.random.randint(2, 10)


    while y-a==0 or (y-a)%b!=0:
        a = np.random.randint(1, 10)
        b = np.random.randint(2, 10)
    mul = b
    temp = proc_jo(mul,4)
    c = x - int((y-a)/b)
    aa1 = "x - {y-"+str(a) +"} over {"+str(b)+"} = " + str(c)
    eq2 = str(b) +"x -(y - " + str(a) +") = " + str(c*b)
    eq3 = str(b) +"x - y = " + str(c*b-a)

    d =np.random.randint(1, 10)
    e = np.random.randint(2, 10)
    f = np.random.randint(2, 10)
    d= int(d/gcd(d,e))
    e = int(e/gcd(d,e))
    while e==1:
        d = np.random.randint(1, 10)
        e = np.random.randint(2, 10)
        f = np.random.randint(2, 10)
        d = int(d / gcd(d, e))
        e = int(e / gcd(d, e))
    lcm1 = lcm(e,f)
    aa = (int(lcm1/e)*x*d)-(int(lcm1/f)*y)
    gcd1 = gcd(lcm1, abs(aa))
    lcm1 = int(lcm1/gcd1)
    aa = int(aa/gcd1)
    aa2 = "{"+str(d)+"} over {"+str(e)+"}x - y over {"+str(f)+"} = {" +str(aa) +"} over {"+str(lcm1)+"}"
    if lcm1==1:
        aa2 = "{" + str(d) + "} over {" + str(e) + "}x - y over {" + str(f) + "} = " + str(aa)

    mul2 = lcm(lcm(e,f),lcm1)
    temp2 = proc_jo(mul2, 4)
    d = d*int(mul2/e)
    yy = int(mul2/f)
    aa = int(mul2/lcm1)*aa
    eq33 = str(d) +"x - "
    if d==1:
        eq33 = "x - "
    if yy==1:
        eq33 = eq33 + "y = " + str(aa)
    else:
        eq33 = eq33 + str(yy)+"y = " + str(aa)
    mul3 = yy
    temp3 = proc_jo(yy, 4)
    eq4 = str(b*mul3- d)+"x = " + str((c*b-a)*mul3-aa)
    eq5 = str(b*x)+" - y = " + str(c*b-a)
    answ = x+y

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    eq = problm(aa1, aa2)
    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq33=eq33, eq5=eq5, eq4=eq4, eq2=eq2, temp3=temp3, temp2=temp2, temp=temp, eq3=eq3, x=x, y=y, mul=mul, mul2=mul2, mul3=mul3, answ=answ)

    return stem, answer, comment

#중2-1-2-133
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_109():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$                                 의 해가\n\n" \
           "x = m, y = n일 때, m - n의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "㉠에서 {eq1}\n" \
              "∴ {eq2} $$수식$$cdots`cdots`$$/수식$$ ㉢\n" \
              "㉢-㉡을 하면 y = $$수식$${y}$$/수식$$\n" \
              "y = $$수식$${y}$$/수식$${temp} ㉡에 대입하면 {eq3}\n" \
              "{eq4}    ∴ x = $$수식$${x}$$/수식$$\n" \
              "따라서 m = $$수식$${x}$$/수식$$, n = $$수식$${y}$$/수식$$이므로\n" \
              "m - n = $$수식$${x}$$/수식$$ - ($$수식$${y}$$/수식$$) = $$수식$${answ}$$/수식$$"

    x = np.random.randint(0, 10)
    y = np.random.randint(0, 10)*-1
    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)*-1
    c = np.random.randint(1, 10)
    d = int((b-c*y)/(x+a))
    e = d*x+y
    while d==0 or (x+a)==(b-c*y) or (b-c*y)%(x+a)!=0:
        x = np.random.randint(0, 10)
        y = np.random.randint(0, 10) * -1
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10) * -1
        c = np.random.randint(1, 10)
        d = int((b-c*y)/(x+a))
        e = d * x + y
    div = int((b-c*y)/(x+a))
    gcd1 =gcd(x+a, abs(b-c*y))
    aaa = int((x+a)/gcd1)
    bbb = int((b-c*y)/gcd1)
    aa1 ="(x + "+str(a)+") : (" +str(b) + "  - " + str(c) +"y) = " + str(aaa) + " : " + str(bbb)
    if c==1:
        aa1 = "(x + " + str(a) + ") : (" + str(b) + " - y) = " + str(aaa) + " : " + str(bbb)

    aa2 = str(d) +"x + y = " + str(e)
    if d==1:
        aa2 = "x + y = "+str(e)
    eq1 = str(b) + "  - " + str(c) +"y = "
    eq2 = str(div)+"x + " +str(c)+"y = " + str(b-div*a)
    if c==1:
        eq1 = str(b) + " - y = "
        eq2 = str(div) + "x + y = " + str(b - div * a)
    eq1 = eq1 + str(div) +"(x + " + str(a)+")"
    eq3 = str(d) +"x - " + str(abs(y))+" = " + str(e)
    eq4 = str(d)+"x = " + str(e-y)
    answ = x-y

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    eq = problm(aa1, aa2)
    temp = proc_jo(y, 4)
    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp=temp, answ=answ, x=x,y=y, eq1=eq1, eq2=eq2, eq3=eq3, eq4=eq4)

    return stem, answer, comment

#중2-1-2-134
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_110():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$                                 의 해가 (a,b)\n\n" \
           "일 때, a - 2b의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "방정식의 양변에 각각 10, $$수식$${mul}$$/수식$${temp} 곱하면\n" \
              "$$수식$${aaa}$$/수식$$\n\n" \
              "즉, $$수식$${vv}$$/수식$$\n\n" \
              "㉠+㉡을 하면 {eq2}      ∴ x = $$수식$${x}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$${temp2} ㉠에 대입하면 {eq3}    ∴ y = $$수식$${y}$$/수식$$\n" \
              "따라서 a = $$수식$${x}$$/수식$$, b = $$수식$${y}$$/수식$$이므로 a - 2b = $$수식$${answ}$$/수식$$"

    x = np.random.randint(1, 10)
    temp2 = proc_jo(x, 4)
    y = np.random.randint(1, 10)
    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = a*x+b*y
    d = np.random.randint(1, 10)
    e = np.random.randint(2, 10)
    f = np.random.randint(2, 10)
    g = np.random.randint(1, 10)
    h =  np.random.randint(2, 10)
    lcm1 = lcm(f, h)
    lcm22 = lcm(lcm(f,h), lcm1)
    cap = int(lcm22/f)
    capp = int(lcm22/h)
    while capp-b!=0:
        x = np.random.randint(1, 10)
        temp2 = proc_jo(x, 4)
        y = np.random.randint(1, 10)
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = a * x + b * y
        d = np.random.randint(1, 10)
        e = np.random.randint(2, 10)
        f = np.random.randint(2, 10)
        g = np.random.randint(1, 10)
        h = np.random.randint(2, 10)
        lcm1 = lcm(f, h)
        lcm22 = lcm(lcm(f, h), lcm1)
        cap = int(lcm22 / f)
        capp = int(lcm22 / h)

    aa1 = str(a/10) +"x + " + str(b/10) + "y = " +str(c/10)
    aaa1 = str(a) +"x + "
    if a==1:
        aaa1 = "x + "
    if b==1:
        aaa1 = aaa1 + "y = " + str(c)
    else:
        aaa1 = aaa1 +str(b) +"y = " + str(c)

    aa = int(lcm1 / f) * ((x*e )+d) - int(lcm1 /h) * (y+g)
    gcd1 = gcd(lcm1, abs(aa))
    lcm1 = int(lcm1 / gcd1)
    aa = int(aa / gcd1)
    aa2 = "{" + str(d) + " + " +str(e)+"x} over {" + str(f) + "} - {"+str(g) +" + y} over {" + str(h) + "} = {" + str(aa) + "} over {" + str(lcm1) + "}"
    if lcm1 == 1:
        aa2 = "{" + str(d) + " + " + str(e) + "x} over {" + str(f) + "} - {" + str(g) +" + y} over {" + str(h) + "} = " + str(aa)
    mul=lcm22
    temp = proc_jo(lcm22, 4)
    f = int(lcm22/f)
    h = int(lcm22/h)
    lcm1 = int(lcm22/lcm1)
    aaa2 = str(f) +"(" + str(d) +" + " + str(e) +"x) - "
    if f==1:
        aaa2 = "(" + str(d) +" + " + str(e) +"x) - "
    if h==1:
        aaa2 = aaa2 + "("+str(g) +" + y) = " + str(int(aa*lcm1))
    else:
        aaa2 = aaa2 + str(h) +"("+str(g) +" + y) = " + str(int(aa*lcm1))
    simplifed = (int(aa*lcm1)) + h*g -d*f
    vv2 = str(e*f) +"x - " + str(h) + "y = " + str(simplifed)
    if h==1:
        vv2 = str(e * f) + "x - y = " + str(simplifed)
    eq2 = str(e*f+a)+"x = " + str(simplifed + c)
    eq3 = str(a*x) + " + " + str(b) +"y = "+ str(c)
    if b==1:
        eq3 = str(a*x) + " + y = "+ str(c)
    answ = x-2*y

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    aaa = "{cases{" + aaa1 + "#" + aaa2 + "}}"
    vv = problm(aaa1, vv2)


    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp=temp,temp2=temp2, answ=answ, vv=vv, aaa=aaa, x=x,y=y, eq2=eq2, eq3=eq3, mul=mul)

    return stem, answer, comment

#중2-1-2-135
#㉠㉡을 연립방정식에 넣으면 에러, 조금 오래 걸림, 중괄호를 연립방정식에 넣는 법을 모르겠음
def expressions212_Stem_111():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$                           {temp}\n\n" \
           "만족시키는 x, y에 대하여 x + y의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${aa1}$$/수식$$                를 정리하면\n" \
              "$$수식$${aa11}$$/수식$$      ∴ $$수식$${eq2}$$/수식$$\n" \
              "$$수식$${aa2}$$/수식$$                     {temp} 정리하면\n" \
              "$$수식$${aa22}$$/수식$$      ∴ $$수식$${eq3}$$/수식$$\n" \
              "따라서 주어진 연립방정식은\n" \
              "$$수식$${vv}$$/수식$$\n\n" \
              "㉠-㉡을 하면 {xx}   ∴ x = $$수식$${x}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$${temp3} ㉡에 대입하면 {yy}   ∴ y = $$수식$${y}$$/수식$$\n" \
              "∴ x + y = $$수식$${answ}$$/수식$$"

    x = np.random.randint(1, 8)
    temp3 = proc_jo(x, 4)
    y = np.random.randint(1, 8)
    a = np.random.randint(2, 8)
    b = np.random.randint(1, 8)
    c = np.random.randint(2, 8)
    d = np.random.randint(1, 8)
    e = np.random.randint(1, 8)
    while a*(x-b*y)!=c*(d-e*y) or b*a-c*e!=1:
        x = np.random.randint(1, 8)
        temp3 = proc_jo(x, 4)
        y = np.random.randint(1, 8)
        a = np.random.randint(2, 8)
        b = np.random.randint(1, 8)
        c = np.random.randint(2, 8)
        d = np.random.randint(1, 8)
        e = np.random.randint(1, 8)

    aa1 = str(a) +"(x - " + str(b) + "y) = "
    if b==1:
        aa1 = str(a) +"(x - y) = "
    if e==1:
        aa1 = aa1 + str(c) +"(" + str(d) + " - y)"
    else:
        aa1 = aa1 + str(c) +"(" + str(d) + " - " + str(e) +"y)"
    aa11 = str(a) + "x - " + str(b*a) +"y = " + str(c*d) + " - " + str(c*e) +"y"
    eq2 = str(a) + "x - y = " + str(c*d)
    aaa = np.random.randint(1, 8)
    bbb = np.random.randint(1, 8)
    ccc = np.random.randint(1, 8)
    ddd = np.random.randint(1, 8)
    eee = np.random.randint(1, 8)
    while aaa-(bbb*x-(ccc*x-y)+ddd)!=eee:
        aaa = np.random.randint(1, 8)
        bbb = np.random.randint(1, 8)
        ccc = np.random.randint(1, 8)
        ddd = np.random.randint(1, 8)
        eee = np.random.randint(1, 8)

    aa2 = str(aaa) +" - (" + str(bbb) +"x - "
    if bbb==1:
        aa2 = str(aaa) + " - (x - "
    if ccc!=1:
        aa2 = aa2 + "(" + str(ccc) +"x - y) + " + str(ddd)  +") = " + str(eee)
    else:
        aa2 = aa2 + "(x - y) + " + str(ddd)  +") = " + str(eee)
    temp = proc_jo(eee, 4)
    aa22 = str(aaa) +" - (" + str(bbb-ccc) +"x + y + " + str(ddd)  +") = " +  str(eee)
    eq3 = str((bbb-ccc)*-1) +"x - y = " +  str(eee-aaa+ddd)
    if bbb-ccc==1:
        aa22 = str(aaa) + " - (x + y + " + str(ddd) + ") = " + str(eee)
        eq3 = "-x - y = " + str(eee - aaa + ddd)
    if bbb-ccc==-1:
        aa22 = str(aaa) + " - (-x + y + " + str(ddd) + ") = " + str(eee)
        eq3 = "x - y = " + str(eee - aaa + ddd)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"

    vv = problm(eq2, eq3)
    xx = str(a-((bbb-ccc)*-1)) +"x = " + str((c*d)-(eee-aaa+ddd))
    if (a-((bbb-ccc)*-1))==1:
        xx = "x = " + str((c*d)-(eee-aaa+ddd))
    if (a-((bbb-ccc)*-1))==-1:
        xx = "-x = " + str((c * d) - (eee - aaa + ddd))

    yy = str(((bbb-ccc)*-1)*x)+" - y = " + str(eee - aaa + ddd)
    answ = x +y

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(aa1=aa1,aa11=aa11, aa22=aa22, aa2=aa2, temp=temp, temp3=temp3, answ=answ, vv=vv, xx=xx, x=x, y=y, yy=yy, eq2=eq2, eq3=eq3)

    return stem, answer, comment


#중2-1-2-136
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_112():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$  을 만족시키는\n\n" \
           "x, y에 대하여 y - x의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "방정식의 양변에 각각 10, $$수식$${mul}$$/수식$${temp} 곱하여 정리하면\n" \
              "$$수식$${vv}$$/수식$$\n\n" \
              "㉠$$수식$$TIMES$$/수식$$$$수식$${mul2}$$/수식$$-㉡$$수식$$TIMES$$/수식$$$$수식$${mul3}$$/수식$${temp2} 하면 {eq2}   ∴ y = $$수식$${y}$$/수식$$\n" \
              "y = $$수식$${y}$$/수식$${ytemp} ㉠에 대입하면 {eq3}    ∴ x = $$수식$${x}$$/수식$$\n" \
              "∴ y - x = $$수식$${answ}$$/수식$$"

    x = np.random.randint(0, 15)
    y = np.random.randint(0, 15)
    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = a*x+b*y
    d = np.random.randint(2, 6)
    e = np.random.randint(2, 6)
    f = np.random.randint(2, 6)
    while a*x+b*y!=c or (1/d)*x-(1/e)*y!=(-1/f):
        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15)
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = a*x+b*y
        d = np.random.randint(2, 6)
        e = np.random.randint(2, 6)
        f = np.random.randint(2, 6)
    ytemp = proc_jo(y, 4)
    aa1 = str(a/10) +"x + " + str(b/10) +"y - " + str(c/10) +" = " + str(0)
    vv1 = str(a) +"x + "
    eq3 = str(a) +"x + " + str(b*y) + " = " + str(c)
    if a==1:
        vv1 = "x + "
        eq3 = "x + " + str(b*y) + " = " + str(c)
    if b==1:
        vv1 = vv1 + "y = " + str(c)
    else:
        vv1 = vv1 + str(b) +"y = " + str(c)
    aa2 = "1 over {" + str(d) +"}x - 1 over {" + str(e) +"}y + 1 over {" + str(f)+"} = 0"
    mul = lcm(lcm(d,e),f)
    d = int(mul/d)
    e = int(mul/e)
    f = int(mul/f)*-1
    vv2 = str(d) +"x - "
    if d==1:
        vv2 = "x - "
    if e==1:
        vv2 = vv2 + "y = " + str(f)
    else:
        vv2 = vv2 + str(e) +"y = " + str(f)
    lcm2 = lcm(a,d)
    mul2 = int(lcm2/a)
    mul3 = int(lcm2/d)
    temp = proc_jo(mul,4)
    temp2 = proc_jo(mul3, 4)
    eq2 = str(b*mul2+e*mul3) +"y = " + str(c*mul2-f*mul3)
    if (b*mul2+e*mul3)==1:
        eq2 = "y = " + str(c*mul2-f*mul3)
    elif (b*mul2+e*mul3)==-1:
        eq2 = "-y = " + str(c * mul2 - f * mul3)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"

    vv = problm(vv1, vv2)
    answ = y-x


    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp2=temp2, temp=temp, mul=mul, mul2=mul2, mul3=mul3, ytemp=ytemp,answ=answ, vv=vv, x=x, y=y,
                            eq2=eq2, eq3=eq3)

    return stem, answer, comment


#중2-1-2-137
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_113():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$  의 해를\n\n" \
           "(a,b)라고 할 때, a + b의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "방정식의 양변에 각각 10, $$수식$${mul}$$/수식$${temp} 곱하여 정리하면\n" \
              "$$수식$${aaa}$$/수식$$    ,\n\n" \
              "즉, $$수식$${vv}$$/수식$$\n\n" \
              "㉠$$수식$$TIMES$$/수식$$$$수식$${mul2}$$/수식$$-㉡$$수식$$TIMES$$/수식$$$$수식$${mul3}$$/수식$${temp2} 하면 {eq2}   \n" \
              "∴ y = $$수식$${y}$$/수식$$\n" \
              "y = $$수식$${y}$$/수식$${ytemp} ㉠에 대입하면 {eq3}    \n" \
              "∴ x = $$수식$${x}$$/수식$$\n" \
              "따라서 a = $$수식$${x}$$/수식$$, b = $$수식$${y}$$/수식$$이므로\n" \
              "∴ a + b = $$수식$${answ}$$/수식$$"

    x = np.random.randint(0, 15)
    y = np.random.randint(0, 15)
    a = np.random.randint(2, 10)
    b = np.random.randint(1, 10)
    c = a*(x+y)-b*y
    d = np.random.randint(2, 6)
    d1 = np.random.randint(1, 5)
    e = np.random.randint(2, 6)
    e1 = np.random.randint(1, 5)
    f = np.random.randint(1, 10)
    while a==b  or d<=d1 or e<=e1 or (d1 / d) * x + (e1/ e) * y != f:
        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15)
        a = np.random.randint(2, 10)
        b = np.random.randint(1, 10)
        c = a*(x+y)-b*y
        d = np.random.randint(2, 20)
        d1 = np.random.randint(1, 20)
        e = np.random.randint(2, 20)
        e1 = np.random.randint(1, 20)
        f = np.random.randint(1, 10)
    gcdd = gcd(d,d1)
    d1 = int(d1/gcdd)
    d = int(d/gcdd)
    gcde = gcd(e,e1)
    e1 = int(e1 / gcde)
    e = int(e / gcde)
    aa1 = str(a/10) +"(x + y) - " + str(b/10) +"y = " + str(c/10)
    if (c/10)%1==0:
        aa1 = str(a / 10) + "(x + y) - " + str(b / 10) + "y = " + str(int(c / 10))

    aaa1 = str(a) +"(x + y) - "+ str(b) +"y  = " +  str(c)
    if b==1:
        aaa1 = str(a) + "(x + y) - y  = " + str(c)
    vv1 = str(a) +"x "
    if a-b>0:
        if a-b==1:
            vv1 = vv1 + "+ y = " + str(c)
        else:
            vv1 = vv1 + "+ " + str(a-b) +"y = " + str(c)
    elif a-b<0:
        if a-b==-1:
            vv1 = vv1 + "- y = " + str(c)
        else:
            vv1 = vv1 + "- " + str(b-a) +"y = " + str(c)

    aa2 = "{"+str(d1)+"} over {" + str(d) +"}x + {"+str(e1)+"} over {" + str(e) +"}y = " + str(f)
    mul = lcm(d,e)
    temp = proc_jo(mul,4)
    d1 = d1*int(mul/d)
    e1 = e1*int(mul/e)
    f= f*mul
    aaa2 = str(d1) +"x + "
    eq3 = str(d1)+"x + " + str(e1*y) +" = " + str(f)
    if d1==1:
        aaa2 = "x + "
        eq3 = "x + " + str(e1 * y) + " = " + str(f)
    if e1==1:
        aaa2 = aaa2 +"y = " + str(f)
    else:
        aaa2 = aaa2 + str(e1) +"y = " + str(f)
    lcm1 = lcm(a, d1)
    mul2 = int(lcm1/a)
    mul3 = int(lcm1/d1)
    ytemp = proc_jo(y, 4)
    temp2 = proc_jo(mul3, 4)
    eq2 = str((a-b)*mul2-e1*mul3) +"y = " + str(c*mul2-f*mul3)
    if (((a-b)*mul2)-e1*mul3)==1:
        eq2 = "y = " + str(c*mul2-f*mul3)
    elif (((a-b)*mul2)-e1*mul3)==-1:
        eq2 = "-y = " + str(c * mul2 - f * mul3)

    answ = x+y

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    aaa = "{cases{" + aaa1 + "#" + aaa2 + "}}"
    vv = problm(vv1,aaa2)
    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp2=temp2, temp=temp, mul=mul, mul2=mul2, mul3=mul3, ytemp=ytemp, answ=answ, vv=vv, x=x,aaa=aaa, y=y,eq2=eq2, eq3=eq3)

    return stem, answer, comment

#중2-1-2-138
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_114():
    stem = "\n다음 연립방정식의 해를 (p,q)라 할 때, p + q\n" \
           "의 값은? $$표$$\n" \
           "$$수식$${eq}$$/수식$$\n\n" \
           "$$/표$$" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "㉠에서 $$수식$${fra}$$/수식$$\n" \
              "양변에 10을 곱하면 {eq1} $$수식$$cdots cdots$$/수식$$ ㉢\n" \
              "㉡$$수식$$TIMES$$/수식$$10을 하면 {eq2}\n" \
              "이 식을 정리하면 {eq3} $$수식$$cdots cdots$$/수식$$ ㉣\n" \
              "㉢+㉣을 하면 {xx}\n" \
              "x = $$수식$${x}$$/수식$${temp} ㉢에 대입하면 {yy}\n" \
              "∴ y = $$수식$${y}$$/수식$$\n" \
              "따라서 p = $$수식$${x}$$/수식$$, q = $$수식$${y}$$/수식$$이므로\n" \
              "p + q = $$수식$${answ}$$/수식$$"
    xw = np.random.randint(0, 2)
    yw = np.random.randint(0, 2)
    x = np.random.randint(0, 15)
    y = np.random.randint(0, 15)
    if xw==1:
        x = x*-1
    if yw ==1:
        y = y*-1
    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = a*x-b*y
    d = np.random.randint(2, 9)
    e = d+1
    f = d*(x-y)+e*(y-x)
    while (a+(d-e))==0 or c==0 or f==0 or -b!=(d-e):
        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15)
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = a * x - b * y
        d = np.random.randint(2, 10)
        e = np.random.randint(1, 10)
        f = d * (x - y) + e * (y - x)
    temp = proc_jo(x, 4)
    fra = "{" + str(a) +"} over 10x - {" + str(b)+"} over 10 = {" + str(c)+"} over 10"
    if c<1:
        fra = "{" + str(a) +"} over 10x - {" + str(b)+"} over 10 = - {" + str(abs(c))+"} over 10"
    aa1 = str(a/10) +"x - " + str(b/10) +"y = " + str(c/10)
    eq1 = str(a) +"x - "
    yy = str(a*x)  + " - " + str(b) +"y = " + str(c)
    if a==1:
        eq1 ="x - "
    if b==1:
        eq1= eq1 +"y = " + str(c)
        yy = str(a*x)  + " - y = " + str(c)
    else:
        eq1 = eq1 + str(b) +"y = "+ str(c)
    aa2 = str(d/10) +"(x - y) + " + str(e/10) +"(y - x) = " + str(f/10)
    eq2 =  str(d) +"(x - y) + " + str(e) +"(y - x) = " + str(f)
    eq3 = str(d-e)+"x + " + str(e-d) + "y = " +str(f)
    xx = str(a+(d-e))+"x = " + str(c+f)
    if (a+(d-e))==1:
        xx = "x = " + str(c+f)
    elif (a+(d-e))==-1:
        xx = "-x = " + str(c + f)
    if e-d==1:
        eq3 = "-x + y = " +str(f)
    answ = x+y
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    eq = problm(aa1,aa2)


    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(xx=xx, yy=yy, eq1=eq1, temp=temp, answ=answ,  x=x,fra=fra, y=y, eq2=eq2, eq3=eq3)

    return stem, answer, comment


#중2-1-2-139
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_115():
    stem = "\n다음 연립방정식 $$수식$${eq}$$/수식$$              $$수식$$``$$/수식$$           의 해를\n\n" \
           "(a,b)라 할 때, a - b의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "주어진 연립방정식에서\n" \
              "$$수식$${aaa}$$/수식$$\n\n" \
              "즉, $$수식$${vv}$$/수식$$\n\n" \
              "㉠$$수식$$TIMES$$/수식$$$$수식$${mul}$$/수식$$-㉡을 하면 {eq2}   \n" \
              "∴ y = $$수식$${y}$$/수식$$\n" \
              "y = $$수식$${y}$$/수식$${ytemp} ㉠에 대입하면 {eq3}    \n" \
              "∴ x = $$수식$${x}$$/수식$$\n" \
              "따라서 a = $$수식$${x}$$/수식$$, b = $$수식$${y}$$/수식$$이므로\n" \
              "∴ a - b = {eq4} = $$수식$${answ}$$/수식$$"


    x = np.random.randint(4, 13)
    y = np.random.randint(4, 13)
    a = np.random.randint(2, 8)
    b = np.random.randint(1, 8)
    c = np.random.randint(1, 8)
    d = np.random.randint(2, 5)
    e = np.random.randint(1, 8)
    f = np.random.randint(2, 8)
    g = np.random.randint(1, 8)
    j = np.random.randint(1, 8)
    h = e * x - f * (y - x) - j * x
    mul = np.random.randint(2, 5)
    while a==d or a*(x+b)!=(y-c)*d:
        x = np.random.randint(4, 13)
        y = np.random.randint(4, 13)
        a = np.random.randint(2, 8)
        b = np.random.randint(1, 8)
        c = np.random.randint(1, 8)
        d = np.random.randint(2, 5)

    while a*mul!=(e+f-j):
        e = np.random.randint(1, 8)
        f = np.random.randint(2, 8)
        g = np.random.randint(1, 8)
        j = np.random.randint(1, 8)
        h = e * x - f * (y - x) - j * x
        mul = np.random.randint(2, 5)
    aa1 = str(a) +"(x + " + str(b)+") : (y - " + str(c)+") = " + str(d) +" : 1"
    aaa1 = str(a) +"(x + " + str(b)+") = " +str(d) +"(y - " + str(c)+")"

    aa2 = str(e)+"x - "
    if e==1:
        aa2 = "x - "
    if j==1:
        aa2 = aa2 + str(f)+"(y - x) = "+str(h) +" + x"
    else:
        aa2 = aa2 + str(f)+"(y - x) = "+str(h) +" + " +  str(j) +"x"
    vv1 = str(a)+"x - " + str(d)+"y = " + str(-(d*c)-(a*b))
    vv2 = str(e+f-j) +"x - " + str(f)+"y = " + str(h)
    if e+f-j==1:
        vv2 = "x - " + str(f)+"y = " + str(h)
    elif e+f-j==-1:
        vv2 = "-x - " + str(f) + "y = " + str(h)
    eq2 = str(-(d*mul)+f)+"y = " + str((-(d*c)-(a*b))*mul-h)
    if (-(d*mul)+f)==1:
        eq2 = "y = " + str((-(d*c)-(a*b))*mul-h)
    elif(-(d*mul)+f)==-1:
        eq2 = "-y = " + str((-(d*c)-(a*b))*mul-h)
    ytemp = proc_jo(y, 4)
    eq3 = str(a)+"x - " + str(d*y)+ " = " + str(-(d*c)-(a*b))
    if (d*y)<0:
        eq3 = str(a) + "x + " + str(abs(d * y)) + " = " + str(-(d * c) - (a * b))

    answ = x-y

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    aaa = "{cases{" + aaa1 + "#" + aa2 + "}}"
    vv = problm(vv1, vv2)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    eq4 = str(x) +" - " + str(y)
    if y<0:
        eq4 = str(x) + " - (" + str(y) +")"

    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq4=eq4, ytemp=ytemp, x=x, y=y, eq=eq, vv=vv, aaa=aaa, mul=mul, answ=answ, eq2=eq2, eq3=eq3)

    return stem, answer, comment

#중2-1-2-140
def expressions212_Stem_116():
    stem = "\nx, y에 대한 연립방정식 $$수식$${eq}$$/수식$$    $$수식$$``$$/수식$$           {temp} 만족\n\n" \
           "하는 x, y에 대하여 x : y = {ratio}일 때, 상수\n" \
           "a의 값은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x : y = {ratio}이므로 {eq2}\n" \
              "연립방정식 $$수식$${aaa}$$/수식$$          {temp2} 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n\n" \
              "x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp3} {aa2}에 대입하면\n" \
              "{eq3}    ∴ a = $$수식$${answ}$$/수식$$"

    xw = np.random.randint(0, 2)
    x = np.random.randint(0, 15)
    if xw == 1:
        x = x * -1
    mul = np.random.randint(2, 6)
    y = x*mul
    temp3 = proc_jo(y, 4)
    ratio ="1 : " + str(mul)
    eq2 = "y = " + str(mul) +"x"
    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = -1*(x*a)+y*b
    while c>50:
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = -1 * (x * a) + y * b
    aa1 = "-" + str(a) +"x + "
    if a==1:
        aa1 = "-x + "
    if b==1:
        aa1 = aa1 + "y = " + str(c)
    else:
        aa1 = aa1 + str(b)+"y = " + str(c)
    temp2 = proc_jo(c, 4)
    d = np.random.randint(1, 10)
    answ = np.random.randint(1, 10)
    e = d*x-answ*y
    while e>50:
        d = np.random.randint(1, 10)
        answ = np.random.randint(1, 10)
        e = d * x - answ * y
    aa2 = str(d) +"x - ay = " + str(e)
    if d==1:
        aa2 = "x - ay = " + str(e)
    eq3 = str(x*d) +" - " + str(y) +"a = " + str(e)
    if y==1:
        eq3 = str(x * d) + " - a = " + str(e)
    elif y==-1:
        eq3 = str(x * d) + " + a = " + str(e)
    elif y<0:
        eq3 = str(x * d) + " + " + str(abs(y)) + "a = " + str(e)

    temp = proc_jo(e, 4)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    aaa = "{cases{" + eq2 + "#" + aa1 + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(eq=eq,temp=temp, ratio=ratio, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, aa2=aa2, ratio=ratio, aaa=aaa, x=x, y=y, temp2=temp2, temp3=temp3, eq2=eq2, eq3=eq3)

    return stem, answer, comment

#중2-1-2-141
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_117():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$       $$수식$$``$$/수식$$                {temp} 만족\n\n" \
           "하는 x, y에 대하여 $$수식$$y over x$$/수식$$의 값은?\n" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "주어진 연립방정식에서\n" \
              "$$수식$${aaa}$$/수식$$\n\n" \
              "즉, $$수식$${vv}$$/수식$$\n\n" \
               "㉠$$수식$$TIMES$$/수식$$$$수식$${mul}$$/수식$${sign}㉡을 하면 x = $$수식$${x}$$/수식$$   \n" \
              "∴ x = $$수식$${x}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$${xtemp} ㉠에 대입하면 {eq3}    \n" \
              "∴ y = $$수식$${y}$$/수식$$\n" \
              "∴ $$수식$$y over x$$/수식$$ = {answ1} = {answ}" \

    xw = np.random.randint(0, 2)
    yw = np.random.randint(0, 2)
    x = np.random.randint(2, 15)
    y = np.random.randint(0, 15)
    if xw == 1:
        x = x * -1
    if yw == 1:
        y = y * -1
    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)
    d = np.random.randint(1, 10)
    e = np.random.randint(2, 6)
    f = np.random.randint(1, 10)
    g = e * (x - f * y) - y
    while d==c or (a*x-b*y)*c != (x-y)*d or (-d+c*b)==0 or (((e*-f)-1))%(-d+c*b)!=0:
        xw = np.random.randint(0, 2)
        yw = np.random.randint(0, 2)
        x = np.random.randint(2, 15)
        y = np.random.randint(0, 15)
        if xw == 1:
            x = x * -1
        if yw == 1:
            y = y * -1
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 10)
        d = np.random.randint(1, 10)
        e = np.random.randint(2, 6)
        f = np.random.randint(1, 10)
        g = e * (x - f * y) - y
    temp = proc_jo(g, 4)
    xtemp = proc_jo(x,4)
    gcd1 = gcd(c,d)
    c = int(c/gcd1)
    d = int(d/gcd1)
    aa1 = "(" + str(a)+"x - "
    if a==1:
        aa1 = "(x - "
    if b==1:
        aa1 = aa1 + "y) : (x - y) = " + str(c) +" : " + str(d)
    else:
        aa1 = aa1 + str(b) +"y) : (x - y) = " + str(c) +" : " + str(d)
    aaa1 = str(d) +"(x-y) = "
    if d==1:
        aaa1 = "(x-y) = "
    if c!=1:
        aaa1 = aaa1 +str(c)
    if a!=1:
        aaa1 = aaa1 + "(" + str(a) +"x - "
    else:
        aaa1 = aaa1 + "(x - "
    if b!=1:
        aaa1 = aaa1 + str(b) +"y)"
    else:
        aaa1 = aaa1 +"y)"
    sign="+"
    vv1 = str(d-c*a)+"x "
    eq3 = str((d-c*a)*x)
    if d-c*a==1:
        vv1 = "x "
    elif d-c*a==-1:
        vv1 = "-x "
    if (-d+c*b)==1:
        vv1 = vv1 + "+ y = " + str(0)
        eq3 = eq3 + "+ y = " + str(0)
    elif (-d+c*b)==-1:
        vv1 = vv1 + "- y = " + str(0)
        eq3 = eq3 + "- y = " + str(0)
        sign="-"
    elif (-d+c*b)<-1:
        vv1 = vv1 + "- " +str(abs(-d+c*b)) +"y = " + str(0)
        eq3 = eq3 + "- " +str(abs(-d+c*b)) +"y = " + str(0)
        sign="-"
    elif  (-d+c*b)>0:
        vv1 = vv1 + "+ " + str(abs(-d+c*b)) +"y = " + str(0)
        eq3 = eq3 + "+ " + str(abs(-d + c * b)) + "y = " + str(0)



    mul = int(abs(((e*-f)-1)/(-d+c*b)))
    aa2 = str(e) +"(x - " + str(f) +"y) - y = " + str(g)
    if f==1:
        aa2 = str(e) +"(x - y) - y = " + str(g)
    vv2 = str(e)+"x - " + str(e*f+1) +"y = " + str(g)

    eq2 = str((d-c*a)-e*mul)+"x = " + str(g*mul)
    if sign=="-":
        eq2 = str((d - c * a)- e*mul) + "x = " + str(-g)
    answ=""
    answ1=""
    gcd2 = gcd(abs(x),abs(y))
    if y<0 and x<0:
        if gcd2 != 1:
            answ1 = "$$수식$${" + str(y) + "} over {" + str(x) + "}$$/수식$$"
        xx = int(x/gcd2)
        yy = int(y/gcd2)
        answ = "$$수식$${" + str(abs(yy)) + "} over {" + str(abs(xx)) + "}$$/수식$$"
    elif y<0 or x<0:
        if gcd2 != 1:
            answ1 = "$$수식$${" + str(y) + "} over {" + str(x) + "}$$/수식$$"
        xx = int(x / gcd2)
        yy = int(y / gcd2)
        answ = "-$$수식$${" + str(abs(yy)) + "} over {" + str(abs(xx)) + "}$$/수식$$"
    else:
        if gcd2 != 1:
            answ1 = "$$수식$${" + str(y) + "} over {" + str(x) + "}$$/수식$$"
        xx = int(x / gcd2)
        yy = int(y / gcd2)
        answ = "$$수식$${" + str(abs(yy)) + "} over {" + str(abs(xx)) + "}$$/수식$$"
    if (y/x)%1==0:
        answ = int(y/x)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = problm(vv1, vv2)
    aaa = "{cases{" + aaa1 + "#" + aa2 + "}}"
    dd = []
    bb = []

    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(2, 10)
        if u>k and k/u not in dd and k != answ:
            dd.append(k/u)
            k = int(k/gcd(k,u))
            u = int(u/gcd(k,u))
            t = "$$수식$${" + str(abs(k)) + "} over {" + str(abs(u)) + "}$$/수식$$"
            if (k/u)%1==0:
                t = int(k/u)
            bb.append(t)
        uu = np.random.randint(1, 10)
        if uu not in dd:
            dd.append(uu)
            bb.append(str(uu))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(eq=eq, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(sign=sign, answ1=answ1, answ=answ, aa2=aa2, x=x, y=y, xtemp=xtemp, eq2=eq2, vv=vv, aaa=aaa, mul=mul,
                             eq3=eq3)

    return stem, answer, comment

#중2-1-2-142
#㉠㉡㉢㉣을 연립방정식에 넣으면 에러,
def expressions212_Stem_118():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$       $$수식$$``$$/수식$$                {temp} 만족시키는\n\n" \
           "x, y에 대하여 x + y의 값은?\n" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "순환소수를 분수로 나타내면\n" \
              "$$수식$${vv}$$/수식$$\n\n" \
              "㉠$$수식$$TIMES$$/수식$$$$수식$${mul}$$/수식$$, ㉡$$수식$$TIMES$$/수식$$$$수식$${mul2}$$/수식$${temp2} 하면\n" \
              "$$수식$${vvv}$$/수식$$\n\n" \
              "㉢-㉣$$수식$$TIMES$$/수식$$$$수식$${mul3}$$/수식$${temp3} 하면 {eq2}\n" \
              "∴ y = $$수식$${y}$$/수식$$\n" \
              "y = $$수식$${y}$$/수식$${temp4} ㉣에 대입하면 x = $$수식$${x}$$/수식$$\n" \
              "∴ x + y = $$수식$${answ}$$/수식$$"

    x = np.random.randint(0, 15)
    y = np.random.randint(0, 15)
    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)*10
    c = (x*a+y*b)
    aa1 = str(a/100) +"x + " + str(b/100) +"y = " + str(c/100)
    a1 = int(90/gcd(90,a))
    aa = int(a/gcd(90,a))
    b1 =int(90/gcd(90,b))
    bb = int(b/gcd(90,b))
    c1 = int(90/gcd(90,c))
    cc = int(c/gcd(90,c))
    vv1 = "{" +str(aa) +"} over {"+str(a1)+"}x + {" +str(bb) +"} over {"+str(b1)+"}y = {" +str(cc) +"} over {"+str(c1)+"}"
    if (cc/c1)%1==0:
        vv1 = "{" + str(aa) + "} over {" + str(a1) + "}x + {" + str(bb) + "} over {" + str(b1) + "}y = " + str(int(cc/c1))
    mul1 = lcm(a1,lcm(b1,c1))

    d = np.random.randint(1, 4)
    e = np.random.randint(1, 10)
    f = d*x+e*y
    aa2 = str(d/100) +"x + " + str(e/100) +"y = " + str(f/100)
    d1 = int(90 / gcd(90, d))
    dd = int(d / gcd(90, d))
    e1 = int(90 / gcd(90, e))
    ee = int(e / gcd(90, e))
    f1 = int(90 / gcd(90, f))
    ff = int(f / gcd(90, f))
    vv2 = "{" + str(dd) + "} over {" + str(d1) + "}x + {" + str(ee) + "} over {" + str(e1) + "}y = {" + str(ff) + "} over {" + str(f1) + "}"
    mul2 = lcm(lcm(d1, e1),f1)
    a = aa*int(mul1/a1)
    b = bb*int(mul1/b1)
    c = cc*int(mul1/c1)
    vvv1 = str(a) +"x + "
    if a==1:
        vvv1 = "x + "
    if b==1:
        vvv1 = vvv1 + "y = " + str(c)
    else:
        vvv1 = vvv1 + str(b) +"y = " + str(c)
    d = dd * int(mul2 / d1)
    e = ee * int(mul2 / e1)
    f = ff * int(mul2 / f1)
    vvv2 = str(d) + "x + "

    if d == 1:
        vvv2 = "x + "
    if e == 1:
        vvv2 = vvv2+ "y = " + str(f)
    else:
        vvv2= vvv2 + str(e) + "y = " + str(f)
    mul3 = a
    if d!=0:
        mul3 = int(a/d)
    eq2 = str(b-mul3*e)+"y = " + str(c-mul3*f)
    if (b-mul3*e)==1:
        eq2 = "y = " + str(c-mul3*f)
    elif (b-mul3*e)==-1:
        eq2 = "-y = " + str(c - mul3 * f)
    answ = x+y
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = problm(vv1, vv2)
    #여기㉢, ㉣
    dd = ""
    de=""
    vvv = "{cases{" + vvv1 + "`cdots`cdots`㉢" + dd+ "#" + vvv2 + "`cdots`cdots`㉣" + de + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    temp = proc_jo(f, 4)
    temp2 =proc_jo(mul2, 4)
    temp3 = proc_jo(mul3, 4)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    temp4 = proc_jo(y,4)
    stem = stem.format(eq=eq, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(mul=mul1, mul2=mul2, mul3=mul3, temp=temp, temp2=temp2, temp3=temp3, vv=vv, vvv=vvv, eq2=eq2, x=x, y=y, answ=answ, temp4=temp4)

    return stem, answer, comment

#중2-1-2-143
#㉠㉡㉢㉣을 연립방정식에 넣으면 에러,
def expressions212_Stem_119():
    stem = "\nx, y의 순서쌍 (a+b, a-b)가 연립방정식\n" \
           "$$수식$${eq}$$/수식$$         의 해일 때, $$수식$$a ^2$$/수식$$ - $$수식$$b ^2$$/수식$$의 값은?\n" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$      에서 $$수식$${vv}$$/수식$$\n\n" \
              "㉠$$수식$$TIMES$$/수식$$$$수식$${mul}$$/수식$$+㉡을 하면 {eq2}   ∴ x = $$수식$${x}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$${temp} ㉠에 대입하면 {eq3}    ∴ y = $$수식$${y}$$/수식$$\n" \
              "∴  $$수식$${vvv}$$/수식$$\n\n" \
              "㉢+㉣을 하면 {a_eq}   ∴ a = $$수식$${a}$$/수식$$\n" \
              "a = $$수식$${a}$$/수식$${temp2} ㉢에 대입하면\n" \
              "{eq4}   ∴ b = $$수식$${b}$$/수식$$\n" \
              "$$수식$$a ^2$$/수식$$ - $$수식$$b ^2$$/수식$$ = {eq5}"


    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    x = a+b
    y = a-b
    aa = np.random.randint(2, 10)
    bb = np.random.randint(2, 10)
    cc = int(lcm(aa, bb) / aa) * x - int(lcm(aa, bb) / bb) * y
    c = lcm(aa, bb)
    if cc != 0:
        cc1 = int(cc / gcd(abs(cc), c))
        c = int(c / gcd(abs(cc), c))
    d = np.random.randint(2, 10)
    e = np.random.randint(1, 10)
    f = np.random.randint(2, 10)
    g = np.random.randint(1, 10)
    e1 = int(e / gcd(f, e))
    lcm2 = lcm(d, f)
    d1 = int(lcm2 / d)
    e1 = int(lcm2 / f) * e
    lcm1 = lcm(lcm(aa, bb), c)
    bb1 = int(lcm1 / bb)

    while f==1 or cc==0 or e1%bb1!=0 or cc1>c or (x/d)+(y*(e/f))!=g:
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        while a<=b:
            a = np.random.randint(1, 10)
            b = np.random.randint(1, 10)
        x = a + b
        y = a - b
        aa = np.random.randint(2, 10)
        bb = np.random.randint(2, 10)
        cc = int(lcm(aa, bb) / aa) * x - int(lcm(aa, bb) / bb) * y
        c = lcm(aa, bb)
        if cc!=0:
            cc1 = int(cc / gcd(abs(cc), c))
            c = int(c / gcd(abs(cc), c))
        d = np.random.randint(2, 10)
        e = np.random.randint(1, 10)
        f = np.random.randint(2, 10)
        g = np.random.randint(1, 10)
        f = int(f/gcd(f,e))
        e1= int(e/gcd(f,e))
        lcm2 = lcm(d, f)
        d1 = int(lcm2 / d)
        e1 = int(lcm2 / f) * e
        lcm1 = lcm(lcm(aa, bb), c)
        bb1 = int(lcm1 / bb)

    aa1 = "x over {"+str(aa)+"} - y over {"+str(bb)+"} = {"+str(cc1)+"} over {"+str(c)+"}"
    aa2 = "x over {"+str(d)+"} + {" +str(e) +"} over {"+str(f)+"}y = " + str(g)
    lcm1 = lcm(lcm(aa,bb),c)
    aa = int(lcm1/aa)
    bb = int(lcm1/bb)
    c = int(lcm1/c)*cc1
    eq3 = str(aa * x) + " - "
    vv1 = str(aa) +"x - "
    if aa==1:
        vv1 = "x - "
    if bb==1:
        vv1 = vv1 +"y = " + str(c)
        eq3 = eq3 + "y = " + str(c)
    else:
        vv1 = vv1 + str(bb) +"y = " + str(c)
        eq3 = eq3 + str(bb) + "y = " + str(c)
    lcm2 = lcm(d, f)
    d = int(lcm2 / d)
    e = int(lcm2 / f)*e
    g = g*lcm2
    vv2 = str(d) + "x + "
    if d == 1:
        vv2 = "x + "
    if e == 1:
        vv2 = vv2 + "y = " + str(g)
    else:
        vv2 = vv2 + str(e) + "y = " + str(g)
    mul = int(e/bb)
    eq2 = str(mul*aa+d)+"x = " + str(mul*c+g)
    vvv1 = "a + b = " + str(x)
    vvv2 = "a - b = " + str(y)
    a_eq = "2a = " + str(x+y)
    eq4 = str(a) + " + b = " + str(x)
    answ = a**2-b**2
    eq5 = str(a**2) +" - " + str(b**2) +" = " + str(answ)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = problm(vv1, vv2)
    # 여기㉢, ㉣
    dd = ""
    de = ""
    vvv = "{cases{" + vvv1 + "`cdots`cdots`㉢" + dd + "#" + vvv2 + "`cdots`cdots`㉣" + de + "}}"
    temp = proc_jo(x, 4)
    temp2  =proc_jo(a,4)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq4=eq4, a_eq=a_eq, mul=mul, temp=temp, temp2=temp2, eq=eq, vv=vv, vvv=vvv, a=a, b=b, x=x, y=y, eq2=eq2, eq3=eq3, eq5=eq5, answ=answ)

    return stem, answer, comment

#중2-1-2-144
def expressions212_Stem_120():
    stem = "\n다음 연립방정식을 풀면?\n$$표$$\n" \
           "$$수식$${eq}$$/수식$$\n\n$$/표$$\n" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "주어진 연립방정식에서\n" \
              "$$수식$${eq1}$$/수식$$       즉, $$수식$${eq2}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$"

    xw = np.random.randint(0, 2)
    yw = np.random.randint(0, 2)
    x = np.random.randint(0, 15)
    y = np.random.randint(0, 15)
    if xw == 1:
        x = x * -1
    if yw == 1:
        y = y * -1
    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)
    d = np.random.randint(2, 10)
    e = np.random.randint(2, 10)
    while e==0 or ((a/10)*x+(b/10)*y-c)!=(-x+(1/d)*y):
        xw = np.random.randint(0, 2)
        yw = np.random.randint(0, 2)
        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15)
        if xw == 1:
            x = x * -1
        if yw == 1:
            y = y * -1
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 10)
        d = np.random.randint(2, 10)
        e = ((a/10)*x+(b/10)*y-c)*10
    e = int(e)
    gcddd = gcd(abs(e),10)
    eee = int(e/gcddd)
    tene = int(10/gcddd)
    aa1 = str(a/10) +"x + " + str(b/10) + "y - " + str(c) + " = - {"+str(abs(eee))+"} over {"+str(abs(tene))+"}"
    aa2 = "-x + 1 over {"+str(d)+"}y = - {"+str(abs(eee))+"} over {"+str(abs(tene))+"}"
    if (eee/tene)%1==0:
        aa1 = str(a / 10) + "x + " + str(b / 10) + "y - " + str(c) + " = - {" + str(abs(eee)) + "}"
        aa2 = "-x + 1 over {" + str(d) + "}y = - {" + str(abs(eee)) + "}"
    eq = str(a/10) +"x + " + str(b/10) + "y - " + str(c) + " = " +aa2
    vv1 = str(a) +"x + "
    if a==1:
        vv1 = "x + "
    if b==1:
        vv1 = vv1 + "y  = " + str(e+c*10)
    else:
        vv1 = vv1 + str(b) +"y = " + str(e+c*10)
    lcm1 = lcm(d,10)
    d = int(lcm1/d)
    e = int(lcm1/10)*e
    vv2 = "- " + str(lcm1) +"x + " + str(d) +"y = " + str(e)
    if d==1:
        vv2 = "- x + y = " + str(e)
    answ = "x = " + str(x)+ " , y = " + str(y)
    eq1 = "{cases{" + aa1 + "#" + aa2 + "}}"
    eq2 = "{cases{" + vv1 + "#" + vv2 + "}}"
    bb=[]
    bb.append("해가 무수히 많다.")
    bb.append("해가 없다.")
    bb.append("x = " + str(-x)+ " , y = " + str(y))
    bb.append("x = " + str(-x)+ " , y = " + str(-y))
    bb.append("x = " + str(x)+ " , y = " + str(-y))



    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, eq1=eq1, eq2=eq2, x=x, y=y)

    return stem, answer, comment

#중2-1-2-145
def expressions212_Stem_121():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$           에서 x, y의 값의 차\n\n" \
           "가 $$수식$${dif}$$/수식$$일 때, 상수 a의 값은? (단, x &gt; y)"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x = y + $$수식$${dif}$$/수식$${temp} 각각의 방정식에 대입하여 정리하면\n" \
              "$$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 y = $$수식$${y}$$/수식$$, a = $$수식$${answ}$$/수식$$"

    x = np.random.randint(0, 15)
    y = np.random.randint(0, 15)
    while y>=x:
        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15)
    dif = x-y
    temp = proc_jo(dif,4)
    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    answ = a*x-b
    aa1 = str(a)+"x - "+ str(b) +" = a"
    vv1 = str(a)+"y - a = " + str(b-a*dif)
    if a==1:
        aa1 = "x - " + str(b) +" = a"
        vv1 = "y - a = " + str(b - a * dif)
    c = np.random.randint(1, 10)
    d = np.random.randint(1, 10)
    e = c*x+d*y+answ
    aa2 = str(c)+"x - "
    vv2 = str(c+d) +"y + a = " + str(e-c*dif)
    if c==1:
        aa2 = "x - "
        vv2 = str(d+1) + "y + a = " + str(e - c * dif)
    if d==1:
        aa2 = aa2 +"y = " + str(e) + " - a"
    else:
        aa2 = aa2 +str(d) + "y = " + str(e) + " - a"
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + vv1 + "#" + vv2 + "}}"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(eq=eq, dif=dif, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp=temp, answ=answ, dif=dif, eq=eq, y=y, vv=vv)

    return stem, answer, comment

#중2-1-2-146
def expressions212_Stem_122():
    stem = "\nx, y에 대한 연립방정식 \n" \
           "$$수식$${eq}$$/수식$$             의 해가\n" \
           "x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$일 때, a + b의 값은? (단, a, b는\n" \
           "상수이다.)"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp} 연립방정식에 대입하면\n" \
              "$$수식$${eq2}$$/수식$$\n" \
              "$$수식$${aaa}$$/수식$$               에서   $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 a = $$수식$${aa}$$/수식$$, b = $$수식$${bb}$$/수식$$\n" \
              "∴ a + b = $$수식$${answ}$$/수식$$"

    x = np.random.randint(1, 15)
    y = np.random.randint(1, 15)
    aa = np.random.randint(1, 10)
    bb = np.random.randint(1, 10)
    a = np.random.randint(2, 10)
    b = np.random.randint(1, 10)
    c = aa*x+bb*y-x-y
    while (aa*x+bb*y)!=(a*(aa*x-bb*y)-b) or c==0:
        x = np.random.randint(1, 15)
        y = np.random.randint(1, 15)
        aa = np.random.randint(1, 10)
        bb = np.random.randint(1, 10)
        a = np.random.randint(2, 10)
        b = np.random.randint(1, 10)
        c = aa * x + bb * y - x - y
    pp= bb
    temp = proc_jo(y,4)
    eq = "ax + by = " + str(a) +"(ax - by) - " + str(b) + " = x + y + " + str(c)
    eq2 = str(x)+"a + "
    aaa1=str(x) +"a + "
    aaa2 = str(a) +"(" + str(x) +"a - "
    if x==1:
        eq2 = "a + "
        aaa1 = "a + "
    if y==1:
        eq2 = eq2 + "b = " + str(a)
        aaa1 = aaa1 +"b = " + str(x+y+c)
    else:
        eq2 = eq2 + str(y) +"b = " + str(a)
        aaa1 = aaa1 + str(y) +"b = " + str(x+y+c)
    if x==1:
        eq2 = eq2 + "(a - "
        aaa2 = str(a) +"(a - "
    else:
        eq2 = eq2 + "(" + str(x) + "a - "
    if y==1:
        eq2 = eq2 + "b) - " + str(b)+" = " + str(x) +" + " + str(y) +" + " + str(c)
        aaa2 = aaa2 +"b) - " + str(b) +" = " + str(x+y+c)
    else:
        eq2 = eq2 + str(y) +"b) - " + str(b) +" = " + str(x) +" + " + str(y) +" + " + str(c)
        aaa2 = aaa2 + str(y)+ "b) - " + str(b) +" = " + str(x + y + c)

    vv2 = str(a*x) +"a - " + str(a*y) +"b = " + str(x+y+c+b)
    answ = aa+bb

    aaa = "{cases{" + aaa1 + "#" + aaa2 + "}}"
    vv = "{cases{" + aaa1 + "#" + vv2 + "}}"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(x=x, y=y, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp=temp, answ=answ, eq2=eq2, aa=aa, bb=pp, aaa=aaa, vv=vv, x=x, y=y)

    return stem, answer, comment

#중2-1-2-147
def expressions212_Stem_123():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$                   {temp} 만족시키는 x\n\n" \
           "의 값이 y의 값보다 $$수식$${dif}$$/수식$$만큼 클 때, 상수 a의 값\n" \
           "은?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x의 값이 y의 값보다 $$수식$${dif}$$/수식$$만큼 크므로 x = y + $$수식$${dif}$$/수식$$\n" \
              "$$수식$${vv}$$/수식$$              {temp} 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n\n" \
              "x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp2} {aa1}에 대입하\n" \
              "면 {eq2}, {eq3}\n" \
              "∴ a = $$수식$${answ}$$/수식$$"

    xw = np.random.randint(0, 2)
    yw = np.random.randint(0, 2)
    x = np.random.randint(0, 15)
    y = np.random.randint(0, 15)
    if xw == 1:
        x = x * -1
    if yw == 1:
        y = y * -1
    answ = np.random.randint(1, 10)
    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    c = np.random.randint(2, 10) * -1
    d = a * x + b * y + c * answ
    while x<=y or d<=0:
        xw = np.random.randint(0, 2)
        yw = np.random.randint(0, 2)
        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15)
        if xw == 1:
            x = x * -1
        if yw == 1:
            y = y * -1
        answ = np.random.randint(1, 10)
        a = np.random.randint(1, 10)
        b = np.random.randint(1, 10)
        c = np.random.randint(2, 10) * -1
        d = a * x + b * y + c * answ
    dif = abs(x-y)



    aa1 = str(a) +"x + "
    if a==1:
        aa1 = "x + "
    if b==1:
        aa1 = aa1 + "y = " + str(c) +"a - " + str(d)
    else:
        aa1 = aa1 + str(b) +"y = "+ str(c) +"a - " + str(d)
    e = np.random.randint(1, 10)
    f = np.random.randint(1, 10)
    g = e*x-f*y
    temp = proc_jo(g, 4)
    aa2 = str(e) +"x - "
    if e==1:
        aa2 = "x - "
    if f==1:
        aa2 = aa2 +"y = " + str(g)
    else:
        aa2 = aa2 +str(f) +"y = " + str(g)
    eq2 = str(x*a) + " + " + str(b*y) +" = " + str(c)+"a - " + str(d)
    if b*y<0:
        eq2 = str(x * a) + " - " + str(abs(b * y)) + " = " + str(c) + "a - " + str(d)
    eq3 = str(c)+"a = " + str(c*answ)
    temp2 = proc_jo(y,4)

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{x = y - " + str(dif) + "#" + aa2 + "}}"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, temp=temp, dif=dif, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(aa1=aa1, temp2=temp2, temp=temp, answ=answ, eq2=eq2, eq3=eq3, vv=vv, x=x, y=y, dif=dif)

    return stem, answer, comment

#중2-1-2-148
#㉠㉡을 연립방정식에 넣으면 에러,
def expressions212_Stem_124():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$                        에서 ㉠의 $$수식$${num}$$/수식$${temp} 잘\n\n" \
           "못 보고 풀어서 x = $$수식$${x}$$/수식$${temp2} 얻었다. $$수식$${num}$$/수식$${temp} 어떤 수로\n" \
           "잘못 보았는가?" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x = $$수식$${x}$$/수식$${temp2} ㉡에 대입하면 {eq2}\n" \
              "∴ y = $$수식$${y}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$ {temp3} ㉠의 좌변에 대입하면\n" \
              "{eq3}\n" \
              "따라서 $$수식$${num}$$/수식$${temp} $$수식$${answ}$$/수식$$로 잘못 보았다."

    num = np.random.randint(1, 10)
    x = np.random.randint(0, 15)
    y = np.random.randint(0, 15)*-1
    a = np.random.randint(2, 10)
    b = np.random.randint(2, 10)
    answ = a*x-y
    while answ>15 or num==a:
        num = np.random.randint(1, 10)
        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15) * -1
        a = np.random.randint(2, 10)
        b = np.random.randint(2, 10)
        answ = a * x - y
    aa1 = str(a) +"x - y = " + str(num)
    temp = proc_jo(num,4)
    temp2 = proc_jo(x,4)
    temp3 = proc_jo(y,4)
    c = b*x-y
    aa2 = str(b)+"x - y = " + str(c)
    eq2=str(b*x) + " - y = " + str(c)
    eq3 = str(a) +"x - y = " + str(a*x) + " + " + str(abs(y)) +" = " + str(answ)


    eq = problm(aa1, aa2)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, temp2=temp2, temp=temp, num=num,x=x, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(x=x, y=y, eq2=eq2, temp2=temp2, temp3=temp3, temp=temp, num=num, answ=answ, eq3=eq3)

    return stem, answer, comment

#중2-1-2-149
def expressions212_Stem_125():
    stem = "\n다음 두 연립방정식의 해가 서로 같을 때 a, b의\n" \
           "값은? $$표$$\n" \
           "$$수식$${eq}$$/수식$$                , $$수식$${eq2}$$/수식$$\n\n" \
           "$$/표$$"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "두 연립방정식의 해는 연립방정식\n" \
              "$$수식$${vv}$$/수식$$                  의 해와 같다.\n\n" \
              "이 연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp} {aa2}, {bb2}에\n" \
              "각각 대입하면\n" \
              "{eq3}     ∴ a = $$수식$${aa}$$/수식$$\n" \
              "{eq4}     ∴ b = $$수식$${bb}$$/수식$$"

    xw = np.random.randint(0, 2)
    yw = np.random.randint(0, 2)
    x = np.random.randint(1, 15)
    y = np.random.randint(1, 15)
    if xw == 1:
        x = x * -1
    if yw == 1:
        y = y * -1
    a = np.random.randint(1, 10)*-1
    b = np.random.randint(1, 10)
    c = a*x+b*y
    aa1 = str(a) + "x + "
    if a==-1:
        aa1 = "-x + "
    if b==1:
        aa1 = aa1 +"y = " + str(c)
    else:
        aa1 = aa1 + str(b) +"y = " + str(c)
    aa = np.random.randint(1, 10)
    d = np.random.randint(1, 10)
    e = aa*x+d*y
    aa2 = "ax + " + str(d) +"y = " + str(e)
    if d==1:
        aa2 = "ax + y = " + str(e)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    f = np.random.randint(1, 10)*-1
    g = np.random.randint(1, 10)
    h = f*x-g*y
    bb1 = str(f) +"x - "
    if f==-1:
        bb1 = "-x + "
    if g==1:
        bb1 = bb1 + "y = " + str(h)
    else:
        bb1 = bb1 + str(g) +"y = " + str(h)
    j = np.random.randint(1, 10)
    bb = np.random.randint(1, 10)*-1
    k = j*x+bb*y
    bb2 = str(j) +"x + by = " + str(k)
    if j==1:
        bb2 = "x + by = " + str(k)

    eq2 ="{cases{" + bb1 + "#" + bb2 + "}}"
    vv = "{cases{" + aa1 + "#" + bb1 + "}}"
    eq3 = str(x) +"a "
    eq4 = str(j*x)
    if x==1:
        eq3 ="a "
    elif x==-1:
        eq3 ="-a "
    if d*y>0:
        eq3 = eq3 + "+ " + str(d*y) +" = " + str(e)
    elif d*y<0:
        eq3 = eq3 + "- " + str(abs(d* y)) + " = " + str(e)
    elif d*y==0:
        eq3 = eq3 + " = " + str(e)
    if y>0:
        eq4 = eq4 + " + " + str(y) +"b = " + str(k)
        if y==1:
            eq4 = eq4 + " + b = " + str(k)
    elif y<0:
        eq4 = eq4 + " - " + str(-y) + "b = " + str(k)
        if y==-1:
            eq4 = eq4 + " - b = " + str(k)
    answ = "a = " + str(aa) +", b = " + str(bb)
    pp =bb
    bb = []
    bb.append("a = " + str(-1*aa) +", b = " + str(pp))
    bb.append("a = " + str(-1*aa) + ", b = " + str(-1*pp))

    dd=[]
    while len(bb) < 4:
        xw = np.random.randint(0, 2)
        yw = np.random.randint(0, 2)
        k = np.random.randint(1, 10)
        u = np.random.randint(1, 10)
        if xw == 1:
            k = k * -1
        if yw == 1:
           u = u * -1
        t = [k,u]
        if k!=aa and k!=-1*aa and u!=pp and u!=-1*pp and t not in dd:
            bb.append("a = " + str(k) + ", b = " + str(u))
            bb.append("a = " + str(-1*k) + ", b = " + str(u))
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    temp = proc_jo(y,4)
    stem = stem.format(eq=eq, eq2=eq2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(aa2=aa2, bb2=bb2,temp=temp, vv=vv, x=x, y=y, aa1=aa1, bb1=bb1, eq3=eq3, eq4=eq4, aa=aa, bb=pp)

    return stem, answer, comment

#중2-1-2-150
def expressions212_Stem_126():
    stem = "\nx, y에 대한 연립방정식 $$수식$${eq}$$/수식$$            의 해가 \n\n" \
           "무수히 많을 때, x에 대한 일차방정식\n" \
           "{eq1}이 해를 갖지 않도록 하\n" \
           "는 b의 값은?(단, a, b는 상수이다.)" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "연립방정식 $$수식$${eq}$$/수식$$            의 x의 계수를 같게\n\n" \
              "하면 $$수식$${vv}$$/수식$$                에서 해가 무수히 많으므로\n\n" \
              "{eq3}, {eq4}    ∴ a = $$수식$${aa}$$/수식$$\n" \
              "이때 x에 대한 일차방정식이 해를 갖지 않으려면\n" \
              "0$$수식$$TIMES$$/수식$$x = (0이 아닌 상수) 꼴이어야 한다.\n" \
              "{eq1}에서 {eq5}\n" \
              "따라서 {eq6}, {eq7}이므로 b = $$수식$${pp}$$/수식$$"


    xw = np.random.randint(0, 2)
    yw = np.random.randint(0, 2)
    x = np.random.randint(0, 15)
    y = np.random.randint(0, 15)
    aa = np.random.randint(1, 10)
    pp = np.random.randint(1, 10)
    if xw == 1:
        aa=aa * -1
    if yw == 1:
        pp = pp * -1
    a = x+aa*y
    b = np.random.randint(1, 10)
    c = np.random.randint(1, 10)
    d = int((b*x+c*y)/aa)
    while b*aa!=c or aa==pp or (b*x+c*y)/aa==1 or (b*x+c*y)%aa!=0:
        xw = np.random.randint(0, 2)
        yw = np.random.randint(0, 2)
        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15)
        aa = np.random.randint(1, 10)
        pp = np.random.randint(1, 10)
        if xw == 1:
            aa = aa * -1
        if yw == 1:
            pp = pp * -1
        a = x + aa * y
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 10)
        d = int((b*x+c*y)/aa)
    aa1 = "x + ay = " + str(a)
    aa2 = str(b) +"x + "
    vv1 = str(b) + "x + " + str(b) +"ay = " + str(a*b)
    eq3 = str(b)+"a = " + str(c)
    eq4 = str(b*a) + " = " + str(d) +"a"
    if b==1:
        aa2 ="x + "
        vv1 = "x + ay = " + str(a*b)
        eq3 = "a = " + str(c)
    if c!=1:
        aa2 = aa2 +str(c) +"y = " + str(d) +"a"
    else:
        aa2 = aa2 +"y = " + str(d) +"a"
    mm = pp-aa
    l = np.random.randint(1, 10)
    while l==pp:
        l = np.random.randint(1, 10)
    eq1 = "(b - a "
    eq5 = "(b"
    if mm>0:
        eq1=eq1 + " - " + str(mm) +")x + (b - " + str(l) +") = 0"
        eq5 = eq5 + " - " + str(abs(mm + aa)) + ")x = " + str(l) + " - b"
    else:
        eq1 = eq1 + " + " + str(abs(mm)) + ")x + (b - " + str(l) + ") = 0"
        eq5 = eq5 + " + " + str(abs(mm + aa)) + ")x = " + str(l) + " - b"


    eq6=""
    if pp>0:
        eq6 = "b - " + str(pp) + " = 0"
    elif pp<0:
        eq6 = "b + " + str(abs(pp)) + " = 0"
    eq7 = str(l) +" - b ≠ 0"
    answ = pp

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + vv1 + "#" + aa2 + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(eq=eq, eq1=eq1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq1=eq1, eq=eq, vv=vv, eq6=eq6, eq7=eq7, eq3=eq3, eq4=eq4, eq5=eq5, aa=aa, pp=pp)

    return stem, answer, comment

#중2-1-2-151
def expressions212_Stem_127():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$                 의 해가 없을\n\n" \
           "때, 상수 a, b의 조건은?\n" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "주어진 연립방정식에서\n" \
              "$$수식$${vv}$$/수식$$\n\n" \
              "연립방정식의 해가 없으므로\n" \
              "$$수식$${eq1}$$/수식$$\n" \
              "즉, {eq2},  {eq3}\n" \
              "∴ a = $$수식$${aa}$$/수식$$, b ≠ $$수식$${pp}$$/수식$$"
    x = np.random.randint(0, 15)
    y = np.random.randint(0, 15)
    a = np.random.randint(2, 10)
    b = np.random.randint(2, 10)
    c = np.random.randint(2, 10)*-1
    aa1 = int(lcm(a,b)/a)*x
    aa2 = int(lcm(a,b)/b)*(y+c)
    bb1 = aa1-aa2
    bb2 = lcm(a,b)
    if bb1!=0:
        bb1 = int(bb1/gcd(abs(bb1),bb2))
        bb2 = int(bb2/gcd(abs(bb1),bb2))
    d = bb1
    j = bb2
    lcm1 = lcm(lcm(a,b),abs(j))
    a1 = int(lcm1/a)
    b1= int(lcm1/b)
    d1 = int(lcm1/j)*d
    aa = np.random.randint(1, 10)
    e = np.random.randint(1, 10)
    f = np.random.randint(1, 10)
    pp = (aa - e) * x + f * y
    while d<=0 or (f*(d1+c*b1))!=(b1*-1*pp) or (-1*b1*(aa-e))!=(a1*f) or f*(d1+c*b1)==0:
        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15)
        a = np.random.randint(2, 10)
        b = np.random.randint(2, 10)
        c = np.random.randint(2, 10)*-1
        aa1 = int(lcm(a, b) / a)*x
        aa2 = int(lcm(a, b) / b) * (y + c)
        bb1 = aa1 - aa2
        bb2 = lcm(a, b)
        if bb1 != 0:
            bb1 = int(bb1 / gcd(abs(bb1), bb2))
            bb2 = int(bb2 / gcd(abs(bb1), bb2))
        d = bb1
        j = bb2
        lcm1 = lcm(lcm(a, b), abs(j))
        a1 = int(lcm1 / a)
        b1 = int(lcm1 / b)
        d1 = int(lcm1 / j) * d
        aa = np.random.randint(1, 10)
        e = np.random.randint(1, 10)
        f = np.random.randint(1, 10)
        pp = (aa - e) * x + f * y
    print(x)
    print(y)
    d = int(d/gcd(abs(d),j))
    j = int(j/gcd(abs(d),j))
    aa1 = "1 over {"+str(a)+"}x - 1 over {"+str(b)+"}(y - " + str(abs(c))+") = {"+str(d)+"} over {"+str(j)+"}"
    if j==1:
        aa1 = "1 over {" + str(a) + "}x - 1 over {" + str(b) + "}(y - " + str(abs(c)) + ") = " +str(d)

    vv1 = str(a1)+"x - "
    if a1==1:
        vv1 = "x - "
    if b1==1:
        vv1 = vv1 +"y = " + str(d1+c)
    else:
        vv1 = vv1 + str(b1) +"y = " + str(d1+c*b1)

    aa2 = "(a - " + str(e) +")x + " + str(f) +"y = b"
    if f==1:
        aa2 = "(a - " + str(e) + ")x + y = b"
    eq1 = "{"+str(a1)+"} over {a - " + str(e) +"} = {"+str(-1*b1)+"} over {" + str(f) +"} ≠ {"+str(d1+c*b1)+"} over b"
    eq2 = str(-1*b1) +"(a - " + str(e) +") = " + str(a1*f)
    eq3 =  str(-1*b1) +"b ≠ " + str(f*(d1+c*b1))
    if -1*b1==-1:
        eq2 = "-(a - " + str(e) +") = " + str(a1*f)
        eq3 = "-b ≠ " + str(f*(d1+c*b1))
    answ = "a = " + str(aa) +", b ≠ " + str(pp)

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + vv1 + "#" + aa2 + "}}"
    bb = []
    bb.append("a = " + str(-1*aa) +", b ≠ " + str(pp))
    bb.append("a = " + str(-1*aa) +", b = " + str(-1*pp))
    bb.append("a = " + str(-aa) + ", b = " + str(pp))
    bb.append("a ≠ " + str(-aa) + ", b = " + str(pp))

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(aa=aa, pp=pp, vv=vv, eq2=eq2, eq1=eq1, eq3=eq3)

    return stem, answer, comment

#중2-1-2-152
#㉠㉡㉢㉣을 연립방정식에 넣으면 에러
def expressions212_Stem_128():
    stem = "\nx, y에 대한 연립방정식 $$수식$${eq}$$/수식$$               {temp} 푸는\n\n" \
           "데 {name1}는 c를 d로 잘못 보고 풀어서 x = $$수식$${xx1}$$/수식$$,\n" \
           "y = $$수식$${yy1}$$/수식$${temp2} 얻었고, {name2}는 바르게 풀어서\n" \
           "x = $$수식$${xx2}$$/수식$$, y = $$수식$${yy2}$$/수식$${temp3} 얻었다. 이때 상수 a, b, c,\n" \
           "d에 대하여 a + b - c - d의 값은?\n" \
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "x = $$수식$${xx1}$$/수식$$, y = $$수식$${yy1}$$/수식$${temp2}$$수식$${eqq}$$/수식$$             에 대입하면\n\n" \
              "$$수식$${vv}$$/수식$$\n\n" \
              "x = $$수식$${xx2}$$/수식$$, y = $$수식$${yy2}$$/수식$${temp3}$$수식$${eq}$$/수식$$               에 대입하면\n\n" \
              "$$수식$${vvv}$$/수식$$\n\n" \
              "㉠+㉢$$수식$$TIMES$$/수식$$$$수식$${mul}$$/수식$${temp4} 하면 {eq2}   ∴ b = $$수식$${pp}$$/수식$$\n" \
              "b = $$수식$${pp}$$/수식$${temp5} ㉢에 대입하면 {eq3}\n" \
              "∴ a = $$수식$${aa}$$/수식$$\n" \
              "㉡을 풀면 {eq4} ∴ d = $$수식$${dd}$$/수식$$\n" \
              "㉣을 풀면 {eq5} ∴ c = $$수식$${cc}$$/수식$$\n" \
              "∴ a + b - c - d = {eq6} = $$수식$${answ}$$/수식$$"

    nameList = ["경희", "민철이", "수진이", "철수","영대","미영이","은혜"]
    o = np.random.randint(0, 7)
    name1 = nameList[o]
    o1 = np.random.randint(0,7)
    name2 = nameList[o1]
    while o ==o1:
        o1 = np.random.randint(0, 7)
        name2 = nameList[o1]
    aa = np.random.randint(0, 8)
    pp = np.random.randint(0, 8)
    cc = np.random.randint(0, 8)*-1
    dd = np.random.randint(0, 8)
    xx2 = np.random.randint(1, 5)*-1
    mul = np.random.randint(1, 5)
    xx1 = xx2*mul*-1
    yy1 = np.random.randint(0, 8)*-1
    yy2 = np.random.randint(0, 8)
    num = np.random.randint(1, 8)
    las = aa*xx1+pp*yy1
    las2 = dd*xx1+num*yy1
    while xx1==xx2 or yy1==yy2 or yy1+yy2*mul==0 or las!=(aa*xx2+pp*yy2) or las2!=(cc*xx2+num*yy2):
        aa = np.random.randint(0, 7)
        pp = np.random.randint(0, 7)
        cc = np.random.randint(0, 7)*-1
        dd = np.random.randint(0, 7)
        xx2 = np.random.randint(1, 5)*-1
        mul = np.random.randint(1, 5)
        xx1 = xx2*mul*-1
        yy1 = np.random.randint(1, 7)*-1
        yy2 = np.random.randint(1, 7)
        num = np.random.randint(2, 7)
        las = aa*xx1+pp*yy1
        las2 = dd*xx1+num*yy1
    aa1 = "ax + by = " + str(las)
    aa2 = "cx + " + str(num) +"y = " + str(las2)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    aaa2 = "dx + " + str(num) +"y = " + str(las2)
    eqq = "{cases{" + aa1 + "#" + aaa2 + "}}"
    vv1 = str(xx1) +"a - "
    vv2 = str(xx1) +"c - " + str(abs(num*yy1)) +" = " + str(las2)
    if xx1==1:
        vv1 = "a - "
        vv2 = "c - " + str(abs(num*yy1)) +" = " + str(las2)
    if yy1==-1:
        vv1 = vv1 +"b = " + str(las)
    else:
        vv1 = vv1 + str(abs(yy1)) +"b = " + str(las)

    vv = problm(vv1, vv2)

    vvv1 = str(xx2) + "a + "
    vvv2 = str(xx2) +"d + " + str(yy2*num)+"y = " + str(las2)
    if xx2 == -1:
        vvv1 = "-a + "
        vvv2 = "-d + " + str(yy2*num)+"y = " + str(las2)
    if yy2 == 1:
        vvv1 = vvv1 + "b = " + str(las)
    else:
        vvv1 = vvv1 + str(abs(yy2)) + "b = " + str(las)

    # 여기㉢, ㉣
    mm = ""
    de = ""
    vvv = "{cases{" + vvv1 + "`cdotscdots`㉢" + mm + "#" + vvv2 + "`cdotscdots`㉣" + de + "}}"
    eq2 = str(yy1+yy2*mul) +"b = " + str(las+las*mul)
    if (yy1+yy2*mul)==1:
        eq2 ="b = " + str(las + las * mul)
    elif (yy1+yy2*mul)==-1:
        eq2 ="-b = " + str(las + las * mul)
    eq3 = str(xx2) +"a + " + str(yy2*pp) + " = " + str(las)
    if xx2==-1:
        eq3 = "-a + " + str(yy2 * pp) + " = " + str(las)
    eq4 = str(xx1) +"d = " + str(xx1*dd)
    if xx1==1:
        eq4 = "d = " + str(xx1 * dd)
    eq5 = str(xx2) +"c = " + str(xx2*cc)
    if xx2==-1:
        eq5 = "-c = " + str(xx2 * cc)
    eq6 = str(aa) +" + " + str(pp) +" + (" +str(cc) +") + " + str(dd)
    answ =aa+pp+cc+dd

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    temp = proc_jo(las2, 4)
    temp2 = proc_jo(yy1, 4)
    temp3 = proc_jo(yy2, 4)
    temp4 = proc_jo(mul,4)
    temp5 = proc_jo(pp,4)

    stem = stem.format(eq=eq, temp=temp, name1=name1, xx1=xx1,yy1=yy1, temp2=temp2, name2=name2, xx2=xx2,yy2=yy2, temp3=temp3, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(xx1=xx1, yy1=yy1,temp2=temp2, vv=vv, eqq=eqq, xx2=xx2, yy2=yy2, temp3=temp3,eq=eq,vvv=vvv,mul=mul, temp4=temp4, eq2=eq2, pp=pp,temp5=temp5, eq3=eq3,aa=aa, eq4=eq4, eq5=eq5, eq6=eq6, dd=dd, cc=cc, answ=answ)

    return stem, answer, comment

#중2-1-2-153
#㉠㉡을 연립방정식에 넣으면 에러
def expressions212_Stem_129():
    stem = "\n연립방정식 $$수식$${eq}$$/수식$$             의 해가 연립방정식\n\n" \
           "$$수식$${eq2}$$/수식$$                    {temp} 만족시키는 x의 값과 y의 값\n\n" \
           "을 바꾸어 놓은 것과 같을 때, 상수 a, b에 대하\n" \
           "여 ab의 값은?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$                    의 해는\n\n" \
              "$$수식$${chang}$$/수식$$                      의 해와 같다.\n\n" \
              "㉠$$수식$$TIMES$$/수식$$$$수식$${mul}$$/수식$$-㉡을 하면 {eq3}    ∴ y = $$수식$${y}$$/수식$$\n" \
              "y = $$수식$${y}$$/수식$${temp2} ㉠에 대입하면 {eq4}    ∴ x = $$수식$${x}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$${temp2} {eq12}에 대입하면\n" \
              "{eq5}  ∴ {eq6}$$수식$$`cdots`cdots`$$/수식$$㉢\n" \
              "x = $$수식$${y}$$/수식$$, y = $$수식$${x}$$/수식$${temp3} {eq22}에 대입하면\n" \
              "{eq7} $$수식$$`cdots`cdots`$$/수식$$㉣\n" \
              "㉢$$수식$$TIMES$$/수식$$$$수식$${mul2}$$/수식$$-㉣을 하면 {eq8} ∴ a = $$수식$${aa}$$/수식$$\n" \
              "a = $$수식$${aa}$$/수식$${temp4} ㉢에 대입하면 {eq9}\n" \
              "∴ b = $$수식$${pp}$$/수식$$\n" \
              "∴ ab = $$수식$${answ}$$/수식$$"

    x = np.random.randint(1, 15)
    y = np.random.randint(1, 15)
    aa = np.random.randint(1, 15)*-1
    pp = np.random.randint(1, 15)*-1
    a =  np.random.randint(1, 10)
    b = x+a*y

    a1 =  np.random.randint(1, 10)*-1
    b1 =  np.random.randint(1, 10)
    c1 = a1*y+b1*x
    mul = b1
    while c1!=a1*x+b1*y or (b*mul-c1)*y!=(a*mul-a1)!=0:
        x = np.random.randint(1, 8)
        y = np.random.randint(1, 8)
        aa = np.random.randint(1, 8) * -1
        pp = np.random.randint(1, 8) * -1
        a = np.random.randint(1, 8)
        b = x + a * y
        a1 = np.random.randint(1, 8) * -1
        b1 = np.random.randint(1, 8)
        c1 = a1 * y + b1 * x
        x = np.random.randint(1, 8)
        y = np.random.randint(1, 8)
        mul = b1
    eq11 = "x + " + str(a) + "y = " + str(b)
    if a==1:
        eq11 = "x + y = " + str(b)
    eq21 = str(a1) +"x + "
    chang1 = " - " + str(abs(a1)) +"y = " + str(c1)
    if a1==-1:
        eq21 = "-x + "
        chang1 = "- y = " + str(c1)
    if b1==1:
        eq21 = eq21 +"y = " + str(c1)
        chang1 = "x" + chang1
    else:
        eq21 = eq21 + str(b1) + "y = " + str(c1)
        chang1 = str(b1) +"x" + chang1
    c = np.random.randint(1, 10)
    d = c*aa*x+y-pp
    eq12 = str(c) +"ax + y = b - " + str(abs(d))
    if c==1:
        eq12 = "ax + y = b - " + str(d)
    eq = "{cases{" + eq11 + "#" + eq12 + "}}"
    d1 = np.random.randint(1, 10)
    e1 = aa*x-d1*pp*y
    eq22 = "ax - " + str(d1) +"by = " + str(e1)
    if d1==1:
        eq22 = "ax - by = " + str(e1)
    eq2 = "{cases{" + eq21 + "#" + eq22 + "}}"
    chang = problm(eq11, chang1)
    mul = b1
    eq3 = str(a*mul-a1) +"y = " + str(b*mul-c1)
    temp = proc_jo(e1,4)
    temp2 = proc_jo(y,4)
    temp3 = proc_jo(x,4)
    temp4 = proc_jo(aa, 4)
    eq4 = "x + " + str(a*y) +" = " + str(b)
    eq5 = str(c*x) + "a + " + str(y) +" = b - " + str(abs(d))
    eq6 = str(c*x) + "a - b = " + str(d-y)
    if c*x == 1:
        eq12 = "a + y = b - " + str(d)
        eq6 ="a - b = " + str(d - y)
    eq7 = str(y) + "a - "
    if y == 1:
        eq7 = "a - "
    if d1*x!=1:
        eq7 = eq7 + str(d1*x) + "b = " + str(e1)
    else:
        eq7 = eq7 + "b = " + str(e1)
    mul2 = d1*x
    eq8 = str(c*x*d1*x-y) +"a = " + str((d -y)*d1*x-e1)
    eq9 = str(c * x*aa) + " - b = " + str(d - y)
    answ = aa*pp

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = (answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, temp=temp, eq2=eq2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(aa=aa, pp=pp, eq12=eq12, eq22=eq22, mul=mul, mul2=mul2, chang=chang, eq=eq, eq2=eq2, eq3=eq3, eq4=eq4, eq5=eq5, eq6=eq6, eq7=eq7,
                             eq8=eq8, eq9=eq9, x=x, y=y, temp2=temp2, temp3=temp3, temp4=temp4, answ=answ)

    return stem, answer, comment

#중2-1-2-154
def expressions212_Stem_130():
    stem = "\n두 수 중 큰 수를 작은 수로 나누면 몫이 $$수식$${div}$$/수식$$이고\n" \
           "나머지가 $$수식$${left}$$/수식$${temp}다. 작은 수에 $$수식$${ad}$$/수식$${temp2} 더한 수를 큰\n" \
           "수로 나누면 몫이 {div2}이고 나머지가 {left2}{temp3}다. 이때 두\n" \
           "수의 차는?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "큰 수를 x, 작은 수를 y라 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 두 수는 $$수식$${x}$$/수식$$, $$수식$${y}$$/수식$$이므로 두 수의 차는\n" \
              "$$수식$${x}$$/수식$$ - $$수식$${y}$$/수식$$ = $$수식$${answ}$$/수식$$"

    num1 = np.random.randint(2, 40)
    num2 = np.random.randint(2, 20)
    ad = np.random.randint(2, 40)
    num3 = num2+ad
    div = int(num1/num2)
    div2 = int(num3/num1)
    left = num1%num2
    left2 = num3%num1
    while num1<=num2 or num3<=num1 or left==0 or left2==0 or div<=1 or div2<=1:
        num1 = np.random.randint(2, 40)
        num2 = np.random.randint(2, 20)
        ad = np.random.randint(2, 40)
        num3 = num2 + ad
        div = int(num1 / num2)
        div2 = int(num3 / num1)
        left = num1 % num2
        left2 = num3 % num1
    temp = proc_jo(left, 3)
    temp2 = proc_jo(ad, 4)
    temp3 = proc_jo(left2, 3)
    aa1 = "x = " + str(div) +"y + " + str(left)
    aa2 = "y + " + str(ad) + " = " + str(div2)+"x + " + str(left)
    answ = num1-num2
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(eq=eq, temp=temp, temp2=temp2, temp3=temp3, div=div, div2=div2, left=left, left2=left2, ad=ad, x1=x1,
                       x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, eq=eq, x=num1, y=num2)
    return stem, answer, comment

#중2-1-2-155
def expressions212_Stem_131():
    stem = "\n두 자리의 자연수가 있다. 일의 자리 숫자의 $$수식$${mul}$$/수식$$배\n" \
           "는 십의 자리 숫자의 $$수식$${mul2}$$/수식$$배보다 $$수식$${left}$$/수식$$만큼 작고, 십의\n" \
           "자리 숫자와 일의 자리 숫자를 바꾼 수는 처음 수\n" \
           "보다 $$수식$${les}$$/수식$$만큼 작다고 한다. 처음 수는?"\
           "\n① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "처음 수의 십의 자리 숫자를 x,\n" \
              "일의 자리 숫자를 y라 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 처음 수는 $$수식$${answ}$$/수식$$이다."

    mul = np.random.randint(2, 4)
    x = np.random.randint(1, 10)
    mul2 = np.random.randint(2, 5)
    left = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    while (y*mul)!=(mul2*x-left) or y>=x:
        mul = np.random.randint(2, 4)
        x = np.random.randint(1, 10)
        mul2 = np.random.randint(2, 5)
        left = np.random.randint(1, 10)
        y = np.random.randint(1, 10)
    answ = 10*x+y
    les = answ - (10*y+x)
    aa1 = str(mul)+"y = "
    if mul==1:
        aa1 = "y = "
    if mul2==1:
        aa1 = aa1 +"x - " + str(left)
    else:
        aa1 = aa1 + str(mul2) +"x - " + str(left)
    aa2 = "10y + x = (10x +y) - " + str(les)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(mul=mul, mul2=mul2, left=left, les=les, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, eq=eq, x=x, y=y)

    return stem, answer, comment

#중2-1-2-157
def expressions212_Stem_132():
    stem = "\n한 개에 $$수식$${price1}$$/수식$$ 원 하는 {item}{temp} 한 개에 $$수식$${price2}$$/수식$$ 원 하는\n" \
           "{item2}{temp2} 합하여 $$수식$${total}$$/수식$$ 개를 사고 $$수식$${tprice}$$/수식$$ 원을 지불하였\n" \
           "다. 이때 {item2}{temp2} {item}보다 몇 개 더 샀는가?"\
           "\n① $$수식$${x1} 개\n② {x2} 개\n③ {x3} 개\n④ {x4} 개\n⑤ {x5} 개\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "{item}{temp3} x개, {item2}{temp2} y개 샀다고 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 {item2}{temp2} $$수식$${answ}$$/수식$$ 개 더 샀다."

    items = ["오렌지", "키위", "바나나","사과","배", "복숭아","포도","참외", "수박"]
    t = np.random.randint(0, 9)
    item1 =  items[t]
    t1 = np.random.randint(0, 9)
    item2 =  items[t1]
    temp = proc_jo(item1, 2)
    temp2 = proc_jo(item2,4)
    temp3 = proc_jo(item1,4)

    while t==t1:
        t1 = np.random.randint(0, 9)
        item2 = items[t1]
    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    while y<=x:
        x = np.random.randint(1, 10)
        y = np.random.randint(1, 10)
    total = x+y
    answ = y-x
    price1 = np.random.randint(1, 10)*100
    price2 = np.random.randint(1, 10)*100
    while price1==price2:
        price2 = np.random.randint(1, 10) * 100
    tprice = x*price1+y*price2
    aa1 = "x + y = " + str(total)
    aa2 = str(price1)+"x + " + str(price2) +"y = " + str(tprice)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(item=item1, temp=temp, temp2=temp2, item2=item2, price1=price1, price2=price2, tprice=tprice,
                       total=total, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(item=item1, item2=item2, temp2=temp2, temp3=temp3, answ=answ, eq=eq, x=x, y=y)

    return stem, answer, comment

#중2-1-2-158
def expressions212_Stem_133():
    stem = "\n{item1} $$수식$${num1}$$/수식$$ 개와 {item2} $$수식$${num2}$$/수식$$ 개의 값을 합하면 $$수식$${tprice1}$$/수식$$ 원\n" \
           "이고, {item1} $$수식$${num11}$$/수식$$ 개와 {item2} $$수식$${num22}$$/수식$$ 개의 값을 합하면\n" \
           "$$수식$${tprice2}$$/수식$$ 원이다. 이때 {item2} 1개의 값은?"\
           "\n① $$수식$${x1} 원\n② {x2} 원\n③ {x3} 원\n④ {x4} 원\n⑤ {x5} 원\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "{item1} 1개의 값을 x원\n" \
              "{item2} 1개의 값을 y원이라 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 {item2} 1개의 값은 $$수식$${y}$$/수식$$"
    items = ["초콜릿","과자","음료수","아이스크림","요거트"]
    t = np.random.randint(0, 5)
    item1 = items[t]
    t1 = np.random.randint(0, 5)
    item2 = items[t1]

    while t == t1:
        t1 = np.random.randint(0, 5)
        item2 = items[t1]
    x = np.random.randint(1, 10)*100
    y = np.random.randint(1, 10)*100
    while x==y:
        x = np.random.randint(1, 10) * 100
        y = np.random.randint(1, 10) * 100
    answ = y
    num1 = np.random.randint(1, 10)
    num2 = np.random.randint(1, 10)
    num11 = np.random.randint(1, 10)
    num22 = np.random.randint(1, 10)
    while num1==num2 or num1==num11 or num2 == num22 or num11==num22:
        num1 = np.random.randint(1, 10)
        num2 = np.random.randint(1, 10)
        num11 = np.random.randint(1, 10)
        num22 = np.random.randint(1, 10)
    tprice1 = num1*x+num2*y
    tprice2 = num11*x+num22*y
    aa1 = str(num1)+"x + "
    if num1==1:
        aa1 = "x + "
    if num2==1:
        aa1 = aa1 + "y = " + str(tprice1)
    else:
        aa1 = aa1 + str(num2) +"y = " + str(tprice1)

    aa2 = str(num11) + "x + "
    if num11 == 1:
        aa2 = "x + "
    if num22 == 1:
        aa2 = aa2+ "y = " + str(tprice2)
    else:
        aa2 = aa2 + str(num22) + "y = " + str(tprice2)

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)*100
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k!=0:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"

    stem = stem.format(item1=item1,item2=item2, tprice1=tprice1, tprice2=tprice2,num1=num1, num2=num2, num11=num11, num22=num22, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(item1=item1, item2=item2,  answ=answ, eq=eq, x=x, y=y)

    return stem, answer, comment

#중2-1-2-159
def expressions212_Stem_134():
    stem = "\nA 농구 선수가 한 경기에서 $$수식$${shoot}$$/수식$$ 개의 슛을 성공하\n" \
           "고 $$수식$${score}$$/수식$$ 득점을 하였다. 이 농구 선수가 성공한 {chose}점\n" \
           "슛은 몇 개인가?"\
           "\n① $$수식$${x1} 개\n② {x2} 개\n③ {x3} 개\n④ {x4} 개\n⑤ {x5} 개\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "2점 슛을 x개, 3점 슛을 y개 성공했다고 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 성공한 {chose}점 슛은 $$수식$${answ}$$/수식$$ 개이다."

    shoot = np.random.randint(10, 30)
    x = np.random.randint(1, 15)
    y = np.random.randint(1, 15)
    shoot = x+y
    score = 2*x+3*y
    aa1 = "x + y = " + str(shoot)
    aa2 = "2x + 3y = " + str(score)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"

    chose1 = np.random.randint(2, 4)
    answ = 0
    chose=""
    if chose1 == 2:
        answ = x
        chose = str(2)
    else:
        answ = y
        chose = str(3)
    while True:
        shoot = np.random.randint(10, 30)
        x = np.random.randint(1, 15)
        y = np.random.randint(1, 15)
        shoot = x + y
        score = 2 * x + 3 * y
        aa1 = "x + y = " + str(shoot)
        aa2 = "2x + 3y = " + str(score)
        eq = "{cases{" + aa1 + "#" + aa2 + "}}"

        chose1 = np.random.randint(2, 4)
        answ = 0
        chose = ""
        if chose1 == 2:
            answ = x
            chose = str(2)
        else:
            answ = y
            chose = str(3)
        kkk = 0
        bb = []
        while len(bb) < 4:
            k = np.random.randint(1, 10)
            u = np.random.randint(0, 2)
            if u == 1:
                k = answ + k
            else:
                k = abs(answ - k)
            if k not in bb and k != answ and k!=0 and k<shoot:
                bb.append(k)
            kkk+=1
            if kkk>1000:
                break
        if len(bb)>=4:
            break
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    stem = stem.format(shoot=shoot, score=score, chose=chose, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(chose=chose, answ=answ, eq=eq, x=x, y=y)

    return stem, answer, comment

#중2-1-2-160
def expressions212_Stem_135():
    stem = "\n지금으로부터 $$수식$${yr}$$/수식$$년 전에는 할아버지의 나이가 손자\n" \
           "의 나이의 $$수식$${mul}$$/수식$$배였고, 지금으로부터 $$수식$${futur}$$/수식$$년 후에는 할\n" \
           "아버지의 나이가 손자의 나이의 $$수식$${mul2}$$/수식$$배보다 $$수식$${ad}$$/수식$$살이\n" \
           "많다고 한다. 현재 {person}의 나이는?"\
           "\n① $$수식$${x1} 살\n② {x2} 살\n③ {x3} 살\n④ {x4} 살\n⑤ {x5} 살\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "현재 할아버지의 나이를 x살, 손자의 나이를 y살\n" \
              "이라 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 {person}의 나이는 $$수식$${answ}$$/수식$$ 살이다." \

    x = np.random.randint(70, 100)
    y = np.random.randint(10, 30)
    yr = np.random.randint(1, 6)
    mul = np.random.randint(2, 7)
    futur = np.random.randint(1, 6)
    mul2 = np.random.randint(2, 7)
    ad = np.random.randint(1, 5)
    while x>100 or x<60 or (x+futur)!=((y+futur)*mul2+ad):
        y = np.random.randint(15, 25)
        yr = np.random.randint(2, 6)
        mul = np.random.randint(3, 7)
        x = ((y-yr)*mul)+yr
        futur = np.random.randint(2, 8)
        mul2 = np.random.randint(2, 5)
        ad = np.random.randint(1, 5)
    aa1 = "x - " + str(yr) + " = " + str(mul) +"(y - " + str(yr) +")"
    aa2 = "x + " + str(futur) +" = " + str(mul2) +"(y + " + str(futur)+") + " + str(ad)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"

    p = np.random.randint(0, 2)
    answ = x
    person = "할아버지"
    if p==1:
        answ = y
        person = "손자"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(person=person, futur=futur, yr=yr, ad=ad, mul=mul, mul2=mul2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(person=person, answ=answ, eq=eq, x=x, y=y)

    return stem, answer, comment

#중2-1-2-161
def expressions212_Stem_136():
    stem = "\n학생 수가 $$수식$${pop}$$/수식$$ 명인 어느 학급에서 남학생의 $$수식$${boy}$$/수식$${temp}\n" \
           "여학생의 $$수식$${girl}$$/수식$${temp2} {sport}{temp3} 좋아한다고 한다. {sport}{temp3}\n" \
           "좋아하는 학생이 전체 학생의  $$수식$${fra}$$/수식$$일 때, 이 학급의\n" \
           "{gender} 수는?"\
           "\n① $$수식$${x1} 명\n② {x2} 명\n③ {x3} 명\n④ {x4} 명\n⑤ {x5} 명\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "남학생 수를 x명, 여학생 수를 y명이라 하면\n" \
              "$$수식$${eq}$$/수식$$          ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 이 학급의 {gender} 수는 $$수식$${answ}$$/수식$$"

    sports = ["야구","축구","농구","하키","수영"]

    sport = sports[np.random.randint(0, 5)]
    temp3 = proc_jo(sport, 4)
    booy = np.random.randint(2, 8)
    boyy = np.random.randint(2, 9)
    while booy>=boyy:
        booy = np.random.randint(2, 8)
        boyy = np.random.randint(2, 9)

    girrl = np.random.randint(2, 10)
    x = np.random.randint(10, 20)
    y = np.random.randint(10, 20)
    while x%boyy!=0 or y%girrl!=0:
        booy = np.random.randint(2, 8)
        boyy = np.random.randint(2, 9)
        while booy >= boyy:
            booy = np.random.randint(2, 8)
            boyy = np.random.randint(2, 9)
        girrl = np.random.randint(2, 10)
        x = np.random.randint(10, 30)
        y = np.random.randint(10, 30)
    booy = int(booy / gcd(booy, boyy))
    boyy = int(boyy / gcd(booy, boyy))
    boy = "{" + str(booy) + "} over {" + str(boyy) + "}"
    temp = proc_jo(boyy, 2)
    girl = "1 over {" + str(girrl) + "}"
    temp2 = proc_jo(girrl,0)
    pop = x+y
    ppp = (x*(booy/boyy))+(y/girrl)
    top = int(ppp/gcd(ppp,pop))
    bot = int(pop/gcd(ppp,pop))
    fra = "{" + str(top) + "} over {" + str(bot) + "}"
    if bot==1:
        fra = top
    aa1 = "x + y = " + str(pop)
    aa2 = boy +"x + " + girl +"y = " + fra +"TIMES" + str(pop)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"

    lcm1 = lcm(boyy,girrl)
    topboy = int(lcm1/boyy)*booy
    gerrl = int(lcm1/girrl)
    boot = int(pop/bot)*top*lcm1
    vv2 = str(topboy) +"x + "

    if topboy==1:
        vv2 = "x + "
    if gerrl ==1:
        vv2 = vv2 +"y = " + str(boot)
    else:
        vv2 = vv2 +str(gerrl) + "y = " + str(boot)
    vv = "{cases{" + aa1 + "#" + vv2 + "}}"
    gender = "여학생"
    answ = y
    oo = np.random.randint(0, 2)
    if oo==1:
        gender = "남학생"
        answ = x
    xx = int(x/(booy/boyy))
    yy = int(y/girrl)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(temp3=temp3, sport =sport, pop=pop, boy=boy, girl=girl, temp=temp, temp2=temp2, gender=gender, fra=fra, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(x=x, y=y, gender=gender, answ=answ,  eq=eq, vv=vv)

    return stem, answer, comment

#중2-1-2-162
def expressions212_Stem_137():
    stem = "\n둘레의 길이가 $$수식$${pop}$$/수식$$ cm인 직사각형이 있다. 이 직\n" \
           "사각형의 가로의 길이를 $$수식$${mul}$$/수식$$배로 늘이고, 세로의 길\n" \
           "이를 $$수식$${ad}$$/수식$$cm 늘였더니 둘레의 길이가 $$수식$${new}$$/수식$$ cm가 되었\n" \
           "다. 처음 직사각형의 {side}의 길이는?"\
           "\n① $$수식$${x1} cm\n② {x2} cm\n③ {x3} cm\n④ {x4} cm\n⑤ {x5} cm\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "처음 직사각형의 가로의 길이를 x cm,\n" \
              "세로의 길이를 y cm라 하면\n" \
              "$$수식$${eq}$$/수식$$                     ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 직사각형의 {side}의 길이는 $$수식$${answ}$$/수식$$ cm이\n" \
              "다."

    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    while x==y:
        y = np.random.randint(1, 10)

    pop = (x+y)*2
    mul = np.random.randint(2, 5)
    ad = np.random.randint(2, 7)
    new = (mul*x+(y+ad))*2
    aa1 = "2(x + y) = " + str(pop)
    aa2 = "2(" + str(mul)+"x + (y + " + str(ad)+")) = " + str(new)
    vv1 = "x + y = " + str(int(pop/2))
    vv2 = str(mul)+"x + y = " + str(int(new/2)-ad)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + vv1 + "#" + vv2 + "}}"

    side = "세로"
    answ = y
    oo = np.random.randint(0, 2)
    if oo == 1:
        side = "가로"
        answ = x

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(side=side, pop=pop, mul=mul, new=new, ad=ad, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(x=x, y=y, side=side, answ=answ, eq=eq, vv=vv)

    return stem, answer, comment

#중2-1-2-163
def expressions212_Stem_138():
    stem = "\n{name}가 참가한 퀴즈 프로그램에서는 한 문제를\n" \
           "맞히면 $$수식$${succ}$$/수식$$ 점을 얻고, 틀리면 $$수식$${penal}$$/수식$$ 점을 잃는다고\n" \
           "한다. {name}가 틀린 문제 수는 맞힌 문제 수의\n" \
           "$$수식$${fra}$$/수식$$배이고, {name}가 얻은 점수는 $$수식$${score}$$/수식$$ 점일 때, {name}\n" \
           "가 푼 총 문제 수는?"\
           "\n① $$수식$${x1} 개\n② {x2} 개\n③ {x3} 개\n④ {x4} 개\n⑤ {x5} 개\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "{name}가 맞힌 문제 수를 x, 틀린 문제 수를 y라\n" \
              "하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 {name}가 푼 총 문제 수는 $$수식$${x}$$/수식$$ + $$수식$${y}$$/수식$$ = $$수식$${answ}$$/수식$$ (개)"

    xx = np.random.randint(2, 6)
    y = np.random.randint(2, 10)
    x = xx*y
    succ = np.random.randint(2, 15)*10
    penal = np.random.randint(2, 10)*10
    score = x*succ-y*penal
    while succ<=penal or score<=0:
        xx = np.random.randint(2, 6)
        y = np.random.randint(2, 10)
        x = xx * y
        succ = np.random.randint(2, 15) * 10
        penal = np.random.randint(2, 10) * 10
        score = x * succ - y * penal

    fra = "1 over {"+str(xx)+"}"
    nameList = ["경희", "민철이", "수진이", "철수", "영대", "미영이", "은혜","세현"]
    o = np.random.randint(0, 8)
    name = nameList[o]
    aa1 = "y = " + fra +"x"
    aa2 = str(succ)+"x - " + str(penal)+"y = " + str(score)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    bb = []
    answ = x+y
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(succ=succ, penal=penal, name=name, fra=fra, score=score, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(x=x, y=y, eq=eq, answ=answ, name=name)

    return stem, answer, comment

#중2-1-2-166
def expressions212_Stem_139():
    stem = "\nA, B 두 제품을 합하여 $$수식$${price}$$/수식$$ 원에 사서 A 제품\n" \
           "은 원가의 $$수식$${per}$$/수식$$ %, B 제품은 원가의 $$수식$${per2}$$/수식$$ %이 이익을\n" \
           "붙여서 판매하였더니 $$수식$${prof}$$/수식$$ 원의 이익을 얻었다. {ee}\n" \
           "제품의 원가는?"\
           "\n① $$수식$${x1} 원\n② {x2} 원\n③ {x3} 원\n④ {x4} 원\n⑤ {x5} 원\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "A 제품의 원가를 x원, B 제품의 원가를 y원이라\n" \
              "고 하면\n" \
              "$$수식$${eq}$$/수식$$           ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 {ee} 제품의 원가는 $$수식$${answ}$$/수식$$ 원이다."

    x = np.random.randint(10, 20)*1000
    y = np.random.randint(10, 20)*1000
    while x==y:
        y = np.random.randint(10, 20) * 1000
    price = x+y
    aa1 = "x + y = " +str(price)
    per = np.random.randint(5, 20)
    per2 = np.random.randint(5, 20)
    while per==per2:
        per2 = np.random.randint(5, 20)
    prof = int(x*(per/100))+int(y*(per2/100))
    aa2 = "{"+str(per)+"} over 100 x + {"+str(per2)+"} over 100 y = " + str(prof)
    gcd1 = gcd(gcd(per, per2), prof*100)
    s1 = int(per/gcd1)
    s2 = int(per2/gcd1)
    s3 = int((prof*100)/gcd1)
    vv2 = str(s1) +"x + "
    if s1==1:
        vv2 = "x + "
    if s2==1:
        vv2 = vv2 + "y = " + str(s3)
    else:
        vv2 = vv2 +str(s2) +"y = " + str(s3)
    ee = "B"
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + aa1 + "#" + vv2 + "}}"

    answ = y
    oo = np.random.randint(0, 2)
    if oo == 1:
        ee = "A"
        answ = x

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)*1000
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(ee=ee, price=price, per=per, per2=per2, prof=prof, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(x=x, y=y, eq=eq, vv=vv,  answ=answ, ee=ee)

    return stem, answer, comment

#중2-1-2-168
def expressions212_Stem_140():
    stem = "\n{name}는 삼촌 댁에 다녀오는데 갈 때는 시속\n" \
           "$$수식$${speed}$$/수식$$ km로 달리는 버스를 탔고, 올 때는 시속\n" \
           "$$수식$${speed2}$$/수식$$ km로 달리는 기차를 탔더니 총 $$수식$${hr}$$/수식$$시간이 걸\n" \
           "렸다. 기차를 타고 온 거리가 버스를 타고 간 거\n" \
           "리보다 $$수식$${more}$$/수식$$ km 더 멀다고 할 때, {ee}를 타고 {ee1}\n" \
           "거리는? (단, 삼촌 댁에 머무른 시간은 무시한다.)"\
           "\n① $$수식$${x1} km\n② {x2} km\n③ {x3} km\n④ {x4} km\n⑤ {x5} km\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "버스를 타고 간 거리를 x km,\n" \
              "기차를 타고 온 거리를 y km라 하면\n" \
              "$$수식$${eq}$$/수식$$             ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 {ee}를 타고 {ee1} 거리는 $$수식$${answ}$$/수식$$ km이다."

    nameList = ["성호","경희", "민철이", "수진이", "철수", "영대", "미영이", "은혜"]
    o = np.random.randint(0, 8)
    name = nameList[o]
    speed = np.random.randint(5, 12)*10
    speed2 = np.random.randint(5, 12)*10
    while speed>=speed2:
        speed = np.random.randint(5, 12) * 10
        speed2 = np.random.randint(5, 12) * 10
    t = np.random.randint(1, 4)
    x = speed*t
    t1 = np.random.randint(1, 4)
    y = speed2*t1
    while x>=y:
        t = np.random.randint(1, 4)
        x = speed * t
        t1 = np.random.randint(1, 4)
        y = speed2 * t1
    ad = y-x
    hr = t+t1
    aa1 = "y = x + " + str(ad)
    aa2 = "x over {"+str(speed)+"} + y over {"+str(speed2)+"} = " + str(hr)
    lcm1 = lcm(speed, speed2)
    s1 = int(lcm1/speed)
    s2 = int(lcm1/speed2)
    s3 = hr*lcm1
    vv1 = str(s1) +"x + "
    if s1==1:
        vv1 = "x + "
    if s2==1:
        vv1 = vv1 +"y = " + str(s3)
    else:
        vv1 = vv1 + str(s2) +"y = " + str(s3)
    ee = "기차"
    ee1 = "온"
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + vv1 + "#" + aa1 + "}}"

    answ = y
    oo = np.random.randint(0, 2)
    if oo == 1:
        ee = "버스"
        ee1 ="간"
        answ = x

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10) * 10
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(name=name, ee=ee, ee1=ee1,speed=speed, speed2=speed2, more=ad, hr=hr, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(name=name,x=x, y=y, eq=eq, vv=vv, answ=answ, ee=ee, ee1=ee1)

    return stem, answer, comment

#중2-1-2-169
def expressions212_Stem_141():
    stem = "\n$$수식$${per}$$/수식$$ %의 {liquid}{temp2} $$수식$${per2}$$/수식$$ %의 {liquid}{temp} 섞은 후 물을\n" \
           "더 넣어 $$수식$${per3}$$/수식$$ %의 {liquid} $$수식$${weight}$$/수식$$ g을 만들었다. 이때\n" \
           "$$수식$${per}$$/수식$$ %의 {liquid}{temp2} 더 넣은 물의 양의 비가 {ratio}이\n" \
           "었다면 더 넣은 물의 양은?"\
           "\n① $$수식$${x1} g\n② {x2} g\n③ {x3} g\n④ {x4} g\n⑤ {x5} g\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${per}$$/수식$$ %의 {liquid}의 양을 x g, $$수식$${per2}$$/수식$$ %의 {liquid}의 양을\n" \
              "y g이라 하면\n" \
              "더 넣은 물의 양은 $$수식$${fra}$$/수식$$x g이므로\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 더 넣은 물의 양은 $$수식$${eq2}$$/수식$$ = $$수식$${answ}$$/수식$$ (g)"

    liquids = ["설탕물", "소금물", "화학물"]
    r = np.random.randint(0, 3)
    liquid = liquids[r]
    temp = proc_jo(liquid, 4)
    temp2 = proc_jo(liquid, 2)

    per = np.random.randint(1, 10)
    per2 =  np.random.randint(1, 10)
    x = 5 * np.random.randint(5, 30)
    y = 5 * np.random.randint(5, 30)
    rati = np.random.randint(1, 6)
    rati2 = np.random.randint(1, 6)
    weight = int((rati2/rati+1)*x)+y
    per3 = int((x*per+y*per2)/weight)
    while x%rati!=0 or rati>=rati2 or (x*(per/100))%1!=0 or (y*(per2/100))%1!=0 or (x*per+y*per2)%weight!=0:
        per = np.random.randint(2, 10)
        per2 =  np.random.randint(2, 10)
        while per>=per2:
            per = np.random.randint(2, 10)
            per2 = np.random.randint(2, 10)
        x = 5*np.random.randint(6, 20)
        y = 5*np.random.randint(1, 7)+x
        rati = np.random.randint(1, 6)
        rati2 = np.random.randint(2, 6)
        weight = int((rati2 / rati + 1) * x) + y
        per3 = int((x * per + y * per2) / weight)

    rati = int(rati/gcd(rati, rati2))
    rati2 = int(rati2/gcd(rati, rati2))
    fra = "{"+str(rati2)+"} over {"+str(rati)+"}"
    if rati==1:
        fra = str(rati2)
    ratio = str(rati) +" : " + str(rati2)
    weight = int((rati2/rati+1)*x)+y
    per3 = int((x*per+y*per2)/weight)
    eq2 = fra +" TIMES " + str(x)
    aa1 = "x + y + " + fra +"x = " + str(weight)
    aa2 = "{"+str(per)+"} over 100 TIMES x + {"+str(per2)+"} over 100 TIMES y = {"+str(per3)+"} over 100 TIMES " + str(weight)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    answ = int(x*(rati2/rati))
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(temp=temp, temp2=temp2, liquid=liquid, per=per, per2=per2, per3=per3, weight=weight, ratio=ratio, x1=x1, x2=x2, x3=x3,
                       x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(fra=fra, eq2=eq2, per2=per2, per=per, liquid=liquid, x=x, y=y, eq=eq, answ=answ, )

    return stem, answer, comment

#중2-1-2-170
def expressions212_Stem_142():
    stem = "\n두 자연수가 있다. 큰 수에서 작은 수의 $$수식$${mul}$$/수식$$배를 빼\n" \
           "면 $$수식$${num1}$$/수식$${temp}고, 큰 수를 작은 수로 나누면 몫이 $$수식$${div}$$/수식$$, 나\n" \
           "머지가 $$수식$${lef}$$/수식$${temp2}다. 두 수 중 큰 수는?"\
           "\n① $$수식$${x1} \n② {x2} \n③ {x3} \n④ {x4} \n⑤ {x5} \n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "큰 수를 x, 작은 수를 y라고 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 두 수 중 큰 수는 $$수식$${answ}$$/수식$${temp3}다."

    y = np.random.randint(5, 20)
    lef =  np.random.randint(1, 6)
    while lef>=y:
        lef = np.random.randint(1, 6)
    div = np.random.randint(3, 15)
    x = div*y+lef
    mul = np.random.randint(2, div)
    while (x-mul*y)<=0:
        y = np.random.randint(5, 20)
        lef = np.random.randint(1, 6)
        while lef >= y:
            lef = np.random.randint(1, 6)
        div = np.random.randint(3, 15)
        x = div * y + lef
        mul = np.random.randint(2, div)
    num1 = (x-mul*y)
    aa1 = "x - " + str(mul)+"y = " + str(num1)
    aa2 = "x = " + str(div)+"y + " + str(lef)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    temp = proc_jo(num1, 3)
    temp2 = proc_jo(lef, 3)
    temp3 = proc_jo(x, 3)

    answ = x
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k != 0:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(mul=mul, div=div, lef=lef, num1=num1, temp=temp, temp2=temp2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, y=y, x=x, eq=eq, temp3=temp3)

    return stem, answer, comment

#중2-1-2-171
def expressions212_Stem_143():
    stem = "\n두 자리의 자연수가 있다. 이 수는 각 자리의 숫\n" \
           "자의 합의 $$수식$${mul}$$/수식$$배이고, 십의 자리 숫자와 일의 자리\n" \
           "숫자를 바꾼 수는 처음 수보다 $$수식$${dif}$$/수식$${temp} 크다고 한다.\n" \
           "이때 처음 수의 각 자리의 숫자의 합은?"\
           "\n① $$수식$${x1} \n② {x2} \n③ {x3} \n④ {x4} \n⑤ {x5} \n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "처음 수의 십의 자리 숫자를 x, 일의 자리 숫자를\n" \
              "y라고 하면\n" \
              "$$수식$${eq}$$/수식$$                         ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "연립ㄹ방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 처음 수는 $$수식$${num}$$/수식$$이므로 각 자리의 숫자의 합\n" \
              "은\n" \
              "$$수식$${x}$$/수식$$ + $$수식$${y}$$/수식$$ = $$수식$${answ}$$/수식$$"

    mul = np.random.randint(2, 6)
    x = np.random.randint(1, 9)
    y = np.random.randint(2, 9)
    while x>=y or (10*x+y)!=mul*(x+y):
        mul = np.random.randint(2, 6)
        x = np.random.randint(1, 9)
        y = np.random.randint(2, 9)
    dif = (10*y+x) -(10*x+y)
    a = 10-mul
    b = mul-1
    aaa = int(a/gcd(a,b))
    b = int(b/gcd(a,b))
    aa1 = "10x + y = " + str(mul) +"(x + y)"
    aa2 = "10y + x = (10x + y) + " + str(dif)
    vv1 = str(b) +"y = "
    if b==1:
        vv1 = "y = "
    if aaa==1:
        vv1 = vv1 +"x"
    else:
        vv1= vv1 +str(aaa) +"x"
    dd = int(dif/gcd(dif,9))
    ddd = int(9/gcd(dif,9))
    vv2 = str(ddd)+"x - " + str(ddd) +"y = "
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    if ddd==1:
        vv2 = "x - y = "
    vv2 = vv2 + str(-1*dd)
    vv = "{cases{" + vv1 + "#" + vv2 + "}}"
    num = 10*x+y
    answ = x+y
    temp = proc_jo(dif, 0)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k>2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(mul=mul, dif=dif, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, answ=answ, vv=vv, y=y, x=x, eq=eq)

    return stem, answer, comment

#중2-1-2-172
def expressions212_Stem_144():
    stem = "\n$$수식$${score}$$/수식$$ 점 이상을 얻어야 합격하는 자격증 시험에 응시\n" \
           "한 $$수식$${pop}$$/수식$$명 중 합격자는 $$수식$${ss}$$/수식$$명이다. 이때 합격한 사람\n" \
           "의 평균 점수는 불합격한 사람의 평균 점수의 $$수식$${mul}$$/수식$$배\n" \
           "보다 $$수식$${lef}$$/수식$$점이 낮고, 불합격한 사람의 평균 점수는\n" \
           "응시자 전체의 평균 점수보다 $$수식$${faa}$$/수식$$점이 낮을 때, 응\n" \
           "시자 전체의 평균 점수는?"\
           "\n① $$수식$${x1} 점\n② {x2} 점\n③ {x3} 점\n④ {x4} 점\n⑤ {x5} 점\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "합격자의 평균 점수를 x점, 불합격자의 평균 점수\n" \
              "를 y점이라 하면 응시자 전체의 평균 점수는\n" \
              "$$수식$${fra1}$$/수식$$   점, 즉 $$수식$${fra2}$$/수식$$  점이므로\n" \
              "$$수식$${eq}$$/수식$$          ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 응시자 전체의 평균 점수는\n" \
              "$$수식$${fra3}$$/수식$$   = $$수식$${answ}$$/수식$$  (점)"

    score = np.random.randint(65, 85)
    x = np.random.randint(score, 100)
    y =  np.random.randint(50, score)
    pop = np.random.randint(2, 6)
    ss = np.random.randint(1, pop)*10
    pop = pop*10
    lef = np.random.randint(10, 40)
    while int((x+lef)/y)<=1 or (ss*x+(pop-ss)*y)%pop!=0:
        score = np.random.randint(65, 85)
        x = np.random.randint(score, 100)
        y = np.random.randint(50, score)
        pop = np.random.randint(2, 6)
        ss = np.random.randint(1, pop) * 10
        pop = pop * 10
        lef = np.random.randint(10, 40)
    mul = int((x+lef)/y)
    aa1 = "x = " + str(mul) +"y - " + str(lef)
    gcd1 = gcd(gcd(pop,ss),(pop-ss))
    fra1 = "{" + str(ss) +"x + " + str(pop-ss) +"y} over {"+str(pop)+"}"
    a = int(pop/gcd1)
    b = int(ss/gcd1)
    c = int((pop-ss)/gcd1)
    faa = int((x-y)/a)
    fra2 = "{"+str(b)+"x + "
    if b==1:
        fra2 = "{x + "
    if c==1:
        fra2 = fra2 + "y} over {"+str(a)+"}"
    else:
        fra2 = fra2 + str(c)+"y} over {"+str(a)+"}"
    aa2 = "y = " + fra2 + " - " + str(faa)
    vv2 = "x - y = " + str(faa*a)
    fra3 = "{" + str(b*x) + " + " + str(c*y) + "} over {" + str(a) + "}"
    answ = int((ss*x+(pop-ss)*y)/pop)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + aa1 + "#" + vv2 + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(score=score, ss=ss, pop=pop, lef=lef, mul=mul, faa=faa, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(fra1=fra1, fra2=fra2, fra3=fra3, vv=vv, eq=eq, answ=answ, x=x, y=y)

    return stem, answer, comment

#중2-1-2-173
def expressions212_Stem_145():
    stem = "\n{country1}{temp} {country2}에 국제전화를 걸면 분당 통화요금이\n" \
           "각각 $$수식$${cost1}$$/수식$$ 원, $$수식$${cost2}$$/수식$$ 원이라고 한다. {name}가 {country1}{temp} {country2}\n" \
           "에 국제전화를 건 시간을 합하면 $$수식$${hr}$$/수식$$시간이고, {country1}\n" \
           "에 건 국제전화 요금이 {country2}에 건 국제전화 요금\n" \
           "에 $$수식$${mul}$$/수식$$배일 때, 국제전화 요금은 모두 얼마인가?"\
           "\n① $$수식$${x1} 원\n② {x2} 원\n③ {x3} 원\n④ {x4} 원\n⑤ {x5} 원\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "{country1}에 전화 건 시간을 x분, {country2}에 전화 건 시간\n" \
              "을 y분이라 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 국제전화 요금은\n" \
              "{eq2} = $$수식$${answ}$$/수식$$ (원)"

    countries =["미국","일본","한국","캐나다","프랑스","중국","이집트"]
    o = np.random.randint(0, 7)
    o1 = np.random.randint(0, 7)
    while o ==o1:
        o1 = np.random.randint(0, 7)
    country1 = countries[o]
    country2 = countries[o1]
    temp = proc_jo(country1, 2)
    nameList = ["경희", "민철이", "수진이", "철수","영대","미영이","은혜"]
    o = np.random.randint(0, 7)
    name = nameList[o]
    cost1 = np.random.randint(1, 9)*10
    cost2 = np.random.randint(1, 9)*10
    if cost1>cost2:
        h = cost2
        cost2 = cost1
        cost1 = h
    hr = np.random.randint(1, 4)
    x = np.random.randint(0, hr*60)
    y = hr*60 - x
    mul = np.random.randint(2, 5)
    while cost1==cost2 or (cost1*x)!=mul*(cost2*y):
        cost1 = np.random.randint(1, 9) * 10
        cost2 = np.random.randint(1, 9) * 10
        if cost1 > cost2:
            h = cost2
            cost2 = cost1
            cost1 = h
        hr = np.random.randint(1, 4)
        x = np.random.randint(0, hr * 60)
        y = hr * 60 - x
        mul = np.random.randint(2, 5)

    aa1 ="x + y = " + str(hr*60)
    aa2 = str(cost1)+"x = " + str(mul) +" TIMES " + str(cost2) +"y"
    eq2 = str(cost1) +"x + " + str(cost2) +"y = " + str(cost1) +" $$수식$$TIMES$$/수식$$ " + str(x) + " + " + str(cost2) +" $$수식$$TIMES$$/수식$$ " +str(y)
    answ = cost1*x +cost2*y

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)*100
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    stem = stem.format(name=name, cost1=cost1, temp=temp, cost2=cost2, country1=country1, country2=country2, mul=mul, hr=hr, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, eq=eq, y=y, x=x, eq2=eq2, country1=country1, country2=country2)

    return stem, answer, comment

#중2-1-2-174
def expressions212_Stem_146():
    stem = "\n{flow} $$수식$${num1}$$/수식$$송이와 {flow2} $$수식$${num2}$$/수식$$송이의 가격은 $$수식$${price}$$/수식$$ 원이고,\n" \
           "{flow2} 한 송이의 가격은 {flow} 한 송이의 가격보다\n" \
           "$$수식$${dif}$$/수식$$ 원 비싸다고 한다. {flow} $$수식$${num11}$$/수식$$송이와 {flow2} $$수식$${num22}$$/수식$$송이\n" \
           "의 가격은?"\
           "\n① $$수식$${x1} 원\n② {x2} 원\n③ {x3} 원\n④ {x4} 원\n⑤ {x5} 원\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "{flow} 한 송이의 가격을 x원, {flow2} 한 송이의 가격\n" \
              "을 y원이라고 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 {flow} $$수식$${num11}$$/수식$$송이와 {flow2} $$수식$${num22}$$/수식$$송이의 가격은\n" \
              "{eq2} = $$수식$${answ}$$/수식$$ (원)"

    flows = ["튤립","장미","백합","코스모스","해바라기"]
    o = np.random.randint(0, 5)
    o1 = np.random.randint(0, 5)
    while o == o1:
        o1 = np.random.randint(0, 5)
    flow = flows[o]
    flow2 = flows[o1]
    x = np.random.randint(7, 15)*100
    y = np.random.randint(7, 15)*100
    while x>=y:
        x = np.random.randint(7, 15) * 100
        y = np.random.randint(7, 15) * 100
    dif = y-x
    num1 = np.random.randint(1, 10)
    num2 = np.random.randint(1, 10)
    num11 = np.random.randint(1, 10)
    num22 = np.random.randint(1, 10)
    while num1==num11 or num2==num22 or num1==num2:
        num1 = np.random.randint(1, 10)
        num2 = np.random.randint(1, 10)
        num11 = np.random.randint(1, 10)
        num22 = np.random.randint(1, 10)
    price =  x*num1+y*num2
    answ = x*num11+y*num22
    aa1 = str(num1) +"x + "
    if num1==1:
        aa1 = "x + "
    if num2==1:
        aa1 = aa1 + "y = " + str(price)
    else:
        aa1 = aa1 + str(num2) +"y = " + str(price)
    aa2 =  "y = x + " + str(dif)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    eq2 = str(num11) +" $$수식$$TIMES$$/수식$$ " + str(x) +" + " + str(num22) +" $$수식$$TIMES$$/수식$$ " + str(y)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10) * 100
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(flow=flow, flow2=flow2, num1=num1, num2=num2, num11=num11, num22=num22,dif=dif, price=price, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, eq=eq, y=y, x=x, eq2=eq2, flow=flow, flow2=flow2, num11=num11, num22=num22)

    return stem, answer, comment

#중2-1-2-175
def expressions212_Stem_147():
    stem = "\n어떤 캠핑 동호회 회원들이 캠핑을 가서 텐트를\n" \
           "설치하였다. 각 텐트에 $$수식$${num1}$$/수식$$명씩 들어가면 하나의 텐\n" \
           "트에는 $$수식$${each}$$/수식$$명이 들어가게 되고, 빈 텐트가 $$수식$${lef}$$/수식$$개 생긴\n" \
           "다. 또 각 텐트에 $$수식$${num2}$$/수식$$명씩 들어가면 {ee} 명은 텐트에\n" \
           "들어갈 수 없다. 캠핑에 참가한 회원은 몇 명인\n" \
           "가?"\
           "\n① $$수식$${x1} 명\n② {x2} 명\n③ {x3} 명\n④ {x4} 명\n⑤ {x5} 명\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "텐트가 x개, 회원이 y명이라 하면\n" \
              "$$수식$${eq}$$/수식$$                  ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 캠핑에 참가한 회원은 $$수식$${answ}$$/수식$$명이다."

    eee = ["한","두","세","네","다섯"]
    e1 = np.random.randint(0, 5)
    ee = eee[e1]
    x = np.random.randint(4, 15)
    num2 = np.random.randint(2, 6)
    y = num2*x+1+e1
    num1 = np.random.randint(2, 6)
    each =  np.random.randint(1, 6)
    lef = np.random.randint(1, 4)
    while num1==num2:
        num1 = np.random.randint(2, 6)
    while each>=num1 or lef>=num1 or (e1+1)>=num2 or x%each==0 or y!=(num1*(x-(1+lef))+each) or (-(num1*(1+lef))+each)==0:
        e1 = np.random.randint(0, 5)
        ee = eee[e1]
        x = np.random.randint(4, 15)
        num2 = np.random.randint(2, 6)
        y = num2 * x + 1 + e1
        num1 = np.random.randint(2, 6)
        each = np.random.randint(1, 6)
        lef = np.random.randint(1, 4)
        while num1 == num2:
            num1 = np.random.randint(2, 6)
    aa1 = "y = " + str(num1) +"(x - " + str((1+lef)) +") + "+ str(each)
    aa2 = str(num2)+"x + " + str(1+e1)
    vv1 = "y = " + str(num1)+"x "
    if (-(num1*(1+lef))+each)>0:
        vv1 = vv1 +" + " + str(-(num1*(1+lef))+each)
    else:
        vv1 = vv1 +" - " + str(abs(-(num1*(1+lef))+each))

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + vv1 + "#" + aa2 + "}}"
    answ = y
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(num1=num1, lef=lef, each=each, num2=num2, ee=ee, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, eq=eq, y=y, x=x, vv=vv)

    return stem, answer, comment

#중2-1-2-176
def expressions212_Stem_148():
    stem = "\n현재 이모의 나이는 {name}의 나이의 $$수식$${mul}$$/수식$$배이고, $$수식$${yr}$$/수식$$\n" \
           "년 전에는 이모의 나이가 {name}의 나이의 $$수식$${mul2}$$/수식$$배였\n" \
           "다고 한다. 현재 이모와 {name}의 나이의 합은?"\
           "\n① $$수식$${x1} 살\n② {x2} 살\n③ {x3} 살\n④ {x4} 살\n⑤ {x5} 살\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "현재 이모의 나이를 x살, {name}의 나이를 y살이\n" \
              "라고 하면\n" \
              "$$수식$${eq}$$/수식$$               ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 현재 이모와 {name}의 나이의 합은\n" \
              "$$수식$${x}$$/수식$$ + $$수식$${y}$$/수식$$ = $$수식$${answ}$$/수식$$ (살)"

    nameList = ["경희", "민철이", "수진이", "철수", "영대", "미영이", "은혜","준혁"]
    o = np.random.randint(0, 8)
    name = nameList[o]
    mul = np.random.randint(2, 10)
    mul2 = np.random.randint(2, 10)
    while mul==mul2:
        mul2 = np.random.randint(2, 10)
    yr = np.random.randint(1, 14)
    y = np.random.randint(10, 25)
    x =  y*mul
    while x>80 or (x-yr)!=mul2*(y-yr):
        mul = np.random.randint(2, 10)
        mul2 = np.random.randint(2, 10)
        while mul == mul2:
            mul2 = np.random.randint(2, 10)
        yr = np.random.randint(1, 14)
        y = np.random.randint(10, 25)
        x = y * mul

    aa1 = "x = " + str(mul) +"y"
    aa2 = "x - " + str(yr) + " = " + str(mul2) +"(y - " + str(yr) +")"
    vv2 = "x - " + str(mul2) +"y = " + str(-(yr*mul2)+yr)
    answ = x+y

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + aa1 + "#" + vv2 + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    stem = stem.format(mul=mul, mul2=mul2, name=name, yr=yr, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(name=name, answ=answ, eq=eq, y=y, x=x, vv=vv)

    return stem, answer, comment

#중2-1-2-177
def expressions212_Stem_149():
    stem = "\n$$수식$${price}$$/수식$$ 원짜리 물건을 사기 위해 {name1}가 가지고\n" \
           "있는 돈의 $$수식$${fra}$$/수식$${temp} 냈고, {name2}가 가지고 있는 돈의\n" \
           "$$수식$${fra2}$$/수식$${temp2} 냈다. {name1}와 {name2}의 남은 돈을 비교하였\n" \
           "더니 {name1}가 $$수식$${dif}$$/수식$$ 원이 많았다고 할 때, {name2}가\n" \
           "처음에 가지고 있었던 금액은 얼마인가?"\
           "\n① $$수식$${x1} 원\n② {x2} 원\n③ {x3} 원\n④ {x4} 원\n⑤ {x5} 원\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "{name1}가 처음 가지고 있던 금액을 x원, {name2}가\n" \
              "처음 가지고 있던 금액을 y원이라 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "즉, $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 {name2}가 처음 가지고 있던 금액은 $$수식$${y}$$/수식$$ 원\n" \
              "이다."

    nameList = ["경희", "민철이", "수진이", "철수","영대","미영이","은혜"]
    o = np.random.randint(0, 7)
    o1 = np.random.randint(0,7)
    while o == o1:
        o1 = np.random.randint(0, 7)
    name1 = nameList[o]
    name2 = nameList[o1]
    x = np.random.randint(5, 20)*1000
    y = np.random.randint(5, 20)*1000
    a = np.random.randint(2, 5)
    b = np.random.randint(2,5)
    while x%a!=0 or y%b!=0 or (x*(1-(1/a)))<=(y*(1-(1/b))) or a==b or x==y:
        x = np.random.randint(5, 20) * 1000
        y = np.random.randint(5, 20) * 1000
        a = np.random.randint(2, 5)
        b = np.random.randint(2, 5)
    price = int(x/a) + int(y/b)
    temp = proc_jo(a, 4)
    temp2 = proc_jo(b, 4)
    fra = "1 over {"+str(a)+"}"
    fra2 = "1 over {" + str(b) + "}"
    aa1 = fra+" x + " + fra2 +" y = " + str(price)
    dif = int(x*(1-(1/a))) - int(y*(1-(1/b)))
    aa2 = "(1 - "+fra +")x - (1 - "+fra2 +")y = " + str(dif)
    lcm1 = lcm(a,b)
    vv1 = str(int(lcm1/a)) +"x + "
    if int(lcm1/a)==1:
        vv1 = "x + "
    if int(lcm1/b)==1:
        vv1 = vv1 + "y = " + str(price*lcm1)
    else:
        vv1 = vv1 + str(int(lcm1/b)) +"y = " + str(price*lcm1)
    vv2 = str(int(lcm1/a)*(a-1)) +"x + "
    if int(lcm1/a)*(a-1)==1:
        vv2 = "x + "
    if int(lcm1/b)*(b-1)==1:
        vv2 = vv2 +"y = "+ str(dif*lcm1)
    else:
        vv2 = vv2 +  str(int(lcm1/b)*(b-1)) +"y = " + str(dif*lcm1)
    answ = y

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + vv1 + "#" + vv2 + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)*1000
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    stem = stem.format(temp=temp, temp2=temp2, name1=name1, name2=name2, fra=fra, fra2=fra2, dif=dif, price=price, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(name1=name1,name2=name2, answ=answ, eq=eq, y=y, x=x, vv=vv)

    return stem, answer, comment

#중2-1-2-178
def expressions212_Stem_150():
    stem = "\n둘레의 길이가 $$수식$${gir}$$/수식$$ cm인 직사각형이 있다. 이 직\n" \
           "사각형의 가로의 길이는 세로의 길이의 $$수식$${mul}$$/수식$$배보다\n" \
           "$$수식$${lef}$$/수식$$ cm가 짧다고 한다. 이 직사각형의 넓이는?"\
           "\n① $$수식$${x1} $$수식$$rm cm ^2$$/수식$$\n② {x2} $$수식$$rm cm ^2$$/수식$$\n③ {x3} $$수식$$rm cm ^2$$/수식$$\n④ {x4} $$수식$$rm cm ^2$$/수식$$\n⑤ {x5} $$수식$$rm cm ^2$$/수식$$\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "직사각형의 가로의 길이를 x cm, 세로의 길이를\n" \
              "y cm라 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 직사각형의 넓이는 $$수식$${x} TIMES {y} = {answ} (rm cm ^2 )  $$/수식$$"

    y = np.random.randint(2, 10)
    mul = np.random.randint(2, 6)
    lef = np.random.randint(1, 5)
    x = y*mul-lef
    while x==y:
        y = np.random.randint(5, 30)
    gir = 2*(x+y)
    aa1 = "2(x + y) = " + str(gir)
    aa2 = "x = " + str(mul) +"y - " + str(lef)
    answ = x*y

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(gir=gir, mul=mul, lef=lef, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, x=x, y=y, answ=answ)

    return stem, answer, comment

#중2-1-2-179
def expressions212_Stem_151():
    stem = "\nA, B 두 팀이 {sport} 경기를 하였다. 전반전에 A\n" \
           "팀은 B팀보다 $$수식$${poi}$$/수식$$점을 더 얻었고, 후반전에 A팀은\n" \
           "B팀이 후반전에 얻은 점수의 $$수식$${fra}$$/수식$${temp} 얻어 {score}\n" \
           "로 B팀이 이겼다. B 팀이 후반전에 얻은 점수는?"\
           "\n① $$수식$${x1} 점\n② {x2} 점\n③ {x3} 점\n④ {x4} 점\n⑤ {x5} 점\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "B팀이 전반전에 얻은 점수를 x점, 후반전에 얻은\n" \
              "점수를 y점이라 하면\n" \
              "$$수식$${eq}$$/수식$$         ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 B 팀이내 후반전에 얻은 점수는 $$수식$${answ}$$/수식$$ 점이다."
    sports = ["야구", "축구", "농구", "하키", "배구"]

    sport = sports[np.random.randint(0, 5)]
    poi = np.random.randint(1, 10)
    x = np.random.randint(5, 20)
    y = np.random.randint(5, 20)
    low = np.random.randint(2, 20)
    while y%low!=0:
        low = np.random.randint(2, 20)
    high = np.random.randint(1, low)
    while (x+y)<=((x+poi)+int(high/low*y)):
        poi = np.random.randint(1, 10)
        x = np.random.randint(5, 20)
        y = np.random.randint(5, 20)
        low = np.random.randint(2, 20)
        while y % low != 0:
            low = np.random.randint(2, 20)
        high = np.random.randint(1, low)
    score = str(((x+poi)+int(high/low*y)))+" : " + str(x+y)
    aa1 ="x + y = " + str(x+y)
    low = int(low/gcd(low,high))
    high = int(high/gcd(low,high))
    p = ((x+poi)+int(high/low*y))
    aa2 = "(x + " + str(poi) +") + {"+str(high)+"} over {"+str(low)+"}y= " + str(p)
    vv2 = str(low) +"x + " + str(high) +"y = " + str(p*low-poi*low)
    if high==1:
        vv2 = str(low) +"x + y = " + str(p*low-poi*low)
    fra = "{"+str(high)+"} over {"+str(low)+"}"
    answ = y
    temp = proc_jo(low, 4)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + aa1 + "#" + vv2 + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(sport=sport, fra=fra, poi=poi, temp=temp, score=score, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(vv=vv, eq=eq, x=x, y=y, answ=answ)

    return stem, answer, comment

#중2-1-2-180
def expressions212_Stem_152():
    stem = "\nA, B 두 사람이 가위바위보를 하여 이긴 사람은\n" \
           "$$수식$${up}$$/수식$$계단씩 올라가고, 진 사람은 $$수식$${down}$$/수식$$계단씩 내려가기고\n" \
           "하였다. 게임이 끝난 후 처음 위치보다 A는 $$수식$${a}$$/수식$$\n" \
           "계단을, B는 $$수식$${b}$$/수식$$계단을 올라갔을 때, B가 이긴\n" \
           "횟수는?"\
           "\n① $$수식$${x1} 회\n② {x2} 회\n③ {x3} 회\n④ {x4} 회\n⑤ {x5} 회\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "B가 이긴 횟수를 x회, 진 횟수를 y회라 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 B가 이긴 횟수는 $$수식$${x}$$/수식$$회이다."


    up = np.random.randint(2, 6)
    down = np.random.randint(1, 5)
    while down>=up:
        up = np.random.randint(2, 6)
        down = np.random.randint(1, 5)
    x = np.random.randint(2, 10)
    y = np.random.randint(2, 10)
    while  up*x-down*y== up*y-down*x or up*x-down*y<=0 or up*y-down*x<=0:
        up = np.random.randint(2, 6)
        down = np.random.randint(1, 5)
        while down >= up:
            up = np.random.randint(2, 6)
            down = np.random.randint(1, 5)
        x = np.random.randint(2, 10)
        y = np.random.randint(2, 10)
    aa1 = str(up) +"y - " + str(down) +"x = " + str(up*y-down*x)
    aa2 = str(up) +"x - " + str(down) +"y = " + str(up*x-down*y)
    if down == 1:
        aa1 = str(up) + "y - x = " + str(up * y - down * x)
        aa2 = str(up) + "x - y = " + str(up * x - down * y)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    a = (up*y-down*x)
    b = (up*x-down*y)
    answ = x

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(down=down, up=up, a=a, b=b, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, x=x, y=y, answ=answ)

    return stem, answer, comment

#중2-1-2-181
def expressions212_Stem_153():
    stem = "\nA, B 두 제품을 생산하는 공장이 있다. 이 공장\n" \
           "의 지난달 생산량은 A, B 두 제품을 합하여 $$수식$${tota}$$/수식$$\n" \
           "개이고, 이번 달 생산량은 지난달에 비해 A 제품\n" \
           "은 $$수식$${per}$$/수식$$ % 증가하고, B 제품은 $$수식$${per2}$$/수식$$ % 감소하여 전체\n" \
           "적으로 지난달 생산량과 같았다. 이번 달 A 제품\n" \
           "의 생산량은?"\
           "\n① $$수식$${x1} 개\n② {x2} 개\n③ {x3} 개\n④ {x4} 개\n⑤ {x5} 개\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "지난달 A 제품의 생산량을 x개, B 제품의 생산량\n" \
              "을 y개라 하면\n" \
              "$$수식$${eq}$$/수식$$            ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 이번 달 A 제품의 생산량은\n" \
              "$$수식$${x}$$/수식$$ + $$수식$${x}$$/수식$$ $$수식$$TIMES$$/수식$$ $$수식$${fra}$$/수식$$   = $$수식$${answ}$$/수식$$ (개)"

    per = np.random.randint(1, 16)
    per2 = np.random.randint(1, 16)
    while per==per2:
        per2 = np.random.randint(1, 16)
    x = np.random.randint(20, 180) * 5
    y = np.random.randint(20, 180) * 5
    while (per/100*x)%1!=0 or (per2/100*y)%1!=0 or per*x!=per2*y or x==y:
        per = np.random.randint(1, 16)
        per2 = np.random.randint(1, 16)
        while per == per2:
            per2 = np.random.randint(1, 16)
        x = np.random.randint(20, 180) * 5
        y = np.random.randint(20, 180) * 5
    aa1 = "x + y = " + str(x+y)
    aa2 = "{"+str(per)+"} over 100 x - {"+str(per2)+"} over 100 y = 0"
    perr = int(per/gcd(per,per2))
    perr2 = int(per2/gcd(per,per2))
    vv2 = str(perr)+"x - "
    if perr==1:
        vv2 = "x - "
    if perr2==1:
        vv2 = vv2 + "y = 0"
    else:
        vv2 = vv2 + str(perr2) +"y = 0"
    fra = "{"+str(per)+"} over 100"
    answ = x + int(per/100*x)
    total = x+y
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + aa1 + "#" + vv2 + "}}"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(per=per, per2=per2, tota=total, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, fra=fra, vv=vv, x=x, y=y, answ=answ)

    return stem, answer, comment

#중2-1-2-182
def expressions212_Stem_154():
    stem = "\n어느 의류 매장에서 {item1}{temp} $$수식$${per}$$/수식$$ % 할인하고,\n" \
           "{item2}{temp2} $$수식$${per2}$$/수식$$ % 할인하여 판매하기로 하였다. 할인하\n" \
           "기 전 {item1}{temp3} {item2}의 판매 가격의 합은\n" \
           "$$수식$${total}$$/수식$$ 원이고, 할인한 후 {item1}{temp3} {item2}의 판매\n" \
           "가격의 합은 할인하기 전보다 $$수식$${total2}$$/수식$$ 원이 적을 때,\n" \
           "할인된 {itemee}의 판매 가격은?"\
           "\n① $$수식$${x1} 원\n② {x2} 원\n③ {x3} 원\n④ {x4} 원\n⑤ {x5} 원\n   $$/수식$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "할인하기 전 {item1}의 판매 가격을 x원, {item2}의\n" \
              "판매 가격을 y원이라 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "즉, $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 할인된 {itemee}의 판매 가격은\n" \
              "{eq2} = $$수식$${answ}$$/수식$$ (원)"

    itemList = ["운동화", "반바지", "자켓", "후드티", "청바지"]
    o = np.random.randint(0, 5)
    o1 = np.random.randint(0, 5)
    while o==o1:
        o1 = np.random.randint(0, 5)
    item1 = itemList[o]
    item2 = itemList[o1]
    temp =proc_jo(item1, -1)
    temp2 = proc_jo(item2, -1)
    temp3 = proc_jo(item1, 2)
    per = 5*np.random.randint(2, 8)
    per2 = 5*np.random.randint(2, 8)
    while per==per2:
        per2 = 5 * np.random.randint(2, 8)
    x = np.random.randint(10, 50)*1000
    y= np.random.randint(10, 50)*1000
    while x==y:
        y = np.random.randint(10, 50) * 1000
    total = x+y
    total2 = int(per/100*x) + int(per2/100*y)
    aa1 = "x + y = " + str(total)
    aa2 = "{"+str(per)+"} over 100 x - {"+str(per2)+"} over 100 y = " + str(total2)
    gcd1 = gcd(gcd(per, per2),total2*100)
    perr = int(per/gcd1)
    perr2 = int(per2/gcd1)
    cc = int(total2*100/gcd1)

    vv2 = str(perr) +"x + "
    if perr==1:
        vv2 = "x + "
    if perr2==1:
        vv2 = vv2 +"y = " + str(cc)
    else:
        vv2 = vv2 + str(perr2) +"y = " + str(cc)

    answ = x- int(per/100*x)
    itemee = item1
    eq2 = str(x) +" - " + str(x) + " $$수식$$TIMES$$/수식$$ " + "$$수식$${"+str(per)+"} over 100$$/수식$$"
    g = np.random.randint(0,2)
    if g==1:
        answ = y-int(per2/100*y)
        itemee = item2
        eq2 = str(y) +" - " + str(y) + " $$수식$$TIMES$$/수식$$ " + "$$수식$${"+str(per2)+"} over 100$$/수식$$"

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + aa1 + "#" + vv2 + "}}"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)*1000
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(temp=temp, temp2=temp2, temp3=temp3, item1=item1, item2=item2, itemee=itemee, per=per, per2=per2, total=total, total2=total2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(itemee=itemee, item1=item1, item2=item2, eq=eq, eq2=eq2, vv=vv, x=x, y=y, answ=answ)

    return stem, answer, comment

#중2-1-2-183
def expressions212_Stem_155():
    stem = "\n어떤 물탱크에 물이 가득 차 있다. 이 물탱크의\n" \
           "물을 A 호스로 $$수식$${hr}$$/수식$$시간 동안 뺀 후 B 호스로 $$수식$${hr2}$$/수식$$시간\n" \
           "동안 빼거나 A 호스로 $$수식$${hr11}$$/수식$$시간 동안 뺀 후 B 호스\n" \
           "로 $$수식$${hr22}$$/수식$$시간 동안 빼면 모두 뺄 수 있다. B 호스만으\n" \
           "로 물을 모두 빼는데 몇 시간이 걸리는가?"\
           "\n① $$수식$${x1} 시간\n② {x2} 시간\n③ {x3} 시간\n④ {x4} 시간\n⑤ {x5} 시간\n   $$/수식$$"
    answer = "\n(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "물탱크에 물이 가득 차 있을 때의 물의 양을 1로\n" \
              "놓고, A, B 호스로 1시간 동안 뺄 수 있는 물의\n" \
              "양을 각각 x, y라 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 B 호스만으로 물을 모두 빼는 데는 $$수식$${answ}$$/수식$$시간\n" \
              "이 걸린다."


    xx = np.random.randint(2, 13)
    yy =  np.random.randint(2, 13)
    while xx==yy:
        yy = np.random.randint(2, 13)
    hr = np.random.randint(1, 7)
    hr2 = np.random.randint(1, 7)
    hr11 = np.random.randint(1, 7)
    hr22 = np.random.randint(1, 7)
    while hr == hr11 or hr == hr2 or hr2 == hr22:
        hr = np.random.randint(1, 7)
        hr2 = np.random.randint(1, 7)
        hr11 = np.random.randint(1, 7)
        hr22 = np.random.randint(1, 7)
    while (hr*(1/xx) +hr2*(1/yy))!=1 or (hr11*(1/xx) +hr22*(1/yy))!=1:
        xx = np.random.randint(2, 13)
        yy = np.random.randint(2, 13)
        while xx == yy:
            yy = np.random.randint(2, 13)
        hr = np.random.randint(1, 7)
        hr2 = np.random.randint(1, 7)
        hr11 = np.random.randint(1, 7)
        hr22 = np.random.randint(1, 7)
        while hr==hr11 or hr==hr2 or hr2==hr22:
            hr = np.random.randint(1, 7)
            hr2 = np.random.randint(1, 7)
            hr11 = np.random.randint(1, 7)
            hr22 = np.random.randint(1, 7)
    aa1 = str(hr)+"x + "
    if hr==1:
        aa1 = "x + "
    if hr2==1:
        aa1 = aa1 +"y = 1"
    else:
        aa1 = aa1 + str(hr2) +"y = 1"
    aa2 = str(hr11)+"x + "
    if hr11 == 1:
        aa2 = "x + "
    if hr22 == 1:
        aa2 = aa2 + "y = 1"
    else:
        aa2 = aa2 + str(hr22) +"y = 1"
    answ = yy
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    x = "1 over {" + str(xx) + "}"
    y = "1 over {" + str(yy) + "}"
    stem = stem.format(hr=hr, hr2=hr2, hr22=hr22, hr11=hr11, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, x=x, y=y, answ=answ)

    return stem, answer, comment

#중2-1-2-184
def expressions212_Stem_156():
    stem = "\n{name}는 주말에 운동을 하기 위해 할아버지 댁에서\n" \
           "집으로 오는 데 처음에는 시속 $$수식$${speed}$$/수식$$ km로 달리다가\n" \
           "도중에 시속 $$수식$${speeed2}$$/수식$$ km로 걸었다. 총 $$수식$${dis}$$/수식$$ km의 거리를\n" \
           "$$수식$${hr}$$/수식$$시간 {min} 걸렸다고 할 때, 달려간 거리는?"\
           "\n① $$수식$${x1} km\n② {x2} km\n③ {x3} km\n④ {x4} km\n⑤ {x5} km\n   $$/수식$$"
    answer = "\n(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "달려간 거리를 x km, 걸어간 거리를 y km라 하\n" \
              "면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 달려간 거리는 $$수식$${x}$$/수식$$ km이다."

    nameList = ["경희", "민철이", "수진이", "철수","영대","미영이","은혜","준호"]
    o = np.random.randint(0, 8)
    name = nameList[o]
    speed = np.random.randint(3, 8)
    speed2 = np.random.randint(2, 5)
    while speed2>=speed:
        speed = np.random.randint(3, 8)
        speed2 = np.random.randint(2, 5)
    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    dis=x+y
    while ((x/speed+y/speed2)*60)%1!=0 or x+5>=dis:
        speed = np.random.randint(3, 8)
        speed2 = np.random.randint(2, 5)
        while speed2 >= speed:
            speed = np.random.randint(3, 8)
            speed2 = np.random.randint(2, 5)
        x = np.random.randint(1, 10)
        y = np.random.randint(1, 10)
        dis=x+y
    hr = int(x/speed+y/speed2)
    min = int((x/speed+y/speed2-hr)*60)
    if min==0:
        min = ""
    else:
        min = str(min) +"분"
    top = x*speed2+y*speed
    bottom = speed2*speed
    gcd1 = gcd(top,bottom)
    top = int(top/gcd1)
    bottom = int(bottom/gcd1)
    dis = x+y
    aa1 = "x + y = " + str(dis)
    aa2 = "x over {"+str(speed)+"} + y over {"+str(speed2)+"} = {"+str(top)+"} over {"+str(bottom)+"}"
    answ = x

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k < dis:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(dis=dis, name=name, hr=hr, min=min, speed=speed, speeed2=speed2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, x=x, y=y, answ=answ)

    return stem, answer, comment

#중2-1-2-185
def expressions212_Stem_157():
    stem = "\n$$수식$${dis}$$/수식$$ km 떨어진 두 지점에서 {name1}와 {name2}가 동시\n" \
           "에 마주 보고 출발하여 도중에 만났다. {name1}는 시\n" \
           "속 $$수식$${speed}$$/수식$$ km, {name2}는 시속 $$수식$${speed2}$$/수식$$ km로 달렸다고 할\n" \
           "때, 두 사람이 만날 때까지 {ee}?"\
           "\n① $$수식$${x1} \n② {x2} \n③ {x3} \n④ {x4} \n⑤ {x5} \n   $$/수식$$"
    answer = "\n(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "{name1}가 달린 거리를 x km, {name2}가 달린 거리를\n" \
              "y km라 하면\n" \
              "$$수식$${eq}$$/수식$$        ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = {x}, y = {y}\n" \
              "따라서 두 사람이 만날 때까지 {ee}\n" \
              "{eq2}{answ}이다."

    nameList = ["경희", "민철이", "수진이", "철수", "영대", "미영이", "은혜"]
    o = np.random.randint(0, 7)
    o1 = np.random.randint(0, 7)
    while o == o1:
        o1 = np.random.randint(0, 7)
    name1 = nameList[o]
    name2 = nameList[o1]
    x = np.random.randint(5, 15)
    y = np.random.randint(5, 15)
    while x==y:
        y = np.random.randint(5, 15)
    speed = np.random.randint(10, 25)
    speed2 = np.random.randint(10, 25)
    while speed==speed2:
        speed2 = np.random.randint(10, 25)
    while (x/speed)!=(y/speed2) or (x/speed*60)%1!=0:
        x = np.random.randint(5, 15)
        y = np.random.randint(5, 15)
        while x == y:
            y = np.random.randint(5, 15)
        speed = np.random.randint(10, 25)
        speed2 = np.random.randint(10, 25)
        while speed == speed2:
            speed2 = np.random.randint(10, 25)
    dis = x+y
    aa1 = "x + y = " + str(dis)
    aa2 = "x over {"+str(speed)+"} = y over {"+str(speed2)+"}"
    lcm1 = lcm(speed, speed2)
    a1 = int(lcm1/speed)
    a2 = int(lcm1/speed2)
    vv2 = str(a1) +"x - "
    if a1==1:
        vv2 = "x - "
    if a2==1:
        vv2 = vv2 +"y = 0"
    else:
        vv2 = vv2 + str(a2) +"y = 0"
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + aa1 + "#" + vv2 + "}}"
    rr = np.random.randint(0, 3)
    eq2=""
    ee = name1 + "가 걸은 거리는"
    answ1 = x
    answ = str(x) +" km"
    bb = []
    dd=[]
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ1 + k
        else:
            k = abs(answ1 - k)
        if k not in dd and k != answ1 and k > 2:
            dd.append(k)
            bb.append(str(k) + " km")
    if rr==1:
        ee = name2 + "가 걸은 거리는"
        answ1 = y
        answ = str(y) + " km"
        bb = []
        dd=[]
        while len(bb) < 4:
            k = np.random.randint(1, 10)
            u = np.random.randint(0, 2)
            if u == 1:
                k = answ1 + k
            else:
                k = abs(answ1 - k)
            if k not in dd and k != answ1:
                dd.append(k)
                bb.append(str(k) + " km")
    elif rr==2:
        eq2 = "$$수식$${"+str(x)+"} over {"+str(speed)+"}$$/수식$$ = " + str(round(x/speed,2)) +"(시간), 즉 "
        hr = int(x/speed)
        min = int((x/speed-hr)*60)
        answ = str(hr)+"시간 "+str(min) +"분"
        if hr==0:
            answ =str(min) +"분"
        elif min==0:
            answ = str(hr)+"시간 "
        bb=[]
        dd=[]
        while len(bb) < 4:
            k = np.random.randint(1, 6)*10
            u = np.random.randint(1, 3)
            yy = str(u)+"시간 "+str(k) +"분"
            if [k,u] not in dd and (k!=min or u!=hr):
                dd.append([k,u])
                bb.append(yy)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(name1=name1, name2=name2, ee=ee, dis=dis, speed=speed, speed2=speed2, x1=x1, x2=x2, x3=x3, x4=x4,
                       x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(name1=name1, name2=name2,eq=eq, x=x, y=y, vv=vv, eq2=eq2, ee=ee, answ=answ)

    return stem, answer, comment

#중2-1-2-188
def expressions212_Stem_158():
    stem = "\nx %의 {frui} 과즙 $$수식$${we}$$/수식$$ g과 y %의 {frui} 과즙\n" \
           "$$수식$${we2}$$/수식$$ g을 섞으면 $$수식$${result}$$/수식$$ %의 {frui} 과즙이 되고, x %의\n" \
           "{frui} 과즙 $$수식$${we11}$$/수식$$ g과 y%의 {frui} 과즙 $$수식$${we22}$$/수식$$ g을 섞\n" \
           "으면 $$수식$${result2}$$/수식$$ %의 {frui} 과즙이 된다. 이때 x + y의 값\n" \
           "은?"\
           "\n① $$수식$${x1} \n② {x2} \n③ {x3} \n④ {x4} \n⑤ {x5} \n   $$/수식$$"
    answer = "\n(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "즉, $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "∴ x + y = $$수식$${answ}$$/수식$$"
    fruits = ["사과","복숭아","망고","오렌지","포도"]
    frui = fruits[np.random.randint(0,5)]
    x = np.random.randint(1, 20)
    y =  np.random.randint(1, 20)
    while x==y:
        y = np.random.randint(1, 20)
    we = np.random.randint(1, 10)*100
    we2 = np.random.randint(1, 10)*100
    we11 = np.random.randint(1, 10)*100
    we22 = np.random.randint(1, 10)*100

    while we==we11 or we22==we2 or we==we2 or we11==we22:
        we = np.random.randint(1, 10) * 100
        we2 = np.random.randint(1, 10) * 100
        we11 = np.random.randint(1, 10) * 100
        we22 = np.random.randint(1, 10) * 100
    while (x*we+y*we2)%(we+we2)!=0 or (x*we11+y*we22)%(we11+we22)!=0:
        x = np.random.randint(1, 20)
        y = np.random.randint(1, 20)
        while x == y:
            y = np.random.randint(1, 20)
        we = np.random.randint(1, 10) * 100
        we2 = np.random.randint(1, 10) * 100
        we11 = np.random.randint(1, 10) * 100
        we22 = np.random.randint(1, 10) * 100

        while we == we11 or we22 == we2 or we == we2 or we11 == we22:
            we = np.random.randint(1, 10) * 100
            we2 = np.random.randint(1, 10) * 100
            we11 = np.random.randint(1, 10) * 100
            we22 = np.random.randint(1, 10) * 100
    result = int((x * int(we / 100) + y * int(we2 / 100))/((we+we2)/100))
    result2 = int((x * int(we11 / 100) + y * int(we22 / 100))/((we11+we22)/100))
    answ = x+y
    aa1 = "x over 100 TIMES " + str(we) + " + y over 100 TIMES " + str(we2) + " = {" + str(result) +"} over 100 TIMES " + str(we+we2)
    aa2 = "x over 100 TIMES " + str(we11) + " + y over 100 TIMES " + str(we22) + " = {" + str(result2) +"} over 100 TIMES " + str(we11+we22)
    vv1 = str(int(we/100))+"x + "
    if int(we/100)==1:
        vv1 = "x + "
    if int(we2/100)==1:
        vv1 = vv1 + "y = " + str(result*int((we+we2)/100))
    else:
        vv1 = vv1 + str(int(we2/100)) + "y = " + str(result*int((we+we2)/100))
    vv2 = str(int(we11 / 100)) + "x + "
    if int(we11 / 100) == 1:
        vv2 = "x + "
    if int(we22 / 100) == 1:
        vv2 = vv2 + "y = " + str(result2 * int((we11 + we22) / 100))
    else:
        vv2 = vv2 + str(int(we22 / 100)) + "y = " + str(result2 * int((we11 + we22) / 100))

    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + vv1 + "#" + vv2 + "}}"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(frui=frui, we=we, we11=we11, we2=we2, we22=we22, result=result, result2=result2, x1=x1, x2=x2, x3=x3, x4=x4,
                       x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, x=x, y=y, vv=vv, eq=eq)

    return stem, answer, comment

#중2-1-2-189
# ㉠, ㉡ 에러
def expressions212_Stem_159():
    stem = "\nA, B 두 사람이 가진 돈을 모두 모아보니 $$수식$${mone}$$/수식$$\n" \
           "원이었다. 그런데 A는 자신의 돈의 $$수식$${per}$$/수식$$ %를 얻고, B는\n" \
           "자신이 가지고 있는 돈의 $$수식$${per2}$$/수식$$ %를 쓰고 보니 $$수식$${inc}$$/수식$$원이 늘었다. 처음 A가\n" \
           "가진 돈은?"\
           "\n① $$수식$${x1} 원\n② {x2} 원\n③ {x3} 원\n④ {x4} 원\n⑤ {x5} 원\n   $$/수식$$"
    answer = "\n(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "처음 A가 가진 돈을 X, B가 가진 돈을 Y라 하\n" \
              "면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "㉡에서 {eq2},\n" \
              "{eq3}$$수식$$cdots cdots$$/수식$$ ㉡\n" \
              "㉠+㉡하면 {eq4}\n" \
              "∴ X = $$수식$${x}$$/수식$$ (원)"

    per2 = np.random.randint(2, 7)
    per = per2*np.random.randint(2, 5)
    x = np.random.randint(500, 1000)
    y = np.random.randint(500, 1000)
    while (x*per/100)%1!=0 or (y*per2/100)%1!=0 or (x*per/100)<=(y*per2/100):
        per2 = np.random.randint(2, 7)
        per = per2 * np.random.randint(2, 5)
        x = np.random.randint(500, 1000)
        y = np.random.randint(500, 1000)
    inc = int(x*per/100) - int(y*per2/100)
    mone = x+y
    aa1 = "X + Y = " + str(mone)
    aa2 = str(per/100) +"X - " + str(per2/100) +"Y = " + str(inc)
    eq2 = str(per) +"X - " +str(per2) +"Y = " + str(inc*100)
    gcd1 = gcd(per, per2)
    aaa = int(per/gcd1)
    aaaa = int(per2/gcd1)
    aaaaa = int(inc*100/gcd1)
    eq3 = str(aaa) +"X - " + str(aaaa) +"Y = " + str(aaaaa)
    if aaaa==1:
        eq3 = str(aaa) + "X - Y = " + str(aaaaa)
    eq4 = str(aaa+1) +"X = " + str(aaaaa+mone)
    answ = x
    eq = problm(aa1, aa2)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)*10
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]


    stem = stem.format(per=per, per2=per2, inc=inc, mone=mone, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, x=x, y=y, eq2=eq2, eq3=eq3, eq4=eq4, eq=eq)

    return stem, answer, comment

#중2-1-2-190
def expressions212_Stem_160():
    stem = "\n{name}가 $$수식$${price}$$/수식$$ 원짜리 {item}{temp} $$수식$${price2}$$/수식$$ 원짜리 {item}{temp2} 몇\n" \
           "개 사고 $$수식$${total}$$/수식$$ 원을 내려고 했더니 계산된 금액은\n" \
           "$$수식$${real}$$/수식$$ 원이었다. $$수식$${total}$$/수식$$ 원은 {name}가 두 {item}의 가격\n" \
           "을 서로 바꿔서 잘못 계산한 것이었다. {name}는\n" \
           "$$수식$${price11}$$/수식$$ 원짜리 과자를 몇 개 샀는가?"\
           "\n① $$수식$${x1} 개\n② {x2} 개\n③ {x3} 개\n④ {x4} 개\n⑤ {x5} 개\n   $$/수식$$"
    answer = "\n(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "$$수식$${price}$$/수식$$ 원짜리 {item}{temp2} x개, $$수식$${price2}$$/수식$$ 원짜리 {item}{temp2} y개\n" \
              "샀다고 하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 $$수식$${price11}$$/수식$$ 원짜리 {item}{temp2} $$수식$${answ}$$/수식$$개 샀다."

    nameList = ["경희", "민철이", "수진이", "철수", "영대", "수현이", "준형이","성주"]
    o = np.random.randint(0, 8)
    name = nameList[o]
    items =["과자","초콜렛","아이스크림","음료수"]
    item = items[np.random.randint(0, 4)]
    price = np.random.randint(1, 10)*100
    price2 =np.random.randint(1, 10)*100
    while price==price2:
        price2 = np.random.randint(1, 10)*100

    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    total = price2*x+price*y
    real = price*x+price2*y
    aa1 = str(price) +"x + " + str(price2) +"y = " + str(real)
    aa2 = str(price2) +"x + " + str(price) +"y = " + str(total)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    answ = x
    price11 = price
    o = np.random.randint(0, 2)
    if o==1:
        answ = y
        price11 = price2
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    temp = proc_jo(item,2)
    temp2 = proc_jo(item, 4)
    stem = stem.format(temp=temp, temp2=temp2, price=price, price2=price2, total=total, real=real, price11=price11, name=name, item=item, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp2=temp2, eq=eq, price=price, price2=price2, item=item, x=x,y=y, price11=price11, answ=answ)

    return stem, answer, comment

#중2-1-2-192
def expressions212_Stem_161():
    stem = "\nA, B 두 호스로 물통에 물을 넣는데 두 호스를\n" \
           "모두 사용하여 $$수식$${min1}$$/수식$$분 동안 물을 넣은 후 A 호스만\n" \
           "으로 $$수식$${min2}$$/수식$$분 동안 넣었더니 물통이 가득 찼다. 또 같\n" \
           "은 크기의 물통에 두 호스를 모두 사용하여 $$수식$${min3}$$/수식$$분\n" \
           "동안 물을 넣은 후 B 호스만으로 $$수식$${min4}$$/수식$$분 동안 넣었더\n" \
           "니 물통이 가득 찼다. 이때 처음부터 {which} 호스만 사\n" \
           "용하여 물을 넣으면 몇 분 만에 물통이 가득 차겠\n" \
           "는가?"\
           "\n① $$수식$${x1} 분\n② {x2} 분\n③ {x3} 분\n④ {x4} 분\n⑤ {x5} 분\n   $$/수식$$"
    answer = "\n(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "물통에 물을 가득 채웠을 때의 물의 양을 1로 놓\n" \
              "고, A, B 호스로 1분 동안 넣는 물의 양을 각각\n" \
              "x, y라 하면\n" \
              "$$수식$${eq}$$/수식$$                  ,즉 $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 처음부터 {which} 호스만 사용하여 물을 넣으면\n" \
              "$$수식$${answ}$$/수식$$분 만에 물통이 가득 찬다."

    min1 = np.random.randint(2, 10)
    min2 = np.random.randint(2, 10)
    min3 = np.random.randint(2, 10)
    min4 = np.random.randint(2, 10)

    while min1==min2 or min2==min3 or min3==min4 or min1==min3 or min1==min4 or min2==min4:
        min1 = np.random.randint(2, 10)
        min2 = np.random.randint(2, 10)
        min3 = np.random.randint(2, 10)
        min4 = np.random.randint(2, 10)
    xx = (min1 + min3 + min2)
    yy = (min3 + min4+ min1)
    while (min1*(1/xx+1/yy) + min2*1/xx)!=1 or (min3*(1/xx+1/yy) + min4*1/yy)!=1:
        min1 = np.random.randint(2, 10)
        min2 = np.random.randint(2, 10)
        min3 = np.random.randint(2, 10)
        min4 = np.random.randint(2, 10)
        while min1 == min2 or min2 == min3 or min3 == min4 or min1 == min3 or min1 == min4 or min2 == min4:
            min1 = np.random.randint(2, 10)
            min2 = np.random.randint(2, 10)
            min3 = np.random.randint(2, 10)
            min4 = np.random.randint(2, 10)
        xx = (min1 + min3 + min2)
        yy = (min3 + min4 + min1)
    aa1 = str(min1) +"(x + y) + " + str(min2) +"x = 1"
    aa2 = str(min3) +"(x + y) + " + str(min4) +"y = 1"
    vv1 = str(min1+min2) +"x + " + str(min1) +"y = 1"
    vv2 = str(min3)+"x + " + str(min3+min4) +"y = 1"
    x = "1 over {"+str(xx)+"}"
    y = "1 over {"+str(yy)+"}"
    answ = xx
    print(min1+min3+min2)
    print(min3+min4+min1)
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + vv1 + "#" + vv2 + "}}"
    which = "A"
    o = np.random.randint(0, 2)
    if o==1:
        answ = yy
        which = "B"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]

    stem = stem.format(which=which, min1=min1, min2=min2, min3=min3, min4=min4, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(x=x, y=y, eq=eq, vv=vv, which=which,answ=answ)

    return stem, answer, comment

#중2-1-2-194
def expressions212_Stem_162():
    stem = "\n어느 학교의 올해의 학생 수는 작년에 비하여 남\n" \
           "학생은 $$수식$${per}$$/수식$$ % 늘고 여학생은 $$수식$${per2}$$/수식$$ % 줄어서, 전체\n" \
           "학생 수는 $$수식$${incr}$$/수식$$명이 늘어나 $$수식$${total}$$/수식$$ 명이 되었다고 한\n" \
           "다. 올해의 남학생 수와 여학생 수를 각각 구하시\n" \
           "오."
    answer = "\n(정답): \n" \
            "남자: $$수식$${newx}$$/수식$$ 명, 여자: $$수식$${newy}$$/수식$$ 명"
    comment = "(해설)\n" \
              "작년의 남학생 수와 여학생 수를 각각 x, y라 하면\n" \
              "x + y = $$수식$${prev}$$/수식$$ $$수식$$cdotscdots$$/수식$$㉠\n" \
              "올해의 학생 수는 남학생이 $$수식$${per}$$/수식$$ % 늘고 여학생은 \n" \
              "$$수식$${per2}$$/수식$$ % 줄어서, 전체 학생 수는 $$수식$${incr}$$/수식$$명이 늘어나\n" \
              "$$수식$${total}$$/수식$$이 되었으므로\n" \
              "{eq2} $$수식$$cdotscdots$$/수식$$㉡\n" \
              "{eq3}\n" \
              "{eq4} $$수식$$cdotscdots$$/수식$$㉡\n" \
              "㉠$$수식$$TIMES$$/수식$${mul}: {eq5} $$수식$$cdotscdots$$/수식$$㉠\n" \
              "㉡-㉠을 하면 {eq6} ∴ x = $$수식$${x}$$/수식$$\n" \
              "x = $$수식$${x}$$/수식$${temp} ㉠에 대입하면 y = $$수식$${y}$$/수식$$\n" \
              "따라서 올해의 남녀 학생 수는 남자는\n" \
              "{eq7} (명)이고, 여자는 {eq8}\n" \
              "(명)이다."

    per = np.random.randint(1, 20)
    per2 = np.random.randint(1, 20)
    x = np.random.randint(250, 400)
    y = np.random.randint(250, 400)
    prev = x + y
    total = int(x * (1 + per / 100)) + int(y * ((1 - per2) / 100))
    incr = total - prev
    while (x*(1+per/100))%1!=0 or (y*((1-per2)/100))%1!=0 or incr<=0 or ((total*100)-(prev*(100-per2)))%(per+per2)!=0:
        per = np.random.randint(1, 20)
        per2 = np.random.randint(1, 20)
        x = np.random.randint(250, 400)
        y = np.random.randint(250, 400)
        prev = x+y
        total = int(x*(1+(per/100))) + int(y*(1-(per2/100)))
        incr = total-prev
    eq2 = "x(1 + " + str(per/100) +") + y(1 - " + str(per2/100) +") = " + str(total)
    eq3 = str(1+per/100) +"x + " + str(1-per2/100) +"y = " + str(total)
    eq4 = str(100+per)+ "x + " + str(100-per2) +"y = " + str(total*100)
    mul = 100-per2
    eq5 = str(mul) +"x + " + str(mul) +"y = " + str(prev*mul)
    eq6 = str(100+per-mul) +"x = " + str((total*100)-(prev*mul))
    temp = proc_jo(x, 4)
    newx = int(x*(1+per/100))
    eq7 = str(x) +" $$수식$$TIMES$$/수식$$ " + str(1+per/100) +" = " + str(newx)
    newy = int(y*(1-(per2/100)))
    eq8 = str(y) +" $$수식$$TIMES$$/수식$$ " + str(1-(per2/100)) +" = " + str(newy)


    stem = stem.format(per=per, per2=per2, incr=incr, total=total )
    answer = answer.format(newx=newx, newy=newy)
    comment = comment.format(total=total, mul=mul,temp=temp, newx=newx, newy=newy, x=x, y=y, eq2=eq2, prev=prev, per=per, per2=per2, eq3=eq3, eq4=eq4, eq5=eq5, eq6=eq6, eq7=eq7, eq8=eq8, incr=incr)

    return stem, answer, comment

#중2-1-2-195
def expressions212_Stem_163():
    stem = "\n어느 상점에서 두 제품 A, B를 합하여 $$수식$${price}$$/수식$$ 원\n" \
           "에 들여왔다. A 제품은 $$수식$${num}$$/수식$$할, B 제품은 $$수식$${num2}$$/수식$$할의 이익\n" \
           "을 붙여 정가를 정했는데 물건이 팔리지 않아 두\n" \
           "제품 모두 각각 정가의 $$수식$${num3}$$/수식$$할을 할인하여 판매하였\n" \
           "다. 두 제품을 모두 팔아 $$수식$${prof}$$/수식$$ 원의 이익을 얻었을\n" \
           "때, 두 제품 A, B의 원가의 차는?" \
            "\n① $$수식$${x1} 원\n② {x2} 원\n③ {x3} 원\n④ {x4} 원\n⑤ {x5} 원\n   $$/수식$$"
    answer = "\n(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "A 제품의 원가를 x원, B 제품의 원가를 y원이라\n" \
              "하면\n" \
              "$$수식$${eq}$$/수식$$\n\n" \
              "즉, $$수식$${vv}$$/수식$$\n\n" \
              "연립방정식을 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n" \
              "따라서 두 제품 A, B의 원가의 차는\n" \
              "$$수식$${x}$$/수식$$ - $$수식$${y}$$/수식$$ = $$수식$${answ}$$/수식$$ (원)"

    x = np.random.randint(10, 40)*100
    y = np.random.randint(10, 40)*100
    while y>=x:
        x = np.random.randint(10, 40) * 100
        y = np.random.randint(10, 40) * 100
    price = x+y
    num = np.random.randint(1, 6)
    num2 = np.random.randint(1, 6)
    num3 = np.random.randint(1, 6)
    while num==num2 or num3>=num2 or num3>=num:
        num = np.random.randint(1, 6)
        num2 = np.random.randint(1, 6)
        num3 = np.random.randint(1, 6)
    prof = int(((1 + num / 10) * x * (1 - num3 / 10) + (1 + num2 / 10) * y * (1 - num3 / 10)))-price
    while prof<=10 or ((price+prof)%(10-num3)!=0):
        x = np.random.randint(10, 40) * 100
        y = np.random.randint(10, 40) * 100
        while y >= x:
            x = np.random.randint(10, 40) * 100
            y = np.random.randint(10, 40) * 100
        price = x + y
        num = np.random.randint(1, 6)
        num2 = np.random.randint(1, 6)
        num3 = np.random.randint(1, 6)
        while num == num2 or num3 >= num2 or num3 >= num:
            num = np.random.randint(1, 6)
            num2 = np.random.randint(1, 6)
            num3 = np.random.randint(1, 6)
        prof = int(((1 + num / 10) * x * (1 - num3 / 10) + (1 + num2 / 10) * y * (1 - num3 / 10))) - price
    aa1 = "x + y = " +  str(price)
    aa2 = str(1+num/10) +"x TIMES " + str(1-num3/10) +" + " + str(1+num2/10) +"y TIMES " + str(1-num3/10)  + " = " + str(price) +" + " + str(prof)
    aaa = int((price+prof)/(10-num3)*100)
    vv2 = str(10+num) +"x + " + str(10+num2) +"y = " + str(aaa)
    answ = x-y

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)*100
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k > 2:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    eq = "{cases{" + aa1 + "#" + aa2 + "}}"
    vv = "{cases{" + aa1 + "#" + vv2 + "}}"

    stem = stem.format(price=price, num=num, num2=num2, num3=num3, prof=prof, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(x=x, y=y, eq=eq, vv=vv, answ=answ)

    return stem, answer, comment

#중2-1-2-196
def expressions212_Stem_164():
    stem = "\nA, B, C가 함께 하면 $$수식$${num}$$/수식$$일이 걸리는 어떤 일을\n" \
           "A와 C가 함께 하면 $$수식$${num2}$$/수식$$일, B와 C가 함께 하면\n" \
           "$$수식$${num3}$$/수식$$일이 걸린다고 한다. 이때 이 일을 A와 B가\n" \
           "함께 하루에 할 수 있는 일의 양은?" \
            "\n① $$수식$${x1} \n② {x2} \n③ {x3} \n④ {x4} \n⑤ {x5} \n   $$/수식$$"
    answer = "\n(정답): \n" \
            "{ans}"
    comment = "(해설)\n" \
              "A, B, C가 하루에 하는 일의 양을 각각 a, b, \n" \
              "c라 하면\n" \
              "a + b + c = $$수식$$1 over {num}$$/수식$$ $$수식$$cdotscdots$$/수식$$㉠\n" \
              "a + c = $$수식$$1 over {num2}$$/수식$$ $$수식$$cdotscdots$$/수식$$㉡\n" \
              "b + c = $$수식$$1 over {num3}$$/수식$$ $$수식$$cdotscdots$$/수식$$㉢\n" \
              "㉡을 ㉠에 대입하면 b = $$수식$${fra}$$/수식$$\n" \
              "㉢을 ㉠에 대입하면 a = $$수식$${fra2}$$/수식$$\n" \
              "따라서 A, B가 함께 일할 때, 하루에 하는 일의\n" \
              "양은\n" \
              "$$수식$${eq}$$/수식$$     = {answ}"

    num = np.random.randint(2, 10)
    num2 = np.random.randint(2, 15)
    num3 = np.random.randint(2, 15)
    while num>=num2 or num>=num3 or num2>=num3:
        num = np.random.randint(2, 10)
        num2 = np.random.randint(2, 15)
        num3 = np.random.randint(2, 15)
    lcm1 = lcm(num,num2)
    a1 = int(lcm1/num)
    a2 = int(lcm1/num2)
    aa1 = a1-a2
    aa11 = int(aa1/gcd(aa1,lcm1))
    lcm1 = int(lcm1/gcd(aa1,lcm1))
    lcm2 = lcm(num, num3)
    b1 = int(lcm2/num)
    b2 = int(lcm2/num3)
    bb1 = b1-b2
    bb11 = int(bb1/gcd(lcm2, bb1))
    lcm2 = int(lcm2/gcd(lcm2,bb1))
    lcm3 = lcm(lcm2, lcm1)
    c1 = int(lcm3/lcm1)*aa11
    c2 = int(lcm3/lcm2)*bb11
    cc1 = c1+c2
    cc11 = int(cc1/gcd(cc1, lcm3))
    lcm3 = int(lcm3/gcd(cc1, lcm3))
    while lcm3>50:
        num = np.random.randint(2, 10)
        num2 = np.random.randint(2, 15)
        num3 = np.random.randint(2, 15)
        while num >= num2 or num >= num3 or num2 >= num3:
            num = np.random.randint(2, 10)
            num2 = np.random.randint(2, 15)
            num3 = np.random.randint(2, 15)
        lcm1 = lcm(num, num2)
        a1 = int(lcm1 / num)
        a2 = int(lcm1 / num2)
        aa1 = a1 - a2
        aa11 = int(aa1 / gcd(aa1, lcm1))
        lcm1 = int(lcm1 / gcd(aa1, lcm1))
        lcm2 = lcm(num, num3)
        b1 = int(lcm2 / num)
        b2 = int(lcm2 / num3)
        bb1 = b1 - b2
        bb11 = int(bb1 / gcd(lcm2, bb1))
        lcm2 = int(lcm2 / gcd(lcm2, bb1))
        lcm3 = lcm(lcm2, lcm1)
        c1 = int(lcm3 / lcm1) * aa11
        c2 = int(lcm3 / lcm2) * bb11
        cc1 = c1 + c2
        cc11 = int(cc1 / gcd(cc1, lcm3))
        lcm3 = int(lcm3 / gcd(cc1, lcm3))
    answ = "$$수식$${"+str(cc11)+"} over {"+str(lcm3)+"}$$/수식$$"
    fra = "{" + str(aa11) + "} over {" + str(lcm1) + "}"
    fra2 = "{"+str(bb11)+"} over {"+str(lcm2)+"}"
    eq = fra2 +" + " + fra

    bb = []
    dd=[]
    while len(bb) < 4:
        k = np.random.randint(1, 15)
        u = np.random.randint(0, 2)
        if u == 1:
            k = cc1 + k
        else:
            k = abs((cc1 - k))
        if k==0:
            k = 1
        k1 = int(k/gcd(k,lcm3))
        e = int(lcm3/gcd(k,lcm3))
        if k not in dd and k != cc1:
            dd.append(k)
            bb.append("$$수식$${"+str(k1)+"} over {"+str(e)+"}$$/수식$$")
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
    stem = stem.format(num=num, num2=num2, num3=num3, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, num=num, num2=num2, num3=num3, fra=fra, fra2=fra2, answ=answ)

    return stem, answer, comment

#중2-1-2-197
def expressions212_Stem_165():
    stem = "둘레의 길이가 $$수식$${num}$$/수식$$ km인 연못을 A, B 두 사람이\n" \
           "같은 장소에서 동시에 출발하여 서로 반대 방향으\n" \
           "로 돌면 $$수식$${time}$$/수식$$분 후 처음으로 다시 만나고, 서로\n" \
           "같은 방향으로 돌면 $$수식$${time2}$$/수식$$분 후에 처음으로 다시 만\n" \
           "난다고 한다. 이때 A, B 두 사람의 속력은 각각\n" \
           "분속 몇 m인지 구하시오.(단, A의 속력은 B의\n" \
           "속력보다 빠르다.)"
    answer = "(정답): \n" \
            "A: $$수식$${x}$$/수식$$ m/분, B: $$수식$${y}$$/수식$$ m/분"
    comment = "(해설)\n" \
              "A의 속력을 x m, B의 속력을 분속 y m라\n" \
              "하면 반대 방향으로 돌 때,\n" \
              "(A가 움직인 거리) + (B가 움직인 거리)\n" \
              "= $$수식$${dis}$$/수식$$ (m)\n" \
              "즉, {eq} $$수식$$cdotscdots$$/수식$$㉠\n" \
              "같은 방향으로 돌 때,\n" \
              "(A가 움직인 거리) - (B가 움직인 거리)\n" \
              "= $$수식$${dis}$$/수식$$ (m)\n" \
              "즉, {eq2} $$수식$$cdotscdots$$/수식$$㉡\n" \
              "㉠, ㉡ 연립하여 풀면 x = $$수식$${x}$$/수식$$, y = $$수식$${y}$$/수식$$\n\n" \
              "따라서 A의 속력은 분속 $$수식$${x}$$/수식$$ m이고\n" \
              "B의 속력은 분속 $$수식$${y}$$/수식$$ m이다."

    x = np.random.randint(13, 45)*5
    y =  np.random.randint(13, 45)*5
    while x<=y:
        x = np.random.randint(13, 45) * 5
        y = np.random.randint(13, 45) * 5
    time = np.random.randint(1, 7)*10
    time2 = np.random.randint(1, 7)*10
    while time*(x+y)!=time2*(x-y) or (time*(x+y))%1000!=0:
        x = np.random.randint(13, 45) * 5
        y = np.random.randint(13, 45) * 5
        while x <= y:
            x = np.random.randint(13, 45) * 5
            y = np.random.randint(13, 45) * 5
        time = np.random.randint(1, 7) * 10
        time2 = np.random.randint(1, 7) * 10
    dis = (time*(x+y))
    num = int((time*(x+y))/1000)
    eq = str(time) +"x + " + str(time) +"y = " + str(dis)
    eq2 = str(time2) +"x - " + str(time2) +"y = " + str(dis)
    stem = stem.format(num=num, time=time, time2=time2)
    answer = answer.format(x=x, y=y)
    comment = comment.format(eq=eq, eq2=eq2, dis=dis, x=x, y=y)

    return stem, answer, comment

#중2-1-2-120
def expressions212_Stem_166():
    stem = "\n다음을 만족시키는 두 자리의 자연수를 구하시오.$$표$$\n" \
           "십의 자리의 숫자가 x, 일의 자리의 숫자가 y\n" \
           "인 두 자리의 자연수가 있다. 십의 자리의 숫\n" \
           "자와 일의 자리의 숫자의 합은 $$수식$${add}$$/수식$${temp}고, 십의 자\n" \
           "리의 숫자와 일의 자리의 숫자를 바꾸면 처음\n" \
           "의 수보다 $$수식$${big}$$/수식$$만큼 크다.$$/표$$"
    answer = "\n(답): \n" \
            "{ans}\n"
    comment = "(해설)\n" \
              "$$수식$${aa}$$/수식$$   $$수식$$``$$/수식$$                  이므로 $$수식$$``$$/수식$$ $$수식$${vv}$$/수식$$\n\n" \
              "x, y는 한 자리의 자연수이므로 {aa1}의 해\n" \
              "는 {list}\n" \
              "{vv2}   의 해는 {list2}\n" \
              "즉, 연립방정식 $$수식$${vv}$$/수식$$  $$수식$$``$$/수식$$        의 해는 {answ}\n\n" \
              "따라서 두 자리의 자연수는 {ans}"

    x = np.random.randint(1, 10)
    y = np.random.randint(1, 10)
    while y<=x:
        x = np.random.randint(1, 10)
        y = np.random.randint(1, 10)
    add =x+y
    temp = proc_jo(add, 3)
    big = (y*10+x)-(x*10+y)
    aa1 = "x + y = " + str(add)
    aa2 ="10y +x = 10x + y + "+str(big)
    gcd1 = gcd(big, 9)
    r = int(9/gcd1)
    rr = int(big/gcd1)*-1
    vv2 = str(r) +"x - " +str(r) +"y = " + str(rr)
    if r==1:
        vv2 = "x - y = " + str(rr)
    liste=[]
    list=""
    for i in range(1, 10):
        for j in range(1, 10):
            if i+j ==add:
                liste.append([i,j])
    for i in range(len(liste)-1):
        list = list + "(" + str(liste[i][0]) +", " + str(liste[i][1])+") , "
    list = list +"(" + str(liste[-1][0]) +", " + str(liste[-1][1])+")"

    liste = []
    list2 = ""
    for i in range(1, 10):
        for j in range(1, 10):
            if r*i -r*j== rr:
                liste.append([i, j])
    for i in range(len(liste) - 1):
        list2 = list2 + "(" + str(liste[i][0]) + ", " + str(liste[i][1]) + ") , "
    list2 = list2 + "(" + str(liste[-1][0]) + ", " + str(liste[-1][1]) + ")"
    answ ="("+str(x) +", " +str(y) +")"
    ans = x*10 +y
    aa = "{cases{" +aa1 +"#" + aa2 +"}}"
    vv = "{cases{" +aa1 +"#" + vv2 +"}}"

    stem = stem.format(add=add, big=big, temp=temp)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, list=list, list2=list2, vv=vv, aa=aa, aa1=aa1, aa2=aa2, vv2=vv2, ans=ans)

    return stem, answer, comment