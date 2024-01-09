import numpy as np

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


def statistics326_Stem_001():
    stem = "$$수식$$4$$/수식$$개의 변량 $$수식$$a, b, c, d$$/수식$$의 평균이 $$수식$${q1}$$/수식$$일 때, $$수식$$6$$/수식$$개의 변량 $$수식$${q2}, a, b, c, d, {q3}$$/수식$$의 평균은?\n" \
           "① $$수식$${s1}$$/수식$$\n" \
           "② $$수식$${s2}$$/수식$$\n" \
           "③ $$수식$${s3}$$/수식$$\n" \
           "④ $$수식$${s4}$$/수식$$\n" \
           "⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a, b, c, d$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{a + b + c + d}} over {{4}}= {q1}$$/수식$$에서\n" \
              "$$수식$$a + b + c + d = {c1}$$/수식$$\n" \
              "따라서 $$수식$$6$$/수식$$개의 변량 $$수식$${q2}, a, b, c, d, {q3}$$/수식$$의 평균은\n" \
              "$$수식$${{{q2} + a + b + c + d + {q3}}} over {{6}} = {{{c2} + {c1}}} over {{6}} = {c3}$$/수식$$\n\n"

    s_candidates = [1,1,1,1,1]
    while (not (cand_check(s_candidates))):  #보기가 중복되지 않을 때까지 반복
        a1 = np.random.randint(14, 50)
    
        q1 = np.random.randint(4, ((a1 - 10) * 6) // 4)
        q2 = np.random.randint(1, (a1 * 6 - q1 * 4) // 2 - 1)
        q3 = a1 * 6 - q1 * 4 - q2
        
        c1 = q1 * 4
        c2 = q2 + q3
        c3 = a1
        
        s_candidates = [q2, (q2 + a1) // 2, a1, (a1 + q3) // 2, q3]
    
    s_candidates, correct_idx =  cand_shuffle(s_candidates, a1)
    s1, s2, s3, s4, s5 = s_candidates
    
    
    stem = stem.format(q1=q1, q2=q2, q3=q3, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, c1=c1, c2=c2, c3=c3)

    return stem, answer, comment


def statistics326_Stem_002():
    stem = "다음 자료는 {q1} 모둠 학생들의 {q2} 성적을 조사하여 나타낸 것이다. 이 모둠의 {q2} 성적의 평균을 구하시오.\n" \
            "$$표$$$$수식$$ {s1}, {s2}, {s3}, {s4}, {s5} $$/수식$$(단위 : 점)$$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$점\n"
    comment = "(해설)\n" \
              "({q1} 모둠 학생들의 {q2} 성적의 평균)\n" \
              "$$수식$$= {{ {c1} + {c2} + {c3} + {c4} + {c5}}} over {{5}} = {c6} over {{5}} = {c7}$$/수식$$(점)\n\n"

    q1 = ['영준이', '철수', '영희', '선우'][np.random.randint(0, 4)]
    q2 = ['영어', '과학', '국어', '수학'][np.random.randint(0, 4)]

    s_candidates = [1,1,1,1,1]
    while (not (cand_check(s_candidates))):  #보기가 중복되지 않을 때까지 반복
        c1 = np.random.randint(1, 100)
        c2 = np.random.randint(1, 100)
        c3 = np.random.randint(1, 100)
        c4 = np.random.randint(1, 100)
        a1 = (c1 + c2 + c3 + c4) // 4 + 2
        c5 = a1 * 5 - c1 - c2 - c3 - c4
        c6 = c1 + c2 + c3 + c4 + c5
        c7 = a1
        
        s_candidates = [c1, c2, c3, c4, c5]
    
    s_candidates, correct_idx =  cand_shuffle(s_candidates)
    s1, s2, s3, s4, s5 = s_candidates
    
    
    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7)

    return stem, answer, comment


def statistics326_Stem_003():
    stem = "$$수식$$3$$/수식$$개의 변량 $$수식$$a, b, c$$/수식$$의 평균이 $$수식$${q1}$$/수식$$일 때, $$수식$$5$$/수식$$개의 변량 $$수식$${q2}, a, b, c, {q3}$$/수식$$의 평균은?\n" \
           "① $$수식$${s1}$$/수식$$\n" \
           "② $$수식$${s2}$$/수식$$\n" \
           "③ $$수식$${s3}$$/수식$$\n" \
           "④ $$수식$${s4}$$/수식$$\n" \
           "⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a, b, c$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{a + b + c}} over {{3}}= {q1}$$/수식$$에서\n" \
              "$$수식$$a + b + c = {c1}$$/수식$$" \
              "따라서 $$수식$${q2}, a, b, c, {q3}$$/수식$$의 평균은\n" \
              "$$수식$${{{q2} + a + b + c + {q3}}} over {{5}} = {{{c2} + {c1}}} over {{5}} = {c3}$$/수식$$\n\n"

    s_candidates = [1,1,1,1,1]
    while (not (cand_check(s_candidates))):  #보기가 중복되지 않을 때까지 반복
        a1 = np.random.randint(14, 50)
    
        q1 = np.random.randint(3, ((a1 - 10) * 5) // 3)
        q2 = np.random.randint(1, (a1 * 5 - q1 * 3) // 2 - 1)
        q3 = a1 * 5 - q1 * 3 - q2
        
        c1 = q1 * 3
        c2 = q2 + q3
        c3 = a1
        
        s_candidates = [q2, (q2 + a1) // 2, a1, (a1 + q3) // 2, q3]
    
    s_candidates, correct_idx =  cand_shuffle(s_candidates, a1)
    s1, s2, s3, s4, s5 = s_candidates
    
    
    stem = stem.format(q1=q1, q2=q2, q3=q3, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, c1=c1, c2=c2, c3=c3)

    return stem, answer, comment

def statistics326_Stem_004():
    stem = "다섯 개의 수 $$수식$$a, b, c, d, e$$/수식$$의 평균이 $$수식$${q1}$$/수식$$일 때, $$수식$$3a - 5$$/수식$$, $$수식$$3b - 5$$/수식$$, $$수식$$3c - 5$$/수식$$, $$수식$$3d - 5$$/수식$$, $$수식$$3e - 5$$/수식$$의 평균은?\n" \
           "① $$수식$${s1}$$/수식$$\n" \
           "② $$수식$${s2}$$/수식$$\n" \
           "③ $$수식$${s3}$$/수식$$\n" \
           "④ $$수식$${s4}$$/수식$$\n" \
           "⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a, b, c, d, e$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{a + b + c + d + e}} over {{5}}= {q1}$$/수식$$에서\n" \
              "$$수식$$a + b + c + d + e = {c1}$$/수식$$\n" \
              "따라서 $$수식$$3a - 5$$/수식$$, $$수식$$3b - 5$$/수식$$, $$수식$$3c - 5$$/수식$$, $$수식$$3d - 5$$/수식$$, $$수식$$3e - 5$$/수식$$의 평균은\n" \
              "$$수식$${{(3a - 5) + (3b - 5) + .... + (3e - 5)}} over {{5}}$$/수식$$\n" \
              "$$수식$$= {{3(a + b + c + e + d) - 5 times 5}} over {{5}}$$/수식$$\n" \
              "$$수식$$= {{3 times {c1} - 25}} over {{5}} = {c2} over {{5}} = {c3}$$/수식$$\n\n"


    q1 = np.random.randint(10, 60)
    c1 = q1 * 5
    c2 = 3 * c1 - 25
    c3 = round(c2 / 5)
    
    a1 = c3

    s3 = np.random.randint(a1 - 2, a1 + 2)
    s_candidates = [s3 - 2, s3 - 1, s3, s3 + 1, s3 + 2]
    
    s1, s2, s3, s4, s5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break
    
    
    stem = stem.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3)

    return stem, answer, comment


def statistics326_Stem_005():
    stem = "{q1}가 중간고사 $$수식$${q2}$$/수식$$과목 성적의 평균을 구하는데 $$수식$${q3}$$/수식$$점인 어느 과목의 점수를 잘못 보아 실제보다 평균이 $$수식$${q4}$$/수식$$점 높게 나왔다. 몇 점으로 잘못 보았는가?\n" \
           "① $$수식$${s1}$$/수식$$\n" \
           "② $$수식$${s2}$$/수식$$\n" \
           "③ $$수식$${s3}$$/수식$$\n" \
           "④ $$수식$${s4}$$/수식$$\n" \
           "⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$${q3}$$/수식$$점을 받은 과목을 제외한 {q2}과목의 총점을 $$수식$$A$$/수식$$점이라 하고,\n$$수식$${q3}$$/수식$$점을 $$수식$$x$$/수식$$점으로 잘못 보았다고 하면 \n" \
              "$$수식$${{A + {q3}}} over {q2} + {q4} = {{A + x}} over {q2}$$/수식$$에서\n" \
              "$$수식$$A + {q3} + {c1} = A + x$$/수식$$\n" \
              "따라서 $$수식$$x = {c2}$$/수식$$,  그러므로 $$수식$${c2}$$/수식$$점으로 잘못 보았다.\n\n "

    q1 = ['영준이', '철수', '영희', '선우'][np.random.randint(0, 4)]

    s_candidates = [1,1,1,1,1]
    while (not (cand_check(s_candidates))):  #보기가 중복되지 않을 때까지 반복
        q2 = np.random.randint(5, 15)
        q4 = np.random.randint(1, 5)
        q3 = np.random.randint(1, 100 - q2 * q4)
        a1 = q3 + q2 * q4
               
        c1 = q2 * q4
        c2 = q3 + c1

        s3 = np.random.randint(a1 - 2, a1 + 2)
        s_candidates = [s3 - 2, s3 - 1, s3, s3 + 1, s3 + 2]

    s1, s2, s3, s4, s5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break
    
    
    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q2=q2, q3=q3, q4=q4, c1=c1, c2=c2)

    return stem, answer, comment


def statistics326_Stem_006():
    stem = "{q1}네 반은 남학생이 $$수식$${q2}$$/수식$$명, 여학생이 $$수식$${q3}$$/수식$$명이다. 여학생의 {q4} 성적의 평균이 $$수식$${q5}$$/수식$$점, {q1}네 반 전체의 {q4} 성적의 평균이 $$수식$${q6}$$/수식$$점일 때, 남학생의 {q4} 성적의 평균을 구하시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$점\n"
    comment = "(해설)\n" \
              "남학생의 {q4} 성적의 평균을 $$수식$$x$$/수식$$점이라 하면\n" \
              "$$수식$${{ {q5} times {q3} + x times {q2} }} over {{ {q3} + {q2} }} = {q6}$$/수식$$\n" \
              "$$수식$${c1} + {q2}x = {c2}$$/수식$$, $$수식$${q2}x = {c3}$$/수식$$ \n" \
              "그러므로 $$수식$$x = {c4}$$/수식$$\n" \
              "따라서 남학생의 {q4} 성적의 평균은 $$수식$${c4}$$/수식$$점이다.\n\n"

    q1 = ['영준이', '재영이', '영희', '선우'][np.random.randint(0, 4)]
    q4 = ['영어', '과학', '국어', '수학', '체육'][np.random.randint(0, 5)]

    q2 = np.random.randint(4, 25)
    q3 = np.random.randint(4, 25)
    r1 = np.random.randint(0, 2)
    r2 = (r1 + 1) % 2
    t1 = np.random.randint(50, 100 - q2 - q3)

    q5 = [t1, t1 + q2 + q3][r1]
    a1 = [t1, t1 + q2 + q3][r2]
    q6 = ((q5 * q3) + (a1 * q2)) // (q2 + q3)

    c1 = q5 * q3
    c2 = q6 * (q2 + q3)
    c3 = c2 - c1
    c4 = c3 // q2
    
    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, c1=c1, c2=c2, c3=c3, c4=c4)

    return stem, answer, comment


def statistics326_Stem_007():
    stem = "$$수식$$4$$/수식$$개의 변량 $$수식$${q1}, {q2}, x, {q3}$$/수식$$의 평균이 $$수식$$3$$/수식$$개의 변량 $$수식$${q1}, {q2}, x$$/수식$$의 평균보다 클 때, 이를 만족하는 자연수 $$수식$$x$$/수식$$의 값의 개수는?\n" \
           "① $$수식$${s1}$$/수식$$\n" \
           "② $$수식$${s2}$$/수식$$\n" \
           "③ $$수식$${s3}$$/수식$$\n" \
           "④ $$수식$${s4}$$/수식$$\n" \
           "⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$${{ {q1} + {q2} + x }} over {{3}} &lt; {{ {q1} + {q2} + x + {q3} }} over {{4}}$$/수식$$\n" \
              "에서 $$수식$${{ {c1} + x }} over {{3}} &lt; {{ {c2} + x }} over {{4}}$$/수식$$" \
              "양변에 $$수식$$12$$/수식$$를 곱하면\n" \
              "$$수식$${c3} + 4x &lt; {c4} + 3x $$/수식$$\n" \
              "따라서 $$수식$$ x &lt; {c5} $$/수식$$\n" \
              "이를 만족시키는 자연수 $$수식$$x$$/수식$$는 $$수식$$1, 2, 3, CDOTS$$/수식$$, $$수식$${c6}$$/수식$$의 $$수식$${c6}$$/수식$$개이다.\n\n"

    s_candidates = [1,1,1,1,1]
    while (not (cand_check(s_candidates))):  #보기가 중복되지 않을 때까지 반복
        q1 = np.random.randint(1, 30)
        q2 = np.random.randint(q1 + 1, 31)
        q3 = np.random.randint(q2 + 1, 32)
                
        c1 = q1 + q2
        c2 = q1 + q2 + q3
        c3 = c1 * 4
        c4 = c2 * 3
        c5 = c4 - c3
        c6 = c5 - 1
        
        a1 = c6
                
        s_candidates = [a1, q3, q3 - q1, q1 + q2, a1 - 2]

    s_candidates, correct_idx =  cand_shuffle(s_candidates, a1)
    s1, s2, s3, s4, s5 = s_candidates
    
    
    stem = stem.format(q1=q1, q2=q2, q3=q3, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)

    return stem, answer, comment

def statistics326_Stem_008():
    stem = "서로 다른 $$수식$${q1}$$/수식$$개의 변량 중 가장 큰 변량을 제외한 $$수식$${q2}$$/수식$$개의 변량의 평균은 $$수식$${q3}$$/수식$$이고, 가장 작은 변량을 제외한 $$수식$${q2}$$/수식$$개의 변량의 평균은 $$수식$${q4}$$/수식$$이다. 가장 큰 변량과 가장 작은 변량의 합이 $$수식$${q5}$$/수식$$일 때, 서로 다른 $$수식$${q1}$$/수식$$개의 변량의 평균을 나타내시오.\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "가장 큰 변량을 $$수식$$a$$/수식$$, 가장 작은 변량을 $$수식$$b$$/수식$$라 하고\n" \
              "$$수식$$a, b$$/수식$$를 포함한 $$수식$${q1}$$/수식$$개의 변량의 총합을 $$수식$$X$$/수식$$라 하면\n" \
              "$$수식$$ X = a + {q2} times {q3} CDOTS (ㄱ)$$/수식$$\n" \
              "$$수식$$ X = b + {q2} times {q4} CDOTS (ㄴ)$$/수식$$\n" \
              "$$수식$$ (ㄱ) - (ㄴ) $$/수식$$을 하면 $$수식$$a - b = {c1}$$/수식$$ 이고\n" \
              "$$수식$$a + b = {q5}$$/수식$$이므로 연립하여 풀면\n" \
              "$$수식$$a = {c2}$$/수식$$, $$수식$$b = {c3}$$/수식$$\n" \
              "따라서 $$수식$${q1}$$/수식$$개의 변량의 평균은\n" \
              "$$수식$${{ {c2} + {q2} times {q3} }} over {{ {q1} }} = {{ {c4} }} over {{ {q1} }} = {c5}$$/수식$$\n\n"

    q4 = np.random.randint(20, 100)
    q3 = np.random.randint(11, q4 - 4)
    q1 = [4, 5, 8, 20, 25][np.random.randint(0, 5)]
    q2 = q1 - 1
    c1 = q2 * (q4 - q3)

    a = np.random.randint(max(q4, c1 + 1), q3 + c1 - 1)
    b = a - c1
    q5 = a + b

    c1 = q2 * (q4 - q3)
    c2 = (c1 + q5) // 2
    c3 = (q5 - c1) // 2
    c4 = c2 + (q2 * q3)
    c5 = c4 / q1
    if round(c5) == c5:
        c5 = round(c5)
    a1 = c5       
    
    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)

    return stem, answer, comment


def statistics326_Stem_009():
    stem = "다음은 {q1}네 반의 가 모둠과 나 모둠의 학생들이 가지고 있는 {q2}의 개수를 조사하여 나타낸 것이다. 가 모둠의 중앙값을 $$수식$$a$$/수식$$개, 나 모둠의 중앙값을 $$수식$$b$$/수식$$개라 할 때, $$수식$$a+b$$/수식$$의 값을 구하시오.\n" \
            "$$표$$[가 모둠]$$수식$$ {s1}, {s2}, {s3}, {s4}, {s5}, {s6}, {s7}, {s8}, {s9}, {s10}$$/수식$$\n [나 모둠] $$수식$${s11}, {s12}, {s13}, {s14}, {s15}, {s16}, {s17}, {s18}, {s19}$$/수식$$ (단위 : 개)$$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "가 모둠의 {q2}의 개수를 크기순으로 나열하면\n" \
              "$$수식$${c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}, {c8}, {c9}, {c10}$$/수식$$\n" \
              "이므로 가 모둠의 중앙값은 $$수식$$a ={{ {c5} + {c6} }} over {{2}} = {cc1}$$/수식$$(개) \n" \
              "나 모둠의 {q2}의 개수를 크기순으로 나열하면\n" \
              "$$수식$${c11}, {c12}, {c13}, {c14}, {c15}, {c16}, {c17}, {c18}, {c19}$$/수식$$\n" \
              "이므로 나 모둠의 중앙값은 $$수식$$b = {c15}$$/수식$$(개) \n" \
              "따라서 $$수식$$a + b ={cc2}$$/수식$$\n\n"

    q1 = ['영준이', '재영이', '영희', '선우', '태인이'][np.random.randint(0, 5)]
    q2 = ['필기구', '공책', '책'][np.random.randint(0, 3)]

    [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10] = [np.random.randint(1, 20) for r in range(10)]
    [s11, s12, s13, s14, s15, s16, s17, s18, s19] = [np.random.randint(1, 20) for r in range(9)]
    t1 = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
    t2 = [s11, s12, s13, s14, s15, s16, s17, s18, s19]
    t1.sort()
    t2.sort()
    [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10] = t1
    [c11, c12, c13, c14, c15, c16, c17, c18, c19] = t2
    
    cc1 = (c5 + c6) / 2
    if round(cc1) == cc1:
        cc1 = round(cc1)
    cc2 = cc1 + c15
    a1 = cc2
    
    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10, s11=s11, s12=s12, s13=s13, s14=s14, s15=s15, s16=s16, s17=s17, s18=s18, s19=s19)
    answer = answer.format(a1=a1)
    comment = comment.format(q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12, c13=c13, c14=c14, c15=c15, c16=c16, c17=c17, c18=c18, c19=c19, cc1=cc1, cc2=cc2)

    return stem, answer, comment


def statistics326_Stem_010():
    stem = "다음 자료는 학생 $$수식$$9$$/수식$$명의 {q1}를 조사하여 나타낸 것이다. {q1}의 중앙값을 구하시오.\n" \
            "$$표$$$$수식$${s1}, {s2}, {s3}, {s4}, {s5}, {s6}, {s7}, {s8}, {s9}$$/수식$$ (단위 : 회)$$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$회\n"
    comment = "(해설)\n" \
              "주어진 자료의 변량을 작은 값부터 크기순으로 나열하면\n" \
              "$$수식$${c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}, {c8}, {c9}$$/수식$$\n" \
              "변량의 개수가 $$수식$$9$$/수식$$이므로 중앙값은 $$수식$$5$$/수식$$번째 변량인 $$수식$${cc1}$$/수식$$회이다.\n\n"

    q1 = ['발표 횟수', '지각 횟수', '출석 횟수'][np.random.randint(0, 3)]

    [s1, s2, s3, s4, s5, s6, s7, s8, s9] = [np.random.randint(1, 20) for r in range(9)]
    t1 = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
    t1.sort()
    [c1, c2, c3, c4, c5, c6, c7, c8, c9] = t1
    
    cc1 = c5
    a1 = cc1
    
    stem = stem.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9)
    answer = answer.format(a1=a1)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, cc1=cc1)

    return stem, answer, comment


def statistics326_Stem_011():
    stem = "다음 자료는 어느 {q1}들의 한 주 동안의 {q2} 수를 조사하여 나타낸 것이다. 이 자료의 중앙값은?\n" \
            "$$표$$$$수식$${s1}, {s2}, {s3}, {s4}, {s5}, {s6}, {s7}$$/수식$$ (단위 : 개)$$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$개\n"
    comment = "(해설)\n" \
              "주어진 자료의 변량을 작은 값부터 크기순으로 나열하면\n" \
              "$$수식$${c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}$$/수식$$\n" \
              "변량의 개수가 이므로 중앙값은 $$수식$$4$$/수식$$번째 변량인 $$수식$${cc1}$$/수식$$회이다.\n\n"

    q1, q2 = [['야구팀 타자', '안타'],['축구팀 선수', '골'],['농구팀 선수', '골']][np.random.randint(0, 3)]
    
    t1 = [np.random.randint(1, 20) for r in range(7)];
    [s1, s2, s3, s4, s5, s6, s7] = t1
    t1.sort()
    [c1, c2, c3, c4, c5, c6, c7] = t1
    
    cc1 = c4
    a1 = cc1

    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7)
    answer = answer.format(a1=a1)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, cc1=cc1)

    return stem, answer, comment



def statistics326_Stem_012():
    stem = "다음 자료는 학생 9명의 {q1} 조사하여 나타낸 것이다. 이 자료의 최빈값은?\n" \
            "$$표$$$$수식$${s1}, {s2}, {s3}, {s4}, {s5}, {s6}, {s7}, {s8}, {s9}$$/수식$$ (단위 : {q2})$$/표$$\n" \
            "① $$수식$${s10}$$/수식$$\n" \
            "② $$수식$${s11}$$/수식$$\n" \
            "③ $$수식$${s12}$$/수식$$\n" \
            "④ $$수식$${s13}$$/수식$$\n" \
            "⑤ $$수식$${s14}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "자료에서 가장 많이 나타나는 값이 $$수식$${c1}$$/수식$${q2}이므로 최빈값은 $$수식$${c1}$$/수식$${q2}이다. \n\n"

    q1, q2 = [['사용 중인 휴대폰 메모리의 용량을', 'GB'],['최근 한 달간 구매한 물건의 개수를', '개'],['한 달 동안 읽은 책의 페이지 수를', '페이지']][np.random.randint(0, 3)]
    
    t_list1 = [32, 64, 128, 256, 512]
    t_list2 = [3, 2, 2, 1, 1]
    np.random.shuffle(t_list2)
    a1 = t_list2.index(3)
    t_list3 = list()
    for i in range(5):
        while (t_list2[i] > 0):
            t_list3.append(t_list1[i])
            t_list2[i] -= 1
    np.random.shuffle(t_list3)
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = t_list3
    s10, s11, s12, s13, s14 = t_list1
    
    c1 = t_list1[a1]

    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10, s11=s11, s12=s12, s13=s13, s14=s14)
    answer = answer.format(a1=answer_dict[a1])
    comment = comment.format(c1=c1, q2=q2)

    return stem, answer, comment

