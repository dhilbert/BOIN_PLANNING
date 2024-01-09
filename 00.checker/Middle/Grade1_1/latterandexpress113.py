import fractions

import numpy as np
import math

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


def divUpDown(up, down):
    g = gcd(up,down)
    return int(up // g), int(down // g)


def vtos(v,f,first=0):
    if f == 0 and first == 0:
        if v == 1:
            return "`+`"+str(v)
        elif v > 0:
            return "`+`"+str(v)
        elif v < 0:
            return str(v)
    elif f == 1 and first == 0:
        if v == 1:
            return "`+`"
        elif v > 0:
            return "`+`"+str(v)
        elif v == -1:
            return "`-`"
        elif v < 0:
            return str(v)
    elif f == 0 and first == 1:
        if v == 1:
            return str(1)
        else:
            return str(v)
    elif f == 1 and first == 1:
        if v == 1:
            return ""
        elif v > 0:
            return str(v)
        elif v == -1:
            return "`-`"
        elif v < 0:
            return str(v)

def vtos2(v):   #-붙이는거
    if v > 0:
        return "%s" % (v)
    else:
        return "LEFT ( %s RIGHT )" % (v)

def vtos3(up,down,first=0): #분수 쓰는거인듯
    if up < 0 and down < 0:
        if first == 0:
            return "`+`{%d over %d}"%(up,down)
        elif first == 1:
            return "{%d over %d}"%(up,down)

    elif up > 0 and down < 0:
        return "`-`{%d over %d}"%(up,down*-1)
    
    elif up < 0 and down > 0:
        return "`-`{%d over %d}"%(up*-1,down)
    
    elif up > 0 and down > 0:
        if first == 0:
            return "`+`{%d over %d}"%(up,down)
        elif first == 1:
            return "{%d over %d}"%(up,down)

def vtos4(up,down):     #분수의 -인건가..?
    if up * down > 0:
        return "%s" % (vtos3(up,down,1))
    else:
        return "LEFT ( %s RIGHT )" % (vtos3(up,down))

def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

def lcm(a,b):
    return abs(a * b) // gcd(a,b)

def fraction_cal_p(up1,down1,up2,down2):
    l = lcm(down1,down2)
    temp1 = l // down1
    temp2 = l // down2
    return divUpDown(temp1*up1+temp2*up2, l)

def fraction_cal_m(up1,down1,up2,down2):
    l = lcm(down1,down2)
    temp1 = l // down1
    temp2 = l // down2
    return divUpDown(temp1*up1-temp2*up2, l)

def fraction_cal_t(up1,down1,up2,down2):
    return divUpDown(up1*up2,down1*down2)




def latterandexpress113_Stem_001():
    stem = "$$수식$${s1}{s2}{s3} ^{s3_1} over {s4}{s5}+{s6}$$/수식$$을 곱셈 기호와 나눗셈 기호를 사용하여 나타내면?\n" \
           "① {c1}\n" \
           "② {c2}\n" \
           "③ {c3}\n" \
           "④ {c4}\n" \
           "⑤ {c5}\n"
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${s1}{s2}{s3} ^{s3_1} over {s4}{s5}+{s6} ` = ` " \
              "{s1}{s2}{s3} ^{s3_1} ` div ` LEFT ( {s4}{s5}+{s6} RIGHT ) $$/수식$$\n" \
              "$$수식$$` = ` {s1} ` TIMES ` {s2} ` TIMES ` {s3} ` TIMES ` {s3} ` div ` LEFT ( {s4} ` TIMES ` {s5}+{s6} RIGHT )$$/수식$$\n\n"


    s1 = np.random.randint(1, 10)
    s2 = 'a'
    s3 = "b"
    s3_1 = 2
    s4 = np.random.randint(1, 10)
    s5 = "x"
    s6 = 'y'


    s7 = "$$수식$${s1} ` TIMES ` {s2} ` TIMES ` {s3} ` TIMES ` {s3} ` DIV ` {s4} ` TIMES ` {s5}+{s6} $$/수식$$".format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6)
    s8 = "$$수식$${s1} ` TIMES ` {s2} ` TIMES ` {s3} ` TIMES ` {s3} ` TIMES ` LEFT ( {s4} ` TIMES ` {s5}+{s6} RIGHT )$$/수식$$".format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6)
    s9 = "$$수식$${s1} ` TIMES ` {s2} ` TIMES ` {s2} ` TIMES ` {s3} ` TIMES ` LEFT ( {s4} ` TIMES ` {s5}+{s6} RIGHT )$$/수식$$".format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6)
    s10 = "$$수식$${s1} ` TIMES ` {s2} ` TIMES ` {s3} ` TIMES ` {s3} ` DIV ` LEFT ( {s4} ` TIMES ` {s5}+{s6} RIGHT )$$/수식$$".format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6)
    s11 = "$$수식$${s1} ` TIMES ` {s2} ` TIMES ` {s2} ` TIMES ` {s3} ` DIV ` LEFT ( {s4} ` TIMES ` {s5}+{s6} RIGHT )$$/수식$$".format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6)


    candidates = [s7, s8, s9, s10, s11]

    np.random.shuffle(candidates)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == s10:
            correct_idx = i
            break


    stem = stem.format(s1=s1, s2=s2, s3=s3, s3_1=s3_1, s4=s4, s5=s5, s6=s6, s7=s7
                       , c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s3_1=s3_1)

    return stem, answer, comment












def latterandexpress113_Stem_002():
    stem = "다음 중 수량을 [  ] 안의 단위로 나타낸 것으로 옳지 않은 것은?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{a1}"
    comment = "(해설) \n{com}\n" \
              "\n\n" \
            

    s1_v1 = "a"
    s1_v2 = "b"
    s1_v2_1 = [2,3,4,5,6,10,12,15,20,30][np.random.randint(0, 10)]

    s1_1 = "$$수식$$ {s1_v1} 시간 ` ` {s1_v2_1}{s1_v2} ` ` [분]" \
           "`=>` LEFT ( {s1_v1_1}{s1_v1} `+` {result2}{s1_v2} RIGHT ) 분 $$/수식$$" \
           .format(s1_v1=s1_v1,s1_v2=s1_v2,s1_v2_1=s1_v2_1, result2 = s1_v2_1, s1_v1_1=60) # to minute correct
    s1_2 = "$$수식$$ {s1_v1} 시간 ` ` {s1_v2_1}{s1_v2} ` ` [분]" \
           "`=>` LEFT ( {s1_v1} `+` {s1_v2} over {result2}  RIGHT ) 분 $$/수식$$" \
           .format(s1_v1=s1_v1,s1_v2=s1_v2,s1_v2_1=s1_v2_1, result2 = 60 //s1_v2_1) # to minute in incorrect

    s1_3 = "$$수식$$ {s1_v1} 시간 ` ` {s1_v2_1}{s1_v2} ` ` [시]" \
           "`=>` LEFT ( {s1_v1} `+` {s1_v2} over {result2}  RIGHT ) 시 $$/수식$$" \
           .format(s1_v1=s1_v1,s1_v2=s1_v2,s1_v2_1=s1_v2_1, result2 = 60 //s1_v2_1) # to clock in correct
    s1_4 = "$$수식$$ {s1_v1} 시간 ` ` {s1_v2_1}{s1_v2} ` ` [시]" \
           "`=>` LEFT ( {s1_v1_1}{s1_v1} `+` {result2}{s1_v2} RIGHT ) 시 $$/수식$$" \
           .format(s1_v1=s1_v1,s1_v2=s1_v2,s1_v2_1=s1_v2_1, result2 = s1_v2_1, s1_v1_1=60) # to clock incorrect


    s1 = [s1_1, s1_2, s1_3, s1_4]
    
    s2_v1 = np.random.randint(2, 10)
    s2_v2 = "y"

    s2_v2_1 = [2, 4, 8, 10][np.random.randint(0, 4)]

    s2_1 = "$$수식$$ {s2_v1}``rm L ` ` it {s2_v2_1}{s2_v2}``rm mL ` ` [L]" \
           " `=>` it LEFT ( {s2_v1} `+` 1 over {result} {s2_v2} RIGHT ) rm L $$/수식$$" \
            .format(s2_v1=s2_v1,s2_v2=s2_v2,s2_v2_1=s2_v2_1,result=1000 // s2_v2_1) # to L correct

    s2_2 = "$$수식$$ {s2_v1}``rm L ` ` it {s2_v2_1}{s2_v2}``rm mL ` ` [L]" \
           " `=>` it LEFT ( {result} `+` {s2_v2_1}{s2_v2} RIGHT ) rm L$$/수식$$" \
            .format(s2_v1=s2_v1,s2_v2=s2_v2,s2_v2_1=s2_v2_1, result=s2_v1 * 1000)  # to L incorrect

    s2_3 = "$$수식$$ {s2_v1}``rm L ` ` it {s2_v2_1}{s2_v2}``rm mL ` ` [mL]" \
           " `=>` it LEFT ( {result} `+` {s2_v2_1}{s2_v2} RIGHT ) rm L$$/수식$$" \
            .format(s2_v1=s2_v1,s2_v2=s2_v2,s2_v2_1=s2_v2_1, result=s2_v1 * 1000)  # to mL correct

    s2_4 = "$$수식$$ {s2_v1}``rm L ` ` it {s2_v2_1}{s2_v2}``rm mL ` ` [mL]" \
           " `=>` it LEFT ( {s2_v1} `+` 1 over {result} {s2_v2} RIGHT ) rm L $$/수식$$" \
            .format(s2_v1=s2_v1,s2_v2=s2_v2,s2_v2_1=s2_v2_1,result=1000 // s2_v2_1) # to mL incorrect


    s2 = [s2_1, s2_2, s2_3, s2_4]

    
    s3_v1 = 'x' 
    s3_v2 = np.random.randint(1, 10)
    s3_result1, s3_result2 = divUpDown(s3_v2,10)
    s3_err_result1, s3_err_result2 =divUpDown(s3_v2, 100)

    s3_1 = "$$수식$$ {s3_v1} 원의 ` ` {s3_v2}할 [원] " \
         "=> {result1} over {result2} {s3_v1} 원$$/수식$$" \
         .format(s3_v1=s3_v1, s3_v2=s3_v2,result1=s3_result1,result2=s3_result2) # correct

    s3_2 = "$$수식$$ {s3_v1} 원의 ` ` {s3_v2}할 [원] " \
         "=> {err_result1} over {err_result2} {s3_v1} 원$$/수식$$" \
         .format(s3_v1=s3_v1, s3_v2=s3_v2,err_result1=s3_err_result1,err_result2=s3_err_result2) # incorrect
    s3 = [s3_1,s3_2]


    s4_v1 = 'x' 
    s4_v2 = 'y'
    s4_unit = ["m", "cm"]
    s4_1 = "$$수식$$ {s4_v1}``rm m ` ` it {s4_v2}``rm cm ` ` [cm]" \
            "it => LEFT ( {s4_v1} `+` {result}{s4_v2} RIGHT ) rm cm $$/수식$$" \
            .format(s4_v1=s4_v1,s4_v2=s4_v2,result=100) # to cm correct
    s4_2 = "$$수식$$ {s4_v1}``rm m ` ` it {s4_v2}``rm cm ` ` [cm]" \
            "it => LEFT ( {result}{s4_v1} `+` {s4_v2} RIGHT )  rm cm $$/수식$$" \
            .format(s4_v1=s4_v1,s4_v2=s4_v2,result=100) # to cm incorrect

    s4_3 = "$$수식$$ {s4_v1}``rm m ` ` it {s4_v2}``rm cm ` ` [m] " \
            "it => LEFT ( {s4_v1} `+` 1 over {result} {s4_v2} RIGHT ) rm m $$/수식$$" \
            .format(s4_v1=s4_v1,s4_v2=s4_v2,result=100) # to m correct
    s4_4 = "$$수식$$ {s4_v1}``rm m ` ` it {s4_v2}``rm cm ` ` [m] " \
            "it => LEFT ( {s4_v1} `+` {result}{s4_v2} RIGHT ) rm m $$/수식$$" \
            .format(s4_v1=s4_v1,s4_v2=s4_v2,result=100) # to m incorrect
    s4 = [s4_1,s4_2,s4_3,s4_4]

    s5_v1 = 'z' 
    s5_v2 = [5,10,20,25,50][np.random.randint(0, 5)]
    _, s5_result1 = divUpDown(s5_v2,100)

    s5_1 = "$$수식$$ {s5_v1}``rm kg의 ` ` {s5_v2}% ` ` [kg]" \
        "`=>` it {s5_v1} over {s5_result1}``rm kg $$/수식$$" \
        .format(s5_v1=s5_v1,s5_v2=s5_v2,s5_result1=s5_result1) # to kg correct
    s5_2 = "$$수식$$ {s5_v1}``rm kg의 ` ` {s5_v2}% ` ` [kg]" \
        "`=>` it {s5_result1}{s5_v1}  rm kg $$/수식$$" \
        .format(s5_v1=s5_v1,s5_v2=s5_v2,s5_result1=1000 // s5_result1) # to kg incorrect

    s5_3 = "$$수식$$ {s5_v1}``rm kg의 ` ` {s5_v2}% ` ` [g]" \
        "`=>` it {s5_result1}{s5_v1}``rm g $$/수식$$" \
        .format(s5_v1=s5_v1,s5_v2=s5_v2,s5_result1=1000 // s5_result1) # to g correct
    s5_4 = "$$수식$$ {s5_v1}``rm kg의 ` ` {s5_v2}% ` ` [g]" \
        "`=>` it {s5_v1} over {s5_result1}``rm g $$/수식$$" \
        .format(s5_v1=s5_v1,s5_v2=s5_v2,s5_result1=s5_result1) # to kg incorrect

    s5 = [s5_1,s5_2,s5_3,s5_4]


    candidates = [s1,s2,s3,s4,s5]

    np.random.shuffle(candidates)

    correct_idx = np.random.randint(0, 5)
    
    c = []
    for i in range(5):
        if i == correct_idx:
            j = np.random.randint(len(candidates[i])//2) * 2 + 1
            com = candidates[i][j-1]
        else:
            j = np.random.randint(len(candidates[i])//2) * 2
        c.append(candidates[i][j])
    c1,c2,c3,c4,c5 = c

    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(com=com)

    return stem, answer, comment













def latterandexpress113_Stem_003():
    stem = "가로의 길이가 $$수식$${s1} ` ` rm cm$$/수식$$, " \
           "세로의 길이가 $$수식$${s2} ` ` rm cm$$/수식$$, " \
           "높이가 $$수식$${s3} ` ` rm cm$$/수식$$인 "\
           "{a}의 부피와 겉넓이를 $$수식$${s1}`,`{s2}`,`{s3}$$/수식$$ 를 사용한 식으로 각각 나타내시오.\n"
    answer = "(정답)\n{volume}, {outerArea}\n"
    comment = "(해설)\n" \
              "{a}의 부피는 \n"\
              "{volumeComment}\n" \
              "{a}의 겉넓이는\n" \
              "{outerAreaComment}\n\n"


    set1 = ['x', 'y', 'z']
    set2 = ['a', 'b', 'c']
    set3 = ['p', 'q', 'r']

    s = [set1,set2,set3][np.random.randint(3)]
    s1, s2, s3 = s
    a = ['정육면체','직육면체'][np.random.randint(2)]

    if a == '정육면체':
        volume = "$$수식$${s1}^3 ```` rm cm^3$$/수식$$ 또는 $$수식$${s2}^3 ```` rm cm^3$$/수식$$ 또는 $$수식$${s3}^3 ```` rm cm^3$$/수식$$".format(s1=s1, s2=s2, s3=s3)
        outerArea = "$$수식$$6{s1}^2 ```` rm cm^2$$/수식$$ 또는 $$수식$$6{s2}^2 ```` rm cm^2$$/수식$$ 또는 $$수식$$6{s3}^2 ```` rm cm^2$$/수식$$".format(s1=s1, s2=s2, s3=s3)
        volumeComment = "$$수식$${s1} `TIMES` {s2} `TIMES`{s3} `=` {s1}{s2}{s3} `=` {s1}^3 `=`{s2}^3 `=`{s3}^3 ```` LEFT ( rm cm^3 RIGHT )$$/수식$$".format(s1=s1, s2=s2, s3=s3)
        outerAreaComment = "$$수식$$ LEFT ( {s1} `TIMES` {s2} RIGHT ) TIMES 2 `+` LEFT ( {s2} `TIMES` {s3} RIGHT ) TIMES 2 `+` LEFT ( {s3} `TIMES` {s1} RIGHT ) TIMES 2  $$/수식$$\n" \
                           "$$수식$$`=` 2{s1}{s2} `+` 2{s2}{s3} `+` 2{s3}{s1} $$/수식$$\n" \
                           "$$수식$$`=` 6{s1}^2 `=` 6{s2}^2 `=` 6{s3}^2 ```` LEFT ( rm cm^2 RIGHT )$$/수식$$".format(s1=s1, s2=s2, s3=s3)

    elif a == '직육면체':
        volume = "$$수식$${s1}{s2}{s3} ```` rm cm^3$$/수식$$".format(s1=s1, s2=s2, s3=s3)
        outerArea = "$$수식$$2{s1}{s2} `+` 2{s2}{s3} `+` 2{s3}{s1} ```` rm cm^2$$/수식$$".format(s1=s1, s2=s2, s3=s3)
        volumeComment = "$$수식$${s1} `TIMES` {s2} `TIMES`{s3} `=`{s1}{s2}{s3} ```` LEFT ( rm cm^3 RIGHT )$$/수식$$".format(s1=s1, s2=s2, s3=s3)
        outerAreaComment = "$$수식$$ LEFT ( {s1} `TIMES` {s2} RIGHT ) TIMES 2 `+` LEFT ( {s2} `TIMES` {s3} RIGHT ) TIMES 2 `+` LEFT ( {s3} `TIMES` {s1} RIGHT ) TIMES 2  $$/수식$$\n" \
                           "$$수식$$`=` 2{s1}{s2} `+` 2{s2}{s3} `+` 2{s3}{s1} ```` LEFT ( rm cm^2 RIGHT ) $$/수식$$\n".format(s1=s1, s2=s2, s3=s3)


    stem = stem.format(s1=s1, s2=s2, s3=s3, a=a)
    answer = answer.format(volume=volume, outerArea=outerArea)
    comment = comment.format(a=a, volumeComment=volumeComment, outerAreaComment=outerAreaComment)

    return stem, answer, comment



















def latterandexpress113_Stem_004():
    stem = "한 권에 {s1}원인 공책 $$수식$${s2}$$/수식$$권과 $$수식$${s3}$$/수식$$자루에 {s4}원인 " \
           "색연필 $$수식$${s5}$$/수식$$자루를 사고 $$수식$${s6}$$/수식$$원을 냈을 때의 " \
           "거스름돈을 문자를 사용한 식으로 나타내면?\n" \
           "① {c1}    " \
           "② {c2}\n" \
           "③ {c3}    " \
           "④ {c4}\n" \
           "⑤ {c5}\n"
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${s6} ` - ` LEFT ( {s2} ` TIMES ` {s1} ` + ` {s4} over {s3} ` TIMES {s5} RIGHT )" \
              " ` = ` {s6} ` - ` LEFT ( {s2}{s1} ` + ` {s5}{s4} over {s3} RIGHT ) $$/수식$$\n" \
              "$$수식$$ ` = ` {s6} ` - ` {s2}{s1} ` - ` {s5}{s4} over {s3} LEFT ( 원 RIGHT ) $$/수식$$\n\n"


    things = ["공책", "사과", "축구공", "양말", "색연필", "연필"]
    units = ["권", "개", "개", "켤레", "자루", "자루"]

    idx1 = np.random.randint(len(things))
    idx2 = np.random.randint(len(things))

    while idx1 == idx2:
        idx2 = np.random.randint(len(things))
    
    t1 = things[idx1]
    t2 = units[idx1]
    t3 = things[idx2]
    t4 = units[idx2]

    s1 = 'a'
    s4 = 'b'
    while True:
        s2 = np.random.randint(2, 10)
        s3 = np.random.randint(2, 10)
        s5 = np.random.randint(2, 10)
        new_s3, new_s5 = divUpDown(s5,s3)

        s6 = np.random.randint(1, 11) * 1000
        if new_s3 != 1:
            break


    a = "$$수식$$ LEFT ( {s6} ` - ` {s2}{s1} ` - ` {new_s5} over {new_s3} {s4} RIGHT )$$/수식$$"\
                            .format(s1=s1, s2=s2, new_s3=new_s3, s4=s4,new_s5=new_s5, s6=s6)
    c1 = "$$수식$$ LEFT ( {s6} ` - ` {s1} over {s2} ` + ` {s4} over {s3}  RIGHT )$$/수식$$"\
                            .format(s1=s1, s2=s2, s3=s3, s4=s4,s5=s5, s6=s6)
    c2 = "$$수식$$ LEFT ( {s6} ` - ` {s2}{s1} ` + ` {s5}{s4} RIGHT )$$/수식$$"\
                            .format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6)
    c3 = "$$수식$$ LEFT ( {s6} ` - ` {s2}{s1} ` - ` {s5}{s4}  RIGHT )$$/수식$$"\
                            .format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6)
    c4 = "$$수식$$ LEFT ( {s6} ` - ` {s2}{s1} ` + ` {new_s5} over {new_s3} {s4} RIGHT )$$/수식$$"\
                            .format(s1=s1, s2=s2, new_s3=new_s3, s4=s4, new_s5=new_s5, s6=s6)


    candidates = [a, c1, c2, c3, c4]

    np.random.shuffle(candidates)

    c5, c6, c7, c8, c9 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == a:
            correct_idx = i
            break


    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6
                       , c1=c5, c2=c6, c3=c7, c4=c8, c5=c9)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6)

    return stem, answer, comment

def latterandexpress113_Stem_005():
    stem = "어느 중학교의 작년 남학생 수는 {man_num}이고 여학생 수는{woman_num} 이었다. " \
           "올해는 작년에 비해 남학생 수는 $$수식$${man_v}$$/수식$${man_pm}하고 여학생 수는 $$수식$${woman_v}$$/수식$${woman_pm}했다고 할 때," \
            "올해 전체 학생 수를 $$수식$${man_v} `,` {woman_v}$$/수식$$를 사용한 식으로 바르게 나타낸 것은?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{a}"
    comment = "(해설) {man_pm}한 남자학생 수가 {com_man1}이므로 올해 남학생 수는 {com_man2} \n" \
    "{woman_pm}한 여학생 수가 {com_woman1}이므로 올해 여학생 수는 {com_woman2} \n" \
    "따라서 올해 전채 학생 수는 $$수식$$ LEFT (  $$/수식$$ {com_man2} $$수식$$ RIGHT ) `+` LEFT ( $$/수식$$ {com_woman2} $$수식$$ RIGHT ) `=` $$/수식$${com_result}"

    man_num_rand = np.random.randint(3, 11)
    man_num = man_num_rand * 50
    woman_num_rand = np.random.randint(3, 11)
    woman_num = woman_num_rand * 50

    man_v = 'a'
    woman_v = 'b'
    temp = np.random.randint(2)
    man_pm = ['증가','감소'][temp]
    man_pm_sym = ['+','-'][temp]
    temp = np.random.randint(2)
    woman_pm = ['증가','감소'][temp]
    woman_pm_sym = ['+','-'][temp]

    total_num = man_num + woman_num

    man_q, man_r = divUpDown(man_num,100)
    woman_q, woman_r = divUpDown(woman_num,100)

    err_man_q = np.random.randint(1,6) * 2 + 1
    err_woman_q = np.random.randint(1,6) * 2 + 1
    err_woman_q2 = np.random.randint(1,6) * 2 + 1

    while err_man_q == man_q:
        err_man_q = np.random.randint(1,6) * 2 + 1

    while err_woman_q == woman_q:
        err_woman_q = np.random.randint(1,6) * 2 + 1

    while err_woman_q2 == woman_q or err_woman_q2 == err_woman_q:
       err_woman_q2 = np.random.randint(1,6) * 2 + 1

    temp_ans1 = "{q}{v}"
    temp_ans2 = "{q} over {r} {v}"

    man_ans = temp_ans1.format(v=man_v,q=man_q)
    woman_ans = temp_ans1.format(v=woman_v,q=woman_q)
    err_man_ans = temp_ans1.format(v=man_v,q=err_man_q)
    err_woman_ans = temp_ans1.format(v=man_v,q=err_woman_q)
    err_woman_ans2 = temp_ans1.format(v=woman_v,q=err_woman_q2)

    if man_num_rand % 2 == 0 and woman_num_rand % 2 == 1:
        woman_ans = temp_ans2.format(v=woman_v,q=woman_q,r=woman_r)
        err_woman_ans = temp_ans2.format(v=woman_v,q=err_woman_q,r=woman_r)
        err_woman_ans2 = temp_ans2.format(v=woman_v,q=err_woman_q2,r=woman_r)
        
    elif man_num_rand % 2 == 1 and woman_num_rand % 2 == 0:
        man_ans = temp_ans2.format(v=man_v,q=man_q,r=man_r)
        err_man_ans = temp_ans2.format(v=man_v,q=err_man_q,r=man_r)
       
    elif man_num_rand % 2 == 1 and woman_num_rand % 2 == 1:
        woman_ans = temp_ans2.format(v=woman_v,q=woman_q,r=woman_r)
        err_woman_ans = temp_ans2.format(v=woman_v,q=err_woman_q,r=woman_r)
        err_woman_ans2 = temp_ans2.format(v=woman_v,q=err_woman_q2,r=woman_r)
        
        man_ans = temp_ans2.format(v=man_v,q=man_q,r=man_r)
        err_man_ans = temp_ans2.format(v=man_v,q=err_man_q,r=man_r)
       

    templete = "$$수식$$ {total_num} `{man_pm_sym}` {man_ans} `{woman_pm_sym}` {woman_ans} $$/수식$$"
    a = templete.format(total_num=total_num,man_pm_sym=man_pm_sym,man_ans=man_ans,woman_pm_sym=woman_pm_sym,woman_ans=woman_ans)
    c1 = templete.format(total_num=total_num,man_pm_sym=man_pm_sym,man_ans=err_man_ans,woman_pm_sym=woman_pm_sym,woman_ans=woman_ans)
    c2 = templete.format(total_num=total_num,man_pm_sym=man_pm_sym,man_ans=man_ans,woman_pm_sym=woman_pm_sym,woman_ans=err_woman_ans)
    c3 = templete.format(total_num=total_num,man_pm_sym=man_pm_sym,man_ans=err_man_ans,woman_pm_sym=woman_pm_sym,woman_ans=err_woman_ans)
    c4 = templete.format(total_num=total_num,man_pm_sym=man_pm_sym,man_ans=err_man_ans,woman_pm_sym=woman_pm_sym,woman_ans=err_woman_ans2)

    comment_templete1 = "$$수식$$ {num} `TIMES` {v} over 100 `=` {ans} $$/수식$$"
    comment_templete2 = "$$수식$$ {num} `{pm_sym}` {ans}$$/수식$$"
    com_man1 = comment_templete1.format(num=man_num,v=man_v,ans=man_ans)
    com_man2 = comment_templete2.format(num=man_num,pm_sym=man_pm_sym,ans=man_ans)

    com_woman1 = comment_templete1.format(num=woman_num,v=woman_v,ans=woman_ans)
    com_woman2 = comment_templete2.format(num=woman_num,pm_sym=woman_pm_sym,ans=woman_ans)
    
    candidates = [a,c1,c2,c3,c4]
    np.random.shuffle(candidates)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == a:
            correct_idx = i
            break

    stem = stem.format(man_num=man_num,man_pm=man_pm,man_v=man_v,woman_num=woman_num,woman_pm=woman_pm,woman_v=woman_v,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(man_pm=man_pm,com_man1=com_man1,com_man2=com_man2,woman_pm=woman_pm,com_woman1=com_woman1,com_woman2=com_woman2,com_result=a)

    return stem, answer, comment

def latterandexpress113_Stem_006():
    stem = "길이가 $$수식$${v}``rm m $$/수식$$인 기차가 $$수식$${length}``rm m $$수식$$인 다리를 시속 $$수식$$ {speed}``rm km $$/수식$$로 완전히 통과하는 데 걸린 시간을 문자를 사용한 식으로 나타내면?\n" \
           "① {c1}\n" \
           "② {c2}\n" \
           "③ {c3}\n" \
           "④ {c4}\n" \
           "⑤ {c5}\n"
    answer = "(정답)\n{a}"
    comment = "(해설) 시속 $$수식$$ {speed}``rm km $$/수식$$는 분속 $$수식$$ {speed_m}``rm m $$/수식$$이고, 기차가 다리를 완전히 통과할 때까지 움직인 거리는 \n" \
    "{com1}\n" \
    "이므로 기차가 다리를 완전히 통과하는 데 걸린 시간은\n" \
    "{result}\n"


    v = 'a'
    length = np.random.randint(10,21) * 100
    speed = np.random.randint(1,9) * 60

    speed_m = speed * 1000 // 60
    f = "{%s `+` %d}"% (v,length)
    a = "$$수식$$ {f} over {speed_m} $$/수식$$".format(f=f,speed_m=speed_m)

    com1 = "$$수식$$ LEFT (  {f} RIGHT )$$/수식$$".format(f=f)
    
    c1 = "$$수식$$ LEFT (  {f} RIGHT ) $$/수식$$".format(f=f)
    c2 = "$$수식$$ {f} over {speed} $$/수식$$".format(f=f,speed=speed)
    c3 = "$$수식$$ {speed_m} over LEFT (  {v} `+` {length} RIGHT ) $$/수식$$".format(v=v,length=length,speed_m=speed_m)
    c4 = "$$수식$$ {speed} over LEFT (  {v} `+` {length} RIGHT ) $$/수식$$".format(v=v,length=length,speed=speed)
    
    candidates = [a,c1,c2,c3,c4]
    np.random.shuffle(candidates)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == a:
            correct_idx = i
            break

    stem = stem.format(v=v,length=length,speed=speed,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(speed=speed,speed_m=speed_m,com1=com1,result=a)

    return stem, answer, comment

def latterandexpress113_Stem_007():
    stem = "$$수식$$ {variable}`=` {value} $$/수식$$일 때, 다음 중 식의 값이 가장 큰 것은?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{a}"
    comment = "(해설) \n" \
           "① $$수식$${c1_com}$$/수식$$\n" \
           "② $$수식$${c2_com}$$/수식$$\n" \
           "③ $$수식$${c3_com}$$/수식$$\n" \
           "④ $$수식$${c4_com}$$/수식$$\n" \
           "⑤ $$수식$${c5_com}$$/수식$$\n" \
           "따라서 식의 값이 가장 큰 것은 {a}이다.\n"

    variable = ['a','x'][np.random.randint(2)]
    while True:
        value = -1 * np.random.randint(2,6)

        case1 = -1 * value ** 3
        case1_s = "`-`{variable}^3".format(variable=variable)
        case1_com = " `-`{variable}^3`=``-`LEFT ( {value} RIGHT )^3`=``-`LEFT ( {result} RIGHT )`=`{case1}".format(variable=variable,value=value,result=case1*-1,case1=case1)

        case2 = value ** 2
        case2_s = "{variable}^2".format(variable=variable)
        case2_com = "{variable}^2`=`LEFT ( {value} RIGHT )^2`=`{case2}".format(variable=variable,value=value,case2=case2)

        case3_v = -1 *  np.random.randint(2,10)
        case3 = case3_v * value
        case3_s = "{case3_v}{variable}".format(case3_v=case3_v, variable=variable)
        case3_com = "{case3_v}{variable}`=`{case3_v}`TIMES`LEFT ( {value} RIGHT )`=`{case3}".format(variable=variable,value=value,case3=case3,case3_v=case3_v)

        case4_v1 = np.random.randint(2,10)
        case4_v2 = np.random.randint(2,10)
        case4_v3 = case4_v1 * value 
        case4 = case4_v3 + case4_v2
        case4_s = "{case4_v1}{variable} `+` {case4_v2}".format(case4_v1=case4_v1,case4_v2=case4_v2, variable=variable)
        case4_com = "{case4_v1}{variable} `+` {case4_v2}`=`{case4_v1} `TIMES` LEFT ( {value} RIGHT ) `+` {case4_v2}`=`{case4_v3} `+` {case4_v2} `=` {case4}".format(variable=variable,value=value,case4=case4,case4_v1=case4_v1,case4_v2=case4_v2,case4_v3=case4_v3)

        case5_v1 = np.random.randint(2,10)
        case5_v2 = np.random.randint(2,10)
        case5_v3 = case5_v1 * value 
        case5 = case5_v3 + case5_v2
        case5_s = "{case5_v1}{variable} `+` {case5_v2}".format(case5_v1=case5_v1,case5_v2=case5_v2, variable=variable)
        case5_com = "{case5_v1}{variable} `+` {case5_v2}`=`{case5_v1} `TIMES` LEFT ( {value} RIGHT ) `+` {case5_v2}`=`{case5_v3} `+` {case5_v2} `=` {case5}".format(variable=variable,value=value,case5=case5,case5_v1=case5_v1,case5_v2=case5_v2,case5_v3=case5_v3)

        
        candidates = [(case1,case1_s,case1_com),(case2,case2_s,case2_com),(case3,case3_s,case3_com),(case4,case4_s,case4_com),(case5,case5_s,case5_com)]

        
        candidates.sort()
        if candidates[-1][0] != candidates[-2][0]:
            break

    a = candidates[-1][0]

    np.random.shuffle(candidates)

    (c1,c1_s,c1_com), (c2,c2_s,c2_com), (c3,c3_s,c3_com), (c4,c4_s,c4_com), (c5,c5_s,c5_com) = candidates
    

    correct_idx = 0
    for i, (c,_,_) in enumerate(candidates):
        if c == a:
            correct_idx = i
            break

    stem = stem.format(value=value,variable=variable,c1=c1_s,c2=c2_s,c3=c3_s,c4=c4_s,c5=c5_s)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(c1_com=c1_com,c2_com=c2_com,c3_com=c3_com,c4_com=c4_com,c5_com=c5_com,a=answer_dict[correct_idx])

    return stem, answer, comment

def latterandexpress113_Stem_008():
    stem = "$$수식$$ {variable}`=` {value} $$/수식$$일 때, 다음 중 식의 값이 나머지 넷과 다른 하나는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{a}"
    comment = "(해설) \n" \
           "① $$수식$${c1_com}$$/수식$$\n" \
           "② $$수식$${c2_com}$$/수식$$\n" \
           "③ $$수식$${c3_com}$$/수식$$\n" \
           "④ $$수식$${c4_com}$$/수식$$\n" \
           "⑤ $$수식$${c5_com}$$/수식$$\n" \
           "따라서 식의 값이 다른 것은 {a}이다.\n"

    variable = ['a','x'][np.random.randint(2)]

    value = -1 * np.random.randint(2,6)

    ca1 = []
    ca2 = []
    case1 = value ** 3
    case1_s = "{variable}^3".format(variable=variable)
    case1_com = " {case1_s}`=`LEFT ( {value} RIGHT )^3`=`{case1}".format(case1_s=case1_s,value=value,result=case1*-1,case1=case1)
    ca1.append((case1_s,case1_com))
    
    case1_v1 = value ** 3
    case1 = -1* case1_v1 
    case1_s = "`-`{variable}^3".format(variable=variable)
    case1_com = " {case1_s}`=``-`LEFT ( {value} RIGHT )^3`=``-`LEFT ( {case1_v1} RIGHT )`=`{case1}".format(case1_s=case1_s,value=value,result=case1*-1,case1=case1,case1_v1=case1_v1)
    ca2.append((case1_s,case1_com))

    case2 = -1 * (-1 * value ** 3)
    case2_s = "`-`LEFT ( `-` {variable}^3 RIGHT )".format(variable=variable)
    case2_com = "{case2_s}`=``-`LEFT ( `-`LEFT ({value}RIGHT )^3 RIGHT )`=`{case2}".format(case2_s=case2_s,value=value,case2=case2)
    ca1.append((case2_s,case2_com))

    case2 = -1 * value ** 3
    case2_s = "`-`LEFT ( `-` {variable}^3 RIGHT )".format(variable=variable)
    case2_com = "{case2_s}`=``-`LEFT ( `-`LEFT ({value}RIGHT )^3 RIGHT )`=`{case2}".format(case2_s=case2_s,value=value,case2=case2)
    ca2.append((case2_s,case2_com))

    case3_v1 = value
    case3_v2 = value ** 2
    case3 = case3_v1 * case3_v2
    case3_s = "{case3_v1}{variable}^2".format(case3_v1=case3_v1, variable=variable)
    case3_com = "{case3_s}`=`{case3_v1}`TIMES`LEFT ( {value} RIGHT )^2`=`{case3_v1}`TIMES`{case3_v2}`=`{case3}".format(case3_s=case3_s,value=value,case3=case3,case3_v1=case3_v1,case3_v2=case3_v2)
    ca1.append((case3_s,case3_com))

    case3_v1 = -1 *  value
    case3_v2 = value ** 2
    case3 = case3_v1 * case3_v2
    case3_s = "{case3_v1}{variable}^2".format(case3_v1=case3_v1, variable=variable)
    case3_com = "{case3_s}`=`{case3_v1}`TIMES`LEFT ( {value} RIGHT )^2`=`{case3_v1}`TIMES`{case3_v2}`=`{case3}".format(case3_s=case3_s,value=value,case3=case3,case3_v1=case3_v1,case3_v2=case3_v2)
    ca2.append((case3_s,case3_com))


    case4_v1 = value 
    case4_v2 = value ** 4 
    case4 = case4_v2 // case4_v1
    case4_s = "`-` {variable}^4 over {case4_v1}".format(case4_v1=case4_v1*-1,variable=variable)
    case4_com = "{case4_s}`=` LEFT ( {value} RIGHT )^4 {case4_v1}`=` `-`{case4_v2} over {case4_v1} `=` {case4}".format(case4_s=case4_s,value=value,case4=case4,case4_v1=case4_v1*-1,case4_v2=case4_v2)
    ca1.append((case4_s,case4_com))

    case4_v1 = -1 * value 
    case4_v2 = value ** 4 
    case4 = case4_v2 // case4_v1
    case4_s = "{variable}^4 over {case4_v1}".format(case4_v1=case4_v1,variable=variable)
    case4_com = "{case4_s}`=` LEFT ( {value} RIGHT )^4 {case4_v1}`=` {case4_v2} over {case4_v1} `=` {case4}".format(case4_s=case4_s,value=value,case4=case4,case4_v1=case4_v1,case4_v2=case4_v2)
    ca2.append((case4_s,case4_com))


    case5_v1 = -1 * value ** 2
    case5_v2 = (value ** 2) + value
    case5_v3 = case5_v2 * value
    case5 = case5_v1 + case5_v3 
    case5_s = "`-`{variable}^2 `+` {case5_v2}{variable}".format(case5_v1=case5_v1,case5_v2=case5_v2, variable=variable)
    case5_com = "{case5_s}`=``-`LEFT ( {value} RIGHT )^2 `+` {case5_v2}`TIMES`LEFT ( {value} RIGHT )`=`{case5_v1} `+` LEFT ({case5_v3}RIGHT ) `=` {case5}".format(case5_s=case5_s,value=value,case5=case5,case5_v1=case5_v1,case5_v2=case5_v2,case5_v3=case5_v3)
    ca1.append((case5_s,case5_com))

    case5_v1 = value ** 2
    case5_v2 = (value ** 2) + value
    case5_v3 = case5_v2 * value
    case5 = case5_v1 - case5_v3 
    case5_s = "{variable}^2 `-` {case5_v2}{variable}".format(case5_v1=case5_v1,case5_v2=case5_v2, variable=variable)
    case5_com = "{case5_s}`=`LEFT ( {value} RIGHT )^2 `-` {case5_v2}`TIMES`LEFT ( {value} RIGHT )`=`{case5_v1} `-` LEFT ({case5_v3}RIGHT ) `=` {case5}".format(case5_s=case5_s,value=value,case5=case5,case5_v1=case5_v1,case5_v2=case5_v2,case5_v3=case5_v3)
    ca2.append((case5_s,case5_com))

    idx = np.random.randint(5)
    
    if np.random.randint(2) == 0:
        candidates = ca1
        candidates[idx] = ca2[idx]
        a = ca2[idx]

    else:
        candidates = ca2
        candidates[idx] = ca1[idx]
        a = ca1[idx]

    np.random.shuffle(candidates)

    (c1_s,c1_com), (c2_s,c2_com), (c3_s,c3_com), (c4_s,c4_com), (c5_s,c5_com) = candidates

    for i, c in enumerate(candidates):
        if c == a:
            correct_idx = i
            break

    stem = stem.format(value=value,variable=variable,c1=c1_s,c2=c2_s,c3=c3_s,c4=c4_s,c5=c5_s)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(c1_com=c1_com,c2_com=c2_com,c3_com=c3_com,c4_com=c4_com,c5_com=c5_com,a=answer_dict[correct_idx])

    return stem, answer, comment

def latterandexpress113_Stem_009():
    stem = "$$수식$$ x `=` `-` 1 over {x1} `,` y `=` 1 over {y1}$$/수식$$일 때, $$수식$${x2}over x  `-` {y2} over y $$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{a}"
    comment = "(해설) \n" \
           "$$수식$${x2}over x  `-` {y2} over y `=` {x2} `DIVIDE` x `-` {y2} `DIVIDE` y$$/수식$$\n" \
            "$$수식$$`=` {x2} `DIVIDE` LEFT (`-` 1 over {x1} RIGHT ) `-` {y2} `DIVIDE` 1 over {y1} $$/수식$$\n" \
            "$$수식$$`=` {x2} `TIMES` LEFT ( `-`{x1} RIGHT ) `-` {y2} `TIMES` {y1}$$/수식$$\n" \
            "$$수식$$`=` {x3} `-` {y3} `=` {result}$$/수식$$\n"

    x1 = np.random.randint(2,8)
    x2 = np.random.randint(2,8)
    
    y1 = np.random.randint(2,8)
    y2 = np.random.randint(2,8)

    x3 = -1 * x1 * x2
    y3 = y1 * y2

    a = x3 - y3
    c = -1 * np.random.randint(2,96,4)
    while True:
        c1,c2,c3,c4 = c
        if a != c1 and a != c2 and a != c3 and a != c4:
            break
        c = -1 * np.random.randint(2,96,4)
            
    candidates=[a,c1,c2,c3,c4]

    np.random.shuffle(candidates)

    c1, c2, c3, c4, c5 = candidates
    
    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == a:
            correct_idx = i
            break

    stem = stem.format(x1=x1,x2=x2,y1=y1,y2=y2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(x1=x1,x2=x2,x3=x3,y1=y1,y2=y2,y3=y3,result=a)

    return stem, answer, comment

def latterandexpress113_Stem_010():
    stem = "$$수식$$a`:b`=1:{v1}$$/수식$$일 때 $$수식$${ss1}$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$$a`:b`=1:`{v1}$$/수식$$에서 $$수식$$b`={v1}a$$/수식$$\n" \
              "$$수식$${ss1}$$/수식$$에 대입하면\n" \
              "$$수식$${ss1} = {ss2} = {ss3} = {sresult}$$/수식$$\n\n" \


    while True:

        v1 = np.random.randint(1,10)
        v2 = np.random.randint(-9,10)
        v3 = np.random.randint(-9,10)
        v4 = np.random.randint(-9,10)
        v5 = np.random.randint(-9,10)

        if v2 == 0 or v3 == 0 or v4 == 0 or v5 == 0:
            continue
    
        vv1 = v1 * v3
        vv2 = v1 * v5

        vvv1 = v2 + vv1
        vvv2 = v4 + vv2

        if vvv1 == 0 or vvv2 == 0:
            continue

        result = divUpDown(vvv1, vvv2)
        if result[1] != 0 and abs(vvv1) < abs(vvv2):
            break

    sv1 = vtos(v2,1,1)
    sv2 = vtos(v3,1)
    sv3 = vtos(v4,1,1)
    sv4 = vtos(v5,1)

    ss1_1 = "{%sa %sb}" % (sv1,sv2)
    ss1_2 = "{%sa %sb}" % (sv3,sv4)


    ss1 = "{ss1_1} over {ss1_2}".format(ss1_1=ss1_1,ss1_2=ss1_2)
    
    svv1 = vtos(vv1,1)
    svv2 = vtos(vv2,1)

    ss2_1 = "{%sa %sa}" % (sv1,svv1)
    ss2_2 = "{%sa %sa}" % (sv3,svv2)

    ss2 = "{ss2_1} over {ss2_2}".format(ss2_1=ss2_1,ss2_2=ss2_2)
    
    svvv1 = vtos(vvv1,1,1)
    svvv2 = vtos(vvv2,1,1)

    ss3 = "{svvv1}a over {svvv2}a".format(svvv1=svvv1,svvv2=svvv2)

    sresult = vtos3(result[0],result[1],1)
    

    candidates = []
    candidates.append(sresult)
    while len(candidates) < 5:
        up = np.random.randint(-20,20)
        down = np.random.randint(-20,20)

        if down == 1 or abs(up) > abs(down) or up == 0 or down == 0:
            continue 
        
        up, down = divUpDown(up,down)


        s = vtos3(up,down,1)
        if s not in candidates:
            candidates.append(s)
    
    np.random.shuffle(candidates)
    
    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == sresult:
            correct_idx = i
            break

    stem = stem.format(v1=v1,ss1=ss1,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(v1=v1,ss1=ss1,ss2=ss2,ss3=ss3,sresult=sresult)

    return stem, answer, comment


def latterandexpress113_Stem_011():
    stem = "지면에서 초속 $$수식$$ {speed}``rm m $$/수식$$로 똑바로 위로 던져 올린 물체의 $$수식$$ t $$/수식$$초 후의 높이는 $$수식$$ LEFT ( {speed}t `-` 5t^2 RIGHT ) rm m $$/수식$$라 한다. 이 물체의 {t}초 후의 높이는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{a}"
    comment = "(해설) \n" \
           "$$수식$$ {speed}t `-` 5t^2 에 t = {t}를 대입하면$$/수식$$\n" \
            "$$수식$$ {speed}`TIMES`{t}`-`5`TIMES`{t}^2`=`{t1}`-`{t2}`=`{result}$$/수식$$\n" \
            "따라서 {t}초 후의 물체의 높이는 {result}m이다.\n"

    while True:
        speed = np.random.randint(1,10) * 5
        t = np.random.randint(1,10)
        t1 = speed * t
        t2 = 5 * t ** 2
        result = t1 - t2
        if result < 0:
            continue
        correct_idx = np.random.randint(5)
        idx = correct_idx * 5
        candidates=[]
        tf = True
        for i in range(5):
            temp = result + idx - i*5
            if temp < 0:
                tf = False
                break
            candidates.append(temp)
        candidates.sort()
        if tf:
            break
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break    
    c1, c2, c3, c4, c5 = candidates
    
    stem = stem.format(speed=speed,t=t,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(speed=speed,t=t,t1=t1,t2=t2,result=result)

    return stem, answer, comment



def latterandexpress113_Stem_012():
    stem = "$$수식$$ a `=`  {sa1_1} `,` b `=` {sb1_1} `,` c `=` {sc1_1} 일 때,  {sa2_1} {sb2_1} {sc2_1} 의 값은? $$/수식$$\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{a}"
    comment = "(해설) \n" \
           "$$수식$$ a `=`  {sa1_1} `,` b `=` {sb1_1} `,` c `=` {sc1_1}$$/수식$$이므로\n" \
            "$$수식$$ 1 over a `=` {va1} `,` 1 over b `=` {vb1} `,` 1 over c `=` {vc1} $$/수식$$\n" \
            "$$수식$$ {sa2_1} {sb2_1} {sc2_1} `=` {sa2_2}`TIMES`{sa1_2}{sb2_2}`TIMES`{sb1_2} {sc2_2}`TIMES`{sc1_2} $$/수식$$\n" \
            "$$수식$$`=` {sa3} {sb3} {sc3}`=` {vr}$$/수식$$\n"

    while True:
        va1 = np.random.randint(-7,8)
        vb1 = np.random.randint(-7,8)
        vc1 = np.random.randint(-7,8)
        if va1 == 1 or vb1 == 1 or vc1 == 1:
            continue
        
        va2 = np.random.randint(-7,8)
        vb2 = np.random.randint(-7,8)
        vc2 = np.random.randint(-7,8)

        va3 = va1 * va2
        vb3 = vb1 * vb2
        vc3 = vc1 * vc2
        if va3 != 0 and vb3 != 0 and vc3 != 0:
            break
    vr = va3 + vb3 + vc3

    sa1_1 = "1 over {va1}".format(va1=va1) if va1 > 0 else "`-`1 over {va1} ".format(va1=va1*-1)
    sb1_1 = "1 over {vb1}".format(vb1=vb1) if vb1 > 0 else "`-`1 over {vb1} ".format(vb1=vb1*-1)
    sc1_1 = "1 over {vc1}".format(vc1=vc1) if vc1 > 0 else "`-`1 over {vc1} ".format(vc1=vc1*-1)

    sa1_2 = "{va1}".format(va1=va1) if va1 > 0 else "LEFT ({va1} RIGHT )".format(va1=va1)
    sb1_2 = "{vb1}".format(vb1=vb1) if vb1 > 0 else "LEFT ({vb1} RIGHT )".format(vb1=vb1)
    sc1_2 = "{vc1}".format(vc1=vc1) if vc1 > 0 else "LEFT ({vc1} RIGHT )".format(vc1=vc1)

    sa2_1 = " {va2} over a".format(va2=va2) if va2 > 0 else "`-`{va2} over a ".format(va2=va2*-1)
    sb2_1 = "`+`{vb2} over b".format(vb2=vb2) if vb2 > 0 else "`-`{vb2} over b ".format(vb2=vb2*-1)
    sc2_1 = "`+`{vc2} over c".format(vc2=vc2) if vc2 > 0 else "`-`{vc2} over c ".format(vc2=vc2*-1)

    sa2_2 = "{va2}".format(va2=va2) if va2 > 0 else "LEFT ({va2} RIGHT )".format(va2=va2)
    sb2_2 = "`+`{vb2}".format(vb2=vb2) if vb2 > 0 else "{vb2}".format(vb2=vb2)
    sc2_2 = "`+`{vc2}".format(vc2=vc2) if vc2 > 0 else "{vc2}".format(vc2=vc2)

    sa3 = "{va3}".format(va3=va3) if va3 > 0 else "{va3}".format(va3=va3)
    sb3 = "`+`{vb3}".format(vb3=vb3) if vb3 > 0 else "{vb3}".format(vb3=vb3)
    sc3 = "`+`{vc3}".format(vc3=vc3) if vc3 > 0 else "{vc3}".format(vc3=vc3)

    sr3 = "{vr}".format(vr=vr)

    c1 = va3 - vb3 + vc3
    c2 = va3 + vb3 - vc3
    c3 = va3 - vb3 - vc3
    c4 = -1 * va3 - vb3 - vc3
    
    candidates=[vr,c1,c2,c3,c4]

    np.random.shuffle(candidates)

    c1, c2, c3, c4, c5 = candidates
    
    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == vr:
            correct_idx = i
            break
        
    stem = stem.format(sa1_1=sa1_1,sb1_1=sb1_1,sc1_1=sc1_1,sa2_1=sa2_1,sb2_1=sb2_1,sc2_1=sc2_1,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(
        sa1_1=sa1_1,sb1_1=sb1_1,sc1_1=sc1_1,
        sa2_1=sa2_1,sb2_1=sb2_1,sc2_1=sc2_1,
        sa1_2=sa1_2,sb1_2=sb1_2,sc1_2=sc1_2,
        sa2_2=sa2_2,sb2_2=sb2_2,sc2_2=sc2_2,
        sa3=sa3,sb3=sb3,sc3=sc3,
        va1=va1,vb1=vb1,vc1=vc1,
        vr=vr)

    return stem, answer, comment



def latterandexpress113_Stem_013():
    stem = "지면에서 $$수식$${vh1}``rm km $$/수식$$높아질 때마다 기온은 $$수식$$ {vt1} DEG rm C$$/수식$$씩 낮아진다고 한다. 현재 지면의 $$수식$${vt2} DEG rm C$$/수식$$기온이 일 때, 높이가 $$수식$${vh2}``rm km$$/수식$$인 곳의 기온은? \n" \
           "① $$수식$${c1} DEG rm C$$/수식$$\n" \
           "② $$수식$${c2} DEG rm C$$/수식$$\n" \
           "③ $$수식$${c3} DEG rm C$$/수식$$\n" \
           "④ $$수식$${c4} DEG rm C$$/수식$$\n" \
           "⑤ $$수식$${c5} DEG rm C$$/수식$$\n"
    answer = "(정답)\n{a}"
    comment = "(해설) \n" \
           "높이가 $$수식$$ x rm km$$/수식$$인 곳에서는 기온이 지면보다" \
           "$$수식$$ {vt1}x DEG rm C$$/수식$$ 가 낮아지므로 높이가" \
           "$$수식$${vt1}x$$/수식$$인 곳에서의 기온은 " \
           "$$수식$$ LEFT ( {vt2} `-` {vt1}x RIGHT ) DEG rm C $$/수식$$\n" \
           "$$수식$$ x `=` 3$$/수식$$ 을 $$수식$${vt2} `-` {vt1}x 에 대입하면 $$/수식$$\n" \
           "$$수식$$ {vt2} `-` {vt1}x `=` {vt2} `-` {vt1}`TIMES`{vh2} = {a} $$/수식$$\n" \
           "따라서 높이가 $$수식$$ {vh2}``rm km $$/수식$$인 곳의 기온은 $$수식$$ {a} DEG rm C$$/수식$$ 이다. \n" \

    while True:
        vh1 = 1
        vt1 = np.random.randint(1,10)
        
        vh2 = np.random.randint(2,10)
        vt2 = np.random.randint(1,30)
        a = vt2 - vt1 * vh2
        if a > -10 and a < 12 :
            break 

    idx = np.random.randint(0,5)
    candidates = [] 
    temp = a - 2 * idx

    for i in range(5):
        candidates.append(temp + i*2)

    c1, c2, c3, c4, c5 = candidates
    
    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == a:
            correct_idx = i
            break
        
    stem = stem.format(vh1=vh1,vt1=vt1,vh2=vh2,vt2=vt2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(vt1=vt1,vt2=vt2,vh2=vh2,a=a)

    return stem, answer, comment

def latterandexpress113_Stem_014():
    stem = "기호 ◆ 을 다음과 같이 계산한다고 할 때,$$수식$${sss1}$$/수식$$의 값은?\n" \
        "$$수식$${sss2}$$/수식$$\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${v1}`>`{v2}$$/수식$$이므로\n" \
              "$$수식$${ss1_1}`=`{ss1_2}={svv3}$$/수식$$\n" \
              "$$수식$${v3}`>`{v4}$$/수식$$이므로\n" \
              "$$수식$${ss1_3}`=`{ss1_4}={svv4}$$/수식$$\n" \
              "$$수식$$THEREFORE~ {sss1}$$/수식$$\n" \
              "$$수식$$= {ss2_1}$$/수식$$\n" \
              "$$수식$$= {ss2_2}$$/수식$$\n" \
              "$$수식$$= {ss3} = {result}$$/수식$$\n" \

    s1 = "LEFT { %s ◆ %s RIGHT }"
    s2 = "%s ◆ %s"
    s3 = "{cases{``x`>`y`일``때,``x`◆y`=`x`y`+`y`%s#``x` LEQ`y `일``때,``x`◆y`=x`y`+`x`%s}}"

    while True:

        v1 = np.random.randint(-9,10)
        v2 = np.random.randint(-9,10)
        v3 = np.random.randint(-9,10)
        v4 = np.random.randint(-9,10)
        v5 = np.random.randint(-9,10)

        if v1 == 0 or v2 == 0 or v3 == 0 or v4 == 0 or v5 == 0:
            continue
        
        if v1 > v2:
            vv1 = v1 * v2 + v2 + v5
        else:
            vv1 = v1 * v2 + v1 + v5

        if v3 > v4:
            vv2 = v3 * v4 + v4 + v5
        else:
            vv2 = v3 * v4 + v3 + v5

        if vv1 > vv2:
            vvv1 = vv1 * vv2
            vvv2 = vv2 + v5
        else:
            vvv1 = vv1 * vv2
            vvv2 = vv1 + v5
        result = vvv1 + vvv2
        if result < 1000 and result > -1000:
            break

    sv1 = vtos2(v1)
    sv2 = vtos2(v2)
    sv3 = vtos2(v3)
    sv4 = vtos2(v4)
    sv5 = vtos(v5,0)

    ss1_1 = s1 % (sv1,sv2)
    if v1 > v2:
        ss1_2 = "{sv1}`TIMES`{sv2}`+`{sv2} {sv5}".format(sv1=sv1,sv2=sv2,sv5=sv5)
    else:
        ss1_2 = "{sv1}`TIMES`{sv2}`+`{sv1} {sv5}".format(sv1=sv1,sv2=sv2,sv5=sv5)
        
    ss1_3 = s1 % (sv3,sv4)
    if v3 > v4:
        ss1_4 = "{sv3}`TIMES`{sv4}`+`{sv4} {sv5}".format(sv3=sv3,sv4=sv4,sv5=sv5)
    else:
        ss1_4 = "{sv3}`TIMES`{sv4}`+`{sv3} {sv5}".format(sv3=sv3,sv4=sv4,sv5=sv5)
        
    svv1 = vtos2(vv1)
    svv2 = vtos2(vv2)
    svv3 = vtos(vv1,0,1)
    svv4 = vtos(vv2,0,1)


    ss2_1 = s1 % (svv1,svv2)
    if vv1 > vv2:
        ss2_2 = "{svv1}`TIMES`{svv2}`+`{svv2} {sv5}".format(svv1=svv1,svv2=svv2,sv5=sv5)
    else:
        ss2_2 = "{svv1}`TIMES`{svv2}`+`{svv1} {sv5}".format(svv1=svv1,svv2=svv2,sv5=sv5)
        
    svvv1 = vtos(vvv1,0,1)
    svvv2 = vtos(vvv2,0)

    ss3 = "{svvv1} {svvv2}".format(svvv1=svvv1,svvv2=svvv2)

    sss1 = s2 % (s1 % (v1,v2), s1 % (v3,v4))

    sss2 = s3 % (sv5,sv5)

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(1,10)
        temp = result - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break


    stem = stem.format(sss1=sss1,sss2=sss2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(v1=v1,v2=v2,ss1_1=ss1_1,ss1_2=ss1_2,svv3=svv3,v3=v3,v4=v4,ss1_3=ss1_3,ss1_4=ss1_4,svv4=svv4,sss1=sss1,ss2_1=ss2_1,ss2_2=ss2_2,ss3=ss3,result=result)

    return stem, answer, comment




def latterandexpress113_Stem_015():
    stem = "다 음 중 일차식인 것은?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "{double_idx1}, {double_idx2}다항식의 차수가 이므로 일차식이 아니다.\n" \
              "{no_idx} 분모에 문자가 있는 식은 다항식이 아니므로 일차식이 아니다.\n" \
              "{con_idx} 상수항은 일차식이 아니다.\n" \
              "따라서 일차식은 {correct_idx}\n" \

    while True:
        v1_1 = np.random.randint(-9,10)
        v1_2 = np.random.randint(-9,10)

        v2_1 = np.random.randint(-9,10)
        v2_2 = np.random.randint(-9,10)
        v2_3 = np.random.randint(-9,10)

        v3_1 = np.random.randint(-9,10)
        v3_2 = np.random.randint(-9,10)

        v4 = np.random.randint(-9,10)

        v5_1 = np.random.randint(-9,10)
        v5_2 = np.random.randint(-9,10)
        if v1_1 * v1_2 * v2_1 * v2_2 * v2_3 * v3_1 * v3_2 * v4 * v5_1 * v5_2 != 0:
            break

    sv1_1 = vtos(v1_1,0,1)
    ss1 = "{sv1_1} + x over {v1_2}".format(sv1_1=sv1_1,v1_2=v1_2) if v1_2 > 0 else "{sv1_1} - x over {v1_2}".format(sv1_1=sv1_1,v1_2=v1_2*-1)

    sv2_1 = vtos(v2_1,1,1)
    sv2_2 = vtos(v2_2,1)
    sv2_3 = vtos(v2_3,0)
    ss2 = "{sv2_1}a {sv2_2}a^2 {sv2_3}".format(sv2_1=sv2_1,sv2_2=sv2_2,sv2_3=sv2_3)

    sv3_2 = vtos(v3_2,0)
    ss3 = "{v3_1} over b {sv3_2}".format(v3_1=v3_1,sv3_2=sv3_2) if v3_1 > 0 else "- {v3_1} over b {sv3_2}".format(v3_1=v3_1*-1,sv3_2=sv3_2)

    sv4 = vtos(v4,0,1)
    ss4 = "{sv4}".format(sv4=sv4) 

    sv5_1 = vtos(v5_1,1,1)
    sv5_2 = vtos(v5_2,1)
    ss5 = "{sv5_1}y^2 {sv5_2}y".format(sv5_1=sv5_1,sv5_2=sv5_2) 


    candidates = [ss1,ss2,ss3,ss4,ss5]

    np.random.shuffle(candidates)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == ss1:
            correct_idx = i
            break

    double_idx = []
    for i, c in enumerate(candidates):
        if c == ss2:
            double_idx.append(i)
        if c == ss5:
            double_idx.append(i)
            
    con_idx = 0
    for i, c in enumerate(candidates):
        if c == ss4:
            con_idx = i

    no_idx = 0
    for i, c in enumerate(candidates):
        if c == ss3:
            no_idx = i

    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(double_idx1=answer_dict[double_idx[0]],double_idx2=answer_dict[double_idx[1]],no_idx=answer_dict[no_idx],con_idx=answer_dict[con_idx],correct_idx=answer_dict[correct_idx])

    return stem, answer, comment

def latterandexpress113_Stem_016():
    stem = "다 음 중 일차식인 것은?\n" \
           "① $$수식$${c1} $$/수식$${sc1}\n" \
           "② $$수식$${c2} $$/수식$${sc2}\n" \
           "③ $$수식$${c3} $$/수식$${sc3}\n" \
           "④ $$수식$${c4} $$/수식$${sc4}\n" \
           "⑤ $$수식$${c5} $$/수식$${sc5}\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "{idx1} {idxc1}\n" \
              "{idx2} {idxc2}\n" \
              "{idx3} {idxc3}\n" \
              "{idx4} {idxc4}\n\n"

    while True:
        v1_1 = np.random.randint(-9,10)
        v1_2 = np.random.randint(-9,10)

        v2_1 = np.random.randint(-9,10)
        v2_2 = np.random.randint(-9,10)
        v2_3 = np.random.randint(-9,10)

        v3_1 = np.random.randint(-9,10)
        v3_2 = np.random.randint(-9,10)
        v3_3 = np.random.randint(-9,10)

        v4_1 = np.random.randint(-9,10)
        v4_2 = np.random.randint(-9,10)

        v5_1 = np.random.randint(-9,10)
        v5_2 = np.random.randint(-9,10)
        v5_3 = np.random.randint(-9,10)
        if v1_1 * v1_2 * v2_1 * v2_2 * v2_3 * v3_1 * v3_2 * v3_3 * v4_1 *v4_2 * v5_1 * v5_2 * v5_3 != 0:
            break

    sv1_1 = vtos(v1_1,1,1)
    sv1_2 = vtos(v1_2,1)
    ss1 = "{sv1_1}x {sv1_2}y".format(sv1_1=sv1_1,sv1_2=sv1_2)
    sa1 = ["의 항은 1개이다.", "의 항은 2개이다."]
    sc1 = "항은 $$수식$${sv1_1}x, {sv1_2}y$$/수식$$로 2개 이다.".format(sv1_1=sv1_1,sv1_2=sv1_2)

    sv2_1 = vtos(v2_1,1,1)
    sv2_2 = vtos(v2_2,1)
    sv2_3 = vtos(v2_3,0)
    ss2 = "{sv2_1}x {sv2_2}y {sv2_3}".format(sv2_1=sv2_1,sv2_2=sv2_2,sv2_3=sv2_3)
    sa2 = ["는 단항식이다.", "는 다항식이다."]
    sc2 = "항이 3개이므로 단항식이 아니다."

    sv3_1 = vtos(v3_1,1,1)
    sv3_2 = vtos(v3_2,1)
    sv3_3 = vtos(v3_3,0)
    ss3 = "{v3_1}x^2 {sv3_2}x {sv3_3}".format(v3_1=v3_1,sv3_2=sv3_2,sv3_3=sv3_3)
    sa3 = ["의 차수는 -2이다.", "의 차수는 2이다."]
    sc3 = "차수는 2이다."

    sv4_1 = vtos(v4_1,1,1)
    sv4_2 = vtos(v4_2,0)
    ss4 = "{sv4_1}x^2 {sv4_2}".format(sv4_1=sv4_1,sv4_2=sv4_2) 
    sa4 = ["의 상수항은 %d 이다." % (v4_2 *-1), "의 상수항은 %d 이다." % (v4_2 )]
    sc4 = "상수항은 %d 이다." % (v4_2)

    sv5_1 = vtos(v5_1,1,1)
    sv5_2 = vtos(v5_2,1)
    sv5_3 = vtos(v5_2,0)
    ss5 = "{sv5_1}x^2 {sv5_2}x".format(sv5_1=sv5_1,sv5_2=sv5_2) 
    sa5 = ["의 $$수식$$x^2$$/수식$$의 계수는 %d 이다." % (v5_1 *-1), "의 $$수식$$x^2$$/수식$$의 계수는 %d 이다." % (v5_1)]
    sc5 = "$$수식$$x^2$$/수식$$의 계수는 %d 이다." % (v5_1)


    candidates = [(ss1,sa1,sc1),(ss2,sa2,sc2),(ss3,sa3,sc3),(ss4,sa4,sc4),(ss5,sa5,sc5)]
    np.random.shuffle(candidates)
    correct_idx = np.random.randint(5)

    idx = []
    idxa = []
    idxs = []
    idxc = []
    for i, (s, a, c) in enumerate(candidates):
        idxs.append(s)
        if i != correct_idx:
            idx.append(i)
            idxa.append(a[0])
            idxc.append(c)
        else:
            idxa.append(a[1])

    stem = stem.format(
        c1=idxs[0],c2=idxs[1],c3=idxs[2],c4=idxs[3],c5=idxs[4],
        sc1=idxa[0],sc2=idxa[1],sc3=idxa[2],sc4=idxa[3],sc5=idxa[4])
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(idx1=answer_dict[idx[0]],idx2=answer_dict[idx[1]],idx3=answer_dict[idx[2]],idx4=answer_dict[idx[3]],idxc1=idxc[0],idxc2=idxc[1],idxc3=idxc[2],idxc4=idxc[3])

    return stem, answer, comment

def latterandexpress113_Stem_017():
    stem = "다음 중 일차식은 것의 개수는?\n" \
           "$$표$$$$수식$${q1},``{q2},``{q3},``{q4},$$/수식$$\n$$수식$${q5},``{q6},``{q7},``{q8}$$/수식$$        $$/표$$\n" \
           "① 1\n" \
           "② 2\n" \
           "③ 3\n" \
           "④ 4\n" \
           "⑤ 5\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${solution}$$/수식$$\n\n"

    sol = np.random.randint(0, 5)

    if (sol == 0):
        b1 = np.random.randint(3,10)
        b2 = b1*(-2)
        b3 = "`-x^2`+x`{%s}`" % (b1*(-3))
        b4 = "`{%s} over x`+{%s}`" % (b1-2, b1*2)
        b5 = "`{%s} over x`" % (b1 + 1)
        b6 = "`-{%s}x^3`" % (b1+2)
        b7 = "`{%s}x^2`" % (b1+4)
        b8 = "`{%s}x`+`{%s}`" % (b1-1,b1-2)
        solution = "일차식은``{%s}의``1개이다." % (b8)
        N = [b1,b2,b3,b4,b5,b6,b7,b8]
        np.random.shuffle(N)
        q1, q2, q3, q4, q5, q6, q7, q8 = N
        answer_num = "①"
    elif (sol == 1):
        b1 = np.random.randint(3, 10)
        b2 = b1 * (-2)
        b3 = "`-x^2`+x`{%s}`" % (b1 * (-3))
        b4 = "`{%s} over x`+{%s}`" % (b1 - 2, b1 * 2)
        b5 = "`{%s} over x`" % (b1 + 1)
        b6 = "`-{%s}x^3`" % (b1 + 2)
        b7 = "`{%s}`+`x over {%s}`" % ( b1 + 2, b1 * 2)
        b8 = "`{%s}x`+`{%s}`" % (b1 - 1, b1 - 2)
        solution = "일차식은``{%s},``{%s}의``2개이다." % (b8, b7)
        N = [b1, b2, b3, b4, b5, b6, b7, b8]
        np.random.shuffle(N)
        q1, q2, q3, q4, q5, q6, q7, q8 = N
        answer_num = "②"
    elif (sol == 2):
        b1 = np.random.randint(3, 10)
        b2 = b1 * (-2)
        b3 = "`-x^2`+x`{%s}`" % (b1 * (-3))
        b4 = "`{%s} over x`+{%s}`" % (b1 - 2, b1 * 2)
        b5 = "`{%s} over x`" % (b1 + 1)
        b6 = "`{%s}-{%s}x`" % (b1 + 2, b1/10)
        b7 = "`{%s}`+`x over {%s}`" % ( b1 + 2, b1 * 2)
        b8 = "`{%s}x`+`{%s}`" % (b1 - 1, b1 - 2)
        solution = "일차식은``{%s},``{%s},``{%s}의``3개이다." % (b8, b7, b6)
        N = [b1, b2, b3, b4, b5, b6, b7, b8]
        np.random.shuffle(N)
        q1, q2, q3, q4, q5, q6, q7, q8 = N
        answer_num = "③"
    elif (sol == 3):
        b1 = np.random.randint(3, 10)
        b2 = b1 * (-2)
        b3 = "`-x^2`+x`{%s}`" % (b1 * (-3))
        b4 = "`{%s} over x`+{%s}`" % (b1 - 2, b1 * 2)
        b5 = "`x over {%s}`+`1`" % (b1 + 1)
        b6 = "`{%s}-{%s}x`" % (b1 + 2, b1 / 10)
        b7 = "`{%s}`+`x over {%s}`" % ( b1 + 2, b1 * 2)
        b8 = "`{%s}x`+`{%s}`" % (b1 - 1, b1 - 2)
        solution = "일차식은``{%s},``{%s},``{%s},``{%s}의``4개이다." % (b8, b7, b6, b5)
        N = [b1, b2, b3, b4, b5, b6, b7, b8]
        np.random.shuffle(N)
        q1, q2, q3, q4, q5, q6, q7, q8 = N
        answer_num = "④"
    else:
        b1 = np.random.randint(3, 10)
        b2 = b1 * (-2)
        b3 = "`-x^2`+x`{%s}`" % (b1 * (-3))
        b4 = "`{%s}x`+`{%s}`" % (b1 - 2, b1 * 2)
        b5 = "`x over {%s}`+`1`" % (b1 + 1)
        b6 = "`{%s}-{%s}x`" % (b1 + 2, b1 / 10)
        b7 = "`{%s}`+`x over {%s}`" % ( b1 + 2, b1 * 2)
        b8 = "`{%s}x`+`{%s}`" % (b1 - 1, b1 - 2)
        solution = "일차식은``{%s},``{%s},``{%s},``{%s},``{%s}의``5개이다." % (b8, b7, b6, b5, b4)
        N = [b1, b2, b3, b4, b5, b6, b7, b8]
        np.random.shuffle(N)
        q1, q2, q3, q4, q5, q6, q7, q8 = N
        answer_num = "⑤"

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(solution=solution)

    return stem, answer, comment

def latterandexpress113_Stem_018():
    stem = "다항식 $$수식$${s1}$$/수식$$가 $$수식$$x$$/수식$$에 대한 일차식이 되도록 하는 상수 $$수식$$a, b$$/수식$$의 조건으로 알맞은 것은?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "주어진 다항식이 에 대한 일차식이 되려면\n" \
              "$$수식$${ss1}, {ss2}$$/수식$$이어야 하므로\n" \
              "$$수식$${result}$$/수식$$\n\n"



    while True:
        v1 = np.random.randint(-9,10)
        v2 = np.random.randint(-9,10)
        v3 = np.random.randint(-9,10)

        if v1 * v2 * v3 != 0:
            break
    sv1 = vtos(v1,0,1)
    sv2 = vtos(v2,0)
    sv3 = vtos(v3,0)
    s1 = "LEFT ( {sv1} `+` a RIGHT )x^2 `+` LEFT ( b {sv2} RIGHT ) {sv3}".format(sv1=sv1,sv2=sv2,sv3=sv3)

    ss1 = "{sv1}`+` a `=` 0".format(sv1=sv1)
    ss2 = "b {sv2} `!=` 0".format(sv2=sv2)
    
    svv1 = vtos(v1*-1,0,1)
    svv2 = vtos(v2*-1,0,1)

    sss1_1 = " a `=` {v1}".format(v1=v1*-1)
    sss2_1 = ", b `!=` {v2}".format(v2=v2*-1)
    
    sss1_2 = " a `!=` {v1}".format(v1=v1)
    sss2_2 = ", b `!=` {v2}".format(v2=v2)

    result = sss1_1 + sss2_1
    c1 = sss1_1 + sss2_2
    c2 = sss1_2 + sss2_1
    c3 = sss1_1 + sss2_2
    c4 = sss1_1 

    candidates = [result,c1,c2,c3,c4]
    np.random.shuffle(candidates)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(s1=s1,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(ss1=ss1,ss2=ss2,result=result)

    return stem, answer, comment

def latterandexpress113_Stem_019():
    stem = "다항식 $$수식$$□$$/수식$$안에 알맞은 수 중 가장 작은 것은?\n" \
           "① $$수식$${c1_1} `=` {c1_2}$$/수식$$\n" \
           "② $$수식$${c2_1} `=` {c2_2}$$/수식$$\n" \
           "③ $$수식$${c3_1} `=` {c3_2}$$/수식$$\n" \
           "④ $$수식$${c4_1} `=` {c4_2}$$/수식$$\n" \
           "⑤ $$수식$${c5_1} `=` {c5_2}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${idx1} {c1_1} `=` {c1_2}$$/수식$$\n" \
              "$$수식$${idx2} {c2_1} `=` {c2_2}$$/수식$$\n" \
              "$$수식$${idx3} {c3_1} `=` {c3_2}$$/수식$$\n" \
              "$$수식$${idx4} {c4_1} `=` {c4_2}$$/수식$$\n" \
              "$$수식$${idx5} {c5_1} `=` {c5_2}$$/수식$$\n\n" 


    while True:
        # + int (int int)
        v1_1 = np.random.randint(2,10)
        v1_2 = np.random.randint(1,10)
        v1_3 = np.random.randint(1,10)
        
        vv1 = [v1_1 * v1_2, v1_1 * v1_3]

        # + int (분수 분수)
        v2_2 = np.random.randint(1,5)
        v2_3 = np.random.randint(v2_2+1,11)
        v2_2, v2_3 = divUpDown(v2_2,v2_3)
        
        v2_4 = np.random.randint(1,5)
        v2_5 = np.random.randint(v2_4+1,11)
        v2_4, v2_5 = divUpDown(v2_4,v2_5)

        v2_1 = lcm(v2_3,v2_5)
        vv2 = [(v2_1 * v2_2) // v2_3, (v2_1 * v2_4) // v2_5]

        # - int (-int -int)
        v3_1 = np.random.randint(-9,0)
        v3_2 = np.random.randint(-9,0)
        v3_3 = np.random.randint(-9,0)
        
        vv3 = [v3_1 * v3_2, v3_1 * v3_3]

        # - int (분수 분수)
        # v4_1 = np.random.randint(-11,-1)
        v4_2 = np.random.randint(1,5)
        v4_3 = np.random.randint(v4_2+1,11)
        v4_2, v4_3 = divUpDown(v4_2,v4_3)

        v4_4 = np.random.randint(1,5)
        v4_5 = np.random.randint(v4_4+1,11)
        v4_4, v4_5 = divUpDown(v4_4,v4_5)
        
        v4_1 = lcm(v4_3,v4_5) * -1
        vv4 = [( v4_1 * v4_2) // v4_3, ( v4_1 * v4_4) // v4_5]

        # + 분수 (int int)
        v5_2 = np.random.randint(2,10)
        v5_3 = np.random.randint(2,10)

        v5_1 = lcm(v5_2,v5_3)
        vv5 = [v5_2 // v5_1, v5_3 // v5_1]

        r1 = np.random.randint(2)
        vvv1 = vv1[r1] 
        r2 = np.random.randint(2)
        vvv2 = vv2[r2]
        r3 = np.random.randint(2)
        vvv3 = vv3[r3]
        r4 = np.random.randint(2)
        vvv4 = vv4[r4]
        if r4 == 1:
            vvv4 *= -1
        r5 = np.random.randint(2)
        vvv5 = vv5[r5]

        if v2_1 % v2_3 ==0 and v2_1 % v2_5 == 0 and v4_1 % v4_3 ==0 and v4_1 % v4_5 == 0 and  v5_2 % v5_1 ==0 and v5_3 % v5_1 == 0 \
            and len(set([vvv1,vvv2,vvv3,vvv4,vvv5])) == 5:
            break

    stemp1 = "%s LEFT ( %s x %s RIGHT ) "

    stemp2 = ["□ x %s", "%s x `+` □"]
    sctemp2 = ["{b} x %s", "%s x `+` {b}"]

    stemp3 = ["□  x %s", "%s x `-` □"]
    sctemp3 = ["{b} x %s", "%s x `-` {b}"]
    
    sv1_1 = vtos(v1_1,1,1)
    sv1_2 = vtos(v1_2,1,1)
    sv1_3 = vtos(v1_3,0)
    s1 = stemp1 % (sv1_1,sv1_2,sv1_3)
    
    svv1 = [vtos(vv1[1],0), vtos(vv1[0],1,1)]
    sc1 = stemp2[r1] % (svv1[r1])
    scc1 = sctemp2[r1].format(b=vvv1) % (svv1[r1])
    

    sv2_1 = vtos(v2_1,1,1)
    sv2_2 = vtos3(v2_2,v2_3,1)
    sv2_3 = vtos3(v2_4,v2_5)
    s2 = stemp1 % (sv2_1,sv2_2,sv2_3)
 
    svv2 = [vtos(vv2[1],0), vtos(vv2[0],1,1)]
    sc2 = stemp2[r2] % (svv2[r2])
    scc2 = sctemp2[r2].format(b=vvv2) % (svv2[r2])


    sv3_1 = vtos(v3_1,1,1)
    sv3_2 = vtos(v3_2,1,1)
    sv3_3 = vtos(v3_3,0)
    s3 = stemp1 % (sv3_1,sv3_2,sv3_3)


    svv3 = [vtos(vv3[1],0), vtos(vv3[0],1,1)]
    sc3 = stemp2[r3] % (svv3[r3])
    scc3 = sctemp2[r3].format(b=vvv3) % (svv3[r3])


    sv4_1 = vtos(v4_1,1,1)
    sv4_2 = vtos3(v4_2,v4_3,1)
    sv4_3 = vtos3(v4_4,v4_5)
    s4 = stemp1 % (sv4_1,sv4_2,sv4_3)

    svv4 = [vtos(vv4[1],0), vtos(vv4[0],1,1)]
    sc4 = stemp3[r4] % (svv4[r4])
    scc4 = sctemp3[r4].format(b=vvv4) % (svv4[r4])


    sv5_1 = vtos3(1,v5_1,1)
    sv5_2 = vtos(v5_2,1,1)
    sv5_3 = vtos(v5_3,0)
    s5 = stemp1 % (sv5_1,sv5_2,sv5_3)

    svv5 = [vtos(vv5[1],0), vtos(vv5[0],1,1)]
    sc5 = stemp2[r5] % (svv5[r5])
    scc5 = sctemp2[r5].format(b=vvv5) % (svv5[r5])

    candidates = [(vvv1,s1,sc1,scc1),(vvv2,s2,sc2,scc2),(vvv3,s3,sc3,scc3),(vvv4,s4,sc4,scc4),(vvv5,s5,sc5,scc5)]

    candidates.sort()

    result = candidates[0][0]
    
    np.random.shuffle(candidates)

    idx = []
    idxs = []
    idxc = []
    idxcc = []
    correct_idx = 0
    for i, (v,s,sc,scc) in enumerate(candidates):
        if v == result:
            correct_idx = i
        idx.append(i)
        idxs.append(s)
        idxc.append(sc)
        idxcc.append(scc)

    stem = stem.format(
        c1_1=idxs[0],c2_1=idxs[1],c3_1=idxs[2],c4_1=idxs[3],c5_1=idxs[4],
        c1_2=idxc[0],c2_2=idxc[1],c3_2=idxc[2],c4_2=idxc[3],c5_2=idxc[4])
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(
        idx1=answer_dict[idx[0]],idx2=answer_dict[idx[1]],idx3=answer_dict[idx[2]],idx4=answer_dict[idx[3]],idx5=answer_dict[idx[4]],
        c1_1=idxs[0],c2_1=idxs[1],c3_1=idxs[2],c4_1=idxs[3],c5_1=idxs[4],
        c1_2=idxcc[0],c2_2=idxcc[1],c3_2=idxcc[2],c4_2=idxcc[3],c5_2=idxcc[4])

    return stem, answer, comment



def latterandexpress113_Stem_020():
    stem = "다음 중 계산 결과가 나머지 넷과 다른 하나는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "{idx1} {idx2} {idx3} {idx4} $$수식$${result1}$$/수식$$" \
              "{idx_res} $$수식$${result3}`=`{result2}$$/수식$$"



    while True:
        # (int int) X int
        v1_1 = np.random.randint(-5,6)
        v1_2 = np.random.randint(-5,6)
        v1_3 = np.random.randint(-5,6)
        if v1_1 == 0 or v1_2 == 0 or v1_3 == 0:
            continue
        vv1_1 = v1_1 * v1_3
        vv1_2 = v1_2 * v1_3

        # (int int) X 분수
        v2_3 = np.random.randint(-9,10)
        if v2_3 == 0 or abs(v2_3) == 1:
            continue
        v2_1 = vv1_1 * v2_3
        v2_2 = vv1_2 * v2_3

        vv2_1 = v2_1 // v2_3
        vv2_2 = v2_2 // v2_3

        # (int int) / int
        v3_3 = np.random.randint(-9,10)
        if v3_3 == 0 or abs(v3_3) == 1:
            continue
        v3_1 = vv1_1 * v3_3
        v3_2 = vv1_2 * v3_3

        vv3_1 = v3_1 // v3_3
        vv3_2 = v3_2 // v3_3

        # (int int) / 분수
        v4_3 = np.random.randint(-9,10)
        if v4_3 == 0 or abs(v4_3) == 1:
            continue        
        v4_1 = vv1_1 // v4_3
        v4_2 = vv1_2 // v4_3

        vv4_1 = v4_1 * v4_3
        vv4_2 = v4_2 * v4_3

        # (int 분수) / 분수 
        v5_3 = np.random.randint(-9,10)
        if v5_3 == 0 or abs(v5_3) == 1:
            continue
        v5_1 = vv1_1 // v5_3
        v5_2 = v5_3 // vv1_2 
        if v5_3 % vv1_2 != 0 or abs(v5_2) == 1:
            continue
        vv5_1 = v5_1 * v5_3
        vv5_2 = v5_3 // v5_2

        if vv1_1 == vv2_1 and vv2_1 == vv3_1 and vv3_1 == vv4_1 and vv4_1 == vv5_1 and \
           vv1_2 == vv2_2 and vv2_2 == vv3_2 and vv3_2 == vv4_2 and vv4_2 == vv5_2 and \
           v1_1 != 0 and v2_1 != 0 and v3_1 != 0 and v4_1 != 0 and v5_1 != 0 and \
           v1_2 != 0 and v2_2 != 0 and v3_2 != 0 and v4_2 != 0 and v5_2 != 0:
            break

    a = np.random.randint(5)

    stemp1 = "LEFT ( %s x %s RIGHT ) `TIMES` %s"
    stemp2 = "LEFT ( %s x %s RIGHT ) `DIVIDE` %s"
 
    candidates_v = [[v1_1,v1_2,v1_3],[v2_1,v2_2,v2_3],[v3_1,v3_2,v3_3],[v4_1,v4_2,v4_3],[v5_1,v5_2,v5_3]]

    t = np.random.randint(3)
    candidates_v[a][t] *= -1

    candidates = []
    candidates_vv = []
    for i in range(5):
        v1, v2, v3 = candidates_v[i]
        if i == 0:
            candidates.append(stemp1 % (vtos(v1,1,1),vtos(v2,0), vtos2(v3)) )
            vv1 = v1 * v3
            vv2 = v2 * v3
        elif i == 1:
            candidates.append(stemp1 % (vtos(v1,1,1),vtos(v2,0), vtos4(1, v3)) )
            vv1 = v1 // v3
            vv2 = v2 // v3
        elif i == 2:
            candidates.append(stemp2 % (vtos(v1,1,1),vtos(v2,0), vtos2(v3)) )
            vv1 = v1 // v3
            vv2 = v2 // v3
        elif i == 3:
            candidates.append(stemp2 % (vtos(v1,1,1),vtos(v2,0), vtos4(1, v3)) )
            vv1 = v1 * v3
            vv2 = v2 * v3
        else:
            candidates.append(stemp2 % (vtos(v1,1,1),vtos3(1, v2, 0), vtos4(1, v3)) )
            vv1 = v1 * v3
            vv2 = v3 // v2
        candidates_vv.append((vv1,vv2))
        

    result1 = "%s x %s" % ( candidates_vv[a-1][0], vtos(candidates_vv[a-1][1],0) )
    result2 = "%s x %s" % ( candidates_vv[a][0], vtos(candidates_vv[a][1] ,0))
    result3 = candidates[a]

    candidates.sort()

    np.random.shuffle(candidates)

    c1, c2, c3, c4, c5 = candidates

    idx = []
    for i, c in enumerate(candidates):
        if c == result3:
            correct_idx = i
        else:
            idx.append(i)

    stem = stem.format(c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(
        idx1=answer_dict[idx[0]],idx2=answer_dict[idx[1]],idx3=answer_dict[idx[2]],idx4=answer_dict[idx[3]],idx_res=answer_dict[correct_idx],result1=result1,result2=result2,result3=result3)

    return stem, answer, comment

def latterandexpress113_Stem_021():
    stem = "$$수식$${s1}`=`ax`+`b$$/수식$$일 때 상수 $$수식$$a, b$$/수식$$에 대하여 $$수식$$a `+` b$$/수식$$의 값은?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${s1}`=`{s2}`=`{s3}$$/수식$$이므로\n" \
              "$$수식$$a`=`{vv1}, b`=`{vv2}$$/수식$$\n" \
              "$$수식$$a`+`b`=`{s4}`=`{result}$$/수식$$\n\n"



    while True:
        v1 = np.random.randint(-9,10)
        v2 = np.random.randint(-9,10)
        v3 = np.random.randint(2,10)

        if v1 == 0 or v2 == 0:
            continue

        vv1 = v1 * v3
        vv2 = v1 * v2
        
        result = vv1+vv2
        if vv1 != 0 and vv2 != 0:
            break

    sv1 = vtos(v1,1,1)
    sv2 = vtos(v2,0)

    s1 = "LEFT ( {sv1}x {sv2} RIGHT ) `DIVIDE` 1 over {v3}".format(sv1=sv1,sv2=sv2,v3=v3)
    s2 = "LEFT ( {sv1}x {sv2} RIGHT ) `TIMES` {v3}".format(sv1=sv1,sv2=sv2,v3=v3)
    
    svv1 = vtos(vv1,1,1)
    svv2 = vtos(vv2,0)
    s3 = "{svv1}x{svv2}".format(svv1=svv1,svv2=svv2)
    s4 = "{svv1}{svv2}".format(svv1=svv1,svv2=svv2)

    idx = np.random.randint(0,5)
    candidates = []

    res_interval = np.random.randint(1,4) 
    temp = result - res_interval * idx

    for i in range(5):
        candidates.append(temp + res_interval * i)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(s1=s1,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,s3=s3,vv1=vv1,vv2=vv2,s4=s4,result=result)

    return stem, answer, comment

def latterandexpress113_Stem_022():
    stem = "어떤 일차식을 $$수식$${sv1}$$/수식$$로 나누어야 할 것을 잘못하여 $$수식$${sv1}$$/수식$$을 곱했더니 $$수식$${s1}$$/수식$$이 되었다. 이때 바르게 계산한 식은?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "어떤 일차식을 $$수식$$BOX~~$$/수식$$라 하면\n" \
              "$$수식$${ss1}$$/수식$$이므로\n" \
              "$$수식$${ss2}`=`{ss3}`=`{ss4}$$/수식$$\n" \
              "즉, 어떤 일차식은 $$수식$${ss4}$$/수식$$이다.\n" \
              "따라서 바르게 계산한 식은\n" \
              "$$수식$${sss1}`=`{sss2}`=`{sss3}$$/수식$$\n\n" 

    while True:
        v1 = np.random.randint(-7,8)
        v2 = np.random.randint(-6,7)
        v3 = np.random.randint(-6,7)
        
        if v1 == 0 or v2 == 0 or abs(v1) == 1:
            continue

        vv1 = v1 * v2
        vv2 = v1 * v3

        vvv1 = vv1 * v1
        vvv2 = vv2 * v1
        break

    sv1 = vtos3(1,v1,1)
    sv2 = vtos(v2,1,1)
    sv3 = vtos(v3,0)
    
    s1 = "{sv2}x{sv3}".format(sv2=sv2,sv3=sv3)

    sv4 = vtos4(1,v1)
    sv5 = vtos2(v1)
    
    ss1 = "BOX~~`TIMES`{sv4}`=`{s1}".format(sv4=sv4,s1=s1)
    ss2 = "BOX~~`=`LEFT ( {s1} RIGHT ) `DIVIDE` {sv4} ".format(s1=s1,sv4=sv4)
    ss3 = "BOX~~`=`LEFT ( {s1} RIGHT ) `TIMES` {sv5} ".format(s1=s1,sv5=sv5)
    
    svv1 = vtos(vv1,1,1)
    svv2 = vtos(vv2,0)
    
    ss4 = "{svv1}x{svv2}".format(svv1=svv1,svv2=svv2)

    sss1 = "LEFT ( {ss4} RIGHT ) `DIVIDE`{sv4}".format(ss4=ss4,sv4=sv4)
    sss2 = "LEFT ( {ss4} RIGHT ) `TIMES`{sv5}".format(ss4=ss4,sv5=sv5)
    
    svvv1 = vtos(vvv1,1,1)
    svvv2 = vtos(vvv2,0)
    
    sss3 = "{svvv1}x{svvv2}".format(svvv1=svvv1,svvv2=svvv2)

    temp = "%sx %s"

    c1 = temp % (svv1,svv2) 
    c2 = temp % (svv1,svvv2) 
    c3 = temp % (svvv1,svv2) 
    c4 = temp % (sv2,svvv2) 

    candidates = [c1,c2,c3,c4,sss3]
    np.random.shuffle(candidates)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == sss3:
            correct_idx = i
            break

    stem = stem.format(sv1=sv1,s1=s1,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(ss1=ss1,ss2=ss2,ss3=ss3,ss4=ss4,sss1=sss1,sss2=sss2,sss3=sss3)

    return stem, answer, comment

def latterandexpress113_Stem_023():
    stem = "다음 중 {a1}a와 동류항인 것의 개수는?\n" \
           "$$표$$$$수식$${q1},``{q2},``{q3},``{q4},``{q5},``{q6}$$/수식$$        $$/표$$\n" \
           "① 1\n" \
           "② 2\n" \
           "③ 3\n" \
           "④ 4\n" \
           "⑤ 5\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${solution}$$/수식$$\n\n"

    a1 = np.random.randint(2,10)
    sol = np.random.randint(0, 5)

    if (sol == 0):
        b1 = np.random.randint(3,10)
        b2 = "`{%s} over {%s}`a`" % (b1-1,b1)
        b3 = "`{%s} over a`" % (b1-1)
        b4 = "`{%s}a^2`" % (b1)
        b5 = b1 - 1
        b6 = "`{%s} over a`" % (b1*2)
        solution = "{%s}a와``동류항인``것은``{%s}이므로``구하는``개수는``1이다." % (a1,b2)
        N = [b1,b2,b3,b4,b5,b6]
        np.random.shuffle(N)
        q1, q2, q3, q4, q5, q6 = N
        answer_num = "①"
    elif (sol == 1):
        b1 = np.random.randint(3, 10)
        b2 = "`{%s} over {%s}`a`" % (b1 - 1, b1)
        b3 = "`{%s} over a`" % (b1 - 1)
        b4 = "`{%s}a^2`" % (b1)
        b5 = b1 - 1
        b6 = "`1 over {%s}`a`" % (b1 + 1)
        solution = "{%s}a와``동류항인``것은``{%s},``{%s}이므로``구하는``개수는``2이다." % (a1, b2, b6)
        N = [b1, b2, b3, b4, b5, b6]
        np.random.shuffle(N)
        q1, q2, q3, q4, q5, q6 = N
        answer_num = "②"
    elif (sol == 2):
        b1 = np.random.randint(3, 10)
        b2 = "`{%s} over {%s}`a`" % (b1 - 1, b1)
        b3 = "`{%s} over a`" % (b1 - 1)
        b4 = "`{%s}a^2`" % (b1)
        b5 = "`{%s} over {%s}`a`" % (b1*2, b1+1)
        b6 = "`1 over {%s}`a`" % (b1 + 1)
        solution = "{%s}a와``동류항인``것은``{%s},``{%s},``{%s}이므로``구하는``개수는``3이다." % (a1, b2, b5, b6)
        N = [b1, b2, b3, b4, b5, b6]
        np.random.shuffle(N)
        q1, q2, q3, q4, q5, q6 = N
        answer_num = "③"
    elif (sol == 3):
        b1 = np.random.randint(3, 10)
        b2 = "`{%s} over {%s}`a`" % (b1 - 1, b1)
        b3 = "`{%s} over {%s}`a`" % (b1*2, b1+1)
        b4 = "`a`"
        b5 = "`a over {%s}`" % (b1+1)
        b6 = "`{%s}a^2`" % (b1-1)
        solution = "{%s}a와``동류항인``것은``{%s},``{%s},``{%s},``{%s}이므로``구하는``개수는``4이다." % (a1, b2, b3, b4, b5)
        N = [b1, b2, b3, b4, b5, b6]
        np.random.shuffle(N)
        q1, q2, q3, q4, q5, q6 = N
        answer_num = "④"
    else:
        b1 = np.random.randint(3, 10)
        b2 = "`{%s} over {%s}`a`" % (b1*2, b1+1)
        b3 = "`{%s} over {%s}`a`" % (b1 - 1, b1)
        b4 = "`a over {%s}`" % (b1+1)
        b5 = "`a`"
        b6 = "`1 over {%s}`a`" % (b1 + 1)
        solution = "{%s}a와``동류항인``것은``{%s},``{%s},``{%s},``{%s},``{%s}이므로``구하는``개수는``5이다." % (a1, b2, b3, b4, b5, b6)
        N = [b1, b2, b3, b4, b5, b6]
        np.random.shuffle(N)
        q1, q2, q3, q4, q5, q6 = N
        answer_num = "⑤"

    stem = stem.format(a1=a1, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(solution=solution)

    return stem, answer, comment

def latterandexpress113_Stem_024():
    stem = "{s}을 계산한 결과는?\n" \
           "① {c1}\n" \
           "② {c2}\n" \
           "③ {c3}\n" \
           "④ {c4}\n" \
           "⑤ {c5}\n"
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${s}={ss}\n={sss}$$/수식$$\n\n"

    while True:
        v1 = np.random.randint(-10,10)
        v2 = np.random.randint(-10,10)
        v3 = np.random.randint(-10,10)
        v4 = np.random.randint(-10,10)
        v5 = np.random.randint(-10,10)
        v6 = np.random.randint(-10,10)
        vv1 = v1 * v2
        vv2 = v1 * v3
        vv3 = v4 * v5
        vv4 = v4 * v6
        vvv1 = vv1 + vv3
        vvv2 = vv2 + vv4
        if v1 != 0 and v2 != 0 and v3 != 0 and v4 != 0 and v5 != 0 and v6 != 0 and vvv1 != 0 and vvv2 != 0:
            break

    sv1 = vtos(v1,1,1)
    sv2 = vtos(v2,1,1)
    sv3 = vtos(v3,0)
    sv4 = vtos(v4,1)
    sv5 = vtos(v5,1,1)
    sv6 = vtos(v6,0)

    s = "$$수식$${sv1}LEFT ({sv2}x{sv3}RIGHT ){sv4}LEFT ({sv5}x{sv6})$$/수식$$".format(sv1=sv1,sv2=sv2,sv3=sv3,sv4=sv4,sv5=sv5,sv6=sv6)
    
    svv1 = vtos(vv1,1,1)
    svv2 = vtos(vv2,0)
    svv3 = vtos(vv3,1)
    svv4 = vtos(vv4,0)
    
    ss = "$$수식$${svv1}x{svv2}{svv3}x{svv4}$$/수식$$".format(svv1=svv1,svv2=svv2,svv3=svv3,svv4=svv4)

    svvv1 = vtos(vvv1,1,1)
    svvv2 = vtos(vvv2,0)

    result = (vvv1,vvv2)
    sss = "{}x{}".format(svvv1,svvv2)

    candidates = []
    candidates.append((vvv1,vvv2))
    while len(candidates) < 5 :
        temp1 = np.random.randint(-50,50)
        temp2 = np.random.randint(-50,50)
        if temp1 == 0 or temp2 == 0:
            continue
        f = True
        for c in candidates:
            if c == (temp1,temp2):
                f = False
                break
        if f:
            candidates.append((temp1,temp2))
    
    c1, c2, c3, c4, c5 = candidates
    c1 = "$$수식$${}x{}$$/수식$$".format(vtos(c1[0],1,1),vtos(c1[1],0))
    c2 = "$$수식$${}x{}$$/수식$$".format(vtos(c2[0],1,1),vtos(c2[1],0))
    c3 = "$$수식$${}x{}$$/수식$$".format(vtos(c3[0],1,1),vtos(c3[1],0))
    c4 = "$$수식$${}x{}$$/수식$$".format(vtos(c4[0],1,1),vtos(c4[1],0))
    c5 = "$$수식$${}x{}$$/수식$$".format(vtos(c5[0],1,1),vtos(c5[1],0))

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break


    stem = stem.format(s=s,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s=s,ss=ss,sss=sss)

    return stem, answer, comment

def latterandexpress113_Stem_025():
    stem = "다음 식을 간단히 하면?\n" \
           "{s}\n" \
           "① {c1}\n" \
           "② {c2}\n" \
           "③ {c3}\n" \
           "④ {c4}\n" \
           "⑤ {c5}\n"  ## 표가 안됨
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "{s}\n={ss}\n={sss}\n\n"

    while True:
        v1 = np.random.randint(-10,10)
        v2 = np.random.randint(-10,10)
        v3 = [-1,1][np.random.randint(2)]
        v4 = np.random.randint(-10,10)
        v5 = np.random.randint(-10,10)
        v6 = np.random.randint(-10,10)
        v7 = np.random.randint(-10,10)
        vv1 = v3 * v4 * v5
        vv2 = v3 * v4 * v6
        vv3 = v3 * v7
        vvv1 = v1 + vv1
        vvv2 = v2 + vv2 + vv3
        if v1 != 0 and v2 != 0 and v3 != 0 and v4 != 0 and v5 != 0 and v6 != 0 and v7 != 0 and vvv1 != 0 and vvv2 != 0:
            break

    sv1 = vtos(v1,1,1)
    sv2 = vtos(v2,0)
    sv3 = vtos(v3,1)
    sv4 = vtos(v4,1,1)
    sv5 = vtos(v5,1,1)
    sv6 = vtos(v6,0)
    sv7 = vtos(v7,0)

    s2 = "LEFT { %s LEFT ( %s a %s RIGHT ) %s RIGHT }" % (sv4,sv5,sv6,sv7)
    s = "$$수식$$LEFT ({sv1}a{sv2}RIGHT ){sv3} {s2} $$/수식$$".format(sv1=sv1,sv2=sv2,sv3=sv3,s2=s2)
    
    svv1 = vtos(vv1,1)
    svv2 = vtos(vv2,0)
    svv3 = vtos(vv3,0)
    
    ss = "$$수식$${sv1}a{sv2}{svv1}a{svv2}{svv3}$$/수식$$".format(sv1=sv1,sv2=sv2,svv1=svv1,svv2=svv2,svv3=svv3)

    svvv1 = vtos(vvv1,1,1)
    svvv2 = vtos(vvv2,0)

    result = (vvv1,vvv2)
    sss = "$$수식$${}a{}$$/수식$$".format(svvv1,svvv2)

    candidates = []
    candidates.append((vvv1,vvv2))
    while len(candidates) < 5 :
        temp1 = np.random.randint(-50,50)
        temp2 = np.random.randint(-50,50)
        if temp1 == 0 or temp2 == 0:
            continue
        f = True
        for c in candidates:
            if c == (temp1,temp2):
                f = False
                break
        if f:
            candidates.append((temp1,temp2))
    
    c1, c2, c3, c4, c5 = candidates
    c1 = "$$수식$${}a{}$$/수식$$".format(vtos(c1[0],1,1),vtos(c1[1],0))
    c2 = "$$수식$${}a{}$$/수식$$".format(vtos(c2[0],1,1),vtos(c2[1],0))
    c3 = "$$수식$${}a{}$$/수식$$".format(vtos(c3[0],1,1),vtos(c3[1],0))
    c4 = "$$수식$${}a{}$$/수식$$".format(vtos(c4[0],1,1),vtos(c4[1],0))
    c5 = "$$수식$${}a{}$$/수식$$".format(vtos(c5[0],1,1),vtos(c5[1],0))

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break


    stem = stem.format(s=s,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s=s,ss=ss,sss=sss)

    return stem, answer, comment

def latterandexpress113_Stem_026():
    stem = "다음 식을 간단히 하였을 때, x의 계수와 상수항의 합은?\n" \
           "{s}\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"  ## 표가 안됨
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "{s}\n={ss}\n={sss}\n\n"

    while True:
        v1 = np.random.randint(-10,10)
        v2 = np.random.randint(-10,10)
        v3 = [-1,1][np.random.randint(2)]
        v4 = np.random.randint(-10,10)
        v5 = np.random.randint(-10,10)
        v6 = np.random.randint(-10,10)
        v7 = np.random.randint(-10,10)
        vv1 = v3 * v4
        vv2 = v3 * v5
        vvv1 = v2 + vv1 + v6
        vvv2 = v1 + vv2 + v7
        if v1 != 0 and v2 != 0 and v3 != 0 and v4 != 0 and v5 != 0 and v6 != 0 and v7 != 0 and vvv1 != 0 and vvv2 != 0:
            break

    sv1 = vtos(v1,0,1)
    sv2 = vtos(v2,1)
    sv3 = vtos(v3,1)
    sv4 = vtos(v4,1,1)
    sv5 = vtos(v5,0)
    sv6 = vtos(v6,1)
    sv7 = vtos(v7,0)

    s2 = "LEFT { %s %s x %s LEFT ( %s x %s RIGHT ) RIGHT }" % (sv1,sv2,sv3,sv4,sv5)
    s = "$$수식$${s2} {sv6} {sv7} $$/수식$$".format(s2=s2,sv6=sv6,sv7=sv7)
    
    svv1 = vtos(vv1,1)
    svv2 = vtos(vv2,0)
    
    ss = "$$수식$$LEFT ( {sv1} {sv2}x {svv1}x {svv2} RIGHT ) {sv6}x {sv7}$$/수식$$".format(sv1=sv1,sv2=sv2,svv1=svv1,svv2=svv2,sv6=sv6,sv7=sv7)

    svvv1 = vtos(vvv1,1,1)
    svvv2 = vtos(vvv2,0)

    result = vvv1 + vvv2

    sss = "$$수식$${}x{}$$/수식$$".format(svvv1,svvv2)


    idx = np.random.randint(0,5)
    candidates = [] 
    temp = result - 1 * idx

    for i in range(5):
        candidates.append(temp + 1 * i)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break


    stem = stem.format(s=s,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s=s,ss=ss,sss=sss)

    return stem, answer, comment

def latterandexpress113_Stem_027():
    stem = "$$수식$${a1}x-{a2} over {a3}`+`{a4}x-{a5} over {a6}`+`{a7}x-{a8} over {a9}`을``계산한``결과는?$$/수식$$\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"  ## 표가 안됨
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${a1}x-{a2} over {a3}`+`{a4}x-{a5} over {a6}`-`{a7}x-{a8} over {a9}$$/수식$$\n" \
              "= $$수식$${f} over {a9}$$/수식$$\n" \
              "= $$수식$${c1}x{c2} over {a9}$$/수식$$\n" \
              "= $$수식$${d1}x{d2}$$/수식$$\n\n"

    while True:
        a1= np.random.randint(2,10)
        a2= np.random.randint(1,10)
        a3= np.random.randint(2,10)
        a4= np.random.randint(2,10)
        a5= np.random.randint(1,10)
        a6= np.random.randint(2,10)
        a7= np.random.randint(2,10)
        a8= np.random.randint(1,10)
        a9= np.random.randint(2,10)

        b1 = a6*a1
        b2 = a6*a2
        b3 = a3*a4
        b4 = a3*a5

        c1 = b1+b3-a7
        c2 = a8-b2-b4

        d1 = math.floor(c1/a9)
        d2 = math.floor(c2/a9)


        if(a9==a3*a6 and a1!=a4!=a7 and a2!=a5!=a8):
            if(c1!=0 and c2!=0 and c2<0 and c1%a9==0 and c2%a9==0):
                break
    f = "{"
    f = f + "{%s}x-{%s}+{%s}x-{%s}-{%s}x+{%s}" % (b1,b2,b3,b4,a7,a8)
    f = f + "}"

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}x{%s}" % (d1,d2)
        q2 = "{%s}x+{%s}" % (d1,d2*(-1))
        q3 = "-{%s}x{%s}" % (d1,d2)
        q4 = "{%s}x" % (d1)
        q5 = "-{%s}x+{%s}" % (d1,d2*(-1))
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}x+{%s}" % (d1,d2*(-1))
        q2 = "{%s}x{%s}" % (d1,d2)
        q3 = "-{%s}x{%s}" % (d1,d2)
        q4 = "{%s}x" % (d1)
        q5 = "-{%s}x+{%s}" % (d1,d2*(-1))
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}x+{%s}" % (d1,d2*(-1))
        q2 = "-{%s}x{%s}" % (d1,d2)
        q3 = "{%s}x{%s}" % (d1,d2)
        q4 = "{%s}x" % (d1)
        q5 = "-{%s}x+{%s}" % (d1,d2*(-1))
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}x+{%s}" % (d1,d2*(-1))
        q2 = "-{%s}x{%s}" % (d1,d2)
        q3 = "{%s}x" % (d1)
        q4 = "{%s}x{%s}" % (d1,d2)
        q5 = "-{%s}x+{%s}" % (d1,d2*(-1))
        answer_num = "④"
    else:
        q1 = "{%s}x+{%s}" % (d1,d2*(-1))
        q2 = "-{%s}x{%s}" % (d1,d2)
        q3 = "{%s}x" % (d1)
        q4 = "-{%s}x+{%s}" % (d1,d2*(-1))
        q5 = "{%s}x{%s}" % (d1,d2)
        answer_num = "⑤"

    stem = stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,a9=a9,q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,a9=a9,f=f, c1=c1,c2=c2,d1=d1,d2=d2)

    return stem, answer, comment

def latterandexpress113_Stem_028():
    stem = "어떤 일차식을 $$수식$${s1}$$/수식$$로 빼어야 할 것을 잘못하여 더했더니 $$수식$${s2}$$/수식$$이 되었다. 이때 바르게 계산한 식은?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "어떤 일차식을 $$수식$$BOX~~$$/수식$$라 하면\n" \
              "$$수식$${ss1}$$/수식$$이므로\n" \
              "$$수식$${ss2}`=`{ss3}`=`{ss4}$$/수식$$\n" \
              "즉, 어떤 일차식은 $$수식$${ss4}$$/수식$$이다.\n" \
              "따라서 바르게 계산한 식은\n" \
              "$$수식$${sss1}`=`{sss2}`=`{sss3}$$/수식$$\n\n"

    while True:
        v0 = np.random.randint(-10, 10)
        v1 = np.random.randint(-10, 10)
        v2 = np.random.randint(-10, 10)
        v3 = np.random.randint(-10, 10)

        if v0 == 0 or v1 == 0 or v2 == 0 or v3 == 0 or v0 == v2 or v1 == v3:
            continue

        vv1 = -v0  + v2
        vv2 = -v1  + v3

        vvv1 = vv1 - v0
        vvv2 = vv2 - v1
        if vv1!= 0 and vv2 != 0 and vvv1 != 0 and vvv2 !=0:
            break

    sv0 = vtos(v0, 1, 1)
    sv1 = vtos(v1, 0)
    sv2 = vtos(v2, 1, 1)
    sv3 = vtos(v3, 0)
    sv4 = vtos(-v0, 1, 0)
    sv6 = vtos(-v1, 0)



    s1 = "{sv0}x{sv1}".format(sv0=sv0, sv1=sv1)
    s2 = "{sv2}x{sv3}".format(sv2=sv2, sv3=sv3)
    s3 = "{sv4}x{sv6}".format(sv4=sv4, sv6=sv6)

    #sv4 = vtos4(1, v1)
    sv5 = vtos2(v1)

    ss1 = "BOX~~`+`{s1}`=`{s2}".format(s1=s1, s2=s2)
    ss2 = "BOX~~`=`{s2} `-`LEFT ( {s1} RIGHT )".format(s2=s2, s1=s1)
    ss3 = "{s2} `{s3} ".format(s2=s2, s3=s3)

    svv1 = vtos(vv1, 1, 1)
    svv2 = vtos(vv2, 0)

    ss4 = "{svv1}x{svv2}".format(svv1=svv1, svv2=svv2)

    sss1 = "{ss4} `-` LEFT ( {s1} RIGHT )".format(ss4=ss4, s1=s1)
    sss2 = "{ss4} `{s3} ".format(ss4=ss4, s3=s3)

    svvv1 = vtos(vvv1, 1, 1)
    svvv2 = vtos(vvv2, 0)

    sss3 = "{svvv1}x{svvv2}".format(svvv1=svvv1, svvv2=svvv2)

    temp = "%sx %s"

    c1 = temp % (svv1, svv2)
    c2 = temp % (svv1, svvv2)
    c3 = temp % (svvv1, svv2)
    c4 = temp % (sv2, svvv2)

    candidates = [c1, c2, c3, c4, sss3]
    np.random.shuffle(candidates)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == sss3:
            correct_idx = i
            break

    stem = stem.format(s1=s1, s2=s2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, sss1=sss1, sss2=sss2, sss3=sss3)

    return stem, answer, comment


def latterandexpress113_Stem_029():
    stem = "$$수식$$-`{a2} over {a1}`(x-{a3})`-`{a9}({a6}x`+`{a8} over {a7}`)를``간단히``하면$$/수식$$\n" \
           "ax+b일 때, 상수 a, b에 대하여 a + b의 값은?\n"\
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$$-`{a2} over {a1}`(x-{a3})`-`{a9}({a6}x`+`{a8} over {a7}`)$$/수식$$\n" \
              "= $$수식$$-`{a2} over {a1}`(x-{a3})`-`{a5} over {a4}`({a6}x`+`{a8} over {a7}`)$$/수식$$\n" \
              "= $$수식$$-`{a2} over {a1}`x`+`{b1}`-`{b2} over {a4}`x-{b3}$$/수식$$\n" \
              "= $$수식$$-`{c1}x+{c2}$$/수식$$\n" \
              "따라서 a = $$수식$$-{c1}$$/수식$$,  b = $$수식$${c2}$$/수식$$ 이므로\n" \
              "a + b = $$수식$${result}$$/수식$$\n"

    while True:
        a1 = [2,5,10][np.random.randint(0,3)]
        a2 = np.random.randint(1,10)
        a3 = a1 or a1*2 or a1*3
        a4 = a1
        a6 = np.random.randint(2,10)
        a7 = np.random.randint(2,10)
        a5 = a7 or a7 * 1 or a7 * 2
        a8 = a4 or a4*2 or a4*3
        a9 = a5/a4

        b1 = math.floor(a2*a3/a1)
        b2 = a5*a6
        b3 = math.floor((a5*a8)/(a4*a7))

        c1 = math.floor((a2+b2)/a1)
        c2 = b1-b3

        result = c2-c1

        if (a2+b2)%a1 == 0 and a5*10%a4 == 0 and fractions.gcd(a2,a1)==1 and fractions.gcd(a8,a7)==1:
            if(result<0):
                break

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result + 1)
        q3 = "{%s}" % (result + 2)
        q4 = "-`{%s} over {%s}" % (abs(result) *a4-1, a4)
        q5 = "-`{%s} over {%s}" % (abs(result) *a4+1,a4)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result - 1)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result + 1)
        q4 = "-`{%s} over {%s}" % (abs(result) * a4 - 1, a4)
        q5 = "-`{%s} over {%s}" % (abs(result) * a4 + 1, a4)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result - 2)
        q2 = "{%s}" % (result - 1)
        q3 = "{%s}" % (result)
        q4 = "-`{%s} over {%s}" % (abs(result) * a4 - 1, a4)
        q5 = "-`{%s} over {%s}" % (abs(result) * a4 + 1, a4)
        answer_num = "③"
    elif (sol == 3):
        q1 = "-`{%s} over {%s}" % (abs(result) * a4 - 1, a4)
        q2 = "-`{%s} over {%s}" % (abs(result) * a4 + 1, a4)
        q3 = "{%s}" % (result - 1)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result + 1)
        answer_num = "④"
    else:
        q1 = "-`{%s} over {%s}" % (abs(result) * a4 - 1, a4)
        q2 = "-`{%s} over {%s}" % (abs(result) * a4 + 1, a4)
        q3 = "{%s}" % (result - 2)
        q4 = "{%s}" % (result - 1)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1,a2=a2,a3=a3,a6=a6,a7=a7,a8=a8,a9=a9,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,a9=a9,b1=b1,b2=b2,b3=b3,c1=c1,c2=c2, result=result)

    return stem, answer, comment


def latterandexpress113_Stem_030():
    stem = "두 식 $$수식$$ A`$$/수식$$, $$수식$$ B`$$/수식$$ 에 대하여 $$수식$${s1}$$/수식$$ ,\n" \
           "$$수식$${s2}$$/수식$$ 라 할 때,\n" \
           "$$수식$${sw1}$$/수식$$\n" \
           "를 계산하면 $$수식$$ a`x`+b`y` $$/수식$$이다. 상수 $$수식$$a`$$/수식$$,$$수식$$b`$$/수식$$ 에 대하여\n" \
           "$$수식$$a`+`b`$$/수식$$ 의 값은?\n" \
           "\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${sw1}$$/수식$$\n" \
              "$$수식$$={sw2}$$/수식$$\n" \
              "$$수식$$={sw3}$$/수식$$\n" \
              "$$수식$$={sw4}$$/수식$$\n" \
              "$$수식$$={sw5}$$/수식$$\n" \
              "따라서 $$수식$$a`=`{a},`b`=`{b}$$/수식$$ 이므로 \n" \
              "$$수식$$a`+`b`=`{result}$$/수식$$\n\n"

    while True:
        v1 = np.random.randint(-5, 5)
        v2 = np.random.randint(-5, 5)
        v3 = np.random.randint(-5, 5)
        v4 = np.random.randint(-5, 5)
        z1 = np.random.randint(-5, 5)
        z2 = np.random.randint(-5, 5)
        z3 = np.random.randint(-5, 5)
        z4 = np.random.randint(-5, 5)
        z5 = np.random.randint(-5, 5)
        z6 = np.random.randint(-5, 5)
        z7 = np.random.randint(-5, 5)
        z8 = np.random.randint(-5, 5)

        if v1 != 0 and v2 != 0 and v3 != 0 and v4 != 0 and z1 != 0 and z2 != 0 and z3 != 0 and z4 != 0 and z5 != 0 and z6 != 0 and z7 != 0 and z8 != 0:
            szv1 = v1 * z1
            szv2 = v1 * z2
            szv3 = v2 * z3
            szv4 = v2 * z4
            szv5 = v3 * z5
            szv6 = v3 * z6
            szv7 = v4 * z7
            szv8 = v4 * z8

            zzv1 = szv1 + szv3
            zzv2 = szv2 + szv4
            zzv3 = szv5 + szv7
            zzv4 = szv6 + szv8

            a = zzv1 - zzv3
            b = zzv2 - zzv4

            if zzv1 !=0 and zzv2 !=0 and zzv3 !=0 and zzv4 !=0 and a!=0 and b!=0:
                break

    sv1 = vtos(v1, 1, 1)
    sv2 = vtos(v2, 1, 0)
    sv3 = vtos(v3, 1, 1)
    sv4 = vtos(v4, 1, 0)

    s1 = "A`◉`B`=`{sv1}A`{sv2}B`".format(sv1=sv1, sv2=sv2)
    s2 = "A`◆`B`=`{sv3}A`{sv4}B`".format(sv3=sv3, sv4=sv4)

    sz1 = vtos(z1, 1, 1)
    sz2 = vtos(z2, 1, 0)
    sz3 = vtos(z3, 1, 1)
    sz4 = vtos(z4, 1, 0)
    sz5 = vtos(z5, 1, 1)
    sz6 = vtos(z6, 1, 0)
    sz7 = vtos(z7, 1, 1)
    sz8 = vtos(z8, 1, 0)

    nszv1 = vtos(szv1, 1, 1)
    nszv2 = vtos(szv2, 1, 0)
    nszv3 = vtos(szv3, 1, 0)
    nszv4 = vtos(szv4, 1, 0)
    nszv5 = vtos(szv5, 1, 1)
    nszv6 = vtos(szv6, 1, 0)
    nszv7 = vtos(szv7, 1, 0)
    nszv8 = vtos(szv8, 1, 0)


    nzzv1 = vtos(zzv1, 1, 1)
    nzzv2 = vtos(zzv2, 1, 0)
    nzzv3 = vtos(zzv3, 1, 1)
    nzzv4 = vtos(zzv4, 1, 0)

    na = vtos(a, 1, 1)
    nb = vtos(b, 1, 0)

    w1 = "{sz1}x`{sz2}y".format(sz1=sz1, sz2=sz2)
    w2 = "{sz3}x`{sz4}y".format(sz3=sz3, sz4=sz4)
    w3 = "{sz5}x`{sz6}y".format(sz5=sz5, sz6=sz6)
    w4 = "{sz7}x`{sz8}y".format(sz7=sz7, sz8=sz8)


    left = "{"
    right = "}"


    sw1 = "LEFT {left} LEFT ( {w1} RIGHT ) ◉ LEFT ( {w2} RIGHT ) RIGHT {right} - LEFT {left} LEFT ( {w3} RIGHT ) ◆ LEFT ( {w4} RIGHT ) RIGHT {right} ".format(left=left, right=right, w1=w1, w2=w2, w3=w3, w4=w4)
    sw2 = "{sv1} LEFT ( {w1} RIGHT ) ` {sv2} LEFT ( {w2} RIGHT )`-` LEFT {left}{sv3} LEFT ( {w3} RIGHT ) ` {sv4} LEFT ( {w4} RIGHT ) RIGHT {right} ".format(left=left,right=right,sv1=sv1,sv2=sv2, sv3=sv3, sv4=sv4, w1=w1,w2=w2,w3=w3,w4=w4)
    sw3 = "{nszv1}x `{nszv2}y ` {nszv3}x ` {nszv4}y `-` LEFT ( {nszv5}x ` {nszv6}y ` {nszv7}x ` {nszv8}y RIGHT )".format(nszv1=nszv1, nszv2=nszv2,nszv3=nszv3,nszv4=nszv4, nszv5=nszv5, nszv6=nszv6,nszv7=nszv7,nszv8=nszv8)
    sw4 = "{nzzv1}x ` {nzzv2}y `-` LEFT ({nzzv3}x ` {nzzv4}y RIGHT )".format(nzzv1=nzzv1,nzzv2=nzzv2,nzzv3=nzzv3,nzzv4=nzzv4)
    sw5 = "{na}x `{nb}y".format(na=na, nb=nb)


    result = a + b

    idx = np.random.randint(0,5)
    candidates = []
    temp = result - 1 * idx

    for i in range(5):
        candidates.append(temp + 1 * i)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break


    stem = stem.format(s1=s1, s2=s2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, sw1=sw1)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(sw1=sw1, sw2=sw2, sw3=sw3, sw4=sw4, sw5=sw5, a=a, b=b, result=result)

    return stem, answer, comment

def latterandexpress113_Stem_031():
    stem = "x가 $$수식$${a}$$/수식$$의 약수일 때, 방정식 $$수식$$1 over {a1}`(x+{a2})`=`{a3}-x의 해는?$$/수식$$\n" \
           "① $$수식$$1$$/수식$$\n" \
           "② $$수식$${aa1}$$/수식$$\n" \
           "③ $$수식$${aa2}$$/수식$$\n" \
           "④ $$수식$${a}$$/수식$$\n" \
           "⑤ $$수식$$1,{aa1}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "x가 $$수식$${a}$$/수식$$의 약수이므로\n" \
              "x = $$수식$$1,``{aa1},``{aa2},``{a}$$/수식$$\n" \
              "$$수식$$1 over {a1}`(x+{a2})`=`{a3}-x`에$$/수식$$\n" \
              "x = 1을 대입하면 $$수식$$1 over {a1}`(1+{a2})`{k1}`{a3}-1`$$/수식$$\n" \
              "x = $$수식$${aa1}$$/수식$$을 대입하면 $$수식$$1 over {a1}`({aa1}+{a2})`{k2}`{a3}-{aa1}`$$/수식$$\n" \
              "x = $$수식$${aa2}$$/수식$$을 대입하면 $$수식$$1 over {a1}`({aa2}+{a2})`{k3}`{a3}-{aa2}`$$/수식$$\n" \
              "x = $$수식$${a}$$/수식$$을 대입하면 $$수식$$1 over {a1}`({a}+{a2})`{k4}`{a3}-{a}`$$/수식$$\n" \
              "따라서 주어진 방정식의 해는 x = $$수식$${result}이다.$$/수식$$\n\n"


    while(1):
        a = [6,8,10,14,15][np.random.randint(0,5)]

        a1 = np.random.randint(2,10)
        a2 = np.random.randint(1,10)
        a3 = np.random.randint(1,10)

        if(a == 6): aa1 = 2; aa2 = 3
        elif(a == 8): aa1 = 2; aa2 = 4
        elif(a == 10): aa1 = 2; aa2 = 5
        elif(a==14): aa1 = 2; aa2 = 7
        else: aa1 = 3; aa2 = 5

        f = fractions.Fraction(1,a1)

        if(f*(1+a2)==a3-1 or f*(aa1+a2)==a3-aa1 or f*(aa2+a2)==a3-aa2 or f*(a+a2)==a3-a ):
            break

    k1 = "≠"; k2 = "≠"; k3 = "≠"; k4 ="≠"

    if (f*(1+a2)==a3-1):
        k1 = "="
        result = 1
        answer_num = "①"
    elif (f*(aa1+a2)==a3-aa1):
        k2 = "="
        result = aa1
        answer_num = "②"
    elif (f*(aa2+a2)==a3-aa2):
        k3 = "="
        result = aa2
        answer_num = "③"
    elif(f*(a+a2)==a3-a):
        k4 = "="
        result = a
        answer_num = "④"


    stem = stem.format(a1=a1,a2=a2, a3=a3, aa1=aa1, aa2=aa2, a=a)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,a2=a2, a3=a3, aa1=aa1, aa2=aa2, a=a, k1=k1, k2=k2, k3=k3, k4=k4, result=result)

    return stem, answer, comment

def latterandexpress113_Stem_032():
    stem = "다음 중 등식인 것의 개수는?\n" \
           "$$표$$(1) $$수식$${t1}$$/수식$$               (2) $$수식$${t2}$$/수식$$\n" \
           "(3) $$수식$${t3}$$/수식$$               (4) $$수식$${t4}$$/수식$$\n" \
           "(5) $$수식$${t5}$$/수식$$               (6) $$수식$${t6}$$/수식$$\n" \
           "(7) $$수식$${t7}$$/수식$$               (8) $$수식$${t8}$$/수식$$\n$$/표$$\n" \
           "① $$수식$$2$$/수식$$\n" \
           "② $$수식$$3$$/수식$$\n" \
           "③ $$수식$$4$$/수식$$\n" \
           "④ $$수식$$5$$/수식$$\n" \
           "⑤ $$수식$$6$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${s1}``다항식이다.$$/수식$$\n" \
              "$$수식$${s2}``부등호가``있으므로``등식이``아니다.$$/수식$$\n" \
              "이상에서 등식인 것은 $$수식$${s3}의``{result}개이다.$$/수식$$\n\n"


    while(1):
        a1 = np.random.randint(2,10)
        a2 = np.random.randint(2,10)
        a3 = np.random.randint(2,10)
        a4 = np.random.randint(2,10)
        a5 = np.random.randint(2,10)

        if(a1!=a2!=a3!=a4!=a5):
            break

    sol = np.random.randint(0, 5)

    if (sol == 0):
        t1 = "{%s}(x-{%s})" % (a1,a2)
        t2 = "{%s}-(-{%s})" % (a4,a1)
        t3 = "x+y-{%s}`=`{%s}x+{%s}" % (a3-1, a2+2, a5)
        t4 = "{%s}+y`=`{%s}" % (a1+2, a3)
        t5 = "{%s}-{%s}`=`0" % (a4+1,a4+1)
        t6 = "{%s}x-{%s}&lt;{%s}" % (a3, a4-1, a2)
        t7 = "{%s}y+{%s}" % (a2, a5-1)
        t8 = "{%s}x-{%s}&gt;{%s}" % (a5+2, a3, a2-1)
        answer_num = "②"
        result = 3
    elif (sol == 1):
        t1 = "{%s}(x-{%s})" % (a1, a2)
        t2 = "{%s}-(-{%s})" % (a4, a1)
        t3 = "x+y-{%s}`=`{%s}x+{%s}" % (a3 - 1, a2 + 2, a5)
        t4 = "{%s}+y`=`{%s}" % (a1 + 2, a3)
        t5 = "{%s}-{%s}`=`0" % (a4 + 1, a4 + 1)
        t6 = "{%s}x-{%s}`=`{%s}" % (a3, a4 - 1, a2)
        t7 = "{%s}y+{%s}" % (a2, a5 - 1)
        t8 = "{%s}x-{%s}&gt;{%s}" % (a5 + 2, a3, a2-1)

        answer_num = "③"
        result = 4
    elif (sol == 2):
        t1 = "{%s}(x-{%s})" % (a1, a2)
        t2 = "{%s}-(-{%s})" % (a4, a1)
        t3 = "x+y-{%s}`=`{%s}x+{%s}" % (a3 - 1, a2 + 2, a5)
        t4 = "{%s}+y`=`{%s}" % (a1 + 2, a3)
        t5 = "{%s}-{%s}`=`0" % (a4 + 1, a4 + 1)
        t6 = "{%s}x-{%s}`=`{%s}" % (a3, a4 - 1, a2)
        t7 = "{%s}y+{%s}`=`{%s}" % (a2, a5 - 1,a1-1)
        t8 = "{%s}x-{%s}&gt;{%s}" % (a5 + 2, a3, a2-1)

        answer_num = "④"
        result = 5
    elif (sol == 3):
        t1 = "{%s}(x-{%s})`=`{%s}" % (a1, a2,a5)
        t2 = "{%s}-(-{%s})" % (a4, a1)
        t3 = "x+y-{%s}`=`{%s}x+{%s}" % (a3 - 1, a2 + 2, a5)
        t4 = "{%s}+y`&lt;`{%s}" % (a1 + 2, a3)
        t5 = "{%s}-{%s}`=`0" % (a4 + 1, a4 + 1)
        t6 = "{%s}x-{%s}`=`{%s}" % (a3, a4 - 1, a2)
        t7 = "{%s}y+{%s}`=`{%s}" % (a2, a5 - 1, a1 - 1)
        t8 = "{%s}x+{%s}={%s}x" % (a5 + 2, a3, a4+1)

        answer_num = "⑤"
        result = 6
    else:
        t1 = "{%s}(x-{%s})`&lt;`{%s}" % (a1, a2,a5-1)
        t2 = "{%s}-(-{%s})" % (a4, a1)
        t3 = "x+y-{%s}`=`{%s}x+{%s}" % (a3 - 1, a2 + 2, a5)
        t4 = "{%s}+y`&gt;`{%s}" % (a1 + 2, a3)
        t5 = "{%s}-{%s}" % (a4 + 1, a4 + 1)
        t6 = "{%s}x-{%s}`=`{%s}" % (a3, a4 - 1, a2)
        t7 = "{%s}y+{%s}`&lt;`{%s}" % (a2, a5 - 1, a1 - 1)
        t8 = "{%s}x+{%s}" % (a5 + 2, a3)

        answer_num = "①"
        result = 2

    s1 = ""
    s2 = ""
    s3 = ""

    T = [t1, t2, t3, t4, t5, t6, t7, t8]
    np.random.shuffle(T)
    t1, t2, t3, t4, t5, t6, t7, t8 = T

    TT = [0, 0, 0, 0, 0, 0, 0, 0]
    cnt = 0
    for i in T:
        if ("=" in i):
            TT[cnt] = 1
        elif ("&lt;" in i or "&gt;" in i):
            TT[cnt] = 2
        cnt = cnt + 1

    c = 1
    for i in TT:
        if i == 0:
            s1 = s1 + "(" + str(c) + ")" + " "
        elif i == 1:
            s3 = s3 + "(" + str(c) + ")" + " "
        elif i == 2:
            s2 = s2 + "(" + str(c) + ")" + " "
        c = c + 1

    stem = stem.format(t1=t1,t2=t2,t3=t3,t4=t4,t5=t5,t6=t6,t7=t7,t8=t8)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(s1=s1,s2=s2,s3=s3,result=result)

    return stem, answer, comment

def latterandexpress113_Stem_033():
    stem = "다음 중 모든 x의 값에 대하여 항상 참이 되는 등식은?\n" \
           "① $$수식$${t1}$$/수식$$\n" \
           "② $$수식$${t2}$$/수식$$\n" \
           "③ $$수식$${t3}$$/수식$$\n" \
           "④ $$수식$${t4}$$/수식$$\n" \
           "⑤ $$수식$${t5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "모든 x의 값에 대하여 항상 참이 되는 등식은 항등식이다.\n" \
              "$$수식$${s1}``일차식$$/수식$$\n" \
              "$$수식$${s2}``방정식$$/수식$$\n\n"

    while(1):
        a1 = np.random.randint(2,10)
        a2 = np.random.randint(2,10)
        a3 = np.random.randint(2,10)

        if(a1!=a2!=a3):
            if a3-1!=1:
                break

    sol = np.random.randint(0, 5)

    if (sol == 0):
        t1 = "x+{%s}`=`{%s}+x" % (a1,a1)
        t2 = "{%s}x`=`{%s}" % (a3-1,a3-1)
        t3 = "{%s}x`+`{%s}`=`{%s}" % (a1*2, a2-1, a3+2)
        t4 = "{%s}`-`x`=`{%s}x" % (a1+2, a3)
        t5 = "{%s}x`+`{%s}" % (a2+2,a1-1)

        s1 = "⑤"
        s2 = "②, ③, ④"
        answer_num = "①"
    elif (sol == 1):
        t1 = "{%s}x`+`{%s}" % (a2+2,a1-1)
        t2 = "x+{%s}`=`{%s}+x" % (a1,a1)
        t3 = "{%s}x`+`{%s}`=`{%s}" % (a1*2, a2-1, a3+2)
        t4 = "{%s}x`=`{%s}" % (a3-1,a3-1)
        t5 = "{%s}`-`x`=`{%s}x" % (a1+2, a3)
        s1 = "①"
        s2 = "③, ④, ⑤"
        answer_num = "②"
    elif (sol == 2):
        t1 = "{%s}x`=`{%s}" % (a3-1,a3-1)
        t2 = "{%s}x`+`{%s}" % (a2+2,a1-1)
        t3 = "x+{%s}`=`{%s}+x" % (a1,a1)
        t4 = "{%s}`-`x`=`{%s}x" % (a1+2, a3)
        t5 = "{%s}x`+`{%s}`=`{%s}" % (a1*2, a2-1, a3+2)
        s1 = "②"
        s2 = "①, ④, ⑤"
        answer_num = "③"
    elif (sol == 3):
        t1 = "{%s}x`+`{%s}`=`{%s}" % (a1*2, a2-1, a3+2)
        t2 = "{%s}`-`x`=`{%s}x" % (a1+2, a3)
        t3 = "{%s}x`+`{%s}" % (a2+2,a1-1)
        t4 = "x+{%s}`=`{%s}+x" % (a1,a1)
        t5 = "{%s}x`=`{%s}" % (a3-1,a3-1)
        s1 = "③"
        s2 = "①, ②, ⑤"
        answer_num = "④"
    else:
        t1 = "{%s}`-`x`=`{%s}x" % (a1+2, a3)
        t2 = "{%s}x`=`{%s}" % (a3-1,a3-1)
        t3 = "{%s}x`+`{%s}`=`{%s}" % (a1*2, a2-1, a3+2)
        t4 = "{%s}x`+`{%s}" % (a2+2,a1-1)
        t5 = "x+{%s}`=`{%s}+x" % (a1,a1)
        s1 = "④"
        s2 = "①, ②, ③"
        answer_num = "⑤"


    stem = stem.format(t1=t1,t2=t2,t3=t3,t4=t4,t5=t5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(s1=s1,s2=s2)

    return stem, answer, comment

def latterandexpress113_Stem_034():
    stem = "다음 중 등식으로 나타낼 수 없는 것은?\n" \
           "① {q1}\n" \
           "② {q2}\n" \
           "③ {q3}\n" \
           "④ {q4}\n" \
           "⑤ {q5}\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "① {s1}\n" \
              "② {s2}\n" \
              "③ {s3}\n" \
              "④ {s4}\n" \
              "⑤ {s5}\n" \
              "따라서 등식으로 나타낼 수 없는 것은 $$수식$${K}$$/수식$$이다.\n\n"


    a1 = np.random.randint(2,10)
    b1 = np.random.randint(1,10)
    b2 = np.random.randint(2,10)
    c1 = np.random.randint(1,10)*10
    c2 = np.random.randint(1,10)*1000
    c3 = c1/100
    d1 = np.random.randint(1,10)*100
    d2 = np.random.randint(1,10)*1000
    d3 = np.random.randint(1,10)*100
    e1 = np.random.randint(1,10)*10

    q1 = "$$수식$$x의``{%s}배는``y와``같다.$$/수식$$"%(a1)
    q2 = "$$수식$$x에서``{%s}를``뺀``후``{%s}배``한다.$$/수식$$" % (b1,b2)
    q3 = "$$수식$$정가가``x원인``제품을``{%s}$$/수식$$" % (c1)
    q3 = q3 + "     %"
    q3 = q3 + "$$수식$$``할인하여``팔``때의``가격은``{%s}원이다.$$/수식$$" % (c2)
    q4 = "$$수식$${%s}원짜리``볼펜을``x자루``사고``{%s}원을``냈더니``거스름돈이``{%s}원이었다.$$/수식$$" % (d1,d2,d3)
    q5 = "$$수식$$가로의``길이가``x rm cm,세로의``길이가``y rm cm인``직사각형의``넓이는``{%s}``rm cm^2``이다.$$/수식$$" % (e1)

    aa = q1
    bb = q2
    cc = q3
    dd = q4
    ee = q5

    NN = [q1, q2, q3, q4, q5]
    np.random.shuffle(NN)
    q1, q2, q3, q4, q5 = NN

    for i in NN:
        if (i == bb and i == q1):
            K = "①"
            break
        if (i == bb and i == q2):
            K = "②"
            break
        if (i == bb and i == q3):
            K = "③"
            break
        if (i == bb and i == q4):
            K = "④"
            break
        if (i == bb and i == q5):
            K = "⑤"
            break

    if (q1 == aa):
        s1 = "$$수식$${%s}x`=`y$$/수식$$" % (a1)
    elif (q1 == bb):
        s1 = "$$수식$${%s}(x-{%s})$$/수식$$" % (b1, b2)
    elif (q1 == cc):
        s1 = "$$수식$${%s}x`=`{%s}$$/수식$$" % (c3,c2)
    elif (q1 == dd):
        s1 = "$$수식$${%s}-{%s}x`=`{%s}$$/수식$$" % (d2,d1,d3)
    else:
        s1 = "$$수식$$xy`=`{%s}$$/수식$$" % (e1)

    if (q2 == aa):
        s2 = "$$수식$${%s}x`=`y$$/수식$$" % (a1)
    elif (q2 == bb):
        s2 = "$$수식$${%s}(x-{%s})$$/수식$$" % (b1, b2)
    elif (q2 == cc):
        s2 = "$$수식$${%s}x`=`{%s}$$/수식$$" % (c3,c2)
    elif (q2 == dd):
        s2 = "$$수식$${%s}-{%s}x`=`{%s}$$/수식$$" % (d2,d1,d3)
    else:
        s2 = "$$수식$$xy`=`{%s}$$/수식$$" % (e1)

    if (q3 == aa):
        s3 = "$$수식$${%s}x`=`y$$/수식$$" % (a1)
    elif (q3 == bb):
        s3 = "$$수식$${%s}(x-{%s})$$/수식$$" % (b1, b2)
    elif (q3 == cc):
        s3 = "$$수식$${%s}x`=`{%s}$$/수식$$" % (c3,c2)
    elif (q3 == dd):
        s3 = "$$수식$${%s}-{%s}x`=`{%s}$$/수식$$" % (d2,d1,d3)
    else:
        s3 = "$$수식$$xy`=`{%s}$$/수식$$" % (e1)

    if (q4 == aa):
        s4 = "$$수식$${%s}x`=`y$$/수식$$" % (a1)
    elif (q4 == bb):
        s4 = "$$수식$${%s}(x-{%s})$$/수식$$" % (b1, b2)
    elif (q4 == cc):
        s4 = "$$수식$${%s}x`=`{%s}$$/수식$$" % (c3,c2)
    elif (q4 == dd):
        s4 = "$$수식$${%s}-{%s}x`=`{%s}$$/수식$$" % (d2,d1,d3)
    else:
        s4 = "$$수식$$xy`=`{%s}$$/수식$$" % (e1)

    if (q5 == aa):
        s5 = "$$수식$${%s}x`=`y$$/수식$$" % (a1)
    elif (q5 == bb):
        s5 = "$$수식$${%s}(x-{%s})$$/수식$$" % (b1, b2)
    elif (q5 == cc):
        s5 = "$$수식$${%s}x`=`{%s}$$/수식$$" % (c3,c2)
    elif (q5 == dd):
        s5 = "$$수식$${%s}-{%s}x`=`{%s}$$/수식$$" % (d2,d1,d3)
    else:
        s5 = "$$수식$$xy`=`{%s}$$/수식$$" % (e1)


    stem = stem.format(q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
    answer = answer.format(K=K)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5,K=K)

    return stem, answer, comment

def latterandexpress113_Stem_035():
    stem = "등식 $$수식$${s1}`=`{s2}$$/수식$$가 모든 $$수식$$x$$/수식$$의 값에 대하여 항상 참이 될 때, 일차식 $$수식$$A$$/수식$$는?\n" \
           "\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"  ## 표가 안됨
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${s1}`=`{ss}`=`{sss}$$/수식$$\n" \
              "따라서 주어진 식은 \n" \
              "$$수식$${sss}`=`{s2}$$/수식$$\n" \
              "$$수식$$THEREFORE~A`=`{ssss}$$/수식$$\n\n"

    while True:
        v1 = np.random.randint(-10,10)
        v2 = np.random.randint(-10,10)
        v3 = np.random.randint(-10,10)
        v4 = np.random.randint(-10,10)
        v5 = np.random.randint(-10,10)
        v6 = np.random.randint(-10,10)
        vv1 = v1 * v2
        vv2 = v1 * v3
        vvv1 = vv1 + v4
        vvv2 = vv2 + v5
        vvvv1 = vvv1 - v6
        if v1 != 0 and v2 != 0 and v3 != 0 and v4 != 0 and v5 != 0 and v6 != 0 and vvv1 != 0 and vvv2 != 0 and vvvv1 != 0:
            break

    sv1 = vtos(v1,1,1)
    sv2 = vtos(v2,1,1)
    sv3 = vtos(v3,0)
    sv4 = vtos(v4,1)
    sv5 = vtos(v5,0)
    sv6 = vtos(v6,1,1)

    s1 = "{sv1} LEFT ( {sv2}x{sv3} RIGHT ) {sv4}x{sv5}".format(sv1=sv1,sv2=sv2,sv3=sv3,sv4=sv4,sv5=sv5)
    s2 = "{sv6}x + A".format(sv6=sv6)
    svv1 = vtos(vv1,1,1)
    svv2 = vtos(vv2,0)
    
    ss = " {svv1}x{svv2}{sv4}x{sv5}".format(svv1=svv1,svv2=svv2,sv4=sv4,sv5=sv5)

    svvv1 = vtos(vvv1,1,1)
    svvv2 = vtos(vvv2,0)


    sss = "{}x{}".format(svvv1,svvv2)

    svvvv1 = vtos(vvvv1,1,1)

    ssss = "{}x{}".format(svvvv1,svvv2)

    result = (vvvv1,vvv2)

    candidates = []
    candidates.append((vvvv1,vvv2))
    while len(candidates) < 5 :
        temp1 = np.random.randint(-30,30)
        temp2 = np.random.randint(-30,30)
        if temp1 == 0 or temp2 == 0:
            continue
        f = True
        for c in candidates:
            if c == (temp1,temp2):
                f = False
                break
        if f:
            candidates.append((temp1,temp2))
    
    c1, c2, c3, c4, c5 = candidates
    c1 = "{}a{}".format(vtos(c1[0],1,1),vtos(c1[1],0))
    c2 = "{}a{}".format(vtos(c2[0],1,1),vtos(c2[1],0))
    c3 = "{}a{}".format(vtos(c3[0],1,1),vtos(c3[1],0))
    c4 = "{}a{}".format(vtos(c4[0],1,1),vtos(c4[1],0))
    c5 = "{}a{}".format(vtos(c5[0],1,1),vtos(c5[1],0))

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break


    stem = stem.format(s1=s1,s2=s2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,ss=ss,sss=sss,ssss=ssss)

    return stem, answer, comment

def latterandexpress113_Stem_036():
    stem = "등식 $$수식$${s1}`=`{s2}$$/수식$$가 $$수식$$x$$/수식$$에 대한 항등식일 때," \
           "상수 $$수식$$ a , b$$/수식$$에 대하여 $$수식$$a^2`+`b^2$$/수식$$\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"  ## 표가 안됨
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${s2}`=`{ss1}$$/수식$$\n" \
              "`=`{ss2}$$/수식$$\n" \
              "이므로\n" \
              "$$수식$${s1}`=`{ss2}$$/수식$$\n" \
              "따라서 $$수식$$ {sab}`=`{v1}`,`{sa}`=`{v2} $$/수식$$이므로\n" \
              "$$수식$$ a`=`{a}`,`b`=`{b} $$/수식$$이므로\n" \
              "$$수식$$THEREFORE~a^2`+`b^2`=`{a2}`+`{b2}`=`{result}$$/수식$$\n\n"

    while True:
        v1 = np.random.randint(-10,10)
        v2 = np.random.randint(-10,10)
        v3 = [-1,1][np.random.randint(2)] # a
        v4 = np.random.randint(-10,10)
        v5 = np.random.randint(-10,10)
        v6 = [-1,1][np.random.randint(2)] # b
        if v1 == 0 or v2 == 0 or v4 == 0 or v5 == 0:
            continue
        vv1 = v3 * v4
        vv2 = v3 * v5
        a = v2 // vv2
        a_mod = v2 % vv2
        b = (v1 - vv1 * a) // v6
        b_mod = (v1 - vv1 * a) % v6

        if a_mod == 0 and b_mod == 0 and b <= 20:
            break

    sv1 = vtos(v1,1,1)
    sv2 = vtos(v2,0)
    sv3 = vtos(v3,1,1)
    sv4 = vtos(v4,1,1)
    sv5 = vtos(v5,0)
    sv6 = vtos(v6,1)

    s1 = "{sv1}x {sv2}".format(sv1=sv1,sv2=sv2)
    s2 = "{sv3} a LEFT ( {sv4}x {sv5} RIGHT ) {sv6}bx".format(sv3=sv3,sv4=sv4,sv5=sv5,sv6=sv6)

    svv1 = vtos(vv1,1,1)
    svv2 = vtos(vv2,1)
    
    ss1 = "{svv1}ax {svv2}a {sv6}bx".format(svv1=svv1,svv2=svv2,sv6=sv6)
    ss2 = "LEFT ( {svv1}ax {sv6}bx RIGHT ) {svv2}a".format(svv1=svv1,svv2=svv2,sv6=sv6)
    sab = "{svv1}a {sv6}b".format(svv1=svv1,sv6=sv6)
    sa = "{svv2}a ".format(svv2=vtos(vv2,1,1))

    a2 = a ** 2
    b2 = b ** 2
    result = a2 + b2
    print(result)
    idx = np.random.randint(0,5)
    candidates = [] 
    temp = result - 4 * idx

    for i in range(5):
        candidates.append(temp + 4 * i)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(s1=s1,s2=s2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,ss1=ss1,ss2=ss2,sab=sab,v1=v1,sa=sa,v2=v2,a=a,b=b,a2=a2,b2=b2,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_037():
    stem = "다음 중 등식의 성질에 대한 설명으로 옳지 않은 것은?\n" \
           "① {q1}\n" \
           "② {q2}\n" \
           "③ {q3}\n" \
           "④ {q4}\n" \
           "⑤ {q5}\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "{K} a = $$수식$${e1}$$/수식$$b의 양변에 1을 더하면\n" \
              "a + 1 = $$수식$${e1}$$/수식$$b + 1\n\n"
    while(1):
        a1 = np.random.randint(2,10)
        b1 = np.random.randint(1,10)
        c1 = np.random.randint(2,10)
        d1 = np.random.randint(1,10)
        e1 = np.random.randint(2,10)
        if(a1!=b1!=c1!=d1!=e1):
            break

    aa = "$$수식$$a over {%s}$$/수식$$" % (a1)

    q1 = "%s=b 이면 a = $$수식$${%s}$$/수식$$b 이다.\n" % (aa,a1)
    q2 = "a - $$수식$${%s}$$/수식$$ = b - $$수식$${%s}$$/수식$$이면 a = b이다.\n" % (b1,b1)
    q3 = "a = $$수식$${%s}$$/수식$$b 이면 -a = -$$수식$${%s}$$/수식$$b 이다.\n" % (c1,c1)
    q4 = "$$수식$${%s}$$/수식$$ - a = $$수식$${%s}$$/수식$$ - b이면 a = b이다.\n" % (d1,d1)
    q5 = "a = $$수식$${%s}$$/수식$$b이면 a + 1 = $$수식$${%s}$$/수식$$(b+1)이다.\n" % (e1,e1)

    result = q5

    candidates = [q1, q2, q3, q4, q5]
    np.random.shuffle(candidates)
    q1, q2, q3, q4, q5 = candidates

    correct_idx = 0
    for i, t in enumerate(candidates):
        if t == result:
            correct_idx = i
            break

    stem = stem.format(q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
    answer = answer.format(K=answer_dict[correct_idx])
    comment = comment.format(K=answer_dict[correct_idx], e1=e1)

    return stem, answer, comment


def latterandexpress113_Stem_038():
    stem = "다음은 등식의 성질을 이용하여 방정식을 푸는 과정이다. 이때 (가), (나)에 이용된 등식의 성질을 " \
           "보기에서 찾아 차례대로 나열한 것은?\n" \
           "$$표$$ $$수식$${a1}x``-``{a2}``=``{a3}$$/수식$$   →   $$수식$${a1}x``=``{a4}$$/수식$$   →  $$수식$$x``=``{a5}$$/수식$$ \n" \
           "            (가)           (나)$$/표$$\n" \
           "보기\n$$표$$ a = b이고 c가 자연수일 때\n" \
           "(ㄱ) a + c = b + c    (ㄴ) a - c = b - c\n" \
           "(ㄷ) ac = bc          (ㄹ) $$수식$$a over c``=``b over c $$/수식$$ $$/표$$\n" \
           "① (ㄱ),(ㄷ)\n" \
           "② (ㄱ),(ㄹ)\n" \
           "③ (ㄴ),(ㄷ)\n" \
           "④ (ㄴ),(ㄹ)\n" \
           "⑤ (ㄷ),(ㄹ)\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "(가) 양변에 $$수식$${a2}$$/수식$$를 더한다. ⇒ (ㄱ)\n" \
              "(나) 양변을 $$수식$${a1}$$/수식$$로 나눈다. ⇒ (ㄹ)\n\n"

    while(1):
        a5 = np.random.randint(1,10)
        a1 = np.random.randint(1,10)
        a4 = a5*a1
        a2 = np.random.randint(1,10)
        a3 = a4-a2
        if(a3 > 0):
            break

    K = "②"

    stem = stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
    answer = answer.format(K=K)
    comment = comment.format(a1=a1,a2=a2)

    return stem, answer, comment


def latterandexpress113_Stem_039():
    stem = "다음 조건을 모두 만족시키는 상수 a,b에 대하여 ab의 값은?\n" \
           "$$표$$(가) $$수식$${a1}$$/수식$$x = 1이면 - $$수식$$x over {a1}$$/수식$$ = a이다.\n" \
           "(나) x - $$수식$${a2}````=````{a3}$$/수식$$이면 x + $$수식$${a2}$$/수식$$ = b이다.$$/표$$\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "(가)에서 $$수식$${a1}$$/수식$$x = 1의 양변을 -$$수식$${b1}$$/수식$$으로 나누면\n" \
              "-$$수식$$x over {a1}``=``-`1 over {b1}`이므로````a``=``-`1 over {b1}$$/수식$$\n" \
              "(나)에서 x - $$수식$${a2}````=````{a3}$$/수식$$의 양변에 $$수식$${b2}$$/수식$$를 더하면\n" \
              " x + $$수식$${a2}이므로````b``=``{b3}$$/수식$$\n" \
              "∴ ab = $$수식$$(``-`1 over {b1}``)`TIMES`{b3}`=`{result}$$/수식$$\n\n"

    while(1):
        a1 = [2,4,8][np.random.randint(0,3)]
        a2 = np.random.randint(1,10)
        a3 = np.random.randint(1,10)
        b1 = a1*a1
        b2 = 2*a2
        b3 = a3 + b2
        if(a2%2==0 and b3%2==0):
            break

    f = fractions.Fraction(1, b1)
    D = f.numerator
    E = f.denominator


    c1 = -1
    c2 = "-{%s} over {%s}" % (D*b3,E)
    c3 = "{%s} over {%s}" % (2*D*b3,E)
    c4 = "{%s} over {%s}" % (D*b3,E)
    c5 = "-{%s} over {%s}" % (D*(2)*b3,E)

    result = c2

    candidates = [c1,c2,c3,c4,c5]
    np.random.shuffle(candidates)
    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, a1=a1, a2=a2, a3=a3)
    answer = answer.format(K=answer_dict[correct_idx])
    comment = comment.format(result=result,a1=a1,a2=a2,a3=a3, b1=b1,b2=b2,b3=b3,c2=c2)

    return stem, answer, comment


def latterandexpress113_Stem_040():
    stem = "$$수식$${a1}a+{a2}={a3}$$/수식$$    일 때, 다음 중 옳지 않은 것은?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{K}\n"
    comment = "(해설)\n" \
              "① $$수식$${s1}$$/수식$$\n" \
              "② $$수식$${s2}$$/수식$$\n" \
              "③ $$수식$${s3}$$/수식$$\n" \
              "④ $$수식$${s4}$$/수식$$\n" \
              "⑤ $$수식$${s5}$$/수식$$\n" \
              "따라서 옳지 않은 것은 $$수식$${K}$$/수식$$ 이다.\n\n"

    while(1):
        a1 = np.random.randint(2,10)
        a2 = np.random.randint(1,10)
        a3 = np.random.randint(1,10)
        if((a3-a2)%a1==0):
            if(a3>a2):
                break

    c1 = "$$수식$${%s}a={%s}$$/수식$$" % (a1, a3+a2)
    c2 = "$$수식$${%s}a{%s}=0$$/수식$$" % (a1, a2-a3)
    c3 = "$$수식$${%s}a+{%s}={%s}$$/수식$$" % (a1*2, a2*2, a3*2)
    c4 = "$$수식$$-a-`{%s} over {%s}`=-`{%s} over {%s}$$/수식$$" % (a2,a1,a3,a1)
    c5 = "$$수식$$-{%s}a-{%s}=-{%s}$$/수식$$" % (a1,a2,a3)

    aa = c1
    bb = c2
    cc = c3
    dd = c4
    ee = c5

    NN = [c1, c2, c3, c4, c5]
    np.random.shuffle(NN)
    c1, c2, c3, c4, c5 = NN

    correct_idx = 0
    for i, c in enumerate(NN):
        if c == aa:
            correct_idx = i
            break

    if(c1 == aa):
        s1 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에서 $$수식$${%s}$$/수식$$를 빼면 $$수식$${%s}a`=`{%s}$$/수식$$" % (a1,a2,a3,a2,a1,a3-a2)
    elif(c2 == aa):
        s2 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에서 $$수식$${%s}$$/수식$$를 빼면 $$수식$${%s}a`=`{%s}$$/수식$$" % (
        a1, a2, a3, a2, a1, a3 - a2)
    elif(c3 == aa):
        s3 = s1 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에서 $$수식$${%s}$$/수식$$를 빼면 $$수식$${%s}a`=`{%s}$$/수식$$" % (a1,a2,a3,a2,a1,a3-a2)
    elif(c4 == aa):
        s4 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에서 $$수식$${%s}$$/수식$$를 빼면 $$수식$${%s}a`=`{%s}$$/수식$$" % (
        a1, a2, a3, a2, a1, a3 - a2)
    else:
        s5 = s1 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에서 $$수식$${%s}$$/수식$$를 빼면 $$수식$${%s}a`=`{%s}$$/수식$$" % (a1,a2,a3,a2,a1,a3-a2)

    if(c1 == bb):
        s1 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에서 $$수식$${%s}$$/수식$$를 빼면 $$수식$${%s}a``{%s}`=`0$$/수식$$" % (a1,a2,a3,a3,a1,a2-a3)
    elif(c2 == bb):
        s2 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에서 $$수식$${%s}$$/수식$$를 빼면 $$수식$${%s}a``{%s}`=`0$$/수식$$" % (a1,a2,a3,a3,a1,a2-a3)
    elif(c3 == bb):
        s3 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에서 $$수식$${%s}$$/수식$$를 빼면 $$수식$${%s}a``{%s}`=`0$$/수식$$" % (a1,a2,a3,a3,a1,a2-a3)
    elif(c4 == bb):
        s4 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에서 $$수식$${%s}$$/수식$$를 빼면 $$수식$${%s}a``{%s}`=`0$$/수식$$" % (a1,a2,a3,a3,a1,a2-a3)
    else:
        s5 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에서 $$수식$${%s}$$/수식$$를 빼면 $$수식$${%s}a``{%s}`=`0$$/수식$$" % (a1,a2,a3,a3,a1,a2-a3)

    if(c1 == cc):
        s1 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에 2를 곱하면 $$수식$${%s}a`+`{%s}`=`{%s}$$/수식$$" % (a1,a2,a3,a1*2,a2*2,a3*2)
    elif(c2 == cc):
        s2 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에 2를 곱하면 $$수식$${%s}a`+`{%s}`=`{%s}$$/수식$$" % (a1,a2,a3,a1*2,a2*2,a3*2)
    elif(c3 == cc):
        s3 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에 2를 곱하면 $$수식$${%s}a`+`{%s}`=`{%s}$$/수식$$" % (a1,a2,a3,a1*2,a2*2,a3*2)
    elif(c4 == cc):
        s4 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에 2를 곱하면 $$수식$${%s}a`+`{%s}`=`{%s}$$/수식$$" % (a1,a2,a3,a1*2,a2*2,a3*2)
    else:
        s5 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변에 2를 곱하면 $$수식$${%s}a`+`{%s}`=`{%s}$$/수식$$" % (a1,a2,a3,a1*2,a2*2,a3*2)

    if(c1 == dd):
        s1 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변을 $$수식$$-{%s}$$/수식$$로 나누면 $$수식$$-a-{%s} over {%s}`=`{%s} over {%s}$$/수식$$" % (a1,a2,a3,a1,a2,a1,a3,a1)
    elif(c2 == dd):
        s2 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변을 $$수식$$-{%s}$$/수식$$로 나누면 $$수식$$-a-{%s} over {%s}`=`{%s} over {%s}$$/수식$$" % (
        a1, a2, a3, a1, a2, a1, a3, a1)
    elif(c3 == dd):
        s3 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변을 $$수식$$-{%s}$$/수식$$로 나누면 $$수식$$-a-{%s} over {%s}`=`{%s} over {%s}$$/수식$$" % (a1,a2,a3,a1,a2,a1,a3,a1)
    elif( c4 == dd):
        s4 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변을 $$수식$$-{%s}$$/수식$$로 나누면 $$수식$$-a-{%s} over {%s}`=`{%s} over {%s}$$/수식$$" % (a1,a2,a3,a1,a2,a1,a3,a1)
    else:
        s5 = "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변을 $$수식$$-{%s}$$/수식$$로 나누면 $$수식$$-a-{%s} over {%s}`=`{%s} over {%s}$$/수식$$" % (a1,a2,a3,a1,a2,a1,a3,a1)

    if(c1 == ee):
        s1 =  "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변을 -1을 곱하면 $$수식$$-{%s}a`-{%s}`=`-{%s}$$/수식$$" % (a1,a2,a3,a1,a2,a3)
    elif(c2 == ee):
        s2 =  "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변을 -1을 곱하면 $$수식$$-{%s}a`-{%s}`=`-{%s}$$/수식$$" % (a1,a2,a3,a1,a2,a3)
    elif(c3 == ee):
        s3 =  "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변을 -1을 곱하면 $$수식$$-{%s}a`-{%s}`=`-{%s}$$/수식$$" % (a1,a2,a3,a1,a2,a3)
    elif(c4 == ee):
        s4 =  "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변을 -1을 곱하면 $$수식$$-{%s}a`-{%s}`=`-{%s}$$/수식$$" % (a1,a2,a3,a1,a2,a3)
    else:
        s5 =  "$$수식$${%s}a+{%s}={%s}$$/수식$$의 양변을 -1을 곱하면 $$수식$$-{%s}a`-{%s}`=`-{%s}$$/수식$$" % (a1,a2,a3,a1,a2,a3)


    stem = stem.format(a1=a1, a2=a2, a3=a3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(K=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, K=answer_dict[correct_idx])

    return stem, answer, comment


def latterandexpress113_Stem_041():
    stem = "$$수식$$-{a1}a+{a2}over {a3}`=`{a4} over {a5}b`-`{a6}일``때,``{a7}a+{a8}b의``값은?$$/수식$$\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{KK}\n"
    comment = "(해설)\n" \
              "$$수식$$-{a1}a+{a2}over {a3}`=`{a4} over {a5}b`-`{a6}의``양변에``{a3}를``곱하면$$/수식$$\n" \
              "$$수식$$-{a1}a+{a2}`=`{b1}b`-`{b2}$$/수식$$\n" \
              "양변에 -2를 곱하면\n" \
              "$$수식$${c1}a{c2}`=`{b3}b`+`{b4}$$/수식$$\n" \
              "양변에 $$수식$${c3}$$/수식$$를 더하면\n" \
              "$$수식$${c1}a={b3}b+{b5}$$/수식$$\n" \
              "양변에 $$수식$${a8}b$$/수식$$를 더하면\n" \
              "$$수식$${a7}a+{a8}b={K}$$/수식$$\n\n"


    a1 = np.random.randint(2,10)
    a2 = np.random.randint(1,10)
    a5 = np.random.randint(2,5)
    a3 = a5*2
    a4 = np.random.randint(1,10)
    a6 = np.random.randint(10,20)
    b1 = 2*a4
    b2 = a3*a6
    c1 = 2*a1
    c2 = -2*a2
    c3 = -1*c2
    b3 = -2*b1
    b4 = 2*b2
    b5 = b4+c3
    a7 = a1*2
    a8 = 4*a4
    K = b5


    sol = np.random.randint(0,5)

    if (sol==0):
        q1 = K
        q2 = K+2
        q3 = K+4
        q4 = K+6
        q5 = K+8
        KK = "①"
    elif(sol==1):
        q1 = K-2
        q2 = K
        q3 = K+2
        q4 = K+4
        q5 = K+6
        KK = "②"
    elif(sol == 2):
        q1 = K - 4
        q2 = K - 2
        q3 = K
        q4 = K + 2
        q5 = K + 4
        KK = "③"
    elif(sol == 3):
        q1 = K - 6
        q2 = K - 4
        q3 = K - 2
        q4 = K
        q5 = K + 2
        KK = "④"
    else:
        q1 = K - 8
        q2 = K - 6
        q3 = K - 4
        q4 = K - 2
        q5 = K
        KK = "⑤"

    stem = stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
    answer = answer.format(KK = KK)
    comment = comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,b1=b1,b2=b2,b3=b3,b4=b4,b5=b5,c1=c1,c2=c2,c3=c3,K=K)

    return stem, answer, comment

def latterandexpress113_Stem_042():
    stem = "일차방정식$$수식$${s1} `=` {s2}$$/수식$$을 풀면?\n" \
           "① $$수식$$x`=`{c1}$$/수식$$\n" \
           "② $$수식$$x`=`{c2}$$/수식$$\n" \
           "③ $$수식$$x`=`{c3}$$/수식$$\n" \
           "④ $$수식$$x`=`{c4}$$/수식$$\n" \
           "⑤ $$수식$$x`=`{c5}$$/수식$$\n"
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${s1} = {s2}$$/수식$$에서 $$수식$$ {v5}x `=` {v6} $$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{a}$$/수식$$\n\n"

    while True:
        v1 = np.random.randint(-10,10)
        v2 = np.random.randint(-10,10)
        v3 = np.random.randint(-10,10)
        v4 = np.random.randint(-10,10)
        if v1!= 0 and v2 != 0 and v3!=0 and v4!=0 and (v1 - v3) != 0 and (v4 - v2) != 0 and (v4 - v2) % (v1 - v3) == 0:
            break

    v5 = v1 - v3
    v6 = v4 - v2
    a = v6 // v5
    b = v5 % v6

    s1 = "{v1}x`+`{v2}".format(v1=v1,v2=v2) if v2 > 0 else "{v1}x{v2}".format(v1=v1,v2=v2)
    s2 = "{v3}x`+`{v4}".format(v3=v3,v4=v4) if v4 > 0 else "{v3}x{v4}".format(v3=v3,v4=v4)


    idx = np.random.randint(0,5)
    candidates = [] 
    temp = a - 1 * idx

    for i in range(5):
        candidates.append(temp + 1 * i)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == a:
            correct_idx = i
            break


    stem = stem.format(s1=s1, s2=s2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2,v5=v5,v6=v6,a=a)

    return stem, answer, comment


def latterandexpress113_Stem_043():
    stem = "등식 $$수식$${s1} `=` {s2}$$/수식$$을 이항만을 이용하여 $$수식$$ ax`=`b LEFT ( a > 0 RIGHT ) $$/수식$$의 꼴로 고쳤을 때, 상수 $$수식$$a, b$$/수식$$에 대하여 $$수식$$a + b$$/수식$$의 값은?\n" \
           "① {c1}\n" \
           "② {c2}\n" \
           "③ {c3}\n" \
           "④ {c4}\n" \
           "⑤ {c5}\n"
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${s1} = {s2}$$/수식$$에서 $$수식$$ {v2}과 {v3}x $$/수식$$를 각각 이항하면\n" \
              "$$수식$${s3} = {s4} \t THEREFORE~{a}x`=`{b}$$/수식$$\n" \
              "따라서 $$수식$$ a`=`{a}, b`=`{b} $$/수식$$이므로" \
              "$$수식$$a+b`=`{result}$$/수식$$"

    while True:
        v1 = np.random.randint(-10,10)
        v2 = np.random.randint(-10,10)
        v3 = np.random.randint(-10,10)
        v4 = np.random.randint(-10,10)
        a = v1 - v3
        b = v4 - v2
        if v1 != 0 and v2 != 0 and v3 !=0 and v4 !=0 and a > 0 and b != 0:
            break
    result = a + b

    s1 = "{v1}x`+`{v2}".format(v1=v1,v2=v2) if v2 > 0 else "{v1}x{v2}".format(v1=v1,v2=v2)
    s2 = "{v3}x`+`{v4}".format(v3=v3,v4=v4) if v4 > 0 else "{v3}x{v4}".format(v3=v3,v4=v4)
    s3 = "{v1}x`+`{v3}x".format(v1=v1,v3=-1*v3) if v3 < 0 else "{v1}x{v3}x".format(v1=v1,v3=-1*v3)
    s4 = "{v4}`+`{v2}".format(v2=-1*v2,v4=v4) if v2 < 0 else "{v4}{v2}".format(v2=-1*v2,v4=v4)


    idx = np.random.randint(0,5)
    candidates = [] 
    temp = result - 1 * idx

    for i in range(5):
        candidates.append(temp + 1 * i)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break


    stem = stem.format(s1=s1, s2=s2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2,s3=s3,s4=s4,v2=v2,v3=v3,a=a,b=b,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_044():
    stem = "등식 $$수식$${s1} `=` {s2}$$/수식$$가 $$수식$$ x $$/수식$$에 대한 일차방정식이 되도록 하는 상수 $$수식$$ a $$/수식$$의 조건은?\n" \
           "① {c1}\n" \
           "② {c2}\n" \
           "③ {c3}\n" \
           "④ {c4}\n" \
           "⑤ {c5}\n"
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${s1} = {s2}$$/수식$$에서 $$수식$$ {s3} `=` {s4}$$/수식$$\n" \
              "이 방정식이 $$수식$$ x $$/수식$$에 대한 일차방정식이 되려면\n" \
              "$$수식$$THEREFORE~a`!=`{result}$$/수식$$"

    while True:
        v1 = np.random.randint(-10,10)
        v2 = np.random.randint(-10,10)
        v3 = [1,-1][np.random.randint(2)]
        v4 = np.random.randint(1,10)
        b = v4 - v2
        if v1 != 0 and v2 != 0 and v3 != 0 and v4 != 0 and b != 0 and v1 != v2 and v1 != v3:
            break
    result = v1
    
    s1 = "{v1}x`+`{v2}".format(v1=v1,v2=v2) if v2 > 0 else "{v1}x{v2}".format(v1=v1,v2=v2)
    s2 = "ax`+`{v4}".format(v4=v4) if v3 > 0 else "-ax`+`{v4}".format(v4=v4)
    s3 = "LEFT ( {v1}`+`a RIGHT )x".format(v1=v1) if v3 < 0 else "LEFT ({v1}`-`a RIGHT )x".format(v1=v1,v3=-1*v3)
    s4 = b
    candidates = [result, -1*result, v2,v2*-1,v3] 


    correct_idx = 0
    candidates2 = []
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            candidates2.append("$$수식$$a`!=`{c}$$/수식$$".format(c=c))
        else:
            q = ["!=","="][np.random.randint(2)]
            candidates2.append("$$수식$$a`{q}`{c}$$/수식$$".format(q=q,c=c))

    c1, c2, c3, c4, c5 = candidates2


    stem = stem.format(s1=s1, s2=s2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,s3=s3,s4=s4,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_045():
    stem = "일차방정식 $$수식$${s1}`=`{s2}$$/수식$$를 풀면\n" \
           "① $$수식$$x`=`{c1}$$/수식$$\n" \
           "② $$수식$$x`=`{c2}$$/수식$$\n" \
           "③ $$수식$$x`=`{c3}$$/수식$$\n" \
           "④ $$수식$$x`=`{c4}$$/수식$$\n" \
           "⑤ $$수식$$x`=`{c5}$$/수식$$\n"  ## 표가 안됨
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${s1}`=`{s2}$$/수식$$에서\n" \
              "$$수식$${ss1}`=`{ss2} `,` {svvv1}x`=`{svvv2}$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{result}$$/수식$$\n\n"

    while True:
        v1 = np.random.randint(-10,10)
        v2 = np.random.randint(-10,10)
        v3 = np.random.randint(-10,10) 
        v4 = np.random.randint(-10,10)
        v5 = np.random.randint(-10,10)
        v6 = np.random.randint(-10,10) 
        v7 = np.random.randint(-10,10) 
        if v1 == 0 or v2 == 0 or v3 == 0 or v4 == 0 or v5 == 0 or v6 == 0 or v7 == 0:
            continue
        vv1 = v1 * v2
        vv2 = v1 * v3
        vv3 = v4 * v5
        vv4 = v4 * v6
        vvv1 = vv1 - vv3
        vvv2 = vv4 + v7 - vv2
        if vvv1 == 0 or vvv2 == 0:
            continue
        result = vvv2 // vvv1
        result_mod = vvv2 % vvv1
        if vvv1 != 0 and vvv2 != 0 and result_mod == 0 and result < 10 and result > -10:
            break

    sv1 = vtos(v1,1,1)
    sv2 = vtos(v2,1,1)
    sv3 = vtos(v3,0)
    sv4 = vtos(v4,1,1)
    sv5 = vtos(v5,1,1)
    sv6 = vtos(v6,0)
    sv7 = vtos(v7,0)

    s1 = "{sv1} LEFT ( {sv2}x {sv3} RIGHT )".format(sv1=sv1,sv2=sv2,sv3=sv3)
    s2 = "{sv4} LEFT ( {sv5}x {sv6} RIGHT ) {sv7}".format(sv4=sv4,sv5=sv5,sv6=sv6,sv7=sv7)
    svv1 = vtos(vv1,1,1)
    svv2 = vtos(vv2,0)
    svv3 = vtos(vv3,1,1)
    svv4 = vtos(vv4,0)
    
    ss1 = "{svv1}x {svv2}".format(svv1=svv1,svv2=svv2)
    ss2 = "{svv3}x {svv4} {sv7}".format(svv3=svv3,svv4=svv4,sv7=sv7)

    svvv1 = vtos(vvv1,1,1)
    svvv2 = vtos(vvv2,0,1)

    idx = np.random.randint(0,5)
    candidates = [] 
    temp = result - 2 * idx

    for i in range(5):
        candidates.append(temp + 2 * i)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(s1=s1,s2=s2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,ss1=ss1,ss2=ss2,svvv1=svvv1,svvv2=svvv2,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_046():
    stem = "일차방정식 $$수식$${s1}`=`{s2}$$/수식$$를 풀면\n" \
           "① $$수식$$x`=`{c1}$$/수식$$\n" \
           "② $$수식$$x`=`{c2}$$/수식$$\n" \
           "③ $$수식$$x`=`{c3}$$/수식$$\n" \
           "④ $$수식$$x`=`{c4}$$/수식$$\n" \
           "⑤ $$수식$$x`=`{c5}$$/수식$$\n"  ## 표가 안됨
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${s1}`=`{s2}에서$$/수식$$\n" \
              "$$수식$$`=`{ss1}`=`{ss2}$$/수식$$\n" \
              "$$수식$${vvv1}x`=`{vvv2} THEREFORE~x`=`{result1}, 즉 a `=` {result1}$$/수식$$\n" \
              "$$수식$$ THEREFORE~ {s3}`-`{s4}`=`{ss3}`-`{ss4} $$/수식$$\n" \
              "$$수식$$ `=`{ss5}`-`{ss6}`=`{vvv3}`-`{vvv4} `=`{result2}$$/수식$$\n\n" 


    while True:
        v1 = np.random.randint(-10,10)
        v2 = np.random.randint(-10,10)
        v3 = np.random.randint(-10,10) 
        v4 = np.random.randint(-10,10)
        v5 = np.random.randint(-10,10)
        v6 = np.random.randint(-10,10) 
        v7 = np.random.randint(-10,10)
        v8 = np.random.randint(-10,10)
        v9 = np.random.randint(-10,10)
        v10 = np.random.randint(-10,10)
        v11 = np.random.randint(-10,10)

        if v1 == 0 or v2 == 0 or v3 == 0 or v4 == 0 or v5 == 0 or v6 == 0 or v7 == 0:
            continue
        if v8 == 0 or v9 == 0 or v10 == 0 or v11 == 0:
            continue


        vv1 = v2 * v3
        vv2 = v2 * v4
        vv3 = v5 * v6
        vv4 = v5 * v7
        vvv1 = vv1 - vv3
        vvv2 = vv4 - v1 - vv2

        if vvv1 == 0 or vvv2 == 0:
            continue

        result1 = vvv2 // vvv1
        result1_mod = vvv2 % vvv1

        vv5 = v8 * result1 + v9
        vv6 = v10 + result1 * v11
        vvv3 = abs(vv5)
        vvv4 = abs(vv6)
        result2 = vvv3 - vvv4 

        if result1_mod == 0 and result1 < 10 and result1 > -10:
            break
        

    sv1 = vtos(v1,0,1)
    sv2 = vtos(v2,1)
    sv3 = vtos(v3,1,1)
    sv4 = vtos(v4,0)
    sv5 = vtos(v5,1,1)
    sv6 = vtos(v6,1,1)
    sv7 = vtos(v7,0)

    sv8 = vtos(v8,1,1)
    sv9 = vtos(v9,0)
    sv10 = vtos(v10,0,1)
    sv11 = vtos(v11,1)

    s1 = "{sv1} {sv2} LEFT ( {sv3}x  {sv4} RIGHT )".format(sv1=sv1,sv2=sv2,sv3=sv3,sv4=sv4)
    s2 = "{sv5} LEFT ( {sv6}x {sv7} RIGHT )".format(sv5=sv5,sv6=sv6,sv7=sv7)

    s3 = "LEFT | {sv8}a {sv9} RIGHT | ".format(sv8=sv8,sv9=sv9)
    s4 = "LEFT | {sv10} {sv11}a RIGHT | ".format(sv10=sv10,sv11=sv11)

    svv1 = vtos(vv1,1)
    svv2 = vtos(vv2,0)

    svv3 = vtos(vv3,1,1)
    svv4 = vtos(vv4,0)

    svv5 = vtos(vv5,0,1)
    svv6 = vtos(vv6,0,1)


    ss1 = "{sv1} {svv1}x {svv2}".format(svv1=svv1,svv2=svv2,sv1=sv1)
    ss2 = "{svv3}x {svv4} ".format(svv3=svv3,svv4=svv4)
    
    sresult1 = vtos2(result1)
    ssv8 = vtos(v8,0,1)
    ssv11 = vtos(v11,0)
    ss3 = "LEFT | {ssv8}`TIMES`{sresult1} {sv9} RIGHT | ".format(ssv8=ssv8,sv9=sv9,sresult1=sresult1)
    ss4 = "LEFT | {sv10} {ssv11} `TIMES`{sresult1} RIGHT | ".format(sv10=sv10,ssv11=ssv11,sresult1=sresult1)

    ss5 = "LEFT | {svv5} RIGHT | ".format(svv5=svv5)
    ss6 = "LEFT | {svv6} RIGHT | ".format(svv6=svv6)

    svvv1 = vtos(vvv1,1,1)
    svvv2 = vtos(vvv2,0,1)

    svvv3 = vtos(vvv1,1,1)
    svvv4 = vtos(vvv2,0,1)

    idx = np.random.randint(0,5)
    candidates = [] 
    temp = result2 - 2 * idx

    for i in range(5):
        candidates.append(temp + 2 * i)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result2:
            correct_idx = i
            break

    stem = stem.format(s1=s1,s2=s2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,ss1=ss1,ss2=ss2,vvv1=vvv1,vvv2=vvv2,result1=result1,s3=s3,s4=s4,ss3=ss3,ss4=ss4,ss5=ss5,ss6=ss6,vvv3=vvv3,vvv4=vvv4,result2=result2)

    return stem, answer, comment


def latterandexpress113_Stem_047():
    stem = "일차방정식 $$수식$${s1}`=`{s2}$$/수식$$를 풀면\n" \
           "① $$수식$$x`=`{c1}$$/수식$$\n" \
           "② $$수식$$x`=`{c2}$$/수식$$\n" \
           "③ $$수식$$x`=`{c3}$$/수식$$\n" \
           "④ $$수식$$x`=`{c4}$$/수식$$\n" \
           "⑤ $$수식$$x`=`{c5}$$/수식$$\n"  ## 표가 안됨
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "주어진 일차방정식의 양변에 을 곱하면\n"\
              "$$수식$${s1}`=`{s2}$$/수식$$, $$수식$${ss1}`=`{ss2}$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{result}$$/수식$$\n\n" 


    while True:
        v1 = np.random.randint(-9,10) / 10
        v2 = np.random.randint(-9,10)
        v3 = np.random.randint(-9,10) / 10
        if v1 == 0 or v2 == 0 or v3 == 0:
            continue

        vv1 = int(v1 * 10)
        vv2 = int(v2 * 10)
        vv3 = int(v3 * 10)

        vvv1 = vv1 - vv3
        vvv2 = -1 * vv2

        if vvv1 == 0:
            continue

        result = vvv2 // vvv1
        result_mod = vvv2 % vvv1

        if result_mod == 0 and result < 10 and result > -10:
            break
        

    sv1 = vtos(v1,1,1)
    sv2 = vtos(v2,0)
    sv3 = vtos(v3,1,1)

    s1 = "{sv1}x {sv2}".format(sv1=sv1,sv2=sv2)
    s2 = "{sv3}x".format(sv3=sv3)

    svv1 = vtos(vv1,1,1)
    svv2 = vtos(vv2,0)
    svv3 = vtos(vv3,1,1)

    ss1 = "{svv1}x {svv2}".format(svv1=svv1,svv2=svv2)
    ss2 = "{svv3}x  ".format(svv3=svv3)


    idx = np.random.randint(0,5)
    candidates = [] 
    temp = result - 2 * idx

    for i in range(5):
        candidates.append(temp + 2 * i)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(s1=s1,s2=s2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,ss1=ss1,ss2=ss2,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_048():
    stem = "방정식 $$수식$${a1}(x-{a2})`=`-{a3}-{a4}({a5}-x)의``해를``x=a라``할``때$$/수식$$\n$$수식$$a보다``작은``자연수의``개수는?$$/수식$$\n" \
           "① $$수식$$1$$/수식$$\n" \
           "② $$수식$$2$$/수식$$\n" \
           "③ $$수식$$3$$/수식$$\n" \
           "④ $$수식$$4$$/수식$$\n" \
           "⑤ $$수식$$5$$/수식$$\n"
    answer = "(정답)\n{result1}\n"
    comment = "(해설)\n" \
              "주어진 일차방정식의 양변에 10을 곱하면\n" \
              "$$수식$${b1}(x-{a2})`=`-{b2}-{b3}({a5}-x)$$/수식$$\n" \
              "$$수식$${b1}x-{c1}`=`-{b2}-{c2}+{b3}x,``{d1}x={d2}$$/수식$$\n" \
              "$$수식$$THEREFORE~ x = {d5} over {d4}$$/수식$$\n" \
              "따라서 $$수식$$a`=`{d5} over {d4}`=`{d3}(최대``소수``3자리수``까지``표현)$$/수식$$이므로 a보다 작은 자연수는\n$$수식$${s1}의``{result}개이다.$$/수식$$\n\n" \

    while(1):
        a1 = np.random.randint(2,10)/10
        a2 = np.random.randint(1,10)
        a3 = np.random.randint(1,10)
        a4 = np.random.randint(1,10)/10
        a5 = np.random.randint(1,10)

        b1 = math.floor(a1*10)
        b2 = math.floor(a3*10)
        b3 = math.floor(a4*10)

        c1 = b1*a2
        c2 = b3*a5

        d1 = b1-b3
        d2 = b1*a2-b2-b3*a5
        if(d1<0 and d2<0):
            d4 = d1*(-1)
            d5 = d2*(-1)
        else:
            d4 = d1
            d5 = d2

        if((d1>0 and d2>0) or (d1<0 and d2<0)):
            if(d2 % d1 != 0):
                if(d2/d1 < 6 and d2/d1>1):
                    break

    d3 = d2/d1
    d3 = round(d3,3)

    result = math.floor(d3)
    s1 = list(range(1,result+1))
    s1 = ','.join(map(str, s1))

    if result == 1: result1 = "①"
    elif result == 2 : result1 = "②"
    elif result == 3 : result1 = "③"
    elif result == 4 : result1 = "④"
    else : result1 = "⑤"

    stem = stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,c1=c1,c2=c2)
    answer = answer.format(result1=result1)
    comment = comment.format(d4=d4,d5=d5,s1=s1,b1=b1,b2=b2,a2=a2,b3=b3,a5=a5,c1=c1,c2=c2,d1=d1,d2=d2,d3=d3, result=result)

    return stem, answer, comment


def latterandexpress113_Stem_049():
    stem = "일차방정식 $$수식$$1 over {a1}`x`+`{a2} over {a3}`=`{a4} over {a5}`를``풀면?$$/수식$$\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "주어진 일차방정식의 양변에 $$수식$${a1}$$/수식$$ 을 곱하면\n" \
              "$$수식$$x+{b1}`=`{b2}$$/수식$$\n" \
              "$$수식$$THEREFORE~ x`=`{b3}$$/수식$$\n\n"

    while(1):
        a2 = np.random.randint(1,10)
        a3 = np.random.randint(1,10)
        a4 = np.random.randint(1,10)
        a5 = np.random.randint(1,10)
        a1 = a3*a5

        b1 = a5*a2
        b2 = a4*a3
        b3 = b2-b1
        if(a2!=a3 and a4!=a5):
            if(b3 != 0):
                break

    sol = np.random.randint(0,5)

    if (sol==0):
        q1 = "x = {%s}" % (b3)
        q2 = "x = {%s}" % (b3 - 1)
        q3 = "x = {%s}" % (b3 - 2)
        q4 = "x = {%s}" % (b3*(-1))
        q5 = "x = {%s}" % (b3*(-1)+1)
        answer_num = "①"
    elif(sol==1):
        q1 = "x = {%s}" % (b3-1)
        q2 = "x = {%s}" % (b3)
        q3 = "x = {%s}" % (b3 +1)
        q4 = "x = {%s}" % (b3 * (-1))
        q5 = "x = {%s}" % (b3 * (-1) + 1)
        answer_num = "②"
    elif(sol == 2):
        q1 = "x = {%s}" % (b3-2)
        q2 = "x = {%s}" % (b3 - 1)
        q3 = "x = {%s}" % (b3)
        q4 = "x = {%s}" % (b3 * (-1))
        q5 = "x = {%s}" % (b3 * (-1) + 1)
        answer_num = "③"
    elif(sol == 3):
        q1 = "x = {%s}" % (b3-3)
        q2 = "x = {%s}" % (b3 - 2)
        q3 = "x = {%s}" % (b3 - 1)
        q4 = "x = {%s}" % (b3)
        q5 = "x = {%s}" % (b3 * (-1))
        answer_num = "④"
    else:
        q1 = "x = {%s}" % (b3*(-1)-1)
        q2 = "x = {%s}" % (b3 *(-1))
        q3 = "x = {%s}" % (b3 - 2)
        q4 = "x = {%s}" % (b3 - 1)
        q5 = "x = {%s}" % (b3)
        answer_num = "⑤"


    stem = stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,b1=b1,b2=b2,b3=b3)

    return stem, answer, comment


def latterandexpress113_Stem_050():
    stem = "일차방정식 $$수식$${a1}(x-{a2})=x-{a3}의``해를``x=a,$$/수식$$\n" \
           "일차방정식 $$수식$$x-{b1} over {b2}`=`{b3}`-`1 over {b4}`x의``해를``x=b라``할``때,$$/수식$$\n" \
           "a+b의 값은?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${a1}(x-{a2})`=`x-{a3}의``양변에``10을``곱하면$$/수식$$\n" \
              "$$수식$${a4}(x-{a2})`=`10(x-{a3}),````{a4}x-{a5}`=`10x-{a6}$$/수식$$\n" \
              "$$수식$${a9}x = {a7}````THEREFORE~ x={a8},````즉,a={a8}$$/수식$$\n" \
              "$$수식$$x-{b1} over {b2}`=`{b3}-`1 over {b4}`x의``양변에``{b5}를``곱하면$$/수식$$\n" \
              "$$수식$${b4}(x-{b1})`=`{b6}-{b2}x,````{b4}x-{b7}`=`{b6}-{b2}x$$/수식$$\n" \
              "$$수식$${b8}x`=`{b9}````THEREFORE~ x = {b10},``즉,b={b10}$$/수식$$\n" \
              "$$수식$$THEREFORE~ a+b`=`{a8}+{b10}`=`{result}$$/수식$$\n\n"

    while True:
        a1 = np.random.randint(2,10)/10
        a2 = np.random.randint(1,10)
        a3 = np.random.randint(1,10)
        a4 = math.floor(a1*10)
        a5 = a4*a2
        a6 = a3*10
        a7 = a6*(-1)+a5
        a9 = a4-10

        b1 = np.random.randint(1,10)
        b2 = np.random.randint(2,10)
        b3 = np.random.randint(1,10)
        b4 = np.random.randint(2,10)
        b5 = b2*b4
        b6 = b3*b5
        b7 = b4*b1
        b8 = b4+b2
        b9 = b6+b7

        a8 = math.floor(a7 / a9)
        b10 = math.floor(b9 / b8)
        result = a8 + b10

        if(a4!=a5 and b2!=b4 and a6>a5):
            if(b9 % b8 == 0 and a7 % a9 == 0):
                break


    sol = np.random.randint(0,5)

    if (sol==0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result + 1)
        q3 = "{%s}" % (result + 2)
        q4 = "{%s}" % (result + 3)
        q5 = "{%s}" % (result + 4)
        answer_num = "①"
    elif(sol==1):
        q1 = "{%s}" % (result - 1)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result + 1)
        q4 = "{%s}" % (result + 2)
        q5 = "{%s}" % (result + 3)
        answer_num = "②"
    elif(sol == 2):
        q1 = "{%s}" % (result - 2)
        q2 = "{%s}" % (result - 1)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result + 1)
        q5 = "{%s}" % (result + 2)
        answer_num = "③"
    elif(sol == 3):
        q1 = "{%s}" % (result-3)
        q2 = "{%s}" % (result - 2)
        q3 = "{%s}" % (result - 1)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result + 1)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result - 4)
        q2 = "{%s}" % (result - 3)
        q3 = "{%s}" % (result - 2)
        q4 = "{%s}" % (result - 1)
        q5 = "{%s}" % (result)
        answer_num = "⑤"

    stem = stem.format(a1=a1,a2=a2,a3=a3,b1=b1,b2=b2,b3=b3,b4=b4, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,a9=a9,b1=b1,b2=b2,b3=b3,b4=b4,b5=b5,b6=b6,b7=b7,b8=b8,b9=b9,b10=b10, result=result)

    return stem, answer, comment


def latterandexpress113_Stem_051():
    stem = "방정식 $$수식$${a1}(x+{a2})`=`x-{a4} over {a3}`의``해를``x`=`a라``할``때,``a의``약수의``개수는?$$/수식$$\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n" \
              "양변에 $$수식$${b1}$$/수식$$을 곱하면\n" \
              "$$수식$${aa1}(x+{a2})`=`{b2}(x-{a4}),``{aa1}x+{b3}`=`{b2}x-{b4}$$/수식$$\n" \
              "$$수식$${d1}x`=`{d2}````THEREFORE~x={d3}$$/수식$$\n" \
              "따라서 a = $$수식$${d3}이고,``{d3}`=`2^{e1} TIMES 3^{e2}`이므로$$/수식$$\n" \
              "a의 약수의 개수는 $$수식$$({e1}+1)({e2}+1)`=`{e3}$$/수식$$\n\n"

    while True:
        a1 = np.random.randint(1,10)/10
        a2 = np.random.randint(1,10)
        a3 = [2,3,4,5,6,8,25][np.random.randint(0,7)]
        a4 = np.random.randint(1,10)

        if(a3==2): b1 = 10
        elif(a3==3): b1 = 30
        elif(a3==4): b1 = 20
        elif(a3==5): b1 = 10
        elif(a3==6): b1 = 30
        elif(a3==8): b1 = 40
        else: b1 = 50

        aa1 = math.floor(a1 * b1)

        b2 = math.floor(b1/a3)
        b3 = aa1*a2
        b4 = b2*a4

        d1 = aa1 - b2
        d2 = (-1) * b4 - b3
        if (d1>0 and d2>0) or (d1<0 and d2<0):
            if(d2!=0 and d1!=0):
                if(d2%d1 == 0):
                    if(d2/d1 in [6,18,54,162,12,24,48,96]):
                        break

    d3 = math.floor(d2 / d1)

    if(d3==6): e1=e2=1; e3=4; result="①"
    elif(d3==18): e1=1; e2=2; e3=6; result="②"
    elif(d3==12): e1=2; e2=1; e3=6; result="②"
    elif(d3==54): e1=1; e2=3; e3=8; result="③"
    elif(d3==24): e1=3; e2=1; e3=8; result="③"
    elif(d3==162): e1=1; e2=4; e3=10; result="④"
    elif(d3==48): e1=4; e2=1; e3=10; result="④"
    else: e1=5; e2=1; e3=12; result="⑤"

    c1 = 4
    c2 = 6
    c3 = 8
    c4 = 10
    c5 = 12

    stem = stem.format(a1=a1,a2=a2,a3=a3, a4=a4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(result=result)
    comment = comment.format(b1=b1,b2=b2,b3=b3,b4=b4,aa1=aa1,a2=a2,a3=a3,a4=a4,d1=d1,d2=d2,d3=d3,e1=e1,e2=e2,e3=e3)

    return stem, answer, comment


def latterandexpress113_Stem_052():
    stem = "일차방정식 $$수식$$1 over 5`x`-`{a1}x`=`-{a2}의``해를``x=a,$$/수식$$\n" \
           "일차방정식 $$수식$$x-{b1} over 2`-`{b2} over 5`=`{b3}(x-{b4})의``해를``x=b라``할``때,$$/수식$$\n" \
           "a-b의 값은?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$$1 over 5`x`-`{a1}x`=`-{a2}에서$$/수식$$\n" \
              "$$수식$$1 over 5`x`-`{a3} over 5`x`=`-`{a4} over 5$$/수식$$\n" \
              "양변에 5를 곱하면\n" \
              "$$수식$$x-{a3}x`=`-{a4},``{a55}x`=`-{a4}$$/수식$$\n" \
              "$$수식$$THEREFORE~ x`=`{a6},``즉``a`=`{a6}$$/수식$$\n" \
              "$$수식$$x-{b1} over 2`-`{b2} over 5`=`{b3}(x-{b4})에서$$/수식$$\n" \
              "$$수식$$x-{b1} over 2`-`{b2} over 5`=`{b5} over 5`(x-{b4})$$/수식$$\n" \
              "양변에 10을 곱하면\n" \
              "$$수식$$5(x-{b1})-{b6}`=`{b7}(x-{b4})$$/수식$$\n" \
              "$$수식$$5x-{b8}-{b6}`=`{b7}x-{b9},``{c11}x`=`{c2}$$/수식$$\n" \
              "$$수식$$THEREFORE~ x`=`{c3},``즉``b`=`{c3}$$/수식$$\n" \
              "$$수식$$THEREFORE~ a-b`=`{a6}-({c3})`=`{result}$$/수식$$\n\n"

    while True:
        a1 = np.random.randint(1, 10)/10
        a2 = np.random.randint(1, 10)/10
        a3 = math.floor(a1*5)
        a4 = math.floor(a2*5)
        a5 = 1-a3
        if a5 == 1: a55 = ""
        elif a5 == -1: a55="-"
        else: a55 = a5

        b1 = np.random.randint(2, 10)
        b2 = np.random.randint(1, 10)
        b3 = np.random.randint(1, 10)/10
        b4 = np.random.randint(1, 6)
        b5 = math.floor(b3*5)
        b6 = b2*2
        b7 = 2*b5
        b8 = b1*5
        b9 = b4*b7
        c1 = 5-b7
        if c1 == 1: c11 = ""
        elif c1 == -1: c11="-"
        else: c11 = c1
        c2 = b8+b6-b9


        if(a1*10 % 2 == 0 and a2*10 % 2 == 0 and b3*10 % 2 == 0):
            if(c2!=0 and c1!=0):
                if(a4!=0 and a5!=0):
                    if(a4%a5 == 0):
                        if(c2%c1 == 0):
                            if(a4/a5 > c2/c1):
                                break

    a6 = math.floor((-1)*a4 / a5)
    c3 = math.floor(c2 / c1)
    result = a6 - c3

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result + 1)
        q3 = "{%s}" % (result + 2)
        q4 = "{%s}" % (result + 3)
        q5 = "{%s}" % (result + 4)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result - 1)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result + 1)
        q4 = "{%s}" % (result + 2)
        q5 = "{%s}" % (result + 3)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result - 2)
        q2 = "{%s}" % (result - 1)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result + 1)
        q5 = "{%s}" % (result + 2)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result - 3)
        q2 = "{%s}" % (result - 2)
        q3 = "{%s}" % (result - 1)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result + 1)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result - 4)
        q2 = "{%s}" % (result - 3)
        q3 = "{%s}" % (result - 2)
        q4 = "{%s}" % (result - 1)
        q5 = "{%s}" % (result)
        answer_num = "⑤"

    stem = stem.format(a1=a1, a2=a2, b1=b1, b2=b2, b3=b3, b4=b4, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, a55=a55, a6=a6, b1=b1, b2=b2, b3=b3, b4=b4,
                             b5=b5, b6=b6, b7=b7, b8=b8, b9=b9, c11=c11,c2=c2,c3=c3, result=result)

    return stem, answer, comment


def latterandexpress113_Stem_053():
    stem = "두 일차방정식 $$수식$${a1}+{a2}x`=`{a3}x+{a4},$$/수식$$\n" \
           "$$수식$${b1}(x-{b2})`=`1 over {b3}`x`+{b4}의``해를``각각``x`=`a,`x`=`b라``할``때,$$/수식$$\n" \
           "a+b의 값은?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${a1}+{a2}x`=`{a3}x+{a4}에서``{a5}x`=`{a6}이므로``x`=`{a7}$$/수식$$\n" \
              "$$수식$${b1}(x-{b2})`=`1 over {b3}`x`+{b4}의``양변에``10을``곱하면$$/수식$$\n" \
              "$$수식$${b6}(x-{b2})`=`{b5}x+{b7},``{b6}x`-`{b8}`=`{b5}x`+`{b7}$$/수식$$\n" \
              "$$수식$${b9}x`=`{b10}````THEREFORE~x`=`{b11}$$/수식$$\n" \
              "따라서 $$수식$$a`=`{a7},``b`=`{b11}이므로$$/수식$$\n" \
              "$$수식$$a`+`b`=`{a7}+{k1}{b11}{k2}`=`{result}$$/수식$$\n\n"

    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(2, 10)
        a3 = np.random.randint(2, 10)
        a4 = np.random.randint(1, 10)
        a5 = a2-a3
        a6 = a4-a1

        b1 = np.random.randint(1, 10)/10
        b2 = np.random.randint(1, 10)
        b3 = [2,5,10][np.random.randint(0,3)]
        b4 = np.random.randint(1, 10)

        if(b3==2): b5=5
        elif(b3==5): b5=2
        else: b5 = 1
        b6 = math.floor(b1*10)
        b7 = b4*10
        b8 = b6*b2
        b9 = b6-b5
        b10 = b7+b8

        if(a6!=0 and a5!=0):
            if(b9!=0 and b10!=0):
                if(a6%a5 == 0 and b10%b9 == 0):
                    if(a6/a5 > -10 and a6/a5 < 10 and b10/b9 > -10 and b10/b9 < 10):
                        break


    a7 = math.floor(a6/a5)
    b11 = math.floor(b10 / b9)
    result = a7 + b11

    if(b11<0):
        k1 = "("
        k2 = ")"
    else:
        k1 = k2 = ""

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result * -1)
        q3 = "{%s}" % (math.floor(result / -2))
        q4 = "{%s}" % (result - 1)
        q5 = "{%s}" % (math.floor(result / 2))
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result * -1)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (math.floor(result / -2))
        q4 = "{%s}" % (result - 1)
        q5 = "{%s}" % (math.floor(result / 2))
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result * -1)
        q2 = "{%s}" % (result - 1)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (math.floor(result / 2))
        q5 = "{%s}" % (math.floor(result / -2))
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result * -1)
        q2 = "{%s}" % (math.floor(result / -2))
        q3 = "{%s}" % (result - 1)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (math.floor(result / 2))
        answer_num = "④"
    else:
        q1 = "{%s}" % (result * -1)
        q2 = "{%s}" % (math.floor(result / -2))
        q3 = "{%s}" % (result - 1)
        q4 = "{%s}" % (math.floor(result / 2))
        q5 = "{%s}" % (result)
        answer_num = "⑤"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, b1=b1, b2=b2, b3=b3, b4=b4, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, b1=b1, b2=b2, b3=b3, b4=b4,
                             b5=b5, b6=b6, b7=b7, b8=b8, b9=b9, b10=b10,b11=b11,k1=k1,k2=k2,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_054():
    stem = "다음 x에 대한 두 일차방정식의 해가 서로 같을 때, 상수 a의 값은?\n" \
           "$$표$$$$수식$${a1}x-{a2}`=`{a3}(x-{a4}),``{b1}x-{b2}({b3}x`+`a)`=`{b4}$$/수식$$$$/표$$\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${a1}x-{a2}`=`{a3}(x-{a4})에서``{a1}x-{a2}`=`{a3}x-{a5}$$/수식$$\n" \
              "$$수식$${a6}x`=`{a7}````````THEREFORE~x`=`{a8}$$/수식$$\n" \
              "$$수식$${b1}x-{b2}({b3}x`+`a)`=`{b4}에``x`=`{a8}을``대입하면$$/수식$$\n" \
              "$$수식$${c1}-{b2}({c2}+a)`=`{b4},``{c1}`{K}`{c3}`-{b2}a`=`{b4}$$/수식$$\n" \
              "따라서 $$수식$$-{b2}a`=`{c4}````````THEREFORE~a`=`{result}$$/수식$$\n\n"

    while True:
        a1 = np.random.randint(2, 6)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(2, 10)
        a4 = np.random.randint(1, 6)
        a5 = a3*a4
        a6 = a1-a3
        a7 = a2-a5

        if(a7!=0 and a6!=0):
            if(a7 % a6 == 0):
                break

    a8 = math.floor(a7 / a6)

    while True:
        b1 = np.random.randint(2, 10)
        b2 = np.random.randint(2, 10)
        b3 = np.random.randint(2, 6)
        b4 = np.random.randint(1, 10)

        c1 = b1 * a8
        c2 = b3 * a8
        c3 = b2 * c2 * (-1)
        c4 = b4 + c3 - c1

        if(c4!=0 and b2!=0):
            if(c4%b2 == 0):
                if(math.floor(c4 / b2*(-1))-2!=math.floor(c4 / b2*(-1))*(-1)+4 and math.floor(c4 / b2*(-1))-2!=math.floor(c4 / b2*(-1))*(-1)+2 and  math.floor(c4 / b2*(-1))-4!=math.floor(c4 / b2*(-1))*(-1)+4 and math.floor(c4 / b2*(-1))-4!=math.floor(c4 / b2*(-1))*(-1)+2):
                    break

    result = math.floor(c4 / b2*(-1))

    if(a8 < 0): K = "+"
    else: K = ""

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result - 2)
        q3 = "{%s}" % (result - 4)
        q4 = "{%s}" % (result * (-1) + 4)
        q5 = "{%s}" % (result * (-1) + 2)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result + 2)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result - 2)
        q4 = "{%s}" % (result * (-1) + 2)
        q5 = "{%s}" % (result * (- 1))
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result + 4)
        q2 = "{%s}" % (result + 2)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result * (-1))
        q5 = "{%s}" % (result * (-1) - 2)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result * (-1) - 4)
        q2 = "{%s}" % (result * (-1) - 2)
        q3 = "{%s}" % (result * (-1))
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result - 2)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result * (-1) - 2)
        q2 = "{%s}" % (result * (-1))
        q3 = "{%s}" % (result - 4)
        q4 = "{%s}" % (result - 2)
        q5 = "{%s}" % (result)
        answer_num = "⑤"

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, b1=b1, b2=b2, b3=b3, b4=b4, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, a8=a8, b1=b1, b2=b2, b3=b3, b4=b4,
                             c1=c1,c2=c2,c3=c3,c4=c4,result=result, K=K)

    return stem, answer, comment


def latterandexpress113_Stem_055():
    stem = "일차방정식 $$수식$${a1}x-{a2}`=`{a7}x-{a4}를``푸는데$$/수식$$\n" \
           "우변의 x의 계수 $$수식$${a7}$$/수식$$를 잘못 보고 풀었더니 해가 $$수식$$x={b1}$$/수식$$이 나왔다.\n" \
           "$$수식$${a7}$$/수식$$를 어떤 수로 잘못 보았는지 구하시오.\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n" \
              "$$수식$${a3}$$/수식$$를 a로 잘못 보았다고 하면\n" \
              "$$수식$${a1}x-{a2}`=`ax-{a4}이고``이``방정식에``x={b1}을``대입하면$$/수식$$\n" \
              "$$수식$${b2}-{a2}`=`{b3}a-{a4}````````THEREFORE~a=`{result}$$/수식$$\n" \
              "$$수식$$따라서``{a7}를``{result}로``잘못``보았다.$$/수식$$\n\n"

    while True:
        a1 = np.random.randint(2, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(2, 10)
        a4 = np.random.randint(1, 10)
        a5 = a2-a4
        a6 = a1-a3
        a7 = np.random.randint(2, 10)

        if(a5==a6): b1=1; b3=""
        elif(a5==(-1)*a6): b1=-1; b3="-"
        elif(a5==2*a6): b1=2; b3 = 2
        elif(a5==(-2)*a6): b1=-2; b3=-2
        else: b1 = 0

        b2 = b1*a1

        if(a5 == a6 or a5 == (-1)*a6 or a5==(-2)*a6 or a5 == 2*a6):
            if(a5!=0 and a6!=0 and b2!=a5):
                if((b2-a2+a4)%b1 == 0):
                    if(a1!=a2 and a3!=a4 and a7!=a3):
                        break

    result = math.floor((b2-a5)/b1)

    sol = np.random.randint(0, 5)

    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, b1=b1, b2=b2, a5=a5, a6=a6, a7=a7)
    answer = answer.format(result=result)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, b1=b1, b2=b2, b3=b3, result=result, a7=a7)

    return stem, answer, comment


def latterandexpress113_Stem_056():
    stem = "x에 대한 일차방정식 $$수식$$ax+{a1}`=`-{a2}({a3}x+{a4})의``해가$$/수식$$\n" \
           "음의 정수가 되도록 하는 모든 정수 a의 값의 합은?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$$ax+{a1}`=`-{a2}({a3}x+{a4})에서``ax+{a1}`=`-{a5}x-{a6}$$/수식$$\n" \
              "$$수식$$(a+{a5})x`=`-{a7}````````THEREFORE~x`=`-`{a7} over a+{a5}$$/수식$$\n" \
              "$$수식$$이때``-`{a7} over a+{a5}`가``음의``정수이려면``a+{a5}이``{a7}의 약수$$/수식$$\n" \
              "즉, $$수식$$a+{a5}은``1``또는``{b1}``또는``{a7}이어야``한다.$$/수식$$\n" \
              "(ⅰ) $$수식$$a+{a5}`=`1``일``때,``a`=`{c1}$$/수식$$\n" \
              "(ⅱ) $$수식$$a+{a5}`=`{b1}``일``때,``a`=`{c2}$$/수식$$\n" \
              "(ⅲ) $$수식$$a+{a5}`=`{a7}``일``때,``a`=`{c3}$$/수식$$\n" \
              "(ⅰ), (ⅱ), (ⅲ)에서 모든 정수 a의 값의 합은\n" \
              "$$수식$${c1}+({c2})+({c3})`=`{result}$$/수식$$\n\n"

    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(2, 6)
        a4 = np.random.randint(1, 6)
        a5 = a2*a3
        a6 = a2*a4
        a7 = a1+a6

        if(a7 == 4): b1 = 2
        elif(a7 == 9): b1 = 3
        elif(a7 == 25): b1 = 5
        else: b1 = 0

        c1 = 1-a5
        c2 = b1-a5
        c3 = a7-a5

        result = c1+c2+c3

        if (a7 == 4 or a7 == 9 or a7 == 25):
            if(result != 1 or result!= -1 or result!= 0):
                break

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result + 2)
        q3 = "{%s}" % (result + 4)
        q4 = "{%s}" % (result * (-1) + 2)
        q5 = "{%s}" % (result * (-1) + 4)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result - 2)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result + 2)
        q4 = "{%s}" % (result * (-1))
        q5 = "{%s}" % (result * (- 1) + 2)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result + 4)
        q2 = "{%s}" % (result + 2)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result * (-1) -2)
        q5 = "{%s}" % (result * (-1))
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result * (-1) + 2)
        q2 = "{%s}" % (result * (-1))
        q3 = "{%s}" % (result + 2)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result - 2)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result * (-1))
        q2 = "{%s}" % (result * (-1) - 2)
        q3 = "{%s}" % (result + 4)
        q4 = "{%s}" % (result + 2)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, b1=b1, a5=a5, a6=a6, a7=a7, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, b1=b1, result=result, a7=a7, c1=c1,c2=c2, c3=c3)

    return stem, answer, comment


def latterandexpress113_Stem_057():
    stem = "일차방정식 $$수식$${a1}-{a2}(-x+{a3})`=`{a4}x-{a5}$$/수식$$의 해를 $$수식$$x=a$$/수식$$라 할 때\n" \
           "일차방정식 $$수식$$ax-{a6}=0의``해는?$$/수식$$\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${a1}-{a2}(-x+{a3})`=`{a4}x-{a5}에서$$/수식$$\n" \
              "$$수식$${a1}+{a2}x-{b1}`=`{a4}x-{a5},``{a2}x{b2}`=`{a4}x-{a5}$$/수식$$\n" \
              "$$수식$${b3}x={b4}````````THEREFORE~x`=`{b5}$$/수식$$\n" \
              "$$수식$$따라서``a`=`{b5}이므로``ax-{a6}`=`0에``대입하면$$/수식$$\n" \
              "$$수식$${b5}x-{a6}`=`0,``{b5}x`=`{a6}$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{result}$$/수식$$\n\n"

    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 10)
        a4 = np.random.randint(2, 10)
        a4 = np.random.randint(1, 10)
        a5 = np.random.randint(1, 10)
        a6 = np.random.randint(1, 20)

        b1 = a2*a3
        b2 = a1-b1
        b3 = a2-a4
        b4 = a5+b2

        if (b4!=0 and b3!=0 and b4/b3 != 1):
            if(b4>0 and b3>0) or (b4<0 and b3<0):
                if(b4%b3 == 0):
                    if(b1>a1 and b4/b3 < 5):
                        if(a6%(b4/b3)==0):
                            break

    b5 = math.floor(b4/b3)
    result = math.floor(a6/b5)

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (a6)
        q3 = "{%s} over {%s}" % (a6,b5+1)
        q4 = "{%s} over {%s}" % (a6,b5+3)
        q5 = "{%s} over {%s}" % (a6,b5+5)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (a6)
        q2 = "{%s}" % (result)
        q3 = "{%s} over {%s}" % (a6,b5+1)
        q4 = "{%s} over {%s}" % (a6,b5+3)
        q5 = "{%s} over {%s}" % (a6,b5+5)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s} over {%s}" % (a6,b5+1)
        q2 = "{%s} over {%s}" % (a6,b5+3)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (a6)
        q5 = "{%s} over {%s}" % (a6,b5+5)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s} over {%s}" % (a6,b5+1)
        q2 = "{%s} over {%s}" % (a6,b5+3)
        q3 = "{%s} over {%s}" % (a6,b5+5)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (a6)
        answer_num = "④"
    else:
        q1 = "{%s} over {%s}" % (a6,b5+1)
        q2 = "{%s} over {%s}" % (a6,b5+3)
        q3 = "{%s} over {%s}" % (a6,b5+5)
        q4 = "{%s}" % (a6 - result - 1)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, b1=b1, a5=a5, a6=a6, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5, result=result)

    return stem, answer, comment


def latterandexpress113_Stem_058():
    stem = "세 방정식 $$수식$${a1}-LEFT (`{a2}x-(x-{a3})RIGHT )`+{a4}`=`0$$/수식$$\n" \
           "일차방정식 $$수식$$1 over 5`x`-{b1}x`=`-{b2},````x-{c2} over {c1}`-`1 over {c3}`=`{c4}(x-{c5})$$/수식$$\n" \
           "의 해를 차레대로 x=a, x=b, x=c라 할 때, a,b,c의 대소 관계를 바르게 나타낸 것은?\n" \
           "① $$수식$$a`&lt;`c`&lt;`b$$/수식$$\n" \
           "② $$수식$$b`&lt;`a`&lt;`c$$/수식$$\n" \
           "③ $$수식$$b`&lt;`c`&lt;`a$$/수식$$\n" \
           "④ $$수식$$c`&lt;`a`&lt;`b$$/수식$$\n" \
           "⑤ $$수식$$c`&lt;`b`&lt;`a$$/수식$$\n"
    answer = "(정답)\n{result}"
    comment = "(해설)\n" \
              "$$수식$${a1}-`LEFT (`{a2}x-(x-{a3})`RIGHT )+{a4}`=`0에서$$/수식$$\n" \
              "$$수식$${a1}-({a5}x+{a3})+{a4}`=`0,````-{a5}x+{a6}`=`0$$/수식$$\n" \
              "$$수식$$-{a5}x`=`-{a6},````x`=`{a7}````````THEREFORE~a`=`{a7}$$/수식$$\n" \
              "$$수식$$1 over 5`x`-{b1}x`=`-{b2}에서````1 over 5`x`-`{b3} over 5`x`=`-`{b4} over 5$$/수식$$\n" \
              "양변에 5를 곱하면\n" \
              "$$수식$$x-{b3}x`=-{b4},``x`=`{b6}````````THEREFORE~b`=`{b6}$$/수식$$\n" \
              "$$수식$$x-{c2} over {c1}`-`1 over {c3}`=`{c4}(x-{c5})에서$$/수식$$\n" \
              "$$수식$$x-{c2} over {c1}`-`1 over {c3}`=`{c6} over 5`(x-{c5})$$/수식$$\n" \
              "양변에 10을 곱하면\n" \
              "$$수식$${c7}(x-{c2})-{c8}`=`{c9}(x-{c5})$$/수식$$\n" \
              "$$수식$${c7}x-{c10}-{c8}`=`{c9}x-{c11},````x`=`{c12}```````THEREFORE~c`=`{c12}$$/수식$$\n" \
              "따라서 세 수 a,b,c의 대소 관계를 바르게 나타내면 $$수식$${t1} &lt; {t2} &lt; {t3}$$/수식$$       이다\n\n"

    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(2, 10)
        a3 = np.random.randint(1, 10)
        a4 = np.random.randint(2, 10)
        a4 = np.random.randint(1, 10)
        a5 = a2-1
        a6 = a1-a3+a4

        b1 = np.random.randint(1, 10)/10
        b2 = np.random.randint(1, 10)/10
        b3 = math.floor(b1*5)
        b4 = math.floor(b2*5)
        b5 = b3-1

        c1 = [2,5,10][np.random.randint(0,3)]
        c2 = np.random.randint(1,10)
        c3 = [2,5,10][np.random.randint(0,3)]
        c4 = np.random.randint(2,10)/10
        c5 = np.random.randint(1,10)
        c6 = math.floor(c4*5)
        c7 = math.floor(10/c1)
        c8 = math.floor(10/c3)
        c9 = c6*2
        c10 = c2*c7
        c11 = c9*c5

        if (a6!=0 and a5!=0 and b4!=0 and b5!=0 and c7!=c9 and c8+c10-c11!=0):
            if(a6%a5==0 and b4%b5==0 and (c8+c10-c11)%(c7-c9)==0):
                if((c4*10)%2==0 and (b1*10)%2==0 and (b2*10)%2==0):
                    if not(a6/a5 < b4/b5 and b4/b5 < (c8+c10-c11)/(c7-c9)):
                        if(a6/a5 != b4/b5 != (c8+c10-c11)/(c7-c9)):
                            break

    a7 = math.floor(a6/a5)
    b6 = math.floor(b4/b5)
    c12 = math.floor((c8+c10-c11)/(c7-c9))

    if(a7<c12<b6): t1="a"; t2="c"; t3="b"; result="①"
    elif(b6<a7<c12): t1="b"; t2="a"; t3="c"; result="②"
    elif(b6<c12<a7): t1="b"; t2="c"; t3="a"; result="③"
    elif(c12<a7<b6): t1="c"; t2="a"; t3="b"; result="④"
    else: t1="c"; t2="b"; t3="a"; result="⑤"



    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, b1=b1, b2=b2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    answer = answer.format(result=result)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6,a7=a7, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5,b6=b6, result=result,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,c6=c6,c7=c7,c8=c8,c9=c9,c10=c10,c11=c11,c12=c12,t1=t1,t2=t2,t3=t3)

    return stem, answer, comment


def latterandexpress113_Stem_059():
    stem = "두 수 $$수식$$a,``b$$/수식$$에 대하여 $$수식$$a◉b = ab - a + b$$/수식$$로 약속 할 때,\n" \
           "$$수식$$({a1}◉x)◉{a2}`=`{a3}을````만족시키는````x의````값은?$$/수식$$\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${a1}◉x`=`{a1}x-{a1}+x`=`{b1}x-{a1}이므로$$/수식$$\n" \
              "$$수식$$({a1}◉x)◉{a2}`=`({b1}x-{a1})◉{a2}$$/수식$$\n" \
              "$$수식$${a2}({b1}x-{a1})-({b1}x-{a1})+{a2}$$/수식$$\n" \
              "$$수식$${c1}x-{c2}-{b1}x+{c3}`=`{c4}x{k}{c5}$$/수식$$\n" \
              "$$수식$$이때``{c4}x{k}{c5}`=`{a3}이므로``{c4}x={c6}$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{result}$$/수식$$\n\n"

    while True:
        a1 = np.random.randint(1, 10)
        a2 = np.random.randint(1, 10)
        a3 = np.random.randint(1, 20)

        b1 = a1+1

        c1 = a2*b1
        c2 = a1*a2
        c3 = a1+a2
        c4 = c1-b1
        c5 = c3-c2
        c6 = a3-c5
        if(c5<0):
            k=""
        else:
            k="+"

        if (c4!=0 and c6!=0):
            if(c6%c4==0):
                if(c4<11):
                    break

    result = math.floor(c6/c4)

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result+1)
        q3 = "{%s}" % (result+2)
        q4 = "{%s}" % (result+3)
        q5 = "{%s}" % (result+4)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result-1)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result+1)
        q4 = "{%s}" % (result+2)
        q5 = "{%s}" % (result+3)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result-2)
        q2 = "{%s}" % (result-1)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result+1)
        q5 = "{%s}" % (result+2)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result-3)
        q2 = "{%s}" % (result-2)
        q3 = "{%s}" % (result-1)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result+1)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result-4)
        q2 = "{%s}" % (result-3)
        q3 = "{%s}" % (result-2)
        q4 = "{%s}" % (result - 1)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1, a2=a2, a3=a3, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1, a2=a2, a3=a3, b1=b1, result=result, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6,k=k)

    return stem, answer, comment


def latterandexpress113_Stem_060():
    stem = "L중학교에서 올해의 남학생 수는 작년보다 $$수식$${a1}%$$/수식$$ 증가했고, 여학생 수는 작년보다 $$수식$${a2}%$$/수식$$ 감소했다." \
           " 작년의 전체 학생은 $$수식$${a3}$$/수식$$명이고 올해는 작년보다 $$수식$${a4}$$/수식$$명이 감소했다고 할 때, 올해의 여학생 수는?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "작년의 여학생 수를 x라 하면 작년의 남학생 수는 $$수식$${a3}-x$$/수식$$ 이므로\n증가한 남학생 수는 " \
              "$$수식$${a1} over 100`({a3}-x)$$/수식$$\n" \
              "감소한 여학생의 수는 $$수식$${a2} over 100`x$$/수식$$\n" \
              "전체적으로 {a4}명이 감소했으므로\n" \
              "$$수식$${a1} over 100`({a3}-x)-`{a2} over 100`x`=`-{a4}$$/수식$$\n" \
              "$$수식$${b1}-{a1}x-{a2}x`=`-{b2}$$/수식$$\n" \
              "$$수식$$-{b3}x`=`-{b4}````````THEREFORE~x`=`{b5}$$/수식$$\n" \
              "따라서 올해의 여학생 수는\n" \
              "$$수식$${b5}-{b5} TIMES {a2} over 100`=`{b5}`-`{b6}`=`{result}(명)$$/수식$$\n\n"

    while True:
        a1 = np.random.randint(2, 10)
        a2 = np.random.randint(2, 11)
        a3 = np.random.randint(200, 900)
        a4 = np.random.randint(2,20)

        b1 = a1*a3
        b2 = a4*100
        b3 = a1+a2
        b4 = b1+b2

        if(b4!=0 and b3!=0):
            b5 = math.floor(b4/b3)
        else:
            b5 = 0

        b6 = math.floor(b5*a2/100)

        if (b3!=0 and b4!=0):
            if((b5*a2)%100 == 0):
                break

    result = b5-b6

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result+8)
        q3 = "{%s}" % (result+16)
        q4 = "{%s}" % (result+24)
        q5 = "{%s}" % (result+32)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result-8)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result+8)
        q4 = "{%s}" % (result+16)
        q5 = "{%s}" % (result+24)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result-16)
        q2 = "{%s}" % (result-8)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result+8)
        q5 = "{%s}" % (result+16)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result-24)
        q2 = "{%s}" % (result-16)
        q3 = "{%s}" % (result-8)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result+8)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result-32)
        q2 = "{%s}" % (result-24)
        q3 = "{%s}" % (result-16)
        q4 = "{%s}" % (result-8)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, b1=b1, result=result, b2=b2, b3=b3, b4=b4, b5=b5, b6=b6)

    return stem, answer, comment


def latterandexpress113_Stem_061():
    stem = "{p1}는 며칠 동안 여행을 다녀왔는데, 여행기간의 $$수식$$1 over {a1}$$/수식$$ 은 잠을 잤고 $$수식$$1 over {a2}$$/수식$$ 은 차를 탔으며 $$수식$$1 over {a3}$$/수식$$ 은 관광을 했다." \
           "또 식사와 쇼핑 등 나머지 시간을 합하면 $$수식$${a4}$$/수식$$ 시간이라 할 때, $$수식$${p1}$$/수식$$ 는 총 몇 시간 동안 여행했는가?\n" \
           "① $$수식$${q1}$$/수식$$시간\n" \
           "② $$수식$${q2}$$/수식$$시간\n" \
           "③ $$수식$${q3}$$/수식$$시간\n" \
           "④ $$수식$${q4}$$/수식$$시간\n" \
           "⑤ $$수식$${q5}$$/수식$$시간\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${p1}$$/수식$$ 가 x시간 동안 여행했다고 하면\n" \
              "$$수식$$1 over {a1}`x`+`1 over {a2}`x`+`1 over {a3}`x`+{a4}`=`x$$/수식$$\n" \
              "$$수식$${b1} over {b2}`x+`{a4}`=`x,````-`{b3} over {b2}`x`=`-{a4}$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 $$수식$${p1}는``{result}시간``동안``여행했다.$$/수식$$\n\n"

    while True:
        p1 = ["은하","영희", "민지", "미주", "수지"][np.random.randint(0,5)]
        a1 = np.random.randint(2, 10)
        a3 = np.random.randint(2, 10)
        a2 = a1*a3
        a4 = np.random.randint(10,30)

        b1 = a1+a3+1
        b2 = a3*a1
        b3 = a3*a1-(a1+a3+1)

        if (b2!=0 and b3!=0):
            if((a4*b2)%b3 == 0):
                break

    result = math.floor(a4*b2/b3)

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result+4)
        q3 = "{%s}" % (result+8)
        q4 = "{%s}" % (result+12)
        q5 = "{%s}" % (result+16)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result-4)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result+4)
        q4 = "{%s}" % (result+8)
        q5 = "{%s}" % (result+16)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result-8)
        q2 = "{%s}" % (result-4)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result+4)
        q5 = "{%s}" % (result+8)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result-12)
        q2 = "{%s}" % (result-8)
        q3 = "{%s}" % (result-4)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result+4)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result-16)
        q2 = "{%s}" % (result-12)
        q3 = "{%s}" % (result-8)
        q4 = "{%s}" % (result-4)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(p1=p1, a1=a1, a2=a2, a3=a3, a4=a4, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(p1=p1, a1=a1, a2=a2, a3=a3, a4=a4, b1=b1, result=result, b2=b2, b3=b3)

    return stem, answer, comment


def latterandexpress113_Stem_062():
    stem = "$$수식$${a1}%$$/수식$$ 의 소금물 $$수식$${a2}``rm g$$/수식$$ 이 있다. 여기에서 몇 g의 물을 증발시키면 $$수식$${a3}%$$/수식$$ 의 소금물이 되는가?\n" \
           "① $$수식$${q1}``rm g$$/수식$$\n" \
           "② $$수식$${q2}``rm g$$/수식$$\n" \
           "③ $$수식$${q3}``rm g$$/수식$$\n" \
           "④ $$수식$${q4}``rm g$$/수식$$\n" \
           "⑤ $$수식$${q5}``rm g$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "x g의 물을 증발시킨다고 하면 물을 증발시켜도 소금의 양은 변하지 않으므로\n" \
              "$$수식$${a1} over 100` TIMES {a2}`=`{a3} over 100` TIMES ({a2}-x)$$/수식$$\n" \
              "$$수식$${b1}`=`{b2}-{a3}x,````{a3}x`=`{b3}$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 물 $$수식$${result}$$/수식$$ g을 증발시킨다.\n\n"

    while True:
        a1 = np.random.randint(2, 10)
        a2 = np.random.randint(300,900)
        a3 = np.random.randint(2, 10)

        b1 = a1*a2
        b2 = a2*a3
        b3 = b2-b1

        if (a1*a2) % 100 == 0 and (a2*a3) % 100 ==0:
            if(b3 % a3 == 0):
                if(a1!=a3 and a1<a3):
                    break

    result = math.floor(b3/a3)

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result+20)
        q3 = "{%s}" % (result+50)
        q4 = "{%s}" % (result+70)
        q5 = "{%s}" % (result+90)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result-20)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result+30)
        q4 = "{%s}" % (result+50)
        q5 = "{%s}" % (result+80)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result-50)
        q2 = "{%s}" % (result-20)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result+20)
        q5 = "{%s}" % (result+50)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result-80)
        q2 = "{%s}" % (result-60)
        q3 = "{%s}" % (result-30)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result+20)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result-90)
        q2 = "{%s}" % (result-70)
        q3 = "{%s}" % (result-40)
        q4 = "{%s}" % (result-20)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1, a2=a2, a3=a3, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1, a2=a2, a3=a3, b1=b1, result=result, b2=b2, b3=b3)

    return stem, answer, comment


def latterandexpress113_Stem_063():
    stem = "$$수식$${a1}%$$/수식$$ 의 소금물 $$수식$${a2}``rm g$$/수식$$과 $$수식$${a3}%$$/수식$$의 소금물을 섞어 $$수식$${a4}%$$/수식$$" \
           "의 소금물을 만들었다. 이때 $$수식$${a3}%$$/수식$$의 소금물의 양은?\n" \
           "① $$수식$${q1}``rm g$$/수식$$\n" \
           "② $$수식$${q2}``rm g$$/수식$$\n" \
           "③ $$수식$${q3}``rm g$$/수식$$\n" \
           "④ $$수식$${q4}``rm g$$/수식$$\n" \
           "⑤ $$수식$${q5}``rm g$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${a3}$$/수식$$의 소금물의 양을 x g이라 하면\n" \
              "$$수식$${a1} over 100` TIMES ` {a2}`+`{a3} over 100` TIMES`x`=`{a4} over 100`TIMES`({a2}+x)$$/수식$$\n" \
              "$$수식$${b1}`+`{a3}x`=`{b2}+{a4}x$$/수식$$\n" \
              "$$수식$${b33}x`=`{b4}````````THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 $$수식$${a3}%의``소금물은``{result}``rm g이다.$$/수식$$\n\n"

    while True:
        a1 = np.random.randint(3, 10)
        a2 = np.random.randint(3,10)*100
        a3 = np.random.randint(2, 10)
        a4 = np.random.randint(2,10)

        b1 = a1*a2
        b2 = a2*a4
        b3 = a3-a4
        if b3==1: b33=""
        elif b3==-1: b33="-"
        else: b33=b3
        b4 = b2-b1

        if b3!=0 and b4!=0:
            if(b4 % b3 == 0):
                if(a1!=a3 and a1<a4<a3):
                    if(b4/b3 > 400):
                        break

    result = math.floor(b4/b3)

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result+100)
        q3 = "{%s}" % (result+200)
        q4 = "{%s}" % (result+300)
        q5 = "{%s}" % (result+400)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result-100)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result+100)
        q4 = "{%s}" % (result+200)
        q5 = "{%s}" % (result+300)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result-200)
        q2 = "{%s}" % (result-100)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result+100)
        q5 = "{%s}" % (result+200)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result-300)
        q2 = "{%s}" % (result-200)
        q3 = "{%s}" % (result-100)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result+100)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result-400)
        q2 = "{%s}" % (result-300)
        q3 = "{%s}" % (result-200)
        q4 = "{%s}" % (result-100)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1, a2=a2, a3=a3, a4=a4, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, b1=b1, result=result, b2=b2, b33=b33, b4=b4)

    return stem, answer, comment


def latterandexpress113_Stem_064():
    stem = "서로 다른 두 자연수가 있다. 큰 수는 작은 수보다 $$수식$${v3}$$/수식$$만큼 크고, 두 수의 합은 $$수식$${v4}$$/수식$$일 때, 큰 수는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "큰 수를 $$수식$$x$$/수식$$라 하면 작은 수는 $$수식$$x`-`{v3}$$/수식$$이므로\n" \
              "$$수식$$x `+` LEFT ( x `-` {v3} RIGHT ) `=` {v4}$$/수식$$, " \
              "$$수식$$ {v5}x`=`{v6} THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 큰 수는 {result} 이다.\n\n"

    while True:
        v1 = np.random.randint(1,40)
        v2 = np.random.randint(1,40)
        v3 = v1 - v2
        v4 = v1 + v2
        v5 = 2
        v6 = v4 + v3
        result = v6 // v5
        result_mod = v6 % v5
        if v1 > v2 and result_mod == 0:
            break



    idx = np.random.randint(0,5)
    candidates = [] 
    temp = result - 3 * idx

    for i in range(5):
        candidates.append(temp + 3 * i)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(v3=v3,v4=v4,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(v3=v3,v4=v4,v5=v5,v6=v6,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_065():
    stem = "어떤 수에 {v1}을 더해야 할 것을 잘못하여 곱하였더니 구하려고 했던 수보다 {v2}만큼 커졌다고 한다. 어떤 수는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "어떤 수를 $$수식$$ x $$/수식$$라 하면\n" \
              "$$수식$$ {sv1}x `=` LEFT ( x `+` {v1} RIGHT ) `+` {v2}`,` {sv2}x`=`{vv2} THEREFORE~x`=`{result} $$/수식$$, " \
              "따라서 어떤 수는 {result} 이다.\n\n"

    while True:
        v1 = np.random.randint(2,40)
        v2 = np.random.randint(1,40)

        vv1 = v1 - 1
        vv2 = v1 + v2

        result = vv2 // vv1
        result_mod = vv2 % vv1

        if vv1 != 0 and result_mod == 0:
            break

    sv1 = vtos(v1,1,1)
    sv2 = vtos(vv1,1,1)

    idx = np.random.randint(0,5)
    candidates = [] 
    temp = result - 3 * idx

    for i in range(5):
        candidates.append(temp + 3 * i)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(sv1=sv1,v1=v1,v2=v2,sv2=sv2,vv2=vv2,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_066():
    stem = "연속하는 세 {s1}수의 합이 {v1}일 때, 세 {s1}수 중 {s2} 수는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "연속하는 세 {s1}수를 $$수식$${s3_1}, {s3_2}, {s3_3}$$/수식$$ 라 하면\n" \
              "$$수식$$ {s4} `=` {v1} , 3x `=` {v2}$$/수식$$" \
              "$$수식$$ THEREFORE~x`=`{result}$$/수식$$" \
              "따라서 연속하는 세 {s1}수는 {v3_1}, {v3_2}, {v3_3}이므로 {s2} 수는 {result}이다.\n\n"
    
    s1_idx = np.random.randint(2)
    s1 = "%d 의 배" % (s1_idx)
    
    s2_idx = np.random.randint(3)
    s2 = ['가장 작은','중간','가장 큰'][s2_idx]
    
    while True:
        v1 = np.random.randint(100,400)
        m = 2 if s1_idx < 2 else s1_idx
        
        if s2_idx == 0:
            v2 = v1 - 3*m
        elif s2_idx == 1:
            v2 = v1
        else:
            v2 = v1 + 3*m

        result = v2 // 3
        result_mod = v2 % 3
        if s1_idx == 0: # 홀
            s1 = "홀"
            if result % 2 == 1 and result_mod == 0:
                break
        elif s1_idx == 1: # 짝
            s1 = "짝"
            if result % 2 == 0 and result_mod == 0:
                break
        else:
            if result % s1_idx == 0 and result_mod == 0:
                break
    
    s3 = [['x','x+%d'%(m),'x+%d'%(2*m)],
          ['x-%d'%(m),'x','x+%d'%(m)],
          ['x-%d'%(2*m),'x-%d'%(m),'x']][s2_idx]

    s3_1, s3_2, s3_3 = s3
    s4 = [" %s  `+` LEFT ( %s RIGHT ) `+`LEFT ( %s RIGHT )" % (s3_1,s3_2,s3_3),
    "LEFT ( %s RIGHT ) `+`  %s  `+`LEFT ( %s RIGHT )" % (s3_1,s3_2,s3_3),
    "LEFT ( %s RIGHT ) `+` LEFT ( %s RIGHT ) `+` %s" % (s3_1,s3_2,s3_3)][s2_idx]
    v3 = [[result,result+m,result+2*m],
          [result-m,result,result+m],
          [result-2*m,result-m,result]][s2_idx]
    v3_1, v3_2, v3_3 = v3

    idx = np.random.randint(0,5)
    candidates = [] 
    temp = result - 3 * idx

    for i in range(5):
        candidates.append(temp + 3 * i)

    c1, c2, c3, c4, c5 = candidates

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(s1=s1,v1=v1,s2=s2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(v1=v1,v2=v2,s1=s1,s2=s2,s3_1=s3_1,s3_2=s3_2,s3_3=s3_3,s4=s4,result=result,v3_1=v3_1,v3_2=v3_2,v3_3=v3_3)

    return stem, answer, comment


def latterandexpress113_Stem_067():
    stem = "십의 자리의 숫자가 일의 자리의 숫자보다 {v1}만큼 큰 두 자리의 자연수가 있다. 이 자연수는 각 자리의 숫자의 합의 {v2}배보다 {v3}만큼 작다고 할 때, 이 자연수는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "일의 자리의 숫자를 $$수식$$x$$/수식$$라 하면 십의 자리의 숫자는  $$수식$$x`+`{v1}$$/수식$$이므로\n" \
              "$$수식$$ {s1} $$/수식$$\n" \
              "$$수식$$ {s2}.{s3} THEREFORE~x`=`{result1}$$/수식$$\n" \
              "따라서 어떤 수는 {result2} 이다.\n\n"

    while True:
        v1 = np.random.randint(3,10)
        v2 = np.random.randint(3,10)
        v3 = np.random.randint(3,10) 

        vv1 = 10 * v1
        vv2 = 2 * v2
        vv3 = v1 * v2 - v3

        vvv1 = 11 - vv2
        vvv2 = vv3 - vv1
        if vv3 == 0 and vvv1 == 0 and vvv2 == 0:
            continue

        result1 = vvv2 // vvv1
        result1_mod = vvv2 % vvv1

        if result1_mod == 0 and result1 + v1 < 10 and result1 > 0:
            break

    s1 = "10LEFT ( x + {v1} RIGHT ) + x `=` {v2}LEFT ( x `+` {v1} `+` x RIGHT ) - {v3}".format(v1=v1,v2=v2,v3=v3)
    s2 = "11x`+`{vv1}`=` {vv2}x`+`{vv3}".format(vv1=vv1,vv2=vv2,vv3=vv3)
    s3 = "{vvv1}x`=`{vvv2}".format(vvv1=vvv1,vvv2=vvv2)

    while True:
        idx = np.random.randint(0,5)
        candidates = []
        result2 = (result1+v1) * 10 + result1

        res_interval = np.random.randint(10)
        temp = result2 - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 < 100 and c2 < 100 and c3 < 100 and c4 < 100 and c5 < 100:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result2:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(v1=v1,s1=s1,s2=s2,s3=s3,result1=result1,result2=result2)

    return stem, answer, comment


def latterandexpress113_Stem_068():
    stem = "$$수식$$1$$/수식$$개에 $$수식$${v1}$$/수식$$원인 {s1}{j1} $$수식$$1$$/수식$$개에 $$수식$${v2}$$/수식$$원인 {s2}{j2} 합하여 $$수식$${v6}$$/수식$$개를 구입하고 $$수식$${v5}$$/수식$$원을 내었더니 거스름돈을 $$수식$${v8}$$/수식$$원 받았다. 이때 구입한 음료수의 개수는??\n" \
           "① $$수식$${c1}$$/수식$$개\n" \
           "② $$수식$${c2}$$/수식$$개\n" \
           "③ $$수식$${c3}$$/수식$$개\n" \
           "④ $$수식$${c4}$$/수식$$개\n" \
           "⑤ $$수식$${c5}$$/수식$$개\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "{s1}{j1} $$수식$$x$$/수식$$개 구입했다고 하면 " \
              "{s2}{j3} $$수식$$ LEFT ( {v6}`-`x RIGHT )$$/수식$$개 구입했으므로\n" \
              "$$수식$$ {ss1} $$/수식$$\n" \
              "$$수식$$ {ss2} $$/수식$$\n "\
              "{ss3} THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 구입한 {s1}의 수는 {result} 이다.\n\n"
    idx = np.random.randint(0, 4)

    s1 = ["과자","사탕","사과","과자"][idx]
    s2 = ["음료수","초콜릿","배","아이스크림"][idx]
    
    j1 = proc_jo(s1, 2)
    j2 = proc_jo(s2, 1)
    j3 = proc_jo(s1, -1)

    while True:
        v1 = np.random.randint(1,10) * 100
        v2 = np.random.randint(1,10) * 100
        
        v3 = np.random.randint(2,10)
        v4 = np.random.randint(2,10)
        v5 = np.random.randint(5,15) * 1000 # 낸돈

        v6 = v3 + v4
        v7 = v1 * v3 + v2 * v4
        
        v8 = v5 - v7 # 거스름돈
        if v8 <= 0 :
            continue

        vv1 = v6 * v2
        vv2 = v5 - v8

        vvv1 = v1 - v2
        vvv2 = vv2 - vv1
        if vvv1 <= 0 :
            continue
        result = vvv2 // vvv1
        result_mod = vvv2 % vvv1

        if result_mod == 0:
            break

    ss1 = "{v1}x `+` {v2} LEFT ( {v6}`-`x RIGHT ) `=` {v5} `-`{v8}".format(v1=v1,v2=v2,v6=v6,v5=v5,v8=v8)
    ss2 = "{v1}x `+` {vv1} `-` {v2}x `=` {vv2}".format(v1=v1,v2=v2,vv1=vv1,vv2=vv2)
    ss3 = "{vvv1}x`=`{vvv2}".format(vvv1=vvv1,vvv2=vvv2)

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(1,10)
        temp = result - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v5=v5,v6=v6,v8=v8,s1=s1,s2=s2,j1=j1,j2=j2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,j1=j1,j3=j3,v6=v6,ss1=ss1,ss2=ss2,ss3=ss3,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_069():
    stem = "올해 {s1}의 나이는 {s2}의 나이의 {v1}배이다. {v2}년 후에 {s1}의 나이가 {s2}의 나이의 {v3} 배가 될 때, 올해 딸의 나이는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "올해 {s2}의 나이를 $$수식$$x$$/수식$$세라 하면 {s1}의 나이는 $$수식$${v1}x$$/수식$$세이므로\n" \
              "$$수식$$ {ss1} $$/수식$$\n" \
              "$$수식$$ {ss2} $$/수식$$\n "\
              "{ss3} THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 올해 {s2}의 나이는 {result}세이다.\n\n"
    
    idx = np.random.randint(0, 4)

    s1 = ["어머니","아버지","어머니","아버지"][idx]
    s2 = ["딸","딸","아들","아들"][idx]
    
    while True:
        v1 = np.random.randint(2,10)
        v2 = np.random.randint(10,20)
        v3 = np.random.randint(2,10)
        
        vv1 = v3 * v2

        vvv1 = v1 - v3
        vvv2 = vv1 - v2

        if vvv1 <= 0 or vvv2 <= 0 :
            continue

        result = vvv2 // vvv1
        result_mod = vvv2 % vvv1

        if result_mod == 0 and result < 100:
            break

    ss1 = "{v1}x`+`{v2}`=`{v3} LEFT ( x `+` {v2} RIGHT )".format(v1=v1,v2=v2,v3=v3)
    ss2 = "{v1}x`+`{v2}`=`{v3}x `+` {vv1}".format(v1=v1,v2=v2,v3=v3,vv1=vv1)
    ss3 = "{vvv1}x`=`{vvv2}".format(vvv1=vvv1,vvv2=vvv2)

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(1,10)
        temp = result - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,s1=s1,s2=s2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,v1=v1,ss1=ss1,ss2=ss2,ss3=ss3,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_070():
    stem = "현재 {s1}와 {s2}의 통장에는 각각 {v1}원, {v2}원이 예금되어 있다. {s1}는 매일 {v3}원씩, {s2}는 매일 {v4}원씩 각자 자신의 통장에서 돈을 찾아 쓰면 며칠 후에 {s1}와 {s2}의 예금액이 같아지는가?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$$x$$/수식$$일 후에 {s1}와 {s2}의 예금액이 같아진다고 하면\n" \
              "$$수식$$ {ss1} $$/수식$$\n" \
              "$$수식$${ss2} THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 {result}일 후에 {s1}와 {s2}의 예금액이 같아진다.\n\n"
    
    idx = np.random.randint(7)

    s1 = ["철수","영수","지후","준우","현우","우주","민규"][idx]
    s2 = ["시아","지유","서아","채아","수아","지우","윤서"][idx]
    
    while True:
        v1 = np.random.randint(10,100) * 1000
        v2 = np.random.randint(10,100) * 1000
        v3 = np.random.randint(1,50) * 100
        v4 = np.random.randint(1,50) * 100
        
        if v1 <= v3 or v2 <= v4 :
            continue

        vv1 = v4 - v3
        vv2 = v2 - v1

        if vv1 <= 0 or vv2 <= 0 :
            continue

        result = vv2 // vv1
        result_mod = vv2 % vv1

        if result_mod == 0:
            break

    ss1 = "{v1} `-` {v3}x `=` {v2} `-` {v4}x".format(v1=v1,v2=v2,v3=v3,v4=v4)
    ss2 = "{vv1}x `=` {vv2}".format(vv1=vv1,vv2=vv2)

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(1,10)
        temp = result - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,v4=v4,s1=s1,s2=s2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,ss1=ss1,ss2=ss2,result=result)

    return stem, answer, comment

def latterandexpress113_Stem_071():
    stem = "원가가 $$수식$${a1}$$/수식$$ 원인 어떤 물건이 있다. 이 물건을 정가의 $$수식$${a2}%$$/수식$$  를" \
           " 할인하여 팔았더니 원가에 대하여 $$수식$${a3}%$$/수식$$의 이익을 얻었다고 한다. 이 물건은 원가에 몇 % 이익을 붙여서 정가를 정한 것인가?\n" \
           "① $$수식$${q1}%`$$/수식$$\n" \
           "② $$수식$${q2}%`$$/수식$$\n" \
           "③ $$수식$${q3}%`$$/수식$$\n" \
           "④ $$수식$${q4}%`$$/수식$$\n" \
           "⑤ $$수식$${q5}%`$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "원가에 x%의 이익을 붙여서 정가를 정했다고 하면\n" \
              "(정가) = $$수식$${a1}`+`{a1} TIMES `x over 100`=`{a1}+{b1}x``(원)$$/수식$$\n" \
              "(판매 가격) = $$수식$$({a1}+{b1}x)-({a1}+{b1}x)`TIMES`{a2} over 100$$/수식$$\n" \
              "= $$수식$${a1}+{b1}x-{b2}-{b3}x$$/수식$$\n" \
              "= $$수식$${b4}+{b5}x``(원)$$/수식$$\n" \
              "(이익) = $$수식$${a1}`TIMES`{a3} over 100`=`{b6}``(원)$$/수식$$\n" \
              "이 때 (판매 가격)-(원가)=(이익)이므로\n" \
              "$$수식$$({b4}+{b5}x)-{a1}`=`{b6},``{b5}x`=`{b7}$$/수식$$\n" \
              "$$수식$$THEREFORE~ x`=`{result}$$/수식$$\n" \
              "따라서 원가에 $$수식$${result}%`$$/수식$$의 이익을 붙여서 정가를 정하였다.\n\n"

    while True:
        a1 = np.random.randint(2, 10) *1000
        a2 = np.random.randint(2,4)*10
        a3 = np.random.randint(2,20)

        b1 = math.floor(a1/100)
        b2 = math.floor(a1*a2/100)
        b3 = math.floor(b1*a2/100)
        b4 = a1-b2
        b5 = b1-b3
        b6 = math.floor(a1*a3/100)
        b7 = b6+a1-b4

        if b5!=0 and b7!=0:
            if(b7 % b5 == 0):
                break

    result = math.floor(b7/b5)

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result+5)
        q3 = "{%s}" % (result+10)
        q4 = "{%s}" % (result+15)
        q5 = "{%s}" % (result+20)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result-5)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result+5)
        q4 = "{%s}" % (result+10)
        q5 = "{%s}" % (result+15)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result-10)
        q2 = "{%s}" % (result-5)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result+5)
        q5 = "{%s}" % (result+10)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result-15)
        q2 = "{%s}" % (result-10)
        q3 = "{%s}" % (result-5)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result+5)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result-20)
        q2 = "{%s}" % (result-15)
        q3 = "{%s}" % (result-10)
        q4 = "{%s}" % (result-5)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1, a2=a2, a3=a3, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1, a2=a2, a3=a3, b1=b1, result=result, b2=b2, b3=b3, b4=b4, b5=b5, b6=b6, b7=b7)

    return stem, answer, comment

def latterandexpress113_Stem_072():
    stem = "길이가 {v1}인 철사를 구부려 가로의 길이와 세로의 길이의 비가 $$수식$${v2}:{v3}$$/수식$$인 직사각형을 만들려고 한다. 이 직사각형의 가로의 길이는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "직사각형의 세로의 길이를 $$수식$${v3} x rm cm$$/수식$$라 하면 가로의 길이는 $$수식$$ {v2} x rm cm$$/수식$$이므로\n" \
              "$$수식$${s1}$$/수식$$\n" \
              "$$수식$${s2}$$/수식$$\n" \
              "따라서 직사각형의 세로의 길이가 $$수식$${result3}``rm cm $$/수식$$이므로 가로의 길이는 \n" \
              "$$수식$${result1}`TIMES`{v2}`=`{result2}$$/수식$$\n\n"
    
    while True:
        v1 = np.random.randint(100,300) 
        v2 = np.random.randint(1,10) 
        v3 = np.random.randint(1,10) 
        
        vv1 = 2 * v2 + 2 * v3
        
        result1 = v1 // vv1
        result1_mod = v1 % vv1
        if result1_mod == 0 :
            break
    result2 = result1 * v2
    result3 = result1 * v3
    s1 = "2 LEFT ( {v2}x `+` {v3}x RIGHT ) `=` {v1} ".format(v1=v1,v2=v2,v3=v3)
    s2 = "{vv1}x `=` {v1}".format(vv1=vv1,v1=v1)

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(1,10)
        temp = result2 - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result2:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(v3=v3,v2=v2,s1=s1,s2=s2,result1=result1,result2=result2,result3=result3)

    return stem, answer, comment

def latterandexpress113_Stem_073():
    stem = "{s1}이네 중학교의 작년의 학생 수는 {v1}명이었다. 올해는 작년에 비하여 남학생은 {v2}명 {s2}하고, 여학생은 {v3}% {s3}하여 전체적으로 {v4}% {s4}하였다. 올해의 여학생 수는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "작년의 여학생 수를 $$수식$$x$$/수식$$명이라 하면\n" \
              "$$수식$${ss1}$$/수식$$\n" \
              "$$수식$${ss2}$$/수식$$\n" \
              "$$수식$${ss3} THEREFORE~x`=`{result1}$$/수식$$\n" \
              "$$수식$${ss4}(명)$$/수식$$\n\n"
    
    idx = np.random.randint(7)

    s1 = ["수연","지안","서윤","하린","하은","서연","서현"][idx]


    while True:
        s2 = ['증가','감소'][np.random.randint(2)]
        s3 = ['증가','감소'][np.random.randint(2)]
        s4 = ['증가','감소'][np.random.randint(2)]

        v1 = np.random.randint(100,1000)
        v2 = np.random.randint(2,50) 
        v3 = np.random.randint(2,100) 
        v4 = np.random.randint(2,100) 

        vv2 = v2 if s2 == '증가' else -1*v2
        vv3 = v3 if s3 == '증가' else -1*v3
        vv4 = v4 if s4 == '증가' else -1*v4
        

        vvv1 = vv2 * 100
        vvv2 = vv4 * v1
        
        vvvv1 = vvv2 - vvv1

        if vvvv1 == 0:
            continue

        result1 = vvvv1 // vv3
        result1_mod = vvvv1 % vv3
        result2 = result1*(1 + vv3 / 100)
        if result1_mod == 0 and result1 > 0 and result2 > 0 and result2 == int(result2) and v1 > result1:
            break
        
    result2 = int(result2)
    sv3 = vtos3(vv3,100)
    sv4 = vtos3(vv4,100,1)

    ss1 = "{vv2} {sv3}x `=`{sv4}`TIMES`{v1}".format(v1=v1,vv2=vv2,sv3=sv3,sv4=sv4)
    ss2 = "{vvv1}`+`{vv3}x `=` {vvv2}".format(vvv1=vvv1,vv3=vv3,vvv2=vvv2)
    ss3 = "{vv3}x `=` {vvvv1}".format(vv3=vv3,vvvv1=vvvv1)
    ss4 = "{result1}LEFT ( 1 {sv3} RIGHT ) `=` {result2}".format(sv3=sv3,result1=result1,result2=result2)

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(1,10)
        temp = result2 - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result2:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,v4=v4,s1=s1,s2=s2,s3=s3,s4=s4,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(ss1=ss1,ss2=ss2,ss3=ss3,ss4=ss4,result1=result1)

    return stem, answer, comment

def latterandexpress113_Stem_074():
    stem = "다음은 조선 후기의 수학자 이명철이 쓴 책 '산학통편'에 실려 있는 문제이다. 손님의 수를" \
           " x명, 방의 수를 y개라 할 때, x-y의 값은?\n" \
           "$$표$$이 씨가 경영하는 여관에 손님이 밀려왔다. 한 방에 $$수식$${a1}$$/수식$$명씩 들어가면 $$수식$${a2}$$/수식$$명이 남는다." \
           " 그런데 한 방에 $$수식$${a3}$$/수식$$명씩 들어가면 방이 하나 남고, 다른 방에는 모두 $$수식$${a3}$$/수식$$명씩 꽉 찬다.$$/표$$\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${a1}y`+`{a2}`=`{a3}(y-1),``{a1}y`+`{a2}`=`{a3}y`-`{a3}$$/수식$$\n" \
              "$$수식$${b1}y`=`{b2}````````THEREFORE~y`=`{b3}$$/수식$$\n" \
              "$$수식$$x`=`{a1} TIMES {b3}`+`{a2}`=`{b4}$$/수식$$\n" \
              "$$수식$$THEREFORE~x-y`=`{b4}-{b3}={result}$$/수식$$\n\n"

    while True:
        a1 = np.random.randint(5, 9)
        a2 = np.random.randint(1,a1)
        a3 = np.random.randint(a1+1,10)

        b1 = a1-a3
        b2 = (-1)*a3-a2
        if(b1!=0 and b2!=0): b3=math.floor(b2/b1)
        else: b3 = 0
        b4 = a1*b3+a2
        result = b4-b3

        if b1!=0 and b2!=0:
            if(b2 % b1 == 0):
                if(b3>0 and b4>0):
                    break


    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result+5)
        q3 = "{%s}" % (result+10)
        q4 = "{%s}" % (result+15)
        q5 = "{%s}" % (result+20)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result-5)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result+5)
        q4 = "{%s}" % (result+10)
        q5 = "{%s}" % (result+15)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result-10)
        q2 = "{%s}" % (result-5)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result+5)
        q5 = "{%s}" % (result+10)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result-15)
        q2 = "{%s}" % (result-10)
        q3 = "{%s}" % (result-5)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result+5)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result-20)
        q2 = "{%s}" % (result-15)
        q3 = "{%s}" % (result-10)
        q4 = "{%s}" % (result-5)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1, a2=a2, a3=a3, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1, a2=a2, a3=a3, b1=b1, result=result, b2=b2, b3=b3, b4=b4)

    return stem, answer, comment


def latterandexpress113_Stem_075():
    stem = "{s1}이가 책 한 권을 모두 읽는 데 {v1}일이 걸렸다. 첫째 날에는 전체의 $$수식$${sv1}$$/수식$$을, 둘째 날에는 남은 부분의 $$수식$${sv2}$$/수식$$을, 셋째 날에는 {v4}쪽을 읽었다고 할 때, 둘째 날 읽은 쪽수는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "작년의 여학생 수를 $$수식$$x$$/수식$$명이라 하면\n" \
              "$$수식$${ss1}$$/수식$$\n" \
              "$$수식$${ss2}$$/수식$$\n" \
              "$$수식$${ss3} THEREFORE~x`=`{result1}$$/수식$$\n" \
              "따라서 둘째 날 읽은 쪽수는\n" \
              "$$수식$${ss4}$$/수식$$\n\n"
    
    idx = np.random.randint(7)

    s1 = ["태현","성준","지혁","민성","현진","재민","태윤"][idx]

    while True:
        v1 = 3
        v2 = np.random.randint(2,10) 
        v3 = np.random.randint(2,10) 
        v4 = np.random.randint(2,100) 

        vv1_1 = fraction_cal_m(1,1,1,v2)
        vv1_2 = fraction_cal_t(vv1_1[0],vv1_1[1],1,v3)

        vvv1_1 = fraction_cal_p(1,v2,vv1_2[0],vv1_2[1])
        vvv1_2 = fraction_cal_m(vvv1_1[0],vvv1_1[1],1,1)
        vvv2 = -1* v4
        
        result1 = vvv2 * vvv1_2[1] // vvv1_2[0]
        result1_mod = vvv2 * vvv1_2[1] % vvv1_2[0]

        result2 = result1 * vv1_2[0] // vv1_2[1]
        result2_mod = result1 * vv1_2[0] % vv1_2[1]

        if result1_mod == 0 and result2_mod == 0:
            break

    sv1 = vtos3(1,v2,1)
    sv2 = vtos3(1,v3,1) 

    ss1 = "{sv1}`+`LEFT ( x `-` {sv1} x RIGHT ) `TIMES` {sv2} `+` {v4}`=`x ".format(sv1=sv1,sv2=sv2,v4=v4)

    svv1 = vtos3(vv1_2[0],vv1_2[1],1)

    ss2 = "{sv1}x`+`{svv1}x`+`{v4}`=`x".format(sv1=sv1,svv1=svv1,v4=v4)

    svvv1 = vtos3(vvv1_2[0],vvv1_2[1])

    ss3 = "{svvv1}x `=` {vvv2}".format(svvv1=svvv1,vvv2=vvv2)
    ss4 = "{svv1}x `=` {svv1}`TIMES`{result1}`=`{result2}".format(svv1=svv1,result1=result1,result2=result2)



    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(1,10)
        temp = result2 - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result2:
            correct_idx = i
            break

    stem = stem.format(s1=s1,v1=v1,sv1=sv1,sv2=sv2,v4=v4,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(ss1=ss1,ss2=ss2,ss3=ss3,ss4=ss4,result1=result1)

    return stem, answer, comment


def latterandexpress113_Stem_076():
    stem = "{s1}이가 공원을 두 바퀴 도는데 처음 한 바퀴는 분속 $$수식$${v1}``rm m$$/수식$$로 걷고, 다음 한 바퀴는 분속 $$수식$${v2}``rm m$$/수식$$로 걸었더니 모두 $$수식$${v3}$$/수식$$분이 걸렸다. 이때 공원 한 바퀴의 거리는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "공원 한 바퀴의 $$수식$$x$$/수식$$ 거리를 라 하면\n" \
              "$$수식$${ss1}$$/수식$$\n" \
              "$$수식$${ss2}$$/수식$$\n" \
              "$$수식$${ss3} THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 공원 한 바퀴의 거리는 $$수식$${result}``rm m $$/수식$$이다.\n\n"
    
    idx = np.random.randint(7)

    s1 = ["수연","지안","서윤","하린","하은","서연","서현"][idx]


    while True:
        v1 = np.random.randint(10,100)
        v2 = np.random.randint(10,100)
        v3 = np.random.randint(10,100)
        v4 = lcm(v1,v2)

        vv1 = v4 // v1
        vv2 = v4 // v2
        vv3 = v4 * v3


        vvv1 = vv1 + vv2
        
        result = vv3 // vvv1
        result_mod = vv3 % vvv1
        if result_mod == 0:
            break

    svv1 = vtos(vv1,1,1)
    svv2 = vtos(vv2,1)
    svvv1 = vtos(vvv1,1,1)

    ss1 = "x over {v1} `+` x over {v2} `=` {v3}".format(v1=v1,v2=v2,v3=v3)
    ss2 = "{svv1}x {svv2}x `=` {vv3}".format(svv1=svv1,svv2=svv2,vv3=vv3)
    ss3 = "{svvv1}x `=` {vv3}".format(vv3=vv3,svvv1=svvv1)

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(5,15) * 10
        temp = result - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,s1=s1,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(ss1=ss1,ss2=ss2,ss3=ss3,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_077():
    stem = "{s1}이가 집에서 공연장까지 가는데 시속 $$수식$${v1}``rm km $$/수식$$로 걸어서 가면 공연 시각보다 $$수식$${v2}$$/수식$$분 늦고, 시속 $$수식$${v3}``rm km $$/수식$$로 뛰어서 가면 공연 시각보다 $$수식$${v4}$$/수식$$분 일찍 도착한다고 한다. 이때 집에서 공연장까지의 거리는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "집에서 공연장까지의 $$수식$$x$$/수식$$거리를 라 하면\n" \
              "$$수식$$(시속 $$수식$$ {v1}``rm km $$/수식$$로 가는 데 걸린 시간)$$/수식$$\n" \
              "$$수식$$ - (시속 $$수식$$ {v3}``rm km $$/수식$$로 가는 데 걸린 시간)$$/수식$$\n" \
              "$$수식$$`=`{vv1} over 60 (시간)$$/수식$$\n" \
              "이므로 $$수식$${ss1}, ````{ss2}$$/수식$$\n" \
              "양변에 {vvvv1}를 곱하면\n" \
              "$$수식$${ss3} ````````````````````THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 집에서 공연장까지의 거리는 $$수식$${result}``rm km $$/수식$$이다.\n\n"
    
    idx = np.random.randint(7)

    s1 = ["태현","성준","지혁","민성","현진","재민","태윤"][idx]


    while True:
        v1 = np.random.randint(1,10)
        v2 = np.random.randint(1,60)
        v3 = np.random.randint(1,10)
        v4 = np.random.randint(1,60)

        vv1 = v2 + v4
        vvv1 = divUpDown(vv1,60)
        if vvv1[1] == 0:
            continue
        vvvv1 = lcm(v1,lcm(v3,vvv1[1]))
        vvvv2 = vvvv1 // v1
        vvvv3 = vvvv1 // v3
        vvvv4 = vvvv1 * vvv1[0] // vvv1[1]
        if vvvv2 - vvvv3 < 1:
            continue
        result = vvvv4 // (vvvv2 - vvvv3)
        result_mod = vvvv4 % (vvvv2 - vvvv3)
        if result_mod == 0:
            break

    ss1 = "x over {v1} `+` x over {v3} `=` {vv1} over 60 ".format(v1=v1,v3=v3,vv1=vv1)
    ss2 = "x over {v1} `+` x over {v3} `=` {vvv1_1} over {vvv1_2} ".format(v1=v1,v3=v3,vvv1_1=vvv1[0],vvv1_2=vvv1[1])
    svvvv2 = vtos(vvvv2,1,1)
    svvvv3 = vtos(vvvv3*(-1),1)
    ss3 = "{svvvv2}x {svvvv3}x `=` {vvvv4}".format(vvvv4=vvvv4,svvvv3=svvvv3,svvvv2=svvvv2)

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(1,4) 
        temp = result - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,v4=v4,s1=s1,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(v1=v1,v2=v2,v3=v3,vvvv1=vvvv1,vv1=vv1,ss1=ss1,ss2=ss2,ss3=ss3,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_078():
    stem = "동생이 집에서 출발한 지 $$수식$${v1}$$/수식$$분 후에 형이 동생을 따라 나섰다. 동생은 매분 $$수식$${v2}``rm m$$/수식$$의 속력으로 걷고, 형은 매분 $$수식$${v3}``rm m $$/수식$$의 속력으로 자전거를 타고 따라 간다고 할 때, 집에서 형과 동생이 만나는 지점까지의 거리는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "형이 집에서 출발한 지 $$수식$$x$$/수식$$분 후에 동생을 만난다고 하면\n" \
              "$$수식$${s1}`,` {s2}$$/수식$$\n" \
              "$$수식$${s3} THEREFORE~x`=`{result1}$$/수식$$\n" \
              "따라서 형이 집에서 출발한 지 {result1}분 후에 형과 동생이 만나므로 집에서 형과 동생이 만나는 지점까지의 거리는\n" \
              "$$수식$${v3} `TIMES` {result1} `=` {result2}``rm (m)$$/수식$$\n\n"
    
    while True:
        v1 = np.random.randint(1,15) 
        v2 = np.random.randint(1,30) * 10
        v3 = np.random.randint(1,30) * 10
        
        vv1 = v1 * v2
        vv2 = v3 - v2
        if vv2 < 100 :
            continue
        result1 = vv1 // vv2
        result1_mod = vv1 % vv2
        if result1_mod == 0 :
            break

    result2 = result1 * v3

    s1 = "{v2} LEFT ( {v1} `+` x RIGHT ) `=` {v3} x".format(v1=v1,v2=v2,v3=v3)
    s2 = "{vv1} `+` {v2}x  `=` {v3} x".format(vv1=vv1,v2=v2,v3=v3)
    s3 = "{vv2}x  `=` {vv1}".format(vv1=vv1,vv2=vv2)

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(5,15) * 10
        temp = result2 - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result2:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,s3=s3,v3=v3,result1=result1,result2=result2)

    return stem, answer, comment


def latterandexpress113_Stem_079():
    stem = "둘레의 길이가 $$수식$${v1}``rm km$$/수식$$인 성의 둘레를 {s1}와 {s2}가 같은 지점에서 출발하여 서로 반대 방향으로 자전거를 타고 가려고 한다. {s1}가 시속 $$수식$${v2}``rm km$$/수식$$로 출발한 지 $$수식$${v3}$$/수식$$분 후에 {s2}가 시속 $$수식$${v4}``rm km$$/수식$$로 출발하였다면 두 사람은 {s1}가 출발한 지 몇 분 후에 처음으로 만나는가?\n" \
           "① $$수식$${c1}분$$/수식$$\n" \
           "② $$수식$${c2}분$$/수식$$\n" \
           "③ $$수식$${c3}분$$/수식$$\n" \
           "④ $$수식$${c4}분$$/수식$$\n" \
           "⑤ $$수식$${c5}분$$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "{s1}가 출발한 지 $$수식$$x$$/수식$$시간 후에 두 사람이 만난다고 하면\n" \
              "$$수식$$({s1}가 $$수식$$x$$/수식$$시간 동안 이동한 거리)$$/수식$$\n" \
              "$$수식$$({s2}가 $$수식$$LEFT ( x `-` {v3} over 60 RIGHT )$$/수식$$시간 동안 이동한 거리)$$/수식$$\n" \
              "=(성의 둘레의 길이)\n" \
              "이므로 $$수식$${ss1}$$/수식$$\n" \
              "$$수식$${ss2}, {ss3}$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{result1_1} over {result1_2}$$/수식$$\n" \
              "따라서 두 사람은 {s1}가 출발한 지 $$수식$${result1_1} over {result1_2}$$/수식$$시간 후, 즉 {result2}분 후에 처음으로 만난다.\n\n"
    
    idx = np.random.randint(7)

    s1 = ["철수","영수","지후","준우","현우","우주","민규"][idx]
    s2 = ["시아","지유","서아","채아","수아","지우","윤서"][idx]
    

    while True:
        v1 = np.random.randint(10,50)
        v2 = np.random.randint(1,20)
        v3 = np.random.randint(1,60)
        v4 = np.random.randint(1,20)

        vv1 = divUpDown(v3*v4,60)
        vv1_1 = vv1[0]
        vv1_2 = vv1[1]
        if vv1[1] == 0:
            continue
        vvv1 = v2 + v4
        vvv2 = fraction_cal_p(v1,1,vv1_1,vv1_2)
        vvv2_1 = vvv2[0]
        vvv2_2 = vvv2[1]
        if vvv2[1] == 0:
            continue
        
        vvvv1 = fraction_cal_t(1,vvv1,vvv2[0],vvv2[1])
        vvvv2 = 60 // vvvv1[1]
        vvvv2_mod = 60 % vvvv1[1]

        if vvvv2_mod == 0:
            break

    result1_1 = vvvv1[0]*vvvv2
    result1_2 = vvvv1[1]*vvvv2
    result2 = result1_1

    ss1 = "{v2}x `+` {v4} LEFT ( x `-` {v3} over 60 RIGHT ) `=` {v1} ".format(v1=v1,v2=v2,v3=v3,v4=v4)

    ss2 = " {v2}x `+` {v4}x `-` {vv1_1} over {vv1_2} `=` {v1} ".format(v2=v2,v4=v4,vv1_1=vv1_1,vv1_2=vv1_2,v1=v1)

    ss3 = "{vvv1}x `=` {vvv2_1} over {vvv2_2}".format(vvv1=vvv1,vvv2_1=vvv2_1,vvv2_2=vvv2_2)
    

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(1,4) 
        temp = result2 - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result2:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,v4=v4,s1=s1,s2=s2,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,v3=v3,vv1_1=vv1_1,vv1_2=vv1_2,ss1=ss1,ss2=ss2,ss3=ss3,result1_1=result1_1,result1_2=result1_2,result2=result2)

    return stem, answer, comment


def latterandexpress113_Stem_080():
    stem = "일정한 속력으로 달리는 열차가 $$수식$${v1}``rm m $$/수식$$ 길이의 터널을 완전히 통과하는 데 $$수식$${v2}$$/수식$$초가 걸렸고,  $$수식$${v3}$$/수식$$길이의 터널을 완전히 통과하는 데 $$수식$${v4}$$/수식$$초가 걸렸다. 이때 열차의 속력은?\n" \
           "① $$수식$$초속`{c1}``rm m $$/수식$$\n" \
           "② $$수식$$초속`{c2}``rm m $$/수식$$\n" \
           "③ $$수식$$초속`{c3}``rm m $$/수식$$\n" \
           "④ $$수식$$초속`{c4}``rm m $$/수식$$\n" \
           "⑤ $$수식$$초속`{c5}``rm m $$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "열차의 길이를 $$수식$$x$$/수식$$라 하면\n" \
              "$$수식$${ss1} `,` {ss2}$$/수식$$\n" \
              "$$수식$${ss3} `,` {ss4}$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{result1}$$/수식$$\n" \
              "따라서 열차의 길이가 $$수식$${result1}``rm m$$/수식$$이므로 열차의 속력은 $$수식$${ss1_3} over {v4} `=` {result2}$$/수식$$시에서 초속 $$수식$${result2}``rm m$$/수식$$이다.\n\n"


    while True:
        v1 = np.random.randint(10,90) * 10
        v2 = np.random.randint(10,60)
        v3 = np.random.randint(10,90) * 10
        v4 = np.random.randint(10,60)
        if v2 == v4:
            continue
        v5 = lcm(v2,v4)

        vv1 = v5 // v2
        vv2 = v5 // v4

        vvv1 = vv1 * v1
        vvv2 = vv2 * v3

        vvvv1 = vv1 - vv2
        vvvv2 = vvv2 - vvv1

        if vvvv1 == 0 or vvvv2 == 0:
            continue
    
        result1 = vvvv2 // vvvv1
        result1_mod = vvvv2 % vvvv1

        result2 = (v3 + result1) // v4
        result2_mod = (v3 + result1) % v4
        if result1_mod == 0 and result2_mod == 0 and result1 > 0 and result2 > 0:
            break
    

    ss1_1 = "{%d `+` x}" % (v1)
    ss1_2 = "{%d `+` x}" % (v3)
    ss1_3 = "{%d `+` %d}" % (v3,result1)
    ss1 = "{ss1_1} over {v2} `=` {ss1_2} over {v4}".format(ss1_1=ss1_1,ss1_2=ss1_2,v2=v2,v4=v4)

    if v5 == v2:
        ss2 = "{v1} `+` x `=`{vv2} LEFT ( {v3} `+` x RIGHT )".format(v1=v1,vv2=vv2,v3=v3)
        
    elif v5 == v4:
        ss2 = "{vv1} LEFT ( {v1} `+` x RIGHT ) `=` {v3} `+` x ".format(v1=v1,vv1=vv1,v3=v3)
    else:
        ss2 = "{vv1} LEFT ( {v1} `+` x RIGHT ) `=` {vv2}LEFT ( {v3} `+` x RIGHT ) ".format(v1=v1,vv1=vv1,vv2=vv2,v3=v3)

    if v5 == v2:
        ss3 = "{v1} `+` x `=`{vvv2} `+` {vv2}x ".format(v1=v1,vvv2=vvv2,vv2=vv2)
    elif v5 == v4:
        ss3 = "{vvv1} `+` {vv1} x `=` {v3} `+` x ".format(vvv1=vvv1,vv1=vv1,v3=v3)
    else:
        ss3 = "{vvv1} `+` {vv1} x  `=` {vvv2} `+` {vv2}x ".format(vvv1=vvv1,vv1=vv1,vvv2=vvv2,vv2=vv2)


    ss4 = "{vvvv1}x `=` {vvvv2}".format(vvvv1=vvvv1,vvvv2=vvvv2)
    

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(2,10) * 5 
        temp = result2 - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result2:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,v4=v4,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(ss1=ss1,ss2=ss2,ss3=ss3,ss4=ss4,result1=result1,ss1_3=ss1_3,v4=v4,result2=result2)

    return stem, answer, comment


def latterandexpress113_Stem_081():
    stem = "$$수식$$ {v1}`% $$/수식$$의 소금물을 만들려다가 물을 너무 많이 넣어서 $$수식$$ {v2}`% $$/수식$$의 소금물 $$수식$$ {v3}` rm g $$/수식$$을 만들었다. 다시 $$수식$$ {v1}`% $$/수식$$의 소금물을 만들기 위해서는 소금을 몇  $$수식$$rm g$$/수식$$더 넣어야 하는가?\n" \
           "① $$수식$${c1}`rm g $$/수식$$\n" \
           "② $$수식$${c2}`rm g $$/수식$$\n" \
           "③ $$수식$${c3}`rm g $$/수식$$\n" \
           "④ $$수식$${c4}`rm g $$/수식$$\n" \
           "⑤ $$수식$${c5}`rm g $$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$${v2}`%$$/수식$$의 소금물 $$수식$${v3}`rm g$$/수식$$에 들어 있는 소금의 양은\n" \
              "$$수식$${ss1}$$/수식$$\n" \
              "이므로 소금 $$수식$$x`rm g$$/수식$$을 더 넣는다고 하면\n" \
              "$$수식$${ss2}$$/수식$$\n" \
              "$$수식$${ss3}$$/수식$$\n" \
              "$$수식$${ss4} THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 소금을 $$수식$${result}`rm g$$/수식$$을 더 넣어야 한다.\n\n"


    while True:
        v1 = np.random.randint(1,50)
        v2 = np.random.randint(1,50)
        v3 = np.random.randint(10,500)

        if v1 <= v2:
            continue

        vv1 = (v2 * v3) // 100
        vv1_mod = (v2 * v3) % 100
        if vv1_mod != 0:
            continue
        vvv1 = vv1 * 100
        vvv2 = v1 * v3

        vvvv1 = 100 - v1
        vvvv2 = vvv2 - vvv1

        if vvvv1 == 0 or vvvv2 == 0:
            continue
    
        result = vvvv2 // vvvv1
        result_mod = vvvv2 % vvvv1

        if result_mod == 0 and result > 0:
            break
    
    ss1 = "{v2} over 100 `TIMES` {v3}".format(v2=v2,v3=v3)

    ss2 = "{vv1} `+` x `=` {v1} over 100 LEFT ( {v3} `+` x RIGHT )".format(vv1=vv1,v1=v1,v3=v3)

    ss3 = "{vvv1} `+` 100x `=` {vvv2} `+` {v1}x".format(vvv1=vvv1,vvv2=vvv2,v1=v1)

    ss4 = "{vvvv1}x `=` {vvvv2}".format(vvvv1=vvvv1,vvvv2=vvvv2)
    

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(2,10) * 5 
        temp = result - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(v2=v2,v3=v3,ss1=ss1,ss2=ss2,ss3=ss3,ss4=ss4,result=result)

    return stem, answer, comment



def latterandexpress113_Stem_082():
    stem = "농도가 $$수식$$ {v1}`% $$/수식$$인 소금물과 농도가 $$수식$$ {v2}`% $$/수식$$인 소금물을 섞은 후에 물을 더 부어서 농도가 $$수식$$ {v3}`% $$/수식$$인 소금물 $$수식$$ {v4}` rm g $$/수식$$을 만들었다. 농도가 $$수식$$ {v1}`% $$/수식$$인 소금물과 더 부은 물의 양의 비가 $$수식$$ 1:{v5} $$/수식$$일 때, 더 부은 물의 양은?\n" \
           "① $$수식$${c1}`rm g $$/수식$$\n" \
           "② $$수식$${c2}`rm g $$/수식$$\n" \
           "③ $$수식$${c3}`rm g $$/수식$$\n" \
           "④ $$수식$${c4}`rm g $$/수식$$\n" \
           "⑤ $$수식$${c5}`rm g $$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "농도가 $$수식$${v1}`%$$/수식$$의 소금물의 양을 $$수식$$x`rm g$$/수식$$이라 하면 더 부은 물의 양은 $$수식$${v5}x rm g$$/수식$$\n" \
              "$$수식$${ss1}$$/수식$$\n" \
              "이므로 소금 $$수식$$x`rm g$$/수식$$을 더 넣는다고 하면\n" \
              "$$수식$${ss2},```{ss3}$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{result1}$$/수식$$\n" \
              "따라서 더 부은 물의 양은 $$수식$$ {v5} `TIMES` {result1} `=` {result2}`rm (g)$$/수식$$\n\n"


    while True:
        v1 = np.random.randint(5,50)
        v2 = np.random.randint(5,50)
        v3 = np.random.randint(1,50)
        v4 = np.random.randint(10,100) * 10
        v5 = np.random.randint(2,7)
        

        vv1 = v2 * v4
        vv2 = (1 + v5) * v2
        vv3 = v3 * v4

        vvv1 = v1 - vv2
        vvv2 = vv3 - vv1
        if vvv1 == 0:
            continue
        result1 = vvv2 // vvv1
        result1_mod = vvv2 % vvv1
        result2 = v5 * result1
        if result1_mod == 0 and result1 > 0 and result1 < 2000:
            break
    
    ss1 = "{v1} over 100 `TIMES` x `+` {v2} over 100 `TIMES` LEFT ( {v4}`-`x`-`{v5}x RIGHT )`=`{v3} over 100 `TIMES` {v4} ".format(v1=v1,v2=v2,v3=v3,v4=v4,v5=v5)

    ss2 = "{v1}x`+`{vv1}`-`{vv2}x`=`{vv3}".format(v1=v1,vv1=vv1,vv2=vv2,vv3=vv3)

    ss3 = "{vvv1}x `=` {vvv2}".format(vvv1=vvv1,vvv2=vvv2)
    

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(2,10) * 5 
        temp = result2 - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result2:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,v4=v4,v5=v5,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(v1=v1,v5=v5,ss1=ss1,ss2=ss2,ss3=ss3,result1=result1,result2=result2)

    return stem, answer, comment


def latterandexpress113_Stem_083():
    stem = "빈 물통에 물을 가득 채우는 데 수도관 $$수식$$A$$/수식$$로 물을 넣으면 $$수식$${v1}$$/수식$$분이 걸리고, 수도관 $$수식$$B$$/수식$$로 물을 넣으면 $$수식$${v2}$$/수식$$분이 걸린다. 처음에 수도관 $$수식$$A$$/수식$$를 열었다가 도중에$$수식$$A$$/수식$$를 잠그고 $$수식$$B$$/수식$$를 열어서 빈 물통에 물을 가득 채웠는데 $$수식$$B$$/수식$$를 연 시간이 $$수식$$A$$/수식$$를 연 시간보다 $$수식$${v3}$$/수식$$분 더 길다고 한다. 수도관 $$수식$$A$$/수식$$, $$수식$$B$$/수식$$로 물을 넣은 시간을 각각 구하면?\n" \
           "① $$수식$$A:{c_a1}분 $$/수식$$, $$수식$$B:{c_b1}분 $$/수식$$\n" \
           "② $$수식$$A:{c_a2}분 $$/수식$$, $$수식$$B:{c_b2}분 $$/수식$$\n" \
           "③ $$수식$$A:{c_a3}분 $$/수식$$, $$수식$$B:{c_b3}분 $$/수식$$\n" \
           "④ $$수식$$A:{c_a4}분 $$/수식$$, $$수식$$B:{c_b4}분 $$/수식$$\n" \
           "⑤ $$수식$$A:{c_a5}분 $$/수식$$, $$수식$$B:{c_b5}분 $$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "물통에 가득 찬 물의 양을 1이라 하면 수도관 $$수식$$A$$/수식$$, $$수식$$B$$/수식$$ 로 1분에 채울 수 있는 물의 양은 각각 $$수식$$1 over {v1}$$/수식$$, $$수식$$1 over {v2}$$/수식$$, 이다.\n" \
              "이때 수도관 $$수식$$A$$/수식$$로 물을 넣은 시간을 $$수식$$x$$/수식$$분이라 하면 수도관 $$수식$$B$$/수식$$로 물을 넣은 시간은 $$수식$$LEFT ( x + {v3} RIGHT ) $$/수식$$이므로\n" \
              "$$수식$${ss1}$$/수식$$\n" \
              "$$수식$${ss2}$$/수식$$\n" \
              "양변에 $$수식$${vv2}$$/수식$$을 곱하면\n" \
              "$$수식$${ss3}$$/수식$$$$수식$${ss4}$$/수식$$$$수식$$THEREFORE~x`=`{result_a}$$/수식$$\n" \
              "따라서 수도관 $$수식$$A$$/수식$$로 물을 넣은 시간은 $$수식$${result_a}$$/수식$$분, 수도관 $$수식$$B$$/수식$$로 물을 넣은 시간은 $$수식$$ {result_a} `+` {v3} `=` {result_b}`(분)$$/수식$$\n\n"


    while True:
        v1 = np.random.randint(5,30)
        v2 = np.random.randint(5,30)
        v3 = np.random.randint(5,30)
        

        vv1 = divUpDown(v3,v2)
        if vv1[1] == 0:
            continue
        vv1_1 = vv1[0]
        vv1_2 = vv1[1]

        vv2 = lcm(v1,lcm(v2,vv1_2))
        
        vvv1 = vv2 // v1
        vvv2 = vv2 // v2
        vvv3 = (vv1_1 * vv2) // vv1_2
        vvv4 = vv2

        vvvv1 = vvv1 + vvv2
        vvvv2 = vvv4 - vvv3
        if vvvv2 == 0:
            continue
        result_a = vvvv2 // vvvv1
        result_a_mod = vvvv2 % vvvv1

        result_b = result_a + v3

        if result_a_mod == 0 and result_a > 0 and result_a < 60 and result_b > 0 and result_b < 60:
            break
    
    ss1 = "1 over {v1} `TIMES` x `+` 1 over {v2} `TIMES` LEFT ( x `+` {v3} RIGHT )`=`1".format(v1=v1,v2=v2,v3=v3)

    ss2 = "1 over {v1} x `+` 1 over {v2} x `+` {vv1_1} over {vv1_2}`=`1".format(v1=v1,v2=v2,vv1_1=vv1_1,vv1_2=vv1_2)

    ss3 = "{vvv1}x`+`{vvv2}x`+`{vvv3}`=`{vvv4}".format(vvv1=vvv1,vvv2=vvv2,vvv3=vvv3,vvv4=vvv4)
    
    ss4 = "{vvvv1}x`=`{vvvv2}".format(vvvv1=vvvv1,vvvv2=vvvv2)
    

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(1,4)
        temp_a = result_a - res_interval * idx
        temp_b = result_b - res_interval * idx

        for i in range(5):
            candidates.append((temp_a + res_interval * i, temp_b + res_interval * i))

        (c_a1,c_b1), (c_a2,c_b2), (c_a3,c_b3), (c_a4,c_b4), (c_a5,c_b5) = candidates
        if c_a1 > 0 and c_a2 > 0 and c_a3 > 0 and c_a4 > 0 and c_a5 > 0 \
           and c_a1 < 60 and c_a2 < 60 and c_a3 < 60 and c_a4 < 60 and c_a5 < 60 \
           and c_b1 > 0 and c_b2 > 0 and c_b3 > 0 and c_b4 > 0 and c_b5 > 0 \
           and c_b1 < 60 and c_b2 < 60 and c_b3 < 60 and c_b4 < 60 and c_b5 < 60:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == (result_a,result_b):
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,c_a1=c_a1,c_a2=c_a2,c_a3=c_a3,c_a4=c_a4,c_a5=c_a5,c_b1=c_b1,c_b2=c_b2,c_b3=c_b3,c_b4=c_b4,c_b5=c_b5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(v1=v1,v2=v2,v3=v3,vv2=vv2,ss1=ss1,ss2=ss2,ss3=ss3,ss4=ss4,result_a=result_a,result_b=result_b)

    return stem, answer, comment


def latterandexpress113_Stem_084():
    stem = "{v1}시와 {v2}시 사이에서 시계의 시침과 분침이 이루는 각의 크기가 $$수식$$ {v3} DEG $$/수식$$가 될 때의 시각은?\n" \
           "① $$수식$$ {v1} 시 {c1} over {result_down}  분 $$/수식$$\n" \
           "② $$수식$$ {v1} 시 {c2} over {result_down}  분 $$/수식$$\n" \
           "③ $$수식$$ {v1} 시 {c3} over {result_down}  분 $$/수식$$\n" \
           "④ $$수식$$ {v1} 시 {c4} over {result_down}  분 $$/수식$$\n" \
           "⑤ $$수식$$ {v1} 시 {c5} over {result_down}  분 $$/수식$$\n" 
    answer = "(정답)\n{a1}"
    comment = "(해설)\n" \
              "$$수식$$ {v3} DEG $$/수식$$가 될 때의 시각을  $$수식$$ {v1}시 x 분 $$/수식$$이라 하면 분침이 시침보다 시곗바늘이 도는 방향으로 $$수식$$ {v3} DEG $$/수식$$만큼 더 움직여야 하므로\n" \
              "$$수식$${ss1}`,` {ss2}$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{ss3}$$/수식$$\n" \
              "따라서 $$수식$$ {v3} DEG $$/수식$$ 가 될 때의 시각은 $$수식$$ {v1}시 {result_up} over {result_down} 분 $$/수식$$이다.\n\n"

    while True:
        v1 = np.random.randint(1,12)
        v2 = v1 + 1
        v3 = np.random.randint(1,7) * 30

        vv1 = 6 - 0.5
        vv2 = v3 + 30 * v1

        result_up, result_down = divUpDown(vv2, vv1)
        result = vv2 // vv1
        if result_down != 1 and result < 50:
            break

    ss1 = "6 x `-` LEFT ( 30 `TIMES` {v1} `+` 0.5 x RIGHT ) `=` {v3}".format(v1=v1,v3=v3)

    ss2 = "{vv1} x = {vv2}".format(vv1=vv1,vv2=vv2)

    ss3 = "{vv2} over {vv1} `=` {result_up} over {result_down}".format(vv1=vv1,vv2=vv2,result_up=result_up,result_down=result_down)
    

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(1,10) * 15
        temp = result_up - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0 and \
            c1 < 660 and c2 < 660 and c3 < 660 and c4 < 660 and c5 < 660:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result_up:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,result_down=result_down)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(v1=v1,v3=v3,ss1=ss1,ss2=ss2,ss3=ss3,result_up=result_up,result_down=result_down)

    return stem, answer, comment


def latterandexpress113_Stem_085():
    stem = "각 자리의 숫자의 합이 $$수식$${v1}$$/수식$$인 두 자리 자연수가 있다. 이 자연수의 십의 자리의 숫자와 일의 자리의 숫자를 바꾼 수는 처음 수보다 $$수식$${v2}$$/수식$$만큼 작다고 할 때, 처음 수를 구하시오.\n"
    answer = "(정답)\n{a}"
    comment = "(해설)\n" \
              "처음 수의 십의 자리의 숫자를 $$수식$$x$$/수식$$라 하면 일의 자리의 숫자는  $$수식$${v1}`-`x $$/수식$$이므로\n" \
              "$$수식$$ {s1} $$/수식$$\n" \
              "$$수식$$ {s2},{s3} THEREFORE~x`=`{result1}$$/수식$$\n" \
              "따라서 어떤 수는 {result2} 이다.\n\n"

    while True:
        v1 = np.random.randint(1,10)
        v2 = np.random.randint(1,10)

        vv1 = 10 * v1
        vv2 = v1 - v2

        vvv1 = vv2 - vv1

        if vv2 == 0 or vvv1 == 0:
            continue

        result1 = vvv1 // (-18)
        result1_mod = vvv1 % (-18)

        result2 = result1 * 10 + (v1 - result1)

        if result1_mod == 0 and result1 < 10 and result1 > 0 and (v1 - result1) > 0:
            break

    s1 = "10 LEFT ( {v1} `-` x RIGHT )`+` x `=` 10x`+`{v1}`-`x`-`{v2}".format(v1=v1,v2=v2)
    s2 = "-9x`+`{vv1}`=` 9x {vv2}".format(vv1=vv1,vv2=vv2)
    s3 = "-18x`=`{vvv1}".format(vvv1=vvv1)

    stem = stem.format(v1=v1,v2=v2)
    answer = answer.format(a=result2)
    comment = comment.format(v1=v1,s1=s1,s2=s2,s3=s3,result1=result1,result2=result2)

    return stem, answer, comment


def latterandexpress113_Stem_086():
    stem = "조선 후기의 실학자 황윤석이 쓴 책 “이수신편”에는 다음과 같은 문제가 실려 있다.\n" \
            "$$수식$$ {v1} $$/수식$$개의 만두와 $$수식$$ {v2} $$/수식$$명의 스님이 있다. 큰 스님이 만두를 {s1} 개씩 가지면 작은 스님은 {s2} 명당 만두 한 개를 나누어 가져야 한다.\n" \
            "이때 큰 스님과 작은 스님은 각각 몇 명인지 차례로 구하시오. \n"
    answer = "(정답)\n{a1} {a2}\n"
    comment = "(해설)\n" \
              "큰 스님의 수를 $$수식$$x$$/수식$$명이라 하면 작은 스님의 수는 $$수식$$ LEFT ( {v2}`-` x RIGHT )$$/수식$$명이다. 큰 스님 한 명에게는 만두를 {s1} 개씩 주고 작은 스님에게는 {s2} 명당 만두를 한 개씩 나누어 주므로\n" \
              "$$수식$$ {ss1} $$/수식$$\n" \
              "양변에 $$수식$$ {v4} $$/수식$$을 곱하면\n" \
              "$$수식$$ {ss2},``{ss3}``` THEREFORE~x`=`{result1} $$/수식$$\n" \
              "따라서 큰 스님은 $$수식$$ {result1} $$/수식$$명, 작은 스님은 $$수식$$ {v2}`-`{result1} `=` {result2} $$/수식$$(명)이다.\n\n"

    
    while True:
        v1 = np.random.randint(5,20) * 10
        v2 = np.random.randint(5,20) * 10

        v3 = np.random.randint(1,11)
        s1 = ["","한", "두", "세","네","다섯","여섯","일곱","여뎗","아홉","열"][v3]
        v4 = np.random.randint(1,11)
        s2 = ["","한", "두", "세","네","다섯","여섯","일곱","여뎗","아홉","열"][v4]

       
        vv1 = v3 * v4
        vv2 = v1 * v4

        vvv1 = vv1 - 1
        vvv2 = vv2 - v2

        if vvv1 == 0 or vvv2 == 0:
            continue

        result1 = vvv2 // vvv1
        result1_mod = vvv2 % vvv1

        result2 = v2 - result1 

        if result1_mod == 0 and result1> 0 and result2 > 0:
            break

    ss1 = "{v3}x`+` 1 over {v4} LEFT ( {v2} `-` x RIGHT ) `=` {v1}".format(v1=v1,v2=v2,v3=v3,v4=v4)
    ss2 = "{vv1}x`+`{v2}`-`x `=` {vv2}".format(vv1=vv1,vv2=vv2,v2=v2)
    ss3 = "{vvv1}x`=`{vvv2}".format(vvv1=vvv1,vvv2=vvv2)

    stem = stem.format(v1=v1,v2=v2,s1=s1,s2=s2)
    answer = answer.format(a1=result1,a2=result2)
    comment = comment.format(v2=v2,v4=v4,s1=s1,s2=s2,ss1=ss1,ss2=ss2,ss3=ss3,result1=result1,result2=result2)

    return stem, answer, comment



def latterandexpress113_Stem_087():
    stem = "나와 형의 나이의 차는 $$수식$${a1}$$/수식$$ 세이고 나와 동생의 나이의 차는 $$수식$${a2}$$/수식$$ 세이다." \
           " 세 사람의 나이의 합이 $$수식$${a3}$$/수식$$일 때, 나의 나이는?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "나의 나이를 x세라 하면 형의 나이는 $$수식$$(x+{a1})세,$$/수식$$\n" \
              "동생의 나이는 $$수식$$(x-{a2})세이므로$$/수식$$\n" \
              "$$수식$$(x+{a1})+x+(x-{a2})`=`{a3},````3x`=`{a4}$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 나의 나이는 $$수식$${result}$$/수식$$ 세이다.\n\n"

    while True:
        a1 = np.random.randint(1,9)
        a2 = np.random.randint(1,9)
        a3 = np.random.randint(20,70)

        a4 = a3-a1+a2
        result = math.floor(a4/3)

        if a4!=0 and a4 % 3 ==0:
            if(result-a2>0):
                break

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result+1)
        q3 = "{%s}" % (result+2)
        q4 = "{%s}" % (result+3)
        q5 = "{%s}" % (result+4)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result-1)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result+1)
        q4 = "{%s}" % (result+2)
        q5 = "{%s}" % (result+3)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result-2)
        q2 = "{%s}" % (result-1)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result+1)
        q5 = "{%s}" % (result+2)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result-3)
        q2 = "{%s}" % (result-2)
        q3 = "{%s}" % (result-1)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result+1)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result-4)
        q2 = "{%s}" % (result-3)
        q3 = "{%s}" % (result-10)
        q4 = "{%s}" % (result-5)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1, a2=a2, a3=a3, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4,  result=result)

    return stem, answer, comment


def latterandexpress113_Stem_088():
    stem = "{s1}는 어버이날 선물을 준비하기 위해 동생 {s2}와 함께 예금을 하기로 하였다. 현재      {s1}의 예금액은 {v1}원이고 {s2}의 예금액은 {v2}원이다. {s1}는 매달 $$수식$${ss1}$$/수식$$원씩, {s2}는 매달 \n" \
        "$$수식$${ss2}$$/수식$$원씩 예금하면 $$수식$${v5}$$/수식$$개월 후에 {s1}와 {s2}의 예금액이 같아진다고 한다. 이때 {s1}의 매달 예금액과 {s2}의 매달 예금액을 차례로 구하시오.\n"
    answer = "(정답)\n$$수식$${a1}$$/수식$$, $$수식$${a2}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${v5}$$/수식$$개월 후 {s1}이의 예금액은 \n" \
              "$$수식$${sss1}`=`{sss2}$$/수식$$\n" \
              "$$수식$${v5}$$/수식$$개월 후 {s2}이의 예금액은 \n" \
              "$$수식$${sss3}`=`{sss4}`=`{sss5}$$/수식$$\n" \
              "$$수식$${v5}$$/수식$$개월 후에 {s1}이와 {s2}의 예금액이 같아진다고 하면 \n" \
              "$$수식$${sss2}`=`{sss5}$$/수식$$\n" \
              "$$수식$${ssss1}  THEREFORE~{ss1}`=`{result1}$$/수식$$\n" \
              "따라서 {s1}이의 매달 예금액은 $$수식$${v5}$$/수식$$원, {s2}의 매달 예금액은 $$수식$${ssss2}$$/수식$$(원)이다.\n\n"

    idx = np.random.randint(7)

    s1 = ["수연","지안","서윤","하린","하은","서연","서현"][idx]
    s2 = ["시아","지유","서아","채아","수아","지우","윤서"][idx]


    while True:
        v1 = np.random.randint(1,30) * 1000
        v2 = np.random.randint(1,30) * 1000
        v3 = np.random.randint(1,10)
        v4 = np.random.randint(1,10) * 1000
        v5 = np.random.randint(2,20)

        vv1 = v3 * v5
        vv2 = v4 * v5
        vv3 = v2 - vv2
        if vv3 <= 0 :
            continue

        vvv1 = v5 - vv1
        vvv2 = vv3 - v1

        if vvv1 >= 0 or vvv2 >= 0:
            continue

        result1 = vvv2 // vvv1
        result1_mod = vvv2 % vvv1
        result2 = v3 * result1 - v4
        if result1_mod == 0 and result1 > 0 and result2 > 0:
            break

    ss1 = "a"
    ss2 = "{v3}{ss1} `-` {v4}".format(v3=v3,ss1=ss1,v4=v4)

    sss1 = "{v1}`+`{ss1}`TIMES`{v5}".format(v1=v1,ss1=ss1,v5=v5)
    sss2 = "{v1}`+`{v5}{ss1}".format(v1=v1,v5=v5,ss1=ss1)

    sss3 = "{v2}`+` LEFT ( {ss2} RIGHT ) `TIMES` {v5} ".format(v2=v2,ss2=ss2,v5=v5)
    sss4 = "{v2}`+`{vv1}{ss1}`-`{vv2}".format(v2=v2,vv1=vv1,ss1=ss1,vv2=vv2)
    sss5 = "{vv3}`+`{vv1}{ss1}".format(vv3=vv3,vv1=vv1,ss1=ss1)

    ssss1 = "{vvv1}a`=`{vvv2}".format(vvv1=vvv1,vvv2=vvv2)
    ssss2 = "{v3}`TIMES` {result1} `-` {v4}`=`{result2}".format(v3=v3,result1=result1,v4=v4,result2=result2)

    stem = stem.format(s1=s1,s2=s2,v1=v1,v2=v2,ss1=ss1,ss2=ss2,v3=v3,v4=v4,v5=v5)
    answer = answer.format(a1=result1,a2=result2)
    comment = comment.format(v5=v5,s1=s1,ss1=ss1,sss1=sss1,sss2=sss2,sss3=sss3,sss4=sss4,sss5=sss5,s2=s2,ssss1=ssss1,ssss2=ssss2,result1=result1)

    return stem, answer, comment


def latterandexpress113_Stem_089():
    stem = "원가가 $$수식$${v1}$$/수식$$원인 상품에  $$수식$${v2}%$$/수식$$이익을 붙여서 정가를 정했다가 다시 정가의 $$수식$$x%$$/수식$$를 할인하여 판매 하였더니 $$수식$$1$$/수식$$개를 팔 때마다 원가의 $$수식$${v3}%$$/수식$$의 이익이 생겼다. 이때 $$수식$$x$$/수식$$의 값은? \n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n$$수식$${a}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$(정가)`=`{ss1}$$/수식$$\n" \
              "$$수식$$`=`{ss2}`=`{vv2}(원)$$/수식$$\n" \
              "이므로 \n" \
              "$$수식$$(판매 가격){ss3}`=`{ss4}(원)$$/수식$$\n" \
              "이때 이익이 원가의 $$수식$$ {v3} % $$/수식$$이므로\n" \
              "$$수식$${sss1}$$/수식$$\n" \
              "$$수식$${sss2}, {sss3}$$/수식$$\n" \
              "$$수식$$THEREFORE~{result}$$/수식$$\n\n"

    while True:
        v1 = np.random.randint(1,20) * 1000
        v2 = np.random.randint(1,10) * 10
        v3 = np.random.randint(1,10) * 10

        vv1 = v1 * v2 // 100
        if (v1 * v2) % 100 != 0:
            continue

        vv2 = v1 + vv1
        vv3 = vv2 // 100

        if vv2 % 100 != 0:
            continue
        
        vvv1 = vv2 - v1
        vvv2 = (v1 * v3) // 100

        if (v1 * v3) % 100 != 0:
            continue

        vvv3 = vvv1 - vvv2
        if vvv3 == 0:
            continue
        result = vvv3 // vv3 
        if vvv3 % vv3 == 0 and result > 0:
            break

    ss1 = "{v1} `+` {v1} `TIMES` {v2} over 100".format(v1=v1,v2=v2)
    ss2 = "{v1}`+`{vv1}".format(v1=v1,vv1=vv1)
    ss3 = "{vv2}`-`{vv2}`TIMES` x over 100".format(vv2=vv2)
    ss4 = "{vv2}`-`{vv3}x".format(vv2=vv2,vv3=vv3)

    sss1 = "LEFT ( {ss4} RIGHT )`-`{v1}`=`{v1}`TIMES`{v3}over100".format(ss4=ss4,v1=v1,v3=v3)
    sss2 = "{vvv1}`-`{vv3}x`=`{vvv2}".format(vvv1=vvv1,vv3=vv3,vvv2=vvv2)
    sss3 = "{vvv3}`=`{vv3}x".format(vvv3=vvv3,vv3=vv3)

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(2,10)
        temp = result - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(ss1=ss1,ss2=ss2,vv2=vv2,ss3=ss3,ss4=ss4,v3=v3,sss1=sss1,sss2=sss2,sss3=sss3,result=result)

    return stem, answer, comment

def latterandexpress113_Stem_090():
    stem = "지난달 {s1}의 몸무게는 {s2}의 몸무게보다 $$수식$${v1}$$/수식$$이 더 나갔다. 현재는 지난달에 비하여 {s1}의 몸무게는 $$수식$${v2}%$$/수식$$ 줄고, {s2}의 몸무게는 $$수식$${v3} %$$/수식$$ 늘어서 두 사람의 몸무게의 합이 $$수식$${v4}``rm kg$$/수식$$ 이다. 이때 지난달 {s2}의 몸무게는?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n" 
    answer = "(정답)\n$$수식$${a}$$/수식$$\n"
    comment = "(해설)\n" \
              "지난달의 {s2}의 몸무게를 $$수식$$x rm kg $$/수식$$이라 하면 {s1}의 몸무게는 $$수식$${ss1}$$/수식$$ 이므로\n" \
              "현재 {s1}의 몸무게는\n" \
              "$$수식$${ss2}$$/수식$$\n" \
              "현재 {s2}의 몸무게는\n" \
              "$$수식$${ss3}$$/수식$$\n" \
              "현재 {s1}와 {s2}의 몸무게의 합이 $$수식$${v4}$$/수식$$이므로 \n" \
              "$$수식$${ss4}$$/수식$$\n" \
              "양변에 $$수식$$100$$/수식$$을 곱하면\n" \
              "$$수식$${ss5}$$/수식$$\n" \
              "$$수식$${ss6}  THEREFORE~{result} $$/수식$$\n" \
              "따라서 지난달 {s2}의 몸무게는 $$수식$${result}``rm kg$$/수식$$이다.\n\n"

    idx = np.random.randint(4)

    s1 = ["어머니","아버지","어머니","아버지"][idx]
    s2 = ["딸","아들","아들","딸"][idx]


    while True:
        v1 = np.random.randint(10,50) 
        v2 = np.random.randint(1,10)
        v3 = np.random.randint(1,10)
        v4 = np.random.randint(1,120)

        vv1 = 100 - v2
        vv2 = 100 + v3

        vvv1 = v4 * 100
        vvv2 = vv1 + vv2
        vvv3 = vvv1 - vv1 * v1
        
        result = vvv3 // vvv2 
        if vvv3 % vvv2 == 0 and result > 0:
            break

    ss1 = "LEFT ( x `+` {v1} RIGHT )".format(v1=v1)
    
    ss2 = "{ss1} `-` {v2} over 100 `TIMES` {ss1} `=` {vv1} over 100 `TIMES`{ss1}".format(ss1=ss1,v2=v2,vv1=vv1)
    
    ss3 = "x`+`{v3} over 100 `TIMES` x `=` {vv2} over 100 x".format(v3=v3,vv2=vv2)
    
    ss4 = "{vv1} over 100 {ss1}`+`{vv2} over 100 x `=` {v4}".format(vv1=vv1,ss1=ss1,vv2=vv2,v4=v4)

    ss5 = "{vv1} {ss1}`+` {vv2}x `=` {vvv1}".format(vv1=vv1,ss1=ss1,vv2=vv2,vvv1=vvv1)

    ss6 = "{vvv2}x`=`{vvv3}".format(vvv2=vvv2,vvv3=vvv3)

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(2,10)
        temp = result - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(s1=s1,s2=s2,v1=v1,v2=v2,v3=v3,v4=v4,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(s1=s1,s2=s2,ss1=ss1,ss2=ss2,ss3=ss3,ss4=ss4,ss5=ss5,ss6=ss6,v4=v4,result=result)

    return stem, answer, comment

def latterandexpress113_Stem_091():
    stem = "어느 축구 동아리에서 회비를 걷어서 축구공을 사려고 한다. 회비를 $$수식$${v1}$$/수식$$원씩 걷으면 $$수식$${v2}$$/수식$$원이 부족하고, $$수식$${v3}$$/수식$$원씩 걷으면 $$수식$${v4}$$/수식$$원이 남는다고 할 때, $$수식$${v5}$$/수식$$원씩 걷으면 부족한 금액은?\n" \
           "① $$수식$${c1}$$/수식$$\n" \
           "② $$수식$${c2}$$/수식$$\n" \
           "③ $$수식$${c3}$$/수식$$\n" \
           "④ $$수식$${c4}$$/수식$$\n" \
           "⑤ $$수식$${c5}$$/수식$$\n"
    answer = "(정답)\n$$수식$${a}$$/수식$$\n"
    comment = "(해설)\n" \
              "축구 동아리의 회원 수를 명이라 하면\n" \
              "$$수식$${v1}$$/수식$$원씩 걷을 때의 축구공의 가격은\n" \
              "$$수식$${ss1}$$/수식$$\n" \
              "$$수식$${v3}$$/수식$$원씩 걷을 때의 축구공의 가격은\n" \
              "$$수식$${ss2}$$/수식$$\n" \
              "이때 축구공의 가격은 같으므로\n" \
              "$$수식$${ss1}`=`{ss2}$$/수식$$\n" \
              "$$수식$${ss3}THEREFORE~{vv3}$$/수식$$\n" \
              "즉, 축구 동아리의 회원 수는 $$수식$${vv3}$$/수식$$명이므로 축구공의 가격은\n" \
              "$$수식$${ss4}$$/수식$$\n" \
              "따라서$$수식$${vv3}$$/수식$$ $$수식$${v5}$$/수식$$명에게 원씩 걷으면 \n" \
              "$$수식$${ss5}$$/수식$$(원)이므로\n" \
              "$$수식$${ss6}$$/수식$$(원)이 부족하다.\n\n"


    while True:
        v1 = np.random.randint(10,100) * 100
        v2 = np.random.randint(10,100) * 100
        v3 = np.random.randint(10,100) * 100
        v4 = np.random.randint(10,100) * 100
        v5 = np.random.randint(10,100) * 100

        vv1 = v1-v3
        vv2 = -v4-v2
        if vv1 == 0:
            continue
        vv3 =  vv2 // vv1
        if vv3 <= 0 or vv2 % vv1 != 0 :
            continue

        vvv1 = v1 * vv3 + v2
        vvv2 = vv3 * v5
        result = vvv1 - vvv2

        if result > 0:
            break

    ss1 = "LEFT ( {v1}x `+` {v2} RIGHT )".format(v1=v1,v2=v2)
    ss2 = "LEFT ( {v3}x `-` {v4} RIGHT )".format(v3=v3,v4=v4)

    ss3 = "{vv1}x `=` {vv2}".format(vv1=vv1,vv2=vv2)

    ss4 = "{v1}`TIMES`{vv3}`+`{v2}`=`{vvv1}".format(v1=v1,vv3=vv3,v2=v2,vvv1=vvv1)

    ss5 = "{vv3}`TIMES`{v5}`=`{vvv2}".format(vv3=vv3,v5=v5,vvv2=vvv2)
    ss6 = "{vvv1}`-`{vvv2}`=`{result}".format(vvv1=vvv1,vvv2=vvv2,result=result)

    while True:
        idx = np.random.randint(0,5)
        candidates = []

        res_interval = np.random.randint(2,10) * 100
        temp = result - res_interval * idx

        for i in range(5):
            candidates.append(temp + res_interval * i)

        c1, c2, c3, c4, c5 = candidates
        if c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and c5 > 0:
            break

    correct_idx = 0
    for i, c in enumerate(candidates):
        if c == result:
            correct_idx = i
            break

    stem = stem.format(v1=v1,v2=v2,v3=v3,v4=v4,v5=v5,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5)
    answer = answer.format(a=answer_dict[correct_idx])
    comment = comment.format(v1=v1,ss1=ss1,v3=v3,ss2=ss2,ss3=ss3,ss4=ss4,ss5=ss5,ss6=ss6,vv3=vv3,v5=v5)

    return stem, answer, comment


def latterandexpress113_Stem_092():
    stem = "어머니가 $$수식$${p1}$$/수식$$을 만들어 삼형제에게 나누어 주었다. 첫째에게 만든 $$수식$${p1}$$/수식$$의" \
           " 절반을 주고 한 개를 더 주었고, 둘째에게도 남은 $$수식$${p1}$$/수식$$의 절반을 주고 한 개를 더 주었다. 셋째에게도 같은 방법으로" \
           " $$수식$${p1}$$/수식$$을 주었더니 어머니에게는 $$수식$${a}$$/수식$$개의 $$수식$${p1}$$/수식$$이 남았다." \
           " 어머니가 만든 $$수식$${p1}$$/수식$$의 개수는?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "어머니가 만든 $$수식$${p1}$$/수식$$의 개수를 x라 하면\n" \
              "첫째에게 준 $$수식$${p1}$$/수식$$의 개수는 $$수식$$1 over 2`x`+`1$$/수식$$\n" \
              "첫째에게 주고 남은 $$수식$${p1}$$/수식$$의 개수는\n" \
              "$$수식$$x`-`(`1 over 2`x`+`1`)`=`1 over 2`x`-`1$$/수식$$\n" \
              "이므로 둘째에게 준 $$수식$${p1}$$/수식$$의 개수는\n" \
              "$$수식$$(`1 over 2`x`-`1`) TIMES 1 over 2`+`1`=`1 over 4`x`+`1 over 2$$/수식$$\n" \
              "둘째에게 주고 남은 $$수식$${p1}$$/수식$$의 개수는\n" \
              "$$수식$$1 over 2`x`-1`-(`1 over 4`x`+`1 over 2`)`=`1 over 4`x`-`3 over 2$$/수식$$\n" \
              "이므로 셋째에게 준 $$수식$${p1}$$/수식$$의 개수는\n" \
              "$$수식$$(`1 over 4`x`-`3 over 2`) TIMES 1 over 2`+1`=`1 over 8`x`+`1 over 4$$/수식$$\n" \
              "남은 $$수식$${p1}$$/수식$$이 $$수식$${a}$$/수식$$개 이므로\n" \
              "$$수식$$(`1 over 2 `x`+1`)`+`(`1 over 4`x`+`1 over 2`)`+`(`1 over 8`x`+`1 over 4`)`+{a}=`x$$/수식$$\n" \
              "$$수식$$7 over 8`x`+`{a1} over 4`=`x,````-`1 over 8`x`=`-`{a1} over 4$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 어머니가 만든 $$수식$${p1}$$/수식$$의 개수는 $$수식$${result}$$/수식$$이다.\n\n"


    p1 = ["빵","떡","곶감"][np.random.randint(0,2)]
    a = np.random.randint(1,10)
    a1 = 7 + a*4
    result = a1*2


    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result+2)
        q3 = "{%s}" % (result+4)
        q4 = "{%s}" % (result+6)
        q5 = "{%s}" % (result+8)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result-2)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result+2)
        q4 = "{%s}" % (result+4)
        q5 = "{%s}" % (result+6)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result-4)
        q2 = "{%s}" % (result-2)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result+2)
        q5 = "{%s}" % (result+4)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result-6)
        q2 = "{%s}" % (result-4)
        q3 = "{%s}" % (result-2)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result+2)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result-8)
        q2 = "{%s}" % (result-6)
        q3 = "{%s}" % (result-4)
        q4 = "{%s}" % (result-2)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(p1=p1, a=a, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(p1=p1,a=a,a1=a1,  result=result)

    return stem, answer, comment


def latterandexpress113_Stem_093():
    stem = "등산을 하는데 올라갈 때는 시속 $$수식$${a1}``rm km$$/수식$$로 걷고," \
           " 정상에서 $$수식$${t1}$$/수식$$시간 동안 휴식을 취한 다음 내려올 때는 다른 길을 시속 $$수식$${a2}``rm km$$/수식$$로 걸어서" \
           " 모두 $$수식$${t2}$$/수식$$ 시간이 걸렸다. 올라간 길과 내려온 길의 거리의 합이 $$수식$${d1}``rm km$$/수식$$ 일 때," \
           " 올라갈 때 걸린 시간을 구하시오.\n"
    answer = "(정답)\n$$수식$${result}$$/수식$$\n"
    comment = "(해설)\n" \
              "올라간 거리를 x km라 하면 내려온 거리는\n" \
              "$$수식$$({d1}-x) rm km이므로$$/수식$$\n" \
              "$$수식$$x over {a1}`+`{t1}`+`({d1}-x) over {a2}`=`{t2},````x over {a1}`+`({d1}-x) over {a2}`=`{t3}$$/수식$$\n" \
              "$$수식$${a2}x`+`{a1}({d1}-x)`=`{a3},````{a4}x`+`{a5}`=`{a3}$$/수식$$\n" \
              "$$수식$${a4}x`=`{a6}````````THEREFORE~x`=`{a7}$$/수식$$\n" \
              "따라서 올라간 거리는 $$수식$${a7}``rm km$$/수식$$이므로 올라갈 때 걸린 시간은\n" \
              "$$수식$${a8}`=`{result}(시간)$$/수식$$"


    while(1):
        a1 = np.random.randint(1,10)
        a2 = np.random.randint(1,10)

        a4 = a2 - a1

        t1 = np.random.randint(1,4)
        d1 = np.random.randint(10, 20)
        a3 = t1 * a1 * a2
        a5 = d1 * a1
        a6 = a3 - a5

        t2 = np.random.randint(6,10)
        t3 = t2-t1


        if(a1<a2 and t2>t1 and (a6/a4)>0 and a2-a1>1):
            if(a6!=0 and a4!=0 and a1!=0):
                if((a6/a4)% a1 == 0 and a6 % a4 == 0):
                    break
    a7 = math.floor(a6/a4)
    result = math.floor(a7/a1)
    a8 = "{%s} over {%s}" % (a7,a1)

    stem = stem.format(a1=a1, a2=a2, t1=t1, t2=t2, d1=d1)
    answer = answer.format(result=result)
    comment = comment.format(a1=a1, a2=a2, a3=a3, a4=a4, a5=a5, a6=a6, a7=a7, a8=a8, t1=t1, t2=t2, t3=t3, d1=d1, result=result)

    return stem, answer, comment


def latterandexpress113_Stem_094():
    stem = "토끼와 거북이가 $$수식$${a1}``rm km$$/수식$$ 달리기 코스에서 경주를 하기로 했다. " \
           "경주에 이길 자신이 있던 토끼는 출발선에 서 있는 거북이보다 $$수식$${a2}``rm m$$/수식$$ 뒤에서 " \
           "거북이와 동시에 출발하였다. 거북이는 분속 $$수식$${a3}``rm m$$/수식$$ 로, 토끼는 거북이의 " \
           "$$수식$${a4}$$/수식$$ 배의 속력으로 달렸는데, 토끼가 중간에 낮잠을 잔 후 결승점으로 부랴부랴 달려가 " \
           "보니 이미 거북이는 토끼보다 $$수식$${a5}$$/수식$$ 분 일찍 들어와 있었다. 이때 토끼가 경주 중간에 낮잠을 잔 시간은?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "토끼가 낮잠을 잔 시간을 x분이라고 하면\n" \
              "((토끼가 달린 시간)+(토끼가 낮잠을 잔 시간)) - (거북이가 달린 시간) = $$수식$${a5}(분)$$/수식$$\n" \
              "이므로 $$수식$$(`{b1} over {b2}`+`x`)`-`{b3} over {a3}`=`{a5}$$/수식$$\n" \
              "$$수식$${b4}`+`x`-`{b5}`=`{a5}````````THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 토끼가 낮잠을 잔 시간은 $$수식$${result}$$/수식$$ 분이다.\n\n"


    while(1):
        a1 = np.random.randint(1,6)
        a2 = np.random.randint(1,6)*100
        a3 = np.random.randint(1,4)*10
        a4 = np.random.randint(1,4)
        a5 = np.random.randint(1,6)*10

        b1 = a1*1000+a2
        b2 = a3*a4
        b3 = a1*1000

        b4 = math.floor(b1/b2)
        b5 = math.floor(b3/a3)

        result = a5+b5-b4

        if(b1 % b2 == 0 and b3 % a3 == 0):
            if(result>0):
                break

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}분" % (result)
        q2 = "{%s}분" % (result+5)
        q3 = "{%s}분" % (result+10)
        q4 = "{%s}분" % (result+15)
        q5 = "{%s}분" % (result+20)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}분" % (result-5)
        q2 = "{%s}분" % (result)
        q3 = "{%s}분" % (result+5)
        q4 = "{%s}분" % (result+10)
        q5 = "{%s}분" % (result+15)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}분" % (result-10)
        q2 = "{%s}분" % (result-5)
        q3 = "{%s}분" % (result)
        q4 = "{%s}분" % (result+5)
        q5 = "{%s}분" % (result+10)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}분" % (result-15)
        q2 = "{%s}분" % (result-10)
        q3 = "{%s}분" % (result-5)
        q4 = "{%s}분" % (result)
        q5 = "{%s}분" % (result+5)
        answer_num = "④"
    else:
        q1 = "{%s}분" % (result-20)
        q2 = "{%s}분" % (result-15)
        q3 = "{%s}분" % (result-10)
        q4 = "{%s}분" % (result-5)
        q5 = "{%s}분" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,b1=b1,b2=b2,b3=b3,b4=b4,b5=b5,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_095():
    stem = "경찰이 $$수식$${a1}``rm m$$/수식$$ 떨어져 있는 도둑을 보고 보고 " \
           "매초 $$수식$${a2}``rm m$$/수식$$의 속력으로 쫓기 시작했다. 경찰이 도둑을 쫓기 " \
           "시작한 지 $$수식$${t1}$$/수식$$초 후에 이를 알아챈 도둑은 매초 $$수식$${a3}``rm m $$/수식$$의 " \
           "속력으로 도망간다고 할 때, 경찰이 출발하여 도둑을 잡을 때까지 걸리는 시간은?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "경찰이 출발하여 x초 후에 도둑을 잡는다고 하면\n" \
              "(경찰이 x초 동안 이동한 거리)\n" \
              "= $$수식$$(도둑이 (x-{t1})초``동안``이동한``거리)`+`{a1}(rm m)$$/수식$$\n" \
              "이므로 $$수식$${a2}x`=`{a3}(x-{t1})`+`{a1}$$/수식$$\n" \
              "$$수식$${a2}x`=`{a3}x+{b1}````````THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 경찰이 출발하여 도둑을 잡을 때까지 $$수식$${result}$$/수식$$초가 걸린다.\n\n"


    while(1):
        a1 = np.random.randint(1,5)*100
        a2 = np.random.randint(2,7)
        t1 = np.random.randint(10,20)
        a3 = np.random.randint(2,7)

        b1 = a1-(t1*a3)

        if(a2>a3):
            if(b1%(a2-a3)==0):
                break


    result = math.floor(b1 / (a2 - a3))

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}초" % (result)
        q2 = "{%s}초" % (result+5)
        q3 = "{%s}초" % (result+10)
        q4 = "{%s}초" % (result+15)
        q5 = "{%s}초" % (result+20)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}초" % (result-5)
        q2 = "{%s}초" % (result)
        q3 = "{%s}초" % (result+5)
        q4 = "{%s}초" % (result+10)
        q5 = "{%s}초" % (result+15)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}초" % (result-10)
        q2 = "{%s}초" % (result-5)
        q3 = "{%s}초" % (result)
        q4 = "{%s}초" % (result+5)
        q5 = "{%s}초" % (result+10)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}초" % (result-15)
        q2 = "{%s}초" % (result-10)
        q3 = "{%s}초" % (result-5)
        q4 = "{%s}초" % (result)
        q5 = "{%s}초" % (result+5)
        answer_num = "④"
    else:
        q1 = "{%s}초" % (result-20)
        q2 = "{%s}초" % (result-15)
        q3 = "{%s}초" % (result-10)
        q4 = "{%s}초" % (result-5)
        q5 = "{%s}초" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1,a2=a2,a3=a3,t1=t1,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,a2=a2,a3=a3,b1=b1,t1=t1,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_096():
    stem = "둘레의 길이가 $$수식$${a1}``rm km$$/수식$$인 호수가 있다. 어느 한 지점에서 A가 분속 " \
           "$$수식$${a2}``rm m$$/수식$$로 걷기 시작한 뒤 $$수식$${t1}$$/수식$$분 후에 B가 그 지점에서 " \
           "반대 방향으로 분속 $$수식$${a3}``rm m$$/수식$$로 걷는다고 할 때, B는 출발한지 몇 분 후에 " \
           "처음으로 A를 만나는가?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "B가 출발한 지 x분 후에 처음으로 A를 만난다고 하면\n" \
              "$$수식$${a2}({t1}+x)+{a3}x`=`{a4}$$/수식$$\n" \
              "$$수식$${b1}+{a2}x+{a3}x`=`{a4}$$/수식$$\n" \
              "$$수식$${b2}x`=`{b3}````````THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 B는 출발한 지 $$수식$${result}$$/수식$$분 후에 처음으로 A를 만난다.\n\n"


    while(1):
        a1 = np.random.randint(2,6)
        a2 = np.random.randint(3,10)*10
        t1 = np.random.randint(1,5)*5
        a3 = np.random.randint(3,10)*10

        a4 = a1*1000

        b1 = a2*t1
        b2 = a2+a3
        b3 = a4-b1

        if(a2-a3>0):
            if(b3%(b2)==0):
                if(b3/b2>8):
                    break


    result = math.floor(b3 / b2)

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}분" % (result)
        q2 = "{%s}분" % (result+2)
        q3 = "{%s}분" % (result+4)
        q4 = "{%s}분" % (result+6)
        q5 = "{%s}분" % (result+8)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}분" % (result-2)
        q2 = "{%s}분" % (result)
        q3 = "{%s}분" % (result+2)
        q4 = "{%s}분" % (result+4)
        q5 = "{%s}분" % (result+6)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}분" % (result-4)
        q2 = "{%s}분" % (result-2)
        q3 = "{%s}분" % (result)
        q4 = "{%s}분" % (result+2)
        q5 = "{%s}분" % (result+4)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}분" % (result-6)
        q2 = "{%s}분" % (result-4)
        q3 = "{%s}분" % (result-2)
        q4 = "{%s}분" % (result)
        q5 = "{%s}분" % (result+2)
        answer_num = "④"
    else:
        q1 = "{%s}분" % (result-8)
        q2 = "{%s}분" % (result-6)
        q3 = "{%s}분" % (result-4)
        q4 = "{%s}분" % (result-2)
        q5 = "{%s}분" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1,a2=a2,a3=a3,t1=t1,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,a2=a2,a3=a3,a4=a4,b1=b1,b2=b2,b3=b3,t1=t1,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_097():
    stem = "일정한 속력으로 달리는 기차가 길이가 $$수식$${a1}``rm m$$/수식$$인 철교를 완전히 " \
           "통과하는 데 $$수식$${t1}$$/수식$$초가 걸렸다. 또 길이가 $$수식$${a2}``rm m$$/수식$$인 터널을 " \
           "통과할 때는 $$수식$${t2}$$/수식$$초 동안 보이지 않았다. 이 기차의 길이는?\n" \
           "① $$수식$${q1}``rm m$$/수식$$\n" \
           "② $$수식$${q2}``rm m$$/수식$$\n" \
           "③ $$수식$${q3}``rm m$$/수식$$\n" \
           "④ $$수식$${q4}``rm m$$/수식$$\n" \
           "⑤ $$수식$${q5}``rm m$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "기차의 길이를 x m라 하면 이 기차가 길이가\n" \
              "$$수식$${a1}``rm m$$/수식$$인 철교를 완전히 통과할 때 이동한 거리는\n" \
              "$$수식$$({a1}+x) rm m$$/수식$$이고, 길이가 $$수식$${a2}``rm m$$/수식$$인 터널을 통과하느라\n" \
              "보이지 않는 동안 이동한 거리는 $$수식$$({a2}-x) rm m$$/수식$$ 이다.\n" \
              "이때 기차의 속력이 일정하므로\n" \
              "$$수식$${a1}+x over {t1}`=`{a2}-x over {t2}$$/수식$$\n" \
              "양변에 $$수식$${t3}$$/수식$$을 곱하면\n" \
              "$$수식$${t2}({a1}+x)`=`{t1}({a2}-x)$$/수식$$\n" \
              "$$수식$${b1}x`=`{b2}````````THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 기차의 길이는 $$수식$${result}``rm m$$/수식$$이다.\n\n"


    while(1):
        a1 = np.random.randint(30,40)*10
        t1 = np.random.randint(10,20)
        a2 = np.random.randint(30,40)*10
        t2 = np.random.randint(10,20)

        t3 = t1*t2

        b1 = t2+t1
        b2 = t1*a2 - t2*a1

        if(a1!=a2 and t1!=t2):
            if(b2%(b1)==0):
                if(b2/b1>40):
                    break


    result = math.floor(b2 / b1)

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result+10)
        q3 = "{%s}" % (result+20)
        q4 = "{%s}" % (result+30)
        q5 = "{%s}" % (result+40)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result-10)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result+10)
        q4 = "{%s}" % (result+20)
        q5 = "{%s}" % (result+30)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result-20)
        q2 = "{%s}" % (result-10)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result+10)
        q5 = "{%s}" % (result+20)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result-30)
        q2 = "{%s}" % (result-20)
        q3 = "{%s}" % (result-10)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result+10)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result-40)
        q2 = "{%s}" % (result-30)
        q3 = "{%s}" % (result-20)
        q4 = "{%s}" % (result-10)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1,a2=a2,t1=t1,t2=t2,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,a2=a2,b1=b1,b2=b2,t1=t1,t2=t2,t3=t3,result=result)

    return stem, answer, comment


def latterandexpress113_Stem_098():
    stem = "$$수식$${p1}$$/수식$$물 $$수식$${a1}``rm g$$/수식$$에 물 $$수식$${a2}``rm g$$/수식$$과 $$수식$${p1}````{a3}``rm g$$/수식$$을 " \
           "더 넣었더니 농도가 처음의 $$수식$${a4}$$/수식$$배가 되었다. 처음 $$수식$${p1}$$/수식$$물의 농도는?\n" \
           "① $$수식$${q1}%$$/수식$$\n" \
           "② $$수식$${q2}%$$/수식$$\n" \
           "③ $$수식$${q3}%$$/수식$$\n" \
           "④ $$수식$${q4}%$$/수식$$\n" \
           "⑤ $$수식$${q5}%$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "처음 $$수식$${p1}물$$/수식$$ 의 농도를 x%라 하면 나중 $$수식$${p1}$$/수식$$물의 양은\n" \
              "$$수식$${a1}`+`{a2}`+`{a3}`=`{b1}(rm g)$$/수식$$      이고, 농도는 {a4}x%이므로\n" \
              "$$수식$$x over 100`TIMES`{a1}`+`{a3}`=`{a4}x over 100`TIMES`{b1}$$/수식$$\n" \
              "$$수식$${b2}x+{a3}`=`{b3}x,````{b4}x`=`{a3}$$/수식$$\n" \
              "$$수식$$THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 처음 $$수식$${p1}$$/수식$$물의 농도는 $$수식$${result}$$/수식$$%이다.\n\n"


    while(1):
        p1 = ["설탕","소금"][np.random.randint(0,2)]

        a1 = np.random.randint(2,10)*100
        a2 = np.random.randint(100,200)
        a3 = np.random.randint(50,100)
        a4 = np.random.randint(2,8)

        b1 = a1+a2+a3
        b2 = math.floor(a1/100)
        b3 = math.floor(a4*b1/100)
        b4 = b3-b2

        if(b4!=0 and a3!=0):
            if(b1%100 == 0):
                if(a4*b1%100==0 and a3%b4 == 0):
                    if(a3/b4 > 4):
                        break


    result = math.floor(a3 / b4)

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result+1)
        q3 = "{%s}" % (result+2)
        q4 = "{%s}" % (result+3)
        q5 = "{%s}" % (result+4)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result-1)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result+1)
        q4 = "{%s}" % (result+2)
        q5 = "{%s}" % (result+3)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result-2)
        q2 = "{%s}" % (result-1)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result+1)
        q5 = "{%s}" % (result+2)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result-3)
        q2 = "{%s}" % (result-2)
        q3 = "{%s}" % (result-1)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result+1)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result-4)
        q2 = "{%s}" % (result-3)
        q3 = "{%s}" % (result-2)
        q4 = "{%s}" % (result-1)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1,a2=a2, a3=a3, a4=a4, p1=p1, q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,a2=a2, a3=a3, a4=a4, b1=b1,b2=b2, b3=b3, b4=b4, p1=p1, result=result)

    return stem, answer, comment


def latterandexpress113_Stem_099():
    stem = "물 $$수식$${a1}``rm g$$/수식$$과 소금 $$수식$${a2}``rm g$$/수식$$을 섞어서 만든 소금물에서 몇 $$수식$$rm g$$/수식$$의 물을 " \
           "증발시키면 농도가 처음 소금물의 농도의 $$수식$${a3}$$/수식$$배가 되는가?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "처음 소금물의 농도는 $$수식$${a2} over {a1}+{a2}`TIMES 100 `=`{b1}(%)이므로$$/수식$$\n" \
              "물을 증발시킨 후의 소금물의 농도는 $$수식$${b2}%$$/수식$$   이다.\n" \
              "증발시키는 물의 양을 xg이라 하면 $$수식$${b2}%$$/수식$$ 의 소금물의 양은 $$수식$$({b3}-x) rm g$$/수식$$   이고,\n" \
              "이 때 소금의 양은 변하지 않으므로\n" \
              "$$수식$${a2}`=`{a2} over 100` TIMES`({b3}-x)$$/수식$$\n" \
              "양변에 100을 곱하면\n" \
              "$$수식$${c1}`=`{c2}-{c3}x$$/수식$$\n" \
              "$$수식$${c3}x`=`{c4}````````THEREFORE~x`=`{result}$$/수식$$\n" \
              "따라서 증발시키는 물의 양은 $$수식$${result}``rm g$$/수식$$ 이다.\n\n"


    while(1):
        a1 = np.random.randint(10,50)*10
        a2 = np.random.randint(1,10)*10
        a3 = np.random.randint(2,5)
        aa1 = a1+a2

        b1 = math.floor(a2*100/aa1)
        b2 = b1*a3
        b3 = aa1

        c1 = a2*100
        c2 = a2*aa1
        c3 = a2
        c4 = c2-c1

        if(aa1%100==0):
            if(c4!=0 and c3!=0):
                if(b1*a3<70):
                    if(a2*100%(a1+a2)==0):
                        break


    result = math.floor(c4 / c3)

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}``rm g" % (result)
        q2 = "{%s}``rm g" % (result+5)
        q3 = "{%s}``rm g" % (result+10)
        q4 = "{%s}``rm g" % (result+15)
        q5 = "{%s}``rm g" % (result+20)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}``rm g" % (result-5)
        q2 = "{%s}``rm g" % (result)
        q3 = "{%s}``rm g" % (result+5)
        q4 = "{%s}``rm g" % (result+10)
        q5 = "{%s}``rm g" % (result+15)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}``rm g" % (result-2*5)
        q2 = "{%s}``rm g" % (result-1*5)
        q3 = "{%s}``rm g" % (result)
        q4 = "{%s}``rm g" % (result+1*5)
        q5 = "{%s}``rm g" % (result+2*5)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}``rm g" % (result-15)
        q2 = "{%s}``rm g" % (result-10)
        q3 = "{%s}``rm g" % (result-5)
        q4 = "{%s}``rm g" % (result)
        q5 = "{%s}``rm g" % (result+5)
        answer_num = "④"
    else:
        q1 = "{%s}``rm g" % (result-20)
        q2 = "{%s}``rm g" % (result-15)
        q3 = "{%s}``rm g" % (result-10)
        q4 = "{%s}``rm g" % (result-5)
        q5 = "{%s}``rm g" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1,a2=a2, a3=a3, q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,a2=a2, a3=a3, b1=b1,b2=b2, b3=b3, c1=c1, c2=c2, c3=c3, c4=c4, result=result)

    return stem, answer, comment


def latterandexpress113_Stem_100():
    stem = "두 제빵사 A,B가 $$수식$${t1}$$/수식$$분 동안 $$수식$${w1}$$/수식$$을 만들면 A가 B보다 $$수식$${a1}$$/수식$$개를 더 만든다고 한다. " \
           "또 A가 $$수식$${t2}$$/수식$$분 동안 만든 $$수식$${w1}$$/수식$$의 개수가 B가 $$수식$${t3}$$/수식$$분 동안 만든 " \
           "$$수식$${w1}$$/수식$$의 개수의 $$수식$${a2}$$/수식$$배라 할 때, A와 B가 1시간 동안 만들 수 있는 " \
           "$$수식$${w1}$$/수식$$의 개수의 합은?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "B가 $$수식$${t1}$$/수식$$분 동안 만든 $$수식$${w1}$$/수식$$ 의 개수를 x라 하면\n" \
              "A가 $$수식$${t1}$$/수식$$분 동안 만든 $$수식$${w1}$$/수식$$ 의 개수는 x+$$수식$${a1}$$/수식$$이므로\n" \
              "A가 $$수식$${t2}$$/수식$$분 동안 만든 $$수식$${w1}$$/수식$$ 의 개수는 $$수식$${b1}(x+{a1}),$$/수식$$\n" \
              "B가 $$수식$${t3}$$/수식$$분 동안 만든 $$수식$${w1}$$/수식$$ 의 개수는 $$수식$${b2}x$$/수식$$이다.\n" \
              "즉, $$수식$${b1}(x+{a1})`=`{a2} TIMES {b2}x이므로$$/수식$$\n" \
              "$$수식$${b1}x+{b3}`=`{b4}x,````{b5}x`=`{b3}````````THEREFORE~x`=`{b6}$$/수식$$\n" \
              "따라서 A,B는 $$수식$${t1}$$/수식$$분 동안 각각 $$수식$${c1}개,{c2}개$$/수식$$의 $$수식$${w1}$$/수식$$ 을 만들 수 " \
              "있으므로 1시간 동안 만들 수 있는 $$수식$${w1}$$/수식$$ 의 개수의 합은\n" \
              "$$수식$${c3}TIMES({c1}+{c2})`=`{result}$$/수식$$\n\n"


    while(1):
        t1 = np.random.randint(2,10)
        a1 = np.random.randint(1,6)*10
        t2 = np.random.randint(1,6)*10
        t3 = np.random.randint(1,6)*10
        a2 = np.random.randint(2,5)
        w1 = ["도넛", "식빵", "쿠키", "케잌"][np.random.randint(0,4)]

        b1 = math.floor(t2/t1)
        b2 = math.floor(t3/t1)
        b3 = b1*a1
        b4 = a2*b2
        b5 = b4-b1
        if(b5!=0): b6 = math.floor(b3/b5)
        else: b6 = 0

        c1 = b6 + a1
        c2 = b6
        c3 = math.floor(60/t1)
        result = c3*(c1+c2)

        if(t2 % t1 == 0 and t3 % t1 == 0 and t2<t3):
            if(b4-b1>0 and b3%b5==0):
                if(60 % a1 == 0 and c3<60):
                    break

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}" % (result)
        q2 = "{%s}" % (result+5)
        q3 = "{%s}" % (result+10)
        q4 = "{%s}" % (result+15)
        q5 = "{%s}" % (result+20)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}" % (result-5)
        q2 = "{%s}" % (result)
        q3 = "{%s}" % (result+5)
        q4 = "{%s}" % (result+10)
        q5 = "{%s}" % (result+15)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}" % (result-2*5)
        q2 = "{%s}" % (result-1*5)
        q3 = "{%s}" % (result)
        q4 = "{%s}" % (result+1*5)
        q5 = "{%s}" % (result+2*5)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}" % (result-15)
        q2 = "{%s}" % (result-10)
        q3 = "{%s}" % (result-5)
        q4 = "{%s}" % (result)
        q5 = "{%s}" % (result+5)
        answer_num = "④"
    else:
        q1 = "{%s}" % (result-20)
        q2 = "{%s}" % (result-15)
        q3 = "{%s}" % (result-10)
        q4 = "{%s}" % (result-5)
        q5 = "{%s}" % (result)
        answer_num = "⑤"


    stem = stem.format(a1=a1,a2=a2, t1=t1,t2=t2,t3=t3,w1=w1, q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,a2=a2, t1=t1,t2=t2,t3=t3,w1=w1, b1=b1,b2=b2, b3=b3, b4=b4, b5=b5, b6=b6, c1=c1, c2=c2, c3=c3, result=result)

    return stem, answer, comment


def latterandexpress113_Stem_101():
    stem = "$$수식$${a1}$$/수식$$시와 $$수식$${a2}$$/수식$$시 사이에 시계의 시침과 분침이 서로 반대 방향으로 일직선을 " \
           "이룰 때의 시각은?\n" \
           "① $$수식$${q1}$$/수식$$\n" \
           "② $$수식$${q2}$$/수식$$\n" \
           "③ $$수식$${q3}$$/수식$$\n" \
           "④ $$수식$${q4}$$/수식$$\n" \
           "⑤ $$수식$${q5}$$/수식$$\n"
    answer = "(정답)\n{answer_num}"
    comment = "(해설)\n" \
              "$$수식$${a1}$$/수식$$시 x분에 시침과 분침이 이루는 각의 크기가 180°가 된다고 하면\n" \
              "(분침이 12시를 기준으로 움직인 각도) = 6°x\n" \
              "(시침이 12시를 기준으로 움직인 각도) = 30°$$수식$$TIMES {a1}`+`0.5°x$$/수식$$\n" \
              "이때 시침과 분침이 이루는 각의 크기가 180°이므로\n" \
              "$$수식$$({b1}°+0.5°x)-6°x`=`180°$$/수식$$\n" \
              "$$수식$$-5.5x`=`{b2}````````THEREFORE~x`=`{b3} over 11$$/수식$$\n" \
              "따라서 구하는 시각은 $$수식$${a1}시``{b3} over 11`분이다.$$/수식$$\n\n"


    while(1):
        a1 = np.random.randint(1,12)
        a2 = a1+1

        b1 = 30*a1
        b2 = 180-b1
        b3 = b2*(-2)

        if(b2 < 0):
            break

    sol = np.random.randint(0, 5)

    if (sol == 0):
        q1 = "{%s}시``{%s} over 11`분" % (a1,b3)
        q2 = "{%s}시``{%s} over 11`분" % (a1,b3+10)
        q3 = "{%s}시``{%s} over 11`분" % (a1,b3+20)
        q4 = "{%s}시``{%s} over 11`분" % (a1,b3+30)
        q5 = "{%s}시``{%s} over 11`분" % (a1,b3+40)
        answer_num = "①"
    elif (sol == 1):
        q1 = "{%s}시``{%s} over 11`분" % (a1,b3-10)
        q2 = "{%s}시``{%s} over 11`분" % (a1,b3)
        q3 = "{%s}시``{%s} over 11`분" % (a1,b3+10)
        q4 = "{%s}시``{%s} over 11`분" % (a1,b3+20)
        q5 = "{%s}시``{%s} over 11`분" % (a1,b3+30)
        answer_num = "②"
    elif (sol == 2):
        q1 = "{%s}시``{%s} over 11`분" % (a1,b3-20)
        q2 = "{%s}시``{%s} over 11`분" % (a1,b3-10)
        q3 = "{%s}시``{%s} over 11`분" % (a1,b3)
        q4 = "{%s}시``{%s} over 11`분" % (a1,b3+10)
        q5 = "{%s}시``{%s} over 11`분" % (a1,b3+20)
        answer_num = "③"
    elif (sol == 3):
        q1 = "{%s}시``{%s} over 11`분" % (a1,b3-30)
        q2 = "{%s}시``{%s} over 11`분" % (a1,b3-20)
        q3 = "{%s}시``{%s} over 11`분" % (a1,b3-10)
        q4 = "{%s}시``{%s} over 11`분" % (a1,b3)
        q5 = "{%s}시``{%s} over 11`분" % (a1,b3+10)
        answer_num = "④"
    else:
        q1 = "{%s}시``{%s} over 11`분" % (a1,b3-40)
        q2 = "{%s}시``{%s} over 11`분" % (a1,b3-30)
        q3 = "{%s}시``{%s} over 11`분" % (a1,b3-20)
        q4 = "{%s}시``{%s} over 11`분" % (a1,b3-10)
        q5 = "{%s}시``{%s} over 11`분" % (a1,b3)
        answer_num = "⑤"


    stem = stem.format(a1=a1,a2=a2,q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
    answer = answer.format(answer_num=answer_num)
    comment = comment.format(a1=a1,a2=a2, b1=b1,b2=b2, b3=b3)

    return stem, answer, comment

