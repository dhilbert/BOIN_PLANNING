import numpy as np
import random

answer_dict = {
    0: "①",
    1: "②",
    2: "③",
    3: "④",
    4: "⑤"
}


def combination(a, b):
    if a < b:
        return [0, "a needs to be larger than b"]   
    if b == 1:
        return [-1, str(a)]

    multiples1 = ""
    mult1 = 1
    for i in range(b):
        if multiples1 == "":
            multiples1 = multiples1 + str(a-i)
        else:
            multiples1 = multiples1 + "`times`" + str(a-i)
        mult1 = mult1 * (a-i)

    multiples2 = ""
    mult2 = 1
    for i in range(b-1):
        if multiples2 == "":
            multiples2 = multiples2 + str(b-i)
        else:
            multiples2 = multiples2 + "`times`" + str(b-i)
        mult2 = mult2 * (b-i)    

    multiples = "{" + multiples1 + "} over {" + multiples2 + "}"

    return [int(mult1/mult2), multiples] 


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
    return [int(a/gcd(a,b)), int(b/gcd(a,b))]


#  a[0]/a[1] + b[0]/b[1]
def sum_frac(a, b):
    lcm_ = lcm(a[1], b[1])
    ctr = ctr_frac2(a[0] * int(lcm_/a[1]) + b[0] * int(lcm_/b[1]), lcm_)
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