def statistics326_Stem_013():
    stem = "다음은 $$수식$$1$$/수식$$ {q1}{j1} $$수식$$2$$/수식$$ {q1}의 {q2} 성적을 조사하여 나타낸 것이다. $$수식$$1$$/수식$$ {q1}의 최빈값의 개수를 $$수식$$a$$/수식$$, $$수식$$2$$/수식$$ {q1}의 최빈값의 개수를 $$수식$$b$$/수식$$라 할 때, $$수식$$a + b$$/수식$$의 값을 구하시오.\n" \
            "$$표$$ $$수식$$1$$/수식$$ {q1} :$$수식$$ {s1}, {s2}, {s3}, {s4}, {s5}, {s6}, {s7}, {s8}, {s9}, {s10},$$/수식$$\n $$수식$${s11}, {s12}, {s13}, {s14}, {s15}, {s16}, {s17}, {s18}, {s19}, {s20}$$/수식$$ (단위 : 점)$$/표$$\n" \
            "$$표$$ $$수식$$2$$/수식$$ {q1} :$$수식$$ {ss1}, {ss2}, {ss3}, {ss4}, {ss5}, {ss6}, {ss7}, {ss8}, {ss9}, {ss10},$$/수식$$\n$$수식$$ {ss11}, {ss12}, {ss13}, {ss14}, {ss15}, {ss16}, {ss17}, {ss18}, {ss19}, {ss20} $$/수식$$(단위 : 점)$$/표$$\n"            
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$1$$/수식$$ {q1}에서 가장 많이 나타나는 점수는 $$수식$${c1}$$/수식$$점, $$수식$${c2}$$/수식$$점, $$수식$${c3}$$/수식$$점이 각각 $$수식$${c4}$$/수식$$번씩이므로 $$수식$$a = {c5}$$/수식$$\n" \
              "$$수식$$2$$/수식$$ {q1}에서 가장 많이 나타나는 점수는 $$수식$${c6}$$/수식$$점, $$수식$${c7}$$/수식$$점, $$수식$${c8}$$/수식$$점이 각각 $$수식$${c9}$$/수식$$번씩이므로 $$수식$$b = {c10}$$/수식$$\n" \
              "따라서 $$수식$$a + b = {c5} + {c10} = {c11}$$/수식$$\n\n"

    q1 = ['반', '조', '학년'][np.random.randint(0, 3)]
    q2 = ['미술', '수학', '영어', '체육'][np.random.randint(0, 4)]
    j1 = proc_jo(q1, 2)

    list_1 = [3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    list_2 = [2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    list_3 = [3, 3, 3, 2, 2, 2, 2, 1, 1, 1] 
    list_4 = [4, 4, 4, 2, 2, 2, 1, 1]
    list_5 = [3, 3, 3, 2, 2, 2, 2, 2, 1]

    list_A = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    list_B = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]

    list_A1 = list()
    list_B1 = list()
    list_A2 = list()
    list_B2 = list()
    while len(list_A1) != len(list_A):
        temp = np.random.randint(10, 100)
        if temp not in list_A1:
           list_A1.append(temp)
    while len(list_B1) != len(list_B):
        temp = np.random.randint(10, 100)
        if temp not in list_B1:
           list_B1.append(temp)
    i = 0
    for i in range(len(list_A)):
        for j in range(list_A[i]):
            list_A2.append(list_A1[i])
    for i in range(len(list_B)):
        for j in range(list_B[i]):
            list_B2.append(list_B1[i])

    [c1, c2, c3] = [list_A2[0], list_A2[(2 * list_A[0]) - 1], list_A2[(2 * list_A[0])]]
    c4 = list_A[0]
    c5 = c4
    [c6, c7, c8] = [list_B2[0], list_B2[(2 * list_B[0]) - 1], list_B2[(2 * list_B[0])]]
    c9 = list_B[0]
    c10 = c9
    c11 = c5 + c10

    np.random.shuffle(list_A2)
    np.random.shuffle(list_B2)
    
    s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20 = list_A2
    ss1, ss2, ss3, ss4, ss5, ss6, ss7, ss8, ss9, ss10, ss11, ss12, ss13, ss14, ss15, ss16, ss17, ss18, ss19, ss20 = list_B2

    stem = stem.format(q1=q1, q2=q2, j1=j1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10, s11=s11, s12=s12, s13=s13, s14=s14, s15=s15, s16=s16, s17=s17, s18=s18, s19=s19, s20=s20, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5, ss6=ss6, ss7=ss7, ss8=ss8, ss9=ss9, ss10=ss10, ss11=ss11, ss12=ss12, ss13=ss13, ss14=ss14, ss15=ss15, ss16=ss16, ss17=ss17, ss18=ss18, ss19=ss19, ss20=ss20)
    answer = answer.format(a1=c11)
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11)

    return stem, answer, comment


def statistics326_Stem_014():
    stem = "다음은 {q1}네 반 학생 $$수식$$25$$/수식$$명의 {q2} 성적을 조사하여 나타낸 것이다. {q1}네 반 학생들의 {q2} 성적의 중앙값을 $$수식$$a$$/수식$$점, 최빈값을 $$수식$$b$$/수식$$점이라 할 때, $$수식$$a + b$$/수식$$의 값을 구하시오.\n" \
            "$$표$$$$수식$${s1}, {s2}, {s3}, {s4}, {s5}, {s6}, {s7}, {s8}, {s9}, {s10},$$/수식$$\n $$수식$${s11}, {s12}, {s13}, {s14}, {s15}, {s16}, {s17}, {s18}, {s19}, {s20},$$/수식$$\n $$수식$${s21}, {s22}, {s23}, {s24}, {s25}$$/수식$$ (단위 : 점)$$/표$$\n"         
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "주어진 자료의 개수는 $$수식$$25$$/수식$$이고 자료를 크기순으로 나열하면\n" \
              "$$수식$${c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}, {c8}, {c9}, {c10},$$/수식$$\n$$수식$$ {c11}, {c12}, {c13}, {c14}, {c15}, {c16}, {c17}, {c18}, {c19}, {c20},$$/수식$$\n $$수식$${c21}, {c22}, {c23}, {c24}, {c25}$$/수식$$\n" \
              "이므로 중앙값 $$수식$$a = {c13}$$/수식$$, 최빈값 $$수식$$b = {c26}$$/수식$$\n" \
              "따라서 $$수식$$a + b = {c13} + {c26} = {c27}$$/수식$$\n\n"

    q1 = ['영준이', '재영이', '영희', '선우', '태인이'][np.random.randint(0, 5)]
    q2 = ['미술', '수학', '영어', '체육'][np.random.randint(0, 4)]

    list_1 = [5, 3, 3, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    list_2 = [3, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    list_3 = [3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1] 
    list_4 = [4, 4, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    list_5 = [3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]

    list_A = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]

    list_A1 = list()
    list_A2 = list()
    while len(list_A1) != len(list_A):
        temp = np.random.randint(10, 100)
        if temp not in list_A1:
           list_A1.append(temp)
    print(list_A1)
    i = 0
    for i in range(len(list_A)):
        for j in range(list_A[i]):
            list_A2.append(list_A1[i])

    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25 = list_A2
    c26 = list_A2[0]
    c27 = c13 + c26
    
    np.random.shuffle(list_A2)
    s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25 = list_A2 

    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10, s11=s11, s12=s12, s13=s13, s14=s14, s15=s15, s16=s16, s17=s17, s18=s18, s19=s19, s20=s20, s21=s21, s22=s22, s23=s23, s24=s24, s25=s25)
    answer = answer.format(a1=c11)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12, c13=c13, c14=c14, c15=c15, c16=c16, c17=c17, c18=c18, c19=c19, c20=c20, c21=c21, c22=c22, c23=c23, c24=c24, c25=c25, c26=c26, c27=c27)

    return stem, answer, comment


def statistics326_Stem_015():
    stem = "다음은 학생 $$수식$$9$$/수식$$명의 {q1} 성적이다. 평균을 $$수식$$a $$/수식$$점, 중앙값을 $$수식$$b $$/수식$$점, 최빈값을 $$수식$$c $$/수식$$점이라 할 때, $$수식$$a + b + c$$/수식$$의 값을 구하시오.\n" \
            "$$표$$$$수식$${s1}, {s2}, {s3}, {s4}, {s5}, {s6}, {s7}, {s8}, {s9} $$/수식$$(단위 : 점)$$/표$$\n"         
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "(평균)$$수식$$= {{{s1} + {s2} + {s3} + {s4} + {s5} + {s6} + {s7} + {s8} + {s9}}} over {{9}}$$/수식$$\n" \
              "$$수식$$= {{ {c10} }} over {{9}} = {c11}$$/수식$$(점)\n" \
              "변량을 작은 값부터 나열하면\n" \
              "$$수식$${c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}, {c8}, {c9} $$/수식$$이고 변량의 개수가 $$수식$$9$$/수식$$개이므로 중앙값은 $$수식$$5$$/수식$$번째인 $$수식$${c5}$$/수식$$점이다.\n" \
              "또 자료에서 가장 많이 나타나는 값이 $$수식$${c12}$$/수식$$이므로 최빈값은 $$수식$${c12}$$/수식$$점이다.\n" \
              "따라서 $$수식$$a = {c11}$$/수식$$, $$수식$$b = {c5}$$/수식$$, $$수식$$c = {c12}$$/수식$$ 이므로\n" \
              "$$수식$$a + b + c = {c13}$$/수식$$\n\n"

    q1 = ['국어 수행 평가', '수학 퀴즈', '체육 수행 평가', '영어 퀴즈'][np.random.randint(0, 4)]

    list_1 = [3, 2, 3, 3, 4, 4, 5, 5, 7]
    list_2 = [4, 3, 4, 4, 5, 5, 6, 6, 8]
    list_3 = [5, 4, 5, 5, 6, 6, 7, 7, 9]
    list_4 = [2, 1, 2, 2, 3, 3, 4, 4, 6]
    list_5 = [4, 5, 5, 2, 4, 7, 4, 4, 10]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    c12 = list_A2[0]
    list_A2.sort()

    c1, c2, c3, c4, c5, c6, c7, c8, c9 = list_A2
    c10 = sum([c1, c2, c3, c4, c5, c6, c7, c8, c9])
    c11 = c10 // 9
    
    c13 = c11 + c5 + c12
    a1 = c13
    
    np.random.shuffle(list_A2)
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = list_A2 

    stem = stem.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9)
    answer = answer.format(a1=a1)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12, c13=c13)

    return stem, answer, comment


def statistics326_Stem_016():
    stem = "다음 자료의 중앙값을 $$수식$$x$$/수식$$, 최빈값을 $$수식$$y$$/수식$$라 할 때, $$수식$$x + y$$/수식$$의 값은? (단, $$수식$$a &lt; b &lt; {s10}$$/수식$$이고, $$수식$$a,b $$/수식$$ 는 자연수이다.)\n" \
           "$$표$$$$수식$${s1}, {s2}, {s3}, {s4}, {s5}, {s6}, {s7}, {s8}, {s9}$$/수식$$$$/표$$\n" \
           "① $$수식$${s11}$$/수식$$\n" \
           "② $$수식$${s12}$$/수식$$\n" \
           "③ $$수식$${s13}$$/수식$$\n" \
           "④ $$수식$${s14}$$/수식$$\n" \
           "⑤ $$수식$${s15}$$/수식$$\n"    
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$${c10}$$/수식$$보다 작은 수는 $$수식$${c1}, {c2}, {c3}, {c4}, {c5}$$/수식$$의 $$수식$$5$$/수식$$개, $$수식$${c10}$$/수식$$보다 큰 수는 $$수식$${c6}, {c7}, {c8}, {c9}$$/수식$$의 $$수식$$4$$/수식$$개이므로 중앙값은 $$수식$${c5}$$/수식$$이다.\n" \
              "또, 자료에서 가장 많이 나타나는 값이 $$수식$${c11}$$/수식$$이므로 최빈값은 $$수식$${c11}$$/수식$$이다.\n" \
              "따라서 $$수식$$x = {c5}$$/수식$$, $$수식$$y = {c11}$$/수식$$이므로 $$수식$$x + y = {c5} + {c11} = {c12}$$/수식$$\n\n" \
              "\n\n"

    q1 = ['국어 수행 평가', '수학 퀴즈', '체육 수행 평가', '영어 퀴즈'][np.random.randint(0, 4)]

    list_1 = [3, 4, 'a', 'b', 6, 8, 8, 8, 11, 7, 8]
    list_2 = [4, 5, 'a' ,'b' ,7, 9, 10, 10, 10, 8, 10]
    list_3 = [2, 'a', 'b', 5, 6, 8, 9, 9, 9, 7, 9]
    list_4 = [1, 'a', 'b', 3, 4, 6, 7, 7, 7, 5, 7]
    list_5 = [1, 'a', 'b', 2, 3, 5, 8, 8, 8, 4, 8]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11 = list_A2
    s10 = c10
    c12 = c5 + c11
    a1 = c12
    
    list_A2t = list_A2[0:9]
    np.random.shuffle(list_A2t)
    s1, s2, s3, s4, s5, s6, s7, s8, s9 = list_A2t

    t1 = np.random.randint(a1 - 2, a1 + 2)
    s_candidates = [t1 - 2, t1 - 1, t1, t1 + 1, t1 + 2]
    s11, s12, s13, s14, s15 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10, s11=s11, s12=s12, s13=s13, s14=s14, s15=s15)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12)

    return stem, answer, comment


def statistics326_Stem_017():
    stem = "다음 자료는 어느 반 학생 $$수식$$5$$/수식$$명의 {q1} 점수를 조사하여 나타낸 것이다. $$수식$$5$$/수식$$명의 평균이 $$수식$${s5}$$/수식$$점일 때, $$수식$$x$$/수식$$의 값을 구하시오.\n" \
            "$$표$$$$수식$${s1}, x, {s2}, {s3}, {s4}$$/수식$$ (단위 : 점)$$/표$$\n"         
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${{{s1} + x + {s2} + {s3} + {s4} }} over {{5}} = {{ {c1} + x }} over {{5}} = {s5}$$/수식$$\n" \
              "$$수식$${c1} + x = {c2}$$/수식$$\n" \
              "따라서 $$수식$$x = {c3}$$/수식$$ \n\n"

    q1 = ['국어 수행 평가', '수학 퀴즈', '체육 수행 평가', '영어 퀴즈'][np.random.randint(0, 4)]

    s5 = np.random.randint(60, 90)
    a1 = np.random.randint(s5 - 20, s5 + 10)
    t1 = (s5 * 5 - a1) // 4
    s1, s2, s3, s4 = [101, 101, 101, 101]    
    while (s1 > 100) or (s2 > 100) or (s3 > 100) or (s4 > 100):
        s1 = np.random.randint(t1 - 20, t1 + 10)
        s2 = np.random.randint(t1 - 20, t1 + 10)
        s3 = np.random.randint(t1 - 20, t1 + 10)
        s4 = (s5 * 5) - s1 - s2 - s3 - a1

    c1 = s1 + s2 + s3 + s4
    c2 = s5 * 5
    c3 = c2 - c1

    stem = stem.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=a1)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, c1=c1, c2=c2, c3=c3)

    return stem, answer, comment


def statistics326_Stem_018():
    stem = "$$수식$$4$$/수식$$회에 걸친 {q1} 성적이 $$수식$${s1}$$/수식$$점, $$수식$${s2}$$/수식$$점, $$수식$${s3}$$/수식$$점, $$수식$${s4}$$/수식$$점이다. $$수식$$5$$/수식$$회째 {q1}에서 몇 점을 받아야 $$수식$$5$$/수식$$회까지의 평균이 $$수식$${s5}$$/수식$$점이 되는가?\n" \
           "① $$수식$${s11}$$/수식$$\n" \
           "② $$수식$${s12}$$/수식$$\n" \
           "③ $$수식$${s13}$$/수식$$\n" \
           "④ $$수식$${s14}$$/수식$$\n" \
           "⑤ $$수식$${s15}$$/수식$$\n"      
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$5$$/수식$$회째 {q1}의 성적을 $$수식$$x$$/수식$$점이라 하면\n" \
              "$$수식$${{{s1} + {s2} + {s3} + {s4} + x }} over {{5}} = {{ {c1} + x }} over {{5}} = {s5}$$/수식$$\n" \
              "$$수식$${c1} + x = {c2}$$/수식$$\n" \
              "그러므로 $$수식$$x = {c3}$$/수식$$ \n" \
              "따라서 $$수식$$5$$/수식$$회째 {q1}에서 $$수식$${c3}$$/수식$$점을 받아야 한다."

    q1 = ['국어 수행 평가', '수학 퀴즈', '체육 수행 평가', '영어 퀴즈'][np.random.randint(0, 4)]

    s5 = np.random.randint(60, 90)
    a1 = np.random.randint(s5 - 20, s5 + 10)
    t1 = (s5 * 5 - a1) // 4
    s1, s2, s3, s4 = [101, 101, 101, 101]    
    while (s1 > 100) or (s2 > 100) or (s3 > 100) or (s4 > 100):
        s1 = np.random.randint(t1 - 20, t1 + 10)
        s2 = np.random.randint(t1 - 20, t1 + 10)
        s3 = np.random.randint(t1 - 20, t1 + 10)
        s4 = (s5 * 5) - s1 - s2 - s3 - a1

    c1 = s1 + s2 + s3 + s4
    c2 = s5 * 5
    c3 = c2 - c1

    t1 = np.random.randint(a1 - 2, a1 + 2)
    s_candidates = [t1 - 2, t1 - 1, t1, t1 + 1, t1 + 2]
    s11, s12, s13, s14, s15 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s11=s11, s12=s12, s13=s13, s14=s14, s15=s15)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, c1=c1, c2=c2, c3=c3)

    return stem, answer, comment


def statistics326_Stem_019():
    stem = "{q1} 이번 중간고사 $$수식$${q2}$$/수식$$과목 중 $$수식$${q3}$$/수식$$과목의 평균이 $$수식$${q4}$$/수식$$점 이었으나 나머지 한 과목 때문에 평균이 $$수식$${q5}$$/수식$$점이 되었다. 나머지 한 과목의 점수를 구하시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$점\n"
    comment = "(해설)\n" \
              "나머지 한 과목의 점수를 $$수식$$x$$/수식$$점이라 하면\n" \
              "$$수식$${{ {q4} times {q3} + x }} over {{ {q2} }} = {q5}$$/수식$$, $$수식$${q4} times {q3} + x = {c1}$$/수식$$\n" \
              "$$수식$${c2} + x = {c1}$$/수식$$\n" \
              "그러므로 $$수식$$x = {c3}$$/수식$$\n" \
              "따라서 나머지 한 과목의 점수는 $$수식$${c3}$$/수식$$점이다.\n\n"

    q1 = ['소진이는', '영훈이는', '선우는', '영준이는'][np.random.randint(0, 4)]
    q2 = np.random.randint(4, 9)
    q3 = q2 - 1
    q5 = np.random.randint(40, 90)
    c3 = 101
    while (c3 < 0) or (c3 > 100):
        q4 = np.random.randint(q5 - 10, q5 + 10)        
        c1 = q2 * q5
        c2 = q4 * q3
        c3 = c1 - c2
        a1 = c3

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    answer = answer.format(a1=a1)
    comment = comment.format(q2=q2, q3=q3, q4=q4, q5=q5, c1=c1, c2=c2, c3=c3)

    return stem, answer, comment


def statistics326_Stem_020():
    stem = "다음 $$수식$$6$$/수식$$개의 자료의 평균이 $$수식$${q1}$$/수식$$일 때, 중앙값은?\n" \
           "$$표$$$$수식$${s6}, {s7}, {s8}, {s9}, x,{s10}$$/수식$$$$/표$$\n" \
           "① $$수식$${s1}$$/수식$$\n" \
           "② $$수식$${s2}$$/수식$$\n" \
           "③ $$수식$${s3}$$/수식$$\n" \
           "④ $$수식$${s4}$$/수식$$\n" \
           "⑤ $$수식$${s5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "(평균)$$수식$$= {{{s6} + {s7} + {s8} + {s9} + x + {s10}}} over {{6}} = {c1}$$/수식$$에서\n" \
              "$$수식$$x + {c2} = {c3}$$/수식$$이므로 $$수식$$x = {c4}$$/수식$$\n" \
              "자료를 작은 값에서부터 크기순으로 나열하면\n" \
              "$$수식$${c6}, {c7}, {c8}, {c9}, {c10}, {c11}$$/수식$$이므로\n" \
              "중앙값은 $$수식$${{ {c8} + {c9} }} over {{2}} = {c5}$$/수식$$\n\n"

    list_1 = [1, 2, 3, 5, 6, 7]
    list_2 = [1, 3, 4, 6, 7, 9]
    list_3 = [1, 2, 5, 7, 7, 8]
    list_4 = [1, 3, 3, 5, 5, 7]
    list_5 = [1, 4, 5, 7, 8, 11]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 5);
    for i in range(len(list_A2)):
        list_A2[i] += t0
    c6, c7, c8, c9, c10, c11 = list_A2
    np.random.shuffle(list_A2)
    s6, s7, s8, s9, x, s10 = list_A2

    q1 = (c6 + c7 + c8 + c9 + c10 + c11) // 6
    c1 = q1
    c2 = s6 + s7 + s8 + s9 + s10
    c3 = c1 * 6
    c4 = c3 - c2
    c5 = (c8 + c9) // 2

    a1 = c5
    t1 = np.random.randint(a1 - 2, a1 + 2)
    s_candidates = [t1 - 2, t1 - 1, t1, t1 + 1, t1 + 2]
    s1, s2, s3, s4, s5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s6=s6, s7=s7, s8=s8, s9=s9, s10=s10, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11)

    return stem, answer, comment


def statistics326_Stem_021():
    stem = "다음 자료는 어느 반 학생 $$수식$$6$$/수식$$명의 {q2} 점수를 조사하여 나타낸 것이다. $$수식$$6$$/수식$$명의 평균이 $$수식$${q1}$$/수식$$일 때, 최빈값을 구하시오.\n" \
           "$$표$$$$수식$${s6}, {s7}, {s8}, {s9},x, {s10} $$/수식$$ (단위: 점)$$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$점\n"
    comment = "(해설)\n" \
              "(평균)$$수식$$= {{{s6} + {s7} + {s8} + {s9} + x + {s10}}} over {{6}} = {c1}$$/수식$$에서\n" \
              "$$수식$$x + {c2} = {c3}$$/수식$$이므로 $$수식$$x = {c4}$$/수식$$\n" \
              "따라서 자료에서 가장 많이 나타나는 값이 $$수식$${c5}$$/수식$$점이므로 최빈값은 $$수식$${c5}$$/수식$$점이다.\n\n"

    q2 = ['국어', '수학 퀴즈', '체육', '영어 퀴즈'][np.random.randint(0, 4)]

    list_1 = [5, 3, 4, 5, 5, 2]
    list_2 = [4, 2, 4, 4, 7, 9]
    list_3 = [2, 2, 5, 6, 7, 8]
    list_4 = [5, 3, 4, 5, 5, 2]
    list_5 = [4, 2, 4, 7, 8, 11]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 5);
    for i in range(len(list_A2)):
        list_A2[i] = list_A2[i] * 5
        list_A2[i] += 40
        list_A2[i] += t0
    c5 = list_A2[0]
    np.random.shuffle(list_A2)
    s6, s7, s8, s9, x, s10 = list_A2

    q1 = (s6 + s7 + s8 + s9 + x + s10) // 6
    c1 = q1
    c2 = s6 + s7 + s8 + s9 + s10
    c3 = c1 * 6
    c4 = c3 - c2

    a1 = c5

    stem = stem.format(q1=q1, q2=q2, s6=s6, s7=s7, s8=s8, s9=s9, s10=s10)
    answer = answer.format(a1=a1)
    comment = comment.format(s6=s6, s7=s7, s8=s8, s9=s9, s10=s10, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)

    return stem, answer, comment


def statistics326_Stem_022():
    stem = "$$수식$$4$$/수식$$개의 변량 $$수식$${s1}, {s2}, {s3}, x$$/수식$$의 중앙값이 $$수식$${q1}$$/수식$$일 때, $$수식$$x$$/수식$$의 값을 구하시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${s1}, {s2}, {s3}, x$$/수식$$의 중앙값이 $$수식$${q1}$$/수식$$이므로\n" \
              "변량을 작은 값부터 크기순으로 나열하면 $$수식$${c1}, x, {c2}, {c3} $$/수식$$이어야 한다.\n" \
              "(중앙값)$$수식$$= {{ x + {c2} }} over {{2}} = {c4}$$/수식$$, $$수식$$x + {c2} = {c5}$$/수식$$\n" \
              "따라서 $$수식$$x = {c6}$$/수식$$\n\n"

    list_1 = [15, 16, 18, 19]
    list_2 = [2, 5, 9, 20]
    list_3 = [24, 28, 30, 31]
    list_4 = [74, 80, 84, 90]
    list_5 = [30, 40, 50, 55]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 5);
    for i in range(len(list_A2)):
        list_A2[i] += t0
    c1, x, c2, c3 = list_A2

    q1 = (x + c2) // 2
    c4 = q1
    c5 = c4 * 2
    c6 = c5 - c2
    a1 = c6

    list_A3 = [c1, c2, c3]
    np.random.shuffle(list_A3)
    s1, s2, s3 = list_A3

    stem = stem.format(q1=q1, s1=s1, s2=s2, s3=s3)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, s1=s1, s2=s2, s3=s3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)

    return stem, answer, comment


def statistics326_Stem_023():
    stem = "다음은 자료를 크기순으로 나열한 것이다. 이 자료의 중앙값이  $$수식$${c1}$$/수식$$일 때, 평균을 구하시오. \n" \
           "$$표$$$$수식$${s1}, {s2}, {s3}, x, {s4}, {s5}$$/수식$$$$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "중앙값은 $$수식$$3$$/수식$$번째 변량과 $$수식$$4$$/수식$$번째 변량의 평균이므로\n" \
              "$$수식$${{ {s3} + x }} over {{2}} = {c1}$$/수식$$, $$수식$${s3} + x = {c2}$$/수식$$\n" \
              "그러므로 $$수식$$x = {c3}$$/수식$$\n" \
              "따라서 주어진 자료의 평균은\n" \
              "$$수식$${{ {s1} + {s2} + {s3} + {c3} + {s4} + {s5} }} over {{6}} = {{ {c4} }} over {{6}} = {c5}$$/수식$$\n\n"

    list_1 = [2, 6, 7, 9, 13, 17]
    list_2 = [2, 3, 5, 9, 20, 21]
    list_3 = [24, 26, 28, 30, 31, 35]
    list_4 = [73, 75, 80, 84, 90, 90]
    list_5 = [30, 33, 40, 50, 55, 56]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 20);
    for i in range(len(list_A2)):
        list_A2[i] += t0
    s1, s2, s3, x, s4, s5 = list_A2

    c1 = (s3 + x) // 2
    c2 = 2 * c1
    c3 = c2 - s3
    c4 = s1 + s2 + s3 + x + s4 + s5
    c5 = c4 // 6

    a1 = c5

    stem = stem.format(c1=c1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=a1)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)

    return stem, answer, comment



