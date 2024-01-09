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


#소인수분해 함수(?)
def factor_equation(num):
    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = ""
    if len(temp1) > 0:
        for i in range(len(temp1) - 1):
            if exp1[i]!=1:
                fact_ = fact_ + "$$수식$${" + str(temp1[i]) + "} ^{" + str(exp1[i]) + "} TIMES$$/수식$$"
            else:
                fact_ = fact_ + "$$수식$${" + str(temp1[i]) + "} TIMES$$/수식$$"
        if exp1[-1] != 1:
            fact_ = fact_ + "$$수식$${" + str(temp1[-1]) + "} ^{" + str(exp1[-1]) + "}$$/수식$$"
        else:
            fact_ = fact_ + "$$수식$${" + str(temp1[-1])  + "}$$/수식$$"
    return fact_

def factor_power(num):
    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    return exp1

def factor_factors(num):
    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    return temp1
def gcd (a, b):
    if b == 0:
        return a
    else :
        if a < b:
            a, b = b, a
        return gcd(b, a % b)





def lcm(a, b):
    return a * b // gcd(a, b)


#중1-1-1-01
def naturalnum111_Stem_001():
    stem = "다음 중 소수는 모두 몇 개인지 구하시오.\n"\
            "$$표$$ $$수식$${aa1}$$/수식$$ $$/표$$ \n"
    answer = "(답): " \
             "$$수식$${ans}$$/수식$$ 개 "
    comment = "(해설)\n" \
              "소수는 $$수식$${aa2}$$/수식$$ 의 $$수식$${ans}$$/수식$$개이다.\n"

    aa = []
    while len(aa)< 10:
        k = np.random.randint(1, 100)
        if k not in aa:
            aa.append(k)
    aa.sort()

    prime = []
    for i in range(len(aa)):
        div = 0
        for j in range(2, aa[i]):
            if aa[i] % j == 0:
                div += 1
        if div == 0 and aa[i] > 1:
            prime.append(aa[i])

    ans = len(prime)

    aa1 = ""
    for i in range (len(aa)-1):
        aa1 = aa1 + str(aa[i]) + "``"
    aa1 = aa1 + str(aa[-1]) + " `` "
    aa2=""
    for i in range(len(prime)-1):
        aa2 = aa2 +  str(prime[i]) + ", "
    if len(prime) > 0:
        aa2 = aa2 + str(prime[-1]) + "``  "

    stem = stem.format(aa1=aa1)
    answer = answer.format(ans=ans)
    comment = comment.format(aa2=aa2, ans=ans)

    return stem, answer, comment


#중1-1-1-03
def naturalnum111_Stem_002():
    stem = "다음 중 소수의 개수를 $$수식$$a$$/수식$$, 합성수의 개수를 $$수식$$b$$/수식$$라 할 때, $$수식$$b-a$$/수식$$의 값을 구하시오.\n$$표$$$$수식$${aa1}$$/수식$$ $$/표$$\n"
    answer = "(답):" \
             "$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "소수는 $$수식$${prime_string}$$/수식$$의 $$수식$${prime_number}$$/수식$$개이므로 \n$$수식$$a `= `{prime_number}$$/수식$$\n" \
              "합성수는 $$수식$${not_prime_string}$$/수식$$\n의 $$수식$${not_prime_num}$$/수식$$개이므로 $$수식$$b` =` {not_prime_num}$$/수식$$\n" \
              "$$수식$$b`-`a `= `{ans}$$/수식$$"
# 해설에선 b-a = -3이여하지만 b-a=3으로 잘못 되어잇음
    aa = []
    while len(aa) < 10:
        k = np.random.randint(1, 100)
        if k not in aa:
            aa.append(k)
    aa.sort()
    aa1 = ""
    for i in range(len(aa) - 1):
        aa1 = aa1 + str(aa[i]) + ", "

    aa1 = aa1 + str(aa[-1])

    prime = []
    not_prime =[]

    for i in range(len(aa)):
        if aa[i] > 1:
            div = 0
            for j in range(2, aa[i]):
                if aa[i] % j == 0:
                    div += 1
            if div == 0:
                prime.append(aa[i])
            else:
                not_prime.append(aa[i])
    a = len(prime)
    b = len(not_prime)

    ques = "①"
    boxone = "box{````%d````}"
    boxtwo = "box{````%d````}"
    prime_string = ""

    if len(prime) > 0:
        if len(prime) > 1:
            for i in range(len(prime) - 1):
                prime_string = prime_string + str(prime[i]) + ", "

        prime_string = prime_string + str(prime[-1])
    not_prime_string = ""
    if len(not_prime) > 0:
        if len(not_prime) > 1:
            for i in range(len(not_prime) - 1):
                not_prime_string = not_prime_string  + str(not_prime[i]) + ", "

        not_prime_string = not_prime_string  + str(not_prime[-1])
    ans = b-a

    stem = stem.format(aa1=aa1, ques=ques)
    answer = answer.format(ans=ans)
    comment = comment.format(prime_string=prime_string, prime_number=a, not_prime_string=not_prime_string, not_prime_num=b, ans=ans)

    return stem, answer, comment


#중1-1-1-04

def naturalnum111_Stem_003():
    stem = "" \
           "$$수식$${num}$$/수식$$ 미만의 자연수 중 합성수의 개수는? ① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(답):" \
             "{ans}"
    comment = "(해설)\n" \
              "$$수식$${num}$$/수식$$ 미만의 자연수 중 합성수는 \n$$수식$${not_prime_string}$$/수식$$의 $$수식$${answ}$$/수식$$개이다.\n"

    num = np.random.randint(5, 30)
    prime = []
    not_prime = []
    for i in range(2, num):
        div = 0
        for j in range(2, i):
            if (i % j) == 0:
                not_prime.append(i)
                div += 1
                break
        if div == 0:
            prime.append(i)
    not_prime_string=""
    for i in range (len(not_prime)-1):
        not_prime_string = not_prime_string + str(not_prime[i]) + ", "


    not_prime_string = not_prime_string + str(not_prime[-1])
    bb=[]
    answ = len(not_prime)
    while len(bb) < 4:
        k = np.random.randint(0, num)
        if k not in bb and k!=answ:
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

    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, answ=answ, not_prime_string=not_prime_string)

    return stem, answer, comment


#중1-1-1-05
def naturalnum111_Stem_004():
    stem = "" \
           "$$수식$${num}$$/수식$$ 미만의 자연수 중 가장 큰 소수와 가장 작은 소수의 합은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):" \
             "{ans}"
    comment = "(해설)\n" \
              "$$수식$${num}$$/수식$$ 미만의 자연수 중 가장 큰 소수는 $$수식$${big}$$/수식$$이고 가장 작은 소수는$$수식$$ `2$$/수식$$이므로 구하는 합은 \n" \
              "$$수식$${big}+2={answ}$$/수식$$\n"

    num = np.random.randint(10, 100)
    big = 0
    for i in range(2, num):
        div = 0
        for j in range(2,i):
            if i % j == 0:
                div += 1
                break
        if div == 0:
            big = i

    answ = big+2
    bb = []
    while len(bb) < 4:
        k = np.random.randint(0, num)
        if k not in bb and k!=answ:
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

    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, answ=answ, big=big)

    return stem, answer, comment

#중1-1-1-06