# 2-2-6-01
def numbercases226_Stem_001():
    stem = "{cond} 자연수가 각각 하나씩 적힌 {card_num}장의 카드 중에서 한 장을 뽑을 때, {pick_num}의 배수가 나오는 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{cond} 자연수 중 {pick_num}의 배수는\n"\
        "$$수식$${d1}$$/수식$$, $$수식$${d2}$$/수식$$, $$수식$$CDOTS$$/수식$$, $$수식$${d3}$$/수식$$\n"\
        "이므로 구하는 경우의 수는 {ans}이다.\n\n"
    
    below_num = np.random.randint(1, 10) * 100
    cond_list = ["두 자리", "세 자리", "$$수식$$ {below_num} $$/수식$$이하의".format(below_num=below_num)]
    card_num_list = [90, 900, below_num]

    out = np.random.randint(0, 3)
    cond = cond_list[out]
    card_num = card_num_list[out]

    pick_num = np.random.randint(3, 20)
    
    if out == 0:
        high = (99 // pick_num)
        low = (9 // pick_num)
        d1 = pick_num * (low+1)
        d2 = pick_num * (low+2)
        d3 = pick_num * high
        ans =  high - low
    elif out == 1:
        high = (999 // pick_num)
        low = (99 // pick_num)
        d1 = pick_num * (low+1)
        d2 = pick_num * (low+2)
        d3 = pick_num * high
        ans =  high - low
    elif out == 2:
        ans = below_num // pick_num
        d1 = pick_num * 1
        d2 = pick_num * 2
        d3 = pick_num * ans
    
    example_list = make_example(ans)
    stem = stem.format(cond=cond, card_num="$$수식$$ "+str(card_num)+" $$/수식$$", pick_num="$$수식$$ "+str(pick_num)+" $$/수식$$", \
            ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(cond=cond, pick_num="$$수식$$ "+str(pick_num)+" $$/수식$$", d1=d1, d2=d2, d3=d3, ans="$$수식$$ "+str(ans)+" $$/수식$$")
    
    return stem, answer, comment


# 2-2-6-03
def numbercases226_Stem_002():
    stem = "서로 다른 두 개의 주사위를 동시에 던질 때, 나오는 눈의 수의 {cond}이 {num}이상인 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "두 주사위에서 나오는 눈의 수를 순서쌍으로 나타내면 눈의 수의 {cond}이 {num}이상인 경우는\n"\
        "{answer_pair}\n"\
        "의 {ans}가지이다.\n\n"

    cond_list = ["합", "곱"]
    cond_ind = np.random.randint(0,2)
    cond = cond_list[cond_ind]

    if cond_ind == 0:
        num = np.random.randint(8,11)
    else:
        num = np.random.randint(18,30)

    answer_pair="$$수식$$"
    ans = 0

    if cond_ind == 0:
        for i in range(6):
            for j in range(6):
                if(i+j+2 >= num):
                    if ans%5==0 and ans != 0: 
                        answer_pair=answer_pair + "$$/수식$$\n$$수식$$"
                    answer_pair = answer_pair + "(%d, %d)`````" % (i+1, j+1)
                    ans = ans + 1

    else:
        for i in range(6):
            for j in range(6):
                if((i+1)*(j+1) >= num):
                    if ans%5==0 and ans != 0: 
                        answer_pair=answer_pair + "$$/수식$$ \n $$수식$$"
                    answer_pair = answer_pair + "(%d, %d)`````" % (i+1, j+1)
                    ans = ans + 1

    answer_pair = answer_pair + "$$/수식$$"
    example_list = make_example(ans)

    stem = stem.format(cond=cond, num="$$수식$$ "+str(num)+" $$/수식$$", \
            ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num="$$수식$$ "+str(num)+" $$/수식$$", cond=cond, answer_pair=answer_pair, ans="$$수식$$ "+str(ans)+" $$/수식$$")

    return stem, answer, comment


# 2-2-6-04
def numbercases226_Stem_003():
    stem = "어느 도시의 {game} 대회는 참가한 팀이 돌아가면서 한 번씩 경기하는 리그전으로 예선을 치른다. "\
        "이 대회에 {num}개의 팀이 참가했을 때, 예선에서 치러지는 전체 경기의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{num}개의 팀을 {team_str}"\
        "라 하고 경기를 하는 두 팀씩 짝지으면 "\
        "{answer_pair}이다.\n"\
        "따라서 구하는 전체 경기의 수는 {ans}이다.\n\n"

    game_list = ["축구", "야구", "농구", "배드민턴", "테니스"]
    game_ind = np.random.randint(0,5)
    game = game_list[game_ind]

    num = np.random.randint(3,6)

    team_list = []
    team_str = ""

    for i in range(num):
        team_list.append("$$수식$$rm%s`$$/수식$$" % chr(65 + i))
        if i == num-1:
            team_str = team_str + team_list[i]
        else:
            team_str = team_str + team_list[i] + ", "

    ans = 0
    answer_pair = ""
    for i in range(num):
        for j in range(i+1, num):
            if i == num-2 and j == num-1:
                answer_pair = answer_pair + team_list[i] + "와 " + team_list[j]
            else:
                answer_pair = answer_pair + team_list[i] + "와 " + team_list[j] + ", "
            ans = ans + 1

    example_list = make_example(ans)

    stem = stem.format(game=game, num="$$수식$$ "+str(num)+" $$/수식$$", \
            ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num="$$수식$$ "+str(num)+" $$/수식$$", team_str=team_str, answer_pair=answer_pair, ans="$$수식$$ "+str(ans)+" $$/수식$$")

    return stem, answer, comment

# 2-2-6-08
def numbercases226_Stem_004():
    stem = "한 개의 주사위를 두 번 던져서 처음에 나오는 눈의 수를 $$수식$$x`$$/수식$$, "\
        "나중에 나오는 눈의 수를 $$수식$$y`$$/수식$$라 할 때, "\
        "$$수식$$ {num1}x`+`{num2}y`{inequality}`{num3} $$/수식$$이 되는 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$ {num1}x`+`{num2}y`{inequality}{num3} $$/수식$$이 되는 "\
        "경우를 순서쌍 $$수식$$ (x,`````y )` $$/수식$$로 나타내면\n"\
        "{answer_pair} "\
        "이므로\n구하는 경우의 수는 {ans}이다.\n\n"

    ineq_list = ["&lt;", "LEQ", "&gt;", "GEQ"]
    ineq_ind = np.random.randint(0,4)
    inequality = ineq_list[ineq_ind]

    num_list = [1, 2, 3, 4, 5, 6]
    out = random.sample(num_list, 2)
    num1 = out[0]
    num2 = out[1]

    if ineq_ind < 2:
        low = num1 * 2 + num2 * 2
        high = num1 * 3 + num2 * 3
        num3 = np.random.randint(low, high)
    else:
        low = num1 * 4 + num2 * 4
        high = num1 * 5 + num2 * 5
        num3 = np.random.randint(low, high)

    answer_pair="$$수식$$"
    ans = 0

    if ineq_ind == 0:
        for i in range(6):
            for j in range(6):
                if(num1 * (i+1) + num2 * (j+1) < num3):
                    if ans%5==0 and ans != 0:
                        answer_pair = answer_pair + "$$/수식$$\n$$수식$$"
                    answer_pair = answer_pair + "(%d, %d)`````" % (i+1, j+1)
                    ans = ans + 1
    elif ineq_ind == 1:
        for i in range(6):
            for j in range(6):
                if(num1 * (i+1) + num2 * (j+1) <= num3):
                    if ans%5==0 and ans != 0:
                        answer_pair = answer_pair + "$$/수식$$\n$$수식$$"
                    answer_pair = answer_pair + "(%d, %d)`````" % (i+1, j+1)
                    ans = ans + 1
    elif ineq_ind == 2:
        for i in range(6):
            for j in range(6):
                if(num1 * (i+1) + num2 * (j+1) > num3):
                    if ans%5==0 and ans != 0:
                        answer_pair = answer_pair + "$$/수식$$\n$$수식$$"
                    answer_pair = answer_pair + "(%d, %d)`````" % (i+1, j+1)
                    ans = ans + 1
    elif ineq_ind == 3:
        for i in range(6):
            for j in range(6):
                if(num1 * (i+1) + num2 * (j+1) >= num3):
                    if ans%5==0 and ans != 0:
                        answer_pair = answer_pair + "$$/수식$$\n$$수식$$"
                    answer_pair = answer_pair + "(%d, %d)`````" % (i+1, j+1)
                    ans = ans + 1

    answer_pair = answer_pair + "$$/수식$$"
    example_list = make_example(ans)

    stem = stem.format(num1=('' if num1 == 1 else num1), num2=('' if num2 == 1 else num2), inequality=inequality, num3=num3, \
                ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=('' if num1 == 1 else num1), num2=('' if num2 == 1 else num2), inequality=inequality, num3=num3, answer_pair=answer_pair, ans="$$수식$$ "+str(ans)+" $$/수식$$")

    return stem, answer, comment


# 2-2-6-09
def numbercases226_Stem_005():
    stem = "두 개의 주사위 $$수식$$rmA$$/수식$$, $$수식$$rmB$$/수식$$를 동시에 던져서 나오는 눈의 수를 각각 "\
        "$$수식$$a,`````b`$$/수식$$라 할 때, $$수식$$x`$$/수식$$에 대한 방정식 "\
        "$$수식$$ ax`-`b`=`{num1}` $$/수식$$의 해가 $$수식$${num2}`$$/수식$${j1} 되는 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$ ax`-`b`=`{num1}` $$/수식$$에 $$수식$$x`=`{num2}`$$/수식$${j2} 대입하면\n"\
        "$$수식$$ {num2_}a`-`b`=`{num1}` $$/수식$$   "\
        "$$수식$$ THEREFORE```{num2_}a`=`b`{plus_num1} $$/수식$$\n"\
        "$$수식$$ {num2_}a`=`b`{plus_num1} $$/수식$${j3} 되는 경우를 순서쌍 $$수식$$ (a,`````b )` $$/수식$$로 나타내면  "\
        "{answer_pair}\n"\
        "이므로 구하는 경우의 수는 $$수식$${ans}$$/수식$$이다.\n\n"

    num2 = np.random.randint(1,4)
    j1 = proc_jo(num2, 0)
    j2 = proc_jo(num2, 4)

    num1 = np.random.randint(0,7) - 3
    j3 = proc_jo(abs(num1), 0)
    plus_num1 = ("+`{num1}".format(num1=num1) if num1 > 0 else "-`{num1}".format(num1=abs(num1))) if num1 != 0 else ""

    answer_pair="$$수식$$"
    ans = 0

    for i in range(6):
            for j in range(6):
                if(num2 * (i+1) == (j+1) + num1):
                    answer_pair = answer_pair + "(%d,`````%d)`````" % (i+1, j+1)
                    ans = ans + 1
                    break

    answer_pair = answer_pair + "$$/수식$$"
    example_list = make_example(ans)

    stem = stem.format(num1=num1, num2=num2, j1=j1, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num2=num2, j2=j2, num2_=('' if num2 == 1 else num2), plus_num1=plus_num1, j3=j3, answer_pair=answer_pair, ans=ans)

    return stem, answer, comment


# 2-2-6-11
def numbercases226_Stem_006():
    stem = "각 면에 $$수식$$1`$$/수식$$부터 $$수식$${num1}`$$/수식$$까지의 자연수가 각각 하나씩 적힌 "\
        "{frac} $$수식$$rmA,`````rmB`$$/수식$$가 있다. $$수식$$rmA,`````rmB`$$/수식$$를 동시에 던져서 "\
        "바닥에 오는 면에 적힌 수를 각각 $$수식$$ a,`````b $$/수식$$라 할 때, "\
        "두 직선 $$수식$$y`=`x`+`a`$$/수식$$와 $$수식$$y`=`bx`$$/수식$$의 교점의 "\
        "$$수식$$x`$$/수식$$좌표가 $$수식$${num2}`$$/수식$$인 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "두 직선 $$수식$$y`=`x`+`a`$$/수식$$와 $$수식$$y`=`bx`$$/수식$$의 교점의 좌표가 {num2}일 때 "\
        "$$수식$$y`$$/수식$$좌표는 각각 $$수식$${num2}`+`a,`````{num2_}b`$$/수식$$이므로"\
        "$$수식$$ {num2}`+`a`=`{num2_}b` $$/수식$$\n"\
        "이것을 만족시키는 $$수식$$ a`,`````b`$$/수식$$의 순서쌍 $$수식$$ (a,`````b )` $$/수식$$는\n"\
        "{answer_pair}\n"\
        "이므로 구하는 경우의 수는 $$수식$${ans}`$$/수식$$이다.\n\n"

    frac_list = ["정사면체", "정팔면체", "정십이면체", "정이십면체"]
    frac_ind = np.random.randint(0,4)
    frac = frac_list[frac_ind]
    num1 = (frac_ind+1)*4 if frac_ind < 3 else 20
    
    if frac_ind == 0:
        num2 = np.random.randint(1,4)
    elif frac_ind == 1:
        num2 = np.random.randint(2,4)
    elif frac_ind == 2:
        num2 = np.random.randint(3,8)
    elif frac_ind == 3:
        num2 = np.random.randint(3,10)
    
    answer_pair="$$수식$$"
    ans = 0

    for i in range(num1):
            for j in range(num1):
                if(num2 + (i+1) == (j+1) * num2):
                    answer_pair = answer_pair + "(%d,`````%d)`````" % (i+1, j+1)
                    ans = ans + 1
                    break

    answer_pair = answer_pair + "$$/수식$$"
    example_list = make_example(ans)

    stem = stem.format(num1=num1, frac=frac, num2=num2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num2=num2, num2_=('' if num2 == 1 else num2), answer_pair=answer_pair, ans=ans)

    return stem, answer, comment


# 2-2-6-12
def numbercases226_Stem_007():
    stem = "{place1}에서 {place2}까지 {trans1}{j1} 타고 가는 방법은 $$수식$${num1}`$$/수식$$가지, "\
        "{trans2}{j2} 타고 가는 방법은 $$수식$${num2}`$$/수식$$가지가 있다. "\
        "{place1}에서 {place2}까지 {trans1} 또는 {trans2}{j2} 타고 가는 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{place1}에서 {place2}까지 {trans1}{j1} 타고 가는 방법은 $$수식$${num1}`$$/수식$$가지, "\
        "{trans2}{j2} 타고 가는 방법은 $$수식$${num2}`$$/수식$$가지이므로\n"\
        "$$수식$$ {num1}`+`{num2}`=`{ans}`$$/수식$$\n\n"

    place_list = ["학교", "공원", "영화관", "도서관", "놀이공원", "동물원", "집"]
    out = random.sample(place_list, 2)
    place1 = out[0]
    place2 = out[1]

    trans_list = ["지하철", "버스", "택시", "자전거"]
    out2 = random.sample(trans_list, 2)
    trans1 = out2[0]
    trans2 = out2[1]
    j1 = proc_jo(trans1, 4)
    j2 = proc_jo(trans2, 4)

    num_list = list(map(lambda x: x+3, range(15)))
    out3 = random.sample(num_list, 2)
    num1 = out3[0]
    num2 = out3[1]

    ans = num1 + num2
    example_list = make_example(ans)

    stem = stem.format(place1=place1, place2=place2, trans1=trans1, j1=j1, \
        num1=num1, num2=num2, trans2=trans2, j2=j2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(place1=place1, place2=place2, trans1=trans1, j1=j1, \
        num1=num1, num2=num2, trans2=trans2, j2=j2, ans=ans)

    return stem, answer, comment


# 2-2-6-13
def numbercases226_Stem_008():
    stem = "{name1}{j1} 명절에 {name2} 댁에 가려고 한다. "\
        "기차의 종류는 {train_list}의 $$수식$${num1}$$/수식$$가지가 있고, "\
        "고속버스의 종류는 {bus_list}의 $$수식$${num2}$$/수식$$가지가 있다. "\
        "이 때 {name1}{j1} 기차 또는 고속버스를 이용하여 {name2} 댁에 가는 경우의 수는?\n"
    answer = "(답): $$수식$${a1}$$/수식$$가지\n"
    comment = "(해설)\n"\
        "기차로 가는 경우는 $$수식$${num1}$$/수식$$가지, "\
        "고속버스로 가는 경우는 $$수식$${num2}`$$/수식$$가지이므로 구하는 경우의 수는\n"\
        "$$수식$$ {num1}`+`{num2}`=`{a1}`$$/수식$$\n\n"
    
    name1_list = ["성진이", "동국이", "종석이", "사랑이", "행복이", "철준이", "찬민이"]
    name1_ind = np.random.randint(0,7)
    name1 = name1_list[name1_ind]
    j1 = proc_jo(name1, -1)

    name2_list = ["할머니", "할아버지", "고모", "큰아버지", "이모"]
    name2_ind = np.random.randint(0,5)
    name2 = name2_list[name2_ind]

    train_num = np.random.randint(1,7)
    train_ = ["KTX", "ITX", "무궁화호", "새마을호", "SRT", "누리호"]
    out = random.sample(train_, train_num)
    train_list = ""
    for i in range(train_num):
        train_list = train_list + out[i]
        if i != train_num-1:
            train_list = train_list + ", "

    bus_num = np.random.randint(1,4)
    bus_ = ["우등 고속", "일반 고속", "프리미엄"]
    out = random.sample(bus_, bus_num)
    bus_list = ""
    for i in range(bus_num):
        bus_list = bus_list + out[i]
        if i != bus_num-1:
            bus_list = bus_list + ", "

    a1 = train_num + bus_num

    stem = stem.format(name1=name1, name2=name2, j1=j1, \
        train_list=train_list, bus_list=bus_list, num1=train_num, num2=bus_num)
    answer = answer.format(a1=a1)
    comment = comment.format(num1=train_num, num2=bus_num, a1=a1)

    return stem, answer, comment

# 2-2-6-14
def numbercases226_Stem_009():
    stem = "$$수식$$1$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 자연수가 각각 하나씩 적힌 "\
        "$$수식$${num1}$$/수식$$개의 공이 들어 있는 주머니가 있다. "\
        "이 주머니에서 한 개의 공을 꺼낼 때, $$수식$${num2}$$/수식$$의 배수 또는 "\
        "$$수식$${num3}$$/수식$$의 배수가 나오는 경우의 수를 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$가지\n"
    comment = "(해설)\n"\
        "$$수식$$1$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 자연수 중 "\
        "$$수식$${num2}$$/수식$$의 배수는 {num2_list}의 $$수식$${ans1}$$/수식$$개이고 "\
        "$$수식$${num3}$$/수식$$의 배수는 {num3_list}의 $$수식$${ans2}$$/수식$$개이다.\n"\
        "따라서 구하는 경우의 수는\n"\
        "$$수식$$ {ans1}`+`{ans2}`=`{a1}`$$/수식$$\n\n"
    
    num_list = list(range(3,12))
    out = random.sample(num_list, 2)
    if out[0] > out[1]:
        num2 = out[1]
        num3 = out[0]
    else:
        num2 = out[0]
        num3 = out[1]

    num1 = np.random.randint(num2 + num3, num2 * num3)

    ans1 = num1 // num2
    ans2 = num1 // num3

    num2_list = ""
    for i in range(ans1):
        num2_list = num2_list + "$$수식$$" + str((i+1)*num2) + "$$/수식$$"
        if i != ans1 -1:
            num2_list = num2_list + ", "
    
    num3_list = ""
    for i in range(ans2):
        num3_list = num3_list + "$$수식$$" + str((i+1)*num3) + "$$/수식$$"
        if i != ans2 -1:
            num3_list = num3_list + ", "   

    a1 = ans1 + ans2

    stem = stem.format(num1=num1, num2=num2, num3=num3)
    answer = answer.format(a1=a1)
    comment = comment.format(num1=num1, num2=num2, num3=num3, \
        num2_list=num2_list, num3_list=num3_list, ans1=ans1, ans2=ans2, a1=a1)

    return stem, answer, comment

# 2-2-6-15
def numbercases226_Stem_010():
    stem = "$$수식$$1$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 자연수가 각각 하나씩 적힌 "\
        "$$수식$${num1}$$/수식$$장의 카드가 들어 있는 상자가 있다. "\
        "이 상자에서 한 장의 카드를 꺼낼 때, $$수식$${num2}$$/수식$$의 배수 또는 "\
        "$$수식$${num3}$$/수식$$의 배수가 나오는 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$1$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 자연수 중에서 "\
        "$$수식$${num2}$$/수식$$의 배수는 {num2_list}의 $$수식$${ans1}$$/수식$$개이고,  "\
        "$$수식$${num3}$$/수식$$의 배수는 {num3_list}의 $$수식$${ans2}$$/수식$$개이다.  "\
        "이때 $$수식$${num2}$$/수식$${j2} $$수식$${num3}$$/수식$$의 공배수는 {num4_list}의 "\
        "$$수식$${ans3}$$/수식$$ 개이므로 구하는 경우의 수는\n"\
        "$$수식$$ {ans1}`+`{ans2}`-`{ans3}`=`{ans}`$$/수식$$\n\n"
    
    num_list = list(range(2,10))
    out = random.sample(num_list, 2)
    if out[0] > out[1]:
        num2 = out[1]
        num3 = out[0]
    else:
        num2 = out[0]
        num3 = out[1]
    j2 = proc_jo(num2, 2)
    num4 = lcm(num2, num3)

    num1 = np.random.randint(num4, num4 * 5)

    ans1 = num1 // num2
    ans2 = num1 // num3
    ans3 = num1 // num4

    num2_list = ""
    if ans1 < 7:
        for i in range(ans1):
            num2_list = num2_list + "$$수식$$" + str((i+1)*num2) + "$$/수식$$"
            if i != ans1 -1:
                num2_list = num2_list + ", "
    else:
        num2_list = num2_list + "$$수식$$" + str(num2) + "$$/수식$$" + ", " + "$$수식$$" + str(2*num2) + "$$/수식$$" + \
             ", " + "$$수식$$CDOTS$$/수식$$" + ", " + "$$수식$$" + str(ans1*num2) + "$$/수식$$"
    
    num3_list = ""
    if ans2 < 7:
        for i in range(ans2):
            num3_list = num3_list + "$$수식$$" + str((i+1)*num3) + "$$/수식$$"
            if i != ans2 -1:
                num3_list = num3_list + ", "  
    else:
        num3_list = num3_list + "$$수식$$" + str(num3) + "$$/수식$$" + ", " + "$$수식$$" + str(2*num3) + "$$/수식$$" + \
             ", " + "$$수식$$CDOTS$$/수식$$" + ", " + "$$수식$$" + str(ans2*num3) + "$$/수식$$"

    num4_list = ""
    for i in range(ans3):
        num4_list = num4_list + "$$수식$$" + str((i+1)*num4) + "$$/수식$$"
        if i != ans3 -1:
            num4_list = num4_list + ", "  

    ans = ans1 + ans2 - ans3
    example_list = make_example_by_interval(ans, ans3)

    stem = stem.format(num1=num1, num2=num2, num3=num3, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num2=num2, num3=num3, j2=j2, \
        num2_list=num2_list, num3_list=num3_list, num4_list=num4_list, ans1=ans1, ans2=ans2, ans3=ans3, ans=ans)

    return stem, answer, comment


# 2-2-6-16
def numbercases226_Stem_011():
    stem = "두 개의 주사위 $$수식$$rmA,`````rmB$$/수식$$를 동시에 던질 때, "\
        "나오는 눈의 수의 {cond}이 $$수식$${num1}$$/수식$$ 또는 $$수식$${num2}$$/수식$$인 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "주사위 $$수식$$rmA,`````rmB$$/수식$$에서 나오는 눈의 수를 $$수식$$a,`````b$$/수식$$라 하고 "\
        "순서쌍 $$수식$$(a,`````b )$$/수식$$로 나타내면 눈의 수의 {cond}이 $$수식$${num1}$$/수식$$인 경우는\n"\
        "$$수식$${answer_pair1}$$/수식$$의 $$수식$${ans1}$$/수식$$가지이고 "\
        "눈의 수의 {cond}이 $$수식$${num2}$$/수식$$인 경우는\n"\
        "$$수식$${answer_pair2}$$/수식$$의 $$수식$${ans2}$$/수식$$가지이다.\n"\
        "따라서 구하는 경우의 수는\n"\
        "$$수식$$ {ans1}`+`{ans2}`=`{ans}`$$/수식$$\n\n"
    
    cond_list = ["합", "곱"]
    cond_ind = int(np.random.rand()+0.15)
    cond = cond_list[cond_ind]

    if cond_ind == 0:
        num_list = list(range(4,11))
        out = random.sample(num_list, 2)
    else:
        num_list = [4, 6, 8, 12]
        out = random.sample(num_list, 2)

    if out[0] > out[1]:
        num1 = out[1]
        num2 = out[0]
    else:
        num1 = out[0]
        num2 = out[1]

    answer_pair1 = ""
    answer_pair2 = ""
    ans1 = 0
    ans2 = 0

    if cond_ind == 0:
        for i in range(6):
            for j in range(6):
                if (i+1) + (j+1) == num1:
                    answer_pair1 = answer_pair1 + "(%d, %d)`````" % (i+1, j+1)
                    ans1 = ans1 + 1
                elif (i+1) + (j+1) == num2:
                    answer_pair2 = answer_pair2 + "(%d, %d)`````" % (i+1, j+1)
                    ans2 = ans2 + 1
    else:
        for i in range(6):
            for j in range(6):
                if (i+1) * (j+1) == num1:
                    answer_pair1 = answer_pair1 + "(%d, %d)`````" % (i+1, j+1)
                    ans1 = ans1 + 1
                elif (i+1) * (j+1) == num2:
                    answer_pair2 = answer_pair2 + "(%d, %d)`````" % (i+1, j+1)
                    ans2 = ans2 + 1

    ans = ans1 + ans2
    example_list = make_example_by_interval(ans, int(ans2/2) if ans2 > 2 else 1)

    stem = stem.format(cond=cond, num1=num1, num2=num2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(cond=cond, num1=num1, num2=num2, \
        answer_pair1=answer_pair1, answer_pair2=answer_pair2, ans1=ans1, ans2=ans2, ans=ans)

    return stem, answer, comment


# 2-2-6-17
def numbercases226_Stem_012():
    stem = "$$수식$$1$$/수식$$에서 $$수식$${num1}$$/수식$$까지의 자연수가 각각 적힌 "\
        "$$수식$${num1}$$/수식$$장의 카드에서 한 장의 카드를 뽑을 때, "\
        "$$수식$${num2}$$/수식$$의 배수 또는 "\
        "$$수식$${num3}$$/수식$$의 배수가 나오는 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "(1) $$수식$${num2}$$/수식$$의 배수인 경우 :  "\
        "{num2_list}의 $$수식$${ans1}$$/수식$$가지\n"\
        "(2) $$수식$${num3}$$/수식$$ 의 배수인 경우 :  "\
        "{num3_list}의 $$수식$${ans2}$$/수식$$가지\n"\
        "(3) $$수식$${num2}$$/수식$$ 의 배수이면서 $$수식$${num3}$$/수식$$의 배수인 경우 : "\
        "{num4_list} 의 $$수식$${ans3}$$/수식$$가지\n"\
        "따라서 구하는 경우의 수는\n"\
        "$$수식$$ {ans1}`+`{ans2}`-`{ans3}`=`{ans}`$$/수식$$\n\n"
    
    num_list = list(range(2,10))
    out = random.sample(num_list, 2)
    if out[0] > out[1]:
        num2 = out[1]
        num3 = out[0]
    else:
        num2 = out[0]
        num3 = out[1]
    j2 = proc_jo(num2, 2)
    num4 = lcm(num2, num3)

    num1 = np.random.randint(num4, num4 * 5)

    ans1 = num1 // num2
    ans2 = num1 // num3
    ans3 = num1 // num4

    num2_list = ""
    if ans1 < 7:
        for i in range(ans1):
            num2_list = num2_list + "$$수식$$" + str((i+1)*num2) + "$$/수식$$"
            if i != ans1 -1:
                num2_list = num2_list + ", "
    else:
        num2_list = num2_list + "$$수식$$" + str(num2) + "$$/수식$$" + ", " + "$$수식$$" + str(2*num2) + "$$/수식$$" + \
             ", " + "$$수식$$CDOTS$$/수식$$" + ", " + "$$수식$$" + str(ans1*num2) + "$$/수식$$"
    
    num3_list = ""
    if ans2 < 7:
        for i in range(ans2):
            num3_list = num3_list + "$$수식$$" + str((i+1)*num3) + "$$/수식$$"
            if i != ans2 -1:
                num3_list = num3_list + ", "  
    else:
        num3_list = num3_list + "$$수식$$" + str(num3) + "$$/수식$$" + ", " + "$$수식$$" + str(2*num3) + "$$/수식$$" + \
             ", " + "$$수식$$CDOTS$$/수식$$" + ", " + "$$수식$$" + str(ans2*num3) + "$$/수식$$"

    num4_list = ""
    for i in range(ans3):
        num4_list = num4_list + "$$수식$$" + str((i+1)*num4) + "$$/수식$$"
        if i != ans3 -1:
            num4_list = num4_list + ", "  

    ans = ans1 + ans2 - ans3
    example_list = make_example_by_interval(ans, ans3)

    stem = stem.format(num1=num1, num2=num2, num3=num3, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num2=num2, num3=num3, j2=j2, \
        num2_list=num2_list, num3_list=num3_list, num4_list=num4_list, ans1=ans1, ans2=ans2, ans3=ans3, ans=ans)

    return stem, answer, comment


# 2-2-6-19
def numbercases226_Stem_013():
    stem = "{place1}에서 {place2}까지 가는 방법은 $$수식$${num1}`$$/수식$$가지, "\
        "{place2}에서 {place3}까지 가는 방법은 $$수식$${num2}`$$/수식$$가지가 있다. "\
        "{place1}에서 {place2}{j2} 거쳐 {place3}까지 가는 방법의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{place1}에서 {place2}까지 가는 방법은 $$수식$${num1}`$$/수식$$가지, "\
        "{place2}에서 {place3}까지 가는 방법은 $$수식$${num2}`$$/수식$$가지이므로\n"\
        "$$수식$$ {num1}`times`{num2}`=`{ans}`$$/수식$$\n\n"

    place_list = ["학교", "공원", "영화관", "도서관", "놀이공원", "동물원", "집"]
    out = random.sample(place_list, 3)
    place1 = out[0]
    place2 = out[1]
    place3 = out[2]
    j2 = proc_jo(place2, 4)

    num_list = list(map(lambda x: x+2, range(10)))
    out3 = random.sample(num_list, 2)
    num1 = out3[0]
    num2 = out3[1]

    ans = num1 * num2
    example_list = make_example(ans)

    stem = stem.format(place1=place1, place2=place2, place3=place3, j2=j2, num1=num1, num2=num2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(place1=place1, place2=place2, place3=place3, \
        num1=num1, num2=num2, ans=ans)

    return stem, answer, comment


# 2-2-6-20
def numbercases226_Stem_014():
    stem = "{intro}"\
        "{place1}에서 이 산의 정상까지 가는 등산로는 $$수식$${num1}`$$/수식$$개가 있고, "\
        "{place2}에서 이 산의 정상까지 가는 등산로는 $$수식$${num2}`$$/수식$$개가 있다고 할 때, "\
        "{place1}에서 이 산의 정상까지 올라갔다가 {place2}{j2} 내려오는 방법의 수를 구하시오."\
        "(단, 한 번 지나간 지점은 다시 지나지 않는다.)\n"
    answer = "(답): $$수식$${a1}$$/수식$$가지\n"
    comment = "(해설)\n"\
        "{place1}에서 산의 정상까지 올라가는 방법은 $$수식$${num1}`$$/수식$$가지 "\
        "정상에서 {place2}까지 내려가는 방법은 $$수식$${num2}`$$/수식$$가지이므로 "\
        "구하는 방법의 수는\n"\
        "$$수식$$ {num1}`times`{num2}`=`{a1}`$$/수식$$\n\n"
    
    place_list1 = ["$$수식$$rmA`$$/수식$$ 지역", "$$수식$$rmB`$$/수식$$ 지역"]
    place_list2 = ["약수터", "정자", "쉼터", "계곡"]
    kind = int(np.random.rand() + 0.6)

    if kind == 0:
        place1 = place_list1[0]
        place2 = place_list1[1]
    else:
        out = random.sample(place_list2, 2)
        place1 = out[0]
        place2 = out[1]
    j1 = proc_jo(place1, 2)
    j2 = "으로" if bool_jo(place1) else "로"

    if kind == 0:
        intro = "{place1}{j1} {place2}에 걸쳐 있는 산이 있다. ".format(place1=place1, j1=j1, place2=place2)
    else:
        intro = "어떤 산에 {place1}{j1} {place2}가 있다. ".format(place1=place1, j1=j1, place2=place2)

    num_list = list(map(lambda x: x+2, range(10)))
    out3 = random.sample(num_list, 2)
    num1 = out3[0]
    num2 = out3[1]

    a1 = num1 * num2

    stem = stem.format(intro=intro, place1=place1, place2=place2, j1=j1, j2=j2, num1=num1, num2=num2)
    answer = answer.format(a1=a1)
    comment = comment.format(place1=place1, place2=place2, num1=num1, num2=num2, a1=a1)

    return stem, answer, comment


# 2-2-6-24
def numbercases226_Stem_015():
    stem = "한 개의 주사위를 두 번 던질 때, "\
        "처음에는 $$수식$${num1}`$$/수식$$의 {cond1}의 눈이 나오고, "\
        "나중에는 $$수식$${num2}`$$/수식$$의 {cond2}의 눈이 나오는 경우의 수를 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$가지\n"
    comment = "(해설)\n"\
        "$$수식$${num1}`$$/수식$$의 {cond1}의 눈이 나오는 경우는"\
        "{num1_list}의 $$수식$${ans1}`$$/수식$$가지이고, "\
        "$$수식$${num2}`$$/수식$$의 {cond2}의 눈이 나오는 경우는"\
        "{num2_list}의 $$수식$${ans2}`$$/수식$$가지이므로 구하는 경우의 수는\n"\
        "$$수식$$ {ans1}`times`{ans2}`=`{a1}`$$/수식$$\n\n"
    
    cond_list = ["배수", "약수"]
    cond1_ind = np.random.randint(0,2)
    cond2_ind = np.random.randint(0,2)
    cond1 = cond_list[cond1_ind]
    cond2 = cond_list[cond2_ind]

    if cond1_ind == cond2_ind:
        if cond1_ind == 0:
            out = random.sample([2, 3], 2)
            num1 = out[0]
            num2 = out[1]
        else:
            out = random.sample([4, 6, 8, 12], 2)
            num1 = out[0]
            num2 = out[1]
    else:
        if cond1_ind == 0:
            num1 = np.random.randint(2,4)
            num2 = random.sample([4, 6, 8, 12],1)[0]
        else:
            num1 = random.sample([4, 6, 8, 12],1)[0]
            num2 = np.random.randint(2,4)

    num1_list = ""
    num2_list = ""
    ans1 = 0
    ans2 = 0

    if cond1_ind == 0:
        for i in range(6):
            if (i+1) % num1 == 0:
                if ans1 == 0:
                    num1_list = num1_list + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                else:
                    num1_list = num1_list + ", " + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                ans1 = ans1 + 1
    else:
        for i in range(6):
            if num1 % (i+1) == 0:
                if ans1 == 0:
                    num1_list = num1_list + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                else:
                    num1_list = num1_list + ", " + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                ans1 = ans1 + 1

    if cond2_ind == 0:
        for i in range(6):
            if (i+1) % num2 == 0:
                if ans2 == 0:
                    num2_list = num2_list + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                else:
                    num2_list = num2_list + ", " + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                ans2 = ans2 + 1
    else:
        for i in range(6):
            if num2 % (i+1) == 0:
                if ans2 == 0:
                    num2_list = num2_list + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                else:
                    num2_list = num2_list + ", " + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                ans2 = ans2 + 1
    

    a1 = ans1 * ans2

    stem = stem.format(cond1=cond1, cond2=cond2, num1=num1, num2=num2)
    answer = answer.format(a1=a1)
    comment = comment.format(cond1=cond1, cond2=cond2, num1=num1, num2=num2, \
        num1_list=num1_list, num2_list=num2_list, ans1=ans1, ans2=ans2, a1=a1)

    return stem, answer, comment


# 2-2-6-25
def numbercases226_Stem_016():
    stem = "각 면에 $$수식$$1`$$/수식$$부터 $$수식$${num1}`$$/수식$$까지의 자연수가 각각 하나씩 적힌 "\
        "{frac}를 두 번 던질 때, 바닥에 오는 면에 적힌 수가 "\
        "첫 번째에는 $$수식$$ {num2}` $$/수식$$의 {cond1}, "\
        "두 번째에는 $$수식$$ {num3}` $$/수식$$의 {cond2}인 경우의 수를 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$가지\n"
    comment = "(해설)\n"\
        "$$수식$$1`$$/수식$$부터 $$수식$${num1}`$$/수식$$까지의 자연수 중 "\
        "$$수식$$ {num2}` $$/수식$$의 {cond1}는 "\
        "{num1_list}의 $$수식$${ans1}`$$/수식$$개고, "\
        "$$수식$${num3}`$$/수식$$의 {cond2}는"\
        "{num2_list}의 $$수식$${ans2}`$$/수식$$개이다.\n"\
        "따라서 구하는 경우의 수는\n"\
        "$$수식$$ {ans1}`times`{ans2}`=`{a1}`$$/수식$$\n\n"

    frac_list = ["정사면체", "정팔면체", "정십이면체", "정이십면체"]
    frac_ind = np.random.randint(0,4)
    frac = frac_list[frac_ind]
    num1 = (frac_ind+1)*4 if frac_ind < 3 else 20
    
    if frac_ind == 0:
        cond1_list = [2, 3]
        cond2_list = [2, 4, 6]
    elif frac_ind == 1:
        cond1_list = [2, 3, 4]
        cond2_list = [4, 6, 8, 12, 20, 24]
    elif frac_ind == 2:
        cond1_list = [2, 3, 4, 5]
        cond2_list = [6, 8, 12, 20, 24, 36]
    elif frac_ind == 3:
        cond1_list = [4, 5, 6, 7, 8]
        cond2_list = [8, 12, 20, 24, 36, 40]

    cond_list = ["배수", "약수"]
    cond1_ind = np.random.randint(0,2)
    cond2_ind = np.random.randint(0,2)
    cond1 = cond_list[cond1_ind]
    cond2 = cond_list[cond2_ind]

    if cond1_ind == cond2_ind:
        if cond1_ind == 0:
            out = random.sample(cond1_list, 2)
            num2 = out[0]
            num3 = out[1]
        else:
            out = random.sample(cond2_list, 2)
            num2 = out[0]
            num3 = out[1]
    else:
        if cond1_ind == 0:
            num2 = random.sample(cond1_list,1)[0]
            num3 = random.sample(cond2_list,1)[0]
        else:
            num2 = random.sample(cond2_list,1)[0]
            num3 = random.sample(cond1_list,1)[0]
    
    num1_list = ""
    num2_list = ""
    ans1 = 0
    ans2 = 0

    if cond1_ind == 0:
        for i in range(num1):
            if (i+1) % num2 == 0:
                if ans1 == 0:
                    num1_list = num1_list + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                else:
                    num1_list = num1_list + ", " + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                ans1 = ans1 + 1
    else:
        for i in range(num1):
            if num2 % (i+1) == 0:
                if ans1 == 0:
                    num1_list = num1_list + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                else:
                    num1_list = num1_list + ", " + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                ans1 = ans1 + 1

    if cond2_ind == 0:
        for i in range(num1):
            if (i+1) % num3 == 0:
                if ans2 == 0:
                    num2_list = num2_list + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                else:
                    num2_list = num2_list + ", " + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                ans2 = ans2 + 1
    else:
        for i in range(num1):
            if num3 % (i+1) == 0:
                if ans2 == 0:
                    num2_list = num2_list + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                else:
                    num2_list = num2_list + ", " + "$$수식$$" + "%d" % (i+1) + "$$/수식$$"
                ans2 = ans2 + 1

    a1 = ans1 * ans2

    stem = stem.format(cond1=cond1, cond2=cond2, num1=num1, num2=num2, num3=num3, frac=frac)
    answer = answer.format(a1=a1)
    comment = comment.format(cond1=cond1, cond2=cond2, num1=num1, num2=num2, num3=num3,\
        num1_list=num1_list, num2_list=num2_list, ans1=ans1, ans2=ans2, a1=a1)
    return stem, answer, comment


# 2-2-6-29
def numbercases226_Stem_017():
    stem = "{contest}에 참가할 학생 $$수식$${num1}$$/수식$$명을 뽑아 순서대로 기록을 측정하려고 한다. "\
        "$$수식$${num1}$$/수식$$명의 학생이 {contest}{j1} 하는 순서는 모두 몇 가지인지 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$가지\n"
    comment = "(해설)\n"\
        "$$수식$${num1}$$/수식$$명을 일렬로 나열하여 세우는 경우는\n"\
        "$$수식$${multiples}`=`{a1}`$$/수식$$(가지)\n\n"
    
    contest_list = ["100m 달리기 대회", "50m 달리기 대회", "마라톤 대회", "축구 대회", "농구 대회", "배구 대회", "야구 대회"]
    contest_ind = np.random.randint(0,7)
    contest = contest_list[contest_ind]
    j1 = proc_jo(contest, 4)

    num1 = np.random.randint(3,8)

    multiples = ""
    a1 = 1

    for i in range(num1):
        if i == 0:
            multiples = "%d"%(i+1) + multiples
        else:
            multiples = "%d`times`"%(i+1) + multiples
        a1 = a1 * (i+1)

    stem = stem.format(contest=contest, num1=num1, j1=j1)
    answer = answer.format(a1=a1)
    comment = comment.format(num1=num1, multiples=multiples, a1=a1)

    return stem, answer, comment


# 2-2-6-30
def numbercases226_Stem_018():
    stem = "서로 다른 {obj} $$수식$${num1}`$$/수식$${unit} 중에서 "\
        "$$수식$${num2}`$$/수식$${unit}{j1} 뽑아 {box}에 일렬로 {verb} 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "서로 다른 {obj} $$수식$${num1}`$$/수식$${unit} 중에서 "\
        "$$수식$${num2}`$$/수식$${unit}{j1} 뽑아 {box}에 일렬로 {verb} 경우의 수이므로\n"\
        "$$수식$$ {multiples}`=`{ans}`$$/수식$$\n\n"
    
    index = np.random.randint(0,3)
    
    obj = ["책" , "우표", "스티커"][index]
    unit = ["권", "개", "개"][index]
    j1 = proc_jo(unit, 4)
    box= ["책꽂이", "편지", "책"][index]
    verb = ["꽂는", "붙이는", "붙이는"][index]
    
    num1 = np.random.randint(5,8)
    num2 = np.random.randint(2, num1-2)

    multiples = ""
    ans = 1

    for i in range(num1-num2, num1):
        if i == num1-num2:
            multiples = "%d"%(i+1) + multiples
        else:
            multiples = "%d`times`"%(i+1) + multiples
        ans = ans * (i+1)

    example_list = make_example_by_interval(ans, num1*(num1-num2+1))


    stem = stem.format(obj=obj, num1=num1, num2=num2, unit=unit, j1=j1, box=box, verb=verb, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(obj=obj, num1=num1, num2=num2, unit=unit, j1=j1, box=box, verb=verb, \
        multiples=multiples, ans=ans)

    return stem, answer, comment


# 2-2-6-31
def numbercases226_Stem_019():
    stem = "{names} $$수식$${num1}`$$/수식$$명이 월요일부터 {fin_day}까지 하루에 한 명씩 순서를 정해서 "\
        "{job}{j1} 하기로 하였다. 이 때 {name1}{j2} {day}에 {job}{j1} 하는 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{name1}{j3} 제외한 나머지 $$수식$${num2}`$$/수식$$명의 순서를 정하면 되므로 "\
        "구하는 경우의 수는\n"\
        "$$수식$$ {multiples}`=`{ans}`$$/수식$$\n\n"

    name_list = ["희수", "연이", "선주", "정호", "민우", "륜한", "태헌", "민하", "상민", "진욱", "주원", "호준", "재연", "준혁", "보경"]
    job_list = ["급식 당번", "청소 당번", "주번", "봉사 활동", "독서 활동"]
    week_day = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

    num1 = np.random.randint(4,8)
    num2 = num1 -1
    

    out = random.sample(name_list, num1)
    names = ""
    for i in range(num1):
        if i == 0:
            names = names + str(out[i])
        else:
            names = names + ", " + str(out[i])

    name1 = out[np.random.randint(0,num1)]
    job = job_list[np.random.randint(0,5)]
    day = week_day[np.random.randint(0,num1)]
    fin_day = week_day[num1-1]
    j1 = proc_jo(job, 4)
    j2 = proc_jo(name1, 0)
    j3 = proc_jo(name1, 4)

    multiples = ""
    ans = 1

    for i in range(num2):
        if i == 0:
            multiples = "%d"%(i+1) + multiples
        else:
            multiples = "%d`times`"%(i+1) + multiples
        ans = ans * (i+1)

    example_list = make_example_by_interval(ans, num2)

    stem = stem.format(names=names, num1=num1, name1=name1, job=job, day=day, j1=j1, j2=j2, fin_day=fin_day, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(name1=name1, num2=num2, job=job, j3=j3, \
        multiples=multiples, ans=ans)

    return stem, answer, comment

    
# 2-2-6-32
def numbercases226_Stem_020():
    stem = "{name1}학생 $$수식$${num1}$$/수식$$명, {name2}학생 $$수식$${num2}$$/수식$$명, "\
        "선생님 $$수식$$2`$$/수식$$명이 {verb1} {verb_}서 함께 {verb2} 한다. 선생님 $$수식$$2`$$/수식$$명은 "\
        "양쪽 끝에 {verb3} 할 때, {verb4} 모든 경우의 수를 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$가지\n"
    comment = "(해설)\n"\
        "선생님 $$수식$$2`$$/수식$$명이 양쪽에 {verb}고 학생 $$수식$${num3}$$/수식$$명이 일렬로 {verb}는 경우는\n"\
        "$$수식$${multiples}`=`{ans1}`$$/수식$$(가지)\n"\
        "선생님 $$수식$$2`$$/수식$$명이 서로 자리를 바꾸는 경우가 $$수식$$2`$$/수식$$가지이므로 구하는 경우의 수는\n"\
        "$$수식$${ans1}`times`2`=`{a1}`$$/수식$$\n\n"
    
    name_ind = np.random.randint(0,3)
    verb_ind = np.random.randint(0,3)
    
    name1 = ["여", "1학년 ", "1반 "][name_ind]
    name2 = ["남", "2학년 ", "2반 "][name_ind]
    verb1 = ["나란히", "일렬로", "일렬로"][verb_ind]
    verb2 = ["사진을 찍으려고", "밥을 먹으려고", "놀이공원에 입장하려고"][verb_ind]
    verb3 = ["서서 찍는다고", "앉아서 먹으려고", "서서 입장하려고"][verb_ind]
    verb4 = ["사진을 찍는", "밥을 먹는", "놀이공원에 입장하는"][verb_ind]
    verb_ = ["서", "앉아", "서"][verb_ind]
    verb = ["서", "앉", "서"][verb_ind]

    num1 = np.random.randint(2,5)
    num2 = np.random.randint(1,4)
    num3 = num1 + num2

    multiples = ""
    ans1 = 1

    for i in range(num3):
        if i == 0:
            multiples = "%d"%(i+1) + multiples
        else:
            multiples = "%d`times`"%(i+1) + multiples
        ans1 = ans1 * (i+1)

    a1 = ans1 * 2

    stem = stem.format(name1=name1, name2=name2, verb1=verb1, verb2=verb2, verb3=verb3, verb4=verb4, verb_=verb_, num1=num1, num2=num2)
    answer = answer.format(a1=a1)
    comment = comment.format(verb=verb, num3=num3, multiples=multiples, ans1=ans1, a1=a1)

    return stem, answer, comment


# 2-2-6-33
def numbercases226_Stem_021():
    stem = "{name1}{j}학생 $$수식$${num1}$$/수식$$명, {name2}{j}학생 $$수식$${num1}$$/수식$$명이 "\
        "한 줄로 {verb1} 때, {name1}{j}학생과 {name2}{j}학생이 교대로 {verb2} 경우의 수는?\n"\
        "①$$수식$${ex1}$$/수식$$           ② $$수식$${ex2}$$/수식$$          ③ $$수식$${ex3}$$/수식$$\n"\
        "④$$수식$${ex4}$$/수식$$           ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{name1}{j}학생과 {name2}{j}학생이 교대로 {verb2} 경우는\n"\
        "{list1},\n{list2} 이므로\n"\
        "경우의 수는 $$수식$$2`$$/수식$$이다.\n"\
        "각각의 경우에 대하여 {name1}학생 $$수식$${num1}$$/수식$$명이 한 줄로 {verb2} 경우의 수는\n"\
        "$$수식$${multiples}`=`{ans1}`$$/수식$$\n"\
        "또 {name2}학생 $$수식$${num1}$$/수식$$명이 한 줄로 {verb2} 경우의 수는\n"\
        "$$수식$${multiples}`=`{ans1}`$$/수식$$\n"\
        "따라서 구하는 경우의 수는\n"\
        "$$수식$$2`times`{ans1}`times`{ans1}`=`{ans}`$$/수식$$\n\n"
    
    name_ind = np.random.randint(0,3)
    verb_ind = np.random.randint(0,2)
    
    name1 = ["여", "1학년", "1반"][name_ind]
    name2 = ["남", "2학년", "2반"][name_ind]
    j = ["", " ", " "][name_ind]
    verb1 = ["설", "앉을"][verb_ind]
    verb2 = ["서는", "앉는"][verb_ind]

    num1 = np.random.randint(2,6)

    list1 = ""
    list2 = ""

    for i in range(num1*2):
        if i == 0:
            list1 = list1 + "| " + str(name1) + " | "
            list2 = list2 + "| " + str(name2) + " | "
        elif i%2 == 0:
            list1 = list1 + str(name1) + " | "
            list2 = list2 + str(name2) + " | "
        elif i%2 != 0:
            list1 = list1 + str(name2) + " | "
            list2 = list2 + str(name1) + " | "

    multiples = ""
    ans1 = 1

    for i in range(num1):
        if i == 0:
            multiples = "%d"%(i+1) + multiples
        else:
            multiples = "%d`times`"%(i+1) + multiples
        ans1 = ans1 * (i+1)

    ans = ans1 * ans1 * 2
    example_list = make_example_by_interval(ans, num1 * 2)

    stem = stem.format(name1=name1, name2=name2, verb1=verb1, verb2=verb2, num1=num1, j=j, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(name1=name1, name2=name2, verb2=verb2, num1=num1, j=j, \
        list1=list1, list2=list2, multiples=multiples, ans1=ans1, ans=ans)

    return stem, answer, comment


# 2-2-6-34
def numbercases226_Stem_022():
    stem = "{colors}의 모형 {name} $$수식$${num1}$$/수식$$대를 장식장에 한 줄로 세울 때, "\
        "{color1} {name}{j1} {color2} {name}{j2} 이웃하여 맨 앞에 세우는 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{color1} {name}{j1} {color2} {name}{j2} 제외한 $$수식$${num2}$$/수식$$대를 한 줄로 세우는 경우의 수는\n"\
        "$$수식$${multiples}`=`{ans1}$$/수식$$\n"\
        "이때 {color1} {name}{j1} {color2} {name}{j3} 자리를 바꾸는 경우의 수는 $$수식$$2`$$/수식$$이므로 \n"\
        "구하는 경우의 수는\n"\
        "$$수식$${ans1}`times`2`=`{ans}`$$/수식$$\n\n"
    
    color_list = ["빨간색", "주황색", "노란색", "초록색", "파란색", "남색", "보라색", "검은색", "흰색", "형광색"]
    name = ["자동차", "자전거", "보트", "비행기"][np.random.randint(0,4)]
    j1 = proc_jo(name, 2)
    j2 = proc_jo(name, 4)
    j3 = proc_jo(name, 0)
    
    num1 = np.random.randint(4,9)
    num2 = num1 - 2
    out = random.sample(color_list, num1)

    colors = ""
    for i in range(num1):
        if i == 0:
            colors = colors + str(out[i])
        else:
            colors = colors + ", " + str(out[i])

    num_out = random.sample(list(range(num1)), 2)
    color1 = out[num_out[0]]
    color2 = out[num_out[1]]

    multiples = ""
    ans1 = 1

    for i in range(num2):
        if i == 0:
            multiples = "%d"%(i+1) + multiples
        else:
            multiples = "%d`times`"%(i+1) + multiples
        ans1 = ans1 * (i+1)

    ans = ans1 * 2
    example_list = make_example_by_interval(ans, (num1-2)*(num1-3)*(num1-4) if num1 > 5 else (num1-2)*(num1-3))

    stem = stem.format(name=name, colors=colors, num1=num1, color1=color1, color2=color2, j1=j1, j2=j2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(color1=color1, color2=color2, name=name, num2=num2, j1=j1, j2=j2, j3=j3, \
        multiples=multiples, ans1=ans1, ans=ans)

    return stem, answer, comment


# 2-2-6-35
def numbercases226_Stem_023():
    stem = "{name1}{j}학생 $$수식$${num1}$$/수식$$명, {name2}{j}학생 $$수식$${num2}$$/수식$$명이 "\
        "일렬로 {verb1}때, {name1}{j}학생은 {name1}{j}학생끼리, {name2}{j}학생은 {name2}{j}학생끼리 "\
        "이웃하여 {verb2} 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$ \n④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{name1}{j}학생과 {name2}{j}학생을 각각 $$수식$$1`$$/수식$$명으로 생각하여 $$수식$$2`$$/수식$$명을 일렬로 배열하는 경우의 수는\n"\
        "$$수식$$2`times`1=`2`$$/수식$$\n"\
        "이때 {name1}{j}학생끼리, {name2}{j}학생끼리 자리를 바꾸는 경우의 수는 각각\n"\
        "$$수식$${multiples1}`=`{ans1}`$$/수식$$, $$수식$${multiples2}`=`{ans2}`$$/수식$$이다. \n"\
        "따라서 구하는 경우의 수는\n"\
        "$$수식$$2`times`{ans1}`times`{ans2}`=`{ans}`$$/수식$$\n\n"
    
    name_ind = np.random.randint(0,4)
    verb_ind = np.random.randint(0,2)
    
    name1 = ["여", "1학년", "1반", "초등"][name_ind]
    name2 = ["남", "2학년", "2반", "중"][name_ind]
    j = ["", " ", " ", ""][name_ind]
    verb1 = ["설", "앉을"][verb_ind]
    verb2 = ["서는", "앉는"][verb_ind]

    num1 = np.random.randint(3,6)
    num2 = np.random.randint(2,5)

    multiples1 = ""
    ans1 = 1
    for i in range(num1):
        if i == 0:
            multiples1 = "%d"%(i+1) + multiples1
        else:
            multiples1 = "%d`times`"%(i+1) + multiples1
        ans1 = ans1 * (i+1)

    multiples2 = ""
    ans2 = 1
    for i in range(num2):
        if i == 0:
            multiples2 = "%d"%(i+1) + multiples2
        else:
            multiples2 = "%d`times`"%(i+1) + multiples2
        ans2 = ans2 * (i+1)

    ans = ans1 * ans2 * 2
    example_list = make_example_by_interval(ans, num1*(num1-1)*(num1-2)*num2*(num2-1))

    stem = stem.format(name1=name1, name2=name2, verb1=verb1, verb2=verb2, num1=num1, num2=num2, j=j, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(name1=name1, name2=name2, verb2=verb2, num1=num1, num2=num2, j=j, \
        multiples1=multiples1, ans1=ans1, multiples2=multiples2, ans2=ans2, ans=ans)

    return stem, answer, comment


# 2-2-6-36
def numbercases226_Stem_024():
    stem = "$$수식$${num1}$$/수식$$명의 학생 {std_str}를 일렬로 "\
        "{verb1} 때, {name1}, {name2}가 이웃하고 {name2}가 {name1}의 뒤에 {verb2} 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{name1}, {name2}를  $$수식$$1`$$/수식$$명으로 생각하여  $$수식$${num2}`$$/수식$$명을 일렬로 배열하는 경우의 수는\n"\
        "$$수식$${multiples}`=`{ans1}`$$/수식$$\n"\
        "이때 {name1}, {name2}의 자리는 정해져 있으므로 구하는 경우의 수는 $$수식$${ans1}$$/수식$$이다.\n\n"

    num1 = np.random.randint(3,8)
    num2 = num1 - 1

    std_list = []
    std_str = ""

    for i in range(num1):
        std_list.append("$$수식$$rm%s`$$/수식$$" % chr(65 + i))
        if i == num1-1:
            std_str = std_str + std_list[i]
        else:
            std_str = std_str + std_list[i] + ", "

    out = random.sample(list(range(num1)), 2)
    name1 = std_list[min(out[0], out[1])]
    name2 = std_list[max(out[0], out[1])]

    verb_ind = np.random.randint(0,2)
    verb1 = ["세울", "앉힐"][verb_ind]
    verb2 = ["서는", "앉는"][verb_ind]

    multiples = ""
    ans1 = 1

    for i in range(num2):
        if i == 0:
            multiples = "%d"%(i+1) + multiples
        else:
            multiples = "%d`times`"%(i+1) + multiples
        ans1 = ans1 * (i+1)

    example_list = make_example_by_interval(ans1, num2*(num2-1)*(num2-2) if num2 > 4 else num2*(num2-1) )

    stem = stem.format(name1=name1, name2=name2, verb1=verb1, verb2=verb2, num1=num1, std_str=std_str, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(name1=name1, name2=name2, verb2=verb2, num2=num2, \
        multiples=multiples, ans1=ans1)

    return stem, answer, comment


# 2-2-6-39
def numbercases226_Stem_025():
    stem = "$$수식$$5`$$/수식$$개의 문자 {alp_str}를 {examples}와 같이 "\
        "사전식으로 나열할 때, {ans_str}는 몇 번째에 나오는가?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{first_case}"\
        "{second_case}"\
        "{third_case}"\
        "{final_case}"\
        "따라서 {ans_str}가 나오는 것은\n"\
        "$$수식$${plus}`=`{ans}$$/수식$$(번째)\n\n"

    first_format = "({num1}) {a1} __ __ __ __인 경우\n" + \
        "$$수식$${a1}$$/수식$$를 제외한 $$수식$$4$$/수식$$개의 문자를 일렬로 나열하는 경우의 수는 " + \
        "$$수식$$4`times`3`times`2`times`1`=`24$$/수식$$\n"
    second_format = "({num2}) {a2_1}$$수식$$``$$/수식$${a2_2}__ __ __인 경우\n" + \
        "$$수식$${a2_1}$$/수식$$, $$수식$${a2_2}$$/수식$$를 제외한 $$수식$$3$$/수식$$개의 문자를 일렬로 나열하는 경우의 수는 " + \
        "$$수식$$3`times`2`times`1`=`6$$/수식$$\n"
    third_format = "({num3}) {a3_1}$$수식$$``$$/수식$${a3_2}$$수식$$``$$/수식$${a3_3} __ __ 인 경우\n" + \
        "$$수식$${a3_1}$$/수식$$, $$수식$${a3_2}$$/수식$$, $$수식$${a3_3}$$/수식$$를 제외한 $$수식$$2$$/수식$$개의 문자를 일렬로 나열하는 경우의 수는 " + \
        "$$수식$$2`times`1`=`2$$/수식$$\n"
    final_format = "({num4}) {a4_1}$$수식$$``$$/수식$${a4_2}$$수식$$``$$/수식$${a4_3} __ __ 인 경우\n" + \
        "{str}의 $$수식$$2$$/수식$$가지이다.\n"
    
    alp_list = []
    alp_str = ""
    examples = "$$수식$$rma``b``c``d``e$$/수식$$, $$수식$$rma``b``c``e``d$$/수식$$, $$수식$$rma``b``d``c``e$$/수식$$, $$수식$$CDOTS$$/수식$$, $$수식$$rme``d``c``b``a$$/수식$$"

    for i in range(5):
        alp_list.append("$$수식$$rm%s$$/수식$$" % chr(97 + i))
        if i == 4:
            alp_str = alp_str + alp_list[i]
        else:
            alp_str = alp_str + alp_list[i] + ", "
    
    #examples = ""

    word = [0, 1, 2, 3, 4]
    while(1):
        np.random.shuffle(word)
        if word[0] != 0 and word[0] != 4:
            break
    
    ans_str = ""
    for i in range(5):
        if i == 0:
            ans_str = ans_str + alp_list[word[i]]
        else:
            ans_str = ans_str + alp_list[word[i]]

    count = 0
    first_case = ""
    for i in range(word[0]):
        count = count + 1
        first_case = first_case + first_format.format(num1=count, a1=alp_list[i])
    first_cnt = count

    second_case = ""
    for i in range(word[1]):
        if i != word[0]:
            count = count + 1
            second_case = second_case + second_format.format(num2=count, a2_1=alp_list[word[0]], a2_2=alp_list[i])
    second_cnt = count

    third_case = ""
    for i in range(word[2]):
        if i != word[0] and i != word[1]:
            count = count + 1
            third_case = third_case + third_format.format(num3=count, a3_1=alp_list[word[0]], a3_2=alp_list[word[1]], a3_3=alp_list[i])
    third_cnt = count

    num_fin = 1
    str_ = alp_list[word[0]] + alp_list[word[1]] + alp_list[word[2]] + alp_list[min(word[3], word[4])] + alp_list[max(word[3], word[4])]
    if(max(word[3], word[4]) == word[3]):
        num_fin = 2
    str_ = str_ + ", "+ alp_list[word[0]] + alp_list[word[1]] + alp_list[word[2]] + alp_list[max(word[3], word[4])] + alp_list[min(word[3], word[4])]
    
    count = count + 1
    final_case = final_format.format(num4=count, a4_1=alp_list[word[0]], a4_2=alp_list[word[1]], a4_3=alp_list[word[2]], str=str_)

    plus = ""
    ans = 0

    for i in range(count):
        if i < first_cnt:
            if i == 0:
                plus = plus + "24"
                ans = ans + 24
            else:
                plus = plus + "`+`24"
                ans = ans + 24
        elif i < second_cnt:
            plus = plus + "`+`6"
            ans = ans + 6
        elif i < third_cnt:
            plus = plus + "`+`2"
            ans = ans + 2
        else:
            plus = plus + "`+`%d"%num_fin
            ans = ans + num_fin

    example_list = make_example_by_interval(ans, 1)

    stem = stem.format(alp_str=alp_str, examples=examples, ans_str=ans_str, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(first_case=first_case, second_case=second_case, third_case=third_case, final_case=final_case, plus=plus, ans_str=ans_str, ans=ans)

    return stem, answer, comment


# 2-2-6-41
def numbercases226_Stem_026():
    stem = "$$수식$${num1}$$/수식$$명의 학생 {name_str}를 일렬로 "\
        "{verb1} 때, 다음 조건을 만족하는 경우의 수는?\n"\
        "$$표$$(가) {name1}와 {name2}는 이웃하고 {name1}가 {name2}의 앞에 선다.\n(나) {names}는 이웃하지 않는다.$$/표$$\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{name1}, {name2}를  $$수식$$1`$$/수식$$명으로 생각하여  $$수식$${num2}`$$/수식$$명을 일렬로 배열하는 경우의 수는\n"\
        "$$수식$${multiples1}`=`{ans1}`$$/수식$$\n"\
        "이때 {name1}, {name2}의 자리는 정해져 있으므로 조건 (가)를 만족시키는 경우의 수는 $$수식$${ans1}$$/수식$$이다.\n"\
        "{name1}, {name2}를  $$수식$$1`$$/수식$$명, {names}를  $$수식$$1`$$/수식$$명으로 생각하여 "\
        "$$수식$${num3}`$$/수식$$명을 일렬로 배열하는 경우의 수는\n"\
        "$$수식$${multiples2}`=`{ans2}`$$/수식$$\n"\
        "이때 {names}가 서로 자리를 바꾸는 경우의 수는 $$수식$${num4}`$$/수식$$이므로 조건 (가)를 만족시키면서 "\
        "{names}가 이웃하는 경우의 수는\n"\
        "$$수식$${ans2}`times{num4}`=`{ans3}`$$/수식$$\n"\
        "따라서 구하는 경우의 수는\n"\
        "$$수식$${ans1}`-`{ans3}`=`{ans}`$$/수식$$\n\n"

    verb1 = ["세울", "앉힐"][np.random.randint(0,2)]

    num1 = np.random.randint(4,8)
    num2 = num1 - 1
    num_ = np.random.randint(2, num1-1)
    num3 = num2 - num_ + 1

    name_list = []
    name_str = ""

    for i in range(num1):
        name_list.append("$$수식$$rm%s`$$/수식$$" % chr(65 + i))
        if i == num1-1:
            name_str = name_str + name_list[i]
        else:
            name_str = name_str + name_list[i] + ", "

    sample_num = list(range(num1))
    out = random.sample(sample_num, 2+num_)
    name1 = name_list[min(out[0], out[1])]
    name2 = name_list[max(out[0], out[1])]

    out = out[2:num_+2]
    out.sort()
    names = ""
    for i in range(num_):
        if i == 0:
            names = names + name_list[out[i]]
        else:
            names = names + ", " + name_list[out[i]]

    multiples1 = ""
    ans1 = 1

    for i in range(num2):
        if i == 0:
            multiples1 = "%d"%(i+1) + multiples1
        else:
            multiples1 = "%d`times`"%(i+1) + multiples1
        ans1 = ans1 * (i+1)

    multiples2 = ""
    ans2 = 1

    for i in range(num3):
        if i == 0:
            multiples2 = "%d"%(i+1) + multiples2
        else:
            multiples2 = "%d`times`"%(i+1) + multiples2
        ans2 = ans2 * (i+1)

    num4 = 1
    for i in range(num_):
        num4 = num4 * (i+1)
    
    ans3 = num4 * ans2
    ans = ans1 - ans3

    example_list = make_example_by_interval(ans, num4)

    stem = stem.format(name1=name1, name2=name2, verb1=verb1, num1=num1, name_str=name_str, names=names, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(name1=name1, name2=name2, names=names, num2=num2, num3=num3, num4=num4, num_=num_, \
        multiples1=multiples1, multiples2=multiples2, ans1=ans1, ans2=ans2, ans3=ans3, ans=ans)

    return stem, answer, comment


# 2-2-6-42
def numbercases226_Stem_027():
    stem = "$$수식$$1$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 자연수가 각각 하나씩 적힌 "\
        "$$수식$${num1}$$/수식$$장의 카드에서 $$수식$$2$$/수식$$장을 뽑아 만들 수 있는 두 자리 자연수 중 "\
        "$$수식$${num2}$$/수식$$보다 {cond} 수의 개수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{cases}"\
        "따라서 $$수식$${num2}$$/수식$$보다 {cond} 수의 개수는\n"\
        "$$수식$$ {plus}`=`{ans}`$$/수식$$\n\n"
    
    cases_format = "({num1}) 십의 자리의 숫자가 $$수식$${num2}$$/수식$$인 경우\n" + \
        "일의 자리에 올 수 있는 숫자는 {numbers}의 $$수식$${num3}$$/수식$$가지이다.\n"
    
    num1 = np.random.randint(5, 9)
    cond_ind = np.random.randint(0,2)
    cond = ["큰", "작은"][cond_ind]

    if cond == 0:
        num2 = np.random.randint((num1//2 + 1), (num1-1))*10 + np.random.randint(num1-3, num1-1)
    else:
        num2 = np.random.randint(2, (num1//2 + 1))*10 + np.random.randint(2, num1//2 + 1)

    num2_1 = num2 // 10
    num2_2 = num2 - num2_1*10

    cases = ""
    count = 1
    num3_list = []
    if cond_ind == 0:
        for i in range(num2_1, num1+1):
            numbers = ""
            num3 = 0
            if i == num2_1:
                for j in range(num1):
                    if (num1-j) == i:
                        continue
                    if (num1-j) > num2_2:
                        if numbers == "":
                            numbers = "$$수식$$%d$$/수식$$"%(num1-j) + numbers
                        else:
                            numbers = "$$수식$$%d$$/수식$$, "%(num1-j) + numbers
                        num3 = num3 + 1
                    else:
                        break
            else:
                for j in range(num1):
                    if (num1-j) == i:
                        continue
                    if numbers == "":
                        numbers = "$$수식$$%d$$/수식$$"%(num1-j) + numbers
                    else:
                        numbers = "$$수식$$%d$$/수식$$, "%(num1-j) + numbers
                    num3 = num3 + 1
            if num3 != 0:
                num3_list.append(num3)
                cases = cases + cases_format.format(num1=count, num2=i, numbers=numbers, num3=num3)
                count = count + 1
    else:
        for i in range(1, num2_1+1):
            numbers = ""
            num3 = 0
            if i == num2_1:
                for j in range(num1):
                    if j+1 == i:
                        continue
                    if j+1 < num2_2:
                        if numbers == "":
                            numbers = numbers + "$$수식$$%d$$/수식$$"%(j+1)
                        else:
                            numbers = numbers + ", $$수식$$%d$$/수식$$"%(j+1)
                        num3 = num3 + 1
                    else:
                        break
            else:
                for j in range(num1):
                    if j+1 == i:
                        continue
                    if numbers == "":
                        numbers = numbers + "$$수식$$%d$$/수식$$"%(j+1)
                    else:
                        numbers = numbers + ", $$수식$$%d$$/수식$$"%(j+1)
                    num3 = num3 + 1
            if num3 != 0:
                num3_list.append(num3)
                cases = cases + cases_format.format(num1=count, num2=i, numbers=numbers, num3=num3)
                count = count + 1

    plus = ""
    ans = 0
    for i in range(len(num3_list)):
        if i == 0:
            plus = plus + str(num3_list[i])
        else:
            plus = plus + "`+`" + str(num3_list[i])
        ans = ans + num3_list[i]
    
    example_list = make_example(ans)

    stem = stem.format(num1=num1, num2=num2, cond=cond, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(cases=cases, num2=num2, cond=cond, plus=plus, ans=ans)

    return stem, answer, comment


# 2-2-6-43
def numbercases226_Stem_028():
    stem = "{numbers}가 각각 하나씩 적힌 $$수식$${num1}$$/수식$$장의 카드 중에서 "\
        "$$수식$${num2}$$/수식$$장을 뽑아 만들 수 있는 {bits_cnt} 자리 자연수의 개수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{case}"\
        "따라서 구하는 자연수의 개수는\n"\
        "$$수식$$ {multiples}`=`{ans}`$$/수식$$\n\n"
    
    if_bai = "백의 자리에 올 수 있는 숫자는 $$수식$$0`$$/수식$$을 제외한 $$수식$${num1}$$/수식$$가지, " + \
        "십의 자리에 올 수 있는 숫자는 백의 자리에 온 숫자를 제외한 $$수식$${num1}$$/수식$$가지, " + \
        "일의 자리에 올 수 있는 숫자는 백의 자리에 온 숫자와 십의 자리에 온 숫자를 제외한 $$수식$${num2}$$/수식$$가지이다.\n"
    
    if_qian = "천의 자리에 올 수 있는 숫자는 $$수식$$0`$$/수식$$을 제외한 $$수식$${num1}$$/수식$$가지, " + \
        "백의 자리에 올 수 있는 숫자는 천의 자리에 온 숫자를 제외한 $$수식$${num1}$$/수식$$가지, " + \
        "십의 자리에 올 수 있는 숫자는 천의 자리에 온 숫자와 백의 자리에 온 숫자를 제외한 $$수식$${num2}$$/수식$$가지, " + \
        "일의 자리에 올 수 있는 숫자는 천의 자리에 온 숫자, 백의 자리에 온 숫자, 십의 자리에 온 숫자를 제외한 $$수식$${num3}$$/수식$$가지이다.\n"

    num1 = np.random.randint(4,10)
    num2 = np.random.randint(3,5)
    numbers = ""
    for i in range(num1):
        if i == 0:
            numbers = numbers + "$$수식$$" + str(i) + "$$/수식$$"
        else:
            numbers = numbers + ", $$수식$$" + str(i) + "$$/수식$$"

    bits_cnt = ["세" , "네"][num2-3]

    if num2 == 3:
        case = if_bai.format(num1=num1-1, num2=num1-2)
        multiples = "%d`times`%d`times`%d"%(num1-1, num1-1, num1-2)
        ans = (num1-1) * (num1-1) * (num1-2)
    else:
        case = if_qian.format(num1=num1-1, num2=num1-2, num3=num1-3)
        multiples = "%d`times`%d`times`%d`times`%d"%(num1-1, num1-1, num1-2, num1-3)
        ans = (num1-1) * (num1-1) * (num1-2) * (num1-3)
    
    example_list = make_example_by_interval(ans, (num1-1)*(num1-2))

    stem = stem.format(numbers=numbers, num1=num1, num2=num2, bits_cnt=bits_cnt, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(case=case, multiples=multiples, ans=ans)

    return stem, answer, comment


# 2-2-6-44
def numbercases226_Stem_029():
    stem = "$$수식$$1`$$/수식$$에서 $$수식$${num1}$$/수식$$까지의 숫자가 하나씩 적혀 있는 카드 $$수식$${num1}$$/수식$$장이 있다. "\
        "이 중에서 $$수식$${num2}$$/수식$$장을 뽑아 {bits_cnt} 자리의 자연수를 만들 때, 그 수가 {cond}인 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{cond}는 일의 자리의 수가 {cond}이면 되므로\n"\
        "일의 자리에 올 수 있는 수는 {numbers}의 $$수식$${num3}$$/수식$$가지이고, 그 각각에 대하여 "\
        "{case}"\
        "따라서 구하는 자연수의 개수는\n"\
        "$$수식$$ {multiples}`=`{ans}`$$/수식$$\n\n"
    
    if_shi = "십의 자리에 올 수 있는 숫자는 일의 자리의 수를 제외한 $$수식$${num1}$$/수식$$가지이므로 구하는 경우의 수는\n"
    
    if_bai = "백의 자리에 올 수 있는 숫자는 일의 자리의 수를 제외한 $$수식$${num1}$$/수식$$가지, " + \
        "십의 자리에 올 수 있는 숫자는 일의 자리와 백의 자리에 온 숫자를 제외한 $$수식$${num2}$$/수식$$가지이므로 구하는 경우의 수는\n"
    
    if_qian = "천의 자리에 올 수 있는 숫자는 일의 자리 수를 제외한 $$수식$${num1}$$/수식$$가지, " + \
        "백의 자리에 올 수 있는 숫자는 일의 자리와 천의 자리 수를 제외한 $$수식$${num2}$$/수식$$가지, " + \
        "십의 자리에 올 수 있는 숫자는 일의 자리, 천의 자리, 백의 자리의 수를 제외한 $$수식$${num3}$$/수식$$가지이므로 구하는 경우의 수는\n"

    num1 = np.random.randint(4,10)
    num2 = np.random.randint(2,5)
    cond_ind = np.random.randint(0,2)
    cond = ["홀수", "짝수"][cond_ind]

    nums_1 = ""
    nums_2 = ""

    for i in range(num1):
        if (i+1) % 2 == 0:
            if nums_2 == "":
                nums_2 = nums_2 + "$$수식$$" + str(i+1) + "$$/수식$$"
            else:
                nums_2 = nums_2 + ", $$수식$$" + str(i+1) + "$$/수식$$"
        else:
            if nums_1 == "":
                nums_1 = nums_1 + "$$수식$$" + str(i+1) + "$$/수식$$"
            else:
                nums_1 = nums_1 + ", $$수식$$" + str(i+1) + "$$/수식$$"

    numbers = nums_1 if cond_ind == 0 else nums_2
    num3 = num1 - int(num1/2) if cond_ind == 0 else int(num1/2)

    bits_cnt = ["두", "세", "네"][num2-2]

    if num2 == 2:
        case = if_shi.format(num1=num1-1)
        multiples = "%d`times`%d"%(num3, num1-1)
        ans = num3 * (num1-1)
    elif num2 == 3:
        case = if_bai.format(num1=num1-1, num2=num1-2)
        multiples = "%d`times`%d`times`%d"%(num3, num1-1, num1-2)
        ans = num3 * (num1-1) * (num1-2)
    elif num2 == 4:
        case = if_qian.format(num1=num1-1, num2=num1-2, num3=num1-3)
        multiples = "%d`times`%d`times`%d`times`%d"%(num3, num1-1, num1-2, num1-3)
        ans = num3 * (num1-1) * (num1-2) * (num1-3)
    
    example_list = make_example_by_interval(ans, (num1-1)*(num1-2))

    stem = stem.format(cond=cond, num1=num1, num2=num2, bits_cnt=bits_cnt, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(cond=cond, numbers=numbers, num3=num3, case=case, multiples=multiples, ans=ans)

    return stem, answer, comment


# 2-2-6-45
def numbercases226_Stem_030():
    stem = "$$수식$$1$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 숫자가 각각 하나씩 적힌 "\
        "$$수식$${num1}$$/수식$$개의 공이 들어 있는 주머니에서 $$수식$$2$$/수식$$개를 동시에 뽑아 "\
        "만들 수 있는 두 자리의 자연수 중에서 $$수식$${num2}$$/수식$$번째로 큰 수를 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
        "큰 수부터 나열하므로 십의 자리의 숫자가 $$수식$${num1}$$/수식$$인 경우부터 차례로 생각한다.\n"\
        "{case}"\
        "위의 경우에서 $$수식$${num_}`times`{count}`=`{num3}$$/수식$$(개)이므로 $$수식$${num2}$$/수식$$번째로 큰 수는 "\
        "십의 자리의 숫자가 $$수식$${num4}$$/수식$$인 수 중에서 $$수식$${num5}$$/수식$$번째로 큰 수이다.\n"\
        "따라서 십의 자리의 숫자가 $$수식$${num4}$$/수식$$인 수를 큰 수부터 차례로 나열하면 {numbers}이므로 $$수식$${num2}$$/수식$$번째로 큰 수는 "\
        "$$수식$${ans}$$/수식$$이다.\n\n"
    
    num1 = np.random.randint(5,10)
    num_ = num1 - 1
    total = (num1)*(num1-1)
    num2 = np.random.randint(int(total/4), int(total/2)+1)

    case_format = "({num1}) $$수식$${num2}``BOX~~``$$/수식$$인 경우\n"+ \
        "일의 자리에 올 수 있는 숫자는 $$수식$${num2}$$/수식$$를 제외한 $$수식$${num3}$$/수식$$개이므로 $$수식$${num3}$$/수식$$개이다.\n"

    tmp = num2
    count = 0
    case = ""
    while tmp > (num1-1):
        count = count + 1
        case = case + case_format.format(num1=count, num2=(num1-count+1), num3=num1-1)
        tmp = tmp - (num1-1)
    
    num3 = num_ * count
    num4 = num1 - count
    num5 = tmp

    numbers = ""
    high = num4 * 10 + num1
    i = 0
    while tmp > 0:
        if num1-i == num4:
            i = i + 1
            continue
        if numbers == "":
            numbers = numbers + "$$수식$$" + str(high-i) + "$$/수식$$"
        else:
            numbers = numbers + ", $$수식$$" + str(high-i) + "$$/수식$$"
        ans = high - i
        tmp = tmp - 1
        i = i + 1
    
    if num5 != (num1-1):
        numbers = numbers + ", $$수식$$CDOTS$$/수식$$"
    

    stem = stem.format(num1=num1, num2=num2, num3=num3)
    answer = answer.format(a1=ans)
    comment = comment.format(num1=num1, num2=num2, num3=num3, num4=num4, num5=num5, num_=num_, \
        case=case, count=count, numbers=numbers, ans=ans)

    return stem, answer, comment


# 2-2-6-46
def numbercases226_Stem_031():
    stem = "$$수식$$0`$$/수식$$부터 $$수식$${num1_f}$$/수식$$까지의 숫자가 각각 적힌 $$수식$${num1}$$/수식$$장의 카드 중 "\
        "$$수식$${num2}$$/수식$$장을 뽑아 만들 수 있는 {bits_cnt} 자리의 자연수 중 {cond}의 개수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{case}"\
        "따라서 구하는 {cond}의 개수는\n"\
        "$$수식$$ {plus}`=`{ans}`$$/수식$$\n\n"
    
    case_4 = "({num1}) $$수식$$ {box1} $$/수식$$$$수식$$`{box2}$$/수식$$ {num2} 인 경우 : "+ \
        "$$수식$${num3}`times`{num4}`times`{num5}`=`{ans}$$/수식$$(개)\n"
    case_3 = "({num1}) $$수식$${box1}``$$/수식$$$$수식$${box2}` $$/수식$${num2}인 경우 : "+ \
        "$$수식$${num3}`times`{num4}`=`{ans}$$/수식$$(개)\n"
    box1="BOX{~①~}"
    box2="BOX{~②~}"

    
    num1 = np.random.randint(5,10)
    num1_f = num1-1
    num2 = np.random.randint(3,5)
    cond_ind = np.random.randint(0,2)
    cond = ["홀수", "짝수"][cond_ind]
    bits_cnt = ["세", "네"][num2-3]

    case = ""
    plus = ""
    count = 1
    ans = 0
    if num2 == 3:
        if cond_ind == 0:
            for i in range(num1):
                if i % 2 != 0:
                    case = case + case_3.format(box1=box1,box2=box2,num1=count, num2=i, num3=num1-2, num4=num1-2, ans=(num1-2)**2)
                    count = count + 1
                    ans = ans + (num1-2)**2
                    if plus == "":
                        plus = plus + str((num1-2)**2)
                    else:
                        plus = plus + "`+`" + str((num1-2)**2)
        else:
            for i in range(num1):
                if i % 2 == 0:
                    if i == 0:
                        case = case + case_3.format(box1=box1,box2=box2,num1=count, num2=i, num3=num1-1, num4=num1-2, ans=(num1-2)*(num1-1))
                        plus = plus + str((num1-2)*(num1-1))
                        ans = ans + (num1-2)*(num1-1)
                    else:
                        case = case + case_3.format(box1=box1,box2=box2,num1=count, num2=i, num3=num1-2, num4=num1-2, ans=(num1-2)**2)
                        plus = plus + "`+`" + str((num1-2)**2)
                        ans = ans + (num1-2)**2
                    count = count + 1
    else:
        if cond == 0:
            for i in range(num1):
                if i % 2 != 0:
                    case = case + case_4.format(box1=box1,box2=box2,num1=count, num2=i, num3=num1-2, num4=num1-2, num5=num1-3, ans=((num1-2)**2)*(num1-3))
                    count = count + 1
                    if plus == "":
                        plus = plus + str(((num1-2)**2)*(num1-3))
                    else:
                        plus = plus + "`+`" + str(((num1-2)**2)*(num1-3))
                    ans = ans + ((num1-2)**2)*(num1-3)
        else:
            for i in range(num1):
                if i % 2 == 0:
                    if i == 0:
                        case = case + case_4.format(box1=box1,box2=box2,num1=count, num2=i, num3=num1-1, num4=num1-2, num5=num1-3, ans=(num1-3)*(num1-2)*(num1-1))
                        plus = plus + str((num1-3)*(num1-2)*(num1-1))
                        ans = ans + (num1-3)*(num1-2)*(num1-1)
                    else:
                        case = case + case_4.format(box1=box1,num1=count,box2=box2, num2=i, num3=num1-2, num4=num1-2, num5=num1-3, ans=((num1-2)**2)*(num1-3))
                        plus = plus + "`+`" + str(((num1-3)*(num1-2)**2))
                        ans = ans + (num1-3)*((num1-2)**2)
                    count = count + 1
    
    example_list = make_example_by_interval(ans, (num1-2)*(num1-2) if num2 == 3 else (num1-2)*(num1-2)*(num1-3))

    stem = stem.format(cond=cond, num1=num1, num1_f=num1_f, num2=num2, bits_cnt=bits_cnt, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(box1=box1, box2=box2,cond=cond, case=case, plus=plus, ans=ans)

    return stem, answer, comment


# 2-2-6-47
def numbercases226_Stem_032():
    stem = "{num_from}의 숫자가 각각 하나씩 적힌 $$수식$${num1}$$/수식$$장의 카드 중에서 "\
        "$$수식$$3`$$/수식$$장을 동시에 뽑아 세 자리의 자연수를 만들어 {cond} 수부터 차례로 나열할 때, "\
        "$$수식$${num2}$$/수식$$번째의 수를 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
        "{cond} 수부터 나열하므로 백의 자리의 숫자가 $$수식$${start_num}$$/수식$$인 경우부터 차례로 생각한다.\n"\
        "{case}"\
        "위의 경우에서 $$수식$${num_}`times`{count}`=`{num3}$$/수식$$(개)이므로 $$수식$${num2}$$/수식$$번째의 수는 "\
        "백의 자리의 숫자가 $$수식$${num4}$$/수식$$인 수 중에서 $$수식$${num5}$$/수식$$번째로 {cond} 수이다.\n"\
        "따라서 백의 자리의 숫자가 $$수식$${num4}$$/수식$$인 수를 {cond} 수부터 차례로 나열하면 {numbers}이므로 $$수식$${num2}$$/수식$$번째의 수는 "\
        "$$수식$${ans}$$/수식$$이다.\n\n"

    num1 = np.random.randint(5,10)
    num_ = (num1-1)*(num1-2)
    num2 = np.random.randint(1,4)*num_ + np.random.randint(2,10)
    cond_ind = np.random.randint(0,2)
    cond = ["작은", "큰"][cond_ind]
    start_num = [1, num1][cond_ind]

    num_from = ""
    for i in range(num1):
        if i == 0:
            num_from = num_from + "$$수식$$" + str(i) + "$$/수식$$"
        else:
            num_from = num_from + ", $$수식$$" + str(i) + "$$/수식$$"

    case_format = "({num1}) $$수식$${num2}$$/수식$$ __ __ 인 경우\n"+ \
        "십의 자리에 올 수 있는 숫자는 $$수식$${num2}$$/수식$${j} 제외한 $$수식$${num3}$$/수식$$개, " + \
        "일의 자리에 올 수 있는 숫자는 십의 자리 수와 $$수식$${num2}$$/수식$${j} 제외한 $$수식$${num4}$$/수식$$개이므로\n" + \
        "$$수식$${num3}`times`{num4}`=`{num5}$$/수식$$(개)\n"

    tmp = num2
    count = 0
    case = ""

    if cond_ind == 0:
        while tmp > num_:
            count = count + 1
            j = proc_jo(count, 4)
            case = case + case_format.format(num1=count, j=j, num2=count, num3=num1-1, num4=num1-2, num5=num_)
            tmp = tmp - num_
        
        num3 = num_ * count
        num4 = count + 1
        num5 = tmp

        numbers = ""
        low = num4 * 100
        i = 0
        for i in range(num1):
            if i == num4:
                continue
            for j in range(num1):
                if j == num4 or j ==i:
                    continue
                if numbers == "":
                    numbers = numbers + "$$수식$$" + str(low + i*10 + j) + "$$/수식$$"
                else:
                    numbers = numbers + ", $$수식$$" + str(low + i*10 + j) + "$$/수식$$"
                tmp = tmp - 1
                ans = low + i*10 + j
                if tmp == 0:
                    break
            if tmp == 0:
                break
        
        if num5 != num_:
            numbers = numbers + ", $$수식$$CDOTS$$/수식$$"
    else:
        while tmp > num_:
            count = count + 1
            j = proc_jo(num1-count+1, 4)
            case = case + case_format.format(num1=count, j=j, num2=num1-count+1, num3=num1-1, num4=num1-2, num5=num_)
            tmp = tmp - num_
        
        num3 = num_ * count
        num4 = num1 - count
        num5 = tmp

        numbers = ""
        low = num4 * 100
        i = 0
        for i in range(num1):
            if i == num4:
                continue
            for j in range(num1):
                if j == num4 or j ==i:
                    continue
                if numbers == "":
                    numbers = numbers + "$$수식$$" + str(low + (num1-i)*10 + (num1-j)) + "$$/수식$$"
                else:
                    numbers = numbers + ", $$수식$$" + str(low + (num1-i)*10 + (num1-j)) + "$$/수식$$"
                tmp = tmp - 1
                ans = low + (num1-i)*10 + (num1-j)
                if tmp == 0:
                    break
            if tmp == 0:
                break
        
        if num5 != num_:
            numbers = numbers + ", $$수식$$CDOTS$$/수식$$"
    

    stem = stem.format(num_from=num_from, num1=num1, num2=num2, cond=cond)
    answer = answer.format(a1=ans)
    comment = comment.format(num2=num2, num3=num3, num4=num4, num5=num5, num_=num_, start_num=start_num, \
        case=case, count=count, numbers=numbers, cond=cond, ans=ans)

    return stem, answer, comment


# 2-2-6-48
def numbercases226_Stem_033():
    stem = "$$수식$$1$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 자연수를 이용하여 세 자리 자연수를 만드려고 한다. "\
        "같은 숫자를 여러 번 사용해도 된다고 할 때, 만들 수 있는 세 자리 자연수 중 "\
        "$$수식$${num2}$$/수식$$번째로 {cond} 수를 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
        "작은 수부터 나열하므로 백의 자리의 숫자가 $$수식$$1$$/수식$$인 경우부터 차례로 생각한다.\n"\
        "{case}"\
        "위의 경우에서 $$수식$${num_}`times`{count}`=`{num3}$$/수식$$(개)이므로 $$수식$${num2}$$/수식$$번째의 수는 "\
        "백의 자리의 숫자가 $$수식$${num4}$$/수식$$인 수 중에서 $$수식$${num5}$$/수식$$번째로 {cond} 수이다.\n"\
        "따라서 백의 자리의 숫자가 $$수식$${num4}$$/수식$$인 수를 {cond} 수부터 차례로 나열하면 {numbers}이므로 $$수식$${num2}$$/수식$$번째의 수는 "\
        "$$수식$${ans}$$/수식$$이다.\n\n"

    num1 = np.random.randint(4,9)
    num_ = num1 * num1
    num2 = np.random.randint(1,4)*num_ + np.random.randint(2, 10)
    cond_ind = np.random.randint(0,2)
    cond = ["작은", "큰"][cond_ind]

    case_format = "({num1}) 백의 자리 숫자가 $$수식$${num2}$$/수식$$인 경우\n"+ \
        "십의 자리, 일의 자리에 올 수 있는 숫자는 각각 $$수식$${num3}$$/수식$$가지이므로\n" + \
        "$$수식$${num3}`times`{num3}`=`{num4}$$/수식$$(개)\n"

    tmp = num2
    count = 0
    case = ""

    if cond_ind == 0:
        while tmp > num_:
            count = count + 1
            case = case + case_format.format(num1=count, num2=count, num3=num1, num4=num_)
            tmp = tmp - num_

        num3 = num_ * count
        num4 = count + 1
        num5 = tmp

        numbers = ""
        low = num4 * 100
        i = 0
        for i in range(num1):
            for j in range(num1):
                if numbers == "":
                    numbers = numbers + "$$수식$$" + str(low + i*10 + j) + "$$/수식$$"
                else:
                    numbers = numbers + ", $$수식$$" + str(low + i*10 + j) + "$$/수식$$"
                tmp = tmp - 1
                ans = low + i*10 + j
                if tmp == 0:
                    break
            if tmp == 0:
                break

        if num5 != num_:
            numbers = numbers + ", $$수식$$CDOTS$$/수식$$"
    else:
        while tmp > num_:
            count = count + 1
            case = case + case_format.format(num1=count, num2=num1-count+1, num3=num1, num4=num_)
            tmp = tmp - num_

        num3 = num_ * count
        num4 = num1 - count
        num5 = tmp

        numbers = ""
        low = num4 * 100
        i = 0
        for i in range(num1):
            for j in range(num1):
                if numbers == "":
                    numbers = numbers + "$$수식$$" + str(low + (num1-i)*10 + (num1-j)) + "$$/수식$$"
                else:
                    numbers = numbers + ", $$수식$$" + str(low + (num1-i)*10 + (num1-j)) + "$$/수식$$"
                tmp = tmp - 1
                ans = low + (num1-i)*10 + (num1-j)
                if tmp == 0:
                    break
            if tmp == 0:
                break

        if num5 != num_:
            numbers = numbers + ", $$수식$$CDOTS$$/수식$$"
    

    stem = stem.format(cond=cond, num1=num1, num2=num2)
    answer = answer.format(a1=ans)
    comment = comment.format(num2=num2, num3=num3, num4=num4, num5=num5, num_=num_, \
        case=case, count=count, numbers=numbers, cond=cond, ans=ans)

    return stem, answer, comment


# 2-2-6-49
def numbercases226_Stem_034():
    stem = "{num_from}의 숫자가 각각 하나씩 적힌 $$수식$${num1}$$/수식$$장의 카드 중에서 "\
        "$$수식$$3`$$/수식$$장을 동시에 뽑아 세 자리의 자연수를 만들 때, $$수식$${num2}$$/수식$$보다 "\
        "{cond} 자연수의 개수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${num2}$$/수식$$보다 {cond} 자연수가 되려면 백의 자리에 올 수 있는 숫자는 {poss_nums}이다.\n"\
        "{case1}{case2}{case3}"\
        "따라서 $$수식$${num2}$$/수식$$보다 {cond} 자연수의 개수는\n"\
        "$$수식$${plus}`=`{ans}$$/수식$$\n\n"

    case1_format = "({num1}) $$수식$${num2}``{num3}$$/수식$$ __ 인 경우\n"+ \
        "일의 자리에 올 수 있는 숫자는 {list1}이므로 " + \
        "$$수식$${ans1}$$/수식$$개\n"
    case2_format = "({num1}) $$수식$${num2}$$/수식$$ __ __ 인 경우\n"+ \
        "십의 자리에 올 수 있는 숫자는 {list1}이고, 각각에 대해 " + \
        "일의 자리에 올 수 있는 숫자는 $$수식$${num2}$$/수식$${j} 십의 자리 수를 제외한 $$수식$${one}$$/수식$$개이므로\n" + \
        "$$수식$${ten}`times`{one}`=`{ans2}$$/수식$$개\n"
    case3_format = "({num1}) $$수식$${num2}$$/수식$$이상인 경우\n"+ \
        "백의 자리에 올 수 있는 숫자는 {list1}이고 각각에 대해 " + \
        "십의 자리에 올 수 있는 숫자는 백의 자리 수를 제외한 $$수식$${ten}$$/수식$$개, " + \
        "일의 자리에 올 수 있는 숫자는 백의 자리와 십의 자리 수를 제외한 $$수식$${one}$$/수식$$개이므로\n" + \
        "$$수식$${hund}`times`{ten}`times`{one}`=`{ans3}$$/수식$$개\n"
    case3_format2 = "({num1}) $$수식$${num2}$$/수식$$미만인 경우\n"+ \
        "백의 자리에 올 수 있는 숫자는 {list1}이고 각각에 대해 " + \
        "십의 자리에 올 수 있는 숫자는 백의 자리 수를 제외한 $$수식$${ten}$$/수식$$개, " + \
        "일의 자리에 올 수 있는 숫자는 백의 자리와 십의 자리 수를 제외한 $$수식$${one}$$/수식$$개이므로\n" + \
        "$$수식$${hund}`times`{ten}`times`{one}`=`{ans3}$$/수식$$개\n"

    num1 = np.random.randint(6,10)
    cond_ind = np.random.randint(0,2)
    cond = ["작은", "큰"][cond_ind]

    box1 = "BOX{~~}"
    num_from = ""
    for i in range(num1):
        if i == 0:
            num_from = num_from + "$$수식$$" + str(i) + "$$/수식$$"
        else:
            num_from = num_from + ", $$수식$$" + str(i) + "$$/수식$$"

    # define num2 and possible hundred number(poss_nums)
    poss_nums = ""
    if cond_ind == 0:
        out = random.sample(list(range(num1)), 3)
        while out[0] < 2 or out[0] > 4:
            out = random.sample(list(range(num1)), 3)
        num2 = out[0] * 100 + out[1] * 10 + out[2]
        for i in range(1, out[0]+1):
            if poss_nums == "":
                poss_nums = poss_nums + "$$수식$$" + str(i) + "$$/수식$$"
            else:
                poss_nums = poss_nums + ", $$수식$$" + str(i) + "$$/수식$$"
    else:
        out = random.sample(list(range(num1)), 3)
        while out[0] < num1-3 or out[0] > num1-2:
            out = random.sample(list(range(num1)), 3)
        num2 = out[0] * 100 + out[1] * 10 + out[2]
        for i in range(out[0], num1):
            if poss_nums == "":
                poss_nums = poss_nums + "$$수식$$" + str(i) + "$$/수식$$"
            else:
                poss_nums = poss_nums + ", $$수식$$" + str(i) + "$$/수식$$"


    if cond_ind == 0:
        case_cnt = 1
        ans_list = []
        
        # for case1
        list1 = ""
        ans1 = 0
        for i in range(0, out[2]):
            if i == out[0] or i == out[1]:
                continue
            if list1 == "":
                list1 = list1 + "$$수식$$" + str(i) + "$$/수식$$"
            else:
                list1 = list1 + ", $$수식$$" + str(i) + "$$/수식$$"
            ans1 = ans1 + 1
        if ans1 == 0:
            case1 = ""
        else:
            case1 = case1_format.format(box1=box1,num1=case_cnt, num2=out[0], num3=out[1], list1=list1, ans1=ans1)
            case_cnt = case_cnt + 1
            ans_list.append(ans1)

        # for case2
        list1 = ""
        ten = 0
        for i in range(0, out[1]):
            if i == out[0]:
                continue
            if list1 == "":
                list1 = list1 + "$$수식$$" + str(i) + "$$/수식$$"
            else:
                list1 = list1 + ", $$수식$$" + str(i) + "$$/수식$$"
            ten = ten + 1
        if ten == 0:
            case2 = ""
            ans2 = 0
        else:
            ans2 = ten * (num1 - 2)
            j = proc_jo(out[0], 2)
            case2 = case2_format.format(box1=box1,num1=case_cnt, num2=out[0], j=j, list1=list1, ten=ten, one=num1-2, ans2=ans2)
            case_cnt = case_cnt + 1
            ans_list.append(ans2)

        # for case3
        list1 = ""
        hund = 0
        for i in range(1, out[0]):
            if list1 == "":
                list1 = list1 + "$$수식$$" + str(i) + "$$/수식$$"
            else:
                list1 = list1 + ", $$수식$$" + str(i) + "$$/수식$$"
            hund = hund + 1
        ten = num1 - 1
        one = num1 - 2
        ans3 = hund * ten * one
        case3 = case3_format2.format(num1=case_cnt, num2=(out[0])*100, list1=list1, hund=hund, ten=ten, one=one, ans3=ans3)
        ans_list.append(ans3)
    else:
        case_cnt = 1
        ans_list = []
        
        # for case1
        list1 = ""
        ans1 = 0
        for i in range(out[2]+1, num1):
            if i == out[0] or i == out[1]:
                continue
            if list1 == "":
                list1 = list1 + "$$수식$$" + str(i) + "$$/수식$$"
            else:
                list1 = list1 + ", $$수식$$" + str(i) + "$$/수식$$"
            ans1 = ans1 + 1
        if ans1 == 0:
            case1 = ""
        else:
            case1 = case1_format.format(box1 = box1,num1=case_cnt, num2=out[0], num3=out[1], list1=list1, ans1=ans1)
            case_cnt = case_cnt + 1
            ans_list.append(ans1)

        # for case2
        list1 = ""
        ten = 0
        for i in range(out[1]+1, num1):
            if i == out[0]:
                continue
            if list1 == "":
                list1 = list1 + "$$수식$$" + str(i) + "$$/수식$$"
            else:
                list1 = list1 + ", $$수식$$" + str(i) + "$$/수식$$"
            ten = ten + 1
        if ten == 0:
            case2 = ""
            ans2 = 0
        else:
            ans2 = ten * (num1 - 2)
            j = proc_jo(out[0], 2)
            case2 = case2_format.format(box1=box1,num1=case_cnt, num2=out[0], j=j, list1=list1, ten=ten, one=num1-2, ans2=ans2)
            case_cnt = case_cnt + 1
            ans_list.append(ans2)

        # for case3
        list1 = ""
        hund = 0
        for i in range(out[0]+1, num1):
            if list1 == "":
                list1 = list1 + "$$수식$$" + str(i) + "$$/수식$$"
            else:
                list1 = list1 + ", $$수식$$" + str(i) + "$$/수식$$"
            hund = hund + 1
        ten = num1 - 1
        one = num1 - 2
        ans3 = hund * ten * one
        case3 = case3_format.format(num1=case_cnt, num2=(out[0]+1)*100, list1=list1, hund=hund, ten=ten, one=one, ans3=ans3)
        ans_list.append(ans3)

    # final plus
    plus = ""
    for i in range(case_cnt):
        if plus == "":
            plus = plus + str(ans_list[i])
        else:
            plus = plus + "`+`" + str(ans_list[i])
    ans = ans1 + ans2 + ans3

    example_list = make_example_by_interval(ans, (num1-2) if ans2 == 0 else ans2)

    stem = stem.format(num_from=num_from, num1=num1, num2=num2, cond=cond, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num2=num2, box1=box1,cond=cond, poss_nums=poss_nums, \
        case1=case1, case2=case2, case3=case3, plus=plus, ans=ans)

    return stem, answer, comment


# 2-2-6-50
def numbercases226_Stem_035():
    stem = "$$수식$${num1}$$/수식$$명의 후보 중에서 {lists}{j} $$수식$$1`$$/수식$$명씩 뽑는 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${num1}$$/수식$$명의 후보 중에서 {lists}를 $$수식$$1`$$/수식$$명씩 뽑는 경우의 수이므로\n"\
        "$$수식$${multiples}`=`{ans}$$/수식$$\n\n"

    job_list = [["회장", "부회장", "총무"], ["반장", "부반장", "서기"], ["대통령", "부통령", "민정수석"], ["교장", "교감", "학년부장"]]
    job_ind = np.random.randint(0,4)

    num1 = np.random.randint(4,9)

    lists = ""
    for i in range(3):
        if i == 0:
            lists = lists + job_list[job_ind][i]
        else:
            lists = lists + ", " + job_list[job_ind][i]
    j = proc_jo(job_list[job_ind][2], 4)

    multiples = ""
    ans = 1
    for i in range(3):
        if i == 0:
            multiples = multiples + str(num1-i)
        else:
            multiples = multiples + "`times`" + str(num1-i)
        ans = ans * (num1-i)

    example_list = make_example_by_interval(ans, num1*(num1-1))

    stem = stem.format(lists=lists, num1=num1, j=j,\
            ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, lists=lists, multiples=multiples, ans=ans)

    return stem, answer, comment


# 2-2-6-51
def numbercases226_Stem_036():
    stem = "{std_str} $$수식$${num1}$$/수식$$명의 후보 중에서 {lists}{j1} 각각 $$수식$$1`$$/수식$$명씩 뽑을 때, "\
        "{name}가 {job}에 뽑히는 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{name}를 제외한 $$수식$${num2}$$/수식$$명 중에서 {lists_except}를 각각 $$수식$$1`$$/수식$$명씩 "\
        "뽑으면 되므로 구하는 경우의 수는\n"\
        "$$수식$${num2}`times{num3}`=`{ans}`$$/수식$$\n\n"

    job_list = [["회장", "부회장", "총무"], ["반장", "부반장", "서기"], ["대통령", "부통령", "민정수석"], ["교장", "교감", "학년부장"]]
    job_ind = np.random.randint(0,4)

    lists = ""
    for i in range(3):
        if i == 0:
            lists = lists + job_list[job_ind][i]
        else:
            lists = lists + ", " + job_list[job_ind][i]
    j1 = proc_jo(job_list[job_ind][2], 4)
    sp_job_ind = np.random.randint(0,3)
    job = job_list[job_ind][sp_job_ind]

    num1 = np.random.randint(4,9)
    num2 = num1 - 1
    num3 = num1 - 2
    ans = num2 * num3

    std_list = []
    std_str = ""
    for i in range(num1):
        std_list.append("$$수식$$rm%s`$$/수식$$" % chr(65 + i))
        if i == num1-1:
            std_str = std_str + std_list[i]
        else:
            std_str = std_str + std_list[i] + ", "

    name = std_list[np.random.randint(0,num1)]

    lists_except = ""
    for i in range(3):
        if i == sp_job_ind:
            continue
        if lists_except == "":
            lists_except = lists_except + job_list[job_ind][i]
        else:
            lists_except = lists_except + ", " + job_list[job_ind][i]

    example_list = make_example_by_interval(ans, num2*(num3-1))

    stem = stem.format(name=name, j1=j1, num1=num1, std_str=std_str, lists=lists, job=job, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(name=name, lists_except=lists_except, num2=num2, num3=num3, ans=ans)

    return stem, answer, comment


# 2-2-6-52
def numbercases226_Stem_037():
    stem = "$$수식$$1`$$/수식$$번부터 $$수식$${num1}`$$/수식$$번까지의 번호를 가진 $$수식$${num1}`$$/수식$$명의 선수 중에서 "\
        "$$수식$${num2}`$$/수식$$명을 뽑아 각각 {prizes}{j} 주려고 한다. "\
        "이때 $$수식$${num3}`$$/수식$$번 선수가 {prize}{j} 받는 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$${num3}`$$/수식$$번 선수를 제외한 나머지 $$수식$${num4}$$/수식$$명의 선수 중에서 "\
        "$$수식$${num5}`$$/수식$$명을 뽑아 {prizes_except}{j} 주는 경우의 수와 같으므로\n"\
        "$$수식$${multiples}`=`{ans}$$/수식$$\n\n"

    p_num = np.random.randint(1,5)*5
    prize_list = [["금메달", "은메달", "동메달"], ["대상", "최우수상", "우수상", "장려상"], ["{n1}만원".format(n1=p_num*5), "{n2}만원".format(n2=p_num*3), "{n3}만원".format(n3=p_num)]]
    prize_ind = np.random.randint(0,3)
    j = proc_jo(prize_list[prize_ind][0], 4)
    
    num2 = len(prize_list[prize_ind])
    sp_prize_ind = np.random.randint(0,num2)
    prize = prize_list[prize_ind][sp_prize_ind]

    num1 = np.random.randint(6,13)
    num3 = np.random.randint(1,num1+1)
    num4 = num1 - 1
    num5 = num2 - 1

    prizes = ""
    prizes_except = ""

    for i in range(num2):
        if prizes == "":
            prizes = prizes + prize_list[prize_ind][i]
        else:
            prizes = prizes + ", " + prize_list[prize_ind][i]

    for i in range(num2):
        if i == sp_prize_ind:
            continue
        if prizes_except == "":
            prizes_except = prizes_except + prize_list[prize_ind][i]
        else:
            prizes_except = prizes_except + ", " + prize_list[prize_ind][i]

    multiples = ""
    ans = 1
    for i in range(num5):
        if i == 0:
            multiples = multiples + str(num4-i)
        else:
            multiples = multiples + "`times`" + str(num4-i)
        ans = ans * (num4-i)

    example_list = make_example_by_interval(ans, num4*(num4-1))

    stem = stem.format(prizes=prizes, prize=prize, j=j, num1=num1, num2=num2, num3=num3, \
            ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(prizes_except=prizes_except, j=j, num3=num3, num4=num4, num5=num5, multiples=multiples, ans=ans)

    return stem, answer, comment


# 2-2-6-53
def numbercases226_Stem_038():
    stem = "$$수식$${num1}$$/수식$$명의 후보 {std_str} 중에서 {job} $$수식$${num2}`$$/수식$$명을 뽑을 때, "\
        "{name}가 뽑히는 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{name}를 제외한 $$수식$${num3}$$/수식$$명 중에서 {job} $$수식$${num4}$$/수식$$명을 뽑아야 하므로 "\
        "구하는 경우의 수는?\n"\
        "$$수식$${multiples}`=`{ans}`$$/수식$$\n\n"

    job_list = ["대표", "주번", "부원", "당선자"]
    job_ind = np.random.randint(0,4)
    job = job_list[job_ind]

    num1 = np.random.randint(4,9)
    num2 = np.random.randint(3,4 if num1 == 4 else 5)
    num3 = num1 - 1
    num4 = num2 - 1

    std_list = []
    std_str = ""
    for i in range(num1):
        std_list.append("$$수식$$rm%s`$$/수식$$" % chr(65 + i))
        if i == num1-1:
            std_str = std_str + std_list[i]
        else:
            std_str = std_str + std_list[i] + ", "

    name = std_list[np.random.randint(0,num1)]

    ans_list = combination(num3, num4)
    ans = ans_list[0]
    if ans == -1:
        ans = num3
    multiples = ans_list[1]

    example_list = make_example_by_interval(ans, num3)

    stem = stem.format(name=name, num1=num1, num2=num2, std_str=std_str, job=job, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(name=name, job=job, num3=num3, num4=num4, multiples=multiples, ans=ans)

    return stem, answer, comment


# 2-2-6-54
def numbercases226_Stem_039():
    stem = "{name1}학생 $$수식$${num1}$$/수식$$명, {name2}학생 $$수식$${num2}$$/수식$$명으로 이루어진 모둠에서 "\
        "{name1}학생 $$수식$${num3}$$/수식$$명, {name2}학생 $$수식$${num4}$$/수식$$명을 {job}{j} 뽑는 경우의 수를 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$가지\n"
    comment = "(해설)\n"\
        "{name1}학생 $$수식$${num1}$$/수식$$명 중에서 {job} $$수식$${num3}$$/수식$$명을 뽑는 경우의 수는\n"\
        "$$수식$${multiples1}{equals1}{ans1}$$/수식$$\n"\
        "{name2}학생 $$수식$${num2}$$/수식$$명 중에서 {job} $$수식$${num4}$$/수식$$명을 뽑는 경우의 수는\n"\
        "$$수식$${multiples2}{equals2}{ans2}`$$/수식$$이므로 구하는 경우의 수는\n"\
        "$$수식$${ans1}`times`{ans2}`=`{a1}`$$/수식$$\n\n"

    name_ind = np.random.randint(0,3)
    name1 = ["여", "1학년 ", "1반 "][name_ind]
    name2 = ["남", "2학년 ", "2반 "][name_ind]

    out = random.sample(list(range(3,8)), 2)
    num1 = out[0]
    num2 = out[1]
    num3 = np.random.randint(1,num1-1)
    num4 = np.random.randint(1,num2-1)
    while num4 == num3:
        num4 = np.random.randint(1,num2-1 if num2 != 3 else 3)

    job_list = ["대표", "주번"]
    job_ind = np.random.randint(0,2)
    job = job_list[job_ind]
    j = "으로" if bool_jo(job) else "로"

    ans_list1 = combination(num1, num3)
    ans1 = ans_list1[0]
    if ans1 == -1:
        ans1 = num1
        equals1 = ""
        multiples1 = ""
    else:
        equals1 = "`=`"
        multiples1 = ans_list1[1]

    ans_list2 = combination(num2, num4)
    ans2 = ans_list2[0]
    if ans2 == -1:
        ans2 = num2
        equals2 = ""
        multiples2 = ""
    else:
        equals2 = "`=`"
        multiples2 = ans_list2[1]

    a1 = ans1 * ans2

    stem = stem.format(name1=name1, name2=name2, num1=num1, num2=num2, num3=num3, num4=num4, j=j, job=job)
    answer = answer.format(a1=a1)
    comment = comment.format(name1=name1, name2=name2, num1=num1, num2=num2, num3=num3, num4=num4, job=job, \
        multiples1=multiples1, ans1=ans1, equals1=equals1, multiples2=multiples2, ans2=ans2, equals2=equals2, a1=a1)

    return stem, answer, comment


# 2-2-6-55
def numbercases226_Stem_040():
    stem = "$$수식$$1`$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 자연수가 각각 하나씩 적힌 $$수식$${num1}$$/수식$$개의 공이 주머니에 들어 있다. "\
        "이 주머니에서 $$수식$${num2}$$/수식$$개의 공을 꺼낼 때, 두 번째로 작은 숫자가 $$수식$${num3}$$/수식$$인 경우의 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"                                                                                                                                           
    comment = "(해설)\n"\
        "$$수식$$1`$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 자연수 중 두 번째로 작은 숫자가 $$수식$${num3}$$/수식$$이면 "\
        "가장 작은 숫자{explain} $$수식$${ans1}$$/수식$$이다.\n"\
        "{case2}\n"\
        "따라서, $$수식$${ans1}`times`{ans2}`=`{ans}`$$/수식$$\n\n"


    num1 = np.random.randint(5,9)
    num2 = np.random.randint(4,5 if num1 == 5 else 6)
    num3 = np.random.randint(2,num1-num2+3)

    if num3 == 2:
        explain = "는"
        ans1 = 1 
    else:
        nums = ""
        for i in range(num3-1):
            if nums == "":
                nums = nums + "$$수식$$" + str(i+1) + "$$/수식$$"
            else:
                nums = nums + ", $$수식$$" + str(i+1) + "$$/수식$$"
        explain = "를 구하는 경우의 수는 {nums} 중 $$수식$$1$$/수식$$개를 선택하는 경우이므로".format(nums=nums)
        ans1 = num3-1

    case2_1 = "나머지 숫자는 {lists}{j} 되어야 하므로 경우의 수는 $$수식$$1$$/수식$$이다."
    case2_2 = "나머지 숫자를 결정하는 경우의 수는 {lists} 중 {diff}$$수식$${num}$$/수식$$개를 선택하는 경우로 " + \
        "{multiple}{equal}{ans2_str}이다."


    lists = ""
    for i in range(num1-num3):
        if lists == "":
            lists = lists + "$$수식$$" + str(num3+i+1) + "$$/수식$$"
        else:
            lists = lists + ", $$수식$$" + str(num3+i+1) + "$$/수식$$"
        j = proc_jo(num3+i+1, 0)

    if (num2-2) == (num1-num3):
        case2 = case2_1.format(lists=lists, j=j)
        ans2 = 1
    else:
        if num2-2 == 1:
            diff = ""
            num = 1
            multiple = ""
            equal = ""
            ans2_str = "$$수식$$" + str(num1-num3) + "$$/수식$$"
            ans2 = num1-num3
        else:
            diff = "서로 다른 "
            num = num2-2
            ans_list = combination(num1-num3, num2-2)
            multiple = "\n" + "$$수식$$" + ans_list[1]
            equal = "`=`"
            ans2_str = str(ans_list[0]) + "$$/수식$$"
            ans2 = ans_list[0]
        case2 = case2_2.format(lists=lists, num=num, diff=diff, multiple=multiple, equal=equal, ans2_str=ans2_str)

    ans = ans1 * ans2
    example_list = make_example_by_interval(ans, ans2)

    stem = stem.format(num1=num1, num2=num2, num3=num3, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num3=num3, explain=explain, case2=case2, ans1=ans1, ans2=ans2, ans=ans)

    return stem, answer, comment


# 2-2-6-58
def numbercases226_Stem_041():
    stem = "$$수식$${num1}$$/수식$$개의 팀이 참가한 어느 {game} 경기의 경기 진행 방식은 다음과 같다.\n"\
        "$$표$$(가) $$수식$${num1}$$/수식$$개의 팀을 $$수식$${num2}$$/수식$$개 팀씩 $$수식$${num3}$$/수식$$개의 조로 나누어 각 조에서 리그전을 한다.\n"\
        "(나) 각 조의 상위 $$수식$${num4}$$/수식$$개의 팀이 $$수식$${num5}$$/수식$$강에 진출하여 토너먼트를 한다.\n"\
        "(다) 결승전에서 이긴 팀이 우승한다.$$/표$$\n"\
        "이때 전체 경기 수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "각 조에 속한 $$수식$${num2}$$/수식$$개 팀이 리그전을 할 때, 각 조의 경기 수는\n"\
        "$$수식$${multiples}`=`{ans1_1}`$$/수식$$\n"\
        "이므로 리그전의 경기 수는 $$수식$${ans1_1}`times`2`=`{ans1}`$$/수식$$\n"\
        "$$수식$${num5}$$/수식$$개의 팀의 토너먼트 경기 수는 $$수식$${plus}`=`{ans2}`$$/수식$$\n"\
        "따라서 구하는 전체 경기 수는\n"\
        "$$수식$${ans1}`+`{ans2}`=`{ans}`$$/수식$$\n\n"

    game_list = ["축구", "야구", "농구"]
    game_ind = np.random.randint(0,3)
    game = game_list[game_ind]

    num1 = [8, 16, 32][np.random.randint(0,3)]
    if num1 == 8:
        num2 = 4
    else:
        num2 = [4, 8][np.random.randint(0,2)]

    num3 = int(num1/num2)
    num4 = int(num2/2)
    num5 = num3*num4

    ans_list = combination(num2, 2)
    ans1_1 = ans_list[0]
    multiples = ans_list[1]
    ans1 = ans1_1 * 2

    plus = ""
    ans2 = 0
    tmp = num5
    while tmp != 1:
        tmp = int(tmp/2)
        if plus == "":
            plus = plus + str(tmp)
        else:
            plus = plus + "`+`" + str(tmp)
        ans2 = ans2 + tmp
    
    ans = ans1 + ans2
    example_list = make_example_by_interval(ans, ans2)

    stem = stem.format(game=game, num1=num1, num2=num2, num3=num3, num4=num4, num5=num5, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num2=num2, num5=num5, multiples=multiples, plus=plus, \
        ans1_1=ans1_1, ans1=ans1, ans2=ans2, ans=ans)

    return stem, answer, comment


# 2-2-6-61
def numbercases226_Stem_042():
    stem = "$$수식$$1`$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 자연수가 각각 적힌 $$수식$${num1}$$/수식$$장의 카드 중에서 "\
        "한 장을 뽑을 때, $$수식$${num2}$$/수식$$의 배수가 적힌 카드가 나올 확률을 구하시오.\n"
    answer = "(답): $$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n"\
        "모든 경우의 수는 $$수식$${num1}$$/수식$$\n"\
        "$$수식$${num2}$$/수식$$의 배수가 적힌 카드가 나오는 경우는 {ans_lists}의 $$수식$${ans1}$$/수식$$가지\n"\
        "따라서 구하는 확률은"\
        "$$수식$${fraction}{equal}{a1}$$/수식$$이다.\n\n"

    num1 = np.random.randint(3, 10) * 4
    num2 = np.random.randint(2,7)

    ans1 = num1 // num2
    
    ans_lists = ""
    if ans1 < 7:
        for i in range(ans1):
            ans_lists = ans_lists + "$$수식$$" + str((i+1)*num2) + "$$/수식$$"
            if i != ans1 -1:
                ans_lists = ans_lists + ", "
    else:
        ans_lists = ans_lists + "$$수식$$" + str(num2) + "$$/수식$$" + ", " + "$$수식$$" + str(2*num2) + "$$/수식$$" + \
             ", " + "$$수식$$CDOTS$$/수식$$" + ", " + "$$수식$$" + str(ans1*num2) + "$$/수식$$"

    cont = ctr_frac(ans1, num1)
    if cont[0] == -1:
        fraction = ""
        equal = ""
        a1 = "{%d} over {%d}" % (ans1, num1)
    else:
        fraction = "{%d} over {%d}" % (ans1, num1)
        equal = "`=`"
        a1 = "{%d} over {%d}" % (cont[0], cont[1])
    
    stem = stem.format(num1=num1, num2=num2)
    answer = answer.format(a1=a1)
    comment = comment.format(num2=num2, num1=num1, ans1=ans1, ans_lists=ans_lists, fraction=fraction, equal=equal, a1=a1)

    return stem, answer, comment


# 2-2-6-62
def numbercases226_Stem_043():
    stem = "한 개의 주사위를 두 번 던질 때, "\
        "나오는 눈의 수의 합이 $$수식$${num1}$$/수식$$ 이하가 될 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "모든 경우의 수는 $$수식$$6`times`6`=`36`$$/수식$$\n"\
        "눈의 수의 합이 $$수식$${num1}$$/수식$$ 이하인 경우는\n"\
        "$$수식$${answer_pair1}$$/수식$$의 $$수식$${ans1}$$/수식$$가지이다.\n"\
        "따라서 구하는 확률은 "\
        "$$수식$${frac}{equal}{ans}$$/수식$$\n\n"

    num1 = np.random.randint(3,7)

    answer_pair1 = ""
    ans1 = 0

    for i in range(6):
        for j in range(6):
            if (i+1) + (j+1) <= num1:
                if ans1%5==0 and ans1 != 0:
                    answer_pair1 = answer_pair1 + "$$/수식$$\n$$수식$$"
                answer_pair1 = answer_pair1 + "(%d, %d)`````" % (i+1, j+1)
                ans1 = ans1 + 1

    cont = ctr_frac(ans1, 36)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans1, 36)
        ans_list = [ans1, 36]
    else:
        frac = "{%d} over {%d}" % (ans1, 36)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    example_list = make_fraction_example(ans_list[0], ans_list[1], 12)

    stem = stem.format(num1=num1, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, answer_pair1=answer_pair1, ans1=ans1, frac=frac, equal=equal, ans=ans)

    return stem, answer, comment


# 2-2-6-64
def numbercases226_Stem_044():
    stem = "{name1}{j}학생 $$수식$${num1}$$/수식$$명, {name2}{j}학생 $$수식$${num2}$$/수식$$명을 "\
        "한 줄로 세울 때, {name}{j}학생끼리 이웃하여 서게 될 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "모든 경우의 수는\n"\
        "$$수식$${multiples1}=`{ans1}`$$/수식$$\n"\
        "{name}{j}학생끼리 이웃하여 서는 경우의 수는 {name}{j}학생들을 한 명으로 생각하면\n"\
        "$$수식$${multiples2}`=`{ans2}`$$/수식$$\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${frac}{equal}{ans}$$/수식$$\n\n"

    name_ind = np.random.randint(0,3)    
    name1 = ["여", "1학년", "1반"][name_ind]
    name2 = ["남", "2학년", "2반"][name_ind]
    j = ["", " ", " "][name_ind]

    sp_ind = np.random.randint(0,2)
    name = [name1, name2][sp_ind]
    
    num1 = np.random.randint(2,4)
    num2 = np.random.randint(2,5)
    num_list = [num1, num2]

    multiples1 = ""
    ans1 = 1
    for i in range(num1 + num2):
        if i == 0:
            multiples1 = "%d"%(i+1) + multiples1
        else:
            multiples1 = "%d`times`"%(i+1) + multiples1
        ans1 = ans1 * (i+1)

    multiples2 = ""
    ans2 = 1
    for i in range(num_list[1-sp_ind]+1):
        if i == 0:
            multiples2 = "%d"%(i+1) + multiples2
        else:
            multiples2 = "%d`times`"%(i+1) + multiples2
        ans2 = ans2 * (i+1)

    m = ""
    for i in range(num_list[sp_ind]):
        if i == 0:
            m = "%d"%(i+1) + m
        else:
            m = "%d`times`"%(i+1) + m
        ans2 = ans2 * (i+1)
    
    multiples2 = "(" + multiples2 + ")`times`(" + m + ")"

    cont = ctr_frac(ans2, ans1)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans2, ans1)
        ans_list = [ans2, ans1]
    else:
        frac = "{%d} over {%d}" % (ans2, ans1)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    example_list = make_fraction_example(ans_list[0], ans_list[1], (num1+num2)*(num1+num2-1))

    stem = stem.format(name1=name1, name2=name2, name=name, j=j, num1=num1, num2=num2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(name=name, j=j, multiples1=multiples1, ans1=ans1, multiples2=multiples2, ans2=ans2, frac=frac, equal=equal, ans=ans)
    return stem, answer, comment


# 2-2-6-66
def numbercases226_Stem_045():
    stem = "한 개의 주사위를 두 번 던져서 처음에 나오는 눈의 수를 $$수식$$x`$$/수식$$, "\
        "나중에 나오는 눈의 수를 $$수식$$y`$$/수식$$라 할 때, "\
        "$$수식$$y`=`{num1}x`+`{num2}$$/수식$$일 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "모든 경우의 수는 $$수식$$6`times`6`=`36`$$/수식$$\n"\
        "$$수식$$y`=`{num1}x`+`{num2}$$/수식$$을 만족시키는 순서쌍 $$수식$$ (x,`````y )` $$/수식$$는\n"\
        "$$수식$${answer_pair}$$/수식$$  "\
        "이므로 구하는 확률은 $$수식$${frac}{equal}{ans}$$/수식$$이다.\n\n"

    num1 = np.random.randint(1,4)
    num2 = np.random.randint(1,4)

    answer_pair=""
    ans1 = 0

    for i in range(6):
            for j in range(6):
                if(num1 * (i+1) + num2 == (j+1)):
                    answer_pair = answer_pair + "(%d, %d)`````" % (i+1, j+1)
                    ans1 = ans1 + 1
    
    cont = ctr_frac(ans1, 36)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans1, 36)
        ans_list = [ans1, 36]
    else:
        frac = "{%d} over {%d}" % (ans1, 36)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    example_list = make_fraction_example(ans_list[0], ans_list[1], 36)

    stem = stem.format(num1=('' if num1 == 1 else num1), num2=num2, \
                ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=('' if num1 == 1 else num1), num2=num2, answer_pair=answer_pair, frac=frac, equal=equal, ans=ans)

    return stem, answer, comment


# 2-2-6-67
def numbercases226_Stem_046():
    stem = "두 개의 주사위 $$수식$$rmA$$/수식$$, $$수식$$rmB$$/수식$$를 동시에 던져서 $$수식$$rmA$$/수식$$ 주사위에서 "\
        "나오는 눈의 수를 $$수식$$x`$$/수식$$, "\
        "$$수식$$rmB$$/수식$$ 주사위에서 나오는 눈의 수를 $$수식$$y`$$/수식$$라 할 때, "\
        "$$수식$${num1}x`+`{num2}y`{inequality}`{num3}$$/수식$$일 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "모든 경우의 수는 $$수식$$6`times`6`=`36`$$/수식$$\n"\
        "$$수식$${num1}x`+`{num2}y`{inequality}`{num3}$$/수식$$을 만족시키는 순서쌍 $$수식$$ (x,`````y )` $$/수식$$는\n"\
        "$$수식$${answer_pair}$$/수식$$로 $$수식$${ans1}$$/수식$$개이므로\n"\
        "구하는 확률은 $$수식$${frac}{equal}{ans}$$/수식$$이다.\n\n"


    ineq_list = ["PREC", "LEQ", "SUCC", "GEQ"]
    ineq_ind = np.random.randint(0,4)
    inequality = ineq_list[ineq_ind]

    num1 = np.random.randint(2,6)
    num2 = np.random.randint(1,4)
    num3 = num1 * np.random.randint(2,5) + num2 * np.random.randint(2,5)

    answer_pair = ""
    ans1 = 0
    answer_list = []
    if ineq_ind == 0:
        for i in range(6):
            for j in range(6):
                if(num1 * (i+1) + num2 * (j+1) < num3):
                    answer_pair = answer_pair + "(%d, %d)`````" % (i+1, j+1)
                    answer_list.append([i+1, j+1])
                    ans1 = ans1 + 1        
    elif ineq_ind == 1:
        for i in range(6):
            for j in range(6):
                if(num1 * (i+1) + num2 * (j+1) <= num3):
                    answer_pair = answer_pair + "(%d, %d)`````" % (i+1, j+1)
                    answer_list.append([i+1, j+1])
                    ans1 = ans1 + 1
    elif ineq_ind == 2:
        for i in range(6):
            for j in range(6):
                if(num1 * (i+1) + num2 * (j+1) > num3):
                    answer_pair = answer_pair + "(%d, %d)`````" % (i+1, j+1)
                    answer_list.append([i+1, j+1])
                    ans1 = ans1 + 1
    elif ineq_ind == 3:
        for i in range(6):
            for j in range(6):
                if(num1 * (i+1) + num2 * (j+1) >= num3):
                    answer_pair = answer_pair + "(%d, %d)`````" % (i+1, j+1)
                    answer_list.append([i+1, j+1])
                    ans1 = ans1 + 1

    if ans1 > 10:
        answer_pair = "(%d, %d)`````" % (answer_list[0][0], answer_list[0][1]) + "(%d, %d)`````" % (answer_list[1][0], answer_list[1][1]) + \
            "(%d, %d)`````" % (answer_list[2][0], answer_list[2][1]) + "CDOTS`````" + "(%d, %d)`````" % (answer_list[ans1-1][0], answer_list[ans1-1][1])
    
    cont = ctr_frac(ans1, 36)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans1, 36)
        ans_list = [ans1, 36]
    else:
        frac = "{%d} over {%d}" % (ans1, 36)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    example_list = make_fraction_example(ans_list[0], ans_list[1], 36)

    stem = stem.format(num1=('' if num1 == 1 else num1), num2=('' if num2 == 1 else num2), num3=num3, inequality=inequality, \
                ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=('' if num1 == 1 else num1), num2=('' if num2 == 1 else num2), num3=num3, inequality=inequality, answer_pair=answer_pair, \
        ans1=ans1, frac=frac, equal=equal, ans=ans)

    return stem, answer, comment


# 2-2-6-68
def numbercases226_Stem_047():
    stem = "한 개의 주사위를 두 번 던져서 처음에 나오는 눈의 수를 $$수식$$a`$$/수식$$, "\
        "나중에 나오는 눈의 수를 $$수식$$b`$$/수식$$라 할 때, "\
        "연립방정식 $$수식$${sss}$$/수식$$의 해가 없을 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "모든 경우의 수는 $$수식$$6`times`6`=`36`$$/수식$$\n"\
        "연립방정식 $$수식$${sss}$$/수식$$이 해가 없으려면\n"\
        "$$수식$${res_eq}`````THEREFORE``a`=`{ansa}$$/수식$$, $$수식$$b`!=`{ansb}$$/수식$$ \n"\
        "이를 만족시키는 순서쌍 $$수식$$ (a,`````b )` $$/수식$$는\n"\
        "$$수식$${answer_pair}$$/수식$$\n"\
        "이므로 구하는 확률은 $$수식$${frac}{equal}{ans}$$/수식$$이다.\n\n"

    num1 = np.random.randint(1,4)
    num2 = np.random.randint(1,3)
    num3 = np.random.randint(1,5)
    num4 = num1 * np.random.randint(2,4)

    if num1==1:
        n1=""
    else:
        n1=num1;

    if num2==1:
        n2=""
    else:
        n2=num2;

    if num3==3:
        n3=""
    else:
        n3=num3;

    if num4==4:
        n4=""
    else:
        n4=num4;
 
    sss="{cases{``{%s}x`+`{%s}y`=`{%s}#``{%s}x`+`ay`=`b}}"%(n1,n2,n3,n4)
    equations = "{" + "``{n1}x`+`{n2}y`=`{n3}#``{n4}x`+`ay`=`b".format(n1="" if num1 == 1 else num1, n2="" if num2 == 1 else num2, n3=num3, n4="" if num4 == 1 else num4) + "}"
    res_eq = "{%d} over {%d} `=` {%d} over {%s} `!=` {%d} over {%s}" % (num1, num4, num2, "rma", num3, "rmb")
    ansa = int(num2 * num4 / num1)
    ansb = int(num3 * num4 / num1)
    #sss="{cases{equation}}"

    answer_pair=""
    ans1 = 0

    for j in range(6):
        if (j+1) != ansb:
            answer_pair = answer_pair + "(%d, %d)`````" % (ansa, j+1)
            ans1 = ans1 + 1
    
    cont = ctr_frac(ans1, 36)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans1, 36)
        ans_list = [ans1, 36]
    else:
        frac = "{%d} over {%d}" % (ans1, 36)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    example_list = make_fraction_example(ans_list[0], ans_list[1], 36)

    stem = stem.format(sss=sss,equations=equations,ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(sss=sss,equations=equations, res_eq=res_eq, ansa=ansa, ansb=ansb, answer_pair=answer_pair, frac=frac, equal=equal, ans=ans)

    return stem, answer, comment


# 2-2-6-69
def numbercases226_Stem_048():
    stem = "수직선의 원점 위에 점 $$수식$$rmP`$$/수식$$가 있다. 동전 $$수식$$1`$$/수식$$개를 던져서 앞면이 나오면 "\
        "점 $$수식$$rmP`$$/수식$$를 양의 방향으로 $$수식$$1`$$/수식$$만큼, 뒷면이 나오면 "\
        "점 $$수식$$rmP`$$/수식$$를 음의 방향으로 $$수식$$1`$$/수식$$만큼 이동시킨다. 동전을 $$수식$${num1}$$/수식$$번 던져 "\
        "점 $$수식$$rmP`$$/수식$$를 이동시킬 때, 점 $$수식$$rmP`$$/수식$$의 좌표가 $$수식$${num2}$$/수식$$일 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "모든 경우의 수는 $$수식$${mult2s}`=`{all_}`$$/수식$$\n"\
        "앞면, 뒷면이 나온 횟수를 각각 $$수식$$x`$$/수식$$, $$수식$$y`$$/수식$$라 하면\n"\
        "$$수식$$x`+`y`=`{num1}$$/수식$$, $$수식$$x`-`y`=`{num2}$$/수식$$\n"\
        "위의 식을 연립하여 풀면 $$수식$$x`=`{ansx}$$/수식$$, $$수식$$y`=`{ansy}$$/수식$$\n"\
        "동전을 $$수식$${num1}$$/수식$$번 던져 앞면이 $$수식$${ansx}$$/수식$$번, 뒷면이 $$수식$${ansy}$$/수식$$번 나오는 경우의 수는 "\
        "동전을 던지는 $$수식$${num1}$$/수식$$번 중에 {min_}이 나오는 $$수식$${minnum}$$/수식$$번의 순서를 결정하는 경우의 수와 일치하므로{e}"\
        "$$수식$${multiples}{equal_}{ans1}$$/수식$$가지\n"\
        "따라서 구하는 확률은 $$수식$${frac}{equal}{ans}$$/수식$$이다.\n\n"

    num1 = np.random.randint(3,7)
    num2 = np.random.randint(-num1+1,num1)
    while num1 % 2 != num2 % 2:
        num2 = np.random.randint(-num1+1,num1)

    mult2s = ""
    for i in range(num1):
        if mult2s == "":
            mult2s = mult2s + "2"
        else:
            mult2s = mult2s + "`times`2"
    all_ = 2 ** num1

    ansx = int((num1+num2)/2)
    ansy = int((num1-num2)/2)

    if ansx <= ansy:
        minnum = ansx
        min_ = "앞면"
    else:
        minnum = ansy
        min_ = "뒷면"

    com = combination(num1, minnum)
    ans1 = com[0]
    equal_ = "`=`"
    e = "\n"
    multiples = com[1]
    if ans1 == -1:
        ans1 = num1
        equal_ = ""
        multiples = ""
        e = " "
    
    
    cont = ctr_frac(ans1, all_)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans1, all_)
        ans_list = [ans1, all_]
    else:
        frac = "{%d} over {%d}" % (ans1, all_)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    example_list = make_fraction_example(ans_list[0], ans_list[1], 16)

    stem = stem.format(num1=num1, num2=num2, \
                ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num2=num2, mult2s=mult2s, all_=all_, ansx=ansx, ansy=ansy, minnum=minnum, min_=min_, \
        multiples=multiples, equal_=equal_, e=e, ans1=ans1, frac=frac, equal=equal, ans=ans)

    return stem, answer, comment



# 2-2-6-70
def numbercases226_Stem_049():
    stem = "두 개의 주사위 $$수식$$rmA$$/수식$$, $$수식$$rmB$$/수식$$를 동시에 던져서 나오는 눈의 수를 각각 "\
        "$$수식$$a$$/수식$$, $$수식$$b$$/수식$$라 할 때, 직선 $$수식$$ ax`+`by`=`{num1}` $$/수식$$가 "\
        "점 $$수식$$ ({num2},`````{num3} )` $$/수식$$을 지날 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "모든 경우의 수는 $$수식$$6`times`6`=`36`$$/수식$$\n"\
        "직선 $$수식$$ ax`+`by`=`{num1}` $$/수식$$가 점 $$수식$$ ({num2},`````{num3} )` $$/수식$$을 지나려면\n"\
        "$$수식$$ a`times`{num2}`+`b`times`{num3}`=`{num1}` $$/수식$$\n"\
        "이를 만족시키는 순서쌍 $$수식$$ (a,`````b )` $$/수식$$를 나타내면\n"\
        "$$수식$${answer_pair}$$/수식$$의 $$수식$${ans1}$$/수식$$가지\n"\
        "따라서 구하는 확률은 $$수식$${frac}{equal}{ans}$$/수식$$이다.\n\n"

    num2 = np.random.randint(2,5)
    num3 = np.random.randint(2,5)
    num1 = np.random.randint(5,10) * max(num2,num3)
    
    answer_pair=""
    ans1 = 0

    for i in range(6):
            for j in range(6):
                if(num2 * (i+1) + num3 * (j+1) == num1):
                    if answer_pair == "":
                        answer_pair = answer_pair + "(%d,`````%d)`````" % (i+1, j+1)
                    else:
                        answer_pair = answer_pair + "`````(%d,`````%d)``" % (i+1, j+1)
                    ans1 = ans1 + 1

    cont = ctr_frac(ans1, 36)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans1, 36)
        ans_list = [ans1, 36]
    else:
        frac = "{%d} over {%d}" % (ans1, 36)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    example_list = make_fraction_example(ans_list[0], ans_list[1], 36)

    stem = stem.format(num1=num1, num2=num2, num3=num3, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num2=num2, num3=num3, answer_pair=answer_pair, ans1=ans1, frac=frac, equal=equal, ans=ans)

    return stem, answer, comment


# 2-2-6-71
def numbercases226_Stem_050():
    stem = "{n1} 공과 {n2} 공이 들어 있는 상자가 있다. 이 상자에서 한 개의 공을 꺼낼 때, {n2} 공일 확률은 $$수식$${p1}$$/수식$$이고, "\
        "처음 상자에 {n1} 공을 {cnt} 개 더 넣은 다음 한 개의 공을 꺼낼 때, {n2} 공일 확률은 $$수식$${p2}$$/수식$$이다. "\
        "처음 상자에 들어 있는 {n2} 공의 개수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{n1} 공과 {n2} 공의 개수를 각각 $$수식$$x$$/수식$$, $$수식$$y$$/수식$$라 하면\n"\
        "$$수식$${eq1}$$/수식$$, $$수식$${eq2}$$/수식$$\n"\
        "$$수식$$THEREFORE```{eq1_1}$$/수식$$, $$수식$${eq2_1}$$/수식$$\n"\
        "위의 식을 연립하여 풀면\n"\
        "$$수식$$x`=`{ansx}$$/수식$$, $$수식$$y`=`{ansy}$$/수식$$\n"\
        "따라서 {n2} 공의 개수는 $$수식$${ansy}$$/수식$$이다.\n\n"

    name = random.sample(["검은", "흰", "노란", "빨간", "파란"],2)
    n1 = name[0]
    n2 = name[1]
    
    cnt_list = ["한", "두", "세"]
    cnt_ind = np.random.randint(0,3)
    cnt = cnt_list[cnt_ind]

    ansx = np.random.randint(4,10)
    ansy = np.random.randint(2,8)

    p1_list = ctr_frac(ansy, ansx+ansy)
    if p1_list[0] == -1:
        p1 = "{%d} over {%d}" % (ansy, ansx+ansy)
        p1_list[0] = ansy
        p1_list[1] = ansx+ansy
    else:
        p1 = "{%d} over {%d}" % (p1_list[0], p1_list[1])
    
    p2_list = ctr_frac(ansy, ansx+ansy+cnt_ind+1)
    if p2_list[0] == -1:
        p2 = "{%d} over {%d}" % (ansy, ansx+ansy+cnt_ind+1)
        p2_list[0] = ansy
        p2_list[1] = ansx+ansy+cnt_ind+1
    else:
        p2 = "{%d} over {%d}" % (p2_list[0], p2_list[1])

    eq1 = "{y} over {x`+`y}`=`%s" % (p1)
    eq2 = "{y} over {x`+`y`+`%d}`=`%s" % (cnt_ind+1,p2)
    eq1_1 = "{n1}y`=`{n2}x`+`{n2}y".format(n1=p1_list[1], n2="" if p1_list[0] == 1 else p1_list[0])
    eq2_1 = "{n1}y`=`{n2}x`+`{n2}y`+`{n3}".format(n1=p2_list[1], n2="" if p2_list[0] == 1 else p2_list[0], n3=p2_list[0]*(cnt_ind+1))

    example_list = make_example_by_interval(ansy, 1)

    stem = stem.format(n1=n1, n2=n2, p1=p1, p2=p2, cnt=cnt, \
                ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, eq1=eq1, eq2=eq2, eq1_1=eq1_1, eq2_1=eq2_1, ansx=ansx, ansy=ansy)

    return stem, answer, comment


# 2-2-6-73
def numbercases226_Stem_051():
    stem = "$$수식$$rmA`$$/수식$$를 포함한 $$수식$${num1}$$/수식$$명의 후보 중에서 {job} $$수식$$2`$$/수식$$명씩 뽑을 때, "\
        "$$수식$$rmA`$$/수식$$가 뽑히지 않을 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "모든 경우의 수는 $$수식$${multiples}`=`{ans1}$$/수식$$\n"\
        "$$수식$$rmA`$$/수식$$가 뽑히는 경우의 수는 $$수식$$rmA`$$/수식$$를 제외한 $$수식$${num2}$$/수식$$명 중에서 "\
        "$$수식$$1$$/수식$$명을 뽑는 경우의 수와 같은 $$수식$${num2}$$/수식$$이므로 $$수식$$rmA`$$/수식$$가 뽑힐 확률은 "\
        "$$수식$${frac}{equal}{ans}$$/수식$$\n"\
        "따라서 구하는 확률은\n $$수식$$1`-`{ans}`=`{rans}$$/수식$$\n\n"

    job_list = ["대표", "주번", "부원", "당선자"]
    job_ind = np.random.randint(0,4)
    job = job_list[job_ind]

    num1 = np.random.randint(3, 11)
    num2 = num1 - 1
    
    com_list = combination(num1, 2)
    ans1 = com_list[0]
    multiples = com_list[1]

    cont = ctr_frac(num2, ans1)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (num2, ans1)
        ans_list = [num2, ans1]
    else:
        frac = "{%d} over {%d}" % (num2, ans1)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    rans = "{%d} over {%d}" % (ans_list[1]-ans_list[0], ans_list[1])

    example_list = make_fraction_example(ans_list[1]-ans_list[0], ans_list[1], int(num1*(num1-1)/2))

    stem = stem.format(num1=num1, job=job, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(multiples=multiples, ans1=ans1, num2=num2, frac=frac, equal=equal, ans=ans, rans=rans)

    return stem, answer, comment


# 2-2-6-74
def numbercases226_Stem_052():
    stem = "{name}{j}는 서로 다른 {obj1} $$수식$${num1}$$/수식$$개와 서로 다른 {obj2} $$수식$${num2}$$/수식$$개를 실수로 섞어 버렸다. "\
        "이 중에서 임의로 $$수식$${num3}$$/수식$$개의 {obj}{j1} 선택할 때, {obj1}{j2} 적어도 한 개 나올 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "모든 경우의 수는 $$수식$${multiples1}`=`{ans1}$$/수식$$\n"\
        "$$수식$${num3}$$/수식$$개의 {obj} 모두 {obj2}{j2} 선택되는 경우의 수는\n"\
        "$$수식$${multiples2}`=`{ans2}$$/수식$$\n"\
        "이므로 그 확률은 "\
        "$$수식$${frac}{equal}{ans}$$/수식$$\n"\
        "따라서 구하는 확률은\n $$수식$$1`-`{ans}`=`{rans}$$/수식$$\n\n"

    name = ["성균", "상균", "병호", "정익", "용권", "성회", "종호"][np.random.randint(0,7)]
    j = proc_jo(name, 3)
    
    obj_ind = np.random.randint(0,2)
    obj = ["건전지", "장난감"][obj_ind]
    obj1 = ["새 건전지", "새 장난감"][obj_ind]
    obj2 = ["폐건전지", "헌 장난감"][obj_ind]
    j1 = proc_jo(obj, 4)
    j2 = proc_jo(obj, 0)

    num1 = np.random.randint(3,6)
    num2 = np.random.randint(3,6)
    num3 = np.random.randint(2,num2)
    
    com_list = combination(num1+num2, num3)
    ans1 = com_list[0]
    multiples1 = com_list[1]

    com2_list = combination(num2, num3)
    ans2 = com2_list[0]
    multiples2 = com2_list[1]

    cont = ctr_frac(ans2, ans1)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans2, ans1)
        ans_list = [ans2, ans1]
    else:
        frac = "{%d} over {%d}" % (ans2, ans1)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    rans = "{%d} over {%d}" % (ans_list[1]-ans_list[0], ans_list[1])

    example_list = make_fraction_example(ans_list[1]-ans_list[0], ans_list[1], int((num1+num2)*(num1+num2-1)/2))

    stem = stem.format(num1=num1, num2=num2, num3=num3, name=name, j=j, j1=j1, j2=j2, obj=obj, obj1=obj1, obj2=obj2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(obj2=obj2, obj=obj, j2=j2, multiples1=multiples1, ans1=ans1, multiples2=multiples2, ans2=ans2, num2=num2, num3=num3, frac=frac, equal=equal, ans=ans, rans=rans)

    return stem, answer, comment


# 2-2-6-75
def numbercases226_Stem_053():
    stem = "서로 다른 {cnt} 개의 주사위를 동시에 던질 때, {cnt} 눈의 수의 합이 $$수식$${num1}$$/수식$$ 이상일 확률을 $$수식$$p`$$/수식$$, "\
        "{cnt} 눈의 수의 곱이 $$수식$${num2}$$/수식$$ 이하일 확률을 $$수식$$q`$$/수식$$라 하자. 이때 $$수식$$q`-`p$$/수식$$의 값을 구하시오.\n"
    answer = "(답): $$수식$$1$$/수식$$\n"
    comment = "(해설)\n"\
        "{cnt} 주사위의 눈의 수의 합은 항상 $$수식$${n1}$$/수식$$이상 $$수식$${n2}$$/수식$$이하이므로 "\
        "눈의 수의 합이 $$수식$${num1}$$/수식$$ 이상일 확률은 $$수식$$0$$/수식$$이다.\n"\
        "{cnt} 주사위의 눈의 수의 곱은 항상 $$수식$${n3}$$/수식$$이하이므로 $$수식$$q`=`1$$/수식$$\n"\
        "$$수식$$THEREFORE```q`-`p`=`1$$/수식$$이다.\n\n"

    cnt_ind = np.random.randint(0,3)
    cnt = ["두", "세", "네"][cnt_ind]
    cnt_num = cnt_ind + 2

    n1 = cnt_num
    n2 = 6 * cnt_num
    n3 = 6 ** cnt_num

    num1 = np.random.randint(n2+1, n2+5)
    num2 = np.random.randint(n3, n3+5)

    stem = stem.format(cnt=cnt, num1=num1, num2=num2)
    comment = comment.format(num1=num1, n1=n1, n2=n2, n3=n3, cnt=cnt)

    return stem, answer, comment


# 2-2-6-76
def numbercases226_Stem_054():
    stem = "{std_str} $$수식$${num1}$$/수식$$명을 일렬로 "\
        "{verb1} 때, {name1}, {name2}가 이웃하여 {verb2} 않을 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "모든 경우의 수는 $$수식$${multiples1}`=`{ans1}$$/수식$$\n"\
        "{name1}, {name2}가 이웃하여 {verb3} 경우의 수는\n"\
        "$$수식$${multiples2}`times`2`=`{ans2}$$/수식$$\n"\
        "이므로 그 확률은 "\
        "$$수식$${frac}{equal}{ans}$$/수식$$\n"\
        "따라서 구하는 확률은\n $$수식$$1`-`{ans}`=`{rans}$$/수식$$\n\n"

    num1 = np.random.randint(5,8)
    num2 = num1 - 1

    std_list = []
    std_str = ""

    for i in range(num1):
        std_list.append("$$수식$$rm%s`$$/수식$$" % chr(65 + i))
        if i == num1-1:
            std_str = std_str + std_list[i]
        else:
            std_str = std_str + std_list[i] + ", "

    out = random.sample(list(range(num1)), 2)
    name1 = std_list[min(out[0], out[1])]
    name2 = std_list[max(out[0], out[1])]

    verb_ind = np.random.randint(0,2)
    verb1 = ["세울", "앉힐"][verb_ind]
    verb2 = ["서지", "앉지"][verb_ind]
    verb3 = ["서는", "앉는"][verb_ind]

    multiples1 = ""
    ans1 = 1

    for i in range(num1):
        if i == 0:
            multiples1 = "%d"%(i+1) + multiples1
        else:
            multiples1 = "%d`times`"%(i+1) + multiples1
        ans1 = ans1 * (i+1)

    multiples2 = ""
    ans2 = 1

    for i in range(num2):
        if i == 0:
            multiples2 = "%d"%(i+1) + multiples2
        else:
            multiples2 = "%d`times`"%(i+1) + multiples2
        ans2 = ans2 * (i+1)
    multiples2 = "(" + multiples2 + ")"
    ans2 = ans2 * 2

    cont = ctr_frac(ans2, ans1)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans2, ans1)
        ans_list = [ans2, ans1]
    else:
        frac = "{%d} over {%d}" % (ans2, ans1)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    rans = "{%d} over {%d}" % (ans_list[1]-ans_list[0], ans_list[1])

    example_list = make_fraction_example(ans_list[1]-ans_list[0], ans_list[1], ans_list[1]*2)

    stem = stem.format(name1=name1, name2=name2, verb1=verb1, verb2=verb2, num1=num1, std_str=std_str, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(name1=name1, name2=name2, verb3=verb3, \
        multiples1=multiples1, ans1=ans1, multiples2=multiples2, ans2=ans2, frac=frac, equal=equal, ans=ans, rans=rans)

    return stem, answer, comment


# 2-2-6-78
def numbercases226_Stem_055():
    stem = "두 개의 주사위 $$수식$$rmA$$/수식$$, $$수식$$rmB$$/수식$$를 동시에 던져서 나오는 눈의 수를 각각 "\
        "$$수식$$a$$/수식$$, $$수식$$b$$/수식$$라 할 때, 직선 $$수식$$ y`=`ax`+`b $$/수식$$가 "\
        "점 $$수식$$ ({num1},`````{num2} )` $$/수식$${j_} 지나지 않을 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "모든 경우의 수는 $$수식$$6`times`6`=`36`$$/수식$$\n"\
        "직선 $$수식$$ y`=`ax`+`b $$/수식$$가 점 $$수식$$ ({num1},`````{num2} )` $$/수식$${j_} 지나려면\n"\
        "$$수식$$ {num1}a+`b`=`{num2}` $$/수식$$\n"\
        "이를 만족시키는 순서쌍 $$수식$$ (a,`````b )` $$/수식$${j_} 나타내면\n"\
        "$$수식$${answer_pair}$$/수식$$\n의 $$수식$${ans1}$$/수식$$가지이므로 그 확률은\n"\
        "$$수식$${frac}{equal}{ans}$$/수식$$\n"\
        "따라서 구하는 확률은\n $$수식$$1`-`{ans}`=`{rans}$$/수식$$\n\n"

    num1 = np.random.randint(2,5)
    num2 = np.random.randint(2,6) * num1
    j_ = proc_jo(num2, 4)
    
    answer_pair=""
    ans1 = 0

    for i in range(6):
            for j in range(6):
                if(num1 * (i+1) + j+1 == num2):
                    if answer_pair == "":
                        answer_pair = answer_pair + "(%d,`````%d)`````" % (i+1, j+1)
                    else:
                        answer_pair = answer_pair + "`````(%d,`````%d)``" % (i+1, j+1)
                    ans1 = ans1 + 1

    cont = ctr_frac(ans1, 36)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans1, 36)
        ans_list = [ans1, 36]
    else:
        frac = "{%d} over {%d}" % (ans1, 36)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    rans = "{%d} over {%d}" % (ans_list[1]-ans_list[0], ans_list[1])

    example_list = make_fraction_example(ans_list[1]-ans_list[0], ans_list[1], 18)

    stem = stem.format(num1=num1, num2=num2, j_=j_, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num2=num2, j_=j_, answer_pair=answer_pair, ans1=ans1, frac=frac, equal=equal, ans=ans, rans=rans)

    return stem, answer, comment


# 2-2-6-79
def numbercases226_Stem_056():
    stem = "{name}{j}네 반 {name1}{j1}학생 $$수식$${num1}$$/수식$$명과 {name2}{j1}학생 $$수식$${num2}$$/수식$$명이 {job}를 하려고 한다. "\
        "이 중에서 대표 $$수식$${num3}$$/수식$$명을 뽑을 때, {name2}{j1}학생이 적어도 한 명 뽑힐 확률을 구하시오\n"
    answer = "(답): $$수식$${rans}$$/수식$$\n"
    comment = "(해설)\n"\
        "전체 학생은 $$수식$${num4}$$/수식$$명이므로 전체 경우의 수는\n$$수식$${multiples1}`=`{ans1}$$/수식$$\n"\
        "{name1}{j1}학생 중 $$수식$${num3}$$/수식$$명을 뽑는 경우의 수는\n"\
        "$$수식$${multiples2}`=`{ans2}$$/수식$$\n"\
        "즉, 대표 $$수식$${num3}$$/수식$$명이 모두 {name1}{j1}학생일 확률은\n"\
        "$$수식$${frac}{equal}{ans}$$/수식$$\n"\
        "따라서 구하는 확률은\n $$수식$$1`-`{ans}`=`{rans}$$/수식$$\n\n"

    name = ["성균", "상균", "병호", "정익", "용권", "성회", "종호"][np.random.randint(0,7)]
    j = proc_jo(name, 3)
    
    name_ind = np.random.randint(0,4)
    name1 = ["여", "1학년", "1반", "초등"][name_ind]
    name2 = ["남", "2학년", "2반", "중"][name_ind]
    j1 = ["", " ", " ", ""][name_ind]

    job = ["환경미화", "달리기", "청소", "발표"][np.random.randint(0,4)]

    num1 = np.random.randint(3,9)
    num2 = np.random.randint(4,7)
    num3 = np.random.randint(2,int(num2/2)+1)
    num4 = num1 + num2
    
    com_list = combination(num4, num3)
    ans1 = com_list[0]
    multiples1 = com_list[1]

    com2_list = combination(num2, num3)
    ans2 = com2_list[0]
    multiples2 = com2_list[1]

    cont = ctr_frac(ans2, ans1)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans2, ans1)
        ans_list = [ans2, ans1]
    else:
        frac = "{%d} over {%d}" % (ans2, ans1)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    rans = "{%d} over {%d}" % (ans_list[1]-ans_list[0], ans_list[1])

    example_list = make_fraction_example(ans_list[1]-ans_list[0], ans_list[1], int((num1+num2)*(num1+num2-1)/2))

    stem = stem.format(num1=num1, num2=num2, num3=num3, name=name, j=j, name1=name1, name2=name2, j1=j1, job=job)
    answer = answer.format(rans=rans)
    comment = comment.format(name1=name1,num3=num3, num4=num4, name2=name2, j1=j1, multiples1=multiples1, ans1=ans1, multiples2=multiples2, ans2=ans2, frac=frac, equal=equal, ans=ans, rans=rans)

    return stem, answer, comment


# 2-2-6-81
def numbercases226_Stem_057():
    stem = "$$수식$$1`$$/수식$$부터 $$수식$$100$$/수식$$까지의 자연수가 각각 하나씩 적힌 $$수식$$100$$/수식$$장의 카드 중에서 한 장을 뽑아 "\
        "나온 수를 분자로 하고 분모가 $$수식$${num1}$$/수식$$인 분수를 소수로 나타낼 때, 유한소수로 나타낼 수 없을 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "나온 수를 $$수식$$x$$/수식$$라 하면\n"\
        "$$수식$${f_frac}`=`{s_frac}$$/수식$$\n"\
        "따라서 $$수식$${f_frac}$$/수식$$를 유한소수로 나타낼 수 있으려면 $$수식$$x$$/수식$$는 $$수식$${mult}{eq}{num3}$$/수식$$의 배수이어야 한다.\n"\
        "이때 $$수식$$1$$/수식$$부터 $$수식$$100$$/수식$$까지의 자연수 중 $$수식$${num3}$$/수식$$의 배수는\n"\
        "{answer_pair}\n"\
        "의 $$수식$${ans1}$$/수식$$개이므로 $$수식$${f_frac}$$/수식$$를 유한소수로 나타낼 수 있는 확률은\n"\
        "$$수식$${frac}{equal}{ans}$$/수식$$\n"\
        "따라서 구하는 확률은\n $$수식$$1`-`{ans}`=`{rans}$$/수식$$\n\n"
    
    n2 = np.random.randint(1,5)
    n5 = np.random.randint(1,3)
    oths = [[3,7], [3, 11], [1, 11], [1, 13], [1, 17], [1, 19]][np.random.randint(0,6)]

    num1 = (2 ** n2) * (5 ** n5) * oths[0] * oths[1]
    num1_str = ""
    mult = ""
    num3 = oths[0] * oths[1]
    for i in range(n2):
        if num1_str == "":
            num1_str = num1_str + "2"
        else:
            num1_str = num1_str + "`times`2"
    if oths[0] != 1:
        num1_str = num1_str + "`times`" + str(oths[0])
        mult = mult + str(oths[0])        
        for i in range(n5):
            num1_str = num1_str + "`times`5"
        num1_str = num1_str + "`times`" + str(oths[1])
        mult = mult + "`times`" + str(oths[1])
        eq = "`=`"
    else:
        for i in range(n5):
            num1_str = num1_str + "`times`5"
        num1_str = num1_str + "`times`" + str(oths[1])
        mult = ""
        eq = ""

    f_frac = "{x} over {%d}" % num1
    s_frac = "{x} over {%s}" % num1_str

    ans1 = 100 // num3
    answer_pair = ""
    for i in range(ans1):
        answer_pair = answer_pair + "$$수식$$" + str((i+1)*num3) + "$$/수식$$"
        if i != ans1 -1:
            answer_pair = answer_pair + ", "

    cont = ctr_frac(ans1, 100)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans1, 100)
        ans_list = [ans1, 100]
    else:
        frac = "{%d} over {%d}" % (ans1, 100)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    rans = "{%d} over {%d}" % (ans_list[1]-ans_list[0], ans_list[1])

    example_list = make_fraction_example(ans_list[1]-ans_list[0], ans_list[1], ans_list[1])

    stem = stem.format(num1=num1, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(f_frac=f_frac, s_frac=s_frac, mult=mult, eq=eq, num3=num3, \
        answer_pair=answer_pair, ans1=ans1, frac=frac, equal=equal, ans=ans, rans=rans)

    return stem, answer, comment


# 2-2-6-82
def numbercases226_Stem_058():
    stem = "$$수식$$1$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 자연수가 각각 하나씩 적힌 "\
        "$$수식$${num1}$$/수식$$장의 카드 중에서 한 장의 카드를 뽑을 때, "\
        "$$수식$${num2}$$/수식$$ 이하 이거나 "\
        "$$수식$${num3}$$/수식$$ 이상의 수가 적힌 카드가 나올 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "카드에 적힌 수가 $$수식$${num2}$$/수식$$ 이하인 경우는\n"\
        "{num2_list}의 $$수식$${ans1}$$/수식$$가지이므로 그 확률은\n"\
        "$$수식$${ans1_frac}$$/수식$$\n"\
        "카드에 적힌 수가 $$수식$${num3}$$/수식$$ 이상인 경우는\n"\
        "{num3_list}의 $$수식$${ans2}$$/수식$$가지이므로 그 확률은\n"\
        "$$수식$${ans2_frac}$$/수식$$\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${ans1_frac}`+`{ans2_frac}`=`{frac}{equal}{ans}$$/수식$$\n\n"
    
    num1 = np.random.randint(8,21)
    num2 = np.random.randint(int(num1/4), int(num1/2)-1)
    num3 = np.random.randint(int(num1/2)+1, int(num1/4*3))

    ans1 = num2
    ans1_frac = "{%d} over {%d}" % (ans1, num1)
    ans2 = num1 - num3 + 1
    ans2_frac = "{%d} over {%d}" % (ans2, num1)

    num2_list = ""
    if ans1 < 7:
        for i in range(ans1):
            num2_list = num2_list + "$$수식$$" + str((i+1)) + "$$/수식$$"
            if i != ans1 -1:
                num2_list = num2_list + ", "
    else:
        num2_list = num2_list + "$$수식$$" + str(1) + "$$/수식$$" + ", " + "$$수식$$" + str(2) + "$$/수식$$" + \
             ", " + "$$수식$$CDOTS$$/수식$$" + ", " + "$$수식$$" + str(ans1) + "$$/수식$$"
    
    num3_list = ""
    if ans2 < 7:
        for i in range(ans2):
            num3_list = num3_list + "$$수식$$" + str(i+num3) + "$$/수식$$"
            if i != ans2 -1:
                num3_list = num3_list + ", "  
    else:
        num3_list = num3_list + "$$수식$$" + str(num3) + "$$/수식$$" + ", " + "$$수식$$" + str(2+num3) + "$$/수식$$" + \
             ", " + "$$수식$$CDOTS$$/수식$$" + ", " + "$$수식$$" + str(ans2+num3-1) + "$$/수식$$"

    cont = ctr_frac(ans1+ans2, num1)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans1+ans2, num1)
        ans_list = [ans1+ans2, num1]
    else:
        frac = "{%d} over {%d}" % (ans1+ans2, num1)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    example_list = make_fraction_example(ans_list[0], ans_list[1], num1)

    stem = stem.format(num1=num1, num2=num2, num3=num3, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num2=num2, num3=num3, num2_list=num2_list, num3_list=num3_list, \
        ans1=ans1, ans1_frac=ans1_frac, ans2=ans2, ans2_frac=ans2_frac, frac=frac, equal=equal, ans=ans)

    return stem, answer, comment


# 2-2-6-83
def numbercases226_Stem_059():
    stem = "영어 단어 {word}에서 이 $$수식$${num1}$$/수식$$개의 알파벳을 일렬로 배열할 때, "\
        "{alp1} 또는 {alp2}{j2} 맨 {cond}에 올 확률을 구하시오.\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "모든 경우의 수는 $$수식$${multiples1}`=`{ans1}`$$/수식$$\n"\
        "{alp1}{j1} 맨 {cond}에 오는 경우의 수는\n"\
        "$$수식$${multiples2}`=`{ans2_1}`$$/수식$$\n"\
        "{alp2}{j2} 맨 {cond}에 오는 경우의 수도 마찬가지로 $$수식$${ans2_1}$$/수식$$이다.\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${frac_}`+`{frac_}`=`{frac}{equal}{ans}$$/수식$$\n\n"

    cond = ["앞", "뒤"][np.random.randint(0,2)]
    
    # BLACK (1 11 0 2 10)
    # GLORY (6 11 14 17 24)
    # FAVORITE (5 0 21 14 17 8 19 4)
    # SONG (18 14 13 6)
    # ORANGE (14 17 0 13 6 4)
    word_list = ["$$수식$$rmBLACK$$/수식$$", "$$수식$$rmGLORY$$/수식$$", "$$수식$$rmFAVORITE$$/수식$$", "$$수식$$rmSONG$$/수식$$", "$$수식$$rmORANGE$$/수식$$"]
    code_list = [[1, 11, 0, 2, 10], [6, 11, 14, 17, 24], [5, 0, 21, 14, 17, 8, 19, 4], [18, 14, 13, 6], [14, 17, 0, 13, 6, 4]]
    word_ind = np.random.randint(0,5)
    word = word_list[word_ind]
    code = code_list[word_ind]

    out = random.sample(code, 2)
    out.sort()
    alp1 = "$$수식$$rm%s`$$/수식$$" % chr(65 + out[0])
    alp2 = "$$수식$$rm%s`$$/수식$$" % chr(65 + out[1])
    j1 = proc_jo(alp1, 0)
    j2 = proc_jo(alp2, 0)
    
    num1 = len(code)

    multiples1 = ""
    ans1 = 1

    for i in range(num1):
        if i == 0:
            multiples1 = "%d"%(i+1) + multiples1
        else:
            multiples1 = "%d`times`"%(i+1) + multiples1
        ans1 = ans1 * (i+1)

    multiples2 = ""
    ans2_1 = 1

    for i in range(num1-1):
        if i == 0:
            multiples2 = "%d"%(i+1) + multiples2
        else:
            multiples2 = "%d`times`"%(i+1) + multiples2
        ans2_1 = ans2_1 * (i+1)
    
    ans2 = ans2_1 * 2

    frac_ = "{%d} over {%d}" % (ans2_1, ans1)

    cont = ctr_frac(ans2, ans1)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans2, ans1)
        ans_list = [ans2, ans1]
    else:
        frac = "{%d} over {%d}" % (ans2, ans1)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    stem = stem.format(word=word, num1=num1, alp1=alp1, alp2=alp2, j2=j2, cond=cond)
    answer = answer.format(ans=ans)
    comment = comment.format(multiples1=multiples1, ans1=ans1, multiples2=multiples2, ans2_1=ans2_1, cond=cond, \
        alp1=alp1, alp2=alp2, j1=j1, j2=j2, frac_=frac_, frac=frac, equal=equal, ans=ans)

    return stem, answer, comment


# 2-2-6-85
def numbercases226_Stem_060():
    stem = "서로 다른 두 개의 주사위를 던져서 나온 눈의 수를 각각 "\
        "$$수식$$a,`````b`$$/수식$$라 할 때, $$수식$$ ax`-`b`=`{num1} $$/수식$$ "\
        "의 해가 $$수식$${num2}$$/수식$$ 또는 $$수식$${num3}$$/수식$$일 확률을 구하시오.\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "해가 $$수식$${num2}$$/수식$$인 경우 $$수식$${num2_}a`-`b`=`{num1}$$/수식$$을 만족하는 $$수식$$(a,`````b )$$/수식$$의 순서쌍은\n"\
        "$$수식$${answer_pair1}$$/수식$$의 $$수식$${ans1}$$/수식$$가지\n"\
        "해가 $$수식$${num3}$$/수식$$인 경우 $$수식$${num3_}a`-`b`=`{num1}$$/수식$$을 만족하는 $$수식$$(a,`````b )$$/수식$$의 순서쌍은\n"\
        "$$수식$${answer_pair2}$$/수식$$의 $$수식$${ans2}$$/수식$$가지\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${frac_1}`+`{frac_2}`=`{frac}{equal}{ans}$$/수식$$\n\n"

    out = random.sample(list(range(1,5)), 2)
    out.sort()
    num2 = out[0]
    num3 = out[1]
    num1 = np.random.randint(-1,4) + int((num2+num3)/2)

    answer_pair1 = ""
    ans1 = 0

    for i in range(6):
            for j in range(6):
                if(num2 * (i+1) == (j+1) + num1):
                    if answer_pair1 == "":
                        answer_pair1 = answer_pair1 + "(%d,`````%d)" % (i+1, j+1)
                    else:
                        answer_pair1 = answer_pair1 + "`````(%d,`````%d)" % (i+1, j+1)
                    ans1 = ans1 + 1

    answer_pair2 = ""
    ans2 = 0

    for i in range(6):
            for j in range(6):
                if(num3 * (i+1) == (j+1) + num1):
                    if answer_pair2 == "":
                        answer_pair2 = answer_pair2 + "(%d,`````%d)" % (i+1, j+1)
                    else:
                        answer_pair2 = answer_pair2 + "`````(%d,`````%d)" % (i+1, j+1)
                    ans2 = ans2 + 1


    frac_1 = "{%d} over {%d}" % (ans1, 36)
    frac_2 = "{%d} over {%d}" % (ans2, 36)

    cont = ctr_frac(ans1 + ans2, 36)
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans1 + ans2, 36)
        ans_list = [ans1 + ans2, 36]
    else:
        frac = "{%d} over {%d}" % (ans1 + ans2, 36)
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    stem = stem.format(num1=num1, num2=num2, num3=num3)
    answer = answer.format(ans=ans)
    comment = comment.format(num1=num1, num2=num2, num3=num3, num2_=('' if num2 == 1 else num2), num3_=('' if num3 == 1 else num3), \
        answer_pair1=answer_pair1, ans1=ans1, answer_pair2=answer_pair2, ans2=ans2, frac_1=frac_1, frac_2=frac_2, frac=frac, equal=equal, ans=ans)

    return stem, answer, comment


# 2-2-6-87
def numbercases226_Stem_061():
    stem = "$$수식$$rmA$$/수식$$ 주머니에는 모양과 크기가 같은 {clr1} 공 $$수식$${num1}$$/수식$$개, {clr2} 공 $$수식$${num2}$$/수식$$개가 들어 있고, "\
        "$$수식$$rmB$$/수식$$ 주머니에는 모양과 크기가 같은 {clr1} 공 $$수식$${num3}$$/수식$$개, {clr2} 공 $$수식$${num4}$$/수식$$개가 들어 있다. "\
        "$$수식$$rmA$$/수식$$, $$수식$$rmB$$/수식$$ 두 주머니에서 각각 $$수식$$1`$$/수식$$개씩 공을 꺼낼 때, $$수식$$rmA$$/수식$$ 주머니에서 {clr1} 공이 나오고, "\
        "$$수식$$rmB$$/수식$$ 주머니에서 {clr2} 공이 나올 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "$$수식$$rmA$$/수식$$ 주머니에서 {clr1} 공이 나올 확률은\n"\
        "$$수식$${ans1_frac}{ans1_eq}{ans1_r}$$/수식$$\n"\
        "$$수식$$rmB$$/수식$$ 주머니에서 {clr2} 공이 나올 확률은\n"\
        "$$수식$${ans2_frac}{ans2_eq}{ans2_r}$$/수식$$\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${ans1_r}`times`{ans2_r}`=`{ans}$$/수식$$\n\n"
    
    clr = ["빨간", "주황", "노란", "초록", "파란", "검은", "흰"]
    clrs = random.sample(clr, 2)
    clr1 = clrs[0]
    clr2 = clrs[1]

    nums1 = random.sample(list(range(2,6)),2)
    nums2 = random.sample(list(range(2,6)),2)
    num1 = nums1[0]
    num2 = nums1[1]
    num3 = nums2[0]
    num4 = nums2[1]

    interval = 1

    cont1 = ctr_frac(num1, num1+num2)
    if cont1[0] == -1:
        ans1_frac = ""
        ans1_eq = ""
        ans1_r = "{%d} over {%d}" % (num1, num1+num2)
        interval = interval * num1+num2
    else:
        ans1_frac = "{%d} over {%d}" % (num1, num1+num2)
        ans1_eq = "`=`"
        ans1_r = "{%d} over {%d}" % (cont1[0], cont1[1])
        interval = interval * cont1[1]

    cont2 = ctr_frac(num4, num3+num4)
    if cont2[0] == -1:
        ans2_frac = ""
        ans2_eq = ""
        ans2_r = "{%d} over {%d}" % (num4, num3+num4)
        interval = interval * (num3+num4)
    else:
        ans2_frac = "{%d} over {%d}" % (num4, num3+num4)
        ans2_eq = "`=`"
        ans2_r = "{%d} over {%d}" % (cont2[0], cont2[1])
        interval = interval * cont2[1]

    cont = ctr_frac(num1 * num4, (num1+num2)*(num3+num4))
    if cont[0] == -1:
        ans = "{%d} over {%d}" % (num1 * num4, (num1+num2)*(num3+num4))
        ans_list = [num1 * num4, (num1+num2)*(num3+num4)]
    else:
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    example_list = make_fraction_example(ans_list[0], ans_list[1], interval)

    stem = stem.format(num1=num1, num2=num2, num3=num3, num4=num4, clr1=clr1, clr2=clr2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(clr1=clr1, clr2=clr2, ans1_frac=ans1_frac, ans1_eq=ans1_eq, ans1_r=ans1_r, \
        ans2_frac=ans2_frac, ans2_eq=ans2_eq, ans2_r=ans2_r, ans=ans)

    return stem, answer, comment


# 2-2-6-88
def numbercases226_Stem_062():
    stem = "어느 공장에서 생산되는 {obj}{j} $$수식$${num1}$$/수식$${unit} 중 $$수식$${num2}$$/수식$${unit} 꼴로 불량품이 "\
        "발생한다고 한다. 이 공장에서 생산되는 {obj} 중 임의로 두 {unit}를 선택할 때, "\
        "모두 불량품일 확률을 구하시오.\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "한 {unit}{j_u} 불량품일 확률은"\
        "$$수식$${frac1}{eq1}{ans1}$$/수식$$\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${ans1}`times`{ans1}`=`{ans}$$/수식$$\n\n"

    obj_ind = np.random.randint(0,5)
    obj = ["장난감 로봇", "컴퓨터", "볼펜", "청소기", "공책"][obj_ind]
    unit = ["개", "개", "자루", "대", "권"][obj_ind]
    j = proc_jo(obj, -1)
    j_u = proc_jo(unit, 0)
    num1 = np.random.randint(3,7) * 100
    num2 = np.random.randint(2, int(num1/100))

    cont = ctr_frac(num2, num1)
    if cont[0] == -1:
        frac1 = ""
        eq1 = ""
        ans1 = "{%d} over {%d}" % (num2, num1)
        ans_list = [num2, num1]
    else:
        frac1 = "{%d} over {%d}" % (num2, num1)
        eq1 = "`=`"
        ans1 = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    ans = "{%d} over {%d}" % (ans_list[0]**2, ans_list[1]**2)

    stem = stem.format(num1=num1, num2=num2, obj=obj, j=j, unit=unit)
    answer = answer.format(ans=ans)
    comment = comment.format(num1=num1, num2=num2, unit=unit, j_u=j_u, frac1=frac1, eq1=eq1, ans1=ans1, ans=ans)

    return stem, answer, comment


# 2-2-6-90
def numbercases226_Stem_063():
    stem = "{n1}{j1} {n2}{j2} 이번 주 {day}에 비가 오지 않으면 함께 {obj}{j} 보기로 하였다. "\
        "{day}에 비가 올 확률은 $$수식$${num1}%$$/수식$$이고, {n1}{j1} {n2}{j2} 약속을 지킬 확률은 각각 $$수식$${num2}%$$/수식$$, $$수식$${num3}%$$/수식$$이다. "\
        "{day}에 두 사람이 함께 {obj}{j} 볼 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "두 사람이 함께 {obj}{j} 보려면 {day}에 비가 오지 않고, 두 사람 모두 약속을 지켜야 한다. "\
        "{day}에 비가 오지 않을 확률은\n"\
        "$$수식$$1`-`{rain_f}`=`{ans1_frac}{ans1_eq}{ans1_r}$$/수식$$\n"\
        "두 사람 모두 약속을 지킬 확률은\n"\
        "$$수식$${n1_f}`times`{n2_f}`=`{ans2_frac}{ans2_eq}{ans2_r}$$/수식$$\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${ans1_r}`times`{ans2_r}`=`{ans}$$/수식$$\n\n"
    
    obj = ["야외 공연", "뮤지컬", "영화", "전시회"][np.random.randint(0,4)]
    j = proc_jo(obj, 4)

    name_list = ["현호", "민성", "상균", "병호", "정익", "용권", "성회", "종호"]
    out = random.sample(name_list, 2)
    n1 = out[0]
    j1 = proc_jo(n1, 2)
    n2 = out[1]
    j2 = proc_jo(n2, 0)

    day = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"][np.random.randint(0,7)]

    num1 = np.random.randint(2,9) * 5
    num2 = np.random.randint(14,19) * 5
    num3 = np.random.randint(10,15) * 5

    rain_f = "{%d} over {%d}" % (num1, 100)
    n1_f = "{%d} over {%d}" % (num2, 100)
    n2_f = "{%d} over {%d}" % (num3, 100)

    interval = 1
    cont1 = ctr_frac(100-num1, 100)
    if cont1[0] == -1:
        ans1_frac = ""
        ans1_eq = ""
        ans1_r = "{%d} over {%d}" % (100-num1, 100)
        interval = interval * 100
    else:
        ans1_frac = "{%d} over {%d}" % (100-num1, 100)
        ans1_eq = "`=`"
        ans1_r = "{%d} over {%d}" % (cont1[0], cont1[1])
        interval = interval * cont1[1]

    cont2 = ctr_frac(num2*num3, 10000)
    if cont2[0] == -1:
        ans2_frac = ""
        ans2_eq = ""
        ans2_r = "{%d} over {%d}" % (num2*num3, 10000)
        interval = interval * (10000)
    else:
        ans2_frac = "{%d} over {%d}" % (num2*num3, 10000)
        ans2_eq = "`=`"
        ans2_r = "{%d} over {%d}" % (cont2[0], cont2[1])
        interval = interval * cont2[1]

    cont = ctr_frac((100-num1)*num2*num3, 1000000)
    if cont[0] == -1:
        ans = "{%d} over {%d}" % ((100-num1)*num2*num3, 1000000)
        ans_list = [(100-num1)*num2*num3, 1000000]
    else:
        ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    example_list = make_fraction_example(ans_list[0], ans_list[1], interval)

    stem = stem.format(num1=num1, num2=num2, num3=num3, n1=n1, n2=n2, j1=j1, j2=j2, obj=obj, j=j, day=day, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(obj=obj, j=j, day=day, rain_f=rain_f, n1_f=n1_f, n2_f=n2_f, \
        ans1_frac=ans1_frac, ans1_eq=ans1_eq, ans1_r=ans1_r, ans2_frac=ans2_frac, ans2_eq=ans2_eq, ans2_r=ans2_r, ans=ans)

    return stem, answer, comment


# 2-2-6-91
def numbercases226_Stem_064():
    stem = "$$수식$$rmA$$/수식$$, $$수식$$rmB$$/수식$$, $$수식$$rmC$$/수식$$ {test}의 합격률이 "\
        "각각 $$수식$${frac1}$$/수식$$, $$수식$${frac2}$$/수식$$, $$수식$${frac3}$$/수식$$이다. "\
        "{name}{j}가 세 {test}에 지원했을 때, 적어도 한 {test}에는 합격할 확률을 구하시오.\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "$$수식$$rmA$$/수식$$ {test}에 불합격할 확률은\n"\
        "$$수식$$1`-`{frac1}`=`{f1}$$/수식$$\n"\
        "$$수식$$rmB$$/수식$$ {test}에 불합격할 확률은\n"\
        "$$수식$$1`-`{frac2}`=`{f2}$$/수식$$\n"\
        "$$수식$$rmC$$/수식$$ {test}에 불합격할 확률은\n"\
        "$$수식$$1`-`{frac3}`=`{f3}$$/수식$$\n"\
        "이므로 세 {test}에 모두 불합격할 확률은\n"\
        "$$수식$${f1}`times`{f2}`times`{f3}`=`{ans1}$$/수식$$\n"\
        "따라서 {name}{j}가 적어도 한 {test}에는 합격할 확률은\n"\
        "$$수식$$1`-`{ans1}`=`{frac}{equal}{ans}$$/수식$$\n\n"

    test = ["오디션", "회사", "대학교"][np.random.randint(0,3)]
    name = ["륜한", "태헌", "민하", "상민", "진욱", "주원", "호준", "재연", "준혁", "보경"][np.random.randint(0,10)]
    j = proc_jo(name, 3)

    num = random.sample(list(range(3,11)), 3)
    num.sort()
    n1 = num[0]
    n2 = num[1]
    n3 = num[2]

    frac1 = "{%d} over {%d}" % (1, n1)
    frac2 = "{%d} over {%d}" % (1, n2)
    frac3 = "{%d} over {%d}" % (1, n3)
    f1 = "{%d} over {%d}" % (n1-1, n1)
    f2 = "{%d} over {%d}" % (n2-1, n2)
    f3 = "{%d} over {%d}" % (n3-1, n3)

    cont = ctr_frac((n1-1)*(n2-1)*(n3-1), n1*n2*n3)
    if cont[0] == -1:
        ans1 = "{%d} over {%d}" % ((n1-1)*(n2-1)*(n3-1), n1*n2*n3)
        ans_list = [(n1-1)*(n2-1)*(n3-1), n1*n2*n3]
    else:
        ans1 = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    cont = ctr_frac(ans_list[1] - ans_list[0], ans_list[1])
    if cont[0] == -1:
        frac = ""
        equal = ""
        ans = "{%d} over {%d}" % (ans_list[1] - ans_list[0], ans_list[1])
    else:
        frac = "{%d} over {%d}" % (ans_list[1] - ans_list[0], ans_list[1])
        equal = "`=`"
        ans = "{%d} over {%d}" % (cont[0], cont[1])

    stem = stem.format(test=test, frac1=frac1, frac2=frac2, frac3=frac3, name=name, j=j)
    answer = answer.format(ans=ans)
    comment = comment.format(test=test, frac1=frac1, frac2=frac2, frac3=frac3, name=name, j=j, \
        f1=f1, f2=f2, f3=f3, ans1=ans1, frac=frac, equal=equal, ans=ans)

    return stem, answer, comment


# 2-2-6-92
def numbercases226_Stem_065():
    stem = "$$수식$$rmA$$/수식$$ 주머니에는 {clr1} 공 $$수식$${num1}$$/수식$$개, {clr2} 공 $$수식$${num2}$$/수식$$개가 들어 있고, "\
        "$$수식$$rmB$$/수식$$ 주머니에는 {clr1} 공 $$수식$${num3}$$/수식$$개, {clr2} 공 $$수식$${num4}$$/수식$$개가 들어 있다. "\
        "$$수식$$rmA$$/수식$$, $$수식$$rmB$$/수식$$ 두 주머니에서 각각 $$수식$$1`$$/수식$$개씩 공을 꺼낼 때, "\
        "적어도 $$수식$$1`$$/수식$$개는 {clr1} 공일 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "두 개 모두 {clr2} 공일 확률은\n"\
        "$$수식$${frac1}`times`{frac2}`=`{rev_ans}$$/수식$$\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$$1`-`{rev_ans}`=`{ans}$$/수식$$\n\n"
    
    clr = ["빨간", "주황", "노란", "초록", "파란", "검은", "흰"]
    clrs = random.sample(clr, 2)
    clr1 = clrs[0]
    clr2 = clrs[1]

    nums1 = random.sample(list(range(2,6)),2)
    nums2 = random.sample(list(range(2,6)),2)
    num1 = nums1[0]
    num2 = nums2[0]
    num3 = nums1[1]
    num4 = nums2[1]

    frac1 = "{%d} over {%d}" % (num2, num1+num2)
    frac2 = "{%d} over {%d}" % (num4, num3+num4)

    cont = ctr_frac(num2 * num4, (num1+num2)*(num3+num4))
    if cont[0] == -1:
        rev_ans = "{%d} over {%d}" % (num2 * num4, (num1+num2)*(num3+num4))
        ans_list = [num2 * num4, (num1+num2)*(num3+num4)]
    else:
        rev_ans = "{%d} over {%d}" % (cont[0], cont[1])
        ans_list = [cont[0], cont[1]]

    ans = "{%d} over {%d}" % (ans_list[1] - ans_list[0], ans_list[1])

    example_list = make_fraction_example(ans_list[1] - ans_list[0], ans_list[1], ans_list[1]*3 if ans_list[1] < 5 else ans_list[1])

    stem = stem.format(num1=num1, num2=num2, num3=num3, num4=num4, clr1=clr1, clr2=clr2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(clr2=clr2, frac1=frac1, frac2=frac2, rev_ans=rev_ans, ans=ans)

    return stem, answer, comment


# 2-2-6-93
def numbercases226_Stem_066():
    stem = "{n1}{j1} {n2}{j2}는 내일 비가 오지 않으면 함께 {long_obj}. "\
        "내일 비가 올 확률은 $$수식$${frac1}$$/수식$$이고, {n1}{j1} {n2}{j2} 약속을 지킬 확률은 각각 $$수식$${frac2}$$/수식$$, $$수식$${frac3}$$/수식$$일 때, "\
        "내일 두 사람이 함께 {short_obj} 할 확률은?\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "{short_obj} 하려면 비가 오지 않고, 두 사람 모두 약속을 지켜야 하므로 두 사람이 함께 {short_obj} 할 확률은\n"\
        "$$수식$$ (1`-`{frac1} )`times`{frac2}`times`{frac3}`=`{frac1_rev}`times`{frac2}`times`{frac3}`=`{ans}$$/수식$$\n\n"
    
    obj_ind = np.random.randint(0,3)
    short_obj = ["등산을", "캠핑을", "봉사를"][obj_ind]
    long_obj = ["등산을 하기로 하고, 등산로 입구에서 만나기로 하였다", "캠핑을 하기로 하고, 캠핑장에서 만나기로 하였다", "봉사를 하기로 하였다"][obj_ind]

    name_list = ["현호", "민성", "상균", "병호", "정익", "용권", "성회", "종호"]
    out = random.sample(name_list, 2)
    n1 = out[0]
    j1 = proc_jo(n1, 2)
    n2 = out[1]
    j2 = proc_jo(n2, 3)

    num1 = np.random.randint(1,4)
    num2 = np.random.randint(6,10)
    num3 = np.random.randint(4,9)

    c1 = ctr_frac(num1, 10)
    if c1[0] == -1:
        frac1 = "{%d} over {%d}" % (num1, 10)
        frac1_rev = "{%d} over {%d}" % (10-num1, 10)
    else:
        frac1 = "{%d} over {%d}" % (c1[0], c1[1])
        frac1_rev = "{%d} over {%d}" % (c1[1] - c1[0], c1[1])

    c2 = ctr_frac(num2, 10)
    if c2[0] == -1:
        frac2 = "{%d} over {%d}" % (num2, 10)
    else:
        frac2 = "{%d} over {%d}" % (c2[0], c2[1])

    c3 = ctr_frac(num3, 10)
    if c3[0] == -1:
        frac3 = "{%d} over {%d}" % (num3, 10)
    else:
        frac3 = "{%d} over {%d}" % (c3[0], c3[1])

    cont = ctr_frac((10-num1)*num2*num3, 1000)
    if cont[0] == -1:
        ans = "{%d} over {%d}" % ((10-num1)*num2*num3, 1000)
    else:
        ans = "{%d} over {%d}" % (cont[0], cont[1])

    stem = stem.format(frac1=frac1, frac2=frac2, frac3=frac3, n1=n1, n2=n2, j1=j1, j2=j2, long_obj=long_obj, short_obj=short_obj)
    answer = answer.format(ans=ans)
    comment = comment.format(frac1=frac1, frac2=frac2, frac3=frac3, frac1_rev=frac1_rev, long_obj=long_obj, short_obj=short_obj, ans=ans)

    return stem, answer, comment


# 2-2-6-94
def numbercases226_Stem_067():
    stem = "정답이 $$수식$$1$$/수식$$개인 {prob_type} 문제 $$수식$${num1}$$/수식$$개가 있다. "\
        "이 중 적어도 두 문제를 맞힐 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "(1) {num1_cnt} 문제 모두 맞히지 못할 확률은\n"\
        "$$수식$$ (1`-`{frac} )^{num1}`=`{ans1_frac}$$/수식$$\n"\
        "(2) 한 문제만 맞힐 확률은\n"\
        "$$수식$${num1}`times`{frac}`times`( 1`-`{frac} )^{num2}`=`{ans2_frac}$$/수식$$\n"\
        "(1), (2)에서 적어도 두 문제를 맞힐 확률은\n"\
        "$$수식$$1`-`({ans1_frac}`+`{ans2_frac} )`=`{ans}$$/수식$$\n\n"
    
    type_ind = np.random.randint(0,2)
    prob_type = ["사지선다형", "오지선다형"][type_ind]
    prob_num = type_ind + 4
    frac = "{%d} over {%d}" % (1, prob_num)

    num1 = np.random.randint(3,6)
    num2 = num1-1
    num1_cnt = ["세", "네", "다섯"][num1-3]

    c1 = ctr_frac((prob_num-1)**num1, prob_num**num1)
    if c1[0] == -1:
        ans1_frac = "{%d} over {%d}" % ((prob_num-1)**num1, prob_num**num1)
        ans_list = [(prob_num-1)**num1, prob_num**num1]
    else:
        ans1_frac = "{%d} over {%d}" % (c1[0], c1[1])
        ans_list = [c1[0], c1[1]]

    c2 = ctr_frac(num1*((prob_num-1)**num2), prob_num**num1)
    if c2[0] == -1:
        ans2_frac = "{%d} over {%d}" % (num1*((prob_num-1)**num2), prob_num**num1)
        ans_list = [num1*((prob_num-1)**num2), prob_num**num1]
    else:
        ans2_frac = "{%d} over {%d}" % (c2[0], c2[1])
        ans_list = [c2[0], c2[1]]

    c3 = ctr_frac(prob_num**num1 - num1*((prob_num-1)**num2) - (prob_num-1)**num1, prob_num**num1)
    if c3[0] == -1:
        ans = "{%d} over {%d}" % (prob_num**num1 - num1*((prob_num-1)**num2) - (prob_num-1)**num1, prob_num**num1)
        ans_list = [prob_num**num1 - num1*((prob_num-1)**num2) - (prob_num-1)**num1, prob_num**num1]
    else:
        ans = "{%d} over {%d}" % (c3[0], c3[1])
        ans_list = [c3[0], c3[1]]
    

    example_list = make_fraction_example(ans_list[0], ans_list[1], prob_num ** int(num1/2))

    stem = stem.format(num1=num1, prob_type=prob_type, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(num1=num1, num2=num2, num1_cnt=num1_cnt, frac=frac, ans1_frac=ans1_frac, ans2_frac=ans2_frac, ans=ans)

    return stem, answer, comment


# 2-2-6-95
def numbercases226_Stem_068():
    stem = "$$수식$$rmA$$/수식$$ 주머니에는 {clr1} 공 $$수식$${num1}$$/수식$$개, {clr2} 공 $$수식$${num2}$$/수식$$개가 들어 있고, "\
        "$$수식$$rmB$$/수식$$ 주머니에는 {clr1} 공 $$수식$${num3}$$/수식$$개, {clr2} 공 $$수식$${num4}$$/수식$$개가 들어 있다. "\
        "{name}{j}가 $$수식$$rmA$$/수식$$, $$수식$$rmB$$/수식$$ 두 주머니에서 각각 $$수식$$1`$$/수식$$개씩 공을 꺼낼 때, "\
        "두 공의 색깔이 모두 {cond} 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "(1) $$수식$$rmA$$/수식$$ 주머니에서 {clr1} 공, $$수식$$rmB$$/수식$$ 주머니에서 {clr12} 공을 꺼낼 확률은\n"\
        "$$수식$${ans1_f1}`times`{ans1_f2}`=`{ans1}$$/수식$$\n"\
        "(2) $$수식$$rmA$$/수식$$ 주머니에서 {clr2} 공, $$수식$$rmB$$/수식$$ 주머니에서 {clr22} 공을 꺼낼 확률은\n"\
        "$$수식$${ans2_f1}`times`{ans2_f2}`=`{ans2}$$/수식$$\n"\
        "(1), (2)에서 구하는 확률은\n"\
        "$$수식$${ans1}`+`{ans2}`=`{ans}$$/수식$$\n\n"
    
    name = ["륜한", "태헌", "민하", "상민", "진욱", "주원", "호준", "재연", "준혁", "보경"][np.random.randint(0,10)]
    j = proc_jo(name, 3)

    clr = ["빨간", "주황", "노란", "초록", "파란", "검은", "흰"]
    clrs = random.sample(clr, 2)
    clr1 = clrs[0]
    clr2 = clrs[1]

    nums1 = random.sample(list(range(2,6)),2)
    nums2 = random.sample(list(range(2,6)),2)
    num1 = nums1[0]
    num2 = nums1[1]
    num3 = nums2[0]
    num4 = nums2[1]

    cond_ind = np.random.randint(0,2)
    cond = ["다를", "같을"][cond_ind]

    if cond_ind == 0:
        clr12 = clr2
        clr22 = clr1
    else:
        clr12 = clr1
        clr22 = clr2

    cont1 = ctr_frac(num1, num1+num2)
    if cont1[0] == -1:
        ans11 = "{%d} over {%d}" % (num1, num1+num2)
    else:
        ans11 = "{%d} over {%d}" % (cont1[0], cont1[1])

    cont1 = ctr_frac(num2, num1+num2)
    if cont1[0] == -1:
        ans12 = "{%d} over {%d}" % (num1, num1+num2)
    else:
        ans12 = "{%d} over {%d}" % (cont1[0], cont1[1])

    cont2 = ctr_frac(num3, num3+num4)
    if cont2[0] == -1:
        ans21 = "{%d} over {%d}" % (num3, num3+num4)
    else:
        ans21 = "{%d} over {%d}" % (cont2[0], cont2[1])

    cont2 = ctr_frac(num4, num3+num4)
    if cont2[0] == -1:
        ans22 = "{%d} over {%d}" % (num4, num3+num4)
    else:
        ans22 = "{%d} over {%d}" % (cont2[0], cont2[1])

    ans1_f1 = ans11
    ans2_f1 = ans12

    if cond_ind == 0:
        ans1_f2 = ans22
        ans2_f2 = ans21

        cont = ctr_frac(num1 * num4, (num1+num2)*(num3+num4))
        if cont[0] == -1:
            ans1 = "{%d} over {%d}" % (num1 * num4, (num1+num2)*(num3+num4))
        else:
            ans1 = "{%d} over {%d}" % (cont[0], cont[1])

        cont = ctr_frac(num2 * num3, (num1+num2)*(num3+num4))
        if cont[0] == -1:
            ans2 = "{%d} over {%d}" % (num2 * num3, (num1+num2)*(num3+num4))
        else:
            ans2 = "{%d} over {%d}" % (cont[0], cont[1])

        cont = ctr_frac(num1 * num4 + num2 * num3, (num1+num2)*(num3+num4))
        if cont[0] == -1:
            ans = "{%d} over {%d}" % (num1 * num4 + num2 * num3, (num1+num2)*(num3+num4))
            ans_list = [num1 * num4 + num2 * num3, (num1+num2)*(num3+num4)]
        else:
            ans = "{%d} over {%d}" % (cont[0], cont[1])
            ans_list = [cont[0], cont[1]]
    else:
        ans1_f2 = ans21
        ans2_f2 = ans22

        cont = ctr_frac(num1 * num3, (num1+num2)*(num3+num4))
        if cont[0] == -1:
            ans1 = "{%d} over {%d}" % (num1 * num3, (num1+num2)*(num3+num4))
        else:
            ans1 = "{%d} over {%d}" % (cont[0], cont[1])

        cont = ctr_frac(num2 * num4, (num1+num2)*(num3+num4))
        if cont[0] == -1:
            ans2 = "{%d} over {%d}" % (num2 * num4, (num1+num2)*(num3+num4))
        else:
            ans2 = "{%d} over {%d}" % (cont[0], cont[1])

        cont = ctr_frac(num1 * num3 + num2 * num4, (num1+num2)*(num3+num4))
        if cont[0] == -1:
            ans = "{%d} over {%d}" % (num1 * num3 + num2 * num4, (num1+num2)*(num3+num4))
            ans_list = [num1 * num3 + num2 * num4, (num1+num2)*(num3+num4)]
        else:
            ans = "{%d} over {%d}" % (cont[0], cont[1])
            ans_list = [cont[0], cont[1]]
    
    example_list = make_fraction_example(ans_list[0], ans_list[1], ans_list[1] * 2 if ans_list[1] < 5 else ans_list[1])

    stem = stem.format(num1=num1, num2=num2, num3=num3, num4=num4, clr1=clr1, clr2=clr2, name=name, j=j, cond=cond, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(clr1=clr1, clr2=clr2, clr12=clr12, clr22=clr22, ans1_f1=ans1_f1, ans1=ans1, \
        ans1_f2=ans1_f2, ans2_f1=ans2_f1, ans2_f2=ans2_f2, ans2=ans2, ans=ans)

    return stem, answer, comment


# 2-2-6-96
def numbercases226_Stem_069():
    stem = "{name}{j}가 {test} 시험에서 정답이 $$수식$$1$$/수식$$개인 {prob_type} 문제 중 $$수식$${num1}$$/수식$$개를 풀지 못하여 "\
        "임의로 답을 적었을 때, 이 중 $$수식$${num2}$$/수식$$ 문제를 맞힐 확률을 구하시오.\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "$$수식$${num1}$$/수식$$ 문제 중에서 정답을 맞히는 $$수식$${num2}$$/수식$$ 문제를 고르는 경우의 수는 $$수식$${ans1}$$/수식$$가지이다.\n"\
        "각 문제에 대해서 정답을 맞힐 확률은 $$수식$${frac1}$$/수식$$, 틀릴 확률은 $$수식$${frac2}$$/수식$$이므로 구하는 확률은\n"\
        "$$수식$${ans1}`times`({frac1})^{num2}`times`({frac2})^{num3}`=`{ans}$$/수식$$\n\n"
    
    name = ["륜한", "태헌", "민하", "상민", "진욱", "주원", "호준", "재연", "준혁", "보경"][np.random.randint(0,10)]
    j = proc_jo(name, 3)

    test = ["중간고사", "기말고사", "모의고사", "수능"][np.random.randint(0,4)]

    type_ind = np.random.randint(0,2)
    prob_type = ["사지선다형", "오지선다형"][type_ind]
    prob_num = type_ind + 4
    frac1 = "{%d} over {%d}" % (1, prob_num)
    frac2 = "{%d} over {%d}" % (prob_num-1, prob_num)
    
    num1 = np.random.randint(3,6)
    num2 = np.random.randint(1,num1)
    num3 = num1 - num2
    ans1 = combination(num1, num2)[0]
    if ans1 == -1:
        ans1 = num1

    c1 = ctr_frac2(ans1 * ((prob_num-1)**num3), prob_num**num1)
    ans = "{%d} over {%d}" % (c1[0], c1[1])

    stem = stem.format(num1=num1, prob_type=prob_type, name=name, j=j, test=test, num2=num2)
    answer = answer.format(ans=ans)
    comment = comment.format(num1=num1, num2=num2, num3=num3, frac1=frac1, frac2=frac2, ans1=ans1, ans=ans)

    return stem, answer, comment


# 2-2-6-98
def numbercases226_Stem_070():
    stem = "두 상자 $$수식$$rmA$$/수식$$, $$수식$$rmB$$/수식$$에 $$수식$$1$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 자연수가 각각 하나씩 적힌 "\
        "카드 $$수식$${num1}$$/수식$$장이 들어 있다. 두 상자에서 각각 $$수식$$1$$/수식$$장씩 카드를 꺼낼 때, "\
        "카드에 적힌 수의 {cond1}이 짝수일 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$                   ② $$수식$${ex2}$$/수식$$                  ③ $$수식$${ex3}$$/수식$$\n④ $$수식$${ex4}$$/수식$$                 ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{case}"\
        "위에서 구하는 확률은\n"\
        "$$수식$$ {ans_plus}`=`{ans}`$$/수식$$\n\n"

    num1 = np.random.randint(2,10)*2 + 1
    even = num1 // 2
    odd = num1 - even

    even_frac = "{%d} over {%d}" % (even, num1)
    odd_frac = "{%d} over {%d}" % (odd, num1)
    f1 = "{%d} over {%d}" % (odd*odd, num1*num1)
    f2 = "{%d} over {%d}" % (even*even, num1*num1)
    f3 = "{%d} over {%d}" % (even*odd, num1*num1)

    ind1 = np.random.randint(0,2)
    cond1 = ["합", "곱"][ind1]

    odd2_format = "({num1}) 두 상자에서 모두 홀수가 적힌 카드를 꺼낼 확률은\n" + \
        "$$수식$${odd_frac}`times`{odd_frac}`=`{frac}$$/수식$$\n"
    even2_format = "({num1}) 두 상자에서 모두 짝수가 적힌 카드를 꺼낼 확률은\n" + \
        "$$수식$${even_frac}`times`{even_frac}`=`{frac}$$/수식$$\n"
    each_format = "({num1}) 두 상자에서 하나는 홀수, 하나는 짝수가 적힌 카드를 꺼낼 확률은\n" + \
        "$$수식$${odd_frac}`times`{even_frac}`=`{frac}$$/수식$$\n"

    case = ""
    ans_plus = ""
    cnt = 1

    if ind1 == 0:
        case = odd2_format.format(num1=1, odd_frac=odd_frac, frac=f1) + even2_format.format(num1=2, even_frac=even_frac, frac=f2)
        ans_plus = f1 + "`+`" + f2
        ctr = ctr_frac2(odd*odd + even*even, num1*num1)
        ans = "{%d} over {%d}" % (ctr[0], ctr[1])
        ans_list = [ctr[0], ctr[1]]
    else:
        case = even2_format.format(num1=1, even_frac=even_frac, frac=f2) + each_format.format(num1=2, even_frac=even_frac, odd_frac=odd_frac, frac=f3)
        ans_plus = f2 + "`+`" + f3
        ctr = ctr_frac2(odd*even + even*even, num1*num1)
        ans = "{%d} over {%d}" % (ctr[0], ctr[1])
        ans_list = [ctr[0], ctr[1]]
    
    example_list = make_fraction_example(ans_list[0], ans_list[1], ans_list[1]*3 if ans_list[1] < 5 else ans_list[1])

    stem = stem.format(num1=num1, cond1=cond1, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(case=case, ans_plus=ans_plus, ans=ans)

    return stem, answer, comment


# 2-2-6-99
def numbercases226_Stem_071():
    stem = "한 개의 주사위를 한 번 던져서 {c1}의 눈이 나오면 한 개의 동전을 {n1} 번 던지고, "\
        "{c2}의 눈이 나오면 동전을 {n2} 번 던지기로 하였다. 이때 동전의 앞면이 적어도 "\
        "{n1} 번 이상 나올 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "(1) {c1}의 눈이 나오는 경우\n"\
        "{n1} 번 모두 동전의 앞면이 나와야 하므로 그 확률은\n"\
        "$$수식$${c1_frac}`times`{n1_frac1}`=`{ans1}$$/수식$$\n"\
        "(2) {c2}의 눈이 나오는 경우는\n"\
        "동전의 앞면이 {n1} 번 나올 확률은 $$수식$${n1_frac2}$$/수식$$, 동전의 앞면이 {n2} 번 나올 확률은 $$수식$${n2_frac2}$$/수식$$이므로 "\
        "그 확률은\n$$수식$${c2_frac}`times`({n1_frac2}`+`{n2_frac2})`=`{ans2}$$/수식$$\n"\
        "(1), (2)에서 구하는 확률은\n"\
        "$$수식$$ {ans1}`+`{ans2}`=`{ans}`$$/수식$$\n\n"

    c_ind = np.random.randint(0,3)
    c1 = ["짝수", "3 이하", "3의 배수"][c_ind]
    c2 = ["홀수", "4 이상", "그 외"][c_ind]

    c1_f = [3, 3, 2][c_ind]
    c2_f = [3, 3, 4][c_ind]
    c1_frac = "{%d} over {%d}" % (c1_f, 6)
    c2_frac = "{%d} over {%d}" % (c2_f, 6)

    n_ind = np.random.randint(0,2)
    n1 = ["두", "세"][n_ind]
    n2 = ["세", "네"][n_ind]

    n1_f1 = [[1,4], [1,8]][n_ind]
    n1_f2 = [[3,8], [4,16]][n_ind]
    n2_f2 = [[1,8], [1,16]][n_ind]
    n1_frac1 = "{%d} over {%d}" % (n1_f1[0], n1_f1[1])
    n1_frac2 = "{%d} over {%d}" % (n1_f2[0], n1_f2[1])
    n2_frac2 = "{%d} over {%d}" % (n2_f2[0], n2_f2[1])

    ctr = ctr_frac2(c1_f*n1_f1[0], 6*n1_f1[1])
    ans1 = "{%d} over {%d}" % (ctr[0], ctr[1])
    ans1_list = [ctr[0], ctr[1]]

    ctr = ctr_frac2(c2_f*(n1_f2[0]+n2_f2[0]), 6*n1_f2[1])
    ans2 = "{%d} over {%d}" % (ctr[0], ctr[1])
    ans2_list = [ctr[0], ctr[1]]

    ans_list = sum_frac(ans1_list, ans2_list)
    ans = "{%d} over {%d}" % (ans_list[0], ans_list[1])

    example_list = make_fraction_example(ans_list[0], ans_list[1], ans_list[1] * 2 if ans_list[1] < 5 else ans_list[1])

    stem = stem.format(c1=c1, c2=c2, n1=n1, n2=n2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(c1=c1, c2=c2, n1=n1, n2=n2, c1_frac=c1_frac, c2_frac=c2_frac, \
        n1_frac1=n1_frac1, n1_frac2=n1_frac2, n2_frac2=n2_frac2, ans1=ans1, ans2=ans2, ans=ans)

    return stem, answer, comment


# 2-2-6-101
def numbercases226_Stem_072():
    stem = "$$수식$${num1}$$/수식$$개의 제비 중 $$수식$${num2}$$/수식$$개의 당첨 제비가 들어 있는 상자가 있다. "\
        "이 상자에서 {n1}{j1}가 제비 $$수식$$1$$/수식$$개를 뽑아 확인하고, 다시 넣은 후 {n2}{j2}가 $$수식$$1$$/수식$$개를 뽑을 때, "\
        "{n1}{j1}는 당첨되고 {n2}{j2}는 당첨되지 않을 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{n1}{j1}가 당첨 제비를 뽑을 확률은  "\
        "$$수식$$ `RARROW`{ans1}$$/수식$$\n"\
        "{n2}{j2}가 당첨 제비를 뽑지 않을 확률은 "\
        "$$수식$$`RARROW`{ans2}$$/수식$$\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${ans1}`times`{ans2}`=`{ans}$$/수식$$\n\n"
    
    name_list = ["현호", "민성", "상균", "병호", "정익", "용권", "성회", "종호"]
    out = random.sample(name_list, 2)
    n1 = out[0]
    j1 = proc_jo(n1, 3)
    n2 = out[1]
    j2 = proc_jo(n2, 3)

    num1 = np.random.randint(1,5) * 10
    num2 = np.random.randint(int(num1/4), int(num1/2))

    ctr = ctr_frac2(num2, num1)
    ans1 = "{%d} over {%d}" % (ctr[0], ctr[1])
    ctr = ctr_frac2(num1-num2, num1)
    ans2 = "{%d} over {%d}" % (ctr[0], ctr[1])

    ctr = ctr_frac2(num2 * (num1-num2), num1*num1)
    ans = "{%d} over {%d}" % (ctr[0], ctr[1])

    example_list = make_fraction_example(ctr[0], ctr[1], ctr[1] if ctr[1] > 5 else ctr[1] * 2)

    stem = stem.format(num1=num1, num2=num2, n1=n1, j1=j1, n2=n2, j2=j2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, j1=j1, n2=n2, j2=j2, ans1=ans1, ans2=ans2, ans=ans)

    return stem, answer, comment


# 2-2-6-103
def numbercases226_Stem_073():
    stem = "주머니에 {n1} 공과 {n2} 공이 합하여 $$수식$${num1}$$/수식$$개가 들어 있다. 이 주머니에서 $$수식$$1$$/수식$$개의 공을 꺼내 "\
        "색을 확인하고 다시 넣은 후 $$수식$$1$$/수식$$개의 공을 또 꺼낼 때, {n1} 공이 한 번 이상 나올 확률이 $$수식$${p_res}$$/수식$$이었다. "\
        "이때 {n2} 공의 개수는?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "{n2} 공의 개수를 $$수식$$x$$/수식$$라 하면 두 번 모두 {n2} 공이 나올 확률은\n"\
        "$$수식$${p_n2}`times`{p_n2}`=`{p_n22}$$/수식$$\n"\
        "이므로 {n1} 공이 한 번 이상 나올 확률은\n"\
        "$$수식$$1`-`{p_n22}$$/수식$$\n"\
        "따라서 $$수식$$1`-`{p_n22}`=`{p_res}$$/수식$$이므로\n"\
        "$$수식$${p_n22}`=`{p_res2}$$/수식$$, $$수식$$x^2`=`{ans1}$$/수식$$  $$수식$$THEREFORE```x`=`{ans}$$/수식$$\n"\
        "따라서 {n2} 공의 개수는 $$수식$${ans}$$/수식$${j}다.\n\n"

    name = random.sample(["검은", "흰", "노란", "빨간", "파란"],2)
    n1 = name[0]
    n2 = name[1]

    ans = np.random.randint(4,8)
    j = proc_jo(ans, 3)
    ans_ = np.random.randint(2,8)
    num1 = ans + ans_

    ctr = ctr_frac2(ans*ans, num1*num1)
    p_res = "{%d} over {%d}" % (ctr[1]-ctr[0], ctr[1])
    p_res2 = "{%d} over {%d}" % (ctr[0], ctr[1])
    ans1 = ans*ans

    p_n2 = "{x} over {%d}" % (num1)
    p_n22 = "{x^2} over {%d}" % (num1*num1)

    example_list = make_example_by_interval(ans, 1)

    stem = stem.format(n1=n1, n2=n2, p_res=p_res, num1=num1, \
                ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, n2=n2, p_n2=p_n2, p_n22=p_n22, p_res=p_res, p_res2=p_res2, ans=ans, j=j, ans_=ans_, ans1=ans1)

    return stem, answer, comment


# 2-2-6-104
def numbercases226_Stem_074():
    stem = "주머니에 {n1} 공 $$수식$${num1}$$/수식$$개, {n2} 공 $$수식$${num2}$$/수식$$개, {n3} 공 $$수식$${num3}$$/수식$$개가 들어 있다. "\
        "연속하여 두 개의 공을 꺼낼 때, 두 번 모두 같은 색의 공을 꺼낼 확률을 구하여라. "\
        "(단, 꺼낸 공은 다시 넣지 않는다.)\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "(1) 두 개 모두 {n1} 공일 확률은\n"\
        "$$수식$${p1_n1}`times`{p2_n1}`=`{ans1}$$/수식$$\n"\
        "(2) 두 개 모두 {n2} 공일 확률은\n"\
        "$$수식$${p1_n2}`times`{p2_n2}`=`{ans2}$$/수식$$\n"\
        "(3) 두 개 모두 {n3} 공일 확률은\n"\
        "$$수식$${p1_n3}`times`{p2_n3}`=`{ans3}$$/수식$$\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${ans1}`+`{ans2}`+`{ans3}`=`{ans}$$/수식$$\n\n"

    name = random.sample(["검은", "흰", "노란", "빨간", "파란", "주황", "초록", "형광"],3)
    n1 = name[0]
    n2 = name[1]
    n3 = name[2]

    nums = random.sample(list(range(2,7)), 3)
    num1 = nums[0]
    num2 = nums[1]
    num3 = nums[2]
    tot = num1 + num2 + num3

    p1_n1 = "{%d} over {%d}" % (num1, tot)
    p2_n1 = "{%d} over {%d}" % (num1-1, tot-1)
    ctr1 = ctr_frac2(num1*(num1-1), tot*(tot-1))
    ans1 = "{%d} over {%d}" % (ctr1[0], ctr1[1])

    p1_n2 = "{%d} over {%d}" % (num2, tot)
    p2_n2 = "{%d} over {%d}" % (num2-1, tot-1)
    ctr2 = ctr_frac2(num2*(num2-1), tot*(tot-1))
    ans2 = "{%d} over {%d}" % (ctr2[0], ctr2[1])

    p1_n3 = "{%d} over {%d}" % (num3, tot)
    p2_n3 = "{%d} over {%d}" % (num3-1, tot-1)
    ctr3 = ctr_frac2(num3*(num3-1), tot*(tot-1))
    ans3 = "{%d} over {%d}" % (ctr3[0], ctr3[1])

    ans_list = sum_frac([ctr1[0], ctr1[1]], [ctr2[0], ctr2[1]])
    ans_list = sum_frac([ans_list[0], ans_list[1]], [ctr3[0], ctr3[1]])
    ans = "{%d} over {%d}" % (ans_list[0], ans_list[1])

    stem = stem.format(n1=n1, n2=n2, n3=n3, num1=num1, num2=num2, num3=num3)
    answer = answer.format(ans=ans)
    comment = comment.format(n1=n1, n2=n2, n3=n3, p1_n1=p1_n1, p2_n1=p2_n1, p1_n2=p1_n2, \
        p2_n2=p2_n2, p1_n3=p1_n3, p2_n3=p2_n3, ans1=ans1, ans2=ans2, ans3=ans3, ans=ans)

    return stem, answer, comment


# 2-2-6-105
def numbercases226_Stem_075():
    stem = "주머니에 {n1} 공 $$수식$${num1}$$/수식$$개, {n2} 공 $$수식$${num2}$$/수식$$개, {n3} 공 $$수식$${num3}$$/수식$$개가 들어 있다. "\
        "연속하여 $$수식$$3$$/수식$$개의 공을 꺼낼 때, {conds} 확률을 구하시오. "\
        "(단, 꺼낸 공은 다시 넣지 않는다.)\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "첫 번째에 {s1} 공을 꺼낼 확률은 "\
        "$$수식$$`RARROW`{p1}$$/수식$$\n"\
        "두 번째에 {s2} 공을 꺼낼 확률은 "\
        "$$수식$$`RARROW`{p2}$$/수식$$\n"\
        "세 번째에 {s3} 공을 꺼낼 확률은"\
        "$$수식$$`RARROW`{p3}$$/수식$$\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${p1}`times`{p2}`times`{p3}`=`{ans}$$/수식$$\n\n"

    name = random.sample(["검은", "흰", "노란", "빨간", "파란", "주황", "초록", "형광"],3)
    n1 = name[0]
    n2 = name[1]
    n3 = name[2]

    nums = random.sample(list(range(2,7)), 3)
    num1 = nums[0]
    num2 = nums[1]
    num3 = nums[2]
    tot = num1 + num2 + num3

    cond_ind = np.random.randint(0,3)
    shuf = list(range(0,3))
    random.shuffle(shuf)

    conds1 = "첫 번째와 두 번째는 {s1} 공이 나오고 세 번째는 {s2} 공이 나올".format(s1=name[shuf[0]], s2=name[shuf[1]])
    conds2 = "첫 번째는 {s1} 공, 두 번째는 {s2} 공, 세 번째는 {s3} 공이 나올".format(s1=name[shuf[0]], s2=name[shuf[1]], s3=name[shuf[2]])
    conds3 = "첫 번째는 {s1} 공, 두 번째와 세 번째는 {s2} 공이 나올".format(s1=name[shuf[0]], s2=name[shuf[1]])
    conds = [conds1, conds2, conds3][cond_ind]

    if cond_ind == 0:
        s1 = name[shuf[0]]
        s2 = name[shuf[0]]
        s3 = name[shuf[1]]

        p1 = "{%d} over {%d}" % (nums[shuf[0]], tot)
        p2 = "{%d} over {%d}" % (nums[shuf[0]]-1, tot-1)
        p3 = "{%d} over {%d}" % (nums[shuf[1]], tot-2)

        ctr = ctr_frac2(nums[shuf[0]]*(nums[shuf[0]]-1)*nums[shuf[1]], tot*(tot-1)*(tot-2))
        ans = "{%d} over {%d}" % (ctr[0], ctr[1])
    elif cond_ind == 1:
        s1 = name[shuf[0]]
        s2 = name[shuf[1]]
        s3 = name[shuf[2]]

        p1 = "{%d} over {%d}" % (nums[shuf[0]], tot)
        p2 = "{%d} over {%d}" % (nums[shuf[1]], tot-1)
        p3 = "{%d} over {%d}" % (nums[shuf[2]], tot-2)

        ctr = ctr_frac2(nums[shuf[0]]*nums[shuf[1]]*nums[shuf[2]], tot*(tot-1)*(tot-2))
        ans = "{%d} over {%d}" % (ctr[0], ctr[1])
    else:
        s1 = name[shuf[0]]
        s2 = name[shuf[1]]
        s3 = name[shuf[1]]

        p1 = "{%d} over {%d}" % (nums[shuf[0]], tot)
        p2 = "{%d} over {%d}" % (nums[shuf[1]], tot-1)
        p3 = "{%d} over {%d}" % (nums[shuf[1]]-1, tot-2)

        ctr = ctr_frac2(nums[shuf[0]]*(nums[shuf[1]]-1)*nums[shuf[1]], tot*(tot-1)*(tot-2))
        ans = "{%d} over {%d}" % (ctr[0], ctr[1])

    stem = stem.format(n1=n1, n2=n2, n3=n3, num1=num1, num2=num2, num3=num3, conds=conds)
    answer = answer.format(ans=ans)
    comment = comment.format(s1=s1, s2=s2, s3=s3, p1=p1, p2=p2, p3=p3, ans=ans)

    return stem, answer, comment


# 2-2-6-106
def numbercases226_Stem_076():
    stem = "$$수식$$1$$/수식$$부터 $$수식$${num1}$$/수식$$까지의 자연수가 각각 적힌 "\
        "$$수식$${num1}$$/수식$$개의 공이 들어 있는 상자에서 공 $$수식$$2$$/수식$$개를 차례로 꺼내어 두 자리의 자연수를 만들려고 한다. "\
        "첫 번째에 꺼낸 공에 적힌 수를 십의 자리의 숫자, 두 번째에 꺼낸 공에 적힌 수를 일의 자리의 숫자로 할 때, 이 자연수가 "\
        "{cond}일 확률을 구하시오. "\
        "(단, 꺼낸 공은 다시 넣지 않는다.)\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "{cond}가 되려면 일의 자리의 숫자가 {f_list} 중 하나이어야 한다.\n"\
        "{cases}"\
        "따라서 구하는 확률은\n"\
        "$$수식$$ {ans_sum}`=`{ans}`$$/수식$$\n\n"
    
    num1 = np.random.randint(4,10)
    cond_ind = np.random.randint(0,2)
    cond = ["짝수", "홀수"][cond_ind]

    fr = num1 // 2

    f_list = ""
    case_list = []
    if cond_ind == 1:
        f_list = f_list + "$$수식$$1$$/수식$$, "
        case_list.append(1)
    
    for i in range(fr):
        f_list = f_list + "$$수식$$" + str((i+1)*2 + cond_ind) + "$$/수식$$"
        case_list.append((i+1)*2 + cond_ind)
        if i != fr-1:
            f_list = f_list + ", "


    p1 = "{%d} over {%d}" % (num1-1, num1)
    p2 = "{%d} over {%d}" % (1, num1-1)
    pans = "{%d} over {%d}" % (1, num1)

    case_format = "일의 자리의 숫자가 $$수식$$%d$$/수식$$일 확률은 $$수식$${p1}`times`{p2}`=`{pans}$$/수식$$\n".format(p1=p1, p2=p2, pans=pans)
    ans_sum = ""
    cases = ""
    for i in case_list:
        cases = cases + case_format % i
        if ans_sum == "":
            ans_sum = ans_sum + pans
        else:
            ans_sum = ans_sum + "`+`" + pans
    
    ctr = ctr_frac2(len(case_list), num1)
    ans = "{%d} over {%d}" % (ctr[0], ctr[1])

    stem = stem.format(num1=num1, cond=cond)
    answer = answer.format(ans=ans)
    comment = comment.format(cond=cond, f_list=f_list, cases=cases, ans_sum=ans_sum, ans=ans)

    return stem, answer, comment


# 2-2-6-107
def numbercases226_Stem_077():
    stem = "$$수식$$rmA$$/수식$$ 주머에는 {clr1} 구슬 $$수식$${num1}$$/수식$$개, {clr2} 구슬 $$수식$${num2}$$/수식$$개가 들어 있고, "\
        "$$수식$$rmB$$/수식$$ 주머니에는 {clr1} 구슬 $$수식$${num3}$$/수식$$개, {clr2} 구슬 $$수식$${num4}$$/수식$$개가 들어 있다. "\
        "$$수식$$rmA$$/수식$$ 주머니에서 구슬 $$수식$$1$$/수식$$개를 꺼내어 $$수식$$rmB$$/수식$$ 주머니에 넣은 후 "\
        "$$수식$$rmB$$/수식$$ 주머니에서 구슬 $$수식$$1$$/수식$$개를 꺼낼 때, {clr2} 구슬일 확률은?\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "(1) $$수식$$rmA$$/수식$$ 주머니에서 {clr1} 구슬 $$수식$$1$$/수식$$개를 꺼내어 $$수식$$rmB$$/수식$$ 주머니에 넣은 후 "\
        "$$수식$$rmB$$/수식$$ 주머니에서 {clr2} 구슬 $$수식$$1$$/수식$$개를 꺼낼 확률은\n"\
        "$$수식$${p11}`times`{p12}`=`{ans1}$$/수식$$\n"\
        "(2) $$수식$$rmA$$/수식$$ 주머니에서 {clr2} 구슬 $$수식$$1$$/수식$$개를 꺼내어 $$수식$$rmB$$/수식$$ 주머니에 넣은 후 "\
        "$$수식$$rmB$$/수식$$ 주머니에서 {clr2} 구슬 $$수식$$1$$/수식$$개를 꺼낼 확률은\n"\
        "$$수식$${p21}`times`{p22}`=`{ans2}$$/수식$$\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${ans1}`+`{ans2}`=`{ans}$$/수식$$\n\n"
    
    clr = ["빨간", "주황", "노란", "초록", "파란", "검은", "흰", "형광"]
    clrs = random.sample(clr, 2)
    clr1 = clrs[0]
    clr2 = clrs[1]

    nums1 = random.sample(list(range(2,6)),2)
    nums2 = random.sample(list(range(2,6)),2)

    num1 = nums1[0]
    num2 = nums1[1]
    numa = num1 + num2

    num3 = nums2[0]
    num4 = nums2[1]
    numb = num3 + num4

    p11 = "{%d} over {%d}" % (num1, numa)
    p12 = "{%d} over {%d}" % (num4, numb+1)
    ctr1 = ctr_frac2(num1*num4, numa*(numb+1))
    ans1 = "{%d} over {%d}" % (ctr1[0], ctr1[1])

    p21 = "{%d} over {%d}" % (num2, numa)
    p22 = "{%d} over {%d}" % (num4+1, numb+1)
    ctr2 = ctr_frac2(num2*(num4+1), numa*(numb+1))
    ans2 = "{%d} over {%d}" % (ctr2[0], ctr2[1])

    ans_list = sum_frac([ctr1[0], ctr1[1]], [ctr2[0], ctr2[1]])
    ans = "{%d} over {%d}" % (ans_list[0], ans_list[1])

    example_list = make_fraction_example(ans_list[0], ans_list[1], ans_list[1] if ans_list[1] > 5 else ans_list[1]*2)

    stem = stem.format(num1=num1, num2=num2, num3=num3, num4=num4, clr1=clr1, clr2=clr2, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(clr1=clr1, clr2=clr2, p11=p11, p12=p12, ans1=ans1, \
        p21=p21, p22=p22, ans2=ans2, ans=ans)

    return stem, answer, comment


# 2-2-6-108
def numbercases226_Stem_078():
    stem = "$$수식$$rmA$$/수식$$, $$수식$$rmB$$/수식$$ 두 사람이 $$수식$$1$$/수식$$회에는 $$수식$$rmA$$/수식$$, $$수식$$2$$/수식$$회에는 $$수식$$rmB$$/수식$$, "\
        "$$수식$$3$$/수식$$회에는 $$수식$$rmA$$/수식$$, $$수식$$4$$/수식$$회에는 $$수식$$rmB$$/수식$$, $$수식$$CDOTS$$/수식$$의 순서대로 번갈아 가며 "\
        "주사위 $$수식$$1$$/수식$$개를 한 번씩 던지는 놀이를 한다. {cond} 눈이 먼저 나오는 사람이 이기는 것으로 할 때, $$수식$${num1}$$/수식$$회 이내에 "\
        "$$수식$$rmA$$/수식$$가 이길 확률을 구하시오.\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "주사위를 던져 {cond} 눈이 나올 확률은 $$수식$${frac}`=`{ans1}$$/수식$$이다.\n"\
        "이때 $$수식$${num1}$$/수식$$회 이내에 $$수식$$rmA$$/수식$$가 이기려면 $$수식$$rmA$$/수식$$는 {lists}회 중에 이겨야 한다.\n"\
        "{cases}"\
        "따라서 구하는 확률은\n"\
        "$$수식$${sums_frac}`=`{ans}$$/수식$$\n\n"

    cond_ind = np.random.randint(0,5)
    cond = ["5보다 작은 수의", "2보다 큰 수의", "짝수의", "홀수의", "3의 배수의"][cond_ind]
    frac_l =[[4,6],[4,6],[3,6],[3,6],[2,6]][cond_ind]
    frac = "{%d} over {%d}" % (frac_l[0], frac_l[1])
    ctr = ctr_frac2(frac_l[0], frac_l[1])
    ans1 = "{%d} over {%d}" % (ctr[0], ctr[1])
    ans1_rev = "{%d} over {%d}" % (ctr[1]-ctr[0], ctr[1])
    
    case1 = "(1) $$수식$$1$$/수식$$회에 $$수식$$rmA$$/수식$$가 이기려면 $$수식$$1$$/수식$$회에 {cond} 눈이 나오면 되므로 그 확률은 $$수식$${ans1}$$/수식$$\n"
    case2 = "({num}) $$수식$${n}$$/수식$$회에 $$수식$$rmA$$/수식$$가 이기려면 $$수식$${fre_lists}$$/수식$$회에 {cond} 눈이 나오고 " + \
        "$$수식$${n}$$/수식$$회에 {cond} 눈이 나오면 되므로 그 확률은\n" + \
        "$$수식$$(1`-`{ans1})^{fre_cnt}`times`{ans1}`=`({ans1_rev})^{fre_cnt}`times`{ans1}`=`{ans}$$/수식$$\n"
    
    num1 = np.random.randint(1,3) * 2 + 1
    lists = ""
    cases = ""
    fre_lists = ""
    sums_frac = ""
    num = 2
    ans_l = []

    for i in range(num1):
        if i % 2 == 0:
            if lists == "":
                lists = lists + "$$수식$$" + str(i+1) + "$$/수식$$"
                cases = cases + case1.format(cond=cond, ans1=ans1)
                ans_l.append([ctr[0], ctr[1]])
                sums_frac = sums_frac + ans1
            else:
                lists = lists + ", $$수식$$" + str(i+1) + "$$/수식$$"
                ctr_ = ctr_frac2(((ctr[1]-ctr[0])**i)*ctr[0],ctr[1]**(i+1))
                ans_l.append([ctr_[0], ctr_[1]])
                ans_ = "{%d} over {%d}" % (ctr_[0], ctr_[1])
                sums_frac = sums_frac + "`+`" + ans_
                cases = cases + case2.format(num=num, n=i+1, fre_lists=fre_lists, cond=cond, ans1=ans1, fre_cnt=i, ans1_rev=ans1_rev, ans=ans_)
                num = num + 1
        if fre_lists == "":
            fre_lists = fre_lists + "$$수식$$" + str(i+1) + "$$/수식$$"
        else:
            fre_lists = fre_lists + ", $$수식$$" + str(i+1) + "$$/수식$$"

    for i in range(len(ans_l)-1):
        ans_l[i+1] = sum_frac(ans_l[i], ans_l[i+1])
    ans = "{%d} over {%d}" % (ans_l[len(ans_l)-1][0], ans_l[len(ans_l)-1][1])

    stem = stem.format(cond=cond, num1=num1)
    answer = answer.format(ans=ans)
    comment = comment.format(cond=cond, frac=frac, ans1=ans1, num1=num1, lists=lists, cases=cases, sums_frac=sums_frac, ans=ans)

    return stem, answer, comment


# 2-2-6-109
def numbercases226_Stem_079():
    stem = "{n1}{j1}와 {n2}{j2}가 $$수식$${num1}$$/수식$$번 경기를 하여 먼저 $$수식$${num2}$$/수식$$번을 이기면 승리하는 시합을 하고 있다. "\
        "한 경기에서 {n1}{j1}가 이길 확률이 $$수식$${p1}$$/수식$$일 때, 이 시합에서 {n1}{j1}가 승리할 확률은? "\
        "(단, 비기는 경우는 없다.)\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "한 경기에서 {n1}{j1}가 질 확률은\n"\
        "$$수식$$1`-`{p1}`=`{p2}$$/수식$$\n"\
        "(1) $$수식$${num2}$$/수식$$번 경기를 하여 {n1}{j1}가 승리할 확률은 {cnt} 번 모두 이기면 되므로\n"\
        "$$수식$$({p1})^{num2}`=`{ans1}$$/수식$$\n"\
        "(2) $$수식$${num1}$$/수식$$번 경기를 하여 {n1}{j1}가 승리할 확률은 마지막에 지는 경우를 제외하고 한 번만 지면 되므로\n"\
        "$$수식$$({num1}`-`1)`times`({p1})^{num2}`times`{p2}`=`{ans2}$$/수식$$\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${sums_frac}`=`{ans}$$/수식$$\n\n"
    
    name_list = ["소현", "은정", "상균", "병호", "정익", "용권", "성회", "종호"]
    out = random.sample(name_list, 2)
    n1 = out[0]
    j1 = proc_jo(n1, 3)
    n2 = out[1]
    j2 = proc_jo(n2, 3)

    num1 = np.random.randint(3, 5)
    num2 = num1 -1
    cnt = ["두", "세"][num2-2]

    nums = random.sample(list(range(1,7)), 2)
    nums.sort()
    ctr = ctr_frac2(nums[0], nums[1])
    p1 = "{%d} over {%d}" % (ctr[0], ctr[1])
    p2 = "{%d} over {%d}" % (ctr[1]-ctr[0], ctr[1])

    ctr1 = ctr_frac2(ctr[0]**num2, ctr[1]**num2)
    ans1 = "{%d} over {%d}" % (ctr1[0], ctr1[1])
    ctr2 = ctr_frac2(num2*(ctr[0]**num2)*(ctr[1]-ctr[0]), ctr[1]**num1)
    ans2 = "{%d} over {%d}" % (ctr2[0], ctr2[1])

    sums_frac = ans1 + "`+`" + ans2

    ans_l = sum_frac([ctr1[0],ctr1[1]], [ctr2[0], ctr2[1]])
    ans = "{%d} over {%d}" % (ans_l[0], ans_l[1])

    example_list = make_fraction_example(ans_l[0], ans_l[1], ans_l[1] if ans_l[1] > 5 else ans_l[1] * 3)

    stem = stem.format(n1=n1, n2=n2, j1=j1, j2=j2, num1=num1, num2=num2, p1=p1, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(n1=n1, j1=j1, num1=num1, num2=num2, p1=p1, p2=p2, cnt=cnt, sums_frac=sums_frac, ans1=ans1, ans2=ans2, ans=ans)

    return stem, answer, comment


# 2-2-6-110
def numbercases226_Stem_080():
    stem = "{n1}{j1}와 {n2}{j2}가 {cnt1} 번의 경기 중에서 {cnt2} 번을 먼저 이기면 승리하는 게임을 한다. "\
        "한 번의 경기에서 {n1}{j1}가 이길 확률이 $$수식$${p1}$$/수식$$일 때, 이 시합에서 {n1}{j1}가 승리할 확률은? "\
        "(단, 비기는 경우는 없다.)\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "한 번의 경기에서 {n2}{j2}가 이길 확률은\n"\
        "$$수식$$1`-`{p1}`=`{p2}$$/수식$$이다.\n"\
        "(1) $$수식$${num2}$$/수식$$번 경기를 하여 {n1}{j1}가 승리할 확률은 {cnt} 번 모두 이기면 되므로\n"\
        "$$수식$$({p1})^{num2}`=`{ans1}$$/수식$$\n"\
        "(2) $$수식$${num1}$$/수식$$번 경기를 하여 {n1}{j1}가 승리할 확률은 마지막에 지는 경우를 제외하고 한 번만 지면 되므로\n"\
        "$$수식$$({num1}`-`1)`times`({p1})^{num2}`times`{p2}`=`{ans2}$$/수식$$\n"\
        "따라서 구하는 확률은\n"\
        "$$수식$${sums_frac}`=`{ans}$$/수식$$\n\n"
    
    name_list = ["주현", "성준", "상균", "병호", "정익", "용권", "성회", "종호"]
    out = random.sample(name_list, 2)
    n1 = out[0]
    j1 = proc_jo(n1, 3)
    n2 = out[1]
    j2 = proc_jo(n2, 3)

    num1 = np.random.randint(3, 5)
    num2 = num1 - 1
    cnt1 = ["세", "네"][num1-3]
    cnt2 = ["두", "세"][num2-2]
    cnt = ["두", "세"][num2-2]

    nums = random.sample(list(range(1,7)), 2)
    nums.sort()
    ctr = ctr_frac2(nums[0], nums[1])
    p1 = "{%d} over {%d}" % (ctr[0], ctr[1])
    p2 = "{%d} over {%d}" % (ctr[1]-ctr[0], ctr[1])

    ctr1 = ctr_frac2(ctr[0]**num2, ctr[1]**num2)
    ans1 = "{%d} over {%d}" % (ctr1[0], ctr1[1])
    ctr2 = ctr_frac2(num2*(ctr[0]**num2)*(ctr[1]-ctr[0]), ctr[1]**num1)
    ans2 = "{%d} over {%d}" % (ctr2[0], ctr2[1])

    sums_frac = ans1 + "`+`" + ans2

    ans_l = sum_frac([ctr1[0],ctr1[1]], [ctr2[0], ctr2[1]])
    ans = "{%d} over {%d}" % (ans_l[0], ans_l[1])

    example_list = make_fraction_example(ans_l[0], ans_l[1], ans_l[1] if ans_l[1] > 5 else ans_l[1] * 3)

    stem = stem.format(n1=n1, n2=n2, j1=j1, j2=j2, cnt1=cnt1, cnt2=cnt2, p1=p1)
    answer = answer.format(ans=ans)
    comment = comment.format(n1=n1, j1=j1, n2=n2, j2=j2, cnt=cnt, num1=num1, num2=num2, p1=p1, p2=p2, sums_frac=sums_frac, ans1=ans1, ans2=ans2, ans=ans)

    return stem, answer, comment


# 2-2-6-111
def numbercases226_Stem_081():
    stem = "$$수식$$rmA$$/수식$$팀, $$수식$$rmB$$/수식$$팀이 경기를 하는데 $$수식$${num1}$$/수식$$경기 중 $$수식$${num2}$$/수식$$경기를 먼저 이기면 우승이라 한다. "\
        "$$수식$$rmA$$/수식$$팀의 승률이 $$수식$${p1}$$/수식$$일 때, {cnt1} 번째 시합에서 $$수식$$rmA$$/수식$$팀이 우승할 확률을 구하시오. "\
        "(단, 비기는 경우는 없다.)\n"
    answer = "(답): $$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n"\
        "{cnt1} 번째 시합에서 $$수식$$rmA$$/수식$$팀이 우승하려면 {lists}의 순서 중 하나로 이겨야 한다.\n"\
        "$$수식$$rmB$$/수식$$팀의 승률은 $$수식$$1`-`{p1}`=`{p2}$$/수식$$\n"\
        "{cases}"\
        "따라서 구하는 확률은\n"\
        "$$수식$${sums_frac}`=`{ans}$$/수식$$\n\n"

    num1 = np.random.randint(3, 5)
    num2 = num1 - 1
    cnt1 = ["세", "네"][num1-3]

    nums = random.sample(list(range(1,7)), 2)
    nums.sort()
    ctr = ctr_frac2(nums[0], nums[1])
    p1 = "{%d} over {%d}" % (ctr[0], ctr[1])
    p2 = "{%d} over {%d}" % (ctr[1]-ctr[0], ctr[1])

    ctr2 = ctr_frac2((ctr[0]**num2)*(ctr[1]-ctr[0]), ctr[1]**num1)
    ans2 = "{%d} over {%d}" % (ctr2[0], ctr2[1])

    ctr1 = ctr_frac2(num2*(ctr[0]**num2)*(ctr[1]-ctr[0]), ctr[1]**num1)
    ans = "{%d} over {%d}" % (ctr1[0], ctr1[1])

    case = "({n}) {order}의 순서대로 이길 확률은 $$수식$${multiples}`=`{ans2}$$/수식$$\n"

    orders = []
    lists = ""
    sums_frac = ""
    cases = ""
    n = 1

    for i in range(num1-1):
        order = ""
        multiples = ""
        for j in range(num1):
            if order == "":
                if j == num1-2-i:
                    order = order + "$$수식$$rmB$$/수식$$"
                    multiples = multiples + p2
                else:
                    order = order + "$$수식$$rmA$$/수식$$"
                    multiples = multiples + p1
            else:
                if j == num1-2-i:
                    order = order + "-> $$수식$$rmB$$/수식$$"
                    multiples = multiples + "`times`" + p2
                else:
                    order = order + "-> $$수식$$rmA$$/수식$$"
                    multiples = multiples + "`times`" + p1
        
        cases = cases + case.format(n=n, order=order, multiples=multiples, ans2=ans2)
        n = n + 1

        orders.append(order)
        if lists == "":
            lists = lists + order
            sums_frac = sums_frac + ans2
        else:
            lists = lists + ", " + order
            sums_frac = sums_frac + "`+`" + ans2
    

    stem = stem.format(num1=num1, num2=num2, cnt1=cnt1, p1=p1)
    answer = answer.format(ans=ans)
    comment = comment.format(cnt1=cnt1, p1=p1, p2=p2, lists=lists, cases=cases, sums_frac=sums_frac, ans=ans)

    return stem, answer, comment


# 2-2-6-112
def numbercases226_Stem_082():
    stem = "{clr1} 공 $$수식$${num1}$$/수식$$개와 {clr2} 공 $$수식$${num2}$$/수식$$개가 들어 있는 주머니에서 한 개의 공을 꺼내고, "\
        "꺼낸 공과 색이 다른 공을 하나 넣은 후 다시 한 개의 공을 꺼낸다고 하자. 이때 꺼낸 두 공의 색이 서로 {cond} 확률은? "\
        "(단, 공은 {clr1} 공과 {clr2} 공뿐이고 꺼낸 공은 다시 넣지 않는다.)\n"\
        "① $$수식$${ex1}$$/수식$$     ② $$수식$${ex2}$$/수식$$     ③ $$수식$${ex3}$$/수식$$     ④ $$수식$${ex4}$$/수식$$     ⑤ $$수식$${ex5}$$/수식$$\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n"\
        "(1) {clr1} 공, {clr12} 공을 차례대로 꺼내는 경우\n"\
        "처음에 {clr1} 공을 꺼낼 확률은 $$수식$${p1}$$/수식$$\n"\
        "다시 꺼낼 때 주머니에는 {clr1} 공 $$수식$${num11}$$/수식$$개와 {clr2} 공 $$수식$${num21}$$/수식$$개가 들어 있으므로 "\
        "{clr12} 공을 꺼낼 확률은 $$수식$${p2}$$/수식$$\n"\
        "따라서 {clr1} 공, {clr12} 공을 차례대로 꺼낼 확률은\n"\
        "$$수식$${p1}`times`{p2}`=`{ans1}$$/수식$$\n"\
        "(2) {clr2} 공, {clr22} 공을 차례대로 꺼내는 경우\n"\
        "처음에 {clr2} 공을 꺼낼 확률은 $$수식$${p3}$$/수식$$\n"\
        "다시 꺼낼 때 주머니에는 {clr1} 공 $$수식$${num12}$$/수식$$개와 {clr2} 공 $$수식$${num22}$$/수식$$개가 들어 있으므로 "\
        "{clr22} 공을 꺼낼 확률은 $$수식$${p4}$$/수식$$\n"\
        "따라서 {clr2} 공, {clr22} 공을 차례대로 꺼낼 확률은\n"\
        "$$수식$${p3}`times`{p4}`=`{ans2}$$/수식$$\n"\
        "(1), (2)에서 구하는 확률은\n"\
        "$$수식$${ans1}`+`{ans2}`=`{ans}$$/수식$$\n\n"

    clr = ["빨간", "주황", "노란", "초록", "파란", "검은", "흰"]
    clrs = random.sample(clr, 2)
    clr1 = clrs[0]
    clr2 = clrs[1]

    nums1 = random.sample(list(range(2,6)),2)
    num1 = nums1[0]
    num2 = nums1[1]
    num11 = num1 - 1
    num21 = num2 + 1
    num12 = num1 + 1
    num22 = num2 - 1

    cond_ind = np.random.randint(0,2)
    cond = ["다를", "같을"][cond_ind]

    if cond_ind == 0:
        clr12 = clr2
        clr22 = clr1

        ctr1 = ctr_frac2(num1, num1+num2)
        p1 = "{%d} over {%d}" % (ctr1[0], ctr1[1])
        ctr2 = ctr_frac2(num2+1, num1+num2)
        p2 = "{%d} over {%d}" % (ctr2[0], ctr2[1])
        ctr3 = ctr_frac2(num2, num1+num2)
        p3 = "{%d} over {%d}" % (ctr3[0], ctr3[1])
        ctr4 = ctr_frac2(num1+1, num1+num2)
        p4 = "{%d} over {%d}" % (ctr4[0], ctr4[1])
    else:
        clr12 = clr1
        clr22 = clr2

        ctr1 = ctr_frac2(num1, num1+num2)
        p1 = "{%d} over {%d}" % (ctr1[0], ctr1[1])
        ctr2 = ctr_frac2(num1-1, num1+num2)
        p2 = "{%d} over {%d}" % (ctr2[0], ctr2[1])
        ctr3 = ctr_frac2(num2, num1+num2)
        p3 = "{%d} over {%d}" % (ctr3[0], ctr3[1])
        ctr4 = ctr_frac2(num2-1, num1+num2)
        p4 = "{%d} over {%d}" % (ctr4[0], ctr4[1])

    ctr = ctr_frac2(ctr1[0]*ctr2[0], ctr1[1]*ctr2[1])
    ans1 = "{%d} over {%d}" % (ctr[0], ctr[1])
    ctr_ = ctr_frac2(ctr3[0]*ctr4[0], ctr3[1]*ctr4[1])
    ans2 = "{%d} over {%d}" % (ctr_[0], ctr_[1])

    ans_list = sum_frac([ctr[0], ctr[1]], [ctr_[0], ctr_[1]])
    ans = "{%d} over {%d}" % (ans_list[0], ans_list[1])

    example_list = make_fraction_example(ans_list[0], ans_list[1], ans_list[1] * 3 if ans_list[1] < 5 else ans_list[1])

    stem = stem.format(num1=num1, num2=num2, clr1=clr1, clr2=clr2, cond=cond, \
        ex1=example_list[1], ex2=example_list[2], ex3=example_list[3], ex4=example_list[4], ex5=example_list[5])
    answer = answer.format(a1=answer_dict[example_list[0]])
    comment = comment.format(clr1=clr1, clr2=clr2, clr12=clr12, clr22=clr22, num11=num11, num12=num12, num21=num21, num22=num22, \
        p1=p1, p2=p2, p3=p3, p4=p4, ans1=ans1, ans2=ans2, ans=ans)

    return stem, answer, comment