def statistics326_Stem_024():
    stem = "다음 $$수식$$7$$/수식$$개의 자료의 평균과 중앙값이 모두 $$수식$${q1}$$/수식$$일 때, 자연수 a, b에 대하여 ab의 값은?(단, $$수식$$a &lt; b$$/수식$$이다.)\n" \
           "$$표$$$$수식$${s1}, {s2}, {s3}, a, {s4}, b, {s5}$$/수식$$$$/표$$\n" \
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$7$$/수식$$개의 자료의 평균이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$$= {{ {s1} + {s2} + {s3} + a + {s4} + b + {s5} }} over {{7}} = {q1}$$/수식$$에서\n" \
              "$$수식$${{ {c6} + a + b }} over {{7}} = {q1}$$/수식$$, $$수식$${c6} + a + b = {c7}$$/수식$$\n" \
              "따라서 $$수식$$a + b = {c8}$$/수식$$\n" \
              "$$수식$$a, b$$/수식$$를 제외한 자료를 작은 값에서부터 크기순으로 나열하면 $$수식$${c1}, {c2}, {c3}, {c4}, {c5}$$/수식$$\n" \
              "이때 중앙값이 $$수식$${q1}$$/수식$$이고 $$수식$$a + b = {c8}$$/수식$$, $$수식$$a &lt; b$$/수식$$이므로\n" \
              "$$수식$$a = {c9}$$/수식$$, $$수식$$b = {c10}$$/수식$$\n" \
              "따라서 $$수식$$ab = {c11}$$/수식$$\n\n"

    list_1 = [1, 2, 3, 5, 6, 8, 10] 
    list_2 = [1, 2, 4, 5, 6, 7, 10] 
    list_3 = [1, 3, 4, 5, 6, 7, 9] 
    list_4 = [1, 2, 4, 5, 6, 8, 9]
    list_5 = [2, 3, 4, 5, 6, 7, 9]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 5)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0

    c1, a, c2, b, c3, c4, c5 = list_A2
    list_temp = [c1, c2, c3, c4, c5]
    np.random.shuffle(list_temp)
    s1, s2, s3, s4, s5 = list_temp

    q1 = sum(list_A2) // 7  
    
    c6 = s1 + s2 + s3 + s4 + s5
    c7 = q1 * 7
    c8 = c7 - c6
    c9 = a
    c10 = b
    c11 = a * b

    a1 = c11
    t1 = np.random.randint(a1 - 2, a1 + 2)
    s_candidates = [t1 - 2, t1 - 1, t1, t1 + 1, t1 + 2]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, ss1=ss1, ss2=ss2,ss3=ss3,ss4=ss4,ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11)
    return stem, answer, comment

def statistics326_Stem_025():
    stem = "다음 자료는 학생 $$수식$$10$$/수식$$명의 {q1} 점수이다. 이 자료의 중앙값이 $$수식$${q2}$$/수식$$점, 최빈값이 $$수식$${q3}$$/수식$$점일 때, $$수식$$a + b + c$$/수식$$의 값을 구하시오. \n" \
           "$$표$$$$수식$${s1}, {s2}, {s3}, {s4}, {s5}, a, b, c, {s6}, {s7} $$/수식$$ (단위: 점)$$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$a, b, c$$/수식$$를 제외한 자료에서 $$수식$${c10}$$/수식$$점의 도수가 $$수식$$2$$/수식$$로 가장 크고, $$수식$${q3}$$/수식$$점의 도수가 $$수식$$1$$/수식$$이므로\n" \
              "최빈값이 $$수식$${q3}$$/수식$$점이 되려면 $$수식$$a, b, c$$/수식$$ 중 적어도 $$수식$$2$$/수식$$개는 $$수식$${q3}$$/수식$$이어야 한다.\n" \
              "즉,$$수식$$ a, b, c$$/수식$$의 값을 $$수식$${q3}, {q3}, x $$/수식$$라 하면 " \
              "중앙값이 $$수식$${q2}$$/수식$$점이므로\n" \
              "자료를 작은 값에서부터 크기순으로 나열하면\n" \
              "$$수식$${c1}, {c2}, {c3}, {c4}, {c5}, x, {c6}, {c7}, {c8}, {c9}$$/수식$$\n" \
              "이때 중앙값은\n" \
              "$$수식$$ {{ {c5} + x }} over {{2}} = {q2}$$/수식$$에서 $$수식$$ {c5} + x = {c11}$$/수식$$\n" \
              "따라서 $$수식$$ x = {c12}$$/수식$$\n" \
              "따라서 $$수식$$a + b + c = {q3} + {q3} + {c12} = {c13}$$/수식$$\n\n"

    q1 = ['수학 수행 평가', '수학 퀴즈', '체육 수행 평가', '영어 퀴즈'][np.random.randint(0, 4)]

    list_1 = [9, 10, 12, 12, 12, 16, 17, 18, 18, 20]
    list_2 = [7, 8, 10, 10, 10, 14, 15, 19, 19, 22] 
    list_3 = [7, 8, 9, 9, 9, 13, 15, 17, 17, 20]  
    list_4 = [7, 8, 10, 10, 10, 14, 15, 19, 19, 22]
    list_5 = [7, 8, 9, 9, 9, 13, 15, 17, 17, 20]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 10)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0

    c1, c2, c3, c4, c5, x, c6, c7, c8, c9 = list_A2
    list_temp = [c1, c2, c3, c6, c7, c8, c9]
    np.random.shuffle(list_temp)
    s1, s2, s3, s4, s5, s6, s7 = list_temp

    q2 = (c5 + x) // 2
    q3 = c5

    c10 = c8
    c11 = q2 * 2
    c12 = c11 - c5
    c13 = q3 + q3 + c12

    a1 = c13

    stem = stem.format(q1=q1, q2=q2, q3=q3, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, q3=q3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12, c13=c13)
    return stem, answer, comment

def statistics326_Stem_026():
    stem = "다음 자료는 {q1} 반 학생들이 $$수식$$1$$/수식$$년 동안 {q2} 방문한 횟수를 조사하여 나타낸 것이다. 이 자료의 최빈값이 $$수식$${q3}$$/수식$$일 때, 중앙값은?\n" \
           "$$표$$$$수식$${s1}, {s2}, {s3}, {s4}, x, {s5}, {s6}, {s7}$$/수식$$ (단위: 회)$$/표$$\n" \
           "① $$수식$${ss1}$$/수식$$회\n" \
           "② $$수식$${ss2}$$/수식$$회\n" \
           "③ $$수식$${ss3}$$/수식$$회\n" \
           "④ $$수식$${ss4}$$/수식$$회\n" \
           "⑤ $$수식$${ss5}$$/수식$$회\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "최빈값이 $$수식$${q3}$$/수식$$회이므로 $$수식$$ x = {q3}$$/수식$$\n" \
              "변량을 작은 값부터 크기순으로 나열하면\n" \
              "$$수식$${c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}, {c8}$$/수식$$\n" \
              "따라서 중앙값은 $$수식$$ {{ {c4} + {c5} }} over {{2}} = {c9}$$/수식$$(회)\n\n"

    q1 = ['영선이네', '수민이네', '하은이네', '영희네'][np.random.randint(0, 4)]
    q2 = ['도서관을', '수영장을', '대형마트를'][np.random.randint(0, 3)]

    list_1 = [16, 19, 23, 23, 25, 25, 25, 30] 
    list_2 = [12, 13, 14, 14, 16, 16, 16, 17] 
    list_3 = [1, 1, 3, 3, 5, 5, 5, 11]
    list_4 = [13, 13, 23, 23, 25, 25, 25, 16]
    list_5 = [15, 17, 22, 22, 24, 24, 24, 29]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 20)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0

    c1, c2, c3, c4, c5, c6, c7, c8 = list_A2
    list_temp = [c1, c2, c3, c4, c6, c7, c8]
    np.random.shuffle(list_temp)
    s1, s2, s3, s4, s5, s6, s7 = list_temp

    q3 = c5    
    c9 = (c4 + c5) // 2

    a1 = c9
    t1 = np.random.randint(a1 - 2, a1 + 2)
    s_candidates = [t1 - 2, t1 - 1, t1, t1 + 1, t1 + 2]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, q2=q2, q3=q3, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q3=q3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9)
    return stem, answer, comment

def statistics326_Stem_027():
    stem = "다음 8개의 자료의 최빈값이 $$수식$${q1}$$/수식$$일 때, 중앙값을 소수로 나타내시오.\n" \
           "$$표$$$$수식$${s1}, {s2}, {s3}, {s4}, a, {s5}, b, {s6}$$/수식$$$$/표$$\n"
    answer = "(답):$$수식$$ {a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "최빈값이 $$수식$${q1}$$/수식$$이므로 $$수식$$ a = {q1}$$/수식$$, $$수식$$ b = {q1}$$/수식$$\n" \
              "변량을 작은 값부터 크기순으로 나열하면\n" \
              "$$수식$${c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}, {c8}$$/수식$$\n" \
              "따라서 중앙값은 $$수식$$ {{ {c4} + {c5} }} over {{2}} = {c9}$$/수식$$(회)\n\n"

    list_1 = [2, 3, 3, 3, 4, 4, 5, 6] 
    list_2 = [1, 3, 3, 3, 4, 4, 5, 10]  
    list_3 = [2, 3, 3, 3, 6, 6, 7, 9] 
    list_4 = [1, 3, 3, 3, 8, 8, 9, 10] 
    list_5 = [1, 2, 2, 2, 5, 5, 6, 7]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 10)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0

    c1, c2, c3, c4, c5, c6, c7, c8 = list_A2
    list_temp = [c1, c4, c5, c6, c7, c8]
    np.random.shuffle(list_temp)
    s1, s2, s3, s4, s5, s6 = list_temp

    q1 = c2
    c9 = (c4 + c5) / 2
    a1 = c9

    stem = stem.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9)
    return stem, answer, comment


def statistics326_Stem_028():
    stem = "다음 $$수식$$7$$/수식$$개 자료의 평균과 최빈값이 같을 때, $$수식$$ a$$/수식$$의 값으로 옳은 것은?\n" \
           "$$표$$$$수식$${s1}, {s2}, {s3}, {s4}, a, {s5}, {s6}$$/수식$$$$/표$$\n" \
           "① $$수식$${ss1}$$/수식$$회\n" \
           "② $$수식$${ss2}$$/수식$$회\n" \
           "③ $$수식$${ss3}$$/수식$$회\n" \
           "④ $$수식$${ss4}$$/수식$$회\n" \
           "⑤ $$수식$${ss5}$$/수식$$회\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "최빈값이 $$수식$${c7}$$/수식$$회이므로 평균도 $$수식$${c7}$$/수식$$\n" \
              "$$수식$${{ {s1} + {s2} + {s3} + {s4} + a + {s5} + {s6} }} over {{7}} = {c7}$$/수식$$에서\n" \
              "$$수식$${{ {c8} + a }} over {{7}} = {c7}$$/수식$$, $$수식$$ {c8} + a = {c9} THEREFORE a = {c10}$$/수식$$\n\n"


    list_1 = [14, 22, 34, 34, 34, 44, 56]
    list_2 = [12, 22, 34, 34, 34, 44, 58] 
    list_3 = [20, 26, 34, 34, 34, 44, 46]
    list_4 = [4, 12, 24, 24, 24, 34, 46]
    list_5 = [10, 16, 24, 24, 24, 34, 36]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 20)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0

    c1, a, c2, c3, c4, c5, c6 = list_A2
    list_temp = [c1, c2, c3, c4, c5, c6]
    np.random.shuffle(list_temp)
    s1, s2, s3, s4, s5, s6 = list_temp

    c7 = c2
    c8 = sum(list_temp)
    c9 = c7 * 7
    c10 = c9 - c8
    

    a1 = c10
    t1 = np.random.randint(a1 - 2, a1 + 2)
    s_candidates = [t1 - 2, t1 - 1, t1, t1 + 1, t1 + 2]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, c7=c7, c8=c8, c9=c9, c10=c10)
    return stem, answer, comment


def statistics326_Stem_029():
    stem = "두 자연수 $$수식$$a, b$$/수식$$에 대하여 $$수식$$5$$/수식$$개의 변량 $$수식$${s1}, {s2}, a, b, {s3}$$/수식$$의 중앙값이 $$수식$${q1}$$/수식$$이고, $$수식$$4$$/수식$$개의 변량 $$수식$${s4}, a, b, {s5}$$/수식$$의 중앙값이 $$수식$${q2}$$/수식$$일 때, 이를 만족시키는 두 자연수 $$수식$$a, b$$/수식$$에 대하여 $$수식$$ a + b$$/수식$$의 값을 구하시오. (단, $$수식$$ a &lt; b$$/수식$$이다.).\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$5$$/수식$$개의 변량 $$수식$${s1}, {s2}, a, b, {s3}$$/수식$$에서\n" \
              "$$수식$$ a &lt; b$$/수식$$이고, 중앙값이 {q1}이므로 $$수식$$ a = {q1}$$/수식$$\n" \
              "또, $$수식$$4$$/수식$$개의 변량  $$수식$${s4}, a, b, {s5}$$/수식$$ 에서\n$$수식$$ a = {q1}$$/수식$$, $$수식$$ a &lt; b$$/수식$$이고 중앙값이 $$수식$${q2}$$/수식$$이므로 \n" \
              "$$수식$$ {{ b + {s4} }} over {{2}} = {q2}$$/수식$$, $$수식$$ b + {s4} = {c1}$$/수식$$ 이므로 $$수식$$ b = {c2}$$/수식$$\n" \
              "따라서 $$수식$$ a + b = {c3}$$/수식$$\n\n"

    list_1 = [1, 2, 6, 8, 13, 4, 7] 
    list_2 = [1, 2, 6, 8, 13, 4, 7] 
    list_3 = [1, 2, 6, 8, 13, 4, 7] 
    list_4 = [1, 2, 6, 8, 13, 4, 7] 
    list_5 = [1, 2, 6, 8, 13, 4, 7]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 30)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0

    s1, s2, s3, s4, s5, q1, q2 = list_A2

    c1 = q2 * 2
    c2 = c1 - s4
    c3 = q1 + c2
    a1 = c3

    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def statistics326_Stem_030():
    stem = "다음 $$수식$$7$$/수식$$개의 자료의 평균과 최빈값이 모두 {c1}일 때, $$수식$$a times b$$/수식$$의 값을 구하시오. (단, $$수식$$a &lt; b$$/수식$$) \n" \
           "$$표$$$$수식$${s1}, {s2}, {s3}, a, {s4}, {s5}, b $$/수식$$$$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "평균이 $$수식$${c1}$$/수식$$이므로\n" \
              "$$수식$${{ {s1} + {s2} + {s3} + a + {s4} + {s5} + b }} over {{7}} = {c1}$$/수식$$ 에서\n" \
              "$$수식$${{ {c2} + a + b }} over {{7}} = {c1}$$/수식$$,\n" \
              "$$수식$${c2} + a + b = {c3}$$/수식$$\n" \
              "$$수식$$ THEREFORE a + b = {c4}$$/수식$$\n" \
              "이때 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$를 제외한 자료에서 모든 자료의 값에 대한 도수가 최빈값 $$수식$${c1}$$/수식$$이 되려면\n$$수식$$a, b$$/수식$$ 중 적어도 하나는 $$수식$${c1}$$/수식$$이어야 한다.\n" \
              "(i) $$수식$$ a = {c1}$$/수식$$이면 $$수식$$ b = {c5}$$/수식$$\n" \
              "(ii) $$수식$$ b = {c1}$$/수식$$이면 $$수식$$ a = {c5}$$/수식$$\n" \
              "그런데 $$수식$$a &lt; b$$/수식$$이므로 $$수식$$ a = {c1}$$/수식$$, $$수식$$ b = {c5}$$/수식$$\n" \
              "따라서 $$수식$$a times b = {c6}$$/수식$$\n\n"

    list_1 = [3, 7, 5, 5, 1, 4, 10]
    list_2 = [3, 7, 5, 5, 1, 4, 10]
    list_3 = [3, 7, 5, 5, 1, 4, 10]
    list_4 = [3, 7, 5, 5, 1, 4, 10]
    list_5 = [3, 7, 5, 5, 1, 4, 10]
  

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 7)
    for i in range(len(list_A2)):
        list_A2[i] += t0
    s1, s2, s3, a, s4, s5, b = list_A2

    c1 = a
    c2 = s1 + s2 + s3 + s4 + s5
    c3 = 7 * c1
    c4 = c3 - c2
    c5 = c4 - c1
    c6 = a * b
    a1 = c6

    stem = stem.format(c1=c1, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=a1)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)

    return stem, answer, comment


def statistics326_Stem_031():
    stem = "{q1}의 $$수식$$4$$/수식$$회에 걸친 {q2} 성적은 $$수식$${s1}$$/수식$$점, $$수식$${s2}$$/수식$$점,$$수식$${s3}$$/수식$$점, $$수식$$x$$/수식$$점이고, 최빈값은 $$수식$${q3}$$/수식$$점이다. $$수식$$5$$/수식$$회의 {q2} 성적이 높아서 $$수식$$5$$/수식$$회까지의 평균이 $$수식$$4$$/수식$$회까지의 평균보다 $$수식$${q4}$$/수식$$점 올랐다면 $$수식$$5$$/수식$$회째의 성적은 몇 점인가?\n" \
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "최빈값이 $$수식$${q3}$$/수식$$점이므로 $$수식$$x = {q3}$$/수식$$\n" \
              "$$수식$$4$$/수식$$회까지의 평균은\n" \
              "$$수식$${{ {s1} + {s2} + {s3} + {q3} }} over {{4}} = {c1}$$/수식$$(점)\n" \
              "$$수식$$5$$/수식$$회까지의 평균은 $$수식$${c1}$$/수식$$점에서 $$수식$${q4}$$/수식$$점이 오른 $$수식$${c2}$$/수식$$점이므로\n$$수식$$5$$/수식$$회의 성적을 $$수식$$y$$/수식$$점이라 하면\n" \
              "$$수식$${{ {s1} + {s2} + {s3} + {q3} + y }} over {{5}} = {c2}$$/수식$$에서\n" \
              "$$수식$$ {c3} + y = {c4} THEREFORE x = {c5}$$/수식$$\n" \
              "따라서 $$수식$$5$$/수식$$회째의 성적은 $$수식$${c5}$$/수식$$점이다.\n\n"

    q1 = ['현기', '수민이', '하은이', '영희'][np.random.randint(0, 4)]
    q2 = ['국어 시험', '체육 수행평가', '영어 시험', '수학 퀴즈'][np.random.randint(0, 4)]

    list_1 = [85, 55, 70, 70]
    list_2 = [85, 55, 70, 55]
    list_3 = [85, 55, 70, 85]
    list_4 = [85, 65, 60, 65]
    list_5 = [45, 85, 80, 45]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 20)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0

    s1, s2, s3, s4 = list_A2
    q3 = s4
    q4 = np.random.randint(2, 6)
    
    c1 = (s1 + s2 + s3 + q3) // 4
    c2 = c1 + q4
    c3 = s1 + s2 + s3 + q3
    c4 = c2 * 5
    c5 = c4 - c3
    
    a1 = c5
    t1 = np.random.randint(a1 - 2, a1 + 2)
    s_candidates = [t1 - 2, t1 - 1, t1, t1 + 1, t1 + 2]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, s1=s1, s2=s2, s3=s3, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, q1=q1, q2=q2, q3=q3, q4=q4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def statistics326_Stem_032():
    stem = "어느 중학교의 {q1} 동아리 회원 $$수식$${q2}$$/수식$$명의 몸무게의 평균은 $$수식$${q3} rm kg$$/수식$$이었다. 그런데 한 명의 회원이 동아리를 탈퇴하여 몸무게의 평균은 $$수식$${q4} rm kg$$/수식$$이 되었다고 할 때, 탈퇴한 회원의 몸무게를 구하시오.\n"
    answer = "(답):$$수식$${a1} rm kg$$/수식$$\n"
    comment = "(해설)\n" \
              "탈퇴한 회원의 몸무게를 $$수식$$x rm kg$$/수식$$이라 하면\n회원 $$수식$${c1}$$/수식$$명의 몸무게의 합은 $$수식$$( {q2} times {q3} - x ) rm kg$$/수식$$\n" \
              "회원 $$수식$${c1}$$/수식$$명의 몸무게의 평균이 $$수식$${q4} rm kg$$/수식$$이므로\n" \
              "$$수식$$ {{ {q2} times {q3} - x }} over {{{c1}}} = {q4}`` THEREFORE x = {c2}$$/수식$$\n" \
              "따라서 탈퇴한 회원의 몸무게는 $$수식$${c2} rm kg$$/수식$$이다.\n\n"

    
    q1 = ['농구', '축구', '야구', '배드민턴'][np.random.randint(0, 4)]
    c1 = np.random.randint(1, 6) * 10
    q2 = c1 + 1
    q3 = np.random.randint(40, 70)
    t0 = np.random.randint(0, 1)
    q4 = q3 - 0.5 - t0

    c2 = round((q2 * q3) - (q4 * c1))
    a1 = c2

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, c1=c1, c2=c2)
    return stem, answer, comment


def statistics326_Stem_033():
    stem = "{q1}네 반 학생 $$수식$${q2}$$/수식$$명의 몸무게의 평균은 $$수식$${q3} rm kg$$/수식$$이다. 두 명의 학생이 전학을 간 후 나머지 $$수식$${c1}$$/수식$$명의 몸무게의 평균이 $$수식$${q4} rm kg$$/수식$$이 되었다. 전학을 간 두 학생의 몸무게의 평균은?\n" \
        "① $$수식$${ss1} rm kg$$/수식$$\n" \
        "② $$수식$${ss2} rm kg$$/수식$$\n" \
        "③ $$수식$${ss3} rm kg$$/수식$$\n" \
        "④ $$수식$${ss4} rm kg$$/수식$$\n" \
        "⑤ $$수식$${ss5} rm kg$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "전학을 간 두 학생의 몸무게의 합을 $$수식$$x rm kg$$/수식$$이라 하면\n" \
              "$$수식$$ {{ {q2} times {q3} - x }} over {{{c1}}} = {q4}$$/수식$$, $$수식$${c2} - x = {c3} $$/수식$$\n" \
              "$$수식$$x = {c4}(rm kg)$$/수식$$\n" \
              "따라서 전학을 간 두 학생의 몸무게의 평균은 $$수식$${{ {c4} }} over {{2}} = {c5}(rm kg)$$/수식$$\n\n"

    
    q1 = ['이준이', '하은이', '수민이', '민제'][np.random.randint(0, 4)]
    q2 = np.random.randint(1, 6) * 10
    c1 = q2 - 2
    q3 = np.random.randint(40, 70) + 0.2
    t0 = np.random.randint(0, 1)
    q4 = q3 - 0.2 - t0

    c2 = round(q2 * q3)
    c3 = round(q4 * c1)
    c4 = c2 - c3
    c5 = c4 / 2
    a1 = c5
    c1, c2, c3, c4, c5, a1, q3, q4 = RoundCheck([c1, c2, c3, c4, c5, a1, q3, q4])

    t1 = np.random.randint(a1 - 1, a1 + 1)
    s_candidates = [t1 - 1, t1 - 0.5, t1, t1 + 0.5, t1 + 1]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break
    s_candidates = RoundCheck(s_candidates)

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, c1=c1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def statistics326_Stem_034():
    stem = "어느 모둠 학생 $$수식$${q1}$$/수식$$명의 키를 작은 값부터 크기순으로 나열할 때, $$수식$${q2}$$/수식$$번째 변량이 $$수식$${q3} rm cm$$/수식$$ 이고 중앙값은 $$수식$${q4} rm cm$$/수식$$이다. 이 모둠에 키가 $$수식$${q5} rm cm$$/수식$$인 학생이 들어올 때, 학생 $$수식$${q6}$$/수식$$명의 키의 중앙값을 구하시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "학생 $$수식$${q1}$$/수식$$명의 키를 작은 값부터 크기순으로 나열하고 $$수식$${c1}$$/수식$$번째 변량을 $$수식$$x rm cm$$/수식$$라 하면\n" \
              "$$수식$$ {{ {q3} + x }} over {{2}} = {q4} THEREFORE x = {c2}$$/수식$$\n" \
              "따라서 학생 $$수식$${q6}$$/수식$$명의 키를 작은 값부터 크기순으로 나열하면\n중앙값은 $$수식$${c1}$$/수식$$번째 변량인 $$수식$${c2} rm cm$$/수식$$이다.\n\n"

    q1 = np.random.randint(2, 8) * 2
    q2 = q1 // 2
    q3 = np.random.randint(150, 175)
    q4 = q3 + np.random.randint(1, 5)    
    q6 = q1 + 1
    c1 = q2 + 1
    c2 = (q4 * 2) - q3
    q5 = c2 + np.random.randint(2, 10)

    a1 = c2

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q3=q3, q4=q4, q6=q6, c1=c1, c2=c2)
    return stem, answer, comment


