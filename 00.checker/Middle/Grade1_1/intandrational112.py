import random
import copy

import numpy as np
import operator

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


def gcd (a, b):
    if b == 0:
        return a
    else:
        if a < b:
            a, b = b, a
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def factor(a):
    fac_list = []
    for i in range(a):
        if lcm(i+1, a) == a:
            fac_list.append(i+1)
    return fac_list

def random_minus(list1):
    random_list = []
    for i in range(len(list1)):
        rf = np.random.randint(0,2)
        if rf == 0:
            random_list.append(list1[i])
        else:
            random_list.append(-list1[i])
    return random_list

def random_minustmp(list1):
    random_list = []
    for i in range(len(list1)):
            random_list.append(list1[i])
       
    return random_list


# contract fraction a/b
def ctr_frac(a, b):
    if a == 0:
        return [0, 1]
    if b < 0:
        if a < 0:
            a = abs(a)
            b = abs(b)
        else:
            a = -a
            b = abs(b)

    isminus = 0
    if a < 0:
        a = abs(a)
        isminus = 1

    if gcd(a,b) == 1:
        return [-1, "already contracted fraction"]
    else:
        if isminus == 0:
            return [int(a/gcd(a,b)), int(b/gcd(a,b))]
        else:
            return [-int(a/gcd(a,b)), int(b/gcd(a,b))]

def ctr_frac2(a, b):
    if a == 0:
        return [0, 1]
    if b < 0:
        if a < 0:
            a = abs(a)
            b = abs(b)
        else:
            a = -a
            b = abs(b)
    if a < 0:
        a = abs(a)
        return [-int(a/gcd(a,b)), int(b/gcd(a,b))]
    else:
        return [int(a/gcd(a,b)), int(b/gcd(a,b))]


#  a[0]/a[1] + b[0]/b[1]
def sum_frac(a, b):
    lcm_ = lcm(a[1], b[1])
    if a[0] * int(lcm_/a[1]) + b[0] * int(lcm_/b[1]) == 0:
        return [0, 1]
    ctr = ctr_frac2(a[0] * int(lcm_/a[1]) + b[0] * int(lcm_/b[1]), lcm_)
    return [ctr[0], ctr[1]]


# big == 0 : generate fraction less than 1
def frac_generator(big, base, high):
    nums = random.sample(list(range(1,base)),2)
    if big == 0:
        nums.sort()
    ctr = ctr_frac2(nums[0], nums[1])
    if big != 0:
        randoms = np.random.randint(0,high)
        ctr = sum_frac(ctr, [randoms,1])
    while ctr[1] == 1:
        nums = random.sample(list(range(1,10)),2)
        if big == 0:
            nums.sort()
        ctr = ctr_frac2(nums[0], nums[1])
        if big != 0:
            randoms = np.random.randint(0,high)
            ctr = sum_frac(ctr, [randoms,1])
    return [ctr[0], ctr[1]]


def frac_generator2(big, base_list, high):
    base_num = random.sample(base_list, 1)[0]
    coprime_list = []
    for i in range(base_num-1):
        if gcd(base_num, i+1) == 1:
            coprime_list.append(i+1)
    
    n = random.sample(coprime_list, 1)[0]
    ctr = [n, base_num]

    if big != 0:
        randoms = np.random.randint(0,high)
        ctr = sum_frac(ctr, [randoms,1])

    return [ctr[0], ctr[1]]


def frac_sum3(a, b):
    res = sum_frac(a[0], b[0])
    if res[0] > 0:
        return (res, res[0]/res[1], " {%d} over {%d} " % (res[0], res[1]))
    else:
        return (res, res[0]/res[1], " -{%d} over {%d} " % (abs(res[0]), res[1]))


def frac_minus3(a, b):
    f = a[0]
    s = [-b[0][0], b[0][1]]
    res = sum_frac(f, s)
    if res[0] > 0:
        return (res, res[0]/res[1], " {%d} over {%d} " % (res[0], res[1]))
    else:
        return (res, res[0]/res[1], "-{%d} over {%d} " % (abs(res[0]), res[1]))


def frac_gen3(minus, big, base_list, high):
    base_num = random.sample(base_list, 1)[0]

    if base_num == 1:
        hi = np.random.randint(1, high)
        if minus == 0:
            return ([hi, 1], hi, str(hi))
        elif minus == -1:
            return ([-hi, 1], -hi, str(-hi))
        else:
            rf = np.random.randint(0,2)
            if rf == 0:
                return ([hi, 1], hi, "+" + str(hi))
            else:
                return ([-hi, 1], -hi, "-" + str(abs(hi)))

    coprime_list = []
    for i in range(base_num-1):
        if gcd(base_num, i+1) == 1:
            coprime_list.append(i+1)
    
    n = random.sample(coprime_list, 1)[0]
    ctr = [n, base_num]

    if big != 0:
        randoms = np.random.randint(0,high)
        ctr = sum_frac(ctr, [randoms,1])

    if minus == 0:
        return ([ctr[0], ctr[1]], ctr[0]/ctr[1], "{%d} over {%d}" % (ctr[0], ctr[1]))
    elif minus == -1:
        return ([-ctr[0], ctr[1]], -ctr[0]/ctr[1], "-{%d} over {%d}" % (ctr[0], ctr[1]))
    
    rf = np.random.randint(0,2)
    if rf == 0:
        return ([ctr[0], ctr[1]], ctr[0]/ctr[1], " {%d} over {%d} " % (ctr[0], ctr[1]))
    else:
        return ([-ctr[0], ctr[1]], -ctr[0]/ctr[1], " -{%d} over {%d} " % (abs(ctr[0]), ctr[1]))


def print_frac3(f1, f2):
    if f2 < 0:
        f1 = -f1
        f2 = abs(f2)
    if f1 == 0:
        return str(0)

    if f2 == 1:
        if f1 < 0:
            return "( -%d )" % (abs(f1)) 
        else:
            return " +%d " % (abs(f1)) 
    if f1 < 0:
        return " (-{%d} over {%d} )" % (abs(f1), f2)
    else:
        return " {%d} over {%d} " % (f1, f2)


def print_ans(f1, f2):
    if f1 == 0:
        return str(0)
    if f2 < 0:
        f1 = -f1
        f2 = abs(f2)
    ctr = ctr_frac2(f1, f2)
    if ctr[1] == 1:
        return str(ctr[0])
    if ctr[0] < 0:
        return "-{%d} over {%d}" % (abs(ctr[0]), ctr[1])
    else:
        return "{%d} over {%d}" % (ctr[0], ctr[1])


def print_parent_int(n):
    if n == 0:
        return " 0 "
    elif n < 0:
        return " -%d " % abs(n)
    else:
        return " +%d " % n


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
            ex_list.append(ans + (i-ans_index)*interval)
    else:
        ans_index = 4 - ans_index
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (ans_index-i)*interval)
    return ex_list


def make_example_by_interval(ans, interval):
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
            ex_list.append(ans + (i-ans_index)*interval)
    else:
        ans_index = 4 - ans_index
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (ans_index-i)*interval)
    return ex_list


def make_example_minus(ans, interval):
    if interval == 0:
        interval = np.random.randint(1, 3)

    ans_index = np.random.randint(0, 5)
    reverse = int(np.random.rand() + 0.25)
    
    ex_list = []
    if reverse == 0:
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (i-ans_index)*interval)
    else:
        ans_index = 4 - ans_index
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (ans_index-i)*interval)
    return ex_list


def make_example_by_interval_fraction_ver(ans, interval, high):
    reverse = 0
    if high-ans < interval:
        ans_index = 4
        reverse = int(np.random.rand() + 0.5)
    elif ans <= interval:
        ans_index = 0
        reverse = int(np.random.rand() + 0.5)
    else:
        h_limit = (ans // interval) if ans // interval < 5 else 5
        l_limit = 4 - ((high-ans) // interval) if 4 - ((high-ans) // interval) >= 0 else 0
        ans_index = np.random.randint(l_limit, h_limit)
        reverse = int(np.random.rand() + 0.25)   

    ex_list = []
    if reverse == 0:
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (i-ans_index)*interval)
    else:
        ans_index = 4 - ans_index
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (ans_index-i)*interval)
    return ex_list

#두개의 분수 더하는 함수
def sumOver(a1,a2, b1,b2):
    m=1
    s=2
    return m,s

#두개의 분수 곱하는 함수
def mulOver(a1,a2,b1,b2):
    r1=a1*a2
    r2=b1*b2
    g=gcd(r1,r2)
    re1=r1/g
    re2=r2/g
    return re1,re2

#분수 만들기
def makeOver(d1,d2):
    a1=np.random.randint(1,d1)
    a2=np.random.randint(2,d2)
    g=gcd(a1,a2)
    r1=a1/g
    r2=a2/g
    if r1==r2:
        r2*=2
    if r2==1:
        temp=r2
        r2=r1
        r1=temp
    return int(r1),int(r2)

#특정 분수에서 가장 가까운 정수
def getNearInt(a1,a2):
    r=a1/a2
    return round(r)

#comp
comp=    ["+", "-"]

#get random comp
def getRanComp():
    r=np.random.randint(0,1)
    return comp[r]

#define is int or not
def in_int(x):
    if x==int(x):
        return True
    else: return False

#수식
def tn(s):
    head="$$수식$$"
    tail="$$/수식$$"
    return head+s+tail

#make random choice and get answer
def makeRandom(choice_list, answer_idx):
    temp=choice_list
    np.random.shuffle(choice_list)
    for i in range(0,len(temp)):
        #print(temp[answer_idx], '|', choice_list[i])
        if temp[answer_idx]==choice_list[i]:
            aidx=i
            break
    return temp,choice_list,aidx


# ans = a/b, interval = 1/fintv
def make_fraction_example(a,b,fintv):
    lcm_ = lcm(b, fintv)
    mult = [int(lcm_/b), int(lcm_/fintv)]
    b = b * mult[0]
    a = a * mult[0]
    fintv = fintv * mult[1]

    ans_list = []
    example_list = make_example_by_interval_fraction_ver(a,mult[1],fintv)
    ans_list.append(example_list[0])
    for i in range(5):
        if gcd(example_list[i+1], fintv) != 1:
            ctr = ctr_frac(example_list[i+1], fintv)
            if ctr[1] == 1:
                ans_list.append("1")
            else:
                ans_list.append("{%d} over {%d}" % (ctr[0], ctr[1]))
        else:
            ans_list.append("{%d} over {%d}" % (example_list[i+1], fintv))
    
    return ans_list


def make_shuffle_example(answer_list, f_ans_ind):    
    example_list = copy.deepcopy(answer_list)
    ind = [0,1,2,3,4]
    random.shuffle(ind)

    ans_ind = ind[f_ans_ind]   
    for i in range(len(ind)):
        example_list[ind[i]] = answer_list[i]

    return [ans_ind] + example_list


def make_fraction_example2(f1, f2):
    if f1 == 0:
        base_list = [0, 1, -1, 2, -2, print_ans(1, 2), print_ans(-1, 2), print_ans(1, 3), print_ans(-1, 3)]
    else:
        base_list = [print_ans(-f1, f2), print_ans(f1, f2*2), print_ans(f1, f2*4), print_ans(f1*2, f2), print_ans(f1*4, f2), print_ans(-f1, f2*2), print_ans(-f1, f2*4), print_ans(-f1*2, f2), print_ans(-f1*4, f2)]
    ans_list = random.sample(base_list,5)
    ans_list[0] = print_ans(f1, f2)
    return make_shuffle_example(ans_list, 0)

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
        #이(라고)
        if bool_jo(num):
            return "이"
        return ""
    elif bool_jo(num):
        # 을를
        return "을"
    return "를"

# 1-1-2-01
def intandrational112_Stem_001():
    stem = "다음 중 $$수식$$+, -$$/수식$$부호를 사용하여 나타낸 것으로 옳은 것은?\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "① {c1}\n" \
              "② {c2}\n" \
              "③ {c3}\n" \
              "④ {c4}\n" \
              "⑤ {c5}\n\n"


    x1 = np.random.randint(10, 60)
    x2 = np.random.randint(10, 100)
    x3 = np.random.randint(1, 25)
    x4 = np.random.randint(100, 1000)
    x5 = np.random.randint(1000, 10000)

    x11 = ["증가", "감소"]
    x13 = ["영상", "영하"]
    x14 = ["해발", "해저"]
    x15 = ["이익", "손해"]

    #to differnetiate numbers choice
    x_choices=[[],[],[],[],[]]
    for i in range(0,5):
        num=np.random.randint(0,1)
        x_choices[i].append(num)
        x_choices[i].append(num^1)

    correctAns = np.random.randint(0, 4)  # check correct answer
    cidx=correctAns
    x_choices[cidx][1]=x_choices[cidx][0]

    y1 = f"$$수식$${x1}``rm {{kg}}$$/수식$$ {x11[x_choices[0][0]]} : $$수식$${comp[x_choices[0][1]]}{x1}``rm {{kg}}$$/수식$$"
    y2 = f"$$수식$${x2}$$/수식$$점 {x11[x_choices[1][0]]} : $$수식$$ {comp[x_choices[1][1]]}{x2}$$/수식$$점"
    y3 = f"{x13[x_choices[2][0]]} $$수식$${x3}``^{{\\circ}}C$$/수식$$ : $$수식$$ {comp[x_choices[2][1]]}{x3}``^{{\\circ}}C$$/수식$$"
    y4= f"{x14[x_choices[3][0]]} $$수식$$ {x4}``rm m$$/수식$$ : $$수식$${comp[x_choices[3][1]]}{x4}``rm m$$/수식$$"
    y5= f"$$수식$${x5}$$/수식$$원 {x15[x_choices[4][0]]} : $$수식$${comp[x_choices[4][1]]}{x5}$$/수식$$원"

    toshuffle = [y1, y2, y3,y4,y5]
    temp=[y1,y2,y3,y4,y5]
    np.random.shuffle(toshuffle)
    choices=[x1,x2,x3, x4, x5] = toshuffle
    comments=toshuffle

    table1=str.maketrans('+','-')
    table2=str.maketrans('-','+')

    for i in range(0,5):
        if choices[i]==temp[cidx]:
            aidx=i
        else:
            if comments[i].find('-')==-1:
                comments[i]=comments[i].translate(table1)
                #print(i,'+')
            elif comments[i].find('+')==-1:
                comments[i]=comments[i].translate(table2)
                #print(i,'-')
    [c1,c2,c3,c4,c5]=comments

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=answer_dict[aidx])
    comment = comment.format(c1=c1, c2=c2,c3=c3,c4=c4,c5=c5, a1=answer_dict[aidx])

    return stem, answer, comment

# 1-1-2-03
def intandrational112_Stem_002():
    stem = " 다음 중 세 수가 모두 정수가 아닌 유리수인 것은?\n" \
           "① {x1}\n"\
           "② {x2}\n"\
           "③ {x3}\n"\
           "④ {x4}\n"\
           "⑤ {x5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
              "① {c1}\n"\
              "② {c2}\n"\
              "③ {c3}\n"\
              "④ {c4}\n"\
              "⑤ {c5}\n\n"


    x1="$$수식$${x11} , ` {x12}, ` {x13}$$/수식$$"  
    x2="$$수식$${x21} , ` {x221} over {x222} , ` {x23}$$/수식$$"    
    x3="$$수식$${x32}, {x311} over {x312}, ` {x33}$$/수식$$"    
    x4="$$수식$${x411} over {x412}, ` {x42} , ` {x431} over {x432}$$/수식$$"   
    x5="$$수식$${x51},` {x521} over {x522}, ` {x53}$$/수식$$" 
    x_list=[x1,x2,x3,x4,x5]
    x_temp=x_list

    x11 = np.random.randint(-5, 5)
    x12= 0
    x13= -x11

    x21 = np.random.randint(1, 5)   
    x221,x222=makeOver(15,10)
    x23= np.random.randint(1,10)

    x31 = np.random.randint(1, 5)    
    x311,x312=makeOver(10,10)
    x32=-np.random.randint(1,8)
    x33=np.random.randint(2,9)

    x411,x412=makeOver(10,10)    
    x421,x422=makeOver(15,15)
    x42=round(x421/x422,1) 
    x432=np.random.randint(3,9)
    n=np.random.randint(0,4)
    lst=[2,3,4,5,6]
    x431=lst[n]*x432
    x43=lst[n]

    x511,x512=makeOver(10,10)
    x51=-round(x511/x512,1)
    x521,x522=makeOver(10,10)
    x531,x532=makeOver(11,11)
    x53=round(x531/x532,1)

    print(x531, x532)

    # to differnetiate numbers choice
    x_choices = [[], [], [], [], []]

    #correctAns = np.random.randint(0, 4)  # check correct answer

    y1 = f"$$수식$${x11} , {x12}, {x13}$$/수식$$"
    y2 = f"$$수식$${x21},{x23}$$/수식$$"
    y3 = f"$$수식$${x32}, {x33}$$/수식$$"
    y4 = f"$$수식$${x431} over {x432}$$/수식$$"
    y5 = f""

    x_list = np.random.permutation((x_list))
    x_index = []
    for i in x_list:
        x_index.append(x_temp.index(i))

    

    [x1,x2,x3,x4,x5]=x_list


    toshuffle = [y1, y2, y3, y4, y5]
    temp = []

    for i in x_index:
        temp.append(toshuffle[i])

    #np.random.shuffle(toshuffle)
    #[x1,x2,x3,x4,x5]=toshuffle    

  
    for i in range(0,5):
        #if temp[4]==toshuffle[i]:
        if temp[i]==toshuffle[4]:
            aidx=i
    

    x_temp = makeRandom(x_list,4)
    comments = temp

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    for i in range(0,5):
        if i!=aidx:
            comments[i]+="는 정수"
        elif i==aidx:
            comments[i]+="세 개의 수 모두 정수가 아닌 유리수"

    [c1, c2, c3, c4, c5] = comments


    stem = stem.format(x11=x11,x12=x12,x13=x13, x21=x21,x221=x221,x222=x222,x23=x23, x31=x31,x311=x311,x312=x312,x32=x32,x33=x33,x411=x411,x412=x412,x42=x42,x431=x431,x432=x432, x51=x51,x521=x521,x522=x522,x53=x53)
    answer = answer.format(a1=answer_dict[aidx])
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)

    return stem, answer, comment


# 1-1-2-04
def intandrational112_Stem_003():
    stem = "다음 수 중에서 양의 정수의 개수를 $$수식$$a$$/수식$$, 음의 정수의 개수를 $$수식$$b$$/수식$$라 할 때, "\
        "$$수식$${equation}$$/수식$$의 값은?\n"\
        "$$표$${number_lists}$$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "양의 정수는 {plus_integers}의 $$수식$${num1}$$/수식$$개이므로 $$수식$$a`=`{num1}$$/수식$$\n"\
        "음의 정수는 {minus_integers}의 $$수식$${num2}$$/수식$$개이므로 $$수식$$b`=`{num2}$$/수식$$\n"\
        "$$수식$$THEREFORE```{equation}`=`{ans}`$$/수식$$\n\n"

    tot = 10
    nums = random.sample(list(range(1,6)), 2)
    nums.sort()
    num1 = nums[1]
    num2 = nums[0]
    num3 = tot - num1 - num2

    eq_ind = np.random.randint(0,3)
    equation = ["a`-`b", "a`+`b", "a`times`b"][eq_ind]
    ans = [num1-num2, num1+num2, num1*num2][eq_ind]

    integers = list(range(1,10))
    np.random.shuffle(integers)
    
    fracters = ["$$수식$$0$$/수식$$"]
    for i in range(10):
        frac = frac_generator(1, 10, 5)
        fracters.append("$$수식$${%d} over {%d}$$/수식$$" % (frac[0], frac[1]))
    np.random.shuffle(fracters)
    
    plus_integers = ""
    minus_integers = ""
    numbers = []

    for i in range(num1 + num2):
        random_factor = np.random.randint(0,5)
        if i < num1:
            if random_factor < 1:
                base = np.random.randint(2,6)
                str_plus = "$$수식$$" + "{%d} over {%d}" % (integers[i]*base, base) + "$$/수식$$"
                plus_integers = plus_integers + str_plus
            elif random_factor < 2:
                str_plus = "$$수식$$+" + str(integers[i]) + "$$/수식$$"
                plus_integers = plus_integers + str_plus
            else:
                str_plus = "$$수식$$" + str(integers[i]) + "$$/수식$$"
                plus_integers = plus_integers + str_plus
            if i != num1-1:
                plus_integers = plus_integers + ", "
            numbers.append(str_plus)
        else:
            if random_factor < 2:
                base = np.random.randint(2,6)
                str_minus = "$$수식$$-" + "{%d} over {%d}" % (integers[i]*base, base) + "$$/수식$$"
                minus_integers = minus_integers + str_minus
            else:
                str_minus = "$$수식$$-" + str(integers[i]) + "$$/수식$$"
                minus_integers = minus_integers + str_minus
            if i != num1+num2-1:
                minus_integers = minus_integers + ", "
            numbers.append(str_minus)
    
    for i in range(num3):
        numbers.append(fracters[i])
    
    np.random.shuffle(numbers)
    number_lists = ""
    for i in range(len(numbers)):
        if number_lists == "":
            number_lists = number_lists + numbers[i]
        else:
            number_lists = number_lists + ", " + numbers[i]

    example_list = make_example_by_interval(ans, 1)

    stem = stem.format(equation=equation, number_lists=number_lists, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num2=num2, plus_integers=plus_integers, minus_integers=minus_integers, equation=equation, ans=ans)

    return stem, answer, comment

# 1-1-2-05
def intandrational112_Stem_004():
    stem = "다음 옳지 않은 것은?\n① {x1}\n② {x2}\n③ {x3}\n④ {x4}\n⑤ {x5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{c1}\n"


    y1="$$수식$$0$$/수식$$은 양수도 음수도 아니다."
    y2="서로 다른 두 유리수 사이에는 무수히 많은 유리수가 존재한다."
    y3="수직선 위에서 음수를 나타내는 점은 항상 원점보다 왼쪽에 있다."
    y4="정수는 자연수를 포함하고, $$수식$$0$$/수식$$을 제외한 정수만 유리수에 포함된다."
    y5 = "유리수란 분자가 정수이고 분모는 $$수식$$0$$/수식$$이 아닌 정수인 분수로 나타낼 수 있는 수이다."

    toshuffle=[y1,y2,y3,y4,y5]
    temp=[y1,y2,y3,y4,y5]
    np.random.shuffle(toshuffle)
    [x1,x2,x3,x4,x5]=toshuffle

    for i in range(0,5):
        if temp[3]==toshuffle[i]:
            aidx=i

    c1=answer_dict[aidx]+" 정수는 모두 유리수에 포함된다.\n"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4, x5=x5)
    answer = answer.format(a1=answer_dict[aidx])
    comment = comment.format(c1=c1, a1=answer_dict[aidx])

    return stem, answer, comment

# 1-1-2-07
def intandrational112_Stem_005():
    stem = "다음 보기에서 정수와 유리수에 대한 설명으로 옳은 것만을 있는 대로 고른 것은?\n $$표$$ ㉠ {x1}\n㉡ {x2}\n㉢ {x3}\n㉣ {x4} $$/표$$ \n① {xc1}     ② {xc2}     ③ {xc3}  \n④  {xc4}     ⑤ {xc5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
              "{c1}\n\n"

    y1 = " $$수식$$0$$/수식$$은 유리수이다."
    y2= " 모든 정수는 유리수이다."
    y3= " 양의 정수는 자연수와 같다."
    y4= " 음의 정수가 아닌 정수는 양의 정수이다."

    choice_list= ["㉠", "㉡", "㉢", "㉣"]
    temp_choice_list = ["㉠", "㉡", "㉢", "㉣"]
    np.random.shuffle(choice_list)

    toshuffle=[y1,y2,y3,y4]
    temp=[y1,y2,y3,y4]

    np.random.shuffle(toshuffle)

    #shuffle된 리스트
    [x1,x2,x3,x4]=toshuffle

    #shuffle된 리스트에서 틀린 답 idx
    for i in range(0,4):
        if temp[3]==toshuffle[i]:
            isnAnsweridx=i

    isAnswer=""
    isntAnswer=""

    #make right string answer
    for i in range(0,4):
        if i!=isnAnsweridx:
            isAnswer+=temp_choice_list[i]

    #make unrihgt string answer
    isntAnswer+=temp_choice_list[isnAnsweridx]
    for i in range(0,4):
        if len(isntAnswer)==3:
            break
        if i!=isnAnsweridx:
            isntAnswer+=temp_choice_list[i]
    isntAnswer=sorted(isntAnswer)


    xc1= "㉠, ㉡"
    xc2= "㉠, ㉢"
    xc3= "㉢, ㉣"

    isAnswer2=""
    isntAnswer2=""
    for i in range(0,len(isAnswer)):
        if i==len(isAnswer)-1:
            isAnswer2+=isAnswer[i]+" "
        else: 
            isAnswer2+=isAnswer[i]+", "
        
    for i in range(0,len(isntAnswer)):
        if i==len(isntAnswer)-1:
            isntAnswer2+=isntAnswer[i]+" "
        else: 
            isntAnswer2+=isntAnswer[i]+", "

    #answer 분배
    randomAnswer=[isAnswer2,isntAnswer2]
    np.random.shuffle(randomAnswer)
    randomAnswer=sorted(randomAnswer)

    xc4= randomAnswer[0]
    xc5= randomAnswer[1]

    #answer
    if xc4==isAnswer2:
        aidx=3
    else:
        aidx=4

    c1=answer_dict[aidx]+" 음의 정수가 아닌 정수는 0 또는 양의 정수이다. 따라서 옳은 것은 " +isAnswer2+"이다.\n"

    stem = stem.format(x1=x1, x2=x2, x3=x3, x4=x4 , xc1=xc1, xc2=xc2 , xc3=xc3, xc4=xc4, xc5=xc5)
    answer = answer.format(a1=answer_dict[aidx])
    comment = comment.format(c1=c1, a1=answer_dict[aidx])

    return stem, answer, comment

# 1-1-2-08
def intandrational112_Stem_006():
    stem = "유리수 $$수식$$x$$/수식$$에 대하여\n$$수식$$`&lt;`x`&gt;={sss}$$/수식$$\n이라 할 때, \n$$수식$$``&lt;`{x11} over {x12} &gt;`+`&lt;`{x2}>`+`&lt;{x3}>`+`&lt;{x4}>`+`&lt;{x5}>$$/수식$$ \n의 값은\n① $$수식$${xc1}$$/수식$$     ② $$수식$${xc2}$$/수식$$     ③ $$수식$${xc3}$$/수식$$\n④ $$수식$${xc4}$$/수식$$     ⑤ $$수식$${xc5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
             "$$수식$${x11} over {x12}, ``{x4}$$/수식$$ 는 정수가 아닌 유리수이므로\n\n"\
             "$$수식$$&lt; {x11}over {x12} > ` = 1 , ` &lt; {x4} > ` = 1$$/수식$$\n\n$$수식$${x2} , `` {x3} , ``` {x5}$$/수식$$ 는 정수이므로\n\n$$수식$$&lt; ` {x2} > ` = 0 , ` &lt; {x3} > ` = 0 ,` &lt; {x5} > ` = 0 $$/수식$$\n\n $$수식$$THEREFORE ` &lt; ` {x11} over {x12} ` > ` + ` &lt; ` {x2} > ` + ` &lt; ` {x3} > ` + ` &lt; ` {x4} > ` + ` &lt; ` {x5} > ` = ` 2$$/수식$$\n\n"

    y1= " 0은 유리수이다."
    y2= " 모든 정수는 유리수이다."
    y3= " 양의 정수는 자연수와 같다."
    y4= " 음의 정수가 아닌 정수는 양의 정수이다."

    choice_list= ["㈀", "㈁", "㈂", "㈃"]
    temp_choice_list=["㈀", "㈁", "㈂", "㈃"]
    np.random.shuffle(choice_list)

    toshuffle=[y1,y2,y3,y4]

    x11=1
    x12=np.random.randint(2,8)
    x2=-np.random.randint(1,6)
    x3=0
    x4=np.random.randint(1,2)/np.random.randint(3,10)
    x4=round(x4,1)
    x5=np.random.randint(1,6)

    xc1=1
    xc2=2
    xc3=3
    xc4=4
    xc5=5

    aidx=1
    sss = "{cases{0``(x는``정수)#1``(정수가``아닌``유리수)}}"
    stem = stem.format(x11=x11, x12=x12, x2=x2, x3=x3, x4=x4, x5=x5, xc1=xc1, xc2=xc2, xc3=xc3, xc4=xc4, xc5=xc5, sss=sss)
    answer = answer.format(a1=answer_dict[aidx])
    comment = comment.format(a1=answer_dict[aidx],x11=x11,x12=x12,x2=x2,x3=x3,x4=x4,x5=x5,aidx=aidx)

    return stem, answer, comment

# 1-1-2-13
def intandrational112_Stem_007():
    stem = "수직선 위에서 $$수식$${x11} over {x12} $$/수식$$를 나타내는 점을 $$수식$$A$$/수식$$, $$수식$${x21} over {x12}$$/수식$$을 " \
           "나타내는 점을 $$수식$$B$$/수식$$라 하고 두 점 $$수식$$A$$/수식$$ 와 $$수식$$B$$/수식$$ 의 한가운데에 있는 점을 " \
           "$$수식$$M$$/수식$$ 이라 하자. 이때 점 $$수식$$M$$/수식$$ 에 대응하는 수는?\n" \
           "① $$수식$${xc1}$$/수식$$     ② $$수식$${xc2}$$/수식$$     ③ $$수식$${xc3}$$/수식$$\n" \
           "④ $$수식$${xc4}$$/수식$$     ⑤ $$수식$${xc5}$$/수식$$\n"

    answer = "(답): {a1}\n"
    comment = "(해설)\n" \
             "점 $$수식$$A$$/수식$$ 원점 사이의 거리는 $$수식$${x22} over {x12}$$/수식$$ 이고 점 $$수식$$B$$/수식$$ 와 원\n" \
              "점 사이의 거리는 $$수식$${x21} over {x12}$$/수식$$이므로 두 점 $$수식$$A$$/수식$$ , $$수식$$B$$/수식$$ 사이의\n" \
              "거리는 $$수식$${x22} over {x12} + {x21} over {x12} = {x51} over {x12}$$/수식$$\n" \
              "이때 $$수식$$ {x51} over {x12} TIMES 1 over 2 = {x63} over {x64}$$/수식$$   이므로 $$수식$$ $$/수식$$ 와 $$수식$$ $$/수식$$ 에 대응하는\n" \
              "두 점 $$수식$$A$$/수식$$, $$수식$$B$$/수식$$ 의 한가운데에 있는 점 $$수식$$M$$/수식$$에 대응하는 수는\n" \
              "$$수식$$ {x21} over {x12} - {x63} over {x64} = {x43} over {x44}$$/수식$$이다.\n\n"


    choice_list= ["㈀", "㈁", "㈂", "㈃"]
    temp_choice_list=["㈀", "㈁", "㈂", "㈃"]
    np.random.shuffle(choice_list)

    while True:
        x11=-np.random.randint(1,9)
        x12=np.random.randint(2,10)
        x21=np.random.randint(1,9)

        if abs(x11) != abs(x12) and abs(x21) != abs(x12) and abs(x11) < abs(x21):
            if gcd(abs(x11),abs(x12)) == 1 and gcd(abs(x21),abs(x12)) == 1:
                break
    
    x22=-x11
    x51=x22+x21

    x61=np.random.randint(2,10)
    x62=x12*2
    #기약분수로 만들어 주기 위한 변수 선언 
    x63=int(x51/gcd(x51,x62))
    x64=int(x62/gcd(x51,x62))

    #통분 
    x31=lcm(x12,x64)
    x32=x31/x12 * x21
    x41=x31/x64 * x63
    x42=abs(x32-x41)

    #최종 결과를 기약분수로 
    x43=int(x42/gcd(x42,x31))
    x44=int(x31/gcd(x42,x31))

    while True:
        answer_list = random.sample([1,2,3,4,5,6,7,8,9], 5)
        if x43 in answer_list and x44 not in answer_list:
            break

    xc1="{a1} over {x44}".format(a1=answer_list[0], x44=x44)
    xc2="{a2} over {x44}".format(a2=answer_list[1], x44=x44)
    xc3="{a3} over {x44}".format(a3=answer_list[2], x44=x44)
    xc4="{a4} over {x44}".format(a4=answer_list[3], x44=x44)
    xc5="{a5} over {x44}".format(a5=answer_list[4], x44=x44)

    aidx=answer_list.index(x43)

    stem = stem.format(x11=x11, x12=x12, x21=x21,x22=x22, x31=x31,x32=x32, x41=x41,x42=x42, x51=x51, x43=x43,x44=x44,x61=x61,x62=x62,x63=x63, x64=x64, xc1=xc1, xc2=xc2, xc3=xc3, xc4=xc4, xc5=xc5)
    answer = answer.format(a1=answer_dict[aidx])
    comment = comment.format(a1=answer_dict[aidx],x11=x11,x12=x12,x21=x21,x22=x22,x31=x31,x32=x32,x41=x41,x42=x42,x51=x51,x43=x43,x44=x44,x61=x61,x62=x62,x63=x63, x64=x64)

    return stem, answer, comment

