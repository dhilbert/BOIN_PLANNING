import numpy as np
from sympy import Symbol, solve, Eq
import random
import math

answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
}

answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤",
    5: "⑥",
    6: "⑦",
    7: "⑧",
    8: "⑨",
    9: "⑩",
    10: "⑪",
    11: "⑫",
    12: "⑬",
    13: "⑭",
    14: "⑮"
}

answer_kodict = {
    0: "㉠",
    1: "㉡",
    2: "㉢",
    3: "㉣",
    4: "㉤"
}

answer_kodict2 = {
    0: 'ㄱ',
    1: 'ㄴ',
    2: 'ㄷ',
    3: 'ㄹ',
    4: 'ㅁ'
}

answer_kodict3 = {
    0: '㈀',
    1: '㈁',
    2: '㈂',
    3: '㈃',
    4: '㈄'
}

def make_example_by_interval_root_ver(ans, interval):
    reverse = 0
    if ans <= interval:
        ans_index = 0
        reverse = int(np.random.rand() + 0.5)
    else:
        limit = (ans // interval) if ans // interval < 5 else 5
        ans_index = np.random.randint(0, limit)
        reverse = int(np.random.rand() + 0.25)

    ex_list = []
    if reverse == 0:
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(make_root(1, ans + (i - ans_index) * interval))
    else:
        ans_index = 4 - ans_index
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(make_root(1, ans + (ans_index - i) * interval))
    return ex_list
#a root b
def make_root(a, b, mini=True) :
    n = (1 if a==1 else a)
    if mini==True :
        for i in range(10, 1, -1):
            if b % i**2 == 0 :
                n*=i
                b/=i**2
            if b==1 : return int(n)
        return tostr(n, True, True)+'root'+str(int(b))
    else : return tostr(n, True, True)+'root'+str(int(b))

def make_frac(a, b):
    if a==0 : return 0
    temp = ctr_frac2(abs(a), abs(b))
    if temp[1] == 1:
        if a * b >= 0:
            return temp[0]
        else:
            return -temp[0]
    elif a * b >= 0:
        return '{' + str(abs(temp[0])) + 'OVER' + str(abs(temp[1])) + '}'
    else:
        return '-{' + str(abs(temp[0])) + 'OVER' + str(abs(temp[1])) + '}'

def make_frac2(a, b, is_first, is_coef):
    if a==0 : return tostr(0, is_first, is_coef)
    temp = ctr_frac2(abs(a), abs(b))
    if temp[1] == 1:
        if a * b >= 0:
            return tostr(temp[0], is_first, is_coef)
        else:
            return tostr(-temp[0], is_first, is_coef)
    elif a * b >= 0:
        if is_first : return '{' + str(abs(temp[0])) + 'OVER' + str(abs(temp[1])) + '}'
        else : return '+`{' + str(abs(temp[0])) + 'OVER' + str(abs(temp[1])) + '}'
    else:
        if is_first : return '-{' + str(abs(temp[0])) + 'OVER' + str(abs(temp[1])) + '}'
        else : return '-`{' + str(abs(temp[0])) + 'OVER' + str(abs(temp[1])) + '}'

def brac(n) :
    if n>=0 : return str(n)
    else : return 'LEFT (' + str(n) + 'RIGHT )'

def rand_not0(first, last) :
    num = random.randint(first, last)
    while(num==0) :
        num = random.randint(first, last)
    return num

def tostr(n, is_first, is_coef, prevnum=0) :
    if n==1 :
        if is_first==True :
            if is_coef==True : n=''
            else : n='1'
        elif is_coef==True : n='+`'
        else : n='+`1'
    elif n==-1 :
        if is_first==True :
            if is_coef == True: n = '-'
            else: n='-1'
        elif is_coef==True : n='-`'
        else : n='-`1'
    elif n>0 :
        if is_first==True : n=str(n)
        else : n='+`'+str(n)
    elif n<0:
        if is_first == True: n=str(n)
        else: n='`'.join(str(n))
    else :
        if is_first == True: n=str(n)
        else :
            if prevnum<0 : n='-`0'
            elif prevnum>0 : n='+`0'
            else : n='`0'
    return n

def gcd (a, b):
    if b == 0:
        return a
    else :
        if a < b:
            a, b = b, a
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

# contract fraction a/b
def ctr_frac(a, b):
    if gcd(a,b) == 1:
        return [-1, "already contracted fraction"]
    else:
        return [int(a/gcd(a,b)), int(b/gcd(a,b))]

def ctr_frac2(a, b):
    asign=1
    bsign=1
    if a<0 :
        asign=-1
        a=-a
    if b<0 :
        bsign=-1
        b=-b
    return [int(a/gcd(a,b))*asign, int(b/gcd(a,b))*bsign]

#  a[0]/a[1] + b[0]/b[1]
def sum_frac(a, b):
    lcm_ = lcm(a[1], b[1])
    ctr = ctr_frac2(a[0] * int(lcm_/a[1]) + b[0] * int(lcm_/b[1]), lcm_)
    return [ctr[0], ctr[1]]

def minus_frac(a, b):
    lcm_ = lcm(a[1], b[1])
    ctr = ctr_frac2(a[0] * int(lcm_/a[1]) - b[0] * int(lcm_/b[1]), lcm_)
    return [ctr[0], ctr[1]]

def make_example(ans):
    interval = np.random.randint(1, 3)
    reverse = 0
    if ans <= interval:
        ans_index = 0
        reverse = int(np.random.rand() + 0.5)
    else:
        limit = (ans // interval) if ans // interval < 5 else 5
        ans_index = np.random.randint(0, limit)
        reverse = int(np.random.rand() + 0.25)

    ex_list = []
    if reverse == 0:
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (i - ans_index) * interval)
    else:
        ans_index = 4 - ans_index
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (ans_index - i) * interval)
    return ex_list

def make_example_by_interval(ans, interval): #make(5, 2)
    reverse = 0
    if ans <= interval:
        ans_index = 0
        reverse = int(np.random.rand() + 0.5)
    else:
        limit = (ans // interval) if ans // interval < 5 else 5
        ans_index = np.random.randint(0, limit)
        reverse = int(np.random.rand() + 0.25)

    ex_list = []
    if reverse == 0:
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (i - ans_index) * interval)
    else:
        ans_index = 4 - ans_index
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (ans_index - i) * interval)
    return ex_list

def make_example_by_interval_fraction_ver(ans, interval, high):
    reverse = 0
    if high - ans < interval:
        ans_index = 4
        reverse = int(np.random.rand() + 0.5)
    elif ans <= interval:
        ans_index = 0
        reverse = int(np.random.rand() + 0.5)
    else:
        h_limit = (ans // interval) if ans // interval < 5 else 5
        l_limit = 4 - ((high - ans) // interval) if 4 - ((high - ans) // interval) >= 0 else 0
        ans_index = np.random.randint(l_limit, h_limit)
        reverse = int(np.random.rand() + 0.25)

    ex_list = []
    if reverse == 0:
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (i - ans_index) * interval)
    else:
        ans_index = 4 - ans_index
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (ans_index - i) * interval)
    return ex_list

# ans = a/b, interval = 1/fintv
def make_fraction_example(a, b, fintv):
    lcm_ = lcm(b, fintv)
    mult = [int(lcm_ / b), int(lcm_ / fintv)]
    b = b * mult[0]
    a = a * mult[0]
    fintv = fintv * mult[1]

    ans_list = []
    example_list = make_example_by_interval(a, mult[1])
    ans_list.append(example_list[0])
    for i in range(5):
        if gcd(example_list[i + 1], fintv) != 1:
            ctr = ctr_frac(example_list[i + 1], fintv)
            if ctr[1] == 1:
                ans_list.append(ctr[0])
            else:
                ans_list.append("{%d} over {%d}" % (ctr[0], ctr[1]))
        else:
            ans_list.append("{%d} over {%d}" % (example_list[i + 1], fintv))
    print(ans_list)

    return ans_list

def make_fraction_example2(a, b, fintv):
    lcm_ = lcm(b, fintv)
    mult = [int(lcm_ / b), int(lcm_ / fintv)]
    b = b * mult[0]
    a = a * mult[0]
    fintv = fintv * mult[1]

    ans_list = []
    example_list = make_example_by_interval(a, mult[1])
    ans_list.append(example_list[0])
    for i in range(5):
        if example_list[i+1]==0 : ans_list.append(0)
        elif gcd(abs(example_list[i + 1]), fintv) != 1:
            ctr = ctr_frac2(example_list[i + 1], fintv)
            if ctr[1] == 1:
                ans_list.append(ctr[0])
            else:
                ans_list.append(make_frac(ctr[0], ctr[1]))
        else:
            ans_list.append(make_frac(example_list[i + 1], fintv))

    return ans_list

# include alphabet - changed
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
        if (num >= 65 and num <= 90) or (num >= 97 and num <= 122):
            t_list = [76, 77, 78, 82, 108, 109, 110, 114]
            if num in t_list:
                return True
            return False
        else:
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
        # 이(라고)
        if bool_jo(num):
            return "이"
        return ""
    elif bool_jo(num):
        # 을를
        return "을"
    return "를"

def name_jo(num):
    # 이
    if bool_jo(num):
        return "이"
    return ""


def getdivisor(num):
    if num < 1:
        return 0
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def is_prime(number):
    if number != 1:
        for i in range(2, number):
            if number % i == 0:
                return False
    else:
        return False
    return True


def getfactor(n):
    result = []
    for i in range(2, int(n / 2) + 1):
        if not is_prime(i):
            continue
        count = 0
        while n % i == 0:
            count = count + 1
            n = int(n / i)
        if count != 0:
            result.append((i, count))
            # (소수, 개수) 형태로 리스트에 추가됨
        if n == 1:
            break
    return result


def getfactor2(n):
    result = []
    for i in range(2, int(n / 2) + 1):
        if not is_prime(i):
            continue
        while n % i == 0:
            result.append(i)
            n = int(n / i)
        if n == 1:
            break
    return result


def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)


def quadequation313_Stem_001():
    stem = "다음 중 이차함수인 것은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     \n③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     \n⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "① 일차함수이다.\n" \
              "② 이차함수가 아니다.\n" \
              "③ $$수식$${com1}$$/수식$$이므로 일차함수이다.\n" \
              "④ 이차함수이다.\n" \
              "⑤ 이차함수가 아니다.\n" \
              "따라서 이차함수인 것은 ④이다.\n\n"

    ex1 = "y="+tostr(rand_not0(1, 5), True, True)+"x" + tostr(rand_not0(-5, 5), False, False)
    ex2 = "y= {"+ str(rand_not0(1, 5))+"} over {x^2}"+ tostr(rand_not0(-5, 5), False, False)
    n1 = rand_not0(-5, 5)
    ex3 = "y=x^2`-`LEFT("+ str(n1)+"-x RIGHT)^2"
    ex4 = "y= {x^2} over {"+ str(rand_not0(1, 5))+"}-2"
    ex5 = "y=x^3`+`LEFT("+ str(rand_not0(-5, 5))+"-x RIGHT)^2"

    com1 ="y=x^2`-`LEFT("+ str(n1)+"-x RIGHT)^{2}="+ tostr(n1*2, True, True)+"x"+ tostr(-n1*n1, False, False)
    stem = stem.format(ex1=ex1, ex2=ex2, ex3=ex3, ex4=ex4, ex5=ex5)
    answer = answer.format(a1=answer_dict[3])
    comment = comment.format(com1= "$$수식$$"+com1+"$$/수식$$")

    return stem, answer, comment

#다시
def quadequation313_Stem_002():
    stem = "$$수식$$ y`=`{n1}x^2`{n2}`{n3}kx`LEFT({n4}`{n5}x RIGHT) `$$/수식$$가 이차함수일 때, 다음 중 상수 $$수식$$k`$$/수식$$의 값이 될 수 없는 것은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{n1}x^2`{n2}`{n3}kx`LEFT({n4}`{n5}x RIGHT)`=`LEFT({c1}`{c2}k RIGHT)x^2`{c3}kx`{n2} `$$/수식$$\n" \
              "이 식이 이차함수가 되려면\n" \
              "$$수식$$ {c1}`{c2}k`!=`0 `$$/수식$$ $$수식$$ THEREFORE```k`!=`{k} `$$/수식$$\n\n"

    n1 = rand_not0(-6, 6)
    n2 = rand_not0(-9, 9)
    n3 = [-1, 1][random.randint(0, 1)]
    n4 = rand_not0(1, 3)
    n5 = [-1, 1][random.randint(0, 1)]

    c1 = n1
    c2 = n3*n5
    c3 = n3*n4
    k = -c1//c2

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, True)
    str_n5 = tostr(n5, False, True)
    str_c2 = tostr(c2, False, True)
    str_c3 = tostr(c3, False, True)

    example_list = make_example(k)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, n5=str_n5,  \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, n5=str_n5, c1=c1, c2=str_c2, c3=str_c3, k=k)

    return stem, answer, comment

#f()+f()
def quadequation313_Stem_003():

    stem = "이차함수 $$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`{n3} `$$/수식$$에서 $$수식$$ f`LEFT({x1} RIGHT)`+`f`LEFT({x2} RIGHT) `$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`{n3} `$$/수식$$이므로\n" \
              "$$수식$$ f`LEFT({x1} RIGHT)`=`{n1} {times1} {x1_}^2 `{n2} {times2} {x1_}`{n3}`=`{c1} $$/수식$$\n" \
              "$$수식$$ f`LEFT({x2} RIGHT)`=`{n1} {times1} {x2_}^2 `{n2} {times2} {x2_}`{n3}`=`{c2} $$/수식$$\n" \
              "$$수식$$ THEREFORE```f`LEFT({x1} RIGHT)`+`f`LEFT({x2} RIGHT)`=`{c1}`+`{c2}`=`{c3} $$/수식$$\n\n"

    out = []
    num = random.randint(-3, 3)
    for i in range(2):
        while num in out:
            num = random.randint(-3, 3)
        out.append(num)
    x1 = out[0]
    x2 = out[1]

    n1 = rand_not0(-3, 3)
    n2 = rand_not0(-5, 5)
    n3 = rand_not0(-9, 9)

    c1 = n1*(x1**2) + n2*x1 + n3
    c2 = n1*(x2**2) + n2*x2 + n3
    c3 = c1+c2

    ans=c3
    example_list = make_example(ans)

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, False)

    x1_ = x1 if x1>=0 else 'LEFT (' + str(x1) + 'RIGHT )'
    x2_ = x2 if x2>=0 else 'LEFT (' + str(x2) + 'RIGHT )'

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, x1=x1, x2=x2,  \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, x1=x1, x2=x2, x1_=x1_, x2_=x2_, c1=c1, c2=c2, c3=c3, \
                            times1=('' if n1==1or n1==-1 else 'TIMES'), times2=('' if n2==1 or n2==-1 else 'TIMES'))

    return stem, answer, comment


def quadequation313_Stem_004():
    stem = "다음 중 $$수식$$y`$$/수식$$가 $$수식$$x`$$/수식$$에 대한 이차함수인 것은?\n" \
           "① 한 모서리의 길이가 $$수식$${n1}x`$$/수식$$인 정육면체의 부피 $$수식$$y`$$/수식$$\n" \
           "② 한 변의 길이가 $$수식$${n2}x`$$/수식$$인 정삼각형 둘레의 길이 $$수식$$y`$$/수식$$\n" \
           "③ 자동차가 시속 $$수식$${n3}``rmkm`$$/수식$$로 $$수식$${n4}`$$/수식$$시간 동안 달린 거리 $$수식$$y``rmkm`$$/수식$$\n" \
           "④ 밑면의 반지름의 길이가 $$수식$$x`$$/수식$$, 높이가 $$수식$${n5}`$$/수식$$인 원기둥의 부피 $$수식$$y`$$/수식$$\n" \
           "⑤ 둘레의 길이가 $$수식$${n6}`$$/수식$$, 세로의 길이가 $$수식$$x`$$/수식$$인 직사각형 가로의 길이\n\n"
    answer = "(답): ④\n"
    comment = "(해설)\n" \
              "① $$수식$$y`=`{c4}x^3`$$/수식$$이므로 이차함수가 아니다.\n" \
              "② $$수식$$y`=`{c5}x`$$/수식$$(일차함수)\n" \
              "③ (거리) = (속력)$$수식$$`TIMES`$$/수식$$(시간)이므로 $$수식$$y`=`{c1}x`$$/수식$$(일차함수)\n" \
              "④ $$수식$$y`=`{c2}`pi`x^2`$$/수식$$(이차함수)\n" \
              "⑤ $$수식$${n6}`=`2`(y`+`x)`$$/수식$$, $$수식$${c3}`=`y`+`x`$$/수식$$\n" \
              "$$수식$$THEREFORE```y`=`{c3}`-`x`$$/수식$$(일차함수)\n" \
              "따라서 이차함수인 것은 ④이다.\n\n"

    n1 = random.randint(2, 5)
    n2 = random.randint(2, 5)
    n3 = ['x', random.randint(50, 150)][random.randint(0,1)]
    n4 = (random.randint(1, 5) if n3=='x' else 'x')
    n5 = random.randint(1, 10)
    n6 = 4*random.randint(1, 8)
    c1 = (tostr(n3, True, True) if type(n3)==int else tostr(n4, True, True))
    c2 = tostr(n5, True, True)
    c3 = n6//2
    c4 = n1*n1*n1
    c5 = 3*n2

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, True, True)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=n3, n4=n4, n5=n5, n6=n6)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=n3, n4=n4, n5=n5, n6=n6, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)

    return stem, answer, comment


def quadequation313_Stem_005():
    stem = "보기에서 $$수식$$y`$$/수식$$가 $$수식$$x`$$/수식$$에 대한 이차함수인 것의 개수를 구하시오.\n" \
           "$$표$$\n" \
           "㈀ $$수식$${ex1}$$/수식$$\n㈁ $$수식$${ex2}$$/수식$$\n㈂ $$수식$${ex3}$$/수식$$\n㈃ $$수식$${ex4}$$/수식$$\n㈄ $$수식$${ex5}$$/수식$$" \
           "\n$$/표$$\n"
    answer = "(답): $$수식$$3$$/수식$$개\n"
    comment = "(해설)\n" \
              "㈀ $$수식$${ex1}$$/수식$$\n㈁ $$수식$${ex2}$$/수식$$\n㈂ $$수식$${ex3}$$/수식$$\n㈃ $$수식$${ex4}$$/수식$$\n㈄ $$수식$${ex5}$$/수식$$\n" \
              "따라서 이차함수인 것은 {c1}, {c2}, {c3}의 $$수식$$3$$/수식$$개이다.\n\n"

    n2 = rand_not0(1, 5)
    n31 = rand_not0(-3, 3)
    n32 = rand_not0(1, 3)
    n33 = rand_not0(-4, 4)
    while n32 * n31 + n33==0 : n33 = rand_not0(-4, 4)
    n41 = rand_not0(1, 3)
    n42 = rand_not0(-5, 5)
    n5 = rand_not0(-4, 4)
    ex = [['x^2`-`y`=`0', 'y`=`x^2', 1], ['y`=`LEFT('+str(n2)+'`-`x RIGHT)^2', 'y`=`x^2`{}x`{}'.format(tostr(-n2*2, False, True), tostr(n2*n2, False, False)), 1],\
          ['y`=`LEFT(x`{}RIGHT)LEFT({}x`{}RIGHT)'.format(tostr(n31, False, False), tostr(n32, True, True), tostr(n33, False, False)),\
           'y`=`{}x^2`{}x`{}'.format(tostr(n32, True, True), tostr(n32*n31+n33, False, True), tostr(n31*n33, False, False)), 1],\
          ['y`=`{}x^2`-({}x`{})^2'.format(tostr(n41*n41, True, True), tostr(n41, True, True), tostr(n42, False, False)),\
           'y`=`{}x`{}'.format(tostr(-n41*n42*2, True, True), tostr(-n42*n42, False, False)), -1],\
          ['y=-x(x`{})+x^2'.format(tostr(n5, False, False)), 'y`=`{}x'.format(-n5, True, True), -1]]
    random.shuffle(ex)

    list=[]
    index=['㈀', '㈁', '㈂', '㈃', '㈄']
    for i in range(5) :
        if ex[i][2]==1 : list.append(i)
    stem = stem.format(ex1=ex[0][0], ex2=ex[1][0], ex3=ex[2][0], ex4=ex[3][0], ex5=ex[4][0])
    comment = comment.format(ex1=ex[0][1], ex2=ex[1][1], ex3=ex[2][1], ex4=ex[3][1], ex5=ex[4][1], c1=index[list[0]], c2=index[list[1]], c3=index[list[2]])

    return stem, answer, comment


def quadequation313_Stem_006():
    stem = "다음 보기 중 이차함수인 것을 모두 고른 것은?\n" \
           "$$표$$\n" \
           "㈀ $$수식$${e1}$$/수식$$\n㈁ $$수식$${e2}$$/수식$$\n㈂ $$수식$${e3}$$/수식$$\n㈃ $$수식$${e4}$$/수식$$" \
           "\n$$/표$$\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     \n④ {ex4}    ⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "㈀ {ex1}\n㈁ {ex2}\n㈂ {ex3}\n㈃ {ex4}\n" \
              "따라서 이차함수인 것은 {c1}, {c2}이다.\n\n"

    n2 = rand_not0(1, 5)
    n31 = rand_not0(-3, 3)
    n32 = rand_not0(-4, 4)
    while n32==-n31 : n32 = rand_not0(-4, 4)
    ex = [['y`=`{}x`{}'.format(tostr(rand_not0(-3, 3), True, True), tostr(rand_not0(-6, 6), False, False)), '일차함수', -1], \
          ['y`=`x({}`-`x)'.format(str(n2)), '$$수식$$y`=`-x^2`{}x`$$/수식$$(이차함수)'.format(tostr(n2, False, True)), 1],\
          ['y`=`LEFT(x`{}RIGHT)LEFT(x`{}RIGHT)`-`x^2'.format(tostr(n31, False, False), tostr(n32, False, False)),\
           '$$수식$$y`=`{}x`{}`$$/수식$$(일차함수)'.format(tostr(n31+n32, True, True), tostr(n31*n32, False, False)), -1],\
          ['y`=`x^2`{}x'.format(tostr(rand_not0(-6, 6), False, True)), '이차함수', 1]]
    random.shuffle(ex)

    list=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    index=['㈀', '㈁', '㈂', '㈃', '㈄']
    ans =[]

    for i in range(4) :
        if ex[i][2]==1 : ans.append(i)

    num = random.randint(0, 5)
    while list[num]==ans : num = random.randint(0, 5)

    example_list=[]
    ind = 0
    for i in range(6) :
        if i==num : continue
        if list[i]==ans : ans.append(ind)
        example_list.append(index[list[i][0]]+', '+index[list[i][1]])
        ind+=1
    stem = stem.format(e1=ex[0][0], e2=ex[1][0], e3=ex[2][0], e4=ex[3][0], \
                       ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans[2]])
    comment = comment.format(ex1=ex[0][1], ex2=ex[1][1], ex3=ex[2][1], ex4=ex[3][1], c1=index[ans[0]], c2=index[ans[1]])

    return stem, answer, comment


def quadequation313_Stem_007():
    stem = "다음 중 $$수식$$y`$$/수식$$가 $$수식$$x`$$/수식$$에 대한 이차함수인 것을 모두 고르면? (정답 $$수식$$2`$$/수식$$개)\n" \
           "① {ex1}\n" \
           "② {ex2}\n" \
           "③ {ex3}\n" \
           "④ {ex4}\n" \
           "⑤ {ex5}\n\n"
    answer = "(답): {a1}, {a2}\n"
    comment = "(해설)\n" \
              "① {c1}\n" \
              "② {c2}\n" \
              "③ {c3}\n" \
              "④ {c4}\n" \
              "⑤ {c5}\n" \
              "따라서 이차함수인 것은 {a1}, {a2}이다.\n\n"

    n1 = 3*random.randint(1, 3)
    n2 = rand_not0(-4, 4)
    n3 = ' LEFT(x`'+tostr(n2, False, False)+'RIGHT)'
    n4 = rand_not0(-4, 4)
    n5 = ' LEFT(x`'+tostr(n4, False, False)+' RIGHT)'
    rand = random.randint(0, 1)
    e1 = [["밑면인 원의 반지름의 길이가 $$수식$${}`rmcm`$$/수식$$, 높이가 $$수식$${}`rmcm`$$/수식$$인 원뿔의 부피 $$수식$$y`rmcm^3`$$/수식$$".format([n1, n3][rand], [n1, n3][1-rand]),\
           "$$수식$$y`=`1 OVER 3`TIMES`pi`TIMES`{}^2`TIMES`{}``=`{} pi{}^2#`=`{}pi x^2`{} pi x`{} pi`$$/수식$$".format( \
               n3, n1, tostr(n1//3, True, True), n3, tostr(n1//3, True, True), tostr(2*(n1//3)*n2, False, True), tostr(n2*n2*(n1//3), False, True))],\
          ["밑변의 길이가 $$수식$${}`rmcm`$$/수식$$, 높이가 $$수식$${}`rmcm`$$/수식$$인 평행사변형의 넓이 $$수식$$y`rmcm^2`$$/수식$$".format(['x', n3][rand], ['x', n3][1-rand]),\
           'y`=`x {}`=`x^2`{}x'.format(n5,tostr(n4, False, True))]]
    n1 = random.randint(1, 4)
    n2 = 2*random.randint(1, 3)
    rand = random.randint(0, 1)
    n3 = rand_not0(2, 4)
    n4 = rand_not0(2, 3)
    n5 = rand_not0(2, 5)
    n6 = 2*rand_not0(1, 2)
    n7 = ' LEFT('+tostr(n3, True, True)+'x`'+tostr(n4, False, False)+' RIGHT)'
    n8 = ' LEFT{'+n7+'`'+tostr(n5, False, True)+'x RIGHT } '
    e2 = [["한 변의 길이가 $$수식$${}x`rmcm`$$/수식$$인 정사각형의 둘레의 길이 $$수식$$y``rmcm`$$/수식$$".format(tostr(n1, True, True)),\
           'y`=`4`TIMES`{}x`=`{}x'.format(tostr(n1, True, True), tostr(n1*4, True, True))],\
          ["밑변의 길이가 $$수식$${}`rmcm`$$/수식$$, 높이가 $$수식$${}`rmcm`$$/수식$$인 삼각형의 넓이 $$수식$$y``rmcm^2`$$/수식$$".format(['x', n2][rand], ['x', n2][1-rand]),\
           'y`=`1 OVER 2`TIMES`x`TIMES`{}`={}x'.format(n2, tostr(n2//2, True, True))],\
          ["윗변의 길이가 $$수식$${}`rmcm`$$/수식$$, 아랫변의 길이가 $$수식$${}x`rmcm`$$/수식$$, 높이가 $$수식$${}`rmcm`$$/수식$$인 사다리꼴의 넓이 $$수식$$y`rmcm^2`$$/수식$$".format(\
              n7, tostr(n5, True, True), n6),\
              'y`=`1 OVER 2`TIMES`{}`TIMES`{}`=`{}x`{}'.format(n8, n6, tostr((n6//2)*(n3+n5), True, True), tostr((n6//2)*n4, False, False))
            ]]

    ans = []
    for i in range(2):
        temp = random.randint(0, 4)
        while temp in ans :  temp = random.randint(0, 4)
        ans.append(temp)

    example_list=[]
    comment_list=[]
    index1=0
    index2=0
    for i in range(5):
        if i in ans :
            example_list.append(e1[index1][0])
            comment_list.append('$$수식$$'+e1[index1][1] +'`$$/수식$$이므로 이차함수이다.')
            index1+=1
        else :
            example_list.append(e2[index2][0])
            comment_list.append('$$수식$$' + e2[index2][1] +'`$$/수식$$이므로 이차함수가 아니다.')
            index2+=1

    ans.sort()
    stem = stem.format(ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans[0]], a2=answer_dict[ans[1]])
    comment = comment.format(c1=comment_list[0], c2=comment_list[1], c3=comment_list[2], c4=comment_list[3], c5=comment_list[4], a1=answer_dict[ans[0]], a2=answer_dict[ans[1]])

    return stem, answer, comment


def quadequation313_Stem_008():
    stem = "다음 보기 중 이차함수인 것을 모두 고른 것은?\n" \
           "$$표$$\n" \
           "㈀ $$수식$${e1}$$/수식$$\n㈁ $$수식$${e2}$$/수식$$\n㈂ $$수식$${e3}$$/수식$$\n㈃ $$수식$${e4}$$/수식$$" \
           "\n$$/표$$\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     \n④ {ex4}    ⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "㈀ {ex1}\n㈁ {ex2}\n㈂ {ex3}\n㈃ {ex4}\n" \
              "따라서 이차함수인 것은 {c1}, {c2}이다.\n\n"

    n1 = 3 * random.randint(1, 3)
    n2 = rand_not0(-4, 4)
    n3 = ' LEFT(x`' + tostr(n2, False, False) + 'RIGHT)'
    n4 = rand_not0(-4, 4)
    n5 = ' LEFT(x`' + tostr(n4, False, False) + ' RIGHT)'
    rand = random.randint(0, 1)
    e1 = [['반지름의 길이가  $$수식$$x`$$/수식$$인 구의 겉넓이 $$수식$$y`$$/수식$$', " $$수식$$y`=`4 pi x^2`$$/수식$$(이차함수)"], \
          ["한 개에 $$수식$${}`$$/수식$$원 하는 공책 $$수식$${}`$$/수식$$개의 값 $$수식$$y`$$/수식$$원".format(\
              ['x', n3][rand], ['x', n3][1 - rand]), \
              '$$수식$$y`=`x {}`````````THEREFORE``y`=`x^2`{}x`$$/수식$$(이차함수)'.format(tostr(n2, False, False), tostr(n2, False, True))]]
    n1 = rand_not0(1,5)*100
    n1 = random.randint(1, 4)
    n3 = rand_not0(2, 4)
    n4 = rand_not0(2, 3)
    n5 = rand_not0(2, 5)
    n6 = 2 * rand_not0(1, 2)
    n7 = ' LEFT(' + tostr(n3, True, True) + 'x`' + tostr(n4, False, False) + ' RIGHT)'
    n8 = ' LEFT{' + n7 + '`' + tostr(n5, False, True) + 'x RIGHT } '


    e2 = [['하루에 {}원씩 저금할 때, $$수식$$x`$$/수식$$일 후에 모인 금액 $$수식$$y`$$/수식$$'.format(n1), "$$수식$$y`=`{}x`$$/수식$$(일차함수)".format(tostr(n1, True, True))],
          ["한 변의 길이가 $$수식$${}x`$$/수식$$인 정사각형의 둘레의 길이 $$수식$$y`$$/수식$$".format(tostr(n1, True, True)), \
           '$$수식$$y`=`4`TIMES`{}x`=`{}x$$/수식$$(일차함수)'.format(tostr(n1, True, True), tostr(n1 * 4, True, True))], \
          ["윗변의 길이가 $$수식$${}x`$$/수식$$, 아랫변의 길이가 $$수식$${}`$$/수식$$, 높이가 $$수식$${}`$$/수식$$인 사다리꼴의 넓이 $$수식$$y`$$/수식$$".format( \
           tostr(n5, True, True), n7, n6), \
            '$$수식$$y`=`1 OVER 2`{}`TIMES`{}`#THEREFORE```{}x`{}$$/수식$$(일차함수)'.format(n8, n6, tostr((n6 // 2) * (n3 + n5), True, True), tostr((n6 // 2) * n4, False, False))
          ]]
    del e2[random.randint(0,2)]
    list=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    index=['㈀', '㈁', '㈂', '㈃', '㈄']

    ans =[]
    for i in range(2) :
        temp = random.randint(0,3)
        while temp in ans : temp = random.randint(0,3)
        ans.append(temp)
    ans.sort()

    num = random.randint(0, 5)
    while list[num]==ans : num = random.randint(0, 5)
    ex = []

    index1=0
    index2=0
    for i in range(4):
        if i in ans :
            ex.append(e1[index1])
            index1+=1
        else :
            ex.append(e2[index2])
            index2+=1

    example_list=[]
    ind = 0
    for i in range(6) :
        if i==num : continue
        if list[i]==ans : ans.append(ind)
        example_list.append(index[list[i][0]]+', '+index[list[i][1]])
        ind+=1


    stem = stem.format(e1=ex[0][0], e2=ex[1][0], e3=ex[2][0], e4=ex[3][0], \
                       ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans[2]])
    comment = comment.format(ex1=ex[0][1], ex2=ex[1][1], ex3=ex[2][1], ex4=ex[3][1], c1=index[ans[0]], c2=index[ans[1]])

    return stem, answer, comment


def quadequation313_Stem_009():

    stem = " $$수식$$y`=`{n1}x^2`{n2}`{n3}ax LEFT(1`-`x RIGHT)`$$/수식$$가 이차함수가 되기 위한 상수 $$수식$$a`$$/수식$$의 조건은?\n" \
           "① $$수식$$a`!=`{ex1}$$/수식$$     ② $$수식$$a`!=`{ex2}$$/수식$$     ③ $$수식$$a`!=`{ex3}$$/수식$$     \n④ $$수식$$a`!=`{ex4}$$/수식$$     ⑤ $$수식$$a`!=`{ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{n1}x^2`{n2}`{n3}ax LEFT(1`-`x RIGHT)`=`LEFT({n11}`{c1}a RIGHT)x^2 `{n3}ax`{n4}`$$/수식$$\n" \
              "이 식이 이차함수가 되려면\n" \
              "$$수식$${n11}`{c1}a !=0`$$/수식$$ $$수식$$THEREFORE```a` !=`{c2}`$$/수식$$\n\n"
    n1 = rand_not0(-3, 3)
    n2 = rand_not0(-5, 5)
    n3 = rand_not0(-3, 3)
    c1 = n3*-1
    ans = n1/-c1

    a = (n1 if n1>0 else -n1)
    b = (-c1 if -c1>0 else c1)

    example_list = make_fraction_example2(a, b, b)

    if n1*(-c1)<0 :
        for i in range(1, len(example_list)) :
            example_list[i]='-'+str(example_list[i])


    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, True)
    str_c1 = tostr(c1, False, True)
    str_n4 = tostr(n2, False, False)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3,  \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=str_n4, c1=str_c1, c2=example_list[example_list[0]+1], n11=n1)

    return stem, answer, comment


def quadequation313_Stem_010():

    stem = " $$수식$$y`=`a`LEFT(x^2 `{n1} RIGHT)`{n2}x`{n3}x^2`$$/수식$$이 이차함수가 되도록 하는 상수 $$수식$$a`$$/수식$$의 조건은?\n" \
           "① $$수식$$a`!=`{ex1}$$/수식$$     ② $$수식$$a`!=`{ex2}$$/수식$$     ③ $$수식$$a`!=`{ex3}$$/수식$$     \n④ $$수식$$a`!=`{ex4}$$/수식$$     ⑤ $$수식$$a`!=`{ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`a`LEFT(x^2 `{n1} RIGHT)`{n2}x`{n3}x^2`=`LEFT(a{n5} RIGHT)x^2`{n2}x`{n4}a`$$/수식$$\n" \
              "이 식이 이차함수가 되려면\n" \
              "$$수식$$a`{n5} != 0`$$/수식$$ $$수식$$THEREFORE```a` !=`{c1}$$/수식$$\n\n"
    n1 = rand_not0(-5, 5)
    n2 = rand_not0(-5, 5)
    n3 = rand_not0(-3, 3)
    c1 = -n3

    ans = c1
    example_list = make_example_by_interval(ans, 1)

    str_n1 = tostr(n1, False, False)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, True)
    str_n4 = tostr(n1, False, True)
    str_n5 = tostr(n3, False, False)
    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=str_n4, n5=str_n5, c1=c1)

    return stem, answer, comment

#분수
def quadequation313_Stem_011():

    stem = "다음 중 함수 $$수식$$ y`=`LEFT(x`{n1} RIGHT)^2`{n2}ax^2`{n3}` $$/수식$${proc} 이차함수가 되기 위한 상수 $$수식$$a`$$/수식$$의 값이 될 수 없는 것은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`LEFT(x`{n1} RIGHT)^2`{n2}ax^2`{n3}`=`(1`{n2}a)x^2`{c1}x`{c2}$$/수식$$\n" \
              "이 함수가 이차함수가 되려면\n" \
              "$$수식$$1`{n2}a != 0`$$/수식$$ $$수식$$THEREFORE```a` !=`{c3}$$/수식$$\n\n"
    n1 = rand_not0(-3, 3)
    n2 = rand_not0(-5, 5)
    n3 = rand_not0(-9, 9)
    c1 = 2*n1
    c2 = n1*n1+n3
    c3 = ctr_frac2(1, -n2)
    if c3[1]<0 :
        c3[0]*=-1
        c3[1]*=-1
    example_list = make_example_by_interval(abs(c3[0]), 1)
    for i in range(1, 6) :
        example_list[i] = make_frac(example_list[i]*c3[0], c3[1])
    str_n1 = tostr(n1, False, False)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, False)
    str_c1 = tostr(c1, False, True)
    str_c2 = tostr(c2, False, False)
    str_c3 = make_frac(c3[0], c3[1])

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3,  proc=proc_jo(n3), \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, c1=str_c1, c2=str_c2, c3=str_c3)

    return stem, answer, comment


def quadequation313_Stem_012():

    stem = "$$수식$$ y`=`k LEFT(k`{n1} RIGHT)x^2`{n2}x`{n3}x^2` $$/수식$$이 $$수식$$x`$$/수식$$에 대한 이차함수 일 때, 다음 중 실수 $$수식$$k`$$/수식$$의 값이 " \
           "될 수 없는 것을 모두 고르면? (정답 $$수식$$2`$$/수식$$개)\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}, {a2}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`k LEFT(k`{n1} RIGHT)x^2`{n2}x`{n3}x^2`$$/수식$$\n" \
              "$$수식$$`````=`LEFT(k^2`{c1}k`{c2} RIGHT)x^2`{n2}x`$$/수식$$\n" \
              "이 함수가 이차함수이려면\n" \
              "$$수식$$k^2`{c1}k`{c2} != 0`$$/수식$$, $$수식$$LEFT(k`{c3} RIGHT) LEFT(k`{c4} RIGHT)!=0`$$/수식$$\n" \
              "$$수식$$THEREFORE````k`!=`{k1}`$$/수식$$이고 $$수식$$k`!=`{k2}`$$/수식$$\n\n"

    k1 = rand_not0(-3,3)
    k2 = rand_not0(-3, 3)
    while abs(k2)==abs(k1) or abs(k2-k1)==5: k2 = rand_not0(-3, 3)
    n2 = rand_not0(-5, 5)
    c3 = -k1
    c4 = -k2
    c1 = c3+c4
    c2 = c3*c4
    n1 = c1
    n3 = c2

    str_n1 = tostr(n1, False, False)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, True)
    str_c1 = tostr(c1, False, True)
    str_c2 = tostr(c2, False, False)
    str_c3 = tostr(c3, False, False)
    str_c4 = tostr(c4, False, False)

    inter = 0
    for i in range(3, 0, -1) :
        if abs(k2-k1)%i==0 : inter=i; break

    example_list = make_example_by_interval((k2 if k2<k1 else k1), inter)
    while k1 not in example_list :
        example_list = make_example_by_interval(k2, inter)

    ans=[]
    for i in range(1, 6) :
        if example_list[i]==k1 : ans.append(i-1)
        elif example_list[i]==k2 : ans.append(i-1)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[ans[0]], a2=answer_dict[ans[1]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, c1=str_c1, c2=str_c2, c3=str_c3, c4=str_c4, k1=k1, k2=k2)

    return stem, answer, comment


def quadequation313_Stem_013():

    stem = "이차함수 $$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`{n3}`$$/수식$$에서 $$수식$$ f`LEFT({x1} RIGHT)`$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`{n3} `$$/수식$$이므로\n" \
              "$$수식$$ f`LEFT({x1} RIGHT)`=`{n1} {times1} {x1_}^2 `{n2} {times2} {x1_}`{n3}`=`{c1} $$/수식$$\n\n"

    n1 = rand_not0(-3, 3)
    n2 = rand_not0(-3, 3)
    n3 = rand_not0(-5, 5)
    x1 = random.randint(-2, 2)
    c1 = n1*x1*x1 + n2*x1 + n3

    ans=c1

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, False)

    x1_ = x1 if x1>=0 else 'LEFT(' + str(x1) + 'RIGHT)'

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, x1=x1)
    answer = answer.format(a1=c1)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, x1=x1, x1_=x1_, c1=c1, \
                            times1=('' if n1==1or n1==-1 else 'TIMES'), times2=('' if n2==1 or n2==-1 else 'TIMES'))

    return stem, answer, comment


def quadequation313_Stem_014():

    stem = "이차함수 $$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`{n3}` $$/수식$$에서 $$수식$$ f`LEFT({x1} RIGHT)`-`f`LEFT({x2} RIGHT) `$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`{n3} `$$/수식$$이므로\n" \
              "$$수식$$ f`LEFT({x1} RIGHT)`=`{n1} {times1} {x1_}^2 `{n2} {times2} {x1_}`{n3}`$$/수식$$\n"\
              "{space1}$$수식$$=`{c4}`{c5}`{c6}`=`{c1} `$$/수식$$\n" \
              "$$수식$$ f`LEFT({x2} RIGHT)`=`{n1} {times1} {x2_}^2 `{n2} {times2} {x2_}`{n3}`$$/수식$$\n" \
              "{space2}$$수식$$=`{c7}`{c8}`{c9}`=`{c2} `$$/수식$$\n" \
              "$$수식$$ THEREFORE```f`LEFT({x1} RIGHT)`-`f`LEFT({x2} RIGHT)`=`{c1}`-`{c2_}`=`{c3} `$$/수식$$\n\n"

    out = []
    num = random.randint(-3, 3)
    for i in range(2):
        while num in out:
            num = random.randint(-3, 3)
        out.append(num)
    x1 = out[0]
    x2 = out[1]

    n1 = rand_not0(-3, 3)
    n2 = rand_not0(-7, 7)
    n3 = rand_not0(-9, 9)

    c1 = n1*(x1**2) + n2*x1 + n3
    c2 = n1*(x2**2) + n2*x2 + n3
    c3 = c1-c2

    c4 = tostr(n1 * x1 * x1, True, False, n1)
    c5 = tostr(n2 * x1, False, False, n2)
    c6 = tostr(n3, False, False)
    c7 = tostr(n1 * x2 * x2, True, False, n1)
    c8 = tostr(n2 * x2, False, False, n2)
    c9 = tostr(n3, False, False)

    ans=c3
    example_list = make_example(ans)

    str1 = tostr(n1, True, True)
    str2 = tostr(n2, False, True)
    str3 = tostr(n3, False, False)

    x1_ = x1 if x1>=0 else 'LEFT (' + str(x1) + 'RIGHT )'
    x2_ = x2 if x2>=0 else 'LEFT (' + str(x2) + 'RIGHT )'

    stem = stem.format(n1=str1, n2=str2, n3=str3, x1=x1, x2=x2,  \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str1, n2=str2, n3=str3, x1=x1, x2=x2, x1_=x1_, x2_=x2_, c1=c1, c2=c2, c3=c3, \
                             c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c2_=(c2 if c2>=0 else 'LEFT (' + str(c2) + 'RIGHT )'), \
                             space1=("       " if x1<0 else "     "), space2=("       " if x2<0 else "     "),
                            times1=('' if n1==1 or n1==-1 else 'TIMES'), times2=('' if n2==1 or n2==-1 else 'TIMES'))

    return stem, answer, comment


def quadequation313_Stem_015():

    stem = "이차함수 $$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`{n3}` $$/수식$$에서 $$수식$$ f`LEFT({x1} RIGHT)`TIMES`f`LEFT({x2} RIGHT)` $$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`{n3} `$$/수식$$이므로\n" \
              "$$수식$$ f`LEFT({x1} RIGHT)`=`{n1} {times1} {x1_}^2 `{n2} {times2} {x1_}`{n3}`=`{c1} `$$/수식$$\n" \
              "$$수식$$ f`LEFT({x2} RIGHT)`=`{n1} {times1} {x2_}^2 `{n2} {times2} {x2_}`{n3}`=`{c2} `$$/수식$$\n" \
              "$$수식$$ THEREFORE```f`LEFT({x1} RIGHT)`TIMES`f`LEFT({x2} RIGHT)`=`{c1}`TIMES`{c2}`=`{c3} $$/수식$$\n\n"

    out = []
    num = random.randint(-1, 3)
    for i in range(2):
        while num in out:
            num = random.randint(-1, 3)
        out.append(num)
    x1 = out[0]
    x2 = out[1]

    n1 = rand_not0(-3, 3)
    n2 = rand_not0(-3, 3)
    n3 = rand_not0(-9, 9)

    c1 = n1*(x1**2) + n2*x1 + n3
    c2 = n1*(x2**2) + n2*x2 + n3
    c3 = c1*c2

    ans=c3

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, False)

    x1_ = x1 if x1>=0 else 'LEFT (' + str(x1) + 'RIGHT )'
    x2_ = x2 if x2>=0 else 'LEFT (' + str(x2) + 'RIGHT )'

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, x1=x1, x2=x2)
    answer = answer.format(a1=ans)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, x1=x1, x2=x2, x1_=x1_, x2_=x2_, c1=c1, c2=c2, c3=c3, \
                            times1=('' if n1==1or n1==-1 else 'TIMES'), times2=('' if n2==1 or n2==-1 else 'TIMES'))

    return stem, answer, comment


def quadequation313_Stem_016():

    stem = "이차함수 $$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`{n3}` $$/수식$$에서 $$수식$$ {left}f`LEFT({x1} RIGHT){right}OVER {left}f`LEFT({x2} RIGHT){right} $$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`{n3}` $$/수식$$이므로\n" \
              "$$수식$$ f`LEFT({x1} RIGHT)`=`{n1} {times1} {x1_}^2 `{n2} {times2} {x1_}`{n3}`=`{c1} $$/수식$$\n" \
              "$$수식$$ f`LEFT({x2} RIGHT)`=`{n1} {times1} {x2_}^2 `{n2} {times2} {x2_}`{n3}`=`{c2} $$/수식$$\n" \
              "$$수식$$ THEREFORE```{left}f`LEFT({x1} RIGHT){right} OVER {left}f`LEFT({x2} RIGHT){right}`=`{c1} OVER {c2}`=`{c3} $$/수식$$\n\n"

    out = []
    num = random.randint(-5, 4)
    for i in range(2):
        while num in out:
            num = random.randint(-5, 4)
        out.append(num)
    x1 = out[0]
    x2 = out[1]

    while(True) :
        n1 = rand_not0(-3, 3)
        n2 = rand_not0(-7, 7)
        n3 = rand_not0(-9, 9)
        c1 = n1 * (x1 ** 2) + n2 * x1 + n3
        c2 = n1 * (x2 ** 2) + n2 * x2 + n3
        if abs(c1)<abs(c2) :c1, c2 = c2, c1
        if c2<=1 or c1>=-1 : continue
        elif c1%c2==0 :break

    c3 = int(c1/c2)

    ans=c3

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, False)

    x1_ = x1 if x1>=0 else 'LEFT (' + str(x1) + 'RIGHT )'
    x2_ = x2 if x2>=0 else 'LEFT (' + str(x2) + 'RIGHT )'

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, x1=x1, x2=x2, left='{', right='}')
    answer = answer.format(a1=ans)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, x1=x1, x2=x2, x1_=x1_, x2_=x2_, c1=c1, c2=c2, c3=c3, left='{', right='}', \
                            times1=('' if n1==1or n1==-1 else 'TIMES'), times2=('' if n2==1 or n2==-1 else 'TIMES'))

    return stem, answer, comment


def quadequation313_Stem_017():

    stem = "이차함수 $$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`+`a`$$/수식$$에서 $$수식$$ f`LEFT({x1} RIGHT)`=`{n3}`$$/수식$$일 때, 상수 $$수식$$ a`$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): $$수식$${a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`+`a `$$/수식$$에서 $$수식$$f`LEFT({x1} RIGHT)`=`{n3}`$$/수식$$이므로\n" \
              "$$수식$$ {n1} {times1} {x1_}^2 `{n2} {times2} {x1_}`+`a`=`{n3} `$$/수식$$ $$수식$$ THEREFORE````a`=`{c1} $$/수식$$\n\n"

    n1 = rand_not0(-3, 3)
    n2 = rand_not0(-7, 7)
    n3 = rand_not0(-9, 9)
    x1 = random.randint(-3, 3)
    c1 = n3-n1*x1*x1-n2*x1

    ans=c1
    example_list = make_example(ans)
    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, True)

    x1_ = x1 if x1>=0 else 'LEFT(' + str(x1) + 'RIGHT)'


    stem = stem.format(n1=str_n1, n2=str_n2, n3=n3, x1=x1,  \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=n3, x1=x1, x1_=x1_, c1=c1, \
                             times1=('' if n1 == 1 or n1 == -1 else 'TIMES'), times2=('' if n2 == 1 or n2 == -1 else 'TIMES'))


    return stem, answer, comment


def quadequation313_Stem_018():

    stem = "이차함수 $$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`{n3}`$$/수식$$에서 $$수식$$ f`LEFT(a RIGHT)`=`{n4}`$$/수식$$에서, 정수 $$수식$$ a`$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): $$수식$${a1}`$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}x`{n3}` $$/수식$$에서 $$수식$$f`LEFT(a RIGHT)`=`{n4}`$$/수식$$이므로\n" \
              "$$수식$$ {n1}a^2`{n2}a`{n3}`=`{n4}` $$/수식$$, $$수식$$ {n1}a^2`{n2}a`{c1}`=`0 $$/수식$$\n" \
              "$$수식$$ LEFT({c2}a`{c3} RIGHT) LEFT(a`{c4} RIGHT)`=`0`$$/수식$$     $$수식$$ THEREFORE```a`=`{a1}`$$/수식$$ 또는 $$수식$$a`=`{a2}$$/수식$$\n" \
              "이때  $$수식$$a`$$/수식$$는 정수이므로  $$수식$$a`=`{a2}$$/수식$$\n\n"

    a1 = ctr_frac2(rand_not0(-3, 3), rand_not0(1, 6))
    while abs(a1[0])>=abs(a1[1])  : a1 = ctr_frac2(rand_not0(-3, 3), rand_not0(1, 6))
    a2 = rand_not0(-4, 4)
    while -a1[0]-a2*a1[1]==0 : a2 = rand_not0(-4, 4)

    c2 = a1[1]
    c3 = -a1[0]
    c4 = -a2
    n1 = c2
    n2 = c3+c2*c4
    c1 = c3*c4
    n4 = rand_not0(-3, 3)
    n3 = c1+n4

    ans=a2
    example_list = make_example(ans)
    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, False)
    str_c1 = tostr(c1, False, False)
    str_c2 = tostr(c2, True, True)
    str_c3 = tostr(c3, False, False)
    str_c4 = tostr(c4, False, False)
    str_a1 = make_frac(a1[0], a1[1])


    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, c1=str_c1, c2=str_c2, c3=str_c3, c4=str_c4, a1=str_a1, a2=a2)


    return stem, answer, comment


def quadequation313_Stem_019():

    stem = "이차함수 $$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}ax`{n3} `$$/수식$$에서 $$수식$$ f`LEFT({x1} RIGHT)`=`{n4}` $$/수식$$이고\n" \
           "$$수식$$ f`LEFT({x2} RIGHT)`=`b`$$/수식$$일 때, 상수 $$수식$$ a`$$/수식$$,  $$수식$$b`$$/수식$$에 대하여 $$수식$$a`+`b`$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}ax`{n3} `$$/수식$$에서 $$수식$$ f`LEFT({x1} RIGHT)`=`{n4}` $$/수식$$이므로\n" \
              "$$수식$$ {c4}`{c5}a`{c6}`=`{n4}` $$/수식$$ $$수식$$ THEREFORE````a`=`{c1} $$/수식$$\n" \
              "즉 $$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2c1}x`{n3}` $$/수식$$이므로\n" \
              "$$수식$$ f`LEFT({x2} RIGHT)`=`b`$$/수식$$에서 $$수식$$ b`=`{c7}`{c8}`{c9}`=`{c2}`$$/수식$$\n" \
              "$$수식$$ THEREFORE```a`+`b`=`{c1}`+`{c2_}`=`{c3} $$/수식$$\n\n"

    out = []
    num = rand_not0(-3, 3)
    for i in range(2):
        while num in out:
            num = rand_not0(-3, 3)
        out.append(num)
    x1 = out[0]
    x2 = out[1]

    n1 = rand_not0(-2, 2)
    n2 = rand_not0(-1, 1)
    n3 = rand_not0(-9, 9)
    n4 = rand_not0(-3, 3)
    while (n4-n1*x1*x1-n3) % (n2*x1) != 0 or n4-n1*x1*x1-n3==0 :
        n3 = rand_not0(-9, 9)

    c4 = n1*x1*x1
    c5 = n2*x1
    c6 = n3
    c1 = (n4-c4-c6)//c5
    n2c1 = n2*c1
    c7 = n1*x2*x2
    c8 = n2c1*x2
    c9 = n3
    c2 = c7+c8+c9
    c3 = c1+c2

    ans=c3
    example_list = make_example(ans)
    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, False)
    str_n2c1 = tostr(n2c1, False, True)
    str_c4 = tostr(c4, True, False)
    str_c5 = tostr(c5, False, True)
    str_c6 = tostr(c6, False, False)
    str_c7 = tostr(c7, True, False)
    str_c8 = tostr(c8, False, False)
    str_c9 = tostr(c9, False, False)

    c2_ = c2 if c2>=0 else 'LEFT (' + str(c2) + 'RIGHT )'

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, x1=x1, x2=x2, \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, x1=x1, x2=x2,  c1=c1, c2=c2, c3=c3, c2_=c2_,\
                             c4=str_c4, c5=str_c5, c6=str_c6, c7=str_c7, c8=str_c8, c9=str_c9, n2c1=str_n2c1, \
                            times1=('' if n1==1or n1==-1 else 'TIMES'), times2=('' if n2==1 or n2==-1 else 'TIMES'))

    return stem, answer, comment


def quadequation313_Stem_020():

    stem = "이차함수 $$수식$$ f`LEFT(x RIGHT)`=`{n1}ax^2`{n2}x`{n3}` $$/수식$$에서 $$수식$$ f`LEFT({x1} RIGHT)`=`{n4}` $$/수식$$이고\n" \
           "$$수식$$ f`LEFT({x2} RIGHT)`=`b`$$/수식$$일 때, 상수 $$수식$$ a`$$/수식$$,  $$수식$$b`$$/수식$$에 대하여 $$수식$$b OVER a`$$/수식$$의 값은?\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ f`LEFT(x RIGHT)`=`{n1}ax^2`{n2}x`{n3} `$$/수식$$에서 $$수식$$ f`LEFT({x1} RIGHT)`=`{n4}` $$/수식$$이므로\n" \
              "$$수식$$ {c4}a`{c5}`{c6}`=`{n4}` $$/수식$$ $$수식$$ THEREFORE````a`=`{c1}` $$/수식$$\n" \
              "즉 $$수식$$ f`LEFT(x RIGHT)`=`{n1c1}x^2`{n2}x`{n3}` $$/수식$$이므로\n" \
              "$$수식$$ f`LEFT({x2} RIGHT)`=`b`$$/수식$$에서 $$수식$$ b`=`{c7}`{c8}`{c9}`=`{c2}$$/수식$$\n" \
              "$$수식$$ THEREFORE```b OVER a`=`{c2} OVER {c1}`=`{c3} $$/수식$$\n\n"

    out = []
    num = rand_not0(-3, 3)
    for i in range(2):
        while num in out:
            num = rand_not0(-3, 3)
        out.append(num)
    x1 = out[0]
    x2 = out[1]

    n1 = rand_not0(-1, 1)
    n2 = rand_not0(-3, 3)
    c1 = rand_not0(-4, 4)
    while True :
        n3 = rand_not0(-9, 9)
        n4 = c1*n1*x1*x1+n2*x1+n3
        if (c1*n1*x2*x2+n2*x2+n3)%c1 ==0 : break

    c4 = n1*x1*x1
    c5 = n2*x1
    c6 = n3
    n1c1 = n1*c1
    c7 = n1c1*x2*x2
    c8 = n2*x2
    c9 = n3
    c2 = c7+c8+c9
    c3 = c2//c1

    ans=c3
    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, False)
    str_n1c1 = tostr(n1c1, True, True)
    str_c4 = tostr(c4, True, True)
    str_c5 = tostr(c5, False, False)
    str_c6 = tostr(c6, False, False)
    str_c7 = tostr(c7, True, False)
    str_c8 = tostr(c8, False, False)
    str_c9 = tostr(c9, False, False)


    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, x1=x1, x2=x2)
    answer = answer.format(a1=ans)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, x1=x1, x2=x2,  c1=c1, c2=c2, c3=c3, \
                             c4=str_c4, c5=str_c5, c6=str_c6, c7=str_c7, c8=str_c8, c9=str_c9, n1c1=str_n1c1, \
                            times1=('' if n1==1or n1==-1 else 'TIMES'), times2=('' if n2==1 or n2==-1 else 'TIMES'))

    return stem, answer, comment


def quadequation313_Stem_021():

    stem = "이차함수 $$수식$$ f`LEFT(x RIGHT)`=`{n1}x^2`{n2}ax`{n3}b `$$/수식$$에서 $$수식$$ f`LEFT({x1} RIGHT)`=`{n4} `$$/수식$$이고\n" \
           "$$수식$$ f`LEFT({x2} RIGHT)`=`{n5}`$$/수식$$일 때, 상수 $$수식$$ a`$$/수식$$,  $$수식$$b`$$/수식$$에 대하여 $$수식$$f`LEFT({x3} RIGHT)`$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ f`LEFT(x RIGHT)`={n1}x^2`{n2}ax`{n3}b` $$/수식$$에서 $$수식$$ f`LEFT({x1} RIGHT)`=`{n4} `$$/수식$$이므로\n" \
              "$$수식$$ {c1}`{c2}a`{c3}b`=`{n4}` $$/수식$$\n"\
              "$$수식$$ THEREFORE````{c2_}a`{c3}b`=`{c4}` $$/수식$$ $$수식$$ CDOTS CDOTS㉠ $$/수식$$\n" \
              "$$수식$$ f`LEFT({x2} RIGHT)`=`{n5}` $$/수식$$이므로\n" \
              "$$수식$$ {c5}`{c6}a`{c7}b`=`{n5}` $$/수식$$\n" \
              "$$수식$$ THEREFORE````{c6_}a`{c7}b`=`{c8}` $$/수식$$ $$수식$$ CDOTS CDOTS㉡ $$/수식$$\n" \
              "㉠, ㉡을 연립하여 풀면\n $$수식$$a`=`{a}`$$/수식$$, $$수식$$b`=`{b}`$$/수식$$\n" \
              "따라서 $$수식$$ f`LEFT(x RIGHT)`={n1}x^2`{n2a}x`{n3b}`$$/수식$$\n" \
              "$$수식$$ f`LEFT({x3} RIGHT)`=`{n1}{times1}{x3_}^2`{n2a}{times2}{x3_}`{n3b}`=`{c9} $$/수식$$\n\n"

    out = []
    num = rand_not0(-3, 4)
    for i in range(3):
        while num in out:
            num = rand_not0(-3, 4)
        out.append(num)
    x1 = out[0]
    x2 = out[1]
    x3 = out[2]


    n1 = rand_not0(-2, 2)
    n2 = rand_not0(-1, 1)
    n3 = rand_not0(-1, 1)
    a = rand_not0(-4, 4)
    b = rand_not0(-4, 4)
    n4 = n1*x1*x1+n2*x1*a+n3*b
    n5 = n1*x2*x2+n2*x2*a+n3*b
    c1 = n1*x1*x1
    c2 = n2*x1
    c3 = n3
    c4 = n4-c1
    c5 = n1*x2*x2
    c6 = n2*x2
    c7 = n3
    c8 = n5-c5

    n2a = n2*a
    n3b = n3*b
    c9 = n1*x3*x3+n2a*x3+n3b

    ans=c9
    example_list = make_example(ans)

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, True)
    str_c1 = tostr(c1, True, False)
    str_c2 = tostr(c2, False, True)
    str_c3 = tostr(c3, False, True)
    str_c5 = tostr(c5, True, False)
    str_c6 = tostr(c6, False, True)
    str_c7 = tostr(c7, False, True)
    str_n2a = tostr(n2a, False, True)
    str_n3b = tostr(n3b, False, False)
    str_c2_ = tostr(c2, True, True)
    str_c6_ = tostr(c6, True, True)

    x3_ = x3 if x3>=0 else 'LEFT(' + str(x3) + 'RIGHT)'

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, n5=n5, x1=x1, x2=x2, x3=x3,\
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, n5=n5, x1=x1, x2=x2, x3=x3, c1=str_c1, c2=str_c2, c3=str_c3, \
                             c4=c4, c5=str_c5, c6=str_c6, c7=str_c7, c8=c8, c9=c9, c2_=str_c2_, c6_=str_c6_, n2a=str_n2a, n3b=str_n3b, x3_=x3_, a=a, b=b,\
                            times1=('' if n1==1or n1==-1 else 'TIMES'), times2=('' if n2a==1 or n2a==-1 else 'TIMES'))

    return stem, answer, comment


def quadequation313_Stem_022():

    stem = "$$수식$$ (a^2 `{n1})x ^2 `{n2}(a ^2 `{n3}a`{n4})y ^2 `{n5}x`{n6}y`=`0` $$/수식$$에서\n" \
           "$$수식$$ y`$$/수식$$가 $$수식$$x`$$/수식$$에 대한 이차함수가 되도록 하는 실수 $$수식$$a`$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "(ⅰ) $$수식$$ a^2 `{n1}`!=`0`$$/수식$$이어야 하므로\n" \
              "$$수식$$ a`!=`{a1}`$$/수식$$이고 $$수식$$ a`!=`{a2}`$$/수식$$\n"\
              "(ⅱ) $$수식$$ a^2 `{n3}a`{n4}`=`0`$$/수식$$이어야 하므로\n" \
              "$$수식$$(a`{c1})(a`{c2})`=`0` $$/수식$$ $$수식$$ THEREFORE````a`=`{a1}`$$/수식$$또는 $$수식$$ a`=`{a3}`$$/수식$$\n" \
              "(ⅰ), (ⅱ)에서 $$수식$$ a`=`{a3}$$/수식$$\n\n"


    a1 = rand_not0(-3, 3)
    a2 = -a1
    a3 = rand_not0(-5, 5)
    while a3==a1 or a3==a2 :
        a3 = rand_not0(-5, 5)

    n1 = a1*a2
    n2 = rand_not0(-1, 1)
    n3 = -a1-a3
    n4 = a1*a3
    n5 = rand_not0(-9, 9)
    n6 = rand_not0(-9, 9)
    c1 = -a1
    c2 = -a3

    ans=a3

    str_n1 = tostr(n1, False, False)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, True)
    str_n4 = tostr(n4, False, False)
    str_n5 = tostr(n5, False, True)
    str_n6 = tostr(n6, False, True)
    str_c1 = tostr(c1, False, False)
    str_c2 = tostr(c2, False, False)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=str_n4, n5=str_n5, n6=str_n6)
    answer = answer.format(a1=ans)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=str_n4, n5=str_n5, n6=str_n6,  a1=a1, a2=a2, a3=a3, c1=str_c1, c2=str_c2)

    return stem, answer, comment


def quadequation313_Stem_023():

    stem = "$$수식$$ y`=`ax^2` $$/수식$$의 그래프에 대한 설명으로 옳지 않은 것은?\n" \
           "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{a1} {c1}\n\n"
    rand = [0, 0, 0, 0, 0]
    ans = random.randint(0, 4)
    rand[ans]=1
    n1 = [0, 'a'][rand[0]]
    n2 = ['위', '아래'][rand[1]]
    n3 = ['LEFT(0,``0 RIGHT)', 'LEFT(1,``a RIGHT)'][rand[2]]
    n41 = tostr(random.randint(2, 5), True, True)
    n42 = ['넓다', '좁다'][rand[3]]
    n5 = ['x', 'y'][rand[4]]


    ex = ['축의 방정식은 $$수식$$x`=`{}`$$/수식$$이다.'.format(n1), '$$수식$$a`&lt;`0`$$/수식$$일 때, {}로 볼록하다.'.format(n2),\
         '꼭짓점의 좌표는 $$수식$${}`$$/수식$$이다.'.format(n3), '$$수식$$y`=`{}ax^2`$$/수식$$의 그래프보다 폭이 {}.'.format(n41, n42),\
         '$$수식$$y`=`-ax^2`$$/수식$$의 그래프와 $$수식$${}`$$/수식$$축에 대하여 대칭이다.'.format(n5)]

    n1 = [0, 'a'][0]
    n2 = ['위', '아래'][0]
    n3 = ['LEFT(0,``0 RIGHT)', 'LEFT(1,``a RIGHT)'][0]
    n42 = ['넓다','좁다'][0]
    n5 = ['x', 'y'][0]

    c1 = ['축의 방정식은 $$수식$$x`=`{}`$$/수식$$이다.'.format(n1), '$$수식$$a`&lt;`0`$$/수식$$일 때, {}로 볼록하다.'.format(n2),\
         '꼭짓점의 좌표는 $$수식$${}`$$/수식$$이다.'.format(n3), '$$수식$$y`=`{}ax^2`$$/수식$$의 그래프보다 폭이 {}.'.format(n41, n42),\
         '$$수식$$y`=`-ax^2`$$/수식$$의 그래프와 $$수식$${}`$$/수식$$축에 대하여 대칭이다.'.format(n5)]


    stem = stem.format(ex1=ex[0], ex2=ex[1], ex3=ex[2], ex4=ex[3], ex5=ex[4])
    answer = answer.format(a1=answer_dict[ans])
    comment = comment.format(a1=answer_dict[ans], c1=c1[ans])

    return stem, answer, comment


def quadequation313_Stem_024():

    stem = "이차함수 $$수식$$ y={n1}x^2` $$/수식$$의 그래프가 점 $$수식$$ LEFT({n2}a,``{n3}a RIGHT)`$$/수식$$를 지날 때, " \
           "$$수식$${n4}a`$$/수식$$의 값을 구하시오. (단, $$수식$$ a!=0 `$$/수식$$)\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ y={n1}x^2` $$/수식$$의 그래프가 점 $$수식$$ LEFT({n2}a,``{n3}a RIGHT)`$$/수식$$를 지나므로\n" \
              "$$수식$$ {n3}a`=`{c2}a^2`$$/수식$$, $$수식$$ {c3}a^2`{c1}a`=`0 `$$/수식$$\n"\
              "$$수식$$ {c9}a({c8}a`{c4})`=`0`$$/수식$$  $$수식$$ THEREFORE````a= {sign}`{c5} over {c6}`$$/수식$$ ($$수식$$BECAUSE````a !=0 `$$/수식$$)\n" \
              "$$수식$$ THEREFORE````{n4}a`=`{c7}`$$/수식$$\n\n"

    n1 = rand_not0(-4, 4)
    while True :
        n2 = rand_not0(-2, 2)
        n3 = rand_not0(-2, 2)
        if abs(n1*n2*n2) > 10 : continue
        if n2!=n3 and abs(n1*n2*n2)>=abs(n3) : break

    c1 = n3
    c2 = n2*n1*n2
    c3 = -c2
    c9 = gcd(abs(c3), abs(c1))
    c8 = int(c3/gcd(abs(c3), abs(c1)))
    c4 = int(c1/gcd(abs(c3), abs(c1)))
    c5 = -c4
    c6 = c8
    n4 = c6*(random.randint(1,2))
    while (n4==n2 or n4==n3) and n4>10 :
        n4 = c6 * (random.randint(1, 4))
    c7 = c5*n4//c6
    ans=c7

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, True, True)
    str_n3 = tostr(n3, True, True)
    str_n4 = tostr(n4, True, True)
    str_c1 = tostr(c1, False, True)
    str_c2 = tostr(c2, True, True)
    str_c3 = tostr(c3, True, True)
    str_c4 = tostr(c4, False, False)
    str_c8 = tostr(c8, True, True)
    str_c9 = tostr(c9, True, True)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4 = str_n4)
    answer = answer.format(a1=ans)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=str_n4, c1=str_c1, c2=str_c2, c3=str_c3, c4=str_c4,
                             c5=abs(c5), c6=abs(c6), c7=c7, c8=str_c8, c9=str_c9, sign=('-' if c5*c6<0 else ''))

    return stem, answer, comment


def quadequation313_Stem_025():

    stem = "이차함수 $$수식$$ y`=`ax^2` $$/수식$$의 그래프가 두 점 $$수식$$ LEFT({n1},``{n2} RIGHT)`$$/수식$$, " \
           " $$수식$$ LEFT({n3},``b RIGHT)`$$/수식$$를 지날 때, $$수식$$ a`+`b`$$/수식$$의 값은? (단,  $$수식$$ a`$$/수식$$는 상수)\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "이차함수 $$수식$$y`=`ax^2`$$/수식$$의 그래프가 두 점 $$수식$$ LEFT({n1},``{n2} RIGHT)`$$/수식$$, $$수식$$ LEFT({n3},``b RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$$y`=`ax^2`$$/수식$$에 $$수식$$ x`=`{n1} `$$/수식$$, $$수식$$ y`=`{n2} `$$/수식$${jo1} 대입하면\n"\
              "$$수식$$ {n2}`=`a TIMES{n1_}^2`$$/수식$$, $$수식$$ {n2}`=`{c1}a`$$/수식$$     $$수식$$ THEREFORE````a`=`{a}`$$/수식$$\n" \
              "$$수식$$y`=`{c2}x^2`$$/수식$$에 $$수식$$ x`=`{n3} `$$/수식$$, $$수식$$ y`=`b `$$/수식$$를 대입하면\n" \
              "$$수식$$ b`=`{a} TIMES {n3_}^2`= {b}`$$/수식$$\n" \
              "$$수식$$ THEREFORE````a`+`b`=`{a}`+`{b_}=`{c3}`$$/수식$$\n\n"


    a = rand_not0(-4, 4)
    n1 = rand_not0(-2, 2)
    n2 = n1*n1*a
    n3 = rand_not0(-2, 2)
    while (abs(n1)==abs(n3)) : n3 = rand_not0(-2, 2)
    b = a*n3*n3
    c1 = n1*n1
    c2 = a
    c3 = a+b

    ans = c3
    example_list = make_example(ans)
    str_c1 = tostr(c1, True, True)
    str_c2 = tostr(c2, True, True)

    stem = stem.format(n1=n1, n2=n2, n3=n3, \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5], jo1=proc_jo(n2, 5))
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, n3=n3,  c1=str_c1, c2=str_c2, c3=c3, a=a, b=b, b_=brac(b), n1_=brac(n1), n3_=brac(n3), jo1=proc_jo(n2, 5))

    return stem, answer, comment


def quadequation313_Stem_026():

    stem = "다음 이차함수 중 그래프가 {cond1}로 볼록하면서 폭이 가장 넓은 것은?\n" \
           "① $$수식$$y`=`{n1}x^2$$/수식$$     ② $$수식$$y`=`{n2}x^2$$/수식$$     ③ $$수식$$y`=`{n3}x^2$$/수식$$     \n" \
           "④ $$수식$$y`=`{n4}x^2$$/수식$$     ⑤ $$수식$$y`=`{n5}x^2$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a`$$/수식$$의 부호가 {cond2}수이면서 절댓값의 크기가 가장 작은 것은 {a1}이다.\n\n"

    updown=[["위", "음"], ["아래", "양"]]
    cond = random.randint(0, 1)

    out = []
    if cond==0 :
        num = rand_not0(-4, 3)
        for i in range(5):
            while num in out:
                num = rand_not0(-4, 3)
            out.append(num)
    else :
        num = rand_not0(-3, 4)
        for i in range(5):
            while num in out:
                num = rand_not0(-3, 4)
            out.append(num)

    ans_i=0
    ans = 10
    for i in range(5):
        if cond==0 and out[i]<0 and abs(out[i])<abs(ans) :
            ans_i = i
            ans = out[i]
        elif cond == 1 and out[i] > 0 and abs(out[i]) < abs(ans):
            ans_i = i
            ans = out[i]
        out[i] = tostr(out[i], True, True)

    stem = stem.format(n1=out[0], n2=out[1], n3=out[2], n4=out[3], n5=out[4], cond1=updown[cond][0])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(a1=answer_dict[ans_i], cond2=updown[cond][1])
    return stem, answer, comment


def quadequation313_Stem_027():

    stem = "이차함수 $$수식$$ y`=`ax^2` $$/수식$$의 그래프가 두 점 $$수식$$ LEFT({n1},``{n2} RIGHT)`$$/수식$$, " \
           " $$수식$$ LEFT(b,``{n3} RIGHT)`$$/수식$$를 지날 때, 양수 $$수식$$b`$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`ax^2`$$/수식$$에 $$수식$$ x`=`{n1} `$$/수식$$, $$수식$$ y`=`{n2}` $$/수식$${jo1} 대입하면\n" \
              "$$수식$$ {n2}`=`a TIMES{n1_}^2`$$/수식$$, $$수식$$ {n2}`=`{c1}a`$$/수식$$     $$수식$$ THEREFORE````a`=`{a}`$$/수식$$\n" \
              "$$수식$$y`=`{a}`x^2`$$/수식$$에 $$수식$$ x`=`b `$$/수식$$, $$수식$$ y`=`{n3} `$$/수식$${jo2} 대입하면\n" \
              "$$수식$$ {n3}`=`{a}`b^2`$$/수식$$, $$수식$$ b^2`=`{bb}`$$/수식$$\n" \
              "이때 $$수식$$ b`>`0`$$/수식$$이므로 $$수식$$ b`=`{b}`$$/수식$$\n\n"

    n1 = rand_not0(-3, 3)
    n2 = rand_not0(-6, 6)
    while abs(n2)>=abs(n1*n1):
        n1 = rand_not0(-3, 3)
        n2 = rand_not0(-6, 6)
    frac = ctr_frac2(abs(n2), abs(n1*n1))
    a1 = frac[0]
    a2 = frac[1]
    sign = -1 if n2<0 else 1
    a = tostr(sign, True, True)+'`'+str(a1)+'OVER'+str(a2)
    c1 = n1*n1
    b = a2*random.randint(1, 3)
    while b>10 : b = a2*random.randint(1, 3)
    bb = b*b
    n3 = int(a1*bb//a2)*sign

    ans = b
    example_list = make_example(b)
    str_c1 = tostr(c1, True, True)

    stem = stem.format(n1=n1, n2=n2, n3=n3, \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, n3=n3,  c1=str_c1, a=a, b=b, bb=bb, n1_=brac(n1), jo1=proc_jo(n2), jo2=proc_jo(n3))

    return stem, answer, comment


def quadequation313_Stem_028():

    stem = "보기의 이차함수 중 그래프가 $$수식$$ x` $$/수식$$축에 대하여 대칭인 것끼리 짝지은 것은?\n" \
           "$$표$$\n" \
           "㈀ $$수식$$y`=`{e1}x^2$$/수식$$     ㈁ $$수식$$y`=`{e2}x^2$$/수식$$     \n㈂ $$수식$$y`=`{e3}x^2$$/수식$$     "\
           "㈃ $$수식$$y`=`{e4}x^2$$/수식$$     \n㈄ $$수식$$y`=`{e5}x^2$$/수식$$     ㈅ $$수식$$y`=`{e6}x^2$$/수식$$\n" \
           "$$/표$$\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     \n④ {ex4}     ⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "그래프가 $$수식$$ x` $$/수식$$축에 대하여 대칭이면 $$수식$$ x^2` $$/수식$$의 계수의 절댓값이 같고 부호가 반대이므로 {c1}과 {c2}, {c3}과 {c4}의 그래프가 " \
              "각각 $$수식$$ x` $$/수식$$축에 대하여 대칭이다.\n\n"

    n1 = ctr_frac2(rand_not0(1, 5), 1)
    while n1[1]==n1[0] : n1 = ctr_frac2(rand_not0(1, 5), 1)
    n2 = ctr_frac2(rand_not0(1, 5), rand_not0(1, 5))
    while n1[0] in n2 or n1[1] in n2 or n2[1]<=n2[0]: n2 = ctr_frac2(rand_not0(1, 5), rand_not0(1, 5))

    ex = [[make_frac2(n1[0], n1[1], True, True), 0], [make_frac2(-n1[0], n1[1], True, True), 0],[make_frac2(n2[0], n2[1], True, True), 1], \
          [make_frac2(-n2[0], n2[1], True, True), 1], [make_frac2(n1[1], n1[0], True, True), 2], [make_frac2(-n2[1], n2[0], True, True), 3]]

    index=['㈀', '㈁', '㈂', '㈃', '㈄', '㈅']
    random.shuffle(ex)
    co = [[],[],[],[]]
    for i in range(6):
        if ex[i][1]==0 : co[0].append(i)
        elif ex[i][1]==1 : co[1].append(i)
        elif ex[i][1]==2 : co[2].append(i)
        elif ex[i][1]==3 : co[3].append(i)
    example_list = [[co[0][0], co[0][1]], [co[0][0], co[2][0]], [co[0][1], co[2][0]], [co[1][0], co[3][0]], [co[1][1], co[3][0]]]
    del co[2]
    del co[2]

    for i in example_list :
        i.sort()
    example_list.sort()

    ans_i = example_list.index(co[0])
    ans1 = co[0][0]
    ans2 = co[0][1]
    ans3 = co[1][0]
    ans4 = co[1][1]
    if co[0][0]>co[1][0] :
        ans1, ans3 = co[1][0], co[0][0]
        ans2, ans4 = co[1][1], co[0][1]

    for i in range(5):
        example_list[i] = index[example_list[i][0]]+', '+index[example_list[i][1]]

    stem = stem.format( e1=ex[0][0], e2=ex[1][0], e3=ex[2][0], e4=ex[3][0], e5=ex[4][0], e6=ex[5][0],\
                       ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(c1=index[ans1], c2=index[ans2], c3=index[ans3], c4=index[ans4])

    return stem, answer, comment


def quadequation313_Stem_029():

    stem = "다음 보기의 이차함수 중 그래프를 폭이 가장 넓은 것부터 순서대로 나열한 것은?\n" \
           "$$표$$\n" \
           "㈀ $$수식$$y`=`{e1}x^2$$/수식$$     \n㈁ $$수식$$y`=`{e2}x^2$$/수식$$     \n㈂ $$수식$$y`=`{e3}x^2$$/수식$$     \n"\
           "㈃ $$수식$$y`=`{e4}x^2$$/수식$$     \n" \
           "$$/표$$\n"\
           "① {ex1}     ② {ex2}     \n③ {ex3}     ④ {ex4}     \n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "이차항의 계수의 절댓값이 작을수록 이차함수의 그래프의 폭이 넓다.\n"\
              "따라서 보기의 이차함수에서 이차항의 계수의 절댓값이 작은 것부터 차례로 나열하면 {c1}이다.\n\n"

    ex = [ctr_frac2(rand_not0(-3, -1), rand_not0(2, 6)), ctr_frac2(rand_not0(1, 3), rand_not0(2, 6)), \
          ctr_frac2(rand_not0(-6, -1), 1), ctr_frac2(rand_not0(1, 6), 1)]
    while abs(ex[0][0]/ex[0][1])==abs(ex[1][0]/ex[1][1]) or abs(ex[2][0])==abs(ex[3][0]) or ex[0][1]==1 or ex[1][1]==1:
        ex = [ctr_frac2(rand_not0(-3, -1), rand_not0(1, 6)), ctr_frac2(rand_not0(1, 3), rand_not0(1, 6)), \
              ctr_frac2(rand_not0(-6, -1), 1), ctr_frac2(rand_not0(1, 6), 1)]
    random.shuffle(ex)
    order = [[abs(ex[0][0]/ex[0][1]), 0], [abs(ex[1][0]/ex[1][1]),1], [abs(ex[2][0]/ex[2][1]),2], [abs(ex[3][0]/ex[3][1]),3]]
    order.sort()

    index=['㈀', '㈁', '㈂', '㈃']
    example_list=[[order[0][1], order[1][1], order[2][1], order[3][1]], [order[0][1], order[1][1], order[3][1], order[2][1]],\
                    [order[1][1], order[0][1], order[2][1], order[3][1]], [order[1][1], order[0][1], order[3][1], order[2][1]],\
                    [order[3][1], order[2][1], order[1][1], order[0][1]]]
    example_list.sort()
    ans_i=example_list.index([order[0][1], order[1][1], order[2][1], order[3][1]])

    for i in range(5):
        example_list[i] = index[example_list[i][0]]+', '+index[example_list[i][1]]+', '+index[example_list[i][2]]+', '+index[example_list[i][3]]
        if i==4 : break
        ex[i] = make_frac2(ex[i][0], ex[i][1], True, True)

    stem = stem.format( e1=ex[0], e2=ex[1], e3=ex[2], e4=ex[3],\
                       ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(c1=example_list[ans_i])

    return stem, answer, comment


def quadequation313_Stem_030():

    stem = "이차함수 $$수식$$ y`=`{n0}x^2` $$/수식$$의 그래프에 대한 설명으로 옳은 것은?\n" \
           "{ex1}\n{ex2}\n{ex3}\n{ex4}\n{ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{c1}\n" \
              "{c2}\n" \
              "{c3}\n" \
              "{c4}\n\n"

    n0 = rand_not0(-3, 3)
    rand = ([0, 0, 0, 0, 0] if n0>0 else [1, 1, 1, 0, 1])
    ans = random.randint(0, 4)
    rand[ans]=1-rand[ans]
    n1 = ['$$수식$$3`$$/수식$$, $$수식$$4`$$/수식$$', '$$수식$$1`$$/수식$$, $$수식$$2`$$/수식$$'][rand[0]]
    n2 = ['위','아래'][rand[1]]
    n3 = [' LEQ ',' GEQ '][rand[2]]
    n41 = ctr_frac2(rand_not0(-3, 3), rand_not0(1, 6))
    while abs(n41[0])>=abs(n41[1]) : n41 = ctr_frac2(rand_not0(-3, 3), rand_not0(1, 6))
    n41 = make_frac2(n41[0], n41[1], True, True)
    n42 = ['좁다', '넓다'][rand[3]]
    n5 = ['x^2', 'x'][rand[4]]


    ex = ['① 제 {}사분면을 지난다.'.format(n1), '② {}로 볼록한 포물선이다.'.format(n2),\
         '③ 모든 실수 $$수식$$x`$$/수식$$에 대하여 $$수식$$y {} 0`$$/수식$$이다.'.format(n3), \
          '④ $$수식$$y`=`{}x^2`$$/수식$$의 그래프보다 폭이 {}.'.format(n41, n42),\
         '⑤ $$수식$$x &lt; 0 `$$/수식$$일 때, $$수식$$y`$$/수식$$의 값은 $$수식$${}`$$/수식$$의 값에 정비례한다.'.format(n5)]


    n1 = ['$$수식$$3`$$/수식$$, $$수식$$4`$$/수식$$', '$$수식$$1`$$/수식$$, $$수식$$2`$$/수식$$'][1-rand[0]]
    n2 = ['위','아래'][1-rand[1]]
    n3 = [' LEQ ',' GEQ '][1-rand[2]]
    n42 = ['좁다', '넓다'][1-rand[3]]
    n5 = ['x^2', 'x'][1-rand[4]]

    co = ['① 제 {}사분면을 지난다.'.format(n1), '② {}로 볼록한 포물선이다.'.format(n2), \
          '③ 모든 실수 $$수식$$x`$$/수식$$에 대하여 $$수식$$y {} 0`$$/수식$$이다.'.format(n3),\
          '④ $$수식$$y`=`{}x^2`$$/수식$$의 그래프보다 폭이 {}.'.format(n41, n42), \
          '⑤ $$수식$$x &lt; 0`$$/수식$$일 때, $$수식$$y`$$/수식$$의 값은 $$수식$${}`$$/수식$$의 값에 정비례한다.'.format(n5)]
    del co[ans]

    stem = stem.format(n0=tostr(n0, True, True),ex1=ex[0], ex2=ex[1], ex3=ex[2], ex4=ex[3], ex5=ex[4])
    answer = answer.format(a1=answer_dict[ans])
    comment = comment.format(c1=co[0], c2=co[1], c3=co[2], c4=co[3])

    return stem, answer, comment


def quadequation313_Stem_031():

    stem = "다음 이차함수 중 그래프 중에서 {cond}로 볼록하면서 폭이 가장 넓은 것은?\n" \
           "① $$수식$$y`=`{n1}x^2$$/수식$$     ② $$수식$$y`=`{n2}x^2$$/수식$$     ③ $$수식$$y`=`{n3}x^2$$/수식$$     \n" \
           "④ $$수식$$y`=`{n4}x^2$$/수식$$     ⑤ $$수식$$y`=`{n5}x^2$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "주어진 이차함수의 그래프 중에서 {cond}로 볼록한 것은\n{list}\n" \
              "이 중 이차항의 계수의 절댓값이 가장 작은 것은 $$수식$$y`=`{c1}x^2`$$/수식$$이므로 {cond}로 볼록하면서 " \
              "폭이 가장 넓은 것은 $$수식$$y`=`{c1}x^2`$$/수식$$의 그래프이다.\n\n"

    updown=['위', '아래']
    cond = random.randint(0, 1)
    n= []
    if cond==1 :
        for i in range(5):
            temp = ctr_frac2(rand_not0(2, 6), rand_not0(2, 9))
            while (temp in n): temp = ctr_frac2(rand_not0(2, 9), rand_not0(2, 9))
            n.append(temp)
    else :
        for i in range(5):
            temp = ctr_frac2(rand_not0(-6, -2), rand_not0(2, 9))
            while (temp in n): temp = ctr_frac2(rand_not0(-9, -2), rand_not0(2, 9))
            n.append(temp)

    for i in range(5) : n[i].append(1)
    rand=[]
    for i in range(2) :
        temp = random.randint(0, 4)
        while temp in rand : temp = random.randint(0, 4)
        rand.append(temp)
    n[rand[0]][2]=-1
    n[rand[1]][2]=-1

    min=10
    min_i=0

    str_n = []
    list = []
    for i in range(5) :
        if n[i][2]==-1 : str_n.append(make_frac2(-n[i][0], n[i][1], True, True))
        else :
            str_n.append(make_frac2(n[i][0], n[i][1], True, True))
            list.append('$$수식$$ y`=`'+str_n[i]+'x^2 $$/수식$$')

            if min>abs(n[i][0]/n[i][1]) :
                min=abs(n[i][0]/n[i][1])
                min_i=i

    ans=min_i

    stem = stem.format(n1=str_n[0], n2=str_n[1], n3=str_n[2], n4=str_n[3], n5=str_n[4], cond=updown[cond])
    answer = answer.format(a1=answer_dict[ans])
    comment = comment.format(list=', '.join(list), c1=str_n[ans], cond=updown[cond])
    return stem, answer, comment


def quadequation313_Stem_032():

    stem = "두 이차함수 $$수식$$y`=`{n1}x^2`$$/수식$$, $$수식$$y`=`{n2}x^2`$$/수식$$의 그래프의 공통점을 보기에서 모두 고른 것은?\n" \
           "$$표$$\n" \
           "㈀ {e1}\n㈁ {e2}\n㈂ {e3}\n㈃ {e4}\n" \
           "$$/표$$\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     \n④ {ex4}     ⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{c1} $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프는 {c2}\n"\
              "{c3} $$수식$$y`=`{n2}x^2`$$/수식$$의 그래프는 {c4}\n" \
              "따라서 두 그래프의 공통점은 {a1}이다.\n\n"

    n0 = rand_not0(-5, 5)
    while abs(n0)==1 : n0 = rand_not0(-5, 5)
    rand = (0 if n0>0 else 1)
    n1 = ['위', '아래'][rand]
    n21 = rand_not0(-4, 4)
    while abs(n21)>=abs(n0) : n21 = rand_not0(-4, 4)
    n21 = tostr(n21, True, True)
    n22 = ['넓다', '좁다'][rand]
    n3 = ['은 감소', '도 증가'][rand]
    n4 = ['$$수식$$1`$$/수식$$, $$수식$$2`$$/수식$$', '$$수식$$3`$$/수식$$, $$수식$$4`$$/수식$$'][rand]
    ex = ['$$수식$$y`$$/수식$$축에 대하여 대칭이다.', '꼭짓점의 좌표는 $$수식$$LEFT(0,``0 RIGHT)`$$/수식$$이다.']
    ex_ = ['{}로 볼록하다.'.format(n1), '$$수식$$y`=`{}x^2`$$/수식$$의 그래프보다 폭이 {}.'.format(n21, n22), \
           '$$수식$$x &lt; 0`$$/수식$$일 때, $$수식$$x`$$/수식$$의 값이 증가하면 $$수식$$y`$$/수식$$의 값{}한다.'.format(n3),
           '제 {}사분면을 지난다.'.format(n4)]
    n1 = ['위', '아래'][1-rand]
    n22 = ['넓다', '좁다'][1-rand]
    n3 = ['은 감소', '도 증가'][1-rand]
    n4 = ['$$수식$$1`$$/수식$$, $$수식$$2`$$/수식$$', '$$수식$$3`$$/수식$$, $$수식$$4`$$/수식$$'][1-rand]
    co = ['{}로 볼록하다.'.format(n1), '$$수식$$y`=`{}x^2`$$/수식$$의 그래프보다 폭이 {}.'.format(n21, n22), \
           '$$수식$$x &lt; 0`$$/수식$$일 때, $$수식$$x`$$/수식$$의 값이 증가하면 $$수식$$y`$$/수식$$의 값{}한다.'.format(n3),
           '제 {}사분면을 지난다.'.format(n4)]

    ans = [random.randint(0,1), random.randint(2, 3)]
    ex_[ans[0]]=ex[0]
    ex_[ans[1]]=ex[1]

    list = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    index = ['㈀', '㈁', '㈂', '㈃']
    num = random.randint(0, 5)
    while list[num]==ans : num = random.randint(0, 5)
    del list[num]

    example_list = []
    for i in range(5) :
        example_list.append(index[list[i][0]]+', '+index[list[i][1]])

    ans_i = list.index(ans)

    stem = stem.format(n1=tostr(n0, True, True), n2=(make_frac2(1, -n0, True, True) if n0<0 else make_frac2(-1, n0, True, True)), e1=ex_[0], e2=ex_[1], e3=ex_[2], e4=ex_[3],\
                       ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(n1=tostr(n0, True, True), n2=(make_frac2(1, -n0, True, True) if n0<0 else make_frac2(-1, n0, True, True)), \
                             c1=index[1-ans[0]], c2=co[1-ans[0]], c3=index[5-ans[1]], c4=co[5-ans[1]], a1 = example_list[ans_i] )

    return stem, answer, comment


def quadequation313_Stem_033():

    stem = "이차함수 $$수식$$y`=`ax^2`$$/수식$$의 그래프의 폭은 $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프보다 좁고, $$수식$$y`=`{n2}x^2`$$/수식$$의 그래프보다 " \
           "넓을 때, 양수 $$수식$$a`$$/수식$$값의 범위를 구하시오.\n"
    answer = "(답): $$수식$${a1} &lt; a &lt; {a2}$$수식$$\n"
    comment = "(해설)\n" \
              "(ⅰ) $$수식$$y`=`ax^2`$$/수식$$의 그래프가 $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프보다 폭이 좁으므로 $$수식$$a`$$/수식$$의 절댓값이 " \
              "$$수식$${c1}`$$/수식$$의 절댓값보다 커야한다.\n" \
              "그런데 $$수식$$a &gt; 0`$$/수식$$이므로 $$수식$$a`&gt; {c2}`$$/수식$$\n"\
              "(ⅱ) $$수식$$y`=`ax^2`$$/수식$$의 그래프가 $$수식$$y`=`{n2}x^2`$$/수식$$의 그래프보다 폭이 넓으므로 $$수식$$a`$$/수식$$의 절댓값이 " \
              "$$수식$${c3}`$$/수식$$의 절댓값보다 작아야한다.\n" \
              "그런데 $$수식$$a &gt; 0`$$/수식$$이므로 $$수식$$0 &lt; a`&lt; {c4}`$$/수식$$\n" \
              "따라서 (ⅰ), (ⅱ)에서  $$수식$${c2} &lt; a`&lt; {c4}`$$/수식$$\n\n"

    n1 = rand_not0(-3, 3)
    n2 = rand_not0(-6, 6)
    while abs(n1)>=abs(n2) : n2 = rand_not0(-6, 6)
    c1 = n1
    c2 = abs(n1)
    c3 = n2
    c4 = abs(n2)

    stem = stem.format(n1=tostr(n1, True, True), n2=tostr(n2, True, True))
    answer = answer.format(a1=c2, a2=c4)
    comment = comment.format(n1=tostr(n1, True, True), n2=tostr(n2, True, True), c1=c1, c2=c2, c3=c3, c4=c4)

    return stem, answer, comment


def quadequation313_Stem_034():

    stem = "다음 이차함수의 그래프 중 $$수식$$ y={n6}x^2` $$/수식$$의 그래프와 $$수식$$x`$$/수식$$축에 대하여 서로 대칭인 것은?\n" \
           "① $$수식$$y`=`{n1}x^2$$/수식$$     ② $$수식$$y`=`{n2}x^2$$/수식$$     ③ $$수식$$y`=`{n3}x^2$$/수식$$     \n" \
           "④ $$수식$$y`=`{n4}x^2$$/수식$$     ⑤ $$수식$$y`=`{n5}x^2$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y={n6}x^2 `$$/수식$$의 그래프와 $$수식$$ x`$$/수식$$축에 대하여 서로 대칭인 그래프를 나타내는 이차함수의 식은 $$수식$$ y={c1}x^2 `$$/수식$$이다.\n\n"

    n1, n2 = ctr_frac2(rand_not0(1, 9), rand_not0(1, 9))
    while (n1>=n2) :
        n1, n2 = ctr_frac2(rand_not0(1, 9), rand_not0(1, 9))


    n_q = [n1,n2,1]
    n_a = [n1,n2,-1]
    a_in = 0
    q_in = 0
    n =[[1, n2, 1], [n1, n2, 1], [n1, n2, -1], [n2, n1, 1], [n2, n1, -1]]
    random.shuffle(n)
    str_n = []
    for i in range(5):
        if n[i][2] == -1:
            if n[i][1] == 1:
                str_n.append(tostr(-n[i][0], True, True))
            else:
                str_n.append('-{' + str(n[i][0]) + 'OVER' + str(n[i][1]) + '}')
        else:
            if n[i][1] == 1:
                str_n.append(tostr(n[i][0], True, True))
            else:
                str_n.append('{' + str(n[i][0]) + 'OVER' + str(n[i][1]) + '}')
        if n[i]==n_a : a_in=i
        elif n[i] == n_q: q_in = i


    stem = stem.format(n1=str_n[0], n2=str_n[1], n3=str_n[2], n4 = str_n[3], n5=str_n[4], n6=str_n[q_in])
    answer = answer.format(a1=answer_dict[a_in])
    comment = comment.format(n1=str_n[0], n2=str_n[1], n3=str_n[2], n4 = str_n[3], n5=str_n[4], n6=str_n[q_in], c1=str_n[a_in])

    return stem, answer, comment


def quadequation313_Stem_035():

    stem = "다음 이차함수 $$수식$$ y`=`{n1}x^2` $$/수식$$의 그래프 위의 점이 아닌 것은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n" \
           "④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{a1}$$수식$$ y`=`{n1}x^2 `$$/수식$$에 $$수식$$ x`=`{c1}`$$/수식$$, $$수식$$ y`=`{c2} `$$/수식$${jo1} 대입하면\n" \
              "$$수식$${c2}`!=`{n1}TIMES {c1_}^2`$$/수식$$\n\n"

    n1, n2 = ctr_frac2(rand_not0(1, 6), rand_not0(2, 8))
    while n1>=n2 or abs(n2)==7 or abs(n2)==5 :
        n1, n2 = ctr_frac2(rand_not0(1, 6), rand_not0(2, 8))

    xlist = []
    for i in range(5) :
        rand = random.randint(-6, 6)
        while rand in xlist or -rand in xlist: rand = random.randint(-6, 6)
        xlist.append(rand)

    ylist = []
    for i in range(4) :
        if xlist[i]==0 : ylist.append([0, 1])
        else : ylist.append(ctr_frac2(xlist[i]*xlist[i]*n1, n2))
        ylist[i].append(False)
    ylist.append(ctr_frac2((xlist[4] * xlist[4] * n1)+1, n2))
    ylist[4].append(True)

    jo1_num = ylist[4][0]

    ex=[]
    for i in range(5):
        ex.append([xlist[i]])
        if ylist[i][1] == 1:
            ex[i].append(ylist[i][0])
        else:
            ex[i].append('{' + str(ylist[i][0]) + 'OVER' + str(ylist[i][1]) + '}')
        ex[i].append(ylist[i][2])
    random.shuffle(ex)

    str_ex = []
    ans_i = 0
    for i in range(5):
        str_ex.append("LEFT( " + str(ex[i][0]) + ",``" + str(ex[i][1]) + "RIGHT)" )
        if ex[i][2]==True : ans_i = i



    stem = stem.format(n1='{'+str(n1) + 'OVER' + str(n2) + '}', ex1=str_ex[0], ex2=str_ex[1], ex3=str_ex[2], ex4=str_ex[3], ex5=str_ex[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(a1=answer_dict[ans_i], n1='{'+str(n1) + 'OVER' + str(n2)+'}', c1=ex[ans_i][0], c2=ex[ans_i][1], c1_=brac(ex[ans_i][0]), jo1=proc_jo(jo1_num, 4) )

    return stem, answer, comment


def quadequation313_Stem_036():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2` $$/수식$$의 그래프와  $$수식$$ x`$$/수식$$에 대하여 서로 대칭인 그래프가 " \
           "점 $$수식$$ LEFT(p`,``p{n2} RIGHT)` $$/수식$${jo1} 지날 때, 양수 $$수식$$ p`$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n" \
           "④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{n1}x^2 `$$/수식$$의 그래프와  $$수식$$ x`$$/수식$$에 대하여 서로 대칭인 그래프를 나타내는 이차함수의 식은" \
              "$$수식$$ y`=`{c1}x^2 `$$/수식$$이다.\n $$수식$$ y`=`{c1}x^2 `$$/수식$$의 그래프가 점 $$수식$$ LEFT(p`,``p{n2} RIGHT)` $$/수식$${jo1} 지나므로" \
              "$$수식$$ p{n2}`=`{c1}p^2`$$/수식$$, $$수식$$ {c2}p^2`{c3}p`{c4}`=`0`$$/수식$$\n" \
              "$$수식$$ LEFT(p`{c5} RIGHT) LEFT({c6}p`{c7} RIGHT)`=`0`$$/수식$$ $$수식$$ THEREFORE````p`=`{p1}`$$/수식$$ 또는 $$수식$$ p`=`{p2}`$$/수식$$\n" \
              "그런데  $$수식$$ p`>`0`$$/수식$$이므로 $$수식$$ p`=`{p2}`$$/수식$$\n\n"

    p1 = random.randint(-2, -1)
    p2 = ctr_frac2(random.randint(1, 3), random.randint(1, 3))
    while -p2[0]+(-p1*p2[1])==0 :p2 = ctr_frac2(random.randint(1, 3), random.randint(1, 3))
    c5 = -p1
    c6 = p2[1]
    c7 = -p2[0]
    c2 = c6
    c3 = c7+c5*c6
    c4 = c5*c7
    jo1_num=ctr_frac2(abs(-c4), abs(c3))[0]
    n2 = make_frac(-c4, -c3)
    if c4%c3!=0 :
        if c4*c3>0 : n2='+'+n2
    else : n2=tostr(n2, False, False)
    if c2 % -c3 != 0 :
        c1 = make_frac(c2, -c3)
        n1 = make_frac(c2, c3)
    else :
        c1 = tostr(make_frac(c2, -c3), True, True)
        n1 = tostr(make_frac(c2, c3), True, True)

    if p2[1]==1 : example_list=make_example_by_interval(p2[0],1)
    else : example_list=make_fraction_example(p2[0], p2[1], p2[1])
    str_p2 = make_frac(p2[0], p2[1])
    str_c5 = tostr(c5, False, False)
    str_c6 = tostr(c6, True, True)
    str_c7 = tostr(c7, False, False)
    str_c2 = tostr(c2, True, True)
    str_c3 = tostr(c3, False, True)
    str_c4 = tostr(c4, False, False)


    stem = stem.format(n1=n1, n2=n2, jo1=proc_jo(jo1_num, 5), ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, p1=p1, p2=str_p2, c1=c1, c2=str_c2, c3=str_c3, c4=str_c4, c5=str_c5, c6=str_c6, c7=str_c7, jo1=proc_jo(jo1_num, 5))

    return stem, answer, comment


def quadequation313_Stem_037():

    stem = "이차함수 $$수식$$ y`=`ax^2` $$/수식$$의 그래프가 두 점 $$수식$$ LEFT({n1}`,``{n2} RIGHT)`$$/수식$$, " \
           " $$수식$$ LEFT({n3}`,``b RIGHT)`$$/수식$$를 지날 때, $$수식$$ a`-`b`$$/수식$$의 값은? (단,  $$수식$$ a`$$/수식$$는 상수)\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "이차함수 $$수식$$y`=`ax^2`$$/수식$$의 그래프가 점 $$수식$$ LEFT({n1},``{n2} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$$ {n2}`=`a TIMES{n1_}^2`$$/수식$$, $$수식$$ {c1}a`=`{n2}`$$/수식$$\n" \
              "$$수식$$ THEREFORE````a`=`{a}`$$/수식$$\n" \
              "$$수식$$y`=`{c2}x^2`$$/수식$$의 그래프가 점 $$수식$$ LEFT({n3}`,``b RIGHT)`$$/수식$$를 지나므로\n" \
              "$$수식$$ b`=`{a} TIMES {n3_}^2`= {b}`$$/수식$$\n" \
              "$$수식$$ THEREFORE````a`-`b`=`{a}`-`{b_}=`{c3}`$$/수식$$\n\n"


    a = rand_not0(-4, 4)
    n1 = ctr_frac2(rand_not0(-2, 2),rand_not0(-6, 6))
    while abs(n1[0])>=abs(n1[1]) : n1 = ctr_frac2(rand_not0(-2, 2), rand_not0(-6, 6))
    n2 = ctr_frac2(n1[0]*n1[0]*a, n1[1]*n1[1])
    n3 = rand_not0(-3, 3)
    b = a*n3*n3
    c1 = ctr_frac2(n1[0]*n1[0], n1[1]*n1[1])
    c2 = a
    c3 = a-b

    str_n1=make_frac(n1[0], n1[1])
    str_n2=make_frac(n2[0], n2[1])
    str_c1=make_frac(c1[0], c1[1])
    str_c2=tostr(c2, True, True)
    ans = c3
    example_list = make_example(ans)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=n3, \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=n3,  c1=str_c1, c2=str_c2, c3=c3, a=a, b=b, b_=brac(b), n1_='LEFT (' + str_n1 + 'RIGHT )', n3_=brac(n3), jo1=proc_jo(n2[0], 6))

    return stem, answer, comment


def quadequation313_Stem_038():

    stem = "이차함수 $$수식$$ y`=`ax^2 `$$/수식$$의 그래프가 두 점 $$수식$$ LEFT({n1}`,``{n2} RIGHT)`$$/수식$$, " \
           " $$수식$$LEFT({n3}`,``b RIGHT)`$$/수식$$를 지날 때, $$수식$$b OVER a`$$/수식$$의 값을 구하시오. (단,  $$수식$$ a`$$/수식$$는 상수)\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "이차함수 $$수식$$y`=`ax^2`$$/수식$$의 그래프가 점 $$수식$$LEFT({n1},``{n2} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$${n2}`=`a TIMES{n1_}^2`$$/수식$$, $$수식$${c1}a`=`{n2}`$$/수식$$\n" \
              "$$수식$$THEREFORE````a`=`{a}`$$/수식$$\n" \
              "$$수식$$y`=`{c2}x^2`$$/수식$$의 그래프가 점 $$수식$$LEFT({n3}`,``b RIGHT)`$$/수식$$를 지나므로\n" \
              "$$수식$$b`=`{a} TIMES {n3_}^2`= {b}`$$/수식$$\n" \
              "$$수식$$THEREFORE````b OVER a`=`{b}OVER{a}`=`{c3}`$$/수식$$\n\n"


    a = rand_not0(-4, 4)
    n1 = ctr_frac2(rand_not0(-3, 3),rand_not0(-6, 6))
    while abs(n1[0])>=abs(n1[1]) : n1 = ctr_frac2(rand_not0(-2, 2), rand_not0(-6, 6))
    n2 = ctr_frac2(n1[0]*n1[0]*a, n1[1]*n1[1])
    n3 = rand_not0(-3, 3)
    b = a*n3*n3
    c1 = ctr_frac2(n1[0]*n1[0], n1[1]*n1[1])
    c2 = a
    c3 = make_frac(b, a)

    str_n1=make_frac(n1[0], n1[1])
    str_n2=make_frac(n2[0], n2[1])
    str_c1=make_frac(c1[0], c1[1])
    str_c2=tostr(c2, True, True)
    ans = c3

    stem = stem.format(n1=str_n1, n2=str_n2, n3=n3)
    answer = answer.format(a1=ans)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=n3,  c1=str_c1, c2=str_c2, c3=c3, a=a, b=b, n1_='LEFT (' + str_n1 + 'RIGHT )', n3_=brac(n3), jo1=proc_jo(n2[0], 6))

    return stem, answer, comment


def quadequation313_Stem_039():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2 `$$/수식$$의 그래프와 $$수식$$x`$$/수식$$축에 대하여 대칭인 그래프가 점 $$수식$$LEFT(a`{n2},``a`{n3} RIGHT)`$$/수식$${jo1} " \
           "지날 때, 모든 $$수식$$a`$$/수식$$의 값의 합은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{n1}x^2`$$/수식$$의 그래프가 점 $$수식$$LEFT(a`{n2},``a`{n3} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$$a`{n3}`=`{n1}LEFT(a`{n2} RIGHT)^2`$$/수식$$, $$수식$$a^2`{c1}a`{c2}`=`0`$$/수식$$\n" \
              "$$수식$$LEFT(a`{c3} RIGHT) LEFT(a`{c4} RIGHT)`=`0`$$/수식$$     $$수식$$THEREFORE````a`=`{a1}`$$/수식$$ 또는 $$수식$$a`=`{a2}`$$/수식$$\n" \
              "따라서 모든 $$수식$$a`$$/수식$$의 값의 합은 $$수식$${c5}`$$/수식$$이다.\n\n"

    a1 = rand_not0(-6, 6)
    a2 = rand_not0(-4, 4)
    while abs(a1)==abs(a2) : a2 = rand_not0(-6, 6)
    c3 = -a1
    c4 = -a2
    c1 = c3+c4
    c2 = c3*c4
    n2 = rand_not0(-6, 6)
    while True:
        n2 = rand_not0(-8, 8)
        if  n2*2==c1 : continue
        if (n2*n2-c2)%(n2*2-c1)==0 : break
    n3 = (n2*n2-c2)//(n2*2-c1)
    n1 = ctr_frac2(1, n2*2-c1)
    c5 = a1+a2

    example_list = make_example(c5)
    str_n1 = make_frac2(n1[0], n1[1], True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, False)
    str_c1 = tostr(c1, False, True)
    str_c2 = tostr(c2, False, False)
    str_c3 = tostr(c3, False, False)
    str_c4 = tostr(c4, False, False)
    stem = stem.format(n1=make_frac2(-n1[0], n1[1], True, True), n2=str_n2, n3=str_n3, jo1=proc_jo(n3, 5),\
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3,  c1=str_c1, c2=str_c2, c3=str_c3, c4=str_c4, c5=c5, a1=a1, a2=a2, jo1=proc_jo(n3, 5))

    return stem, answer, comment


def quadequation313_Stem_040():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2 `$$/수식$$의 그래프와 $$수식$$x`$$/수식$$축에 대하여 대칭인 그래프가 점 $$수식$$LEFT(a`{n2},``a`{n3} RIGHT)`$$/수식$${jo1} " \
           "지날 때, 모든 $$수식$$a`$$/수식$$의 값의 곱을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{n1}x^2`$$/수식$$의 그래프가 점 $$수식$$LEFT(a`{n2},``a`{n3} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$$a`{n3}`=`{n1}LEFT(a`{n2} RIGHT)^2`$$/수식$$, $$수식$$a^2`{c1}a`{c2}`=`0`$$/수식$$\n" \
              "$$수식$$LEFT(a`{c3} RIGHT) LEFT(a`{c4} RIGHT)`=`0`$$/수식$$     $$수식$$THEREFORE````a`=`{a1}`$$/수식$$ 또는 $$수식$$a`=`{a2}`$$/수식$$\n" \
              "따라서 근과 계수의 관계에 의해 모든 $$수식$$a`$$/수식$$의 값의 곱은 $$수식$${c5}`$$/수식$$이다.\n\n"

    a1 = rand_not0(-6, 6)
    a2 = rand_not0(-4, 4)
    while abs(a1)==abs(a2) : a2 = rand_not0(-6, 6)
    c3 = -a1
    c4 = -a2
    c1 = c3+c4
    c2 = c3*c4
    n2 = rand_not0(-6, 6)
    while True:
        n2 = rand_not0(-8, 8)
        if  n2*2==c1 : continue
        if (n2*n2-c2)%(n2*2-c1)==0 : break
    n3 = (n2*n2-c2)//(n2*2-c1)
    n1 = ctr_frac2(1, n2*2-c1)
    c5 = a1*a2

    str_n1 = make_frac2(n1[0], n1[1], True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, False)
    str_c1 = tostr(c1, False, True)
    str_c2 = tostr(c2, False, False)
    str_c3 = tostr(c3, False, False)
    str_c4 = tostr(c4, False, False)
    stem = stem.format(n1=make_frac2(-n1[0], n1[1], True, True), n2=str_n2, n3=str_n3, jo1=proc_jo(n3, 5))
    answer = answer.format(a1=c5)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3,  c1=str_c1, c2=str_c2, c3=str_c3, c4=str_c4, c5=c5, a1=a1, a2=a2, jo1=proc_jo(n3, 5))

    return stem, answer, comment


def quadequation313_Stem_041():

    stem = "이차함수 $$수식$$ y`=`{n0}x^2 `$$/수식$$의 그래프에 대한 설명으로 옳은 것은?\n" \
           "{ex1}\n{ex2}\n{ex3}\n{ex4}\n{ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{c1}\n" \
              "{c2}\n" \
              "{c3}\n" \
              "{c4}\n\n"

    n0 = ctr_frac2(rand_not0(-3, 3), rand_not0(1, 6))
    while n0[0]>n0[1] : n0 = ctr_frac2(rand_not0(-3, 3), rand_not0(1, 6))
    rand = ([0, 0, 0, 0, 0] if n0[0]>0 else [1, 0, 1, 0, 1])
    ans = random.randint(0, 4)
    rand[ans]=1-rand[ans]
    n1 = ['위', '아래'][rand[0]]
    n2 = [make_frac2(n0[0], n0[1], True, True), 0][rand[1]]
    n3 = [['$$수식$$3`$$/수식$$', '$$수식$$4`$$/수식$$'], ['$$수식$$1`$$/수식$$', '$$수식$$2`$$/수식$$']][rand[2]]
    n4 = [make_frac2(n0[1], n0[0], True, True), make_frac2(-n0[0], n0[1], True, True)][rand[3]]
    n5 = ['도 증가', '은 감소'][rand[4]]


    ex = ['① {}로 볼록한 포물선이다.'.format(n1), '② 꼭짓점의 좌표는 $$수식$$LEFT(0,``{} RIGHT)`$$/수식$$이다.'.format(n2),\
          '③ 제 {}사분면과 제{}사분면을 지난다.'.format(n3[0], n3[1]), \
          '④ $$수식$$y`=`{}x^2`$$/수식$$의 그래프와 $$수식$$x`$$/수식$$축에 대하여 서로 대칭이다.'.format(n4),\
         '⑤ $$수식$$x &lt; 0`$$/수식$$일 때, $$수식$$x`$$/수식$$의 값이 증가하면 $$수식$$y`$$/수식$$의 값{}한다.'.format(n5)]

    n1 = ['위', '아래'][1-rand[0]]
    n2 = [make_frac2(n0[0], n0[1], True, True), 0][1-rand[1]]
    n3 = [['$$수식$$3`$$/수식$$', '$$수식$$4`$$/수식$$'], ['$$수식$$1`$$/수식$$', '$$수식$$2`$$/수식$$']][1-rand[2]]
    n4 = [make_frac2(n0[1], n0[0], True, True), make_frac2(-n0[0], n0[1], True, True)][1-rand[3]]
    n5 = ['도 증가', '은 감소'][1-rand[4]]

    co = ['① {}로 볼록한 포물선이다.'.format(n1), '② 꼭짓점의 좌표는 $$수식$$LEFT(0,``{} RIGHT)`$$/수식$$이다.'.format(n2), \
          '③ 제 {}사분면과 제{}사분면을 지난다.'.format(n3[0], n3[1]), \
          '④ $$수식$$y`=`{}x^2`$$/수식$$의 그래프와 $$수식$$x`$$/수식$$축에 대하여 서로 대칭이다.'.format(n4), \
          '⑤ $$수식$$x &lt; 0`$$/수식$$일 때, $$수식$$x`$$/수식$$의 값이 증가하면 $$수식$$y`$$/수식$$의 값{}한다.'.format(n5)]
    del co[ans]

    stem = stem.format(n0=make_frac2(n0[0], n0[1], True, True),ex1=ex[0], ex2=ex[1], ex3=ex[2], ex4=ex[3], ex5=ex[4])
    answer = answer.format(a1=answer_dict[ans])
    comment = comment.format(c1=co[0], c2=co[1], c3=co[2], c4=co[3])

    return stem, answer, comment


def quadequation313_Stem_042():

    stem = "다음 보기 중 이차함수 $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프에 대한 설명으로 옳은 것을 모두 고른 것은?\n" \
           "$$표$$\n" \
           "㈀ {e1}\n㈁ {e2}\n㈂ {e3}\n㈃ {e4}\n" \
           "$$/표$$\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     \n④ {ex4}     ⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{c1} {c2}\n"\
              "{c3} {c4}\n" \
              "따라서 옳은 것은 {a1}이다.\n\n"

    n0 = rand_not0(-5, 5)
    while abs(n0)==1 : n0 = rand_not0(-5, 5)
    rand = (0 if n0>0 else 1)
    n1 = ['위', '아래'][rand]
    n21 = rand_not0(-4, 4)
    while abs(n21)>=abs(n0) : n21 = rand_not0(-4, 4)
    n21 = tostr(n21, True, True)
    n22 = ['넓다', '좁다'][rand]
    n3 = ['도 증가','은 감소'][rand]
    n4 = ['$$수식$$3`$$/수식$$, $$수식$$4`$$/수식$$', '$$수식$$1`$$/수식$$, $$수식$$2`$$/수식$$'][rand]
    n5 = ['y', 'x'][1]
    n = rand_not0(-3, 3)
    n6 = [[n, -n*n*n0], [n, n*n*n0]][0]
    ex = ['{}로 볼록하다.'.format(n1), '$$수식$$y`=`{}x^2`$$/수식$$의 그래프보다 폭이 {}.'.format(n21, n22), \
           '$$수식$$x &lt; 0`$$/수식$$일 때, $$수식$$x`$$/수식$$의 값이 증가하면 $$수식$$y`$$/수식$$의 값{}한다.'.format(n3),\
           '제 {}사분면을 지난다.'.format(n4),'$$수식$${}`$$/수식$$축에 대하여 대칭이다.'.format(n5), \
          '점 $$수식$$LEFT({},``{} RIGHT)`$$/수식$${} 지난다.'.format(n6[0], n6[1], proc_jo(n6[1], 5))]

    n1 = ['위', '아래'][1-rand]
    n22 = ['넓다', '좁다'][1-rand]
    n3 = ['도 증가', '은 감소'][1-rand]
    n4 = ['$$수식$$3`$$/수식$$, $$수식$$4`$$/수식$$', '$$수식$$1`$$/수식$$, $$수식$$2`$$/수식$$'][1-rand]
    n5 = ['y', 'x'][0]
    n6 = [[n, -n * n * n0], [n, n * n * n0]][1]
    co = ['{}로 볼록하다.'.format(n1), '$$수식$$y`=`{}x^2`$$/수식$$의 그래프보다 폭이 {}.'.format(n21, n22), \
          '$$수식$$x &lt; 0`$$/수식$$일 때, $$수식$$x`$$/수식$$의 값이 증가하면 $$수식$$y`$$/수식$$의 값{}한다.'.format(n3), \
          '제 {}사분면을 지난다.'.format(n4), '$$수식$${}`$$/수식$$축에 대하여 대칭이다.'.format(n5), \
          '점 $$수식$$LEFT({},``{} RIGHT)`$$/수식$${} 지난다.'.format(n6[0], n6[1], proc_jo(n6[1], 5))]

    de = [random.randint(0, 5), random.randint(0, 4)]
    while de[0]==de[1] : de = [random.randint(0, 5), random.randint(0, 4)]
    del ex[de[0]]
    del ex[de[1]]
    del co[de[0]]
    del co[de[1]]

    ans = [random.randint(0,3), random.randint(0, 3)]
    while ans[0]==ans[1] : ans = [random.randint(0,3), random.randint(0, 3)]
    ex[ans[0]] = co[ans[0]]
    ex[ans[1]] = co[ans[1]]

    list = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    index = ['㈀', '㈁', '㈂', '㈃']
    num = random.randint(0, 5)
    ans.sort()
    while list[num]==ans : num = random.randint(0, 5)
    del list[num]

    example_list = []
    for i in range(5) :
        example_list.append(index[list[i][0]]+', '+index[list[i][1]])

    noans =[]
    for i in range(4):
        if i not in ans : noans.append(i)

    ans_i = list.index(ans)

    stem = stem.format(n1=tostr(n0, True, True), e1=ex[0], e2=ex[1], e3=ex[2], e4=ex[3],\
                       ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(c1=index[noans[0]], c2=co[noans[0]], c3=index[noans[1]], c4=co[noans[1]], a1 = example_list[ans_i] )

    return stem, answer, comment


def quadequation313_Stem_043():

    stem = "다음 보기 중 이차함수의 그래프에 대한 설명으로 옳지 않은 것은?\n" \
           "$$표$$\n" \
           "㈀ $$수식$$y`=`{e1}x^2$$/수식$$\n㈁ $$수식$$y`=`{e2}x^2$$/수식$$\n㈂ $$수식$$y`=`{e3}x^2$$/수식$$\n" \
           "㈃ $$수식$$y`=`{e4}x^2$$/수식$$\n㈄ $$수식$$y`=`{e5}x^2$$/수식$$\n㈅ $$수식$$y`=`{e6}x^2$$/수식$$\n" \
           "$$/표$$\n"\
           "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{c1} {c2}\n\n"


    index = ['㈀', '㈁', '㈂', '㈃', '㈄', '㈅']
    ex = []
    for i in range(3):
        temp = ctr_frac2(rand_not0(-5, 5), 1)
        while [temp[0], 1] in ex or [-temp[0], 1] in ex : temp = ctr_frac2(rand_not0(-5, 5), 1)
        ex.append(temp)
    ex.append(ctr_frac2(-ex[2][1], ex[2][0]))
    temp = ctr_frac2(rand_not0(-3, 3), rand_not0(2, 6))
    while abs(temp[0])>=abs(temp[1]) or temp==ex[3] or abs(temp[0])==1: temp = ctr_frac2(rand_not0(-3, 3), rand_not0(2, 6))
    ex.append(temp)
    ex.append(ctr_frac2(-temp[0],temp[1]))
    random.shuffle(ex)

    order = [[abs(ex[0][0]//ex[0][1]), index[0]], [abs(ex[1][0]//ex[1][1]), index[1]], [abs(ex[2][0]//ex[2][1]),index[2]],\
             [abs(ex[3][0]//ex[3][1]),index[3]], [abs(ex[4][0]//ex[4][1]),index[4]]]
    order.sort()
    sign = [[],[]]
    duo = [[],[]]
    for i in range(6):
        if ex[i][0]*ex[i][1]>0 : sign[0].append(index[i])
        else : sign[1].append(index[i])
        if abs(ex[i][0])!=1 and abs(ex[i][1])!=1 : duo[0].append(index[i])
        elif abs(ex[i][0])==1 and index[i] not in duo[1]:
            for j in range(6):
                if i==j : continue
                if abs(ex[i][1])==abs(ex[j][0]) and abs(ex[i][0])==abs(ex[j][1]):
                    duo[1].append(index[i])
                    duo[1].append(index[j])

    duo[1].sort()
    ans = random.randint(0, 4)
    while ans==1 : ans = random.randint(0, 4)
    rand = [0, 0, 0, 0, 0]
    rand[ans] = 1
    n1 = ['같다', '같지 않다'][rand[0]]
    n3 = [order[4][1], order[random.randint(0, 3)][1]][rand[2]]
    n4 = [', '.join(sign[0]), ', '.join(sign[1])][rand[3]]
    n5 = [duo[0], duo[1]][rand[4]]

    example_list = ['각 그래프의 꼭짓점은 모두 {}.'.format(n1), '축의 방정식은 모두 $$수식$$x`=`0`$$/수식$$이다.', \
           '그래프의 폭이 가장 좁은 것은 {}이다.'.format(n3),\
           '아래로 볼록한 그래프는 {}이다.'.format(n4), \
          '{}과 {}은 $$수식$$x`$$/수식$$축에 대하여 서로 대칭이다.'.format(n5[0], n5[1])]

    rand = 0
    n1 = ['같다', '같지 않다.'][rand]
    n3 = [order[4][1], order[random.randint(0, 3)][1]][rand]
    n4 = [', '.join(sign[0]), ', '.join(sign[1])][rand]
    n5 = [duo[0], duo[1]][rand]
    co = ['각 그래프의 꼭짓점은 모두 {}.'.format(n1), '축의 방정식은 모두 $$수식$$x`=`0`$$/수식$$이다.', \
          '그래프의 폭이 가장 좁은 것은 {}이다.'.format(n3), \
          '아래로 볼록한 그래프는 {}이다.'.format(n4), \
          '{}과 {}은 $$수식$$x`$$/수식$$축에 대하여 서로 대칭이다.'.format(n5[0], n5[1])]

    for i in range(6) :
        ex[i] = make_frac2(ex[i][0], ex[i][1], True, True)

    stem = stem.format(e1=ex[0], e2=ex[1], e3=ex[2], e4=ex[3], e5=ex[4], e6=ex[5],\
                       ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans])
    comment = comment.format(c1=answer_dict[ans], c2=co[ans] )

    return stem, answer, comment


def quadequation313_Stem_044():

    stem = "원점을 꼭짓점으로 하고 $$수식$$ y`$$/수식$$축을 축으로 하는 포물선이 두 점 $$수식$$ LEFT({n1}`,``{n2} RIGHT)`$$/수식$$, " \
           " $$수식$$LEFT(k`,``{n3} RIGHT)`$$/수식$${jo1} 지날 때, 양수 $$수식$$k`$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "포물선의 식을 $$수식$$y`=`ax^2`$$/수식$$으로 놓으면 그래프가 점 $$수식$$LEFT({n1}`,``{n2} RIGHT)`$$/수식$${jo2} 지나므로\n" \
              "$$수식$${n2}`=`a TIMES{n1_}^2`$$/수식$$ $$수식$$THEREFORE````a`=`{a}`$$/수식$$\n" \
              "따라서 $$수식$$y`=`{c1}x^2`$$/수식$$의 그래프가 점 $$수식$$LEFT(k`,``{n3} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$${n3}`=`{c1}k^2`$$/수식$$, $$수식$$k^2`=`{c2}`$$/수식$$\n" \
              "$$수식$$THEREFORE````k`=`{c3} LEFT( `BECAUSE````k>0` RIGHT)`$$/수식$$\n\n"


    a = rand_not0(-4, 4)
    n1 = rand_not0(-3, 3)
    n2 = a*n1*n1
    c1 = a
    c2 = random.randint(2, 12)
    n3 = c2*a

    if make_root(1, c2, False)==make_root(1, c2, True) : c3 = make_root(1, c2, True)
    else : c3 = str(make_root(1, c2, False)) + "`=`"+ str(make_root(1, c2, True))

    example_list = make_example_by_interval_root_ver(c2, 1)

    str_c1 = tostr(c1, True, True)
    stem = stem.format(n1=n1, n2=n2, n3=n3, jo1=proc_jo(n3), ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, n3=n3, jo1=proc_jo(n3, 5), jo2=proc_jo(n2, 5), a=a, c1=str_c1, c2=c2, n1_=brac(n1), c3=c3)

    return stem, answer, comment


def quadequation313_Stem_045():

    stem = "원점을 꼭짓점으로 하고 $$수식$$ y`$$/수식$$축을 축으로 하는 포물선이 두 점 $$수식$$ LEFT({n1}`,``{n2} RIGHT)`$$/수식$$, " \
           " $$수식$$LEFT(k`,``{n3} RIGHT)`$$/수식$${jo1} 지날 때, 음수 $$수식$$p`$$/수식$$의 값은?\n" \
           "① $$수식$$-{ex1}$$/수식$$     ② $$수식$$-{ex2}$$/수식$$     ③ $$수식$$-{ex3}$$/수식$$     \n④ $$수식$$-{ex4}$$/수식$$     ⑤ $$수식$$-{ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "포물선의 식을 $$수식$$y`=`ax^2`$$/수식$$으로 놓으면 그래프가 점 $$수식$$LEFT({n1}`,``{n2} RIGHT)`$$/수식$${jo2} 지나므로\n" \
              "$$수식$${n2}`=`a TIMES{n1_}^2`$$/수식$$ $$수식$$THEREFORE````a`=`{a}`$$/수식$$\n" \
              "따라서 $$수식$$y`=`{c1}x^2`$$/수식$$의 그래프가 점 $$수식$$LEFT(k`,``{n3} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$${n3}`=`{c1}k^2`$$/수식$$, $$수식$$k^2`=`{c2}`$$/수식$$ $$수식$$THEREFORE````p`=`+-{c3}`$$/수식$$\n" \
              "그런데 $$수식$$p`$$/수식$$는 음수이므로 $$수식$$p`=`-{c3}`$$/수식$$\n\n"


    a = rand_not0(-4, 4)
    n1 = rand_not0(-3, 3)
    n2 = a*n1*n1
    c1 = a
    c2 = random.randint(2, 12)
    n3 = c2*a

    c3 = make_root(1, c2, True)

    example_list = make_example_by_interval_root_ver(c2, 1)

    str_c1 = tostr(c1, True, True)
    stem = stem.format(n1=n1, n2=n2, n3=n3, jo1=proc_jo(n3), ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, n3=n3, jo1=proc_jo(n3, 5), jo2=proc_jo(n2, 5), a=a, c1=str_c1, c2=c2, n1_=brac(n1), c3=c3)

    return stem, answer, comment


def quadequation313_Stem_046():

    stem = "원점을 꼭짓점으로 하고 점 $$수식$$ LEFT({n1}`,``{n2} RIGHT) `$$/수식$${jo1} 지나는 포물선을 그래프로 하는 이차함수의 식은?\n" \
           "① $$수식$$y`=`{ex1}x^2$$/수식$$     ② $$수식$$y`=`{ex2}x^2$$/수식$$     ③ $$수식$$y`=`{ex3}x^2$$/수식$$     \n" \
           "④ $$수식$$y`=`{ex4}x^2$$/수식$$     ⑤ $$수식$$y`=`{ex5}x^2$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "그래프의 꼭짓점이 원점이므로 구하는 이차함수의 식을 $$수식$$y`=`ax^2`$$/수식$$으로 놓자.\n" \
              "$$수식$$y`=`ax^2`$$/수식$$의 그래프가 점 $$수식$$ LEFT({n1}`,``{n2} RIGHT) `$$/수식$${jo1} 지나므로\n" \
              "$$수식$${n2}`=`{c1}a`$$/수식$$ $$수식$$THEREFORE````a`=`{a}`$$/수식$$\n" \
              "따라서 구하는 이차함수의 식은 $$수식$$y`=`{c2}x^2`$$/수식$$이다.\n\n"

    a = ctr_frac2(rand_not0(-3, 3), rand_not0(-6, 6))
    n1 = rand_not0(-3, 3)
    n2 = make_frac(a[0]*n1*n1, a[1])
    ex = [[a[0],a[1],1], [-a[0], a[1],-1], [a[1],a[0],-1], [a[1],-a[0],-1],[a[0],a[1]+2,-1]]
    random.shuffle(ex)

    c1 = n1*n1

    ans_i=0
    example_list=[]
    for i in range(len(ex)) :
        if ex[i][2]==1 : ans_i=i
        temp = make_frac(ex[i][0], ex[i][1])
        if type(temp)==int : example_list.append(tostr(temp, True, True))
        else : example_list.append(temp)

    c2 = example_list[ans_i]
    str_a = make_frac(a[0], a[1])


    stem = stem.format(n1=n1, n2=n2, jo1=proc_jo(n2,5), ex1=example_list[0], ex2=example_list[1], ex3=example_list[2],ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(n1=n1, n2=n2, jo1=proc_jo(n2,5), c1=tostr(c1, True, True), c2=c2, a=str_a)
    return stem, answer, comment


def quadequation313_Stem_047():

    stem = "다음 이차함수 중 아래 조건을 모두 만족하는 것은?\n" \
           "$$표$$(가) 그래프의 꼭짓점이 원점이다.\n" \
           "(나) 그래프가 점 $$수식$$ LEFT({n1},``{n2} RIGHT)`$$/수식$${jo1} 지난다.$$/표$$\n" \
           "① $$수식$$y`=`{ex1}x^2$$/수식$$     ② $$수식$$y`=`{ex2}x^2$$/수식$$     ③ $$수식$$y`=`{ex3}x^2$$/수식$$     \n" \
           "④ $$수식$$y`=`{ex4}x^2$$/수식$$     ⑤ $$수식$$y`=`{ex5}x^2$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "그래프의 꼭짓점이 원점이므로 구하는 이차함수의 식을 $$수식$$y`=`ax^2`$$/수식$$으로 놓자.\n" \
              "$$수식$$y`=`ax^2`$$/수식$$에 $$수식$$x`={n1}`$$/수식$$, $$수식$$y`={n2}`$$/수식$${jo1} 대입하면\n" \
              "$$수식$${n2}`=`{c1}a`$$/수식$$     $$수식$$THEREFORE````a`=`{a}`$$/수식$$\n" \
              "따라서 구하는 이차함수의 식은 $$수식$$y`=`{c2}x^2`$$/수식$$이다.\n\n"

    a = ctr_frac2(rand_not0(-3, 3), rand_not0(-6, 6))
    while a[1]+2==0 or a[0]==a[1] or abs(a[1])==1: a = ctr_frac2(rand_not0(-3, 3), rand_not0(-6, 6))
    n1 = rand_not0(-6, 6)
    while n1**2%a[1]!=0 :n1 = rand_not0(-6, 6)
    n2 = make_frac(a[0]*n1*n1, a[1])
    ex = [[a[0],a[1],1], [-a[0], a[1],-1], [a[1],a[0],-1], [a[1],-a[0],-1],[a[0],a[1]+2,-1]]
    random.shuffle(ex)

    c1 = n1*n1

    ans_i=0
    example_list=[]
    for i in range(len(ex)) :
        if ex[i][2]==1 : ans_i=i
        temp = make_frac(ex[i][0], ex[i][1])
        if type(temp)==int : example_list.append(tostr(temp, True, True))
        else : example_list.append(temp)

    c2 = example_list[ans_i]
    str_a = make_frac(a[0], a[1])


    stem = stem.format(n1=n1, n2=n2, jo1=proc_jo(n2,5), ex1=example_list[0], ex2=example_list[1], ex3=example_list[2],ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(n1=n1, n2=n2, jo1=proc_jo(n2,5), c1=tostr(c1, True, True), c2=c2, a=str_a)
    return stem, answer, comment


def quadequation313_Stem_048():

    stem = "다음 중 이차함수 $$수식$$y`=`{n0}ax^2`$$/수식$$의 그래프에 대한 설명으로 옳지 않은 것은?\n" \
           "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{c1} $$수식$$y`=`{n0}ax^2`$$/수식$$의 그래프에서 {c2}{c3}\n\n"

    ans = random.randint(0, 4)
    while ans==3 : ans = random.randint(0, 4)
    n0 = [-1, 1][random.randint(0, 1)]
    rand = ([0, 0, 0, 0, 0] if n0>0 else [1, 0, 0, 1, 1])
    rand[ans] = 1-rand[ans]
    n1 = ['a', '-a'][rand[0]]
    n2 = ['절댓', ''][rand[1]]
    n3 = [[-n0, 'x'], [-n0, 'y']][rand[2]]
    n40 = rand_not0(1, 5)
    n4 = [n40, -n40]
    n5 = [[3, 4], [1, 2]][rand[4]]

    example_list = ['점 $$수식$$LEFT(-1,``{} RIGHT)`$$/수식$$를 지난다.'.format(n1), '$$수식$$a`$$/수식$$의 {}값이 클수록 그래프의 폭이 좁아진다.'.format(n2), \
           '$$수식$$y`=`{}ax^2`$$/수식$$의 그래프와 $$수식$${}`$$/수식$$축에 대하여 서로 대칭이다.'.format(tostr(n3[0], True, True), n3[1]),\
           '$$수식$$x`=`{}`$$/수식$$일 때와 $$수식$$x`=`{}`$$/수식$$일 때의 $$수식$$y`$$/수식$$의 값이 같다.'.format(n4[0], n4[1]), \
          '$$수식$$a &lt; 0`$$/수식$$일 때, 제$$수식$${}`$$/수식$$사분면과 제$$수식$${}`$$/수식$$사분면을 지난다.'.format(n5[0], n5[1])]

    rand = [1-rand[0], 1-rand[1], 1-rand[2], 1-rand[3], 1-rand[4]]
    n1 = ['a', '-a'][rand[0]]
    n2 = ['절댓', ''][rand[1]]
    n3 = [[-n0, 'x'], [-n0, 'y']][rand[2]]
    n5 = [[3, 4], [1, 2]][rand[4]]

    co = ['점 $$수식$$LEFT(-1,``{} RIGHT)`$$/수식$$를 지난다.'.format(n1), '$$수식$$a`$$/수식$$의 {}값이 클수록 그래프의 폭이 좁아진다.'.format(n2), \
        '$$수식$$y`=`{}ax^2$$/수식$$의 그래프와 $$수식$${}`$$/수식$$축에 대하여 서로 대칭이다.'.format(tostr(n3[0], True, True), n3[1]), \
        '$$수식$$x`=`{}`$$/수식$$일 때와 $$수식$$x`=`{}`$$/수식$$일 때의 $$수식$$y`$$/수식$$의 값이 같다.'.format(n4[0], n4[1]), \
        '$$수식$$a &lt; 0`$$/수식$$일 때, 제$$수식$${}`$$/수식$$사분면과 제$$수식$${}`$$/수식$$사분면을 지난다.'.format(n5[0], n5[1])]

    co2=''
    if ans==1 :
        co2='\n즉, $$수식$$ a &gt; 0`$$/수식$$이면 $$수식$$a`$$/수식$$의 값이 클수록 그래프의 폭이 좁아지고, $$수식$$a &lt; 0`$$/수식$$이면 ' \
            '$$수식$$a`$$/수식$$의 값이 작을수록 그래프의 폭이 좁아진다.'

    stem = stem.format(n0=tostr(n0, True, True), ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans])
    comment = comment.format(n0=tostr(n0, True, True),c1=answer_dict[ans], c2=co[ans], c3=co2 )

    return stem, answer, comment


def quadequation313_Stem_049():

    stem = "다음 중 원점을 꼭짓점으로 하고 $$수식$$ y`$$/수식$$축을 축으로 하며 점 $$수식$$ LEFT({n1}`,``{n2} RIGHT)`$$/수식$${jo1} " \
           "지나는 포물선과  $$수식$$ x`$$/수식$$축에 대하여 대칭인 포물선이 지나는 점이 아닌 것은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "포물선의 식을 $$수식$$y`=`ax^2`$$/수식$$으로 놓으면 이 그래프가 점 $$수식$$LEFT({n1}`,``{n2} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$${n2}`=`a TIMES{n1_}^2`$$/수식$$ $$수식$$THEREFORE````a`=`{a}`$$/수식$$\n" \
              "$$수식$$y`=`{c1}x^2`$$/수식$$의 그래프와 점 $$수식$$x`$$/수식$$축에 대하여 대칭인 포물선의 식은 $$수식$$y`=`{c2}x^2`$$/수식$$\n" \
              "따라서 이 포물선이 지나는 점이 아닌 것은 {a1}이다.\n\n"


    a = rand_not0(-3, 3)
    n1 = rand_not0(-2, 2)
    n2 = a*n1*n1
    c1 = a
    c2 = -a

    xlist = []
    for i in range(5) :
        x = ctr_frac2(rand_not0(-3, 3), rand_not0(3,3))
        while [x[0], x[1]] in xlist or [-x[0], -x[1]] in xlist :
            x = ctr_frac2(rand_not0(-3, 3), rand_not0(3, 3))
        xlist.append(x)

    ylist=[]
    for i in range(4) :
        ylist.append(ctr_frac2(xlist[i][0]*xlist[i][0]*-a, xlist[i][1]*xlist[i][1]))
    ylist.append(ctr_frac2(xlist[i][0]*xlist[i][0]*-a, xlist[i][1]+1*xlist[i][1]))

    ex=[]
    for i in range(5) :
        ex.append([xlist[i]])
        ex[i].append(ylist[i])
        ex[i].append(1)
    ex[4][2]=-1
    random.shuffle(ex)

    example_list=[]
    ans_i=0
    for i in range(5) :
        temp = 'LEFT('+str(make_frac(ex[i][0][0], ex[i][0][1]))+'`,``'+str(make_frac(ex[i][1][0], ex[i][1][1]))+' RIGHT)'
        print(ex[i][0], ex[i][1])
        example_list.append(temp)
        if ex[i][2]==-1 : ans_i=i

    str_c1 = tostr(c1, True, True)
    str_c2 = tostr(c2, True, True)

    str_c1 = tostr(c1, True, True)
    stem = stem.format(n1=n1, n2=n2,  jo1=proc_jo(n2, 5), ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(n1=n1, n2=n2, jo1=proc_jo(n2, 5), a=a, c1=str_c1, c2=str_c2, n1_=brac(n1), a1=answer_dict[ans_i])

    return stem, answer, comment


def quadequation313_Stem_050():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2 `$$/수식$$의 그래프 위의 두 점 $$수식$$ LEFT({n2}`,``p RIGHT)`$$/수식$$, " \
           " $$수식$$LEFT(q`,``{n3} RIGHT)`$$/수식$${jo1} 을 지나는 직선의 방정식은? (단,  $$수식$$ q`>`0`$$/수식$$)\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     \n③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     \n⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$p`=`{n1} {times1}{n2_}^2`=`{c1}`$$/수식$$\n" \
              "$$수식$${n3}`=`{c2}q^2`$$/수식$$이므로 $$수식$$q^2`=`{c3}`$$/수식$$ $$수식$$THEREFORE```q`=`{q}`(BECAUSE````q`>`0)`$$/수식$$\n" \
              "두 점 $$수식$$ LEFT({n2}`,``{p} RIGHT)`$$/수식$$, $$수식$$LEFT({q}`,``{n3} RIGHT)`$$/수식$${jo1} 지나는 직선의 기울기는\n" \
              "$$수식$$ {left}{n3}`-`{p_}{right} OVER {left}{q}`-`{n2_}{right}`=`{c4}`$$/수식$$\n" \
              "이므로 직선의 방정식을 $$수식$$y`=`{c5}x`+`b`$$/수식$$로 놓으면 이 직선이 점 $$수식$$ LEFT({n2}`,``{p} RIGHT)`$$/수식$${jo2} 지나므로\n" \
              "$$수식$${p}`=`{c6}`+`b`$$/수식$$ $$수식$$THEREFORE````b`=`{b}`$$/수식$$\n" \
              "$$수식$$THEREFORE````{a1}`$$/수식$$\n\n"

    n1 = ctr_frac2(rand_not0(-2, 2), rand_not0(-4, 4))
    n2 = rand_not0(-4, 4)
    q = rand_not0(6, 9)
    p = n2*n2*n1[0]/n1[1]
    n3 = q*q*n1[0]/n1[1]
    while (n3-p)%(q-n2) !=0 :
        n1 = ctr_frac2(rand_not0(-2, 2), rand_not0(-4, 4))
        n2 = rand_not0(-4, 4)
        while n2**2%n1[1]!=0:  n2 = rand_not0(-4, 4)
        q = rand_not0(6, 9)
        while q**2%n1[1]!=0: q = rand_not0(6, 9)
        p = n2 * n2 * n1[0] / n1[1]
        n3 = q * q * n1[0] / n1[1]

    p = int(p)
    n3 = int(n3)
    c1 = make_frac(n1[0]*n2*n2, n1[1])
    c2 = make_frac(n1[0], n1[1])
    c3 = q * q
    c4 = make_frac(n3 - p, q - n2)
    c5 = c4
    c6 = c4*n2
    b = p-c6

    n1 = make_frac(n1[0], n1[1])
    str_n1 = (tostr(n1, True, True) if type(n1) == int else n1)
    str_c2 = (tostr(c2, True, True) if type(c2) == int else c2)
    str_c5 = tostr(c5, True, True)

    example_list = [[c4, b, 1], [-c4, b, -1], [c4, -b, -1], [-2*c4, b, -1], [2*c4, -b, -1]]
    random.shuffle(example_list)
    ans_i=0
    for i in range(5) :
        if example_list[i][2]==1 : ans_i=i
        coef = tostr(example_list[i][0], True, True)
        num = tostr(example_list[i][1], False, False)
        example_list[i] = "y`=`"+coef+"x`"+num


    stem = stem.format(n1=str_n1, n2=n2, n3=n3, jo1=proc_jo(n3,5), ex1=example_list[0], ex2=example_list[1],ex3=example_list[2],ex4=example_list[3],ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, c1=c1, c2=str_c2, c3=c3, c4=c4, c5=str_c5, c6=c6, b=b, p=p, q=q, p_=brac(p), n2_=brac(n2), \
                             jo1=proc_jo(n2, 6), jo2=proc_jo(p, 5), left='{', right='}', times1=('' if n1==1or n1==-1 else 'TIMES'), a1=example_list[ans_i])

    return stem, answer, comment


def quadequation313_Stem_051():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2 `$$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼 평행이동한 그래프의 꼭짓점의 좌표를 " \
           " $$수식$$LEFT(p`,``q RIGHT)`$$/수식$$, 축의 방정식을 $$수식$$ x`=`m`$$/수식$$이라 할 때, $$수식$$ p`+`q`+`m`$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{c1} `$$/수식$$의 그래프의 꼭짓점의 좌표는" \
              "$$수식$$ LEFT({p}`,``{q} RIGHT)`$$/수식$$이고, 축의 방정식은 $$수식$$x`=`{m}`$$/수식$$이므로\n" \
              "$$수식$$p`=`{p}`$$/수식$$, $$수식$$q`=`{q}`$$/수식$$, $$수식$$m`=`{m}`$$/수식$$\n" \
              "$$수식$$THEREFORE````p`+`q`+`m`=`{c2}`$$/수식$$\n\n"

    n1 = rand_not0(-9, 9)
    n2 = rand_not0(-9, 9)


    c1 = "{n1} LEFT(x`{n2} RIGHT)^2`".format(n1=tostr(n1, True, True), n2=tostr(-n2, False, False))
    p = n2
    q = 0
    m = n2
    c2 = p+q+m



    ans = c2
    example_list = make_example(c2)

    str_n1 = tostr(n1, True, True)

    stem = stem.format(n1=str_n1, n2=n2, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=n2, p=p, q=q, m=m, c1=c1, c2=c2)

    return stem, answer, comment


def quadequation313_Stem_052():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2 `$$/수식$$의 그래프를 $$수식$$ y`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼 평행이동하면 " \
           "점 $$수식$$LEFT({n3}`,``k RIGHT)`$$/수식$$를 지날 때, $$수식$$ k`$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "이차함수 $$수식$$ y`=`{n1}x^2 `$$/수식$$의 그래프를 $$수식$$ y`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼 평행이동한 그래프의 식은\n" \
              "$$수식$$ y`=`{n1}x^2`{c1} `$$/수식$$\n" \
              "이 그래프가 점 $$수식$$LEFT({n3}`,``k RIGHT)`$$/수식$$를 지나므로\n" \
              "$$수식$$ k`=`{n1}{times1}{n3_}^2`{c1}`=`{c2}`$$/수식$$\n\n"

    n1 = rand_not0(-4, 4)
    n2 = ctr_frac2(rand_not0(-4, 4), rand_not0(2, 9))
    n3 = rand_not0(-3, 3)
    c1 = make_frac2(n2[0], n2[1], False, False)
    c2 =[n1*n3*n3*n2[1]+n2[0], n2[1]]


    example_list = make_fraction_example2(c2[0], c2[1], c2[1])

    str_n1 = tostr(n1, True, True)
    str_n2 = make_frac(n2[0], n2[1])
    str_c2 = make_frac2(c2[0], c2[1], True, False)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=n3, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=n3, c1=c1, c2=str_c2, times1=('' if (n1==1 or n1==-1) else 'TIMES'), n3_=brac(n3))

    return stem, answer, comment


def quadequation313_Stem_053():

    stem = "이차함수 $$수식$$ y`=`ax^2 `$$/수식$$의 그래프를 $$수식$$ y`$$/수식$$축의 방향으로 $$수식$${n1}`$$/수식$$만큼 평행이동한 그래프가 " \
           "점 $$수식$$LEFT({n2}`,``{n3} RIGHT)`$$/수식$${jo1} 지날 때, 상수 $$수식$$ a`$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`ax^2`{c1} `$$/수식$$의 그래프가 점 $$수식$$LEFT({n2}`,``{n3} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$$ {n3}`=`a TIMES {n2_}^2`{c1} `$$/수식$$, $$수식$$ {c2}a`=`{c3} `$$/수식$$\n" \
              "$$수식$$ THEREFORE````a`=`{c4}`$$/수식$$\n\n"

    n1 = rand_not0(-9, 9)
    n2 = rand_not0(-4, 4)
    n3 = rand_not0(-20, 20)
    while n3-n1==0 : n3 = rand_not0(-20, 20)
    c1 = n1
    c2 = n2*n2
    c3 = n3-n1
    c4 = [c3, c2]


    example_list = make_fraction_example2(c4[0], c4[1], c4[1])

    str_c1 = tostr(c1, False, False)
    str_c2 = tostr(c2, True, True)
    str_c4 = make_frac(c4[0], c4[1])

    stem = stem.format(n1=n1, n2=n2, n3=n3, jo1=proc_jo(n3, 5), ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, n3=n3, c1=str_c1, c2=str_c2, c3=c3, c4=str_c4, n2_=brac(n2), jo1=proc_jo(n3, 5))

    return stem, answer, comment


def quadequation313_Stem_054():

    stem = "이차함수 $$수식$$ y`=`ax^2`{n1} `$$/수식$$의 그래프를 $$수식$$ y`$$/수식$$축의 방향으로 $$수식$$b`$$/수식$$만큼 평행이동한 그래프를 " \
           "나타내는 이차함수의 식이 $$수식$$ y`=`{n2}x^2`{n3} `$$/수식$$일 때, $$수식$$ a OVER b`$$/수식$$의 값을 구하시오. (단, $$수식$$ a`$$/수식$$는 상수이다.)\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`ax^2`{n1} `$$/수식$$의 그래프를 $$수식$$ y`$$/수식$$축의 방향으로 $$수식$$b`$$/수식$$만큼 평행이동한 그래프의 식은" \
              "$$수식$$ y`=`ax^2`{n1}`+`b `$$/수식$$\n 이 식이 $$수식$$ y`=`{n2}x^2`{n3} `$$/수식$${jo1} 일치하므로\n" \
              "$$수식$$ a`=`{a} `$$/수식$$, $$수식$$ {c1}`+`b`=`{c2} `$$/수식$$, $$수식$$ b`=`{b} `$$/수식$$\n" \
              "$$수식$$ THEREFORE````a OVER b`=`{a}OVER{b}`=`{c3} `$$/수식$$\n\n"

    n1 = rand_not0(-9, 9)
    a = rand_not0(-9, 9)
    b = rand_not0(-9, 9)
    n2 = a
    n3 = n1+b
    c1 = n1
    c2 = n3
    c3 = make_frac(a, b)

    str_n1 = tostr(n1, False, False)
    str_n2 = tostr(n2, True, True)
    str_n3 = tostr(n3, False, False)
    str_c1 = tostr(c1, True, False)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, jo1=proc_jo(n3, 2))
    answer = answer.format(a1=c3)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, c1=str_c1, c2=c2, c3=c3, jo1=proc_jo(n3, 2), a=a, b=b)

    return stem, answer, comment


def quadequation313_Stem_055():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2` $$/수식$$의 그래프를 $$수식$$ y`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼 평행이동한 그래프가 " \
           "두 점 $$수식$$ LEFT(a`,``{n3} RIGHT)`$$/수식$$, $$수식$$ LEFT({n4}`,``b RIGHT)`$$/수식$$를 지난다. $$수식$$ a`&lt;`0 `$$/수식$$일 때, " \
           "$$수식$$ a^2`{sign}`2ab`+`b^2 `$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{n1}x^2` $$/수식$$의 그래프를 $$수식$$ y`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼 평행이동한 그래프의 식은" \
              "$$수식$$ y`=`{n1}x^2`{c1} `$$/수식$$\n 이 그래프가 점 $$수식$$LEFT(a`,``{n3} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$$ {n3}`=`{n1}a^2`{c1} `$$/수식$$, $$수식$$ a^2`={c2} `$$/수식$$\n" \
              "$$수식$$ THEREFORE````a`=`{a}` LEFT(BECAUSE`a`&lt;`0 RIGHT) `$$/수식$$\n" \
              "또, 점 $$수식$$LEFT({n4}`,``b RIGHT)`$$/수식$$를 지나므로" \
              "$$수식$$ b`=`{n1}{times1}{n4_}^2`{c1}`=`{b} `$$/수식$$\n" \
              "$$수식$$ THEREFORE````a^2`{sign}`2ab`+`b^2`=`(a`{sign}`b)^2 `=`({a}`{sign}`{b_})^2`=`{c3} `$$/수식$$\n\n"

    n1 = ctr_frac2(rand_not0(-2, 2), rand_not0(2, 4))
    while n1[1]==3 : n1 = ctr_frac2(rand_not0(-2, 2), rand_not0(2, 4))
    a = rand_not0(-4, 4)
    while a ** 2 % n1[1] != 0: a = rand_not0(-4, 4)
    n2 = rand_not0(-5, 5)
    n3 = make_frac(n1[0]*a*a,n1[1])+n2
    n4 = rand_not0(-6, 6)
    while n4**2%n1[1]!=0 or a==n4: n4 = rand_not0(-4, 4)
    b = make_frac(n1[0]*n4*n4,n1[1])+n2
    c1 = n2
    c2 = a*a

    if (a+b)**2 > (a-b)**2 :
        sign ='-'
        c3 = (a-b)**2
        ans = a-b
    else :
        sign = '+'
        c3 = (a+b)**2
        ans = a+b

    example_list=make_example_by_interval(abs(ans), 1)
    while -1 in example_list : example_list=make_example_by_interval(ans, 1)

    for i in range(1, 6):
        example_list[i]*=example_list[i]

    str_n1 = make_frac2(n1[0], n1[1], True, True)
    str_c1 = tostr(c1, False, False)
    n1 = make_frac(n1[0], n1[1])

    stem = stem.format(n1=str_n1, n2=n2, n3=n3, n4=n4, sign=sign, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, n4=n4, c1=str_c1, c2=c2, c3=c3, jo1=proc_jo(n3,5), a=a, b=b, n4_=brac(n4), \
                             b_=brac(b), sign=sign, times1=('' if n1==1 or n1==-1 else 'TIMES'))

    return stem, answer, comment


def quadequation313_Stem_056():

    stem = "이차함수 $$수식$$ y`=`ax^2`{n1} `$$/수식$$의 그래프를 $$수식$$ y`$$/수식$$축의 방향으로 $$수식$$b`$$/수식$$만큼 평행이동한 그래프를 " \
           "나타내는 이차함수의 식이 $$수식$$ y`=`{n2}x^2`{n3} `$$/수식$$일 때, $$수식$$ a`-`b`$$/수식$$의 값을 구하시오. (단, $$수식$$ a`$$/수식$$는 상수이다.)\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`ax^2`{n1} `$$/수식$$의 그래프를 $$수식$$ y`$$/수식$$축의 방향으로 $$수식$$b`$$/수식$$만큼 평행이동한 그래프의 식은" \
              "$$수식$$ y`=`ax^2`{n1}`+`b `$$/수식$$\n 이 식이 $$수식$$ y`=`{n2}x^2`{n3} `$$/수식$${jo1} 일치하므로\n" \
              "$$수식$$ a`=`{a} `$$/수식$$, $$수식$$ {c1}`+`b`=`{c2} `$$/수식$$에서 $$수식$$ b`=`{b} `$$/수식$$\n" \
              "$$수식$$ THEREFORE````a`-`b`=`{a}`-`{b_}`=`{c3} `$$/수식$$\n\n"

    n1 = rand_not0(-9, 9)
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)
    while n1==n3 : n3 = rand_not0(-9, 9)
    a = n2
    b = n3-n1
    c1 = n1
    c2 = n3
    c3 = a-b

    example_list = make_example(c3)
    str_n1 = tostr(n1, False, False)
    str_n2 = tostr(n2, True, True)
    str_n3 = tostr(n3, False, False)
    str_c1 = tostr(c1, True, False)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, jo1=proc_jo(n3, 2), ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, c1=str_c1, c2=c2, c3=c3, jo1=proc_jo(n3, 2), a=a, b=b, b_=brac(b))

    return stem, answer, comment


def quadequation313_Stem_057():

    stem = "이차함수 $$수식$$ y`=`{n0}x^2`{n00}`$$/수식$$의 그래프에 대한 설명으로 옳지 않은 것은?\n" \
           "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{c1} {c2}\n\n"

    n0 = ctr_frac2(rand_not0(-4, 4), rand_not0(1, 6))
    while abs(n0[0])>=abs(n0[1]) : n0 = ctr_frac2(rand_not0(-4, 4), rand_not0(1, 6))
    n00 = (rand_not0(-8, -1) if n0[0]<0 else rand_not0(1, 8))
    s = (0 if n0[0]<0 else 1)
    rand = ([0, 0, 0, 0, 0, 0, 0] if n0[0]<0 else [1, 0, 0, 0, 0, 0, 1])
    ans = random.randint(0, 6)
    rand[ans]=1-rand[ans]
    n1 = ['위', '아래'][rand[0]]
    n2 = [n00, -n00][rand[1]]
    n3 = ['넓다', '좁다'][rand[2]]
    n4 = ['y','x'][rand[3]]
    sign = [' LEQ ', ' GEQ '][s]
    n5 = [[sign, n00],[sign, -n00]][rand[4]]
    n6 = [n00, -n00][rand[5]]
    n7 = [[3, 4], [1, 2]][rand[6]]

    ex = ['{}로 볼록한 포물선이다.'.format(n1), '꼭짓점의 좌표는 $$수식$$LEFT(0,``{} RIGHT)`$$/수식$$이다.'.format(n2),\
          '$$수식$$y`=`x^2`$$/수식$$보다 폭이 {}.'.format(n3), \
          '$$수식$${}`$$/수식$$축에 대하여 대칭이다.'.format(n4),\
         '$$수식$$y`$$/수식$$값의 범위는 $$수식$$y {} {}`$$/수식$$이다.'.format(n5[0], str(n5[1])),\
          '$$수식$$ y`=`{}x^2`$$/수식$$의 그래프를 $$수식$$y`$$/수식$$축의 방향으로 $$수식$${}`$$/수식$$만큼 평행이동한 것이다.'.format(make_frac2(n0[0], n0[1], True, True), n6),\
          '제$$수식$${}`$$/수식$$, $$수식$${}`$$/수식$$사분면을 지난다.'.format(n7[0], n7[1])]

    n1 = ['위', '아래'][1-rand[0]]
    n2 = [n00, -n00][1-rand[1]]
    n3 = ['넓다', '좁다'][1-rand[2]]
    n4 = ['y', 'x'][1-rand[3]]
    n5 = [[sign, n00], [sign, -n00]][1-rand[4]]
    n6 = [n00, -n00][1-rand[5]]
    n7 = [[3, 4], [1, 2]][1-rand[6]]

    co = ['{}로 볼록한 포물선이다.'.format(n1), '꼭짓점의 좌표는 $$수식$$LEFT(0,``{} RIGHT)`$$/수식$$이다.'.format(n2), \
          '$$수식$$y`=`x^2`$$/수식$$보다 폭이 {}.'.format(n3), \
          '$$수식$${}`$$/수식$$축에 대하여 대칭이다.'.format(n4), \
          '$$수식$$y`$$/수식$$값의 범위는 $$수식$$y {} {}`$$/수식$$이다.'.format(n5[0], str(n5[1])), \
          '$$수식$$ y`=`{}x^2`$$/수식$$의 그래프를 $$수식$$y`$$/수식$$축의 방향으로 $$수식$${}`$$/수식$$만큼 평행이동한 것이다.'.format(make_frac2(n0[0], n0[1], True, True), n6), \
          '제$$수식$${}`$$/수식$$, $$수식$${}`$$/수식$$사분면을 지난다.'.format(n7[0], n7[1])]

    de=[random.randint(0, 6), random.randint(0, 5)]
    while ans in de or de[1]==ans-1 : de=[random.randint(0, 6), random.randint(0, 5)]
    del ex[de[0]]
    del co[de[0]]
    del ex[de[1]]
    del co[de[1]]
    if de[0]<ans : ans-=1
    if de[1]<ans : ans-=1

    stem = stem.format(n0=make_frac2(n0[0], n0[1], True, True), n00=tostr(n00, False, False), ex1=ex[0], ex2=ex[1], ex3=ex[2], ex4=ex[3], ex5=ex[4])
    answer = answer.format(a1=answer_dict[ans])
    comment = comment.format(c1=answer_dict[ans], c2=co[ans])

    return stem, answer, comment


def quadequation313_Stem_058():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2`q` $$/수식$$의 그래프가 $$수식$$ LEFT({n2}`,``{n3} RIGHT) `$$/수식$${jo1} 지날 때, 꼭짓점의 좌표는?" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{n1}x^2`q` $$/수식$$의 그래프가 $$수식$$ LEFT({n2}`,``{n3} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$$ {n3}`=`{n1}{times1}{n2_}^2`+`q `$$/수식$$ $$수식$$ THEREFORE````q`=`{q} `$$/수식$$\n" \
              "따라서 $$수식$$ y`=`{n1}x^2`{c1}` $$/수식$$의 그래프의 꼭짓점의 좌표는\n" \
              "$$수식$$ LEFT( 0`,``{q} RIGHT)` $$/수식$$이다.\n\n"

    n1 = rand_not0(-5, 5)
    q = rand_not0(-9, 9)
    while n1==q : q = rand_not0(-9, 9)
    n2 = rand_not0(-3, 3)
    n3 = n1*n2*n2+q
    c1 = q

    example_list = [q, -q, n1, -n1, 0]
    random.shuffle(example_list)

    ans_i = 0
    for i in range(5):
        if example_list==q : ans_i=i
        example_list[i]= 'LEFT(0`,``'+str(example_list[i])+'RIGHT)'

    str_n1 = tostr(n1, True, True)
    str_c1 = tostr(c1, False, False)

    stem = stem.format(n1=str_n1, n2=n2, n3=n3, jo1=proc_jo(n3,5), ex1=example_list[0], ex2=example_list[1],ex3=example_list[2],ex4=example_list[3],ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, c1=str_c1, q=q, times1=('' if n1==1or n1==-1 else 'TIMES'), n2_=brac(n2), jo1=proc_jo(n3,5))

    return stem, answer, comment


def quadequation313_Stem_059():

    stem = "이차함수 $$수식$$y`=`{n1}ax^2`{n2}q`$$/수식$$의 그래프에 대한 설명으로 옳은 것을 모두 고른 것은?\n" \
           "$$표$$\n" \
           "㈀ {e1}\n㈁ {e2}\n㈂ {e3}\n㈃ {e4}\n" \
           "$$/표$$\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     \n④ {ex4}     ⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{c1} {c2}\n"\
              "{c3} {c4}\n" \
              "따라서 옳은 것은 {a1}이다.\n\n"

    n0 = [1, -1][random.randint(0, 1)]
    rand = (0 if n0>0 else 1)
    n1 = ['위', '아래'][rand]
    n2 = [[n0, -n0],[n0, n0]][0]
    sign = ['&gt;', '&lt;']
    n3 = [[sign[rand], n0, '크'], [sign[rand], n0,'크거나 같']][0]
    n5 = [[-n0, n0], [-n0, -n0]][0]
    n6 = [-n0, n0][0]
    ex = ['$$수식$$a &gt; 0`$$/수식$$일 때, {}로 볼록하다.'.format(n1), \
          '이차함수 $$수식$$y`=`{}ax^2`$$/수식$$의 그래프를 $$수식$$x`$$/수식$$축의 방향으로 $$수식$${}q`$$/수식$$만큼 평행이동한 것이다.'.format(tostr(n2[0], True, True), tostr(n2[1], True, True)), \
           '$$수식$$a {} 0`$$/수식$$일 때, 모든 $$수식$$y`$$/수식$$의 값은 $$수식$${}q`$$/수식$$보다 {}다.'.format(n3[0], tostr(n3[1], True, True), n3[2]),\
           '이차함수 $$수식$$y`=`{}ax^2`{}q`$$/수식$$의 그래프와 $$수식$$x`$$/수식$$축에 대하여 대칭이다.'.format(tostr(n5[0], True, True), tostr(n5[1], False, True)), \
          '꼭짓점의 좌표는 $$수식$$LEFT(0,``{}q RIGHT)`$$/수식$$이다.'.format(tostr(n6,True, True))]

    n1 = ['위', '아래'][1-rand]
    n2 = [[n0, -n0], [n0, n0]][1]
    n3 = [[sign[rand], n0, '크'], [sign[rand], n0,'크거나 같']][1]
    n5 = [[-n0, n0], [-n0, -n0]][1]
    n6 = [0, n0][1]
    co = ['$$수식$$a &gt; 0`$$/수식$$일 때, {}로 볼록하다.'.format(n1), \
          '이차함수 $$수식$$y`=`{}ax^2`$$/수식$$의 그래프를 $$수식$$x`$$/수식$$축의 방향으로 $$수식$${}q`$$/수식$$만큼 평행이동한 것이다.'.format(tostr(n2[0], True, True), tostr(n2[1], True, True)), \
           '$$수식$$a {} 0`$$/수식$$일 때, 모든 $$수식$$y`$$/수식$$의 값은 $$수식$${}q`$$/수식$$보다 {}다.'.format(n3[0], tostr(n3[1], True, True), n3[2]),\
           '이차함수 $$수식$$y`=`{}ax^2`{}q`$$/수식$$의 그래프와 $$수식$$x`$$/수식$$축에 대하여 대칭이다.'.format(tostr(n5[0], True, True), tostr(n5[1], False, True)), \
          '꼭짓점의 좌표는 $$수식$$LEFT(0,``{}q RIGHT)`$$/수식$$이다.'.format(tostr(n6,True, True))]

    de = random.randint(0, 4)
    del ex[de]
    del co[de]

    ans = [random.randint(0,3), random.randint(0, 3)]
    while ans[0]==ans[1] : ans = [random.randint(0,3), random.randint(0, 3)]
    ex[ans[0]] = co[ans[0]]
    ex[ans[1]] = co[ans[1]]

    list = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    index = ['㈀', '㈁', '㈂', '㈃']
    num = random.randint(0, 5)
    ans.sort()
    while list[num]==ans : num = random.randint(0, 5)
    del list[num]

    example_list = []
    for i in range(5) :
        example_list.append(index[list[i][0]]+', '+index[list[i][1]])

    noans =[]
    for i in range(4):
        if i not in ans : noans.append(i)

    ans_i = list.index(ans)

    stem = stem.format(n1=tostr(n0, True, True), n2=tostr(n0, False, True), e1=ex[0], e2=ex[1], e3=ex[2], e4=ex[3],\
                       ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(c1=index[noans[0]], c2=co[noans[0]], c3=index[noans[1]], c4=co[noans[1]], a1 = example_list[ans_i] )

    return stem, answer, comment


def quadequation313_Stem_060():

    stem = "다음 조건을 모두 만족시키는 이차함수의 식은?\n" \
           "$$표$$ (가) 점 $$수식$$ LEFT(0`,``{n1} RIGHT)`$$/수식$${jo1} 꼭짓점으로 한다.\n" \
           "(나) 평행이동하면  $$수식$$ y`=`{n2}x^2`$$/수식$$의 그래프와 포개어진다. $$/표$$\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     \n③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     \n⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "(가)에서 그래프의 꼭짓점의 좌표가 $$수식$$ LEFT(0`,``{n1} RIGHT)`$$/수식$$이므로 이차함수의 식을 $$수식$$ y`=`ax^2`{c1}`$$/수식$$으로 놓을 수 있다.\n" \
              "(나)에서 $$수식$$ y`=`ax^2`{c1}`$$/수식$$의 그래프가 평행이동에 의해 $$수식$$ y`=`{n2}x^2`$$/수식$$의 그래프와 포개어지므로 $$수식$$ a`=`{c2}`$$/수식$$\n" \
              "따라서 구하는 이차함수의 식은 $$수식$$ y`=`{n2}x^2`{c1}`$$/수식$$\n\n"

    n1 = rand_not0(-9, 9)
    n2 = rand_not0(-9, 9)
    c1 = n1
    c2 = n2

    str_n1 = tostr(n1, False, False)
    str_n2 = tostr(n2, True, True)
    str_c1 = tostr(c1, False, False)

    example_list = [[tostr(n1, True, True)+'x^2', -1], [str_n2+'x^2`'+str_n1, 1], [tostr(-n2, True, True)+'x^2`'+str_n1, -1], \
                    [str_n2+'(x`'+tostr(-n1, False, False)+')^2', -1], [tostr(-n2, True, True)+'(x`'+tostr(-n1, False, False)+')^2', -1]]
    random.shuffle(example_list)

    ans_i = 0
    for i in range(5):
        if example_list[i][1]==1 : ans_i=i
        example_list[i]= 'y`=`'+example_list[i][0]

    stem = stem.format(n1=n1, n2=str_n2, jo1=proc_jo(n1,5), ex1=example_list[0], ex2=example_list[1],ex3=example_list[2],ex4=example_list[3],ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(n1=n1, n2=str_n2,c1=str_c1, c2=c2)

    return stem, answer, comment


def quadequation313_Stem_061():

    stem = "이차함수 $$수식$$ y`=`LEFT({n1}`k`{n2} RIGHT)x^2`{n3}k`{n4} `$$/수식$$에서 모든 그래프가 $$수식$$ x`$$/수식$$의 값에 대하여" \
           "$$수식$$ y`$$/수식$$의 값이 음수가 되도록 하는 모든 정수 $$수식$$ k`$$/수식$$의 합은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`LEFT({n1}`k`{n2} RIGHT)x^2`{n3}k`{n4} `$$/수식$$에서 모든 $$수식$$ x`$$/수식$$의 값에 대하여 $$수식$$ y`$$/수식$$의 " \
              "값이 음수이려면 그래프가 위로 볼록해야 하므로\n" \
              "$$수식$$ {n1}`k`{n2}`&lt;`0 `$$/수식$$    $$수식$$ THEREFORE````k`&lt;`{c1} `$$/수식$$         $$수식$$CDOTS CDOTS㉠`$$/수식$$\n" \
              "또 꼭짓점의 $$수식$$ y`$$/수식$$좌표가 음수이어야 하므로\n" \
              "$$수식$$ {c3}k`{n4}`&lt;`0 `$$/수식$$    $$수식$$ THEREFORE````k`&gt;`{c2} `$$/수식$$         $$수식$$CDOTS CDOTS㉡`$$/수식$$\n" \
              "㉠, ㉡을 모두 만족시키는 정수 $$수식$$ k`$$/수식$$는 {k1} 이므로 구하는 합은\n" \
              "$$수식$${k2}`=`{c4}`$$/수식$$\n\n"

    n1 = rand_not0(1, 6)
    n2 = rand_not0(-3, 3)
    c1 = ctr_frac2(-n2, n1)
    n3 = rand_not0(-9, -1)
    n4 = rand_not0(-6, 6)
    while c1[0]//c1[1]-2<= -n4//n3 :
        n3 = rand_not0(-9, -1)
        n4 = rand_not0(-6, 6)
    c2 = ctr_frac2(-n4, n3)
    c3 = n3

    k1=[]
    k2=[]
    c4=0
    ran1 = (math.floor(c2[0]/c2[1]) if c2[0]%c2[1]!=0 else c2[0]//c2[1]+1)
    ran2 = (math.floor(c1[0]/c1[1])+1 if c1[0]%c1[1]!=0 else c1[0]//c1[1])

    for i in range(ran1, ran2):
        k2.append(brac(i))
        k1.append("$$수식$$"+str(i)+"`$$/수식$$")
        c4+=i

    k1 = ', '.join(k1)
    k2 = '`+`'.join(k2)

    ans=c2
    example_list = make_example(c4)

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, True)
    str_n4 = tostr(n4, False, False)
    str_c1 = make_frac(c1[0], c1[1])
    str_c2 = make_frac(c2[0], c2[1])
    str_c3 = tostr(c3, True, True)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=str_n4, \
                       ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=str_n4, c1=str_c1, c2=str_c2, c3=str_c3, c4=c4, k1=k1, k2=k2)

    return stem, answer, comment


def quadequation313_Stem_062():

    stem = "이차함수 $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프를 평행이동하여 완전히 포갤 수 있는 그래프를 보기에서 모두 고른 것은?\n" \
           "$$표$$\n" \
           "㈀ $$수식$${e1}$$/수식$$\n㈁ $$수식$${e2}$$/수식$$\n㈂ $$수식$${e3}$$/수식$$\n㈃ $$수식$${e4}$$/수식$$\n" \
           "$$/표$$\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     \n④ {ex4}     ⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{c1} {c2}\n"\
              "{c3} {c4}\n" \
              "따라서 완전히 포갤 수 있는 그래프는 {a1}이다.\n\n"

    n0 = ctr_frac2(rand_not0(-4, 4), rand_not0(1, 6))
    while abs(n0[0])==abs(n0[1]) : n0 = ctr_frac2(rand_not0(-4, 4), rand_not0(1, 6))
    sign = (1 if n0[0]>0 else -1)
    rand = (0 if n0[0]>0 else 1)
    n3 = rand_not0(-6, 6)
    n4 = rand_not0(-4, 4)
    ex = [['y`=`{}LEFT(x`{} RIGHT)^2'.format(tostr(sign, True, True), make_frac2(n0[0], n0[1], False, False)), 1], \
          ['y`=`{}x^2'.format(make_frac2(n0[1], n0[0], True, True)), 1], \
          ['y`=`{}x^2`{}'.format(make_frac2(n0[0], n0[1], True, True), tostr(n3, False, False)), 0, 'y', n3], \
          ['y`=`{}LEFT(x`{} RIGHT)^2'.format(make_frac2(n0[0], n0[1], True, True), tostr(n4, False, False)), 0, 'x', -n4]]
    random.shuffle(ex)

    co=[]
    ans=[]
    for i in range(4):
        if ex[i][1]==0 :
            co.append([i, '이차함수 $$수식$$y`=`{}x^2`$$/수식$$의 그래프를 $$수식$${}`$$/수식$$축의 방향으로 $$수식$${}`$$/수식$$만큼 평행이동하면 ' \
                          '$$수식$${}`$$/수식$$의 그래프와 포개어진다.'.format(make_frac2(n0[0], n0[1], True, True), ex[i][2], ex[i][3], ex[i][0])])
            ans.append(i)

    list = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    index = ['㈀', '㈁', '㈂', '㈃']
    num = random.randint(0, 5)
    co.sort()
    ans.sort()
    while list[num]==ans : num = random.randint(0, 5)
    del list[num]

    example_list = []
    for i in range(5) :
        example_list.append(index[list[i][0]]+', '+index[list[i][1]])

    ans_i = list.index(ans)

    stem = stem.format(n1=make_frac2(n0[0], n0[1], True, True), e1=ex[0][0], e2=ex[1][0], e3=ex[2][0], e4=ex[3][0],\
                       ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(c1=index[co[0][0]], c2=co[0][1], c3=index[co[1][0]], c4=co[1][1], a1 = example_list[ans_i] )

    return stem, answer, comment


def quadequation313_Stem_063():

    stem = "이차함수 $$수식$$ y`=`ax^2` $$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$${n1}`$$/수식$$만큼 평행이동하면 " \
           "점 $$수식$$ LEFT({n2}`,``{n3} RIGHT)`$$/수식$${jo1} 지날 때, 상수 $$수식$$ a`$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`ax^2` $$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$${n1}`$$/수식$$만큼 평행이동한 그래프의 식은" \
              "$$수식$$ y`=`a LEFT(x`{c1} RIGHT)^2 `$$/수식$$\n" \
              "이 그래프가 점 $$수식$$LEFT({n2}`,``{n3} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$$ {n3}`=`a LEFT({n2}`{c1} RIGHT)^2 `$$/수식$$, $$수식$$ {n3}`={c2}a `$$/수식$$    $$수식$$ THEREFORE````a`=`{a}` $$/수식$$\n\n"

    n1 = rand_not0(-9, 9)
    n2 = rand_not0(-9, 9)
    while abs(n2-n1)>3 or n2==n1 :
        n2 = rand_not0(-9, 9)
    a = rand_not0(-3, 3)
    n3 = a*(n2-n1)**2

    c1 = -n1
    c2 = (n2-n1)**2

    str_c1 = tostr(c1, False, False)
    str_c2 = tostr(c2, True, True)

    example_list = make_example(a)

    stem = stem.format(n1=n1, n2=n2, n3=n3, jo1=proc_jo(n3, 5), ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, n3=n3, c1=str_c1, c2=str_c2, jo1=proc_jo(n3,5), a=a)

    return stem, answer, comment


def quadequation313_Stem_064():

    stem = "이차함수 $$수식$$ y`=`LEFT(x`-`p RIGHT)^2` $$/수식$$의 그래프가 점 $$수식$$ LEFT({n1}`,``{n2} RIGHT)`$$/수식$${jo1} 지날 때, " \
           "이 이차함수의 그래프의 축의 방정식은? (단, $$수식$$ p`&gt;`0`$$/수식$$)\n"\
           "① $$수식$$x`=`{ex1}$$/수식$$     ② $$수식$$x`=`{ex2}$$/수식$$     ③ $$수식$$x`=`{ex3}$$/수식$$     \n④ $$수식$$x`=`{ex4}$$/수식$$     ⑤ $$수식$$x`=`{ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`LEFT(x`-`p RIGHT)^2` $$/수식$$의 그래프가 점 $$수식$$ LEFT({n1}`,``{n2} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$$ {n2}`=`LEFT({n1}`-p RIGHT)^2 `$$/수식$$, $$수식$$ {n1}`-`p`=`+-{c1} `$$/수식$$\n " \
              "$$수식$$ THEREFORE````p`=`{p}` $$/수식$$   $$수식$$ LEFT( BECAUSE`p`&gt;`0 RIGHT)`$$/수식$$\n" \
              "따라서 축의 방정식은 $$수식$$ x`=`{p}`$$/수식$$이다.\n\n"

    n1 = rand_not0(-3, 9)
    p = rand_not0(1, 9)
    while abs(n1-p)>6 or p==n1 or abs(n1-p)<abs(n1) :
        n1 = rand_not0(-3, 9)
        p = rand_not0(1, 9)
    n2 = (n1-p)**2
    c1 = abs(n1-p)

    example_list = make_example(p)

    stem = stem.format(n1=n1, n2=n2, jo1=proc_jo(n2, 5), ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, c1=c1, jo1=proc_jo(n2,5), p=p)

    return stem, answer, comment


def quadequation313_Stem_065():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2` $$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼 평행이동하면 " \
           "점 $$수식$$ LEFT({n3}`,``k RIGHT)`$$/수식$$를 지날 때, $$수식$$ k`$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{n1}x^2` $$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼 평행이동한 그래프의 식은" \
              "$$수식$$ y`=`{n1}LEFT(x`{c1} RIGHT)^2 `$$/수식$$\n 이 그래프가 점 $$수식$$LEFT({n3}`,``k RIGHT)`$$/수식$$를 지나므로\n" \
              "$$수식$$ k`=`{n1}LEFT({n3}`{c1} RIGHT)^2`=`{k} `$$/수식$$\n\n"

    n1 = ctr_frac2(rand_not0(-3, 3), rand_not0(1, 6))
    while n1[0]>n1[1] : n1 = ctr_frac2(rand_not0(-3, 3), rand_not0(1, 6))
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)
    while abs(n3-n2)>5 or n2==n3: n3 = rand_not0(-9, 9)
    c1 = -n2
    k = ctr_frac2(n1[0]*(n2-n3)**2, n1[1])


    example_list=make_example_by_interval(abs(n2-n3), 1)
    while 0 in example_list : example_list=make_example_by_interval(abs(n2-n3), 1)
    print(example_list)
    for i in range(1, 6) :
        example_list[i] = make_frac(n1[0]*example_list[i]**2, n1[1])


    str_n1 = make_frac2(n1[0], n1[1], True, True)
    str_c1 = tostr(c1, False, False)
    str_k = make_frac(k[0], k[1])

    stem = stem.format(n1=str_n1, n2=n2, n3=n3, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, c1=str_c1, k=str_k)

    return stem, answer, comment


def quadequation313_Stem_066():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2` $$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼 평행이동한 그래프에서 " \
           "다음 중 $$수식$$ x`$$/수식$$의 값이 {condx}할 때, $$수식$$ y`$$/수식$$ 값{jo} {condy}하는 $$수식$$ x`$$/수식$$값의 범위가 될 수 있는 것은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{n1}LEFT(x`{c1} RIGHT)^2 `$$/수식$$이므로 $$수식$$ x`{compx}`{n2}`$$/수식$$이면 $$수식$$ x`$$/수식$$의 값이 {condx}할 때, \n" \
              "$$수식$$ y`$$/수식$$의 값{jo} {condy}한다.\n\n"

    n1 = ctr_frac2(rand_not0(-9, 9), rand_not0(1, 9))
    n2 = rand_not0(-9, 9)
    cond = ['증가', '감소']
    dx = random.randint(0, 1)
    dy = random.randint(0, 1)
    c1 = -n2
    comp = ['&lt;', '&gt;']
    px = 0
    if n1[0]>0 :
        if (dx==0 and dy==0) or (dx==1 and dy==1): px = 1
    else :
        if (dx==0 and dy==1) or (dx==1 and dy==0): px = 1

    str_n1 = make_frac2(n1[0], n1[1], True, True)
    str_c1 = tostr(c1, False, False)
    condx = cond[dx]
    condy = cond[dy]
    compx = comp[px]

    ex = [[px, n2, 1], [1-px, n2, -1], [px, -n2, -1], [px, 0, -1], [1-px, 0, -1]]
    random.shuffle(ex)
    ans_i=0
    example_list=[]
    for i in range(5):
        if ex[i][2]==1 : ans_i = i
        example_list.append('x'+comp[ex[i][0]]+' '+str(ex[i][1]))


    stem = stem.format(n1=str_n1, n2=n2, condx=condx, condy=condy, jo = ('은' if dy!=dx else '도'),\
                       ex1=example_list[0], ex2=example_list[1],ex3=example_list[2],ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(n1=str_n1, n2=n2, c1=str_c1, condx=condx, condy=condy, compx=compx, jo = ('은' if dy!=dx else '도'))

    return stem, answer, comment


def quadequation313_Stem_067():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2` $$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼 평행이동한 그래프가 " \
           "두 점 $$수식$$ LEFT({n3}`,``m RIGHT)`$$/수식$$, $$수식$$ LEFT({n4}`,``n RIGHT)`$$/수식$$를 지날 때, $$수식$$ n OVER m`$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{n1}LEFT(x`{c1} RIGHT)^2` $$/수식$$의 그래프가 점 $$수식$$LEFT({n3}`,``m RIGHT)`$$/수식$$을 지나므로\n" \
              "$$수식$$ m`=`{n1}{times1} LEFT({n3}`{c1} RIGHT)^2`=`{m} `$$/수식$$\n" \
              "또, 점 $$수식$$LEFT({n4}`,``n RIGHT)`$$/수식$$을 지나므로\n" \
              "$$수식$$ n`=`{n1}{times1} LEFT({n4}`{c1} RIGHT)^2`=`{n} `$$/수식$$\n" \
              "$$수식$$ THEREFORE````n OVER m`=`{n} OVER {m}`=`{c2} `$$/수식$$\n\n"

    n1 = ctr_frac2(rand_not0(-4, 4), rand_not0(1, 4))
    while n1[1]==3 : n1 = ctr_frac2(rand_not0(-4, 4), rand_not0(1, 4))
    n2 = rand_not0(-6, 6)
    n3 = rand_not0(-6, 6)
    n4 = rand_not0(-6, 6)
    while (n3-n2)**2%n1[1]!=0 or abs(n3-n2)>4 or n3==n2:
        n3 = rand_not0(-6, 6)
    while (n4-n2)**2%n1[1]!=0 or n3==n4 or abs(n4-n2)>4 or n4==n2:
        n4 = rand_not0(-6, 6)
    c1 = -n2
    m= (n1[0]*(n3-n2)**2)//n1[1]
    n= (n1[0]*(n4-n2)**2)//n1[1]
    c2 = ctr_frac2(n, m)

    str_n1 = make_frac2(n1[0], n1[1], True, True)
    str_c1 = tostr(c1, False, False)
    str_c2 = make_frac(c2[0], c2[1])

    stem = stem.format(n1=str_n1, n2=n2, n3=n3, n4=n4)
    answer = answer.format(a1=str_c2)
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, n4=n4, c1=str_c1, c2=str_c2, m=m, n=n, times1=('' if str_n1=='' or str_n1=='-' else 'TIMES'))
    return stem, answer, comment


def quadequation313_Stem_068():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2` $$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼 평행이동한 그래프가 " \
           "두 점 $$수식$$ LEFT({n3}`,``m RIGHT)`$$/수식$$, $$수식$$ LEFT({n4}`,``n RIGHT)`$$/수식$$를 지날 때, $$수식$$ m`+`n`$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{n1}LEFT(x`{c1} RIGHT)^2` $$/수식$$의 그래프가 점 $$수식$$LEFT({n3}`,``m RIGHT)`$$/수식$$을 지나므로\n" \
              "$$수식$$ m`=`{n1}{times1} LEFT({n3}`{c1} RIGHT)^2`=`{m} `$$/수식$$\n" \
              "또, 점 $$수식$$LEFT({n4}`,``n RIGHT)`$$/수식$$을 지나므로\n" \
              "$$수식$$ n`=`{n1}{times1} LEFT({n4}`{c1} RIGHT)^2`=`{n} `$$/수식$$\n" \
              "$$수식$$ THEREFORE````m`+`n`=`{c2} `$$/수식$$\n\n"

    n1 = ctr_frac2(rand_not0(-4, 4), rand_not0(1, 4))
    while n1[1]==3 : n1 = ctr_frac2(rand_not0(-4, 4), rand_not0(1, 4))
    n2 = rand_not0(-6, 6)
    n3 = rand_not0(-6, 6)
    n4 = rand_not0(-6, 6)
    while (n3-n2)**2%n1[1]!=0 or abs(n3-n2)>4 or n3==n2:
        n3 = rand_not0(-6, 6)
    while (n4-n2)**2%n1[1]!=0 or n3==n4 or abs(n4-n2)>4 or n4==n2:
        n4 = rand_not0(-6, 6)
    c1 = -n2
    m= (n1[0]*(n3-n2)**2)//n1[1]
    n= (n1[0]*(n4-n2)**2)//n1[1]
    c2 = m+n

    str_n1 = make_frac2(n1[0], n1[1], True, True)
    str_c1 = tostr(c1, False, False)

    example_list = make_example(c2)

    stem = stem.format(n1=str_n1, n2=n2, n3=n3, n4=n4, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, n4=n4, c1=str_c1, c2=c2, m=m, n=n, times1=('' if str_n1=='' or str_n1=='-' else 'TIMES'))
    return stem, answer, comment


def quadequation313_Stem_069():

    stem = "이차함수 $$수식$$ y`=`{n1}x^2` $$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$p`$$/수식$$만큼 평행이동하면 " \
           "두 점 $$수식$$ LEFT({n2}`,``{n3} RIGHT)`$$/수식$$, $$수식$$ LEFT({n4}`,``q RIGHT)`$$/수식$$를 지날 때, " \
           "$$수식$$ p`+`q`$$/수식$$의 값은? (단, $$수식$$ q`!=`0)$$/수식$$\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{n1}x^2` $$/수식$$의 그래프가 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$p`$$/수식$$만큼 평행이동한\n" \
              "그래프의 식은 $$수식$$y`=`{n1}LEFT(x`-`p RIGHT)^2`$$/수식$$\n" \
              "이 그래프가 점 $$수식$$LEFT({n2}`,``{n3} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$$ {n3}`=`{n1}LEFT({n2}`-`p RIGHT)^2`$$/수식$$, $$수식$$ LEFT({n2}`-`p RIGHT)^2`=`{c1}`$$/수식$$\n" \
              "$$수식$$ {c5}`{c6}p`+`p^2`=`{c1}`$$/수식$$, $$수식$$ p^2`{c2}p`=`0`$$/수식$$\n" \
              "$$수식$$ p LEFT(p`{c3} RIGHT)`=`0`$$/수식$$ $$수식$$ THEREFORE````p`=`0`$$/수식$$또는 $$수식$$ p`=`{p}`$$/수식$$\n" \
              "(ⅰ) $$수식$$ p`=`0`$$/수식$$일 때,\n" \
              "$$수식$$ y`=`{n1}x^2` $$/수식$$에 $$수식$$x`=`{n4} `$$/수식$$, $$수식$$ y`=`q `$$/수식$$를 대입하면 $$수식$$ THEREFORE````q`=`0`$$/수식$$\n" \
              "(ⅱ) $$수식$$ p`=`{p}`$$/수식$$일 때,\n" \
              "$$수식$$ y`=`{n1}LEFT( x`{c3} RIGHT)^2`$$/수식$$에 $$수식$$x`=`{n4} `$$/수식$$, $$수식$$ y`=`q `$$/수식$$를 대입하면 \n" \
              "$$수식$$ q`=`{n1}LEFT({n4}`{c3} RIGHT)^2 `$$/수식$$ $$수식$$ THEREFORE````q`=`{q}`$$/수식$$\n" \
              "그런데 $$수식$$q`!=`0 `$$/수식$$이므로 $$수식$$p`=`{p} `$$/수식$$, $$수식$$q`=`{q} `$$/수식$$\n" \
              "$$수식$$ THEREFORE````p`+`q`=`{p}`+`{q_}`=`{c4} `$$/수식$$\n\n"

    n1 = rand_not0(-3, 3)
    p = rand_not0(-4, 4)
    while p%2!=0 : p=rand_not0(-4, 4)
    n2 = p//2 if abs(p//2-p) < abs(-p//2-p) else -p//2
    n3 = n1*(n2-p)**2
    n4 = 0
    q = n1*(n4-p)**2
    c1 = n3//n1
    c2 = -p
    c3 = -p
    c4 = p+q
    c5 = (c2//2)**2#n2*n2
    c6 = -2*n2

    str_n1 = tostr(n1, True, True)
    str_c2 = tostr(c2, False, True)
    str_c3 = tostr(c3, False, False)
    str_c6 = tostr(c6, False, True)
    ans = c4
    example_list = make_example(ans)

    stem = stem.format(n1=str_n1, n2=n2, n3=n3, n4=n4, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, n4=n4, c1=c1, c2=str_c2, c3=str_c3, c4=c4, c5=c5, c6=str_c6, p=p,q=q, jo1=proc_jo(n3, 5), q_=brac(q))

    return stem, answer, comment


def quadequation313_Stem_070():

    stem = "이차함수 $$수식$$ y`=`{n0}x^2 `$$/수식$$의 그래프를 $$수식$$x`$$/수식$$축의 방향으로 $$수식$${n00}`$$/수식$$만큼 " \
           "평행이동한 그래프에 대한 설명으로 옳은 것은?\n" \
           "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{n0}LEFT(x`{n00} RIGHT)^2 `$$/수식$$\n" \
              "{c1}\n" \
              "{c2}\n" \
              "{c3}\n" \
              "{c4}\n\n"

    n0 = rand_not0(-5, 5)
    while abs(n0)==1 : n0 = rand_not0(-5, 5)
    n00 = rand_not0(-8, 8)
    rand = ([0, 0, 0, 0, 0, 0] if n0>0 else [1, 0, 0, 0, 1, 1])
    ans = random.randint(0, 4)
    rand[ans]=1-rand[ans]
    n1 = ['위', '아래'][rand[0]]
    n2 = [-n0, n00][rand[1]]
    n3 = ['넓다', '좁다'][rand[2]]
    n4 = [[n0, n00], [n0, -n00]][rand[3]]
    n5 = [[n00, '도 증가'],[n00, '은 감소']][rand[4]]
    n6 = ['양수', '음수'][rand[5]]

    ex = ['{}로 볼록한 포물선이다.'.format(n1), '꼭짓점의 좌표는 $$수식$$LEFT({},``0 RIGHT)`$$/수식$$이다.'.format(n2),\
          '$$수식$$y`=`x^2`$$/수식$$보다 폭이 {}.'.format(n3), \
          '$$수식$$y`=`{}(x`{})^2`$$/수식$$의 그래프와 $$수식$$x`$$/수식$$축에 대하여 서로 대칭이다.'.format(tostr(-n4[0], True, True), tostr(n4[1], False, False)),\
         '$$수식$$x &lt; {}`$$/수식$$일 때, $$수식$$x`$$/수식$$의 값이 증가하면 $$수식$$y`$$/수식$$의 값{}한다.'.format(str(n5[0]), n5[1]),
          '모든 $$수식$$x`$$/수식$$값에 대하여 $$수식$$y`$$/수식$$의 값은 {}이다.'.format(n6)]


    n1 = ['위', '아래'][1-rand[0]]
    n2 = [-n0, n00][1-rand[1]]
    n3 = ['넓다', '좁다'][1-rand[2]]
    n4 = [[n0, n00], [n0, -n00]][1-rand[3]]
    n5 = [[n00, '도 증가'], [n00, '은 감소']][1-rand[4]]

    co = ['{}로 볼록한 포물선이다.'.format(n1), '꼭짓점의 좌표는 $$수식$$LEFT({},``0 RIGHT)`$$/수식$$이다.'.format(n2), \
          '$$수식$$y`=`x^2`$$/수식$$보다 폭이 {}.'.format(n3), \
          '$$수식$$y`=`{}(x`{})^2`$$/수식$$의 그래프와 $$수식$$x`$$/수식$$축에 대하여 서로 대칭이다.'.format(tostr(-n4[0], True, True), tostr(n4[1], False, False)), \
          '$$수식$$x &lt; {}`$$/수식$$일 때, $$수식$$x`$$/수식$$의 값이 증가하면 $$수식$$y`$$/수식$$의 값{}한다.'.format(str(n5[0]), n5[1]),
          '$$수식$$x`=`{}`$$/수식$$일 때, $$수식$$y`=`0`$$/수식$$이다.'.format(n00)]

    de=random.randint(0, 5)
    while de==ans : de=random.randint(0, 5)
    del ex[de]
    del co[de]
    if de<ans : ans-=1

    co[0] = '① ' + co[0]
    co[1] = '② ' + co[1]
    co[2] = '③ ' + co[2]
    co[3] = '④ ' + co[3]
    co[4] = '⑤ ' + co[4]
    del co[ans]

    stem = stem.format(n0=tostr(n0, True, True), n00=n00, ex1=ex[0], ex2=ex[1], ex3=ex[2], ex4=ex[3], ex5=ex[4])
    answer = answer.format(a1=answer_dict[ans])
    comment = comment.format(n0=tostr(n0, True, True), n00=tostr(-n00, False, False),c1=co[0], c2=co[1], c3=co[2], c4=co[3])

    return stem, answer, comment


def quadequation313_Stem_071():

    stem = "이차함수 $$수식$$ y`=`x^2` $$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$p`$$/수식$$만큼 평행이동한 " \
           "그래프를 나타내는 식을 $$수식$$ y`=`f`LEFT(x RIGHT)` $$/수식$$라 하자. $$수식$$`f`LEFT({n1} RIGHT)`=`{n2}`$$/수식$${jo1} " \
           "만족시키는 모든 이차함수 $$수식$$ y`=`f`LEFT(x RIGHT) `$$/수식$$의 그래프의 $$수식$$ y`$$/수식$$절편의 합은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ f`LEFT(x RIGHT)`=`LEFT( x`-`p RIGHT)^2 `$$/수식$$이고 $$수식$$ `f`LEFT({n1} RIGHT)`=`{n2}`$$/수식$$이므로\n" \
              "$$수식$$ {n2}`=`LEFT({n1}`-`p RIGHT)^2 `$$/수식$$, $$수식$$ {n1}`-`p =`+-{c1} `$$/수식$$\n" \
              "$$수식$$ THEREFORE````p`=`{p1}`$$/수식$$ 또는$$수식$$ p`=`{p2}`$$/수식$$\n" \
              "$$수식$$ THEREFORE````f`(x)`=`(x`{c2})^2`$$/수식$$ 또는 $$수식$$ f`(x)`=`(x`{c3}`)^2`$$/수식$$\n" \
              "따라서 두 이차함수의 그래프의 $$수식$$ y`$$/수식$$절편은 각각 $$수식$${c4}`$$/수식$$, $$수식$${c5}`$$/수식$$이므로 " \
              "구하는 합은 $$수식$${c6}`$$/수식$$이다.\n\n"

    n1 = rand_not0(-4, 4)
    c1 = rand_not0(1, 3)
    while n1+c1==0 or n1-c1==0 : c1 = rand_not0(-3, 3)
    n2 = c1**2
    p1 =  n1-c1
    p2 = n1+c1
    c2 = -p1
    c3 = -p2
    c4 = p1**2
    c5 = p2**2
    c6 = c4+c5

    str_c2 = tostr(c2, False, False)
    str_c3 = tostr(c3, False, False)

    ans = c6
    example_list = make_example(ans)

    stem = stem.format(n1=n1, n2=n2, jo1=proc_jo(n2, 5), ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, c1=c1, c2=str_c2, c3=str_c3, c4=c4, c5=c5, c6=c6, p1=p1, p2=p2)

    return stem, answer, comment


def quadequation313_Stem_072():

    stem = "이차함수 $$수식$$ y`=`x^2` $$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$p`$$/수식$$만큼 평행이동한 " \
           "그래프를 나타내는 식을 $$수식$$ y`=`f`LEFT(x RIGHT)` $$/수식$$라 하자. $$수식$$`f`LEFT({n1} RIGHT)`=`{n2}`$$/수식$${jo1} " \
           "만족시키는 모든 이차함수 $$수식$$ y`=`f`LEFT(x RIGHT) `$$/수식$$의 그래프의 $$수식$$ y`$$/수식$$절편의 곱을 구하시오\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ f`LEFT(x RIGHT)`=`LEFT( x`-`p RIGHT)^2 `$$/수식$$이고 $$수식$$ `f`LEFT({n1} RIGHT)`=`{n2}`$$/수식$$이므로\n" \
              "$$수식$$ {n2}`=`LEFT({n1}`-`p RIGHT)^2 `$$/수식$$, $$수식$$ {n1}`-`p =`+-{c1} `$$/수식$$\n" \
              "$$수식$$ THEREFORE````p`=`{p1}`$$/수식$$ 또는$$수식$$ p`=`{p2}`$$/수식$$\n" \
              "$$수식$$ THEREFORE````f`(x)`=`(x`{c2})^2`$$/수식$$ 또는 $$수식$$ f`(x)`=`(x`{c3}`)^2`$$/수식$$\n" \
              "따라서 두 이차함수의 그래프의 $$수식$$ y`$$/수식$$절편은 각각 $$수식$${c4}`$$/수식$$, $$수식$${c5}`$$/수식$$이므로 " \
              "구하는 합은 $$수식$${c6}`$$/수식$$이다.\n\n"

    n1 = rand_not0(-4, 4)
    c1 = rand_not0(1, 3)
    while n1-c1==0 or n1+c1==0 : c1 = rand_not0(-3, 3)
    n2 = c1**2
    p1 = n1-c1
    p2 = n1+c1
    c2 = -p1
    c3 = -p2
    c4 = p1**2
    c5 = p2**2
    c6 = c4*c5

    str_c2 = tostr(c2, False, False)
    str_c3 = tostr(c3, False, False)

    ans = c6

    stem = stem.format(n1=n1, n2=n2, jo1=proc_jo(n2, 5))
    answer = answer.format(a1='$$수식$$'+str(ans)+'`$$/수식$$')
    comment = comment.format(n1=n1, n2=n2, c1=c1, c2=str_c2, c3=str_c3, c4=c4, c5=c5, c6=c6, p1=p1, p2=p2)

    return stem, answer, comment


def quadequation313_Stem_073():

    stem = "이차함수 $$수식$$ y`=`{n2}x^2`$$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$${n1}k`$$/수식$$만큼 평행이동한 " \
           "그래프가 $$수식$$ x`$$/수식$$축과 만나는 점을 $$수식$$rm A`$$/수식$$, $$수식$$y`$$/수식$$축과 만나는 점을 $$수식$$rm B`$$/수식$$라 " \
           "할 때, $$수식$$TRIANGLE rmO`A`B`$$/수식$$의 넓이는 $$수식$${n3}`$$/수식$$이다. 이때 양수 $$수식$$k`$$/수식$$의 값은? " \
           "(단, $$수식$$rmO`$$/수식$$는 원점이다.)\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{n2}LEFT( x`{c1}k RIGHT)^2 `$$/수식$$에 $$수식$$ y`=`0`$$/수식$$을 대입하면\n" \
              "$$수식$$ 0`=`{n2}LEFT( x`{c1}k RIGHT)^2 `$$/수식$$ $$수식$$ THEREFORE````x`=`{n1}k `$$/수식$$ " \
              "$$수식$$ THEREFORE````rmA LEFT({n1}k`,``0) `$$/수식$$\n" \
              "$$수식$$ y`=`{n2}LEFT( x`{c1}k RIGHT)^2 `$$/수식$$에 $$수식$$ x`=`0`$$/수식$$을 대입하면\n" \
              "$$수식$$ y`=`{n2}LEFT({c2}k RIGHT)^2`=`{c3}k^2 `$$/수식$$ $$수식$$ THEREFORE````rmB LEFT(0`,``{c3}k^2 RIGHT) `$$/수식$$\n" \
              "$$수식$$ TRIANGLE rmO`A`B`=`1OVER2 TIMES{n1}k TIMES{c3}k^2`=`{n3} `$$/수식$$이므로\n" \
              "$$수식$${c4}k^3`=`{n3}`$$/수식$$, $$수식$$k^3`=`{c5}`=`{k}^3`$$/수식$$이다.\n" \
              "$$수식$$THEREFORE````k`=`{k}`$$/수식$$\n\n"

    n1 = rand_not0(1, 4)
    while n1==1 or n1==3 : n1 = rand_not0(1, 4)
    n2 = ctr_frac2(rand_not0(1, 2), rand_not0(2, 4))
    while n2[1]==3 : n2 = ctr_frac2(rand_not0(1, 2), rand_not0(2, 4))
    k = rand_not0(1, 5)
    c1 = -n1
    c2 = c1
    c3 = (c2*c2*n2[0])//n2[1]
    n3 = (k*k*k*n1*c3)//2
    c4 = n3//(k*k*k)
    c5 = k*k*k

    str_n1 = tostr(n1, True, True)
    str_n2 = make_frac2(n2[0], n2[1], True, True)
    str_c1 = tostr(c1, False, True)
    str_c2 = tostr(c2, True, True)
    str_c3 = tostr(c3, True, True)
    str_c4 = tostr(c4, True, True)

    ans = k
    example_list = make_example(ans)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=n3, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=n3, c1=str_c1, c2=str_c2, c3=str_c3, c4=str_c4, c5=c5, k=k)

    return stem, answer, comment


def quadequation313_Stem_074():

    stem = "축의 방정식이 $$수식$$x`=`{n1}`$$/수식$$이고 $$수식$$x`$$/수식$$에 접하며 점 $$수식$$LEFT({n2}`,``{n3} RIGHT)`$$/수식$${jo1} 지나는 " \
           "포물선을 그래프로 하는 이차함수의 식은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     \n③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     \n⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "꼭짓점의 좌표가 $$수식$$ LEFT({n1}`,``0 RIGHT) `$$/수식$$이므로 구하는 이차함수의 식을" \
              "$$수식$$ y`=`a LEFT( x`{c1} RIGHT)^2 `$$/수식$$으로 놓을 수 있다.\n" \
              "이 그래프가 점 $$수식$$LEFT({n2}`,``{n3} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$$ {n3}`=`a LEFT({n2}`{c1} RIGHT)^2 `$$/수식$$ $$수식$$ THEREFORE````a`=`{a} `$$/수식$$\n" \
              "따라서 구하는 이차함수의 식은\n" \
              "$$수식$$ {a1} `$$/수식$$\n\n"

    n1 = rand_not0(-9, 9)
    n2 = rand_not0(-9, 9)
    while n1==n2 or abs(n2-n1)>=5 : n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)
    a = ctr_frac2(n3, (n2-n1)**2)
    c1 = -n1

    str_c1 = tostr(c1, False, False)
    str_a = make_frac(a[0], a[1])

    example_list = make_example(a[1])
    for i in range(1, 6) :
        example_list[i] = 'y`=`'+ make_frac2(a[0], example_list[i], True, True) + 'LEFT(x`'+ str_c1 + 'RIGHT)^2'

    stem = stem.format(n1=n1, n2=n2, n3=n3, jo1=proc_jo(n3, 5), ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, n3=n3, c1=str_c1, a=str_a, jo1=proc_jo(n3, 5), a1=example_list[example_list[0]+1])

    return stem, answer, comment


def quadequation313_Stem_075():

    stem = "이차함수 $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프를 $$수식$$x`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼 $$수식$$y`$$/수식$$축의 " \
           "방향으로 $$수식$${n3}`$$/수식$$만큼 평행이동하면 점 $$수식$$LEFT({n4}`,``k RIGHT)`$$/수식$$를 지날 때, $$수식$$k`$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{n1}LEFT(x`{c1} RIGHT)^2`{c2}`$$/수식$$의 그래프가 점 $$수식$$LEFT({n4}`,``k RIGHT)`$$/수식$$를 지나므로\n" \
              "$$수식$$k`=`{n1}{times1}LEFT({n4}`{c1} RIGHT)^2`{c2}`=`{k}`$$/수식$$\n\n"

    n1 = rand_not0(-3, 3)
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)
    n4 = rand_not0(-9, 9)
    while n1==n2 or abs(n4-n2)>=5 : n2 = rand_not0(-9, 9)
    k = n1*((n4-n2)**2)+n3
    c1 = -n2
    c2 = n3

    str_n1 = tostr(n1, True, True)
    str_c1 = tostr(c1, False, False)
    str_c2 = tostr(c2, False, False)
    example_list = make_example(k)

    stem = stem.format(n1=str_n1, n2=n2, n3=n3, n4=n4, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, n4=n4, c1=str_c1, c2=str_c2, k=k, times1=('' if n1==1or n1==-1 else 'TIMES'))

    return stem, answer, comment


def quadequation313_Stem_076():

    stem = "이차함수 $$수식$$y`=`{n1}LEFT(x`{n2} RIGHT)^2`{n3}`$$/수식$$의 그래프를 $$수식$$x`$$/수식$$축의 방향으로 $$수식$$p`$$/수식$$만큼, $$수식$$y`$$/수식$$축의 " \
           "방향으로 $$수식$$q`$$/수식$$만큼 평행이동하였더니\n $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프와 일치하였다. 이때 $$수식$$p`-`q`$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{n1}LEFT(x`-`p`{n2} RIGHT)^2`{n3}`+`q`$$/수식$$와 $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프가 일치하므로\n" \
              "$$수식$$-`p`{n2}`=`0`$$/수식$$, $$수식$${c1}`+`q`=`0`$$/수식$$\n" \
              "따라서 $$수식$$p`=`{p}`$$/수식$$, $$수식$$q`=`{q}`$$/수식$$이므로\n" \
              "$$수식$$p`-`q`=`{c2}`$$/수식$$\n\n"

    n1 = rand_not0(-3, 3)
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)
    p = n2
    q = -n3
    c1 = n3
    c2 = p-q

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, False)
    example_list = make_example(c2)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, c1=c1, c2=c2, p=p, q=q)

    return stem, answer, comment


def quadequation313_Stem_077():

    stem = "이차함수 $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프와 모양이 같고, 꼭짓점의 좌표가 $$수식$$LEFT({n2},``{n3} RIGHT)`$$/수식$$인 " \
           "포물선을 그래프로 하는 이차함수의 식을 $$수식$$y`=`a LEFT(x`+`p)^2`+`q`$$/수식$$라 할 때, 상수 $$수식$$a`$$/수식$$, " \
           "$$수식$$p`$$/수식$$, $$수식$$q`$$/수식$$에 대하여 $$수식$$a`p`q`$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "주어진 조건을 만족시키는 이차함수의 식은\n" \
              "$$수식$$y`=`{n1}LEFT(x`{c1} RIGHT)^2`{c2}`$$/수식$$이므로\n" \
              "$$수식$$a`=`{a}`$$/수식$$, $$수식$$p`=`{p}`$$/수식$$, $$수식$$q`=`{q}`$$/수식$$이므로\n" \
              "$$수식$$THEREFORE````a`p`q`=`{c3}`$$/수식$$\n\n"

    n1 = ctr_frac2(rand_not0(-3, 3), rand_not0(1, 6))
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)
    while n2==n3 or n2*n3%n1[1]!=0 : n3 = rand_not0(-9, 9)
    c1 = -n2
    c2 = -n3
    p = c1
    q = c2
    a = n1
    c3 = (a[0]*p*q)//a[1]

    str_n1 = make_frac2(n1[0], n1[1], True, True)
    str_c1 = tostr(c1, False, False)
    str_c2 = tostr(c2, False, False)
    str_a = make_frac(a[0], a[1])

    example_list = make_example(c3)

    stem = stem.format(n1=str_n1, n2=n2, n3=n3, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, c1=str_c1, c2=str_c2, c3=c3, a=str_a, p=p, q=q)

    return stem, answer, comment


def quadequation313_Stem_078():

    stem = "이차함수 $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프를 $$수식$$x`$$/수식$$축의 방향으로  $$수식$${n2}`$$/수식$$만큼 " \
           "$$수식$$y`$$/수식$$축의 방향으로 $$수식$${n3}`$$/수식$$만큼 평행이동한 그래프를 나타내는 이차함수의 식은?\n"\
           "① $$수식$${ex1}$$/수식$$\n② $$수식$${ex2}$$/수식$$\n③ $$수식$${ex3}$$/수식$$\n④ $$수식$${ex4}$$/수식$$\n⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{n1}x^2`$$/수식$$의 그래프를 $$수식$$x`$$/수식$$축의 방향으로  $$수식$${n2}`$$/수식$$만큼 " \
              "$$수식$$y`$$/수식$$축의 방향으로 $$수식$${n3}`$$/수식$$만큼 평행이동한 그래프를 나타내는 이차함수의 식은\n"\
              "$$수식$${a1}`$$/수식$$\n\n"

    n1 = rand_not0(-9, 9)
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)

    str_n1 = tostr(n1, True, True)

    ex = [[n1,-n2,n3,1],[n1,-n2,-n3,-1],[n1,n2,n3,-1],[n1,n2,-n3,-1],[-n1,-n2,n3,-1]]
    random.shuffle(ex)
    example_list = []
    ans_i=0
    for i in range(5):
        if ex[i][3]==1: ans_i=i
        example_list.append('y`=`'+tostr(ex[i][0], True, True)+'LEFT(x`'+tostr(ex[i][1], False, False)+'RIGHT)^2 '+tostr(ex[i][2], False, False))


    stem = stem.format(n1=str_n1, n2=n2, n3=n3, ex1=example_list[0], ex2=example_list[1],ex3=example_list[2],ex4=example_list[3],ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, a1=example_list[ans_i])

    return stem, answer, comment


def quadequation313_Stem_079():

    stem = "그래프의 꼭짓점이 제$$수식$${n1}`$$/수식$$사분면에 있는 이차함수를 보기에서 모두 고른 것은?\n" \
           "$$표$$\n" \
           "㈀ $$수식$${e1}$$/수식$$\n㈁ $$수식$${e2}$$/수식$$\n㈂ $$수식$${e3}$$/수식$$\n㈃ $$수식$${e4}$$/수식$$\n" \
           "$$/표$$\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     \n④ {ex4}     ⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "주어진 이차함수의 그래프의 꼭짓점의 좌표를 구해보면\n" \
              "㈀ {c1}\n"\
              "㈁ {c2}\n" \
              "㈂ {c3}\n" \
              "㈃ {c4}\n" \
              "따라서 그래프의 꼭짓점이 제$$수식$${n1}`$$/수식$$사분면에 있는 이차함수는 {a1}이다.\n\n"

    num = random.randint(1, 4)
    sa = [random.randint(1, 4), random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)]
    while sa.count(num)!=2 : sa = [random.randint(1, 4), random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)]
    ans=[]
    dot=[]
    for i in range(4) :
        if sa[i]==num : ans.append(i)
        if sa[i]==1: dot.append([random.randint(1, 6), random.randint(1, 9)])
        elif sa[i] == 2: dot.append([random.randint(-6, -1), random.randint(1, 9)])
        elif sa[i] == 3: dot.append([random.randint(-6, -1), random.randint(-9, -1)])
        elif sa[i] == 4: dot.append([random.randint(1, 6), random.randint(-9, -1)])

    coef=[]
    for i in range(4):
        temp = rand_not0(-6, 6)
        while temp in coef : temp = rand_not0(-6, 6)
        coef.append(temp)

    ex=[]
    co=[]
    for i in range(4) :
        ex.append('y`=`{} LEFT(x`{} RIGHT)^2`{}'.format(tostr(coef[i], True, True), tostr(-dot[i][0], False, False), tostr(dot[i][1], False, False)))
        co.append('$$수식$$ LEFT({},``{} RIGHT) `$$/수식$$ : 제$$수식$${}`$$/수식$$사분면'.format(dot[i][0], dot[i][1], sa[i]))

    list = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
    index = ['㈀', '㈁', '㈂', '㈃']
    example_list = []

    de = random.randint(0, 5)
    while list[de]==ans : de = random.randint(0, 5)
    del list[de]

    for i in range(5) :
        example_list.append(index[list[i][0]]+', '+index[list[i][1]])

    ans_i = list.index(ans)

    stem = stem.format(n1=num, e1=ex[0], e2=ex[1], e3=ex[2], e4=ex[3],\
                       ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(n1=num, c1=co[0], c2=co[1], c3=co[2], c4=co[3], a1 = example_list[ans_i] )

    return stem, answer, comment


def quadequation313_Stem_080():

    stem = "이차함수 $$수식$$y`=`{n1}LEFT(x`{n2} RIGHT)^2`{n3}`$$/수식$$의 그래프는" \
           "$$수식$$y`=`{n1}x^2`$$/수식$$의 그래프를 $$수식$$x`$$/수식$$축의 방향으로 $$수식$$p`$$/수식$$만큼, " \
           "$$수식$$y`$$/수식$$축의 방향으로 $$수식$$q`$$/수식$$만큼 평행이동한 것이다. 이때 $$수식$$p`-`q`$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "이차함수 $$수식$$y`=`{n1}LEFT(x`{n2} RIGHT)^2`{n3}`$$/수식$$의 그래프는 " \
              "$$수식$$y`=`{n1}x^2`$$/수식$$의 그래프를 $$수식$$x`$$/수식$$축의 방향으로 $$수식$${c1}`$$/수식$$만큼, " \
              "$$수식$$y`$$/수식$$축의 방향으로 $$수식$${c2}`$$/수식$$만큼 평행이동한 것이다.\n" \
              "따라서 $$수식$$p`=`{c1}`$$/수식$$,  $$수식$$q`=`{c2}`$$/수식$$이므로 $$수식$$p`-`q`=`{c3}`$$/수식$$\n\n"

    n1 = ctr_frac2(rand_not0(-9, 9), rand_not0(1, 9))
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)
    c1 = -n2
    c2 = n3
    c3 = c1-c2

    str_n1 = make_frac2(n1[0], n1[1], True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, False)

    example_list = make_example(c3)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, c1=c1, c2=c2, c3=c3)

    return stem, answer, comment


def quadequation313_Stem_081():

    stem = "다음 이차함수 중 좌표평면 위에서 그 그래프의 축이 가장 {cond}에 있는 것은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     \n" \
           "③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     \n" \
           "⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "축의 방정식을 각각 구하면\n" \
              "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$     ④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n" \
              "따라서 좌표평면 위에서 축이 가장 {cond}에 있는 것은 {a1}이다.\n\n"

    cond_ex=['왼쪽', '오른쪽']
    cond = random.randint(0, 1)
    ex = [[], [], []]
    for i in range(5) :
        ex[0].append(rand_not0(-9, 9))
        temp = random.randint(-9, 9)
        while temp in ex[1] : temp = random.randint(-9, 9)
        ex[1].append(temp)
        ex[2].append(random.randint(-9, 9))

    example_list = []
    comment_list = []
    ans_maxi=0
    ans_mini=0
    max=-10
    min=10
    for i in range(5) :
        if ex[1][i]==0 :
            if ex[2][i]==0 : example_list.append('y`=`'+tostr(ex[0][i], True, True)+'x^2')
            else : example_list.append('y`=`'+tostr(ex[0][i], True, True)+'x^2`'+tostr(ex[2][i], False, False))
        else :
            if ex[2][i]==0 : example_list.append('y`=`'+tostr(ex[0][i], True, True)+'LEFT(x`'+tostr(ex[1][i], False, False)+'RIGHT)^2 ')
            else : example_list.append('y`=`'+tostr(ex[0][i], True, True)+'LEFT(x`'+tostr(ex[1][i], False, False)\
                                       +'RIGHT)^2 '+tostr(ex[2][i], False, False))

        comment_list.append('x`=`'+str(-ex[1][i]))
        if max<ex[1][i] :
            ans_maxi=i
            max = ex[1][i]
        if min>ex[1][i] :
            ans_mini=i
            min = ex[1][i]


    stem = stem.format(ex1=example_list[0], ex2=example_list[1],ex3=example_list[2],ex4=example_list[3],ex5=example_list[4], cond=cond_ex[cond])
    answer = answer.format(a1=(answer_dict[ans_maxi] if cond==0 else answer_dict[ans_mini]))
    comment = comment.format(c1=comment_list[0], c2=comment_list[1], c3=comment_list[2], c4=comment_list[3], c5=comment_list[4], cond=cond_ex[cond],\
                             a1=(answer_dict[ans_maxi] if cond==0 else answer_dict[ans_mini]))

    return stem, answer, comment


def quadequation313_Stem_082():

    stem = "이차함수 $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프를 $$수식$$x`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼, " \
           "$$수식$$y`$$/수식$$축의 방향으로 $$수식$$a`$$/수식$$만큼 평행이동하면 두 점 $$수식$$LEFT({n3},``{n4} RIGHT)`$$/수식$$, " \
           "$$수식$$LEFT({n5},``b RIGHT)`$$/수식$$를 지난다. 이때 $$수식$$a`+`b`$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{n1}x^2`$$/수식$$의 그래프를 $$수식$$x`$$/수식$$축의 방향으로 $$수식$${n2}`$$/수식$$만큼, " \
              "$$수식$$y`$$/수식$$축의 방향으로 $$수식$$a`$$/수식$$만큼 평행이동한 그래프를 나타내는 이차함수의 식은\n" \
              "$$수식$$y`=`{n1}LEFT(x`{c1})^2`+`a`$$/수식$$\n" \
              "이 함수의 그래프가 점 $$수식$$LEFT({n3},``{n4} RIGHT)`$$/수식$${jo1} 지나므로\n " \
              "$$수식$${n4}`=`{n1}LEFT({n3}`{c1})^2`+`a`$$/수식$$, $$수식$${n4}`=`{c2}`+`a`$$/수식$$\n" \
              "$$수식$$THEREFORE````a`=`{a}`$$/수식$$" \
              "따라서 구하는 이차함수의 식은 $$수식$$y`=`{n1}LEFT(x`{c1})^2`{c3}`$$/수식$$이고 이 그래프가 " \
              "점 $$수식$$LEFT({n5},``b RIGHT)`$$/수식$$를 지나므로" \
              "$$수식$$b`=`{n1}LEFT({n5}`{c1})^2`{c3}`=`{b}`$$/수식$$" \
              "$$수식$$THEREFORE````a`+`b`=`{c4}`$$/수식$$\n\n"

    n1 = rand_not0(-3, 3)
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)
    while abs(n3-n2)>5 or n3==n2: n3 = rand_not0(-9, 9)
    n5 = rand_not0(-9, 9)
    while abs(n5-n2)>5 or n5==n2 or n5==n3: n5 = rand_not0(-9, 9)
    a = (rand_not0(-9, -1)) if n1>0 else rand_not0(1, 9)
    n4 = n1*((n3-n2)**2)+a
    b = n1*((n5-n2)**2)+a
    c1 = -n2
    c2 = n1*((n3-n2)**2)
    c3 = a
    c4 = a+b

    str_n1 = tostr(n1, True, True)
    str_c1 = tostr(c1, False, False)
    str_c3 = tostr(c3, False, False)

    example_list = make_example(c4)

    stem = stem.format(n1=str_n1, n2=n2, n3=n3, n4=n4, n5=n5, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, n4=n4, n5=n5, c1=str_c1, c2=c2, c3=str_c3, c4=c4, jo1=proc_jo(n4, 5), a=a, b=b)

    return stem, answer, comment


def quadequation313_Stem_083():

    stem = "이차함수 $$수식$$y`=`{n1}LEFT(x`{n2}p)^2`{n3}p^2`$$/수식$$의 그래프의 꼭짓점이 직선 $$수식$$y`=`{n4}x`{n5}`$$/수식$$" \
           "위에 있을 때, 상수 $$수식$$p`$$/수식$$의 값은? (단, $$수식$$p`&lt;`0`$$/수식$$)\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "꼭짓점의 좌표가 $$수식$$LEFT({c1}p,``{c2}p^2 RIGHT)`$$/수식$$이고 이 점이 직선\n " \
              "$$수식$$y`=`{n4}x`{n5}`$$/수식$$ 위에 있으므로\n" \
              "$$수식$${c3}p^2`=`{c4}p`{c5}`$$/수식$$, $$수식$${c3}p^2`{c6}p`{c7}`=`0`$$/수식$$\n" \
              "$$수식$$LEFT({c8}p`{c9} RIGHT) LEFT({c10}p`{c11} RIGHT)`=`0`$$/수식$$    " \
              "$$수식$$THEREFORE````p`=`{p1} LEFT(BECAUSE`p`&lt;`0 RIGHT)`$$/수식$$\n\n"

    p1 = ctr_frac2(rand_not0(-3, -1), rand_not0(1, 4))
    p2 = ctr_frac2(rand_not0(1, 3), rand_not0(1, 4))

    c8 = p1[1]
    c9 = -p1[0]
    c10 = p2[1]
    c11 = -p2[0]
    c3 = c8*c10
    c6 = c9*c10+c8*c11
    c7 = c9*c11
    c4 = -c6
    c5 = -c7
    n4 = (-1 if c4<0 else 1)
    n5 = c5
    c1 = c4//n4
    c2 = c3
    n1 = ctr_frac2(rand_not0(-3, 3), rand_not0(1, 9))
    n2 = -c1
    n3 = c2

    str_n1 = make_frac2(n1[0], n1[1], True, True)
    str_n2 = tostr(n2, False, True)
    str_n3 = tostr(n3, False, True)
    str_n4 = tostr(n4, True, True)
    str_n5 = tostr(n5, False, False)
    str_c1 = tostr(c1, True, True)
    str_c2 = tostr(c2, True, True)
    str_c3 = tostr(c3, True, True)
    str_c4 = tostr(c4, True, True)
    str_c5 = tostr(c5, False, False)
    str_c6 = tostr(c6, False, True)
    str_c7 = tostr(c7, False, False)
    str_c8 = tostr(c8, True, True)
    str_c9 = tostr(c9, False, False)
    str_c10 = tostr(c10, True, True)
    str_c11 = tostr(c11, False, False)
    str_p1 = make_frac(p1[0], p1[1])

    example_list = make_fraction_example2(p1[0], p1[1], p1[1]*6)
    while 0 in example_list :  example_list = make_fraction_example2(p1[0], p1[1], p1[1]*6)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=str_n4, n5=str_n5, \
                       ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=str_n4, n5=str_n5, c1=str_c1, c2=str_c2, c3=str_c3, c4=str_c4, c5=str_c5, \
                             c6=str_c6, c7=str_c7, c8=str_c8, c9=str_c9, c10=str_c10, c11=str_c11, p1=str_p1)
    return stem, answer, comment


def quadequation313_Stem_084():

    stem = "이차함수 $$수식$$y`=`a LEFT(x`-`p)^2`{n1}`$$/수식$$의 그래프가 직선 $$수식$$x`=`{n2}`$$/수식$${jo2} 축으로 하고 " \
           "점 $$수식$$LEFT({n3},``{n4} RIGHT)`$$/수식$${jo1} 지날 때, $$수식$$a`$$/수식$$의 값은? " \
           "(단, $$수식$$a`$$/수식$$, $$수식$$p`$$/수식$$는 상수이다.)\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`a LEFT(x`-`p)^2`{n1}`$$/수식$$의 그래프가 직선 $$수식$$x`=`{n2}`$$/수식$${jo2} 축으로 하므로\n" \
              "$$수식$$p`=`{n2}`$$/수식$$\n" \
              "따라서 $$수식$$y`=`a LEFT(x`{c1})^2`{n1}`$$/수식$$의 그래프가 점 $$수식$$LEFT({n3},``{n4} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$${n4}`=`a LEFT({n3}`{c1})^2`{n1}`$$/수식$$    $$수식$$THEREFORE````a`=`{a}`$$/수식$$\n\n"

    n1 = rand_not0(-9, 9)
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)
    while n3==n2 or abs(n3-n2)>4 : n3 = rand_not0(-9, 9)
    n4 = (rand_not0(-12, 2)  if n1<0 else rand_not0(-2, 12))
    if n4==n1 : n4 = (rand_not0(-12, 2)  if n1<0 else rand_not0(-2, 12))
    a = [n4-n1, (n3-n2)**2]

    str_n1 = tostr(n1, False, False)
    str_c1 = tostr(-n2, False, False)
    str_a = make_frac(a[0], a[1])
    example_list = make_fraction_example2(a[0], a[1], a[1])

    stem = stem.format(n1=str_n1, n2=n2, n3=n3, n4=n4, jo2=proc_jo(n2,5), jo1=proc_jo(n4,5), ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, n4=n4, a=str_a, c1=str_c1, jo1=proc_jo(n4, 5), jo2=proc_jo(n2,5))
    return stem, answer, comment


def quadequation313_Stem_085():

    stem = "다음 이차함수 중 그래프가 {cond1}로 볼록하고 꼭짓점이 제$$수식$${cond2}`$$/수식$$사분면에 있는 것은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     \n③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     \n⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "그래프가 {cond1}로 볼록하다. ⇨ {c1a}, {c1b}, {c1c}\n" \
              "이들의 꼭짓점의 좌표를 각각 구해 보면\n" \
              "{c1a} $$수식$${c2}`$$/수식$$"     "{c1b}$$수식$${c3}`$$/수식$$"     "{c1c}$$수식$${c4}`$$/수식$$\n" \
              "따라서 {cond1}로 볼록하고 꼭짓점이 제{cond2}사분면에 있는 것은 {a1}이다.\n\n"

    updown = ['위', '아래']
    con1 = random.randint(0, 1)
    con2 = random.randint(1, 4)

    ex=[]
    if con1==0 :
        for i in range(3) : ex.append([rand_not0(-3, -1)])
        for i in range(2) : ex.append([rand_not0(1, 3)])
    else :
        for i in range(3) : ex.append([rand_not0(1, 3)])
        for i in range(2) : ex.append([rand_not0(-3, -1)])

    #1 : 양수, 2:음수
    def make_sa(xa, ya) :
        rand = [[-9, 9], [1, 9], [-9, -1], [0, 9], [-9, 0]]
        ex[0].append(random.randint(rand[xa][0], rand[xa][1]))
        ex[0].append(random.randint(rand[ya][0], rand[ya][1]))
        ex[0].append(1)
        for i in range(1, 3):
            ex[i].append(random.randint(rand[5-xa][0], rand[5-xa][1]))
            ex[i].append(random.randint(rand[0][0], rand[0][1]))
            ex[i].append(-1)
        for i in range(3, 5):
            ex[i].append(random.randint(rand[0][0], rand[0][1]))
            ex[i].append(random.randint(rand[5-ya][0], rand[5-ya][1]))
            ex[i].append(-1)

    if con2==1 : make_sa(1, 1)
    elif con2==2 : make_sa(2, 1)
    elif con2==3 : make_sa(2, 2)
    elif con2==4 : make_sa(1, 2)

    random.shuffle(ex)

    ans_i=0
    c1 = []
    example_list=[]
    for i in range(5):
        if ex[i][1] == 0:
            if ex[i][2] == 0:
                example_list.append('y`=`' + tostr(ex[i][0], True, True) + 'x^2')
            else:
                example_list.append('y`=`' + tostr(ex[i][0], True, True) + 'x^2`' + tostr(ex[i][2], False, False))
        else:
            if ex[i][2] == 0:
                example_list.append('y`=`' + tostr(ex[i][0], True, True) + 'LEFT(x`' + tostr(-ex[i][1], False, False) + 'RIGHT)^2 ')
            else:
                example_list.append('y`=`' + tostr(ex[i][0], True, True) + 'LEFT(x`' + tostr(-ex[i][1], False, False) \
                                    + 'RIGHT)^2 ' + tostr(ex[i][2], False, False))
        if ex[i][3]==1 : ans_i=i
        if con1==0 and ex[i][0]<0 :  c1.append([answer_dict[i], 'LEFT('+str(ex[i][1])+',``'+str(ex[i][2])+'RIGHT)'])
        elif con1==1 and ex[i][0]>0:  c1.append([answer_dict[i], 'LEFT(' + str(ex[i][1]) + ',``' + str(ex[i][2]) + 'RIGHT)'])


    stem = stem.format(cond1=updown[con1], cond2=con2, ex1=example_list[0], ex2=example_list[1],ex3=example_list[2], ex4=example_list[3],ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(cond1=updown[con1], cond2=con2, c1a=c1[0][0], c1b=c1[1][0], c1c=c1[2][0], c2=c1[0][1], c3=c1[1][1], c4=c1[2][1], a1=answer_dict[ans_i])

    return stem, answer, comment


def quadequation313_Stem_086():

    stem = "다음 중 이차함수 $$수식$$y`=`{n1}LEFT(x`{n2})^2`{n3}`$$/수식$$의 그래프가 지나지 않는 사분면을 모두 구한 것은?\n" \
           "① {ex1}    \n② {ex2}    \n③ {ex3}     \n④ {ex4}     \n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{n1}LEFT(x`{n2})^2`{n3}`$$/수식$$의 그래프가 {cond}로 볼록한 포물선이고, 꼭짓점의 좌표가 " \
              "$$수식$$LEFT({c1},``{c2})`$$/수식$$로 제$$수식$${c3}`$$/수식$$사분면에 있다. 따라서 그 그래프는 제$$수식$${c4}`$$/수식$$사분면과 " \
              "제$$수식$${c5}`$$/수식$$사분면을 지나지 않는다.\n\n"

    n1 = rand_not0(-9, 9)
    c1 = rand_not0(-9, 9)
    c2 = rand_not0(-9, 9)
    c3=0
    c4=0
    c5=0

    if c1 > 0 and c2 > 0:
        c3 = 1; c4 = 3; c5 = 4
        n1 = rand_not0(1, 9)
    elif c1 < 0 and c2 > 0:
        c3 = 2; c4 = 3; c5 = 4
        n1 = rand_not0(1, 9)
    elif c1 < 0 and c2 < 0:
        c3 = 3; c4 = 1; c5 = 2
        n1 = rand_not0(-9, -1)
    elif c1 > 0 and c2 < 0:
        c3 = 4; c4 = 1; c5 = 2
        n1 = rand_not0(-9, -1)

    cond=('위' if n1<0 else '아래')

    n2 = -c1
    n3 = c2

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, False)

    ex=[[c4, c5], [c4], [c5], [4-c4, 6-c5]]
    random.shuffle(ex)
    example_list =[]
    ans_i=0
    for i in range(4) :
        if ex[i]==[c4, c5] : ans_i=i
        if len(ex[i])==1 :  example_list.append('제$$수식$$'+str(ex[i][0])+'`$$/수식$$사분면')
        else : example_list.append('제$$수식$$'+str(ex[i][0])+'`$$/수식$$사분면, 제$$수식$$'+str(ex[i][1])+'`$$/수식$$사분면')
    example_list.append('모든 사분면을 지난다.')

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, ex1=example_list[0], ex2=example_list[1],ex3=example_list[2],ex4=example_list[3],ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, cond=cond)
    return stem, answer, comment


def quadequation313_Stem_087():

    stem = "다음 중 아래 조건을 모두 만족시키는 포물선을 그래프로 하는 이차함수의 식은?\n" \
           "$$표$$ (가) 이차함수 $$수식$$ y`=`{n1}x^2`$$/수식$$의 그래프와 폭이 같다.\n" \
           "(나) 꼭짓점이 제$$수식$${n2}`$$/수식$$사분면에 있다.\n" \
           "(다) 그래프는 {n3}로 볼록한 포물선이다. $$/표$$\n" \
           "① $$수식$${ex1}$$/수식$$     \n② $$수식$${ex2}$$/수식$$     \n③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     \n⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "구하는 이차함수의 식을 이차함수의 식을 $$수식$$ y`=`a LEFT(x`-`p RIGHT)^2`+`q`$$/수식$$로 놓으면\n" \
              "(가), (다)에서 $$수식$$ a`=`{c1}`$$/수식$$ ⇨ {c2}, {c3}, {c4}\n" \
              "이들의 꼭짓점의 좌표를 각각 구해보면\n" \
              "{c2} $$수식$$ {c22}`$$/수식$$     {c3} $$수식$$ {c33}`$$/수식$$     {c4} $$수식$$ {c44}`$$/수식$$\n" \
              "따라서 주어진 조건을 모두 만족시키는 이차함수는 {a1}이다.\n\n"

    updown = ['위', '아래']
    n1 = random.randint(1, 4)
    n2 = random.randint(1, 4)
    n3 = random.randint(0, 1)

    ex = []
    if n3 == 0:
        a=-n1
    else:
        a=n1

    if n2 == 1:
        p = rand_not0(1, 9)
        q = rand_not0(1, 9)
    elif n2 == 2:
        p = rand_not0(-9, -1)
        q = rand_not0(1, 9)
    elif n2 == 3:
        p = rand_not0(-9, -1)
        q = rand_not0(-9, -1)
    elif n2 == 4:
        p = rand_not0(1, 9)
        q = rand_not0(-9, -1)

    ex = [[a, p, q, 1], [a, -p, q, -1], [a, p, -q, -1], [-a, p, q, -1], [-a, -p, -q, -1]]
    random.shuffle(ex)

    ans_i = 0
    example_list = []
    comment_list = []
    for i in range(5):
        example_list.append('y`=`' + tostr(ex[i][0], True, True) + 'LEFT(x`' + tostr(-ex[i][1], False, False) \
                                    + 'RIGHT)^2 ' + tostr(ex[i][2], False, False))
        if ex[i][3] == 1: ans_i = i
        if n3 == 0 and ex[i][0] < 0:
            comment_list.append([answer_dict[i], 'LEFT(' + str(ex[i][1]) + ',``' + str(ex[i][2]) + 'RIGHT)'])
        elif n3 == 1 and ex[i][0] > 0:
            comment_list.append([answer_dict[i], 'LEFT(' + str(ex[i][1]) + ',``' + str(ex[i][2]) + 'RIGHT)'])

    str_n1 = tostr(n1, True, True)


    stem = stem.format(n1=str_n1, n2=n2, n3=updown[n3], ex1=example_list[0], ex2=example_list[1],ex3=example_list[2],ex4=example_list[3],ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(c1 = a, c2=comment_list[0][0], c3=comment_list[1][0], c4=comment_list[2][0], \
                             c22=comment_list[0][1], c33=comment_list[1][1], c44=comment_list[2][1], a1=answer_dict[ans_i])

    return stem, answer, comment


def quadequation313_Stem_088():

    stem = "이차함수  $$수식$$ y`=`{n1}LEFT(x`{n2})^2`{n3}`$$/수식$$의 그래프를  $$수식$$ x`$$/수식$$축의 방향으로  $$수식$$ p`$$/수식$$만큼, " \
           "$$수식$$ y`$$/수식$$축의 방향으로  $$수식$$ q`$$/수식$$만큼 평행이동하였더니 $$수식$$ y`=`{n1}x^2`$$/수식$$의 그래프와 일치하였다. " \
           "이 때  $$수식$$ q OVER p`$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ y`=`{n1} LEFT(x`-`p`{n2})^2`{n3}`+`q`$$/수식$$와 $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프가 일치하므로\n" \
              "$$수식$$ -`p`{n2}`=`0`$$/수식$$, $$수식$$ {c1}`+`q`=`0`$$/수식$$\n" \
              "따라서 $$수식$$ p`=`{p}`$$/수식$$, $$수식$$q`=`{q}`$$/수식$$\n" \
              "$$수식$$ q OVER p = {q} OVER {p} `=`{c2}`$$/수식$$\n\n"

    n1 = rand_not0(-9, 9)
    p = rand_not0(-9, 9)
    q = rand_not0(-9, 9)
    while q%p!=0 : q = rand_not0(-9, 9)
    n2 = p
    n3 = -q
    c1 = n3
    c2 = ctr_frac2(q, p)

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, False)
    str_c1 = tostr(c1, True, False)
    str_c2 = make_frac(c2[0], c2[1])

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3)
    answer = answer.format(a1=str_c2)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, c1 =str_c1, c2 = str_c2, p=p, q=q)

    return stem, answer, comment


def quadequation313_Stem_089():

    stem = "이차함수 $$수식$$ y`=`{n1}LEFT(x`{n2} RIGHT)^2`{n3}`$$/수식$$의 그래프를 $$수식$$x`$$/수식$$축의 방향으로 $$수식$$ {n4}`$$/수식$$만큼, " \
           "$$수식$$y`$$/수식$$축의 방향으로 $$수식$$ {n5}`$$/수식$$만큼 평행이동한 그래프를 나타내는 이차함수의 식은?\n" \
           "① $$수식$$y`=`{ex1}$$/수식$$     ② $$수식$$y`=`{ex2}$$/수식$$     \n" \
           "③ $$수식$$y`=`{ex3}$$/수식$$     ④ $$수식$$y`=`{ex4}$$/수식$$     \n⑤ $$수식$$y`=`{ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              " $$수식$$ y`=`{n1}LEFT(x`{c1}`{n2} RIGHT)^2`{n3}`{c2}`=`{c3}`$$/수식$$\n\n"

    n1 = rand_not0(-9, 9)
    n2 = rand_not0(-5, 5)
    n3 = rand_not0(-5, 5)
    n4 = rand_not0(-7, 7)
    n5 = rand_not0(-7, 7)
    c1 = -n4
    c2 = n5

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, False)
    str_c1 = tostr(c1, False, False)
    str_c2 = tostr(c2, False, False)

    ex=[[n1, c1+n2, c2+n3, 1], [n1, c1+n2, n3-c2, -1], [n1, n2-c1, c2+n3, -1], [n1, n2-c1, n3-c2, -1], [n1, c2-c1, n3, -1]]

    ans_i=0
    example_list=[]
    for i in range(5):
        if ex[i][1] == 0:
            if ex[i][2] == 0:
                example_list.append(tostr(ex[i][0], True, True) + 'x^2')
            else:
                example_list.append(tostr(ex[i][0], True, True) + 'x^2`' + tostr(ex[i][2], False, False))
        else:
            if ex[i][2] == 0:
                example_list.append(tostr(ex[i][0], True, True) + 'LEFT(x`' + tostr(ex[i][1], False, False) + 'RIGHT)^2 ')
            else:
                example_list.append(tostr(ex[i][0], True, True) + 'LEFT(x`' + tostr(ex[i][1], False, False) \
                                    + 'RIGHT)^2 ' + tostr(ex[i][2], False, False))
        if ex[i][3]==1 : ans_i=i




    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, n5=n5, ex1=example_list[0], ex2=example_list[1],ex3=example_list[2],ex4=example_list[3],ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_i])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, n5=n5, c1=str_c1, c2=str_c2, c3=example_list[ans_i])

    return stem, answer, comment


def quadequation313_Stem_090():

    stem = "이차함수 $$수식$$ y`=`a LEFT(x`{n1} RIGHT)^2`$$/수식$$의 그래프를 $$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ {n2}`$$/수식$$만큼 " \
           "평행이동하면 점 $$수식$$ LEFT({n3},``{n4} RIGHT)`$$/수식$${jo1} 지난다고 할 때, 상수 $$수식$$a`$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              " $$수식$$ y`=`a LEFT(x`{n1} RIGHT)^2`$$/수식$$의 그래프를 $$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ {n2}`$$/수식$$만큼 " \
              "평행이동한 그래프의 식은 $$수식$$ y`=`a LEFT(x`{n1} RIGHT)^2`{c1}`$$/수식$$\n" \
              "이 그래프가 점 $$수식$$ LEFT({n3},``{n4} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$$ {n4}`=`a TIMES LEFT({n3}`{n1} RIGHT)^2`{c1}`$$/수식$$    $$수식$$ a`=`{a}`$$/수식$$\n\n"

    n1 = rand_not0(-9, 9)
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)
    while abs(n3+n1)>4 or n3+n1==0 : n3 = rand_not0(-9, 9)
    a = rand_not0(-3, 3)
    n4 = (a*(n3+n1)**2)+n2
    c1 = n2
    ans = a

    str_n1 = tostr(n1, False, False)
    str_c1 = tostr(c1, False, False)

    stem = stem.format(n1=str_n1, n2=n2, n3=n3, n4=n4, jo1=proc_jo(n4, 5))
    answer = answer.format(a1=ans)
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, n4=n4, c1=str_c1, jo1=proc_jo(n4, 5), a=a)

    return stem, answer, comment


def quadequation313_Stem_091():

    stem = "이차함수 $$수식$$y`=`LEFT(x`{n1})^2`{n2}`$$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$ {n3}k`$$/수식$$만큼, " \
           "$$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ {n4}k`$$/수식$$만큼 " \
           "평행이동하면 점 $$수식$$ LEFT({n5},``{n6} RIGHT)`$$/수식$${jo1} 지난다. 이때, 양수 $$수식$$k`$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`LEFT(x`{c1}k`{n1})^2`{n2}`{c2}k`$$/수식$$의 그래프가 점 $$수식$$ LEFT({n5},``{n6} RIGHT)`$$/수식$${jo1} 지나므로\n" \
              "$$수식$${n6}`=`LEFT({n5}`{c1}k`{n1})^2`{n2}`{c2}k`$$/수식$$, $$수식$$ k^2`{c3}k`{c4}`=`0`$$/수식$$\n" \
              "$$수식$$LEFT(k`{c5} RIGHT) LEFT(k`{c6} RIGHT)`=`0`$$/수식$$    " \
              "$$수식$$THEREFORE````k`=`{k1} LEFT(BECAUSE`k`&gt;`0 RIGHT)`$$/수식$$\n\n"

    k1 = rand_not0(1, 4)
    k2 = rand_not0(-4, -1)
    while k1+k2==0 : k2 = rand_not0(-4, -1)
    n1 = rand_not0(-6, 6)
    n2 = rand_not0(-6, 6)
    n3 = 1
    n5 = -n1

    c1 = -n3
    c5 = -k1
    c6 = -k2
    c3 = c5+c6
    c4 = c5*c6
    n4 = c3
    c2 = c3
    n6 = n2-c4

    str_n1 = tostr(n1, False, False)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, True, True)
    str_n4 = tostr(n4, True, True)
    str_c1 = tostr(c1, False, True)
    str_c2 = tostr(c2, False, True)
    str_c3 = tostr(c3, False, True)
    str_c4 = tostr(c4, False, False)
    str_c5 = tostr(c5, False, False)
    str_c6 = tostr(c6, False, False)

    ans=k1


    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=str_n4, n5=n5, n6=n6, jo1=proc_jo(n6, 5))
    answer = answer.format(a1=ans)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=str_n4, n5=n5, n6=n6, c1=str_c1, c2=str_c2, c3=str_c3, c4=str_c4, c5=str_c5, \
                             c6=str_c6, jo1=proc_jo(n6, 5), k1=k1)
    return stem, answer, comment


def quadequation313_Stem_092():

    stem = "이차함수 $$수식$$y`=`{n1}LEFT(x`{n2})^2`{n3}`$$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$ a`$$/수식$$만큼, " \
           "$$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ b`$$/수식$$만큼 평행이동하면 $$수식$$ y`=`{n1}x^2`$$/수식$$의 그래프와 일치한다. " \
           "이때, $$수식$$a`+`b`$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{n1}LEFT(x`{n2})^2`{n3}`$$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$ a`$$/수식$$만큼, " \
              "$$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ b`$$/수식$$만큼 평행이동한 그래프를 나타내는 이차함수의 식은\n" \
              "$$수식$$y`=`{n1}LEFT(x`{n2}`-`a)^2`{n3}`+`b`$$/수식$$\n" \
              "이 함수가 $$수식$$ y`=`{n1}x^2`$$/수식$$과 일치하므로\n" \
              "$$수식$${c1}`-`a`=`0`$$/수식$$, $$수식$${c2}`+`b`=`0`$$/수식$$    $$수식$$THEREFORE````a`=`{a}`$$/수식$$, $$수식$$b`=`{b}`$$/수식$$\n" \
              "$$수식$$THEREFORE````a`+`b`=`{c3}`$$/수식$$\n\n"

    n1 = rand_not0(-4, 4)
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)
    a = n2
    b = -n3
    c1 = n2
    c2 = n3
    c3 = a+b
    ans = c3

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, False)

    example_list= make_example(ans)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, ex1=example_list[1], ex2=example_list[2],ex3=example_list[3],ex4=example_list[4],ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, c1=c1, c2=c2, c3=c3, a=a, b=b)
    return stem, answer, comment


def quadequation313_Stem_093():

    stem = "이차함수 $$수식$$y`=`a LEFT(x`{n2} RIGHT)^2`{n3}`$$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$ {n4}`$$/수식$$만큼, " \
           "$$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ {n5}`$$/수식$$만큼 평행이동하면 $$수식$$ y`=`{n1}LEFT(x`+`b RIGHT)^2`+`c`$$/수식$$의 그래프와 " \
           "일치하였다. 이때 $$수식$$a`+`b`+`c`$$/수식$$의 값을 구하시오. (단, $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$, $$수식$$c`$$/수식$$는 상수이다.)\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`a LEFT(x`{n2} RIGHT)^2`{n3}`$$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$ {n4}`$$/수식$$만큼, " \
              "$$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ {n5}`$$/수식$$만큼 평행이동한 그래프의 식은\n" \
              "$$수식$$y`=`a LEFT(x`{c1}`{n2} RIGHT)^2`{n3}`{c2}`=`a LEFT(x`{c3} RIGHT)^2`{c4}`$$/수식$$\n" \
              "이것이 $$수식$$ y`=`{n1}LEFT(x`+`b RIGHT)^2`+`c`$$/수식$$와 일치하므로\n" \
              "$$수식$$a`=`{a}`$$/수식$$, $$수식$$b`=`{b}`$$/수식$$, $$수식$$c`=`{c}`$$/수식$$\n" \
              "$$수식$$THEREFORE````a`+`b`+`c`=`{a}`+`{b_}`+`{c_}`=`{c5}`$$/수식$$\n\n"

    n1 = rand_not0(-4, 4)
    n2 = rand_not0(-3, 3)
    n3 = rand_not0(-5, 5)
    n4 = rand_not0(-7, 7)
    while n2-n4==0 :n4 = rand_not0(-7, 7)
    n5 = rand_not0(-7, 7)
    while n3+n5==0: n5 = rand_not0(-7, 7)
    c1 = -n4
    c2 = n5
    c3 = c1+n2
    c4 = c2+n3
    a = n1
    b = c3
    c = c4
    c5 = a+b+c
    ans = c5

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, False)
    str_c1 = tostr(c1, False, False)
    str_c2 = tostr(c2, False, False)
    str_c3 = tostr(c3, False, False)
    str_c4 = tostr(c4, False, False)


    example_list= make_example(ans)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, n5=n5)
    answer = answer.format(a1=ans)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, n5=n5, c1=str_c1, c2=str_c2, c3=str_c3, c4=str_c4, c5=c5, \
                             a=a, b=b, c=c, b_=brac(b), c_=brac(c))
    return stem, answer, comment


def quadequation313_Stem_094():

    stem = "이차함수 $$수식$$y`=`a LEFT(x`{n2} RIGHT)^2`{n3}`$$/수식$$의 그래프는 이차함수 $$수식$$ y`=`{n1}LEFT(x`+`b RIGHT)^2`+`c`$$/수식$$의 " \
           "그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$ {n4}`$$/수식$$만큼, $$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ {n5}`$$/수식$$만큼 " \
           "평행이동한 것이다. 이때 상수 $$수식$$a,`b,`c`$$/수식$$에 대하여 $$수식$$a`+`b`+`c`$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{n1}LEFT(x`{c1}`+`b RIGHT)^2`+`c`{c2}`$$/수식$${jo1} $$수식$$y`=`a LEFT(x`{n2} RIGHT)^2`{n3}`$$/수식$$의 그래프가 일치하므로\n" \
              "$$수식$$a`=`{a}`$$/수식$$, $$수식$${c3}`+`b`=`{c4}`$$/수식$$, $$수식$$c`{c2}`=`{c5}`$$/수식$$\n" \
              "따라서 $$수식$$a`=`{a}`$$/수식$$, $$수식$$b`=`{b}`$$/수식$$, $$수식$$c`=`{c}`$$/수식$$이므로\n" \
              "$$수식$$a`+`b`+`c`=`{c6}`$$/수식$$\n\n"

    n1 = rand_not0(-4, 4)
    n2 = rand_not0(-3, 3)
    n3 = rand_not0(-5, 5)
    n4 = rand_not0(-7, 7)
    while n2-n4==0 :n4 = rand_not0(-7, 7)
    n5 = rand_not0(-7, 7)
    while n3+n5==0: n5 = rand_not0(-7, 7)
    c1 = -n4
    c2 = n5
    c3 = c1
    c4 = n2
    c5 = n3
    a=n1
    b=c4-c3
    c=c5-c2
    c6 = a+b+c
    ans = c6

    str_n1 = tostr(n1, True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, False)
    str_c1 = tostr(c1, False, False)
    str_c2 = tostr(c2, False, False)

    example_list= make_example(ans)

    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, n5=n5, \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, n4=n4, n5=n5, c1=str_c1, c2=str_c2, c3=c3, c4=c4, c5=c5, c6=c6, \
                             a=a, b=b, c=c, jo1=proc_jo(n2, 2))
    return stem, answer, comment


def quadequation313_Stem_095():

    stem = "이차함수 $$수식$$y`=`a LEFT(x`{n2} RIGHT)^2`{n3}`$$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$ {n4}`$$/수식$$만큼, " \
           "$$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ {n5}`$$/수식$$만큼 평행이동한 그래프의 꼭짓점의 좌표를 $$수식$$ LEFT(p,``q RIGHT)`$$/수식$$, " \
           "축의 방정식을 $$수식$$x`=`m`$$/수식$$이라 할 때, $$수식$$p`+`q`+`m`$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`a LEFT(x`{n2} RIGHT)^2`{n3}`$$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$ {n4}`$$/수식$$만큼, " \
              "$$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ {n5}`$$/수식$$만큼 평행이동한 그래프를 나타내는 이차함수의 식은\n" \
              "$$수식$$y`=`a LEFT(x`{c1}`{n2} RIGHT)^2`{n3}`{c2}`=`a LEFT(x`{c3} RIGHT)^2`{c4}`$$/수식$$\n" \
              "이 함수의 그래프의 꼭짓점의 좌표는 $$수식$$ LEFT({p},``{q} RIGHT)`$$/수식$$, 축의 방정식은 $$수식$$x`=`{m}`$$/수식$$이므로" \
              "$$수식$$p`=`{p}`$$/수식$$, $$수식$$q`=`{q}`$$/수식$$, $$수식$$m`=`{m}`$$/수식$$\n" \
              "$$수식$$THEREFORE````p`+`q`+`m`=`{c5}`$$/수식$$\n\n"

    n2 = rand_not0(-3, 3)
    n3 = rand_not0(-5, 5)
    n4 = rand_not0(-7, 7)
    while n2-n4==0 :n4 = rand_not0(-7, 7)
    n5 = rand_not0(-7, 7)
    while n3+n5==0: n5 = rand_not0(-7, 7)
    c1 = -n4
    c2 = n5
    c3 = c1+n2
    c4 = n3+c2
    p = -c3
    q = c4
    m = -c3
    c5 = p+q+m
    ans = c5

    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, False)
    str_c1 = tostr(c1, False, False)
    str_c2 = tostr(c2, False, False)
    str_c3 = tostr(c3, False, False)
    str_c4 = tostr(c4, False, False)

    example_list= make_example(ans)

    stem = stem.format(n2=str_n2, n3=str_n3, n4=n4, n5=n5, \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n2=str_n2, n3=str_n3, n4=n4, n5=n5, c1=str_c1, c2=str_c2, c3=str_c3, c4=str_c4, c5=c5, p=p, q=q, m=m)
    return stem, answer, comment


def quadequation313_Stem_096():

    stem = "이차함수 $$수식$$y`=`{n1}x^2`{n3}`$$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$ k`$$/수식$$만큼, " \
           "$$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ {n5}`$$/수식$$만큼 평행이동한 그래프의 꼭짓점이 직선 $$수식$$y`=`{n6}x`{n7}`$$/수식$$ 위에 " \
           "있을 때, 상수 $$수식$$k`$$/수식$$의 값은?\n" \
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"

    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{n1}x^2`{n3}`$$/수식$$의 그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$k`$$/수식$$만큼, " \
              "$$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ {n5}`$$/수식$$만큼 평행이동한 그래프를 나타내는 이차함수의 식은\n" \
              "$$수식$$y`=`{n1} LEFT(x`-`k RIGHT)^2`{n3}`{c1}`=`{n1} LEFT(x`-`k RIGHT)^2`{c2}`$$/수식$$\n" \
              "이 함수의 그래프의 꼭짓점의 좌표는 $$수식$$ LEFT(k,``{c3} RIGHT)`$$/수식$$이고 이 점이 직선 $$수식$$y`=`{n6}x`{n7}`$$/수식$$ 위에 있으므로\n" \
              "$$수식$${c3}`=`{n6}k`{n7}`$$/수식$$, $$수식$${c4}k`=`{c5}`$$/수식$$    $$수식$$THEREFORE````k`=`{k}`$$/수식$$\n\n"

    n1 = rand_not0(-4, 4)
    n3 = rand_not0(-5, 5)
    n5 = rand_not0(-7, 7)
    n6 = rand_not0(-4, 4)
    n7 = (rand_not0(-6, -1) if n5+n3<0 else rand_not0(1, 6))
    while n5+n3-n7==0 : n7 = (rand_not0(-6, -1) if n5+n3<0 else rand_not0(1, 6))
    c1 = n5
    c2 = n5+n3
    c3 = c2
    c4 = (n6 if n6>0 else -n6)
    c5 = (c3-n7 if n6>0 else n7-c3)
    k = ctr_frac2(c5, c4)

    str_n1 = tostr(n1, True, True)
    str_n3 = tostr(n3, False, False)
    str_n6 = tostr(n6, True, True)
    str_n7 = tostr(n7, False, False)
    str_c1 = tostr(c1, False, False)
    str_c2 = tostr(c2, False, False)
    str_c2 = ('' if str_c2=='`0' else str_c2)
    str_c4 = tostr(c4, True, True)
    str_k = make_frac(k[0], k[1])

    example_list = make_fraction_example2(k[0], k[1], k[1])

    stem = stem.format(n1=str_n1, n3=str_n3, n5=n5, n6=str_n6, n7=str_n7, \
                       ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=str_n1, n3=str_n3, n5=n5, n6=str_n6, n7=str_n7, c1=str_c1, c2=str_c2, c3=c3, c4=str_c4, c5=c5, k=str_k)
    return stem, answer, comment


def quadequation313_Stem_097():

    stem = "이차함수 $$수식$$y`=`{n1}x^2`$$/수식$$의 그래프와 모양이 같고, 꼭짓점의 좌표가 $$수식$$ LEFT({n2},``{n3} RIGHT)`$$/수식$$인 포물선을 " \
           "그래프로 하는 이차함수의 식을 $$수식$$y`=`a LEFT(x`+`p RIGHT)^2`+`q`$$/수식$$라 할 때, 상수 $$수식$$a`$$/수식$$, $$수식$$p`$$/수식$$, " \
           "$$수식$$q`$$/수식$$에 대하여 $$수식$$a`+`p`+`q`$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "주어진 조건을 만족시키는 이차함수의 식은\n" \
              "$$수식$$y`=`{n1} LEFT(x`{c1} RIGHT)^2`{c2}`$$/수식$$이므로\n" \
              "$$수식$$a`=`{a}`$$/수식$$, $$수식$$p`=`{p}`$$/수식$$, $$수식$$q`=`{q}`$$/수식$$\n" \
              "$$수식$$THEREFORE````a`+`p`+`q`=`{c3}`$$/수식$$\n\n"

    n1 = rand_not0(-4, 4)
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-9, 9)
    c1 = -n2
    c2 = n3
    a = n1
    p = c1
    q = c2
    c3 = a+p+q
    ans = c3

    str_n1 = tostr(n1, True, True)
    str_c1 = tostr(c1, False, False)
    str_c2 = tostr(c2, False, False)


    stem = stem.format(n1=str_n1, n2=n2, n3=n3)
    answer = answer.format(a1=ans)
    comment = comment.format(n1=str_n1, n2=n2, n3=n3, c1=str_c1, c2=str_c2, c3=c3, a=a, p=p, q=q)
    return stem, answer, comment


def quadequation313_Stem_098():

    stem = "이차함수 $$수식$$y`=`{n1} LEFT(x`{n2} RIGHT)^2`{n3}`$$/수식$$의 그래프는 $$수식$$ y`=`{n1}x^2`$$/수식$$의 " \
           "그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$ p`$$/수식$$만큼, $$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ q`$$/수식$$만큼 " \
           "평행이동한 것이다. 이때 $$수식$$q OVER p`$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "이차함수 $$수식$$y`=`{n1} LEFT(x`{n2} RIGHT)^2`{n3}`$$/수식$$의 그래프는 $$수식$$ y`=`{n1}x^2`$$/수식$$의 " \
              "그래프를 $$수식$$ x`$$/수식$$축의 방향으로 $$수식$$ {p}`$$/수식$$만큼, $$수식$$ y`$$/수식$$축의 방향으로 $$수식$$ {q}`$$/수식$$만큼 " \
              "평행이동한 것이다.\n" \
              "따라서 $$수식$$p`=`{p}`$$/수식$$, $$수식$$q`=`{q}`$$/수식$$이므로\n" \
              "$$수식$$q OVER p`=`{q} OVER {p}`=`{c1}`$$/수식$$\n\n"

    n1 = ctr_frac2(rand_not0(-9, 9), rand_not0(-9, 9))
    n2 = rand_not0(-9, 9)
    n3 = rand_not0(-10, 10)
    p = -n2
    q = n3
    c1 = ctr_frac2(q, p)

    str_n1 = make_frac2(n1[0], n1[1], True, True)
    str_n2 = tostr(n2, False, False)
    str_n3 = tostr(n3, False, False)
    str_c1 = make_frac(c1[0], c1[1])


    stem = stem.format(n1=str_n1, n2=str_n2, n3=str_n3)
    answer = answer.format(a1=str_c1)
    comment = comment.format(n1=str_n1, n2=str_n2, n3=str_n3, c1=str_c1, p=p, q=q)
    return stem, answer, comment

def quadequation313_Stem_099():
    stem = "이차함수 $$수식$$y`=` a LEFT ( x`-`{x1} RIGHT )  ^2 `-`{x2}`$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$${x3}$$/수식$$만큼, " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$${x4}$$/수식$$만큼 평행이동하였더니 " \
           "$$수식$$y`=`{x5}(x`+`b)^2`+c`$$/수식$$의 그래프와 일치하였다. " \
           "이때 $$수식$$a`b`c$$/수식$$의 값은? (단, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$는 상수이다.)\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {a}\n"
    comment = "(해설)\n" \
              "$$수식$$y=a LEFT ( x`-`{x1} RIGHT ) ^2 `-`{x2}`$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$${x3}$$/수식$$만큼, " \
              "$$수식$$y$$/수식$$축의 방향으로 $$수식$${x4}$$/수식$$만큼 평행이동한 그래프의 식은 "\
              "$$수식$$y`=`a LEFT ( x`-`{x1}`-{x3} RIGHT ) ^2 `-`{x2}`+`{x4} `=`a(x {x6})^2 `{k}` {x7}$$/수식$$\n" \
              "이것이 $$수식$$y`= {x5}(x`+`b)^2`+c`$$/수식$$와 일치하므로\n"\
              "$$수식$$a `=` {x5}$$/수식$$, $$수식$$b `=` {x6} $$/수식$$, $$수식$$c `=` {x7}$$/수식$$\n"\
              "$$수식$$THEREFORE~a`b`c`=`{x8}$$/수식$$\n\n"

    x1 = np.random.randint(1, 5)
    x2 = np.random.randint(1, 5)
    x3 = np.random.randint(1, 5)
    x4 = np.random.randint(1, 5)
    x5 = np.random.randint(-5, 5)
    while x5 == 0 or x5 == 1 or x5 == -1:
        x5 = np.random.randint(-5, 5)

    x6 = -x1 -x3
    x7 = x4 - x2
    x8 = x5 * x6 * x7

    if x7 >= 0 :
        k = "+"
    else :
        k = ""
    candidates = [x8, -x8, x8 + 2, -x8 -2, x8 - 2]
    if x8 == 0 :
        candidates = [x8, x8 + 2, x8 - 2, x8 + 4, x8 - 4]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == x8:
            correct_idx = idx
            break

    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(a = answer_dict[correct_idx])
    comment = comment.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x6 = x6, x7 = x7, x8 = x8, k = k)
    return stem, answer, comment


def quadequation313_Stem_100():
    stem = "직선 $$수식$$x`=`{p}$$/수식$${j1} 축으로 하고 두 점 $$수식$$LEFT ( {x1}, ``{y1} RIGHT ) $$/수식$$, $$수식$$LEFT ( {x2}, ``{y2} RIGHT ) $$/수식$${j2} " \
           "지나는 포물선을 그래프로 하는 이차함수의 식을 $$수식$$y = a LEFT ( x - p RIGHT ) ^2 +q`$$/수식$$라 할 때, 상수 $$수식$$a$$/수식$$, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$에 대하여 "\
           "$$수식$$a `+` p `+` q$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "축의 방정식이 $$수식$$x `=` {p}$$/수식$$이므로 $$수식$$p `=` {p}$$/수식$$\n"\
              "즉 $$수식$$y=a LEFT( x - {p} RIGHT ) ^2 +q`$$/수식$$의 그래프가 점 $$수식$$LEFT ( {x1},`` {y1} RIGHT ) $$/수식$${j3} 지나므로\n"\
              "$$수식$${y1} = a TIMES LEFT ( {x1} `-` {p} RIGHT )^2 +q$$/수식$$\n"\
              "$$수식$$THEREFORE~ {t0}a+q={y1} ````````````CDOTS CDOTS㉠$$/수식$$\n"\
              "또 점 $$수식$$LEFT ( {x2},`` {y2} RIGHT ) $$/수식$${j2} 지나므로\n"\
              "$$수식$${y2} = a TIMES({x2} - {p}) ^2 +q$$/수식$$\n"\
              "$$수식$$THEREFORE~ {t1}a+q={y2} ````````````CDOTS CDOTS㉡$$/수식$$\n"\
              "㉠, ㉡을 연립하여 풀면 $$수식$$a `=` {a}$$/수식$$, $$수식$$ q `=` {q}$$/수식$$\n"\
              "$$수식$$THEREFORE~a`+`p`+`q`=`{a1}$$/수식$$\n\n"

    p = np.random.randint(1, 6)
    a = np.random.randint(1, 5)
    q = np.random.randint(1, 10)

    x1 = np.random.randint(0, 6)
    x2 = np.random.randint(0, 6)

    while x1 == p or abs(x1-p) == 1:
        x1 = np.random.randint(0, 6)
    while x1 == x2 or x2 == p or abs(x2-p) == 1 :
        x2 = np.random.randint(0, 6)

    t0 = (x1 - p)**2

    y1 = a * t0 + q

    t1 = (x2 - p) ** 2
    y2 = a * t1 + q

    while y1 == y2 :
        x1 = np.random.randint(0, 6)
        x2 = np.random.randint(0, 6)

        while x1 == p:
            x1 = np.random.randint(0, 6)
        while x1 == x2 or x2 == p:
            x2 = np.random.randint(0, 6)

        t0 = (x1 - p) ** 2
        y1 = a * t0 + q

        t1 = (x2 - p) ** 2
        y2 = a * t1 + q


    a1 = a + p + q

    j1 = proc_jo(p, 4)
    j2 = proc_jo(y2, 4)
    j3 = proc_jo(y1, 4)
    stem = stem.format(a = a, p = p, x1 = x1, x2 = x2, y1 = y1, y2 = y2, j1 = j1, j2 = j2)
    answer = answer.format(a1 = a1)
    comment = comment.format(a = a, p = p, q = q, a1 = a1, x1 = x1, x2 = x2, y1 = y1, y2 = y2, t0 = t0, t1 = t1, j2 = j2, j3 = j3)
    return stem, answer, comment

def quadequation313_Stem_101():
    stem = "다음 중 꼭짓점의 좌표가 $$수식$$LEFT ( 0, ``{y1} RIGHT )$$/수식$$이고, 점 $$수식$$LEFT ( {x2}, `` {y2} RIGHT) $$/수식$${j1} 지나는 이차함수의 그래프 위의 점인 것은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "꼭짓점의 좌표가 $$수식$$LEFT ( 0, ``{y1} RIGHT )$$/수식$$이므로 이차함수의 식을 \n"\
              "$$수식$$y`=`ax^2`+{y1}`$$/수식$$로 놓을 수 있다.\n"\
              "$$수식$$y`=`ax^2`+{y1}`$$/수식$$의 그래프가 점 $$수식$$LEFT ( {x2}, ``{y2} RIGHT )$$/수식$${j1} 지나므로\n"\
              "$$수식$${y2} `=` a `TIMES` LEFT ( {x2} RIGHT ) ^2 `+` {y1}$$/수식$$\n"\
              "$$수식$$THEREFORE~a`=`{a}$$/수식$$\n"\
              "따라서 y`=`{a}x^2`+{y1}`$$/수식$$의 그래프 위의 점인 것은 {anum}이다.\n\n"

    a = np.random.randint(1, 6)
    y1 = np.random.randint(1, 10)

    x2 = np.random.randint(-5, 5)
    while x2 == 0 :
        x2 = np.random.randint(-5, 5)
    y2 = a * (x2**2) + y1

    j1 = proc_jo(y2, 4)

    x_list = []
    for i in range(-5, 6):
        if i != 0 and i != x2 :
            x_list.append(i)

    x_1 = x_list.pop(np.random.randint(0, len(x_list)))
    y_1 = a * (x_1**2) + y1
    a1 = f"LEFT ( {x_1}, `` {y_1} RIGHT )"

    x_2 = x_list.pop(np.random.randint(0, len(x_list)))
    tmp = np.random.randint(-3, 4)
    while tmp == 0 :
        tmp = np.random.randint(-3, 4)
    y_2 = a * (x_2**2) + y1 + tmp
    a2 = f"LEFT ( {x_2}, `` {y_2} RIGHT )"

    x_3 = x_list.pop(np.random.randint(0, len(x_list)))
    tmp = np.random.randint(-3, 4)
    while tmp == 0:
        tmp = np.random.randint(-3, 4)
    y_3 = a * (x_3 ** 2) + y1 + tmp
    a3 = f"LEFT ( {x_3}, `` {y_3} RIGHT )"

    x_4 = x_list.pop(np.random.randint(0, len(x_list)))
    tmp = np.random.randint(-3, 4)
    while tmp == 0:
        tmp = np.random.randint(-3, 4)
    y_4 = a * (x_4 ** 2) + y1 + tmp
    a4 = f"LEFT ( {x_4}, `` {y_4} RIGHT )"

    x_5 = x_list.pop(np.random.randint(0, len(x_list)))
    tmp = np.random.randint(-3, 4)
    while tmp == 0:
        tmp = np.random.randint(-3, 4)
    y_5 = a * (x_5 ** 2) + y1 + tmp
    a5 = f"LEFT ( {x_5}, `` {y_5} RIGHT )"

    candidates = [a1, a2, a3, a4, a5]
    np.random.shuffle(candidates)
    [a_1, a_2, a_3, a_4, a_5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == a1:
            correct_idx = idx
            break

    stem = stem.format(y1 = y1, x2 = x2, y2 = y2, j1 = j1, a1 = a_1, a2 = a_2, a3 = a_3, a4 = a_4, a5 = a_5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(y1 = y1, x2 = x2, y2 = y2, j1 = j1, a = a, anum = answer_dict[correct_idx])
    return stem, answer, comment

def quadequation313_Stem_102():
    stem = "이차함수 $$수식$$y`=` - 1 over {a_} x ^2 `$$/수식$$의 그래프와 모양이 같고, 꼭짓점의 좌표가 $$수식$$LEFT ( {p}, ``{q} RIGHT )$$/수식$$인 포물선을 그래프로 하는 " \
           "이차함수의 식을 $$수식$$y = a(x-p) ^2 +q`$$/수식$$라 할 때, " \
           "상수 $$수식$$a$$/수식$$, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$에 대하여 $$수식$$a`p`q$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "이차함수 $$수식$$ y`=` - 1 over {a_} x ^2 `$$/수식$$의 그래프와 모양이 같으므로 구하는 이차함수의 식을 " \
              "$$수식$$ y = - 1 over {a_} LEFT ( x-p RIGHT ) ^2 +q`$$/수식$$로 놓을 수 있다. 꼭짓점의 좌표가 $$수식$$ LEFT ( {p}, ``{q} RIGHT )$$/수식$$이므로 "\
              "$$수식$$ y = - 1 over {a_} LEFT ( x{op1}{p_} RIGHT ) ^2 {op2}{q} $$/수식$$\n" \
              "따라서 $$수식$$ a`=` - 1 over {a_}`, p`=`{p}`, q`=`{q} $$/수식$$이므로\n"\
              "$$수식$$ a`p`q` =` {an} $$/수식$$\n\n"

    a_ = np.random.randint(2, 6)

    p = a_ * np.random.randint(-2, 3)
    while p == 0 :
        p = a_ * np.random.randint(-2, 3)
    if p < 0 :
        op1 = '+'
        p_ = -1 * p
    else :
        op1 = '-'
        p_ = p

    q = np.random.randint(-9, 10)
    while q == 0 :
        q = np.random.randint(-9, 10)
    if q > 0 :
        op2 = '+'
    else :
        op2 = ''

    an = -1 * int((1/a_) * p * q)

    candidates = [an, -an, an*2, -an*2, an*3]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break

    stem = stem.format(a_ = a_, p = p, q = q, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(a_ = a_, p = p, q = q, p_ = p_, op1 = op1, op2 = op2, an = an)
    return stem, answer, comment


def quadequation313_Stem_103():
    stem = "이차함수 $$수식$$y`=`a(x`-`p)  ^2 `+ {q}`$$/수식$$의 그래프가 직선 $$수식$$x `=` {p}$$/수식$${j1} 축으로 하고 " \
           "점 $$수식$$LEFT ( {x1}, `` {y1} RIGHT)$$/수식$${j2} 지날 때, $$수식$$p over a$$/수식$$의 값을 구하시오. " \
           "(단, $$수식$$a$$/수식$$, $$수식$$p$$/수식$$는 상수이다.)\n"
    answer = "(답): {an}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` a (x`-`p) ^2 `+{q}`$$/수식$$의 그래프가 직선 $$수식$$x`=`{p}`$$/수식$${j1} 축으로 하므로 " \
              "$$수식$$p `=` {p}$$/수식$$\n" \
              "따라서 $$수식$$y`=`a(x `{op}` {p_}) ^2 `+{q}`$$/수식$$의 그래프가 점 $$수식$$LEFT ( {x1}, `` {y1} RIGHT)$$/수식$${j2} 지나므로\n"\
              "$$수식$${y1} `=` a({x1}`{op}`{p_}) ^2 `+{q}````````````````THEREFORE~a`=`{a}$$/수식$$\n"\
              "$$수식$$THEREFORE~ p over a  `=` {p} over {a}`=`{an}$$/수식$$\n\n"

    a = np.random.randint(-5, 6)
    while a == 0 :
        a = np.random.randint(-5, 6)

    p = a * np.random.randint(-4, 5)
    while p == 0 :
        p = a * np.random.randint(-4, 5)

    if p > 0 :
        op = '-'
        p_ = p
    else :
        op = '+'
        p_ = p * -1
    q = np.random.randint(1, 10)

    x1 = np.random.randint(-3, 4)
    while x1 == p :
        x1 = np.random.randint(-5, 6)
    y1 = a * ((x1 - p)**2) + q
    an = int(p / a)

    j1 = proc_jo(p, 4)
    j2 = proc_jo(y1, 4)

    stem = stem.format(q = q, p = p, j1 = j1, j2 = j2, x1 = x1, y1 = y1)
    answer = answer.format(an = an)
    comment = comment.format(a = a, p = p, q = q, p_ = p_, op = op, j1 = j1, j2 = j2, x1 = x1, y1 = y1, an = an)
    return stem, answer, comment


def quadequation313_Stem_104():
    stem = "이차함수 $$수식$$y`=`{a}(x`+`{p}) ^2 `- {q}$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$$b$$/수식$$만큼 평행이동하면 $$수식$$y `=` {a} x^2$$/수식$$의 그래프와 일치한다. " \
           "이때 $$수식$$a `+` b$$/수식$$의 값을 구하시오.\n"
    answer = "(답): {an}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{a}(x`+`{p}) ^2 `- {q}$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, " \
              "$$수식$$y$$/수식$$축의 방향으로 $$수식$$b$$/수식$$만큼 평행이동한 그래프를 나타내는 이차함수의 식은\n"\
              "$$수식$$y`=`{a}(x`+`{p}`-`a) ^2 `-{q}`+`b$$/수식$$\n"\
              "이 함수가 $$수식$$y `=` {a} x^2$$/수식$$과 일치하므로\n"\
              "$$수식$${p} `-` a `=` 0$$/수식$$, $$수식$$-{q} `+` b `=` 0 ````````````````THEREFORE~a`=`{p}`$$/수식$$, $$수식$$b `=` {q}$$/수식$$\n"\
              "$$수식$$THEREFORE~ a`+`b`=`{an}$$/수식$$\n\n"

    a = np.random.randint(-9, 10)
    while a == 0 :
        a = np.random.randint(-9, 10)

    p = np.random.randint(1, 5)
    q = p * np.random.randint(1, 6)
    while q == 0 :
        q = p * np.random.randint(-5, 6)
    an = p+q

    stem = stem.format(a = a, p = p, q = q)
    answer = answer.format(an = an)
    comment = comment.format(a = a, p = p, q = q, an = an)
    return stem, answer, comment


def quadequation313_Stem_105():
    stem = "이차함수 $$수식$$y`=`a(x`+`{p}) ^2 `-{q}$$/수식$$의 그래프는 이차함수 " \
           "$$수식$$y`=`{a_}(x`+`b) ^2 `+c$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$${x}$$/수식$$만큼, " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$${y}$$/수식$$만큼 평행이동한 것이다. " \
           "이때 상수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$에 대하여 $$수식$$a`b`c$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${an}$$수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{a_}(x{op0}`{x_}+`b`) ^2 `+c`{op1}`{y}$$/수식$$과 $$수식$$y`=`a(x`+`{p}) ^2 `-{q}$$/수식$$의 그래프가 일치하므로 " \
              "$$수식$$ a `=` {a}$$/수식$$, $$수식$$ {x__} `+` b `=` {p}$$/수식$$, $$수식$$ c `{op1} {y} `=` -{q}$$/수식$$\n"\
              "따라서 $$수식$$ a `=` {a}$$/수식$$, $$수식$$ b `=` {b}$$/수식$$, $$수식$$ c `=` {c}$$/수식$$이므로\n"\
              "$$수식$$a`b`c `=` {an}$$/수식$$\n\n"

    a = np.random.randint(-2, 3)
    while a == 0 :
        a = np.random.randint(-2, 3)
    if a == -1 :
        a_ = '-'
    elif a == 1 :
        a_ = ''
    else :
        a_ = a

    p = np.random.randint(1, 6)
    q = np.random.randint(1, 6)

    x = np.random.randint(-5, 6)
    while x == 0 :
        x = np.random.randint(-5, 6)
    if x < 0 :
        op0 = '+'
        x_ = -1 * x
    else :
        op0 = '-'
        x_ = x
    x__ = -1 * x
    y = np.random.randint(-5, 6)
    while y == 0 :
        y = np.random.randint(-5, 6)
    if y > 0 :
        op1 = '+'
    else :
        op1 = ''

    b = p - x__
    c = -q - y

    an = a * b * c

    stem = stem.format(a_ = a_, p = p, q = q, x = x, y = y)
    answer = answer.format(an = an)
    comment = comment.format(a_ = a_, a = a, b = b, c = c, op0 = op0, op1 = op1, x = x, y = y, x_ = x_, x__ = x__, p = p, q = q, an = an)
    return stem, answer, comment


def quadequation313_Stem_106():
    stem = "이차함수 $$수식$$y=a LEFT ( x`+`{a} RIGHT ) ^2 `-`{b}`$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$${x}$$/수식$$만큼, " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$${y}$$/수식$$만큼 평행이동한 그래프의 꼭짓점의 좌표를 $$수식$$LEFT ( p, `` q RIGHT )$$/수식$$, " \
           "축의 방정식을 $$수식$$x `=` m$$/수식$$이라 할 때, $$수식$$p`q`m$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${an}$$수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y=a LEFT ( x`+`{a} RIGHT ) ^2 `-`{b}`$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$${x}$$/수식$$만큼, " \
              "$$수식$$y$$/수식$$축의 방향으로 $$수식$${y}$$/수식$$만큼 평행이동한 그래프를 나타내는 이차함수의 식은 \n"\
              "$$수식$$y`=` a LEFT ( x`+`{a}`-`({x}) RIGHT ) ^2 `-{b}`{op0}`{y}`=` a(x`{op1}`{p_}) ^2 `{op2}`{q}$$/수식$$\n"\
              "이 함수의 그래프의 꼭짓점의 좌표는 $$수식$$ LEFT ( {p}, {q} RIGHT )$$/수식$$, 축의 방정식은 $$수식$$x `=` {p} $$/수식$$이므로\n"\
              "$$수식$$ p `=` {p}$$/수식$$, $$수식$$ q `=` {q}$$/수식$$, $$수식$$ m `=` {m}$$/수식$$\n"\
              "$$수식$$THEREFORE~ p`q`m `=`{an}$$/수식$$\n\n"

    a = np.random.randint(1, 5)
    b = np.random.randint(1, 5)
    x = np.random.randint(-4, 5)
    while x == 0 or x == a:
        x = np.random.randint(-4, 5)
    y = np.random.randint(-4, 5)
    while y == 0 or y == b:
        y = np.random.randint(-4, 5)
    if y > 0 :
        op0 = '+'
    else :
        op0 = ''

    p_ = a - x
    if p_ > 0 :
        op1 = '+'
    else :
        op1 = ''
    p = -1 * p_

    q = -b + y
    if q > 0 :
        op2 = '+'
    else :
        op2 = ''
    m = p
    an = p * q * m

    stem = stem.format(a = a, b = b, x = x, y = y)
    answer = answer.format(an = an)
    comment = comment.format(a = a, b = b, x = x, y = y, op0 = op0, op1 = op1, op2 = op2, p = p, p_ = p_, q = q, m = m, an = an)
    return stem, answer, comment


def quadequation313_Stem_107():
    stem = "직선 $$수식$$x `=` {x0}$$/수식$${j1} 축으로 하고 두 점 $$수식$$LEFT ( {x1}, {y1} RIGHT )$$/수식$$, $$수식$$LEFT ( {x2}, {y2} RIGHT )$$/수식$$" \
           "{j2} 지나는 포물선을 그래프로 하는 이차함수의 식을 $$수식$$y = a LEFT ( x - p RIGHT ) ^2 +q`$$/수식$$라 할 때, " \
           "상수 $$수식$$a$$/수식$$, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$에 대하여 $$수식$$a`p`q$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${an}$$수식$$\n"
    comment = "(해설)\n" \
              "축의 방정식이 이므로 $$수식$$x `=` {x0}$$/수식$$이므로 $$수식$$p `=` {x0}$$/수식$$\n" \
              "즉 $$수식$$y = a LEFT ( x - {x0} RIGHT ) ^2 +q`$$/수식$$의 그래프가 점 $$수식$$LEFT ( {x1}, {y1} RIGHT )$$/수식$${j3} 지나므로\n"\
              "$$수식$$ {y1} = a TIMES LEFT ( {x1} - {x0}) ^2 +q $$/수식$$\n"\
              "$$수식$$THEREFORE~{t0}a+q={y1}````````````````CDOTS CDOTS㉠$$/수식$$\n"\
              "또 점 $$수식$$LEFT ( {x2}, {y2} RIGHT )$$/수식$${j2} 지나므로\n"\
              "$$수식$${y2} = a TIMES LEFT ( {x2} - {x0} RIGHT ) ^ 2 +q$$/수식$$\n"\
              "$$수식$$THEREFORE~{t1}a+q={y2}````````````````CDOTS CDOTS㉡$$/수식$$\n"\
              "㉠, ㉡을 연립하여 풀면 $$수식$$a = {a}$$/수식$$, $$수식$$q = {q}$$/수식$$\n"\
              "$$수식$$THEREFORE~a`p`q`=`{an}$$/수식$$\n\n"

    a = np.random.randint(-3, 4)
    while a == 0 :
        a = np.random.randint(-3, 4)
    p = np.random.randint(1, 6)
    x0 = p
    q = np.random.randint(1, 10)

    x1 = np.random.randint(-3, 4)
    while x1 == x0 :
        x1 = np.random.randint(-3, 4)
    y1 = a * ((x1 - x0)**2) + q

    x2 = np.random.randint(-3, 4)
    while x2 == x0 or x2 == x1 :
        x2 = np.random.randint(-3, 4)
    y2 = a * ((x2 - x0)**2) + q

    t0 = (x1-x0)**2
    t1 = (x2-x0)**2
    if t0 == 1 :
        t0 = ''
    if t1 == 1 :
        t1 = ''

    an = a * p * q

    j1 = proc_jo(x0, 4)
    j2 = proc_jo(y2, 4)
    j3 = proc_jo(y1, 4)

    stem = stem.format(x0 = x0, x1 = x1, x2 = x2, y1 = y1, y2 = y2, j1 =j1, j2 = j2)
    answer = answer.format(an = an)
    comment = comment.format(x0 = x0, x1 = x1, x2 = x2, y1 = y1, y2 = y2, j1 =j1, j2 = j2, j3 = j3, t0 = t0, t1 = t1, a = a, q = q, an = an)
    return stem, answer, comment


def quadequation313_Stem_108():
    stem = "이차함수 $$수식$$y`=`- 1 over {a_} x ^2 `$$/수식$$의 그래프와 모양이 같고, " \
           "꼭짓점의 좌표가 $$수식$$LEFT ( {x0}, ``{y0} RIGHT ) $$/수식$$인 포물선을 그래프로 하는 이차함수의 식을 " \
           "$$수식$$y = a LEFT ( x - p RIGHT ) ^2 +q`$$/수식$$라 할 때, " \
           "상수 $$수식$$a$$/수식$$, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$에 대하여 $$수식$${k}a `+` p `+` q$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${an}$$수식$$\n"
    comment = "(해설)\n" \
              "이차함수 $$수식$$y`=`- 1 over {a_} x ^2 `$$/수식$$의 그래프와 모양이 같으므로 " \
              "구하는 이차함수의 식을 $$수식$$y = - 1 over {a_} (x-p) ^2 +q`$$/수식$$로 놓을 수 있다. " \
              "꼭짓점의 좌표가 이므로 $$수식$$LEFT ( {x0}, ``{y0} RIGHT ) $$/수식$$이므로 $$수식$$y=- 1 over {a_} (x {op0} {x0_}) ^2 {op1} {y0_}$$/수식$$\n"\
              "따라서 $$수식$$ a `=` - 1 over {a_}$$/수식$$, $$수식$$ p `=` {x0}$$/수식$$, $$수식$$ q `=` {y0}$$/수식$$이므로\n"\
              "$$수식$${k}a `+` p `+` q `=` {an}$$/수식$$\n\n"

    a_ = np.random.randint(2, 6)

    k = a_ * [-2, -1, 1, 2][np.random.randint(0, 4)]
    x0 = np.random.randint(-9, 10)
    y0 = np.random.randint(-9, 10)
    while x0 == 0 :
        x0 = np.random.randint(-9, 10)
    while y0 == 0 :
        y0 = np.random.randint(-9, 10)

    if x0 > 0 :
        op0 = '-'
        x0_ = x0
    else :
        op0 = '+'
        x0_ = -x0

    if y0 > 0 :
        op1 = '+'
        y0_ = y0
    else :
        op1 = ''
        y0_ = y0

    an =  int(-1*k*(1/a_) + x0 + y0)

    stem = stem.format(a_ = a_, x0 = x0, y0 = y0, k = k)
    answer = answer.format(an = an)
    comment = comment.format(a_ = a_, x0 = x0, y0 = y0, x0_ = x0_, y0_ = y0_, op0 = op0, op1 = op1, an = an, k = k)
    return stem, answer, comment



def quadequation313_Stem_109():
    stem = "이차함수 $$수식$$y = {a}x^2`$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$${yb}$$/수식$$만큼 평행이동하면 두 점 $$수식$$LEFT ( {x1}, ``b RIGHT)$$/수식$$, " \
           "$$수식$$LEFT ( 0, ``{y2} RIGHT )$$/수식$${j1} 지난다. " \
           "이때 $$수식$$a over b$$/수식$$의 값을 구하시오. (단, $$수식$$a &gt; 0$$/수식$$)\n"
    answer = "(답): $$수식$${an}$$수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y = {a}x^2`$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, " \
              "$$수식$$y$$/수식$$축의 방향으로 $$수식$${yb}$$/수식$$만큼 평행이동한 그래프를 나타내는 이차함수의 식은\n"\
              "$$수식$$y`=`{a}(x`-`a)  ^2 `{op0}{yb}$$/수식$$\n"\
              "이 함수의 그래프가 점 $$수식$$LEFT ( 0, ``{y2} RIGHT)$$/수식$${j1} 지나므로\n"\
              "$$수식$${y2}`=`{a}(0`-`a) ^2 `{op0}{yb}`$$/수식$$, $$수식$${a}`a^2`=`{t0}$$/수식$$, $$수식$$a^2`=`{t1}$$/수식$$\n"\
              "$$수식$$THEREFORE~a`=`{xa}$$/수식$$ $$수식$$LEFT ( BECAUSE~a>0 RIGHT )$$/수식$$\n"\
              "따라서 구하는 이차함수의 식은 $$수식$$y`=`{a}(x`-`{xa}) ^2 `{op0}{yb}`$$/수식$$이고 " \
              "이 그래프가 점 $$수식$$LEFT ( {x1}, ``b RIGHT)$$/수식$$를 지나므로\n"\
              "$$수식$$b`=`{a}({x1}`-`{xa}) ^2 `{op0}{yb}`=`{t2}$$/수식$$\n"\
              "$$수식$$THEREFORE~ b over a `=`{an}$$/수식$$\n\n"

    a = np.random.randint(2, 6)

    xa = np.random.randint(1, 6)

    x1 = np.random.randint(-5, 6)
    while x1 == 0 :
        x1 = np.random.randint(-5, 6)
    y1 = xa * [-3, -1, -2, 1, 2, 3][np.random.randint(0, 6)]
    yb = -1* a*(x1 - xa)**2 + y1

    while yb == 0 :
        y1 = xa * [-1, -2, 1, 2][np.random.randint(0, 4)]
        yb = -1 * a * (x1 - xa) ** 2 + y1

    y2 = a * (0 - xa)**2 + yb

    if yb > 0 :
        op0 = '+'
    else :
        op0 = ''
    t0 = y2 - yb
    t1 = int(t0/a)
    t2 = a * (x1-xa)**2+ yb
    j1 = proc_jo(y2, 4)

    an = int(y1 / xa)
    stem = stem.format(a = a, yb = yb, x1 = x1, y2 = y2, j1 = j1)
    answer = answer.format(an = an)
    comment = comment.format(a = a, op0 = op0, yb = yb, y2 = y2, j1 = j1, t0 = t0, t1 = t1, t2 = t2, xa = xa, x1 = x1, an = an )
    return stem, answer, comment


def quadequation313_Stem_110():
    stem = "이차함수 $$수식$$y=a(x-{p}) ^2 + {q}$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$$b$$/수식$$만큼, " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$$c$$/수식$$만큼 평행이동하면 " \
           "꼭짓점의 좌표가 $$수식$$LEFT ( {x0}, `` {y0} RIGHT )$$/수식$$이고, " \
           "점 $$수식$$LEFT ( {x1}, `` {y1} RIGHT ) $$/수식$${j1} 지난다. " \
           "이때 $$수식$$ a `+` b `+` c`$$/수식$$의 값을 구하시오. (단, $$수식$$a$$/수식$$는 상수이다.)\n"
    answer = "(답): $$수식$${an}$$수식$$\n"
    comment = "(해설)\n" \
              "평행이동한 그래프의 꼭짓점의 좌표가 $$수식$$LEFT ( {x0}, `` {y0} RIGHT )$$/수식$$이므로 " \
              "평행이동한 이차함수의 식을 $$수식$$y = a(x-{x0}) ^2 + {y0}$$/수식$$로 놓을 수 있다.\n"\
              "$$수식$$y = a(x-{x0}) ^2 + {y0}$$/수식$$의 그래프가 점 $$수식$$LEFT ( {x1}, `` {y1} RIGHT ) $$/수식$${j1} 지나므로\n"\
              "$$수식$${y1} = a({t0}) ^2 + {y0} ````````````THEREFORE~a={a}$$/수식$$\n"\
              "즉 $$수식$$y=(x-b-{p})^2 +{q}+c$$/수식$$와 $$수식$$y=(x-{x0}) ^2 +{y0}$$/수식$$의 그래프가 일치하므로\n"\
              "$$수식$$-b-{p}=-{x0}$$/수식$$, $$수식$${q}+c={y0}$$/수식$$\n"\
              "$$수식$$THEREFORE~b={b}, c = {c}$$/수식$$\n"\
              "$$수식$$THEREFORE~a+b+c={an}$$/수식$$\n\n"

    a = np.random.randint(-3, 4)
    while a == 0 :
        a = np.random.randint(-3, 4)
    p = np.random.randint(1, 6)
    q = np.random.randint(1, 6)
    x0 = np.random.randint(1, 6)
    while (a == 0) and (x0-p) == 0 :
        x0 = np.random.randint(1, 6)
    y0 = np.random.randint(1, 6)
    while (a == 0 or x0-p == 0) and y0-q == 0 :
        y0 = np.random.randint(1, 6)
    x1 = np.random.randint(1, 6)
    while x1 == x0 :
        x1 = np.random.randint(1, 6)
    t0 = (x1 - x0)
    y1 = a * t0**2 + y0
    b = x0 - p
    c = y0 -q
    an = a + b + c
    j1 = proc_jo(y1, 4)

    stem = stem.format(p = p, q = q, x0 = x0, y0 = y0, x1 = x1, y1 = y1, j1 = j1)
    answer = answer.format(an = an)
    comment = comment.format(x0 = x0, y0 = y0, x1 = x1, y1 = y1, j1 = j1, t0 = t0, a = a, b = b, c = c, p = p, q = q, an = an)
    return stem, answer, comment


def quadequation313_Stem_111():
    stem = "이차함수 $$수식$$y=a LEFT ( x`-`p RIGHT )^2` +`q$$/수식$$의 그래프의 꼭짓점의 좌표가 $$수식$$ LEFT ( {x0}, `` {y0} RIGHT )$$/수식$$이고, " \
           "점 $$수식$$LEFT ( {x1}, ``{y1} RIGHT )$$/수식$${j1} 지난다. " \
           "이때 $$수식$$a`+`p`+`q$$/수식$$의 값을 구하시오. (단, $$수식$$a$$/수식$$, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$는 상수이다.)\n"
    answer = "(답): $$수식$${an}$$수식$$\n"
    comment = "(해설)\n" \
              "꼭짓점의 좌표가 $$수식$$ LEFT ( {x0}, `` {y0} RIGHT )$$/수식$$이므로 $$수식$$p `=` {x0}$$/수식$$, $$수식$$q `=` {y0}$$/수식$$\n"\
              "즉, $$수식$$y=a LEFT ( x`-`{x0} RIGHT ) ^2 `+`{y0}`$$/수식$$의 그래프가 점 $$수식$$LEFT ( {x1}, `` {y1} RIGHT ) $$/수식$${j1} 지나므로\n"\
              "$$수식$${y1}`=`a({x1}`-`{x0})^2`+`{y0}$$/수식$$, $$수식$${t0}`=`{t1_}a ````````````THEREFORE~a`=`{a}$$/수식$$\n"\
              "$$수식$$THEREFORE~a`+`p`+`q`=`{an}$$/수식$$\n\n"

    a = np.random.randint(-5, 6)
    while a == 0 or a == 1 or a == -1:
        a = np.random.randint(-5, 6)
    x0 = np.random.randint(1, 6)
    y0 = np.random.randint(1, 6)
    x1 = np.random.randint(-5, 6)
    while x1 == x0 :
        x1 = np.random.randint(-5, 6)
    y1 = a * (x1 - x0)**2 + y0
    t0 = y1 - y0
    t1 = (x1 - x0)**2
    if t1 == 1:
        t1_ = ""
    else :
        t1_ = t1
    j1 = proc_jo(y1, 4)
    an = a + x0 + y0

    stem = stem.format(x0 = x0, y0 = y0, x1 = x1, y1 = y1, j1 = j1)
    answer = answer.format(an = an)
    comment = comment.format(x0 = x0, y0 = y0, x1 = x1, y1 = y1, j1 = j1, t0 = t0, t1 = t1, t1_ = t1_, an = an, a = a)
    return stem, answer, comment


def quadequation313_Stem_112():
    stem = "꼭짓점의 좌표가 $$수식$$LEFT ( {x0}, `` {y0} RIGHT )$$/수식$$이고 점 $$수식$$LEFT ( {x1}, `` {y1} RIGHT )$$/수식$${j1} 지나는 포물선이 " \
           "$$수식$$y$$/수식$$축과 만나는 점의 $$수식$$y$$/수식$$좌표는? \n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "꼭짓점의 좌표가 $$수식$$ LEFT ( {x0}, `` {y0} RIGHT )$$/수식$$이므로 " \
              "이차함수의 식을 $$수식$$y`=`a(x`{op0}`{x0_})^2`{op1}{y0}`$$/수식$$으로 놓을 수 있다.\n"\
              "이 함수의 그래프가 점 $$수식$$LEFT ( {x1}, `` {y1} RIGHT )$$/수식$${j1} 지나므로 \n"\
              "$$수식$${y1}`=`a({x1}`{op0}`{x0_})^2`{op1}{y0}`$$/수식$$, $$수식$${t0}`=`{t1}a ````````````THEREFORE~a`=` 1 over {a_}$$/수식$$\n"\
              "$$수식$$THEREFORE~y`=` 1 over {a_} (x`{op0}`{x0_})^2`{op1}{y0}$$/수식$$\n"\
              "따라서 $$수식$$y$$/수식$$축과 만나는 점의 좌표는 $$수식$$x `=` 0$$/수식$$일 때이므로\n"\
              "$$수식$$y`=` 1 over {a_} (0`{op0}`{x0_}) ^2 `{op1}{y0}`=`{an}$$/수식$$\n\n"

    a_ = np.random.randint(2, 6)
    x0 = a_*np.random.randint(1, 3)
    y0 = np.random.randint(-5, 6)
    while y0 == 0 or (1/a_*x0**2+y0 == 0):
        y0 = np.random.randint(-5, 6)
    x1 = a_ * np.random.randint(1, 3) + x0
    while x1 == x0 or x1 == 0 :
        x1 = np.random.randint(-5, 6)
    y1 = int((1/a_) * (x1 - x0)**2 + y0)

    if x0 > 0 :
        op0 = '-'
        x0_ = x0
    else :
        op0 = '+'
        x0_ = -x0

    if y0 > 0 :
        op1 = '+'
    else :
        op1 = ''

    t0 = y1 - y0
    t1 = (x1 - x0)**2

    an = int((1/a_)*(x0**2) + y0)

    candidates = [an, -an, an*2, -an*2, 0]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break

    j1 = proc_jo(y1, 4)

    stem = stem.format(x0 = x0, y0 = y0, x1 = x1, y1 = y1, j1 = j1, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(x0_ = x0_, x0 = x0, y0 = y0, x1 = x1, y1 = y1, j1 = j1, t0 = t0, t1 = t1, an = an, op0 = op0, op1 = op1, a_ = a_)
    return stem, answer, comment


def quadequation313_Stem_113():
    stem = "직선 $$수식$$x`=`{p}$$/수식$${j0} 축으로 하고 두 점 $$수식$$LEFT ( {x0}, ``{y0} RIGHT )$$/수식$${j1} $$수식$$LEFT ( {x1}, `` {y1} RIGHT ) $$/수식$${j2} " \
           "지나는 포물선을 그래프로 하는 이차함수의 식을 $$수식$$y=a LEFT ( x`-`p RIGHT )^2`$$/수식$$라 할 때, $$수식$$a `+` p `-` q`$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "축의 방정식이 $$수식$$x`=`{p}$$/수식$$이므로 $$수식$$p `=` {p}$$/수식$$\n"\
              "즉, $$수식$$y=a LEFT ( x`-`{p} RIGHT ) ^2 `+`q`$$/수식$$의 그래프가 두 점 $$수식$$LEFT ( {x0}, ``{y0} RIGHT )$$/수식$$, " \
              "$$수식$$LEFT ( {x1}, `` {y1} RIGHT )$$/수식$${j2} 지나므로\n"\
              "$$수식$${y0}`=`{t0}a`+`q`$$/수식$$, $$수식$${y1} `=` {t1}a`+`q`$$/수식$$\n"\
              "위의 두 식을 연립하여 풀면 $$수식$$a`=`{a}$$/수식$$, $$수식$$q `=` {q}$$/수식$$\n"\
              "$$수식$$THEREFORE~ a`+`p`-q``=`{a}`+`{p}`-({q})`=`{an}$$/수식$$\n\n"

    a = np.random.randint(1, 5)
    p = np.random.randint(1, 6)
    q = -1 * np.random.randint(1, 6)

    x0 = np.random.randint(-3, 4)
    while x0 == p :
        x0 = np.random.randint(-3, 4)
    x1 = np.random.randint(-3, 4)
    while x1 == x0 or x1 == p :
        x1 = np.random.randint(-3, 4)

    t0 = (x0 - p)**2
    t1 = (x1 - p)**2
    y0 = a * t0 + q
    y1 = a * t1 + q

    an = a + p - q

    j0 = proc_jo(p, 4)
    j1 = proc_jo(y0, 2)
    j2 = proc_jo(y1, 4)

    candidates = [an, -an, an*2, -an*2, an + 3]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break

    stem = stem.format(p = p, x0 = x0, y0 = y0, x1 = x1, y1 = y1, j1 = j1, j2 = j2, j0 = j0, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(a = a, p = p, q = q, x0 = x0, y0 = y0, x1 = x1, y1 = y1, t0 = t0, t1 = t1, an = an, j2 = j2)
    return stem, answer, comment


def quadequation313_Stem_114():
    stem = "이차함수 $$수식$$y={a} LEFT ( x`+`{p} RIGHT ) ^2 `{q}`$$/수식$$의 그래프를 " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼 평행이동하면 " \
           "점 $$수식$$LEFT ( {x0}, `` {y0} RIGHT )$$/수식$${j1} 지나고, " \
           "$$수식$$x$$/수식$$축의 방향으로 $$수식$$b$$/수식$$만큼 평행이동하면 " \
           "점 $$수식$$LEFT ( {x1}, `` {y1} RIGHT )$$/수식$${j2} 지난다. 이때 $$수식$$a`+`b`$$/수식$$의 값은? \n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y={a} LEFT ( x`+`{p} RIGHT ) ^2 `{q}` +`a$$/수식$$의 그래프가 점 $$수식$$LEFT ( {x0}, `` {y0} RIGHT )$$/수식$${j1} 지나므로 \n"\
              "$$수식$${y0}`=`{a}({x0}+{p})^2`{q}+a$$/수식$$\n"\
              "$$수식$$THEREFORE~a`=`{ya}$$/수식$$\n"\
              "$$수식$$y={a} LEFT ( x`-`b`+`{p} RIGHT ) ^2 `{q}`$$/수식$$의 그래프가 점 $$수식$$LEFT ({x1}, ``{y1} RIGHT )$$/수식$${j2} 지나므로 \n"\
              "$$수식$${y1}`=`{a}({x1}-b+{p}) ^2 `{q}$$/수식$$\n"\
              "$$수식$$(b`+`{t0}) ^2 `=` {k}$$/수식$$, $$수식$$b`+`{t0} `=` +- {k_}$$/수식$$\n"\
              "$$수식$$THEREFORE~b`=`{xb}` ````LEFT ( BECAUSE~b &lt; 0 RIGHT )$$/수식$$\n"\
              "$$수식$$ THEREFORE~a`+`b`=`{an}$$/수식$$\n\n"

    a = np.random.randint(-3, 4)
    while a == 0 or a == -1 or a == 1:
        a = np.random.randint(-3, 4)
    p = np.random.randint(1, 4)
    q = -1 * np.random.randint(1, 4)

    k_ = np.random.randint(2, 6)
    k = k_**2

    y1 = k*a + q
    x1 = np.random.randint(-4, 0)
    while x1 + p >= 0 :
        x1 = np.random.randint(-4, 0)

    xb = (x1+ p - k_)
    while -xb + p == 0 or x1 + p >= 0 or k_ < x1 + xb:
        x1 = np.random.randint(-4, 0)
        xb = (x1 + p - k_)
        p = np.random.randint(1, 4)

    ###
    x0 = np.random.randint(-3, 4)
    while x0 == x1 or x0 == -p :
        x0 = np.random.randint(-3, 4)

    ya = np.random.randint(-20, 21)
    while ya == 0 :
        ya = np.random.randint(-20, 21)
    y0 = a *(x0 + p)**2 +q + ya


    t0 = -1 * (x1 + p)
    t1 = int((y1-q)/a)

    an = ya + xb

    if an == 0 :
        candidates = [[an, an+2, an-2, an+4, an-4],[an, an+1, an-1, an+2, an-2]][np.random.randint(0, 3)]
    else :
        candidates = [[an, -an, an*2, -an*2, an*3], [an, an+2, an-2, an+4, an-4], [an, an+1, an-1, an+2, an-2]][np.random.randint(0, 3)]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break

    j1 = proc_jo(y0, 4)
    j2 = proc_jo(y1, 4)
    stem = stem.format(a = a, p = p, q = q, x0 = x0, y0 = y0, x1 = x1, y1 = y1, j1 = j1, j2 = j2, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(a = a, p = p, q = q, x0 =x0, y0 = y0, x1 = x1, y1 = y1, ya = ya, xb = xb, t0 = t0, t1 = t1, k = k, k_ = k_, j1 = j1, j2 = j2, an = an)
    return stem, answer, comment


def quadequation313_Stem_115():
    stem = "이차함수 $$수식$$y=a LEFT ( x`-`p RIGHT )^2`+`q$$/수식$$의 그래프가 $$수식$$x$$/수식$$축과 두 점 $$수식$$LEFT ( {x0}, ``0 RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x1}, `` 0 RIGHT )$$/수식$$에서 만나고, " \
           "꼭짓점이 직선  $$수식$$y `=` {q}`$$/수식$$위에 있을 때, $$수식$$a`p`q`$$/수식$$의 값은? (단, $$수식$$a$$/수식$$, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$는 상수이다.)\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "이차함수 $$수식$$y=a LEFT ( x`-`p RIGHT )^2`+`q$$/수식$$의 그래프가 $$수식$$x$$/수식$$축과 두 점 , $$수식$$LEFT ( {x0}, ``0 RIGHT )$$/수식$$, " \
              "$$수식$$LEFT ( {x1}, `` 0 RIGHT )$$/수식$$에서 만나므로 꼭짓점의 $$수식$$x$$/수식$$좌표는 \n"\
              "$$수식$$ {lg}{x0}`+`{x1}{rg} over 2 `=` {p} ````````````THEREFORE~p`=`{p}$$/수식$$\n"\
              "또 꼭짓점이 직선 $$수식$$y`=`{q}$$/수식$$위에 있으므로 꼭짓점의 $$수식$$y$$/수식$$좌표는 $$수식$${q}$$/수식$$이다.\n"\
              "$$수식$$THEREFORE~q`=`{q}$$/수식$$\n"\
              "따라서 꼭짓점의 좌표가 $$수식$$ LEFT ( {p}, ``{q} RIGHT )$$/수식$$인 이차함수의 식은\n"\
              "$$수식$$y=a LEFT ( x`-`{p} RIGHT ) ^2 {q}$$/수식$$\n"\
              "이 이차함수의 그래프가 점 $$수식$$LEFT ( {x1}, `` 0 RIGHT )$$/수식$$을 지나므로\n"\
              "$$수식$${t0}a{q} `=` 0 ````````````THEREFORE~a`=` {a2} over {a1}$$/수식$$\n"\
              "$$수식$$THEREFORE~a`p`q`=` {a2} over {a1} TIMES {p} TIMES {q} `=`{an}$$/수식$$\n\n"

    a1_ = np.random.randint(2, 6)
    a2_ = a1_ - 1

    p = np.random.randint(1, 6)
    k = np.random.randint(1, 4)
    x0 = p - k
    x1 = p + k
    q = int(-1 * (a2_ / a1_) * (x1 - p) ** 2)
    while ((x1-p)**2) % a1_ != 0 or q % a1_ != 0 :
        a1_ = np.random.randint(2, 6)
        a2_ = a1_ - 1
        p = np.random.randint(1, 6)
        k = np.random.randint(1, 4)
        x0 = p - k
        x1 = p + k
        q = int(-1 * (a2_ / a1_) * (x1 - p) ** 2)

    t0 = (x1 - p)**2
    an = int((a2_/a1_) * p * q)

    if an == 0:
        candidates = [[an, an + 2, an - 2, an + 4, an - 4], [an, an + 1, an - 1, an + 2, an - 2]][np.random.randint(0, 3)]
    else:
        candidates = [[an, -an, an * 2, -an * 2, an * 3], [an, an + 2, an - 2, an + 4, an - 4],[an, an + 1, an - 1, an + 2, an - 2]][np.random.randint(0, 3)]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break
    lg = "{"
    rg = "}"
    stem = stem.format(x0 = x0, x1 = x1, q = q, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(lg = lg, rg = rg, a1 = a1_, a2 = a2_, an = an, x0 = x0, x1 = x1, p = p, q = q, t0 = t0)
    return stem, answer, comment


def quadequation313_Stem_116():
    stem = "이차함수 $$수식$$y= {k} LEFT ( x`+a+{l} RIGHT ) ^2 `{op0}`{m}a`{op0}`{n}`$$/수식$$의 그래프의 축이 " \
           "$$수식$$y$$/수식$$축의 {lr}쪽에 위치할 때, 이 그래프의 꼭짓점이 있는 사분면을 구하시오.\n"\
           "(단, $$수식$$a$$/수식$$는 상수이다.)\n" \
           "제 $$수식$${box}$$/수식$$사분면\n"
    answer = "(답): $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "주어진 이차함수의 그래프의 축의 방정식은\n"\
              "$$수식$$x`=`-a-{l}$$/수식$$\n" \
              "축이 $$수식$$y$$/수식$$축의 {lr}쪽에 위치하므로\n"\
              "$$수식$$-a-{l}`{ch0}`0 ```````````THEREFORE~a{ch1}`-{l}$$/수식$$\n"\
              "주어진 이차함수의 그래프의 꼭짓점의 좌표는\n"\
              "$$수식$$LEFT ( -a-{l}, ``{op0_}`{m}a`{op0}`{n} RIGHT )$$/수식$$\n"\
              "$$수식$$a `{ch1}` - {l}$$/수식$$이므로 $$수식$${m}a `{ch2}`{op1}{n_}$$/수식$$\n"\
              "$$수식$$THEREFORE~{m}a`{op0}{n}`{ch2}`0$$/수식$$\n"\
              "따라서 꼭짓점 $$수식$$LEFT ( -a-{l}, ``{op0_}`{m}a`{op0}`{n} RIGHT )$$/수식$${j1} 제$$수식$${an}$$/수식$$사분면에 있다.\n\n"

    lr = ['오른', '왼'][np.random.randint(0, 2)]
    k = [-5, -4, -3, -2, 2, 3, 4, 5][np.random.randint(0, 8)]
    if lr == '오른' :
        an = [1, 4][np.random.randint(0, 2)]
        ch0 = '&gt;'
        ch1 = '&lt;'
    else :
        an = [2, 3][np.random.randint(0, 2)]
        ch0 = '&lt;'
        ch1 = '&gt;'
    l = np.random.randint(1, 6)

    if lr == '오른' and an == 1 :
        m = np.random.randint(-5, -1)
        op0 = ''
        op1 = ''
        op0_ = op0
        if ch1 == '&lt;':
            ch2 = '&gt;'
        else:
            ch2 = '&lt;'
    elif lr == '오른' and an == 4 :
        m = np.random.randint(2, 6)
        op0 = '+'
        op0_ = ''
        op1 = '-'
        ch2 = ch1
    elif lr == '왼' and an == 2 :
        m = np.random.randint(2, 6)
        op0 = '+'
        op1 = '-'
        op0_ = ''
        ch2 = ch1
    elif lr == '왼' and an == 3 :
        m = np.random.randint(-5, -1)
        op0 = ''
        op1 = ''
        op0_ = op0
        if ch1 == '&lt;':
            ch2 = '&gt;'
        else:
            ch2 = '&lt;'
    n = l * m
    n_ = abs(n)
    j1 = proc_jo(n, -1)

    box = "BOX{````①````}"

    stem = stem.format(k = k, l = l, m =  m, n = n, op0 = op0, lr = lr, box = box)
    answer = answer.format(an = an)
    comment = comment.format(op0_ = op0_, l = l, m = m, n = n, op0 = op0, op1 = op1, lr = lr, ch0 = ch0, ch1 = ch1, ch2 = ch2, n_ = n_, an = an, j1 = j1)
    return stem, answer, comment

def quadequation313_Stem_117():
    stem = "다음 중 이차함수 $$수식$$y=k LEFT ( x`{op0}`{p} RIGHT ) ^2 `{op1}{q}`$$/수식$$의 그래프가 모든 사분면을 지나도록 하는 " \
           "상수 $$수식$$k$$/수식$$의 값이 될 수 있는 것은?\n"\
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "꼭짓점의 좌표가 $$수식$$LEFT ( {op0_}{p}, ``{op1__}{q} RIGHT )$$/수식$$이므로 꼭짓점은 제$$수식$${n}$$/수식$$사분면의 점이다. " \
              "이때 그래프가 모든 사분면을 지나려면 {ud}로 볼록해야 하므로 \n"\
              "$$수식$$k `{ch0}` 0 ````````````CDOTS CDOTS㉠$$/수식$$\n"\
              "또 $$수식$$y$$/수식$$축과의 교점이 $$수식$$x$$/수식$$축의 {ud}쪽에 위치해야 하므로 \n"\
              "$$수식$$k`TIMES ({p})^2`{op1}{q}`{ch1}`0 ````````````THEREFORE~k `{ch1}`{op1_}{lg}{q}over {p2}{rg}```````````CDOTS CDOTS㉡$$/수식$$\n"\
              "㉠, ㉡에서 상수 $$수식$$k$$/수식$$의 값이 될 수 있는 것은 {anum}이다.\n\n"

    n = np.random.randint(1, 5) # 사분면
    p = np.random.randint(3, 6)
    p2 = p**2

    q = np.random.randint(2, p2-4)
    while gcd(p2, q) != 1 :
        p = np.random.randint(3, 6)
        p2 = p ** 2
        q = np.random.randint(2, p2 - 5)

    if n == 1 :
        op0 = '-'
        op1 = '+'
        op0_ = ''
        op1_ = '-'
        op1__ = ''
        ud = '위'
        ch0 = '&lt;'
        ch1 = '&gt;'
    elif n == 2 :
        op0 = '+'
        op1 = '+'
        op0_ = '-'
        op1_ = '-'
        op1__ = ''
        ud = '위'
        ch0 = '&lt;'
        ch1 = '&gt;'
    elif n == 3 :
        op0 = '+'
        op1 = '-'
        op0_ = '-'
        op1_ = ''
        op1__ = '-'
        ud = '아래'
        ch0 = '&gt;'
        ch1 = '&lt;'
    else :
        op0 = '-'
        op1 = '-'
        op0_ = ''
        op1_ = ''
        op1__ = '-'
        ud = '아래'
        ch0 = '&gt;'
        ch1 = '&lt;'

    lg = '{'
    rg = '}'

    if n == 1 or n == 2 :
        if p % 2 == 0 :
            q_ = q - 2
            q__ = q + 4
        else :
            q_ = q - 1
            q__ = q + 2
        if q_ < 0 :
            q_1 = q_ * -1
        else :
            q_1 = q_

        candidates = [f'-{lg}{q} over {p2}{rg}', f'-{lg} {q_1} over {p2}{rg}', f'{q_} over {p2}', f'{q} over {p2}', f'{q__} over {p2}']
    else :
        if p%2 == 0 :
            q_ = q - 2
            q__ = q - 4
            if q_ == 0 :
                q_ = q - 4
                q__ = q - 6
            elif q__ == 0 :
                q__ = q- 6
        else :
            q_ = q - 1
            q__ = q - 2
            if q_ == 0 :
                q_ = q - 3
                q__ = q - 5
            elif q__ == 0 :
                q__ = q- 5
        if q_ == 1 :
            q__ = q - 5
        if q_ < 0 :
            q_1 = q_ * -1
        else :
            q_1 = q_
        if q__ < 0 :
            q__1 = q__ * -1
        else :
            q__1 = q__

        candidates = [f'{q} over {p2}', f' {q_} over {p2}', f'-{lg}{q_1} over {p2}{rg}', f'-{lg}{q} over {p2}{rg}', f'-{lg}{q__1} over {p2}{rg}']

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if n == 1 or n == 2 :
            if sdx == f'-{lg} {q_1} over {p2}{rg}':
                correct_idx = idx
                break
        else :
            if sdx == f' {q_} over {p2}':
                correct_idx = idx
                break
    stem = stem.format(op0 = op0, op1 = op1, p = p, q = q, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(anum = answer_dict[correct_idx], lg = lg, rg = rg, op0 = op0, op1 = op1, op0_ = op0_, op1_ = op1_, op1__ = op1__, n = n, ud = ud, ch0 = ch0, ch1 = ch1, p2 = p2, q = q, p = p)
    return stem, answer, comment


def quadequation313_Stem_118():
    stem = "다음 중 아래 조건을 모두 만족시키는 포물선을 그래프로 하는 이차함수의 식은?\n" \
           "$$표$$ " \
           "(가) 이차함수 $$수식$$y `=` {op0} {k} x^2 $$/수식$$의 그래프와 폭이 같다.\n"\
           "(나) 꼭짓점은 제$$수식$${n}$$/수식$$사분면에 있다.\n"\
           "(다) {ud}로 볼록하다. $$/표$$\n"\
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y=a LEFT ( x`-`p RIGHT )^2`+`q$$/수식$$로 놓으면 조건 (가), (다)에 의하여 $$수식$$a `=` {op1} {k}$$/수식$$\n"\
              "조건 (나)에 의하여 $$수식$$p `{ch0}` 0$$/수식$$, $$수식$$q `{ch1}` 0 $$/수식$$\n"\
              "따라서 주어진 조건을 모두 만족시키는 이차함수의 식은 {anum}이다.\n\n"

    op0 = ['-', ''][np.random.randint(0, 2)]
    k = np.random.randint(1, 6)
    n = np.random.randint(1, 5) # 사분면
    ud = ['위', '아래'][np.random.randint(0, 2)]
    if ud == '위' :
        op1 = '-'
    else :
        op1 = ''

    p = np.random.randint(1, 10)
    q = np.random.randint(1, 10)
    p_ = np.random.randint(1, 10)
    while p == p_ :
        p = np.random.randint(1, 10)
    q_ = np.random.randint(1, 10)
    while q == q_ :
        q_ = np.random.randint(1, 10)

    if n == 1 :
        op2 = '-'
        op3 = '+'
        ch0 = '&gt;'
        ch1 = '&gt;'
    elif n == 2 :
        op2 = '+'
        op3 = '-'
        ch0 = '&lt;'
        ch1 = '&gt;'
    elif n == 3 :
        op2 = '+'
        op3 = '-'
        ch0 = '&lt;'
        ch1 = '&lt;'
    else :
        op2 = '-'
        op3 = '-'
        ch0 = '&gt;'
        ch1 = '&lt;'

    if op1 == '' :
        op1_ = '-'
    else :
        op1_ = ''

    if op2 == '+' :
        op2_ = '-'
    else :
        op2_ = '+'

    if op3 == '+' :
        op3_ = '-'
    else :
        op3_ = '+'

    t1 = f'y`=`{op1}{k} ( x `{op2}{p})^2 `{op3}`{q}'
    t2 = f'y`=`{op1}{k} ( x `{op2}{p_})^2 `{op3_}`{q}'
    t3 = f'y`=`{op1}{k} ( x `{op2_}{p})^2 `{op3}`{q_}'
    t4 = f'y`=`{op1_}{k} ( x `{op2}{p_})^2 `{op3}`{q}'
    t5 = f'y`=`{op1_}{k} ( x `{op2_}{p_})^2 `{op3_}`{q_}'
    candidates = [t1, t2, t3, t4, t5]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == t1 :
            correct_idx = idx
            break

    stem = stem.format(op0 = op0, k = k, n = n, ud = ud, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(anum = answer_dict[correct_idx], op1 = op1, ch0 = ch0, ch1 = ch1, k = k)
    return stem, answer, comment


def quadequation313_Stem_119():
    stem = "이차함수 $$수식$$y`=` 1 over {k} x^2`{op0}`{l}x`{op1}`{m}`$$/수식$${j1} "\
           "$$수식$$y=a LEFT ( x`-`p RIGHT )^2` +`q`$$/수식$$의 꼴로 나타낼 때, " \
           "$$수식$${t}a `+` p`+`q`$$/수식$$의 값은? " \
           "(단, $$수식$$a$$/수식$$, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$는 상수이다.)\n"\
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` 1 over {k} x^2`{op0}`{l}x`{op1}`{m}`$$/수식$$\n"\
              "$$수식$$`````=`1 over {k} ( x^2`{op0}`{n}x `+`{o2} `-`{o2} ) `{op1}` {m}$$/수식$$\n"\
              "$$수식$$`````=`1 over {k} (x `{op0}` {p})^2`{op2}`{q}`$$/수식$$\n"\
              "따라서 $$수식$$a`=`1 over {k}$$/수식$$, $$수식$$p`=`{p_}$$/수식$$, $$수식$$q`=`{q}$$/수식$$이므로\n"\
              "$$수식$${t}a `+` p`+`q` `=` {an}$$/수식$$\n\n"

    k = np.random.randint(2, 6)
    t = k * np.random.randint(1, 3)
    l = [-4, -2, 2, 4][np.random.randint(0, 4)]
    m = np.random.randint(-9, 10)
    while m == 0 :
        m = np.random.randint(-9, 10)
    if l > 0 :
        op0 = '+'
    else :
        op0 = ''
    if m > 0 :
        op1 = '+'
    else :
        op1 = ''
    j1 = proc_jo(m, 4)
    n = k * l
    p = o = int(n/2)
    o2 = o**2
    q = int(-1*o2 *(1/k))+ m
    p_ = p*-1
    an = int(t*(1/k)) + p_ + q

    if q > 0 :
        op2 = '+'
    else :
        op2 = ''

    if an == 0 :
        candidates = [an, an+2, an-2, an+4, an-4]
    else :
        candidates = [an, an*2, -an*2, -an, an*3]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an :
            correct_idx = idx
            break

    stem = stem.format(k = k, op0 = op0, op1 = op1, l = l, m= m, j1 = j1, t = t, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(p_ = p_, t = t, an = an, k = k, op0 = op0, op1 = op1, op2 = op2, l = l, m = m, n = n, p = p, q = q, o2 = o2)
    return stem, answer, comment


def quadequation313_Stem_120():
    stem = "이차함수 $$수식$$y=-x ^2 +{p_}x$$/수식$$의 그래프와 이차함수 $$수식$$y=x ^2`-2px`+q`$$/수식$$의 그래프의 꼭짓점이 일치할 때, " \
           "$$수식$$p`+`q$$/수식$$의 값은?\n" \
           "(단, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$는 상수이다.)\n"\
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y=-x ^2 +{p_}x `=`-(x-{p})^2`+{p2}`$$/수식$$의 그래프의 꼭짓점의 좌표는 $$수식$$LEFT ( {p}, ``{p2} RIGHT )$$/수식$$\n"\
              "$$수식$$y=x ^2`-2px`+q``=`(x-p)^2`-p^2`+q`$$/수식$$의 그래프의 꼭짓점의 좌표는 $$수식$$LEFT (p, `` -p^2`+`q RIGHT )$$/수식$$\n"\
              "따라서 $$수식$$p`=`{p}$$/수식$$, $$수식$$-p^2`+q`=`{p2}`$$/수식$$에서 $$수식$$q`=`{q}$$/수식$$\n"\
              "$$수식$$THEREFORE~p`+`q`=`{an}$$/수식$$\n\n"

    p = np.random.randint(1, 6)
    p_ = p * 2
    p2 = p ** 2
    q = 2 * p2
    an = p + q

    candidates = [an-1, an, an+3, an+5, an+7]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an :
            correct_idx = idx
            break

    stem = stem.format(p_ = p_, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(p_ = p_, p = p, p2 = p2, q = q, an = an)
    return stem, answer, comment


def quadequation313_Stem_121():
    stem = "$$수식$$y`=`x^2`{op0}{k}x`{op1}{l}`$$/수식$$의 그래프가 $$수식$$x$$/수식$$축과 만나는 두 점의 $$수식$$x$$/수식$$좌표를 " \
           "각각 $$수식$$p$$/수식$$, $$수식$$q$$/수식$$라 하고, " \
           "$$수식$$y$$/수식$$축과 만나는 점의 $$수식$$y$$/수식$$좌표를 $$수식$$r$$/수식$$라 할 때, $$수식$$p`+`q`+`r`$$/수식$$의 값은?\n"\
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`x^2`{op0}{k}x`{op1}{l}`$$/수식$$에 $$수식$$y `=` 0$$/수식$$을 대입하면\n"\
              "$$수식$$x ^2 `{op0}{k}x`{op1}{l}`=`0$$/수식$$, $$수식$$LEFT (x`{op2}`{x0})(x`{op3}`{x1})`=`0$$/수식$$\n"\
              "$$수식$$THEREFORE~x`=`{p}`$$/수식$$, 또는 $$수식$$x `=` {q}$$/수식$$\n"\
              "$$수식$$y`=`x^2`{op0}{k}x`{op1}{l}`$$/수식$$에 $$수식$$x `=` 0$$/수식$$을 대입하면 $$수식$$y `=` {l}$$/수식$$\n"\
              "따라서 $$수식$$p`=`{p}`$$/수식$$, $$수식$$q`=`{q}`$$/수식$$, $$수식$$r`=`{l}`$$/수식$$ " \
              "또는 $$수식$$p`=`{q}`$$/수식$$, $$수식$$q`=`{p}`$$/수식$$, $$수식$$r`=`{l}`$$/수식$$이므로\n"\
              "$$수식$$p`+`q`+`r`=`{an}$$/수식$$\n\n"

    x0 = np.random.randint(-9, 10)
    while x0 == 0 :
        x0 = np.random.randint(-9, 10)
    x1 = np.random.randint(-9, 10)
    while x1 == 0 or x1 == x0 or x0 + x1 == 1 or x0 + x1 == -1 or x0 + x1 == 0 :
        x1 = np.random.randint(-9, 10)

    k = x0 + x1
    l = x0 * x1
    p = -x0
    q = -x1

    if k > 0 :
        op0 = '+'
    else :
        op0 = ''

    if l > 0 :
        op1 = '+'
    else :
        op1 = ''
    if x0 > 0 :
        op2 = '+'
    else :
        op2 = ''
    if x1 > 0 :
        op3 = '+'
    else :
        op3 = ''

    an = p + q + l

    if an == 0 :
        candidates = [an, an-1, an+1, an,-2, an+2]
    else :
        candidates = [an, an-2, an+1, an-1, an+2]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an :
            correct_idx = idx
            break

    stem = stem.format(k = k, l = l, op0 = op0, op1 = op1, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(x0 = x0, x1 = x1, op0 = op0, op1 = op1, op2 = op2, op3 = op3, k = k, l = l, p = p, q = q, an = an)
    return stem, answer, comment


def quadequation313_Stem_122():
    stem = "이차함수 $$수식$$y`=` {a}x ^2 `+{b}x`+`{c}`$$/수식$${j1} $$수식$$y=a LEFT ( x`-`p RIGHT )^2`+`q$$/수식$$의 꼴로 나타낼 때, " \
           "$$수식$$a`p`q`$$/수식$$의 값을 구하시오. (단, $$수식$$a$$/수식$$, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$는 상수이다.)\n"
    answer = "(답): $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` {a}x ^2 `+{b}x`+`{c}`$$/수식$$\n"\
              "$$수식$$``=` {a} (x ^2 `+`{k}x`+`{l}`-`{l})`+{c}$$/수식$$\n"\
              "$$수식$$``=` {a}(x+{p_}) ^2 `{op0}{q}$$/수식$$\n"\
              "따라서 $$수식$$a`=`{a}$$/수식$$, $$수식$$p`=`{p}$$/수식$$, $$수식$${q}$$/수식$$이므로 \n"\
              "$$수식$$a`p`q`=`{an}$$/수식$$\n\n"

    a = np.random.randint(2, 5)
    b = np.random.randint(a+1, 10)
    if a == 2 :
        while b % 4 != 0 or b % a != 0:
            b = np.random.randint(a + 1, 11)
    elif a == 4 :
        while b % 8 != 0 or b % a != 0:
            b = np.random.randint(a + 1, 10)
    else :
        while b % 2 != 0 or b % a != 0:
            b = np.random.randint(a + 1, 10)
    c = np.random.randint(1, 10)
    k = int(b/a)
    m = int(b/(2*a))**2
    p_ = int(b/(2*a))
    q = -1*m*a+c
    while q == 0 :
        c = np.random.randint(1, 10)
        q = -1 * m * a + c
    if q > 0 :
        op0 = '+'
    else :
        op0 = ''

    p = -p_
    an = a * p * q
    j1 = proc_jo(c, 4)
    stem = stem.format(a = a, b = b, c = c, j1 = j1)
    answer = answer.format(an = an)
    comment = comment.format(a = a, b = b, c = c, k = k, l = m, p_ = p_, p = p, q = q, op0 = op0, an = an )
    return stem, answer, comment


def quadequation313_Stem_123():
    stem = "이차함수 $$수식$$y`=` 1 over {a} x ^2 `-`{b}x`$$/수식$${j1} $$수식$$y`=`1 over {a} LEFT ( x`-`p RIGHT )^2`+`q$$/수식$$의 꼴로 나타낼 때, " \
           "$$수식$$q over p$$/수식$$의 값을 구하시오. (단, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$는 상수이다.)\n"
    answer = "(답): $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` 1 over {a} x ^2 `- {b}x$$/수식$$\n"\
              "$$수식$$``=` 1 over {a} (x ^2 `-`{c}x`+`{d}`-`{d})`$$/수식$$\n"\
              "$$수식$$``=` 1 over {a} (x-{p}) ^2 `{q}$$/수식$$\n"\
              "따라서 $$수식$$p`=`{p}$$/수식$$, $$수식$$q`=`{q}$$/수식$$이므로 \n"\
              "$$수식$$q over p `=`{an}$$/수식$$\n\n"

    a = np.random.randint(2, 6)
    b = np.random.randint(1, 6)
    while (a*b) % 2 != 0 :
        b = np.random.randint(1, 6)
    c = a * b
    d = int(c/2)**2
    p = int(c/2)
    q = -1 * int(d / a)
    while q % p != 0 or q == 0:
        a = np.random.randint(2, 6)
        b = np.random.randint(1, 6)
        while (a * b) % 2 != 0:
            b = np.random.randint(1, 6)
        c = a * b
        d = int(c / 2) ** 2
        p = int(c / 2)
        q = -1 * int(d / a)
    an = int(q / p)
    j1 = proc_jo(b, 4)
    stem = stem.format(a = a, b = b, j1 = j1)
    answer = answer.format(an = an)
    comment = comment.format(a = a, b = b, c = c, d = d, p = p, q = q, an = an )
    return stem, answer, comment


def quadequation313_Stem_124():
    stem = "이차함수 $$수식$$y`=` {a}x ^2 `{op0}`{b_}`x`{op1}`{c}`$$/수식$$의 그래프가 이차함수 " \
           "$$수식$$y`=`{a} LEFT ( x`-`p RIGHT ) ^2 `+` {m} over q$$/수식$$의 그래프와 일치한다고 할 때, " \
           "$$수식$$p`q`$$/수식$$의 값은? (단, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$는 상수이다.)\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` {a}x ^2 `{op0}{b_}`x`{op1}`{c}$$/수식$$\n"\
              "$$수식$$``=` {a} LEFT ( x^2` {op3} {t1} over {t2} x`+ {t3} over {t4}`- {t3} over {t4} RIGHT )`{op1}`{c}$$/수식$$\n"\
              "$$수식$$``=` {a} LEFT ( x {op3} {t1_} over {t2_} RIGHT )^2`{op4}` {m} over {q}$$/수식$$\n"\
              "따라서 $$수식$$p`=` {op5} {t1_} over {t2_}$$/수식$$, $$수식$$q`=`{q_}$$/수식$$이므로 \n"\
              "$$수식$$p`q `=` {op5} {t1_} over {t2_} `TIMES` {q_}  `=` {an}$$/수식$$\n\n"

    a = np.random.randint(-5, 6)
    while a == 0 or a == -1 or a == 1 :
        a = np.random.randint(-5, 6)

    if a == 2 or a == -2 :
        b = 1
        b_ = ''
    else :
        b = np.random.randint(-5, 6)
        while b == 0 or b == 1 or b == -1 or a == b or a == -b:
            b = np.random.randint(-5, 6)
        b_ = b
    c = np.random.randint(-5, 6)
    while c == 0 :
        c = np.random.randint(-5, 6)

    if b > 0 :
        op0 = '+'
    else :
        op0 = ''

    if c > 0 :
        op1 = '+'
    else :
        op1 = ''

    gcd_ab = gcd(abs(a), abs(b))
    t1 = int(b/gcd_ab)
    t2 = int(a/gcd_ab)
    if t1 < 0 and t2 < 0 :
        op3 = '+'
    elif (t1 < 0 and t2 > 0) or (t1 > 0 and t2 < 0) :
        op3 = '-'
    else :
        op3 = '+'
    t1 = abs(t1)
    t2 = abs(t2)

    gcd_2ab = gcd(4*(a**2), b**2)
    t3 = int(b**2 / gcd_2ab)
    t4 = int(4*(a**2) / gcd_2ab)

    gcd_t1_t2_ = gcd(t1, 2*t2)
    t1_ = int(t1 / gcd_t1_t2_)
    t2_ = int(2*t2 / gcd_t1_t2_)

    m = -a * t3 + c * t4
    q = t4
    gcd_mq = gcd(abs(m), q)
    m = int(m/gcd_mq)
    q = int(t4/gcd_mq)

    if m > 0 :
        op4 = '+'
    else :
        op4 = '-'
        m = m * -1

    if op4 == '+':
        q_ = q
    else:
        q_ = -q

    if op3  == '+':
        op5 = '-'
        an = - int(t1_ / t2_ * q_)
    else :
        op5 = ''
        an = int(t1_ / t2_ * q_)

    candidates = [an, -an, an * 2, -an * 2, an* 3]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break

    stem = stem.format(a = a, b_ = b_, c = c, m = m, op0 = op0, op1 = op1, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(a = a, b_ = b_, c = c, m  = m, q = q, q_ = q_, t1 = t1, t2 = t2, t3 = t3, t4 = t4, t1_ =t1_, t2_ = t2_, op0 = op0, op1 = op1, op3 = op3, op4  = op4, op5 = op5, an = an)
    return stem, answer, comment


def quadequation313_Stem_125():
    stem = "이차함수 $$수식$$y`=` {a}x ^2 `+`x`-`{c}`$$/수식$$의 그래프가 이차함수 " \
           "$$수식$$y= {a} LEFT ( x`-`p RIGHT ) ^2 `{op0}` {m} over q$$/수식$$의 그래프와 일치한다고 할 때, " \
           "$$수식$${k}p`+`q`$$/수식$$의 값은? (단, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$는 상수이다.)\n"
    answer = "(답): $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` {a}x ^2 `+``x`-`{c}$$/수식$$\n"\
              "$$수식$$``=` {a} LEFT ( x^2` -` 1 over {t} x`+ 1 over {p2}`- 1 over {p2} RIGHT )`-{c}$$/수식$$\n"\
              "$$수식$$``=` {a} LEFT ( x `-` 1 over {p} RIGHT )^2`{op0} {m} over {q}$$/수식$$\n"\
              "따라서 $$수식$$p`=`1 over {p}$$/수식$$, $$수식$$q`=`{q_}$$/수식$$이므로 \n"\
              "$$수식$${k}p`+`q `=` {k} `TIMES` 1 over {p} `{op1}` {q_}  `=` {an}$$/수식$$\n\n"

    p = np.random.randint(3, 8)
    while p % 2 != 0 :
        p = np.random.randint(3, 8)
    a = -1 * int(p/2)
    t = -1 * a
    p2 = p ** 2
    c = np.random.randint(1, 6)
    q = p2
    m = -1 * a - q*c
    if m > 0 :
        op0 = '+'
    else :
        op0 = '-'
        m = -1*m
    qm_gcd = gcd(q, m)
    q = int(q / qm_gcd)
    m = int(m / qm_gcd)
    if op0 == '+' :
        q_ = -1 * q
        op1 = ''
    else :
        q_ = q
        op1 = '+'
    k = p*[-2, -1, 1, 2][np.random.randint(0, 4)]

    an = int(k * (1/p)) + q_

    stem = stem.format(k = k, a = a, c = c, m = m, op0 = op0)
    answer = answer.format(an = an)
    comment = comment.format(a = a, c =c , t = t, p = p, p2 = p2, op0 = op0, op1 = op1, an = an, q_ = q_, m = m, q = q, k = k)
    return stem, answer, comment


def quadequation313_Stem_126():
    stem = "이차함수 $$수식$$y`= `- 1 over {a} x^2 `+` {b}x `{op0}`{c}`$$/수식$${j1} " \
           "$$수식$$y= `- 1 over {a} LEFT ( x`-`p RIGHT ) ^2 `+` q $$/수식$$꼴로 나타낼 때, " \
           "$$수식$$p`+`q`$$/수식$$의 값은? (단, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$는 상수이다.)\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`= `- 1 over {a} x^2 `+` {b}x `{op0}`{c}`$$/수식$$\n"\
              "$$수식$$``=` - 1 over {a} LEFT ( x^2` -` {p_2} x`+ {p2} `-` {p2} RIGHT )`{op0}`{c}$$/수식$$\n"\
              "$$수식$$``=` - 1 over {a} LEFT ( x `-` {p} RIGHT )^2`{op1} {q}$$/수식$$\n"\
              "따라서 $$수식$$p`=` {p}$$/수식$$, $$수식$$q`=`{q}$$/수식$$이므로 \n"\
              "$$수식$$p`+`q `=` {an}$$/수식$$\n\n"

    p = np.random.randint(2, 10)
    p_2 = p * 2
    p2 = p ** 2
    a = np.random.randint(2, 10)
    while p_2 % a != 0 or p2 % a != 0 :
        a = np.random.randint(2, 10)
    b = int(p_2/a)
    q = np.random.randint(-10, 11)
    while q == 0 :
        q = np.random.randint(-10, 11)
    c = -1 * int(p2/a) + q

    if c > 0 :
        op0 = '+'
    else :
        op0 = ''

    if q > 0 :
        op1 = '+'
    else :
        op1 = ''

    an = p + q

    km_list = [-5, -4, -3, -2, -1]
    kp_list = [ 1, 2, 3, 4, 5]
    t1 = an + km_list.pop(np.random.randint(0, len(km_list)))
    t2 = an + km_list.pop(np.random.randint(0, len(km_list)))
    t3 = an + kp_list.pop(np.random.randint(0, len(kp_list)))
    t4 = an + kp_list.pop(np.random.randint(0, len(kp_list)))
    candidates = [an, t1, t2, t3, t4]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break

    j1 = proc_jo(c, 4)
    stem = stem.format(a = a, b = b, c = c, j1 = j1, op0 = op0, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(a = a, b = b, c = c, p_2 = p_2, p2 = p2, op0 = op0, p = p, q = q, an = an, op1 = op1)
    return stem, answer, comment


def quadequation313_Stem_127():
    stem = "이차함수 $$수식$$y`= `{a} x^2 `-` {b}x `+`{c}`$$/수식$$의 그래프는 이차함수 " \
           "$$수식$$y= {a} x^2$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$$p$$/수식$$만큼, " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$$q$$/수식$$만큼 평행이동한 것이다. 이때 $$수식$$q over p$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` {a} x^2 `-` {b}x `+`{c} `=` {a} LEFT ( x `-` {p} RIGHT ) ^2 `+`{q}$$/수식$$\n"\
              "따라서 $$수식$$y`=`{a}x^2$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$${p}$$/수식$$만큼, " \
              "$$수식$$y$$/수식$$축의 방향으로 $$수식$${q}$$/수식$$만큼 평행이동한 것이므로\n"\
              "$$수식$$p`=`{p}$$/수식$$, $$수식$$q`=`{q}$$/수식$$\n"\
              "$$수식$$THEREFORE~ q over p `=`{an}$$/수식$$\n\n"

    p = np.random.randint(1, 6)
    q = p * np.random.randint(1, 6)
    a = np.random.randint(2, 6)
    b = 2*a*p
    c = a*p**2 + q
    an = int(q/p)

    stem = stem.format(a = a, b = b, c = c)
    answer = answer.format(an = an)
    comment = comment.format(a = a, b = b, c = c, p = p, q = q, an = an)
    return stem, answer, comment


def quadequation313_Stem_128():
    stem = "이차함수 $$수식$$y`= `{a} x^2 `-` {b}x `{op1}`{c}`$$/수식$$의 그래프는 이차함수 " \
           "$$수식$$y= {a} x^2$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$$p$$/수식$$만큼, " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$$q$$/수식$$만큼 평행이동한 것이다. 이때 $$수식$$p`-`q$$/수식$$의 값을 구하시오.\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` {a} x^2 `-` {b}x `{op1}`{c} `=` {a} LEFT ( x `-` {p} RIGHT ) ^2 `{op0}`{q}$$/수식$$\n"\
              "따라서 $$수식$$y`=`{a}x^2$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$${p}$$/수식$$만큼, " \
              "$$수식$$y$$/수식$$축의 방향으로 $$수식$${q}$$/수식$$만큼 평행이동한 것이므로\n"\
              "$$수식$$p`=`{p}$$/수식$$, $$수식$$q`=`{q}$$/수식$$\n"\
              "$$수식$$THEREFORE~ p `-` q `=`{an}$$/수식$$\n\n"
    a = np.random.randint(2, 6)
    p = np.random.randint(1, 6)
    q = np.random.randint(-10, 10)
    while q == 0 :
        q = np.random.randint(-10, 10)

    c = a*p**2 + q
    while c == 0 or q == 0:
        print ("1")
        q = np.random.randint(-10, 10)
        c = a * p ** 2 + q

    if q < 0:
        op0 = ''
    else:
        op0 = '+'

    b = 2*a*p

    an = int(p - q)
    if c > 0 :
        op1 = '+'
    else :
        op1 = ''

    km_list = [-5, -4, -3, -2, -1]
    kp_list = [1, 2, 3, 4, 5]
    t1 = an + km_list.pop(np.random.randint(0, len(km_list)))
    t2 = an + km_list.pop(np.random.randint(0, len(km_list)))
    t3 = an + kp_list.pop(np.random.randint(0, len(kp_list)))
    t4 = an + kp_list.pop(np.random.randint(0, len(kp_list)))
    candidates = [an, t1, t2, t3, t4]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break
    stem = stem.format(op1 = op1, a = a, b = b, c = c, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(op1 = op1, op0 = op0, a = a, b = b, c = c, p = p, q = q, an = an)
    return stem, answer, comment


def quadequation313_Stem_129():
    stem = "이차함수 $$수식$$y`=` -x^2 `+` {b}x`$$/수식$$의 그래프와 $$수식$$y= x^2 `-`2px `+`q`$$/수식$$의 그래프의 꼭짓점이 일치할 때, " \
           "$$수식$$q over p$$/수식$$의 값을 구하시오.\n" \
           "(단, $$수식$$p$$/수식$$, $$수식$$q$$/수식$$는 상수이다.)\n"
    answer = "(답): $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` -x^2 `+` {b}x `=` - LEFT ( x `-` {p} RIGHT )^2 `+ {c}$$/수식$$의 그래프의 꼭짓점의 좌표는 $$수식$$LEFT ( {p}, ``{c} RIGHT )$$/수식$$\n"\
              "$$수식$$y= x^2 `-`2px `+`q` `=` LEFT ( x `-` p RIGHT )^2 `-`p^2 `+` q`$$/수식$$의 그래프의 꼭짓점의 좌표는 $$수식$$LEFT ( p, ``-p^2`+`q RIGHT )$$/수식$$\n"\
              "따라서 $$수식$$p`=`{p}$$/수식$$, $$수식$$-p^2`+`q `=`{c}$$/수식$$이므로 $$수식$$q`=`{q}$$/수식$$\n"\
              "$$수식$$THEREFORE~ q over p `=`{an}$$/수식$$\n\n"

    p = np.random.randint(1, 10)
    c = p**2
    q = 2*c
    an = int(q/p)
    b = 2 * p
    stem = stem.format(b = b)
    answer = answer.format(an = an)
    comment = comment.format(b = b, p = p, c = c, an = an, q = q)
    return stem, answer, comment


def quadequation313_Stem_130():
    stem = "이차함수 $$수식$$y`=` {a}x^2 `-` {t_2}x`$$/수식$$를 $$수식$$y`=` a LEFT ( x `+` b RIGHT )^2 `+` c$$/수식$$ 꼴로 나타낼 때, " \
           "$$수식$$a`b`c`$$/수식$$의 값은? (단, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$는 상수이다.)\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` {a}x^2 `-` {t_2}x$$/수식$$\n"\
              "$$수식$$``=` {a} LEFT ( x^2 `-` {t_2} over {a} x `+` {t2} over {a2_} `-` {t2} over {a2_} RIGHT ) $$/수식$$\n" \
              "$$수식$$``=` {a} LEFT ( x `-` {t} over {a} RIGHT ) ^2 `-` {t2} over {a}$$/수식$$\n" \
              "따라서 $$수식$$a`=`{a}$$/수식$$, $$수식$$b `=` - {b1} over {b2}$$/수식$$, $$수식$$c `=` - {c1} over {c2}$$/수식$$이므로 " \
              "$$수식$$a`b`c` =` {an1} over {an2}$$/수식$$\n\n"

    a = np.random.randint(2, 6)
    t = np.random.randint(1, 6)
    while gcd(a, t) != 1 :
        t = np.random.randint(1, 6)
    t_2 = t * 2
    t2 = t ** 2
    a2_ = a ** 2
    b1 = t
    b2 = a
    c1 = t2
    c2 = a
    an1 = b1 * c1
    an2 = a


    tmp1 = int(an1*2 / gcd(an1*2, an2))
    tmp2 = int(an2 / gcd(an1*2, an2))
    if an2 == 2 :
        tmp1 = int((an1 + 2) / gcd(an1 + 2, an2))
        tmp2 = int(an2 / gcd(an1 + 2, an2))
    s1 = f"$$수식$${an1} over {an2}$$/수식$$"
    s2 = f"$$수식$$- {an1} over {an2}$$/수식$$"
    s3 = f"$$수식$${tmp1} over {tmp2}$$/수식$$"
    s4 = f"$$수식$$- {tmp1} over {tmp2}$$/수식$$"

    tmp3 = int(an1 * 3 / gcd(an1 * 3, an2))
    tmp4 = int(an2 / gcd(an1 * 3, an2))
    while (tmp3 == tmp1 and tmp4 == tmp2) or (tmp3 == an1 and tmp4 == an2) :
        tmp3 = int(an1 * 5 / gcd(an1 * 5, an2))
        tmp4 = int(an2 / gcd(an1 * 5, an2))
    if an2 == 3 :
        tmp3 = int(an1 * 4 / gcd(an1 * 4, an2))
        tmp4 = int(an2 / gcd(an1 * 4, an2))
    while (tmp3 == tmp1 and tmp4 == tmp2) or (tmp3 == an1 and tmp4 == an2) :
        tmp3 = int(an1 * 6 / gcd(an1 * 6, an2))
        tmp4 = int(an2 / gcd(an1 * 6, an2))

    s5 = f"$$수식$${tmp3} over {tmp4}$$/수식$$"

    candidates = [s1, s2, s3, s4, s5]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == s1:
            correct_idx = idx

    stem = stem.format(a = a, t_2 = t_2, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(a = a, t_2 = t_2, t = t, t2 = t2, a2_ = a2_, b1 = b1, b2 = b2, c1 = c1, c2 = c2, an1 = an1, an2 = an2)
    return stem, answer, comment


def quadequation313_Stem_131():
    stem = "이차함수 $$수식$$y`=` x^2 `+` ax `{op0}` {k}$$/수식$$의 그래프가 점 $$수식$$LEFT ( {x0}, `` {y0} RIGHT )$$/수식$${j1} 지날 때, " \
           "이 꼭짓점의 좌표는?\n" \
           "(단, $$수식$$a$$/수식$$는 상수이다.)\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` x^2 `+` ax `{op0}` {k}$$/수식$$의 그래프가 점 $$수식$$ LEFT ( {x0}, `` {y0} RIGHT )$$/수식$${j1} 지나므로\n"\
              "$$수식$${y0} `=` {x_2} `{op2}` {x0}a `{op0}` {k}`````````````THEREFORE~a`=`{a}$$/수식$$\n"\
              "$$수식$$THEREFORE~y`=`x^2 {a}x`{op0}`{k}`=` LEFT ( x^2`{a}`x`+`{n}`-`{n})`{op0}`{k}$$/수식$$\n" \
              "$$수식$$`````=` LEFT ( x `-` {p} RIGHT ) ^2 {op1} {q} $$/수식$$\n"\
              "따라서 꼭짓점의 좌표는 $$수식$$LEFT ( {p}, ``{q} RIGHT )$$/수식$$이다.\n\n"

    p = np.random.randint(1, 10)
    q = np.random.randint(-10, 11)
    while q == 0 or p == q or p == -q:
        q = np.random.randint(-10, 11)
    if q > 0 :
        op1 = '+'
    else :
        op1 = ''
    a = -2*p
    k = p**2 + q
    n = (int(a/2))**2
    x0 = np.random.randint(-3, 4)
    while x0 == 0 or x0 == -1 or x0 == 1:
        x0 = np.random.randint(-3, 4)
    x2 = x0 **2
    y0 = x2 + x0*a + k
    if k < 0 :
        op0 = ''
    else :
        op0 = '+'
    j1 = proc_jo(y0, 4)
    if x0 < 0 :
        op2 = ''
    else :
        op2 = '+'
    p2 = -p
    q2 = -q
    s1 = f"$$수식$$LEFT ( {p}, ``{q} RIGHT )$$/수식$$"
    s2 = f"$$수식$$LEFT ( {p}, ``{q2} RIGHT )$$/수식$$"
    s3 = f"$$수식$$LEFT ( {p2}, ``{q} RIGHT )$$/수식$$"
    s4 = f"$$수식$$LEFT ( {p2}, ``{q2} RIGHT )$$/수식$$"
    s5 = f"$$수식$$LEFT ( {q}, ``{p} RIGHT )$$/수식$$"


    candidates = [s1, s2, s3, s4, s5]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == s1:
            correct_idx = idx

    stem = stem.format(k = k, x0 = x0, y0 = y0, op0 = op0, j1 = j1, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(op2 = op2, op0 = op0, x0 = x0, y0 = y0, j1 = j1, x2 = x2, op1 = op1, k = k, a = a, n = n, p = p, q = q, x_2 = x2)
    return stem, answer, comment


def quadequation313_Stem_132():
    stem = "$$수식$$y`=` x^2 `{op2}`{a}x`{op3}`{b}$$/수식$$그래프가 $$수식$$x$$/수식$$축과 만나는 두 점의 $$수식$$x$$/수식$$좌표를 " \
           "각각 $$수식$$p$$/수식$$, $$수식$$q$$/수식$$라 하고, " \
           "$$수식$$y$$/수식$$축과 만나는 점의 $$수식$$y$$/수식$$좌표를 $$수식$$r$$/수식$$라 할 때, $$수식$$p`q`r`$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` x^2 `{op2}`{a}x`{op3}`{b}$$/수식$$에 $$수식$$y `=` 0$$/수식$$을 대입하면 \n"\
              "$$수식$$x^2 `{op2}`{a}x`{op3}`{b}`=`0$$/수식$$, $$수식$$LEFT ( x`{op0}`{p_} RIGHT ) LEFT(x`{op1}`{q_} RIGHT ) `=` 0 $$/수식$$\n"\
              "$$수식$$THEREFORE~x`=`{p}`$$/수식$$ 또는 $$수식$$x `=` {q}$$/수식$$\n"\
              "$$수식$$y`=` x^2 `{op2}`{a}x`{op3}`{b}$$/수식$$에 $$수식$$x `=` 0$$/수식$$을 대입하면 $$수식$$y `=` {b}$$/수식$$\n"\
              "따라서 $$수식$$p `=` {p}$$/수식$$, $$수식$$q`=`{q}$$/수식$$, $$수식$$r`=`{b}$$/수식$$ 또는 " \
              "$$수식$$p `=` {q}$$/수식$$, $$수식$$q`=`{p}$$/수식$$, $$수식$$r`=`{b}$$/수식$$이므로\n"\
              "$$수식$$p`q`r`=`{an}$$/수식$$\n\n"

    p = np.random.randint(-5, 6)
    q = np.random.randint(-5, 6)
    while p == 0 :
        p= np.random.randint(-5, 6)
    while q == 0 or q == p :
        q= np.random.randint(-5, 6)
    p_ = -1 * p
    q_ = -1 * q
    a = p_ + q_
    b = p_ * q_
    while a == 0 or a == -1 or a == 1 or b == 0:
        q = np.random.randint(-5, 6)
        while q == 0 or q == p:
            q = np.random.randint(-5, 6)
        p_ = -1 * p
        q_ = -1 * q
        a = p_ + q_
        b = p_ * q_

    if p_ > 0 :
        op0 = '+'
    else :
        op0 = ''
    if q_ > 0 :
        op1 = '+'
    else :
        op1 = ''
    if a > 0 :
        op2 = '+'
    else :
        op2 = ''
    if b > 0 :
        op3 = '+'
    else :
        op3 = ''

    an = p * q * b

    stem = stem.format(a = a, b = b, op2 = op2, op3 = op3)
    answer = answer.format(an = an)
    comment = comment.format(a = a, b = b, op0 = op0, op1 = op1, op2 = op2, op3 = op3, p_ = p_, q_ = q_, p = p, q = q, an = an)
    return stem, answer, comment


def quadequation313_Stem_133():
    stem = "다음 이차함수 중에서 그래프의 축이 좌표평면에서 가장 오른쪽에 있는 것은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "그래프의 축은 다음과 같다.\n"\
              "① {s1}\n" \
              "② {s2}\n" \
              "③ {s3}\n" \
              "④ {s4}\n" \
              "⑤ {s5}\n" \
              "따라서 그래프의 축이 가장 오른쪽에 있는 것은 {anum}이다.\n\n"

    x1 = 0
    x_list = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    x2 = x_list.pop(np.random.randint(len(x_list)))
    x3 = x_list.pop(np.random.randint(len(x_list)))
    x4 = 1/2


    # 1번
    a1 = np.random.randint(-5, 6)
    while a1 == 0 or a1 == 1 or a1 == -1 :
        a1 = np.random.randint(-5, 6)
    b1 = np.random.randint(-5, 6)
    while b1 == 0 :
        b1 = np.random.randint(-5, 6)
    if b1 > 0 :
        op1 = '+'
    else :
        op1 = ''

    n1 = f"$$수식$$y`=`{a1}x^2 `{op1}` {b1}$$/수식$$"
    z1 = f"$$수식$$x`=`0$$/수식$$"
    # 2번
    a2 = np.random.randint(-5, 6)
    while a2 == 0 or a2 == -1 or a2 == 1 :
        a2 = np.random.randint(-5, 6)
    b2 = -x2
    if b2 > 0 :
        op2 = '+'
    else :
        op2 = ''

    n2 = f"$$수식$$y`=`{a2} LEFT ( x `{op2} `{b2} RIGHT )^2$$/수식$$"
    z2 = f"$$수식$$x`=`{x2}$$/수식$$"

    # 3번
    a3 = np.random.randint(-5, 6)
    while a3 == 0 or a3 == -1 or a3 == 1:
        a3 = np.random.randint(-5, 6)
    b3 = -x3
    if b3 > 0 :
        op3 = '+'
    else :
        op3 = ''
    c3 = np.random.randint(-9, 10)
    while c3 == 0 :
        c3 = np.random.randint(-9, 10)
    if c3 > 0 :
        op3_2 = '+'
    else :
        op3_2 = ''
    n3 = f"$$수식$$y`=`{a3} LEFT ( x `{op3}` {b3} RIGHT ) ^2 {op3_2} {c3}$$/수식$$"
    z3 = f"$$수식$$x`=`{x3}$$/수식$$"

    # 4번
    b4 = 2
    c4 = np.random.randint(-5, 6)
    while c4 == 0 :
        c4 = np.random.randint(-5, 6)

    if c4 > 0 :
        op4 = '+'
    else :
        op4 = ''
    c4_t = (-1 + 4 * c4)
    if c4_t < 0 :
        c4_tt = c4_t * -1
    else :
        c4_tt = c4_t
    gcd_c4 = gcd(c4_tt, 4)
    c4_1 = int(c4_t / gcd_c4)
    c4_2 = int(4 / gcd_c4)
    if c4_1 > 0 :
        op4_2 = '+'
    else :
        c4_1 = c4_1 * -1
        op4_2 = '-'
    n4 = f"$$수식$$y`=` x^2 `-` x {op4}`{c4}$$/수식$$"
    z4 = f"$$수식$$y`=` LEFT( x `-` 1 over 2 RIGHT )^2 `{op4_2}` {c4_1} over {c4_2}$$/수식$$이므로 $$수식$$x`=` 1 over 2$$/수식$$"

    # 5번
    a5 = [3, 5, 7][np.random.randint(0, 3)]
    b5_1 = a5
    b5_2 = 2

    c5 = np.random.randint(-5, 6)
    while c5 == 0 :
        c5 = np.random.randint(-5, 6)
    c5_1 = -1 * a5 + c5 * 4
    c5_2 = b5_2**2

    if c5_1 < 0 :
        c5_1t = -1 * c5_1
    else :
        c5_1t = c5_1
    gcd_c5 = gcd(c5_1t, c5_2)
    c5_1 = int(c5_1 / gcd_c5)
    c5_2 = int(c5_2 / gcd_c5)

    while c5_2 == 1 :
        c5 = np.random.randint(-5, 6)
        while c5 == 0:
            c5 = np.random.randint(-5, 6)
        c5_1 = -1* int( ((b5_1** 2)/a5)) + c5 * b5_2
        c5_2 = b5_2 ** 2

        if c5_1 < 0:
            c5_1t = -1 * c5_1
        else:
            c5_1t = c5_1
        gcd_c5 = gcd(c5_1t, c5_2)
        c5_1 = int(c5_1 / gcd_c5)
        c5_2 = int(c5_2 / gcd_c5)
    if c5 > 0 :
        op5 = '+'
    else :
        op5 = ''

    if c5_1 > 0 :
        op5_2 = '+'
    else :
        op5_2 = '-'
    n5 = f"$$수식$$ 1 over {a5} x^2 `+`x`{op5}`{c5}$$/수식$$"
    z5 = f"$$수식$$1 over {a5} LEFT ( x `+` {b5_1} over {b5_2} RIGHT ) ^2 {op5_2}` {c5_1t} over {c5_2} $$/수식$$이므로 $$수식$$x`=` - {b5_1} over {b5_2}$$/수식$$"
    x5 = -1 * (b5_1 / b5_2)

    x_dict = {x1 :0, x2:1, x3:2, x4:3, x5:4}
    nz_dict = {n1:z1, n2:z2, n3:z3, n4:z4, n5:z5}
    x_list = [x1, x2, x3, x4, x5]
    x_list.sort(reverse=True)

    an = x_dict[x_list[0]] #번째
    n_list = [n1, n2, n3, n4, n5]

    candidates = [n1, n2, n3, n4, n5]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == n_list[an]:
            correct_idx = idx
    s1 = nz_dict[a1]
    s2 = nz_dict[a2]
    s3 = nz_dict[a3]
    s4 = nz_dict[a4]
    s5 = nz_dict[a5]
    stem = stem.format(a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(s1 = s1, s2 = s2, s3 = s3, s4 = s4, s5 = s5, anum = answer_dict[correct_idx])
    return stem, answer, comment


def quadequation313_Stem_134():
    stem = "이차함수 $$수식$$y`=`x^2`{op0}`{k}x`+`b`$$/수식$$의 그래프의 꼭짓점의 좌표가 $$수식$$LEFT ( a, ``{q} RIGHT )$$/수식$$일 때, " \
           "$$수식$$b`-`a`$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`x^2`{op0}`{k}x`+`b`=`(x`{op0}`{a_})^2`-{a2}`+`b`$$/수식$$이므로 꼭짓점의 좌표는 $$수식$$LEFT ( {a}, ``-{a2}`+`b RIGHT )$$/수식$$\n"\
              "따라서 $$수식$$a`=`{a}$$/수식$$, $$수식$$-{a2}`+`b`=`{q}$$/수식$$에서 $$수식$$b`=`{b}$$/수식$$\n"\
              "$$수식$$THEREFORE~b`-`a`=`{b}`-`{lg}{a}{rg}`=`{an}$$/수식$$\n\n"

    a = np.random.randint(-5, 6)
    while a == 0 :
        a = np.random.randint(-5, 6)
    a_ = -1 * a
    k = -2 * a
    if k > 0 :
        op0 = '+'
    else :
        op0 = ''
    q = np.random.randint(-9, 10)
    while q == 0 :
        q = np.random.randint(-9, 10)
    a_2 = a**2
    b = q + a_2
    if a < 0 :
        lg = "("
        rg = ")"
    else :
        lg = ""
        rg = ""
    an = b - a

    candidates = [an, an-1, an+1, an+2, an+3]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx

    stem = stem.format(op0 = op0, k = k, q = q, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(op0 = op0, k = k, a = a, a2 = a_2, a_ = a_, b = b, an = an, q = q, lg = lg, rg = rg)
    return stem, answer, comment


def quadequation313_Stem_135():
    stem = "다음 이차함수 중에서 그래프의 꼭짓점이 제$$수식$${n}$$/수식$$사분면에 있는 것은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "그래프의 꼭짓점은 다음과 같다.\n"\
              "① {s1} \n"\
              "② {s2} \n"\
              "③ {s3} \n"\
              "④ {s4} \n"\
              "⑤ {s5} \n"\
              "따라서 꼭짓점이 제$$수식$${n}$$/수식$$사분면에 있는 것은 {anum}이다.\n\n"

    n = np.random.randint(1, 5)

    # 1번 - 1사분면
    k1 = np.random.randint(-3, 4)
    while k1 == 0 :
        k1 = np.random.randint(-3, 4)
    x1 = np.random.randint(1, 6)
    y1 = np.random.randint(1, 10)
    if k1 == 1 :
        k_1 = ''
    elif k1 == -1:
        k_1 = '-'
    else :
        k_1 = k1

    m1 = -2*x1*k1
    n1 = k1*x1**2+y1
    if m1 > 0 :
        op1 = '+'
    else:
        op1 = ''
    if n1 > 0 :
        op1_ = '+'
    else :
        op1_ = ''
    o1 = f"$$수식$$y`=`{k_1}x^2`{op1}`{m1}x`{op1_}`{n1}$$/수식$$"
    z1 = f"$$수식$$y`=`{k_1}LEFT( x`-`{x1} RIGHT )^2 `+` {y1}$$/수식$$이므로 $$수식$$LEFT ( {x1},``{y1} RIGHT ) $$/수식$$"

    # 2번 - 2사분면
    k2 = np.random.randint(-3, 4)
    while k2 == 0 :
        k2 = np.random.randint(-3, 4)
    x2 = np.random.randint(-5, 0)
    y2 = np.random.randint(1, 10)

    if k2 == 1:
        k_2 = ''
    elif k2 == -1:
        k_2 = '-'
    else:
        k_2 = k2

    m2 = -2 * x2 * k2
    n2 = k2 * x2 ** 2 + y2

    if m2 > 0:
        op2 = '+'
    else:
        op2 = ''
    if n2 > 0:
        op2_ = '+'
    else:
        op2_ = ''
    x2_ = -1 * x2
    o2 = f"$$수식$$y`=`{k_2}x^2`{op2}`{m2}x`{op2_}`{n2}$$/수식$$"
    z2 = f"$$수식$$y`=`{k_2}LEFT( x`+`{x2_} RIGHT )^2 `+` {y2}$$/수식$$이므로 $$수식$$LEFT ( {x2},``{y2} RIGHT ) $$/수식$$"

    # 3번 - 3사분면
    k3 = np.random.randint(-3, 4)
    while k3 == 0:
        k3 = np.random.randint(-3, 4)
    x3 = np.random.randint(-5, 0)
    y3 = np.random.randint(-9, 0)

    if k3 == 1:
        k_3 = ''
    elif k3 == -1:
        k_3 = '-'
    else:
        k_3 = k3

    m3 = -2 * x3 * k3
    n3 = k3 * x3**2 + y3

    if m3 > 0:
        op3 = '+'
    else:
        op3 = ''
    if n3 > 0:
        op3_ = '+'
    else:
        op3_ = ''
    x3_ = -1 * x3
    o3 = f"$$수식$$y`=`{k_3}x^2`{op3}`{m3}x`{op3_}`{n3}$$/수식$$"
    z3 = f"$$수식$$y`=`{k_3}LEFT( x`+`{x3_} RIGHT )^2 `{y3}$$/수식$$이므로 $$수식$$LEFT ( {x3},``{y3} RIGHT ) $$/수식$$"

    # 4번 - 4사분면
    k4 = np.random.randint(-3, 4)
    while k4 == 0:
        k4 = np.random.randint(-3, 4)
    x4 = np.random.randint(1, 6)
    y4 = np.random.randint(-9, 0)

    if k4 == 1:
        k_4 = ''
    elif k4 == -1:
        k_4 = '-'
    else:
        k_4 = k4

    m4 = -2 * x4 * k4
    n4 = k4 * x4 **2 + y4

    if m4 > 0:
        op4 = '+'
    else:
        op4 = ''
    if n4 > 0:
        op4_ = '+'
    else:
        op4_ = ''
    o4 = f"$$수식$$y`=`{k_4}x^2`{op4}`{m4}x`{op4_}`{n4}$$/수식$$"
    z4 = f"$$수식$$y`=`{k_4}LEFT( x`-`{x4} RIGHT )^2 ` {y4}$$/수식$$이므로 $$수식$$LEFT ( {x4},``{y4} RIGHT ) $$/수식$$"

    # 5번 - ?
    k5 = np.random.randint(-3, 4)
    while k5 == 0:
        k5 = np.random.randint(-3, 4)
    x5 = np.random.randint(1, 6)
    if n == 1 or n == 2 :
        y5 = np.random.randint(-9, 0)
        op5_2 = ''
        while x5 == x3 or x5 == x4 :
            x5 = np.random.randint(1, 6)
    else :
        y5 = np.random.randint(1, 10)
        op5_2 = '+'
        while x5 == x1 or x5 == x2 :
            x5 = np.random.randint(1, 6)
    if k5 == 1:
        k_5 = ''
    elif k5 == -1:
        k_5 = '-'
    else:
        k_5 = k5

    m5 = -2 * x5 * k5
    n5 = k5 * x5 ** 2 + y5

    if m5 > 0:
        op5 = '+'
    else:
        op5 = ''
    if n5 > 0:
        op5_ = '+'
    else:
        op5_ = ''
    o5 = f"$$수식$$y`=`{k_5}x^2`{op5}`{m5}x`{op5_}`{n5}$$/수식$$"
    z5 = f"$$수식$$y`=`{k_5}LEFT( x`-`{x5} RIGHT )^2 `{op5_2}`{y5}$$/수식$$이므로 $$수식$$LEFT ( {x5},``{y5} RIGHT ) $$/수식$$"

    oz_dict = {o1 : z1, o2 : z2, o3 :z3, o4:z4, o5 :z5}
    candidates = [o1, o2, o3, o4, o5]
    an = candidates[n-1]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx

    s1 = oz_dict[a1]
    s2 = oz_dict[a2]
    s3 = oz_dict[a3]
    s4 = oz_dict[a4]
    s5 = oz_dict[a5]

    stem = stem.format(a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5, n = n)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(n = n, s1 = s1, s2 = s2, s3 = s3, s4 = s4, s5 = s5, anum = answer_dict[correct_idx])
    return stem, answer, comment


def quadequation313_Stem_136():
    stem = "이차함수 $$수식$$y={k_}x ^2 {op1}{o}x`+`a$$/수식$$와 $$수식$$y= 1 over 2 x ^2 -`bx{op2}`{m}`$$/수식$$의 그래프의 꼭짓점이 일치할 때, $$수식$$a`+`b$$/수식$$의 값은?\n"\
           "(단, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$는 상수이다.)\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y={k_}x ^2 {op1}{o}x`+`a$$/수식$$\n"\
              "$$수식$$``=`{k_} LEFT ( x^2 {op0}{x_2_}x`+`{x2}`-`{x2}` RIGHT ) `+` a$$/수식$$\n"\
              "$$수식$$``=`{k_} LEFT ( x `{op0}`{x_} RIGHT ) ^2 `+`a`{op0_}`{l}$$/수식$$\n"\
              "이므로 꼭짓점의 좌표는 $$수식$$LEFT ( {x}, a`{op0_}`{l} RIGHT )$$/수식$$이다.\n"\
              "$$수식$$y= 1 over 2 x ^2 -`bx{op2}`{m}`$$/수식$$\n"\
              "$$수식$$``=`1 over 2 LEFT( x^2 -2bx `+` b^2 `-`b^2 RIGHT ) `{op2}`{m}$$/수식$$\n"\
              "$$수식$$``=` 1 over 2 LEFT ( x `-` b RIGHT ) ^2 `-` 1 over 2 b^2 `{op2}`{m}$$/수식$$\n"\
              "이므로 꼭짓점의 좌표는 $$수식$$LEFT ( b, - 1 over 2 b^2 `{op2}`{m} RIGHT )$$/수식$$이다.\n"\
              "두 그래프의 꼭짓점이 일치하므로 $$수식$$b `=` {x}$$/수식$$\n"\
              "$$수식$$- 1 over 2 b ^2 `{op2}`{m} `=` a {op0_}`{l}$$/수식$$에서 $$수식$$a `=` {a}$$/수식$$\n"\
              "$$수식$$THEREFORE~a`+`b`=`{an}$$/수식$$\n\n"

    x = np.random.randint(-5, 6)
    while x == 0 or x % 2 != 0:
        x = np.random.randint(-5, 6)

    m = np.random.randint(-9, 10)
    while m == 0 :
        m = np.random.randint(-9, 10)
    if m > 0 :
        op2 = '+'
    else :
        op2 = ''
    y = int(-0.5*(x**2) + m)

    k = np.random.randint(-2, 3)
    while k == 0 :
        k = np.random.randint(-2, 3)

    if k == -1 :
        k_ = '-'
    elif k == 1 :
        k_= ''
    else :
        k_ = k

    x_2 = x * 2
    x2 = x ** 2
    if x > 0 :
        op0 = '-'
        x_ = x
        x_2_ = x_2
    else :
        op0 = '+'
        x_ = -x
        x_2_ = x_2 * -1
    l = -k * x2
    if l > 0 :
        op0_ = '+'
    else :
        op0_ = ''

    o = -1 * k * x_2

    if o > 0 :
        op1 = '+'
    else :
        op1 = ''

    b = x
    a = int(-0.5 * (b**2) + m - l)

    an = a + b

    candidates = [an, an-1, an+1, an+2, an-2]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx

    stem = stem.format(k_ = k_, op1 = op1, op2 = op2, o = o, m = m, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(x_2_ = x_2_, x_ = x_, x_2 = x_2, x2 = x2, k_ = k_, op1 = op1, o = o, m = m, op2 = op2, op0 = op0, op0_ = op0_, l = l, x = x, y = y, an = an, a = a, b = b)
    return stem, answer, comment


def quadequation313_Stem_137():
    stem = "이차함수 $$수식$$y`=` {op0}` 1 over {m} x^2 `{op1}` 2 over {m} kx`{op2}`{n}$$/수식$$의 그래프의 축의 방정식이 $$수식$$x`=`{p}$$/수식$$일 때, " \
           "상수 $$수식$$k$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=` {op0}` 1 over {m} x^2 `{op1}` 2 over {m} kx`{op2}`{n} `=` {op0}` 1 over {m} LEFT ( x `{op3}` k RIGHT )^2 `{op4}` 1 over {m} k^2 `{op2}`{n}$$/수식$$\n"\
              "따라서 그래프의 축의 방정식이 $$수식$$x`=`k$$/수식$$이므로 $$수식$$k`=`{p}$$/수식$$\n\n"

    p = np.random.randint(-5, 6)
    while p == 0 :
        p = np.random.randint(-5, 6)

    m = np.random.randint(3, 10)
    while m % 2 == 0 :
        m = np.random.randint(3, 10)
    op0 = ['+', '-'][np.random.randint(0, 2)]

    if op0 == '+' :
        m_ = m
    else :
        m_ = -m

    if p > 0 :
        op3 = '-'
    else :
        op3 = '+'

    if op3 == '+' :
        if op0 == '-' :
            op1 = '-'
        else :
            op1 = '+'
    else :
        if op0 == '-' :
            op1 = '+'
        else :
            op1 = '-'
    n = np.random.randint(-9, 10)
    while n == 0 :
        n = np.random.randint(-9, 10)

    if n > 0 :
        op2 = '+'
    else :
        op2 = ''

    if op0 == '+' :
        op4 = '-'
    else :
        op4 = '+'
    an = p
    if op0 == '+' :
        op0 = ''
    candidates = [an, an-1, an+1, an+2, an+3]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx

    stem = stem.format(op0 = op0, op1 = op1, op2 = op2, m = m, n = n, p = p, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(op0 = op0, op1 = op1, op2 = op2, op3 = op3, op4 = op4, m = m, n = n, p = p)
    return stem, answer, comment


def quadequation313_Stem_138():
    stem = "이차함수 $$수식$$y`=`x^2 `-{a}kx`+`{b}k^2 `{op0}`{c}k`{op1}`{d}`$$/수식$$의 그래프의 꼭짓점이 제$$수식$${n}$$/수식$$사분면에 있을 때, 상수 $$수식$$k$$/수식$$의 값의 범위는?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`x^2 `-{a}kx`+`{b}k^2 `{op0}`{c}k`{op1}`{d}`$$/수식$$\n" \
              "$$수식$$``=` LEFT ( x `-` {e}k RIGHT )^2 `{op0}`{c}k `{op1}`{d}$$/수식$$\n"\
              "이므로 이 이차함수의 그래프의 꼭짓점의 좌표는 $$수식$$LEFT ({e}k, ``{op0_}{c}k`{op1}{d} RIGHT )$$/수식$$\n"\
              "이 꼭짓점이 제$$수식$${n}$$/수식$$사분면에 있으므로 \n"\
              "$$수식$${e}k `{ch0}` 0$$/수식$$에서 $$수식$$k`{ch0}`0$$/수식$$, $$수식$${op0_}{c}k`{op1}`{d}`{ch1}`0$$/수식$$에서 $$수식$$k`{ch2}`{op2}`{d} over {c}$$/수식$$\n"\
              "따라서 구하는 상수 $$수식$$k$$/수식$$의 값의 범위는 $$수식$${an}$$/수식$$이다.\n\n"

    e = np.random.randint(2, 10)

    a = 2 * e
    b = e ** 2

    n = np.random.randint(1, 5)
    c = np.random.randint(2, 10)
    d = np.random.randint(1, 10)
    while gcd(c, d) != 1 :
        c = np.random.randint(2, 10)
        d = np.random.randint(1, 10)

    # 1사분면
    if n == 1 :
        ch0 = '&gt;'
        ch1 = '&gt;'
        op0 = '-'
        op0_ = '-'
        op1 = '+'
        op2 = ''
        ch2 = '&lt;'
        an = f"$$수식$$0 `&lt;` k `&lt;` {d} over {c}$$/수식$$"

    # 2사분면
    elif n == 2 :
        ch0 = '&lt;'
        ch1 = '&gt;'
        op0 = '+'
        op0_ = ''
        op1 = '+'
        op2 = '-'
        ch2 = '&gt;'
        an = f"$$수식$${op2} {d} over {c} `&lt;` k `&lt;` 0$$/수식$$"

    # 3사분면
    elif n == 3 :
        ch0 = '&lt;'
        ch1 = '&lt;'
        op0 = '-'
        op0_ = '-'
        op1 = '-'
        op2 = '-'
        ch2 = '&gt;'
        an = f"$$수식$${op2} {d} over {c} `&lt;` k `&lt;` 0$$/수식$$"

    # 4사분면
    elif n == 4 :
        ch0 = '&gt;'
        ch1 = '&lt;'
        op0 = '+'
        op0_ = ''
        op1 = '-'
        op2 = ''
        ch2 = '&lt;'
        an = f"$$수식$$0 `&lt;` k `&lt;` {d} over {c}$$/수식$$"


    d_ = d + 2
    if gcd(c, d_) != 1 :
        d_ += 1
    if d != 1 :
        an_2 = f"$$수식$$0 `&lt;` k `&lt;` {c} over {d}$$/수식$$"
        an_3 = f"$$수식$$0 `&lt;` k `&lt;` {d_} over {c}$$/수식$$"
        an_4 = f"$$수식$$- {c} over {d} `&lt;` k `&lt;` 0$$/수식$$"
        an_5 = f"$$수식$$- {d_} over {c} `&lt;` k `&lt;` 0$$/수식$$"
    else :
        an_2 = f"$$수식$$0 `&lt;` k `&lt;` {c}$$/수식$$"
        an_3 = f"$$수식$$0 `&lt;` k `&lt;` {d_} over {c}$$/수식$$"
        an_4 = f"$$수식$$- {c}`&lt;` k `&lt;` 0$$/수식$$"
        an_5 = f"$$수식$$- {d_} over {c} `&lt;` k `&lt;` 0$$/수식$$"

    candidates = [an, an_2, an_3, an_4, an_5]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx

    stem = stem.format(n = n, a = a, b = b, c = c, d = d, op0 = op0, op1 = op1, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(an = an, op0_ = op0_, n = n, a = a, b = b, c = c, d = d, op0 = op0, op1 = op1, op2 = op2, ch0 = ch0, ch1 = ch1, ch2 = ch2, e = e )
    return stem, answer, comment


def quadequation313_Stem_139():
    stem = "$$수식$$y`=`- 1 over {k} x ^2 `+`{n_3}px`{op0}`{q}`$$/수식$$의 그래프의 축의 $$수식$$x`=`{m}$$/수식$$방정식이 일 때, 상수 $$수식$$p$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`- 1 over {k} x ^2 `+`{n_3}px`{op0}`{q}`$$/수식$$\n"\
              "$$수식$$``=`- 1 over {k} LEFT ( x^2 `-`{n_2}px `+` {n2}p^2 `-`{n2}p^2 RIGHT ) `{op0}` {q}$$/수식$$\n"\
              "$$수식$$``=`- 1 over {k} LEFT ( x `-`{n}p RIGHT ) ^2 `+` {n2_}p^2 `{op0}` {q}$$/수식$$\n"\
              "따라서 축의 방정식이 $$수식$$x `=` {n}p$$/수식$$이므로 \n"\
              "$$수식$${n}p `=` {m} ````````````THEREFORE~p`=`{p}$$/수식$$ \n\n"

    k = np.random.randint(2, 9)
    while k % 2 != 0 :
        k = np.random.randint(2, 9)
    n_2 = k * np.random.randint(2, 5)
    n = int(n_2/2)
    while n % 2 != 0 :
        n_2 = k * np.random.randint(2, 5)
        n = int(n_2 / 2)

    n2 = n**2
    n_3 = int(n_2 / k)
    n2_ = int(n2/k)
    q = np.random.randint(-9, 10)
    while q == 0 :
        q = np.random.randint(-9, 10)
    if q > 0 :
        op0 = '+'
    else :
        op0 = ''
    m = n * np.random.randint(-5, 6)
    while m == 0 :
        m = n * np.random.randint(-5, 6)
    p = int(m / n)

    an = p

    candidates = [[an, an-1, an-2, an+1, an+2], [an, an-1, an-2, an-3, an+1],[an, an+1, an+2, an+3, an+4],[an, an-1, an-2, an-3, an-4]][np.random.randint(0, 4)]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx

    stem = stem.format(q = q, k = k, op0 = op0, n_3 = n_3, m = m, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 =a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(k = k, op0 = op0, q = q, n_3 = n_3, n_2 = n_2, n2 = n2, n2_ = n2_, m = m, n = n, p = p)
    return stem, answer, comment


def quadequation313_Stem_140():
    stem = "$$수식$$y`=`{k_}x^2`{op2}`{n}x`{op1}`{m}$$/수식$$의 그래프의 축의 방정식은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{k_}x^2`{op2}`{n}x`{op1}`{m}$$/수식$$\n"\
              "$$수식$$``=`{k_} LEFT ( x^2 `{op0}`{p_2}x`+`{p2}`-`{p2} RIGHT ) `{op1}`{m}$$/수식$$\n"\
              "$$수식$$``=`{k_} LEFT ( x `{op0}` {p_} RIGHT )^2 `{op3}`{q}$$/수식$$\n"\
              "따라서 축의 방정식이 $$수식$$x `=` {p}$$/수식$$이다.\n\n"

    p = np.random.randint(-5, 6)
    while p == 0 :
        p = np.random.randint(-5, 6)
    p_ = p * -1
    if p_ > 0 :
        op0 = '+'
    else :
        op0 = ''
    k = np.random.randint(-5, 6)
    while k == 0 :
        k = np.random.randint(-5, 6)

    if k == 1 :
        k_ = ''
    elif k == -1 :
        k_ = '-'
    else :
        k_ = k
    p_2 = 2 * p_
    p2 = p**2
    n = k * p_2
    if n > 0 :
        op2 = '+'
    else :
        op2 = ''

    m = np.random.randint(-10, 11)
    while m == 0 :
        m = np.random.randint(-10, 11)
    q = m + k*(-p2)
    while q == 0 :
        m = np.random.randint(-10, 11)
        while m == 0:
            m = np.random.randint(-10, 11)
        q = m + k * (-p2)

    if m > 0 :
        op1 = '+'
    else :
        op1 = ''
    if q > 0 :
        op3 = '+'
    else :
        op3 = ''
    candidates = [p, -p, p+1, p-1, -p*2]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == p:
            correct_idx = idx

    stem = stem.format(k_ = k_, n = n, m = m, op1 = op1, op2 = op2, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 =a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(k_ = k_, n = n, m = m, p_ = p_, p = p, p_2 = p_2, p2 = p2, op0 = op0, op1 = op1, op2 = op2, op3 = op3, q = q)
    return stem, answer, comment


def quadequation313_Stem_141():
    stem = "이차함수 $$수식$$y`=`{m}x^2`{op0}`{k_}x`+`a`$$/수식$$의 그래프는 $$수식$$x$$/수식$$축과 서로 다른 두 점에서 만난다. " \
           "두 교점 중 한 점의 $$수식$$x$$/수식$$좌표가 $$수식$${n} over {m}$$/수식$$일 때, 이 그래프가 $$수식$$y$$/수식$$축과 만나는 점의 좌표는?\n"\
           "(단, $$수식$$a$$/수식$$는 상수이다.)\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{m}x^2`{op0}`{k_}x`+`a`$$/수식$$에 $$수식$$x`=`{n} over {m}$$/수식$$, $$수식$$y`=`0$$/수식$$을 대입하면\n"\
              "$$수식$$0`=`{n2} over {m} `{op0_}` {l} over {m} `+` a ````````````THEREFORE~a`=`{a}$$/수식$$\n"\
              "$$수식$$y`=`{m}x^2`{op0}`{k_}x`+`a`$$/수식$$에 $$수식$$x`=`0$$/수식$$을 대입하면 $$수식$$y`=`{a}$$/수식$$\n"\
              "따라서 이 그래프가 $$수식$$y$$/수식$$축과 만나는 점의 좌표는 $$수식$$LEFT ( 0, `` {a} RIGHT )$$/수식$$이다.\n\n"

    m = np.random.randint(2, 10)
    n = np.random.randint(1, m)
    while gcd(m, n) != 1 :
        n = np.random.randint(1, m)
    n2 = n ** 2

    tmp = np.random.randint(-4, 5)
    while tmp == 0  :
        tmp = np.random.randint(-4, 5)
    k = ((m*tmp - n2)/n)

    l = n * k
    while k == 0 or (n2 + l)% n != 0 or k % n != 0:
        n = np.random.randint(1, m)
        while gcd(m, n) != 1:
            n = np.random.randint(1, m)
        n2 = n ** 2
        tmp = np.random.randint(-4, 5)
        while tmp == 0:
            tmp = np.random.randint(-4, 5)
        k = ((m * tmp - n2) / n)
        l = n * k

    k = int(k)
    a = -(int((n2+l)/m))
    l = abs(int(l))
    if k  == 1 :
        k_ = ''
    elif k == -1 :
        k_ = '-'
    else :
        k_ = k

    if n*k > 0 :
        op0_ = '+'
    else :
        op0_ = '-'
    if k > 0 :
        op0 = '+'
    else :
        op0 = ''

    if a > 0 :
        op1 = '+'
    else :
        op1 = ''

    a2 = a - 1
    a3 = a - 2
    a4 = a + 1
    a5 = a + 2
    an = f"$$수식$$LEFT ( 0, ``{a} RIGHT )$$/수식$$"
    an2 = f"$$수식$$LEFT ( 0, ``{a2} RIGHT )$$/수식$$"
    an3 = f"$$수식$$LEFT ( 0, ``{a3} RIGHT )$$/수식$$"
    an4 = f"$$수식$$LEFT ( 0, ``{a4} RIGHT )$$/수식$$"
    an5 = f"$$수식$$LEFT ( 0, ``{a5} RIGHT )$$/수식$$"
    candidates = [an, an2, an3, an4, an5]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx

    stem = stem.format(m = m, n = n, op0 = op0, k_ = k_, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 =a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(l = l, n2 = n2, k_ = k_, k = k, m = m, n = n, a = a, op0 = op0, op1 = op1, op0_ = op0_)
    return stem, answer, comment


def quadequation313_Stem_142():
    stem = "다음 이차함수 중에서 그래프의 축이 좌표평면에서 가장 왼쪽에 있는 것은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "그래프의 축은 다음과 같다.\n"\
              "① {s1}\n" \
              "② {s2}\n" \
              "③ {s3}\n" \
              "④ {s4}\n" \
              "⑤ {s5}\n" \
              "따라서 그래프의 축이 가장 오른쪽에 있는 것은 {anum}이다.\n\n"

    x1 = 0
    x_list = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    x2 = x_list.pop(np.random.randint(len(x_list)))
    x3 = x_list.pop(np.random.randint(len(x_list)))
    x4 = 1/2


    # 1번
    a1 = np.random.randint(-5, 6)
    while a1 == 0 or a1 == 1 or a1 == -1 :
        a1 = np.random.randint(-5, 6)
    b1 = np.random.randint(-5, 6)
    while b1 == 0 :
        b1 = np.random.randint(-5, 6)
    if b1 > 0 :
        op1 = '+'
    else :
        op1 = ''

    n1 = f"$$수식$$y`=`{a1}x^2 `{op1}` {b1}$$/수식$$"
    z1 = f"$$수식$$y`=`{a1}x^2 `{op1}` {b1}$$/수식$$의 그래프의 축의 방정식은 $$수식$$x`=`0$$/수식$$"
    # 2번
    a2 = np.random.randint(-5, 6)
    while a2 == 0 or a2 == -1 or a2 == 1 :
        a2 = np.random.randint(-5, 6)
    b2 = -x2
    if b2 > 0 :
        op2 = '+'
    else :
        op2 = ''

    n2 = f"$$수식$$y`=`{a2} LEFT ( x `{op2} `{b2} RIGHT )^2$$/수식$$"
    z2 = f"$$수식$$y`=`{a2} LEFT ( x `{op2} `{b2} RIGHT )^2$$/수식$$의 그래프의 축의 방정식은 $$수식$$x`=`{x2}$$/수식$$"

    # 3번
    a3 = np.random.randint(-5, 6)
    while a3 == 0 or a3 == -1 or a3 == 1:
        a3 = np.random.randint(-5, 6)
    b3 = -x3
    if b3 > 0 :
        op3 = '+'
    else :
        op3 = ''
    c3 = np.random.randint(-9, 10)
    while c3 == 0 :
        c3 = np.random.randint(-9, 10)
    if c3 > 0 :
        op3_2 = '+'
    else :
        op3_2 = ''
    n3 = f"$$수식$$y`=`{a3} LEFT ( x `{op3}` {b3} RIGHT ) ^2 {op3_2} {c3}$$/수식$$"
    z3 = f"$$수식$$y`=` {a3} LEFT ( x `{op3}` {b3} RIGHT ) ^2 {op3_2} {c3}$$/수식$$의 그래프의 축의 방정식은 $$수식$$x`=`{x3}$$/수식$$"

    # 4번
    b4 = 2
    c4 = np.random.randint(-5, 6)
    while c4 == 0 :
        c4 = np.random.randint(-5, 6)

    if c4 > 0 :
        op4 = '+'
    else :
        op4 = ''
    c4_t = (-1 + 4 * c4)
    if c4_t < 0 :
        c4_tt = c4_t * -1
    else :
        c4_tt = c4_t
    gcd_c4 = gcd(c4_tt, 4)
    c4_1 = int(c4_t / gcd_c4)
    c4_2 = int(4 / gcd_c4)
    if c4_1 > 0 :
        op4_2 = '+'
    else :
        c4_1 = c4_1 * -1
        op4_2 = '-'
    n4 = f"$$수식$$y`=` x^2 `-` x {op4}`{c4}$$/수식$$"
    z4 = f"$$수식$$y`=` x^2 `-` x {op4}`{c4} `=` LEFT( x `-` 1 over 2 RIGHT )^2 `{op4_2}` {c4_1} over {c4_2}$$/수식$$의 그래프의 축의 방정식은 $$수식$$x`=` 1 over 2$$/수식$$"

    # 5번
    a5 = [3, 5, 7][np.random.randint(0, 3)]
    b5_1 = a5
    b5_2 = 2

    c5 = np.random.randint(-5, 6)
    while c5 == 0 :
        c5 = np.random.randint(-5, 6)
    c5_1 = -1 * a5 + c5 * 4
    c5_2 = b5_2**2

    if c5_1 < 0 :
        c5_1t = -1 * c5_1
    else :
        c5_1t = c5_1
    gcd_c5 = gcd(c5_1t, c5_2)
    c5_1 = int(c5_1 / gcd_c5)
    c5_2 = int(c5_2 / gcd_c5)

    while c5_2 == 1 :
        c5 = np.random.randint(-5, 6)
        while c5 == 0:
            c5 = np.random.randint(-5, 6)
        c5_1 = -1* int( ((b5_1** 2)/a5)) + c5 * b5_2
        c5_2 = b5_2 ** 2

        if c5_1 < 0:
            c5_1t = -1 * c5_1
        else:
            c5_1t = c5_1
        gcd_c5 = gcd(c5_1t, c5_2)
        c5_1 = int(c5_1 / gcd_c5)
        c5_2 = int(c5_2 / gcd_c5)
    if c5 > 0 :
        op5 = '+'
    else :
        op5 = ''

    if c5_1 > 0 :
        op5_2 = '+'
    else :
        op5_2 = '-'
    n5 = f"$$수식$$ 1 over {a5} x^2 `+`x`{op5}`{c5}$$/수식$$"
    z5 = f"$$수식$$ 1 over {a5} x^2 `+`x`{op5}`{c5} `=`1 over {a5} LEFT ( x `+` {b5_1} over {b5_2} RIGHT ) ^2 {op5_2}` {c5_1t} over {c5_2} $$/수식$$의 그래프의 축의 방정식은 $$수식$$x`=` - {b5_1} over {b5_2}$$/수식$$"
    x5 = -1 * (b5_1 / b5_2)

    x_dict = {x1 :0, x2:1, x3:2, x4:3, x5:4}
    nz_dict = {n1:z1, n2:z2, n3:z3, n4:z4, n5:z5}
    x_list = [x1, x2, x3, x4, x5]
    x_list.sort()

    an = x_dict[x_list[4]] #번째
    n_list = [n1, n2, n3, n4, n5]

    candidates = [n1, n2, n3, n4, n5]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == n_list[an]:
            correct_idx = idx
    s1 = nz_dict[a1]
    s2 = nz_dict[a2]
    s3 = nz_dict[a3]
    s4 = nz_dict[a4]
    s5 = nz_dict[a5]
    stem = stem.format(a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(s1 = s1, s2 = s2, s3 = s3, s4 = s4, s5 = s5, anum = answer_dict[correct_idx])
    return stem, answer, comment


def quadequation313_Stem_143():
    stem = "이차함수 $$수식$$y`=`{k}x ^2 `{op2_}`{ka}x`{op3_}`{kb}`$$/수식$$의 그래프와 $$수식$$x$$/수식$$축의 교점을 $$수식$$A$$/수식$$, $$수식$$B$$/수식$$라 할 때, " \
           "$$수식$$bar {lg}rmA`B{rg}$$/수식$$의 길이는?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{k}x ^2 `{op2_}`{ka}x`{op3_}`{kb}`$$/수식$$에 $$수식$$y`=`0$$/수식$$을 대입하면\n"\
              "$$수식$$0`=`{k}x ^2 `{op2_}`{ka}x`{op3_}`{kb}`$$/수식$$, $$수식$$x^2 `{op2}`{a_}x`{op3}`{b}`=`0$$/수식$$\n"\
              "$$수식$$LEFT ( x `{op0}`{p_} RIGHT ) LEFT ( x `{op1}`{q_} RIGHT) `=` 0 ````````````THEREFORE~x`=`{p}$$/수식$$ 또는 $$수식$$THEREFORE~x`=`{q}$$/수식$$\n" \
              "따라서 $$수식$$A ` LEFT ( {p}, ``0 RIGHT )$$/수식$$,  $$수식$$B ` LEFT ( {q}, ``0 RIGHT )$$/수식$$ " \
              "또는 $$수식$$A ` LEFT ( {q}, ``0 RIGHT )$$/수식$$,  $$수식$$B ` LEFT ( {p}, ``0 RIGHT )$$/수식$$이므로 $$수식$$bar {lg}rmA`B{rg} `=` {an}$$/수식$$\n\n"

    p = np.random.randint(-9, 10)
    while p == 0 :
        p = np.random.randint(-9, 10)
    q = np.random.randint(-9, 10)
    while q == 0 or p == q or p == -q:
        q = np.random.randint(-9, 10)

    p_ = -p
    q_ = -q

    a = p_ + q_
    b = p_ * q_

    if p_ > 0 :
        op0 = '+'
    else :
        op0 = ''

    if q_ > 0 :
        op1 = '+'
    else :
        op1 = ''
    k = np.random.randint(-5, 6)
    while k == 0 or k == -1 or k == 1:
        k = np.random.randint(-5, 6)

    if a == 1 or a == -1:
        a_ = ''
    else :
        a_ = a
    ka = k * a
    kb = k * b
    if ka > 0 :
        op2_ = '+'
    else :
        op2_ = ''
    if kb > 0 :
        op3_ = '+'
    else :
        op3_ = ''

    if a > 0 :
        op2 = '+'
    else :
        op2 = ''
    if b > 0 :
        op3 = '+'
    else :
        op3 = ''
    an = abs(p-q)
    if an == 1 :
        candidates = [an, an+1, an+2, an+3, an+4]
    else :
        candidates = [an-1, an, an+1, an+2, an+3]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx

    lg = "{"
    rg = "}"
    stem = stem.format(lg = lg, rg = rg, k= k, ka = ka, kb = kb, op2_ = op2_, op3_ = op3_, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 =a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(lg = lg, rg = rg, a_ = a_, p_ = p_, q_ = q_, k = k, ka = ka, kb = kb, a = a, b = b, p = p, q = q, an = an, op0 = op0, op1 = op1, op2 = op2, op3 = op3, op2_ = op2_, op3_ = op3_)
    return stem, answer, comment


def quadequation313_Stem_144():
    stem = "이차함수 $$수식$$y={p}x ^2 {a}x{q_}`$$/수식$$의 그래프가 $$수식$$x$$/수식$$축과 만나는 두 점의 $$수식$$x$$/수식$$좌표가 $$수식$$p$$/수식$$, $$수식$$q$$/수식$$이고, " \
           "$$수식$$y$$/수식$$축과 만나는 점의 $$수식$$y$$/수식$$좌표가 $$수식$$r$$/수식$$일 때, $$수식$${k}p`+`q`+`r`$$/수식$$의 값을 구하시오. (단, $$수식$$p `&lt;` q$$/수식$$)\n"
    answer = "(답): $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y={p}x^2 {a}x{q_}`$$/수식$$에 $$수식$$y`=`0$$/수식$$을 대입하면\n"\
              "$$수식$$0={p}x^2 {a}x{q_}`$$/수식$$, $$수식$$LEFT ( {p}x`+`1 RIGHT) LEFT ( x `-`{q} RIGHT ) `=` 0 $$/수식$$\n"\
              "$$수식$$THEREFORE~x`=` - 1 over {p}$$/수식$$ 또는 $$수식$$x`=`{q}$$/수식$$\n"\
              "$$수식$$THEREFORE~p`=` - 1 over {p}$$/수식$$, $$수식$$q`=`{q} ````( BECAUSE~p`&lt;`q )$$/수식$$\n"\
              "$$수식$$y={p}x^2 {a}x{q_}`$$/수식$$에 $$수식$$x`=`0$$/수식$$을 대입하면 $$수식$$y`=`{r}$$/수식$$\n"\
              "$$수식$$THEREFORE~r`=`{r}$$/수식$$\n"\
              "$$수식$$THEREFORE~{k}p`+`q`+`r`=`{an}$$/수식$$\n\n"

    p = np.random.randint(2, 6)
    q = np.random.randint(1, 6)
    q_ = -q
    r = q_
    a = p*q_ + 1
    k = p * np.random.randint(1, 6)
    an = int(-1*k * (1/p) +q + r)

    stem = stem.format(p = p, a = a, q_ = q_, k = k)
    answer = answer.format(an = an)
    comment = comment.format(a = a, p = p, q = q, q_ = q_, r = r, an = an, k = k)
    return stem, answer, comment


def quadequation313_Stem_145():
    stem = "이차함수 $$수식$$y`=`ax ^2 `{op2_}{am}x`{op3_}`{bm}`$$/수식$$의 그래프는 $$수식$$x$$/수식$$축과 서로 다른 두 점에서 만난다. " \
           "두 교점 중 한 점의 좌표가 $$수식$$LEFT ( {x0}, `` 0 RIGHT )$$/수식$$일 때, 다른 한 점의 좌표는? (단, $$수식$$a$$/수식$$는 상수이다.)\n" \
           "(단, $$수식$$a$$/수식$$는 상수이다.)\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`ax ^2 `{op2_}{am}x`{op3_}`{bm}`$$/수식$$에 $$수식$$x`=`{x0}$$/수식$$, $$수식$$y`=`0$$/수식$$을 대입하면\n"\
              "$$수식$$0 `=` {m}a`{op4}`{ax}`{op3_}`{bm} ````````````THEREFORE~a`=`- 1 over {m}$$/수식$$\n"\
              "$$수식$$y`=`- 1 over {m} x ^2 `{op2_}{am_}x`{op3_}`{bm}`$$/수식$$에 $$수식$$y`=`0$$/수식$$을 대입하면\n"\
              "$$수식$$0`=`- 1 over {m} x ^2 `{op2_}{am_}x`{op3_}`{bm}`$$/수식$$, $$수식$$x^2 `{op2}`{a}x`{op3}`{b}`=`0$$/수식$$\n"\
              "$$수식$$LEFT ( x`{op1}`{x1_} RIGHT ) LEFT ( x `{op0}`{x0_} RIGHT ) `=` 0$$/수식$$\n"\
              "$$수식$$THEREFORE~x`=`{x1}$$/수식$$ 또는 $$수식$$x`=`{x0}$$/수식$$\n"\
              "따라서 다른 한 점의 좌표는 $$수식$$ LEFT ( {x1}, `` 0 RIGHT )$$/수식$$이다.\n\n"


    x0 = np.random.randint(-20, 21)
    while x0 == 0 :
        x0 = np.random.randint(-20, 21)
    x1 = np.random.randint(-20, 21)
    while x1 == 0 or x1 == x0 or x1 == -x0 or x0 + x1 == 0:
        x1 = np.random.randint(-20, 21)

    x0_ = -x0
    x1_ = -x1
    a = x0_ + x1_
    b = x0_ * x1_

    m = x0 ** 2
    bm = int(-1 * b/m)
    am = int(-1 * a / m)
    gcd_ab = gcd(abs(a), abs(b))
    while gcd_ab == 1 or (bm + am * x0 != 1) or m != gcd_ab :
        x0 = np.random.randint(-20, 21)
        while x0 == 0:
            x0 = np.random.randint(-20, 21)
        x1 = np.random.randint(-20, 21)
        while x1 == 0 or x1 == x0 or x1 == -x0 or x0 + x1 == 0:
            x1 = np.random.randint(-20, 21)

        x0_ = -x0
        x1_ = -x1
        a = x0_ + x1_
        b = x0_ * x1_

        m = x0 ** 2
        bm = int(-1 * b / m)
        am = int(-1 * a / m)
        gcd_ab = gcd(abs(a), abs(b))

    ax = am * x0
    if x0_ > 0 :
        op0 = '+'
    else :
        op0 = ''
    if x1_ > 0 :
        op1 = '+'
    else :
        op1 = ''

    if a > 0 :
        op2 = '+'
    else :
        op2 = ''
    if b > 0 :
        op3 = '+'
    else :
        op3 = ''
    if am > 0 :
        op2_ = '+'
    else :
        op2_ = ''
    if bm > 0 :
        op3_ = '+'
    else :
        op3_ = ''
    if ax > 0 :
        op4 = '+'
    else :
        op4 = ''

    if am == 1 :
        am_ = ''
    elif am == -1 :
        am_ = '-'
    else :
        am_ = am
    x2 = -x1
    x3 = np.random.randint(-20, 21)
    while x3 == x1 or x3 == x0 or x3 == x2 :
        x3 = np.random.randint(-20, 21)
    x4 = np.random.randint(-20, 21)
    while x4 == x3 or x4 == x2 or x4 == x1 or x4 == x0 :
        x4 = np.random.randint(-20, 21)
    x5 = np.random.randint(-20, 21)
    while x5 == x4 or x5 == x3 or x5 == x2 or x5 == x1 or x5 == x0 :
        x5 = np.random.randint(-20, 21)
    s1 = f"$$수식$$LEFT ( {x1}, ``0 RIGHT )$$/수식$$"
    s2 = f"$$수식$$LEFT ( {x2}, ``0 RIGHT )$$/수식$$"
    s3 = f"$$수식$$LEFT ( {x3}, ``0 RIGHT )$$/수식$$"
    s4 = f"$$수식$$LEFT ( {x4}, ``0 RIGHT )$$/수식$$"
    s5 = f"$$수식$$LEFT ( {x5}, ``0 RIGHT )$$/수식$$"

    candidates = [s1, s2, s3, s4, s5]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == s1:
            correct_idx = idx

    stem = stem.format(x0 = x0, op2_ = op2_, op3_ = op3_, am = am, bm = bm, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(am_ = am_, m = m, am = am, bm = bm, a = a, b = b, x0 = x0, x1 = x1, x0_ = x0_, x1_ = x1_, op0 = op0, op1 = op1, op2 = op2, op3 = op3, op2_ = op2_, op3_ = op3_, ax = ax, op4 = op4)
    return stem, answer, comment


def quadequation313_Stem_146():
    stem = "이차함수 $$수식$$y`=`{op0} 1 over {k} x^2 `{op3}{a}x`{op4}{b}`$$/수식$$의 그래프의 꼭짓점의 좌표가 $$수식$$LEFT ( p, `` q RIGHT )$$/수식$$이고, " \
           "$$수식$$y$$/수식$$축과 만나는 점의 $$수식$$y$$/수식$$좌표가 $$수식$$r$$/수식$$일 때, $$수식$$p`q`r`$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y`=`{op0} 1 over {k} x^2 `{op3}{a}x`{op4}{b}`=` {op0} 1 over {k} LEFT ( x `{op1}` {p_} RIGHT ) ^2 `{op2}`{q}$$/수식$$이므로 " \
              "꼭짓점의 좌표는 $$수식$$ LEFT ( {p}, ``{q} RIGHT )$$/수식$$이다.\n"\
              "$$수식$$THEREFORE~p`=`{p}`$$/수식$$, $$수식$$q`=`{q}`$$/수식$$\n"\
              "$$수식$$y`=`{op0} 1 over {k} x^2 `{op3}{a}x`{op4}{b}`$$/수식$$에 $$수식$$x`=`0$$/수식$$을 대입하면 \n"\
              "$$수식$$y`=`{b} ````````````THEREFORE~r`=`{b}$$/수식$$\n"\
              "$$수식$$THEREFORE~p`q`r`=`{an}$$/수식$$\n\n"

    op0 = ['-', ''][np.random.randint(0, 2)]
    k = np.random.randint(2, 4)
    p = np.random.randint(-3, 4) * k
    while p == 0 :
        p = np.random.randint(-3, 4) * k
    q = np.random.randint(-3, 4)
    while q == 0 or q == p :
        q = np.random.randint(-3, 4)
    p_ = -p
    if op0 == '-' :
        k_ = -k
    else :
        k_ = k

    a = int((2 * p_) / k_)
    b = int((p_**2)/k_) + q

    while b > 10 :
        p = np.random.randint(-3, 4) * k
        while p == 0:
            p = np.random.randint(-3, 4) * k
        q = np.random.randint(-3, 4)
        while q == 0 or q == p:
            q = np.random.randint(-3, 4)
        p_ = -p
        if op0 == '-':
            k_ = -k
        else:
            k_ = k

        a = int((2 * p_) / k_)
        b = int((p_ ** 2) / k_) + q
    if p_ > 0 :
        op1 = '+'
    else :
        op1 = ''
    if q > 0 :
        op2 = '+'
    else :
        op2 = ''

    if a > 0 :
        op3 = '+'
    else :
        op3 = ''
    if b > 0 :
        op4 = '+'
    else :
        op4 =''
    an = p * q * b
    if an == 0 :
        candidates = [an, an+2, an-2, an+4, an-4]
    else :
        candidates = [an, -an, an*2, -an*2, an*3]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx

    stem = stem.format(op0 = op0, k = k, a = a, b = b, op3 = op3, op4 = op4, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(op0 = op0, op1 = op1, op2 = op2, op3 = op3, op4 = op4, a = a, k = k, b = b, p_ = p_, p = p, q = q, an = an)
    return stem, answer, comment


def quadequation313_Stem_147():
    stem = "이차함수 $$수식$$y=x^2`+2ax`+`b`$$/수식$$의 그래프가 점 $$수식$$LEFT ( {x0}, `` {y0} RIGHT )$$/수식$${j1} 지나고 " \
           "꼭짓점이 직선  $$수식$$y`=`{r_}x `{op2}{s}$$/수식$$위에 있을 때, " \
           "상수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$b`-`a$$/수식$$의 값은? (단, $$수식$$a `&gt;` 0 $$/수식$$)\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답): {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$y=x^2`+2ax`+`b`$$/수식$$의 그래프가 점 $$수식$$LEFT ( {x0}, `` {y0} RIGHT )$$/수식$${j1} 지나므로\n"\
              "$$수식$${y0}`=`{x0_2} `{op3}`{m}a`+`b ````````````THEREFORE~b`=`{m_}a`{op1}`{n}$$/수식$$\n"\
              "$$수식$$THEREFORE~y`=`x^2`+2ax`{op4}`{m_}a`{op1}{n}$$/수식$$\n"\
              "$$수식$$````=`(x ^2 `+2ax`+a ^2 `-a ^2 `){op4}{m_}a`{op1}{n}$$/수식$$\n"\
              "$$수식$$````=`(x`+`a)^2`-a^2`{op4}{m_}a`{op1}{n}$$/수식$$\n"\
              "이 그래프의 꼭짓점의 좌표는 $$수식$$LEFT ( -a, ``-a^2 `{op4}{m_}a `{op1}`{n} RIGHT )$$/수식$$\n"\
              "이 꼭짓점이 직선 $$수식$$y`=`{r_}x`{op2}`{s}$$/수식$$위에 있으므로\n"\
              "$$수식$$-a^2`{op4}`{m_}a`{op1}`{n}`=`{r__}a`{op2}`{s}$$/수식$$, $$수식$$a^2`{op0}`{k_}a`{l}`=`0$$/수식$$\n"\
              "$$수식$$LEFT ( a`+`{p} RIGHT ) LEFT ( a `-` {q} RIGHT )`=`0 ````````````THEREFORE ~a`=`{q}(BECAUSE~a>0)$$/수식$$\n"\
              "$$수식$$THEREFORE~b`=`{m_} TIMES{a}`{op1}`{n}`=`{b}$$/수식$$\n"\
              "$$수식$$THEREFORE~b`-`a`=`{an}$$/수식$$\n\n"

    p = np.random.randint(1, 6)
    q = np.random.randint(1, 6)
    k = p - q
    l = -1 * p * q


    while k == 0 :
        p = np.random.randint(1, 6)
        q = np.random.randint(1, 6)
        k = p - q
        l = -1 * p * q
    if k == 1 :
        k_ = ''
    elif k == -1:
        k_ = '-'
    else :
        k_ = k

    x0 = np.random.randint(-2, 3)
    while x0 == 0 :
        x0 = np.random.randint(-2, 3)
    y0 = np.random.randint(-3, 4)
    x0_2 = x0 ** 2
    m = 2 * x0
    n = y0 - x0_2
    m_ = -m
    r = -(k + m_)
    while n == 0 or r == 0 :
        x0 = np.random.randint(-2, 3)
        while x0 == 0:
            x0 = np.random.randint(-2, 3)
        y0 = np.random.randint(-3, 4)
        x0_2 = x0 ** 2
        m = 2 * x0
        n = y0 - x0_2
        m_ = -m
        r = -(k + m_)
    s = l + n

    if k > 0 :
        op0 = '+'
    else :
        op0 = ''
    if s > 0 :
        op2 = '+'
    else :
        op2 = ''
    if n > 0 :
        op1 = '+'
    else :
        op1 = ''
    if m > 0 :
        op3 = '+'
    else :
        op3 = ''

    a = q
    b = -m * a + n
    an = b - a

    if r == 1 :
        r_ = ''
    elif r == -1 :
        r_ = '-'
    else :
        r_ = r
    r__ = -1 * r
    if r == 1 :
        r__ = ''
    elif r == -1 :
        r__ = '-'

    if m_ > 0 :
        op4 = '+'
    else :
        op4 = ''
    if an == 0 :
        candidates = [an, an+2, an-2, an+4, an-4]
    else :
        candidates = [an, -an, an*2, -an*2, an*3]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
    j1 = proc_jo(y0, 4)
    stem = stem.format(x0 = x0, y0 = y0, j1 = j1, op2 = op2, s = s, r_ = r_, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5 )
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(r_ = r_, r__ = r__, op4 = op4, m_ = m_, op3 = op3, x0_2 = x0_2, op0 = op0, k_ = k_, b = b, a = a,  x0 = x0, y0 = y0, j1 = j1, m = m, op1 = op1, n = n, op2 = op2, r = r, s = s, k = k, l = l, p = p, q = q, an = an)
    return stem, answer, comment

# 3-1-3-186
def quadequation313_Stem_148():
    stem = "$$수식$$x$$/수식$$에 대한 이차함수 " \
           "$$수식$$y = LEFT ( x + a RIGHT ) ^2 + {p1} LEFT ( a + {p2} RIGHT ) x + {p3}$$/수식$$" \
           "의 그래프의 꼭짓점의 좌표가 $$수식$$LEFT ( {s1}$$/수식$$,$$수식$$b RIGHT )$$/수식$$일 때, " \
           "상수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$ab$$/수식$$의 값을 구하시오.\n"
    answer = "(답): {ab}\n"
    comment = "(해설)\n" \
              "$$수식$$y = LEFT ( x + a RIGHT ) ^2 + {p1} LEFT ( a + {p2} RIGHT ) x + {p3}$$/수식$$\n" \
              "$$수식$$= x^2 + LEFT ( {p4} a + {p5} RIGHT ) x + a^2 + {p3}$$/수식$$\n" \
              "$$수식$$= LEFT ( x + {p6} a + {p7} RIGHT ) ^2 - {p8} a^2 - {p9} a + {p10}$$/수식$$\n" \
              "이 그래프의 꼭짓점의 좌표는 " \
              "$$수식$$LEFT ( - {p6} a - {p7}$$/수식$$, $$수식$$- {p8} a^2 - {p9} a + {p10} RIGHT )$$/수식$$이므로\n" \
              "$$수식$$- {p6} a - {p7} = {s1}$$/수식$$, $$수식$$- {p8} a^2 - {p9} a + {p10} = b$$/수식$$\n" \
              "$$수식$$THEREFORE~ a = {a1}$$/수식$$, $$수식$$b = {b1}$$/수식$$\n" \
              "$$수식$$THEREFORE~ ab = {ab}$$/수식$$\n\n"

    p1 = np.random.randint(1, 6) * 2
    p2 = np.random.randint(1, 5)
    p4 = 2 + p1
    p5 = p1*p2
    p6 = int(p4 / 2)
    p7 = int(p5 / 2)
    p8 = p6 * p6 - 1
    p9 = 2 * p6 * p7
    p10 = np.random.randint(1, 10)
    p3 = p7 * p7 + p10
    a1 = np.random.randint(-5, 6)
    b1 = p10 - p8 * a1 * a1 - p9 * a1
    s1 = - p7 - p6 * a1
    ab = a1 * b1

    stem = stem.format(p1=p1, p2=p2, p3=p3, s1=s1)
    answer = answer.format(ab=ab)
    comment = comment.format(s1=s1, a1=a1, b1=b1, ab=ab, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10)

    return stem, answer, comment





# 3-1-3-189
def quadequation313_Stem_149():
    stem = "다음 중 이차함수 $$수식$$y = x^2 + {p1} k x + {p2} k^2 - k + {p3}$$/수식$$의 그래프의 꼭짓점이 제$$수식$${dim}$$/수식$$사분면에 있을 때, " \
           "실수 $$수식$$k$$/수식$$의 값이 될 수 있는 것은?\n" \
           "① $$수식$${c1}$$/수식$$\t\t② $$수식$${c2}$$/수식$$\t\t③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\t\t⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = x^2 + {p1} k x + {p2} k^2 - k + {p3} " \
              "= LEFT ( x + {p4} k RIGHT ) ^2 - k + {p3}$$/수식$$\n" \
              "이 그래프의 꼭짓점의 좌표는 $$수식$$LEFT ( - {p4} k$$/수식$$, $$수식$$- k + {p3} RIGHT )$$/수식$$\n" \
              "이 점이 제$$수식$${dim}$$/수식$$사분면에 있으려면 $$수식$$- {p4} k {opx1} 0$$/수식$$, $$수식$$- k + {p3} {opy1} 0$$/수식$$\n" \
              "$$수식$$- {p4} k {opx1} 0$$/수식$$에서 $$수식$$k {opx2} 0$$/수식$$ \t$$수식$$CDOTS$$/수식$$㉠\n" \
              "$$수식$$- k + {p3} {opy1} 0$$/수식$$에서 $$수식$$k {opy2} {p3}$$/수식$$ \t$$수식$$CDOTS$$/수식$$㉡\n" \
              "㉠, ㉡에서 실수 $$수식$$k$$/수식$$의 값이 될 수 있는 것은 {s}이다.\n\n"

    dim = np.random.randint(1, 4)
    p4 = np.random.randint(2, 6)
    p1 = p4*2
    p2 = p4*p4
    p3 = np.random.randint(2, 6)
    if dim == 1:
        opx1 = '&gt;'
        opx2 = '&lt;'
        opy1 = '&gt;'
        opy2 = '&lt;'
        ss = np.random.randint(-3, 0)
        c = list(range(0, 4))
        c.append(ss)
    elif dim == 2:
        opx1 = '&lt;'
        opx2 = '&gt;'
        opy1 = '&gt;'
        opy2 = '&lt;'
        ss = np.random.randint(1, p3)
        c = random.sample(list(range(-p3, 1)), 2) + random.sample(list(range(p3, p3+4)), 2)
        c.append(ss)
    else:  # dim == 3
        opx1 = '&lt;'
        opx2 = '&gt;'
        opy1 = '&lt;'
        opy2 = '&gt;'
        ss = np.random.randint(p3+1, p3+4)
        c = random.sample(list(range(-p3, p3)), 4)
        c.append(ss)
    np.random.shuffle(c)
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break
    c1, c2, c3, c4, c5 = c

    stem = stem.format(p1=p1, p2=p2, p3=p3, dim=dim, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, opx1=opx1, opx2=opx2, opy1=opy1, opy2=opy2, dim=dim, s=s)

    return stem, answer, comment





# 3-1-3-192
def quadequation313_Stem_150():
    stem = "이차함수 $$수식$$y = {p1} OVER {p2} x^2 {op1} {p3} x {op2} {p4}$$/수식$$의 그래프가 " \
           "지나는 사분면을 모두 고른 것은?\n" \
           "① 제$$수식$$1$$/수식$$, $$수식$$2$$/수식$$사분면\n" \
           "② 제$$수식$$1$$/수식$$, $$수식$$4$$/수식$$사분면\n" \
           "③ 제$$수식$$1$$/수식$$, $$수식$$2$$/수식$$, $$수식$$3$$/수식$$사분면\n" \
           "④ 제$$수식$$1$$/수식$$, $$수식$$2$$/수식$$, $$수식$$4$$/수식$$사분면\n" \
           "⑤ 모든 사분면을 지난다.\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = {p1} OVER {p2} x^2 {op1} {p3} x {op2} {p4}" \
              "= {p1} OVER {p2} LEFT ( x {op1} {p5} RIGHT ) ^2 {op3} {p6} OVER {p7}$$/수식$$\n" \
              "따라서 꼭짓점의 좌표가 $$수식$$LEFT ( {op4} {p5}$$/수식$$, $$수식$${op5} {p6} OVER {p7} RIGHT )$$/수식$$이고 " \
              "$$수식$$y$$/수식$$축과의 교점의 좌표가 $$수식$$LEFT ( 0$$/수식$$, $$수식$${op6} {p4} RIGHT )$$/수식$$이므로 {ss}사분면을 지난다.\n\n"

    op1, op4 = [['-', ''], ['+', '-']][np.random.randint(0, 2)]
    op2, op6 = [['+', ''], ['-', '-']][np.random.randint(0, 2)]
    while True:
        p1 = np.random.randint(1, 4)
        p2 = 2 * np.random.randint(1, 4)
        p3 = p1 * np.random.randint(1, 6)
        if GCD(p1, p2) == 1 and (p2*p3*p3) % (4*p1) != 0:
            break

    p4 = np.random.randint(1, 6)
    p5 = int((p2*p3)/(p1*2))
    if op2 == '+':
        p6 = 4*p1*p4 - p2*p3*p3
        p7 = 4*p1
        if p6 > 0:
            op3, op5 = ['+', '']
        else:
            op3, op5 = ['-', '-']
            p6 = -p6
    else:
        p6 = 4*p1*p4 + p2*p3*p3
        p7 = 4*p1
        op3, op5 = ['-', '-']
    gcd67 = GCD(p6, p7)
    p6 = int(p6 / gcd67)
    p7 = int(p7 / gcd67)

    if op3 == '+' and op2 == '+':
        s = answer_dict[0]
        ss = '제$$수식$$1$$/수식$$, $$수식$$2$$/수식$$'
    elif op3 == '-' and op2 == '-':
        s = answer_dict[4]
        ss = '모든 '
    elif op3 == '-' and op2 == '+':
        if op1 == '+':
            s = answer_dict[2]
            ss = '제$$수식$$1$$/수식$$, $$수식$$2$$/수식$$, $$수식$$3$$/수식$$'
        else:
            s = answer_dict[3]
            ss = '제$$수식$$1$$/수식$$, $$수식$$2$$/수식$$, $$수식$$4$$/수식$$'

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, op1=op1, op2=op2)
    answer = answer.format(s=s)
    comment = comment.format(op1=op1, op2=op2, op3=op3, op4=op4, op5=op5, op6=op6, ss=ss, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7)

    return stem, answer, comment





# 3-1-3-193
def quadequation313_Stem_151():
    stem = "다음 이차함수 중 그래프가 모든 사분면을 지나는 것은?\n" \
           "① $$수식$${c1}$$/수식$$ \t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n\n"

    p1 = np.random.randint(2, 5)
    p16 = np.random.randint(1, 4)
    p2 = 2*p1*p16
    p3 = np.random.randint(1, 4)
    p17 = p3 + p1*p16*p16

    while True:
        p18 = np.random.randint(1, 5)
        p5 = 2*p18
        p4 = np.random.randint(1, 4)
        p6 = int(2*p4*p18/p5)
        p7 = np.random.randint(1, 10)
        p20 = p5
        p19 = p18*(2*p7+p4*p18)
        gcd1920 = GCD(p19, p20)
        p19 = int(p19/gcd1920)
        p20 = int(p20/gcd1920)
        if p6 == 1:
            p6 = ''
        if p20 > 1 and GCD(p4, p5) == 1:
            break

    while True:
        p22 = 2
        p21 = np.random.randint(1, 6)
        p8 = int(2*p21/p22)
        p9 = np.random.randint(1, 6)
        p24 = p22*p22
        p23 = p21*p21 - p24*p9
        gcd2324 = GCD(p23, p24)
        p23 = int(p23/gcd2324)
        p24 = int(p24/gcd2324)
        if p8 == 1:
            p8 = ''
        if p24 > 1 and GCD(p21, p22) == 1 and p23 > 0:
            break

    while True:
        p26 = 2 * np.random.randint(1, 3)
        p25 = np.random.randint(1, 4)
        p10 = p26 * np.random.randint(1, 3)
        p11 = int(2*p10*p25/p26)
        p28 = int(p26*p26/2)
        p27 = 2 * np.random.randint(0, 2) + 1
        p12 = int((p10*p25*p25 + 2*p27)/(p26*p26))
        gcd2728 = GCD(p27, p28)
        p27 = int(p27/gcd2728)
        p28 = int(p28/gcd2728)
        if p11 == 1:
            p11 = ''
        if p28 > 1 and p10 != 1 and GCD(p25, p26) == 1 and (p10*p25*p25 + 2*p27) % (p26*p26) == 0:
            break

    while True:
        p30 = np.random.randint(2, 6)
        p29 = np.random.randint(1, 4)
        p13 = p30*p30
        p14 = p13
        p15 = p29*p29
        if GCD(p29, p30) == 1:
            break

    c1 = 'y = - {p1} x^2 + {p2} x - {p3}'.format(p1=p1, p2=p2, p3=p3)
    c2 = 'y = - {p4} OVER {p5} x^2 - {p6} x + {p7}'.format(p4=p4, p5=p5, p6=p6, p7=p7)
    c3 = 'y = x^2 - {p8} x + {p9}'.format(p8=p8, p9=p9)
    c4 = 'y = {p10} x^2 + {p11} x + {p12}'.format(p10=p10, p11=p11, p12=p12)
    c5 = 'y = {p13} x^2 - {p14} x + {p15}'.format(p13=p13, p14=p14, p15=p15)
    c_ans = c2

    s1 = '$$수식$$y = - {p1} x^2 + {p2} x - {p3} = - {p1} LEFT ( x - {p16} RIGHT ) ^2 - {p17}$$/수식$$\n' \
         '따라서 꼭짓점의 좌표가 $$수식$$LEFT ( {p16}$$/수식$$, $$수식$$- {p17} RIGHT )$$/수식$$이고 ' \
         '$$수식$$y$$/수식$$축과의 교점의 좌표가 $$수식$$LEFT ( 0$$/수식$$, $$수식$$- {p3} RIGHT )$$/수식$$이므로 ' \
         '제$$수식$$1$$/수식$$, $$수식$$2$$/수식$$사분면을 지나지 않는다.'.format(p1=p1, p2=p2, p3=p3, p16=p16, p17=p17)
    s2 = '$$수식$$y = - {p4} OVER {p5} x^2 - {p6} x + {p7} ' \
         '= - {p4} OVER {p5} LEFT ( x + {p18} RIGHT ) ^2 + {p19} OVER {p20}$$/수식$$\n' \
         '따라서 꼭짓점의 좌표가 $$수식$$LEFT ( - {p18}$$/수식$$, $$수식$${p19} OVER {p20} RIGHT )$$/수식$$이고 ' \
         '$$수식$$y$$/수식$$축과의 교점의 좌표가 $$수식$$LEFT ( 0$$/수식$$, $$수식$${p7} RIGHT )$$/수식$$이므로 ' \
         '모든 사분면을 지난다.'.format(p4=p4, p5=p5, p6=p6, p7=p7, p18=p18, p19=p19, p20=p20)
    s3 = '$$수식$$y = x^2 - {p8} x + {p9} = LEFT ( x - {p21} OVER {p22} RIGHT ) ^2 - {p23} OVER {p24}$$/수식$$\n' \
         '따라서 꼭짓점의 좌표가 $$수식$$LEFT ( {p21} OVER {p22}$$/수식$$, $$수식$$- {p23} OVER {p24} RIGHT )$$/수식$$이고 ' \
         '$$수식$$y$$/수식$$축과의 교점의 좌표가 $$수식$$LEFT ( 0$$/수식$$, $$수식$${p9} RIGHT )$$/수식$$이므로 ' \
         '제$$수식$$3$$/수식$$사분면을 지나지 않는다.'.format(p8=p8, p9=p9, p21=p21, p22=p22, p23=p23, p24=p24)
    s4 = '$$수식$$y = {p10} x^2 + {p11} x + {p12} ' \
         '= {p10} LEFT ( x + {p25} OVER {p26} RIGHT ) ^2 + {p27} OVER {p28}$$/수식$$\n' \
         '따라서 꼭짓점의 좌표가 $$수식$$LEFT ( - {p25} OVER {p26}$$/수식$$, $$수식$${p27} OVER {p28} RIGHT )$$/수식$$이고 ' \
         '$$수식$$y$$/수식$$축과의 교점의 좌표가 $$수식$$LEFT ( 0$$/수식$$, $$수식$${p12} RIGHT )$$/수식$$이므로 ' \
         '제$$수식$$3$$/수식$$, $$수식$$4$$/수식$$사분면을 지나지 않는다.'.format(p10=p10, p11=p11, p12=p12, p25=p25, p26=p26, p27=p27, p28=p28)
    s5 = '$$수식$$y = {p13} x^2 - {p14} x + {p15} = {p13} LEFT ( x - {p29} OVER {p30} RIGHT ) ^2$$/수식$$\n' \
         '따라서 꼭짓점의 좌표가 $$수식$$LEFT ( {p29} OVER {p30}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$이고 ' \
         '$$수식$$y$$/수식$$축과의 교점의 좌표가 $$수식$$LEFT ( 0$$/수식$$, $$수식$${p15} RIGHT )$$/수식$$이므로 ' \
         '제$$수식$$3$$/수식$$, $$수식$$4$$/수식$$사분면을 지나지 않는다.'.format(p13=p13, p14=p14, p15=p15, p29=p29, p30=p30)

    cs = [[c1, s1], [c2, s2], [c3, s3], [c4, s4], [c5, s5]]
    np.random.shuffle(cs)
    [c1, s1], [c2, s2], [c3, s3], [c4, s4], [c5, s5] = cs
    for i in range(0, len(cs)):
        if cs[i][0] == c_ans:
            s = answer_dict[i]
            break
    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)

    return stem, answer, comment





# 3-1-3-194
def quadequation313_Stem_152():
    stem = "다음 이차함수 중 그래프가 $$수식$$x$$/수식$$축과 서로 다른 두 점에서 만나는 것은?\n" \
           "① $$수식$${c1}$$/수식$$ \t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n\n"

    while True:
        p18 = np.random.randint(2, 6)
        p1 = p18 * np.random.randint(1, 3)
        p17 = np.random.randint(1, 6)
        p2 = int(2 * p1 * p17 / p18)
        p3 = p1*p17*p17
        p4 = p18*p18
        gcd34 = GCD(p3, p4)
        p3 = int(p3/gcd34)
        p4 = int(p4/gcd34)
        if p2 == 1:
            p2 = ''
        if p4 > 1 and GCD(p17, p18) == 1 and (p1*p17*p17) % (p18*p18) != 0:
            break

    p19 = np.random.randint(1, 6)
    p20 = np.random.randint(1, 10)
    p5 = 2 * p19
    p6 = p19*p19 + p20

    while True:
        p7 = np.random.randint(1, 5)
        p8 = np.random.randint(2, 6)
        p21 = p8 * np.random.randint(1, 4)
        p9 = int(2 * p21 * p7 / p8)
        p22 = np.random.randint(1, 10)
        p10 = int(p21*p21*p7/p8) + p22
        if p9 == 1:
            p9 == ''
        if GCD(p7, p8) == 1:
            break

    while True:
        p11 = np.random.randint(1, 4)
        p12 = np.random.randint(2, 5)
        p23 = np.random.randint(1, 5)
        p13 = 2 * p11 * p23
        p14 = p12
        gcd1314 = GCD(p13, p14)
        p13 = int(p13/gcd1314)
        p14 = int(p14/gcd1314)
        p15 = p11 * p23 * p23
        p16 = p12
        gcd1516 = GCD(p15, p16)
        p15 = int(p15/gcd1516)
        p16 = int(p16/gcd1516)
        if p14 > 1 and p16 > 1 and GCD(p11, p12) == 1 and GCD(p12, p23) == 1:
            break

    while True:
        p25 = 2
        p24 = np.random.randint(1, 6)
        p28 = int(2*p24/p25)
        p26 = p24*p24
        p27 = p25*p25
        if p28 == 1:
            p28 = ''
        if GCD(p24, p25) == 1:
            break

    c1 = 'y = {p1} x^2 - {p2} x + {p3} OVER {p4}'.format(p1=p1, p2=p2, p3=p3, p4=p4)
    c2 = 'y = x^2 - {p5} x + {p6}'.format(p5=p5, p6=p6)
    c3 = 'y = - {p7} OVER {p8} x^2 + {p9} x - {p10}'.format(p7=p7, p8=p8, p9=p9, p10=p10)
    c4 = 'y = - {p11} OVER {p12} x^2 + {p13} OVER {p14} x - {p15} OVER {p16}'.format(p11=p11, p12=p12, p13=p13, p14=p14, p15=p15, p16=p16)
    c5 = 'y = - x^2 - {p17} x'.format(p17=p28)
    c_ans = c5

    s1 = '$$수식$$y = {p1} x^2 - {p2} x + {p3} OVER {p4} = {p1} LEFT ( x - {p17} OVER {p18} RIGHT ) ^2$$/수식$$\n' \
         '따라서 이 그래프는 $$수식$$x$$/수식$$축과 한 점에서 만난다.'.format(p1=p1, p2=p2, p3=p3, p4=p4, p17=p17, p18=p18)
    s2 = '$$수식$$y = x^2 - {p5} x + {p6} = LEFT ( x - {p19} RIGHT ) ^2 + {p20}$$/수식$$\n' \
         '따라서 이 그래프는 $$수식$$x$$/수식$$축과 만나지 않는다.'.format(p5=p5, p6=p6, p19=p19, p20=p20)
    s3 = '$$수식$$y = - {p7} OVER {p8} x^2 + {p9} x - {p10} ' \
         '= - {p7} OVER {p8} LEFT ( x - {p21} RIGHT ) ^2 - {p22}$$/수식$$\n' \
         '따라서 이 그래프는 $$수식$$x$$/수식$$축과 만나지 않는다.'.format(p7=p7, p8=p8, p9=p9, p10=p10, p21=p21, p22=p22)
    s4 = '$$수식$$y = - {p11} OVER {p12} x^2 + {p13} OVER {p14} x - {p15} OVER {p16} ' \
         '= - {p11} OVER {p12} x^2 LEFT ( x - {p23} RIGHT ) ^2$$/수식$$\n' \
         '따라서 이 그래프는 $$수식$$x$$/수식$$축과 한 점에서 만난다.'.format(p11=p11, p12=p12, p13=p13, p14=p14, p15=p15, p16=p16, p23=p23)
    s5 = '$$수식$$y = - x^2 - {p28} x = - LEFT ( x + {p24} OVER {p25} RIGHT ) ^2 + {p26} OVER {p27}$$/수식$$\n' \
         '따라서 이 그래프는 $$수식$$x$$/수식$$축과 서로 다른 두 점에서 만난다.'.format(p28=p28, p24=p24, p25=p25, p26=p26, p27=p27)

    cs = [[c1, s1], [c2, s2], [c3, s3], [c4, s4], [c5, s5]]
    np.random.shuffle(cs)
    [c1, s1], [c2, s2], [c3, s3], [c4, s4], [c5, s5] = cs
    for i in range(0, len(cs)):
        if cs[i][0] == c_ans:
            s = answer_dict[i]
            break
    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)

    return stem, answer, comment





# 3-1-3-195
def quadequation313_Stem_153():
    stem = "다음 이차함수 중 그래프가 $$수식$$x$$/수식$$축과 만나지 않는 것은?\n" \
           "① $$수식$${c1}$$/수식$$ \t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n\n"

    while True:
        p1 = np.random.randint(2, 6)
        p13 = 2 * p1
        p12 = np.random.randint(1, 6)
        p2 = int(2*p1*p12/p13)
        p14 = p1*p12*p12
        p15 = p13*p13
        gcd1415 = GCD(p14, p15)
        p14 = int(p14/gcd1415)
        p15 = int(p15/gcd1415)
        if GCD(p12, p13) == 1:
            break

    p16 = 2 * np.random.randint(1, 3) + 1
    p17 = 2
    p3 = int(2 * p16 / p17)
    p19 = p17 * p17
    p18 = 2 * np.random.randint(0, 4) + 1
    p4 = int((p16 * p16 + p18) / (p17 * p17))

    p20 = np.random.randint(1, 9)
    p5 = 2*p20
    p6 = p20*p20

    p21 = np.random.randint(2, 7)
    p7 = 2 * p21
    p22 = np.random.randint(1, p21*p21)
    p8 = p21*p21 - p22

    p9 = np.random.randint(2, 5)
    p23 = np.random.randint(1, 7)
    p10 = 2*p9*p23
    p11 = p9*p23*p23

    c1 = 'y = {p1} x^2 + {p2} x'.format(p1=p1, p2=p2)
    c2 = 'y = x^2 - {p3} x + {p4}'.format(p3=p3, p4=p4)
    c3 = 'y = x^2 - {p5} x + {p6}'.format(p5=p5, p6=p6)
    c4 = 'y = - x^2 - {p7} x - {p8}'.format(p7=p7, p8=p8)
    c5 = 'y = - {p9} x^2 - {p10} x - {p11}'.format(p9=p9, p10=p10, p11=p11)
    c_ans = c2

    s1 = '$$수식$$y = {p1} x^2 + {p2} x = {p1} LEFT ( x + {p12} OVER {p13} RIGHT ) ^2 - {p14} OVER {p15}$$/수식$$\n' \
         '따라서 이 그래프는 $$수식$$x$$/수식$$축과 두 점에서 만난다.'.format(p1=p1, p2=p2, p12=p12, p13=p13, p14=p14, p15=p15)
    s2 = '$$수식$$y = x^2 - {p3} x + {p4} = LEFT ( x - {p16} OVER {p17} RIGHT ) ^2 + {p18} OVER {p19}$$/수식$$\n' \
         '따라서 이 그래프는 $$수식$$x$$/수식$$축과 만나지 않는다.'.format(p3=p3, p4=p4, p16=p16, p17=p17, p18=p18, p19=p19)
    s3 = '$$수식$$y = x^2 - {p5} x + {p6} = LEFT ( x - {p20} RIGHT ) ^2$$/수식$$\n' \
         '따라서 이 그래프는 $$수식$$x$$/수식$$축과 한 점에서 만난다.'.format(p5=p5, p6=p6, p20=p20)
    s4 = '$$수식$$y = - x^2 - {p7} x - {p8} = - LEFT ( x + {p21} RIGHT ) ^2 + {p22}$$/수식$$\n' \
         '따라서 이 그래프는 $$수식$$x$$/수식$$축과 두 점에서 만난다.'.format(p7=p7, p8=p8, p21=p21, p22=p22)
    s5 = '$$수식$$y = - {p9} x^2 - {p10} x - {p11} = - {p9} LEFT ( x + {p23} RIGHT ) ^2$$/수식$$\n' \
         '따라서 이 그래프는 $$수식$$x$$/수식$$축과 한 점에서 만난다.'.format(p9=p9, p10=p10, p11=p11, p23=p23)

    cs = [[c1, s1], [c2, s2], [c3, s3], [c4, s4], [c5, s5]]
    np.random.shuffle(cs)
    [c1, s1], [c2, s2], [c3, s3], [c4, s4], [c5, s5] = cs
    for i in range(0, len(cs)):
        if cs[i][0] == c_ans:
            s = answer_dict[i]
            break
    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)

    return stem, answer, comment





# 3-1-3-196
def quadequation313_Stem_154():
    stem = "이차함수 $$수식$$y = x^2 + {p1} x - {p2}$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$$b$$/수식$$만큼 평행이동 하면 " \
           "$$수식$$y = x^2 - {p3} x + {p4}$$/수식$$의 그래프와 일치한다. 이때 $$수식$$ab$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$ \t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = x^2 + {p1} x - {p2} = LEFT ( x + {p5} RIGHT ) ^2 - {p6}$$/수식$$의 그래프를 " \
              "$$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, $$수식$$y$$/수식$$축의 방향으로 $$수식$$b$$/수식$$만큼 " \
              "평행이동한 그래프의 식은\n" \
              "$$수식$$y = LEFT ( x - a + {p5} RIGHT ) ^2 - {p6} + b$$/수식$$\n이 그래프가 " \
              "$$수식$$y = x^2 - {p3} x + {p4} = LEFT ( x - {p7} RIGHT ) ^2 - {p8}$$/수식$$의 그래프와 일치하므로\n" \
              "$$수식$$- a + {p5} = - {p7}$$/수식$$, $$수식$$- {p6} + b = - {p8}$$/수식$$\n" \
              "따라서 $$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$이므로\n" \
              "$$수식$$ab = {ab}$$/수식$$\n\n"

    p5 = np.random.randint(1, 4)
    p6 = np.random.randint(p5*p5+1, p5*p5+5)
    p2 = p6 - p5*p5
    p1 = 2*p5
    p7 = np.random.randint(2, 6)
    p8 = np.random.randint(1, p7*p7)
    p4 = p7*p7 - p8
    p3 = 2*p7
    a = p5 + p7
    b = p6 - p8
    ab = a*b
    c = random.sample(list(range(ab-10, ab))+list(range(ab+1, ab+11)), 4)
    c.append(ab)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ab:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, a=a, b=b, ab=ab)

    return stem, answer, comment





# 3-1-3-197
def quadequation313_Stem_155():
    stem = "이차함수 $$수식$$y = - {p1} x^2 - {p2} x - {p3}$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$$b$$/수식$$만큼 평행이동 하면 " \
           "$$수식$$y = - {p1} x^2 - {p4} x - {p5}$$/수식$$의 그래프와 일치한다. 이때 $$수식$$a + b$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$ \t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = - {p1} x^2 - {p2} x - {p3} = - {p1} LEFT ( x + {p6} RIGHT ) ^2 - {p7}$$/수식$$의 그래프를 " \
              "$$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, $$수식$$y$$/수식$$축의 방향으로 $$수식$$b$$/수식$$만큼 " \
              "평행이동한 그래프의 식은\n" \
              "$$수식$$y = - {p1} LEFT ( x - a + {p6} RIGHT ) ^2 - {p7} + b$$/수식$$\n이 그래프가 " \
              "$$수식$$y = - {p1} x^2 - {p4} x - {p5} = - {p1} LEFT ( x + {p8} RIGHT ) ^2 + {p9}$$/수식$$의 그래프와 일치하므로\n" \
              "$$수식$$- a + {p6} = {p8}$$/수식$$, $$수식$$- {p7} + b = {p9}$$/수식$$\n" \
              "따라서 $$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$이므로\n" \
              "$$수식$$a + b = {ab}$$/수식$$\n\n"

    p1 = np.random.randint(2, 4)
    p6, p8 = random.sample(list(range(1, 5)), 2)
    p2 = 2*p1*p6
    p7 = np.random.randint(1, 10)
    p3 = p6*p6*p1 + p7
    p4 = 2*p1*p8
    p9 = np.random.randint(1, p1*p8*p8)
    p5 = p1*p8*p8 - p9
    a = p6 - p8
    b = p7 + p9
    ab = a + b
    c = random.sample(list(range(ab-5, ab))+list(range(ab+1, ab+6)), 4)
    c.append(ab)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ab:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, a=a, b=b, ab=ab)

    return stem, answer, comment





# 3-1-3-198
def quadequation313_Stem_156():
    stem = "이차함수 $$수식$$y = {p1} x^2 + {p2} x - {p3}$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$$b$$/수식$$만큼 평행이동 하면 " \
           "$$수식$$y = {p1} x^2 - {p4} x + {p5}$$/수식$$의 그래프와 일치한다. 이때 $$수식$$b OVER a$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${ab}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y = {p1} x^2 + {p2} x - {p3} = {p1} LEFT ( x + {p6} RIGHT ) ^2 - {p7}$$/수식$$의 그래프를 " \
              "$$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, $$수식$$y$$/수식$$축의 방향으로 $$수식$$b$$/수식$$만큼 " \
              "평행이동한 그래프의 식은\n" \
              "$$수식$$y = {p1} LEFT ( x - a + {p6} RIGHT ) ^2 - {p7} + b$$/수식$$\n이 그래프가 " \
              "$$수식$$y = {p1} x^2 - {p4} x + {p5} = {p1} LEFT ( x - {p8} RIGHT ) ^2 + {p9}$$/수식$$의 그래프와 일치하므로\n" \
              "$$수식$$- a + {p6} = - {p8}$$/수식$$, $$수식$$- {p7} + b = {p9}$$/수식$$\n" \
              "따라서 $$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$이므로\n" \
              "$$수식$$b OVER a = {ab}$$/수식$$\n\n"

    while True:
        p1 = np.random.randint(2, 4)
        p6, p8 = random.sample(list(range(1, 6)), 2)
        p2 = 2*p1*p6
        p4 = 2*p1*p8
        p3 = np.random.randint(1, 11)
        p7 = p3 + p1*p6*p6
        p9 = np.random.randint(1, 11)
        p5 = p1*p8*p8 + p9
        a = p6 + p8
        b = p7 + p9
        if b % a == 0:
            break
    ab = int(b / a)

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5)
    answer = answer.format(ab=ab)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, a=a, b=b, ab=ab)

    return stem, answer, comment





# 3-1-3-199
def quadequation313_Stem_157():
    stem = "이차함수 $$수식$$y = x^2 - {p1} x + {p2}$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$${op1}{a}$$/수식$$만큼, " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$${op2}{b}$$/수식$$만큼 평행이동한 그래프의 축의 방정식은?\n" \
           "① $$수식$$x = {c1}$$/수식$$ \t② $$수식$$x = {c2}$$/수식$$\n" \
           "③ $$수식$$x = {c3}$$/수식$$ \t④ $$수식$$x = {c4}$$/수식$$\n" \
           "⑤ $$수식$$x = {c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = x^2 - {p1} x + {p2} = LEFT ( x - {p3} RIGHT ) ^2 + {p4}$$/수식$$의 그래프를 " \
              "$$수식$$x$$/수식$$축의 방향으로 $$수식$${op1}{a}$$/수식$$만큼, $$수식$$y$$/수식$$축의 방향으로 $$수식$${op2}{b}$$/수식$$만큼 " \
              "평행이동한 그래프의 식은\n" \
              "$$수식$$y = LEFT ( x {op11} {a} - {p3} RIGHT ) ^2 + {p4} {op22} {b} = LEFT ( x - {p5} RIGHT ) ^2 + {p6}$$/수식$$\n" \
              "따라서 그래프의 축의 방정식은 $$수식$$x = {x}$$/수식$$\n\n"

    op1, op11 = [['', '-'], ['-', '+']][np.random.randint(0, 2)]
    op2, op22 = [['', '+'], ['-', '-']][np.random.randint(0, 2)]

    p35 = random.sample(list(range(1, 7)), 2)
    p35.sort()
    if op11 == '+':
        p5, p3 = p35
        a = p3 - p5
    else:
        p3, p5 = p35
        a = p5 - p3
    p46 = random.sample(list(range(1, 10)), 2)
    p46.sort()
    if op22 == '+':
        p4, p6 = p46
        b = p6 - p4
    else:
        p6, p4 = p46
        b = p4 - p6
    p1 = 2 * p3
    p2 = p3 * p3 + p4
    x = p5

    c = random.sample(list(range(x-5, x))+list(range(x+1, x+6)), 4)
    c.append(x)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == x:
            s = answer_dict[i]
            break

    stem = stem.format(op1=op1, op2=op2, p1=p1, p2=p2, a=a, b=b, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, a=a, b=b, op1=op1, op2=op2, op11=op11, op22=op22, x=x)

    return stem, answer, comment





# 3-1-3-200
def quadequation313_Stem_158():
    stem = "이차함수 $$수식$$y = {p1} OVER {p2} x^2$$/수식$$의 그래프를 꼭짓점의 좌표가 " \
           "$$수식$$LEFT ( {op1} {x}$$/수식$$, $$수식$${op2} {y} RIGHT )$$/수식$$이 되도록 평행이동하면 " \
           "$$수식$$y = ax^2 + bx + c$$/수식$$의 그래프와 일치할 때, " \
           "$$수식$${p2} a + b + c$$/수식$$의 값은? " \
           "$$수식$$LEFT ($$/수식$$단, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$는 상수이다.$$수식$$RIGHT )$$/수식$$\n" \
           "① $$수식$${c1}$$/수식$$ \t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "이차함수 $$수식$$y = {p1} OVER {p2} x^2$$/수식$$의 그래프를 꼭짓점의 좌표가 " \
              "$$수식$$LEFT ( {op1} {x}$$/수식$$, $$수식$${op2} {y} RIGHT )$$/수식$$이 되도록 평행이동하면\n" \
              "$$수식$$y = {p1} OVER {p2} LEFT ( x {op11} {x} RIGHT ) ^2 {op22} {y} " \
              "= {p1} OVER {p2} x^2 {op11} {b} x {op3} {c}$$/수식$$\n" \
              "따라서 $$수식$$a = {p1} OVER {p2}$$/수식$$, $$수식$$b = {op111} {b}$$/수식$$, $$수식$$c = {op33} {c}$$/수식$$이므로\n" \
              "$$수식$${p2} a + b + c = {ss}$$/수식$$\n\n"

    op1, op11, op111 = [['', '-', '-'], ['-', '+', '']][np.random.randint(0, 2)]
    op2, op22 = [['', '+'], ['-', '-']][np.random.randint(0, 2)]

    p1 = 2 * np.random.randint(0, 3) + 1
    p2 = 2 * np.random.randint(1, 3)
    x = p2 * np.random.randint(1, 4)
    y = np.random.randint(1, 10)
    b = int(x*p1/p2)

    if op22 == '+':
        c = int(x*x*p1/p2) + y
    else:
        c = int(x*x*p1/p2) - y

    ss = p1
    if c > 0:
        op3, op33 = '+', ''
        ss = ss + c
    else:
        op3, op33 = '-', '-'
        ss = ss - c
    if op111 == '-':
        ss = ss - b
    else:
        ss = ss + b

    if b == 1:
        b = ''

    cc = random.sample(list(range(ss-5, ss))+list(range(ss+1, ss+6)), 4)
    cc.append(ss)
    cc.sort()
    c1, c2, c3, c4, c5 = cc
    for i in range(0, len(cc)):
        if cc[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(op1=op1, op2=op2, x=x, y=y, p1=p1, p2=p2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, op1=op1, op2=op2, op11=op11, op22=op22, op3=op3, op33=op33, op111=op111, b=b, c=c, x=x, y=y, ss=ss)

    return stem, answer, comment





# 3-1-3-201
def quadequation313_Stem_159():
    stem = "이차함수 $$수식$$y = {p1} x^2 - {p2} x + {p3}$$/수식$$의 그래프를 " \
           "$$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, $$수식$$y$$/수식$$축의 방향으로 $$수식$${y}$$/수식$$만큼 " \
           "평행이동한 그래프의 꼭짓점의 좌표가 $$수식$$LEFT ( {x}$$/수식$$, $$수식$$b RIGHT )$$/수식$$일 때, " \
           "$$수식$$a + b$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$ \t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = {p1} x^2 - {p2} x + {p3} = {p1} LEFT ( x - {p4} OVER {p5} RIGHT ) ^2 - {p6}$$/수식$$의 그래프를 " \
              "$$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, $$수식$$y$$/수식$$축의 방향으로 $$수식$${y}$$/수식$$만큼 " \
              "평행이동한 그래프의 식은\n" \
              "$$수식$$y = {p1} LEFT ( x - a - {p4} OVER {p5} RIGHT ) ^2 - {p6} {op1} {y}" \
              "= {p1} LEFT ( x - a - {p4} OVER {p5} RIGHT ) ^2 - {p7}$$/수식$$\n" \
              "이 그래프의 꼭짓점의 좌표가 $$수식$$LEFT ( {x}$$/수식$$, $$수식$$b RIGHT )$$/수식$$이므로\n" \
              "$$수식$$a + {p4} OVER {p5} = {x}$$/수식$$, $$수식$$b = - {p7}$$/수식$$\n" \
              "따라서 $$수식$$a = - {p8} OVER {p9}$$/수식$$, $$수식$$b = - {p7}$$/수식$$이므로\n" \
              "$$수식$$a + b = - {p10} OVER {p11}$$/수식$$\n\n"

    while True:
        p4, p5 = [[1, 2], [3, 2], [1, 3], [2, 3], [4, 3], [5, 3]][np.random.randint(0, 6)]
        p1 = p5 * p5 * np.random.randint(1, 3)
        p2 = int(2*p1*p4/p5)
        if int(p1*p4*p4/(p5*p5)) <= 1:
            continue
        p3 = np.random.randint(1, int(p1*p4*p4/(p5*p5)))
        p6 = int(p1*p4*p4/(p5*p5)) - p3
        if p6 > 1:
            break
    y = random.sample(list(range(-5, 0))+list(range(1, p6)), 1)[0]
    p7 = p6 - y
    x = np.random.randint(-5, int(p4/p5))
    p8 = p4 - p5*x
    p9 = p5
    gcd89 = GCD(p8, p9)
    p8 = int(p8/gcd89)
    p9 = int(p9/gcd89)
    p10 = p8 + p7*p9
    p11 = p9
    gcd1011 = GCD(p10, p11)
    p10 = int(p10/gcd1011)
    p11 = int(p11/gcd1011)
    op1 = ''
    if y > 0:
        op1 = '+'

    ss = '- {t1} OVER {t2}'.format(t1=p10, t2=p11)
    c = [ss]
    c.append('- {t1} OVER {t2}'.format(t1=(p10+p11), t2=p11))
    c.append('- {t1} OVER {t2}'.format(t1=(p10+p11+p11), t2=p11))
    c.append('- {t1}'.format(t1=int(p10/p11)))
    c.append('- {t1}'.format(t1=(int(p10/p11)-1)))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(x=x, y=y, p1=p1, p2=p2, p3=p3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(x=x, y=y, op1=op1, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11)

    return stem, answer, comment





# 3-1-3-202
def quadequation313_Stem_160():
    stem = "이차함수 $$수식$$y = {p1} x^2 - {p2} x + {p3}$$/수식$$의 그래프를 " \
           "$$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, $$수식$$y$$/수식$$축의 방향으로 $$수식$${op2} {y}$$/수식$$만큼 " \
           "평행이동한 그래프의 꼭짓점의 좌표가 $$수식$$LEFT ( {op1} {x}$$/수식$$, $$수식$$b RIGHT )$$/수식$$일 때, " \
           "$$수식$$b OVER a$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${ab}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y = {p1} x^2 - {p2} x + {p3} = {p1} LEFT ( x - {p4} RIGHT ) ^2 - {p5}$$/수식$$의 그래프를 " \
              "$$수식$$x$$/수식$$축의 방향으로 $$수식$$a$$/수식$$만큼, $$수식$$y$$/수식$$축의 방향으로 $$수식$${op2} {y}$$/수식$$만큼 " \
              "평행이동한 그래프의 식은\n" \
              "$$수식$$y = {p1} LEFT ( x - a - {p4} RIGHT ) ^2 - {p5} {op22} {y}" \
              "= {p1} LEFT ( x - a - {p4} RIGHT ) ^2 - {p6}$$/수식$$\n" \
              "이 그래프의 꼭짓점의 좌표가 $$수식$$LEFT ( {op1} {x}$$/수식$$, $$수식$$b RIGHT )$$/수식$$이므로\n" \
              "$$수식$$a + {p4} = {op1} {x}$$/수식$$, $$수식$$b = - {p6}$$/수식$$\n" \
              "따라서 $$수식$$a = {p7}$$/수식$$, $$수식$$b = - {p6}$$/수식$$이므로\n" \
              "$$수식$$b OVER a = {op3} {p8}$$/수식$$\n\n"

    while True:
        op1 = ['', '-'][np.random.randint(0, 2)]
        op2, op22 = [['', '+'], ['-', '-']][np.random.randint(0, 2)]

        p1 = np.random.randint(2, 4)
        p4 = np.random.randint(2, 6)
        p5 = np.random.randint(5, p1*p4*p4)
        p3 = p1*p4*p4 - p5
        p2 = 2*p1*p4

        if op22 == '+':
            y = np.random.randint(1, p5)
            p6 = p5 - y
        else:
            y = np.random.randint(1, 8)
            p6 = p5 + y
        b = - p6

        x = np.random.randint(1, 8)
        if op1 == '-':
            a = - p4 - x
        else:
            a = - p4 + x

        if a > 0 and b % a == 0:
            break

    p7 = a
    p8 = int(b / a)
    ab = p8

    if b / a > 0:
        op3 = ''
    else:
        op3 = '-'
        p8 = - p8

    stem = stem.format(op1=op1, op2=op2, x=x, y=y, p1=p1, p2=p2, p3=p3)
    answer = answer.format(ab=ab)
    comment = comment.format(op1=op1, op2=op2, op22=op22, op3=op3, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, x=x, y=y)

    return stem, answer, comment





# 3-1-3-203
def quadequation313_Stem_161():
    stem = "이차함수 $$수식$$y = x^2 + {p1} x - {p2}$$/수식$$의 그래프를 " \
           "$$수식$$x$$/수식$$축의 방향으로 $$수식$${a}$$/수식$$만큼, $$수식$$y$$/수식$$축의 방향으로 $$수식$${b}$$/수식$$만큼 " \
           "평행이동한 그래프의 꼭짓점의 좌표는?\n" \
           "① $$수식$$LEFT ( {c1}$$/수식$$, $$수식$${c2} RIGHT )$$/수식$$\t" \
           "② $$수식$$LEFT ( {c3}$$/수식$$, $$수식$${c4} RIGHT )$$/수식$$\t" \
           "③ $$수식$$LEFT ( {c5}$$/수식$$, $$수식$${c6} RIGHT )$$/수식$$\n" \
           "④ $$수식$$LEFT ( {c7}$$/수식$$, $$수식$${c8} RIGHT )$$/수식$$\t" \
           "⑤ $$수식$$LEFT ( {c9}$$/수식$$, $$수식$${c10} RIGHT )$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = x^2 + {p1} x - {p2} = LEFT ( x + {p3} RIGHT ) ^2 - {p4}$$/수식$$\n" \
              "이 함수의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$${a}$$/수식$$만큼, " \
              "$$수식$$y$$/수식$$축의 방향으로 $$수식$${b}$$/수식$$만큼 평행이동한 그래프의 식은\n" \
              "$$수식$$y = LEFT ( x + {p3} {op1} {ma} RIGHT ) ^2 - {p4} {op2} {b}$$/수식$$\n" \
              "$$수식$$THEREFORE~ y = LEFT ( x {op3} {p5} RIGHT ) ^2 {op4} {p6}$$/수식$$\n" \
              "따라서 꼭짓점의 좌표는 $$수식$$LEFT ( {p7}$$/수식$$, $$수식$${p8} RIGHT )$$/수식$$\n\n"

    while True:
        p2 = np.random.randint(1, 6)
        p3 = np.random.randint(1, 6)
        p4 = p2 + p3*p3
        p1 = 2*p3

        a, b = random.sample(list(range(-6, 0))+list(range(1, 7)), 2)
        op3, op4 = '', ''
        p5 = p3 - a
        p6 = - p4 + b
        if p5 != 0 and p6 != 0 and p5 != p6:
            break
    if p5 > 0:
        op3 = '+'
    if p6 > 0:
        op4 = '+'
    ma = -a
    if ma > 0:
        op1 = '+'
    else:
        op1 = ''
    if b > 0:
        op2 = '+'
    else:
        op2 = ''
    p7 = -p5
    p8 = p6

    c = [[p7, p8], [-p7, p8], [p7, -p8], [-p7, -p8], [p8, p7]]
    c.sort()
    [[c1, c2], [c3, c4], [c5, c6], [c7, c8], [c9, c10]] = c
    for i in range(0, len(c)):
        if c[i] == [p7, p8]:
            s = answer_dict[i]
            break

    stem = stem.format(a=a, b=b, p1=p1, p2=p2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10)
    answer = answer.format(s=s)
    comment = comment.format(a=a, b=b, ma=ma, op1=op1, op2=op2, op3=op3, op4=op4, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8)

    return stem, answer, comment





# 3-1-3-204
def quadequation313_Stem_162():
    stem = "이차함수 $$수식$$y = - {p1} OVER {p2} x^2 - {p3} x - {p4}$$/수식$$의 그래프를 " \
           "$$수식$$x$$/수식$$축의 방향으로 $$수식$${a}$$/수식$$만큼 평행이동한 그래프가 " \
           "점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$$m RIGHT )$$/수식$$을 지날 때, $$수식$$m$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$ \t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = - {p1} OVER {p2} x^2 - {p3} x - {p4} " \
              "= - {p1} OVER {p2} LEFT ( x + {p5} RIGHT ) ^2 + {p6} OVER {p7}$$/수식$$의 그래프를 " \
              "$$수식$$x$$/수식$$축의 방향으로 $$수식$${a}$$/수식$$만큼 평행이동한 그래프의 식은\n" \
              "$$수식$$y = - {p1} OVER {p2} LEFT ( x {op1} {ma} + {p5} RIGHT ) ^2 + {p6} OVER {p7}$$/수식$$\n" \
              "$$수식$$  = - {p1} OVER {p2} LEFT ( x {op2} {p8} RIGHT ) ^2 + {p6} OVER {p7}$$/수식$$\n" \
              "이 그래프가 점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$$m RIGHT )$$/수식$$을 지나므로\n" \
              "$$수식$$m = - {p1} OVER {p2} TIMES {p9}^2 + {p6} OVER {p7} = {op3} {p10} OVER {p11}$$/수식$$\n\n"

    a = random.sample(list(range(-7, 0))+list(range(1, 8)), 1)[0]
    ma = -a
    if ma > 0:
        op1 = '+'
    else:
        op1 = ''

    while True:
        p2 = 2
        p1 = 2 * np.random.randint(0, 2) + 1
        p5 = 2 * np.random.randint(0, 3) + 1
        p3 = int(2*p5*p1/p2)
        p7 = p2
        p4 = np.random.randint(1, 8)
        p6 = p1*p5*p5 - 2*p4
        p8 = p5 - a
        if p8 > 0:
            x1 = np.random.randint(-p8-10, p8+2)
        else:
            x1 = np.random.randint(p8-2, -p8+10)
        p9 = x1 + p8
        p11 = p2
        p10 = p6 - p1 * p9 * p9
        if p8 != 0 and p6 > 0 and x1 != 0 and p9 > 0 and p10 != 0 and GCD(p10, p11) == 1:
            break

    if p8 > 0:
        op2 = '+'
    else:
        op2 = ''

    op3 = ''
    if p10 < 0:
        op3 = '-'
        p10 = -p10

    ss = '{op3} {t1} OVER {t2}'.format(op3=op3, t1=p10, t2=p11)
    c = random.sample(list(range(int(p10/p11)-5, int(p10/p11)+5)), 3)
    c.append(ss)
    c.append('{op3} {t1} OVER {t2}'.format(op3=op3, t1=(p10+p11), t2=p11))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(x1=x1, a=a, p1=p1, p2=p2, p3=p3, p4=p4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(x1=x1, a=a, ma=ma, op1=op1, op2=op2, op3=op3, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11)

    return stem, answer, comment





# 3-1-3-205
def quadequation313_Stem_163():
    stem = "이차함수 $$수식$$y = - x^2 + {p1} x + k$$/수식$$의 그래프를 " \
           "$$수식$$y$$/수식$$축의 방향으로 $$수식$${b}$$/수식$$만큼 평행이동하였더니 " \
           "$$수식$$x$$/수식$$축과 만나지 않았다. 이때 상수 $$수식$$k$$/수식$$의 값의 범위는?\n" \
           "① $$수식$$k &lt; {c1}$$/수식$$ \t② $$수식$$k &lt; {c2}$$/수식$$\n" \
           "③ $$수식$$k &lt; {c3}$$/수식$$ \t④ $$수식$$k &lt; {c4}$$/수식$$\n" \
           "⑤ $$수식$$k &lt; {c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = - x^2 + {p1} x + k = - LEFT ( x - {p2} RIGHT ) ^2 + k + {p3}$$/수식$$의 그래프를 " \
              "$$수식$$y$$/수식$$축의 방향으로 $$수식$${b}$$/수식$$만큼 평행이동한 그래프의 식은\n" \
              "$$수식$$y = - LEFT ( x - {p2} RIGHT ) ^2 + k + {p3} {op1} {b}$$/수식$$\n" \
              "$$수식$$  = - LEFT ( x - {p2} RIGHT ) ^2 + k {op2} {p4}$$/수식$$\n" \
              "이 그래프의 꼭짓점의 좌표는 $$수식$$LEFT ( {p2}$$/수식$$, $$수식$$k {op2} {p4} RIGHT )$$/수식$$이므로 " \
              "$$수식$$x$$/수식$$축과 만나지 않으려면\n" \
              "$$수식$$k {op2} {p4} &lt; 0$$/수식$$\t\t$$수식$$THEREFORE~ k &lt; {p5}$$/수식$$\n\n"

    while True:
        p2 = np.random.randint(1, 5)
        p1 = 2*p2
        p3 = p2*p2
        b = random.sample(list(range(-9, 0))+list(range(1, 5)), 1)[0]
        p4 = p3 + b
        p5 = -p4
        if b != 0 and p4 != 0:
            break

    op1, op2 = '', ''
    if b > 0:
        op1 = '+'
    if p4 > 0:
        op2 = '+'

    c = random.sample(list(range(p5-5, p5))+list(range(p5+1, p5+6)), 4)
    c.append(p5)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == p5:
            s = answer_dict[i]
            break

    stem = stem.format(b=b, p1=p1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(b=b, op1=op1, op2=op2, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5)

    return stem, answer, comment





# 3-1-3-208
def quadequation313_Stem_164():
    stem = "이차함수 $$수식$$y = - {p1} x^2 - {p2} x - {p3}$$/수식$$의 그래프에서 " \
           "$$수식$$x$$/수식$$의 값이 증가할 때 $$수식$$y$$/수식$$의 값{menu}하는 " \
           "$$수식$$x$$/수식$$의 값의 범위는?\n" \
           "① $$수식$${c1}$$/수식$$ \t\t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t\t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = - {p1} x^2 - {p2} x - {p3} = - {p1} LEFT ( x + {p4} RIGHT ) ^2 - {p5}$$/수식$$이므로 " \
              "구하는 범위는\n$$수식$$x {op1} {p6}$$/수식$$\n\n"

    pick = np.random.randint(0, 2)
    menu, op1, op2 = [['은 감소', '&gt;', '&lt;'], ['도 증가', '&lt;', '&gt;']][pick]

    p1 = np.random.randint(2, 4)
    p4 = np.random.randint(1, 4)
    p2 = 2*p1*p4
    p5 = np.random.randint(1, 7)
    p3 = p1*p4*p4 + p5
    p6 = -p4

    ss = 'x {op} {num}'.format(op=op1, num=p6)
    c = [ss]
    if pick == 0:
        c.append('x {op} {num}'.format(op=op2, num=p6))
        c.append('x {op} {num}'.format(op=op1, num=(p6-1)))
        c.append('x {op} {num}'.format(op=op2, num=(p6-1)))
        c.append('x {op} {num}'.format(op=op1, num=(p6-2)))
    else:
        c.append('x {op} {num}'.format(op=op2, num=p6))
        c.append('x {op} {num}'.format(op=op1, num=(p6 + 1)))
        c.append('x {op} {num}'.format(op=op2, num=(p6 + 1)))
        c.append('x {op} {num}'.format(op=op1, num=(p6 + 2)))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(menu=menu, p1=p1, p2=p2, p3=p3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(op1=op1, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6)

    return stem, answer, comment





# 3-1-3-209
def quadequation313_Stem_165():
    stem = "이차함수 $$수식$$y = - {p1} OVER {p2} x^2 + {p3} x - {p4}$$/수식$$의 그래프에서 " \
           "$$수식$$x$$/수식$$의 값이 증가할 때 $$수식$$y$$/수식$$의 값{menu}하는 " \
           "$$수식$$x$$/수식$$의 값의 범위는?\n" \
           "① $$수식$${c1}$$/수식$$ \t\t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t\t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = - {p1} OVER {p2} x^2 + {p3} x - {p4} " \
              "= - {p1} OVER {p2} LEFT ( x - {p5} RIGHT ) ^2 - {p6} OVER {p7}$$/수식$$\n" \
              "이 함수의 그래프는 위로 볼록하고 축의 방정식은 $$수식$$x = {p5}$$/수식$$이다.\n" \
              "따라서 $$수식$$x {op1} {p5}$$/수식$$일 때, $$수식$$x$$/수식$$의 값이 증가하면 " \
              "$$수식$$y$$/수식$$의 값{menu}한다.\n\n"

    pick = np.random.randint(0, 2)
    menu, op1, op2 = [['은 감소', '&gt;', '&lt;'], ['도 증가', '&lt;', '&gt;']][pick]

    while True:
        p1 = 2 * np.random.randint(0, 3) + 1
        p2 = 2
        p5 = 2 * np.random.randint(0, 3) + 1
        p3 = int(2*p5*p1/p2)
        p4 = np.random.randint(int(p1*p5*p5/p2)+1, int(p1*p5*p5/p2)+4)
        p7 = p2
        p6 = p2*p4 - p1*p5*p5
        if GCD(p1, p2) == 1:
            break

    ss = 'x {op} {num}'.format(op=op1, num=p5)
    c = [ss]
    if pick == 0:
        c.append('x {op} {num}'.format(op=op2, num=p5))
        c.append('x {op} {num}'.format(op=op2, num=-p5))
        c.append('x {op} {num}'.format(op=op1, num=(p5-1)))
        c.append('x {op} {num}'.format(op=op2, num=(p5-1)))
    else:
        c.append('x {op} {num}'.format(op=op2, num=p5))
        c.append('x {op} {num}'.format(op=op2, num=-p5))
        c.append('x {op} {num}'.format(op=op1, num=(p5+1)))
        c.append('x {op} {num}'.format(op=op2, num=(p5+1)))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(menu=menu, p1=p1, p2=p2, p3=p3, p4=p4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(op1=op1, menu=menu, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7)

    return stem, answer, comment





# 3-1-3-210
def quadequation313_Stem_166():
    stem = "이차함수 $$수식$$y = - {p1} OVER {p2} x^2 + {p3} OVER {p4} ax - {p5}$$/수식$$의 그래프에서 " \
           "$$수식$$x &lt; {p6}$$/수식$$이면 $$수식$$x$$/수식$$의 값이 증가할 때 $$수식$$y$$/수식$$의 값도 증가하고, " \
           "$$수식$$x &gt; {p6}$$/수식$$이면 $$수식$$x$$/수식$$의 값이 증가할 때 $$수식$$y$$/수식$$의 값은 감소한다. " \
           "이 때 상수 $$수식$$a$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$ \t\t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t\t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = - {p1} OVER {p2} x^2 + {p3} OVER {p4} ax - {p5}$$/수식$$\n" \
              "$$수식$$  = - {p1} OVER {p2} LEFT ( x - {p7} a RIGHT ) ^2 + {p8} OVER {p9} a^2 - {p5}$$/수식$$\n" \
              "이 때 축의 방정식이 $$수식$$x = {p6}$$/수식$$이므로 $$수식$$a = {a}$$/수식$$\n\n"

    p1 = 1
    p2 = 2 * np.random.randint(1, 3) + 1
    p7 = [1, 2, 4][np.random.randint(0, 3)]
    p4 = p2
    a = np.random.randint(-6, 7)
    p3 = 2*p1*p7
    p9 = p2
    p8 = p1*p7*p7
    p6 = p7 * a
    p5 = np.random.randint(1, 6)

    if p7 == 1:
        p7 = ''

    c = random.sample(list(range(a-5, a))+list(range(a+1, a+6)), 4)
    c.append(a)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == a:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(a=a, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9)

    return stem, answer, comment





# 3-1-3-211
def quadequation313_Stem_167():
    stem = "이차함수 $$수식$$y = - {p1} x^2 + kx + {p2}$$/수식$$의 그래프가 " \
           "점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$를 지난다. 이 그래프에서 " \
           "$$수식$$x$$/수식$$의 값이 증가할 때, $$수식$$y$$/수식$$의 값{menu}하는 $$수식$$x$$/수식$$의 값의 범위는? " \
           "$$수식$$LEFT ($$/수식$$단, $$수식$$k$$/수식$$는 상수이다.$$수식$$RIGHT )$$/수식$$\n" \
           "① $$수식$${c1}$$/수식$$ \t\t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t\t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = - {p1} x^2 + kx + {p2}$$/수식$$의 그래프가 " \
              "점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$${y1} = - {p3} {op} {x1} k + {p2}$$/수식$$, $$수식$${x1} k = {p4}$$/수식$$" \
              "\t\t$$수식$$THEREFORE~ k = {p5}$$/수식$$\n" \
              "즉, $$수식$$y = - {p1} x^2 + {p6} x + {p2} = - {p1} LEFT ( x - {p7} RIGHT ) ^2 + {p8}$$/수식$$의 " \
              "그래프는 위로 볼록하고 축의 방정식은 $$수식$$x = {p7}$$/수식$$이다.\n" \
              "따라서 $$수식$$x {op1} {p7}$$/수식$$일 때, $$수식$$x$$/수식$$의 값이 증가하면 " \
              "$$수식$$y$$/수식$$의 값{menu}한다.\n\n"

    p1 = np.random.randint(1, 4)
    p2 = np.random.randint(1, 7)
    p7 = np.random.randint(1, 4)
    p8 = p2 + p1 * p7 * p7
    p6 = 2 * p1 * p7
    p5 = p6
    x1 = random.sample(list(range(-4, -1))+list(range(2, 5)), 1)[0]
    p3 = p1 * x1 * x1
    y1 = x1 * p5 - p3 + p2
    p4 = y1 + p3 - p2

    op = ''
    if x1 > 0:
        op = '+'

    if p1 == 1:
        p1 = ''

    pick = np.random.randint(0, 2)
    menu, op1, op2 = [['은 감소', '&gt;', '&lt;'], ['도 증가', '&lt;', '&gt;']][pick]

    ss = 'x {op} {num}'.format(op=op1, num=p7)
    c = [ss]
    if pick == 0:
        c.append('x {op} {num}'.format(op=op2, num=p7))
        c.append('x {op} {num}'.format(op=op1, num=-p7))
        c.append('x {op} {num}'.format(op=op1, num=(p7+1)))
        c.append('x {op} {num}'.format(op=op2, num=(p7+1)))
    else:
        c.append('x {op} {num}'.format(op=op2, num=p7))
        c.append('x {op} {num}'.format(op=op1, num=-p7))
        c.append('x {op} {num}'.format(op=op1, num=(p7-1)))
        c.append('x {op} {num}'.format(op=op2, num=(p7-1)))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(menu=menu, x1=x1, y1=y1, p1=p1, p2=p2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(op=op, x1=x1, y1=y1, op1=op1, menu=menu, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8)

    return stem, answer, comment





# 3-1-3-212
def quadequation313_Stem_168():
    stem = "이차함수 $$수식$$y = {p1} x^2 - {p2} x + {p3}$$/수식$$의 그래프를 " \
           "$$수식$$x$$/수식$$축의 방향으로 $$수식$$k$$/수식$$만큼 평행이동하면 " \
           "$$수식$$x$$/수식$$의 값이 증가할 때 $$수식$$y$$/수식$$의 값{menu}하는 " \
           "$$수식$$x$$/수식$$의 값의 범위는 $$수식$$x {op1} {p4}$$/수식$$이다. " \
           "이 때 $$수식$$k$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$ \t\t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t\t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = {p1} x^2 - {p2} x + {p3} = {p1} LEFT ( x - {p5} RIGHT ) ^2 - {p6}$$/수식$$의 그래프를 " \
              "$$수식$$x$$/수식$$축의 방향으로 $$수식$$k$$/수식$$만큼 평행이동한 그래프의 식은\n" \
              "$$수식$$y = {p1} LEFT ( x - k - {p5} RIGHT ) ^2 - {p6}$$/수식$$\n" \
              "이 때 축의 방정식이 $$수식$$x = k + {p5}$$/수식$$이므로\n" \
              "$$수식$$k + {p5} = {p4}\t\tTHEREFORE~ k = {k}$$/수식$$\n\n"

    pick = np.random.randint(0, 2)
    menu, op1 = [['도 증가', '&gt;'], ['는 감소', '&lt;']][pick]

    p4, p5 = random.sample(list(range(2, 6)), 2)
    k = p4 - p5
    p1 = np.random.randint(2, 4)
    p6 = np.random.randint(1, p1*p5*p5)
    p3 = p1*p5*p5 - p6
    p2 = 2 * p1 * p5

    c = random.sample(list(range(k-5, k))+list(range(k+1, 6)), 4)
    c.append(k)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == k:
            s = answer_dict[i]
            break

    stem = stem.format(menu=menu, op1=op1, p1=p1, p2=p2, p3=p3, p4=p4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(k=k, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6)

    return stem, answer, comment





# 3-1-3-213
def quadequation313_Stem_169():
    stem = "점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$를 지나는 " \
           "이차함수 $$수식$$y = {p1} x^2 + kx + {p2}$$/수식$$의 그래프에서 " \
           "$$수식$$x$$/수식$$의 값이 증가할 때 $$수식$$y$$/수식$$의 값{menu}하는 $$수식$$x$$/수식$$의 값의 범위는? " \
           "$$수식$$LEFT ($$/수식$$단, $$수식$$k$$/수식$$는 상수이다.$$수식$$RIGHT )$$/수식$$\n" \
           "① $$수식$${c1}$$/수식$$ \t\t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t\t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = {p1} x^2 + kx + {p2}$$/수식$$의 그래프가 " \
              "점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$${y1} = {p3} {op} {x1} k + {p2}$$/수식$$\t\t$$수식$$THEREFORE~ k = {p4}$$/수식$$\n" \
              "따라서 $$수식$$y = {p1} x^2 + {p4} x + {p2} = {p1} LEFT ( x + {p5} RIGHT ) ^2 - {p6}$$/수식$$이므로 " \
              "구하는 범위는\n$$수식$$x {op1} {p7}$$/수식$$\n\n"

    p1 = np.random.randint(2, 4)
    p5 = np.random.randint(1, 4)
    p6 = np.random.randint(1, p1*p5*p5)
    p2 = p1*p5*p5 - p6
    p4 = 2*p1*p5
    x1 = random.sample(list(range(-4, 0)) + list(range(1, 4)), 1)[0]
    p3 = p1*x1*x1
    y1 = p3 + x1*p4 + p2
    p7 = -p5
    op = ''
    if x1 > 0:
        op = '+'
    if x1 == 1:
        x1 = ''
    elif x1 == -1:
        x1 = '-'

    pick = np.random.randint(0, 2)
    menu, op1, op2 = [['은 감소', '&lt;', '&gt;'], ['도 증가', '&gt;', '&lt;']][pick]

    ss = 'x {op} {num}'.format(op=op1, num=p7)
    c = [ss]
    if pick == 0:
        c.append('x {op} {num}'.format(op=op2, num=p7))
        c.append('x {op} {num}'.format(op=op1, num=-p7))
        c.append('x {op} {num}'.format(op=op1, num=(p7+1)))
        c.append('x {op} {num}'.format(op=op2, num=(p7+1)))
    else:
        c.append('x {op} {num}'.format(op=op2, num=p7))
        c.append('x {op} {num}'.format(op=op1, num=-p7))
        c.append('x {op} {num}'.format(op=op1, num=(p7-1)))
        c.append('x {op} {num}'.format(op=op2, num=(p7-1)))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(menu=menu, x1=x1, y1=y1, p1=p1, p2=p2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(op=op, x1=x1, y1=y1, op1=op1, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7)

    return stem, answer, comment





# 3-1-3-215
def quadequation313_Stem_170():
    stem = "이차함수 $$수식$$y = {p1} OVER {p2} x^2 + {p3} OVER {p4} mx + {p5} m - {p6}$$/수식$$의 그래프에서 " \
           "$$수식$$x &lt; {p12}$$/수식$$이면 $$수식$$x$$/수식$$의 값이 증가할 때 $$수식$$y$$/수식$$의 값도 감소하고, " \
           "$$수식$$x &gt; {p12}$$/수식$$이면 $$수식$$x$$/수식$$의 값이 증가할 때 $$수식$$y$$/수식$$의 값은 증가할 때 " \
           "그래프의 꼭짓점의 좌표는?\n" \
           "① $$수식$${c1}$$/수식$$ \t\t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$ \t\t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = {p1} OVER {p2} x^2 + {p3} OVER {p4} mx + {p5} m - {p6}$$/수식$$에서\n" \
              "$$수식$$y = {p1} OVER {p2} LEFT ( x + {p7} m RIGHT ) ^2 - {p8} OVER {p9} m^2 + {p5} m - {p6}$$/수식$$\n" \
              "이 그래프의 축의 방정식이 $$수식$$x = {p12}$$/수식$$이므로 $$수식$$m = {m}$$/수식$$\n" \
              "따라서 $$수식$$- {p8} OVER {p9} m^2 + {p5} m - {p6} = {p10} OVER {p11}$$/수식$$이므로 " \
              "구하는 꼭짓점의 좌표는 $$수식$$LEFT ( {p12}$$/수식$$, $$수식$${p10} OVER {p11} RIGHT )$$/수식$$\n\n"

    while True:
        p1 = np.random.randint(1, 3)
        p2 = 2 * np.random.randint(1, 3) + 1
        p7 = [1, 2, 4][np.random.randint(0, 3)]
        p4 = p2
        p3 = 2*p1*p7
        m = [-1, 1, 2, -2, 4][np.random.randint(0, 5)]
        p12 = -p7 * m
        p9 = p2
        p8 = p1*p7*p7
        p5 = np.random.randint(2, 4)
        p6 = np.random.randint(1, 4)
        p11 = p9
        p10 = -p8 * m * m + p5 * p9 * m - p6 * p9
        if p10 > 0 and p10 % p11 != 0:
            break

    gcd1011 = GCD(p10, p11)
    p10 = int(p10/gcd1011)
    p11 = int(p11/gcd1011)
    if p7 == 1:
        p7 = ''

    ss = '$$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} OVER {y2} RIGHT )$$/수식$$'.format(x1=p12, y1=p10, y2=p11)
    c = [ss]
    c.append('$$수식$$LEFT ( {x1}$$/수식$$, $$수식$$- {y1} OVER {y2} RIGHT )$$/수식$$'.format(x1=p12, y1=p10, y2=p11))
    c.append('$$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} OVER {y2} RIGHT )$$/수식$$'.format(x1=-p12, y1=p10, y2=p11))
    c.append('$$수식$$LEFT ( {x1}$$/수식$$, $$수식$$- {y1} OVER {y2} RIGHT )$$/수식$$'.format(x1=-p12, y1=p10, y2=p11))
    c.append('$$수식$$LEFT ( {y1} OVER {y2}$$/수식$$, $$수식$${x1} RIGHT )$$/수식$$'.format(x1=p12, y1=p10, y2=p11))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p12=p12, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(m=m, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12)

    return stem, answer, comment





# 3-1-3-216
def quadequation313_Stem_171():
    stem = "이차함수 $$수식$$y = - x^2 + {p1} x + {p2}$$/수식$$의 그래프에 대한 설명으로 옳지 않은 것은?\n" \
           "① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = - x^2 + {p1} x + {p2} = - LEFT (x - {p3} RIGHT ) ^2 + {p4}$$/수식$$\n" \
              "{s} {explain}\n\n"

    op, menu = [['&gt;', '은 감소한다'], ['&lt;', '도 증가한다']][np.random.randint(0, 2)]

    while True:
        p3 = np.random.randint(1, 4)
        p1 = 2*p3
        p2 = np.random.randint(2, 6)
        p4 = p2 + p3*p3
        a = p3
        b = p4
        x1 = p3
        x3 = p4
        x2 = np.random.randint(2, x3)
        if is_prime(x3) and is_prime(x2):
            break

    c = ['모든 사분면을 지난다.',
         '함숫값의 범위는 $$수식$$y LEQ {b}$$/수식$$이다.'.format(b=b),
         '꼭짓점의 좌표는 $$수식$$LEFT ( {a}$$/수식$$, $$수식$${b} RIGHT )$$/수식$$이다.'.format(a=a, b=b),
         '$$수식$$x$$/수식$$축과의 교점의 좌표는 $$수식$$LEFT ( {x1} - SQRT {x2} $$/수식$$, $$수식$$0 RIGHT )$$/수식$$, '
         '$$수식$$LEFT ( {x1} + SQRT {x2}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$이다.'.format(x1=x1, x2=x2),
         '$$수식$$x {op} {a}$$/수식$$일 때, $$수식$$x$$/수식$$의 값이 증가하면 $$수식$$y$$/수식$$의 값{menu}.'.format(op=op, a=a, menu=menu)]
    ss = '$$수식$$x$$/수식$$축과의 교점의 좌표는 $$수식$$LEFT ( {x1} - SQRT {x2} $$/수식$$, $$수식$$0 RIGHT )$$/수식$$, ' \
         '$$수식$$LEFT ( {x1} + SQRT {x2}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$이다.'.format(x1=x1, x2=x2)
    explain = '$$수식$$- x^2 + {p1} x + {p2} = 0$$/수식$$에서 $$수식$$x^2 - {p1} x - {p2} = 0$$/수식$$\n' \
              '근의 공식에 의해 $$수식$$x = {x1} PLUSMINUS SQRT {x3}$$/수식$$이므로 $$수식$$x$$/수식$$축과의 교점의 좌표는 ' \
              '$$수식$$LEFT ( {x1} - SQRT {x3}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$, ' \
              '$$수식$$LEFT ( {x1} + SQRT {x3}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$이다.'.format(x1=x1, x3=x3, p1=p1, p2=p2)
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(s=s, explain=explain, p1=p1, p2=p2, p3=p3, p4=p4)

    return stem, answer, comment





# 3-1-3-217
def quadequation313_Stem_172():
    stem = "이차함수 $$수식$$y = - {p1} x^2 + {p2} x - {p3}$$/수식$$의 그래프에 대한 설명으로 옳은 것은?\n" \
           "① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = - {p1} x^2 + {p2} x - {p3} = - {p1} LEFT ( x - {p4} RIGHT ) ^2 + {p5}$$/수식$$\n" \
              "{n1} {ex1}\n" \
              "{n2} {ex2}\n" \
              "{n3} {ex3}\n" \
              "{n4} {ex4}\n\n"

    p1 = np.random.randint(2, 5)
    p4 = np.random.randint(1, 4)
    p2 = 2 * p1 * p4
    p3 = np.random.randint(1, p1*p4*p4)
    p5 = p1*p4*p4 - p3

    x = - p4
    op, menu1, menu2 = [['&lt;', '는 감소한다', '도 증가한다'], ['&gt;', '도 증가한다', '는 감소한다']][np.random.randint(0, 2)]

    cs = [['축의 방정식은 $$수식$$x = {x}$$/수식$$이다.'.format(x=x),
           '축의 방정식은 $$수식$$x = {p4}$$/수식$$이다.'.format(p4=p4)],
          ['$$수식$$y = {p1} x^2 - {p2} x + {p3}$$/수식$$의 그래프와 $$수식$$y$$/수식$$축에 대하여 대칭이다.'.format(p1=p1, p2=p2, p3=p3),
           '$$수식$$y = {p1} x^2 - {p2} x + {p3}$$/수식$$의 그래프와 $$수식$$x$$/수식$$축에 대하여 대칭이다.'.format(p1=p1, p2=p2, p3=p3)],
          ['위로 볼록하고, 대칭축은 $$수식$$y$$/수식$$축의 왼쪽에 위치한다.',
           '위로 볼록하고, 대칭축은 $$수식$$y$$/수식$$축의 오른쪽에 위치한다.'],
          ['$$수식$$y = - {p1} x^2$$/수식$$의 그래프를 $$수식$$x$$/수식$$축의 방향으로 $$수식$${p4}$$/수식$$만큼, '
           '$$수식$$y$$/수식$$축의 방향으로 $$수식$${p5}$$/수식$$만큼 평행이동한 것이다.'.format(p1=p1, p4=p4, p5=p5),
           ''],
          ['$$수식$$x {op} {p4}$$/수식$$일 때, $$수식$$x$$/수식$$의 값이 증가하면 $$수식$$y$$/수식$$의 값{menu1}.'.format(op=op, p4=p4, menu1=menu1),
           '$$수식$$x {op} {p4}$$/수식$$일 때, $$수식$$x$$/수식$$의 값이 증가하면 $$수식$$y$$/수식$$의 값{menu2}.'.format(op=op, p4=p4, menu2=menu2)]]

    np.random.shuffle(cs)
    [c1, _], [c2, _], [c3, _], [c4, _], [c5, _] = cs
    n = ["①", "②", "③", "④", "⑤"]
    for i in range(0, len(cs)):
        if cs[i][1] == '':
            s = answer_dict[i]
            n.remove(s)
            cs.remove(cs[i])
            break
    [_, ex1], [_, ex2], [_, ex3], [_, ex4] = cs
    n1, n2, n3, n4 = n

    stem = stem.format(p1=p1, p2=p2, p3=p3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, ex1=ex1, ex2=ex2, ex3=ex3, ex4=ex4, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5)

    return stem, answer, comment




# 3-1-3-218
def quadequation313_Stem_173():
    stem = "이차함수 $$수식$$y = {p1} x^2 + {p2} x + {p3}$$/수식$$의 그래프에 대한 설명으로 옳은 것은?\n" \
           "① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = {p1} x^2 + {p2} x + {p3} = {p1} LEFT ( x + {p4} RIGHT ) ^2 - {p5}$$/수식$$\n" \
              "{n1} {ex1}\n" \
              "{n2} {ex2}\n" \
              "{n3} {ex3}\n" \
              "{n4} {ex4}\n\n"

    while True:
        xx = random.sample(list(range(-5, 0)), 2)
        xx.sort()
        x1, x2 = xx
        p1 = np.random.randint(2, 4)
        p2 = - p1 * (x1 + x2)
        p3 = p1 * x1*x2
        p4 = int(p2/(2*p1))
        p5 = p1*p4*p4 - p3
        if p2 % (2*p1) == 0 and p5 > 0:
            break

    cs = [['모든 사분면을 지난다.',
           '제$$수식$$4$$/수식$$사분면을 지나지 않는다.'],
          ['축의 방정식은 $$수식$$x = {p4}$$/수식$$이다.'.format(p4=p4),
           '축의 방정식은 $$수식$$x = {p4}$$/수식$$이다.'.format(p4=-p4)],
          ['꼭짓점의 좌표는 $$수식$$LEFT ( {p4}$$/수식$$, $$수식$${p5} RIGHT )$$/수식$$이다.'.format(p4=p4, p5=-p5),
           '꼭짓점의 좌표는 $$수식$$LEFT ( {p4}$$/수식$$, $$수식$${p5} RIGHT )$$/수식$$이다.'.format(p4=-p4, p5=-p5)],
          ['$$수식$$x$$/수식$$축과의 교점의 좌표는 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$, '
           '$$수식$$LEFT ( {x2}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$이다.'.format(x1=x1, x2=x2),
           ''],
          ['이차함수 $$수식$$y = - {p1} x^2 - {p2} x - {p3}$$/수식$$의 그래프와 $$수식$$y$$/수식$$축에 대하여 대칭이다.'.format(p1=p1, p2=p2, p3=p3),
           '이차함수 $$수식$$y = - {p1} x^2 - {p2} x - {p3}$$/수식$$의 그래프와 $$수식$$x$$/수식$$축에 대하여 대칭이다.'.format(p1=p1, p2=p2, p3=p3)]]

    np.random.shuffle(cs)
    [c1, _], [c2, _], [c3, _], [c4, _], [c5, _] = cs
    n = ["①", "②", "③", "④", "⑤"]
    for i in range(0, len(cs)):
        if cs[i][1] == '':
            s = answer_dict[i]
            n.remove(s)
            cs.remove(cs[i])
            break
    [_, ex1], [_, ex2], [_, ex3], [_, ex4] = cs
    n1, n2, n3, n4 = n

    stem = stem.format(p1=p1, p2=p2, p3=p3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, ex1=ex1, ex2=ex2, ex3=ex3, ex4=ex4, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5)

    return stem, answer, comment





# 3-1-3-219
def quadequation313_Stem_174():
    stem = "이차함수 $$수식$$y = - {p1} x^2 + {p2} x$$/수식$$의 그래프에 대한 설명으로 옳지 않은 것은?\n" \
           "① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = - {p1} x^2 + {p2} x = - {p1} LEFT (x - {p3} RIGHT ) ^2 + {p4}$$/수식$$\n" \
              "{s} {explain}\n\n"

    p1 = np.random.randint(2, 6)
    p3 = np.random.randint(1, 4)
    p4 = p1*p3*p3
    p2 = 2*p1*p3
    op, menu = [['&gt;', '은 감소한다'], ['&lt;', '도 증가한다']][np.random.randint(0, 2)]

    c = ['원점을 지난다.',
         '위로 볼록한 포물선이다.',
         '함숫값의 범위는 $$수식$$y GEQ {p4}$$/수식$$이다.'.format(p4=p4),
         '평행이동하면 $$수식$$y = - {p1} x^2$$/수식$$의 그래프와 포개어진다.'.format(p1=p1),
         '$$수식$$x {op} {p3}$$/수식$$일 때, $$수식$$x$$/수식$$의 값이 증가하면 $$수식$$y$$/수식$$의 값{menu}.'.format(op=op, p3=p3, menu=menu)]
    ss = '함숫값의 범위는 $$수식$$y GEQ {p4}$$/수식$$이다.'.format(p4=p4)
    explain = '함숫값의 범위는 $$수식$$y LEQ {p4}$$/수식$$이다.'.format(p4=p4)
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(s=s, explain=explain, p1=p1, p2=p2, p3=p3, p4=p4)

    return stem, answer, comment




# 3-1-3-220
def quadequation313_Stem_175():
    stem = "다음 중 이차함수 $$수식$$y = ax^2 + bx + c$$/수식$$의 그래프에 대한 설명으로 옳지 않은 것은? " \
           "$$수식$$LEFT ($$/수식$$단, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$는 상수이다.$$수식$$RIGHT )$$/수식$$\n" \
           "① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "{s} {explain}\n" \
              "따라서 옳지 않은 것은 {s}이다.\n\n"

    op, dir1 = [['&gt;', '아래로'], ['&lt;', '위로']][np.random.randint(0, 2)]

    c = ['$$수식$$x$$/수식$$절편은 $$수식$$c$$/수식$$이다.',
         '그래프 모양은 포물선이다.',
         '축의 방정식은 $$수식$$x = - b OVER 2a$$/수식$$이다.',
         '$$수식$$a {op} 0$$/수식$$이면 그래프는 {dir1} 볼록하다.'.format(op=op, dir1=dir1),
         '꼭짓점의 좌표는 $$수식$$LEFT ( - b OVER 2a$$/수식$$, $$수식$$- { b^2 - 4ac } over { 4a } RIGHT )$$/수식$$이다.']

    ss = '$$수식$$x$$/수식$$절편은 $$수식$$c$$/수식$$이다.'
    explain = '$$수식$$x$$/수식$$절편은 이차방정식 $$수식$$ax^2 + bx + c$$/수식$$의 해이고 $$수식$$y$$/수식$$절편이 $$수식$$c$$/수식$$이다.'
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(s=s, explain=explain)

    return stem, answer, comment





# 3-1-3-221
def quadequation313_Stem_176():
    stem = "이차함수 $$수식$$y = {p1} x^2 - {p2} x + {p3}$$/수식$$의 그래프에 대한 설명으로 " \
           "옳은 것을 보기에서 있는 대로 고른 것은?\n" \
           "$$표$$ |  보기  |\n" \
           "㈀ {c1}\n㈁ {c2}\n㈂ {c3}\n㈃ {c4}$$/표$$\n" \
           "① ㈀, ㈁\t\t② ㈀, ㈂\t\t③ ㈁, ㈂\n④ ㈁, ㈃\t\t⑤ ㈂, ㈃\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = {p1} x^2 - {p2} x + {p3} = {p1} LEFT (x - {p4} RIGHT ) ^2 - {p5}$$/수식$$\n" \
              "{s1} {ex1}\n" \
              "{s2} {ex2}\n" \
              "따라서 옳은 것은 {s1}, {s2}이다.\n\n"

    p1 = np.random.randint(2, 4)
    p4 = np.random.randint(1, 4)
    p2 = 2 * p1 * p4
    p5 = np.random.randint(1, p1*p4*p4)
    p3 = p1*p4*p4 - p5

    cs = [['$$수식$$x$$/수식$$축과 두 점에서 만난다.',  # 정답
           '$$수식$$x$$/수식$$축과 한 점에서 만난다.'],  # 오답
          ['제$$수식$$3$$/수식$$사분면을 지나지 않는다.',
           '제$$수식$$3$$/수식$$사분면을 지난다.'],
          ['꼭짓점의 좌표는 $$수식$$LEFT ( {a}$$/수식$$, $$수식$${b} RIGHT )$$/수식$$이다.'.format(a=p4, b=-p5),
           '꼭짓점의 좌표는 $$수식$$LEFT ( {a}$$/수식$$, $$수식$${b} RIGHT )$$/수식$$이다.'.format(a=-p4, b=p5)],
          ['$$수식$$y$$/수식$$축과의 교점의 좌표는 $$수식$$LEFT ( 0$$/수식$$, $$수식$${y} RIGHT )$$/수식$$'.format(y=p3),
           '$$수식$$y$$/수식$$축과의 교점의 좌표는 $$수식$$LEFT ( 0$$/수식$$, $$수식$${y} RIGHT )$$/수식$$'.format(y=-p5)]]
    np.random.shuffle(cs)

    while True:
        ans = random.sample(list(range(0, 4)), 2)
        if not ((0 in ans) and (3 in ans)):
            break
    c = []
    ss = []
    ex = []
    count = 0
    for i in range(0, len(cs)):
        if i in ans:
            c.append(cs[i][0])
            count += i
        else:
            c.append(cs[i][1])
            ss.append(answer_kodict3[i])
            ex.append(cs[i][0])

    s = answer_dict[count-1]
    c1, c2, c3, c4 = c
    s1, s2 = ss
    ex1, ex2 = ex

    stem = stem.format(p1=p1, p2=p2, p3=p3, c1=c1, c2=c2, c3=c3, c4=c4)
    answer = answer.format(s=s)
    comment = comment.format(s1=s1, s2=s2, ex1=ex1, ex2=ex2, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5)

    return stem, answer, comment





# 3-1-3-222
def quadequation313_Stem_177():
    stem = "다음 중 이차함수 $$수식$$y = ax^2 + bx + c$$/수식$$의 그래프에 대한 설명으로 옳은 것은?\n" \
           "① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = ax^2 + bx + c = a LEFT ( x + b OVER 2a RIGHT ) ^2 + c - b^2 OVER 4a$$/수식$$\n" \
              "{n1} {ex1}\n" \
              "{n2} {ex2}\n" \
              "{n3} {ex3}\n" \
              "{n4} {ex4}\n\n"

    cs = [['$$수식$$a &lt; 0$$/수식$$이면 그래프는 위로 볼록하다.',  # 정답
           '$$수식$$a &lt; 0$$/수식$$이면 그래프는 아래로 볼록하다.'],  # 오답
          ['축의 방정식은 $$수식$$x = - b OVER 2a$$/수식$$이다.',
           '축의 방정식은 $$수식$$x = b OVER 2a$$/수식$$이다.'],
          ['$$수식$$x$$/수식$$축과의 교점의 개수는 알 수 없다.',
           '$$수식$$x$$/수식$$축과의 교점의 개수는 $$수식$$1$$/수식$$이다.'],
          ['$$수식$$y = ax^2$$/수식$$의 그래프와 폭이 같다.',
           '$$수식$$y = ax^2$$/수식$$의 그래프보다 폭이 넓다.'],
          ['이차함수 $$수식$$y = - ax^2 - bx - c$$/수식$$의 그래프와 $$수식$$x$$/수식$$축에 대하여 대칭이다.',
           '이차함수 $$수식$$y = - ax^2 - bx - c$$/수식$$의 그래프와 $$수식$$y$$/수식$$축에 대하여 대칭이다.']]
    np.random.shuffle(cs)

    ans = np.random.randint(0, 5)
    c = []
    n = []
    ex = []
    for i in range(0, len(cs)):
        if i == ans:
            s = answer_dict[i]
            c.append(cs[i][0])
        else:
            c.append(cs[i][1])
            ex.append(cs[i][0])
            n.append(answer_dict[i])

    n1, n2, n3, n4 = n
    ex1, ex2, ex3, ex4 = ex
    c1, c2, c3, c4, c5 = c

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, ex1=ex1, ex2=ex2, ex3=ex3, ex4=ex4)

    return stem, answer, comment





# 3-1-3-240
def quadequation313_Stem_178():
    stem = "꼭짓점의 좌표가 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$이고, " \
           "$$수식$$y$$/수식$$축과의 교점의 $$수식$$y$$/수식$$좌표가 $$수식$${y2}$$/수식$$인 포물선을 " \
           "그래프로 하는 이차함수의 식을 $$수식$$y = ax^2 + bx + c$$/수식$$라 할 때, " \
           "$$수식$$a - b + c$$/수식$$의 값은? " \
           "$$수식$$LEFT ($$/수식$$단, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$는 상수이다.$$수식$$RIGHT )$$/수식$$\n" \
           "① $$수식$${c1}$$/수식$$\t\t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\t\t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = ax^2 + bx + c$$/수식$$의 그래프의 꼭짓점이 좌표가 " \
              "$$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$이므로 이차함수의 식을 " \
              "$$수식$$y = a LEFT ( x {op1} {x11} RIGHT ) ^2 {op2} {y1}$$/수식$$로 놓을 수 있다.\n" \
              "이 그래프가 점 $$수식$$LEFT ( 0$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$${y2} = {x112} a {op2} {y1}$$/수식$$\t\t$$수식$$THEREFORE~ a = {a}$$/수식$$\n" \
              "따라서 $$수식$$y = {a} LEFT ( x {op1} {x11} RIGHT ) ^2 {op2} {y1} = {a} x^2 {op1} {b} x {op3} {c}$$/수식$$이므로\n" \
              "$$수식$$b = {b}$$/수식$$, $$수식$$c = {c}$$/수식$$\n" \
              "$$수식$$THEREFORE~ a - b + c = {ss}$$/수식$$\n\n"

    while True:
        a = np.random.randint(2, 4)
        x1 = random.sample(list(range(-3, 0))+list(range(1, 4)), 1)[0]
        y1 = random.sample(list(range(-5, 0))+list(range(1, 6)), 1)[0]
        x11 = -x1
        x112 = x11 * x11
        b = 2 * a * x11
        c = a * x112 + y1
        y2 = c
        if c != 0:
            break

    op1, op2, op3 = '', '', ''
    if x11 > 0:
        op1 = '+'
    if y1 > 0:
        op2 = '+'
    if c > 0:
        op3 = '+'

    if x112 == 1:
        x112 = ''

    ss = a - b + c
    cc = random.sample(list(range(ss-10, ss))+list(range(ss+1, ss+11)), 4)
    cc.append(ss)
    cc.sort()
    c1, c2, c3, c4, c5 = cc
    for i in range(0, len(cc)):
        if cc[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(x1=x1, y1=y1, y2=y2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(x1=x1, y1=y1, y2=y2, x11=x11, x112=x112, op1=op1, op2=op2, op3=op3, ss=ss, a=a, b=b, c=c)

    return stem, answer, comment





# 3-1-3-241
def quadequation313_Stem_179():
    stem = "꼭짓점이 좌표가 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$이고, " \
           "점 $$수식$$LEFT ( {x2}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$을 지나는 " \
           "이차함수의 그래프가 $$수식$$y$$/수식$$축과 만나는 점의 좌표는?\n" \
           "① {c1}\t\t② {c2}\n" \
           "③ {c3}\t\t④ {c4}\n" \
           "⑤ {c5}\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "꼭짓점이 좌표가 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$이므로 " \
              "이차함수의 식을 $$수식$$y = a LEFT ( x {op1} {x11} RIGHT ) ^2 {op2} {y1}$$/수식$$로 놓을 수 있다.\n" \
              "이 그래프가 점 $$수식$$LEFT ( {x2}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$을 지나므로\n" \
              "$$수식$$0 = {x112} a {op2} {y1}$$/수식$$\t\t$$수식$$THEREFORE~ a = {p1} OVER {p2}$$/수식$$\n" \
              "따라서 $$수식$$y = {p1} OVER {p2} LEFT ( x {op1} {x11} RIGHT ) ^2 {op2} {y1} " \
              "= {p1} OVER {p2} x^2 {op1} {p3} x {op3} {p4} OVER {p5}$$/수식$$이므로 " \
              "이 그래프가 $$수식$$y$$/수식$$축과 만나는 점의 좌표는 " \
              "$$수식$$LEFT ( 0$$/수식$$, $$수식$${op33} {p4} OVER {p5} RIGHT )$$/수식$$이다.\n\n"

    while True:
        p1, p2 = [[1, 2], [3, 2], [5, 2]][np.random.randint(0, 3)]
        y1 = -2 * p1
        x1 = 2 *np.random.randint(-2, 2) + 1
        x2 = [x1+2, x1-2][np.random.randint(0, 2)]
        x11 = -x1
        x112 = (x2 - x1)*(x2 - x1)
        p3 = -int(2*x1*p1/p2)
        p4 = p1*x1*x1 + p2*y1
        p5 = p2
        if GCD(p1, p2) == 1 and p4 != 0:
            break

    op1, op2 = '', ''
    if x11 > 0:
        op1 = '+'
    if p4 > 0:
        op3, op33 = '+', ''
    else:
        op3, op33 = '-', '-'
        p4 = -p4

    ss = '$$수식$$LEFT ( 0$$/수식$$, $$수식$${op} {y1} OVER {y2} RIGHT )$$/수식$$'.format(op=op33, y1=p4, y2=p5)
    c = [ss]
    c.append('$$수식$$LEFT ( 0$$/수식$$, $$수식$${op} {y1} OVER {y2} RIGHT )$$/수식$$'.format(op=op33, y1=(p4+p5), y2=p5))
    if op3 == '+':
        c.append('$$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$'.format(y1=int(p4/p5)))
        c.append('$$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$'.format(y1=(int(p4/p5)-1)))
        c.append('$$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$'.format(y1=(int(p4/p5)+1)))
    else:  # op3 == '-'
        c.append('$$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$'.format(y1=-int(p4 / p5)))
        c.append('$$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$'.format(y1=-(int(p4 / p5) - 1)))
        c.append('$$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$'.format(y1=-(int(p4 / p5) + 1)))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(x1=x1, x2=x2, y1=y1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(x1=x1, x2=x2, y1=y1, x11=x11, x112=x112, op1=op1, op2=op2, op3=op3, op33=op33, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5)

    return stem, answer, comment





# 3-1-3-242
def quadequation313_Stem_180():
    stem = "꼭짓점의 좌표가 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$이고, " \
           "$$수식$$y$$/수식$$축과의 교점의 $$수식$$y$$/수식$$좌표가 $$수식$${y2}$$/수식$$인 포물선을 " \
           "그래프로 하는 이차함수의 식을 $$수식$$y = ax^2 + bx + c$$/수식$$라 할 때, " \
           "$$수식$$bc OVER a$$/수식$$의 값을 구하시오. " \
           "$$수식$$LEFT ($$/수식$$단, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$는 상수이다.$$수식$$RIGHT )$$/수식$$\n"
    answer = "(답): $$수식$${s}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y = ax^2 + bx + c$$/수식$$의 그래프의 꼭짓점이 좌표가 " \
              "$$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$이므로 이차함수의 식을 " \
              "$$수식$$y = a LEFT ( x {op1} {x11} RIGHT ) ^2 {op2} {y1}$$/수식$$로 놓을 수 있다.\n" \
              "이 그래프가 점 $$수식$$LEFT ( 0$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$${y2} = {x112} a {op2} {y1}$$/수식$$\t\t$$수식$$THEREFORE~ a = {a}$$/수식$$\n" \
              "따라서 $$수식$$y = {a} LEFT ( x {op1} {x11} RIGHT ) ^2 {op2} {y1} = {a} x^2 {op1} {b} x {op3} {c}$$/수식$$이므로\n" \
              "$$수식$$b = {b}$$/수식$$, $$수식$$c = {c}$$/수식$$\n" \
              "$$수식$$THEREFORE~ bc OVER a = {s}$$/수식$$\n\n"

    while True:
        a = np.random.randint(2, 4)
        x1 = random.sample(list(range(-3, 0))+list(range(1, 4)), 1)[0]
        y1 = random.sample(list(range(-5, 0))+list(range(1, 6)), 1)[0]
        x11 = -x1
        x112 = x11 * x11
        b = 2 * a * x11
        c = a * x112 + y1
        y2 = c
        if c != 0 and (b*c) % a == 0:
            break

    s =int(b*c/a)

    op1, op2, op3 = '', '', ''
    if x11 > 0:
        op1 = '+'
    if y1 > 0:
        op2 = '+'
    if c > 0:
        op3 = '+'

    if x112 == 1:
        x112 = ''

    stem = stem.format(x1=x1, y1=y1, y2=y2)
    answer = answer.format(s=s)
    comment = comment.format(x1=x1, y1=y1, y2=y2, x11=x11, x112=x112, op1=op1, op2=op2, op3=op3, s=s, a=a, b=b, c=c)

    return stem, answer, comment





# 3-1-3-246
def quadequation313_Stem_181():
    stem = "이차함수 $$수식$$y = {p1} x^2 {p2}$$/수식$$의 그래프와 꼭짓점이 같고, " \
           "점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$를 지나는 포물선이 " \
           "$$수식$$x$$/수식$$축과 만나는 두 점 사이의 거리를 구하시오.\n"
    answer = "(답): $$수식$${s}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y = {p1} x^2 {p2}$$/수식$$의 그래프의 꼭짓점의 좌표는\n" \
              "$$수식$$LEFT ( 0$$/수식$$, $$수식$${p2} RIGHT )$$/수식$$\n" \
              "이므로 이차함수의 식을 $$수식$$y = ax^2 {p2}$$/수식$$로 놓을 수 있다.\n" \
              "이 그래프가 점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$${y1} = {x11} a {p2}$$/수식$$\t\t$$수식$$THEREFORE~ a = {a}$$/수식$$\n" \
              "$$수식$$THEREFORE~ y = {p3} x^2 {p2}$$/수식$$\n" \
              "$$수식$$y = {p3} x^2 {p2}$$/수식$$에 $$수식$$y = 0$$/수식$$을 대입하면\n" \
              "$$수식$$0 = {p3} x^2 {p2}$$/수식$$, $$수식$$x^2 = {p4}$$/수식$$\n" \
              "$$수식$$THEREFORE~ x = PLUSMINUS {p5}$$/수식$$\n" \
              "따라서 이차함수의 그래프가 $$수식$$x$$/수식$$축과 만나는 두 점이 좌표는 " \
              "$$수식$$LEFT ( - {p5}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$, $$수식$$LEFT ( {p5}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$이므로 " \
              "두 점 사이의 거리는 $$수식$${p5} - LEFT ( - {p5} RIGHT ) = {s}$$/수식$$\n\n"

    p1 = random.sample(list(range(-4, -1)) + list(range(2, 5)), 1)[0]
    x1 = random.sample(list(range(-3, 0)) + list(range(1, 4)), 1)[0]
    x11 = x1 * x1
    a = np.random.randint(1, 4)
    p3 = a
    p5 = np.random.randint(1, 6)
    p4 = p5 * p5
    p2 = - p5 * p5 * p3
    y1 = x1 * x1 * a + p2
    s = 2 * p5

    if x11 == 1:
        x11 = ''
    if p3 == 1:
        p3 = ''

    stem = stem.format(p1=p1, p2=p2, x1=x1, y1=y1)
    answer = answer.format(s=s)
    comment = comment.format(a=a, s=s, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, x1=x1, x11=x11, y1=y1)

    return stem, answer, comment





# 3-1-3-249
def quadequation313_Stem_182():
    stem = "직선 $$수식$$x = {p1}$$/수식$$을 축으로 하고, 두 점 " \
           "$$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$를 지나는 " \
           "포물선을 그래프로 하는 이차함수의 식은?\n" \
           "① $$수식$${c1}$$/수식$$\t\t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\t\t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "축의 방정식이 $$수식$$x = {p1}$$/수식$$이므로 이차함수의 식을 " \
              "$$수식$$y = a LEFT ( x {op1} {p2} RIGHT ) ^2 + q$$/수식$$로 놓을 수 있다.\n" \
              "이 그래프가 점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$${y1} = {p3} a + q$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉠\n" \
              "또 점 $$수식$$LEFT ( {x2}$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$을 지나므로\n" \
              "$$수식$${y2} = {p4} a + q$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉡\n" \
              "㉠, ㉡을 연립하여 풀면\n$$수식$$a = {a}$$/수식$$, $$수식$$q = {q}$$/수식$$\n" \
              "$$수식$$THEREFORE~ y = {p5} LEFT ( x {op1} {p2} RIGHT ) ^2 {op2} {q} " \
              "= {p5} x^2 {op1} {p6} x {op3} {p7}$$/수식$$\n\n"
    while True:
        p1 = random.sample(list(range(-3, 0)) + list(range(1, 4)), 1)[0]
        p2 = -p1
        p33, p44 = random.sample(list(range(1, 5)), 2)
        p3 = p33*p33
        p4 = p44*p44
        x1 = [p1+p33, p1-p33][np.random.randint(0, 2)]
        x2 = [p1+p44, p1-p44][np.random.randint(0, 2)]
        a = np.random.randint(1, 5)
        p5 = a
        y2 = np.random.randint(-4, 5)
        y1 = a * (p3-p4) + y2
        q = y1 - p3 * a
        p7 = p5 * p2 * p2 + q
        p6 = 2 * p5 * p2
        if q != 0 and p7 != 0:
            break

    op1, op2, op3 = '', '', ''
    if p2 > 0:
        op1 = '+'
    if q > 0:
        op2 = '+'
    if p7 > 0:
        op3 = '+'

    if p3 == 1:
        p3 = ''
    if p4 == 1:
        p4 = ''
    if p5 == 1:
        p5 = ''

    ss = 'y = {a} x^2 {op1} {b} x {op2} {c}'.format(a=p5, op1=op1, b=p6, op2=op3, c=p7)
    c = [ss]
    c.append('y = - {a} x^2 {op1} {b} x {op2} {c}'.format(a=p5, op1=op1, b=p6, op2=op3, c=p7))
    c.append('y = {a} x^2 {op1} {b} x {op2} {c}'.format(a=(2*p5), op1=op1, b=p6, op2=op3, c=p7))
    c.append('y = - {a} x^2 {op1} {b} x {op2} {c}'.format(a=(2*p5), op1=op1, b=p6, op2=op3, c=p7))
    c.append('y = {a} x^2 {op1} {b} x {op2} {c}'.format(a=p5, op1=op1, b=p6+1, op2=op3, c=p7))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, x1=x1, x2=x2, y1=y1, y2=y2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(a=a, q=q, x1=x1, x2=x2, y1=y1, y2=y2, op1=op1, op2=op2, op3=op3, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7)

    return stem, answer, comment





# 3-1-3-250
def quadequation313_Stem_183():
    stem = "이차함수 $$수식$$y = x^2 + ax + b$$/수식$$의 그래프는 축의 방정식이 $$수식$$x = {p1}$$/수식$$이고, " \
           "점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$를 지난다. " \
           "이 때 상수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$a + b$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$\t\t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\t\t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = x^2 + ax + b$$/수식$$의 그래프의 축의 방정식이 $$수식$$x = {p1}$$/수식$$이므로 " \
              "이차함수의 식을 $$수식$$y = LEFT ( x {op1} {p2} RIGHT ) ^2 + q$$/수식$$로 놓을 수 있다.\n" \
              "이 그래프가 점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$${y1} = {p3} + q$$/수식$$\t\t$$수식$$THEREFORE~ q = {q}$$/수식$$\n" \
              "따라서 $$수식$$y = LEFT ( x {op1} {p2} RIGHT ) ^2 {op2} {p4} = x^2 {op1} {p5} x {op3} {p6}$$/수식$$이므로\n" \
              "$$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$" \
              "$$수식$$THEREFORE~ a + b = {ab}$$/수식$$\n\n"

    p1 = random.sample(list(range(-3, 0)) + list(range(1, 4)), 1)[0]
    p2 = -p1
    x1 = np.random.randint(-5, 6)
    p3 = (x1 - p1) * (x1 - p1)
    q = np.random.randint(-9, 10)
    y1 = p3 + q
    p4 = q
    p5 = 2*p2
    p6 = p2*p2 + q
    a = p5
    b = p6
    ab = a + b

    op1, op2, op3 = '', '', ''
    if p2 > 0:
        op1 = '+'
    if p4 > 0:
        op2 = '+'
    elif p4 == 0:
        p4 = ''
    if p6 > 0:
        op3 = '+'
    elif p6 == 0:
        p6 = ''

    c = random.sample(list(range(ab-5, ab))+list(range(ab+1, ab+6)), 4)
    c.append(ab)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ab:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, x1=x1, y1=y1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(a=a, b=b, ab=ab, q=q, x1=x1, y1=y1, op1=op1, op2=op2, op3=op3, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6)

    return stem, answer, comment





# 3-1-3-251
def quadequation313_Stem_184():
    stem = "이차함수 $$수식$$y = x^2 + ax + b$$/수식$$의 그래프는 축의 방정식이 $$수식$$x = {p1}$$/수식$$이고, " \
           "점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$를 지난다. " \
           "이 때 상수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$ab$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${ab}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$y = x^2 + ax + b$$/수식$$의 그래프의 축의 방정식이 $$수식$$x = {p1}$$/수식$$이므로 " \
              "이차함수의 식을 $$수식$$y = LEFT ( x {op1} {p2} RIGHT ) ^2 + q$$/수식$$로 놓을 수 있다.\n" \
              "이 그래프가 점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$${y1} = {p3} + q$$/수식$$\t\t$$수식$$THEREFORE~ q = {q}$$/수식$$\n" \
              "따라서 $$수식$$y = LEFT ( x {op1} {p2} RIGHT ) ^2 {op2} {p4} = x^2 {op1} {p5} x {op3} {p6}$$/수식$$이므로\n" \
              "$$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$" \
              "$$수식$$THEREFORE~ ab = {ab}$$/수식$$\n\n"

    while True:
        p1 = random.sample(list(range(-3, 0)) + list(range(1, 4)), 1)[0]
        p2 = -p1
        x1 = np.random.randint(-5, 6)
        p3 = (x1 - p1) * (x1 - p1)
        q = np.random.randint(-9, 10)
        y1 = p3 + q
        p4 = q
        p5 = 2*p2
        p6 = p2*p2 + q
        a = p5
        b = p6
        ab = a * b
        if a != 0 and b != 0:
            break

    op1, op2, op3 = '', '', ''
    if p2 > 0:
        op1 = '+'
    if p4 > 0:
        op2 = '+'
    elif p4 == 0:
        p4 = ''
    if p6 > 0:
        op3 = '+'

    stem = stem.format(p1=p1, x1=x1, y1=y1)
    answer = answer.format(ab=ab)
    comment = comment.format(a=a, b=b, ab=ab, q=q, x1=x1, y1=y1, op1=op1, op2=op2, op3=op3, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6)

    return stem, answer, comment





# 3-1-3-253
def quadequation313_Stem_185():
    stem = "축의 방정식이 $$수식$$x = {p1}$$/수식$$이고, " \
           "두 점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$를 지나는 이차함수의 그래프가 " \
           "점 $$수식$$LEFT ( {x3}$$/수식$$, $$수식$$k RIGHT )$$/수식$$를 지날 때, $$수식$$k$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$\t\t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\t\t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "축의 방정식이 $$수식$$x = {p1}$$/수식$$이므로 " \
              "이차함수의 식을 $$수식$$y = a LEFT ( x {op1} {p2} RIGHT ) ^2 + q$$/수식$$로 놓을 수 있다.\n" \
              "이 그래프가 점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$${y1} = {p3} a + q$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉠\n" \
              "또 점 $$수식$$LEFT ( {x2}$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$을 지나므로\n" \
              "$$수식$${y2} = {p4} a + q$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉡\n" \
              "㉠, ㉡을 연립하여 풀면\n$$수식$$a = {a}$$/수식$$, $$수식$$q = {q}$$/수식$$\n" \
              "따라서 $$수식$$y = {p5} LEFT ( x {op1} {p2} RIGHT ) ^2 {op2} {p6}$$/수식$$의 그래프가 " \
              "점 $$수식$$LEFT ( {x3}$$/수식$$, $$수식$$k RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$$k = {p5} LEFT ( {x3} {op1} {p2} RIGHT ) ^2 {op2} {p6} = {k}$$/수식$$\n\n"

    while True:
        p1 = random.sample(list(range(-3, 0)) + list(range(1, 4)), 1)[0]
        p2 = -p1
        x1, x2, x3 = random.sample(list(range(-5, 6)), 3)
        p3 = (x1 - p1) * (x1 - p1)
        p4 = (x2 - p1) * (x2 - p1)
        a = np.random.randint(1, 5)
        q = np.random.randint(-9, 10)
        y1 = a*p3 + q
        y2 = a*p4 + q
        p5 = a
        p6 = q
        k = a*(x3 - p1)*(x3 - p1) + q
        if p3 != 0 and p4 != 0:
            break

    op1, op2 = '', ''
    if p2 > 0:
        op1 = '+'
    if p6 > 0:
        op2 = '+'
    elif p6 == 0:
        p6 = ''
    if p5 == 1:
        p5 = ''
    if p3 == 1:
        p3 = ''
    if p4 == 1:
        p4 = ''

    c = random.sample(list(range(k-10, k))+list(range(k+1, k+11)), 4)
    c.append(k)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == k:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, x1=x1, y1=y1, x2=x2, y2=y2, x3=x3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(k=k, a=a, q=q, x1=x1, y1=y1, x2=x2, y2=y2, x3=x3, op1=op1, op2=op2, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6)

    return stem, answer, comment





# 3-1-3-255
def quadequation313_Stem_186():
    stem = "이차함수 $$수식$$y = ax^2 + bx + c$$/수식$$의 그래프가 세 점 " \
           "$$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x3}$$/수식$$, $$수식$${y3} RIGHT )$$/수식$$을 지날 때, " \
           "상수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$에 대하여 $$수식$$abc$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$\t\t② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\t\t④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y$$/수식$$절편이 $$수식$${y1}$$/수식$$이므로 $$수식$$c = {y1}$$/수식$$\n" \
              "$$수식$$y = ax^2 + bx {op1} {y1}$$/수식$$의 그래프가 점 " \
              "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$${y2} = {p1} a {op2} {p2} b {op1} {y1}$$/수식$$\t\t" \
              "$$수식$$THEREFORE~ {p1} a {op2} {p2} b = {p3}$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉠\n" \
              "또 점 $$수식$$LEFT ( {x3}$$/수식$$, $$수식$${y3} RIGHT )$$/수식$$을 지나므로\n" \
              "$$수식$${y3} = {p4} a {op3} {p5} b {op1} {y1}$$/수식$$\t\t" \
              "$$수식$$THEREFORE~ {p4} a {op3} {p5} b = {p6}$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉡\n" \
              "㉠, ㉡을 연립하여 풀면\n$$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$\n" \
              "$$수식$$THEREFORE~ abc = {abc}$$/수식$$\n\n"

    a, b, c = random.sample(list(range(-4, 0)) + list(range(1, 5)), 3)
    abc = a * b * c
    y1 = c
    x2, x3 = random.sample(list(range(-3, 0)) + list(range(1, 4)), 2)
    p1 = x2 * x2
    p2 = x2
    p3 = p1 * a + p2 * b
    p4 = x3 * x3
    p5 = x3
    p6 = p4 * a + p5 * b
    y2 = p3 + y1
    y3 = p6 + y1

    op1, op2, op3 = '', '', ''
    if y1 > 0:
        op1 = '+'
    if p2 > 0:
        op2 = '+'
    if p5 > 0:
        op3 = '+'

    if x2 == 1:
        p1 = ''
        p2 = ''
    elif x2 == -1:
        p1 = ''
        p2 = '-'

    if x3 == 1:
        p4 = ''
        p5 = ''
    elif x3 == -1:
        p4 = ''
        p5 = '-'

    c = random.sample(list(range(abc-10, abc))+list(range(abc+1, abc+11)), 4)
    c.append(abc)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == abc:
            s = answer_dict[i]
            break

    stem = stem.format(x2=x2, x3=x3, y1=y1, y2=y2, y3=y3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(abc=abc, a=a, b=b, x2=x2, x3=x3, y1=y1, y2=y2, y3=y3, op1=op1, op2=op2, op3=op3, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6)

    return stem, answer, comment





# 3-1-3-256
def quadequation313_Stem_187():
    stem = "세 점 $$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x3}$$/수식$$, $$수식$${y3} RIGHT )$$/수식$$을 지나는 이차함수의 그래프의 꼭짓점의 좌표는?\n" \
           "① $$수식$$LEFT ( {c1}$$/수식$$, $$수식$${c2} RIGHT )$$/수식$$\t\t" \
           "② $$수식$$LEFT ( {c3}$$/수식$$, $$수식$${c4} RIGHT )$$/수식$$\t\t" \
           "③ $$수식$$LEFT ( {c5}$$/수식$$, $$수식$${c6} RIGHT )$$/수식$$\n" \
           "④ $$수식$$LEFT ( {c7}$$/수식$$, $$수식$${c8} RIGHT )$$/수식$$\t\t" \
           "⑤ $$수식$$LEFT ( {c9}$$/수식$$, $$수식$${c10} RIGHT )$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "구하는 이차함수의 식을 $$수식$$y = ax^2 + bx + c$$/수식$$로 놓고 " \
              "$$수식$$x = 0$$/수식$$, $$수식$$y = {y1}$$/수식$$을 대입하면 $$수식$$c = {y1}$$/수식$$\n" \
              "즉, $$수식$$y = ax^2 + bx {op1} {y1}$$/수식$$에\n" \
              "$$수식$$LEFT ($$/수식$$ⅰ$$수식$$RIGHT )$$/수식$$ " \
              "$$수식$$x = {x2}$$/수식$$, $$수식$$y = {y2}$$/수식$$을 대입하면\n" \
              "$$수식$${y2} = {p1} a {op2} {p2} b {op1} {y1}$$/수식$$\n" \
              "$$수식$$THEREFORE~ {p7} a {op2} {p8} b = {p9}$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉠\n" \
              "$$수식$$LEFT ($$/수식$$ⅱ$$수식$$RIGHT )$$/수식$$ " \
              "$$수식$$x = {x3}$$/수식$$, $$수식$$y = {y3}$$/수식$$을 대입하면\n" \
              "$$수식$${y3} = {p4} a {op3} {p5} b {op1} {y1}$$/수식$$\n" \
              "$$수식$$THEREFORE~ {p10} a {op3} {p11} b = {p12}$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉡\n" \
              "㉠, ㉡을 연립하여 풀면\n$$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$\n" \
              "따라서 $$수식$$y = {p13} x^2 {op4} {p14} x {op1} {y1} " \
              "= {p13} LEFT ( x {op5} {p15} RIGHT ) ^2 {op6} {p16}$$/수식$$이므로 " \
              "이 그래프의 꼭짓점의 좌표는 $$수식$$LEFT ( {s1}$$/수식$$, $$수식$${s2} RIGHT )$$/수식$$이다.\n\n"

    while True:
        s1, s2, x2, x3 = random.sample(list(range(-3, 0)) + list(range(1, 4)), 4)
        if s1 != s2 and s1 != -s2:
            break
    a = random.sample(list(range(-4, 0)) + list(range(1, 5)), 1)[0]
    b = -2 * s1 * a
    c = a*s1*s1 + s2
    y1 = c
    p1 = x2 * x2
    p2 = x2
    p3 = p1 * a + p2 * b
    p4 = x3 * x3
    p5 = x3
    p6 = p4 * a + p5 * b
    y2 = p3 + y1
    y3 = p6 + y1
    if p3 != 0:
        gcd123 = abs(GCD(GCD(p1, p2), GCD(p2, p3)))
        p7, p8, p9 = int(p1/gcd123), int(p2/gcd123), int(p3/gcd123)
    else:
        gcd12 = abs(GCD(p1, p2))
        p7, p8, p9 = int(p1/gcd12), int(p2/gcd12), p3
    if p6 != 0:
        gcd456 = abs(GCD(GCD(p4, p5), GCD(p5, p6)))
        p10, p11, p12 = int(p4/gcd456), int(p5/gcd456), int(p6/gcd456)
    else:
        gcd45 = abs(GCD(p4, p5))
        p10, p11, p12 = int(p4/gcd45), int(p5/gcd45), p6
    p13 = a
    p14 = b
    p15 = -s1
    p16 = s2

    op1, op2, op3, op4, op5, op6 = '', '', '', '', '', ''
    if y1 > 0:
        op1 = '+'
    if p2 > 0:
        op2 = '+'
    if p5 > 0:
        op3 = '+'
    if p14 > 0:
        op4 = '+'
    if p15 > 0:
        op5 = '+'
    if p16 > 0:
        op6 = '+'

    if x2 == 1:
        p1 = ''
        p2 = ''
    elif x2 == -1:
        p1 = ''
        p2 = '-'
    if x3 == 1:
        p4 = ''
        p5 = ''
    elif x3 == -1:
        p4 = ''
        p5 = '-'

    if p7 == 1:
        p7 = ''
    elif p7 == -1:
        p7 = '-'
    if p8 == 1:
        p8 = ''
    elif p8 == -1:
        p8 = '-'
    if p10 == 1:
        p10 = ''
    elif p10 == -1:
        p10 = '-'
    if p11 == 1:
        p11 = ''
    else:
        p11 = '-'

    if p13 == 1:
        p13 = ''
    elif p13 == -1:
        p13 = '-'
    if p14 == 1:
        p14 = ''
    elif p14 == -1:
        p14 = '-'

    c = [[s1, s2], [-s1, s2], [s1, -s2], [-s1, -s2], [s2, s1]]
    c.sort()
    [[c1, c2], [c3, c4], [c5, c6], [c7, c8], [c9, c10]] = c
    for i in range(0, len(c)):
        if c[i] == [s1, s2]:
            s = answer_dict[i]
            break

    stem = stem.format(x2=x2, x3=x3, y1=y1, y2=y2, y3=y3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10)
    answer = answer.format(s=s)
    comment = comment.format(s1=s1, s2=s2, a=a, b=b, x2=x2, x3=x3, y1=y1, y2=y2, y3=y3, op1=op1, op2=op2, op3=op3, op4=op4, op5=op5, op6=op6,
                             p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12, p13=p13, p14=p14, p15=p15, p16=p16)

    return stem, answer, comment





# 3-1-3-257
def quadequation313_Stem_188():
    stem = "세 점 $$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x3}$$/수식$$, $$수식$${y3} RIGHT )$$/수식$$을 지나는 이차함수의 그래프의 꼭짓점의 좌표는?\n" \
           "① {c1}\t\t② {c2}\t\t③ {c3}\n" \
           "④ {c4}\t\t⑤ {c5}\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "이차함수의 식을 $$수식$$y = ax^2 + bx {op1} {y1}$$/수식$$로 놓으면 그래프가 점 " \
              "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$${y2} = {p1} a {op2} {p2} b {op1} {y1}$$/수식$$\t\t" \
              "$$수식$$THEREFORE~ {p1} a {op2} {p2} b = {p3}$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉠\n" \
              "또  점 $$수식$$LEFT ( {x3}$$/수식$$, $$수식$${y3} RIGHT )$$/수식$$를 지나므로\n" \
              "$$수식$${y3} = {p4} a {op3} {p5} b {op1} {y1}$$/수식$$\t\t" \
              "$$수식$$THEREFORE~ {p4} a {op3} {p5} b = {p6}$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉡\n" \
              "㉠, ㉡을 연립하여 풀면\n$$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$\n" \
              "따라서 $$수식$$y = {p7} x^2 {op4} {p8} x {op1} {y1} " \
              "= {p7} LEFT ( x - {p9} OVER {p10} RIGHT ) ^2 + {p11} OVER {p12}$$/수식$$이므로 " \
              "이 그래프의 꼭짓점의 좌표는 $$수식$$LEFT ( {p9} OVER {p10}$$/수식$$, $$수식$${p11} OVER {p12} RIGHT )$$/수식$$이다.\n\n"

    while True:
        a = np.random.randint(1, 6)
        p7 = a
        p10 = 2*p7
        p9 = np.random.randint(1, 8)
        if GCD(p9, p10) != 1:
            continue
        b = -p9
        p8 = b
        p12 = int(p10*p10/2)
        p11 = np.random.randint(1, 8)
        if GCD(p11, p12) != 1:
            continue
        if (p7*p9*p9 + 2*p11) % (p10*p10) == 0:
            break
    y1 = int((p7*p9*p9 + 2*p11)/(p10*p10))
    x2, x3 = random.sample(list(range(-4, -1)) + list(range(2, 5)), 2)
    p1 = x2*x2
    p2 = x2
    y2 = p1*a + p2*b + y1
    p3 = y2 - y1
    p4 = x3*x3
    p5 = x3
    y3 = p4*a + p5*b + y1
    p6 = y3 - y1

    if p7 == 1:
        p7 = ''
    if p8 == -1:
        p8 = ''

    op1, op2, op3, op4 = '', '', '', ''
    if y1 > 0:
        op1 = '+'
    if p2 > 0:
        op2 = '+'
    if p5 > 0:
        op3 = '+'

    ss = '$$수식$$LEFT ( {c1} OVER {c2}$$/수식$$, $$수식$${c3} OVER {c4} RIGHT )$$/수식$$'.format(c1=p9, c2=p10, c3=p11, c4=p12)
    c = [ss]
    c.append('$$수식$$LEFT ( {c1} OVER {c2}$$/수식$$, $$수식$${c3} OVER {c4} RIGHT )$$/수식$$'.format(c1=p9, c2=int(p10/2), c3=p11, c4=p12))
    c.append('$$수식$$LEFT ( {c1} OVER {c2}$$/수식$$, $$수식$${c3} OVER {c4} RIGHT )$$/수식$$'.format(c1=p9, c2=p10, c3=p11, c4=int(p12/2)))
    c.append('$$수식$$LEFT ( {c1} OVER {c2}$$/수식$$, $$수식$${c3} OVER {c4} RIGHT )$$/수식$$'.format(c1=p9, c2=int(p10/2), c3=p11, c4=int(p12/2)))
    c.append('$$수식$$LEFT ( {c1} OVER {c2}$$/수식$$, $$수식$${c3} OVER {c4} RIGHT )$$/수식$$'.format(c1=p9, c2=int(p10*2), c3=p11, c4=p12))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(x2=x2, x3=x3, y1=y1, y2=y2, y3=y3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(a=a, b=b, x2=x2, x3=x3, y1=y1, y2=y2, y3=y3, op1=op1, op2=op2, op3=op3, op4=op4,
                             p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12)

    return stem, answer, comment





# 3-1-3-258
def quadequation313_Stem_189():
    stem = "세 점 $$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x3}$$/수식$$, $$수식$${y3} RIGHT )$$/수식$$을 지나는 포물선을 그래프로 하는 이차함수의 식은?\n" \
           "① $$수식$${c1}$$/수식$$\t\t② $$수식$${c2}$$/수식$$\t\t③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\t\t⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "구하는 이차함수의 식을 $$수식$$y = ax^2 + bx + c$$/수식$$로 놓고\n" \
              "$$수식$$x = 0$$/수식$$, $$수식$$y = {y1}$$/수식$$을 대입하면 $$수식$$c = {y1}$$/수식$$\n" \
              "즉, $$수식$$y = ax^2 + bx {op1} {y1}$$/수식$$에" \
              "$$수식$$LEFT ($$/수식$$ⅰ$$수식$$RIGHT )$$/수식$$ " \
              "$$수식$$x = {x2}$$/수식$$, $$수식$$y = {y2}$$/수식$$을 대입하면\n" \
              "$$수식$${y2} = {p1} a {op2} {p2} b {op1} {y1}$$/수식$$\n" \
              "$$수식$$THEREFORE~ {p1} a {op2} {p2} b = {p3}$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉠\n" \
              "$$수식$$LEFT ($$/수식$$ⅱ$$수식$$RIGHT )$$/수식$$ " \
              "$$수식$$x = {x3}$$/수식$$, $$수식$$y = {y3}$$/수식$$을 대입하면\n" \
              "$$수식$${y3} = {p4} a {op3} {p5} b {op1} {y1}$$/수식$$\n" \
              "$$수식$$THEREFORE~ {p4} a {op3} {p5} b = {p6}$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉡\n" \
              "㉠, ㉡을 연립하여 풀면\n$$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$\n" \
              "따라서 구하는 이차함수의 식은 $$수식$$y = {p13} x^2 {op4} {p14} x {op1} {y1}$$/수식$$이다.\n\n"

    while True:
        s1, s2, x2, x3 = random.sample(list(range(-3, 0)) + list(range(1, 4)), 4)
        if s1 != s2 and s1 != -s2:
            break
    a = random.sample(list(range(-4, -1)) + list(range(2, 5)), 1)[0]
    b = -2 * s1 * a
    c = a * s1 * s1 + s2
    y1 = c
    p1 = x2 * x2
    p2 = x2
    p3 = p1 * a + p2 * b
    p4 = x3 * x3
    p5 = x3
    p6 = p4 * a + p5 * b
    y2 = p3 + y1
    y3 = p6 + y1

    p13 = a
    p14 = b
    p15 = -s1
    p16 = s2

    op1, op2, op3, op4, op5, op6, op7, op8 = '', '', '', '', '', '', '', ''
    if y1 > 0:
        op1 = '+'
    else:
        op8 = '+'
    if p2 > 0:
        op2 = '+'
    if p5 > 0:
        op3 = '+'
    if p14 > 0:
        op4 = '+'
    else:
        op7 = '+'
    if p15 > 0:
        op5 = '+'
    if p16 > 0:
        op6 = '+'

    if p1 == 1:
        p1, p2 = '', ''
    if p4 == 1:
        p4, p5 = '', ''

    ss = 'y = {a} x^2 {op1} {b} x {op2} {c}'.format(a=p13, op1=op4, b=p14, op2=op1, c=y1)
    c = [ss]
    c.append('y = {a} x^2 {op1} {b} x {op2} {c}'.format(a=-p13, op1=op4, b=p14, op2=op1, c=y1))
    c.append('y = {a} x^2 {op1} {b} x {op2} {c}'.format(a=p13, op1=op7, b=-p14, op2=op1, c=y1))
    c.append('y = {a} x^2 {op1} {b} x {op2} {c}'.format(a=p13, op1=op7, b=-p14, op2=op8, c=-y1))
    c.append('y = {a} x^2 {op1} {b} x {op2} {c}'.format(a=-p13, op1=op4, b=p14, op2=op8, c=-y1))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(x2=x2, x3=x3, y1=y1, y2=y2, y3=y3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(a=a, b=b, x2=x2, x3=x3, y1=y1, y2=y2, y3=y3, op1=op1, op2=op2, op3=op3, op4=op4, op5=op5, op6=op6,
                             p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p13=p13, p14=p14)

    return stem, answer, comment





# 3-1-3-261
def quadequation313_Stem_190():
    stem = "세 점 $$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x3}$$/수식$$, $$수식$${y3} RIGHT )$$/수식$$을 지나는 이차함수의 그래프와 " \
           "$$수식$$x$$/수식$$축의 두 교점을 $$수식$$A$$/수식$$, $$수식$$B$$/수식$$라 할 때, " \
           "$$수식$$BAR AB$$/수식$$의 길이는?\n" \
           "① $$수식$${c1}$$/수식$$\t\t② $$수식$${c2}$$/수식$$\t\t③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\t\t⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "이차함수의 식을 $$수식$$y = ax^2 + bx {op1} {y1}$$/수식$$으로 놓으면 그래프가 점 \n" \
              "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$${y2} RIGHT )$$/수식$$을 지나므로\n" \
              "$$수식$${y2} = {p1} a {op2} {p2} b {op1} {y1}$$/수식$$\n" \
              "$$수식$$THEREFORE~ {p1} a {op2} {p2} b = {p3}$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉠\n" \
              "또 점 $$수식$$LEFT ( {x3}$$/수식$$, $$수식$${y3} RIGHT )$$/수식$$을 지나므로\n" \
              "$$수식$${y3} = {p4} a {op3} {p5} b {op1} {y1}$$/수식$$\n" \
              "$$수식$$THEREFORE~ {p4} a {op3} {p5} b = {p6}$$/수식$$\t\t$$수식$$CDOTS CDOTS$$/수식$$㉡\n" \
              "㉠, ㉡을 연립하여 풀면\n$$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$\n" \
              "즉 $$수식$$y = {p7} x^2 {op4} {p8} x {op1} {y1}$$/수식$$이므로 $$수식$$y = 0$$/수식$$을 대입하면\n" \
              "$$수식$${p7} x^2 {op4} {p8} x {op1} {y1} = 0$$/수식$$, " \
              "$$수식$${p77} x^2 {op5} {p88} x {op6} {y11} = 0$$/수식$$\n" \
              "$$수식$$LEFT ( x + {p9} RIGHT ) LEFT ( {p77} x - {p10} RIGHT ) = 0$$/수식$$\t\t" \
              "$$수식$$THEREFORE~ x = {p99}$$/수식$$ 또는 $$수식$$x = {p10} OVER {p77}$$/수식$$\n" \
              "따라서 $$수식$$x$$/수식$$축과의 두 교점의 좌표가 $$수식$$LEFT ( {p99}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$, " \
              "$$수식$$LEFT ( {p10} OVER {p77}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$이므로\n" \
              "$$수식$$BAR AB = {p10} OVER {p77} - LEFT ( {p99} RIGHT ) = {s1} OVER {s2}$$/수식$$\n\n"

    while True:
        p9, p10, p77 = random.sample(list(range(2, 8)), 3)
        if GCD(p10, p77) != 1:
            continue
        p88 = p9*p77 - p10
        if p88 > 1:
            break

    y11 = -p10*p9
    y1 = -y11
    p7 = -p77
    p8 = -p88
    p99 = -p9

    a = p7
    b = p8
    x2, x3 = random.sample(list(range(-3, -1)) + list(range(2, 4)), 2)
    p1 = x2 * x2
    p2 = x2
    p3 = p1 * a + p2 * b
    p4 = x3 * x3
    p5 = x3
    p6 = p4 * a + p5 * b
    y2 = p3 + y1
    y3 = p6 + y1

    s1 = p10 + p77*p9
    s2 = p77
    gcd12 = GCD(s1, s2)
    s1 = int(s1/gcd12)
    s2 = int(s2/gcd12)

    op1, op2, op3, op4, op5, op6 = '', '', '', '', '', ''
    if y1 > 0:
        op1 = '+'
    if p2 > 0:
        op2 = '+'
    if p5 > 0:
        op3 = '+'
    if p8 > 0:
        op4 = '+'
    if p88 > 0:
        op5 = '+'
    if y11 > 0:
        op6 = '+'

    ss = '{s1} OVER {s2}'.format(s1=s1, s2=s2)
    c = [ss]
    c.append('{s1} OVER {s2}'.format(s1=(s1+s2), s2=s2))
    c.append('{s1}'.format(s1=int(s1/s2)))
    c.append('{s1}'.format(s1=(int(s1/s2)+1)))
    c.append('{s1}'.format(s1=(int(s1/s2)-1)))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(x2=x2, x3=x3, y1=y1, y2=y2, y3=y3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(s1=s1, s2=s2, a=a, b=b, x2=x2, x3=x3, y1=y1, y11=y11, y2=y2, y3=y3, op1=op1, op2=op2, op3=op3, op4=op4, op5=op5, op6=op6,
                             p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p77=p77, p8=p8, p88=p88, p9=p9, p99=p99, p10=p10)

    return stem, answer, comment





# 3-1-3-262
def quadequation313_Stem_191():
    stem = "$$수식$$x$$/수식$$축과 두 점 " \
           "$$수식$$LEFT ( {x1}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$에서 만나고 점 " \
           "$$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$을 지나는 포물선을 그래프로 하는 이차함수의 식을 " \
           "$$수식$$y = a LEFT ( x - p RIGHT ) ^2 + q$$/수식$$라 할 때, $$수식$$a - p + q$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${s}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$x$$/수식$$축과 두 점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$, " \
              "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$에서 만나므로 이차함수의 식을 " \
              "$$수식$$y = a LEFT ( x {op1} {x11} RIGHT ) LEFT ( x {op2} {x22} RIGHT )$$/수식$$으로 놓을 수 있다.\n" \
              "이 그래프가 점 $$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$을 지나므로\n" \
              "$$수식$${y1} = {x12} a$$/수식$$\t\t$$수식$$THEREFORE~ a = {a}$$/수식$$\n" \
              "$$수식$$THEREFORE~ y = {a} LEFT ( x {op1} {x11} RIGHT ) LEFT ( x {op2} {x22} RIGHT ) " \
              "= {a} x^2 {op3} {b} x {op4} {c}$$/수식$$\n" \
              "\t$$수식$$= {a} LEFT ( x {op5} {pp} RIGHT ) ^2 {op6} {q}$$/수식$$\n" \
              "따라서 $$수식$$p = {p}$$/수식$$, $$수식$$q = {q}$$/수식$$이므로\n" \
              "$$수식$$a - p + q = {a} {op5} {pp} {op6} {q} = {s}$$/수식$$\n\n"

    while True:
        x1, x2 = random.sample(list(range(-4, 0)) + list(range(1, 5)), 2)
        a = random.sample(list(range(-3, -1)) + list(range(2, 4)), 1)[0]
        p = int((x1 + x2)/2)
        q = a * (x1*x2 - p*p)
        if (x1 + x2) != 0 and (x1 + x2) % 2 == 0 and q != 0:
            break
    pp = -p
    x11 = -x1
    x22 = -x2
    x12 = x1*x2
    y1 = x1*x2*a
    b = 2*a*pp
    c = a*pp*pp + q
    s = a - p + q

    op1, op2, op3, op4, op5, op6 = '', '', '', '', '', ''
    if x11 > 0:
        op1 = '+'
    if x22 > 0:
        op2 = '+'
    if b > 0:
        op3 = '+'
    if c > 0:
        op4 = '+'
    if pp > 0:
        op5 = '+'
    if q > 0:
        op6 = '+'

    stem = stem.format(x1=x1, x2=x2, y1=y1)
    answer = answer.format(s=s)
    comment = comment.format(x1=x1, x2=x2, x11=x11, x22=x22, x12=x12, y1=y1, s=s, p=p, pp=pp, q=q, a=a, b=b, c=c, op1=op1, op2=op2, op3=op3, op4=op4, op5=op5, op6=op6)

    return stem, answer, comment





# 3-1-3-263
def quadequation313_Stem_192():
    stem = "이차함수 $$수식$$y = ax^2 + bx + c$$/수식$$의 그래프가 $$수식$$x$$/수식$$축과 두 점 " \
           "$$수식$$LEFT ( {x1}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$에서 만나고 $$수식$$y$$/수식$$축과 점 " \
           "$$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$에서 만날 때, $$수식$$abc$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$\t\t② $$수식$${c2}$$/수식$$\t\t③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\t\t⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = ax^2 + bx + c$$/수식$$의 그래프가 $$수식$$x$$/수식$$축과 두 점 " \
              "$$수식$$LEFT ( {x1}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$, " \
              "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$에서 만나므로 이차함수의 식을\n" \
              "$$수식$$y = a LEFT ( x {op1} {x11} RIGHT ) LEFT ( x {op2} {x22} RIGHT )$$/수식$$으로 놓을 수 있다.\n" \
              "이 그래프가 점 $$수식$$LEFT ( 0$$/수식$$, $$수식$${y1} RIGHT )$$/수식$$을 지나므로\n" \
              "$$수식$${y1} = a LEFT ( 0 {op1} {x11} RIGHT ) LEFT ( 0 {op2} {x22} RIGHT )$$/수식$$, " \
              "$$수식$${y1} = {x12} a$$/수식$$\t\t $$수식$$THEREFORE~ a = {a}$$/수식$$\n" \
              "$$수식$$THEREFORE~ y = {p1} LEFT ( x {op1} {x11} RIGHT ) LEFT ( x {op2} {x22} RIGHT ) " \
              "= {p1} x^2 {op3} {p2} x {op4} {p3}$$/수식$$\n" \
              "따라서 $$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$, $$수식$$c = {c}$$/수식$$이므로\n" \
              "$$수식$$abc = {abc}$$/수식$$\n\n"

    while True:
        x1, x2 = random.sample(list(range(-4, 0)) + list(range(1, 5)), 2)
        if (x1 + x2) != 0:
            break
    a = random.sample(list(range(-3, 0)) + list(range(1, 4)), 1)[0]
    b = -a * (x1 + x2)
    c = x1*x2*a
    x11 = -x1
    x22 = -x2
    x12 = x1*x2
    y1 = c
    p1, p2, p3 = a, b, c
    abc = a * b * c

    op1, op2, op3, op4 = '', '', '', ''
    if x11 > 0:
        op1 = '+'
    if x22 > 0:
        op2 = '+'
    if p2 > 0:
        op3 = '+'
    if p3 > 0:
        op4 = '+'

    if p1 == 1:
        p1 = ''
    elif p1 == -1:
        p1 = '-'
    if p2 == 1:
        p2 = ''
    elif p2 == -1:
        p2 = '-'

    cc = random.sample(list(range(abc - 10, abc)) + list(range(abc + 1, abc + 11)), 4)
    cc.append(abc)
    cc.sort()
    c1, c2, c3, c4, c5 = cc
    for i in range(0, len(cc)):
        if cc[i] == abc:
            s = answer_dict[i]
            break

    stem = stem.format(x1=x1, x2=x2, y1=y1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(x1=x1, x2=x2, x11=x11, x22=x22, x12=x12, y1=y1, a=a, b=b, c=c, abc=abc, op1=op1, op2=op2, op3=op3, op4=op4, p1=p1, p2=p2, p3=p3)

    return stem, answer, comment





# 3-1-3-264
def quadequation313_Stem_193():
    stem = "이차함수 $$수식$$y = {p1} x^2$$/수식$$의 그래프와 모양이 같고, " \
           "$$수식$$x$$/수식$$축과의 두 교점의 좌표가 $$수식$${x1}$$/수식$$, $$수식$${x2}$$/수식$$인 " \
           "포물선을 그래프로 하는 이차함수의 식은?\n" \
           "① $$수식$${c1}$$/수식$$\t\t② $$수식$${c2}$$/수식$$\t\t③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\t\t⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "$$수식$$y = {p1} LEFT ( x {op1} {x11} RIGHT ) LEFT ( x {op2} {x22} RIGHT ) " \
              "= {p1} x^2 {op3} {p2} x {op4} {p3}$$/수식$$\n\n"

    while True:
        x1, x2 = random.sample(list(range(-4, 0)) + list(range(1, 5)), 2)
        if (x1 + x2) != 0:
            break
    a = random.sample(list(range(-4, -1)) + list(range(2, 5)), 1)[0]
    b = -a * (x1 + x2)
    c = x1*x2*a
    x11 = -x1
    x22 = -x2
    p1, p2, p3 = a, b, c

    op1, op2, op3, op4, op5, op6 = '', '', '', '', '', ''
    if x11 > 0:
        op1 = '+'
    if x22 > 0:
        op2 = '+'
    if p2 > 0:
        op3 = '+'
    else:
        op5 = '+'
    if p3 > 0:
        op4 = '+'
    else:
        op6 = '+'

    ss = '{p1} x^2 {op3} {p2} x {op4} {p3}'.format(p1=p1, p2=p2, p3=p3, op3=op3, op4=op4)
    cc = [ss]
    cc.append('{p1} x^2 {op3} {p2} x {op4} {p3}'.format(p1=p1, p2=-p2, p3=p3, op3=op5, op4=op4))
    cc.append('{p1} x^2 {op3} {p2} x {op4} {p3}'.format(p1=p1, p2=p2, p3=-p3, op3=op3, op4=op6))
    cc.append('{q1} OVER {q2} x^2 {op3} {p2} x {op4} {p3}'.format(q1=1, q2=abs(p1), p2=-p2, p3=p3, op3=op5, op4=op4))
    cc.append('{q1} OVER {q2} x^2 {op3} {p2} x {op4} {p3}'.format(q1=1, q2=abs(p1), p2=-p2, p3=-p3, op3=op5, op4=op6))
    np.random.shuffle(cc)
    c1, c2, c3, c4, c5 = cc
    for i in range(0, len(cc)):
        if cc[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, x1=x1, x2=x2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(x11=x11, x22=x22, op1=op1, op2=op2, op3=op3, op4=op4, p1=p1, p2=p2, p3=p3)

    return stem, answer, comment





# 3-1-3-267
def quadequation313_Stem_194():
    stem = "두 점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$, " \
           "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$을 지나고 꼭짓점의 $$수식$$y$$/수식$$좌표가 " \
           "$$수식$${y1}$$/수식$$인 포물선을 그래프로 하는 이차함수의 식은?\n" \
           "① $$수식$${c1}$$/수식$$\t\t② $$수식$${c2}$$/수식$$\t\t③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\t\t⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "두 점 $$수식$$LEFT ( {x1}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$, " \
              "$$수식$$LEFT ( {x2}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$을 지나므로 구하는 이차함수의 식을 " \
              "$$수식$$y = a LEFT ( x {op1} {x11} RIGHT ) LEFT ( x {op2} {x22} RIGHT )$$/수식$$으로 놓으면\n" \
              "$$수식$$y = a LEFT ( x {op1} {x11} RIGHT ) LEFT ( x {op2} {x22} RIGHT ) " \
              "= a LEFT ( x^2 {op3} {p2} x {op4} {p3} RIGHT )$$/수식$$\n" \
              "  $$수식$$= a LEFT ( x {op3} {p4} RIGHT ) ^2 {op5} {p5} a$$/수식$$\n" \
              "이 때 꼭짓점의 $$수식$$y$$/수식$$좌표가 $$수식$${y1}$$/수식$$이므로\n" \
              "$$수식$${p5} a = {y1}$$/수식$$\t\t$$수식$$THEREFORE~ a = {a}$$/수식$$\n" \
              "$$수식$$THEREFORE y = {p1} LEFT ( x^2 {op3} {p2} x {op4} {p3} RIGHT ) " \
              "= {p1} x^2 {op6} {p6} x {op7} {p7}$$/수식$$\n\n"

    while True:
        x1, x2 = random.sample(list(range(-4, 0)) + list(range(1, 5)), 2)
        p2 = -(x1 + x2)
        p3 = x1 * x2
        p4 = int(p2 / 2)
        p5 = p3 - p4*p4
        if (x1 + x2) != 0 and (x1 + x2) % 2 == 0 and p5 != 0:
            break
    a = random.sample(list(range(-4, -1)) + list(range(2, 5)), 1)[0]
    b = -a * (x1 + x2)
    c = x1*x2*a
    x11 = -x1
    x22 = -x2
    y1 = p5 * a
    p1, p6, p7 = a, b, c

    op1, op2, op3, op4, op5, op6, op7, op8, op9 = '', '', '', '', '', '', '', '', ''
    if x11 > 0:
        op1 = '+'
    if x22 > 0:
        op2 = '+'
    if p2 > 0:
        op3 = '+'
    if p3 > 0:
        op4 = '+'
    if p5 > 0:
        op5 = '+'
    if p6 > 0:
        op6 = '+'
    else:
        op8 = '+'
    if p7 > 0:
        op7 = '+'
    else:
        op9 = '+'

    if p5 == 1:
        p5 = ''
    elif p5 == -1:
        p5 = '-'
    if p2 == 1:
        p2 = ''
    elif p2 == -1:
        p2 = '-'

    p11, p66 = -p1, -p6
    if p1 == 1:
        p1, p11 = '', '-'
    elif p1 == -1:
        p1, p11 = '-', ''
    if p6 == 1:
        p6, p66 = '', '-'
    elif p6 == -1:
        p6, p66 = '-', ''

    ss = '{p1} x^2 {op6} {p6} x {op7} {p7}'.format(p1=p1, p6=p6, p7=p7, op6=op6, op7=op7)
    cc = [ss]
    cc.append('{p1} x^2 {op6} {p6} x {op7} {p7}'.format(p1=p11, p6=p6, p7=p7, op6=op6, op7=op7))
    cc.append('{p1} x^2 {op6} {p6} x {op7} {p7}'.format(p1=p11, p6=p66, p7=p7, op6=op8, op7=op7))
    cc.append('{p1} x^2 {op6} {p6} x {op7} {p7}'.format(p1=p11, p6=p6, p7=-p7, op6=op6, op7=op9))
    cc.append('{p1} x^2 {op6} {p6} x {op7} {p7}'.format(p1=p1, p6=p66, p7=p7, op6=op8, op7=op7))
    np.random.shuffle(cc)
    c1, c2, c3, c4, c5 = cc
    for i in range(0, len(cc)):
        if cc[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, x1=x1, x2=x2, y1=y1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(a=a, x1=x1, x2=x2, y1=y1, x11=x11, x22=x22, op1=op1, op2=op2, op3=op3, op4=op4, op5=op5, op6=op6, op7=op7,
                             p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7)

    return stem, answer, comment





# 3-1-3-269
def quadequation313_Stem_195():
    stem = "이차함수 $$수식$$y = x^2 + ax + b$$/수식$$의 그래프는 $$수식$$y$$/수식$$축을 축으로 하고, " \
           "$$수식$$x$$/수식$$축과 만나는 두 점 사이의 거리가 $$수식$${dist}$$/수식$$이다. 이때 상수 " \
           "$$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$a + b$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$\t\t② $$수식$${c2}$$/수식$$\t\t③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\t\t⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답): {s}\n"
    comment = "(해설)\n" \
              "이차함수 $$수식$$y = x^2 + ax + b$$/수식$$의 그래프가 $$수식$$x$$/수식$$축과 두 점 " \
              "$$수식$$LEFT ( - {x1}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$, " \
              "$$수식$$LEFT ( {x1}$$/수식$$, $$수식$$0 RIGHT )$$/수식$$에서 만나므로\n" \
              "$$수식$$y = LEFT ( x + {x1} RIGHT ) LEFT ( x - {x1} RIGHT ) = x^2 - {x2}$$/수식$$\n" \
              "즉 $$수식$$a = 0$$/수식$$, $$수식$$b = - {x2}$$/수식$$이므로 $$수식$$a + b = {ss}$$/수식$$\n\n"

    x1 = np.random.randint(1, 8)
    x2 = x1*x1
    dist = 2*x1
    ss = -x2
    cc = random.sample(list(range(ss-5, ss))+list(range(ss+1, ss+6)), 4)
    cc.append(ss)
    cc.sort()
    c1, c2, c3, c4, c5 = cc
    for i in range(0, len(cc)):
        if cc[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(dist=dist, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(x1=x1, x2=x2, ss=ss)

    return stem, answer, comment