def statistics326_Stem_035():
    stem = "다음은 어느 {q1} 회원 $$수식$$5$$/수식$$명의 나이를 변량으로 한 자료에 대한 설명이다. 이때 나머지 한 회원의 나이를 구하시오.\n" \
            "$$표$$(가) 가장 어린 회원의 나이는 $$수식$${s1}$$/수식$$살이다.\n (나) 회원들의 나이의 평균은 $$수식$${s2}$$/수식$$살이다.\n (다) 한 회원의 나이는 $$수식$${s3}$$/수식$$살이다.\n (라) 최빈값은 $$수식$${s4}$$/수식$$살로 $$수식$$2$$/수식$$명이 있다.$$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$살\n"
    comment = "(해설)\n" \
              "조건 (가), (다), (라)에 의하여 4명의 회원의 나이는 각각 $$수식$${s1}$$/수식$$살, $$수식$${s3}$$/수식$$살, $$수식$${s4}$$/수식$$살, $$수식$${s4}$$/수식$$살이다.\n" \
              "나머지 한 회원의 나이를 $$수식$$x$$/수식$$살이라 하면\n" \
              "조건 (나)에 의하여\n" \
              "$$수식$$ {{ {s1} + {s3} + {s4} + {s4} + x }} over {{5}} = {s2}$$/수식$$\n" \
              "$$수식$$ {c1} + x = {c2} THEREFORE x = {c3}$$/수식$$\n" \
              "따라서 나머지 한 회원의 나이는 $$수식$${c3}$$/수식$$살이다.\n\n"

    q1 = ['동호회', '동아리', '축구팀', '야구팀'][np.random.randint(0, 4)]

    list_1 = [13, 14, 16, 15]
    list_2 = [10, 12, 16, 14]
    list_3 = [9, 15, 16, 17]
    list_4 = [11, 13, 17, 15]
    list_5 = [10, 13, 14, 15]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 20)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0

    s1, s3, s4, x = list_A2
    s2 = (s1 + s3 + s4 + s4 + x) / 5
    c1 = s1 + s3 + s4 + s4
    c2 = s2 * 5
    c3 = c2 - c1
    s1, s2, s3, s4, c1, c2, c3 = RoundCheck([s1, s2, s3, s4, c1, c2, c3])
    
    a1 = c3

    stem = stem.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4)
    answer = answer.format(a1=a1)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, c1=c1, c2=c2, c3=c3)
    return stem, answer, comment


def statistics326_Stem_036():
    stem = "다음 $$수식$$8$$/수식$$개 자료의 중앙값은 $$수식$$a + 2$$/수식$$이고, 최빈값은 $$수식$$a$$/수식$$일 때, $$수식$$a$$/수식$$의 값을 구하시오.\n" \
            "$$표$$$$수식$${s1}, {s2}, {s3}, {s4}, a, {s5}, {s6}, {s7}$$/수식$$$$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "주어진 자료에서 $$수식$$a$$/수식$$를 제외한 $$수식$$7$$/수식$$개의 변량을 작은 값부터 순서대로 나열하면\n" \
              "$$수식$${c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}$$/수식$$\n" \
              "이때 최빈값이 $$수식$$a$$/수식$$이므로\n" \
              "$$수식$$a = {c3}$$/수식$$ 또는 $$수식$$a = {c4}$$/수식$$\n" \
              "(i) $$수식$$a = {c3}$$/수식$$인 경우 변량을 작은 값부터 순서대로 나열하면\n" \
              "$$수식$${c1}, {c2}, {c3}, {c3}, {c4}, {c5}, {c6}, {c7}$$/수식$$\n" \
              "따라서 중앙값은 $$수식$$ {{ {c3} + {c4} }} over {{2}} = {c8}$$/수식$$이고, $$수식$$a + 2 = {c8}$$/수식$$이므로 조건을 만족시킨다.\n" \
              "(ii) $$수식$$a = {c4}$$/수식$$인 경우 변량을 작은 값부터 순서대로 나열하면\n" \
              "$$수식$${c1}, {c2}, {c3}, {c4}, {c4}, {c5}, {c6}, {c7}$$/수식$$\n" \
              "따라서 중앙값은 $$수식$$ {{ {c4} + {c4} }} over {{2}} = {c4}$$/수식$$이고, $$수식$$a + 2 = {c8}$$/수식$$이므로 조건을 만족시키지 않는다.\n" \
              "(i), (ii)에서 $$수식$$a = {c3}$$/수식$$\n\n"

    list_1 = [14, 18, 18, 22, 22, 26, 28]
    list_2 = [10, 18, 18, 22, 22, 23, 24]
    list_3 = [2, 8, 8, 12, 12, 14, 20]
    list_4 = [4, 8, 8, 12, 12, 15, 16]
    list_5 = [6, 8, 8, 12, 12, 16, 17]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 20)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0
    c1, c2, c3, c4, c5, c6, c7 = list_A2

    np.random.shuffle(list_A2)
    s1, s2, s3, s4, s5, s6, s7 = list_A2

    c8 = c4 + 2
    
    a1 = c3

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7)
    answer = answer.format(a1=a1)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8)
    return stem, answer, comment


def statistics326_Stem_037():
    stem = "어떤 자료의 편차가 다음과 같을 때, $$수식$$x$$/수식$$의 값을 구하시오.\n" \
            "$$표$$$$수식$${s1}, {s2}, x, {s3}, {s4}  $$/수식$$$$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "편차의 총합은 $$수식$$0$$/수식$$이므로\n" \
              "$$수식$$({s1}) + ({s2}) + x + {s3} + {s4} = 0$$/수식$$\n" \
              "$$수식$$THEREFORE x = {c1}$$/수식$$\n\n"

    list_1 = [-4, -1, 3, 1]
    list_2 = [-4, -2, 3, 2]
    list_3 = [-5, -2, 4, 1]
    list_4 = [-4, -5, 3, 2]
    list_5 = [-5, -1, 3, 2]

    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    s1, s2, s3, s4 = list_A2
    t0 = np.random.randint(0, 3)
    s2 -= t0
    s3 += t0
    t0 = np.random.randint(0, 3)
    s1 -= t0
    s4 += t0
    
    c1 = -s1 - s2 - s3 - s4
    
    a1 = c1

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4)
    answer = answer.format(a1=a1)
    comment = comment.format(c1=c1, s1=s1, s2=s2, s3=s3, s4=s4)
    return stem, answer, comment


def statistics326_Stem_038():
    stem = "아래 자료는 {q1}네 반 학생 $$수식$$ 6$$/수식$$명의 {q2} 점수를 조사하여 나타낸 것이다. 다음 중 이 변량들의 편차가 될 수 없는 것은?\n" \
        "$$표$$ $$수식$${s1}, {s2}, {s3}, {s4}, {s5}, {s6}$$/수식$$ (단위: 점)$$/표$$\n" \
        "① $$수식$${ss1}$$/수식$$점\n" \
        "② $$수식$${ss2}$$/수식$$점\n" \
        "③ $$수식$${ss3}$$/수식$$점\n" \
        "④ $$수식$${ss4}$$/수식$$점\n" \
        "⑤ $$수식$${ss5}$$/수식$$점\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "(평균)" \
              "$$수식$$= {{ {s1} + {s2} + {s3} + {s4} + {s5} + {s6} }} over {{6}}$$/수식$$\n$$수식$$= {{{c1}}} over {{6}} = {c2}$$/수식$$(점)이므로\n" \
              "각 변량의 편차를 차례대로 구해 보면\n" \
              "$$수식$${s1} - {c2} = {c3}$$/수식$$(점), $$수식$${s2} - {c2} = {c4}$$/수식$$(점),\n" \
              "$$수식$${s3} - {c2} = {c5}$$/수식$$(점), $$수식$${s4} - {c2} = {c6}$$/수식$$(점),\n" \
              "$$수식$${s5} - {c2} = {c7}$$/수식$$(점), $$수식$${s6} - {c2} = {c8}$$/수식$$(점)\n" \
              "따라서 이 변량들의 편차가 될 수 없는 것은 $$수식$${c9}$$/수식$$점이다.\n\n"

    
    q1 = ['이준이', '하은이', '수민이', '민제'][np.random.randint(0, 4)]
    q2 = ['영어 퀴즈', '국어', '체육 수행 평가', '수학'][np.random.randint(0, 4)]

    list_1 = [19, 21, 22, 24, 26, 26]
    list_2 = [18, 19, 20, 24, 28, 29]
    list_3 = [17, 19, 22, 26, 27, 27]
    list_4 = [17, 19, 20, 24, 29, 29]
    list_5 = [16, 18, 22, 26, 28, 28]
    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 20)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0
    s1, s2, s3, s4, s5, s6 = list_A2
    
    c1 = s1 + s2 + s3 + s4 + s5 + s6
    c2 = c1 // 6
    c3 = s1 - c2
    c4 = s2 - c2
    c5 = s3 - c2
    c6 = s4 - c2
    c7 = s5 - c2
    c8 = s6 - c2
    c9 = [c3 - 1, 0, c8 + 1][np.random.randint(0, 3)]

    a1 = c9

    s_candidates = [c3, c4, c5, c7, c9]
    np.random.shuffle(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break
    s_candidates = RoundCheck(s_candidates)

    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9)
    return stem, answer, comment


def statistics326_Stem_039():
    stem = "{q1}네 반 학생들의 {q2} 성적의 평균은 $$수식$${q3}$$/수식$$점이다. {q1}의 {q2} 성적의 편차가 $$수식$${q4}$$/수식$$일 때, {q1}의 {q2} 성적을 구하시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$점\n"
    comment = "(해설)\n" \
              "$$수식$${q3} + {q4} = {c1}$$/수식$$(점)\n\n"

    q1 = ['이준이', '하은이', '수민이', '민제'][np.random.randint(0, 4)]
    q2 = ['영어 퀴즈', '국어', '체육 수행 평가', '수학'][np.random.randint(0, 4)]
    q3 = np.random.randint(50, 90)
    q4 = np.random.randint(1, 9)
    c1 = q3 + q4
    
    a1 = c1

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4)
    answer = answer.format(a1=a1)
    comment = comment.format(c1=c1, q3=q3, q4=q4)
    return stem, answer, comment


def statistics326_Stem_040():
    stem = "다음은 $$수식$$5$$/수식$$회에 걸쳐 실시한 {q2} 시험에서 {q1}가 받은 점수를 나타낸 것이다. {q2} 점수의 분산은? \n" \
        "$$표$$$$수식$${s1}, {s2}, {s3}, {s4}, {s5} $$/수식$$(단위: 점)$$/표$$\n" \
        "① $$수식$${ss1}$$/수식$$\n" \
        "② $$수식$${ss2}$$/수식$$\n" \
        "③ $$수식$${ss3}$$/수식$$\n" \
        "④ $$수식$${ss4}$$/수식$$\n" \
        "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "(평균)$$수식$$= {{ {s1} + {s2} + {s3} + {s4} + {s5} }} over {{5}}$$/수식$$\n$$수식$$= {{{c1}}} over {{5}} = {c2}$$/수식$$\n" \
              "각 변량의 편차를 차례대로 구해 보면\n" \
              "$$수식$${s1} - {c2} = {c3}$$/수식$$, $$수식$${s2} - {c2} = {c4}$$/수식$$, $$수식$${s3} - {c2} = {c5}$$/수식$$,\n" \
              "$$수식$${s4} - {c2} = {c6}$$/수식$$, $$수식$${s5} - {c2} = {c7}$$/수식$$ 따라서 분산은\n" \
              "" \
              "$$수식$${{ ({c3})^{{2}} + {c4}^{{2}} + {c5}^{{2}} + ({c6})^{{2}} + {c7}^{{2}} }} over {{5}} = {{{c8}}} over {{5}} = {c9}$$/수식$$\n\n"

    
    q1 = ['이준이', '하은이', '수민이', '민제'][np.random.randint(0, 4)]
    q2 = ['영어 퀴즈', '국어', '체육 수행 평가', '수학'][np.random.randint(0, 4)]

    list_1 = [10, 12, 12, 10, 11]
    list_2 = [8, 12, 12, 10, 13]
    list_3 = [9, 11, 11, 10, 14]
    list_A2 = [list_1, list_2, list_3][np.random.randint(0, 3)]
    t0 = np.random.randint(0, 20)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0
    s1, s2, s3, s4, s5= list_A2
    
    c1 = s1 + s2 + s3 + s4 + s5
    c2 = c1 / 5
    c3 = s1 - c2
    c4 = s2 - c2
    c5 = s3 - c2
    c6 = s4 - c2
    c7 = s5 - c2
    c8 = int(np.square(c3) + np.square(c4) + np.square(c5) + np.square(c6) + np.square(c7))
    c9 = round(c8 / 5, 1)
    c1, c2, c3, c4, c5, c6, c7, c8, c9 = RoundCheck([c1, c2, c3, c4, c5, c6, c7, c8, c9])

    a1 = c9
    
    s_candidates = [0, round(c9 - 0.6,1), c9, c9 * 5, c9 * 10]
    s_candidates = RoundCheck(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9)
    return stem, answer, comment


def statistics326_Stem_041():
    stem = "$$수식$$5$$/수식$$개의 변량  $$수식$$ {s1}, {s2},x , {s3}, {s4}$$/수식$$의 평균이 $$수식$${c1}$$/수식$$일 때, 분산은?\n" \
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "평균이 $$수식$${c1}$$/수식$$이므로\n" \
              "$$수식$${{ {s1} + {s2} + x + {s3} + {s4} }} over {{5}} = {c1}$$/수식$$, $$수식$${c2} + x = {c3}$$/수식$$\n" \
              "$$수식$$THEREFORE x = {c4}$$/수식$$\n" \
              "따라서 각 자료의 편차는\n" \
              "$$수식$${d1}, {d2}, {d3}, {d4}, {d5}$$/수식$$이므로 분산은\n" \
              "$$수식$${{ ({d1})^{{2}} + {d2}^{{2}} + {d3}^{{2}} + {d4}^{{2}} + ({d5})^{{2}} }} over {{5}} = {{ {c5} }} over {{5}} = {c6}$$/수식$$\n\n"

    list_1 = [2, 6, 8, 10, 4]
    list_2 = [3, 5, 8, 6, 3]
    list_3 = [2, 5, 7, 8, 3]
    list_4 = [2, 4, 6, 10, 3]
    list_5 = [1, 6, 7, 9, 2]
    
    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 7);
    for i in range(len(list_A2)):
        list_A2[i] += t0
    s1, s2, x, s3, s4 = list_A2

    c1 = (s1 + s2 + x + s3 + s4) // 5
    c2 = s1 + s2 + s3 + s4
    c3 = c1 * 5
    c4 = c3 - c2
    
    d1 = s1 - c1
    d2 = s2 - c1
    d3 = x - c1
    d4 = s3 - c1
    d5 = s4 - c1

    c5 = d1**2 + d2**2 + d3**2 + d4**2 + d5**2
    c6 = RoundCheck([c5 / 5])[0]

    a1 = c6
    t1 = [round(a1-0.4, 1), round(a1-0.2, 1), a1, round(a1+0.2, 1), round(a1+0.4, 1)][np.random.randint(0,5)]
    s_candidates = [t1 - 0.4, t1 - 0.2, t1, t1 + 0.2, t1 + 0.4]
    for i in range(len(s_candidates)):
        s_candidates[i]=round(s_candidates[i], 1)
    s_candidates = RoundCheck(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, c1=c1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5)

    return stem, answer, comment



def statistics326_Stem_042():
    stem = "다음 자료의 분산과 표준편차를 각각 구하면?\n" \
           "$$표$$$$수식$$ {s1}, {s2}, {s3}, {s4}, {s5}$$/수식$$$$/표$$\n" \
           "① 분산: $$수식$$ {v1}$$/수식$$ , 표준편차: {sd1}\n" \
           "② 분산: $$수식$$ {v2}$$/수식$$ , 표준편차: {sd2}\n" \
           "③ 분산: $$수식$$ {v3}$$/수식$$ , 표준편차: {sd3}\n" \
           "④ 분산: $$수식$$ {v4}$$/수식$$ , 표준편차: {sd4}\n" \
           "⑤ 분산: $$수식$$ {v5}$$/수식$$ , 표준편차: {sd5}\n"
    answer = "(답):$$수식$$ {a1}$$/수식$$ \n"
    comment = "(해설)\n" \
              "주어진 자료의 평균은\n" \
              "$$수식$${{ {s1} + {s2} + {s3} + {s4} + {s5} }} over {{5}} = {{ {c1} }} over {{5}} = {c2}$$/수식$$\n" \
              "$$수식$$THEREFORE $$/수식$$ (분산) $$수식$$= {{ ({d1})^{{2}} + ({d2})^{{2}} + {d3}^{{2}} + {d4}^{{2}} + {d5}^{{2}} }} over {{5}}$$/수식$$\n" \
              "\t$$수식$$= {{ {c3} }} over {{5}} = {c4}$$/수식$$\n" \
              "(표준편차) $$수식$$= sqrt{{{c4}}}$$/수식$$\n\n"

    list_1 = [3, 4, 5, 6, 7]
    list_2 = [1, 3, 5, 7, 9]
    list_3 = [1, 2, 5, 8, 9]
    list_4 = [1, 4, 5, 6, 9]
    list_5 = [1, 2, 6, 7, 9]
    
    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 7);
    for i in range(len(list_A2)):
        list_A2[i] += t0
    s1, s2, s3, s4, s5 = list_A2

    c1 = s1 + s2 + s3 + s4 + s5
    c2 = c1 // 5
    
    d1 = s1 - c2
    d2 = s2 - c2
    d3 = s3 - c2
    d4 = s4 - c2
    d5 = s5 - c2

    c3 = d1**2 + d2**2 + d3**2 + d4**2 + d5**2
    c4 = RoundCheck([c3 / 5])[0]

    a1 = c4
    if a1<=2:
        t1 = [a1, a1+1, a1+2][np.random.randint(0,3)]
    else:
        t1 = [a1-2, a1-1, a1, a1+1, a1+2][np.random.randint(0,5)]
    s_candidates = [t1 - 2, t1 - 1, t1, t1 + 1, t1 + 2]
    for i in range(len(s_candidates)):
        s_candidates[i]=round(s_candidates[i], 1)
    s_candidates = RoundCheck(s_candidates)
    v1, v2, v3, v4, v5 = s_candidates
    sd_list = []
    for i in range(len(s_candidates)):
        if np.sqrt(s_candidates[i]) % 1 == 0:
            sd_list.append("$$수식$$" + str(int(np.sqrt(s_candidates[i]))) + "$$/수식$$")
        else:
            sd_list.append("$$수식$$sqrt{{{"+str(s_candidates[i])+"}}}$$/수식$$")
    sd1, sd2, sd3, sd4, sd5 = sd_list
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, c1=c1, v1=v1, v2=v2, v3=v3, v4=v4, v5=v5, sd1=sd1, sd2=sd2, sd3=sd3, sd4=sd4, sd5=sd5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, c1=c1, c2=c2, c3=c3, c4=c4, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5)

    return stem, answer, comment



def statistics326_Stem_043():
    stem = "다음 중 아래 자료에 대한 설명으로 옳은 것은?\n" \
           "$$표$$$$수식$$ {s1}, {s2}, {s3}, {s4}$$/수식$$ $$/표$$\n" \
           "① 평균은 $$수식$$ {ss1}$$/수식$$ 이다.\n" \
           "② 분산은 $$수식$$ {ss2}$$/수식$$ 이다.\n" \
           "③ 표준편차는 $$수식$$ {ss3}$$/수식$$ 이다.\n" \
           "④ 편차의 총합은 $$수식$$ {ss4}$$/수식$$ 이다.\n" \
           "⑤ 편차의 제곱의 총합은 $$수식$$ {ss5}$$/수식$$ 이다.\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "① (평균) $$수식$$ = {{ {s1} + {s2} + {s3} + {s4} }} over {{4}}$$/수식$$\n$$수식$$= {{ {c1} }} over {{4}} = {ans1}$$/수식$$\n" \
              "② (분산) $$수식$$= {{ {d1}^{{2}} + ({d2})^{{2}} + ({d3})^{{2}} + {d4}^{{2}} }} over {{4}}$$/수식$$\n$$수식$$= {{ {c2} }} over {{4}} = {ans2}$$/수식$$\n" \
              "③ 표준편차는 $$수식$$ {ans3}$$/수식$$ 이다.\n" \
              "④ 편차의 총합은 $$수식$$ {ans4}$$/수식$$ 이다.\n" \
              "⑤ 편차의 제곱의 총합은 $$수식$$ {ans5}$$/수식$$ 이다.\n" \
              "따라서 옳은 것은  $$수식$$ {a1}$$/수식$$ 이다.\n\n"

    list_1 = [8, 5, 5, 6]
    list_2 = [7, 1, 3, 5]
    list_3 = [8, 1, 2, 5]
    list_4 = [7, 2, 4, 7]
    list_5 = [7, 1, 2, 6]
    
    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 7);
    for i in range(len(list_A2)):
        list_A2[i] += t0
    s1, s2, s3, s4 = list_A2

    ans = list(range(5))
    ss = list(range(5))
    
    c1 = s1 + s2 + s3 + s4
    ans[0] = c1 // 4
    
    d1 = s1 - ans[0]
    d2 = s2 - ans[0]
    d3 = s3 - ans[0]
    d4 = s4 - ans[0]
    c2 = d1**2 + d2**2 + d3**2 + d4**2
    ans[1] = RoundCheck([c2 / 4])[0]

    if np.sqrt(ans[1]) % 1 == 0:
        ans[2] = int(np.sqrt(ans[1]))
        ss[2] = ans[2] + 1
    else:
        ans[2] = "$$수식$$sqrt{{{"+str(ans[1])+"}}}$$/수식$$"
        ss[2] = "$$수식$$sqrt{{{"+str(ans[1]+1)+"}}}$$/수식$$"
    
    ans[3] = d1 + d2 + d3 + d4
    ans[4] = c2
    
    ss[0] = ans[0] - 1
    ss[1] = ans[1] + 0.5
    ss[3] = ans[3] + 1
    ss[4] = ans[4] * 2

    correct_idx = np.random.randint(0,5)
    ss[correct_idx] = ans[correct_idx]

    ans = RoundCheck(ans)
    ss = RoundCheck(ss)

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, ss1=ss[0], ss2=ss[1], ss3=ss[2], ss4=ss[3], ss5=ss[4])
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, c1=c1, c2=c2, d1=d1, d2=d2, d3=d3, d4=d4, ans1=ans[0], ans2=ans[1], ans3=ans[2], ans4=ans[3], ans5=ans[4], a1=answer_dict[correct_idx])

    return stem, answer, comment


def statistics326_Stem_044():
    stem = "세 수 $$수식$$a + {s1},` {s2},` {s3} - a$$/수식$$의 표준편차가 $$수식$$sqrt{{{q1}}}$$/수식$$일 때, 양수 $$수식$$a$$/수식$$의 값은?\n"  \
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "(평균) $$수식$$={{ (a + {s1}) + {s2} + ({s3} - a ) }} over {{3}} = {{ {c1} }} over {{3}} = {c2}$$/수식$$\n" \
              "(분산)$$수식$$= {{ a^{{2}} + ( {c3} )^{{2}} + ({c4} - a )^{{2}} }} over {{3}}$$/수식$$\n"   \
              "$$수식$$= {{ 2a^{{2}} - {c5}a + {c6} }} over {{3}} = $$/수식$$($$수식$$sqrt{{{q1}}}$$/수식$$)$$수식$$^{{2}}$$/수식$$\n" \
              "이므로 $$수식$$2a^{{2}} - {c5}a + {c6} = {c7}$$/수식$$, $$수식$$a^{{2}} - a + {c9} = {c10}$$/수식$$\n" \
              "$$수식$$a^{{2}} - a - {c11} = 0$$/수식$$, $$수식$$(a - {aa1})(a + {aa2}) = 0$$/수식$$\n" \
              "따라서 $$수식$$a = {aa1}$$/수식$$ ($$수식$$BECAUSE a &gt; 0$$/수식$$)\n\n"
              
    list_1 = [5, 4, 6, 2, 1, 2]
    list_2 = [5, 4, 6, 2, 1, 2]
    list_3 = [5, 4, 6, 2, 1, 2]
    
    list_A2 = [list_1, list_2, list_3][np.random.randint(0, 3)]
    t0 = np.random.randint(0,10)
    for i in range(3):
        list_A2[i] += t0
    s1, s2, s3, aa1, aa2, q1 = list_A2

    c1 = s1 + s2 + s3
    c2 = c1 / 3
    c3 = s2 - c2
    c4 = s3 - c2
    c5 = c4 * 2
    c6 = np.square(c3) + np.square(c4)
    c7 = q1 * 3
    c8 = c5 / 2
    c9 = c6 / 2
    c10 = c7 / 2
    c11 = c10 - c9

    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11 = RoundCheck([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11])

    a1 = aa1

    t1 = [a1-4, a1-2, a1, a1+2, a1+4][np.random.randint(0,5)]
    s_candidates = np.array([t1 - 4, t1 - 2, t1, t1 + 2, t1 + 4])
    while( s_candidates[0] < 0 ):
        s_candidates = s_candidates + 2
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
            break

    stem = stem.format(s1=s1, s2=s2, s3=s3, q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, q1=q1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, aa1=aa1, aa2=aa2)

    return stem, answer, comment



def statistics326_Stem_045():
    stem = "$$수식$$3$$/수식$$개의 변량 $$수식$$ {s1}, a + {s1} ,  2a + {s1}$$/수식$$의 분산이 $$수식$$ {s2}$$/수식$$ 일 때, 양수 $$수식$$a$$/수식$$의 값을 구하시오.\n"
    answer = "(답):$$수식$$ {a1}$$/수식$$ \n"
    comment = "(해설)\n" \
              "(평균) $$수식$$ = {{ {s1} + (a + {s1}) + (2a + {s1}) }} over {{3}} = a + {s1}$$/수식$$\n" \
              "각 변량의 편차를 차례대로 구하면\n" \
              "$$수식$${s1} - (a + {s1}) = -a$$/수식$$, $$수식$$(a + {s1}) - (a + {s1}) = 0$$/수식$$\n" \
              "$$수식$$(2a + {s1}) - (a + {s1}) = a$$/수식$$\n" \
              "분산이 $$수식$${s2}$$/수식$$이므로\n" \
              "$$수식$${{ (-a )^{{2}} + {{0}}^{{2}} + a^{{2}} }} over {{3}} = {{ 2a^{{2}} }} over {{3}} = {s2}$$/수식$$\n" \
              "$$수식$$ 2a^{{2}} = {c1}$$/수식$$, $$수식$$ a^{{2}} = {c2}$$/수식$$\n" \
              "$$수식$$ THEREFORE a = {c3} ( BECAUSE a&gt;0 )$$/수식$$\n\n"

    s1 = np.random.randint(2, 8)
    s2 = [6, 24, 54, 96][np.random.randint(0,4)]

    c1 = 3 * s2
    c2 = c1 // 2
    c3 = int(np.sqrt(c2))

    a1 = c3

    stem = stem.format(s1=s1, s2=s2)
    answer = answer.format(a1=a1)
    comment = comment.format(s1=s1, s2=s2, c1=c1, c2=c2, c3=c3)

    return stem, answer, comment