# 1-1-2-14
def intandrational112_Stem_008():
    stem = "수직선 위에서 $$수식$${frac1}$$/수식$$에 가장 가까운 정수를 $$수식$$a$$/수식$$, "\
        "$$수식$${frac2}$$/수식$$에 가장 가까운 정수를 $$수식$$b$$/수식$$라 할 때, "\
        "$$수식$${equation}$$/수식$$의 값은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${frac1}$$/수식$$에 가장 가까운 정수는 $$수식$${num1}$$/수식$$이므로 $$수식$$a`=`{num1}$$/수식$$\n"\
        "$$수식$${frac2}$$/수식$$에 가장 가까운 정수는 $$수식$${num2}$$/수식$$이므로 $$수식$$b`=`{num2}$$/수식$$\n"\
        "$$수식$$THEREFORE```{equation}`=`{ans}`$$/수식$$\n\n"

    nums = random.sample(list(range(1,6)), 2)
    nums.sort()
    num1 = nums[1]
    num2 = -nums[0]

    fr1 = frac_generator(0, 10, 10)
    ctr = ctr_frac2(fr1[0], fr1[1]*2)
    pm = np.random.randint(0,2)
    if pm == 0:
        sum1 = sum_frac([num1,1],ctr)  
    else:
        sum1 = sum_frac([num1,1],[-ctr[0],ctr[1]])
    if sum1[0] < 0: 
        frac1 = "-{%d} over {%d}" % (abs(sum1[0]), sum1[1])
    else:
        frac1 = "{%d} over {%d}" % (sum1[0], sum1[1])
        
    
    fr2 = frac_generator(0, 10, 10)
    ctr = ctr_frac2(fr2[0], fr2[1]*2)
    pm = np.random.randint(0,2)
    if pm == 0:
        sum2 = sum_frac([num2,1],ctr)
    else:
        sum2 = sum_frac([num2,1],[-ctr[0],ctr[1]])
    if sum2[0] < 0: 
        frac2 = "-{%d} over {%d}" % (abs(sum2[0]), sum2[1])
    else:
        frac2 = "{%d} over {%d}" % (sum2[0], sum2[1])

    eq_ind = np.random.randint(0,3)
    equation = ["a`-`b", "a`+`b", "a`times`b"][eq_ind]
    ans = [num1-num2, num1+num2, num1*num2][eq_ind]

    example_list = make_example_by_interval(ans, 1)

    stem = stem.format(equation=equation, frac1=frac1, frac2=frac2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num2=num2, frac1=frac1, frac2=frac2, equation=equation, ans=ans)

    return stem, answer, comment


# 1-1-2-16
def intandrational112_Stem_009():
    stem = "$$수식$${num1}$$/수식$$의 절댓값을 $$수식$$a$$/수식$$, $$수식$${num2}$$/수식$$의 절댓값을 $$수식$$b$$/수식$$라 할 때, "\
        "$$수식$${equation}$$/수식$$의 값은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${num1}$$/수식$$의 절댓값은 $$수식$${a}$$/수식$$이므로 $$수식$$a`=`{a}$$/수식$$\n"\
        "$$수식$${num2}$$/수식$$의 절댓값은 $$수식$${b}$$/수식$$이므로 $$수식$$b`=`{b}$$/수식$$\n"\
        "$$수식$$THEREFORE```{equation}`=`{ans}`$$/수식$$\n\n"

    integers = list(range(1,10))
    np.random.shuffle(integers)
    
    cond = np.random.randint(0,2)
    if cond == 0:
        num1 = -integers[0]
        num2 = integers[1]
    else:
        num1 = integers[0]
        num2 = -integers[1]

    a = abs(num1)
    b = abs(num2)

    eq_ind = np.random.randint(0,2)
    equation = ["a`+`b", "a`times`b"][eq_ind]
    ans = [a+b, a*b][eq_ind]

    example_list = make_example(ans)

    stem = stem.format(equation=equation, num1=num1, num2=num2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num2=num2, a=a, b=b, equation=equation, ans=ans)

    return stem, answer, comment


# 1-1-2-17
def intandrational112_Stem_010():
    stem = "$$수식$$|a|`=`{num1}$$/수식$$, $$수식$$|b|`=`{num2}$$/수식$$이고 수직선에서 $$수식$$a$$/수식$$와 $$수식$$b$$/수식$$를 "\
        "나타내는 점은 각각 $$수식$$0$$/수식$$을 나타내는 점의 {c1}과 {c2}에 있을 때, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$의 값은?\n"\
        "① {ex1}     ② {ex2}     ③ {ex3}     \n④ {ex4}    ⑤  {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "절댓값이 $$수식$${num1}$$/수식$$인 수는 $$수식$${num1}$$/수식$$, $$수식$${mnum1}$$/수식$$이고 "\
        "수직선에서 $$수식$$0$$/수식$$을 나타내는 점의 {c1}의 점은 {c1_str}를 나타내므로 $$수식$$a`=`{a}$$/수식$$\n"\
        "절댓값이 $$수식$${num2}$$/수식$$인 수는 $$수식$${num2}$$/수식$$, $$수식$${mnum2}$$/수식$$이고 "\
        "수직선에서 $$수식$$0$$/수식$$을 나타내는 점의 {c2}의 점은 {c2_str}를 나타내므로 $$수식$$b`=`{b}$$/수식$$\n\n"

    integers = list(range(1,10))
    np.random.shuffle(integers)
    num1 = integers[0]
    num2 = integers[1]
    mnum1 = -num1
    mnum2 = -num2

    
    ans_f = "$$수식$$a`=`{a}$$/수식$$, $$수식$$b`=`{b}$$/수식$$"
    example_list = []
    example_list.append(ans_f.format(a=-num1, b=-num2))
    example_list.append(ans_f.format(a=num1, b=num2))
    example_list.append(ans_f.format(a=num2, b=-num1))
    example_list.append(ans_f.format(a=-num2, b=num1))

    ans_ind = np.random.randint(0,5)

    cond = np.random.randint(0,2)
    if cond == 0:
        c1 = "오른쪽"
        c2 = "왼쪽"
        c1_str = "양수"
        c2_str = "음수"
        a = num1
        b = -num2
        example_list.append(ans_f.format(a=-num1, b=num2))
        np.random.shuffle(example_list)
        example_list[ans_ind] = ans_f.format(a=num1, b=-num2)
    else:
        c2 = "오른쪽"
        c1 = "왼쪽"
        c2_str = "양수"
        c1_str = "음수"
        a = -num1
        b = num2
        example_list.append(ans_f.format(a=num1, b=-num2))
        np.random.shuffle(example_list)
        example_list[ans_ind] = ans_f.format(a=-num1, b=num2)

    stem = stem.format(c1=c1, c2=c2, num1=num1, num2=num2, \
        ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_ind])
    comment = comment.format(num1=num1, num2=num2, mnum1=mnum1, mnum2=mnum2, c1=c1, c2=c2, c1_str=c1_str, c2_str=c2_str, a=a, b=b)

    return stem, answer, comment


# 1-1-2-21
def intandrational112_Stem_011():
    stem = "두 수 $$수식$$|x|$$/수식$$, $$수식$$|y|$$/수식$$에 대하여 $$수식$$|x|`=`|y| $$/수식$$이고, "\
        "수직선에서 $$수식$$x$$/수식$$, $$수식$$y$$/수식$$를 나타내는 두 점 사이의 거리가 $$수식$${p1}$$/수식$$이다. "\
        "이때 $$수식$${target}$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "$$수식$$|x| `=` |y|$$/수식$$이고, 두 점 사이의 거리가 $$수식$${p1}$$/수식$$이므로 "\
        "두 점은 $$수식$$0$$/수식$$을 나타내는 점으로부터 각각 $$수식$${p1}`times`{half_frac}`=`{ans1}$$/수식$$만큼 떨어진 점이다.\n"\
        "따라서 $$수식$$|{tar}|`=`{ans1}$$/수식$$이므로 $$수식$${target}`=`{ans}$$/수식$$\n\n"

    frac = frac_generator(1, 10, 5)
    p1 = "{%d} over {%d}" % (frac[0], frac[1])
    half_frac = "{1} over {2}"
    
    ctr = ctr_frac2(frac[0], frac[1]*2)
    ans1 = "{%d} over {%d}" % (ctr[0], ctr[1])

    random_factor = np.random.randint(0,2)
    if random_factor == 0:
        tar = "x"
        target = "%d`|x|" % ctr[1]
    else:
        tar = "y"
        target = "%d`|y|" % ctr[1]

    ans = ctr[0]

    stem = stem.format(p1=p1, target=target)
    answer = answer.format(ans=ans)
    comment = comment.format(p1=p1, tar=tar, target=target, ans1=ans1, half_frac=half_frac, ans=ans)

    return stem, answer, comment



