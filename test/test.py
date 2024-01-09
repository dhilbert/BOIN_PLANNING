import numpy as np







#5-2-6-05
def aveandpro526_Stem_001():
    stem = "다음 $$수식$$4$$/수식$$개의 수의 평균은 얼마인가요?\n$$표$$$$수식$${sa}$$/수식$$    $$수식$${sb}$$/수식$$    $$수식$${sc}$$/수식$$    $$수식$${sd}$$/수식$$$$/표$$\n"
    answer = "(정답)\n$$수식$${ans}$$/수식$$\n"
    comment = "(해설)\n" \
              "$$수식$${sa}$$/수식$$, $$수식$${sb}$$/수식$$, $$수식$${sc}$$/수식$$, $$수식$${sd}$$/수식$$의 수를 고르게 하면 " \
              "$$수식$${m}$$/수식$$, $$수식$${m}$$/수식$$, $$수식$${m}$$/수식$$, $$수식$${m}$$/수식$$이므로 평균은 $$수식$${m}$$/수식$$입니다.\n\n"


    m = np.random.randint(4, 10)
    a = m
    b = m - 1
    c = m + 2
    d = m - 1

    candidates = [a, b, c, d]
    np.random.shuffle(candidates)
    sa, sb, sc, sd = candidates

    stem = stem.format(sa=sa, sb=sb, sc=sc, sd=sd)
    answer = answer.format(ans=m)
    comment = comment.format(sa=sa, sb=sb, sc=sc, sd=sd, m=m)

    return [stem, answer, comment]


print(aveandpro526_Stem_001())