def statistics326_Stem_046():
    stem = "학생 $$수식$${s1}$$/수식$$명의 {q1} 성적의 평균은 $$수식$${s2}$$/수식$$점이고 분산은 $$수식$${s3}$$/수식$$이다. {q1} 성적이 $$수식$${s2}$$/수식$$점인 학생 한 명이 새로 들어왔을 때, 학생 $$수식$${s4}$$/수식$$명의 {q1} 성적의 분산은?\n" \
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "학생 $$수식$${s1}$$/수식$$명의 $$수식$$({q2})^{{2}}$$/수식$$의 총합 $$수식$$ = {s3} times {s1} = {c1}$$/수식$$\n" \
              "이때 새로 들어온 학생의 {q1} 성적이 평균과 같으므로\n$$수식$$({q2})^{{2}}$$/수식$$의 총합에는 변화가 없다.\n" \
              "$$수식$$THEREFORE$$/수식$$ (분산) $$수식$$ = {{ {c1} }} over {{ {s4} }} = {c2}$$/수식$$\n\n"

    
    q1 = ["과학", "수학", "영어", "국어", "사회"][np.random.randint(0,5)]
    q2 = "$$/수식$$편차$$수식$$"
    s1 = np.random.randint(4,9)
    s2 = np.random.randint(8,19) * 5
    s3 = np.random.randint(2,5) * (s1+1)
    s4 = s1 + 1

    c1 = s1 * s3
    c2 = c1 // s4

    a1 = c2
    t1 = [a1-10, a1-5, a1, a1+5, a1+10][np.random.randint(0,5)]
    s_candidates = np.array([t1 - 10, t1 - 5, t1, t1 + 5, t1 + 10])
    while( s_candidates[0] < 0 ):
        s_candidates = s_candidates + 5
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s3=s3, s4=s4, q1=q1, q2=q2, c1=c1, c2=c2)

    return stem, answer, comment



def statistics326_Stem_047():
    stem = "다음 중 아래 자료에 대한 설명으로 옳은 것은?\n" \
           "$$표$$$$수식$$ {s1}, {s2}, {s3}, {s4}, {s4}, {s5}, {s6}, {s7}$$/수식$$ $$/표$$\n" \
           "① 평균은 $$수식$$  {ss1}$$/수식$$ 이다.\n" \
           "② 중앙값은 $$수식$$ {ss2}$$/수식$$ 이다.\n" \
           "③ 최빈값은 $$수식$$ {ss3}$$/수식$$ 이다.\n" \
           "④ 분산은 $$수식$$ {ss4}$$/수식$$ 이다.\n" \
           "⑤ 표준편차는 $$수식$$ {ss5}$$/수식$$ 이다.\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "① (평균) $$수식$$ = {{ {s1} + {s2} + {s3} + {s4} + {s5} + {s6} + {s7} }} over {{7}}$$/수식$$\n$$수식$$= {{ {c1} }} over {{7}} = {ans1}$$/수식$$\n" \
              "② 자료를 작은 값부터 크기순으로 나열하면 $$수식$$  {f1}, {f2}, {f3}, {f4}, {f5}, {f6}, {f7}$$/수식$$ 이므로\n중앙값은 $$수식$${ans2}$$/수식$$이다.\n" \
              "③ $$수식$$ {ans31}$$/수식$$ 과 $$수식$$ {ans32}$$/수식$$ 가 각각 두 번씩 가장 많이 나타나므로 최빈값은 $$수식$$ {ans31}$$/수식$$ 과 $$수식$$  {ans32}$$/수식$$ 이다.\n" \
              "④ (분산)\n$$수식$$= {{ {d1}^{{2}} + ({d2})^{{2}} + ({d3})^{{2}} + ({d4})^{{2}} + {d5}^{{2}} + {d6}^{{2}} + {d7}^{{2}} }} over {{7}}$$/수식$$\n$$수식$$ = {{ {c2} }} over {{7}} = {ans4}$$/수식$$\n" \
              "⑤ (표준편차) $$수식$$ =$$/수식$$ {ans5}\n" \
              "따라서 옳은 것은 {a1}이다.\n\n"

    list_1 = [11, 5, 7, 5, 9, 10, 9]
    list_2 = [9, 4, 3, 4, 6, 7, 9]
    list_3 = [10, 4, 6, 4, 7, 9, 9]
    
    list_A2 = [list_1, list_2, list_3][np.random.randint(0, 3)]
    t0 = np.random.randint(0, 7);
    for i in range(len(list_A2)):
        list_A2[i] += t0
    s1, s2, s3, s4, s5, s6, s7 = list_A2
    list_A2_sorted = sorted(list_A2)
    f1, f2, f3, f4, f5, f6, f7 = list_A2_sorted

    ans = list(range(5))
    ans[2] = []
    ss = list(range(5))
    
    c1 = s1 + s2 + s3 + s4 + s5 + s6 + s7
    ans[0] = c1 // 7
    ans[1] = f4

    for i in range(len(list_A2_sorted)-1):
        if list_A2_sorted[i] == list_A2_sorted[i+1]:
            ans[2].append(list_A2_sorted[i])

    d1 = s1 - ans[0]
    d2 = s2 - ans[0]
    d3 = s3 - ans[0]
    d4 = s4 - ans[0]
    d5 = s5 - ans[0]
    d6 = s6 - ans[0]
    d7 = s7 - ans[0]
    c2 = d1**2 + d2**2 + d3**2 + d4**2 + d5**2 + d6**2 + d7**2
    ans[3] = RoundCheck([round(c2 / 7, 1)])[0]

    if np.sqrt(ans[3]) % 1 == 0:
        ans[4] = int(np.sqrt(ans[3]))
        ss[4] = ans[3] + 1
    else:
        ans[4] = "$$수식$$sqrt{{{"+str(ans[3])+"}}}$$/수식$$"
        ss[4] = "$$수식$$sqrt{{{"+str(ans[3]+1)+"}}}$$/수식$$"
    
    ss[0] = ans[0] + 1
    ss[1] = f6
    ss[2] = ans[2][0]
    ss[3] = round(ans[3] - 1, 1)

    correct_idx = np.random.randint(0,5)
    if correct_idx == 2:
        ss[2] = str(ans[2][0]) + ", " + str(ans[2][1])
    else:
        ss[correct_idx] = ans[correct_idx]

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, ss1=ss[0], ss2=ss[1], ss3=ss[2], ss4=ss[3], ss5=ss[4])
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6, s7=s7, c1=c1, c2=c2, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5, d6=d6, d7=d7, f1=f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, ans1=ans[0], ans2=ans[1], ans31=ans[2][0], ans32=ans[2][1], ans4=ans[3], ans5=ans[4], a1=answer_dict[correct_idx])

    return stem, answer, comment



def statistics326_Stem_048():
    stem = "$$수식$$5$$/수식$$개의 변량 $$수식$${s1}, {s2},$$/수식$$ $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$의 중앙값과 최빈값이 모두 $$수식$${c1}$$/수식$$이고, 평균이 $$수식$${c2}$$/수식$$일 때, 분산을 소수로 나타내시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$a LEQ b LEQ c$$/수식$$라 하면 중앙값과 최빈값이 $$수식$${c1}$$/수식$$이므로 $$수식$$a = {s3}$$/수식$$, $$수식$$b = {s4}$$/수식$$\n" \
              "이때 평균이 $$수식$${c1}$$/수식$$이므로 $$수식$${{ {s1} + {s2} + {s3} + {s4} + c }} over {{5}} = {c2}$$/수식$$\n" \
              "$$수식$${c3} + c = {c4} `` THEREFORE c = {s5}$$/수식$$\n" \
              "따라서 분산은\n" \
              "$$수식$$ = {{ ({d1})^{{2}} + ({d2})^{{2}} + {d3}^{{2}} + {d4}^{{2}} + {d5}^{{2}} }} over {{5}}$$/수식$$\n" \
              "$$수식$$ = {{ {c5} }} over {{5}} = {c6}$$/수식$$\n\n"

    list_1 = np.array([4, 6, 9, 9, 12])
    list_2 = np.array([3, 4, 7, 7, 9])
    list_3 = np.array([3, 5, 7, 7, 8])
    list_4 = np.array([2, 5, 9, 9, 10])

    list_A2 = [list_1, list_2, list_3, list_4][np.random.randint(0,4)] + np.random.randint(0,7)
    s1, s2, s3, s4, s5 = list_A2

    c1 = s3
    c2 = (s1 + s2 + s3 + s4 + s5) // 5
    c3 = s1 + s2 + s3 + s4
    c4 = c2 * 5

    d1 = s1 - c2
    d2 = s2 - c2
    d3 = s3 - c2
    d4 = s4 - c2
    d5 = s5 - c2

    c5 = d1**2 + d2**2 + d3**2 + d4**2 + d5**2
    c6 = round(c5 / 5, 1)

    a1 = c6

    stem = stem.format(s1=s1, s2=s2, c1=c1, c2=c2)
    answer = answer.format(a1=a1)
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5)

    return stem, answer, comment



def statistics326_Stem_049():
    stem = "$$수식$$5$$/수식$$개의 변량  $$수식$$ {s1}, {s2},$$/수식$$ $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$의 중앙값과 최빈값이 모두 $$수식$${c1}$$/수식$$이고, 평균이 $$수식$${c2}$$/수식$$일 때, 표준편차는?\n" \
           "① {ss1}\n" \
           "② {ss2}\n" \
           "③ {ss3}\n" \
           "④ {ss4}\n" \
           "⑤ {ss5}\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a LEQ b LEQ c$$/수식$$라고 하면 중앙값과 최빈값이 $$수식$${c1}$$/수식$$이므로 $$수식$$a = {s3}$$/수식$$, $$수식$$b = {s4}$$/수식$$\n" \
              "또, 평균이 $$수식$${c1}$$/수식$$이므로 $$수식$${{ {s1} + {s2} + {s3} + {s4} + c }} over {{5}} = {c2}$$/수식$$에서 $$수식$$c = {s5}$$/수식$$\n" \
              "따라서 분산은\n" \
              "$$수식$$ = {{ ({d1})^{{2}} + ({d2})^{{2}} + {d3}^{{2}} + {d4}^{{2}} + {d5}^{{2}} }} over {{5}} = {{ {c3} }} over {{5}} = {c4}$$/수식$$\n" \
              "이므로 표준편차는 {c5}이다.\n\n"

    list_1 = np.array([4, 6, 9, 9, 12])
    list_2 = np.array([3, 4, 7, 7, 9])
    list_3 = np.array([3, 5, 7, 7, 8])
    list_4 = np.array([2, 5, 9, 9, 10])

    list_A2 = [list_1, list_2, list_3, list_4][np.random.randint(0,4)] + np.random.randint(0,7)
    s1, s2, s3, s4, s5 = list_A2

    c1 = s3
    c2 = (s1 + s2 + s3 + s4 + s5) // 5

    d1 = s1 - c2
    d2 = s2 - c2
    d3 = s3 - c2
    d4 = s4 - c2
    d5 = s5 - c2

    c3 = d1**2 + d2**2 + d3**2 + d4**2 + d5**2
    c4 = round(c3 / 5, 1)
    c5 = "$$수식$$sqrt{{{"+str(c4)+"}}}$$/수식$$"

    a1 = c4
    t1 = [c4-2.4, c4-1.2, c4, c4+1.2, c4+2.4][np.random.randint(0,5)]
    s_candidates = np.array([t1 - 2.4, t1 - 1.2, t1, t1 + 1.2, t1 + 2.4])
    while( s_candidates[0] < 0 ):
        s_candidates = s_candidates + 1.2
    s_candidates = list(s_candidates)
    s_candidates = Round(s_candidates, 1)
    ss = list(range(5))
    for i in range(len(ss)):
        if np.sqrt(s_candidates[i]) % 1 == 0:
            ss[i] = "$$수식$$"+int(np.sqrt(s_candidates[i]))+"$$/수식$$"
        else:
            ss[i] = "$$수식$$sqrt{{{"+str(s_candidates[i])+"}}}$$/수식$$"
    ss1 = ss[0]
    ss2 = ss[1]
    ss3 = ss[2]
    ss4 = ss[3]
    ss5 = ss[4]
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == c4:
                correct_idx = idx
                break

    stem = stem.format(s1=s1, s2=s2, c1=c1, c2=c2, ss1=ss[0], ss2=ss[1], ss3=ss[2], ss4=ss[3], ss5=ss[4])
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5)

    return stem, answer, comment


def statistics326_Stem_050():
    stem = "$$수식$$10$$/수식$$개의 변량 $$수식$$x_{{1}}$$/수식$$, $$수식$$x_{{2}}$$/수식$$, $$수식$$x_{{3}}$$/수식$$, $$수식$$CDOTS$$/수식$$, $$수식$$x_{{10}}$$/수식$$의 합이 $$수식$${q1}$$/수식$$이고 각각의 변량의 제곱의 합이 $$수식$${q2}$$/수식$$일 때, $$수식$$x_{{1}}$$/수식$$, $$수식$$x_{{2}}$$/수식$$, $$수식$$x_{{3}}$$/수식$$, $$수식$$CDOTS$$/수식$$, $$수식$$x_{{10}}$$/수식$$의 표준편차는?\n" \
        "① $$수식$$sqrt{{{ss1}}}$$/수식$$\n" \
        "② $$수식$$sqrt{{{ss2}}}$$/수식$$\n" \
        "③ $$수식$$sqrt{{{ss3}}}$$/수식$$\n" \
        "④ $$수식$$sqrt{{{ss4}}}$$/수식$$\n" \
        "⑤ $$수식$$sqrt{{{ss5}}}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$x_{{1}} + x_{{2}} + CDOTS + x_{{10}} = {q1}$$/수식$$이므로 평균은 $$수식$${{ {q1} }} over {{10}} = {c1}$$/수식$$\n" \
              "또, $$수식$$x_{{1}}^{{2}} + x_{{2}}^{{2}} + CDOTS + x_{{10}}^{{2}} = {q2}$$/수식$$이므로\n" \
              "분산은\n"    \
              "$$수식$${{ (x_{{1}}^{{2}} - {c1})^{{2}} + (x_{{2}}^{{2}} - {c1})^{{2}} + CDOTS + (x_{{10}}^{{2}} - {c1})^{{2}} }} over {{10}}$$/수식$$\n" \
              "$$수식$$= {{ x_{{1}}^{{2}} + x_{{2}}^{{2}} + CDOTS + x_{{10}}^{{2}} }} over {{10}}$$/수식$$\n" \
              "$$수식$$- {{ {c2} ( x_{{1}} + x_{{2}} + CDOTS + x_{{10}} ) + {c3} }} over {{10}}$$/수식$$\n" \
              "$$수식$$= {{ {q2} - {c2} times {q1} + {c5} }} over {{10}} = {c6}$$/수식$$\n" \
              "따라서 표준편차는 $$수식$$sqrt{{ {c6} }}$$/수식$$\n\n"
                  
    c6 = 1.1
    q2 = 0
    while (c6 != int(c6)) or (q2 <= 0):
        t0 = [2, 3, 5, 6, 7][np.random.randint(0, 5)]
        q1 = 10 * np.random.randint(2, 5)

        c1 = q1 / 10
        c2 = c1 * 2
        c3 = np.square(c1) * 10
        c4 = c2 * q1
        c5 = c3
        q2 = (10 * t0) - c5 + c4
        c6 = (q2 - c4 + c5) / 10

        c1, c2, c3, c4, c5, c6, q1, q2 = RoundCheck([c1, c2, c3, c4, c5, c6, q1, q2])

    a1 = c6
    s_candidates = [2, 3, 5, 6, 7]
    s_candidates = RoundCheck(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break
    s_candidates = RoundCheck(s_candidates)

    stem = stem.format(q1=q1, q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c5=c5, c6=c6)
    return stem, answer, comment


def statistics326_Stem_051():
    stem = "학생 $$수식$$6$$/수식$$명의 {s1} 점수의 평균이 $$수식$${q1}$$/수식$$점, 분신이 $$수식$${q2}$$/수식$$점이라고 한다. 이 학생 $$수식$$6$$/수식$$명 중에서 {s1} 점수가 $$수식$${q1}$$/수식$$점인 한 학생을 제외한 나머지 $$수식$$5$$/수식$$명의 {s1} 점수의 분산을 구하시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${q1}$$/수식$$점인 학생의 점수의 편차는 $$수식$$0$$/수식$$이므로\n" \
              "나머지 학생 $$수식$$5$$/수식$$명의 점수의 편차를 각각 $$수식$$a$$/수식$$점, $$수식$$b$$/수식$$점, $$수식$$c$$/수식$$점, $$수식$$d$$/수식$$점, $$수식$$e$$/수식$$점이라고 하자.\n" \
              "학생 $$수식$$6$$/수식$$명의 점수의 분산이 $$수식$${q2}$$/수식$$이므로\n" \
              "$$수식$${{ 0^{{2}} + a^{{2}} + b^{{2}} + c^{{2}} + d^{{2}} + e^{{2}} }} over {{6}} = {q2}$$/수식$$에서\n"    \
              "$$수식$$a^{{2}} + b^{{2}} + c^{{2}} + d^{{2}} + e^{{2}} = {c1}$$/수식$$\n" \
              "따라서 점수가 $$수식$${q1}$$/수식$$점인 한 학생을 제외한 나머지 학생 $$수식$$5$$/수식$$명의 점수의 평균도 $$수식$${q1}$$/수식$$점이므로\n"  \
              "학생 $$수식$$5$$/수식$$명의 분산은\n"  \
              "$$수식$${{ a^{{2}} + b^{{2}} + c^{{2}} + d^{{2}} + e^{{2}} }} over {{5}} = {c2}$$/수식$$\n\n"

    s1 = ['수학 수행 평가', '국어', '체육 수행 평가', '영어 퀴즈'][np.random.randint(0, 4)]
    q2 = np.random.randint(1,9) * 5
    q1 = np.random.randint(20, 90)
    
    c1 = q2 * 6
    c2 = c1 / 5
    c1, c2 = RoundCheck([c1, c2])

    a1 = c2

    stem = stem.format(q1=q1, q2=q2, s1=s1)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2)
    return stem, answer, comment


def statistics326_Stem_052():
    stem = "$$수식$$100$$/수식$$개의 변량의 총합이 $$수식$${q1}$$/수식$$이고 각 변량의 제곱의 총합이 $$수식$${q2}$$/수식$$인 자료의 표준편차는?\n" \
        "① $$수식$$sqrt{{{ss1}}}$$/수식$$\n" \
        "② $$수식$$sqrt{{{ss2}}}$$/수식$$\n" \
        "③ $$수식$$sqrt{{{ss3}}}$$/수식$$\n" \
        "④ $$수식$$sqrt{{{ss4}}}$$/수식$$\n" \
        "⑤ $$수식$$sqrt{{{ss5}}}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$100$$/수식$$개의 변량을 $$수식$$x_{{1}}$$/수식$$, $$수식$$x_{{2}}$$/수식$$, $$수식$$CDOTS$$/수식$$, $$수식$$x_{{100}}$$/수식$$이라 하면\n" \
              "$$수식$$x_{{1}} + x_{{2}} + CDOTS + x_{{100}} = {q1}$$/수식$$,\n" \
              "$$수식$$x_{{1}}^{{2}} + x_{{2}}^{{2}} + CDOTS + x_{{100}}^{{2}} = {q2}$$/수식$$,\n" \
              "(평균)$$수식$$= {{ x_{{1}} + x_{{2}} + CDOTS + x_{{100}} }} over {{100}} = {c1}$$/수식$$\n" \
              "(분산)\n"    \
              "$$수식$$= {{ (x_{{1}}^{{2}} - {c1})^{{2}} + (x_{{2}}^{{2}} - {c1})^{{2}} + CDOTS + (x_{{100}}^{{2}} - {c1})^{{2}} }} over {{100}}$$/수식$$\n" \
              "$$수식$$= {{ x_{{1}}^{{2}} + x_{{2}}^{{2}} + CDOTS + x_{{100}}^{{2}} }} over {{100}}$$/수식$$\n" \
              "$$수식$$- {{ {c2} ( x_{{1}} + x_{{2}} + CDOTS + x_{{100}} ) + {c3} times 100 }} over {{100}}$$/수식$$\n" \
              "$$수식$$= {{ {q2} - {c4} + {c5} }} over {{100}} = {c6}$$/수식$$\n" \
              "따라서 표준편차는 $$수식$$sqrt{{ {c6} }}$$/수식$$\n\n"
                  
    c6 = 1.1
    while (c6 != int(c6)):
        t0 = [2, 3, 5, 6, 7][np.random.randint(0, 5)]
        q1 = 100 * np.random.randint(2, 5)

        c1 = q1 / 100
        c2 = c1 * 2
        c3 = np.square(c1)
        c4 = c2 * q1
        c5 = c3 * 100
        q2 = (100 * t0) - c5 + c4
        c6 = (q2 - c4 + c5) / 100

        c1, c2, c3, c4, c5, c6, q1, q2 = RoundCheck([c1, c2, c3, c4, c5, c6, q1, q2])

    a1 = c6  
    s_candidates = [2, 3, 5, 6, 7]
    s_candidates = RoundCheck(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break
    s_candidates = RoundCheck(s_candidates)

    stem = stem.format(q1=q1, q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    return stem, answer, comment


def statistics326_Stem_053():
    stem = "$$수식$$5$$/수식$$개의 변량  $$수식$${s1} $$/수식$$, $$수식$$x$$/수식$$,  $$수식$${s2} $$/수식$$, $$수식$${s3} - x$$/수식$$,  $$수식$${s4} $$/수식$$의 분산이 $$수식$${q1} $$/수식$$일 때, $$수식$$x$$/수식$$의 값을 구하시오. (단, $$수식$$x &gt; {aa1}$$/수식$$)\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "(평균) $$수식$$={{ {s1} + x + {s2} + {s3} - x + {s4} }} over {{5}}$$/수식$$\n" \
              "$$수식$$= {{ {c1} }} over {{5}} = {c2}$$/수식$$\n" \
              "각 변량의 편차를 차례대로 구하면\n" \
              "$$수식$${c3}$$/수식$$, $$수식$$x - {c2}$$/수식$$, $$수식$${c4}$$/수식$$, $$수식$${c5} - x$$/수식$$, $$수식$${c6}$$/수식$$이므로\n"   \
              "(분산)$$수식$$= {{ ({c3})^{{2}} + ( x - {c2})^{{2}} + {c4}^{{2}} + ({c5} - x )^{{2}} + {c6}^{{2}} }} over {{5}}$$/수식$$\n"   \
              "$$수식$$= {q1}$$/수식$$\n" \
              "에서\n" \
              "$$수식$$2x^{{2}} - {c7}x + {c8} = {c9}$$/수식$$, $$수식$$x^{{2}} - {c10}x + {c11} = 0$$/수식$$\n" \
              "$$수식$$(x - {aa1})(x - {aa2}) = 0 THEREFORE x = {aa1}$$/수식$$ 또는 $$수식$$x = {aa2}$$/수식$$\n" \
              "그런데 $$수식$$x &gt; {aa1}$$/수식$$이므로 $$수식$$x = {aa2}$$/수식$$\n\n"
              

    q1 = 0
    c8 = 200
    while (q1 <= 0) or (c8 >= 200):
        aa1 = np.random.randint(1, 5)
        aa2 = np.random.randint(aa1 + 4, 10)
        s3 = aa1 + aa2
        s2 = np.random.randint(2, s3 - 1)
        while ((((4 * s2) - s3)) <= 1):
            s2 = np.random.randint(2, s3 - 1)
        s1 = np.random.randint(1, min(s2, (4 * s2) - s3))
        s4 = (4 * s2) - s3 - s1
        q1 = (np.square(s1 - s2) + np.square(-s2) + np.square(s2 - s2) + np.square(s3 - s2) + np.square(s4 - s2) - (aa1 * aa2 * 2)) / 5
        
        c1 = s1 + s2 + s3 + s4
        c2 = c1 / 5
        c3 = s1 - c2
        c4 = s2 - c2
        c5 = s3 - c2
        c6 = s4 - c2
        c7 = 2 * (c2 + c5)
        c8 = np.square(c3) + np.square(c2) + np.square(c4) + np.square(c5) + np.square(c6)
        c9 = q1 * 5
        c10 = c7 / 2
        c11 = (c8 - c9) / 2

        
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11 = RoundCheck([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11])

        a1 = aa2

    stem = stem.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4, aa1=aa1)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, s1=s1, s2=s2, s3=s3, s4=s4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, aa1=aa1, aa2=aa2)
    return stem, answer, comment



