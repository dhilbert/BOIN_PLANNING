import numpy as np
import numpy as np
import random
import codecs
import os
import re
import math
from itertools import product
from fractions import Fraction
import itertools
import copy
import fractions
from random import randint

answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
}

answer_dict_kor = {
    0: "(ㄱ)",
    1: "(ㄴ)",
    2: "(ㄷ)",
    3: "(ㄹ)",
    4: "(ㅁ)"
}

answer_dict_ko = {
    0: "㈀",
    1: "㈁",
    2: "㈂",
    3: "㈃",
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
def divUpDown(up, down):
    g = gcd(up,down)
    return int(up // g), int(down // g)

def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

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
            
def cand_check(s_candidates):
    return len(set(s_candidates)) == len(s_candidates) #중복값이 있으면 True

def cand_shuffle(s_candidates, ans=np.nan):
    np.random.shuffle(s_candidates)
    correct_idx = 0
    if (np.isfinite(ans)):
        for idx, s_cand in enumerate(s_candidates):
            if s_cand == ans:
                correct_idx = idx
                break
    return s_candidates, correct_idx

def RoundCheck(Flist):
    for i in range(len(Flist)):
        if type(Flist[i]) == str:
            continue
        elif Flist[i] == int(Flist[i]):
            Flist[i] = int(Flist[i])
    return Flist

def Round(Flist, n):
    for i in range(len(Flist)):
        Flist[i] = round(Flist[i], n)
        if Flist[i] == int(Flist[i]):
            Flist[i] = int(Flist[i])
    return Flist

def pickPrime(n, c_list_len):
    list_prime_1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    list_prime = list_prime_1[:n]
    c_list = np.array([])
    while True:
        t0 = list_prime[np.random.randint(0, len(list_prime))]
        c_list = np.union1d(c_list, t0)
        if len(c_list) == c_list_len:
            break
    c_list = RoundCheck(list(c_list))
    np.random.shuffle(c_list)
    return c_list

def comment_gen(p):
    ans = []
    for i,j in enumerate(["(ㄱ)","(ㄴ)","(ㄷ)","(ㄹ)"]):
        if p[i]:
            ans.append(j)
    return ans

def answer_gen(n):
    if n == 0: return "①"
    elif n == 1 : return "②"
    elif n == 2: return "③"
    elif n == 3: return "④"
    elif n == 4: return "⑤"
    else: print("error : answer_gen")


def prime_number(number):
    if number!=1:
        for f in range(2,number):
            if number % f == 0:
                return False
    else:
        return False

    return True
def prime_number_list(number):
    integer_list = (x for x in range(2, number + 1))
    prime_numbers = []
    for num in integer_list:
        if prime_number(num):
            prime_numbers.append(num)
    return prime_numbers
def soinsoo(number):
    result={}
    prime_numbers = prime_number_list(number)
    for prime in prime_numbers:
        degree = 0
        while number % prime == 0:
            degree = degree + 1
            number = number // prime
        result[prime] = degree
        if number == 1:
            break
    return result
def non_integer(number):
    result = soinsoo(number)
    length = len(result)
    primes = list(result)
    for i in range(0,length):
        if(result[primes[i]] == 0):
            del result[primes[i]]
    length = len(result)
    primes = list(result)
    a=1
    for i in range(0,length):
        if result[primes[i]]%2==0:
            a=1
        else:
            a=0
    if a==1:
        return False
    elif a == 0:
        return True
def out_route(number):
    result = soinsoo(number)
    length = len(result)
    primes = list(result)
    for i in range(0,length):
        if(result[primes[i]] == 0):
            del result[primes[i]]
    length = len(result)
    primes = list(result)
    integer = 1
    cnt = 0
    for i in range(0,length):
        if(result[primes[i]]>=2):
            integer = integer * (primes[i]**(int(result[primes[i]]//2)))
        else:
            cnt = cnt+1
    if cnt!=0:
        if integer !=1:
            return int(integer)
        else:
            return 0
    else:
        return 0
def gcd (a, b):
    if b == 0:
        return a
    else :
        if a < b:
            a, b = b, a
        return gcd(b, a % b)

eq = '`=`'
ts = '`times`'
ps = '`+`'
ms = '`-`'
dd = '`div`'

## ===================== with 수식 tag ================
# 양끝에 수식 태그를 붙여주는 함수입니다.

class fraction:
    def __init__(self,numer,denom):
        self.numer = numer
        self.denom = denom
    def change(self,numer,denom):
        self.numer=numer
        self.denom=denom
    def reduct(self):
        a=Fraction(self.numer,self.denom)
        self.change(a.numerator,a.denominator)
    def print(self):
        return makefrac(self.numer,self.denom)

    def numer_factor_print(self):
        return factor_print(self.numer)

    def add(self, frac):
        c=Fraction(self.numer,self.denom)+Fraction(frac.numer,frac.denom)
        addfrac=fraction(c.numerator,c.denominator)
        return addfrac

def choice_nsq(n1,n2):
        number=random.randrage(n1,n2+1)
        while is_int(number**0.05)==True:
            number=random.randrage(n1,n2+1)
        return number

def addTag(content) :
    if isinstance(content, list) or isinstance(content, tuple):
        return [addTag(x) for x in content]
    else :
        return "$$수식$$" + str(content) + "$$/수식$$"

def addTable(content) :
        return "$$표$$$$셀$$" + str(content) + "$$/셀$$$$/표$$"

def makeroot(content):
    if isinstance(content, list) or isinstance(content, tuple):
        return [makeroot(x) for x in content]
    else :
        return "sqrt" + "{" +str(content) + "}"

def makefrac(str1,str2):
    return "".join(["{",str(str1),"}","OVER","{", str(str2),"}"])

def makefrac_good(str1,str2):
    if str1 == str2:
        return "1"
    elif str2 == "1" or str2 == int(1):
        return str(str1)
    else :
        return "".join(["{",str(str1),"}","OVER","{", str(str2),"}"]) 

def makefrac_reduct(str1,str2):
    temp=Fraction(str1,str2)
    return "".join(["{",str(temp.numerator),"}","OVER","{", str(temp.denominator),"}"])

def rootout(n):
    result=factor(n)
    out_root=1
    in_root=1
    for i in result:
        if i[1]%2==0:
            out_root=out_root* i[0]**(i[1]//2)
        else :
            out_root=out_root* i[0]**(i[1]//2)
            in_root=in_root*i[0]
    return [out_root,in_root]

def rootout_print(n):
    li=rootout(n)
    if li[1]!=1:
        if li[0] !=1:
            return "".join([str(li[0]),makeroot(li[1])])
        else:
            return makeroot(li[1])
    else:
        return str(li[0])

def factor(n): 
    result=[] 
    for i in [2,3,5,7,11,13,17]: 
        count=0 
        while n % i == 0: 
            count+=1 
            n=int(n/i) 
        if count!=0: 
            result.append([i, count])
        if n==1: break 
    return result

def factor_print(n):
    factor_list=factor(n)
    factor_list_print=[]

    for i in factor_list:
        if i[1] != 1:
            factor_list_print.append("{"+str(i[0])+"}"+"^"+"{"+str(i[1])+"}")
        else: 
            factor_list_print.append(str(i[0]))
    return " `TIMES` ".join(factor_list_print)

def is_int(x):
    if int(x)==x:
        return True
    else:
        False

def print_power(n,k):
    if k != 1:
        return "".join(["{",str(n),"}","^","{",str(k),"}"])
    else:
        return str(n)


def degit_of_num(n):
        want=n
        degit=0
        while(not is_int(want)):
            want=want*10
            degit=degit+1
        return degit

def bool_jo(num):
    if isinstance(num, int):
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

def getAllDivisors(num):  # 1과 자기 자신을 포함한 약수를 구한다.
    if num < 1:
        return 0
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor


def getMyDivisors(num):  # 1과 자기 자신을 뺀 약수를 구한다.
    if num < 1:
        return 0
    divisor = []
    for i in range(2, num):
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


def isSquare(n):
    return int(n ** 0.5) ** 2 == n


def removeOne(num):
    if num == 1:
        num = ''
    elif num == -1:
        num = '-'
    return num

# 랜덤 정수 생성 (0 제외 && -num이상 num이하로 제한)
# :param num: 랜덤 정수 범위의 최소/최댓값 [int]
def make_exclude0(num):
    while True:
        result=randint(-num, num) #0이 아니면
        if(abs(result)>0):
            return result

# 절대 0이 나올 수 없는 경우(ex: 분모)에 사용
# :param num: 랜덤 정수 범위의 최소/최댓값 [int]
def make_excludeunder1(num):
    while True:
        result=randint(-num, num)
        if(abs(result)>1): #-1,0,1이 아니면
            return result

# 제곱근 안에 들어갈 수 생성 (2, 3, 5, 6, 7)
# 기본 7까지 생성, max 값이 주어지면 그 값까지 생성
def make_sqrt(max = 7):
    sqrt_list = [2, 3, 5, 7, 11, 13]
    index = sqrt_list.index(max)
    return sqrt_list[randint(0, index)]

# 거듭제곱의 지수 생성 (0 또는 2로 고정)
# 밑은 1~3으로 제한 randint(1, 3)
def make_exponent():
    ex_list = [0, 2]
    return ex_list[randint(0, 1)]

# 은, 는
def make_post(num):
    string = str(num)
    if(string[len(string)-1] in ['0', '1', '3', '6', '7', '8']):
        return '은'
    else:
        return '는'

# 옳은/옳지 않은
make_cond = ['은', '지 않은']

# 수식 변환 함수
# parameter로 str(수식 문자열), name(정수 이름), start(시작 번호), end(끝 번호)가 주어짐
# :param str: 변환할 문자열
# :param name: 사용한 변수 이름 ex)N, R [int]
# :param start: 시작 번호 [int]
# :param end: 끝 번호 [int]
def conv(str, name, start, end):
    # formating을 위한 변환
    newstr = str.replace('{', 'left')
    newstr = newstr.replace('}', 'right')
    newstr = newstr.replace('left', '{left}')
    newstr = newstr.replace('right', '{right}')

    # 변수 변환
    for i in reversed(range(start, end+1)):
        val = '{name}{i}'.format(name=name, i=i)
        newstr = newstr.replace(val, '{'+val+'}')

    return newstr

# 해당 값 num에 대해 +-3의 오차로 무작위 값 생성해 리스트로 반환
# :param num: 해당 변수의 정답값 [int]
def make_choice(num):
    sel = list(range(num - 3, num + 4))
    #정답은 반드시 포함되어야 하므로 삭제 후 오답끼리 섞어 4개를 추출한 후 추가
    del sel[sel.index(num)]
    random.shuffle(sel)
    choice_list = sel[0:4]
    choice_list.append(num)
    #정렬
    choice_list.sort()
    return choice_list

# 해당 값 num에 대해 +-3의 오차로 0을 제외한 무작위 값 생성해 리스트로 반환
# :param num: 해당 변수의 정답값 [int]
def make_choice_exclude0(num):
    while True:
        sel = random.sample(range(num - 3, num + 4), 5)
        if(0 not in sel):
            break
    #정답은 반드시 포함되어야 하므로 삭제 후 오답끼리 섞어 4개를 추출한 후 추가
    if(num in sel):
        del sel[sel.index(num)]
    random.shuffle(sel)
    choice_list = sel[0:4]
    choice_list.append(num)
    #정렬
    choice_list.sort()
    return choice_list

# 해당 값 num에 대해 +-3의 오차로 양수인 무작위 값 생성해 리스트로 반환
# :param num: 해당 변수의 정답값 [int]
def make_choice_positive(num):
    sel = random.sample(range(0, num + 7), 5)
    #정답은 반드시 포함되어야 하므로 삭제 후 오답끼리 섞어 4개를 추출한 후 추가
    if(num in sel):
        del sel[sel.index(num)]
    random.shuffle(sel)
    choice_list = sel[0:4]
    choice_list.append(num)
    #정렬
    choice_list.sort()
    return choice_list

# 부호 변환
def conv_sign(str):
    if(str.find('-`-')!=-1):
        str = str.replace('-`-', '+`')
    if(str.find('--')!=-1):
        str = str.replace('--', '`+`')
    if(str.find('+`-')!=-1):
        str = str.replace('+`-', '-`')
    if(str.find('+-')!=-1):
        str = str.replace('+-', '`-`')
    if (str.find('-` {-') != -1):
        str = str.replace('-` {-', '+` {')
    if (str.find('+` {-') != -1):
        str = str.replace('+` {-', '-` {')
    if (str.find('-` {`-') != -1):
        str = str.replace('-` {`-', '+` {`')
    if (str.find('+` {`-') != -1):
        str = str.replace('+` {`-', '-` {`')
    if(str.find('{-')!=-1):
        str = str.replace('{-', '-{')
    return str

# 불필요한 0, 1 제거 변환
def remove_coef(str):
    if(str.find('`1 ')!=-1):
        str = str.replace('`1 ', '')
    if(str.find('`-1 ')!=-1):
        str = str.replace('`-1 ', '`-')
    if(str.find('over {1}')!=-1):
        str = str.replace('over {1}', '')
    if(str.find('over {-1}')!=-1):
        str = str.replace('over {-1}', '')
    if(str.find('`0`+')!=-1):
        str = str.replace('`0`+', '')
    if (str.find('`0 ') != -1):
        str = str.replace('`0 ', '`0 `TIMES`')
    if(str.find('`0`') != -1):
        str = str.replace('`0`', '`')
    return str

# 최종 변환 (부호 조정, 불필요한 계수 제거 위함)
def return_conv(str):
    str = remove_coef(str)
    str = conv_sign(str)
    str = remove_coef(str)
    return str

# 제곱근의 완전제곱을 밖으로 빼내는 함수
# sq_list[0]에는 계산된 정수가, sq_list[1]에는 제곱근이 남는다
def sqrt_calc(num):
    sq_list = [1, num]
    for i in range(10, 0, -1):
        if(sq_list[1]%(i**2)==0):
            sq_list[0]*=i
            sq_list[1]= int(sq_list[1]/(i**2))
    return sq_list

def large_or_small(n1, n2):
    ineq = ''
    if(n1 > n2):
        ineq = '&gt;'
    elif(n1 < n2):
        ineq = '&lt;'
    else:
        ineq = '='
    return ineq

# 임의의 3항 제곱근 계산식 생성
# 마지막 index는 sq를 반환
def make_form_sqrt(wrong = 0):
    f1 = conv('$$수식$$`N1 sqrt {N2} `-`N3 sqrt {N4} `+`N5 sqrt {N6}$$/수식$$', 'N', 1, 6)
    f2 = conv('$$수식$$`=`R2 sqrt {R1} `-`R3 sqrt {R1} `+`R4 sqrt {R1}$$/수식$$', 'R', 1, 4)
    f3 = conv('$$수식$$=`R5 sqrt {R6}$$/수식$$', 'R', 5, 6)

    while True:
        sq = make_sqrt()
        N1 = make_exclude0(5)
        N2 = sq * pow(randint(1, 3), 2)
        N3 = make_exclude0(5)
        N4 = sq * pow(randint(1, 3), 2)
        N5 = make_exclude0(5)
        N6 = sq * pow(randint(1, 3), 2)
        R1 = sq
        R2 = N1 * int(math.sqrt(N2 / sq))
        R3 = N3 * int(math.sqrt(N4 / sq))
        R4 = N5 * int(math.sqrt(N6 / sq))
        R5 = R2 - R3 + R4
        R6 = R1

        if(not (N2 == sq and N4 == sq and N6 == sq)):
            break

    if(wrong==0):
        W5 = R5
    else:
        W5 = R5 * make_excludeunder1(2)

    f1 = f1.format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, left=left, right=right)
    f2 = f2.format(R1=R1, R2=R2, R3=R3, R4=R4, left=left, right=right)

    if(R5==0):
        a3 = '$$수식$$=0$$/수식$$'
        a4 = f3.format(R5 = make_exclude0(2), R6=R6, left=left, right=right)
        return [f1,f2,a3,a4]

    # 정답
    a3 = f3.format(R5=R5, R6=R6, left=left, right=right)
    # 오답 (wrong!=0 이라면 정답)
    a4 = f3.format(R5=W5, R6=R6, left=left, right=right)

    return [f1, f2, a3, a4]

# 잉믜의 2항 분수 제곱근 계산식 생성
# 마지막 index는 sq를 반환
def make_form_sqrt_frac(wrong = 0):
    f1 = conv('$$수식$${N1} over {sqrt {N2}} `-` {N3} over {sqrt {N4}}$$/수식$$', 'N', 1, 4)
    f2 = conv('$$수식$$`=` {R1} over {`R2 sqrt {R3}} `-` {R4} over {`R5 sqrt {R3}}$$/수식$$', 'R', 1, 5)
    f3 = conv('$$수식$$=` {`R6 sqrt {R3}} over {R7} `-` {`R8 sqrt {R3}} over {R9}$$/수식$$', 'R', 3, 9)
    f4 = conv('$$수식$$`=` {`R11 sqrt {R10}} over {R12}$$/수식$$', 'R', 10, 12)

    sq = make_sqrt()
    N1 = make_exclude0(5)
    N2 = sq * pow(randint(1, 3), make_exponent())
    N3 = make_exclude0(5)
    N4 = sq * pow(randint(1, 3), make_exponent())
    R1 = N1
    R2 = int(math.sqrt(N2/sq))
    R3 = sq
    R4 = N3
    R5 = int(math.sqrt(N4/sq))
    R10=R3

    red1 = Fraction(R1, R2*R3)
    R6 = red1.numerator
    R7 = red1.denominator

    red2 = Fraction(R4, R3*R5)
    R8 = red2.numerator
    R9 = red2.denominator

    wnum = make_excludeunder1(2)
    red3 = Fraction(R6, R7) - Fraction(R8, R9)
    if(wrong==0):
        wred3 = red3
    else:
        wred3 = Fraction(R6*wnum, R7) - Fraction(R8, R9)

    R11 = red3.numerator
    R12 = red3.denominator
    W11 = wred3.numerator
    W12 = wred3.denominator

    f1 = f1.format(N1=N1, N2=N2, N3=N3, N4=N4, left=left, right=right)
    f2 = f2.format(R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, left=left, right=right)
    f3 = f3.format(R3=R3, R6=R6, R7=R7, R8=R8, R9=R9, left=left, right=right)

    if(R11==0):
        a4 = '$$수식$$=0$$/수식$$'
        a5 = f4.format(R11 = make_exclude0(2), R10=R10, R12=R12, left=left, right=right)
        return [f1, f2, f3, a4, a5]

    a4 = f4.format(R10=R10, R11=R11, R12=R12, left=left, right=right)
    # 오답
    a5 = f4.format(R10=R10, R11=W11, R12=W12, left=left, right=right)

    return [f1, f2, f3, a4, a5]
    
# 중괄호
left = "{"
right = "}"

##########################################################################################################
##########################################################################################################


def realnum311_Stem_304():
    stem = "$$수식$$x$$/수식$$가 {q1}의 제곱근일 때, $$수식$$x$$/수식$$와 {q1} 사이의 관계식으로 옳은 것은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$x$$/수식$$가 {q1}의 제곱근이므로\n" \
              "$$수식$$x^{{2}} `=` {q1}$$/수식$$ 또는 $$수식$$x `=` ± sqrt{{{q1}}}$$/수식$$\n\n"

    list_A2 = [2, 3, 4, 5, 6, 10, 15, 35]
    q1 = list_A2[np.random.randint(0, len(list_A2))]
    a1 = "$$수식$$x^{{2}} `=` " + str(q1) + "$$/수식$$"

    s_candidates = ["$$수식$$x `=` " + str(q1) + "$$/수식$$", "$$수식$$x^{{2}} `=` " + str(q1) + "$$/수식$$", "$$수식$$x^{{2}} `=` sqrt{{{" + str(q1) + "}}}$$/수식$$", "$$수식$$x `=` - sqrt{{{" + str(q1) + "}}}$$/수식$$", "$$수식$$x `=` " + str((q1 // 2)) + "$$/수식$$"]
    np.random.shuffle(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1)
    return stem, answer, comment


def realnum311_Stem_305():
    stem = "다음 중 제곱근이 없는 수를 모두 고르면? (정답 2개)\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}, {a2}\n"
    comment = "(해설)\n" \
              "음수의 제곱근은 없으므로 {a1}, {a2}이다.\n\n"

    q1 = np.random.randint(0, 5)
    q2 = np.random.randint(q1 + 1, q1 + 5)
    q3 = np.random.randint(q2 + 1, q2 + 5)
    q4 = np.random.randint(q3 + 1, q3 + 5)
    q5 = np.random.randint(q4 + 1, q4 + 5)


    a1 = -q2
    a2 = "$$수식$$(" + str(-q4) + ")^{{3}}$$/수식$$"

    s_candidates = [q1, a1, q3, a2, q5]
    np.random.shuffle(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx1 = idx
                break
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a2:
                correct_idx2 = idx
                break

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx1], a2=answer_dict[correct_idx2])
    comment = comment.format(a1=answer_dict[correct_idx1], a2=answer_dict[correct_idx2])
    return stem, answer, comment


def realnum311_Stem_306():
    stem = "다음 중 제곱근이 있는 수를 모두 고르면? (정답 2개)\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a2}, {a1}\n"
    comment = "(해설)\n" \
              "{a2} {q5}의 제곱근은 {q5}이다.\n"    \
              "{a1} {q2}의 제곱근은 $$수식$$sqrt{{{q2}}}$$/수식$$, $$수식$$- sqrt{{{q2}}}$$/수식$$이다.\n" \
              "따라서 제곱근이 있는 수는 {a2}, {a1}이다.\n\n"

    q1 = np.random.randint(1, 5)
    q2 = np.random.randint(q1, q1 + 7)
    q3 = np.random.randint(q2 + 1, q2 + 7)
    q4 = np.random.randint(q3 + 1, q3 + 7)
    q5 = 0

    a1 = q2
    a2 = q5

    s_candidates = [-q4, -q3, "$$수식$$(" + str(-q1) + ")^{{3}}$$/수식$$", q5, a1]
    #np.random.shuffle(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx1 = idx
                break
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a2:
                correct_idx2 = idx
                break

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx1], a2=answer_dict[correct_idx2])
    comment = comment.format(a1=answer_dict[correct_idx1], a2=answer_dict[correct_idx2], q2=q2, q5=q5)
    return stem, answer, comment


def realnum311_Stem_001():
    stem = "{q1}의 제곱근을 구하시오.\n"
    answer = "(답) {a1}, {a2}\n"
    comment = "(해설)\n" \
              "$$수식$$({a1})^{{2}} `=` {q1}$$/수식$$,$$수식$$({a2})^{{2}} `=` {q1}$$/수식$$이므로 {q1}의 제곱근은 {a1}, {a2}이다.\n\n"

    a1 = np.random.randint(2, 21)
    a2 = -a1
    q1 = np.square(a1)

    stem = stem.format(q1=q1)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(q1=q1, a1=a1, a2=a2)
    return stem, answer, comment


def realnum311_Stem_002():
    stem = "다음 중 '$$수식$$x$$/수식$$는 {q1}의 제곱근이다.'를 식으로 바르게 나타낸 것은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$x$$/수식$$를 제곱하면 {q1}. $$수식$$`THEREFORE` x^{{2}} `=` {q1}$$/수식$$\n\n"

    list_prime = [2, 3, 4, 5, 7, 11, 13, 17]
    t1 = list_prime[np.random.randint(len(list_prime))]
    t2 = t1
    while t2 == t1:
        t2 = list_prime[np.random.randint(len(list_prime))]
    q1 = t1 * t2

    a1 = "$$수식$$x^{{2}} `=` " + str(q1) + "$$/수식$$"

    s_candidates = ["$$수식$$x `=` " + str(q1) + "$$/수식$$", "$$수식$$x^{{2}} `=` " + str(q1) + "$$/수식$$", "$$수식$$x `=` sqrt{{{" + str(q1) + "}}}$$/수식$$", "$$수식$$x `=` - sqrt{{{" + str(q1) + "}}}$$/수식$$", "$$수식$$2x `=` " + str(q1) + "$$/수식$$"]
    np.random.shuffle(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1)
    return stem, answer, comment


def realnum311_Stem_003():
    stem = "$$수식$$x^{{2}} `=` {q1}$$/수식$$을 만족시키는 $$수식$$x$$/수식$$의 값을 모두 구하시오.\n"
    answer = "(답) {a1}, {a2}\n"
    comment = "(해설)\n" \
              "$$수식$$x^{{2}} `=` a ( a `GEQ` 0 )$$/수식$$을 만족시키는 $$수식$$x$$/수식$$은 $$수식$$a$$/수식$$의 제곱근이다.\n" \
              "따라서 {q1}의 제곱근은 {a1}, {a2}이다.\n\n"

    a1 = -1 * np.random.randint(2, 20)
    a2 = -a1
    q1 = np.square(a1)

    stem = stem.format(q1=q1)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(q1=q1, a1=a1, a2=a2)
    return stem, answer, comment


def realnum311_Stem_004():
    stem = "다음 괄호 안에 알맞은 수를 순서대로 써넣으시오.\n"  \
           "$$표$${q1}의 제곱근 \n $$수식$$RARROW`$$/수식$$ 제곱하여 (    )가 되는 수\n $$수식$$RARROW`$$/수식$$ $$수식$$x^{{2}} `=` $$/수식$$(    )를 만족시키는 $$수식$$x$$/수식$$의 값\n $$수식$$RARROW`$$/수식$$ (    )$$/표$$"
    answer = "(답) $$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$, ±$$수식$${a3}$$/수식$$\n"
    comment = "(해설)\n" \
              "{q1}의 제곱근 \n $$수식$$RARROW`$$/수식$$ 제곱하여 {q1}가 되는 수\n $$수식$$RARROW`$$/수식$$ $$수식$$x^{{2}} `=` {q1}$$/수식$$를 만족시키는 $$수식$$x$$/수식$$의 값\n $$수식$$RARROW` ±{c1}$$/수식$$\n\n"

    c1 = np.random.randint(2, 20)
    q1 = np.power(c1, 2)    
    a1 = q1
    a2 = q1
    a3 = c1

    stem = stem.format(q1=q1)
    answer = answer.format(a1=a1, a2=a2, a3=a3)
    comment = comment.format(q1=q1, c1=c1)
    return stem, answer, comment


def realnum311_Stem_005():
    stem = "{q1}의 제곱근을 $$수식$$a$$/수식$$, {q2}의 제곱근을 $$수식$$b$$/수식$$라 할 때, $$수식$$b^{{2}} `-` a^{{2}}$$/수식$$의 값은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a^{{2}} `=` {q1}$$/수식$$, $$수식$$b^{{2}} `=` {q2}$$/수식$$이므로\n" \
              "$$수식$$b^{{2}} `-` a^{{2}} `=` {c1}$$/수식$$이다.\n\n"

    q1 = np.random.randint(1, 20)
    q2 = q1
    while q1 == q2:
        q2 = np.random.randint(1, 20)
    c1 = q2 - q1

    a1 = c1

    t1 = [a1 - 4, a1 - 2, a1, a1 + 2, a1 + 4][np.random.randint(0, 5)]
    s_candidates = [t1 - 4, t1 - 2, t1, t1 + 2, t1 + 4]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1)
    return stem, answer, comment


def realnum311_Stem_006():
    stem = "{q1}의 제곱근을 $$수식$$a$$/수식$$, {q2}의 제곱근을 $$수식$$b$$/수식$$라 할 때, $$수식$${{ b^{{2}} }} over {{ a^{{2}} }}$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a^{{2}} `=` {q1}$$/수식$$, $$수식$$b^{{2}} `=` {q2}$$/수식$$이므로\n" \
              "$$수식$${{ b^{{2}} }} over {{ a^{{2}} }} `=` {c1}$$/수식$$\n\n"

    q1 = np.random.randint(2, 20)
    c1 = np.random.randint(2, 20)
    q2 = q1 * c1

    a1 = c1

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1)
    return stem, answer, comment


def realnum311_Stem_007():
    stem = "다음 중 그 값이 나머지 넷과 다른 하나는?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "{c1}, {c3}, {c4}, {c5} 은 $$수식$$±{c6}$$/수식$$이고,  {c2}는 $$수식$$sqrt{{{c7}}} `=` {c6}$$/수식$$이다.\n\n"

    c6 = np.random.randint(2, 20)
    c7 = np.square(c6)

    s_can = ["$$수식$$±$$/수식$$" + str(c6), "제곱근 " + str(c7), str(c7) + "의 제곱근", "제곱하여 " + str(c7) + "인 수", "$$수식$$x^{{2}} `=` $$/수식$$" + str(c7) + "를 만족시키는 $$수식$$x$$/수식$$의 값"]
    s_candidates = list((np.array(s_can)).copy())
    np.random.shuffle(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == s_can[0]:
                correct_idx1 = idx
            elif s_cand == s_can[1]:
                correct_idx2 = idx
            elif s_cand == s_can[2]:
                correct_idx3 = idx
            elif s_cand == s_can[3]:
                correct_idx4 = idx
            elif s_cand == s_can[4]:
                correct_idx5 = idx

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx2])
    comment = comment.format(c6=c6, c7=c7, c1=answer_dict[correct_idx1], c2=answer_dict[correct_idx2], c3=answer_dict[correct_idx3], c4=answer_dict[correct_idx4], c5=answer_dict[correct_idx5])
    return stem, answer, comment


def realnum311_Stem_008():
    stem = "다음 중 옳지 않은 것을 모두 고르면? (정답 2개)\n" \
           "① 제곱근 {c6}는 {c7}이다.\n" \
           "② -$$수식$$sqrt{{{c8}}}$$/수식$$은 {c8}의 제곱근이다.\n" \
           "③ 제곱하여 {c9}이 되는 수는 없다.\n" \
           "④ $$수식$${c10}^{{2}}$$/수식$$의 제곱근은 $$수식$$± {c16}$$/수식$$이다.\n" \
           "⑤ $$수식$${{ {c12} }} over {{ {c13} }}$$/수식$$의 제곱근은 2개이고, 두 제곱근의 합은 0이다.\n"
    answer = "(답) {a1}, {a2}\n"
    comment = "(해설)\n" \
              "{c1} $$수식$$sqrt{{ {c6} }} `=` {c7}$$/수식$$\n" \
              "{c2} {c8}의 제곱근은 $$수식$$± sqrt{{{c8}}}$$/수식$$이므로 -$$수식$$sqrt{{{c8}}}$$/수식$$은(는) {c8}의 제곱근이다.\n"   \
              "{c3} 제곱하여 {c9}이(가) 되는 수는 $$수식$$± sqrt{{{c9}}}$$/수식$$의 2개이다.\n" \
              "{c4} $$수식$${c10}^{{2}} `=` {c11}$$/수식$$의 제곱근은 $$수식$$± {c10}$$/수식$$이다.\n" \
              "{c5} $$수식$${{ {c12} }} over {{ {c13} }}$$/수식$$의 제곱근은 $$수식$$± {{ {c14} }} over {{ {c15} }}$$/수식$$의 2개이고, $$수식$${{ {c14} }} over {{ {c15} }} `+` ( -{{ {c14} }} over {{ {c15} }} ) `=` 0$$/수식$$이다.\n\n"

    list_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    list_prime_s = [2, 3, 5, 7]
    t1 = list_prime_s[np.random.randint(0, 4)]
    c7 = t1 / 10
    c6 = np.square(t1) / 100
    c8 = list_prime[np.random.randint(0, 10)]
    c9 = list_prime[np.random.randint(0, 10)] / 10
    c16 = np.random.randint(2, 8)
    c10 = np.square(c16)
    c11 = np.square(c10)
    c14 = list_prime[np.random.randint(0, 10)]
    c15 = c14
    while c15 == c14:
        c15 = list_prime[np.random.randint(0, 10)]
    c12 = np.square(c14)
    c13 = np.square(c15)

    stem = stem.format(c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c12=c12, c13=c13, c16=c16)
    answer = answer.format(a1=answer_dict[2], a2=answer_dict[3])
    comment = comment.format(c1=answer_dict[0], c2=answer_dict[1], c3=answer_dict[2], c4=answer_dict[3], c5=answer_dict[4], c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12, c13=c13, c14=c14, c15=c15)
    return stem, answer, comment


def realnum311_Stem_009():
    stem = "제곱근에 대한 설명으로 옳은 것을 보기에서 모두 고르시오.\n" \
           "$$표$$ ① 제곱근 $$수식$$sqrt{{{c1}}}$$/수식$$는 $$수식$$sqrt{{{c2}}}$$/수식$$이다.\n ② -$$수식$$sqrt{{ ( {{ {c3} over {c4} }})^{{2}} }}$$/수식$$의 제곱근은 없다.\n ③ $$수식$$0.{{DOT{c5}}}$$/수식$$의 제곱근은 $$수식$$±0.{{DOT{c6}}}$$/수식$$이다.\n ④ 음이 아닌 모든 수의 제곱근은 2개이다.$$/표$$\n"
    answer = "(답) ①, ③\n"
    comment = "(해설)\n" \
              "① $$수식$$sqrt{{{c1}}} `=` {c2}$$/수식$$이고, 제곱근 {c2}은 $$수식$$sqrt{{{c2}}}$$/수식$$이다.\n" \
              "② 음수의 제곱근은 없다.\n"   \
              "③ $$수식$$ 0.dots{c5}  `=` {{ {c5} }} over {{9}}$$/수식$$의 제곱근은 $$수식$$±{{ {c6} }} over {{3}}$$/수식$$이고, $$수식$$±0.{{DOT{c6}}} `=` ±{{ {c6} }} over {{9}}$$/수식$$이다.\n" \
              "④ 0의 제곱근은 0의 1개이다.\n" \
              "이상에서 옳은 것은 ①, ②이다.\n\n"

    list_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    list_prime_s = [2, 3]
    c2 = list_prime[np.random.randint(0, 10)]
    c1 = np.square(c2)
    c3 = list_prime[np.random.randint(0, 10)]
    c4 = c3
    while c4 == c3:
        c4 = list_prime[np.random.randint(0, 10)]
    c6 = list_prime_s[np.random.randint(0, 2)]
    c5 = np.square(c6)

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    answer = answer.format()
    comment = comment.format(c1=c1, c2=c2, c5=c5, c6=c6)
    return stem, answer, comment


def realnum311_Stem_010():
    stem = "$$수식$$sqrt{{ {q1} }}$$/수식$$의 음의 제곱근을 $$수식$$A$$/수식$$, $$수식$$sqrt{{ {q2} }}$$/수식$$의 양의 제곱근을 $$수식$$B$$/수식$$라 할 때, $$수식$${{ B }} over {{ A }}$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ {q1} }}$$/수식$$의 음의 제곱근은 {c1}이므로 $$수식$$A `=` {c1}$$/수식$$\n" \
              "$$수식$$sqrt{{ {q2} }}$$/수식$$의 양의 제곱근은 {c2}이므로 $$수식$$B `=` {c2}$$/수식$$\n" \
              "$$수식$$THEREFORE` {{ B }} over {{ A }} `=` {c3}$$/수식$$\n\n"
    q2 = 1000
    while q2 >= 1000:
        c1 = np.random.randint(2, 20) * -1
        c3 = np.random.randint(2, 10) * -1
        c2 = c1 * c3
        q1 = np.square(c1)
        q2 = np.square(c2)

    a1 = c3

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_011():
    stem = "제곱근 {q1}을 $$수식$$a$$/수식$$, $$수식$$sqrt{{ {q2} }}$$/수식$$의 양의 제곱근을 $$수식$$b$$/수식$$라 할 때, $$수식$$a `+` b$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "제곱근은 {q1}은 $$수식$$sqrt{{ {q1} }} `=` {c1}$$/수식$$, $$수식$$sqrt{{ {q2} }} `=` {c2}$$/수식$$의 양의 제곱근은 $$수식$$sqrt{{ {c2} }} `=` {c3}$$/수식$$\n" \
              "따라서 $$수식$$a `=` {c1}$$/수식$$, $$수식$$b `=` {c3}$$/수식$$이므로\n" \
              "$$수식$$a `+` b `=` {c1} `+` {c3} `=` {c4}$$/수식$$\n\n"
    q2 = 1000
    while q2 >= 1000:
        c1 = np.random.randint(2, 16)
        c3 = np.random.randint(2, 10)
        c2 = np.square(c3)
        q1 = np.square(c1)
        q2 = np.square(c2)

    c4 = c1 + c3
    a1 = c4

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment


def realnum311_Stem_012():
    stem = "제곱근 $$수식$${{ {q1} }} over {{ {q2} }}$$/수식$$을 $$수식$${{b}} over {{a}}$$/수식$$라 할 때, $$수식$$a `-` b$$/수식$$의 값은? (단, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$는 서로소인 자연수이다.)\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${{b}} over {{a}} `=` sqrt{{ {{ {q1} }} over {{ {q2} }} }} `=` {{ {c1} }} over {{ {c2} }}$$/수식$$이므로 $$수식$$a `=` {c2}$$/수식$$, $$수식$$b `=` {c1}$$/수식$$\n" \
              "$$수식$$THEREFORE` a `-` b `=` {c3}$$/수식$$\n\n"
    q2 = 1000
    while q2 >= 1000:
        list_prime = [2, 3, 5, 7, 11]
        c_list = np.array([])
        c_list_len = np.random.randint(2, 5)
        while True:
            t0 = list_prime[np.random.randint(0, len(list_prime))]
            c_list = np.union1d(c_list, t0)
            if len(c_list) == c_list_len:
                break
        c_list = RoundCheck(list(c_list))
        np.random.shuffle(c_list)

        c1 = 1
        c2 = 1        
        for i, c in enumerate(c_list):
            if (i % 2) == 0:
                c1 = c1 * c
            else:
                c2 = c2 * c
        if c1 > c2:
            c1, c2 = c2, c1
        
        c3 = c2 - c1
        q1 = np.square(c1)
        q2 = np.square(c2)

    a1 = c3  #답 

    diff = a1 // 2
    s_positive = 0
    cnt=0
    if a1==1:
        print("hello")
        s_candidates=[3,2,1,4,5]
    else:
        while s_positive - (2 * diff) <=0:
            s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
        s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
   
   
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_013():
    stem = "제곱근 $$수식$${{ {q1} }} over {{ {q2} }}$$/수식$$를 $$수식$${{b}} over {{a}}$$/수식$$라 할 때, $$수식$$ab$$/수식$$의 값을 구하시오. (단, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$는 서로소인 자연수이다.)\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${{b}} over {{a}} `=` sqrt{{ {{ {q1} }} over {{ {q2} }} }} `=` {{ {c1} }} over {{ {c2} }}$$/수식$$이므로 $$수식$$a `=` {c2}$$/수식$$, $$수식$$b `=` {c1}$$/수식$$\n" \
              "$$수식$$THEREFORE` ab `=` {c2} `times` {c1} `=` {c3}$$/수식$$\n\n"
    q2 = 1000
    while q2 >= 1000:
        list_prime = [2, 3, 5, 7, 11]
        c_list = np.array([])
        c_list_len = np.random.randint(2, 5)
        while True:
            t0 = list_prime[np.random.randint(0, len(list_prime))]
            c_list = np.union1d(c_list, t0)
            if len(c_list) == c_list_len:
                break
        c_list = RoundCheck(list(c_list))
        np.random.shuffle(c_list)

        c1 = 1
        c2 = 1        
        for i, c in enumerate(c_list):
            if (i % 2) == 0:
                c1 = c1 * c
            else:
                c2 = c2 * c
        
        c3 = c1 * c2
        q1 = np.square(c1)
        q2 = np.square(c2)

    a1 = c3

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_014():
    stem = "다음 중 옳은 것을 모두 고르면? (정답 2개)\n" \
           "① {s1}의 제곱근 $$수식$$`=` ±{s2}$$/수식$$\n" \
           "② {s3}의 제곱근 $$수식$$`=` ±{s4}$$/수식$$\n" \
           "③ {s5}의 제곱근 $$수식$$`=` ±{s6}$$/수식$$\n" \
           "④ $$수식$$sqrt{{ {s7} }}$$/수식$$의 제곱근 $$수식$$`=` ±{s8}$$/수식$$\n" \
           "⑤ $$수식$$sqrt{{ {s9} }}$$/수식$$의 제곱근 $$수식$$`=` ±{s10}$$/수식$$\n"
    answer = "(답) ③, ⑤\n"
    comment = "(해설)\n" \
              "①  $$수식$${s1}$$/수식$$의 제곱근 = ± $$수식$$sqrt{{ {s1} }}$$/수식$$\n" \
              "②  $$수식$${s3}$$/수식$$의 제곱근 = ± $$수식$$sqrt{{ {s3} }}$$/수식$$\n"   \
              "④ $$수식$$sqrt{{ {s7} }} `=` {s8}$$/수식$$의 제곱근  =  ±$$수식$$sqrt{{ {s8} }}$$/수식$$\n\n"

    c_list = set([])
    while len(c_list) < 2:
        c_list.add(np.random.randint(5, 200))
    s1, s3 = np.array(list(c_list))
    s2 = int(np.sqrt(s1)) - 2
    s4 = int(np.sqrt(s3)) - 2
    s6 = np.random.randint(2, 20)
    s5 = np.square(s6)
    s8 = np.random.randint(2, 6)
    s10 = s8
    s7 = np.square(s8)
    s9 = np.power(s8, 4)
    
    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10)
    answer = answer.format()
    comment = comment.format(s1=s1, s3=s3, s7=s7, s8=s8)
    return stem, answer, comment


def realnum311_Stem_015():
    stem = "다음은 각 수의 제곱근을 구한 것이다. 옳지 않은 것은?\n" \
           "① $$수식$${s1}$$/수식$$의 제곱근 $$수식$$`=` ±{s2}$$/수식$$\n" \
           "② $$수식$${s3}$$/수식$$의 제곱근 $$수식$$`=` ±{s4}$$/수식$$\n" \
           "③ $$수식$${s5}$$/수식$$의 제곱근 $$수식$$`=` ±{s6}$$/수식$$\n" \
           "④ $$수식$$sqrt{{ {s7} }}$$/수식$$의 제곱근 $$수식$$`=` ±{s8}$$/수식$$\n" \
           "⑤ $$수식$$sqrt{{ {s9} }}$$/수식$$의 제곱근 $$수식$$`=` ±{s10}$$/수식$$\n"
    answer = "(답) ②\n"
    comment = "(해설)\n" \
              "② $$수식$${s3}$$/수식$$의 제곱근 = ±$$수식$$sqrt{{ {s3} }}$$/수식$$\n\n"

    c_list = set([])
    while len(c_list) < 2:
        c_list.add(np.random.randint(5, 20))
    s2, s6 = np.array(list(c_list))
    s1 = np.power(s2, 2)
    s5 = np.power(s6, 2)

    s3 = np.random.randint(2, 20)
    s4 = int(s3 % 2) + 1

    s8, s10 = pickPrime(5, 2)
    s7 = np.power(s8, 4)
    s9 = np.power(s10, 4)
    
    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10)
    answer = answer.format()
    comment = comment.format(s3=s3)
    return stem, answer, comment

def realnum311_Stem_016():
    stem = "$$수식$${q1}.DOT{{ {q2} }}$$/수식$$의 음의 제곱근은?\n" \
           "① $$수식$$-{{ {c3} }} over {{9}}$$/수식$$\n" \
           "② $$수식$$-{{ {c4} }} over {{3}}$$/수식$$\n" \
           "③ $$수식$$-{{ {c4} }} over {{9}}$$/수식$$\n" \
           "④ $$수식$${{ {c4} }} over {{9}}$$/수식$$\n" \
           "⑤ $$수식$${{ {c4} }} over {{3}}$$/수식$$\n"
    answer = "(답) ②\n"
    comment = "(해설)\n" \
              "$$수식$${q1}.DOT{{ {q2} }} `=` {{ {c1} `-` {c2} }} over {{9}} `=` {{ {c3} }} over {{9}}$$/수식$$이므로 $$수식$${q1}.DOT{{ {q2} }}$$/수식$$의 음의 제곱근은\n" \
              "-$$수식$$sqrt{{ {{ {c3} }} over {{9}} }} `=` - {{ {c4} }} over {{ 3 }}$$/수식$$\n\n"
    c1 = 10
    q1 = 2
    while (c1 // 10) != q1:
        c4 = np.random.randint(2, 33)
        if c4 % 3 == 0:
            c4 += 1
        c3 = np.power(c4, 2)
        t0 = -10
        while t0 < 10:
            if (c1 // 10) != q1:
                q1 = c3 // 10 + t0
                c2 = q1
                c1 = c3 + c2
                q2 = c1 % 10
            t0 += 1
    
    
    stem = stem.format(q1=q1, q2=q2, c3=c3, c4=c4)
    answer = answer.format()
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment

def realnum311_Stem_017():
    stem = "$$수식$${q1}.DOT{{ {q2} }}$$/수식$$의 양의 제곱근을 $$수식$$A$$/수식$$라 할 때, $$수식$${q3}A$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${q1}.DOT{{ {q2} }} `=` {{ {c1} `-` {c2} }} over {{9}} `=` {{ {c3} }} over {{9}}$$/수식$$이므로 $$수식$${q1}.DOT{{ {q2} }}$$/수식$$의 양의 제곱근은 \n" \
              "$$수식$$A$$/수식$$ = $$수식$$sqrt{{ {{ {c3} }} over {{9}} }} `=` {{ {c4} }} over {{ 3 }}$$/수식$$\n"    \
              "$$수식$$THEREFORE` {q3}A `=` {q3} `times` {{ {c4} }} over {{ 3 }} `=` {c5}$$/수식$$"
    c1 = 10
    q1 = 2
    while (c1 // 10) != q1:
        c4 = np.random.randint(2, 33)
        if c4 % 3 == 0:
            c4 += 1
        c3 = np.power(c4, 2)
        t0 = -10
        while t0 < 10:
            if (c1 // 10) != q1:
                q1 = c3 // 10 + t0
                c2 = q1
                c1 = c3 + c2
                q2 = c1 % 10
            t0 += 1
    
    q3 = np.random.randint(1, 4) * 3
    c5 = q3 // 3 * c4
    a1 = c5
    
    stem = stem.format(q1=q1, q2=q2, q3=q3)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, q3=q3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_018():
    stem = "제곱근 {q1}을 $$수식$$A$$/수식$$, $$수식$$( - {{ {q2} }} over {{ {q3} }} )^{{2}}$$/수식$$의 음의 제곱근을 $$수식$$B$$/수식$$라 할 때, $$수식$$AB$$/수식$$의 값은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "제곱근 {q1}은 {c1}이므로 $$수식$$A `=` {c1}$$/수식$$\n" \
              "$$수식$$( - {{ {q2} }} over {{ {q3} }} )^{{2}} `=` {{ {c2} }} over {{ {c3} }}$$/수식$$의 음의 제곱근은 $$수식$$ - {{ {q2} }} over {{ {q3} }}$$/수식$$이므로\n" \
              "$$수식$$B `=` - {{ {q2} }} over {{ {q3} }}$$/수식$$\n" \
              "$$수식$$THEREFORE` AB `=` {c4}$$/수식$$\n\n"
   
    q2, q3 = pickPrime(5, 2)
    c1 = q3 * np.random.randint(1, 3)
    q1 = np.power(c1, 2)
    c2 = np.power(q2, 2)
    c3 = np.power(q3, 2)
    c4 = -1 * c1 // q3 * q2

    a1 = c4

    diff = c4
    s_positive = 0
    while s_positive - (2 * diff) <= 0:
        s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1,q2=q2, q3=q3, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment


def realnum311_Stem_019():
    stem = "제곱근 {q1}을 $$수식$$A$$/수식$$, $$수식$$( - {{ {q2} }} over {{ {q3} }} )^{{2}}$$/수식$$의 음의 제곱근을 $$수식$$B$$/수식$$라 할 때, $$수식$$A `+` {q4}B$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "제곱근 {q1}은 {c1}이므로 $$수식$$A `=` {c1}$$/수식$$\n" \
              "$$수식$$( - {{ {q2} }} over {{ {q3} }} )^{{2}} `=` {{ {c2} }} over {{ {c3} }}$$/수식$$의 음의 제곱근은 $$수식$$- {{ {q2} }} over {{ {q3} }}$$/수식$$이므로\n" \
              "$$수식$$B `=` - {{ {q2} }} over {{ {q3} }}$$/수식$$\n" \
              "$$수식$$THEREFORE` A `+` {q4}B `=` {c4}$$/수식$$\n\n"
   
    c1, q2, q3 = pickPrime(5, 3)
    q4 = q3 * np.random.randint(1, 3)
    q1 = np.power(c1, 2)
    c2 = np.power(q2, 2)
    c3 = np.power(q3, 2)
    c4 = c1 + (-1 * q4 // q3 * q2)

    a1 = c4

    stem = stem.format(q1=q1,q2=q2, q3=q3, q4=q4)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment


def realnum311_Stem_020():
    stem = "{q1}의 두 제곱근을 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$라 할 때, 제곱근 $$수식$$sqrt{{ {q2}a `-` b }}$$/수식$$는? (단, $$수식$$a `&gt;` b$$/수식$$)\n" \
           "① $$수식$$sqrt{{ {ss1} }}$$/수식$$\n" \
           "② $$수식$$sqrt{{ {ss2} }}$$/수식$$\n" \
           "③ $$수식$$sqrt{{ {ss3} }}$$/수식$$\n" \
           "④ $$수식$$sqrt{{ {ss4} }}$$/수식$$\n" \
           "⑤ $$수식$$sqrt{{ {ss5} }}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a `=` {c1}$$/수식$$, $$수식$$b `=` -{c1}$$/수식$$ $$수식$$`( BECAUSE` a `&gt;` b )$$/수식$$이므로\n" \
              "$$수식$$sqrt{{ {q2}a `-` b }} `=` sqrt{{ {q2} `times` {c1} `-` ( - {c1} ) }}$$/수식$$\n" \
              "$$수식$$`=` sqrt{{ {c2} }} `=` {c3}$$/수식$$\n" \
              "따라서 제곱근 {c3}은 $$수식$$sqrt{{ {c3} }}$$/수식$$이다.\n\n"
    
    q1 = 3000
    while q1 >= 3000:
        t0 = pickPrime(10, 1)[0]
        t1 = pickPrime(10, 1)[0]
        if t0 < t1:
            t0, t1 = t1, t0
        if t0 == 1:
            t0 = 4
        c3 = t0 * t1
        c2 = np.power(c3, 2)
        c1 = c3 * t1
        q2 = t0 - 1
        q1 = np.power(c1, 2)
    
    a1 = c3

    diff = 1
    s_positive = 0
    while s_positive - (2 * diff) <= 0:
        s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1,q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_021():
    stem = "{q1}의 두 제곱근을 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$라 할 때, 제곱근 $$수식$$sqrt{{ {q2}a `-` {q3}b + {q4} }}$$/수식$$을 구하시오. (단, $$수식$$a `&gt;` b$$/수식$$)\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a `=` {c1}$$/수식$$, $$수식$$b `=` -{c1}$$/수식$$ ($$수식$$BECAUSE` a `&gt;` b$$/수식$$)이므로\n" \
              "$$수식$$sqrt{{ {q2}a `-` {q3}b + {q4} }} `=` sqrt{{ {q2} `times` {c1} `-` {q3} `times` ( - {c1} ) `+` {q4} }}$$/수식$$\n" \
              "$$수식$$`=` sqrt{{ {c2} }} `=` {c3}$$/수식$$\n" \
              "따라서 제곱근 {c3}은 $$수식$$sqrt{{ {c3} }}$$/수식$$이다.\n\n"
    
    q1 = 3000
    while q1 >= 3000:
        t0 = pickPrime(10, 1)[0]
        t1 = pickPrime(10, 1)[0]
        if t0 < t1:
            t0, t1 = t1, t0
        if t0 == 1:
            t0 = 4
        c3 = t0 * t1
        c1 = c3 * t1
        q2 = t0 - np.random.randint(1, t0)
        q3 = t0 - q2
        
        c3 = t0 * t1 + 1
        c2 = np.power(c3, 2)
        q4 = c2 - (t0 * c1)
        q1 = np.power(c1, 2)
    
    a1 = c3

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment

def realnum311_Stem_022():
    stem = "$$수식$$sqrt{{ {q1} }}$$/수식$$을 근호를 사용하지 않고 나타내시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${q1} `=` {c1}^{{2}}$$/수식$$이므로 $$수식$$sqrt{{ {q1} }}$$/수식$$를 근호를 사용하지 않고 나타내면 {c1}이다.\n\n"
    
    c1 = np.random.randint(2, 33)
    q1 = np.power(c1, 2)


    a1 = c1

    stem = stem.format(q1=q1)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, c1=c1)
    return stem, answer, comment


def realnum311_Stem_023():
    stem = "다음 중 근호를 사용하지 않고 나타낼 수 있는 수는?\n" \
           "① {c6}\n" \
           "② {c7}\n" \
           "③ {c3}\n" \
           "④ {c4}\n" \
           "⑤ {c5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "{a1} -$$수식$$sqrt{{ {{ {ss31} }} over {{ {ss32} }} }} $$/수식$$ =- $$수식$$ sqrt{{ ({{ {c1} }} over {{ {c2} }})^{{2}} }} `=` -{{ {c1} }} over {{ {c2} }}$$/수식$$\n\n"
    
    c1, c2 = pickPrime(10, 2)
    ss31 = np.power(c1, 2)
    ss32 = np.power(c2, 2)
    ss1 = np.power(np.random.randint(1, 20), 3)
    ss2 = np.power(np.random.randint(1, 20), 2) / 10
    ss4 = np.power(np.random.randint(1, 20), 3)
    t0, t1 = pickPrime(10, 2)
    ss5 = t0 * t1

    
    a1 = "$$수식$$-sqrt{{ {{" + str(ss31) + "}} over {{" + str(ss32) + "}} }}$$/수식$$"

    s_candidates = ["$$수식$$sqrt{{ {{1}} over" + str(ss1) + "}}$$/수식$$", "$$수식$$sqrt{{" + str(ss2) + "}}$$/수식$$", "$$수식$$-sqrt{{ {{" + str(ss31) + "}} over {{" + str(ss32) + "}} }}$$/수식$$", "$$수식$$sqrt{{" + str(ss4) + "}}$$/수식$$", "$$수식$$sqrt{{" + str(ss5) + "}}$$/수식$$"]
    np.random.shuffle(s_candidates)
    c6, c7, c3, c4, c5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(c6=c6, c7=c7, c3=c3, c4=c4, c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(a1=answer_dict[correct_idx], c1=c1, c2=c2, ss31=ss31, ss32=ss32)
    return stem, answer, comment


def realnum311_Stem_024():
    stem = "다음 중 제곱근을 근호를 사용하지 않고 나타낼 수 없는 것은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "① {c1}\n" \
              "② {c2}\n" \
              "③ {c3}\n" \
              "④ {c4}\n" \
              "⑤ {c5}\n\n"
    s3 = 5000
    s7 = 5000
    s10 = 5000
    s13 = 5000
    while max(s3, s7, s10, s13) >= 5000:
        t0 = np.random.randint(1,10)
        s2 = t0 / 10
        s1 = round(np.power(t0, 2) / 100, 2)

        s5 = np.random.randint(2, 10)
        s4 = np.power(s5, 2)
        s3 = np.power(s5, 4)

        s8, s9 = pickPrime(5, 2)
        s6 = np.power(s8, 2)
        s7 = np.power(s9, 2)

        s12 = np.random.randint(2, 10)
        s11 = np.power(s12, 2)
        s10 = np.power(s12, 4)

        s15 = s5
        while s15 == s5:
            s15 = np.random.randint(2, 10)
            s14 = np.power(s15, 2)
            s13 = np.power(s15, 4)
        
    s_candidates = ["$$수식$$sqrt{{ " + str(s1) + "}}$$/수식$$", "$$수식$$sqrt{{ {{ 1 }} over {{ " + str(s3) + "}} }}$$/수식$$", "$$수식$$ sqrt{{" + str(s6) + "}} over {{" + str(s7) + "}}$$/수식$$", "$$수식$$sqrt{{" + str(s10) + "}}$$/수식$$", "$$수식$$sqrt{{ {{ 1 }} over {{ " + str(s13) + "}} }}$$/수식$$"]
    s_answer = ["$$수식$$sqrt{{ " + str(s1) + "}} `=` " + str(s2) + "$$/수식$$의 제곱근은 ±$$수식$$sqrt{{" + str(s2) + "}}$$/수식$$", "$$수식$$sqrt{{ {{ 1 }} over {{ " + str(s3) + "}} }} `=` {{1}} over {{" + str(s4) + "}} $$/수식$$의 제곱근은 ±$$수식$$sqrt{{ {{1}} over {{" + str(s4) + "}} }} `=` ± {{ 1 }} over {{ " + str(s5) + "}} $$/수식$$", "±$$수식$$sqrt{{ {{" + str(s6) + "}} over {{" + str(s7) + "}} }}`=` ±{{" + str(s8) + "}} over {{" + str(s9) + "}}$$/수식$$", "$$수식$$sqrt{{" + str(s10) + "}} `=` " + str(s11) + "}}$$/수식$$의 제곱근은 ±$$수식$$sqrt{{" + str(s11) + "}} `=` ±" + str(s12) + "$$/수식$$", "$$수식$$sqrt{{ {{ 1 }} over {{ " + str(s13) + "}} }} `=` {{1}} over {{" + str(s14) + "}} $$/수식$$의 제곱근은 ±$$수식$$sqrt{{ {{1}} over {{" + str(s14) + "}} }} `=` ± {{ 1 }} over {{ " + str(s15) + "}} $$/수식$$"]

    s_shuf = np.arange(5)
    #np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    s_answer = np.array(s_answer)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    c1, c2, c3, c4, c5 = s_answer[s_shuf]
    correct_idx = np.where(s_shuf == 0)[0][0]

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_025():
    stem = "가로의 길이가 {q1}, 세로의 길이가 {q2}인 직사각형과 넓이가 같은 정사각형의 한 변의 길이는?\n" \
           "① $$수식$$sqrt{{ {ss1} }}$$/수식$$\n" \
           "② $$수식$$sqrt{{ {ss2} }}$$/수식$$\n" \
           "③ $$수식$$sqrt{{ {ss3} }}$$/수식$$\n" \
           "④ $$수식$$sqrt{{ {ss4} }}$$/수식$$\n" \
           "⑤ $$수식$$sqrt{{ {ss5} }}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "(직사각형의 넓이) $$수식$$`=` {q1} `times` {q2} `=` {c1}$$/수식$$\n" \
              "넓이가 {c1}인 정사각형의 한 변의 길이를 $$수식$$x$$/수식$$라 하면\n" \
              "$$수식$$x^{{2}} `=` {c1} `THEREFORE` x `=` sqrt{{ {c1} }} ( BECAUSE x `&gt;` 0 )$$/수식$$\n" \
              "따라서 구하는 정사각형의 한 변의 길이는 $$수식$$sqrt{{ {c1} }}$$/수식$$이다.\n\n"
    

    q1 = np.random.randint(2, 20)
    q2 = np.random.randint(2, 20)
    c1 = q1 * q2

    a1 = c1
    diff = 1
    s_positive = 0
    while s_positive - (2 * diff) <= 0:
        s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1)
    return stem, answer, comment


def realnum311_Stem_026():
    stem = "가로의 길이가 $$수식$${q1}`rm m$$/수식$$, 세로의 길이가 $$수식$${q2}`rm m$$/수식$$인 직사각형 모양의 텃밭과 넓이가 같은 정사각형 모양의 텃밭을 만들려고 할 때, 정사각형 모양의 한 변의 길이를 구하시오.\n"
    answer = "(답) $$수식$${a1} `rm m$$/수식$$\n"
    comment = "(해설)\n" \
              "직사각형 모양의 텃밭의 넓이는\n" \
              "$$수식$${q1} `times` {q2} `=` {c1} (rm m^{{2}})$$/수식$$\n" \
              "정사각형 모양의 텃밭의 한 변의 길이를 $$수식$$x`rm m`$$/수식$$라 하면\n" \
              "$$수식$$x^{{2}} `=` {c1} `THEREFORE` x `=` {c2} ( BECAUSE x `&gt;` 0 )$$/수식$$\n" \
              "따라서 정사각형 모양의 텃밭의 한 변의 길이는 $$수식$${c2}`rm m`$$/수식$$이다.\n\n"
    

    t1, t2 = np.random.choice(range(1, 17), 2, replace=False)
    q1 = np.power(t1, 2)
    q2 = np.power(t2, 2)
    c1 = q1 * q2
    c2 = t1 * t2

    a1 = c2

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2)
    return stem, answer, comment


def realnum311_Stem_027():
    stem = "근호를 사용하지 않고 나타낼 수 있는 것을 보기에서 모두 고르시오.\n" \
           "$$표$$(ㄱ) {ss1}\n (ㄴ) {ss2}\n (ㄷ) {ss3}\n (ㄹ) {ss4}\n $$/표$$\n\n"
    answer = "(답) {a1}, {a2}\n"
    comment = "(해설)\n" \
              "(ㄱ) {c1}\n" \
              "(ㄴ) {c2}\n" \
              "(ㄷ) {c3}\n" \
              "(ㄹ) {c4}\n" \
              "이상에서 근호를 사용하지 않고 나타낼 수 있는 것은 {a1}, {a2}이다.\n\n"
    
    s77 = np.random.randint(2, 20)
    s1 = np.power(s77, 2)

    s7 = np.random.randint(2, 20)
    s8 = np.random.randint(2, 20)
    s2 = np.power(s7, 2)
    s3 = np.power(s8, 2)
    
    t0, t1 = pickPrime(5, 2)
    s9 = t0 * t1
    s4 = 6 * s9

    list_A2 = [[2,3],[3,5],[4,5],[4,7],[5,7],[6,7],[7,8],[8,9],[10,11]]
    s5, s6 = list_A2[np.random.randint(0,len(list_A2))]
    s10 = np.power(s5, 2) + np.power(s6, 2)

    s_candidates = ["넓이가 $$수식$$" + str(s1) + " pi$$/수식$$인 원의 반지름의 길이", "넓이가 $$수식$$ {{" + str(s2) + "}} over {{" + str(s3) + "}}$$/수식$$인 정사각형의 넓이", "겉넓이가 " + str(s4) + "인 정육면체의 한 모서리의 길이", "직각을 낀 두 변의 길이가 각각 " + str(s5) + ", " + str(s6) + "인 직각삼각형의 빗변의 길이"]
    s_answer = ["원의 반지름의 길이를 r이라 하면\n $$수식$$ pi r^{{2}} `=` " + str(s1) + "pi$$/수식$$, $$수식$$r^{{2}} `=` " + str(s1) + "`THEREFORE` r `=`" + str(s77) + "( BECAUSE r `&gt;` 0 )$$/수식$$", "정사각형의 한 변의 길이를 $$수식$$x$$/수식$$라 하면\n $$수식$$x^{{2}} `=` {{" + str(s2) + "}} over {{" + str(s3) + "}} `THEREFORE` x `=` {{ " + str(s7) + "}} over {{" + str(s8) + "}} $$/수식$$", "정육면체의 한 변의 길이를 $$수식$$x$$/수식$$라 하면\n $$수식$$6x^{{2}} `=` " + str(s4) + "$$/수식$$, $$수식$$x^{{2}} `=` " + str(s9) + " `THEREFORE` x `=` sqrt{{ " + str(s9) + "}} ( BECAUSE x `&gt;` 0 )$$/수식$$", "$$수식$$sqrt{{" + str(s5) + "^{{2}} `+`" + str(s6) + "^{{2}} }} `=` sqrt{{" + str(s10) + "}}$$/수식$$\n"]

    s_shuf = np.arange(4)
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    s_answer = np.array(s_answer)
    ss1, ss2, ss3, ss4 = s_candidates[s_shuf]
    c1, c2, c3, c4 = s_answer[s_shuf]
    correct_idx1 = np.where(s_shuf == 0)[0][0]
    correct_idx2 = np.where(s_shuf == 1)[0][0]

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4)
    answer = answer.format(a1=answer_dict_kor[correct_idx1], a2=answer_dict_kor[correct_idx2])
    comment = comment.format(a1=answer_dict_kor[correct_idx1], a2=answer_dict_kor[correct_idx2], c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment


def realnum311_Stem_028():
    stem = "다음 중 옳지 않은 것을 모두 고르면? (정답 2개)\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}, {a2}\n"
    comment = "(해설)\n" \
              "{a1} $$수식$$sqrt{{ {{ {s4} }} over {{ {s5} }} }} `=` {tmp}$$/수식$$\n" \
              "{a2} $$수식$$sqrt{{ {s8} }} `=` {c1}$$/수식$$를 2배하면 $$수식$${c2} `=` sqrt{{ {c3} }}$$/수식$$\n\n"
    
    s2 = np.random.randint(2,8)
    s1 = np.power(s2, 4)

    s3 = -np.random.randint(2, 20)
    
    s6 = np.random.randint(2, 20)
    s7 = np.random.randint(2, 20)
    s4 = np.power(s6, 2)
    s5 = np.power(s7, 2)
    s11 = s6
    s12 = s7
    if gcd(s11,s12)!=1:
        s13,s14=divUpDown(s11,s12)
        if s14==1:
            tt="{%s}"%(s13)
            tmp="{%s}over {%s}`=`{%s}"%(s11,s12,s13)
        else :
            tt="{%s}over{%s}"%(s13,s14)
            tmp="{%s}over{%s}` = `{%s}over {%s}"%(s11,s12,s13,s14)
    else :
        tt="{%s}over{%s}"%(s11,s12)
        tmp="{%s}over {%s}"%(s11,s12)


    c1 = np.random.randint(2, 15)
    c2 = 2 * c1
    c3 = np.power(c2, 2)
    s8 = np.power(c1, 2)
    s9 = 2 * s8

    s10 = np.random.randint(21, 30) / 10
    
    s_candidates = ["$$수식$$sqrt{{" + str(s1) + "}}$$/수식$$의 제곱근은 $$수식$$±" + str(s2) + "$$/수식$$이다.", str(s3) + "의 제곱근은 없다.", "제곱근 $$수식$$ {{" + str(s4) + "}} over {{" + str(s5) + "}}$$/수식$$는 $$수식$$±{{" + str(tt) + "}}$$/수식$$이다.", "$$수식$$sqrt{{" + str(s8) + "}}$$/수식$$을 2배하면 $$수식$$sqrt {{" + str(s9) + "}}$$/수식$$이다.", "제곱하여 " + str(s10) + "가 되는 수는 2개이다."] 

    s_shuf = np.arange(5)
    correct_idx1 = 0
    correct_idx2 = 0
    while correct_idx1 >= correct_idx2:
        np.random.shuffle(s_shuf)
        s_candidates = np.array(s_candidates)
        ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
        correct_idx1 = np.where(s_shuf == 2)[0][0]
        correct_idx2 = np.where(s_shuf == 3)[0][0]

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, tt=tt,ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx1], a2=answer_dict[correct_idx2])
    comment = comment.format(tmp=tmp,a1=answer_dict[correct_idx1], a2=answer_dict[correct_idx2], s4=s4, s5=s5, s11=s11, s12=s12, s8=s8, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_029():
    stem = "$$수식$$ ( -{{ {q1} }} over {{ {q2} }} )^{{2}}$$/수식$$의 양의 제곱근을 $$수식$$A$$/수식$$, $$수식$${q3}.DOT{{ {q4} }}$$/수식$$의 음의 제곱근을 $$수식$$B$$/수식$$라 할 때, $$수식$$B `DIVIDE` A$$/수식$$의 값은? \n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$A `=` sqrt{{ ( -{{ {q1} }} over {{ {q2} }} )^{{2}} }} `=` {{ {q1} }} over {{ {q2} }}$$/수식$$\n" \
              "$$수식$$B `=` - sqrt{{ {q3}.DOT{{ {q4} }} }} `=` - sqrt{{ {{ {c3} }} over {{9}}   }} `=` - {{ {c4} }} over {{3}}$$/수식$$\n" \
              "$$수식$$THEREFORE` B `DIVIDE` A `=` - {{ {c4} }} over {{3}} `DIVIDE` {{ {q1} }} over {{ {q2} }} `=` - {{ {c4} }} over {{3}} `times` {{ {q2} }} over {{ {q1} }} `=` - {c5}$$/수식$$\n\n"
                  
    
    c1 = 10 
    q3 = 2
    while (c1 // 10) != q3:
        c4 = np.random.randint(2, 33)
        if c4 % 3 == 0:
            c4 += 1
        c3 = np.power(c4, 2)
        t0 = -10
        while t0 < 10:
            if (c1 // 10) != q3:
                q3 = c3 // 10 + t0
                c2 = q3
                c1 = c3 + c2
                q4 = c1 % 10
            t0 += 1

    q1 = c4
    q2 = 3 * np.random.randint(2, 15)
    
    c5 = q2 // 3
    
    a1 = - c5
    
    diff = 2
    
    s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_030():
    stem = "닮음비가 $$수식$${q1} `:` {q2}$$/수식$$인 두 원의 넓이의 합이 $$수식$${q3} `rm cm^{{2}}$$/수식$$일 때, 큰 원의 반지름의 길이는?\n" \
           "① $$수식$$sqrt{{ {ss1} }}$$/수식$$\n" \
           "② $$수식$$sqrt{{ {ss2} }}$$/수식$$\n" \
           "③ $$수식$$sqrt{{ {ss3} }}$$/수식$$\n" \
           "④ $$수식$$sqrt{{ {ss4} }}$$/수식$$\n" \
           "⑤ $$수식$$sqrt{{ {ss5} }}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "닮음비가 $$수식$${q1} `:` {q2}$$/수식$$이므로 두 원의 넓이의 비는\n" \
              "$$수식$${q1}^{{2}} `:` {q2}^{{2}} `=` {c1} `:` {c2}$$/수식$$\n" \
              "두 원의 넓이를 각각 $$수식$${c1}x `rm cm^{{2}}$$/수식$$, $$수식$${c2}x `rm cm^{{2}}$$/수식$$라 하면\n"   \
              "$$수식$${c1}x `+` {c2}x `=` {c3}pi$$/수식$$, $$수식$${c4}x `=` {c3}pi `THEREFORE` x `=` {c5}pi$$/수식$$\n"   \
              "따라서 큰 원의 넓이는 $$수식$${c2}x `=` {c6}pi (rm cm^{{2}})$$/수식$$이므로 큰 원의 반지름의 길이는 $$수식$$sqrt{{ {c6} }}`rm cm$$/수식$$이다."
                  
    q1, q2 = np.random.choice(np.arange(2, 15), 2, replace=False)
    if q1 > q2:
        q1, q2 = q2, q1
    c5 = np.random.randint(2, 15)
    c1 = np.power(q1, 2)
    c2 = np.power(q2, 2)
    c4 = c1 + c2
    q3 = c4 * c5
    c3 = q3
    c6 = c2 * c5
    
    a1 = c6
    
    diff = c1
    
    s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, q3=q3, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    return stem, answer, comment


def realnum311_Stem_031():
    stem = "다음 중 옳은 것은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "① {c1}\n" \
              "② {c2}\n" \
              "③ {c3}\n" \
              "④ {c4}\n" \
              "⑤ {c5}\n\n"
    
    s1, s2, s5, s6 = np.random.choice(np.arange(2, 30), 4, replace=True)
    s3 = np.random.randint(2, 10) / 10
    s4 = np.power(s5, 2)    

    s_candidates = ["$$수식$$-sqrt{{ ( {{ 1 }} over {{" + str(s1) + "}} )^{{2}} }} `=` {{ 1 }} over {{" + str(s1) + "}}$$/수식$$", "$$수식$$sqrt{{ ( -" + str(s2) + ")^{{2}} }} `=` - " + str(s2) + "$$/수식$$", "$$수식$$( - sqrt{{" + str(s3) + "}} )^{{2}} `=` -" + str(s3) + "$$/수식$$", "$$수식$$sqrt{{" + str(s4) + "^{{2}} }} `=`" + str(s5) + "$$/수식$$", "$$수식$$-sqrt{{ ( -" + str(s6) + ")^{{2}} }} `=` -" + str(s6) + "$$/수식$$"]
    s_answer = ["$$수식$$sqrt{{ ( {{ 1 }} over {{" + str(s1) + "}} )^{{2}} }} `=` {{ 1 }} over {{" + str(s1) + "}}$$/수식$$이므로 $$수식$$-sqrt{{ ( {{ 1 }} over {{" + str(s1) + "}} )^{{2}} }} `=` -{{ 1 }} over {{" + str(s1) + "}}$$/수식$$", "$$수식$$sqrt{{ ( -" + str(s2) + ")^{{2}} }} `=` " + str(s2) + "$$/수식$$", "$$수식$$( - sqrt{{" + str(s3) + "}} )^{{2}} `=` " + str(s3) + "$$/수식$$", "$$수식$$sqrt{{" + str(s4) + "^{{2}} }} `=`" + str(s4) + "$$/수식$$", "$$수식$$sqrt{{ ( -" + str(s6) + ")^{{2}} }} `=` " + str(s6) + "$$/수식$$이므로 $$수식$$-sqrt{{ ( -" + str(s6) + ")^{{2}} }} `=` -" + str(s6) + "$$/수식$$"]

    s_shuf = np.arange(5)
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    s_answer = np.array(s_answer)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    c1, c2, c3, c4, c5 = s_answer[s_shuf]
    correct_idx = np.where(s_shuf == 4)[0][0]

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_032():
    stem = "다음 중 옳지 않은 것은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "{a1} $$수식$$sqrt{{ ( -{{ {s0} }} over {{ {s1} }} )^{{2}} }} `=` {{ {s0} }} over {{ {s1} }}$$/수식$$\n\n"
    
    s0, s1 = pickPrime(10, 2) #np.random.choice(np.arange(2, 30), 2, replace=False)
    s2, s5, s6 = np.random.choice(np.arange(2, 30), 3, replace=True)
    s3 = np.random.randint(2, 10) / 10
    s4 = np.power(s5, 2)

    s_candidates = ["$$수식$$sqrt{{ ( -{{" + str(s0) + "}} over {{" + str(s1) + "}} )^{{2}} }} `=` -{{" + str(s0) + "}} over {{" + str(s1) + "}}$$/수식$$", "-$$수식$$sqrt{{ (- " + str(s2) + ")^{{2}} }} `=` - " + str(s2) + "$$/수식$$", "$$수식$$( sqrt{{" + str(s3) + "}} )^{{2}} `=` " + str(s3) + "$$/수식$$", "$$수식$$sqrt{{" + str(s4) + "^{{2}} }} `=`" + str(s4) + "$$/수식$$", "-(-$$수식$$sqrt{{ " + str(s6) + "}})^{{2}} `=` -" + str(s6) + "$$/수식$$"]
    s_answer = ["$$수식$$sqrt{{ ( -{{" + str(s0) + "}} over {{" + str(s1) + "}} )^{{2}} }} `=` {{" + str(s0) + "}} over {{" + str(s1) + "}}$$/수식$$"]

    s_shuf = np.arange(5)
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    s_answer = np.array(s_answer)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    correct_idx = np.where(s_shuf == 0)[0][0]

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(a1=answer_dict[correct_idx], s0=s0, s1=s1)
    return stem, answer, comment


def realnum311_Stem_033():
    stem = "다음 중 가장 작은 수는?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "① {c1}\n" \
              "② {c2}\n" \
              "③ {c3}\n" \
              "④ {c4}\n" \
              "⑤ {c5}\n\n"
    
    cc1, s2, s3, s4, s5 = np.random.choice(np.arange(2, 30), 5, replace=True)
    s1 = np.power(cc1, 2)
    cc2 = np.power(s2, 2)
       

    s_candidates = ["$$수식$$sqrt{{ {{1}} over {{ " + str(s1) + "}} }}$$/수식$$", "$$수식$$( {{1}} over {{ " + str(s2) + "}} )^{{2}}$$/수식$$", "$$수식$$sqrt{{ ( {{1}} over {{ " + str(s3) + "}} )^{{2}} }}$$/수식$$", "$$수식$$sqrt{{ ( - {{1}} over {{ " + str(s4) + "}} )^{{2}} }}$$/수식$$", "-$$수식$$ ( sqrt{{ {{1}} over {{ " + str(s5) + "}} }} )^{{2}}$$/수식$$"]
    s_answer = ["$$수식$$ {{1}} over {{" + str(cc1) + "}}$$/수식$$", "$$수식$$ {{1}} over {{" + str(cc2) + "}}$$/수식$$", "$$수식$$ {{1}} over {{" + str(s3) + "}}$$/수식$$", "$$수식$$ {{1}} over {{" + str(s4) + "}}$$/수식$$", "$$수식$$ {{1}} over {{" + str(s5) + "}}$$/수식$$"]

    s_shuf = np.arange(5)
    s_ans = np.array([cc1, cc2, s3, s4, s5])
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    s_answer = np.array(s_answer)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    c1, c2, c3, c4, c5 = s_answer[s_shuf]
    s_ans = s_ans[s_shuf]
    
    correct_idx = np.where(s_ans == np.amax(s_ans))[0][0]

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_034():
    stem = "다음 중 가장 큰 수는?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "① {c1}\n" \
              "② {c2}\n" \
              "③ {c3}\n" \
              "④ {c4}\n" \
              "⑤ {c5}\n\n"
    
    cc1, s2, s3, s4, s5 = np.random.choice(np.arange(2, 30), 5, replace=True)
    s1 = np.power(cc1, 2)
    cc2 = np.power(s2, 2)
       

    s_candidates = ["$$수식$$sqrt{{ {{1}} over {{ " + str(s1) + "}} }}$$/수식$$", "$$수식$$( {{1}} over {{ " + str(s2) + "}} )^{{2}}$$/수식$$", "$$수식$$sqrt{{ ( {{1}} over {{ " + str(s3) + "}} )^{{2}} }}$$/수식$$", "$$수식$$sqrt{{ ( - {{1}} over {{ " + str(s4) + "}} )^{{2}} }}$$/수식$$", "- ( -$$수식$$sqrt{{ {{1}} over {{ " + str(s5) + "}} }} )^{{2}}$$/수식$$"]
    s_answer = ["$$수식$$ {{1}} over {{" + str(cc1) + "}}$$/수식$$", "$$수식$$ {{1}} over {{" + str(cc2) + "}}$$/수식$$", "$$수식$$ {{1}} over {{" + str(s3) + "}}$$/수식$$", "$$수식$$ {{1}} over {{" + str(s4) + "}}$$/수식$$", "$$수식$$ - {{1}} over {{" + str(s5) + "}}$$/수식$$"]

    s_shuf = np.arange(5)
    s_ans = np.array([cc1, cc2, s3, s4, -s5 + 1000])
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    s_answer = np.array(s_answer)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    c1, c2, c3, c4, c5 = s_answer[s_shuf]
    s_ans = s_ans[s_shuf]
    
    correct_idx = np.where(s_ans == np.amin(s_ans))[0][0]

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_035():
    stem = "$$수식$$( - sqrt{{ {{ 1 }} over {{ {q1} }} }} )^{{2}}$$/수식$$의 제곱근은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$( - sqrt{{ {{ 1 }} over {{ {q1} }} }} )^{{2}} `=` {{1}} over {{ {q1} }}$$/수식$$의 제곱근은 $$수식$$±{{1}} over {{ {s2} }}$$/수식$$이다.\n\n"
    
    s2 = np.random.randint(2, 20)
    s1 = np.power(s2, 2)
    q1 = s1
       

    s_candidates = ["$$수식$${{ 1 }} over {{" + str(s1) + "}}$$/수식$$", "$$수식$$±{{ 1 }} over {{" + str(s1) + "}}$$/수식$$", "$$수식$${{ 1 }} over {{" + str(s2) + "}}$$/수식$$", "$$수식$$±{{ 1 }} over {{" + str(s2) + "}}$$/수식$$", "$$수식$$± sqrt{{ {{ 1 }} over {{" + str(s1) + "}} }} $$/수식$$"]

    s_shuf = np.arange(5)
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    
    correct_idx = np.where(s_shuf == 3)[0][0]

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, s2=s2)
    return stem, answer, comment


def realnum311_Stem_036():
    stem = "옳은 것을 보기에서 모두 고른 것은?\n" \
           "$$표$$(ㄱ) $$수식$$sqrt{{ ( - {s1} )^{{2}} }} `=` - {s1}$$/수식$$ (ㄴ)  -$$수식$$ sqrt{{ {s2} }} `=` - {s3}$$/수식$$\n (ㄷ) (-$$수식$$sqrt{{ {s4} }} )^{{2}} `=` {s4}$$/수식$$ (ㄹ) -$$수식$$sqrt{{ {s5} }} `=` {s6}$$/수식$$ $$/표$$\n" \
           "① (ㄱ), (ㄴ)\n" \
           "② (ㄱ), (ㄷ)\n" \
           "③ (ㄴ), (ㄹ)\n" \
           "④ (ㄱ), (ㄴ), (ㄷ)\n" \
           "⑤ (ㄱ), (ㄷ), (ㄹ)\n"
    answer = "(답) ④\n"
    comment = "(해설)\n" \
              "(ㄹ) -$$수식$$sqrt{{ {s5} }} `=` -{s6}$$/수식$$\n"   \
              "이상에서 옳은 것은 (ㄱ), (ㄴ), (ㄷ)이다."
    
    s1 = np.random.randint(2, 20)
    s3 = np.random.randint(2, 20)
    s2 = np.power(s3, 2)
    s4 = np.random.randint(2,20)
    s6 = np.random.randint(2, 20)
    s5 = np.power(s6, 2)

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6)
    answer = answer.format()
    comment = comment.format(s5=s5, s6=s6)
    return stem, answer, comment


def realnum311_Stem_037():
    stem = "$$수식$$ ( sqrt{{ {q1} }} )^{{2}}$$/수식$$의 음의 제곱근을 $$수식$$A$$/수식$$, $$수식$$sqrt{{ ( - {q2} )^{{2}} }}$$/수식$$의 양의 제곱근을 $$수식$$B$$/수식$$라 할 때, $$수식$$A^{{2}} - B$$/수식$$의 값은? \n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ ( sqrt{{ {q1} }} )^{{2}} `=` {q1}$$/수식$$의 음의 제곱근은 -$$수식$$sqrt{{ {q1} }}$$/수식$$이므로\n" \
              "$$수식$$A `=` - sqrt{{ {q1} }}$$/수식$$\n" \
              "$$수식$$sqrt{{ ( - {q2} )^{{2}} }} `=` {q2}$$/수식$$의 양의 제곱근은 $$수식$${c1}$$/수식$$이므로\n" \
              "$$수식$$B `=` {c1}$$/수식$$\n" \
              "$$수식$$THEREFORE` A^{{2}} `-` B `=` (- sqrt{{ {q1} }} )^{{2}} `-` {c1} `=` {q1} `-` {c1} `=` {c2}$$/수식$$\n\n"
                  
    x = np.array([0, 1, 4, 9, 16])
    y = np.array(range(20))
    z = np.setdiff1d(y, x)
    q1 = np.random.choice(z, 1)[0]
    c1 = np.random.randint(2,20)
    q2 = np.power(c1, 2)
    c2 = q1 - c1
       
    a1 = c2
    
    diff = 1
    
    s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2)
    return stem, answer, comment


def realnum311_Stem_038():
    stem = "$$수식$$ ( sqrt{{ {q1} }} )^{{2}}$$/수식$$의 양의 제곱근을 $$수식$$A$$/수식$$, $$수식$$sqrt{{ ( - {q2} )^{{2}} }}$$/수식$$의 음의 제곱근을 $$수식$$B$$/수식$$라 할 때, $$수식$$A - B$$/수식$$의 값은? \n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ ( sqrt{{ {q1} }} )^{{2}} `=` {q1}$$/수식$$의 양의 제곱근은 $$수식$${c1}$$/수식$$이므로\n" \
              "$$수식$$A `=` {c1}$$/수식$$\n" \
              "$$수식$$sqrt{{ ( - {q2} )^{{2}} }} `=` {q2}$$/수식$$의 음의 제곱근은 $$수식$$-{c2}$$/수식$$이므로\n" \
              "$$수식$$B `=` -{c2}$$/수식$$\n" \
              "$$수식$$THEREFORE` A `-` B `=` {c1} `-` ( -{c2} ) `=` {c3}$$/수식$$\n\n"
                  
    c1, c2 = np.random.choice(np.arange(2, 20), 2, replace=False)
    q1, q2 = np.power([c1, c2], 2)
    c3 = c1 + c2

    a1 = c3

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_039():
    stem = "다음 중 옳지 않은 것은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "① {c1}\n" \
              "② {c2}\n" \
              "③ {c3}\n" \
              "④ {c4}\n" \
              "⑤ {c5}\n\n"
    
    s1, s2 = np.random.choice(np.arange(2, 30), 2, replace=True)
    s3 = s1 + s2
    
    s4, s5, c1 = np.random.choice(np.arange(2, 30), 3, replace=True)
    s6 = np.power(c1, 2)
    c2 = s4 * s5 - c1
    s7 = c2 + s5

    s8, s9, s10 = np.random.choice(np.arange(2, 30), 3, replace=True)
    s11 = s8 * s9 + s10

    t0, t1, s13, s15, s16 = np.random.choice(np.arange(2, 30), 5, replace=True)
    s12 = t0 * s15
    s14 = t1 * s13
    s17 = -t0 * t1 * s16
    
    s18 = np.random.randint(2, 20)
    t2 = round(np.random.randint(2, 10) / 10, 1)
    s19 = round(t2*t2, 2)    
    s20 = 10
    s21 = int(s18 - (t2 * s20))

    s_candidates = ["$$수식$$( sqrt {{" + str(s1) + "}} )^{{2}} `+`$$/수식$$ (-$$수식$$sqrt{{" + str(s2) + "}} )^{{2}} `=` " + str(s3) + "$$/수식$$", "( - $$수식$$sqrt {{" + str(s4) + "}} )^{{2}} `times` sqrt{{ (-" + str(s5) + ")^{{2}} }} `-` sqrt{{" + str(s6) + "}} `=` " + str(s7) + "$$/수식$$", "( - $$수식$$sqrt {{" + str(s8) + "}} )^{{2}} `div` sqrt{{ ( {{1}} over {{" + str(s9) + "}} )^{{2}} }} `+` sqrt{{" + str(s10) + "^{{2}} }} `=` " + str(s11) + "$$/수식$$", "-$$수식$$  sqrt{{ ( {{" + str(s12) + "}} over {{" + str(s13) + "}} )^{{2}} }}  `times` ( sqrt{{ {{" + str(s14) + "}} over {{" + str(s15) + "}} }} )^{{2}} `times` ( - sqrt{{" + str(s16) + "}} )^{{2}} `=` " + str(s17) + "$$/수식$$", "$$수식$$( - sqrt {{" + str(s18) + "}} )^{{2}} `-` sqrt{{ " + str(s19) + "}} `times` sqrt{{ (-" + str(s20) + ")^{{2}} }} `=` " + str(s21) + "$$/수식$$"]
    s_answer = ["(주어진 식) $$수식$$`=`" + str(s1) + "`+`" + str(s2) + "`=`" + str(s3) + "$$/수식$$", "(주어진 식) $$수식$$`=`" + str(s4) + "`times`" + str(s5) + "`-`" + str(c1) + "`=`" + str(c2) + "$$/수식$$", "(주어진 식) $$수식$$`=`" + str(s8) + "`div` {{1}} over {{" + str(s9) + "}} `+`" + str(s10) + "`=`" + str(s11) + "$$/수식$$", "(주어진 식) $$수식$$`=` - {{" + str(s12) + "}} over {{" + str(s13) + "}} `times` {{" + str(s14) + "}} over {{" + str(s15) + "}} `times`" + str(s16) + "`=`" + str(s17) + "$$/수식$$", "(주어진 식) $$수식$$`=`" + str(s18) + "`-`" + str(t2) + "`times`" + str(s20) + "`=`" + str(s21) + "$$/수식$$"]

    s_shuf = np.arange(5)
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    s_answer = np.array(s_answer)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    c1, c2, c3, c4, c5 = s_answer[s_shuf]
    
    correct_idx = np.where(s_shuf == 1)[0][0]

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_040():
    stem = "$$수식$$ ( - sqrt{{ {q1} }} )^{{2}} `-` ( - sqrt {{ {q2} }} )^{{2}}$$/수식$$을 계산하시오.\n"
    answer = "(답) $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$ ( - sqrt{{ {q1} }} )^{{2}} `-` ( - sqrt {{ {q2} }} )^{{2}} `=` {q1} - {q2} `=` {c1}$$/수식$$\n\n"
                  
    q1, q2 = np.random.choice(np.arange(2, 20), 2, replace=False)
    c1 = q1 - q2

    a1 = c1

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1)
    return stem, answer, comment


def realnum311_Stem_041():
    stem = "-$$수식$$ sqrt{{ (-{q1})^{{2}} }} `times` ( - sqrt {{ {{1}} over {{ {q2} }} }} )^{{2}}$$/수식$$을 계산하시오.\n"
    answer = "(답) $$수식$$-{a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "(주어진 식) $$수식$$`=` -{q1} `times` {{1}} over {{ {q2} }} `=` -{c1}$$/수식$$\n\n"
                  
    c1, q2 = np.random.choice(np.arange(2, 20), 2, replace=False)
    q1 = c1 * q2
    
    a1 = c1

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1)
    return stem, answer, comment


def realnum311_Stem_042():
    stem = "$$수식$$ sqrt{{ {q1} }} `-` sqrt {{ ( - {q2} )^{{2}} }} `+` ( - sqrt{{ {q3} }} )^{{2}}$$/수식$$을 계산하면?\n" \
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "(주어진 식) $$수식$$`=` {c1} `-` {q2} `+` {q3} `=` {c2}$$/수식$$\n\n"
                  
    c1, q2, q3 = np.random.choice(np.arange(2, 20), 3, replace=False)
    q1 = np.power(c1, 2)
    c2 = c1 - q2 + q3
    
    a1 = c2

    diff = 1
    
    s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, q3=q3, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q2=q2, q3=q3, c1=c1, c2=c2)
    return stem, answer, comment


def realnum311_Stem_043():
    stem = "$$수식$$ sqrt{{ {q1} }} `-` sqrt{{ ( -{q2} )^{{2}} }} `+`$$/수식$$ (-$$수식$$sqrt{{ {q3} }} )^{{2}} `=` A$$/수식$$라 할 때, $$수식$${q4}A$$/수식$$의 값을 구하시오.\n"
    answer = "(답) $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "(주어진 식) $$수식$$`=` {c1} `-` {q2} `+` {q3} `=` {c2}$$/수식$$이므로\n"    \
              "$$수식$$A `=` {c2} $$/수식$$\n$$수식$$`THEREFORE` {q4}A `=` {c3}$$/수식$$\n\n"
                  
    c1, q2, q3, q4 = np.random.choice(np.arange(2, 20), 4, replace=False)
    q1 = np.power(c1, 2)
    c2 = c1 - q2 + q3
    c3 = q4 * c2

    a1 = c3

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4)
    answer = answer.format(a1=a1)
    comment = comment.format(q2=q2, q3=q3, q4=q4, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_044():
    stem = "$$수식$$A$$/수식$$, $$수식$$B$$/수식$$가 다음과 같을 때, $$수식$$A `-` B$$/수식$$의 값은?\n" \
           "$$표$$ $$수식$$A `=` ( sqrt{{ 0.{q1} }} )^{{2}} `div` (- sqrt{{ 0.{q2} }} )^{{2}} `times` sqrt{{ {q3} }}$$/수식$$\n $$수식$$B `=` ( - sqrt{{ {q4} }} )^{{2}} `times` sqrt{{ ( {{1}} over {{ {q5} }} )^{{2}} }} `-` sqrt{{ {q6} }} `times` sqrt{{ ( - {q7} )^{{2}} }}$$/수식$$ $$/표$$\n" \
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$A `=` 0.{q1} `div` 0.{q2} `times` {c7} `=` {{1}} over {{ {q2} }} `times` {q1} `times` {c7} `=` {c1}$$/수식$$\n"   \
              "$$수식$$B `=` {q4} `times` {{1}} over {{ {q5} }} `-` {c2} `times` {q7} `=` {c3} `-` {c4} `=` {c5}$$/수식$$\n"   \
              "$$수식$$THEREFORE` A `-` B `=` {c6}$$/수식$$\n\n"
                  
    q1, q2, t0 = np.random.choice(np.arange(2, 10), 3, replace=False)
    c7 = t0 * q2
    q3 = np.power(c7, 2)
    c1 = t0 * q1

    c3, q5, c2, q7 = np.random.choice(np.arange(2, 10), 4, replace=False)
    q6 = np.power(c2, 2)
    q4 = q5 * c3
    c4 = c2 * q7
    c5 = c3 - c4
    
    c6 = c1 - c5
    a1 = c6

    diff = 2
    
    s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q7=q7, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7)
    return stem, answer, comment


def realnum311_Stem_045():
    stem = "$$수식$$A `=` sqrt{{ (-{q1})^{{2}} }} `+` $$/수식$$(-$$수식$$sqrt{{ {q2} }} )^{{2}} `+` sqrt{{ {q3} }} `-` sqrt{{ ( - {q4} )^{{2}} }}$$/수식$$일 때, $$수식$$sqrt{{ A }}$$/수식$$의 값은?\n" \
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$A `=` {q1} `+` {q2} `+` {c1} `-` {q4} `=` {c2}$$/수식$$\n"   \
              "$$수식$$THEREFORE` sqrt{{ A }} `=` sqrt{{ {c2} }} `=` {c3}$$/수식$$\n\n"

    q4 = 0
    while q4 <= 0:
        q1, q2, c1 = np.random.choice(np.arange(2, 20), 3, replace=False)
        q3 = np.power(c1, 2)
        c3 = np.random.randint(2, 20)
        c2 = np.power(c3, 2)
        q4 = q1 + q2 + c1 - c2
    
    a1 = c3

    diff = 1
    s_positive = 0
    while s_positive - (2 * diff) <= 0:
        s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q4=q4, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_046():
    stem = "$$수식$$sqrt{{ {q1}^{{2}} }} `times` ( - sqrt{{ {q2} }} )^{{2}} `-` ( - sqrt{{ {q3} }} )^{{2}}$$/수식$$을 계산하시오.\n"
    answer = "(답) $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ {q1}^{{2}} }} `times` ( - sqrt{{ {q2} }} )^{{2}} `-` ( - sqrt{{ {q3} }} )^{{2}} `=` {q1} `times` {q2} `-` {q3} `=` {c1}$$/수식$$\n\n"
                  
    q1, q2, q3 = np.random.choice(np.arange(2, 20), 3, replace=False)
    c1 = q1 * q2 - q3

    a1 = c1

    stem = stem.format(q1=q1, q2=q2, q3=q3)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, q3=q3, c1=c1)
    return stem, answer, comment


def realnum311_Stem_047():
    stem = "$$수식$$sqrt{{ ( - {q1} )^{{2}} }} `times` sqrt{{ {{ {q2} }} over {{ {q3} }} }} `+` sqrt{{ ( {{ {q4} }} over {{ {q5} }} )^{{2}} }} `div` ( - sqrt{{ {{1}} over {{ {q6} }} }} )^{{2}}$$/수식$$을 계산하시오.\n"
    answer = "(답) $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ ( - {q1} )^{{2}} }} `times` sqrt{{ {{ {q2} }} over {{ {q3} }} }} `+` sqrt{{ ( {{ {q4} }} over {{ {q5} }} )^{{2}} }} `div` ( - sqrt{{ {{1}} over {{ {q6} }} }} )^{{2}}$$/수식$$\n"    \
              "$$수식$$=` {q1} `times` {{ {c4} }} over {{ {c5} }} `+` {{ {q4} }} over {{ {q5} }} `div` {{1}} over {{ {q6} }}$$/수식$$\n" \
              "$$수식$$=` {q1} `times` {{ {c4} }} over {{ {c5} }} `+` {{ {q4} }} over {{ {q5} }} `times` {q6}$$/수식$$\n" \
              "$$수식$$=` {c1} `+` {c2} `=` {c3}$$/수식$$\n\n"
                  
    c4, c5, q4, q5 = np.random.choice(np.arange(2, 17), 4, replace=False)
    q2, q3 = np.power([c4, c5], 2)
    t0, t1 = np.random.choice(np.arange(2, 10), 2, replace=True)
    q1 = t0 * c5
    q6 = t1 * q5

    c1 = t0 * c4
    c2 = t1 * q4
    c3 = c1 + c2

    a1 = c3

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_048():
    stem = "$$수식$$sqrt{{ {q1} }} `-` sqrt{{ (- {q2} )^{{2}} }} `div` sqrt{{ 0.{q3} }} `+` ( sqrt{{ {q4} }} )^{{2}}$$/수식$$을 계산하면?\n"\
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ {q1} }} `-` sqrt{{ (- {q2} )^{{2}} }} `div` sqrt{{ 0.{q3} }} `+` ( sqrt{{ {q4} }} )^{{2}}$$/수식$$\n"    \
              "$$수식$$=` {c1} `-` {q2} `div` 0.{c3} `+` {q4}$$/수식$$\n" \
              "$$수식$$=` {c1} `-` {q2} `times` {{ {c3} }} over {{10}} `+` {q4}$$/수식$$\n" \
              "$$수식$$=` {c1} `-` {c2} `+` {q4} `=` {c4}$$/수식$$\n\n"
    c4 = -1
    while (c4 < 0):
        c3 = np.random.randint(4, 10)
        c1, q4 = np.random.choice(np.arange(2, 17), 2, replace=False)
        q1, q3 = np.power([c1, c3], 2)
        t0 = np.random.choice(np.arange(2, 10), 1, replace=True)[0]
        q2 = t0 * 10

        c2 = t0 * c3
        c4 = c1 - c2 + q4

    a1 = c4

    diff = 1
    s_positive = 0
    while s_positive - (2 * diff) < 0:
        s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment


def realnum311_Stem_049():
    stem = "$$수식$$a `=` sqrt{{ {q1} }}$$/수식$$, $$수식$$b `=` - sqrt{{ {q2} }}$$/수식$$, $$수식$$c `=` - sqrt{{ {q3} }}$$/수식$$일 때, $$수식$$a^{{2}} `-` b^{{2}} `+` {q4}c^{{2}}$$/수식$$의 값은?\n"\
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a^{{2}} `-` b^{{2}} `+` {q4}c^{{2}}$$/수식$$\n"    \
              "= ($$수식$$sqrt{{ {q1} }})^{{2}} `-` (- sqrt{{ {q2} }})^{{2}} `+` {q4} `times` (- sqrt{{ {q3} }})^{{2}}$$/수식$$\n" \
              "$$수식$$=` {q1} `-` {q2} `+` {q4} `times` {q3} `=` {c1}$$/수식$$\n\n"
    
    q1, q2, q3, q4 = np.random.choice(np.arange(2, 17), 4, replace=False)
    c1 = q1 - q2 + (q4 * q3)

    a1 = c1

    diff = 1
    
    s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, c1=c1)
    return stem, answer, comment


def realnum311_Stem_050():
    stem = "$$수식$$a `=` sqrt{{ {q1} }}$$/수식$$, $$수식$$b `=` - sqrt{{ {q2} }}$$/수식$$, $$수식$$c `=` {q3}$$/수식$$일 때, $$수식$${q4}a^{{2}} `-` ( ab )^{{2}} `+` sqrt{{ c^{{2}} }} `times` sqrt{{ ( -c )^{{2}} }}$$/수식$$의 값은?\n"\
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${q4} `times` ( sqrt{{ {q1} }} )^{{2}} `-` {q1} `times` ( - sqrt{{ {q2} }} )^{{2}} `+` sqrt{{ {q3}^{{2}} }} `times` sqrt{{ ( -{q3} )^{{2}} }}$$/수식$$\n"    \
              "$$수식$$=` {q4} `times` {q1} `-` {q1} `times` {q2} `+` {q3} `times` {q3}$$/수식$$\n" \
              "$$수식$$=` {c1} `-` {c2} `+` {c3} `=` {c4}$$/수식$$\n\n"
    
    q1, q2, q3, q4 = np.random.choice(np.arange(2, 17), 4, replace=False)
    c1 = q4 * q1
    c2 = q1 * q2
    c3 = q3 * q3
    c4 = c1 - c2 + c3

    a1 = c4

    diff = 1
    
    s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment


def realnum311_Stem_051():
    stem = "$$수식$$a `&lt;` 0$$/수식$$일 때, $$수식$$sqrt{{ {q1}a^{{2}} }}$$/수식$$을 간단히 하면?\n"\
           "① $$수식$${ss1}a^{{2}}$$/수식$$\n" \
           "② $$수식$${ss2}a$$/수식$$\n" \
           "③ $$수식$${ss3}a$$/수식$$\n" \
           "④ $$수식$${ss4}a^{{2}}$$/수식$$\n" \
           "⑤ $$수식$${ss5}a$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ {q1}a^{{2}} }} `=` sqrt{{ ( {c1}a )^{{2}} }}$$/수식$$이고, $$수식$${c1}a `&lt;` 0$$/수식$$이므로\n" \
              "$$수식$$sqrt{{ {q1}a^{{2}} }} `=` sqrt{{ ( {c1}a )^{{2}} }} `=` -{c1}a$$/수식$$\n\n"
    
    c1 = np.random.choice(np.arange(2, 17), 1, replace=False)[0]
    q1 = np.power(c1, 2)

    a1 = -c1

    s_candidates = [a1, a1, -a1, -a1, a1 * a1]
    ss1, ss2, ss3, ss4, ss5 = s_candidates

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[1])
    comment = comment.format(q1=q1, c1=c1)
    return stem, answer, comment


def realnum311_Stem_052():
    stem = "$$수식$$a `&gt;` 0$$/수식$$일 때, 다음 중 옳지 않은 것은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "① {c1}\n" \
              "② {c2}\n" \
              "③ {c3}\n" \
              "④ {c4}\n" \
              "⑤ {c5}\n\n"
    
    q1, q2, c1, q4 = np.random.choice(np.arange(2, 25), 4, replace=False)
    q3 = np.power(c1, 2)

    s_candidates = ["$$수식$$sqrt{{ ( - a )^{{2}} }} `=` a$$/수식$$", "$$수식$$ - sqrt{{ (" + str(q1) + "a )^{{2}} }}`=` - " + str(q1) + "a$$/수식$$", "$$수식$$sqrt{{ ( - " + str(q2) + "a )^{{2}} }} `=` " + str(q2) + "a$$/수식$$", "$$수식$$ - sqrt{{" + str(q3) + "a^{{2}} }} `=` -" + str(q3) + "a$$/수식$$", "$$수식$$ - sqrt{{ ( - " + str(q4) + "a )^{{2}} }}`=` -" + str(q4) + "a$$/수식$$"]
    s_answer = ["$$수식$$-a `&lt;` 0$$/수식$$이므로 $$수식$$sqrt{{ ( - a )^{{2}} }} `=` -(-a ) `=` a$$/수식$$", "$$수식$$" + str(q1) + "a `&gt;` 0$$/수식$$이므로 $$수식$$ - sqrt{{ (" + str(q1) + "a )^{{2}} }}`=` -" + str(q1) + "a$$/수식$$", "$$수식$$-" + str(q2) + "a `&lt;` 0$$/수식$$이므로 $$수식$$sqrt{{ ( -" + str(q2) + "a )^{{2}} }} `=` -(-" + str(q2) + "a ) `=`" + str(q2) + "a$$/수식$$", "-$$수식$$ sqrt{{" + str(q3) + "a^{{2}} }} `=` - sqrt{{ (" + str(c1) + "a )^{{2}} }}$$/수식$$이고, $$수식$$" + str(c1) + "a `&gt;` 0$$/수식$$이므로  -$$수식$$ sqrt{{" + str(q3) + "a^{{2}} }} `=` - sqrt{{ (" + str(c1) + "a )^{{2}} }} `=` -" + str(c1) + "a$$/수식$$", "$$수식$$ - " + str(q4) + "a `&lt;` 0$$/수식$$이므로 - sqrt{{ ( -" + str(q4) + "a )^{{2}} }} `=` -" + str(q4) + "a$$/수식$$"]

    s_shuf = np.arange(5)
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    s_answer = np.array(s_answer)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    c1, c2, c3, c4, c5 = s_answer[s_shuf]
    
    correct_idx = np.where(s_shuf == 3)[0][0]

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_053():
    stem = "$$수식$$a `&lt;` 0$$/수식$$일 때, 다음 중 옳은 것은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a `&lt;` 0$$/수식$$일 때\n" \
              "① {c1}\n" \
              "② {c2}\n" \
              "③ {c3}\n" \
              "④ {c4}\n" \
              "⑤ {c5}\n\n"
    
    q1, q2, c1, c2 = np.random.choice(np.arange(2, 25), 4, replace=False)
    q3, q4 = np.power([c1, c2], 2)

    s_candidates = ["$$수식$$sqrt{{ a^{{2}} }} `=` a$$/수식$$", "$$수식$$ - sqrt{{ (" + str(q1) + "a )^{{2}} }}`=` " + str(q1) + "a$$/수식$$", "-$$수식$$sqrt{{ ( - " + str(q2) + "a )^{{2}} }} `=` -" + str(q2) + "a$$/수식$$", "$$수식$$ - sqrt{{" + str(q3) + "a^{{2}} }} `=`" + str(q3) + "a$$/수식$$", "$$수식$$ sqrt{{" + str(q4) + "a^{{2}} }} `=`" + str(c2) + "a$$/수식$$"]
    s_answer = ["$$수식$$sqrt{{ a^{{2}} }} `=` -a$$/수식$$", "$$수식$$" + str(q1) + "a `&lt;` 0$$/수식$$이므로 $$수식$$ - sqrt{{ (" + str(q1) + "a )^{{2}} }}`=` -(-" + str(q1) + "a ) `=`" + str(q1) + "a$$/수식$$", "$$수식$$-" + str(q2) + "a `&gt;` 0$$/수식$$이므로  $$수식$$- sqrt{{ ( -" + str(q2) + "a )^{{2}} }} `=` - (-" + str(q2) + "a ) `=`" + str(q2) + "a$$/수식$$", " -$$수식$$ sqrt{{" + str(q3) + "a^{{2}} }} `=` - sqrt{{ (" + str(c1) + "a )^{{2}} }}$$/수식$$이고, $$수식$$" + str(c1) + "a `&lt;` 0$$/수식$$이므로 $$수식$$ - sqrt{{" + str(q3) + "a^{{2}} }} `=` - sqrt{{ (" + str(c1) + "a )^{{2}} }} `=` - (-" + str(c1) + "a ) `=` " + str(c1) + "a$$/수식$$", "$$수식$$ sqrt{{" + str(q4) + "a^{{2}} }} `=` sqrt{{ (" + str(c2) + "a )^{{2}} }}$$/수식$$이고, $$수식$$" + str(c2) + "a `&lt;` 0$$/수식$$이므로 $$수식$$ sqrt{{" + str(q4) + "a^{{2}} }} `=` sqrt{{ (" + str(c2) + "a )^{{2}} }} `=` - " + str(c2) + "a$$/수식$$"]

    s_shuf = np.arange(5)
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    s_answer = np.array(s_answer)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    c1, c2, c3, c4, c5 = s_answer[s_shuf]
    
    correct_idx = np.where(s_shuf == 1)[0][0]

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_054():
    stem = "$$수식$$a `&gt;` 0$$/수식$$일 때, 다음 중 그 값이 가장 큰 것은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "① {cc1}\n" \
              "② {cc2}\n" \
              "③ {cc3}\n" \
              "④ {cc4}\n" \
              "⑤ {cc5}\n\n"

    s1 = 1
    c2 = 2
    s4 = 1
    while (c2/s4) >= s1:
        s1, s4 = np.random.choice(np.arange(3, 25), 2, replace=False)
        s5 = s1
        s6 = np.random.randint(2, s1)
        c3 = 2 * s4
        c2 = s1
        s2 = np.power(s1, 2)
        s3 = np.power(c3, 2)

    s_candidates = ["$$수식$$" + str(s1) + "sqrt{{ a^{{2}} }}$$/수식$$",
    "$$수식$$sqrt{{ {{" + str(s2) + "a^{{2}} }} over {{" + str(s3) + "}} }}$$/수식$$",
    "$$수식$${{ sqrt{{" + str(s2) + "a^{{2}} }} }} over {{" + str(s4) + "}}$$/수식$$",
    "$$수식$$- sqrt{{ ( - " + str(s5) + "a )^{{2}} }}$$/수식$$",
    "$$수식$$sqrt{{ ( -" + str(s6) + "a )^{{2}} }}$$/수식$$"]
    s_answer = ["$$수식$$ a `&gt; 0$$/수식$$이므로 $$수식$$" + str(s1) + "sqrt{{ a^{{2}} }} `=` " + str(s1) + "a$$/수식$$",
    "$$수식$$sqrt{{ {{" + str(s2) + "a^{{2}} }} over {{" + str(s3) + "}} }} `=` sqrt{{ ( {{" + str(c2) + "}} over {{" + str(c3) + "}} a )^{{2}} }}$$/수식$$이고, $$수식$$ {{" + str(c2) + "}} over {{" + str(c3) + "}} a `&gt;` 0$$/수식$$이므로\n $$수식$$sqrt{{ {{" + str(s2) + "a^{{2}} }} over {{" + str(s3) + "}} }} `=` {{" + str(c2) + "}} over {{" + str(c3) + "}} a $$/수식$$",
    "$$수식$${{ sqrt{{" + str(s2) + "a^{{2}} }} }} over {{" + str(s4) + "}} `=` {{ sqrt{{ (" + str(c2) + "a )^{{2}} }} }} over {{" + str(s4) + "}}$$/수식$$이고, $$수식$$" + str(c2) + "a `&gt;` 0$$/수식$$이므로\n $$수식$${{ sqrt{{" + str(s2) + "a^{{2}} }} }} over {{" + str(s4) + "}} `=` {{" + str(c2) + "}} over {{" + str(s4) + "}}a $$/수식$$",
    "$$수식$$- " + str(s5) + "a `&lt;` 0$$/수식$$이므로   $$수식$$- sqrt{{ ( - " + str(s5) + "a )^{{2}} }} `=` - { - ( -" + str(s5) + "a ) } `=` - " + str(s5) + "a$$/수식$$",
    "$$수식$$- " + str(s6) + "a `&lt;` 0$$/수식$$이므로   $$수식$$sqrt{{ ( -" + str(s6) + "a )^{{2}} }}`=` - ( -" + str(s6) + "a ) `=`" + str(s6) + "a$$/수식$$"]

    s_shuf = np.arange(5)
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    s_answer = np.array(s_answer)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    cc1, cc2, cc3, cc4, cc5 = s_answer[s_shuf]
    
    correct_idx = np.where(s_shuf == 0)[0][0]

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(cc1=cc1, cc2=cc2, cc3=cc3, cc4=cc4, cc5=cc5)
    return stem, answer, comment


def realnum311_Stem_055():
    stem = "$$수식$$sqrt{{ ( {q1}a `-` {q2} )^{{2}} }} `=` {q3}$$/수식$$을 만족시키는 모든 $$수식$$a$$/수식$$의 값의 합은?\n"\
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "(i) $$수식$${q1}a `-` {q2} `GEQ` 0$$/수식$$, 즉 $$수식$$a `GEQ` {{1}} over {{2}}$$/수식$$일 때,\n" \
              "$$수식$$sqrt{{ ( {q1}a `-` {q2} )^{{2}} }}`=` {q1}a `-` {q2} `=` {q3} `THEREFORE` a `=` {c1}$$/수식$$\n" \
              "(ii) $$수식$${q1}a `-` {q2} `&lt;` 0$$/수식$$, 즉 $$수식$$a `&lt;` {{1}} over {{2}}$$/수식$$일 때,\n" \
              "$$수식$$sqrt{{ ( {q1}a `-` {q2} )^{{2}} }}`=` - ( {q1}a `-` {q2} ) `=` {q3} `THEREFORE` a `=` {c2}$$/수식$$\n" \
              "(i), (ii)에서 $$수식$$a `=` {c1}$$/수식$$ 또는 $$수식$$a `=` {c2}$$/수식$$이므로 구하는 값은 1이다.\n\n"
    
    t0 = np.random.randint(1, 7)
    q1 = 2 * t0
    q2 = t0
    t1 = np.random.randint(1, 7)
    q3 = q2 + (q1 * t1)
    c1 = (q3 + q2) // q1
    c2 = (-q3 + q2) // q1
    c3 = c1 + c2

    a1 = c3

    diff = 1

    s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, q3=q3, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, c1=c1, c2=c2)
    return stem, answer, comment


def realnum311_Stem_056():
    stem = "$$수식$$a `&lt;` 0$$/수식$$일 때, $$수식$$sqrt{{ a^{{2}} }} `+` sqrt{{ {q1} a^{{2}} }} `-` sqrt{{ (-{q2})^{{2}}a^{{2}} }}$$/수식$$을 간단히 하면?\n"\
           "① $$수식$$a$$/수식$$\n" \
           "② $$수식$${ss2}a$$/수식$$\n" \
           "③ $$수식$${ss3}a$$/수식$$\n" \
           "④ $$수식$${ss4}a$$/수식$$\n" \
           "⑤ $$수식$${ss5}a$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ a^{{2}} }} `+` sqrt{{ {q1} a^{{2}} }} `-` sqrt{{ (-{q2})^{{2}}a^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` sqrt{{ a^{{2}} }} `+` sqrt{{ ({c1}a )^{{2}} }} `-` sqrt{{ (-{q2}a )^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` -a `+` (-{c1}a ) `-` (-{q2}a )$$/수식$$\n" \
              "$$수식$$=` {c2}a$$/수식$$\n\n"
    c2 = 0
    while c2 <= 1:
        c1, q2 = np.random.choice(np.arange(2, 25), 2, replace=False)
        q1 = np.power(c1, 2)
        c2 = q2 - c1 - 1
    a1 = c2

    diff = 1
    s_positive = 0
    while s_positive - (2 * diff) < 1:
        s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff][np.random.randint(0, 4)]
    s_candidates = [s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx + 1])
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2)
    return stem, answer, comment


def realnum311_Stem_057():
    stem = "$$수식$$a `&lt;` 0$$/수식$$일 때\n, $$수식$$sqrt{{ a^{{2}} }} `times` sqrt{{ (- {{ {q1} }} over {{ {q2} }} a )^{{2}} }} `-` sqrt{{ {q3}a^{{2}} }} `times` sqrt{{ 0.{q4}a^{{2}} }}$$/수식$$을 간단히 하면?\n"\
           "① $$수식$${{1}} over {{ {ss1} }}a^{{2}}$$/수식$$\n" \
           "② $$수식$${{1}} over {{ {ss2} }}a^{{2}}$$/수식$$\n" \
           "③ $$수식$${{1}} over {{ {ss3} }}a^{{2}}$$/수식$$\n" \
           "④ $$수식$$a^{{2}}$$/수식$$\n" \
           "⑤ $$수식$${ss5}a^{{2}}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ a^{{2}} }} `times` sqrt{{ (- {{ {q1} }} over {{ {q2} }} a )^{{2}} }} `-` sqrt{{ {q3}a^{{2}} }} `times` sqrt{{ 0.{q4}a^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` sqrt{{ a^{{2}} }} `times` sqrt{{ (- {{ {q1} }} over {{ {q2} }} a )^{{2}} }} `-` sqrt{{ ({c3}a )^{{2}} }} `times` sqrt{{ ( 0.{c4}a )^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` -a `times` (- {{ {q1} }} over {{ {q2} }} a ) `-` (-{c3}a ) `times` (- 0.{c4}a )$$/수식$$\n" \
              "$$수식$$=` {{ {q1} }} over {{ {q2} }} a^{{2}} `-` {c1}a^{{2}}$$/수식$$\n"    \
              "$$수식$$=` {{ 1 }} over {{ {q2} }} a^{{2}}$$/수식$$\n\n"
    
    q2 = np.random.randint(2, 10)
    t0 = np.random.randint(2, 10)
    c3 = t0 * 10
    c4 = np.random.randint(2, 10)       
    c1 = c4 * t0
    q3, q4 = np.power([c3, c4], 2)
    q1 = q2 * c1 + 1

    ss1, ss2, ss3, ss5 = [q2 * 3, q2 * 2, q2, q2]

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, ss1=ss1, ss2=ss2, ss3=ss3, ss5=ss5)
    answer = answer.format(a1=answer_dict[2])
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, c1=c1, c3=c3, c4=c4)
    return stem, answer, comment


def realnum311_Stem_058():
    stem = "$$수식$$a `&gt;` 0$$/수식$$, $$수식$$ab `&lt;` 0$$/수식$$일 때\n, $$수식$$sqrt{{ (-a )^{{2}} }} `-` sqrt{{ {q2} a^{{2}} }} `+` sqrt{{ (- {q3}b )^{{2}} }} `-` sqrt{{ b^{{2}} }}$$/수식$$을 간단히 하면?\n"\
           "① $$수식$$- {s1}a `-` {s2}b$$/수식$$\n" \
           "② $$수식$$- {c1}a `-` {c3}b$$/수식$$\n" \
           "③ $$수식$$ {c1}a `-` {s2}b$$/수식$$\n" \
           "④ $$수식$$ {c1}a `+` {c3}b$$/수식$$\n" \
           "⑤ $$수식$$ {c3}a `+` {c3}b$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a `&gt;` 0$$/수식$$, $$수식$$ab `&lt;` 0$$/수식$$에서 $$수식$$b `&lt;` 0$$/수식$$이므로\n" \
              "$$수식$$sqrt{{ (-a )^{{2}} }} `-` sqrt{{ {q2} a^{{2}} }} `+` sqrt{{ (- {q3}b )^{{2}} }} `-` sqrt{{ b^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` sqrt{{ (-a )^{{2}} }} `-` sqrt{{ ({c2} a )^{{2}} }} `+` sqrt{{ (- {q3}b )^{{2}} }} `-` sqrt{{ b^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` - (-a ) `-` {c2}a `+` (- {q3}b ) `-` (- b )$$/수식$$\n" \
              "$$수식$$=` - {c1}a `-` {c3}b $$/수식$$\n\n"
    c1 = 1
    c3 = 1
    while c1 == c3:
        c2 = np.random.randint(3, 10)
        q2 = np.power(c2, 2)    
        c1 = c2 - 1
        q3 = np.random.randint(3, 10)
        c3 = q3 - 1

        s1 = c2 + 1
        s2 = q3 + 1

    stem = stem.format(q2=q2, q3=q3, c1=c1, s1=s1, s2=s2, c3=c3)
    answer = answer.format(a1=answer_dict[1])
    comment = comment.format(q2=q2, q3=q3, c2=c2, c1=c1, c3=c3)
    return stem, answer, comment


def realnum311_Stem_059():
    stem = "$$수식$$a `-` b `&lt;` 0$$/수식$$, $$수식$$ab `&lt;` 0$$/수식$$일 때\n, $$수식$$sqrt{{ a^{{2}} }} `-` sqrt{{ {q2} b^{{2}} }} `+` sqrt{{ (- a )^{{2}} }} `+` sqrt{{ (-b )^{{2}} }}$$/수식$$을 간단히 하면?\n"\
           "① $$수식$$ -2a `-` b $$/수식$$\n" \
           "② $$수식$$ -2a `-` {c1}b $$/수식$$\n" \
           "③ $$수식$$ -a $$/수식$$\n" \
           "④ $$수식$$ a $$/수식$$\n" \
           "⑤ $$수식$$ 2a `+` {c1}b $$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a `-` b `&lt;` 0$$/수식$$에서 $$수식$$a `&lt;` b$$/수식$$이고 $$수식$$ab `&lt;` 0$$/수식$$이므로\n" \
              "$$수식$$a `&lt;` 0$$/수식$$, $$수식$$b `&gt;` 0$$/수식$$\n" \
              "$$수식$$THEREFORE` sqrt{{ a^{{2}} }} `-` sqrt{{ {q2} b^{{2}} }} `+` sqrt{{ (- a )^{{2}} }} `+` sqrt{{ (-b )^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` sqrt{{ a^{{2}} }} `-` sqrt{{ ({c2} b )^{{2}} }} `+` sqrt{{ (- a )^{{2}} }} `+` sqrt{{ (-b )^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` -a `-` {c2}b `+` (-a ) `-` (- b )$$/수식$$\n" \
              "$$수식$$=` -2a - {c1}b$$/수식$$\n\n"
    
    c2 = np.random.randint(3, 20)
    q2 = np.power(c2, 2)
    c1 = c2 - 1

    stem = stem.format(q2=q2, c1=c1)
    answer = answer.format(a1=answer_dict[1])
    comment = comment.format(q2=q2, c1=c1, c2=c2)
    return stem, answer, comment

def realnum311_Stem_060():
    stem = "$$수식$$a `&gt;` 0$$/수식$$, $$수식$$ab `&lt;` 0$$/수식$$일 때, \n$$수식$$ {q1} sqrt{{ a^{{2}} }} `times` ( - sqrt{{ -b }} )^{{2}} `-` sqrt{{ (- {q3}a )^{{2}} }} `times` sqrt{{ 0.DOT{{ {q4} }}b^{{2}} }}$$/수식$$을 간단히 하면?\n"\
           "① $$수식$$ -2ab $$/수식$$\n" \
           "② $$수식$$ -ab $$/수식$$\n" \
           "③ $$수식$$ ab $$/수식$$\n" \
           "④ $$수식$$ 2ab $$/수식$$\n" \
           "⑤ $$수식$$ 3ab $$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a `&gt;` 0$$/수식$$, $$수식$$ab `&lt;` 0$$/수식$$에서 $$수식$$b `&lt;` 0$$/수식$$\n" \
              "$$수식$$ sqrt{{ 0.DOT{{ {q4} }}b^{{2}} }} `=` sqrt{{ ( {{ {c4} }} over {{3}} b )^{{2}} }}  $$/수식$$이므로\n" \
              "$$수식$${q1} sqrt{{ a^{{2}} }} `times` ( - sqrt{{ -b }} )^{{2}} `-` sqrt{{ (- {q3}a )^{{2}} }} `times` sqrt{{ 0.DOT{{ {q4} }}b^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` {q1}a `times` ( -b ) `-` {{ -( -{q3}a ) }} `times` (- {{ {c4} }} over {{3}} b ) $$/수식$$\n" \
              "$$수식$$=` -{q1}ab `+` {c1}ab$$/수식$$\n" \
              "$$수식$$=` -ab $$/수식$$\n\n"
    
    c4 = [1, 2][np.random.randint(0, 2)]
    q4 = np.power(c4, 2)
    q3 = np.random.randint(2, 16) * 3
    c1 = (q3 // 3) * c4
    q1 = c1 + 1

    stem = stem.format(q1=q1, q3=q3, q4=q4)
    answer = answer.format(a1=answer_dict[1])
    comment = comment.format(q1=q1, q3=q3, q4=q4, c1=c1, c4=c4)
    return stem, answer, comment


def realnum311_Stem_061():
    stem = "$$수식$$a `&lt;` 0$$/수식$$, $$수식$$b `&gt;` 0$$/수식$$일 때\n, $$수식$$ sqrt{{ (a `-` {q1}b )^{{2}} }} `+` sqrt{{ (-a )^{{2}} }} `-` sqrt{{ {q3}b^{{2}} }} $$/수식$$을 간단히 하면?\n"\
           "① $$수식$$ -2a $$/수식$$\n" \
           "② $$수식$$ -a `+` {q1}b $$/수식$$\n" \
           "③ $$수식$$ 2a `-` {s1}b $$/수식$$\n" \
           "④ $$수식$$ 2a `-` {q1}b $$/수식$$\n" \
           "⑤ $$수식$$ {s1}a `-` b$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a `&lt;` 0$$/수식$$, $$수식$$b `&gt;` 0$$/수식$$일 때 $$수식$$a - {q1}b `&lt;` 0$$/수식$$, $$수식$$ -a `&gt;` 0$$/수식$$, $$수식$${c3}b `&gt;` 0$$/수식$$이므로\n" \
              "$$수식$$sqrt{{ (a `-` {q1}b )^{{2}} }} `+` sqrt{{ (-a )^{{2}} }} `-` sqrt{{ {q3}b^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` sqrt{{ (a `-` {q1}b )^{{2}} }} `+` sqrt{{ (-a )^{{2}} }} `-` sqrt{{ ({c3}b )^{{2}} }} $$/수식$$\n" \
              "$$수식$$=` - ( a `-` {q1}b ) `+` (-a ) `-` {c3}b$$/수식$$\n" \
              "$$수식$$=` -a `+` {q1}b `-` a `-` {c3}b$$/수식$$\n" \
              "$$수식$$=` -2a$$/수식$$\n\n"
    
    q1 = np.random.randint(2, 17)
    c3 = q1
    q3 = np.power(c3, 2)
    s1 = np.random.randint(3, q3 + 1)

    stem = stem.format(q1=q1, q3=q3, s1=s1)
    answer = answer.format(a1=answer_dict[0])
    comment = comment.format(q1=q1, q3=q3, c3=c3)
    return stem, answer, comment


def realnum311_Stem_062():
    stem = "$$수식$$a `&lt;` 0$$/수식$$일 때, $$수식$$ sqrt{{ (a `-` {q1} )^{{2}} }} `+` sqrt{{ ({q1} `-` a )^{{2}} }}$$/수식$$을 간단히 하면?\n"\
           "① $$수식$$ 0 $$/수식$$\n" \
           "② $$수식$$ {c1} $$/수식$$\n" \
           "③ $$수식$$ -2a `+` {c1} $$/수식$$\n" \
           "④ $$수식$$ 2a `-` {c1} $$/수식$$\n" \
           "⑤ $$수식$$ 2a $$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a `-` {q1} `&lt;` 0$$/수식$$, $$수식$${q1} `-` a `&gt;` 0$$/수식$$이므로\n" \
              "$$수식$$sqrt{{ (a `-` {q1} )^{{2}} }} `+` sqrt{{ ({q1} `-` a )^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` -(a `-` {q1}) `+` ({q1} `-` a ) $$/수식$$\n" \
              "$$수식$$=` -2a `+` {c1}$$/수식$$\n\n"
    
    q1 = np.random.randint(2, 100)
    c1 = q1 * 2

    stem = stem.format(q1=q1, c1=c1)
    answer = answer.format(a1=answer_dict[2])
    comment = comment.format(q1=q1, c1=c1)
    return stem, answer, comment


def realnum311_Stem_063():
    stem = "$$수식$$x `&lt;` {q1}$$/수식$$일 때, $$수식$$ sqrt{{ (x `-` {q1} )^{{2}} }} `+` sqrt{{ (x `-` {q2} )^{{2}} }} `=` {q3}$$/수식$$을 만족시키는 $$수식$$x$$/수식$$의 값은?\n"\
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$x `&lt;` {q1}$$/수식$$에서 $$수식$$x `-` {q1} `&lt;` 0$$/수식$$, $$수식$$x `-` {q2} `&lt;` 0$$/수식$$이므로\n" \
              "$$수식$$sqrt{{ (x `-` {q1} )^{{2}} }} `+` sqrt{{ (x `-` {q2} )^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` -(x `-` {q1}) `-` (x `-` {q2} ) $$/수식$$\n" \
              "$$수식$$=` -2x `+` {c1}$$/수식$$\n"  \
              "즉, $$수식$$-2x `+` {c1} `=` {q3}$$/수식$$이므로 $$수식$$-2x `=` {c2}$$/수식$$\n"   \
              "$$수식$$THEREFORE` x `=` {c3}$$/수식$$"
    
    q1 = np.random.randint(2, 10)
    q2 = np.random.randint(q1 + 1, 20)
    c1 = q1 + q2
    c3 = -np.random.randint(2, 10)
    c2 = -2 * c3
    q3 = c1 + c2

    a1 = c3

    diff = q1
    s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, q3=q3, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_064():
    stem = "$$수식$${q1} `&lt;` a `&lt;` {q2}$$/수식$$이고, $$수식$$ x `=` sqrt{{ (a `-` {q1} )^{{2}} }} `+` sqrt{{ (a `-` {q2} )^{{2}} }}$$/수식$$일 때, $$수식$$ sqrt{{ ({q3} `-` x )^{{2}} }} `+` sqrt{{ (x `+` {q4} )^{{2}} }} $$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${q1} `&lt;` a `&lt;` {q2}$$/수식$$일 때, $$수식$$ a `-` {q1} `&gt;` 0$$/수식$$, $$수식$$ a `-` {q2} `&lt;` 0$$/수식$$이므로\n" \
              "$$수식$$ x `=` sqrt{{ (a `-` {q1} )^{{2}} }} `+` sqrt{{ (a `-` {q2} )^{{2}} }} $$/수식$$\n" \
              "$$수식$$=` (a `-` {q1}) `+` {{-(a `-` {q2})}} `=` {c1} $$/수식$$\n" \
              "$$수식$$THEREFORE` sqrt{{ ({q3} `-` x )^{{2}} }} `+` sqrt{{ (x `+` {q4} )^{{2}} }}$$/수식$$\n" \
              "$$수식$$=`   sqrt{{ ({q3} `-` {c1} )^{{2}} }} `+` sqrt{{ ({c1} `+` {q4} )^{{2}} }} $$/수식$$\n" \
              "$$수식$$=` sqrt{{ (-{c2})^{{2}} }} `+` sqrt{{ {c3}^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` {c2} `+` {c3} `=` {c4}$$/수식$$\n\n"
    
    q1 = np.random.randint(2, 15)
    q2 = np.random.randint(q1 + 2, 20)
    c1 = q2 - q1
    q3 = np.random.randint(1, c1)
    q4 = np.random.randint(2, 15)
    c2 = c1 - q3
    c3 = c1 + q4
    c4 = c2 + c3

    a1 = c4

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment


def realnum311_Stem_065():
    stem = "$$수식$$a `&gt;` 0$$/수식$$, $$수식$$ab `&lt;` 0$$/수식$$일 때\n, $$수식$$sqrt{{ (-a )^{{2}} }} `+` sqrt{{ (b `-` {q2}a )^{{2}} }} `+` sqrt{{ {q3}b^{{2}} }} $$/수식$$을 간단히 하면?\n"\
           "① $$수식$$ {c1}a `-` {c2}b $$/수식$$\n" \
           "② $$수식$$ a `-` {c2}b $$/수식$$\n" \
           "③ $$수식$$ 0 $$/수식$$\n" \
           "④ $$수식$$ -a `-` b $$/수식$$\n" \
           "⑤ $$수식$$ {c1}a `+` {c2}b $$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a &gt;` 0$$/수식$$, $$수식$$ab `&lt;` 0$$/수식$$이므로 $$수식$$b `&lt;` 0$$/수식$$\n" \
              "$$수식$$sqrt{{ (-a )^{{2}} }} `+` sqrt{{ (b `-` {q2}a )^{{2}} }} `+` sqrt{{ {q3}b^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` sqrt{{ (-a )^{{2}} }} `+` sqrt{{ (b `-` {q2}a )^{{2}} }} `+` sqrt{{ ({c3}b )^{{2}} }}$$/수식$$\n" \
              "$$수식$$=` -(-a ) `-` (b `-` {q2}a ) `+` (- {c3}b )$$/수식$$\n" \
              "$$수식$$=` {c1}a - {c2}b$$/수식$$\n\n"
    
    q2, c3 = np.random.choice(np.arange(2, 25), 2, replace=True)
    q3 = np.power(c3, 2)
    c1 = 1 + q2
    c2 = 1 + c3

    stem = stem.format(q2=q2, q3=q3, c1=c1, c2=c2)
    answer = answer.format(a1=answer_dict[0])
    comment = comment.format(q2=q2, q3=q3, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_066():
    stem = "$$수식$$a `&lt;` 0$$/수식$$이고 $$수식$$ b `=` sqrt{{ ( -a )^{{2}} }}$$/수식$$, $$수식$$c `=` - sqrt{{ {q1} b^{{2}} }}$$/수식$$일 때, $$수식$$a `-` b `+` c$$/수식$$를 간단히 하면?\n"\
           "① $$수식$${ss1}a$$/수식$$\n" \
           "② $$수식$${ss2}a$$/수식$$\n" \
           "③ $$수식$${ss3}a$$/수식$$\n" \
           "④ $$수식$${ss4}a$$/수식$$\n" \
           "⑤ $$수식$${ss5}a$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a `&lt;` 0$$/수식$$이므로\n" \
              "$$수식$$b `=` sqrt{{ ( -a )^{{2}} }} `=` -a$$/수식$$\n" \
              "위의 식에서 $$수식$$-a `&gt;` 0$$/수식$$, 즉 $$수식$$b `&gt;` 0$$/수식$$이므로\n" \
              "$$수식$$c `=` - sqrt{{ {q1}b^{{2}} }} `=` - sqrt{{ ( {c1}b )^{{2}} }} `=` - {c1}b$$/수식$$\n"  \
              "$$수식$$=` - {c1} `times` ( -a ) `=` {c1}a$$/수식$$\n"   \
              "$$수식$$THEREFORE` a `-` b `+` c `=` a `-` ( -a ) `+` {c1}a `=` {c2}a$$/수식$$\n\n"
    
    c1 = np.random.randint(4, 20)
    q1 = np.power(c1, 2)
    c2 = c1 + 2

    a1 = c2

    s_candidates = [-a1 + 2, -a1 + 4, a1 - 4, a1 - 2, a1]
    np.random.shuffle(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2)
    return stem, answer, comment


def realnum311_Stem_067():
    stem = "$$수식$$sqrt{{ ( a `+` {q1} )^{{2}} }} `+` sqrt{{ ( a `-` {q1} )^{{2}} }} =` {q2}$$/수식$$를 만족시키는 모든 $$수식$$a$$/수식$$의 값의 범위는?\n"\
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "(i) $$수식$$a `GEQ` {q1}$$/수식$$일 때, $$수식$$a `+` {q1} `&gt;` 0$$/수식$$, $$수식$$a `-` {q1} `GEQ` 0$$/수식$$이므로\n" \
              "$$수식$$( a `+` {q1} ) `+` ( a `-` {q1} ) `=` {q2}$$/수식$$, $$수식$$2a `=` {q2}$$/수식$$\n" \
              "$$수식$$`THEREFORE` a `=` {q1}$$/수식$$\n" \
              "(ii) $$수식$$-{q1} `LEQ` a `&lt;` {q1}$$/수식$$일 때, $$수식$$a `+` {q1} `GEQ` 0$$/수식$$, $$수식$$a `-` {q1} `&lt;` 0$$/수식$$이므로\n" \
              "$$수식$$( a `+` {q1} ) `-` ( a `-` {q1} ) `=` {q2} `THEREFORE` -{q1} `LEQ` a `&lt;` {q1}$$/수식$$\n" \
              "(iii) $$수식$$a `&lt;` -{q1}$$/수식$$일 때, $$수식$$a `+` {q1} `&lt;` 0$$/수식$$, $$수식$$a `-` {q1} `&lt;` 0$$/수식$$이므로\n" \
              "$$수식$$-( a `+` {q1} ) `-` ( a `-` {q1} ) `=` {q2}$$/수식$$, $$수식$$-2a `=` {q2}$$/수식$$\n" \
              "$$수식$$`THEREFORE` a `=` -{q1}$$/수식$$\n" \
              "$$수식$$a `=` -{q1}$$/수식$$은 $$수식$$a `&lt;` -{q1}$$/수식$$을 만족시키지 않는다.\n" \
              "이상에서 $$수식$$-{q1} `LEQ` a `LEQ` {q1}$$/수식$$\n\n"
    
    q1 = np.random.randint(3, 30)
    q2 = q1 * 2
    c1 = q1 + 1

    s_candidates = ["$$수식$$ -"+ str(q1) + "`&lt;` a `&lt;`" + str(q1) +  "$$/수식$$", "$$수식$$ -" + str(q1) + "`LEQ` a `&lt;`" + str(q1) +  "$$/수식$$", "$$수식$$ -" + str(q1) + "`&lt;` a `LEQ`" + str(q1) +  "$$/수식$$", "$$수식$$ -" + str(q1) + "`LEQ` a `LEQ`" + str(q1) +  "$$/수식$$", "$$수식$$ -" + str(q1) + "`LEQ` a `LEQ`" + str(c1) +  "$$/수식$$"]

    s_shuf = np.arange(5)
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    
    correct_idx = np.where(s_shuf == 3)[0][0]

    stem = stem.format(q1=q1, q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2)
    return stem, answer, comment


def realnum311_Stem_068():
    stem = "$$수식$$ {c1}x `+` {c2} `&gt;` {c3}(x `+` {c4}) $$/수식$$일 때, 다음 식을 간단히 하면?\n"\
           "$$표$$ $$수식$$ sqrt{{ {q1}(x `+` {q2} )^{{2}} }} `-` sqrt{{ x^{{2}} }} `+` sqrt{{ ( {q2} `-` x )^{{2}} }} $$/수식$$ $$/표$$\n" \
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$ {c1}x `+` {c2} `&gt;` {c3}(x `+` {c4}) $$/수식$$에서 $$수식$$  {c1}x `+` {c2} `&gt;` {c3}x `+` {c5} $$/수식$$\n" \
              "$$수식$$ {c6}x `&gt;` {c7} `THEREFORE` x `&gt;` {q2}$$/수식$$\n" \
              "따라서 $$수식$$x `+` {q2} `&gt;` 0$$/수식$$, $$수식$$x `&gt;` 0$$/수식$$, $$수식$${q2} `-`x `&lt;` 0$$/수식$$이므로\n" \
              "$$수식$$ sqrt{{ {q1}(x `+` {q2} )^{{2}} }} `-` sqrt{{ x^{{2}} }} `+` sqrt{{ ( {q2} `-` x )^{{2}} }} $$/수식$$\n" \
              "$$수식$$=` sqrt{{ {{ {c8}^{{2}}(x `+` {q2} )}}^{{2}} }} `-` sqrt{{ x^{{2}} }} `+` sqrt{{ ( {q2} `-` x )^{{2}} }} $$/수식$$\n" \
              "$$수식$$=` {c8}(x `+` {q2}) `-` x `-` ({q2} `-` x ) $$/수식$$\n" \
              "$$수식$$=` {c8}x `+` {c9} $$/수식$$\n\n"
    
    c8 = np.random.randint(2, 16)
    q2 = np.random.randint(2, 10)
    q1 = np.power(c8, 2)
    c9 = c8 * q2 - q2

    c6 = np.random.randint(2, 10)
    c3 = np.random.randint(2, 10)
    c1 = c3 + c6
    c7 = c6 * q2

    c4 = np.random.randint(c7//c3 + 1, 50)
    c5 = c3 * c4
    c2 = c5 + c7

    s_candidates = ["$$수식$$ x `-` " + str(q2) + "$$/수식$$", "$$수식$$ x `+` " + str(q2) + "$$/수식$$", "$$수식$$" + str(c8) + "x `-` " + str(c7) + "$$/수식$$", "$$수식$$" + str(c8) + "x `+` 1$$/수식$$", "$$수식$$" + str(c8) + "x `+` " + str(c9) + "$$/수식$$"]

    s_shuf = np.arange(5)
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    
    correct_idx = np.where(s_shuf == 4)[0][0]

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, q1=q1, q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9)
    return stem, answer, comment


def realnum311_Stem_069():
    stem = "$$수식$$ sqrt{{ ( x `-` a )^{{2}} }} `+` sqrt{{ {q1}(x `+` b )^{{2}} }} $$/수식$$을 간단히 하는 과정에서 식 $$수식$$x `-` a$$/수식$$의 부호를 잘못 보고 계산하였더니\n $$수식$$ sqrt{{ ( x `-` a )^{{2}} }} `+` sqrt{{ {q1}(x `+` b )^{{2}} }} `=` {q2}x `-` {q3}$$/수식$$\n가 되었다. $$수식$$a `+` b `=` {q4}$$/수식$$일 때, 바르게 계산한 식은? (단, $$수식$$x `!=` a$$/수식$$, $$수식$$x `!=` -b$$/수식$$)\n"\
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "(i) $$수식$$x `&gt;` a$$/수식$$, $$수식$$x `&gt;` -b$$/수식$$일 때, $$수식$$x `-` a `&gt;` 0$$/수식$$, $$수식$$x `+` b `&gt;` 0$$/수식$$이므로\n"    \
              "(좌변) $$수식$$`=` (x `-` a ) `+` {c1}(x `+` b ) `=` {c2}x `-` a `+` {c1}b$$/수식$$\n" \
              "이때, $$수식$$ {c2}x `-` a `+` {c1}b `=` {q2}x `-` {q3}$$/수식$$이므로\n" \
              "$$수식$$ - a `+` {c1}b  `=` `-`{q3}$$/수식$$\n"  \
              "(ii) $$수식$$x `&gt;` a$$/수식$$, $$수식$$x `&lt;` -b$$/수식$$일 때, $$수식$$x `-` a `&gt;` 0$$/수식$$, $$수식$$x `+` b `&lt;` 0$$/수식$$이므로\n"    \
              "(좌변) $$수식$$`=` (x `-` a ) `-` {c1}(x `+` b ) `=` -{c3}x `-` a `-` {c1}b$$/수식$$\n" \
              "$$수식$$THEREFORE` -{c3}x `-` a `-` {c1}b `!=` {q2}x `-` {q3}$$/수식$$\n" \
              "(iii) $$수식$$x `&lt;` a$$/수식$$, $$수식$$x `&gt;` -b$$/수식$$일 때, $$수식$$x `-` a `&lt;` 0$$/수식$$, $$수식$$x `+` b `&gt;` 0$$/수식$$이므로\n"    \
              "(좌변) $$수식$$`=` -(x `-` a ) `+` {c1}(x `+` b ) `=` {c3}x `+` a `+` {c1}b$$/수식$$\n" \
              "$$수식$$THEREFORE` {c3}x `+` a `+` {c1}b `!=` {q2}x `-` {q3}$$/수식$$\n" \
              "(iv) $$수식$$x `&lt;` a$$/수식$$, $$수식$$x `&lt;` -b$$/수식$$일 때, $$수식$$x `-` a `&lt;` 0$$/수식$$, $$수식$$x `+` b `&lt;` 0$$/수식$$이므로\n"    \
              "(좌변) $$수식$$`=` -(x `-` a ) `-` {c1}(x `+` b ) `=` -{c2}x `+` a `-` {c1}b$$/수식$$\n" \
              "$$수식$$THEREFORE` -{c2}x `+` a `-` {c1}b `!=` {q2}x `-` {q3}$$/수식$$\n" \
              "이상에서 $$수식$$ - a `+` {c1}b  `=` `-`{q3}$$/수식$$\n" \
              "또 $$수식$$a `+` b `=` {q4}$$/수식$$이므로 두 식을 연립하여 풀면\n"  \
              "$$수식$$a `=` {c4}$$/수식$$, $$수식$$b `=` {c5}$$/수식$$\n"  \
              "따라서 바르게 계산한 식은\n" \
              "$$수식$$ -(x `-` {c4} ) `+` {c1}(x `+` {c5} ) `=` {c3}x `+` {c6}$$/수식$$\n\n"

    c1, c2, c3, c4, c5, c6, q1, q2, q3, q4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    while min([c1, c2, c3, c4, c5, c6, q1, q2, q3, q4]) <= 1:
        c1 = np.random.randint(3, 20)
        q1 = np.power(c1, 2)
        c2 = c1 + 1 #2이상
        c3 = c1 - 1 #2이상


        q4 = (c1 + 1) * np.random.randint(2, 15)
        q3 = (c1 + 1) * np.random.randint(1, (q4 // c1))
        c5 = (q4 - q3) // (c1 + 1)  #a
        c4 = q4 - c5  #b
        q2 = c2
        
        c6 = c4 + (c1 * c5)
        #print(c1, c2, c3, c4, c5, c6, q1, q2, q3, q4)

    s_candidates = ["$$수식$$" + str(c3) + "x `-` " + str(c6 + 2) + "$$/수식$$", "$$수식$$" + str(c3) + "x `-` " + str(c6) + "$$/수식$$", "$$수식$$" + str(c3) + "x `-` " + str(c6 - 2) + "$$/수식$$", "$$수식$$" + str(c3) + "x `+` " + str(c6 - 2) + "$$/수식$$", "$$수식$$" + str(c3) + "x `+` " + str(c6) + "$$/수식$$"]

    s_shuf = np.arange(5)
    np.random.shuffle(s_shuf)
    s_candidates = np.array(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates[s_shuf]
    
    correct_idx = np.where(s_shuf == 4)[0][0]

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    return stem, answer, comment
    

def realnum311_Stem_070():
    stem = "$$수식$$sqrt{{ {q1}x }}$$/수식$$가 자연수가 되도록 하는 가장 작은 두 자리 자연수 $$수식$$a$$/수식$$의 값은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${q1}a `=` {c1}^{{{c2}}} `times` {c3}^{{{c4}}} `times {c5} `times` x$$/수식$$이므로\n" \
              "$$수식$$x `=` {c5} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "따라서 가장 작은 두 자리 자연수 $$수식$$x$$/수식$$는\n" \
              "$$수식$${c5} `times` {c6}^{{2}} `=` {c7}$$/수식$$\n\n"
   
    q1 = 2000
    while q1 >= 2000:
        list_prime = [2, 3, 5, 7, 11]
        c_list = np.array([])
        c_list_len = 3
        while True:
            t0 = list_prime[np.random.randint(0, len(list_prime))]
            c_list = np.union1d(c_list, t0)
            if len(c_list) == c_list_len:
                break
        c_list = list(c_list)
        np.random.shuffle(c_list)
        c1, c3, c5 = RoundCheck(c_list)
        c2 = np.random.randint(1, 3) * 2
        c4 = np.random.randint(1, 3) * 2
        q1 = np.power(c1, c2) * np.power(c3, c4) * c5
        
    c6 = 1
    c7 = c5 * np.square(c6)
    while (c7 % 10) == c7:
        c6 += 1
        c7 = c5 * np.square(c6)
    a1 = c7

    diff = c5
    s_positive = 0
    while s_positive - (2 * diff) <= 9:
        s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7)
    return stem, answer, comment


def realnum311_Stem_071():
    stem = "다음 중 $$수식$$sqrt{{ {c1}^{{{c2}}} `times` {c3}^{{{c4}}} `times` x }}$$/수식$$가 자연수가 되도록 하는 자연수 $$수식$$x$$/수식$$의 값이 될 수 없는 것은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$x `=` {c3} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "{c15} $$수식$${c5} `=` {c3} `times` {c6}^{{2}}$$/수식$$ {c16} $$수식$${c7} `=` {c3} `times` {c8}$$/수식$$ {c17} $$수식$${c9} `=` {c3} `times` {c10}^{{2}}$$/수식$$\n" \
              "{c18} $$수식$${c11} `=` {c3} `times` {c12}^{{2}}$$/수식$$ {c19} $$수식$${c13} `=` {c3} `times` {c14}^{{2}}$$/수식$$\n\n"

    c5, c7, c9, c11, c13 = [1, 1, 1, 1, 1]
    while len(set([c5, c7, c9, c11, c13])) != 5:
        list_prime = np.array([2, 3, 5, 7, 11])
        c1 = list_prime[np.random.randint(0, 5)]
        c3 = c1
        while c3 == c1:
            c3 = list_prime[np.random.randint(0, 5)]
        c2 = np.random.randint(1, 3) * 2
        c4 = np.random.randint(1, 3) * 2 + 1
        c_list = np.array([])
        while True:
            t0 = np.random.randint(1, 10)
            c_list = np.union1d(c_list, t0)
            if len(c_list) == 5:
                break
        c_list = list(c_list)
        np.random.shuffle(c_list)
        c6, c8, c10, c12, c14 = RoundCheck(c_list)
        c8 = pickPrime(10, 1)[0]
        c5 = c3 * np.square(c6)
        c7 = c3 * c8
        c9 = c3 * np.square(c10)
        c11 = c3 * np.square(c12)
        c13 = c3 * np.square(c14)

    s_can = [c5, c7, c9, c11, c13]
    s_candidates = list((np.array(s_can)).copy())
    np.random.shuffle(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == s_can[0]:
            correct_idx1 = idx
        elif s_cand == s_can[1]:
            correct_idx2 = idx
        elif s_cand == s_can[2]:
            correct_idx3 = idx
        elif s_cand == s_can[3]:
            correct_idx4 = idx
        elif s_cand == s_can[4]:
            correct_idx5 = idx

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx2])
    comment = comment.format(c3=c3, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12, c13=c13, c14=c14, c15=answer_dict[correct_idx1], c16=answer_dict[correct_idx2], c17=answer_dict[correct_idx3], c18=answer_dict[correct_idx4], c19=answer_dict[correct_idx5])
    return stem, answer, comment


def realnum311_Stem_072():
    stem = "$$수식$$sqrt{{ {q1}a }}$$/수식$$가 자연수가 되도록 하는 가장 작은 자연수 $$수식$$a$$/수식$$의 값은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ {q1}a }} `=` {c1}^{{{c2}}} `times` {c3}^{{{c4}}} `times a$$/수식$$이므로\n" \
              "$$수식$$a `=` {c3} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "따라서 가장 작은 자연수 $$수식$$a$$/수식$$는 {c3}이다.\n\n"
   
    q1 = 1000
    while q1 >= 1000:
        list_prime = [2, 3, 5, 7, 11]
        c3 = list_prime[np.random.randint(0, 5)]
        c1 = c3
        while c1 == c3:
            c1 = list_prime[np.random.randint(0, 5)]
        c2 = np.random.randint(1, 3) * 2
        c4 = np.random.randint(1, 3) * 2 - 1
        q1 = np.power(c1, c2) * np.power(c3, c4)

        a1 = c3

    diff = c3
    s_positive = 0
    while s_positive - (2 * diff) <= 0:
        s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment


def realnum311_Stem_073():
    stem = "$$수식$$sqrt{{ {q1}a }}$$/수식$$가 자연수가 되도록 하는 {q2}보다 작은 자연수의 개수를 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ {q1}a }} `=` sqrt{{ {c1} `times` {c2}^{{{c3}}} `times` {c4} `times` a }}$$/수식$$가 자연수가 되려면\n" \
              "$$수식$$a `=` {c1} `times` {c4} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "따라서 {q2}보다 작은 자연수 $$수식$$a$$/수식$$는\n" \
              "$$수식$$a `=` {c1} `times` {c4} `times` 1^{{2}} `=` {c5}$$/수식$$, $$수식$$a `=` {c1} `times` {c4} `times` 2^{{2}} `=` {c6}$$/수식$$,\n" \
              "$$수식$$a `=` {c1} `times` {c4} `times` 3^{{2}} `=` {c7}$$/수식$$의 3개이다.\n\n"

    q1 = 1500
    while q1 >= 1500:
        list_prime = [2, 3, 5, 7, 11]
        c1 = list_prime[np.random.randint(0, 5)]
        c2 = c1
        while c2 == c1:
            c2 = list_prime[np.random.randint(0, 5)]
        c3 = np.random.randint(1, 3) * 2
        c4 = c2
        while (c4 == c2) or (c4 == c1):
            c4 = list_prime[np.random.randint(0, 5)]
        q1 = c1 * np.power(c2, c3) * c4
        c5 = c1 * c4
        c6 = c1 * c4 * 4
        c7 = c1 * c4 * 9
        q2 = c7 + 1
        while (q2 % 10) != 0:
            q2 += 1

        a1 = 3

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7)
    return stem, answer, comment


def realnum311_Stem_074():
    stem = "$$수식$$sqrt{{ {{ {q1} }} over {{ {q2} }}x }}$$/수식$$가 자연수가 되도록 하는 가장 작은 자연수 $$수식$$x$$/수식$$의 값은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${{ {q1} }} over {{ {q2} }}x `=` {{ {c1} `times` {c2}^{{{c3}}} }} over {{ {q2} }} `times` x$$/수식$$이므로\n" \
              "$$수식$$x `=` {c1} `times` {q2} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "따라서 가장 작은 자연수 $$수식$$x$$/수식$$는\n" \
              "$$수식$${c1} `times` {q2} `=` {c4}$$/수식$$\n\n"
   
    q1 = 1000
    while q1 >= 1000:
        list_prime = [2, 3, 5, 7, 11]
        c1 = list_prime[np.random.randint(0, 5)]
        c2 = c1
        while c2 == c1:
            c2 = list_prime[np.random.randint(0, 5)]
        c3 = np.random.randint(1, 3) * 2
        q2 = c2
        while (q2 == c2) or (q2 == c1):
            q2 = list_prime[np.random.randint(0, 5)]
        q1 = np.power(c2, c3) * c1
        c4 = c1 * q2

        a1 = c4

    diff = c1
    s_positive = 0
    while s_positive - (2 * diff) <= 0:
        s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment


def realnum311_Stem_075():
    stem = "$$수식$$sqrt{{ {q1}x }}$$/수식$$가 자연수가 되도록 하는 $$수식$$x$$/수식$$ 중 가장 작은 두 자리의 자연수를 $$수식$$a$$/수식$$, 가장 큰 두 자리의 자연수를 $$수식$$b$$/수식$$라 할 때, $$수식$$a `+` b$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ {q1}x }} `=` sqrt{{ {c1}^{{{c2}}} `times` {c3} `times` x }}$$/수식$$가 자연수가 되려면\n" \
              "$$수식$$x `=` {c3} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "따라서 가장 작은 두 자리의 자연수 $$수식$$a$$/수식$$는\n" \
              "$$수식$$a `=` {c3} `times` {c4}^{{2}} `=` {c5}$$/수식$$\n" \
              "또 가장 큰 두 자리의 자연수 $$수식$$b$$/수식$$는\n" \
              "$$수식$$b `=` {c3} `times` {c6}^{{2}} `=` {c7}$$/수식$$\n" \
              "$$수식$$THEREFORE` a `+` b `=` {c5} `+` {c7} `=` {c8}$$/수식$$\n\n"
    q1 = 1000
    while q1 >= 1000:

        list_1 = [2, 3, 7]
        list_2 = [3, 2, 5]
        list_3 = [5, 2, 4]
        list_4 = [7, 2, 3]
        list_5 = [11, 1, 3]
        list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
        c3, c4, c6 = list_A2

        list_prime = [2, 3, 5, 7, 11]
        c1 = c3
        while c1 == c3:
            c1 = list_prime[np.random.randint(0, 5)]
        c2 = np.random.randint(1, 3) * 2
        c5 = c3 * np.power(c4, 2)
        c7 = c3 * np.power(c6, 2)
        c8 = c5 + c7
        q1 = np.power(c1, c2) * c3

        a1 = c8

    stem = stem.format(q1=q1)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8)
    return stem, answer, comment


def realnum311_Stem_076():
    stem = "$$수식$${q1} `LEQ` n `&lt;` {q2}$$/수식$$인 자연수 $$수식$$n$$/수식$$에 대하여 $$수식$$sqrt{{ {q3}n }}$$/수식$$이 자연수가 되도록 하는 $$수식$$n$$/수식$$의 개수는?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${q3}n `=` {c1} `times` {c2}^{{{c3}}} `times` n $$/수식$$이므로 $$수식$$n `=` {c1} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "$$수식$${q1} `LEQ` n `&lt;` {q2}$$/수식$$인 $$수식$$n$$/수식$$은\n" \
              "$$수식$${c1} `times` {{3}}^{{2}} $$/수식$$, $$수식$${c1} `times` {{4}}^{{2}} $$/수식$$, $$수식$${c1} `times` {{5}}^{{2}} $$/수식$$, $$수식$${c1} `times` {{6}}^{{2}} $$/수식$$, $$수식$${c1} `times` {{7}}^{{2}} $$/수식$$\n" \
              "의 5개이다.\n\n"
   
    q3 = 1000
    while q3 >= 1000:
        list_prime = [2, 3, 5, 7, 11]
        c1 = list_prime[np.random.randint(0, 5)]
        c2 = c1
        while c2 == c1:
            c2 = list_prime[np.random.randint(0, 5)]
        c3 = np.random.randint(1, 3) * 2
        q3 = np.power(c2, c3) * c1
        q1 = c1 * 9
        q2 = c1 * 49
        while (q1 % 10) != 0:
            q1 -= 1
        while (q2 % 10) != 0:
            q2 += 1

        a1 = 5

    diff = 1
    s_positive = 0
    while s_positive - (2 * diff) <= 0:
        s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, q3=q3, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_077():
    stem = "$$수식$$sqrt{{ {q1}a }}$$/수식$$가 자연수가 되도록 하는 {q2} 보다 작은 자연수 $$수식$$a$$/수식$$의 개수를 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ {q1}a }} `=` sqrt{{ {c1} `times` {c2}^{{2}} `times` {c3} `times` a }}$$/수식$$가 자연수가 되려면\n" \
              "$$수식$$a `=` {c1} `times` {c3} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "따라서 {q2}보다 작은 자연수 $$수식$$a$$/수식$$는\n" \
              "$$수식$${c1} `times` {c3}$$/수식$$, $$수식$${c1} `times` {c3} `times` 2^{{2}}$$/수식$$, $$수식$${c1} `times` {c3} `times` 3^{{2}}$$/수식$$의 3개이다.\n\n"
    q1 = 5000
    while q1 >= 5000:
        list_prime = [2, 3, 5, 7, 11]
        c1 = list_prime[np.random.randint(0, 5)]
        c2 = c1
        while c2 == c1:
            c2 = list_prime[np.random.randint(0, 5)]
        c3 = c2
        while (c3 == c2) or (c3 == c1):
            c3 = list_prime[np.random.randint(0, 5)]
        q2 = c1 * c3 * 9  
        while (q2 % 10) != 0:
            q2 += 1
        q1 = c1 * c2 * c2 * c3

        a1 = 3

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_078():
    stem = "자연수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$sqrt{{ {{ {q1}a }} over {{ {q2} }} `=` b$$/수식$$일 때, $$수식$$a `+` b$$/수식$$의 값 중 가장 작은 값은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${{ {q1}a }} over {{ {q2} }} `=` {{ {c1}^{{{c2}}} `times` {c3} `times` a }} over {{ {q2} }}$$/수식$$이므로\n" \
              "$$수식$$a `=` {c3} `times` {q2} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "$$수식$$a$$/수식$$의 값이 가장 작을 때, $$수식$$a `+` b$$/수식$$의 값도 가장 작으므로\n" \
              "$$수식$$a `=` {c3} `times` {q2} `=` {c4}$$/수식$$\n" \
              "$$수식$$a `=` {c4}$$/수식$$일 때, $$수식$$b `=` sqrt{{ {c1}^{{{c2}}} `times` {c3}^{{2}} }} `=` sqrt{{ ({c1} `times` {c3})^{{2}} }} `=` {c5}$$/수식$$\n" \
              "$$수식$$THEREFORE` a `+` b `=` {c6}$$/수식$$\n\n"
   
    q1 = 1000
    while q1 >= 1000:
        list_prime = [2, 3, 5, 7, 11]
        c1 = list_prime[np.random.randint(0, 5)]
        c3 = c1
        while c3 == c1:
            c3 = list_prime[np.random.randint(0, 5)]
        q2 = c3
        while (q2 == c3) or (q2 == c1):
            q2 = list_prime[np.random.randint(0, 5)]
        c2 = np.random.randint(1, 3) * 2

        q1 = np.power(c1, c2) * c3

        c4 = c3 * q2
        c5 = c1 * c3
        c6 = c4 + c5

        a1 = c6

    diff = c3
    t1 = 0
    while t1 - (2 * diff) <= 0:
        t1 = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [t1 - (2 * diff), t1 - diff, t1, t1 + diff, t1 + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    return stem, answer, comment


def realnum311_Stem_079():
    stem = "$$수식$$sqrt{{ {{ {q1} }} over {{ a }}$$/수식$$가 최대의 자연수가 되도록 하는 $$수식$$a$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a$$/수식$$의 값이 최소일 때 $$수식$$sqrt{{ {{ {q1} }} over {{ a }}$$/수식$$의 값이 최대이므로 $$수식$$sqrt{{ {{ {q1} }} over {{ a }}$$/수식$$가 자연수가 되도록 하는 가장 작은 자연수 $$수식$$a$$/수식$$의 값을 구한다.\n" \
              "이때 $$수식$$sqrt{{ {{ {q1} }} over {{ a }} }} `=` sqrt{{ {{ {c1}^{{{c2}}} `times` {c3}^{{{c4}}} }} over {{ a }} }}$$/수식$$이 자연수가 되려면\n" \
              "$$수식$$a `=` {c1} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다. (단, $$수식$$a `LEQ` {q1}$$/수식$$)\n" \
              "따라서 가장 큰 작은 자연수 $$수식$$a$$/수식$$의 값은 {c1}이다.\n\n"
    q1 = 5000
    while q1 >= 5000:
        list_prime = [2, 3, 5, 7, 11]
        c1 = list_prime[np.random.randint(0, 5)]
        c3 = c1
        while c3 == c1:
            c3 = list_prime[np.random.randint(0, 5)]
        c2 = (np.random.randint(1, 3) * 2) + 1
        c4 = np.random.randint(1, 3) * 2

        q1 = np.power(c1, c2) * np.power(c3, c4)

        a1 = c1

    stem = stem.format(q1=q1)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment


def realnum311_Stem_080():
    stem = "$$수식$$sqrt{{ {{ {q1} }} over {{ x }}$$/수식$$이 자연수가 되도록 하는 가장 큰 두 자리 자연수 $$수식$$x$$/수식$$의 값은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${{ {q1} }} over {{ x }} `=` {{ {c1}^{{{c2}}} `times` {c3}^{{{c4}}} `times` {c5} }} over {{ x }}$$/수식$$이므로 $$수식$$x$$/수식$$는 {q1}의 약수이면서\n" \
              "$$수식$${c1} `times` {c5} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "따라서 가장 큰 두 자리 자연수 $$수식$$x$$/수식$$는\n" \
              "$$수식$${c1} `times` {c5} `times` {c6}^{{2}} `=` {c7}$$/수식$$\n\n"
    
    list_1 = [2, 3, 3, 2, 5, 3]
    list_2 = [2, 3, 7, 2, 5, 2]
    list_3 = [3, 3, 2, 2, 5, 2]
    list_4 = [2, 5, 3, 2, 5, 3]
    list_5 = [2, 3, 5, 2, 7, 2]
    list_6 = [2, 3, 3, 2, 11, 2]
    list_7 = [3, 3, 2, 2, 7, 2]

    q1 = 5000
    while q1 >= 5000:
        list_A2 = [list_1, list_2, list_3, list_4, list_5, list_6, list_7][np.random.randint(0, 7)]
        c1, c2, c3, c4, c5, c6 = list_A2

        #c2 += np.random.randint(0, 2) * 2
        c4 += np.random.randint(0, 2) * 2

        q1 = np.power(c1, c2) * np.power(c3, c4) * c5
        c7 = np.power(c1, 1) * np.power(c6, 2) * c5

        a1 = c7

    s_candidates = [c1 * c6, c1 * c1 * c6, c5 * c6, c5 * c5 * c6, c1 * c5 * c6 * c6]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7)
    return stem, answer, comment


def realnum311_Stem_081():
    stem = "$$수식$$sqrt{{ {{ {q1} }} over {{ a }}$$/수식$$과 $$수식$$sqrt{{ {q2}a }}$$/수식$$가 자연수가 되게 하는 모든 자연수 $$수식$$a$$/수식$$의 값의 합은?\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "{q1}을 소인수분해하면 $$수식$${q1} `=` {c1}^{{2}} `times` {c2}^{{3}}$$/수식$$이므로\n" \
              "$$수식$$sqrt{{ {{ {q1} }} over {{ a }}$$/수식$$이 자연수가 되도록 하는 자연수 $$수식$$a$$/수식$$는\n" \
              "{c2}, $$수식$${c1}^{{2}} `times` {c2}$$/수식$$, $$수식$${c2}^{{3}}$$/수식$$, $$수식$${c1}^{{2}} `times` {c2}^{{3}}$$/수식$$\n" \
              "{q2}를 소인수분해하면 $$수식$${q2} = {c1}^{{2}} `times` {c2}$$/수식$$이므로\n" \
              "$$수식$$sqrt{{ {q2}a }}$$/수식$$가 자연수가 되려면 $$수식$$a `=` {c2} `times` ( 자연수 )^{{2}}$$/수식$$꼴이어야 한다.\n" \
              "따라서 구하는 가장 작은 자연수 $$수식$$a$$/수식$$의 값은 {c2}이다.\n\n"
   
    q1 = 5000
    while q1 >= 5000:
        list_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        c1 = list_prime[np.random.randint(0, 4)]
        c2 = c1
        while c2 == c1:
            c2 = list_prime[np.random.randint(0, 4)]
        q1 = np.power(c1, 2) * np.power(c2, 3)
        q2 = np.power(c1, 2) * c2

    a1 = c2

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2)
    return stem, answer, comment


def realnum311_Stem_082():
    stem = "$$수식$$sqrt{{ {{ {q1} }} over {{ a }}$$/수식$$가 자연수가 되게 하는 모든 자연수 $$수식$$a$$/수식$$의 값의 합은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ {{ {q1} }} over {{ a }} }} `=` sqrt{{ {{ {c1}^{{{c2}}} `times` {c3} }} over {{ a }}$$/수식$$이므로\n" \
              "$$수식$$a$$/수식$$는 {q1}의 약수이면서 $$수식$${c3} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "따라서 자연수 $$수식$$a$$/수식$$는 {c3}, $$수식$${c3} `times` {c1}^{{2}}$$/수식$$, $$수식$${c3} `times` {c1}^{{4}}$$/수식$$이므로 구하는 합은\n" \
              "$$수식$${c3} `+` {c4} `+` {c5} `=` {c6}$$/수식$$\n\n"
   
    q1 = 2000
    while q1 >= 2000:
        list_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        c1 = list_prime[np.random.randint(0, 2)]
        c2 = 4
        c3 = c1
        while c3 == c1:
            c3 = list_prime[np.random.randint(0, 10)]
        q1 = np.power(c1, c2) * c3
        c4 = c3 * np.power(c1, 2)
        c5 = c3 * np.power(c1, 4)
        c6 = c3 + c4 + c5
    a1 = c6
    
    diff = c3
    s_candidates = [0, 0, 0, 0, 0]
    s_candidates[0] = 0
    while s_candidates[0] <= 0:
        t1 = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
        s_candidates = [t1 - (2 * diff), t1 - diff, t1, t1 + diff, t1 + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    return stem, answer, comment


def realnum311_Stem_083():
    stem = "$$수식$$sqrt{{ {{ {q1} }} over {{ x^{{3}} }} }}$$/수식$$이 유리수가 되게 하는 가장 작은 자연수 $$수식$$x$$/수식$$의 값은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${{ {q1} }} over {{ x^{{3}} }} `=` {{ {c1}^{c2} `times` {c3} }} over {{ x^{{3}} }} $$/수식$$이므로\n" \
              "$$수식$$x^{{3}} `=` {c3} `times` ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "이때 $$수식$$x$$/수식$$가 자연수이고 가장 작은 수이어야 하므로\n" \
              "$$수식$$x^{{3}} `=` {c3} `times` {c3}^{{2}} `THEREFORE` x `=` {c3}$$/수식$$\n\n"
   
    q1 = 5000
    while q1 >= 5000:
        list_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        c1 = list_prime[np.random.randint(0, 2)]
        c2 = np.random.randint(1, 3) * 2
        c3 = c1
        while c3 == c1:
            c3 = list_prime[np.random.randint(0, 10)]
        q1 = np.power(c1, c2) * c3

    a1 = c3
    
    diff = c3 // 2
    s_candidates = [0, 0, 0, 0, 0]
    s_candidates[0] = 0
    while s_candidates[0] <= 0:
        t1 = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
        s_candidates = [t1 - (2 * diff), t1 - diff, t1, t1 + diff, t1 + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_084():
    stem = "자연수 $$수식$$m$$/수식$$, $$수식$$n$$/수식$$에 대하여 $$수식$$sqrt{{ {{ {q1} }} over {{m}} }} `=` n$$/수식$$이라 할 때, $$수식$$n$$/수식$$이 될 수 있는 값 중 가장 큰 값은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${{ {q1} }} over {{m}} `=` {{ {c1} `times` {c2}^{{3}} }} over {{m}}$$/수식$$이므로 $$수식$$m$$/수식$$은 {q1}의 약수이면서\n" \
              "$$수식$${c1} `times` {c2} `times ( 자연수 )^{{2}}$$/수식$$ 꼴이어야 한다.\n" \
              "$$수식$$n$$/수식$$의 값이 가장 크려면 $$수식$$m$$/수식$$의 값은 가장 작아야 하므로\n" \
              "$$수식$$n `=` sqrt{{ {{ {q1} }} over {{ {c4} }} }} `=` sqrt{{ {c5} }} `=` {c2}$$/수식$$\n\n"
    q1 = 3000
    while q1 >= 3000:
        list_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        c1 = list_prime[np.random.randint(0, 10)]
        c2 = c1
        while c2 == c1:
            c2 = list_prime[np.random.randint(0, 5)]
        q1 = c1 * np.power(c2, 3)
        c4 = c1 * c2
        c5 = q1 // c4

    a1 = c2
    
    diff = 1
    s_candidates = [0, 0, 0, 0, 0]
    s_candidates[0] = 0
    while s_candidates[0] <= 0:
        t1 = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
        s_candidates = [t1 - (2 * diff), t1 - diff, t1, t1 + diff, t1 + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_085():
    stem = "$$수식$$sqrt{{ {{ {q1} }} over {{x}} }}$$/수식$$이 자연수가 되게 하는 자연수 $$수식$$x$$/수식$$의 값이 중 가장 큰 수와 가장 작은 수의 차는?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ {{ {q1} }} over {{x}} }} `=` sqrt{{ {{ {c1}^{c2} `times` {c3}^{c4} `times` {c5} }} over {{x}} }}$$/수식$$이므로\n" \
              "$$수식$$x `=` {c5} `times` ( 자연수 )^{{2}}$$/수식$$의 꼴이어야 한다.\n" \
              "이 때 {q1}의 약수이면서 가장 작은 자연수 $$수식$$x$$/수식$$는 $$수식$${c5} `times` 1^{{2}} `=` {c5}$$/수식$$이고\n" \
              "가장 큰 자연수 $$수식$$x$$/수식$$는 $$수식$${c1}^{c2} `times` {c3}^{c4} `times` {c5} `=` {q1}$$/수식$$이다.\n" \
              "따라서 $$수식$$x$$/수식$$의 값 중 가장 큰 수와 가장 작은 수의 차는 $$수식$${q1} `-` {c5} `=` {c6}$$/수식$$이다.\n\n"
    q1 = 3000
    while q1 >= 3000:
        list_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        c1 = list_prime[np.random.randint(0, 5)]
        c2 = np.random.randint(1, 3) * 2
        c3 = c1
        while c3 == c1:
            c3 = list_prime[np.random.randint(0, 5)]
        c4 = np.random.randint(1, 3) * 2
        c5 = c3
        while (c5 == c3) or (c5 == c1):
            c5 = list_prime[np.random.randint(0, 5)]
        q1 = np.power(c1, c2) * np.power(c3, c4) * c5

    c6 = q1 - c5
    a1 = c6
    
    diff = np.square(c5)
    t1 = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [t1 - (2 * diff), t1 - diff, t1, t1 + diff, t1 + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    return stem, answer, comment


def realnum311_Stem_086():
    stem = "다음 중 $$수식$$sqrt{{ {q1} `+` x }}$$/수식$$가 자연수가 되도록 하는 자연수 $$수식$$x$$/수식$$의 값이 아닌 것은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${q1} `+` x$$/수식$$가 {q1}보다 큰 $$수식$$( 자연수 )^{{2}}$$/수식$$ 꼴이어야 하므로\n" \
              "$$수식$${q1} `+` x `=`$$/수식$${c1}, {c2}, {c3}, {c4}, {c5}, $$수식$$CDOTS$$/수식$$\n" \
              "$$수식$$x `=`$$/수식$${c6}, {c7}, {c8}, {c9}, {c10}, $$수식$$CDOTS$$/수식$$\n" \
              "따라서 $$수식$$x$$/수식$$의 값이 아닌 것은 {a1}이다.\n\n"

    list_1 = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 169]
    t1 = np.random.randint(1, 7)
    q1 = np.random.randint(list_1[t1 - 1], list_1[t1])
    c1, c2, c3, c4, c5 = list_1[t1:t1 + 5]
    c6, c7, c8, c9, c10 = np.array(list_1[t1:t1 + 5]) - q1
    list_2 = [c6, c7, c8, c9, c10]
    t2 = np.random.randint(0, 5)
    list_2[t2] -= 1 

    a1 = list_2[t2]
    
    s_candidates = list_2
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, a1=a1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10)
    return stem, answer, comment


def realnum311_Stem_087():
    stem = "$$수식$$sqrt{{ {q1} `+` a }} `=` b$$/수식$$라 할 때, $$수식$$b$$/수식$$가 자연수가 되도록 하는 가장 작은 자연수 $$수식$$a$$/수식$$와 그때의 $$수식$$b$$/수식$$에 대하여 $$수식$$a `+` b$$/수식$$의 값은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "{q1}보다 큰 $$수식$$( 자연수 )^{{2}}$$/수식$$ 꼴인 수는\n" \
              "{c1}, {c2}, {c3}, $$수식$$CDOTS$$/수식$$\n" \
              "$$수식$$a$$/수식$$가 가장 작은 자연수이므로\n" \
              "$$수식$${q1} `+` a `=` {c1} `THEREFORE` a = {c4}$$/수식$$\n" \
              "$$수식$$THEREFORE` b `=` sqrt{{ {q1} + a }} `=` sqrt{{ {q1} + {c4} }} `=` sqrt{{ {c1} }} `=` {c5}$$/수식$$\n" \
              "$$수식$$THEREFORE` a `+` b `=` {c6}$$/수식$$\n\n"

    list_1 = [4, 9, 16, 25, 36, 49, 64, 81, 100]
    t1 = np.random.randint(1, 7)
    q1 = np.random.randint(list_1[t1 - 1], list_1[t1])
    c1 = list_1[t1]
    c2 = list_1[t1 + 1]
    c3 = list_1[t1 + 2]
    c4 = c1 - q1
    c5 = int(np.sqrt(c1))
    c6 = c4 + c5

    a1 = c6
    
    t1 = [a1 - 4, a1 - 2, a1, a1 + 2, a1 + 4][np.random.randint(0, 5)]
    s_candidates = [t1 - 4 , t1 - 2, t1, t1 + 2, t1 + 4]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    return stem, answer, comment


def realnum311_Stem_088():
    stem = "$$수식$$sqrt{{ {q1} `+` n }}$$/수식$$이 자연수가 되게 하는 100 이하인 자연수 $$수식$$n$$/수식$$의 개수는?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${q1} `+` n$$/수식$$의 값이 {q1}보다 큰 자연수의 제곱인 수이어야 한다.\n" \
              "이때 $$수식$$n$$/수식$$이 100 이하인 자연수이어야 하므로\n" \
              "$$수식$${q1} `+` n `=` $$/수식$$ {c1}\n" \
              "따라서 $$수식$$n `=` $$/수식$$ {c2}의 {c3}개이다.\n\n"

    list_1 = [4, 9, 16, 25, 36, 49, 64, 81, 100]
    t1 = np.random.randint(1, 6)
    q1 = np.random.randint(list_1[t1], list_1[t1 + 1])
    c1 = str()
    c2 = str()
    ch = 0
    for num in list_1[t1 + 1:]:
        if ch == 0:
            c1 += str(num)
            c2 += str(num - q1)
            ch = 1
        else:
            c1 += ", " + str(num)
            c2 += ", " + str(num - q1)
    c3 = 8 - t1

    a1 = c3
    
    s_candidates = [3, 4, 5, 6, 7]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_089():
    stem = "$$수식$$sqrt{{ {q1} `-` x }}$$/수식$$이 자연수가 되도록 하는 모든 자연수 $$수식$$x$$/수식$$의 값의 합은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${q1} `-` x$$/수식$$가 {q1}보다 작은 $$수식$$( 자연수 )^{{2}}$$/수식$$ 꼴인 수이어야 하므로\n" \
              "$$수식$${q1} `-` x `=` $$/수식$$ {c1}\n" \
              "$$수식$$THEREFORE` x `=` $$/수식$$ {c2}\n" \
              "따라서 모든 자연수 $$수식$$x$$/수식$$의 값의 합은 {c3}이다.\n\n"

    list_1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
    t1 = np.random.randint(3, 10)
    q1 = np.random.randint(list_1[t1] + 1, list_1[t1 + 1] + 1)
    c1 = str()
    c2 = str()
    ch = 0
    c3 = 0
    for num in list_1[:t1 + 1]:
        if ch == 0:
            c1 += str(num)
            c2 += str(q1 - num)
            ch = 1
            c3 += num
        else:
            c1 += ", " + str(num)
            c2 += ", " + str(q1 - num)
            c3 += num

    a1 = c3
    
    t1 = [a1 - 8, a1 - 4, a1, a1 + 4, a1 + 8][np.random.randint(0, 5)]
    s_candidates = [t1 - 8 , t1 - 4, t1, t1 + 4, t1 + 8]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def realnum311_Stem_090():
    stem = "$$수식$$sqrt{{ {q1} `-` x }}$$/수식$$가 정수가 되도록 하는 자연수 $$수식$$x$$/수식$$의 값 중 가장 큰 값과 가장 작은 값의 합은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${q1} `-` x$$/수식$$가 {q1}보다 작은 $$수식$$( 자연수 )^{{2}}$$/수식$$ 꼴인 수 또는 0이어야 하므로\n" \
              "$$수식$${q1} `-` x `=` $$/수식$$ {c1}\n" \
              "$$수식$${q1} `-` x `=` 0 $$/수식$$에서 $$수식$$x `=` {c2}$$/수식$$\n" \
              "$$수식$${q1} `-` x `=` {c3}$$/수식$$에서 $$수식$$x `=` {c4}$$/수식$$\n" \
              "따라서 $$수식$$x$$/수식$$의 값 중 가장 큰 값과 가장 작은 값의 합은 {c5}이다.\n\n"

    list_1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
    t1 = np.random.randint(3, 10)
    q1 = np.random.randint(list_1[t1] + 1, list_1[t1 + 1] + 1)
    c1 = str()
    ch = 0
    for num in ([0] + list_1[:t1 + 1]):
        if ch == 0:
            c1 += str(num)
            ch = 1
        else:
            c1 += ", " + str(num)
    c2 = q1
    c3 = list_1[t1]
    c4 = q1 - c3
    c5 = c2 + c4   

    a1 = c5
    
    t1 = [a1 - 4, a1 - 2, a1, a1 + 2, a1 + 4][np.random.randint(0, 5)]
    s_candidates = [t1 - 4 , t1 - 2, t1, t1 + 2, t1 + 4]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_091():
    stem = "두  수 $$수식$$sqrt{{ {q1}x }}$$/수식$$, $$수식$$sqrt{{ {{ {q2} }} over {{x}} }}$$/수식$$이 모두 자연수가 되도록 하는 가장 작은 두 자리 자연수 $$수식$$x$$/수식$$의 값은?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "(i)$$수식$${q1}x `=` {c1}^{{{c2}}} `times` {c3} `times x$$/수식$$이므로 $$수식$$x `=` {c3} `times` (자연수 )^{{2}}$$/수식$$꼴이어야 한다.\n" \
              "(ii)$$수식$${{ {q2} }} over {{x}} `=` {{ {c1}^{{{c4}}} `times` {c3}^{{{c5}}} }} over {{x}}$$/수식$$이므로 $$수식$$x$$/수식$$는 {q2}의 약수이면서 $$수식$$x `=` {c3} `times` (자연수 )^{{2}}$$/수식$$꼴이어야 한다.\n" \
              "(i), (ii)에서 가장 작은 두 자리 자연수 $$수식$$x$$/수식$$는 $$수식$${c3} `times` {{ {c6} }}^{{2}} `=` {c7}$$/수식$$\n\n"

    q_limit = 1000
    q1 = q_limit
    q2 = q_limit
    while (q1 >= q_limit) or (q2 >= q_limit):
        list_prime = [2, 3, 5, 7]
        list_1 = [[3,2,3],[2,3,2],[2,5,2],[2,7,2],[2,11,1],[2,13,1]]
        c1, c3, c6 = list_1[np.random.randint(0, len(list_1))]
        if c6 == 1:
            c1 = list_prime[np.random.randint(0, len(list_prime))]
        c2 = [2, 4][np.random.randint(0, 2)]
        c4 = [2, 4][np.random.randint(0, 2)]
        c5 = [3, 5][np.random.randint(0, 2)]
        c7 = c3 * np.power(c6, 2)
        q1 = np.power(c1, c2) * c3
        q2 = np.power(c1, c4) * np.power(c3, c5)

    a1 = c7
    
    diff = 4
    s_positive = 0
    while s_positive - (2 * diff) <= 0:
        s_positive = [a1 - (2 * diff), a1 - diff, a1, a1 + diff, a1 + (2 * diff)][np.random.randint(0, 5)]
    s_candidates = [s_positive - (2 * diff), s_positive - diff, s_positive, s_positive + diff, s_positive + (2 * diff)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(q1=q1, q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7)
    return stem, answer, comment



def realnum311_Stem_092():
    stem = "$$수식$$sqrt{{ {q1} `-` x }} `-` sqrt{{ {q2} `+` y }}$$/수식$$가 가장 큰 정수가 되도록 하는 자연수 $$수식$$x$$/수식$$, $$수식$$y$$/수식$$에 대하여 $$수식$$x `+` y$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{{ {q1} `-` x }}$$/수식$$가 가장 큰 정수가 되어야 하므로\n" \
              "$$수식$${q1} `-` x `=` {c1} `THEREFORE` x `=` {c2}$$/수식$$\n" \
              "$$수식$$sqrt{{ {q2} `+` y }}$$/수식$$가 가장 작은 정수가 되어야 하므로\n" \
              "$$수식$${q2} `+` y `=` {c3} `THEREFORE` y `=` {c4}$$/수식$$\n" \
              "$$수식$$THEREFORE` x `+` y `=` {c5}$$/수식$$\n\n"

    t1 = np.random.randint(2, 17)
    t2 = np.random.randint(2, 17)
    c1 = np.square(t1)
    c3 = np.square(t2)
    q1 = np.random.randint(c1 + 1, np.square(t1 + 1) - 1)
    q2 = np.random.randint(np.square(t2 - 1) + 1, c3 - 1)

    c2 = q1 - c1
    c4 = c3 - q2
    c5 = c2 + c4
    a1 = c5

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, a1=a1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def realnum311_Stem_093():
    stem = "서로 다른 두 개의 주사위를 던져 나온 눈의 수를 각각 $$수식$$x$$/수식$$, $$수식$$y$$/수식$$라 할 때, $$수식$$sqrt{{ {q1}xy }}$$/수식$$가 자연수가 될 확률은?\n" \
           "① $$수식$${{1}} over {{36}}$$/수식$$\n" \
           "② $$수식$${{1}} over {{18}}$$/수식$$\n" \
           "③ $$수식$${{1}} over {{12}}$$/수식$$\n" \
           "④ $$수식$${{1}} over {{6}}$$/수식$$\n" \
           "⑤ $$수식$${{1}} over {{3}}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${q1}xy `=` 2^{{ 3 }} `times` {c1}^{{ {c2} }} `times` xy$$/수식$$에서\n" \
              "$$수식$$xy `=` 2 `times` ( 자연수 )^{{ 2 }}$$/수식$$꼴이어야 하므로\n" \
              "$$수식$$xy `=` 2, 2 `times` 2^{{ 2 }}$$/수식$$, $$수식$$2 `times` 3^{{ 2 }} ( BECAUSE` 1 `LEQ` xy `LEQ` 36 )$$/수식$$\n" \
              "따라서 $$수식$$x$$/수식$$, $$수식$$y$$/수식$$의 순서쌍 $$수식$$(x, y )$$/수식$$는\n" \
              "(i) $$수식$$xy = 2$$/수식$$인 경우 : $$수식$$(1, 2 )$$/수식$$, $$수식$$(2, 1 )$$/수식$$의 2개\n" \
              "(ii) $$수식$$xy = 2 `times` 2^{{ 2 }}$$/수식$$인 경우 : $$수식$$(2, 4 )$$/수식$$, $$수식$$(4, 2 )$$/수식$$의 2개\n" \
              "(iii) $$수식$$xy = 2 `times` 3^{{ 2 }}$$/수식$$인 경우 : $$수식$$(3, 6 )$$/수식$$, $$수식$$(6, 3 )$$/수식$$의 2개\n" \
              "이상에서 구하는 확률은 $$수식$$ {{6}} over {{36}} `=` {{1}} over {{6}}$$/수식$$\n\n"
    
    q1 = 7000
    while q1 >= 7000:
        c1 = [3, 5, 7][np.random.randint(0, 3)]
        c2 = np.random.randint(1, 3) * 2
        q1 = np.power(2, 3) * np.power(c1, c2)

    stem = stem.format(q1=q1)
    answer = answer.format(a1=answer_dict[3])
    comment = comment.format(q1=q1, c1=c1, c2=c2)
    return stem, answer, comment


def realnum311_Stem_094():
    stem = "$$수식$$sqrt{{ {q1} over n }}$$/수식$$이 자연수가 되도록 하는 자연수 $$수식$$n$$/수식$$의 개수는?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n" \
              "$$수식$${{ {q1} }} over {{n}} `=` {{ {c1}^{{{c2}}} `times` {c3} `times {c4}^{{{c5}}} }} over {{n}} `=` {{ {c3} `times` {c6}^{{2}} }} over {{n}}$$/수식$$이므로\n" \
              "$$수식$$n `=` {c3} `times` a^{{2}}$$/수식$$ ($$수식$$a$$/수식$$는 {c6}의 약수) 꼴이어야 한다.\n" \
              "$$수식$${c6} = {c1}^{{{c7}}} `times` {c4}^{{{c8}}}$$/수식$$이므로 {c6}의 약수의 개수는\n" \
              "$$수식$$(1 `+` {c7}) `times` (1 `+` {c8}) `=` {c9}$$/수식$$\n" \
              "따라서 자연수 $$수식$$n$$/수식$$의 개수는 {c9}이다.\n\n"
    q1 = 10000
    while (q1 >= 10000):
        c3 = [3, 5, 7, 11][np.random.randint(0, 4)]
        c1 = c3
        while c1 == c3:
            c1 = [2, 3][np.random.randint(0, 2)]
        c4 = c3
        while (c4 == c3) or (c4 == c1):
            c4 = [2, 3, 5, 7][np.random.randint(0, 4)]
        c2 = np.random.randint(1, 3) * 2
        c5 = np.random.randint(1, 3) * 2

        c6 = np.power(c1, c2 // 2) * np.power(c4, c5 // 2)
        c7 = c2 // 2
        c8 = c5 // 2
        c9 = (1 + c7) * (1 + c8)
        q1 = np.power(c1, c2) * c3 * np.power(c4, c5)

        a1 = c9

    s_candidates = [4, 6, 8, 9, 12]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9)
    return stem, answer, comment

def realnum311_Stem_095():
    stem = "$$수식$$ sqrt {lg} {nums} {rg} $$/수식$$이 자연수가 되도록 하는 가장 작은 자연수 $$수식$$n$$/수식$$을 구하시오.\n"
    answer = "(답) $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "{c1}"\
              "$$수식$$=`$$/수식$${c2}"\
              "$$수식$$=`$$/수식$${c3}"\
              "이므로 $$수식$$n `=` {an} `TIMES`  ( 자연수  ) ^2 $$/수식$$ 꼴이어야 한다.\n"\
              "따라서 가장 작은 자연수 $$수식$$n$$/수식$$은 $$수식$${an}$$/수식$$이다.\n\n"

    case = np.random.randint(4, 11)

    c2_list = ["$$수식$$1 TIMES 2 TIMES 3 TIMES 2^2 $$/수식$$\n", "$$수식$$1 TIMES 2 TIMES 3 TIMES 2^2 TIMES 5$$/수식$$\n",
               "$$수식$$1 TIMES 2 TIMES 3 TIMES 2^2 TIMES 5 TIMES (2 TIMES 3 )$$/수식$$\n",
               "$$수식$$1 TIMES 2 TIMES 3 TIMES 2^2 TIMES 5 TIMES (2 TIMES 3 ) TIMES 7$$/수식$$\n",
               "$$수식$$1 TIMES 2 TIMES 3 TIMES 2^2 TIMES 5 TIMES (2 TIMES 3 ) TIMES 7 TIMES 2^3$$/수식$$\n",
               "$$수식$$1 TIMES 2 TIMES 3 TIMES 2^2 TIMES 5 TIMES (2 TIMES 3 ) TIMES 7 TIMES 2^3 TIMES 3^2$$/수식$$\n",
               "$$수식$$1 TIMES 2 TIMES 3 TIMES 2^2 TIMES 5 TIMES (2 TIMES 3 ) TIMES 7 TIMES 2^3 TIMES 3^2 TIMES  ( 2 TIMES 5  )$$/수식$$\n"][case-4]
    c3_list = ["$$수식$$2^3 TIMES 3 $$/수식$$\n", "$$수식$$2^3 TIMES 3 TIMES 5 $$/수식$$\n", "$$수식$$2^4 TIMES 3^2 TIMES 5 $$/수식$$\n",
               "$$수식$$2^4 TIMES 3^2 TIMES 5 TIMES 7$$/수식$$\n", "$$수식$$2^7 TIMES 3^2 TIMES 5 TIMES 7$$/수식$$\n", "$$수식$$2^7 TIMES 3^4 TIMES 5 TIMES 7$$/수식$$\n", "$$수식$$2^8 TIMES 3^4 TIMES 5^2 TIMES 7$$/수식$$\n"][case-4]
    an_list = [6, 30, 5, 35, 70, 70, 7][case-4]


    if case == 4 :
        c1 = "$$수식$$1 TIMES 2 TIMES 3 TIMES 4 $$/수식$$\n"
        nums = "1 TIMES 2 TIMES 3 TIMES 4 TIMES n "
    elif case == 5 :
        c1 = "$$수식$$1 TIMES 2 TIMES 3 TIMES 4 TIMES 5 $$/수식$$\n"
        nums = "1 TIMES 2 TIMES 3 TIMES 4 TIMES 5 TIMES n "
    else :
        c1 = f"$$수식$$1 TIMES 2 TIMES 3 TIMES CDOTS TIMES {case} $$/수식$$\n"
        if case == 6 :
            nums = "1 TIMES 2 TIMES 3 TIMES 4 TIMES 5 TIMES 6 TIMES n"
        elif case == 7 :
            nums = "1 TIMES 2 TIMES 3 TIMES 4 TIMES 5 TIMES 6 TIMES 7 TIMES n "
        else :
            nums = "1 TIMES 2 TIMES 3 TIMES CDOTS "
            for i in range(case-2, case + 1):
                nums += f"TIMES {i} "
            nums += "TIMES n "

    lg = "{"
    rg = "}"
    stem = stem.format(nums = nums, lg = lg, rg = rg)
    answer = answer.format(an = an_list)
    comment = comment.format(c1 = c1, c2 = c2_list, c3 = c3_list, an = an_list)
    return stem, answer, comment


def realnum311_Stem_096():
    stem = "다음은 어느 {s1}의 {s2}{j1} {s3}에 대한 설명이다. $$수식$$n$$/수식$$이 자연수일 때, 이 {s1}의 {s3}의 넓이는?\n" \
           "$$표$$(가) {z1}\n"\
           "(나) {z2}\n"\
           "(다) {z3}$$/표$$\n"\
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "{s2}{j1} {s3}의 한 변의 길이는 각각 $$수식$$sqrt {lg}{a}n{rg}$$/수식$$, $$수식$$sqrt {lg}{b}-n{rg}$$/수식$$이고, 모두 자연수이다.\n"\
              "$$수식$$sqrt {lg}{a}n{rg} `=` sqrt {lg} {n1} TIMES n {rg}$$/수식$$이므로 $$수식$$n`=`{n2} TIMES  ( 자연수  )^2$$/수식$$꼴이어야 한다.\n"\
              "$$수식$${b}-n$$/수식$$은 $$수식$${b}$$/수식$$보다 작은 $$수식$$ ( 자연수  )^2$$/수식$$꼴인 수이어야 하므로\n"\
              "$$수식$${b}-n`=`{n3}$$/수식$$\n"\
              "$$수식$$THEREFORE ~n`=`{n4}$$/수식$$\n"\
              "따라서 $$수식$$n`=`{n}$$/수식$$이므로 {s3}의 넓이는 $$수식$${b} `-` {n} `=` {an}$$/수식$$\n\n"


    s_num = np.random.randint(0, 4)
    s1 = ['병원', '학원', '유치원', '학교'][s_num]
    s2 = ['진료실', '수학반', '달님반', '교무실'][s_num]
    s3 = ['주사실', '국어반', '별님반', '시청각실'][s_num]
    j1 = proc_jo(s2, 2)

    ch = 0
    while (ch == 0):
        tmp = np.random.randint(0, 8)
        a = [6, 8, 12, 18, 20, 24, 27, 28][tmp]
        n1 = ['2 TIMES 3', '2^3', '2^2 TIMES 3', '2 TIMES 3^2', '2^2 TIMES 5', '2^3 TIMES 3', '3^3', '2^2 TIMES 7'][tmp]
        n2 = [6, 2, 3, 2, 5, 6, 3, 7][tmp]

        n = n2 * np.random.randint(1, 4)**2
        an = np.random.randint(3, 10)**2
        b = an + n

        n3 = "1"
        n3_list = [1]
        for i in range(2, int(np.sqrt(b))+1) :
            inum = i**2
            n3 += f", ~{inum}"
            n3_list.append(inum)

        jnum = b - n3_list[0]
        n4 = f"{jnum}"
        n4_list = [jnum]
        for j in range(1, len(n3_list)):
            jnum = b - n3_list[j]
            n4 += f", ~{jnum}"
            n4_list.append(jnum)

        for k in range(len(n4_list)):
            if n4_list[k] != n and n4_list[k]%n2 == 0 and int(np.sqrt(n4_list[k]%2)) == np.sqrt(n4_list[k]%2):
                ch == 2
                break
        if ch == 2 :
            ch = 0
        else :
            ch = 1
    y1 = f"{s2}{j1} {s3} 모두 정사각형이고, 이들의 한 변의 길이는 모두 자연수이다."
    y2 = f"{s2}의 넓이는 $$수식$${a}n$$/수식$$이다."
    y3 = f"{s3}의 넓이는 $$수식$${b}-n$$/수식$$이다."

    lg = "{"
    rg = "}"

    z_candidates = [y1, y2, y3]

    np.random.shuffle(z_candidates)
    [z1, z2, z3] = z_candidates

    an_candidates = [an, an+4, an - 4, an+8, an+12]
    np.random.shuffle(an_candidates)

    [a1, a2, a3, a4, a5] = an_candidates
    correct_idx = 0
    for idx, sdx in enumerate(an_candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break

    stem = stem.format(z1 = z1, z2 = z2, z3 = z3, s1 = s1, s2 = s2, s3 = s3, j1 = j1, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(lg = lg, rg = rg, s2 = s2, s3 = s3, j1 = j1, n = n, n1 = n1, n2 = n2, n3 = n3, n4 = n4, a = a, b = b, an = an)
    return stem, answer, comment


def realnum311_Stem_097():
    stem = "한 자리 자연수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$에 대하여 $$수식$$sqrt{k}a `-` sqrt{m}b `=` c$$/수식$$일 때, " \
           "$$수식$$a`+`b`+`c`$$/수식$$의 값을 구하시오.\n"
    answer = "(답) $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{k}a `=` sqrt{lg}2^{n1} TIMES {n2}^2 TIMES a {rg} $$/수식$$, $$수식$$sqrt{m}b `=` sqrt{lg}{n3}^2 TIMES {n4} TIMES b {rg}$$/수식$$이므로\n"\
              "이때 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$는 한 자리 자연수이므로 $$수식$$a`=`2 TIMES 1^2 `=` 2 $$/수식$$, $$수식$$2 TIMES 2^2 `=` 8$$/수식$$이고, " \
              "$$수식$$b`=`{n4} TIMES 1^2 `=` {n4}$$/수식$$이다.\n"\
              "(ⅰ) $$수식$$ a `=` 2$$/수식$$, $$수식$$b`=`{n4}$$/수식$$일 때,\n"\
              "$$수식$$c`=` sqrt{ak} `-` sqrt{bm} `=` {ak_} `-` {bm_} `=` {c1}$$/수식$$\n"\
              "(ⅱ) $$수식$$ a `=` 8$$/수식$$, $$수식$$b`=`{n4}$$/수식$$일 때,\n"\
              "$$수식$$c`=` sqrt{ak2} `-` sqrt{bm} `=` {ak2_} `-` {bm_} `=` {c2}$$/수식$$\n"\
              "이때 $$수식$$c$$/수식$$는 한 자리 자연수이므로 $$수식$$c `=` {c1}$$/수식$$\n"\
              "따라서 $$수식$$a`=`2$$/수식$$, $$수식$$b`=`{n4}$$/수식$$, $$수식$$c`=`{c1}$$/수식$$이므로 \n"\
              "$$수식$$a`+`b`+`c `=` 2 `+` {n4} `+` {c1} `=` {an}$$/수식$$\n\n"
    c1 = 100
    c2 = 100
    while c1 >= 10 or c2 < 10 or ak < bm:
        n1 = [3, 5][np.random.randint(0, 2)]
        n2 = [3, 5][np.random.randint(0, 2)]
        k = (2**n1)*(n2**2)
        ak = k*2
        ak_ = int(np.sqrt(ak))
        ak2 = k*8
        ak2_ = int(np.sqrt(ak2))

        n3 = [2, 3][np.random.randint(0, 2)]
        n4 = [5, 7][np.random.randint(0, 2)]
        m = (n3**2) * n4
        bm = n4 * m
        bm_ = int(np.sqrt(bm))

        c1 = ak_ - bm_
        c2 = ak2_ - bm_

    an = 2 + n4 + c1
    lg = "{"
    rg = "}"
    stem = stem.format(k = k, m = m)
    answer = answer.format(an = an)
    comment = comment.format(lg = lg, rg = rg, an = an, ak = ak, bm = bm, ak2 = ak2, ak_ = ak_, ak2_ = ak2_, bm_ = bm_, c1 = c1, c2 = c2, n4 = n4, n1 = n1, n2 = n2, n3 = n3, k = k, m = m)
    return stem, answer, comment


def realnum311_Stem_098():
    stem = "다음 중 두 번째로 작은 수는?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "{num1}{h1}\n"\
              "{num2}{h2}\n"\
              "이때 $$수식$$1 over {n1}`&lt;` 1 over {n2}`&lt;` 1 over {c}`&lt;`{a}`&lt;`{e}`$$/수식$$이므로\n"\
              "$$수식$$ sqrt {lg} 1 over {n1} {rg} `&lt;` sqrt {lg} 1 over {n2} {rg} `&lt;` sqrt {lg} 1 over {c} {rg} `&lt;` sqrt {a} `&lt;` sqrt {e}$$/수식$$에서 \n"\
              "$$수식$${n3}`&lt;`{n4}`&lt;` sqrt {lg} 1 over {c} {rg}`&lt;` sqrt {a}`&lt;` sqrt {e}$$/수식$$\n" \
              "따라서 두 번째로 작은 수는 {anum}이다.\n\n"

    a = np.random.randint(2, 10)
    e = np.random.randint(a+1, 20)
    c = np.random.randint(2, 10)

    bk = [4, 5, 8][np.random.randint(0, 3)]
    d = [3, 5, 6, 7][np.random.randint(0, 4)]
    while bk == d or d == c:
        d = [3, 5, 6, 7][np.random.randint(0, 4)]
    b = 1 / bk
    bk2 = bk ** 2
    d2 = d ** 2

    if bk < d :
        n1 = d2
        n2 = bk2
        n3 = f"1 over {d}"
        n4 = b
        an = f"$$수식$${b}$$/수식$$"
    else :
        n1 = bk2
        n2 = d2
        n3 = b
        n4 = f"1 over {d}"
        an = f"$$수식$$1 over {d}$$/수식$$"

    lg = "{"
    rg = "}"
    candidates = [f"$$수식$$sqrt{lg}{a}{rg}$$/수식$$", f"$$수식$${b}$$/수식$$", f"$$수식$$sqrt{lg} 1 over {c} {rg}$$/수식$$", f"$$수식$$1 over {d}$$/수식$$", f"$$수식$$sqrt{lg} {e} {rg}$$/수식$$"]

    np.random.shuffle(candidates)

    [a1, a2, a3, a4, a5] = candidates
    correct_idx = 0
    x_list = []
    n_list = []
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
        if sdx == f"$$수식$${b}$$/수식$$":
            n_list.append(idx)
            x_list.append(b)
        elif sdx == f"$$수식$$1 over {d}$$/수식$$" :
            n_list.append(idx)
            x_list.append(d)


    num1 = answer_dict[n_list[0]]
    num2 = answer_dict[n_list[1]]
    if x_list[0] == b :
        h1 = f"$$수식$${b} `=` 1 over {bk} `=` sqrt{lg} 1 over {bk2} {rg}$$/수식$$"
        h2 = f"$$수식$$1 over {d} `=` sqrt{lg} 1 over {d2} {rg} $$/수식$$"
    else :
        h1 = f"$$수식$$1 over {d} `=` sqrt{lg} 1 over {d2} {rg} $$/수식$$"
        h2 = f"$$수식$${b} `=` 1 over {bk} `=` sqrt{lg} 1 over {bk2} {rg}$$/수식$$"

    stem = stem.format(a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(lg = lg, rg = rg, num1 = num1 , num2 = num2, h1 = h1, h2 = h2, n1 = n1, n2 = n2, c = c, a = a, e = e, n3 = n3, n4 = n4, anum = answer_dict[correct_idx])
    return stem, answer, comment


def realnum311_Stem_099():
    stem = "$$수식$$x`=`{k}$$/수식$$일 때, 다음 중 그 값이 가장 작은 것은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "① $$수식$${z1}$$/수식$$  ② $$수식$${z2}$$/수식$$  ③ $$수식$${z3}$$/수식$$  ④ $$수식$${z4}$$/수식$$  ⑤ $$수식$${z5}$$/수식$$\n"\
              "따라서 가장 작은 것은 {anum}이다.\n\n"
    lg = "{"
    rg = "}"
    y1 = "$$수식$$x$$/수식$$"
    y2 = "$$수식$$x^2$$/수식$$"
    y3 = f"$$수식$$sqrt{lg}x{rg}$$/수식$$"
    y4 = "$$수식$$1 over x$$/수식$$"
    y5 = f"$$수식$$sqrt{lg} 1 over x {rg}"

    k = np.random.randint(2, 10)
    x1 = k
    x2 = k **2
    x3 = f"$$수식$$sqrt{lg}{k}{rg}$$/수식$$"
    x4 = f"$$수식$$1 over {k}$$/수식$$"
    x5 = f"$$수식$$sqrt{lg} 1 over {k} $$/수식$$"

    yx_dict = {y1: x1, y2: x2, y3: x3, y4: x4, y5: x5}
    candidates = [y1, y2, y3, y4, y5]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == "$$수식$$1 over x$$/수식$$" :
            correct_idx = idx
            break

    z1 = yx_dict[a1]
    z2 = yx_dict[a2]
    z3 = yx_dict[a3]
    z4 = yx_dict[a4]
    z5 = yx_dict[a5]

    stem = stem.format(k = k, a1 = a1, a2 = a2, a3 = a3, a4= a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(anum = answer_dict[correct_idx], z1 = z1, z2 = z2, z3 = z3, z4 = z4, z5 =z5)
    return stem, answer, comment


def realnum311_Stem_100():
    stem = "다음 수 중에서 가장 작은 수를 $$수식$$a$$/수식$$, 가장 큰 수를 $$수식$$b$$/수식$$라 할 때, $$수식$$a^2 `-` b^2$$/수식$$의 값은?\n" \
           "$$표$$" \
           "$$수식$${c1}$$/수식$$, $$수식$${c2}$$/수식$$, $$수식$${c3}$$/수식$$, $$수식$${c4}$$/수식$$, $$수식$${c5}$$/수식$$\n"\
           "$$/표$$\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "$$수식$${p_} `=` sqrt{lg}{p2}{rg}$$/수식$$, $$수식$$sqrt{lg}{m} over {n} {rg} `=` sqrt{lg}{mn}{rg}$$/수식$$, " \
              "$$수식$$sqrt{lg}  ( {k}  ) ^2 {rg} `=` sqrt{lg}{k2}{rg}$$/수식$$이고\n"\
              "$$수식$${z1} `&lt;` {z2} `&lt;` {z3} `&lt;` {z4} `&lt;` {z5} $$/수식$$\n"\
              "이므로 $$수식$${y1} `&lt;` {y2} `&lt;` {y3} `&lt;` {y4} `&lt;` {y5} $$/수식$$\n"\
              "$$수식$$THEREFORE ~ {x1} `&lt;` {x2} `&lt;` {x3} `&lt;` {x4} `&lt;` {x5} $$/수식$$\n"\
              "따라서 $$수식$$a`=`{x1}$$/수식$$, $$수식$$b`=`{x5}$$/수식$$이므로 \n"\
              "$$수식$$a^2 `-` b^2 `=`  ( {x1}  ) ^2 `-`  ( {x5}  ) ^2 `=` {x1_} `-` {x5_} `=` {an}$$/수식$$\n\n"
    lg = "{"
    rg = "}"
    mn2 = 1
    x1_ = mn2
    x5_ = mn2
    while x1_ == mn2 or x5_ == mn2 :
        k = np.random.randint(-5, -1)
        l = np.random.randint(2, 9)
        p = np.random.randint(-5, -1)
        while abs(k) == abs(p) :
            p = np.random.randint(-5, -1)
        while l == 4 or abs(k**2) == l**2 or abs(p**2) == l**2:
            l = np.random.randint(2, 9)

        m = np.random.randint(10, 30)
        n = np.random.randint(2, 10)
        while m % n == 0 or (m*10)%n != 0 :
            m = np.random.randint(10, 30)
            n = np.random.randint(2, 10)
        q = np.random.randint(2, 9)
        while q == 4 or l == q or abs(k**2) == q**2 or abs(p**2) == q**2:
            q = np.random.randint(2, 9)

        p2 = p**2
        mn = m / n
        k2 = k**2

        b1 = f"$$수식$$- sqrt {lg} ( {k} )^2 {rg}$$/수식$$"
        b2 = f"$$수식$$- sqrt {lg} {l} {rg}$$/수식$$"
        b3 = f"$$수식$${p}$$/수식$$"
        b4 = f"$$수식$$- sqrt {lg} {m} over {n} {rg}$$/수식$$"
        b5 = f"$$수식$$- sqrt{lg} {q} {rg}$$/수식$$"
        l2 = l ** 2
        p_ = -p
        mn2 = mn**2
        q2 = q**2
        z_list = [l, p2, mn, q, k2]
        zy_dict = {l : f"sqrt {lg} {l} {rg}", k2 : f"sqrt {lg} ( {k} )^2 {rg}", p2 : f"{p_}",
                   mn : f"sqrt {lg} {m} over {n} {rg}", q :f"sqrt{lg} {q} {rg}"}

        zx_dict = {l : f"- sqrt {lg} {l} {rg}", k2 : f"- sqrt {lg} ( {k} )^2 {rg}", p2 : f"{p}",
                   mn : f"- sqrt {lg} {m} over {n} {rg}", q :f"- sqrt{lg} {q} {rg}"}
        xb_dict = {f"- sqrt {lg} {l} {rg}" : l, f"- sqrt {lg} ( {k} )^2 {rg}" : k2, f"{p}" : p2,
                   f"- sqrt {lg} {m} over {n} {rg}" : mn2, f"- sqrt{lg} {q} {rg}" : q}

        z_list.sort()
        z1 = z_list[0]
        z2 = z_list[1]
        z3 = z_list[2]
        z4 = z_list[3]
        z5 = z_list[4]

        y1 = zy_dict[z1]
        y2 = zy_dict[z2]
        y3 = zy_dict[z3]
        y4 = zy_dict[z4]
        y5 = zy_dict[z5]

        x1 = zx_dict[z5]
        x2 = zx_dict[z4]
        x3 = zx_dict[z3]
        x4 = zx_dict[z2]
        x5 = zx_dict[z1]

        x1_ = xb_dict[x1]
        x5_ = xb_dict[x5]

        an = x1_ - x5_


    candidates = [an -2, an, an+2, an+4, an+6]
    c_candidates = [b1, b2, b3, b4, b5]
    np.random.shuffle(c_candidates)
    [c1, c2, c3, c4, c5] = c_candidates


    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break


    stem = stem.format(c1 = c1, c2 = c2, c3 = c3, c4 = c4, c5 = c5, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(lg = lg, rg = rg, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5, p2 = p2, p_ = p_, m = m, n = n, mn = mn, k = k, k2 = k2, z1 = z1, z2 = z2, z3 = z3, z4 = z4, z5 = z5,
                             y1 = y1, y2 = y2, y3 = y3, y4 = y4, y5 = y5, x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5, x1_ = x1_, x5_ = x5_, an = an)
    return stem, answer, comment


def realnum311_Stem_101():
    stem = "$$수식$${m} `&lt;` sqrt{lg}{k}x{rg} `&lt;` {n}$$/수식$${j1} 만족시키는 자연수 $$수식$$x$$/수식$$의 값을 모두 구하시오.\n"\
           "$$수식$${box1}$$/수식$$, $$수식$${box2}$$/수식$$\n"
    answer = "(답) $$수식$${an1}$$/수식$$, $$수식$${an2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${m} `&lt;` sqrt{lg}{k}x{rg} `&lt;` {n}$$/수식$$의 각 변을 제곱하면\n"\
              "$$수식$${m2} `&lt;` {k}x `&lt;` {n2}$$/수식$$\n"\
              "각 변을 $$수식$${k}$$/수식$$로 나누면 $$수식$${mk_} `&lt;` x `&lt;` {nk_}$$/수식$$\n"\
              "따라서 부등식을 만족시키는 자연수 $$수식$$x$$/수식$$는 $$수식$${an1}$$/수식$$, $$수식$${an2}$$/수식$$이다.\n\n"

    box1 = "BOX{````①````}"
    box2 = "BOX{````②````}"
    lg = "{"
    rg = "}"

    k = np.random.randint(2, 6)
    tmp = np.random.randint(0, 2)

    if k == 5 :
        tmp = 1
    if k == 2 :
        m = k
        n = 3
        m2 = m ** 2
        n2 = n ** 2
        mk = m/k
        nk = n/k
        mk_ = 2
        nk_ = "9 over 2"
        an1 = 3
        an2 = 4
    else :
        if tmp == 0 :
            n = k
            n2 = n**2
            m = n
            while m**2/k > n**2/k -2 :
                m = m - 1
            m2 = m **2
            mk = m2 / k
            nk = int(n2 / k)
            if m2 %k == 0 :
                mk_ = int(mk)
            else :
                mk_ = f"{m2} over {k}"
            nk_ = nk
            an1 = nk - 2
            an2 = nk - 1
        else :
            m = k
            m2 = m ** 2
            n = m
            while n**2/k < m**2/k +2 :
                n = n + 1
            n2 = n ** 2
            mk = int(m2 / k)
            nk = n2 / k
            if n2 % k == 0 :
                nk_ = int(nk)
            else :
                nk_ = f"{n2} over {k}"
            mk_ = mk
            an1 = mk + 1
            an2 = mk + 2

    j1 = proc_jo(n, 4)
    stem = stem.format(j1 = j1, lg = lg, rg = rg, m= m, k = k, n = n , box1 = box1, box2 = box2)
    answer = answer.format(an1 = an1, an2 = an2)
    comment = comment.format(lg = lg, rg = rg, an1 = an1, an2 = an2, mk_ = mk_, nk_ = nk_, m =m, n = n, k = k, m2 = m2, n2 = n2)
    return stem, answer, comment


def realnum311_Stem_102():
    stem = "두 수의 대소 관계가 옳은 것을 보기에서 모두 고른 것은?\n"\
           "$$표$$\n" \
           "㈀ $$수식$${x1}$$/수식$$\n"\
           "㈁ $$수식$${x2}$$/수식$$\n"\
           "㈂ $$수식$${x3}$$/수식$$\n"\
           "㈃ $$수식$${x4}$$/수식$$ $$/표$$\n"\
           "① {z1}\n" \
           "② {z2}\n" \
           "③ {z3}\n" \
           "④ {z4}\n" \
           "⑤ {z5}\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "㈀ {y1}\n"\
              "㈁ {y2}\n"\
              "㈂ {y3}\n"\
              "㈃ {y4}\n"\
              "이상에서 옳은 것은 {an1}, {an2}이다.\n\n"

    lg = "{"
    rg = "}"
    n_list = [0, 1, 2, 3]
    n1 = n_list.pop(np.random.randint(len(n_list)))
    n2 = n_list.pop(np.random.randint(len(n_list)))

    # 1번
    a1 = np.random.randint(2, 10)
    a2 = np.random.randint(2, 7)
    a2_ = a2**2
    while a1 == a2_ :
        a2 = np.random.randint(2, 7)
        a2_ = a2 ** 2
    if a1 > a2_ :
        ac1 = a2_
        ac2 = a1
        ch1 = '&gt;'
    else :
        ac1 = a1
        ac2 = a2_
        ch1 = '&lt;'
    if n1 == 0 or n2 == 0 :
        ch1_ = ch1
    else :
        if ch1 == '&gt;' :
            ch1_ = '&lt;'
        else :
            ch1_ = '&gt;'

    ax = f"sqrt{lg}{a1}{rg} `{ch1_}` {a2}"
    ay = f"$$수식$${a2} `=` sqrt{lg}{a2_}{rg}$$/수식$$이고 $$수식$$sqrt{lg}{ac1}{rg} `&lt;` sqrt{lg}{ac2}{rg}$$/수식$$이므로 $$수식$$sqrt{lg}{a1}{rg} `{ch1}` {a2}$$/수식$$"

    # 2번
    b1 = round(np.random.randint(2, 10) / 10, 1)
    b2 = b1
    b1_ = round(b1 ** 2, 2)
    bc1 = b1_
    bc2 = b2
    ch2 = '&lt;'
    if n1 == 1 or n2 == 1 :
        ch2_ = ch2
    else :
        ch2_ = '&gt;'

    bx = f"{b1}`{ch2_}` sqrt{lg}{b2}{rg} "
    by = f"$$수식$${b1} `=` sqrt{lg}{b1_}{rg}$$/수식$$이고 $$수식$$sqrt{lg}{bc1}{rg} `&lt;` sqrt{lg}{bc2}{rg}$$/수식$$이므로 $$수식$$sqrt{lg}{b1}{rg} `{ch2}` {b2}$$/수식$$"

    # 3번
    c1 = np.random.randint(2, 10)
    c2 = np.random.randint(2, 20)
    while c1 == c2 :
        c2 = np.random.randint(2, 20)
    c1_ = c1 ** 2

    if c1_ < c2 :
        ch3 = '&lt;'
    else :
        ch3 = '&gt;'

    if n1 == 2 or n2 == 2 :
        ch3_ = ch3
    else :
        if ch3 == '&lt;':
            ch3_ = '&gt;'
        else :
            ch3_ = '&lt;'
    cx = f"{c1}`-` sqrt{lg}{c2}{rg} `{ch3_}` 0"
    cy = f"$$수식$${c1} `=` sqrt{lg}{c1_}{rg}$$/수식$$이고 $$수식$$sqrt{lg}{c1_}{rg} `{ch3}` sqrt{lg}{c2}{rg}$$/수식$$이므로 $$수식$${c1} `{ch3}` sqrt{lg}{c2}{rg}$$/수식$$\n" \
         f"$$수식$$````````THEREFORE ~{c1} `-` sqrt{lg}{c2}{rg} `{ch3}` 0$$/수식$$"

    # 4번
    d1 = np.random.randint(2, 20)
    d2 = np.random.randint(2, 10)
    while d1 == d2:
        d1 = np.random.randint(2, 20)
    d2_ = d2 ** 2

    if d1 < d2_ :
        ch4 = '&lt;'
    else :
        ch4 = '&gt;'

    if n1 == 3 or n2 == 3 :
        ch4_ = ch4
    else :
        if ch4 == '&lt;':
            ch4_ = '&gt;'
        else:
            ch4_ = '&lt;'

    dx = f"sqrt{lg}{d1}{rg} `-` {d2} `{ch4_}` 0"
    dy = f"$$수식$${d2} `=` sqrt{lg}{d2_}{rg}$$/수식$$이고 $$수식$$sqrt{lg}{d1}{rg} `{ch4}` sqrt{lg}{d2_}{rg}$$/수식$$이므로 $$수식$$sqrt{lg}{d1}{rg} `{ch4}` {d2}$$/수식$$\n" \
         f"$$수식$$````````THEREFORE ~$$/수식$$$$수식$$sqrt{lg}{d1}{rg} `-` {d2} `{ch4}` 0$$/수식$$"

    anx_dict = {0 : ax, 1 : bx, 2 : cx, 3 : dx}
    x_list = [ax, bx, cx, dx]
    xy_dict = {ax : ay, bx : by, cx : cy, dx : dy}
    n_list = [n1, n2]
    n_list.sort()
    #보기
    np.random.shuffle(x_list)
    [x1, x2, x3, x4] = x_list
    # 해설
    y1 = xy_dict[x1]
    y2 = xy_dict[x2]
    y3 = xy_dict[x3]
    y4 = xy_dict[x4]

    # 선택지
    xan_dict = {x1 : "㈀", x2 : "㈁", x3 : "㈂", x4 : "㈃"}
    an_list = [xan_dict[anx_dict[n_list[0]]], xan_dict[anx_dict[n_list[1]]]]
    an_list.sort()
    an1 = an_list[0]
    an2 = an_list[1]

    kan = f"{an1}, {an2}"
    if kan == "㈀, ㈃" :
        k1 = "㈀, ㈃"
    else :
        k1 = "㈀, ㈁"
    k2 = "㈀, ㈂"
    k3 = "㈁, ㈂"
    k4 = "㈁, ㈃"
    k5 = "㈂, ㈃"

    k_candidates = [k1, k2, k3, k4, k5]
    #np.random.shuffle(k_candidates)

    [z1, z2, z3, z4, z5] = k_candidates

    correct_idx = 0
    for idx, sdx in enumerate(k_candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == kan:
            correct_idx = idx
            break
    stem = stem.format(x1 = x1, x2 = x2, x3 = x3, x4 = x4, z1 = z1, z2 = z2, z3 = z3, z4 = z4, z5 = z5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(y1 = y1, y2 = y2, y3= y3, y4 = y4, an1 = an1, an2 = an2)
    return stem, answer, comment


def realnum311_Stem_103():
    stem = "$$수식$$0`&lt;`a`&lt;`1`$$/수식$$일 때, 다음 중 그 값이 가장 큰 것은?\n" \
           "① {a1}\n" \
           "② {a2}\n" \
           "③ {a3}\n" \
           "④ {a4}\n" \
           "⑤ {a5}\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "① $$수식$${z1}$$/수식$$  ② $$수식$${z2}$$/수식$$  ③ $$수식$${z3}$$/수식$$\n"\
              "④ $$수식$${z4}$$/수식$$  ⑤ $$수식$${z5}$$/수식$$\n"\
              "이때 $$수식$$1 over a `&gt;` sqrt {lg} 1 over a {rg}`$$/수식$$이므로 $$수식$$1 over a$$/수식$$의 값이 가장 크다.\n\n"

    lg = "{"
    rg = "}"

    x1 = "$$수식$$a$$/수식$$"
    x2 = "$$수식$$a^2$$/수식$$"
    x3 = f"$$수식$$sqrt{lg}a{rg}$$/수식$$"
    x4 = "$$수식$$1 over a$$/수식$$"
    x5 = f"$$수식$$sqrt{lg} 1 over a {rg}$$/수식$$"

    y1 = "0`&lt;`a`&lt;`1"
    y2 = "0`&lt;`a^2`&lt;`1"
    y3 = f"0`&lt;`sqrt{lg}a{rg}`&lt;`1"
    y4 = "1 over a `&gt;` 1"
    y5 = f"sqrt {lg} 1 over a {rg} `&gt;` 1"

    xy_dict = {x1 : y1, x2 : y2, x3 : y3, x4 : y4, x5 : y5}
    x_candidates = [x1, x2, x3, x4, x5]
    np.random.shuffle(x_candidates)
    [a1, a2, a3, a4, a5] = x_candidates
    z1 = xy_dict[a1]
    z2 = xy_dict[a2]
    z3 = xy_dict[a3]
    z4 = xy_dict[a4]
    z5 = xy_dict[a5]

    correct_idx = 0
    for idx, sdx in enumerate(x_candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == x4:
            correct_idx = idx
            break
    stem = stem.format(a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(z1 = z1, z2 = z2, z3 = z3, z4 = z4, z5 = z5, lg = lg, rg = rg)
    return stem, answer, comment


def realnum311_Stem_104():
    stem = "$$수식$$sqrt {lg}( sqrt {lg}{k}{rg} `-`{m})  ^2{rg} `+` sqrt {lg}( sqrt {lg}{k}{rg} `-`{n})  ^2{rg} `$$/수식$$을 간단히 하면?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{m2} `&lt;` sqrt{k} `&lt;` sqrt{n2}$$/수식$$이므로 $$수식$${m} `&lt;` sqrt{k} `&lt;` {n}$$/수식$$\n"\
              "따라서 $$수식$$sqrt{k} `-`{m}`&gt;`0$$/수식$$, $$수식$$sqrt{k} `-`{n}`&lt;`0$$/수식$$이므로\n"\
              "$$수식$$sqrt {lg}( sqrt {lg}{k}{rg} `-`{m})  ^2{rg} `+` sqrt {lg}( sqrt {lg}{k}{rg} `-`{n})  ^2{rg} `$$/수식$$\n"\
              "$$수식$$=` ( sqrt{k} `-` {m} ) `-` ( sqrt{k} `-` {n} ) $$/수식$$\n"\
              "$$수식$$=` sqrt{k} `-` {m} `-` sqrt{k} `+` {n} `=` {an}$$/수식$$\n\n"

    lg = "{"
    rg = "}"

    m = np.random.randint(1, 10)
    n = m + 1
    m2 = m ** 2
    n2 = n ** 2
    k = np.random.randint(m2+1, n2)
    an = n - m

    candidates = [an, -an, f"2 sqrt {lg}{k}{rg}", f"-2 sqrt {lg}{k}{rg}", f"sqrt{k}"]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break
    stem = stem.format(lg = lg, rg = rg, k = k, m = m, n = n, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(lg = lg, rg = rg, m = m, n = n, k = k, m2 = m2, n2 = n2, an = an)
    return stem, answer, comment


def realnum311_Stem_105():
    stem = "다음 식을 간단히 하면?\n"\
           "$$표$$\n"\
           "sqrt{lg}({m}- sqrt{n} ) ^2{rg} - sqrt{lg}( sqrt {n} -{m}) ^2{rg} + sqrt{lg}(-{m}) ^2{rg}+(- sqrt {n} ) ^2$$/수식$$\n"\
           "$$/표$$\n"\
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt {n} `&lt;` sqrt {m2} `$$/수식$$이므로 $$수식$$sqrt{n} `&lt;` {m}$$/수식$$\n"\
              "따라서 $$수식$${m} `-` sqrt{n} `&gt;` 0$$/수식$$, $$수식$$sqrt{n} `-` {m} `&lt;` 0$$/수식$$이므로\n"\
              "(주어진 식)\n"\
              "$$수식$$=`({m}`-` sqrt {n} )`-`  {lg} -( sqrt {n} `-`{m})  {rg} `+`{m}`+`{n}$$/수식$$\n"\
              "$$수식$$=`({m}`-` sqrt {n} )`+ ( sqrt {n} `-`{m})`+`{m}`+`{n}$$/수식$$\n"\
              "$$수식$$=`{an}$$/수식$$\n\n"

    lg = "{"
    rg = "}"

    n = np.random.randint(2, 10)
    m = np.random.randint(2, 10)
    m2 = m ** 2
    while n >= m2 :
        m = np.random.randint(2, 10)
        m2 = m ** 2
    an = m + n

    candidates = [an, an - 3, an +3, an+6, an+9]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break
    stem = stem.format(lg = lg, rg = rg,m = m, n = n, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(lg = lg, rg = rg, m = m, n = n, an = an, m2 = m2)
    return stem, answer, comment


def realnum311_Stem_106():
    stem = "다음 중 $$수식$${m} `&lt;` sqrt{lg}x{rg} `&lt;` {n}$$/수식$${j1} 만족시키는 자연수 $$수식$$x$$/수식$$가 아닌 것은?\n"\
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "$$수식$${m} `&lt;` sqrt{lg}x{rg} `&lt;` {n}$$/수식$$에서 $$수식$${m} `=` sqrt{m2}$$/수식$$, $$수식$${n} `=` sqrt{n2}$$/수식$$이므로\n"\
              "$$수식$$sqrt{m2} `&lt;` sqrt{lg}x{rg} `&lt;` sqrt{n2} ````````````THEREFORE~{m2}`&lt;``x`&lt;`{n2}$$/수식$$\n"\
              "따라서 보기 중 자연수 $$수식$$x$$/수식$$가 아닌 것은 $$수식$${an}$$/수식$$이다.\n\n"

    lg = "{"
    rg = "}"

    m = np.random.randint(2, 9)
    n = np.random.randint(m+1, 10)
    m2 = m ** 2
    n2 = n ** 2

    an_list = []
    for i in range(m2+1, n2) :
        an_list.append(i)

    an = [m2, n2][np.random.randint(0, 2)]
    candidates = [an_list.pop(np.random.randint(len(an_list))), an_list.pop(np.random.randint(len(an_list))), an_list.pop(np.random.randint(len(an_list))),
                  an_list.pop(np.random.randint(len(an_list))), an]
    candidates.sort()
    [a1, a2, a3, a4, a5] = candidates
    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break
    j1 = proc_jo(n, 4)
    stem = stem.format(j1 = j1, lg = lg, rg = rg,m = m, n = n, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(lg = lg, rg = rg, m = m, n = n, an = an, m2 = m2, n2 = n2)
    return stem, answer, comment


def realnum311_Stem_107():
    stem = "$$수식$$sqrt{k}n `&lt;` {m}$$/수식$${j1} 만족시키는 자연수 $$수식$$n$$/수식$$의 개수를 구하시오.\n"
    answer = "(답) $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt{k}n `&lt;` {m}$$/수식$$에서 $$수식$$ ( sqrt{k}n  )^2 ` &lt;` {m}^2$$/수식$$\n"\
              "$$수식$${k}n `&lt;` {m2} ````````````THEREFORE~ n `&lt;` {m2} over {k}$$/수식$$\n"\
              "따라서 자연수 $$수식$$n$$/수식$$은 {s1}의 $$수식$${an}$$/수식$$개이다.\n\n"

    lg = "{"
    rg = "}"

    k = np.random.randint(2, 6)
    m = np.random.randint(3, 10)
    m2 = m ** 2
    while k >= m :
        m = np.random.randint(3, 10)
        m2 = m ** 2

    s1 = "$$수식$$1"
    n = m2/k
    if n < 6 :
        if m2 % k == 0 :
            n = int(m2/k)-1
        else :
            n = int(m2/k)
        for i in range(2, int(m2/k)+1) :
            s1 += f", ~{i}"
        s1+="$$/수식$$"
        an = n
    else :
        if m2 % k == 0 :
            n = int(m2/k)-1
        else :
            n = int(m2/k)
        s1 = f"$$수식$$1, ~2, ~3, ~CDOTS, ~{n}$$/수식$$"
        an = n
    j1 = proc_jo(m, 4)
    stem = stem.format(j1 = j1, k = k, m = m)
    answer = answer.format(an = an)
    comment = comment.format(k = k, m = m, m2 = m2, s1 = s1, an = an)
    return stem, answer, comment


def realnum311_Stem_108():
    stem = "$$수식$$sqrt {a}`&lt;` sqrt {k}n `LEQ` {b}`$$/수식$${j1} 만족시키는 자연수 $$수식$$n$$/수식$$의 값 중에서 가장 큰 수를 $$수식$$x$$/수식$$, " \
           "가장 작은 수를 $$수식$$y$$/수식$$라 할 때, $$수식$$x`+`y$$/수식$$의 값을 구하시오.\n"
    answer = "(답) $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt {a}`&lt;` sqrt {k}n `LEQ` {b}`$$/수식$$에서 $$수식$${b} `=` sqrt {b2}$$/수식$$이므로\n"\
              "$$수식$$sqrt {a}`&lt;` sqrt {k}n `LEQ` sqrt {b2}`$$/수식$$\n"\
              "$$수식$${a}`&lt;` {k}n `LEQ` {b2}`$$/수식$$\n"\
              "$$수식$$THEREFORE~ {a} over {k} `&lt;` n `LEQ` {b2_k}$$/수식$$\n"\
              "따라서 $$수식$$x`=`{x}$$/수식$$, $$수식$$y`=`{y}$$/수식$$이므로\n"\
              "$$수식$$x`+`y`=`{an}$$/수식$$\n\n"

    k = np.random.randint(2, 6)
    b = k * np.random.randint(2, 4)
    b2 = b ** 2
    b2_k = int(b2/k)
    a = np.random.randint(2, b2)
    while (a/k >= b2) or a % k == 0:
        a = np.random.randint(2, b2)
    x = b2_k
    y =  int(a/k) + 1
    an = x + y
    j1 = proc_jo(b, 4)
    stem = stem.format(j1 = j1, a = a, k = k, b = b)
    answer = answer.format(an = an)
    comment = comment.format(k = k, a = a, b = b, b2 = b2, b2_k = b2_k, x = x, y = y, an = an)
    return stem, answer, comment


def realnum311_Stem_109():
    stem = "$$수식$${a}`&lt;` sqrt {k}n `&lt;`{b}$$/수식$${j1} 만족시키는 모든 자연수 $$수식$$n$$/수식$$의 값의 합은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "$$수식$${a}`&lt;` sqrt {k}n `&lt;`{b}$$/수식$$에서\n"\
              "$$수식$${a}^2`&lt;`  ( sqrt {k}n  )^2 `&lt;`{b}^2$$/수식$$, $$수식$${a2} `&lt;` {k}n `&lt;` {b2}$$/수식$$\n"\
              "$$수식$$THEREFORE~ {a2_k} `&lt;` n `&lt;` {b2_k}$$/수식$$\n"\
              "따라서 자연수 $$수식$$n$$/수식$$는 {s1}이므로 구하는 합은 $$수식$${an}$$/수식$$이다.\n\n"


    a = np.random.randint(2, 6)
    b = a + 1
    k = np.random.randint(2, a+1)
    a2 = a ** 2
    b2 = b ** 2
    a2k = int(a2 / k)
    b2k = int(b2/k)
    if a2%k == 0 :
        a2_k = a2k
    else :
        a2_k = f"{a2} over {k}"

    if b2%k == 0 :
        b2_k = b2k
        b2_k_ = b2k
    else :
        b2_k_ = b2k+1
        b2_k = f"{b2} over {k}"

    s1 = ""
    an = 0

    for i in range(a2k+1, b2_k_) :
        s1 += f"$$수식$${i}$$/수식$$, "
        an += i
    s1 = s1[0:-2]
    candidates = [an, an - 2, an -1, an + 1, an + 2]
    np.random.shuffle(candidates)
    [a1, a_2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break
    j1 = proc_jo(b, 4)
    stem = stem.format(j1 = j1, a = a, k = k, b = b, a1 = a1, a2 = a_2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(a2 = a2, b2 = b2, k = k, a = a, b = b, b2_k = b2_k,a2_k = a2_k, s1 = s1, an = an)
    return stem, answer, comment


def realnum311_Stem_110():
    stem = "-$$수식$$sqrt {m} `&lt;`- sqrt {lg}{a}x`{op}`{b}{rg} `&lt;`-{n}`$$/수식$${j1} 만족시키는 모든 자연수 $$수식$$x$$/수식$$의 값의 합은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "-$$수식$$sqrt {m} `&lt;`- sqrt {lg}{a}x`{op}`{b}{rg} `&lt;`-{n}`$$/수식$$에서\n"\
              "$$수식$${n} `&lt;`sqrt {lg}{a}x`{op}`{b}{rg} `&lt;`sqrt {m}`$$/수식$$\n"\
              "$$수식$${n}^2 `&lt;`  ( sqrt {lg}{a}x`{op}`{b}{rg}  )^2 `&lt;`  ( sqrt {m}  ) ^2`$$/수식$$\n"\
              "$$수식$${n2} `&lt;` {a}x`{op}`{b} `&lt;`{m} ````````````THEREFORE~ {n2b_a} `&lt;` x `&lt;` {mb_a}$$/수식$$\n"\
              "따라서 자연수 $$수식$$x$$/수식$$는 {s1}이므로 구하는 합은 $$수식$${an}$$/수식$$이다.\n\n"


    n = np.random.randint(2, 6)
    n2 = n ** 2
    m = np.random.randint(n2+2, 30)
    a = np.random.randint(2, 6)
    b = np.random.randint(-2, 3)
    while b == 0 :
        b = np.random.randint(-2, 3)
    if b > 0 :
        op = '+'
    else :
        op = ''

    n2b = n2 - b
    mb = m - b
    while int(n2b/a) ==int(mb/a) :
        m = np.random.randint(n2 + 2, 30)
        a = np.random.randint(2, 6)
        b = np.random.randint(-2, 3)
        while b == 0:
            b = np.random.randint(-2, 3)
        if b > 0:
            op = '+'
        else:
            op = ''

        n2b = n2 - b
        mb = m - b
    if n2b % a == 0 :
        n2b_a = int(n2b/a)
    else :
        n2b_a = f"{n2b} over {a}"
    if mb % a == 0 :
        mb_a = int(mb/a)
        mb_a_ = mb_a
    else :
        mb_a = f"{mb} over {a}"
        mb_a_ = int(mb/a)+1

    s1 = ""
    an = 0

    for i in range(int(n2b/a)+1, mb_a_) :
        s1 += f"$$수식$${i}$$/수식$$, "
        an += i
    s1 = s1[0:-2]
    candidates = [an, an - 2, an -1, an + 1, an + 2]
    np.random.shuffle(candidates)
    [a1, a_2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break
    j1 = proc_jo(n, 4)
    lg = "{"
    rg = "}"
    stem = stem.format(op = op, lg = lg, rg = rg, j1 = j1, m = m, a = a, b = b, n = n, a1 = a1, a2 = a_2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(op = op, lg = lg, rg = rg, m = m, n = n, a = a, b = b, n2 = n2, n2b_a = n2b_a, mb_a = mb_a, s1 = s1, an = an)
    return stem, answer, comment


def realnum311_Stem_111():
    stem = "$$수식$$sqrt {lg} {t1} {rg}$$/수식$$이 $$수식$${p}$$/수식$${j1} $$수식$${q}$$/수식$$ 사이의 값이 되도록 하는 자연수 $$수식$$n$$/수식$$의 개수를 구하시오.\n"
    answer = "(답) $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${p} `&lt;` sqrt {lg} {t1} {rg} `&lt;` {q}$$/수식$$에서 $$수식$${p} `=` sqrt{p2}$$/수식$$, $$수식$${q} `=` sqrt{q2}$$/수식$$이므로\n"\
              "$$수식$$sqrt{p2} `&lt;` sqrt {lg} {t1} {rg} `&lt;` sqrt{q2}$$/수식$$, $$수식$$````{p2} `&lt ;` {t1} `&lt;` {q2}$$/수식$$\n"\
              "THEREFORE~ {p2k} `&lt;` n `&lt;` {q2k}$$/수식$$\n"\
              "따라서 자연수 $$수식$$n$$/수식$$은 {s1}의 $$수식$${an}$$/수식$$개이다.\n\n"

    n='n'
    an = 20
    while an > 18 :
        p = np.random.randint(1, 6)
        q = p + np.random.randint(1, 4)
        p2 = p ** 2
        q2 = q ** 2
        k = np.random.randint(2, 4)
        p2k = p2 * k
        q2k = q2 * k

        s1 = ""
        an = 0
        for i in range(p2k+1, q2k) :
            s1 += f"$$수식$${i}$$/수식$$, "
            an += 1
    s1 = s1[0:-2]
    j1 = proc_jo(p, 2)
    lg = "{"
    rg = "}"
    t1="{{%s}over{%s}}"%(n,k)
    stem = stem.format(t1=t1,lg = lg, rg = rg, k = k, p = p, q = q, j1 = j1)
    answer = answer.format(an = an)
    comment = comment.format(p2k = p2k,t1=t1, q2k = q2k, lg = lg, rg =rg, p = p, q= q, k = k, p2 = p2, q2 = q2, an = an, s1 = s1)
    return stem, answer, comment


def realnum311_Stem_112():
    stem = "$$수식$$sqrt {p} `&lt;` x `&lt;` sqrt {q} `$$/수식$${j1} 만족시키는 자연수 $$수식$$x$$/수식$$의 값 중에서 가장 큰 수를 $$수식$$M$$/수식$$, " \
           "가장 작은 수를 $$수식$$m$$/수식$$이라 할 때, $$수식$$M`-`m$$/수식$$의 값은?\n"\
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt {p} `&lt;` x `&lt;` sqrt {q} `$$/수식$$에서 $$수식$$ ( sqrt {p}  ) ^2 `&lt;` x^2 `&lt;`  ( sqrt {q}  )^2 `$$/수식$$\n"\
              "$$수식$$THEREFORE~ {p} `&lt;` x^2 `&lt;` {q} `$$/수식$$\n"\
              "따라서 자연수 $$수식$$x$$/수식$$는 {s1}이므로\n"\
              "$$수식$$M`=`{m1}$$/수식$$, $$수식$$m`=`{m2}$$/수식$$\n"\
              "$$수식$$THEREFORE~ M`-`m `=` {an}$$/수식$$\n\n"

    q_ = np.random.randint(4, 8)
    q = q_**2 +np.random.randint(1, 6)
    p_ = q_ - np.random.randint(2, 4)
    p = p_**2 + np.random.randint(1, 3)

    s1 = ""
    for i in range(p_+1, q_+1) :
        s1 += f"$$수식$${i}$$/수식$$, "
    s1 = s1[0:-2]
    m1 = q_
    m2 = p_+1
    j1 = proc_jo(q, 4)
    an = m1 - m2

    if an == 1 :
        candidates = [an, an + 1, an + 2, an + 3, an + 4]
    else :
        candidates = [an, an - 1, an + 1, an + 2, an + 3]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break
    lg = "{"
    rg = "}"
    stem = stem.format(j1 = j1, p = p, q = q, a1 = a1, a2 = a2, a3 = a3, a4 =a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(p = p, q = q, s1 = s1, m1 = m1, m2 = m2, an = an)
    return stem, answer, comment


def realnum311_Stem_113():
    stem = "부등식 $$수식$$-{p} `&lt;` - sqrt x `&lt;` 0 `$$/수식$$을 만족시키는 자연수 $$수식$$x$$/수식$$중에서 가장 큰 수를 $$수식$$M$$/수식$$, 가장 작은 수를 $$수식$$m$$/수식$$이라 할 때, " \
           "$$수식$$M`+`m$$/수식$$의 값을 구하시오.\n"
    answer = "(답) $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$-{p} `&lt;`- sqrt x `&lt;` 0 `$$/수식$$의 각 변에 $$수식$$-1$$/수식$$을 곱하면\n"\
              "$$수식$$0 `&lt;` sqrt x `&lt;` {p} ````````````````CDOTS CDOTS ㉠$$/수식$$\n"\
              "㉠에서 $$수식$${p} `=` sqrt {p2}$$/수식$$이므로 $$수식$$0 `&lt;` sqrt x `&lt;` sqrt{p2}$$/수식$$\n"\
              "$$수식$$THEREFORE~ 0 `&lt;` x `&lt;` {p2}$$/수식$$\n"\
              "따라서 $$수식$$M`=`{m}$$/수식$$, $$수식$$m`=`1$$/수식$$이므로\n"\
              "$$수식$$M`+`m`=`{an}$$/수식$$\n\n"

    p = np.random.randint(2, 10)
    p2 = p ** 2
    m = p2 - 1
    an = p2
    lg = "{"
    rg = "}"
    stem = stem.format(p = p)
    answer = answer.format(an = an)
    comment = comment.format(p = p, p2 = p2, m = m, an = an)
    return stem, answer, comment


def realnum311_Stem_114():
    stem = "다음 두 부등식을 동시에 만족시키는 모든 자연수 $$수식$$x$$/수식$$의 값의 합은?\n"\
           "$$표$$\n"\
           "$$수식$${p} `&lt;` sqrt x `&lt;` {q}$$/수식$$, $$수식$$sqrt {m} `&lt;` x `&lt;` sqrt {n}$$/수식$$\n$$/표$$\n"\
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "(ⅰ) $$수식$${p} `&lt;` sqrt x `&lt;` {q}$$/수식$$에서 $$수식$${p}^2 `&lt;`  ( sqrt x  )^2 `&lt;` {q}^2$$/수식$$\n"\
              "$$수식$$THEREFORE~ {p2} `&lt;` x `&lt;` {q2}$$/수식$$\n"\
              "따라서 이를 만족시키는 자연수 $$수식$$x$$/수식$$의 값은 {s1}이다.\n"\
              "(ⅱ) $$수식$$sqrt {m} `&lt;` x `&lt;` sqrt {n}$$/수식$$에서\n"\
              "$$수식$$ ( sqrt {m}  )^2 `&lt;` x^2 `&lt;`  ( sqrt {n}  )^2$$/수식$$\n"\
              "$$수식$$THEREFORE~ {m} `&lt;` x^2 `&lt;` {n}$$/수식$$\n"\
              "따라서 이를 만족시키는 자연수 $$수식$$x$$/수식$$의 값은 {s2}이다.\n"\
              "(ⅰ), (ⅱ)에서 두 부등식을 동시에 만족시키는 자연수 $$수식$$x$$/수식$$는 {s3}이므로 구하는 합은 $$수식$${an}$$/수식$$이다.\n\n"

    p = np.random.randint(2, 4)
    q = p + 1
    p2 = p ** 2
    q2 = q ** 2

    s1_list = []
    s1 = ""
    for i in range(p2+1, q2) :
        s1_list.append(i)
        s1 += f"$$수식$${i}$$/수식$$, "
    s1 = s1[0:-2]

    m_ = s1_list.pop(np.random.randint(len(s1_list)))
    s1_list.append(m_)
    while m_ == p2+1 :
        m_ = s1_list.pop(np.random.randint(len(s1_list)))
        s1_list.append(m_)

    m = m_ ** 2 - np.random.randint(1, 4)
    n_ = m_ + np.random.randint(1, 4)
    n = n_ **2 + np.random.randint(1, 5)

    s2 = ""
    s2_list = []
    for i in range(m_, n_+1):
        s2 += f"$$수식$${i}$$/수식$$, "
        s2_list.append(i)
    s2 = s2[0:-2]
    s1_list.sort()

    if s1_list[0] == s2_list[0] :
        snum = s1_list[0]
    else :
        snum = max(s1_list[0], s2_list[0])
    if s1_list[-1] == s2_list[-1] :
        lnum = s1_list[-1]
    else :
        lnum = min(s1_list[-1], s2_list[-1])

    if snum == lnum :
        s3 = f"$$수식$${snum}$$/수식$$"
        an = snum
    else :
        s3 = ""
        an = 0
        for i in range(snum, lnum+1):
            s3 += f"$$수식$${i}$$/수식$$, "
            an += i
        s3 = s3[0:-2]

    candidates = [an, an-2, an -1, an+1, an+2]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break
    stem = stem.format(p = p, q = q, m = m, n = n, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 =a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(p = p, q = q, p2 = p2, q2 = q2, s1 = s1, m = m, n = n, s2 = s2, s3 = s3, an = an)
    return stem, answer, comment


def realnum311_Stem_115():
    stem = "부등식 $$수식$$sqrt {p} `&lt;` x `&lt;` sqrt {q}$$/수식$${j1} 만족시키는 모든 자연수 $$수식$$x$$/수식$$의 값의 합을 구하시오.\n"
    answer = "(답) $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$x`&gt;`0$$/수식$$이므로 $$수식$$x`=` sqrt x^2$$/수식$$\n"\
              "즉, $$수식$$sqrt {p} `&lt;` x `&lt;` sqrt {q}$$/수식$$에서 $$수식$$sqrt {p} `&lt;` sqrt x^2 `&lt;` sqrt {q}$$/수식$$\n"\
              "$$수식$${p} `&lt;` x^2 `&lt;` {q}$$/수식$$\n"\
              "이때 $$수식$$x$$/수식$$는 자연수이므로 $$수식$$x^2 `=` $$/수식$${s1}\n"\
              "따라서 자연수 $$수식$$x$$/수식$$는 {s2}이므로 모든 자연수 $$수식$$x$$/수식$$의 값의 합은 {s3}$$수식$$`=`{an}$$/수식$$\n\n"

    p_ = np.random.randint(2, 6)
    q_ = p_ + np.random.randint(1, 6)
    p = p_ ** 2 - np.random.randint(1, p_)
    q = q_**2 + np.random.randint(1, 5)

    s1 = ""
    s2 = ""
    s3 = ""
    an = 0
    for i in range(p_, q_+1):
        i2 = i ** 2
        s1 += f"$$수식$${i2}$$/수식$$, "
        s2 += f"$$수식$${i}$$/수식$$, "
        s3 += f"$$수식$${i}`+`$$/수식$$"
        an += i
    s1 = s1[0:-2]
    s2 = s2[0:-2]
    s3 = s3[0:-10]
    s3 += "$$/수식$$"
    j1 = proc_jo(q, 4)
    stem = stem.format(j1 = j1, p = p, q = q)
    answer = answer.format(an = an)
    comment = comment.format(p = p, q = q, s1 = s1, s2 = s2, s3 = s3, an = an)
    return stem, answer, comment


def realnum311_Stem_116():
    stem = "$$수식$${p} `LEQ`  sqrt n `&lt;` {q}`$$/수식$${j1} 만족시키는 자연수 $$수식$$n$$/수식$$의 값 중에서 가장 큰 값을 $$수식$$a$$/수식$$, " \
           "가장 작은 값을 $$수식$$b$$/수식$$라 할 때, $$수식$$sqrt {lg} {t1} `TIMES` c {rg}$$/수식$$가 자연수가 되도록 하는 가장 작은 자연수 $$수식$$c$$/수식$$의 값은?\n"\
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "$$수식$${p} `LEQ`  sqrt n `&lt;` {q}`$$/수식$$에서 $$수식$${p}^2 `LEQ`   ( sqrt n  )^2 `&lt;` {q}^2`$$/수식$$\n"\
              "$$수식$$THEREFORE~ {p2} `LEQ` n `&lt;` {q2}$$/수식$$\n"\
              "$$수식$$n$$/수식$$이 자연수이므로 $$수식$$n`=`$$/수식$${s1}\n"\
              "$$수식$$THEREFORE~ a`=`{a}$$/수식$$, $$수식$$b`=`{b}$$/수식$$\n"\
              "$$수식$$sqrt {lg} {t1} `TIMES` c {rg} `=` sqrt {lg} {t2} ` TIMES `c{rg} `=` sqrt {lg} {lg}{s2}{rg} over {b} ` TIMES` c{rg} ``$$/수식$$이므로\n"\
              "$$수식$$c`=`{s3}`TIMES`(자연수)^2$$/수식$$꼴이어야 한다.\n"\
              "따라서 가장 작은 자연수 $$수식$$c$$/수식$$는 $$수식$${s4}{an}$$/수식$$\n\n"

    p = np.random.randint(2, 8)
    q = p+0.5
    p2 = p**2
    q2 = round(q**2,2)

    aa='a'
    bb='b'
    t1="{%s}over{%s}"%(aa,bb)

    s1 = ""
    for i in range(p2, int(q2)+1) :
        s1 += f"$$수식$${i}$$/수식$$, "
    s1 = s1[0:-2]
    a = int(q2)
    b = p2

    t2="{{%s}over{%s}}"%(a,b)

    if p == 2 :
        s2 = "2 `TIMES` 3"
        s3 = s2
        s4 = s3 + "`=`"
        an = a
    elif p == 3 :
        s2 = "2 `TIMES` 2 `TIMES` 3"
        s3 = 3
        an = 3
        s4 = ''
    elif p == 4 :
        s2 = "2 `TIMES` 2 `TIMES` 5"
        s3 = "4 `TIMES` 5"
        an = 20
        s4 = s3 + "="
    elif p == 5 :
        s2 = "2 `TIMES` 3 `TIMES` 5"
        s3 = "5 `TIMES`6"
        an = 30
        s4 = s3 + "`=`"
    elif p == 6 :
        s2 = "2 `TIMES` 3 `TIMES` 7"
        s3 = s2
        an = 42
        s4 = s3 + "`=`"
    elif p == 7 :
        s2 = "2 `TIMES` 2 `TIMES` 2 `TIMES` 7"
        s3 = "2 `TIMES` 7"
        an = 14
        s4 = s3 + "`=`"

    candidates = [[an, an - 1, an + 4, an + 10, an + 15], [an, an-2, an - 1, an+5 ,an+10]][np.random.randint(0, 2)]

    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break
    j1 = proc_jo(q, 4)
    lg = "{"
    rg = "}"
    stem = stem.format(lg = lg, t1=t1,rg = rg, j1 = j1, p = p, q = q, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(t1=t1,t2=t2,s4 = s4, an = an, a = a, b = b, lg = lg, rg = rg, p = p, q = q, s1 = s1, s2 = s2, s3 = s3, p2 = p2, q2 = q2)
    return stem, answer, comment


def realnum311_Stem_117():
    stem = "부등식 $$수식$$-{p}`&lt;`- sqrt {lg}{m}x`-`{n}{rg} `&lt;`-{q}`$$/수식$${j1} 만족시키는 자연수 $$수식$$x$$/수식$$중 $$수식$${k}$$/수식$$의 배수의 합을 구하시오.\n"
    answer = "(답) $$수식$${an}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$-{p}`&lt;`- sqrt {lg}{m}x`-`{n}{rg} `&lt;`-{q}`$$/수식$$의 각 변에 $$수식$$-1$$/수식$$을 곱하면\n"\
              "$$수식$${q}`&lt;`sqrt {lg}{m}x`-`{n}{rg} `&lt;`{p}` ````````````CDOTS CDOTS㉠$$/수식$$\n"\
              "㉠에서 $$수식$${q}`=` sqrt{q2}$$/수식$$, $$수식$${p}`=`sqrt{p2}$$/수식$$이므로\n"\
              "$$수식$$sqrt{q2}`&lt;`sqrt {lg}{m}x`-`{n}{rg} `&lt;` sqrt{p2}$$/수식$$, $$수식$${q2}`&lt;`{m}x`-`{n} `&lt;` {p2}$$/수식$$\n"\
              "$$수식$${q2n}`&lt;`{m}x `&lt;` {p2n} ````````````THEREFORE~ {q2n_m} `&lt;` x `&lt;` {p2n_m}$$/수식$$\n"\
              "따라서 이를 만족시키는 자연수 $$수식$$x$$/수식$$중에서 $$수식$${k}$$/수식$$의 배수는 {s1}이므로\n"\
              "$$수식$${s2}`=`{an}$$/수식$$\n\n"

    count = 0
    while count < 2 :
        q = np.random.randint(3, 6)
        p = np.random.randint(q+1, q+4)
        p2 = p**2
        q2 = q ** 2
        m = [2, 3, 5][np.random.randint(0, 3)]
        n = np.random.randint(1, 4)
        q2n = q2 + n
        p2n = p2 +n

        if q2n%m == 0 :
            q2n_m = int(q2n/m)
            q2n_m_ = q2n_m
        else :
            q2n_m = f"{q2n} over {m}"
            q2n_m_ = int(q2n/m)
        if p2n%m == 0 :
            p2n_m = int(p2n/m)
            p2n_m_ = p2n_m
        else :
            p2n_m = f"{p2n} over {m}"
            p2n_m_ = int(p2n/m)+1

        k = np.random.randint(2, 4)
        count = 0
        s1 = ""
        s2 = ""
        an = 0
        for i in range(q2n_m_+1, p2n_m_):
            if i % k == 0 :
                s1 += f"$$수식$${i}$$/수식$$, "
                s2 += f"{i}`+`"
                count += 1
                an += i

    s1 = s1[0:-2]
    s2 = s2[0:-3]

    j1 = proc_jo(q, 4)
    lg = "{"
    rg = "}"
    stem = stem.format(lg = lg, rg = rg, j1 = j1, p = p, q = q, m = m, n = n, k = k)
    answer = answer.format(an = an)
    comment = comment.format(lg = lg, rg = rg, p = p, q = q, p2 = p2, q2 = q2, m = m, n =n ,p2n = p2n, q2n = q2n, p2n_m = p2n_m, q2n_m = q2n_m, k = k, s1 = s1, s2 = s2, an = an)
    return stem, answer, comment


def realnum311_Stem_118():
    stem = "$$수식$$sqrt {p}$$/수식$$보다 작은 자연수의 개수를 $$수식$$a$$/수식$$, $$수식$$sqrt {q}$$/수식$$보다 작은 자연수의 개수를 $$수식$$b$$/수식$$라 할 때, " \
           "$$수식$$b`-`a$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt {p1} `&lt;` sqrt {p} `&lt;` sqrt {p2} `$$/수식$$이므로\n"\
              "$$수식$${p1_} `&lt;` sqrt {p} `&lt;` {p2_} ````````````THEREFORE~ a`=`{p1_}$$/수식$$\n"\
              "또 $$수식$$sqrt {q1} `&lt;` sqrt {q} `&lt;` sqrt {q2} `$$/수식$$이므로\n"\
              "$$수식$${q1_} `&lt;` sqrt {q} `&lt;` {q2_} ````````````THEREFORE~ b`=`{q1_}$$/수식$$\n"\
              "THEREFORE b`-`a`=`{an}$$/수식$$\n\n"

    p1_ = np.random.randint(3, 6)
    p2_ = p1_+1
    p1 = p1_**2
    p2 = p2_**2
    p = np.random.randint(p1+1, p2)

    q1_ = np.random.randint(p1_+2, p1_+6)
    q2_ = q1_ +1
    q1 = q1_ ** 2
    q2 = q2_**2
    q = np.random.randint(q1+1, q2)
    an = q1_ - p1_

    candidates = [an, an - 2, an -1, an+1, an+2]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break

    stem = stem.format(p = p, q = q, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(p1 = p1, p2 = p2, p = p, p1_ = p1_, p2_ = p2_, q = q, q1 = q1, q2 = q2, q1_ = q1_, q2_ = q2_, an = an)
    return stem, answer, comment


def realnum311_Stem_119():
    stem = "자연수 $$수식$$x$$/수식$$에 대하여 $$수식$$sqrt x$$/수식$$이하의 자연수의 개수를 $$수식$$f(x)`$$/수식$$라 할 때, $$수식$$f({p}) `-` f({q})$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "$$수식$${p1}`=` sqrt {p12} `&lt;` sqrt{p} `&lt;` sqrt{p22} `=` {p2}$$/수식$$이므로 $$수식$$f({p}) `=` {p1}$$/수식$$\n"\
              "또 $$수식$${q1}`=` sqrt{q12} `&lt;` sqrt{q} `&lt;` sqrt{q22} `=` {q2}$$/수식$$이므로 $$수식$$f({q}) `=` {q1}$$/수식$$\n"\
              "$$수식$$THEREFORE~ f({p}) `-` f({q}) `=` {p1} `-` {q1} `=` {an}$$/수식$$\n\n"

    q1 = np.random.randint(2, 10)
    q2 = q1 + 1
    q12 = q1 ** 2
    q22 = q2 ** 2
    q = np.random.randint(q12+1, q22)

    p1 = np.random.randint(10, 21)
    p2 = p1 + 1
    p12 = p1 ** 2
    p22 = p2 ** 2
    p = np.random.randint(p12+1, p22)

    an = p1 - q1

    if an == 1 :
        candidates = [an, an+1, an+2, an+3, an+4]
    elif an == 2 :
        candidates = [[an, an+1, an+2, an+3, an+4], [an, an-1, an+1, an+2, an+3]][np.random.randint(0, 2)]
    else :
        candidates = [[an, an - 2, an -1, an+1, an+2], [an, an+1, an+2, an+3, an+4], [an, an-1, an+1, an+2, an+3]][np.random.randint(0, 3)]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break

    stem = stem.format(p = p, q = q, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(p1 = p1, p12 = p12, p22 = p22, p2 = p2, p = p, q1 = q1, q2 = q2, q12 = q12, q22 = q22, q = q, an = an )
    return stem, answer, comment


def realnum311_Stem_120():
    stem = "자연수 $$수식$$x$$/수식$$에 대하여 $$수식$$sqrt x$$/수식$$이하의 자연수 중 가장 큰 수를 $$수식$$f({m}x-{n})`$$/수식$$라 할 때, " \
           "$$수식$$f({p}) `-` f({q})$$/수식$$의 값은?\n" \
           "① $$수식$${a1}$$/수식$$\n" \
           "② $$수식$${a2}$$/수식$$\n" \
           "③ $$수식$${a3}$$/수식$$\n" \
           "④ $$수식$${a4}$$/수식$$\n" \
           "⑤ $$수식$${a5}$$/수식$$\n"
    answer = "(답) {anum}\n"
    comment = "(해설)\n" \
              "$$수식$${m}x`-`{n}`=`{p}$$/수식$$에서\n"\
              "$$수식$${m}x`=`{pn}````````````THEREFORE~ x`=`{pn_m}$$/수식$$\n"\
              "이때 $$수식$$sqrt{p12} `&lt;` sqrt{pn_m} `&lt;` sqrt{p22}$$/수식$$, 즉 $$수식$${p1}`&lt;` sqrt{pn_m} `&lt;` {p2}$$/수식$$이므로\n"\
              "$$수식$$f({p}) `=` {p1}$$/수식$$\n"\
              "$$수식$${m}x`-`{n}`=`{q}$$/수식$$에서\n"\
              "$$수식$${m}x`=`{qn}````````````THEREFORE~ x`=`{qn_m}$$/수식$$\n"\
              "이때 $$수식$$sqrt{q12} `&lt;` sqrt{qn_m} `&lt;` sqrt{q22}$$/수식$$, 즉 $$수식$${q1} `&lt;` sqrt{qn_m} `&lt;`{q2}$$/수식$$이므로\n"\
              "$$수식$$f({q}) `=` {q1}$$/수식$$\n"\
              "THEREFORE~ f({p}) `-` f({q}) `=` {p1} `-` {q1} `=` {an}$$/수식$$\n\n"

    m = np.random.randint(2, 4)
    n = np.random.randint(1, 4)

    q1 = np.random.randint(2, 10)
    q2 = q1 + 1
    q12 = q1 ** 2
    q22 = q2 ** 2

    qn_m = np.random.randint(q12+1, q22)
    qn = qn_m * m
    q = qn-n

    p1 = np.random.randint(q1+1, 21)
    p2 = p1 + 1
    p12 = p1 ** 2
    p22 = p2 ** 2

    pn_m = np.random.randint(p12 + 1, p22)
    pn = pn_m * m
    p = pn - n

    an = p1 - q1

    if an == 1 :
        candidates = [an, an+1, an+2, an+3, an+4]
    elif an == 2 :
        candidates = [[an, an+1, an+2, an+3, an+4], [an, an-1, an+1, an+2, an+3]][np.random.randint(0, 2)]
    else :
        candidates = [[an, an - 2, an -1, an+1, an+2], [an, an+1, an+2, an+3, an+4], [an, an-1, an+1, an+2, an+3]][np.random.randint(0, 3)]
    np.random.shuffle(candidates)
    [a1, a2, a3, a4, a5] = candidates

    correct_idx = 0
    for idx, sdx in enumerate(candidates):  # [a, b, c] => 0 : a, 1 : b, 2 :c
        if sdx == an:
            correct_idx = idx
            break

    stem = stem.format(p = p, q = q, m = m, n = n, a1 = a1, a2 = a2, a3 = a3, a4 = a4, a5 = a5)
    answer = answer.format(anum = answer_dict[correct_idx])
    comment = comment.format(m = m, n = n, pn = pn, pn_m = pn_m, qn = qn, qn_m = qn_m, p1 = p1, p12 = p12, p22 = p22, p2 = p2, p = p, q1 = q1, q2 = q2, q12 = q12, q22 = q22, q = q, an = an )
    return stem, answer, comment

def realnum311_Stem_121():
    '''3-1-1-158'''
    stem = "자연수 $$수식$$x$$/수식$$에 대하여 $$수식$$sqrt x$$/수식$$ 보다 작은 자연수의 개수를 $$수식$$f(x)$$/수식$$라 할 때," \
           "$$수식$$f(1) + f(2) + f(3) + `CDOTS` + f(n) = {A}$$/수식$${pj} 만족시키는 자연수 $$수식$$n$$/수식$$의 값은?\n" \
           "① $$수식$${s1}$$/수식$$\n" \
           "② $$수식$${s2}$$/수식$$\n" \
           "③ $$수식$${s3}$$/수식$$\n" \
           "④ $$수식$${s4}$$/수식$$\n" \
           "⑤ $$수식$${s5}$$/수식$$\n"

    answer = "(정답) ②\n"

    comment = "(해설)" \
              "$$수식$$f(1)=0$$/수식$$\n" \
              "$$수식$$f(2)=f(3)=f(4)=1$$/수식$$\n" \
              "$$수식$$f(5)=f(6)=f(7)=f(8)=f(9)=2$$/수식$$\n" \
              "$$수식$$f(10)=f(11)=f(12)=f(13)=f(14)=f(15)=f(16)=3$$/수식$$\n" \
              "$$수식$$f(17)=`CDOTS`=f({n})=4$$/수식$$\n" \
              "따라서 $$수식$$f(1)+f(2)+f(3)+`CDOTS`+f({n}) = {A} $$/수식$$\n"

    def f(n):
        return int(math.sqrt(n) - 0.001)

    n = np.random.randint(20, 26)
    A = sum([f(i) for i in range(1, n + 1)])

    pj= proc_jo(A, 3)

    s1 = n - 1
    s2 = n
    s3 = n + 1
    s4 = n + 2
    s5 = n + 3

    stem = stem.format(A=A, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, n=n,pj=pj)
    answer = answer.format(A=A, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, n=n)
    comment = comment.format(A=A, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, n=n)

    return stem, answer, comment


def realnum311_Stem_122():
    '''3-1-1-159'''
    t1='1'
    t2="sqrt a "
    t3="$$수식$${{%s}over{%s}}$$/수식$$"%(t1,t2)

    q = np.array([["$$수식$$ a &gt; 1 over a $$/수식$$","$$수식$$ a &lt; 1 over a $$/수식$$"],
                  ["$$수식$$sqrt a - 1 &gt; 0 $$/수식$$","$$수식$$sqrt a - 1 &lt; 0 $$/수식$$"],
                  ["$$수식$$ a ^ 2 &gt;$$/수식$$ %s "%(t3), "$$수식$$ a ^ 2 &lt;$$/수식$$ %s "%(t3)],
                  ["$$수식$$sqrt{(a-1)^2} = a - 1 $$/수식$$","$$수식$$sqrt(a-1)^2 = 1 - a $$/수식$$"]])

    p = [np.random.randint(2), np.random.randint(2), np.random.randint(2), np.random.randint(2)]
    
    np.random.choice(4,[0,1],replace=True)
    stem = "$$수식$$ 0 &lt; a &lt; 1 $$/수식$$일 때, 보기에서 옳은 것의 개수는?\n"\
           "$$표$$"\
           "보기\n"\
           "(ㄱ)" + q[0,p[0]] + "     "\
           "(ㄴ)" + q[1,p[1]] + "\n"\
           "(ㄷ)" + q[2,p[2]] + "     "\
           "(ㄹ)" + q[3,p[3]] + "\n$$/표$$" \
           "① 0\n" \
           "② 1\n" \
           "③ 2\n" \
           "④ 3\n" \
           "⑤ 4\n"

    answer = "(정답)" + answer_gen(sum(p)) 

    if sum(p):
        comment_1 = f"이상에서 옳은 것은 {comment_gen(p)}의 {sum(p)} 개이다.\n\n"
    else:
        comment_1 = f"이상에서 옳은 것은 없다.\n\n"


    comment = "(ㄱ) $$수식$$ 0 &lt; a &lt; 1 $$/수식$$ 이므로" \
              "     $$수식$$1 over a &gt; 1$$/수식$$\n$$수식$$∴ a &lt; 1 over a $$/수식$$\n" \
              "(ㄴ)$$수식$$ 0 &lt; sqrt a &lt; sqrt 1 $$/수식$$이므로" \
              "     $$수식$$ 0 &lt; sqrt a &lt; 1$$/수식$$\n$$수식$$∴ sqrt a - 1 &lt; 0 $$/수식$$\n" \
              "(ㄷ) $$수식$$ 0 &lt; a^2 &lt; 1 이고, 0 &lt; sqrt a &lt; 1에서 $$/수식$$ %s $$수식$$ &gt; 1$$/수식$$ 이므로 \n"%(t3), \
              "∴ a^2 &lt;$$/수식$$ %s\n"%(t3) ,\
              "(ㄹ) $$수식$$ a-1 &lt; 0 $$/수식$$이므로" \
              "$$수식$$ ∴ sqrt{(a-1)^2} = -(a-1)=1-a $$/수식$$\n" + comment_1

    return stem, answer, comment


def realnum311_Stem_123():
    '''3-1-1-160'''
    stem = "다음 식을 작은 값부터 차례대로 나열할 때, {num} 번째에 오는 식은? (단, $$수식$$ a ` &lt; `1 $$/수식$$)\n" \
           "① {x1}\n" \
           "② {x2}\n" \
           "③ {x3}\n" \
           "④ {x4}\n" \
           "⑤ {x5}\n"

    answer = "(정답) {ans}"

    comment_c = "$$수식$$ a = {1 over 2} $$/수식$$이라 하고 각 식에 대입하여 값을 구한 후 대소를 비교합니다.\n" \
              "$$수식$$ {1 over a} = 2  ,$$/수식$$$$수식$$sqrt a = sqrt{1 over 2},``$$/수식$$$$수식$$sqrt{1 over a} = sqrt {2},  ~{1 over a^2} = 4 $$/수식$$ 이므로\n" \
              "따라서 작은 값부터 차례대로 나열하면 $$수식$$ a`,``$$/수식$$ $$수식$$sqrt {a}`$$/수식$$,  $$수식$$sqrt{1 over a}`,~{1 over a}`,~{1 over {a^2}}$$/수식$$ 이므로\n"
    comment = "{num} 번째에 오는 식은 {xans}이다."

    x1="$$수식$$a$$/수식$$"
    x2="$$수식$$sqrt a$$/수식$$"
    x3="$$수식$$ sqrt{1 over a}$$/수식$$"
    x4="$$수식$$ 1 over a$$/수식$$"
    x5="$$수식$$ 1 over a^2$$/수식$$"

    num_list=["첫", "두", "세", "네", "다섯"]
    num=np.random.choice(num_list)
    if num=="첫":
        a=x1
        xans=x1
    elif num=="두":
        a=x2
        xans=x2
    elif num=="세":
        a=x3
        xans=x3
    elif num=="네":
        a=x4
        xans=x4
    elif num=="다섯":
        a=x5
        xans=x5

    candidates = [x1, x2, x3,x4,x5]
    np.random.shuffle(candidates)

    answer_dict = {
        0: "①",
        1: "②",
        2: "③",
        3: "④",
        4: "⑤"
    }
    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == a:
            correct_idx = idx
            break

    [x1, x2, x3,x4,x5] = candidates

    stem = stem.format(x1=x1,x2=x2,x3=x3,x4=x4,x5=x5,num=num)
    answer = answer.format(ans=answer_dict[correct_idx])
    comment = comment.format(num=num, xans=xans)
    comment=comment_c+comment
    return stem, answer, comment


def realnum311_Stem_124():
    '''3-1-1-161'''
    stem = "$$수식$$ {q1} &lt; p &lt; {q2} $$/수식$$에 대하여 n의 양의 제곱근이 $$수식$$ {a} + p $$/수식$$일 때, " \
           "자연수 n의 값 중 가장 큰 값은?\n" \
           "① $$수식$${s1}$$/수식$$    " \
           "② $$수식$${s2}$$/수식$$    " \
           "③ $$수식$${s3}$$/수식$$    " \
           "④ $$수식$${s4}$$/수식$$    " \
           "⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(정답) ③\n"
    comment = "(해설) $$수식$$n$$/수식$$의 양의 제곱근이 $$수식$${a} + p $$/수식$$ 이므로 \n" \
              "$$수식$$ sqrt n = {a} + p $$/수식$$\n" \
              "$$수식$$ {q1} &lt; p &lt; {q2}$$/수식$$ 이므로\n" \
              "$$수식$$ {q3} &lt; {a} + p &lt; {q4} ~~~~∴{q3} &lt; sqrt n &lt; {q4}$$/수식$$\n" \
              "$$수식$$∴ {q5} &lt; n &lt; {q6}$$/수식$$"\
              "따라서 자연수 n의 값 중 가장 큰 값은 {ans}이다.\n\n"

    n_root = np.random.randint(10, 15)
    n = (n_root + 1) ** 2
    a = np.random.randint(1, 7)
    ans = n-1
    q1 = n_root - a
    q2 = q1 + 1
    q3 = q1 + a
    q4 = q2 + a
    q5 = q3 ** 2
    q6 = q4 ** 2

    s1 = n - 3
    s2 = n - 2
    s3 = n - 1
    s4 = n
    s5 = n + 1

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, n=n, a=a, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, n=n, a=a, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, n=n, a=a, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, ans=ans)

    return stem, answer, comment


def realnum311_Stem_125():
    '''3-1-1-162'''
    stem = "자연수 $$수식$$n$$/수식$$ 에 대하여 $$수식$$ {q1} LEQ {sq} &lt; {q2} $$/수식$${pj} 만족시키는 모든 " \
           "$$수식$$x$$/수식$$의 값의 합은 $$수식$${x}$$/수식$$이다. 이때 $$수식$$n$$/수식$$의 값은? " \
           "(단, $$수식$$nx$$/수식$$는 자연수이다.)\n" \
           "① $$수식$${s1}$$/수식$$     " \
           "② $$수식$${s2}$$/수식$$     " \
           "③ $$수식$${s3}$$/수식$$     " \
           "④ $$수식$${s4}$$/수식$$     " \
           "⑤ $$수식$${s5}$$/수식$$\n"
    
    answer = "(정답) ②\n"
    comment = "(해설) $$수식$$ {q1} LEQ {sq}&lt; {q2} $$/수식$$에서 $$수식$$ {q3} LEQ nx &lt; {q4} $$/수식$$" \
              "이고, $$수식$$ nx $$/수식$$는 자연수이므로\n" \
              "$$수식$$nx`=`{items_a}$$/수식$$\n"\
              "$$수식$$THEREFORE~x`=` {i1} over n`,`{i2} over n`, `CDOTS`,`{i3} over n`,`{i4} over n$$/수식$$\n"\
              "$$수식$${i1} over n`+`{i2} over n`+ `CDOTS`+ {i3} over n`+`{i4} over n`=`{x}$$/수식$$이므로\n"\
              "$$수식$${x_sum} over n`=`{x}$$/수식$$ \t $$수식$$ THEREFORE n `=` {n}  $$/수식$$\n\n"

    nn="nx"
    sq="sqrt{%s}"%(nn)
    q1 = np.random.randint(2, 10)
    q2 = q1+1
    q3 = q1 ** 2
    q4 = q2 ** 2
    items = list(range(q3, q4))
    items_a = list(map(int, items))
    i1=items[0]
    i2=items[1]
    i3=items[-2]
    i4=items[-1]
    x_sum = int(sum(items))
    n_list=[]
    for i in range(1, x_sum + 1):
        if x_sum % i == 0:
            n_list.append(i)
    while True:
        n=np.random.choice(n_list)
        if n!=1 and n!=x_sum:
            break

    x=int(x_sum/n)
    pj=proc_jo(q2,3)

    s1 = n - 1
    s2 = n
    s3 = n +1
    s4 = n +2
    s5 = n + 3

    stem = stem.format(q1=q1, q2=q2, sq=sq, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, x=x,pj=pj)
    comment = comment.format(sq=sq,q1=q1, q2=q2, q3=q3, q4=q4, i1=i1, i2=i2, i3=i3, i4=i4, n=n,x=x, x_sum=x_sum,items_a=items_a)
    return stem, answer, comment


def realnum311_Stem_126():
    '''3-1-1-163'''

    def N(x):
        return int(math.sqrt(2 * x - 1))

    n = np.random.randint(8, 13)
    my_ans = sum([N(i) for i in range(1, n + 1)])

    s1 = my_ans - 6
    s2 = my_ans - 4
    s3 = my_ans - 2
    s4 = my_ans
    s5 = my_ans + 2

    last = n -8
    ttmp="2x-1"
    st="sqrt{%s}"%(ttmp)

    if n == 8:
        comment1 = ""
        comment2 = f"$$수식$$ (1 times 2) + (2 times 2) + (3 times 4) = {1*2 + 2*2 + 3*4}$$/수식$$"
    else:
        comment1 = "$$수식$$ N(9)=N(10)=N(11)=N(12)=4 $$/수식$$\n"
        comment2 = f"$$수식$$ (1 times 2) + (2 times 2) + (3 times 4) + (4 times {last}) = {1*2 + 2*2 + 3*4 + 4* last}$$/수식$$"

    stem = "자연수 $$수식$$ x $$/수식$$에 대하여 $$수식$$ {st} $$/수식$$ 이하의 자연수의 개수를 " \
           "$$수식$$ N(x) $$/수식$$라 할 때, $$수식$$ N(1) + N(2) + `CDOTS` + N({n}) $$/수식$$의 값은?\n" \
           "① $$수식$${s1}$$/수식$$     " \
           "② $$수식$${s2}$$/수식$$     " \
           "③ $$수식$${s3}$$/수식$$     " \
           "④ $$수식$${s4}$$/수식$$     " \
           "⑤ $$수식$${s5}$$/수식$$\n"


    answer = "(정답) ④\n"

    comment = "$$수식$$ N(1)=N(2)=1$$/수식$$\n" \
              "$$수식$$ N(3)=N(4)=2 $$/수식$$\n" \
              "$$수식$$ N(5)=N(6)=N(7)=N(8)=3 $$/수식$$\n" +\
              comment1 +\
              "... \n" \
              f"따라서 (주어진 식) = " + \
              comment2

    stem = stem.format(n=n, st=st, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(n=n, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    comment = comment.format(n=n, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)

    return stem, answer, comment

def realnum311_Stem_127():
    ''' 3-1-1-167 '''
    stem = "다음 정사각형 중 한 변의 길이가 유리수인 것은? \n" \
           "① 넓이가 $$수식$$ {s1} $$/수식$$인 정사각형\n" \
           "② 넓이가 $$수식$$ {s2} $$/수식$$인 정사각형\n" \
           "③ 넓이가 $$수식$$ {s3} $$/수식$$인 정사각형\n" \
           "④ 넓이가 $$수식$$ {s4} $$/수식$$인 정사각형\n" \
           "⑤ 둘레의 길이가 $$수식$$ {s6} sqrt {s5} $$/수식$$인 정사각형\n"
    answer = "(정답) ③\n"
    comment = "(해설) \n" \
              "각 정사각형의 한 변의 길이를 구해 보면 다음과 같다.\n" \
              "① $$수식$$ sqrt {s1} $$/수식$$\n" \
              "② $$수식$$ sqrt {s2} $$/수식$$\n" \
              "③ $$수식$$ sqrt {s3} = {s8} $$/수식$$\n" \
              "④ $$수식$$ sqrt {s4} $$/수식$$\n" \
              "⑤ $$수식$$ {s7} sqrt {s5} $$/수식$$\n\n" 

    def nextSqure(n):
        return 0 if int(math.sqrt(n)) == math.sqrt(n) else 1

    while True:
        s1 = np.random.randint(2,50)
        s2 = np.random.randint(2,50)
        s3 = np.random.randint(2,50)
        s4 = np.random.randint(2,50)
        s5 = np.random.randint(2,10)
        s6 = np.random.randint(2,50)
        if nextSqure(s1)==1 and nextSqure(s2)==1 and nextSqure(s3)==0 and nextSqure(s4)==1 and nextSqure(s5)==1 and s6%4==0 and s1<s2<s3<s4:
            break
    s7=int(s6/4)
    s8=int(math.sqrt(s3))
    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5,s6=s6)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6,s7=s7,s8=s8)
    return stem, answer, comment


def realnum311_Stem_128():
    '''3-1-1-168'''
    stem = "다음 중 순환소수가 아닌 무한소수로 나타내어지는 것을 모두 고르면? (정답 2개)\n" \
           "① $$수식$${tt1}$$/수식$$\n" \
           "② $$수식$$sqrt {left}0.{left}dot{left}{s2}{right}{right}{right}$$/수식$$\n" \
           "③ $$수식$${s3}$$/수식$$의 제곱근\n" \
           "④ 제곱근 $$수식$${s4}$$/수식$$\n" \
           "⑤ $$수식$$sqrt{s5} - sqrt{ss5}$$/수식$$\n"
    answer = "(정답)①,④\n"
    comment = "(해설)" \
              "② $$수식$$sqrt 0.dot{s2} = sqrt {left}4 over 9{right}  = 2 over 3$$/수식$$\n" \
              "③ $$수식$$sqrt{s3} = {ss3} $$/수식$$\n" \
              "⑤ $$수식$$sqrt{s5} - sqrt{ss5} = {bong} - {bongs} $$/수식$$\n"

    s1 = [2, 5, 8, 10, 11][np.random.randint(4)]
    ss1 = [9, 16, 25, 36][np.random.randint(4)]
    s2 = [4][np.random.randint(1)]
    sib = np.random.randint(3)
    s3 = [1.3 ** 2, 1.5 ** 2, 1.7 ** 2, 1.9 ** 2][sib]
    s3 = round(s3, 3)
    s33 = [1.3, 1.5, 1.7, 1.9][sib]
    s4 = [8.1, 6.4, 4.9, 1.6][np.random.randint(3)]
    s5 = [0.04, 0.09, 0.16, 0.25][sib]
    bong = [0.2, 0.3, 0.4, 0.5][sib]
    ss5 = [1, 9, 25, 4][sib]
    bongs = [1, 3, 5, 2][sib]
    left = "{"
    right = "}"

    t1="sqrt %s"%(s1)
    t2="sqrt %s"%(s2)
    tt1="{%s}over{%s}"%(t1,t2)

    stem = stem.format(tt1=tt1,ss1=ss1,t1=t1,t2=t2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, ss5=ss5, ss3=s33, bong=bong, bongs=bongs, left=left, right=right)
    answer = answer.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, ss5=ss5, ss3=s33, bong=bong, bongs=bongs, left=left, right=right)

    return stem, answer, comment


def realnum311_Stem_129():
    '''3-1-1-169'''
    stem = "다음 중 무리수인 것은?\n" \
           "① $$수식$${s1}$$/수식$$\n" \
           "② $$수식$$sqrt {s2}$$/수식$$\n" \
           "③ $$수식$${s3} - sqrt{ss3}$$/수식$$\n" \
           "④ $$수식$$ sqrt 0.dot{s4}$$/수식$$\n" \
           "⑤ $$수식$${tt1}$$/수식$$\n"
    answer = "(정답) ③\n"
    comment = "(해설) \n" \
              "② $$수식$$sqrt{s2} = {ss2} $$/수식$$\n" \
              "④ $$수식$$sqrt 0.dot{s4} = sqrt 4/9  = 2/3$$/수식$$\n"\
              "⑤ $$수식$${tt1} = {bong} $$/수식$$\n"


    s1 = [3.1, 4.5, 6.9, 7.2, 9.9][np.random.randint(4)]
    ss1 = [9, 16, 25, 36][np.random.randint(4)]
    tmp=np.random.randint(4)
    s2 = [144, 169, 361, 400, 16][tmp]
    ss2=[12,13,19,20,4][tmp]
    sib = np.random.randint(4)
    s3 = [1, 2, 3, 4, 5][sib]
    ss3 = [3, 6, 9, 12, 15][sib]
    s4 = [4, 9][np.random.randint(2)]
    s5 = [0.04, 0.09, 0.16, 0.25][sib]
    bong = [0.2, 0.3, 0.4, 0.5][sib]
    ss5 = [1, 9, 25, 4][sib]
    bongs = [1, 3, 5, 2][sib]
    t1="-{%s}^2"%(s5)
    tt1="sqrt{%s}"%(t1)

    stem = stem.format(ss1=ss1, tt1=tt1,s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, ss5=ss5, ss3=ss3, bong=bong, bongs=bongs)
    answer = answer.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    comment = comment.format(s1=s1,ss2=ss2,tt1=tt1, s2=s2, s3=s3, s4=s4, s5=s5, ss5=ss5, ss3=ss3, bong=bong, bongs=bongs)

    return stem, answer, comment


def realnum311_Stem_130():
    '''3-1-1-170'''

    def no_root(n) :
        import random

        bong = [i for i in range(1,n+1) if not i in [1,4,9,16,25,36,49,64,81,100]]
        a = random.choice(bong)
        return a

    a = no_root(100)

    stem = f"$$수식$$a = sqrt{a}$$/수식$$일 때, 다음 중 무리수인 것은?\n" \
           f"① $$수식$$a-sqrt{a}$$/수식$$\n" \
           f"② $$수식$$(-a)^2$$/수식$$\n" \
           f"③ $$수식$$ sqrt {a}a^2 $$/수식$$\n" \
           f"④ $$수식$$ a+{a} $$/수식$$\n" \
           f"⑤ $$수식$$ a^2$$/수식$$\n"
    answer = "(정답) ④\n"
    comment = "(해설) \n" \
              f"① $$수식$$sqrt{a} - sqrt{a} =0$$/수식$$\n" \
              f"② $$수식$$ (-sqrt{a} )^2 = {a} $$/수식$$\n" \
              f"③ $$수식$$ sqrt {a} times(sqrt {a} )^2 = {a} $$/수식$$\n" \
              f"④ $$수식$$ sqrt{a} + {a} $$/수식$$\n" \
              f"⑤ $$수식$$ sqrt {a}^2 `=` {a} $$/수식$$\n"

    stem = stem.format(a=a)
    answer = answer.format()
    comment = comment.format(a=a)

    return stem, answer, comment


def realnum311_Stem_131():
    '''3-1-1-171'''
    import random as rd

    idx = rd.sample(range(10), 1)

    bye = [1,2,3,4,5,6,7,8,9,10]
    bong = len([i for i in bye if (10 <= bye[idx[0]] * i**2) and (bye[idx[0]] * i**2 < 100) ])

    ans = 90-bong
    stem = f"두 자리 자연수 $$수식$$ x $$/수식$$에 대하여 $$수식$$ sqrt {bye[idx[0]]}x $$/수식$$가 무리수가 되도록" \
           " 하는 $$수식$$ x $$/수식$$의 개수는??\n" \
           f"① $$수식$$ {ans - 6} $$/수식$$\n" \
           f"② $$수식$$ {ans - 4} $$/수식$$\n" \
           f"③ $$수식$$ {ans - 2} $$/수식$$\n" \
           f"④ $$수식$$ {ans} $$/수식$$\n" \
           f"⑤ $$수식$$ {ans + 2} $$/수식$$\n"

    answer = "(정답) ④\n"

    comment = "(해설) \n" \
              f"자연수 중에서 제곱꼴인 자연수의 개수는\n" \
              "$$수식$$ 1^2,` 2^2,` 3^2,` 4^2,` 5^2,` 6^2,` 7^2,` 8^2,` 9^2` $$/수식$$\n" \
              f"이 때 여기에 {bye[idx[0]]}을 곱한 값이 100보다 작을 때 주어진 조건을 만족하며 " \
              f"$$수식$$ sqrt {bye[idx[0]]}x $$/수식$$가 유리수가 되도록 한다." \
              f" 따라서 이를 제외하면 $$수식$$ sqrt {bye[idx[0]]}x $$/수식$$가 무리수가 되도록 하는 x의 개수는\n" \
              f"90 - {bong} = {90-bong}"

    return stem, answer, comment


def realnum311_Stem_132():
    '''3-1-1-172'''
    stem = "다음 중 옳지 않은 것은?\n" \
           "① {x1}\n" \
           "② {x2}\n" \
           "③ {x3}\n" \
           "④ {x4}\n" \
           "⑤ {x5}\n"
    answer = "(정답) {ans}\n"
    comment = "(해설) \n {ans} " \
              "$$수식$$ sqrt 25 = 5 $$/수식$$와 같이 근호 안의 수가 유리수의 제곱인 수이면 유리수이다."

    x1="순환소수는 모두 유리수이다."
    x2="무한소수 중에는 유리수인 것도 있다."
    x3="근호를 사용하여 나타낸 수는 모두 무리수이다."
    x4="순환소수가 아닌 무한소수는 모두 무리수이다."
    x5="무리수는 $$수식$$ {정수} over {0이~아닌~정수} $$/수식$$ 꼴로 나타낼 수 있다."

    candidates = [x1, x2, x3,x4,x5]
    np.random.shuffle(candidates)

    answer_dict = {
        0: "①",
        1: "②",
        2: "③",
        3: "④",
        4: "⑤"
    }
    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == x3:
            correct_idx = idx
            break

    [x1, x2, x3,x4,x5] = candidates

    stem = stem.format(x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer = answer.format(ans=answer_dict[correct_idx])
    comment = comment.format(ans=answer_dict[correct_idx])

    return stem, answer, comment


def realnum311_Stem_133():
    '''3-1-1-173'''

    def no_root(n) :
        import random

        bong = [i for i in range(1,n+1) if not i in [1,4,9,16,25,36,49,64,81,100]]
        a = random.choice(bong)
        return a

    stem = "다음 중 $$수식$$ sqrt{a} $$/수식$$에 대한 설명으로 옳지 않은 것은?\n" \
           "① 무리수이다.\n" \
           "② $$수식$$ {a} $$/수식$$ 무한소수 중에는 유리수인 것도 있다.\n" \
           "③ 제곱하면 유리수가 된다.\n" \
           "④ 기약분수로 나타낼 수 있다.\n" \
           "⑤ 순환소수가 아닌 무한소수로 나타내진다. \n"
    answer = "(정답) ④\n"
    comment = "(해설) \n" \
              "④ 무리수는 기약분수로 나타낼 수 없다."

    a = no_root(100)

    stem = stem.format(a=a)
    return stem, answer, comment


def realnum311_Stem_134():
    '''3-1-1-174'''

    import random

    right_idx = random.sample(range(6), 3)
    print(right_idx)
    right = ["유리수가 아닌 수",
             "순환소수가 아닌 무한소수로 나타낼 수 있는 수",
             "분모, 분자가 정수인 분수로 나타낼 수 없는 수 (단, (분모) $$수식$$ not= 0$$/수식$$)",
             "실수 평면 위에 나타낼 수 있는 수",
             "0과 1 사이에 무한히 많이 존재하는 수",
             "무리수를 유리수로 나눈 수"]

    wrong_idx = random.sample(range(4), 2)
    wrong = np.array([["근호를 사용하여 나타낸 수","근호 안의 수가 자연수의 제곱이면 유리수이다."],
                      ["유한소수로 나타낼 수 없는 수","순환소수는 유한소수로 나타낼 수 없지만 유리수이다."],
                      ["제곱하면 유리수가 되는 수", "원주율의 경우는 제곱하여도 무리수이다."],
                      ["자연에서 관찰되지 않는 수", "원주율, 황금비 처럼 많은 무리수가 자연에서 관찰된다."]])

    stem = "무리수에 대한 설명으로 옳은 것은 보기에서 모두 고르면?\n" \
           "㈀ " + right[right_idx[0]] + "\n" \
           "㈁ " + wrong[wrong_idx[0],0] + "\n" \
           "㈂ "+ right[right_idx[1]] + "\n" \
           "㈃ " + wrong[wrong_idx[1],0] + "\n" \
           "㈄ "+ right[right_idx[1]] + "\n" \
           "① ㈀, ㈁\n" \
           "② ㈀, ㈂\n" \
           "③ ㈁, ㈂\n" \
           "④ ㈀, ㈁, ㈂\n" \
           "⑤ ㈀, ㈂, ㈄ \n"
    answer = "(정답) ⑤\n"
    comment = "(해설) \n" \
              "㈁ " + wrong[wrong_idx[0],1] + "\n" \
              "㈃ " + wrong[wrong_idx[1],1] + "\n" \
              "이상에서 옳은 것은 ㈀, ㈂, ㈄이다."

    return stem, answer, comment


def realnum311_Stem_135():
    '''3-1-1-175'''
    stem = "다음 중 □ 안의 수에 해당하는 것은?\n" \
           "$$표$$$$수식$$ 실수 cases {유리수 cases { 정수 cases { 양의~정수 # 0 # 음의~정수}#정수가~아닌~유리수}#{BOX{``````````````````````}}$$/수식$$$$/표$$\n\n\n\n\n\n"
    stem_for_format = "① $$수식$$ sqrt{s1} $$/수식$$\n" \
                      "② $$수식$$ sqrt {s2}over{ss2} $$/수식$$\n" \
                      "③ $$수식$$ sqrt {s3} $$/수식$$\n" \
                      "④ $$수식$$ {s4} - sqrt{ss4} $$/수식$$\n" \
                      "⑤ $$수식$$ - {s5}over sqrt{ss5} $$/수식$$ \n"
    answer = "(정답) ③\n"
    comment = "(해설) \n" \
              "□ 안에 알맞은 것은 무리수이다.\n"

    a_rand = np.random.randint(4)
    a = [2, 3, 5, 7, 11][a_rand]

    s1_rand = np.random.randint(4)
    s1 = [4, 9, 16, 25, 36][s1_rand]
    ss1 = [9, 16, 25, 36][s1_rand]

    s2_rand = np.random.randint(4)
    s2 = [144, 169, 381, 400, 16][s2_rand]
    ss2 = [4, 9, 16, 25, 32][s2_rand]

    s3_rand = np.random.randint(4)
    s3 = [4.8, 7.4, 2.5, 9.9, 12][s3_rand]
    ss3 = [3, 6, 9, 12, 15][s3_rand]

    s4_rand = np.random.randint(4)
    s4 = [2, 3, 5, 7, 9][s4_rand]
    ss4 = [4, 1, 16, 25, 9][s4_rand]

    s5_rand = np.random.randint(4)
    s5 = [2, 4, 6, 8][s5_rand]
    ss5 = [1, 9, 25, 4][s5_rand]

    stem_for_format = stem_for_format.format(s1=s1, ss1=ss1, s2=s2, ss2=ss2, s3=s3, ss3=ss3, s4=s4, ss4=ss4, s5=s5, ss5=ss5, a=a)
    answer = answer.format()
    comment = comment.format(s1=s1, ss1=ss1, s2=s2, ss2=ss2, s3=s3, ss3=ss3, s4=s4, ss4=ss4, s5=s5, ss5=ss5, a=a)
    stem = stem + stem_for_format

    return stem, answer, comment


def realnum311_Stem_136():
    '''3-1-1-176'''

    import numpy as np
    import random as rd

    idx = rd.sample(range(10),5)

    # 10 x 2 size array
    q = np.array([["실수 중 유리수가 아닌 수는 무리수이다.\n","실수 중 유리수가 아닌 수는 무리수가 맞다.\n"],
                 ["모든 실수는 순환소수로 나타낼 수 있다.\n","무리수는 순환소수로 나타낼 수 없다.\n"],
                 ["정수는 유리수가 아니다. \n","정수는 유리수이다. \n"],
                 ["실수 중 무리수가 아닌 수는 정수이다.\n","$$수식$$1 over 2$$/수식$$은 실수이며 무리수가 아니지만 정수이다.\n"],
                 ["정수가 아니면서 유리수인 수는 없다. \n"," $$수식$$1 over 2$$/수식$$은 정수가 아니지만 유리수이다.\n"],
                 ["정수와 또 다른 정수 사이에는 유한한 개수의 무한소수가 있다.\n",
                  "정수와 또 다른 정수 사이에는 무한한 개수의 무한소수가 있다.\n"],
                 ["유리수는 정수에 포함된다.\n"," $$수식$$1 over 2$$/수식$$은 정수에 포함되지 않는다\n"],
                 ["모든 실수는 무리수를 포함하지 않는다.\n"," $$수식$$ sqrt2 $/수식$$는 실수이고 무리수이다\n"],
                 ["무리수 간의 연산으로 정수를 나타낼 수 없다.\n","$$수식$$ sqrt2 $$/수식$$를 제곱한다면 2이다.\n"],
                 ["0은 관습적으로 양의 정수에 포함한다.\n"," 0은 양의 정수, 음에 정수 어디에도 포함되지 않는다.\n"]])

    stem = "다음 중 옳은 것은?\n" \
           "①" + q[idx[0],0] +"" \
           "②" + q[idx[1],0] +"" \
           "③" + q[idx[2],0] +"" \
           "④" + q[idx[3],0] +"" \
           "⑤" + q[idx[4],0] +"" \

    answer = "(정답) ①\n"

    comment = "(해설) \n" \
           "①" + q[idx[0],1] +"" \
           "②" + q[idx[1],1] +"" \
           "③" + q[idx[2],1] +"" \
           "④" + q[idx[3],1] +"" \
           "⑤" + q[idx[4],1] +""

    return stem, answer, comment

def realnum311_Stem_137():
    '''3-1-1-177'''

    import random
    def no_root(n) :
        bong = [i for i in range(1,n+1) if not i in [1,4,9,16,25,36,49,64,81,100]]
        a = random.choice(bong)
        return a

    a = no_root(100)

    idx = random.sample(range(4), 4)

    q = ["무리수이다.\n",
        f"$$수식$$ {math.floor(math.sqrt(a))} $$/수식$$보다 크고 "
        f"$$수식$$ {math.ceil(math.sqrt(a))} $$/수식$$보다 작다.\n",
        "순환하지 않는 무한소수이다. \n",
        "분수 $$수식$$ a over b (a,b는 정수, b not=0 )의 $$/수식$$ 꼴로 나타낼 수 없다. \n"]

    stem = "다음 중 $$수식$$ sqrt{a} $$/수식$$에 대한 설명으로 옳지 않은 것은?\n" \
           "①" + q[idx[0]] + \
           "②" + q[idx[1]] + \
           "③" + q[idx[2]] + \
           "④ 근호를 사용하지 않고 나타낼 수 있다.\n" \
           "⑤" + q[idx[3]]

    answer = "(정답) ④\n"
    comment = "(해설) \n" \
              "④ 근호를 사용하지 않고 나타낼 수 없다."

    stem = stem.format(a=a)
    comment = comment.format(a=a)

    return stem, answer, comment


def realnum311_Stem_138():
    '''3-1-1-182'''

    import numpy as np
    import random as rd

    idx = rd.sample(range(10),5)

    q = np.array([["$$수식$$ a+d $$/수식$$\n","(유리수) + (무리수) = (무리수)이므로 $$수식$$ a+d= $$/수식$$ (무리수)\n"],
          ["$$수식$$ c+d $$/수식$$\n","$$수식$$ c = sqrt{2}, d = -sqrt{2}이면 c+d=0 $$/수식$$\n"],
          ["$$수식$$ a times c $$/수식$$\n","$$수식$$ a=0, c=sqrt2 이면 ac=0 $$/수식$$ \n"],
          ["$$수식$$ 1 over {cd} $$/수식$$\n","$$수식$$ c=sqrt2,  `d=sqrt2 $$/수식$$ 이면, "
                                          "$$수식$$ 1 over cd = 1 over {sqrt2 times sqrt2} = 1 over 2 $$/수식$$\n"],
          ["$$수식$$ c^2 $$/수식$$\n","$$수식$$ c = sqrt2 이면 c^2 = 2 $$/수식$$\n"],
          ["$$수식$$ abcd$$/수식$$\n","$$수식$$ a = 0`$$/수식$$이면 0.\n"],
          ["$$수식$$ c times d over a (a not= 0)$$/수식$$\n","$$수식$$ c = d = sqrt2 이면 유리수이다.$$/수식$$\n"],
          ["$$수식$$ a^c$$/수식$$\n","$$수식$$ a = 0 `$$/수식$$ 이면 0이다.\n"],
          ["$$수식$$ a^b$$/수식$$\n","$$수식$$ 2^1 = 2$$/수식$$\n"],
          ["$$수식$$ c over d $$/수식$$\n","$$수식$$ c = d $$/수식$$이면 1이다.\n"]])

    stem = "두 유리수 a, b와 두 무리수 c, d에 대하여 다음 중 항상 무리수인 것은?\n" \
           "①" + q[idx[0],0] +"" \
           "②" + q[idx[1],0] +"" \
           "③" + q[idx[2],0] +"" \
           "④" + q[idx[3],0] +"" \
           "⑤" + q[idx[4],0] +""

    answer = "(정답) ①\n"

    comment = "(해설) \n" \
           "①" + q[idx[0],1] +"" \
           "②" + q[idx[1],1] +"" \
           "③" + q[idx[2],1] +"" \
           "④" + q[idx[3],1] +"" \
           "⑤" + q[idx[4],1] +"" \
              " 따라서 항상 무리수인 것은 ①이다."

    return stem, answer, comment


def realnum311_Stem_139():
    '''3-1-1-183'''

    a = np.random.randint(16,64)
    bong = math.floor(math.sqrt(a))

    stem = "한 자리 자연수 $$수식$$ f(n) = sqrt {0 dot n} $$/수식$$에 대하여 $$수식$$  $$/수식$$이라 할 때" \
           f"$$수식$$ f(1),f(2),f(3), ... ,f({a})$$/수식$$ 중에서 유리수의 개수를 구하시오.\n"
    answer = f"(정답) {bong}\n"
    comment = "(해설) \n" \
              "$$수식$$ f(n) = sqrt {0 dot n} = sqrt {n over9} = sqrt {n over 3^2} $$/수식$$이므로\n" \
              "$$수식$$sqrt {n over 3^2}$$/수식$$" \
              f"이 유리수가 되도록 하는 $$수식$$ n은 `1^2, 2^2, `...`  {bong}^2`의 {bong}개이다. $$/수식$$\n" \

    return stem, answer, comment


def realnum311_Stem_140():
    '''3-1-1-185'''
    stem = "1 에서 $$수식$${n}$$/수식$$ 까지의 자연수 $$수식$$ n $$/수식$$에 대하여 $$수식$$ sqrt n $$/수식$$이 " \
           "무리수가 되게 하는 수의 개수를 a, $$수식$$ sqrt 2n $$/수식$$이" \
           " 자연수가 되게 하는 수의 개수를 b라 할 때, a-b의 값은?\n" \
           "① $$수식$$ {s1} $$/수식$$\n" \
           "② $$수식$$ {s2} $$/수식$$\n" \
           "③ $$수식$$ {s3} $$/수식$$\n" \
           "④ $$수식$$ {s4} $$/수식$$\n" \
           "⑤ $$수식$$ {s5} $$/수식$$\n"
    answer = "(정답) ④\n"
    comment = "(해설) \n" \
              "$$수식$$ sqrt n $$/수식$$ 이 무리수가 되게 하는 자연수 " \
              "$$수식$$ n $$/수식$$ 은 자연수의 제곱인 수가 아니여야 한다.\n" \
              "이때 , $$수식$$ {ii}^2 ={iis}, {i}^2 ={iss} $$/수식$$ 이므로 $$수식$$ a = {n}-{ii} = {a} $$/수식$$\n" \
              "$$수식$$ sqrt 2n $$/수식$$이 자연수가 되게 하는 자연수 $$수식$$ n $$/수식$$은 \n" \
              "$$수식$$ 2 times 자연수^2 $$/수식$$의 꼴이어야 한다.\n" \
              "이때 $$수식$$ 1 &lt;= x &lt;= {n} $$/수식$$이므로 $$수식$$ 가능한 x은`2 times k^2 $$/수식$$의 꼴이다.\n" \
              "따라서 $$수식$$ 1 &lt;= k &lt;= {b} `이므로` b = {b}$$/수식$$\n" \
              "$$수식$$a - b = {s4} $$/수식$$"

    n = np.random.randint(100, 999)
    a = n
    for i in range(1, n + 1):
        if (i ** 2 <= n):
            a = a - 1
        else:
            break

    ii = i - 1
    iis = ii ** 2
    iss = i ^ 2

    b = 0
    for j in range(1, n + 1):
        if (2 * j ** 2 <= n):
            b = b + 1
        else:
            break

    s1 = a - b - 30
    s2 = a - b - 20
    s3 = a - b - 10
    s4 = a - b
    s5 = a - b + 10

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, a=a, b=b, n=n, ii=ii, iss=iss, i=i, iis=iis)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, a=a, b=b, n=n, ii=ii, iss=iss, i=i, iis=iis)

    return stem, answer, comment


def realnum311_Stem_141():
    '''3-1-1-186'''
    stem = " $$수식$$ {n} $$/수식$$이하의 자연수 $$수식$$ n $$/수식$$에 대하여" \
           "$$수식$$ sqrt n, sqrt 3n, sqrt 5n $$/수식$$ 이 모두 무리수가" \
           " 되도록 하는 $$수식$$ n $$/수식$$의 개수는?\n" \
           "① $$수식$$ {s1} $$/수식$$\n" \
           "② $$수식$$ {s2} $$/수식$$\n" \
           "③ $$수식$$ {s3} $$/수식$$\n" \
           "④ $$수식$$ {s4} $$/수식$$\n" \
           "⑤ $$수식$$ {s5} $$/수식$$\n"
    answer = "(정답) ④\n"
    comment = "(해설) \n" \
              "(ⅰ) $$수식$$ sqrt n $$/수식$$이 유리수가 되도록 하는 $$수식$$ n은`1 times k^2$$/수식$$의 꼴.\n" \
              " 이 경우에 k의 최대값은 {c}\n" \
              "(ⅱ) $$수식$$ sqrt 3n $$/수식$$이 유리수가 되도록 하는 $$수식$$ n은`3 times k^2 $$/수식$$의 꼴.\n" \
              " 이 경우에 k의 최대값은 {b}\n" \
              "(ⅲ) $$수식$$ sqrt 5n $$/수식$$이 유리수가 되도록 하는 $$수식$$ n은`5 times k^2 $$/수식$$의 꼴.\n" \
              " 이 경우에 k의 최대값은 {d}\n" \
              " 이상으로 구하는 값은 $$수식$$ {n} - ({b}+{c}+{d}) = {a} $$/수식$$ "

    def is_integer(x, diff=0.0001):
        if (round(x) - diff <= x) and (x <= round(x) + diff):
            return True
        else:
            return False

    n = np.random.randint(400, 999)

    d = 0
    c = 0
    b = 0
    a = 0
    for i in range(1, n + 1):
        if not is_integer(math.sqrt(i)):
            if not is_integer(math.sqrt(3 * i)):
                if not is_integer(math.sqrt(5 * i)):
                    a = a + 1
                else:
                    d = d + 1
            else:
                b = b + 1
        else:
            c = c + 1

    s1 = round(a / 5)
    s2 = round(a / 3)
    s3 = round(a / 2)
    s4 = a
    s5 = n - 27

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, n=n)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, n=n, a=a, b=b, c=c, d=d)

    return stem, answer, comment


def realnum311_Stem_142():
    '''3-1-1-197'''
    stem = "다음 중 옳지 않은 것은?\n" \
           "① {x1}\n" \
           "② {x2}\n" \
           "③ {x3}\n" \
           "④ {x4}\n" \
           "⑤ {x5}\n"
    answer = "(정답) {ans}\n"
    comment = "(해설) \n {ans} " \
              "수직선은 유리수와 무리수, 즉 실수에 대응하는 점으로 완전히 메울 수 있다."

    x1="모든 유리수는 각각 수직선 위의 한 점에 대응한다."
    x2="실수 중에서 유리수이면서 동시에 무리수인 수는 없다."
    x3="무리수만으로 수직선을 완전히 메울 수 있다."
    x4="서로 다른 두 무리수 사이에는 무수히 많은 무리수가 있다."
    x5="서로 다른 두 무리수 사이에는 무수히 많은 유리수가 있다."

    candidates = [x1, x2, x3,x4,x5]
    np.random.shuffle(candidates)

    answer_dict = {
        0: "①",
        1: "②",
        2: "③",
        3: "④",
        4: "⑤"
    }
    correct_idx = 0
    for idx, sdx in enumerate(candidates):
        if sdx == x3:
            correct_idx = idx
            break

    [x1, x2, x3,x4, x5] = candidates

    stem = stem.format(x1=x1,x2=x2,x3=x3,x4=x4,x5=x5)
    answer = answer.format(ans=answer_dict[correct_idx])
    comment = comment.format(ans=answer_dict[correct_idx])
    return stem, answer, comment


def realnum311_Stem_143():
    '''3-1-1-198'''
    stem = "다음 중 옳은 것을 모두 고르면? (정답 2개)\n" \
           "① $$수식$$ {s1} $$/수식$$에 가장 가까운 유리수를 찾을 수 있다.\n" \
           "② $$수식$$ sqrt{s2} $$/수식$$와 $$수식$$ sqrt{s3} $$/수식$$사이에는 무수히 많은 무리수가 있다.\n" \
           "③ 서로 다른 두 무리수 사이에는 무리수만 있다.\n" \
           "④ $$수식$$ {s4} over 12 $$/수식$$와 $$수식$$ {s5} over 12 $$/수식$$사이에는 3개의 유리수가 있다.\n" \
           "⑤ 실수 중에서 유리수이면서 동시에 무리수인 수는 없다.\n"
    answer = "(정답) ②, ⑤\n"
    comment = "(해설) \n" \
              "① $$수식$$ {s1} $$/수식$$에 가장 가까운 유리수는 찾을 수 없다.\n" \
              "③ 서로 다른 두 무리수 사이에는 무수히 많은 유리수도 있다.\n" \
              "④ $$수식$$ {s4} over 12 $$/수식$$과 $$수식$$ {s5} over 12 $$/수식$$사이에는 무수히 많은 유리수가 있다."

    rand_idx = np.random.randint(4)
    s1 = [-1, 0, 1][np.random.randint(3)]
    s2 = [2, 3, 4, 5, 6][np.random.randint(4)]
    s3 = s2 + 1
    s4 = [3, 5, 7, 9, 10][rand_idx]
    s5 = s4 + 3

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)

    return stem, answer, comment


def realnum311_Stem_144():
    '''3-1-1-199'''

    students = ["인생살이..","선희", "지호", "재석", "봉경", "현무", "자연", "승태", "석필", "선규", "미화", "지영", "지수"]
    rand_idx = np.random.randint(1, 4)
    st1 = students[rand_idx]
    st2 = students[3 + rand_idx]
    st3 = students[6 + rand_idx]
    st4 = students[9 + rand_idx]

    a = np.random.randint(1,10)
    s1 = [-1, 0, 1][np.random.randint(3)]
    s2 = [2, 3, 4, 5, 6][np.random.randint(4)]
    s3 = s2 + 1
    s4 = [3, 5, 7, 9, 10][np.random.randint(4)]
    s5 = s4 + 3

    stem = "다음은 4명의 학생이 유리수와 무리수에 대하여 나눈 대화의 일부이다. 옳지 않은 설명을 한 학생을 모두 고르면?\n" \
           f"{st1}: $$수식$$ {a} $$/수식$$에 가장 가까운 무리수는 $$수식$$ sqrt {a} $$/수식$$야.\n" \
           "{st2}: $$수식$$ sqrt{s1} $$/수식$$과  $$수식$$ sqrt{s2} $$/수식$$사이에는 무수히 많은 무리수가 있어.\n" \
           "{st3}: 서로 다른 두 실수 사이에는 무수히 많은 유리수가 있어.\n" \
           "{st4}: 무리수 중에서 수직선 위의 점에 대응되지 않는 수도 있어.\n" \
           "① {st1}, {st2}\n" \
           "② {st1}, {st4}\n" \
           "③ {st2}, {st4}\n" \
           "④ {st2}, {st3}\n" \
           "⑤ {st3}, {st4}\n"
    answer = "(정답) ②\n"
    comment = "(해설) \n" \
              "{st1}: $$수식$$ 1 $$/수식$$에 가장 가까운 무리수는 알 수 없다.\n" \
              "{st4}: 모든 무리수는 각각 수직선 위의 점에 대응한다.\n" \
              "따라서 옳지 않은 설명을 한 학생은 {st1}, {st4}이다."

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, st1=st1, st2=st2, st3=st3, st4=st4)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, st1=st1, st2=st2, st3=st3, st4=st4)

    return stem, answer, comment


def realnum311_Stem_145():
    '''3-1-1-200'''

    import numpy as np
    import random as rd

    s1 = np.random.randint(-1,30)
    s2 = np.random.randint(((s1+2)**2 + 1),((s1+3)**2))
    rand_idx = np.random.randint(3)
    # s1 = [-1, 0, 1, 2][rand_idx]
    # s2 = [3, 5, 10, 17][rand_idx]
    ss2 = [2, 3, 4, 5][rand_idx]
    s4 = rand_idx + 1
    s3 = s4 + 2
    s5 = round(math.sqrt(s2), 2)

    idx = rd.sample(range(5),5)
    q = ["자연수","정수","유리수","무리수","실수"]

    stem = "보기에서 $$수식$$ x $$/수식$$의 값이 무수히 많은 것의 개수는?\n"  \
           "㈀ $$수식$$ x는` {s1} &lt;= x &lt; sqrt {s2} $$/수식$$인 " + q[idx[0]] + "\n"\
           "㈁ $$수식$$ x는` {s1} &lt;= x &lt; sqrt {s2} $$/수식$$인 " + q[idx[1]] + "\n"\
           "㈂ $$수식$$ x는` {s1} &lt;= x &lt; sqrt {s2} $$/수식$$인 " + q[idx[2]] + "\n"\
           "㈃ $$수식$$ x는` {s1} &lt;= x &lt; sqrt {s2} $$/수식$$인 " + q[idx[3]] + "\n"\
           "㈄ $$수식$$ x는` {s1} &lt;= x &lt; sqrt {s2} $$/수식$$인 " + q[idx[4]] + "\n"\
           "① 1\n" \
           "② 2\n" \
           "③ 3\n" \
           "④ 4\n" \
           "⑤ 5\n"
    answer = "(정답) ③\n"
    comment = "(해설) \n" \
              f"$$수식$$ {math.floor(math.sqrt(s2))} &lt; sqrt {s2} &lt; {math.ceil(math.sqrt(s2))} $$/수식$$ 이다.\n" \
              " 따라서 자연수는 총 $$수식$$2$$/수식$$개, " \
              "정수는 총 $$수식$$2$$/수식$$개.\n" \
              "이상에서 $$수식$$ x $$/수식$$의 값이 무수히 많은 것은 실수, 무리수, 유리수로 3 개이다.\n"


    stem = stem.format(s1=s1, s2=s2, ss2=ss2, s3=s3, s4=s4, s5=s5)
    comment = comment.format(s1=s1, s2=s2, ss2=ss2, s3=s3, s4=s4, s5=s5)

    return stem, answer, comment


def realnum311_Stem_146():
    '''3-1-1-207'''

    def bong(n):
        ret = math.ceil(math.sqrt(n))+1
        return ret

    def no_root(n) :
        import random

        bong = [i for i in range(1,n+1) if not i in [1,4,9,16,25,36,49,64,81,100]]
        a = random.choice(bong)
        return a

    rand_idx = np.random.randint(5)
    s1 = no_root(77)
    s2 = bong(s1)
    s4 = math.ceil(math.sqrt(s1))
    s3 = math.floor(math.sqrt(s1))
    like_6 = math.ceil(s1 / 2)

    stem = f"다음 중 두 수 $$수식$$ sqrt{s1} $$/수식$$과  $$수식$$ {s2} $$/수식$$사이에 있는"\
           " 무리수가 아닌 것을 모두 고르면? (정답 2개)\n"\
           f"① $$수식$$ sqrt {s1} + 1  $$/수식$$ \n" \
           f"② $$수식$$ {s2-1} $$/수식$$ \n" \
           f"③ $$수식$$ sqrt {2*s2**2-1}over sqrt2 $$/수식$$ \n" \
           f"④ $$수식$$ sqrt{s1} + 2 $$/수식$$ \n" \
           f"⑤ $$수식$$ sqrt{like_6} + 2 $$/수식$$ \n"
    answer = "(정답) ②, ④\n"
    comment = f"(해설) \n"\
              f"$$수식$$ sqrt{s3**2} &lt; sqrt{s1} &lt; sqrt{s4**2} $$/수식$$, 즉"\
              f" $$수식$$ {s3} &lt; sqrt{s1} &lt; {s4}$$/수식$$이고"\
              f" $$수식$$ sqrt{s2**2} = {s2} $$/수식$$이다.\n" \
              f"① $$수식$$ {s3}&lt; sqrt{s1} &lt; {s4}$$/수식$$ 에서 $$수식$$ {s3+1}&lt; sqrt{s1} + 1 &lt; {s4+1}$$/수식$$\n"\
              f"② {s2-1}는 유리수이다. \n" \
              f"③ $$수식$$ sqrt{s1} &lt; sqrt {2*s2**2-1}over sqrt2 &lt; sqrt{s2**2}$$/수식$$ \n"\
              f"④ $$수식$$ {s3} &lt; sqrt{s1} &lt;{s4}$$/수식$$에서"\
              f"$$수식$$ {s3+2} &lt; sqrt{s1} + 2 &lt; {s4+2} $$/수식$$  \n" \
              f"⑤ $$수식$$ sqrt{(math.floor(math.sqrt(like_6)))**2} &lt; sqrt{like_6} &lt; " \
              f"sqrt{(math.ceil(math.sqrt(like_6)))**2} $$/수식$$, 즉 " \
              f"$$수식$$ {math.floor(math.sqrt(like_6))} &lt; sqrt{like_6} &lt; {math.ceil(math.sqrt(like_6))}$$/수식$$"\
              f"이므로\n" \
              f"$$수식$$ {math.ceil(math.sqrt(like_6)) +1} &lt; sqrt{like_6} + 2 &lt; {math.ceil(math.sqrt(like_6)) + 2} $$/수식$$ \n"


    return stem, answer, comment

def realnum311_Stem_147():
    stem ="다음 중 두 수 $$수식$$ {c1} $$/수식$$와 $$수식$${c2}$$/수식$$ 사이에 있는 수의 개수는?\n"\
           "$$표$$ $$셀$$ $$수식$$ sqrt{c3},````sqrt{c4},````sqrt{c5},````sqrt{c6}$$/수식$$ \n  $$수식$$sqrt{c7},````sqrt{c8},````sqrt{c9}$$/수식$$ $$/셀$$ $$/표$$\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$ {c1} `=`sqrt{d1}$$/수식$$, $$수식$$ {c2} `=` sqrt{d2}$$/수식$$ 이므로 {c1}와 {c2}사이에 있는 수는 \n"\
              "$$수식$$ sqrt{c4},``sqrt{c6},``sqrt{c7},``sqrt{c9}$$/수식$$\n"\
              "의 $$수식$$ {ans} $$/수식$$개 이다.\n\n"
    left='{'
    right='}'
    c1 = random.randint(2,5)
    c2 = c1+1
    d1 = c1*c1
    d2 = c2*c2
    ans = 4
    ex1= ans-1
    ex2=ans
    ex3=ans+1
    ex4=ans+2
    ex5=ans+3
    while(True):
        c3 = random.randint(2,10)
        c4 = random.randint(2,30)
        if(c3 < c1**2)&(c4>c1**2)&(c4<c2**2):
            break
    while(True):
        cmp1 = random.random()
        cmpint = random.randint(1,10)
        c5 = cmp1 + cmpint
        c5 = round(c5,2)
        if(c5 >c2):
            break
    while(True):
        cmp1 = random.random()
        cmpint = random.randint(1,10)
        c6 = cmp1 + cmpint
        c6 = round(c6,2)
        if(c6 >c2)&(c6>c5):
            break
    while(True):
        mo1 = random.randint(2,5)
        ja1 = random.randint(10,20)
        if(non_integer(mo1))&(non_integer(ja1))&(ja1/mo1>c1)&((ja1/mo1)<c2)&(gcd(mo1,ja1)==1):
            c7 = "{left}{b1} over {b2}{right}".format(b1=ja1, b2 = mo1,left=left,right=right)
            break
    while(True):
        mo1 = random.randint(2,5)
        ja1 = random.randint(6,20)
        if(non_integer(mo1))&(non_integer(ja1))&((ja1/mo1)>c2)&(gcd(mo1,ja1)==1):
            c8 = "{left}{b1} over {b2}{right}".format(b1=ja1, b2 = mo1,left=left,right=right)
            break
    while(True):
        mo1 = random.randint(2,5)
        ja1 = random.randint(10,20)
        if(non_integer(mo1))&(non_integer(ja1))&(ja1/mo1>c1)&((ja1/mo1)<c2)&(gcd(mo1,ja1)==1):
            c9 = "{left}{b1} over {b2}{right}".format(b1=ja1, b2 = mo1,left=left,right=right)
            break
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8,c9=c9,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1 = answer_dict.get(1))
    comment = comment.format(c1=c1,c2=c2,d1=d1,d2=d2,c4=c4,c6=c6,c7=c7,c9=c9,ans=ans)
    return stem, answer, comment

#209
def realnum311_Stem_148():
    import random
    answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
}
    stem = "$$수식$$ sqrt{a}$$/수식$$의 값이 {num1}과 {num2}사이에 있도록 하는 자연수 $$수식$${a}$$/수식$$의 개수는?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
        
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${num1}&lt;$$/수식$$$$수식$$sqrt{a}$$/수식$$$$수식$$&lt;{num2}$$/수식$$에서 $$수식$${doublenum1}&lt;{a}&lt;{doublenum2}$$/수식$$\n"\
        "따라서 구하는 자연수 $$수식$$a$$/수식$$의 개수는\n"\
        "$$수식$${list0},~{list1},~{list2},~ CDOTS,~{list3}$$/수식$$의 $$수식$${ans}$$/수식$$\n\n"
    num1 = random.randint(2, 10)
    num2 = random.randint(((num1)+1),((num1)+4))
    doublenum1 = num1 * num1
    doublenum2 = num2 * num2
    cont_num=[(doublenum2)-1]
    for i in range(0,3):
        cont_num.insert(i,(doublenum1 + (i+1)))
        i = i+1
    ans = cont_num[3] - cont_num[0] + 1
    ex1 = ans - 3
    ex2 = ans - 2
    ex3 = ans - 1
    ex4 = ans
    ex5 = ans + 1
    stem = stem.format(num1="$$수식$$"+ str(num1)+"$$/수식$$", num2="$$수식$$"+str(num2)+"$$/수식$$",a='a',\
                       ex1 = "$$수식$$"+str(ex1)+"$$/수식$$", ex2 = "$$수식$$"+str(ex2)+"$$/수식$$", ex3 = "$$수식$$"+str(ex3)+"$$/수식$$", ex4 = "$$수식$$"+str(ex4)+"$$/수식$$",\
                       ex5 = "$$수식$$"+str(ex5)+"$$/수식$$")
    answer = answer.format(a1 = answer_dict.get(3))
    comment = comment.format(num1="$$수식$$"+str(num1)+"$$/수식$$", num2="$$수식$$"+str(num2)+"$$/수식$$",\
                             doublenum1 = "$$수식$$"+str(doublenum1)+"$$/수식$$",a='a', doublenum2 = "$$수식$$"+str(doublenum2)+"$$/수식$$",\
                             list0 = cont_num[0], list1 = cont_num[1], list2 = cont_num[2], list3 = cont_num[3], ans = "$$수식$$"+str(ans)+"$$/수식$$")
    
    return stem, answer, comment


#211
def realnum311_Stem_149():
    stem = "두 수 $$수식$$sqrt {num1} - {num2}$$/수식$$와 $$수식$${num3} - sqrt {num1}$$/수식$$ 사이에 있는 모든 정수의 합은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$sqrt {route1} &lt; sqrt{num1} &lt; sqrt{route2}$$/수식$$, 즉 $$수식$${integer1} &lt; sqrt{num1} &lt; {integer2}$$/수식$$이므로"\
              "$$수식$${integer3} &lt; sqrt{num1} - {num2} &lt; {integer4}$$/수식$$"\
              "또 $$수식$${integer1} &lt; sqrt{num1} &lt; {integer2}$$/수식$$에서 $$수식$$- {integer2} &lt; - sqrt{num1} &lt; -{integer1}$$/수식$$"\
              "$$수식$$ THEREFORE ~ {integer5} &lt; {num3} - sqrt{num1} &lt; {integer6}$$/수식$$"\
              "따라서 $$수식$$sqrt{num1} - {num2}$$/수식$$와 $$수식$${num3} - sqrt{num1}$$/수식$$ 사이에 있는 정수는 $$수식$${answer1}$$/수식$$"\
              "이므로 구하는 합은"\
              "$$수식$${answer2} = {ans}$$/수식$$\n\n"
    while(True):
        while(True):
            while(True):
                num1=random.randint(5,20)
                if(num1 !=9)&(num1!=16):
                    break
            num2 = random.randint(1,int(math.sqrt(num1))+1)
            num3 = random.randint(int(math.sqrt(num1))+1, int(math.sqrt(num1))+5)
            route1 = int(math.sqrt(num1))**2
            route2 = int(math.sqrt(num1)+1)**2
            integer1 = int(math.sqrt(num1))
            integer2 = int(math.sqrt(num1))+1
            integer3 = integer1 - num2
            integer4 = integer3 + 1
            integer5 = num3 - int(math.sqrt(num1)) -1
            integer6 = num3 - int(math.sqrt(num1))
            if(integer4 < integer5):
                break
        biggest = integer6 - integer3 -1
        sum=0
        final_list=[]
        k = integer3
        while(True):
            sum = sum + (k+1)
            final_list.append(k + 1)
            biggest = biggest - 1
            k = k + 1
            if biggest == 0:
                break
        if(len(final_list)!=1):
            break
    if(len(final_list)==2):
        answer1 = "{e1}, {e2}".format(e1 = final_list[0], e2 = final_list[1])
        answer2 = "{e1} + {e2}".format(e1 = final_list[0], e2 = final_list[1])
    elif(len(final_list)==3):
        answer1 = "{e1}, {e2}, {e3}".format(e1 = final_list[0], e2 = final_list[1], e3 = final_list[2])
        answer2 = "{e1} + {e2} + {e3}".format(e1 = final_list[0], e2 = final_list[1], e3 = final_list[2])

    elif(len(final_list)==4):
        answer1 = "{e1}, {e2}, {e3}, {e4}".format(e1 = final_list[0], e2 = final_list[1], e3 = final_list[2], e4 = final_list[3])
        answer2 = "{e1} + {e2} + {e3} + {e4}".format(e1 = final_list[0], e2 = final_list[1], e3 = final_list[2], e4 = final_list[3])

    else:
        answer1 = "{e1}, {e2}, {e3}, {e4}, {e5}".format(e1 = final_list[0], e2 = final_list[1], e3 = final_list[2], e4 = final_list[3], e5 = final_list[4])
        answer2 = "{e1} + {e2} + {e3} + {e4} + {e5}".format(e1 = final_list[0], e2 = final_list[1], e3 = final_list[2], e4 = final_list[3], e5 = final_list[4])

    ans = sum
            
    ex1 = ans - 1
    ex2 = ans
    ex3 = ans + 1
    ex4 = ans + 2
    ex5 = ans + 3
    stem = stem.format(num1 = num1, num2 = num2, num3 = num3,\
                           ex1 = ex1, ex2 = ex2, ex3 = ex3, ex4 = ex4, ex5 = ex5)
    answer = answer.format(a1 = answer_dict.get(1))
    comment = comment.format(route1 = route1, num1 = num1, route2 = route2, integer1 = integer1,\
                             integer2 = integer2, integer3 = integer3, num2 =num2, integer4 = integer4,\
                             integer5 = integer5, num3 = num3, integer6 = integer6, answer1 = answer1,answer2 = answer2,\
                             ans=ans)
    return stem, answer, comment


#213
def realnum311_Stem_150():
    stem = "실수 $$수식$$x$$/수식$$에 대하여 $$수식$$sqrt{num1} LEQ x LEQ sqrt{num2} `$$/수식$$를 만족시킬"\
           " 때, 다음 중 옳은 것을 모두 고르면? (정답 2개)\n"\
           "① 정수인 $$수식$$x$$/수식$$의 개수는 $$수식$${ex1}$$/수식$$이다.\n"\
           "② 실수 $$수식$$x$$/수식$$의 개수는 유한개이다.\n"\
           "③ 유리수인 $$수식$$x$$/수식$$의 개수는 유한개이다.\n"\
           "④ 무리수인 $$수식$$x$$/수식$$의 개수는 $$수식$${ex4}$$/수식$$이다.\n"\
           "⑤ $$수식$$x = sqrt{num3} + {num4}$$/수식$$는 조건을 만족시킨다.\n"
    answer = "(답) {a1}, {a2}\n"
    comment = "(해설)\n"\
              "① $$수식$$ {c1} &lt; sqrt{num1} &lt; {c2}$$/수식$$, $$수식$$ {c3} &lt; sqrt{num2} &lt; {c4}$$/수식$$ 이므로"\
              " 정수는 $$수식$$ {c5}, ` {c6}$$/수식$$ 의 $$수식$${c7}$$/수식$$개이다.\n"\
              "② 실수 $$수식$$x$$/수식$$는 무수히 많다.\n"\
              "③ 유리수인 $$수식$$x$$/수식$$는 무수히 많다.\n"\
              "④ 무리수 $$수식$$x$$/수식$$는 무수히 많다.\n"\
              "⑤ $$수식$$ {d1} &lt; sqrt{num3} &lt; {d2}$$/수식$$에서 $$수식$${d3} &lt; sqrt{num3} + {num4} &lt; {d4}$$/수식$$\n"\
              "sqrt{num1} &lt; {c2}$$/수식$$, $$수식$${c3} &lt; sqrt{num2}$$/수식$$이므로\n"\
              "$$수식$$ sqrt{num1} &lt; sqrt{num3} + {num4} &lt; sqrt{num2}$$/수식$$\n\n"
    while(True):
        while(True):
            num1 = random.randint(5,16)
            num2 = random.randint(17, 30)
            num3 = random.randint(2, 16)
            if(num2!=25)&(num3!=4)&(num3!=9)&(int((num2)**0.5) - int((num1)**0.5) == 2):
                break
        c1 = int((num1)**0.5)
        c2 = c1 + 1
        c3 = int((num2)**0.5)
        c4 = c3 + 1
        ex1 = c4 - c1 - 1
        ex4 = random.randint(5,20)
        integer1 = int((num1)**0.5+1)- int((num3)**0.5)
        integer2 = int((num2)**0.5)-int((num3)**0.5+1)
        if ( integer2 == integer1 ):
            num4 = integer2
        else:
            num4 = random.randint(integer1, (integer2 + 1))
        if(num4 != 0):
            break
    
    c5 = c1 + 1
    c6 = c5 + 1
    c7 = c3 - c1
    d1 = int((num3)**0.5)
    d2 = d1 + 1
    d3 = d1 + num4
    d4 = d3 + 1
    stem = stem.format(num1=num1, num2 = num2, ex1 = ex1, ex4 = ex4,\
                       num3 = num3, num4 = num4)
    answer = answer.format(a1 = answer_dict.get(0), a2 = answer_dict.get(4))
    comment = comment.format(c1 = c1, num1 = num1, c2 = c2, c3 =c3,\
                             num2 = num2, c4 = c4, c5 = c5, c6 = c6,\
                             c7 = c7,d1 = d1, num3 = num3, d2 = d2,\
                             d3 = d3, num4 = num4, d4 = d4)
    return stem, answer, comment

        

#222
def realnum311_Stem_151():
    stem = "다음 중 옳지 않은 것은?\n"\
           "① $$수식$$ sqrt{c1} ` TIMES ` sqrt{c2} ` = ` sqrt{c3}$$/수식$$\n"\
           "② $$수식$$ {c4} sqrt{c5} ` TIMES ` {c6} sqrt{c7} ` = ` {c8} sqrt{c9}$$/수식$$\n"\
           "③ $$수식$$ - sqrt{c10} ` TIMES ` sqrt{c11} = - {c12}$$/수식$$\n"\
           "④ $$수식$$ sqrt{left}{c13} over {c14}{right} ` TIMES ` sqrt {left}{c15} over {c16}{right} ` = ` sqrt{cond}$$/수식$$"\
           "⑤ $$수식$$ sqrt {left}{c18} over {c19}{right} ` TIMES ` {c20} sqrt {left}{c21} over {c22}{right} ` = ` {c20} sqrt {left}{c24} over {c25}{right}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "④ $$수식$$sqrt {left}{c13} over {c14}{right} ` TIMES ` sqrt {left}{c15} over {c16}{right} ` = ` sqrt {left}{c13} over {c14} ` TIMES ` {c15} over {c16}{right} ` = ` sqrt {c17}$$/수식$$"
    left = '{'
    right = '}'
    primelist=[2,3,5,7,11,13]
    while(True):
        c1 = random.choice(primelist)
        c2 = random.choice(primelist)
        if(c1!=c2):
            break
    c3 = c1*c2
        #여기까지가 1번
        
    c4 = random.randint(2,5)
    c6 = random.randint(2,5)
    c8 = c4*c6
    while(True):
        c5 = random.randint(2,6)
        c7 = random.randint(6,12)
        if (c5!=4)&(c7!=9)&(c7!=8):
            break
    c9 = c5 * c7 
    if(out_route(c9)!=0):
        c8 = c8 * out_route(c9)
        c9 = int(c9/(out_route(c9)**2))
        
        
    ### 여기까지가 2

    choicelist=[2,3]
    two = [2,8,32,128]
    three = [3,27]
    choice = random.choice(choicelist)
    if choice == 2:
        c10 = random.choice(two)
        c11 = random.choice(two)
        c12 = int(2**(((two.index(c10)*2 +1)+(two.index(c11)*2+1))/2))
        
    elif choice == 3:
        c10 = random.choice(three)
        c11 = random.choice(three)
        c12 = int(3**(((three.index(c10)*2 +1)+(three.index(c11)*2+1))/2))      
    ## 여기까지가 3
    while(True):
        while(True):
            c13 = random.randint(6, 13)
            c14 = random.randint(2, 4)
            if (gcd(c13,c14)==1):
                break
        while(True):
            c15 = random.randint(6, 24)
            c16 = random.randint(2, 5)
            if (gcd(c15,c16)==1):
                break
        compare1 = c16*c14
        compare2 = c15*c13
        if (gcd(compare1, compare2)==compare1):
            c17 = int(compare2 / compare1)
            k = random.randint(1,5)
            temp = c17 + k
            if(non_integer(temp)):
                break

        

    ##여기까지가 4번

    while(True):
        c18 = random.randint(2,4)
        c19 = random.randint(6,13)
        if (gcd(c18,c19)==1):
            break
    c20 = random.randint(2,4)
    while(True):
        c21 = random.randint(2,4)
        c22 = random.randint(6,13)
        if (gcd(c21,c22)==1):
            break
    cmp1 = c19 * c22
    cmp2 = c18 * c21
    division = gcd(cmp1, cmp2)
    if(division == 1):
        c24 = cmp2
        c25 = cmp1
    else:
        c24 = int(cmp2 / division)
        c25 = int(cmp1 / division)

    ##5번까지 끝
    stem=stem.format(c1 = c1, c2 = c2, c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8,c9=c9,c10=c10,c11=c11,c12=c12,left = left, c13=c13,c14=c14,right = right, c15=c15,c16=c16,cond=temp,c18=c18,c19=c19,c20=c20,\
                     c21=c21,c22=c22,c24=c24,c25=c25)
    answer = answer.format(a1=answer_dict.get(3))
    if ( non_integer(c17) ):
        comment = comment.format(left = left, c13=c13,c14=c14,c15=c15,c16=c16,right = right, c17=c17)+"\n\n"
    else:
        comment = comment.format(left = left, c13=c13,c14=c14,c15=c15,c16=c16,right = right, c17=c17)+"  =  $$수식$${d1}$$/수식$$\n\n".format(d1 = int(c17**0.5))

    return stem, answer, comment
        
#223       
def realnum311_Stem_152():
    stem = "$$수식$$ sqrt{c1} TIMES sqrt{c2} ` = ` sqrtA$$/수식$$일 때, $$수식$$A$$/수식$$의 값을 구하시오.\n"
    answer = "(정답) {ans}\n"
    comment = "$$수식$$ sqrt {c1} TIMES sqrt{c2} ` = ` sqrt{left}{c1} TIMES {c2}{right} ` = ` sqrt{c3} ` = ` sqrtA$$/수식$$이므로\n"\
              "$$수식$$A ` = ` {c4}$$/수식$$"
    primelist = [2, 3, 5, 7, 11, 13, 17]
    left = '{'
    right = '}'
    while(True):
        c1 = random.choice(primelist)
        c2 = random.choice(primelist)
        if (c1 != c2):
            break
    c3 = c1*c2
    c4 = c3
    ans = c3
    stem = stem.format(c1 = c1, c2 = c2)
    answer = answer.format(ans=ans)
    comment = comment.format(c1 = c1, c2 = c2, left= left, right = right, c3 = c3, c4 = c4)
    return stem, answer, comment

#224
def realnum311_Stem_153():
    stem = "$$수식$$ sqrt{c1} TIMES sqrt{c2}$$/수식$$를 계산하면?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(정답) {a1}\n"
    comment = "$$수식$$ sqrt{c1} TIMES sqrt{c2} ` = ` sqrt{left}{c1} TIMES {c2}{right} ` = ` sqrt{c3} ` = ` {c4}$$/수식$$\n\n"
    left = '{'
    right = '}'
    c1list=[0.2, 0.4, 0.5, 0.6, 0.8]
    c2list=[0.08, 0.32, 0.64, 0.03, 0.27, 0.81, 0.24, 0.36, 0.44, 0.48, 0.52, 0.56, 0.60, 0.68, 0.72, 0.76]
    while(True):
        while(True):
            c1 = random.choice(c1list)
            c2 = random.choice(c2list)
            c3 = c1 * c2
            if((c1*10)*(c2*100)) % 10 == 0:
                num1 = int(c3* 100)
                break
        result = soinsoo(num1)
        length = len(result)
        a=1 # 아래 for문에서 True False 역할
        primes=list(result)
        for i in range (0, length):
            if result[primes[i]] % 2 == 0:
                a = 1 #True
            else:
                a=0
                break
        if (a==1):
            c4 = (c3**0.5)
            break

    ans = c4
    ex1 = ans/10
    ex2 = ans/50
    ex3 = ans/500
    ex4 = ans/2
    ex5 = ans
    stem=stem.format(c1=c1, c2=c2, ex1=ex1, ex2 =ex2, ex3 = ex3, ex4 = ex4, ex5 = ex5)
    answer = answer.format(a1=answer_dict.get(4))
    comment = comment.format(c1 = c1, c2 = c2, left = left, right = right, c3=c3, c4=c4)
    return stem, answer, comment

#225
def realnum311_Stem_154():
    stem = "$$수식$$sqrt {left}{c1} over {c2}{right}  TIMES  sqrt {c3}  TIMES  sqrt {left}{c4} over {c5}{right} ` = ` A `$$/수식$$라 할 때, $$수식$$100 A$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$ sqrt {left}{c1} over {c2}{right}  TIMES  sqrt {c3}  TIMES  sqrt {left}{c4} over {c5}{right} `$$/수식$$$$수식$$= ` sqrt {left}{c1} over {c2}  TIMES {c3} TIMES  {c4} over {c5}{right}$$/수식$$\n"\
              "$$수식$$ = ` sqrt {left}{c1} over {c2}  TIMES  {d1} over {d2}  TIMES  {c4} over {c5}{right}$$/수식$$\n"\
              "$$수식$$ = ` sqrt {left}{d3} over {d4}{right} ` = ` {d5} over {d6}$$/수식$$"\
              "$$수식$$ ` = ` A$$/수식$$\n"\
              "$$수식$$ THEREFORE ~ 100 ` A ` = ` 100 TIMES {d5} over {d6} ` = ` {ans}$$/수식$$\n\n"
    left = '{'
    right = '}'
    dotnumber = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.02, 0.03, 0.06, 0.05, 0.08, 0.12, 0.14, 0.15, 0.18, 0.24, 0.28, 0.32, 0.35, 0.45, 0.48, 0.54, 0.56, 0.72, 0.75, 0.84, 0.85, 0.99]
    while(True):
        c1 = random.randint(1,9)
        c2 = 100
        c3 = random.choice(dotnumber)
        c4 = random.randint(1,9)
        if((int(c3*100)) % 10 == 0): #한자리 소수점 
            c5 = 10
            d2 = 10**1
            d1 = int(c3*d2)
            d3 = c1 * d1 * c4
            d4 = 10000
            result = soinsoo(d3)
            length = len(result)
            primes = list(result)
            for i in range(0,length):
                if(result[primes[i]] == 0):
                    del result[primes[i]]
            length = len(result)
            primes = list(result)
            a=1
            for i in range(0,length):
                if result[primes[i]]%2==0:
                    a=1
                else:
                    a=0
                    break
            if (a == 0):
                continue
            else:
                d5 = int(d3**0.5)
                d6 = 100
                ja = 100 * d5
                if(gcd(ja, 100) == 100):
                    ans = int(ja / 100)
                    break

        


    stem = stem.format(left = left, c1 = c1, c2 =c2, right = right, c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1 = ans)
    comment = comment.format(left=left, c1=c1, c2=c2, right=right, c3=c3, c4=c4, c5=c5, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5, d6=d6, ans = ans)
    return stem, answer, comment



#226
def realnum311_Stem_155():
    stem = "다음을 만족시키는 유리수 $$수식$$a,``b$$/수식$$에 대하여 $$수식$$a`+`b$$/수식$$의 값을 구하시오.\n"\
           "$$표$$ $$수식$$sqrt{left} {c1} over {c2} {right} TIMES sqrt{left} {c3} over {c4} {right} `=` a$$/수식$$,  $$수식$$sqrt{left}{c5} over {c6}{right} TIMES {c7} sqrt{left}{c8} over {c9}{right} `=` b$$/수식$$$$/표$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              " $$수식$$sqrt{left} {c1} over {c2} {right} TIMES sqrt{left} {c3} over {c4} {right} `=` sqrt {left}{c1}over{c2} TIMES {c3} over {c4} {right}`=` sqrt {d1} `=` {d2}$$/수식$$이므로\n"\
              "$$수식$$ a`=` {d2} $$/수식$$\n"\
              "$$수식$$sqrt{left}{c5} over {c6}{right} TIMES {c7} sqrt{left}{c8} over {c9}{right} `=` {c7} sqrt{left}{c5} over {c6} TIMES {c8} over {c9}{right} `=` {d3}$$/수식$$ 이므로 \n"\
              "$$수식$$ b`=`{d3} $$/수식$$ \n"\
              "$$수식$$ THEREFORE ~ a`+`b`=`{ans}$$/수식$$\n\n"
    while(True):
        c1 = random.randint(2,10)
        c2 = random.randint(2,10)
        c3 = random.randint(5,20)
        c4 = random.randint(2,6)
        if (non_integer(c1))&(non_integer(c2))&(non_integer(c3))&(non_integer(c4))&(gcd(c1,c2)==1)&(gcd(c3,c4)==1)&(c1!=c2)&(c3!=c4):
            ja_1 = c1*c3
            mo_1 = c2*c4
            if(gcd(ja_1,mo_1)==mo_1):
                num1 = int(ja_1/mo_1)
                if(non_integer(num1)):
                    continue
                else:
                    break
    d1 = num1
    d2 = int(d1**0.5)
    while(True):
        c7 = random.randint(2,5)
        c5 = random.randint(2,10)
        c6 = random.randint(2,10)
        c8 = random.randint(5,10)
        c9 = random.randint(5,20)
        if (non_integer(c5))&(non_integer(c6))&(non_integer(c8))&(non_integer(c9))&(gcd(c5,c6)==1)&(gcd(c8,c9)==1)&(c5!=c6)&(c8!=c9):
            ja_2 = c5*c8
            mo_2 = c6*c9
            if(gcd(ja_2,mo_2)==mo_2):
                num2 = int(ja_2/mo_2)
                if(non_integer(num2)):
                    continue
                else:
                    break
    d3 = c7 * int(num2**0.5)
    ans = d3+d2
    left='{'
    right='}'
    stem = stem.format(left=left,right=right,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8,c9=c9)
    answer = answer.format(a1 = ans)
    comment = comment.format(left=left, right=right, c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8,c9=c9,d1=d1,d2=d2,d3=d3,ans=ans)
    return stem, answer, comment

#227
def realnum311_Stem_156():
    stem = "$$수식$$ {c1} TIMES sqrt{c2} TIMES sqrt k ` = ` sqrt {c3} TIMES sqrt {c4}$$/수식$$을 만족시키는 양의 유리수 $$수식$$ k $$/수식$$의 값은?\n"\
           "① {ex1}    ② {ex2}     ③ {ex3}    ④ {ex4}     ⑤ {ex5}\n"
    answer = "(정답) {a1}\n"
    comment = "$$수식$$ {c1} TIMES sqrt{c2} TIMES sqrt k ` = ` {c1} sqrt{left}{c2}k{right} `$$/수식$$,\n"\
              "$$수식$$ sqrt {c3} TIMES sqrt {c4} ` = ` sqrt{c5} ` = ` {c6}$$/수식$$이므로\n"\
              "$$수식$${c1} sqrt{left}{c2}k{right} ` = ` {c6}$$/수식$$, $$수식$$sqrt{left}{c2}k{right} ` = ` {c7}$$/수식$$, "\
              "$$수식$$ {c2}k ` = ` {c8}$$/수식$$\n"\
              "$$수식$$ THEREFORE ~ k ` = ` $$/수식$$ $$수식$${c9}$$/수식$$\n\n"
    left='{'
    right='}'

    while(True):
        while(True):
            prime=[2,3,5,7,11,13]
            c2=random.choice(prime)
            c3 = random.randint(2,15)
            c4 = random.randint(10,35)
            if(non_integer(c3))&(non_integer(c4)):
                break
        c5 = c3*c4
        result = soinsoo(c5)
        length = len(result)
        primelist=list(result)
        for i in range(0,length):
            if(result[primelist[i]]==0):
                del result[primelist[i]]
        length = len(result)
        primelist=list(result)
        for i in range(0,length):
            if(result[primelist[i]]%2 != 0):
                a=1
                break
            else:
                a=0   
        if a==0:
            c6 = int(c5**0.5)
            c1 = random.randint(2,6)
            if(c6%c1==0):
                break
        else:
            continue
    

    #c1 구하는 while문
    c7 = int(c6/c1)
    c8 = c7*c7
    if(gcd(c8,c2)==c2):
        c9 = int(c8/c2)
    elif(gcd(c8,c2)==1):
        c9 = "{c8} over {c2}".format(c8=c8,c2=c2)
        
    ans = Fraction(c8,c2)
    ex1 = ans - Fraction(2,c2)
    if(ex1.numerator ==0):
        ex1 = "$$수식$$ 0 $$/수식$$"
    elif gcd((ex1.numerator),(ex1.denominator)) != (ex1.denominator):
        ex1 = "$$수식$$ {num1} over {den1}$$/수식$$".format(num1 = (ex1.numerator), den1 = (ex1.denominator)) # Fraction 형태 분수를 over로 바꾸는 형태
    ex2 = ans - Fraction(1,c2)
    if(ex2.numerator ==0):
        ex2 = "$$수식$$ 0 $$/수식$$"
    elif gcd((ex2.numerator),(ex2.denominator)) != (ex2.denominator):
        ex2 = "$$수식$$ {num2} over {den2}$$/수식$$".format(num2 = ex2.numerator, den2 = ex2.denominator)    
    if gcd((ans.numerator),(ans.denominator)) == (ans.denominator):
        ex3 = "$$수식$$ {b1} $$/수식$$".format(b1 = int(ans.numerator/ans.denominator))
    else:
        ex3 = "$$수식$$ {b1} over {b2} $$/수식$$".format(b1 = int(ans.numerator), b2 = ans.denominator)
    ex4 = Fraction(c8,c2) + Fraction(1,c2)
    if(ex4.numerator ==0):
        ex4 = "$$수식$$ 0 $$/수식$$"
    elif gcd((ex4.numerator),(ex4.denominator)) != (ex4.denominator):
        ex4 = "$$수식$$ {num4} over {den4}$$/수식$$".format(num4 = ex4.numerator, den4 = ex4.denominator)
    ex5 = Fraction(c8,c2) + Fraction(2,c2)
    if gcd((ex5.numerator),(ex5.denominator)) != (ex5.denominator):
        ex5 = "$$수식$$ {num5} over {den5}$$/수식$$".format(num5 = ex5.numerator, den5 = ex5.denominator)
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1=answer_dict.get(2))
    comment = comment.format(c1=c1,c2=c2,left=left,right=right,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8,c9=c9) 
    return stem, answer, comment

#228
def realnum311_Stem_157():
    stem = "$$수식$$ sqrt {c1} TIMES sqrt{c2} TIMES sqrt a TIMES sqrt{c3} TIMES sqrt {left}{c4}a{right} ` = ` {c5}$$/수식$$일 때, 자연수 $$수식$$a$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "$$수식$$ sqrt {c1} ` TIMES ` sqrt{c2} ` TIMES ` sqrt a ` TIMES ` sqrt{c3} ` TIMES ` sqrt {left}{c4}a{right}$$/수식$$"\
              "$$수식$$= ` sqrt {left} {c1} TIMES {c2} TIMES a TIMES {c3} TIMES {c4}a {right}$$/수식$$\n"\
              "$$수식$$= ` sqrt {left} {c6} ^2 ` TIMES ` a ^2{right}$$/수식$$\n"\
              "$$수식$$= ` sqrt {left} {leftg} {c6}a {rightg} ^ 2 {right}$$/수식$$\n"\
              "$$수식$$= ` {c6}a {leftg} BECAUSE ~ a &gt; 0 {rightg}$$/수식$$\n"\
              "따라서 $$수식$$ {c6}a ` = ` {c5}$$/수식$$이므로 $$수식$$ a ` = ` {ans}$$/수식$$\n\n"
    left = '{'
    right = '}'
    leftg='('
    rightg=')'
    while(True):
        while(True):
            c1 = random.randint(2,6)
            c2 = random.randint(2,8)
            if(c1 != 4) & (c2 != 4) & (c1 != c2):
                break
        c3 = random.randint(10,21)
        c4 = random.randint(2,6)
        multiple = c1 * c2 * c3 * c4 # 해설 3번쨰 줄 들어갈 값
        #---------c6 구하는 과정----------#
        result = soinsoo(multiple)
        length = len(result)
        primelist = list(result)
        for i in range ( 0, length):
            if(result[primelist[i]] == 0):
                del result[primelist[i]]
        length = len(result)#업데이트
        primelist = list(result)#업더에트
        c6 = 1
        a=1 # True False
        for i in range(0,length):
            if(result[primelist[i]]%2==0):
                c6 = c6 *primelist[i]**(int(result[primelist[i]]/2))
                a=1
            else:
                a=0
                break
        if(a==1):
            break
    anslist = [4,5,6,7]
    ans = random.choice(anslist)
    c5 = c6 * ans
    ex1 = ans-3
    ex2=ans-2
    ex3=ans-1
    ex4=ans
    ex5=ans+1
    stem = stem.format(c1=c1,c2=c2,c3=c3,left=left,c4=c4,right=right,c5=c5,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer=answer.format(a1=answer_dict.get(3))
    comment=comment.format(c1=c1,c2=c2,c3=c3,left=left,c4=c4,right=right,c5=c5,leftg=leftg, c6=c6, rightg=rightg, ans=ans)
    return stem, answer,comment

#229
def realnum311_Stem_158():
    stem = "$$수식$$ {c1} sqrt{c2} TIMES {c3} sqrt{c4} ` = ` {c5} sqrt a$$/수식$$, $$수식$${c6} sqrt{c7} TIMES {c8} sqrt{c9} ` = ` b sqrt{c10}$$/수식$$"\
           "일 때, 자연수 $$수식$$ a, ` b$$/수식$$에 대하여 $$수식$$a ` - ` b$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설) \n"\
              "$$수식$$ {c1} sqrt{c2} TIMES {c3} sqrt{c4} ` = ` {leftg} {c1} TIMES {c3} {rightg} sqrt {left} {c2} TIMES {c4} {right} ` = ` {c5} sqrt {d1}$$/수식$$"\
              "이므로\n $$수식$$ a ` = ` {d1}$$/수식$$ \n"\
              "$$수식$${c6} sqrt{c7} TIMES {c8} sqrt{c9} ` = ` {leftg} {c6} TIMES {c8} {rightg} sqrt {left} {c7} TIMES {c9} {right} ` = ` {d2} sqrt {c10}$$/수식$$"\
              "이므로\n $$수식$$b ` = ` {d2}$$/수식$$\n"\
              "따라서 $$수식$$ a ` - ` b ` = ` {ans}$$/수식$$\n\n"
    right = '}'
    left='{'
    rightg=')'
    leftg='('

    c1 = random.randint(2,4)
    c3 = random.randint(2,4)
    c5 = c1*c3
    while(True):
        c2 = random.randint(2,6)
        c4 = random.randint(3,7)
        if(c2!=4)&(c4!=4)&(c2!=c4):
            break
    c6 = random.randint(2,4)
    c8 = random.randint(2,4)
    while(True):
        c7 = random.randint(2,6)
        c9 = random.randint(3,7)
        c10 = c7*c9
        if(c7!=4)&(c9!=4)&(c9!=c7):
            result = soinsoo(c10)
            length = len(result)
            primes=list(result)
            for i in range(0,length):
                if(result[primes[i]]==0):
                    del result[primes[i]]
            length = len(result)#없데요
            primes = list(result)#없ㄷ에ㅛ
            a=1
            for i in range(0,length):
                if (result[primes[i]]>=2):
                    a=1
                    break
                else:
                    a=0

            if(a==0):
                break
    d1 = c2 * c4
    d2 = c6*c8
    ans = d1 - d2
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8,c9=c9,c10=c10)
    answer = answer.format(a1 = ans)
    comment = comment.format(c1=c1,c2=c2,c3=c3,c4=c4,leftg=leftg,rightg=rightg,left=left,right=right,c5=c5,d1=d1,c6=c6,c7=c7,c8=c8,c9=c9,d2=d2,c10=c10,ans=ans)
    return stem, answer, comment

#230
def realnum311_Stem_159():
    stem = "$$수식$$ sqrt{c1} ` = ` k sqrt {c2}$$/수식$$일 때, 자연수 $$수식$$ k $$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "$$수식$$ sqrt {c1} ` = ` sqrt {left}{d1} ^ {d3} ` TIMES ` {c2}{right} ` = ` {d1} sqrt {c2} `$$/수식$$이므로 $$수식$$k ` = ` {d1}$$/수식$$\n\n"
    while(True):
        while(True):
            c1 = random.randint(30,160)
            if(non_integer(c1)):
                break
        result = soinsoo(c1)
        length = len(result)
        primes = list(result)
        for i in range(0,length):
            if(result[primes[i]] ==0):
                del result[primes[i]]
        length = len(result)
        primes = list(result)
        outroute=[]
        for i in range(0,length):
            if(result[primes[i]]>=2):
                outroute.append(primes[i])
        length_route = len(outroute)
        d1 = 1
        for i in range(0,length_route):
            d1 = d1 * (outroute[i]**(int(result[outroute[i]]/2)))
        d3 = 2
        if(d1>2):
            break
    c2 = int(c1 / ((d1)**2))
    left='{'
    right='}'
    ex1 = d1-2
    ex2=d1-1
    ex3 = d1
    ex4=d1+1
    ex5=d1+2
    stem = stem.format(c1=c1,c2=c2,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1 = answer_dict.get(2))
    comment = comment.format(c1=c1,left=left,d1=d1,d3=d3,c2=c2,right=right)
    return stem, answer, comment

#232
def realnum311_Stem_160():
    stem = "다음 중 옳지 않은 것은?\n"\
           "① $$수식$$ sqrt {c1} ` = ` {c2} sqrt {c3}$$/수식$$\n"\
           "② $$수식$$ {c4} sqrt {c5} ` = ` sqrt {c6}$$/수식$$\n"\
           "③ $$수식$$ sqrt {c7} ` = ` {ans} sqrt {c9}$$/수식$$\n"\
           "④ $$수식$$ {c10} sqrt {c11} ` = ` sqrt {c12}$$/수식$$\n"\
           "⑤ $$수식$$ sqrt {c13} ` = ` {c14} sqrt {c15}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "① $$수식$$ sqrt {c1} ` = sqrt {left} {d1} ^ 2 TIMES {d2} {right}` = ` {c2} sqrt {c3}$$/수식$$\n"\
              "② $$수식$$ {c4} sqrt {c5} ` = ` sqrt {left} {c4} ^ 2 TIMES {c5} {right}` = ` sqrt {c6}$$/수식$$\n"\
              "③ $$수식$$ sqrt {c7} ` = ` sqrt {left}{c8} ^ 2 TIMES {c9}{right} ` = ` {c8} sqrt {c9}$$/수식$$\n"\
              "④ $$수식$$ {c10} sqrt {c11} ` = ` sqrt{left}{c10} ^ 2 TIMES {c11} {right} ` = ` sqrt {c12}$$/수식$$\n"\
              "⑤ $$수식$$ sqrt {c13} ` = ` sqrt{left}{c14} ^ 2 TIMES {c15} {right} ` = ` {c14} sqrt {c15}$$/수식$$\n\n"
    left='{'
    right='}'
    while(True):
        ################# 여기서부터 1번 #######################
        while(True):
            while(True):
                c1 = random.randint(10, 99)
                if(c1!=16)&(c1!=25)&(c1!=36)&(c1!=49)&(c1!=64)&(c1!=81):
                    break
            result_1 = soinsoo(c1)
            length_1 = len(result_1)
            primes_1=list(result_1)
            for i in range (0,length_1):
                if (result_1[primes_1[i]] ==0):
                    del result_1[primes_1[i]]
            length_1 = len(result_1)
            primes_1 = list(result_1)
            outroute_1=[]
            for i in range(0,length_1):
                if (result_1[primes_1[i]]>2):
                    outroute_1.append(primes_1[i])
            c2 = 1
            for i in range(0,len(outroute_1)):
                c2 = c2 * outroute_1[i]**(int(result_1[outroute_1[i]]//2))
            if(c2!=1):
                break
        c3 = int (c1/(c2**2))
        d1 = c2
        d2=c3
        ## 여기까지가 1번 ##
        
        ################# 여기서부터 2번 #######################
        c4 = random.randint(2,4)
        
        while(True):
            c5 = random.randint(3,6)
            if(c5!=4):
                break
        c6 = (c4**2)*c5
        
        ## 여기까지가 2번 ##

        ################# 여기서부터 3번 #######################
        while(True):
            while(True):
                c7 = random.randint(10, 99)
                if(non_integer(c7)):
                    break
            result_3 = soinsoo(c7)
            length_3 = len(result_3)
            primes_3=list(result_3)
            for i in range (0,length_3):
                if (result_3[primes_3[i]] ==0):
                    del result_3[primes_3[i]]
            length_3 = len(result_3)
            primes_3 = list(result_3)
            outroute_3=[]
            for i in range(0,length_3):
                if (result_3[primes_3[i]]>2):
                    outroute_3.append(primes_3[i])
            c8 = 1
            for i in range(0,len(outroute_3)):
                c8 = c8 * outroute_3[i]**(int(result_3[outroute_3[i]]//2))
            if(c8!=1):
                break
        c9 = int (c7/(c8**2))
        ans = c8 * 2
        
        ## 여기까지가 3번 ##
        ################# 여기서부터 4번 #######################
        c10 = random.randint(2,4)
        
        while(True):
            c11 = random.randint(3,6)
            if(c11!=4):
                break
        c12 = (c10**2)*c11
        
        ## 여기까지가 4번 ##
        
        ################# 여기서부터 5번 #######################
        while(True):
            while(True):
                c13 = random.randint(10, 99)
                if(non_integer(c13)):
                    break
            result_5 = soinsoo(c13)
            length_5 = len(result_5)
            primes_5=list(result_5)
            for i in range (0,length_5):
                if (result_5[primes_5[i]] ==0):
                    del result_5[primes_5[i]]
            length_5 = len(result_5)
            primes_5 = list(result_5)
            outroute_5=[]
            for i in range(0,length_5):
                if (result_5[primes_5[i]]>2):
                    outroute_5.append(primes_5[i])
            c14 = 1
            for i in range(0,len(outroute_5)):
                c14 = c14 * outroute_5[i]**(int(result_5[outroute_5[i]]//2))
            if(c14!=1):
                break
        c15 = int (c13/(c14**2))
        d1 = c2
    ## 여기까지가 5번 ##
        if(c1 != c7) & (c7 != c13) & (c1 != c13):
            break
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,ans=ans,c8=c8,c9=c9,c10=c10,c11=c11,c12=c12,c13=c13,c14=c14,c15=c15)
    answer = answer.format(a1 = answer_dict.get(2))
    comment = comment.format(c1=c1,left=left,d1=d1,d2=d2,right=right,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8,c9=c9,c10=c10,c11=c11,c12=c12,c13=c13,c14=c14,c15=c15)
    return stem, answer, comment
    
            
            
    

#233
def realnum311_Stem_161():
    stem = "$$수식$$ sqrt {c1} $$/수식$$은 $$수식$$sqrt {c2}$$/수식$$의 $$수식$$ x $$/수식$$배, $$수식$$ sqrt{c3} $$/수식$$은 $$수식$$ sqrt {c4}$$/수식$$의 $$수식$$ y $$/수식$$배일 때, $$수식$$ x ` - ` y $$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "$$수식$$ sqrt {c1} ` = ` sqrt{left}{d1} ^ 2 TIMES {d2}{right} ` = ` {d1} sqrt{d2} $$/수식$$이므로 $$수식$$ x ` = ` {d1}$$/수식$$\n"\
              "$$수식$$ sqrt {c3} ` = ` sqrt{left}{d3} ^ 2 TIMES {d4}{right} ` = ` {d3} sqrt{d4} $$/수식$$이므로 $$수식$$ y ` = ` {d3}$$/수식$$\n"\
              "$$수식$$ THEREFORE ~ x ` - ` y ` = ` {ans}$$/수식$$\n\n"
    example = [2,3,5,6,7,8]
    while(True):
        while(True):
            c1 = random.randint(101,999)
            result_1 = soinsoo(c1)
            length_1 = len(result_1)
            primes_1=list(result_1)
            for i in range(0, length_1):
                if(result_1[primes_1[i]]==0):
                    del result_1[primes_1[i]]
            length_1 = len(result_1)
            primes_1=list(result_1)
            d1 = 1
            cnt=0
            for i in range(0, length_1):
                if(result_1[primes_1[i]]>=2):
                    d1 = d1*(primes_1[i]**int(result_1[primes_1[i]]//2))
                else:
                    cnt = cnt+1
            if cnt!=0:
                if (d1!=1)&(d1<=10):
                    break
        a=1
        for i in range(0,len(example)):
            d2 = int(c1/(d1**2))
            if(example[i] == d2):
                a=0
        if a == 0:
            break
    c2 = d2
           

    while(True):
        while(True):
            c3 = random.randint(101,999)
            result_3 = soinsoo(c3)
            length_3 = len(result_3)
            primes_3=list(result_3)
            for i in range(0, length_3):
                if(result_3[primes_3[i]]==0):
                    del result_3[primes_3[i]]
            length_3 = len(result_3)
            primes_3=list(result_3)
            d3 = 1
            cnt=0
            for i in range(0, length_3):
                if(result_3[primes_3[i]]>=2):
                    d3 = d3*(primes_3[i]**int(result_3[primes_3[i]]//2))
                else:
                    cnt = cnt+1
            if cnt!=0:
                if (d3!=1)&(d3<=10):
                    break
        a=1
        for i in range(0,len(example)):
            d4 = int(c3/(d3**2))
            if(example[i] == d4):
                a=0
        if a == 0:
            break
    
    d4 = int(c3/(d3**2))
    c4 = d4
    ans = d1-d3
    ex1 = ans-4
    ex2 = ans-3
    ex3 = ans - 2
    ex4 = ans -1
    ex5 = ans
    left = '{'
    right = '}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1=answer_dict.get(4))
    comment = comment.format(c1=c1,left=left,d1=d1,d2=d2,right=right,c3=c3,d3=d3,d4=d4,ans=ans)
    return stem, answer,comment

#234
def realnum311_Stem_162():
    stem = " 세 자연수 $$수식$$a, ` b, ` c$$/수식$$에 대하여 $$수식$${c1} sqrt{c2} ` = ` sqrt a $$/수식$$, $$수식$$sqrt {c3} ` = ` b sqrt c $$/수식$$일 때,"\
           "$$수식$$a ` + ` b ` + c$$/수식$$의 값을 구하시오. {leftg} 단, $$수식$$b ` != ` 1$$/수식$${rightg}\n"
    answer = "(답) {a1}\n"
    comment = "$$수식$${c1} sqrt{c2} ` = ` sqrt {left}{c1} ^ 2 TIMES {c2}{right} ` = ` sqrt {d1}$$/수식$$  $$수식$$THEREFORE ~ a ` = ` {d1}$$/수식$$\n"\
              "또, $$수식$$b ` != ` 1$$/수식$$ 이므로 \n"\
              "$$수식$$sqrt {c3} ` = ` sqrt {left}{d2} ^ 2 TIMES {d3}{right} ` = ` {d2}sqrt{d3}$$/수식$$  $$수식$$THEREFORE ~ b ` = ` {d2} `$$/수식$$$$수식$$c ` = ` {d3}$$/수식$$\n"\
              "$$수식$$THEREFORE ~ a ` + ` b ` + ` c ` = ` {d1} ` + ` {d2} ` + ` {d3} ` = ` {ans}$$/수식$$\n\n"
    c1 = random.randint(2,5)
    while(True):
        while(True):
            c2 = random.randint(2,5)
            if(c2!=4):
                break
        while(True):
            c3 = random.randint(10,50)
            if non_integer(c3):
                break
        d1 = c1*c1*c2
        if out_route(c3)!=0:
            d2 = out_route(c3)
            break
        else:
            continue
    d3 = c3//d2
    ans = d1+d2+d3
    left = '{'
    right='}'
    leftg='('
    rightg=')'
    stem = stem.format(c1=c1,c2=c2,c3=c3,leftg=leftg,rightg=rightg)
    answer = answer.format(a1=ans)
    comment = comment.format(c1=c1,c2=c2,left=left,right=right,d1=d1,c3=c3,d2=d2,d3=d3,ans=ans)
    return stem, answer, comment

#235
def realnum311_Stem_163():
    stem = "다음 □ 안에 들어갈 수 중 가장 큰 것은?\n"\
           "① $$수식$$ - sqrt {c1} ` = ` - {c2} sqrt {left}{left} BOX{left} ` ` ` ` ` ` ` ` ` ` {right}{right}{right}$$/수식$$\n"\
           "② $$수식$$ sqrt {c3} ` = ` {left} BOX {left} ` ` ` ` ` ` ` ` ` ` {right}{right} sqrt {c4}$$/수식$$\n"\
           "③ $$수식$$ sqrt {c5} ` = ` {c6} sqrt {left}{left} BOX {left} ` ` ` ` ` ` ` ` ` ` {right}{right}{right}$$/수식$$\n"\
           "④ $$수식$$ sqrt {c7} ` = ` {left} BOX {left} ` ` ` ` ` ` ` ` ` ` {right}{right} sqrt {c8}$$/수식$$\n"\
           "⑤ $$수식$$ sqrt {c9} ` = ` {left} BOX {left} ` ` ` ` ` ` ` ` ` ` {right}{right} sqrt {c10}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "① $$수식$$ - sqrt {c1} ` = ` - sqrt{left} {d1} ^ 2 TIMES {d2}{right} ` = ` -{d1} sqrt{d2}$$/수식$$\n"\
              "$$수식$$THEREFORE ~ {left} BOX {left} ` ` ` ` ` ` ` `{right}{right} ` = ` {d2}$$/수식$$\n"\
              "② $$수식$$ sqrt {c3} ` = ` sqrt{left}{d3} ^ 2 TIMES {d4}{right} ` = ` {d3} sqrt{d4}$$/수식$$  $$수식$$THEREFORE ~ {left} BOX {left} ` ` ` ` ` ` ` ` {right}{right} ` = `{d3}$$/수식$$\n"\
              "③ $$수식$$ sqrt {c5} ` = ` sqrt{left}{d5} ^ 2 TIMES {d6}{right} ` = ` {d5} sqrt{d6}$$/수식$$  $$수식$$THEREFORE ~ {left} BOX {left} ` ` ` ` ` ` ` ` {right}{right} ` = `{d6}$$/수식$$\n"\
              "④ $$수식$$ sqrt {c7} ` = ` sqrt{left}{d7} ^ 2 TIMES {d8}{right} ` = ` {d7} sqrt{d8}$$/수식$$  $$수식$$THEREFORE ~ {left} BOX {left} ` ` ` ` ` ` ` ` {right}{right} ` = `{d7}$$/수식$$\n"\
              "⑤ $$수식$$ sqrt {c9} ` = ` sqrt{left}{d9} ^ 2 TIMES {d10}{right} ` = ` {d9} sqrt{d10}$$/수식$$  $$수식$$THEREFORE ~ {left} BOX {left} ` ` ` ` ` ` ` ` {right}{right} ` = `{d9}$$/수식$$\n"\
              "따라서 □ 안에 들어갈 수 중 가장 큰 것은 {ans}이다.\n\n"
    listnum = [10, 12, 14, 15, 18, 20, 24, 25,26, 27, 28, 30, 32, 34, 35, 36, 38, 40, 42, 45, 47, 48, 49, 52, 54, 56, 57, 58, 60, 62, 63, 64, 66, 68, 69, 70, 72, 75, 76, 78, 80, 82, 84, 81, \
               86, 88, 89, 90, 92, 93, 95, 96, 98, 100, 102, 104, 105, 106, 108, 111, 112, 114, 116, 118, 120, 180, 150, 168]

    ######  1번  #######
    while (True):
        while(True):
            c1 = random.choice(listnum)
            if non_integer(c1):
                break
        if out_route(c1)!=0:
            c2 = out_route(c1)
            d1 = c2
            d2 = int(c1 // (c2**2))
            break

    ######  1번  ######

    ######  2번  #######
    while (True):       
        while(True):
            c3 = random.choice(listnum)
            if non_integer(c3):
                break
        if out_route(c3)!=0:
            d3 = out_route(c3)
            d4 = int(c3 // (d3**2))
            c4 = d4
            break

    ######  2번  ######

    ######  3번  #######
    while (True):
        while(True):
            c5 = random.choice(listnum)
            if non_integer(c5):
                break
        if out_route(c5)!=0:
            c6 = out_route(c5)
            d5 = c6
            d6 = int(c5 // (d5**2))
            break
    ######  3번  ######

    ######  4번  #######
    while (True):
        while(True):
            c7 = random.choice(listnum)
            if non_integer(c7):
                break
        if out_route(c7)!=0:
            d7 = out_route(c7)
            d8 = int(c7 // (d7**2))
            c8 = d8
            break
    ######  4번  ######

    ######  5번  #######
    while (True):
        while(True):
            c9 = random.choice(listnum)
            if non_integer(c9):
                break
        if out_route(c9)!=0:
            d9 = out_route(c9)
            d10 = int(c9 // (d9**2))
            c10 = d10
            break
        else:
            a=1
    ######  5번  ######
    left = '{'
    right = '}'
    leftg='('
    rightg=')'
    
    anses=[d2,d3,d6,d7,d9]
    Max = 0
    for i in range(0,5):
        if Max <=anses[i]:
            Max = anses[i]
            k=i

        else:
            Max = Max

    
        
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8,c9=c9,c10=c10,left=left,right=right)
    answer =answer.format(a1 = answer_dict.get(k))
    comment = comment.format(c1=c1,left=left,d1=d1,d2=d2,right=right,c3=c3,d3=d3,d4=d4,c5=c5,d5=d5,d6=d6,c7=c7,d7=d7,d8=d8,c9=c9,d9=d9,d10=d10,ans= answer_dict.get(k))
    return stem, answer, comment

#236
def realnum311_Stem_164():
    stem = "다음 중 가장 큰 수는?\n"\
           "① $$수식$$sqrt{c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3} sqrt{c4}$$/수식$$     ④ $$수식$${c5} sqrt{c6}$$/수식$$     ⑤ $$수식$${c7} sqrt{c8}$$/수식$$\n"

    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
             "① $$수식$$sqrt{c1}$$/수식$$\n"\
             "② $$수식$${c2} ` = ` sqrt {d1}$$/수식$$\n"\
             "③ $$수식$${c3} sqrt{c4} ` = ` sqrt{left}{c3}^2 TIMES {c4}{right} ` = ` sqrt{d2} $$/수식$$ \n"\
             "④ $$수식$${c5} sqrt{c6} ` = ` sqrt {left} {c5} ^ 2 TIMES {c6}{right} ` = ` sqrt{d3}$$/수식$$\n"\
             "⑤ $$수식$${c7} sqrt{c8} ` = ` sqrt {left} {c7} ^ 2 TIMES {c8}{right} ` = ` sqrt{d4}$$/수식$$\n"\
             "따라서 가장 큰 수는 $$수식$${c7} sqrt{c8}$$/수식$$이다.\n\n"
    while(True):
        while(True):
            c1 = random.randint(10, 20)
            c2 = random.randint(2,5)
            c3 = random.randint(2,4)
            c4 = random.randint(2,5)
            c5 = random.randint(2,4)
            c6 = random.randint(5,10)
            c7 = random.randint(3,5)
            c8 = random.randint(3,6)
            if (non_integer(c1))&(non_integer(c4))&(non_integer(c6))&(non_integer(c8)):
                break
        d1 = c2*c2
        d2 = c3*c3*c4
        d3 = c5*c5*c6
        d4 = c7*c7*c8
        list = [c1,d1,d2,d3,d4]
        max=0
        for i in range(0,len(list)):
            if max <=list[i]:
                max = list[i]
                k = i
            else:
                max=max
        b=1
        for i in range(0,len(list)):
            if list[k] == list[i]:
                if(k==i):
                    b=1
                else:
                    b=0
                    break
            else:
                b=1
                
        if k == 4:
            if b==1:
                break
    left = '{'
    right='}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8)
    answer = answer.format(a1 = answer_dict.get(4))
    comment = comment.format(c1=c1,c2=c2,d1=d1,c3=c3,c4=c4,left=left,right=right,d2=d2,c5=c5,c6=c6,d3=d3,c7=c7,c8=c8,d4=d4)
    return stem, answer, comment

#237
def realnum311_Stem_165():
    stem = "다음을 만족시키는 양의 유리수 $$수식$$a,``b,``c$$/수식$$에 대하여 $$수식$$ sqrt{left}ac over b{right}$$/수식$$의 값은?\n"\
           "$$표$$$$수식$$sqrt{c1} `=`{c2} sqrt a$$/수식$$,$$수식$$ sqrt{c3} `=` {c4} sqrtb $$/수식$$, $$수식$$ sqrt{c5}`=` {c6} sqrt c $$/수식$$ $$/표$$\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     ④ {ex4}     ⑤ {ex5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$ sqrt{c1} `=` sqrt{left}{c2} ^ 2 TIMES {d1}{right} `=` {c2} sqrt{d1} $$/수식$$이므로\n"\
              "$$수식$$ a`=` {d1} $$/수식$$\n"\
              "$$수식$$ sqrt{c3} `=` sqrt{left}{c4} ^ 2 TIMES {d2}{right} `=` {c4} sqrt{d2} $$/수식$$이므로\n"\
              "$$수식$$ b `=` {d2} $$/수식$$\n"\
              "$$수식$$ sqrt{c5} `=` sqrt{left}{c6} ^ 2 TIMES {d3}{right} `=` {c6} sqrt{d3} $$/수식$$이므로\n"\
              "$$수식$$ c`=` {d3} $$/수식$$\n"\
              "$$수식$$ THEREFORE ~ sqrt{left}ac over b {right}`=` sqrt{left}{left}{d1} TIMES {d3}{right} over {d2}{right} `=` sqrt {d4} $$/수식$$\n"\
              "$$수식$$ `=` sqrt{left}{d5}^2 TIMES {d6}{right}`=` {d5} sqrt{d6} $$/수식$$\n\n"
    listnum1 = [2,3,5,6,8,10]
    listnum2 = [5,10]
    listnum3 = [200,300,500,600,700,800,1000,1200,1500]
    while(True):
        while(True):
            while(True):
                c1 = random.randint(10,80)
                if(non_integer(c1)) :
                    break
            a=0
            if(out_route(c1)!=0):
                for i in range(0,len(listnum1)):
                    d1 = int(c1/(out_route(c1)**2))
                    if(d1==listnum1[i]):
                        c2 = out_route(c1)
                        a=1
                        break
                    else:
                        a=0
            if(a==1):
                break
        while(True):
            while(True):
                c3 = random.randint(31,300)
                if(non_integer(c3)):
                    break
            b = 0
            if(out_route(c3)!=0):
                for i in range(0,len(listnum1)):
                    d2 = int(c3 / out_route(c3)**2)
                    if(d2==listnum1[i]):
                        c4 = out_route(c3)
                        b = 1
                        break
                    else:
                        b = 0
            if (b ==1):
                    break
        while(True):
            a=0
            c5 = random.choice(listnum3)
            if(out_route(c5)!=0):
                d3 = int(c5 / (out_route(c5))**2)
                c6 = out_route(c5)
                a=1
            if (a==1):
                break
                
        ja = d1 * d3
        mo = d2
        if(gcd(ja,mo)==mo):
            d4 = int(ja/mo)
            if(out_route(d4)!=0):
                d5 = out_route(d4)
                d6 = int(d4/(d5**2))
                break
        
    
    ex4 = "$$수식$$ {e1} sqrt {e2} $$/수식$$".format(e1 = d5, e2 = d6)
    num = d5*d5*d6
    cmp = d6 -1
    if (d6 == 2) :
        ex1 = "1"
        ex2 = "$$수식$$sqrt 2$$/수식$$"
        sss = random.randint(0,2)
        ssss = d5 + sss
        ex3 = "$$수식$$ {h1} sqrt{h2} $$/수식$$".format(h1 = ssss, h2 = 2)
        cmp2 = 1
        while(True):
            if( int((num)**0.5) < cmp2):
                break
            else:
                ss = random.randint(1,4)
                cmp2 = cmp2 + ss
        ex5 = "$$수식$$ {i1} $$/수식$$".format(i1 = cmp2)
    else:
        while(True):
            if(non_integer(cmp)):
                break
            else:
                cmp = cmp-1
        ex1 = "$$수식$$ sqrt{f1}$$/수식$$".format(f1= cmp)
        ex2 = "$$수식$$ sqrt{g1} $$/수식$$".format(g1 = d6)
        sss = random.randint(0,2)
        ssss = d5 + sss
        ex3 = "$$수식$$ {h1} sqrt{h2} $$/수식$$".format(h1 = ssss, h2 = cmp)
        cmp2 = 1
        while(True):
            if( int((num)**0.5) < cmp2):
                break
            else:
                ss = random.randint(1,4)
                cmp2 = cmp2 + ss
        ex5 = "$$수식$$ {i1} $$/수식$$".format(i1 = cmp2)
    left = '{'
    right = '}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5, left = left, right=right)
    answer = answer.format(a1 = answer_dict.get(3))
    comment = comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,d1=d1,d2=d2,d3=d3,d4=d4,d5=d5,d6=d6,left=left,right=right)
    return stem, answer, comment

#238
def realnum311_Stem_166():
    stem = "$$수식$$ sqrt{c1} TIMES sqrt{c2} TIMES sqrt{c3} TIMES sqrt{c4} TIMES sqrt{c5} TIMES sqrt{c6} `=`A sqrt{c7}$$/수식$$일 때,"\
           "유리수 $$수식$$ A $$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$ sqrt{c1} TIMES sqrt{c2} TIMES sqrt{c3} TIMES sqrt{c4} TIMES sqrt{c5} TIMES sqrt{c6}$$/수식$$\n"\
              "$$수식$$ `=` {d1} sqrt{left}{cond1}{cond2}{cond3}{cond4}{cond5}{cond6}{right}$$/수식$$\n"\
              "$$수식$$ {d1} sqrt{left}{cond7}{right}$$/수식$$\n"\
              "$$수식$$ {d1} sqrt{left}{cond8}{right}$$/수식$$\n"\
              "$$수식$$ {d1} TIMES {d2}sqrt{d3} `=` {d4} sqrt{d3}$$/수식$$\n"\
              "$$수식$$ THEREFORE ~ A `=` {d4}$$/수식$$\n\n"
    while(True):
        c1 = random.randint(2,7)
        if(c1!=4):
            break
    c2 = c1 + 1 # 3 ~ 8
    c3 = c2 + 1 #(4 ~ 9)
    c4 = c3 + 1 #( 5 ~ 10 )
    c5 = c4 + 1 # 6 ~ 11
    c6 = c5 + 1 # 7 ~ 12
    d1 = 1
    num1 = 1
    if(non_integer(c1)):
        if(c1 ==6):
            cond1 = "2 TIMES 3 TIMES"
            num1 = 6 * num1
        else:
            cond1 = "{b1} TIMES".format(b1 = c1)
            num1 = num1 * c1
            
    else:
        d1 = d1 * int(c1**0.5)
        cond1 = ''
        num1 = num1

        
    #################################
        
    if(non_integer(c2)):
        if(c2 ==6):
            cond2 = " 2 TIMES 3 TIMES"
            num1 = num1 * 6
        elif(c2 ==8):
            d1 = d1 * 2
            cond2 = " {b2} TIMES".format(b2 = 2)
            num1 = num1 * 2
        else:
            cond2 = " {b2} TIMES".format(b2 = c2)
            num1 = num1 *c2
    else:
        d1 = d1 * int(c2**0.5)
        cond2 = ''
        num1 = num1
    ################################
        
    if(non_integer(c3)):
        if( c3 == 6 ):
            cond3 = " 2 TIMES 3 TIMES"
            num1 = num1 * 6
        elif ( c3 == 8 ):
            d1 = d1 * 2
            cond3 = " {b3} TIMES".format(b3 = 2)
            num1 = num1 *2
        else:
            cond3 = " {b3} TIMES".format(b3 = c3)
            num1 = num1 * c3
    else:
        d1 = d1 * int(c3**0.5)
        cond3 = ''
        num1 = num1

    ###################################

        
    if(non_integer(c4)):
        if( c4 == 6 ):
            cond4 = " 2 TIMES 3 TIMES"
            num1 = num1 * 6
        elif ( c4 == 8 ):
            d1 = d1 * 2
            cond4 = " {b4} TIMES".format(b4 = 2)
            num1 = num1*2
        elif(c4==10):
            cond4 = " 2 TIMES 5 TIMES"
            num1 = num1 * 10
        else:
            cond4 = " {b4} TIMES".format(b4 = c4)
            num1 = num1*c4
        
    else:
        d1 = d1 * int(c4**0.5)
        cond4 = ''
        num1 = num1

    ####################################

    if(non_integer(c5)):
        if( c5 == 6 ):
            cond5 = " 2 TIMES 3 TIMES"
            num1 = num1 * 6
        elif ( c5 == 8 ):
            d1 = d1 * 2
            cond5 = " {b5} TIMES".format(b5 = 2)
            num1 = num1 * 2
        elif(c5==10):
            cond5 = " 2 TIMES 5 TIMES"
            num1 = num1 * 10
        else:
            cond5 = " {b5} TIMES".format(b5 = c5)
            num1 = num1 * c5
    else:
        d1 = d1 * int(c5**0.5)
        cond5 = ''
        num1 = num1

    ################################
        
    if(non_integer(c6)):
        if(c6 == 8):
            d1 = d1 * 2
            cond6 = " {b6}".format(b6 = 2)
            num1 = num1 * 2
        elif(c6==10):
            cond6 = " 2 TIMES 5"
            num1 = num1 * 10
        elif(c6 == 12):
            d1 = d1*2
            cond6 = " 3"
            num1 = num1 * 3
        else:
            cond6 = " {b6}".format(b6=c6)
            num1 = num1 * c6
    else:
        d1 = d1 * int(c6**0.5)
        cond6 = ''
        num1 = num1

    ###############################
    result = soinsoo(num1)
    list1 = list(result)
    dict1={}
    for i in range( 0,len(result)):
        if(result[list1[i]]==0):
            del result[list[i]]
    list1 = list(result)
    for i in range(0,len(result)):
        if(result[list1[i]]>=2):
            dict1[list1[i]] = int(result[list1[i]]//2)
            result[list1[i]] = result[list1[i]] - 2 * int(result[list1[i]]//2)
            if (result[list1[i]]==0):
                del result[list1[i]]
    list1 = list(result)
    list2 = list(dict1)
    if (len(dict1)==1):
        tempt1 = "{e1} ^ 2".format(e1 = list2[0])
        tempt3 = tempt1
    else:
        tempt1 = "{e1} ^ 2 TIMES {e2} ^ 2".format(e1 = list2[0], e2 = list2[1])
        tempt3 = "{leftg}{e1} TIMES {e2}{rightg}^2".format(e1 = list2[0], e2 = list2[1],leftg='(', rightg=')')
    if ( len(result)==1):
        tempt2 = " TIMES {f1}".format(f1 = list1[0])
    elif( len(result)==2):
        tempt2 = " TIMES {f1} TIMES {f2}".format(f1 = list1[0], f2 = list1[1])
    elif ( len(result)==3):
        tempt2 = " TIMES {f1} TIMES {f2} TIMES {f3}".format(f1 = list1[0], f2 = list1[1], f3 = list1[2])
    else:
        tempt2 = " TIMES {f1} TIMES {f2} TIMES {f3} TIMES {f4}".format(f1 = list1[0], f2 = list1[1], f3 = list1[2], f4 = list1[3])
    cond7 = tempt1 + tempt2
    cond8 = tempt3 + tempt2
    d2 = out_route(num1)
    d3 = int(num1 / (d2*d2))
    d4 = d2 * d1
    c7 = d3
    left = '{'
    right ='}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7)
    answer = answer.format(a1 = d4)
    comment = comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,cond1=cond1,cond2=cond2,cond3=cond3,cond4=cond4,cond5=cond5,cond6=cond6,d1=d1,cond7=cond7,\
                             cond8=cond8, left=left,right=right, d2=d2,d3=d3,d4=d4)
    return stem, answer, comment

#240
def realnum311_Stem_167():
    stem = "$$수식$$ sqrt {c1} TIMES sqrt{c2} TIMES sqrt{c3} `=` a sqrt{c4}$$/수식$$을 만족시키는 자연수 $$수식$$ a $$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "$$수식$$ sqrt {c1} TIMES sqrt{c2} TIMES sqrt{c3} `=` sqrt{left}{cond1}{right} `=` {d1} sqrt{d2}$$/수식$$\n"\
              "$$수식$$ THEREFORE ~ a`=` {d1}$$/수식$$\n\n"
    num1 = [10,12,14,15,18,20]
    num2 = [21,24,27,28,30,32,35,40,42,45,48,52,54,56,60,68]
    while(True):
        while(True):
            num = 1
            c1 = random.randint(3,8)
            if(non_integer(c1)):
                if(c1 == 6):
                    tempt1 = "2 TIMES 3 TIMES"
                    num = num * 6
                elif(c1 == 8):
                    tempt1 = "2 ^ 3 TIMES"
                    num = num * 8
                else:
                    tempt1 =" {e1} TIMES ".format(e1 = c1)
                    num = num * c1
                break
        c2 = random.choice(num1)
        result2 = soinsoo(c2)
        list2 = list(result2)
        for i in range( 0,len(result2)):
            if(result2[list2[i]] == 0):
                del result2[list2[i]]
        list2 = list(result2)
        if ((len(list2)) == 2):
            tempt2 = "{e1} ^ {e2} TIMES {e3} TIMES".format(e1 = list2[0], e2 = 2, e3 = list2[1])

        elif(c2 == 10):
            tempt2 = "2 TIMES 5 TIMES"
            tempt2_2=''
        elif(c2 == 14):
            tempt2 = "2 TIMES 7 TIMES "
            tempt2_2=''
        elif(c2 == 15):
            tempt2 = "3 TIMES 5 TIMES "
            tempt2_2=''
        elif(c2 == 18):
            tempt2 = "3 ^ 2 TIMES 2 TIMES "
        
        c3 = random.choice(num2)
        result3 = soinsoo(c3)
        list3 = list(result3)
        for i in range( 0,len(result3)):
            if(result3[list3[i]] == 0):
                del result3[list3[i]]
        list3 = list(result3)
        if ((len(list3)) == 1):
            if(result3[list3[0]]==1):
                tempt3 = "{e1} ".format(e1 = list3[0])
            else:
                tempt3 = "{e1}^{e2} ".format(e1 = list3[0],e2=result3[list3[0]])
        elif((len(list3) == 2)):
            tempt3 = "{e1} ^ {e2} TIMES {e3}".format(e1 = list3[0], e2 = result3[list3[0]], e3 = list3[1])
        elif((len(list3) == 3)):
            tempt3 = "{e1} ^ {e2} TIMES {e3} TIMES {e4} ".format(e1 = list3[0], e2 = result3[list3[0]], e3 = list3[1], e4 = list3[2])
               
        elif(c3 == 21):
            tempt3 = "3 TIMES 7"
        elif(c3 == 30):
            tempt3 = "2 TIMES 3 TIMES 5 "
        elif(c3 == 42):
            tempt3 = "2 TIMES 3 TIMES 7 "
        if(c2<c3):
            num = num * c2 * c3
            if(out_route(num)!=0):
                c4 = int(num/(out_route(num)**2))
                d1 = out_route(num)
                d2 = c4
                if(d1>3):
                    break
        cond1 = tempt1 + tempt2 + tempt3
        ex1 = 1
        ex2 =1
        ex3=1
        ex5=1
    while(True):
        ex1 = random.randint(1,(d1-1))
        ex2 = random.randint(1,(d1-1))
        ex3 = random.randint(1,(d1-1))
        ex4 = d1
        ex5 = random.randint((d1+1),(d1+6))
        if(ex1<ex2)&(ex2<ex3):
            break
    cond1 = tempt1 + tempt2 + tempt3 
    left = '{'
    right='}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1 = answer_dict.get(3))
    comment = comment.format(c1=c1,c2=c2,c3=c3,d1=d1,d2=d2,left=left,right=right,cond1=cond1)
    return stem, answer, comment

#242
def realnum311_Stem_168():
    stem = "다음 수를 크기가 작은 것부터 례대로 나열하였을 때, 두 번째에 오는 수를 구하시오.\n"\
           "$$표$$$$수식$$ {c1}sqrt{c2}$$/수식$$, $$수식$$ {c3} $$/수식$$, $$수식$$sqrt{c4}$$/수식$$, $$수식$${c5}sqrt{c6}$$/수식$$ $$/표$$\n"\
           "① {ex1}     \n② {ex2}   \n③ {ex3}     \n④ {ex4}     \n⑤ {ex5}\n"
    answer = "(답) \n"
    comment = "(해설)\n"\
              "$$수식$$ {c1} sqrt{c2} `=`sqrt{left}{c1}^2 TIMES {c2}{right}`=`sqrt{d1}$$/수식$$, $$수식$${c3} `=` sqrt{d2}$$/수식$$,\n"\
              "$$수식$${c5}sqrt{c6} `=` sqrt{left}{c5}^2 TIMES {c6}{right}`=` sqrt{d3}$$/수식$$이므로 \n"\
              "$$수식$$ {c3} `&lt;` sqrt{c4}  `&lt;` {c5}sqrt{c6}  `&lt;` {c1}sqrt{c2}$$/수식$$\n\n"
    while(True):
        while(True):
            c1 = random.randint(2,3)
            c2 = random.randint(2,6)
            c3 = random.randint(2,5)
            c4 = random.randint(10,24)
            c5 = random.randint(2,4)
            c6 = random.randint(2,6)
            
            if(non_integer(c2))&(non_integer(c4))&(non_integer(c6)):
                break
        d1 = c1*c1*c2
        d2 = c3*c3
        d3 = c5*c5*c6
        if(d1>d3)&(d3>c4)&(c4>d2):
            break
        
    left='{'
    right='}'
    ex1 = "$$수식$$ {c1}sqrt{c2} &lt;  &lt; {c3} &lt; sqrt{c4}$$/수식$$".format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6)
    ex2 = "$$수식$$ {c1}sqrt{c2} &lt; {c3} &lt; {c5}sqrt{c6} &lt; sqrt{c4}$$/수식$$".format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6)
    ex3 = "$$수식$$ {c5}sqrt{c6} &lt; {c1}sqrt{c2} &lt; {c3} &lt; sqrt{c4}$$/수식$$".format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6)
    ex4 = "$$수식$$ {c3} &lt; sqrt{c4} &lt; {c1}sqrt{c2} &lt; {c5}sqrt{c6}$$/수식$$".format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6)
    ex5 = "$$수식$$ {c3} &lt; sqrt{c4} &lt; {c5}sqrt{c6} &lt; {c1}sqrt{c2}$$/수식$$".format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6)
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(answer_dict.get(4))
    comment = comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,d1=d1,d2=d2,d3=d3,left=left,right=right)
    return stem, answer, comment  

#243
def realnum311_Stem_169():
    stem = "$$수식$$ sqrt {left} {c1} + {c2}x {right} ` = ` {c3} sqrt {c4}$$/수식$$를 만족시키는 $$수식$$ x $$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "$$수식$${c3} sqrt {c4} ` = ` sqrt {left} {c3} ^ 2 TIMES {c4} {right} ` = ` sqrt{d1}$$/수식$$이므로\n"\
              "$$수식$$ {c1} + {c2}x ` = ` {d1}$$/수식$$, $$수식$${c2}x ` = ` {d2}$$/수식$$    $$수식$$THEREFORE ~ x ` = ` {ans}$$/수식$$\n\n"
    while(True):
        c1 = random.randint(10, 20)
        c2 = random.randint(2,6)
        c3 = random.randint(2,4)
        while(True):
            c4 = random.randint(3,6)
            if(c4!=4):
                break
        d1 = c3*c3*c4
        d2 = d1 - c1
        if(d2%c2==0):
            if(d2!=c2):
                break
    ans = int(d2/c2)
    ex1 = ans-1
    ex2=ans
    ex3=ans+1
    ex4=ans+2
    ex5=ans+3
    left='{'
    right='}'
    stem = stem.format(left=left,c1=c1,c2=c2,right=right,c3=c3,c4=c4,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1=answer_dict.get(1))
    comment = comment.format(c3=c3,c4=c4,left=left,right=right,d1=d1, c1=c1,c2=c2,d2=d2,ans=ans)
    return stem, answer, comment

#244
def realnum311_Stem_170():
    stem = "$$수식$$ a &gt; 0$$/수식$$, $$수식$$ b &gt; 0$$/수식$$, $$수식$$ ab ` = `{c1}$$/수식$$ 일 때,"\
           "$$수식$$ a sqrt {left}{c2}b over a{right} `+`b sqrt {left}{c3}a over b{right} `$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "$$수식$$ a sqrt {left}{c2}a over b{right} `+`b sqrt {left}{c3}b over a{right} ` = ` sqrt{left} a ^ 2 TIMES {c2}b overa{right} ` + ` sqrt{left} b ^ 2 TIMES {c3}a over b {right}$$/수식$$\n"\
              "$$수식$$= sqrt{left}{c2}ab{right} + sqrt{left}{c3}ab{right}$$/수식$$\n"\
              "$$수식$$= {d1}sqrt{left}ab{right} + {d2}sqrt{left}ab{right}$$/수식$$\n"\
              "$$수식$$ab ` = ` {c1}$$/수식$$을 위의 식에 대입하면\n"\
              "$$수식$$= {d1}sqrt{left}ab{right} + {d2}sqrt{left}ab{right} ` = ` {d1}sqrt{c1} + {d2}sqrt{c1}$$/수식$$\n"\
              "$$수식$$= {d3} + {d4} ` = `{d5}$$/수식$$\n\n"
    listnum=[4,9,16,25,36,49,64,81]
    listnum2=[4,9,16,25]
    while(True):
        c1 = random.choice(listnum)
        c2 = random.choice(listnum2)
        c3 = random.choice(listnum2)
        if (c2!=c3):
            break
    d1 = int(c2**0.5)
    d2 = int(c3**0.5)
    d3 = int(c1**0.5)*d1
    d4 = int(c1**0.5)*d2
    d5 = d3+d4
    left='{'
    right='}'
    while(True):
        k = 2
        exlist=[]
        for i in range(0,d5):
            if (d5%k)==0:
                exlist.append(k)
                k=k+1
            else:
                k = k+1
        multi = random.choice(exlist)
        ex1 = d5 - (multi*4)
        ex2 = d5 - (multi*3)
        ex3 = d5 - (multi*2)
        ex4 = d5 - multi
        ex5 = d5
        if(ex1>0):
            break
    stem = stem.format(c1=c1,left=left,c2=c2,right=right,c3=c3,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1 = answer_dict.get(4))
    comment = comment.format(left = left, c2=c2,right=right,c3=c3,d1=d1,d2=d2,c1=c1,d3=d3,d4=d4,d5=d5)
    return stem, answer, comment

#245
def realnum311_Stem_171():
    stem = "$$수식$$ {c1}sqrt{c2} TIMES sqrt{left}{c3} over {c4} {right}$$/수식$$를 계산하여 근호 안의 수가 가장 작은 자연수가 되도록 $$수식$$a sqrt b$$/수식$$"\
           "꼴로 나타내었을 때, 자연수 $$수식$$ a, ` b$$/수식$$에 대하여 $$수식$$a ` + ` b$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}"
    comment = "(해설)\n"\
              "$$수식$$ {c1}sqrt{c2} TIMES sqrt{left}{c3} over {c4} {right} ` = ` {c1} sqrt {left}{c2} TIMES {c3}over{c4}{right}$$/수식$$\n"\
              "$$수식$$= {c1} sqrt {d1} ` = ` {d2} sqrt{d3}$$/수식$$\n"\
              "따라서 $$수식$$a ` = ` {d2}$$/수식$$, $$수식$$b ` = ` {d3}$$/수식$$이므로\n"\
              "$$수식$$ a ` + ` b = {d4}$$/수식$$\n\n"
    numlist=[12, 14, 15, 18, 20, 21, 24, 27, 28, 30, 32, 35, 40, 45, 48, 56]
    while(True):
        while(True):
            c1 = random.randint(2,4)
            c2 = random.randint(5,8)
            c3 = random.choice(numlist)
            c4 = random.randint(5, 20)
            if (gcd(c2,c4)!=1)&(gcd(c3,c4)==1):
                break
        ja = c2*c3
        if(gcd(ja,c4)!=c4):
            continue
        else:
            d1 = int(ja/c4)
            if(out_route(d1)!=0):
                d2 = c1 * (out_route(d1))
                d3 = int(d1/((out_route(d1))**2))
                break
            else:
                continue
    d4 = d2+d3
    left='{'
    right='}'
    ex1 = d4-4
    ex2=d4-3
    ex3 = d4-2
    ex4=d4-1
    ex5=d4
    stem = stem.format(c1=c1,c2=c2,left=left,c3=c3,c4=c4,right=right, ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1 = answer_dict.get(4))
    comment = comment.format(c1=c1,c2=c2,left=left,c3=c3,c4=c4,right=right,d1=d1,d2=d2,d3=d3,d4=d4)
    return stem, answer, comment

#246
def realnum311_Stem_172():
    stem = "다음 중 옳지 않은 것은?\n"\
          "① $$수식$$sqrt {c1} DIVIDE sqrt {c2} ` = ` sqrt {c3}$$/수식$$ \n"\
          "② $$수식$$- {left}sqrt {c4}{right} over {left}sqrt {c5}{right} `=`- sqrt {c6}$$/수식$$ \n"\
          "③ $$수식$$sqrt {left}{c7} over {c8}{right} DIVIDE sqrt {left}1 over {c10}{right} `=`{c11}$$/수식$$ \n"\
          "④ $$수식$$- sqrt {c12} DIVIDE sqrt {left}{c13} over {c14}{right} `=`-{c15}$$/수식$$ \n"\
          "⑤ $$수식$$ sqrt {c16} DIVIDE sqrt {c17} DIVIDE  {leftg} - sqrt {left}{c18} over {c19}{right}  {rightg} `=`- sqrt {ans}$$/수식$$ \n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "① $$수식$$sqrt {c1} DIVIDE sqrt {c2} `=` sqrt {c3}$$/수식$$\n"\
              "② $$수식$$- {left}sqrt {c4}{right} over {left}sqrt {c5}{right} `=`- sqrt {c6}$$/수식$$\n"\
              "③ $$수식$$sqrt {left}{c7} over {c8}{right} DIVIDE sqrt {left}1 over {c10}{right} `=`{c11}$$/수식$$\n"\
              "④ $$수식$$- sqrt {c12} DIVIDE sqrt {left}{c13} over {c14}{right} `=`-{c15}$$/수식$$\n"\
              "⑤ $$수식$$ sqrt {c16} DIVIDE sqrt {c17} DIVIDE  {leftg} - sqrt {left}{c18} over {c19}{right}  {rightg} `=`- sqrt {c20}$$/수식$$\n\n"
    ############## 1번###############
    while(True):
        c1 = random.randint(2,15)
        c2 = random.randint(2,6)
        if(gcd(c1,c2)==c2):
            break
    c3 = int(c1/c2)
    ############ 1번!################

    ############ 2번 ################
    while (True):
        c4 = random.randint(5,20)
        c5 = random.randint(2,3)
        if(gcd(c4,c5)==c5):
            c6 = int(c4/c5)
            if(non_integer(c6)):
                break
    ############ 2번 ###############

    ############ 3번 ###############
    while(True):
        listnum=[4,9,16,25,36]
        c7 = random.choice(listnum)
        c8 = random.randint(2,5)
        c10 = random.randint(2,5)
        if(gcd(c7,c8)==1):
            ja = c7*c10
            if(gcd(ja,c8)==c8):
                cmp = int(ja/c8)
                if non_integer(cmp):
                   continue
                else:
                   c11 = int(cmp**0.5)
                   break                   
            else:
                continue
        else:
            continue
    ########### 3번 ##################

    ########### 4번 ##################
    while(True):
        while(True):
            c12 = random.randint(10, 60)
            c13 = random.randint(3,6)
            c14 = random.randint(2,15)
            if(non_integer(c12))&(non_integer(c13))&(non_integer(c14))&(gcd(c13,c14)==1):
                break
        ja_4 = c12*c14
        if(gcd(ja_4,c13)==c13):
            cmp_4 = int(ja_4/c13)
            if(non_integer(cmp_4)):
                continue
            else:
               c15 = int(cmp_4**0.5)
               break
               
        else:
            continue
    ############ 4번##############

    ########### 5번###############
    while(True):
        while(True):
            c16 = random.randint(3,7)
            c17 = random.randint(6,11)
            c18 = c16
            ans = random.randint(2,5)
            c19 = c17 * ans
            if (non_integer(c16))&(non_integer(c17)):
                break
        cmp_5 = int(c16*c19/(c17*c18))
        if(non_integer(cmp_5)):
            c20 = cmp_5
            break
    ans = c20 + 3
     ########### 5번###############
    left = '{'
    right = '}'
    leftg='('
    rightg=')'
    stem = stem.format(c1=c1,c2=c2,c3=c3,left=left,c4=c4,c5=c5,c6=c6,right=right,c7=c7,c8=c8,c10=c10,c11=c11,c12=c12,c13=c13,c14=c14,c15=c15,\
                       c16=c16,c17=c17,leftg=leftg,rightg=rightg,c18=c18,c19=c19,ans=ans)
    answer=answer.format(a1 = answer_dict.get(4))
    comment = comment.format(c1=c1,c2=c2,c3=c3,left=left,c4=c4,c5=c5,c6=c6,right=right,c7=c7,c8=c8,c10=c10,c11=c11,c12=c12,c13=c13,c14=c14,c15=c15,\
                       c16=c16,c17=c17,leftg=leftg,rightg=rightg,c18=c18,c19=c19,c20=c20)
    return stem, answer, comment

#247
def realnum311_Stem_173():
    stem = "$$수식$$sqrt{c1} DIVIDE sqrt{c2} ` = ` sqrt A$$/수식$$일 때, $$수식$$ A $$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$sqrt{c1} DIVIDE sqrt{c2} ` = ` {left}sqrt {c1}{right} over {left}sqrt {c2}{right} `=` sqrt {left}{c1} over {c2}{right} `=` sqrt {c3} `=` sqrt A `$$/수식$$이므로\n"\
              "$$수식$$ A ` = ` {c3}$$/수식$$\n\n"
    while(True):
        while(True):
            c1 = random.randint(10,100)
            c2 = random.randint(3,7)
            if(non_integer(c1))&(non_integer(c2))&(gcd(c1,c2)==c2):
                break
        c3 = int(c1/c2)
        if(non_integer(c3)):
            break
    left='{'
    right='}'
    stem = stem.format(c1=c1,c2=c2)
    answer = answer.format(a1=c3)
    comment = comment.format(c1=c1,c2=c2,c3=c3,left=left,right=right)
    return stem, answer, comment
    

#248
def realnum311_Stem_174():
    stem = "$$수식$${left}sqrt a{right} over {left}sqrt {c1}{right} ` DIVIDE ` {left}sqrt {c2}{right} over {left}sqrt {c3}{right} ` = ` sqrt {c4} `$$/수식$$"\
           "일 때, 자연수 $$수식$$ a $$/수식$$의 값을 구하시오.\n"
    answer="(답) {a1}\n"
    comment = "$$수식$${left}sqrt a{right} over {left}sqrt {c1}{right} ` DIVIDE ` {left}sqrt {c2}{right} over {left}sqrt {c3}{right} ` = ` "\
              "{left}sqrt a{right} over {left}sqrt {c1}{right} ` TIMES ` {left}sqrt {c3}{right} over {left}sqrt {c2}{right} ` = sqrt {c4} ``$$/수식$$에서\n"\
              "$$수식$$sqrt{left}{d1}a{right} ` = ` sqrt{d2}$$/수식$$, $$수식$${d1}a ` = ` {d2}$$/수식$$   $$수식$$a`=`{d3}$$/수식$$\n\n"
    left='{'
    right='}'
    while(True):
        while(True):
            c1 = random.randint(2,6)
            c2 = random.randint(2,8)
            c3 = random.randint(2,8)
            c4 = random.randint(10,20)
            if(c2!=c3)&non_integer(c1)&non_integer(c2)&non_integer(c3)&non_integer(c4)&(c1!=c2)&(c1!=c3):
                break
        division = gcd(c1,c3)
        if(division == 1):
            d1 = c3
            d2 = c4*c1*c2
        else:
            d1 = int(c3/division)
            d2 = c4*c2*int(c1/division)
        if(gcd(d1,d2)==d1):
            d3 = int(d2/d1)
            break
        else:
            continue
    stem = stem.format(left=left,right=right,c1=c1,c2=c2,c3=c3,c4=c4)
    answer = answer.format(a1=d3)
    comment = comment.format(left=left,right=right,c1=c1,c2=c2,c3=c3,c4=c4,d1=d1,d2=d2,d3=d3)
    return stem, answer, comment

#250
def realnum311_Stem_175():
    stem = "$$수식$${leftg} sqrt {c1} {rightg} ^2$$/수식$$의 음의 제곱근을 $$수식$$ A $$/수식$$, $$수식$$ sqrt {left}-{c2} ^2{right}$$/수식$$의 양의 제곱근"\
           "을 $$수식$$B$$/수식$$라 할 때, $$수식$$  {leftg} A over B  {rightg} ^ 2$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설) \n"\
              "$$수식$${leftg} sqrt {c1} {rightg} ^2 ` = ` {c1}$$/수식$$의 음의 제곱근은 $$수식$$- sqrt{c1}$$/수식$$이므로 $$수식$$A ` = ` - sqrt{c1}$$/수식$$\n"\
              "$$수식$$sqrt {left}-{c2} ^2{right} ` = ` {c2}$$/수식$$의 양의 제곱근은 $$수식$$sqrt{c2}$$/수식$$이므로 $$수식$$ B ` = ` sqrt{c2}$$/수식$$\n"\
              "$$수식$$THEREFORE ~  {leftg} A over B  {rightg} ^2 `=  {leftg} {left}- sqrt {c1}{right} over {left}sqrt {c2}{right}  {rightg} ^2 `=`  {leftg}- sqrt {d1}  {rightg} ^2 `=`{d2}$$/수식$$\n\n"
    while(True):
        while(True):
            c1 = random.randint(5,50)
            c2 = random.randint(2,15)
            if (c1!=c2)&non_integer(c1)&non_integer(c2):
                break
        if(gcd(c1,c2)==c2):
            d1 = int(c1/c2)
            d2 = d1
            break
    left='{'
    right='}'
    leftg='('
    rightg=')'
    stem = stem.format(leftg=leftg, rightg=rightg, c1=c1,c2=c2, left=left,right=right)
    answer = answer.format(a1 = d2)
    comment = comment.format(leftg=leftg,rightg=rightg,c1=c1,c2=c2,d1=d1,d2=d2,left=left,right=right)
    return stem, answer, comment
        
#251
def realnum311_Stem_176():
    stem = " $$수식$$ {c1} sqrt {c2} ` DIVIDE ` {left}sqrt {c3}{right} over {left}sqrt {c4}{right} ` DIVIDE` 1 over {left}sqrt {c5}{right} ` = `n sqrt {c6} ``$$/수식$$"\
           "일 때, 자연수 $$수식$$n$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment="(해설)\n"\
             "$$수식$$ {c1} sqrt {c2} ` DIVIDE ` {left}sqrt {c3}{right} over {left}sqrt {c4}{right} ` DIVIDE` 1 over {left}sqrt {c5}{right} ` = `"\
             "{c1} sqrt {c2} ` TIMES ` {left}sqrt {c4}{right} over {left}sqrt {c3}{right} ` TIMES` sqrt {c5}$$/수식$$\n"\
             "$$수식$$= ` {c1} sqrt{left}{c2} TIMES {c4} over {c3} TIMES {c5} {right}$$/수식$$\n"\
             "$$수식$$ = {d1} sqrt{c6}$$/수식$$\n"\
             "$$수식$$ THEREFORE ~ n ` = ` {d1}$$/수식$$\n\n"
    numlist=[12, 14, 15, 18, 20, 21, 24, 27, 28, 30, 32, 35, 40, 45, 48, 56]
    while(True):
        while(True):
            c1 = random.randint(2,4)
            c2 = random.randint(2,3)
            c3 = random.randint(5,10)
            c4 = random.randint(5,10)
            c5 = random.choice(numlist)
            if(c3!=c4)&non_integer(c3)&non_integer(c4)&(gcd(c3,c4)==1):
                break
        num = c2*c4*c5
        if(gcd(num,c3)==c3):
            cmp = int(num/c3)
            if(out_route(cmp)!=0):
                break
    d1 = c1*out_route(cmp)
    d2 = int(cmp/(out_route(cmp)**2))
    left='{'
    right='}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=d2,left=left,right=right,ex1=d1-3,ex2=d1-2,ex3=d1-1,ex4=d1,ex5=d1+1)
    answer = answer.format(a1 = answer_dict.get(3))
    comment = comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,left=left,right=right,d1=d1,c6=d2)
    return stem, answer, comment

#252
def realnum311_Stem_177():
    stem = " $$수식$${left} {c1}sqrt {c2}{right} over {left}sqrt {c3}{right} DIVIDE  {leftg} - 1 over {left}sqrt {c4}{right}  {rightg} `$$/수식$$"\
           "의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "$$수식$${left} {c1}sqrt {c2}{right} over {left}sqrt {c3}{right} DIVIDE  {leftg} - 1 over {left}sqrt {c4}{right}  {rightg} `$$/수식$$"\
              "$$수식$$` =` {left}{c1}sqrt {c2}{right} over {left}sqrt {c3}{right} TIMES{leftg}- sqrt {c4} {rightg}$$/수식$$"\
              "$$수식$$=`-{c1} sqrt {left}{c2} over {c3} TIMES{c4}{right} `=`-{d1}$$/수식$$\n\n"
    while(True):
        while(True):
            c1 = random.randint(2,6)
            c2 = random.randint(2,40)
            c3 = random.randint(2,20)
            c4 = random.randint(2,10)
            if(c2!=c3)&(c3!=c4)&(non_integer(c2))&(non_integer(c3)):
                if(gcd(c2,c3)==1):
                    break
        cmp = c2*c4
        if(gcd(cmp,c3)==c3):
            num = int(cmp/c3)
            if(non_integer(num)):
                continue
            else:
                multi = int(num**0.5)
                break
    d1 = c1*multi
    left='{'
    right='}'
    leftg='('
    rightg=')'
    stem=stem.format(left=left,c1=c1,c2=c2,right=right,c3=c3,c4=c4,leftg=leftg,rightg=rightg)
    answer = answer.format(a1 = d1)
    comment = comment.format(left=left,c1=c1,c2=c2,right=right,c3=c3,leftg=leftg,rightg=rightg,c4=c4,d1=d1)
    return stem, answer, comment

#253
def realnum311_Stem_178():
    stem = "$$수식$$sqrt{c1}$$/수식$$는 $$수식$$sqrt{c2} over {c3}$$/수식$$의 몇 배인가?\n"\
           "① $$수식$${ex1}$$/수식$$배     ② $$수식$${ex2}$$/수식$$배     ③ $$수식$${ex3}$$/수식$$배     ④ $$수식$${ex4}$$/수식$$배     ⑤ $$수식$${ex5}$$/수식$$배\n"

    answer = "(답) {a1}\n"
    comment = "$$수식$$sqrt {c1} ` ÷ ` {left}sqrt {c2}{right} over {c3} ` = ` sqrt {c1} ` TIMES ` {c3} over {left}sqrt {c2}{right} ` = ` {c3} sqrt {left}{c1} ` TIMES ` 1 over {c2}{right}$$/수식$$\n"\
              "$$수식$$= ` {c3} sqrt {c4} ` = ` {c5}$$/수식$$\n"\
              "따라서 $$수식$$sqrt{c1}$$/수식$$는 $$수식$$sqrt{c2} over {c3}$$/수식$$의 $$수식$${c5}$$/수식$$배이다.\n\n"
    left = '{'
    right='}'
    while(True):
        while(True):
            c1 = random.randint(2,20)
            c2 = random.randint(2,20)
            division = gcd(c1,c2)
            cmp1 = int(c1 / division)
            cmp2 = int(c2/division)
            if(c1!=4)&(c1!=16)&(c1!=9)&(c1!=c2)&(c2!=4)&(c2!=16)&(c2 !=9):
                if cmp2 ==1:
                    break
        c3 = random.randint(2,5)

        result_cmp1 = soinsoo(cmp1)
        length_cmp1 = len(result_cmp1)
        list_cmp1 = list(result_cmp1)
        a=1
        for i in range(0, length_cmp1):
            if result_cmp1[list_cmp1[i]] % 2 ==0:
                a=1
            else:
                a=0
                break

        if (a==1):
            break
    c4 = cmp1
    c5 = c3 * int(c4**0.5)
    ex1 = c5 -2
    ex2 = c5 - 1
    ex3 = c5
    ex4 = c5 + 1
    ex5 = c5 + 2
    stem = stem.format(c1=c1, c2=c2, c3=c3, ex1=ex1, ex2=ex2, ex3=ex3, ex4=ex4, ex5=ex5)
    answer = answer.format(a1 = answer_dict.get(2))
    comment = comment.format(c1=c1, left=left, c2=c2, right=right, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment

#254
def realnum311_Stem_179():
    stem = "다음 중 가장 작은 수는?\n"\
           "① $$수식$${left}sqrt {c1}{right} over {left}sqrt {c2}{right}$$/수식$$    ② $$수식$${left}{c3} sqrt {c4}{right} over {left}sqrt {c5}{right}$$/수식$$"\
           "③ $$수식$${left}{c6} sqrt {c7}{right} over {left}{c8} sqrt {c7}{right}$$/수식$$\n"\
           "④ $$수식$$sqrt {c9} DIVIDE sqrt {c10}$$/수식$$	⑤ $$수식$${c11} sqrt {c12} DIVIDE {c13} sqrt {c14}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "① $$수식$${left}sqrt {c1}{right} over {left}sqrt {c2}{right}`=` sqrt {left}{c1} over {c2}{right} `=` sqrt {d1}$$/수식$$\n"\
              "② $$수식$$ {left}{c3} sqrt {c4}{right} over {left}sqrt {c5}{right}`=`{c3} sqrt {left}{c4} over {c5}{right} `=`{c3} sqrt {d2} `=` sqrt {d3}$$/수식$$\n"\
              "③ $$수식$${left}{c6} sqrt {c7}{right} over {left}{c8} sqrt {c7}{right} ` = ` {c6} over {c8} ` = ` sqrt{left}{d4} over{d5}{right}$$/수식$$\n"\
              "④ $$수식$$sqrt {c9} DIVIDE sqrt {c10}`=`sqrt{c9} over sqrt {c10} ` = ` sqrt{left}{c9}over{c10}{right} ` = ` sqrt{d6}$$/수식$$\n"\
              "⑤ $$수식$${c11} sqrt {c12} DIVIDE {c13} sqrt {c14}`=`{left}{c11}sqrt{c12}{right} over{left}{c13}sqrt{c14}{right} ` = ` {d7}sqrt{left}{c12}over{c14}{right}"\
              "` = ` {d7}sqrt{d8} ` = ` sqrt{d9}$$/수식$$\n"\
              "따라서 가장 작은 수는 {a1}이다.\n\n"

        # 1번
    while(True):
        while(True):
            c1 = random.randint(10,50)
            c2 = random.randint(2,6)
            if(non_integer(c1))&(non_integer(c2))&(gcd(c1,c2)==c2):
                break
        cmp_1 = int(c1/c2)
        if non_integer(cmp_1):
            d1 = cmp_1
            break
            

        # 1번 끝
    #2번 시작
    while(True):
        while(True):
            c3 = random.randint(2,4)
            c4 = random.randint(10,40)
            c5 = random.randint(2,6)
            if(non_integer(c4))&(non_integer(c5))&(gcd(c4,c5)==c5):
                break
        cmp_2 = int(c4/c5)
        if non_integer(cmp_2):
            d2 = cmp_2
            d3 = d2*(c3**2)
            break
    #2번 ㄲㅌ

    #3번 시작
    while(True):
        c6 = random.randint(3,9)
        c7 = random.randint(2,5)
        c8 = random.randint(3,6)
        if(c6!=c8)&non_integer(c7)&(gcd(c6,c8)==1)&(c6>c8):
            d4 = c6**2
            d5 = c8**2
            break
    #3번 끝

    #4번 시작
    while(True):
        c9 = random.randint(10,60)
        c10 = random.randint(3,8)
        if(non_integer(c9))&non_integer(c10)&(gcd(c9,c10)==c10):
            cmp_4 = int(c9/c10)
            if(non_integer(cmp_4)):
                d6 = cmp_4
                break
    #4번 끝

    #5번 시작
    while(True):
        c11=random.randint(3,6)
        c13=random.randint(2,3)
        c12 = random.randint(10,50)
        c14=random.randint(3,6)
        if(gcd(c11,c13)==c13)&(gcd(c12,c14)==c14)&(non_integer(c12))&(non_integer(c14))&(c11!=c13):
            d7 = int(c11/c13)
            cmp_5 = int(c12/c14)
            if(non_integer(cmp_5)):
                d8 = cmp_5
                d9 = d7*d8*d8
                break
    # 5번 끝
    num1 = d4/d5
    list = [d1,d3,num1,d6,d9]
    min = list[0]
    minindex = 0
    for i in range(1,len(list)):
        if min>= list[i]:
            min = list[i]
            minindex = i
        else:
            min=min
    left = '{'
    right='}'
    leftg='('
    rightg=')'
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8,c9=c9,c10=c10,c11=c11,c12=c12,c13=c13,c14=c14,left=left,right=right)
    answer = answer.format(a1 = answer_dict.get(minindex))
    comment = comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8,c9=c9,c10=c10,c11=c11,c12=c12,c13=c13,c14=c14,left=left,right=right,d1=d1,d2=d2,d3=d3,d4=d4,d5=d5,d6=d6,d7=d7,d8=d8,d9=d9,a1 = answer_dict.get(minindex))
    return stem, answer, comment

#255
def realnum311_Stem_180():
    stem = "다음을 만족시키는 유리수 $$수식$$a,``b$$/수식$$에 대하여 $$수식$$sqrt a DIVIDE sqrt b$$/수식$$의 값은?\n"\
           "$$표$$ $$수식$$sqrt{c1} over sqrt{c2} `=` sqrt a $$/수식$$, $$수식$$ sqrt{left}{c3}over{c4}{right} DIVIDE sqrt{left}{c5}over{c6}{right}`=`sqrt b $$/수식$$$$/표$$\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     ④ {ex4}     ⑤ {ex5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$ sqrt a `=` sqrt {c1} over sqrt{c2} `=` sqrt{left}{c1} over {c2}{right}`=`sqrt{d1}$$/수식$$\n"\
              "$$수식$$ sqrt b `=` sqrt{left}{c3}over{c4}{right} DIVIDE sqrt{left}{c5}over{c6}{right} `=` sqrt{c3} over sqrt{c4} DIVIDE sqrt{c5} over sqrt{c6} `=` sqrt{c3} over sqrt{c4} TIMES sqrt{c6} over sqrt{c5}$$/수식$$\n"\
              "$$수식$$ `=` sqrt{left}{c3} over {c4} TIMES {c6} over {c5}{right} `=` sqrt{d2}$$/수식$$\n"\
              "$$수식$$ THEREFORE ~ sqrt a DIVIDE sqrt b `=` sqrt{d1} DIVIDE sqrt{d2} `=` sqrt{d1} TIMES 1 over sqrt{d2} `=` sqrt{left}{d1} over {d2}{right} `=` sqrt{d3} `=` {d4}$$/수식$$\n\n"
    while(True):
        numlist=[12, 13, 14, 15, 18, 20, 21, 24, 26, 27, 28, 30, 32, 35, 40, 45, 48, 56,44,52,68,60,68,72,76,80,84,90,96,99,102]
        numlist2 = [2,3,5,7]
        while(True):
            c1 = random.choice(numlist)
            c2 = random.choice(numlist2)
            if (gcd(c1,c2)==c2):
                d1 = int(c1/c2)
                break
        while(True):
            c3 = random.choice(numlist)
            c4 = random.choice(numlist2)
            c5 = random.choice(numlist)
            c6 = random.choice(numlist2)
            ja = c3 * c6
            mo = c4 * c5
            if(gcd(ja,mo)==mo)&(ja!=mo):
                d2 = int(ja / mo)
                break
        if(gcd(d1,d2) == d2)&(d1!=d2):
            d3 = int(d1/d2)
            result = soinsoo(d3)
            length = len(result)
            primes = list(result)
            for i in range(0,length):
                if(result[primes[i]] == 0):
                    del result[primes[i]]
            length = len(result)
            primes = list(result)
            a=1
            for i in range(0,length):
                if result[primes[i]]%2==0:
                    a=1
                else:
                    a=0
                    break
            if ( a == 1):
                d4 = int(d3**0.5)
                break
    left = '{'
    right='}'
    ex1 = "$$수식$$sqrt{b1}  $$/수식$$".format(b1 = d3 - 2)
    ex2 = "$$수식$$ sqrt{b2} $$/수식$$".format(b2 = d3 - 1)
    ex3 = "$$수식$$ {b3} $$/수식$$".format(b3 = d4)
    ex4 = "$$수식$$ sqrt{b4} $$/수식$$".format(b4 = d3 + 1)
    ex5 = "$$수식$$ sqrt{b5} $$/수식$$".format(b5 = d3 + 2)
    
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5, left=left,right=right)
    answer = answer.format(a1 = answer_dict.get(2))
    comment = comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,d1=d1,d2=d2,d3=d3,d4=d4,left=left,right=right)
    return stem, answer, comment   

#256
def realnum311_Stem_181():
    stem = " $$수식$$ {c1} sqrt {c2} ` DIVIDE ` {left}sqrt {c3}{right} over {left}sqrt {c4}{right} ` DIVIDE` sqrt{e1} over {left}sqrt {c5}{right} ` = `n sqrt {c6} ``$$/수식$$"\
           "일 때, 자연수 $$수식$$n$$/수식$$의 값은?\n"
    answer = "(답) {a1}\n"
    comment="(해설)\n"\
             "$$수식$$ {c1} sqrt {c2} ` DIVIDE ` {left}sqrt {c3}{right} over {left}sqrt {c4}{right} ` DIVIDE` {e1} over {left}sqrt {c5}{right} ` = `"\
             "{c1} sqrt {c2} ` TIMES ` {left}sqrt {c4}{right} over {left}sqrt {c3}{right} ` TIMES` sqrt {c5}over sqrt {e1}$$/수식$$\n"\
             "$$수식$$= ` {c1} sqrt{left}{c2} TIMES {c4} over {c3} TIMES {c5}over{e1} {right}$$/수식$$\n"\
             "$$수식$$ = {d1} sqrt{c6}$$/수식$$\n"\
             "$$수식$$ THEREFORE ~ n ` = ` {d1}$$/수식$$\n\n"
    numlist=[12, 14, 15, 18, 20, 21, 24, 27, 28, 30, 32, 35, 40, 45, 48, 56]
    while(True):
        while(True):
            c1 = random.randint(2,4)
            c2 = random.randint(2,3)
            c3 = random.randint(5,10)
            c4 = random.randint(5,10)
            c5 = random.choice(numlist)
            e1 = random.randint(2,3)
            if(c3!=c4)&non_integer(c3)&non_integer(c4)&(gcd(c3,c4)==1):
                break
        num = c2*c4*c5
        mo = e1*c3
        if(gcd(num,mo)==mo):
            cmp = int(num/mo)
            if(out_route(cmp)!=0):
                break
    d1 = c1*out_route(cmp)
    d2 = int(cmp/(out_route(cmp)**2))
    c6=d2
    left='{'
    right='}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=d2,left=left,right=right,e1=e1)
    answer = answer.format(a1 = d1)
    comment = comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,left=left,right=right,d1=d1,c6=c6,e1=e1)
    return stem, answer, comment    

#258
def realnum311_Stem_182():
    stem = "$$수식$$ sqrt{c1}$$/수식$$를 $$수식$$a sqrt b $$/수식$$의 꼴로 나타낼 때, $$수식$$ a ` + ` b$$/수식$$의 값을 구하시오."\
           "(단, $$수식$$a sqrt b $$/수식$$는 자연수이고, $$수식$$ a &gt; b $$/수식$$이다.)\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$ sqrt{c1}` = ` sqrt {left}{d1} TIMES {d2}{right} `=` {d1} sqrt{d2}$$/수식$$이므로\n"\
              "$$수식$$ a ` = ` {d1}$$/수식$$ $$수식$$ b ` = ` {d2}$$/수식$$\n"\
              "$$수식$$ a ` + ` b ` = ` {ans}$$/수식$$\n"
    numlist=[12, 14, 15, 18, 20, 21, 24, 27, 28, 30, 32, 35, 40, 45, 48, 56,44,52,68,60,68,72,76,80,84,90,96,99,102]
    while(True):
        c1 = random.choice(numlist)
        if(out_route(c1)!=0):
            d1 = out_route(c1)
            d2 = int(c1/(d1**2))
            break
    ans = d1+d2
    left = '{'
    right='}'
    stem = stem.format(c1=c1)
    answer = answer.format(a1=ans)
    comment = comment.format(c1=c1,left=left,right=right,d1=d1,d2=d2,ans=ans)
    return stem, answer, comment

#259
def realnum311_Stem_183():
    numlist=[12, 14, 15, 18, 20, 21, 24, 27, 28, 30, 32, 35, 40, 45, 48, 56,44,52,68,60,68,72,75,76,80,84,90,96,99,102]
    stem = "$$수식$${left}sqrt {c1}{right} over {left}sqrt {c2}{right} `$$/수식$$을 $$수식$${left}sqrt b{right} over a`$$/수식$$의 꼴로 나타낼 때,"\
           "$$수식$$ a ` + ` b $$/수식$$의 값을 구하시오.(단, $$수식$$a,`b$$/수식$$은 자연수이고, $$수식$$ a &gt; 1$$/수식$$이다.)\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$${left}sqrt {c1}{right} over {left}sqrt {c2}{right} ` = ` sqrt {left}{c1} over {c2}{right}`=`sqrt{left}{d1}over{d2}{right}$$/수식$$"\
              "$$수식$$`=`sqrt{left}{d1}over{d3}^2{right} `=`sqrt{d1} over {d3}$$/수식$$\이므로\n $$수식$$ a `= ` {d3},`b`=`{d1}$$/수식$$\n"\
              "$$수식$$ THEREFORE a ` + ` b ` = ` {ans}$$/수식$$\n\n"
    left= '{'
    right='}'
    while(True):
        c1 = random.choice(numlist)
        c2 = random.choice(numlist)
        if(c2>c1):
            division = gcd(c1,c2)
            if(division!=c1)&(division!=1):
                d1 = int(c1/division)
                if(non_integer(d1)):
                    d2 = int(c2/division)
                    if(non_integer(d2)):
                        continue
                    else:
                        d3 = int(d2**0.5)
                        ans = d3+d1
                        break
                else:
                   continue
        
    
    stem = stem.format(left=left,c1=c1,c2=c2,right=right)
    answer = answer.format(a1=ans)
    comment=comment.format(left=left,c1=c1,right=right,c2=c2,d1=d1,d2=d2,d3=d3,ans=ans)
    return stem, answer, comment

#260
def realnum311_Stem_184():
    stem = "$$수식$$sqrt {left}{c1} over {c2}{right} `$$/수식$$을 근호 안의 수가 가장 작은 자연수가 되도록 $$수식$$ sqrt b over a $$/수식$$꼴로 나타내었을 때, 자연수 $$수식$$a,`b$$/수식$$에 대하여 $$수식$$a`+`b$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$sqrt {left}{c1} over {c2}{right} `=`sqrt{left}{d1}over{d2}{right}`=`sqrt{left}{d1}over {d3}^2{right} `=` sqrt{d1}over{d3}$$/수식$$\n"\
              "따라서 $$수식$$ a `=`{d3},`b`=`{d1}$$/수식$$이므로\n"\
              "$$수식$$a`+`b`=`{ans}$$/수식$$\n\n"
    numlist=[12, 14, 15, 18, 20, 21, 24, 27, 28, 30, 32, 35, 40, 45, 48, 56,44,52,68,60,68,72,75,76,80,84,90,96,99,102, 108, 112, 116, 124]
    left= '{'
    right='}'
    while(True):
        c1 = random.choice(numlist)
        c2 = random.choice(numlist)
        if(c2>c1):
            division = gcd(c1,c2)
            if(division!=c1)&(division!=1):
                d1 = int(c1/division)
                if(non_integer(d1)):
                    d2 = int(c2/division)
                    if(non_integer(d2)):
                        continue
                    else:
                        d3 = int(d2**0.5)
                        ans = d3+d1
                        break
                else:
                   continue
        
    ex1 = ans-4
    ex2=ans-3
    ex3=ans-2
    ex4=ans-1
    ex5=ans
    stem = stem.format(left=left,c1=c1,c2=c2,right=right,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1=answer_dict.get(4))
    comment=comment.format(left=left,c1=c1,right=right,c2=c2,d1=d1,d2=d2,d3=d3,ans=ans)
    return stem, answer, comment

#261
def realnum311_Stem_185():
    stem="$$수식$$sqrt{c1} ` = ` k sqrt 10$$/수식$$일 때, 유리수 $$수식$$ k $$/수식$$의 값은?\n"\
          "① $$수식$${d1}$$/수식$$     ② $$수식$${d3}over{d4}$$/수식$$     ③ $$수식$${d5}$$/수식$$     ④ $$수식$${d6}$$/수식$$     ⑤ $$수식$${d7}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$sqrt{c1} ` = ` sqrt{left}{e1}over {f1}{right} ` = ` sqrt {left}{e2}^2 TIMES 10 over {f2}^ 2{right} ` = ` {left}{e2}sqrt10{right} over {f2}$$/수식$$\n"\
              "$$수식$$ k ` = `  {d3} over {d4}$$/수식$$\n\n"
    
    while(True):
        list1=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.016, 0.025, 0.036, 0.049, 0.064]

        c1 = random.choice(list1)
        if(c1!=0)&(c1!=1):
            if(int(c1*100)%10==0):  # 한자리 소수점
                f1 = 100
                f2 = 10
                e1 = int(c1*10)*10
                if(non_integer(int(c1*10))):

                    continue

                else:
                    e2 = int(int(c1*10)**0.5)

                    if((e2/f2)<=0.75)&((e2/f2)>0.01):
                        break

            else:
                f1 = 10000
                f2 = 100
                e1 = int(c1*10000)
                if(non_integer(int(c1*1000))):
                    continue
                else:
                    e2 = int(int(c1*1000)**0.5)

                    if((e2/f2)<=0.75)&((e2/f2)>0.01):
                        break

            
    
    ex1 = "1 over 10"
    ex2 = "1 over 5"
    ex3 = "1 over 4"
    ex4 = "3 over 10"
    ex5 = "2 over 5"
    ex6 = "1 over 2"
    ex7 = "3 over 5"
    ex8 = "3 over 4"
    ex9 = "7 over 10"
    ex10 = "4 over 5"
    ex11 = "9 over 10"
    ex12 = "1 over 100"
    ex13 = "1 over 20"
    ex14 = "3 over 20"
    ex15 = "7 over 20"
    realex1 = 1 / 10
    realex2 = 1 / 5
    realex3 = 1 / 4
    realex4 = 3 / 10
    realex5 = 2 / 5
    realex6 = 0.5
    realex7 = 0.6
    realex8 = 0.75
    realex9 = 0.7
    realex10 = 0.8
    realex11 = 0.9
    realex12 = 0.01
    realex13 = 0.05
    realex14 = 0.15
    realex15 = 0.35
    while(True):
        while(True):
            list2 = ["1 over 10", "1 over 5","1 over 4","3 over 10","2 over 5","1 over 2","3 over 5","3 over 4","7 over 10","4 over 5","9 over 10","1 over 100","1 over 20","3 over 20","7 over 20"]
            list3=[]
            list4 = []
            list5= [0.1, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.75, 0.7, 0.8, 0.9, 0.01, 0.05, 0.15, 0.35]
            for i in range(0,4):
                a = random.choice(list2)
                list3.append(a)
                list4.append(list2.index(a))
            decide = 1
            for i in range(0,3):
                for j in range(0,4):
                    if list4[i] == list4[j]:
                        if( i !=j ):
                            decide = 0
                            break
                if (decide == 0):
                    break
            if(decide==1):
                break
        for i in range(0,3):
            for j in range((i+1),4):
                if(list5[list4[i]]>list5[list4[j]]):
                    list3[i],list3[j] = list3[j],list3[i]
                    list4[i],list4[j] = list4[j],list4[i]
        division = gcd(f2,e2)
        if (division == 1):
            d3 = e2
            d4 = f2
            cmp2 = d3/d4
            if(cmp2 < list5[list4[1]])&(cmp2>list5[list4[0]]):
                break
        else:
            d3 = int(e2/division)
            d4 = int(f2/division)
            cmp2 = d3 / d4
            if(cmp2 < list5[list4[1]])&(cmp2>list5[list4[0]]):
                break
    left = '{'
    right='}'
    stem = stem.format(c1=c1,d1=list3[0],d3=d3,d4=d4,d5=list3[1],d6=list3[2],d7=list3[3])
    answer = answer.format(a1= answer_dict.get(1))
    comment = comment.format(c1=c1,left=left,right=right,e1=e1,e2=e2,d3=d3,d4=d4,f1=f1,f2=f2)
    return stem, answer, comment

#262
def realnum311_Stem_186():
    stem= "1 보다 큰 네 자연수 $$수식$$a,``b,``c,``d$$/수식$$에 대하여"\
          "$$수식$$ {left}{c1} sqrt{c2}{right} over sqrt{c3} ` = ` a sqrt b$$/수식$$, $$수식$$ {c4} over sqrt{c5} ` = ` c sqrt d$$/수식$$일 때,"\
          "$$수식$$a`+`b`+`c`+`d$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$ a>1$$/수식$$,  $$수식$$ b>1$$/수식$$ 이므로\n"\
              "$$수식$${left}{c1} sqrt{c2}{right} over sqrt{c3} ` = ` sqrt{left}{c1}^2 TIMES {c2}{right} over sqrt{c3} ` = ` sqrt{left}{left} {c1}^2 TIMES {c2}{right}over{c3}{right}$$/수식$$"\
              "$$수식$$ ` = sqrt{d1} ` = ` {d2} sqrt{d3} $$/수식$$\n"\
              "$$수식$$ THEREFORE ~ a `= ` {d2}, b `=`{d3}$$/수식$$\n"\
              "또, $$수식$$ c > 1 ,`` d>1$$/수식$$ 이므로\n"\
              "$$수식$$ {c4} over sqrt{c5} `=` sqrt {c4}^2 over sqrt{c5} ` = ` sqrt{left} {d4} over {c5} {right} `= ` sqrt{d5} `= `{d6} sqrt{d7}$$/수식$$\n"\
              "$$수식$$ THEREFORE c `=` {d6}, ``d`=`{d7} $$/수식$$\n"\
              "$$수식$$ THEREFORE a ` + ` b ` + ` c ` + ` d ` = ` {d2} ` + `{d3} ` + `{d6} ` + `{d7} `=`{ans}$$/수식$$\n\n"
    
    while(True):
        c1 = random.randint(2,20)
        c2 = random.randint(2,10) 
        c3 = random.randint(5,30) #분모임
        if(non_integer(c3))&(c2!=c3):
            ja_1 = c1*c1*c2
            if(gcd(ja_1,c3)==c3):
                cmp_1 =  int(ja_1 / c3)
                if(out_route(cmp_1)!=0):
                    d1 = cmp_1
                    d2 = out_route(cmp_1)
                    d3 = int(cmp_1/(d2**2))
                    break
    while(True):
        c4 = random.randint(2,14)
        c5 = random.randint(2,12)
        if(non_integer(c5)):
            d4 = c4*c4
            if(gcd(d4,c5)==c5):
                d5 = int(d4/c5)
                if(out_route(d5)!=0):
                    d6 = out_route(d5)
                    d7 = int(d5/(d6*d6))
                    break
    ans = d2+d3+d6+d7
    left='{'
    right='}'
    stem = stem.format(left=left,right=right,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1 = ans)
    comment = comment.format(left=left,right=right,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,d1=d1,d2=d2,d3=d3,d4=d4,d5=d5,d6=d6,d7=d7,ans=ans)
    return stem, answer, comment

#263
def realnum311_Stem_187():
    stem = "$$수식$${left}{c1} sqrt {c2}{right} over {left}sqrt{c3}{right} `=` sqrt a$$/수식$$,  $$수식$$ {c4} over {left}{c5} sqrt {c6}{right} `=` sqrt b$$/수식$$"\
           "일 때, 유리수 $$수식$$a,``b$$/수식$$에 대하여 $$수식$$ab$$/수식$$의 값은?\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     ④ {ex4}     ⑤ {ex5}\n"
    answer = "(답) {a1}\n"
    comment = "$$수식$${left}{c1} sqrt {c2}{right} over {left}sqrt{c3}{right} `=` sqrt{left}{c1}^2 TIMES {c2}{right} over sqrt{c3} `=` sqrt{d1} over sqrt{c3} `=` sqrt{left}{d1}over{c3} {right} `=` sqrt{left}{d2}over{d3}{right}$$/수식$$이므로\n"\
              "$$수식$$ a `=` {d2} over {d3}$$/수식$$ \n"\
              "$$수식$$  {c4} over {left}{c5} sqrt {c6}{right} `=` sqrt{c4}^2 over sqrt{left}c5^2 TIMES {c6}{right} `=` sqrt{d4} over sqrt{d5} `=` sqrt{left}{d4} over {d5}{right}$$/수식$$이므로\n"\
              "$$수식$$ b `=` {d4} over {d5}$$/수식$$ \n"\
              "$$수식$$ THEREFORE ~ ab `=` {d2} over {d3} TIMES {d4} over {d5} `=`$$/수식$${ans}\n\n"
    while(True):
        while(True):
            c1 = random.randint(2,3)
            c2 = random.randint(2,5)
            c3 = random.randint(10,20)
            if(non_integer(c2))&(non_integer(c3)):
                d1 = c1*c1*c2
                if(gcd(d1,c3)!=c3)&(gcd(d1,c3)!=1):
                    break
        div1 = gcd(d1,c3)
        d2 = int(d1/div1)
        d3 = int(c3/div1)
        while(True):
            c4 = random.randint(3,6)
            c5 = random.randint(2,3)
            c6 = random.randint(2,5)
            if ( c4!= c5)&(gcd(c4,c5)==1):
                d4 = c4*c4
                d5 = c5*c5*c6
                if(gcd(d4,d5)==1):
                    break
        ja = d2*d4
        mo = d3*d5
        if(gcd(ja,mo)!=mo)&(gcd(ja,mo)!=1)&(ja>mo):
            div2 = gcd(ja,mo)
            break
    cmp1 = int(ja/div2)
    cmp2 = int(mo / div2)
    ex4 = "$$수식$$ {b1} over {b2} $$/수식$$".format(b1=cmp1, b2 = cmp2)
    num1 = int(cmp1/cmp2)
    ex3 = "$$수식$$ {e1}$$/수식$$".format(e1 = num1)
    ex5 = "$$수식$$ {f1} $$/수식$$".format(f1 = num1 + 1)
    ex2 = "$$수식$$ 1 over 2 $$/수식$$"
    ex1 = "$$수식$$ {g1} over {g2}$$/수식$$".format(g1 = cmp2, g2 = cmp1)
    left = '{'
    right='}'

    stem = stem.format(left=left,right=right,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1=answer_dict.get(3))
    comment = comment.format(left=left, right=right, c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,d1=d1,d2=d2,d3=d3,d4=d4,d5=d5,ans=ex4)
    return stem, answer, comment

#264
def realnum311_Stem_188():
    stem = "$$수식$$sqrt {left}{c1} over {c2}{right} `=`a sqrt {c3} `$$/수식$$, $$수식$$ sqrt{c4} ` = ` b sqrt {c5} $$/수식$$ 일 때, 유리수 $$수식$$a, ` b $$/수식$$에 대하여 $$수식$$a over b $$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "$$수식$$sqrt {left}{c1} over {c2}{right} `=`a sqrt {c3} `=` sqrt{left}  {left} {d1}^2 TIMES {d2}{right} over {d3}^2 {right} `=` {d1}sqrt{d2} over {d3}$$/수식$$ 이므로\n"\
              "$$수식$$ a ` = ` {d1} over {d3}$$/수식$$\n"\
              "$$수식$$ sqrt{c4} ` = ` sqrt{left}{d4} over 10000{right} `= ` sqrt{left}{left}{d5}^2 TIMES {d6}{right} over 100^2{right} `=` {left} {d5} sqrt{d6}{right} over 100$$/수식$${extra}이므로\n"\
              "{b1}\n"\
              "$$수식$$ THERERFORE ~ a over b ` =` a TIMES {left}1 over b{right} `=` {d1}over {d3} TIMES {b2} `=` {ans}$$/수식$$\n\n"
    left='{'
    right='}'
    num1 = [0.0012, 0.0014, 0.0018, 0.0024, 0.0028, 0.0032, 0.0034, 0.0035, 0.0045, 0.0048, 0.0056, 0.0068, 0.0072, 0.0085, 0.0096, 0.0112, 0.0116, 0.0124, 0.0128, 0.0132, 0.0136, 0.0135, 0.0144, 0.0145,\
            0.0162, 0.0165, 0.0164, 0.0168, 0.0172, 0.0175, 0.0174, 0.0182, 0.0183, 0.0185, 0.0186, 0.0188]
    while(True):
        while(True):
            c1 = random.randint(10,150)
            c2 = random.randint(2,70)
            if (non_integer(c1)):
                if(non_integer(c2)):
                    continue
                else:
                    if(out_route(c1)!=0):
                        d1 = out_route(c1)
                        d2 = int(c1/(d1*d1))
                        d3 = int(c2**0.5)
                        c3 = d2
                        if(d3!=1):
                            break
        if ( gcd(d1,d3)==1):
            dans = "{d1}over{d3}".format(d1=d1,d3=d3)
        elif d1 == d3:
            dans = "1"
        else :
            d1 = int(d1/gcd(d1,d3))
            d3 = int(d3/gcd(d1,d3))
            if(d3!=1):
                dans = "{d1}over{d3}".format(d1=d1,d3=d3)
            else:
                dans = "{d1}".format(d1=d1)
                
        while(True):
            c4 = random.choice(num1)
            d4 = int(c4 * 10000)
            if(non_integer(d4)):
                if(out_route(d4)!=0):
                    d5= out_route(d4)
                    d6 = int(d4/(d5*d5))
                    c5 = d6
                    break
        if(gcd(d5,100)==1):
            extra = '  '
            b1 = "$$수식$$ {f1} over {f2} $$/수식$$".format(f1 = d5, f2=100)
            if(d5==1):
                b2 = 100
                cmp = d1 * b2
                if(gcd(cmp, d3)==d3):
                    ans = int(cmp/d3)
                    break
            else:
                b2 = "$$수식$$ {g1} over {g2} $$/수식$$".format(g1 = 100, g2 = d5)
                ja = d1*100
                mo = d3 * d5
                if(gcd(ja,mo)==mo):
                    ans = int(ja/mo)
                    break
        else:
            extra = "$$수식$$ {f1} over {f2} $$/수식$$".format(f1 = int(d5/gcd(d5,100)), f2 = int(100/gcd(d5,100)))
            b1 = "$$수식$$ b ` = ` $$/수식$$"+str(extra)
            if (int(d5/gcd(d5,100))==1):
                b2 = int(100/gcd(d5,100))
                cmp = d1 * b2
                if(gcd(cmp,d3)==d3):
                    ans = int(cmp/d3)
                    break
            else:
                b2 = "$$수식$$ {g1} over {g2} $$/수식$$".format(g1 = int(100/gcd(d5,100)), g2 = int(d5/gcd(d5,100)))
                ja = d1 * int(100/gcd(d5,100))
                mo = d3 * int(d5/gcd(d5,100))
                if(gcd(ja,mo)==mo):
                    ans = int(ja/mo)
                    break
    ex1 = ans
    ex2 = ans+2
    ex3=ans+4
    ex4=ans+6
    ex5=ans+8
    stem = stem.format(left=left,right=right,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer= answer.format(a1 = answer_dict.get(0))
    comment = comment.format( left=left, right=right, c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,d1=d1,d2=d2,d3=d3,d4=d4,d5=d5,d6=d6,extra=extra, ans=ans,b1=b1,b2=b2,dans=dans)
    return stem, answer, comment

#265
def realnum311_Stem_189():
    stem = "$$수식$$ a &gt; 0,``b &gt; 0$$/수식$$이고 $$수식$$ sqrt ab `=` {c1}$$/수식$$일 때, $$수식$$ {c2} over b sqrt {left}b over a{right}`-` {c3} over a sqrt {left}a over b{right}$$/수식$$의 값은?\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     ④ {ex4}     ⑤ {ex5}\n"
    answer = "(답) {a1}\n"
    comment = "$$수식$$ {c2} over b sqrt {left}b over a{right}`-` {c3} over a sqrt {left}a over b{right} `=` sqrt{left}{d1}over b^2 TIMES b over a{right} `-` sqrt{left}{d2}over a ^ 2 TIMES a over b{right}$$/수식$$\n"\
             "$$수식$$ `=` sqrt{left}{d1} over ab{right} `-` sqrt{left}{d2} over ab{right} `=` {c2} over sqrt ab `-` {c3} over sqrt ab$$/수식$$\n"\
             "$$수식$$ `=` {c2} over {c1} `-` {c3} over {c1} `=`$$/수식$${ans} \n\n"
    numlist = [2,3,4,5,6,8,10]
    while(True):
        while(True):
            c1 = random.choice(numlist)
            while(True):
                c2 = random.randint(1,4)
                c3 = random.randint(2,8)
                if (c2!=c3) & (c2 < c3):
                    break
            ja = c2 - c3
            if(ja<0):
                break
        d1 = c2*c2
        d2 = c3*c3
            
        if(gcd(-ja, c1)==1):
            if(c1!=2):
                ans = "$$수식$$ - {b1} over {b2}$$/수식$$".format(b1 = - ja, b2 = c1)
                cmp1 = -ja
                cmp2 = c1
                break
        elif(gcd(-ja,c1)==c1):
            num1 = int(-ja/c1)
            ans = "$$수식$$ - {b1} $$/수식$$".format(b1 = num1)
            cmp1 = -ja
            cmp2 = c1
            break
        else:
            div = gcd(-ja,c1)
            cmp1 = int(-ja/div)
            cmp2 = int(c1 / div)
            if(cmp2!=2):
                ans = "$$수식$$ - {b1} over {b2} $$/수식$$".format(b1 = cmp1, b2 = cmp2)
                break
    ex2 = ans
    if(gcd(cmp1*2,cmp2)==cmp2):
        ex1 = "$$수식$$ - {e1} $$/수식$$".format(e1 = int(cmp1*2/cmp2))
    elif(gcd(cmp1*2,cmp2)==1):
        ex1 = "$$수식$$ - {e1} over {e2} $$/수식$$".format(e1 = cmp1*2, e2 = cmp2)
    else:
        div1 = gcd(cmp1*2,cmp2)
        ex1 = "$$수식$$ - {e1} over {e2} $$/수식$$".format(e1 = int(cmp1*2/div1), e2 = int(cmp2/div1))
    if(gcd(cmp1,cmp2)==cmp2):
        ex3 = "$$수식$$  {e1} $$/수식$$".format(e1 = int(cmp1/cmp2))
    elif(gcd(cmp1,cmp2)==1):
        ex3 = "$$수식$$ {b1} over {b2} $$/수식$$".format(b1 = cmp1, b2 = cmp2)
    else:
        div2 = gcd(cmp1,cmp2)
        ex3 = "$$수식$$ {e1} over {e2} $$/수식$$".format(e1 = int(cmp1/div2), e2 = int(cmp2/div2))
    if(gcd(cmp1*2,cmp2)==cmp2):
        ex4 = "$$수식$$  {e1} $$/수식$$".format(e1 = int(cmp1*2/cmp2))
        ex5 = "$$수식$$ {f1} $$/수식$$".format(f1 = int(cmp1*2/cmp2) + 1)
    elif gcd(cmp1*2,cmp2)==1:
        ex4 = "$$수식$$  {e1} over {e2} $$/수식$$".format(e1 = cmp1*2, e2 = cmp2)
        ex5 = "$$수식$$ {f1} $$/수식$$".format(f1 = int(cmp1/cmp2) + 1)
    else:
        div4 = gcd(cmp1*2,cmp2)
        ex4 = "$$수식$$ {e1} over {e2} $$/수식$$".format(e1 = int(cmp1*2/div4), e2 = int(cmp2/div4))
        ex5 = "$$수식$$ {f1} $$/수식$$".format(f1 = int(cmp1/cmp2) + 1)

    left = '{'
    right = '}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,left=left,right=right, ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1 = answer_dict.get(1))
    comment = comment.format(c1=c1,c2=c2,c3=c3,left=left,right=right,d1=d1,d2=d2, ans=ans)
    return stem, answer, comment

#266
def realnum311_Stem_190():
    stem = "$$수식$$ sqrt{c1} $$/수식$$는 $$수식$$sqrt{c2}$$/수식$$의 $$수식$$ a $$/수식$$배이고, $$수식$$sqrt{c3}$$/수식$$은 $$수식$$ sqrt{c4}$$/수식$$의 $$수식$$ b $$/수식$$배일 때,"\
           "$$수식$$ 2ab $$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$ sqrt{c1}$$/수식$$\n"\
              "$$수식$$ =` sqrt {left}{d1} over 1000{right} `=` sqrt {left}{d2} over 10000{right} `=` {left}{d3} sqrt {d4}{right} over 100 `=` {left}sqrt {d4}{right} over {d5} `$$/수식$$\n"\
              "이므로 $$수식$$ a ` = ` 1 over {d5} $$/수식$$\n"\
              "$$수식$$ sqrt{c3} ` = ` sqrt{left} {e1} ^ 2 TIMES {d6} {right} ` = ` {e1} sqrt{d7}$$/수식$$이므로 $$수식$$ b ` = ` {e1} $$/수식$$\n"\
              "따라서 $$수식$$ 2ab ` = ` 2 TIMES {left}1 over {d5}{right} TIMES {e1} ` = ` {ans}$$/수식$$\n\n"
    while(True):
        prime = [2,3,5,7]
        while(True):
            listnum=[0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009, 0.01, 0.012, 0.014, 0.016,0.018,0.02,0.025,0.028,0.03,0.032]
            c1 = random.choice(listnum)
            d1 = int(c1*1000)
            d2 = d1*10
            if(out_route(d2)!=0):
                d3 = out_route(d2)
                d4 = int(d2/(d3*d3))
                c2 = d4
                if(gcd(d3,100)==d3):
                    d5 = int(100/gcd(d3,100))
                    break
        while(True):
            c3 = random.randint(100,1500)
            c4 = random.choice(prime)
            if(gcd(c3,c4)==c4):
                cmp = int(c3/c4)
                if(non_integer(cmp)):
                    continue
                else:
                    e1 = int(cmp**0.5)
                    d6 = c4
                    d7 = c4
                    break
        ja = 2 * e1
        if(gcd(ja,d5)==d5):
            break
    ans = int(ja/d5)
    left='{'
    right='}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4)
    answer = answer.format(a1 = ans)
    comment = comment.format(c1=c1,c2=c2,c3=c3,c4=c4,d1=d1,d2=d2,d3=d3,d4=d4,d5=d5,d6=d6,e1=e1,d7=d7,ans=ans,left=left,right=right)
    return stem, answer, comment
        

#268
def realnum311_Stem_191():
    stem = "$$수식$$sqrt 3.14 ` = ` 1.772$$/수식$$, $$수식$$ sqrt 31.4 ` = ` 5.604$$/수식$$일 때, $$수식$$ sqrt{c1}$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "$$수식$$ sqrt{c1} ` = ` sqrt {left} {c2} TIMES {c3} {right} ` = ` {c4} sqrt{c5} $$/수식$$\n"\
              "$$수식$$ ` = ` {c4} TIMES {c6} ` = ` {ans}$$/수식$$\n\n"
    listnum = [314, 3140, 31400, 0.314, 0.0314]
    c1 = random.choice(listnum)
    if ( c1 == 314):
        c2 = 3.14
        c3 = 100
        c4 = 10
        c5 = c2
        c6 = 1.772
        ans = 17.72
        ex1 = 5.604
        ex3 = 56.04
        ex4 = 177.2
        ex5 = 560.4
    elif ( c1 == 3140):
        c2 = 31.4
        c3 = 100
        c4 = 10
        c5 = 31.4
        c6 = 5.604
        ans = 56.0
        ex1 = 17.72
        ex3 = 177.2
        ex4 = 560.4
        ex5 = 1772
    elif ( c1 == 31400 ):
        c2 = 3.14
        c3 = 10000
        c4 = 100
        c5 = 3.14
        c6 = 1.772
        ans = 177.2
        ex1 = 56.04
        ex3 = 560.4
        ex4 = 1772
        ex5 = 5604
    elif (c1 == 0.314):
        c2 = 31.4
        c3 = "10 ^ -2"
        c4 = "1 over 10 "
        c5 = 31.4
        c6 = 5.604
        ans = 0.5604
        ex1 = 0.1772
        ex3 = 1.772
        ex4 = 5.604
        ex5 = 17.72
    else:
        c2 = 3.14
        c3 = "10 ^ -2"
        c4 = " 1 over 10"
        c5 = 3.14
        c6 = 1.772
        ans = 0.1772
        ex1 = 0.05604
        ex3 = 0.5604
        ex4 = 1.772
        ex5 = 5.604
    left = '{'
    right='}'
    ex2 = ans
    stem = stem.format(c1=c1,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1= answer_dict.get(1))
    comment = comment.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,ans=ans,left=left,right=right)
    return stem, answer, comment

#269
def realnum311_Stem_192():
    stem = "다음 중 $$수식$$ sqrt {c1} `=` {c2}$$/수식$$ 임을 이용하여 그 값을 구할 수 없는 것을 모두 고르면? (정답 2개) \n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer= "(답) {a1}, {a2}\n"
    comment = "(해설)\n"\
              "② $$수식$$ {ex2} = sqrt {left}{c1} over 10000{right} = {left}sqrt {c1}{right} over 100 = {c2} over 100` =`{ans2}$$/수식$$\n"\
              "③ $$수식$$ {ex3} = sqrt {left}{c1} TIMES100{right} = 10 sqrt {c1} =10 TIMES {c2} ={ans3}$$/수식$$\n"\
              "④ $$수식$$ {ex4} = sqrt {left}{c1} over 100{right} = {left}sqrt {c1}{right} over 10 = {c2} over 10 ={ans4}$$/수식$$\n\n"
    list1 =[]
    left= '{'
    right='}'
    dict = {5 : 2.236, 3.1 : 1.761, 3.2 : 1.789, 3.3 : 1.817, 5.63 : 2.373, 4.2 :2.049, 5.26 : 2.293}
    list1 = list(dict)
    c1 = random.choice(list1)
    c2 = dict[c1]
    if(c1*10 == int(c1*10)):
       ex1 = "sqrt {left}{b1}{right}".format(b1=int(c1 *10),left=left, right=right)
    else:
       b1 = c1*10
       ex1 = "sqrt {left}{b1}{right}".format(b1=round(b1,1),left=left, right=right)
    b2 = c1/10000
    ex2 = "sqrt{left}{b2} {right}".format(b2=b2,left=left, right=right)
    ex3 = "sqrt{left}{b3} {right}".format(b3=int(c1 *100),left=left, right=right)
    b4 = c1/100
    if ( c1 == 5.26 )|(c1==5.63):
        ex4 = "sqrt{left}{b4} {right}".format(b4=round(b4,4),left=left, right=right)
    else:
        ex4 = "sqrt{left}{b4} {right}".format(b4=b4,left=left, right=right)
    ex5 = "sqrt{left}{b5} {right}".format(b5=int(c1 * 1000),left=left, right=right)
    ans2 = (c2)/100
    ans2 = round(ans2,5)
    ans3 =(c2)*10
    ans3 = round(ans3,2)
    ans4 = (c2)/10
    ans4 = round(ans4,4)
    stem = stem.format(c1=c1,c2=c2,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1 = answer_dict.get(0), a2 = answer_dict.get(4))
    comment = comment.format(ex2=ex2,left=left,c1=c1,right=right, c2=c2,ans2=ans2, ex3=ex3, ans3=ans3, ex4=ex4, ans4=ans4)
    return stem, answer, comment

#270
def realnum311_Stem_193():
    stem = "$$수식$$ sqrt{c1} `=` {c2}$$/수식$$, $$수식$$ sqrt{c3} `=` {c4} $$/수식$$일 때, $$수식$$sqrt{c5}$$/수식$$과 가장 가까운 정수는?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$ sqrt{c5} `=` sqrt{left}{d1} TIMES {d2}{right} `=` {d3} sqrt{d1}$$/수식$$ \n"\
              "$$수식$$ `=` {d3} TIMES {d4} `=` {d5} $$/수식$$\n"\
              "따라서 $$수식$$ sqrt{c5} $$/수식$$과 가장 가까운 정수는 {ans}이다.\n\n"
    dict1 = {5 : 2.236, 3.1 : 1.761, 3.2 : 1.789, 4.2 :2.049, 7.3 : 2.702, 7.5 : 2.738, 3.7 : 1.923}
    dict2 = {50 : 7.071, 31 : 5.567, 32 : 5.656, 42 : 6.481, 73 : 8.544, 75 : 8.661, 37 : 6.082 }
    listnum = [100, 10000]
    list1 = list(dict1)
    list2 = list(dict2)
    list3 = []
    c1 = random.choice(list1)
    list3.append(c1)
    c2 = dict1[c1]
    
    for i in range(0,len(dict2)):
        if (int(c1*10) == list2[i]) :
            c3 = list2[i]
            list3.append(c3)
            c4 = dict2[c3]
            break
    multi = random.choice(listnum)
    num1 = random.choice(list3)
    c5 = int(num1 * multi)
    d1 = num1
    d2 = multi
    d3 = int(d2**0.5)
    if d1 in dict1:
        d4 = dict1[d1]
        d5 = dict1[d1] * d3
    if d1 in dict2:
        d4 = dict2[d1]
        d5 = dict2[d1] * d3
    if (d2 == 100):
        d5 = round(d5,2)
    else:
        d5 = round(d5,1)
    ans = round(d5)

    ex1 = random.randint(1, ans - 1)
    ex2 = ans
    while(True):
        ex3 = random.randint(ans+1, ans+100)
        ex4 = random.randint(ans+1, ans+100)
        ex5 = random.randint(ans+1, ans+100)
        if(ex3 < ex4) & (ex4 < ex5):
            break
    left = '{'
    right = '}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1 = answer_dict.get(1))
    comment = comment.format(c5=c5,left=left,right=right,d1=d1,d2=d2,d3=d3,d4=d4,d5=d5,ans=ans)
    return stem, answer, comment


#272
def realnum311_Stem_194():
    stem="$$수식$$sqrt{c1} ` =` {c2} $$/수식$$일 때, $$수식$$ sqrt a ` = ` {c3}$$/수식$$을 만족시키는 유리수 $$수식$$ a $$/수식$$의 값은?\n"\
          "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment ="(해설)\n"\
              "$$수식$$ {c3} ` =` {e1} TIMES {c2}$$/수식$$\n"\
              "→ $$수식$$ {e1} sqrt {c1} `=` sqrt {left} {c1} TIMES {e2}{right} `=` sqrt {ans}$$/수식$$\n\n"
    dict = {5 : 2.236, 3.1 : 1.761, 3.2 : 1.789, 3.3 : 1.817, 4.2 :2.049, 5.26 : 2.293,4.4 : 2.097, 4.6 : 2.144,4.8 : 2.190, 5.2 : 2.280, 5.4 : 2.323,\
            4.5 : 2.121, 4.7 : 2.167, 4.9 : 2.213, 5.1 : 2.258, 6.1 : 2.469, 6.2 : 2.489, 6.3 : 2.509, 6.4 : 2.529, 6.5 : 2.549, 6.6 : 2.569, 6.7 : 2.588 , \
            6.8 : 2.607, 6.9:2.626, 7.1 : 2.664, 7.2: 2.683, 7.3 : 2.701, 7.4 : 2.720, 7.5 : 2.738, 7.6 : 2.756, 7.7 : 2.774, 7.8 : 2.792, 7.9 : 2.811, 8.1 : 2.846}
    listnum = [10, 100, 0.1]
    list1 = list(dict)
    c1 = random.choice(list1)
    c2 = dict[c1]
    num1 = random.choice(listnum)
    if (num1 ==10):
        c3 = c2 * 10
        c3 = round(c3,2)
        e1 = 10
        e2 = 100
        ans = int(c1*100)
        ex1 = c1 / 100
        ex1 = round(ex1,3)
        ex2 = c1 / 10
        ex2 = round(ex2, 2)
        ex3 = int(c1 * 10)
        ex4 = ans
        ex5 = int(c1*1000)
        answer = answer.format(a1=answer_dict.get(3))
    elif (num1 == 100):
        c3 = c2 * 100
        c3 = round(c3,1)
        e1 = 100
        e2 = 1000
        ans = int(c1*10000)
        ex1 = c1 / 100
        ex1 = round(ex1,3)
        ex2 = c1 / 10
        ex2 = round(ex2, 2)
        ex3 = int(c1 * 10)
        ex4 = int(c1*100)
        ex5 = ans
        answer = answer.format(a1=answer_dict.get(4))
    else:
        c3 = c2/10
        c3 = round(c3,4)
        e1 = 0.1
        e2 = 0.01
        ans = c1 / 100
        ans = round(ans,3)
        ex1 = c1 / 10000
        ex1 = round(ex1,5)
        ex2 = c1 / 1000
        ex2 = round(ex2, 4)
        ex3 = c1 / 100
        ex3 = round(ex3,3)
        ex4 = c1 / 10
        ex4 - round(ex4,2)
        ex5 = int(c1*10)
        answer = answer.format(a1 = answer_dict.get(2))

    left='{'
    right='}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    comment = comment.format(c3=c3,c2=c2,c1=c1,left=left,right=right,ans=ans,e1=e1,e2=e2)
    return stem, answer ,comment

#273
def realnum311_Stem_195():
    dict1 = {5 : 2.236, 3:1.7320, 6:2.4494, 7:2.6457, 8:2.8284, 3.2 : 1.788, 6.2 : 2.489, 7.2: 2.683}
    dict2 = {50:7.0710, 30 : 5.4772, 60 : 7.7459, 80 : 8.9442, 32 : 5.656, 62 : 7.874, 72 : 8.485}
    stem = "$$수식$$ sqrt{c1} `=` {c2},`````sqrt{c3} `=` {c4}$$/수식$$일 때, $$수식$$ sqrt{c5}$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$$ sqrt{c5} ` = ` sqrt{left}{d1}over{d2}{right} ` = ` {left}{d3} sqrt{d4}{right}over{d5} $$/수식$$\n$$수식$$` = ` {left}{d3} TIMES {d6}{right} over {d5} `=` {ans}$$/수식$$\n\n"
    list1 = list(dict1)
    list2 = list(dict2)
    while(True):
        while(True):
            c1 = random.choice(list1)
            c2 = dict1[c1]
            c3 = random.choice(list2)
            if(c1*10 == c3):
                break
        c4 = dict2[c3]
        list3 = [0.002, 0.004, 0.006, 0.008, 0.01, 0.012, 0.014, 0.016, 0.018, 0.02, 0.024, 0.025, 0.028, 0.03, 0.032,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.034, 0.035, 0.036, 0.037, 0.038, \
                 0.045, 0.048, 0.052, 0.054, 0.056, 0.058, 0.068, 0.072, 0.075, 0.076, 0.078, 0.084, 0.086, 0.092, 0.093, 0.096, 0.099 ]
        c5 = random.choice(list3)
        if(int(c5*10) !=0): # 한자리 소수
            d2 = 100
            d1 = int(c5*100)
            
            if(out_route(d1)!=0):
                d3 = out_route(d1)
                d4 = int(d1/(d3**2))
                d5 = 10
                if(d4 == c1):
                    d6 = c2
                    ans = (d6 * d3) / d5
                    ans = round(ans,4)
                    break
                elif ( d4 == c3):
                    d6 = c4
                    ans = (d6* d3 )/d5
                    ans = round(ans,4)
                    break
                else:
                    continue

        else: # 나머지 소수
            d2 = 10000
            d1 = int(c5*10000)
            if(out_route(d1)!=0):
                d3 = out_route(d1)
                d4 = int(d1 / (d3*d3))
                d5 = 100
                if(d4 == c1):
                    d6 = c2
                    ans = (d6 * d3 )/d5
                    ans = round(ans,5)
                    break
                elif (d4 == c3):
                    d6 = c4
                    ans = (d6*d3)/d5
                    ans = round(ans,5)
                    break
                else:
                    continue
    ex1 = ans/2
    ex2= ans
    ex3 = c2/10
    ex3 = round(ex3,4)
    ex4 = c4 / 20
    ex5 = c4/10
    left = '{'
    right = '}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1 = answer_dict.get(1))
    comment = comment.format(c5=c5,d1=d1,d2=d2,d3=d3,d4=d4,d5=d5,d6=d6,left=left,right=right,ans=ans)
    return stem, answer, comment
            

#274
def realnum311_Stem_196():
    dict1 = {5 : 2.236, 3.1 : 1.761, 3.2 : 1.789, 4.2 :2.049, 7.3 : 2.702, 7.5 : 2.7386, 3.7 : 1.9235, 4.4 : 2.097, 4.6 : 2.144, 4.8 : 2.191, 5.2 : 2.280, 6.2 : 2.489, 6.6 : 2.569, 6.8 : 2.607, 7 : 2.645 }
    dict2 = {50 : 7.071, 31 : 5.5677, 32 : 5.6568, 42 : 6.4807, 73 : 8.544, 75 : 8.6602, 37 : 6.0827 , 44 : 6.633, 46 : 6.782, 48 : 6.928, 52 : 7.211, 62 : 7.874, 66 : 8.124, 68 : 8.246, 70 : 8.366}
    stem = "$$수식$$sqrt{c1} `=` {c2}$$/수식$$, $$수식$$sqrt{c3}`=`{c4}$$/수식$$일 때, 옳은 것을 보기에서 모두 고른 것은?\n"\
           "$$표$$ ㈀ $$수식$$ sqrt{d1} `=` {d2} $$/수식$$\n"\
           "㈁ $$수식$$ sqrt{d3}`=`{d4} $$/수식$$\n"\
           "㈂ $$수식$$ sqrt{d5} `=` {d6} $$/수식$$\n"\
           "㈃ $$수식$$ sqrt{d7} `=` {d8} $$/수식$$\n"\
           "① {ex1}     ② {ex2}     ③ {ex3}     ④ {ex4}     ⑤ {ex5}\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "㈀ $$수식$$ sqrt{d1} `=` sqrt{left}{c1} TIMES 10000{right} `=` 100sqrt{c1} $$/수식$$ \n"\
              "$$수식$$ `=` 100 TIMES {c2} `= `{e1} $$/수식$$\n"\
              "㈁ $$수식$$ sqrt{d3}`=` sqrt{left}{c3} TIMES 100 {right} `=` 10 sqrt{c3} $$/수식$$\n"\
              "$$수식$$ `=` 10 TIMES {c4} `=` {e2} $$/수식$$\n"\
              "㈂ $$수식$$ sqrt{d5} `=` sqrt{left} {c3} over 100 {right} `=` sqrt{c3} over 10 `=` {c4} over 10 = {e3}$$/수식$$\n"\
              "㈃ $$수식$$ sqrt{d7} `=` sqrt{left}{c1}over 100{right} `=` sqrt{c1} over 10 `=` {c2} over 10 `=` {e4} $$/수식$$\n"\
              "이상에서 옳은 것은 ㈀, ㈁, ㈂이다.\n\n"
    len1 = len(dict1)
    list1 = list(dict1)
    len2 = len(dict2)
    list2 = list(dict2)
    c1 = random.choice(list1)
    c2 = dict1[c1]
    c3 = random.choice(list2)
    c4 = dict2[c3]
    d1 = int(c1*10000)
    d2 = c2 * 100
    d2 = round(d2,1)
    d3 = int(c3*100)
    d4 = c4*10
    d4 = round(c4,2)
    d5 = c3/100
    d5 = round(d5,2)
    d6 = c4/10
    d6 = round(d6,5)
    d7 = c1/100
    d7 = round(d7,3)
    d8 = c2/10
    d8 = round(d8,5)
    e1=d2
    e2=d4
    e3=d6
    e4=d8
    d8 = d8/10
    d8 = round(d8,5)
    ex1 = "㈀, ㈁"
    ex2 = "㈀, ㈂"
    ex3 = "㈁, ㈂"
    ex4 = "㈀, ㈁, ㈂"
    ex5 = "㈁, ㈂, ㈃"
    left = '{'
    right = '}'
    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,d1=d1,d2=d2,d3=d3,d4=d4,d5=d5,d6=d6,d7=d7,d8=d8,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1 = answer_dict.get(3))
    comment = comment.format(d1=d1,left=left,right=right,c2=c2,e1=e1,d3=d3,c3=c3,c1=c1,c4=c4,e2=e2,d5=d5,d7=d7,e4=e4,e3=e3)
    return stem, answer, comment


#275
def realnum311_Stem_197():
    stem = "$$수식$$ sqrt{c1} ` = ` {c2}$$/수식$$일 때, $$수식$${c3}$$/수식$$의 값은?\n"\
           "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "$$수식$${d1} `=` {d2} TIMES {c2} `=` {d2} sqrt {c1}$$/수식$$이므로\n"\
              "$$수식$${c3} `=` {leftg} {d2}sqrt{c1} {rightg} ^2 `=` {d3} TIMES {c1} ` = ` {ans}$$/수식$$\n\n"
    dict = {5 : 2.236, 3.1 : 1.761, 3.2 : 1.789, 3.3 : 1.817, 5.63 : 2.373, 4.2 :2.049, 5.26 : 2.293, \
            4.5 : 2.121, 4.7 : 2.167, 4.9 : 2.213, 5.1 : 2.258, 6.1 : 2.469, 6.2 : 2.489, 6.3 : 2.509, 6.4 : 2.529, 6.5 : 2.549, 6.6 : 2.569, 6.7 : 2.588 , \
            6.8 : 2.607, 6.9:2.626, 7.1 : 2.664, 7.2: 2.683, 7.3 : 2.701, 7.4 : 2.720, 7.5 : 2.738, 7.6 : 2.756, 7.7 : 2.774, 7.8 : 2.792, 7.9 : 2.811, 8.1 : 2.846}
    list1 = list(dict)
    c1 = random.choice(list1)
    c2 = dict[c1]
    listnum = [10, 100, 1000]
    multi = random.choice(listnum)
    
    if ( multi == 10):
        d1 = c2 *multi
        d1 = round(d1,2)
    elif(multi == 100):
        d1 = c2 * multi
        d1 = round(d1,1)
    else:
        d1 = int(c2*multi)
    c3 = "{b1}^2 ".format(b1 = d1)
    d2 = multi
    d3 = d2**2
    ans = int(d3 * c1)
    left = '{'
    right='}'
    leftg='('
    rightg=')'
    ex1= ans
    if (int(ans/10)==ans/10):
        ex2 = int(ans/10)
    else:
        ex2= ans/10
    if ((ans/100) == int(ans/100)):
        ex3 = int(ans/100)
    else:
        ex3 = ans/100
    if((ans/1000)==int(ans/1000)):
       ex4 = int(ans/1000)
    else:
        ex4=ans/1000
    if(ans/10000 == int(ans/10000)):
        ex5=int(ans/10000)
    else:
       ex5 = ans/10000
    stem = stem.format(c1=c1,c2=c2,c3=c3,ex1=ex1,ex2=ex2,ex3=ex3,ex4=ex4,ex5=ex5)
    answer = answer.format(a1 = answer_dict.get(0))
    comment = comment.format(d1=d1,d2=d2,c2=c2,c3=c3,leftg=leftg,rightg=rightg, d3=d3,ans=ans,c1=c1)
    return stem, answer, comment

#276
def realnum311_Stem_198():
    stem = "$$수식$$ sqrt{c1} `=` a$$/수식$$, $$수식$$ sqrt{c2} `=` b$$/수식$$라 할 때, 다음 중 옳은 것을 모두 고르면?(정답 2개)\n"\
           "① $$수식$$ sqrt{d1} `=` {d2}b $$/수식$$"\
           "	② $$수식$$ sqrt{d3} `=` {d4}a $$/수식$$\n"\
           "③ $$수식$$ sqrt{d5} `=` {d6}a$$/수식$$"\
           "		④ $$수식$$ sqrt{d7} `=` {d8}a$$/수식$$\n"\
           "⑤ $$수식$$ sqrt{d9} `=` {d10}a$$/수식$$\n"
    answer = "(답) {a1}\n"
    comment = "(해설)\n"\
              "① $$수식$$ sqrt{d1} `=` sqrt{left}{c1} over {e1}{right}`=` sqrt{c1} over {e2}$$/수식$$\n $$수식$$`=` 1 over {e2} a `=` {e3}a $$/수식$$\n"\
              "② $$수식$$ sqrt{d3} `=` sqrt{left}{c2} over {e4}{right} `=` sqrt{c2} over {e5} $$/수식$$\n $$수식$$`=` 1 over {e5} b `=` {e6} b $$/수식$$\n"\
              "③ $$수식$$ sqrt{d5} `=` sqrt{left}{c1} TIMES {e7}{right} `=` {e8} sqrt{c1} `=` {e8} a$$/수식$$\n"\
              "④ $$수식$$ sqrt{d7} `=` sqrt{left}{c2} TIMES {e9}{right}`=`{e10} sqrt{c2} `=` {e10}b$$/수식$$\n"\
              "⑤ $$수식$$ sqrt{d9} `=` sqrt{left}{c1} TIMES {e11}{right}`=` {e12} sqrt{c1} `=` {e12} a$$/수식$$\n\n"
    dict1 = {5 : 2.236, 3.1 : 1.761, 3.2 : 1.789, 4.2 :2.049, 7.3 : 2.702, 7.5 : 2.7386, 3.7 : 1.9235, 4.4 : 2.097, 4.6 : 2.144, 4.8 : 2.191, 5.2 : 2.280, 6.2 : 2.489, 6.6 : 2.569, 6.8 : 2.607, 7 : 2.645 }
    dict2 = {50 : 7.071, 31 : 5.5677, 32 : 5.6568, 42 : 6.4807, 73 : 8.544, 75 : 8.6602, 37 : 6.0827 , 44 : 6.633, 46 : 6.782, 48 : 6.928, 52 : 7.211, 62 : 7.874, 66 : 8.124, 68 : 8.246, 70 : 8.366}
    list1 = list(dict1)
    list2 = list(dict2)
    listnum1 = [100,10000]
    listnum2 = [100, 400, 900, 10000, 40000, 90000]
    while(True):
        while(True):
            c1 = random.choice(list1)
            c2 = random.choice(list2)
            if(int(c1*10) == c2):
                break
        ##################1번#################
        num1 = random.choice(listnum1)
        if(num1 == 100):
            d1 = c1 / 100
            d1 = round(d1,3)
            d2 = 0.1
            e1 = 100
            e2 = 10
            e3 = d2
        else:
            d1 = c1 / 10000
            d1 = round(d1,5)
            d2 = 0.01
            e1 = 10000
            e2 = 100
            e3 = d2

        ############2번
        num2 = random.choice(listnum1)
        if (num2 == 100):
            d3 = c2 / 100
            d3 = round(d3, 2)
            d4 = 0.1
            e4 = 100
            e5 = 10
            e6 = d4
        else:
            d3 = c2 / 10000
            d3 = round(d3, 4)
            d4 = 0.01
            e4 = 10000
            e5 = 100
            e6 = d4
        ################ 3번
        num3 = random.choice(listnum2)
        d5 = int(c1*num3)
        d6 = int(num3**0.5)
        e7 = num3
        e8 = d6
        num4 = random.choice(listnum2)
        d7 = int(c2 * num4)
        d8 = int(num4**0.5)
        e9 = num4
        e10 = d8
        num5 = random.choice(listnum2)
        d9 = int(c1 * num5)
        d10 = int(num5**0.5)
        e11 = num5
        e12 = d10
        if(d1 != d3)&(d5 != d7)&(d7!=d9)&(d5!=d9):
            break
    left = '{'
    right ='}'
    stem = stem.format(c1=c1,c2=c2,d1=d1,d2=d2,d3=d3,d4=d4,d5=d5,d6=d6,d7=d7,d8=d8,d9=d9,d10=d10)
    answer = answer.format(a1 = answer_dict.get(2), a2 = answer_dict.get(4))
    comment = comment.format(c1=c1,c2=c2,d6=d6,d1=d1,d3=d3,d5=d5,d7=d7,d9=d9,e1=e1,e2=e2,e3=e3,e4=e4,e5=e5,e6=e6,e7=e7,e8=e8,e9=e9,e10=e10,e11=e11,e12=e12,\
                             left=left,right=right)
    return stem, answer, comment

#3-1-1-277
def realnum311_Stem_199():
    stem = "{eqt1}, {eqt2}일 때, {eqt3} {jo1} {var1}, {var2}를 이용하여 나타내면? \n① {s1}    ② {s2}    ③ {s3}    ④ {s4}    ⑤ {s5}\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt} \n\n"
    
    prime=[2,3,5,7]
    n_exp=[1,2]
    var1="a"
    var2="b"
    prime1=random.choice(prime)    
    prime2=random.choice(prime)
    while  prime1 == prime2 :
        prime2=random.choice(prime)
    ## 소인수 크기정렬
    if prime1 > prime2:
        prime1,prime2=prime2,prime1

    prime3=1
    in_root=1
    while True:
        prime3=random.choice(prime)
        while prime1==prime3 or prime2==prime3:
            prime3=random.choice(prime)
        n1=random.choice(n_exp)
        n2=random.choice(n_exp)
        n3=2
        in_root=(prime1**n1)*(prime2**n2)*(prime3**n3)
        if in_root < 400 : break
    
    eqt1=" `=` ".join([makeroot(prime1),var1])
    eqt2=" `=` ".join([makeroot(prime2),var2])
    eqt3=makeroot(in_root)
    jo1=proc_jo(in_root,1)
    
    comt1=makeroot(in_root)
    comt2=makeroot(factor_print(in_root))
    
    root_prime1=""
    root_prime1=""

    if n1 != 1:
        root_prime1="("+makeroot(prime1)+")"
    else :
        root_prime1=makeroot(prime1)
    if n2 != 1:
        root_prime2="("+makeroot(prime2)+")"
    else:
        root_prime2=makeroot(prime2)

    s1=str(prime3)+var1+var2
    s2=str(prime3)+var1+print_power(var2,2)
    s3=print_power(var1,2)+var2
    s4=str(prime3)+print_power(var1,2)+var2
    s5=print_power(var1,2)+print_power(var2,2)
    sol=[s1,s2,s3,s4,s5]
    
    comt3=str(prime3)+" `TIMES` "+print_power(root_prime1,n1)+" `TIMES` "+print_power(root_prime2,n2)
    comt4=str(prime3)+print_power(var1,n1)+print_power(var2,n2)
    comt=" `=` ".join([comt1,comt2,comt3,comt4])
    
    ans=""
    count=1
    for i in sol:
        if comt4==i:
            ans=answer_dict[count]
        count=count+1

    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), eqt3=addTag(eqt3), jo1=jo1, var1=addTag(var1), var2=addTag(var2), \
        s1=addTag(s1), s2=addTag(s2), s3=addTag(s3), s4=addTag(s4), s5=addTag(s5))
    answer = answer.format(ans=addTag(ans))
    comment = comment.format(comt=addTag(comt))
    return stem, answer, comment

#question_3_1_1_278():
def realnum311_Stem_200():    
    stem = "{eqt1}, {eqt2}일 때, {eqt3}의 값은?\n① {s1}    ② {s2}    ③ {s3}    ④ {s4}    ⑤ {s5}\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt1} 이므로\n {comt2}\n {comt3} 이므로\n {comt4}\n {comt5}\n\n"

    prime=[2,3,5,7,11]

    var1="a"
    var2="b"

    prime1=random.choice(prime)     #첫번째 등식 좌변 분자 루트 밖
    while prime1==11:
       prime1=random.choice(prime) 
    prime2=random.choice(prime)     #첫번째 등식 좌변 분자 루트 안
    while prime1 == prime2:
        prime2=random.choice(prime)
    prime3=random.choice(prime)     #첫번재 등식 좌변 분모 루트 안
    while prime3==prime1 or prime3==prime2:
        prime3=random.choice(prime)
    numer1=[prime1,prime2]
    denom1=prime3

    frac1=fraction(numer1,denom1)
    eqt1_1=makefrac(str(frac1.numer[0])+makeroot(frac1.numer[1]),makeroot(denom1))
    eqt1_2=var1+" `` "+makeroot(frac1.numer[1]*frac1.denom)
    eqt1=" `=` ".join([eqt1_1,eqt1_2])


    numer2=prime3     #두번째 등식 좌변 분자
    number1=random.choice(prime)    #두번째 등식 좌변 분모 루트 안 소인수
    while number1==frac1.numer[0]*frac1.denom:
        number1=random.choice(prime)
    
    number2=2*prime1   #두번째 등식 좌변 분모 루트 안 소인수와 곱해질 숫자
    while number2==number1:
        number2=random.randrange(3,5)
    frac2=fraction(numer2,number1* (number2**2) )
    
    eqt2_1=makefrac(frac2.numer,makeroot(frac2.denom))
    eqt2_2=var2+" `` "+makeroot(number1)
    eqt2=" `=` ".join([eqt2_1,eqt2_2])
    
    eqt3=makeroot(var1+var2)

    comt1_1=eqt1_1
    comt1_2=makefrac(str(frac1.numer[0])+makeroot(frac1.numer[1])+" `TIMES` "+ makeroot(frac1.denom),makeroot(frac1.denom)+" `TIMES` "+ makeroot(frac1.denom))
    frac1.change([frac1.numer[0],frac1.numer[1]*frac1.denom],frac1.denom)
    comt1_3=makefrac(str(frac1.numer[0])+makeroot(frac1.numer[1]),frac1.denom)
    comt1=" `=` ".join([comt1_1,comt1_2,comt1_3])

    frac1_reduct=Fraction(frac1.numer[0],frac1.denom)
    if frac1_reduct.numerator!=frac1.numer[0]:
        comt1_4=makefrac(str(frac1_reduct.numerator)+makeroot(frac1.numer[1]),str(frac1_reduct.denominator))
        comt1=" `=` ".join([comt1_1,comt1_2,comt1_3,comt1_4])

    comt2=" `=` ".join([var1,makefrac(frac1_reduct.numerator,frac1_reduct.denominator)])
    
    comt3_1=eqt2_1
    frac2.change(frac2.numer,[number2,number1])

    comt3_2=makefrac(frac2.numer,str(frac2.denom[0])+makeroot(frac2.denom[1]))
    comt3_3=makefrac(str(frac2.numer)+makeroot(frac2.denom[1]),str(frac2.denom[0])+makeroot(frac2.denom[1])+" `TIMES` "+makeroot(frac2.denom[1]))
    frac2.change([frac2.numer,frac2.denom[1]],frac2.denom[0]*frac2.denom[1])
    comt3_4=makefrac(rootout_print(frac2.numer[0]**2*frac2.numer[1]),frac2.denom)
    comt3=" `=` ".join([comt3_1,comt3_2,comt3_3,comt3_4])
    
    frac2_reduct=Fraction(frac2.numer[0],frac2.denom)
    if frac2_reduct.numerator!=frac2.numer[0]:
        comt3_5=makefrac(rootout_print(frac2_reduct.numerator**2*frac2.numer[1]),str(frac2_reduct.denominator))
        comt3=" `=` ".join([comt3_1,comt3_2,comt3_3,comt3_4,comt3_5])
   
    comt4=" `=` ".join([var2,makefrac(frac2_reduct.numerator,frac2_reduct.denominator)])
        
    comt5_1="THEREFORE ~"
    comt5_2=makeroot(var1+var2)
    comt5_3=makeroot(makefrac(frac1_reduct.numerator,frac1_reduct.denominator)+" `TIMES` "+makefrac(frac2_reduct.numerator,frac2_reduct.denominator))

    frac3=fraction(frac1_reduct.numerator*frac2_reduct.numerator,frac1_reduct.denominator*frac2_reduct.denominator)
    frac3.reduct()
    
    comt5_4=makeroot(makefrac(frac3.numer,frac3.denom))
    frac3.change(frac3.numer*frac3.denom,frac3.denom)
    frac3.change(rootout(frac3.numer),frac3.denom)
    frac3_reduct=Fraction(frac3.numer[0],frac3.denom)
    frac3.change([frac3_reduct.numerator,frac3.numer[1]],frac3_reduct.denominator)
    comt5_5=makefrac(rootout_print(frac3.numer[0]**2*frac3.numer[1]),frac3.denom)
    
    comt5=" `=` ".join([comt5_1+comt5_2,comt5_3,comt5_4,comt5_5])
    
    s1=""
    s2=""
    s3=""
    s4=""
    s5=""
    ans=""

    if number1==2:
        s1=makefrac(1,2)
        s2=makefrac(makeroot(2),2)
        s3=makefrac(1,4)
        s4=makefrac(makeroot(2),4)
        s5="1"
        ans=answer_dict[1]
    elif number1==3:
        s1=makefrac(1,3)
        s2=makefrac(makeroot(3),3)
        s3=makefrac(1,6)
        s4=makefrac(makeroot(3),6)
        s5=makefrac(makeroot(6),6)
        ans=answer_dict[5]
    elif number1==5:
        s1=makefrac(1,5)
        s2=makefrac(makeroot(5),5)
        s3=makefrac(makeroot(5),10)
        s4=makefrac(makeroot(10),10)
        s5=makefrac(1,2)
        ans=answer_dict[4]
    elif number1==7:
        s1=makefrac(1,7)
        s2=makefrac(makeroot(7),7)
        s3=makefrac(makeroot(14),7)
        s4=makefrac(7,14)
        s5=makefrac(makeroot(14),14)
        ans=answer_dict[5]
    elif number1==11:
        s1=makefrac(1,11)
        s2=makefrac(makeroot(11),11)
        s3=makefrac(1,22)
        s4=makefrac(makeroot(11),22)
        s5=makefrac(makeroot(22),22)
        ans=answer_dict[5]


    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), eqt3=addTag(eqt3),s1=addTag(s1), s2=addTag(s2), s3=addTag(s3), s4=addTag(s4), s5=addTag(s5))
    answer = answer.format(ans=addTag(ans))
    comment = comment.format(comt1=addTag(comt1), comt2=addTag(comt2), comt3=addTag(comt3), comt4=addTag(comt4), comt5=addTag(comt5))

    return stem, answer, comment

#question_3_1_1_279
def realnum311_Stem_201():
    stem = "{eqt1}일 때, {eqt2}{jo1} {var}에 관한 식으로 나타내면? \n① {s1}    ② {s2}    ③ {s3}    ④ {s4}    ⑤ {s5}\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt} \n\n"

    dec=[2,3,5,7,11]
    numlist_of_dec=[1,2]
    dec_out=[2,3,5,7,11,13]
    numlist_of_dec_out=[1,2]
    var="k"
    # 루트 안 설정
    while True:
        list_of_dec=[]
        in_root=1
        num_of_dec=random.choice(numlist_of_dec)
        for i in range(0,num_of_dec):
            ran_dec=random.choice(dec)
            while ran_dec in list_of_dec:
                ran_dec=random.choice(dec)
            list_of_dec.append(ran_dec)
            in_root=in_root*(list_of_dec[i])
        if in_root<40: break

    ## 루트 안 과 밖 소인수 중복 방지
    for i in range(0,num_of_dec):
        if list_of_dec[i] in dec_out:
            dec_out.remove(list_of_dec[i])

    #루트 밖 설정
    while True:
        list_of_dec_out=[]
        out_root=1
        num_of_dec_out=random.choice(numlist_of_dec_out)
        for i in range(0,num_of_dec_out):
            ran_dec_out=random.choice(dec_out)
            while (ran_dec_out in list_of_dec_out):
                ran_dec_out=random.choice(dec)
            list_of_dec_out.append(ran_dec_out)
            out_root=out_root*(list_of_dec_out[i])
        if out_root<16 : break
    
    root=in_root*(out_root**2)

    eqt1="sqrt{%d} = {%s}"%(in_root,"k")
    eqt2="sqrt{%d}"%root
    jo1=proc_jo(root%10,1)
    comt1_1="{%d ^ 2}" %(out_root)
    comt1 = eqt2+ " `=` " + "sqrt {" + comt1_1 + " `TIMES` " + "%d"%in_root + "}"
    comt2 = "%d"%out_root + "sqrt {"+"%d"%in_root +"}" + " `=` " +"%d"%out_root+"%s"%("k")
    comt = comt1+" `=` "+comt2
    
    if out_root<10:
        s1=makefrac(1,out_root*10)+var
        s2=makefrac(1,out_root**2)+var
        s3=makefrac(1,out_root)+var
        s4=str(out_root)+var
        s5=str(10*out_root)+var
        ans=answer_dict[4]
    else:
        s1=makefrac(1,out_root*10)+var
        s2=makefrac(1,out_root)+var
        s3=str(out_root)+var
        s4=str(10*out_root)+var
        s5=str(100*out_root)+var
        ans=answer_dict[3]

    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), jo1=(jo1), var=addTag(var),s1=addTag(s1), s2=addTag(s2), s3=addTag(s3), s4=addTag(s4), s5=addTag(s5))
    answer = answer.format(ans=addTag(ans))
    comment = comment.format(comt=addTag(comt))
    return stem, answer, comment

#question_3_1_1_280
def realnum311_Stem_202():
    stem = "{eqt1}, {eqt2}라고 할 때, {eqt3}의 값과 같은 것은? \n ① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5} \n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt} \n\n"

    dec_list=[2,3,5,7,11]
    num_list=[-2,-2,2,3]
    
    dec = random.choice(dec_list)
    num_ = random.choice(num_list)

    num=10**num_
    if num_< 0:
        root= round(dec*num,-(num_))
    else:
        root = dec*num
    var1="a"
    var2="b"

    s1=makefrac(var1,"10")
    s2=makefrac(var1,"100")
    s3="".join(["10",var1])
    s4=makefrac(var2,10)
    s5="".join(["10",var2])

    eqt1="".join([makeroot(dec), "=", var1,"}"])
    eqt2="".join([makeroot(dec*10), "=", var2])
    eqt3="".join([makeroot(root)])
    
    comt1="".join([makeroot(root)])
    ans=""
    comt=""
    if num==0.01 :
        comt2="".join([makeroot(makefrac(str(dec),"100"))])
        comt3="".join([makefrac(makeroot(str(dec)),"10")])
        comt4="".join([makefrac(var1,"10")])
        comt="=".join([comt1,comt2,comt3,comt4])
        ans= "①"
    elif num==0.1:
        comt2="".join([makeroot(makefrac(str(dec),"10"))])
        comt3="".join([makeroot(makefrac(str(10*dec),"100"))])
        comt4="".join([makefrac(makeroot(str(10*dec)),"10")])
        comt5="".join([makefrac(var2,"10")])
        comt="=".join([comt1,comt2,comt3,comt4,comt5])
        ans="④"
    elif num==100:
        comt2="".join([makeroot("10^2 TIMES"+str(dec))])
        comt3="".join(["10",makeroot(str(dec))])
        comt4="".join(["10",var1])
        comt="=".join([comt1,comt2,comt3,comt4])
        ans="③"
    elif num==1000:
        comt2="".join([makeroot("10^2 TIMES"+str(10*dec))])
        comt3="".join(["10",makeroot(str(10*dec))])
        comt4="".join(["10",var2])
        comt="=".join([comt1,comt2,comt3,comt4])
        ans="⑤"

    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), eqt3=addTag(eqt3), s1=addTag(s1), s2=addTag(s2),s3=addTag(s3),s4=addTag(s4),s5=addTag(s5))
    answer = answer.format(ans=ans)
    comment = comment.format(comt=addTag(comt))
    return stem, answer, comment

#question_3_1_1_281
def realnum311_Stem_203():
    stem = "{eqt1}, {eqt2}일 때, {eqt3}{jo1} {var1}, {var2}를 이용하여 나타내면?\n ① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt} \n\n"

    dec_list=[2,3,5,7,11,13]
    num_list=[1,2]

    dec1 = random.choice(dec_list)
    while True:
        dec2 = random.choice(dec_list)
        if dec1 != dec2: break
    
    if dec1>dec2:
        dec1,dec2=dec2,dec1
    
    num1=random.choice(num_list)
    num2=random.choice(num_list)

    
    while True:
        coef1=[]
        codec1=1
        for i in range(0,num1):
            while True:
                coef=random.choice(dec_list)
                if coef not in coef1: 
                    coef1.append(coef)
                    break
            codec1=codec1*coef
        if (codec1**2)*dec1 <1000: break

    while True:
        coef2=[]
        codec2=1
        for i in range(0,num1):
            while True:
                coef=random.choice(dec_list)
                if coef not in coef2: 
                    coef2.append(coef)
                    break
            codec2=codec2*coef
        if (codec2**2)*dec2<1000:break

    order=random.choice([True,False])
    porm=random.choice([" `+` "," `-` "])
    var1="x"
    var2="y"

    eqt1="".join([makeroot(dec1)," `=` ",var1])
    eqt2="".join([makeroot(dec2)," `=` ",var2])

    if order == True:
        eqt3="".join([makeroot(codec1**2 *dec1),porm,makeroot(codec2**2 * dec2)])
        jo1=proc_jo(codec2**2 * dec2%10,1)
        comt1=eqt3
        comt2="".join([makeroot(str(codec1)+"^2 `TIMES` "+ str(dec1)), porm,makeroot(str(codec2)+"^2 `TIMES` "+ str(dec2))])
        comt3="".join([str(codec1),makeroot(str(dec1)),porm,str(codec2),makeroot(str(dec2))])
        comt4="".join([str(codec1),var1,porm,str(codec2),var2])
        comt="=".join([comt1,comt2,comt3,comt4])

    else:
        eqt3="".join([makeroot(codec2**2 *dec2),porm,makeroot(codec1**2 * dec1)])
        jo1=proc_jo(codec1**2 * dec1%10,1)
        comt1=eqt3
        comt2="".join([makeroot(str(codec2)+"^2 `TIMES` "+ str(dec2)), porm,makeroot(str(codec1)+"^2 `TIMES` "+ str(dec1))])
        comt3="".join([str(codec2),makeroot(str(dec2)),porm,str(codec1),makeroot(str(dec1))])
        if porm == " `+` ":
            comt4="".join([str(codec2),var2," `+` ",str(codec1),var1])
            comt5="".join([str(codec1),var1," `+` ",str(codec2),var2])
        else:
            comt4="".join([str(codec2),var2,porm,str(codec1),var1])
            comt5="".join([porm,str(codec1),var1," `+` ",str(codec2),var2])
        comt=" `=` ".join([comt1,comt2,comt3,comt4,comt5])
    
    if codec1!=codec2:
        s1="".join([str(codec1),var1," `+` ",str(codec2),var2])
        s2="".join([" `-` "+str(codec1),var1," `+` ",str(codec2),var2])
        s3="".join([str(codec1),var1," `+` ",str(codec1),var2])
        s4="".join([str(codec1),var1," `-` ",str(codec2),var2])
        s5="".join([" `-` "+str(codec1),var1," `-` ",str(codec2),var2])
        
        if porm == " `+` ":
                ans=answer_dict[1]
        else:
            if order==True:
                ans=answer_dict[4]
            else:
                ans=answer_dict[2]
    else:
        s1="".join([str(codec1),var1," `+` ",str(codec2),var2])
        s2="".join([" `-` "+str(codec1),var1," `+` ",str(codec2),var2])
        s3="".join([str(codec1),var1," `-` ",str(codec2),var2])
        s4="".join([" `-` "+str(codec1),var1," `-` ",str(codec2*2),var2])
        s5="".join([str(2*codec1),var1," `+` ",str(codec2),var2])

        if porm == " `+` ":
            ans=answer_dict[1]
        else:
            if order ==True:
                ans=answer_dict[3]
            else:
                ans=answer_dict[2]
    

    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), eqt3=addTag(eqt3),jo1=addTag(jo1), var1=var1, var2=var2, s1=addTag(s1), s2=addTag(s2),s3=addTag(s3),s4=addTag(s4),s5=addTag(s5))
    answer = answer.format(ans=ans)
    comment = comment.format(comt=addTag(comt))
    return stem, answer, comment

#question_3_1_1_282
def realnum311_Stem_204():
    stem = "{eqt1}일 때, {eqt2}{jo1} {var}에 관한 식으로 나타내면? \n ① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt} \n\n"

    prime_list=[2,3,5,7,11,13]
    dec_list=[-4,-2]

    num_of_prime=random.choice([1])
    
    list_of_prime=[]

    in_root_prime=1

    for i in range(0,num_of_prime):
        prime=random.choice(prime_list)
        
        while prime in list_of_prime:
            prime=random.choice(prime_list)
        
        in_root_prime=in_root_prime*prime
        list_of_prime.append(prime)

    coef_list=[2,3,5,7,11,13]

    for i in list_of_prime:
        if i in coef_list:
            coef_list.remove(i)
    
    while True:
        coef=random.choice(coef_list)
        in_root=in_root_prime*(coef**2)
        if in_root<200:break

    var="a"

    dec_=random.choice(dec_list)
    dec=10**dec_

    eqt1="".join([makeroot(in_root_prime), "=", var,"}"])
    eqt2="".join([makeroot(round(in_root*dec,-dec_))])
    jo1=proc_jo(in_root%10,1)

    if dec == 0.0001 :
        comt1=eqt2
        comt2="".join([makeroot(makefrac(in_root,"10000"))])
        comt3="".join([makefrac(makeroot(in_root),"100")])
        
        list_of_factor=factor(in_root)
        root_out=1
        root_in=1

        for i in list_of_factor:
            if i[1]%2==0:
                root_out=root_out*(i[0]**(i[1]//2))
            else:
                root_out=root_out*(i[0]**(i[1]//2))
                root_in=root_in*i[0]
        comt4="".join([makefrac(str(root_out)+makeroot(root_in),100)])
        
        frac=Fraction(root_out,100)

        numer=frac.numerator
        denom=frac.denominator

        if numer != 1:
            comt5="".join([makefrac(str(numer)+makeroot(root_in),denom)])
            comt6="".join([makefrac(str(numer),denom),var])
        else :
            comt5="".join([makefrac(makeroot(root_in),denom)])
            comt6="".join([makefrac(str(numer),denom),var])
        comt="=".join([comt1,comt2,comt3,comt4,comt5,comt6])

    elif dec==0.01:
        comt1=eqt2
        comt2="".join([makeroot(makefrac(in_root,"100"))])
        comt3="".join([makefrac(makeroot(in_root),"10")])
        
        list_of_factor=factor(in_root)
        root_out=1
        root_in=1

        for i in list_of_factor:
            if i[1]%2==0:
                root_out=root_out*(i[0]**(i[1]//2))
            else:
                root_out=root_out*(i[0]**(i[1]//2))
                root_in=root_in*i[0]

        frac=Fraction(root_out,10)
        numer=frac.numerator
        denom=frac.denominator

        if numer != 1:
            comt4="".join([makefrac(str(numer)+makeroot(root_in),denom)])
            comt5="".join([makefrac(str(numer),denom),var])
        else:
            comt4="".join([makefrac(makeroot(root_in),denom)])
            comt5="".join([makefrac(str(numer),denom),var])

        comt="=".join([comt1,comt2,comt3,comt4,comt5])
    if denom >20:
        s1=makefrac(numer,denom)+var
        s2=makefrac(numer,denom)+print_power(var,2)
        s3=makefrac(numer,denom//10)+var
        s4=makefrac(numer,denom//10)+print_power(var,2)
        s5=makefrac(numer,denom//10)+print_power(var,3)
        ans=answer_dict[1]

    else:
        s1=makefrac(numer,denom*10)+var
        s2=makefrac(numer,denom*10)+print_power(var,2)
        s3=makefrac(numer,denom*10)+print_power(var,3)
        s4=makefrac(numer,denom)+var
        s5=makefrac(numer,denom)+print_power(var,2)
        ans=answer_dict[4]

    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), jo1=addTag(jo1), var=addTag(var), s1=addTag(s1), s2=addTag(s2),s3=addTag(s3),s4=addTag(s4),s5=addTag(s5))
    answer = answer.format(ans=ans)
    comment = comment.format(comt=addTag(comt))
    return stem, answer, comment

#question_3_1_1_283
def realnum311_Stem_205():
    stem = "{eqt1}일 때, {eqt2}의 값을 {var}에 관한 식으로 나타내면? \n① {s1}    ② {s2}    ③ {s3}    ④ {s4}    ⑤ {s5}\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt} \n\n"

    prime_list=[2,3,5,7,11,13]
    coef_list=[0.1,0.2,0.3,0.4,0.5,0.6,0.7]
    var="a"

    while True:
        prime=random.choice(prime_list)
        
        coef1=random.choice(coef_list)
        coef2=random.choice(coef_list)

        while coef1 == coef2 :
            coef2=random.choice(coef_list)
        
        in_root1=round((coef1**2)*prime,2)
        in_root2=round((coef2**2)*prime,2)
        
        degit_of_in_root1=degit_of_num(in_root1)
        degit_of_in_root2=degit_of_num(in_root2)

        if degit_of_in_root1 == degit_of_in_root2:break
    
    eqt1="".join([makeroot(prime)," = ",var])
    eqt2="".join([makeroot(in_root1)," + ",makeroot(in_root2)])
    
    comt=[]

    comt1=eqt2
    #########################################
    frac1=fraction(int(in_root1*10**degit_of_in_root1),10**degit_of_in_root1)
    frac2=fraction(int(in_root2*10**degit_of_in_root2),10**degit_of_in_root2)

    comt2=" + ".join([makeroot(frac1.print()),makeroot(frac2.print())])
    #########################################
    frac1.change(frac1.numer*frac1.denom,frac1.denom)
    frac2.change(frac2.numer*frac2.denom,frac1.denom)

    in_root_3_1=frac1.numer_factor_print()
    in_root_3_2=frac2.numer_factor_print()

    frac1_3=makefrac(makeroot(in_root_3_1),frac1.denom)
    frac2_3=makefrac(makeroot(in_root_3_2),frac2.denom)
    comt3=" + ".join([frac1_3,frac2_3])
    ###########################################
    in_root=rootout(frac1.numer)[1]
    frac1.change(rootout(frac1.numer)[0],frac1.denom)
    frac2.change(rootout(frac2.numer)[0],frac2.denom)
    
    frac1_4=makefrac(str(frac1.numer)+makeroot(in_root),frac1.denom)
    frac2_4=makefrac(str(frac2.numer)+makeroot(in_root),frac2.denom)
    comt4=" + ".join([frac1_4,frac2_4])
    #########################################
    frac1.change(frac1.numer,frac1.denom)
    frac2.change(frac2.numer,frac2.denom)
    new_frac=frac1.add(frac2)
    comt5="".join([makefrac_good(new_frac.numer,new_frac.denom),makeroot(in_root)])
    if makefrac_good(new_frac.numer,new_frac.denom)=="1":
        comt5="".join([makeroot(in_root)])
    ######################

    if new_frac.numer>new_frac.denom:
        s1=makefrac_good(Fraction(new_frac.numer-2,new_frac.denom).numerator,Fraction(new_frac.numer-2,new_frac.denom).denominator)
        s2=makefrac_good(Fraction(new_frac.numer-1,new_frac.denom).numerator,Fraction(new_frac.numer-1,new_frac.denom).denominator)
        s3=makefrac_good(Fraction(new_frac.numer,new_frac.denom).numerator,Fraction(new_frac.numer,new_frac.denom).denominator)
        s4=makefrac_good(Fraction(new_frac.numer+1,new_frac.denom).numerator,Fraction(new_frac.numer+1,new_frac.denom).denominator)
        s5=makefrac_good(Fraction(new_frac.numer+2,new_frac.denom).numerator,Fraction(new_frac.numer+2,new_frac.denom).denominator)
        ans=answer_dict[3]
    else:
        s1=makefrac_good(Fraction(new_frac.numer,new_frac.denom).numerator,Fraction(new_frac.numer,new_frac.denom).denominator)
        s2=makefrac_good(Fraction(new_frac.numer+1,new_frac.denom).numerator,Fraction(new_frac.numer+1,new_frac.denom).denominator)
        s3=makefrac_good(Fraction(new_frac.numer+2,new_frac.denom).numerator,Fraction(new_frac.numer+2,new_frac.denom).denominator)
        s4=makefrac_good(Fraction(new_frac.numer+3,new_frac.denom).numerator,Fraction(new_frac.numer+3,new_frac.denom).denominator)
        s5=makefrac_good(Fraction(new_frac.numer+4,new_frac.denom).numerator,Fraction(new_frac.numer+4,new_frac.denom).denominator)
        ans=answer_dict[1]

    comt=" = ".join([comt1,comt2+"# #",comt3+"# #",comt4,comt5+"# #"])
    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), var=addTag(var), s1=addTag(s1), s2=addTag(s2),s3=addTag(s3),s4=addTag(s4),s5=addTag(s5))
    answer = answer.format(ans=ans)
    comment = comment.format(comt=addTag(comt))
    return stem, answer, comment

    #question_3_1_1_284
def realnum311_Stem_206():
    stem = "{eqt1} , {eqt2}일 때, 다음 중 옳은 것은? \n① {s1}    ② {s2}    ③ {s3}    ④ {s4}    ⑤ {s5}\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt} \n\n"

    var1="a"
    var2="b"

    prime_list=[2,3,5,7,11,13]
    prime=random.choice(prime_list)

    eqt1="".join([makeroot(prime)," `=` ",var1])
    eqt2="".join([makeroot(10*prime)," `=` ",var2])

    s=random.choice([1,3,4,5])

    if s==1 :
        s1="".join([makeroot(round(prime*10**-4,4))," `=` ",makefrac(var1,100)])
        s2="".join([makeroot(round(prime*10**-3,3))," `=` ",makefrac(var2,10)])
        s3="".join([makeroot(round(prime*10**-1,1))," `=` ",makefrac(var1,10)])
        s4="".join([makeroot(prime*10**3)," = ","10",var1])
        s5="".join([makeroot(prime*10**4)," = ","100",var2])
        ans="①"

    elif s==3 :
        s1="".join([makeroot(round(prime*10**-4,4))," `=` ",makefrac(var2,100)])
        s2="".join([makeroot(round(prime*10**-3,3))," `=` ",makefrac(var1,100)])
        s3="".join([makeroot(round(prime*10**-1,1))," `=` ",makefrac(var2,10)])
        s4="".join([makeroot(prime*10**3)," = ","10",var1])
        s5="".join([makeroot(prime*10**4)," = ","100",var2])
        ans="③"
    elif s==4 :
        s1="".join([makeroot(round(prime*10**-4,4))," `=` ",makefrac(var2,100)])
        s2="".join([makeroot(round(prime*10**-3,3))," `=` ",makefrac(var1,100)])
        s3="".join([makeroot(round(prime*10**-1,1))," `=` ",makefrac(var1,10)])
        s4="".join([makeroot(prime*10**3)," `=` ","10",var2])
        s5="".join([makeroot(prime*10**4)," `=` ","100",var2])
        ans="④"
    elif s==5 :
        s1="".join([makeroot(round(prime*10**-4,4))," `=` ",makefrac(var2,100)])
        s2="".join([makeroot(round(prime*10**-3,3))," `=` ",makefrac(var1,100)])
        s3="".join([makeroot(round(prime*10**-1,1))," `=` ",makefrac(var1,10)])
        s4="".join([makeroot(prime*10**3)," `=` ","10",var1])
        s5="".join([makeroot(prime*10**4)," `=` ","100",var1])
        ans="⑤"

    comt1_1="".join(["①",makeroot(round(prime*10**-4,4))," `=` ", makeroot(makefrac(prime,"{100 }^ {2}"))])
    comt1_2="".join([makefrac(makeroot(prime),"100")])
    comt1_3="".join([makefrac(var1,100)])
    comt1=" `=` ".join([comt1_1,comt1_2,comt1_3])

    comt2_1="".join(["②",makeroot(round(prime*10**-3,3))," `=` ", makeroot(makefrac(prime*10,"{100 }^ {2}"))])
    comt2_2="".join([makefrac(makeroot(prime*10),"100")])
    comt2_3="".join([makefrac(var2,100)])
    comt2=" `=` ".join([comt2_1,comt2_2,comt2_3])

    comt3_1="".join(["③",makeroot(round(prime*10**-1,1))," `=` ", makeroot(makefrac(prime*10,"{10 }^ {2}"))])
    comt3_2="".join([makefrac(makeroot(prime*10),"10")])
    comt3_3="".join([makefrac(var2,10)])
    comt3=" `=` ".join([comt3_1,comt3_2,comt3_3])
    
    comt4_1="".join(["④",makeroot(prime*10**3)," `=` ", makeroot(str(prime*10) +"TIMES"+"{10 }^ {2}")])
    comt4_2="".join(["10"+makeroot(10*prime)])
    comt4_3="".join(["10"+var2])
    comt4=" `=` ".join([comt4_1,comt4_2,comt4_3])

    comt5_1="".join(["⑤",makeroot(prime*10**4)," `=` ", makeroot(str(prime) +"TIMES"+"{100 }^ {2}")])
    comt5_2="".join(["100"+makeroot(prime)])
    comt5_3="".join(["100"+var1])
    comt5=" `=` ".join([comt5_1,comt5_2,comt5_3])

    comt="#".join([comt1,comt2,comt3,comt4,comt5])

    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), s1=addTag(s1), s2=addTag(s2),s3=addTag(s3),s4=addTag(s4),s5=addTag(s5))
    answer = answer.format(ans=ans)
    comment = comment.format(comt=addTag(comt))
    return stem, answer, comment

#question_3_1_1_285
def realnum311_Stem_207():
    stem = "다음 중 {eqt1} , {eqt2}일 때,{eqt3}{jo1} {var1}, {var2}를 사용하여 바르게 나타낸 것은? \n① {s1}    ② {s2}    ③ {s3}    ④ {s4}    ⑤ {s5}\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt} \n\n"
    
    var1="a"
    var2="b"
    
    prime=[2,3,5,7,11,13]
    dec=[2,4]

    prime1 = random.choice(prime)
    prime2 = random.choice(prime)
    while prime1==prime2:
        prime2 = random.choice(prime)
    
    if prime1>prime2:
        prime1,prime2=prime2,prime1
    
    prime3 = random.choice(prime)
    while prime3==prime1 or prime3==prime2:
        prime3 = random.choice(prime)
    
    if prime2>prime3:
        prime2,prime3=prime3,prime2

    dec1=random.choice(dec)

    eqt1=" `=` ".join([makeroot(prime2),var1])
    eqt2=" `=` ".join([makeroot(prime3),var2])
    eqt3=makeroot(round(prime1**2*prime2*prime3*10**(-dec1),dec1))

    jo1=proc_jo(prime1**2*prime2*prime3%10,1)
    frac=fraction(prime1**2*prime2*prime3,10**dec1)

    comt1=eqt3
    comt2=makeroot(makefrac(frac.numer,frac.denom))
    comt3=makeroot(makefrac(factor_print(frac.numer),print_power(10,dec1)))
    comt4=makefrac(rootout_print(frac.numer),10**(dec1//2))
    frac_reduct=Fraction(rootout(frac.numer)[0],10**(dec1//2))
    comt5=makefrac(frac_reduct.numerator,frac_reduct.denominator)+ " `TIMES` "+makeroot(rootout(frac.numer)[1])
    comt6=makefrac(frac_reduct.numerator,frac_reduct.denominator)+ " `TIMES` "+makeroot(str(prime2)+" `TIMES` "+str(prime3))
    comt7=makefrac(frac_reduct.numerator,frac_reduct.denominator)+ " `TIMES` "+makeroot(str(prime2))+" `TIMES` "+makeroot(str(prime3))
    comt8=makefrac(frac_reduct.numerator,frac_reduct.denominator)+var1+var2
    comt=" `=` ".join([comt1,comt2,comt3,comt4,comt5+"#",comt6,comt7,comt8])
    
    if frac_reduct.denominator>30:
        s1=makefrac_reduct(frac_reduct.numerator*2,frac_reduct.denominator)+print_power(var1,2)+var2
        s2=makefrac_reduct(frac_reduct.numerator*2,frac_reduct.denominator)+var1+print_power(var2,3)
        s3=makefrac_reduct(frac_reduct.numerator*2,frac_reduct.denominator)+var1+var2
        s4=makefrac_reduct(frac_reduct.numerator,frac_reduct.denominator)+var1+var2
        s5=makefrac_reduct(frac_reduct.numerator,frac_reduct.denominator)+print_power(var1,2)+var2
        ans=answer_dict[4]
    else:
        s1=makefrac_reduct(frac_reduct.numerator,frac_reduct.denominator)+print_power(var1,2)+var2
        s2=makefrac_reduct(frac_reduct.numerator,frac_reduct.denominator)+var1+print_power(var2,3)
        s3=makefrac_reduct(frac_reduct.numerator,frac_reduct.denominator)+var1+var2
        s4=makefrac_reduct(frac_reduct.numerator,frac_reduct.denominator*2)+var1+var2
        s5=makefrac_reduct(frac_reduct.numerator,frac_reduct.denominator*2)+print_power(var1,2)+var2
        ans=answer_dict[3]


    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), eqt3=addTag(eqt3), jo1=jo1, var1=addTag(var1), var2=addTag(var2), \
        s1=addTag(s1), s2=addTag(s2),s3=addTag(s3),s4=addTag(s4),s5=addTag(s5))
    answer = answer.format(ans=ans)
    comment = comment.format(comt=addTag(comt))
    return stem, answer, comment

#question_3_1_1_286
def realnum311_Stem_208():
    stem = "다음 중 {eqt1} , {eqt2}일 때,{eqt3}이다. 이때 유리수 {var1}, {var2}에 대하여 {eqt4}의 값은? \n① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5} \n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt1}\n {comt2}\n 따라서 {comt3}이므로\n{comt4} \n{comt5}\n\n"
    
    var1="a"
    var2="b"
    var_1='x'
    var_2='y'
    prime_list=[2,3,5,7,11,13]
    
    prime1 = random.choice(prime_list)

    while True:
        prime2 = random.choice(prime_list)
        if prime1 != prime2 and prime1*prime2 <50: break
    
    if prime1>prime2:
        prime1,prime2=prime2,prime1

    coef1=random.randrange(2,10)
    while (coef1**2*prime1>100):
        coef1=random.randrange(2,10)
    
    coef2=random.randrange(2,10)
    while (coef2**2*prime1*prime2>250):
        coef2=random.randrange(2,10)
    
    in_root1=prime1*coef1**2
    in_root2=prime1*prime2*coef2**2

    eqt1="".join([makeroot(prime1), " `=` ", var1])
    eqt2="".join([makeroot(prime2), " `=` ", var2])
    eqt3="".join([makeroot(in_root1), " `-` ",makeroot(in_root2), " `=` ", var1, var_1," `+` ",var2, var_1, var_2])
    eqt4="".join([var1,var2])

    comt1_1="".join([makeroot(in_root1)])
    comt1_2="".join([makeroot(print_power(coef1,2)+" `TIMES` "+str(prime1))])
    

    comt1_3="".join([str(coef1), makeroot(prime1) ])
    comt1_4="".join([str(coef1),var_1])

    comt1=" `=` ".join([comt1_1,comt1_2,comt1_3,comt1_4])

    comt2_1="".join([makeroot(in_root2)])
    comt2_2="".join([makeroot(print_power(coef2,2)+"  `TIMES` "+str(prime1)+" `TIMES` "+str(prime2))])
    comt2_3=" `TIMES` ".join([str(coef2),makeroot(prime1),makeroot(prime2)])
    comt2_4="".join([str(coef2),var_1,var_2])
    
    comt2=" `=` ".join([comt2_1,comt2_2,comt2_3,comt2_4])

    comt3= "".join([makeroot(in_root1), " `-` ",makeroot(in_root2)," `=` ", str(coef1),var_1," `-` ", str(coef2), var_2])
    
    comt4="".join([var1," `=` ",str(coef1), ",``",var2, " `=` ", str(-coef2)])
    comt5="".join(["THEREFORE ", "``",var1, var2," `=` ", str(-coef1*coef2)])

    coff=coef1*coef2
    if coff %2==0:
        if coff >10:
            s1=str(-coff)
            s2=str(-(coff-2))
            s3=str(-(coff-2-2))
            s4=str(-(coff-2-2-2))
            s5=str(-(coff-2-2-2-2))
            ans = "①"
        else:
            s1=str(-(coff+2+2))
            s2=str(-(coff+2))
            s3=str(-(coff))
            s4=str(-(coff-2))
            s5=str(-(coff-2-2))
            ans= "③"
    else:
        if coff >10:
            s1=str(-(coff+2))
            s2=str(-(coff))
            s3=str(-(coff-2))
            s4=str(-(coff-2-2))
            s5=str(-(coff-2-2-2))
            ans = "②"
        else:
            s1=str(-(coff+2+2+2))
            s2=str(-(coff+2+2))
            s3=str(-(coff+2))
            s4=str(-(coff))
            s5=str(-(coff-2))
            ans= "④"

    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), eqt3=addTag(eqt3), eqt4=addTag(eqt4), var1=addTag(var1), var2=addTag(var2),s1=addTag(s1),
    s2=addTag(s2),s3=addTag(s3),s4=addTag(s4),s5=addTag(s5))

    answer = answer.format(ans=ans)
    comment = comment.format(comt1=addTag(comt1),comt2=addTag(comt2),comt3=addTag(comt3),comt4=addTag(comt4),comt5=addTag(comt5))
    return stem, answer, comment

#question_3_1_1_287
def realnum311_Stem_209():
    stem = "다음 중 {eqt1}, {eqt2}일 때, {eqt3}{jo1} {var1}, {var2}를 사용하여 바르게 나타낸 것은? \n① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5} \n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt} \n\n"
    
    var1="a" #첫번째 변수
    var2="b" #두번째 변수
    sol=0 #답 번호

    num=random.randrange(101,500) #루트안 기본 숫자
    while(str(num)[2]=="0"):
        num=random.randrange(101,500)

    in_root1=round(num*(0.01),2) #첫번째 루트 안의 숫자 
    in_root2=round(num*(0.1),1) #두번째 루트 안의 숫자

    dec_list=[0.1,10] #문제 루트속 숫자 자릿수 설정
    dec_1=random.choice(dec_list) #첫번째 루트속 자릿수

    dec_2=random.choice(dec_list) #두번째 루트속 자릿수
    

    if dec_1==0.1:
        dec_2=10 

    if dec_1==0.1:
        pro_in_root1=round(num*dec_1**4,4)
        pro_in_root2=round(num*10)
        sol=2

    else:
        pro_in_root1=num
        
        if dec_2==0.1:
            pro_in_root2=round(num*dec_2**3,3)
            sol=4
        else:
            pro_in_root2=round(num*10)
            sol=5


    eqt1="".join([makeroot(in_root1)," `=` ", var1])
    eqt2="".join([makeroot(in_root2)," `=` ", var2])
    eqt3=" `+` ".join([makeroot(pro_in_root1),makeroot(pro_in_root2)])
    jo1=proc_jo(pro_in_root2%10,1)

    ans= answer_dict[sol]

    s1="".join([makefrac(var1,10), " `+` ", makefrac(var2,100)])
    s2="".join([makefrac(var1,10), " `+` ", "10",var2])
    s3="".join(["10",var1," `+` ",makefrac(var2,100)])
    s4="".join(["10",var1," `+` ",makefrac(var2,10)])
    s5="".join(["10",var1," `+` " , "10",var2])

    comt1_1=makeroot(pro_in_root1)
    comt1_2="".join([makeroot(str(round(dec_1**2,2*degit_of_num(dec_1)))+"`TIMES`"+str(in_root1))])

    comt1_3=""
    comt1_4=""

    if dec_1== 0.1:
        comt1_3="".join([makefrac(1,10),makeroot(in_root1)])
        comt1_4="".join([makefrac(var1,10)])
    else:
        comt1_3="".join([str(dec_1),makeroot(in_root1)])
        comt1_4="".join([str(dec_1),var1])

    comt1=" `=` ".join([comt1_1,comt1_2,comt1_3,comt1_4])
    
    comt2_1=makeroot(pro_in_root2)
    comt2_2="".join([makeroot(str(round(dec_2**2,2*degit_of_num(dec_2)))+"`TIMES`"+str(in_root2))])
    
    comt2_3=""
    comt2_4=""

    if dec_2== 0.1:
        comt2_3="".join([str(dec_2),makeroot(in_root2)])
        comt2_4="".join([makefrac(var2,10)])
    else:
        comt2_3="".join([str(dec_2),makeroot(in_root2)])
        comt2_4="".join([str(dec_2),var2])

    comt2=" `=` ".join([comt2_1,comt2_2,comt2_3,comt2_4])
    
    comt3_1="THEREFORE ~"
    comt3_2=" `+` ".join([makeroot(pro_in_root1),makeroot(pro_in_root2)])
    comt3_3=" `+` ".join([comt1_4,comt2_4])
    comt3=" `=` ".join([comt3_1+comt3_2,comt3_3])

    comt="#".join([comt1,comt2,comt3])

    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), eqt3=addTag(eqt3), jo1=jo1, var1=addTag(var1), var2=addTag(var2),s1=addTag(s1),
    s2=addTag(s2),s3=addTag(s3),s4=addTag(s4),s5=addTag(s5))

    answer = answer.format(ans=ans)
    comment = comment.format(comt=addTag(comt))
    return stem, answer, comment

#question_3_1_1_288
def realnum311_Stem_210():
    stem = "양의 정수 {var}에 대하여 {eqt1} , {eqt2}일 때, {eqt3}를 {var}를 이용하여 나타내면? \n ① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5} \n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt} \n\n"
    
    var='k' #문제에 쓰인 첫번재 변수
    var1="a" #문제에 쓰인 두번째 변수
    var2="b" #문제에 쓰인 세번째 변수

    prime=[2,3,5,7,11]
    power=[2,3]

    prime1=random.choice(prime) #첫번째 변수 등식에 들어가는 계수
    prime2=random.choice(prime) #두번째 변수 등식에 들어가는 계수
    
    while prime1==prime2 or prime1*prime2==10:
        prime2=random.choice(prime)

    dec1_=random.choice(power)
    dec1=10**dec1_
    dec2_=random.choice(power)
    dec2=10**dec2_
    
    
    coef1=prime1*dec1
    coef2=prime2*dec2

    
    eqt1=" `=` ".join([var1,str(coef1)+var])
    eqt2=" `=` ".join([var2,str(coef2)+var])
    eqt3="".join([makeroot(var1+var2)])
    
    ###################################
    comt1="".join([makeroot(var1+var2)])
    comt2="".join([makeroot(str(coef1)+var+"`TIMES`"+str(coef2)+var)])

    deci=dec1_+dec2_
    
    li=rootout(coef1*coef2)
    
    if (deci) %2==0:
        comt3="".join([makeroot(print_power(10,deci)+" `TIMES` "+print_power(var,2)+" `TIMES` "+str(prime1*prime2))])
        comt4="".join([str(li[0]),var])
        if li[1]!=1 :
            comt4=comt4+"`"+makeroot(li[1])
    else:
        comt3="".join([makeroot(print_power(10,deci)+" `TIMES` "+print_power('k',2)+ " `TIMES` "+str(prime1*prime2))])
        comt4="".join([str(li[0]),var])
        if li[1]!=1 :
            comt4=comt4+"`"+makeroot(li[1])
   

    comt=" `=` ".join([comt1,comt2,comt3,comt4])
    
    s1="".join([makeroot(li[1]),var])
    s2="".join([str(li[0]),var])
    s3="".join([str(li[0]),var,"`",makeroot(li[1])])
    s4="".join([str(10*li[0]),var])
    s5="".join([str(10*li[0]),var,"`",makeroot(li[1])])
    
    ans="③"

    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), eqt3=addTag(eqt3), var=addTag(var), s1=addTag(s1),
    s2=addTag(s2),s3=addTag(s3),s4=addTag(s4),s5=addTag(s5))

    answer = answer.format(ans=ans)
    comment = comment.format(comt=addTag(comt))
    return stem, answer, comment

#question_3_1_1_289
def realnum311_Stem_211():
    stem = "{eqt1} , {eqt2}일 때, {eqt3}{jo1} {var1}, {var2}를 이용하여 나타내면? \n ① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5} \n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt} \n\n"

    var1="a" #문제에 쓰인 두번째 변수
    var2="b" #문제에 쓰인 세번째 변수

    prime=[2,3,5,7]

    prime1=random.choice(prime) #첫번째 변수 등식에 들어가는 계수
    prime2=random.choice(prime) #두번째 변수 등식에 들어가는 계수
    
    while prime1==prime2:
        prime2=random.choice(prime)

    if prime1>prime2:
        prime1,prime2=prime2,prime1

    sol=random.choice([3,5])
    
    number=1
    eqt1="".join([makeroot(prime1)," `=` ", var1])
    eqt2="".join([makeroot(prime2)," `=` ", var2])
    eqt3=""
    
    number=prime1+prime2

    if sol==3:
        eqt3=makeroot(number)
        if rootout(number)[0] !=1:
            eqt3=rootout_print(number)

    elif sol==5 :
        eqt3=str(number)
    

    s1="".join([makeroot(var1+var2)])
    s2="".join([makeroot(var1+" `+` "+var2)])
    s3="".join([makeroot(print_power(var1,2)+" `+` "+print_power(var2,2))])
    s4="".join([var1," `+` ",var2])
    s5="".join([print_power(var1,2)," `+` ",print_power(var2,2)])
    
    jo1=proc_jo(number%10,1)
    comt=""
    if sol==3:
        comt1=" `+` ~".join([makeroot(str(prime1)+"`+`"+str(prime2))])
        comt2_1=" `+` ".join([print_power("("+makeroot(prime1),2)+")", print_power("("+makeroot(prime2)+")",2)])
        comt2=makeroot(comt2_1)
        comt3_1=" `+` ".join([print_power(var1,2),print_power(var2,2)])
        comt3=makeroot(comt3_1)+"이므로 `"
        comt4=eqt3
        comt5="".join(makeroot(print_power(var1,2)+"`+`"+print_power(var2,2)))
        
        if rootout(number)[0] ==1:
            comt=" `=` ".join([makeroot(number),comt1,comt2,comt3])+ " `=` ".join([comt4,comt5])
        else:
            comt=" `=` ".join([rootout_print(number),makeroot(number),comt1,comt2,comt3])+ " `=` ".join([comt4,comt5])
            jo1=proc_jo(rootout(number)[1]%10,1)
    
    elif sol==5:
        comt1=" `+` ".join([str(prime1), str(prime2)])
        comt2=" `+` ".join([print_power("("+makeroot(prime1),2)+")", print_power("("+makeroot(prime2)+")",2)])
        comt3=" `+` ".join([print_power(var1,2),print_power(var2,2)])
        comt=" `=` ".join([str(number),comt1,comt2,comt3])
        jo1=proc_jo(number%10,1)


    ans=answer_dict[sol]

    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), eqt3=addTag(eqt3),jo1=jo1,var1=addTag(var1), var2=addTag(var2), s1=addTag(s1),
    s2=addTag(s2),s3=addTag(s3),s4=addTag(s4),s5=addTag(s5))

    answer = answer.format(ans=ans)
    comment = comment.format(comt=addTag(comt))
    return stem, answer, comment

#question_3_1_1_290
def realnum311_Stem_212():
    stem = "{eqt1} , {eqt2}일 때, {eqt3}{jo1} {var1}, {var2}를 사용한 식으로 나타내면 {eqt4}가 될 때 {eqt5}의 값을 구하시오\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt1} \n {comt2}이므로 \n {comt3} \n 따라서, {comt4}, {comt5}이므로 \n {comt6}"

    var1="a" #문제에 쓰인 두번째 변수
    var2="b" #문제에 쓰인 세번째 변수
    coef1="x" #구하고자 하는 첫번째 계수
    coef2="y" #구하고자 하는 두번째 계수

    prime=[2,3,5,7]
    dec=[-2,-1,1,2]
    
    prime1=random.choice(prime) #첫번째 변수 등식에 들어가는 계수
    prime2=random.choice(prime) #두번째 변수 등식에 들어가는 계수

    while prime1==prime2:
        prime2=random.choice(prime)

    if prime1>prime2:
        prime1,prime2=prime2,prime1
    
    dec1_=random.choice(dec)
    dec2_=random.choice(dec)
    
    dec1=10**dec1_
    dec2=10**dec2_

    in_root1=1
    if dec1 == 0.01 or dec1==0.1:
        in_root1=round(prime1*dec1**2,degit_of_num(dec1)*2)
    else:
        in_root1=prime1*(dec1**2)
    
    in_root2=1
    if dec2 == 0.01 or dec2==0.1:
        in_root2=round(prime2*dec2**2,degit_of_num(dec2)*2)
    else:
        in_root2=prime2*(dec2**2)

    order=random.choice([True, False])

    eqt1="".join([makeroot(prime1)," `=` ", var1])
    eqt2="".join([makeroot(prime2)," `=` ", var2])
    if order == True:
        eqt3=" `+` ".join([makeroot(in_root1),makeroot(in_root2)])
    else:
        eqt3=" `+` ".join([makeroot(in_root2),makeroot(in_root1)])
    eqt4=" `+` ".join([coef1+var1,coef2+var2])
    eqt5="".join([coef1,coef2])

    jo1=proc_jo(in_root2%10,1)
    
    dec_=(dec1_+dec2_)

    sol=""
    if(dec_<0):
        sol=makefrac(1,10**-dec_)
    else:
        sol=str(10**dec_)
    
    
    comt1=""
    comt2=""
    comt3=""
    comt1_1=makeroot(in_root1)
    comt_of_1=""
    comt1_4=""
    real_coef1=""

    if dec1_>0:
        comt1_2=makeroot(" `TIMES` ".join([print_power(10,dec1_*2),str(prime1)]))
        comt1_3=str(10**dec1_)+makeroot(prime1)
        comt1_4=str(10**dec1_)+var1
        real_coef1=str(10**dec1_)
        comt_of_1=" `=` ".join([comt1_1,comt1_2,comt1_3,comt1_4])
    else:
        comt1_2=makeroot(makefrac(prime1,10**(-dec1_*2)))
        comt1_3=makefrac(makeroot(in_root1),10**(-dec1_))
        comt1_4=makefrac(var1,10**(-dec1_))
        real_coef1=makefrac(1,10**(-dec1_))
        comt_of_1=" `=` ".join([comt1_1,comt1_2,comt1_3,comt1_4])
    
    comt2_1=makeroot(in_root2)
    comt_of_2=""
    comt2_4=""
    real_coef2=""

    if dec2_>0:
        comt2_2=makeroot(" `TIMES` ".join([print_power(10,dec2_*2),str(prime2)]))
        comt2_3=str(10**dec2_)+makeroot(prime2)
        comt2_4=str(10**dec2_)+var2
        real_coef2=str(10**dec2_)
        comt_of_2=" `=` ".join([comt2_1,comt2_2,comt2_3,comt2_4])
    else:
        comt2_2=makeroot(makefrac(prime2,10**(-dec2_*2)))
        comt2_3=makefrac(makeroot(in_root2),10**(-dec2_))
        comt2_4=makefrac(var2,10**(-dec2_))
        real_coef2=makefrac(1,10**(-dec2_))
        comt_of_2=" `=` ".join([comt2_1,comt2_2,comt2_3,comt2_4])
    
    if order==True:
        comt1=comt_of_1
        comt2=comt_of_2
        comt3=eqt3+" `=` "+comt1_4+" `+` "+ comt2_4
        
    else:
        comt1=comt_of_2
        comt2=comt_of_1
        comt3=eqt3+" `=` "+comt2_4+" `+` "+ comt1_4
        
    comt4=coef1+" `=` "+ str(real_coef1)
    comt5=coef2+" `=` " +str(real_coef2)
    comt6=coef1+coef2+ " `=` "+ sol

    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), eqt3=addTag(eqt3),eqt4=addTag(eqt4),eqt5=addTag(eqt5),jo1=jo1,var1=addTag(var1), var2=addTag(var2))

    answer = answer.format(ans=addTag(sol))
    comment = comment.format(comt1=addTag(comt1),comt2=addTag(comt2),comt3=addTag(comt3),comt4=addTag(comt4),comt5=addTag(comt5),comt6=addTag(comt6))
    return stem, answer, comment

    #question_3_1_1_291
def realnum311_Stem_213():
    stem = "다음 중 다음 중 분모를 유리화한 것으로 옳지 않은 것은?\n ① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5} \n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {ans} {comt} \n\n"

    sol=random.randrange(1,6)
    ans=answer_dict[sol]
    prime=[2,3,5,7,11]
    power=[1,2]
    
    primeList_1 = random.sample(prime, 3)

    f1=fraction(primeList_1[0],primeList_1[1]*primeList_1[2]**2)
    s1=makefrac(makeroot(f1.numer),makeroot(f1.denom))
    f1.change(f1.numer*primeList_1[1],primeList_1[1]*primeList_1[2])
    s1=s1+ " `=`" +makefrac(makeroot(f1.numer),f1.denom)

    primeList_2 = random.sample(prime, 3)
    f2=fraction(primeList_2[0],primeList_2[1]*primeList_2[2])
    s2=makefrac(makeroot(f2.numer),makeroot(f2.denom))
    f2.change(f2.numer*f2.denom,f2.denom)
    s2= s2 + " `=` "+makefrac(makeroot(f2.numer),f2.denom)

    primeList_3 = random.sample(prime, 2)
    f3=fraction(1,primeList_3[0]*primeList_3[1])
    s3=makefrac(f3.numer,makeroot(f3.denom))
    f3.change(f3.numer*f3.denom,f3.denom)
    s3=s3 + "`=`" +makefrac(makeroot(f3.numer),f3.denom)

    primeList_4 = random.sample(prime, 3)
    f4=fraction(primeList_4[0]*primeList_4[1],primeList_4[2])
    s4=s4_=makefrac(f4.numer,str(f4.denom)+makeroot(f4.denom))
    f4.change([f4.numer,f4.denom],f4.denom)
    s4=s4+ "`=`" +makefrac(str(f4.numer[0])+makeroot(f4.numer[1]),f4.denom)
    
    primeList_5 = random.sample(prime, 3)
    while primeList_5[0]*primeList_5[1]*primeList_5[2]>200:
        primeList_5 = random.sample(prime, 3)
    f5=fraction([primeList_5[1],primeList_5[0]],[primeList_5[1],primeList_5[2]])
    s5=makefrac(str(f5.numer[0])+makeroot(f5.numer[1]),makeroot(f5.denom[0])+makeroot(f5.denom[1]))
    f5.change(primeList_5[0]*primeList_5[1]*primeList_5[2],f5.denom[1])
    s5=s5+ "`=`" + makefrac(makeroot(f5.numer),f5.denom)
    
    s=[s1,s2,s3,s4,s5]
    random.shuffle(s)
    
    count=0
    for i in s:
        count=count+1
        if i ==s4:
            break
    ans=answer_dict[count]

    comt1=s4_
    comt2=makefrac(str(f4.numer[0])+makeroot(f4.numer[1]),str(f4.denom)+makeroot(f4.denom)+"`TIMES`"+makeroot(f4.denom))
    comt3=makefrac(str(f4.numer[0])+makeroot(f4.numer[1]),f4.denom**2)
    comt=" `=` ".join([comt1,comt2,comt3])

    stem = stem.format(s1=addTag(s[0]),s2=addTag(s[1]),s3=addTag(s[2]),s4=addTag(s[3]),s5=addTag(s[4]))
    answer = answer.format(ans=addTag(ans))
    comment = comment.format(ans=ans, comt=addTag(comt))
    return stem, answer, comment
    
    #question_3_1_1_292
def realnum311_Stem_214():
    stem = "{eqt1}일 때, 유리수 {var}의 값을 구하시오. \n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt1} \n {comt2} \n\n"

    prime=[2,3,5,7,11]
    prime1=random.choice(prime)
    prime2=random.choice(prime)
    var="k"
    
    while prime1==prime2 or prime1 * prime2**2 >500:
        prime2=random.choice(prime)
    
    in_root=prime1 * prime2**2
    
    ans=prime1*prime2
    eqt1=" `=` ".join([makefrac(1,makeroot(in_root)),makefrac(1,var)+makeroot(prime1)])
    comt1=" `= ".join([makefrac(1,makeroot(in_root)),makefrac(1,rootout_print(in_root)) \
        ,makefrac(makeroot(prime1),rootout_print(in_root)+"`TIMES`"+makeroot(prime1)) \
        ,makefrac(makeroot(prime1),prime1*prime2)])
    comt2="".join(["THEREFORE ~ `",var," `=` ",str(prime1*prime2)])

    stem = stem.format(eqt1=addTag(eqt1),var=addTag(var))
    answer = answer.format(ans=addTag(ans))
    comment = comment.format(comt1=addTag(comt1),comt2=addTag(comt2))
    return stem, answer, comment

#question_3_1_1_293
def realnum311_Stem_215():
    stem = "{eqt1}, {eqt2}일때, {eqt3}의 값은? \n ① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5} \n "
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt1}, {comt2}에서 \n {comt3}, {comt4} \n {comt5}\n"
    var1="A"
    var2="B"
    prime=[2,3,5,7,11]
    primeList1=random.sample(prime, 3)
   
    frac1=fraction(primeList1[0],[primeList1[1],primeList1[2]])
    eqt1_1=makefrac(frac1.numer,makeroot(frac1.denom[0]*frac1.denom[1]**2))
    eqt1_2=var1+"`"+makeroot(frac1.denom[0])
    eqt1=" =` ".join([eqt1_1,eqt1_2])

    for i in primeList1:
        if i in prime:
            prime.remove(i)
    
    primeList2=[primeList1[2],primeList1[1]]
    frac2=fraction(1,[primeList2[0],primeList2[1]])
    eqt2_1=makefrac(1,str(frac2.denom[0])+makeroot(frac2.denom[1]))
    eqt2_2=var2+"`"+makeroot(frac2.denom[1])
    eqt2=" `=` ".join([eqt2_1,eqt2_2])
    eqt3=var1+" `+` "+var2
    
    comt1_1=eqt1_1
    comt1_2=makefrac(frac1.numer,str(frac1.denom[1])+makeroot(frac1.denom[0]))
    comt1_3=makefrac(frac1.numer,frac1.denom[1]*frac1.denom[0])+makeroot(frac1.denom[0])
    comt1=" `=` ".join([comt1_1,comt1_2,comt1_3])

    comt2_1=eqt2_1
    comt2_2=makefrac(makeroot(frac2.denom[1]),frac2.denom[0]*frac2.denom[1])
    comt2=" `=` ".join([comt2_1,comt2_2])

    comt3= var1 + " `=` " + makefrac(frac1.numer,frac1.denom[1]*frac1.denom[0])
    comt4= var2 + " `=` " + makefrac(1,frac2.denom[0]*frac2.denom[1])
    frac3=Fraction(primeList1[0]+1,primeList1[1]*primeList1[2])
    comt5= "THEREFORE~ " + eqt3 + " `=` "+ makefrac_good(frac3.numerator,frac3.denominator)
    
    if frac3.denominator<20:
        if Fraction(frac3.numerator,frac3.denominator) !=1:
            s1=makefrac_good(Fraction(frac3.numerator,frac3.denominator).numerator,Fraction(frac3.numerator,frac3.denominator).denominator)
        else :
            s1="1"
        if Fraction(frac3.numerator+1,frac3.denominator) !=1:    
            s2=makefrac_good(Fraction(frac3.numerator+1,frac3.denominator).numerator,Fraction(frac3.numerator+1,frac3.denominator).denominator)
        else :
            s2="1"
        if Fraction(frac3.numerator+2,frac3.denominator) !=1: 
            s3=makefrac_good(Fraction(frac3.numerator+2,frac3.denominator).numerator,Fraction(frac3.numerator+2,frac3.denominator).denominator)
        else :
            s3="1"
        if Fraction(frac3.numerator+3,frac3.denominator) !=1:     
            s4=makefrac_good(Fraction(frac3.numerator+3,frac3.denominator).numerator,Fraction(frac3.numerator+3,frac3.denominator).denominator)
        else :
            s4="1"
        if Fraction(frac3.numerator+4,frac3.denominator) !=1:     
            s5=makefrac_good(Fraction(frac3.numerator+4,frac3.denominator).numerator,Fraction(frac3.numerator+4,frac3.denominator).denominator)
        else :
            s5="1"
        ans=answer_dict[1]
    else:
        if Fraction(frac3.numerator,frac3.denominator*2) !=1:
            s1=makefrac_good(Fraction(frac3.numerator,frac3.denominator*2).numerator,Fraction(frac3.numerator,frac3.denominator*2).denominator)
        else :
            s1="1"
        if Fraction(frac3.numerator,frac3.denominator) !=1:    
            s2=makefrac_good(Fraction(frac3.numerator,frac3.denominator).numerator,Fraction(frac3.numerator,frac3.denominator).denominator)
        else :
            s2="1"
        if Fraction(frac3.numerator*2,frac3.denominator) !=1: 
            s3=makefrac_good(Fraction(frac3.numerator*2,frac3.denominator).numerator,Fraction(frac3.numerator*2,frac3.denominator).denominator)
        else :
            s3="1"
        if Fraction(frac3.numerator*3,frac3.denominator) !=1:     
            s4=makefrac_good(Fraction(frac3.numerator*3,frac3.denominator).numerator,Fraction(frac3.numerator*3,frac3.denominator).denominator)
        else :
            s4="1"
        if Fraction(frac3.numerator*4,frac3.denominator) !=1:     
            s5=makefrac_good(Fraction(frac3.numerator*4,frac3.denominator).numerator,Fraction(frac3.numerator*4,frac3.denominator).denominator)
        else :
            s5="1"
        ans=answer_dict[2]

    stem = stem.format(eqt1=addTag(eqt1), eqt2=addTag(eqt2), eqt3=addTag(eqt3), s1=addTag(s1),s2=addTag(s2),s3=addTag(s3),s4=addTag(s4),s5=addTag(s5))
    answer = answer.format(ans=addTag(ans))
    comment = comment.format(comt1=addTag(comt1),comt2=addTag(comt2),comt3=addTag(comt3),comt4=addTag(comt4),comt5=addTag(comt5))
    
    return stem, answer, comment


    #question_3_1_1_294
def realnum311_Stem_216():
    stem = "다음 수를 크기가 작은 것부터 차례대로 나열할 때, 세 번째에 오는 수는?\n $$표$$ {sel} $$/표$$ \n ① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt1}, {comt2},\n {comt3}, {comt4}이므로\n {comt5}\n 따라서 세번째에 오는 수는 {comt6}이다."

    prime=[2,3,5,7,11]
    primeList=random.sample(prime, 2)
    prime1=primeList[0]
    prime2=primeList[1]

    if prime1>prime2:
        prime1,prime2=prime2,prime1
    
    s1=makefrac(prime1,makeroot(prime2))
    s2=makefrac(prime1,prime2)
    s3=makefrac(makeroot(prime1),makeroot(prime2))
    s4=makefrac(makeroot(prime1),prime2)
    s5=makeroot(prime2)
    sel=" `,` ".join([s1,s2,s3,s4,s5])

    comt1_1=makefrac(prime1,makeroot(prime2))
    comt1_2=makefrac(str(prime1)+makeroot(prime2),prime2)
    comt1_3=makefrac(makeroot((prime1**2)*prime2),prime2)
    comt1=" `=` ".join([comt1_1,comt1_2,comt1_3])

    comt2_1=makefrac(prime1,prime2)
    comt2_2=makefrac(makeroot(prime1**2),prime2)
    comt2=" `=` ".join([comt2_1,comt2_2])

    comt3_1=makefrac(makeroot(prime1),makeroot(prime2))
    comt3_2=makefrac(makeroot(prime1*prime2),prime2)
    comt3=" `=` ".join([comt3_1,comt3_2])

    comt4_1=makeroot(prime2)
    comt4_2=makefrac(str(prime2)+makeroot(prime2),prime2)
    comt4_3=makefrac(makeroot(prime2**3),prime2)
    comt4=" `=` ".join([comt4_1,comt4_2,comt4_3])

    comt5= " &lt; ".join([s4,s2,s3,s1,s5])
    comt6=s3
    ans=answer_dict[3]

    stem = stem.format(sel=addTag(sel), s1=addTag(s1), s2=addTag(s2), s3=addTag(s3), s4=addTag(s4), s5=addTag(s5))
    answer = answer.format(ans=addTag(ans))
    comment = comment.format(comt1=addTag(comt1),comt2=addTag(comt2),comt3=addTag(comt3),comt4=addTag(comt4),comt5=addTag(comt5),comt6=addTag(comt6))
    
    return stem, answer, comment

#question_3_1_1_295
def realnum311_Stem_217():
    stem = "{eqt1}, {eqt2}일 때, 옳은 것을 보기에서 모두 고른 것은? \n $$표$$ ㈀ {L1}  ㈁ {L2} \n ㈂ {L3}  ㈃ {L4} $$/표$$ \n ① ㈀, ㈂   ② ㈀, ㈃   ③ ㈁, ㈃   ④ ㈀, ㈁, ㈃   ⑤ ㈀, ㈂, ㈃ \n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n ㈂ {comt}\n 이상에서 옳은 것은 ㈀, ㈁, ㈃이다.\n\n"

    var1="x"
    var2="y"
    eqt1=var1+"&gt; 0"
    eqt2=var2+"&gt; 0"
    L1=" `=`".join([makefrac(var2,makeroot(var1)),makefrac(var2+"`"+makeroot(var1),var1)])
    L2=" `=`".join([makefrac(makeroot(var2),makeroot(var1)),makefrac(makeroot(var1+var2),var1)])
    L3=" `=`".join([makeroot(makefrac(var1,var2)),makefrac(var1+"`"+makeroot(var2),var2)])
    L4=" `=`".join([makefrac(makeroot(var1),"k `"+makeroot(var2)),makefrac(makeroot(var1+var2),"k`"+var2) +"(k != 0)"])
    L5=" `=`".join([makefrac(makeroot(var1),makeroot(print_power("("+"k"+var2+")",2))),makefrac(makeroot(var1),"-k"+var2)+"(k &lt; 0)"])
    L6=" `=`".join([makefrac(makeroot(print_power("("+"k `"+var1+")",2)),makeroot(var2)),makefrac("k `"+"`"+var1+"`"+makeroot(var2),var2)+"(k &lt; 0)"])
    L7=" `=`".join([makefrac(makeroot(print_power("("+"k `"+var1+")",2)),makeroot(print_power("("+"l `"+var2+")",2))),makefrac("k `"+var1,"l `"+var2)+"(k &lt; 0, ` l &lt; 0)"])

    List1_=[L1,L2,L4,L5,L7]
    List2_=[L3,L6]
    List1 = random.sample(List1_, 3)
    List2 = random.sample(List2_, 1)
    List=[List1[0],List1[1],List2[0],List1[2]]

    ans=answer_dict[4]

    comt1_1=makeroot(makefrac(var1,var2))
    comt1_2=makefrac(makeroot(var1),makeroot(var2))
    comt1_3=makefrac(makeroot(var1)+makeroot(var2),makeroot(var2)+makeroot(var2))
    comt1_4=makefrac(makeroot(var1+var2),var2)
    comt1=" `=` ".join([comt1_1,comt1_2,comt1_3,comt1_4])

    comt2_1=makefrac(makeroot(print_power("k `"+var1,2)),makeroot(var2))
    comt2_2=makefrac("-k `"+var1,makeroot(var2))
    comt2_3=makefrac("-k `"+var1+"`"+makeroot(var2),var2)
    comt2=" `=` ".join([comt2_1,comt2_2,comt2_3])

    if List2[0]==L3:
        comt=comt1
        L3_=L3
    else:
        comt=comt2
        L3_=L6

    stem = stem.format(eqt1=addTag(eqt1),eqt2=addTag(eqt2), L1=addTag(List[0]), L2=addTag(List[1]), L3=addTag(List[2]), L4=addTag(List[3]))
    answer = answer.format(ans=addTag(ans))
    comment = comment.format(comt=addTag(comt))
    
    return stem, answer, comment

#question_3_1_1_296
def realnum311_Stem_218():
    stem = "{eqt1}일 때, {eqt2}에 대하여 {eqt3}의 값은? (단, {var1}와 {var2}는 서로소인 자연수, {var3}는 유리수이다.)\n ① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt1}\n 따라서  {comt2}이므로 {comt3}\n\n"

    var1="a"
    var2="b"
    var3="c"
    prime=[2,3,5,7,11]
    primeList=random.sample(prime, 4)
    primeList.sort()

    eqt1_1=makeroot(makefrac(primeList[0]**2*primeList[1],primeList[2]**2*primeList[3]))
    eqt1_2=makefrac(var2+"`"+makeroot(primeList[1]),var1+"`"+makeroot(primeList[3]))
    eqt1_3=var3+"`"+makeroot(primeList[1]*primeList[3])
    eqt1="`=`".join([eqt1_1,eqt1_2,eqt1_3])
    eqt2=",`".join([var1,var2,var3])
    eqt3=var1+var2+var3

    comt1_1=makeroot(makefrac(primeList[0]**2*primeList[1],primeList[2]**2*primeList[3]))
    comt1_2=makefrac(makeroot(primeList[0]**2*primeList[1]),makeroot(primeList[2]**2*primeList[3]))
    comt1_3=makefrac(str(primeList[0])+makeroot(primeList[1]),str(primeList[2])+makeroot(primeList[3]))
    comt1_4=makefrac(str(primeList[0])+makeroot(primeList[1])+" `TIMES`"+makeroot(primeList[3]),str(primeList[2])+makeroot(primeList[3])+" `TIMES`"+makeroot(primeList[3]))
    comt1_5=makefrac(str(primeList[0])+makeroot(primeList[1]*primeList[3]),primeList[2]*primeList[3])
    comt1="`=`".join([comt1_1,comt1_2,comt1_3,comt1_4,comt1_5])

    frac=Fraction(primeList[0],primeList[2]*primeList[3])
    if frac.numerator!=primeList[0]:
        comt1=comt1+"`=`"+makefrac(str(frac.numerator)+makeroot(primeList[0]),frac.denominator)

    comt2_1= var1+ "`=`" +str(primeList[2])
    comt2_2= var2+ "`=`" +str(primeList[0])
    comt2_3= var3+ "`=`" +makefrac(frac.numerator,frac.denominator)
    comt2=",``".join([comt2_1,comt2_2,comt2_3])
    
    frac2=Fraction(primeList[2]*primeList[0]*frac.numerator ,frac.denominator)

    comt3=var1+var2+var3 +"`=`"+ makefrac(frac2.numerator,frac2.denominator)
    if random.choice([True,False]):
        s1= makefrac_good(Fraction(frac2.numerator,frac2.denominator*3).numerator,Fraction(frac2.numerator,frac2.denominator*3).denominator)
        s2= makefrac_good(Fraction(frac2.numerator,frac2.denominator*2).numerator,Fraction(frac2.numerator,frac2.denominator*2).denominator)
        s3= makefrac_good(frac2.numerator,frac2.denominator)
        s4= makefrac_good(Fraction(frac2.numerator*2,frac2.denominator).numerator,Fraction(frac2.numerator*2,frac2.denominator).denominator)
        s5= makefrac_good(Fraction(frac2.numerator*3,frac2.denominator).numerator,Fraction(frac2.numerator*3,frac2.denominator).denominator)
        ans=answer_dict[3]
    else:
        s1= makefrac_good(Fraction(frac2.numerator-1,frac2.denominator).numerator,Fraction(frac2.numerator-1,frac2.denominator).denominator)
        s2= makefrac_good(Fraction(frac2.numerator,frac2.denominator).numerator,Fraction(frac2.numerator,frac2.denominator).denominator)
        s3= makefrac_good(Fraction(frac2.numerator+1,frac2.denominator).numerator,Fraction(frac2.numerator+1,frac2.denominator).denominator)
        s4= makefrac_good(Fraction(frac2.numerator+2,frac2.denominator).numerator,Fraction(frac2.numerator+2,frac2.denominator).denominator)
        s5= makefrac_good(Fraction(frac2.numerator+3,frac2.denominator).numerator,Fraction(frac2.numerator+3,frac2.denominator).denominator)
        ans=answer_dict[2]

    stem = stem.format(eqt1=addTag(eqt1),eqt2=addTag(eqt2), eqt3=addTag(eqt3), var1=addTag(var1),var2=addTag(var2),var3=addTag(var3),s1=addTag(s1),s2=addTag(s2),s3=addTag(s3),s4=addTag(s4),s5=addTag(s5))
    answer = answer.format(ans=addTag(ans))
    comment = comment.format(comt1=addTag(comt1),comt2=addTag(comt2),comt3=addTag(comt3))
    
    return stem, answer, comment

    #question_3_1_1_297
def realnum311_Stem_219():
    stem = "{eqt1}에 대하여 {eqt2}일 때, {eqt3}의 값은? (단, {var3}와 {var4}는 서로소인 자연수이다.) \n ① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt1}\n 따라서 {comt2}이므로 {comt3}\n\n"

    var1="a"
    var2="b"
    var3="p"
    var4="q"
    
    prime=[2,3,5,7,11,13]
    primeList=random.sample(prime, 2)
    primeList.sort()

    eqt1_1=" `=` ".join([var1,makeroot(primeList[0])])
    eqt1_2=" `=` ".join([var2,makeroot(primeList[1])])
    eqt1="`,`".join([eqt1_1,eqt1_2])
    eqt2=" `=` ".join([makefrac(str(primeList[1])+print_power((var1),3),var2),makefrac(var3+"`"+makeroot(primeList[0]*primeList[1]),var4)])
    eqt3=" `+` ".join([var3,var4])

    ans=answer_dict[4]
    
    comt1_1=makefrac(str(primeList[1])+print_power((var1),3),var2)
    comt1_2=makefrac(str(primeList[1])+" `TIMES` "+print_power("("+makeroot(primeList[0])+")",3),makeroot(primeList[1]))
    comt1_3=makefrac(str(primeList[1])+" `TIMES` "+rootout_print(primeList[0]**3),makeroot(primeList[1]))
    comt1_4=makefrac(str(primeList[1])+" `TIMES` "+rootout_print(primeList[0]**3)+" `TIMES` "+makeroot(primeList[1]),makeroot(primeList[1])+" `TIMES` "+makeroot(primeList[1]))
    comt1_5=str(primeList[0])+makeroot(primeList[0]*primeList[1])
    comt1= "`=`".join([comt1_1,comt1_2,comt1_3,comt1_4,comt1_5])

    comt2_1="`=`".join([var3,str(primeList[0])])
    comt2_2="`=`".join([var4,"1"])
    comt2=" `,` ".join([comt2_1,comt2_2])

    comt3="`=`".join([var3+"`+`"+var4,str(primeList[0]+1)])
    
    s1=str(primeList[0])
    s2=str(primeList[0]+1)
    s3=str(primeList[0]+2)
    s4=str(primeList[0]+3)
    s5=str(primeList[0]+4)
    
    ans=answer_dict[2]

    stem = stem.format(eqt1=addTag(eqt1),eqt2=addTag(eqt2), eqt3=addTag(eqt3), var3=addTag(var3), var4=addTag(var4), s1=addTag(s1), s2=addTag(s2), s3=addTag(s3), s4=addTag(s4), s5=addTag(s5))
    answer = answer.format(ans=addTag(ans))
    comment = comment.format(comt1=addTag(comt1),comt2=addTag(comt2),comt3=addTag(comt3))
    
    return stem, answer, comment

    #question_3_1_1_298
def realnum311_Stem_220():
    stem = "{eqt1}, {eqt2}일 때, {eqt3}{jo1} {eqt4}를 이용하여 나타내면? \n ① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(정답)\n {ans}\n"
    comment = "(해설)\n {comt1}\n {comt2}\n {comt3}\n\n"

    var1="a"
    var2="b"
    
    prime=[2,3,5,7,11]
    primeList=random.sample(prime, 3)
    primeList.sort(reverse=True)
    
    for i in primeList:
        if i in prime:
            prime.remove(i)
            
    primeList[1]=primeList[1]*primeList[2]
    if random.choice([True,False]):
        primeList[0],primeList[1]=primeList[1],primeList[0]

    eqt1=" `=` ".join([makeroot(primeList[0]),var1])
    eqt2=" `=` ".join([makeroot(primeList[1]),var2])

    coef=random.choice(prime)
    coef1=coef*10
    eqt3_1=makeroot(coef1**2*primeList[0])
    coef2=coef*10**(-2)
    eqt3_2=makeroot(round(coef2**2*primeList[1],4))
    eqt3="`+`".join([eqt3_1,eqt3_2])
    jo1=proc_jo(coef**2*primeList[1]%10,1)

    eqt4="`,`".join([var1,var2])


    ans=answer_dict[4]
    
    comt1_1=eqt3_1
    comt1_2=makeroot(str(coef1**2)+"`TIMES`"+str(primeList[0]))
    comt1_3=str(coef1)+makeroot(primeList[0])
    comt1_4=str(coef1)+var1
    comt1="`=`".join([comt1_1,comt1_2,comt1_3,comt1_4])

    comt2_1=eqt3_2
    comt2_2=makeroot(makefrac(coef**2*primeList[1],10**4))
    comt2_3=makefrac(str(coef)+makeroot(primeList[1]),10**2)
    frac=Fraction(coef,100)
    if coef!=frac.numerator:
        if frac.numerator !=1:
            comt2_4=makefrac(str(frac.numerator)+makeroot(primeList[1]),frac.denominator)
            c2=comt2_5=makefrac(str(frac.numerator),frac.denominator)+var2
        else:
            comt2_4=makefrac(makeroot(frac.numerator**2*primeList[1]),frac.denominator)
            c2=comt2_5=makefrac(1,frac.denominator)+var2
        
        comt2="`=`".join([comt2_1,comt2_2,comt2_3,comt2_4,comt2_5])
    else: 
        c2=comt2_4=makefrac(str(frac.numerator),frac.denominator)+var2
        comt2="`=`".join([comt2_1,comt2_2,comt2_3,comt2_4])
    
    comt3_1="THEREFORE~"
    comt3_2=eqt3
    comt3_3=comt1_4 +"`+`"+c2
    comt3="`=`".join([comt3_1+comt3_2,comt3_3])
    
    s1=comt1_4 +"`+`"+makefrac(Fraction(frac.numerator,frac.denominator*coef).numerator,Fraction(frac.numerator,frac.denominator*coef).denominator)+var2
    s2=comt1_4 +"`+`"+c2
    s3=comt1_4 +"`+`"+makefrac(Fraction(frac.numerator*coef,frac.denominator).numerator,Fraction(frac.numerator*coef,frac.denominator).denominator)+var2
    s4=str(coef1+coef)+var1 +"`+`"+makefrac(Fraction(frac.numerator,frac.denominator*coef).numerator,Fraction(frac.numerator,frac.denominator*coef).denominator)+var2
    s5=str(coef1+coef)+var1 +"`+`"+c2

    ans=answer_dict[2]

    stem = stem.format(eqt1=addTag(eqt1),eqt2=addTag(eqt2), eqt3=addTag(eqt3), eqt4=addTag(eqt4), jo1=addTag(jo1), var1=addTag(var1), var2=addTag(var2), s1=addTag(s1), s2=addTag(s2), s3=addTag(s3), s4=addTag(s4), s5=addTag(s5))
    answer = answer.format(ans=addTag(ans))
    comment = comment.format(comt1=addTag(comt1),comt2=addTag(comt2),comt3=addTag(comt3))
    
    return stem, answer, comment

# 3-1-1-299
def realnum311_Stem_221():
    stem = "$$수식$$x = sqrt {x}$$/수식$$, $$수식$$y = sqrt {y}$$/수식$$일 때, " \
           "다음 중 옳지 않은 것은?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "① $$수식$${s1}$$/수식$$\n" \
              "② $$수식$${s2}$$/수식$$\n" \
              "③ $$수식$${s3}$$/수식$$\n" \
              "④ $$수식$${s4}$$/수식$$\n" \
              "⑤ $$수식$${s5}$$/수식$$\n\n"

    while True:
        y = [2, 4, 5][np.random.randint(0, 3)]
        x = np.random.randint(2, 6)
        if x != y and GCD(x, y) == 1:
            break

    # 순서 : 옳은 보기, 틀린 보기, 해설
    cs = [['sqrt {num} = x^2 y'.format(num=(x*x*y)), 'sqrt {num} = x y^2'.format(num=(x*x*y)),
           'sqrt {num} = sqrt {{ {x} ^2 TIMES {y} }} =  ( sqrt {x}  ) ^2 TIMES sqrt {y} = x^2 y'.format(num=(x*x*y), x=x, y=y)],
          ['sqrt {{ {y} OVER {x} }} = y OVER x'.format(x=x, y=y), 'sqrt {{ {y} OVER {x} }} = x OVER y'.format(x=x, y=y),
           'sqrt {{ {y} OVER {x} }} = sqrt {y} OVER sqrt {x} = y OVER x'.format(x=x, y=y)],
          ['sqrt {num} = 10xy'.format(num=(x*y*100)), 'sqrt {num} = 100xy'.format(num=(x*y*100)),
           'sqrt {num} = sqrt {{ {x} TIMES {y} TIMES 10^2 }} = sqrt {x} TIMES sqrt {y} TIMES 10 = 10xy'.format(num=(x*y*100), x=x, y=y)],
          ['sqrt {num} = 1 OVER 10 y'.format(num=(y/100)), 'sqrt {num} = 1 OVER 10xy'.format(num=(y/100)),
           'sqrt {num} = sqrt {{ {y} OVER 100 }} = sqrt {y} OVER 10 = 1 OVER 10 y'.format(num=(y/100), y=y)],
          ['sqrt {{ {num} OVER {y} }} = x^3 OVER y'.format(num=(x*x*x), y=y), 'sqrt {{ {num} OVER {y} }} = x^2 OVER y'.format(num=(x*x*x), y=y),
           'sqrt {{ {num} OVER {y} }} = sqrt {num} OVER sqrt {y} = {{  ( sqrt {x}  ) ^3 }} OVER sqrt {y} = x^3 OVER y'.format(num=(x*x*x), x=x, y=y)]]

    np.random.shuffle(cs)
    c = []
    ss = []
    s = np.random.randint(0, 5)
    for i in range(0, len(cs)):
        if i == s:  # 틀린 보기 넣기
            c.append(cs[i][1])
        else:  # 옳은 보기 넣기
            c.append(cs[i][0])
        ss.append(cs[i][2])

    c1, c2, c3, c4, c5 = c
    s1, s2, s3, s4, s5 = ss
    s = answer_dict[s]

    stem = stem.format(x=x, y=y, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)

    return stem, answer, comment





# 3-1-1-300
def realnum311_Stem_222():
    stem = "$$수식$$sqrt {p1} OVER {{ {p2} sqrt k }} = {{ {p3} sqrt {p4} }} OVER {p5}$$/수식$$을 " \
           "만족시키는 자연수 $$수식$$k$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt {p1} OVER {{ {p2} sqrt k }} = {{ {p6} sqrt {p7} }} OVER {{ {p2} sqrt k }} = " \
              "{{ {p8} sqrt {p7} }} OVER sqrt k = {{ {p8} sqrt {{ {p7} k }} }} OVER k$$/수식$$\n" \
              "따라서 $$수식$${{ {p8} sqrt {{ {p7} k }} }} OVER k = {{ {p3} sqrt {p4} }} OVER {p5}$$/수식$$이므로\n" \
              "$$수식$$k = {k}$$/수식$$\n\n"

    while True:
        k, p7 = random.sample([2, 3, 5, 7, 11], 2)
        p5 = k
        p4 = p7 * k
        p2 = np.random.randint(2, 6)
        p8 = np.random.randint(2, 4)
        p3 = p8
        p6 = p8 * p2
        p1 = p6 * p6 * p7
        if p1 < 200:
            break

    c = random.sample(list(range(k-5, k))+list(range(k+1, k+6)), 4)
    c.append(k)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == k:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(k=k, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8)

    return stem, answer, comment





# 3-1-1-302
def realnum311_Stem_223():
    stem = "$$수식$${p1} OVER sqrt {p2} = a sqrt {p2}$$/수식$$, " \
           "$$수식$${p3} OVER sqrt {p4} = b sqrt {p5}$$/수식$$일 때, " \
           "유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$ab$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$${p1} OVER sqrt {p2} = {{ {p1} sqrt {p2} }} OVER  {p2}$$/수식$$이므로 $$수식$$a = {p1} OVER {p2}$$/수식$$\n" \
              "$$수식$${p3} OVER sqrt {p4} = {p3} OVER sqrt {{ {p6} ^2 TIMES {p7} }} = {p3} OVER {{ {p6} sqrt {p7} }} " \
              "= {p8} OVER {{ {p9} sqrt {p7} }} = {{ {p101} sqrt {p5} }} OVER {p11}$$/수식$$이므로 " \
              "$$수식$$b = {p10} OVER {p11}$$/수식$$\n" \
              "$$수식$$THEREFORE~ ab = {p1} OVER {p2} TIMES {p10} OVER {p11} = {p12} OVER {p13}$$/수식$$\n\n"

    while True:
        p2, p7 = random.sample([2, 3, 5, 6, 7], 2)
        p1 = np.random.randint(2, 7)
        p8, p9 = random.sample(list(range(2, 7)), 2)
        p10 = p8
        p11 = p9 * p7
        gcd1011 = GCD(p10, p11)
        p10 = int(p10/gcd1011)
        p11 = int(p11/gcd1011)
        p12 = p1 * p10
        p13 = p2 * p11
        gcd1213 = GCD(p12, p13)
        p12 = int(p12/gcd1213)
        p13 = int(p13/gcd1213)
        if GCD(p1, p2) == 1 and GCD(p8, p9) == 1 and p11 != 1 and p13 != 1:
            break
    p3 = p8 * 2
    p6 = p9 * 2
    p4 = p6*p6*p7
    p5 = p7
    p101 = p10
    if p101 == 1:
        p101 = ''

    ss = '{x} OVER {y}'.format(x=p12, y=p13)
    c = [ss]
    while True:
        y = p2 * p11
        x = p1 * p10 + np.random.randint(-4, 5)
        gcdxy = GCD(x, y)
        y = int(y/gcdxy)
        x = int(x/gcdxy)
        if x > 0 and y != 1:
            c.append('{x} OVER {y}'.format(x=x, y=y))
        c = list(set(c))
        if len(c) == 5:
            break
    c.sort()
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break
    c1, c2, c3, c4, c5 = c

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p101=p101, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12, p13=p13)

    return stem, answer, comment





# 3-1-1-304
def realnum311_Stem_224():
    stem = "$$수식$${p1} sqrt {p2} TIMES  ( {p3} sqrt {p4}  ) DIV {p5} sqrt {p6}$$/수식$$을 계산하시오.\n"
    answer = "(답) $$수식$${s}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${p1} sqrt {p2} TIMES  ( {p3} sqrt {p4}  ) DIV {p5} sqrt {p6}$$/수식$$\n" \
              "$$수식$$= {p1} sqrt {p2} TIMES  ( {p3} sqrt {p4}  ) TIMES 1 OVER {{ {p5} sqrt {p6} }}$$/수식$$\n" \
              "$$수식$$= {{ {p7} sqrt {p8} }} OVER {{ {p5} sqrt {p6} }}$$/수식$$\n" \
              "$$수식$$= {{ {p9} TIMES {p10} sqrt {p11} }} OVER {{ sqrt {p6} }}$$/수식$$\n" \
              "$$수식$$= {s}$$/수식$$\n\n"

    while True:
        p7 = np.random.randint(10, 40)
        divs7 = getMyDivisors(p7)
        if len(divs7) >= 4:
            break
    while True:
        p1, p5 = random.sample(divs7, 2)
        if p1 * p5 != p7:
            break
    p3 = -int(p7/p1)
    p9 = -int(p7/p5)
    p7 = -p7

    while True:
        p10 = np.random.randint(2, 4)
        p11 = [2, 3, 5, 7][np.random.randint(0, 4)]
        p8 = p10*p10*p11
        divs8 = getMyDivisors(p8)
        if len(divs8) >= 2:
            break
    p2 = random.sample(divs8, 1)[0]
    p4 = int(p8/p2)
    p6 = p11
    s = p9 * p10

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6)
    answer = answer.format(s=s)
    comment = comment.format(s=s, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11)

    return stem, answer, comment





# 3-1-1-305
def realnum311_Stem_225():
    stem = "$$수식$${p1} sqrt {p2} TIMES  ( {p3} sqrt {p4}  ) DIV {{ sqrt {p5} }} OVER {p6}$$/수식$$을 간단히 한 것은?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$${p1} sqrt {p2} TIMES  ( {p3} sqrt {p4}  ) DIV {{ sqrt {p5} }} OVER {p6}$$/수식$$\n" \
              "$$수식$$= {p7} sqrt {p8} TIMES {p6} OVER {{ sqrt {p5} }}$$/수식$$\n" \
              "$$수식$$= {p9} TIMES {p6}$$/수식$$\n" \
              "$$수식$$= {p10}$$/수식$$\n\n"

    p7 = [4, 6, 8, 9, 10][np.random.randint(0, 5)]
    divs7 = getMyDivisors(p7)
    p1 = random.sample(divs7, 1)[0]
    p3 = -int(p7/p1)

    while True:
        a = np.random.randint(2, 4)
        p5 = [2, 3, 5, 7][np.random.randint(0, 4)]
        p8 = p5 * a * a
        divs8 = getMyDivisors(p8)
        p2 = random.sample(divs8, 1)[0]
        p4 = int(p8/p2)
        if (not isSquare(p2)) and (not isSquare(p4)):
            break
    p7 = -p7
    p9 = p7 * a
    p6 = np.random.randint(2, 8)
    p10 = p9 * p6

    c = random.sample(list(range(p10-5, p10))+list(range(p10+1, 0)), 4)
    c.append(p10)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == p10:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10)

    return stem, answer, comment





# 3-1-1-306
def realnum311_Stem_226():
    stem = "다음 중 옳지 않은 것은?\n" \
           "① $$수식$${c1}$$/수식$$\n② $$수식$${c2}$$/수식$$\n③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "① {s1}\n" \
              "② {s2}\n" \
              "③ {s3}\n" \
              "④ {s4}\n" \
              "⑤ {s5}\n\n"

    while True:
        p1, p2, p = random.sample([2, 3, 5, 7, 11], 3)
        p3 = p1 * p
        p5 = p2 * p
        p4, p7 = random.sample(list(range(2, 6)), 2)
        p6 = p7 * p7
        p8 = p1 * p7
        p9 = p2 * p4
        gcdp89 = GCD(p8, p9)
        p8 = int(p8/gcdp89)
        p9 = int(p9/gcdp89)
        if p8 != 1 and p9 != 1:
            break

    while True:
        q2, q4 = random.sample([2, 3, 5, 7, 11], 2)
        q9 = q2
        q6 = q4
        q1, q3 = [[2, 3], [3, 2]][np.random.randint(0, 2)]
        q8 = q1
        q5 = q8 * q8 * q9
        q10 = np.random.randint(1, 6)
        q7 = q3 * q10
        if q8 != q4:
            break

    rr2, rr3, rr4 = random.sample([2, 3, 5], 3)
    rr1 = np.random.randint(2, 4)
    r4 = rr1 * rr1 * rr2
    r8 = rr2
    r2 = rr3 * rr4
    r6 = rr2 * rr3
    r3 = np.random.randint(2, 6)
    r5 = r3
    r1 = rr1
    r7 = r3 * rr1
    r9 = rr3
    r10 = rr4

    x3, x5 = random.sample([2, 3, 5], 2)
    x2 = x3 * x5
    x4 = np.random.randint(2, 5)
    x6 = x4
    x1 = x4 * x4 * x5

    y2, y8 = random.sample([2, 3, 5, 7], 2)
    y6 = y2 * y8
    y5, y10 = random.sample([2, 3, 5, 7], 2)
    y3 = y5 * y10
    y7 = np.random.randint(2, 5)
    y4 = y7 * y7 * y8
    y9 = np.random.randint(2, 6)
    y1 = y9 * y7

    # 옳은 보기, 틀린 보기, 해설 순
    cs = [['$$수식$$sqrt {{ {p1} OVER {p2} }} TIMES {{ sqrt {p3} }} OVER {p4} DIV sqrt {{ {p5} OVER {p6} }} '
           '= {p8} OVER {p9}$$/수식$$'.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p8=p8, p9=p9),
           '$$수식$$sqrt {{ {p1} OVER {p2} }} TIMES {{ sqrt {p3} }} OVER {p4} DIV sqrt {{ {p5} OVER {p6} }} '
           '= {p8} OVER {p9}$$/수식$$'.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p8=p9, p9=p8),
           '$$수식$$sqrt {{ {p1} OVER {p2} }} TIMES {{ sqrt {p3} }} OVER {p4} DIV sqrt {{ {p5} OVER {p6} }}$$/수식$$\n'
           '$$수식$$= {{ sqrt {p1} }} OVER {{ sqrt {p2} }} TIMES {{ sqrt {p3} }} OVER {p4} TIMES {p7} OVER {{ sqrt {p5} }} '
           '= {p8} OVER {p9}$$/수식$$'.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9)],
          ['$$수식$${{ {q1} sqrt {q2} }} OVER {q3} TIMES sqrt {{ {q4} OVER {q5} }} DIV {{ sqrt {q6} }} OVER {q7} '
           '= {q10}$$/수식$$'.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q10=q10),
           '$$수식$${{ {q1} sqrt {q2} }} OVER {q3} TIMES sqrt {{ {q4} OVER {q5} }} DIV {{ sqrt {q6} }} OVER {q7} '
           '= {q10}$$/수식$$'.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q10=(q10+1)),
           '$$수식$${{ {q1} sqrt {q2} }} OVER {q3} TIMES sqrt {{ {q4} OVER {q5} }} DIV {{ sqrt {q6} }} OVER {q7}$$/수식$$\n'
           '$$수식$$= {{ {q1} sqrt {q2} }} OVER {q3} TIMES sqrt {q4} OVER {{ {q8} sqrt {q9} }} TIMES {q7} OVER {{ sqrt {q6} }} '
           '= {q10}$$/수식$$'.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9, q10=q10)],
          ['$$수식$${r1} sqrt {r2} DIV {r3} sqrt {r4} TIMES {r5} sqrt {r6}'
           '= {r9} sqrt {r10}$$/수식$$'.format(r1=r1, r2=r2, r3=r3, r4=r4, r5=r5, r6=r6, r9=r9, r10=r10),
           '$$수식$${r1} sqrt {r2} DIV {r3} sqrt {r4} TIMES {r5} sqrt {r6}'
           '= {r9} sqrt {r10}$$/수식$$'.format(r1=r1, r2=r2, r3=r3, r4=r4, r5=r5, r6=r6, r9=(r9+1), r10=r10),
           '$$수식$${r1} sqrt {r2} DIV {r3} sqrt {r4} TIMES {r5} sqrt {r6}$$/수식$$\n'
           '$$수식$$= {r1} sqrt {r2} TIMES 1 OVER {{ {r7} sqrt {r8} }} TIMES {r5} sqrt {r6} '
           '= {r9} sqrt {r10}$$/수식$$'.format(r1=r1, r2=r2, r3=r3, r4=r4, r5=r5, r6=r6, r7=r7, r8=r8, r9=r9, r10=r10)],
          ['$$수식$$sqrt {x1} DIV sqrt {x2} TIMES sqrt {x3} = {x6}$$/수식$$'.format(x1=x1, x2=x2, x3=x3, x6=x6),
           '$$수식$$sqrt {x1} DIV sqrt {x2} TIMES sqrt {x3} = {x6}$$/수식$$'.format(x1=x1, x2=x2, x3=x3, x6=(x6+1)),
           '$$수식$$sqrt {x1} DIV sqrt {x2} TIMES sqrt {x3} = {x4} sqrt {x5} TIMES 1 OVER {{ sqrt {x2} }} TIMES sqrt {x3} '
           '= {x6}$$/수식$$'.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6)],
          ['$$수식$${y1} OVER {{ sqrt {y2} }} TIMES {{ sqrt {y3} }} OVER {{ sqrt {y4} }} DIV {{ sqrt {y5} }} OVER {{ sqrt {y6} }} '
           '= {y9} sqrt {y10}$$/수식$$'.format(y1=y1, y2=y2, y3=y3, y4=y4, y5=y5, y6=y6, y9=y9, y10=y10),
           '$$수식$${y1} OVER {{ sqrt {y2} }} TIMES {{ sqrt {y3} }} OVER {{ sqrt {y4} }} DIV {{ sqrt {y5} }} OVER {{ sqrt {y6} }} '
           '= {y9} sqrt {y10}$$/수식$$'.format(y1=y1, y2=y2, y3=y3, y4=y4, y5=y5, y6=y6, y9=(y9+1), y10=y10),
           '$$수식$${y1} OVER {{ sqrt {y2} }} TIMES {{ sqrt {y3} }} OVER {{ sqrt {y4} }} DIV {{ sqrt {y5} }} OVER {{ sqrt {y6} }}$$/수식$$\n'
           '$$수식$$= {y1} OVER {{ sqrt {y2} }} TIMES {{ sqrt {y3} }} OVER {{ {y7} sqrt {y8} }} TIMES {{ sqrt {y6} }} OVER {{ sqrt {y5} }} '
           '= {y9} sqrt {y10}$$/수식$$'.format(y1=y1, y2=y2, y3=y3, y4=y4, y5=y5, y6=y6, y7=y7, y8=y8, y9=y9, y10=y10)]]

    np.random.shuffle(cs)
    ans = np.random.randint(0, 5)
    s = answer_dict[ans]
    c = []
    ss = []
    for i in range(0, len(cs)):
        if i == ans:
            c.append(cs[i][1])
        else:
            c.append(cs[i][0])
        ss.append(cs[i][2])
    c1, c2, c3, c4, c5 = c
    s1, s2, s3, s4, s5 = ss

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)

    return stem, answer, comment





# 3-1-1-307
def realnum311_Stem_227():
    stem = "$$수식$$sqrt {p1} TIMES sqrt {p2} DIV sqrt {p3} = a sqrt {p4}$$/수식$$를 만족시키는 유리수 $$수식$$a$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt {p1} TIMES sqrt {p2} DIV sqrt {p3} = a sqrt {p4}$$/수식$$\n" \
              "$$수식$$= {p5} sqrt {p6} TIMES {p7} sqrt {p8} TIMES 1 OVER {{ {p9} sqrt {p10} }} = {p11} sqrt {p4}$$/수식$$\n" \
              "$$수식$$THEREFORE~ a = {a}$$/수식$$\n\n"

    p6, p8 = random.sample([2, 3, 5, 7], 2)
    p10, p4 = [[p6, p8], [p8, p6]][np.random.randint(0, 2)]
    while True:
        p5, p7 = random.sample(list(range(2, 6)), 2)
        p9 = np.random.randint(2, 7)
        p1 = p5*p5*p6
        p2 = p7*p7*p8
        p3 = p9*p9*p10
        if (p5*p7) % p9 == 0 and p1 < 200 and p2 < 200 and p3 < 200 and p1 != p2 and p1 != p3 and p2 != p3:
            break
    a = int(p5*p7/p9)
    p11 = a
    if p11 == 1:
        p11 = ''

    c = random.sample(list(range(0, a))+list(range(a+1, a+10)), 4)
    c.append(a)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == a:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(a=a, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11)

    return stem, answer, comment





# 3-1-1-308
def realnum311_Stem_228():
    stem = "$$수식$${p1} OVER {{ sqrt {p2} }} TIMES {p3} OVER {{ sqrt {p4} }} DIV sqrt {{ {p5} OVER {p6} }} = a sqrt {p7}$$/수식$$" \
           "을 만족시키는 유리수 $$수식$$a$$/수식$$에 대하여 $$수식$${mul} a$$/수식$$의 값을 구하시오.\n"
    answer = "(답) $$수식$${s}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${p1} OVER {{ sqrt {p2} }} TIMES {p3} OVER {{ sqrt {p4} }} DIV sqrt {{ {p5} OVER {p6} }} " \
              "= {p1} OVER {{ sqrt {p2} }} TIMES {p3} OVER {{ sqrt {p4} }} DIV {{ sqrt {p5} }} OVER {{ sqrt {p6} }}$$/수식$$\n" \
              "     \t$$수식$$= {p1} OVER {{ sqrt {p2} }} TIMES {p3} OVER {{ sqrt {p4} }} TIMES {{ {p8} sqrt {p9} }} OVER {p10}$$/수식$$\n" \
              "     \t$$수식$$= {p11} OVER {{ {p12} sqrt {p13} }}$$/수식$$\n" \
              "     \t$$수식$$= {{ {p11} TIMES sqrt {p13} }} OVER {{ {p12} sqrt {p13} TIMES sqrt {p13} }}$$/수식$$\n" \
              "     \t$$수식$$= {{ {p14} sqrt {p13} }} OVER {p15} = a sqrt {p7}$$/수식$$\n" \
              "따라서 $$수식$$a = {p14} OVER {p15}$$/수식$$이므로 $$수식$${mul} a = {s}$$/수식$$\n\n"

    while True:
        p2, p4 = random.sample([2, 3, 5, 7], 2)
        p9, p13 = [[p2, p4], [p4, p2]][np.random.randint(0, 2)]
        p7 = p13
        p8 = np.random.randint(2, 4)
        p10 = np.random.randint(2, 6)
        if GCD(p8, p10) != 1:
            continue
        p5 = p10*p10
        p6 = p8*p8*p9
        if GCD(p5, p6) != 1:
            continue
        p1, p3 = random.sample(list(range(2, 6)), 2)
        p11 = p1 * p3 * p8
        p12 = p10
        gcd1112 = GCD(p11, p12)
        p11 = int(p11/gcd1112)
        p12 = int(p12/gcd1112)
        if p12 == 1:
            continue
        p14 = p11
        p15 = p12 * p13
        gcd1415 = GCD(p14, p15)
        p14 = int(p14/gcd1415)
        p15 = int(p15/gcd1415)
        if p15 != 1:
            break
    mul = p15 * np.random.randint(1, 3)
    s = int(p14/p15*mul)

    stem = stem.format(mul=mul, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7)
    answer = answer.format(s=s)
    comment = comment.format(mul=mul, s=s, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12, p13=p13, p14=p14, p15=p15)

    return stem, answer, comment





# 3-1-1-309
def realnum311_Stem_229():
    stem = "$$수식$${{ sqrt {p1} }} OVER {p2} TIMES sqrt {p3} DIV  ( - {p4} sqrt {p5}  )$$/수식$$를 계산하면?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$${{ sqrt {p1} }} OVER {p2} TIMES sqrt {p3} DIV  ( - {p4} sqrt {p5}  )$$/수식$$\n" \
              "$$수식$$= {{ {p6} sqrt {p7} }} OVER {p2} TIMES {p8} sqrt {p9} TIMES  ( - 1 OVER {{ {p4} sqrt {p5} }}  )$$/수식$$\n" \
              "$$수식$$= - sqrt {p10}$$/수식$$\n\n"

    while True:
        p7, p9 = random.sample([2, 3, 5, 7], 2)
        p5, p10 = [[p7, p9], [p9, p7]][np.random.randint(0, 2)]
        while True:
            num = np.random.randint(10, 40)
            divs = getMyDivisors(num)
            if len(divs) >= 4:
                break
        p6, p2 = random.sample(divs, 2)
        if p6 * p2 == num or GCD(p6, p2) != 1:
            continue
        p8 = int(num/p6)
        p4 = int(num/p2)
        p1 = p6 * p6 * p7
        p3 = p8 * p8 * p9
        if p1 < 200 and p3 < 200:
            break

    ss = '- sqrt {p10}'.format(p10=p10)
    c = []
    while True:
        x, z = random.sample(list(range(2, 6)), 2)
        if GCD(x, z) != 1:
            continue
        c.append('- {{ {x} sqrt {y} }} OVER {z}'.format(x=x, y=p10, z=z))
        c = list(set(c))
        if len(c) == 4:
            break
    c.append(ss)
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(0, len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10)

    return stem, answer, comment





# 3-1-1-310
def realnum311_Stem_230():
    stem = "양의 유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 다음 식의 값은?\n" \
           "$$표$$$$수식$$sqrt {{ {p1} a }} OVER sqrt {{ {p2} b }} TIMES  sqrt {{ {p3} b }} OVER sqrt {{ {p4} a }} " \
           "DIV sqrt {{ {{ {p5} b }} OVER {{ {p6} a }} }} DIV sqrt {{ {{ {p7} a }} OVER {{ {p8} b }} }}$$/수식$$$$/표$$\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$$ sqrt {{ {p1} a }} OVER sqrt {{ {p2} b }} TIMES sqrt {{ {p3} b }} OVER sqrt {{ {p4} a }} " \
              "DIV sqrt {{ {{ {p5} b }} OVER {{ {p6} a }} }} DIV sqrt {{ {{ {p7} a }} OVER {{ {p8} b }} }}$$/수식$$\n" \
              "$$수식$$= sqrt {{ {p1} a }} OVER sqrt {{ {p2} b }} TIMES sqrt {{ {p3} b }} OVER {{ {p9} sqrt a }} " \
              "TIMES sqrt {{ {p6} a }} OVER sqrt {{ {p5} b }} TIMES sqrt {{ {p8} b }} OVER sqrt {{ {p7} a }}$$/수식$$\n" \
              "$$수식$$= sqrt {p10} OVER {{ {p11} sqrt {p12} }} = sqrt {p13} OVER {p14}$$/수식$$\n\n"

    p1, p2 = random.sample([2, 3, 5, 7], 2)
    p3, p8 = [['', p1], [p1, '']][np.random.randint(0, 2)]
    p9 = p1
    p4 = p9 * p9
    p7 = p2
    p11 = p2
    while True:
        p5, p6 = random.sample([2, 3, 5, 6, 7, 11], 2)
        if GCD(p5, p6) == 1:
            break
    p10 = p6
    p12 = p5
    p13 = p10 * p12
    p14 = p11 * p12

    ss = '{{ sqrt {x} }} OVER {y}'.format(x=p13, y=p14)
    c = [ss]
    c.append('{{ sqrt {x} }} OVER {y}'.format(x=p10, y=p11))
    c.append('{{ sqrt {x} }} OVER {y}'.format(x=p12, y=p14))
    c.append('{{ sqrt {x} }} OVER {y}'.format(x=p13, y=p11))
    c.append('{{ sqrt {x} }} OVER {y}'.format(x=p10, y=p12))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12, p13=p13, p14=p14)

    return stem, answer, comment





# 3-1-1-311
def realnum311_Stem_231():
    stem = "다음과 같이 화살표 위에 쓰여진 계산을 차례대로 한 결과가 $$수식$${p4}$$/수식$$일 때, ㈎에 알맞은 수는?\n" \
           "$$표$$$$수식$$TIMES {p1} sqrt {p2}$$/수식$$     $$수식$$DIV sqrt {p3}$$/수식$$\n" \
           "$$수식$${box1}$$/수식$$ ──→ $$수식$${box2}$$/수식$$ ──→ $$수식$${p4}$$/수식$$$$/표$$\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$${p4} TIMES sqrt {p3} DIV {p1} sqrt {p2} " \
              "= {p4} TIMES {p5} sqrt {p6} TIMES 1 OVER {{ {p1} sqrt {p2} }}$$/수식$$\n" \
              "$$수식$$= {{ {p7} sqrt {p6} }} OVER {{ sqrt {p2} }} = {p8} sqrt {p9}$$/수식$$\n\n"

    box1 = 'box{````㈎````}'
    box2 = 'box{````````````}'

    while True:
        p2, p6 = random.sample([2, 3, 5, 7], 2)
        while True:
            num = np.random.randint(10, 30)
            divs = getMyDivisors(num)
            if len(divs) >= 4:
                break
        p1, p4 = random.sample(divs, 2)
        if p1 * p4 == num:
            continue
        p5 = int(num / p4)
        p7 = int(num / p1)
        p3 = p5 * p5 * p6
        if p7 % p2 == 0 and p3 < 200:
            break
    p8 = int(p7/p2)
    p9 = p2 * p6
    if p8 == 1:
        p8 = ''

    ss = '{x} sqrt {y}'.format(x=p8, y=p9)
    c = [ss]
    c.append('{x} sqrt {y}'.format(x=p8, y=p6))
    c.append('{x} sqrt {y}'.format(x=p7, y=p9))
    c.append('{x} sqrt {y}'.format(x=p7, y=p2))
    c.append('{x} sqrt {y}'.format(x=p7, y=p6))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(box1=box1, box2=box2, p1=p1, p2=p2, p3=p3, p4=p4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9)

    return stem, answer, comment





# 3-1-1-325
def realnum311_Stem_232():
    stem = "다음을 만족시키는 유리수 $$수식$$a$$/수식$$의 값은?\n" \
           "$$표$$$$수식$${p1} OVER sqrt {p2} DIV sqrt {p3} OVER {{ {p4} sqrt {p5} }} TIMES sqrt {{ {p6} OVER {p7} }} " \
           "= {p8} sqrt a$$/수식$$$$/표$$\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$${p1} OVER sqrt {p2} DIV sqrt {p3} OVER {{ {p4} sqrt {p5} }} TIMES sqrt {{ {p6} OVER {p7} }}$$/수식$$\n" \
              "$$수식$$= {p1} OVER sqrt {p2} TIMES {{ {p4} sqrt {p5} }} OVER sqrt {p3} TIMES sqrt {p6} OVER sqrt {p7}$$/수식$$\n" \
              "$$수식$$= {p1} OVER sqrt {p3} = {p8} sqrt {a}$$/수식$$\n" \
              "$$수식$$THEREFORE~ a = {a}$$/수식$$\n\n"

    while True:
        p3, p5, p6 = random.sample([2, 3, 5, 7], 3)
        p4 = p3
        p2 = p3 * p6
        p7 = p3 * p5
        a = p3
        p8 = np.random.randint(2, 6)
        p1 = p8 * p3
        if GCD(p6, p7) == 1 and p1 != p2:
            break

    c = random.sample(list(range(1, a))+list(range(a+1, a+5)), 4)
    c.append(a)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == a:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(a=a, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8)

    return stem, answer, comment





# 3-1-1-328
def realnum311_Stem_233():
    stem = "어느 피자 가게에서 피자를 레귤러사이즈는 $$수식$${p1}$$/수식$$원에, 라지사이즈는 $$수식$${p2}$$/수식$$에 판매하고 있다. " \
           "피자의 가격은 피자의 넓이와 정비례한다고 할 때, 라지사이즈 피자의 반지름의 길이는 레귤러사이즈 피자의 반지름의 길이의 몇 배인가?\n" \
           "① $$수식$${c1}$$/수식$$배     ② $$수식$${c2}$$/수식$$배     ③ $$수식$${c3}$$/수식$$배\n" \
           "④ $$수식$${c4}$$/수식$$배     ⑤ $$수식$${c5}$$/수식$$배\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "레귤러사이즈 피자의 반지름의 길이를 $$수식$$a$$/수식$$, 라지사이즈 피자의 반지름의 길이를 $$수식$$b$$/수식$$라 하면\n" \
              "$$수식$$a^2 pi$$/수식$$:$$수식$$b^2 pi = {p1}$$/수식$$:$$수식$${p2}$$/수식$$\n" \
              "즉 $$수식$$a^2$$/수식$$:$$수식$$b^2 = {p3}$$/수식$$:$$수식$${p4}$$/수식$$이므로 $$수식$${p3} b^2 = {p4} a^2$$/수식$$\n" \
              "$$수식$$b^2 = {p4} OVER {p3} a^2$$/수식$$\n" \
              "$$수식$$THEREFORE~ b = {p5} OVER sqrt {p3} a = {{ {p5} sqrt {p3} }} OVER {p3} a$$/수식$$\n" \
              "따라서 라지사이즈 피자의 반지름의 길이는 레귤러사이즈 피자의 반지름의 길이의 $$수식$${{ {p5} sqrt {p3} }} OVER {p3}$$/수식$$배이다.\n\n"

    p3, p4, p5 = [[3, 4, 2], [5, 9, 3], [7, 9, 3], [11, 16, 4], [13, 16, 4]][np.random.randint(0, 5)]
    if p4 == 4:
        mul = 1000 * np.random.randint(6, 9)
    elif p4 == 9:
        mul = 1000 * np.random.randint(3, 5)
    else:
        mul = 1000 * 2
    p1, p2 = p3*mul, p4*mul

    ss = '{{ {p5} sqrt {p3} }} OVER {p3}'.format(p5=p5, p3=p3)
    c = [ss]
    c.append('{p5} sqrt {p3}'.format(p3=p3, p5=p5))
    c.append('sqrt {p3} OVER {p3}'.format(p3=p3))
    c.append('sqrt {p5} OVER {p3}'.format(p3=p3, p5=p5))
    c.append('{{ {p3} sqrt {p5} }} OVER {p5}'.format(p3=p3, p5=p5))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5)

    return stem, answer, comment





# 3-1-1-334
def realnum311_Stem_234():
    stem = "다음 중 옳은 것은?\n" \
           "① $$수식$${c1}$$/수식$$\n② $$수식$${c2}$$/수식$$\n③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "① {s1}\n" \
              "② {s2}\n" \
              "③ {s3}\n" \
              "④ {s4}\n" \
              "⑤ {s5}\n\n"

    p1, p2 = random.sample([2, 3, 5, 6, 7], 2)
    p3 = p1 + p2

    q2 = [2, 3, 5, 6, 7][np.random.randint(0, 5)]
    q3 = np.random.randint(2, 6)
    q1 = np.random.randint(q3 + 1, 10)
    q4 = q1 - q3

    r2, r4 = random.sample([2, 3, 5, 7], 2)
    r6 = r2 + r4
    r1, r3 = random.sample(list(range(2, 8)), 2)
    r5 = r1 + r3

    x2 = [2, 3, 5, 6, 7][np.random.randint(0, 5)]
    x1 = np.random.randint(2, 6)
    x3 = np.random.randint(x1 + 2, 10)
    x4 = x1 - x3

    y2, y3 = random.sample([2, 3, 5, 6, 7], 2)
    y1 = np.random.randint(3, 7)
    y4 = y1 - 1

    # 옳은 보기, 틀린 보기
    cs = [['$$수식$$sqrt {p1} + sqrt {p2} != sqrt {p3}$$/수식$$'.format(p1=p1, p2=p2, p3=p3),
           '$$수식$$sqrt {p1} + sqrt {p2} = sqrt {p3}$$/수식$$'.format(p1=p1, p2=p2, p3=p3),
           '$$수식$$sqrt {p1} + sqrt {p2} != sqrt {p3}$$/수식$$'.format(p1=p1, p2=p2, p3=p3)],
          ['$$수식$${q1} sqrt {q2} - {q3} sqrt {q2} = {q4} sqrt {q2}$$/수식$$'.format(q1=q1, q2=q2, q3=q3, q4=q4),
           '$$수식$${q1} sqrt {q2} - {q3} sqrt {q2} = {q4}$$/수식$$'.format(q1=q1, q2=q2, q3=q3, q4=q4),
           '$$수식$${q1} sqrt {q2} - {q3} sqrt {q2} =  ( {q1} - {q3}  ) sqrt {q2} = {q4} sqrt {q2}$$/수식$$'.format(q1=q1, q2=q2, q3=q3, q4=q4)],
          ['$$수식$${r1} sqrt {r2} + {r3} sqrt {r4} != {r5} sqrt {r6}$$/수식$$'.format(r1=r1, r2=r2, r3=r3, r4=r4, r5=r5, r6=r6),
           '$$수식$${r1} sqrt {r2} + {r3} sqrt {r4} = {r5} sqrt {r6}$$/수식$$'.format(r1=r1, r2=r2, r3=r3, r4=r4, r5=r5, r6=r6),
           '$$수식$${r1} sqrt {r2} + {r3} sqrt {r4} != {r5} sqrt {r6}$$/수식$$'.format(r1=r1, r2=r2, r3=r3, r4=r4, r5=r5, r6=r6)],
          ['$$수식$${x1} sqrt {x2} - {x3} sqrt {x2} = {x4} sqrt {x2}$$/수식$$'.format(x1=x1, x2=x2, x3=x3, x4=x4),
           '$$수식$${x1} sqrt {x2} - {x3} sqrt {x2} = {x4}$$/수식$$'.format(x1=x1, x2=x2, x3=x3, x4=x4),
           '$$수식$${x1} sqrt {x2} - {x3} sqrt {x2} =  ( {x1} - {x3}  ) sqrt {x2} = {x4} sqrt {x2}$$/수식$$'.format(x1=x1, x2=x2, x3=x3, x4=x4)],
          ['$$수식$${y1} sqrt {y2} + sqrt {y3} - sqrt {y2} = {y4} sqrt {y2} + sqrt {y3}$$/수식$$'.format(y1=y1, y2=y2, y3=y3, y4=y4),
           '$$수식$${y1} sqrt {y2} + sqrt {y3} - sqrt {y2} = {y1} sqrt {y3}$$/수식$$'.format(y1=y1, y2=y2, y3=y3),
           '$$수식$${y1} sqrt {y2} + sqrt {y3} - sqrt {y2} = {y4} sqrt {y2} + sqrt {y3}$$/수식$$'.format(y1=y1, y2=y2, y3=y3, y4=y4)]]

    np.random.shuffle(cs)
    ans = np.random.randint(0, 5)
    s = answer_dict[ans]
    c = []
    ss = []
    for i in range(0, len(cs)):
        if i == ans:
            c.append(cs[i][0])
        else:
            c.append(cs[i][1])
        ss.append(cs[i][2])
    c1, c2, c3, c4, c5 = c
    s1, s2, s3, s4, s5 = ss

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)

    return stem, answer, comment





# 3-1-1-335
def realnum311_Stem_235():
    stem = "$$수식$$A = {p2} sqrt {p1} + {p3} sqrt {p1} - {p4} sqrt {p1}$$/수식$$, " \
           "$$수식$$B = {p6} sqrt {p5} - {p7} sqrt {p5} - {p8} sqrt {p5}$$/수식$$일 때, " \
           "$$수식$$A + B$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$$A = {p9} sqrt {p1}$$/수식$$, $$수식$$B = {p10} sqrt {p5}$$/수식$$이므로\n" \
              "$$수식$$A + B = {p9} sqrt {p1} {op} {p10} sqrt {p5}$$/수식$$\n\n"

    p1, p5 = random.sample([2, 3, 5, 6, 7], 2)

    while True:
        p2, p3, p4 = random.sample(list(range(2, 11)), 3)
        p9 = p2 + p3 - p4
        if abs(p9) > 1:
            break

    while True:
        p6 = np.random.randint(3, 9)
        p7 = np.random.randint(2, 5)
        p8 = np.random.randint(2, 5)
        p10 = p6 - p7 - p8
        if p10 != 0:
            break
    op, nop = '', ''
    if p10 > 0:
        op = '+'
    else:
        nop = '+'
    p101 = p10
    if p10 == 1:
        p10, p101 = '', '-'
    elif p10 == -1:
        p10, p101 = '-', ''

    ss = '{x1} sqrt {x2} {op} {y1} sqrt {y2}'.format(x1=p9, x2=p1, op=op, y1=p10, y2=p5)
    c = [ss]
    c.append('{x1} sqrt {x2} {op} {y1} sqrt {y2}'.format(x1=p9, x2=p1, op=nop, y1=p101, y2=p5))
    c.append('{x1} sqrt {x2}'.format(x1=p9, x2=p1))
    c.append('{x1} sqrt {x2} {op} {y1} sqrt {y2}'.format(x1=(p9+1), x2=p1, op=nop, y1=p101, y2=p5))
    c.append('{x1} sqrt {x2}'.format(x1=(p9+1), x2=p1))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p5=p5, p9=p9, p10=p10, op=op)

    return stem, answer, comment





# 3-1-1-336
def realnum311_Stem_236():
    stem = "$$수식$${{ {p1} sqrt {p2} }} OVER {p3} + {{ {p4} sqrt {p5} }} OVER {p6} " \
           "- {{ {p7} sqrt {p2} }} OVER {p8} - {{ {p9} sqrt {p5} }} OVER {p10}$$/수식$$을 계산하면?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$${{ {p1} sqrt {p2} }} OVER {p3} + {{ {p4} sqrt {p5} }} OVER {p6} " \
              "- {{ {p7} sqrt {p2} }} OVER {p8} - {{ {p9} sqrt {p5} }} OVER {p10}$$/수식$$\n" \
              "$$수식$$=  ( {p111} OVER {p3} - {p77} OVER {p8}  ) sqrt {p2} " \
              "+  ( {p44} OVER {p6} - {p99} OVER {p10}  ) sqrt {p5}$$/수식$$\n" \
              "$$수식$$= {op1} {{ {p11} sqrt {p2} }} OVER {p12} {op2} {{ {p13} sqrt {p5} }} OVER {p14}$$/수식$$\n\n"

    p2, p5 = random.sample([2, 3, 5, 6, 7], 2)
    while True:
        p3, p8 = random.sample(list(range(2, 6)), 2)
        p1, p7 = random.sample(list(range(1, 4)), 2)
        p11 = p1 * p8 - p3 * p7
        p12 = p3 * p8
        if p11 == 0:
            continue
        gcd1112 = GCD(p11, p12)
        p11 = int(p11/gcd1112)
        p12 = int(p12/gcd1112)
        if p12 != 1 and GCD(p1, p3) == 1 and GCD(p7, p8) == 1:
            break
    while True:
        p6, p10 = random.sample(list(range(2, 6)), 2)
        p4, p9 = random.sample(list(range(1, 4)), 2)
        p13 = p4 * p10 - p6 * p9
        p14 = p6 * p10
        if p13 == 0:
            continue
        gcd1314 = GCD(p13, p14)
        p13 = int(p13/gcd1314)
        p14 = int(p14/gcd1314)
        if p14 != 1 and (p3 != p6 or p8 != p10) and GCD(p4, p6) == 1 and GCD(p9, p10) == 1:
            break

    p111 = p1
    p44 = p4
    p77 = p7
    p99 = p9

    if p1 == 1:
        p1 = ''
    if p4 == 1:
        p4 = ''
    if p7 == 1:
        p7 = ''
    if p9 == 1:
        p9 = ''

    op1, op2, op22 = '', '+', '-'
    if p11 < 0:
        op1 = '-'
        p11 = -p11
    if p13 < 0:
        op2, op22 = '-', '+'
        p13 = -p13
    if p11 == 1:
        p11 = ''
    if p13 == 1:
        p13 = ''

    ss = '{op1} {{ {x1} sqrt {x2} }} OVER {x3} {op2} {{ {y1} sqrt {y2} }} OVER {y3}'.format(op1=op1, x1=p11, x2=p2, x3=p12, op2=op2, y1=p13, y2=p5, y3=p14)
    c = [ss]
    c.append('{op1} {{ {x1} sqrt {x2} }} OVER {x3} {op2} {{ {y1} sqrt {y2} }} OVER {y3}'.format(op1=op1, x1=p11, x2=p2, x3=p12, op2=op22, y1=p13, y2=p5, y3=p14))
    c.append('{op1} {{ {x1} sqrt {x2} }} OVER {x3} {op2} {{ {y1} sqrt {y2} }} OVER {y3}'.format(op1=op1, x1=p11, x2=p2, x3=p12, op2=op2, y1=p13, y2=p5, y3=p6))
    c.append('{op1} {{ {x1} sqrt {x2} }} OVER {x3} {op2} {{ {y1} sqrt {y2} }} OVER {y3}'.format(op1=op1, x1=p11, x2=p2, x3=p8, op2=op2, y1=p13, y2=p5, y3=p6))
    c.append('{op1} {{ {x1} sqrt {x2} }} OVER {x3} {op2} {{ {y1} sqrt {y2} }} OVER {y3}'.format(op1=op1, x1=p11, x2=p2, x3=p8, op2=op2, y1=p13, y2=p5, y3=p14))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p111=p111, p44=p44, p77=p77, p99=p99, op1=op1, op2=op2, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12, p13=p13, p14=p14)

    return stem, answer, comment





# 3-1-1-337
def realnum311_Stem_237():
    stem = "$$수식$$sqrt a OVER {p1} - sqrt a OVER {p2} = {p3}$$/수식$$일 때, 양수 $$수식$$a$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt a OVER {p1} - sqrt a OVER {p2} = {{ {p4} sqrt a }} OVER {p5} = {p3}$$/수식$$에서 " \
              "$$수식$$sqrt a = {p6} OVER {p7}$$/수식$$\n" \
              "$$수식$$THEREFORE~ a = {p8} OVER {p9}$$/수식$$\n\n"

    while True:
        p1 = np.random.randint(2, 6)
        p2 = np.random.randint(p1+1, 10)
        p3 = np.random.randint(1, 4)
        p4 = p2 - p1
        p5 = p1 * p2
        gcd45 = GCD(p4, p5)
        p4 = int(p4/gcd45)
        p5 = int(p5/gcd45)
        p6 = p3 * p5
        p7 = p4
        gcd67 = GCD(p6, p7)
        p6 = int(p6/gcd67)
        p7 = int(p7/gcd67)
        if p5 == 1 or p7 == 1:
            continue
        p8 = p6 * p6
        p9 = p7 * p7
        if p8 < 250:
            break

    ss = '{x} OVER {y}'.format(x=p8, y=p9)
    c = [ss]
    c.append('{x} OVER {y}'.format(x=p6, y=p7))
    c.append('{x} OVER {y}'.format(x=p9, y=p8))
    c.append('{x} OVER {y}'.format(x=int(p8/p5), y=p9))
    c.append('{x} OVER {y}'.format(x=p9, y=int(p8/p5)))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9)

    return stem, answer, comment





# 3-1-1-338
def realnum311_Stem_238():
    stem = "$$수식$$A = {p2} sqrt {p1} {op1} {p3} sqrt {p1} {op2} {p4} sqrt {p1}$$/수식$$, " \
           "$$수식$$B = {p6} sqrt {p5} {op3} {p7} sqrt {p5} {op4} {p8} sqrt {p5}$$/수식$$일 때, " \
           "$$수식$$sqrt {p11} AB$$/수식$$의 값을 구하시오.\n"
    answer = "(답) $$수식$${s}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$A = {p2} sqrt {p1} {op1} {p3} sqrt {p1} {op2} {p4} sqrt {p1}$$/수식$$\n" \
              "$$수식$$=  ( {p22} {op1} {p33} {op2} {p44}  ) sqrt {p1} = {p9} sqrt {p1}$$/수식$$\n" \
              "$$수식$$B = {p6} sqrt {p5} {op3} {p7} sqrt {p5} {op4} {p8} sqrt {p5}$$/수식$$\n" \
              "$$수식$$=  ( {p66} {op3} {p77} {op4} {p88}  ) sqrt {p5} = {p10} sqrt {p5}$$/수식$$\n" \
              "$$수식$$THEREFORE~ sqrt {p11} AB = sqrt {p11} TIMES {p9} sqrt {p1} TIMES {p10} sqrt {p5} = {s}$$/수식$$\n\n"

    while True:
        p2, p3, p4 = random.sample(list(range(-5, 0))+list(range(1, 6)), 3)
        p6, p7, p8 = random.sample(list(range(-5, 0))+list(range(1, 6)), 3)
        if (p2, p3, p4) == (p6, p7, p8):
            continue
        p9 = p2 + p3 + p4
        p10 = p6 + p7 + p8
        if p9 == 0 or p10 == 0:
            continue
        p1, p5 = random.sample([2, 3, 5, 7], 2)
        p11 = p1 * p5
        s = p11 * p9 * p10
        if abs(s) < 300:
            break

    p22, p33, p44 = p2, p3, p4
    p66, p77, p88 = p6, p7, p8
    p2 = removeOne(p2)
    p3 = removeOne(p3)
    p4 = removeOne(p4)
    p6 = removeOne(p6)
    p7 = removeOne(p7)
    p8 = removeOne(p8)
    p9 = removeOne(p9)
    p10 = removeOne(p10)

    op1, op2, op3, op4 = '', '', '', ''
    if p33 > 0:
        op1 = '+'
    if p44 > 0:
        op2 = '+'
    if p77 > 0:
        op3 = '+'
    if p88 > 0:
        op4 = '+'

    stem = stem.format(op1=op1, op2=op2, op3=op3, op4=op4, p11=p11, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8)
    answer = answer.format(s=s)
    comment = comment.format(s=s, op1=op1, op2=op2, op3=op3, op4=op4, p22=p22, p33=p33, p44=p44, p66=p66, p77=p77, p88=p88, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11)

    return stem, answer, comment





# 3-1-1-339
def realnum311_Stem_239():
    stem = "$$수식$$x = {{ {p1} + sqrt {p2} }} OVER 2$$/수식$$, $$수식$$y = {{ {p1} - sqrt {p2} }} OVER 2$$/수식$$일 때, " \
           "$$수식$$ ( x + y  )  ( x - y  )$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$$ ( x + y  ) = {{ {p1} + sqrt {p2} }} OVER 2 + {{ {p1} - sqrt {p2} }} OVER 2 " \
              "= {p3} OVER 2 = {p1}$$/수식$$\n" \
              "$$수식$$ ( x - y  ) = {{ {p1} + sqrt {p2} }} OVER 2 - {{ {p1} - sqrt {p2} }} OVER 2 " \
              "= {{ 2 sqrt {p2} }} OVER 2 = sqrt {p2}$$/수식$$\n" \
              "$$수식$$THEREFORE~  ( x + y  )  ( x - y  ) = {p1} TIMES sqrt {p2} = {p4} sqrt {p2}$$/수식$$\n\n"

    p1 = np.random.randint(1, 8)
    p2 = [2, 3, 5, 7, 11][np.random.randint(0, 5)]
    p3 = 2 * p1
    p4 = p1
    p4 = removeOne(p4)

    if p1 == 1:
        x = random.sample(list(range(2, 9)), 4)
    else:
        x = random.sample(list(range(1, p1))+list(range(p1+1, 9)), 4)
    x.append(p1)
    x.sort()

    ss = '{x} sqrt {y}'.format(x=p4, y=p2)
    c = []
    for i in range(len(x)):
        x[i] = removeOne(x[i])
        c.append('{x} sqrt {y}'.format(x=x[i], y=p2))
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4)

    return stem, answer, comment





# 3-1-1-340
def realnum311_Stem_240():
    stem = "$$수식$${p1} sqrt a - {p2} = {p3} sqrt a + {p4}$$/수식$$을 만족시키는 양수 $$수식$$a$$/수식$$의 값을 구하시오.\n"
    answer = "(답) $$수식$${s}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${p1} sqrt a - {p2} = {p3} sqrt a + {p4}$$/수식$$에서\n" \
              "$$수식$${p1} sqrt a - {p3} sqrt a = {p2} + {p4}$$/수식$$, " \
              "$$수식$${p5} sqrt a = {p6}$$/수식$$, $$수식$$sqrt a = {p7}$$/수식$$\n" \
              "$$수식$$THEREFORE~ a = {p8}$$/수식$$\n\n"

    p5, p7 = random.sample(list(range(2, 7)), 2)
    p6 = p5 * p7
    p8 = p7 * p7
    p2 = np.random.randint(1, p6)
    p4 = p6 - p2
    p3 = np.random.randint(1, 4)
    p1 = p3 + p5
    p3 = removeOne(p3)
    s = p8

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8)

    return stem, answer, comment





# 3-1-1-341
def realnum311_Stem_241():
    stem = "$$수식$$sqrt {{  ( {p1} - sqrt {p2}  ) ^2 }} - sqrt {{  ( {p3} sqrt {p4} - {p5}  ) ^2 }}$$/수식$$을 계산하면?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$${p1} - sqrt {p2} = sqrt {p6} - sqrt {p2} &gt; 0$$/수식$$, " \
              "$$수식$${p3} sqrt {p4} - {p5} = sqrt {p7} - sqrt {p8} &lt; 0$$/수식$$\n" \
              "$$수식$$THEREFORE~ sqrt {{  ( {p1} - sqrt {p2}  ) ^2 }} - sqrt {{  ( {p3} sqrt {p4} - {p5}  ) ^2 }}$$/수식$$\n" \
              "$$수식$$=  ( {p1} - sqrt {p2}  ) -  {{ -  ( {p3} sqrt {p4} - {p5}  )  }}$$/수식$$\n" \
              "$$수식$$=  ( {p1} - sqrt {p2}  ) +  ( {p3} sqrt {p4} - {p5}  )$$/수식$$\n" \
              "$$수식$$= {p9} + {p10} sqrt {p2}$$/수식$$\n\n"

    while True:
        p2 = [2, 3, 5, 6, 7][np.random.randint(0, 5)]
        p4 = p2
        p1 = np.random.randint(2, 5)
        p6 = p1 * p1
        if p6 <= p2:
            continue
        p3 = np.random.randint(2, 5)
        p7 = p3 * p3 * p4
        p5 = np.random.randint(1, 6)
        p8 = p5 * p5
        if p7 >= p8:
            continue
        p9 = p1 - p5
        p10 = p3 - 1
        if p9 != 0:
            break
    p10 = removeOne(p10)

    ss = '{x} + {y} sqrt {z}'.format(x=p9, y=p10, z=p2)
    c = [ss]
    c.append('{x} + {y} sqrt {z}'.format(x=p9, y=p3, z=p2))
    if p9 > 0:
        c.append('{x} + {y} sqrt {z}'.format(x=(p9+1), y=p3, z=p2))
        c.append('{x} + {y} sqrt {z}'.format(x=(p9+1), y=p10, z=p2))
    else:
        c.append('{x} + {y} sqrt {z}'.format(x=(p9-1), y=p3, z=p2))
        c.append('{x} + {y} sqrt {z}'.format(x=(p9-1), y=p10, z=p2))
    c.append('{y} sqrt {z}'.format(y=p10, z=p2))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10)

    return stem, answer, comment





# 3-1-1-342
def realnum311_Stem_242():
    stem = "$$수식$$a = {{ sqrt {p1} {op1} sqrt {p2} }} OVER 2$$/수식$$, " \
           "$$수식$$b = {{ sqrt {p1} {op2} sqrt {p2} }} OVER 2$$/수식$$일 때, " \
           "$$수식$$sqrt {p3}  ( a + b  )  ( a - b  )$$/수식$$의 값을 구하시오.\n"
    answer = "(답) $$수식$${s}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$a + b = {{ sqrt {p1} {op1} sqrt {p2} }} OVER 2 + {{ sqrt {p1} {op2} sqrt {p2} }} OVER 2$$/수식$$\n" \
              "\t$$수식$$= {{ 2 sqrt {p1} }} OVER 2 = sqrt {p1}$$/수식$$\n" \
              "$$수식$$a - b = {{ sqrt {p1} {op1} sqrt {p2} }} OVER 2 - {{ sqrt {p1} {op2} sqrt {p2} }} OVER 2$$/수식$$\n" \
              "\t$$수식$$= {op3} {{ 2 sqrt {p2} }} OVER 2 = {op3} sqrt {p2}$$/수식$$\n" \
              "$$수식$$THEREFORE~ sqrt {p3}  ( a + b  )  ( a - b  ) = sqrt {p3} TIMES sqrt {p1} TIMES {p22} = {s}$$/수식$$\n\n"

    op1, op2, op3 = [['+', '-', ''], ['-', '+', '-']][np.random.randint(0, 2)]
    p1, p2 = random.sample([2, 3, 5, 7, 11], 2)
    p3 = p1 * p2
    s = p3
    p22 = 'sqrt {p2}'.format(p2=p2)
    if op3 == '-':
        p22 = ' ( - sqrt {p2}  )'.format(p2=p2)
        s = -s

    stem = stem.format(op1=op1, op2=op2, p1=p1, p2=p2, p3=p3)
    answer = answer.format(s=s)
    comment = comment.format(op1=op1, op2=op2, op3=op3, p22=p22, p1=p1, p2=p2, p3=p3, s=s)

    return stem, answer, comment





# 3-1-1-343
def realnum311_Stem_243():
    stem = "$$수식$$x = sqrt {p1}$$/수식$$일 때, " \
           "$$수식$$x^2 {op1} {p2} x {op2} {p2} sqrt {p1} + {p3}$$/수식$$의 값을 구하시오.\n"
    answer = "(답) $$수식$${s}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$x^2 {op1} {p2} x {op2} {p2} sqrt {p1} + {p3}$$/수식$$\n" \
              "$$수식$$=  ( sqrt {p1}  ) ^2 {op1} {p2} TIMES sqrt {p1} {op2} {p2} sqrt {p1} + {p3} = {p4}$$/수식$$\n\n"

    op1, op2 = [['+', '-'], ['-', '+']][np.random.randint(0, 2)]
    p1 = [2, 3, 5, 6, 7][np.random.randint(0, 5)]
    p2 = np.random.randint(2, 8)
    p3 = np.random.randint(1, 9)
    p4 = p1 + p3
    s = p4

    stem = stem.format(op1=op1, op2=op2, p1=p1, p2=p2, p3=p3)
    answer = answer.format(s=s)
    comment = comment.format(op1=op1, op2=op2, p1=p1, p2=p2, p3=p3, p4=p4)

    return stem, answer, comment





# 3-1-1-344
def realnum311_Stem_244():
    stem = "$$수식$$sqrt {p1} {op1} {p2} sqrt {p3} {op2} sqrt {p4} {op3} sqrt {p5} = a sqrt {p7} + b sqrt {p9}$$/수식$$일 때, " \
           "유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$ab$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt {p1} {op1} {p2} sqrt {p3} {op2} sqrt {p4} {op3} sqrt {p5}$$/수식$$\n" \
              "$$수식$$= {p6} sqrt {p7} {op1} {p8} sqrt {p9} {op2} {p10} sqrt {p7} {op3} {p11} sqrt {p9}$$/수식$$\n" \
              "$$수식$$= {p12} sqrt {p7} {op4} {p13} sqrt {p9}$$/수식$$\n" \
              "따라서 $$수식$$a = {a}$$/수식$$, $$수식$$b = {b}$$/수식$$이므로\n" \
              "$$수식$$ab = {ab}$$/수식$$\n\n"

    while True:
        p7, p9 = random.sample([2, 3, 5, 6], 2)
        p2 = np.random.randint(2, 4)
        p8 = p2 * np.random.randint(2, 4)
        p6, p10, p11 = random.sample(list(range(-6, 0))+list(range(1, 7)), 3)
        p1 = p6 * p6 * p7
        p3 = int((p8*p8*p9) / (p2*p2))
        p4 = p10 * p10 * p7
        p5 = p11 * p11 * p9
        p12 = p6 + p10
        p13 = p8 + p11
        a, b = p12, p13
        ab = a * b
        if p12 != 0 and p13 != 0 and abs(ab) > 1:
            break

    op1, op2, op3, op4 = '+', '+', '+', '+'
    if p8 < 0:
        op1 = '-'
        p8 = -p8
    if p10 < 0:
        op2 = '-'
        p10 = -p10
    if p11 < 0:
        op3 = '-'
        p11 = -p11
    if p13 < 0:
        op4 = '-'
        p13 = -p13

    p6 = removeOne(p6)
    p10 = removeOne(p10)
    p11 = removeOne(p11)
    p12 = removeOne(p12)
    p13 = removeOne(p13)

    if ab < 0:
        c = random.sample(list(range(ab-10, ab))+list(range(ab+1, 0)), 4)
    else:
        c = random.sample(list(range(1, ab))+list(range(ab+1, ab+11)), 4)
    c.append(ab)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == ab:
            s = answer_dict[i]
            break

    stem = stem.format(op1=op1, op2=op2, op3=op3, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p7=p7, p9=p9, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(a=a, b=b, ab=ab, op1=op1, op2=op2, op3=op3, op4=op4, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12, p13=p13)

    return stem, answer, comment





# 3-1-1-345
def realnum311_Stem_245():
    stem = "$$수식$${op3} sqrt {p1} {op1} {p2} sqrt {p3} {op2} {p4} sqrt {p5}$$/수식$$를 계산하면?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$${op3} sqrt {p1} {op1} {p2} sqrt {p3} {op2} {p4} sqrt {p5}$$/수식$$\n" \
              "$$수식$$= {p6} sqrt {p7} {op1} {p8} sqrt {p7} {op2} {p9} sqrt {p7} = {p10} sqrt {p7}$$/수식$$\n\n"

    while True:
        p7 = [2, 3, 5, 6, 7][np.random.randint(0, 5)]
        p2, p4 = random.sample([-2, -3, 2, 3], 2)
        p8 = p2 * np.random.randint(2, 5)
        p9 = p4 * np.random.randint(2, 5)
        p6 = random.sample(list(range(-9, 0))+list(range(1, 10)), 1)[0]
        p1 = p6 * p6 * p7
        p3 = int((p8*p8*p7)/(p2*p2))
        p5 = int((p9*p9*p7)/(p4*p4))
        p10 = p6 + p8 + p9
        if p10 != 0 and p1 < 250 and p3 < 250 and p5 < 250:
            break

    op1, op2, op3 = '', '', ''
    if p2 > 0:
        op1 = '+'
    if p4 > 0:
        op2 = '+'
    if p6 < 0:
        op3 = '-'

    if p10 > 0:
        if p10 > 1:
            x = random.sample(list(range(1, p10))+list(range(p10+1, p10+6)), 4)
        else:
            x = random.sample(list(range(p10+1, p10+6)), 4)
    else:
        if p10 < -1:
            x = random.sample(list(range(p10+1, 0))+list(range(p10-5, p10)), 4)
        else:
            x = random.sample(list(range(p10-5, p10)), 4)
    x.append(p10)
    x.sort()

    p6 = removeOne(p6)
    p10 = removeOne(p10)

    ss = '{x} sqrt {y}'.format(x=p10, y=p7)
    c = []
    for i in range(len(x)):
        x[i] = removeOne(x[i])
        c.append('{x} sqrt {y}'.format(x=x[i], y=p7))
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(op1=op1, op2=op2, op3=op3, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(op1=op1, op2=op2, op3=op3, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10)

    return stem, answer, comment





# 3-1-1-346
def realnum311_Stem_246():
    stem = "$$수식$${p1} sqrt {p2} {op1} {p3} sqrt {p4} {op2} sqrt {p5}$$/수식$$를 만족하는 유리수 $$수식$$a$$/수식$$의 값을 구하시오.\n"
    answer = "(답) $$수식$${s}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${p1} sqrt {p2} {op1} {p3} sqrt {p4} {op2} sqrt {p5} " \
              "= {p1} sqrt {p2} {op1} {p3} TIMES {p6} sqrt {p2} {op3} {p7} sqrt {p2}$$/수식$$\n" \
              "     $$수식$$= {p1} sqrt {p2} {op1} {p8} sqrt {p2} {op3} {p7} sqrt {p2}$$/수식$$\n" \
              "     $$수식$$=  ( {p11} {op1} {p8} {op3} {p7}  ) sqrt {p2} = {p9} sqrt {p2}$$/수식$$\n" \
              "$$수식$$THEREFORE~ a = {s}$$/수식$$\n\n"

    while True:
        p1 = random.sample(list(range(-9, 0))+list(range(1, 10)), 1)[0]
        p2 = [2, 3, 5, 6, 7][np.random.randint(0, 5)]
        p3 = [-2, -3, 2, 3][np.random.randint(0, 4)]
        p6 = np.random.randint(2, 5)
        p8 = p3 * p6
        p7 = np.random.randint(2, 5)
        p4 = p6 * p6 * p2
        p5 = p7 * p7 * p2
        p9 = p1 + p8 + p7
        if p9 != 0 and p4 != p5 and p4 < 200 and p5 < 250:
            break

    s = p9
    p11 = p1
    p1 = removeOne(p1)
    p9 = removeOne(p9)

    op1 = ''
    if p3 > 0:
        op1 = '+'
    if p7 > 0:
        op2, op3 = '+', '+'
    else:
        op2, op3 = '-', ''

    stem = stem.format(op1=op1, op2=op2, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5)
    answer = answer.format(s=s)
    comment = comment.format(s=s, op1=op1, op2=op2, op3=op3, p11=p11, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9)

    return stem, answer, comment





# 3-1-1-347
def realnum311_Stem_247():
    stem = "$$수식$${p1} sqrt a {op1} sqrt {p2} {op2} sqrt {p3} = sqrt {p4}$$/수식$$일 때, 자연수 $$수식$$a$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$${p1} sqrt a {op1} sqrt {p2} {op2} sqrt {p3} = sqrt {p4}$$/수식$$에서\n" \
              "$$수식$${p1} sqrt a {op3} {p5} sqrt {p6} {op4} {p7} sqrt {p6} = {p8} sqrt {p6}$$/수식$$\n" \
              "$$수식$${p1} sqrt a = {p9} sqrt {p6}$$/수식$$, $$수식$$sqrt a = {p10} sqrt {p6}$$/수식$$\n" \
              "$$수식$$THEREFORE~ a = {a}$$/수식$$\n\n"

    while True:
        p6 = [2, 3, 5, 6, 7][np.random.randint(0, 5)]
        p5, p7, p8 = random.sample(list(range(-5, -1))+list(range(2, 6)), 3)
        p9 = p8 - p5 - p7
        if p9 <= 0:
            continue
        divs = getMyDivisors(p9)
        if len(divs) <= 1:
            continue
        p1 = random.sample(divs, 1)[0]
        p10 = int(p9 / p1)
        a = p10 * p10 * p6
        p2 = p5 * p5 * p6
        p3 = p7 * p7 * p6
        p4 = p8 * p8 * p6
        if a < 100 and p2 < 250 and p3 < 250 and p4 < 250:
            break

    if p5 > 0:
        op1, op3 = '+', '+'
    else:
        op1, op3 = '-', ''
    if p7 > 0:
        op2, op4 = '+', '+'
    else:
        op2, op4 = '-', ''

    c = random.sample(list(range(a-5, a)) + list(range(a + 1, a + 6)), 4)
    c.append(a)
    c.sort()
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == a:
            s = answer_dict[i]
            break

    stem = stem.format(op1=op1, op2=op2, p1=p1, p2=p2, p3=p3, p4=p4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(a=a, op1=op1, op2=op2, op3=op3, op4=op4, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10)

    return stem, answer, comment





# 3-1-1-348
def realnum311_Stem_248():
    stem = "$$수식$${op1} sqrt {p1} + a sqrt {p2} {op2} sqrt {p3} = {p4} sqrt {p2}$$/수식$$일 때, " \
           "유리수 $$수식$$a$$/수식$$의 값을 구하시오.\n"
    answer = "(답) $$수식$${s}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${op1} sqrt {p1} + a sqrt {p2} {op2} sqrt {p3} = {p4} sqrt {p2}$$/수식$$에서\n" \
              "$$수식$${p5} sqrt {p2} + a sqrt {p2} {op3} {p6} sqrt {p2} = {p4} sqrt {p2}$$/수식$$\n" \
              "$$수식$$ ( {p5} + a {op3} {p6}  ) sqrt {p2} = {p4} sqrt {p2}$$/수식$$\n" \
              "$$수식$$a {op4} {p7} = {p4}$$/수식$$\n" \
              "$$수식$$THEREFORE~ a = {s}$$/수식$$\n\n"

    while True:
        p5, p6 = random.sample(list(range(-5, -1))+list(range(2, 6)), 2)
        p4 = random.sample(list(range(-5, 0))+list(range(1, 6)), 1)[0]
        p7 = p5 + p6
        s = p4 - p7
        if p7 != 0 and s != 0:
            break

    p2 = [2, 3, 5, 6, 7][np.random.randint(0, 5)]
    p1 = p5 * p5 * p2
    p3 = p6 * p6 * p2
    p4 = removeOne(p4)

    op1, op4 = '', ''
    if p5 < 0:
        op1 = '-'
    if p6 > 0:
        op2, op3 = '+', '+'
    else:
        op2, op3 = '-', ''
    if p7 > 0:
        op4 = '+'

    stem = stem.format(op1=op1, op2=op2, p1=p1, p2=p2, p3=p3, p4=p4)
    answer = answer.format(s=s)
    comment = comment.format(s=s, op1=op1, op2=op2, op3=op3, op4=op4, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7)

    return stem, answer, comment





# 3-1-1-349
def realnum311_Stem_249():
    stem = "$$수식$${op1} sqrt {p1} OVER {p2} {op2} sqrt {p3} OVER {p4} {op3} sqrt {p5} OVER {p6} {op4} sqrt {p7} " \
           "= k sqrt {p}$$/수식$$을 만족시키는 유리수 $$수식$$k$$/수식$$의 값을 구하시오.\n"
    answer = "(답) $$수식$${s}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${op1} sqrt {p1} OVER {p2} {op2} sqrt {p3} OVER {p4} {op3} sqrt {p5} OVER {p6} {op4} sqrt {p7}$$/수식$$\n" \
              "$$수식$$= {op1} {{ {p8} sqrt {p} }}OVER {p2} {op2} {{ {p9} sqrt {p} }} OVER {p4} " \
              "{op3} {{ {p10} sqrt {p} }} OVER {p6} {op5} {p11} sqrt {p}$$/수식$$\n" \
              "$$수식$$= {op1} {p12} sqrt {p} {op2} sqrt {p} OVER {p13} {op3} sqrt {p} OVER {p13} {op5} {p11} sqrt {p}$$/수식$$\n" \
              "$$수식$$= {p14} sqrt {p}$$/수식$$\n" \
              "$$수식$$THEREFORE~ k = {s}$$/수식$$\n\n"

    while True:
        p = [2, 3, 5, 6, 7][np.random.randint(0, 5)]
        op1 = ['', '-'][np.random.randint(0, 2)]
        p2 = np.random.randint(2, 4)
        p12 = np.random.randint(1, 3)
        p8 = p2 * p12
        p1 = p8 * p8 * p
        op2, op3 = [['+', '-'], ['-', '+']][np.random.randint(0, 2)]
        p9, p10 = random.sample(list(range(2, 6)), 2)
        p13 = np.random.randint(2, 4)
        p4 = p9 * p13
        p6 = p10 * p13
        p3 = p9 * p9 * p
        p5 = p10 * p10 * p
        p11 = random.sample(list(range(-5, -1))+list(range(2, 6)), 1)[0]
        p7 = p11 * p11 * p
        if op1 == '-':
            p14 = p11 - p12
        else:
            p14 = p11 + p12
        if p14 != 0:
            break
    s = p14
    p14 = removeOne(p14)
    p12 = removeOne(p12)
    if p11 > 0:
        op4, op5 = '+', '+'
    else:
        op4, op5 = '-', ''

    stem = stem.format(op1=op1, op2=op2, op3=op3, op4=op4, p=p, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7)
    answer = answer.format(s=s)
    comment = comment.format(s=s, op1=op1, op2=op2, op3=op3, op4=op4, op5=op5, p=p, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12, p13=p13, p14=p14)

    return stem, answer, comment





# 3-1-1-350
def realnum311_Stem_250():
    stem = "$$수식$${op1} sqrt {p1} OVER {p2} {op2} sqrt {p3} OVER {p4} {op3} sqrt {p5} OVER {p6} {op4} sqrt {p7}$$/수식$$를 계산하면?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$${op1} sqrt {p1} OVER {p2} {op2} sqrt {p3} OVER {p4} {op3} sqrt {p5} OVER {p6} {op4} sqrt {p7}$$/수식$$\n" \
              "$$수식$$= {op1} {{ {p8} sqrt {x} }} OVER {p2} {op2} {{ {p9} sqrt {y} }} OVER {p4} " \
              "{op3} {{ {p10} sqrt {x} }} OVER {p6} {op5} {p11} sqrt {y}$$/수식$$\n" \
              "$$수식$$=  ( {op1} {p8} OVER {p2} {op3} {p10} OVER {p6}  ) sqrt {x} " \
              "+  ( {op6} {p12} {op5} {p11}  ) sqrt {y}$$/수식$$\n" \
              "$$수식$$= {op7} {{ {p13} sqrt {x} }} OVER {p14} {op8} {p15} sqrt {y}$$/수식$$\n\n"

    x, y = random.sample([2, 3, 5, 6], 2)

    op1 = ['', '-'][np.random.randint(0, 2)]
    op3 = ['+', '-'][np.random.randint(0, 2)]
    while True:
        p2, p8 = random.sample(list(range(2, 7)), 2)
        if GCD(p2, p8) != 1:
            continue
        p6, p10 = random.sample(list(range(2, 7)), 2)
        if GCD(p6, p10) != 1:
            continue
        op7, op77 = '', '-'
        if op1 == '-' and op3 == '-':
            p13 = p8 * p6 + p10 * p2
            op7, op77 = '-', ''
        elif op1 == '-':
            p13 = - p8 * p6 + p10 * p2
            if p13 < 0:
                p13 = -p13
                op7, op77 = '-', ''
        elif op3 == '-':
            p13 = p8 * p6 - p10 * p2
            if p13 < 0:
                p13 = -p13
                op7, op77 = '-', ''
        else:
            p13 = p8 * p6 + p10 * p2
        p14 = p2 * p6
        if p13 == 0:
            continue
        gcd1314 = GCD(p13, p14)
        p13 = int(p13/gcd1314)
        p14 = int(p14/gcd1314)
        if p14 != 1:
            break
    p1 = p8 * p8 * x
    p5 = p10 * p10 * x
    p13 = removeOne(p13)

    while True:
        p11 = random.sample(list(range(-5, -1))+list(range(2, 6)), 1)[0]
        p7 = p11 * p11 * y
        p4 = np.random.randint(2, 4)
        p12 = np.random.randint(1, 3)
        p9 = p4 * p12
        p3 = p9 * p9 * y
        if p11 > 0:
            op4, op5 = '+', '+'
        else:
            op4, op5 = '-', ''
        op2, op6 = [['+', ''], ['-', '-']][np.random.randint(0, 2)]
        if op6 == '-':
            p15 = p11 - p12
        else:
            p15 = p11 + p12
        if p15 != 0:
            break
    if p15 > 0:
        op8, op88 = '+', '-'
    else:
        p15 = -p15
        op8, op88 = '-', '+'
    p15 = removeOne(p15)

    ss = '{op7} {{ {p13} sqrt {x} }} OVER {p14} {op8} {p15} sqrt {y}'.format(op7=op7, op8=op8, x=x, y=y, p13=p13, p14=p14, p15=p15)
    c = [ss]
    c.append('{op7} {{ {p13} sqrt {x} }} OVER {p14} {op8} {p15} sqrt {y}'.format(op7=op77, op8=op8, x=x, y=y, p13=p13, p14=p14, p15=p15))
    c.append('{op7} {{ {p13} sqrt {x} }} OVER {p14} {op8} {p15} sqrt {y}'.format(op7=op7, op8=op88, x=x, y=y, p13=p13, p14=p14, p15=p15))
    c.append('{op7} {{ {p13} sqrt {x} }} OVER {p14} {op8} {p15} sqrt {y}'.format(op7=op77, op8=op88, x=x, y=y, p13=p13, p14=p14, p15=p15))
    c.append('{op7} {{ {p13} sqrt {x} }} OVER {p14} {op8} {p15} sqrt {y}'.format(op7=op77, op8=op8, x=y, y=x, p13=p13, p14=p14, p15=p15))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(op1=op1, op2=op2, op3=op3, op4=op4, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(x=x, y=y, op1=op1, op2=op2, op3=op3, op4=op4, op5=op5, op6=op6, op7=op7, op8=op8, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12, p13=p13, p14=p14, p15=p15)

    return stem, answer, comment





# 3-1-1-352
def realnum311_Stem_251():
    stem = "$$수식$${p1}  ( sqrt {p2} - sqrt {p3}  ) - sqrt {p4}  ( sqrt {p5} - {p6}  )$$/수식$$를 계산하면?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$${p1}  ( sqrt {p2} - sqrt {p3}  ) - sqrt {p4}  ( sqrt {p5} - {p6}  )$$/수식$$\n" \
              "$$수식$$= {p1}  ( {p7} sqrt {p8} - {p9} sqrt {p10}  ) - sqrt {p4}  ( {p11} sqrt {p12} - {p6}  )$$/수식$$\n" \
              "$$수식$$= {p13} sqrt {p8} - {p14} sqrt {p10} - {p11} sqrt {p15} + {p6} sqrt {p4}$$/수식$$\n" \
              "$$수식$$= {p13} sqrt {p8} - {p14} sqrt {p10} - {p16} sqrt {p8} + {p6} sqrt {p4} = {p17} sqrt {p8}$$/수식$$\n\n"

    while True:
        p8, p12 = random.sample([2, 3, 5, 7], 2)
        p4 = p8 * p12
        p15 = p4 * p12
        p10 = p4
        p7 = np.random.randint(2, 5)
        p9 = np.random.randint(2, 5)
        p11 = np.random.randint(2, 5)
        p2 = p7 * p7 * p8
        p3 = p9 * p9 * p10
        p5 = p11 * p11 * p12
        p16 = p11 * p12
        p1 = np.random.randint(2, 6)
        p13 = p1 * p7
        p14 = p1 * p9
        p6 = p14
        p17 = p13 - p16
        if p17 != 0:
            break

    p77 = p17
    p17 = removeOne(p17)
    ss = '{x} sqrt {y}'.format(x=p17, y=p8)
    c = [ss]
    c.append('{x} sqrt {y}'.format(x=removeOne(-p77), y=p8))
    c.append('{x} sqrt {y}'.format(x=(2*p77), y=p10))
    c.append('{x} sqrt {y}'.format(x=-(2*p77), y=p10))
    c.append('sqrt {x} + {y} sqrt {z}'.format(x=p8, y=removeOne(abs(p77)), z=p12))
    np.random.shuffle(c)
    c1, c2, c3, c4, c5 = c
    for i in range(len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10, p11=p11, p12=p12, p13=p13, p14=p14, p15=p15, p16=p16, p17=p17)

    return stem, answer, comment





# 3-1-1-353
def realnum311_Stem_252():
    stem = "$$수식$$sqrt {p1} - sqrt {y}  ( {p2} sqrt {p3} - sqrt {p4}  )$$/수식$$를 계산하면?\n" \
           "① $$수식$${c1}$$/수식$$     ② $$수식$${c2}$$/수식$$     ③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$     ⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(답) {s}\n"
    comment = "(해설)\n" \
              "$$수식$$sqrt {p1} - sqrt {y}  ( {p2} sqrt {p3} - sqrt {p4}  )$$/수식$$\n" \
              "$$수식$$= {p5} sqrt {x} - {p2} sqrt {p6} + sqrt {p7}$$/수식$$\n" \
              "$$수식$$= {p5} sqrt {x} - {p8} sqrt {x} + {p9} sqrt {x}$$/수식$$\n" \
              "$$수식$$= {p10} sqrt {x}$$/수식$$\n\n"

    while True:
        x, y = random.sample([2, 3, 5], 2)
        p3 = x * y
        p6 = p3 * y
        mul = np.random.randint(2, 4)
        p4 = p3 * mul * mul
        p7 = p4 * y
        p9 = mul * y
        p2 = np.random.randint(1, 5)
        p8 = p2 * y
        p5 = np.random.randint(2, 7)
        p1 = p5 * p5 * x
        p10 = p5 - p8 + p9
        if p10 != 0 and p7 < 300:
            break

    while True:
        cs = random.sample(list(range(p10-10, p10))+list(range(p10+1, p10+11)), 4)
        if 0 not in cs:
            break
    cs.append(p10)
    cs.sort()
    c = []
    for i in range(len(cs)):
        cs[i] = removeOne(cs[i])
        c.append('{p10} sqrt {x}'.format(p10=cs[i], x=x))
    c1, c2, c3, c4, c5 = c

    p10 = removeOne(p10)
    p2 = removeOne(p2)
    ss = '{p10} sqrt {x}'.format(p10=p10, x=x)
    for i in range(len(c)):
        if c[i] == ss:
            s = answer_dict[i]
            break

    stem = stem.format(y=y, p1=p1, p2=p2, p3=p3, p4=p4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(s=s)
    comment = comment.format(x=x, y=y, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10)

    return stem, answer, comment

# 3-1-1-354
def realnum311_Stem_253():
    stem = "{f1}을 계산하면?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n"\
        "{f1}\n"\
        "{f2}\n"\
        "{f3}\n\n"

    f1 = conv('$$수식$$`N1 sqrt {N2} ( `N3 sqrt {N2} `-`N4)`-` sqrt {N5} `+`N6 sqrt {(N7) ^{N8}} `$$/수식$$', 'N', 1, 8)
    f2 = conv('$$수식$$=`R1`-`R2 sqrt {R3} `-`R4 sqrt {R3} `+`R5$$/수식$$', 'R', 1, 5)
    f3 = conv('$$수식$$=`R6`-`R7 sqrt {R8}$$/수식$$', 'R', 5, 8)

    N1 = randint(1, 5)
    N2 = make_sqrt()
    N3 = randint(1, 5)
    N4 = make_exclude0(9)
    while True:
        N5 = N2 * pow(randint(2, 3), make_exponent())
        if(int(math.sqrt(N5/N2)) != N1*N4):
            break
    N6 = make_exclude0(5)
    N7 = make_excludeunder1(3)
    #지수는 2로 통일
    N8 = 2
    R1 = N1*N2*N3
    R2 = N1*N4
    R3 = N2
    R4 = int(math.sqrt(N5/N2))
    R5 = N6 * int(math.sqrt(pow(N7, N8)))
    R6 = R1+R5
    R7 = R2+R4
    R8 = R3

    a = f3.replace('=', '')
    R6_list = make_choice(R6)
    R7_list = make_choice(R7)
    # 두 개 이상의 R 값을 바꾸는 경우 첫 번째에 옳은 R값이 할당된 index를 이용해 정답 생성
    index = R6_list.index(R6)
    choice_list = []
    for i in range(0, 5):
        if(R7_list[i]!=0):
            choice_list.append(a.format(R6=R6_list[i], R7=R7_list[i], R8=R8, left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$$`{R6}`$$/수식$$'.format(R6=R6))
    if(R7!=0):
        choice_list[index] = a.format(R6=R6, R7=R7, R8=R8, left='{left}', right='{right}')


    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-355
def realnum311_Stem_254():
    stem = "{f1}, {f2}일 때, {f3}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n"\
        "{f3}\n"\
        "{f4}\n"\
        "{f5}\n"\
        "{f6}\n\n"

    f1 = conv('$$수식$$x`=`N1 sqrt {N2} `-`N3 sqrt {N4}$$/수식$$', 'N', 1, 4)
    f2 = conv('$$수식$$y`=`N5 sqrt {N2} `+`N6 sqrt {N4}$$/수식$$', 'N', 2, 6)
    f3 = conv('$$수식$$sqrt {N4} x`-` sqrt {N2} y`$$/수식$$', 'N', 2, 4)
    f4 = conv('$$수식$$=` sqrt {N4} (`N1 sqrt {N2} `-`N3 sqrt {N4} )`-` sqrt {N2} (`N5 sqrt {N2} `+`N6 sqrt {N4} )$$/수식$$', 'N', 1, 6)
    f5 = conv('$$수식$$=`R1 sqrt {R2} `-`R3`-`R4`-`R5 sqrt {R2}$$/수식$$', 'R', 1, 5)
    f6 = conv('$$수식$$=`-R6$$/수식$$', 'R', 6, 6)

    N1 = randint(1, 5)
    N2 = make_sqrt()
    N3 = randint(1, 5)
    while True:
        N4 = make_sqrt()
        if(N4 != N2):
            break
    N5 = randint(1, 5)
    N6 = N1
    R1 = N1
    R2 = N2*N4
    R3 = N3*N4
    R4 = N2*N5
    R5 = N6
    R6 = R3+R4

    a = f6.replace('=', '')
    R6_list = make_choice(R6)
    index = R6_list.index(R6)
    choice_list = []
    for i in range(0, 5):
        choice_list.append(a.format(R6=R6_list[i], left='{left}', right='{right}'))


    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4])\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f3=f3, f4=f4, f5=f5, f6=f6)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-356
def realnum311_Stem_255():
    stem = "다음 중 {f1}, {f2}일 때, {f3}을 a, b를 사용하여 바르게 나타낸 것은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n"\
        "{f3}\n"\
        "{f4}\n"\
        "{f5}\n"\
        "{f6}\n"\
        "{f7}\n\n"

    f1 = conv('$$수식$$sqrt {N1} `=`a`$$/수식$$', 'N', 1, 1)
    f2 = conv('$$수식$$sqrt {N2} `=`b`$$/수식$$', 'N', 2, 2)
    f3 = conv('$$수식$$`N3 sqrt {N1} (`N4 sqrt {N2} `+`N5 sqrt {N1} )`-`(`N6 sqrt {N2} `-`N7 sqrt {N1} )`N8 sqrt {N2} `$$/수식$$', 'N', 1, 8)
    f4 = conv('$$수식$$=`R1 sqrt {R2} `+`R3`-`(`R4`-`R5 sqrt {R2} )$$/수식$$', 'R', 1, 5)
    f5 = conv('$$수식$$=`R1 sqrt {R2} `+`R3`-`R4`-`R5 sqrt {R2} `=`R6 sqrt {R2}$$/수식$$', 'R', 1, 6)
    f6 = conv('$$수식$$=`R6 sqrt {R7 TIMES R8} `=`R6 sqrt {R7} sqrt {R8}$$/수식$$', 'R', 6, 8)
    f7 = conv('$$수식$$=`R6 a`b$$/수식$$', 'R', 6, 6)

    N1 = make_sqrt()
    while True:
        N2 = make_sqrt()
        if(N2 != N1):
            break
    N3 = N2
    while True:
        N4 = make_sqrt()
        if(N4 != N2):
            break
    N4 = randint(1, 5)
    N5 = make_exclude0(5)
    N6 = N1
    N7 = make_exclude0(5)
    N8 = N5
    R1 = N3*N4
    R2 = N1*N2
    R3 = N1*N3*N5
    R4 = N2*N6*N8
    R5 = N7*N8
    R6 = R1-R5
    R7 = N1
    R8 = N2

    a = f7.replace('=', '')
    R6_list = make_choice(R6)
    index = R6_list.index(R6)
    choice_list = []
    for i in range(0, 5):
        if(R6_list[i]!=0):
            choice_list.append(a.format(R6=R6_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$$`0$$/수식$$')
    if(R6==0):
        f6 = '$$수식$$`0$$/수식$$'
        f7 = ''

    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4])\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f3=f3, f4=f4, f5=f5, f6=f6, f7=f7)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-357
def realnum311_Stem_256():
    stem = "{f1}, {f2}라 할 때, 다음 중 {f3}을 계산한 결과와 같은 것은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n"\
        "{f3}\n"\
        "{f4}\n"\
        "{f5}\n"\
        "{f6}\n"\
        "{f7}\n\n"

    f1 = conv('$$수식$$sqrt {N1} `=`a`$$/수식$$', 'N', 1, 1)
    f2 = conv('$$수식$$sqrt {N2} `=`b`$$/수식$$', 'N', 2, 2)
    f3 = conv('$$수식$$sqrt {N3} ( sqrt {N4} `-`N5 sqrt {N6} )`+`N7 sqrt {N8} ( sqrt {N9} `-`N10 sqrt {N11} )$$/수식$$', 'N', 3, 11)
    f4 = conv('$$수식$$= sqrt {R1} `-`R2 sqrt {R3} `+`R4 sqrt {R5} `-`R6 sqrt {R7}$$/수식$$', 'R', 1, 7)
    f5 = conv('$$수식$$=`R8 sqrt {R9} `-`R10 sqrt {R11} `+`R12 sqrt {R9} `-`R13 sqrt {R11}$$/수식$$', 'R', 8, 13)
    f6 = conv('$$수식$$=`R14 sqrt {R9} `-`R15 sqrt {R11}$$/수식$$', 'R', 9, 15)
    f7 = conv('$$수식$$=`R14 a`-`R15 b$$/수식$$', 'R', 14, 15)

    while True:
        N1 = make_sqrt(5)
        while True:
            N2 = make_sqrt(5)
            if (N2 != N1):
                break
        # N3는 N1을 포함한 수 (N1*N1 제외)
        while True:
            N3 = N1 * randint(2, 3)
            if (N3 != N1 * N1):
                break
        # N4는 N3/N1에 완전제곱이 곱해진 수
        N4 = int(N3 / N1 * pow(randint(1, 2), make_exponent()))
        N5 = make_exclude0(5)
        N6 = N2 * N3
        N7 = make_exclude0(5)
        N8 = N1 * N2
        N9 = N2
        N10 = make_exclude0(5)
        N11 = N1
        R1 = N3 * N4
        R2 = N5
        R3 = N3 * N6
        R4 = N7
        R5 = N8 * N9
        R6 = N7 * N10
        R7 = N8 * N11
        R8 = int(math.sqrt(R1 / N1))
        R9 = N1
        R10 = R2 * int(math.sqrt(R3 / N2))
        R11 = N2
        R12 = R4 * int(math.sqrt(R5 / N1))
        R13 = R6 * int(math.sqrt(R7 / N2))
        R14 = R8 + R12
        R15 = R10 + R13

        if(R14 != 0 and R15 != 0):
            break

    a = f7.replace('=', '')
    R14_list = make_choice(R14)
    R15_list = make_choice(R15)
    # 두 개 이상의 R 값을 바꾸는 경우 첫 번째에 옳은 R값이 할당된 index를 이용해 정답 생성
    index = R14_list.index(R14)
    choice_list = []
    for i in range(0, 5):
        choice_list.append(a.format(R14=R14_list[i], R15=R15_list[i], left='{left}', right='{right}'))
    choice_list[index]=a.format(R14=R14, R15=R15, left='{left}', right='{right}')


    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9, N10=N10, N11=N11, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f3=f3, f4=f4, f5=f5, f6=f6, f7=f7)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9, N10=N10, N11=N11,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, R12=R12, R13=R13, R14=R14, R15=R15, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-358
def realnum311_Stem_257():
    stem = "{f1}일 때, 유리수 $$수식$$p$$/수식$$, $$수식$$q$$/수식$$에 대하여 $$수식$$p ^{ex} +q ^{ex}$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f2}{f3}\n"\
              "{f4}\n"\
              "따라서 {f5}이므로\n" \
              "{f6}\n\n"

    f1 = conv('$$수식$$` sqrt {N3} `-`N4 sqrt {N5} `+`N6 sqrt {N7} ( sqrt {N8} `-`N9)`=`p sqrt {N1} `+`q sqrt {N2}$$/수식$$', 'N', 1, 9)
    f2 = conv('$$수식$$` sqrt {N3} `-`N4 sqrt {N5} `+`N6 sqrt {N7} ( sqrt {N8} `-`N9)$$/수식$$', 'N', 3, 9)
    f3 = conv('$$수식$$`=`R1 sqrt {R2} `-`R3 sqrt {R4} `+`R5 sqrt {R2} `-`R6 sqrt {R4}$$/수식$$', 'R', 1, 6)
    f4 = conv('$$수식$$`=`R7 sqrt {R2} `+`R8 sqrt {R4}$$/수식$$', 'R', 2, 8)
    f5 = conv('$$수식$$p`=`R7,~q`=`R8$$/수식$$', 'R', 7, 8)
    f6 = conv('$$수식$$p ^{2} +q ^{2} `=`(R7) ^{2} `+`(R8) ^{2} =R9$$/수식$$', 'R', 7, 9)

    N1 = make_sqrt()
    while True:
        N2 = make_sqrt()
        if (N2 != N1):
            break
    N3 = N1 * pow(randint(1, 3), make_exponent())
    N4 = make_exclude0(1)
    N5 = N2 * pow(randint(1, 3), make_exponent())
    N6 = make_exclude0(1)
    N7 = N2
    N8 = N1*N2
    N9 = make_exclude0(10)
    R1 = int(math.sqrt(N3/N1))
    R2 = N1
    R3 = N4*int(math.sqrt(N5/N2))
    R4 = N2
    R5 = N6*N2
    R6 = N6*N9
    R7 = R1+R5
    R8 = -(R3+R6)
    R9 = pow(R7, 2)+pow(R8, 2)
    a = R9

    stem = stem.format(f1=f1, ex=2) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9, left=left, right=right)
    answer = answer.format(a=a)
    comment = comment.format(f2=f2, f3=f3, f4=f4, f5=f5, f6=f6)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-359
def realnum311_Stem_258():
    stem = "{f1}을 계산하면?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n"\
              "{f2}\n"\
              "{f3}\n" \
              "{f4}\n"\
              "{f5}\n\n"

    f1 = conv('$$수식$${`N1 sqrt {N2}} over {N3} `-` {N4} over {sqrt {N5}} `+` {sqrt {N6}} over {sqrt {N7}} `$$/수식$$', 'N', 1, 7)
    f2 = conv('$$수식$$=` {`R1`TIMES`R2 sqrt {R3}} over {R2} `-` {R4} over {`R5 sqrt {R3}} `+` {sqrt {R6}} over {`R7 sqrt {R8}}$$/수식$$', 'R', 1, 8)
    f3 = conv('$$수식$$=`R11 sqrt {R3} `-` {`R4 sqrt {R3}} over {R9} `+` {sqrt {R3}} over {R10}$$/수식$$', 'R', 3, 11)
    f4 = conv('$$수식$$=`  ( `R11`-` {R4} over {R9} `+` {1} over {R10}  ) ` sqrt {R3}$$/수식$$', 'R', 3, 11)
    f5 = conv('$$수식$$={`R12 sqrt {R3}} over {R13}$$/수식$$', 'R', 3, 13)

    sq = make_sqrt(5) #모든 제곱근의 공통 요소

    N1 = randint(2, 5)
    N2 = sq * pow(randint(2, 4), 2)
    N3 = int(math.sqrt(N2/sq))
    N4 = randint(1, 5)
    N5 = sq * pow(randint(1, 4), make_exponent())
    while True:
        N6 = make_sqrt(5)
        if (N6 != sq):
            break
    N7 = N6 * sq * pow(randint(1, 2), make_exponent())
    R1 = N1
    R2 = N3
    R3 = sq
    R4 = N4
    R5 = int(math.sqrt(N5/sq))
    R6 = N6
    R7 = int(math.sqrt(N7/(sq*N6)))
    R8 = R3*R6
    R9 = R3*R5
    R10 = R3*R7
    R11 = R1

    result= R1 - Fraction(R4, R9) + Fraction(1, R10)
    # 분자
    R12 = result.numerator
    # 분모(>0)
    R13 = result.denominator

    a = f5.replace('=', '')
    if(R13>3):
        R13_list = make_choice(R13)
    else:
        R13_list = [R13, R13+1, R13+1, R13+2, R13+3]
        random.shuffle(R13_list)
    R12_list = make_choice(R12)
    # 두 개 이상의 R 값을 바꾸는 경우 첫 번째에 옳은 R값이 할당된 index를 이용해 정답 생성
    index = R13_list.index(R13)
    choice_list = []
    for i in range(0, 5):
        if(R12_list[i]!=0):
            R12_list[i] = Fraction(R12_list[i], R13_list[i]).numerator
            R13_list[i] = Fraction(R12_list[i], R13_list[i]).denominator
            choice_list.append(a.format(R3=R3, R12=R12_list[i], R13=R13_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$$0$$/수식$$')
    if(R12 != 0):
        choice_list[index] = a.format(R3=R3, R12=R12, R13=R13, left='{left}', right='{right}')

    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, R12=R12, R13=R13, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-360
def realnum311_Stem_259():
    stem = "{f1}을 계산하면?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n"\
              "{f2}{f3}\n\n"

    f1 = conv('$$수식$$-`N1 sqrt {N2} `-`N3 sqrt {N4} `+` {`N5 sqrt {N6}} over {sqrt {N7}} `$$/수식$$', 'N', 1, 7)
    f2 = conv('$$수식$$=`-`R1 sqrt {R2} `-`R3 sqrt {R2} `+`R4 sqrt {R2}$$/수식$$', 'R', 1, 4)
    f3 = conv('$$수식$$`=`R5 sqrt {R2}$$/수식$$', 'R', 2, 5)
    sq = make_sqrt()
    N1 = make_exclude0(5)
    N2 = sq * pow(randint(1, 3), make_exponent())
    N3 = make_exclude0(5)
    N4 = sq * pow(randint(2, 4), 2)
    N5 = sq * make_exclude0(5)
    while True:
        N6 = make_sqrt()
        if(N6!=sq):
            break
    N7 = N6*sq
    R1 = N1 * int(math.sqrt(N2/sq))
    R2 = sq
    R3 = N3 * int(math.sqrt(N4/sq))
    R4 = int(N5/sq)
    R5 = -R1-R3+R4

    a = f3.replace('=', '')
    R5_list = make_choice(R5)
    index = R5_list.index(R5)
    choice_list = []
    for i in range(0, 5):
        if (R5_list[i] != 0):
            choice_list.append(a.format(R2=R2, R5=R5_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$$0$$/수식$$')

    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-361
def realnum311_Stem_260():
    stem = "{f1}을 계산하면?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n"\
              "{f2}{f3}\n"\
              "{f4}{f5}\n"\
              "{f6}\n\n"

    f1 = conv('$$수식$$`N1 sqrt {N2} `+` {N3} over {sqrt {N4}} `$$/수식$$', 'N', 1, 4)
    f2 = conv('$$수식$$`=`R1 sqrt {{1} over {R2}} `+` {R3} over {`R4 sqrt {R2}}$$/수식$$', 'R', 1, 5)
    f3 = conv('$$수식$$`=` {R1} over {sqrt {R2}} `+` {R3} over {`R4 sqrt {R2}}$$/수식$$', 'R', 1, 4)
    f4 = conv('$$수식$$=` {`R8 sqrt {R2}} over {R9} `+` {`R10 sqrt {R2}} over {R5}$$/수식$$', 'R', 2, 10)
    f5 = conv('$$수식$$`=`  ( {R8} over {R9} `+` {R10} over {R5}  ) ` sqrt {R2}$$/수식$$', 'R', 2, 10)
    f6 = conv('$$수식$$=` {`R6 sqrt {R2}} over {R7}$$/수식$$', 'R', 2, 7)

    sq = a = random.choice([2, 5])
    N1 = make_exclude0(5)
    N2 = 1/sq
    N3 = make_exclude0(5)
    N4 = sq * pow(randint(2, 4), 2)
    R1 = N1
    R2 = sq

    R3 = N3
    R4 = int(math.sqrt(N4/sq))
    red = Fraction(R3, R4)
    R3 = red.numerator
    R4 = red.denominator

    R5 = R2*R4
    red2 = Fraction(R3, R5)
    R10 = red2.numerator
    R5 = red2.denominator

    result = Fraction(R1, R2) + Fraction(R3, R5)
    # 분자
    R6 = result.numerator
    # 분모
    R7 = result.denominator

    red3 = Fraction(R1, R2)
    R8 = red3.numerator
    R9 = red3.denominator

    a = f6.replace('=', '')
    if(R7>3):
        R7_list = make_choice(R7)
    else:
        R7_list = [R7, R7+1, R7+1, R7+2, R7+3]
        random.shuffle(R7_list)
    R6_list = make_choice(R6)
    # 두 개 이상의 R 값을 바꾸는 경우 첫 번째에 옳은 R값이 할당된 index를 이용해 정답 생성
    index = R7_list.index(R7)
    choice_list = []
    for i in range(0, 5):
        if(R6_list[i]!=0):
            R6_list[i] = Fraction(R6_list[i], R7_list[i]).numerator
            R7_list[i] = Fraction(R6_list[i], R7_list[i]).denominator
            choice_list.append(a.format(R2=R2, R6=R6_list[i], R7=R7_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$$0$$/수식$$')
    if(R6 != 0):
        choice_list[index] = a.format(R2=R2, R6=R6, R7=R7, left='{left}', right='{right}')

    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-362
def realnum311_Stem_261():
    stem = "다음 중 옳{cond} 것을 모두 고르면? (정답 2개)\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "① {f1}\n" \
              "② {f2}\n" \
              "③ {f3}\n" \
              "④ {f4}\n" \
              "⑤ {f5}\n\n"

    cond = randint(0, 1)
    num = randint(2, 3)
    list = []
    a_list = []
    # 오답 3개 (정답 2개)
    if (cond == 0):
        w = 3
        wrong_list = random.sample([0, 1, 2, 3, 4], w)
        for i in range(0, num):
            # 오답인 index면 오답 생성(parameter로 True 전달)
            if (i in wrong_list):
                list.append(make_form_sqrt(1))
            else:
                list.append(make_form_sqrt())
                a_list.append(i)
        for i in range(num, 5):
            if (i in wrong_list):
                list.append(make_form_sqrt_frac(1))
            else:
                list.append(make_form_sqrt_frac())
                a_list.append(i)
    # 오답 2개
    else:
        w = 2
        wrong_list = random.sample([0, 1, 2, 3, 4], w)
        for i in range(0, num):
            # 오답인 index면 오답 생성(parameter로 True 전달)
            if (i in wrong_list):
                list.append(make_form_sqrt(1))
                a_list.append(i)
            else:
                list.append(make_form_sqrt())
        for i in range(num, 5):
            if (i in wrong_list):
                list.append(make_form_sqrt_frac(1))
                a_list.append(i)
            else:
                list.append(make_form_sqrt_frac())

    f1 = ''
    f2 = ''
    f3 = ''
    f4 = ''
    f5 = ''

    for i in range(0, len(list[0])-1):
        f1 += list[0][i]
    for i in range(0, len(list[1])-1):
        f2 += list[1][i]
    for i in range(0, len(list[2])-1):
        f3 += list[2][i]
    for i in range(0, len(list[3])-1):
        f4 += list[3][i]
    for i in range(0, len(list[4])-1):
        f5 += list[4][i]

    stem = stem.format(cond=make_cond[cond],
                       s1=list[0][0] + list[0][3], s2=list[1][0] + list[1][3], s3=list[2][0] + list[2][6 - num],
                       s4=list[3][0]+list[3][4], s5=list[4][0]+list[4][4])
    answer = answer.format(a=answer_dict[a_list[0]] + ', ' + answer_dict[a_list[1]])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-363
def realnum311_Stem_262():
    stem = "{f1}{f7}을 만족시키는 유리수 {a}에 대하여 {num}의 값을 구하시오.\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}{f2}\n" \
              "{f3}\n" \
              "{f4}\n" \
              "{f5}\n" \
              "{f6}{f7}" \
              "따라서 {f8}이므로 {f9}\n\n"

    f1 = conv('$$수식$$sqrt {{N1} over {N2}} `-` {N3} over {sqrt {N4}} `+`N5 sqrt {N6}$$/수식$$', 'N', 1, 6)
    f2 = conv('$$수식$$=` {sqrt {R1}} over {R2} `-` {R3} over {`R4 sqrt {R1}} `+`R5 sqrt {R1}$$/수식$$', 'R', 1, 6)
    f3 = conv('$$수식$$=` {sqrt {R1}} over {R2} `-` {`R3 sqrt {R1}} over {`R4 sqrt {R1} TIMES sqrt {R1}} `+`R5 sqrt {R1}$$/수식$$', 'R', 1, 6)
    f4 = conv('$$수식$$=` {sqrt {R1}} over {R2} `-` {`R3 sqrt {R1}} over {R6} `+`R5 sqrt {R1}$$/수식$$', 'R', 1, 6)
    f5 = conv('$$수식$$=`  ( {1} over {R2} `-` {R3} over {R6} `+`R5 ) ` sqrt {R1}$$/수식$$', 'R', 1, 6)
    f6 = conv('$$수식$$=` {`R7 sqrt {R1}} over {R8}$$/수식$$', 'R', 1, 8)
    f7 = conv('$$수식$$`=`a sqrt {R1}$$/수식$$', 'R', 1, 1)
    f8 = conv('$$수식$$a`=` {R7} over {R8} `$$/수식$$', 'R', 7, 8)
    f9 = conv('$$수식$$`R8 a`=`R7$$/수식$$', 'R', 7, 8)
    num = conv('$$수식$$`R8 a`$$/수식$$', 'R', 8, 8)

    N1 = make_sqrt(5)
    while True:
        N2 = pow(randint(2, 3), 2)
        if(pow(N1, 2)!=N2):
            break
    N3 = make_exclude0(5)
    N4 = N1 * N2
    N5 = make_exclude0(5)
    N6 = N1 * pow(randint(1, 3), make_exponent())
    R1 = N1
    R2 = int(math.sqrt(N2))
    red1 = Fraction(N3, R2)
    R3 = red1.numerator
    R4 = red1.denominator
    R5 = N5 * int(math.sqrt(N6 / N1))
    R6 = R1 * R4
    red2 = Fraction(1, R2) - Fraction(R3, R6) + R5
    R7 = red2.numerator
    R8 = red2.denominator

    a = R7

    stem = stem.format(f1=f1, f7=f7, a='$$수식$$a$$/수식$$', num=num) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, R1=R1, R8=R8, left=left, right=right)
    answer = answer.format(a=a)
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, \
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-364
def realnum311_Stem_263():
    stem = "{f1}이고 {f2}일 때, {b}는 {a}의 몇 배인가?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f2}{f3}{f4}\n" \
              "{f5}{f6}\n"\
              "따라서 {b}는 {a}의 {f7}배이다.\n\n"

    f1 = conv('$$수식$$a`=` sqrt {N1} `$$/수식$$', 'N', 1, 1)
    f2 = conv('$$수식$$b`=`a`-` {N2} over {a} `$$/수식$$', 'N', 2, 2)
    f3 = conv('$$수식$$`=` sqrt {N1} `-` {N2} over {sqrt {N1}}$$/수식$$', 'N', 1, 2)
    f4 = conv('$$수식$$`=` sqrt {N1} `-` {`N2 sqrt {N1}} over {N1} `$$/수식$$', 'N', 1, 2)
    f5 = conv('$$수식$$=` {R1 sqrt {R2}} over {R2}$$/수식$$', 'R', 1, 2)
    f6 = conv('$$수식$$`=` {R1} over {R2} a$$/수식$$', 'R', 1, 2)
    f7 = conv('$$수식$${R1} over {R2}$$/수식$$', 'R', 1, 2)

    N1 = random.choice([2, 3, 5, 6, 7, 10, 11, 13, 14, 15])
    N2 = make_exclude0(1)

    red = Fraction(N1-N2, N1)
    R1 = red.numerator
    R2 = red.denominator

    a = f7.replace('=', '')
    if(R2>3):
        R2_list = make_choice(R2)
    else:
        R2_list = [R2, R2+1, R2+1, R2+2, R2+3]
        random.shuffle(R2_list)
    R1_list = make_choice(R1)
    index = R2_list.index(R2)
    choice_list = []
    for i in range(0, 5):
        if(R1_list[i]!=0):
            R1_list[i] = Fraction(R1_list[i], R2_list[i]).numerator
            R2_list[i] = Fraction(R1_list[i], R2_list[i]).denominator
            choice_list.append(a.format(R1=R1_list[i], R2=R2_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$$0$$/수식$$')
    if(R1 != 0):
        choice_list[index] = a.format(R1=R1, R2=R2, left='{left}', right='{right}')

    stem = stem.format(f1=f1, f2=f2, b='$$수식$$b$$/수식$$', a='$$수식$$a$$/수식$$', s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, R1=R1, R2=R2, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, b='$$수식$$b$$/수식$$', a='$$수식$$a$$/수식$$', f7=f7)\
        .format(N1=N1, N2=N2,\
                R1=R1, R2=R2, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-365
def realnum311_Stem_264():
    stem = "{f1}, {f2}일 때, {f3}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f4}\n"\
              "{f5}\n"\
              "{f6}\n" \
              "{f7}\n"\
              "{f8}\n\n"

    f1 = conv('$$수식$$x`=` sqrt {N1} `+`N2`$$/수식$$', 'N', 1, 2)
    f2 = conv('$$수식$$y`=` sqrt {N1} `-`N2`$$/수식$$', 'N', 1, 2)
    f3 = conv('$$수식$${1} over {x`+`y} `-` {N3} over {x`-`y} `$$/수식$$', 'N', 3, 3)
    f4 = conv('$$수식$$x`+`y`=`( sqrt {N1} `+`N2)`+`( sqrt {N1} `-`N2)`=`2 sqrt {N1}$$/수식$$', 'N', 1, 2)
    f5 = conv('$$수식$$x`-`y`=`( sqrt {N1} `+`N2)`-`( sqrt {N1} `-`N2)`=`N4$$/수식$$', 'N', 1, 4)
    f6 = conv('$$수식$$THEREFORE~ {1} over {x`+`y} `-` {N3} over {x`-`y} `=` {1} over {2 sqrt {N1}} `-` {N3} over {N4}$$/수식$$', 'N', 1, 4)
    f7 = conv('$$수식$$=` {sqrt {R1}} over {R2} `-` {R3} over {R4}$$/수식$$', 'R', 1, 4)
    f8 = conv('$$수식$$=` {`R5 sqrt {R1} `-`R6} over {R7}$$/수식$$', 'R', 1, 7)

    N1 = make_sqrt()
    N2 = randint(1, 5)
    N3 = make_exclude0(1)
    N4 = 2*N2
    R1 = N1
    R2 = 2*N1
    R3 = N3
    R4 = N4

    red = Fraction(R2, R4)
    R5 = red.denominator
    R6 = R3 * red.numerator
    R7 = R2*R5

    a = f8.replace('=', '')

    R6_list = make_choice(R6)
    index = R6_list.index(R6)
    choice_list = []
    for i in range(0, 5):
        if(R6_list[i]!=0):
            choice_list.append(a.format(R1=R1, R5=R5, R6=R6_list[i], R7=R7, left='{left}', right='{right}'))
        else:
            choice_list.append(conv('$$수식$$` {`R5 sqrt {R1}} over {R7}$$/수식$$', 'R', 1, 7).format(R1=R1, R5=R5, R7=R7, left='{left}', right='{right}'))

    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f4=f4, f5=f5, f6=f6, f7=f7, f8=f8)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-366
def realnum311_Stem_265():
    stem = "{f1}, {f2}일 때, {f3}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f3}{f4}{f5}\n" \
              "{f6}\n\n"

    f1 = conv('$$수식$$a`=` sqrt {N1}$$/수식$$', 'N', 1, 1)
    f2 = conv('$$수식$$b`=` sqrt {N2}$$/수식$$', 'N', 2, 2)
    f3 = conv('$$수식$${b} over {a} `+` {`N3 a} over {b} `$$/수식$$', 'N', 3, 3)
    f4 = conv('$$수식$$`=` {sqrt {N2}} over {sqrt {N1}} `+` {`N3 sqrt {N1}} over {sqrt {N2}} $$/수식$$', 'N', 1, 3)
    f5 = conv('$$수식$$`=` {sqrt {N4}} over {N1} `+` {`N3 sqrt {N4}} over {N2} `$$/수식$$', 'N', 1, 4)
    f6 = conv('$$수식$$=` {`R2 sqrt {R1}} over {R3}$$/수식$$', 'R', 1, 3)

    N1 = random.choice([2, 3, 5, 7, 11])
    while True:
        N2 = random.choice([2, 3, 5, 7, 11])
        if(N2!=N1):
            break
    N3 = make_exclude0(1)
    N4 = N1*N2
    R1 = N4

    red = Fraction(1, N1) + Fraction(N3, N2)
    R2 = red.numerator
    R3 = red.denominator

    a = f6.replace('=', '')
    R2_list = make_choice(R2)
    index = R2_list.index(R2)
    choice_list = []
    for i in range(0, 5):
        if(R2_list[i]!=0):
            red2 = Fraction(R2_list[i], R3)
            choice_list.append(a.format(R1=R1, R2=red2.numerator, R3=red2.denominator, left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$$0$$/수식$$')

    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f3=f3, f4=f4, f5=f5, f6=f6) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4,
                R1=R1, R2=R2, R3=R3, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-368
def realnum311_Stem_266():
    stem = "{f1}의 값을 구하시오.\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n"\
              "{f2}\n"\
              "{f3}\n" \
              "{f4}{f5}\n\n"

    f1 = conv('$$수식$${`N3 sqrt {N2} `+`N4 sqrt {N1}} over {sqrt {N1}} `-` {`N7 sqrt {N6} `-`N8 sqrt {N5}} over {sqrt {N5}} `$$/수식$$', 'N', 1, 8)
    f2 = conv('$$수식$$=` {(`R3 sqrt {R2} `+`R4 sqrt {R1} ) TIMES sqrt {R1}} over {sqrt {R1} TIMES sqrt {R1}} - {(R5 sqrt {R1} `-`R6 sqrt {R2} ) TIMES sqrt {R2}} over {sqrt {R2} TIMES sqrt {R2}}$$/수식$$', 'R', 1, 6)
    f3 = conv('$$수식$$=` {`R3 sqrt {R7} `+`R8} over {R1} `-` {`R5 sqrt {R7} `-`R9} over {R2}$$/수식$$', 'R', 1, 9)
    f4 = conv('$$수식$$=`R10 sqrt {R7} `+`R4`-`R11 sqrt {R7} `+`R6$$/수식$$', 'R', 4, 11)
    f5 = conv('$$수식$$`=`R12$$/수식$$', 'R', 12, 12)

    N1 = make_sqrt()
    while True:
        N5 = make_sqrt()
        if(N5 != N1):
            break
    N2 = N5 * pow(N1, 2)
    N3 = randint(1, 5)
    N4 = make_exclude0(5)
    N6 = N1 * pow(N5, 2)
    N7 = N3
    N8 = make_exclude0(5)
    R1 = N1
    R2 = N5
    R3 = N3 * N1
    R4 = N4
    R5 = N7 * N5
    R6 = N8
    R7 = R1 * R2
    R8 = R1 * R4
    R9 = R2 * R6
    R10 = N3
    R11 = N7
    R12 = R4 + R6

    a = f5.replace('=', '').format(R12=R12)
    stem = stem.format(f1=f1)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, left=left, right=right)
    answer = answer.format(a=a)
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, R12=R12, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-369
def realnum311_Stem_267():
    stem = "{f1}을 계산하면?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n"\
              "{f2}\n"\
              "{f3}\n" \
              "{f4}{f5}\n\n"

    f1 = conv('$$수식$$` {`N2 sqrt {N1} `-`N3} over {sqrt {N1}} `+`N4 sqrt {N1}$$/수식$$', 'N', 1, 4)
    f2 = conv('$$수식$$=` {(`N2 sqrt {N1} `-`N3)` TIMES` sqrt {N1}} over {sqrt {N1} ` TIMES` sqrt {N1}} `+`N4 sqrt {N1}$$/수식$$', 'N', 1, 4)
    f3 = conv('$$수식$$=` {`R2`-`R3 sqrt {R1}} over {R1} `+`R4 sqrt {R1}$$/수식$$', 'R', 1, 4)
    f4 = conv('$$수식$$=`R6`-`R5 sqrt {R1} `+`R4 sqrt {R1} `$$/수식$$', 'R', 1, 6)
    f5 = conv('$$수식$$=`R6`-`R7 sqrt {R1}$$/수식$$', 'R', 1, 7)

    N1 = make_sqrt()
    N2 = randint(1, 5)
    N3 = N1 * make_exclude0(5)
    N4 = make_exclude0(5)
    R1 = N1
    R2 = N1 * N2
    R3 = N3
    R4 = N4
    R5 = int(N3/N1)
    R6 = N2
    R7 = R5-R4

    a = f5.replace('=', '')
    R6_list = make_choice_exclude0(R6)
    R7_list = make_choice(R7)
    # 두 개 이상의 R 값을 바꾸는 경우 첫 번째에 옳은 R값이 할당된 index를 이용해 정답 생성
    index = R6_list.index(R6)
    choice_list = []
    for i in range(0, 5):
        if (R7_list[i] != 0):
            choice_list.append(a.format(R1=R1, R6=R6_list[i], R7=R7_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$$`{R6}$$/수식$$'.format(R6=R6_list[i]))
    if (R7 != 0):
        choice_list[index] = a.format(R1=R1, R6=R6, R7=R7, left='{left}', right='{right}')
    else:
        choice_list[index] = '$$수식$$`{R6}$$/수식$$'.format(R6=R6)

    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5='='+choice_list[index])\
        .format(N1=N1, N2=N2, N3=N3, N4=N4,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-370
def realnum311_Stem_268():
    stem = "{f1}을 간단히 하면 {f6}일 때, 유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$a`+`b`$$/수식$$의 값을 구하시오.\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}{f2}\n"\
              "{f3}\n" \
              "{f4}\n"\
              "{f5}{f6}\n"\
              "따라서 {f7}, {f8}이므로\n"\
              "{f9}{f10}\n\n"

    f1 = conv('$$수식$$sqrt {N1} `-` {`N2 sqrt {N3} `-`N4} over {sqrt {N5}} `$$/수식$$', 'N', 1, 5)
    f2 = conv('$$수식$$=`R1`-` {(R2 sqrt {R3} `-`R4) TIMES sqrt {R3}} over {sqrt {R3} TIMES sqrt {R3}}$$/수식$$', 'R', 1, 4)
    f3 = conv('$$수식$$=`R1`-` {R5`-`R4 sqrt {R3}} over {R3}$$/수식$$', 'R', 1, 5)
    f4 = conv('$$수식$$=`R1`-`(R6`-`R7 sqrt {R3} )$$/수식$$', 'R', 1, 7)
    f5 = conv('$$수식$$=`R8`+`R7 sqrt {R3}$$/수식$$', 'R', 3, 8)
    f6 = conv('$$수식$$=`a`+`b sqrt {R3} `$$/수식$$', 'R', 3, 3)
    f7 = conv('$$수식$$a`=`R8`$$/수식$$', 'R', 8, 8)
    f8 = conv('$$수식$$b`=`R7`$$/수식$$', 'R', 7, 7)
    f9 = conv('$$수식$$a`+`b`=`R8`+`R7$$/수식$$', 'R', 7, 8)
    f10 = conv('$$수식$$`=`R9$$/수식$$', 'R', 9, 9)

    N1 = pow(make_sqrt(5), 2)
    N2 = randint(1, 5)
    N5 = make_sqrt()
    N3 = N5 * pow(randint(2, 3), 2)
    N4 = N5 * make_exclude0(5)
    R1 = int(math.sqrt(N1))
    R2 = N2 * int(math.sqrt(N3/N5))
    R3 = N5
    R4 = N4
    R5 = R2 * R3
    R6 = R2
    R7 = int(R4/R3)
    R8 = R1 - R6
    R9 = R7 + R8

    a = f10.replace('=', '')

    stem = stem.format(f1=f1, f6=f6) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, R3=R3, left=left, right=right)
    answer = answer.format(a=a).format(R9=R9)
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-371
def realnum311_Stem_269():
    stem = "{f1}, {f2}일 때, {f3}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f4}\n"\
              "{f5}\n"\
              "{f6}\n" \
              "{f7}\n"\
              "따라서 {f8}이므로\n"\
              "{f9}{f10}\n\n"

    f1 = conv('$$수식$$x`=` {N1`+`N2 sqrt {N3}} over {sqrt {N4}}$$/수식$$', 'N', 1, 4)
    f2 = conv('$$수식$$y`=` {N1`-`N2 sqrt {N3}} over {sqrt {N4}} `$$/수식$$', 'N', 1, 4)
    f3 = conv('$$수식$$sqrt {N4} (x`+`y)`$$/수식$$', 'N', 4, 4)
    f4 = conv('$$수식$$x`=` {N1`+`N2 sqrt {N3}} over {sqrt {N4}} `=` {(N1`+`N2 sqrt {N3} )` TIMES` sqrt {N4}} over {sqrt {N4} ` TIMES` sqrt {N4}}$$/수식$$', 'N', 1, 4)
    f5 = conv('$$수식$$=` {`R1 sqrt {R2} `+`R3 sqrt {R4}} over {R2}$$/수식$$', 'R', 1, 4)
    f6 = conv('$$수식$$y`=` {N1`-`N2 sqrt {N3}} over {sqrt {N4}} `=` {(N1`-`N2 sqrt {N3} )` TIMES` sqrt {N4}} over {sqrt {N4} ` TIMES` sqrt {N4}}$$/수식$$', 'N', 1, 4)
    f7 = conv('$$수식$$=` {`R1 sqrt {R2} `-`R3 sqrt {R4}} over {R2}$$/수식$$', 'R', 1, 4)
    f8 = conv('$$수식$$x`+`y`=`R5 sqrt {R2} `$$/수식$$', 'R', 2, 5)
    f9 = conv('$$수식$$sqrt {R2} (x`+`y)`=` sqrt {R2} ` TIMES`R5 sqrt {R2} `$$/수식$$', 'R', 2, 5)
    f10 = conv('$$수식$$=`R6$$/수식$$', 'R', 6, 6)

    N4 = make_sqrt()
    N1 = N4 * randint(1, 3)
    N2 = make_exclude0(5)
    while True:
        N3 = make_sqrt()
        if(N3 != N4):
            break
    R1 = N1
    R2 = N4
    R3 = N2
    R4 = N3 * N4
    R5 = 2 * int(R1 / R2)
    R6 = R2 * R5

    sel = conv('$$수식$$R6 sqrt {R2}$$/수식$$', 'R', 2, 6)
    a = f10.replace('=', '')
    R6_list = make_choice(R6)
    R2_list = [1, R2]
    index = R6_list.index(R6)
    choice_list = []

    for i in range(5):
        R2_temp = R2_list[randint(0, 1)]
        if(R2_temp == 1):
            choice_list.append(a.format(R6=R6_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append(sel.format(R2=R2, R6=R6_list[i], left='{left}', right='{right}'))
    choice_list[index] = a.format(R6=R6, left='{left}', right='{right}')

    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-372
def realnum311_Stem_270():
    stem = "{f1}을 계산하면?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n"\
              "{f2}\n"\
              "{f3}\n" \
              "{f4}\n"\
              "{f5}\n\n"

    f1 = conv('$$수식$${N1`+`N2 sqrt {N3}} over {sqrt {N4}} `-` {N5`+`N2 sqrt {N6}} over {sqrt {N7}} `$$/수식$$', 'N', 1, 7)
    f2 = conv('$$수식$$=` {(N1`+`N2 sqrt {N3} ) TIMES sqrt {N4}} over {sqrt {N4} TIMES sqrt {N4}} `-` {(N5`+`N2 sqrt {N6} ) TIMES sqrt {N7}} over {sqrt {N7} TIMES sqrt {N7}}$$/수식$$', 'N', 1, 7)
    f3 = conv('$$수식$$=` {`R1 sqrt {R2} `+`R3 sqrt {R4}} over {R2} `-` {`R5 sqrt {R6} `+`R7 sqrt {R4}} over {R6}$$/수식$$', 'R', 1, 7)
    f4 = conv('$$수식$$=`(`R8 sqrt {R2} `+`R9 sqrt {R4} )`-`(`R10 sqrt {R6} `+`R9 sqrt {R4} )$$/수식$$', 'R', 2, 10)
    f5 = conv('$$수식$$=`R8 sqrt {R2} `-`R10 sqrt {R6}$$/수식$$', 'R', 2, 10)

    N4, N7, R4 = random.sample([2, 3, 5], 3)
    N1 = N4 * randint(2, 4)
    N2 = make_exclude0(1)
    N3 = N4 * R4
    N5 = N7 * randint(2, 4)
    N6 = N7 * R4
    R1 = N1
    R2 = N4
    R3 = N2 * N4
    R5 = N5
    R6 = N7
    R7 = N2 * N7
    R8 = int(N1/N4)
    R9 = N2
    R10 = int(N5/N7)

    a = f5.replace('=', '')

    R8_list = make_choice_exclude0(R8)
    R10_list = make_choice_exclude0(R10)
    index = R8_list.index(R8)
    choice_list = []
    for i in range(5):
        R2_temp, R6_temp = random.sample([N4, N7, R4], 2)
        choice_list.append(a.format(R2=R2_temp, R6=R6_temp, R8=R8_list[i], R10=R10_list[i], left='{left}', right='{right}'))
    choice_list[index] = a.format(R2=R2, R6=R6, R8=R8, R10=R10, left='{left}', right='{right}')

    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-373
def realnum311_Stem_271():
    stem = "{f1}, {f2}일 때, {f3}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f4}\n"\
              "{f5}\n"\
              "{f6}\n" \
              "{f7}\n"\
              "따라서 {f8}이므로\n"\
              "{f9}{f10}\n\n"

    f1 = conv('$$수식$$x`=` {sqrt {N1} `+`N3 sqrt {N2}} over {sqrt {N1}} `$$/수식$$', 'N', 1, 3)
    f2 = conv('$$수식$$y`=` {sqrt {N1} `-`N3 sqrt {N2}} over {sqrt {N1}} `$$/수식$$', 'N', 1, 3)
    f3 = conv('$$수식$${x`+`y} over {`R5 (x`-`y)} `$$/수식$$', 'R', 5, 5)
    f4 = conv('$$수식$$x`=` {sqrt {N1} `+`N3 sqrt {N2}} over {sqrt {N1}} `=` {( sqrt {N1} `+`N3 sqrt {N2} )` TIMES` sqrt {N1}} over {sqrt {N1} ` TIMES` sqrt {N1}}$$/수식$$', 'N', 1, 3)
    f5 = conv('$$수식$$=` {R1`+`R3 sqrt {R2}} over {R1}$$/수식$$', 'R', 1, 3)
    f6 = conv('$$수식$$y`=` {sqrt {N1} `-`N3 sqrt {N2}} over {sqrt {N1}} `=` {( sqrt {N1} `-`N3 sqrt {N2} )` TIMES` sqrt {N1}} over {sqrt {N1} ` TIMES` sqrt {N1}}$$/수식$$', 'N', 1, 3)
    f7 = conv('$$수식$$=` {R1`-`R3 sqrt {R2}} over {R1}$$/수식$$', 'R', 1, 3)
    f8 = conv('$$수식$$x`+`y`=`2,~x`-`y`=` {`R4 sqrt {R2}} over {R5} `$$/수식$$', 'R', 2, 5)
    f9 = conv('$$수식$${x`+`y} over {`R5 (x`-`y)} `=` {2} over {`R4 sqrt {R2}} `$$/수식$$', 'R', 2, 5)
    f10 = conv('$$수식$$=` {`R6 sqrt {R2}} over {R7}$$/수식$$', 'R', 2, 7)

    N1, N2 = random.sample([2, 3, 5, 7], 2)
    N3 = make_exclude0(1)
    R1 = N1
    R2 = N1 * N2
    R3 = N3
    red = Fraction(2*R3, R1)
    R4 = red.numerator
    R5 = red.denominator
    red2 = Fraction(2, R2 * R4)
    R6 = red2.numerator
    R7 = red2.denominator


    sel = conv('$$수식$${R6} over {R7}$$/수식$$', 'R', 6, 7)
    a = f10.replace('=', '')
    R7_list = make_choice_exclude0(R7)
    R2_list = [1, N1, N2, R2]
    index = R7_list.index(R7)
    choice_list = []

    for i in range(5):
        R2_temp = R2_list[randint(0, 3)]
        if(R2_temp == 1):
            choice_list.append(sel.format(R6=1, R7=R7_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append(a.format(R2=R2_temp, R6=R6, R7=R7_list[i], left='{left}', right='{right}'))
    choice_list[index] = a.format(R2=R2, R6=R6, R7=R7, left='{left}', right='{right}')

    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, R5=R5, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10)\
        .format(N1=N1, N2=N2, N3=N3,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-374
def realnum311_Stem_272():
    stem = "자연수 $$수식$$x$$/수식$$에 대하여 $$수식$$sqrt {x}$$/수식$$의 소수 부분을 $$수식$$f`(x)`$$/수식$$라 할 때, {f1}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f2}이므로 {f3}의 소수 부분은 {f4}이다.\n"\
              "{f5}\n"\
              "또 {f6}이므로 {f7}의 소수 부분은 {f8}이다.\n"\
              "{f9}\n" \
              "{f10}{f11}{f12}\n"\
              "{f13}\n"\
              "{f14}{f15}\n\n"

    f1 = conv('$$수식$${`N3 f(N1)} over {f(N2)`+`N4}$$/수식$$', 'N', 1, 4)
    f2 = conv('$$수식$$R2`&lt;` sqrt {R1} `&lt;`R3`$$/수식$$', 'R', 1, 3)
    f3 = conv('$$수식$$sqrt {R1} `$$/수식$$', 'R', 1, 1)
    f4 = conv('$$수식$$sqrt {R1} `-`R2`$$/수식$$', 'R', 1, 2)
    f5 = conv('$$수식$$THEREFORE~f(R1)`=`R4 sqrt {R5} `-`R2$$/수식$$', 'R', 1, 5)
    f6 = conv('$$수식$$R7`&lt;` sqrt {R6} `&lt;`R8`$$/수식$$', 'R', 6, 8)
    f7 = conv('$$수식$$sqrt {R6} `$$/수식$$', 'R', 6, 6)
    f8 = conv('$$수식$$sqrt {R6} `-`R7`$$/수식$$', 'R', 6, 7)
    f9 = conv('$$수식$$THEREFORE~f(R6)`=`R9 sqrt {R10} `-`R7$$/수식$$', 'R', 6, 10)
    f10 = conv('$$수식$$THEREFORE~ {`N3 f(N1)} over {f(N2)`+`N4}$$/수식$$', 'N', 1, 4)
    f11 = conv('$$수식$$=` {`R11(`R4 sqrt {R5} `-`R2)} over {(`R9 sqrt {R10} `-`R7)`+`R7} `$$/수식$$', 'R', 2, 11)
    f12 = conv('$$수식$$=` {`R12 sqrt {R10} `-`R13} over {`R9 sqrt {R10}}$$/수식$$', 'R', 9, 13)
    f13 = conv('$$수식$$=` {`R14 sqrt {R10} `-`R15} over {sqrt {R10}} `=` {(`R14 sqrt {R10} `-`R15) TIMES sqrt {R10}} over {sqrt {R10} TIMES sqrt {R10}}$$/수식$$', 'R', 10, 15)
    f14 = conv('$$수식$$=` {`R16`-`R15 sqrt {R10}} over {R10} `$$/수식$$', 'R', 10, 18)
    f15 = conv('$$수식$$=`R17`-`R18 sqrt {R10}$$/수식$$', 'R', 10, 18)

    sq = make_sqrt(5)
    N1 = sq * pow(randint(1, 3), 2)
    while True:
        N2 = sq * pow(randint(1, 3), 2)
        if(N2 != N1):
            break

    R1 = N1
    R2 = math.floor(math.sqrt(N1))
    R3 = R2 + 1
    R4 = int(math.sqrt(N1/sq))
    R5 = sq

    R6 = N2
    R7 = math.floor(math.sqrt(N2))

    N4 = R7

    R8 = R7 + 1
    R9 = int(math.sqrt(N2/sq))

    N3 = R9 * R5 * randint(1, 2)

    R10 = R5

    R11 = N3
    R12 = R4 * R11
    R13 = R2 * R11
    R14 = int(R12/R9)
    R15 = int(R13/R9)
    R16 = R10 * R14
    R17 = int(R16/R10)
    R18 = int(R15/R10)

    a = f15.replace('=', '')

    R17_list = make_choice_exclude0(R17)
    R18_list = make_choice_exclude0(R18)
    index = R17_list.index(R17)
    choice_list = []
    for i in range(5):
        choice_list.append(a.format(R10=R10, R17=R17_list[i], R18=R18_list[i], left='{left}', right='{right}'))
    choice_list[index] = a.format(R10=R10, R17=R17, R18=R18, left='{left}', right='{right}')

    stem = stem.format(f1=f1, x='{x}', s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(x='{x}', N1=N1, N2=N2, N3=N3, N4=N4, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10, f11=f11, f12=f12, f13=f13, f14=f14, f15=f15)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4,
        R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, R12=R12, R13=R13, R14=R14, R15=R15, R16=R16, R17=R17, R18=R18, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-377
def realnum311_Stem_273():
    stem = "{f1}, {f2}일 때, {f3}의 값은 {f4}이다. 유리수 $$수식$$a,~b`$$/수식$$에 대하여 $$수식$$a`+`b`$$/수식$$의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f5},\n"\
              "{f6}이므로\n"\
              "{f7}\n" \
              "{f8}\n"\
              "{f9}\n"\
              "{f10}\n"\
              "따라서 {f11}, {f12}이므로\n"\
              "$$수식$$a`+`b`=`$$/수식$${f13}\n\n"

    f1 = conv('$$수식$$x`=` {sqrt {N2} `+`N3 sqrt {N4}} over {sqrt {N1}} `$$/수식$$', 'N', 1, 4)
    f2 = conv('$$수식$$y`=` {sqrt {N6} `-`N7 sqrt {N8}} over {sqrt {N5}} `$$/수식$$', 'N', 5, 8)
    f3 = conv('$$수식$${x`-`R16 y} over {`R16 x`+`y} `$$/수식$$', 'R', 16, 16)
    f4 = conv('$$수식$$a sqrt {R5} `+`b`$$/수식$$', 'R', 5, 5)
    f5 = conv('$$수식$$x`=` {`R2 sqrt {R3} `+`R4 sqrt {R1}} over {sqrt {R1}} `=` {`R2 sqrt {R5} `+R6} over {R1} `=`R7 sqrt {R5} `+`R8$$/수식$$', 'R', 1, 8)
    f6 = conv('$$수식$$y`=` {`R10 sqrt {R11} `-`R12 sqrt {R9}} over {sqrt {R9}} `=` {`R10 sqrt {R5} `-`R13} over {R9} `=`R14 sqrt {R5} `-`R15$$/수식$$', 'R', 5, 15)
    f7 = conv('$$수식$$`R16 x`+`y`=`R16 (`R7 sqrt {R5} `+`R8)`+`(`R14 sqrt {R5} `-`R15)`=`R17 sqrt {R5}$$/수식$$', 'R', 5, 17)
    f8 = conv('$$수식$$x`-`R16 y`=`(`R7 sqrt {R5} `+`R8)`-`R16 (`R14 sqrt {R5} `-`R15)`=`R18`-`R19 sqrt {R5}$$/수식$$', 'R', 5, 19)
    f9 = conv('$$수식$$THEREFORE~ {x`-`R16 y} over {`R16 x`+`y} `=` {`R18`-`R19 sqrt {R5}} over {`R17 sqrt {R5}} `=` {`R18 sqrt {R5} `-`R20} over {R21} `$$/수식$$', 'R', 5, 21)
    f10 = conv('$$수식$$=` {`R23 sqrt {R5}} over {R22} `-` {R25} over {R24}$$/수식$$', 'R', 5, 25)
    f11 = conv('$$수식$$a`=` {R23} over {R22}$$/수식$$', 'R', 22, 23)
    f12 = conv('$$수식$$b`=`-{R25} over {R24}$$/수식$$', 'R', 24, 25)
    f13 = conv('$$수식$${R27} over {R26}$$/수식$$', 'R', 26, 27)

    N1 = make_sqrt(5)
    while True:
        N5 = make_sqrt(5)
        if(N5 != N1):
            break
    N2 = N5 * pow(N1, 2)
    N3 = make_exclude0(1)

    rand = randint(1, 2)
    N4 = N1 * pow(rand, 2)
    N6 = N1 * pow(N5, 2)
    N7 = N3
    N8 = N5 * pow(rand * randint(2, 3), 2)

    R1 = N1
    R2 = int(math.sqrt(N2/N5))
    R3 = N5
    R4 = N3 * int(math.sqrt(N4/N1))
    R5 = R1 * R3
    R6 = R1 * R4
    R7 = int(R2/R1)
    R8 = R4

    R9 = N5
    R10 = int(math.sqrt(N6/N1))
    R11 = R1
    R12 = N7 * int(math.sqrt(N8/N5))
    R13 = R9 * R12
    R14 = int(R10/R9)
    R15 = R12

    R16 = int(R15/R8)

    R17 = R7 * R16 + R14
    R18 = R8 + R15 * R16
    R19 = R14 * R16 - R7
    R20 = R5 * R19
    R21 = R5 * R17

    red = Fraction(R18, R21)
    R22 = red.denominator
    R23 = red.numerator
    red2 = Fraction(R20, R21)
    R24 = red2.denominator
    R25 = red2.numerator
    red3 = Fraction(R23, R22) - Fraction(R25, R24)
    R26 = red3.denominator
    R27 = red3.numerator

    R26_list = make_choice_exclude0(R26)
    R27_list = make_choice(R27)
    index = R27_list.index(R27)
    choice_list = []
    for i in range(5):
        red_temp = Fraction(R27_list[i], R26_list[i])
        choice_list.append(f13.format(R26=red_temp.denominator, R27=red_temp.numerator, left='{left}', right='{right}'))
    choice_list[index] = f13.format(R26=R26, R27=R27, left='{left}', right='{right}')

    stem = stem.format(f1=f1, f2=f2, f3=f3, f4=f4, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, R5=R5, R16=R16, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10, f11=f11, f12=f12, f13=f13)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, R12=R12, R13=R13, R14=R14, \
                R15=R15, R16=R16, R17=R17, R18=R18, R19=R19, R20=R20, R21=R21, R22=R22, R23=R23, R24=R24, R25=R25, R26=R26, R27=R27, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-378
def realnum311_Stem_274():
    stem = "$$수식$$a&gt;0,~b&gt;0`$$/수식$$이고 {f1}, {f2}일 때, {f3}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f4}\n"\
              "{f5}{f6}\n\n"

    f1 = conv('$$수식$$a`+`b`=`N1$$/수식$$', 'N', 1, 1)
    f2 = conv('$$수식$$ab`=`N2`$$/수식$$', 'N', 2, 2)
    f3 = conv('$$수식$$sqrt {{b} over {a}} `+` sqrt {{a} over {b}} `$$/수식$$', 'N', 0, 0)
    f4 = conv('$$수식$$sqrt {{b} over {a}} `+` sqrt {{a} over {b}} `=` {sqrt {b}} over {sqrt {a}} `+` {sqrt {a}} over {sqrt {b}} `=` {a`+`b} over {sqrt {ab}}$$/수식$$', 'N', 0, 0)
    f5 = conv('$$수식$$=` {N1} over {sqrt {N2}} `$$/수식$$', 'N', 1, 2)
    f6 = conv('$$수식$$=`R1$$/수식$$', 'R', 1, 1)

    N2 = pow(randint(2, 5), 2)
    N1 = N2 * randint(1, 4)
    R1 = int(N1/N2) * int(math.sqrt(N2))
    R2 = R1

    sel = conv('$$수식$$`R2 sqrt {R3}$$/수식$$', 'R', 2, 3)
    a = f6.replace('=', '')
    R2_list = make_choice_exclude0(R2)
    R3_list = [1, 2, 3, 5]
    index = R2_list.index(R2)
    choice_list = []
    for i in range(5):
        R3_temp = R3_list[randint(0, 1)]
        if(R3_temp == 1):
            choice_list.append(a.format(R1=R2_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append(sel.format(R2=R2_list[i], R3=R3_temp, left='{left}', right='{right}'))
    choice_list[index] = a.format(R1=R1, left='{left}', right='{right}')

    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f4=f4, f5=f5, f6=f6)\
        .format(N1=N1, N2=N2,\
                R1=R1, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-381
def realnum311_Stem_275():
    stem = "{f1}을 계산하면?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n"\
              "{f2}\n"\
              "{f3}\n\n"

    f1 = conv('$$수식$$`N1 sqrt {N2} (N3`-`N4 sqrt {N5} )`+` {N6} over {sqrt {N2}} `-` sqrt {N7} `$$/수식$$', 'N', 1, 7)
    f2 = conv('$$수식$$=`R1 sqrt {R2} `-`R3`+`R4 sqrt {R2} `-`R5 sqrt {R2}$$/수식$$', 'R', 1, 5)
    f3 = conv('$$수식$$=`R6 sqrt {R2} `-`R7$$/수식$$', 'R', 2, 7)

    N1 = randint(1, 3)
    N2 = make_sqrt()
    N3 = randint(1, 3)
    N4 = make_exclude0(3)
    N5 = N2
    N6 = N2 * randint(1, 3)
    N7 = N2 * pow(randint(2, 3), 2)

    R1 = N1 * N3
    R2 = N2
    R3 = N1 * N2 * N4
    R4 = int(N6/N2)
    R5 = int(math.sqrt(N7/N2))

    R6 = R1 + R4 - R5
    R7 = R3

    a = f3.replace('=', '')

    R7_list = make_choice_exclude0(R7)
    R6_list = make_choice(R6)
    index = R7_list.index(R7)
    choice_list = []
    for i in range(5):
        if (R6_list[i] != 0):
            choice_list.append(a.format(R2=R2, R6=R6_list[i], R7=R7_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$$`-`{R7}$$/수식$$'.format(R7=R7_list[i], left='{left}', right='{right}'))
    if(R6 != 0):
        choice_list[index] = a.format(R2=R2, R6=R6, R7=R7, left='{left}', right='{right}')
    else:
        choice_list[index] = '$$수식$$`-`{R7}$$/수식$$'.format(R7=R7, left='{left}', right='{right}')

    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-382
def realnum311_Stem_276():
    stem = "다음 등식을 만족시키는 유리수 $$수식$$a,~b`$$/수식$$에 대하여 $$수식$$b`-`a`$$/수식$$의 값은?\n"\
           "{f1}\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f2}\n"\
              "{f3}\n"\
              "{f4}\n" \
              "따라서 {f5}이므로\n"\
              "{f6}{f7}\n\n"

    f1 = conv('$$수식$$$$표$${N2} over {sqrt {N1}} `+` {N4} over {sqrt {N3}} `-`N5 sqrt {N1} (N6`-` sqrt {N7} )`=`a sqrt {N1} `+`b sqrt {N2}$$/표$$$$/수식$$', 'N', 1, 7)
    f2 = conv('$$수식$${N2} over {sqrt {N1}} `+` {N4} over {sqrt {N3}} `-`N5 sqrt {N1} (N6`-` sqrt {N7} )`$$/수식$$', 'N', 1, 7)
    f3 = conv('$$수식$$=`R2 sqrt {R1} `+`R4 sqrt {R3} `-`R5 sqrt {R1} `+`R6 sqrt {R3}$$/수식$$', 'R', 1, 6)
    f4 = conv('$$수식$$=`R7 sqrt {R1} `+`R8 sqrt {R3}$$/수식$$', 'R', 1, 8)
    f5 = conv('$$수식$$a`=`R7,~b`=`R8`$$/수식$$', 'R', 7, 8)
    f6 = conv('$$수식$$b`-`a`=`R8`-`R7`$$/수식$$', 'R', 7, 8)
    f7 = conv('$$수식$$=`R9$$/수식$$', 'R', 9, 9)

    N1 = make_sqrt()
    while True:
        N3 = make_sqrt()
        if(N3 != N1):
            break
    N2 = N1 * randint(1, 3)
    N4 = N3 * randint(1, 3)
    N5 = make_exclude0(5)
    N6 = randint(1, 5)
    N7 = N1 * N3

    R1 = N1
    R2 = int(N2/N1)
    R3 = N3
    R4 = int(N4/N3)
    R5 = N5 * N6
    R6 = N1 * N5
    R7 = R2 - R5
    R8 = R4 + R6
    R9 = R8 - R7

    a = f7.replace('=', '')
    R9_list = make_choice(R9)
    index = R9_list.index(R9)
    choice_list = []
    for i in range(0, 5):
        choice_list.append(a.format(R9=R9_list[i], left='{left}', right='{right}'))

    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-383
def realnum311_Stem_277():
    stem = "{f1}$$수식$$=`A`$$/수식$$라 할 때, {f2}의 값을 구하시오.\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n"\
              "{f3}\n"\
              "{f4}\n" \
              "{f5}\n"\
              "{f6}\n"\
              "{f7}{f8}\n\n"

    f1 = conv('$$수식$$sqrt {N1} (`N2 sqrt {N3} `-`N4)`+` {`N5`-`N6 sqrt {N3}} over {sqrt {N1}} `$$/수식$$', 'N', 1, 6)
    f2 = conv('$$수식$$sqrt {R2} `A`$$/수식$$', 'R', 2, 2)
    f3 = conv('$$수식$$=`R1 sqrt {R2} `-`R3 sqrt {R4} `+` {(`R5`-`R6 sqrt {R7} ) TIMES sqrt {R4}} over {sqrt {R4} TIMES sqrt {R4}}$$/수식$$', 'R', 1, 7)
    f4 = conv('$$수식$$=`R1 sqrt {R2} `-`R3 sqrt {R4} `+` {`R5 sqrt {R4} `-`R6 sqrt {R2}} over {R4}$$/수식$$', 'R', 1, 6)
    f5 = conv('$$수식$$=`R1 sqrt {R2} `-`R3 sqrt {R4} `+`R8 sqrt {R4} `-`R9 sqrt {R2}$$/수식$$', 'R', 1, 9)
    f6 = conv('$$수식$$=`R10 sqrt {R2} `=`A$$/수식$$', 'R', 2, 10)
    f7 = conv('$$수식$$THEREFORE~ sqrt {R2} `A`=` sqrt {R2} TIMES `R10 sqrt {R2} `$$/수식$$', 'R', 2, 10)
    f8 = conv('$$수식$$=`R11$$/수식$$', 'R', 11, 11)

    N1 = make_sqrt(5)
    while True:
        N3 = make_sqrt(5)
        if(N3 != N1):
            break
    N2 = randint(1, 5)
    N4 = randint(1, 5)
    N5 = N1 * N4
    N6 = N1 * make_exclude0(5)

    R1 = N2
    R2 = N1 * N3
    R3 = N4
    R4 = N1
    R5 = N5
    R6 = N6
    R7 = N3
    R8 = int(R5/R4)
    R9 = int(R6/R4)
    R10 = R1 - R9
    R11 = R2 * R10

    a = '$$수식$${R11}$$/수식$$'.format(R11=R11)

    stem = stem.format(f1=f1, f2=f2) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, R2=R2, left=left, right=right)
    answer = answer.format(a=a)
    comment = comment.format(f1=f1, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-384
def realnum311_Stem_278():
    stem = "{f1}, {f2}일 때, {f3}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f3}\n"\
              "{f4}\n"\
              "{f5}\n" \
              "{f6}\n\n"

    f1 = conv('$$수식$$A`=`N1 sqrt {N2} `+` {N3} over {sqrt {N4}}$$/수식$$', 'N', 1, 4)
    f2 = conv('$$수식$$B`=`N5 sqrt {N2} `-` {`N3 sqrt {N4}} over {N4} `$$/수식$$', 'N', 2, 5)
    f3 = conv('$$수식$$sqrt {N4} A`-`N4 sqrt {N2} B`$$/수식$$', 'N', 2, 4)
    f4 = conv('$$수식$$=` sqrt {N4}  ( `N1 sqrt {N2} `+` {N3} over {sqrt {N4}}  ) `-`N4 sqrt {N2}  ( `N5 sqrt {N2} `-` {`N3 sqrt {N4}} over {N4}  )$$/수식$$', 'N', 1, 5)
    f5 = conv('$$수식$$=`R1 sqrt {R2} `+`R3`-`R4`+`R5 sqrt {R2}$$/수식$$', 'R', 1, 5)
    f6 = conv('$$수식$$=`R6 sqrt {R2} `-`R7$$/수식$$', 'R', 2, 7)

    N1 = randint(1, 5)
    N2 = make_sqrt(5)
    # R6 != 0 을 위함
    while True:
        N3 = make_exclude0(5)
        if(N1 != -N3):
            break
    while True:
        N4 = make_sqrt(5)
        if(N4 != N2):
            break
    N5 = randint(1, 5)

    R1 = N1
    R2 = N2 * N4
    R3 = N3
    R4 = N2 * N4 * N5
    R5 = N3
    R6 = R1 + R5
    R7 = R4 - R3

    a = f6.replace('=', '')
    R6_list = make_choice_exclude0(R6)
    R7_list = make_choice(R7)
    index = R6_list.index(R6)
    choice_list = []
    for i in range(5):
        if(R7_list[i]!=0):
            choice_list.append(a.format(R2=R2, R6=R6_list[i], R7=R7_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$$R6 sqrt {R2} `$$/수식$$'.format(R2=R2, R6=R6_list[i], left='{left}', right='{right}'))
    if(R7 != 0):
        choice_list[index] = a.format(R2=R2, R6=R6, R7=R7, left='{left}', right='{right}')
    else:
        choice_list[index] = '$$수식$$R6 sqrt {R2} `$$/수식$$'.format(R2=R2, R6=R6_list[i], left='{left}', right='{right}')

    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f3=f3, f4=f4, f5=f5, f6=f6)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-385
def realnum311_Stem_279():
    stem = "{f1}을 계산하면?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n"\
              "{f2}\n"\
              "{f3}\n" \
              "{f4}\n"\
              "{f5}\n\n"

    f1 = conv('$$수식$$sqrt {N1} `  ( sqrt {N2} `+` {N3} over {sqrt {N4}}  ) `+` {N5} over {sqrt {N4}} `( sqrt {N6} `+`N7 sqrt {N2} )`$$/수식$$', 'N', 1, 7)
    f2 = conv('$$수식$$`R1 sqrt {R2} `  ( sqrt {R3} `+` {R4} over {sqrt {R2}}  ) `+` {R5} over {sqrt {R2}} `(`R6 sqrt {R2} `+`R0 sqrt {R3} )`$$/수식$$', 'R', 0, 6)
    f3 = conv('$$수식$$=`R7 sqrt {R8} `+`R9`+`R10`+`R11 sqrt {R12}$$/수식$$', 'R', 7, 12)
    f4 = conv('$$수식$$=`R13 sqrt {R12} `+`R14`+`R11 sqrt {R12}$$/수식$$', 'R', 11, 14)
    f5 = conv('$$수식$$=`R14`+`R15 sqrt {R12}$$/수식$$', 'R', 12, 15)

    N2, N4 = random.sample([2, 3, 5], 2)
    N2 *= N4
    N1 = N4 * pow(randint(2, 4), 2)
    N3 = make_exclude0(5)
    N5 = make_exclude0(5)
    N6 = N4 * pow(randint(2, 4), 2)
    N7 = make_exclude0(5)

    R0 = N7
    R1 = int(math.sqrt(N1/N4))
    R2 = N4
    R3 = N2
    R4 = N3
    R5 = N5
    R6 = int(math.sqrt(N6/N4))
    R7 = R1
    R8 = R2 * R3
    R9 = R1 * R4
    R10 = R5 * R6
    R11 = R5
    R12 = int(N2/N4)
    R13 = R2 * R7
    R14 = R9 + R10
    R15 = R11 + R13

    a = f5.replace('=', '')
    R14_list = make_choice(R14)
    R15_list = make_choice(R15)
    index = R14_list.index(R14)
    choice_list = []
    for i in range(5):
        if(R15_list[i] == 0):
            choice_list.append(conv('$$수식$$`R14$$/수식$$', 'R', 14, 14).format(R14=R14_list[i], left='{left}', right='{right}'))
        elif(R14_list[i] == 0):
            choice_list.append(conv('$$수식$$`R15 sqrt {R12}$$/수식$$', 'R', 12, 15).format(R12=R12, R15=R15_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append(a.format(R12=R12, R14=R14_list[i], R15=R15_list[i], left='{left}', right='{right}'))
    if(R15==0):
        choice_list[index] = conv('$$수식$$`R14$$/수식$$', 'R', 14, 14).format(R14=R14, left='{left}', right='{right}')
    elif(R14 ==0):
        choice_list[index] = conv('$$수식$$`R15 sqrt {R12}$$/수식$$', 'R', 12, 15).format(R12=R12, R15=R15, left='{left}', right='{right}')
    else:
        choice_list[index] = a.format(R12=R12, R14=R14, R15=R15, left='{left}', right='{right}')

    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7,\
                R0=R0, R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, R12=R12, R13=R13, R14=R14, R15=R15, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-386
def realnum311_Stem_280():
    stem = "{f1}일 때, 유리수 $$수식$$m,~n`$$/수식$$에 대하여 {f2}의 값은?\n" \
           "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n"\
              "{f3}\n"\
              "{f4}\n"\
              "{f5}\n" \
              "{f6}\n"\
              "따라서 {f7}, {f8}이므로\n"\
              "{f9}{f10}\n\n"

    f1 = conv('$$수식$${`N1`+`N2 sqrt {N3}} over {sqrt {N4}} `+` {`N5 sqrt {N4}} over {N4} (`N6+`N7 sqrt {N8} )`=`m sqrt {N4} `+`n sqrt {N9} `$$/수식$$', 'N', 1, 9)
    f2 = conv('$$수식$$sqrt {m`+`n} `$$/수식$$', 'N', 0, 0)
    f3 = conv('$$수식$${`N1`+`N2 sqrt {N3}} over {sqrt {N4}} `+` {`N5 sqrt {N4}} over {N4} (`N6+`N7 sqrt {N8} )`$$/수식$$', 'N', 1, 8)
    f4 = conv('$$수식$$=` {R1` sqrt {R2} `+`R3 sqrt {R4}} over {R2} `+R5 sqrt {R2} `+` {`R6 sqrt {R4}} over {R2} `$$/수식$$', 'R', 1, 6)
    f5 = conv('$$수식$$=`R7 sqrt {R2} `+` {R3 sqrt {R4}} over {R2} `+`R5 sqrt {R2} `+` {`R6 sqrt {R4}} over {R2}$$/수식$$', 'R', 2, 7)
    f6 = conv('$$수식$$=`R8 sqrt {R2} `+`R9 sqrt {R4}$$/수식$$', 'R', 2, 9)
    f7 = conv('$$수식$$m`=`R8$$/수식$$', 'R', 8, 8)
    f8 = conv('$$수식$$n`=`R9$$/수식$$', 'R', 9, 9)
    f9 = conv('$$수식$$sqrt {m`+`n} `=` sqrt {R8`+`R9} `=` $$/수식$$', 'R', 8, 9)
    f10 = conv('$$수식$$sqrt {R10}$$/수식$$', 'R', 10, 10)

    # R3과 R6의 합이 R2로 나눠져야 함 -> R3+R6을 R2의 배수로 설정

    while True:
        N4 = make_sqrt(5)
        while True:
            N8 = make_sqrt(5)
            if(N8 != N4):
                break
        N1 = N4 * randint(1, 5)
        R9 = make_exclude0(5)
        N2 = make_exclude0(1)
        while True:
            N3 = N8 * pow(randint(2, 3), 2)
            if(int(N3/N8) != pow(N4, 2)):
                break
        temp = abs(N4 * R9 - N2 * int(math.sqrt(N3/N8)))
        N5 = 1
        for i in range(2, temp+1):
            if(temp%i==0):
                N5=i
                break
        N7 = int(temp / N5)
        if(R9 < 0):
            N7 *= -1
        N6 = N4
        N9 = N4 * N8

        R1 = N1
        R2 = N4
        R3 = N2 * int(math.sqrt(N3/N8))
        R4 = N9
        R5 = N5
        R6 = N5 * N7
        R7 = int(R1/R2)
        R8 = R5 + R7
        R10 = R8 + R9
        if(R10>4):
            break

    R10_list = make_choice(R10)
    index = R10_list.index(R10)
    choice_list = []
    for i in range(5):
        sq_list = sqrt_calc(R10_list[i])
        if(sq_list[1] == 1):
            choice_list.append(conv('$$수식$$`R11`$$/수식$$', 'R', 11, 11).format(R11=sq_list[0], left='{left}', right='{right}'))
        elif (sq_list[0] != 1):
            choice_list.append(conv('$$수식$$`R11 sqrt {R10}$$/수식$$', 'R', 10, 11).format(R10=sq_list[1], R11=sq_list[0], left='{left}', right='{right}'))
        else:
            choice_list.append(f10.format(R10=R10_list[i], left='{left}', right='{right}'))

    stem = stem.format(f1=f1, f2=f2, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=choice_list[index])\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-387
def realnum311_Stem_281():
    stem = "{f1}, {f2}일 때, $$수식$$a`+`b`$$/수식$$을 계산하면?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f3}\n"\
              "{f4}\n"\
              "{f5}\n" \
              "{f2}\n"\
              "{f6}\n"\
              "{f7}\n"\
              "{f8}{f9}\n\n"

    f1 = conv('$$수식$$a`=` sqrt {N3} `-` {N4} over {sqrt {N1}} `+` sqrt {N1} ( sqrt {N1} `-` sqrt {N2} )`$$/수식$$', 'N', 1, 4)
    f2 = conv('$$수식$$b`=` sqrt {N2} ( sqrt {N5} `+` sqrt {N1} )`-` {N6} over {sqrt {N1}} ( sqrt {N7} `-` sqrt {N8} )$$/수식$$', 'N', 1, 8)
    f3 = conv('$$수식$$a`=` sqrt {N1} ( sqrt {N1} `-` sqrt {N2} )`+` sqrt {N3} `-` {N4} over {sqrt {N1}}$$/수식$$', 'N', 1, 4)
    f4 = conv('$$수식$$=`R1`-` sqrt {R2} `+`R3 sqrt {R2} `-`R4 sqrt {R1}$$/수식$$', 'R', 1, 4)
    f5 = conv('$$수식$$=`R1`-`R4 sqrt {R1} `+`R5 sqrt {R2}$$/수식$$', 'R', 1, 5)
    f6 = conv('$$수식$$=`R4 sqrt {R1} `+` sqrt {R2} `-`R3 sqrt {R2} `+`R6$$/수식$$', 'R', 1, 6)
    f7 = conv('$$수식$$=`R6`+`R4 sqrt {R1} `-`R5 sqrt {R2}$$/수식$$', 'R', 1, 6)
    f8 = conv('$$수식$$THEREFORE~a`+`b`$$/수식$$', 'R', 0, 0)
    f9 = conv('$$수식$$=`R7$$/수식$$', 'R', 7, 7)

    N1 = make_sqrt(5)
    while True:
        N2 = make_sqrt(5)
        if(N2 != N1):
            break
    N3 = N1 * N2 * pow(randint(2, 3), 2)
    N4 = N1 * N2
    N5 = N1 * N2
    N6 = int(math.sqrt(N3/(N1*N2)))
    N7 = N1 * N1 * N2
    N8 = N1 * N2 * N2 * pow(randint(1, 3), 2)

    R1 = N1
    R2 = N1 * N2
    R3 = N6
    R4 = N2
    R5 = R3 - 1
    R6 = N6 * int(math.sqrt(N8/N1))
    R7 = R1 + R6

    a = f9.replace('=', '')
    R7_list = make_choice(R7)
    index = R7_list.index(R7)
    choice_list = []
    for i in range(0, 5):
        choice_list.append(a.format(R7=R7_list[i], left='{left}', right='{right}'))

    stem = stem.format(f1=f1, f2=f2, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-388
def realnum311_Stem_282():
    stem = "{f1}가 유리수가 되도록 하는 유리수 $$수식$$a$$/수식$$의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}{f2}\n"\
              "{f3}\n"\
              "유리수가 되려면 {f4}이어야 하므로\n"\
              "$$수식$$a`=`$$/수식$${f5}\n\n"

    f1 = conv('$$수식$$`N1 (`N2`+`a sqrt {N3} )`+`N4 a`-`N5 sqrt {N3}$$/수식$$', 'N', 1, 5)
    f2 = conv('$$수식$$=`R1`+`R2 a sqrt {R3} `+`R4 a`-`R5 sqrt {R3}$$/수식$$', 'R', 1, 5)
    f3 = conv('$$수식$$=(R1`+`R4 a)`+`(`R2 a`-`R5) sqrt {R3}$$/수식$$', 'R', 1, 5)
    f4 = conv('$$수식$$`R2 a`-`R5`=`0$$/수식$$', 'R', 2, 5)
    f5 = conv('$$수식$$R6$$/수식$$', 'R', 6, 6)

    N1 = randint(1, 5)
    N2 = randint(1, 5)
    N3 = make_sqrt()
    N4 = make_exclude0(5)
    N5 = N1 * make_exclude0(5)

    R1 = N1 * N2
    R2 = N1
    R3 = N3
    R4 = N4
    R5 = N5
    R6 = int(N5/N1)

    R6_list = make_choice(R6)
    index = R6_list.index(R6)
    choice_list = []
    for i in range(0, 5):
        choice_list.append(f5.format(R6=R6_list[i], left='{left}', right='{right}'))

    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-389
def realnum311_Stem_283():
    stem = "{f1}가 유리수가 되도록 하는 유리수 $$수식$$a$$/수식$$의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n" \
              "{f2}\n"\
              "{f3}\n"\
              "유리수가 되려면 {f4}이어야 하므로\n"\
              "$$수식$$a`=`$$/수식$${f5}\n\n"

    f1 = conv('$$수식$$sqrt {N1} `-` {N2} over {sqrt {N3}} `+`N4 sqrt {N3} `-`N5 a sqrt {N3}$$/수식$$', 'N', 1, 5)
    f2 = conv('$$수식$$=`R1 sqrt {R2} `-`R3 sqrt {R2} `+`R4 sqrt {R2} `-`R5 a sqrt {R2}$$/수식$$', 'R', 1, 5)
    f3 = conv('$$수식$$=`(`R6`-`R5 a) sqrt {R2}$$/수식$$', 'R', 2, 6)
    f4 = conv('$$수식$$`R6`-`R5 a`=`0$$/수식$$', 'R', 5, 6)
    f5 = conv('$$수식$$R7$$/수식$$', 'R', 7, 7)

    while True:
        N3 = make_sqrt()
        N1 = N3 * pow(randint(2, 5), 2)
        N2 = N3 * make_exclude0(5)
        N4 = make_exclude0(5)

        R1 = int(math.sqrt(N1 / N3))
        R2 = N3
        R3 = int(N2 / N3)
        R4 = N4
        R6 = R1 - R3 + R4

        if(R6 != 0):
            break

    div_list = [1]
    for i in range(2, R6+1):
        if(R6%i == 0):
            div_list.append(i)

    N5 = random.choice(div_list)
    R5 = N5

    R7 = int(R6/R5)

    R7_list = make_choice(R7)
    index = R7_list.index(R7)
    choice_list = []
    for i in range(0, 5):
        choice_list.append(f5.format(R7=R7_list[i], left='{left}', right='{right}'))

    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-390
def realnum311_Stem_284():
    stem = "{f1}가 유리수가 되도록 하는 유리수 $$수식$$a$$/수식$$의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n" \
              "{f2}\n"\
              "{f3}\n"\
              "유리수가 되려면 {f4}이어야 하므로\n"\
              "$$수식$$a`=`$$/수식$${f5}\n\n"

    f1 = conv('$$수식$${a} over {sqrt {N1}} ( sqrt {N2} `-`N3)`+` sqrt {N4}  ( {N7} over {sqrt {N5}} `-` {N8} over {sqrt {N6}}  ) `$$/수식$$', 'N', 1, 8)
    f2 = conv('$$수식$$=`R1 a`-`R2 sqrt {R3} a`+`R4`-`R5 sqrt {R3}$$/수식$$', 'R', 1, 5)
    f3 = conv('$$수식$$=`(`R1 a`+`R4)`-`(`R2`+`R5 a) sqrt {R3}$$/수식$$', 'R', 1, 5)
    f4 = conv('$$수식$$`R2`+`R5 a`=`0`$$/수식$$', 'R', 2, 5)
    f5 = conv('$$수식$$R6$$/수식$$', 'R', 6, 6)

    N1 = make_sqrt(5)
    N2 = N1 * pow(randint(2, 5), 2)
    while True:
        N5 = make_sqrt(5)
        if(N5 != N1):
            break
    N6 = N1 * N5
    N4 = N1 * N6 * pow(randint(1, 2), 2)
    N7 = randint(1, 5)
    N8 = make_exclude0(5)

    R1 = int(math.sqrt(N2/N1))
    R3 = N1
    R4 = int(math.sqrt(N4/N5)) * N7
    R5 = int(math.sqrt(N4/(N1*N6))) * N8

    N3 = N1 * R5 * make_exclude0(5)
    R2 = int(N3/N1)

    R6 = int(R2/R5) * -1

    R6_list = make_choice(R6)
    index = R6_list.index(R6)
    choice_list = []
    for i in range(0, 5):
        choice_list.append(f5.format(R6=R6_list[i], left='{left}', right='{right}'))

    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-391
def realnum311_Stem_285():
    stem = "다음 두 식을 계산한 결과가 각각 유리수가 되도록 하는 유리수 $$수식$$a,~b$$/수식$$에 대하여 $$수식$$a-b$$/수식$$의 값은?\n"\
           "$$표$${f1}\n{f2}$$/표$$\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}{f3}\n"\
              "{f4}\n"\
              "{f2}\n" \
              "{f5}\n" \
              "{f6}\n" \
              "두 식의 계산 결과가 각각 유리수가 되려면\n" \
              "{f7}, {f8}\n" \
              "이어야 하므로 {f9}\n" \
              "$$수식$$THEREFORE~a-b`=$$/수식$${f10}\n\n"

    f1 = conv('$$수식$$`N1 (a`+`N2 sqrt {N3} )`+`a sqrt {N4}$$/수식$$', 'N', 1, 4)
    f2 = conv('$$수식$$sqrt {N6}  ( {N7} over {sqrt {N5}} `-` {N8} over {N5}  ) `+` {b} over {sqrt {N5}} ( sqrt {N9} `-`N10)$$/수식$$', 'N', 5, 10)
    f3 = conv('$$수식$$=`R1 a`+`R2 sqrt {R3} `+`R4 a sqrt {R5}$$/수식$$', 'R', 1, 5)
    f4 = conv('$$수식$$=`R1 a`+`(R2`+`R4 a) sqrt {R5}$$/수식$$', 'R', 1, 5)

    f5 = conv('$$수식$$=`R6`-`R7 sqrt {R8} `+`R9 b`-`R10 b sqrt {R8}$$/수식$$', 'R', 6, 10)
    f6 = conv('$$수식$$=`(R6`+`R9 b)`-`(R7`+`R10 b) sqrt {R8}$$/수식$$', 'R', 6, 10)

    f7 = conv('$$수식$$R2`+`R4 a`=`0$$/수식$$', 'R', 2, 4)
    f8 = conv('$$수식$$R7`+`R10 b`=`0$$/수식$$', 'R', 7, 10)
    f9 = conv('$$수식$$a`=`R11,~b`=`R12$$/수식$$', 'R', 11, 12)
    f10 = conv('$$수식$$R13$$/수식$$', 'R', 13, 13)

    N1 = randint(1, 5)
    N3 = make_sqrt(5)
    N4 = N3 * pow(randint(1, 3), 2)
    N2 = int(math.sqrt(N4/N3)) * make_exclude0(3)

    N5 = make_sqrt(5)
    N6 = N5**3
    N7 = randint(1, 5)
    N9 = N5 * pow(randint(1, 3), 2)
    N10 = N5 * randint(1, 5)
    N8 = int(N10/N5) * randint(1, 3)

    R1 = N1
    R2 = N1*N2
    R3 = N3
    R4 = int(math.sqrt(N4/N3))
    R5 = N3

    R6 = N5 * N7
    R7 = N8
    R8 = N5
    R9 = int(math.sqrt(N9/N5))
    R10 = int(N10/N5)

    R11 = int(R2/R4) * -1
    R12 = int(R7/R10) * -1
    R13 = R11 - R12

    a = f10.replace('=', '')
    R13_list = make_choice(R13)
    index = R13_list.index(R13)
    choice_list = []
    for i in range(5):
        choice_list.append(a.format(R13=R13_list[i], left='{left}', right='{right}'))

    stem = stem.format(f1=f1, f2=f2, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9, N10=N10, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9, N10=N10,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, R12=R12, R13=R13, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-392
def realnum311_Stem_286():
    stem = "$$수식$$A`$$/수식$$가 유리수일 때, 다음을 구하시오.\n"\
        "$$표$${f1}$$/표$$\n"
    answer = "(답) {a1}, {a2}\n"
    comment = "(해설)\n" \
              "(1) {f1}\n"\
              "{f2}\n" \
              "$$수식$$A`$$/수식$$가 유리수이므로 {f3}이어야 한다."\
              "$$수식$$THEREFORE~k`=`$$/수식$${f4}\n" \
              "(2) $$수식$$k`=`$$/수식$${f4}이므로\n"\
              "{f5}\n\n"

    f1 = conv('$$수식$$A`=`N1 (k`-` sqrt {N2} )`-`N3 sqrt {N2} `+`N4 k sqrt {N2} `-`N5$$/수식$$', 'N', 1, 5)
    f2 = conv('$$수식$$=`(`R1 k`-`R2)`+`(`R3 k`-`R4) sqrt {R5}$$/수식$$', 'R', 1, 5)
    f3 = conv('$$수식$$`R3 k`-`R4=`0$$/수식$$', 'R', 3, 4)
    f4 = conv('$$수식$$R6$$/수식$$', 'R', 6, 6)
    f5 = conv('$$수식$$A`=`R1 k`-`R2=`R1 TIMES R6`-`R2=`R7$$/수식$$', 'R', 1, 7)

    while True:
        N1 = make_exclude0(5)
        N2 = make_sqrt()
        while True:
            N3 = randint(1, 5)
            if (N3 != N1):
                break
        div_list = [1]
        for i in range(1, N1 + N3 + 1):
            if ((N1 + N3) % i == 0):
                div_list.append(i)
        N4 = random.choice(div_list)
        N5 = make_exclude0(5)

        R1 = N1
        R2 = N5
        R3 = N4
        R4 = N1 + N3
        R5 = N2
        R6 = int(R4 / R3)
        R7 = (R1 * R6) - R2

        if(R6 != 0):
            break

    a1 = '$$수식$${R6}$$/수식$$'.format(R6=R6)
    a2 = '$$수식$${R7}$$/수식$$'.format(R7=R7)

    stem = stem.format(f1=f1) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, left=left, right=right)
    answer = answer.format(a1=a1, a2=a2)
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-393
def realnum311_Stem_287():
    stem = "두 실수 $$수식$$x,~y`$$/수식$$에 대하여 {f1}라 하자. {f2}를 만족시키는 유리수 $$수식$$a,~b`$$/수식$$에 대하여 {f3}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f4}\n"\
              "{f5}\n"\
              "따라서 {f6}, {f7}이므로\n" \
              "{f8}\n"\
              "{f9}\n" \
              "{f10}\n\n"

    f1 = conv('$$수식$$x◇y`=`x sqrt {N1} `-`y`$$/수식$$', 'N', 1, 1)
    f2 = conv('$$수식$$(a◇N2)`+`(N3◇a)`=`b`$$/수식$$', 'N', 2, 3)
    f3 = conv('$$수식$$`b sqrt {N1} ◇a`$$/수식$$', 'N', 1, 1)
    f4 = conv('$$수식$$(a◇N2)`+`(N3◇a)`=`(`a sqrt {N1} `-`N2)`+(`N3 sqrt {N1} `-`a)$$/수식$$', 'N', 1, 3)
    f5 = conv('$$수식$$=`(-N2`-`a)`+`(a`+`N3) sqrt {N1}$$/수식$$', 'N', 1, 3)
    f6 = conv('$$수식$$-N2`-`a`=`b$$/수식$$', 'N', 2, 2)
    f7 = conv('$$수식$$a`+`N3`=`0$$/수식$$', 'N', 3, 3)
    f8 = conv('$$수식$$a`=`R1,~b`=`R2$$/수식$$', 'R', 1, 2)
    f9 = conv('$$수식$$THEREFORE~b sqrt {R3} `◇a`=`R2 sqrt {R3} ◇(R1)`$$/수식$$', 'R', 1, 3)
    f10 = conv('$$수식$$=`R2 sqrt {R3} sqrt {R3} `-`(R1)`=`R4$$/수식$$', 'R', 1, 4)

    N1 = make_sqrt()
    N2 = randint(1, 5)
    while True:
        N3 = randint(1, 5)
        if(N3 != N2):
            break

    R1 = N3 * -1
    R2 = (N2 + R1) * -1
    R3 = N1
    R4 = R2 * R3 - R1

    a = '$$수식$${R4}$$/수식$$'
    R4_list = make_choice(R4)
    index = R4_list.index(R4)
    choice_list = []
    for i in range(5):
        choice_list.append(a.format(R4=R4_list[i], left='{left}', right='{right}'))

    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10)\
        .format(N1=N1, N2=N2, N3=N3,\
                R1=R1, R2=R2, R3=R3, R4=R4, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-394
def realnum311_Stem_288():
    stem = "{f1}의 소수 부분을 $$수식$$a`$$/수식$$, {f2}의 소수 부분을 $$수식$$b`$$/수식$$라 할 때, {f3}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f4}이므로 {f5}\n"\
              "{f6}이므로 {f7}\n"\
              "$$수식$$THEREFORE~ $$/수식$${f3}\n" \
              "{f8}\n"\
              "{f9}\n" \
              "{f10}\n\n"

    f1 = conv('$$수식$$sqrt {N1}$$/수식$$', 'N', 1, 1)
    f2 = conv('$$수식$$sqrt {N4} `$$/수식$$', 'N', 4, 4)
    f3 = conv('$$수식$$sqrt {N1} a`+` sqrt {N4} b`+` {N8} over {sqrt {N7}} `$$/수식$$', 'N', 1, 8)
    f4 = conv('$$수식$$N2 &lt; sqrt {N1} &lt; N3`$$/수식$$', 'N', 1, 3)
    f5 = conv('$$수식$$a`=` sqrt {N1} `-`N2`$$/수식$$', 'N', 1, 2)
    f6 = conv('$$수식$$N5 &lt; sqrt {N4} &lt; N6`$$/수식$$', 'N', 4, 6)
    f7 = conv('$$수식$$b`=` sqrt {N4} `-`N5$$/수식$$', 'N', 4, 5)
    f8 = conv('$$수식$$= sqrt {R1} ( sqrt {R1} `-`R2)`+` sqrt {R4} ( sqrt {R4} `-`R5)`+`R2 sqrt {R1}$$/수식$$', 'R', 1, 5)
    f9 = conv('$$수식$$=`R1`-`R2 sqrt {R1} `+`R4`-`R5 sqrt {R4} `+`R2 sqrt {R1}$$/수식$$', 'R', 1, 5)
    f10 = conv('$$수식$$=`R6`-`R5 sqrt {R4}$$/수식$$', 'R', 4, 6)

    N1 = make_sqrt()
    while True:
        N4 = make_sqrt()
        if(N4 != N1):
            break
    N2 = math.floor(math.sqrt(N1))
    N3 = N2 + 1
    N5 = math.floor(math.sqrt(N4))
    N6 = N5 + 1
    N7 = N1
    N8 = N7 * N2

    R1 = N1
    R2 = N2
    R4 = N4
    R5 = N5
    R6 = R1 + R4

    a = f10.replace('=', '')
    R6_list = make_choice(R6)
    index = R6_list.index(R6)
    choice_list = []
    for i in range(5):
        choice_list.append(a.format(R4=R4, R5=R5, R6=R6_list[i], left='{left}', right='{right}'))

    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8,\
                R1=R1, R2=R2, R4=R4, R5=R5, R6=R6, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)

# 3-1-1-395
def realnum311_Stem_289():
    stem = "자연수 $$수식$$n`$$/수식$$에 대하여 {sq_n}의 소수 부분을 $$수식$$f(n)`$$/수식$$이라 할 때, {f1}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f2}이므로\n"\
              "{f3}\n"\
              "{f4}이므로\n" \
              "{f5}\n"\
              "{f6}\n\n"
    sq_n = conv('$$수식$$sqrt {n`}$$/수식$$', 'N', 0, 0)
    f1 = conv('$$수식$$f(N1)`-`f(N4)`$$/수식$$', 'N', 1, 4)
    f2 = conv('$$수식$$N2 &lt; sqrt {N1} &lt; N3`$$/수식$$', 'N', 1, 3)
    f3 = conv('$$수식$$f(R1)`=` sqrt {R1} `-`R2`=`R3 sqrt {R4} `-`R2`$$/수식$$', 'R', 1, 4)
    f4 = conv('$$수식$$N5 &lt; sqrt {N4} &lt; N6`$$/수식$$', 'N', 4, 6)
    f5 = conv('$$수식$$f(R5)`=` sqrt {R5} `-`R6`=`R7 sqrt {R4} `-`R6$$/수식$$', 'R', 4, 7)
    f6 = conv('$$수식$$THEREFORE~f(R1)`-`f(R5)`=`R8 sqrt {R4} `-`R9$$/수식$$', 'R', 1, 9)

    sq = make_sqrt()
    N1 = sq * pow(randint(2, 5), 2)
    while True:
        N4 = sq * pow(randint(2, 5), 2)
        if(N4 != N1):
            break
    N2 = math.floor(math.sqrt(N1))
    N3 = N2 + 1
    N5 = math.floor(math.sqrt(N4))
    N6 = N5 + 1

    R1 = N1
    R2 = N2
    R3 = int(math.sqrt(N1/sq))
    R4 = sq
    R5 = N4
    R6 = N5
    R7 = int(math.sqrt(N4/sq))
    R8 = R3 - R7
    R9 = R2 - R6

    a = conv('$$수식$$`R8 sqrt {R4} `-`R9$$/수식$$', 'R', 4, 9)
    sel = conv('$$수식$$`R8 sqrt {R4} `$$/수식$$', 'R', 4, 8)
    R8_list = make_choice_exclude0(R8)
    R9_list = make_choice(R9)
    index = R8_list.index(R8)
    choice_list = []
    for i in range(5):
        if (R9_list[i] != 0):
            choice_list.append(a.format(R4=R4, R8=R8_list[i], R9=R9_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append(sel.format(R4=R4, R8=R8_list[i], left='{left}', right='{right}'))
    if (R9 != 0):
        choice_list[index] = a.format(R4=R4, R8=R8, R9=R9, left='{left}', right='{right}')
    else:
        choice_list[index] = sel.format(R4=R4, R8=R8, left='{left}', right='{right}')

    stem = stem.format(f1=f1, sq_n=sq_n, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f2=f2, f3=f3, f4=f4, f5=f5, f6=f6)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-396
def realnum311_Stem_290():
    stem = "{f1}의 소수 부분을 $$수식$$k`$$/수식$$라 할 때, {f2}의 소수 부분을 $$수식$$k`$$/수식$$를 이용하여 나타내면?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f3}이므로 {f4}\n"\
              "{f5}\n"\
              "이때 {f6}이므로 {f2}의 소수 부분은\n" \
              "{f7}\n"\
              "{f8}{f9}\n\n"

    f1 = conv('$$수식$$sqrt {N1} `$$/수식$$', 'N', 1, 1)
    f2 = conv('$$수식$$sqrt {N4} `$$/수식$$', 'N', 4, 4)
    f3 = conv('$$수식$$N2 &lt; sqrt {N1} &lt; N3`$$/수식$$', 'N', 1, 3)
    f4 = conv('$$수식$$k`=` sqrt {N1} `-`N2$$/수식$$', 'N', 1, 2)
    f5 = conv('$$수식$$THEREFORE~ sqrt {N1} `=`k`+`N2$$/수식$$', 'N', 1, 2)
    f6 = conv('$$수식$$N5 &lt; sqrt {N4} &lt; N6`$$/수식$$', 'N', 4, 6)
    f7 = conv('$$수식$$sqrt {R1} `-`R2`=`R3 sqrt {R4} `-`R2$$/수식$$', 'R', 1, 4)
    f8 = conv('$$수식$$=`R3 (k`+`R5)`-`R2`=$$/수식$$', 'R', 2, 5)

    N1 = make_sqrt()
    N2 = math.floor(math.sqrt(N1))
    N3 = N2 + 1
    N4 = N1 * pow(randint(2, 5), 2)
    N5 = math.floor(math.sqrt(N4))
    N6 = N5 + 1

    R1 = N4
    R2 = N5
    R3 = int(math.sqrt(N4/N1))
    R4 = N1
    R5 = N2
    R6 = R2 - R3 * R5

    a = conv('$$수식$$`R3 k`-`R6$$/수식$$', 'R', 3, 6)
    R6_list = make_choice(R6)
    index = R6_list.index(R6)
    choice_list = []
    for i in range(5):
        if(R6_list[i] != 0):
            choice_list.append(a.format(R3=R3, R6=R6_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$$`{R3} k`$$/수식$$'.format(R3=R3, left='{left}', right='{right}'))


    stem = stem.format(f1=f1, f2=f2, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=choice_list[index])\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-397
def realnum311_Stem_291():
    stem = "{sq_n}의 정수 부분을 $$수식$$a`$$/수식$$, 소수 부분을 $$수식$$b`$$/수식$$라 할 때, 다음 조건을 만족시키는 자연수 $$수식$$n`$$/수식$$의 개수는?\n" \
           "$$표$${f1}, {f2}$$/표$$\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{sq_n}$$수식$$`=`a`+`b`$$/수식$$이고 {f1}, {f2}에서\n"\
              "(ⅰ) {f3}일 때, {f4}\n"\
              "{f5}\n" \
              "(ⅱ) {f6}일 때, {f7}\n"\
              "{f8}\n" \
              "(ⅰ), (ⅱ)에서 구하는 자연수 $$수식$$n`$$/수식$$은 {f9}의 {f10}개이다.\n\n"

    sq_n = conv('$$수식$$sqrt {n}$$/수식$$', 'N', 0, 0)
    f1 = conv('$$수식$$N1 &lt; a &lt; N2`$$/수식$$', 'N', 1, 2)
    f2 = conv('$$수식$$N3 &lt; b &lt; N4`$$/수식$$', 'N', 3, 4)
    f3 = conv('$$수식$$a`=`R1`$$/수식$$', 'R', 1, 1)
    f4 = conv('$$수식$$R2 &lt; sqrt {n} &lt; R3`$$/수식$$', 'R', 2, 3)
    f5 = conv('$$수식$$THEREFORE~R4 &lt; n &lt; R5`$$/수식$$', 'R', 4, 5)
    f6 = conv('$$수식$$a`=`R6`$$/수식$$', 'R', 6, 6)
    f7 = conv('$$수식$$R7 &lt; sqrt {n} &lt; R8`$$/수식$$', 'R', 7, 8)
    f8 = conv('$$수식$$THEREFORE~R9 &lt; n &lt; R10$$/수식$$', 'R', 9, 10)
    f9 = ''
    f10 = conv('$$수식$$R11$$/수식$$', 'R', 11, 11)

    N1 = randint(1, 3)
    N2 = N1 + 3
    N3 = 0.1
    N4 = round(N3 * randint(3, 9), 1)

    R1 = N1 + 1
    R2 = R1 + N3
    R3 = R1 + N4
    R4 = round(R2**2, 2)
    R5 = round(R3**2, 2)

    R6 = R1 + 1
    R7 = R6 + N3
    R8 = R6 + N4
    R9 = round(R7**2, 2)
    R10 = round(R8**2, 2)

    n_list = []
    for i in range(N1**2, (N2+1)**2):
        if(i > R4 and i < R5):
            n_list.append('$$수식$${}$$/수식$$'.format(i))
        elif(i > R9 and i < R10):
            n_list.append('$$수식$${}$$/수식$$'.format(i))

    R11 = len(n_list)

    for str in n_list:
        f9 += ', '
        f9 += str
    f9 = f9[2:]

    if(R11 < 3):
        R11_list = make_choice_positive(R11)
    else:
        R11_list = make_choice(R11)
    index = R11_list.index(R11)
    choice_list = []
    for i in range(5):
        choice_list.append(f10.format(R11=R11_list[i], left='{left}', right='{right}'))

    stem = stem.format(sq_n=sq_n, f1=f1, f2=f2, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(sq_n=sq_n, f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-405
def realnum311_Stem_292():
    stem = "{f1}을 계산하면 {f2}이다. 이때 유리수 $$수식$$a,~b`$$/수식$$에 대하여 {f3}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n"\
              "{f4}\n"\
              "{f5}\n" \
              "{f6}\n"\
              "따라서 {f7}, {f8}이므로\n" \
              "{f9}\n" \
              "{f10}{f11}\n\n"

    f1 = conv('$$수식$$sqrt {N1}  ( {N2} over {sqrt {N3}} `-` {N4} over {sqrt {N5}}  ) `-` sqrt {N5}  ( {N6} over {sqrt {N1}} `-` {N7} over {sqrt {N8}}  ) `$$/수식$$', 'N', 1, 8)
    f2 = conv('$$수식$$a sqrt {N9} `+`b sqrt {N1} `$$/수식$$', 'N', 1, 9)
    f3 = conv('$$수식$$sqrt {b`-`R12 a}$$/수식$$', 'R', 12, 12)
    f4 = conv('$$수식$$=` {`R1 sqrt {R2}} over {`R3 sqrt {R4}} `-`R5 sqrt {R6} `-` {R7} over {sqrt {R6}} `+` {R8} over {sqrt {R2}}$$/수식$$', 'R', 1, 8)
    f5 = conv('$$수식$$=` {`R9 sqrt {R6}} over {R10} `-`R5 sqrt {R6} `-` {`R7 sqrt {R6}} over {R6} `+` {`R8 sqrt {R2}} over {R2}$$/수식$$', 'R', 2, 10)
    f6 = conv('$$수식$$=`-` {`R11 sqrt {R6}} over {R12} `+` {`R13 sqrt {R2}} over {R14}$$/수식$$', 'R', 2, 14)
    f7 = conv('$$수식$$a`=`- {R11} over {R12} `$$/수식$$', 'R', 11, 12)
    f8 = conv('$$수식$$b`=` {R13} over {R14}$$/수식$$', 'R', 13, 14)
    f9 = conv('$$수식$$sqrt {b`-`R12 a} `=` sqrt {{R13} over {R14} `-`R12` TIMES`  ( `-` {R11} over {R12}  )} `=` sqrt {{R15} over {R16}}$$/수식$$', 'R', 2, 16)
    f10 = conv('$$수식$$=` {`R17 sqrt {R18}} over {sqrt {R16}} `$$/수식$$', 'R', 16, 18)
    f11 = conv('$$수식$$=` {`R19 sqrt {R20}} over {R21}$$/수식$$', 'R', 19, 21)

    while True:
        N9 = random.choice([2, 3])
        while True:
            N5 = random.choice([2, 3])
            if (N5 != N9):
                break
        N1 = N5 * N9
        N2 = randint(1, 5)
        N3 = N5 * pow(randint(2, 3), 2)
        N4 = make_exclude0(5)
        N6 = randint(1, 5)
        N7 = make_exclude0(5)
        N8 = N1 * N5

        R1 = N2
        R2 = N1
        R3 = int(math.sqrt(N3 / N5))
        R4 = N5
        R5 = N4
        R6 = N9
        R7 = N6
        R8 = N7

        red = Fraction(R1, R3)
        R9 = red.numerator
        R10 = red.denominator
        red2 = R5 + Fraction(R7, R6) - red
        R11 = red2.numerator
        R12 = red2.denominator
        red3 = Fraction(R8, R2)
        R13 = red3.numerator
        R14 = red3.denominator
        red4 = Fraction(R13, R14) + R11
        R15 = red4.numerator
        R16 = red4.denominator

        sq_list = sqrt_calc(R15)
        R17 = sq_list[0]
        R18 = sq_list[1]

        R20 = R16 * R18
        sq_list2 = sqrt_calc(R20)
        R19 = R17 * sq_list2[0]
        R20 = sq_list2[1]
        R21 = R16
        red5 = Fraction(R19, R21)
        R19 = red5.numerator
        R21 = red5.denominator

        # 의도대로 식이 나온 경우에만 반복문 탈출
        if (R15 > 0 and R16 != R18 and R19 != 1):
            break

    if(R18 == 1):
        f10 = f10.replace('sqrt {left}{R18}{right}', '')

    a = f11.replace('=', '')
    R19_list = make_choice_exclude0(R19)
    index = R19_list.index(R19)
    choice_list = []
    for i in range(5):
        if(R18 != 1):
            R20_temp = random.choice([R18, R20])
        else:
            R20_temp = R20
        red_temp = Fraction(R19_list[i], R21)
        if(R20_temp == 1 and red_temp.numerator == 1):
            if(red_temp.denominator == 1):
                choice_list.append('$$수식$${R19}$$/수식$$'.format(R19=1))
            else:
                choice_list.append('$$수식$${R19} over {R21}$$/수식$$'.format(R19=1, R21=red_temp.denominator))
        else:
            choice_list.append(a.format(R19=red_temp.numerator, R20=R20_temp, R21=red_temp.denominator, left='{left}', right='{right}'))
        if(R20_temp == 1):
            choice_list[i] = choice_list[i].replace('sqrt {1}', '')

    choice_list[index] = a.format(R19=R19, R20=R20, R21=R21, left='{left}', right='{right}')

    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9, R12=R12, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10, f11=f11)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, R12=R12,\
                R13=R13, R14=R14, R15=R15, R16=R16, R17=R17, R18=R18, R19=R19, R20=R20, R21=R21, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-406
def realnum311_Stem_293():
    stem = "{f1}, {f2}일 때, {f3}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}{f4}\n"\
              "{f5}\n"\
              "{f6}\n" \
              "{f7}\n"\
              "$$수식$$THEREFORE~ $$/수식$${f3}\n" \
              "{f8}\n" \
              "{f9}" \
              "{f10}\n\n"

    f1 = conv('$$수식$$A`=` sqrt {N2} `-` {N3} over {sqrt {N1}}$$/수식$$', 'N', 1, 3)
    f2 = conv('$$수식$$B`=` sqrt {N1} `+` {sqrt {N4}} over {N5} `$$/수식$$', 'N', 1, 5)
    f3 = conv('$$수식$$sqrt {R4} A`+` {1} over {sqrt {R2}} (`R5 A`-`R6 B)`$$/수식$$', 'R', 2, 6)
    f4 = conv('$$수식$$=`R1 sqrt {R2} `-` {`R3 sqrt {R4}} over {R5}$$/수식$$', 'R', 1, 5)
    f5 = conv('$$수식$$`R5 A`-`R6 B`=`R5  ( `R1 sqrt {R2} `-` {`R3 sqrt {R4}} over {R5}  ) `-`R6  ( sqrt {R4} `+` {sqrt {R2}} over {R6}  )$$/수식$$', 'R', 1, 6)
    f6 = conv('$$수식$$=`R7 sqrt {R2} `-`R3 sqrt {R4} `-`R6 sqrt {R4} `-` sqrt {R2}$$/수식$$', 'R', 2, 7)
    f7 = conv('$$수식$$=`R8 sqrt {R2} `-`R9 sqrt {R4}$$/수식$$', 'R', 2, 9)
    f8 = conv('$$수식$$=` sqrt {R4}  ( `R1 sqrt {R2} `-` {`R3 sqrt {R4}} over {R5}  ) `+` {1} over {sqrt {R2}} (`R8 sqrt {R2} `-`R9 sqrt {R4} )$$/수식$$', 'R', 1, 9)
    f9 = conv('$$수식$$=`R10 sqrt {R11} `-`R12`+`R8`-`R13 sqrt {R11}$$/수식$$', 'R', 8, 13)
    f10 = conv('$$수식$$=`R14`-`R15 sqrt {R11}$$/수식$$', 'R', 11, 15)

    while True:
        N1 = make_sqrt(5)
        while True:
            N4 = make_sqrt(5)
            if (N4 != N1):
                break
        N2 = N4 * pow(randint(2, 3), 2)
        N3 = N1 * make_exclude0(5)
        N5 = randint(2, 5)

        R1 = int(math.sqrt(N2 / N4))
        R2 = N4
        red = Fraction(N3, N1)
        R3 = red.numerator
        R4 = N1
        R5 = red.denominator
        R6 = N5
        R7 = R1 * R5
        R8 = R7 - 1
        R9 = R3 + R6
        R10 = R1
        R11 = R2 * R4
        R12 = Fraction(R3 * R4, R5).numerator
        R13 = Fraction(R9, R2).numerator
        R14 = R8 - R12
        R15 = R13 - R10

        if(R9 != 0 and R9%R2 == 0 and R14 != 0):
            break

    a = f10.replace('=', '')
    R14_list = make_choice_exclude0(R14)
    R15_list = make_choice(R15)
    index = R14_list.index(R14)
    choice_list = []
    for i in range(5):
        if(R15_list[i] != 0):
            choice_list.append(a.format(R11=R11, R14=R14_list[i], R15=R15_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$${R14}$$/수식$$'.format(R14=R14_list[i]))
    if(R15 != 0):
        choice_list[index] = a.format(R11=R11, R14=R14, R15=R15, left='{left}', right='{right}')
    else:
        choice_list[index] = '$$수식$${R14}$$/수식$$'.format(R14=R14)

    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, \
                R2=R2, R4=R4, R5=R5, R6=R6, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, R12=R12, R13=R13, R14=R14, R15=R15, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-408
def realnum311_Stem_294():
    stem = "실수 $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$, $$수식$$c`$$/수식$$, $$수식$$d`$$/수식$$에 대하여" \
           "$$수식$$rm A( it a`,~b)`$$/수식$$, $$수식$$rm B( it c`,~d)`$$/수식$$일 때, $$수식$$rm A△B`=` it ad`-`bc`$$/수식$$라 하자." \
           "{f1}, {f2}에 대하여 $$수식$$rm P TRIANGLE Q`$$/수식$$의 값은?\n" \
           "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f3}\n"\
              "{f4}\n"\
              "{f5}\n" \
              "{f6}\n"\
              "{f7}\n\n"

    f1 = conv('$$수식$$rm P  ( {N1} over {sqrt {N2}} ,~ sqrt {N3} `-`N4 sqrt {N5}  )$$/수식$$', 'N', 1, 5)
    f2 = conv('$$수식$$rm Q`  ( {N6} over {sqrt {N7}} ,~ sqrt {N2} `-` sqrt {N7}  ) `$$/수식$$', 'N', 2, 7)
    f3 = conv('$$수식$$rm P TRIANGLEQ`=`  ( {N1} over {sqrt {N2}} ,~ sqrt {N3} `-`N4 sqrt {N5}  ) TRIANGLE  ( {N6} over {sqrt {N7}} ,~ sqrt {N2} `-` sqrt {N7}  ) `$$/수식$$', 'N', 1, 7)
    f4 = conv('$$수식$$=` {N1} over {sqrt {N2}} ( sqrt {N2} `-` sqrt {N7} )`-`( sqrt {N3} `-`N4 sqrt {N5} )` TIMES` {N6} over {sqrt {N7}}$$/수식$$', 'N', 1, 7)
    f5 = conv('$$수식$$=`R1`-` {`R2 sqrt {R3}} over {sqrt {R4}} `-`R5`+` {`R6 sqrt {R4}} over {sqrt {R3}}$$/수식$$', 'R', 1, 6)
    f6 = conv('$$수식$$=`R1`-`R7 sqrt {R8} `-`R5`+`R9 sqrt {R8}$$/수식$$', 'R', 1, 9)
    f7 = conv('$$수식$$=`R10`-`R11 sqrt {R8}$$/수식$$', 'R', 8, 11)

    while True:
        N2 = make_sqrt(5)
        while True:
            N7 = make_sqrt(5)
            if (N7 != N2):
                break
        N1 = N2 * randint(2, 4)
        N3 = N7 * pow(randint(2, 4), 2)
        N4 = N7 * randint(1, 3)
        N5 = N2
        N6 = randint(1, 5)

        R1 = N1
        R2 = N1
        R3 = N7
        R4 = N2
        R5 = N6 * int(math.sqrt(N3 / N7))
        R6 = N4 * N6
        R7 = int(R2 / R4)
        R8 = N2 * N7
        R9 = int(R6 / R3)
        R10 = R1 - R5
        R11 = R7 - R9
        if(R10 != 0):
            break

    a = f7.replace('=', '')
    R10_list = make_choice_exclude0(R10)
    R11_list = make_choice(R11)
    index = R10_list.index(R10)
    choice_list = []
    for i in range(5):
        if (R11_list[i] != 0):
            choice_list.append(
                a.format(R8=R8, R10=R10_list[i], R11=R11_list[i], left='{left}', right='{right}'))
        else:
            choice_list.append('$$수식$${R10}$$/수식$$'.format(R10=R10_list[i]))
    if (R11 != 0):
        choice_list[index] = a.format(R8=R8, R10=R10, R11=R11, left='{left}', right='{right}')
    else:
        choice_list[index] = '$$수식$${R10}$$/수식$$'.format(R10=R10)

    stem = stem.format(f1=f1, f2=f2, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3],
                       s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f3=f3, f4=f4, f5=f5, f6=f6, f7='$$수식$$=`$$/수식$$'+choice_list[index]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, \
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-410
def realnum311_Stem_295():
    stem = "다음 중 두 실수의 대소 관계가 옳{cond} 것은?\n" \
           "① {s1}\n" \
           "② {s2}\n" \
           "③ {s3}\n" \
           "④ {s4}\n" \
           "⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "① {f1}\n"\
              "{f2}\n" \
              "∴ {a1}\n"\
              "② {f3}\n" \
              "{f4}\n"\
              "∴ {a2}\n" \
              "③ {f5}\n" \
              "{f6}\n" \
              "∴ {a3}\n" \
              "④ {f7}\n" \
              "{f8}\n" \
              "∴ {a4}\n" \
              "⑤ {f9}" \
              "{f10}\n" \
              "∴ {a5}\n\n"

    sel_list = []
    index = randint(0, 4)
    a1 = conv('$$수식$$sqrt {N1} `-`N2`ineq1`N2`$$/수식$$', 'N', 1, 2)
    a2 = conv('$$수식$$sqrt {N3} `-`N4`ineq2`-N4`+` sqrt {N5}$$/수식$$', 'N', 3, 5)
    a3 = conv('$$수식$$N6`-`N7 sqrt {N8} `ineq3`N7 sqrt {N8} `-`N9$$/수식$$', 'N', 6, 9)
    a4 = conv('$$수식$$N10`-` sqrt {{1} over {N11}} ineq4N10`-` sqrt {{1} over {N12}}$$/수식$$', 'N', 10, 12)
    a5 = conv('$$수식$$N13`-` sqrt {N14} `ineq5` sqrt {N14} `-`N15`$$/수식$$', 'N', 13, 15)

    f1 = conv('$$수식$$( sqrt {R1} `-`R2)`-`R2`= sqrt {R1} `-`R3`$$/수식$$', 'R', 1, 3)
    f2 = conv('$$수식$$=` sqrt {R1} `-` sqrt {R4} `ineq1`0$$/수식$$', 'R', 1, 4)
    f3 = conv('$$수식$$( sqrt {R5} `-`R6)`-`(-R6`+` sqrt {R7} )$$/수식$$', 'R', 5, 7)
    f4 = conv('$$수식$$=` sqrt {R5} `-` sqrt {R7} ineq2`0$$/수식$$', 'R', 5, 7)
    f5 = conv('$$수식$$(R8`-`R9 sqrt {R10} )`-`(R9 sqrt {10} `-`R11)`$$/수식$$', 'R', 8, 11)
    f6 = conv('$$수식$$=`R12`-`R13 sqrt {R10} `=` sqrt {R14} `-` sqrt {R15} `ineq3`0$$/수식$$', 'R', 10, 15)
    f7 = conv('$$수식$$ ( R16`-` sqrt {{1} over {R17}}  ) -  ( R16`-` sqrt {{1} over {R18}}  )$$/수식$$',
              'R', 16, 18)
    f8 = conv('$$수식$$=`- sqrt {{1} over {R17}} `+` sqrt {{1} over {R18}} `ineq4`0$$/수식$$', 'R', 17, 18)
    f9 = conv('$$수식$$(R19`-` sqrt {R20} )`-`( sqrt {R20} `-`R21)`$$/수식$$', 'R', 19, 21)
    f10 = conv('$$수식$$=R22`-`R23 sqrt {R20} `=` sqrt {R24} `-` sqrt {R25} `ineq5`0$$/수식$$', 'R', 20, 25)

    index = randint(0, 4)
    cond = randint(0, 1)

    # 1
    N1 = make_sqrt(13)
    N2 = randint(2, 5)
    R1 = N1
    R2 = N2
    R3 = N2 * 2
    R4 = R3 ** 2
    ineq1 = large_or_small(R1, R4)
    a1 = a1.replace('ineq1', ineq1)
    f2 = f2.replace('ineq1', ineq1)
    if ((cond) == (index == 0)):
        s1 = a1.replace(ineq1, large_or_small(R4, R1))
    else:
        s1 = a1

    # 2
    N3 = make_sqrt(13)
    N4 = randint(2, 5)
    while True:
        N5 = make_sqrt(13)
        if (N5 != N3):
            break
    R5 = N3
    R6 = N4
    R7 = N5
    ineq2 = large_or_small(R5, R7)
    a2 = a2.replace('ineq2', ineq2)
    f4 = f4.replace('ineq2', ineq2)
    if (cond == (index == 1)):
        s2 = a2.replace(ineq2, large_or_small(R7, R5))
    else:
        s2 = a2

    # 3
    N6 = randint(2, 6)
    N7 = randint(2, 3)
    N8 = make_sqrt(5)
    N9 = randint(2, 6)
    R8 = N6
    R9 = N7
    R10 = N8
    R11 = N9
    R12 = R8 + R11
    R13 = R9 * 2
    R14 = R12 ** 2
    R15 = R10 * (R13 ** 2)
    ineq3 = large_or_small(R14, R15)
    a3 = a3.replace('ineq3', ineq3)
    f6 = f6.replace('ineq3', ineq3)
    if (cond == (index == 2)):
        s3 = a3.replace(ineq3, large_or_small(R15, R14))
    else:
        s3 = a3

    # 4
    N10 = randint(2, 10)
    N11, N12 = random.sample([2, 3, 5, 6, 7, 10, 11, 13, 14], 2)
    R16 = N10
    R17 = N11
    R18 = N12
    ineq4 = large_or_small(R17, R18)
    a4 = a4.replace('ineq4', ineq4)
    f8 = f8.replace('ineq4', ineq4)
    if (cond == (index == 3)):
        s4 = a4.replace(ineq4, large_or_small(R18, R17))
    else:
        s4 = a4

    # 5
    N13 = randint(2, 5)
    N14 = make_sqrt()
    N15 = randint(2, 5)
    R19 = N13
    R20 = N14
    R21 = N15
    R22 = R19 + R21
    R23 = 2
    R24 = R22 ** 2
    R25 = R20 * (R23 ** 2)
    ineq5 = large_or_small(R24, R25)
    a5 = a5.replace('ineq5', ineq5)
    f10 = f10.replace('ineq5', ineq5)
    if (cond == (index == 4)):
        s5 = a5.replace(ineq5, large_or_small(R25, R24))
    else:
        s5 = a5

    stem = stem.format(cond=make_cond[cond], s1=s1, s2=s2, s3=s3, s4=s4, s5=s5) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, \
                N8=N8, N9=N9, N10=N10, N11=N11, N12=N12, N13=N13, N14=N14, N15=N15, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10, \
                             a1=a1, a2=a2, a3=a3, a4=a4, a5=a5) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9, N10=N10, N11=N11, N12=N12, N13=N13,
                N14=N14, N15=N15, \
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, R12=R12, R13=R13,
                R14=R14, R15=R15, R16=R16, R17=R17, \
                R18=R18, R19=R19, R20=R20, R21=R21, R22=R22, R23=R23, R24=R24, R25=R25, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-411
def realnum311_Stem_296():
    stem = "다음 세 수 $$수식$$a`$$/수식$$, $$수식$$b`$$/수식$$, $$수식$$c`$$/수식$$의 대소 관계를 바르게 나타낸 것은?\n" \
           "$$표$${f1}$$/표$$\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f2}이므로\n"\
              "{f3}\n"\
              "{f4}\n" \
              "{f5}이므로\n"\
              "{f6}\n" \
              "∴ {f7}\n\n"

    f1 = '$$수식$$a`=` {a}$$/수식$$, $$수식$$b`=` {b}`$$/수식$$, $$수식$$c`=` {c}`$$/수식$$'
    f2 = conv('$$수식$$R1`-`R2`=`( sqrt {R3} `+`R4)`-`R5=` sqrt {R3}`-`R6&gt;0`$$/수식$$', 'R', 1, 6)
    f3 = conv('$$수식$$R1`&gt;`R2`$$/수식$$', 'R', 1, 2)
    f4 = conv('$$수식$$R7`-R8`=`( sqrt {R3} `+`R4)`-`(R9- sqrt {R10} )`$$/수식$$', 'R', 3, 10)
    f5 = conv('$$수식$$=` sqrt {R3} `+` sqrt {R10} `-`R11&lt;`0$$/수식$$', 'R', 3, 11)
    f6 = conv('$$수식$$R7`&lt;`R8`$$/수식$$', 'R', 7, 8)
    f7 = conv('$$수식$$R2&lt;R1&lt;R8$$/수식$$', 'R', 1, 8)

    N1 = make_sqrt(5)
    N2 = randint(1, 3)
    while True:
        N4 = make_sqrt(5)
        if(N4 != N1):
            break
    N3 = int(math.sqrt(N1))+N2+int(math.sqrt(N4))+randint(2, 4)
    N5 = N2 + 1
    max_list = ['a', 'b', 'c']
    max_dict = {'a':0, 'b':0, 'c':0}
    random.shuffle(max_list)

    max_dict[max_list[0]] = '`N3`-` sqrt {N4} `'
    max_dict[max_list[1]] = ' sqrt {N1} `+`N2`'
    max_dict[max_list[2]] = '`N5'
    f1 = conv(f1.format(a=max_dict['a'], b=max_dict['b'], c=max_dict['c']), 'N', 1, 5)

    R1 = max_list[1]
    R2 = max_list[2]
    R3 = N1
    R4 = N2
    R5 = N5
    R6 = R5 - R4
    R7 = R1
    R8 = max_list[0]
    R9 = N3
    R10 = N4
    R11 = R9 - R4

    a = f7.format(R2=R2,R1=R1,R8=R8)
    abc_list = ['$$수식$$a&lt;b&lt;c$$/수식$$', '$$수식$$a&lt;c&lt;b$$/수식$$', '$$수식$$b&lt;a&lt;c$$/수식$$', '$$수식$$b&lt;c&lt;a$$/수식$$', '$$수식$$c&lt;a&lt;b$$/수식$$', '$$수식$$c&lt;b&lt;a$$/수식$$']
    while True:
        choice_list = random.sample(abc_list, 5)
        if(a in choice_list):
            choice_list.sort()
            break
    index = choice_list.index(a)

    stem = stem.format(f1=f1, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f2=f2,f3=f3,f4=f4,f5=f5,f6=f6,f7=f7)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-416
def realnum311_Stem_297():
    stem = "두 실수의 대소 관계가 옳{cond} 것을 보기에서 모두 고른 것은?\n" \
           "$$표$$㈀ {s1}\n" \
           "㈁ {s2}\n" \
           "㈂ {s3}\n" \
           "㈃ {s4}$$/표$$\n" \
           "① {c1}     ② {c2}    ③ {c3}     ④ {c4}     ⑤ {c5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "㈀ {f1}\n"\
              "{f2}\n" \
              "{f3}\n" \
              "∴ {a1}\n"\
              "㈁ {f4}\n" \
              "{f5}\n"\
              "∴ {a2}\n" \
              "㈂ {f6}\n" \
              "{f7}\n" \
              "{f8}\n" \
              "∴ {a3}\n" \
              "㈃ {f9}\n" \
              "{f10}\n" \
              "{f11}\n" \
              "∴ {a4}\n" \
              "이상에서 옳은 것은 {a}이다.\n"

    a1 = conv('$$수식$$sqrt {N1} `+` sqrt {N2} ` ineq1` sqrt {N3} `+` sqrt {N4} `$$/수식$$', 'N', 1, 4)
    a2 = conv('$$수식$$`N5 sqrt {N6} `+`N7 sqrt {N8} ` ineq2`N9 sqrt {N6} `+`N10 sqrt {N8} `$$/수식$$', 'N', 5, 10)
    a3 = conv('$$수식$$N11`+` sqrt {N12} ` ineq3`N13`+` sqrt {N14} `$$/수식$$', 'N', 11, 14)
    a4 = conv('$$수식$$`N15 sqrt {N16} `+` sqrt {N17} ` ineq4` sqrt {N18} `+` sqrt {N19} `$$/수식$$', 'N', 15, 19)

    f1 = conv('$$수식$$( sqrt {N1} `+` sqrt {N2} )`-`( sqrt {N3} `+` sqrt {N4} )`$$/수식$$', 'N', 1, 4)
    f2 = conv('$$수식$$`=` sqrt {R1} `+`R2 sqrt {R3} `-`R4 sqrt {R1} `-` sqrt {R3} `$$/수식$$', 'R', 1, 4)
    f3 = conv('$$수식$$=`R5 sqrt {R3} `-`R6 sqrt {R1} `ineq1`0$$/수식$$', 'R', 1, 6)

    f4 = conv('$$수식$$(`N5 sqrt {N6} `+`N7 sqrt {N8} )`-`(`N9 sqrt {N6} `+`N10 sqrt {N8} )`$$/수식$$', 'N', 5, 10)
    f5 = conv('$$수식$$=`R7 sqrt {R8} `-`R9 sqrt {R10} `ineq2`0$$/수식$$', 'R', 7, 10)

    f6 = conv('$$수식$$(N11`+` sqrt {N12} )`-`(N13`+` sqrt {N14} )`$$/수식$$', 'N', 11, 14)
    f7 = conv('$$수식$$=`R11`+`R12 sqrt {R13} `-`R14`-`R15 sqrt {R13} `=`R16`-`R17 sqrt {R18}`$$/수식$$', 'R', 11, 18)
    f8 = conv('$$수식$$=` sqrt {R19} `-`R17 sqrt {R18} `ineq3`0$$/수식$$', 'R', 17, 19)

    f9 = conv('$$수식$$(`N15 sqrt {N16} `-` sqrt {N17} )`-`( sqrt {N18} `+` sqrt {N19} )`$$/수식$$', 'N', 15, 19)
    f10 = conv('$$수식$$=`R20 sqrt {R21} `-`R22 sqrt {R23} `-`R24 sqrt {R21} `-`R25 sqrt {R23}$$/수식$$', 'R', 19, 25)
    f11 = conv('$$수식$$`=`R26 sqrt {R21} `-`R27 sqrt {R23} `=` sqrt {R28} `-` sqrt {R29} `ineq4`0$$/수식$$', 'R', 20, 29)

    index = random.sample(range(4), 2)
    index.sort()
    cond = randint(0, 1)

    # 1
    N1 = make_sqrt(13)
    while True:
        N4 = make_sqrt(13)
        if(N4!=N1):
            break
    N2 = N4 * 4
    N3 = N1 * 4
    R1 = N1
    R2 = 2
    R3 = N4
    R4 = 2
    R5 = 1
    R6 = 1
    ineq1 = large_or_small(N4, N1)
    a1 = a1.replace('ineq1', ineq1)
    f3 = f3.replace('ineq1', ineq1)
    if ((cond) == (0 in index)):
        s1 = a1.replace(ineq1, large_or_small(N1, N4))
    else:
        s1 = a1

    # 2
    N5 = make_excludeunder1(4)
    N6 = make_sqrt(5)
    N7 = make_excludeunder1(4)
    while True:
        N8 = make_sqrt(5)
        if(N8 != N5):
            break
    N9 = N5 - 1
    N10 = N7 + 1
    R7 = 1
    R8 = N6
    R9 = 1
    R10 = N8
    ineq2 = large_or_small(R8, R10)
    a2 = a2.replace('ineq2', ineq2)
    f5 = f5.replace('ineq2', ineq2)
    if (cond == (1 in index)):
        s2 = a2.replace(ineq2, large_or_small(R10, R8))
    else:
        s2 = a2

    # 3
    N11 = randint(5, 8)
    r = randint(1, 3)
    N12 = make_sqrt() * (r**2)
    N13 = randint(1, 4)
    N14 = int(N12/(r**2)) * ((r+1)**2)
    R11 = N11
    R12 = r
    R13 = int(N12/(r**2))
    R14 = N13
    R15 = r+1
    R16 = N11 - N13
    R17 = 1
    R18 = R13
    R19 = R16**2
    ineq3 = large_or_small(R19, R18)
    a3 = a3.replace('ineq3', ineq3)
    f8 = f8.replace('ineq3', ineq3)
    if (cond == (2 in index)):
        s3 = a3.replace(ineq3, large_or_small(R18, R19))
    else:
        s3 = a3

    # 4
    N15 = randint(5, 6)
    N16 = make_sqrt(5)
    while True:
        N19 = make_sqrt(5)
        if(N19 != N16):
            break
    N17 = N19 * pow(randint(2, 3), 2)
    N18 = N16 * pow(randint(2, 3), 2)
    R20 = N15
    R21 = N16
    R22 = int(math.sqrt(N17/N19))
    R23 = N19
    R24 = int(math.sqrt(N18/N16))
    R25 = 1
    R26 = R20 - R24
    R27 = R22 + 1
    R28 = (R26**2) * R21
    R29 = (R27**2) * R23
    ineq4 = large_or_small(R28, R29)
    a4 = a4.replace('ineq4', ineq4)
    f11 = f11.replace('ineq4', ineq4)
    if (cond == (3 in index)):
        s4 = a4.replace(ineq4, large_or_small(R29, R28))
    else:
        s4 = a4

    a = answer_dict_ko[index[0]]+', '+answer_dict_ko[index[1]]
    abc_list = ['㈀, ㈁', '㈀, ㈂', '㈀, ㈃', '㈁, ㈂', '㈁, ㈃', '㈂, ㈃']
    while True:
        choice_list = random.sample(abc_list, 5)
        if(a in choice_list):
            choice_list.sort()
            break
    index = choice_list.index(a)
    stem = stem.format(cond=make_cond[cond], s1=s1, s2=s2, s3=s3, s4=s4,
                       c1=choice_list[0], c2=choice_list[1], c3=choice_list[2], c4=choice_list[3], c5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9, N10=N10, N11=N11,
                N12=N12, N13=N13, N14=N14, N15=N15, N16=N16, N17=N17, N18=N18, N19=N19, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10, f11=f11,\
                             a=a, a1=a1, a2=a2, a3=a3, a4=a4) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, N8=N8, N9=N9, N10=N10, N11=N11, N12=N12, N13=N13,
                N14=N14, N15=N15, N16=N16, N17=N17, N18=N18, N19=N19, \
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, R12=R12, R13=R13,
                R14=R14, R15=R15, R16=R16, R17=R17, R18=R18, R19=R19, R20=R20, R21=R21, R22=R22, R23=R23, R24=R24,
                R25=R25, R26=R26, R27=R27, R28=R28, R29=R29, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-417
def realnum311_Stem_298():
    stem = "세 수 $$수식$$a`=` {a}$$/수식$$, $$수식$$b`=` {b}`$$/수식$$, $$수식$$c`=` {c}`$$/수식$$의 대소를 비교하면?\n" \
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n" \
              "이므로\n"\
              "{f2}\n"\
              "{f3}\n" \
              "이므로\n" \
              "{f4}\n"\
              "∴ {f5}\n\n"

    f1 = conv('$$수식$$R1`-`R2`=`( sqrt {R3} `+` sqrt {R4} )`-`2 sqrt {R3} `=` sqrt {R4} `-` sqrt {R3} `&gt;`0$$/수식$$', 'R', 1, 4)
    f2 = conv('$$수식$$R1`&gt;`R2$$/수식$$', 'R', 1, 2)
    f3 = conv('$$수식$$R5`-`R2`=`(`R6 sqrt {R7} `-` sqrt {R8} )`-`R7 sqrt {R8} `=`R6 sqrt {R7} `-`R6 sqrt {R8} `&lt;`0$$/수식$$', 'R', 2, 8)
    f4 = conv('$$수식$$R5`&lt;`R2$$/수식$$', 'R', 2, 5)
    f5 = conv('$$수식$$R5&lt;R2&lt;R1$$/수식$$', 'R', 1, 5)

    while True:
        N1, N2 = random.sample([5, 7, 11], 2)
        if(N2 > N1):
            break
    N3 = 2
    N4 = N1
    N5 = 3
    N6 = make_sqrt(3)
    N7 = N1

    max_list = ['a', 'b', 'c']
    max_dict = {'a':0, 'b':0, 'c':0}
    random.shuffle(max_list)

    max_dict[max_list[0]] = conv('sqrt {N1} `+` sqrt {N2}', 'N', 1, 2)
    max_dict[max_list[1]] = conv('`N3 sqrt {N4} `', 'N', 3, 4)
    max_dict[max_list[2]] = conv('`N5 sqrt {N6} `-` sqrt {N7} `', 'N', 5, 7)

    R1 = max_list[0]
    R2 = max_list[1]
    R3 = N1
    R4 = N2
    R5 = max_list[2]
    R6 = N5
    R7 = N6
    R8 = N7

    a = f5.format(R1=R1, R2=R2, R5=R5)
    abc_list = ['$$수식$$a&lt;b&lt;c$$/수식$$', '$$수식$$a&lt;c&lt;b$$/수식$$', '$$수식$$b&lt;a&lt;c$$/수식$$', '$$수식$$b&lt;c&lt;a$$/수식$$', '$$수식$$c&lt;a&lt;b$$/수식$$', '$$수식$$c&lt;b&lt;a$$/수식$$']
    while True:
        choice_list = random.sample(abc_list, 5)
        if(a in choice_list):
            choice_list.sort()
            break
    index = choice_list.index(a)

    stem = stem.format(a=max_dict['a'], b=max_dict['b'], c=max_dict['c'], s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-420
def realnum311_Stem_299():
    stem = "반지름의 길이가 $$수식$${a}$$/수식$$, $$수식$${b}$$/수식$$, $$수식$${c}$$/수식$$인 세 원을 각각 $$수식$$A`$$/수식$$, $$수식$$B`$$/수식$$, $$수식$$C`$$/수식$$라 할 때, 넓이가 가장 큰 원을 말하시오.\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}이므로\n"\
              "{f2}\n"\
              "{f3}이므로\n" \
              "{f4}\n"\
              "∴ {f5}\n" \
              "따라서 {f6}{post} 가장 큰 수이므로 {f7}의 넓이가 가장 크다.\n\n"

    f1 = conv('$$수식$$(R1`-` sqrt {R2} )`-`R3`=`R4`-` sqrt {R2} `&lt;`0$$/수식$$', 'R', 1, 4)
    f2 = conv('$$수식$$R1`-` sqrt {R2} `&lt;`R3`$$/수식$$', 'R', 1, 3)
    f3 = conv('$$수식$$R5`-`(R6`-` sqrt {R7} )`=`R8`+` sqrt {R7} `&gt;`0$$/수식$$', 'R', 5, 8)
    f4 = conv('$$수식$$R5`&gt;`R6`-` sqrt {R7} `$$/수식$$', 'R', 5, 7)
    f5 = conv('$$수식$$N4`-` sqrt {N5} `&lt;`N1`-` sqrt {N2} `&lt;`N3$$/수식$$', 'N', 1, 5)
    f6 = conv('$$수식$$N3$$/수식$$', 'N', 3, 3)
    f7 = conv('$$수식$$a$$/수식$$', 'N', 0, 0)

    max_list = ['A', 'B', 'C']
    max_dict = {'A':0, 'B':0, 'C':0}
    random.shuffle(max_list)

    max_dict[max_list[0]] = conv('N4`-` sqrt {N5} `', 'N', 4, 5)
    max_dict[max_list[1]] = conv('N1`-` sqrt {N2} `', 'N', 1, 2)
    max_dict[max_list[2]] = conv('N3', 'N', 3, 3)

    while True:
        N1 = randint(3, 7)
        N2 = random.choice([5, 7])
        N3 = N1 - randint(1, 2)
        N4 = N3 - make_exclude0(1)
        while True:
            N5 = make_sqrt(13)
            if (N5 > N2):
                break
        #모두 양수면
        if((N1**2 > N2) and (N4**2 > N5)):
            break

    R1 = N1
    R2 = N2
    R3 = N3
    R4 = R1 - R3
    R5 = N3
    R6 = N4
    R7 = N5
    R8 = R5 - R6
    f7 = f7.replace('a', max_list[2])

    stem = stem.format(a=max_dict['A'], b=max_dict['B'], c=max_dict['C']) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, left=left, right=right)
    answer = answer.format(a=max_list[2])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, post=make_post(N3)) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-421
def realnum311_Stem_300():
    stem = "세 수 $$수식$$a`=` {a}$$/수식$$, $$수식$$b`=` {b}`$$/수식$$, $$수식$$c`=` {c}`$$/수식$$의 대소를 비교하면?\n" \
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}\n" \
              "{f2}\n" \
              "{f3}\n" \
              "이므로 {f4}\n"\
              "{f5}\n"\
              "{f6}\n" \
              "{f7}\n" \
              "이므로 {f8}\n" \
              "따라서 {f4}, {f8}이므로 {f9}\n\n"

    f1 = conv('$$수식$$R1`-`R2`=`(R3 sqrt {R4} `+`R5)`-`(R6`-` sqrt {R4} )`$$/수식$$', 'R', 1, 6)
    f2 = conv('$$수식$$=`R7 sqrt {R4} `-`R8$$/수식$$', 'R', 4, 8)
    f3 = conv('$$수식$$=` sqrt {R9} `-` sqrt {R10} `&lt;`0$$/수식$$', 'R', 9, 10)
    f4 = conv('$$수식$$R1`&lt;`R2$$/수식$$', 'R', 1, 2)
    f5 = conv('$$수식$$R11`-`R12`=`(`R3 sqrt {R4} `+`R5)`-`(`R13 sqrt {R14} `+`R5)`$$/수식$$', 'R', 3, 14)
    f6 = conv('$$수식$$`=`R3 sqrt {R4} `-`R13 sqrt {R14} `$$/수식$$', 'R', 3, 14)
    f7 = conv('$$수식$$=` sqrt {R15} `-` sqrt {R16} `&gt;`0$$/수식$$', 'R', 15, 16)
    f8 = conv('$$수식$$R11`&gt;`R12$$/수식$$', 'R', 11, 12)
    f9 = conv('$$수식$$R12&lt;R11&lt;R2$$/수식$$', 'R', 2, 12)

    max_list = ['A', 'B', 'C']
    max_dict = {'A':0, 'B':0, 'C':0}
    random.shuffle(max_list)

    max_dict[max_list[0]] = conv('`N5 sqrt {N6} `+`N7`', 'N', 5, 7)
    max_dict[max_list[1]] = conv('`N1 sqrt {N2} `+`N3`', 'N', 1, 3)
    max_dict[max_list[2]] = conv('`N4`-` sqrt {N2} `', 'N', 2, 4)

    while True:
        sq1, sq2 = random.sample([8, 12, 18, 20, 24, 27, 45, 54], 2)
        if(sq1 > sq2):
            break
    sq_li1 = sqrt_calc(sq1)
    sq_li2 = sqrt_calc(sq2)
    N1 = sq_li1[0]
    N2 = sq_li1[1]
    N3 = randint(1, 5)
    N4 = randint(13, 17)
    N5 = sq_li2[0]
    N6 = sq_li2[1]
    N7 = N3

    R1 = max_list[1]
    R2 = max_list[2]
    R3 = N1
    R4 = N2
    R5 = N3
    R6 = N4
    R7 = R3 + 1
    R8 = R6 - R5
    R9 = R4 * (R7**2)
    R10 = R8**2
    R11 = R1
    R12 = max_list[0]
    R13 = N5
    R14 = N6
    R15 = sq1
    R16 = sq2

    a = f9.format(R2=R2, R11=R11, R12=R12)
    abc_list = ['$$수식$$A&lt;B&lt;C$$/수식$$', '$$수식$$A&lt;C&lt;B$$/수식$$', '$$수식$$B&lt;A&lt;C$$/수식$$', '$$수식$$B&lt;C&lt;A$$/수식$$', '$$수식$$C&lt;A&lt;B$$/수식$$', '$$수식$$C&lt;B&lt;A$$/수식$$']
    while True:
        choice_list = random.sample(abc_list, 5)
        if(a in choice_list):
            choice_list.sort()
            break
    index = choice_list.index(a)

    stem = stem.format(a=max_dict['A'], b=max_dict['B'], c=max_dict['C'], s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, R9=R9, R10=R10, R11=R11, R12=R12, R13=R13, R14=R14, R15=R15, R16=R16, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-422
def realnum311_Stem_301():
    stem = "다음 수를 크기가 큰 것부터 차례대로 나열한 것은?\n" \
           "$$표$$$$수식$${a}, {b}, {c}, {d}$$/수식$$$$/표$$\n" \
           "① {s1}\n" \
           "② {s2}\n" \
           "③ {s3}\n" \
           "④ {s4}\n" \
           "⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f1}{post1} 음수이고, {f2}, {f3}, {f4}{post2} 양수이다. \n"\
              "{f5}이므로\n" \
              "{f6}\n"\
              "{f7}\n" \
              "이므로\n" \
              "{f8}\n"\
              "∴ {f9}\n" \
              "따라서 큰 것부터 차례대로 나열한 것은 {a}이다.\n"

    f5 = conv('$$수식$$( sqrt {N3} `+` sqrt {N2} )`-`(N1`+` sqrt {N2} )`=` sqrt {N3} `-`N1`&gt;`0$$/수식$$', 'N', 1, 3)
    f6 = conv('$$수식$$sqrt {N3} `+` sqrt {N2} `&gt;`N1`+` sqrt {N2} `$$/수식$$', 'N', 1, 3)
    f7 = conv('$$수식$$(`R1`+` sqrt {R2} )`-`R3`=`-R4`+` sqrt {R2} `=`- sqrt {R5} `+` sqrt {R2} `&gt;`0$$/수식$$', 'R', 1, 5)
    f8 = conv('$$수식$$N1`+` sqrt {N2} `&gt;`N5`$$/수식$$', 'N', 1, 5)
    f9 = conv('$$수식$$ sqrt {N3} `+` sqrt {N2} &gt;N1`+` sqrt {N2} &gt;N5&gt;N4`-` sqrt {N2} `$$/수식$$', 'N', 1, 5)

    max_list = ['A', 'B', 'C', 'D']
    max_dict = {'A':0, 'B':0, 'C':0, 'D':0}
    random.shuffle(max_list)

    max_dict[max_list[0]] = conv('$$수식$$`N4`-` sqrt {N2}$$/수식$$', 'N', 2, 4)
    max_dict[max_list[1]] = conv('$$수식$$N5$$/수식$$', 'N', 5, 5)
    max_dict[max_list[2]] = conv('$$수식$$N1`+` sqrt {N2}$$/수식$$', 'N', 1, 2)
    max_dict[max_list[3]] = conv('$$수식$$sqrt {N3} `+` sqrt {N2}$$/수식$$', 'N', 2, 3)

    f1 = max_dict[max_list[0]]
    f2 = max_dict[max_list[3]]
    f3 = max_dict[max_list[2]]
    f4 = max_dict[max_list[1]]

    N2 = make_sqrt(13)
    while True:
        N3 = make_sqrt(13)
        if(N3 != N2):
            break
    N1 = randint(1, int(math.sqrt(N3)))
    N4 = make_exclude0(int(math.sqrt(N2)))
    while True:
        N5 = randint(1, (int(math.sqrt(N2)) + 1) + N1)
        if(N5 != N1):
            break

    R1 = N1
    R2 = N2
    R3 = N5
    R4 = R3 - R1
    R5 = R4**2

    a = f9
    abc_list = [[3, 2, 1, 0], [3, 1, 2, 0], [3, 2, 0, 1], [3, 1, 0, 2], [2, 3, 1, 0], [2, 3, 0, 1], [2, 1, 3, 0]]
    while True:
        sel_list = random.sample(abc_list, 5)
        if([3, 2, 1, 0] in sel_list):
            break
    index = sel_list.index([3, 2, 1, 0])
    choice_list = []
    for i in range(5):
        str = '$$수식$$'
        for j in sel_list[i]:
            str += max_dict[max_list[j]]
            if(j != sel_list[i][3]):
                str += ', '
        str += '$$/수식$$'
        choice_list.append(str)

    stem = stem.format(a=max_dict['A'], b=max_dict['B'], c=max_dict['C'], d=max_dict['D'], s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(a=answer_dict[index], f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, post1 = make_post(N2), post2 = make_post(N5)) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-423
def realnum311_Stem_302():
    stem = "다음 수를 수직선 위에 나타낼 때, 오른쪽에서 두 번째에 오는 수와 왼쪽에서 두 번째에 오는 수를 차례로 구한 것은?\n" \
           "$$표$$$$수식$${a}, {b}, {c}, {d}, {e}$$/수식$$$$/표$$\n" \
           "① {s1}\n" \
           "② {s2}\n" \
           "③ {s3}\n" \
           "④ {s4}\n" \
           "⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "(ⅰ) 음수: {f1}, {f2}\n"\
              "{f3}이므로\n"\
              "{f4}\n" \
              "(ⅱ) 양수: {f5}, {f6}, {f7}\n"\
              "{f8}이므로\n" \
              "{f9}\n" \
              "{f10}\n" \
              "{f11}이므로\n" \
              "{f12}\n" \
              "{f13}\n" \
              "(ⅰ), (ⅱ)에서\n" \
              "{f14}\n" \
              "따라서 수를 수직선 위에 나타낼 때, 왼쪽에서 오른쪽으로 갈수록 큰 수이므로 오른쪽에서 두 번째에 오는 수는 {f15}이고, 왼쪽에서 두 번째에 오는 수는 {f16}이다. "

    f1 = conv('$$수식$$- sqrt {N3} `+`N4$$/수식$$', 'N', 3, 4)
    f2 = conv('$$수식$$N4`-` sqrt {N5}$$/수식$$', 'N', 4, 5)
    f3 = conv('$$수식$$(- sqrt {N3} `+`N4)`-`(N4`-` sqrt {N5} )`=`- sqrt {N3} `+` sqrt {N5} `&lt;`0$$/수식$$', 'N', 3, 5)
    f4 = conv('$$수식$$- sqrt {N3} `+`N4`&lt;`N4`-` sqrt {N5}$$/수식$$', 'N', 3, 5)

    f5 = conv('$$수식$$sqrt {N1} `+`N2$$/수식$$', 'N', 1, 2)
    f6 = conv('$$수식$$N6`-` sqrt {N1}$$/수식$$', 'N', 1, 6)
    f7 = conv('$$수식$$N7$$/수식$$', 'N', 7, 7)
    f8 = conv('$$수식$$( sqrt {R1} `+`R2)`-`R3`=` sqrt {R1} `-`R4&gt;`0$$/수식$$', 'R', 1, 4)
    f9 = conv('$$수식$$sqrt {N1} `+`N2`&gt;`N7$$/수식$$', 'N', 1, 7)
    f10 = conv('$$수식$$( sqrt {N1} `+`N2)`-`(N6`-` sqrt {N1} )`$$/수식$$', 'N', 1, 6)
    f11 = conv('$$수식$$=`2 sqrt {R5} `-`R6`=` sqrt {R7} `-` sqrt {R8} `&lt;`0$$/수식$$', 'R', 5, 8)
    f12 = conv('$$수식$$sqrt {N1} `+`N2`&lt;`N6`-` sqrt {N1}$$/수식$$', 'N', 1, 6)
    f13 = conv('$$수식$$THEREFORE~N7`&lt;` sqrt {N1} `+`N2`&lt;`N6`-` sqrt {N1}$$/수식$$', 'N', 1, 7)
    f14 = conv('$$수식$$- sqrt {N3} `+`N4 &lt; N4`-` sqrt {N5} &lt; N7 &lt; sqrt {N1} +N2 &lt; N6`-` sqrt {N1}$$/수식$$', 'N', 1, 7)

    max_list = ['A', 'B', 'C', 'D', 'E']
    max_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    random.shuffle(max_list)

    max_dict[max_list[0]] = conv('$$수식$$- sqrt {N3} `+`N4$$/수식$$', 'N', 3, 4)
    max_dict[max_list[1]] = conv('$$수식$$N4`-` sqrt {N5}$$/수식$$', 'N', 4, 5)
    max_dict[max_list[2]] = conv('$$수식$$N7$$/수식$$', 'N', 7, 7)
    max_dict[max_list[3]] = conv('$$수식$$sqrt {N1} `+`N2$$/수식$$', 'N', 1, 2)
    max_dict[max_list[4]] = conv('$$수식$$N6`-` sqrt {N1}$$/수식$$', 'N', 1, 6)

    f15 = max_dict[max_list[3]]
    f16 = max_dict[max_list[1]]

    while True:
        N1 = make_sqrt()
        N2 = randint(1, 5)
        while True:
            N3, N5 = random.sample([2, 3, 5, 6, 7, 10, 11, 13, 14, 15], 2)
            if (N3 > N5):
                break
        N4 = make_exclude0(8)
        N6 = randint(5, 15)
        N7 = randint(5, 15)

        R1 = N1
        R2 = N2
        R3 = N7
        R4 = R3 - R2
        R5 = N1
        R6 = N6 - N2
        R7 = R5 * 4
        R8 = R6**2

        if(R1 > R4**2 and R8 > R7):
            break

    abc_list = [[4, 0], [4, 1], [4, 2], [3, 0], [3, 1], [3, 2], [2, 3]]
    while True:
        sel_list = random.sample(abc_list, 5)
        if ([3, 1] in sel_list):
            break
    index = sel_list.index([3, 1])
    choice_list = []
    for i in range(5):
        str = '$$수식$$'
        for j in sel_list[i]:
            str += max_dict[max_list[j]]
            if (j != sel_list[i][1]):
                str += ', '
        str += '$$/수식$$'
        choice_list.append(str)

    stem = stem.format(a=max_dict['A'], b=max_dict['B'], c=max_dict['C'], d=max_dict['D'], e=max_dict['E'],
                       s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10, f11=f11, f12=f12, f13=f13, f14=f14, f15=f15, f16=f16) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, N5=N5, N6=N6, N7=N7, \
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, R7=R7, R8=R8, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)


# 3-1-1-426
def realnum311_Stem_303():
    stem = "{f1}, {f2}일 때, {f3}의 값은?\n"\
        "① {s1}     ② {s2}    ③ {s3}     ④ {s4}     ⑤ {s5}\n"
    answer = "(답) {a}\n"
    comment = "(해설)\n" \
              "{f4}\n"\
              "{f5}\n"\
              "{f6}\n" \
              "{f7}\n\n"

    f1 = conv('$$수식$$a=N1$$/수식$$', 'N', 1, 1)
    f2 = conv('$$수식$$b= sqrt {N2} +N3$$/수식$$', 'N', 2, 3)
    f3 = conv('$$수식$$sqrt {(a+b) ^{2}} - sqrt {(a-b) ^{2}}$$/수식$$', 'N', 0, 0)
    f4 = conv('$$수식$$a+b`=`N1`+`( sqrt {N2} `+`N3)`=`N4`+` sqrt {N2} `&gt;`0$$/수식$$', 'N', 1, 4)
    f5 = conv('$$수식$$a-b`=`R1`-`( sqrt {R2} `+`R3)`=`R4`-` sqrt {R2} `=` sqrt {R5} `-` sqrt {R2} `&lt;`0$$/수식$$', 'R', 1, 5)
    f6 = conv('$$수식$$THEREFORE~ sqrt {(a+b) ^{2}} - sqrt {(a-b) ^{2}} =a+b+(a-b)$$/수식$$', 'N', 0, 0)
    f7 = conv('$$수식$$=2a`=`2 TIMESR1`=`R6$$/수식$$', 'R', 1, 6)

    N1 = randint(4, 10)
    N2 = random.choice([11, 13, 14, 15, 17, 19, 21])
    N3 = N1 - randint(1, 3)
    N4 = N1 + N3

    R1 = N1
    R2 = N2
    R3 = N3
    R4 = R1 - R3
    R5 = R4**2
    R6 = 2 * R1

    a = '$$수식$$`{R6}$$/수식$$'
    R6_list = make_choice(R6)
    index = R6_list.index(R6)
    choice_list = []
    for i in range(5):
        choice_list.append(a.format(R6=R6_list[i], left='{left}', right='{right}'))

    stem = stem.format(f1=f1, f2=f2, f3=f3, s1=choice_list[0], s2=choice_list[1], s3=choice_list[2], s4=choice_list[3], s5=choice_list[4]) \
        .format(N1=N1, N2=N2, N3=N3, N4=N4, left=left, right=right)
    answer = answer.format(a=answer_dict[index])
    comment = comment.format(f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7)\
        .format(N1=N1, N2=N2, N3=N3, N4=N4,\
                R1=R1, R2=R2, R3=R3, R4=R4, R5=R5, R6=R6, left=left, right=right)

    return return_conv(stem), return_conv(answer), return_conv(comment)