# 1-1-2-22
def intandrational112_Stem_012():
    stem = "$$수식$$a`!=`b$$/수식$$일 때, 다음 조건을 모두 만족시키는 두 유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$의 값은?\n"\
        "$$표$$ (가) $$수식$$|a|`=`|b|$$/수식$$\n (나) $$수식$$a`=`b`{sign}`{f1}$$/수식$$ $$/표$$\n"\
        "① {ex1}     ② {ex2}     ③ {ex3}     \n④ {ex4}    ⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "조건 (가)에 의하여 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$는 절댓값이 같고 부호가 반대인 수이다. ($$수식$$BECAUSE```a`!=`b$$/수식$$)"\
        "이때 조건 (나)에서 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$를 나타내는 두 점 사이의 거리가 $$수식$${f1}$$/수식$$이므로 "\
        "두 점은 $$수식$$0$$/수식$$을 나타내는 점으로부터 각각 $$수식$${f2}$$/수식$$만큼 떨어져 있고 $$수식$$a$$/수식$$는 {a_sign}, "\
        "$$수식$$b$$/수식$$는 {b_sign}이므로\n $$수식$$a`=`{a}$$/수식$$, $$수식$$b`=`{b}$$/수식$$\n\n"

    frac = frac_generator(1, 10, 5)
    f1 = "{%d} over {%d}" % (frac[0], frac[1])

    ctr = ctr_frac2(frac[0], frac[1]*2)
    f2 = "{%d} over {%d}" % (ctr[0], ctr[1])

    ctr_ = ctr_frac2(frac[0]*2, frac[1])
    f_ = "{%d} over {%d}" % (ctr_[0], ctr_[1])

    
    ans_f = "$$수식$$a`=`{a}$$/수식$$, $$수식$$b`=`{b}$$/수식$$"
    example_list = []
    example_list.append(ans_f.format(a=f1, b="-"+f1))
    example_list.append(ans_f.format(a="-"+f1, b=f1))
    example_list.append(ans_f.format(a=f_, b="-"+f_))
    example_list.append(ans_f.format(a="-"+f_, b=f_))

    ans_ind = np.random.randint(0,5)

    cond = np.random.randint(0,2)
    if cond == 0:
        sign = "+"
        a_sign = "양수"
        b_sign = "음수"
        a = f2
        b = "-"+f2
        example_list.append(ans_f.format(a="-"+f2, b=f2))
        np.random.shuffle(example_list)
        example_list[ans_ind] = ans_f.format(a=f2, b="-"+f2)
    else:
        sign = "-"
        b_sign = "양수"
        a_sign = "음수"
        a = "-"+f2
        b = f2
        example_list.append(ans_f.format(a=f2, b="-"+f2))
        np.random.shuffle(example_list)
        example_list[ans_ind] = ans_f.format(a="-"+f2, b=f2)

    stem = stem.format(sign=sign, f1=f1, \
        ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_ind])
    comment = comment.format(f1=f1, f2=f2, a_sign=a_sign, b_sign=b_sign, a=a, b=b)

    return stem, answer, comment


# 1-1-2-23
def intandrational112_Stem_013():
    stem = "다음 수를 수직선 위에 점으로 나타낼 때, $$수식$$0$$/수식$$을 나타내는 점에서 {cond} 것은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$0$$/수식$$을 나타내는 점에서 {cond} 점이 나타내는 수는 절댓값이 {cond_str} 수이다.\n"\
        "주어진 절댓값의 대소를 비교하면\n"\
        "$$수식$$| {n1} | &lt; | {n2} | &lt; | {n3} | &lt; | {n4} | &lt; | {n5} |$$/수식$$\n"\
        "따라서 구하는 수는 $$수식$${ans}$$/수식$$이다.\n\n"

    cond_ind = np.random.randint(0,4)
    cond = ["가장 가까운", "가장 먼", "두 번째로 가까운", "두 번째로 먼"][cond_ind]
    cond_str = ["가장 작은", "가장 큰", "두 번째로 작은", "두 번째로 큰"][cond_ind]

    nums = random.sample(list(range(1,10)), 3)
    
    fr = frac_generator(1, 6, 5)
    f1 = fr[0]/fr[1]
    f1_str = "{%d} over {%d}" % (fr[0], fr[1])
    nums.append(f1)

    fr = frac_generator(1, 6, 5)
    f2 = round(fr[0]/fr[1], 1)
    nums.append(f2)

    nums.sort()
    nums_str = []
    for i in range(len(nums)):
        f = np.random.randint(0,2)
        if f == 0:
            if nums[i] == f1:
                nums_str.append("-"+f1_str)
            else:
                nums_str.append("-"+str(nums[i]))
        else:
            if nums[i] == f1:
                nums_str.append(f1_str)
            else:
                nums_str.append(str(nums[i]))

    n1 = nums_str[0]
    n2 = nums_str[1]
    n3 = nums_str[2]
    n4 = nums_str[3]
    n5 = nums_str[4]

    example_list = copy.deepcopy(nums_str)

    ind = list(range(0,5))
    random.shuffle(ind)

    if cond_ind == 0:
        ans_ind = ind[0]
        ans = n1
    elif cond_ind == 1:
        ans_ind = ind[4]
        ans = n5
    elif cond_ind == 2:
        ans_ind = ind[1]
        ans = n2
    elif cond_ind == 3:
        ans_ind = ind[3]
        ans = n4
    
    for i in range(len(ind)):
        example_list[ind[i]] = nums_str[i]

    stem = stem.format(cond=cond, \
        ex1=example_list[0], ex2=example_list[1], ex3=example_list[2], ex4=example_list[3], ex5=example_list[4])
    answer = answer.format(a1=answer_dict[ans_ind])
    comment = comment.format(cond=cond, cond_str=cond_str, n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, ans=ans)

    return stem, answer, comment


# 1-1-2-25
def intandrational112_Stem_014():
    stem = "절댓값이 $$수식$${frac1}$$/수식$$보다 작은 정수의 개수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "원점으로부터의 거리가 $$수식$${frac1}$$/수식$$보다 작은 정수는 {num_lists}이다.\n"\
        "따라서 구하는 정수의 개수는 $$수식$${ans}$$/수식$$이다.\n\n"
    
    fr1 = frac_generator(1, 6, 5)
    frac1 = "{%d} over {%d}" % (fr1[0], fr1[1])
    high = int(fr1[0]/fr1[1])
    low = -high
    ans = 2 * high + 1

    num_lists = ""
    for i in range(ans):
        if num_lists == "":
            num_lists = num_lists + "$$수식$$" + str(low+i) + "$$/수식$$"
        else:
            num_lists = num_lists + ", $$수식$$" + str(low+i) + "$$/수식$$"

    example_list = make_example_by_interval(ans, 1)

    stem = stem.format(frac1=frac1, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(frac1=frac1, num_lists=num_lists, ans=ans)

    return stem, answer, comment


# 1-1-2-26
def intandrational112_Stem_015():
    stem = "정수 $$수식$$n$$/수식$$에 대하여 $$수식$${frac1}$$/수식$$의 절댓값이 $$수식$${num2}$$/수식$$보다 작게 되는 $$수식$$n$$/수식$$의 값의 개수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$| {frac1} | &lt; {num2}$$/수식$$이어야 하므로 $$수식$$ -{num3} &lt; | n | &lt;{num3} $$/수식$$이다.\n"\
        "따라서 정수 $$수식$$n$$/수식$$의 값은 {num_lists}이므로 개수는 "\
        "$$수식$${ans}$$/수식$$이다.\n\n"
    
    num1 = np.random.randint(2, 8)
    num2 = np.random.randint(1,int(14/num1))
    num3 = num1 * num2
    ans = (num3-1) * 2 + 1
    low = -(num3-1)

    frac1 = "{%s} over {%d}" % ("n", num1)

    num_lists = ""
    for i in range(ans):
        if num_lists == "":
            num_lists = num_lists + "$$수식$$" + str(low+i) + "$$/수식$$"
        else:
            num_lists = num_lists + ", $$수식$$" + str(low+i) + "$$/수식$$"

    example_list = make_example(ans)

    stem = stem.format(frac1=frac1, num2=num2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(frac1=frac1, num2=num2, num3=num3, num_lists=num_lists, ans=ans)

    return stem, answer, comment


# 1-1-2-28
def intandrational112_Stem_016():
    stem = "두 정수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$| a |`+`| b |`=`{num1}$$/수식$$를 "\
        "만족시키는 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$를 $$수식$$(a,`````b )$$/수식$$로 나타낼 때, "\
        "$$수식$$(a,`````b )$$/수식$$의 개수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{cases}"\
        "위에서 구하는 $$수식$$(a,`````b )$$/수식$$의 개수는 $$수식$${ans}$$/수식$$이다.\n\n"
    
    case = "({n}) $$수식$$| a |`=`{a}$$/수식$$, $$수식$$| b |`=`{b}$$/수식$$일 때,\n" + \
        "$$수식$$(a,`````b )`=`$$/수식$${lists}\n"

    num1 = np.random.randint(1, 6)
    cnt = 1

    cases = ""
    for i in range(num1+1):
        if i == 0:
            lists = "$$수식$$(%d, %d)$$/수식$$, $$수식$$(%d, -%d)$$/수식$$" % (0, num1, 0, num1)
        elif i == num1:
            lists = "$$수식$$(%d, %d)$$/수식$$, $$수식$$(-%d, %d)$$/수식$$" % (num1, 0, num1, 0)
        else:
            lists = "$$수식$$({n1}, {n2})$$/수식$$, $$수식$$({n1}, -{n2})$$/수식$$, " + \
                "$$수식$$(-{n1}, {n2})$$/수식$$, $$수식$$(-{n1}, -{n2})$$/수식$$"
            lists = lists.format(n1=i, n2=num1-i)
        cases = cases + case.format(n=cnt, a=i, b=num1-i, lists=lists)
        cnt = cnt + 1

    if num1 == 1:
        ans = 4
    else:
        ans = (num1-1)*4 + 4

    example_list = make_example(ans)

    stem = stem.format(num1=num1, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(cases=cases, ans=ans)

    return stem, answer, comment


# 1-1-2-29
def intandrational112_Stem_017():
    stem = "두 수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여\n $$수식$$ {equation}$$/수식$$\n라 할 때, "\
        "$$수식$$rmM`({n1}`,`{n2})`{sign}`rmM`({n3}`,`{n4})$$/수식$$의 값은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$| {n1}|`=`{n1_}$$/수식$$, $$수식$$| {n2} |`=`{n2_}$$/수식$$에서 $$수식$${eq1}$$/수식$$이므로\n"\
        "$$수식$$rmM`({n1}`,`{n2})`=`{ans1}$$/수식$$\n"\
        "$$수식$$| {n3} |`=`{n3_}$$/수식$$, $$수식$$| {n4} |`=`{n4_}$$/수식$$에서 $$수식$${eq2}$$/수식$$이므로\n"\
        "$$수식$$rmM`({n3}`,`{n4})`=`{ans2}$$/수식$$\n"\
        "$$수식$$THEREFORE```rmM`({n1}`,`{n2})`{sign}`rmM`({n3}`,`{n4})`=`{ans1}`{sign}`{ans2}`=`{ans}$$/수식$$\n\n"
    
    equation = "rmM`(a`,`b)`=`{cases{``|a ` | `( | a`| GEQ | b`| `)#`` | b`| `( | a` | &lt; | b`| )}}"
    
    nums = random.sample(list(range(1,10)), 4)
    nums.sort()

    snums = []
    for i in range(4):
        rf = np.random.randint(0,2)
        if rf == 0:
            snums.append(nums[i])
        else:
            snums.append(-nums[i])

    r1 = np.random.randint(0,2) * 3
    r2 = np.random.randint(1,3)

    n1_ = nums[r1]
    n1 = snums[r1]
    n2_ = nums[3-r1]
    n2 = snums[3-r1]
    n3_ = nums[r2]
    n3 = snums[r2]
    n4_ = nums[3-r2]
    n4 = snums[3-r2]

    if n1_ > n2_:
        eq1 = "| {n1}|`&gt;`| {n2} |".format(n1=n1, n2=n2)
        ans1 = n1_
    else:
        eq1 = "| {n1} |`&lt;`| {n2}|".format(n1=n1, n2=n2)
        ans1 = n2_

    if n3_ > n4_:
        eq2 = "| {n1}|`&gt;`| {n2}|".format(n1=n3, n2=n4)
        ans2 = n3_
    else:
        eq2 = "| {n1}|`&lt;`| {n2} |".format(n1=n3, n2=n4)
        ans2 = n4_

    si_ind = np.random.randint(0,3)
    sign = ["-", "+", "times"][si_ind]
    ans = [ans1-ans2, ans1+ans2, ans1*ans2][si_ind]

    example_list = make_example(ans)

    stem = stem.format(equation=equation, n1=n1, n2=n2, n3=n3, n4=n4, sign=sign, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, n1_=n1_, n2_=n2_, n3_=n3_, n4_=n4_, \
        sign=sign, eq1=eq1, eq2=eq2, ans1=ans1, ans2=ans2, ans=ans)   

    return stem, answer, comment


# 1-1-2-30
def intandrational112_Stem_018():
    stem = "다음 중 대소 관계가 옳은 것은?\n"\
        "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{cases}\n"

    # &lt; <, &gt; >
    ineqs = ["&lt;", "&gt;"]
    right = np.random.randint(0,4)

    f1 = "$$수식$${p1}`{ineq}`{p2}$$/수식$$"
    f2 = "$$수식$$-{i1}`{ineq}`0$$/수식$$"
    f3 = "$$수식$$-{i1}`{ineq}`-{i2}$$/수식$$"
    f4 = "$$수식$$-{flt1}`{ineq}`{flt2}$$/수식$$"
    f5 = "$$수식$$| -{i1} |`{ineq}`{i1}$$/수식$$"
    
    c1 = "$$수식$${p1}`=`{p1_}$$/수식$$, $$수식$${p2}`=`{p2_}$$/수식$$이므로 $$수식$${p1}`{ineq}`{p2}$$/수식$$\n"
    c2 = "$$수식$$-{i1}`{ineq}`0$$/수식$$\n"
    c3 = "$$수식$$| -{i1} |`{ineq_}`| -{i2} |$$/수식$$이므로 $$수식$$-{i1}`{ineq}`-{i2}$$/수식$$\n"
    c4 = "음수는 항상 양수보다 작으므로 $$수식$$-{flt1}`{ineq}`{flt2}$$/수식$$\n"
    c5 = "$$수식$$ | -{i1} |`=`{i1}$$/수식$$\n"

    fr1 = frac_generator(1, 6, 4)
    p1 = "{%d} over {%d}" % (fr1[0], fr1[1])
    fr2 = frac_generator(1, 6, 5)
    while fr1[1] == fr2[1]:
        fr2 = frac_generator(1, 6, 5)
    p2 = "{%d} over {%d}" % (fr2[0], fr2[1])

    lcm_ = lcm(fr1[1], fr2[1])
    mult = [int(lcm_/fr1[1]), int(lcm_/fr2[1])]
    p1_ = "{%d} over {%d}" % (fr1[0]*mult[0], lcm_)
    p2_ = "{%d} over {%d}" % (fr2[0]*mult[1], lcm_)

    if fr1[0]*mult[0] > fr2[0]*mult[1]:
        ineq_id = 1
    else:
        ineq_id = 0

    if right == 0:
        f1 = f1.format(p1=p1, ineq=ineqs[ineq_id], p2=p2)
    else:
        f1 = f1.format(p1=p1, ineq=ineqs[1-ineq_id], p2=p2)

    c1 = c1.format(p1=p1, p1_=p1_, p2=p2, p2_=p2_, ineq=ineqs[ineq_id])

    ints = random.sample(list(range(1,10)), 3)

    if right == 1:
        f2 = f2.format(i1=ints[0], ineq=ineqs[0])
    else:
        f2 = f2.format(i1=ints[0], ineq=ineqs[1])
    
    c2 = c2.format(i1=ints[0], ineq=ineqs[0])

    if ints[1] > ints[2]:
        ineq_id = 0
    else:
        ineq_id = 1
    
    if right == 2:
        f3 = f3.format(i1=ints[1], i2=ints[2], ineq=ineqs[ineq_id])
    else:
        f3 = f3.format(i1=ints[1], i2=ints[2], ineq=ineqs[1-ineq_id])

    c3 = c3.format(i1=ints[1], i2=ints[2], ineq=ineqs[ineq_id], ineq_=ineqs[1-ineq_id])      

    fr3 = frac_generator(1, 10, 3)
    fr4 = frac_generator(1, 10, 5)

    flt1 = round(fr3[0]/fr3[1], 1)
    flt2 = round(fr4[0]/fr4[1], 1)

    if right == 3:
        f4 = f4.format(flt1=flt1, flt2=flt2, ineq=ineqs[0])
    else:
        f4 = f4.format(flt1=flt1, flt2=flt2, ineq=ineqs[1])

    c4 = c4.format(flt1=flt1, flt2=flt2, ineq=ineqs[0])

    fr5 = frac_generator(1, 10, 5)
    flt3 = round(fr5[0]/fr5[1], 1)

    ineq_id = np.random.randint(0,2)
    f5 = f5.format(i1=flt3, ineq=ineqs[ineq_id])
    c5 = c5.format(i1=flt3)

    ex_list = [[f1, c1], [f2, c2], [f3, c3], [f4, c4], [f5, c5]]
    ans_list = make_shuffle_example(ex_list,right)

    cases = ""
    for i in range(5):
        if i != ans_list[0]:
            cases = cases + answer_dict[i] + " " + ans_list[i+1][1]

    stem = stem.format(ex1=ans_list[1][0], ex2=ans_list[2][0], ex3=ans_list[3][0], ex4=ans_list[4][0], ex5=ans_list[5][0])
    answer = answer.format(a1=answer_dict[ans_list[0]])
    comment = comment.format(cases=cases)

    return stem, answer, comment

# 이문제 아예 출력 안나옴 
# 1-1-2-32
def intandrational112_Stem_019():
    stem = "다음 중 $$수식$$□$$/수식$$ 안에 들어갈 부등호가 나머지 넷과 다른 하나는?\n"\
        "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{cases}"\
        "따라서 부등호가 나머지 넷과 다른 하나는 {a1}이다.\n\n"

    # &lt; <, &gt; >
    ineqs = ["&lt;", "&gt;"]
    right = np.random.randint(0,5)

    f1 = "$$수식$${p1}``□``{p2}$$/수식$$"
    f2 = "$$수식$${i1}``□``{i2}$$/수식$$"
    f3 = "$$수식$$-{i1}``□``-{i2}$$/수식$$"
    f4 = "$$수식$${i1}``□``{i2}$$/수식$$"
    f5 = "$$수식$$LEFT | {i1} RIGHT |``□``LEFT | {i2} RIGHT |$$/수식$$"
    
    c1 = "$$수식$${p1}`=`{p1_}$$/수식$$, $$수식$${p2}`=`{p2_}$$/수식$$이므로 $$수식$${p1}`{ineq}`{p2}$$/수식$$\n"
    c2 = "음수는 항상 양수보다 작으므로 $$수식$${i1}`{ineq}`{i2}$$/수식$$\n"
    c3 = "$$수식$$LEFT | -{i1} RIGHT |`{ineq_}`LEFT | -{i2} RIGHT |$$/수식$$이므로 $$수식$$-{i1}`{ineq}`-{i2}$$/수식$$\n"
    c4 = "$$수식$${i1}`{ineq}`{i2}$$/수식$$\n"
    c5 = "$$수식$$LEFT | {i1} RIGHT |`{ineq}`LEFT | {i2} RIGHT |$$/수식$$\n"

    fr1 = frac_generator(1, 6, 4)
    p1 = "{%d} over {%d}" % (fr1[0], fr1[1])
    fr2 = frac_generator(1, 6, 5)
    while fr1[1] == fr2[1]:
        fr2 = frac_generator(1, 6, 5)
    p2 = "{%d} over {%d}" % (fr2[0], fr2[1])

    lcm_ = lcm(fr1[1], fr2[1])
    mult = [int(lcm_/fr1[1]), int(lcm_/fr2[1])]
    p1_ = "{%d} over {%d}" % (fr1[0]*mult[0], lcm_)
    p2_ = "{%d} over {%d}" % (fr2[0]*mult[1], lcm_)

    if right == 0:
        if fr1[0]*mult[0] > fr2[0]*mult[1]:
            f1 = f1.format(p1=p1, p2=p2)
            c1 = c1.format(p1=p1, p1_=p1_, p2=p2, p2_=p2_, ineq=ineqs[1])
        else:
            f1 = f1.format(p1=p2, p2=p1)
            c1 = c1.format(p1=p2, p1_=p2_, p2=p1, p2_=p1_, ineq=ineqs[1])
    else:
        if fr1[0]*mult[0] < fr2[0]*mult[1]:
            f1 = f1.format(p1=p1, p2=p2)
            c1 = c1.format(p1=p1, p1_=p1_, p2=p2, p2_=p2_, ineq=ineqs[0])
        else:
            f1 = f1.format(p1=p2, p2=p1)
            c1 = c1.format(p1=p2, p1_=p2_, p2=p1, p2_=p1_, ineq=ineqs[0])

   
    int1 = np.random.randint(1,6)

    if right == 1:
        f2 = f2.format(i1=0, i2=-int1)
        c2 = c2.format(i1=0, i2=-int1, ineq=ineqs[1])
    else:
        f2 = f2.format(i1=-int1, i2=0)
        c2 = c2.format(i1=-int1, i2=0, ineq=ineqs[0])

    ints = random.sample(list(range(1,10)), 2)
    ints[0] = ints[0] + round(np.random.rand(),1)
    ints.sort()
    
    if right == 2:
        f3 = f3.format(i1=ints[0], i2=ints[1])
        c3 = c3.format(i1=ints[0], i2=ints[1], ineq=ineqs[1], ineq_=ineqs[0])
    else:
        f3 = f3.format(i1=ints[1], i2=ints[0])
        c3 = c3.format(i1=ints[1], i2=ints[0], ineq=ineqs[0], ineq_=ineqs[1])

    fr3 = frac_generator(1, 10, 3)
    fr4 = frac_generator(1, 10, 5)

    flt1 = round(fr3[0]/fr3[1], 1)
    flt2 = round(fr4[0]/fr4[1], 1)

    if right == 3:
        f4 = f4.format(i1=flt1, i2=-flt2)
        c4 = c4.format(i1=flt1, i2=-flt2, ineq=ineqs[1])
    else:
        f4 = f4.format(i1=-flt1, i2=flt2)
        c4 = c4.format(i1=-flt1, i2=flt2, ineq=ineqs[0])


    ints = random.sample(list(range(1,8)), 2)
    ints.sort()

    if right == 4:
        f5 = f5.format(i1=-ints[1], i2=-ints[0])
        c5 = c5.format(i1=-ints[1], i2=-ints[0], ineq=ineqs[1])
    else:
        f5 = f5.format(i1=-ints[0], i2=-ints[1])
        c5 = c5.format(i1=-ints[0], i2=-ints[1], ineq=ineqs[0])

    ex_list = [[f1, c1], [f2, c2], [f3, c3], [f4, c4], [f5, c5]]
    ans_list = make_shuffle_example(ex_list, right)

    cases = ""
    for i in range(5):
        cases = cases + answer_dict[i] + " " + ans_list[i+1][1]

    stem = stem.format(ex1=ans_list[1][0], ex2=ans_list[2][0], ex3=ans_list[3][0], ex4=ans_list[4][0], ex5=ans_list[5][0])
    answer = answer.format(a1=answer_dict[ans_list[0]])
    comment = comment.format(cases=cases, a1=answer_dict[ans_list[0]])

    return stem, answer, comment


# 1-1-2-34
def intandrational112_Stem_020():
    stem = "다음 수를 {cond} 수부터 차례대로 나열할 때, {cnt} 번째에 오는 수는?\n"\
        "$$표$${number_lists}$$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "주어진 수의 대소를 비교하면\n"\
        "$$수식$${equations}$$/수식$$\n"\
        "따라서 {cond} 수부터 차례대로 나열할 때, {cnt} 번째에 오는 수는 "\
        "$$수식$${ans}$$/수식$$이다.\n\n"

    cond_ind = np.random.randint(0,2)
    cond = ["작은", "큰"][cond_ind]

    cnt_ind = np.random.randint(0,3)
    cnt = ["첫", "두", "세"][cnt_ind]

    tot = 8
    # num1 : integer, num2 : decimal, num3 : fraction
    nums = random.sample(list(range(2,5)), 2)
    nums.sort()
    num1 = nums[1]
    num2 = nums[0]
    num3 = tot - num1 - num2

    ans_ind = cond_ind * tot
    if cond_ind == 0:
        ans_ind = ans_ind + cnt_ind
    else:
        ans_ind = ans_ind - 1 - cnt_ind
    
    ex_base = list(range(tot))
    del ex_base[ans_ind]
    examples_idx = random.sample(ex_base, 4)
    examples_idx.append(ans_ind)

    # &lt; : <

    integers = random.sample(list(range(1,10)), num1)
    
    decimals = random.sample(list(range(1,6)), num2)
    for i in range(num2):
        decimals[i] = decimals[i] + round(np.random.rand(), 1)

    numbers = integers + decimals

    fractions = []
    for i in range(num3):
        fr = frac_generator(1, 7, 5)
        fractions.append([fr[0], fr[1]])
        numbers.append(fr[0]/fr[1])
    
    numbers = random_minus(numbers)
    numbers.sort()
    numbers_ = copy.deepcopy(numbers)

    equations = ""
    for i in range(tot):
        for j in range(len(fractions)):
            if abs(numbers[i]) == fractions[j][0]/fractions[j][1]:
                if numbers[i] > 0:
                    numbers_[i] = "{%d} over {%d}" % (fractions[j][0], fractions[j][1])
                else:
                    numbers_[i] = "-{%d} over {%d}" % (fractions[j][0], fractions[j][1])
        if equations == "":
            equations = equations + str(numbers_[i])
        else:
            equations = equations + "`&lt;`" + str(numbers_[i])

    ans_list = []
    ans = numbers_[ans_ind]
    for i in range(5):
        ans_list.append(numbers_[examples_idx[i]])
    
    np.random.shuffle(numbers_)
    number_lists = ""
    for i in range(len(numbers_)):
        if number_lists == "":
            number_lists = number_lists  + "$$수식$$" + str(numbers_[i]) + "$$/수식$$"
        else:
            number_lists = number_lists + ", $$수식$$" + str(numbers_[i]) + "$$/수식$$"

    example_list = make_shuffle_example(ans_list, 4)

    stem = stem.format(cond=cond, cnt=cnt, number_lists=number_lists, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(cond=cond, cnt=cnt, equations=equations, ans=ans)

    return stem, answer, comment


# 1-1-2-35
def intandrational112_Stem_021():
    stem = "다음 조건을 모두 만족시키는 서로 다른 세 유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$의 대소 관계로 옳은 것은?\n"\
        "$$표$$(가) $$수식$$a`&lt;`-{n1}$$/수식$$\n(나) $$수식$$b`&lt;`{n1}$$/수식$$, $$수식$$| b |`=`{n1}$$/수식$$\n(다) {statement} $$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$\n② $$수식$${ex2}$$/수식$$\n③ $$수식$${ex3}$$/수식$$\n④ $$수식$${ex4}$$/수식$$\n⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "(나)에서 $$수식$$b`&lt;`{n1}$$/수식$$, $$수식$$| b |`=`{n1}$$/수식$$이므로 $$수식$$b`=`-{n1}$$/수식$$\n"\
        "이때 (가)에서 $$수식$$a`&lt;`-{n1}$$/수식$$이므로 $$수식$$a`&lt;`b$$/수식$$\n"\
        "또 (다)에서 {statement_com}\n"\
        "$$수식$$THEREFORE```{ans}$$/수식$$이다.\n\n"
    
    nums = ["a", "b", "c"]
    order = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    ex_lists = []
    for i in range(len(order)):
        ex_lists.append(nums[order[i][0]] + "`&lt;`" + nums[order[i][1]] + "`&lt;`" + nums[order[i][2]])

    n1 = np.random.randint(1,7)
    cond_ind = np.random.randint(0,2)
    cond = ["가깝다.", "멀다."][cond_ind]
    st_f = "수직선에서 $$수식$${p1}$$/수식$$를 나타내는 점보다 $$수식$${p2}$$/수식$$를 나타내는 점이 $$수식$$0$$/수식$$을 나타내는 점에 더 {cond}"
    st_c = "$$수식$${p1}$$/수식$$를 나타내는 점이 $$수식$${p2}$$/수식$$를 나타내는 점보다 오른쪽에 있다."

    if cond_ind == 0:
        statement = st_f.format(p1="b", p2="c", cond=cond)
        statement_com = st_c.format(p1="c", p2="b")
        ans_ind = 0
    else:
        statement = "$$수식$$c$$/수식$$는 $$수식$$a$$/수식$$와 부호가 같고, " + st_f.format(p1="a", p2="c", cond=cond)
        statement_com = st_c.format(p1="a", p2="c")
        ans_ind = 4

    base = list(range(6))
    del base[ans_ind]
    examples_idx = random.sample(base, 4)
    examples_idx.append(ans_ind)

    ans_list = []
    ans = ex_lists[ans_ind]
    for i in range(5):
        ans_list.append(ex_lists[examples_idx[i]])

    example_list = make_shuffle_example(ans_list, 4)

    stem = stem.format(n1=n1, statement=statement, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, statement_com=statement_com, ans=ans)

    return stem, answer, comment


# 1-1-2-37
def intandrational112_Stem_022():
    stem = "다음 조건을 모두 만족시키는 서로 다른 세 유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$의 대소 관계를 부등호를 사용하여 바르게 나타낸 것은?\n"\
        "$$표$$(가) {st1}\n(나) {st2}\n$$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$\n② $$수식$${ex2}$$/수식$$\n③ $$수식$${ex3}$$/수식$$\n④ $$수식$${ex4}$$/수식$$\n⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "조건 (가)에서 서로 다른 두 유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$의 절댓값이 같으므로 $$수식$$a`{ineqa}`0$$/수식$$, $$수식$$b`{ineqb}`0$$/수식$$\n"\
        "$$수식$$THEREFORE```a`{ineq1}`b$$/수식$$     $$수식$$CDOTS`$$/수식$$㉠\n"\
        "{st2_com}\n"\
        "$$수식$$THEREFORE```c`{ineq2}`{p}$$/수식$$     $$수식$$CDOTS`$$/수식$$㉡\n"\
        "㉠, ㉡에 의하여 "\
        "$$수식$${ans}$$/수식$$\n\n"
    
    nums = ["a", "b", "c"]
    order = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    ex_lists = []
    for i in range(len(order)):
        ex_lists.append(nums[order[i][0]] + "`&lt;`" + nums[order[i][1]] + "`&lt;`" + nums[order[i][2]])

    # &lt; < &gt; >
    sign = ["양수", "음수"]
    ineqs = ["&gt;", "&lt;"]

    a_si = np.random.randint(0,2)
    ineqa = ineqs[a_si]
    cnd1 = sign[a_si]
    b_si = 1 - a_si
    ineqb = ineqs[b_si]
    ineq1 = ineqs[a_si]

    c_si = np.random.randint(0,2)
    cnd2 = sign[c_si]

    st1 = "$$수식$$a$$/수식$$는 {cnd1}이고 $$수식$$| a |`=`| b |$$/수식$$이다.".format(cnd1=cnd1)
    st2_f = "$$수식$$c$$/수식$$는 {cnd2}이고 $$수식$$| b |`{ineq_}` |c|$$/수식$$이다."
    st2_c1 = "조건 (가), (나)에 의하여 $$수식$$| {p1} |`&lt;`| {p2} |$$/수식$$이고 " + \
        "$$수식$${p1}$$/수식$$, $$수식$${p2}$$/수식$$가 모두 {cnd}이므로"
    st2_c2 = "조건 (나)에 의하여 $$수식$$| {p1} |`&lt;`| {p2} |$$/수식$$이고 " + \
        "$$수식$${p1}$$/수식$$, $$수식$${p2}$$/수식$$가 모두 {cnd}이므로"

    ineq_rf = np.random.randint(0,2)
    ineq_ = ineqs[ineq_rf]
    st2 = st2_f.format(cnd2=cnd2, ineq_=ineq_)

    if a_si == c_si:
        p = "a"
        # |b| > |c|
        if ineq_rf == 0:
            st2_com = st2_c1.format(p1="c", p2="a", cnd=cnd1)
            ineq2 = ineqs[1-a_si]
            ans_ind = 3 - 2 * a_si
        # |b| < |c|
        else:
            st2_com = st2_c1.format(p1="a", p2="c", cnd=cnd1)
            ineq2 = ineqs[a_si]
            ans_ind = 2 + 2 * a_si
    else:
        p = "b"
        # |b| > |c|
        if ineq_rf == 0:
            st2_com = st2_c2.format(p1="c", p2="b", cnd=cnd2)
            ineq2 = ineqs[1-b_si] 
            ans_ind = 2 * b_si + 1
        # |b| < |c|
        else:
            st2_com = st2_c2.format(p1="b", p2="c", cnd=cnd2)
            ineq2 = ineqs[b_si]
            ans_ind = 5 * b_si

    base = list(range(6))
    del base[ans_ind]
    examples_idx = random.sample(base, 4)
    examples_idx.append(ans_ind)

    ans_list = []
    ans = ex_lists[ans_ind]
    for i in range(5):
        ans_list.append(ex_lists[examples_idx[i]])

    example_list = make_shuffle_example(ans_list, 4)

    stem = stem.format(st1=st1, st2=st2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(ineqa=ineqa, ineqb=ineqb, ineq1=ineq1, ineq2=ineq2, st2_com=st2_com, p=p, ans=ans)

    return stem, answer, comment



# 1-1-2-38
def intandrational112_Stem_023():
    stem = "다음 중 부등호를 사용하여 나타낸 것으로 옳지 않은 것은?\n"\
        "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{case}\n\n"

    # &lt; <, &gt; >
    ineqs = ["&lt;", "&gt;"]
    right = np.random.randint(0,5)

    strs1 = ["작다", "크다", "작지 않다", "크지 않다", "크거나 같다", "작거나 같다"]
    #cs1 = ["&lt;", "&gt;", "GEQ", "LEQ", "GEQ", "LEQ"]
    cs1 = ["&lt;", "&gt;", "GEQ", "LEQ"]
    strs2_1 = ["보다 크고", " 이상이고", " 초과이고"]
    cs2_1 = ["&lt;", "LEQ", "&lt;"]
    strs2_2 = [" 이하이다", " 미만이다", "보다 작다"]
    cs2_2 = ["LEQ", "&lt;", "&lt;"]

    f1 = "$$수식$$a$$/수식$$는 $$수식$${num1}$$/수식$$보다 {cond}."
    c1 = "$$수식$$a`{ineq}`{num1}$$/수식$$"
    f2 = "$$수식$$a$$/수식$$는 $$수식$${num1}$$/수식$${cond1}, $$수식$${num2}$$/수식$${cond2}."
    c2 = "$$수식$${num1}`{ineq1}`a`{ineq2}`{num2}$$/수식$$"

    ex_list = []
    for i in range(5):
        rf = np.random.randint(0,2)
        if rf == 0:
            # minus == 0 : -, minus == 1 : + (3:7)
            minus = int(np.random.rand() + 0.7)
            n1 = np.random.randint(1,9) * (2*minus-1)
            #cond_rf = np.random.randint(0,5)
            cond_rf = np.random.randint(0,3)
            f = f1.format(num1=n1, cond=strs1[cond_rf])
            if right == i:
                while True:
                    cond_rf_index = np.random.randint(0,3)
                    if cond_rf_index != cond_rf:
                        break

                print("cond_rf: ", cond_rf)
                print("cond_rf_index: ", cond_rf_index)
                c = c1.format(num1=n1, ineq=cs1[cond_rf_index])
                c_ = c1.format(num1=n1, ineq=cs1[cond_rf])
            else:
                c = c1.format(num1=n1, ineq=cs1[cond_rf])
                c_ = c
            st = f + " → " + c
            ex_list.append([st, c_])
        else:
            # minus == 0 : -, minus == 1 : + (3:7)
            minus = int(np.random.rand() + 0.7)
            nums = random.sample(list(range(0,8)), 2)
            nums.sort()
            n1 = nums[0] * (2*minus-1)
            n2 = nums[1]
            rf1 = np.random.randint(0,3)
            rf2 = np.random.randint(0,3)
            f = f2.format(num1=n1, num2=n2, cond1=strs2_1[rf1], cond2=strs2_2[rf2])
            if right == i:
                while True:
                    rf1_index = np.random.randint(0,3)
                    rf2_index = np.random.randint(0,3)
                    if rf1_index != rf1 and rf2_index != rf2:
                        break
                c = c2.format(num1=n1, num2=n2, ineq1=cs2_1[rf1_index], ineq2=cs2_2[rf1_index])
                c_ = c2.format(num1=n1, num2=n2, ineq1=cs2_1[rf1], ineq2=cs2_2[rf2])
            else:
                c = c2.format(num1=n1, num2=n2, ineq1=cs2_1[rf1], ineq2=cs2_2[rf2])
                c_ = c
            st = f + " → " + c
            ex_list.append([st, c_])

    ans_list = make_shuffle_example(ex_list, right)
    case = answer_dict[ans_list[0]] + " " + ans_list[ans_list[0]+1][1]

    stem = stem.format(ex1=ans_list[1][0], ex2=ans_list[2][0], ex3=ans_list[3][0], ex4=ans_list[4][0], ex5=ans_list[5][0])
    answer = answer.format(a1=answer_dict[ans_list[0]])
    comment = comment.format(case=case)

    return stem, answer, comment


# 1-1-2-39
def intandrational112_Stem_024():
    stem = "'{f}'를 부등호를 사용하여 바르게 나타낸 것은?\n"\
        "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{case}\n\n"

    nums = random.sample(list(range(10)), 2)
    minus = np.random.randint(0,2)
    if minus == 0:
        num1 = -nums[0]
        num2 = nums[1]
    else:
        nums.sort()
        num1 = nums[0]
        num2 = nums[1]

    # &lt; <, &gt; >
    ineqs = ["&lt;", "&gt;"]
    right = np.random.randint(0,5)

    cs1 = ["&lt;", "&gt;", "GEQ", "LEQ"]
    strs2_1 = ["보다 크고", " 이상이고", " 초과이고"]
    cs2_1 = ["&lt;", "LEQ"]
    strs2_2 = [" 미만이다", " 이하이다", "보다 작다"]
    cs2_2 = ["&lt;", "LEQ"]

    c1 = "$$수식$$a`{ineq}`{num1}$$/수식$$"
    f2 = "$$수식$$a$$/수식$$는 $$수식$${num1}$$/수식$${cond1}, $$수식$${num2}$$/수식$${cond2}."
    c2 = "$$수식$${num1}`{ineq1}`a`{ineq2}`{num2}$$/수식$$"

    rf1 = np.random.randint(0,3)
    rf2 = np.random.randint(0,3)
    f = f2.format(num1=num1, num2=num2, cond1=strs2_1[rf1], cond2=strs2_2[rf2])

    ans = c2.format(num1=num1, num2=num2, ineq1=cs2_1[rf1%2], ineq2=cs2_2[rf2%2])
    cf = c2.format(num1=num1, num2=num2, ineq1=cs2_1[(rf1+1)%2], ineq2=cs2_2[rf2%2])
    cs = c2.format(num1=num1, num2=num2, ineq1=cs2_1[(rf1+1)%2], ineq2=cs2_2[(rf2+1)%2])
    ct = c2.format(num1=num1, num2=num2, ineq1=cs2_1[rf1%2], ineq2=cs2_2[(rf2+1)%2])
    
    rf = np.random.randint(0,2)
    c_rf = np.random.randint(0,4)
    if rf == 1:
        c_ = c1.format(num1=num1, ineq=cs1[c_rf])
    else:
        c_ = c1.format(num1=num2, ineq=cs1[c_rf])

    ex_list = [ans, cf, cs, ct, c_]
    ans_list = make_shuffle_example(ex_list, 0)

    case = answer_dict[ans_list[0]] + " " + ans_list[ans_list[0]+1]

    stem = stem.format(f=f, ex1=ans_list[1], ex2=ans_list[2], ex3=ans_list[3], ex4=ans_list[4], ex5=ans_list[5])
    answer = answer.format(a1=answer_dict[ans_list[0]])
    comment = comment.format(case=case)

    return stem, answer, comment


# 1-1-2-41
def intandrational112_Stem_025():
    stem = "{f}{j} 만족시키는 정수 $$수식$$x$$/수식$$의 {target}?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{f}{j} 만족시키는 정수는 {num_lists}이므로 {target}\n$$수식$${sums}{equal}{ans}$$/수식$$이다.\n\n"
    
    target_idx = np.random.randint(0,2)
    target = ["값들의 합은", "개수는"][target_idx]

    nums = random.sample(list(range(10)), 2)
    minus = np.random.randint(0,2)
    if minus == 0:
        num1 = -nums[0]
        num2 = nums[1]
    else:
        while abs(nums[0]-nums[1]) == 1:
            nums = random.sample(list(range(10)), 2)
        nums.sort()
        num1 = nums[0]
        num2 = nums[1]
    j = proc_jo(num2, 4)

    c = ["&lt;", "LEQ"]

    rf1 = np.random.randint(0,2)
    rf2 = np.random.randint(0,2)

    f = "$$수식$${num1}`{ineq1}`a`{ineq2}`{num2}$$/수식$$".format(num1=num1, num2=num2, ineq1=c[rf1], ineq2=c[rf2])

    if minus == 0:
        low = num1 + 1 - rf1
        cnt1 = abs(num1) - 1 + rf1
        cnt2 = num2 - 1 + rf2
        ans1 = cnt1 + cnt2 + 1
    else:
        low = num1 + 1 - rf1
        cnt1 = num1 - rf1
        cnt2 = num2 - 1 + rf2
        ans1 = cnt2 - cnt1

    ans = 0
    num_lists = ""
    sums = ""
    equal = "`=`"
    for i in range(ans1):
        if num_lists == "":
            num_lists = num_lists + "$$수식$$" + str(low+i) + "$$/수식$$"
            sums = sums + str(low+i)
        else:
            num_lists = num_lists + ", $$수식$$" + str(low+i) + "$$/수식$$"
            sums = sums + "`+`" + str(low+i)
        ans = ans + low+i

    if target_idx == 1:
        ans = ans1
        sums = ""
        equal = ""

    example_list = make_example(ans)

    stem = stem.format(f=f, j=j, target=target, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(f=f, j=j, target=target, num_lists=num_lists, equal=equal, sums=sums, ans=ans)

    return stem, answer, comment


# 1-1-2-42
def intandrational112_Stem_026():
    stem = "다음 조건을 모두 만족하는 서로 다른 세 유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$의 대소 관계를 옳게 나타낸 것은?\n"\
        "$$표$$(가) {st1}\n(나) {st2}\n (다) {st3}\n (라) {st4}\n$$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "(가), (다)에 의해 $$수식$$a`{ineqa}`0$$/수식$$, $$수식$$b`{ineqb}`0$$/수식$$이고 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$의 "\
        "절댓값은 $$수식$${num1}`times`{half_frac}`=`{num1_half}$$/수식$$이므로 $$수식$$a`=`{a}$$/수식$$, $$수식$$b`=`{b}$$/수식$$\n"\
        "(나), (라)에 의해 $$수식$$c`=`{c}$$/수식$$\n"\
        "$$수식$$THEREFORE```{ans}$$/수식$$\n\n"
    
    nums = ["a", "b", "c"]
    order = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    ex_lists = []
    for i in range(len(order)):
        ex_lists.append(nums[order[i][0]] + "`&lt;`" + nums[order[i][1]] + "`&lt;`" + nums[order[i][2]])

    # &lt; < &gt; >
    sign = ["양수", "음수"]
    ineqs = ["&gt;", "&lt;"]
    half_frac = "{%d} over {%d}" % (1,2)

    a_si = np.random.randint(0,2)
    ineqa = ineqs[a_si]
    cnd1 = sign[a_si]
    b_si = 1 - a_si
    ineqb = ineqs[b_si]
    ineq1 = ineqs[a_si]

    c_si = np.random.randint(0,2)
    ineqc = ineqs[c_si]

    integers = random.sample(list(range(1,10)), 2)
    integers.sort()

    st1 = "$$수식$$a$$/수식$$와 $$수식$$b$$/수식$$의 절댓값은 같다."
    st3_f = "$$수식$${p1}$$/수식$$은 $$수식$${p2}$$/수식$$보다 $$수식$${num1}$$/수식$$만큼 크다."
    st2 = "$$수식$$c`{ineqc}`0$$/수식$$".format(ineqc=ineqc)
    st4_f = "$$수식$$c$$/수식$$의 절댓값은 $$수식$${num2}$$/수식$$이다."

    rf = np.random.randint(0,2)
    # |a| < |c|
    if rf == 0:
        num1 = integers[0]*2
        num1_half = integers[0]
        num2 = integers[1]
        # a < 0 , c < 0
        if a_si == 1:
            p1 = "b"
            p2 = "a"
            a = -integers[0]
            b = integers[0]
            if c_si == 1:
                c = -num2
                ans_ind = 4
            else:
                c = num2
                ans_ind = 0
        else:
            p1 = "a"
            p2 = "b"
            a = integers[0]
            b = -integers[0]
            if c_si == 1:
                c = -num2
                ans_ind = 5
            else:
                c = num2
                ans_ind = 2
    # |a| > |c|
    else:
        num1 = integers[1]*2
        num1_half = integers[1]
        num2 = integers[0]
        # a < 0 , c < 0
        if a_si == 1:
            p1 = "b"
            p2 = "a"
            a = -integers[1]
            b = integers[1]
            if c_si == 1:
                c = -num2
                ans_ind = 1
            else:
                c = num2
                ans_ind = 1
        else:
            p1 = "a"
            p2 = "b"
            a = integers[1]
            b = -integers[1]
            if c_si == 1:
                c = -num2
                ans_ind = 3
            else:
                c = num2
                ans_ind = 3

    st3 = st3_f.format(p1=p1, p2=p2, num1=num1)
    st4 = st4_f.format(num2=num2)

    base = list(range(6))
    del base[ans_ind]
    examples_idx = random.sample(base, 4)
    examples_idx.append(ans_ind)

    ans_list = []
    ans = ex_lists[ans_ind]
    for i in range(5):
        ans_list.append(ex_lists[examples_idx[i]])

    example_list = make_shuffle_example(ans_list, 4)

    stem = stem.format(st1=st1, st2=st2, st3=st3, st4=st4, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(ineqa=ineqa, ineqb=ineqb, num1=num1, half_frac=half_frac, num1_half=num1_half, a=a, b=b, c=c, ans=ans)

    return stem, answer, comment


# 1-1-2-43
def intandrational112_Stem_027():
    stem = "절댓값이 $$수식$${p1}$$/수식$$인 두 수 사이에 있는 정수의 {target}?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "절댓값이 $$수식$${p1}$$/수식$$인 두 수는 $$수식$$-{p1}$$/수식$$과 $$수식$${p1}$$/수식$$이고, "\
        "$$수식$$-{num1}`&lt;`-{p1}`&lt;`-{num2}$$/수식$$, $$수식$${num2}`&lt;`{p1}`&lt;`{num1}$$/수식$$이므로 $$수식$$-{p1}$$/수식$$과 $$수식$${p1}$$/수식$$ 사이에 있는 정수는 "\
        "{num_lists}이므로 {target} {target_ans}\n\n"
    
    target_idx = 1
    target = ["값들의 합은", "개수는"][target_idx]
    target_ans = ["$$수식$${sums}`=`{ans}$$/수식$$이다.", "$$수식$${ans}$$/수식$$이다."][target_idx]

    fr = frac_generator(1, 10, 5)
    p1 = "{%d} over {%d}" % (fr[0], fr[1])
    num2 = int(fr[0]/fr[1])
    num1 = num2 + 1

    tot_num = 2 * num2 + 1
    low = -num2

    sum_tot = 0
    num_lists = ""
    sums = ""
    for i in range(tot_num):
        if num_lists == "":
            num_lists = num_lists + "$$수식$$" + str(low+i) + "$$/수식$$"
            sums = sums + str(low+i)
        else:
            num_lists = num_lists + ", $$수식$$" + str(low+i) + "$$/수식$$"
            sums = sums + "`+`" + str(low+i)
        sum_tot = sum_tot + low+i

    if target_idx == 0:
        target_ans = target_ans.format(sums=sums, ans=sum_tot)
        ans = sum_tot
    else:
        target_ans = target_ans.format(ans=tot_num)
        ans = tot_num

    example_list = make_example(ans)

    stem = stem.format(p1=p1, target=target, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(p1=p1, num1=num1, num2=num2, target=target, target_ans=target_ans, num_lists=num_lists, ans=ans)

    return stem, answer, comment


# 1-1-2-44
def intandrational112_Stem_028():
    stem = "$$수식$$0$$/수식$$보다 크고 $$수식$$x$$/수식$$보다 작거나 같은 정수가 아닌 유리수 중 분모가 $$수식$${num1}$$/수식$$인 수의 개수가 "\
        "$$수식$${num2}$$/수식$$일 때, 자연수 $$수식$$x$$/수식$$의 값은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "(1) $$수식$$x`=`1$$/수식$$일 때,\n{frac_list1}의 $$수식$${n1}$$/수식$$개\n"\
        "(2) $$수식$$x`=`2$$/수식$$일 때,\n{frac_list2}의 $$수식$${n2}$$/수식$$개\n"\
        "(3) $$수식$$x`=`3$$/수식$$일 때,\n{frac_list3}의 $$수식$${n3}$$/수식$$개\n"\
        "이상에서 $$수식$$x$$/수식$$가 $$수식$$1$$/수식$$만큼 커질 때마다 분모가 $$수식$${num1}$$/수식$$인 정수가 아닌 유리수가 "\
        "$$수식$${num3}$$/수식$$개씩 증가한다.\n"\
        "이때 $$수식$${num2}`=`{num3}`times`{ans}$$/수식$$이므로 구하는 자연수 $$수식$$x$$/수식$$는 "\
        "$$수식$${ans}$$/수식$$이다.\n\n"
    
    num1 = np.random.randint(3,8)
    num3 = 0

    f = []
    for i in range(num1-1):
        if gcd(num1, i+1) == 1:
            num3 = num3 + 1
            f.append(i+1)
    
    ans = np.random.randint(5,19)
    num2 = num3 * ans

    frac_list1 = ""
    for i in range(num3):
        if frac_list1 == "":
            frac_list1 = frac_list1 + "$$수식$${%d} over {%d}$$/수식$$" % (f[i], num1)
        else:
            frac_list1 = frac_list1 + ", $$수식$${%d} over {%d}$$/수식$$" % (f[i], num1)
    n1 = num3
    
    frac_list2 = frac_list1
    for i in range(num3):
        frac_list2 = frac_list2 + ", $$수식$${%d} over {%d}$$/수식$$" % (num1 + f[i], num1)
    n2 = num3 * 2

    frac_list3 = frac_list2
    for i in range(num3):
        frac_list3 = frac_list3 + ", $$수식$${%d} over {%d}$$/수식$$" % (2*num1 + f[i], num1)
    n3 = num3 * 3

    example_list = make_example(ans)

    stem = stem.format(num1=num1, num2=num2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num2=num2, num3=num3, n1=n1, n2=n2, n3=n3, frac_list1=frac_list1, frac_list2=frac_list2, frac_list3=frac_list3, ans=ans)

    return stem, answer, comment


# 1-1-2-48
def intandrational112_Stem_029():
    stem = "다음 중 계산 결과가 나머지 넷과 다른 하나는?\n"\
        "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{cases}"\
        "따라서 계산 결과가 나머지 넷과 다른 하나는 {dict_}이다.\n\n"

    f = "$$수식$$   {n1}`+` {n2} $$/수식$$"
    c = "$$수식$$   {n1}`+`{n2}`=`{a}$$/수식$$\n"
    ex_list = []

    same_ans = np.random.randint(3,10)
    same_ans_str = "" + str(same_ans)
    nums = random.sample(list(range(-3,9)),5)
    for i in range(4):
        n1 = nums[i]
        n2 = same_ans - n1
        if n1 > 0:
            n1 = "" + str(n1)
        elif n1<0:
            n1="(" + str(n1)+")"
        if n2 > 0:
            n2 = "" + str(n2)
        elif n2<0:
            n2="(" + str(n2)+")"
        f1 = f.format(n1=n1, n2=n2)
        c1 = c.format(n1=n1, n2=n2, a=same_ans_str)
        ex_list.append([f1, c1])
    
    diff_ans = np.random.randint(-5, 5)
    if diff_ans > 0:
        diff_ans_str = "" + str(diff_ans)
    elif diff_ans<0:
        diff_ans_str = "-" + str(abs(diff_ans))
    n1 = nums[4]
    n2 = diff_ans - n1
    if n1 > 0:
        n1 = "" + str(n1)
    elif n1<0:
            n1="(" + str(n1)+")"
    if n2 > 0:
        n2 = "" + str(n2)
    elif n2<0:
            n2="(" + str(n2)+")"
    f1 = f.format(n1=n1, n2=n2)
    c1 = c.format(n1=n1, n2=n2, a=diff_ans_str)
    ex_list.append([f1, c1])

    ans_list = make_shuffle_example(ex_list, 4)
    cases = ""
    for i in range(5):
        cases = cases + answer_dict[i] + " " + ans_list[i+1][1]
    dict_ = answer_dict[ans_list[0]]

    stem = stem.format(ex1=ans_list[1][0], ex2=ans_list[2][0], ex3=ans_list[3][0], ex4=ans_list[4][0], ex5=ans_list[5][0])
    answer = answer.format(a1=answer_dict[ans_list[0]])
    comment = comment.format(cases=cases, dict_=dict_)

    return stem, answer, comment


# 1-1-2-49
def intandrational112_Stem_030():
    stem = "다음 중 계산 결과가 {cond}?\n"\
        "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{cases}"\
        "따라서 계산 결과가 {cond} {dict_}이다.\n\n"

    cond_idx = np.random.randint(0,4)
    cond = ["가장 큰 것은", "가장 작은 것은", "두 번째로 큰 것은", "두 번째로 작은 것은"][cond_idx]
    ans_idx = [4, 0, 3, 1][cond_idx]

    f = "$$수식$${n1}`+`{n2}$$/수식$$"
    c = "$$수식$${n1}`+`{n2}`=`{a}$$/수식$$\n"
    ex_list = []

    # num1 : num of integers, num2 : num of decimals, num3 : num of fractions
    tot = 5
    num1 = np.random.randint(1,3)
    num2 = np.random.randint(1,3)
    num3 = tot - num1 - num2
    answers = []
    ex_list = []

    integers = random.sample(list(range(1,10)), num1*2)
    integers = random_minus(integers)
    
    for i in range(num1):
        n1 = integers[i*2]
        n2 = integers[i*2 + 1]
        temp_ans = n1 + n2
        if temp_ans > 0:
            temp_ans_str = "" + str(temp_ans)
        else:
            temp_ans_str = temp_ans
        if n1 > 0:
                n1 = "" + str(n1)
        elif n1<0:
            n1="(" + str(n1)+")"
        if n2 > 0:
            n2 = "" + str(n2)
        elif n2<0:
            n2="(" + str(n2)+")"
        f1 = f.format(n1=n1, n2=n2)
        c1 = c.format(n1=n1, n2=n2, a=temp_ans_str)
        ex_list.append((f1, c1, temp_ans))
     
    decimals = random.sample(list(range(1,6)), num2*2)
    for i in range(num2*2):
        decimals[i] = decimals[i] + round(np.random.rand(), 1)
    decimals = random_minus(decimals)

    for i in range(num2):
        n1 = decimals[i*2]
        n2 = decimals[i*2 + 1]
        temp_ans = round(n1 + n2, 1)
        if temp_ans > 0:
            temp_ans_str = "" + str(temp_ans)
        else:
            temp_ans_str = temp_ans
    
        if n1 > 0:
            n1 = "" + str(n1)
        elif n1<0:
            n1="(" + str(n1)+")"
        if n2 > 0:
            n2 = "" + str(n2)
        elif n2<0:
            n2="(" + str(n2)+")"
        f1 = f.format(n1=n1, n2=n2)
        c1 = c.format(n1=n1, n2=n2, a=temp_ans_str)
        ex_list.append((f1, c1, temp_ans))

    fractions = []
    for i in range(num3*2):
        fr = frac_generator(1, 7, 5)
        if i != 0:
            while fractions[i-1][0]/fractions[i-1][1] == fr[0]/fr[1]:
                fr = frac_generator(1, 7, 5)
        fractions.append([fr[0], fr[1]])
    for i in range(num3*2):
        rf = np.random.randint(0,2)
        if rf == 1:
            fractions[i][0] = -fractions[i][0]
    
    
    for i in range(num3):
        n1 = fractions[i*2]
        n2 = fractions[i*2 + 1]
        temp_ans = sum_frac(n1, n2)
        if temp_ans[0] > 0:
            temp_ans_str = "{%d} over {%d}" % (temp_ans[0], temp_ans[1])
        else:
            temp_ans_str = "-{%d} over {%d}" % (abs(temp_ans[0]), temp_ans[1])
        if n1[0] > 0:
            n1 = "{%d} over {%d}" % (n1[0], n1[1])
        else:
            n1 = "-{%d} over {%d}" % (abs(n1[0]), n1[1])
        if n2[0] > 0:
            n2 = "{%d} over {%d}" % (n2[0], n2[1])
        else:
            n2 = "-{%d} over {%d}" % (abs(n2[0]), n2[1])
        f1 = f.format(n1=n1, n2=n2)
        c1 = c.format(n1=n1, n2=n2, a=temp_ans_str)
        ex_list.append((f1, c1, temp_ans[0]/temp_ans[1]))

    ex_list = sorted(ex_list, key=lambda element: element[2])

    ans_list = make_shuffle_example(ex_list, ans_idx)
    cases = ""
    for i in range(5):
        cases = cases + answer_dict[i] + " " + ans_list[i+1][1]
    dict_ = answer_dict[ans_list[0]]

    stem = stem.format(cond=cond, ex1=ans_list[1][0], ex2=ans_list[2][0], ex3=ans_list[3][0], ex4=ans_list[4][0], ex5=ans_list[5][0])
    answer = answer.format(a1=answer_dict[ans_list[0]])
    comment = comment.format(cond=cond, cases=cases, dict_=dict_)

    return stem, answer, comment



# 1-1-2-51
def intandrational112_Stem_031():
    stem = "다음 수 중 {cond1} 수를 $$수식$$a$$/수식$$, {cond2} 수를 $$수식$$b$$/수식$$라 할 때, $$수식$${target_eq}$$/수식$$의 값은?\n"\
        "$$표$${number_lists}$$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "주어진 수의 대소를 비교하면\n"\
        "$$수식$${equations}$$/수식$$\n"\
        "따라서 {cond1} 수는 $$수식$${ans1}$$/수식$$이므로 $$수식$$a`=`{ans1}$$/수식$$\n"\
        "{cond2} 수는 $$수식$${ans2}$$/수식$$이므로 $$수식$$b`=`{ans2}$$/수식$$\n"\
        "$$수식$$THEREFORE```{target_eq}`=`{ans}$$/수식$$이다.\n\n"

    cond1_ind = np.random.randint(0,2)
    cond1 = ["가장 작은", "가장 큰"][cond1_ind]

    cond2_ind = 1 - cond1_ind
    cond2 = ["절댓값이 가장 작은", "절댓값이 가장 큰"][cond2_ind]

    tot = 8
    # num1 : integer, num2 : decimal, num3 : fraction
    nums = random.sample(list(range(2,5)), 2)
    nums.sort()
    num1 = nums[1]
    num2 = nums[0]
    num3 = tot - num1 - num2

    ans1_ind = cond1_ind * (tot-1)
    ans2_ind = cond2_ind * (tot-1)

    # &lt; : <

    integers = random.sample(list(range(1,10)), num1)
    
    decimals = random.sample(list(range(1,6)), num2)
    for i in range(num2):
        decimals[i] = decimals[i] + round(np.random.rand(), 1)

    numbers = integers + decimals

    fractions = []
    for i in range(num3):
        fr = frac_generator2(1, [2, 4, 5], 5)
        fractions.append([fr[0], fr[1]])
        numbers.append(fr[0]/fr[1])
    
    numbers.sort()
    ans2 = numbers[ans2_ind]

    numbers = random_minus(numbers)
    if numbers[ans2_ind] != ans2:
        ans2 = -ans2

    numbers.sort()
    ans1 = numbers[ans1_ind]

    numbers_ = copy.deepcopy(numbers)

    equations = ""
    for i in range(tot):
        for j in range(len(fractions)):
            if abs(numbers[i]) == fractions[j][0]/fractions[j][1]:
                if numbers[i] > 0:
                    numbers_[i] = "{%d} over {%d}" % (fractions[j][0], fractions[j][1])
                else:
                    numbers_[i] = "-{%d} over {%d}" % (fractions[j][0], fractions[j][1])
        if equations == "":
            equations = equations + str(numbers_[i])
        else:
            equations = equations + "`&lt;`" + str(numbers_[i])
    
    np.random.shuffle(numbers_)
    number_lists = ""
    for i in range(len(numbers_)):
        if number_lists == "":
            number_lists = number_lists  + "$$수식$$" + str(numbers_[i]) + "$$/수식$$"
        else:
            number_lists = number_lists + ", $$수식$$" + str(numbers_[i]) + "$$/수식$$"

    eq_ind = np.random.randint(0,3)
    target_eq = ["a`-`b", "a`+`b", "a`times`b"][eq_ind]
    ans = [ans1-ans2, ans1+ans2, ans1*ans2][eq_ind]

    ans_list = []
    while len(ans_list) < 5:
        ex_idxs = random.sample(list(range(tot)), 2)
        if eq_ind == 0:
            ans_ = round(numbers[ex_idxs[0]] - numbers[ex_idxs[1]], 2)
        elif eq_ind == 1:
            ans_ = round(numbers[ex_idxs[0]] + numbers[ex_idxs[1]], 2)
        else:
            ans_ = round(numbers[ex_idxs[0]] * numbers[ex_idxs[1]], 2)
        if ans_ != ans:
            ans_list.append(ans_)
            ans_list = list(set(ans_list))

    ans_list[0] = ans

    example_list = make_shuffle_example(ans_list, 0)

    stem = stem.format(cond1=cond1, cond2=cond2, target_eq=target_eq, number_lists=number_lists, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(cond1=cond1, cond2=cond2, ans1=ans1, ans2=ans2, equations=equations, target_eq=target_eq, ans=ans)

    return stem, answer, comment


# 1-1-2-53
def intandrational112_Stem_032():
    stem = "다음 수 중 절댓값이 {cond1} 수를 $$수식$$a$$/수식$$, 절댓값이 {cond2} 수를 $$수식$$b$$/수식$$라 할 때, $$수식$${target_eq}$$/수식$$의 값은?\n"\
        "$$표$${number_lists}$$/표$$\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "$$수식$${equations}$$/수식$$이므로\n"\
        "$$수식$$a`=`{ans1_1}$$/수식$$, $$수식$$b`=`{ans2_1}$$/수식$$\n"\
        "$$수식$$THEREFORE```{eq1}`=`( {ans1_1} )`{sign}`( {ans2_1})$$/수식$$\n{cals}"\
        "$$수식$$THEREFORE```{target_eq}`=`{ans}$$/수식$$\n\n"

    tot = 8
    eq_ind = np.random.randint(0,2)
    eq1 = ["a`-`b", "a`+`b"][eq_ind]
    sign = ["-", "+"][eq_ind]

    c_idx = random.sample(list(range(4)), 2)
    cs = ["가장 작은", "가장 큰", "두번째로 작은", "두번째로 큰"]
    a_lists = [0, tot-1, 1, tot-2]
    cond1 = cs[c_idx[0]]
    cond2 = cs[c_idx[1]]
    ans1_idx = a_lists[c_idx[0]]
    ans2_idx = a_lists[c_idx[1]]

    fractions = []
    while len(fractions) < tot:
        fr = frac_generator2(1, [2, 3, 4, 5, 10, 20], 5)   
        same = 0    
        for i in range(len(fractions)):
            if fractions[i][1] == fr[0]/fr[1]:
                same = 1
        if same == 0:
            fractions.append(([fr[0], fr[1]], fr[0]/fr[1]))

    fractions.sort(key = lambda num: num[1])
    ans1 = copy.deepcopy(fractions[ans1_idx][0])
    ans2 = copy.deepcopy(fractions[ans2_idx][0])

    ans1_1 = 0
    ans2_1 = 0
    ans_isdec = [0, 0]

    strs = []
    equations = "|"
    for i in range(tot):     
        rf2 = np.random.randint(0,2)
        rf1 = np.random.randint(0,2)
        if rf2 == 0:
            append = 0
            if fractions[i][0][1] in [2,4,5,10]:
                if rf1 == 0:
                    strs.append(str(fractions[i][1]))
                    append = 1
                    if i == ans1_idx:
                        ans1_1 = fractions[i][1]
                        ans_isdec[0] = 1
                    if i == ans2_idx:
                        ans2_1 = fractions[i][1]
                        ans_isdec[1] = 1
            if append == 0:
                strs.append("+{%d} over {%d}" % (fractions[i][0][0], fractions[i][0][1]))
        else:
            if i == ans1_idx:
                ans1[0] = -ans1[0]
            if i == ans2_idx:
                ans2[0] = -ans2[0]
            append = 0
            if fractions[i][0][1] in [2,4,5,10]:
                if rf1 == 0:
                    strs.append(str(fractions[i][1]))
                    append = 1
                    if i == ans1_idx:
                        ans1_1 = fractions[i][1]
                        ans_isdec[0] = 1
                    if i == ans2_idx:
                        ans2_1 = fractions[i][1]
                        ans_isdec[1] = 1
            if append == 0:
                strs.append("-{%d} over {%d}" % (fractions[i][0][0], fractions[i][0][1]))
        
        if equations == "|":
            equations = equations + strs[i]
        else:
            equations = equations + "|`&lt;`| " + strs[i]
    equations = equations + "|"

    if ans1_1 == 0:
        ans1_1 = strs[ans1_idx]
    if ans2_1 == 0:
        ans2_1 = strs[ans2_idx]

    cals = ""
    cals_f = "$$수식$$=`( {a1})`{sign}`( {a2} )$$/수식$$\n"
          
    lcm_ = lcm(ans1[1], ans2[1])
    mult = [int(lcm_/ans1[1]), int(lcm_/ans2[1])]

    if ans_isdec[0] != 0 or ans_isdec[1] != 0 or mult[0] != 1 or mult[1] != 1 :
        if ans1[0] > 0:  
            a1 = "{%d} over {%d}" % (ans1[0]*mult[0], lcm_)
        else:
            a1 = "-{%d} over {%d}" % (abs(ans1[0])*mult[0], lcm_)
        if ans2[0] > 0:
            a2 = "{%d} over {%d}" % (ans2[0]*mult[1], lcm_)
        else:
            a2 = "-{%d} over {%d}" % (abs(ans2[0])*mult[1], lcm_)
        cals = cals_f.format(a1=a1, sign=sign, a2=a2)

    if eq_ind == 0:
        ab = ans1[0]*mult[0] - ans2[0]*mult[1]
    else:
        ab = ans1[0]*mult[0] + ans2[0]*mult[1]
    if ab > 0:
        ans_frac = "{%d} over {%d}" % (ab, lcm_)
    else:
        ans_frac = "-{%d} over {%d}" % (abs(ab), lcm_)

    cals = cals + "$$수식$$=`{ans_frac}".format(ans_frac=ans_frac)
    ctr = ctr_frac(ab, lcm_)
    if ctr[0] == -1:
        cals = cals + "$$/수식$$\n"
        ctr[0] = ab
    else:
        ans_frac = "{%d} over {%d}" % (ctr[0], ctr[1])
        lcm_ = ctr[1]
        cals = cals + "`=`{ans_frac2}$$/수식$$\n".format(ans_frac2=ans_frac)

    target_eq = "{n1}`(a`{sign}`b)".format(n1=lcm_, sign=sign)
    ans = ctr[0]
    
    np.random.shuffle(strs)
    number_lists = ""
    for i in range(len(strs)):
        if number_lists == "":
            number_lists = number_lists  + "$$수식$$" + strs[i] + "$$/수식$$"
        else:
            number_lists = number_lists + ", $$수식$$" + strs[i] + "$$/수식$$"

    stem = stem.format(cond1=cond1, cond2=cond2, target_eq=target_eq, number_lists=number_lists)
    answer = answer.format(ans=ans)
    comment = comment.format(equations=equations, ans1_1=ans1_1, ans2_1=ans2_1, eq1=eq1, cals=cals, sign=sign, target_eq=target_eq, ans=ans)

    return stem, answer, comment



# 1-1-2-57
def intandrational112_Stem_033():
    stem = "$$수식$${p1}`{s1}`{p2}`{s2}`{p3}$$/수식$$을 계산한 결과는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${p1}`{s1}`{p2}`{s2}`{p3}`=`{p1_}`{s1}`{p2_}`{s2}`{p3_}$$/수식$$\n"\
        "$$수식$$`=`{ans}$$/수식$$\n\n"
    
    fractions = []
    while len(fractions) < 3:
        fr = frac_gen3(0, 1, [2, 3, 4, 5, 6], 5)
        isfrac = 0
        for i in range(len(fractions)):
            if fractions[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fractions.append(fr)

    sign_idx1 = np.random.randint(0,2)
    sign_idx2 = np.random.randint(0,2)
    s1 = ["+", "-"][sign_idx1]
    s2 = ["+", "-"][sign_idx2]
    
    lcm_ = lcm(fractions[0][0][1], fractions[1][0][1])
    lcm_ = lcm(fractions[2][0][1], lcm_)
    mult = [int(lcm_/fractions[0][0][1]), int(lcm_/fractions[1][0][1]), int(lcm_/fractions[2][0][1])]
    p1_ = "{%d} over {%d}" % (fractions[0][0][0]*mult[0], lcm_)
    p2_ = "{%d} over {%d}" % (fractions[1][0][0]*mult[1], lcm_)
    p3_ = "{%d} over {%d}" % (fractions[2][0][0]*mult[2], lcm_)

    sum11 = frac_sum3(fractions[0], fractions[1])
    sum12 = frac_minus3(fractions[0], fractions[1])

    if sign_idx1 == 0:
        ans1 = sum11
    else:
        ans1 = sum12
    
    sum21 = frac_sum3(fractions[2], ans1)
    sum22 = frac_minus3(fractions[2], ans1)

    if sign_idx2 == 0:
        ans2 = sum21
        ans2_ = sum22
    else:
        ans2 = sum22
        ans2_ = sum21
    
    ex_list = [0, sum11[2], sum12[2], ans2_[2], ans2[2]]

    example_list = make_shuffle_example(ex_list, 4)

    stem = stem.format(p1=fractions[0][2], s1=s1, p2=fractions[1][2], s2=s2, p3=fractions[2][2], \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(p1=fractions[0][2], s1=s1, p2=fractions[1][2], s2=s2, p3=fractions[2][2], p1_=p1_, p2_=p2_, p3_=p3_, ans=ans2[2])

    return stem, answer, comment


# 1-1-2-58
def intandrational112_Stem_034():
    stem = "$$수식$${eq}$$/수식$$을 계산한 결과는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${eq}$$/수식$$\n"\
        "$$수식$$=`{eq1}$$/수식$$\n"\
        "$$수식$$=`(-1 )`+`(-1 )`+`CDOTS`+`(-1 )`=`{ans}$$/수식$$\n\n"
    
    num1 = np.random.randint(0, 26)*2 + 50
    eq = "1`-`2`+`3`-`4`+`CDOTS`+`%d`-`%d" % (num1-1, num1)
    eq1 = "( 1`-`2 )`+`( 3`-`4 )`+`CDOTS`+`( %d`-`%d )" % (num1-1, num1)
    
    ans = -int(num1/2)
    
    base_list = [int(ans/2), -int(ans/2), -ans, num1, -num1, 0]
    base_list.sort()
    ex_list = base_list[0:4]
    ex_list.append(ans)

    example_list = make_shuffle_example(ex_list, 4)

    stem = stem.format(eq=eq, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(eq=eq, eq1=eq1, ans=ans)

    return stem, answer, comment


# 1-1-2-59
def intandrational112_Stem_035():
    stem = "다음 식의 ㉠, ㉡, ㉢에 세 수 $$수식$${p1}$$/수식$$, $$수식$${p2}$$/수식$$, $$수식$${p3}$$/수식$${j} "\
        "한 번씩 넣어 계산한 결과 중 가장 {cond} 값을 $$수식$$a$$/수식$$라 할 때, $$수식$${eq}$$/수식$$의 값을 구하시오.\n"\
        "$$표$$ $$수식$$ ㉠`{s1}`㉡`{s2}`㉢$$/수식$$ $$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
        "계산한 결과가 가장 {cond_} {kodict}에는 세 수 중 가장 {kodict_cond} 수를 넣어야 한다.\n"\
        "이때 $$수식$${equations}$$/수식$$이므로 {kodict}에는 $$수식$${kodict_p}$$/수식$$를 넣으면 되므로 가장 {cond} 값은\n"\
        "$$수식$${ko_p1}`{s1}`{ko_p2}`{s2}`{ko_p3}`=`{p1_}`{s1}`{p2_}`{s2}`{p3_}$$/수식$$\n"\
        "$$수식$$`=`{frac}{equal}{ans}$$/수식$$\n"\
        "따라서 $$수식$$a`=`{ans}$$/수식$$이므로 $$수식$${eq}`=`{a1}$$/수식$$\n\n"
    
    # ㉠, ㉡, ㉢
    box1 = "BOX{~~㉠~~}"
    box2 = "BOX{~~㉡~~}"
    box3 = "BOX{~~㉢~~}"
    
    cond_idx = np.random.randint(0,2)
    cond = ["큰", "작은"][cond_idx]
    cond_ = ["크려면", "작으려면"][cond_idx]
    kodict_cond = ["작은", "큰"][cond_idx]
    kodict_idx = [0, 2][cond_idx]
    oth_idxs = [[1, 2], [0, 1]][cond_idx]

    sign_idx1 = np.random.randint(0,2)
    sign_idx2 = 1-sign_idx1
    s1 = ["+", "-"][sign_idx1]
    s2 = ["+", "-"][sign_idx2]
    kodict = ["㉡", "㉢"][sign_idx2]
    

    fractions = []
    while len(fractions) < 3:
        fr = frac_gen3(1, 1, [2, 3, 4, 5, 6], 5)
        isfrac = 0
        for i in range(len(fractions)):
            if fractions[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fractions.append(fr)

    p1 = fractions[0][2]
    p2 = fractions[1][2]
    p3 = fractions[2][2]
    j = proc_jo(fractions[2][0][1],4)

    fractions.sort(key = lambda ele: ele[1])
    equations = ""
    for i in range(3):
        if equations == "":
            equations = equations + fractions[i][2]
        else:
            equations = equations + "`&lt;`" + fractions[i][2]

    kodict_p = fractions[kodict_idx][2]
    if sign_idx2 == 0:
        p_1 = fractions[oth_idxs[0]]
        p_2 = fractions[kodict_idx]
        p_3 = fractions[oth_idxs[1]]

        ko_p2 = p_2[2]
        ko_p1 = p_1[2]
        ko_p3 = p_3[2]

        lcm_ = lcm(fractions[0][0][1], fractions[1][0][1])
        lcm_ = lcm(fractions[2][0][1], lcm_)
        mult = [int(lcm_/p_1[0][1]), int(lcm_/p_2[0][1]), int(lcm_/p_3[0][1])]

        p1_ = print_frac3(p_1[0][0]*mult[0], lcm_)
        p2_ = print_frac3(p_2[0][0]*mult[1], lcm_)
        p3_ = print_frac3(p_3[0][0]*mult[2], lcm_)

        ctr = ctr_frac(p_1[0][0]*mult[0]-p_2[0][0]*mult[1]+p_3[0][0]*mult[2], lcm_)
        if ctr[0] == -1:
            frac = ""
            equal = ""
            ans = print_frac3(p_1[0][0]*mult[0]-p_2[0][0]*mult[1]+p_3[0][0]*mult[2], lcm_)
            ctr[0] = p_1[0][0]*mult[0]-p_2[0][0]*mult[1]+p_3[0][0]*mult[2]
        else:
            equal = "`=`"
            frac = print_frac3(p_1[0][0]*mult[0]-p_2[0][0]*mult[1]+p_3[0][0]*mult[2], lcm_)
            ans = print_frac3(ctr[0], ctr[1])
            lcm_ = ctr[1]
    else:
        p_1 = fractions[oth_idxs[0]]
        p_3 = fractions[kodict_idx]
        p_2 = fractions[oth_idxs[1]]

        ko_p2 = p_2[2]
        ko_p1 = p_1[2]
        ko_p3 = p_3[2]

        lcm_ = lcm(fractions[0][0][1], fractions[1][0][1])
        lcm_ = lcm(fractions[2][0][1], lcm_)
        mult = [int(lcm_/p_1[0][1]), int(lcm_/p_2[0][1]), int(lcm_/p_3[0][1])]

        p1_ = print_frac3(p_1[0][0]*mult[0], lcm_)
        p2_ = print_frac3(p_2[0][0]*mult[1], lcm_)
        p3_ = print_frac3(p_3[0][0]*mult[2], lcm_)

        ctr = ctr_frac(p_1[0][0]*mult[0]+p_2[0][0]*mult[1]-p_3[0][0]*mult[2], lcm_)
        if ctr[0] == -1:
            frac = ""
            equal = ""
            ans = print_frac3(p_1[0][0]*mult[0]+p_2[0][0]*mult[1]-p_3[0][0]*mult[2], lcm_)
            ctr[0] = p_1[0][0]*mult[0]+p_2[0][0]*mult[1]-p_3[0][0]*mult[2]
        else:
            equal = "`=`"
            frac = print_frac3(p_1[0][0]*mult[0]+p_2[0][0]*mult[1]-p_3[0][0]*mult[2], lcm_)
            ans = print_frac3(ctr[0], ctr[1])
            lcm_ = ctr[1]

    eq = "{%d}a" % (lcm_)
    a1 = ctr[0]
    
    stem = stem.format(p1=p1, s1=s1, p2=p2, s2=s2, p3=p3, j=j, eq=eq, cond=cond, box1=box1, box2=box2, box3=box3)
    answer = answer.format(a1=a1)
    comment = comment.format(ko_p1=ko_p1, s1=s1, ko_p2=ko_p2, s2=s2, ko_p3=ko_p3, p1_=p1_, p2_=p2_, p3_=p3_, equations=equations, \
        cond_=cond_, kodict=kodict, kodict_cond=kodict_cond, kodict_p=kodict_p, eq=eq, cond=cond, frac=frac, equal=equal, ans=ans, a1=a1)

    return stem, answer, comment


# 1-1-2-60
def intandrational112_Stem_036():
    stem = "두 수 $$수식$$rmA$$/수식$$, $$수식$$rmB$$/수식$$가 다음과 같을 때, $$수식$${num1}( rmA`{sign}`rmB )$$/수식$$의 값을 구하시오.\n"\
        "$$표$$ $$수식$$rmA$$/수식$$는 $$수식$${p1}$$/수식$$보다 $$수식$${p2}$$/수식$$만큼 {cond1} 수이다.\n"\
        "$$수식$$rmB$$/수식$$는 $$수식$${p3}$$/수식$$보다 $$수식$${p4}$$/수식$$만큼 {cond2} 수이다. $$/표$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
        "$$수식$$rmA`=`{p1}`{s1}`{p2}`=`{p1_}`{s1}`{p2_}$$/수식$$\n$$수식$$`=`{fr1}{eq1}{ansa}$$/수식$$\n"\
        "$$수식$$rmB`=`{p3}`{s2}`{p4}`=`{p3_}`{s2}`{p4_}$$/수식$$\n$$수식$$`=`{fr2}{eq2}{ansb}$$/수식$$\n"\
        "$$수식$$THEREFORE```rmA`{sign}`rmB`=`{ansa}`{sign}`{ansb}$$/수식$$\n$$수식$$`=`{ansa_}`{sign}`{ansb_}`=`{fr}{eq}{ans}$$/수식$$\n"\
        "$$수식$$THEREFORE```{num1}( rmA`{sign}`rmB )`=`{a1}$$/수식$$\n\n"

    
    cond_idx1 = np.random.randint(0,2)
    cond_idx2 = 1 - cond_idx1
    cond1 = ["큰", "작은"][cond_idx1]
    cond2 = ["큰", "작은"][cond_idx2]
    s1 = ["+", "-"][cond_idx1]
    s2 = ["+", "-"][cond_idx2]

    sign_idx = np.random.randint(0,2)
    sign = ["+", "-"][sign_idx]

    fractions = []
    while len(fractions) < 4:
        fr = frac_gen3(1, 1, [2, 3, 4, 5, 6], 5)
        isfrac = 0
        for i in range(len(fractions)):
            if fractions[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fractions.append(fr)

    p1 = fractions[0][2]
    p2 = fractions[1][2]
    p3 = fractions[2][2]
    p4 = fractions[3][2]

    lcm1 = lcm(fractions[0][0][1], fractions[1][0][1])
    mult = [int(lcm1/fractions[0][0][1]), int(lcm1/fractions[1][0][1])]
    p1_ = print_frac3(fractions[0][0][0]*mult[0], lcm1)
    p2_ = print_frac3(fractions[1][0][0]*mult[1], lcm1)

    if cond_idx1 == 0:
        a_hi = fractions[0][0][0]*mult[0] + fractions[1][0][0]*mult[1]
    else:
        a_hi = fractions[0][0][0]*mult[0] - fractions[1][0][0]*mult[1]

    ctr1 = ctr_frac(a_hi, lcm1)
    if ctr1[0] == -1:
        fr1 = ""
        eq1 = ""
        ansa = print_frac3(a_hi, lcm1)
        ctr1[0] = a_hi
        ctr1[1] = lcm1
    else:
        eq1 = "`=`"
        fr1 = print_frac3(a_hi, lcm1)
        ansa = print_frac3(ctr1[0], ctr1[1])
        lcm1 = ctr1[1]

    lcm2 = lcm(fractions[2][0][1], fractions[3][0][1])
    mult = [int(lcm2/fractions[2][0][1]), int(lcm2/fractions[3][0][1])]
    p3_ = print_frac3(fractions[2][0][0]*mult[0], lcm2)
    p4_ = print_frac3(fractions[3][0][0]*mult[1], lcm2)

    if cond_idx2 == 0:
        b_hi = fractions[2][0][0]*mult[0] + fractions[3][0][0]*mult[1]
    else:
        b_hi = fractions[2][0][0]*mult[0] - fractions[3][0][0]*mult[1]

    ctr2 = ctr_frac(b_hi, lcm2)
    if ctr2[0] == -1:
        fr2 = ""
        eq2 = ""
        ansb = print_frac3(b_hi, lcm2)
        ctr2[0] = b_hi
        ctr2[1] = lcm2
    else:
        eq2 = "`=`"
        fr2 = print_frac3(b_hi, lcm2)
        ansb = print_frac3(ctr2[0], ctr2[1])
        lcm2 = ctr2[1]
    
    lcm3 = lcm(lcm1, lcm2)
    mult = [int(lcm3/lcm1), int(lcm3/lcm2)]
    ansa_ = print_frac3(ctr1[0]*mult[0], lcm3)
    ansb_ = print_frac3(ctr2[0]*mult[1], lcm3)

    if sign_idx == 0:
        hi = ctr1[0]*mult[0] + ctr2[0]*mult[1]
    else:
        hi = ctr1[0]*mult[0] - ctr2[0]*mult[1]

    ctr3 = ctr_frac(hi, lcm3)
    if ctr3[0] == -1:
        fr = ""
        eq = ""
        ans = print_frac3(hi, lcm3)
        ctr3[0] = hi
        ctr3[1] = lcm3
    else:
        eq = "`=`"
        fr = print_frac3(hi, lcm3)
        ans = print_frac3(ctr3[0], ctr3[1])
        lcm3 = ctr3[1]
    
    num1 = lcm3
    if num1 == 1:
        num1 = ""
    a1 = ctr3[0]

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, num1=num1, cond1=cond1, cond2=cond2, sign=sign)
    answer = answer.format(a1=a1)
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, s1=s1, s2=s2, sign=sign, p1_=p1_, p2_=p2_, p3_=p3_, p4_=p4_, \
        fr1=fr1, eq1=eq1, ansa=ansa, fr2=fr2, eq2=eq2, ansb=ansb, ansa_=ansa_, ansb_=ansb_, num1=num1, fr=fr, eq=eq, ans=ans, a1=a1)

    return stem, answer, comment


# 1-1-2-61
def intandrational112_Stem_037():
    stem = "다음은 {n1}, {n2}, {n3}, {n4}의 {val}{j_v} 비교한 것이다.\n"\
        "$$표$$ (가) {n2}{j2} {n3}보다 $$수식$${p1}`{unit}$$/수식$$ {c1}.\n(나) {n1}{j1} {n2}보다 $$수식$${p2}`{unit}$$/수식$$ {c2}.\n"\
        "(다) {n4}{j4} {n1}보다 $$수식$${p3}`{unit}$$/수식$$ {c3}.\n$$/표$$\n"\
        "$$수식$$4$$/수식$$개의 {n}{j} {val}{j_v2} 높은 것부터 차례대로 나열하시오."
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{n3}의 {val}{j_v} $$수식$$0`{unit}$$/수식$$로 놓고, 각 {n}의 {val}{j_v} 부호 $$수식$$+$$/수식$$ 또는 $$수식$$-$$/수식$$를 사용하여 나타내면\n"\
        "{n2}의 {val} : $$수식$$0`{s1}`( {p1} )`=`{ans1}$$/수식$$\n"\
        "{n1}의 {val} : $$수식$$( {ans1} )`{s2}`( {p2} )`=`{ans2}$$/수식$$\n"\
        "{n4}의 {val} : $$수식$$( {ans2} )`{s3}`( {p3} )`=`{ans3}$$/수식$$\n"\
        "따라서 {val}{j_v2} 높은 것부터 차례대로 나열하면 {ans_list}이다.\n\n"
    
    n_idx = np.random.randint(0,4)
    n = ["산", "나라", "산", "나라"][n_idx]
    j = proc_jo(n, 4)
    val = ["높이", "평균 기온", "기온", "평균 습도"][n_idx]
    j_v = proc_jo(val, 4)
    j_v2 = proc_jo(val, 0)
    unit = ["rmm", "CENTIGRADE", "CENTIGRADE", "%"][n_idx]
    base_ns = [["한라산", "설악산", "지리산", "오대산", "금강산", "매봉산", "소백산", "팔봉산"], ["한국", "중국", "일본", "미국", "영국", "프랑스", "독일"]][n_idx % 2]
    names = random.sample(base_ns, 4)
    n1 = names[0]
    j1 = proc_jo(n1, -1)
    n2 = names[1]
    j2 = proc_jo(n2, -1)
    n3 = names[2]
    n4 = names[3]
    j4 = proc_jo(n4, -1)

    base_nums = [list(range(30,300)), list(range(5,20)), list(range(5,20)), list(range(5,40))][n_idx]
    nums = random.sample(base_nums, 4)
    nums = random_minustmp(nums)
    p1 = nums[0]
    p2 = nums[1]
    p3 = nums[2]

    s1_idx = np.random.randint(0,2)
    s2_idx = np.random.randint(0,2)
    s3_idx = np.random.randint(0,2)

    s1 = ["+", "-"][s1_idx]
    s2 = ["+", "-"][s2_idx]
    s3 = ["+", "-"][s3_idx]
    c1 = ["높다", "낮다"][s1_idx]
    c2 = ["높다", "낮다"][s2_idx]
    c3 = ["높다", "낮다"][s3_idx]

    target_idx = 1
    target = ["값들의 합은", "개수는"][target_idx]
    target_ans = ["$$수식$${sums}`=`{ans}$$/수식$$이다.", "$$수식$${ans}$$/수식$$이다."][target_idx]

    if s1_idx == 0:
        ans1 = p1
    else:
        ans1 = -p1

    if s2_idx == 0:
        ans2 = ans1 + p2
    else:
        ans2 = ans1 - p2

    if s3_idx == 0:
        ans3 = ans2 + p3
    else:
        ans3 = ans2 - p3

    answers = [(0, ans2), (1, ans1), (2, 0), (3, ans3)]
    answers.sort(key= lambda ele: ele[1])

    ans_list = ""
    for i in range(4):
        if ans_list == "":
            ans_list = ans_list + names[answers[i][0]]
        else:
            ans_list = ans_list + ", " + names[answers[i][0]]

    stem = stem.format(n1=n1, n2=n2, n3=n3, n4=n4, val=val, j_v=j_v, j_v2=j_v2, j2=j2, j1=j1, j4=j4, \
        p1=p1, p2=p2, p3=p3, c1=c1, c2=c2, c3=c3, unit=unit, n=n, j=j)
    answer = answer.format(a1=ans_list)
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, val=val, j_v=j_v, j_v2=j_v2, unit=unit, n=n, s1=s1, s2=s2, s3=s3,\
        p1=p1, p2=p2, p3=p3, ans1=ans1, ans2=ans2, ans3=ans3, ans_list=ans_list)

    return stem, answer, comment


# 1-1-2-62
def intandrational112_Stem_038():
    #p2에 왜 상자가 들어가 있니..?
    stem = "$$수식$${box1}$$/수식$$$$수식$$`{s1}`{p1}`=`{p2}`$$/수식$$일 때, $$수식$${box1}$$/수식$$ 안에 알맞은 수를 "\
        "$$수식$$rmA$$/수식$$라 하자. 이때 $$수식$${target}$$/수식$$의 값을 구하시오.\n"
    

    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
        "$$수식$${box1}$$/수식$$$$수식$$`=`{p2}`{s2}`{p1}`=`{p2_}`{s2}`{p1_}$$/수식$$\n"\
        "$$수식$$`=`{fr}{eq}{ans}$$/수식$$\n"\
        "따라서 $$수식$$rmA`=`{ans}$$/수식$$이므로 "\
        "$$수식$${target}`=`{a1}$$/수식$$\n\n"
    

    box1="BOX{~~㉠~~}"
    cond_idx1 = np.random.randint(0,2)
    cond_idx2 = 1 - cond_idx1
    s1 = ["+", "-"][cond_idx1]
    s2 = ["+", "-"][cond_idx2]

    fractions = []
    while len(fractions) < 2:
        fr = frac_gen3(1, 1, [2, 3, 4, 5, 6], 5)
        isfrac = 0
        for i in range(len(fractions)):
            if fractions[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fractions.append(fr)

    p1 = fractions[0][2]
    p2 = fractions[1][2]

    lcm1 = lcm(fractions[0][0][1], fractions[1][0][1])  #1분수의 분모와 2분수 분모의최소 공배수 구해준건가 ->통분?
    mult = [int(lcm1/fractions[0][0][1]), int(lcm1/fractions[1][0][1])]
    p1_ = print_frac3(fractions[0][0][0]*mult[0], lcm1) #최소공배수 곱해준 분수 (계산을 위해 )
    p2_ = print_frac3(fractions[1][0][0]*mult[1], lcm1)

    if cond_idx2 == 0:
        hi = fractions[1][0][0]*mult[1] + fractions[0][0][0]*mult[0]
    else:
        hi = fractions[1][0][0]*mult[1] - fractions[0][0][0]*mult[0]

    ctr1 = ctr_frac(hi, lcm1)
    if ctr1[0] == -1:
        fr = ""
        eq = ""
        ans = print_frac3(hi, lcm1)
        ctr1[0] = hi
        ctr1[1] = lcm1
    else:
        eq = "`=`"
        fr = print_frac3(hi, lcm1)
        ans = print_frac3(ctr1[0], ctr1[1])
        lcm1 = ctr1[1]
    
    target = "{n}rmA".format(n="" if lcm1 == 1 else lcm1)
    a1 = ctr1[0]
    
    if s1 == "-":
        p1 = "("+p1+")"

    stem = stem.format(s1=s1, p1=p1, p2=p2, target=target,box1=box1)
    answer = answer.format(a1=a1)
    comment = comment.format(box1=box1,target=target, p1=p1, p2=p2, s2=s2, p1_=p1_, p2_=p2_, fr=fr, eq=eq, ans=ans, a1=a1)

    return stem, answer, comment


# 1-1-2-64
def intandrational112_Stem_039():
    stem = "어떤 유리수에 $$수식$${p1}$$/수식$$를 {c1} 할 것을 잘못하여 $$수식$${p2}$$/수식$$을 {c2} 그 결과가 "\
        "$$수식$${p3}$$/수식$$이 되었다. 이때 바르게 계산한 값을 $$수식$$rmA$$/수식$$라 할 때, $$수식$${target}$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
        "어떤 유리수를 $$수식$$x$$/수식$$라 하면 $$수식$$x`{s1}`{p2}`=`{p3}$$/수식$$에서\n"\
        "$$수식$$x`=`{p3}`{s2}`{p2}`=`{p3_}`{s2}`{p2_}`=`{fr1}{eq1}{ans1}$$/수식$$\n"\
        "따라서 바르게 계산한 값은\n"\
        "$$수식$${ans1}`{s1}`{p1}`=`{ans1_}`{s1}`{p1_}`=`{fr}{eq}{ans}$$/수식$$이므로\n"\
        "$$수식$$rmA`=`{ans}$$/수식$$,   $$수식$$THEREFORE```{target}`=`{a1}$$/수식$$\n\n"
    
    cond_idx1 = np.random.randint(0,2)
    cond_idx2 = 1 - cond_idx1
    c1 = ["더해야", "빼야"][cond_idx1]
    c2 = ["더했더니", "뺐더니"][cond_idx1]
    s1 = ["+", "-"][cond_idx1]
    s2 = ["+", "-"][cond_idx2]

    fractions = []
    while len(fractions) < 3:
        fr = frac_gen3(1, 1, [2, 3, 4, 5, 6], 5)
        isfrac = 0
        for i in range(len(fractions)):
            if fractions[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fractions.append(fr)

    p1 = fractions[0][2]
    p2 = fractions[1][2]
    p3 = fractions[2][2]

    lcm1 = lcm(fractions[1][0][1], fractions[2][0][1])
    mult = [int(lcm1/fractions[1][0][1]), int(lcm1/fractions[2][0][1])]
    p2_ = print_frac3(fractions[1][0][0]*mult[0], lcm1)
    p3_ = print_frac3(fractions[2][0][0]*mult[1], lcm1)

    if cond_idx2 == 0:
        a_hi = fractions[2][0][0]*mult[1] + fractions[1][0][0]*mult[0]
    else:
        a_hi = fractions[2][0][0]*mult[1] - fractions[1][0][0]*mult[0]

    ctr1 = ctr_frac(a_hi, lcm1)
    if ctr1[0] == -1:
        fr1 = ""
        eq1 = ""
        ans1 = print_frac3(a_hi, lcm1)
        ctr1[0] = a_hi
        ctr1[1] = lcm1
    else:
        eq1 = "`=`"
        fr1 = print_frac3(a_hi, lcm1)
        ans1 = print_frac3(ctr1[0], ctr1[1])
        lcm1 = ctr1[1]

    ctr1[0], ctr1[1]

    lcm2 = lcm(ctr1[1], fractions[0][0][1])
    mult = [int(lcm2/ctr1[1]), int(lcm2/fractions[0][0][1])]
    ans1_ = print_frac3(ctr1[0]*mult[0], lcm2)
    p1_ = print_frac3(fractions[0][0][0]*mult[1], lcm2)

    if cond_idx1 == 0:
        b_hi = ctr1[0]*mult[0] + fractions[0][0][0]*mult[1]
    else:
        b_hi = ctr1[0]*mult[0] - fractions[0][0][0]*mult[1]

    ctr2 = ctr_frac(b_hi, lcm2)
    if ctr2[0] == -1:
        fr = ""
        eq = ""
        ans = print_frac3(b_hi, lcm2)
        ctr2[0] = b_hi
        ctr2[1] = lcm2
    else:
        eq = "`=`"
        fr = print_frac3(b_hi, lcm2)
        ans = print_frac3(ctr2[0], ctr2[1])
        lcm2 = ctr2[1]
    
    target = "{n1}rmA".format(n1="" if lcm2 == 1 else lcm2)
    a1 = ctr2[0]

    stem = stem.format(p1=p1, p2=p2, p3=p3, c1=c1, c2=c2, target=target)
    answer = answer.format(a1=a1)
    comment = comment.format(p1=p1, p2=p2, p3=p3, s1=s1, s2=s2, p1_=p1_, p2_=p2_, p3_=p3_, \
        fr1=fr1, eq1=eq1, ans1=ans1, ans1_=ans1_, fr=fr, eq=eq, ans=ans, target=target, a1=a1)

    return stem, answer, comment


# 1-1-2-67
def intandrational112_Stem_040():
    stem = "{f}{j} 만족시키는 정수 $$수식$$x$$/수식$$의 {target}?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{f}{j} 만족시키는 정수는 {num_lists}이므로 {target}\n$$수식$${sums}{equal}{ans}$$/수식$$이다.\n\n"
    
    target_idx = np.random.randint(0,2)
    target = ["값들의 합은", "개수는"][target_idx]

    nums = random.sample(list(range(10)), 2)
    minus = np.random.randint(0,2)
    if minus == 0:
        num1 = -nums[0]
        num2 = nums[1]
    else:
        while abs(nums[0]-nums[1]) == 1:
            nums = random.sample(list(range(10)), 2)
        nums.sort()
        num1 = nums[0]
        num2 = nums[1]
    j = proc_jo(num2, 4)

    c = ["&lt;", "LEQ"]

    rf1 = np.random.randint(0,2)
    rf2 = np.random.randint(0,2)

    f = "$$수식$${num1}`{ineq1}`a`{ineq2}`{num2}$$/수식$$".format(num1=num1, num2=num2, ineq1=c[rf1], ineq2=c[rf2])

    if minus == 0:
        low = num1 + 1 - rf1
        cnt1 = abs(num1) - 1 + rf1
        cnt2 = num2 - 1 + rf2
        ans1 = cnt1 + cnt2 + 1
    else:
        low = num1 + 1 - rf1
        cnt1 = num1 - rf1
        cnt2 = num2 - 1 + rf2
        ans1 = cnt2 - cnt1

    ans = 0
    num_lists = ""
    sums = ""
    equal = "`=`"
    for i in range(ans1):
        if num_lists == "":
            num_lists = num_lists + "$$수식$$" + str(low+i) + "$$/수식$$"
            sums = sums + str(low+i)
        else:
            num_lists = num_lists + ", $$수식$$" + str(low+i) + "$$/수식$$"
            sums = sums + "`+`" + str(low+i)
        ans = ans + low+i

    if target_idx == 1:
        ans = ans1
        sums = ""
        equal = ""

    example_list = make_example(ans)

    stem = stem.format(f=f, j=j, target=target, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(f=f, j=j, target=target, num_lists=num_lists, equal=equal, sums=sums, ans=ans)

    return stem, answer, comment


# 1-1-2-70
def intandrational112_Stem_041():
    stem = "$$수식$${p1}$$/수식$$보다 $$수식$${p2}$$/수식$$만큼 {cond1} 수를 $$수식$$a$$/수식$$, "\
        "$$수식$${p3}$$/수식$$보다 $$수식$${p4}$$/수식$$만큼 {cond2} 수를 $$수식$$b$$/수식$$라 할 때, "\
        "$$수식$${min_c}`{ineq1}`x`{ineq2}`{max_c}$$/수식$$를 만족시키는 정수 $$수식$$x$$/수식$$ {target}?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$a`=`{p1}`{s1}`{p2}`=`{p1_}`{s1}`{p2_}`=`{fr1}{eq1}{ansa}$$/수식$$\n"\
        "$$수식$$b`=`{p3}`{s2}`{p4}`=`{p3_}`{s2}`{p4_}`=`{fr2}{eq2}{ansb}$$/수식$$\n"\
        "따라서 $$수식$${min}`{ineq1}`x`{ineq2}`{max}$$/수식$$을 만족시키는 정수 $$수식$$x$$/수식$$는"\
        "{num_lists}므로 {target}\n$$수식$${sums}{equal}{ans}$$/수식$$이다.\n\n"

    
    cond_idx1 = np.random.randint(0,2)
    cond_idx2 = 1 - cond_idx1
    cond1 = ["큰", "작은"][cond_idx1]
    cond2 = ["큰", "작은"][cond_idx2]
    s1 = ["+", "-"][cond_idx1]
    s2 = ["+", "-"][cond_idx2]

    fractions = []
    while len(fractions) < 4:
        fr = frac_gen3(1, 1, [2, 3, 4, 5, 6], 5)
        isfrac = 0
        if len(fractions) == 1:
            if fractions[0][0][1] == fr[0][1]:
                    isfrac = 1
        if len(fractions) == 3:
            if fractions[2][0][1] == fr[0][1]:
                    isfrac = 1
        if isfrac == 0:
            fractions.append(fr)

    p1 = fractions[0][2]
    p2 = fractions[1][2]
    p3 = fractions[2][2]
    p4 = fractions[3][2]

    lcm1 = lcm(fractions[0][0][1], fractions[1][0][1])
    mult = [int(lcm1/fractions[0][0][1]), int(lcm1/fractions[1][0][1])]
    p1_ = print_frac3(fractions[0][0][0]*mult[0], lcm1)
    p2_ = print_frac3(fractions[1][0][0]*mult[1], lcm1)

    if cond_idx1 == 0:
        a_hi = fractions[0][0][0]*mult[0] + fractions[1][0][0]*mult[1]
    else:
        a_hi = fractions[0][0][0]*mult[0] - fractions[1][0][0]*mult[1]

    ctr1 = ctr_frac(a_hi, lcm1)
    if ctr1[0] == -1:
        fr1 = ""
        eq1 = ""
        ansa = print_frac3(a_hi, lcm1)
        ctr1[0] = a_hi
        ctr1[1] = lcm1
    else:
        eq1 = "`=`"
        fr1 = print_frac3(a_hi, lcm1)
        ansa = print_frac3(ctr1[0], ctr1[1])
        lcm1 = ctr1[1]

    lcm2 = lcm(fractions[2][0][1], fractions[3][0][1])
    mult = [int(lcm2/fractions[2][0][1]), int(lcm2/fractions[3][0][1])]
    p3_ = print_frac3(fractions[2][0][0]*mult[0], lcm2)
    p4_ = print_frac3(fractions[3][0][0]*mult[1], lcm2)

    if cond_idx2 == 0:
        b_hi = fractions[2][0][0]*mult[0] + fractions[3][0][0]*mult[1]
    else:
        b_hi = fractions[2][0][0]*mult[0] - fractions[3][0][0]*mult[1]

    ctr2 = ctr_frac(b_hi, lcm2)
    if ctr2[0] == -1:
        fr2 = ""
        eq2 = ""
        ansb = print_frac3(b_hi, lcm2)
        ctr2[0] = b_hi
        ctr2[1] = lcm2
    else:
        eq2 = "`=`"
        fr2 = print_frac3(b_hi, lcm2)
        ansb = print_frac3(ctr2[0], ctr2[1])
        lcm2 = ctr2[1]

    answers = [(0, ctr1[0]/ctr1[1], ansa), (1, ctr2[0]/ctr2[1], ansb)]
    answers.sort(key= lambda ele: ele[1])

    min_ = answers[0][2]
    min_c = ["a", "b"][answers[0][0]]
    max_ = answers[1][2]
    max_c = ["a", "b"][answers[1][0]]

    target_idx = np.random.randint(0,2)
    target = ["값들의 합은", "개수는"][target_idx]
    num1 = int(answers[0][1])
    num2 = int(answers[1][1])

    rf1 = np.random.randint(0,2)
    rf2 = np.random.randint(0,2)
    c = ["&lt;", "LEQ"]
    ineq1=c[rf1]
    ineq2=c[rf2]

    low = num1
    ans1 = num2 - num1 + 1 
    if num1 == num2:
        if num1 == 0 and answers[0][1]*answers[1][1] < 0:
            ans1 = 1
        else:
            ans1 = 0

    ans = 0
    num_lists = ""
    sums = ""
    equal = "`=`"
    for i in range(ans1):
        if num_lists == "":
            num_lists = num_lists + "$$수식$$" + str(low+i) + "$$/수식$$"
            sums = sums + str(low+i)
        else:
            num_lists = num_lists + ", $$수식$$" + str(low+i) + "$$/수식$$"
            sums = sums + "`+`" + str(low+i)
        ans = ans + low+i
    num_lists = num_lists + "이"

    if ans1 == 0:
        num_lists = " 없으"
        target = "개수는"
        ans = 0
        equal = ""
        sums = ""

    if target_idx == 1:
        ans = ans1
        sums = ""
        equal = ""

    example_list = make_example(ans)

    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, num1=num1, cond1=cond1, cond2=cond2, min=min_, ineq1=ineq1, ineq2=ineq2, max=max_, target=target, \
        min_c=min_c, max_c=max_c, ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(p1=p1, p2=p2, p3=p3, p4=p4, s1=s1, s2=s2, p1_=p1_, p2_=p2_, p3_=p3_, p4_=p4_, \
        fr1=fr1, eq1=eq1, ansa=ansa, fr2=fr2, eq2=eq2, ansb=ansb, min=min_, ineq1=ineq1, ineq2=ineq2, max=max_, target=target, num_lists=num_lists, equal=equal, sums=sums, ans=ans)

    return stem, answer, comment


# 1-1-2-71
def intandrational112_Stem_042():
    stem = "어떤 정수에 $$수식$${n1}$$/수식$$를 더하면 {r1} 정수가 되고, $$수식$${n2}$$/수식$$를 더하면 "\
        "{r2} 정수가 될 때, 어떤 정수를 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
        "어떤 정수를 x라 하면 $$수식$$x`+`{n1}`{ineq1}`0$$/수식$$이므로 "\
        "$$수식$$x$$/수식$$는 $$수식$${n1_}$$/수식$$보다 {c1} 정수이다.\n"\
        "즉, $$수식$$x`=`$$/수식$${num_list1} $$수식$$CDOTS`$$/수식$$㉠\n"\
        "또 $$수식$$x~~`+`{n2}`{ineq2}`0$$/수식$$이므로 $$수식$$x$$/수식$$는 $$수식$${n2_}$$/수식$$보다 {c2} 정수이다.\n"\
        "즉, $$수식$$x~~`=`$$/수식$${num_list2} $$수식$$CDOTS`$$/수식$$㉡\n"\
        "㉠, ㉡에서 $$수식$$x`=`{ans}$$/수식$$\n\n"
    
    # &gt; > &lt; <
    # ㉠ ㉡
    # rf == 0 : n2 = n1 + 1
    rf = np.random.randint(0,2)
    n1 = random.sample([-4,-3,-1,1,3,4,5,6,7], 1)[0]
    n1_ = -n1
    n2 = n1 + (-2*rf + 1)*2
    n2_ = -n2

    r1 = ["양의", "음의"][1-rf]
    r2 = ["양의", "음의"][rf]
    ineq1 = ["&gt;", "&lt;"][1-rf]
    ineq2 = ["&gt;", "&lt;"][rf]
    c1 = ["큰", "작은"][1-rf]
    c2 = ["큰", "작은"][rf]

    f_plus = -2*(1-rf) + 1
    num_list1 = "$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$CDOTS$$/수식$$" % (n1_ + f_plus, n1_ + f_plus*2, n1_ + f_plus*3)

    f2_plus = -2*(rf) + 1
    num_list2 = "$$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$%d$$/수식$$, $$수식$$CDOTS$$/수식$$" % (n2_ + f2_plus, n2_ + f2_plus*2, n2_ + f2_plus*3)

    ans = n2_ + f2_plus

    stem = stem.format(n1=n1, n2=n2, r1=r1, r2=r2)
    answer = answer.format(a1=ans)
    comment = comment.format(n1=n1, n2=n2, n1_=n1_, n2_=n2_, ineq1=ineq1, ineq2=ineq2, \
        c1=c1, c2=c2, num_list1=num_list1, num_list2=num_list2, ans=ans)

    return stem, answer, comment


# 1-1-2-75
def intandrational112_Stem_043():
    stem = "$$수식$${p1}`{s1}`{p2}`{s2}`{p3}$$/수식$$을 계산한 결과는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${p1}`{s1}`{p2}`{s2}`{p3}`=`{sign}( {p1_}`{s1}`{p2_}`{s2}`{p3_} )$$/수식$$\n"\
        "$$수식$$`=`{ans}$$/수식$$\n\n"
    
    fractions = []
    while len(fractions) < 3:
        fr = frac_gen3(1, 1, [2, 3, 4, 5, 6], 5)
        isfrac = 0
        for i in range(len(fractions)):
            if fractions[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fractions.append(fr)

    p1 = fractions[0][2]
    p2 = fractions[1][2]
    p3 = fractions[2][2]

    sign_idx1 = np.random.randint(0,2)
    sign_idx2 = np.random.randint(0,2)
    s1 = ["TIMES", "DIV"][sign_idx1]
    s2 = ["TIMES", "DIV"][sign_idx2]
    
    p1_ = "{%d} over {%d}" % (abs(fractions[0][0][0]), fractions[0][0][1])
    p2_ = "{%d} over {%d}" % (abs(fractions[1][0][0]), fractions[1][0][1])
    p3_ = "{%d} over {%d}" % (abs(fractions[2][0][0]), fractions[2][0][1])
    
    if fractions[0][1] * fractions[1][1] * fractions[2][1] < 0:
        sign = "-"
    else:
        sign = "+"

    hi = fractions[0][0][0]
    lo = fractions[0][0][1]

    if sign_idx1 == 0:
        hi = hi * fractions[1][0][0]
        lo = lo * fractions[1][0][1]
    else:
        hi = hi * fractions[1][0][1]
        lo = lo * fractions[1][0][0]
    
    if sign_idx2 == 0:
        hi = hi * fractions[2][0][0]
        lo = lo * fractions[2][0][1]
    else:
        hi = hi * fractions[2][0][1]
        lo = lo * fractions[2][0][0]

    ctr = ctr_frac2(hi, lo)
    ans = print_ans(ctr[0], ctr[1])

    example_list = make_fraction_example2(ctr[0], ctr[1])

    stem = stem.format(p1=p1, s1=s1, p2=p2, s2=s2, p3=p3, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(p1=p1, s1=s1, p2=p2, s2=s2, sign=sign, p3=p3, p1_=p1_, p2_=p2_, p3_=p3_, ans=ans)

    return stem, answer, comment


# 1-1-2-78
def intandrational112_Stem_044():
    stem = "$$수식$${eq}$$/수식$$을 계산한 결과는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${eq}$$/수식$$\n"\
        "$$수식$$=`{eq1}$$/수식$$\n"\
        "$$수식$$=`{ans}$$/수식$$\n\n"
    
    num1 = np.random.randint(2,5) * 5
    rf = np.random.randint(0,2)
    if rf == 0:
        eq = "( -1 )`+`( -1 )^{n2}`+`( -1 )^{n3}`+`CDOTS`+`( -1 )^{n5}`+`( -1 )^{n6}".format(n2=2, n3=3, n5=num1-1, n6=num1)
        if num1 % 2 == 0:
            last = "{  ( -1 )`+`1}"
            ans = 0
        else:
            last = "( -1 )"
            ans = -1
        eq1 = "{ ( -1 )`+`1}`+`{  ( -1 )`+`1 }`+`CDOTS`+`%s" % (last)
    else:
        eq = "( -1 )^2`+`( -1 )^4`+`( -1 )^6`+`CDOTS`+`( -1 )^{n5}`+`( -1 )^{n6}".format(n5=2*(num1-1), n6=2*num1)
        if num1 % 2 == 0:
            last = "1"
        else:
            last = "1"
        eq1 = "{ 1`+`1 }`+`{ 1`+`1}`+`CDOTS`+`%s" % (last)
        ans = num1
    
    base_list = [ans-1, ans+1, ans+2, ans-2, int(num1/2), -int(num1/2), -num1]
    base_list.sort()
    ex_list = base_list[0:4]
    ex_list.append(ans)

    example_list = make_shuffle_example(ex_list, 4)

    stem = stem.format(eq=eq, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(eq=eq, eq1=eq1, ans=ans)

    return stem, answer, comment


# 1-1-2-79
def intandrational112_Stem_045():
    stem = "$$수식$$a$$/수식$$가 {c1}일 때, 다음 수 중에서 {c2}인 것의 개수는?\n"\
        "$$표$$ {lists} $$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$a$$/수식$$가 {c1}이므로 $$수식$$a`=`{n}$$/수식$$이라 하면\n"\
        "{cases}"\
        "이상에서 {c2}인 것의 개수는 $$수식$${ans}$$/수식$$이다.\n\n"

    num = np.random.randint(4,8)
    bases = [[0,"$$수식$$-a$$/수식$$"], [1,"$$수식$$( -a )^2$$/수식$$"], [2,"$$수식$$-a^2$$/수식$$"], [3,"$$수식$$-(-a )^3$$/수식$$"], [4,"$$수식$$a^3$$/수식$$"], [5,"$$수식$$-a^3$$/수식$$"], [6,"$$수식$$-a^4$$/수식$$"], [7,"$$수식$$a^4$$/수식$$"]]
    bases_s = random.sample(bases, num)
    lists = ""
    for i in range(num):
        if lists == "":
            lists = lists + bases_s[i][1]
        else:
            lists = lists + ", " + bases_s[i][1]
    
    minus_c = ["$$수식$$-a`=`-( -1 )`=`1", "$$수식$$( -a )^2`=`1^2`=`1", "$$수식$$-a^2`=`-( -1 )^2`=`-1", \
        "$$수식$$-(-a )^3`=`-1^3`=`-1", "$$수식$$a^3`=`( -1 )^3`=`-1", "$$수식$$-a^3`=`-( -1 )^3`=`1", \
        "$$수식$$-a^4`=`-( -1 )^4`=`-1", "$$수식$$a^4`=`( -1 )^4`=`1"]
    minus_a = [0, 0, 1, 1, 1, 0, 1, 0]
    plus_c = ["$$수식$$-a`=`-1", "$$수식$$( -a )^2`=`( -1 )^2`=`1", "$$수식$$-a^2`=`-1^2`=`-1", \
        "$$수식$$-(-a )^3`=`-( -1 )^3`=`-( -1 )`=`1", "$$수식$$a^3`=`1^3`=`1", "$$수식$$-a^3`=`-1^3`=`-1", \
        "$$수식$$-a^4`=`-1^4`=`-1", "$$수식$$a^4`=`1^4`=`1"]
    plus_a = [1, 0, 1, 0, 0, 1, 1, 0]

    ind1 = np.random.randint(0,2)
    c1 = ["양수", "음수"][ind1]
    ind2 = np.random.randint(0,2)
    c2 = ["양수", "음수"][ind2]

    cases = ""
    case_f = "({cnt}) {f}`{ineq}`0$$/수식$$\n"
    ans_m = 0
    ans_p = 0
    cnt = 1

    if ind1 == 1:
        n = -1
        for i in range(num):
            idx = bases_s[i][0]
            if minus_a[idx] == 0:
                cases = cases + case_f.format(cnt=cnt, f=minus_c[idx], ineq="&gt;")
                ans_p = ans_p + 1
            else:
                cases = cases + case_f.format(cnt=cnt, f=minus_c[idx], ineq="&lt;")
                ans_m = ans_m + 1
            cnt = cnt + 1
    else:
        n = 1
        for i in range(num):
            idx = bases_s[i][0]
            if plus_a[idx] == 0:
                cases = cases + case_f.format(cnt=cnt, f=plus_c[idx], ineq="&gt;")
                ans_p = ans_p + 1
            else:
                cases = cases + case_f.format(cnt=cnt, f=plus_c[idx], ineq="&lt;")
                ans_m = ans_m + 1
            cnt = cnt + 1
    
    if ind2 == 0:
        ans = ans_p
    else:
        ans = ans_m

    interval = 1
    reverse = np.random.randint(0,2)
    if ans < 4:
        lo = max(4-num+ans, 0)
        ans_index = np.random.randint(lo, ans+1)
    else:
        ans_index = np.random.randint(ans-3, 5)
    
    ex_list = []
    if reverse == 0:
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (i-ans_index)*interval)
    else:
        ans_index = 4 - ans_index
        ex_list.append(ans_index)
        for i in range(5):
            ex_list.append(ans + (ans_index-i)*interval)

    example_list = ex_list

    stem = stem.format(c1=c1, c2=c2, lists=lists, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(c1=c1, c2=c2, n=n, cases=cases, ans=ans)

    return stem, answer, comment


# 1-1-2-80
def intandrational112_Stem_046():
    stem = "$$수식$${eq}$$/수식$$을 계산한 결과는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${eq}$$/수식$$\n"\
        "$$수식$$=`{eq1}$$/수식$$\n"\
        "$$수식$$=`{ans}$$/수식$$\n\n"
    
    num1 = np.random.randint(2,5) * 5
    rf = np.random.randint(0,2)
    if rf == 0:
        eq = "( -{%d} over {%d} )`times`( -{%d} over {%d} )`times`( -{%d} over {%d} )`times`CDOTS`times`( -{%d} over {%d} )" % (1, 3, 3, 5, 5, 7, 2*num1-1, 2*num1+1)
        if num1 % 2 == 0:
            sign = "-"
            ans_frac = [-1, 2*num1+1]
            ans = print_ans(ans_frac[0], ans_frac[1])
        else:
            sign = "+"
            ans_frac = [1, 2*num1+1]
            ans = print_ans(ans_frac[0], ans_frac[1])
        eq1 = "%s( {%d} over {%d}`times`{%d} over {%d}`times`{%d} over {%d}`times`CDOTS`times`{%d} over {%d} )" % (sign, 1, 3, 3, 5, 5, 7, 2*num1-1, 2*num1+1)
    else:
        eq = "( -{%d} over {%d} )`times`( -{%d} over {%d} )`times`( -{%d} over {%d} )`times`CDOTS`times`( -{%d} over {%d} )" % (1, 2, 2, 3, 3, 4, num1-1, num1)
        if num1 % 2 == 0:
            sign = "-"
            ans_frac = [-1, num1]
            ans = print_ans(ans_frac[0], ans_frac[1])
        else:
            sign = "+"
            ans_frac = [1, num1]
            ans = print_ans(ans_frac[0], ans_frac[1])
        eq1 = "%s( {%d} over {%d}`times`{%d} over {%d}`times`{%d} over {%d}`times`CDOTS`times`{%d} over {%d} )" % (sign, 1, 2, 2, 3, 3, 4, num1-1, num1)

    example_list = make_fraction_example2(ans_frac[0], ans_frac[1])

    stem = stem.format(eq=eq, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(eq=eq, eq1=eq1, ans=ans)

    return stem, answer, comment


# 1-1-2-81
def intandrational112_Stem_047():
    stem = "$$수식$${eq}$$/수식$$을 계산한 결과는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$n$$/수식$$이 자연수이므로{odd}{even}\n"\
        "$$수식$$(-1)^{p1}`+`( -1 )^{p2}`=`0$$/수식$$\n"\
        "$$수식$$THEREFORE```{eq}$$/수식$$\n"\
        "$$수식$$=`{eq_}$$/수식$$\n"\
        "$$수식$$=`{eq1}`=`{ans}$$/수식$$\n\n"

    p1 = ["{n}", "{n+2}"][np.random.randint(0,2)]
    p2 = ["{n+1}", "{n-1}"][np.random.randint(0,2)]
    power_list = [[0, p1], [0, p2]]

    rf1 = np.random.randint(0,3)
    rf2 = 2-rf1
    power_even = ["{2n-2}", "{2n}", "{2n+2}"]
    power_odd = ["{2n-1}", "{2n+1}", "{2n+3}"]

    odd_f = " {odd_list}은 홀수이고,"
    even_f = " {even_list}{j} 짝수이고,"
    odd = ""
    even = ""

    if rf1 != 0:
        evens = random.sample(power_even, rf1)
        even_list = ""
        for i in range(rf1):
            if even_list == "":
                even_list = even_list + "$$수식$$" + evens[i] + "$$/수식$$"
            else:
                even_list = even_list + ", $$수식$$" + evens[i] + "$$/수식$$"
            j = proc_jo(evens[i], -1)
            power_list.append([i+1, evens[i]])
        even = even_f.format(even_list=even_list, j=j)
    if rf2 != 0:
        odds = random.sample(power_odd, rf2)
        odd_list = ""
        for i in range(rf2):
            if odd_list == "":
                odd_list = odd_list + "$$수식$$" + odds[i] + "$$/수식$$"
            else:
                odd_list = odd_list + ", $$수식$$" + odds[i] + "$$/수식$$"
            power_list.append([rf1+1+i, odds[i]])
        odd = odd_f.format(odd_list=odd_list)

    ele_f = "{s}`( -1 )^{n}"
    eq_f = "{a1}`{a2}`{a3}`{a4}"

    s_idxs = [np.random.randint(0,2), np.random.randint(0,2), np.random.randint(0,2)]
    s_str = ["+", "-"]
    f_str = ["", "-"]
    s_int = [1, -1]

    if rf1 == 0:
        eq1 = "{s0}0`{s1}`( -1 )`{s2}`( -1 )".format(s0=f_str[s_idxs[0]], s1=s_str[s_idxs[1]], s2=s_str[s_idxs[2]])
        ans = s_int[s_idxs[1]]*(-1) + s_int[s_idxs[2]]*(-1)
    elif rf1 == 1:
        eq1 = "{s0}0`{s1}`1`{s2}`( -1 )".format(s0=f_str[s_idxs[0]], s1=s_str[s_idxs[1]], s2=s_str[s_idxs[2]])
        ans = s_int[s_idxs[1]] + s_int[s_idxs[2]]*(-1)
    else:
        eq1 = "{s0}0`{s1}`1`{s2}`1".format(s0=f_str[s_idxs[0]], s1=s_str[s_idxs[1]], s2=s_str[s_idxs[2]])
        ans = s_int[s_idxs[1]] + s_int[s_idxs[2]]

    ele_list_sort = []
    for i in range(4):
        if i == 0:
            if s_idxs[power_list[i][0]] == 0:
                ele_list_sort.append(ele_f.format(s="", n=power_list[i][1]))
            else:
                ele_list_sort.append(ele_f.format(s="-", n=power_list[i][1]))
        else:
            ele_list_sort.append(ele_f.format(s=s_str[s_idxs[power_list[i][0]]], n=power_list[i][1]))

    random.shuffle(power_list)
    ele_list = []
    for i in range(4):
        if i == 0:
            if s_idxs[power_list[i][0]] == 0:
                ele_list.append(ele_f.format(s="", n=power_list[i][1]))
            else:
                ele_list.append(ele_f.format(s="-", n=power_list[i][1]))
        else:
            ele_list.append(ele_f.format(s=s_str[s_idxs[power_list[i][0]]], n=power_list[i][1]))

    eq = eq_f.format(a1=ele_list[0], a2=ele_list[1], a3=ele_list[2], a4=ele_list[3])
    eq_ = eq_f.format(a1=ele_list_sort[0], a2=ele_list_sort[1], a3=ele_list_sort[2], a4=ele_list_sort[3])
    
    base_list = [ans-3, ans+3, ans-1, ans+1, ans+2, ans-2]
    random.shuffle(base_list)
    ex_list = base_list[0:4]
    ex_list.append(ans)

    #example_list = make_shuffle_example(ex_list, 4)
    example_list = make_example_minus(ans, 0)

    stem = stem.format(eq=eq, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(odd=odd, even=even, p1=p1, p2=p2, eq=eq, eq_=eq_, eq1=eq1, ans=ans)

    return stem, answer, comment


# 1-1-2-82
def intandrational112_Stem_048():
    stem = "$$수식$$n$$/수식$$이 {c1}일 때, $$수식$${eq}$$/수식$$을 계산한 결과는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$n$$/수식$$이 {c1}이므로{odd}{even}\n"\
        "$$수식$$THEREFORE```{eq}$$/수식$$\n"\
        "$$수식$$=`{eq1}`=`{ans}$$/수식$$\n\n"

    powers = ["n", "n`times`2", "n`times`3", "n`times`4"]

    rf = np.random.randint(0,2)
    c1 = ["짝수", "홀수"][rf]

    odd_f = " {odd_list}은 홀수이고,"
    even_f = " {even_list}{j} 짝수이다."
    odd = ""
    even = ""

    if rf == 0:
        even_list = ""
        for i in range(4):
            if even_list == "":
                even_list = even_list + "$$수식$$" + powers[i] + "$$/수식$$"
            else:
                even_list = even_list + ", $$수식$$" + powers[i] + "$$/수식$$"
            j = proc_jo(powers[i], -1)
        even = even_f.format(even_list=even_list, j=j)
    else:
        odd_list = ""
        even_list = ""
        for i in range(2):
            if odd_list == "":
                odd_list = odd_list + "$$수식$$" + powers[2*i] + "$$/수식$$"
                even_list = even_list + "$$수식$$" + powers[2*i+1] + "$$/수식$$"
            else:
                odd_list = odd_list + ", $$수식$$" + powers[2*i] + "$$/수식$$"
                even_list = even_list + ", $$수식$$" + powers[2*i+1] + "$$/수식$$"
            j = proc_jo(powers[2*i+1], -1)
        odd = odd_f.format(odd_list=odd_list)
        even = even_f.format(even_list=even_list, j=j)
        
    eq = "( -1 )^{%s}`%s`( -1 )^{%s}`%s`( -1 )^{%s}`%s`( -1 )^{%s}"

    s_idxs = [np.random.randint(0,2), np.random.randint(0,2), np.random.randint(0,2)]
    s_str = ["+", "-"]
    f_str = ["", "-"]
    s_int = [1, -1]

    eq = eq % (powers[0], s_str[s_idxs[0]], powers[1], s_str[s_idxs[1]], powers[2], s_str[s_idxs[2]], powers[3])

    if rf == 1:
        eq1 = "( -1 )`{s1}`1`{s2}`( -1 )`{s3}`1".format(s1=s_str[s_idxs[0]], s2=s_str[s_idxs[1]], s3=s_str[s_idxs[2]])
        ans = -1 + s_int[s_idxs[0]] + s_int[s_idxs[1]]*(-1) + s_int[s_idxs[2]]
    else:
        eq1 = "1`{s1}`1`{s2}`1`{s3}`1".format(s1=s_str[s_idxs[0]], s2=s_str[s_idxs[1]], s3=s_str[s_idxs[2]])
        ans = 1 + s_int[s_idxs[0]] + s_int[s_idxs[1]] + s_int[s_idxs[2]]

    example_list = make_example_minus(ans, 0)

    stem = stem.format(c1=c1, eq=eq, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(c1=c1, odd=odd, even=even, eq=eq, eq1=eq1, ans=ans)

    return stem, answer, comment


# 1-1-2-83
def intandrational112_Stem_049():
    stem = "네 유리수 $$수식$${p1}$$/수식$$, $$수식$${p2}$$/수식$$, $$수식$${p3}$$/수식$$, $$수식$${p4}$$/수식$$ 중에서 "\
        "서로 다른 세 수를 뽑아 곱한 값 중 {cond1} 값을 $$수식$$a$$/수식$$, {cond2} 값을 $$수식$$b$$/수식$$라 할 때, "\
        "$$수식$$a`{s}`b$$/수식$$의 값을 구하시오.\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${equations}$$/수식$$\n"\
        "{cond1} 값은 {cond1_str} $$수식$$a`=`{c11}`times`{c12}`times`{c13}`=`{ansa}$$/수식$$\n"\
        "{cond2} 값은 {cond2_str} $$수식$$b`=`{c21}`times`{c22}`times`{c23}`=`{ansb}$$/수식$$\n"\
        "$$수식$$THEREFORE```a`{s}`b`=`( {ansa} )`{s}`( {ansb} )`=`{ans}$$/수식$$\n\n"
    
    conds = ["가장 큰", "가장 작은", "두번째로 큰", "두번째로 작은"]
    cond_strs = ["두 음수와 절댓값이 큰 양수를 뽑아야 하므로", "두 양수와 절댓값이 큰 음수를 뽑아야 하므로",\
        "두 음수와 절댓값이 작은 양수를 뽑아야 하므로", "두 양수와 절댓값이 작은 음수를 뽑아야 하므로"]
    idxs = [[0,1,3], [0,2,3], [0,1,2], [1,2,3]]
    
    c1_idx = np.random.randint(0,4)
    c2_idx = np.random.randint(0,4)
    cond1 = conds[c1_idx]
    cond1_str = cond_strs[c1_idx]
    idxs1 = idxs[c1_idx]
    cond2 = conds[c2_idx]
    cond2_str = cond_strs[c2_idx]
    idxs2 = idxs[c2_idx]

    fractions = []
    while len(fractions) < 2:
        fr = frac_gen3(-1, 1, [2, 3, 4, 5, 6], 1)
        isfrac = 0
        for i in range(len(fractions)):
            if fractions[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fractions.append(fr)
    
    while len(fractions) < 4:
        fr = frac_gen3(0, 1, [2, 3, 4, 5, 6], 1)
        isfrac = 0
        for i in range(len(fractions)):
            if fractions[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fractions.append(fr)

    p1 = fractions[0][2]
    p2 = fractions[1][2]
    p3 = fractions[2][2]
    p4 = fractions[3][2]

    fractions.sort(key= lambda ele: abs(ele[1]))
    equations = ""
    for i in range(4):
        if equations == "":
            equations = equations + "| " + fractions[i][2] + " |"
        else:
            equations = equations + "`&lt;`" + "| " + fractions[i][2] + "|"

    fractions.sort(key= lambda ele: ele[1])
    
    c11 = fractions[idxs1[0]][2]
    c12 = fractions[idxs1[1]][2]
    c13 = fractions[idxs1[2]][2]

    hi = fractions[idxs1[0]][0][0]*fractions[idxs1[1]][0][0]*fractions[idxs1[2]][0][0]
    lo = fractions[idxs1[0]][0][1]*fractions[idxs1[1]][0][1]*fractions[idxs1[2]][0][1]
    ctr1 = ctr_frac2(hi, lo)
    ansa = print_ans(ctr1[0], ctr1[1])

    c21 = fractions[idxs2[0]][2]
    c22 = fractions[idxs2[1]][2]
    c23 = fractions[idxs2[2]][2]

    hi = fractions[idxs2[0]][0][0]*fractions[idxs2[1]][0][0]*fractions[idxs2[2]][0][0]
    lo = fractions[idxs2[0]][0][1]*fractions[idxs2[1]][0][1]*fractions[idxs2[2]][0][1]
    ctr2 = ctr_frac2(hi, lo)
    ansb = print_ans(ctr2[0], ctr2[1])

    si_idx = np.random.randint(0,2)
    s = ["+", "-"][si_idx]
    s_int = [1, -1][si_idx]

    ans_frac = sum_frac(ctr1, [ctr2[0]*s_int, ctr2[1]])
    ans = print_ans(ans_frac[0], ans_frac[1])

    example_list = make_fraction_example2(ans_frac[0], ans_frac[1])
    
    stem = stem.format(p1=p1, p2=p2, p3=p3, p4=p4, s=s, cond1=cond1, cond2=cond2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(cond1=cond1, cond2=cond2, cond1_str=cond1_str, cond2_str=cond2_str, equations=equations, \
        c11=c11, c12=c12, c13=c13, c21=c21, c22=c22, c23=c23, s=s, ansa=ansa, ansb=ansb, ans=ans)

    return stem, answer, comment


# 1-1-2-84
def intandrational112_Stem_050():
    stem = "$$수식$$( {n1_str} )`times`{p}`+`( {n2_str} )`times`{p}$$/수식$$을 계산한 결과는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$( {n1_str} )`times`{p}`+`( {n2_str} )`times`{p}`=`( {n1}`{s}`{abs_n2} )`times`{p}$$/수식$$\n"\
        "$$수식$$=`( {n3} )`times`{p}`=`{ans}$$/수식$$\n\n"

    ismin = random.sample([-1, 1], 1)[0]
    n3 = np.random.randint(1,4) * 10 * ismin
    n1 = random.sample([7, 13, 17, 19, 23, 27, 29, 31, 33, 37, 39, 43, 47, 49], 1)[0]
    n2 = n3 - n1

    n1_str = str(n1)
    n2_str = str(n2)
    abs_n2 = abs(n2)
    s = "-"
    if n1 > 0:
        n1_str = "+" + n1_str
    if n2 > 0:
        n2_str = "+" + n2_str
        s = "+"

    p = np.random.randint(1,5) + np.random.randint(1,10)/10
    ans = round(n3 * p)

    example_list = make_example_minus(ans, 0)

    stem = stem.format(n1_str=n1_str, n2_str=n2_str, p=p, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1_str=n1_str, n2_str=n2_str, p=p, n1=n1, n2=n2, n3=n3, abs_n2=abs_n2, s=s, ans=ans)

    return stem, answer, comment


# 1-1-2-85
def intandrational112_Stem_051():
    stem = "세 수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$에 대하여 $$수식$${c1}`times`{c2}`=`{n1}$$/수식$$, "\
        "$$수식$${c1}`times`( {c2}`{s1}`{c3} )`=`{n2}$$/수식$$일 때, $$수식$${c1}`times`{c3}$$/수식$$의 값은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${c1}`times`( {c2}`{s1}`{c3} )`=`{c1}`times`{c2}`{s1}`{c1}`times`{c3}`=`{n1}`{s1}`{c1}`times`{c3}`=`{n2}$$/수식$$이므로\n"\
        "$$수식$${c1}`times`{c3}`=`{ans}$$/수식$$\n\n"

    ch = ["a", "b", "c"]
    random.shuffle(ch)

    c1 = ch[0]
    c2 = ch[1]
    c3 = ch[2]

    s_idx = np.random.randint(0,2)
    s1 = ["+", "-"][s_idx]

    n1 = np.random.randint(1, 20) * random.sample([-1, 1], 1)[0]
    n2 = np.random.randint(1, 20) * random.sample([-1, 1], 1)[0]

    if s_idx == 0:
        ans = n2 - n1
    else:
        ans = n1 - n2

    example_list = make_example_minus(ans, 0)

    stem = stem.format(c1=c1, c2=c2, c3=c3, s1=s1, n1=n1, n2=n2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(c1=c1, c2=c2, c3=c3, s1=s1, n1=n1, n2=n2, ans=ans)

    return stem, answer, comment


# 1-1-2-87
def intandrational112_Stem_052():
    stem = "다음을 만족시키는 두 정수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$a`{s_}`b$$/수식$$의 값은?\n"\
        "$$표$$ $$수식$$ {n1_str} `times`{p}`+` {n2_str} `times`{p}$$/수식$$\n"\
        "$$수식$$`=`a`times`{p}`=`b$$/수식$$ $$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$ {n1_str} `times`{p}`+` {n2_str} `times`{p}`=`( {n1}`{s}`{abs_n2} )`times`{p}$$/수식$$\n"\
        "$$수식$$=` {ansa} `times`{p}`=`{ansb}$$/수식$$\n"\
        "$$수식$$THEREFORE```a`{s_}`b=`{ansa}`{s_}`{ansb_str}`=`{ans}$$/수식$$\n\n"

    ismin = random.sample([-1, 1], 1)[0]
    ansa = np.random.randint(1,4) * 100 * ismin
    n1 = random.sample([23, 27, 29, 31, 33, 37, 39, 43, 47, 49, 53, 57, 63, 67, 73, 79, 83, 87, 97], 1)[0] + np.random.randint(0,2) * 100
    n2 = ansa - n1

    n1_str = str(n1)
    n2_str = str(n2)
    abs_n2 = abs(n2)
    s = "-"
    if n1 > 0:
        n1_str = "" + n1_str
    elif n1<0:
        n1_str="("+n1_str+")"
    if n2 > 0:
        n2_str = "" + n2_str
        s = "+"
    elif n2<0:
        n2_str="("+n2_str+")"

    p = np.random.randint(8, 50)/100
    ansb = round(ansa * p)
    ansb_str = str(ansb)
    if ansb < 0:
        ansb_str = "( " + ansb_str + ")"

    s_idx = np.random.randint(0,2)
    s_ = ["+", "-"][s_idx]
    if s_idx == 0:
        ans = ansa + ansb
    else:
        ans = ansa - ansb

    example_list = make_example_minus(ans, int(ans/10))

    stem = stem.format(n1_str=n1_str, n2_str=n2_str, p=p, s_=s_, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1_str=n1_str, n2_str=n2_str, p=p, n1=n1, n2=n2, abs_n2=abs_n2, \
        s=s, s_=s_, ansa=ansa, ansb=ansb, ansb_str=ansb_str, ans=ans)

    return stem, answer, comment


# 1-1-2-90
def intandrational112_Stem_053():
    stem = "$$수식$${sa}a$$/수식$$의 역수가 $$수식$${n1}$$/수식$$이고, $$수식$${n2}$$/수식$$의 역수가 $$수식$${sb}b$$/수식$$일 때, "\
        "$$수식$$a`{s_}`b$$/수식$$의 값은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${sa}a$$/수식$$의 역수가 $$수식$${n1}$$/수식$$이므로 $$수식$${n1}$$/수식$$의 역수는 $$수식$${sa}a$$/수식$$이다.\n"\
        "즉, {a_str}\n"\
        "$$수식$${n2}`=`{p2}$$/수식$$이므로 {b_str}\n"\
        "$$수식$$THEREFORE```a`{s_}`b=`=`{ans}$$/수식$$\n\n"

    minus_str = "$$수식$$-{c}`=`{n}$$/수식$$이므로 $$수식$${c}`=`{n_}$$/수식$$"
    plus_str = "$$수식$${c}`=`{n}$$/수식$$"

    s_idx = np.random.randint(0,2)
    sa = ["", "-"][s_idx]
    sb = ["", "-"][1-s_idx]

    a_frac = frac_gen3(0, 1, [2, 3, 5, 6, 7], 1)
    n1 = a_frac[2]
    b_frac = frac_gen3(0, 1, [2, 5], 1)
    while a_frac[1] == b_frac[1]:
        b_frac = frac_gen3(0, 1, [2, 5], 2)
    n2 = b_frac[1]
    p2 = b_frac[2]

    if s_idx == 0:
        ansa_f = [a_frac[0][1], a_frac[0][0]]
        ansa = print_ans(a_frac[0][1], a_frac[0][0])
        a_str = plus_str.format(c="a", n=ansa)

        ansb_f = [-b_frac[0][1], b_frac[0][0]]
        ansb_ = print_ans(b_frac[0][1], b_frac[0][0])
        ansb = print_ans(-b_frac[0][1], b_frac[0][0])
        b_str = minus_str.format(c="b", n=ansb_, n_=ansb)
    else:
        ansb_f = [b_frac[0][1], b_frac[0][0]]
        ansb = print_ans(b_frac[0][1], b_frac[0][0])
        b_str = plus_str.format(c="b", n=ansb)

        ansa_f = [-a_frac[0][1], a_frac[0][0]]
        ansa_ = print_ans(a_frac[0][1], a_frac[0][0])
        ansa = print_ans(-a_frac[0][1], a_frac[0][0])
        a_str = minus_str.format(c="a", n=ansa_, n_=ansa)

    s_idx = np.random.randint(0,2)
    s_ = ["+", "-"][s_idx]
    if s_idx == 0:
        ans_f = sum_frac(ansa_f, ansb_f)
    else:
        ans_f = sum_frac(ansa_f, [-ansb_f[0], ansb_f[1]])
    
    ans = print_ans(ans_f[0], ans_f[1])

    example_list = make_fraction_example2(ans_f[0], ans_f[1])

    stem = stem.format(n1=n1, n2=n2, sa=sa, sb=sb, s_=s_, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(sa=sa, n1=n1, n2=n2, p2=p2, a_str=a_str, b_str=b_str, s_=s_, ans=ans)

    return stem, answer, comment


# 1-1-2-91
def intandrational112_Stem_054():
    stem = "다음 중 두 수가 서로 역수 관계인 것은?\n"\
        "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{cases}"\
        "따라서 두 수가 서로 역수 관계인 것은 {dict_}이다.\n\n"

    fs = []
    while len(fs) < 5:
        fr = frac_gen3(1, 1, [2, 3, 4, 5, 6, 10], 1)
        isfrac = 0
        for i in range(len(fs)):
            if fs[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs.append(fr)
    
    # minus, minus_reverse, decimal : 0,1,2
    ans_idx = np.random.randint(0,5)
    ex_list = []
    for i in range(5):
        fr = fs[i]
        origin = "$$수식$$" + print_ans(fr[0][0], fr[0][1]) + "$$/수식$$"
        reverse = "$$수식$$" + print_ans(fr[0][1], fr[0][0]) + "$$/수식$$"
        minus = "$$수식$$" + print_ans(-fr[0][0], fr[0][1]) + "$$/수식$$"
        minus_reverse = "$$수식$$" + print_ans(-fr[0][1], fr[0][0]) + "$$/수식$$"
        decimal = "$$수식$$" + str(round(fr[1], 1)) + "$$/수식$$"

        if i == ans_idx:
            f = origin + ", " + reverse
            c = "RIGHT ANSWER"
        else:
            if fr[0][1] in [2, 5, 10]:
                rf = np.random.randint(0,3)
            else:
                rf = np.random.randint(0,2)
            
            if rf == 0:
                f = origin + ", " + minus
                c = f + "의 역수는 각각 " + reverse + ", " + minus_reverse + "이다.\n"
            elif rf == 1:
                f = origin + ", " + minus_reverse
                c = f + "의 역수는 각각 " + reverse + ", " + minus + "이다.\n"
            elif rf == 2:
                f = origin + ", " + decimal
                c = f + "의 역수는 " + reverse + "이다.\n"
        
        ex_list.append([f, c])

    ans_list = make_shuffle_example(ex_list, ans_idx)
    cases = ""
    for i in range(5):
        if i != ans_list[0]:
            cases = cases + answer_dict[i] + " " + ans_list[i+1][1]
    dict_ = answer_dict[ans_list[0]]

    stem = stem.format(ex1=ans_list[1][0], ex2=ans_list[2][0], ex3=ans_list[3][0], ex4=ans_list[4][0], ex5=ans_list[5][0])
    answer = answer.format(a1=answer_dict[ans_list[0]])
    comment = comment.format(cases=cases, dict_=dict_)

    return stem, answer, comment


# 1-1-2-92
def intandrational112_Stem_055():
    stem = "$$수식$${p1}`{s1}`{p2}`{s2}`{p3}$$/수식$$을 계산한 결과는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${p1}`{s1}`{p2}`{s2}`{p3}`=`{p1}`times`{p2_}`times`{p3_}$$/수식$$\n"\
        "$$수식$$`=`{s}`( {p1_abs}`times`{p2_abs}`times`{p3_abs} )`=`{ans}$$/수식$$\n\n"

    fs = []
    while len(fs) < 3:
        fr = frac_gen3(1, 1, [2, 3, 4, 5, 6, 7], 1)
        isfrac = 0
        for i in range(len(fs)):
            if fs[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs.append(fr)

    p1 = fs[0][2]
    p2 = fs[1][2]
    p3 = fs[2][2]

    minus = 1
    for i in range(3):
        if fs[i][1] < 0:
            minus = minus * (-1)

    
    if minus == -1:
        s = "-"
    else:
        s = "+"

    rf = np.random.randint(0,3)
    sign = ["TIMES", "DIV"]

    if rf == 0:
        s1 = sign[0]
        s2 = sign[1]
        p2_ = p2
        p3_ = print_frac3(fs[2][0][1], fs[2][0][0])

        p1_abs = print_ans(abs(fs[0][0][0]), fs[0][0][1])
        p2_abs = print_ans(abs(fs[1][0][0]), fs[1][0][1])
        p3_abs = print_ans(abs(fs[2][0][1]), abs(fs[2][0][0]))
        
        ctr = ctr_frac2(abs(fs[0][0][0])*abs(fs[1][0][0])*abs(fs[2][0][1]), fs[0][0][1]*fs[1][0][1]*abs(fs[2][0][0]))
        ans_f = [minus*ctr[0], ctr[1]]
    elif rf == 1:
        s1 = sign[1]
        s2 = sign[0]
        p2_ = print_frac3(fs[1][0][1], fs[1][0][0])
        p3_ = p3

        p1_abs = print_ans(abs(fs[0][0][0]), fs[0][0][1])
        p2_abs = print_ans(abs(fs[1][0][1]), abs(fs[1][0][0]))
        p3_abs = print_ans(abs(fs[2][0][0]), fs[2][0][1])

        ctr = ctr_frac2(abs(fs[0][0][0])*abs(fs[1][0][1])*abs(fs[2][0][0]), fs[0][0][1]*abs(fs[1][0][0])*fs[2][0][1])
        ans_f = [minus*ctr[0], ctr[1]]
    elif rf == 2:
        s1 = sign[1]
        s2 = sign[1]
        p2_ = print_frac3(fs[1][0][1], fs[1][0][0])
        p3_ = print_frac3(fs[2][0][1], fs[2][0][0])

        p1_abs = print_ans(abs(fs[0][0][0]), fs[0][0][1])
        p2_abs = print_ans(abs(fs[1][0][1]), abs(fs[1][0][0]))
        p3_abs = print_ans(abs(fs[2][0][1]), abs(fs[2][0][0]))

        ctr = ctr_frac2(abs(fs[0][0][0])*abs(fs[1][0][1])*abs(fs[2][0][1]), fs[0][0][1]*abs(fs[1][0][0])*abs(fs[2][0][0]))
        ans_f = [minus*ctr[0], ctr[1]]

    ans = print_ans(ans_f[0], ans_f[1])
    example_list = make_fraction_example2(ans_f[0], ans_f[1])

    stem = stem.format(p1=p1, p2=p2, p3=p3, s1=s1, s2=s2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(p1=p1, p2=p2, p3=p3, s1=s1, s2=s2, p2_=p2_, p3_=p3_, s=s, p1_abs=p1_abs, p2_abs=p2_abs, p3_abs=p3_abs, ans=ans)

    return stem, answer, comment


# 1-1-2-93
def intandrational112_Stem_056():
    stem = "$$수식$$a`{s1}`{n1}`=`{n2}$$/수식$$, $$수식$$b`{s2}`{n3}`=`{n4}$$/수식$$일 때, "\
        "$$수식$$a`{s}`b$$/수식$$의 값은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$a`=`{n2}`{s1_}`{n1}{eqa}`=`{ansa_a}$$/수식$$\n"\
        "$$수식$$b`=`{n4}`{s2_}`{n3}{eqb}`=`{ansb_a}$$/수식$$\n"\
        "$$수식$$a`{s}`b`=`{ansa}`{s}`{ansb}`=`{ans}$$/수식$$\n\n"

    s_idx = np.random.randint(0,2)
    s1 = ["TIMES", "DIV"][s_idx]
    s2 = ["TIMES", "DIV"][1-s_idx]
    s1_ = ["TIMES", "DIV"][1-s_idx]
    s2_ = ["TIMES", "DIV"][s_idx]

    fs = []
    while len(fs) < 4:
        fr = frac_gen3(1, 1, [2], 5)
        isfrac = 0
        for i in range(len(fs)):
            if fs[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs.append(fr)

    n1 = fs[0][2]
    n2 = print_ans(fs[1][0][0], fs[1][0][1])
    n3 = fs[2][2]
    n4 = print_ans(fs[3][0][0], fs[3][0][1])

    eq_f = "`=`{n}`times`{n_}"
    if s_idx == 1:
        eqa = ""
        ansa_f = [fs[0][0][0]*fs[1][0][0], fs[0][0][1]*fs[1][0][1]]

        n3_ = print_frac3(fs[2][0][1], fs[2][0][0])
        eqb = eq_f.format(n=n4, n_=n3_)
        ansb_f = [fs[2][0][1]*fs[3][0][0], fs[2][0][0]*fs[3][0][1]]
        
    else:
        eqb = ""
        ansb_f = [fs[2][0][0]*fs[3][0][0], fs[2][0][1]*fs[3][0][1]]

        n1_ = print_frac3(fs[0][0][1], fs[0][0][0])
        eqa = eq_f.format(n=n2, n_=n1_)
        ansa_f = [fs[0][0][1]*fs[1][0][0], fs[0][0][0]*fs[1][0][1]]
    
    ansa_f = ctr_frac2(ansa_f[0], ansa_f[1])
    ansa_a = print_ans(ansa_f[0], ansa_f[1])
    ansa = print_frac3(ansa_f[0], ansa_f[1])

    ansb_f = ctr_frac2(ansb_f[0], ansb_f[1])
    ansb_a = print_ans(ansb_f[0], ansb_f[1])
    ansb = print_frac3(ansb_f[0], ansb_f[1])

    rf = np.random.randint(0,2)
    if rf == 0:
        s = "TIMES"
        ans_f = [ansa_f[0]*ansb_f[0], ansa_f[1]*ansb_f[1]]
    else:
        s = "DIV"
        ans_f = [ansa_f[0]*ansb_f[1], ansa_f[1]*ansb_f[0]]

    ans = print_ans(ans_f[0], ans_f[1])
    example_list = make_fraction_example2(ans_f[0], ans_f[1])

    stem = stem.format(n1=n1, n2=n2, n3=n3, n4=n4, s1=s1, s2=s2, s=s, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, n3=n3, n4=n4, s1_=s1_, s2_=s2_, eqa=eqa, eqb=eqb, ansa_a=ansa_a, ansa=ansa, ansb_a=ansb_a, ansb=ansb, s=s, ans=ans)

    return stem, answer, comment

# 1-1-2-94
def intandrational112_Stem_057():
    stem = "다음 중 계산 결과가 옳지 않은 것은?\n"\
        "① {ex1}\n② {ex2}\n③ {ex3}\n④ {ex4}\n⑤ {ex5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{cases}\n\n"
    
    ex_list = []
    ans_idx = np.random.randint(0,5)
    f = "$$수식$${p1}`{s1}`{p2}`{s2}`{p3}`=`{ans}$$/수식$$"
    c = "$$수식$${p1}`{s1}`{p2}`{s2}`{p3}`=`{p1}`times`{p2_}`times`{p3_}`=`{ans}$$/수식$$"
    for idx in range(5):

        int_num = np.random.randint(0,3)

        fs = []
        if int_num != 0:
            ns = random.sample([2, 3, 4, 5, 8, 10, 12, 15, 16, 20], int_num)
            ns = random_minus(ns)
            for i in range(int_num):
                if ns[i] > 0:
                    fs.append([[ns[i], 1], ns[i], " %d " % ns[i]])
                else:
                    fs.append([[ns[i], 1], ns[i], "( %d )" % ns[i]])

        
        while len(fs) < 3:
            fr = frac_gen3(1, 1, [2, 3, 4, 5, 6, 7], 1)
            isfrac = 0
            for i in range(len(fs)):
                if fs[i][1] == fr[1]:
                    isfrac = 1
            if isfrac == 0:
                fs.append(fr)

        p1 = fs[0][2]
        p2 = fs[1][2]
        p3 = fs[2][2]

        minus = 1
        for i in range(3):
            if fs[i][1] < 0:
                minus = minus * (-1)

        rf = np.random.randint(0,3)
        sign = ["TIMES", "DIV"]

        if rf == 0:
            #곱 나누기 
            s1 = sign[0]
            s2 = sign[1]
            
            p2_=p2
           
            p3_ = print_frac3(fs[2][0][1], fs[2][0][0])
            ctr = ctr_frac2(abs(fs[0][0][0])*abs(fs[1][0][0])*abs(fs[2][0][1]), fs[0][0][1]*fs[1][0][1]*abs(fs[2][0][0]))
            ans_f = [minus*ctr[0], ctr[1]]
        elif rf == 1:
            #나누기 곱

            s1 = sign[1]
            s2 = sign[0]
            p2_ = print_frac3(fs[1][0][1], fs[1][0][0])
            p3_ = p3

            ctr = ctr_frac2(abs(fs[0][0][0])*abs(fs[1][0][1])*abs(fs[2][0][0]), fs[0][0][1]*abs(fs[1][0][0])*fs[2][0][1])
            ans_f = [minus*ctr[0], ctr[1]]
        elif rf == 2:
            #나누기 나눈기 
            s1 = sign[1]
            s2 = sign[1]
            p2_ = print_frac3(fs[1][0][1], fs[1][0][0])
            p3_ = print_frac3(fs[2][0][1], fs[2][0][0])

            ctr = ctr_frac2(abs(fs[0][0][0])*abs(fs[1][0][1])*abs(fs[2][0][1]), fs[0][0][1]*abs(fs[1][0][0])*abs(fs[2][0][0]))
            ans_f = [minus*ctr[0], ctr[1]]

        ans = print_ans(ans_f[0], ans_f[1])

        f_ = f.format(p1=p1, p2=p2, p3=p3, s1=s1, s2=s2, ans=ans)
        c_ = "RIGHT"
        if idx == ans_idx:
            ans_ = [print_ans(ans_f[0], ans_f[1]), print_ans(2*ans_f[0], ans_f[1]), print_ans(4*ans_f[0], ans_f[1]), \
                print_ans(ans_f[0], 2*ans_f[1]), print_ans(-2*ans_f[0], ans_f[1]), print_ans(-ans_f[0], ans_f[1])]
            ans1 = ans_[np.random.randint(0,6)]
            f_ = f.format(p1=p1, p2=p2, p3=p3, s1=s1, s2=s2, ans=ans1)
            c_ = c.format(p1=p1, p2=p2, p3=p3, s1=s1, s2=s2, p2_=p2_, p3_=p3_, ans=ans)
        
        ex_list.append([f_, c_])

    ans_list = make_shuffle_example(ex_list, ans_idx)
    cases = answer_dict[ans_list[0]] + " " + ans_list[ans_list[0]+1][1]
    dict_ = answer_dict[ans_list[0]]

    stem = stem.format(ex1=ans_list[1][0], ex2=ans_list[2][0], ex3=ans_list[3][0], ex4=ans_list[4][0], ex5=ans_list[5][0])
    answer = answer.format(a1=answer_dict[ans_list[0]])
    comment = comment.format(cases=cases, dict_=dict_)

    return stem, answer, comment


# 1-1-2-95

#s1은 연산자 
# n1은 분수 
def intandrational112_Stem_058():
    stem = "두 유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여\n"\
        "$$수식$$a`{s1}`{n1}`=`{n2}$$/수식$$,  $$수식$${n3}`{s2}`b`=`{n4}$$/수식$$일 때, "\
        "$$수식$$a`{s}`b$$/수식$$의 값은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$a`=`{n2}`{s1_}`{n1}`{eqa}=`{ansa_a}$$/수식$$\n"\
        "$$수식$$b`=`{nb1}`DIV`{nb2}`=`{nb1}`TIMES`{nb2_}`=`{ansb_a}$$/수식$$\n"\
        "$$수식$$a`{s}`b`=`{ansa}`{s}`{ansb}`=`{ans}$$/수식$$\n\n"

    s_idx = np.random.randint(0,2)
    s1 = ["TIMES", "DIV"][s_idx]
    s2 = ["TIMES", "DIV"][1-s_idx]
    s1_ = ["TIMES", "DIV"][1-s_idx]
    s2_ = ["TIMES", "DIV"][s_idx]

    fs = []
    while len(fs) < 4:
        fr = frac_gen3(1, 1, [2], 5)
        isfrac = 0
        for i in range(len(fs)):
            if fs[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs.append(fr)

    n1 = fs[0][2]
    n2 = print_ans(fs[1][0][0], fs[1][0][1])
    n3 = fs[2][2]
    n4 = print_ans(fs[3][0][0], fs[3][0][1])

    eq_f = "`=`{n}`times`{n_}"
    if s_idx == 1:  #곱하기이면 
        eqa = ""
        ansa_f = [fs[0][0][0]*fs[1][0][0], fs[0][0][1]*fs[1][0][1]]

        nb1 = n3
        nb2 = n4
        nb2_ = print_frac3(fs[3][0][1], fs[3][0][0])
        ansb_f = [fs[2][0][0]*fs[3][0][1], fs[2][0][1]*fs[3][0][0]]

    else:   #나누기이면 
        nb1 = n4
        nb2 = n3
        nb2_ = print_frac3(fs[2][0][1], fs[2][0][0])
        ansb_f = [fs[2][0][1]*fs[3][0][0], fs[2][0][0]*fs[3][0][1]]

        n1_ = print_frac3(fs[0][0][1], fs[0][0][0])
        eqa = eq_f.format(n=n2, n_=n1_)
        ansa_f = [fs[0][0][1]*fs[1][0][0], fs[0][0][0]*fs[1][0][1]]
    
    ansa_f = ctr_frac2(ansa_f[0], ansa_f[1])
    ansa_a = print_ans(ansa_f[0], ansa_f[1])
    ansa = print_frac3(ansa_f[0], ansa_f[1])

    ansb_f = ctr_frac2(ansb_f[0], ansb_f[1])
    ansb_a = print_ans(ansb_f[0], ansb_f[1])
    ansb = print_frac3(ansb_f[0], ansb_f[1])

    rf = np.random.randint(0,2)
    if rf == 0:
        s = "TIMES"
        ans_f = [ansa_f[0]*ansb_f[0], ansa_f[1]*ansb_f[1]]
    else:
        s = "DIV"
        ans_f = [ansa_f[0]*ansb_f[1], ansa_f[1]*ansb_f[0]]

    ans = print_ans(ans_f[0], ans_f[1])
    example_list = make_fraction_example2(ans_f[0], ans_f[1])

    stem = stem.format(n1=n1, n2=n2, n3=n3, n4=n4, s1=s1, s2=s2, s=s, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, nb1=nb1, nb2=nb2, nb2_=nb2_, s1_=s1_, eqa=eqa, ansa_a=ansa_a, ansa=ansa, ansb_a=ansb_a, ansb=ansb, s=s, ans=ans)

    return stem, answer, comment


# 1-1-2-96
def intandrational112_Stem_059():
    stem = "어떤 유리수를 $$수식$${p1_a}$$/수식$${c1} 할 것을 잘못하여 {c2} 그 결과가 "\
        "$$수식$${p2_a}$$/수식$$이 되었다. 바르게 계산한 답은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "어떤 유리수를 $$수식$$x$$/수식$$라 하면 $$수식$$x`{s2}`{p1}`=`{p2}$$/수식$$에서\n"\
        "$$수식$$THEREFORE```x`=`{p2}`{s2_}`{p1}{eqx}`=`{ansx_a}$$/수식$$\n"\
        "따라서 바르게 계산하면\n"\
        "$$수식$${ansx}`{s1}`{p1}`=`{eq}`=`{ans}$$/수식$$\n\n"
    
    cond_idx = np.random.randint(0,2)
    c1 = ["을 곱해야", "으로 나누어야"][cond_idx]
    c2 = ["곱했더니", "나눴더니"][1 - cond_idx]
    s1 = ["TIMES", "DIV"][cond_idx]
    s2 = ["TIMES", "DIV"][1 - cond_idx]

    int_num = np.random.randint(0,2)

    fs = []
    if int_num != 0:
        ns = random.sample([2, 3, 4, 5, 8, 10, 12, 15, 16, 20], int_num)
        ns = random_minus(ns)
        for i in range(int_num):
            if ns[i] > 0:
                fs.append([[ns[i], 1], ns[i], "( +%d)" % ns[i]])
            else:
                fs.append([[ns[i], 1], ns[i], "( %d)" % ns[i]])

    while len(fs) < 2:
        fr = frac_gen3(1, 1, [2, 3, 4, 5, 6], 5)
        isfrac = 0
        for i in range(len(fs)):
            if fs[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs.append(fr)

    p1 = fs[0][2]
    p2 = fs[1][2]
    p1_a = print_ans(fs[0][0][0], fs[0][0][1])
    p2_a = print_ans(fs[1][0][0], fs[1][0][1])

    eq_f = "`=`{n}`times`{n_}"
    p1_ = print_frac3(fs[0][0][1], fs[0][0][0])
    if cond_idx == 0:
        s2_ = "TIMES"
        eqx = ""
        ansx_f = [fs[0][0][0]*fs[1][0][0], fs[0][0][1]*fs[1][0][1]]
        ansx_f = ctr_frac2(ansx_f[0], ansx_f[1])
        ansx = print_frac3(ansx_f[0], ansx_f[1])
        
        
        s1_ = "TIMES"
        eq = ""
        ans_f = [ansx_f[0]*fs[0][0][0], ansx_f[1]*fs[0][0][1]]

    else:
        s2_ = "DIV"
        eqx = eq_f.format(n=p2, n_=p1_)
        ansx_f = [fs[0][0][1]*fs[1][0][0], fs[0][0][0]*fs[1][0][1]]
        ansx_f = ctr_frac2(ansx_f[0], ansx_f[1])
        ansx = print_frac3(ansx_f[0], ansx_f[1])


        s1_ = "DIV"
        eq = eq_f.format(n=ansx, n_=p1_)
        ans_f = [ansx_f[0]*fs[0][0][1], ansx_f[1]*fs[0][0][0]]
    
    
    ansx_a = print_ans(ansx_f[0], ansx_f[1])
    ans = print_ans(ans_f[0], ans_f[1])

    example_list = make_fraction_example2(ans_f[0], ans_f[1])    

    stem = stem.format(c1=c1, c2=c2, p1_a=p1_a, p2_a=p2_a, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(p1=p1, p2=p2, s1=s1, s2=s2, s1_=s1_, s2_=s2_, \
        eqx=eqx, eq=eq, ansx_a=ansx_a, ansx=ansx, ans=ans)

    return stem, answer, comment



# 1-1-2-99
def intandrational112_Stem_060():
    stem = "다음 $$수식$$□$$/수식$$ 안에 알맞은 수는?\n"\
        "$$표$$ $$수식$${p1}`{s1}`□`{s2}`{p2}`=`{p3}$$/수식$$ $$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${p1}`{s1}`□`{s2}`{p2}`=`{p3}$$/수식$$에서\n"\
        "$$수식$${p1}`{s1}`□`=`{p3}`{s2_}`{p2}{eq1}`=`{ans1_a}$$/수식$$\n"\
        "즉, $$수식$${p1}`{s1}`□`=`{ans1_a}$$/수식$$이므로\n"\
        "$$수식$$□`=`{l1}`DIV`{l2}`=`{l1}`TIMES`{l2_}`=`{ans}$$/수식$$\n\n"
    
    fs = []
    while len(fs) < 3:
        fr = frac_gen3(1, 1, [2, 3, 4, 5, 6, 7], 1)
        isfrac = 0
        for i in range(len(fs)):
            if fs[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs.append(fr)

    p1 = fs[0][2]
    p2 = fs[1][2]
    p3 = fs[2][2]

    rf = np.random.randint(0,2)
    sign = ["TIMES", "DIV"]
    
    eq_f = "`=`{n}`times`{n_}"
    if rf == 0:
        s1 = sign[0]
        s1_ = sign[1]
        s2 = sign[1]
        s2_ = sign[0]
        
        eq1 = ""
        ans1_f = ctr_frac2(fs[1][0][0]*fs[2][0][0], fs[1][0][1]*fs[2][0][1])
        ans1_a = print_ans(ans1_f[0], ans1_f[1])
        ans1 = print_frac3(ans1_f[0], ans1_f[1])
        
        l1 = ans1
        l2 = p1
        l2_ = print_frac3(fs[0][0][1], fs[0][0][0])
        ans_f = ctr_frac2(fs[0][0][1]*ans1_f[0], fs[0][0][0]*ans1_f[1])
    else:
        s1 = sign[1]
        s1_ = sign[0]
        s2 = sign[0]
        s2_ = sign[1]

        p2_ = print_frac3(fs[1][0][1], fs[1][0][0])
        eq1 = eq_f.format(n=p3, n_=p2_)
        ans1_f = ctr_frac2(fs[1][0][1]*fs[2][0][0], fs[1][0][0]*fs[2][0][1])
        ans1_a = print_ans(ans1_f[0], ans1_f[1])
        ans1 = print_frac3(ans1_f[0], ans1_f[1])

        l1 = p1
        l2 = ans1
        l2_ = print_frac3(ans1_f[1], ans1_f[0])
        ans_f = ctr_frac2(fs[0][0][0]*ans1_f[1], fs[0][0][1]*ans1_f[0])

    ans = print_ans(ans_f[0], ans_f[1])
    example_list = make_fraction_example2(ans_f[0], ans_f[1])

    stem = stem.format(p1=p1, p2=p2, p3=p3, s1=s1, s2=s2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(p1=p1, p2=p2, p3=p3, s1=s1, s2=s2, s2_=s2_, eq1=eq1, l1=l1, l2=l2, l2_=l2_, ans1_a=ans1_a, ans1=ans1, ans=ans)

    return stem, answer, comment


# 1-1-2-101
def intandrational112_Stem_061():
    stem = "어떤 유리수 $$수식$$rmA$$/수식$$에 $$수식$${p1_a}$$/수식$${j1} {c1} 할 것을 잘못하여 {c2} 그 결과가 "\
        "$$수식$${p2_a}$$/수식$${j2} 되었다. 바르게 계산한 답을 $$수식$$rmB$$/수식$$라 할 때, $$수식$$rmA`{s}`rmB$$/수식$$의 값을 구하시오.\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$rmA`{s1}`{p1}`=`{p2}$$/수식$$이므로\n"\
        "$$수식$$rmA`=`{p2}`{s1_}`{p1}{eqa}`=`{ansa_a}$$/수식$$\n"\
        "따라서 바르게 계산하면\n"\
        "$$수식$$rmB`=`rmA`{s2}`{p1}`=`{ansa}`{s2}`{p1}`=`{ansa_}`{s2}`{p1_}`=`{frb}{eqb}{ansb_a}$$/수식$$\n"\
        "$$수식$$THEREFORE```rmA`{s}`rmB`=`{ansa}`{s}`{ansb}{eq}`=`{ans}$$/수식$$\n\n"
    
    cond_idx1 = np.random.randint(0,2)
    cond_idx2 = np.random.randint(0,2)
    c1 = ["더해야", "빼야"][cond_idx1]
    c2 = ["곱했더니", "나눴더니"][cond_idx2]
    s1 = ["TIMES", "DIV"][cond_idx2]
    s1_ = ["DIV", "TIMES"][cond_idx2]
    s2 = ["+", "-"][cond_idx1]

    fs = []
    while len(fs) < 2:
        fr = frac_gen3(1, 1, [2, 3, 4, 5, 6], 3)
        isfrac = 0
        for i in range(len(fs)):
            if fs[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs.append(fr)

    p1 = fs[0][2]
    j1 = proc_jo(fs[0][0][0], 4)
    p2 = fs[1][2]
    j2 = proc_jo(fs[1][0][0], 0)

    p1_a = print_ans(fs[0][0][0], fs[0][0][1])
    p2_a = print_ans(fs[1][0][0], fs[1][0][1])

    eq_f = "`=`{n}`times`{n_}"
    if cond_idx2 == 1:
        eqa = ""
        ansa_f = ctr_frac2(fs[0][0][0]*fs[1][0][0], fs[0][0][1]*fs[1][0][1])
        ansa_a = print_ans(ansa_f[0], ansa_f[1])
        ansa = print_frac3(ansa_f[0], ansa_f[1])
    else:
        p1_ = print_frac3(fs[0][0][1], fs[0][0][0])
        eqa = eq_f.format(n=p2, n_=p1_)
        ansa_f = ctr_frac2(fs[0][0][1]*fs[1][0][0], fs[0][0][0]*fs[0][0][1])
        ansa_a = print_ans(ansa_f[0], ansa_f[1])
        ansa = print_frac3(ansa_f[0], ansa_f[1])

    lcm1 = lcm(fs[0][0][1], ansa_f[1])
    mult = [int(lcm1/fs[0][0][1]), int(lcm1/ansa_f[1])]
    ansa_ = print_frac3(ansa_f[0]*mult[1], lcm1)
    p1_ = print_frac3(fs[0][0][0]*mult[0], lcm1)

    if cond_idx1 == 0:
        a_hi = ansa_f[0]*mult[1] + fs[0][0][0]*mult[0]
    else:
        a_hi = ansa_f[0]*mult[1] - fs[0][0][0]*mult[0]

    ctr1 = ctr_frac(a_hi, lcm1)
    if ctr1[0] == -1:
        frb = ""
        eqb = ""
        ansb_f = [a_hi, lcm1]
    else:
        eqb = "`=`"
        frb = print_frac3(a_hi, lcm1)
        ansb_f = [ctr1[0], ctr1[1]]
    
    ansb_a = print_ans(ansb_f[0], ansb_f[1])
    ansb = print_frac3(ansb_f[0], ansb_f[1])

    s_idx = np.random.randint(0,2)
    s = ["TIMES", "DIV"][s_idx]

    if s == 0:
        eq = ""
        ans_f = ctr_frac2(ansa_f[0]*ansb_f[0], ansa_f[1]*ansb_f[1])
    else:
        ansb_ = print_frac3(ansb_f[1], ansb_f[0])
        eq = eq_f.format(n=ansa, n_=ansb_)
        ans_f = ctr_frac2(ansa_f[0]*ansb_f[1], ansa_f[1]*ansb_f[0])
    
    ans = print_ans(ans_f[0], ans_f[1])
    example_list = make_fraction_example2(ans_f[0], ans_f[1])

    stem = stem.format(p1_a=p1_a, p2_a=p2_a, c1=c1, c2=c2, j1=j1, j2=j2, s=s, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(p1=p1, p2=p2, s1=s1, s2=s2, s1_=s1_, eqa=eqa, p1_=p1_, ansa_=ansa_, \
        ansa_a=ansa_a, ansa=ansa, frb=frb, eqb=eqb, ansb_a=ansb_a, ansb=ansb, s=s, eq=eq, ans=ans)

    return stem, answer, comment


# 1-1-2-102
def intandrational112_Stem_062():
    stem = "두 수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$a`times`b`{ineq1}`0$$/수식$$이고 "\
        "$$수식$$| a|`=`{p1}$$/수식$$, $$수식$$| b|`=`{p2}$$/수식$$일 때, "\
        "$$수식$$a`{s}`b$$/수식$$의 값은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$a`times`b`{ineq1}`0$$/수식$$이므로 {case1} 또는 {case2}\n"\
        "(1) {case1}일 때, $$수식$$a`=`{p11_}$$/수식$$, $$수식$$b`=`{p21_}$$/수식$$이므로\n"\
        "$$수식$$a`{s}`b`=`{p11}`{s}`{p21}`=`{ans}$$/수식$$\n"\
        "(2) {case2}일 때, $$수식$$a`=`{p12_}$$/수식$$, $$수식$$b`=`{p22_}$$/수식$$이므로\n"\
        "$$수식$$a`{s}`b`=`{p12}`{s}`{p22}`=`{ans}$$/수식$$\n"\
        "(1), (2)에서 $$수식$$a`{s}`b`=`{ans}$$/수식$$\n\n"

    # &lt; < &gt; >
    ineq_idx = np.random.randint(0,2)
    ineq = ["&lt;", "&gt;"]
    ineq1 = ineq[ineq_idx]

    fs = []
    while len(fs) < 2:
        fr = frac_gen3(0, 1, [2,3,4,5,10], 2)
        isfrac = 0
        for i in range(len(fs)):
            if fs[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs.append(fr)

    p1 = print_ans(fs[0][0][0], fs[0][0][1])
    p2 = print_ans(fs[1][0][0], fs[1][0][1])

    case = "$$수식$$a`{i1}`0$$/수식$$, $$수식$$b`{i2}`0$$/수식$$"
    rf = np.random.randint(0,2)
    if ineq_idx == 0:
        case1 = case.format(i1=ineq[1], i2=ineq[0])
        case2 = case.format(i1=ineq[0], i2=ineq[1])
        p11 = fs[0][2]
        p11_ = p1
        p22 = fs[1][2]
        p22_ = p2

        p21 = print_frac3(-fs[1][0][0], fs[1][0][1])
        p21_ = print_ans(-fs[1][0][0], fs[1][0][1])
        p12 = print_frac3(-fs[0][0][0], fs[0][0][1])
        p12_ = print_ans(-fs[0][0][0], fs[0][0][1])

        if rf == 0:
            s = "TIMES"
            ans_f = ctr_frac2(-fs[0][0][0]*fs[1][0][0], fs[0][0][1]*fs[1][0][1])
        else:
            s = "DIV"
            ans_f = ctr_frac2(-fs[0][0][0]*fs[1][0][1], fs[0][0][1]*fs[1][0][0])
    else:
        case1 = case.format(i1=ineq[1], i2=ineq[1])
        case2 = case.format(i1=ineq[0], i2=ineq[0])
        p11 = fs[0][2]
        p11_ = p1
        p21 = fs[1][2]
        p21_ = p2

        p22 = print_frac3(-fs[1][0][0], fs[1][0][1])
        p22_ = print_ans(-fs[1][0][0], fs[1][0][1])
        p12 = print_frac3(-fs[0][0][0], fs[0][0][1])
        p12_ = print_ans(-fs[0][0][0], fs[0][0][1])

        if rf == 0:
            s = "TIMES"
            ans_f = ctr_frac2(fs[0][0][0]*fs[1][0][0], fs[0][0][1]*fs[1][0][1])
        else:
            s = "DIV"
            ans_f = ctr_frac2(fs[0][0][0]*fs[1][0][1], fs[0][0][1]*fs[1][0][0])
    
    ans = print_ans(ans_f[0], ans_f[1])
    example_list = make_fraction_example2(ans_f[0], ans_f[1])

    stem = stem.format(p1=p1, p2=p2, ineq1=ineq1, s=s, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(ineq1=ineq1, case1=case1, case2=case2, p11_=p11_, p12_=p12_, p21_=p21_, p22_=p22_, p11=p11, p12=p12, p21=p21, p22=p22, s=s, ans=ans)

    return stem, answer, comment


# 1-1-2-103
def intandrational112_Stem_063():
    stem = "$$수식$$| a`{sa}`{na1} |`=`{na2}$$/수식$$, $$수식$$| b`{sb}`{nb1} |`=`{nb2}$$/수식$$를 "\
        "만족시키는 정수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여 $$수식$$a`{s}`b$$/수식$$의 값 중 가장 {cond} 것은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$| a`{sa}`{na1} |`=`{na2}$$/수식$$이므로 $$수식$$a`{sa}`{na1}`=`{na2}$$/수식$$ 또는 $$수식$$a`{sa}`{na1}`=`{na2_}$$/수식$$\n"\
        "{a_com}"\
        "$$수식$$| b`{sb}`{nb1} |`=`{nb2}$$/수식$$이므로 $$수식$$b`{sb}`{nb1}`=`{nb2}$$/수식$$ 또는 $$수식$$b`{sb}`{nb1}`=`{nb2_}$$/수식$$\n"\
        "{b_com}"\
        "$$수식$$a`{s}`b$$/수식$$의 값 중 가장 {cond} 것은 $$수식$$a`=`{ansa}$$/수식$$, $$수식$$b`=`{ansb}$$/수식$$일 때이므로\n"\
        "$$수식$$a`{s}`b`=`{ansa_}`{s}`{ansb_}`=`{ans}$$/수식$$\n\n"

    c_idx = np.random.randint(0,2)
    cond = ["큰", "작은"][c_idx]

    s_idx = np.random.randint(0,2)
    s = ["+", "-"][s_idx]

    ans_idxs = [[0,0], [0,1], [1,1], [1,0]][c_idx*2 + s_idx]

    sa_idx = np.random.randint(0,2)
    sb_idx = 1 - sa_idx
    sa = ["TIMES", "DIV"][sa_idx]
    sa_ = ["DIV", "TIMES"][sa_idx]
    sb = ["TIMES", "DIV"][sb_idx]
    sb_ = ["DIV", "TIMES"][sb_idx]

    com_fa = "$$수식$$THEREFORE```a`=`{na2}`{sa_}`{na1}`=`{ansa1}$$/수식$$ 또는 $$수식$$a`=`{na2_}`{sa_}`{na1}`=`{ansa2}$$/수식$$\n"
    com_fb = "$$수식$$THEREFORE```b`=`{nb2}`{sb_}`{nb1}`=`{ansb1}$$/수식$$ 또는 $$수식$$b`=`{nb2_}`{sb_}`{nb1}`=`{ansb2}$$/수식$$\n"

    if sa_idx == 0:
        na1 = np.random.randint(2,6)
        ansa1 = np.random.randint(2,6)
        ansa2 = -ansa1
        na2 = na1 * ansa1
        na2_ = "( -" + str(na2) + ")"

        nb1 = np.random.randint(2,6)
        nb2 = np.random.randint(2,6)
        nb2_ = "( -" + str(nb2) + ")"
        ansb1 = nb1 * nb2
        ansb2 = -ansb1
    else:
        nb1 = np.random.randint(2,6)
        ansb1 = np.random.randint(2,6)
        nb2 = nb1 * ansb1
        nb2_ = "( -" + str(nb2) + ")"
        ansb2 = -ansb1

        na1 = np.random.randint(2,6)
        na2 = np.random.randint(2,6)
        na2_ = "( -" + str(na2) + ")"
        ansa1 = na1 * na2
        ansa2 = -ansa1
    
    a_com = com_fa.format(na2=na2, sa_=sa_, na1=na1, ansa1=ansa1, na2_=na2_, ansa2=ansa2)
    b_com = com_fb.format(nb2=nb2, sb_=sb_, nb1=nb1, ansb1=ansb1, nb2_=nb2_, ansb2=ansb2)
    
    ansa = [ansa1, ansa2][ans_idxs[0]]
    ansb = [ansb1, ansb2][ans_idxs[1]]
    ansa_ = print_frac3(ansa, 1)
    ansb_ = print_frac3(ansb, 1)

    if s_idx == 0:
        ans = ansa + ansb
    else:
        ans = ansa - ansb

    example_list = make_example_minus(ans, int(ans/3))

    stem = stem.format(na1=na1, na2=na2, nb1=nb1, nb2=nb2, sa=sa, sb=sb, cond=cond, s=s, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(na1=na1, na2=na2, nb1=nb1, nb2=nb2, sa=sa, sb=sb, cond=cond, s=s,\
        na2_=na2_, nb2_=nb2_, a_com=a_com, b_com=b_com, ansa=ansa, ansb=ansb, ansa_=ansa_, ansb_=ansb_, ans=ans)

    return stem, answer, comment


# 1-1-2-106
def intandrational112_Stem_064():
    stem = "다음과 같이 어떤 수를 넣으면 $$수식$$rmA$$/수식$$, $$수식$$rmB$$/수식$$, $$수식$$rmC$$/수식$$의 과정을 거쳐 "\
        "계산되는 기계가 있다. 이 기계에 $$수식$${n1}$$/수식$$을 넣었을 때, 계산 결과는?\n"\
        "$$표$$ $$수식$$rmA$$/수식$$: {A_str}\n$$수식$$rmB$$/수식$$: {B_str}\n$$수식$$rmC$$/수식$$: {C_str} $$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${n1}$$/수식$$ → $$수식$$rmA$$/수식$$: $$수식$${eqA}`=`{n2}$$/수식$$\n"\
        "$$수식$${n2}$$/수식$$ → $$수식$$rmB$$/수식$$: $$수식$${eqB}`=`{n3}$$/수식$$\n"\
        "$$수식$${n3}$$/수식$$ → $$수식$$rmC$$/수식$$: $$수식$${eqC}`=`{ans}$$/수식$$\n"\
        "따라서 계산 결과는 $$수식$${ans}$$/수식$$이다.\n\n"
    
    strA = "들어온 수에 $$수식$${p1}$$/수식$${j1} 더한 후 $$수식$${p2}$$/수식$${j2}로 나눈다."
    eqA_f = "LEFT{ %d `+` %s RIGHT}`DIV`%s"

    strB = "들어온 수에서 $$수식$${p3}$$/수식$${j3} 뺀 후 $$수식$${p4}$$/수식$${j4} 곱한다."
    eqB_f = "LEFT{ %d `-` %s RIGHT}`TIMES`%s"
    
    strC = "들어온 수를 $$수식$${p5}$$/수식$${j5}로 나눈 후 $$수식$${p6}$$/수식$${j6} 더한다."
    eqC_f = "%d`DIV`%s`+`%s"

    n1 = np.random.randint(3,10)
    n1 = random_minus([n1])[0]
    p1 = random.sample([-3,-2,-1,1,2,3,4], 1)[0]
    m1 = n1 + p1
    while m1 == 0:
        p1 = random.sample([-3,-2,-1,1,2,3,4], 1)[0]
        m1 = n1 + p1
    j1 = proc_jo(p1, 4)
    
    m1_f = factor(abs(m1))
    if len(m1_f) == 0:
        p2 = random.sample([-1, 1], 1)[0]
    else:
        p2 = random.sample(m1_f, 1)[0]
        p2 = random_minus([p2])[0]
    j2 = "으" if bool_jo(p2) else ""

    p1_ = print_parent_int(p1)
    p2_ = print_parent_int(p2)

    n2 = int(m1/p2)
    A_str = strA.format(p1=p1, j1=j1, p2=p2, j2=j2)
    eqA = eqA_f % (n1, p1_, p2_)
    
    nums = random.sample([-2,-3,-4,2,3,4,5,6,7,8], 2)
    p3 = nums[0]
    p4 = nums[1]
    if n2 == p3:
        p3 = nums[1]
        p4 = nums[0]
    j3 = proc_jo(p3, 4)
    j4 = proc_jo(p4, 4)

    n3 = (n2-p3) * p4
    p3_ = print_parent_int(p3)
    p4_ = print_parent_int(p4)

    B_str = strB.format(p3=p3, j3=j3, p4=p4, j4=j4)
    eqB = eqB_f % (n2, p3_, p4_)

    n3_f = factor(abs(n3))
    if len(n3_f) == 0:
        p5 = random.sample([-1, 1], 1)[0]
    else:
        p5 = random.sample(n3_f, 1)[0]
        p5 = random_minus([p5])[0]
    j5 = "으" if bool_jo(p5) else ""
    p5_ = print_parent_int(p5)

    p6 = random.sample([-3,-2,-1,1,2,3,4], 1)[0]
    p6_ = print_parent_int(p6)
    j6 = proc_jo(p6, 4)
    ans = int(n3/p5) + p6

    C_str = strC.format(p5=p5, j5=j5, p6=p6, j6=j6)
    eqC = eqC_f % (n3, p5_, p6_)

    example_list = make_example_minus(ans, int(ans/3))

    stem = stem.format(n1=n1, A_str=A_str, B_str=B_str, C_str=C_str, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, n3=n3, eqA=eqA, eqB=eqB, eqC=eqC, ans=ans)

    return stem, answer, comment


# 1-1-2-107
def intandrational112_Stem_065():
    stem = "두 유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여\n"\
        "$$수식$$a`◉`b`=`( a`{s1}`b )`{s1}`a`{m1}`b$$/수식$$, "\
        "$$수식$$a`◇`b`=`{n1}`TIMES`b`{s2}`{n2}`TIMES`a$$/수식$$라 약속할 때, "\
        "$$수식$$( {p1}`◇`{p2} )`◉`{p3}$$/수식$$의 값은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${p1}`◇`{p2}`=`{n1}`TIMES`{p2}`{s2}`{n2}`TIMES`{p1}`=`{ans1_}`{s2}`{ans2_}`=`{fr3}{eq3}{ans3}$$/수식$$\n"\
        "$$수식$$( {p1}`◇`{p2} )`◉`{p3}`=`{ans3}`◉`{p3}`=`( {ans3}`{s1}`{p3} )`{s1}`{ans3_}`{m1}`{p3}$$/수식$$\n"\
        "$$수식$$=`{ans4_}`{s1}`{ans5_}`=`{ans}$$/수식$$\n\n"

    # ◉ ◇
    s1_idx = np.random.randint(0,2)
    s2_idx = np.random.randint(0,2)
    m1_idx = np.random.randint(0,2)
    s1 = ["+", "-"][s1_idx]
    s2 = ["+", "-"][s2_idx]
    m1 = ["TIMES", "DIV"][m1_idx]

    ns = random.sample(list(range(2,6)), 2)
    n1 = ns[0]
    n2 = ns[1]

    fs = []
    while len(fs) < 3:
        fr = frac_gen3(0, 1, [2,3,5,6], 3)
        isfrac = 0
        for i in range(len(fs)):
            if fs[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs.append(fr)

    p1 = print_ans(fs[0][0][0], fs[0][0][1])
    p2 = print_ans(fs[1][0][0], fs[1][0][1])
    p3 = print_ans(fs[2][0][0], fs[2][0][1])

    if fs[1][0][1] != 2:
        n1 = factor(fs[1][0][1])[1] * random.sample([-2,-1,1,2],1)[0]
    
    if fs[0][0][1] != 2:
        n2 = factor(fs[0][0][1])[1] * random.sample([-2,-1,1,2],1)[0]

    ans1_f = ctr_frac2(n1*fs[1][0][0], fs[1][0][1])
    ans1_ = print_frac3(ans1_f[0], ans1_f[1])
    ans2_f = ctr_frac2(n2*fs[0][0][0], fs[0][0][1])
    ans2_ = print_frac3(ans2_f[0], ans2_f[1])

    lcm1 = lcm(ans1_f[1], ans2_f[1])
    mult = [int(lcm1/ans1_f[1]), int(lcm1/ans2_f[1])]
    if s2_idx == 0:
        a_hi = ans1_f[0]*mult[0] + ans2_f[0]*mult[1]
    else:
        a_hi = ans1_f[0]*mult[0] - ans2_f[0]*mult[1]

    ctr1 = ctr_frac(a_hi, lcm1)
    if ctr1[0] == -1:
        fr3 = ""
        eq3 = ""
        ans3_f = [a_hi, lcm1]
    else:
        eq3 = "`=`"
        fr3 = print_frac3(a_hi, lcm1)
        ans3_f = [ctr1[0], ctr1[1]]
    ans3 = print_ans(ans3_f[0], ans3_f[1])
    ans3_ = print_frac3(ans3_f[0], ans3_f[1])

    if s1_idx == 0:
        ans4_f = sum_frac(ans3_f, fs[2][0])
    else:
        ans4_f = sum_frac(ans3_f, [-fs[2][0][0], fs[2][0][1]])
    ans4_ = print_frac3(ans4_f[0], ans4_f[1])

    if m1_idx == 0:
        ans5_f = ctr_frac2(ans3_f[0]*fs[2][0][0], ans3_f[1]*fs[2][0][1])
    else:
        ans5_f = ctr_frac2(ans3_f[0]*fs[2][0][1], ans3_f[1]*fs[2][0][0])
    ans5_ = print_frac3(ans5_f[0], ans5_f[1])

    if s1_idx == 0:
        ans_f = sum_frac(ans4_f, ans5_f)
    else:
        ans_f = sum_frac(ans4_f, [-ans5_f[0], ans5_f[1]])
    ans = print_ans(ans_f[0], ans_f[1])

    example_list = make_fraction_example2(ans_f[0], ans_f[1])

    stem = stem.format(n1=n1, n2=n2, s1=s1, s2=s2, m1=m1, p1=p1, p2=p2, p3=p3, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, s1=s1, s2=s2, m1=m1, p1=p1, p2=p2, p3=p3, \
        ans1_=ans1_, ans2_=ans2_, ans3_=ans3_, ans4_=ans4_, ans5_=ans5_, fr3=fr3, eq3=eq3, ans3=ans3, ans=ans)

    return stem, answer, comment


# 1-1-2-108
def intandrational112_Stem_066():
    stem = "$$수식$${eq}$$/수식$$을 계산한 결과는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "음수의 개수가 {c} 개이므로\n"\
        "$$수식$${eq}$$/수식$$\n"\
        "$$수식$$=`{eq1}$$/수식$$\n"\
        "$$수식$$=`{ans}$$/수식$$\n\n"
    
    num1 = np.random.randint(2,5) * 5
    rf = np.random.randint(0,2)

    if rf == 1:
        if num1 % 2 == 0:
            eq = "{%d} over {%d}`times`( -{%d} over {%d} )`times`{%d} over {%d}`times`CDOTS`times`{%d} over {%d}`times`( -{%d} over {%d} )" % (1, 3, 3, 5, 5, 7, 2*num1-3, 2*num1-1, 2*num1-1, 2*num1+1)
        else:
            eq = "{%d} over {%d}`times`( -{%d} over {%d} )`times`{%d} over {%d}`times`CDOTS`times`( -{%d} over {%d} )`times`{%d} over {%d}" % (1, 3, 3, 5, 5, 7, 2*num1-3, 2*num1-1, 2*num1-1, 2*num1+1)
        
        if num1 % 4 in [0, 1]:
            sign = "+"
            c = "짝수"
            ans_frac = [1, 2*num1+1]
            ans = print_ans(ans_frac[0], ans_frac[1])
        else:
            c = "홀수"
            sign = "-"
            ans_frac = [-1, 2*num1+1]
            ans = print_ans(ans_frac[0], ans_frac[1])
        eq1 = "%s( {%d} over {%d}`times`{%d} over {%d}`times`{%d} over {%d}`times`CDOTS`times`{%d} over {%d} )" % (sign, 1, 3, 3, 5, 5, 7, 2*num1-1, 2*num1+1)
    else:
        print("########")
        if num1 % 2 == 1:
            eq = "{%d} over {%d}`times`( -{%d} over {%d} )`times`{%d} over {%d}`times`CDOTS`times`{%d} over {%d}`times`( -{%d} over {%d} )" % (1, 2, 2, 3, 3, 4, num1-2, num1-1, num1-1, num1)
        else:
            eq = "{%d} over {%d}`times`( -{%d} over {%d} )`times`{%d} over {%d}`times`CDOTS`times`( -{%d} over {%d} )`times`{%d} over {%d}" % (1, 2, 2, 3, 3, 4, num1-2, num1-1, num1-1, num1)

        #if num1 % 4 in [0, 1]:
        if num1 % 4 not in [0, 1]:
            sign = "+"
            c = "짝수"
            #ans_frac = [1, 2*num1+1]
            ans_frac = [1, num1]
            ans = print_ans(ans_frac[0], ans_frac[1])
        else:
            c = "홀수"
            sign = "-"
            #ans_frac = [-1, 2*num1+1]
            ans_frac = [-1, num1]
            ans = print_ans(ans_frac[0], ans_frac[1])
        eq1 = "%s( {%d} over {%d}`times`{%d} over {%d}`times`{%d} over {%d}`times`CDOTS`times`{%d} over {%d} )" % (sign, 1, 2, 2, 3, 3, 4, num1-1, num1)

    example_list = make_fraction_example2(ans_frac[0], ans_frac[1])

    stem = stem.format(eq=eq, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(c=c, eq=eq, eq1=eq1, ans=ans)

    return stem, answer, comment

# 1-1-2-110
def intandrational112_Stem_067():
    stem = "수직선 위에 네 유리수 $$수식$${p1}$$/수식$$, $$수식$$x$$/수식$$, $$수식$${p2}$$/수식$$, $$수식$$y$$/수식$$를 "\
        "나타내는 점을 차례대로 나열하면 네 점 사이의 간격이 일정하다. "\
        "이 때, $$수식$$x`{s}`y$$/수식$$의 값은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "각 점 사이의 거리는\n"\
        "$$수식$$ ({minus})`times`{half_f}`=`{intv} $$/수식$$이므로\n"\
        "$$수식$$x`=`{p1}`+`{intv}`=`{ansx}$$/수식$$, $$수식$$y`=`{p2}`+`{intv}`=`{ansy}$$/수식$$\n"\
        "$$수식$$THEREFORE```x`{s}`y`=`{ansx}`{s}`{ansy_}`=`{ans}`$$/수식$$\n\n"

    half_f = "{%d} over {%d}" % (1, 2)

    fs = []
    while len(fs) < 3:
        fr = frac_gen3(1, 1, [2, 3, 4, 5, 6], 3)
        isfrac = 0
        for i in range(len(fs)):
            if fs[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs.append(fr)

    fs.sort(key = lambda ele: ele[1])

    p1 = print_ans(fs[0][0][0], fs[0][0][1])
    p2 = print_ans(fs[1][0][0], fs[1][0][1])

    minus = "LEFT{ %s`-`%s RIGHT}" % (p2, print_frac3(fs[0][0][0], fs[0][0][1]))
    m1 = sum_frac(fs[1][0], [-fs[0][0][0], fs[0][0][1]])
    intv_f = ctr_frac2(m1[0], m1[1]*2)
    intv = print_ans(intv_f[0], intv_f[1])

    ansx_f = sum_frac(fs[0][0], intv_f)
    ansy_f = sum_frac(fs[1][0], intv_f)
    ansx = print_ans(ansx_f[0], ansx_f[1])
    ansy = print_ans(ansy_f[0], ansy_f[1])
    ansy_ = print_frac3(ansy_f[0], ansy_f[1])

    s_idx = np.random.randint(0,2)
    s = ["+", "-"][s_idx]
    if s_idx == 0:
        ans_f = sum_frac(ansx_f, ansy_f)
    else:
        ans_f = sum_frac(ansx_f, [-ansy_f[0], ansy_f[1]])

    ans = print_ans(ans_f[0], ans_f[1])
    example_list = make_fraction_example2(ans_f[0], ans_f[1])

    stem = stem.format(p1=p1, p2=p2, s=s, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(minus=minus, half_f=half_f, intv=intv, p1=p1, p2=p2, ansx=ansx, ansy=ansy, ansy_=ansy_, s=s, ans=ans)

    return stem, answer, comment


# 1-1-2-111
def intandrational112_Stem_068():
    stem = "어느 퀴즈 대회에서 정답을 맞히면 $$수식$${n1}$$/수식$$점, 맞히지 못하면 $$수식$${n2}$$/수식$$점을 준다고 한다. "\
        "또, 맞힌 문제의 개수만큼 보너스 점수를 받는다고 한다. {name}{j} 퀴즈 대회에 나가서 총 $$수식$${tot}$$/수식$$문제 중 "\
        "$$수식$${right}$$/수식$$문제를 맞혔다고 할 때, 받은 점수는?\n"\
        "① $$수식$${ex1}$$/수식$$점     ② $$수식$${ex2}$$/수식$$점     ③ $$수식$${ex3}$$/수식$$점     ④ $$수식$${ex4}$$/수식$$점     ⑤ $$수식$${ex5}$$/수식$$점\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{name}{j} 받은 점수를 계산하면\n"\
        "$$수식$${right}`times`{n1}`+`{wrong}`times`{n2_}`+`{right}`=`{eq}`=`{ans}$$/수식$$점이다.\n\n"
    
    name = ["륜한", "태헌", "민하", "상민", "진욱", "주원", "호준", "재연", "준혁", "보경"][np.random.randint(0,10)]
    j = proc_jo(name, 0)

    n1 = np.random.randint(3,10)
    n2 = random.sample([-1,-2,-3,1,2],1)[0]
    n2_ = n2
    si = "+"
    if n2 < 0:
        n2_ = print_parent_int(n2)
        si = "-"

    tot = np.random.randint(1,4)*5
    right = np.random.randint(int(tot/2), int(tot*3/4))
    wrong = tot - right

    eq = "%d`%s`%d`+`%d" % (n1*right, si, abs(n2)*wrong, right)
    ans = n1*right + n2*wrong + right

    example_list = make_example_by_interval(ans,right)

    stem = stem.format(n1=n1, n2=n2, name=name, j=j, tot=tot, right=right, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2_=n2_, name=name, j=j, right=right, wrong=wrong, eq=eq, ans=ans)

    return stem, answer, comment


# 1-1-2-112
def intandrational112_Stem_069():
    stem = "$$수식$${tot}$$/수식$$개의 수 {lists} 중에서 서로 다른 세 수를 선택하여 다음 괄호 안에 넣어 "\
        "계산하려고 한다. 계산 결과 중 가장 {c1} 것은?\n"\
        "$$표$$ $$수식$$(~~)`DIV`(~~)`TIMES`(~~)^2$$/수식$$ $$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
        "양수가 $$수식$${plus_nr}$$/수식$$개, 음수가 $$수식$${minus_nr}$$/수식$$개일 때, "\
        "$$수식$$(~~)`DIV`(~~)`TIMES`(~~)^2$$/수식$$, 즉 $$수식$$a`DIV`b`TIMES`c^2$$/수식$$을 "\
        "계산한 결과가 가장 {c2} $$수식$$c$$/수식$$는 절댓값이 가장 큰 수이어야 하므로 $$수식$$c`=`{ansc}$$/수식$$\n"\
        "(1) $$수식$$ ( {s11} )`DIV`( {s12} )`TIMES`{ansc_}^2 $$/수식$$\n"\
        "계산한 결과가 가장 {c1} 수이려면\n"\
        "$$수식$${p1}`DIV`{p2}`TIMES`{ansc_}^2`=`{p1}`TIMES`{p2_}`TIMES`{ansc_2}`=`{ans1}$$/수식$$\n"\
        "(2) $$수식$$ ( {s21} )`DIV`( {s22} )`TIMES`{ansc_}^2 $$/수식$$\n"\
        "계산한 결과가 가장 {c1} 수이려면\n"\
        "$$수식$${p3}`DIV`{p4}`TIMES`{ansc_}^2`=`{p3}`TIMES`{p4_}`TIMES`{ansc_2}`=`{ans2}$$/수식$$\n"\
        "(1), (2)에서 계산 결과 중 가장 {c1} 수는 $$수식$${ans}$$/수식$$이다.\n\n"

    c_idx = np.random.randint(0,2)
    c1 = ["큰", "작은"][c_idx]
    c2 = ["크려면", "작으려면"][c_idx]

    tot = 6
    plus_n = np.random.randint(2,4)
    minus_n = tot - plus_n

    fs_p = []
    while len(fs_p) < plus_n:
        fr = frac_gen3(0, 1, [1, 2, 3, 4, 5], 2)
        isfrac = 0
        for i in range(len(fs_p)):
            if fs_p[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs_p.append(fr)
    fs_p.sort(key= lambda ele:ele[1])

    fs_m = []
    while len(fs_m) < minus_n:
        fr = frac_gen3(-1, 1, [1, 2, 3, 4, 5], 2)
        isfrac = 0
        for i in range(len(fs_m)):
            if fs_m[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs_m.append(fr)
    fs_m.sort(key= lambda ele:abs(ele[1]))
    
    fall = fs_p + fs_m

    random.shuffle(fall)
    lists = ""
    for i in range(tot):
        if lists == "":
            lists = lists + "$$수식$$" + print_ans(fall[i][0][0], fall[i][0][1]) + "$$/수식$$"
        else:
            lists = lists + ", $$수식$$" + print_ans(fall[i][0][0], fall[i][0][1]) + "$$/수식$$"

    fall.sort(key= lambda ele:abs(ele[1]))
    ansc = print_ans(fall[tot-1][0][0], fall[tot-1][0][1])
    ansc_ = print_frac3(fall[tot-1][0][0], fall[tot-1][0][1])
    ansc_2f = ctr_frac2(fall[tot-1][0][0]**2, fall[tot-1][0][1]**2)
    ansc_2 = print_frac3(ansc_2f[0], ansc_2f[1])
    
    if fall[tot-1][1] > 0 and plus_n == 2:
        temp = fs_m[minus_n-1]
        temp_ = ([-temp[0][0], temp[0][1]], -temp[1], "RIGHT( +{%d} over {%d} LEFT)" % (abs(temp[0][0]), temp[0][1]))
        fs_p.append(temp_)
        fs_p.sort(key=lambda ele:ele[1])
        del fs_m[minus_n-1]
        plus_n = plus_n + 1
        minus_n = minus_n - 1
    elif fall[tot-1][1] < 0 and minus_n == 2:
        temp = fs_p[plus_n-1]
        temp_ = ([-temp[0][0], temp[0][1]], -temp[1], "RIGHT( -{%d} over {%d} LEFT)" % (temp[0][0], temp[0][1]))
        fs_m.append(temp_)
        fs_m.sort(key=lambda ele:abs(ele[1]))
        del fs_p[plus_n-1]
        plus_n = plus_n - 1
        minus_n = minus_n + 1

    plus_nr = plus_n
    minus_nr = minus_n

    if fall[tot-1][1] > 0:
        del fs_p[plus_n - 1]
        plus_n = plus_n - 1
    else:
        del fs_m[minus_n - 1]
        minus_n = minus_n - 1

    
    if c_idx == 0:
        s11 = "양수"
        s12 = "양수"
        s21 = "음수"
        s22 = "음수"

        p1 = print_ans(fs_p[plus_n-1][0][0], fs_p[plus_n-1][0][1])
        p2 = print_ans(fs_p[0][0][0], fs_p[0][0][1])
        p2_ = print_ans(fs_p[0][0][1], fs_p[0][0][0])
        ans1_f = ctr_frac2(fs_p[plus_n-1][0][0]*fs_p[0][0][1]*ansc_2f[0], fs_p[plus_n-1][0][1]*fs_p[0][0][0]*ansc_2f[1])
        ans1 = print_ans(ans1_f[0], ans1_f[1])

        p3 = print_ans(fs_m[minus_n-1][0][0], fs_m[minus_n-1][0][1])
        p4 = print_ans(fs_m[0][0][0], fs_m[0][0][1])
        p4_ = print_ans(fs_m[0][0][1], fs_m[0][0][0])
        ans2_f = ctr_frac2(fs_m[minus_n-1][0][0]*fs_m[0][0][1]*ansc_2f[0], fs_m[minus_n-1][0][1]*fs_m[0][0][0]*ansc_2f[1])
        ans2 = print_ans(ans2_f[0], ans2_f[1])

        if ans1_f[0]/ans1_f[1] > ans2_f[0]/ans2_f[1]:
            ans_f = ans1_f
        else:
            ans_f = ans2_f

    else:
        s11 = "양수"
        s12 = "음수"
        s21 = "양수"
        s22 = "음수"

        p1 = print_ans(fs_p[plus_n-1][0][0], fs_p[plus_n-1][0][1])
        p2 = print_ans(fs_m[0][0][0], fs_m[0][0][1])
        p2_ = print_ans(fs_m[0][0][1], fs_m[0][0][0])
        ans1_f = ctr_frac2(fs_p[plus_n-1][0][0]*fs_m[0][0][1]*ansc_2f[0], fs_p[plus_n-1][0][1]*fs_m[0][0][0]*ansc_2f[1])
        ans1 = print_ans(ans1_f[0], ans1_f[1])

        p3 = print_ans(fs_m[minus_n-1][0][0], fs_m[minus_n-1][0][1])
        p4 = print_ans(fs_p[0][0][0], fs_p[0][0][1])
        p4_ = print_ans(fs_p[0][0][1], fs_p[0][0][0])
        ans2_f = ctr_frac2(fs_m[minus_n-1][0][0]*fs_p[0][0][1]*ansc_2f[0], fs_m[minus_n-1][0][1]*fs_p[0][0][0]*ansc_2f[1])
        ans2 = print_ans(ans2_f[0], ans2_f[1])

        if ans1_f[0]/ans1_f[1] < ans2_f[0]/ans2_f[1]:
            ans_f = ans1_f
        else:
            ans_f = ans2_f

    ans = print_ans(ans_f[0], ans_f[1])
    example_list = make_fraction_example2(ans_f[0], ans_f[1])

    stem = stem.format(tot=tot, lists=lists, c1=c1, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(plus_nr=plus_nr, minus_nr=minus_nr, c1=c1, c2=c2, ansc=ansc, s11=s11, s12=s12, s21=s21, s22=s22, \
        ansc_=ansc_, ansc_2=ansc_2, p1=p1, p2=p2, p2_=p2_, p3=p3, p4=p4, p4_=p4_, ans1=ans1, ans2=ans2, ans=ans)

    return stem, answer, comment


# 1-1-2-114
def intandrational112_Stem_070():
    stem = "서로 다른 두 유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$에 대하여"\
        "$$수식$$a`◉`b`=`{n1}`{m1}`( a`{s1}`b )$$/수식$$라 할 때, "\
        "$$수식$${p1}`◉`{p2}$$/수식$$의 값은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${p1}`◉`{p2}`=`{n1}`{m1}`( {p1}`{s1}`{p2} )$$/수식$$\n"\
        "{eq_}"\
        "$$수식$$=`{n1}`{m1}`{ans1}$$/수식$$\n"\
        "$$수식$$=`{eq}{ans}$$/수식$$\n\n"

    eq_f = "{n}`TIMES`{n_}`=`"
    eq_2f = "$$수식$$=`{n1}`{m1}`( {p1_}`{s1}`{p2_} )$$/수식$$\n"

    # ◉ ◇
    s1_idx = np.random.randint(0,2)
    m1_idx = np.random.randint(0,2)
    s1 = ["+", "-"][s1_idx]
    m1 = ["TIMES", "DIV"][m1_idx]
    n1 = random.sample(list(range(2,6)), 1)[0]

    fs = []
    while len(fs) < 2:
        fr = frac_gen3(1, 1, [2,3,5,6], 3)
        isfrac = 0
        for i in range(len(fs)):
            if fs[i][1] == fr[1]:
                isfrac = 1
        if isfrac == 0:
            fs.append(fr)

    p1 = print_frac3(fs[0][0][0], fs[0][0][1])
    p2 = print_frac3(fs[1][0][0], fs[1][0][1])

    lcm1 = lcm(fs[0][0][1], fs[1][0][1])
    mult = [int(lcm1/fs[0][0][1]), int(lcm1/fs[1][0][1])]
    p1_ = print_frac3(fs[0][0][0]*mult[0], lcm1)
    p2_ = print_frac3(fs[1][0][0]*mult[1], lcm1)
    if s1_idx == 0:
        a_hi = fs[0][0][0]*mult[0] + fs[1][0][0]*mult[1]
    else:
        a_hi = fs[0][0][0]*mult[0] - fs[1][0][0]*mult[1]

    ans1_f = ctr_frac2(a_hi, lcm1)
    ans1 = print_frac3(ans1_f[0], ans1_f[1])

    if lcm1 == fs[0][0][1]:
        eq_ = ""
    else:
        eq_ = eq_2f.format(n1=n1, m1=m1, p1_=p1_, s1=s1, p2_=p2_)

    if m1_idx == 0:
        ans_f = ctr_frac2(ans1_f[0]*n1, ans1_f[1])
        eq = ""
    else:
        ans_f = ctr_frac2(ans1_f[1]*n1, ans1_f[0])
        eq = eq_f.format(n=n1, n_=print_frac3(ans1_f[1], ans1_f[0]))
    ans = print_ans(ans_f[0], ans_f[1])

    example_list = make_fraction_example2(ans_f[0], ans_f[1])

    stem = stem.format(n1=n1, s1=s1, m1=m1, p1=p1, p2=p2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, s1=s1,m1=m1, p1=p1, p2=p2, eq_=eq_, ans1=ans1, eq=eq, ans=ans)

    return stem, answer, comment


# 1-1-2-116
def intandrational112_Stem_071():
    stem = "자연수 $$수식$$n$$/수식$$에 대하여  $$수식$${given_eq}$$/수식$$임을 이용하여 "\
        "$$수식$${eq}$$/수식$$을 계산한 결과는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${eq}$$/수식$$\n"\
        "$$수식$$=`{eq1}$$/수식$$\n"\
        "$$수식$$=`{eq2}`=`{ans}$$/수식$$\n\n"
    
    given_eq = "{1} over {n(n+1)} = {1} over {n} - {1} over {n+1}"
    eq_f = "{1} over {1 TIMES 2} + {1} over {2 TIMES 3} + {1} over {3 TIMES 4} +` CDOTS `+ {1} over {%d TIMES %d} `"
    eq1_f = "= LEFT ( {1} over {1} - {1} over {2} RIGHT ) + LEFT ( {1} over {2} - {1} over {3} RIGHT ) + LEFT ( {1} over {3} - {1} over {4} RIGHT ) +` CDOTS `+ LEFT ( {1} over {%d} - {1} over {%d} RIGHT )"

    num1 = np.random.randint(2,5) * 5
    rf = np.random.randint(0,2)

    eq = eq_f % (num1-1, num1)
    eq1 = eq1_f % (num1-1, num1)
    eq2 = "1`-`{1} over {%d}" % (num1)
    sum_f = sum_frac([1,1], [-1, num1])
    ans_f = ctr_frac2(sum_f[0], sum_f[1])
    ans = print_ans(ans_f[0], ans_f[1])

    example_list = make_fraction_example2(ans_f[0], ans_f[1])

    stem = stem.format(given_eq=given_eq, eq=eq, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(eq=eq, eq1=eq1, eq2=eq2, ans=ans)

    return stem, answer, comment


# 1-1-2-117
def intandrational112_Stem_072():
    stem = "다음 조건을 모두 만족시키는 서로 다른 세 유리수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$의 대소 관계는?\n"\
        "$$표$$ (가) {st1}\n(나) {st2}\n(다) {st3}\n(라) {st4} $$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "조건 (나), (다)에 의하여 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$ 중 {si_}는 한 개이다.\n"\
        "그런데 조건 (가)에 의하여 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$는 모두 양수이거나 음수이므로\n"\
        "$$수식$$a`{ineqa}`0$$/수식$$, $$수식$$b`{ineqa}`0$$/수식$$, $$수식$$c`{ineqc}`0$$/수식$$\n"\
        "이때 조건 (라)에서 $$수식$$b`{ineqb}`{p_m}$$/수식$$이므로, {eqb}\n"\
        "$$수식$$THEREFORE```{ans}$$/수식$$\n\n"
    
    nums = ["a", "b", "c"]
    order = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    ex_lists = []
    for i in range(len(order)):
        ex_lists.append(nums[order[i][0]] + "`&lt;`" + nums[order[i][1]] + "`&lt;`" + nums[order[i][2]])

    # &lt; < &gt; >
    sign = ["양수", "음수"]
    ineqs = ["&gt;", "&lt;"]

    c1_idx = np.random.randint(0,2)
    c2_idx = np.random.randint(0,2)

    st1 = "$$수식$$a$$/수식$$는 $$수식$$b$$/수식$$의 역수이다."
    st2_f = "$$수식$$a`TIMES`b`TIMES`c`{ineq}`0`$$/수식$$이다."
    st3_f = "$$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$ 중 적어도 하나는 {si}이다."
    st4_f = "$$수식$$| b |`{ineq}`1$$/수식$$이다."
    eqb_f = "$$수식$${1} over {b}`%s`%d$$/수식$$, 즉 $$수식$$a`%s`%d$$/수식$$"

    # a > 0, b > 0, c < 0
    if c1_idx == 0:
        st2 = st2_f.format(ineq=ineqs[1])
        st3 = st3_f.format(si=sign[0])
        si_ = sign[1]

        ineqa = ineqs[0]
        ineqc = ineqs[1]

        p_m = 1
        if c2_idx == 0:
            st4 = st4_f.format(ineq=ineqs[0])
            ineqb = ineqs[0]
            eqb = eqb_f % (ineqs[1], 1, ineqs[1], 1)
            ans_idx = 4
        else:
            st4 = st4_f.format(ineq=ineqs[1])
            ineqb = ineqs[1]
            eqb = eqb_f % (ineqs[0], 1, ineqs[0], 1)
            ans_idx = 5
    # a < 0, b < 0, c > 0
    else:
        st2 = st2_f.format(ineq=ineqs[0])
        st3 = st3_f.format(si=sign[1])
        si_ = sign[0]

        ineqa = ineqs[1]
        ineqc = ineqs[0]

        p_m = -1
        if c2_idx == 0:
            st4 = st4_f.format(ineq=ineqs[0])
            ineqb = ineqs[1]
            eqb = eqb_f % (ineqs[0], -1, ineqs[0], -1)
            ans_idx = 2
        else:
            st4 = st4_f.format(ineq=ineqs[1])
            ineqb = ineqs[0]
            eqb = eqb_f % (ineqs[1], -1, ineqs[1], -1)
            ans_idx = 0

    base = list(range(6))
    del base[ans_idx]
    examples_idx = random.sample(base, 4)
    examples_idx.append(ans_idx)

    ans_list = []
    ans = ex_lists[ans_idx]
    for i in range(5):
        ans_list.append(ex_lists[examples_idx[i]])

    example_list = make_shuffle_example(ans_list, 4)

    stem = stem.format(st1=st1, st2=st2, st3=st3, st4=st4, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(ineqa=ineqa, ineqb=ineqb, ineqc=ineqc, si_=si_, eqb=eqb, p_m=p_m, ans=ans)

    return stem, answer, comment


# 1-1-2-119
def intandrational112_Stem_073():
    stem = "아래는 동전 던지기 게임의 규칙이다. 처음 점수가 $$수식$$0$$/수식$$점일 때, 다음 중 동전을 $$수식$${tot}$$/수식$$번 던져서 "\
        "받을 수 없는 점수는?\n"\
        "$$표$$ (가) 동전의 앞면이 나오면 $$수식$${n1}$$/수식$$점을 받는다.\n"\
        "(나) 동전의 뒷면이 나오면 $$수식$${n2}$$/수식$$점 받는다. $$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$점     ② $$수식$${ex2}$$/수식$$점     ③ $$수식$${ex3}$$/수식$$점     ④ $$수식$${ex4}$$/수식$$점     ⑤ $$수식$${ex5}$$/수식$$점\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{cases}"\
        "이상에서 받을 수 없는 점수는 {a_dict}이다.\n\n"
    
    case_f = "앞면이 $$수식$${front}$$/수식$$회, 뒷면이 $$수식$${back}$$/수식$$회 나오는 경우의 점수는 " + \
        "$$수식$${front}`times`{n1}`+`{back}`times`{n2_}`=`{ans}$$/수식$$(점)\n"

    n1 = np.random.randint(3,8)
    n2 = random.sample([-1,-2,-3,1,2],1)[0]
    n2_ = n2
    if n2 < 0:
        n2_ = print_parent_int(n2)

    tot = np.random.randint(3,6)
    ans_lists = []
    cases = ""
    for i in range(tot+1):
        front = i
        back = tot - i
        ans_ = front*n1 + back*n2
        cases = cases + case_f.format(front=front, back=back, n1=n1, n2_=n2_, ans=ans_)
        ans_lists.append(ans_)

    found = 0
    while found != 1:
        wrong = np.random.randint(-ans_lists[0]-2, ans_lists[len(ans_lists)-1]+2)
        found = 1
        if wrong in ans_lists:
            found = 0
    
    random.shuffle(ans_lists)
    ex_lists = ans_lists[0:4]
    ex_lists.append(wrong)

    example_list = make_shuffle_example(ex_lists, 4)
    a_dict = answer_dict[example_list[0]]

    stem = stem.format(n1=n1, n2=n2, tot=tot, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(cases=cases, a_dict=a_dict)

    return stem, answer, comment