def statistics326_Stem_054():
    stem = "$$수식$$5$$/수식$$개의 변량 $$수식$${s1}, {s2}, {s3}, {s4}, x$$/수식$$의 평균이 $$수식$${c1}$$/수식$$일 때, 분산은?\n" \
           "① $$수식$${ss1}$$/수식$$\n" \
           "② $$수식$${ss2}$$/수식$$\n" \
           "③ $$수식$${ss3}$$/수식$$\n" \
           "④ $$수식$${ss4}$$/수식$$\n" \
           "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "평균이 $$수식$${c1}$$/수식$$이므로\n" \
              "$$수식$${{ {s1} + {s2} + {s3} + {s4} + x }} over {{5}} = {c1}$$/수식$$, $$수식$${c2} + x = {c3}$$/수식$$\n" \
              "$$수식$$THEREFORE x = {c4}$$/수식$$\n" \
              "따라서 각 자료의 편차는\n" \
              "$$수식$${d1}, {d2}, {d3}, {d4}, {d5}$$/수식$$이므로\n" \
              "분산은\n$$수식$${{ ({d1})^{{2}} + {d2}^{{2}} + {d3}^{{2}} + {d4}^{{2}} + ({d5})^{{2}} }} over {{5}} = {{ {c5} }} over {{5}} = {c6}$$/수식$$\n\n"

    list_1 = [2, 6, 8, 10, 4]
    list_2 = [3, 5, 8, 6, 3]
    list_3 = [2, 5, 7, 8, 3]
    list_4 = [2, 4, 6, 10, 3]
    list_5 = [1, 6, 7, 9, 2]
    
    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(0, 7);
    for i in range(len(list_A2)):
        list_A2[i] += t0
    s1, s2, x, s3, s4 = list_A2

    c1 = (s1 + s2 + x + s3 + s4) // 5
    c2 = s1 + s2 + s3 + s4
    c3 = c1 * 5
    c4 = c3 - c2
    
    d1 = s1 - c1
    d2 = s2 - c1
    d3 = x - c1
    d4 = s3 - c1
    d5 = s4 - c1

    c5 = d1**2 + d2**2 + d3**2 + d4**2 + d5**2
    c6 = RoundCheck([c5 / 5])[0]

    a1 = c6
    t1 = [round(a1-0.4, 1), round(a1-0.2, 1), a1, round(a1+0.2, 1), round(a1+0.4, 1)][np.random.randint(0,5)]
    s_candidates = [t1 - 0.4, t1 - 0.2, t1, t1 + 0.2, t1 + 0.4]
    for i in range(len(s_candidates)):
        s_candidates[i]=round(s_candidates[i], 1)
    s_candidates = RoundCheck(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, c1=c1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(s1=s1, s2=s2, s3=s3, s4=s4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, d1=d1, d2=d2, d3=d3, d4=d4, d5=d5)

    return stem, answer, comment


def statistics326_Stem_055():
    stem = "$$수식$$5$$/수식$$개의 수 $$수식$$ {s1}, {s2}, {s3}, a$$/수식$$, $$수식$$b$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이고 분산이 $$수식$${q2}$$/수식$$일 때, $$수식$$a^{{2}} + b^{{2}}$$/수식$$의 값을 구하시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "평균이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{ {s1} + {s2} + {s3} + a + b }} over {{5}} = {q1}$$/수식$$에서\n" \
              "$$수식$${c1} + a + b = {c2} THEREFORE a + b = {c10}$$/수식$$\n" \
              "분산이 $$수식$${q2}$$/수식$$이므로\n" \
              "$$수식$${{ ({c3})^{{2}} + ({c4})^{{2}} + ({c5})^{{2}} + (a - {q1})^{{2}} + (b - {q1})^{{2}} }} over {{5}}$$/수식$$\n" \
              "$$수식$$= {q2}$$/수식$$에서\n" \
              "$$수식$$(a - {q1})^{{2}} + (b - {q1})^{{2}} = {c6}$$/수식$$\n" \
              "$$수식$$a^{{2}} + b^{{2}} - {c7}( a + b ) + {c8} = {c6}$$/수식$$\n" \
              "$$수식$$THEREFORE a^{{2}} + b^{{2}} = {c6} + {c7} times {c10} - {c8} = {c9}$$/수식$$\n\n"
              

    c10 = 0
    c9 = 0
    c6 = 0
    while (c9 != int(c9)) or (c10 <= 0) or (c9 <= 0) or (c6 <= 0):
        s1 = np.random.randint(5, 10)
        s2 = np.random.randint(3, s1)
        s3 = np.random.randint(s1, 15)
        q1 = np.random.randint(min([s1, s2, s3]) - 1, max([s1, s2, s3]) + 1)
        q2 = np.random.randint(2, 8)

        c1 = s1 + s2 + s3
        c2 = q1 * 5
        c10 = c2 - c1
        c3 = s1 - q1
        c4 = s2 - q1
        c5 = s3 - q1
        c6 = (5 * q2) - np.square(c3) - np.square(c4) - np.square(c5)
        c7 = q1 * 2
        c8 = 2 * np.square(q1)
        c9 = c6 + (c7 * c10) - c8
        
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = RoundCheck([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10])

        a1 = c9

    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10)
    return stem, answer, comment


def statistics326_Stem_056():
    stem = "편차가 각각 $$수식$${s1},` {s2},` a$$/수식$$,$$수식$$ {s3},`b$$/수식$$인 $$수식$$5$$/수식$$개 변량의 분산이 $$수식$${q1}$$/수식$$일 때, $$수식$$ab$$/수식$$의 값은?\n" \
        "① $$수식$${ss1}$$/수식$$\n" \
        "② $$수식$${ss2}$$/수식$$\n" \
        "③ $$수식$${ss3}$$/수식$$\n" \
        "④ $$수식$${ss4}$$/수식$$\n" \
        "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "편차의 총합은 $$수식$$0$$/수식$$이므로 \n" \
              "$$수식$$( {s1} ) + ( {s2} ) + a + {s3} + b = 0$$/수식$$에서 $$수식$$a + b = {c1}$$/수식$$\n" \
              "분산이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{ ( {s1} )^{{2}} + ( {s2} )^{{2}} + a^{{2}} + {s3}^{{2}} + b^{{2}} }} over {{5}} = {q1}$$/수식$$에서\n" \
              "$$수식$$a^{{2}} + b^{{2}} + {c2} = {c3} THEREFORE a^{{2}} + b^{{2}} = {c4}$$/수식$$\n" \
              "따라서 $$수식$$(a + b )^{{2}} = a^{{2}} + b^  {{2}} + 2ab$$/수식$$에서\n" \
              "$$수식$${c1}^{{2}} = {c4} + 2ab$$/수식$$, $$수식$$2ab = {c5} THEREFORE ab = {c6}$$/수식$$\n\n"

    c1 = 0
    c6 = 0
    c5 = 0
    c4 = 0
    while (c5 != int(c5)) or (c1 <= 0) or (c4 <= 0) or (c6 <= 0):

        s1 = (-1) * np.random.randint(1, 10)
        s2 = (-1) * np.random.randint(1, 10)
        s3 = np.random.randint(1, 10)
        q1 = np.random.randint(2, 20)

        c1 = -s1 - s2 - s3
        c2 = np.square(s1) + np.square(s2) + np.square(s3)
        c3 = q1 * 5
        c4 = c3 - c2
        c5 = np.square(c1) - c4
        c6 = c5 / 2

        c1, c2, c3, c4, c5, c6 = RoundCheck([c1, c2, c3, c4, c5, c6])

    a1 = c6
    gap = 0.5
    t1 = gap * 2
    while (t1 - (gap * 2)) <= 0:
        t1 = [a1 - (gap * 2), a1 - gap, a1, a1 + gap, a1 + (gap * 2)][np.   random.randint(0, 5)]   
    s_candidates = [t1 - (gap * 2), t1 - gap, t1, t1 + gap, t1 + (gap * 2)]
    s_candidates = RoundCheck(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break
    s_candidates = RoundCheck(s_candidates)

    stem = stem.format(q1=q1, s1=s1, s2=s2, s3=s3, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, s1=s1, s2=s2, s3=s3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    return stem, answer, comment


def statistics326_Stem_057():
    stem = "세 수 $$수식$$x$$/수식$$, $$수식$$y$$/수식$$, $$수식$$z$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이고 분산이 $$수식$${q2}$$/수식$$일 때, 세 수 $$수식$$x^{{2}}$$/수식$$, $$수식$$y^{{2}}$$/수식$$, $$수식$$z^{{2}}$$/수식$$의 평균을 구하시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "세 수 $$수식$$x$$/수식$$, $$수식$$y$$/수식$$, $$수식$$z$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{ x + y + z }} over {{3}} = {q1}$$/수식$$에서 $$수식$$x + y + z = {c1}$$/수식$$\n" \
              "또 $$수식$$x$$/수식$$, $$수식$$y$$/수식$$, $$수식$$z$$/수식$$의 분산이 $$수식$${q2}$$/수식$$이므로\n" \
              "$$수식$${{ (x - {q1})^{{2}} + (y - {q1})^{{2}} + (z - {q1})^{{2}} }} over {{3}} = {q2}$$/수식$$에서\n" \
              "$$수식$$ (x - {q1})^{{2}} + (y - {q1})^{{2}} + (z - {q1})^{{2}} = {c2}$$/수식$$\n" \
              "$$수식$$x^{{2}} + y^{{2}} + z^{{2}} - {c3}(x + y + z ) + {c4} = {c2}$$/수식$$\n" \
              "$$수식$$x^{{2}} + y^{{2}} + z^{{2}} - {c3} times {c1} + {c4} = {c2}$$/수식$$\n" \
              "$$수식$$THEREFORE x^{{2}} + y^{{2}} + z^{{2}} = {c5}$$/수식$$\n" \
              "따라서 $$수식$$x^{{2}}$$/수식$$, $$수식$$y^{{2}}$$/수식$$, $$수식$$z^{{2}}$$/수식$$의 평균은\n" \
              "$$수식$${{ x^{{2}} + y^{{2}} + z^{{2}} }} over {{3}} = {{ {c5} }} over {{3}} = {c6}$$/수식$$\n\n"
              

    c6 = 0
    c5 = 0
    while (c6 != int(c6)) or (c5 <= 0):
        q1 = np.random.randint(5, 20)
        q2 = np.random.randint(2, 8)

        c1 = q1 * 3
        c2 = q2 * 3
        c3 = q1 * 2
        c4 = 3 * np.square(q1)
        c5 = c2 + (c3 * c1) - c4
        c6 = c5 / 3

        c1, c2, c3, c4, c5, c6 = RoundCheck([c1, c2, c3, c4, c5, c6])

        a1 = c6

    stem = stem.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    return stem, answer, comment


def statistics326_Stem_058():
    stem = "$$수식$$5$$/수식$$개의 변량 $$수식$${s1}, {s2}, a$$/수식$$, $$수식$$b,  {s3}$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이고 분산이 $$수식$${q2}$$/수식$$일 때, $$수식$$ab$$/수식$$ 의 값을 구하시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "변량 $$수식$${s1}, {s2}, a, b, {s3}$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{ {s1} + {s2} + a + b + {s3} }} over {{5}} = {q1}$$/수식$$에서\n" \
              "$$수식$$ a + b + {c1} = {c2} THEREFORE a + b = {c3}$$/수식$$\n" \
              "분산이 $$수식$${q2}$$/수식$$이므로\n" \
              "$$수식$${{1}} over {{5}} {{ ({s1} - {q1})^{{2}} + ({s2} - {q1})^{{2}} + (a - {q1})^{{2}}$$/수식$$\n" \
              "$$수식$$+ (b - {q1})^{{2}} + ({s3} - {q1})^{{2}} }} = {q2}$$/수식$$에서\n" \
              "$$수식$${c4} + a^{{2}} + b^{{2}} - {c5}(a + b ) = {c6}$$/수식$$\n" \
              "$$수식$${c4} + a^{{2}} + b^{{2}} - {c5} times {c3} = {c6}$$/수식$$\n" \
              "$$수식$$THEREFORE a^{{2}} + b^{{2}} = {c7}$$/수식$$\n" \
              "따라서 $$수식$$(a + b )^{{2}} = a^{{2}} + b^{{2}} + 2ab$$/수식$$에서\n" \
              "$$수식$${c3}^{{2}} = {c7} + 2ab$$/수식$$, $$수식$$2ab = {c8}$$/수식$$\n" \
              "$$수식$$THEREFORE ab = {c9}$$/수식$$\n\n"

    c9 = 0
    c3 = 0
    while (c9 != int(c9)) or (c3 <= 0):
        s1 = np.random.randint(3, 15)
        s2 = np.random.randint(3, 15)
        s3 = np.random.randint(s2 + 1, 16)
        q1 = np.random.randint(min([s1,s2,s3]), max([s1,s2,s3]))
        q2 = np.random.randint(2, 8)

        c1 = s1 + s2 + s3
        c2 = q1 * 5
        c3 = c2 - c1
        c4 = np.square(s1 - q1) + np.square(s2 - q1) + np.square(s3 - q1) + np.square(q1) + np.square(q1)
        c5 = 2 * q1
        c6 = q2 * 5
        c7 = c6 + (c5 * c3) - c4
        c8 = np.square(c3) - c7
        c9 = c8 / 2

        c1, c2, c3, c4, c5, c6, c7, c8, c9 = RoundCheck([c1, c2, c3, c4, c5, c6, c7, c8, c9])

        a1 = c9

    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9)
    return stem, answer, comment


def statistics326_Stem_059():
    stem = "가로의 길이가 $$수식$$x$$/수식$$, 세로의 길이가 $$수식$$y$$/수식$$, 높이가 $$수식$${s1}$$/수식$$인 직육면체의 $$수식$$12$$/수식$$개의 모서리의 길이의 평균이 $$수식$${q1}$$/수식$$, 분산이 $$수식$${q2}$$/수식$$이다. 이때 이 직육면체의 $$수식$$6$$/수식$$개의 면의 넓이의 평균을 소수로 나타내시오.\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "직육면체에는 길이가 같은 모서리가 $$수식$$4$$/수식$$개씩 있으므로\n$$수식$$12$$/수식$$개의 변량 $$수식$$x$$/수식$$, $$수식$$x$$/수식$$, $$수식$$x$$/수식$$, $$수식$$x$$/수식$$, $$수식$$y$$/수식$$, $$수식$$y$$/수식$$, $$수식$$y$$/수식$$, $$수식$$y$$/수식$$, $$수식$${s1}$$/수식$$, $$수식$${s1}$$/수식$$, $$수식$${s1}$$/수식$$, $$수식$${s1}$$/수식$$의 평균이 $$수식$${q1}$$/수식$$, 분산이 $$수식$${q2}$$/수식$$이다.\n" \
              "$$수식$${{4x + 4y + {c1} }} over {{12}} = {q1}$$/수식$$에서 $$수식$$ x + y + {s1} = {c2}$$/수식$$\n" \
              "$$수식$$THEREFORE x + y = {c3}$$/수식$$\n" \
              "$$수식$${{ 4 (x - {q1})^{{2}} + 4 (y - {q1})^{{2}} + 4 ({s1} - {q1})^{{2}} }} over {{12}} = {q2}$$/수식$$\n" \
              "$$수식$$x^{{2}} + y^{{2}} - {c4}(x + y ) + {c5} = {c6}$$/수식$$\n" \
              "$$수식$$x^{{2}} + y^{{2}} = {c7}$$/수식$$\n" \
              "이때 $$수식$$x^{{2}} + y^{{2}} = (x + y )^{{2}} - 2xy$$/수식$$에서\n" \
              "$$수식$$2xy = (x + y )^{{2}} - ( x^{{2}} + y^{{2}}) = {c8} - {c7} = {c9}$$/수식$$\n" \
              "따라서 이 직육면체는 넓이가 각각 $$수식$$xy, {s1}x, {s1}y$$/수식$$인 면이 $$수식$$2$$/수식$$개씩 있으므로\n구하는 평균은 " \
              "$$수식$${{ 2xy + {c10}x + {c10}y }} over {{6}} = {{ {c9} + {c11} }} over {{6}} = {{ {c12} }} over {{2}} = {c13}$$/수식$$\n\n"
    c12 = 0
    c9 = 0
    while (c12 != int(c12)) or (c9 <= 0):
        s1 = np.random.randint(3, 10)
        q1 = np.random.randint(s1 - 2, s1 + 2)
        q2 = np.random.randint(3, 10)

        c1 = 4 * s1
        c2 = q1 * 3
        c3 = c2 - s1
        c4 = 2 * q1
        c5 = np.square(q1) + np.square(q1) + np.square(s1 - q1)
        c6 = q2 * 3
        c7 = c6 - c5 + (c4 * c3)
        c8 = np.square(c3)
        c9 = c8 - c7
        c10 = 2 * s1
        c11 = c10 * c3
        c12 = (c9 + c11) / 3
        c13 = c12 / 2

        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13 = RoundCheck([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11,  c12, c13])

        a1 = c13

    stem = stem.format(q1=q1, q2=q2, s1=s1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12, c13=c13)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, s1=s1, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12, c13=c13)
    return stem, answer, comment


def statistics326_Stem_060():
    stem = "$$수식$$4$$/수식$$개의 변량 $$수식$${s1}$$/수식$$, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$${s2}$$/수식$$에서 두 변량을 각각 $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$(을)를 $$수식$${s3}$$/수식$$, $$수식$${s4}$$/수식$$(으)로 잘못 보고 평균과 분산을 구하였더니 평균이 $$수식$${q1}$$/수식$$이고 분산이 $$수식$${q2}$$/수식$$이었다. 이때 원래의 변량에 대한 분산을 소수로 나타내시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "잘못 본 변량 $$수식$${s3}$$/수식$$, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$${s4}$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이고 분산이 $$수식$${q2}$$/수식$$이므로\n" \
              "$$수식$${{ {s3} + a + b + {s4} }} over {{4}} = {q1}$$/수식$$에서 $$수식$$a + b = {c1}$$/수식$$\n" \
              "$$수식$${{ ({s3} - {q1})^{{2}} + (a - {q1})^{{2}} + (b - {q1})^{{2}} + ({s4} - {q1})^{{2}} }} over {{4}}$$/수식$$\n"   \
              "$$수식$$={q2}$$/수식$$에서\n"    \
              "$$수식$$(a - {q1})^{{2}} + (b - {q1})^{{2}} = {c2}$$/수식$$\n" \
              "따라서 원래의 변량 $$수식$${s1}$$/수식$$, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$${s2}$$/수식$$의 평균은\n" \
              "$$수식$${{ {s1} + a + b + {s2} }} over {{4}} = {{ {c3} + a + b }} over {{4}} = {c4}$$/수식$$" \
              "이므로\n" \
              "$$수식$${s1}$$/수식$$, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$${s2}$$/수식$$의 분산은\n"   \
              "$$수식$${{ ({s1} - {c4})^{{2}} + (a - {c4})^{{2}} + (b - {c4})^{{2}} + ({s2} - {c4})^{{2}} }} over {{4}}$$/수식$$\n"   \
              "$$수식$$= {{ {c5} + (a - {c4})^{{2}} + (b - {c4})^{{2}} }} over {{4}}$$/수식$$\n"   \
              "$$수식$${{ {c5} + {c2} }} over {{4}} = {c6}$$/수식$$\n"    \

    q2 = np.random.randint(5, 20)

    list_1 = [3, 5, 7, 5]
    list_2 = [2, 4, 6, 5]
    list_3 = [3, 4, 7, 5]
    list_A2 = [list_1, list_2, list_3][np.random.randint(0, 3)]
    t0 = np.random.randint(0, 5)
    for i in range(len(list_A2)):
        list_A2[i] += t0
    s1, s3, s4, q1 = list_A2
    
    c1 = (q1 * 4) - s3 - s4
    q1_2 =  q1
    s2 = (4 * q1_2) - c1 - s1
    
    c2 = (4 * q2) - np.square(s3 - q1) - np.square(s4 - q1)
    c3 = s1 + s2
    c4 = (s1 + s2 + c1) / 4
    c5 = np.square(s1 - c4) + np.square(s2 - c4)
    c6 = (c5 + c2) / 4

    c1, c2, c3, c4, c5, c6 = RoundCheck([c1, c2, c3, c4, c5, c6])
    
    a1 = c6

    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, s4=s4)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, s4=s4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    return stem, answer, comment


def statistics326_Stem_061():
    stem = "$$수식$$3$$/수식$$개의 변량 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이고 표준편차가 $$수식$${q2}$$/수식$$일 때, $$수식$$(a - {q1})^{{2}} + (b - {q1})^{{2}} + (c - {q1})^{{2}}$$/수식$$의 값은?\n" \
        "① $$수식$${ss1}$$/수식$$\n" \
        "② $$수식$${ss2}$$/수식$$\n" \
        "③ $$수식$${ss3}$$/수식$$\n" \
        "④ $$수식$${ss4}$$/수식$$\n" \
        "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이고 표준편차가 $$수식$${q2}$$/수식$$이므로\n" \
              "$$수식$${{ (a - {q1})^{{2}} + (b - {q1})^{{2}} + (c - {q1})^{{2}} }} over {{3}} = {q2}^{{2}}$$/수식$$\n" \
              "$$수식$$THEREFORE (a - {q1})^{{2}} + (b - {q1})^{{2}} + (c - {q1})^{{2}} = {c1}$$/수식$$\n\n"

    q1 = np.random.randint(1, 12)
    q2 = [1, 2, 3, 5, 7][np.random.randint(0, 5)]
    
    c1 = np.square(q2) * 3
    
    a1 = c1
    gap = 3 * q2
    t1 = gap * 2
    while (t1 - (gap * 2)) <= 0:
        t1 = [a1 - (gap * 2), a1 - gap, a1, a1 + gap, a1 + (gap * 2)][np.random.randint(0, 5)]   
    s_candidates = [t1 - (gap * 2), t1 - gap, t1, t1 + gap, t1 + (gap * 2)]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break
    s_candidates = RoundCheck(s_candidates)

    stem = stem.format(q1=q1, q2=q2, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, c1=c1)
    return stem, answer, comment


def statistics326_Stem_062():
    stem = "$$수식$$5$$/수식$$개의 변량 $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$, $$수식$$x$$/수식$$, $$수식$$y$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이 표준편차가 $$수식$$sqrt{{{q2}}}$$/수식$$일 때, $$수식$$x^{{2}} + y^{{2}}$$/수식$$의 값은?\n" \
        "① $$수식$${ss1}$$/수식$$\n" \
        "② $$수식$${ss2}$$/수식$$\n" \
        "③ $$수식$${ss3}$$/수식$$\n" \
        "④ $$수식$${ss4}$$/수식$$\n" \
        "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "주어진 변량의 평균이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{ {s1} + {s2} + {s3} + x + y }} over {{5}} = {q1}$$/수식$$에서 $$수식$$THEREFORE {c1} + x + y = {c2}$$/수식$$\n" \
              "$$수식$$THEREFORE x + y = {c3}$$/수식$$\n" \
              "따라서 표준편차는\n" \
              "$$수식$${{ ({c4})^{{2}} + {c5}^{{2}} + {c6}^{{2}} + (x - {q1})^{{2}} + (y - {q1})^{{2}} }} over {{5}} =$$/수식$$($$수식$$ sqrt{{{q2}}}$$/수식$$ )$$수식$$ ^{{2}}$$/수식$$\n" \
              "$$수식$$x^{{2}} + y^{{2}} - {c7}(x + y ) + {c8} = {c9}$$/수식$$\n" \
              "$$수식$$THEREFORE x^{{2}} + y^{{2}} = {c10}$$/수식$$\n\n"

    list_1 = [1, 2, 3, 2, 2]
    list_2 = [1, 3, 4, 3, 2]
    list_3 = [1, 2, 4, 2, 2]
    list_4 = [1, 3, 5, 3, 2]
    list_A2 = [list_1, list_2, list_3, list_4][np.random.randint(0, 4)]
    t0 = np.random.randint(0, 5)
    for i in range(len(list_A2)):
        list_A2[i] += t0
    list_A2[4] = [1, 2, 3, 5, 7][np.random.randint(0, 5)]
    s1, s2, s3, q1, q2 = list_A2
    
    c1 = s1 + s2 + s3
    c2 = q1 * 5
    c3 = c2 - c1
    c4 = s1 - q1
    c5 = s2 - q1
    c6 = s3 - q1
    c7 = 2 * q1
    c8 = np.square(c4) + np.square(c5) + np.square(c6) + (np.square(q1) * 2)
    c9 = 5 * q2
    c10 = c9 - c8 + (c7 * c3)

        
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = RoundCheck([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10])
    a1 = c10
    t1 = 10
    while (t1 - 10) <= 0:
        t1 = [a1 - 10, a1 - 5, a1, a1 + 5, a1 + 10][np.random.randint(0, 5)]   
    s_candidates = [t1 - 10, t1 - 5, t1, t1 + 5, t1 + 10]
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break
    s_candidates = RoundCheck(s_candidates)

    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10)
    return stem, answer, comment