def naturalnum111_Stem_005():
    stem = "다음 보기에서 자연수에 대한 설명으로 옳은 것만 있는 대로 고른 것은?\n" \
           "$$표$$㉠ 가장 작은 소수는 $$수식$$2$$/수식$$이다.\n㉡ 모든 소수의 약수는 $$수식$$2$$/수식$$개이다.\n㉢ $$수식$${num}$$/수식$$ 이하의 소수는 $$수식$${not_true}$$/수식$$개이다.\n㉣ 자연수는 " \
           "$$수식$$1$$/수식$$, 소수, 합성수로 이루어져 있다.$$/표$$① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(답):" \
             "{ans}"
    comment = "(해설)\n" \
              "㉢ $$수식$${x1}$$/수식$$이하의 소수는 $$수식$${prime_string}$$/수식$$\n의 $$수식$${prime_num}$$/수식$$개이다. 따라서 옳은 것은 ㉠, ㉡, ㉣이다.\n"

    ans = "④"
    num = np.random.randint(11, 100)
    prime =[]
    not_true =0
    for i in range(2,num+1):
        div = 0
        for j in range(2,i):
            if i % j == 0:
                div += 1
                break
        if div == 0:
            prime.append(i)
    if np.random.randint(0,2) == 0:
        not_true = len(prime) + np.random.randint(1,2)
    else:
        not_true = len(prime) - np.random.randint(1, 2)

    prime_string = ""
    for i in range(len(prime) - 1):
        prime_string = prime_string + str(prime[i]) + ", "

    prime_string = prime_string + str(prime[-1])
    bb=[]
    bb.append("㉠, ㉡")
    bb.append("㉠, ㉣")
    bb.append("㉠, ㉡, ㉢")
    answ = "㉠, ㉡, ㉣ "
    bb.append("㉡, ㉢, ㉣")
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

    stem = stem.format(num=num, not_true=not_true,x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(x1=num, prime_string=prime_string, prime_num=len(prime))

    return stem, answer, comment


#중1-1-1-07

def naturalnum111_Stem_006():
    stem = "자연수 $$수식$$x$$/수식$$보다 작은 수 중 가장 큰 소수를 {left}$$수식$$x$$/수식$${right}로 타내기로 할때, {left}$$수식$$x$$/수식$${right}$$수식$$= {num}$$/수식$${temp} " \
           "만족시키는 자연수 $$수식$$x$$/수식$$의 개수는?① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(답):\n" \
             "{ans}"
    comment = "(해설)\n" \
              "$$수식$${num}$$/수식$$보단 큰 소수 중 가장 작은 소수는 $$수식$${first}$$/수식$$이다.\n" \
              "따라서 {left}$$수식$$x$$/수식$${right} = $$수식$${num}$$/수식$${temp} 만족시키는 자연수는 $$수식$$x$$/수식$$는 \n$$수식$${not_prime_string}$$/수식$$\n이므로 " \
              "구하는 개수는 $$수식$${answ}$$/수식$$이다. \n"
    x="x"
    fac = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    k=np.random.randint(10, 24)
    num = fac[k]
    not_prime = []
    first=0
    for i in range(num+1, 102):
        div = 0
        for j in range(2, i):
            if i % j == 0:
                div += 1
        if div == 0:
            first = i
            break
        else:
            not_prime.append(i)
    answ = len(not_prime)
    not_prime_string=""
    if len(not_prime) > 0:
        if len(not_prime) > 1:
            for i in range(len(not_prime) - 1):
                not_prime_string = not_prime_string + str(not_prime[i]) + ", "

        not_prime_string = not_prime_string + str(not_prime[-1])

    bb = []
    while len(bb) < 4:
        k = np.random.randint(0, 10)
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

    temp = proc_jo(num, 4)
    left = "{"
    right ="}"
    stem = stem.format(left=left,right=right,x=x, num=num, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(left=left,right=right,x=x, num=num, first=first, temp=temp, not_prime_string=not_prime_string, answ=answ)

    return stem, answer, comment


#중1-1-1-08

def naturalnum111_Stem_007():
    stem = "다음 조건을 모두 만족시키는 자연수 $$수식$$n$$/수식$$의 개수는?\n $$표$$(가) $$수식$$n$$/수식$$은 $$수식$${low}$$/수식$$보다 작고 $$수식$${high}$$/수식$$" \
           "보다 작은 자연수이다.\n(나) $$수식$$n$$/수식$$의 모든 약수의 합은 $$수식$$n+1$$/수식$$이다. $$/표$$① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$"
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "조건 (나)에서 자연수 $$수식$$n$$/수식$$의 모든 약수의 합이 $$수식$$n+1$$/수식$$이므로 $$수식$$n$$/수식$$의 약수는 $$수식$$1`,` n`$$/수식$$이다.\n" \
              "따라서 조건 (가)에 의하여 $$수식$$n$$/수식$$은 $$수식$${low}$$/수식$$보다 작고 $$수식$${high}$$/수식$$" \
              "보다 작은 소수이므로 $$수식$$n$$/수식$$의 개수는 $$수식$${prime_string}$$/수식$$ 의 $$수식$${answ}$$/수식$$이다. \n"

    low = np.random.randint(1, 50)
    high = np.random.randint(low+1, 100)
    prime =[]
    for i in range(low, high+1):
        div = 0
        for j in range(2,i):
            if i % j == 0:
                div += 1
                break
        if div == 0:
            prime.append(i)
    if 1 in prime:
        prime.remove(1)
    answ = len(prime)
    prime_string = ""
    if len(prime) > 0:
        if len(prime) > 1:
            for i in range(len(prime) - 1):
                prime_string = prime_string + str(prime[i]) + ",  "

        prime_string = prime_string + str(prime[-1])
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

    stem = stem.format(low=low, high=high, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(low=low, high=high,prime_string=prime_string, answ=answ)

    return stem, answer, comment
#중1-1-1-11
def naturalnum111_Stem_008():
    stem = "$$수식$${eq1}$$/수식$$, $$수식$${one} over {bunmo} = {one} over {ans2}$$/수식$${temp} 만족시키는 자연수 $$수식$$`a`, `b`$$/수식$$에 " \
           "대하여 $$수식$$a-b$$/수식$$의 값은?① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$"
    answer = "(답):{ans}"
    comment = "(해설)" \
              "\n$$수식$${num1} ^{a}$$/수식$$ = $$수식$${ans1}$$/수식$$ \n$$수식$$ {one} over {bunmo1}$$/수식$$ = $$수식$$ {one} over {ans2}$$/수식$$이므로\n$$수식$$a `= `{a}$$/수식$$, $$수식$$b `= `{b}$$/수식$$\n" \
              "$$수식$$a `- `b` =` {a}$$/수식$$ - $$수식$${b}$$/수식$$ = $$수식$${answ}$$/수식$$"
    num1 = np.random.randint(3, 10)
    num2 = np.random.randint(3, 10)
    while num1==num2:
        num2 = np.random.randint(3, 10)
    a = np.random.randint(3, 6)
    b = np.random.randint(3, 6)

    while num1**a > 100:
        a = np.random.randint(2, 6)
    while num2**b > 100:
        b = np.random.randint(2, 6)
    answ = a-b

    ans1 = num1**a
    ans2 = num2**b

    bb = []
    while len(bb) < 4:
        k = np.random.randint(0, 10)
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
    temp = proc_jo(ans2, 4)
    five=5
    one=1
    bunmo = "{%d^b}"%num2
    part = "%d^"+str(b)
    bunmo1="{{%d}^{%d}}"%(num2,b)
    #bunmo1 = part%num2
    eq1 ="$$수식$${"+str(num1)+"} ^{a}$$/수식$$ = $$수식$${"+str(ans1)+"}$$/수식$$"
    eq2 = "$$수식$$ {"+str(1)+"} over $$수식$${"+str(ans2)+"}$$/수식$$ $$/수식$$"
    eq11 ="$$수식$${num1} ^{"+str(a)+"}$$/수식$$ = $$수식$${"+str(ans1)+"}$$/수식$$"
    eq21 = str(1)+ "$$수식$$over {"+str(num2)+"} ^{"+str(b)+"}$$/수식$$ $$/수식$$ = $$수식$${1} $$수식$$over {"+str(ans2)+"}$$/수식$$ $$/수식$$"

    stem = stem.format(one=one, bunmo=bunmo,a="a", b="b", ans2=ans2, eq2=eq2, eq1=eq1, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(one=one,bunmo=bunmo, bunmo1=bunmo1, num1=num1, eq1=eq11,a=a, eq2=eq21,b=b,ans1=ans1, ans2=ans2, answ=answ)

    return stem, answer, comment

#중1-1-1-12

def naturalnum111_Stem_009():
    stem = "$$수식$${equ} `=` {a} ^{x} TIMES {b} ^{y} TIMES {c} ^{z}$$/수식$${temp} 만" \
           "족 시키는 자연수 $$수식$$`x`, `y`, `z$$/수식$$에 대하여 $$수식$$y+z-x$$/수식$$의 " \
           "값은? (단 $$수식$$a, `b,` c$$/수식$$는 다른 소수이다.) ① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${equ} `=`$$/수식$$ " \
              "$$수식$${a} ^{ans1} TIMES {b} ^{ans2} TIMES {c} ^{ans3}$$/수식$$이므로\n" \
              "$$수식$$x `= `{ans1}$$/수식$$, $$수식$$y `=` {ans2}$$/수식$$, $$수식$$z` =` {ans3}$$/수식$$\n" \
              "$$수식$$y+z-x `=` {answ}$$/수식$$"
    a="a"
    b="b"
    x="x"
    y="y"
    c ="c"
    z="z"
    fac = [2, 3]
    ans1 = fac[np.random.randint(0, 2)]
    ans2 = fac[np.random.randint(0, 2)]
    ans3 = fac[np.random.randint(0, 2)]
    one = two = three =0
    answ = ans2 + ans3 - ans1
    lis=[]
    while one+two+three < ans1+ans2+ans3:
        if one < ans1 and np.random.randint(0, 2) == 0:
            lis.append("a")
            one+=1
        elif two < ans2 and np.random.randint(0, 2) == 0:
            lis.append("b")
            two+=1
        elif three < ans3 and np.random.randint(0, 2) == 0:
            lis.append("c")
            three+=1
    equ=""
    for i in range(len(lis)-1):
        equ = equ + lis[i] + " TIMES "
    equ = equ + lis[len(lis)-1] + ""

    temp =  proc_jo(ans3, 4)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(0, 10)
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
    stem = stem.format(a=a,x=x,y=y,z=z,c=c,b=b, equ=equ, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(a=a,c=c,b=b,equ=equ, ans1=ans1, ans2=ans2, ans3=ans3, answ=answ)

    return stem, answer, comment


#중1-1-1-13
def naturalnum111_Stem_010():
    stem = "$$수식$${num1} ^{ep1}$$/수식$$ + $$수식$${num2} ^{ep2}$$/수식$$의 일의 자리의 숫자는?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n"
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "(i) $$수식$${list} CDOTS$$/수식$$ 이므로 $$수식$${num1}$$/수식$$의 거듭제곱의 일의 자리의" \
              "숫자는 $$수식$${one_list_string}$$/수식$$이 반복된다. \n" \
              "이때 $$수식$${ep1}$$/수식$$ = $$수식$${ep11} TIMES {ep12}$$/수식$$이므로 $$수식$${num1} ^{ep1}$$/수식$$" \
              "의 일의 자리의 숫자는 $$수식$${num1} ^{ep11}$$/수식$$의 일의 자리의 숫자와 같은 $$수식$${last1}$$/수식$$이다.\n" \
              "(ii) $$수식$${list2} CDOTS$$/수식$$이므로 $$수식$${num2}$$/수식$$의 거듭제곱의 일의 자리의" \
              "숫자는 $$수식$${two_list_string}$$/수식$$이 반복된다. \n" \
              "이때 $$수식$${ep2}$$/수식$$ = $$수식$${ep21} TIMES {ep22}$$/수식$$이므로 $$수식$${num2} ^{ep2}$$/수식$$" \
              "의 일의 자리의 숫자는 $$수식$${num2} ^{ep21}$$/수식$$의 일의 자리의 숫자와 같은 $$수식$${last2}$$/수식$$이다.\n" \
              "(i), (ii)에서 $$수식$${num1} ^{ep1}$$/수식$$ + $$수식$${num2} ^{ep2}$$/수식$$의 일의 자리의 숫자는 " \
              "$$수식$${last1}$$/수식$$ + $$수식$${last2}$$/수식$$ = $$수식$${answ11}$$/수식$$"

    num1 = np.random.randint(1, 10)
    num2 = np.random.randint(1, 10)
    ep1 = np.random.randint(100, 400)
    ep2 = np.random.randint(100, 400)
    k=num1
    j=num2
    one_list =[k]
    two_list = [j]
    i = 2
    while True:
        l = k**i
        while l > 10:
            l = l % 10
        if l not in one_list:
            one_list.append(l)
        else:
            break
        i += 1

    while True:
        l = j**i
        while l > 10:
            l = l % 10
        if l not in two_list:
            two_list.append(l)
        else:
            break
        i+=1


    ep11 = len(one_list)
    ep21 = len(two_list)

    remainder1 = ep1 % ep11
    ep12 = int(ep1 / ep11)
    remainder2 = ep2 % ep21
    ep22 = int(ep2 / ep21)
    last1 = last2=0
    ep13 = str(ep12)
    ep23= str(ep22)
    if remainder1 != 0:
        last1 = one_list[remainder1-1]
        ep13 = str(ep12) +" + "+ str(remainder1)
    else:
        last1 = one_list[-1]
    if remainder2 != 0:
        last2 = two_list[remainder2-1]
        ep23 = str(ep22) + "+" + str(remainder2)
    else:
        last2 = two_list[-1]
    answ1 = last1 + last2
    answ11=""
    answ=""
    if answ1 >= 10:
        answ1 = answ1 % 10
        answ11 = str(last1+last2) + " - " + str(10) + " = " + str(answ1)
        answ = str(answ1)
    else:
        answ11 = str(answ1)
        answ = str(answ1)
    one_list_string=""
    if len(one_list) > 0:
        if len(one_list) > 1:
            for i in range(len(one_list)-1):
                one_list_string = one_list_string + str(one_list[i]) +", "
        one_list_string = one_list_string + str(one_list[-1])
    two_list_string=""
    if len(two_list) > 0:
        if len(two_list) > 1:
            for i in range(len(two_list)-1):
                two_list_string = two_list_string + str(two_list[i]) +", "
        two_list_string = two_list_string + str(two_list[-1])
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ1 + k
        else:
            k = abs(answ1 - k)
        if k not in bb and k != answ1:
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

    list ="$$수식$${"+str(num1)+"} ^{"+str(1)+"}$$/수식$$ = $$수식$${"+str(num1**1)+"}$$/수식$$, $$수식$${"+str(num1)+"} ^{"+str(2)+"}$$/수식$$ = $$수식$${"+str(num1**2)+"}$$/수식$$" \
              ", $$수식$${"+str(num1)+"} ^{"+str(3)+"}$$/수식$$ = $$수식$${"+str(num1**3)+"}$$/수식$$, $$수식$${"+str(num1)+"} ^{"+str(4)+"}$$/수식$$ = $$수식$${"+str(num1**4)+"}$$/수식$$" \
              ", $$수식$${"+str(num1)+"} ^{"+str(5)+"}$$/수식$$ = $$수식$${"+str(num1**5)+"}$$/수식$$"
    list2 ="$$수식$${"+str(num2)+"} ^{"+str(1)+"}$$/수식$$ = $$수식$${"+str(num2)+"}$$/수식$$, $$수식$${"+str(num2)+"} ^{"+str(2)+"}$$/수식$$ = $$수식$${"+str(num2**2)+"}$$/수식$$" \
              ", $$수식$${"+str(num2)+"} ^{"+str(3)+"}$$/수식$$ = $$수식$${"+str(num2**3)+"}$$/수식$$, $$수식$${"+str(num2)+"} ^{"+str(4)+"}$$/수식$$ = $$수식$${"+str(num2**4)+"}$$/수식$$, " \
              ", $$수식$${"+str(num2)+"} ^{"+str(5)+"}$$/수식$$ = $$수식$${"+str(num2**5)+"}$$/수식$$"
    stem = stem.format(num1=num1,num2=num2, ep1=ep1, ep2=ep2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ11=answ11, list=list, list2=list2, num1=num1, ep1=ep1, ep11=ep11, ep12=ep13, one_list_string=one_list_string, last1=last1, last2=last2, num2=num2,  two_list_string=two_list_string, ep2=ep2, ep21=ep21, ep22=ep23, answ=answ)

    return stem, answer, comment
#중1-1-1-14
def naturalnum111_Stem_011():
    stem = "다음과 같이 2보다 큰 자연수 $$수식$$x$$/수식$$에 대하여 $$수식$$f(x)$$/수식$$를 약속할 때, $$수식$$f$$/수식$$($$수식$${num1}$$/수식$$) + $$수식$$f({num2}$$/수식$$)의 값은?\n" \
           "$$표$$(가) $$수식$$f(x)$$/수식$$는 $$수식$$x$$/수식$$의 소인수들의 합이다.\n(나) 같은 소인수가 여러 번 곱해져 있으면 곱한 개수만큼 더한다.\n" \
           "예를 들어 $$수식$${six}$$/수식$$ = $$수식$${two} ^{two} TIMES {three} ^{two}$$/수식$$ 이므로 \n" \
           "$$수식$$f({six}) = {two} + {two} + {three} + {three} = {ten}$$/수식$$$$/표$$\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답): {ans}"
    comment = "(해설)\n" \
              "$$수식$${num1}$$/수식$$ = {eq11} 이므로\n" \
              "$$수식$$f({num1}$$/수식$$) = $$수식$${eq12}$$/수식$$ = $$수식$${ans1}$$/수식$$\n" \
              "$$수식$${num2}$$/수식$$ = {eq21} 이므로\n" \
              "$$수식$$f({num2}$$/수식$$) = $$수식$${eq22}$$/수식$$ = $$수식$${ans2}$$/수식$$\n" \
              "∴$$수식$$f({num1}$$/수식$$) + $$수식$$f({num2}$$/수식$$) = $$수식$${ans1}$$/수식$$ + $$수식$${ans2}$$/수식$$ = $$수식$${answ}$$/수식$$"
    six = 36
    two = 2
    three = 3
    ten = 10

    num1 = np.random.randint(1, 149)
    num_one=[]
    num2 = np.random.randint(1, 149)
    num_two = []

    i = 2
    n=num1
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1

    i=2
    n=num2
    while n > 1:
        if n % i == 0:
            num_two.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    num_two.sort()
    ans1=0
    for x in num_one:
        ans1 = ans1 + x

    ans2=0
    for x in num_two:
        ans2 = ans2 + x
    answ = ans1 + ans2

    eq12 =""
    eq22=""
    if len(num_one)>0:
        for i in range(len(num_one)-1):
            eq12 = eq12 + str(num_one[i]) + "+"
        eq12 = eq12 + str(num_one[-1]) + ""
    if len(num_two)>0:
        for i in range(len(num_two)-1):
            eq22 = eq22 + str(num_two[i]) + "+"
        eq22 = eq22 + str(num_two[-1]) + ""

    exp11 = factor_equation(num1)

    exp21 = factor_equation(num2)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(0, 50)
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

    stem = stem.format(num1=num1, num2=num2, six=six, two=two, ten=ten, three=three, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num1=num1, num2=num2, eq11=exp11, eq12=eq12, ans1=ans1, ans2=ans2, eq21=exp21, eq22=eq22, answ=answ)

    return stem, answer, comment

#중1-1-1-15
def naturalnum111_Stem_012():
    stem = "한 덩어리의 밀가루 반죽을 손으로 길게 잡아당겨 한번 접고 다시 잡아당겨 접는 일을 반복하여 수" \
           "타면을 만들려고 한다. 한번 접으면 면은 $$수식$$2$$/수식$$가닥이 되고, 두 번 접으면 $$수식$$4$$/수식$$가닥이 된다고 할때," \
           "$$수식$${num}$$/수식$$가닥의 면을 만들려면 밀가루 반죽을 몇 번 접어야 하는가?" \
            "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$$1$$/수식$$ 번 접었을 때 면의 가닥 수는 $$수식$$2 `=` {two} ^ {one}$$/수식$$\n" \
              "$$수식$$2$$/수식$$ 번 접었을 때 면의 가닥 수는 $$수식$$2 `TIMES`2 $$/수식$$  = $$수식$${two} ^ {two}$$/수식$$\n" \
              "$$수식$$3$$/수식$$ 번 접었을 때 면의 가닥 수는 $$수식$${two} ^ {two} `TIMES`2$$/수식$$ = $$수식$${two} ^ {three}$$/수식$$\n" \
              ".\n" \
              ".\n" \
              ".\n" \
              "$$수식$$x$$/수식$$번 접었을 때 면의 가닥 수는 $$수식$${two} ^ {x}$$/수식$$\n" \
              "이때 $$수식$${two} ^ {answ}$$/수식$$ = $$수식$${num}$$/수식$$이므로 $$수식$${answ}$$/수식$$번 접으면 $$수식$${num}$$/수식$$가닥의 면을\n" \
              "만들 수 있다."
    two = 2
    one = 1
    three = 3
    x="x"
    answ = np.random.randint(2, 10)
    num = 2**answ

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
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

    stem = stem.format(num=num,  x=x, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, x=x, one=one, two=two, three=three,answ=answ)

    return stem, answer, comment
#중1-1-1-17

def naturalnum111_Stem_013():
    stem = "$$수식$${num}$$/수식$$의 소인수를 모두 구한 것은?\n"\
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${num}$$/수식$${temp} 소인수분해하면 $$수식$${num}$$/수식$$ = $$수식$${eq}$$/수식$$\n" \
              "따라서 $$수식$${num}$$/수식$$의 소인수는 $$수식$${answ}$$/수식$$ {temp1}다"

    num = np.random.randint(1, 100)
    temp = proc_jo(num, 4)
    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1

    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    answ = ""
    if len(temp1) > 0:
        for i in range(len(temp1) - 1):
            answ = answ + str(temp1[i]) + ", "
        answ = answ + str(temp1[-1])

    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    while len(exp1)<=1:
        num = np.random.randint(1, 100)
        temp = proc_jo(num, 4)
        num_one = []
        i = 2
        n = num
        while n > 1:
            if n % i == 0:
                num_one.append(i)
                n = n / i
                i = i - 1
            i += 1

        num_one.sort()
        temp1 = []
        exp1 = []
        num_one.sort()
        for x in num_one:
            if x not in temp1:
                temp1.append(x)
        answ = ""
        if len(temp1) > 0:
            for i in range(len(temp1) - 1):
                answ = answ + str(temp1[i]) + ", "
            answ = answ + str(temp1[-1])

        for x in temp1:
            i = 0
            for y in num_one:
                if x == y:
                    i += 1
            exp1.append(i)
    eq = factor_equation(num)
    temp1 = proc_jo(exp1[-1],3)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = str(exp1[-1])
        x3 = "1, " + answ
        x4 = str(exp1[0]) + ", " + str(exp1[-1]+5)
        x5 = str(exp1[0]) + " , " + " {"+str(exp1[-1]+2)+ "} ^2"

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = str(exp1[-1])
        x3 = "1, " + answ
        x4 = str(exp1[0]) + ", " + str(exp1[-1]+5)
        x5 =str(exp1[0]) + " , " + "{"+str(exp1[-1]+2)+ "} ^2"
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = str(exp1[-1])
        x2 = "1, " + answ
        x4 = str(exp1[0]) + ", " + str(exp1[-1]+5)
        x5 =str(exp1[0]) + " , " + "{"+str(exp1[-1]+2)+ "} ^2"
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = str(exp1[-1])
        x2 = "1, " + answ
        x3 = str(exp1[0]) + ", " + str(exp1[-1]+5)
        x5 = str(exp1[0]) + " , " + "{"+str(exp1[-1]+2)+ "} ^2"
    else:
        ans = "⑤"
        x5 = answ
        x1 = str(exp1[-1])
        x2 = "1, " + answ
        x3 = str(exp1[0]) + ", " + str(exp1[-1]+5)
        x4 =str(exp1[0]) + " , " + "{"+str(exp1[-1]+2)+ "} ^2"



    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp1=temp1, num=num, temp=temp, answ=answ, eq=eq)

    return stem, answer, comment

#중1-1-1-18

def naturalnum111_Stem_014():
    stem = "$$수식$${num}$$/수식$$ 의 모든 소인수의 합을 구하시오.\n"
    answer = "(답):$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${num}$$/수식$$= $$수식$${eq1}$$/수식$$이므로 소인수는 $$수식$${fac_string}$$/수식$$ 이다.\n" \
              "따라서 모든 소인수의 합은\n" \
              "$$수식$${eq2}$$/수식$$  = $$수식$${ans}$$/수식$$"

    num = np.random.randint(1, 500)
    while num==433:
        num = np.random.randint(1, 500)
    ques = "①"
    num_one = []
    while len(num_one)==0:
        num = np.random.randint(1, 500)
        while num == 433:
            num = np.random.randint(1, 500)
        num_one = []
        i = 2
        n = num
        while n > 1:
            if n % i == 0:
                num_one.append(i)
                n = n / i
                i = i - 1
            i += 1
        num_one.sort()
        temp1 = []
        exp1 = []
        num_one.sort()
        for x in num_one:
            if x not in temp1:
                temp1.append(x)
        for x in temp1:
            i = 0
            for y in num_one:
                if x == y:
                    i += 1
            exp1.append(i)
    ans = 0
    for x in temp1:
        ans = ans + x
    eq1 = factor_equation(num)
    eq2 = ""
    if len(temp1) > 0:
        for i in range(len(temp1) - 1):
            eq2 = eq2 + str(temp1[i]) +  " + "
    eq2 = eq2 + str(num_one[-1]) + ""

    fac_string = ""
    if len(temp1) > 0:
        for i in range(len(temp1) - 1):
            fac_string = fac_string + str(temp1[i]) + ",  "
    fac_string = fac_string + str(num_one[-1]) + ""
    while len(temp1)==1:
        num = np.random.randint(1, 500)
        ques = "①"
        num_one = []
        i = 2
        n = num
        while n > 1:
            if n % i == 0:
                num_one.append(i)
                n = n / i
                i = i - 1
            i += 1
        num_one.sort()
        temp1 = []
        exp1 = []
        num_one.sort()
        for x in num_one:
            if x not in temp1:
                temp1.append(x)
        for x in temp1:
            i = 0
            for y in num_one:
                if x == y:
                    i += 1
            exp1.append(i)
        ans = 0
        for x in temp1:
            ans = ans + x
        eq1 = factor_equation(num)
        eq2 = ""
        if len(temp1) > 1:
            for i in range(len(temp1) - 1):
                eq2 = eq2 + str(temp1[i]) + " + "
        eq2 = eq2 + str(num_one[-1]) + ""

        fac_string = ""
        if len(temp1) > 1:
            for i in range(len(temp1) - 1):
                fac_string = fac_string + str(temp1[i]) + ",  "
        fac_string = fac_string + str(num_one[-1]) + ""
    stem = stem.format(num=num, ques=ques)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, ans=ans, eq1=eq1, eq2=eq2, fac_string=fac_string)

    return stem, answer, comment

#중1-1-1-21

def naturalnum111_Stem_015():
    stem = "$$수식$${big_eq}$$/수식$$ {temp} $$수식$${eq}$$/수식$$  의 꼴로 나타냈을 때, 자연수 " \
           "$$수식$$`a`, `b`$$/수식$$의 값을 각각 바르게 구한 것은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${big_eq} `=` {small_eq1} TIMES {small_eq2} `=` {eq1}$$/수식$$이므로\n" \
              "$$수식$${answ}$$/수식$$"
    a1 = np.random.randint(1, 5)
    b1 = np.random.randint(1, 5)
    a2 = np.random.randint(1, 5)
    b2 = np.random.randint(1, 5)
    first_number = 2 ** a1 * 3 ** b1
    second_number = 2 ** a2 * 3 ** b2
    while first_number == second_number:
        a2 = np.random.randint(1, 5)
        b2 = np.random.randint(1, 5)
        second_number = 2 ** a2 * 3 ** b2
    while first_number*second_number>1000:
        a1 = np.random.randint(1, 5)
        b1 = np.random.randint(1, 5)
        a2 = np.random.randint(1, 5)
        b2 = np.random.randint(1, 5)
        first_number = 2 ** a1 * 3 ** b1
        second_number = 2 ** a2 * 3 ** b2
        while first_number == second_number:
            a2 = np.random.randint(1, 5)
            b2 = np.random.randint(1, 5)
            second_number = 2 ** a2 * 3 ** b2
    a = a1 + a2
    b = b1 + b2
    big_eq = "$$수식$${" + str(first_number) + "} TIMES {" + str(second_number) + "}$$/수식$$"
    temp = proc_jo(second_number, 4)
    eq = "$$수식$${2} ^{a} TIMES {3} ^{b}$$/수식$$"

    small_eq1 = "(" + factor_equation(first_number) + ")"
    small_eq2= "(" + factor_equation(second_number)+")"
    eq1 = factor_equation(first_number*second_number)
    answ = "$$수식$$a =  {" + str(a) +"}$$/수식$$, $$수식$$b =  {" + str(b) + "}$$/수식$$"

    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = "a =  " + str(1) + "}, b =  {" + str(b+1) + "}"
        x3 = "a =  " + str(a+1) + "}, b =  {" + str(b) + "}"
        x4 = "a =  " + str(3) + "}, b =  {" + str(b+2) + "}"
        x5 = "a =  " + str(a+3) + "}, b =  {" + str(b+1) + "}"

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = "a = {" + str(1) + "}, b =  {" + str(b + 1) + "}"
        x3 = "a =  {" + str(a + 1) + "}, b =  {" + str(b) + "}"
        x4 = "a =  {" + str(3) + "}, b =  {" + str(b + 2) + "}"
        x5 = "a =  {" + str(a + 3) + "}, b =  {" + str(b + 1) + "}"
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = "a = {" + str(1) + "}, b =  {" + str(b + 1) + "}"
        x2 = "a =  {" + str(a + 1) + "}, b =  {" + str(b) + "}"
        x4 = "a =  {" + str(3) + "}, b =  {" + str(b + 2) + "}"
        x5 = "a =  {" + str(a + 3) + "}, b =  {" + str(b + 1) + "}"
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = "a = {" + str(1) + "}, b =  {" + str(b + 1) + "}"
        x2 = "a =  {" + str(a + 1) + "}, b =  {" + str(b) + "}"
        x3 = "a =  {" + str(3) + "}, b =  {" + str(b + 2) + "}"
        x5 = "a =  {" + str(a + 3) + "}, b =  {" + str(b + 1) + "}"
    else:
        ans = "⑤"
        x5 = answ
        x1 = "a = {" + str(1) + "}, b =  {" + str(b + 1) + "}"
        x2 = "a =  {" + str(a + 1) + "}, b =  {" + str(b) + "}"
        x3 = "a =  {" + str(3) + "}, b =  {" + str(b + 2) + "}"
        x4 = "a =  {" + str(a + 3) + "}, b =  {" + str(b + 1) + "}"


    stem = stem.format(big_eq=big_eq, temp=temp, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(big_eq=big_eq, small_eq2=small_eq2,small_eq1=small_eq1, eq1=eq1, answ=answ)

    return stem, answer, comment


#중1-1-1-22
def naturalnum111_Stem_016():
    stem = "$$수식$${num}$$/수식$${temp} 소인수분해하면 $$수식$${a} ^{m} TIMES {b} ^{n}$$/수식$$이다. 이때 자연수\n" \
           "$$수식$$a,` b,` m,` n$$/수식$$에 대하여 $$수식$$a + b + m + n$$/수식$$의 값은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "

    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${num}$$/수식$$ = $$수식$${eq}$$/수식$$이므로\n" \
              "$$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$, $$수식$$m = {m}$$/수식$$, $$수식$$n = {n}$$/수식$$ 또는" \
              "$$수식$$a = {b}$$/수식$$, $$수식$$b = {a}$$/수식$$, $$수식$$m = {n}$$/수식$$, $$수식$$n = {m}$$/수식$$\n" \
              "$$수식$$a + b + m + n = {answ}$$/수식$$" \

    fac = [2, 3, 5, 7]
    a = fac[np.random.randint(0, 4)]
    m = np.random.randint(1, 6)
    b = fac[np.random.randint(0, 4)]
    n = np.random.randint(1, 6)
    while a == b:
        b = fac[np.random.randint(0, 4)]
    while a ** m * b ** n > 500:
        a = fac[np.random.randint(0, 4)]
        m = np.random.randint(1, 6)
        b = fac[np.random.randint(0, 4)]
        n = np.random.randint(1, 6)
        while a == b:
            b = fac[np.random.randint(0, 4)]
    num = (a ** m) *(b ** n)
    answ = a + b + m + n
    eq = factor_equation(num)
    temp = proc_jo(num, 4)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(0, 17)
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

    stem = stem.format(num=num, temp=temp, a="a", b="b", m="m", n="n", x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, eq=eq, a=a, b=b, m=m, n=n, answ=answ)

    return stem, answer, comment

#중1-1-1-23

def naturalnum111_Stem_017():
    stem = "$$수식$${num} TIMES `a$$/수식$$ = $$수식$${b} ^{two}$$/수식$$을 만족시키는 가장 작은 자연수 $$수식$$a," \
           "b`$$/수식$$에 대하여 $$수식$$a `+` b$$/수식$$의 값은?\n" \
            "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${num}$$/수식$$ = $$수식$${fac_list}$$/수식$$ 이므로 " \
              " $$수식$$ a = $$/수식$${a_eq} \n" \
              "따라서 $$수식$${bsq_eq}$$/수식$$\n" \
              "$$수식$$ b = $$/수식$${b_eq}\n" \
              "∴ $$수식$$a`+`b `=` {ab}$$/수식$$ = $$수식$${answ}$$/수식$$"
    num = np.random.randint(10, 50)
    bsq = num ** 2
    bi = 0
    b = 0
    while True:
        if bsq % num == 0 and bsq % math.sqrt(bsq) == 0:
            bi = bsq
        bsq -= 1
        if (bsq == 1):
            break
    b = math.sqrt(bi)
    a = b ** 2 / num
    a = int(a)
    b = int(b)
    bsq = int(bsq)
    bsq = b**2
    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_list = factor_equation(num)

    a_list =[]
    i = 2
    n = a
    while n > 1:
        if n % i == 0:
            a_list.append(i)
            n = n / i
            i = i - 1
        i += 1
    a_list.sort()
    temp1.clear()
    exp1.clear()
    a_list.sort()
    for x in a_list:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in a_list:
            if x == y:
                i += 1
        exp1.append(i)
    a_eq =factor_equation(a)
    if len(temp1) == 1:
        if exp1[-1] != 1:
            a_eq = "$$수식$${" + str(temp1[-1]) + "} ^{" + str(exp1[-1]) + "} `TIMES`1 $$/수식$$"
        else:
            a_eq = "$$수식$${" + str(temp1[-1]) + "} `TIMES`1 $$/수식$$ "
    if len(temp1)==0:
        a_eq =str(1)
    tempb = bsq / a
    bsq_list = []

    i = 2
    n = tempb
    while n > 1:
        if n % i == 0:
            bsq_list.append(i)
            n = n / i
            i = i - 1
        i += 1
    bsq_list.sort()
    temp1.clear()
    exp1.clear()
    bsq_list.sort()
    for x in bsq_list:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in bsq_list:
            if x == y:
                i += 1
        exp1.append(i)

    bsq_eq =factor_equation(tempb)
    if len(temp1) == 1:
        if exp1[-1] != 1:
            bsq_eq = "$$수식$${" + str(temp1[-1]) + "} ^{" + str(exp1[-1]) + "}`TIMES`1 $$/수식$$"
        else:
            bsq_eq = "$$수식$${" + str(temp1[-1]) + "}`TIMES`1 $$/수식$$"
    bsq_eq = "(" + bsq_eq + ")"
    another_atemp = "$$수식$$TIMES$$/수식$$ (" + a_eq + ")"
    if a_eq==str(1):
        another_atemp = ""
    bsq_eq = bsq_eq + another_atemp



    tempb = bsq
    bsq_list = []

    i = 2
    n = tempb
    bsq_list.clear()
    while n > 1:
        if n % i == 0:
            bsq_list.append(i)
            n = n / i
            i = i - 1
        i += 1
    bsq_list.sort()
    temp1.clear()
    exp1.clear()
    bsq_list.sort()
    for x in bsq_list:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in bsq_list:
            if x == y:
                i += 1
        exp1.append(i)

    bsq_f_eq =""
    if len(temp1) > 0:
        if len(temp1) > 1:
            for i in range(len(temp1) - 1):
                bsq_f_eq = bsq_f_eq + "  $$수식$${" + str(temp1[i])+"} ^{" + str(exp1[i]) + "} TIMES$$/수식$$"
        bsq_f_eq = bsq_f_eq + "  $$수식$${" + str(temp1[-1])+"} ^{"+ str(exp1[-1]) + "}$$/수식$$"

    bsq_eq = bsq_eq + "=" + bsq_f_eq

    b_eq = factor_equation(int(math.sqrt(tempb)))

    bsq_eq = "$$수식$${b} ^{2}$$/수식$$ =" + bsq_eq
    answ = a+b
    bb = []
    while len(bb) < 4:
        k = np.random.randint(0, 50)
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
    ab = str(a) + " + " + str(b)

    stem = stem.format(two=2,num=num, b="b", x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, fac_list=fact_list, a_eq=a_eq, bsq_eq=bsq_eq, b_eq=b_eq, ab=ab, answ=answ)

    return stem, answer, comment

#중1-1-1-24

def naturalnum111_Stem_018():
    stem = "$$수식$${num}$$/수식$${temp} 자연수 $$수식$$a$$/수식$$로 나누어 어떤 자연수 $$수식$$b$$/수식$$의 제곱" \
            "이 되도록 할 때, 나눌 수 있는 가장 작은 자연수 " \
            "$$수식$$a$$/수식$$와 이때의 $$수식$$b$$/수식$$의 값의 합은?\n" \
            "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "



    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${num}$$/수식$$ = $$수식$${eq}$$/수식$$ 이므로 " \
              "$$수식$$ a=$$/수식$${a_eq}\n" \
              "$$수식$${b_div}$$/수식$$\n" \
              "따라서 $$수식$$b `=`{b}$$/수식$$이므로\n" \
              "$$수식$$a + b = {answ}$$/수식$$" \

    fac = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    num = np.random.randint(100, 500)
    while True:
        u = 0
        num = np.random.randint(100, 500)
        for x in fac:
            if num%x==0:
                u+=1
        if u>=1:
            break
    temp = proc_jo(num, 4)

    a = num - 1
    bsq = 1
    b = 0
    while True:
        if num % a == 0 and (num / a) % math.sqrt(num / a) == 0:
            bsq = num / a
        a -= 1
        if (a == 1):
            break
    b = int(math.sqrt(bsq))
    a = int(num / bsq)
    bsq = int(bsq)

    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_list = factor_equation(num)

    eq = fact_list

    a_list = []
    i = 2
    n = a
    while n > 1:
        if n % i == 0:
            a_list.append(i)
            n = n / i
            i = i - 1
        i += 1
    a_list.sort()
    temp1.clear()
    exp1.clear()
    a_list.sort()
    for x in a_list:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in a_list:
            if x == y:
                i += 1
        exp1.append(i)
    a_eq = factor_equation(a)
    if len(temp1) == 1:
        if exp1[-1] != 1:
            a_eq = "$$수식$${" + str(temp1[-1]) + "} ^{" + str(exp1[-1]) + "}`TIMES`1$$/수식$$"
        else:
            a_eq = "$$수식$${" + str(temp1[-1]) + "}`TIMES`1$$/수식$$"
    a_eq = a_eq + "$$수식$$ = " + str(a)+"$$/수식$$"

    b_div = str(num) + "DIV`" + str(a) + " = " + str(bsq) + " = " + "{`" + str(b) + "} ^{" + str(2) + "`}"
    answ = a + b
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

    stem = stem.format(num=num, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, eq=eq, a_eq=a_eq, b=b, b_div=b_div, answ=answ)

    return stem, answer, comment

#중1-1-1-26


def naturalnum111_Stem_019():
    stem = "$$수식$${num}$$/수식$${temp} 자연수 $$수식$$x$$/수식$$로 나누어 어떤 자연수의 제곱이 " \
               "되도록 할 때, 다음 중 $$수식$$x$$/수식$$의 값이 될 수 있는 것은?\n" \
               "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${num}$$/수식$$ = $$수식$${eq}$$/수식$$ 이므로 $$수식$$x$$/수식$$는 $$수식$${num}$$/수식$$ 의 약수이면서\n" \
              "{d_eq} 꼴이어야 한다.\n" \
              "{list}\n" \
              "따라서 $$수식$$x$$/수식$$의 값이 될수 있는 것은 $$수식$${ans}이다 \n" \
              "$$/수식$$"

    num = np.random.randint(100, 999)
    while num==809 or num==149 or num==433:
        num = np.random.randint(100, 999)
    temp = proc_jo(num, 4)

    a = num - 1
    bsq = 1
    b = 0
    while True:
        if num % a == 0 and (num / a) % math.sqrt(num / a) == 0:
            bsq = num / a
        a -= 1
        if (a == 1):
            break
    b = int(math.sqrt(bsq))
    a = int(num / bsq)
    bsq = int(bsq)

    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_list = factor_equation(num)

    eq = fact_list
    fact_list=""
    answ = a

    while answ==num:
        num = np.random.randint(100, 999)
        while num == 809 or num == 149 or num == 433:
            num = np.random.randint(100, 999)
        temp = proc_jo(num, 4)

        a = num - 1
        bsq = 1
        b = 0
        while True:
            if num % a == 0 and (num / a) % math.sqrt(num / a) == 0:
                bsq = num / a
            a -= 1
            if (a == 1):
                break
        b = int(math.sqrt(bsq))
        a = int(num / bsq)
        bsq = int(bsq)

        num_one = []
        i = 2
        n = num
        while n > 1:
            if n % i == 0:
                num_one.append(i)
                n = n / i
                i = i - 1
            i += 1
        num_one.sort()
        temp1 = []
        exp1 = []
        num_one.sort()
        for x in num_one:
            if x not in temp1:
                temp1.append(x)
        for x in temp1:
            i = 0
            for y in num_one:
                if x == y:
                    i += 1
            exp1.append(i)
        fact_list = factor_equation(num)

        eq = fact_list
        fact_list = ""
        answ = a

    bb = []
    while len(bb) < 4:
        k = np.random.randint(0,999)
        if k not in bb and k != answ:
            bb.append(k)
    bb.append(answ)
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
    num_one.clear()
    for x in bb:
        num_two = []
        num_two.clear()
        i = 2
        n = x
        while n > 1:
            if n % i == 0:
                num_two.append(i)
                n = n / i
                i = i - 1
            i += 1
        num_two.sort()
        num_one.append(num_two)

    exp1=[]
    exp1.clear()
    temp1=[]
    temp1.clear()
    temp2=[]
    temp2.clear()
    for x in num_one:
        for y in x:
            if y not in temp2:
                temp2.append(y)
        temp1.append(temp2)
        temp2=[]
    count = 0
    temp_exp =[]
    for i in range (len(temp1)):
        for x in temp1[i]:
            k = 0
            for y in num_one[i]:
                if x == y:
                    k += 1

            temp_exp.append(k)
            k = 0
        exp1.append(temp_exp)
        temp_exp = []
    for i in range (len(bb)):
        bb[i] = str(bb[i]) + "$$수식$$`=`$$/수식$$"
    d_eq = ""
    for j in range(len(temp1[4]) - 1):
        if exp1[-1][j] !=1:
            d_eq = d_eq + "$$수식$${" + str(temp1[-1][j]) + "} ^{" + str(exp1[-1][j]) + "}`TIMES`$$/수식$$"
        else:
            d_eq = d_eq + "$$수식$${" + str(temp1[-1][j]) + "}`TIMES`$$/수식$$"
    if exp1[-1][-1] != 1:
        d_eq = d_eq + "$$수식$${" + str(temp1[-1][-1]) + "} ^{" + str(exp1[-1][-1]) + "}$$/수식$$"
    else:
        d_eq = d_eq + "$$수식$${" + str(temp1[-1][-1]) + "}$$/수식$$ "
    d_eq = d_eq + "$$수식$$TIMES  ($$/수식$$ 자연수$$수식$$) ^2$$/수식$$ "
    e = 1
    for j in range(len(temp1[4])):
        e = e*temp1[-1][j]**exp1[-1][j]

    if e ==num:
        temp1[-1].append(1)
        exp1[-1].append(2)

    for i in range (len(bb)):
        for j in range (len(temp1[i])-1):
            if exp1[i][j] != 1:
                bb[i] ="$$수식$$"+ str(bb[i]) + "{" + str(temp1[i][j]) + "} ^{" + str(exp1[i][j]) + "} TIMES$$/수식$$"
            else:
                bb[i] = "$$수식$$"+str(bb[i]) + "{" + str(temp1[i][j]) + "} TIMES$$/수식$$"
        if len(exp1[i])>0:
            if exp1[i][-1] != 1:
                bb[i] = "$$수식$$"+str(bb[i]) + "{" + str(temp1[i][-1]) + "} ^{" + str(exp1[i][-1]) + "}$$/수식$$"
            else:
                bb[i] = "$$수식$$"+str(bb[i]) + "{" + str(temp1[i][-1]) + "}$$/수식$$"
    liste=""
    if rande == 1:
        liste = "① " + bb[4] + "\n② " +bb[0] +"\n③ "+ bb[1]+ "\n④ "+ bb[2] +"\n⑤ " +bb[3]
    elif rande == 2:
        liste = "① " +bb[0] + "\n② " + bb[4] + "\n③ "+ bb[1] + "\n④ "+ bb[2] +"\n⑤ " +bb[3]
    elif rande == 3:
        liste = "① " + bb[0] + "\n② " + bb[1] + "\n③ " + bb[4] + "\n④ " + bb[2] + "\n⑤ " + bb[3]
    elif rande == 4:
        liste = "① " + bb[0] + "\n② " + bb[1] + "\n③ " + bb[2] + "\n④ " + bb[4] + "\n⑤ " + bb[3]
    else:
        liste = "① " + bb[0] + "\n② " + bb[1] + "\n③ " + bb[2] + "\n④ " + bb[3] + "\n⑤ " + bb[4]


    stem = stem.format(num=num, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, eq=eq, list=liste, d_eq=d_eq, ans=ans)

    return stem, answer, comment
#중1-1-1-27

def naturalnum111_Stem_020():
    stem = "$$수식$${num}$$/수식$${temp} 작은 자연수 $$수식$$a$$/수식$$로 나누어 어떤 자연수n$$수식$$b$$/수식$$의 제곱" \
            "이 되도록 할 때, $$수식$$a`-`b$$/수식$$의 값은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "


    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${num}$$/수식$$ = $$수식$${eq}$$/수식$$  이므로 " \
              "$$수식$$a = {a_eq}$$/수식$$\n" \
              " {b_div} 이므로" \
              "$$수식$$b `= `{b}$$/수식$$\n" \
              "$$수식$$a `- `b `=`{a}$$/수식$$ - $$수식$${b}$$/수식$$ = $$수식$${answ}$$/수식$$" \

    num = np.random.randint(20, 30)*(np.random.randint(2, 5)**2)
    temp = proc_jo(num, 4)

    a = num - 1
    bsq = 1
    b = 0
    while True:
        if num % a == 0 and (num / a) % math.sqrt(num / a) == 0:
            bsq = num / a
        a -= 1
        if (a == 1):
            break
    b = int(math.sqrt(bsq))
    a = int(num / bsq)
    bsq = int(bsq)

    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_list = factor_equation(num)

    eq = fact_list

    a_list = []
    i = 2
    n = a
    while n > 1:
        if n % i == 0:
            a_list.append(i)
            n = n / i
            i = i - 1
        i += 1
    a_list.sort()
    temp1.clear()
    exp1.clear()
    a_list.sort()
    for x in a_list:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in a_list:
            if x == y:
                i += 1
        exp1.append(i)
    a_eq = factor_equation(a)
    a_eq = a_eq + " =$$수식$$" + str(a)+"$$/수식$$"

    b_div = "$$수식$$"+str(num) + "DIV " + str(a) + " = " + str(bsq) + " = " + "{`" + str(b) + "} ^{" + str(
        2) + "`}$$/수식$$"
    answ = a - b
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

    stem = stem.format(num=num, temp=temp, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, eq=eq, a_eq=a_eq, a=a, b=b, b_div=b_div, answ=answ)

    return stem, answer, comment



#중1-1-1-28
def naturalnum111_Stem_021():
    stem = "$$수식$$1$$/수식$$부터 $$수식$$100$$/수식$$까지의 자연수의 곱을 $$수식$$N$$/수식$$이라 하자. $$수식$$N$$/수식$$" \
           "이 $$수식$${num} ^{k}$$/수식$$으로 나누어떨어질 때, 자연수 $$수식$$k$$/수식$$의 값중 가장 큰 것은?\n"\
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$$N` =` $$/수식$${eq} 이 $$수식$${num} ^{k}$$/수식$$으로 나누어떨어지므\n" \
              "로 $$수식$$k$$/수식$$의 값 중 가장 큰 것은 $$수식$$N$$/수식$$을 소인수분해했을\n" \
              "때 소인수 $$수식$${num}$$/수식$$의 지수와 같다.\n" \
              "$$수식$$1$$/수식$$부터 $$수식$$100$$/수식$$까지의 자연수 중 $$수식$${num}$$/수식$$의 배수는\n" \
              "{m_eq}\n" \
              "$$수식$${par_answ}$$/수식$$개이다.\n" \
              "이 중에서 $$수식$${eq3}$$/수식$$ 에서는 소인수 $$수식$${num}$$/수식$$이 $$수식$$2$$/수식$$번씩 \n" \
              "곱해지므로 $$수식$$N$$/수식$$을 소인수분해했을 때 소인수 $$수식$${num}$$/수식$$의 지수는\n" \
              "$$수식$${eq4}$$/수식$$\n" \
              "따라서 $$수식$$k$$/수식$$의 값 중 가장 큰 것은 $$수식$${answ}$$/수식$$이다." \

    num = np.random.randint(6, 10)
    count =0
    for i in range(1,100):
        k=i
        while k % num ==0:
            k =k/num
            count+=1
    answ=count
    intk = int(100/num)
    eq = "$$수식$$1 `TIMES` 2 `TIMES`  3 `TIMES` `CDOTS `TIMES` 100$$/수식$$"
    m_eq = "$$수식$$"+str(num) + " `TIMES` 1  = " + str(num) +", " + str(num) + " `TIMES` 2 = " + str(num*2) +", " + str(num) + "`TIMES` 3 = " + str(num*3) + "CDOTS,$$/수식$$\n$$수식$$" + str(num) + " `TIMES` "+ str(intk) + " = " +  str(num * intk)+"$$/수식$$"

    par_answ=intk
    eq31 =[]
    eq3 = ""
    p=num
    for i in range (1,intk+1):
        if p*i % p**2 ==0:
            eq31.append(i)
    eq31.sort()
    if len(eq31) > 1:
        for i in range (0, len(eq31)-1):
            eq3 = eq3 + str(num) + " `TIMES` " + str(eq31[i]) + ", "
    eq3 = eq3 + str(num) + "`TIMES`" +  str(eq31[-1]) 


    temp = "$$/수식$${" +proc_jo(eq31[-1], -1) + "}$$/수식$$"

    eq4 = str(par_answ) +" + " + str(len(eq31)) + " = " + str(count)

    bb = []
    while len(bb) < 4:
        k = np.random.randint(2, 20)
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
    k = "k"
    eq3 = eq3 +  str(eq31[-1])
    stem = stem.format(num=num, k=k, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(k=k, num=num, eq=eq, m_eq=m_eq,par_answ=par_answ,eq3=eq3,eq4=eq4,temp=temp, answ=count)

    return stem, answer, comment

#중1-1-1-29
def naturalnum111_Stem_022():
    stem = "모든 소인수의 합이 $$수식$${num}$$/수식$$인 두 자리 자연수의 개수는?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답): {ans}"
    comment = "(해설)\n" \
              "합이 $$수식$${num}$$/수식$$인 소수는 $$수식$${pair}$$/수식$$ 이므로\n" \
              "구하는 수는  {eq}꼴이다. \n" \
              "따라서 두 자리 자연수는  " \
              "{eq2}\n" \
              "의 $$수식$${answ}$$/수식$$개이다." \

    num = np.random.randint(5, 10)
    div_num = []
    pair_list = []
    while num==6 or num==7:
        num = np.random.randint(5, 10)
    if num == 5:
        pair_list = [[2,3]]

    elif num == 8:
        pair_list = [[3,5]]
    else:
        pair_list = [[2, 7]]

    pair=""
    eq=""
    k =len(pair_list)
    for x in pair_list:
        if k > 1:
            if len(pair_list) == 1:
                pair = "$$수식$${" + str(x[0]) +"}$$/수식$$" + proc_jo(x[0],2) + "  $$/수식$${"+ str(x[1]) + "}$$/수식$$ ,"
                eq = eq + "$$수식$${" +str(x[0]) +"} ^{m}$$/수식$$ ,"
            else:
                pair = pair + "$$수식$${" + str(x[0]) +"}$$/수식$$" + proc_jo(x[0],2) + " $$/수식$${" + str(x[1]) + "}$$/수식$$ ,"
                eq = eq + "$$수식$${" + str(x[0]) + "} ^{m} TIMES {" +str(x[1]) +"} ^{n}$$/수식$$, "
        else:
            if len(x) == 1:
                pair = "$$수식$${" + str(x[0]) + "}$$/수식$$"
                eq = eq + "$$수식$${" + str(x[0]) + "} ^{m}$$/수식$$ (m은 자연수)"
            else:
                pair = pair + "$$수식$${" + str(x[0]) +"}$$/수식$$"+ proc_jo(x[0],2) + " $$수식$${"+  str(x[1]) + "}$$/수식$$"
                eq = eq + "$$수식$${" + str(x[0]) + "} ^{m} TIMES {" + str(x[1]) + "} ^{n}$$/수식$$ ($$수식$$`m`,` n`$$/수식$$ 은 자연수)"
        k-=1
    base = []
    temp1 =[]
    if len(pair_list[0]) ==1:
        base.append(pair_list[0][0])
    else:
        base.append(pair_list[0][0]*pair_list[0][1])
    if len(pair_list) > 1:
        base.append(pair_list[1][0] * pair_list[1][1])
    if len(pair_list[0]) > 1:
        for i in range (0, len(base)):
            div_num =[]
            mul_num = base[i]
            div_num.append(mul_num)
            div_num.append(mul_num*pair_list[i][1])
            while True:
                if mul_num * pair_list[i][0] < 100:
                    mul_num = mul_num * pair_list[i][0]
                    if mul_num not in div_num:
                        div_num.append(mul_num)
                else:
                    temp1.append(div_num)
                    break
                while True:
                    if mul_num*pair_list[i][1] < 100:
                        mul_num = mul_num * pair_list[i][1]
                        if mul_num not in div_num:
                            div_num.append(mul_num)
                    else:
                        break
    else:
        mul_num = base[0]
        div_num.append(mul_num)
        while True:
            if mul_num*pair_list[0][0] < 100:
                mul_num = mul_num*pair_list[0][0]
                if mul_num not in div_num:
                    div_num.append(mul_num)
            else:
                temp1.append(div_num)
                break
    temp11=[]
    temp22=[]
    for i in range(0, len(temp1)):
        for j in range(0, len(temp1[i])):
            if temp1[i][j]>10:
                temp11.append(temp1[i][j])
        temp22.append(temp11)
    temp1= temp22
    ep1=[]
    for i in range(0, len(temp1)):
        for x in temp1[i]:
            temp2 = []
            for y in pair_list[i]:
                count=0
                while x % y == 0:
                    x = x / y
                    count+=1
                temp2.append(count)
            ep1.append(temp2)
    answ = len(ep1)
    eq2 =""

    if len(pair_list[0]) > 1:
        for i in range(0, len(pair_list)):
            for j in range(0, len(temp1[i])-1):
                for k in range(0,1):
                    if ep1[j][k]!=1:
                        eq2 = eq2 + "$$수식$${" + str(pair_list[i][k]) + "} ^{"+str(ep1[j][k]) +"} TIMES$$/수식$$"
                    else:
                        eq2 = eq2 + "$$수식$${" + str(pair_list[i][k]) + "} TIMES$$/수식$$"
                if ep1[j][-1] != 1:
                    eq2 = eq2 + "$$수식$${" + str(pair_list[i][1]) + "}^{"+str(ep1[j][-1]) +"}$$/수식$$ = $$수식$${" + str(temp1[i][j]) + "}$$/수식$$,    "
                else:
                    eq2 = eq2 + "$$수식$${" + str(pair_list[i][1]) + "}$$/수식$$ = $$수식$${" + str(temp1[i][j]) + "}$$/수식$$,    "
            for k in range(0, len(pair_list)-1):
                if ep1[-1][0]!=1:
                    eq2 = eq2 + "$$수식$${" + str(pair_list[-1][0]) + "} ^{" + str(ep1[-1][0]) + "} TIMES$$/수식$$"
                else:
                    eq2 = eq2 + "$$수식$${" + str(pair_list[-1][0]) + "} TIMES$$/수식$$"
                if ep1[-1][-1]!=1:
                     eq2 = eq2 + "$$수식$${" + str(pair_list[-1][-1]) + "} ^{" + str(ep1[-1][-1]) + "}$$/수식$$  = $$수식$${" + str(temp1[-1][-1]) + "}$$/수식$$"
                else:
                    eq2 = eq2 + "$$수식$${" + str(pair_list[-1][-1]) + "}$$/수식$$  = $$수식$${" + str(temp1[-1][-1]) + "}$$/수식$$"
    else:
        for j in range(0, len(temp1[0]) - 1):
            if ep1[j][0]!=1:
                eq2 = eq2 + "$$수식$${" + str(pair_list[0][0]) + "} ^{" + str(ep1[j][0]) + "}$$/수식$$  = $$수식$${" + str(temp1[0][j]) + "}$$/수식$$,     "
            else:
                eq2 = eq2 + "$$수식$${" + str(pair_list[0][0]) + "}$$/수식$$  = $$수식$${" + str(temp1[0][j]) + "}$$/수식$$,     "
            if ep1[-1][0]!=1:
                 eq2 = eq2 + "$$수식$${" + str(pair_list[0][0]) + "} ^{" + str(ep1[-1][0]) + "}$$/수식$$  = $$수식$${" + str(temp1[0][-1]) + "}$$/수식$$"
            else:
                eq2 = eq2 + "$$수식$${" + str(pair_list[0][0]) + "}$$/수식$$  = $$수식$${" + str(temp1[0][-1]) + "}$$/수식$$"


    bb = []
    while len(bb) < 4:
        k = np.random.randint(2, 10)
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
    k = "k"

    stem = stem.format(num=num,  x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(pair=pair, num=num, eq=eq, eq2=eq2,  answ=answ)

    return stem, answer, comment

#중1-1-1-30
def naturalnum111_Stem_023():
    stem = "$$수식$${num} TIMES x$$/수식$$가 어떤 자연수의 제곱이 되게 할 때, 두 " \
           "자리 자연수 $$수식$$x$$/수식$$의 값들의 합은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$ 이므로\n" \
              "$$수식$$x$$/수식$$ = $$수식$${x_eq} CDOTS$$/수식$$\n" \
              "이때 $$수식$$x$$/수식$$의 값 중에서 두 자리 자연수는\n" \
              "{div_eq}\n" \
              "따라서 $$수식$$x$$/수식$$의 값 중에서 두 자리 자연수의 합은\n"\
              "$$수식$${answ_eq}$$/수식$$" \

    fac = [3, 5,7]
    num1 = fac [np.random.randint(0,3)]
    num = np.random.randint(100, 500)
    while True:
        num = np.random.randint(100, 500)
        num_one = []
        count=0
        i = 2
        n = num
        while n > 1:
            if n % i == 0:
                num_one.append(i)
                n = n / i
                i = i - 1
            i += 1
        num_one.sort()
        temp1 = []
        exp1 = []
        num_one.sort()
        for x in num_one:
            if x not in temp1:
                temp1.append(x)
        for x in temp1:
            i = 0
            for y in num_one:
                if x == y:
                    i += 1
            exp1.append(i)
        for x in exp1:
            if x % 2 !=0 and num % num1 ==0:
                count+=1
        if count==1:
            break


    fact_list = "$$수식$$"+str(num) +"$$/수식$$ = "
    if len(temp1) > 1:
        for i in range(len(temp1) - 1):
            if exp1[i]!=1:
                fact_list = fact_list + "$$수식$${" + str(temp1[i]) + "} ^{" + str(exp1[i]) + "} TIMES$$/수식$$"
            else:
                fact_list = fact_list + "$$수식$${" + str(temp1[i]) + "} TIMES$$/수식$$"
    if exp1[-1]!=1:
        fact_list = fact_list + " $$수식$${" + str(temp1[-1]) + "} ^{" + str(exp1[-1]) + "}$$/수식$$ $$/수식$$"
    else:
        fact_list = fact_list + " $$수식$${" + str(temp1[-1]) + "}$$/수식$$ $$/수식$$"
    eq = fact_list

    answ_list =[]
    for i in range (10, 100):
        if i*num % math.sqrt(i*num) ==0:
            answ_list.append(i)
    for i in range (len(exp1)):
        if (exp1[i] % 2 ==1 or exp1[i]==1) and temp1[i]>9 and temp1[i] <100 and temp1[i] not in answ_list:
            answ_list.append(temp1[i])
    x_eq=""
    for i in range (1,5):
        x_eq = x_eq + "$$수식$${" + str(1) + "} TIMES {" + str(num1) + "}^{" + str(2) + "}$$/수식$$, "
    x_eq = x_eq + "$$수식$${" + str(5) + "} TIMES {" + str(num1) + "}^{" + str(
        2) + "}$$/수식$$"
    temp2 =[]
    exp2 =[]
    for q in answ_list:
        num_one = []
        count=0
        i = 2
        n = q
        while n > 1:
            if n % i == 0:
                num_one.append(i)
                n = n / i
                i = i - 1
            i += 1
        num_one.sort()
        temp1 = []
        exp1 = []
        num_one.sort()
        for x in num_one:
            if x not in temp1:
                temp1.append(x)
        temp2.append(temp1)
        for x in temp1:
            i = 0
            for y in num_one:
                if x == y:
                    i += 1
            exp1.append(i)
        exp2.append(exp1)


    div_eq=""
    answ = 0
    answ_eq = ""
    if len(answ_list) >= 1:
        for i in range(0, len(answ_list)):
            for j in range(0, len(exp2[i]) - 1):
                if exp2[i][j]!=1:
                    div_eq = div_eq + "$$수식$${" + str(temp2[i][j]) + "} ^{" + str(exp2[i][j]) + "} TIMES$$/수식$$"
                else:
                    div_eq = div_eq + "$$수식$${" + str(temp2[i][j]) + "} TIMES$$/수식$$"
            if exp2[i][-1]!=1:
                div_eq = div_eq +"$$수식$${" + str(temp2[i][-1]) + "} ^ {" + str(exp2[i][-1]) + "} = {" + str(answ_list[i]) + "}$$/수식$$           "
            else:
                div_eq = div_eq + "$$수식$${" + str(temp2[i][-1]) + "} = {" + str(answ_list[i]) + "}$$/수식$$           "
        for i in range (0, len(answ_list)-1):
            answ = answ + answ_list[i]
            answ_eq = answ_eq + "$$수식$${" + str(answ_list[i]) +" } + $$/수식$$"
        answ = answ + answ_list[-1]
        answ_eq = answ_eq + "$$수식$${" + str(answ_list[-1]) + "} = {" + str(answ) + "}$$/수식$$"
    else:
        div_eq = "없다"
        answ_eq = "0 = 0"

    answ = answ=+1
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
    k = "k"

    stem = stem.format(num=num,  x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(div_eq=div_eq, x_eq=x_eq, num=num, eq=eq, answ_eq=answ_eq,  answ=answ)

    return stem, answer, comment



#중1-1-1-31
def naturalnum111_Stem_024():
    stem = "$$수식$$1$$/수식$$부터 $$수식$${num}$$/수식$$까지의 자연수가 각각 적혀 있는 사물함" \
           "이 있다. 이 사물함은 모두 문이 닫혀 있고, $$수식$${num}$$/수식$$명" \
           "의 학생이 다음의 규칙에 따라 문을 열거나 닫는" \
           "다. 이때 문이 열려 있는 사물함의 개수는?\n" \
           "$$표$$$$수식$$1$$/수식$$번 학생은 모든 사물함의 문을 연다.\n" \
           "☞ $$수식$$2$$/수식$$번 학생은 $$수식$$2$$/수식$$배의 배수가 적혀 있는 사물함의 문을 모두 닫는다.\n" \
           "☞ $$수식$$3$$/수식$$번 학생은 $$수식$$3$$/수식$$배의 배수가 적혀 있는 사물함의 문이 닫혀 있으면 열고, 열려 있으면 닫는다.\n" \
           "$$수식$$CDOTS$$/수식$$\n" \
           "☞ $$수식$${num}$$/수식$$번의 학생은 $$수식$${num}$$/수식$$의 배수가 적혀 있는 사물함의 문이 닫혀 있으면 열고, 열려 있으면 닫는다. $$/표$$\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "문이 열려 있는 사물함에 적혀 있는 자연수는 $$수식$${num}$$/수식$$\n" \
              "이하의 자연수 중 약수의 개수가 홀수 개인 수이\n" \
              "다. 이때 $$수식$${num}$$/수식$$ 이하의 자연수 중 약수의 개수가 홀\n" \
              "수 개인 수는 $$수식$${ko} ^2$$/수식$$꼴이다.\n" \
              "즉, 적혀 있는 자연수는 $$수식$${list}$$/수식$$이다.\n" \
              "따라서 문이 열려 있는 사물함의 개수는 $$수식$${answ}$$/수식$$이다.\n"

    ko = "$$수식$$ ($$/수식$$ 자연수$$수식$$) ^2$$/수식$$"
    num = np.random.randint(3, 100)
    answ = int(math.sqrt(num))
    list =""
    for i in range (1,4):
        list = list + "$$수식$${" + str(i) + "} ^{"+str(2)+"}$$/수식$$, "
    list = list + "$$수식$$CDOTS$$/수식$$, $$수식$${" + str(answ) + "} ^{"+str(2)+"}$$/수식$$, "
    bb = []
    while len(bb) < 4:
        k = np.random.randint(2, 10)
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

    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(ko=ko, list=list, num=num, answ=answ)

    return stem, answer, comment
#중1-1-1-33

def naturalnum111_Stem_025():
    stem = "$$수식$${num}$$/수식$$의 약수의 개수는?\n"\
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans} "
    comment = "(해설)\n" \
              "$$수식$${num}`=` {eq}`TIMES`1$$/수식$$ 이므로 $$수식$${num}$$/수식$$의 약수의 개수는\n" \
              "{eq2}$$수식$$`=` {answ}$$/수식$$" \

    num = np.random.randint(30, 100)
    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = factor_equation(num)

    eq =fact_
    answ=1
    for x in exp1:
        answ = answ * (1 + x)

    eq2 = ""
    if len(exp1) > 1:
        for i in range (len(exp1)-1):
            eq2 = eq2  +"$$수식$$(" + str(exp1[i]) + " + " + str(1) + ") TIMES$$/수식$$"
    eq2 = eq2 +"$$수식$$(" + str(exp1[-1]) + " + " + str(1) + ")$$/수식$$ "

    bb = []
    while len(bb) < 4:
        k = np.random.randint(2, 10)
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

    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, eq=eq, eq2=eq2, answ=answ)

    return stem, answer, comment

#중1-1-1-34
def naturalnum111_Stem_026():
    stem = "$$수식$${num}$$/수식$$의 약수가 아닌것은?\n"\
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${list}$$/수식$$\n" \
              "따라서 $$수식$${num}$$/수식$$의 약수가 아닌 것은 $$수식$${ans}" \
              

    fac = [2, 3, 5]
    num1 = fac[np.random.randint(0,3)]
    ex1 = np.random.randint(1, 4)
    num2 = fac[np.random.randint(0,3)]
    ex2 = np.random.randint(1, 4)
    num3 = fac[np.random.randint(0,3)]
    ex3= np.random.randint(1, 4)
    while num1 == num2 or num1==num3 or num2==num3:
        num2 = fac[np.random.randint(0, 3)]
        num3 = fac[np.random.randint(0, 3)]


    answ1 = num1**ex1 * num2**ex2 * num3**ex3
    num_st = factor_equation(answ1)
    bb =[]
    cc=[]
    t=""
    while True:
        temp1 = np.random.randint(0, 5)
        temp2  = np.random.randint(0, 5)
        temp3 = np.random.randint(0, 5)
        v = num1**temp1 * num2**temp2 * num3**temp3
        if temp1<=ex1 and temp2<=ex2 and temp3<=ex3 and v < answ1 and v not in bb:
            t ="$$수식$$"+str(v) + " = $$/수식$$" + factor_equation(num1**temp1*num2**temp2*num3**temp3)+ "\n"
            if v==1:
                t =  "$$수식$$"+str(1) + "$$/수식$$ = $$수식$$" + str(1)+"$$/수식$$\n"
            cc.append(t)
            bb.append(v)
        if len(bb)==4:
            break
    bb.append(answ1)
    p = min(num1, num2)
    p = min(p, num3)
    answ_string=""
    answ = answ1 +1
    # print(ex1)
    # print(ex2)
    # print(ex3)

    while answ > answ1:
        temp1 = np.random.randint(0, 5)
        temp2 = np.random.randint(0, 5)
        temp3 = np.random.randint(0, 5)

        if p ==num1 and num1**(ex1+1) * num2**temp2 * num3**temp3 <answ1:
            answ = num1**(ex1+1) * num2**temp2 * num3**temp3
            ex1+=1
            ans_string = "$$수식$$" + str(answ) + " = $$/수식$$" + factor_equation(answ)+ "\n"

        elif p ==num2 and num1**(temp1) * num2**(ex2+1) * num3**temp3 < answ1:
            answ = num1**(temp1) * num2**(ex2+1) * num3**temp3
            ex2+=1
            ans_string = "$$수식$$" + str(answ) + " = $$/수식$$" + factor_equation(answ)+ "\n"

        elif p ==num3 and num1**(temp1) * num2**temp2 * num3**(ex3+1) < answ1:
            answ = num1**(temp1) * num2**temp2 * num3**(ex3+1)
            ex3+=1
            ans_string = "$$수식$$" + \
                str(answ) + " = $$/수식$$" + factor_equation(answ) + "\n"

    # print(ex2)
    # print(ex3)

    cc.append(ans_string)
    t=""
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
        t = "① " + cc[4] + "② " + cc[0] + "③ " + cc[1] + "④ " + cc[2] + "⑤ " + cc[3]
    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = bb[0]
        x3 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
        t = "① " + cc[0] + "② " + cc[4] + "③ " + cc[1] + "④ " + cc[2] + "⑤ " + cc[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = bb[0]
        x2 = bb[1]
        x4 = bb[2]
        x5 = bb[3]
        t = "① " + cc[0] + "② " + cc[1] + "③ " + cc[0] + "④ " + cc[2] + "⑤ " + cc[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x5 = bb[3]
        t = "① " + cc[0] + "② " + cc[1] + "③ " + cc[2] + "④ " + cc[4] + "⑤ " + cc[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = bb[0]
        x2 = bb[1]
        x3 = bb[2]
        x4 = bb[3]
        t = "① " + cc[0] + "② " + cc[1] + "③ " + cc[2] + "④ " + cc[3] + "⑤ " + cc[4]

    stem = stem.format(num=num_st, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num_st, list=t, ans=ans)

    return stem, answer, comment


#중1-1-1-35
def naturalnum111_Stem_027():
    stem = "$$수식$${num}$$/수식$$의 모든 약수의 합은?\n"\
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$ 이므로 $$수식$${num}$$/수식$$의 약수는\n" \
              "$$수식$$1 , {list}$$/수식$$\n" \
              "따라서 구하는 합은\n" \
              "$$수식$${ad_eq}$$/수식$$" \

    num = np.random.randint(0,200)
    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = "$$수식$${"+str(num) + "}$$/수식$$   = " + factor_equation(num)

    eq = fact_
    answ_list =[]

    for i in range(2, num+1):
        if num % i ==0 and i not in answ_list:
            answ_list.append(i)

    temp2 = []
    exp2 = []
    for q in answ_list:
        num_one = []
        count = 0
        i = 2
        n = q
        while n > 1:
            if n % i == 0:
                num_one.append(i)
                n = n / i
                i = i - 1
            i += 1
        num_one.sort()
        temp1 = []
        exp1 = []
        num_one.sort()
        for x in num_one:
            if x not in temp1:
                temp1.append(x)
        temp2.append(temp1)
        for x in temp1:
            i = 0
            for y in num_one:
                if x == y:
                    i += 1
            exp1.append(i)
        exp2.append(exp1)

    div_eq = ""
    answ = 0
    answ_eq = ""
    # print(exp2)
    # print(answ_list)
    if len(answ_list) > 1:
        for i in range(0, len(answ_list)):
            for j in range(0, len(exp2[i]) - 1):
                if exp2[i][j]!=1:
                    div_eq = div_eq + "$$수식$${" + str(temp2[i][j]) + "} ^{" + str(exp2[i][j]) + "} TIMES$$/수식$$"
                else:
                    div_eq = div_eq + "$$수식$${" + str(temp2[i][j]) + "} TIMES$$/수식$$"
            if len(exp2[i])>1:
                if exp2[i][-1]!=1:
                    div_eq = div_eq + "$$수식$${" + str(temp2[i][-1]) + "} ^ {" + str(exp2[i][-1]) + "}$$/수식$$ = $$수식$${" + str(answ_list[i]) + "} `,`$$/수식$$  "
                else:
                    div_eq = div_eq + "$$수식$${" + str(temp2[i][-1]) + "}$$/수식$$ = $$수식$${" + str(answ_list[i]) + "} `,`$$/수식$$ "
            else:
                if exp2[i][-1]!=1:
                    div_eq = div_eq + "$$수식$${" + str(temp2[i][-1]) + "} ^ {" + str(exp2[i][-1]) + "}$$/수식$$ = $$수식$${" + str(answ_list[i]) + "} `,`$$/수식$$ "
                else:
                    div_eq = div_eq + "$$수식$${" + str(temp2[i][-1]) + "} `,`$$/수식$$ "
        for i in range(0, len(answ_list) - 1):
            answ = answ + answ_list[i]
            answ_eq = answ_eq + "$$수식$${" + str(answ_list[i]) + " }   `+` $$/수식$$"
        answ = answ + answ_list[-1]
        answ_eq = answ_eq + "$$수식$${" + str(answ_list[-1]) + "}$$/수식$$  = $$수식$${" + str(answ) + "}$$/수식$$"
    else:
        div_eq =  str(num)
        answ_eq = "0 = 0"
    list = div_eq
    ad_eq ="$$수식$$1 +$$/수식$$ "
    answ =1
    for x in answ_list:
        answ = answ + x
    if len(answ_list) > 0:
        for i in range (len(answ_list)-1):
            ad_eq = ad_eq + "$$수식$${"  + str(answ_list[i]) + "} `+` $$/수식$$"
        ad_eq = ad_eq + "$$수식$${" + str(answ_list[-1]) + "}  `=`  {" + str(answ) + "}$$/수식$$"

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
    k = "k"

    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=list,  num=num, eq=eq, ad_eq=ad_eq)

    return stem, answer, comment

#중1-1-1-38
def naturalnum111_Stem_028():
    stem = "$$수식$${num}$$/수식$$  의 모든 약수의 개수가  $$수식$${total}$$/수식$$일 때, 자연수 $$수식$$a$$/수식$$" \
           "의 값은?\n"\
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$이므로\n" \
              "$$수식$${ans_eq} {ans}$$/수식$$"

    num1 = np.random.randint(2, 15)
    ex1 = np.random.randint(2, 5)
    num2 = np.random.randint(2, 15)
    ex2 = np.random.randint(2, 5)
    num3 = np.random.randint(2, 15)
    ex3 = np.random.randint(2, 5)
    while num1 == num2 or num2 == num3 or num1 == num3:
        num2 = np.random.randint(2, 15)
        num3 = np.random.randint(2, 15)
    total = (1+ex1) *(1+ ex2) *(1+ ex3)
    k = np.random.randint(0,3)
    a=1
    num=""
    eq=""
    ans_eq=""
    if k==0:
        a = ex1
        num =num + "$$수식$${" + str(num1) + "} ^{a} TIMES {" + str(num2) + "} ^{"+str(ex2)+"} TIMES {" + str(num3) + "} ^{"+str(ex3)+"}$$/수식$$"
        eq = eq + "(a + 1)`TIMES`({" + str(ex2) + "} + 1)`TIMES` ({" + str(ex3) + "} + 1) = " + "{" + str(total) + "}"
    elif k==1:
        a = ex2
        num = num + "$$수식$${" + str(num1) + "} ^{"+str(ex1)+"} TIMES {" + str(num2) + "} ^{a} TIMES {" + str(num3) + "} ^{" + str(ex3) + "}$$/수식$$"
        eq = eq + "(" + str(ex1) + " + 1) `TIMES` ({a} + 1) `TIMES` ({" + str(ex3) + "} + 1) = " + "{" + str(total) + "}"
    else:
        a = ex3
        num = num + "$$수식$${" + str(num1) + "} ^{" + str(ex1) + "} TIMES {" + str(num2) + "} ^{" + str(ex2) + "} TIMES {" + str(num3) + "} ^{a}$$/수식$$"
        eq = eq + "(" + str(ex1) + " + 1) `TIMES` ({" + str(ex2) + "} + 1) `TIMES` ({a} + 1) = " + "{" + str(total) + "}"

    ans_eq = "$$수식$$a + 1 $$/수식$$= $$수식$${" + str(a+1) + "}$$/수식$$"
    ans2 = "$$수식$$a$$/수식$$ = $$수식$${" + str(a) + "}$$/수식$$"
    answ = a
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
    k = "k"

    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, total=total)
    answer = answer.format(ans=ans)
    comment = comment.format(ans_eq=ans_eq, num=num, eq=eq,ans=ans2)

    return stem, answer, comment


#중1-1-1-39
def naturalnum111_Stem_029():
    stem = "$$수식$${num} TIMES$$/수식$$ □의 모든 약수의 개수가 $$수식$${total}$$/수식$$일 때, 다음 중 □" \
           "안에 들어갈 수 있는 값은?\n"\
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "{liste}" \
              "따라서 □ 안에 들어갈 수 있는 것은 {ans}"
    fac = [3,5,7,11]
    num = np.random.randint(10, 50)
    r_num = np.random.randint(2, 6)
    temp_num = num*r_num
    num_one = []
    temp1 = []
    exp1 = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = "{" + str(num) + "}`TIMES`{" + str(r_num) + "}`=`"
    fact_ = fact_ + factor_equation(num)

    answ_fact1 = fact_
    total=1
    for x in exp1:
        total = total * (x + 1)
    answ_expo =""
    for i in range (0, len(exp1)-1):
        answ_expo =  answ_expo +"({" + str(exp1[i]) + "}  + 1) `TIMES`"
    answ_expo = answ_expo + "({" + str(exp1[-1]) + "}  + 1) `=`{" + str(total) + "} \n"
    fact_ = fact_ + answ_expo
    fal_num =[]
    fal_exp1 =[]
    while len(fal_num) < 4:
        false_number = np.random.randint(2, 10)
        if false_number*num not in fal_num and false_number*num!=r_num and false_number not in fal_exp1:
            fal_exp1.append(false_number)
            fal_num.append(false_number*num)
    temp2 = []
    exp2 = []
    for q in fal_num:
        num_one = []
        count = 0
        i = 2
        n = q
        while n > 1:
            if n % i == 0:
                num_one.append(i)
                n = n / i
                i = i - 1
            i += 1
        num_one.sort()
        temp1 = []
        exp1 = []
        num_one.sort()
        for x in num_one:
            if x not in temp1:
                temp1.append(x)
        temp2.append(temp1)
        for x in temp1:
            i = 0
            for y in num_one:
                if x == y:
                    i += 1
            exp1.append(i)
        exp2.append(exp1)
    div_eq= ""
    bb=[]
    fal_exp = []
    for x in exp2:
        f=0
        for y in x:
            f = f + y + 1
        fal_exp.append(f)
    # print(num)
    # print(r_num)
    # print(fal_num)
    # print(temp2)
    # print(exp2)
    if len(fal_num) > 0:
        for i in range(0, len(fal_num)):
            div_eq = "$$수식$${" + str(num) + "}`TIMES`{" + str(fal_exp1[i]) + "=$$/수식$$"
            for j in range(0, len(exp2[i]) - 1):
                if exp2[i][j]!=1:
                    div_eq = div_eq + " $$수식$${" + str(temp2[i][j]) + "} ^{" + str(exp2[i][j]) + "}`TIMES`$$/수식$$"
                else:
                    div_eq = div_eq + "$$수식$${" + str(temp2[i][j]) + "}`TIMES`$$/수식$$"
            if exp2[i][-1]!=1:
                div_eq = div_eq +" $$수식$${" + str(temp2[i][-1]) + "} ^ {" + str(exp2[i][-1]) + "}$$/수식$$이므로 약수의 개수는 \n"
            else:
                div_eq = div_eq + " $$수식$${" + str(temp2[i][-1]) + "}$$/수식$$이므로 약수의 개수는 \n"
            for j in range(0, len(exp2[i])-1):
                div_eq = div_eq + "$$수식$$(" + str(exp2[i][j]) + " + 1) `TIMES`$$/수식$$"
            div_eq = div_eq + "$$수식$$({" + str(exp2[-1][-1]) + "} + 1) `=` " + "{" + str(fal_exp[-1]) + "}$$/수식$$\n"
            bb.append(div_eq)
    num_one = []
    temp1 = []
    exp1 = []
    i = 2
    n = num*r_num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = "$$수식$${" + str(num) + "}`TIMES`{" + str(r_num) + "} = $$/수식$$"
    fact_ = fact_ + factor_equation(num*r_num) + "이므로 약수의 개수는 \n"

    answ_fact1 = fact_
    total = 1
    for x in exp1:
        total = total * (x + 1)
    answ_expo = ""
    if len(exp1) > 0:
        for i in range(0, len(exp1) - 1):
            answ_expo = answ_expo + "$$수식$$ ({" + str(exp1[i]) + "} + 1)  `TIMES`$$/수식$$"
        answ_expo = answ_expo + "$$수식$$({" + str(exp1[-1]) + "} + 1) `=` {" + str(total) + "}$$/수식$$\n"
        fact_ = fact_ + answ_expo

    bb.append(fact_)
    # print(len(bb))
    rande = np.random.randint(1, 6)
    answ = r_num
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = fal_exp1[0]
        x3 = fal_exp1[1]
        x4 = fal_exp1[2]
        x5 = fal_exp1[3]

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = fal_exp1[0]
        x3 = fal_exp1[1]
        x4 = fal_exp1[2]
        x5 = fal_exp1[3]
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = fal_exp1[0]
        x2 = fal_exp1[1]
        x4 = fal_exp1[2]
        x5 = fal_exp1[3]
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = fal_exp1[0]
        x2 = fal_exp1[1]
        x3 = fal_exp1[2]
        x5 = fal_exp1[3]
    else:
        ans = "⑤"
        x5 = answ
        x1 = fal_exp1[0]
        x2 = fal_exp1[1]
        x3 = fal_exp1[2]
        x4 = fal_exp1[3]

    liste=""
    if rande == 1:
        liste = "① " + bb[4] + "② " + bb[0] + "③ " + bb[1] + "④ " + bb[2] + "⑤ " + bb[3] 
    elif rande == 2:
        liste = "① " + bb[0] + "② " + bb[4] + "③ " + bb[1] + "④ " + bb[2] + "⑤ " + bb[3]
    elif rande == 3:
        liste = "① " + bb[0] + "② " + bb[1] + "③ " + bb[4] + "④ " + bb[2] + "⑤ " + bb[3]
    elif rande == 4:
        liste = "① " + bb[0] + "② " + bb[1] + "③ " + bb[2] + "④ " + bb[4] + "⑤ " + bb[3]
    else:
        liste = "① " + bb[0] + "② " + bb[1] + "③ " + bb[2] + "④ " + bb[3] + "⑤ " + bb[4]

    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, total=total)
    answer = answer.format(ans=ans)
    comment = comment.format(ans=ans, liste=liste)

    return stem, answer, comment




#중1-1-1-40
def naturalnum111_Stem_030():
    stem = "$$수식$${num1} TIMES {num2} TIMES {u}  $$/수식$$의 약수의 개수가 $$수식$${total}$$/수식$$일 때, $$수식$${u}$$/수식$$ 안에 들" \
           "어갈 수 있는 가장 작은 자연수는?\n"\
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${num1} TIMES {num2} TIMES {u} $$/수식$$의 약수의 개수가 $$수식$${total}  $$/수식$$ {temp}$$수식$$ $$/수식$$ 되려면\n" \
              "(i) $$수식$${expl1}  $$/수식$$ 에서 $$수식$${expl11}$$/수식$$\n" \
              "(ii) $$수식$${expl2}  $$/수식$$ 에서 $$수식$${expl21}$$/수식$$\n" \
              "(iii) $$수식$${expl3}$$/수식$$\n" \
              "따라서 (i), (ii), (iii)에 의해 $$수식$${u}  $$/수식$$안에 들어갈 수\n" \
              "있는 가장 작은 자연수는 $$수식$${answ}$$/수식$$이다." \

    fac = [2,3,5,7,11,13,17,19]

    num1 = fac[np.random.randint(0, 7)]
    num2 = fac[np.random.randint(0, 7)]
    while num1 == num2:
        num2 = fac[np.random.randint(0, 7)]
    if num1 > num2:
        em = num2
        num2 = num1
        num1 = em
    total = np.random.randint(5, 15)
    while total% 2 !=0 or total==8:
        total = np.random.randint(5, 15)
    op = [num1, num2]
    for x in fac:
        if x!= num1 and x!=num2:
            op.append(x)
    one_fact =""
    for i in range (0, 3):
        if fac[i]!= num1 and fac[i]!=num2:
            if int(total-(total/2))-2!=1:
                one_fact = one_fact +"$$수식$${" + str(fac[i]) + "} ^{" + str(int(total-(total/2))-2) + "}$$/수식$$, "
            else:
                one_fact = one_fact + "$$수식$${" + str(fac[i]) + "}$$/수식$$, "
    op.sort()
    answ1 = op[0]
    for x in op:
        answ1 = min(answ1, x)
        if int(total - (total / 2)) - 2== 1:
            answ = "$$수식$${" + str(answ1) + "}$$/수식$$"
        elif int(total - (total / 2)) - 2 ==0:
            answ = str(1)
        else:
            answ = "$$수식$${" + str(answ1) + "} ^{" + str(int(total - (total / 2)) - 2) + "}$$/수식$$"
    if total % 4 !=0:
        answ1 = min(num1,num2)
        if int(total - (total / 2)) - 2 == 1:
            answ = "$$수식$${" + str(answ1) + "}$$/수식$$"
        elif int(total - (total / 2)) - 2 == 0:
            answ = str(1)
        else:
            answ = "$$수식$${" + str(answ1) + "} ^{" + str(int(total - (total / 2)) - 2) + "}$$/수식$$"
    expl1 = "$$수식$${" + str(num1) + "} TIMES {" + str(num2) + "} TIMES {□}$$/수식$$  = "
    expl1 = expl1 + "$$수식$${" + str(num1) + "} ^{" + str(int((total/2)-1)) + "} TIMES {" + str(num2) + "}$$/수식$$"
    expl11 =  "$$수식$${□}$$/수식$$  =$$수식$${" + str(num1) + "} ^{" + str(int(total-(total/2))-2) +"}$$/수식$$  = $$수식$${" + str(int(num1**(int(total-(total/2))-2))) + "}$$/수식$$"

    expl2 = "$$수식$${" + str(num1) + "} TIMES {" + str(num2) + "} TIMES {□}$$/수식$$ = "
    expl2 = expl2 + "$$수식$${" + str(num1) + "} TIMES {" + str(num2) + "}^{" + str(int((total / 2) - 1)) +"$$/수식$$"
    expl21 = "$$수식$${□}$$/수식$$  =$$수식$${" + str(num2) + "} ^{" + str(int(total -(total / 2))-2) + "}$$/수식$$ = $$수식$${" + str(int(num2**(total -(int(total/2))-2))) + "}$$/수식$$"

    expl3 = "$$수식$${" + str(num1) + "} TIMES {" + str(num2) + "} TIMES {□}$$/수식$$ 에서 $$수식$${□}$$/수식$$는 $$수식$${" + str(num1) + "}$$/수식$$" + proc_jo(num1,2) + " $$수식$${" + str(num2) + "}$$/수식$$" + proc_jo(num2,0)+ "아닌 다른 소수이어\n" \
                                                                                                                                                                                                                                          "야 하므로 $$수식$${□}$$/수식$$ =" + one_fact + "$$수식$${CDOTS}$$/수식$$"
    expl31 = "따라서 "
    bb = []
    while len(bb) < 4:
        k = fac[np.random.randint(0, 7)]
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
    temp = proc_jo(total,0)
    stem = stem.format(u="□", num1=num1, num2=num2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, total=total)
    answer = answer.format(ans=ans)
    comment = comment.format(temp=temp,u="□", num1=num1, expl1=expl1, expl2=expl2, expl3=expl3, num2=num2, expl11=expl11, expl21=expl21, answ=answ, total=total)

    return stem, answer, comment

#중1-1-1-42
##Zzzzz
def naturalnum111_Stem_031():
    stem = "$$수식$${num1}$$/수식$$의 약수의 개수와  $$수식$${eq}의 약수의 개수" \
           "가 같을 때, 자연수 $$수식$$a$$/수식$$의 값은?\n"\
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "{num_eq} 약수의 개수는\n" \
              "{fac_eq} = $$수식$${total}$$/수식$$\n" \
              "{eq} 의 약수의 개수는\n" \
              "{fac_eq2} = {a_eq2}\n"\
              "따라서  {a_eq2} = $$수식$${total}$$/수식$$ 이므로\n" \
              "$$수식$$ a `+` 1 = {answ_1}$$/수식$$  " \
              "∴$$수식$$a `=`{answ}$$/수식$$" \

    fac = [2, 3, 5, 7, 11, 13, 17, 19]
    num11 = fac[np.random.randint(0, 7)]
    numm = np.random.randint(1, 5)
    num12 = fac[np.random.randint(0, 7)]
    nummm = np.random.randint(1, 5)
    num13 = fac[np.random.randint(0, 7)]
    numw = np.random.randint(1, 5)
    while num11 == num12 or num12 == num13 or num11 ==num13:
        num12 = fac[np.random.randint(0, 7)]
        num13 = fac[np.random.randint(0, 7)]
    num1 = num11**numm*num12**nummm*num13**numw
    while num1 > 500:
        num11 = fac[np.random.randint(0, 7)]
        numm = np.random.randint(1, 5)
        num12 = fac[np.random.randint(0, 7)]
        nummm = np.random.randint(1, 5)
        num13 = fac[np.random.randint(0, 7)]
        numw = np.random.randint(1, 5)
        while num11 == num12 or num12 == num13 or num11 == num13:
            num12 = fac[np.random.randint(0, 7)]
            num13 = fac[np.random.randint(0, 7)]
        num1 = num11 ** numm * num12 ** nummm * num13 ** numw
    fact_ = "$$수식$${" + str(num1) + "}$$/수식$$" + "=" + factor_equation(num1)
    exp1 = factor_power(num1)
    num_eq =  fact_
    total=1
    for x in exp1:
        total = total * (x + 1)


    fac_eq=""
    eq=""
    if len(exp1) > 1:
        for i in range(0, len(exp1)-1):
            fac_eq = fac_eq +  "$$수식$$(" + str(exp1[i]) + " + 1) `TIMES`$$/수식$$"
    fac_eq = fac_eq + "($$수식$${" + str(exp1[-1]) + "} `+` 1)$$/수식$$ "

    num21 = fac[np.random.randint(0, 7)]
    num22 = fac[np.random.randint(0, 7)]
    num23 = fac[np.random.randint(0, 7)]
    while num21 == num22 or num22 == num23 or num21 ==num23:
        num22 = fac[np.random.randint(0, 7)]
        num23 = fac[np.random.randint(0, 7)]


    ex11 = numm
    ex21 = nummm
    ex31 = numw

    fac_eq2 =""
    eq=""
    a_eq2 =""
    answ_1 =0
    answ=0

    k = np.random.randint(0, 3)
    if k == 0:
        a = ex11
        eq = eq + "$$수식$${" + str(num21) + "} ^{a} TIMES$$/수식$$"
        if ex21!=1:
            eq = eq + "$$수식$${" + str(num22) + "} ^{" + str(ex21) + "} TIMES$$/수식$$"
        else:
            eq = eq + "$$수식$${" + str(num22) + "} TIMES$$/수식$$"
        if ex31!=1:
             eq = eq +"$$수식$${" + str(num23) + "} ^ {" + str(ex31) + "}$$/수식$$"
        else:
            eq = eq + "$$수식$${" + str(num23) + "}$$/수식$$"
        fac_eq2 = fac_eq2 + "$$수식$$(a + 1) `TIMES` ({" + str(ex21) + "} + 1) `TIMES`({" + str(ex31) + "}+ 1) $$/수식$$"
        a_eq2 = "$$수식$${" + str((ex21 + 1)*(ex31 + 1)) + "} `TIMES`(a + 1)$$/수식$$ "
        answ_1 = int(total/((ex21 + 1)*(ex31 + 1)))
    elif k == 1:
        a = ex21
        if ex11!=1:
            eq = eq + "$$수식$${" + str(num21) + "} ^{" + str(ex11) + "} TIMES$$/수식$$"
        else:
            eq = eq + "$$수식$${" + str(num21) + "} TIMES$$/수식$$"
        eq = eq + "$$수식$${" + str(num22) + "} ^ {a} TIMES$$/수식$$"
        if ex31!=1:
            eq = eq + "$$수식$${" + str(num23) + "} ^ {" + str(ex31) + "}$$/수식$$"
        else:
            eq = eq + "$$수식$${" + str(num23) + "}$$/수식$$"
        fac_eq2 = fac_eq2 + "$$수식$$(" + str(ex11) + " + 1) `TIMES`({a} `+` 1) `TIMES` ({" + str(ex31) + "} + 1) $$/수식$$"
        a_eq2 = "$$수식$${" + str((ex11 + 1)*(ex31 + 1)) + "}`TIMES`(a`+`1)$$/수식$$"
        answ_1 = int(total/((ex11 + 1)*(ex31 + 1)))
    else:
        a = ex31
        if ex11 != 1:
            eq = eq + "$$수식$${" + str(num21) + "} ^{" + str(ex11) + "} TIMES$$/수식$$"
        else:
            eq = eq + "$$수식$${" + str(num21) + "} TIMES$$/수식$$"
        if ex21 != 1:
            eq = eq + "$$수식$${" + str(num22) + "} ^ {" + str(ex21) + "}TIMES$$/수식$$"
        else:
            eq = eq + "$$수식$${" + str(num22) + "}TIMES$$/수식$$"
        eq = eq + "$$수식$${" + str(num23) + "} ^{a}$$/수식$$"
        fac_eq2 = fac_eq2 + "$$수식$$(" + str(ex11) + " + 1)`TIMES`({" + str(ex21) + "} + 1) `TIMES` ({a}`+` 1)$$/수식$$ "
        a_eq2 = "$$수식$${" + str((ex11 + 1)*(ex21 + 1)) + "} TIMES`(a + 1)$$/수식$$  "
        answ_1 = int(total/((ex21 + 1)*(ex11 + 1)))

    answ = answ_1 - 1

    bb = []
    while len(bb) < 4:
        k = fac[np.random.randint(0, 7)]
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

    stem = stem.format(num1=num1, eq=eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, total=total)
    answer = answer.format(ans=ans)
    comment = comment.format(num_eq=num_eq, fac_eq=fac_eq, eq=eq, fac_eq2=fac_eq2, a_eq2=a_eq2, answ_1=answ_1, answ=answ, total=total)

    return stem, answer, comment

#중1-1-1-43
def naturalnum111_Stem_032():
    stem = "$$수식$${num1} ^{ep1} TIMES$$/수식$$ a 의 약수의 개수와  $$수식$${total}일 때, 다음 중 자연수 " \
           "$$수식$$a$$/수식$$의 값이 될 수 있는 것은?\n"\
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "{list}\n" \
              "따라서 a의 값이 될 수 있는 것은 {ans}" \
              "이다." \

    fac = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    num1 = fac[np.random.randint(0, 7)]
    exp11 = np.random.randint(2, 5)
    ep1 = exp11
    part1_ = "$$수식$${" + str(num1) + "} ^{" + str(exp11) + "} TIMES$$/수식$$"
    a = np.random.randint(2, 30)
    num = num1**exp11 * a
    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    total = 1
    for x in exp1:
        total = total * (x + 1)

    num_one = []
    i = 2
    n = a
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = factor_equation(a)
    a_fact = fact_
    answ = a_fact
    bb=[]
    answ_list=[]
    cc = []
    b = np.random.randint(0,2)
    # print(a_fact)
    while len(answ_list) < 4:
        if b ==0:
            k =  fac[np.random.randint(0, 8)]
            ep_temp = np.random.randint(1, 8)
            while k==num1 or k**ep_temp == a or (ep_temp + 1)*(exp11+1) == total:
                k = fac[np.random.randint(0, 8)]
                ep_temp = np.random.randint(1, 8)
            cc.append("$$수식$${" + str(k) + "} ^{" + str(ep_temp) + "}$$/수식$$")
            answ_list.append(k**ep_temp)
            layout = part1_ + cc[-1] + " 의 약수의 개수는\n($$수식$${" + str(exp11) + "} + 1) TIMES$$/수식$$ ($$수식$${" + str(ep_temp) + "} + 1) `=` {" + str((exp11+1)*(ep_temp+1)) + "}$$/수식$$\n"
            bb.append(layout)
        else:
            k1 = fac[np.random.randint(0, 8)]
            ep_temp1 = np.random.randint(1, 8)
            k2 = fac[np.random.randint(0, 8)]
            while k1 == num1 or k2 == num1 or k1 ** ep_temp1 * k2 == a or (ep_temp1 + 1 )*(exp11+1) == total or (ep_temp1 + 2 )*(exp11+1) == total:
                k1 = fac[np.random.randint(0, 8)]
                ep_temp1 = np.random.randint(1, 8)
                k2 = fac[np.random.randint(0, 8)]
            if k1 == k2:
                cc.append("$$수식$${" + str(k1) + "} ^{" + str(ep_temp1+1) + "}$$/수식$$")
                answ_list.append(k1 ** ep_temp1)
                layout = part1_ + cc[-1] + " 의 약수의 개수는\n($$수식$${" + str(exp11) + "} + 1) TIMES$$/수식$$ ($$수식$${" + str(ep_temp1+1) + "}+ 1) `=` {" + str((exp11 + 1) * (ep_temp1 + 2)) + "}$$/수식$$\n"
                bb.append(layout)
            else:
                cc.append("$$수식$${" + str(k1) + "} ^{" + str(ep_temp1) + "} TIMES {" + str(k2) + "}$$/수식$$")
                answ_list.append(k1 ** ep_temp1*k2)
                layout = part1_ + cc[-1] + " 의 약수의 개수는\n($$수식$${" + str(exp11) + "}+ 1) TIMES$$/수식$$ ($$수식$${" + str(ep_temp1) + "}+ 1)  $$수식$$TIMES` (`1 `+` 1`)`=` {" + str((exp11 + 1) * (ep_temp1 + 1)*2) + "}$$/수식$$\n"
                bb.append(layout)
    answ_string = part1_ + a_fact + " 의 약수의 개수는\n($$수식$${" + str(exp11) + "}+ 1) TIMES$$/수식$$"
    for i in range(0, len(temp1)):
        if temp1[i] == num1:
            exp11 = exp11 + exp1[i]
            exp1.remove(exp1[i])
    if len(exp1) >0:
        for i in range (0, len(exp1)-1):
            answ_string = answ_string + "($$수식$${" + str(exp1[i]) + "}+ 1)  TIMES$$/수식$$"
        answ_string = answ_string + "($$수식$${" + str(exp1[-1]) + "} + 1) `=` {" + str(total) + "}$$/수식$$\n"
    bb.append(answ_string)


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
        liste = "① " + bb[4] + "② " + bb[0] + "③ " + bb[1] + "④ " + bb[2] + "⑤ " + bb[3]
    elif rande == 2:
        liste = "① " + bb[0] + "② " + bb[4] + "③ " + bb[1] + "④ " + bb[2] + "⑤ " + bb[3]
    elif rande == 3:
        liste = "① " + bb[0] + "② " + bb[1] + "③ " + bb[4] + "④ " + bb[2] + "⑤ " + bb[3]
    elif rande == 4:
        liste = "① " + bb[0] + "② " + bb[1] + "③ " + bb[2] + "④ " + bb[4] + "⑤ " + bb[3]
    else:
        liste = "① " + bb[0] + "② " + bb[1] + "③ " + bb[2] + "④ " + bb[3] + "⑤ " + bb[4]




    stem = stem.format(num1=num1, ep1=ep1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, total=total)
    answer = answer.format(ans=ans)
    comment = comment.format(list=liste,  ans=ans)

    return stem, answer, comment



#중1-1-1-44

def naturalnum111_Stem_033():
    stem = "$$수식$${num1}$$/수식$$ 이하의 자연수 중 약수의 개수가 $$수식$${num2}$$/수식$$인 수의 개수는?\n"\
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "약수의 개수가 $$수식$${num2}$$/수식$$ 인 자연수는 {ee}꼴로 소인수분해된다. \n" \
              "따라서 구하는 수는\n" \
              "$$수식$${list}$$/수식$$\n" \
              "의 $$수식$${answ}$$/수식$$ 개이다"

    num1 = np.random.randint(50, 600)
    num2 = 3
    ee="$$수식$$(소수$$수식$$)^2$$/수식$$"
    if num2 ==4:
        ee = "$$수식$$(소수$$수식$$)^3$$/수식$$이나 $$수식$$(소수$$수식$$)TIMES$$수식$$(소수$$수식$$)"
    num3 = num2 -1
    k = []
    list =""
    for i in range (2, num1):
        aaa = factor_power(i)
        sum = 1
        for x in aaa:
            sum *= (1+x)
        if sum == num2:
            k.append(i)
    for i in range(0, len(k)-1):
        list = list + factor_equation(k[i]) +" = $$수식$${" + str(k[i]) + "}$$/수식$$,   "
    list = list + factor_equation(k[-1]) +" = $$수식$${" + str(k[-1]) + "}$$/수식$$"
    answ = len(k)

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


    stem = stem.format(num1=num1, num2=num2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(ee=ee, list=list, num3=num3, num2=num2, answ=answ)

    return stem, answer, comment




#중1-1-1-45
#분수가 안됨
def naturalnum111_Stem_034():
    stem = "$$수식$${ttmp}$$/수식$$  이 자연수가 되게 하는 자연수 $$수식$$n$$/수식$$의 값" \
           "들의 합은?\n"\
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "

    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${ttmp}$$/수식$$이 자연수가 되려면 $$수식$${num2}$$/수식$$ {temp10} $$수식$${num1}$$/수식$$의" \
              "약수이어야 한다.\n" \
              "이때 $$수식$${eq}$$/수식$$ 이므로 $$수식$${num1}$$/수식$$의 약수는 $$수식$${list}$$/수식$$" \
              "$$수식$$ $$/수식$$이다.\n" \
              "$$수식$${list2}$$/수식$$\n" \
              "따라서 $$수식$${ttmp}$$/수식$$이 자연수가 되게 하는 자연수\n" \
              "$$수식$$n$$/수식$$의 값들을 합은 $$수식$${ans_eq}{answ}$$/수식$$" \

    num1 = np.random.randint(50, 200)
    list = ""
    answ_list = []
    for i in range (2, num1+1):
        if num1 % i ==0 and i not in answ_list:
            answ_list.append(i)
    if len(answ_list)>1:
        for i in range(0, len(answ_list)-1):
            list = list + "$$수식$${" + str(answ_list[i]) + "}$$/수식$$,  "
    list = list + "$$수식$${" + str(answ_list[-1]) + "}$$/수식$$"

    num_one = []
    i = 2
    n = num1
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = "$$수식$${" + str(num1) + "}$$/수식$$  = " + factor_equation(num1)

    eq = fact_
    # print(answ_list)
    num2_temp = np.random.randint(2, 10)
    num2_total=0
    if len(answ_list) >1:
        num2_total = answ_list[np.random.randint(0, len(answ_list))]
    num2_total = answ_list[-1]
    while num2_temp > num2_total or num2_total % num2_temp == 0:
        num2_temp = np.random.randint(2, 10)
        num2_total = 0
        if len(answ_list) > 1:
            num2_total = answ_list[np.random.randint(0, len(answ_list))]
        num2_total = answ_list[-1]
        num2_total = answ_list[np.random.randint(1, len(answ_list) - 1)]
    answ_temp = num2_total / num2_temp
    num2_remainder = num2_total % num2_temp
    #num2 = str(num2_temp) + "TIMESn-" + str(num2_remainder)

    num2="{%s}`TIMES`n-{%s}"%(num2_temp, num2_remainder)

    ttmp="{%s}over {%s}"%(num1,num2)

    answ_op = []

    list2 = ""
    answ = 0
    tt =[]
    for x in answ_list:
        if (x + num2_remainder) % num2_temp ==0:
            tt.append(int(((x + num2_remainder) / num2_temp)))
            answ = answ + int(((x + num2_remainder) / num2_temp))
            list2 = list2 + "$$수식$${" + num2 + "}$$/수식$$ = " + "$$수식$${" + str(x) + "} ` `$$/수식$$☞ $$수식$${" + str(int((x + num2_remainder) / num2_temp) )+ "}$$/수식$$\n"
        else:
            list2 = list2 + "$$수식$${" +num2  + "}$$/수식$$ = " + "$$수식$${" + str(x) + "} ` `$$/수식$$☞ $$수식$${" + str(x + num2_remainder) + "} over {" + str(num2_temp) + "}$$/수식$$\n"


    while answ ==0:
        num1 = np.random.randint(50, 200)
        list = ""
        answ_list = []
        for i in range(2, num1 + 1):
            if num1 % i == 0 and i not in answ_list:
                answ_list.append(i)
        if len(answ_list) > 1:
            for i in range(0, len(answ_list) - 1):
                list = list + "$$수식$${" + str(answ_list[i]) + "}$$/수식$$,  "
        list = list + "$$수식$${" + str(answ_list[-1]) + "}$$/수식$$"

        num_one = []
        i = 2
        n = num1
        while n > 1:
            if n % i == 0:
                num_one.append(i)
                n = n / i
                i = i - 1
            i += 1
        num_one.sort()
        temp1 = []
        exp1 = []
        num_one.sort()
        for x in num_one:
            if x not in temp1:
                temp1.append(x)
        for x in temp1:
            i = 0
            for y in num_one:
                if x == y:
                    i += 1
            exp1.append(i)
        fact_ = "$$수식$${" + str(num1) + "}$$/수식$$  = " + factor_equation(num1)

        eq = fact_
        # print(answ_list)
        num2_temp = np.random.randint(2, 10)
        num2_total = 0
        if len(answ_list) > 1:
            num2_total = answ_list[np.random.randint(0, len(answ_list))]
        num2_total = answ_list[-1]
        while num2_temp > num2_total or num2_total % num2_temp == 0:
            num2_temp = np.random.randint(2, 10)
            num2_total = 0
            if len(answ_list) > 1:
                num2_total = answ_list[np.random.randint(0, len(answ_list))]
            num2_total = answ_list[-1]
            num2_total = answ_list[np.random.randint(1, len(answ_list) - 1)]
        answ_temp = num2_total / num2_temp
        num2_remainder = num2_total % num2_temp
        #num2 = str(num2_temp) + "TIMESn-" + str(num2_remainder)

        num2="{%s}`TIMES`n-{%s}"%(num2_temp, num2_remainder)
        answ_op = []

        list2 = ""
        answ = 0
        tt = []
        for x in answ_list:
            if (x + num2_remainder) % num2_temp == 0:
                tt.append(int(((x + num2_remainder) / num2_temp)))
                answ = answ + int(((x + num2_remainder) / num2_temp))
                list2 = list2 + "$$수식$${" + num2 + "}$$/수식$$ = " + "$$수식$${" + str(
                    x) + "} ` `$$/수식$$☞ $$수식$${" + str(
                    int((x + num2_remainder) / num2_temp)) + "}$$/수식$$\n"
            else:
                list2 = list2 + "$$수식$${" +num2  + "}$$/수식$$ = " + "$$수식$${" + str(x) + "} ` `$$/수식$$☞ $$수식$${" + str(x + num2_remainder) + "} over {" + str(num2_temp) + "}$$/수식$$\n"


    ans_eq=""
    if len(tt)>1:
        for i in range(len(tt)-1):
            ans_eq = ans_eq + "$$수식$${" + str(tt[i]) + "}$$/수식$$ + "
        ans_eq = ans_eq + "$$수식$${" + str(tt[-1]) + "}$$/수식$$    $$수식$$`=`$$/수식$$ "
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
    temp10 = proc_jo(num2_remainder,0)
    stem = stem.format(ttmp=ttmp,num1=num1,num2=num2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(ttmp=ttmp,temp10=temp10, num2_temp=num2_temp,num2_remainder=num2_remainder , ans_eq=ans_eq, eq=eq, num1=num1, list=list, num2=num2, answ=answ, list2=list2)

    return stem, answer, comment



#중1-1-1-46
def naturalnum111_Stem_035():
    stem = "$$수식$${num}$$/수식$$의 약수 중 홀수의 개수는?\n"\
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "

    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "두 수의 곱이 홀수가 되는 경우는\n" \
              "$$수식$$($$/수식$$홀수$$수식$$) TIMES ($$/수식$$홀수$$수식$$)$$/수식$$ 인 경우 밖에 없다.\n" \
              "즉, $$수식$${num}$$/수식$$ 의 약수 중 홀수는\n" \
              "{odd_prime} 의 꼴이다.\n" \
              "따라서 구하는 홀수의 개수는\n" \
              "{eq}"
    fac = [2, 3, 5, 7, 11, 13, 17, 19]
    num1 = fac[np.random.randint(0, 7)]
    exp1 = np.random.randint(1, 7)
    num2 = fac[np.random.randint(0, 7)]
    num3 = fac[np.random.randint(0, 7)]
    exp2 = np.random.randint(1, 7)
    exp3 = np.random.randint(1, 7)
    while num1 == num2 or num1 == num3 or num2 == num3:
        num2 = fac[np.random.randint(0, 7)]
        num3 = fac[np.random.randint(0, 7)]
    answ_list = []
    answ=1
    eq=""
    odd_prime =""
    if num1 % 2!=0:
        answ_list.append(exp1)
        answ = (exp1+1) * answ
        if num2 % 2 !=0 or num3 % 2!=0:
            if exp1!=1:
                odd_prime = odd_prime + "($$수식$${"+str(num1)+"} ^{"+str(exp1)+"}$$/수식$$ 의 약수) $$수식$$TIMES$$/수식$$"
            else:
                odd_prime = odd_prime + "($$수식$${" + str(num1) + "}$$/수식$$ 의 약수) $$수식$$TIMES$$/수식$$"
            #eq = eq + "($$수식$${" + str(exp1) + "}$$/수식$$ + 1) $$수식$$TIMES$$/수식$$"
            eq = eq+"$$수식$$("+str(exp1)+"+1) `TIMES`$$/수식$$"
        else:
            if exp1!=1:
                odd_prime = "($$수식$${" + str(num1) + "} ^{" + str(exp1) + "}$$/수식$$ 의 약수) "
            else:
                odd_prime = "($$수식$${" + str(num1) + "}$$/수식$$ 의 약수) "
            #eq = eq + "($$수식$${" + str(exp1) + "}$$/수식$$ + 1) $수식$$$$/수식$$"
            eq = eq+"("+str(exp1)+"+1)"
    if num2 % 2!=0:
        answ_list.append(exp1)
        answ = (exp2+1) * answ
        if num3 % 2!=0:
            if exp2!=1:
                odd_prime = odd_prime + "($$수식$${"+str(num2)+"} ^{"+str(exp2)+"}$$/수식$$ 의 약수 ) $$수식$$TIMES$$/수식$$"
            else:
                odd_prime = odd_prime + "($$수식$${" + str(num2) + "}$$/수식$$ 의 약수) $$수식$$TIMES$$/수식$$"
            #eq = eq + "($$수식$${" + str(exp2) + "}$$/수식$$ + 1) TIMES$$/수식$$"
            eq = eq+"$$수식$$("+str(exp2)+"+1)`TIMES`$$/수식$$"
        else:
            if exp2!=1:
                odd_prime = odd_prime + "($$수식$${" + str(num2) + "} ^{" + str(exp2) + "}$$/수식$$ 의 약수 )"
            else:
                odd_prime = odd_prime + "($$수식$${" + str(num2) + "}$$/수식$$ 의 약수)"
            #eq = eq + "($$수식$${" + str(exp2) + "}$$/수식$$ + 1) "
            eq = eq+"$$수식$$("+str(exp1)+"+1)$$/수식$$"

    if num3 % 2!=0:
        answ_list.append(exp1)
        answ = (exp3+1) * answ
        if exp3!=1:
            odd_prime = odd_prime + "($$수식$${" + str(num3) + "} ^{" + str(exp3) + "}$$/수식$$ 의 약수) "
        else:
            odd_prime = odd_prime + "($$수식$${" + str(num3) + "}$$/수식$$ 의 약수) "
        #eq = eq + "($$수식$${" + str(exp3) + "}$$/수식$$ + 1) $$수식$$`=` {" + str(answ) + "}$$/수식$$"
        eq = eq+"$$수식$$("+str(exp3)+"+1) = "+str(answ)+"$$/수식$$"
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
    # print(eq)
    num=""
    if exp1!=1:
        num = "$$수식$${"+str(num1)+"} ^{"+str(exp1)+"} TIMES$$/수식$$"
    else:
        num = "$$수식$${" + str(num1) + "} TIMES$$/수식$$"
    if exp2!=1:
        num = num + "$$수식$${"+str(num2)+"} ^ {"+str(exp2)+"} TIMES$$/수식$$"
    else:
        num = num + "$$수식$${" + str(num2) + "} TIMES$$/수식$$"
    if exp3!=1:
        num = num + "$$수식$${"+str(num3)+"} ^{"+str(exp3)+"}$$/수식$$"
    else:
        num = num + "$$수식$${" + str(num3) + "}$$/수식$$"
    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, odd_prime=odd_prime, eq=eq)

    return stem, answer, comment

# 중1-1-1-47
def naturalnum111_Stem_036():
    stem = "자연수 $$수식$$A$$/수식$$를 소인수분해하면 $$수식$${eq}$$/수식$$이다. $$수식$$A$$/수식$$" \
           "의 약수의 개수가 $$수식$${prime_num}$$/수식$$일 때, $$수식$$A$$/수식$$의 값은? " \
           "(단, $$수식$$`a`,` b`$$/수식$$는 $$수식$$a `LEQ` b$$/수식$$인 자연수이다.)\n" \
          "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$$A$$/수식$$의 약수의 개수가 $$수식$${prime_num}$$/수식$$이므로\n" \
              "$$수식$${add_eq}$$/수식$$" \
              "$$수식$${add_eq2}$$/수식$$\n" \
              "$$수식$$a, b$$/수식$$는 자연수이고 $$수식$$a`LEQ` b$$/수식$$이므로\n" \
              "$$수식$${total_eq}$$/수식$$" \

    fac = [2, 3, 5, 7]

    num1 = fac[np.random.randint(0, 4)]
    exp1 = np.random.randint(1, 3)
    num2 = fac[np.random.randint(0, 4)]
    exp2 = np.random.randint(1, 3)
    num3 = fac[np.random.randint(0, 4)]
    exp3 = np.random.randint(1, 3)
    while num1 == num2 or num1 == num3 or num2 == num3:
        num2 = fac[np.random.randint(0, 4)]
        num3 = fac[np.random.randint(0, 4)]
    if exp2 > exp3:
        d = exp2
        exp2 = exp3
        exp3 = d
    answ = num1 ** exp1 * num2 ** exp2 * num3 ** exp3
    eq = ""
    if exp1!=1:
        eq = eq + "$$수식$${" + str(num1) + "} ^{" + str(exp1) + "} TIMES {" + str(num2) + "} ^{a} TIMES {" + str(num3) + "} ^{b}$$/수식$$"
    else:
        eq = eq + "$$수식$${" + str(num1) + "} TIMES {" + str(num2) + "} ^{a} TIMES {" + str(num3) + "} ^{b}$$/수식$$"

    prime_num = (exp1 + 1) * (exp2 + 1) * (exp3 + 1)

    add_eq = "($$수식$${" + str(
        exp1) + "}+ 1) `TIMES` (`a` +` 1`) TIMES (`b` +` 1`)`=` {" + str(
        prime_num) + "}$$/수식$$\n"
    add_eq2 = "$$수식$$(`a `+` 1`) TIMES (`b `+` 1`)`=` {" + str(
        round(prime_num / (exp1 + 1))) + "}$$/수식$$"

    total_eq = "$$수식$$`a` +` 1 `=` {" + str(exp2 + 1) + "}$$/수식$$ , $$수식$$ b `+` 1 `=` {" + str(
        exp3 + 1) + "}$$/수식$$\n$$수식$$a `=` {" + str(exp2) + "}$$/수식$$, $$수식$$b `=` {" + str(exp3) + "}$$/수식$$\n"
    total_eq = total_eq + "$$수식$$A = $$/수식$$" + factor_equation(answ)
    total_eq = total_eq + "$$수식$$`=` {" + str(answ) + "}$$/수식$$"

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

    stem = stem.format(eq=eq, prime_num=prime_num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(prime_num=prime_num, add_eq=add_eq, add_eq2=add_eq2, total_eq=total_eq)

    return stem, answer, comment




# 중1-1-1-48
def naturalnum111_Stem_037():
    stem = "자연수 $$수식$${eq}$$/수식$$   의 약수의 개수가 $$수식$${num}$$/수식$$일 때, 다음 " \
           "중  □ 안에 들어갈 수 없는 것은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${list}$$/수식$$\n" \
              "따라서 □안에 들어갈 수 없는 것은 {ans} 이다.\n" \

    fac = [2, 3, 5, 7, 11, 13]

    num1 = fac[np.random.randint(0, 6)]
    num2 = fac[np.random.randint(0, 6)]
    while num1 == num2:
        num2 = fac[np.random.randint(0, 6)]
    exp11 = np.random.randint(1, 3)
    num_one = []
    i = 2
    s = np.random.randint(1,4)
    n = num1**exp11*num2**s
    c = num1
    u = exp11
    total = (exp11+1)*(s+1)
    while ((num1**(exp11+1)*num2**(s))/(c**u))>1000:
        num1 = fac[np.random.randint(0, 6)]
        num2 = fac[np.random.randint(0, 6)]
        while num1 == num2:
            num2 = fac[np.random.randint(0, 6)]
        exp11 = np.random.randint(1, 3)
        i = 2
        s = np.random.randint(1, 4)
        n = num1 ** exp11 * num2 ** s
        c = num1
        u = exp11
        total = (exp11 + 1) * (s + 1)
    part1_ = ""
    if exp11 != 1:
        part1_ = part1_ + "$$수식$${" + str(num1) + "} ^{" + str(exp11) + "} TIMES$$/수식$$"
    else:
        part1_ = part1_ + "$$수식$${" + str(num1) + "} TIMES$$/수식$$"
    eq = part1_ + "$$수식$$□$$/수식$$"

    bb = []
    answ_list = []
    cc = []
    k123=[]
    o = np.random.randint(1, 4)
    k1=num1
    q = exp11
    # print(total)
    while len(k123) < 4:
        ep_temp = np.random.randint(0, 3)
        e = ep_temp
        exp11 = q
        p = exp11
        exp11 = exp11 + ep_temp
        ep_temp2 = int(total / exp11)
        while total % (exp11+1) != 0:
            exp11 =p
            ep_temp = np.random.randint(0, 3)
            exp11 = exp11 + ep_temp
        ep_temp2 = int(total/(exp11+1)) -1
        k2 = fac[np.random.randint(0, 6)]
        while k1 ==k2:
            k2 = fac[np.random.randint(0, 6)]
        x = int((k1 ** exp11*k2**ep_temp2)/c**u)
        if x not in k123:
            # print(x)
            k123.append(x)
            cc.append("{" + str(x) +"}")
            layout = part1_ + "$$수식$${" + str(x) +"}$$/수식$$"
            layout = layout + "$$수식$$`=`$$/수식$$ " + factor_equation(x*c**u)
            layout = layout + " 의 약수의 개수는\n($$수식$${" + str(exp11) + "} `+` 1`) TIMES$$/수식$$ ($$수식$${" + str(ep_temp2) + "}`+`1`) `=` {" + str((exp11 + 1) * (ep_temp2 + 1)) + "}$$/수식$$\n"
            bb.append(layout)

    answ = int((num1**(exp11+1)*num2**(s))/(c**u))
    answ_string = part1_ +"$$수식$$"+str(answ)+"$$/수식$$"
    if exp11!=0:
        answ_string = answ_string +"$$수식$$`=` {" + str(num1) + "} ^{" + str(exp11+1) + "} TIMES$$/수식$$"
    else:
        answ_string = answ_string + "$$수식$$`=` {" + str(num1) + "} TIMES$$/수식$$"
    if s!=1:
        answ_string = answ_string + "$$수식$${" + str(num2) + "} ^ {" + str(s) + "}$$/수식$$ 의 약수의 개수는\n($$수식$${" + str(exp11+1) + "}`+` 1`) TIMES$$/수식$$ ($$수식$${" + str(s) + "}   `+` 1`) ` = ` {" + str((exp11+2)*(s+1)) + "}$$/수식$$\n"
    else:
        answ_string = answ_string + "$$수식$${" + str(num2) + "}$$/수식$$ 의 약수의 개수는\n($$수식$${" + str(exp11+1) + "} `+` 1`) TIMES$$/수식$$ ($$수식$${" + str(s) + "}` +` 1`) ` = ` {" + str((exp11+2)*(s+1)) + "}$$/수식$$\n"
    bb.append(answ_string)

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
        liste = "① " + bb[4] + "② " + bb[0] + "③ " + bb[1] + "④ " + bb[2] + "⑤ " + bb[3]
    elif rande == 2:
        liste = "① " + bb[0] + "② " + bb[4] + "③ " + bb[1] + "④ " + bb[2] + "⑤ " + bb[3]
    elif rande == 3:
        liste = "① " + bb[0] + "② " + bb[1] + "③ " + bb[4] + "④ " + bb[2] + "⑤ " + bb[3]
    elif rande == 4:
        liste = "① " + bb[0] + "② " + bb[1] + "③ " + bb[2] + "④ " + bb[4] + "⑤ " + bb[3]
    else:
        liste = "① " + bb[0] + "② " + bb[1] + "③ " + bb[2] + "④ " + bb[3] + "⑤ " + bb[4]

    stem = stem.format(eq=eq , x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, num=total)
    answer = answer.format(ans=ans)
    comment = comment.format(list=liste, ans=ans)

    return stem, answer, comment



# 중1-1-1-49

def naturalnum111_Stem_038():
    stem = "$$수식$${num}$$/수식$$ 이하의 자연수 중 약수의 개수가 $$수식$${num1}$$/수식$$인 모든 수" \
           "의 곱을 $$수식$$a$$/수식$$라 할 때, $$수식$$a$$/수식$$의 소인수를 모두 구한 것은?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "약수의 개수가 $$수식$${num1}$$/수식$$인 자연수는 $$수식$$a ^m$$/수식$$ 또는 $$수식$$a ^m TIMES b ^n$$/수식$$\n" \
              "($$수식$$a`,` b`$$/수식$$는 서로 다른 소수, $$수식$$m`,` n`$$/수식$$은 자연수)" \
              "꼴이다.\n" \
              "(i) $$수식$$a ^m$$/수식$$꼴일 때,\n" \
              "$$수식$$m `+` 1` =` {num1}$$/수식$$에서 $$수식$$m `= `{ans11}$$/수식$$이므로 $$수식$${num}$$/수식$$ 이하의 자연수는\n" \
              "$$수식$${b} ^{ans11}$$/수식$$이다.\n" \
              "(ii) $$수식$$a ^m TIMES b ^n$$/수식$$꼴일 때,\n" \
              "$$수식$$(`m` +` 1`) `TIMES`  (`n `+ `1`) `= `{num1}$$/수식$$에서\n" \
              "$$수식$${list}$$/수식$$\n" \
              "따라서 $$수식$${num}$$/수식$$ 이하의 자연수는\n" \
              "$$수식$${long_list}$$/수식$$\n" \
              "(i), (ii)에서\n" \
              "{longer_list}\n" \
              "따라서 $$수식$$a$$/수식$$의 소인수는 {ans_list}이다.\n"
    
    fac = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    num = np.random.randint(20, 70)
    m = np.random.randint(1, 3)
    n = np.random.randint(1, 3)
    num1 = (m + 1) * (n + 1)
    ans11 = num1 - 1
    answ_list = []
    long_list = ""
    longer_list = ""
    list = ""
    temp6 =[]
    for i in range(0, ans11):
        temp6.append(i)
    if ans11!=1:
        longer_list = longer_list + "$$수식$${" + str(2) + "} ^{" + str(ans11) + "} TIMES$$/수식$$"
    else:
        longer_list = longer_list + "$$수식$${" + str(2) + "} TIMES$$/수식$$"
    list ="m = $$수식$${" + str(m) + "}$$/수식$$, n = $$수식$${" + str(n) + "}$$/수식$$ 또는 m =$$수식$${" + str(n) + "}$$/수식$$, n = $$수식$${" + str(m) + "}$$/수식$$"
    temp1 = []

    for i in range(1, num+1):
        r = factor_power(i)
        total_temp=1
        for x in r:
            total_temp = total_temp*(x+1)
        if total_temp==num1:
            temp1.append(i)
    while len(temp1)>5 or len(temp1)==0:
        fac = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        num = np.random.randint(20, 70)
        m = np.random.randint(1, 3)
        n = np.random.randint(1, 3)
        num1 = (m + 1) * (n + 1)
        ans11 = num1 - 1
        answ_list = []
        long_list = ""
        longer_list = ""
        list = ""
        temp6 = []
        for i in range(0, ans11):
            temp6.append(i)
        if ans11 != 1:
            longer_list = longer_list + "$$수식$${" + str(2) + "} ^{" + str(ans11) + "} TIMES$$/수식$$"
        else:
            longer_list = longer_list + "$$수식$${" + str(2) + "} TIMES$$/수식$$"
        list = "$$수식$$m `=` {" + str(m) + "}$$/수식$$, $$수식$$ n `=`{" + str(n) + "}$$/수식$$ 또는 $$수식$$m `=`{" + str(
            n) + "}$$/수식$$, $$수식$$n `= `{" + str(m) + "}$$/수식$$"
        temp1 = []

        for i in range(1, num + 1):
            r = factor_power(i)
            total_temp = 1
            for x in r:
                total_temp = total_temp * (x + 1)
            if total_temp == num1:
                temp1.append(i)
    if len(temp1) >0:
        for i in range(0, len(temp1)-1):
            long_list = long_list + factor_equation(temp1[i]) + "$$수식$$`,`$$/수식$$"
            longer_list = longer_list + "$$수식$$`(`$$/수식$$" + factor_equation(temp1[i]) +"$$수식$$`)`TIMES$$/수식$$"
        long_list = long_list + factor_equation(temp1[-1])
        longer_list = longer_list +  "$$수식$$`(`$$/수식$$" + factor_equation(temp1[-1]) + "$$수식$$`)`$$/수식$$"
    eeee =1
    if len(temp1)>0:
        for x in temp1:
            eeee = eeee*x
    longer_list = longer_list + "\n=" + factor_equation(eeee)
    facttors = factor_factors(eeee)
    ans_list = ""
    rr = []
    if len(facttors) >0:
        for i in range(0, len(facttors) - 1):
            ans_list = ans_list + "$$수식$${" + str(facttors[i]) + "}`,`$$/수식$$"
            rr.append(facttors[i])
        ans_list = ans_list + "$$수식$${" + str(facttors[-1]) + "}$$/수식$$"
        rr.append(facttors[-1])
    answ = ans_list
    bb = []

    y =[]
    numm =[]
    numm.append(rr)
    while len(bb)<4:
        dd = []
        for i in range(len(fac)- np.random.randint(0,7)):
            u = fac[np.random.randint(0,np.random.randint(1,8))]
            if u not in dd:
                dd.append(u)
        dd.sort()
        if dd not in numm:
            numm.append(dd)
            k=""
            for i in range(len(dd)-1):
                k = k + "$$수식$${" + str(dd[i]) + "}`,`$$/수식$$"
            k = k + "$$수식$${" + str(dd[-1]) + "}$$/수식$$"
            if dd not in y:
                bb.append(k)
                y.append(dd)

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

    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, num1=num1)
    answer = answer.format(ans=ans)
    comment = comment.format(b=2, num=num, num1=num1, long_list=long_list, longer_list=longer_list, list=list, ans_list=ans_list, ans11=ans11)

    return stem, answer, comment


# 중1-1-1-50
def naturalnum111_Stem_039():
    stem = "자연수 $$수식$$a$$/수식$$의 약수의 개수를 $$수식$$f(`a`)$$/수식$$라 할때, " \
           "$$수식$$f$$/수식$$($$수식$${num}$$/수식$$) $$수식$$TIMES f(x) `=` {num1}$$/수식$$" \
           "{temp} 만족시키는 자연수 $$수식$$x$$/수식$$의 값 중에서 가장 작은 " \
           "값은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$ 이므로\n" \
              "$$수식$$f$$/수식$$($$수식$${num}$$/수식$$) $$수식$$`=` {fac}$$/수식$$\n" \
              "$$수식$$f$$/수식$$($$수식$${num}$$/수식$$) $$수식$$TIMES f(x)`=` {num1}$$/수식$$ 에서\n" \
              "{eq1}\n" \
              "따라서 약수의 개수가  $$수식$${ans1}$$/수식$$인 $$수식$$x$$/수식$$ 값 중에서\n" \
              "가장 작은 자연수는 {answ1}이다.\n" \

    num = np.random.randint(30, 100)
    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = "$$수식$${" + str(num) + "} `=`$$/수식$$ " + factor_equation(num)

    eq=fact_
    num11=1
    for x in exp1:
        num11 = num11 * (1+x)

    op = [2,3,4,6]
    op1 = [2,4, 6,12, 8]
    h = np.random.randint(0, 4)
    num1 = num11 * op[h]
    fac=""
    if len(temp1) > 1:
        for i in range(len(temp1)-1):
            fac = fac + "$$수식$$`(`{" + str(exp1[i]) + "} + 1 `)` TIMES$$/수식$$ "
    fac= fac + "$$수식$$`(`{" + str(exp1[-1]) + "} + 1 `)`$$/수식$$ = $$수식$${" + str(num11) + "}$$/수식$$"

    eq1= "$$수식$${" + str(num11) + "} TIMES f(x)$$/수식$$,  $$수식$$f(x) `= `{" + str(op[h]) + "}$$/수식$$"

    answ = op[h]
    answ=1
    if h==0:
        answ1 = "$$수식$$2$$/수식$$"
    elif h==1:
        answ1 = "$$수식$$3$$/수식$$"
    elif h==2:
        answ1 = "$$수식$$2 `TIMES`  2 `=` 4$$/수식$$"
    elif h==3:
        answ1 = "$$수식$$2` TIMES` 3 `=` 6$$/수식$$"
    bb=[op1[h]]

    while len(bb) <4:
        q = np.random.randint(0, 4)
        if op1[q]!=op1[h] and op1[q] not in bb:
            bb.append(op1[q])
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

    temp = proc_jo(num1, 4)
    stem = stem.format(num=num, temp=temp, num1=num1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, num=num, fac=fac, num1=num1, eq1=eq1, ans1=op[h], answ1=answ1)

    return stem, answer, comment

# 중1-1-1-52
def naturalnum111_Stem_040():
    stem = "다음 중 두 수 $$수식$${num}$$/수식$$의 공약수가 " \
           "아닌 것은?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n$$/수식$$"
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${num}$$/수식$$의 최대공약수는$$수식$${num1}$$/수식$$\n" \
              "따라서 {ans} $$수식$${answ}$$/수식$${temp} $$수식$${num}$$/수식$$의 약수가 아니다.\n" \

    exp11 = np.random.randint(1, 5)
    exp12 = np.random.randint(1, 5)
    exp13 = np.random.randint(1, 5)

    exp21 = np.random.randint(1, 5)
    exp22 = np.random.randint(1, 5)
    exp23 = np.random.randint(1, 5)
    num11 = 2**exp11*3**exp12*5**exp13
    num22 = 2**exp21*3**exp22*5**exp23
    num = factor_equation(num11) + "$$수식$$`, ` $$/수식$$"
    num =  num + factor_equation(num22)
    dd=[]
    bb =[]
    while len(bb) < 4:
        bb1=""
        temp1 = np.random.randint(0, 4)
        temp2 = np.random.randint(0, 4)
        temp3 = np.random.randint(0, 4)
        while temp1 > min(exp11, exp21) or  temp2 > min(exp12, exp22) or temp3> min(exp13, exp23):
            temp1 = np.random.randint(0, 4)
            temp2 = np.random.randint(0, 4)
            temp3 = np.random.randint(0, 4)

        if (2**temp1*3**temp2*5**temp3)!=1 and [temp1,temp2,temp3] not in dd:
            dd.append([temp1,temp2,temp3])
            bb1 = factor_equation(2**temp1*3**temp2*5**temp3)
            bb.append(bb1)
    one = min(exp11, exp21)
    two =min(exp12, exp22)
    three = min(exp13, exp23)
    num1 = factor_equation(gcd(num11, num22))
    temp= ""
    t = np.random.randint(0, 4)
    if t==0:
        one = min(exp11, exp21)+2
        q= min(exp13, exp23)
        temp =proc_jo(min(exp13, exp23), -1)
    elif t==1:
        two = min(exp12, exp22)+2
        q= min(exp13, exp23)
        temp =proc_jo(min(exp13, exp23), -1)
    else:
        q = three = min(exp13, exp23)+2
        temp = proc_jo(min(exp13, exp23)+2, -1)

    if q==1:
        temp= proc_jo(5, -1)
    answ = factor_equation(2**one*3**two*5**three)
    bb.append(answ)

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

    stem = stem.format(num=num, temp=temp, num1=num1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, num1=num1, ans=ans, answ=answ, temp=temp)

    return stem, answer, comment


# 중1-1-1-53
def naturalnum111_Stem_041():
    def gcd(x,y):
        while y:
            x,y=x,y%x
        
        return x

    stem = "다음 중 두 수가 두 수가 서로소인 것은?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "두 수의 최대공약수는\n" \
              "{list}\n" \
              "따라서 주어진 두 수가 서로소인 것은 {ans} 이다."

    op=x1=x2=x3=x4=x5=ans=list=""
    choice = 0
    fac = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    num1 = np.random.randint(1, 100)
    num2 = np.random.randint(1, 100)
    for x in fac:
        while num1 == num2 or (num1 % x == 0 and num2 % x == 0):
            num1 = np.random.randint(2, 100)
            num2 = np.random.randint(2, 100)
    div = []
    bb = []
    while len(bb) < 4:
        for x in fac:
            num3 = np.random.randint(2, 100)
            num4 = np.random.randint(2, 100)
            while num3 == num4:
                num3 = np.random.randint(2, 100)
            if num3 % x == 0 and num4 % x == 0 and (num3!=num1 or num3!=num2):
           
                bb.append([num3, num4])
                an = 0
                for i in range(2, min(num3, num4) + 1):
                    if num3 % i == 0 and num4 % i == 0:
                        an = i
                div.append(an)
                
    
    answ = "$$수식$${" + str(num1) + "}$$/수식$$ , $$수식$${" + str(num2) + "}$$/수식$$"
    rande = np.random.randint(1, 4)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = "$$수식$${" + str(bb[0][0]) + "}$$/수식$$,   $$수식$${" + str(bb[0][1]) + "}$$/수식$$"
        x3 = "$$수식$${" + str(bb[1][0]) + "}$$/수식$$,   $$수식$${" + str(bb[1][1]) + "}$$/수식$$"
        x4 = "$$수식$${" + str(bb[2][0]) + "}$$/수식$$,   $$수식$${" + str(bb[2][1]) + "}$$/수식$$"
        x5 = "$$수식$${" + str(bb[3][0]) + "}$$/수식$$,   $$수식$${" + str(bb[3][1]) + "}$$/수식$$"
        list = "① $$수식$$1$$/수식$$\n② $$수식$$" + str(div[0]) + "$$/수식$$\n③ $$수식$$" + str(div[1]) + "$$/수식$$\n④ $$수식$$" + str(div[2]) + "$$/수식$$\n⑤ $$수식$$" + str(div[3]) + "$$/수식$$     "

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = "$$수식$${" + str(bb[0][0]) + "}$$/수식$$,   $$수식$${" + str(bb[0][1]) + "}$$/수식$$"
        x3 = "$$수식$${" + str(bb[1][0]) + "}$$/수식$$,   $$수식$${" + str(bb[1][1]) + "}$$/수식$$"
        x4 = "$$수식$${" + str(bb[2][0]) + "}$$/수식$$,   $$수식$${" + str(bb[2][1]) + "}$$/수식$$"
        x5 = "$$수식$${" + str(bb[3][0]) + "}$$/수식$$,   $$수식$${" + str(bb[3][1]) + "}$$/수식$$"
        list = "① $$수식$$" + str(div[0]) + "$$/수식$$\n② $$수식$$1$$/수식$$\n③ $$수식$$" + str(div[1]) + "$$/수식$$\n④ $$수식$$" + str(div[2]) + "$$/수식$$\n⑤ $$수식$$" + str(div[3]) + "$$/수식$$      "
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = "$$수식$${" + str(bb[0][0]) + "}$$/수식$$,   $$수식$${" + str(bb[0][1]) + "}$$/수식$$"
        x2 = "$$수식$${" + str(bb[1][0]) + "}$$/수식$$,   $$수식$${" + str(bb[1][1]) + "}$$/수식$$"
        x4 = "$$수식$${" + str(bb[2][0]) + "}$$/수식$$,   $$수식$${" + str(bb[2][1]) + "}$$/수식$$"
        x5 = "$$수식$${" + str(bb[3][0]) + "}$$/수식$$,   $$수식$${" + str(bb[3][1]) + "}$$/수식$$"
        list = "① $$수식$$" + str(div[0]) + "$$/수식$$\n② $$수식$$" + str(div[1]) + "$$/수식$$\n③ $$수식$$1$$/수식$$\n④ $$수식$$" + str(div[2]) + "$$/수식$$\n⑤ $$수식$$" + str(div[3]) + " $$/수식$$     "



    stem = stem.format(op=op, num1=num1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=list, ans=ans)

    return stem, answer, comment


# 중1-1-1-54
def naturalnum111_Stem_042():
    stem = "두 자연수 $$수식$$A`,` B$$/수식$$의 최대공약수가 $$수식$${num}$$/수식$$일 때, 이 두 " \
           "수 $$수식$$A`,` B$$/수식$$의 공약수의 개수는?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$$A$$/수식$$와 $$수식$$B$$/수식$$의 공약수의 개수는 두 수의 최대공약수인\n" \
              "$$수식$${num}$$/수식$$의 약수의 개수와 같다.\n" \
              "이 때 $$수식$${eq}$$/수식$$ 이므로 구하는 공약수의 개수는\n" \
              "$$수식$${eq2}$$/수식$$\n"

    num = np.random.randint(1, 100)
    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = "$$수식$${" + str(num) + "} `=`$$/수식$$" + factor_equation(num)

    eq = fact_
    answ = 1
    for x in exp1:
        answ = answ * (1 + x)
    eq2 = ""
    if len(exp1)>0:
        for i in range(len(exp1) - 1):
            eq2 = eq2 + "($$수식$${" + str(exp1[i]) + "} `+` 1) TIMES$$/수식$$"
        eq2 = eq2 + "($$수식$${" + str(exp1[-1]) + "} `+` 1) `=` {" + str(answ) + "}$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k>=2:
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

    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, eq=eq, eq2=eq2)

    return stem, answer, comment


#중1-1-1-55
def naturalnum111_Stem_043():
    stem = "세 수 $$수식$${num}$$/수식$$의 공약수의 개수는?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "

    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${list}$$/수식$$ 이므로\n" \
              "세 수 $$수식$${num}$$/수식$$   의 최대공약수는 $$수식$${eq}$$/수식$$이다.\n" \
              "따라서 공약수의 개수는 $$수식$${eq2}$$/수식$$\n" \

    fac = [2, 3, 5]
    num11 = fac[np.random.randint(0, 3)]
    exp11 = np.random.randint(1, 4)
    num12 = fac[np.random.randint(0, 3)]
    exp12 = np.random.randint(1, 4)
    while num11 == num12:
        num12 =fac[np.random.randint(0, 3)]
    if num11 < num12:
        b = num12
        num12 = num11
        num11 =b
    num1 = num11**exp11 *num12**exp12

    num21 = 2
    exp21 = np.random.randint(1, 4)
    num22 = 3
    exp22 = np.random.randint(1, 4)
    num23 = 5
    exp23 = np.random.randint(1, 4)
    num2 = num21 ** exp21 * num22 ** exp22*num23**exp23

    num31 = fac[np.random.randint(0, 3)]
    exp31 = np.random.randint(1, 4)
    num32 = fac[np.random.randint(0, 3)]
    exp32 = np.random.randint(1, 4)
    while num31==num32:
        num32 = fac[np.random.randint(0, 3)]
    if num31 < num32:
        b = num32
        num32 = num31
        num31 = b
    num3 = num31 ** exp31 * num32 ** exp32

    num = "$$수식$${"+str(num1)+"}`,  {"+str(num2)+"}`,  {"+str(num3)+"}$$/수식$$"
    nume =[num1, num2, num3]
    fact_=""
    for p in range(0,2):
        fact_ = fact_ + "$$수식$${" + str(nume[p]) + "} `=`$$/수식$$"
        num_one = []
        i = 2
        n = nume[p]
        while n > 1:
            if n % i == 0:
                num_one.append(i)
                n = n / i
                i = i - 1
            i += 1
        num_one.sort()
        temp1 = []
        exp1 = []
        num_one.sort()
        for x in num_one:
            if x not in temp1:
                temp1.append(x)
        for x in temp1:
            i = 0
            for y in num_one:
                if x == y:
                    i += 1
            exp1.append(i)
        if len(nume) > 0:
            fact_ = fact_ + factor_equation(nume[p]) + "$$수식$$`, `$$/수식$$ "

    list = fact_ + "$$수식$${" + str(nume[-1]) + "} `=`$$/수식$$" + factor_equation(num31**exp31*num32**exp32)

    exp =[]
    comoon=[]
    if num11 == num21 == num31:
        exp.append(min(exp11, exp21, exp31))
        comoon.append(num11)
    if num11 == num22 == num31:
        exp.append(min(exp11, exp22, exp31))
        comoon.append(num11)
    if num11 == num22 == num32:
        exp.append(min(exp11, exp22, exp32))
        comoon.append(num11)
    if num11 == num21 == num32:
        exp.append(min(exp11, exp21, exp32))
        comoon.append(num11)
    if num12 == num21 == num31:
        exp.append(min(exp12, exp21, exp31))
        comoon.append(num21)
    if num12 == num22 == num31:
        exp.append(min(exp12, exp22, exp31))
        comoon.append(num21)
    if num12 == num22 == num32:
        exp.append(min(exp12, exp22, exp32))
        comoon.append(num21)
    if num12 == num21 == num32:
        exp.append(min(exp12, exp21, exp32))
        comoon.append(num21)
    if num11 == num23 == num31:
        exp.append(min(exp11, exp23, exp31))
        comoon.append(num11)
    if num11 == num22 == num31:
        exp.append(min(exp11, exp23, exp32))
        comoon.append(num11)
    if num11 == num22 == num32:
        exp.append(min(exp12, exp23, exp32))
        comoon.append(num11)
    if num11 == num21 == num32:
        exp.append(min(exp12, exp23, exp31))
        comoon.append(num11)



    answ = 1
    for x in exp:
        answ = answ * (1 + x)
    eq2 = ""
    eq=""
    if len(exp)>1:
        for i in range(len(exp) - 1):
            if exp[i]!=1:
                eq = eq + "$$수식$${" + str(comoon[i]) + "} ^{" + str(exp[i]) + "} TIMES$$/수식$$"
            else:
                eq = eq + "$$수식$${" + str(comoon[i]) + "} TIMES$$/수식$$"
            eq2 = eq2 + "($$수식$${" + str(exp[i]) + "}` +` 1) TIMES$$/수식$$"
        eq2 = eq2 + "($$수식$${" + str(exp[-1]) + "}`+` 1) `=` {" + str(answ) + "}$$/수식$$"
        if exp[-1]!=1:
            eq = eq + "$$수식$${" + str(comoon[-1]) + "} ^{" + str(exp[-1]) + "}$$/수식$$"
        else:
            eq = eq + "$$수식$${" + str(comoon[-1]) + "}$$/수식$$"
    elif len(exp)==1:
        eq2 = eq2 + "($$수식$${" + str(exp[-1]) + "} `+` 1) `=` {" + str(answ) + "}$$/수식$$"
        if exp[-1]!=1:
            eq = eq + "$$수식$${" + str(comoon[-1]) + "} ^{" + str(exp[-1]) + "}$$/수식$$"
        else:
            eq = eq + "$$수식$${" + str(comoon[-1]) + "}$$/수식$$"
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

    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, list=list, eq=eq, eq2=eq2)

    return stem, answer, comment


# 중1-1-1-56
def naturalnum111_Stem_044():
    stem = "세 수 $$수식$${num}$$/수식$$ 의 최대공약수는?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n$$/수식$$"
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "세수 $$수식$${num}$$/수식$$ 의 최대공약수는\n" \
              "$$수식$${answ}$$/수식$$ 이다." \

    num=""
    fac = [2, 3, 5]
    num11 = fac[np.random.randint(0, 3)]
    exp11 = np.random.randint(1, 4)
    num12 = fac[np.random.randint(0, 3)]
    exp12 = np.random.randint(1, 4)
    while num11 == num12:
        num12 = fac[np.random.randint(0, 3)]
    if num11 < num12:
        b = num12
        num12 = num11
        num11 = b

    num1 = num11 ** exp11 * num12 ** exp12
    num = num + factor_equation(num1) + "$$수식$$` , `$$/수식$$"

    num21 = 2
    exp21 = np.random.randint(1, 4)
    num22 = 3
    exp22 = np.random.randint(1, 4)
    num23 = 5
    exp23 = np.random.randint(1, 4)
    num2 = num21 ** exp21 * num22 ** exp22 * num23 ** exp23

    num = num + factor_equation(num2) + "$$수식$$` , `$$/수식$$"

    num31 = fac[np.random.randint(0, 3)]
    exp31 = np.random.randint(1, 4)
    num32 = fac[np.random.randint(0, 3)]
    exp32 = np.random.randint(1, 4)
    while num31 == num32:
        num32 = fac[np.random.randint(0, 3)]
    if num31 < num32:
        b = num32
        num32 = num31
        num31 = b
    num3 = num31 ** exp31 * num32 ** exp32

    num = num + factor_equation(num3)

    exp = factor_power(gcd(gcd(num1, num2), num3))
    comoon = factor_factors(gcd(gcd(num1, num2), num3))

    answ = 1
    for x in exp:
        answ = answ * (1 + x)
    eq2 = ""
    eq = ""
    if len(exp) > 1:
        for i in range(len(exp) - 1):
            if exp[i]!=1:
                eq = eq + "$$수식$${" + str(comoon[i]) + "} ^{" + str(exp[i]) + "} TIMES$$/수식$$"
            else:
                eq = eq + "$$수식$${" + str(comoon[i]) + "} TIMES$$/수식$$"
            eq2 = eq2 + "($$수식$${" + str(exp[i]) + "}$$/수식$$ + 1) $$수식$$TIMES$$/수식$$"
        eq2 = eq2 + "($$수식$${" + str(exp[-1]) + "}$$/수식$$ + 1) $$수식$$`=` {" + str(answ) + "}$$/수식$$"
        if exp[-1]!=1:
            eq = eq + "$$수식$${" + str(comoon[-1]) + "} ^{" + str(exp[-1]) + "}$$/수식$$"
        else:
            eq = eq + "$$수식$${" + str(comoon[-1]) + "}$$/수식$$"
    elif len(exp) == 1:
        eq2 = eq2 + "($$수식$${" + str(exp[-1]) + "}$$/수식$$ + 1) $$수식$$`=` {" + str(answ) + "}$$/수식$$"
        if exp[-1]!=1:
            eq = eq + "$$수식$${" + str(comoon[-1]) + "} ^{" + str(exp[-1]) + "}$$/수식$$"
        else:
            eq = eq + "$$수식$${" + str(comoon[-1]) + "}$$/수식$$"
    answ = factor_equation(gcd(gcd(num1, num2), num3))
    bb = []
    if len(exp) == 1:
        for i in range(1, 6):
            bb.append("$$수식$${" + str(comoon[0]) + "} ^{" + str(exp[0] + i+1) + "}$$/수식$$")
    elif len(exp) > 1:
        bb.append("$$수식$${" + str(comoon[0]) + "} ^{" + str(exp[0] + 2) + "} TIMES {" + str(comoon[1]) + "} ^{" + str(exp[1] + 2) + "}$$/수식$$")
        bb.append("$$수식$${" + str(comoon[0]) + "} ^{" + str(exp[0] + 3) + "}$$/수식$$")
        bb.append("$$수식$${" + str(comoon[1]) + "} ^{" + str(exp[1] + 2) + "}$$/수식$$")
        bb.append("$$수식$${" + str(comoon[0]) + "} ^{" + str(exp[0] + 4) + "} TIMES {" + str(
            comoon[1]) + "} ^{" + str(exp[1]+1) + "}$$/수식$$")
    else:
        bb.append("$$수식$${" + str(num11) + "} ^{" + str(2) + "}$$/수식$$")
        bb.append("$$수식$${" + str(num21) + "} ^{" + str(3) + "}$$/수식$$")
        bb.append("$$수식$${" + str(num12) + "} ^{" + str(5) + "}$$/수식$$")
        bb.append("$$수식$${" + str(num31) + "} ^{" + str(4) + "}$$/수식$$")

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

    stem = stem.format(num=num, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, answ=answ)

    return stem, answer, comment



# 중1-1-1-57
def naturalnum111_Stem_045():
    stem = "다음중 두 수가 서로소가 아닌 것은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${list}$$/수식$$" \
              "\n따라서 서로소가 아닌 두 수는 {ans}이다." \


    fac = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    ans1 = np.random.randint(5, 50)
    ans2 = np.random.randint(5, 50)
    while ans1 == ans2:
        ans2 = np.random.randint(5, 50)
    dd = []
    div = 0
    bre =0
    while bre==0:
        for x in fac:
            if ans1 % x == 0 and ans2 % x == 0:
                bre+=1
                for i in range(2, min(ans1, ans2) + 1):
                    if ans1 % i == 0 and ans2 % i == 0:
                        div = i
            else:
                ans1 = np.random.randint(5, 50)
                ans2 = np.random.randint(5, 50)
    if ans2 > ans1:
        b = ans2
        ans2 = ans1
        ans1 = b
    div = gcd(ans1, ans2)
    while div==1:
        ans1 = np.random.randint(5, 50)
        ans2 = np.random.randint(5, 50)
        while ans1 == ans2:
            ans2 = np.random.randint(5, 50)
        dd = []
        div = 0
        bre = 0
        while bre == 0:
            for x in fac:
                if ans1 % x == 0 and ans2 % x == 0:
                    bre += 1
                    for i in range(2, min(ans1, ans2) + 1):
                        if ans1 % i == 0 and ans2 % i == 0:
                            div = i
                else:
                    ans1 = np.random.randint(5, 50)
                    ans2 = np.random.randint(5, 50)
        if ans2 > ans1:
            b = ans2
            ans2 = ans1
            ans1 = b
        div = gcd(ans1, ans2)
    answ_str = "$$수식$$ {" + str(ans1) + "}$$/수식$$" + proc_jo(ans1, 2) + "$$수식$$` `{" + str(ans2) + "}$$/수식$$ 의 최대공약수는 $$수식$${"+ str(div) + "}$$/수식$$ 이다."
    answ = "$$수식$${" + str(ans1) + "}  ,  {"+ str(ans2) +"}$$/수식$$ "
    while len(dd) < 4:
        count = 0
        num1 = np.random.randint(5, 50)
        num2 = np.random.randint(5, 50)
        while num1 == num2:
            num1 = np.random.randint(5, 50)
        for x in fac:
            if num1 % x == 0 and num2 % x == 0:
                count += 1
        if count == 0:
            dd.append([num1, num2])
    cc = []
    bb = []

    for x in dd:
        cc.append("$$수식$${" + str(x[0]) +"}  ,  {" + str(x[1])+"}$$/수식$$")
        bb.append("$$수식$${" + str(x[0]) +"}$$/수식$$" + proc_jo(x[0], 2) + "$$수식$$` ` {" + str(x[1])+"}  $$/수식$$의 최대공약수는 $$수식$$1$$/수식$$이다. ")
    bb.append(answ_str)
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
        liste = "① " + bb[4] + "\n② " + bb[0] + "\n③ " + bb[1] + "\n④ " + bb[2] + "\n⑤ " + bb[3]
    elif rande == 2:
        liste = "① " + bb[0] + "\n② " + bb[4] + "\n③ " + bb[1] + "\n④ " + bb[2] + "\n⑤ " + bb[3]
    elif rande == 3:
        liste = "① " + bb[0] + "\n② " + bb[1] + "\n③ " + bb[4] + "\n④ " + bb[2] + "\n⑤ " + bb[3]
    elif rande == 4:
        liste = "① " + bb[0] + "\n② " + bb[1] + "\n③ " + bb[2] + "\n④ " + bb[4] + "\n⑤ " + bb[3]
    else:
        liste = "① " + bb[0] + "\n② " + bb[1] + "\n③ " + bb[2] + "\n④ " + bb[3] + "\n⑤ " + bb[4]

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=liste, ans=ans)

    return stem, answer, comment






# 중1-1-1-58
#수와 연사 21?
def naturalnum111_Stem_046():
    stem = "다음 중 자연수에 대한 설명으로 옳지 않은것은?\n" \
           "① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "{ans} $$수식$$3,``9$$/수식$$는 서로 다른 홀수이지만\n최대공약수가 $$수식$$3$$/수식$$" \
              "이므로 서로소가 아니다.\n" \

    cc = []
    cc.append("가장 작은 소수는 $$수식$$2$$/수식$$이다.")
    cc.append("서로 다른 두 소수는 서로소이다.")
    cc.append("서로 다른 두 짝수는 서로소가 아니다.")
    cc.append("최대공약수가 $$수식$$1$$/수식$$인 두 자연수는 서로소이다.")
    answ = "서로 다른 두 홀수는 서로소이다."
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

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(ans=ans)

    return stem, answer, comment


# 중1-1-1-59
def naturalnum111_Stem_047():
    stem = "$$수식$${low}$$/수식$$ 이상 $$수식$${high}$$/수식$$ 이하의 자연수 중에서 $$수식$${num}$$/수식$${temp1} 서로소인 " \
           "수의 개수는?\n" \
         "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${low}$$/수식$$ 이상 $$수식$${high}$$/수식$$ 이하의 자연수 중에서 $$수식$${eq}$$/수식$${temp2} 서로소인 수는\n" \
              "{fac} 수이므로\n" \
              "$$수식$${list}$$/수식$$의 $$수식$${anse}$$/수식$$개이다.\n" \


    low = np.random.randint(5, 30)
    high = np.random.randint(low + 10, 50)
    num = np.random.randint(10, 30)
    lis = []
    fac1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    for i in range(low + 1, high):
        count = 0
        for x in fac1:
            if i % x == 0 and num % x == 0:
                count += 1
        if count == 0:
            lis.append(i)
    anse = len(lis)
    answ = anse
    list = ""
    if len(lis) > 0:
        for i in range(0, len(lis) - 1):
            list = list + "$$수식$${" + str(lis[i]) + "}$$/수식$$,"
        list = list + "$$수식$${" + str(lis[-1]) + "}$$/수식$$"
    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = factor_equation(num)
    eq = fact_
    fac = ""
    if len(exp1) > 0:
        for i in range(0, len(exp1) - 1):
            fac = fac + "$$수식$${" + str(temp1[i]) + "}$$/수식$$의 배수가 아니고 "
        fac = fac + "$$수식$${" + str(temp1[-1]) + "}$$/수식$$의 배수가 아닌"

    temp1 = proc_jo(num, 2)
    temp2 = proc_jo(temp1[-1], 2)
    bb = []
    bb.clear()
    k=0
    while len(bb) < 4:
        k = fac1[np.random.randint(0, 7)]
        if k not in bb and k != anse:
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

    stem = stem.format(high=high, low=low, num=num, temp1=temp1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=list, high=high, low=low, temp2=temp2, eq=eq, fac=fac, anse=answ)

    return stem, answer, comment




# 중1-1-1-60
def naturalnum111_Stem_048():
    stem = "$$수식$${num1}$$/수식$$ {temp}  자연수 $$수식$$a$$/수식$$의 공약수가 $$수식$${num2}$$/수식$$의 약수와 같을 때, " \
           "다음 중 $$수식$$a$$/수식$$의 값이 될 수 없는 것은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):{ans}"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$ {temp10} $$수식$$a$$/수식$$의 최대공약수가 $$수식$${num2}$$/수식$$이어야 한다.\n" \
              "$$수식$${list}$$/수식$$ "  \


    temp10=""
    fac = [2, 3, 5, 7, 11]
    num21 = fac[np.random.randint(0,3)]
    num22 = fac[np.random.randint(0,3)]
    while num21 == num22:
        num22 = fac[np.random.randint(0, 4)]
    exp21 = np.random.randint(1,4)
    exp22 = np.random.randint(1,4)
    num2 = num21**exp21 * num22 ** exp22
    while num2 > 40:
        num21 = fac[np.random.randint(0, 3)]
        num22 = fac[np.random.randint(0, 3)]
        while num21 == num22:
            num22 = fac[np.random.randint(0, 4)]
        exp21 = np.random.randint(1, 4)
        exp22 = np.random.randint(1, 4)
        num2 = num21 ** exp21 * num22 ** exp22
    num2_stri = factor_equation(num2)
    right_ones = []
    bb=[]
    fact_=""
    while len(right_ones) <5:
        k = fac[np.random.randint(0,5)]
        if k*num2 not in right_ones:
            right_ones.append(k*num2)
    num1 = right_ones[4]*3
    right_ones.remove(right_ones[4])
    temp = proc_jo(num1,2)
    cc = right_ones
    for x in right_ones:
        fact_ = ""
        num_one = []
        i = 2
        n = x
        while n > 1:
            if n % i == 0:
                num_one.append(i)
                n = n / i
                i = i - 1
            i += 1
        num_one.sort()
        temp1 = []
        exp1 = []
        num_one.sort()
        for y in num_one:
            if y not in temp1:
                temp1.append(y)
        for z in temp1:
            i = 0
            for y in num_one:
                if z == y:
                    i += 1
            exp1.append(i)
        fact_ = fact_ + "$$수식$${" + str(x) + "}`=`" + factor_equation(x)+"$$/수식$$"
        fact_  = fact_ + " 이므로 $$수식$${" + str(num1) + "}$$/수식$$ " + temp +" $$수식$$a$$/수식$$의 최대공약수는$$수식$$ " + num2_stri + "`=` {"+str(num2)+"}$$/수식$$"
        bb.append(fact_)
    answ = num21**exp21 * num22 ** (exp22) * 3
    if num21 ==3:
        exp21 = exp21+1
    elif num22 ==3:
        exp22 = exp21 + 1
    num_one = []
    i = 2
    n = answ
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    num2_stri1 = factor_equation(num21**exp21*num22*exp22)
    if num21 !=3 and num22!=3:
        num2_stri1 = factor_equation(num21**exp21*num22*exp22) + "$$수식$$TIMES 3$$/수식$$  "
    fact_ = "$$수식$${" + str(answ) + "}`=`$$/수식$$"
    if len(temp1) > 0:
        for i in range(len(temp1) - 1):
            if exp1[i]!=1:
                fact_ = fact_ + "$$수식$${" + str(temp1[i]) + "} ^{" + str(exp1[i]) + "} TIMES$$/수식$$"
            else:
                fact_ = fact_ + "$$수식$${" + str(temp1[i]) + "} TIMES$$/수식$$"
        if exp1[-1]!=1:
            fact_ = fact_ + "$$수식$${" + str(temp1[-1]) + "} ^{" + str(exp1[-1]) + "}$$/수식$$이므로 $$수식$${" + str(num1) + "}$$/수식$$ " + temp + " $$수식$$a$$/수식$$의 최대공약수는 " + num2_stri1 + "$$수식$$`=` {" + str(answ) + "}$$/수식$$"
        else:
            fact_ = fact_ + "$$수식$${" + str(temp1[-1]) + "}$$/수식$$이므로 $$수식$${" + str(num1) + "}$$/수식$$ " + temp + " $$수식$$a$$/수식$$ 의 최대공약수는 " + num2_stri1 + "$$수식$$`=` {" + str(answ) + "}$$/수식$$"
    bb.append(fact_)

    num_one = []
    i = 2
    n = num1
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = "$$수식$${" + str(num1) + "} `=`$$/수식$$" + factor_equation(num1)
    if len(temp1) > 0:
        temp10 = proc_jo(exp1[-1], 2)
    eq = fact_

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

    if rande == 1:
        liste = "①  " + bb[4] + "\n②  " + bb[0] + "\n③  " + bb[1] + "\n④  " + bb[2] + "\n⑤  " + bb[3]
    elif rande == 2:
        liste = "①  " + bb[0] + "\n②  " + bb[4] + "\n③  " + bb[1] + "\n④  " + bb[2] + "\n⑤  " + bb[3]
    elif rande == 3:
        liste = "①  " + bb[0] + "\n②  " + bb[1] + "\n③  " + bb[4] + "\n④  " + bb[2] + "\n⑤  " + bb[3]
    elif rande == 4:
        liste = "①  " + bb[0] + "\n②  " + bb[1] + "\n③  " + bb[2] + "\n④  " + bb[4] + "\n⑤  " + bb[3]
    else:
        liste = "①  " + bb[0] + "\n②  " + bb[1] + "\n③  " + bb[2] + "\n④  " + bb[3] + "\n⑤  " + bb[4]

    stem = stem.format(temp=temp,  num1=num1, num2=num2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp10=temp10, num2=num2, list=liste, eq=eq)

    return stem, answer, comment


# 중1-1-1-61
def naturalnum111_Stem_049():
    stem = "다음 조건을 모두 만족시키는 자연수 중에서 가장 작은 수를 구하시오.\n" \
           "$$표$$(가) 약수가 $$수식$$1$$/수식$$과 자기 자신뿐이다.\n" \
           "(나) $$수식$${low}$$/수식$$보다 큰 수이다.\n" \
           "(다) $$수식$${num}$$/수식$${jo} 서로소이다.$$/표$$"
    answer = "(답):\n$$수식$${ans}$$/수식$$"
    comment = "(해설)\n" \
              "구하는 수를 $$수식$$x$$/수식$$라 하면 조건 (가), (나)에서 $$수식$$x$$/수식$$는\n" \
              "$$수식$${low}$$/수식$$보다 큰 소수이므로\n" \
              "$$수식$$x `=`$$/수식$${list}\n" \
              "조건 (다)에서 $$수식$${eq}$$/수식$$이므로 {small_eq}\n" \
              "따라서 구하는 수는 $$수식$${ans}$$/수식$$이다." \

    low = np.random.randint(1, 30)
    num = np.random.randint(10, 70)
    fac = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    list=""
    liste=[]
    for x in fac:
        if x > low:
            liste.append(x)
    liste.sort()
    for i in range(2):
        list = list + "$$수식$${" + str(liste[i]) + "}$$/수식$$ , "
    list = list + "$$수식$${" + str(liste[2]) + "} CDOTS$$/수식$$"

    num_one = []
    i = 2
    n = num
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = "$$수식$${" + str(num) + "} `=`$$/수식$$" + factor_equation(num)
    eq = fact_
    q = 0
    small_eq="$$수식$$x ≠$$/수식$$"
    for x in temp1:
        for y in liste:
            if x == y:
                liste.remove(x)
                small_eq = small_eq + "$$수식$${" + str(x) + "}$$/수식$$ ,  "
                q+=1
    if q==0:
        small_eq = ""
    ans = liste[0]
    num = str(num)
    
    jo = proc_jo(num,2)

    stem = stem.format(low=low, num=num, jo=jo)
    answer = answer.format(ans=ans)
    comment = comment.format(low=low, list=list, small_eq=small_eq, eq=eq, ans=ans)

    return stem, answer, comment



# 중1-1-1-62
def naturalnum111_Stem_050():
    stem = "$$수식$${low}$$/수식$${temp} $$수식$${high}$$/수식$$의 공약수 중 어떤 자연수의 제곱이 되는 모든 수의 합은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$의 최대공약수는 $$수식$${ans1}$$/수식$$ 이다.\n" \
              "즉, $$수식$${low}$$/수식$${temp} $$수식$${high}$$/수식$$의 공약수는 $$수식$${ans1}$$/수식$$의 약수이므로\n" \
              "$$수식$${low}$$/수식$${temp} $$수식$${high}$$/수식$$의 공약수 중 어떤 자연수의 제곱이되는 수는 $$수식$$1$$/수식$$\n" \
              "{list}" \
              "따라서 구하는 합은 " \
              "$$수식$${list2}$$/수식$$\n" \

    low = np.random.randint(10, 400)
    high = np.random.randint(low+10, 600)
    temp = proc_jo(low, 2)

    num_one = []
    i = 2
    n = low
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = "$$수식$${" + str(low) + "}`=`$$/수식$$" + factor_equation(low)  + ", "

    eq= fact_

    num_one = []
    i = 2
    n = high
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp2 = []
    exp2 = []
    num_one.sort()
    for x in num_one:
        if x not in temp2:
            temp2.append(x)
    for x in temp2:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp2.append(i)
    fact_ = "$$수식$${" + str(high) + "} `=`$$/수식$$" +  factor_equation(high)

    eq = eq + fact_

    factors_list =[]
    exp_factors =[]
    for i in range (0, len(temp1)):
        for j in range(0, len(temp2)):
            if temp1[i]==temp2[j] and temp1[i] not in factors_list:
                factors_list.append(temp1[i])
                exp_factors.append(min(exp1[i],exp2[j]))
    ans1=""
    if len(factors_list) > 0:
        for i in range(len(factors_list) - 1):
            if exp_factors[i]!=1:
                ans1 = ans1 + "$$수식$${" + str(factors_list[i]) + "} ^{" + str(exp_factors[i]) + "} TIMES$$/수식$$"
            else:
                ans1 = ans1 + "$$수식$${" + str(factors_list[i]) + "} TIMES$$/수식$$"
        if exp_factors[-1]!=1:
            ans1 = ans1 + "$$수식$${" + str(factors_list[-1]) + "} ^{" + str(exp_factors[-1]) + "}$$/수식$$"
        else:
            ans1 = ans1 + "$$수식$${" + str(factors_list[-1]) + "}$$/수식$$"
    if len(factors_list)== 0:
        ans1 = "1"
    highest_factor = 1
    fac_num_list =[]
    for i in range(0, len(factors_list)):
        highest_factor = highest_factor * (factors_list[i]**exp_factors[i])
    for i in range(2, highest_factor+1):
        if i % math.sqrt(i) ==0:
            fac_num_list.append(i)
    fact_ = ""
    for x in fac_num_list:
        num_one = []
        i = 2
        n = x
        while n > 1:
            if n % i == 0:
                num_one.append(i)
                n = n / i
                i = i - 1
            i += 1
        num_one.sort()
        temp1 = []
        exp1 = []
        num_one.sort()
        for t in num_one:
            if t not in temp1:
                temp1.append(t)
        for k in temp1:
            i = 0
            for y in num_one:
                if k == y:
                    i += 1
            exp1.append(i)
        fact_ = fact_ + " ," + factor_equation(x) + "= " + str(x)
    list = fact_
    answ =1
    list2="1"
    for x in fac_num_list:
        answ = answ +x
    if len(fac_num_list) > 0:
        for i in range(len(fac_num_list)-1):
            list2 = list2 + " + " + str(fac_num_list[i])
        list2 = list2 + " + " + str(fac_num_list[-1]) + str(answ)

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

    stem = stem.format(low=low, temp=temp, high=high,x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(ans1=ans1, eq=eq, low=low, high=high, temp=temp, list=list, list2=list2)

    return stem, answer, comment


# 중1-1-1-63
def naturalnum111_Stem_051():
    stem = "다음에서 두 분수 $$수식$${num1}$$/수식$$, $$수식$${num2}$$/수식$$중 어느 것을 택하여 " \
           "곱해도 자연수가 되는 수가 아닌 것은?\n" \
           "$$수식$$① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n   $$/수식$$"
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "$$수식$${num2}={num10}$$/수식$$이므로 구하는 수를 $$수식$${tmp}$$/수식$$ 라 하면 $$수식$$a$$/수식$$는\n" \
              "$$수식$${num12}$$/수식$${temp1} $$수식$${num23}$$/수식$$ 의 공배수이다.\n" \
              "$$수식$${num12_eq}$$/수식$${temp2} $$수식$${num23_eq}$$/수식$$의 최소공배수는\n" \
              "$$수식$${fac_eq}$$/수식$$ 이므로\n" \
              "$$수식$$a$$/수식$$ = $$수식$${list} CDOTS$$/수식$$\n" \
              "$$수식$$b$$/수식$$는 $$수식$${num11}$$/수식$${temp3} $$수식$${num3}$$/수식$$의 공약수이고 $$수식$${num11}$$/수식$${temp3} $$수식$${num3}$$/수식$$의 최대공약수\n" \
              "는 $$수식$${fact}$$/수식$$이므로 $$수식$$b$$/수식$$ = $$수식$${fac_list}$$/수식$$\n" \
              "따라서 조건을 만족시키는 수는 $$수식$${list}$$/수식$$\n$$수식$$CDOTS$$/수식$$" \
              "$$수식$${frac_list} CDOTS$$/수식$$ 이므로 $$수식$${num1}$$/수식$$, $$수식$${num2}$$/수식$$ 중\n" \
              "어느 것을 택하여 곱해도 자연수가 되는 수가\n" \
              "아닌 것은 $$수식$${answ}$$/수식$$ 이다.\n" \


    a='a'
    b='b'
    tmp="{{%s} over {%s}}"%(a,b)


    num11 = np.random.randint(2, 10)
    num12 = np.random.randint(5, 30)
    while num11 == num12 or num11 >  num12 or num12 % num11 ==0:
        num11 = np.random.randint(2, 10)
        num12 = np.random.randint(5, 30)
    num1  = "$$수식$${"+str(num11)+"} over {"+str(num12)+"}$$/수식$$"
    tempor = num11 * np.random.randint(10, 30)
    num23 = np.random.randint(5, 30)
    num21 =  int(tempor / num23)
    num22 =  tempor % num23
    while num22 >=  num23 or num23 == num12 or tempor % num23==0:
        tempor = num11 * np.random.randint(10, 30)
        num23 = np.random.randint(5, 30)
        num21 = int(tempor / num23)
        num22 = tempor % num23
    # print(tempor)
    # print(num21)
    
    num3 = num21 * num23 +  num22
    num2 = "$$수식$${"+str(num21)+"}{"+str(num22)+"} over {"+str(num23)+"}$$/수식$$"

    num10 = "$$수식$${"+str(num3)+" over {"+str(num23)+"}$$/수식$$"
    temp1 = proc_jo(num12,2)

    num_one = []
    i = 2
    n = num12
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    tem1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in tem1:
            tem1.append(x)
    for x in tem1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = "$$수식$${" + str(num12) + "} `=`$$/수식$$"
    if len(tem1) > 0:
        for i in range(len(tem1) - 1):
            if exp1[i]!=1:
                fact_ = fact_ + "$$수식$${" + str(tem1[i]) + "} ^{" + str(exp1[i]) + "} TIMES$$/수식$$"
            else:
                fact_ = fact_ + "$$수식$${" + str(tem1[i]) + "} TIMES$$/수식$$"
    if len(exp1)>0:
        if exp1[-1] != 1:
            fact_ = fact_ + "$$수식$${" + str(tem1[-1]) + "} ^{" + str(exp1[-1]) + "}$$/수식$$"
        else:
            fact_ = fact_ + "$$수식$${" + str(tem1[-1]) + "}$$/수식$$"
    num12_eq = fact_
    temp2 = proc_jo(tem1[-1],2)

    num_two = []
    i = 2
    n = num23
    while n > 1:
        if n % i == 0:
            num_two.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_two.sort()
    tem2 = []
    exp2 = []
    num_two.sort()
    for x in num_two:
        if x not in tem2:
            tem2.append(x)
    for x in tem2:
        i = 0
        for y in num_two:
            if x == y:
                i += 1
        exp2.append(i)
    fact_ = "$$수식$${" + str(num23) + "}`=`$$/수식$$"
    if len(tem2) > 0:
        for i in range(len(tem2) - 1):
            if exp2[i]!=1:
                fact_ = fact_ + "$$수식$${" + str(tem2[i]) + "} ^{" + str(exp2[i]) + "} TIMES$$/수식$$"
            else:
                fact_ = fact_ + "$$수식$${" + str(tem2[i]) + "} TIMES$$/수식$$"
    if len(exp2)>0:
        if exp2[-1] != 1:
            fact_ = fact_ + "$$수식$${" + str(tem2[-1]) + "} ^{" + str(exp2[-1]) + "}$$/수식$$"
        else:
            fact_ = fact_ + "$$수식$${" + str(tem2[-1]) + "}$$/수식$$"
    num23_eq = fact_

    minu = []
    minu_ep = []

    for i in range (len(tem1)):
        for j in range(len(tem2)):
            if tem1[i]==tem2[j] and tem1[i] not in minu_ep:
                minu.append(tem1[i])
                minu_ep.append(min(exp1[i],exp2[j]))
    for x in tem1:
        if x not in minu:
            minu.append(x)
            minu_ep.append(1)

    for x in tem2:
        if x not in minu:
            minu.append(x)
            minu_ep.append(1)
    top_fra =1
    for i in range(len(minu)):
        top_fra = top_fra * (minu[i]**minu_ep[i])

    fact_=""
    if len(minu) > 0:
        for i in range(len(minu) - 1):
            if minu_ep[i]!=1:
                fact_ = fact_ + "$$수식$${" + str(minu[i]) + "} ^{" + str(minu_ep[i]) + "} TIMES$$/수식$$"
            else:
                fact_ = fact_ + "$$수식$${" + str(minu[i]) + "} TIMES$$/수식$$"
    if len(minu_ep)>0:
        if minu_ep[-1] != 1:
            fact_ = fact_ + "$$수식$${" + str(minu[-1]) + "} ^{" + str(minu_ep[-1]) + "} `=` {" + str(top_fra) + "}$$/수식$$"
        else:
            fact_ = fact_ + "$$수식$${" + str(minu[-1]) + "} `=` {" + str(top_fra) + "}$$/수식$$"
    fac_eq = fact_

    list = ""
    for i in range(1,4):
        list = list + "$$수식$${" + str(top_fra*i) + "}$$/수식$$, "

    temp3 = proc_jo(num11,2)
    fact = 1
    fac_list =""
    # print("num11"+ str(num11))
    # print("num3" + str(num3))
    for i in range(1, max(num11,num3 )+1):
        if num11 % i==0 and num3 % i==0:
            fact = i
    # print(fact)
    for i in range(1, fact):
        if fact % i ==0:
            fac_list = fac_list + "$$수식$${" + str(i) + "}$$/수식$$, "
    fac_list = fac_list + "$$수식$${" + str(fact) + "}$$/수식$$"

    frac_list = ""
    for i in range(1,4):
        frac_list = frac_list + "$$수식$${" + str(top_fra * i) + "} over {" + str(fact) + "}$$/수식$$, "
    answ = ""
    anse = np.random.randint(top_fra+1, top_fra+100)
    # print(fact)
    while anse % top_fra==0 and anse % fact == 0:
        anse = np.random.randint(top_fra+1, top_fra+100)

    answ =  "$$수식$${" + str(anse) + "} over {" + str(fact) + "}$$/수식$$"

    bb = []
    cc=[anse]
    while len(bb) < 4:
        k = np.random.randint(1, 15)
        if k not in cc and top_fra * k!=anse:
            cc.append(k)
            p = "$$수식$${" + str(top_fra * k) + "} over {" + str(fact) + "}$$/수식$$"
            bb.append(p)
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

    stem = stem.format(num1=num1, num2=num2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(tmp=tmp,fact=fact, fac_list=fac_list, frac_list=frac_list, answ=answ, num3=num3, num11=num11,
                             num2=num2, num10=num10, num12=num12, temp1=temp1, temp2=temp2, num23=num23,
                             num12_eq=num12_eq, num23_eq=num23_eq, fac_eq=fac_eq, list=list, temp3=temp3,num1=num1 )

    return stem, answer, comment


# 중1-1-1-64
def naturalnum111_Stem_052():
    stem = "{name}는 {item1} $$수식$${num1}$$/수식$$개, {item2} $$수식$${num2}$$/수식$$개를 가능한 한 많" \
           "은 접시에 똑같이 나누어 담으려고 할 때, 필요한 접시의 개수는?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "필요한 접시의 개수는 $$수식$${list}$$/수식$$\n" \
              "의 최대공약수이어야 하므로 $$수식$${answ1}$$/수식$$(개)이다." \

    nameList = ["경희", "민철이", "수진이", "철수"]
    name = nameList[np.random.randint(0,4)]
    itemList = [["인절미", "가래떡"],["피자", "스파게티"],["만두","김밥"]]
    p = np.random.randint(0,3)
    item1 = itemList[p][0]
    item2 = itemList[p][1]

    num1 =  np.random.randint(5,30)
    num2 =  np.random.randint(5, 30)
    while num1 == num2 or gcd(num1, num2)==1:
        num1 = np.random.randint(5, 30)
        num2 = np.random.randint(5, 30)

    num_one = []
    i = 2
    n = num1
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    tem1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in tem1:
            tem1.append(x)
    for x in tem1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = "$$수식$${" + str(num1) + "} `=`$$/수식$$"
    if len(tem1) > 1:
        for i in range(len(tem1) - 1):
            if exp1[i] != 1:
                fact_ = fact_ + "$$수식$${" + str(tem1[i]) + "} ^{" + str(exp1[i]) + "} TIMES$$/수식$$"
            else:
                fact_ = fact_ + "$$수식$${" + str(tem1[i]) + "} TIMES$$/수식$$"
    if exp1[-1] != 1:
        fact_ = fact_ + "$$수식$${" + str(tem1[-1]) + "} ^{" + str(exp1[-1]) + "}$$/수식$$"
    else:
        fact_ = fact_ + "$$수식$${" + str(tem1[-1]) + "}$$/수식$$"
    list = fact_ + "$$수식$$`, `$$/수식$$"

    num_two = []
    i = 2
    n = num2
    while n > 1:
        if n % i == 0:
            num_two.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_two.sort()
    tem2 = []
    exp2 = []
    num_two.sort()
    for x in num_two:
        if x not in tem2:
            tem2.append(x)
    for x in tem2:
        i = 0
        for y in num_two:
            if x == y:
                i += 1
        exp2.append(i)
    fact_ = "$$수식$${" + str(num2) + "} `=`$$/수식$$"
    if len(tem2) > 1:
        for i in range(len(tem2) - 1):
            if exp2[i] != 1:
                fact_ = fact_ + "$$수식$${" + str(tem2[i]) + "} ^{" + str(exp2[i]) + "} TIMES$$/수식$$"
            else:
                fact_ = fact_ + "$$수식$${" + str(tem2[i]) + "} TIMES$$/수식$$"
    if exp2[-1] != 1:
        fact_ = fact_ + "$$수식$${" + str(tem2[-1]) + "} ^{" + str(exp2[-1]) + "}$$/수식$$"
    else:
        fact_ = fact_ + "$$수식$${" + str(tem2[-1]) + "}$$/수식$$"
    list =  list  + fact_

    answ = gcd (num1, num2)

    num_two = []
    i = 2
    n = answ
    while n > 1:
        if n % i == 0:
            num_two.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_two.sort()
    tem2 = []
    exp2 = []
    num_two.sort()
    for x in num_two:
        if x not in tem2:
            tem2.append(x)
    for x in tem2:
        i = 0
        for y in num_two:
            if x == y:
                i += 1
        exp2.append(i)
    fact_ = ""
    if len(tem2) > 0:
        for i in range(len(tem2) - 1):
            if exp2[i] != 1:
                fact_ = fact_ + "$$수식$${" + str(tem2[i]) + "} ^{" + str(exp2[i]) + "} TIMES$$/수식$$"
            else:
                fact_ = fact_ + "$$수식$${" + str(tem2[i]) + "} TIMES$$/수식$$"
        if exp2[-1] != 1:
            fact_ = fact_ + "$$수식$${" + str(tem2[-1]) + "} ^{" + str(exp2[-1]) + "}$$/수식$$"
        else:
            fact_ = fact_ + "$$수식$${" + str(tem2[-1]) + "}$$/수식$$"
    else:
        fact_ = fact_ + "$$수식$${" + str(1) + "}$$/수식$$"
    answ1 =fact_ +  "$$수식$$`=`{" + str(answ) + "}$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(4, 10)
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
    k = "k"


    stem = stem.format(name=name, item1=item1, item2=item2, num1=num1, num2=num2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=list, answ1=answ1)

    return stem, answer, comment



# 중1-1-1-65
def naturalnum111_Stem_053():
    stem = "가로의 길이가 $$수식$${width}``rm {{cm}}$$/수식$$, 세로의 길이가 $$수식$${length}``rm {{cm}}$$/수식$$인 " \
           "직사각형 모양의 종이를 남는 부분 없이 크기가 " \
           "같은 여러 개의 정사각형 모양의 종이로 나누려고 " \
           "한다. 정사각형의 크기를 될 수 있는 한 크게 할 " \
           "때, 정사각형의 한 변의 길이는?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "

    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "정사각형의 크기를 될 수 있는 한 크게 하려면 정사각형의\n" \
              "한 변의 길이는 $$수식$${width}$$/수식$${temp} $$수식$${length}$$/수식$$의 최대공약수이어야 한다.\n" \
              "따라서 구하는 정사각형의 한 변의 길이는\n" \
              "{eq}$$수식$$(rm cm)$$/수식$$" \

    area = np.random.randint(7000, 9000)
    num1 = np.random.randint(100,200)
    num2 = int(area / num1)
    while area % num1 != 0 or gcd(num1,num2)==1:
        area = np.random.randint(7000, 9000)
        num1 = np.random.randint(100, 200)
        num2 = int(area/num1)

    one_side = gcd(num1, num2)
    answ= one_side
    temp = proc_jo(num1,2)
    num_two = []
    i = 2
    n = one_side
    while n > 1:
        if n % i == 0:
            num_two.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_two.sort()
    tem2 = []
    exp2 = []
    num_two.sort()
    for x in num_two:
        if x not in tem2:
            tem2.append(x)
    for x in tem2:
        i = 0
        for y in num_two:
            if x == y:
                i += 1
        exp2.append(i)
    fact_ = ""
    if len(tem2) > 0:
        for i in range(len(tem2) - 1):
            if exp2[i] != 1:
                fact_ = fact_ + "$$수식$${" + str(tem2[i]) + "} ^{" + str(exp2[i]) + "} TIMES$$/수식$$"
            else:
                fact_ = fact_ + "$$수식$${" + str(tem2[i]) + "} TIMES$$/수식$$"
        if exp2[-1] != 1:
            fact_ = fact_ + "$$수식$${" + str(tem2[-1]) + "} ^{" + str(exp2[-1]) + "}$$/수식$$"
        else:
            fact_ = fact_ + "$$수식$${" + str(tem2[-1]) + "}$$/수식$$"
    else:
        fact_ = fact_ + "$$수식$${" + str(1) + "}$$/수식$$"
    eq =fact_ +  "$$수식$$`=`{" + str(answ) + "}$$/수식$$"

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

    stem = stem.format(width=num1, length=num2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(width=num1, length=num2, eq=eq, temp=temp)

    return stem, answer, comment

# 중1-1-1-68
def naturalnum111_Stem_054():
    stem = "{classe}반의 여학생은 $$수식$${girl}$$/수식$$ 명이고 남학생은 $$수식$${boy}$$/수식$$명이다. " \
           "최대한 많은 모둠으로 나누어 한 모둠에 여학생 " \
           "$$수식$$a$$/수식$$명과 남학생 $$수식$$b$$/수식$$명을 배치하여 실험을 하려고 한다. " \
           "나누어진 모둠의 수를 $$수식$$c$$/수식$$개라 할 때, $$수식$$a + b + c$$/수식$$의 값은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "나누어진 모둠의 수는 $$수식$${girl}$$/수식$$, $$수식$${boy}$$/수식$$의 최대공약수이어야\n" \
              "하므로 $$수식$$c `= `{c}$$/수식$$\n"\
              "한 모둠의 여학생 수와 남학생 수는 각각\n" \
              "$$수식$${eq}$$/수식$$ 이므로 $$수식$$a `=` {a}$$/수식$$, $$수식$$b `=` {b}$$/수식$$\n" \
              "∴ {ans_eq}\n"

    classList = ["볼링","수학","수영","밴드"]
    classe = classList[np.random.randint(0, 4)]
    girl = np.random.randint(10, 30)
    boy = np.random.randint(10, 30)
    while girl == boy or girl*2==boy or boy*2==girl:
        girl = np.random.randint(10, 30)
        boy = np.random.randint(10, 30)

    c = gcd(girl, boy)

    while c==1:
        girl = np.random.randint(10, 30)
        boy = np.random.randint(10, 30)
        while girl == boy or girl*2==boy or boy*2==girl:
            girl = np.random.randint(10, 30)
            boy = np.random.randint(10, 30)
        c = gcd(girl, boy)

    a = int(girl/c)
    b = int(boy/c)

    eq = "$$수식$${" + str(girl) + "} DIV {" + str(c) + "} `=` {" + str(a) + "}$$/수식$$ , "
    eq = eq + "$$수식$${" + str(boy) + "} DIV {" + str(c) + "} `=` {" + str(b) + "}$$/수식$$"

    ans_eq = "$$수식$$`a + b + c = {" + str(a) + " +{" + str(b) + "} + {" + str(c) + "}`=`{" + str(a+b+c) + "}$$/수식$$"

    answ = a+b+c


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

    stem = stem.format(classe=classe, girl=girl, boy=boy, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(c=c, girl=girl, boy=boy, a=a, b=b, ans_eq=ans_eq, eq=eq)

    return stem, answer, comment


# 중1-1-1-70
def naturalnum111_Stem_055():
    stem = "가로의 길이가 $$수식$${width}``rm m$$/수식$$, 세로의 길이가 $$수식$${length}``rm m$$/수식$$인 직사" \
           "각형 모양의 공원의 가장자리를 따라 가로, 세로 " \
           "모두 같은 간격으로 가로등을 설치하려고 한다. " \
           "가로등의 개수는 최소로 하고, 네 모퉁이에는 반드시 " \
           "가로등을 설치한다고 할 때, 설치해야 할 가로등의 개수는?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "가로등 사이의 간격은 $$수식$${width}$$/수식$$, $$수식$${length}$$/수식$$의 최대공약수이어야 하므로 " \
              "$$수식$${gc}``rm m$$/수식$$이다.\n" \
              "이 때 $$수식$${eq}$$/수식$$ 이므로 설치해야 할\n" \
              "가로등의 개수는\n" \
              "{answ_eq}"

    width = np.random.randint(20, 90)
    length = np.random.randint(20, 90)
    while width == length:
        width = np.random.randint(20, 90)

    gc = gcd(width, length)

    while gc == 1:
        width = np.random.randint(20, 90)
        length = np.random.randint(20, 90)
        while width == length:
            length = np.random.randint(20, 90)
        gc = gcd(width, length)

    w = int(width/gc)
    l = int(length/gc)
    eq = "$$수식$${" + str(width) + "} DIV {" + str(gc) + "} `=` {" + str(w) + "}$$/수식$$ , "
    eq = eq + "$$수식$${" + str(length) + "} DIV {" + str(gc) + "} `=` {" + str(l) + "}$$/수식$$"
    answ = (w+l)*2
    answ_eq = "$$수식$$({" + str(w) + "}+{" + str(l) + "})`TIMES` 2`=`{" + str(answ) + "}$$/수식$$"

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


    stem = stem.format(width=width, length=length, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(width=width, length=length, eq=eq, answ_eq=answ_eq, gc=gc)

    return stem, answer, comment


# 중1-1-1-71
def naturalnum111_Stem_056():
    stem = "어떤 수로 $$수식$${num1}$$/수식$${temp10} 나누면 $$수식$${num11}$$/수식$${jo1} 남고, $$수식$${num2}$$/수식$${temp20} 나누면 $$수식$${num21}$$/수식$$" \
           "{jo2} 남는다. 이때 어떤 자연수가 될 수 있는 수들의 합은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "

    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "어떤 자연수는 $$수식$${num1_eq}$$/수식$$, $$수식$${num2_eq}$$/수식$$  즉, $$수식$${num10}$$/수식$$, $$수식$${num20}$$/수식$$의 공약수이므로\n" \
              "어떤 자연수 중 가장 큰 수는 $$수식$${num10}$$/수식$$, $$수식$${num20}$$/수식$$의 최대공약수인 $$수식$${gc}$$/수식$$이다.\n" \
              "이때 어떤 자연수는 $$수식$${num21}$$/수식$$보다 커야 하므로 어떤 자연수가\n" \
              "될수 있는 수는 $$수식$${liste}$$/수식$$이다.\n" \
              "따라서 구하는 합은 $$수식$${ans_eq}$$/수식$$"

    fac = [2, 3, 5, 7]
    num1 = np.random.randint(20, 90)
    num2 = np.random.randint(20, 90)
    while num1 == num2:
        num2 = np.random.randint(20, 90)

    gc = gcd(num1, num2)
    o = np.random.randint(0, 4)
    num11 = fac[o]
    num21 = fac[o - 1]
    if num21 < num11:
        b = num11
        num11 = num21
        num21 = b

    while gc <= num21:
        num1 = np.random.randint(20, 90)
        num2 = np.random.randint(20, 90)
        while num1 == num2:
            num2 = np.random.randint(20, 90)
        gc = gcd(num1, num2)
        o = np.random.randint(0, 4)
        num11 = fac[o]
        num21 = fac[o - 1]
        if num21 < num11:
            b = num11
            num11 = num21
            num21 = b

    num10 = num1
    num20 = num2

    num1 = num1 + num11
    num2 = num2 + num21
    temp10 = proc_jo(num1, 4)
    temp20 = proc_jo(num2, 4)
    jo1 = proc_jo(num11, 0)
    jo2 = proc_jo(num21, 0 )

    num1_eq = "$$수식$${" + str(num1) + "}-{" + str(num11) + "}$$/수식$$"
    num2_eq = "$$수식$${" + str(num2) + "}-{" + str(num21) + "}$$/수식$$"

    ans1=[]
    for i in range(num21+1, gc+1):
        if gc % i ==0:
            ans1.append(i)

    liste=""
    ans_eq =""
    answ = 0
    if len(ans1) >0:
        for i in range(len(ans1)-1):
            liste =  liste + "$$수식$${" + str(ans1[i]) + "}$$/수식$$, "
            ans_eq = ans_eq +  "$$수식$${" + str(ans1[i]) + "}$$/수식$$ + "
            answ = answ + ans1[i]
        answ = answ + ans1[-1]
        liste = liste +  "$$수식$${" + str(ans1[-1]) + "}$$/수식$$"
        ans_eq = ans_eq + "$$수식$${" + str(ans1[-1]) + "} `=` {"+str(answ)+"}$$/수식$$"

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


    stem = stem.format(num1=num1, num2=num2, num11=num11, num21=num21, temp10=temp10, temp20=temp20, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, jo1=jo1, jo2=jo2)
    answer = answer.format(ans=ans)
    comment = comment.format(num1_eq=num1_eq, num2_eq=num2_eq, num10=num10, num20=num20, num21=num21, liste=liste, ans_eq=ans_eq, gc=gc)

    return stem, answer, comment


# 중1-1-1-72
def naturalnum111_Stem_057():
    stem = "한 개에 $$수식$${price1}$$/수식$$원인 {item1}$$수식$${num1}$$/수식$$개, 한개에 $$수식$${price2}$$/수식$$원인 " \
           "{item2}$$수식$${num2}$$/수식$$개, 한개에 $$수식$${price3}$$/수식$$원인 {item3}$$수식$${num3}$$/수식$$개를 남김" \
           "없이 바구니에 담아 판매하려고 한다. 각 과일 바구니에 들어 있는{itemList}의 개수는 " \
           "각각 같게 하고, 과일 바구니를 되도록 많이 만들려고 할 때, 한 바구니의 가격은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "각 과일 바구니에 들어 있는 {itemList}의 개수를\n" \
              "각각 같게 하여 되도록 많은 바구니를 만들려면\n" \
              "바구니의 개수는 $$수식$${num_List}$$/수식$$의 최대공약수이어야 하므로\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "따라서 한 바구니에 들어 있는{itemList}의\n" \
              "개수는 각각 $$수식$${eq2}$$/수식$$\n" \
              "이므로 한 바구니의 가격은\n" \
              "$$수식$${eq3}$$/수식$$(원)\n"


    items = [["오렌지", "키위", "바나나"],["사과","배", "복숭아"],["포도","참외", "수박"]]
    y = np.random.randint(0, 3)
    item1 =  items[y][0]
    item2 =  items[y][1]
    item3 = items[y][2]
    itemList = item1 + ", " +item2 + ", "+item3

    p1 = np.random.randint(5, 11)
    p2 = np.random.randint(5, 11)
    p3 = np.random.randint(5, 11)
    while p1 == p2 or p2 == p3 or p1 ==p3:
        p1 = np.random.randint(5, 11)
        p2 = np.random.randint(5, 11)
        p3 = np.random.randint(5, 11)
    price1 = p1 *100
    price2 = p2 *100
    price3 = p3 *100

    num1 = np.random.randint(10, 40)
    num2 = np.random.randint(10, 40)
    num3 = np.random.randint(10, 40)
    while num1 ==num2 or num2 == num3 or num1 ==num3:
        num1 = np.random.randint(10, 40)
        num2 = np.random.randint(10, 40)
        num2 = np.random.randint(10, 40)

    temp100 = gcd(num1, num2)
    gc = gcd(temp100, num3)
    while gc < 10:
        num1 = np.random.randint(10, 40)
        num2 = np.random.randint(10, 40)
        num3 = np.random.randint(10, 40)
        while num1 == num2 or num2 == num3 or num1 == num3:
            num1 = np.random.randint(10, 40)
            num2 = np.random.randint(10, 40)
            num2 = np.random.randint(10, 40)

        temp100 = gcd(num1, num2)
        gc = gcd(temp100, num3)

    num_List = "$$수식$${" + str(num1) + "}$$/수식$$, $$수식$${" + str(num2) + "}$$/수식$$, $$수식$${" + str(num3) + "}$$/수식$$"
    num_one = []
    i = 2
    n = gc
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = ""
    if len(temp1) > 1:
        for i in range(len(temp1) - 1):
            if exp1[i] != 1:
                fact_ = fact_ + "$$수식$${" + str(temp1[i]) + "} ^{" + str(exp1[i]) + "} TIMES $$/수식$$"
            else:
                fact_ = fact_ + "$$수식$${" + str(temp1[i]) + "} TIMES $$/수식$$"
    if exp1[-1] != 1:
        fact_ = fact_ + "$$수식$${" + str(temp1[-1]) + "} ^{" + str(exp1[-1]) + "}$$/수식$$"
    else:
        fact_ = fact_ + "$$수식$${" + str(temp1[-1]) + "}$$/수식$$"
    eq = fact_ + " $$수식$$`=` {" + str(gc) + "}$$/수식$$"

    a = int(num1/gc)
    b = int(num2/gc)
    c = int(num3/gc)

    eq2 = "$$수식$${" + str(num1) + "} DIV {" + str(gc) + "} `=` {" + str(a) + "}$$/수식$$ , "
    eq2 = eq2 + "$$수식$${" + str(num2) + "} DIV {" + str(gc) + "} `=` {" + str(b) + "}$$/수식$$ , "
    eq2 = eq2 + "$$수식$${" + str(num3) + "} DIV {" + str(gc) + "} `=` {" + str(c) + "}$$/수식$$"

    answ = price1*a + price2*b + price3*c
    eq3 = "$$수식$${" + str(price1) + "} TIMES {" + str(a) + "} `+`$$/수식$$"
    eq3 = eq3 + "$$수식$${" + str(price2) + "} TIMES {" + str(b) + "} `+`$$/수식$$"
    eq3 = eq3 + "$$수식$${" + str(price3) + "} TIMES {" + str(c) + "} `=` {" + str(answ) + "}$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)*1000
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

    stem = stem.format(price1=price1, price2=price2, price3=price3, item1=item1, item2=item2, item3=item3, num1=num1,
                       num2=num2, num3=num3, x1=x1, x2=x2,
                       x3=x3, x4=x4, x5=x5, itemList=itemList)
    answer = answer.format(ans=ans)
    comment = comment.format(itemList=itemList, num_List=num_List, eq2=eq2, eq=eq, eq3=eq3, gc=gc)

    return stem, answer, comment


# 중1-1-1-73
def naturalnum111_Stem_058():
    stem = "가로의 길이가 $$수식$${num1}``rm cm$$/수식$$, 세로의 길이가 $$수식$${num2}``rm cm$$/수식$$, " \
           "높이가 $$수식$${num3}``rm cm$$/수식$$인 직육면체 모양의 나무 상자에 " \
           "크기가 같은 정육면체 모양의 제품을 담으려고 한다. " \
           "이 나무 상자에 제품을 빈틈없이 담을 때, 담을 수 있는 제품의 최소 개수는? " \
           "(단, 제품의 한 모서리의 길이는 소수이다.)\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "

    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "정육면체 모양의 제품의 한 모서리의 길이는 $$수식$${num1}$$/수식$$, \n" \
              "$$수식$${num2}$$/수식$$, $$수식$${num3}$$/수식$$의 공약수 이어야 한다. 즉 $$수식$${num1}$$/수식$$, " \
              "$$수식$${num2}$$/수식$$, \n$$수식$${num3}$$/수식$$의 최대공약수는 $$수식$${corner}$$/수식$$이므로 한 모서리의 길이는\n" \
              "$$수식$${corner}``rm cm$$/수식$$의 약수이어야 한다.\n" \
              "이때 $$수식$${corner}$$/수식$$의 약수는 $$수식$${list}$$/수식$$이고, 이 중 가장\n" \
              "큰 소수는 $$수식$${prime}$$/수식$$이므로 정육면체 모양의 제품의 한\n" \
              "모서리의 길이는 $$수식$${prime}``rm cm$$/수식$$이다.\n" \
              "따라서 필요한 정육면체 모양의 제품의 개수는 밑면의\n" \
              " 가로 방향으로 $$수식$${num1_eq}$$/수식$$ 세로 방향으\n" \
              "로 $$수식$${num2_eq}$$/수식$$,  높이로 $$수식$${num3_eq}$$/수식$$  이므로\n" \
              "구하는 개수는\n" \
              "$$수식$${ans_eq}$$/수식$$"


    num1= np.random.randint(100, 400)
    num2= np.random.randint(100, 400)
    num3= np.random.randint(100, 400)
    while num1 == num2 or num2 == num3 or num1 == num3:
        num1 = np.random.randint(100, 400)
        num2 = np.random.randint(100, 400)
        num3 = np.random.randint(100, 400)

    temp100 = gcd(num1, num2)
    gc = gcd(temp100, num3)
    while gc < 20:
        num1 = np.random.randint(100, 400)
        num2 = np.random.randint(100, 400)
        num3 = np.random.randint(100, 400)
        while num1 == num2 or num2 == num3 or num1 == num3:
            num1 = np.random.randint(100, 400)
            num2 = np.random.randint(100, 400)
            num3 = np.random.randint(100, 400)

        temp100 = gcd(num1, num2)
        gc = gcd(temp100, num3)
    corner = gc
    fac = [2,3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    num_one = []
    i = 2
    n = gc
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = [1]
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)

    list=""
    temp1.sort()
    for i in range (len(temp1)-1):
        list = list + "$$수식$${" + str(temp1[i]) + "}$$/수식$$ , "
    list = list + "$$수식$${" + str(temp1[-1]) + "}$$/수식$$"

    prime =1
    for x in temp1:
        if x in fac:
            prime = x
    a = int(num1/gc)
    b = int(num2/gc)
    c = int(num3/gc)


    num1_eq = "$$수식$${" + str(num1) + "} DIV {" + str(gc) + "} `=` {" + str(a) + "}$$/수식$$ , "
    num2_eq =  "$$수식$${" + str(num2) + "} DIV {" + str(gc) + "} `=` {" + str(b) + "}$$/수식$$ , "
    num3_eq =  "$$수식$${" + str(num3) + "} DIV {" + str(gc) + "} `=` {" + str(c) + "}$$/수식$$"

    ans_eq = "$$수식$${" + str(a) + "} TIMES {" + str(b) + "} TIMES {" + str(c) + "} `=` {" + str(a*b*c) + "}$$/수식$$"
    answ = a*b*c
    bb = []
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)*100
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

    stem = stem.format(num1=num1, num2=num2, num3=num3, x1=x1, x2=x2,x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(list=list, num1=num1, num2=num2, num3=num3, corner=corner, prime=prime, num1_eq=num1_eq, num2_eq=num2_eq, num3_eq=num3_eq,ans_eq=ans_eq )

    return stem, answer, comment


# 중1-1-1-74
def naturalnum111_Stem_059():
    stem = "가로의 길이가 $$수식$${num1}``rm m$$/수식$$, 세로의 길이가 $$수식$${num2}``rm m$$/수식$$인 직사각형 모양의 땅이 있다. " \
           "이 땅에서 소를 키우기 위해 울타리를 설치하려고 할 때, 다음 조건을 모두 만족하는 최소한의 말뚝의 개수는?\n" \
           "$$표$$" \
           "(가) 네 모퉁이에는 반드시 말둑을 박아야 한다.\n" \
           "(나) 땅의 둘레에 같은 간격으로 말뚝을 박아야 한다.\n" \
           "(다) 말뚝 사이의 간격은 $$수식$${limit}``rm m$$/수식$$를 넘지 않아야 한다.\n" \
           "$$/표$$\n"  \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "

    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "(가), (나)에 의해 말뚝 사이의 간격은 $$수식$${num1}$$/수식$${temp} $$수식$${num2}$$/수식$$의\n" \
              "공약수이어야 한다.\n" \
              "$$수식$${num1}$$/수식$${temp} $$수식$${num2}$$/수식$$의 최대공약수는 $$수식$${gce}$$/수식$$이므로 \n" \
              "$$수식$${num1}$$/수식$${temp} $$수식$${num2}$$/수식$$의 공약수는 $$수식$${liste}$$/수식$$이다.\n" \
              "(다)에서 말뚝 사이의 간격이 $$수식$${limit}`rm m $$/수식$$ 를 넘지 않아야\n" \
              "하므로 말뚝 사이의 간격은 $$수식$${list_limit}$$/수식$$이다.\n" \
              "이때 이를 만족하는 최소한의 말뚝의 개수를 구하려면\n" \
              "말뚝 사이의 간격이 최대한 넓어야 하므로\n" \
              "말뚝 사이의 간격은 $$수식$${ans11}``rm m $$/수식$$ 이어야 한다.\n" \
              "{eq}이므로 구하는 말뚝의 개수는\n" \
              "{ans_eq}"

    num1 = np.random.randint(70, 150)
    num2 = np.random.randint(70, 150)
    while num1 == num2 or gcd(num1,num2)==1:
        num1 = np.random.randint(70, 150)
        num2 = np.random.randint(70, 150)

    gc = gcd(num1, num2)
    while gc < 10:
        num1 = np.random.randint(70, 150)
        num2 = np.random.randint(70, 150)
        while num1 == num2:
            num1 = np.random.randint(70, 150)
            num2 = np.random.randint(70, 150)

        gc = gcd(num1, num2)
    if num1 > num2:
        b  =num1
        num1 = num2
        num2 = b
    temp = proc_jo(num1, 2)

    num_one = []
    i = 2
    n = gc
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = ""
    if len(temp1) > 0:
        for i in range(len(num_one) - 1):
            fact_ = fact_ + "$$수식$${" + str(num_one[i]) + "} TIMES$$/수식$$"
        fact_ = fact_ + "$$수식$${" + str(num_one[-1]) + "} `=` {" + str(gc) + "}$$/수식$$"
    gce = fact_
    listtt =[]
    liste=""
    for i in range(1, gc+1):
        if gc % i ==0:
            listtt.append(i)

    for i in range(len(listtt)-1):
        liste = liste + "$$수식$${" + str(listtt[i]) + "}$$/수식$$ , "
    liste = liste + "$$수식$${" + str(listtt[-1]) + "}$$/수식$$"

    list_limit=""
    list_limite =[]
    limit = np.random.randint(5, 10)
    for i in range(len(listtt) - 1):
        if listtt[i] <= limit:
            list_limite.append(listtt[i])
    if listtt[-1] <= limit:
        list_limite.append(listtt[-1])
    for i in range(len(list_limite)-1):
        list_limit = list_limit + "$$수식$${" + str(list_limite[i]) + "}``rm m$$/수식$$, "
    list_limit = list_limit + "$$수식$${" + str(list_limite[-1]) + "}``rm m$$/수식$$"
    ans11 = list_limite[-1]

    a = int(num1/gc)
    b = int(num2/gc)
    answ = (a+b)*2
    eq ="$$수식$${" + str(num1) + "} DIV{" + str(gc) + "} `=` {" + str(a) + "}$$/수식$$ , "
    eq = eq + "$$수식$${" + str(num2) + "} DIV{" + str(gc) + "} `=` {" + str(b) + "}$$/수식$$ , "

    ans_eq = "$$수식$$ 2 `TIMES$$/수식$$ ($$수식$${" + str(a) + "}$$/수식$$  +  $$수식$${" + str(b) + "}$$/수식$$) $$수식$$`=` {" + str(answ) + "}$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k>1:
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

    stem = stem.format(num1=num1, num2=num2, limit=limit, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(temp=temp, gce=gce, num1=num1, num2=num2, limit=limit, list_limit=list_limit, ans11=ans11,
                             eq=eq, ans_eq=ans_eq, liste=liste)

    return stem, answer, comment



# 중1-1-1-75
def naturalnum111_Stem_060():
    stem = "{school} 중학교에서 점심 급식으로 {food1}$$수식$${num1}$$/수식$$개, " \
           "{food2} $$수식$${num2}$$/수식$$개를 만들어 $$수식$$1$$/수식$$학년 학생들 모두에게 " \
           "똑같이 나누어 주었더니 {foodList} 모두 " \
           "$$수식$${left}$$/수식$$개씩 남았을 때 $$수식$$1$$/수식$$학년 학생 수를 구하시오. " \
           "(단, $$수식$$1$$/수식$$학년 학생 수는 $$수식$$100$$/수식$$명 보다 많고 $$수식$$200$$/수식$$명 보다 적다.)"
    answer = "(답):\n$$수식$${ans}$$/수식$$명"
    comment = "(해설)\n" \
              "{foodList}  모두 $$수식$${left}$$/수식$$개씩 남았으므로\n" \
              "{food1_t} $$수식$${eq1}$$/수식$$ (개), \n" \
              "{food2_t} $$수식$${eq2}$$/수식$$ (개)이면\n" \
              "학생들에게 똑같이 나누어줄 수 있다.\n" \
              "따라서 학생 수는 $$수식$${num10}$$/수식$$, $$수식$${num20}$$/수식$$의 최대공약수인\n" \
              "$$수식$${gc_eq}$$/수식$$ 의 약수이면서 $$수식$${left}$$/수식$$보다 큰 수이므로\n" \
              "$$수식$${list}$$/수식$$\n" \
              "이때 $$수식$$1$$/수식$$학년 학생은 $$수식$$100$$/수식$$명보다 많고 $$수식$$200$$/수식$$명 보다\n" \
              "적으므로 $$수식$$1$$/수식$$학년 학생 수는 $$수식$${answ}$$/수식$$명이다.\n"


    schoole = ["대지","벼리","온수","서초","슬기"]
    school = schoole[np.random.randint(0, 5)]
    foods = [["삶은계란","버섯전"],["돈까스","소세지"],["버섯구이","마늘구이"]]
    m = np.random.randint(0, 3)
    food1 = foods[m][0]
    food2 = foods[m][1]
    foodList = food1 + proc_jo(food1, 2) + " "  + food2
    food1_t = food1 + proc_jo(food1, 3)
    food2_t = food2 + proc_jo(food2, 3)


    answ = np.random.randint(101, 200)
    num1 = answ*np.random.randint(2, 5)
    num2 = answ*np.random.randint(2, 5)
    while num1 == num2:
        num1 = answ * np.random.randint(2, 5)
        num2 = answ * np.random.randint(2, 5)
    gc = gcd(num1, num2)
    while gc < 10:
        answ = np.random.randint(101, 200)
        num1 = answ * np.random.randint(2, 5)
        num2 = answ * np.random.randint(2, 5)
        while num1 == num2:
            num1 = answ * np.random.randint(2, 5)
            num2 = answ * np.random.randint(2, 5)
    num10 = num1
    num20 = num2
    left = np.random.randint(5, 10)
    num1 = num1 + left
    num2 = num2 + left

    num_one = []
    i = 2
    n = gc
    while n > 1:
        if n % i == 0:
            num_one.append(i)
            n = n / i
            i = i - 1
        i += 1
    num_one.sort()
    temp1 = []
    exp1 = []
    num_one.sort()
    for x in num_one:
        if x not in temp1:
            temp1.append(x)
    for x in temp1:
        i = 0
        for y in num_one:
            if x == y:
                i += 1
        exp1.append(i)
    fact_ = ""
    if len(temp1) > 1:
        for i in range(len(temp1) - 1):
            if exp1[i] != 1:
                fact_ = fact_ + "$$수식$${" + str(temp1[i]) + "} ^{" + str(exp1[i]) + "} TIMES$$/수식$$"
            else:
                fact_ = fact_ + "$$수식$${" + str(temp1[i]) + "} TIMES$$/수식$$"
    if exp1[-1] != 1:
        fact_ = fact_ + "$$수식$${" + str(temp1[-1]) + "} ^{" + str(exp1[-1]) + "}$$/수식$$"
    else:
        fact_ = fact_ + "$$수식$${" + str(temp1[-1]) + "}$$/수식$$"
    gc_eq = fact_ + "   $$수식$$`=` {" + str(gc) + "}$$/수식$$"

    eq1 = "$$수식$${" + str(num1) + "} - {" + str(left) + "} `=` {" + str(num10) + "}$$/수식$$"
    eq2 = "$$수식$${" + str(num2) + "} - {" + str(left) + "} `=` {" + str(num20) + "}$$/수식$$"

    gc_lists =[]
    for i in range(left+1, gc+1):
        if gc % i ==0:
            gc_lists.append(i)
    list=""
    for i in range(len(gc_lists)-1):
        list = list + "$$수식$${" + str(gc_lists[i]) + "}$$/수식$$ , "
    list = list + "$$수식$${" + str(gc_lists[-1]) + "}$$/수식$$"

    stem = stem.format(num1=num1, num2=num2, school=school, food1=food1, food2=food2, left=left, foodList=foodList)
    answer = answer.format(ans=answ)
    comment = comment.format(foodList=foodList, left=left, food1_t=food1_t, food2_t=food2_t, eq2=eq2, eq1=eq1,
                             num10=num10, num20=num20, list=list, answ=answ, gc_eq=gc_eq)

    return stem, answer, comment


# 중1-1-1-77
def naturalnum111_Stem_061():
    stem = "세 수 {num1}, {num2}, {num3}의 최소공배수는?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n$$/수식$$"
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "주어진 세 수의 최소공배수는 $$수식$${answ}$$/수식$$" \

    num11 = np.random.randint(20, 100)
    num22 = np.random.randint(20, 100)
    num33 = np.random.randint(20, 100)

    while num11==num22 or num11 == num33 or num22==num33:
        num22 = np.random.randint(20, 100)
        num33 = np.random.randint(20, 100)
    num1 = factor_equation(num11)
    num2 = factor_equation(num22)
    num3 = factor_equation(num33)

    ans11 = lcm(lcm(num11,num22),num33)
    answ = factor_equation(ans11)

    cc=[]
    bb=[]
    while len(cc) <4:
        p =  np.random.randint(2, 6)
        if ans11*p not in cc:
            cc.append(ans11*p)
            bb.append(factor_equation(ans11*p))

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

    stem = stem.format(num1=num1, num2=num2, num3=num3,x1=x1, x2=x2, x3=x3, x4=x4, x5=x5 )
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ)

    return stem, answer, comment



# 중1-1-1-78
def naturalnum111_Stem_062():
    stem = "세 자연수 $$수식$$A,` B,` C$$/수식$$의 최소공배수가 $$수식$${lcm1}$$/수식$$일 때, " \
           "$$수식$$ A, B, C$$/수식$$의 공배수 중 가장 작은 세 자리 자연수는?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "$$수식$$A, B, C$$/수식$$의 공배수는 세 수의 최소공배수인 $$수식$${lcm1}$$/수식$$의 배수이다.\n" \
              "{eq1}, {eq2}이므로 공배수 중 가장\n" \
              "작은 세 자리 자연수는 $$수식$${answ}$$/수식$$이다.\n"

    lcm1 = np.random.randint(10, 30)
    op = 0
    for i in range(1, 1000):
        if lcm1*i > 99:
            op = i
            break

    answ = lcm1*op

    eq1 = "$$수식$${" + str(lcm1) + "} TIMES {" + str(op-1) + "}$$/수식$$"
    eq1 = eq1 + "$$수식$$`=` {" + str(lcm1*(op-1)) + "}$$/수식$$"
    eq2 =  "$$수식$${" + str(lcm1) + "} TIMES {" + str(op) + "}$$/수식$$"
    eq2 = eq2 + "$$수식$$`=` {" + str(lcm1*op) + "}$$/수식$$"

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

    stem = stem.format(lcm1=lcm1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(lcm1=lcm1, eq1=eq1, eq2=eq2, answ=answ)

    return stem, answer, comment



# 중1-1-1-80
def naturalnum111_Stem_063():
    stem = "두 자연수 $$수식$$A$$/수식$$와 $$수식$${num}$$/수식$$의 최소공배수가 $$수식$${lcm1}$$/수식$$" \
           "일 때, 다음 중 $$수식$$A$$/수식$$의 값이 될 수 없는 것은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "$$수식$${num}$$/수식$$ = $$수식$${num_eq}$$/수식$$\n" \
              "$$수식$${list}$$/수식$$\n" \

    num = np.random.randint(20, 50)
    num_eq = factor_equation(num)
    temp1 = np.random.randint(20, 200)

    lcm1 = lcm(num, temp1)
    cc=[]
    lcm_eq = factor_equation(lcm1)

    while len(cc)< 4:
        temp1 = np.random.randint(20, 200)
        lcm2 = lcm(num, temp1)
        while lcm1 != lcm2 and temp1 in cc:
            temp1 = np.random.randint(20, 200)
            lcm2 = lcm(num, temp1)
        cc.append(temp1)

    temp2 = np.random.randint(20, 200)
    lcm3 = lcm(num, temp2)
    while lcm1 == lcm3:
        temp2 = np.random.randint(20, 200)
        lcm3 = lcm(num, temp2)
    answ = temp2

    bb=[]
    for x in cc:
        e=""
        e = "$$수식$${" + str(x) + "} `=`$$/수식$$" + factor_equation(x) + " 이므로 $$수식$$"+str(num)+"$$/수식$$ $수식$$``$$/수식$$" + proc_jo(num, 2) + "의 최소공배수는 " + lcm_eq +"\n"
        bb.append(e)
    bb.append("$$수식$${" + str(temp2) + "} `=`$$/수식$$" + factor_equation(temp2) + " 이므로 $$수식$$"+str(num)+"$$/수식$$ $수식$$``$$/수식$$" + proc_jo(num, 2) + "의 최소공배수는 " + factor_equation(lcm3)+"\n" )


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
        liste = "① " + bb[4] + "② " + bb[0] + "③ " + bb[1] + "④ " + bb[2] + "⑤ " + bb[3]
    elif rande == 2:
        liste = "① " + bb[0] + "② " + bb[4] + "③ " + bb[1] + "④ " + bb[2] + "⑤ " + bb[3]
    elif rande == 3:
        liste = "① " + bb[0] + "② " + bb[1] + "③ " + bb[4] + "④ " + bb[2] + "⑤ " + bb[3]
    elif rande == 4:
        liste = "① " + bb[0] + "② " + bb[1] + "③ " + bb[2] + "④ " + bb[4] + "⑤ " + bb[3]
    else:
        liste = "① " + bb[0] + "② " + bb[1] + "③ " + bb[2] + "④ " + bb[3] + "⑤ " + bb[4]

    stem = stem.format(num=num, lcm1=lcm_eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num=num, num_eq=num_eq, list=liste)

    return stem, answer, comment


# 중1-1-1-84
def naturalnum111_Stem_064():
    stem = "두 분수 $$수식$$1 over {num1}$$/수식$$, $$수식$$1 over {num2}$$/수식$$의 어느 것에 곱하여도 그 결과" \
           "가 자연수가 되는 자연수 중에서 가장 작은 수는?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
          
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "두 분수 $$수식$$1 over {num1}$$/수식$$, $$수식$$1 over {num2}$$/수식$$의 어느 것에 곱하여도 그 결과가 자연\n" \
              "수가 되는 자연수는 두 분수 $$수식$${num1}$$/수식$${temp} $$수식$${num2}$$/수식$$의 공배수이다.\n" \
              "이때 $$수식$${num1}$$/수식$${temp} $$수식$${num2}$$/수식$$의 최소공배수는 $$수식$${eq}$$/수식$$이므로\n" \
              "구하는 수는 $$수식$${answ}$$/수식$$이다.\n" \


    num1 = np.random.randint(20, 100)
    num2 = np.random.randint(20, 100)
    while num1 == num2:
        num2 = np.random.randint(20, 100)

    answ = lcm(num1, num2)
    temp = proc_jo(num1, 2)

    eq = factor_equation(answ)
    eq = eq + "$$수식$$={"+str(answ)+"}$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k!=1:
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

    stem = stem.format(num1=num1, num2=num2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, num1=num1,num2=num2, temp=temp, answ=answ)

    return stem, answer, comment



# 중1-1-1-85
def naturalnum111_Stem_065():
    stem = "두 분수 $$수식$${num11} over {num1}$$/수식$$, $$수식$${num22} over {num2}$$/수식$$의 어느 것에 곱하여도 그 결과" \
           "가 자연수가 되는 분수 중에서 가장 작은 수는?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n$$/수식$$"
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "구하는 분수를 $$수식$${tmp}$$/수식$$라 하면\n" \
              "a는 $$수식$${num11}$$/수식$$, $$수식$${num22}$$/수식$$의 최대공약수이어야 하므로 $$수식$$a =  {ans1}$$/수식$$\n" \
              "b는 $$수식$${num1}$$/수식$$, $$수식$${num2}$$/수식$$의 최소공배수이어야 하므로 $$수식$$b = {ans2}$$/수식$$\n" \
              "따라서 구하는 분수는 $$수식$${ans2} over {ans1}$$/수식$$이다.\n"
    aa='a'
    bb='b'
    tmp="{%s}over{%s}"%(bb,aa)
    num1=1
    num2 =1
    num11=num22=1
    ans1 = ans2 = 1
    while ans2>100 or ans1 % ans2 == 0 or ans1==0 or ans1==1:
        num11 = np.random.randint(10, 50)
        num1 = np.random.randint(10, 50)
        num2 = np.random.randint(10, 50)
        while num1 == num2:
            num2 = np.random.randint(10, 50)
        if num1 > num11:
            b = num11
            num11 = num1
            num1 = b
        while gcd(num11, num1)!=1:
            num11 = np.random.randint(10, 50)
        num22 = np.random.randint(10, 50)

        if num22 > num2:
            b = num22
            num22 = num2
            num2 = b
        while gcd(num22, num2)!=1:
            num22 = np.random.randint(10, 50)
        ans1 = gcd(num11, num22)
        ans2 = lcm(num1, num2)
    answ = "$$수식$${"+str(ans2)+"} over {"+str(ans1)+"}$$/수식$$"
    cc=[]
    dd=[]
    while len(cc)<4:
        p  = np.random.randint(1, 10)
        if num11 + p % num1 !=0 and num11+p not in dd:
            dd.append(num11+p)
            cc.append("$$수식$${"+str(num11+p)+"} over {"+str(num1)+"}$$/수식$$")
        if num2 + p % num22 != 0 and num2+p not in dd:
            dd.append(num2+p)
            cc.append("$$수식$${" + str(num22) + "} over {" + str(num2+p) + "}$$/수식$$")

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

    stem = stem.format(num11=num11, num1=num1,num22=num22, num2=num2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num11=num11,tmp=tmp, num1=num1,num22=num22, num2=num2, ans1=ans1, ans2=ans2)

    return stem, answer, comment



# 중1-1-1-86
def naturalnum111_Stem_066():
    stem = "어떤 자연수에 $$수식$${num1}$$/수식$${temp1} 곱하여 $$수식$${num2}$$/수식$$, $$수식$${num3}$$/수식$$의 공배" \
           "수가 되게 하려고 한다. 이러한 자연수 중 가장 작은 것은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "$$수식$${eq1}$$/수식$$, $$수식$${eq2}$$/수식$$의 최소공배수는\n" \
              "$$수식$${lcm_eq}$$/수식$$\n" \
              "따라서 어떤 자연수를 $$수식$$x$$/수식$$라 하면 $$수식$$x `TIMES {num1}$$/수식$${temp2} $$수식$${lcm1}$$/수식$$의\n" \
              "배수이므로\n" \
              "$$수식$$x `TIMES {num1}$$/수식$$ = $$수식$${list1}$$/수식$$\n" \
              "∴ $$수식$$x `= `$$/수식$${list2}\n" \
              "즉, 가장 작은 자연수는 $$수식$${answ}$$/수식$$\n"

    num1 = np.random.randint(10, 30)
    num2 = np.random.randint(30, 70)
    num3 =  np.random.randint(30, 70)
    lcm1 = lcm(num2, num3)
    while num2==num3 or lcm1 % num1 ==0:
        num1 = np.random.randint(10, 30)
        num2 = np.random.randint(30, 70)
        num3 = np.random.randint(30, 70)
        lcm1 = lcm(num2, num3)
    if num2 > num3:
        b = num2
        num2 = num3
        num3 = b

    eq1 = factor_equation(num2)
    eq1 = "$$수식$$"+str(num2)+" `=`$$/수식$$" + eq1
    eq2 = factor_equation(num3)
    eq2 = "$$수식$$" + str(num3) + " `=`$$/수식$$" + eq2
    temp1 = proc_jo(num1,4)
    temp2 = proc_jo(num1, -1)


    lcm_eq = factor_equation(lcm1)
    lcm_eq = lcm_eq + "$$수식$$`=` "+str(lcm1)+"$$/수식$$"
    list = ""
    list2 =""
    for i in range(1,3):
        list = list + "$$수식$$"+str(lcm1*i)+" ` ,`$$/수식$$"
        list2 = list2 + "$$수식$$"+str(int(lcm1*i/num1))+" ` ,`$$/수식$$"
    list = list + "$$수식$$CDOTS$$/수식$$"
    list2 = list2 + "$$수식$$CDOTS$$/수식$$"

    answ = int(lcm1/num1)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k!=1:
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

    stem = stem.format(num1=num1,num3=num3, num2=num2, temp1=temp1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, eq1=eq1, eq2=eq2, lcm_eq=lcm_eq, temp2=temp2, num1=num1,lcm1=lcm1, list1=list, list2=list2, num2=num2)

    return stem, answer, comment




# 중1-1-1-87
def naturalnum111_Stem_067():
    stem = "두 자연수 $$수식$$A, B$$/수식$$에 대하여 $$수식$$A◉B$$/수식$$는 두 수의 최대공약수를, $$수식$$A◇B$$/수식$$는 두 수의 최소공배수를 나타낸다고 할때 " \
           "$$수식$${num1}◉({num2}◇{num3})$$/수식$$의 값은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "$$수식$${num2}◇{num3}=$$/수식$$({eq1})$$수식$$◇$$/수식$$({eq2})$$수식$$ = $$/수식$${lcm_eq}\n" \
              "∴ $$수식$${num1}◉({num2}◇{num3})=$$/수식$$({eq3})$$수식$$◉$$/수식$$({lcm_eq})\n" \
              "$$수식$$=$$/수식$${gcd_eq}$$수식$$ = {answ}$$/수식$$\n" \


    num2 = np.random.randint(4, 90)
    num3 = np.random.randint(4, 90)
    while num2 == num3:
        num2 = np.random.randint(4, 90)
        num3 = np.random.randint(4, 90)
    if num2 > num3:
        b = num2
        num2 = num3
        num3 =b
    lcm1 = lcm(num2, num3)
    lcm_eq =  factor_equation(lcm1)
    eq1 = factor_equation(num2)
    eq2  = factor_equation(num3)

    num1 = np.random.randint(4, 90)
    while num1==num2 or num1==num3:
        num1 = np.random.randint(4, 90)
    answ = gcd(num1, lcm1)
    while answ <2 or answ>50:
        num2 = np.random.randint(4, 90)
        num3 = np.random.randint(4, 90)
        while num2 == num3:
            num2 = np.random.randint(4, 90)
            num3 = np.random.randint(4, 90)
        if num2 > num3:
            b = num2
            num2 = num3
            num3 = b
        lcm1 = lcm(num2, num3)
        lcm_eq = factor_equation(lcm1)
        eq1 = factor_equation(num2)
        eq2 = factor_equation(num3)

        num1 = np.random.randint(4, 90)
        while num1 == num2 or num1 == num3:
            num1 = np.random.randint(4, 90)
        answ = gcd(num1, lcm1)
    eq3 = factor_equation(num1)

    gcd_eq = factor_equation(answ)

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k>1:
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

    stem = stem.format(num1=num1, num3=num3, num2=num2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, eq1=eq1, eq2=eq2, lcm_eq=lcm_eq, num1=num1, num2=num2, num3=num3,
                             eq3=eq3, gcd_eq=gcd_eq)

    return stem, answer, comment


# 중1-1-1-88
#three dots
def naturalnum111_Stem_068():
    stem = "세 수 $$수식$${num1},``{num2},``{num3}$$/수식$$의 " \
           "최대공약수가 $$수식$${gcd_eq}$$/수식$$, 최소공배수가 " \
           "$$수식$${lcm_eq}$$/수식$$일 때, 자연수 $$수식$$a,` b,` c`$$/수식$$에 대하여 " \
           "$$수식$$a+b+c$$/수식$$의 값은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "

    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "세 수 $$수식$${num1}$$/수식$$, $$수식$${num2}$$/수식$$, $$수식$${num3}$$/수식$$의\n" \
              "최소공배수가 $$수식$${lcm_eq}$$/수식$$ 이므로\n" \
              "$$수식$$2 ^a$$/수식$$ = $$수식$$2 ^{a}$$/수식$$, $$수식$$5 ^c$$/수식$$ = $$수식$$5 ^{c}$$/수식$$ ∴  $$수식$$`a` =`{a}$$/수식$$,  $$수식$$c `= `{c}$$/수식$$\n" \
              "한편 최대공약수가 $$수식$${gcd_eq}$$/수식$$이고 세 수의\n" \
              "최대공약수, 최소공배수의 소인수 $$수식$$3$$/수식$$의 지수가\n" \
              "{list}이므로\n" \
              "$$수식$$3 ^b=3 ^{b}$$/수식$$    ∴ $$수식$$b `=` {b}$$/수식$$\n" \
              "∴ $$수식$$  a `+` b `+` c `=` {answ}$$/수식$$"\

    a = np.random.randint(2, 5)
    b = np.random.randint(2, 5)
    c = np.random.randint(2, 5)
    exp13 = np.random.randint(1,6)
    while True:
        if exp13 < c:
            break
        exp13 = np.random.randint(1, 6)
    exp12 =np.random.randint(1,6)
    while True:
        if exp12 >  b:
            break
        exp12 = np.random.randint(1, 6)
    exp21 = np.random.randint(1, 6)
    while True:
        if exp21 < a:
            break
        exp21 = np.random.randint(1, 6)
    exp23 = np.random.randint(1,6)
    while True:
        if exp23 <  c:
            break
        exp23 = np.random.randint(1, 6)
    exp31 = np.random.randint(1,6)
    while True:
        if exp31 <a:
            break
        exp31 = np.random.randint(1, 6)
    exp32 = np.random.randint(1,6)
    while True:
        if exp32 > b:
            break
        exp32 = np.random.randint(1, 6)

    exp34 = np.random.randint(1, 5)
    num11 = 2**a*3**exp12*5**exp13
    num22= 2**exp21*3**b*5**exp23*7**exp34
    num33 = 2**exp31*3**exp32*5**c

    num1 = "$$수식$${2} ^{a} TIMES$$/수식$$" + factor_equation(3**exp12*5**exp13)
    num2 = factor_equation(2**exp21) + "$$수식$$TIMES 3 ^b TIMES$$/수식$$" + factor_equation(5**exp23*7**exp34)
    num3 = factor_equation(2**exp31*3**exp32) +"$$수식$$TIMES 5^ c$$/수식$$"

    lcm_eq = factor_equation(lcm(lcm(num11,num22),num33))
    gcd_eq = factor_equation(gcd(gcd(num11,num22),num33))

    list=""
    if exp12 == exp32:
        list = "모두 " + "$$수식$${"+str(exp12)+"}$$/수식$$ "
    else:
        list = "$$수식$${"+str(exp12)+"}$$/수식$$, $$수식$${"+str(exp32)+"}$$/수식$$"

    answ = a+b+c

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k!=1:
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



    stem = stem.format(num1=num1, num3=num3, num2=num2, gcd_eq=gcd_eq, lcm_eq=lcm_eq, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(answ=answ, num1=num1, num3=num3, num2=num2, gcd_eq=gcd_eq, lcm_eq=lcm_eq,a=a, b=b, c=c, list=list)

    return stem, answer, comment



# 중1-1-1-90
def naturalnum111_Stem_069():
    stem = "서로 맞물려 도는 두 톱니바퀴 $$수식$$A`,` B$$/수식$$에 대하여 " \
           "$$수식$$A$$/수식$$의 톱니의 수는 $$수식$${num1}$$/수식$$개, $$수식$$B$$/수식$$의 톱니의 수는 $$수식$${num2}$$/수식$$개이다. " \
           "두 톱니바퀴가 회전하기 시작하여 처음으로 " \
           "다시 같은 톱니에서 맞물릴 때가지 톱니바퀴 $$수식$$A$$/수식$$는" \
           "몇 바퀴를 회전해야 하는가?\n" \
           "① $$수식$${x1}$$/수식$$ 바퀴\n② $$수식$${x2}$$/수식$$ 바퀴\n③ $$수식$${x3}$$/수식$$ 바퀴 \n④ $$수식$${x4}$$/수식$$ 바퀴 \n⑤ $$수식$${x5}$$/수식$$ 바퀴 \n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "두 톱니바퀴가 회전하기 시작하여 처음으로 다시\n" \
              "같이 톱니에서 맞물릴 때까지 돌아간 톱니의 수는\n" \
              "$$수식$${num1}$$/수식$$, $$수식$${num2}$$/수식$$의 최소공배수이므로 $$수식$${lcm1}$$/수식$$개이다.\n" \
              "따라서 두 톱니바퀴가 회전하기 시작하여 처음으\n" \
              "로 다시 같은 톱니에서 맞물릴 때까지 톱니바퀴\n" \
              "$$수식$$A$$/수식$$ 는 $$수식$${eq}$$/수식$$  (바퀴)를 회전해야 한다.\n" \


    num1 =np.random.randint(10, 50)
    num2 =np.random.randint(10, 50)
    while num1==num2 or gcd(num1,num2)==1:
        num1 = np.random.randint(10, 50)
        num2 = np.random.randint(10, 50)
    p = lcm(num1, num2)

    while p <2 or p>100:
        num1 = np.random.randint(10, 50)
        num2 = np.random.randint(10, 50)
        while num1 == num2:
            num2 = np.random.randint(10, 50)
        p = lcm(num1, num2)
    if num1 > num2:
        b = num1
        num1 = num2
        num2 = b
    answ = int(p/num1)
    eq = "$$수식$${"+str(p)+"} DIV {"+str(num1)+"} `=` {"+str(answ)+"}$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
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

    stem = stem.format(num1=num1, num2=num2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num1=num1, num2=num2, eq=eq, lcm1=p)

    return stem, answer, comment



# 중1-1-1-92
def naturalnum111_Stem_070():
    stem = "{name1}는 $$수식$${day1}`$$/수식$$일을 일하고 하루를 쉬고,{name2}는 $$수식$${day2}$$/수식$$일을 " \
           "일하고 하루를 쉬는 아르바이트를 하고 있다. " \
           "두 사람이{w_day}에 함께 쉬었을 때, 그 다음에 처음으로 같이 쉬는 요일은?\n" \
           "① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "{name1}는 $$수식$${day1}$$/수식$$일을 일하고 하루를 쉬고,{name2}는 $$수식$${day2}$$/수식$$일을\n" \
              "일하고 하루를 쉬므로 두 사람은 $$수식$${eq1}$$/수식$$\n" \
              "즉 $$수식$${da1}$$/수식$$일, $$수식$${da2}$$/수식$$일에 하루를 쉰다.\n" \
              "따라서{name1}와{name2}가 그 다음에 처음으로 같이\n" \
              "쉬는 날 $$수식$${da1}$$/수식$${temp} $$수식$${da2}$$/수식$$의 최소공배수인 $$수식$${lcm1}$$/수식$$일 후이다.\n" \
              "이때 $$수식$${eq}$$/수식$$이므로 두 사람은 {w_day}로부터\n" \
              "$$수식$${remainder}$$/수식$$일 후인{answ}에 처음으로 같이 쉰다.\n" \


    nameList = ["경희", "민철이", "수진이", "철수","영대"]
    o = np.random.randint(0, 5)
    name1 = nameList[o]
    o1 = np.random.randint(0,5)
    name2 = nameList[o1]
    while o ==o1:
        o1 = np.random.randint(0, 5)
        name2 = nameList[o1]

    week = ["일요일","월요일", "화요일", "수요일", "목요일","금요일","토요일"]
    break_ = np.random.randint(0,7)
    w_day = week[break_]

    day1 = np.random.randint(3,10)
    day2 = np.random.randint(3,10)
    while day1 == day2:
        day2 = np.random.randint(3, 10)
    if day1 > day2:
        d = day1
        day1 = day2
        day2 = d
    da1 = day1+1
    da2 = day2+1
    temp = proc_jo(da1, 2)
    lcm1 = lcm(da1, da2)

    remainder = lcm1 % 7
    eq1 = "$$수식$${"+str(day1)+"}` +` 1$$/수식$$ , $$수식$${"+str(day2)+"} `+` 1,$$/수식$$"
    eq="$$수식$${"+str(lcm1)+"} `=` {"+str(int(lcm1 / 7))+"} TIMES` 7 `$$/수식$$+ $$수식$${"+str(remainder)+"}$$/수식$$"
    n = (break_+remainder) % 7
    answ = week[n]
    bb=[]
    cc=[]
    while len(bb) < 4:
        k = np.random.randint(0, 7)
        if k not in cc and k != n:
            cc.append(k)
            bb.append(week[k])
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

    stem = stem.format(name1=name1, name2=name2, day1=day1, day2=day2, w_day=w_day, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq1=eq1, name1=name1, name2=name2, day1=day1, day2=day2, w_day=w_day, eq=eq, answ=answ,
                                 remainder=remainder, lcm1=lcm1, da1=da1, da2=da2,temp=temp)

    return stem, answer, comment


# 중1-1-1-94
def naturalnum111_Stem_071():
    stem = "톱니의 개수가 각각 $$수식$${num1}$$/수식$$, $$수식$${num2}$$/수식$$, $$수식$${num3}$$/수식$$인 세 톱니바퀴 " \
           "$$수식$$A,` B,` C$$/수식$$ 가 서로 맞물려 돌아가고 있다." \
           "세 톱니바퀴가 회전하기 시작하여 처음으로 다시 같은 톱니에서 동시에 맞물리는 것은 " \
           "톱니바퀴 $$수식$$B$$/수식$$가 몇 바퀴 회전한 후인가?\n" \
           "① $$수식$${x1}$$/수식$$ 바퀴\n② $$수식$${x2}$$/수식$$ 바퀴\n③ $$수식$${x3}$$/수식$$ 바퀴 \n④ $$수식$${x4}$$/수식$$ 바퀴 \n⑤ $$수식$${x5}$$/수식$$ 바퀴 \n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "세 톱니바퀴가 처음으로 다시 같은 톱니에서 동시에 맞물릴 때까지\n" \
              "돌아간 톱니의 개수는 $$수식$${num1}$$/수식$$, $$수식$${num2}$$/수식$$, $$수식$${num3}$$/수식$$의 최소공배수이므로\n" \
              "$$수식$${lcm_eq}$$/수식$$\n" \
              "따라서 세 톱니바퀴가 처음으로 다시 같은 톱니에서\n" \
              "동시에 맞물리는 것은 톱니바퀴 $$수식$$B$$/수식$$가\n" \
              "$$수식$${eq}$$/수식$$(바퀴) 회전한 후이다.\n" \

    num1 = np.random.randint(10, 70)
    num2 = np.random.randint(10, 70)
    num3 =np.random.randint(10, 70)
    while num1== num2 or num1 == num3 or num2 ==num3 or gcd(gcd(num1,num2),num3)==1:
        num1 = np.random.randint(10, 70)
        num2 = np.random.randint(10, 70)
        num3 = np.random.randint(10, 70)

    lcm1 = lcm(lcm(num1, num2),num3)
    while lcm1 > 400 or lcm1 < 4:
        num1 = np.random.randint(10, 70)
        num2 = np.random.randint(10, 70)
        num3 = np.random.randint(10, 70)
        while num1 == num2 or num1 == num3 or num2 == num3:
            num2 = np.random.randint(10, 70)
            num3 = np.random.randint(10, 70)
        lcm1 = lcm(lcm(num1, num2), num3)
    lcm_eq = factor_equation(lcm1) + "  $$수식$$`=` {"+str(lcm1)+"}$$/수식$$"
    answ = int(lcm1/num2)
    eq = "$$수식$${"+str(lcm1)+"} DIV {"+str(num2)+"} `=` {"+str(answ)+"}$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
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


    stem = stem.format(num1=num1, num2=num2, num3=num3, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num1=num1, num2=num2, num3=num3, eq=eq, lcm_eq=lcm_eq)

    return stem, answer, comment



# 중1-1-1-95
def naturalnum111_Stem_072():
    stem = "가로, 세로의 길이가 각각 $$수식$${num1}``rm cm$$/수식$$, $$수식$${num2}``rm cm$$/수식$$인 직사각형 모양의 카드를 " \
           "일정한 방향으로 겹치지 않게 빈틈없이 붙여서 정사각형을 만들려고 한다. " \
           "다음 중 정사각형의 한 변의 길이가 될 수 있는 것은?\n" \
           "① $$수식$${x1} ``rm cm$$/수식$$\n② $$수식$${x2} ``rm cm$$/수식$$\n③ $$수식$${x3} ``rm cm$$/수식$$\n④ $$수식$${x4} ``rm cm$$/수식$$\n⑤ $$수식$${x5} ``rm cm$$/수식$$\n "

    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "정사각형의 한 변의 길이는 $$수식$${num1}$$/수식$${temp}$$수식$${num2}$$/수식$$의\n" \
              "공배수이어야 한다.\n" \
              "$$수식$${num1}$$/수식$${temp}$$수식$${num2}$$/수식$$의 최소공배수는\n" \
              "$$수식$${lcm_eq}$$/수식$$이므로\n" \
              "정사각형의 한 변의 길이가 될 수 있는 것은\n" \
              "$$수식$${lcm1}$$/수식$$의 배수인 $$수식$${lcm11}``rm cm$$/수식$$이다.\n" \

    num1 = np.random.randint(10, 50)
    num2 = np.random.randint(10, 50)
    while num1 == num2:
        num2 = np.random.randint(10, 50)
    lcm1 = lcm(num1, num2)
    while lcm1 > 150:
        num1 = np.random.randint(10, 50)
        num2 = np.random.randint(10, 50)
        while num1 == num2:
            num2 = np.random.randint(10, 50)
        lcm1 = lcm(num1, num2)

    lcm_eq = factor_equation(lcm1) + "  $$수식$$`=` {"+str(lcm1)+"}$$/수식$$"

    lcm11 = lcm1 * np.random.randint(1, 4)
    answ = lcm11
    u = int(lcm1 / num1)
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k!=1:
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
    temp = proc_jo(num1, 2)
    stem = stem.format(num1=num1, num2=num2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num1=num1, num2=num2, temp=temp,  lcm1=lcm1, lcm_eq=lcm_eq,lcm11=lcm11)

    return stem, answer, comment


# 중1-1-1-96
def naturalnum111_Stem_073():
    stem = "어느 중학교에서 운동회에 참가한  $$수식$$1 $$/수식$$학년 전체 학생을 " \
           "$$수식$${num1}$$/수식$$명씩 $$수식$${num2}$$/수식$$명씩, $$수식$${num3}$$/수식$$명씩 조를 짜면 항상 $$수식$${left}$$/수식$$명이 남는다고 한다. " \
           "운동회에 $$수식$${low}$$/수식$$보다 많고 $$수식$${high}$$/수식$$명보다 적은 학생이 참가하였을 때, " \
           "$$수식$${qe}$$/수식$$명씩 조를 짜면 남은 학생 수는?\n" \
           "① $$수식$${x1}$$/수식$$명\n② $$수식$${x2}$$/수식$$명\n③ $$수식$${x3}$$/수식$$명\n④ $$수식$${x4}$$/수식$$명\n⑤ $$수식$${x5}$$/수식$$명\n "

    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "운동회에 참가한 학생 수를 $$수식$$x$$/수식$$명이라 하면 $$수식$$x `- `{left}$$/수식$$는\n" \
              "$$수식$${num1}$$/수식$$, $$수식$${num2}$$/수식$$, $$수식$${num3}$$/수식$$의 공배수이다.\n" \
              "$$수식$${num1}$$/수식$$, $$수식$${num2}$$/수식$$, $$수식$${num3}$$/수식$$의 공배수는 $$수식$${lcm1}$$/수식$$이므로\n" \
              "$$수식$$x`-`{left} =`$$/수식$${list}\n" \
              "$$수식$$ ∴ x = $$/수식$${new_list}$$/수식$$\n" \
              "따라서 운동회에 참가한 학생 수는 $$수식$${total}$$/수식$$명이고\n" \
              "$$수식$${eq}$$/수식$$ 이므로 $$수식$${qe}$$/수식$$명씩 조를 짜면\n" \
              "남는 학생 수는 $$수식$${answ}$$/수식$$명이다.\n"

    low = 100 *np.random.randint(2, 10)
    high = low +100
    num1 = np.random.randint(3, 16)
    num2 = np.random.randint(3, 16)
    num3 = np.random.randint(3, 16)
    while num1== num2 or num2 == num3 or num1==num3:
        num2 = np.random.randint(3, 16)
        num3 = np.random.randint(3, 16)
    left = np.random.randint(2, 15)
    while left >= num1:
        left = np.random.randint(2, 15)
    lcm1 = lcm(lcm(num1, num2), num3)
    total=0
    while True:
        for i in range(1, 10000):
            if lcm1*i+left > low and lcm1*i+left < high:
                total = lcm1*i+left
                break
        if total!=0 and lcm1*(i-1)+left < low and lcm1*(i+1)+left > high:
            break
        num1 = np.random.randint(3, 16)
        num2 = np.random.randint(3, 16)
        num3 = np.random.randint(3, 16)
        while num1 == num2 or num2 == num3 or num1 == num3:
            num2 = np.random.randint(3, 16)
            num3 = np.random.randint(3, 16)
            lcm1 = lcm(lcm(num1, num2), num3)
        while left >= num1:
            left = np.random.randint(2, 15)

    r = [num1, num2, num3]
    r.sort()
    num1 = r[0]
    num2 = r[1]
    num3 = r[2]

    list=""
    new_list=""
    for i in range(1,4):
        list = list + "$$수식$${"+str(lcm1*i)+"} ` , `$$/수식$$ "
        new_list = new_list + "$$수식$${"+str(lcm1*i+left)+"} ` , `$$/수식$$"
    list = list + "$$수식$$CDOTS$$/수식$$"
    new_list = new_list + "$$수식$$CDOTS$$/수식$$"

    qe = np.random.randint(3, 16)
    while num1 == qe or num2 == qe or qe == num3:
        qe = np.random.randint(3, 16)
    answ = total%qe
    eq = "$$수식$${"+str(total)+"} `=` {"+str(qe)+"} TIMES {"+str(int(total/qe))+"} + {"+str(answ)+"}$$/수식$$"

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

    stem = stem.format(num1=num1, num2=num2, num3=num3, left=left, low=low, high=high, qe=qe, x1=x1, x2=x2, x3=x3,
                           x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, lcm1=lcm1, num1=num1, num2=num2, num3=num3, left=left, low=low, high=high, qe=qe, list=list,
                                 new_list=new_list, total=total, answ=answ)

    return stem, answer, comment



# 중1-1-1-97
def naturalnum111_Stem_074():
    stem = "총 $$수식$${distance}``rm {{km}}$$/수식$$ 의 거리를 걷는 국토 대장정에 참여한 {name1}와 {name2}는 " \
           "같은 지점에서 동시에 출발하여 같은 길을 걸었다. " \
           "{name1}는 하루에 $$수식$${first}``rm {{km}}$$/수식$$씩 , " \
           "{name2}는 하루에 $$수식$${second}``rm {{km}}$$/수식$$씩 걷고, 하루의 일정을 마친 지점마다 자신의 깃발을 꽂아 두었다. " \
           "두 사람이 국토 대장정을 마쳤을 때, 두 사람의 깃발이 함께 꽃힌 지점은 모두 몇 개인가?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "

    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "두 사람의 깃발이 함께 꽂힌 두 지점 사이의 간격은\n" \
              "$$수식$${first}$$/수식$${temp} $$수식$${second}$$/수식$$의 최소공배수이므로\n" \
              "$$수식$${lcm_eq}(rm km)$$/수식$$  \n" \
              "따라서 $$수식$${lcm1}``rm {{km}}$$/수식$$마다 깃발이 함께 꽂힌다.\n" \
              "총 거리가 $$수식$${distance}``rm {{km}}$$/수식$$이므로\n" \
              "$$수식$${eq}$$/수식$$\n" \
              "따라서 깃발이 함께 꽂힌 지점은 모두 $$수식$${answ}$$/수식$$이다.\n" \

    nameList = ["경희", "민철이", "수진이", "철수","영대","미영이","은혜"]
    o = np.random.randint(0, 7)
    name1 = nameList[o]
    o1 = np.random.randint(0,7)
    name2 = nameList[o1]
    while o ==o1:
        o1 = np.random.randint(0, 7)
        name2 = nameList[o1]

    num1 = np.random.randint(10, 40)
    num2 = np.random.randint(10, 40)
    while num1 == num2:
        num2 = np.random.randint(10, 40)
    lcm1 = lcm(num1, num2)
    while lcm1 > 100:
        num1 = np.random.randint(10, 40)
        num2 = np.random.randint(10, 40)
        while num1 == num2:
            num2 = np.random.randint(10, 40)
        lcm1 = lcm(num1, num2)
    temp = proc_jo(num1, 2)
    lcm_eq = factor_equation(lcm1) + "  $$수식$$`=` {" + str(lcm1) + "}$$/수식$$"

    answ = np.random.randint(2, 5)
    distance = lcm1*answ

    eq= "$$수식$$"+str(distance) + "DIV {" + str(lcm1) + "} `=` {" + str(answ) + "}$$/수식$$"

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

    stem = stem.format(name1=name1, name2=name2, distance=distance, first=num1, second=num2, x1=x1, x2=x2, x3=x3,
                       x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq=eq, lcm1=lcm1, first=num1, second=num2, lcm_eq=lcm_eq,
                             distance=distance, answ=answ, temp=temp)

    return stem, answer, comment




# 중1-1-1-98
def naturalnum111_Stem_075():
    stem = "서로 맞물려 도는 두 톱니바퀴 $$수식$$A, B$$/수식$$가 있다. $$수식$$A$$/수식$$의 톱니의 수는 $$수식$${num1}$$/수식$$개이고, " \
           "두 톱니바퀴가 회전하기 시작하여 처음으로 다시 같은 톱니에서 맞물리는 것은 $$수식$$A$$/수식$$가 $$수식$${turns}$$/수식$$바퀴를 돌고 난 후일 때, " \
           "$$수식$$B$$/수식$$의 톱니의 수는? (단, $$수식$$A$$/수식$$의 톱니의 수는 $$수식$$B$$/수식$$의 톱니의 수보다 많다.)\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "두 톱니바퀴가 처음으로 다시 같은 톱니에서 동시에\n" \
              "맞물릴 때가지 돌아간 톱니의 개수는\n" \
              "$$수식$${eq1}$$/수식$$이므로 두 톱니의 개수의\n" \
              "최소공배수는 $$수식$${lcm_eq}$$/수식$$이다.\n" \
              "따라서 $$수식$$B$$/수식$$의 톱니의 수는 $$수식$${eq2}$$/수식$$ 또는\n" \
              "$$수식$${lcm_eq}$$/수식$$이고 $$수식$$A$$/수식$$의 톱니의 수보다 적어야 하므로\n" \
              "$$수식$${answ_eq}$$/수식$$  이다.\n" \

    num1 = np.random.randint(10, 40)
    num2 = np.random.randint(10, 40)
    while num1 == num2 or gcd(num1,num2)==1:
        num1 = np.random.randint(10, 40)
        num2 = np.random.randint(10, 40)
    lcm1 = lcm(num1, num2)
    while lcm1 > 100:
        num1 = np.random.randint(10, 40)
        num2 = np.random.randint(10, 40)
        while num1 == num2:
            num2 = np.random.randint(10, 40)
        lcm1 = lcm(num1, num2)
    temp = proc_jo(num1, 2)
    lcm_eq = factor_equation(lcm1)
    if num2 > num1:
        b = num2
        num2 = num1
        num1 = b
    turns = int(lcm1/num1)

    eq1 = "$$수식$${"+str(num1)+"} TIMES {"+str(turns)+"} `=`$$/수식$$" + lcm_eq

    eq2 = factor_equation(num2)
    answ_eq = eq2 + "$$수식$$`=` {"+str(num2)+"}$$/수식$$"

    answ = num2

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

    stem = stem.format(num1=num1, turns=turns, x1=x1, x2=x2, x3=x3,
                       x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq1=eq1, eq2=eq2, lcm_eq=lcm_eq, answ_eq=answ_eq, )

    return stem, answer, comment



# 중1-1-1-99
def naturalnum111_Stem_076():
    stem = "{name1}는 $$수식$${high}$$/수식$$ 이하의 사탕을 갖고 있는데, 갖고있는 사탕을 " \
           "$$수식$${div1}$$/수식$$개씩 포장하면 $$수식$${remainder1}$$/수식$$개가 남고, $$수식$${div2}$$/수식$$개씩 포장하면 " \
           "$$수식$${remainder2}$$/수식$$가 남고, $$수식$${div3}$$/수식$$개씩 포장하면 $$수식$${remainder3}$$/수식$$개가 남는다고 한다. " \
           "이 사탕을 $$수식$${qe}$$/수식$$개씩 포장할 때, 남는 사탕의 개수는?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "$$수식$${div1}$$/수식$$개, $$수식$${div2}$$/수식$$개, $$수식$${div3}$$/수식$$개씩 포장하면 모두 $$수식$${patt}$$/수식$$개가 부족하므로\n" \
              "사탕 수를 $$수식$$x$$/수식$$라 하면 $$수식$$x `+ `{patt}$$/수식$${temp} $$수식$${div1}$$/수식$$, $$수식$${div2}$$/수식$$, $$수식$${div3}$$/수식$$의 공배수이다.\n" \
              "$$수식$${div1}$$/수식$$, $$수식$${div2}$$/수식$$, $$수식$${div3}$$/수식$$의 최소공배수는 $$수식$${lcm_eq}$$/수식$$이므로\n" \
              "$$수식$$x `+ `{patt}$$/수식$$ = $$수식$${list1}$$/수식$$\n" \
              "$$수식$$∴ x `=` $$/수식$${list2}\n" \
              "이때 사탕이 $$수식$${high}$$/수식$$개 이하이므로 사탕의 개수는 $$수식$${lcm1}$$/수식$$이고,\n" \
              "$$수식$${eq}$$/수식$$이므로 $$수식$${qe}$$/수식$$개씩 포장하면 $$수식$${answ}$$/수식$$개가 남는다.\n" \

    nameList = ["경희", "민철이", "수진이", "철수"]
    name1 = nameList[np.random.randint(0, 4)]
    div1 = np.random.randint(5, 20)
    div2 = np.random.randint(5, 20)
    div3 = np.random.randint(5, 20)
    while div1== div2 or div2 == div3 or div1==div3:
        div2 = np.random.randint(5, 20)
        div3 = np.random.randint(5, 20)

    patt = np.random.randint(1, 5)

    lcm1 =lcm(lcm(div1, div2),div3)
    while lcm1 > 200 or lcm1 < 55:
        div1 = np.random.randint(5, 20)
        div2 = np.random.randint(5, 20)
        div3 = np.random.randint(5, 20)
        while div1 == div2 or div2 == div3 or div1 == div3:
            div2 = np.random.randint(5, 20)
            div3 = np.random.randint(5, 20)
        lcm1 = lcm(lcm(div1, div2), div3)
    y = [div1, div2, div3]
    y.sort()
    div1 = y[0]
    div2 = y[1]
    div3 = y[2]
    high=0
    if lcm1 < 200 and lcm1 >= 100:
        high = 200
    elif lcm1 < 100 and lcm1 > 0:
        high = 100
    lcm_eq = factor_equation(lcm1) + "$$수식$$`=` {"+str(lcm1)+"}$$/수식$$"
    remainder1 = div1 - patt
    remainder2 = div2 - patt
    remainder3 = div3 - patt
    temp = proc_jo(patt, -1)
    list1=""
    list2=""
    for i in range(1, 4):
        list1 = list1 + "$$수식$${"+str(lcm1*i)+"}`,`$$/수식$$"
        list2 = list2 + "$$수식$${"+str(lcm1*i-patt)+"}`,`$$/수식$$"
    list1 = list1 + "  $$수식$$CDOTS$$/수식$$"
    list2 = list2 + "  $$수식$$CDOTS$$/수식$$"

    qe = np.random.randint(5, 20)
    while div1== qe or div2 == qe or qe==div3:
        qe = np.random.randint(5, 20)
    a = lcm1 - patt
    answ = a % qe
    t = int(a/qe)
    eq = "$$수식$${"+str(a)+"}$$/수식$$ = $$수식$${"+str(qe)+"} TIMES {"+str(t)+"}$$/수식$$ + $$수식$${"+str(answ)+"}$$/수식$$"

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


    stem = stem.format(qe=qe, name1= name1, high=high, div1=div1, remainder1=remainder1, div2=div2, remainder2=remainder2, div3=div3,
                       remainder3=remainder3, x1=x1, x2=x2, x3=x3,
                       x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(high=high, div1=div1, div2=div2, div3=div3, patt=patt, temp=temp, list1=list1, list2=list2, lcm_eq=lcm_eq, eq=eq, answ=answ, qe=qe, lcm1=a)

    return stem, answer, comment




# 중1-1-1-100
def naturalnum111_Stem_077():
    stem = "두 자연수 $$수식$${num1}$$/수식$$, $$수식$$A$$/수식$$의 최대공약수가 $$수식$${gcd1}$$/수식$$, 최대공배수가 " \
           "$$수식$${lcm1}$$/수식$$일 때, 자연수 $$수식$$A$$/수식$$의 값은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "$$수식$${num1} TIMES` A$$/수식$$ = $$수식$${eq}$$/수식$$이므로 $$수식$$A = {answ}$$/수식$$\n" \

    num1 = np.random.randint(20, 100)
    num2 = np.random.randint(20, 100)
    while num1 == num2:
        num2 = np.random.randint(20, 100)
    gcd1 = gcd(num1, num2)
    lcm1 = lcm(num1, num2)
    while lcm1 > 400 or gcd1 < 7:
        num1 = np.random.randint(20, 100)
        num2 = np.random.randint(20, 100)
        while num1 == num2:
            num2 = np.random.randint(20, 100)
        gcd1 = gcd(num1, num2)
        lcm1 = lcm(num1, num2)
    if num1 > num2:
        b = num1
        num1 = num2
        num2 = b
    eq = "$$수식$${"+str(gcd1)+"} TIMES {"+str(lcm1)+"}$$/수식$$"
    answ = num2
    bb=[]
    for i in range(2, 1000):
        if lcm(num1,(i*gcd1))!=lcm1 and int(answ/(i*gcd1))!= answ and int((i*gcd1)) not in bb :
            bb.append(int((i*gcd1)))
        if len(bb)==4:
            break
    while len(bb)<4:
        e = np.random.randint(3, 5)
        if answ*e != answ and answ*e not in bb:
            bb.append(answ*e)

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

    stem = stem.format(num1=num1, lcm1=lcm1, gcd1=gcd1, x1=x1, x2=x2, x3=x3,
                       x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num1=num1, eq=eq, answ=answ)

    return stem, answer, comment




# 중1-1-1-102
def naturalnum111_Stem_078():
    stem = "자연수 $$수식$$A$$/수식$$와 $$수식$${num}$$/수식$$의 최대공약수가 $$수식$${num_temp}$$/수식$${temp1} 되도록 하는 " \
           "두 자리 자연수 $$수식$$A$$/수식$$의 개수는?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "$$수식$${eq}$$/수식$$  이므로 $$수식$$A `= `{num_temp} TIMES`a $$/수식$$($$수식$$a$$/수식$$와 $$수식$${num1}$$/수식$${temp2} 서로소)라\n" \
              "하면 $$수식$$a$$/수식$$와 $$수식$${num1}$$/수식$${temp2} 서로소이므로\n" \
              "$$수식$$a = $$/수식$${list}\n" \
              " $$수식$$∴``A = $$/수식$${list2}\n" \
              "따라서 두 자리 자연수 $$수식$$A$$/수식$$는 $$수식$${ans_list}$$/수식$$\n의 $$수식$${answ}$$/수식$$개이다.\n" \

    fac = [3, 5, 7, 11, 13, 17]
    num1 = fac[np.random.randint(0, 6)]
    num_temp = np.random.randint(5, 20)
    while num_temp in fac:
        num_temp = np.random.randint(5, 20)
    num = num_temp*num1
    list1 =[]
    list=""
    list2 =""
    ans_list=""
    t =0
    for i in range(1, int(100/num_temp)+2):
        p = gcd(i, num1)
        if p==1 and t <1:
            list = list + "$$수식$${"+str(i)+"}$$/수식$$ , "
            list2 = list2 + "$$수식$${"+str(i*num_temp)+"}$$/수식$$ , "
            if i*num_temp > 9 and i*num_temp <100:
                list1.append(i*num_temp)
        if i*num_temp > 100:
            t+=1
    list = list + "  $$수식$$CDOTS$$/수식$$"
    list2 = list2 + "  $$수식$$CDOTS$$/수식$$"
    for i in range(len(list1)-1):
        ans_list = ans_list + "$$수식$${"+str(list1[i])+"}$$/수식$$ , "
    ans_list = ans_list + "$$수식$${" + str(list1[-1]) + "}$$/수식$$"

    answ = len(list1)
    eq = "$$수식$${"+str(num)+"}$$/수식$$   = $$수식$${"+str(num_temp)+"} TIMES {"+str(num1)+"}$$/수식$$"
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
    temp1 = proc_jo(num_temp, 0)
    temp2=proc_jo(num1,-1)
    stem = stem.format(num=num, num_temp=num_temp, temp1=temp1,x1 = x1, x2 = x2, x3 = x3,x4 = x4, x5 = x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num_temp=num_temp, eq=eq, num1=num1, num=num, ans_list=ans_list,list=list, list2=list2, answ=answ,
                             temp2=temp2)

    return stem, answer, comment



# 중1-1-1-103
def naturalnum111_Stem_079():
    stem = "두 자리 자연수 $$수식$$A,` B$$/수식$$의 최대공약수는 $$수식$${gcd1}$$/수식$$, 최대공배수는 " \
           "$$수식$${lcm1}$$/수식$$일때, $$수식$$A `+` B$$/수식$$의 값은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "$$수식$$A,` B`$$/수식$$의 최대공약수가 $$수식$${gcd1}$$/수식$$이므로\n" \
              "$$수식$$A `= `{gcd1} TIMES`a` , `B` = ` {gcd1} TIMES `b`$$/수식$$, ($$수식$$a`,` b$$/수식$$는 서로소, $$수식$$a `&lt;` b$$/수식$$)\n" \
              "라 하자.\n" \
              "이때, $$수식$$A`,` B`$$/수식$$의 최소공배수가 $$수식$${lcm1}$$/수식$$이므로\n" \
              "$$수식$${gcd1} TIMES a `TIMES`b$$/수식$$  = $$수식$${lcm1}$$/수식$$    ∴ $$수식$$ a `TIMES` b$$/수식$$  = $$수식$${ans11}$$/수식$$\n" \
              "$$수식$$`(i)`a` = `1, `b `=` {ans11}$$/수식$$  일 때, $$수식$$`A` =` {A1}$$/수식$$, $$수식$$B `= `{B1}$$/수식$$\n" \
              "{list}\n" \
              "이 때, $$수식$$A`, `B$$/수식$$는 두 자리 자연수이므로\n" \
              "$$수식$$A `= `{A}$$/수식$$, $$수식$$B `= `{B}$$/수식$$\n" \
              "∴ $$수식$$A `+ `B `= `{answ}$$/수식$$\n"


    num1 = np.random.randint(10, 100)
    num2 = np.random.randint(10, 100)
    while num1 == num2:
        num2 = np.random.randint(10, 100)
    gcd1 = gcd(num1, num2)
    lcm1 = lcm(num1, num2)
    d=[]
    fac = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for x in fac:
        for y in fac:
            if x!=y and x*y not in d:
                d.append(x*y)

    while lcm1 %gcd1 !=0 or gcd1 < 2 or lcm1 > 300:
        num1 = np.random.randint(10, 100)
        num2 = np.random.randint(10, 100)
        while num1 == num2:
            num2 = np.random.randint(10, 100)
        gcd1 = gcd(num1, num2)
        lcm1 = lcm(num1, num2)
    if num1 > num2:
        b = num1
        num1 = num2
        num2 = b
    ans11 = int(lcm1/gcd1)
    a1 = int(num1/gcd1)
    b1 = int(num2/gcd1)
    A = num1
    B = num2
    A1 = gcd1
    B1 = gcd1*ans11
    answ = A +B
    list=""
    if a1 == 1:
        list = ""
    else:
        list = "$$수식$$(ii)`a `=` {"+str(a1)+"}$$/수식$$, $$수식$$b `=`{"+str(b1)+"}$$/수식$$일 때, $$수식$$A `=` {"+str(A)+"}$$/수식$$, $$수식$$B `=` {"+str(B)+"}$$/수식$$"
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = answ + bb[0]
        x3 = abs(answ - bb[1])
        x4 = answ + bb[2]
        x5 = abs(bb[3] - answ)

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = answ + bb[0]
        x3 = abs(answ - bb[1])
        x4 = answ + bb[2]
        x5 = abs(bb[3] - answ)
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = answ + bb[0]
        x2 = abs(answ - bb[1])
        x4 = answ + bb[2]
        x5 = abs(bb[3] - answ)
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = answ + bb[0]
        x2 = abs(answ - bb[1])
        x3 = answ + bb[2]
        x5 = abs(bb[3] - answ)
    else:
        ans = "⑤"
        x5 = answ
        x1 = answ + bb[0]
        x2 = abs(answ - bb[1])
        x3 = answ + bb[2]
        x4 = abs(bb[3] - answ)

    stem = stem.format(gcd1=gcd1, lcm1=lcm1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(A=A, B=B,gcd1=gcd1, lcm1=lcm1, answ=answ, list=list, ans11=ans11, A1=A1, B1=B1)

    return stem, answer, comment



# 중1-1-1-104
def naturalnum111_Stem_080():
    stem = "두 자리 자연수 $$수식$$A, `B$$/수식$$의 최대공약수가 $$수식$${gcd1}$$/수식$$, 최대공배수가 $$수식$${lcm1}$$/수식$$이다. " \
           "다음 중 $$수식$$A, `B$$/수식$$가 될 수 없는 두 자연수는?\n" \
           "① $$수식$${x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n$$/수식$$"
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "(두 자연수 $$수식$$A, `B`$$/수식$$의 곱) = (최대공약수) $$수식$$TIMES$$/수식$$ (최소공배" \
              "수) = $$수식$${gcd1} TIMES {lcm1} `=` {mul}$$/수식$$\n" \
              "두 자연수 $$수식$${num1}$$/수식$$, $$수식$${num2}$$/수식$$에서 $$수식$${eq}$$/수식$$ 이므로\n" \
              "$$수식$${num1}$$/수식$${temp1} $$수식$${num2}$$/수식$$ {temp2}  $$수식$$ A,` B$$/수식$$가 될 수 없다.\n" \

    op =[]
    bb=[]
    num1 = np.random.randint(10, 300)
    num2 = np.random.randint(10, 300)
    while num1 == num2 or num1*num2>10000:
        num1 = np.random.randint(10, 300)
        num2 = np.random.randint(10, 300)
    lcm1 = lcm(num1, num2)
    gcd1 = gcd(num1, num2)

    while lcm1 < 200 or lcm1 > 600 or gcd1 < 10 or num1*num2>10000:
        num1 = np.random.randint(2, 300)
        num2 = np.random.randint(2, 300)
        while num1 == num2:
            num1 = np.random.randint(2, 300)
            num2 = np.random.randint(2, 300)
        lcm1 = lcm(num1, num2)
        gcd1 = gcd(num1, num2)

    if num1 > num2:
        b = num1
        num1 = num2
        num2 = b
    bb.append(str(num1)+ " $$수식$$`,`$$/수식$$ " + str(num2))
    op.append(num1)
    mul = lcm1*gcd1
    while True:
        num1 = np.random.randint(10, 300)
        num2 = np.random.randint(10, 300)
        while num1 == num2 or num1 * num2 > 10000:
            num1 = np.random.randint(10, 300)
            num2 = np.random.randint(10, 300)
        lcm1 = lcm(num1, num2)
        gcd1 = gcd(num1, num2)

        while lcm1 < 200 or lcm1 > 600 or gcd1 < 10 or num1 * num2 > 10000:
            num1 = np.random.randint(2, 300)
            num2 = np.random.randint(2, 300)
            while num1 == num2:
                num1 = np.random.randint(2, 300)
                num2 = np.random.randint(2, 300)
            lcm1 = lcm(num1, num2)
            gcd1 = gcd(num1, num2)

        if num1 > num2:
            b = num1
            num1 = num2
            num2 = b
        bb.append(str(num1) + " $$수식$$`,`$$/수식$$ " + str(num2))
        op.append(num1)
        mul = lcm1 * gcd1
        mmm = 0
        bb=[]
        while len(bb)<=4:
            num1 = np.random.randint(2, 300)
            while mul%num1!=0:
                num1 = np.random.randint(2, 300)
            num2 = int(mul/num1)
            if num1 > num2:
                e = num1
                num1 = num2
                num2= e
            if num1 not in op:
                bb.append("$$수식$${"+str(num1) + "} `,` {"+ str(num2) + "}$$/수식$$")
                op.append(num1)
            mmm+=1
            if mmm>=100:
                break
        if len(bb)>=4:
            break

    num1 = np.random.randint(2, 300)
    num2 = np.random.randint(2, 300)
    while num1 == num2 or num1*num2>10000:
        num1 = np.random.randint(2, 300)
        num2 = np.random.randint(2, 300)
    lcm2 = lcm(num1, num2)
    gcd2 = gcd(num1, num2)
    while lcm1 == lcm2 or gcd1==gcd2 or num1*num2>10000:
        num1 = np.random.randint(2, 300)
        num2 = np.random.randint(2, 300)
        while num1 == num2:
            num1 = np.random.randint(2, 300)
            num2 = np.random.randint(2, 300)
        lcm2 = lcm(num1, num2)
        gcd2 = gcd(num1, num2)
    if num1 > num2:
        b = num1
        num1 = num2
        num2 = b
    answ = "$$수식$${" + str(num1) + "} `,` {" + str(num2) + "}$$/수식$$"

    eq = "$$수식$${" + str(num1) + "} TIMES {" + str(num2) + "} `=` {" + str(num2*num1) + "}$$/수식$$"
    temp1 = proc_jo(num1, 2)
    temp2 = proc_jo(num2, -1)
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

    stem = stem.format(gcd1=gcd1, lcm1=lcm1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(num1=num1, num2=num2, ans=ans, temp1=temp1, temp2=temp2, mul=mul, gcd1=gcd1, lcm1=lcm1, answ=answ, eq=eq)

    return stem, answer, comment



# 중1-1-1-105
def naturalnum111_Stem_081():
    stem = "다음 조건을 모두 만족시키는 가장 작은 자연수" \
           "$$수식$$x$$/수식$$는?\n$$표$$" \
           "(가) $$수식$$x`$$/수식$$와 $$수식$${num1}$$/수식$$의 최대공약수는 $$수식$${gcd1}$$/수식$$이다.\n" \
           "(나) $$수식$$x`$$/수식$$와 $$수식$${num2}$$/수식$$의 최대공약수는  $$수식$${gcd2}$$/수식$$이다.\n" \
           "(다) $$수식$$x`$$/수식$$는 세 자리 자연수이다.\n" \
           "$$/표$$\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "

    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "조건 (가)에서 $$수식$${eq1}$$/수식$$  이므로\n" \
              "$$수식$$x `= `{gcd1} TIMES`a$$/수식$$  ($$수식$$a$$/수식$$는 $$수식$${num12}$$/수식$${temp} 서로소)    $$수식$$CDOTSCDOTS$$/수식$$ ㉠\n" \
              "조건 (나)에서 $$수식$${eq2}$$/수식$$  이므로\n"   \
              "$$수식$$x `= `{gcd2} TIMES`a$$/수식$$  ($$수식$$a$$/수식$$는 $$수식$${num12}$$/수식$${temp} 서로소)    $$수식$$CDOTSCDOTS$$/수식$$ ㉡\n" \
              "이때 $$수식$$x$$/수식$$가 ㉠, ㉡을 모두 만족시켜야 하므로 $$수식$$x$$/수식$$는\n" \
              "$$수식$${gcd1}$$/수식$${temp2}$$수식$${gcd2}$$/수식$$의 공배수이면서 $$수식$${num12}$$/수식$${temp}는 서로소이어야 한다.\n" \
              "$$수식$${gcd1}$$/수식$${temp2}$$수식$${gcd2}$$/수식$$의 최소공배수는 $$수식$${gcd_eq}$$/수식$$ 이므로\n" \
              "$$수식$$x `= `{gcd3} TIMES k$$/수식$$ ($$수식$$k$$/수식$$는 $$수식$${num12}$$/수식$${temp} 서로소)\n" \
              "따라서 조건 (다)를 만족시키는 가장 작은 자연수\n" \
              "$$수식$$x$$/수식$$는 " \
              "$$수식$${eq}$$/수식$$" \

    fac = [2, 3, 5, 7, 11]
    while True:
        answ = np.random.randint(100, 300)
        num12 = fac[np.random.randint(0, 5)]
        p = np.random.randint(2, 50)
        while num12 == p:
            p = np.random.randint(2, 50)
        num1 = num12 * p
        gcd1 = p
        o = np.random.randint(2, 20)
        num2 = num12 * o
        while num12 == o:
            o = np.random.randint(2, 50)
        gcd2 = o
        if gcd(num1, answ) == p and gcd(num2, answ) ==o:
            break
    gcd3 = lcm(gcd1, gcd2)


    gcd_eq = factor_equation(gcd3) + " $$수식$$`=` {"+str(gcd3)+"}$$/수식$$"
    k=0
    for i in range(1,100):
        if gcd(i, num12) ==1 and gcd3*i > 100:
            k =i
            break
    answ = k*gcd3
    eq1 = "$$수식$${"+str(num1)+"} `=` {"+str(gcd1)+"} TIMES {"+str(num12)+"}$$/수식$$"
    eq2 = "$$수식$${"+str(num2)+"} `=` {"+str(gcd2)+"} TIMES {"+str(num12)+"}$$/수식$$"
    eq = " {"+str(gcd3)+"} TIMES {"+str(k)+"} `=` {"+str(answ)+"}$$/수식$$"

    temp = proc_jo(num12, 2)
    temp2 = proc_jo(gcd1, 2)
    bb = []
    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 5)
        u = np.random.randint(0, 2)
        if u == 1:
            k = answ + k
        else:
            k = abs(answ - k)
        if k not in bb and k != answ and k>100:
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

    stem = stem.format(num1=num1, num2=num2, gcd1=gcd1, gcd2=gcd2, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(eq1=eq1, eq2=eq2, gcd1=gcd1, gcd2=gcd2, gcd3=gcd3, num12=num12, temp=temp, temp2=temp2, gcd_eq=gcd_eq,
                             eq=eq)

    return stem, answer, comment


# 중1-1-1-106
def naturalnum111_Stem_082():
    stem = "두 자리 자연수 $$수식$$A,` B$$/수식$$ 에 대하여 두 수의 곱이 $$수식$${mul}$$/수식$$이고 " \
           "최대공약수가 $$수식$${gcd1}$$/수식$$일 때, 두 수의 합은?\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "

    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "$$수식$$A,` B$$/수식$$의 최대공약수가 $$수식$${gcd1}$$/수식$$이므로\n" \
              "$$수식$$A `= `{gcd1} TIMES` a$$/수식$$, $$수식$$B `=` {gcd1} TIMES`b $$/수식$$  (단 $$수식$$a, `b$$/수식$$는 서로소)라 하면\n" \
              "두 수의 곱이 $$수식$${mul}$$/수식$$이므로\n" \
              "$$수식$$A`TIMES`B$$/수식$$  = $$수식$${gcd1}`TIMES`a`TIMES`{gcd1}`TIMES`b $$/수식$$  = $$수식$${mul}$$/수식$$에서  $$수식$$a`TIMES b `=`{ans11}$$/수식$$\n" \
              "$$수식$$∴ a `= `{ans11}$$/수식$$, $$수식$$ b` = `1$$/수식$$ 또는 $$수식$$a `=` {a}$$/수식$$, $$수식$$b `= `{b}$$/수식$$\n" \
              "그런데 $$수식$$A,` B$$/수식$$ 가 두 자리 자연수이므로\n" \
              "$$수식$$a `= `{a}$$/수식$$ , $$수식$$b `=` {b}$$/수식$$\n" \
              "따라서 $$수식$${eq1}$$/수식$$, $$수식$${eq2}$$/수식$$ 이므로\n" \
              "$$수식$$A `+` B `= `$$/수식$${ans_eq}\n" \

    num1 = np.random.randint(10, 100)
    num2 = np.random.randint(10, 100)
    while num1 == num2:
        num1 = np.random.randint(10, 100)
        num2 = np.random.randint(10, 100)
    mul = num1*num2
    gcd1 = gcd(num1, num2)
    ans11 = int(mul / (gcd1 ** 2))
    while gcd1 < 4 or ans11>100:
        num1 = np.random.randint(10, 100)
        num2 = np.random.randint(10, 100)
        while num1 == num2:
            num2 = np.random.randint(10, 100)
        mul = num1 * num2
        gcd1 = gcd(num1, num2)
        ans11 = int(mul/(gcd1**2))

    a = b= 0
    for i in range(2, mul):
        for j in range(2, mul):
            if i*j == ans11 and gcd(i,j)==1 and i!=j:
                a = i
                b = j
                break
        if a!=0 and b!=0:
            break
    if a != 0 and b != 0:
        list=""
    if a == b and a == 0:
        a = ans11
        b = 1
    eq1 =  "$$수식$${"+str(gcd1)+"} TIMES {"+str(a)+"} `=` {"+str(gcd1*a)+"}$$/수식$$"
    eq2 =  "$$수식$${"+str(gcd1)+"} TIMES {"+str(b)+"} `=` {"+str(gcd1*b)+"}$$/수식$$"
    answ = gcd1*a + gcd1*b
    ans_eq = "$$수식$${"+str(gcd1*a)+"} `+` {"+str(gcd1*b)+"} `=` {"+str(answ)+"}$$/수식$$"



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


    stem = stem.format(mul=mul, gcd1=gcd1,x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(a=a, b=b, eq1=eq1, eq2=eq2, gcd1=gcd1, mul=mul, ans11=ans11, ans_eq=ans_eq)

    return stem, answer, comment



# 중1-1-1-107
def naturalnum111_Stem_083():
    stem = "세 자연수 $$수식$$a, `b,` c$$/수식$$가 다음 조건을 모두 만족시킬때 " \
           "$$수식$$a `+` b `+` c$$/수식$$의 값은? (단,$$수식$$ a` &lt; `b` &lt;` c`$$/수식$$)\n" \
           "$$표$$(가) $$수식$$a,` b,` c`$$/수식$$의 최대공약수는 $$수식$${gcd1}$$/수식$$이다.\n" \
           "(나) $$수식$$a,` b`$$/수식$$의 최대공약수는 $$수식$${gcd2}$$/수식$$, 최소공배수는 $$수식$${lcm1}$$/수식$$이다.\n" \
           "(다) $$수식$$b, `c`$$/수식$$의 최대공약수는 $$수식$${gcd3}$$/수식$$, 최소공배수는 $$수식$${lcm2}$$/수식$$이다.\n" \
           "$$/표$$\n" \
           "① $$수식$${x1}$$/수식$$\n② $$수식$${x2}$$/수식$$\n③ $$수식$${x3}$$/수식$$\n④ $$수식$${x4}$$/수식$$\n⑤ $$수식$${x5}$$/수식$$\n "
    answer = "(답):\n{ans}"
    comment = "(해설)\n" \
              "$$수식$$a `=`{gcd1} TIMES`x$$/수식$$ ,  $$수식$$b`=`{lcm3} TIMES y, `c` = `{gcd3} TIMES`z$$/수식$$ 로 놓으면\n" \
              "(나)에 의하여 $$수식$${gcd1} TIMES$$/수식$$ ($$수식$$x`TIMES {num_temp} TIMES`y $$/수식$$ ) $$수식$$`=` {lcm1}$$/수식$$,  $$수식$$x`TIMES y`=`{first_num}$$/수식$$\n" \
              "(다)에 의하여 $$수식$${gcd3} TIMES$$/수식$$ ($$수식$${d} TIMES y`TIMES`z$$/수식$$ ) $$수식$$`=` {lcm2}$$/수식$$,  $$수식$$y`TIMES z`=`{second_num}$$/수식$$\n" \
              "이때 $$수식$$a  `&lt;` b `&lt; `c$$/수식$$ 이므로 $$수식$$x `= `{x}$$/수식$$, $$수식$$y`=`{y}$$/수식$$, $$수식$$z`=`{z}$$/수식$$\n" \
              "따라서  $$수식$$a`=`{a}$$/수식$$, $$수식$$b`=`{b}$$/수식$$, $$수식$$c`=`{c}$$/수식$$이므로\n" \
              "$$수식$$a` +` b` +` c `=`$$/수식$${eq}\n"

    num1 = np.random.randint(10, 100)
    num2 = np.random.randint(10, 100)
    num3 = np.random.randint(10, 100)
    while num1 == num2 or num2 == num3 or num1 == num3:
        num2 = np.random.randint(10, 100)
        num3 = np.random.randint(10, 100)
    r = [num1, num2, num3]
    r.sort()
    num1 = r[0]
    num2 = r[1]
    num3 = r[2]
    gcd1 = gcd(gcd(num1,num2), num3)
    gcd2 = gcd(num1, num2)
    gcd3 = gcd(num2, num3)
    lcm1 = lcm(num1, num2)
    lcm2 = lcm(num2, num3)
    while gcd1 < 3 or gcd2 < 3 or gcd3 < 3 or lcm1 > 300 or lcm2 > 300:
        num1 = np.random.randint(10, 100)
        num2 = np.random.randint(10, 100)
        num3 = np.random.randint(10, 100)
        while num1 == num2 or num2 == num3 or num1 == num3:
            num2 = np.random.randint(10, 100)
            num3 = np.random.randint(10, 100)
        r = [num1, num2, num3]
        r.sort()
        num1 = r[0]
        num2 = r[1]
        num3 = r[2]
        gcd1 = gcd(gcd(num1, num2), num3)
        gcd2 = gcd(num1, num2)
        gcd3 = gcd(num2, num3)
        lcm1 = lcm(num1, num2)
        lcm2 = lcm(num2, num3)
    lcm3 = lcm(gcd2, gcd3)
    num_temp = int(gcd3/gcd1)
    first_num = int(lcm1/gcd3)
    d = int(lcm3/gcd3)
    second_num = int(lcm2/(lcm3))
    a = num1
    b = num2
    c = num3
    x = int(num1/gcd1)
    y = int(num2/lcm3)
    z = int(num3/gcd3)
    answ = num1+num2+num3
    eq = "$$수식$${"+str(num1)+"} `+` {"+str(num2)+"} `+` {"+str(num3)+"} `=` {"+str(answ)+"}$$/수식$$"

    bb = []
    while len(bb) < 4:
        k = np.random.randint(1, 10)
        if k not in bb and k != answ:
            bb.append(k)
    rande = np.random.randint(1, 6)
    if rande == 1:
        ans = "①"
        x1 = answ
        x2 = answ + bb[0]
        x3 = abs(answ - bb[1])
        x4 = answ + bb[2]
        x5 = abs(bb[3] - answ)

    elif rande == 2:
        ans = "②"
        x2 = answ
        x1 = answ + bb[0]
        x3 = abs(answ - bb[1])
        x4 = answ + bb[2]
        x5 = abs(bb[3] - answ)
    elif rande == 3:
        ans = "③"
        x3 = answ
        x1 = answ + bb[0]
        x2 = abs(answ - bb[1])
        x4 = answ + bb[2]
        x5 = abs(bb[3] - answ)
    elif rande == 4:
        ans = "④"
        x4 = answ
        x1 = answ + bb[0]
        x2 = abs(answ - bb[1])
        x3 = answ + bb[2]
        x5 = abs(bb[3] - answ)
    else:
        ans = "⑤"
        x5 = answ
        x1 = answ + bb[0]
        x2 = abs(answ - bb[1])
        x3 = answ + bb[2]
        x4 = abs(bb[3] - answ)

    stem = stem.format(gcd2=gcd2, gcd3=gcd3, lcm1=lcm1, lcm2=lcm2, gcd1=gcd1, x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(ans=ans)
    comment = comment.format(d=d, num_temp=num_temp, lcm3=lcm3, gcd2=gcd2, gcd3=gcd3, lcm1=lcm1, lcm2=lcm2, gcd1=gcd1, a=a, b=b, c=c, x=x, y=y, z=z, first_num=first_num, second_num=second_num, eq=eq)

    return stem, answer, comment