def statistics326_Stem_063():
    stem = "세 수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이고 표준편차가 $$수식$${q2}$$/수식$$일 때, 세 수 $$수식$$a^{{2}}$$/수식$$, $$수식$$b^{{2}}$$/수식$$, $$수식$$c^{{2}}$$/수식$$을 구하시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "주어진 변량의 평균이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{a + b + c}} over {{3}} = {q1}$$/수식$$에서 $$수식$$a + b + c = {c1}$$/수식$$\n" \
              "표준편차가 $$수식$${q2}$$/수식$$이므로\n" \
              "$$수식$${{ (a - {q1})^{{2}} + (b - {q1})^{{2}} + (c - {q1})^{{2}} }} over {{3}} = {q2}^{{2}}$$/수식$$에서\n" \
              "$$수식$$(a - {q1})^{{2}} + (b - {q1})^{{2}} + (c - {q1})^{{2}} = {c2}$$/수식$$\n" \
              "$$수식$$a^{{2}} + b^{{2}} + c^{{2}} - {c3}(a + b + c ) + {c4} = {c2}$$/수식$$\n" \
              "$$수식$$a^{{2}} + b^{{2}} + c^{{2}} - {c3} times {c1} + {c4} = {c2}$$/수식$$\n" \
              "$$수식$$ THEREFORE a^{{2}} + b^{{2}} + c^{{2}} = {c5}$$/수식$$\n" \
              "따라서 세 수$$수식$$a^{{2}}$$/수식$$, $$수식$$b^{{2}}$$/수식$$, $$수식$$c^{{2}}$$/수식$$의 평균은\n" \
              "$$수식$${{ a^{{2}} + b^{{2}} + c^{{2}} }} over {{3}} = {{ {c5} }} over {{3}}= {c6}$$/수식$$"

    q1 = np.random.randint(1, 5) * 3
    q2 = np.random.randint(1, 5)
    
    c1 = q1 * 3
    c2 = np.square(q2) * 3
    c3 = q1 * 2
    c4 = np.square(q1) * 3
    c5 = c2 - c4 + (c3 * c1)
    c6 = c5 / 3

    c1, c2, c3, c4, c5, c6 = RoundCheck([c1, c2, c3, c4, c5, c6])
    a1 = c6

    stem = stem.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    return stem, answer, comment


def statistics326_Stem_064():
    stem = "$$수식$$5$$/수식$$개의 변량에 대하여 그 편차가 각각 $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$$a$$/수식$$, $$수식$${s3}$$/수식$$, $$수식$$b$$/수식$$이고 표준편차가 $$수식$${q1}sqrt{{{q2}}}$$/수식$$일 때, $$수식$$ab$$/수식$$의 값을 구하시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "편차의 총합은 $$수식$$0$$/수식$$이므로\n" \
              "$$수식$$({s1}) + ({s2}) + a + {s3} + b = 0$$/수식$$\n" \
              "$$수식$$THEREFORE a + b = {c1}$$/수식$$\n" \
              "표준편차가 $$수식$${q1}sqrt{{{q2}}}$$/수식$$이므로\n" \
              "$$수식$${{ ({s1})^{{2}} + ({s2})^{{2}} + a^{{2}} + {s3}^{{2}} + b^{{2}} }} over {{5}} = ({q1}sqrt{{{q2}}})^{{2}}$$/수식$$\n" \
              "$$수식$${{ ({s1})^{{2}} + ({s2})^{{2}} + a^{{2}} + {s3}^{{2}} + b^{{2}} }} over {{5}} = {c2}$$/수식$$\n" \
              "$$수식$$a^{{2}} + b^{{2}} + {c3} = {c4} THEREFORE a^{{2}} + b^{{2}} = {c5}$$/수식$$\n" \
              "따라서 $$수식$$ (a + b )^{{2}} = a^{{2}} + b^{{2}} + 2ab$$/수식$$이므로\n"  \
              "$$수식$${c6} = {c5} + 2ab$$/수식$$, $$수식$$2ab = {c7}$$/수식$$\n" \
              "$$수식$$THEREFORE ab = {c8}$$/수식$$\n\n"

    list_1 = [-3, -2, 1, 2, 3]
    list_2 = [-3, -2, 1, 2, 5]
    list_3 = [-3, -2, 1, 3, 3]
    list_3 = [-3, -2, 1, 3, 2]
    list_A2 = [list_1, list_2, list_3][np.random.randint(0, 3)]
    t0 = np.random.randint(0, 2)
    for i in range(3):
        list_A2[i] += t0
    s1, s2, s3, q1, q2 = list_A2
    
    c1 = -s1 - s2 - s3
    c2 = np.square(q1) * q2
    c3 = np.square(s1) + np.square(s2) + np.square(s3)
    c4 = c2 * 5
    c5 = c4 - c3
    c6 = np.square(c1)
    c7 = c6 - c5
    c8 = c7 / 2    
        
    c1, c2, c3, c4, c5, c6, c7, c8 = RoundCheck([c1, c2, c3, c4, c5, c6, c7, c8])
    a1 = c8

    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, s1=s1, s2=s2, s3=s3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8)
    return stem, answer, comment


def statistics326_Stem_065():
    stem = "$$수식$$4$$/수식$$개의 변량 $$수식$${s1}$$/수식$$, $$수식$$a$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$$b$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이고 표준편차가 $$수식$${q2}$$/수식$$일 때, $$수식$$ab$$/수식$$의 값을 구하시오.\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "주어진 변량의 평균이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{ {s1} + a + {s2} + b }} over {{4}} = {q1}$$/수식$$에서 $$수식$${s1} + a + {s2} + b = {c1}$$/수식$$\n" \
              "$$수식$$THEREFORE a + b = {c2}$$/수식$$\n" \
              "표준편차가 $$수식$${q2}$$/수식$$이므로\n" \
              "$$수식$${{ ({c3})^{{2}} + (a - {q1})^{{2}} + {c4}^{{2}} + (b - {q1})^{{2}} }} over {{4}} = {q2}^{{2}}$$/수식$$에서\n" \
              "$$수식$$ ({c3})^{{2}} + (a - {q1})^{{2}} + {c4}^{{2}} + (b - {q1})^{{2}} = {c5}$$/수식$$\n" \
              "$$수식$$a^{{2}} + b^{{2}} - {c6}( a + b ) + {c7} = {c5}$$/수식$$\n" \
              "$$수식$$a^{{2}} + b^{{2}} - {c8} = {c5} THEREFORE a^{{2}} + b^{{2}} = {c9}$$/수식$$\n" \
              "따라서 $$수식$$ (a + b )^{{2}} = a^{{2}} + b^{{2}} + 2ab$$/수식$$이므로\n"  \
              "$$수식$${c10} = {c9} + 2ab$$/수식$$, $$수식$$2ab = {c11}$$/수식$$\n" \
              "$$수식$$THEREFORE ab = {c12}$$/수식$$\n\n"

    list_1 = [2, 4, 4, 2]
    list_2 = [2, 5, 5, 3]
    list_3 = [2, 7, 7, 3]
    list_A2 = [list_1, list_2, list_3][np.random.randint(0, 3)]
    t0 = np.random.randint(0, 3)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0
    s1, s2, q1, q2 = list_A2    
    
    c1 = q1 * 4
    c2 = c1 - s1 - s2
    c3 = s1 - q1
    c4 = s2 - q1
    c5 = np.square(q2) * 4
    c6 = q1 * 2
    c7 = np.square(c3) + np.square(c4) + (np.square(q1) * 2)
    c8 = -c7 + (c6 * c2)
    c9 = c5 + c8
    c10 = np.square(c2)
    c11 = c10 - c9
    c12 = c11 / 2
        
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12 = RoundCheck([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12])
    a1 = c12

    stem = stem.format(q1=q1, q2=q2, s1=s1, s2=s2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, s1=s1, s2=s2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12)
    return stem, answer, comment


def statistics326_Stem_066():
    stem = "다음은 어느 {q1} 야구 선수 $$수식$$5$$/수식$$명이 지난 대회에서 안타를 친 횟수의 편차이다. 표준편차가 $$수식$${q2}sqrt{{{q3}}}$$/수식$$회일 때, $$수식$$ab$$/수식$$의 값을 구하시오.\n" \
        "$$표$$ $$수식$${s1}$$/수식$$, $$수식$${s2}$$/수식$$, $$수식$${s3}$$/수식$$, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$ $$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "편차의 총합은 $$수식$$0$$/수식$$이므로\n" \
              "$$수식$$({s1}) + ({s2}) + {s3} + a + b = 0$$/수식$$에서\n" \
              "$$수식$$a + b = {c1}$$/수식$$\n" \
              "표준편차가 $$수식$${q2}sqrt{{{q3}}}$$/수식$$회이면 분산은 {c2}이므로\n" \
              "(분산)$$수식$$= {{ ({s1})^{{2}} + ({s2})^{{2}} + {s3}^{{2}} + a^{{2}} + b^{{2}} }} over {{5}}$$/수식$$\n" \
              "$$수식$$= {{ a^{{2}} + b^{{2}} + {c3} }} over {{5}} = {c2}$$/수식$$\n" \
              "에서 $$수식$$a^{{2}} + b^{{2}} = {c4}$$/수식$$\n" \
              "따라서 $$수식$$a^{{2}} + b^{{2}} = (a + b )^{{2}} - 2ab$$/수식$$이므로\n" \
              "$$수식$${c4} = {c1}^{{2}} - 2ab$$/수식$$\n" \
              "$$수식$$THEREFORE ab = {c5}$$/수식$$\n\n"

    q1 = ['초등학교', '중학교', '고등학교','대학교'][np.random.randint(0, 4)]
    q2 = np.random.randint(2, 5)
    q3 = np.random.randint(2, 4)

    list_1 = [-3, -2, 1]
    list_2 = [-4, -2, 1]
    list_3 = [-3, -3, 1]
    list_A2 = [list_1, list_2, list_3][np.random.randint(0, 3)]
    t0 = np.random.randint(0, 2)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0
    s1, s2, s3 = list_A2    
    
    c1 = -s1 - s2 - s3
    c2 = np.square(q2) * q3
    c3 = np.square(s1) + np.square(s2) + np.square(s3)
    c4 = (c2 * 5) - c3
    c5 = round((np.square(c1) - c4) / 2, 1)
    
    c1, c2, c3, c4, c5 = RoundCheck([c1, c2, c3, c4, c5])
    a1 = c5

    stem = stem.format(q1=q1, q2=q2, q3=q3, s1=s1, s2=s2, s3=s3)
    answer = answer.format(a1=a1)
    comment = comment.format(q2=q2, q3=q3, s1=s1, s2=s2, s3=s3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def statistics326_Stem_067():
    stem = "$$수식$$5$$/수식$$개의 변량 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$, $$수식$$d$$/수식$$, $$수식$$e$$/수식$$의 평균이 $$수식$${q3}$$/수식$$이고 표준편차가 $$수식$${q4}$$/수식$$일 때, 변량 $$수식$$a + {q5}$$/수식$$, $$수식$$b + {q5}$$/수식$$, $$수식$$c + {q5}$$/수식$$, $$수식$$d + {q5}$$/수식$$, $$수식$$e + {q5}$$/수식$$의 평균과 표준편차를 차례대로 구하면?\n" \
        "① $$수식$${ss1}$$/수식$$, $$수식$${s1}$$/수식$$\n" \
        "② $$수식$${ss2}$$/수식$$, $$수식$${s2}$$/수식$$\n" \
        "③ $$수식$${ss3}$$/수식$$, $$수식$${s3}$$/수식$$\n" \
        "④ $$수식$${ss4}$$/수식$$, $$수식$${s4}$$/수식$$\n" \
        "⑤ $$수식$${ss5}$$/수식$$, $$수식$${s5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$, $$수식$$d$$/수식$$, $$수식$$e$$/수식$$의 평균이 $$수식$${q3}$$/수식$$이므로\n" \
              "$$수식$${{ a + b + c + d + e }} over {{5}} = {q3}$$/수식$$에서\n" \
              "$$수식$$a + b + c + d + e = {c1}$$/수식$$\n" \
              "표준편차가 $$수식$${q4}$$/수식$$이므로\n" \
              "$$수식$${{1}} over {{5}} {{ ( a - {q3})^{{2}} +( b - {q3})^{{2}} + ( c - {q3})^{{2}}$$/수식$$\n" \
              "$$수식$$+ ( d - {q3})^{{2}} + ( e - {q3})^{{2}} }} = {q4}^{{2}}$$/수식$$\n" \
              "이때 $$수식$$a + {q5}$$/수식$$, $$수식$$b + {q5}$$/수식$$, $$수식$$c + {q5}$$/수식$$, $$수식$$d + {q5}$$/수식$$, $$수식$$e + {q5}$$/수식$$의 평균은\n" \
              "$$수식$${{ a + b + c + d + e + {c2} }} over {{5}} = {{ {c1} + {c2} }} over {{5}} = {c3}$$/수식$$\n\n" \
              "\n$$수식$$a + {q5}$$/수식$$, $$수식$$b + {q5}$$/수식$$, $$수식$$c + {q5}$$/수식$$, $$수식$$d + {q5}$$/수식$$, $$수식$$e + {q5}$$/수식$$의 분산은\n" \
              "$$수식$${{1}} over {{5}} {{ ( a + {q5} - {c3})^{{2}} + ( b + {q5} - {c3})^{{2}}$$/수식$$\n$$수식$$ + ( c + {q5} - {c3})^{{2}}$$/수식$$" \
              "$$수식$$+ ( d + {q5} - {c3})^{{2}} + ( e + {q5} - {c3})^{{2}} }}$$/수식$$\n" \
              "$$수식$$= {{1}} over {{5}} {{ ( a - {c4})^{{2}} + ( b - {c4})^{{2}} + ( c - {c4})^{{2}}$$/수식$$" \
              "$$수식$$+ ( d - {c4})^{{2}} + ( e - {c4})^{{2}} }}$$/수식$$\n" \
              "$$수식$$={q4}^{{2}}$$/수식$$\n" \
              "\n따라서 구하는 평균과 표준편차는 각각 $$수식$${c3}$$/수식$$, $$수식$${q4}$$/수식$$이다.\n\n"

    q3 = np.random.randint(6, 11)
    q4 = np.random.randint(2, 7)
    q5 = np.random.randint(3, 6)
            
    c1 = q3 * 5
    c2 = q5 * 5
    c3 = (c1 + c2) // 5
    c4 = c3 - q5
    
    ss1, ss2, ss3, ss4, ss5 = [q3, c3, q3, c3, c3 + 1]
    s1, s2, s3, s4, s5 = [0, 1, q4 + 1, q4, q4 + 2]

    stem = stem.format(q3=q3, q4=q4, q5=q5, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[3])
    comment = comment.format(q3=q3, q4=q4, q5=q5, c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment


def statistics326_Stem_068():
    stem = "$$수식$$3$$/수식$$개의 변량 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$의 평균이 $$수식$${q1}$$/수식$$, 표준편차가 $$수식$${q2}$$/수식$$일 때, 변량 $$수식$${q3}a$$/수식$$, $$수식$${q3}b$$/수식$$, $$수식$${q3}c$$/수식$$의 평균은 $$수식$$m$$/수식$$, 표준편차는 $$수식$$n$$/수식$$이다. 이때 $$수식$$m + n$$/수식$$의 값을 구하시오.\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$의 평균이 $$수식$${q1}$$/수식$$, 표준편차가 $$수식$${q2}$$/수식$$이므로\n" \
              "$$수식$${{ a + b + c}} over {{3}} = {q1}$$/수식$$\n" \
              "$$수식$${{ (a - {q1})^{{2}} + (b - {q1})^{{2}} + (c - {q1})^{{2}} }} over {{3}} = {q2}^{{2}} = {c1}$$/수식$$\n" \
              "이때 $$수식$${q3}a$$/수식$$, $$수식$${q3}b$$/수식$$, $$수식$${q3}c$$/수식$$의 평균은\n" \
              "$$수식$$m = {{ {q3}a + {q3}b + {q3}c }} over {{3}} = {{ {q3}(a + b + c ) }} over {{3}}$$/수식$$\n" \
              "$$수식$$= {q3} times {q1} = {c2}$$/수식$$\n" \
              "$$수식$${q3}a$$/수식$$, $$수식$${q3}b$$/수식$$, $$수식$${q3}c$$/수식$$의 분산은\n" \
              "$$수식$$n^{{2}} = {{ ({q3}a - {c2} )^{{2}} + ({q3}b - {c2} )^{{2}} + ({q3}c - {c2} )^{{2}} }} over {{3}}$$/수식$$\n" \
              "$$수식$$= {{ {c3} times {{ (a - {q1})^{{2}} + (b - {q1})^{{2}} + (c - {q1})^{{2}} }} }} over {{3}}$$/수식$$\n" \
              "$$수식$$= {c3} times {c1} = {c4}$$/수식$$\n" \
              "즉, $$수식$$ n = sqrt{{{c4}}} = {c5}$$/수식$$\n" \
              "따라서 $$수식$$m + n = {c2} + {c5} = {c6}$$/수식$$\n\n"

    q1 = np.random.randint(2, 20)
    q2 = np.random.randint(2, 9)
    q3 = np.random.randint(2, 5)
    
    c1 = np.square(q2)
    c2 = q3 * q1
    c3 = np.square(q3)
    c4 = c3 * c1
    c5 = int(np.sqrt(c4))
    c6 = c2 + c5
    
    c1, c2, c3, c4, c5, c6 = RoundCheck([c1, c2, c3, c4, c5, c6])
    a1 = c6

    stem = stem.format(q1=q1, q2=q2, q3=q3)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, q3=q3, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6)
    return stem, answer, comment


def statistics326_Stem_069():
    stem = "{q1}의 $$수식$${q2}$$/수식$$학기 중간고사 $$수식$$5$$/수식$$개 과목의 성적의 평균이 $$수식$${q3}$$/수식$$점, 표준편차가 $$수식$${q4}$$/수식$$점이었고, 기말고사에서는 $$수식$$5$$/수식$$개 과목 모두 점수가 $$수식$${q5}$$/수식$$점씩 올랐다. 기말고사 $$수식$$5$$/수식$$개 과목의 평균과 분산을 차례대로 구하면? (단, 중간고사와 기말고사의 $$수식$$5$$/수식$$개 과목은 동일하다.)\n" \
        "① $$수식$${ss1}$$/수식$$점, $$수식$${s1}$$/수식$$\n" \
        "② $$수식$${ss2}$$/수식$$점, $$수식$${s2}$$/수식$$\n" \
        "③ $$수식$${ss3}$$/수식$$점, $$수식$${s3}$$/수식$$\n" \
        "④ $$수식$${ss4}$$/수식$$점, $$수식$${s4}$$/수식$$\n" \
        "⑤ $$수식$${ss5}$$/수식$$점, $$수식$${s5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "중간고사 $$수식$$5$$/수식$$개 과목의 성적을 각각 $$수식$$a$$/수식$$점, $$수식$$b$$/수식$$점, $$수식$$c$$/수식$$점, $$수식$$d$$/수식$$점, $$수식$$e$$/수식$$점이라 하면\n" \
              "기말고사의 성적은 $$수식$$(a + {q5})$$/수식$$점, $$수식$$(b + {q5})$$/수식$$점, $$수식$$(c + {q5})$$/수식$$점, $$수식$$(d + {q5})$$/수식$$점, $$수식$$(e + {q5})$$/수식$$점이다.\n" \
              "따라서 기말고사 $$수식$$5$$/수식$$개 과목의 평균은\n" \
              "$$수식$${{ a + b + c + d + e }} over {{5}} + {q5} = {q3} + {q5} = {c1}$$/수식$$\n" \
              "또한 분산은\n" \
              "$$수식$${{1}} over {{5}}$$/수식$${ttmp}\n" \
              "$$수식$$= {{1}} over {{5}}$$/수식$${ttmp2}\n" \
              "$$수식$$= {q4}^{{2}} = {c2} $$/수식$$\n\n"

    q1 = ['이준이', '하은이', '수민이', '민제'][np.random.randint(0, 4)]
    q2 = np.random.randint(1, 3)

    q3 = np.random.randint(60, 80)
    q4 = np.random.randint(2, 7)
    q5 = np.random.randint(3, 15)
            
    c1 = q3 + q5
    c2 = np.square(q4)
    ttmp="{$$수식$$( a + %d - %d)^{{2}} + ( b + %d - %d)^{{2}}+$$/수식$$\n$$수식$$CDOTS + ( e + %d - %d)^{{2}}$$/수식$$}"%(q5,c1,q5,c1,q5,c1)
    ttmp2="{$$수식$$ ( a - %d)^{{2}} + ( b - %d)^{{2}} + CDOTS + ( e - %d)^{{2}}$$/수식$$}"%(q3,q3,q3)
    ss1, ss2, ss3, ss4, ss5 = [q3, q3, q3 + 1 , c1, c1]
    s1, s2, s3, s4, s5 = [q4, c2, c2, c2, q4]    


    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[3])
    comment = comment.format(ttmp=ttmp,ttmp2=ttmp2,q3=q3, q4=q4, q5=q5, c1=c1, c2=c2)
    return stem, answer, comment


def statistics326_Stem_070():
    stem = "변량 $$수식$$x_{{1}}$$/수식$$, $$수식$$x_{{2}}$$/수식$$, $$수식$$x_{{3}}$$/수식$$, $$수식$$ CDOTS $$/수식$$, $$수식$$x_{{n}}$$/수식$$의 표준편차가 $$수식$${q1}$$/수식$$일 때, 변량 $$수식$${q2}x_{{1}} + {q3}$$/수식$$, $$수식$${q2}x_{{2}} + {q3}$$/수식$$, $$수식$${q2}x_{{3}} + {q3}$$/수식$$, $$수식$$ CDOTS $$/수식$$, $$수식$${q2}x_{{n}} + {q3}$$/수식$$의 표준편차는?\n" \
        "① $$수식$${ss1}$$/수식$$\n" \
        "② $$수식$${ss2}$$/수식$$\n" \
        "③ $$수식$${ss3}$$/수식$$\n" \
        "④ $$수식$${ss4}$$/수식$$\n" \
        "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "변량 $$수식$$x_{{1}}$$/수식$$, $$수식$$x_{{2}}$$/수식$$, $$수식$$x_{{3}}$$/수식$$, $$수식$$ CDOTS $$/수식$$, $$수식$$x_{{n}}$$/수식$$의 평균을 $$수식$$m$$/수식$$이라 하면\n" \
              "$$수식$$ {{ x_{{1}} + x_{{2}} + CDOTS + x_{{n}} }} over {{ n }} = {{ m }}$$/수식$$\n" \
              "또, 표준편차가 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{ (x_{{1}} - m )^{{2}} + (x_{{2}} - m )^{{2}} + CDOTS + (x_{{n}} - m )^{{2}} }} over {{n}} = {c1}$$/수식$$\n" \
              "변량 $$수식$${q2}x_{{1}} + {q3}$$/수식$$, $$수식$${q2}x_{{2}} + {q3}$$/수식$$, $$수식$${q2}x_{{3}} + {q3}$$/수식$$, $$수식$$ CDOTS $$/수식$$, $$수식$${q2}x_{{n}} + {q3}$$/수식$$의 평균은\n" \
              "$$수식$${{ ({q2}x_{{1}} + {q3} ) + ({q2}x_{{2}} + {q3} ) + CDOTS + ({q2}x_{{n}} + {q3} ) }} over {{n}}$$/수식$$\n"  \
              "$$수식$$= {{ {q2}(x_{{1}} + x_{{2}} + CDOTS + x_{{n}}) + {q3}n }} over {{n}}$$/수식$$\n"  \
              "$$수식$$= {q2}m + {q3}$$/수식$$ "    \
              "이고, 분산은\n" \
              "$$수식$${{1}} over {{n}}$$/수식$${ttmp}\n" \
              "$$수식$$= {c2} times {{1}} over {{n}}$$/수식$${ttmp2}" \
              "$$수식$$= {c2} times {c1} = {c3} $$/수식$$\n" \
              "따라서 구하는 표준편차는 $$수식$${c4}$$/수식$$이다."

    q1 = np.random.randint(2, 10)
    q2 = np.random.randint(2, 10)
    q3 = np.random.randint(1, 8)
        
    c1 = np.square(q1)
    c2 = np.square(q2)
    c3 = c2 * c1
    c4 = int(np.sqrt(c3))
    c1, c2, c3 = RoundCheck([c1, c2, c3])

    a1 = c4

    t1 = np.random.randint(a1 - 2, a1 + 2)
    s_candidates = [t1 - 2, t1 - 1, t1, t1 + 1, t1 + 2]
    s_candidates = RoundCheck(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break


    ttmp= "{$$수식$$({%s}x_{{1}} + {%s} - {%s}m - {%s})^{{2}} + ({%s}x_{{2}} + {%s} - {%s}m - {%s})^{{2}}+ CDOTS + ({%s}x_{{n}} + {%s} - {%s}m - {%s})^{{2}} $$/수식$$}"%(q2,q3,q2,q3,q2,q3,q2,q3,q2,q3,q2,q3)
    ttmp2= "{$$수식$$ (x_{{1}} - m )^{{2}} + (x_{{2}} - m )^{{2}}+ CDOTS$$/수식$$\n$$수식$$ + (x_{{n}} - m )^{{2}}$$/수식$$ }"
    stem = stem.format(q1=q1, q2=q2, q3=q3, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, ttmp=ttmp,q2=q2, ttmp2=ttmp2,q3=q3, c1=c1, c2=c2, c3=c3, c4=c4)
    return stem, answer, comment


def statistics326_Stem_071():
    stem = "$$수식$$4$$/수식$$개의 변량 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$, $$수식$$d$$/수식$$의 평균이 $$수식$${q1}$$/수식$$, 분산이 $$수식$${q2}$$/수식$$일 때, 다음 자료의 평균을 $$수식$$m$$/수식$$, 분산을 $$수식$$n$$/수식$$이라 하자. $$수식$$m + n$$/수식$$의 값을 구하시오.\n" \
        "$$표$$ $$수식$$2a + 1$$/수식$$, $$수식$$2b + 1$$/수식$$, $$수식$$2c + 1$$/수식$$, $$수식$$2d + 1$$/수식$$ $$/표$$\n"
    answer = "(답):$$수식$${a1}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$, $$수식$$d$$/수식$$의 평균이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{ a + b + c + d}} over {{4}} = {q1}$$/수식$$에서 $$수식$$a + b + c + d = {c1}$$/수식$$\n" \
              "분산이 $$수식$${q2}$$/수식$$이므로\n" \
              "$$수식$${{ (a - {q1})^{{2}} + (b - {q1})^{{2}} + (c - {q1})^{{2}} + (d - {q1})^{{2}} }} over {{4}} = {q2}$$/수식$$\n" \
              "$$수식$$THEREFORE m = {{ (2a + 1 ) + (2b + 1 ) + (2c + 1 ) + (2d + 1 ) }} over {{4}}$$/수식$$\n" \
              "$$수식$$= 2 times {q1} + 1 = {c2}$$/수식$$\n" \
              "$$수식$$THEREFORE n = {{ (2a - {c3} )^{{2}} + (2b - {c3} )^{{2}} + (2c - {c3} )^{{2}} + (2d - {c3} )^{{2}} }} over {{4}}$$/수식$$\n" \
              "$$수식$$= 4 times {{ (a - {q1})^{{2}} + (b - {q1})^{{2}} + (c - {q1})^{{2}} + (d - {q1})^{{2}} }} over {{4}}$$/수식$$\n" \
              "$$수식$$= 4 times {q2}$$/수식$$\n" \
              "$$수식$$= {c4}$$/수식$$\n" \
              "따라서 $$수식$$m + n = {c2} + {c4} = {c5}$$/수식$$\n\n"

    q1 = np.random.randint(2, 10)
    q2 = np.random.randint(2, 10)
    
    c1 = q1 * 4
    c2 = (2 * q1) + 1
    c3 = c2 - 1
    c4 = 4 * q2
    c5 = c2 + c4
    
    c1, c2, c3, c4, c5 = RoundCheck([c1, c2, c3, c4, c5])
    a1 = c4

    stem = stem.format(q1=q1, q2=q2)
    answer = answer.format(a1=a1)
    comment = comment.format(q1=q1, q2=q2, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)
    return stem, answer, comment


def statistics326_Stem_072():
    stem = "{q1} 결과 남학생 $$수식$${q2}$$/수식$$명과 여학생 $$수식$${q3}$$/수식$$명의 평균은 같고 분산은 각각 $$수식$${q4}$$/수식$$, $$수식$${q5}$$/수식$$이었다. 전체 $$수식$${q6}$$/수식$$명의 {q1} 점수의 분산은? \n" \
        "① $$수식$${ss1}$$/수식$$\n" \
        "② $$수식$${ss2}$$/수식$$\n" \
        "③ $$수식$${ss3}$$/수식$$\n" \
        "④ $$수식$${ss4}$$/수식$$\n" \
        "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "남학생과 여학생의 {q1} 점수의 평균이 같으므로\n" \
              "(분산)$$수식$$= {{ {q2} times {q4} + {q3} times {q5} }} over {{ {q6} }} = {{ {c1} }} over {{ {q6} }} = {c2} $$/수식$$\n\n"
    
    q1 = ['영어 퀴즈', '국어 시험', '체육 수행 평가', '수학 시험'][np.random.randint(0, 4)]

    list_1 = [4, 6, 6, 16]
    list_2 = [4, 6, 3, 8]
    list_3 = [4, 6, 4, 9]
    list_4 = [3, 7, 5, 5]
    list_5 = [2, 8, 6, 6]
    list_A2 = [list_1, list_2, list_3, list_4, list_5][np.random.randint(0, 5)]
    t0 = np.random.randint(1, 3)
    for i in range(0, len(list_A2)):
        list_A2[i] *= t0
    q2, q3, q4, q5 = list_A2
    q6 = q2 + q3
    
    c1 = (q2 * q4) + (q3 * q5)
    c2 = c1 // q6

    a1 = c2

    t1 = np.random.randint(a1 - 2, a1 + 2)
    s_candidates = [t1 - 2, t1 - 1, t1, t1 + 1, t1 + 2]
    s_candidates = RoundCheck(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, c1=c1, c2=c2)
    return stem, answer, comment


def statistics326_Stem_073():
    stem = "네 수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$, $$수식$$d$$/수식$$에 대하여 두 수 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$의 평균과 분산이 각각 $$수식$${q1}$$/수식$$, $$수식$${q2}$$/수식$$이고 $$수식$$c$$/수식$$, $$수식$$d$$/수식$$의 평균과 분산이 각각 {q3}, {q4}일 때, $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$, $$수식$$d$$/수식$$의 분산은? \n" \
        "① $$수식$${ss1}$$/수식$$\n" \
        "② $$수식$${ss2}$$/수식$$\n" \
        "③ $$수식$${ss3}$$/수식$$\n" \
        "④ $$수식$${ss4}$$/수식$$\n" \
        "⑤ $$수식$${ss5}$$/수식$$\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "$$수식$$a$$/수식$$, $$수식$$b$$/수식$$ 의 평균이 $$수식$${q1}$$/수식$$이므로\n" \
              "$$수식$${{ a + b }} over {{2}} = {c1}$$/수식$$에서 $$수식$$a + b = {c2}$$/수식$$\n" \
              "$$수식$$a$$/수식$$, $$수식$$b$$/수식$$의 분산이 $$수식$${q2}$$/수식$$이므로\n" \
              "$$수식$${{ (a - {q1})^{{2}} + (b - {q1})^{{2}} }} over {{2}} = {q2}$$/수식$$에서\n" \
              "$$수식$$a^{{2}} + b^{{2}} - {c3}(a + b ) + {c4} = {c5}$$/수식$$,  즉, $$수식$$a^{{2}} + b^{{2}} = {c6}$$/수식$$\n" \
              "$$수식$$c$$/수식$$, $$수식$$d$$/수식$$의 평균이 $$수식$${q3}$$/수식$$이므로\n" \
              "$$수식$${{ c + d }} over {{2}} = {c7}$$/수식$$에서 $$수식$$c + d = {c8}$$/수식$$\n" \
              "$$수식$$c$$/수식$$, $$수식$$d$$/수식$$의 분산이 $$수식$${q4}$$/수식$$이므로\n" \
              "$$수식$${{ (c - {q3})^{{2}} + (d - {q3})^{{2}} }} over {{2}} = {q4}$$/수식$$에서\n" \
              "$$수식$$c^{{2}} + d^{{2}} - {c9}(c + d ) + {c10} = {c11}$$/수식$$,   즉, $$수식$$c^{{2}} + d^{{2}} = {c12}$$/수식$$\n" \
              "따라서 $$수식$$a$$/수식$$, $$수식$$b$$/수식$$, $$수식$$c$$/수식$$, $$수식$$d$$/수식$$의 평균은\n" \
              "$$수식$${{ a + b + c + d }} over {{4}} = {{ {c2} + {c8} }} over {{4}} = {c13}$$/수식$$이고, 분산은\n" \
              "$$수식$${{ (a -{c11})^{{2}} + (b -{c11})^{{2}} + (c -{c11})^{{2}} + (d -{c11})^{{2}} }} over {{4}}$$/수식$$\n" \
              "$$수식$$= {{ a^{{2}} + b^{{2}} + c^{{2}} + d^{{2}} - {c14}(a + b + c + d ) + {c15} }} over {{4}}$$/수식$$\n" \
              "$$수식$${{ {c6} + {c12} - {c14}({c2} + {c8}) + {c15} }} over {{4}} = {c16}$$/수식$$\n\n"

    list_1 = [3, 5, 3, 9]
    list_2 = [2, 6, 2, 10]
    list_3 = [3, 9, 2, 6]
    list_A2 = [list_1, list_2, list_3][np.random.randint(0, 3)]
    t0 = np.random.randint(0, 20)
    for i in range(0, len(list_A2)):
        list_A2[i] += t0
    a, b, c, d = list_A2

    q1 = (a + b) // 2
    q2 = (np.square(a - q1) + np.square(b - q1)) // 2
    q3 = (c + d) // 2
    q4 = (np.square(c - q3) + np.square(d - q3)) // 2
    
    c1 = (a + b) // 2
    c2 = c1 * 2
    c3 = 2 * q1
    c4 = np.square(q1) * 2
    c5 = 2 * q2
    c6 = c5 - c4 + (c3 * c2)
    c7 = (c + d) // 2
    c8 = c7 * 2
    c9 = 2 * q3
    c10 = np.square(q3) * 2
    c11 = 2 * q4
    c12 = c11 - c10 + (c9 * c8)
    c13 = (c2 + c8) // 4
    c14 = c11 * 2
    c15 = np.square(c11) * 4
    c16 = (c6 + c12 - (c14 * (c2 + c8)) + c15) // 4
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16 = RoundCheck([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16])

    a1 = c16

    t1 = np.random.randint(a1 - 2, a1 + 2)
    s_candidates = [t1 - 2, t1 - 1, t1, t1 + 1, t1 + 2]
    s_candidates = RoundCheck(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(q1=q1, q2=q2, q3=q3, q4=q4, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, q2=q2, q3=q3, q4=q4, c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, c6=c6, c7=c7, c8=c8, c9=c9, c10=c10, c11=c11, c12=c12, c13=c13, c14=c14, c15=c15, c16=c16)
    return stem, answer, comment


#######################################################################################
#######################################################################################

def statistics326_Stem_074():
    stem = "통계에 대한 다음 설명 중 옳지 않은 것은? \n" \
        "① {ss1}\n" \
        "② {ss2}\n" \
        "③ {ss3}\n" \
        "④ {ss4}\n" \
        "⑤ {ss5}\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "{a1} {c1}\n\n"

    
    yy = ["편차의 총합은 항상 $$수식$$0$$/수식$$이다.", "편차의 평균은 항상 $$수식$$0$$/수식$$이다.", "모든 변량이 같은 값인 자료의 분산은 $$수식$$0$$/수식$$이다.", "표준편차가 작을수록 그 변량들은 평균 가까이에 분포되어 있다.", "평균이 같은 두 자료의 표준 편차는 서로 다를 수도 있다."]
    nn = ["편차의 총합은 항상 $$수식$$0$$/수식$$이 아니다.", "편차의 평균은 항상 $$수식$$0$$/수식$$이 아니다.", "모든 변량이 같은 값인 자료의 분산은 $$수식$$0$$/수식$$이 아니다.", "표준편차가 작을수록 그 변량들은 평균에서 멀리 분포되어 있다.", "평균이 같은 두 자료의 표준 편차는 서로 같다."]
    
    t0 = np.random.randint(0, 5)
    if t0 == 0:
        list_A2 = [nn[0]] + list(yy[1:])
    elif t0 == 4:
        list_A2 = list(yy[:4]) + [nn[4]]
    else:
        list_A2 = list(yy[0:t0]) + [nn[t0]] + list(yy[t0 + 1:])
    ss1, ss2, ss3, ss4, ss5 = list_A2
    
    c1 = yy[t0]

    a1 = nn[t0]
    
    np.random.shuffle(list_A2)
    s_candidates = list_A2
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
            if s_cand == a1:
                correct_idx = idx
                break

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(a1=answer_dict[correct_idx], c1=c1)
    return stem, answer, comment


def statistics326_Stem_075():
    stem = "다음 중 두 변량 사이에 양의 상관관계가 있다고 말할 수 있는 것은?\n" \
        "① {ss1}\n" \
        "② {ss2}\n" \
        "③ {ss3}\n" \
        "④ {ss4}\n" \
        "⑤ {ss5}\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "{c1}, {c2}, {c3} 상관관계가 없다.\n" \
              "{c4} 음의 상관관계\n" \
              "따라서 양의 상관관계가 있다고 말할 수 있는 것은 {a1}이다.\n\n"

    
    yy = ["키와 앉은키", "키와 몸무게", "마트에서 산 물건의 수와 지불해야 할 금액", "택시 승차 시간과 요금", "인구와 전체 쌀 소비량", "여름철 기온과 물 소비량", "도보로 통학하는 경우 통학거리와 통학하는데 걸리는 시간", "사춘기 소년의 나이와 키", "전화 통화 시간과 전화 요금"]
    nn = ["쌀의 생산량과 쌀값", "낮의 길이와 밤의 길이", "가격과 판매량", "지원자 수와 합격률", "겨울철 기온과 난방비", "산의 높이와 기온", "자동차 수와 평균 주행 속도", "겨울철 기온과 감기 환자의 수"]
    mm = ["몸무게와 걸음의 나비", "가슴둘레와 지능지수", "영어 성적과 체력", "키와 쌀값", "눈동자의 색깔과 시력", "어느 학생의 몸무게와 시력", "통학 시간과 성적"]
    
    list_1 = list(np.random.choice(yy, size=1, replace=False))
    list_2 = list(np.random.choice(nn, size=1, replace=False))
    list_3 = list(np.random.choice(mm, size=3, replace=False))
    s_candidates = list_1 + list_2 + list_3
    a1, c4, c1, c2, c3 = s_candidates
    np.random.shuffle(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates

    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
        elif s_cand == c4:
            c4_idx = idx
        elif s_cand == c1:
            c1_idx = idx
        elif s_cand == c2:
            c2_idx = idx
        elif s_cand == c3:
            c3_idx = idx
        else:
            print("ERROR")
    

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(a1=answer_dict[correct_idx], c1=answer_dict[c1_idx], c2=answer_dict[c2_idx], c3=answer_dict[c3_idx], c4=answer_dict[c4_idx])
    return stem, answer, comment


def statistics326_Stem_076():
    stem = "다음 중 두 변량 사이에 상관관계가 없는 것은?\n" \
        "① {ss1}\n" \
        "② {ss2}\n" \
        "③ {ss3}\n" \
        "④ {ss4}\n" \
        "⑤ {ss5}\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "{c1}, {c2} 음의 상관관계\n" \
              "{c3}, {c4} 양의 상관관계\n" \
              "따라서 상관관계가 없는 것은 {a1}이다.\n\n"

    yy = ["키와 앉은키", "키와 몸무게", "마트에서 산 물건의 수와 지불해야 할 금액", "택시 승차 시간과 요금", "인구와 전체 쌀 소비량", "여름철 기온과 물 소비량", "도보로 통학하는 경우 통학거리와 통학하는데 걸리는 시간", "사춘기 소년의 나이와 키", "전화 통화 시간과 전화 요금"]
    nn = ["쌀의 생산량과 쌀값", "낮의 길이와 밤의 길이", "가격과 판매량", "지원자 수와 합격률", "겨울철 기온과 난방비", "산의 높이와 기온", "자동차 수와 평균 주행 속도", "겨울철 기온과 감기 환자의 수"]
    mm = ["몸무게와 걸음의 나비", "가슴둘레와 지능지수", "영어 성적과 체력", "키와 쌀값", "눈동자의 색깔과 시력", "어느 학생의 몸무게와 시력", "통학 시간과 성적"]

    list_1 = list(np.random.choice(yy, size=2, replace=False))
    list_2 = list(np.random.choice(nn, size=2, replace=False))
    list_3 = list(np.random.choice(mm, size=1, replace=False))
    s_candidates = list_1 + list_2 + list_3
    c3, c4, c1, c2, a1 = s_candidates
    np.random.shuffle(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
        elif s_cand == c4:
            c4_idx = idx
        elif s_cand == c1:
            c1_idx = idx
        elif s_cand == c2:
            c2_idx = idx
        elif s_cand == c3:
            c3_idx = idx
        else:
            print("ERROR")

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(a1=answer_dict[correct_idx], c1=answer_dict[c1_idx], c2=answer_dict[c2_idx], c3=answer_dict[c3_idx] , c4=answer_dict[c4_idx])
    return stem, answer, comment


def statistics326_Stem_077():
    stem = "다음 중 두 변량 사이의 상관관계가 나머지 넷과 다른 하나는?\n" \
        "① {ss1}\n" \
        "② {ss2}\n" \
        "③ {ss3}\n" \
        "④ {ss4}\n" \
        "⑤ {ss5}\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "{c1}, {c2}, {c3}, {c4} {c5}\n" \
              "{a1} {c6}\n" \
              "따라서 상관관계가 나머지 넷과 다른 하나는 {a1}이다.\n\n"

    yy = ["키와 앉은키", "키와 몸무게", "마트에서 산 물건의 수와 지불해야 할 금액", "택시 승차 시간과 요금", "인구와 전체 쌀 소비량", "여름철 기온과 물 소비량", "도보로 통학하는 경우 통학거리와 통학하는데 걸리는 시간", "사춘기 소년의 나이와 키", "전화 통화 시간과 전화 요금"]
    nn = ["쌀의 생산량과 쌀값", "낮의 길이와 밤의 길이", "가격과 판매량", "지원자 수와 합격률", "겨울철 기온과 난방비", "산의 높이와 기온", "자동차 수와 평균 주행 속도", "겨울철 기온과 감기 환자의 수"]
    mm = ["몸무게와 걸음의 나비", "가슴둘레와 지능지수", "영어 성적과 체력", "키와 쌀값", "눈동자의 색깔과 시력", "어느 학생의 몸무게와 시력", "통학 시간과 성적"]
    
    t0 = np.random.randint(0, 6)
    if t0 == 0:
        list_1 = list(np.random.choice(yy, size=4, replace=False))
        list_2 = list(np.random.choice(nn, size=1, replace=False))
        s_candidates = list_1 + list_2
        c1, c2, c3, c4, a1 = s_candidates
        c5, c6 = ["양의 상관관계", "음의 상관관계"]
    elif t0 == 1:
        list_1 = list(np.random.choice(yy, size=4, replace=False))
        list_3 = list(np.random.choice(mm, size=1, replace=False))
        s_candidates = list_1 + list_3
        c1, c2, c3, c4, a1 = s_candidates
        c5, c6 = ["양의 상관관계", "상관관계가 없다."]
    elif t0 == 2:
        list_1 = list(np.random.choice(yy, size=1, replace=False))
        list_2 = list(np.random.choice(nn, size=4, replace=False))
        s_candidates = list_1 + list_2
        a1, c1, c2, c3, c4 = s_candidates
        c5, c6 = ["음의 상관관계", "양의 상관관계"]
    elif t0 == 3:
        list_2 = list(np.random.choice(nn, size=4, replace=False))
        list_3 = list(np.random.choice(mm, size=1, replace=False))
        s_candidates = list_2 + list_3
        c1, c2, c3, c4, a1 = s_candidates
        c5, c6 = ["음의 상관관계", "상관관계가 없다."]
    elif t0 == 4:
        list_1 = list(np.random.choice(yy, size=1, replace=False))
        list_3 = list(np.random.choice(mm, size=4, replace=False))
        s_candidates = list_1 + list_3
        a1, c1, c2, c3, c4 = s_candidates
        c5, c6 = ["상관관계가 없다.", "양의 상관관계"]
    elif t0 == 5:
        list_2 = list(np.random.choice(nn, size=1, replace=False))
        list_3 = list(np.random.choice(mm, size=4, replace=False))
        s_candidates = list_2 + list_3
        a1, c1, c2, c3, c4 = s_candidates
        c5, c6 = ["상관관계가 없다.", "음의 상관관계"]
    
    np.random.shuffle(s_candidates)
    ss1, ss2, ss3, ss4, ss5 = s_candidates
    for idx, s_cand in enumerate(s_candidates):
        if s_cand == a1:
            correct_idx = idx
        elif s_cand == c4:
            c4_idx = idx
        elif s_cand == c1:
            c1_idx = idx
        elif s_cand == c2:
            c2_idx = idx
        elif s_cand == c3:
            c3_idx = idx
        else:
            print("ERROR")

    stem = stem.format(ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(a1=answer_dict[correct_idx], c1=answer_dict[c1_idx], c2=answer_dict[c2_idx], c3=answer_dict[c3_idx] , c4=answer_dict[c4_idx], c5=c5, c6=c6)
    return stem, answer, comment


def statistics326_Stem_078():
    stem = "다음 중 {q1} 사이의 상관관계와 같은 상관관계를 갖는 것은?\n" \
        "① {ss1}\n" \
        "② {ss2}\n" \
        "③ {ss3}\n" \
        "④ {ss4}\n" \
        "⑤ {ss5}\n"
    answer = "(답):{a1}\n"
    comment = "(해설)\n" \
              "{q1} 사이에는 {c6}\n" \
              "{c1}, {c2}, {c3} {c7}\n" \
              "{c4} {c8}\n" \
              "{c5} {c9}\n" \
              "따라서 같은 상관관계를 갖는 것은 {a1}이다.\n\n"

    yy = ["키와 앉은키", "키와 몸무게", "마트에서 산 물건의 수와 지불해야 할 금액", "택시 승차 시간과 요금", "인구와 전체 쌀 소비량", "여름철 기온과 물 소비량", "도보로 통학하는 경우 통학거리와 통학하는데 걸리는 시간", "사춘기 소년의 나이와 키", "전화 통화 시간과 전화 요금"]
    nn = ["쌀의 생산량과 쌀값", "낮의 길이와 밤의 길이", "가격과 판매량", "지원자 수와 합격률", "겨울철 기온과 난방비", "산의 높이와 기온", "자동차 수와 평균 주행 속도", "겨울철 기온과 감기 환자의 수"]
    mm = ["몸무게와 걸음의 나비", "가슴둘레와 지능지수", "영어 성적과 체력", "키와 쌀값", "눈동자의 색깔과 시력", "어느 학생의 몸무게와 시력", "통학 시간과 성적"]
    
    t0 = np.random.randint(0, 6)
    if t0 == 0:
        list_1 = list(np.random.choice(yy, size=3, replace=False))
        list_2 = list(np.random.choice(nn, size=1, replace=False))
        list_3 = list(np.random.choice(mm, size=2, replace=False))
        s_candidates = list_1 + list_2 + list_3
        c1, c2, c3, c4, c5, q1  = s_candidates
        c6, c7, c8, c9 = ["상관관계가 없다.", "양의 상관관계", "음의 상관관계", "상관관계가 없다."]
    elif t0 == 1:
        list_1 = list(np.random.choice(nn, size=3, replace=False))
        list_2 = list(np.random.choice(yy, size=1, replace=False))
        list_3 = list(np.random.choice(mm, size=2, replace=False))
        s_candidates = list_1 + list_2 + list_3
        c1, c2, c3, c4, c5, q1  = s_candidates
        c6, c7, c8, c9 = ["상관관계가 없다.", "음의 상관관계", "양의 상관관계", "상관관계가 없다."]
    elif t0 == 2:
        list_1 = list(np.random.choice(mm, size=3, replace=False))
        list_2 = list(np.random.choice(nn, size=1, replace=False))
        list_3 = list(np.random.choice(yy, size=2, replace=False))
        s_candidates = list_1 + list_2 + list_3
        c1, c2, c3, c4, c5, q1  = s_candidates
        c6, c7, c8, c9 = ["양의 상관관계가 있다.", "상관관계가 없다.", "음의 상관관계", "양의 상관관계"]
    elif t0 == 3:
        list_1 = list(np.random.choice(nn, size=3, replace=False))
        list_2 = list(np.random.choice(mm, size=1, replace=False))
        list_3 = list(np.random.choice(yy, size=2, replace=False))
        s_candidates = list_1 + list_2 + list_3
        c1, c2, c3, c4, c5, q1  = s_candidates
        c6, c7, c8, c9 = ["양의 상관관계가 있다.", "음의 상관관계", "상관관계가 없다.", "양의 상관관계"]
    elif t0 == 4:
        list_1 = list(np.random.choice(mm, size=3, replace=False))
        list_2 = list(np.random.choice(yy, size=1, replace=False))
        list_3 = list(np.random.choice(nn, size=2, replace=False))
        s_candidates = list_1 + list_2 + list_3
        c1, c2, c3, c4, c5, q1  = s_candidates
        c6, c7, c8, c9 = ["음의 상관관계가 있다.", "상관관계가 없다.", "양의 상관관계", "음의 상관관계"]
    elif t0 == 5:
        list_1 = list(np.random.choice(yy, size=3, replace=False))
        list_2 = list(np.random.choice(mm, size=1, replace=False))
        list_3 = list(np.random.choice(nn, size=2, replace=False))
        s_candidates = list_1 + list_2 + list_3
        c1, c2, c3, c4, c5, q1  = s_candidates
        c6, c7, c8, c9 = ["음의 상관관계가 있다.", "양의 상관관계", "상관관계가 없다.", "음의 상관관계"]

    a1 = c5
    s_candidates2 = [c1, c2, c3, c4, c5]
    np.random.shuffle(s_candidates2)
    ss1, ss2, ss3, ss4, ss5 = s_candidates2
    for idx, s_cand in enumerate(s_candidates2):
        if s_cand == a1:
            correct_idx = idx
        elif s_cand == c4:
            c4_idx = idx
        elif s_cand == c1:
            c1_idx = idx
        elif s_cand == c2:
            c2_idx = idx
        elif s_cand == c3:
            c3_idx = idx
        else:
            print("ERROR")

    stem = stem.format(q1=q1, ss1=ss1, ss2=ss2, ss3=ss3, ss4=ss4, ss5=ss5)
    answer = answer.format(a1=answer_dict[correct_idx])
    comment = comment.format(q1=q1, a1=answer_dict[correct_idx], c1=answer_dict[c1_idx], c2=answer_dict[c2_idx], c3=answer_dict[c3_idx] , c4=answer_dict[c4_idx], c5=answer_dict[correct_idx], c6=c6, c7=c7, c8=c8, c9=c9)
    return stem, answer, comment