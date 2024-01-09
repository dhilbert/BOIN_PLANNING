from fractions import Fraction
from math import gcd
import numpy as np
import random

import re

from sympy.ntheory import factorint, isprime, primerange, randprime, divisors

from sympy import sympify, latex

from math import ceil
from functools import reduce
from operator import mul

import sympy as sp

from sympy import powsimp, expand_power_base, simplify, solve, Eq, Integer, Rational, powdenest, symbols
from decimal import Decimal

answer_dict = { 0: "①", 1: "②", 2: "③", 3: "④", 4: "⑤" }
answer_kodict = { 0: "㉠", 1: "㉡", 2: "㉢", 3: "㉣", 4: "㉤" }
# answer_kodict = {0:'가', 1:'나', 2:'다', 3:'라', 4:'마'}

eq = '`=`'
ts = '`times`'
ps = '`+`'
ms = '`-`'
dd = '`div`'
pw = "^"
ov = 'over'
lp = "left ("
rp = "right )"

rb = "`＜`" # right bigger
rs = "`＞`" # right smaller
rqb = "`≤`" # right equal or bigger
rqs = "`≥`" # right equal or smaller

thus = 'therefore~'

eqs = ' `=` '
tss = ' `times` '
pss = ' `+` '
mss = ' `-` '
dds = ' `div` '
pws = " ^ "
ovs = ' over '
lps = " left ( "
rps = " right ) "

rbs = " `＜` " # right bigger
rss = " `＞` " # right smaller
rqbs = " `≤` " # right equal or bigger
rqss = " `≥` " # right equal or smaller

thuss = ' therefore~ '

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
    elif check==10:
        if num in [0, 3, 6]:
            return "으로"
        else :
            return "로"
    elif bool_jo(num):
        # 을를
        return "을"
    return "를"

def lcm(a, b):
    return a * b // gcd(a, b)

"① ② ③ ④ ⑤"
"① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}"


## ========== get divisor of an integer ==============

## sympy.ntheory.divisors()

def getDivisors(number) :
    smaller = []
    larger = []
    maxSearch = int(number**0.5) + 1

    for i in range(1, maxSearch):
        remainder = number % i
        if not remainder :
            smaller.append(i)
            larger.append(number//i)

    larger.reverse()
    if smaller[-1] == larger[0] :
        res = smaller + larger[1:]
    else :
        res = smaller + larger

    return res

## ================= get coprime nubmers ==============
def getCoprimeList(number) :
    allNumber= range(1, number+1)
    factorized = factorint(number)
    primes = factorized.keys()
    second = []

    for p in primes :
        for n in allNumber :
            if n % p :
                second.append(n)
        allNumber = second
        second = []

    return allNumber

# decimal tuple (소수튜플) => (1.3, 334)
# decimal formula (규칙에 맞는 소수 한글 서식) => 1.3 dot3 3 dot4
# decimal number (늘여쓴 소수 한글 서식) => 1.3334334334...

## ================= make random fraction ==================
# choice1 = repeating/non-repeating (yes, no, rand) & if repeating, the max length of repeat
# choice2 = more than 1/less than 1/random (yes, no, rand)
# choice3 = reducible/irreducible (yes, no, rand)
# choice4 = max digit for each number and probability of digits as list
# 분수튜플을 임의로 생성하는 함수입니다.
def makeRandomFraction(repeat='no', repeatMax=3, nonrepeatMax=10, minValue=0, maxValue=0, irreducible='yes',
                       numeratorMaxDigit = (0, (0, )), denominatorMaxDigit = (0, (0, )),
                       returnDecimal=False, over1='no', maxDigit=None):
    # for legacy
    if minValue or maxValue : #최솟값 또는 최댓값을 지정한 경우 over1은 무력화됩니다.
        pass
    else : #최솟값, 최댓값이 0인 경우에는 over1의 값에 따라 최솟값이나 최댓값을 조정합니다.
        if over1=='no':
            maxValue = 1
        elif over1=='yes':
            minValue = 1

    if maxDigit is None :
        maxDigit = {'numerator': (2, (0.4, 0.6)), 'denominator': (2, (0.2, 0.8))}

    if numeratorMaxDigit != (0, (0, )) :
        maxDigit['numerator'] = numeratorMaxDigit
    if denominatorMaxDigit != (0, (0, )):
        maxDigit['denominator'] = denominatorMaxDigit


    # maxDigit의 자리수의 값과 가중치 리스트의 길이는 동일해야 합니다
    if maxDigit['numerator'][0] != len(maxDigit['numerator'][1]) \
            or maxDigit['denominator'][0] != len(maxDigit['denominator'][1]):
        raise ValueError("wrong input on maxDight")

    while True:
        # print('new start')
        # 실제 사용할 자리수를 주어진 가중치에 맞게 결정합니다.
        denominatorDigit = random.choices(range(1, maxDigit['denominator'][0] + 1), weights=maxDigit['denominator'][1])[0]

        # 자리수를 기초로 하여 분모를 먼저 구합니다.
        denominator = random.choice(range(10 ** (denominatorDigit - 1), 10 ** denominatorDigit))
        if denominator == 1 :
            continue

        # 주어진 함수의 조건을 충족하는지 확인합니다.

        numeratorConditionSatisfied = False
        while not numeratorConditionSatisfied :
            # 분자 생성
            numeratorDigit = random.choices(range(1, maxDigit['numerator'][0] + 1), weights=maxDigit['numerator'][1])[0]
            numerator = random.choice(range(10 ** (numeratorDigit - 1), 10 ** numeratorDigit))
            # print("numerator:", numerator, 'denom:', denominator)

            # 분수값 조건 확인
            fracValue = numerator/denominator
            if fracValue == 1 :
                continue
            if minValue :
                if fracValue < minValue :
                    continue
            if maxValue :
                if fracValue > maxValue :
                    continue

            # print(numerator, denominator)

            # 기약분수 조건 확인
            if irreducible=='yes' :
                numeratorFactored = factorint(numerator)
                denominatorFactored = factorint(denominator)

                hasCommonFactors = False

                for denomFactor in denominatorFactored:
                    if denomFactor in numeratorFactored :
                        hasCommonFactors = True

                if hasCommonFactors:
                    continue

            numeratorConditionSatisfied = True
            # print('numerator created')

        #순환마디를 체크하기 위해 소수튜플로 변환합니다.
        decimalTuple = fractionToDecimalTuple(numerator, denominator)

        # 유한소수인 경우 순환부가 있으면 처음부터 다시 시작합니다.
        if repeat=='no':
            if decimalTuple[1]:
                continue
        else: # 무한소수이거나 혹은 조건이 주어지지 않은 경우
            # 무한소수인데 순환부가 없으면 처음부터 다시 시작합니다.
            if repeat=='yes':
                if not decimalTuple[1]:
                    continue
            # 순환마디의 길이가 최댓값을 넘어선 경우 처음부터 다시 시작합니다.
            if len(decimalTuple[1]) > repeatMax :
                continue
            # 비순환부의 길이가 최댓값을 넘어선 경우 처음부터 다시 시작합니다.
            if len(decimalTuple[0].split(".")[1]) > nonrepeatMax :
                continue

        # print(decimalTuple)
        break

    frac = (numerator, denominator)
    if returnDecimal :
        return (frac, decimalTuple)
    else :
        return frac

## =================== fraction to decimal tuple ===================
#분수튜플을 소수튜플로 변환하는 함수입니다
def fractionToDecimalTuple(numerator, denominator):
    # print("---->", numerator, "/", denominator)
    # 1차 몫을 계산합니다. 최초에는 반복이 없다고 가정합니다.
    nonrepeat = str(numerator // denominator) + "."
    repeat = ""
    # 나중에 순환마디를 찾을 때 최초에 구한 순환하지 않는 부분의 길이가 필요하므로 미리 저장해 둡니다.
    # 이 이후부터는 계속 나머지를 저장하기 때문에 인덱스로 추적할 수 있습니다.
    initialNonrepeatLen = len(nonrepeat)
    # 1차 몫을 계산한 후 나머지를 저장합니다. 나머지는 추후 순환마디를 찾을 때 활용합니다.
    subresults = [numerator % denominator]  ### changed ###
    # 나머지를 새로운 피제수로 정하고 다음 계산을 진행합니다. 원리는 필산 나눗셈과 동일합니다.
    numerator %= denominator
    while numerator != 0:
        numerator *= 10
        result_digit, numerator = divmod(numerator, denominator) #divmod는 몫과 나머지를 한꺼번에 알려주는 함수입니다.
        # 일단 계산된 몫은 비반복부라고 가정하고 끝에 값을 추가합니다.
        nonrepeat += str(result_digit)

        # 나머지는 기존에 나왔던 나머지가 아닌 경우 새로 추가하고, 다음 단계로 진행합니다.
        if numerator not in subresults:
            subresults.append(numerator)
        # 기존에 나왔던 나머지가 나온 경우 이후부터는 순환하므로 정지하고 순환마디를 지정합니다.
        else:
            # 기존에 나왔던 나머지의 위치를 리스트에서 찾고, 처음에 구한 비순환부의 길이를 더하면 순환마디의 시작점을 알 수 있습니다.
            repeatStart = subresults.index(numerator) + initialNonrepeatLen
            # 순환마디를 자릅니다.
            repeat = nonrepeat[repeatStart:]
            nonrepeat = nonrepeat[:repeatStart]
            break

    return nonrepeat, repeat

## =============== decimal tuple to fraction ========================
# 소수튜플을 분수튜플로 변환합니다. 분수에 적당한 수를 곱하여 순환마디를 맞춘 후 뺄셈하여 구하는 방법을 사용합니다.
def decimalTupleToFraction(decTup, irreducible=True):
    #소숫점 이하에서 비순환하는 길이를 구해 둡니다.
    nonrepeatLen = len(decTup[0].split(".")[1])
    #순환마디의 길이를 구합니다.
    repeatLen = len(decTup[1])

    if repeatLen :
        #순환하지 않는 앞부분에 적당한 수를 곱하여 모두 정수로 바꾸어 주는 과정입니다.
        frontPart = decTup[0].replace(".", "")
        # 순환소수의 분모 및 분자 부분을 계산합니다.
        denominator = 10 ** (repeatLen + nonrepeatLen) - 10 ** nonrepeatLen
        numerator = int(frontPart + decTup[1]) - int(frontPart)
    else :
        denominator = 10 ** nonrepeatLen
        numerator = int(decTup[0].replace(".", ""))

    # 결과값을 기약분수로 받을지 확인하여 기약분수인 경우 Fraction클래스를 활용합니다.
    if irreducible:
        f = Fraction(numerator, denominator)
        return f.numerator, f.denominator
    else:
        return numerator, denominator

## ===================== with 수식 tag ================
# 양끝에 수식 태그를 붙여주는 함수입니다.
def addTag(content) :
    if isinstance(content, list) or isinstance(content, tuple):
        return [addTag(x) for x in content]
    else :
        return "$$수식$$" + str(content) + "$$/수식$$"


aT = addTag
## ======================= fraction formula ======================
# 분수튜플을 한글 수식으로 변환해 줍니다. 단독으로 입력할 상황을 대비하여 태그를 달아 출력할 수 있습니다.
def makeFractionFormula(numerator, denominator, withTag=False) :
    if withTag :
        return addTag("{n} over {d}".format(n="{" + str(numerator) + "}", d="{" + str(denominator) + "}"))
    else :
        return "{n} over {d}".format(n="{" + str(numerator) + "}", d="{" + str(denominator) + "}")

## ================== make correct representation of a tuple decimal ===============
# 소수튜플 중 순환소수를 규칙에 맞게 한글 수식으로 변환해 주는 함수입니다.
def makeCorrectDecimalFormula(nonrepeat, repeat, withTag=False):
    if len(repeat) == 0 :
        content = nonrepeat
    elif len(repeat) == 1 : #마디의 길이가 1인 경우
        content = "".join([nonrepeat, " dot", repeat[0]])
    else : #마디의 길이가 2 이상인 경우
        startRepeat = repeat[0]
        endRepeat = repeat[-1]
        middle = repeat[1:-1]
        content = "".join([nonrepeat, " dot", startRepeat, " ", middle, " dot", endRepeat])

    if withTag :
        return addTag(content)
    else :
        return content

## ================= long real decimal (ellipsis) =============
# 소수튜플을 늘여쓴 한글 수식으로 바꾸어 줍니다.
def makeDecimalNumber(decimal, withTag=False) :
    if decimal[1] : #순환마디가 있는 무한소수인 경우 마디를 3번 반복하고 끝에 가운뎃점 3개를 찍습니다
        content = "".join([decimal[0], decimal[1]*3, " cdots"])
    else : # 순환마디가 없는 유한소수인 경우
        content = decimal[0]

    if withTag :
        return addTag(content)
    else :
        return content

## ================== make wrong representation of a tuple decimal =================
# 올바르지 않은 순환소수를 생성하는 종류입니다. 마디의 개수가 2, 3인 경우만 적용할 수 있습니다.
# 유형1, 2, 3은 마디의 개수가 2개인 경우, 유형2, 3, 4는 마디의 개수가 3개인 경우에 각각 적용할 수 있습니다.

#유형1 : 마디가 2자리일 때, 첫 자리를 한 번 더 붙여 세 자리 마디로 바꿉니다
def makeWrongDecimalFormula_1(nonrepeat, repeat, withTag=False) :  #only when repeat length is 2
    if len(repeat) == 2 :
        content = "".join([nonrepeat, " dot", repeat[0]," ", repeat[1], " dot", repeat[0]])
    else :
        return "wrong1"
    if withTag :
        return addTag(content)
    else :
        return content

# 유형2 : 순환마디의 뒤에 첫 자리를 더 붙여 틀린 표현으로 만듭니다.
def makeWrongDecimalFormula_2(nonrepeat, repeat, withTag=False) :
    if len(repeat) == 2:
        content = "".join([nonrepeat, " dot", repeat[0], " dot", repeat[1], " ", repeat[0]])
    else : # len(repeat) == 3
        content = "".join([nonrepeat, " dot", repeat[0], " ", repeat[1], " dot", repeat[2], " ", repeat[0]])
    if withTag :
        return addTag(content)
    else :
        return content

# 유형3 : 순환마디의 첫 자리를 비순환부에 덧붙이고, 실제순환마디는 한 자리씩 앞으로 이동하는 식으로 바꿉니다.
def makeWrongDecimalFormula_3(nonrepeat, repeat, withTag=False):
    if len(repeat) == 2 :
        content = "".join([nonrepeat, " ", repeat[0], " dot", repeat[1], " dot", repeat[0]])
    else : # len(repeat) == 3
        content = "".join([nonrepeat, " ", repeat[0], " dot", repeat[1], " ", repeat[2], " dot", repeat[0]])
    if withTag :
        return addTag(content)
    else :
        return content

# 유형4 : 순환마디 전체에 모두 윗점을 찍습니다.
def makeWrongDecimalFormula_4(nonrepeat, repeat, withTag=False) : #only when repeat length is 3
    if len(repeat) == 2 :
        return "wrong4"
    else : # len(repeat) == 3
        content = "".join([nonrepeat, " dot", repeat[0], " dot", repeat[1], " dot", repeat[2]])
    if withTag :
        return addTag(content)
    else :
        return content

## ======================== make variation of tuple decimals ================
# 세 개의 한 자리 정수를 이용하여 5가지의 순환소수튜플을 만듭니다.
def generateDecimalTuples(front, middle, end):
    res = []
    res.append((front+".", middle+end))
    res.append((front+".", middle+end+middle))
    res.append((front+"."+middle, middle+end))
    res.append((front+"."+end, end+middle))
    res.append((front+".", end+middle+end))
    return res

## =================== make 4 wrong and 1 correct choices of decimal representations===========
# 순환소수튜플과 정답이 결정되어 있는 상태에서, 순환소수튜플을 올바른 한글 수식으로 나타내는지를 자동으로 짝지어 줍니다.
def makeChoiceFormulas(decimals, answerIndex):
    wrongType_2_length = [makeWrongDecimalFormula_1, makeWrongDecimalFormula_1, makeWrongDecimalFormula_2, makeWrongDecimalFormula_3]
    wrongType_3_length = [makeWrongDecimalFormula_2, makeWrongDecimalFormula_3, makeWrongDecimalFormula_4, makeWrongDecimalFormula_4]
    res = []
    for index, decimal in enumerate(decimals):
        if index == answerIndex:
            res.append(makeCorrectDecimalFormula(*decimal))
        else:
            if len(decimal[1]) == 2:
                res.append(np.random.choice(wrongType_2_length)(*decimal))
            else:
                res.append(np.random.choice(wrongType_3_length)(*decimal))
    return res

## =============== make equality from two ordered lists ========
# 양변의 리스트를 바탕으로 등식 한글 수식 묶음을 만듭니다.
def makeEquality(leftList, rightList, withTag=False):
    length = len(leftList)
    if length != len(rightList) :
        return "equation pairing error"
    else :
        contents = [str(leftList[i]) + "`=`" + str(rightList[i]) for i in range(length)]
    if withTag :
        contents = [addTag(content) for content in contents]
    return contents

## =================== check whether it is a repeating decimal ============
# 분수튜플이 순환소수인지 아닌지를 판단해 줍니다.
def isRepeatingDecimal(fractionTuple) :
    dec = fractionToDecimalTuple(*fractionTuple)
    if dec[1]: #순환마디부에 값이 있다면 순환소수
        return True
    else :
        return False

## ================== make random decimals ====================
# 임의의 소수튜플을 만듭니다. 순환마디의 길이와 비순환부의 크기 및 자리수를 고려합니다.
def makeRandomDecimal(integerDigit, nonRepeatDigit, repeatDigit) :
    #integerDigit : 정수 부분에 들어갈 값의 자리수를 생각합니다. 0인 경우는 0, 1 이상인 경우 해당 자릿수에 맞는 랜덤한 숫자
    #nonRepeatDigit : 소수 부분의 비순환부 자리수입니다. 0인 경우는 비순환부가 없고, 1 이상인 경우 위와 동일
    #repeatDigit : 순환마디의 길이입니다. 0인 경우는 순환부가 없고, 1이상인 경우는 위와 동일합니다!
    if integerDigit :
        frontPart = str(random.choice(range(10**(integerDigit-1), 10**integerDigit))) + "."
    else :
        frontPart = '0.'
    if nonRepeatDigit :
        while True :
            middlePart = random.choice(range(10**(nonRepeatDigit-1), 10**nonRepeatDigit))
            if repeatDigit :
                break
            else :
                if middlePart % 10 != 0 :
                    break
        middlePart = str(middlePart)
    else :
        middlePart = ""
    # 순환마디와 비순환하는 소수의 끝부분이 일치하는 경우 순환마디를 다시 생성합니다.
    # 또, 순환마디의 숫자가 모두 9인 경우에는 재생성합니다.
    # 순환마디의 자리수가 2 이상일 때, 같은 수가 나온 경우에는 재생성합니다.
    if repeatDigit :
        while True :
            endPart = str(random.choice(range(10**(repeatDigit-1), 10**repeatDigit)))
            endNumbers = set([x for x in endPart])

            duplicated = False
            if middlePart :
                for eN in endNumbers :
                    if eN in middlePart :
                        duplicated = True

            if duplicated:
                continue

            if len(endPart) == 1 and endPart == "9" :
                continue
            elif len(endPart) > 1 and len(endNumbers) == 1 :
                continue

            break
        # print('finished', middlePart, endNumbers)
    else :
        endPart = ""

    return frontPart+middlePart, endPart

# ===========================================================================
# 순환소수의 소숫점 이하 특정 자리의 숫자를 구합니다.
def findDigitInDecimal(decimal, nth, returnType=int) :
    length_repeat = len(decimal[1])
    res = 0
    # 순환 소수만 다룹니다.
    if length_repeat :
        nonrepeat = decimal[0].split(".")[1]
        # 소수점 이하에 비순환부가 있는 경우에는, 구하는 자리의 값에 따라 다시 경우를 나눕니다.
        if nonrepeat :
            length_nonrepeat = len(nonrepeat)
            # 구하려는 자리가 비순환부 안에 있는 경우
            if nth <= length_nonrepeat :
                res = nonrepeat[nth-1]
            # 구하려는 자리가 비순환부 밖에 있는 경우
            else :
                nth = nth - length_nonrepeat
                remainder = nth % length_repeat
                res = decimal[1][remainder-1]
        else :
            remainder = nth % length_repeat
            res = decimal[1][remainder - 1]
        return returnType(res)
    else :
        raise ValueError("wrong input.")

## =================================================================
# 나눗셈 몫과 나머지를 담은 식을 만들어 줍니다.
def divisionEquation(numerator, denominator):
    quotient, remainder = divmod(numerator, denominator)

    resEquation = " ".join([str(x) for x in [numerator, "=", denominator, 'times', quotient]])
    if remainder:
        resEquation += " + " + str(remainder)

    return resEquation

# ==============
# 수식에 공간을 주는 함수
def giveSpace(text, space="`"):
    return space + text + space

gS = giveSpace


## ==================== 분모 또는 분자를 인수분해한 형태의 식을 만들어주는 함수 =====
def getFactoredIntFormula(number, equalityFront=False, equalityEnd=False, withTag=False, returnFactorDict=False):
    factored = factorint(int(number))
    n_f = []
    if factored:
        for k in factored:
            if factored[k] == 1:
                n_f.append(str(k))
            else:
                n_f.append(str(k) + "^" + str(factored[k]))
    else:
        n_f.append(str(1))

    factoredFormula = " times ".join(n_f)

    if equalityFront :
        factoredFormula = str(number) + " = " + factoredFormula
    if equalityEnd :
        factoredFormula = factoredFormula + " = " + str(number)

    if withTag :
        factoredFormula = aT(factoredFormula)

    if returnFactorDict :
        return factoredFormula, factored
    else :
        return factoredFormula


def makeFactoredFractionFormula(fraction, toBeFactored=(False, True), withTag=False):
    if not toBeFactored[0] and not toBeFactored[1] :
        raise ValueError("no need to use this function if both of them are not to be factored")

    if toBeFactored[0] :
        numeratorFormula = getFactoredIntFormula(fraction[0])

    if toBeFactored[1] :
        denominatorFormula = getFactoredIntFormula(fraction[1])

    if toBeFactored[0] and not toBeFactored[1] :
        res = makeFractionFormula(numeratorFormula, fraction[1], withTag=withTag)
    elif toBeFactored[0] and toBeFactored[1] :
        res = makeFractionFormula(numeratorFormula, denominatorFormula, withTag=withTag)
    elif not toBeFactored[0] and toBeFactored[1] :
        res = makeFractionFormula(fraction[0], denominatorFormula, withTag=withTag)

    return res

# ===========common tasks when making questions =====================
# make denominator that gives non-repeat decimal
def twoFiveDenom(twoRange=(0, 4), fiveRange=(0, 3)) :
    while True :
        two_up = random.choice(range(*twoRange))
        five_up = random.choice(range(*fiveRange))
        denominator = 2 ** two_up * 5 ** five_up

        if denominator != 1 :
            break

    denominator_factored = getFactoredIntFormula(denominator)

    return denominator, denominator_factored

# get multiples of a number under a certain range
def multipleUnderRange(number, start, end):
    quotient, remainder = divmod(start, number)
    if remainder :
        start = (quotient+1) * number
    return list(range(start, end, number))

# get an equation of some symbols with random coefficients
def getRandomEquation(givenChars = ('x', 'y'), coefficientRange = ((1, 4), (-2, 0)), realValues = (1, 1), avoidZero=False):
    if len(givenChars) != len(coefficientRange) or len(coefficientRange) != len(realValues) :
        raise ValueError("The length of all parameters should be same")

    coeffs = []
    for start, end in coefficientRange :
        while True :
            tempCoeff = random.choice(range(start, end))
            if avoidZero and not tempCoeff :
                continue
            break

        coeffs.append(tempCoeff)

    ansValue = sum([reduce(mul, item) for item in zip(coeffs, realValues)])

    # make Text
    resText = ""
    for ind, coeff in enumerate(coeffs) :
        added = ""
        if coeff == 1 :
            added = "`+"
        elif coeff > 1 :
            added = "`+" + str(coeff)
        elif coeff == -1 :
            added = "`-"
        elif coeff == 0 :
            pass
        else: # coeff < -1
            added = "`" + str(coeff)

        if added :
            resText += added
            resText += givenChars[ind]

    resText = resText[1:]
    if resText[0] == "+" :
        resText = resText[1:]

    resDict = {
        'coeffs' : coeffs,
        'ansValue' : ansValue,
        'text' : resText
    }

    return resDict

## =========== 선택지를 만드는 함수 ===============
def makeChoices(ansValue, diff=1, positive=False, positiveWithoutZero=False, withTag=True) :
    while True :
        answerMinus = random.choice(range(5))
        minusValue = answerMinus * diff
        valueGap = ansValue - minusValue
        if positive and valueGap < 0 :
            continue
        elif positiveWithoutZero and valueGap <= 0 :
            continue
        break

    endSum = diff * 5

    ansNums = [x for x in range(ansValue - minusValue, ansValue - minusValue + endSum, diff)]

    if withTag :
        ansNums = list(map(aT, ansNums))

    ansIndex = answerMinus

    return ansIndex, ansNums

## ================== 리스트 원소를 조인하는 함수 ==============
def joinList(joinList, sep=" ") :
    return sep.join(map(str, joinList))

def replaceParen(matchObj):
    string = matchObj.group()
    res = "{" + string[1:-1] + "}"
    return res

def preserveTimes(matchObj):
    string = matchObj.group()
    res = string.replace("*", tss)
    return res

def convertIntoHangul(stringRepresentation, leaveTimes=False, slashToDiv=False, removeSpace=False, parenToBracket=False,
                      timesToSpace=False, bracketToFrac=False, minusWithSpace=False, avoidNumMinus=False):

    if not isinstance(stringRepresentation, str) :
        stringRepresentation = str(stringRepresentation)

    res = stringRepresentation

    if minusWithSpace :
        res = res.replace("-", " - ")
    # else :
    #     res = res.replace("-", ms)

    # res = res.replace("+", ps)

    if bracketToFrac :
        splited = [x.strip() for x in res.split("/")]

        if len(splited) == 2 :
            if splited[1].startswith("(") and splited[1].endswith(")") :
                splited[1] = wrapParen(splited[1][1:-1])
            else :
                splited[1] = wrapParen(splited[1])

            numText = splited[0].strip()
            if avoidNumMinus :
                if numText.startswith("-") :
                    numText = wrapParen(numText[1:])
                    numText = mss + numText
            else :
                numText = wrapParen(splited[0])
            res = joinList([numText, "/", splited[1]])

    #지수의 괄호를 중괄호로 바꾸어주는 것(가장 중요)
    res = re.sub(r"(?<=[\*]{2})\(.*?\)", replaceParen, res)

    res = re.sub(r"[0-9]+?\*[0-9]+?", preserveTimes, res)

    res = res.replace("**", pw)

    if slashToDiv :
        res = res.replace("/", dds)
    else :
        res = res.replace("/", ovs)

    if leaveTimes :
        res = res.replace("*", tss)
    elif timesToSpace :
        res= res.replace("*", " ")
    else :
        res = res.replace("*", "")

    if removeSpace :
        res = res.replace(" ", "")

    if parenToBracket :
        res = res.replace("(", "{")
        res = res.replace(")", "}")

    return res

def convertNegExp(expression):
    if isinstance(expression, str) :
        converted = sympify(expression)
    else :
        converted = expression

    converted = converted * -1
    res = str(converted)[1:]

    return res

def exponentForm(base, exp, paren=True, baseParen=False):
    if exp == 1:
        res = str(base)
    else:
        if baseParen :
            base = ' left ( ' + base + ' right ) '

        res = joinList([" ", base, pw, "{", exp, "} "], "")

        if paren:
            res = " left ( " + res + " right ) "

    return res

def wrapParen(exp, replace=False):
    exp = str(exp)
    if replace :
        res = joinList(["{", exp[1:-1], "}"], "")
    else :
        res = joinList(["{", exp, "}"])
    return res

def getNumberCalc(numbers, withRes=False):
    resList = [numbers[0]]
    for n in numbers[1:] :
        if n < 0 :
            resList.append(n)
        else :
            resList.append(ps)
            resList.append(n)

    if withRes :
        resList.append(eq)
        resList.append(sum(numbers))

    return joinList(resList)

def connectEqations(eq1Text, eq2Text):
    eq1Text = str(eq1Text).strip()
    eq2Text = str(eq2Text).strip()

    resText = eq1Text

    if eq2Text.startswith("-") :
        resText = resText + " " + eq2Text
    else :
        resText = resText + " + " + eq2Text

    return resText

def handleNegExpChar(base, exp):
    expStr = str(exp)

    if "-" in expStr:
        numExp, denomExp = [x.strip() for x in expStr.split("-")]
        numerator = exponentForm(base, numExp)
        denominator = exponentForm(base, denomExp)
        return makeFractionFormula(numerator, denominator)

    else :
        return exponentForm(base, exp)

def stringReplace(string, replacePairs):
    string = str(string)

    for pair in replacePairs :
        string = string.replace(*pair)

    return string

def getPolyText(sympyExpr, *mainChar):
    poly = sympyExpr.as_poly(*mainChar)
    polyText = str(poly)[5:].split(", ")[0]

    return polyText

def latexToHwp(latexText):
    if "frac" in latexText :
        latexText = latexText.replace("}{", "} over {")
        latexText = latexText.replace("\\frac", "")
    return latexText


# =====================================================================================
# =====================================================================================




def rationalandprime211_Stem_001():
    stem = "다음 중 순환소수의 표현이 옳은 것은?\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{c1}\n{c2}\n{c3}\n{c4}\n\n"

    # randomly choose three integers less than 10
    numbers = list(map(str, random.sample(range(1, 9), k=3)))

    # make five repeating decimals
    realDecimals = generateDecimalTuples(*numbers)
    random.shuffle(realDecimals)
    realDecimals = tuple(realDecimals) # to prevent the possibility of order change

    answerIndex = random.choice(range(5)) # pick an answer
    needComments = list(range(5))
    needComments.remove(answerIndex)

    decimalChoices = makeChoiceFormulas(realDecimals, answerIndex)

    stemChoiceRes = makeEquality([makeDecimalNumber(dec) for dec in realDecimals], decimalChoices, withTag=True)
    # print(stemChoiceRes)
    [s1, s2, s3, s4, s5] = stemChoiceRes

    commentChoices = []
    for i in range(5):
        if i == answerIndex:
            pass
        else:
            commentChoices.append(makeCorrectDecimalFormula(*realDecimals[i]))

    commentFormulas = makeEquality([makeDecimalNumber(realDecimals[i]) for i in needComments], commentChoices, withTag=True)

    commentNumbers = [answer_dict[i] for i in needComments]

    finalComments = [commentNumbers[i] + " " + commentFormulas[i] for i in range(len(needComments))]

    [c1, c2, c3, c4] = finalComments

    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[answerIndex])
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4)

    return stem, answer, comment


def rationalandprime211_Stem_002():
    stem = "다음 중 옳{s0} 것은?\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment_pos = "(해설)\n{c1}\n{c2}\n{c3}\n{c4}\n\n"
    comment_neg = "(해설)\n{c1}\n\n"

    # 긍정형 질문인지 부정형 질문인지를 결정합니다.
    posOrNeg = random.choice([True, False])

    # 선택지의 형태는 아래 네 가지 중의 하나를 사용합니다.
    choice_rational = "{fraction}{postp} 유리수{statement}."
    choice_singleFrac = "{fraction}{postp} 소수로 나타내면 {decimalType}이다."
    choice_decimalNum = "{decNum}{postp} {decimalType}이다."
    choice_doubleFrac = "두 분수 {frac1}{postp1} {frac2}{postp2} 소수로 나타내면 {decimalType}이다."

    comment_singleFrac = "$$수식$${fraction}`=`{decNum}$$/수식$$ 이므로 {decimalType}이다."
    comment_doubleFrac = "$$수식$${frac1}`=`{decNum1}$$/수식$$ 이므로 {decType1}이고, $$수식$${frac2}`=`{decNum2}$$/수식$$ 이므로 {decType2}이다."

    choices_empty = [choice_rational, choice_singleFrac, choice_decimalNum, choice_doubleFrac]
    choices_empty.append(random.choice(choices_empty[1:])) #omit choice_rational

    answerIndex = random.choice(range(5))
    choices_filled = []
    comments = []

    for ind, string in enumerate(choices_empty) :
        isAnswer = (ind == answerIndex)
        if string == choice_rational :
            frac = makeRandomFraction(repeat='yes', over1='rand')
            fraction = makeFractionFormula(*frac, withTag=True)
            postp = proc_jo(frac[0], -1)
            if (posOrNeg and isAnswer) or (not posOrNeg and not isAnswer) : #맞는 답을 고르는 상황, 정답일 때 or 틀린 답을 고르는 상황, 오답일 때
                statement, commentStatement = "이다", "가 아니다"
            else : # 맞는 답을 고르는 상황, 오답일 때 or 틀린 답을 고르는 상황, 정답일 때
                statement, commentStatement = "가 아니다", "이다"
            temp = string.format(fraction=fraction, postp=postp, statement=statement)
            _comment = string.format(fraction=fraction, postp=postp, statement=commentStatement)
        elif string == choice_singleFrac :
            frac = makeRandomFraction(repeat='rand', over1='rand')
            fraction = makeFractionFormula(*frac)
            postp = proc_jo(frac[0], -1)
            # 유한소수/무한소수 여부를 판단하기 위해
            dec = fractionToDecimalTuple(*frac)
            isRepeating = dec[1]
            if isRepeating :
                if (posOrNeg and isAnswer) or (not posOrNeg and not isAnswer) :
                    decimalType, commentDecimalType = "무한소수", "유한소수"
                else :
                    decimalType, commentDecimalType = "유한소수", "무한소수"
            else :
                if (posOrNeg and isAnswer) or (not posOrNeg and not isAnswer) :
                    decimalType, commentDecimalType = "유한소수", "무한소수"
                else :
                    decimalType, commentDecimalType = "무한소수", "유한소수"
            temp = string.format(fraction=addTag(fraction), postp=postp, decimalType=decimalType)
            _comment = comment_singleFrac.format(fraction=fraction, decNum=makeDecimalNumber(dec),
                                                decimalType=commentDecimalType)
        elif string == choice_decimalNum :
            isRepeating = random.choice(range(1))
            if isRepeating : #isRepeating == 1 then repeating, ==0 then not repeating
                decimalTuple = makeRandomDecimal(random.choice(range(1)), random.choice(range(1)), random.choice(range(1, 4)))
                if (posOrNeg and isAnswer) or (not posOrNeg and not isAnswer) :
                    decimalType, commentDecimalType = "무한소수", "유한소수"
                else :
                    decimalType, commentDecimalType = "유한소수", "무한소수"
                postp = proc_jo(int(decimalTuple[1][-1]), -1)
            else : #not repeating
                decimalTuple = makeRandomDecimal(random.choice(range(1)), random.choice(range(1, 4)), 0)
                if (posOrNeg and isAnswer) or (not posOrNeg and not isAnswer) :
                    decimalType, commentDecimalType = "유한소수", "무한소수"
                else :
                    decimalType, commentDecimalType = "무한소수", "유한소수"
                postp = proc_jo(int(decimalTuple[0][-1]), -1)
            decNum = makeDecimalNumber(decimalTuple, withTag=True)

            temp = string.format(decNum=decNum, postp=postp, decimalType=decimalType)
            _comment = string.format(decNum=decNum, postp=postp, decimalType=commentDecimalType)
        else :
            isRepeating = random.choice(range(1))
            if isRepeating:  #isRepeating == 1 then repeating, ==0 then not repeating
                decimalType = "무한소수"
                if (posOrNeg and isAnswer) or (not posOrNeg and not isAnswer):
                    frac1 = makeRandomFraction(repeat='yes', over1='no')
                    while True :
                        frac2 = makeRandomFraction(repeat='yes', over1='rand')
                        if frac2[1] != frac1[1] :
                            break
                else:
                    frac1 = makeRandomFraction(repeat='rand', over1='rand')
                    while True:
                        frac2 = makeRandomFraction(repeat='no', over1='no')
                        if frac2[1] != frac1[1]:
                            break
            else:  # not repeating
                decimalType = "유한소수"
                if (posOrNeg and isAnswer) or (not posOrNeg and not isAnswer):
                    frac1 = makeRandomFraction(repeat='no', over1='no')
                    while True:
                        frac2 = makeRandomFraction(repeat='no', over1='rand')
                        if frac2[1] != frac1[1]:
                            break
                else:
                    frac1 = makeRandomFraction(repeat='yes', over1='rand')
                    while True:
                        frac2 = makeRandomFraction(repeat='rand', over1='no')
                        if frac2[1] != frac1[1]:
                            break
            fraction1 = makeFractionFormula(*frac1)
            fraction2 = makeFractionFormula(*frac2)
            postp1 = proc_jo(frac1[0], 2)
            postp2 = proc_jo(frac2[0], -1)
            temp = string.format(frac1=addTag(fraction1), postp1=postp1,
                                 frac2=addTag(fraction2), postp2=postp2, decimalType=decimalType)
            dec1 = fractionToDecimalTuple(*frac1)
            dec2 = fractionToDecimalTuple(*frac2)
            decNum1 = makeDecimalNumber(dec1)
            decNum2 = makeDecimalNumber(dec2)
            if dec1[1] :
                decType1 = "무한소수"
            else :
                decType1 = "유한소수"
            if dec2[1] :
                decType2 = "무한소수"
            else :
                decType2 = "유한소수"
            _comment = comment_doubleFrac.format(frac1=fraction1, decNum1=decNum1, decType1=decType1,
                                                frac2=fraction2, decNum2=decNum2, decType2=decType2)
        choices_filled.append(temp)
        comments.append(_comment)

    #make question according to its type
    if posOrNeg :
        s0 = "은"
    else :
        s0 = "지 않은"

    [s1, s2, s3, s4, s5] = choices_filled

    if posOrNeg :
        needComments = []
        for i in range(5):
            if i == answerIndex:
                pass
            else:
                needComments.append(i)
        finalComments = [answer_dict[i] + " " + comments[i] for i in needComments]

        [c1, c2, c3, c4] = finalComments
        comment = comment_pos.format(c1=c1, c2=c2, c3=c3, c4=c4)
    else :
        c1 = answer_dict[answerIndex] + " " + comments[answerIndex]
        comment = comment_neg.format(c1=c1)

    # print(c1, c2, c3, c4, sep='\n')
    stem = stem.format(s0=s0, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[answerIndex])

    return stem, answer, comment


def rationalandprime211_Stem_003():
    stem = "두 분수 {frac1}{postp1} {frac2}{postp2} 소수로 나타낼 때, 순환마디를 이루는 숫자의 개수를 각각 $$수식$$a,```b$$/수식$$라 할 때 {formula}의 값을 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{frac1}이므로 순환마디는 {repeat1}이다.\n{avalue}\n{frac2}이므로 순환마디는 {repeat2}이다.\n{bvalue}\n{answerFormula}\n\n"

    # 먼저, 순환소수인 분수 2개를 생성합니다.
    fraction1 = makeRandomFraction(repeat='yes', repeatMax=5)
    while True : # 같은 분모인 경우를 제거합니다.
        fraction2 = makeRandomFraction(repeat='yes', repeatMax=5)
        if fraction1[1] != fraction2[1] :
            break

    postp1 = proc_jo(fraction1[0], check=2)
    postp2 = proc_jo(fraction2[0], check=1)

    # 분수튜플을 소수튜플로 변환합니다.
    decimal1 = fractionToDecimalTuple(*fraction1)
    decimal2 = fractionToDecimalTuple(*fraction2)

    # 변수의 값을 먼저 구합니다.
    a = len(decimal1[1])
    b = len(decimal2[1])

    # a와 b에 붙을 계수를 구합니다.
    coeff_a = random.choice(range(1, 6))
    coeff_b = random.choice(range(-5, 0))

    # 정답을 구합니다.
    answerValue = coeff_a*a + coeff_b*b

    # 위 내용으로 문제를 구성하기 위한 텍스트를 모두 생성합니다.
    frac1 = makeFractionFormula(*fraction1)
    frac2 = makeFractionFormula(*fraction2)
    dec1 = makeDecimalNumber(decimal1)
    dec2 = makeDecimalNumber(decimal2)

    # 한글 수식에서 계수가 1이거나 -1인 경우를 조정합니다.
    if coeff_a == 1 :
        _coeff_a = ""
    else :
        _coeff_a = coeff_a

    if coeff_b == -1 :
        _coeff_b = "-"
    else :
        _coeff_b = coeff_b

    formula = "".join([str(x) for x in [_coeff_a, 'a', '`', _coeff_b, 'b']])

    # 해설부에 필요한 등식을 순서대로 생성합니다.
    equalitiesForComment = makeEquality([frac1, 'therefore~a', frac2, 'therefore~b', 'therefore~'+formula], [dec1, str(a), dec2, str(b), str(answerValue)], withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(frac1=addTag(frac1), postp1=postp1, frac2=addTag(frac2), postp2=postp2, formula=addTag(formula))
    answer = answer.format(a1=addTag(str(answerValue)))
    comment = comment.format(frac1=equalitiesForComment[0], repeat1=addTag(str(decimal1[1])), avalue=equalitiesForComment[1],
                             frac2=equalitiesForComment[2], repeat2=addTag(str(decimal2[1])), bvalue=equalitiesForComment[3],
                             answerFormula=equalitiesForComment[4])

    return stem, answer, comment


def rationalandprime211_Stem_004():
    stem = "다음 중 분수를 소수로 나타낼 때, 순환마디가 나머지 넷과 다른 하나는?\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n주어진 분수를 소수로 나타내어 순환마디를 구하면 다음과 같다.\n① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}\n\n"

    # 순환마디를 정합니다. 계산량을 고려하여 1자리 범위에서 숫자를 지정합니다. 이 때 9는 제외합니다.
    # 순환마디를 정할 때 넷과 다른 1개의 순환마디를 만들 때 사용할 숫자도 함께 고릅니다.
    repeatPart, _other = [str(x) for x in random.sample(range(1, 9), 2)]
    # print('digit 1', repeatPart, _other)
    otherPart = repeatPart + _other

    # 정답을 정합니다.
    answerValue = random.choice(range(5))

    # 비순환부를 정하여 분수를 구합니다. 이 때, 분모가 최소 3종류 이상 나와야 합니다.
    denominators = {}
    fractions = []
    ind = 0
    while ind < 5:
        digit = random.choice(range(4))
        if digit:  # 비순환부가 0이 아닌 경우 숫자를 구한 후, 10으로 나누어 문자열로 변환합니다.
            done = False
            while not done:  # 비순환부의 소수 자리는 1자리 또는 2자리이고, 끝자리가 순환부와 겹치지 않도록 합니다.
                nonrepeat = random.choice(range(10 ** (digit - 1), 10 ** digit))
                _nonrepeat = str(nonrepeat)
                if repeatPart not in _nonrepeat and _other not in _nonrepeat :
                    if digit < 3 :
                        nonrepeatPart = str(nonrepeat / 10)
                    else :
                        nonrepeatPart = str(nonrepeat / 100)
                    done = True
        else:  # 비순환부가 0인 경우 정수 부분이 없고 소수점부터 바로 순환마디가 시작됩니다.
            nonrepeatPart = "0."

        # 분수로 만들어 봅니다.
        if ind == answerValue :
            tempFrac = decimalTupleToFraction((nonrepeatPart, otherPart))
        else :
            tempFrac = decimalTupleToFraction((nonrepeatPart, repeatPart))

        # 중복된 분모, 세 자리 수 이상의 분모, 중복된 분수는 피합니다.
        if tempFrac[1] > 100 :
            continue

        if tempFrac[1] in denominators :
            if denominators[tempFrac[1]] >= 2 :
                continue

        if tempFrac in fractions :
            continue

        fractions.append(tempFrac)
        denominators.setdefault(tempFrac[1], 0)
        denominators[tempFrac[1]] += 1
        ind += 1

    # 위의 확보된 정보로 소수와 분수를 각각 생성합니다.
    decimals = [fractionToDecimalTuple(*frac) for frac in fractions]

    # 소수와 분수의 한글 서식을 각각 생성합니다.
    decimalFormulas = [makeDecimalNumber(dec) for dec in decimals]
    fractionFormulas = [makeFractionFormula(*frac) for frac in fractions]

    # 서식을 채워넣습니다.
    s1, s2, s3, s4, s5 = [addTag(formula) for formula in fractionFormulas]
    commentList = makeEquality(fractionFormulas, decimalFormulas, withTag=True)

    repeatPart_tagged = addTag(repeatPart)
    otherPart_tagged = addTag(otherPart)

    ind = 0
    while ind < 5:
        if ind == answerValue:
            commentList[ind] = commentList[ind] + " ⇨ " + otherPart_tagged
        else:
            commentList[ind] = commentList[ind] + " ⇨ " + repeatPart_tagged
        ind += 1

    c1, c2, c3, c4, c5 = commentList

    # 내용을 채웁니다.
    stem = stem.format(s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[answerValue])
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5)

    return stem, answer, comment


def rationalandprime211_Stem_005():
    stem = "다음 중 가장 {s0} 수는?\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}\n따라서 가장 {s0} 수는 {a1}이다.\n\n"

    # 큰 것, 작은 것 중 고릅니다.
    isBig = random.choice([True, False])

    # 순환마디에 사용할 서로 다른 숫자 4개를 고릅니다.
    int1, int2, int3, int4 = [str(x) for x in random.sample(range(1, 8), 4)]

    # 다섯개의 소수튜플을 생성합니다.
    dec1 = ("".join(["0.", int1, int2, int3, int4]), "")
    dec2 = ("".join(["0.", int1, int2, int3]), int4)
    dec3 = ("".join(["0.", int1, int2]), int3 + int4)
    dec4 = ("0." + int1, "".join([int2, int3, int4]))
    dec5 = ("0.", "".join([int1, int2, int3, int4]))

    # 소수튜플 리스트와 분수튜플 리스트를 만듭니다.
    decimals = [dec1, dec2, dec3, dec4, dec5]
    decimalValues = {}

    for dec in decimals :
        if dec[1] :
            frac = decimalTupleToFraction(dec)
            val = float(frac[0])/float(frac[1])
        else :
            val = float(dec[0])
        decimalValues[dec] = val

    # 가장 큰 것 혹은 작은 것을 골라냅니다.
    sortedItems = sorted(decimalValues.items(), key=lambda x : x[1])
    if isBig :
        largest_smallest = sortedItems[-1]
        s0 = "큰"
    else :
        largest_smallest = sortedItems[0]
        s0 = "작은"

    # 소수튜플을 섞습니다.
    random.shuffle(decimals)

    # 정답 인덱스를 구합니다.
    answerValue = decimals.index(largest_smallest[0])

    # 질문에 쓰일 소수 표현식을 구합니다.
    # print(decimals)
    decFormulas = [makeCorrectDecimalFormula(*dec) if dec[1] else dec[0] for dec in decimals]
    decFormulas_tagged = [addTag(dec) for dec in decFormulas]

    # 해설에 쓰일 소수 표현식을 구합니다.
    decEqualities = []
    for ind, dec in enumerate(decimals) :
        temp = makeEquality([decFormulas[ind]], [makeDecimalNumber(dec)], withTag=True)[0]
        # print(temp)
        decEqualities.append(temp)

    # 서식에 알맞게 집어 넣습니다.
    s1, s2, s3, s4, s5 = decFormulas_tagged
    c1, c2, c3, c4, c5 = decEqualities
    a1 = answer_dict[answerValue]

    # 내용을 채웁니다.
    stem = stem.format(s0=s0, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=a1)
    comment = comment.format(c1=c1, c2=c2, c3=c3, c4=c4, c5=c5, s0=s0, a1=a1)

    return stem, answer, comment

def rationalandprime211_Stem_006():
    stem = "분수 {frac}{postp} 소수로 나타낼 때, 소수점 아래 {num1}번째 자리의 숫자를 {a}, {num2}번째 자리의 숫자를 {b}라 할 때, {formula}의 값은?\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{fracFormula}이므로 {repeatPart}{postp} 순서대로 반복되어 나타난다.\n이 때, {num1Formula}이므로 소수점 아래 {num1}번째 숫자는 {aValue}이다. {aFormula}\n" \
              "또 {num2Formula}이므로 소수점 아래 {num2}번째 숫자는 {bValue}이다. {bFormula}\n{formulaAnswer}\n\n"

    # 순환소수인 분수를 하나 생성합니다. 이 때 순환마디가 3이상 6이하로 맞춥니다.
    while True:
        fraction = makeRandomFraction(repeat='yes', repeatMax=6)
        decimal = fractionToDecimalTuple(*fraction)
        length_repeat = len(decimal[1])
        if length_repeat > 2 and int(fraction[1]) < 71 and len(decimal[0]) == 2:
            break

    # 자리수를 구할 자리를 정합니다.
    num1 = random.choice(range(10, 100))
    num2 = random.choice(range(100, 201))

    # 변수의 값을 먼저 구합니다.
    quotient1, remainder1 = divmod(num1, length_repeat)
    quotient2, remainder2 = divmod(num2, length_repeat)

    a = int(decimal[1][remainder1 - 1])
    b = int(decimal[1][remainder2 - 1])

    # a와 b에 붙을 계수를 구합니다.
    coeff_a = random.choice(range(1, 4))
    coeff_b = random.choice(range(-3, 0))

    # 정답을 구합니다.
    answerValue = coeff_a * a + coeff_b * b

    # 한글 수식에서 계수가 1이거나 -1인 경우를 조정합니다.
    if coeff_a == 1:
        _coeff_a = ""
    else:
        _coeff_a = coeff_a

    if coeff_b == -1:
        _coeff_b = "-"
    else:
        _coeff_b = coeff_b

    formula = "".join([str(x) for x in [_coeff_a, 'a', '`', _coeff_b, 'b']])

    # 보기로 사용할 숫자를 생성합니다.
    jump = random.choice(range(1, 4))
    answerInd = random.choice(range(5))
    startNum = answerValue - jump * answerInd
    stemNumbers = range(startNum, startNum + jump * 5, jump)

    # 해설에 사용할 등식을 모두 생성합니다.
    fracFormula = makeFractionFormula(*fraction)
    decimalNumber = makeDecimalNumber(decimal)

    num1Formula = " ` ".join([str(x) for x in [length_repeat, 'times', quotient1]])
    if remainder1:
        num1Formula += " ` + ` " + str(remainder1)
    num2Formula = " ` ".join([str(x) for x in [length_repeat, 'times', quotient2]])
    if remainder2:
        num2Formula += " ` + ` " + str(remainder2)

    leftPart = [fracFormula, str(num1), 'therefore~a', str(num2), 'therefore~b', 'therefore~'+formula]
    rightPart = [decimalNumber, num1Formula, str(a), num2Formula, str(b), str(answerValue)]

    #     print(leftPart)
    #     print(rightPart)

    equalities = makeEquality(leftPart, rightPart, withTag=True)

    repeatPart = addTag(",``".join([x for x in decimal[1]]))

    s1, s2, s3, s4, s5 = [addTag(str(x)) for x in stemNumbers]

    # 내용을 채웁니다.
    stem = stem.format(frac=addTag(fracFormula), postp=proc_jo(int(fraction[0]), -1),
                       num1=addTag(str(num1)), a=addTag('a'),
                       num2=addTag(str(num2)), b=addTag('b'),
                       formula=addTag(formula), s1=s1, s2=s2, s3=s3, s4=s4, s5=s5)
    answer = answer.format(a1=answer_dict[answerInd])
    comment = comment.format(fracFormula=equalities[0], repeatPart=repeatPart, postp=proc_jo(int(decimal[1][-1])),
                             num1Formula=equalities[1], num1=addTag(str(num1)), aValue=addTag(str(a)),
                             aFormula=equalities[2],
                             num2Formula=equalities[3], num2=addTag(str(num2)), bValue=addTag(str(b)),
                             bFormula=equalities[4],
                             formulaAnswer=equalities[5])

    return stem, answer, comment


def rationalandprime211_Stem_007():
    stem = "분수 {frac}{postp_f} 소수로 나타낼 때, 소수점 아래 첫째자리의 숫자부터 소수점 아래 {num1}번째 자리의 숫자까지의 합을 구하시오.\n"
    answer = "(답): {a1}\n"
    comment_before = "(해설)\n{fracFormula}에서 {repeatPart}{postp_d} 순서대로 반복된다.\n" \
                    "{num1Formula}이므로 {repeatPart}{postp_d} {num2}번 반복"
    comment_after_1 = "된다. 따라서 구하는 합은 {answerFormula}이다.\n\n"
    comment_after_2 = "된 후, {remainingPart}{postp2} 한 번 더 나오게 된다.\n따라서 구하는 합은 {answerFormula}이다.\n\n"

    # 순환소수인 분수를 하나 생성합니다. 이 때 순환마디가 3이상 6이하로 맞춥니다.
    while True:
        fraction = makeRandomFraction(repeat='yes', repeatMax=6)
        decimal = fractionToDecimalTuple(*fraction)
        length_repeat = len(decimal[1])
        if length_repeat > 2 and int(fraction[1]) < 71 and len(decimal[0]) == 2:
            break

    # 자리수를 구할 자리를 정합니다.
    num1 = random.choice(range(10, 91))

    # 순환마디를 리스트로 만듭니다.
    repeatList = [int(x) for x in decimal[1]]
    repeatList_string = [x for x in decimal[1]]
    repeatSum = sum(repeatList)

    quotient1, remainder1 = divmod(num1, length_repeat)

    # a = int(decimal[1][remainder1 - 1])
    answerValue = repeatSum*quotient1 + sum(repeatList[:remainder1])

    # 서식에 들어갈 텍스트를 차례대로 생성합니다.
    frac = makeFractionFormula(*fraction)
    decNum = makeDecimalNumber(decimal)
    repeatString = ", ".join(repeatList_string)
    remainingString = ", ".join(repeatList_string[:remainder1])

    num1Formula = " ".join([str(x) for x in [length_repeat, 'times', quotient1]])
    if remainder1:
        num1Formula += " + " + str(remainder1)

    _repeat_sum_string = "".join(["( ", " + ".join(repeatList_string), " ) ", 'times ', str(quotient1)])
    _remaining_sum_string = "".join([" + ", " + ".join(repeatList_string[:remainder1])])

    if remainingString :
        formulaString = _repeat_sum_string + _remaining_sum_string
        comment = comment_before + comment_after_2
    else :
        formulaString = _repeat_sum_string
        comment = comment_before + comment_after_1

    # 해설에 사용할 등식을 모두 생성합니다.
    leftPart = [frac, str(num1), formulaString]
    rightPart = [decNum, num1Formula, str(answerValue)]

    equalities = makeEquality(leftPart, rightPart, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(frac=addTag(frac), postp_f=proc_jo(int(fraction[0]), 1),
                       num1=addTag(str(num1)))
    answer = answer.format(a1=str(answerValue))
    comment_before = comment_before.format(fracFormula=equalities[0], repeatPart=repeatString, postp_d=proc_jo(int(decimal[1][-1]), 0),
                                           num1Formula=equalities[1], num2=str(quotient1))
    if remainingString :
        comment_after_2 = comment_after_2.format(remainingPart=remainingString, postp2=proc_jo(repeatList[:remainder1][-1], 0),
                                                 answerFormula=equalities[2])
        comment = comment_before + comment_after_2
    else :
        comment_after_1 = comment_after_1.format(answerFormula=equalities[2])
        comment = comment_before + comment_after_1

    return stem, answer, comment


def rationalandprime211_Stem_008():
    stem = "서로 다른 세 분수 {xyz}를 소수로 나타내면 각각 순환소수, 유한소수, 순환소수이다. " \
           "다음 중 그 값을 나타내면 항상 순환소수인 것은?\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{c1}\n{c2}\n{c3}\n{c4}\n\n"

    # x, z 순환/ y 유한

    alwaysRepeat = ["X+Y", 'X divide Y', "Y+Z"]
    undetermined = ["X+Z", "X times Z", "Y divide Z", "X times Y", "Y times Z", "X divide Z"]

    # aR_counter = {
    #     "X+Y": "".join([addTag("X = 1 over 3 ,~ Y = 1 over 2"), "이면 ", addTag("X+Y = 5 over 6 = 0.8333 cdots")]),
    #     "X divide Y": "".join([addTag("X = 1 over 3 ,~ Y = 1 over 2"), "이면 ", addTag("X divide Y = 2 over 3 = 0.6666 cdots")]),
    #     "Y+Z": "".join([addTag("Y = 1 over 2 ,~ Z = 1 over 3"), "이면 ", addTag("Y+Z = 5 over 6 = 0.8333 cdots")]),
    # }
    # undecided_repeat = {
    #     "X+Z": "".join([addTag("X = 1 over 3 ,~ Z = 1 over 3"), "이면 ", addTag("X+Z = 2 over 3 = 0.6666 cdots")]),
    #     "X times Z": "".join([addTag("X = 1 over 3 ,~ Z = 1 over 3"), "이면 ", addTag("X times Z = 1 over 9 = 0.1111 cdots")]),
    #     "Y divide Z": "".join([addTag("Y = 1 over 2 ,~ Z = 3 over 7"), "이면 ", addTag("Y divide Z = 7 over 6 = 1.1666 cdots")]),
    #     "X times Y": "".join([addTag("X = 1 over 3 ,~ Y = 1 over 2"), "이면 ", addTag("X times Y = 1 over 6 = 0.1666 cdots")]),
    #     "Y times Z": "".join([addTag("Y = 1 over 2 ,~ Z = 1 over 3"), "이면 ", addTag("Y times Z = 1 over 6 = 0.1666 cdots")]),
    #     "X divide Z": "".join([addTag("X = 1 over 3 ,~ Z = 1 over 7"), "이면 ", addTag("X divide Z = 7 over 3 = 2.6666 cdots")])
    # }
    undetermined_nonrepeat = {
        "X+Z": "".join([addTag("X = 1 over 3"), ", ", addTag("~ Z = 1 over 6"), "이면 ", addTag("X+Z = 1 over 2 = 0.5")]),
        "X times Z": "".join([addTag("X = 3 over 7"), ", ", addTag("~ Z = 7 over 6"), "이면 ", addTag("X times Z = 1 over 2 = 0.5")]),
        "Y divide Z": "".join([addTag("Y = 1 over 2"), ", ", addTag("~ Z = 1 over 3"), "이면 ", addTag("Y divide Z = 3 over 2 = 1.5")]),
        "X times Y": "".join([addTag("X = 1 over 3"), ", ", addTag("~ Y = 3 over 5"), "이면 ", addTag("X times Y = 1 over 5 = 0.2")]),
        "Y times Z": "".join([addTag("Y = 3 over 5"), ", ", addTag("~ Z = 1 over 3"), "이면 ", addTag("Y times Z = 1 over 5 = 0.2")]),
        "X divide Z": "".join([addTag("X = 1 over 3"), ", ", addTag("~ Z = 2 over 3"), "이면 ", addTag("X divide Z = 1 over 2 = 0.5")])
    }

    # res = "\n".join(["\n".join(aR_counter.values()), "\n".join(undecided_repeat.values()), "\n".join(undecided_nonrepeat.values())])

    # 정답을 구합니다.
    answerInd = random.choice(range(5))

    # 선지를 구합니다.
    _choices = random.sample(undetermined, k=4)
    _choices.insert(answerInd, random.choice(alwaysRepeat))
    choices = [addTag(x) for x in _choices]

    # 해설을 구합니다.
    commentList = []
    for i in range(5):
        if i == answerInd:
            pass
        else:
            temp = answer_dict[i] + " " + undetermined_nonrepeat[_choices[i]]
            commentList.append(temp)

    # 서식에 결과물을 삽입합니다.
    stem = stem.format(xyz = addTag("X ,~ Y ,~ Z"), s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[answerInd])
    comment = comment.format(c1=commentList[0], c2=commentList[1], c3=commentList[2], c4=commentList[3])

    return stem, answer, comment


def rationalandprime211_Stem_009():
    stem = "분수 {frac}{postp1} 소수로 나타낼 때, 소수점 아래 {n}번째 자리의 숫자를 {fn}이라 하자. 옳은 것을 보기에서 모두 고르시오.\n{choice1}\n{choice2}\n{choice3}\n"
    answer = "(답): {a1}\n"
    comment = "{fracEquation}이므로 순환마디를 이루는 숫자는 {x}개이고, {fxs}\n{c1_front1}이므로 {c1_after1}\n{c2_front1}이므로 {c2_after1}, {c2_front2}이므로 {c2_after2}\n{c2_answer}\n" \
              "{c3_front}이므로\n{c3_sum1}{c3_sum2}\n따라서, 옳은 것은 {a1}이다.\n\n"
    # comment = "{fracEquation}이므로 순환마디를 이루는 숫자는 {x}개이고, {fxs}\n{c1_front1}이므로 {c1_after1}\n{c2_front1}이므로 {c2_after1}\n{c2_front2}이므로 {c2_after2}"
    # comment2 = "\n{c2_answer}\n{c3_sum1}\n{c3_sum2}\n따라서, 옳은 것은 {a1}이다.\n\n"

    # 순환소수인 분수를 하나 생성합니다. 이 때 순환마디가 3이상 6이하로 맞춥니다.
    while True:
        fraction = makeRandomFraction(repeat='yes', repeatMax=6)
        decimal = fractionToDecimalTuple(*fraction)
        length_repeat = len(decimal[1])
        if length_repeat > 2 and int(fraction[1]) < 71 and len(decimal[0]) == 2:
            break

    # 정답이 될 선택지를 미리 구합니다.
    answers = random.sample([0, 1, 2], k=random.choice([1, 2, 3]))

    # ㄱ에 해당하는 선택지를 만듭니다.
    firstN = random.choice(range(10, 100))
    firstInd = firstN % length_repeat - 1

    if 0 in answers:
        #         print(type(decimal[1][firstInd]))
        firstFormula = "".join(["f(", str(firstN), ")`=`", decimal[1][firstInd]])
    else:
        firstRange = decimal[1].replace(decimal[1][firstInd], "")
        firstFormula = "".join(["f(", str(firstN), ")`=`", random.choice(firstRange)])

    # ㄴ에 해당하는 선택지를 만듭니다.
    second1, second2 = random.sample(range(10, 100), k=2)
    second1_ind = second1 % length_repeat - 1
    second2_ind = second2 % length_repeat - 1

    right = ""
    wrong = []

    if int(decimal[1][second1_ind]) > int(decimal[1][second2_ind]):
        right = "`＞`"
        wrong = ['`＝`', '`＜`']
    elif int(decimal[1][second1_ind]) == int(decimal[1][second2_ind]):
        right = "`＝`"
        wrong = ["`＜`", "`＞`"]
    else:
        right = "`＜`"
        wrong = ["`＞`", "`＝`"]

    if 1 in answers:
        secondFormula = "".join(["f(", str(second1), ")", right, "f(", str(second2), ")"])
    else:
        secondFormula = "".join(["f(", str(second1), ")", random.choice(wrong), "f(", str(second2), ")"])

    # ㄷ에 해당하는 선택지를 만듭니다.
    startNum = random.choice(range(10, 61))
    targetNumbers = range(startNum, startNum + 5)

    targetRes = [decimal[1][i % length_repeat - 1] for i in targetNumbers]
    value = sum(map(int, targetRes))

    fs = "`+`".join(["f(" + str(i) + ")" for i in targetNumbers])
    if 2 in answers:
        thirdFormula = "".join([fs, "`=`", str(value)])
    else:
        thirdFormula = "".join([fs, "`=`", str(value + 1)])

    # 해설을 만듭니다.
    decimalFormula = makeCorrectDecimalFormula(*decimal)

    f1tofn = ["f(" + str(i) + ")" for i in range(1, length_repeat + 1)]

    firstN_eq = divisionEquation(firstN, length_repeat)
    second1_eq = divisionEquation(second1, length_repeat)
    second2_eq = divisionEquation(second2, length_repeat)

    firstComment = "".join(["f(", str(firstN), ")`=`", decimal[1][firstInd]])
    second1Comment = "".join(["f(", str(second1), ")`=`", decimal[1][second1_ind]])
    second2Comment = "".join(["f(", str(second2), ")`=`", decimal[1][second2_ind]])
    secondAnswer = "".join(["f(", str(second1), ")", right, "f(", str(second2), ")"])

    fNums = "=" + "`+`".join([str(x) for x in targetRes])

    frac = makeFractionFormula(*fraction)
    equalities = makeEquality([frac] + f1tofn + [fNums], [decimalFormula] + [x for x in decimal[1]] + [str(value)])

    # 내용을 채웁니다.
    stem = stem.format(frac=addTag(frac), postp1=proc_jo(int(fraction[0]), 1), n=addTag('n'), fn=addTag("f(n)"),
                       choice1 = answer_kodict[0] +" "+ addTag(firstFormula), choice2 = answer_kodict[1] +" "+ addTag(secondFormula), choice3 = answer_kodict[2]+ " "+ addTag(thirdFormula))
    answerText = ", ".join([answer_kodict[i] for i in range(3) if i in answers])
    answer = answer.format(a1=answerText)

    comment = comment.format(fracEquation=addTag(equalities[0]), x=addTag(str(length_repeat)),
                             fxs=", ".join(map(addTag, equalities[1:1 + length_repeat])),
                             c1_front1=answer_kodict[0] + " " + addTag(firstN_eq), c1_after1=addTag(firstComment),
                             c2_front1=answer_kodict[1] + " " + addTag(second1_eq), c2_after1=addTag(second1Comment),
                             c2_front2=addTag(second2_eq), c2_after2=addTag(second2Comment),
                             c2_answer=addTag("therefore " + secondAnswer),
                             c3_front=answer_kodict[2] + " " + addTag(divisionEquation(startNum, length_repeat)), c3_sum1=addTag(fs), c3_sum2=addTag(equalities[-1]), a1=answerText)

    return stem, answer, comment


def rationalandprime211_Stem_010():
    stem = "{fracSum}{postp} 소수로 나타낼 때, 소수점 아래 {n}번째 자리의 숫자를 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{fracSum}\n{parenSum}\n{simplifiedSum}\n{decimalSum}\n{decimalNumber}{decimalFormula}\n이 때, " \
                     "{division}이므로 소수점 아래 {n}번째 자리의 숫자는 순환마디 {repeatPart}의 {nn} 번째 자리 숫자인 {ans}이다.\n\n"

    # 문제 생성에 사용할 숫자 4개를 뽑습니다.
    while True:
        first, second, third = random.choices(range(1, 10), k=3)

        repeatPart = str(second * 10 - third)

        if str(first) in repeatPart :
            continue

        if len(repeatPart) == 2 :
            if repeatPart[0] != repeatPart[1] :
                break

    first, second, third = map(str, [first, second, third])

    n = random.choice(range(10, 100))

    # 답을 구합니다.
    remainder = (n-1) % 2
    if not remainder :
        nn = "두"
    else :
        nn = "첫"

    # 식을 만듭니다.
    fracSum = "".join([makeFractionFormula(first+second, "10^2"), " - ", makeFractionFormula(third, "10^3"), " + ",
                       makeFractionFormula(second, "10^4"), " - ", makeFractionFormula(third, "10^5"), " + ",
                       makeFractionFormula(second, "10^6"), " + cdots"])
    parenSum = "".join(["= left ( ", makeFractionFormula(first+second+"0", "10^3"), " - ", makeFractionFormula(third, "10^3"), " right ) + left ( ",
                       makeFractionFormula(second+"0", "10^5"), " - ", makeFractionFormula(third, "10^5"), " right ) + left ( ",
                       makeFractionFormula(second+"0", "10^7"), " - ", makeFractionFormula(third, "10^7"), " right ) + cdots"])
    num1 = str(int(first+second+"0") - int(third))
    num2 = num1[1:]

    ans = num2[remainder-1]

    simplifiedSum = "".join(["= ", makeFractionFormula(num1, "10^3"), " + ", makeFractionFormula(num2, "10^5"),
                             " + ", makeFractionFormula(num2, "10^7"), " + cdots"])

    decimalSum = "".join(["= ", "0.", num1, " + 0.000", num2, " + 0.00000", num2, " + cdots"])

    decimalFormula = "= " + makeCorrectDecimalFormula("0." + first, num2)
    decimalNumber = "= " + makeDecimalNumber(("0."+ first, num2))

    division = divisionEquation(n-1, 2)
    division = "".join([str(n), " = 1 + ", division[4:]])

    # 내용을 채웁니다.
    stem = stem.format(fracSum=addTag(fracSum), postp=proc_jo(int(second), 1), n=addTag(str(n)))
    answer = answer.format(a1=addTag(ans))
    comment = comment.format(fracSum=addTag(fracSum), parenSum=addTag(parenSum), simplifiedSum=addTag(simplifiedSum),
                             decimalSum=addTag(decimalSum), decimalFormula=addTag(decimalFormula),
                             decimalNumber=addTag(decimalNumber), division=addTag(division), n=addTag(str(n)),
                             repeatPart=addTag(repeatPart), nn=nn, ans=addTag(ans))

    return stem, answer, comment


def rationalandprime211_Stem_011():
    stem = "다음은 분수 {frac}{postp} 유한소수로 나타내는 과정이다. 이 때, {bc_a}의 값을 구하시오.\n{fracConvert}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{a}, {b}, {c}이므로\n{bc_a}\n\n"

    # 문제 생성에 사용할 숫자들을 생성합니다.
    twos = ["", "2", "2^2", "2^3", "2^4"]
    fives = ["", "5", "5^2", "5^3", "5^4"]

    two_up, five_up = random.sample(range(5), k=2)
    bigger_up = max(two_up, five_up)

    b = 10 ** bigger_up

    bigger_up = str(bigger_up)

    initialDenominator = 2**two_up * 5**five_up
    a = int(b / initialDenominator)

    numerators = [3, 7, 9, 11, 13, 17]
    numerator = random.choice(numerators)

    c = numerator / initialDenominator

    # 식을 만듭니다.
    if two_up :
        if five_up :
            denom = twos[two_up] + " times " + fives[five_up]
        else :
            denom = twos[two_up]
    else :
        if five_up :
            denom = fives[five_up]

    frac = makeFractionFormula(numerator, denom)
    # print(frac)
    postp = proc_jo(numerator%10, 1)

    bc_a = addTag("bc-a")

    ans = int(b*c-a)

    fracConvert = "".join([frac, " = ", makeFractionFormula(str(numerator) + " times a", "".join([denom, " times a"])),
                           " = ", makeFractionFormula(numerator*a, "b"), " = c"])

    a_comment = "a = " + str(a)
    b_comment = "".join(["b = ", "2^", bigger_up, ' times ', "5^", bigger_up, " = 10^", bigger_up, " = ", str(b)])
    c_comment = "c = " + str(c)

    bc_a_comment = "".join(["bc-a = ", str(b), " times ", str(c), " - ", str(a), " = ", str(int(b*c)), " - ", str(a), " = ", str(ans)])

    # 내용을 채웁니다.
    stem = stem.format(frac=aT(frac), postp=postp, bc_a=bc_a, fracConvert=aT(fracConvert))
    answer = answer.format(a1=addTag(ans))
    comment = comment.format(a=aT(a_comment), b=aT(b_comment), c=aT(c_comment), bc_a=aT(bc_a_comment))

    return stem, answer, comment


def rationalandprime211_Stem_012():
    stem = "다음 분수 중 분모를 10의 거듭제곱으로 나타낼 수 없는 것을 고르면?\n① {frac1}\n② {frac2}\n③ {frac3}\n④ {frac4}\n⑤ {frac5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{c1}\n{c2}\n{c3}\n{c4}\n{c5}\n\n"

    # 문제 생성에 사용할 숫자들을 생성합니다.
    twos = ["", "2", "2^2", "2^3", "2^4"]
    fives = ["", "5", "5^2", "5^3"]

    fractions = [] # (unfactorized fraction, fraction formula for comment)
    _frac = []

    while len(fractions) < 4 :
        while True :
            two_up = random.choice(range(5))
            five_up = random.choice(range(4))

            if two_up != five_up:
                break

        bigger_up = max(two_up, five_up)
        b = 10 ** bigger_up
        bigger_up = str(bigger_up)

        initialDenominator = 2**two_up * 5**five_up
        a = int(b / initialDenominator)

        numerators = [3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29]

        if two_up :
            if not five_up:
                numerators.extend([5, 10, 15])
        else :
            if five_up :
                numerators.extend([2, 4, 6, 8, 12, 14])

        numerator = random.choice(numerators)


        # 식을 만듭니다.
        if two_up :
            if five_up :
                denom = twos[two_up] + " times " + fives[five_up]
            else :
                denom = twos[two_up]
        else :
            if five_up :
                denom = fives[five_up]

        frac = makeFractionFormula(numerator, initialDenominator)
        frac_factorized = makeFractionFormula(numerator, denom)
        frac_times = makeFractionFormula(" ".join([str(numerator), 'times', str(a)]), " ".join([denom, "times", str(a)]))
        frac_10s = makeFractionFormula(numerator*a, "10^"+bigger_up)

        if frac in _frac :
            continue
        else :
            fractions.append((frac, " = ".join([frac, frac_factorized, frac_times, frac_10s])))
            _frac.append(frac)

    while True :
        otherFracTuple = makeRandomFraction(repeat='yes', repeatMax=12, irreducible='no')
        otherFrac = Fraction(*otherFracTuple)

        if otherFrac.denominator != otherFracTuple[1] :
            break

    otherFrac_initial = makeFractionFormula(*otherFracTuple)
    otherFrac_irr = makeFractionFormula(otherFrac.numerator, otherFrac.denominator)

    # 분자와 분모의 소인수분해된 식을 구합니다.
    numeratorFactored = getFactoredIntFormula(otherFrac.numerator)
    denomFactored = getFactoredIntFormula(otherFrac.denominator)

    otherFrac_factored = makeFractionFormula(numeratorFactored, denomFactored)
    finalOther = (otherFrac_initial, " = ".join([otherFrac_initial, otherFrac_irr, otherFrac_factored]))

    answerInd = random.choice(range(5))

    fractions.insert(answerInd, finalOther)


    stem = stem.format(frac1 = aT(fractions[0][0]), frac2 = aT(fractions[1][0]), frac3 = aT(fractions[2][0]),
                       frac4= aT(fractions[3][0]), frac5=aT(fractions[4][0]))
    answer = answer.format(a1=answer_dict[answerInd])
    comment = comment.format(c1=answer_dict[0] + " " + aT(fractions[0][1]), c2=answer_dict[1] + " " + aT(fractions[1][1]),
                             c3=answer_dict[2] + " " + aT(fractions[2][1]), c4=answer_dict[3] + " " + aT(fractions[3][1]),
                             c5=answer_dict[4] + " " + aT(fractions[4][1]))

    return stem, answer, comment


def rationalandprime211_Stem_013():
    stem = "분수 {frac}{postp} {frac2}의 꼴로 고쳐 유한소수로 나타낼 때, 두 자연수 {A}, {n}에 대하여 {formula}의 최솟값을 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "{fracConvert}\n따라서 {formula}의 값 중 가장 작은 수는 {calc}\n\n"

    # 문제 생성에 사용할 숫자들을 생성합니다.
    twos = ["", "2", "2^2", "2^3"]
    fives = ["", "5", "5^2"]

    while True:
        two_up = random.choice(range(4))
        five_up = random.choice(range(3))

        if two_up != five_up:
            break

    bigger_up = max(two_up, five_up)
    b = 10 ** bigger_up
    bigger_up = str(bigger_up)

    initialDenominator = 2 ** two_up * 5 ** five_up
    a = int(b / initialDenominator)

    numerators = [3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29]

    if two_up:
        if not five_up:
            numerators.extend([5, 10, 15])
    else:
        if five_up:
            numerators.extend([2, 4, 6, 8, 12, 14])

    numerator = random.choice(numerators)

    # 식을 만듭니다.
    if two_up:
        if five_up:
            denom = twos[two_up] + " times " + fives[five_up]
        else:
            denom = twos[two_up]
    else:
        if five_up:
            denom = fives[five_up]

    frac = makeFractionFormula(numerator, initialDenominator)
    frac_factorized = makeFractionFormula(numerator, denom)
    frac_times = makeFractionFormula(" ".join([str(numerator), 'times', str(a)]),
                                     " ".join([denom, "times", str(a)]))
    frac_10s = makeFractionFormula(numerator * a, "10^" + bigger_up)
    frac_10ss = makeFractionFormula(numerator * a * 10, "10^" + str(int(bigger_up)+1))

    A = numerator * a
    n = bigger_up

    coeff_n = random.choice(range(11, 30))
    formula = aT("A-" + str(coeff_n) + "n")
    ans = A - int(n) * coeff_n

    frac2 = aT("A over 10^n")

    # 내용을 채웁니다.
    stem = stem.format(frac=addTag(frac), postp=proc_jo(numerator, 1), frac2=frac2, A=aT("A"), n=aT("n"), formula=formula)
    answer = answer.format(a1=aT(ans))
    comment = comment.format(fracConvert=aT(" `=` ".join([frac, frac_factorized, frac_times, frac_10s, frac_10ss, 'cdots'])),
                             formula=formula, calc=aT(ans))
    return stem, answer, comment


def rationalandprime211_Stem_014():
    stem = "다음 보기의 분수 중 유한소수로 나타낼 수 없는 것을 모두 고르시오.\nㄱ. {frac1}     ㄴ. {frac2}     ㄷ. {frac3}\nㄹ. {frac4}     ㅁ. {frac5}     ㅂ. {frac6}\n"
    answer = "(답): {ans}\n"
    comment = "(해설)\n{commentText}\n따라서, 유한소수로 나타낼 수 없는 것은 {ans}이다.\n\n"

    answerList = [0, 0, 0, 1, 1, 1]
    random.shuffle(answerList)
    fractions = []
    _fracs = []
    for ans in answerList :
        while True:
            if ans : #repeat
                initial = makeRandomFraction(repeat="yes", repeatMax=10, irreducible='no')
            else :
                initial = makeRandomFraction(repeat='no', irreducible='no')

            irreducible = Fraction(*initial)
            irreducible = (irreducible.numerator, irreducible.denominator)
            if irreducible not in _fracs :
                break

        if random.choice(range(2)): # 0 -> unfactorized / 1 -> factorized
            fracChoice = makeFactoredFractionFormula(initial)
            fracFactored = True
        else :
            fracChoice = makeFractionFormula(*initial)
            fracFactored = False

        fractions.append((initial, fracFactored, fracChoice))
        _fracs.append(irreducible)

    # print(fractions)
    # print(_fracs)

    commentList = []
    for ind, f_tuple in enumerate(fractions):
        # print(f_tuple, _fracs[ind])
        if f_tuple[0] == _fracs[ind]: #애초에 기약분수였던 경우
            if f_tuple[1] : #사용할 식이 이미 인수분해된 경우
                pass # 해설 없음
            else : # 기약분수였지만 인수분해는 안 되었던 경우
                factored = makeFactoredFractionFormula(f_tuple[0])
                c = "`=`".join([f_tuple[2], factored])
                # print(c)
                commentList.append((ind, c))
        else : #기약분수가 아닌 경우
            if f_tuple[1] : #식은 인수분해된 경우
                factored = makeFactoredFractionFormula(_fracs[ind])
                c = '`=`'.join([f_tuple[2], factored])
                # print(c)
                commentList.append((ind, c))
            else : #식이 인수분해가 안 되었던 경우
                initialFactored = makeFactoredFractionFormula(f_tuple[0])
                simplifiedFactored = makeFactoredFractionFormula(_fracs[ind])
                c = '`=`'.join([f_tuple[2], initialFactored, simplifiedFactored])
                # print(c)
                commentList.append((ind, c))

    answerChoices = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ']

    answerValue = []
    for ind, ans in enumerate(answerList) :
        if ans :
            answerValue.append(answerChoices[ind])

    answerText = ", ".join(answerValue)

    commentText = "\n".join([answerChoices[item[0]] + ". " + aT(item[1]) for item in commentList])

    # 내용을 채웁니다.

    stem = stem.format(frac1 = aT(fractions[0][2]), frac2 = aT(fractions[1][2]), frac3 = aT(fractions[2][2]),
                       frac4= aT(fractions[3][2]), frac5=aT(fractions[4][2]), frac6=aT(fractions[5][2]))
    answer = answer.format(ans=answerText)
    comment = comment.format(commentText=commentText, ans=answerText)

    return stem, answer, comment


def rationalandprime211_Stem_015():
    stem = "두 분수 {frac1}과 {frac2} 사이에 있는 분모가 {denom}인 분수 중에서 유한소수로 나타낼 수 있는 것의 개수를 구하면? (단, 분자는 자연수이다.)\n① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n주어진 조건을 만족시키는 분수를 {frac_comment}라 할 때, {denom_formula}이고, {frac1_formula}, {frac2_formula}이므로 {a}는 {multi}의 배수이어야 한다.\n" \
              "이 때, {frac1_numerator}{postp} {frac2_numerator} 사이에 있는 {multi}의 배수는 {multiList}이다. 따라서 구하는 개수는 {ans}개이다.\n\n"

    # 문제에 사용할 분모를 정합니다.
    primes = [3, 7, 9, 11, 13, 17]
    multi = random.choice(primes)

    frac2 = random.choice([(3, 5), (4, 5), (7, 10), (9, 10)])
    frac1 = (1, multi*2)

    denom = multi * 10
    denom_formula = "".join([str(denom)," = ", " times ".join( map (str, sorted ( [2, 5, multi] ) ) ) ] )

    # 정답을 구합니다.
    smallest = 5
    largest = frac2[0] * 2 * multi
    if frac2[1] == 10 :
        largest = int(largest/2)

    _s = (smallest//multi) + 1
    _l = largest // multi
    if largest / multi == _l :
        _l -= 1

    ans = _l - _s + 1

    while True :
        answerMinus = random.choice(range(5))
        if ans <= answerMinus :
            continue
        else :
            ansNums = [str(x)+"개" for x in range(ans-answerMinus, ans-answerMinus+5)]
            ansIndex = answerMinus
            break


    multipleList = range(multi*_s, multi*_l + 1, multi)

    frac1_multi = (smallest, denom)
    frac2_multi = (largest, denom)

    equalities = makeEquality([makeFractionFormula(*frac1), makeFractionFormula(*frac2)], [makeFractionFormula(*frac1_multi), makeFractionFormula(*frac2_multi)], withTag=True)

    # 내용을 채워 넣습니다.

    stem = stem.format(frac1=aT(makeFractionFormula(*frac1)), frac2=aT(makeFractionFormula(*frac2)), denom=str(denom),
                       n1=ansNums[0], n2=ansNums[1], n3=ansNums[2], n4=ansNums[3], n5=ansNums[4])
    answer = answer.format(a1=answer_dict[ansIndex])
    comment = comment.format(frac_comment=makeFractionFormula(*("a", 2*5*multi), withTag=True), denom_formula=aT(denom_formula),
                             frac1_formula=equalities[0], frac2_formula=equalities[1], a=aT("a"), multi=aT(str(multi)),
                             frac1_numerator=aT(smallest), postp=proc_jo(smallest%10, 2), frac2_numerator=aT(largest),
                             multiList=", ".join([aT(x) for x in multipleList]), ans=aT(ans))

    return stem, answer, comment


def rationalandprime211_Stem_016():
    stem = "분수 {frac}를 소수로 나타내면 유한소수가 될 때, {a}의 값이 될 수 있는 가장 {optionText} 자연수를 구하면?\n① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{frac_comment}에서 {a}가 {multi}의 배수가 되면 주어진 분수는 약분이 되어 유한소수로 나타낼 수 있다.\n" \
              "따라서, {a}의 값이 될 수 있는 가장 {optionText} 자연수는 {ansFormula}.\n\n"

    # 문제에 사용할 분모를 정합니다.
    denom1 = random.choice([2, 4, 5])
    denom2 = random.choice([3, 9])
    denom3 = random.choice([7, 11, 13])

    possibleNumerator1 = [3, denom3]
    if denom1 == 4 :
        possibleNumerator1.append(2)

    numerator1 = random.choice(possibleNumerator1)

    denominator = denom1 * denom2 * denom3
    denominatorFormula = getFactoredIntFormula(denominator)
    simplifedFraction = Fraction(numerator1, denominator)
    denom_simpliedFormula = getFactoredIntFormula(simplifedFraction.denominator)

    if simplifedFraction.denominator % 4 == 0 :
        multi = int(simplifedFraction.denominator / 4)
    elif simplifedFraction.denominator % 2 == 0 :
        multi = int(simplifedFraction.denominator / 2)
    else :
        multi = int(simplifedFraction.denominator / 5)

    if (100 % multi) < 5 or (multi > 95) :
        biggest = False
    else :
        biggest = random.choice([True, False])

    if biggest :
        optionText = "큰 두 자리의"
        ansValue = 100 - 100 % multi
        ansFormula = "".join(map(str, [multi, " times ", ansValue // multi, " = ", ansValue]))
    else :
        optionText = "작은"
        ansValue = multi
        ansFormula = ansValue

    while True :
        answerMinus = random.choice(range(5))
        if (ansValue <= answerMinus) or (biggest and ((ansValue - answerMinus + 4) > 100)):
            print(multi, ansValue, answerMinus)
            continue
        else :
            ansNums = [str(x) for x in range(ansValue-answerMinus, ansValue-answerMinus+5)]
            ansIndex = answerMinus
            break

    fractionFormula = makeFractionFormula(str(numerator1)+" times a", str(denominator))
    frac_comment1 = makeFractionFormula(str(numerator1)+" times a", denominatorFormula)
    frac_comment2 = makeFractionFormula("a", denom_simpliedFormula)

    frac_comment = " = ".join([fractionFormula, frac_comment1, frac_comment2])

    # 내용을 채워 넣습니다.

    stem = stem.format(frac=aT(fractionFormula), a=aT("a"), optionText=optionText,
                       n1=ansNums[0], n2=ansNums[1], n3=ansNums[2], n4=ansNums[3], n5=ansNums[4])
    answer = answer.format(a1=answer_dict[ansIndex])
    comment = comment.format(frac_comment=aT(frac_comment), a=aT("a"), multi=aT(multi), optionText=optionText, ansFormula=aT(ansFormula))

    return stem, answer, comment


def rationalandprime211_Stem_017():
    stem = "분수 {frac}을 소수로 나타내면 유한소수가 될 때, {number} {optionText}의 자연수 {n}의 개수를 구하면?\n① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{frac_comment}이므로 {frac}이 유한소수로 나타내어지려면 {n}은 {multi}의 배수이어야 한다.\n" \
              "따라서, {number} {optionText}의 자연수 중 {n}이 될 수 있는 것은 {multiples}의 {ans}개이다.\n\n"

    # 문제에 사용할 분모를 정합니다.
    denom1 = random.choice([2, 4, 5, 10])
    multi = random.choice(list(primerange(6, 40)))
    denominator = denom1 * multi

    fracTuple = ("n", denominator)
    frac = makeFractionFormula(*fracTuple)
    frac_factorized = makeFactoredFractionFormula(fracTuple)

    included = random.choice([True, False])
    if included :
        optionText = "이하"
        ansValue = denom1
    else :
        optionText = "미만"
        ansValue = denom1-1
    multiples = ", ".join([aT(x) for x in range(multi, multi * ansValue + 1, multi)])

    while True :
        answerMinus = random.choice(range(5))
        if (ansValue <= answerMinus) or ((ansValue - answerMinus + 4) > 100):
            continue
        else :
            ansNums = [str(x) for x in range(ansValue-answerMinus, ansValue-answerMinus+5)]
            ansIndex = answerMinus
            break

    frac_comment = " = ".join([frac, frac_factorized])

    # 내용을 채워 넣습니다.

    stem = stem.format(frac=aT(frac), number=aT(denominator), optionText=optionText, n=aT("n"),
                       n1=ansNums[0], n2=ansNums[1], n3=ansNums[2], n4=ansNums[3], n5=ansNums[4])
    answer = answer.format(a1=answer_dict[ansIndex])
    comment = comment.format(frac_comment=aT(frac_comment), frac=aT(frac), n=aT("n"), multi=aT(multi),
                             number=aT(denominator), optionText=optionText, multiples=multiples, ans=aT(ansValue))

    return stem, answer, comment


def rationalandprime211_Stem_018():
    stem = "두 분수 {frac1}, {frac2}에 어떤 자연수 {n}을 곱하면 두 수 모두 유한소수로 나타낼 수 있다고 한다. 자연수 {n}의 값이 될 수 있는 가장 작은 수는?\n① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{frac1_comment}, {frac2_comment}이므로 두 분수가 모두 유한소수로 나타내어지기 위해 곱해야 하는 자연수 {n}은 {multiFormula}의 배수이어야 한다.\n" \
              "따라서, {n}의 값이 될 수 있는 가장 작은 자연수는 {ansFormula}.\n\n"

    # 문제에 사용할 분수를 생성합니다.


    while True :
        frac1 = makeRandomFraction(repeat='yes', repeatMax=100)
        frac2 = makeRandomFraction(repeat='yes', repeatMax=100)
        if frac1[1] > 35 and isprime(frac1[1]) :
            continue
        elif frac2[1] > 35 and isprime(frac2[1]) :
            continue
        else :
            break

    frac1Formula = makeFractionFormula(*frac1)
    frac2Formula = makeFractionFormula(*frac2)

    frac1Factored = makeFactoredFractionFormula(frac1)
    frac2Factored = makeFactoredFractionFormula(frac2)

    frac1DenomFactored = factorint(int(frac1[1]))
    frac2DenomFactored = factorint(int(frac2[1]))

    multiFactored = {}
    for factored in [frac1DenomFactored, frac2DenomFactored]:
        for k in factored :
            if k != 2 and k != 5 :
                if k in multiFactored :
                    if multiFactored[k] < factored[k] :
                        multiFactored[k] = factored[k]
                else :
                    multiFactored[k] = factored[k]

    multi = 1
    for p, q in multiFactored.items() :
        multi *= p ** q

    ansValue = multi


    while True :
        answerMinus = random.choice(range(5))
        if (ansValue <= answerMinus):
            continue
        else :
            ansNums = [aT(x) for x in range(ansValue-answerMinus, ansValue-answerMinus+5)]
            ansIndex = answerMinus
            break

    multiFormula = getFactoredIntFormula(multi, withTag=True)
    ansFormula = getFactoredIntFormula(multi, equalityEnd=True, withTag=True)

    equalities = makeEquality([frac1Formula, frac2Formula], [frac1Factored, frac2Factored], withTag=True)

    # 내용을 채워 넣습니다.

    stem = stem.format(frac1=aT(frac1Formula), frac2=aT(frac2Formula), n=aT("n"),
                       n1=ansNums[0], n2=ansNums[1], n3=ansNums[2], n4=ansNums[3], n5=ansNums[4])
    answer = answer.format(a1=answer_dict[ansIndex])
    comment = comment.format(frac1_comment=equalities[0], frac2_comment=equalities[1], n=aT("n"), multiFormula=multiFormula,
                             ansFormula=ansFormula)

    return stem, answer, comment


def rationalandprime211_Stem_019():
    stem = "{fracX}를 유한소수로 나타낼 수 있다고 한다. 자연수 {x}의 값이 될 수 있는 가장 작은 수는?\n① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{frac_comment}이므로 자연수 {x}는 {multi}의 배수이어야 한다. 따라서 {x}의 값은 {ans}이다.\n\n"

    # 문제에 사용할 분수를 생성합니다.
    while True :
        frac = makeRandomFraction(repeat='yes', repeatMax=100, maxDigit={'numerator': (2, [0.5, 0.5]), 'denominator': (2, [0, 1])})
        if frac[1] > 35 and isprime(frac[1]) or ((frac[1]%2) and (frac[1]%5)) :
            continue
        else :
            break

    fracFormula = makeFractionFormula(*frac)
    fracX = " times ".join([fracFormula, "x"])

    fracFactored = makeFactoredFractionFormula(frac)

    fracDenomFactored = factorint(int(frac[1]))

    multi = 1

    for k in fracDenomFactored :
        if k != 2 and k != 5 :
            multi *= k ** fracDenomFactored[k]

    ansValue = multi


    while True :
        answerMinus = random.choice(range(5))
        if (ansValue <= answerMinus):
            continue
        else :
            ansNums = [aT(x) for x in range(ansValue-answerMinus, ansValue-answerMinus+5)]
            ansIndex = answerMinus
            break

    equalities = makeEquality([fracFormula], [fracFactored], withTag=True)
    x=aT("x")
    # 내용을 채워 넣습니다.

    stem = stem.format(fracX=aT(fracX), x=x,
                       n1=ansNums[0], n2=ansNums[1], n3=ansNums[2], n4=ansNums[3], n5=ansNums[4])
    answer = answer.format(a1=answer_dict[ansIndex])
    comment = comment.format(frac_comment=equalities[0], x=x, multi=aT(multi), ans=aT(ansValue))

    return stem, answer, comment


def rationalandprime211_Stem_020():
    stem = "분수 {fracX}{postp} 유한소수로 나타낼 수 있다고 한다. {x}가 {x_range}인 자연수일 때, 모든 {x}의 값의 합을 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{frac_comment}{postp} 유한소수로 나타내어지도록 하는 {x_range}인 자연수 {x}는 {x_values}이다.\n따라서 모든 {x}의 값은 {ansFormula}이다.\n\n"

    # 문제 생성에 사용할 숫자들을 생성합니다.
    two_up = random.choice(range(1, 4))
    five_up = random.choice(range(1, 4))
    while True:
        numerator = random.choice(range(10, 100))
        if numerator%2 and numerator%5 :
            continue
        break
    x_start = random.choice(range(10, 51, 5))

    initialDenominator = 2 ** two_up * 5 ** five_up
    frac_reduced = Fraction(numerator, initialDenominator)

    answerList = []
    for tempValue in range(x_start, x_start+10) :
        decimal = fractionToDecimalTuple(frac_reduced.numerator, frac_reduced.denominator*tempValue)
        if not decimal[1] :
            answerList.append(tempValue)

    ansValue = sum(answerList)
    ansSumFormula = " + ".join(map(str, answerList)) + " = " + str(ansValue)

    initialDenominatorFactored = getFactoredIntFormula(initialDenominator)
    reducedDenominatorFactored = getFactoredIntFormula(frac_reduced.denominator)

    fracX_denom = " times ".join([initialDenominatorFactored, "x"])
    fracX = makeFractionFormula(numerator, fracX_denom)
    fracX_reduced_denom = " times ".join([reducedDenominatorFactored, "x"])
    fracX_reduced = makeFractionFormula(frac_reduced.numerator, fracX_reduced_denom)

    equality = makeEquality([fracX], [fracX_reduced], withTag=True)[0]

    x_range = "".join([str(x_start), "≤", " x ", "＜", str(x_start+10)])

    x = aT("x")

    # 내용을 채워 넣습니다.

    stem = stem.format(fracX=aT(fracX), postp=proc_jo(numerator%10, 1), x=x, x_range=aT(x_range))
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(frac_comment=equality, postp=proc_jo(frac_reduced.denominator%10), x_range=aT(x_range),
                             x=x, x_values=", ".join([aT(x) for x in answerList]), ansFormula=aT(ansSumFormula))

    return stem, answer, comment


def rationalandprime211_Stem_021():
    stem = "분수 {fracX}를 소수로 나타내면 유한소수가 되고, 기약분수로 나타내면 {fracX_reduced}{postp} 된다. {x}가 {x_range}인 자연수일 때, {question}의 값은?\n" \
           "① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{fracX}를 기약분수로 나타냈을 때 {fracX_reduced}이므로 {x}는 {numerator_reduced}의 배수이어야 한다.\n" \
              "{denomFactored}이고 {x_range}이므로 {x}는 {x_values}이다. 이 때, {possibleFracFormula}이므로 {x_eq}, {y_eq}\n" \
              "{ansFormula}\n\n"

    # 문제 생성에 사용할 분수를 생성합니다.
    frac = makeRandomFraction(repeat='no', maxDigit={'numerator': (2, [0.5, 0.5]), 'denominator': (3, [0, 0.7, 0.3])})
    y = frac[1]
    commonNum = random.choice(range(2, 8))
    x = frac[0] * commonNum
    initialDenom = y * commonNum

    x_start = (x // 10) * 10
    x_end = x_start + 10

    reduced_numerator = frac[0]
    if x_start % reduced_numerator :
        temp1 = ((x_start // reduced_numerator) + 1) * reduced_numerator
    else :
        temp1 = x_start

    if not temp1:
        temp1 += reduced_numerator

    temp2 = (x_end // reduced_numerator) * reduced_numerator + 1

    possibleNums = range(temp1, temp2, frac[0])
    possibleFracList1 = []
    possibleFracList2 = []

    for n in possibleNums :
        possibleFracList1.append((n, initialDenom))
        possibleFracList2.append(Fraction(n, initialDenom))

    possibleFracList1 = list(map(lambda x : makeFractionFormula(*x), possibleFracList1))
    possibleFracList2 = list(map(lambda x : makeFractionFormula(x.numerator, x.denominator), possibleFracList2))

    equalities = makeEquality(possibleFracList1, possibleFracList2, withTag=True)

    initialDenomFactored = getFactoredIntFormula(initialDenom, equalityFront=True, withTag=True)


    # a와 b에 붙을 계수를 구합니다.
    coeff_x = random.choice(range(1, 4))
    coeff_y = random.choice(range(-2, 0))

    # 정답을 구합니다.
    ansValue = coeff_x * x + coeff_y * y

    # 한글 수식에서 계수가 1이거나 -1인 경우를 조정합니다.
    if coeff_x == 1:
        _coeff_x = ""
    else:
        _coeff_x = coeff_x

    if coeff_y == -1:
        _coeff_y = "-"
    else:
        _coeff_y = coeff_y

    question = "".join([str(x) for x in [_coeff_x, 'x', '`', _coeff_y, 'y']])
    answerFormula = " ".join(['therefore~', question, "=", str(ansValue)])


    answerMinus = random.choice(range(5))

    ansNums = [aT(x) for x in range(ansValue-answerMinus, ansValue-answerMinus+5)]
    ansIndex = answerMinus

    x_range = "".join([str(x_start), "≤", " x ", "＜", str(x_start+10)])

    x_text = aT("x")
    y_text = aT("y")

    xy_eqs = makeEquality(['x', 'y'], [x, y], withTag=True)

    fracX = makeFractionFormula("x", initialDenom, withTag=True)
    fracX_reduced = makeFractionFormula(frac[0], "y", withTag=True)


    # 내용을 채워 넣습니다.

    stem = stem.format(fracX=fracX, fracX_reduced=fracX_reduced, postp=proc_jo(frac[0]%10), x=x_text, x_range=aT(x_range), question=aT(question),
                       n1=ansNums[0], n2=ansNums[1], n3=ansNums[2], n4=ansNums[3], n5=ansNums[4])
    answer = answer.format(a1=answer_dict[ansIndex])
    comment = comment.format(fracX=fracX, fracX_reduced=fracX_reduced, x=x_text, numerator_reduced=aT(frac[0]),
                             denomFactored = initialDenomFactored, x_range=aT(x_range), x_values=", ".join([aT(x) for x in possibleNums]),
                             possibleFracFormula=", ".join(equalities), x_eq=xy_eqs[0], y_eq=xy_eqs[1],
                             ansFormula = aT(answerFormula))

    return stem, answer, comment


def rationalandprime211_Stem_022():
    stem = "분수 {fracX}를 기약분수로 나타내면 {fracX_reduced}이고, 소수로 나타내면 유한소수가 된다. 이 때, {question}의 값은?\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{fracX}를 기약분수로 나타냈을 때 {fracX_reduced}이므로 {x}는 {numerator_reduced}의 배수이어야 한다.\n" \
              "또 {denomFactored}이므로 {x}는 {commonNum}의 배수이어야 한다.\n{x_eq}, {frac_comment}이므로 {y_eq}\n" \
              "{ansFormula}\n\n"

    # 문제 생성에 사용할 분수를 생성합니다.
    commonNum = random.choice([3, 7, 11, 13])

    while True :
        frac = makeRandomFraction(repeat='no', maxDigit={'numerator': (2, [0.5, 0.5]), 'denominator': (3, [0.2, 0.7, 0.1])})
        if frac[0] != 1 and frac[0]%commonNum:
            break

    y = frac[1]
    x = frac[0] * commonNum
    initialDenom = y * commonNum

    frac_comment = makeEquality([makeFractionFormula(x, initialDenom)], [makeFractionFormula(*frac)], withTag=True)[0]

    initialDenomFactored = getFactoredIntFormula(initialDenom, equalityFront=True, withTag=True)

    # a와 b에 붙을 계수를 구합니다.
    coeff_x = random.choice(range(1, 4))
    coeff_y = random.choice(range(-2, 0))

    # 정답을 구합니다.
    ansValue = coeff_x * x + coeff_y * y

    # 한글 수식에서 계수가 1이거나 -1인 경우를 조정합니다.
    if coeff_x == 1:
        _coeff_x = ""
    else:
        _coeff_x = coeff_x

    if coeff_y == -1:
        _coeff_y = "-"
    else:
        _coeff_y = coeff_y

    question = "".join([str(x) for x in [_coeff_x, 'x', '`', _coeff_y, 'y']])
    answerFormula = " ".join(['therefore~', question, "=", str(ansValue)])

    x_text = aT("x")
    y_text = aT("y")

    xy_eqs = makeEquality(['x', 'y'], [x, y])
    xy_eqs[0] = "therefore~" + xy_eqs[0]

    fracX = makeFractionFormula("x", initialDenom, withTag=True)
    fracX_reduced = makeFractionFormula(frac[0], "y", withTag=True)

    # 내용을 채워 넣습니다.

    stem = stem.format(fracX=fracX, fracX_reduced=fracX_reduced, question=aT(question))
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(fracX=fracX, fracX_reduced=fracX_reduced, x=x_text, numerator_reduced=aT(frac[0]),
                             denomFactored = initialDenomFactored, commonNum=aT(commonNum),
                             x_eq=aT(xy_eqs[0]), frac_comment=frac_comment, y_eq=aT(xy_eqs[1]), ansFormula = aT(answerFormula))

    return stem, answer, comment


def rationalandprime211_Stem_023():
    stem = "분수 {fracA}{postp} 유한소수로 나타낼 수 {optionText}을 때, 다음 중 자연수 {a}의 값으로 적절한 것은?\n① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}\n따라서 유한소수로 나타낼 수 {optionText}는 것은 {ans}이다.\n\n"

    # 문제의 조건을 정합니다.
    isNonrepeat = random.choice([True, False])
    while True :
        numerator = random.choice(range(10, 100))
        factored = factorint(numerator)
        if len(factored) == 1 or (2 in factored) or (5 in factored):
            continue
        else :
            break

    factorKeys = list(factored.keys())
    otherNums = []
    avoided = factorKeys + [2, 5]

    if isNonrepeat : #유한소수로 나타낼 수 있는 경우가 정답
        optionText = "있"
        ansValue = random.choice(factorKeys) * random.choice([2, 5])

        while len(otherNums) < 2 :
            temp = randprime(1, 20)
            divideCheck = 0
            for k in avoided :
                if temp % k :
                    divideCheck += 1
            if divideCheck == len(avoided) :
                otherNums.append(temp)
        _otherNums = [random.choice([2, 5])*x for x in otherNums]
        otherNums.extend(_otherNums)
        # print(isNonrepeat, otherNums)
    else : #유한소수로 나타낼 수 없는 경우가 정답
        optionText = "없"
        otherNums = []
        while len(otherNums) < 4 :
            temp = random.choice(factorKeys) * random.choice([1, 2, 5])
            if temp not in otherNums :
                otherNums.append(temp)
        # print(isNonrepeat, otherNums)
        while True :
            temp = randprime(1, 20)
            if temp not in avoided :
                ansValue = temp
                break

    otherNums.append(ansValue)
    otherNums.sort()
    # print(isNonrepeat, otherNums)
    answerInd = otherNums.index(ansValue)
    ansNums = otherNums


    two_up = random.choice(range(1, 4))
    five_up = random.choice(range(1, 3))
    denominator = 2 ** two_up * 5 ** five_up

    denominator_factored = getFactoredIntFormula(denominator)

    fracA = makeFractionFormula(numerator, denominator_factored + ' times a', withTag=True)
    fracFilled = []
    for n in ansNums:
        fracTemp = makeFractionFormula(numerator, denominator_factored + ' times ' + str(n))
        fracSimpled = Fraction(numerator, denominator*n)
        if fracSimpled.numerator == numerator :
            temp = fracTemp
        else :
            fracSimpled = makeFractionFormula(fracSimpled.numerator, getFactoredIntFormula(fracSimpled.denominator))
            temp = fracTemp + "`=`" + fracSimpled
        fracFilled.append(temp)

    fracFilled = list(map(aT, fracFilled))

    # 내용을 채워 넣습니다.

    stem = stem.format(fracA=fracA, postp=proc_jo(numerator%10, 1), a=aT("a"), optionText=optionText,
                       n1=ansNums[0], n2=ansNums[1], n3=ansNums[2], n4=ansNums[3], n5=ansNums[4])
    answer = answer.format(a1=answer_dict[answerInd])
    comment = comment.format(c1=fracFilled[0], c2=fracFilled[1], c3=fracFilled[2], c4=fracFilled[3], c5=fracFilled[4],
                             optionText=optionText, ans=answer_dict[answerInd])

    return stem, answer, comment


def rationalandprime211_Stem_024():
    stem = "다음 조건을 모두 만족시키는 {x}의 개수를 구하시오.\n㈎ {x}는 {n_bottom} 이상 {n_top} 이하의 자연수이다.\n㈏ {fracX}{postp} 유한소수로 나타내어진다.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{i1} {largeN}의 분모의 소인수가 2 또는 5뿐일 때, {x}는 {x_2and5Possibles}의 {x_2and5Num}개\n" \
              "{i2} {largeN}의 분모의 소인수에 {otherFactor}{postp} 포함될 때, {x}는 {x_otherPossibles}의 {x_otherNum}개\n" \
              "따라서 {x}의 개수는 {ans}이다.\n\n"

    # 문제에 필요한 숫자들을 생성합니다.
    n_bottom = random.choice([1, 10, 20, 30])
    n_top = random.choice([60, 70, 80, 90, 100])

    numerator = random.choice([3, 6, 12, 7, 14, 28, 11, 22])
    if numerator % 3 == 0 :
        otherFactor = 3
    elif numerator % 7 == 0 :
        otherFactor = 7
    else :
        otherFactor = 11

    x_2and5s = []
    x_others = []

    twoAndFive = [2, 5]
    tFandOther = [2, 5, otherFactor]

    for i in range(n_bottom, n_top+1):
        if i == 1 :
            x_2and5s.append(i)
        else :
            factored = factorint(i)
            factors = factored.keys()

            check = sum([k in twoAndFive for k in factors])
            if check == len(factors) :
                x_2and5s.append(i)
                continue

            check = sum([k in tFandOther for k in factors])
            if check == len(factored) and factored[otherFactor]==1:
                x_others.append(i)

    x_2and5Num = len(x_2and5s)
    x_otherNum = len(x_others)
    ans = x_2and5Num + x_otherNum

    x_2and5Possibles = [getFactoredIntFormula(i, withTag=True) for i in x_2and5s]
    x_otherPossibles = [getFactoredIntFormula(i, withTag=True) for i in x_others]

    two_up = random.choice(range(1, 3))
    five_up = random.choice(range(1, 3))
    denominator = 2 ** two_up * 5 ** five_up

    denominator_factored = getFactoredIntFormula(denominator)

    fracX = makeFractionFormula(numerator, denominator_factored + ' times x')
    fracX = aT("N = " + fracX)

    x = aT('x')

    # 내용을 채워 넣습니다.

    stem = stem.format(x=x, n_bottom=aT(n_bottom), n_top=aT(n_top), fracX=aT(fracX), postp=proc_jo(numerator%10, -1))
    answer = answer.format(a1=aT(ans))
    comment = comment.format(i1=aT("(i)"), largeN=aT("N"), x=x, x_2and5Possibles=", ".join(x_2and5Possibles),
                             x_2and5Num=aT(x_2and5Num), i2=aT("(ii)"), otherFactor=aT(otherFactor), postp=proc_jo(otherFactor%10),
                             x_otherPossibles=", ".join(x_otherPossibles), x_otherNum=aT(x_otherNum), ans=aT(ans))

    return stem, answer, comment


def rationalandprime211_Stem_025():
    stem = "분수 {fracA}를 소수로 나타내면 유한소수가 되고, 이 분수를 기약분수로 나타내면 {fracBC}가 된다. " \
           "이를 만족시키는 세 자연수 {abcSeparate}에 대하여 {abcFormula}의 {optionText}을 구하시오. (단, {valueRange})\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n분수 {fracAFormula}가 유한소수가 되려면 {a}는 {aValue}의 배수이어야 한다. 이 때, {valueRange}이므로 {a}로 가능한 값은 {aPossibles}이다.\n" \
              "{possibleProcedures}\n\n"

    # 문제 생성에 사용할 분수를 생성합니다.
    aValue = random.choice([3, 9, 7, 11, 13])

    denominator = aValue * twoFiveDenom(twoRange=(1, 4), fiveRange=(1, 3))[0]
    denominator_factored = getFactoredIntFormula(denominator)

    fracA = makeFractionFormula("a", denominator)
    fracAFactored = makeFractionFormula("a", denominator_factored)
    fracAFormula = makeEquality([fracA], [fracAFactored], withTag=True)[0]

    a_start = random.choice(range(10, 40, 10))
    a_range = ceil(aValue*2*.1) * 10
    a_end = a_start + a_range

    valueRange = "".join([str(a_start), "`＜`", " a ", "`＜`", str(a_end)])

    possibleAs = multipleUnderRange(aValue, a_start+1, a_end)
    givenChars= ['a', 'b', 'c']
    # print(possibleAs)

    abc = getRandomEquation(givenChars=givenChars, coefficientRange=[(-1, 2) for i in range(3)],
                            realValues=[1, 1, 1], avoidZero=True)
    abcFormula = abc['text']
    abcCoeffs = abc['coeffs']

    fracBC = makeFractionFormula("b", "c", withTag=True)

    commentList = []
    partialComment = "{numFormula} {aFormula}이면 {fracFormula}이므로 {bFormula}, {cFormula}, {ansFormula}\n"
    # tempLeft = ['a', 'b', 'c', abcFormula]
    iText = "i"
    possibleAnswers = []
    for pA in possibleAs :
        tempLeft = ['a', 'b', 'c', abcFormula]
        tempRight = [pA]

        tempFrac = makeFractionFormula(pA, denominator)
        tempFracReduced = Fraction(pA, denominator)
        b = tempFracReduced.numerator
        c = tempFracReduced.denominator
        tempFracReducedFormula = makeFractionFormula(b, c)
        charValues = [pA, b, c]
        tempAns = sum([reduce(mul, item) for item in zip(abcCoeffs, charValues)])
        possibleAnswers.append(tempAns)

        tempLeft.insert(1, tempFrac)
        tempRight.append(tempFracReducedFormula)
        tempRight.append(b)
        tempRight.append(c)
        tempRight.append(tempAns)

        tempEqualities = makeEquality(tempLeft, tempRight)
        tempCommentPart = partialComment.format(numFormula=aT("".join(["( ", iText, " )"])), aFormula=aT(tempEqualities[0]), fracFormula=aT(tempEqualities[1]),
                                                bFormula=aT(tempEqualities[2]), cFormula=aT(tempEqualities[3]),
                                                ansFormula=aT("therefore~"+tempEqualities[4]))
        commentList.append(tempCommentPart)
        iText += "i"

    isBiggest = random.choice([True, False])
    # print(possibleAnswers)
    if isBiggest :
        optionText = "최댓값"
        ansValue = max(possibleAnswers)
    else :
        optionText = "최솟값"
        ansValue = min(possibleAnswers)

    # aPossibles = addTag(possibleAs)

    # 내용을 채웁니다.
    stem = stem.format(fracA=aT(fracA), fracBC=fracBC, abcSeparate=", ".join([aT(x) for x in givenChars]),
                       abcFormula=aT(abcFormula), optionText=optionText, valueRange=aT(valueRange))
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(fracAFormula=fracAFormula, a=aT("a"), aValue=aT(aValue), valueRange=aT(valueRange),
                             aPossibles=", ".join(addTag(possibleAs)), possibleProcedures="".join(commentList))

    return stem, answer, comment


def rationalandprime211_Stem_026():
    stem = "분수 {fracAB}를 유한소수로 나타낼 수 {optionText}도록 하는 자연수 {a}, {b}의 순서쌍 {pairFormula}의 개수는? (단, {a_range}, {b_range})\n① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{startOption}{fracAB}가 유한소수가 되려면 우선 {b}는 반드시 {primeFactor}의 배수이어야 한다. {b_range}에서 가능한 수는 {b_possibles}이다.\n{bCases}\n" \
              "따라서 분수가 유한소수가 되도록 하는 순서쌍의 개수는 총 {nonrepeatAnswer}이다. {optionComment}\n\n"

    optionCommentText = "전체 가능한 순서쌍의 개수는 {totalPairs}개이므로, 분수가 유한소수가 되지 않도록 하는 순서쌍의 개수는 {repeatAnswer}이다."
    startOptionText = "주어진 분수를 유한소수로 나타낼 수 없도록 하는 순서쌍의 개수를 구하기 위해서는, " \
                         "주어진 범위의 {a}, {b}로 만들 수 있는 모든 순서쌍의 개수에서 분수가 유한소수가 되도록 하는 순서쌍의 개수를 빼면 된다.\n"

    # 문제에 필요한 숫자들을 생성합니다.
    primeFactor = random.choice([3, 7, 11, 13, 17, 19])
    a_range = "".join(['1', "≤", " a ", "＜", '10'])

    b_start = random.choice([10, 20, 30])
    if primeFactor == 3 :
        _brange = 10
    else :
        _brange = 20
    b_end = b_start + _brange
    b_range = "".join([str(b_start), "≤", " b ", "＜", str(b_end)])

    possibleBs = multipleUnderRange(primeFactor, b_start, b_end)

    twoFiveValue = twoFiveDenom(twoRange=(1, 3), fiveRange=(1, 3))[0]

    initialDenom = twoFiveValue * primeFactor
    initialDenomFactored = getFactoredIntFormula(initialDenom)

    fracAB = makeFractionFormula("b", initialDenomFactored + " times a", withTag=True)

    possibleAsList = []
    nonrepeat_pairs = 0
    for pB in possibleBs :
        tempAs = []
        for a in range(1, 10):
            tempFrac = (pB, initialDenom*a)
            if not isRepeatingDecimal(tempFrac) :
                tempAs.append(a)
                nonrepeat_pairs += 1
        possibleAsList.append(tempAs)

    caseComment = "{numCount} {bFormula}일 때 분수를 유한소수로 만드는 {a}는 {aValues}로 총 {aN}개이다."

    bCasesList = []
    for ind, pB in enumerate(possibleBs) :
        numCount = aT(str(ind+1) + ")")
        bFormula = aT("b = " + str(pB))
        aValues = ", ".join(map(aT, possibleAsList[ind]))
        _comment = caseComment.format(numCount=numCount, bFormula=bFormula, a=aT("a"), aValues=aValues, aN=aT(len(possibleAsList[ind])))
        bCasesList.append(_comment)

    pairFormula = aT(" ".join(['(', 'a', ',~ ', 'b', ')']))
    allPairs = 9 * _brange

    isrepeat = random.choice([0, 1])
    if isrepeat:
        optionText = "없"
        ansValue = allPairs - nonrepeat_pairs
        startOption = startOptionText.format(a=aT("a"), b=aT("b"))
        optionComment = optionCommentText.format(totalPairs = aT("".join(['9 times ', str(_brange), " = ", str(allPairs)])),
                                                 repeatAnswer=aT(" ".join([str(x) for x in [allPairs, "-", nonrepeat_pairs, "=", ansValue]])))
    else:
        optionText = "있"
        ansValue = nonrepeat_pairs
        startOption = ""
        optionComment = ""

    ansInd, ansNums = makeChoices(ansValue, random.choice([2, 3]), True)
    # print(ansNums)

    # 내용을 채워 넣습니다.

    stem = stem.format(fracAB=fracAB, optionText=optionText, a=aT("a"), b=aT("b"), pairFormula=pairFormula, a_range=aT(a_range),
                       b_range=aT(b_range), n1 = ansNums[0], n2 = ansNums[1], n3 = ansNums[2], n4 = ansNums[3], n5 = ansNums[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(startOption=startOption, fracAB=fracAB, b=aT("b"), primeFactor=aT(primeFactor), b_range=aT(b_range),
                             b_possibles=", ".join(map(aT, possibleBs)), bCases="\n".join(bCasesList), nonrepeatAnswer=aT(nonrepeat_pairs),
                             optionComment=optionComment)

    return stem, answer, comment


def rationalandprime211_Stem_027():
    stem = "순환소수 {decimalNum}{postp} 분수로 나타내려고 한다. {xFormula}이라 할 때, 다음 중 이용할 수 있는 가장 간단한 식은?\n① {n1}\n② {n2}\n③ {n3}\n④ {n4}\n⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{xExtended}이므로 {largeXFormula}, {smallXFormula}\n{ansFormula}\n따라서 이용할 수 있는 가장 간단한 식은 {xFormula}이다.\n\n"

    # 정답지를 지정합니다
    ansNums = list(map(aT, ['10x`-`x', '100x`-`x', '100x`-`10x', '1000x`-`10x', '1000x`-`100x']))

    # 순환소수 하나를 생성합니다.
    while True :
        repeatLength = random.choices([1, 2], weights=[2, 3], k=1)[0]
        nonrepeatLen = random.choices([0, 1, 2], weights=[1, 2, 2], k=1)[0]
        if repeatLength == 2 and nonrepeatLen == 2 :
            pass
        else :
            break

    decimal = makeRandomDecimal(0, nonrepeatLen, repeatLength)

    # 정답지를 저장합니다.
    if nonrepeatLen== 0 :
        if repeatLength == 1 :
            ansInd = 0
        else :
            ansInd = 1
    elif nonrepeatLen == 1 :
        if repeatLength == 1 :
            ansInd = 2
        else :
            ansInd = 3
    else :
        ansInd = 4

    decimalNum = makeCorrectDecimalFormula(*decimal)
    xFormula = "x = " + decimalNum

    xExtended = xFormula + " = " + makeDecimalNumber(decimal)

    after10 = 10 ** nonrepeatLen
    before10 = after10 * (10 ** repeatLength)

    frac = decimalTupleToFraction(decimal)
    _frac = Fraction(*frac)

    _beforeFraction = _frac * before10
    _afterFraction = _frac * after10

    beforeDecimal = fractionToDecimalTuple(_beforeFraction.numerator, _beforeFraction.denominator)
    afterDecimal = fractionToDecimalTuple(_afterFraction.numerator, _afterFraction.denominator)

    if after10 == 1 :
        after10Text = ""
    else :
        after10Text = str(after10)

    beforeFormula = " ".join(map(str, [before10, 'x', '`=`', makeDecimalNumber(beforeDecimal)]))
    afterFormula = " ".join(map(str, [after10Text, 'x', '=', makeDecimalNumber(afterDecimal)]))

    _value = _beforeFraction - _afterFraction
    value = _value.numerator

    ansFormula = " ".join(map(str, ['therefore~', before10, 'x', '`-`', after10Text, 'x', '`=`', value]))


    # 내용을 채웁니다.
    stem = stem.format(decimalNum=aT(decimalNum), postp=proc_jo(int(decimal[1][-1]), 1), xFormula=aT(xFormula),
                       n1 = ansNums[0], n2 = ansNums[1], n3 = ansNums[2], n4 = ansNums[3], n5 = ansNums[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(xExtended=aT(xExtended), largeXFormula=aT(beforeFormula), smallXFormula=aT(afterFormula),
                             ansFormula=aT(ansFormula), xFormula=ansNums[ansInd])

    return stem, answer, comment


def rationalandprime211_Stem_028():
    stem = "순환소수 {x}를 분수로 나타낼 때, {ansChoice}를 이용하면 계산이 편리한 {x}의 값으로 가장 적절한 것은?\n① {n1}\n② {n2}\n③ {n3}\n④ {n4}\n⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{ansNum} {xFormula}일 때,\n{largeXFormula} -- ㉠,\n{smallXFormula} -- ㉡\n㉠ - ㉡을 하면 {ansFormula} {xFraction}\n\n"

    # 정답지를 지정합니다
    possibleForms = list(map(aT, ['10x`-`x', '100x`-`x', '100x`-`10x', '1000x`-`10x', '1000x`-`100x']))

    # 순환부와 비순환부의 자리를 정리합니다.
    decimalCreationInfo = [(0, 1), (0, 2), (1, 1), (1, 2), (2, 1)]

    # 조건에 맞게 순환소수를 생성합니다.
    allDecimals = []
    for nonrepeatLen, repeatLength in decimalCreationInfo :
        tempDec = makeRandomDecimal(0, nonrepeatLen, repeatLength)
        allDecimals.append(tempDec)

    # 정답을 정합니다.
    ansInd = random.choice(range(5))

    # 선택지를 만듭니다.
    decimalFormulas = list(map(lambda x : makeCorrectDecimalFormula(*x, withTag=True), allDecimals))

    ansDecimal = allDecimals[ansInd]

    xFormula = "x = " + makeDecimalNumber(ansDecimal)

    nonrepeatLen = decimalCreationInfo[ansInd][0]
    repeatLength = decimalCreationInfo[ansInd][1]
    after10 = 10 ** nonrepeatLen
    before10 = after10 * (10 ** repeatLength)

    frac = decimalTupleToFraction(ansDecimal)
    _frac = Fraction(*frac)

    _beforeFraction = _frac * before10
    _afterFraction = _frac * after10

    beforeDecimal = fractionToDecimalTuple(_beforeFraction.numerator, _beforeFraction.denominator)
    afterDecimal = fractionToDecimalTuple(_afterFraction.numerator, _afterFraction.denominator)

    if after10 == 1 :
        after10Text = ""
    else :
        after10Text = str(after10)

    coeff = before10 - after10
    if coeff == 1:
        coeffText = ""
    else:
        coeffText = str(coeff)

    beforeFormula = " ".join(map(str, [before10, 'x', '`=`', makeDecimalNumber(beforeDecimal)]))
    afterFormula = " ".join(map(str, [after10Text, 'x', '=', makeDecimalNumber(afterDecimal)]))

    _value = _beforeFraction - _afterFraction
    value = _value.numerator

    ansFormula = " ".join(map(str, [coeffText, 'x', '`=`', value]))

    xFraction = makeFractionFormula(value, coeffText)
    xFraction = " ".join(map(str, ['therefore~', 'x', '`=`', xFraction]))

    reducedFrac = Fraction(value, coeff)
    if reducedFrac.numerator != value :
        xFraction = joinList([xFraction, eq, makeFractionFormula(reducedFrac.numerator, reducedFrac.denominator)])

    # 내용을 채웁니다.
    stem = stem.format(x=aT("x"), ansChoice=possibleForms[ansInd],
                       n1 = decimalFormulas[0], n2 = decimalFormulas[1], n3 = decimalFormulas[2], n4 = decimalFormulas[3], n5 = decimalFormulas[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(ansNum=answer_dict[ansInd], xFormula=aT(xFormula),
                             largeXFormula=aT(beforeFormula), smallXFormula=aT(afterFormula),
                             ansFormula=aT(ansFormula), xFraction=aT(xFraction))

    return stem, answer, comment


def rationalandprime211_Stem_029():
    stem = "순환소수 {xFormula}에 대한 설명으로 옳지 않은 것은?\n① {otherDecimal}보다 {bigOrSmall}다.\n② {xEquation}이다.\n" \
           "③ {decimalFormula}{postp} 나타낸다.\n④ 분수로 나타내면 {frac}이다.\n⑤ 분수로 나타낼 때 가장 편리한 식은 {largeX_smallX}이다.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{xExtended}이므로 {largeXFormula}, {smallXFormula}\n따라서 {subtractFormula}이므로 {simplifiedX} {xFraction}\n따라서 옳지 않은 것은 {ans}이다.\n\n"

    # 정답지를 지정합니다
    possibleXs = list(map(aT, ['10x`-`x', '100x`-`x', '100x`-`10x', '1000x`-`10x', '1000x`-`100x']))

    # 순환소수 하나를 생성합니다.
    nonrepeatLen = 1
    repeatLength = 2
    decimal = makeRandomDecimal(0, nonrepeatLen, repeatLength)
    otherDecimal = ("0.", decimal[0][-1] + decimal[1][0])

    largeX_smallX = possibleXs[3]

    decimalFormula = makeCorrectDecimalFormula(*decimal, withTag=True)
    decimalNumber = makeDecimalNumber(decimal)

    xFormula = "x = " + decimalNumber

    after10 = 10 ** nonrepeatLen
    before10 = after10 * (10 ** repeatLength)

    frac = decimalTupleToFraction(decimal)
    _frac = Fraction(*frac)

    otherFrac = decimalTupleToFraction(otherDecimal)
    _otherFrac = Fraction(*otherFrac)

    _beforeFraction = _frac * before10
    _afterFraction = _frac * after10

    beforeDecimal = fractionToDecimalTuple(_beforeFraction.numerator, _beforeFraction.denominator)
    afterDecimal = fractionToDecimalTuple(_afterFraction.numerator, _afterFraction.denominator)

    if after10 == 1 :
        after10Text = ""
    else :
        after10Text = str(after10)

    beforeFormula = " ".join(map(str, [before10, 'x', '`=`', makeDecimalNumber(beforeDecimal)]))
    afterFormula = " ".join(map(str, [after10Text, 'x', '=', makeDecimalNumber(afterDecimal)]))

    _value = _beforeFraction - _afterFraction
    value = _value.numerator

    coeff = before10 - after10
    if coeff == 1:
        coeff = ""
    else:
        coeff = str(coeff)

    subtractFormula = " ".join(map(str, [before10, 'x', '`-`', after10Text, 'x', '`=`', value]))
    simplifiedX = " ".join(map(str, [coeff, 'x', '`=`', value]))

    xFraction = makeFractionFormula(value, coeff)
    xFraction = " ".join(map(str, ['therefore~', 'x', '`=`', xFraction]))

    if value != _frac.numerator :
        reducedFraction = makeFractionFormula(_frac.numerator, _frac.denominator)
        xFraction = xFraction + " `=` " + reducedFraction

    # 정답을 정합니다.
    ansInd = random.choice([0, 1, 3])

    if _otherFrac < _frac :
        if ansInd == 0 :
            optionText = "작"
        else :
            optionText = "크"
    else :
        if ansInd == 0 :
            optionText = "크"
        else :
            optionText = "작"

    if ansInd != 3 :
        fracForm = makeFractionFormula(_frac.numerator, _frac.denominator)
    else :
        fracForm = makeFractionFormula(_otherFrac.numerator, _otherFrac.denominator)

    if ansInd == 1 :
        _other_after10 = 10 ** 0
        _other_before10 = after10 * (10 ** 2)

        _other_beforeFraction = _otherFrac * before10
        _other_afterFraction = _otherFrac * after10

        _other_value = _other_beforeFraction - _other_afterFraction
        otherValue = _other_value.numerator

        _other_coeff = _other_before10 - _other_after10
        if _other_coeff == 1:
            _other_coeff = ""
        else:
            _other_coeff = str(_other_coeff)

        _other_simplifiedX = " ".join(map(str, [_other_coeff, 'x', '`=`', otherValue]))

        xEquation = aT(_other_simplifiedX)
    else :
        xEquation = aT(simplifiedX)

    # 내용을 채웁니다.
    stem = stem.format(xFormula = aT(xFormula), otherDecimal=makeCorrectDecimalFormula(*otherDecimal, withTag=True),
                       bigOrSmall=optionText, xEquation=xEquation, decimalFormula=decimalFormula,
                       postp=proc_jo(int(decimal[1][-1]), check=10), frac=aT(fracForm), largeX_smallX=aT(largeX_smallX))
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(xExtended=aT(xFormula), largeXFormula=aT(beforeFormula), smallXFormula=aT(afterFormula),
                             subtractFormula=aT(subtractFormula), simplifiedX=aT(simplifiedX), xFraction=aT(xFraction),
                             ans=answer_dict[ansInd])

    return stem, answer, comment


def rationalandprime211_Stem_030():
    stem = "다음 중 순환소수를 분수로 나타낸 것으로 옳지 않은 것은?\n① {n1}\n② {n2}\n③ {n3}\n④ {n4}\n⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{ansNum} {correctDecimalEquation}\n\n"

    # 순환부와 비순환부의 자리를 정리합니다.
    decimalCreationInfo = [(0, 1), (0, 2), (1, 1), (1, 2), (2, 1)]

    # 조건에 맞게 순환소수를 생성합니다.
    allDecimals = []
    for nonrepeatLen, repeatLength in decimalCreationInfo :
        tempDec = makeRandomDecimal(0, nonrepeatLen, repeatLength)
        allDecimals.append(tempDec)

    # 정답을 정합니다.
    ansInd = random.choice(range(5))

    # 선택지를 만듭니다.
    decimalFormulas = list(map(lambda x : makeCorrectDecimalFormula(*x), allDecimals))
    fractions = list(map(lambda x: decimalTupleToFraction(x, irreducible=False), allDecimals))

    ansFracCorrect = list(fractions[ansInd])
    ansFracWrong = ansFracCorrect[:]
    ansFracWrong[1] *= 10
    fractions[ansInd] = tuple(ansFracWrong)

    fractions = list(map(lambda x: Fraction(*x), fractions))
    fracForms = list(map(lambda x : makeFractionFormula(x.numerator, x.denominator), fractions))

    choices = makeEquality(decimalFormulas, fracForms, True)

    ansFracCorrect = Fraction(*ansFracCorrect)
    correctFracForm = makeFractionFormula(ansFracCorrect.numerator, ansFracCorrect.denominator)

    correctDecimalEquation = makeEquality([decimalFormulas[ansInd]], [correctFracForm], True)[0]


    # 내용을 채웁니다.
    stem = stem.format(n1 = choices[0], n2 = choices[1], n3 = choices[2], n4 = choices[3], n5 = choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(ansNum=answer_dict[ansInd], correctDecimalEquation=correctDecimalEquation)

    return stem, answer, comment


def rationalandprime211_Stem_031():
    stem = "서로소인 두 자연수 {ab}에 대하여 {bOverA}를 소수로 나타내면 {decimal}이다. 이 때, {aOverB}를 순환소수로 나타내면?\n" \
           "① {n1}\n② {n2}\n③ {n3}\n④ {n4}\n⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{decimalFormula}이므로 {aValue}, {bValue}\n{ansFormula}\n\n"

    # 임의의 분수를 생성합니다. 조건에 맞으면 a, b를 구합니다.
    while True :
        frac = makeRandomFraction(repeat='yes')
        givenDecimal = fractionToDecimalTuple(*frac)
        if len(str(givenDecimal[0]).split(".")[1]) > 2 :
            continue
        reversedFrac = (frac[1], frac[0])
        reversedDecimal = fractionToDecimalTuple(*reversedFrac)

        if len(str(reversedDecimal[0]).split(".")[1]) > 2 :
            continue
        if len(str(reversedDecimal[1])) > 3 or len(str(reversedDecimal[1]))==0:
            continue
        break

    aValue = frac[1]
    bValue = frac[0]

    # 분자와 분모를 뒤집은 분수를 만듭니다.


    # 뒤집은 분수의 소수자리 숫자를 활용하여 여러 개의 순환소수를 만듭니다.
    frontPart = reversedDecimal[0].split(".")
    if frontPart[1] and frontPart[1] :
        front = frontPart[0]
        middle = frontPart[1][0]
        end = reversedDecimal[1][0]
    else :
        front = int(frontPart[0])
        if len(reversedDecimal[1]) > 1 :
            middle = int(reversedDecimal[1][0])
            end = int(reversedDecimal[1][1])
        else :
            end = int(reversedDecimal[1][0])
            middle = (int(front) + int(end)) // 2

    if front == middle :
        if middle == 9 :
            middle = 8
        else :
            middle += 1
    while True :
        if end in [front, middle]:
            end = random.choice(range(1, 8))
        else :
            break

    decimalChoices = generateDecimalTuples(str(front), str(middle), str(end))

    random.shuffle(decimalChoices)

    if reversedDecimal in decimalChoices :
        decimalChoices.remove(reversedDecimal)

    ansInd = random.choice(range(5))

    if len(decimalChoices) > 4 :
        decimalChoices = decimalChoices[:4]

    decimalChoices.insert(ansInd, reversedDecimal)
    decimalChoices = list(map(lambda x : makeCorrectDecimalFormula(*x), decimalChoices))

    initialFraction = decimalTupleToFraction(givenDecimal, False)
    givenDecimalFormula = makeCorrectDecimalFormula(*givenDecimal)

    decimalFormula = [givenDecimalFormula, "`=`", makeFractionFormula(*initialFraction)]
    if initialFraction != frac :
        decimalFormula.append("`=`")
        decimalFormula.append(makeFractionFormula(*frac))

    bOverA = makeFractionFormula("b", "a")
    aOverB = makeFractionFormula("a", "b")

    ansFormula = [aOverB, "`=`", makeFractionFormula(*reversedFrac), "`=`", makeDecimalNumber(reversedDecimal), "`=`", decimalChoices[ansInd]]
    ab = aT("a,~b")

    aValueText = " ".join(['a', '`=`', str(aValue)])
    bValueText = " ".join(['b', '`=`', str(bValue)])

    decimalChoices = list(map(aT, decimalChoices))

    # 내용을 채웁니다.


    stem = stem.format(ab=ab, bOverA=aT(bOverA), decimal=aT(givenDecimalFormula), aOverB=aT(aOverB),
                       n1=decimalChoices[0], n2=decimalChoices[1], n3=decimalChoices[2], n4=decimalChoices[3], n5=decimalChoices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(decimalFormula=aT(" ".join(decimalFormula)), aValue=aT(aValueText), bValue=aT(bValueText), ansFormula=aT(" ".join(ansFormula)))

    return stem, answer, comment


def rationalandprime211_Stem_032():
    stem = "{problemEquation}을 계산하여 기약분수로 나타내면?\n" \
           "① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{commentFormula}\n\n"

    # 문제 생성에 사용할 숫자 2개를 뽑습니다.
    first = random.choice(range(10))
    numbers = list(range(1, 9))
    if first in numbers :
        numbers.remove(first)
    second = random.choice(numbers)

    numeratorText = str(first) + str(second)

    numerator = int(numeratorText)

    decimal = ("1.", numeratorText)

    decimalFormula = makeCorrectDecimalFormula(*decimal)

    initialFraction = decimalTupleToFraction(decimal, irreducible=False)

    simplifiedFraction = decimalTupleToFraction(decimal)

    # 식을 만듭니다.
    fracSum = "".join(['1', ' `+` ', makeFractionFormula(str(numerator), "10^2"), " `+` ", makeFractionFormula(numerator, "10^4"), " `+` ",
                       makeFractionFormula(numerator, "10^6"), " `+` cdots"])
    parenSum = "".join(["=` 1 `+` (", str(numerator/10**2), " `+` ", str(numerator/10**4), " `+` ", "{:f}".format(numerator/10**6), " `+` cdots )"])

    decimalSum = "".join(['=`1 `+` ', makeDecimalNumber(("0.", numeratorText)), " `=` ", decimalFormula])

    finalSum = "=` " + makeFractionFormula(*initialFraction)

    if initialFraction != simplifiedFraction :
        finalSum = finalSum + " `=` " + makeFractionFormula(*simplifiedFraction)

    finalNumerator = simplifiedFraction[0]

    ansInd, otherNumerators = makeChoices(finalNumerator, diff=4, positive=True, withTag=False)
    # print(otherNumerators)
    _choiceFractions = [Fraction(num, int(simplifiedFraction[1])) for num in otherNumerators]
    choiceFractions = list(map(lambda x : makeFractionFormula(x.numerator, x.denominator, withTag=True), _choiceFractions))

    commentFormula = "\n".join(map(aT, [fracSum, parenSum, decimalSum, finalSum]))

    # 내용을 채웁니다.
    stem = stem.format(problemEquation=aT(fracSum), n1=choiceFractions[0], n2=choiceFractions[1],
                       n3=choiceFractions[2], n4=choiceFractions[3], n5=choiceFractions[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(commentFormula=aT(commentFormula))

    return stem, answer, comment



def rationalandprime211_Stem_033():
    stem = "어떤 기약분수를 소수로 나타내는데 종훈이는 분모를 잘못 보아서 {decimal1}{postp1} 나타내었고, " \
           "승아는 분자를 잘못 보아서 {decimal2}{postp2} 나타내었다. 이 때 처음 기약분수를 소수로 바르게 나타낸 것은?\n" \
           "① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n종훈이는 분자를 제대로 보았으므로 {decimal1Formula}에서 처음 기약분수의 분자는 {numerator}이다.\n" \
              "승아는 분모를 제대로 보았으므로 {decimal2Formula}에서 처음 기약분수의 분모는 {denominator}이다.\n" \
              "{ansFormula}\n\n"

    # 문제 생성에 사용할 분수를 생성합니다.
    while True :
        firstFraction, firstDecimal = makeRandomFraction(repeat='yes', repeatMax=2, nonrepeatMax=1, maxValue=4,
                                                         returnDecimal=True, numeratorMaxDigit=(2, [0.3, 0.7]),
                                                         denominatorMaxDigit=(3, [0.1, 0.8, 0.3]))
        secondFraction, secondDecimal = makeRandomFraction(repeat='yes', repeatMax=2, nonrepeatMax=1, maxValue=4,
                                                           returnDecimal=True, numeratorMaxDigit=(2, [0.3, 0.7]),
                                                           denominatorMaxDigit=(3, [0.1, 0.8, 0.3]))
        if secondFraction == firstFraction :
            continue

        if gcd(firstFraction[0], secondFraction[1]) != 1 :
            continue

        thirdFraction = (firstFraction[0], secondFraction[1])
        thirdDecimal = fractionToDecimalTuple(*thirdFraction)
        if not thirdDecimal[1] :
            continue
        if len(thirdDecimal[0].split(".")[1]) > 1 :
            continue
        if len(thirdDecimal[1]) > 2 :
            continue

        break

    # 뒤집은 분수의 소수자리 숫자를 활용하여 여러 개의 순환소수를 만듭니다.
    frontPart = thirdDecimal[0].split(".")
    if frontPart[1] :
        # print(thirdDecimal)
        front = int(frontPart[0])
        middle = int(frontPart[1][0])
        end = int(thirdDecimal[1][0])

    else :
        front = int(frontPart[0])
        if len(thirdDecimal[1]) > 1 :
            middle = int(thirdDecimal[1][0])
            end = int(thirdDecimal[1][1])
        else :
            end = int(thirdDecimal[1][0])
            middle = (int(front) + int(end)) // 2

    if front == middle :
        if middle == 9 :
            middle = 8
        else :
            middle += 1
    while True :
        if end in [front, middle]:
            end = random.choice(range(1, 8))
        else :
            break

    # 정답 소수를 활용하여 다른 선택지를 만들고, 정답 번호를 정합니다.
    decimalChoices = generateDecimalTuples(str(front), str(middle), str(end))
    random.shuffle(decimalChoices)
    ansInd = random.choice(range(5))

    if thirdDecimal in decimalChoices :
        decimalChoices.remove(thirdDecimal)
    else :
        decimalChoices = decimalChoices[:4]

    decimalChoices.insert(ansInd, thirdDecimal)

    # 해설에 사용할 여러 식을 만듭니다.
    firstDecimalFormula = makeCorrectDecimalFormula(*firstDecimal)
    firstFractionFormula = makeFractionFormula(*firstFraction)

    secondDecimalFormula = makeCorrectDecimalFormula(*secondDecimal)
    secondFractionFormula = makeFractionFormula(*secondFraction)

    thirdFractionFormula = makeFractionFormula(*thirdFraction)
    thirdDecimalFormula = makeCorrectDecimalFormula(*thirdDecimal)

    equalities = makeEquality([firstDecimalFormula, secondDecimalFormula, thirdFractionFormula],
                              [firstFractionFormula, secondFractionFormula, thirdDecimalFormula])

    # 최종적으로 선택지를 구성합니다.
    choiceDecimals = list(map(lambda x : makeCorrectDecimalFormula(*x, withTag=True), decimalChoices))

    # 내용을 채웁니다.
    stem = stem.format(decimal1=aT(firstDecimalFormula), postp1=proc_jo(int(firstDecimal[1][-1]), check=10),
                       decimal2=aT(secondDecimalFormula), postp2=proc_jo(int(secondDecimal[1][-1]), check=10),
                       n1=choiceDecimals[0], n2=choiceDecimals[1], n3=choiceDecimals[2],
                       n4=choiceDecimals[3], n5=choiceDecimals[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(decimal1Formula=aT(equalities[0]), numerator=aT(thirdFraction[0]),
                             decimal2Formula=aT(equalities[1]), denominator=aT(thirdFraction[1]),
                             ansFormula=aT("".join(["therefore~ ", equalities[2]])))

    return stem, answer, comment



def rationalandprime211_Stem_034():
    stem = "{aDecimal}, {bDecimal}일 때, {bOverA}를 순환소수로 나타내면?\n"\
           "① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{aFormula},\n{bFormula}이므로\n{bOverAFormula}{ansDecimalFormula}\n\n"

    # 문제 생성에 사용할 분수를 생성합니다.
    while True :
        firstFraction, firstDecimal = makeRandomFraction(repeat='yes', repeatMax=2, nonrepeatMax=1, maxValue=4,
                                                         returnDecimal=True, numeratorMaxDigit=(2, [0.3, 0.7]),
                                                         denominatorMaxDigit=(3, [0.1, 0.8, 0.3]))
        secondFraction, secondDecimal = makeRandomFraction(repeat='yes', repeatMax=2, nonrepeatMax=1, maxValue=4,
                                                           returnDecimal=True, numeratorMaxDigit=(2, [0.3, 0.7]),
                                                           denominatorMaxDigit=(3, [0.1, 0.8, 0.3]))
        if secondFraction == firstFraction :
            continue


        _thirdFraction = Fraction(*secondFraction) / Fraction(*firstFraction)
        thirdFraction = (_thirdFraction.numerator, _thirdFraction.denominator)
        thirdDecimal = fractionToDecimalTuple(*thirdFraction)
        if not thirdDecimal[1] :
            continue
        if len(thirdDecimal[0].split(".")[1]) > 1 :
            continue
        if len(thirdDecimal[1]) > 2 :
            continue

        break

    # 정답이 되는 분수의 소수자리 숫자를 활용하여 여러 개의 순환소수를 만듭니다.
    frontPart = thirdDecimal[0].split(".")
    if frontPart[1] :
        # print(thirdDecimal)
        front = int(frontPart[0])
        middle = int(frontPart[1][0])
        end = int(thirdDecimal[1][0])

    else :
        front = int(frontPart[0])
        if len(thirdDecimal[1]) > 1 :
            middle = int(thirdDecimal[1][0])
            end = int(thirdDecimal[1][1])
        else :
            end = int(thirdDecimal[1][0])
            middle = (int(front) + int(end)) // 2

    if front == middle :
        if middle == 9 :
            middle = 8
        else :
            middle += 1
    while True :
        if end in [front, middle]:
            end = random.choice(range(1, 8))
        else :
            break

    # 정답 소수를 활용하여 다른 선택지를 만들고, 정답 번호를 정합니다.
    decimalChoices = generateDecimalTuples(str(front), str(middle), str(end))
    random.shuffle(decimalChoices)
    ansInd = random.choice(range(5))

    if thirdDecimal in decimalChoices :
        decimalChoices.remove(thirdDecimal)
    else :
        decimalChoices = decimalChoices[:4]

    decimalChoices.insert(ansInd, thirdDecimal)

    # 해설에 사용할 여러 식을 만듭니다.
    firstDecimalFormula = makeCorrectDecimalFormula(*firstDecimal)
    firstFractionFormula = makeFractionFormula(*firstFraction)
    _firstDecimalToFraction = decimalTupleToFraction(firstDecimal, irreducible=False)
    firstDecimalToFraction = makeFractionFormula(*_firstDecimalToFraction)

    secondDecimalFormula = makeCorrectDecimalFormula(*secondDecimal)
    secondFractionFormula = makeFractionFormula(*secondFraction)
    _secondDecimalToFraction = decimalTupleToFraction(secondDecimal, irreducible=False)
    secondDecimalToFraction = makeFractionFormula(*_secondDecimalToFraction)

    aDecimal, bDecimal = makeEquality(['a', 'b'], [firstDecimalFormula, secondDecimalFormula])
    bOverA = makeFractionFormula("b", "a")

    # eq = '`=`' / _t = '`times`' / _p = '`+`' / _m = '`-`' / _d = '`div`'

    aFormulaList = [aDecimal, eq, firstDecimalToFraction]
    if firstDecimalToFraction != firstFraction:
        aFormulaList.append(eq)
        aFormulaList.append(firstFractionFormula)

    bFormulaList = [bDecimal, eq, secondDecimalToFraction]
    if secondDecimalToFraction != secondFraction:
        bFormulaList.append(eq)
        bFormulaList.append(secondFractionFormula)

    thirdFractionFormula = makeFractionFormula(*thirdFraction)
    thirdDecimalNumber = makeDecimalNumber(thirdDecimal)
    thirdDecimalFormula = makeCorrectDecimalFormula(*thirdDecimal)

    bOverAFormulaList = [bOverA, eq, "b", ts, makeFractionFormula(1, 'a'),
                      eq, secondFractionFormula, ts, makeFractionFormula(firstFraction[1], firstFraction[0]), eq, thirdFractionFormula]

    ansDecimalFormula = [eq, thirdDecimalNumber, eq, thirdDecimalFormula]



    # 최종적으로 선택지를 구성합니다.
    choiceDecimals = list(map(lambda x : makeCorrectDecimalFormula(*x, withTag=True), decimalChoices))

    # 내용을 채웁니다.
    stem = stem.format(aDecimal=aT(aDecimal), bDecimal=aT(bDecimal), bOverA=aT(bOverA),
                       n1=choiceDecimals[0], n2=choiceDecimals[1], n3=choiceDecimals[2],
                       n4=choiceDecimals[3], n5=choiceDecimals[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(aFormula=aT(" ".join(aFormulaList)), bFormula=aT(" ".join(bFormulaList)),
                             bOverAFormula=aT(" ".join(bOverAFormulaList)), ansDecimalFormula=aT(" ".join(ansDecimalFormula)))

    return stem, answer, comment



def rationalandprime211_Stem_035():
    stem = "{decimalSum}{postp} 계산한 값을 기약분수로 나타내면 {bOverA}일 때, 자연수 {a_b}에 대하여 {optionText}의 값을 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{decimalSumFormula}\n따라서 {aFormula}, {bFormula}이므로 {abFormula}\n\n"

    # 문제 생성에 사용할 조건을 정합니다.
    howManyDigit = random.choice(range(1, 3))

    if howManyDigit==2 :
        optionText = "a+b"
    else :
        optionText = 'ab'

    while True :
        aDecimal = makeRandomDecimal(1, 0, howManyDigit)
        bDecimal = makeRandomDecimal(0, 0, howManyDigit)
        if aDecimal != bDecimal :
            break

    aFraction = decimalTupleToFraction(aDecimal, irreducible=False)
    bFraction = decimalTupleToFraction(bDecimal, irreducible=False)

    _aFraction = Fraction(*aFraction)
    _bFraction = Fraction(*bFraction)

    _aPlusB = _aFraction + _bFraction

    aValue = _aPlusB.denominator
    bValue = _aPlusB.numerator

    if howManyDigit==1 :
        ansValue = aValue * bValue
    else :
        ansValue = aValue + bValue

    _numerator = int(aFraction[0]) + int(bFraction[0])
    if _numerator != bValue :
        middleFraction = makeFractionFormula(_numerator, aFraction[1])
    else :
        middleFraction = ""

    aDecimalFormula = makeCorrectDecimalFormula(*aDecimal)
    bDecimalFormula = makeCorrectDecimalFormula(*bDecimal)

    aFractionFormula = makeFractionFormula(*aFraction)
    bFractionFormula = makeFractionFormula(*bFraction)

    aPlusBFractionFormula = makeFractionFormula(bValue, aValue)
    decimalSumText = " ".join([aDecimalFormula, ps, bDecimalFormula])

    bOverAText = makeFractionFormula('b', 'a', withTag=True)

    equalities = makeEquality(['a', 'b', optionText], list(map(str, [aValue, bValue, ansValue])), withTag=True)

    decimalSumFormulaList = [aDecimalFormula, ps, bDecimalFormula, eq,
                             aFractionFormula, ps, bFractionFormula, eq]
    if middleFraction:
        decimalSumFormulaList.append(middleFraction)
        decimalSumFormulaList.append(eq)

    decimalSumFormulaList.append(aPlusBFractionFormula)

    # 내용을 채웁니다.
    stem = stem.format(decimalSum = aT(decimalSumText), postp=proc_jo(int(bDecimal[1]), check=1), bOverA=bOverAText,
                       a_b=aT("a,~" + "b"), optionText=aT(optionText))
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(decimalSumFormula=aT(" ".join(decimalSumFormulaList)), aFormula=equalities[0], bFormula=equalities[1],
                             abFormula=equalities[2])

    return stem, answer, comment



def rationalandprime211_Stem_036():
    stem = "등식 {questionFormula}{postp} 만족시키는 {y}의 값을 순환소수로 나타내면?\n" \
           "① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{questionFormula}에서 {secondDecimalFraction}이므로 {yValueFormula}\n{answerFormula}\n\n"

    # 문제 생성에 사용할 조건을 정합니다.
    howManyDigit = random.choice(range(1, 3))

    while True :
        yDecimal = makeRandomDecimal(0, 0, howManyDigit)
        secondDecimal = makeRandomDecimal(0, 0, howManyDigit)

        yFraction = decimalTupleToFraction(yDecimal)
        secondFraction = decimalTupleToFraction(secondDecimal)

        _yFraction = Fraction(*yFraction)
        _secondFraction = Fraction(*secondFraction)

        _yPlusSecond = _yFraction + _secondFraction

        if yDecimal != secondDecimal and _yPlusSecond.numerator != _yPlusSecond.denominator:
            break

    yDecimalFormula = makeCorrectDecimalFormula(*yDecimal)
    secondDecimalFormula = makeCorrectDecimalFormula(*secondDecimal)

    yFractionFormula = makeFractionFormula(*yFraction)
    secondFractionFormula = makeFractionFormula(*secondFraction)

    aPlusBFractionFormula = makeFractionFormula(_yPlusSecond.numerator, _yPlusSecond.denominator)

    yDecimalNumber = makeDecimalNumber(yDecimal)

    questionFormula = aT(" ".join([aPlusBFractionFormula, eq, "y", ps, secondDecimalFormula]))
    secondDecimalFraction = aT(" ".join([secondDecimalFormula, eq, secondFractionFormula]))
    yValueFormula = aT(" ".join(['y', eq, aPlusBFractionFormula, ms, secondFractionFormula, eq, yFractionFormula]))
    answerFormula = aT(" ".join(['therefore~', 'y', eq, yFractionFormula, eq, yDecimalNumber, eq, yDecimalFormula]))


    # 정답이 되는 분수의 소수자리 숫자를 활용하여 여러 개의 순환소수를 만듭니다.
    frontPart = yDecimal[0].split(".")
    if frontPart[1]:
        # print(thirdDecimal)
        front = int(frontPart[0])
        middle = int(frontPart[1][0])
        end = int(yDecimal[1][0])

    else:
        front = int(frontPart[0])
        if len(yDecimal[1]) > 1:
            middle = int(yDecimal[1][0])
            end = int(yDecimal[1][1])
        else:
            end = int(yDecimal[1][0])
            middle = (int(front) + int(end)) // 2

    if front == middle:
        if middle == 9:
            middle = 8
        else:
            middle += 1
    while True:
        if end in [front, middle]:
            end = random.choice(range(1, 8))
        else:
            break

    # 정답 소수를 활용하여 다른 선택지를 만들고, 정답 번호를 정합니다.
    decimalChoices = generateDecimalTuples(str(front), str(middle), str(end))
    random.shuffle(decimalChoices)
    ansInd = random.choice(range(5))

    if yDecimal in decimalChoices:
        decimalChoices.remove(yDecimal)
    else:
        decimalChoices = decimalChoices[:4]

    decimalChoices.insert(ansInd, yDecimal)

    # 최종적으로 선택지를 구성합니다.
    choiceDecimals = list(map(lambda x: makeCorrectDecimalFormula(*x, withTag=True), decimalChoices))

    # 내용을 채웁니다.
    stem = stem.format(questionFormula=questionFormula, postp=proc_jo(int(secondDecimal[1][-1]), check=1), y=aT("y"),
                       n1=choiceDecimals[0], n2=choiceDecimals[1], n3=choiceDecimals[2],
                       n4=choiceDecimals[3], n5=choiceDecimals[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(questionFormula=questionFormula, secondDecimalFraction=secondDecimalFraction,
                             yValueFormula=yValueFormula, answerFormula=answerFormula)

    return stem, answer, comment



def rationalandprime211_Stem_037():
    stem = "일차방정식 {xEquation}{postp} 만족시키는 {x}에 대하여 {questionInequality}{postp2} 만족시키는 모든 한 자리 자연수 {y}의 {optionText}?\n" \
           "① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{firstDecimalFraction}, {secondDecimalFraction}, {thirdDecimalFraction}이므로 주어진 일차방정식은 {xEquationFractioned}, {xEquationMonomial} {xValue}\n" \
              "이 때 주어진 부등식은 {questionInequalityXFilled}, {questionInequalitySameDenom}\n" \
              "{y}는 한 자리 자연수이므로 {yValues}이다. 따라서 모든 {y}의 {optionText} {ansValue}이다.\n\n"

    # 문제 생성에 사용할 조건을 정합니다.
    xValue = random.choice([1, 2, 5, 6, 9])
    y = symbols('y', real=True)
    isSum = random.choice([True, False])

    if isSum :
        optionText = "값의 합은"
    else :
        optionText = "개수는"

    yDenom = random.choice([6, 9, 10, 12, 18])

    # 일차방정식을 구성할 소수를 생성합니다.
    while True :
        firstDecimal = makeRandomDecimal(0, 0, 1)
        secondDecimal = makeRandomDecimal(0, 0, 1)

        firstFraction = decimalTupleToFraction(firstDecimal)
        secondFraction = decimalTupleToFraction(secondDecimal)

        _firstFraction = Fraction(*firstFraction)
        _secondFraction = Fraction(*secondFraction)

        _thirdFraction = _firstFraction * xValue + _secondFraction

        if firstDecimal != secondDecimal and _thirdFraction.numerator != _thirdFraction.denominator and _thirdFraction.denominator != 1:
            break

    # 만들어진 소수를 바탕으로 문제 지문 및 해설에 사용할 소수 및 분수 형태 식을 모두 생성합니다.
    firstDecimalFormula = makeCorrectDecimalFormula(*firstDecimal)
    secondDecimalFormula = makeCorrectDecimalFormula(*secondDecimal)

    thirdDecimal = fractionToDecimalTuple(_thirdFraction.numerator, _thirdFraction.denominator)
    thirdDecimalFormula = makeCorrectDecimalFormula(*thirdDecimal)

    firstFractionFormula = makeFractionFormula(*firstFraction)
    secondFractionFormula = makeFractionFormula(*secondFraction)
    thirdFractionFormula = makeFractionFormula(_thirdFraction.numerator, _thirdFraction.denominator)

    # 문제의 조건에 따라 부등식의 모양이 다릅니다. 이에 맞추어 부등식을 구성합니다.
    xDecimal = makeCorrectDecimalFormula("0.", 'x')
    xDenomFraction = makeFractionFormula(1, 'x')
    middlePart = ('y', yDenom)

    xDenomFractionValue = (1, xValue)
    xDecimalValue = (xValue, 9)

    # 먼저, 문제의 지문에 활용할 부등식의 내용물을 구성합니다.
    if xValue < 3 :
        leftPart = xDecimal
        rightPart = xDenomFraction
        postp2 = proc_jo(1, 1)

        leftPartValue = xDecimalValue
        rightPartValue = xDenomFractionValue
    else :
        leftPart = xDenomFraction
        rightPart = xDecimal
        postp2 = proc_jo(9, 1)

        leftPartValue = xDenomFractionValue
        rightPartValue = xDecimalValue

    # 문제의 해설에 사용할 부등식의 내용물을 구성합니다.
    leftPartFraction = makeFractionFormula(*leftPartValue)
    rightPartFraction = makeFractionFormula(*rightPartValue)
    middlePartFraction = makeFractionFormula(*middlePart)

    lcmOfThree = lcm(lcm(xValue, yDenom), 9)

    leftPartMultiplier = int(lcmOfThree / leftPartValue[1])
    rightPartMultiplier = int(lcmOfThree / rightPartValue[1])
    middlePartMultiplier = int(lcmOfThree / middlePart[1])

    leftPartSameDenom = [i * leftPartMultiplier for i in leftPartValue]
    rightPartSameDenom = [i * rightPartMultiplier for i in rightPartValue]
    middlePartSameDenomSym = middlePartMultiplier * y
    middlePartSameDenomSymText = convertIntoHangul(middlePartSameDenomSym)
    middlePartSameDenom = (middlePartSameDenomSymText, yDenom * middlePartMultiplier)

    leftPartSameDenomFraction = makeFractionFormula(*leftPartSameDenom)
    rightPartSameDenomFraction = makeFractionFormula(*rightPartSameDenom)
    middlePartSameDenomFraction = makeFractionFormula(*middlePartSameDenom)

    # 주어진 부등식을 만족하는 정답을 구합니다.
    leftValue = leftPartValue[0] / leftPartValue[1]
    rightValue = rightPartValue[0] / rightPartValue[1]

    satisfyingNumbers = []
    for n in range(1, 10):
        tempMiddle = n / yDenom
        if tempMiddle > leftValue and tempMiddle <= rightValue :
            satisfyingNumbers.append(n)

    if isSum :
        ansValue = sum(satisfyingNumbers)
    else :
        ansValue = len(satisfyingNumbers)

    # 문제에 사용할 여러 식들을 위의 재료를 바탕으로 순서대로 구성합니다.
    xEquation = aT(" ".join([firstDecimalFormula, "x", ps, secondDecimalFormula, eq, thirdDecimalFormula]))
    questionInequality = aT(" ".join([leftPart, rb, middlePartFraction, rqb, rightPart]))
    trivialEqualities = makeEquality([firstDecimalFormula, secondDecimalFormula, thirdDecimalFormula, "therefore~ x"],
                                     [firstFractionFormula, secondFractionFormula, thirdFractionFormula, str(xValue)],
                                     withTag=True)
    xEquationFractioned = aT(" ".join([firstFractionFormula, "x", ps, secondFractionFormula, eq, thirdFractionFormula]))
    _firstTimesX = _firstFraction * xValue
    xEquationMonomial = aT(" ".join(
        [firstFractionFormula, 'x', eq, makeFractionFormula(_firstTimesX.numerator, _firstTimesX.denominator)]))
    questionInequalityXFilled = aT(" ".join([leftPartFraction, rb, middlePartFraction, rqb, rightPartFraction]))
    questionInequalitySameDenom = aT(
        " ".join([leftPartSameDenomFraction, rb, middlePartSameDenomFraction, rqb, rightPartSameDenomFraction]))

    # 정답지를 구성합니다.
    ansInd, ansNums = makeChoices(ansValue)

    # 내용을 채웁니다.
    stem = stem.format(xEquation=xEquation, postp=proc_jo(int(thirdDecimal[1][-1]), 1), x=aT("x"),
                       questionInequality=questionInequality, postp2=postp2, y=aT("y"), optionText=optionText,
                       n1 = ansNums[0], n2 = ansNums[1], n3 = ansNums[2], n4 = ansNums[3], n5 = ansNums[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(firstDecimalFraction=trivialEqualities[0], secondDecimalFraction=trivialEqualities[1],
                             thirdDecimalFraction=trivialEqualities[2], xEquationFractioned=xEquationFractioned,
                             xEquationMonomial=xEquationMonomial, xValue=trivialEqualities[3],
                             questionInequalityXFilled = questionInequalityXFilled, questionInequalitySameDenom=questionInequalitySameDenom,
                             y=aT("y"), yValues=", ".join(map(lambda x : aT(str(x)), satisfyingNumbers)), optionText=optionText,
                             ansValue=aT(ansValue))

    return stem, answer, comment



def rationalandprime211_Stem_038():
    stem = "순환소수 {decimal}에 자연수 {x}를 곱하여 어떤 자연수의 제곱이 되게 하려고 한다. 이 때 가능한 {x}의 값 중 가장 작은 것은?\n① {n1}\n② {n2}\n③ {n3}\n④ {n4}\n⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{decimalEquation}이므로 {x}는 {denom}의 배수이어야 한다. 따라서 가능한 {x}의 값 중 가장 작은 것은 {ansFormula}\n\n"

    # 순환소수 하나를 생성합니다.
    frac, decimal = makeRandomFraction(repeat='yes', repeatMax=2, nonrepeatMax=2, returnDecimal=True)

    # 정답을 구합니다.
    numerator = frac[0]
    denominator = frac[1]

    factoredNumerator = factorint(numerator)
    necessaryFactors = [denominator]

    for prime in factoredNumerator :
        if factoredNumerator[prime] % 2 :
            necessaryFactors.append(prime)

    ansValue = reduce(mul, necessaryFactors)

    # 정답지를 만듭니다.
    ansInd, ansNums = makeChoices(ansValue, diff=4, positive=True)

    # 문제에 사용할 식을 만듭니다
    decimalNumber = makeCorrectDecimalFormula(*decimal)
    fractionFormula = makeFractionFormula(*frac)
    decimalEquation = " ".join([decimalNumber, eq, fractionFormula])
    if len(necessaryFactors) == 1 :
        ansFormula = aT(ansValue)
    else :
        ansFormula = " `times` ".join(map(str, necessaryFactors))
        ansFormula = ansFormula + eq + str(ansValue)

    # 내용을 채웁니다.
    stem = stem.format(decimal=aT(decimalNumber), x=aT('x'),
                       n1 = ansNums[0], n2 = ansNums[1], n3 = ansNums[2], n4 = ansNums[3], n5 = ansNums[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(decimalEquation=aT(decimalEquation), x=aT("x"), denom=aT(str(denominator)), ansFormula=aT(ansFormula))

    return stem, answer, comment


def rationalandprime211_Stem_039():
    stem = "{decimalX}가 유한소수가 되도록 하는 가장 작은 자연수 {x}의 값을 {a}라 하고, 가장 큰 {optionText} 자리 자연수 {x}의 값을 {b}라 할 때, {question}의 값을 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{decimalToFraction}\n따라서 {x}는 {aValue}의 배수이어야 하므로 {aFormula}, {bFormula}\n{ansFormula}\n\n"

    # 순환소수 하나를 생성합니다.
    # print('frac make start')
    frac, decimal = makeRandomFraction(repeat='yes', repeatMax=2, nonrepeatMax=1, returnDecimal=True, minValue=0.2, maxValue=2)
    # print('frac make end')

    # 문제에 사용할 수식을 생성합니다.
    # print('ques form make start')
    questionDict = getRandomEquation(['b', 'a'], coefficientRange=[(1, 3), (-2, 0)], avoidZero=True)
    question=questionDict['text']
    # print('ques form make end')

    # 정답을 구합니다.
    numerator = frac[0]
    denominator = frac[1]

    factoredDenominator = factorint(denominator)
    necessaryFactors = []

    for prime in factoredDenominator :
        if prime != 2 and prime != 5 :
            necessaryFactors.append(prime ** factoredDenominator[prime])

    aValue = reduce(mul, necessaryFactors)
    if aValue >= 50 :
        optionText = "세"
        quotient = 1000 // aValue
    else :
        optionText= "두"
        quotient = 100 // aValue
    bValue = aValue * quotient

    coeffs= questionDict['coeffs']
    variables = [bValue, aValue]
    ansValue = sum([coeffs[i] * variables[i] for i in range(2)])

    # 문제에 사용할 식을 구합니다.
    decimalFormula = makeCorrectDecimalFormula(*decimal)
    fractionFormula = makeFractionFormula(*frac)
    factoredFraction = makeFractionFormula(frac[0], getFactoredIntFormula(denominator))

    decimalX = " ".join([decimalFormula, ts, 'x'])
    decimalToFraction = " ".join([decimalFormula, eq, fractionFormula, eq, factoredFraction])
    aFormula = " ".join(['a', eq, str(aValue)])
    bFormula = " ".join(['b', eq, str(bValue)])
    ansFormula = " ".join(['therefore~', question, eq, str(ansValue)])

    # 내용을 채웁니다.
    stem = stem.format(decimalX=aT(decimalX), x=aT('x'), a=aT("a"), optionText=optionText, b=aT('b'), question=aT(question))
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(decimalToFraction=aT(decimalToFraction), x=aT("x"), aValue=aT(aValue), aFormula=aT(aFormula),
                             bFormula=aT(bFormula), ansFormula=aT(ansFormula))

    return stem, answer, comment


def rationalandprime211_Stem_040():
    stem = "순환소수 {decimal}에 자연수 {A}를 곱하여 어떤 자연수의 제곱이 되게 하려고 한다. 이 때 가능한 {A}의 값 중 가장 작은 {optionText}자연수를 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{decimalEquation}\n따라서 {A}는 {AForm}의 꼴이어야 하므로 가장 작은 {optionText}자연수는 {ansFormula}\n\n"

    # 순환소수 하나를 생성합니다.
    frac, decimal = makeRandomFraction(repeat='yes', repeatMax=1, nonrepeatMax=2, returnDecimal=True, maxValue=4)

    # 정답을 구합니다.
    numerator = frac[0]
    denominator = frac[1]

    factoredNumerator = factorint(numerator)
    necessaryFactors = [denominator]

    for prime in factoredNumerator :
        if factoredNumerator[prime] % 2 :
            necessaryFactors.append(prime)

    minimumRequired = reduce(mul, necessaryFactors)
    if len(str(minimumRequired)) > 3 :
        optionText=  ""
    else :
        optionText = "세 자리의 "

    if minimumRequired >= 100 :
        ansValue = minimumRequired
    else :
        multiplier = 1
        while True :
            temp = minimumRequired
            temp = temp * multiplier ** 2
            if temp >= 100 :
                ansValue = temp
                break
            multiplier += 1

    # 문제에 사용할 식을 만듭니다
    decimalNumber = makeCorrectDecimalFormula(*decimal)
    unreducedFraction = makeFractionFormula(*decimalTupleToFraction(decimal, irreducible=False))
    fractionFormula = makeFractionFormula(*frac)

    factoredFraction = makeFractionFormula(getFactoredIntFormula(numerator), denominator)

    decimalEquationList = [decimalNumber, eq, unreducedFraction]
    if unreducedFraction != fractionFormula :
        decimalEquationList.append(eq)
        decimalEquationList.append(fractionFormula)

    if fractionFormula != factoredFraction :
        decimalEquationList.append(eq)
        decimalEquationList.append(factoredFraction)

    decimalEquation = aT(joinList(decimalEquationList))

    A = aT("A")

    minReqFactored = getFactoredIntFormula(minimumRequired)
    AForm = aT(joinList([minReqFactored, ts, "(자연수)^2"]))

    ansValueFactored = getFactoredIntFormula(ansValue, equalityEnd=True, withTag=True)


    # 내용을 채웁니다.
    stem = stem.format(decimal=aT(decimalNumber), A=A, optionText=optionText)
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(decimalEquation=aT(decimalEquation), A=A, AForm=AForm, optionText=optionText,
                             ansFormula=ansValueFactored)

    return stem, answer, comment


def rationalandprime211_Stem_041():
    stem = "한 자리 자연수 {a}, {b}{aBiggerThanB}에 대하여 두 순환소수 {abDecimal}와 {baDecimal}의 합이 {decimalSum}일 때, 가능한 모든 {questionFormula}의 값 중 가장 큰 것은?\n" \
           "① {n1}\n② {n2}\n③ {n3}\n④ {n4}\n⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{abPlusBaEquation}에서 {fractionedEquation},\n{denomRemovedEquation}, {parenRemovedEquation}, {coeffAEquation}\n" \
              "이 때, {zeroBAInequality}이고 {aEquationInequality}이므로 {aValueEquation}, {bValueEquation}일 때 {questionFormula}의 값이 가장 크다.\n" \
              "{answerEquation}\n\n"

    # a, b의 합을 먼저 구합니다.
    abSum = random.choice(range(3, 18)) # 서로 다른 한 자리 자연수의 합의 최소는 1+2, 최대는 9+8

    # 10a + b - (10b + a) = 9a - 9b = 9(a-b)이므로, 두 수의 차가 가장 큰 쌍이 문제의 답이 됩니다.
    # 반복적으로 값을 확인하면서 가장 차이가 큰 두 수를 구합니다.
    pairs = (0, 0)
    gap = 0
    for possibleA in range(2, 10):
        b = abSum - possibleA
        if b > 0 and possibleA > b :
            possibleDiff = possibleA - b
            if possibleDiff > gap :
                gap = possibleDiff
                pairs = (possibleA, b)

    a, b = pairs

    # 정답지를 만듭니다.
    while True:
        ansIndex, _ansNums = makeChoices(9*(a - b), 9, positive=True, withTag=False)
        # 정답지에 90이 넘는 자연수가 있을 경우 식에 문제가 생기므로 제거합니다.
        satisfied = True
        for num in _ansNums :
            if num >= 90  or num < 1:
                satisfied = False

        if satisfied :
            break

    ansNums = list(map(lambda x: str(x).zfill(2), _ansNums))
    ansNums = list(map(lambda x: makeCorrectDecimalFormula("0.", x), ansNums))

    answerDecimal = ansNums[ansIndex]

    ansNums = list(map(aT, ansNums))

    # 해설 및 문제 지문에 필요한 각종 수식을 만듭니다.
    abDec = ("0.", str(a)+str(b))
    baDec = ("0.", str(b)+str(a))

    abFraction = decimalTupleToFraction(abDec, irreducible=False)
    baFraction = decimalTupleToFraction(baDec, irreducible=False)

    _abFraction = Fraction(*abFraction)
    _baFraction = Fraction(*baFraction)

    _abPlus_ba = _abFraction + _baFraction
    abPlusBaDec = fractionToDecimalTuple(_abPlus_ba.numerator, _abPlus_ba.denominator)

    _abMinus_ba = _abFraction - _baFraction
    abMinusBaDec = fractionToDecimalTuple(_abMinus_ba.numerator, _abMinus_ba.denominator)

    abDecFormula = makeCorrectDecimalFormula(*abDec)
    baDecFormula = makeCorrectDecimalFormula(*baDec)

    abTextFormula = makeCorrectDecimalFormula("0.", "ab")
    baTextFormula = makeCorrectDecimalFormula("0.", "ba")

    aText = aT("a")
    bText = aT("b")

    aBiggerThanB = aT(" ".join(['(', "a ", rs, " b", ")"]))

    abPlusBaDecFormula = makeCorrectDecimalFormula(*abPlusBaDec)

    questionFormula = " ".join([abTextFormula, ms, baTextFormula])

    abPlusBaEquation = " ".join([abTextFormula, ps, baTextFormula, eq, abPlusBaDecFormula])

    abPlusBaFractionFormula = makeFractionFormula(11*abSum, 99)

    tenAplusB = " ".join(['10a', ps, 'b'])
    tenBplusA = " ".join(['10b', ps, 'a'])

    fractionedEquation = " ".join([makeFractionFormula(tenAplusB, '99'), ps, makeFractionFormula(tenBplusA, "99"),
                                   eq, abPlusBaFractionFormula])

    denomRemovedEquation = " ".join(["(", tenAplusB, ")", ps, "(", tenBplusA, ")", eq, str(11*abSum)])
    parenRemovedEquation = " ".join(["11a", eq, str(11*abSum), ms, "11b"])
    coeffAEquation = " ".join(["a", eq, str(abSum), ms, "b"])

    zeroBAInequality = " ".join(["0", rb, "b", rb, "a"])
    aEquationInequality = " ".join([str(abSum), ms, "b", rs, "0"])

    aValueEquation = " ".join(['a', eq, str(a)])
    bValueEquation = " ".join(['b', eq, str(b)])

    answerEquation = " ".join([thus, questionFormula, eq, abDecFormula, ms, baDecFormula, eq, makeFractionFormula(*abFraction),
                               ms, makeFractionFormula(*baFraction), eq, makeFractionFormula(9*(a-b), 99),
                               eq, answerDecimal])

    # 내용을 채웁니다.
    stem = stem.format(a=aText, b=bText, aBiggerThanB = aBiggerThanB, abDecimal=aT(abTextFormula), baDecimal=aT(baTextFormula),
                       decimalSum=aT(abPlusBaDecFormula), questionFormula=aT(questionFormula),
                       n1 = ansNums[0], n2 = ansNums[1], n3 = ansNums[2], n4 = ansNums[3], n5 = ansNums[4])
    answer = answer.format(a1=answer_dict[ansIndex])
    comment = comment.format(abPlusBaEquation=aT(abPlusBaEquation), fractionedEquation=aT(fractionedEquation),
                             denomRemovedEquation=aT(denomRemovedEquation), parenRemovedEquation=aT(parenRemovedEquation),
                             coeffAEquation=aT(coeffAEquation), zeroBAInequality=aT(zeroBAInequality),
                             aEquationInequality=aT(aEquationInequality), aValueEquation=aT(aValueEquation),
                             bValueEquation=aT(bValueEquation), questionFormula=aT(questionFormula),
                             answerEquation=aT(answerEquation))

    return stem, answer, comment


def rationalandprime211_Stem_042():
    stem = "한 자리 자연수 {a}, {b}에 대하여 {xEquation}이면 {givenEquation}일 때, {questionFormula}의 값을 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenEquation}에서 {calculatedEquation}이므로\n{givenFractioned}, {xMinusOneEquation}\n" \
              "{xFracDecEquation}\n" \
              "따라서 {aValueEquation}, {bValueEquation}이므로 {answerEquation}\n\n"

    # 손으로 계산이 가능하고 조건을 만족하는 순환소수를 구합니다.
    while True :
        a, b = random.sample(range(1, 9), k=2)
        nDigit = random.choice(range(1, 10))
        repeatLen = random.choice(range(1, 3))

        if repeatLen > 1 :
            xDecimal = (str(nDigit)+".", str(a)+str(b))
            xTextDecimal = (str(nDigit)+".", "ab")
        else :
            xDecimal = (str(nDigit)+"."+str(a), str(b))
            xTextDecimal = (str(nDigit) + ".a", "b")

        xFraction = decimalTupleToFraction(xDecimal)
        _xFraction = Fraction(*xFraction)

        _givenFraction = 1 / (_xFraction - 1)
        givenDecimal = fractionToDecimalTuple(_givenFraction.numerator, _givenFraction.denominator)

        if (len(givenDecimal[0].split(".")[1]) + len(givenDecimal[1])) < 5 and len(givenDecimal[1]) < 4:
            break

    # 문제 지문과 해설을 만듭니다.
    aText = aT('a')
    bText = aT('b')

    xDecimalFormula = makeCorrectDecimalFormula(*xDecimal)
    givenDecimalFormula = makeCorrectDecimalFormula(*givenDecimal)
    givenFractionFormula = makeFractionFormula(1, "x-1")
    givenFractionValueFormula = makeFractionFormula(_givenFraction.numerator, _givenFraction.denominator)

    xEquation = "x" + eq + makeCorrectDecimalFormula(*xTextDecimal)
    givenEquation = givenFractionFormula + eq + givenDecimalFormula

    questionDict = getRandomEquation(['a', 'b'], realValues=[a, b], avoidZero=True)

    questionFormula = questionDict['text']
    ansValue = questionDict['ansValue']

    calculatedEquationList = [givenDecimalFormula, eq]
    givenFractionUnreduced = decimalTupleToFraction(givenDecimal, irreducible=False)
    if givenFractionUnreduced[1] == _givenFraction.denominator :
        pass
    else :
        # print(givenDecimal, _givenFraction, givenFractionUnreduced)
        calculatedEquationList.append(makeFractionFormula(*givenFractionUnreduced))
        calculatedEquationList.append(eq)

    calculatedEquationList.append(givenFractionValueFormula)
    givenFractioned = " ".join([givenFractionFormula, eq, givenFractionValueFormula])
    xMinusOneEquation = " ".join(['x', ms, '1', eq, makeFractionFormula(_givenFraction.denominator, _givenFraction.numerator)])
    xFracDecEquation = " ".join([thus, 'x', eq, makeFractionFormula(*xFraction), eq, xDecimalFormula])
    aValueEquation = " ".join(['a', eq, str(a)])
    bValueEquation = " ".join(['b', eq, str(b)])
    answerEquation = joinList([questionFormula, eq, ansValue], " ")


    # 내용을 채웁니다.
    stem = stem.format(a=aText, b=bText, xEquation=aT(xEquation), givenEquation=aT(givenEquation), questionFormula=aT(questionFormula))
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(givenEquation=aT(givenEquation), calculatedEquation=aT(" ".join(calculatedEquationList)),
                             givenFractioned=aT(givenFractioned), xMinusOneEquation=aT(xMinusOneEquation),
                             xFracDecEquation=aT(xFracDecEquation), aValueEquation=aT(aValueEquation), bValueEquation=aT(bValueEquation),
                             answerEquation=aT(answerEquation))

    return stem, answer, comment


def rationalandprime211_Stem_043():
    stem = "어떤 자연수 {A}에 {correctValue}{postp} 곱해야 하는데 잘못하여 {wrongValue}{postp} 곱했더니 " \
           "그 결과가 바르게 계산한 값보다 {diff}만큼 크게 되었다. 자연수 {A}의 값을 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n주어진 조건을 식으로 나타내면 {conditionEquation}  --- ㉠\n" \
              "이 때 {repeatingDecimalEquation}이므로 ㉠에서 {conditionEquationFractioned}\n" \
              "{conditionEquationSimplified}, {conditionAOnly} {AEquation}\n\n"

    # 손으로 계산이 가능하고 조건을 만족하는 순환소수를 구합니다.
    a, b = random.sample(range(1, 9), k=2)
    nDigit = random.choice(range(1, 10))
    # repeatLen = random.choice(range(1, 3))

    # if repeatLen > 1 :
    #     repeatingDecimal = (str(nDigit)+".", str(a)+str(b))
    # else :
    repeatingDecimal = (str(nDigit)+"."+str(a), str(b))

    nonrepeatingDecimal = (str(nDigit)+"."+str(a)+str(b), "")
    repeatingDecimalFraction = decimalTupleToFraction(repeatingDecimal, irreducible=False)
    nonrepeatingDecimalFraction = decimalTupleToFraction(nonrepeatingDecimal, irreducible=False)
    _repeatingDecimalFraction = Fraction(*repeatingDecimalFraction)
    _nonrepeatingDecimalFraction = Fraction(*nonrepeatingDecimalFraction)

    repeatingDecimalFractionFormula = makeFractionFormula(_repeatingDecimalFraction.numerator, _repeatingDecimalFraction.denominator)
    nonrepeatingDecimalFractionFormula = makeFractionFormula(_nonrepeatingDecimalFraction.numerator, _nonrepeatingDecimalFraction.denominator)

    A = random.choice(range(5, 65, 5))

    _diff = _repeatingDecimalFraction * A - _nonrepeatingDecimalFraction * A
    diffFractionFormula = makeFractionFormula(_diff.numerator, _diff.denominator)

    postp = proc_jo(b, 1)

    # 문제 지문과 해설을 만듭니다.
    AText = "A"
    A_Text = aT("A")
    correctValue = makeCorrectDecimalFormula(*nonrepeatingDecimal)
    wrongValue = makeCorrectDecimalFormula(*repeatingDecimal)
    diffDecimal = fractionToDecimalTuple(_diff.numerator, _diff.denominator)
    diffDecimalFormula = makeCorrectDecimalFormula(*diffDecimal)

    conditionEquation = joinList([AText, ts, wrongValue, ms, AText, ts, correctValue, eq, diffDecimalFormula])
    repeatingDecimalEquationList = [wrongValue, eq]
    if repeatingDecimalFraction[1] == _repeatingDecimalFraction.denominator:
        pass
    else :
        repeatingDecimalEquationList.append(makeFractionFormula(*repeatingDecimalFraction))
        repeatingDecimalEquationList.append(eq)
    repeatingDecimalEquationList.append(repeatingDecimalFractionFormula)

    conditionEquationFractioned = joinList([AText, ts, repeatingDecimalFractionFormula, ms, AText, ts, nonrepeatingDecimalFractionFormula,
                                            eq, diffFractionFormula])

    leastCommonMultiplier = lcm(lcm(_repeatingDecimalFraction.denominator, _nonrepeatingDecimalFraction.denominator), _diff.denominator)

    repeatingMultiplied = _repeatingDecimalFraction * leastCommonMultiplier
    nonrepeatingMultiplied = _nonrepeatingDecimalFraction * leastCommonMultiplier
    diffMultiplied = _diff * leastCommonMultiplier

    conditionEquationSimplified = joinList([repeatingMultiplied.numerator, AText, ms, nonrepeatingMultiplied.numerator, AText,
                                            eq, diffMultiplied.numerator])

    coeff = repeatingMultiplied.numerator - nonrepeatingMultiplied.numerator

    conditionAOnlyList = []
    if coeff != 1 :
        conditionAOnlyList.append(coeff)
    else :
        conditionAOnlyList.append(thus)

    conditionAOnlyList.extend([AText, eq, diffMultiplied.numerator])
    conditionAOnly = joinList(conditionAOnlyList)

    if coeff != 1 :
        AEquation = aT(joinList([thus, AText, eq, diffMultiplied.numerator // coeff]))
    else :
        AEquation = ""





    # 내용을 채웁니다.
    stem = stem.format(correctValue=aT(correctValue), postp=postp, wrongValue=aT(wrongValue), diff=aT(diffDecimalFormula), A=A_Text)
    answer = answer.format(a1=A)
    comment = comment.format(conditionEquation=aT(conditionEquation), repeatingDecimalEquation=aT(joinList(repeatingDecimalEquationList)),
                             conditionEquationFractioned=aT(conditionEquationFractioned),
                             conditionEquationSimplified=aT(conditionEquationSimplified),
                             conditionAOnly=aT(conditionAOnly), AEquation=AEquation)

    return stem, answer, comment


def rationalandprime211_Stem_044():
    stem = "한 자리 자연수 {a}, {b}에 대하여 {definition}라 하자. {questionFormula}일 때, {A}의 값을 순환소수로 나타내면?\n" \
           "① {n1}   ② {n2}   ③ {n3}   ④ {n4}   ⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{questionCalculated}\n{answerFormula}\n\n"

    # 한 자리 자연수끼리의 곱을 먼저 구합니다.
    while True :
        largeA, multiplier = random.sample(range(2, 9), k=2)
        value = largeA * multiplier
        if value > 10 and value % 10 :
            break

    a, b = divmod(value, 10)

    aTextDecimal = ("0.", "a")
    aDecimal = ("0.", str(a))
    aDecimalFormula = makeCorrectDecimalFormula(*aDecimal)
    aTextDecimalFormula = makeCorrectDecimalFormula(*aTextDecimal)
    aFraction = (a, 9)
    aFractionFormula = makeFractionFormula(*aFraction)

    bTextDecimal = ("0.", '0b')
    bDecimal = ("0.", "0"+str(b))
    bDecimalFormula = makeCorrectDecimalFormula(*bDecimal)
    bTextDecimalFormula = makeCorrectDecimalFormula(*bTextDecimal)
    bFraction = (b, 90)
    bFractionFormula = makeFractionFormula(*bFraction)

    largeAFrac = (largeA, 90)
    largeAFractionFormula = makeFractionFormula(*largeAFrac)
    largeADec = fractionToDecimalTuple(*largeAFrac)
    largeADecFormula = makeCorrectDecimalFormula(*largeADec)

    firstDecimals = generateDecimalTuples('0', '0', str(largeA))
    firstDecimals.pop(3)
    firstDecimals.pop(1)

    secondDecimals = generateDecimalTuples('0','1', str(largeA))
    firstDecimals.append(secondDecimals[0])

    random.shuffle(firstDecimals)

    ansInd = random.choice(range(5))
    firstDecimals.insert(ansInd, largeADec)

    choiceDecimals = list(map(lambda x : makeCorrectDecimalFormula(*x, withTag=True), firstDecimals))

    # 문제 지문과 해설을 만듭니다.
    definition = " ".join(["(a,~b)", eq, aTextDecimalFormula, ps, bTextDecimalFormula])
    questionFormula = joinList(["(", a, ",~", b, ")", eq, multiplier, "A"])

    questionCalculated = joinList(["(", a, ",~", b, ")", eq, aDecimalFormula, ps, bDecimalFormula, eq,
                                   aFractionFormula, ps, bFractionFormula, eq, makeFractionFormula(value, 90), eq, multiplier, ts, largeAFractionFormula])
    answerFormula = joinList([thus, "A", eq, largeAFractionFormula, eq, largeADecFormula])

    # 내용을 채웁니다.
    stem = stem.format(a=aT("a"), b=aT("b"), definition=aT(definition), questionFormula=aT(questionFormula), A=aT("A"),
                       n1=choiceDecimals[0], n2=choiceDecimals[1], n3=choiceDecimals[2],
                       n4=choiceDecimals[3], n5=choiceDecimals[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(questionCalculated=aT(questionCalculated), answerFormula=aT(answerFormula))

    return stem, answer, comment



def rationalandprime211_Stem_045():
    stem = "다음 중 옳지 않은 것은?\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{ansNum} {c1}\n\n"

    set1 = ["어떤 무한소수는 순환소수이다.",
            ["모든 무한소수는 순환소수이다.", "어떤 무한소수는 순환소수로 나타낼 수 없다."]]
    set2 = ["어떤 무한소수는 순환소수가 아니다.",
            ["모든 무한소수는 순환소수가 아니다.", "유리수인 무한소수는 모두 순환소수이다"]]
    set3 = ["모든 순환소수는 유리수이다.",
            ["어떤 순환소수는 유리수가 아니다.", "모든 순환소수는 유리수이다."]]
    set4 = ["모든 유한소수는 유리수이다.",
            ["어떤 유한소수는 유리수가 아니다.", "모든 유한소수는 유리수이다."]]
    set5 = ["어떤 무한소수는 유리수가 아니다.",
            ["모든 무한소수는 유리수이다.", "어떤 무한소수는 유리수가 아니다."]]
    set6 = ["모든 순환소수는 무한소수이다.",
            ["어떤 순환소수는 무한소수가 아니다.", "모든 순환소수는 무한소수이다."]]
    set7 = ["정수가 아닌 유리수 중 유한소수로 나타낼 수 없는 것은 순환소수로 나타낼 수 있다.",
            ["어떤 정수는 유한소수로 나타낼 수 없다.", "모든 정수는 유한소수로 나타낼 수 있다"]]
    set8 = ["어떤 유리수는 유한소수로 나타낼 수 있다.",
            ["모든 유리수는 유한소수로 나타낼 수 있다.", "어떤 유리수는 유한소수로 나타낼 수 없다"]]
    set9 = ["모든 유한소수는 분모가 10의 거듭제곱인 분수로 나타낼 수 있다.",
            ["어떤 순환소수는 분모가 10의 거듭제곱인 분수로 나타낼 수 있다.", "모든 순환소수는 분모가 10의 거듭제곱인 분수로 나타낼 수 없다."]]
    set10 = ["모든 순환소수는 분수로 나타낼 수 있다.",
             ["어떤 순환소수는 분수로 나타낼 수 없다.", "모든 순환소수는 분수로 나타낼 수 있다."]]
    set11 = ["기약분수의 분모의 소인수가 2 또는 5뿐이면 유한소수로 나타낼 수 있다.",
             ["기약분수는 모두 유한소수로 나타낼 수 있다.", "모든 기약분수를 유한소수로 나타낼 수 있는 것은 아니다."]]
    set12 = ["0은 유리수이다.", ["0은 유리수가 아니다.", "0은 유리수이다."]]

    allSets = [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12]

    ansInd = random.choice(range(5))
    _choices = random.sample(allSets, k=5)
    choices = []

    for ind, setItem in enumerate(_choices) :
        if ind == ansInd :
            choices.append(setItem[1][0])
            c1 = setItem[1][1]
        else :
            choices.append(setItem[0])


    # 내용을 채웁니다.
    stem = stem.format(s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(ansNum=answer_dict[ansInd], c1=c1)

    return stem, answer, comment


def rationalandprime211_Stem_046():
    stem = "다음 중 옳은 것을 보기에서 모두 고른 것은?\n\n[보기]\n" \
           "   ㄱ. {s1}\n   ㄴ. {s2}\n   ㄷ. {s3}\n   ㄹ. {s4}\n\n" \
           "① {n1}\n② {n2}\n③ {n3}\n④ {n4}\n⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{wrongItems}\n\n"

    set1 = ["어떤 무한소수는 순환소수이다.",
            ["모든 무한소수는 순환소수이다.", "어떤 무한소수는 순환소수로 나타낼 수 없다."]]
    set2 = ["어떤 무한소수는 순환소수가 아니다.",
            ["모든 무한소수는 순환소수가 아니다.", "유리수인 무한소수는 모두 순환소수이다."]]
    set3 = ["모든 순환소수는 유리수이다.",
            ["어떤 순환소수는 유리수가 아니다.", "모든 순환소수는 유리수이다."]]
    set4 = ["모든 유한소수는 유리수이다.",
            ["어떤 유한소수는 유리수가 아니다.", "모든 유한소수는 유리수이다."]]
    set5 = ["어떤 무한소수는 유리수가 아니다.",
            ["모든 무한소수는 유리수이다.", "어떤 무한소수는 유리수가 아니다."]]
    set6 = ["모든 순환소수는 무한소수이다.",
            ["어떤 순환소수는 무한소수가 아니다.", "모든 순환소수는 무한소수이다."]]
    set7 = ["정수가 아닌 유리수 중 유한소수로 나타낼 수 없는 것은 순환소수로 나타낼 수 있다.",
            ["어떤 정수는 유한소수로 나타낼 수 없다.", "모든 정수는 유한소수로 나타낼 수 있다."]]
    set8 = ["어떤 유리수는 유한소수로 나타낼 수 있다.",
            ["모든 유리수는 유한소수로 나타낼 수 있다.", "어떤 유리수는 유한소수로 나타낼 수 없다."]]
    set9 = ["모든 유한소수는 분모가 10의 거듭제곱인 분수로 나타낼 수 있다.",
            ["어떤 순환소수는 분모가 10의 거듭제곱인 분수로 나타낼 수 있다.", "모든 순환소수는 분모가 10의 거듭제곱인 분수로 나타낼 수 없다."]]
    set10 = ["모든 순환소수는 분수로 나타낼 수 있다.",
             ["어떤 순환소수는 분수로 나타낼 수 없다.", "모든 순환소수는 분수로 나타낼 수 있다."]]
    set11 = ["기약분수의 분모의 소인수가 2 또는 5뿐이면 유한소수로 나타낼 수 있다.",
             ["기약분수는 모두 유한소수로 나타낼 수 있다.", "모든 기약분수를 유한소수로 나타낼 수 있는 것은 아니다."]]
    set12 = ["0은 유리수이다.", ["0은 유리수가 아니다.", "0은 유리수이다."]]

    allSets = [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12]

    oneItems = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ']
    twoItems = ['ㄱ, ㄴ', 'ㄱ, ㄷ', 'ㄱ, ㄹ', 'ㄴ, ㄷ', 'ㄴ, ㄹ', 'ㄷ, ㄹ']
    threeItems = ['ㄱ, ㄴ, ㄷ', 'ㄱ, ㄴ, ㄹ', 'ㄱ, ㄷ, ㄹ', 'ㄴ, ㄷ, ㄹ']

    items = [oneItems, twoItems, threeItems]

    selectionCharacters = {0: 'ㄱ', 1: 'ㄴ', 2: 'ㄷ', 3: 'ㄹ'}

    howManyCorrects = random.choice(range(1, 4))
    corrects = random.sample(range(4), k=howManyCorrects)

    corrects.sort()

    structs = [(2, 2, 0), (0, 2, 2)]
    struct = random.choice(structs)

    ansChars = ", ".join([selectionCharacters[x] for x in corrects])

    selects = []
    for i, s in enumerate(struct) :
        if howManyCorrects-1 == i :
            if s == 0 :
                temp = [ansChars]
            else :
                while True :
                    temp = random.sample(items[i], k=s)
                    if ansChars not in temp :
                        break
                temp.append(ansChars)
                temp.sort()
        else :
            temp = random.sample(items[i], k=s)
            temp.sort()
        selects.extend(temp)

    ansInd = selects.index(ansChars)

    _choices = random.sample(allSets, k=4)
    choices = []
    comments = []

    for ind, setItem in enumerate(_choices) :
        if ind not in corrects :
            choices.append(setItem[1][0])
            comments.append(selectionCharacters[ind] + ". " + setItem[1][1])
        else :
            choices.append(setItem[0])


    # 내용을 채웁니다.
    stem = stem.format(s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3],
                       n1=selects[0], n2=selects[1], n3=selects[2], n4=selects[3], n5=selects[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(wrongItems = "\n".join(comments))

    return stem, answer, comment


def rationalandprime211_Stem_047():
    stem = "다섯 명의 학생이 소수에 대하여 이야기를 나누고 있다. 바르게 이야기한 학생을 모두 고르면? (정답 2개)\n① 선우: {s1}\n② 민주: {s2}\n③ 지민: {s3}\n④ 현지: {s4}\n⑤ 철수: {s5}\n"
    answer = "(답): {a1}, {a2}\n"
    comment = "(해설)\n{wrongNum1} {c1}\n{wrongNum2} {c2}\n{wrongNum3} {c3}\n\n"

    set1 = ["어떤 무한소수는 순환소수야",
            ["모든 무한소수는 순환소수가 아니야.", "어떤 무한소수는 순환소수로 나타낼 수 없다."]]
    set2 = ["어떤 무한소수는 순환소수가 아니야.",
            ["모든 무한소수는 순환소수가 아니야.", "유리수인 무한소수는 모두 순환소수이다"]]
    set3 = ["모든 순환소수는 유리수야.",
            ["어떤 순환소수는 유리수가 아니야.", "모든 순환소수는 유리수이다."]]
    set4 = ["모든 유한소수는 유리수야.",
            ["어떤 유한소수는 유리수가 아니야.", "모든 유한소수는 유리수이다."]]
    set5 = ["어떤 무한소수는 유리수가 아니야.",
            ["모든 무한소수는 유리수야.", "어떤 무한소수는 유리수가 아니다."]]
    set6 = ["모든 순환소수는 무한소수야.",
            ["어떤 순환소수는 무한소수가 아니야.", "모든 순환소수는 무한소수이다."]]
    set7 = ["정수가 아닌 유리수 중 유한소수로 나타낼 수 없는 것은 순환소수로 나타낼 수 있어.",
            ["어떤 정수는 유한소수로 나타낼 수 없어.", "모든 정수는 유한소수로 나타낼 수 있다"]]
    set8 = ["어떤 유리수는 유한소수로 나타낼 수 있어.",
            ["모든 유리수는 유한소수로 나타낼 수 있어.", "어떤 유리수는 유한소수로 나타낼 수 없다"]]
    set9 = ["모든 유한소수는 분모가 10의 거듭제곱인 분수로 나타낼 수 있어.",
            ["어떤 순환소수는 분모가 10의 거듭제곱인 분수로 나타낼 수 있어.", "모든 순환소수는 분모가 10의 거듭제곱인 분수로 나타낼 수 없다."]]
    set10 = ["모든 순환소수는 분수로 나타낼 수 있어.",
             ["어떤 순환소수는 분수로 나타낼 수 없어.", "모든 순환소수는 분수로 나타낼 수 있다."]]
    set11 = ["기약분수의 분모의 소인수가 2 또는 5뿐이면 유한소수로 나타낼 수 있어.",
             ["기약분수는 모두 유한소수로 나타낼 수 있어.", "모든 기약분수를 유한소수로 나타낼 수 있는 것은 아니다."]]
    # set12 = ["0은 유리수이다.", ["0은 유리수가 아니다.", "0은 유리수이다."]]

    allSets = [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11]

    ansInds = sorted(random.sample(range(5), k=2))
    wrongInds =[]
    _choices = random.sample(allSets, k=5)
    choices = []
    comments = []
    for ind, setItem in enumerate(_choices) :
        if ind not in ansInds :
            choices.append(setItem[1][0])
            comments.append(setItem[1][1])
            wrongInds.append(ind)
        else :
            choices.append(setItem[0])

    # 내용을 채웁니다.
    stem = stem.format(s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInds[0]], a2=answer_dict[ansInds[1]])
    comment = comment.format(wrongNum1=answer_dict[wrongInds[0]], c1=comments[0],
                             wrongNum2=answer_dict[wrongInds[1]], c2=comments[1],
                             wrongNum3=answer_dict[wrongInds[2]], c3=comments[2])

    return stem, answer, comment


def rationalandprime211_Stem_048():
    stem = "다음 중 옳은 것은?\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}\n\n"

    a = symbols('a', positive=True)
    basicStruct = "a**{e1} / a**{e2}"

    wrongTypes = []

    # wrongType1 : divisors
    temp1 = random.choice([6, 8, 10, 12, 16])
    temp1Divisors = divisors(temp1)
    temp2 = random.choice(temp1Divisors[1:-1])
    temp3 = temp1 // temp2
    type1 = basicStruct.format(e1=str(temp1), e2=str(temp2))
    type1Hangul = convertIntoHangul(type1, slashToDiv=True)
    type1Choice = joinList([type1Hangul, eq, "a**", temp3])

    correctTemp3 = temp1 - temp2
    correctType1 = joinList([type1Hangul, eq, "a**{", temp1, ms, temp2, "}", eq, "a**", correctTemp3])

    wrongTypes.append((type1Choice, correctType1))

    # wrongType2 : wrong negative exponent
    while True :
        temp1, temp2 = sorted(random.sample(range(2, 12), k=2))
        temp3 = temp2 - temp1
        if temp3 != 1 :
            break
    type2 = basicStruct.format(e1=str(temp1), e2=str(temp2))
    type2Hangul = convertIntoHangul(type2, slashToDiv=True)
    type2Choice = joinList([type2Hangul, eq, "a**", temp3])

    correctType2 = joinList([type2Hangul, eq, "1 over a**{", temp2, ms, temp1, "}", eq, "1 over a**", temp3])

    wrongTypes.append((type2Choice, correctType2))

    # wrongType3 : wrong division of same exponent
    temp1 = random.choice(range(3, 9))
    type3 = basicStruct.format(e1=str(temp1), e2=str(temp1))
    type3Hangul = convertIntoHangul(type3, slashToDiv=True)
    type3Choice = joinList([type3Hangul, eq, "a"])

    correctType3 = joinList([type3Hangul, eq, "1"])

    wrongTypes.append((type3Choice, correctType3))

    # wrongType4 : wrong division
    while True :
        temp1, temp2 = sorted(random.sample(range(2, 12), k=2))
        temp3 = temp2 - temp1
        if temp3 != 1 :
            break
    type4 = basicStruct.format(e1=str(temp2), e2=str(temp1))
    type4Hangul = convertIntoHangul(type4, slashToDiv=True)
    type4Choice = joinList([type4Hangul, eq, "1 / a**", temp3])

    correctType4 = joinList([type4Hangul, eq, "a**{", temp2, ms, temp1, "}", eq, "a**", temp3])

    wrongTypes.append((type4Choice, correctType4))

    # right answer
    ansInd = random.choice(range(5))
    temp1, temp2 = random.sample(range(2, 12), k=2)
    type5 = basicStruct.format(e1=str(temp1), e2=str(temp2))
    type5Hangul = convertIntoHangul(type5, slashToDiv=True)
    res = sympify(type5)
    if temp1 < temp2 :
        res = convertNegExp(res)
        correctComment = joinList(["1 over a**{", temp2, ms, temp1, "}"])
    else :
        correctComment = joinList(["a**{", temp1, ms, temp2, "}"])

    correctFormula = joinList([type5Hangul, eq, res])
    correctFormulaComment = joinList([type5Hangul, eq, correctComment, eq, res])

    random.shuffle(wrongTypes)
    wrongTypes.insert(ansInd, (correctFormula, correctFormulaComment))

    choices = list(map(lambda x : aT(convertIntoHangul(x[0])), wrongTypes))
    comments = list(map(lambda x : aT(convertIntoHangul(x[1])), wrongTypes))

    for i, c in enumerate(comments) :
        if i == ansInd :
            comments[i] = comments[i] + " (참)"
        else :
            comments[i] = comments[i] + " (거짓)"

    stem = stem.format(s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(c1=comments[0], c2=comments[1], c3=comments[2], c4=comments[3], c5=comments[4])

    return stem, answer, comment


def rationalandprime211_Stem_049():
    stem = "{questionEquation}일 때, {xyzFormula}의 값은? (단, {x}, {y}, {z}는 자연수이다)\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{commentText1}\n{commentText2}\n{commentText3}\n{commentText4}\n\n"

    # 문제에 필요한 여러 요소들을 생성합니다.
    twos = [2, 4, 8, 16]
    threes = [3, 9, 27]
    fives = [5, 25]
    others = [6, 9, 10, 12, 15, 18, 20]

    chosenNumbers = []
    chosenNumbers.append(random.choice(twos))
    chosenNumbers.append(random.choice(threes))
    chosenNumbers.append(random.choice(fives))
    chosenNumbers.extend(random.sample(others, k=2))

    chosenNumbers.sort()

    givenMultiplication = joinList(chosenNumbers, ts)
    givenxyz = joinList(["2^x", "3^y", "5^z"], ts)

    value = reduce(mul, chosenNumbers)
    valueFactored = factorint(value)
    valueFactoredText = getFactoredIntFormula(value)
    xVal = valueFactored[2]
    yVal = valueFactored[3]
    zVal = valueFactored[5]

    operators = ["+", "-", "*"]
    operator1 = random.choice(operators)
    operator2 = random.choice(operators)

    xyzText = joinList(['x', operator1, 'y', operator2, 'z'])
    xyzSympy = sympify(xyzText)
    xyzFormula = convertIntoHangul(xyzText)
    xyzSubs = xyzText.replace('x', str(xVal))
    xyzSubs = xyzSubs.replace("y", str(yVal))
    xyzSubs = xyzSubs.replace('z', str(zVal))
    xyzSubsText = convertIntoHangul(xyzSubs, leaveTimes=True)

    ansValue = int(str(xyzSympy.subs([('x', xVal), ('y', yVal), ('z', zVal)])))

    # 문제와 해설에 들어갈 수식을 생성합니다.
    questionEquation = joinList([givenMultiplication, eq, givenxyz])

    givenFactoredTextList = []
    for num in chosenNumbers :
        numFactored = factorint(num, multiple=True)
        numText = joinList(numFactored, ts)
        if len(numFactored) > 1 :
            numText = joinList(["(", numText, ")"])
        givenFactoredTextList.append(numText)

    givenFactoredText = joinList(givenFactoredTextList, ts)

    commentText1 = joinList([aT(givenMultiplication), "\n", aT(eq + givenFactoredText)])
    commentText2 = joinList([valueFactoredText, eq, givenxyz])
    xyzEquations = makeEquality(['x', 'y', 'z'], [xVal, yVal, zVal])
    commentText3 = aT(thus) + ", ".join(map(aT, xyzEquations))
    commentText4 = joinList([thus, xyzFormula, eq, xyzSubsText, eq, str(ansValue)])

    ansInd, choices = makeChoices(ansValue, withTag=True)

    stem = stem.format(questionEquation=aT(questionEquation), xyzFormula=aT(xyzFormula), x=aT("x"), y=aT("y"), z=aT("z"),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(commentText1=commentText1, commentText2=aT(commentText2), commentText3=commentText3,
                             commentText4=aT(commentText4))

    return stem, answer, comment


def rationalandprime211_Stem_050():
    stem = "{questionEquation}을 만족시키는 {x}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{commentText1}\n즉, {commentText2}이므로\n{commentText3}\n{commentText4}\n\n"

    # 문제에 필요한 여러 요소들을 생성합니다.
    basis1 = [2, 3, 5]
    basis2 = [4, 6, 7, 8, 9, 10]
    bases = [basis1, basis2]

    # thinking, n(ax+b) = m(cx+d), first decide n and m
    exp1 = [1, 2, 3]
    exp2 = [1, 2]
    exps = [exp1, exp2]

    # 어떤 쪽의 짝을 이용할지 정합니다.
    which = random.choice(range(2))
    base = random.choice(bases[which])
    n, m = sorted(random.sample(exps[which], k=2))

    left_text = "a*x+b"
    right_text = "c*x+d"
    coeff_x_text = "n*a - m*c"
    constant_text = "m*d - n*b"

    # first, decide c
    cVal = random.choice(range(1, 3))
    mc = m * cVal
    smallestA = mc // n + 1
    aVal = random.choice(range(smallestA, smallestA+2))

    coeff_x_val = n * aVal - mc

    if n==1 or coeff_x_val % n :
        bVal = random.choice(range(coeff_x_val, coeff_x_val*4, coeff_x_val))
    else :
        bVal = random.choice(range(1, 5))
    smallestD = n*bVal // m + 1
    count = random.choice(range(1, 5))
    while True :
        constant_val = m * smallestD - n * bVal
        # print(constant_val, coeff_x_val, "m", m, "n", n, "b", bVal)
        if constant_val % coeff_x_val :
            smallestD += 1
        else :
            count -= 1
            if not count :
                dVal = smallestD
                break
            else :
                smallestD += 1



    xVal = constant_val // coeff_x_val

    leftBase = base**n
    rightBase = base**m

    leftSubs = left_text.replace('a', str(aVal))
    leftSubs = leftSubs.replace('b', str(bVal))

    rightSubs = right_text.replace('c', str(cVal))
    rightSubs = rightSubs.replace('d', str(dVal))

    leftExp = convertIntoHangul(str(sympify(leftSubs)), removeSpace=True)
    rightExp = convertIntoHangul(str(sympify(rightSubs)), removeSpace=True)

    questionEquation = joinList([leftBase, pw, leftExp, eq, rightBase, pw, rightExp])

    commentText1List = []
    if n != 1 :
        leftNSubs = left_text.replace('a', str(n*aVal))
        leftNSubs = leftNSubs.replace("b", str(n*bVal))
        leftNExp = convertIntoHangul(str(sympify(leftNSubs)), removeSpace=True)
        tempText = joinList([leftBase, pw, leftExp, eq, "(", base, pw, n, ")", pw, leftExp, eq, base, pw, leftNExp])
        commentText1List.append(tempText)
    else :
        leftNExp = leftExp
    if m != 1 :
        rightNSubs = right_text.replace("c", str(m*cVal))
        rightNSubs = rightNSubs.replace("d", str(m*dVal))
        rightNExp = convertIntoHangul(str(sympify(rightNSubs)), removeSpace=True)
        tempText = joinList([rightBase, pw, rightExp, eq, "(", base, pw, m, ")", pw, rightExp, eq, base, pw, rightNExp])
        commentText1List.append(tempText)
    else :
        rightNExp = rightExp

    commentText1 = joinList(map(aT, commentText1List), "\n")
    commentText2 = joinList([base, pw, leftNExp, eq, base, pw, rightNExp])
    commentText3 = joinList([leftNExp, eq, rightNExp])
    commentText4 = joinList([thus, "x", eq, xVal])

    ansInd, choices = makeChoices(xVal, withTag=True)

    stem = stem.format(questionEquation=aT(questionEquation), x=aT("x"),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(commentText1=commentText1, commentText2=aT(commentText2), commentText3=aT(commentText3),
                             commentText4=aT(commentText4))

    return stem, answer, comment


def rationalandprime211_Stem_051():
    stem = "다음 네 수를 작은 것부터 순서대로 나열하면?\n" \
           "   ㄱ. {n1}   ㄴ. {n2}   ㄷ. {n3}   ㄹ. {n4}\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{exponents}의 최대공약수는 {gcd}이므로\n{n1Equation}, {n2Equation}\n{n3Equation}, {n4Equation}\n" \
              "따라서 {orderedInequality}이므로 작은 것부터 순서대로 나열하면 {answerOrderNumber}이므로 답은 {a1}이다.\n\n"

    # 문제에 필요한 여러 요소들을 생성합니다.

    # 비교가 의미가 있는 범위의 숫자를 정합니다.
    sets = {
        2 : [[3], [5, 6], range(10, 41)],
        3 : [[4, 5], [7, 8, 10, 11, 12, 13], range(60, 171)],
        4 : [[6, 7], [14, 15, 17, 18, 19, 20], range(200, 401)]
    }

    # 동일한 밑을 가지거나 계산 결과값이 동일한 경우를 제외하고 숫자를 뽑습니다.
    showingBases = []
    cardinalBases = []
    base4 = random.choice(list(sets.keys()))
    showingBases.append(base4**4)
    cardinalBases.append(base4)
    base3 = random.choice(sets[base4][0])
    showingBases.append(base3**3)
    cardinalBases.append(base3)
    while True :
        base2 = random.choice(sets[base4][1])
        val = base2**2
        if val in showingBases or base2 in cardinalBases:
            continue
        else :
            showingBases.append(val)
            cardinalBases.append(base2)
            break
    while True :
        base1 = random.choice(sets[base4][2])
        val = base1
        if val in showingBases or base1 in cardinalBases:
            continue
        else :
            showingBases.append(val)
            cardinalBases.append(base1)
            break

    # 최대공약수가 되는 지수를 구합니다.
    baseExp = random.choice(range(10, 55, 5))

    # 실제 보여질 밑과 기저가 되는 밑을 리스트로 정리합니다.
    bases = [(showingBases[0], base4, 4), (showingBases[1], base3, 3), (showingBases[2], base2, 2), (showingBases[3], base1, 1)]

    # 문제에서 숫자가 보여질 순서를 정합니다.
    showingOrderIndex = random.sample(range(4), k=4)

    # 보여지는 순서대로 밑을 정렬합니다.
    showingOrderBases = [showingBases[x] for x in showingOrderIndex]

    # 보여지는 순서대로 정렬된 밑에 대해서 값이 작은 순서대로 정렬합니다.
    # 그리고 보여지는 순서대로 되어 있는 리스트의 인덱스를 함께 저장합니다.
    sortedBases = sorted([(val, ind) for ind, val in enumerate(showingOrderBases)])

    # 정답이 되는 순서를 찾습니다.
    answerOrderIndex = [sortedBases[x][1] for x in range(4)]

    # 문제와 해설에 필요한 숫자 식을 만듭니다.
    # 보여지는 순서대로 값을 채웁니다.
    numbersForQuestion = []
    numbersForComment = []
    for ind in showingOrderIndex :
        tup = bases[ind]
        questionText = joinList([tup[1], pw, tup[2] * baseExp], "")
        commentText = joinList([tup[0], pw, baseExp], "")
        numbersForQuestion.append(questionText)
        numbersForComment.append(commentText)
    #
    # print(numbersForQuestion)
    # print(numbersForComment)

    # 선택지를 만들기 위해 정답인 순서를 먼저 저장합니다.
    choiceOrderIndices = [answerOrderIndex]

    # 그리고 랜덤하게 4가지 경우의 수를 추가합니다.
    # 이 때 정답과 겹치지 않도록 합니다.
    for _ in range(4):
        while True :
            temp = random.sample(range(4), k=4)
            if temp not in choiceOrderIndices :
                choiceOrderIndices.append(temp)
                break

    # 정답인 순서가 실제 선지에 위치할 곳을 뽑습니다.
    ansInd = random.choice(range(5))

    # 선지 모음에 정답인 순서를 위의 뽑은 값에 맞추어 집어 넣습니다.
    choiceOrderIndices = choiceOrderIndices[1:]
    choiceOrderIndices.insert(ansInd, answerOrderIndex)

    # 위에서 만들어진 선지 인덱스에 맞추어 ㄱㄴㄷㄹ을 배열하여 실제 선지를 만듭니다.
    choices = []
    for indexList in choiceOrderIndices :
        temp = []
        for ind in indexList :
            temp.append(answer_kodict[ind])
        tempText = ", ".join(temp)
        choices.append(tempText)

    # 해설의 최대공약수를 구하는 해설 부분에서 사용할 지수들을 문제에서 보여지는 순서대로 모읍니다.
    exps = []
    for ind in showingOrderIndex :
        temp = aT(bases[ind][2]*baseExp)
        exps.append(temp)

    # 대소 비교를 위해 지수를 통일하는 과정에서 일부 계산이 필요한 경우를 체크하여 해설용으로 텍스트를 만듭니다.
    # 역시나 보여지는 순서대로 텍스트를 생성합니다.
    comments = []
    for ind in range(4):
        tup = bases[showingOrderIndex[ind]]
        if tup[2] != 1 :
            temp = joinList([numbersForQuestion[ind], eq, "(", tup[1], pw, tup[2], ")", pw, baseExp, eq, numbersForComment[ind]])
            comments.append(temp)
        else :
            comments.append(numbersForQuestion[ind])

    # 이제, 작은 순서대로 정렬된 부등식을 만듭니다.
    orderedInequality = joinList([numbersForComment[ind] for ind in answerOrderIndex],  " " + rb + " ")

    # 마지막으로, 작은 순서대로 정렬된 숫자 식을 만듭니다.
    answerOrderNumber = joinList([aT(numbersForQuestion[ind]) for ind in answerOrderIndex], ", ")

    # 내용을 채워 넣습니다.
    stem = stem.format(n1=aT(numbersForQuestion[0]), n2=aT(numbersForQuestion[1]),
                       n3=aT(numbersForQuestion[2]), n4=aT(numbersForQuestion[3]),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(exponents=joinList(exps, ", "), gcd=aT(baseExp), n1Equation=aT(comments[0]),
                             n2Equation=aT(comments[1]), n3Equation=aT(comments[2]), n4Equation=aT(comments[3]),
                             orderedInequality=aT(orderedInequality), answerOrderNumber=answerOrderNumber,
                             a1=answer_dict[ansInd])

    return stem, answer, comment


def rationalandprime211_Stem_052():
    stem = "다음 중 가장 큰 수는?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{commentNumbers}\n" \
              "따라서 밑의 크기를 비교하면 {orderedInequality}이므로 가장 큰 수는 {ansValue}이다.\n\n"

    # 문제에 필요한 여러 요소들을 생성합니다.

    # 비교가 의미가 있는 범위의 숫자를 정합니다.
    sets = {
        2 : [[3], [5, 6], range(10, 41), range(10, 21)],
        3 : [[4, 5], [7, 8, 10, 11, 12, 13], range(60, 171), range(60, 100, 10)]
    }

    # 동일한 밑을 가지거나 계산 결과값이 동일한 경우를 제외하고 숫자를 뽑습니다.
    showingBases = []
    cardinalBases = []
    base4 = random.choice(list(sets.keys()))
    showingBases.append(base4**4)
    cardinalBases.append(base4)
    base3 = random.choice(sets[base4][0])
    showingBases.append(base3**3)
    cardinalBases.append(base3)
    while True :
        base2 = random.choice(sets[base4][1])
        val = base2**2
        if val in showingBases or base2 in cardinalBases:
            continue
        else :
            showingBases.append(val)
            cardinalBases.append(base2)
            break
    while True :
        base1 = random.choice(sets[base4][2])
        val = base1
        if val in showingBases or base1 in cardinalBases:
            continue
        else :
            showingBases.append(val)
            cardinalBases.append(base1)
            break
    while True :
        base0 = random.choice(sets[base4][3])
        if base0 in showingBases or base0 in cardinalBases :
            continue
        else :
            showingBases.append(base0)
            cardinalBases.append(base0)
            break

    # 최대공약수가 되는 지수를 구합니다.
    baseExp = random.choice(range(10, 60, 10))

    # 실제 보여질 밑과 기저가 되는 밑을 리스트로 정리합니다.
    bases = [(showingBases[0], base4, 4), (showingBases[1], base3, 3), (showingBases[2], base2, 2), (showingBases[3], base1, 1), (showingBases[4], base0, 0.5)]

    # 문제에서 숫자가 보여질 순서를 정합니다.
    showingOrderIndex = random.sample(range(5), k=5)

    # 보여지는 순서대로 밑을 정렬합니다.
    showingOrderBases = [showingBases[x] for x in showingOrderIndex]

    # 보여지는 순서대로 정렬된 밑에 대해서 값이 작은 순서대로 정렬합니다.
    # 그리고 보여지는 순서대로 되어 있는 리스트의 인덱스를 함께 저장합니다.
    sortedBases = sorted([(val, ind) for ind, val in enumerate(showingOrderBases)])

    # 정답이 되는 순서를 찾습니다.
    answerOrderIndex = [sortedBases[x][1] for x in range(5)]
    ansInd = answerOrderIndex[-1]

    # 문제와 해설에 필요한 숫자 식을 만듭니다.
    # 보여지는 순서대로 값을 채웁니다.
    numbersForQuestion = []
    numbersForComment = []
    for ind in showingOrderIndex :
        tup = bases[ind]
        if tup[2] >= 1 :
            questionText = joinList([tup[1], pw, tup[2] * baseExp], "")
        else :
            questionText = joinList([tup[1]**2, pw, int(tup[2] * baseExp)], "")
        commentText = joinList([tup[0], pw, baseExp], "")
        numbersForQuestion.append(questionText)
        numbersForComment.append(commentText)

    ansValue = numbersForQuestion[ansInd]

    # 대소 비교를 위해 지수를 통일하는 과정에서 일부 계산이 필요한 경우를 체크하여 해설용으로 텍스트를 만듭니다.
    # 역시나 보여지는 순서대로 텍스트를 생성합니다.
    comments = []
    for ind in range(5):
        tup = bases[showingOrderIndex[ind]]
        if tup[2] > 1 :
            temp = joinList([numbersForQuestion[ind], eq, "(", tup[1], pw, tup[2], ")", pw, baseExp, eq, numbersForComment[ind]])
            temp = answer_dict[ind] + " " + aT(temp)
            comments.append(temp)
        elif tup[2] < 1 :
            temp = joinList([numbersForQuestion[ind], eq, "(", tup[1], pw, 2, ")", pw, int(baseExp*tup[2]), eq, numbersForComment[ind]])
            temp = answer_dict[ind] + " " + aT(temp)
            comments.append(temp)


    # 이제, 작은 순서대로 정렬된 부등식을 만듭니다.
    orderedInequality = joinList(map(lambda x : x[0], sortedBases),  " " + rb + " ")


    # 내용을 채워 넣습니다.
    stem = stem.format(s1=aT(numbersForQuestion[0]), s2=aT(numbersForQuestion[1]),
                       s3=aT(numbersForQuestion[2]), s4=aT(numbersForQuestion[3]),
                       s5=aT(numbersForQuestion[4]))
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(commentNumbers=joinList(comments, "\n"), orderedInequality=aT(orderedInequality),
                             ansValue=aT(ansValue))

    return stem, answer, comment


def rationalandprime211_Stem_053():
    stem = "다음 중 계산 결과가 나머지 넷과 다른 하나는?\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}\n따라서 나머지 넷과 다른 하나는 {a1}이다.\n\n"

    # 문제에 사용할 지수 하나를 고릅니다.
    mainExp = random.choice(range(10, 25, 2))

    # 문제에 사용될 여러 타입의 구조를 만듭니다.
    type1Anchor = random.choice(range(2, mainExp-1))
    type1 = ["a^", type1Anchor, " ", ts, " a^", mainExp-type1Anchor, 0]

    type2Anchor = mainExp // 2
    type2 = ["(a^2 )^", type2Anchor, 1]

    type3Anchor = random.choice(range(2, 9))
    type3 = ["a^", type3Anchor+mainExp, " ", dd, " a^", type3Anchor, 0]

    type4Anchor1 = random.choice(range(5, 9))
    type4Anchor2 = type4Anchor1 - 2
    type4 = ["a^", mainExp+2, " ", ts, " a^", type4Anchor2, " ", dd, " a^", type4Anchor1, 0]

    type5Anchor = mainExp // 2 - 1
    type5 = ["(a^2 )^", type5Anchor, " ", ts, " a^2", 1]

    types = [type1, type2, type3, type4, type5]
    random.shuffle(types)

    ansInd = random.choice(range(5))
    diff = random.choice([1, -1])
    types[ansInd][1] += diff

    choicesAndResults = []
    for ind, ty in enumerate(types) :
        tempEq = joinList(ty[:-1], "")
        if ind != ansInd:
            res = "a^" + str(mainExp)
        else :
            res = "a^" + str(mainExp + diff + diff*ty[-1])
        choicesAndResults.append((tempEq, res))

    choices = list(map(lambda x : aT(x[0]), choicesAndResults))
    comments = list(map(lambda x : aT(joinList([x[0], eq, x[1]])), choicesAndResults))

    # 내용을 채웁니다.
    stem = stem.format(s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(c1=comments[0], c2=comments[1], c3=comments[2], c4=comments[3], c5=comments[4],
                             a1=answer_dict[ansInd])

    return stem, answer, comment


def rationalandprime211_Stem_054():
    stem = "{aFormula}, {bFormula}일 때, 자연수 {a}, {b}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{aCommentFormula}에서 {aEquation}  {thusA}\n" \
              "{bCommentFormula}에서 {bEquation}  {thusB}\n{thusAnswer}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    first, a, second, b, third = random.sample(range(2, 9), k=5)

    x = symbols("x", positive=True)
    type1Simplified = x**first / x**a
    type2Simplified = x**second * x**b / x**third

    type1QuestionStruct = joinList(["2^", first, " ", dd, " 2^a"], "")
    type2QuestionStruct = joinList([2 ** second, " ", ts, " 2^b ", dd, " ", 2 ** third])
    type2CommentStruct = joinList(["2^", second, " ", ts, " 2^b ", dd, " 2^", third])

    type1QuetionAns = convertIntoHangul(str(type1Simplified.subs(x, 2)))
    type1CommentAns = convertIntoHangul(convertNegExp(type1Simplified)).replace("x", "2")
    type2QuestionAns = convertIntoHangul(str(type2Simplified.subs(x, 2)))
    type2CommentAns = convertIntoHangul(convertNegExp(type2Simplified)).replace("x", "2")

    if first-a >= 0 :
        aEquationList = [first, ms, "a", eq, first-a]
    else :
        aEquationList = ["a", ms, first, eq, a-first]

    if second + b - third >= 0 :
        bEquationList = [second, ps, "b", ms, third, eq, second + b - third]
    else :
        bEquationList = [third, ms, second, ms, "b", eq, third - second - b]

    questionEqDict = getRandomEquation(givenChars=['a', 'b'], realValues=[a, b], avoidZero=True)

    questionFormula = questionEqDict['text']
    ansValue = questionEqDict['ansValue']

    ansInd, choices = makeChoices(ansValue, withTag=True)

    # 모든 등식을 만듭니다.
    aFormula = joinList([type1QuestionStruct, eq, type1QuetionAns])
    bFormula = joinList([type2QuestionStruct, eq, type2QuestionAns])

    aCommentFormula = joinList([type1QuestionStruct, eq, type1CommentAns])
    bCommentFormula = joinList([type2CommentStruct, eq, type2CommentAns])

    aEquation = joinList(aEquationList)
    bEquation = joinList(bEquationList)

    thusA = joinList([thus, "a", eq, a])
    thusB = joinList([thus, "b", eq, b])
    thusAnswer = joinList([thus, questionFormula, eq, ansValue])

    # 내용을 채웁니다.
    stem = stem.format(aFormula=aT(aFormula), bFormula=aT(bFormula), a=aT("a"), b=aT("b"), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(aCommentFormula=aT(aCommentFormula), aEquation=aT(aEquation), thusA=aT(thusA),
                             bCommentFormula=aT(bCommentFormula), bEquation=aT(bEquation), thusB=aT(thusB),
                             thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_055():
    stem = "{questionEquation}일 때, 정수 {x}의 값은? (단, {exp1}, {exp2}{postp} 정수)\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{commentText1}\n즉, {commentText2}이므로\n{commentText3}\n{commentText4}\n\n"

    coeffRange = list(range(-6, 0)) + list(range(1, 7)) #한 자리 정수
    # 정답을 먼저 정합니다.
    xVal = random.choice(coeffRange)

    # 결과값의 지수를 정합니다.
    expDiff = random.choice([-2, -1, 1, 2])

    # expDiff 차이가 나는 일차식 2개를 랜덤하게 생성합니다.

    aVal, bVal = random.choices(coeffRange, k=2)
    xChar = symbols("x", real=True)
    upperExp = aVal * xChar + bVal
    upperExpVal = int(str(upperExp.subs(xChar, xVal)))
    lowerExpVal = upperExpVal - expDiff

    while True :
        cVal = random.choice(coeffRange)
        if cVal != aVal :
            break
    dVal = lowerExpVal - cVal * xVal
    lowerExp = cVal * xChar + dVal
        # tempVal = int(str(lowerExp.subs(xChar, xVal)))
        # if tempVal == lowerExpVal :
        #     break

    # 문제에 활용할 밑을 정합니다.
    base = random.choice(range(11, 20))

    calRes = sympify(joinList([base, "**", expDiff]))
    calResText = convertIntoHangul(str(calRes))

    # 문제에 활용할 여러 수식을 만듭니다.
    upperExpText = convertIntoHangul(str(upperExp), removeSpace=True)
    lowerExpText = convertIntoHangul(str(lowerExp), removeSpace=True)
    numerator = joinList([base, pw, upperExpText])
    denominator = joinList([base, pw, lowerExpText])
    frac = makeFractionFormula(numerator, denominator)

    questionEquation = joinList([frac, eq, calResText])

    expSimplified1 = joinList([base, pw, "{", joinList([upperExpText, ms, "(", lowerExpText, ")"], ""), "}"])
    simplifiedExp = upperExp - lowerExp
    simplifiedExpText = convertIntoHangul(str(simplifiedExp), removeSpace=True)

    commentText1 = joinList([frac, eq, expSimplified1, eq, base, pw, simplifiedExpText])

    if expDiff < 0 :
        simplifiedExp *= -1
        simplifiedExpText = convertIntoHangul(str(simplifiedExp), removeSpace=True)
        expDiff *= -1

    commentText2 = joinList([base, pw, simplifiedExpText, eq, base, pw, expDiff])

    commentText3 = joinList([simplifiedExpText, eq, expDiff])

    commentText4 = joinList([thus, "x", eq, xVal])

    lastChar = lowerExpText[-1]
    try :
        num = int(lastChar)
    except ValueError :
        postp = "는"
    else :
        postp = proc_jo(num, -1)

    # 내용을 채워 넣습니다.
    stem = stem.format(questionEquation=aT(questionEquation), x=aT("x"), exp1=aT(upperExpText), exp2=aT(lowerExpText),
                       postp=postp)
    answer = answer.format(a1=aT(xVal))
    comment = comment.format(commentText1=aT(commentText1), commentText2=aT(commentText2), commentText3=aT(commentText3),
                             commentText4=aT(commentText4))

    return stem, answer, comment


def rationalandprime211_Stem_056():
    stem = "{givenFormula}일 때, 자연수 {a}, {b}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenCommentFormula}\n" \
              "{frontPartFormula}에서 {bEquation}\n" \
              "{rearPartFormula}에서 {aEquation}\n" \
              "{thusAnswer}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    base = random.choice(range(2, 7))
    aVal = random.choice(range(2, 9))
    if base > 4 :
        bVal = random.choice(range(2, 4))
    else :
        bVal = random.choice(range(3, 5))

    # 문제 계산식을 생성합니다.
    questionFormulaInfos = getRandomEquation(givenChars=['a', 'b'], realValues=[aVal, bVal], avoidZero=True)
    questionFormula = questionFormulaInfos['text']
    ansValue = questionFormulaInfos['ansValue']

    ansInd, choices = makeChoices(ansValue, withTag=True)

    givenFormula = joinList(["(", base, "x^a )^b", eq, base**bVal, "x^{", aVal*bVal])
    givenCommentFormula = joinList(["(", base, "x^a )^b", eq, base, pw, "b", "x^ab", eq, base**bVal, "x^{", aVal*bVal])

    frontPartFormula = joinList([base, pw, "b", eq, base**bVal, eq, base, pw, bVal])
    bEquation = joinList(["b", eq, bVal])

    rearPartFormula = joinList(["ab", eq, bVal, "a", eq, aVal*bVal])
    aEquation = joinList(['a', eq, aVal])

    thusAnswer = joinList([thus, questionFormula, eq, ansValue])

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), a=aT("a"), b=aT("b"), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenCommentFormula=aT(givenCommentFormula), frontPartFormula=aT(frontPartFormula),
                             bEquation=aT(bEquation), rearPartFormula=aT(rearPartFormula), aEquation=aT(aEquation),
                             thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_057():
    stem = "{A}는 양수이고 {givenFormula}일 때, {factoredXYFormula}을 만족시키는 자연수 {x}, {y}에 대하여 {questionFormula}의 값을 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{numFactoredFormula}이므로\n" \
              "{givenCommentFormula}\n" \
              "{thusXthusY}\n" \
              "{thusAnswer}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    while True :
        base1, base2 = sorted(random.sample([2, 3, 5, 7, 11, 13], k=2))
        exp1, exp2 = random.choices(range(2, 5), k=2)
        value = base1**exp1 * base2**exp2
        if value > 100 and value < 800 :
            break
    exp3 = random.choice(range(2, 5))

    xVal = exp1 * exp3
    yVal = exp2 * exp3

    questionEquationDict = getRandomEquation(realValues=[xVal, yVal])
    ansVal = questionEquationDict['ansValue']
    questionFormula = questionEquationDict['text']

    # 식을 만듭니다.
    givenFormula = joinList(["A^2 ", eq, " ", value, pw, exp3], "")
    factoredXYFormula = joinList([value, pw, exp3, " ", eq, " ", base1, pw, "x", " ", ts, " ", base2, pw, "y"], "")

    numFactoredFormula = joinList([value, " ", eq, " ", base1, pw, exp1, " ", ts, " ", base2, pw, exp2], "")
    givenCommentFormula = joinList([value, pw, exp3, " ", eq,
                                    " (", base1, pw, exp1, " ", ts, " ", base2, pw, exp2, " )^", exp3, " ", eq, " ",
                                    base1, pw, xVal, " " , ts, " ", base2, pw, yVal], "")
    thusXthusY = joinList([thus, "x", eq, xVal, ",~", "y", eq, yVal])
    thusAnswer = joinList([thus, questionFormula, eq, ansVal])

    # 내용을 채웁니다.
    stem = stem.format(A=aT("A"), givenFormula=aT(givenFormula), factoredXYFormula=aT(factoredXYFormula), x=aT("x"), y=aT("y"),
                       questionFormula=aT(questionFormula))
    answer = answer.format(a1=aT(ansVal))
    comment = comment.format(numFactoredFormula=aT(numFactoredFormula), givenCommentFormula=aT(givenCommentFormula),
                             thusXthusY=aT(thusXthusY), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_058():
    stem = "다음 두 식을 모두 만족시키는 자연수 {a}, {b}에 대하여 {questionFormula}의 값을 구하시오.\n" \
           "   {firstEquation}, {secondEquation}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{commentFormula1}이므로 {aEquation}\n" \
              "{commentFormula2}이므로 {bEquation}\n" \
              "{thusAnswer}\n\n"

    # 첫 번째 식에 사용할 숫자들
    while True :
        exp1 = random.choice(range(2, 5))
        exp2 = random.choice(range(2, 6))
        exp3 = random.choice(range(5, 10))
        exp4 = random.choice(range(2, 5))

        aVal = exp1*exp2 - exp3 + exp4
        if aVal > 0 :
            break

    # 두 번째 식에 사용할 숫자들
    while True :
        bVal = random.choice(range(3, 7))
        exp5 = random.choice(range(4, 9))
        exp6 = random.choice(range(2, 5))
        break

    # 정답을 구합니다.
    questionFormulaDict = getRandomEquation(['a', 'b'], realValues=[aVal, bVal])
    questionFormula = questionFormulaDict['text']
    ansVal = questionFormulaDict['ansValue']

    # 식을 만듭니다.
    firstEquation = joinList(["( x^", exp1, " )^", exp2, " ", dd, " ", "x^", exp3, " ", ts, " ", "x^", exp4, " ", eq, " x^a"], "")
    secondEquation = joinList(["left ( ", "x^b over y^", exp5, " right )^", exp6, " ", eq, " ", "x^", bVal*exp6, " over y^", exp5*exp6], "")

    commentEquation1 = joinList(["( x^", exp1, " )^", exp2, " ", dd, " ", "x^", exp3, " ", ts, " ", "x^", exp4, " ", eq, " x^a ", eq, " ",
                                 "x^{", exp1*exp2, ms, exp3, ps, exp4, "} ", eq, " x^", aVal], "")
    aEquation = joinList(['a', eq, aVal])
    commentEquation2 = joinList(["left ( ", "x^b over y^", exp5, " right )^", exp6, " ", eq, " ",
                                 "x^", exp6, "b", " over y^", exp5*exp6, " ", eq, " ", "x^", bVal*exp6, " over y^", exp5*exp6], "")
    bEquation = joinList(['b', eq, bVal])
    thusAnswer = joinList([thus, questionFormula, eq, ansVal])

    # 내용을 채웁니다.
    stem = stem.format(a=aT("a"), b=aT("b"), questionFormula=aT(questionFormula),
                       firstEquation=aT(firstEquation), secondEquation=aT(secondEquation))
    answer = answer.format(a1=aT(ansVal))
    comment = comment.format(commentFormula1=aT(commentEquation1), aEquation=aT(aEquation),
                             commentFormula2=aT(commentEquation2), bEquation=aT(bEquation),
                             thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_059():
    stem = "다음 중 식을 간단히 한 것으로 옳은 것은?\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{c1}\n{c2}\n{c3}\n{c4}\n따라서 옳은 것은 {a1}이다.\n\n"

    # 문제에 사용될 여러 타입의 구조를 만듭니다.
    exp1, exp2 = random.sample(range(2, 10), k=2)
    type1 = [["x^", exp1, " ", ts, " x^", exp2, " ", eq], [" x^", exp1+exp2], [" x^", exp1*exp2]]

    exp1, exp2 = random.sample(range(2, 10), k=2)
    type2 = [["(x^", exp1, " )^", exp2, " ", eq], [" x^", exp1*exp2], [" x^", exp1+exp2]]

    exp1, exp2 = sorted(random.sample(range(3, 9), k=2))
    exp1 = exp1 - 1
    type3 = [["x^", exp1, " ", dd, " x^", exp2, " ", eq], ["1 over x^", exp2-exp1], [" x^", exp2-exp1]]

    exp1, exp2, exp3 = sorted(random.sample(range(2, 9), k=3))
    type4 = [["( x^", exp1, " y^", exp2, " )^", exp3, " ", eq], [" x^", exp1*exp3, " y^", exp2*exp3], [" x^", exp2*exp3, " y^", exp2*exp3]]

    exp1, exp2, exp3 = sorted(random.sample(range(2, 9), k=3))
    type5 = [["left ( x^", exp1, "over y^", exp2, " right )^", exp3, " ", eq], [" x^", exp1 * exp3, "over y^", exp2 * exp3],
             [" x^", exp1 * exp3, "over y^", exp1 * exp3]]

    types = [type1, type2, type3, type4, type5]
    random.shuffle(types)

    ansInd = random.choice(range(5))

    choices = []
    comments = []
    for ind, ty in enumerate(types) :
        leftPart = joinList(ty[0], "")
        if ind != ansInd:
            rightPart = joinList(ty[2], "")
            commentRightPart = joinList(ty[1], "")
            commentText = answer_dict[ind] + " " + aT(leftPart + commentRightPart)
            comments.append(commentText)
        else :
            rightPart = joinList(ty[1], "")
        choiceText = leftPart + rightPart
        choices.append(choiceText)

    choices = list(map(lambda x : aT(x), choices))

    # 내용을 채웁니다.
    stem = stem.format(s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(c1=comments[0], c2=comments[1], c3=comments[2], c4=comments[3],
                             a1=answer_dict[ansInd])

    return stem, answer, comment


def rationalandprime211_Stem_060():
    stem = "다음 중 □ 안에 알맞은 자연수가 가장 작은 것은?\n① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n① {c1}\n② {c2}\n③ {c3}\n④ {c4}\n⑤ {c5}\n따라서 □ 안에 알맞은 자연수가 가장 작은 것은 {a1}이다.\n\n"

    # 문제에 사용될 여러 타입의 구조를 만듭니다.
    values = []
    exp1, val1 = random.sample(range(2, 10), k=2)
    type1 = [["x^", exp1, " ", ts, " x^□ ", eq, " x^", exp1+val1], [exp1, ps, "□", eq, exp1+val1], ["□", eq, val1]]
    values.append(val1)

    while True :
        val2, exp2 = random.sample(range(2, 10), k=2)
        if val2 not in values :
            break
    type2 = [["(x^□ )^", exp2, " ", eq, " x^", val2 * exp2], [exp2, ts, "□", eq, val2*exp2], ["□", eq, val2]]
    values.append(val2)

    while True :
        exp1, exp2 = sorted(random.sample(range(3, 9), k=2))
        exp1 = exp1 - 1
        val3 = exp2 - exp1
        if val3 not in values :
            break
    type3 = [["x^", exp1, " ", dd, " x^", exp2, " ", eq, "1 over x^□"], [exp2, ms, exp1, eq, val3], ["□", eq, val3]]
    values.append(val3)

    while True :
        exp1, val4, exp3 = sorted(random.sample(range(2, 9), k=3))
        if val4 not in values :
            break
    type4 = [["( x^", exp1, " y^□ )^", exp3, " ", eq, " x^", exp1*exp3, " y^", val4*exp3],  [exp3, ts, "□", eq, val4*exp3], ["□", eq, val4]]
    values.append(val4)

    while True :
        exp1, exp2 = sorted(random.sample(range(3, 9), k=2))
        exp1 = exp1 - 1
        val5 = exp2 - exp1
        if val5 not in values :
            break
    type5 = [["x^", exp2, " ", dd, " x^", exp1, " ", eq, "x^□"], [exp2, ms, exp1, eq, val5], ["□", eq, val5]]
    values.append(val5)

    showingOrder = list(range(5))
    random.shuffle(showingOrder)

    types = [type1, type2, type3, type4, type5]
    minValue = min(values)
    # print(values)
    # print(showingOrder)
    # print(minValue)
    # print(values.index(minValue))
    # print(showingOrder[values.index(minValue)])
    ansInd = showingOrder.index(values.index(minValue))

    choices = []
    comments = []
    for ind in showingOrder :
        mainText = joinList(types[ind][0], "")
        commentText = aT(joinList(types[ind][1])) + "이므로 " + aT(joinList(types[ind][2]))

        choices.append(mainText)
        comments.append(commentText)

    choices = list(map(lambda x : aT(x), choices))

    # 내용을 채웁니다.
    stem = stem.format(s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(c1=comments[0], c2=comments[1], c3=comments[2], c4=comments[3], c5=comments[4],
                             a1=answer_dict[ansInd])

    return stem, answer, comment


def rationalandprime211_Stem_061():
    stem = "어떤 세균은 {unitMinute}분마다 그 수가 {unitMultiplier}배씩 증가한다. " \
           "이 세균 {initValue}마리가 {duration}시간 후에 {finalValue}마리가 된다고 할 때, 자연수 {k}의 값을 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{unitMinute}분마다 세균의 수가 {unitMultiplier}배씩 증가하므로 1시간에 {hourlyIncrease}배씩 증가한다.\n" \
              "따라서 {duration}시간 후의 세균의 수는 {commentEquation}\n" \
              "{thusAnswer}\n\n"

    # 첫 번째 식에 사용할 숫자들
    minutes = divisors(60)[:-1]
    unitMinute = random.choice(minutes)
    unitMultiplier = random.choice(range(2, 6))

    if unitMultiplier % 2 == 0 :
        base = 2
        initExp = random.choice(range(1, 7))
    elif unitMultiplier % 3 == 0 :
        base = 3
        initExp = random.choice(range(1, 5))
    else :
        base = 5
        initExp = random.choice(range(1, 3))

    initValue = base ** initExp
    duration = random.choice(range(2, 7))
    finalValue = joinList([base, pw, 'k'])

    # 해설을 만듭니다.
    hourlyMultiplier = 60 // unitMinute
    if unitMultiplier == 4 :
        hourlyMultiplier *= 2
    ansValue = hourlyMultiplier * duration + initExp

    hourlyIncrease = joinList([base, pw, hourlyMultiplier])
    commentEquation = joinList([initValue, " ", ts, " (", base, pw, hourlyMultiplier, " )^", duration, " ", eq, " ",
                                base, pw, initExp, " ", ts, " ", base, pw, hourlyMultiplier*duration, " ", eq, " ",
                                base, pw, ansValue], "")
    thusAnswer = joinList([thus, "k", eq, ansValue])


    # 내용을 채웁니다.
    stem = stem.format(unitMinute=aT(unitMinute), unitMultiplier=aT(unitMultiplier), initValue=aT(initValue),
                       duration=aT(duration), finalValue=aT(finalValue), k=aT("k"))
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(unitMinute=aT(unitMinute), unitMultiplier=aT(unitMultiplier), hourlyIncrease=aT(hourlyIncrease),
                             duration=aT(duration), commentEquation=aT(commentEquation), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_062():
    stem = "도화지 한 장을 반으로 접으면 그 두께는 처음의 두 배가 된다. 도화지 한 장을 계속해서 반으로 접을 때, " \
           "{fold1}번 접은 도화지의 두께는 {fold2}번 접은 도화지의 두께의 {k}배라 한다. 이때 {k}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{fold1}번 접은 도화지의 두께는 처음의 {two_fold1}배이고, {fold2}번 접은 도화지의 두께는 처음의 {two_fold2}배이다.\n" \
            "따라서 {formula}이므로 {kEquation}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    fold2 = random.choice(range(3, 8))
    foldDiff = random.choice(range(2, 7))
    fold1 = fold2 + foldDiff

    two_fold1 = "2^" + str(fold1)
    two_fold2 = "2^" + str(fold2)
    formula = joinList([two_fold1, " ", dd, " ", two_fold2, " ", eq, " " , "2^", foldDiff, " ", eq, " ", 2**foldDiff])
    kEquation = joinList(["k", eq, 2**foldDiff])

    ansInd, choices = makeChoices(foldDiff, positive=True, withTag=False)
    choices = list(map(lambda x : aT(2**int(x)), choices))

    # 내용을 채웁니다.
    stem = stem.format(fold1=aT(fold1), fold2=aT(fold2), k=aT("k"),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(fold1=aT(fold1), two_fold1=aT(two_fold1), fold2=aT(fold2), two_fold2=aT(two_fold2),
                             formula=aT(formula), kEquation=aT(kEquation))

    return stem, answer, comment


def rationalandprime211_Stem_063():
    stem = "{n}이 자연수일 때, 다음 중 옳은 것을 보기에서 모두 고른 것은?\n\n[보기]\n" \
           "   ㄱ. {s1}\n   ㄴ. {s2}\n   ㄷ. {s3}\n   ㄹ. {s4}\n\n" \
           "① {n1}\n② {n2}\n③ {n3}\n④ {n4}\n⑤ {n5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{mainComment}\nㄱ. {comment1}\nㄴ. {comment2}\nㄷ. {comment3}\nㄹ. {comment4}\n따라서 옳은 것은 {ans}이다.\n\n"

    def unit(form, withTag=False) :
        res = joinList([" (-1)^", form, " "], "")
        if withTag :
            return aT(res)
        else :
            return res

    exponents = ['n', 'n+1', '2n', '2n-1', '2n+1', '3n', '3n+1', '3n-1', '4n', '4n+1', '4n-1']

    set11 = [joinList([unit('n'), ts, unit('n')]), [1, -1], unit('2n')]
    set12 = [joinList([unit('n'), ts, unit('n+1')]), [-1, 1], unit('2n+1')]
    set13 = [joinList([unit('2n+1'), ts, unit('2n-1')]), [1, -1], unit('4n')]
    set14 = [joinList([unit('3n'), ts, unit('3n+1')]), [-1, 1], unit('6n+1')]
    type1 = [set11, set12, set13, set14]

    set21 = [joinList([unit('n'), ps, unit('n')]), [False, 2], joinList([aT('n'), "이 짝수이면 2, 홀수이면 -2이다."])]
    set22 = [joinList([unit('n'), ps, unit('n+1')]), [0, -1], joinList([unit('n'), ps, "(-1)", ts, unit('n')])]
    set23 = [joinList([unit('2n-1'), ps, unit('2n')]), [0, 1], joinList(["(-1)", ps, 1])]
    set24 = [joinList([unit('4n+1'), ps, unit('4n-1')]), [-2, 0], joinList(["(-1)", ps, "(-1)"])]
    type2 = [set21, set22, set23, set24]

    set31 = [joinList([unit('n'), ts, unit('n+1'), ts, unit('n+2')]), [False, -1], joinList([aT('n'), "이 짝수이면 -1, 홀수이면 1이다."])]
    set32 = [joinList([unit('n'), ts, unit('2n-1'), ts, unit('3n')]), [-1, 1], unit('6n-1')]
    set33 = [joinList([unit('2n'), ts, unit('2n+1'), ts, unit('2n-1')]), [1, -1], unit('6n')]
    set34 = [joinList([unit('3n'), ts, unit('3n-1'), ts, unit('2n+1')]), [1, -1], unit('8n')]
    type3 = [set31, set32, set33, set34]

    set41 = [joinList([unit('n'), ps, unit('n+1'), ps, unit('n+2')]), [False, -1], joinList([aT('n'), "이 짝수이면 1, 홀수이면 -1이다."])]
    set42 = [joinList([unit('n'), ps, unit('2n-1'), ps, unit('2n')]), [False, 1], joinList([aT('n'), "이 짝수이면 1, 홀수이면 -1이다."])]
    set43 = [joinList([unit('2n'), ps, unit('2n+1'), ps, unit('2n-1')]), [-1, -2], joinList(["1", ps, "(-1)", ps, "(-1)"])]
    set44 = [joinList([unit('3n'), ps, unit('3n+1'), ps, unit('2n+2')]), [1, -1], joinList([unit('3n'), "-", unit('3n'), ps, unit('2n+2'), eq, unit('2n+2')])]
    type4 = [set41, set42, set43, set44]

    types = [type1, type2, type3, type4]

    oneItems = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ']
    twoItems = ['ㄱ, ㄴ', 'ㄱ, ㄷ', 'ㄱ, ㄹ', 'ㄴ, ㄷ', 'ㄴ, ㄹ', 'ㄷ, ㄹ']
    threeItems = ['ㄱ, ㄴ, ㄷ', 'ㄱ, ㄴ, ㄹ', 'ㄱ, ㄷ, ㄹ', 'ㄴ, ㄷ, ㄹ']

    items = [oneItems, twoItems, threeItems]

    selectionCharacters = {0: 'ㄱ', 1: 'ㄴ', 2: 'ㄷ', 3: 'ㄹ'}

    howManyCorrects = random.choice(range(1, 4))
    corrects = random.sample(range(4), k=howManyCorrects)

    corrects.sort()

    structs = [(2, 2, 0), (0, 2, 2)]
    struct = random.choice(structs)

    ansChars = ", ".join([selectionCharacters[x] for x in corrects])

    selects = []
    for i, s in enumerate(struct) :
        if howManyCorrects-1 == i :
            if s == 0 :
                temp = [ansChars]
            else :
                while True :
                    temp = random.sample(items[i], k=s)
                    if ansChars not in temp :
                        break
                temp.append(ansChars)
                temp.sort()
        else :
            temp = random.sample(items[i], k=s)
            temp.sort()
        selects.extend(temp)

    ansInd = selects.index(ansChars)

    choices = []
    comments = []

    for ind in range(4):
        if ind in corrects:
            while True :
                statementList = random.choice(types[ind])
                if isinstance(statementList[1][0], bool) :
                    continue
                else :
                    break

            tempText = aT(joinList([statementList[0], eq, statementList[1][0]]))
            tempComment = aT(joinList([statementList[0], eq, statementList[2], eq, statementList[1][0]]))
        else :
            statementList = random.choice(types[ind])
            tempText = aT(joinList([statementList[0], eq, statementList[1][1]]))
            if isinstance(statementList[1][0], bool) :
                tempComment = statementList[2]
            else :
                tempComment = aT(joinList([statementList[0], eq, statementList[2], eq, statementList[1][0]]))

        choices.append(tempText)
        comments.append(tempComment)

    mainComment = aT(joinList([unit("(홀수)"), eq, "-1", ",~", unit("(짝수)"), eq, "1"])) + "임을 이용하여 문제를 해결한다."

    # 내용을 채웁니다.
    stem = stem.format(n=aT('n'), s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3],
                       n1=selects[0], n2=selects[1], n3=selects[2], n4=selects[3], n5=selects[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(mainComment=mainComment, comment1=comments[0], comment2=comments[1], comment3=comments[2],
                             comment4=comments[3], ans=ansChars)

    return stem, answer, comment


def rationalandprime211_Stem_064():
    stem = "{givenFormula}{postp} 만족시키는 가장 큰 자연수 {d}에 대하여 {questionFormula}의 값을 구하시오. (단, {abc}는 자연수이다)\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenCommentFormula}이므로\n" \
              "{adEquation}, {bdEquation}, {cdEquation}\n" \
              "이를 만족시키는 가장 큰 자연수 {d}는 {exponents}의 최대공약수이므로 {dEquation}이다.\n" \
              "따라서 {adReplaced}에서 {aEquation}, {bdReplaced}에서 {bEquation}, {cdReplaced}에서 {cEquation}이므로\n" \
              "{answerEquation}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    ds = [4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16]
    abcs = [2, 3, 4, 5, 6, 7, 8, 9]

    while True :
        aVal, bVal, cVal = random.sample(abcs, k=3)
        commons = gcd(gcd(aVal, bVal), cVal)
        if commons < 2 :
            break

    dVal = random.choice(ds)

    charValueDict = {'a':aVal, 'b':bVal, 'c':cVal, 'd':dVal}
    charValueItems = list(charValueDict.items())
    random.shuffle(charValueItems)

    charValueItems[:2] = sorted(charValueItems[:2])
    charValueItems[2:] = sorted(charValueItems[2:])

    questionFormula = joinList([charValueItems[0][0], charValueItems[1][0], ms, charValueItems[2][0], charValueItems[3][0]])
    ansValue = charValueItems[0][1]*charValueItems[1][1] - charValueItems[2][1]*charValueItems[3][1]

    # 식을 만듭니다.
    givenFormulaLeft = " ( x^a y^b z^c )^d "
    givenFormulaMiddle = " x^ad y^bd z^cd "
    adVal = aVal*dVal
    bdVal = bVal*dVal
    cdVal = cVal*dVal
    givenFormulaRight = joinList(['x', pw, adVal, " ", 'y', pw, bdVal, " ", 'z', pw, cdVal])

    givenFormula = joinList([givenFormulaLeft, eq, givenFormulaRight])
    givenCommentFormula = joinList([givenFormulaLeft, eq, givenFormulaMiddle, eq, givenFormulaRight])

    d = str(dVal)
    leftParts = ['ad', 'bd', 'cd', 'd', d+'a', 'a', d+'b', 'b', d+'c', 'c']
    rightParts = [adVal, bdVal, cdVal, dVal, adVal, aVal, bdVal, bVal, cdVal, cVal]

    equalities = makeEquality(leftParts, rightParts, withTag=True)
    exponents = joinList([adVal, bdVal, cdVal], ",~ ")
    answerEquation = joinList([questionFormula, eq, charValueItems[0][1], ts, charValueItems[1][1], ms, charValueItems[2][1], ts, charValueItems[3][1], eq, ansValue])

    postp = proc_jo(cdVal % 10, 1)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), postp=postp, d=aT('d'), questionFormula=aT(questionFormula), abc=aT('a,~ b,~ c'))
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(givenCommentFormula=aT(givenCommentFormula), adEquation=equalities[0], bdEquation=equalities[1],
                             cdEquation=equalities[2], d=aT('d'), exponents=aT(exponents), dEquation=equalities[3],
                             adReplaced=equalities[4], aEquation=equalities[5], bdReplaced=equalities[6], bEquation=equalities[7],
                             cdReplaced=equalities[8], cEquation=equalities[9], answerEquation=aT(answerEquation))

    return stem, answer, comment


def rationalandprime211_Stem_065():
    stem = "{givenFormula}{postp} 만족시키는 모든 자연수 {n}의 {optionText} 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}에서 {commentFormula1},\n{commentFormula2}, {commentFormula3}이므로\n" \
              "조건을 만족시키는 자연수 {n}은 {ansStart}부터 {ansEnd}까지이다.\n따라서 모든 {n}의 {optionText2} {ansValue}이다.\n\n"

    # 문제에 필요한 여러 요소들을 생성합니다.

    # 비교가 의미가 있는 범위의 숫자를 정합니다.
    sets = {
        1 : range(5, 355, 5),
        2 : range(2, 20),
        3 : range(2, 8),
    }

    # n의 지수를 구합니다.
    kVal = random.choice(range(1, 4))

    if kVal < 3 :
        optionText = "개수를"
        optionText2 = "개수는"
    else :
        optionText = "합을"
        optionText2 = '합은'

    commonMultiplier = random.choice(range(10, 210, 10))


    if kVal == 1 :
        while True :
            leftExp, rightExp = random.sample(range(2, 4), k=2)
            leftBase = random.choice(sets[leftExp])
            rightBase = random.choice(sets[rightExp])
            leftVal = leftBase ** leftExp
            rightVal = rightBase ** rightExp

            if leftVal < rightVal and rightVal - leftVal > 2:
                ansStart = leftVal + 1
                ansEnd = rightVal - 1
                ansValue = ansEnd - ansStart + 1
                break

    elif kVal == 2 :
        while True :
            leftExp, rightExp = random.sample([1, 3], k=2)
            leftBase = random.choice(sets[leftExp])
            rightBase = random.choice(sets[rightExp])
            leftVal = leftBase ** leftExp
            rightVal = rightBase ** rightExp

            if leftVal >= rightVal :
                continue
            else :
                ansCount = 0
                ansValues = []
                for val in sets[kVal]:
                    realVal = val**kVal
                    if realVal > leftVal and realVal < rightVal :
                        ansCount += 1
                        ansValues.append(val)
                if ansCount > 1 :
                    ansStart = ansValues[0]
                    ansEnd = ansValues[-1]
                    ansValue = ansEnd - ansStart + 1
                    break

    else:
        while True :
            leftExp, rightExp = random.sample([1, 2], k=2)
            leftBase = random.choice(sets[leftExp])
            rightBase = random.choice(sets[rightExp])
            leftVal = leftBase ** leftExp
            rightVal = rightBase ** rightExp

            if leftVal >= rightVal :
                continue
            else :
                ansCount = 0
                ansValues = []
                for val in sets[kVal]:
                    realVal = val**kVal
                    if realVal > leftVal and realVal < rightVal :
                        ansCount += 1
                        ansValues.append(val)
                if ansCount > 1 :
                    ansStart = ansValues[0]
                    ansEnd = ansValues[-1]
                    ansValue = sum(ansValues)
                    break

    leftForm = exponentForm(leftBase, leftExp)
    rightForm = exponentForm(rightBase, rightExp)
    nForm = exponentForm("n", kVal)

    leftForm_noParen = exponentForm(leftBase, leftExp, paren=False)
    rightForm_noParen = exponentForm(rightBase, rightExp, paren=False)
    nForm_noParen = exponentForm("n", kVal, paren=False)


    # 문제에 필요한 식을 구성합니다.
    givenFormula = joinList([leftBase, pw, leftExp*commonMultiplier, " ", rb, " ", "n^", kVal*commonMultiplier, " ", rb, " ", rightBase, pw, rightExp*commonMultiplier], "")
    postp = proc_jo(rightExp*commonMultiplier % 10, 1)
    commentFormula1 = joinList([leftForm, pw, commonMultiplier, " ", rb, nForm, pw, commonMultiplier, " ", rb, rightForm, pw, commonMultiplier], "")
    commentFormula2 = joinList([leftForm_noParen, rb, nForm_noParen, rb, rightForm_noParen], "")
    commentFormula3 = joinList([leftVal, rb, nForm_noParen, rb, rightVal], "")

    # 내용을 채워 넣습니다.
    stem = stem.format(givenFormula=aT(givenFormula), postp=postp, n=aT("n"), optionText=optionText)
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(givenFormula=aT(givenFormula), commentFormula1=aT(commentFormula1),
                             commentFormula2=aT(commentFormula2), commentFormula3=aT(commentFormula3), n=aT("n"),
                             ansStart=aT(ansStart), ansEnd=aT(ansEnd), optionText2=optionText2, ansValue=aT(ansValue))

    return stem, answer, comment


def rationalandprime211_Stem_066():
    stem = "다음을 모두 만족시키는 자연수 {x}, {y}에 대하여 {questionFormula}의 값은?\n" \
           "   {type1Question}, {type2Question}\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{type1Question}에서 {type1Comment}\n" \
              "즉, {xEquation}이므로 {thusX}\n" \
              "{type2Question}에서\n" \
              "{type2Comment1}, {type2Comment2}\n" \
              "즉, {yEquation}이므로 {thusY}\n" \
              "{thusAnswer}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    first = random.choice(range(2, 5))
    x = random.choice(range(4, 10))
    while True :
        second = random.choice(range(2, 7))
        third = random.choice(range(2, 6))
        y = random.choice(range(1, 4))
        fourth = 3*y - second*2 + third
        if fourth > 0 :
            break

    z = symbols("z", positive=True)
    z2 = z**2
    z3 = z**3
    type1Simplified = z2**first / z**x
    type2Simplified = z2**second / z**third * z**fourth

    if third == x :
        xForm = 'x'
    else :
        diff = third-x
        if diff > 0 :
            xForm = joinList(['{ x', ps, diff, " }"], "")
        else :
            xForm = joinList(['{ x', diff, " }"], "")

    type1QuestionStruct = joinList(["9^", first, " ", dd, " 3^x"], "")
    type1CommentStruct = joinList(["3^", 2*first, " ", dd, " 3^x"], "")
    type2QuestionStruct = joinList(["4^", second, " ", dd, " 2^", xForm, " ", ts, " ", 2 ** fourth], "")
    type2CommentStruct = joinList(["2^", 2*second, " ", dd, " 2^", third, " ", ts, " 2^", fourth], "")

    type1QuetionAns = convertIntoHangul(str(type1Simplified.subs(z, 3)))
    type1CommentAns = convertIntoHangul(convertNegExp(type1Simplified)).replace("z", "3")
    type2QuestionAns = " 8^y "
    type2CommentAns = " 2^3y"
    # type2CommentAns = convertIntoHangul(convertNegExp(type2Simplified)).replace("z", "2")

    firstReal = first*2
    if first*2-x >= 0 :
        xEquationList = [firstReal, ms, "x", eq, firstReal-x]
    else :
        xEquationList = ["x", ms, firstReal, eq, x-firstReal]

    type1Question = joinList([type1QuestionStruct, eq, type1QuetionAns])
    type2Question = joinList([type2QuestionStruct, eq, type2QuestionAns])

    type1Comment = joinList([type1CommentStruct, eq, type1CommentAns])
    xEquation = joinList(xEquationList)
    thusX = joinList(["x", eq, x])

    secondReal = second*2
    type2Exps = joinList(["{ ", secondReal, ms, third, ps, fourth, " }"], "")

    type2Comment1 = joinList([type2CommentStruct, eq, type2CommentAns])
    type2Comment2 = joinList(["2^", type2Exps, " ", eq, " ", type2CommentAns], "")
    yEquation = joinList([3*y, eq, '3y'])
    thusY = joinList(['y', eq, y])

    questionEqDict = getRandomEquation(givenChars=['x', 'y'], realValues=[x, y], avoidZero=True)

    questionFormula = questionEqDict['text']
    ansValue = questionEqDict['ansValue']

    ansInd, choices = makeChoices(ansValue, withTag=True)
    thusAnswer = joinList([thus, questionFormula, eq, ansValue])

    # 내용을 채웁니다.
    stem = stem.format(x=aT('x'), y=aT('y'), questionFormula=aT(questionFormula), type1Question=aT(type1Question),
                       type2Question=aT(type2Question),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(type1Question=aT(type1Question), type1Comment=aT(type1Comment), xEquation=aT(xEquation),
                             thusX=aT(thusX), type2Question=aT(type2Question), type2Comment1=aT(type2Comment1),
                             type2Comment2=aT(type2Comment2), yEquation=aT(yEquation), thusY=aT(thusY),
                             thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_067():
    stem = "빛의 속도는 초속 {speedOfLight}km이다. {startPoint}에서 {endPoint}까지의 거리가 {distance}m일 때, " \
           "빛이 {startPoint}에서 출발하여 {endPoint}에 도달하는데 몇 초가 걸리는지 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{distanceToKilo}이므로 구하는 시간은\n" \
              "{answerFormula}\n\n"

    # 문제에 필요한 여러 요소들을 생성합니다.
    planets = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성']
    fromSum = list(map(lambda x : Decimal(str(x)), [0, 0.579, 1.08, 1.5, 2.28, 7.8, 14.4, 28.8]))

    ind1, ind2 = random.sample(range(len(planets)), k=2)
    startPoint, endPoint = planets[ind1], planets[ind2]
    dist = abs(fromSum[ind1] - fromSum[ind2])
    distText = str(dist)

    speedOfLight = joinList(['3.0', ts, '10^5 '])
    distance = joinList([distText, ts, "10^11 "])
    distToKilo = joinList([distText, ts, "10^8 "])
    distanceToKilo = joinList([distance, 'rm (m)', eq, distToKilo, 'rm (km)'])

    ansVal = int(dist/3 * 1000)

    answerFormula = joinList([makeFractionFormula(distToKilo, speedOfLight), eq, dist/3, ts, '10^3 ', eq, ansVal])

    # 내용을 채워 넣습니다.
    stem = stem.format(speedOfLight=aT(speedOfLight), startPoint=startPoint, endPoint=endPoint, distance=aT(distance))
    answer = answer.format(a1=aT(ansVal))
    comment = comment.format(distanceToKilo=aT(distanceToKilo), answerFormula=aT(answerFormula)+"(초)")

    return stem, answer, comment


def rationalandprime211_Stem_068():
    stem = "{given1}, {given2}일 때, 자연수 {a}, {b}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{given1Comment}이므로 {aFormula}\n{given2Comment}이므로 {bFormula}\n{thusAnswer}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    twoBase = random.choice([2, 4, 8])
    threeBase = random.choice([3, 9])

    twoLength = random.choice([2, 4])
    threeLength = 3

    twoExp = random.choice(range(3, 9))
    threeExp = random.choice(range(3, 10))

    twoExponentForm = exponentForm(twoBase, twoExp, paren=False)
    threeExponentForm = exponentForm(threeBase, threeExp, paren=False)

    given1List = [twoExponentForm for _ in range(twoLength)]
    given2List= [threeExponentForm for _ in range(threeLength)]

    given1 = joinList([joinList(given1List, ps), eq, '2^a'])
    given2 = joinList([joinList(given2List, ps), eq, '3^b'])

    if twoLength == 4 :
        twoLenText = " 2^2 "
    else :
        twoLenText = "2"

    given1CommentFront = joinList([joinList(given1List, ps), eq, twoLength, ts, twoExponentForm])
    given1Val = twoLength * twoBase ** twoExp
    aVal = factorint(given1Val)[2]
    aFormula = joinList(['a', eq, aVal])
    given1ResText = "2^" + str(aVal)

    if twoBase==2 and twoLength==2 :
        given1Comment = joinList([given1CommentFront, eq, given1ResText])
    else :
        if twoBase == 4 :
            twoExponentFormSimplified = exponentForm(2, 2 * twoExp, paren=False)
        elif twoBase == 8 :
            twoExponentFormSimplified = exponentForm(2, 3 * twoExp, paren=False)
        else :
            twoExponentFormSimplified = twoExponentForm

        simplifiedText1 = joinList([twoLenText, ts, twoExponentFormSimplified])
        given1Comment = joinList([given1CommentFront, eq, simplifiedText1, eq, given1ResText])

    given2CommentFront = joinList([joinList(given2List, ps), eq, threeLength, ts, threeExponentForm])
    given2Val = threeLength * threeBase ** threeExp
    bVal = factorint(given2Val)[3]
    bFormula = joinList(['b', eq, bVal])
    given2ResText = "3^" + str(bVal)

    if threeBase == 3 :
        given2Comment = joinList([given2CommentFront, eq, given2ResText])
    else:
        threeExponentFormSimplified = exponentForm(3, 2 * threeExp, paren=False)
        simplifiedText2 = joinList([threeLength, ts, threeExponentFormSimplified])
        given2Comment = joinList([given2CommentFront, eq, simplifiedText2, eq, given2ResText])

    # 정답 식을 만듭니다.
    questionFormulaDict = getRandomEquation(givenChars=['a', 'b'], realValues=[aVal, bVal], avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']
    thusAnswer = joinList([thus, questionFormula, eq, ansValue])

    # 선택지를 만듭니다.
    ansInd, choices = makeChoices(ansValue, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(given1=aT(given1), given2=aT(given2), a=aT('a'), b=aT('b'), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(given1Comment=aT(given1Comment), aFormula=aT(aFormula), given2Comment=aT(given2Comment),
                             bFormula=aT(bFormula), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_069():
    stem = "다음을 만족시키는 자연수 {abc}에 대하여 {questionFormula}의 값은?\n" \
           "   {givenFormula1},  {givenFormula2},  {givenFormula3}\n"\
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula1Comment}이므로 {aFormula}\n{givenFormula2Comment}이므로 {bFormula}\n" \
              "{givenFormula3Comment}이므로 {cFormula}\n{thusAnswer}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    twoBase = random.choice([2, 4, 8])
    threeBase = random.choice([3, 9])

    twoLength = random.choice([2, 3])
    threeLength = 3

    twoExp = random.choice(range(3, 9))
    threeExp = random.choice(range(3, 7))

    twoExponentForm = exponentForm(twoBase, twoExp, paren=False)
    threeExponentForm = exponentForm(threeBase, threeExp, paren=False)

    given1List = [twoExponentForm for _ in range(twoLength)]
    given2List= [threeExponentForm for _ in range(threeLength)]

    given1 = joinList(given1List, ts)
    given2 = joinList(given2List, ps)

    givenFormula1 = joinList([given1, eq, '2^a'])
    givenFormula2 = joinList([given2, eq, '3^b'])

    fiveExp1, fiveExp2 = random.choices(range(2, 10), k=2)

    given3 = joinList(["( 5^", fiveExp1, " )^", fiveExp2], "")
    givenFormula3 = joinList([given3, eq, '5^c'])

    twoExpLenMuled = twoExp * twoLength
    givenFormula1CommentFirstText = joinList([twoBase, pw, twoExpLenMuled], "")

    if twoBase==2 :
        givenFormula1Comment = joinList([given1, eq, givenFormula1CommentFirstText])
        aVal = twoExpLenMuled
    else :
        if twoBase==4:
            aVal = twoExpLenMuled * 2
        else :
            aVal = twoExpLenMuled * 3

        twoExponentFormSimplified = exponentForm(2, aVal, paren=False)
        givenFormula1Comment = joinList([given1, eq, givenFormula1CommentFirstText, eq, twoExponentFormSimplified])

    aFormula = joinList(['a', eq, aVal])

    given2CommentFront = joinList([joinList(given2List, ps), eq, threeLength, ts, threeExponentForm])
    given2Val = threeLength * threeBase ** threeExp
    bVal = factorint(given2Val)[3]
    bFormula = joinList(['b', eq, bVal])
    given2ResText = "3^" + str(bVal)

    if threeBase == 3 :
        givenFormula2Comment = joinList([given2CommentFront, eq, given2ResText])
    else:
        threeExponentFormSimplified = exponentForm(3, 2 * threeExp, paren=False)
        simplifiedText2 = joinList([threeLength, ts, threeExponentFormSimplified])
        givenFormula2Comment = joinList([given2CommentFront, eq, simplifiedText2, eq, given2ResText])

    cVal = fiveExp1 * fiveExp2
    givenFormula3Comment = joinList([given3, " ", eq, " 5^", cVal], "")
    cFormula = joinList(['c', eq, cVal])

    givenChars = ['a', 'b', 'c']
    questionFormulaDict = getRandomEquation(givenChars=givenChars, coefficientRange=[(-2, 3) for i in range(3)],
                            realValues=[aVal, bVal, cVal], avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']

    abc = joinList(list(map(aT, givenChars)), ", ")

    # 선택지를 만듭니다.
    ansInd, choices = makeChoices(ansValue, withTag=True)

    # 정답 식을 만듭니다.
    thusAnswer = joinList([thus, questionFormula, eq, ansValue])

    # 내용을 채웁니다.
    stem = stem.format(abc=abc, questionFormula=aT(questionFormula), givenFormula1=aT(givenFormula1),
                       givenFormula2=aT(givenFormula2), givenFormula3=aT(givenFormula3),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula1Comment=aT(givenFormula1Comment), aFormula=aT(aFormula),
                             givenFormula2Comment=aT(givenFormula2Comment), bFormula=aT(bFormula),
                             givenFormula3Comment=aT(givenFormula3Comment), cFormula=aT(cFormula),
                             thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_070():
    stem = "{givenFormula}일 때, 음이 아닌 정수 {x}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaComment}이므로 {commentText2}\n{thusAnswer}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    base = random.choice(range(2, 10))
    while True :
        xVal = random.choice(range(1, 7))
        if base ** xVal < 126 :
            if base > 5 :
                addValMax = 2
            else :
                addValMax = 3
            break

    possibleAddVals = list(range(-xVal, 0)) + list(range(1, addValMax+1))

    addVal = random.choice(possibleAddVals)

    x = symbols('x', real=True)
    expFormula = x + addVal
    expForm = exponentForm(base, wrapParen(expFormula), paren=False)
    baseForm = joinList([" ", base, pw, 'x '], "")

    resValue = int((base**xVal) * (base**addVal + 1))

    given = joinList([expForm, pss, base, pw, 'x'], "")
    givenFormula = joinList([given, eq, resValue])

    sep = sympify(joinList([base, "**", addVal]))
    sepText = convertIntoHangul(convertNegExp(sep))
    coeff = sep + 1
    coeffText = convertIntoHangul(str(coeff))

    baseResValue = int(resValue // coeff)

    givenFormulaComment = joinList([given, eq, sepText, ts, baseForm, ps, baseForm, eq, coeffText, ts, baseForm, eq, resValue])
    commentText2 = joinList([baseForm, eqs, baseResValue, eqs, base, pw, xVal], "")
    thusAnswer = joinList([thus, 'x', eq, xVal])

    # 선택지를 만듭니다.
    ansInd, choices = makeChoices(xVal, positive=True, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), x=aT('x'),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaComment=aT(givenFormulaComment), commentText2=aT(commentText2),
                             thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_071():
    stem = "{questionFormula}을 간단히 하면?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n(주어진 식){commentFormula1}\n{commentFormula2}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    while True :
        twoBase1, twoBase2 = random.choices([2, 4, 8], k=2)
        threeBase1, threeBase2 = random.choices([3, 9], k=2)

        twoLength1, twoLength2 = random.choices([2, 4], k=2)
        threeLength = 3

        twoExp1, twoExp2 = random.sample(range(2, 7), k=2)
        threeExp1, threeExp2 = random.sample(range(2, 6), k=2)

        leftUpper = twoLength1 * twoBase1 ** twoExp1
        leftLower = threeLength * threeBase1 ** threeExp1
        rightUpper = threeLength * threeBase2 ** threeExp2
        rightLower = twoLength2 * twoBase2 ** twoExp2
        resValue = sympify(joinList([leftUpper, "/", leftLower, "*", rightUpper, "/", rightLower]))
        rVfloat = float(resValue)
        if rVfloat > 0.001 and rVfloat < 1000 :
            break

    twoExponentForm1, twoExponentForm2 = exponentForm(twoBase1, twoExp1, paren=False), exponentForm(twoBase2, twoExp2, paren=False)
    threeExponentForm1, threeExponentForm2 = exponentForm(threeBase1, threeExp1, paren=False), exponentForm(threeBase2, threeExp2, paren=False)

    twoBaseExp1 = [twoExponentForm1 for _ in range(twoLength1)]
    twoBaseExp2 = [twoExponentForm2 for _ in range(twoLength2)]
    threeBaseExp1 = [threeExponentForm1 for _ in range(threeLength)]
    threeBaseExp2 = [threeExponentForm2 for _ in range(threeLength)]

    twoBaseExp1Text = joinList(twoBaseExp1, ps)
    twoBaseExp2Text = joinList(twoBaseExp2, ps)
    threeBaseExp1Text = joinList(threeBaseExp1, ps)
    threeBaseExp2Text = joinList(threeBaseExp2, ps)

    questionFormula = joinList([makeFractionFormula(twoBaseExp1Text, threeBaseExp1Text),
                                ts, makeFractionFormula(threeBaseExp2Text, twoBaseExp2Text)])

    twoLen1Factored = getFactoredIntFormula(twoLength1)
    twoLen2Factored = getFactoredIntFormula(twoLength2)

    comment1LeftUpper = joinList([twoLen1Factored, ts, twoExponentForm1])
    comment1LeftLower = joinList([threeLength, ts, threeExponentForm1])
    comment1RightUpper = joinList([threeLength, ts, threeExponentForm2])
    comment1RightLower = joinList([twoLen2Factored, ts, twoExponentForm2])

    comment1Left = makeFractionFormula(comment1LeftUpper, comment1LeftLower)
    comment1Right = makeFractionFormula(comment1RightUpper, comment1RightLower)

    commentText1 = joinList([eq, comment1Left, ts, comment1Right])


    comment2LeftUpper = getFactoredIntFormula(leftUpper)

    comment2LeftLower = getFactoredIntFormula(leftLower)

    comment2RightUpper = getFactoredIntFormula(rightUpper)

    comment2RightLower = getFactoredIntFormula(rightLower)

    comment2Left = makeFractionFormula(comment2LeftUpper, comment2LeftLower)
    comment2Right = makeFractionFormula(comment2RightUpper, comment2RightLower)


    resValueSplited = str(resValue).split("/")
    if len(resValueSplited) == 2 :
        numerator, denominator = list(map(int, resValueSplited))
        numeratorFactored = getFactoredIntFormula(numerator)
        denominatorFactored = getFactoredIntFormula(denominator)

        if str(numerator) == numeratorFactored and str(denominator) == denominatorFactored:
            additional = ""
        else:
            additional = makeFractionFormula(numerator, denominator)

        resFactored = makeFractionFormula(numeratorFactored, denominatorFactored)

        commentText2 = joinList([comment2Left, ts, comment2Right, eq, resFactored])
        if additional:
            commentText2 = joinList([commentText2, eq, additional])

        ansInd, numerators = makeChoices(numerator, positiveWithoutZero=True, withTag=False)

        choices = []
        for num in numerators:
            temp = aT(convertIntoHangul(str(sympify(joinList([num, "/", denominator])))))
            choices.append(temp)

    else :
        resValueInt = int(str(resValue))
        resValueIntFactored = getFactoredIntFormula(resValueInt)

        if str(resValueInt) == resValueIntFactored :
            additional = ""
        else :
            additional = resValueInt

        commentText2 = joinList([comment2Left, ts, comment2Right, eq, resValueIntFactored])
        if additional :
            commentText2 = joinList([commentText2, eq, additional])

        ansInd, choices = makeChoices(resValueInt, positiveWithoutZero=True)

    commentText2 = eqs + commentText2

    # 내용을 채웁니다.
    stem = stem.format(questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(commentFormula1=aT(commentText1), commentFormula2=aT(commentText2))

    return stem, answer, comment


def rationalandprime211_Stem_072():
    stem = "{largeAFormula}, {largeBFormula}라 할 때, {givenValue}을 {A}, {B}를 사용하여 바르게 나타낸 것은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenValueFormula}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    base1, base2 = sorted(random.sample([2, 3, 5, 7], k=2))
    while True :
        baseExp1, baseExp2 = random.choices([1, 2, 3], k=2)
        if baseExp1!=1 or baseExp2!=1 :
            break

    commonMul = baseExp1 * baseExp2

    while True :
        valExp1, valExp2 = random.sample(range(commonMul, commonMul*6, commonMul), k=2)

        outerExp = gcd(valExp1, valExp2)

        innerExp1 = valExp1 // outerExp
        innerExp2 = valExp2 // outerExp

        showingValue = base1 ** innerExp1 * base2 ** innerExp2

        if showingValue < 1000 :
            break

    aExp = valExp1 // baseExp1
    bExp = valExp2 // baseExp2

    aExpFormNoParen = exponentForm(base1, baseExp1, paren=False)
    bExpFormNoParen = exponentForm(base2, baseExp2, paren=False)

    AExpForm = exponentForm("A", aExp, paren=False)
    BExpForm = exponentForm("B", bExp, paren=False)

    aFormula = joinList([aExpFormNoParen, eq, "A"])
    bFormula = joinList([bExpFormNoParen, eq, "B"])

    givenValue = joinList([showingValue, pw, outerExp])

    innerExpForm1 = exponentForm(base1, innerExp1, False)
    innerExpForm2 = exponentForm(base2, innerExp2, False)

    needEndPart = False
    if (aExp != 1) and (baseExp1 != 1) :
        aExpForm = exponentForm(base1, baseExp1)
        valExpForm1 = exponentForm(aExpForm, aExp, False)
        needEndPart = True
    else :
        valExpForm1 = exponentForm(base1, valExp1, False)

    if (bExp != 1) and (baseExp2 != 1):
        bExpForm = exponentForm(base2, baseExp2)
        valExpForm2 = exponentForm(bExpForm, bExp, False)
        needEndPart = True
    else:
        valExpForm2 = exponentForm(base2, valExp2, False)

    givenValueFormula = joinList([givenValue, eqs, "( ", innerExpForm1, tss, innerExpForm2, " )", pw, outerExp,
                                  eqs, base1, pw, valExp1, tss, base2, pw, valExp2], "")

    if needEndPart :
        givenValueFormulaEndPart = joinList([eqs, valExpForm1, tss, valExpForm2])
        givenValueFormula += givenValueFormulaEndPart

    givenValueFormula += joinList([eqs, AExpForm, BExpForm], "")

    pairs = [(aExp, bExp)]
    # print(pairs)
    for _ in range(4):
        while True :
            aGap, bGap = random.choices(range(-1, 2), k=2)
            realTemp = (aGap+aExp, bGap+bExp)
            # print(pairs[0], realTemp)
            if (realTemp not in pairs) and (realTemp[0] > 0) and (realTemp[1] > 0) :
                pairs.append(realTemp)
                break

    pairs.sort()

    ansInd = pairs.index((aExp, bExp))

    # 선택지를 만듭니다.
    choices = list(map(lambda x : aT(exponentForm('A', x[0], False) + exponentForm("B", x[1], False)), pairs))

    # 내용을 채웁니다.
    stem = stem.format(largeAFormula=aT(aFormula), largeBFormula=aT(bFormula), givenValue=aT(givenValue),
                       A=aT("A"), B=aT("B"), s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenValueFormula=aT(givenValueFormula))

    return stem, answer, comment


def rationalandprime211_Stem_073():
    stem = "{aFormula}, {bFormula}, {cFormula}라 할 때, {givenValue}을 {A}, {B}, {C}를 사용하여 나타내시오. (단, {x}는 자연수이다)\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenValueFactorized}이므로\n{givenValueComment1}\n{givenValueComment2}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    while True :
        bases = sorted(random.sample([2, 3, 5, 7], k=3))
        exps = random.choices([1, 2, 3, 4], k=3)
        if len(set(exps)) == 1 :
            continue
        zipBaseExp = zip(bases, exps)
        showingValue = reduce(mul, map(lambda x : x[0]**x[1], zipBaseExp))

        if showingValue < 1000 :
            break

    chars = ["A", "B", "C"]

    charExpForms = list(map(lambda x: exponentForm(x[0], x[1], False), zip(chars, exps)))
    ansText = joinList(charExpForms)

    baseX = list(map(lambda x: joinList([" ", x, pw, "x "], ""), bases))

    formulas = makeEquality(baseX, chars, withTag=True)

    showingValueX = joinList([" ", showingValue, pw, "x "], "")

    showingValueFactorized = getFactoredIntFormula(showingValue)

    baseXDeveloped = []
    baseXSwapped = []
    for ind, exp in enumerate(exps) :
        if exp != 1 :
            baseXDeveloped.append(joinList([" ", bases[ind], pw, exp, "x "], ""))
            baseXSwapped.append(joinList([" ( ", bases[ind], pw, "x )^", exp, " "], ""))
        else :
            baseXDeveloped.append(baseX[ind])
            baseXSwapped.append(baseX[ind])

    givenValueFactorized = joinList([showingValue, eq, showingValueFactorized])
    givenValueComment1 = joinList([showingValueX, eq, "( ", showingValueFactorized, " )^x",
                                   eq, joinList(baseXDeveloped, ts)])
    givenValueComment2 = joinList([eq, joinList(baseXSwapped, ts), eq, ansText])

    # 내용을 채웁니다.
    stem = stem.format(aFormula=formulas[0], bFormula=formulas[1], cFormula=formulas[2], givenValue=aT(showingValueX),
                       A=aT("A"), B=aT("B"), C=aT("C"), x=aT('x'))
    answer = answer.format(a1=aT(ansText))
    comment = comment.format(givenValueFactorized=aT(givenValueFactorized), givenValueComment1=aT(givenValueComment1),
                             givenValueComment2=aT(givenValueComment2))

    return stem, answer, comment


def rationalandprime211_Stem_074():
    stem = "{aFormula}라 할 때, {givenFormula}이다. 이 때 상수 {k}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{aFormula}이므로\n{commentFormula1}\n{commentFormula2}\n{thusKa}\n{thusK}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    while True :
        base = random.choice(range(2, 10))
        basicExp = random.choice(range(20, 50, 5))
        firstExp, secondExp = random.choices(range(1, 5), k=2)
        firstCoeff = base**firstExp
        _secondCoeff = base**secondExp
        if firstCoeff < 100 and _secondCoeff < 100 :
            break

    # 정답을 계산합니다.
    kValSympy = sympify(joinList([firstCoeff, "- 1/",  _secondCoeff]))
    kValSplited = str(kValSympy).split("/")

    kValText = convertIntoHangul(str(kValSympy))

    # k값은 정수로 나올 수 없으므로 kValSplited의 길이에 따른 조건 확인은 생략합니다.
    numerator, denominator = list(map(int, kValSplited))

    firstCoeffExpForm = exponentForm(base, firstExp, False)
    _secondCoeffExpForm = exponentForm(base, secondExp, False)

    aFormula = joinList([base, pw, basicExp, eqs, 'a'], "")

    firstWholeForm = joinList([base, pw, basicExp+firstExp], "")
    secondWholeForm = joinList([base, pw, basicExp-secondExp], "")
    basicForm = joinList([base, pw, basicExp], "")

    givenFormulaLeft = joinList([firstWholeForm, mss, secondWholeForm])

    givenFormula = joinList([givenFormulaLeft, eq, 'ka'])

    commentFormula1 = joinList([firstWholeForm, eqs, base, "^{", firstExp, ps, basicExp, "}",
                               eqs, firstCoeffExpForm, tss, basicForm, eqs, firstCoeffExpForm, ' a'], "")
    if firstCoeffExpForm != str(firstCoeff) :
        commentFormula1 = joinList([commentFormula1, eq, firstCoeff, 'a'])

    commentFormula2 = joinList([secondWholeForm, eqs, base, "^{", basicExp, ms, secondExp, "}",
                                eqs, basicForm, dds, _secondCoeffExpForm, eqs, makeFractionFormula('a', _secondCoeffExpForm)], "")
    if _secondCoeffExpForm != str(_secondCoeff) :
        commentFormula2 = joinList([commentFormula2, eq, makeFractionFormula('a', _secondCoeff)])

    thusKa = joinList([thus, firstWholeForm, ms, secondWholeForm, eq, firstCoeff, 'a', ms, makeFractionFormula('a', _secondCoeff), eq, kValText, 'a'])

    thusK = joinList([thus, 'k', eq, kValText])

    ansInd, numerators = makeChoices(numerator, positiveWithoutZero=True, withTag=False)

    choices = []
    for num in numerators:
        temp = aT(convertIntoHangul(str(sympify(joinList([num, "/", denominator])))))
        choices.append(temp)

    # 내용을 채웁니다.
    stem = stem.format(aFormula=aT(aFormula), givenFormula=aT(givenFormula), k=aT('k'),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(aFormula=aT(aFormula), commentFormula1=aT(commentFormula1), commentFormula2=aT(commentFormula2),
                             thusKa=aT(thusKa), thusK=aT(thusK))

    return stem, answer, comment


def rationalandprime211_Stem_075():
    stem = "{aFormula}, {bFormula}라 할 때, {givenValue}을 {A}, {B}를 사용하여 바르게 나타낸 것은? (단, {x}는 2 이상의 자연수이다)\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{aFormulaExpanded}이므로 {base1XEq}\n{bFormulaExpanded}이므로 {base2XEq}\n" \
              "{thusGivenValueExpanded}\n{givenValueDeveloped}\n{towardAnswer}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    base1, base2 = sorted(random.sample([2, 3, 5, 7], k=2))
    while True :
        base1XExp, base2XExp = random.choices([-2, -1, 1, 2], k=2)
        base1OnlyExp, base2OnlyExp = random.choices(range(1, 7), k=2)
        base1MixedExp, base2MixedExp = random.choices(range(1, 4), k=2)
        base1OnlyValue = base1 ** base1OnlyExp
        base2OnlyValue = base2 ** base2OnlyExp
        base1base2Value = base1 ** base1MixedExp * base2 ** base2MixedExp

        if (base1OnlyValue > 125) or (base2OnlyValue > 125) or (base1base2Value > 100) :
            continue

        exps = [[base1OnlyExp, 0], [base1MixedExp, base2MixedExp], [0, base2OnlyExp]]
        whichToDivide = random.choice([0, 2])

        exps[whichToDivide] = [-i for i in exps[whichToDivide]]

        base1ExpSum = sum(map(lambda y: y[0], exps))
        base2ExpSum = sum(map(lambda y: y[1], exps))

        if base1ExpSum * base2ExpSum == 0 :
            continue

        tempValuesForFinalCoeffs = list(map(Integer, [base1, -base1XExp, base1ExpSum, base2, -base2XExp, base2ExpSum]))
        tempFinalCoeffSym = Rational((tempValuesForFinalCoeffs[0]**tempValuesForFinalCoeffs[1])**tempValuesForFinalCoeffs[2]
                                 * (tempValuesForFinalCoeffs[3]**tempValuesForFinalCoeffs[4])**tempValuesForFinalCoeffs[5])

        if (tempFinalCoeffSym.p < 1000) and (tempFinalCoeffSym.q < 1000):
            break

    # print(exps)
    # print(base1ExpSum, base2ExpSum)

    # 문제를 구성합니다.
    x, A, B = symbols("x A B", positive=True)

    aExpSym = x + base1XExp
    bExpSym = x + base2XExp

    aExpForm = exponentForm(base1, wrapParen(aExpSym), paren=False)
    bExpForm = exponentForm(base2, wrapParen(bExpSym), paren=False)

    aFormula = joinList([aExpForm, eq, "A"])
    bFormula = joinList([bExpForm, eq, "B"])

    givenNumbers = [base1OnlyValue, base1base2Value, base2OnlyValue]

    # givenNumbers = [(base1OnlyValue, a**(base1OnlyExp*x)), (base1base2Value, a**(base1MixedExp*x) * b**(base2MixedExp*x)),
    #                 (base2OnlyValue, b**(base2OnlyExp*x))]

    if whichToDivide == 0 :
        givenNumbers[0], givenNumbers[2] = givenNumbers[2], givenNumbers[0]

    givenValue = joinList([givenNumbers[0], pw, "x", tss, givenNumbers[1], pw, 'x', dds, givenNumbers[2], pw, 'x'], "")

    aBaseForm = exponentForm(base1, 'x', False)
    bBaseForm = exponentForm(base2, 'x', False)

    base1XExpSym = Integer(base1XExp)
    base2XExpSym = Integer(base2XExp)

    base1Sym = Integer(base1)
    base2Sym = Integer(base2)

    aFormulaExpandedRear = convertIntoHangul(str((base1Sym ** aExpSym).apart()), leaveTimes=True)
    bFormulaExpandedRear = convertIntoHangul(str((base2Sym ** bExpSym).apart()), leaveTimes=True)

    base1XSym = base1Sym ** (-base1XExpSym) * A
    base2XSym = base2Sym ** (-base2XExpSym) * B

    base1XReplaced = convertIntoHangul(str(base1XSym))
    base2XReplaced = convertIntoHangul(str(base2XSym))

    aFormulaExpanded = joinList([aExpForm, eq, aFormulaExpandedRear, eq, "A"])
    bFormulaExpanded = joinList([bExpForm, eq, bFormulaExpandedRear, eq, "B"])

    base1XEq = joinList([aBaseForm, eq, base1XReplaced])
    base2XEq = joinList([bBaseForm, eq, base2XReplaced])

    base1OnlySym = powdenest(base1**(base1OnlyExp*x))
    base2OnlySym = powdenest(base2**(base2OnlyExp*x))
    base1MixedSym = powdenest(base1**(base1MixedExp*x))
    base2MixedSym = powdenest(base2**(base2MixedExp*x))

    base1OnlyForm = convertIntoHangul(base1OnlySym, parenToBracket=True)
    base2OnlyForm = convertIntoHangul(base2OnlySym, parenToBracket=True)
    base1MixedForm = convertIntoHangul(base1MixedSym, parenToBracket=True)
    base2MixedForm = convertIntoHangul(base2MixedSym, parenToBracket=True)

    if base1ExpSum > 0 :
        base1Res1Exp = 1
    else :
        base1Res1Exp = -1

    if base2ExpSum > 0 :
        base2Res1Exp = 1
    else :
        base2Res1Exp = -1

    base1base2Res1Form = convertIntoHangul(str(A ** base1Res1Exp * B ** base2Res1Exp), leaveTimes=True)

    base1ExpSumAbs = abs(base1ExpSum)
    base2ExpSumAbs = abs(base2ExpSum)

    base1Res1Form = convertIntoHangul(powdenest(base1**(base1ExpSumAbs*x)), parenToBracket=True)
    base2Res1Form = convertIntoHangul(powdenest(base2**(base2ExpSumAbs*x)), parenToBracket=True)

    res1Form = base1base2Res1Form.replace("A", base1Res1Form)
    res1Form = res1Form.replace("B", base2Res1Form)

    if base1ExpSumAbs != 1 :
        base1XSemiFinalForm = exponentForm(exponentForm(base1, "x"), base1ExpSumAbs, False)
        base1XFinalForm = exponentForm(joinList(["left (", base1XReplaced, "right )"]), base1ExpSumAbs, False)
    else :
        base1XSemiFinalForm = aBaseForm
        base1XFinalForm = base1XReplaced
    if base2ExpSumAbs != 1 :
        base2XSemiFinalForm = exponentForm(exponentForm(base2, "x"), base2ExpSumAbs, False)
        base2XFinalForm = exponentForm(joinList(["left (", base2XReplaced, "right )"]), base2ExpSumAbs, False)
    else :
        base2XSemiFinalForm = bBaseForm
        base2XFinalForm = base2XReplaced

    res2Form = base1base2Res1Form.replace("A", wrapParen(base1XSemiFinalForm))
    res2Form = res2Form.replace("B", wrapParen(base2XSemiFinalForm))

    res3Form = base1base2Res1Form.replace("A", wrapParen(base1XFinalForm))
    res3Form = res3Form.replace("B", wrapParen(base2XFinalForm))

    # 식을 구성합니다.
    base1base2ValueFactored = getFactoredIntFormula(base1base2Value)
    if whichToDivide == 2 :
        front = base1OnlyForm
        end = base2OnlyForm
    else :
        front = base2OnlyForm
        end = base1OnlyForm

    thusGivenValueExpanded = joinList([thus, givenValue, eq, front, ts, "(", base1base2ValueFactored, ")^x", dd, end])
    givenValueDeveloped = joinList([eq, front, ts, base1MixedForm, ts, base2MixedForm, dd, end, eq, res1Form])


    pairs = [(base1ExpSum, base2ExpSum)]
    # print(pairs)
    for _ in range(4):
        while True :
            aGap, bGap = random.choices(range(-2, 3), k=2)
            realTemp = (aGap+base1ExpSum, bGap+base2ExpSum)

            tempValuesForFinalCoeffs = list(map(Integer, [base1, -base1XExp, realTemp[0], base2, -base2XExp, realTemp[1]]))
            tempFinalCoeffSym = Rational((tempValuesForFinalCoeffs[0] ** tempValuesForFinalCoeffs[1]) ** tempValuesForFinalCoeffs[2]
                                     * (tempValuesForFinalCoeffs[3] ** tempValuesForFinalCoeffs[4]) ** tempValuesForFinalCoeffs[5])

            if (realTemp not in pairs) and (tempFinalCoeffSym.p < 1000) and (tempFinalCoeffSym.q < 1000):
                pairs.append(realTemp)
                break

    pairs.sort()

    ansInd = pairs.index((base1ExpSum, base2ExpSum))

    # 선택지를 만듭니다.
    choices = []
    for ind in range(5):
        tempSym = base1XSym ** pairs[ind][0] * base2XSym ** pairs[ind][1]
        tempString = str(tempSym)

        if "/" in tempString :
            numerator, denominator = tempString.split('/')
            tempString = joinList(["(", numerator, ")", "/", denominator])

        tempText = convertIntoHangul(tempString, parenToBracket=True, timesToSpace=True)

        choices.append(tempText)

    resText = choices[ansInd]
    towardAnswer = joinList([eq, res2Form, eq, res3Form, eq, resText])

    choices = list(map(aT, choices))

    # 내용을 채웁니다.
    stem = stem.format(aFormula=aT(aFormula), bFormula=aT(bFormula), givenValue=aT(givenValue), A=aT("A"), B=aT("B"), x=aT("x"),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(aFormulaExpanded=aT(aFormulaExpanded), base1XEq=aT(base1XEq),
                             bFormulaExpanded=aT(bFormulaExpanded), base2XEq=aT(base2XEq),
                             thusGivenValueExpanded=aT(thusGivenValueExpanded), givenValueDeveloped=aT(givenValueDeveloped),
                             towardAnswer=aT(towardAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_076():
    stem = "{givenFormula}이 {n}자리 자연수이고, 각 자리의 숫자의 {optionText}을 {k}라 할 때, {nk}의 값은??\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaComment1}이므로\n{givenFormulaComment2}\n" \
              "따라서 {givenFormula}은 {nVal}자리 자연수이므로 {nFormula}\n" \
              "또, 각 자리 숫자의 합은 {sumFormula}이므로 {kFormula}\n" \
              "{thusAnswer}\n\n"

    # (어떤 수) * (10의 거듭제곱) 꼴
    tenExp = random.choice(range(5, 10))
    while True :
        mantissa = random.choice(range(11, 100))
        if isprime(mantissa) or (mantissa % 10 == 0):
            continue
        mantissaValue = mantissa
        mantissa = str(mantissa)
        break

    nVal = tenExp + 2
    kVal = int(mantissa[0]) + int(mantissa[1])
    isSum = random.choice([True, False])

    if isSum :
        ansValue = nVal + kVal
        optionText = "합"
        ansTextForm = joinList(['n', ps, 'k'])
    else :
        ansValue = nVal * kVal
        optionText = '곱'
        ansTextForm = joinList(['n', ts, 'k'])


    givenValue = mantissaValue * 10 ** tenExp
    givenFormula = getFactoredIntFormula(givenValue)

    mantissaFactored = getFactoredIntFormula(mantissa)

    givenFormulaComment1 = joinList([givenFormula, eqs, mantissaFactored, tss, "( 2 times 5 )^", tenExp], "")
    givenFormulaComment2 = joinList([eqs, mantissa, tss, "10^", tenExp], "")

    nFormula = joinList(['n', eq, nVal])

    sumFormula = joinList([mantissa[0], ps, mantissa[1], eq, kVal])

    kFormula = joinList(['k', eq, kVal])

    thusAnswer = joinList([thus, ansTextForm, eq, ansValue])

    ansInd, choices = makeChoices(ansValue, diff=2, positive=True, withTag=True)


    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), n=aT('n'), optionText=optionText, k=aT('k'), nk=aT(ansTextForm),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaComment1=aT(givenFormulaComment1), givenFormulaComment2=aT(givenFormulaComment2),
                             givenFormula=aT(givenFormula), nVal=aT(nVal), nFormula=aT(nFormula), sumFormula=aT(sumFormula),
                             kFormula=aT(kFormula), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_077():
    stem = "{questionFormula}의 자리수를 {n}이라 할 때, {n}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{questionFormulaComment1}\n{questionFormulaComment2}\n{ansValueFactored}\n" \
              "따라서 {questionFormula}은 {ansValue}자리 자연수이다.\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    while True :
        twoBase = random.choice([2, 4, 8])
        fiveBase = 5

        twoLength = random.choice(range(2, 6))
        fiveLength = random.choice(range(2, 6))

        twoExp = random.choice(range(2, 7))
        fiveExp = random.choice(range(3, 9))

        givenValue = twoBase ** twoExp * twoLength * fiveBase ** fiveExp * fiveLength

        givenValueFactoredText, givenValueFactoredDict = getFactoredIntFormula(givenValue, returnFactorDict=True)

        givenValueTwoExp = givenValueFactoredDict[2]
        givenValueFiveExp = givenValueFactoredDict[5]

        tenExp = min(givenValueTwoExp, givenValueFiveExp)

        mantissaValue = givenValue // 10 ** tenExp
        mantissa = str(mantissaValue)
        if mantissaValue < 500 :
            break

    twoExponentForm = exponentForm(twoBase, twoExp, paren=False)
    fiveExponentForm = exponentForm(fiveBase, fiveExp, paren=False)

    given1List = [twoExponentForm for _ in range(twoLength)]
    given2List= [fiveExponentForm for _ in range(fiveLength)]

    given1 = joinList(["(", joinList(given1List, ps), ")"])
    given2 = joinList(["(", joinList(given2List, ps), ")"])

    questionFormula = given1 + given2

    given1Simplified = joinList(["(", twoLength, ts, twoExponentForm, ")"])
    given2Simplified = joinList(["(", fiveLength, ts, fiveExponentForm, ")"])

    questionFormulaComment1 = joinList([questionFormula, eq, given1Simplified, given2Simplified])

    mantissaFactored = getFactoredIntFormula(mantissaValue)

    questionFormulaComment2 = joinList([eqs, mantissaFactored, tss, '( 2 times 5 )^', tenExp], "")
    ansValueFactored = joinList([eqs, mantissa, tss, '10^', tenExp], "")

    ansValue = len(mantissa) + tenExp

    # 선택지를 만듭니다.
    ansInd, choices = makeChoices(ansValue, withTag=True, positive=True)

    # 내용을 채웁니다.
    stem = stem.format(questionFormula=aT(questionFormula), n=aT('n'),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(questionFormulaComment1=aT(questionFormulaComment1), questionFormulaComment2=aT(questionFormulaComment2),
                             ansValueFactored=aT(ansValueFactored), questionFormula=aT(questionFormula), ansValue=aT(ansValue))

    return stem, answer, comment


def rationalandprime211_Stem_078():
    stem = "{questionFormula}의 자리수를 {n}이라 할 때, {n}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{questionFormulaComment1}\n{questionFormulaComment2}\n{ansValueFactored}\n" \
              "따라서 {questionFormula}은 {ansValue}자리 자연수이다.\n\n"

    # 문제에 사용할 숫자들을 생성합니다.
    # 문제 폼은 2**k * X ** k * 5 ** l / (X ** m * 5 ** m)의 형태입니다.
    while True :
        twoBase = random.choice([2, 4])
        fiveBase = 5
        otherBase = random.choice([3, 7, 11, 13])

        mVal, kVal, lVal = sorted(random.sample(range(2, 13), k=3))

        lMinusM = lVal - mVal
        kMinusM = kVal - mVal

        mantissa = otherBase ** kMinusM

        if lMinusM > kVal :
            tenExp = kVal
            mantissa = mantissa * fiveBase ** (lMinusM - kVal)
        else :
            tenExp = lMinusM
            mantissa = mantissa * twoBase ** (kVal - lMinusM)

        if mantissa < 500 :
            mantissaValue = mantissa
            mantissa = str(mantissa)
            break

    otherBaseTimesTwoBase = otherBase * twoBase
    otherBaseTimesFiveBase = otherBase * fiveBase
    otherBaseTimesFiveBaseFactored = getFactoredIntFormula(otherBaseTimesFiveBase)

    otherBaseTimesTwoBaseText = joinList(["(", twoBase, ts, otherBase, ")"])
    otherBaseTimesFiveBaseText = joinList(["(", otherBaseTimesFiveBaseFactored, ")"])

    givenNumerator = otherBaseTimesTwoBase ** kVal * fiveBase ** lVal
    givenDenominator = otherBaseTimesFiveBase ** mVal
    givenValue = givenNumerator // givenDenominator

    givenNumeratorFactored = getFactoredIntFormula(givenNumerator)
    givenDenominatorFactored = getFactoredIntFormula(givenDenominator)

    givenValueFactoredText, givenValueFactoredDict = getFactoredIntFormula(givenValue, returnFactorDict=True)

    mantissaFactored = getFactoredIntFormula(mantissaValue)

    givenNumeratorText = joinList([otherBaseTimesTwoBase, pw, kVal, tss, fiveBase, pw, lVal], "")
    givenDenominatorText = joinList([otherBaseTimesFiveBase, pw, mVal], "")

    questionFormula = makeFractionFormula(givenNumeratorText, givenDenominatorText)

    givenNumeratorText2 = joinList([otherBaseTimesTwoBaseText, pw, kVal, tss, fiveBase, pw, lVal], "")
    givenDenominatorText2 = joinList([otherBaseTimesFiveBaseText, pw, mVal], "")

    questionFormulaFactored1 = makeFractionFormula(givenNumeratorText2, givenDenominatorText2)
    questionFormulaFactored2 = makeFractionFormula(givenNumeratorFactored, givenDenominatorFactored)

    questionFormulaComment1 = joinList([questionFormula, eq, questionFormulaFactored1, eq, questionFormulaFactored2])

    questionFormulaComment2 = joinList([eqs, givenValueFactoredText, eqs, mantissaFactored, tss, '( 2 times 5 )^', tenExp], "")
    ansValueFactored = joinList([eqs, mantissa, tss, '10^', tenExp], "")

    ansValue = len(mantissa) + tenExp

    # 선택지를 만듭니다.
    ansInd, choices = makeChoices(ansValue, withTag=True, positive=True)

    # 내용을 채웁니다.
    stem = stem.format(questionFormula=aT(questionFormula), n=aT('n'),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(questionFormulaComment1=aT(questionFormulaComment1), questionFormulaComment2=aT(questionFormulaComment2),
                             ansValueFactored=aT(ansValueFactored), questionFormula=aT(questionFormula), ansValue=aT(ansValue))

    return stem, answer, comment


def rationalandprime211_Stem_079():
    stem = "{givenFormula}{postp} 만족시키는 자연수 {x}의 값을 구하시오. (단, {xLimit})\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{leftBaseItemsComments}이므로\n{secondCommentText}\n{secondCommentText2}\n" \
              "{rightPartEquation}이므로\n{leftRightSimplified}  {thusBaseX}\n{thusAnswer}\n\n"

    # 문제에 사용할 숫자들을 생성합니다.

    x = symbols('x', positive=True)

    while True:
        leftBase = random.choice(range(2, 10))
        leftBaseSym = Integer(leftBase)
        if leftBase in [6, 7, 8, 9] :
            expAdds = [-1, 0, 1]
            minExp = 1
        elif leftBase in [3, 4, 5] :
            expAdds = sorted(random.sample(range(-2, 3), k=3))
            minExp = 2
        else : # base == 2
            expAdds = sorted(random.sample(range(-3, 4), k=3))
            minExp = 3

        expXs = [x+a for a in expAdds]

        leftBaseXForms = [exponentForm(leftBase, str(form), paren=False) for form in expXs]
        leftBaseExpBasic = exponentForm(leftBase, 'x', False)

        leftPartItems = [leftBaseSym**e for e in expXs]
        leftPartX = sum(leftPartItems)
        leftPartXText = joinList(leftBaseXForms, pss)

        # print(leftPartX)

        xVal = random.choice(range(minExp, 10))
        rightPartValueSym = leftPartX.subs(x, xVal)
        rightBase = random.choice(range(2, 10))

        if isinstance(rightPartValueSym, Integer) and (rightPartValueSym < 600) and (rightPartValueSym >= rightBase ** 2):
            rightExp = 2
            while True:
                if (rightBase ** (rightExp + 1) < rightPartValueSym):
                    rightExp += 1
                else:
                    break
            break

    firstCommentItems = []
    for ind, val in enumerate(expAdds) :
        if val < 0 :
            tempDenom = exponentForm(leftBase, -val, False)
            tempFrac = makeFractionFormula(1, tempDenom)
            temp = joinList([leftBaseXForms[ind], eq, leftBaseExpBasic, dd, tempDenom, eq, tempFrac, ts, leftBaseExpBasic])
            firstCommentItems.append(aT(temp))
        elif val > 0 :
            tempCoeff = exponentForm(leftBase, val, False)
            temp = joinList([leftBaseXForms[ind], eq, tempCoeff, ts, leftBaseExpBasic])
            firstCommentItems.append(aT(temp))

    # print(leftPartX)
    leftBaseXValued = leftPartX.as_coefficient(leftBase**x)
    # print(leftBaseXValued)
    leftBaseXValuedText = convertIntoHangul(leftBaseXValued)

    leftPartCoeff = leftBaseXValued.cancel()
    leftPartCoeffText = convertIntoHangul(leftPartCoeff)

    rightPartExpForm = exponentForm(rightBase, rightExp, False)
    remainder = rightPartValueSym - rightBase ** rightExp
    postp = proc_jo(int(remainder) % 10, 1)
    rightPartFormula = joinList([rightPartExpForm, ps, remainder])

    givenFormula = joinList([leftPartXText, eq, rightPartFormula])

    xLimit = joinList(['x', rs, minExp])

    leftBaseItemsComments = joinList(firstCommentItems, ", ")


    secondCommentText = joinList([leftPartXText, eq, "left (", leftBaseXValuedText, "right )", ts, leftBaseExpBasic])
    leftSimplified = joinList([leftPartCoeffText, ts, leftBaseExpBasic])
    secondCommentText2 = joinList([eq, leftSimplified])

    rightPartEquation = joinList([rightPartFormula, eq, rightPartValueSym])
    leftRightSimplified = joinList([leftSimplified, eq, rightPartValueSym])

    thusBaseX = joinList([thus, leftBaseExpBasic, eqs, leftBase, pw, xVal], "")

    thusAnswer = joinList([thus, 'x', eq, xVal])


    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), postp=postp, x=aT('x'), xLimit=aT(xLimit))
    answer = answer.format(a1=aT(xVal))
    comment = comment.format(leftBaseItemsComments=leftBaseItemsComments, secondCommentText=aT(secondCommentText),
                             secondCommentText2=aT(secondCommentText2), rightPartEquation=aT(rightPartEquation),
                             leftRightSimplified=aT(leftRightSimplified), thusBaseX=aT(thusBaseX), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_080():
    stem = "다음 조건을 모두 만족시키는 자연수 {x}, {y}에 대하여 {questionFormula}의 값을 구하시오.\n" \
           "   ㈎ {givenFormula1}\n   ㈏ {givenFormula2}은 {y}자리 자연수이다.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n조건 ㈎에서\n{givenFormula1Comment1}\n{givenFormula1Comment2}\n{givenFormula1Comment3}\n{givenFormula1Comment4}  {thusX}\n\n" \
              "조건 ㈏에서\n{givenFormula2Comment1}\n{givenFormula2Comment2}\n" \
              "따라서 {givenFormula2}은 {yVal}자리 자연수이므로 {yFormula}\n" \
              "{thusAnswer}\n\n"

    # x의 값을 정합니다.
    xVal = random.choice(range(1, 7))

    # (가)에 사용할 밑을 정합니다.
    base = random.choice([2, 3])
    if base == 2 :
        baseExps = random.sample(range(2, 7), k=3)
    else :
        baseExps = random.sample(range(2, 5), k=3)

    baseExps.insert(0, 1)
    baseExps[:3] = sorted(baseExps[:3])

    # (가)의 지수에 사용할 일차식을 랜덤하게 만들고, 조건을 충족하는지 확인합니다.
    x = symbols('x', positive=True)
    # print(x)
    while True :
        a, c, e = random.choices(range(1, 4), k=3)
        b, d, f = random.choices(range(-5, 7), k=3)
        expPairs = [(a, b), (c, d), (e, f)]
        if len(set(expPairs)) != 3 :
            continue

        expFormulaSyms = [p[0] * x + p[1] for p in expPairs]
        expFormulaDevelopedSyms = [baseExps[i] * expFormulaSyms[i] for i in range(3)]
        expFormulaSumSym = sum(expFormulaDevelopedSyms)
        expFormulaSum = expFormulaSumSym.subs(x, xVal)

        quotient, remainder = divmod(expFormulaSum, baseExps[-1])
        if remainder :
            expFormulaSyms[0] -= remainder
            expFormulaDevelopedSyms = [baseExps[i] * expFormulaSyms[i] for i in range(3)]
            expFormulaSumSym = sum(expFormulaDevelopedSyms)
            expFormulaSum = expFormulaSumSym.subs(x, xVal)

        givenFormula1RightBaseExp = expFormulaSum // baseExps[-1]
        break

    expFormulaSymsText = list(map(convertIntoHangul, expFormulaSyms))
    expFormulaDevelopedSymsText = list(map(convertIntoHangul, expFormulaDevelopedSyms))
    expFormulaSumSymText = convertIntoHangul(expFormulaSumSym)

    # (어떤 수) * (10의 거듭제곱) 꼴
    tenExp = random.choice(range(3, 8))
    # print(tenExp)
    while True :
        mantissa = random.choice(range(11, 100))
        if isprime(mantissa) or (mantissa % 10 == 0):
            continue
        mantissaValue = mantissa
        mantissa = str(mantissa)
        break

    yVal = tenExp + 2

    questionFormulaDict = getRandomEquation(realValues=[xVal, yVal], avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']

    givenFormula1LeftList = [exponentForm(base**baseExps[i], str(expFormulaSymsText[i]), False) for i in range(3)]
    givenFormula1RightExpForm = exponentForm(base**baseExps[-1], givenFormula1RightBaseExp, False)
    givenFormula1RightParenList = []

    for ind, exp in enumerate(baseExps[:-1]) :
        if exp == 1 :
            givenFormula1RightParenList.append(givenFormula1LeftList[ind])
        else :
            givenFormula1RightParenList.append(exponentForm(exponentForm(base, exp), str(expFormulaSymsText[ind]), False))

    givenFormula1BaseSame = [exponentForm(base, str(expFormulaDevelopedSymsText[i]), False) for i in range(3)]
    givenFormula1Simplified = exponentForm(base, str(expFormulaSumSymText), False)

    if givenFormula1RightBaseExp != 1 :
        temp = joinList([givenFormula1RightExpForm,
                         eq, exponentForm(exponentForm(base, baseExps[-1]), givenFormula1RightBaseExp, False),
                         eq, exponentForm(base, expFormulaSum, False)])
    else :
        temp = joinList([givenFormula1RightExpForm, eq, exponentForm(base, expFormulaSum, False)])
    givenFormula1ValueDeveloped = aT(temp) + "이므로\n"

    givenFormula1ExpEquation = joinList([str(expFormulaSumSymText), eq, givenFormula1RightBaseExp*baseExps[-1]])

    thusX = joinList([thus, "x", eq, xVal])

    givenFormula1Left = joinList(givenFormula1LeftList, tss)
    givenFormula1 = joinList([givenFormula1Left, eq, givenFormula1RightExpForm])

    givenFormula1RightParen = joinList(givenFormula1RightParenList, tss)
    givenFormula1Comment1 = joinList([givenFormula1Left, eq, givenFormula1RightParen])

    givenFormula1Comment2Right = joinList(givenFormula1BaseSame, tss)
    givenFormula1Comment2 = joinList([eq, givenFormula1Comment2Right])
    givenFormula1Comment3 = joinList([eq, givenFormula1Simplified])

    givenFormula1Comment4 = joinList([givenFormula1ValueDeveloped, aT(givenFormula1ExpEquation)])



    givenFormula2Value = mantissaValue * 10 ** tenExp
    givenFormula2 = getFactoredIntFormula(givenFormula2Value)

    mantissaFactored = getFactoredIntFormula(mantissaValue)

    givenFormula2Comment1 = joinList([givenFormula2, eqs, mantissaFactored, tss, "( 2 times 5 )^", tenExp], "")
    givenFormula2Comment2 = joinList([eqs, mantissa, tss, "10^", tenExp], "")

    yFormula = joinList(['y', eq, yVal])

    thusAnswer = joinList([thus, questionFormula, eq, ansValue])

    # 내용을 채웁니다.
    stem = stem.format(questionFormula=aT(questionFormula), x=aT('x'), y=aT('y'), givenFormula1=aT(givenFormula1),
                       givenFormula2 = aT(givenFormula2))
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(givenFormula1Comment1=aT(givenFormula1Comment1), givenFormula1Comment2=aT(givenFormula1Comment2),
                             givenFormula1Comment3=aT(givenFormula1Comment3), givenFormula1Comment4=givenFormula1Comment4,
                             thusX=aT(thusX), givenFormula2Comment1=aT(givenFormula2Comment1), givenFormula2Comment2=aT(givenFormula2Comment2),
                             givenFormula2=aT(givenFormula2), yVal=aT(yVal), yFormula=aT(yFormula), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_081():
    stem = "{givenFormula}일 때, 상수 {a}, {b}, {c}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaLeft}\n{givenFormulaComment1}\n" \
              "{givenFormulaSimplified}\n이므로 {aFormula}, {bFormula}, {cFormula}\n" \
              "{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    # A, B, C = symbols("A B C", integer=True)
    # e1, e2, e3, e4, e5, e6, L1, L2, L3 = symbols("e1 e2 e3 e4 e5 e6 L1 L2 L3", positive=True)
    x, y = symbols("x y", positive=True)

    coeffs = random.choices([-3, -2, -1, 1, 2, 3], k=3)
    eVals = random.choices(range(1, 4), k=6)
    LVals = random.choices([1, 2], k=3)

    insideTermsSym = [coeffs[i] * x**eVals[i*2] * y**eVals[i*2+1] for i in range(3)]
    termsParenText = [exponentForm(str(convertIntoHangul(insideTermsSym[i], timesToSpace=True)), LVals[i], baseParen=True, paren=False) for i in range(3)]

    termsSym = [insideTermsSym[i]**LVals[i] for i in range(3)]
    termsDevelopedText = [convertIntoHangul(termsSym[i], timesToSpace=True) for i in range(3)]

    resSym = reduce(mul, termsSym)
    resText = convertIntoHangul(resSym, timesToSpace=True)

    aVal = reduce(mul, [coeffs[i]**LVals[i] for i in range(3)])
    bVal = sum([eVals[i*2-2]*LVals[i] for i in range(3)])
    cVal = sum([eVals[i*2-1]*LVals[i] for i in range(3)])

    questionFormulaDict = getRandomEquation(['a', 'b', 'c'], [(1, 3), (-3, 4), (-3, 4)], realValues=[aVal, bVal, cVal], avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']

    givenFormulaLeft = joinList(termsParenText, tss)
    givenFormula = joinList([givenFormulaLeft, eq, "a x^b y^c"])

    givenFormulaComment1Left = joinList(termsDevelopedText, tss)
    givenFormulaComment1 = joinList([eq, givenFormulaComment1Left])

    givenFormulaComment2 = joinList([eq, resText])

    aFormula = joinList(['a', eq, aVal])
    bFormula = joinList(['b', eq, bVal])
    cFormula = joinList(['c', eq, cVal])

    vals = [aVal, bVal, cVal]
    numberTerms = [vals[i] * questionFormulaDict['coeffs'][i] for i in range(3)]
    thusAnswer = joinList([thus, questionFormula, eq, getNumberCalc(numberTerms, withRes=True)])

    ansInd, choices = makeChoices(ansValue, diff=1, withTag=True)


    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), a=aT('a'), b=aT('b'), c=aT('c'), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaLeft=aT(givenFormulaLeft), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaSimplified = aT(givenFormulaComment2), aFormula=aT(aFormula), bFormula=aT(bFormula),
                             cFormula=aT(cFormula), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_082():
    stem = "{givenFormula}을 간단히 한 것은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}\n" \
              "{givenFormulaComment2}\n{givenFormulaComment3}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    # A, B, C = symbols("A B C", integer=True)
    # e1, e2, e3, e4, e5, e6, L1, L2, L3 = symbols("e1 e2 e3 e4 e5 e6 L1 L2 L3", positive=True)
    x, y = symbols("x y", positive=True)

    coeffs = random.choices([-3, -2, -1, 1, 2, 3], k=4)
    eVals = random.choices(range(1, 4), k=6)
    LVals = random.choices([2, 3], k=3)

    insideTermsSym = [coeffs[i] * x**eVals[i*2] * y**eVals[i*2+1] for i in range(2)]
    fractionInsideTermSym = coeffs[-2] * y ** eVals[-2] / (coeffs[-1] * x ** eVals[-1])
    insideTermsSym.append(fractionInsideTermSym)

    termsParenText = [exponentForm(convertIntoHangul(insideTermsSym[i], timesToSpace=True, parenToBracket=True, bracketToFrac=True, avoidNumMinus=True), LVals[i], baseParen=True, paren=False) for i in range(3)]
    # fractionTermParenText = exponentForm(convertIntoHangul(fractionInsideTermSym, parenToBracket=True), LVals[-1], baseParen=True, paren=False)
    # termsParenText.append(fractionTermParenText)

    # 선택지를 만듭니다.
    LValsForChoices = [LVals]
    choices = []
    for _ in range(4):
        while True :
            tempVals = random.choices([2, 3], k=3)
            if tempVals not in LValsForChoices :
                LValsForChoices.append(tempVals)
                break

    random.shuffle(LValsForChoices)
    ansInd = LValsForChoices.index(LVals)

    for ind, tempLVals in enumerate(LValsForChoices) :
        tempTermsSym = [insideTermsSym[i] ** tempLVals[i] for i in range(3)]
        if ind == ansInd :
            termsInitialSym = tempTermsSym[:]
        tempTermsSym[1:] = list(map(lambda x: x ** (-1), tempTermsSym[1:]))
        tempResSym = reduce(mul, tempTermsSym)
        tempResText = convertIntoHangul(latexToHwp(latex(tempResSym)), timesToSpace=True, parenToBracket=True, bracketToFrac=True, avoidNumMinus=True)
        choices.append(tempResText)

        if ind == ansInd :
            termsDevelopedText = [convertIntoHangul(latexToHwp(latex(tempTermsSym[i])), timesToSpace=True, parenToBracket=True, bracketToFrac=True, avoidNumMinus=True) for i in
                                      range(3)]
            resSym = tempResSym
            resText = tempResText

    givenFormula = joinList(termsParenText, dds)

    termsSymText = [convertIntoHangul(latexToHwp(latex(sym)), timesToSpace=True, parenToBracket=True, bracketToFrac=True, avoidNumMinus=True) for sym in termsInitialSym]

    givenFormulaComment1Right = joinList(termsSymText, dds)
    givenFormulaComment1 = joinList([eq, givenFormulaComment1Right])

    givenFormulaComment2Right = joinList(termsDevelopedText, tss)
    givenFormulaComment2 = joinList([eq, givenFormulaComment2Right])

    resSymCoeff, resSymChars = resSym.as_content_primitive()
    resCoeffText = convertIntoHangul(resSymCoeff)
    resCharsText = convertIntoHangul(latexToHwp(latex(resSymChars)), bracketToFrac=True, parenToBracket=True, timesToSpace=True, avoidNumMinus=True)

    givenFormulaComment3 = joinList([eq, resCoeffText, ts, resCharsText, eq, resText])

    choices = list(map(aT, choices))

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2 = aT(givenFormulaComment2), givenFormulaComment3=aT(givenFormulaComment3))

    return stem, answer, comment


def rationalandprime211_Stem_083():
    stem = "{givenFormula}일 때, 자연수 {a}, {b}, {c}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaComment1}\n{givenFormulaComment2}\n" \
              "즉, {givenFormulaComment3}이므로\n" \
              "{firstEquation}, {secondEquation}, {thirdEquation}\n" \
              "{thusABC}\n" \
              "{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    # A, B, C = symbols("A B C", integer=True)
    # e1, e2, e3, e4, e5, e6, L1, L2, L3 = symbols("e1 e2 e3 e4 e5 e6 L1 L2 L3", positive=True)
    x, y, A, B, C = symbols("x y A B C", integer=True)

    coeffValues = random.choices([1, 2, 3], k=2)
    eVals = random.choices(range(1, 4), k=4)
    LValValues = random.choices([1, 2], k=2)

    aVal = coeffValues[0]
    coeffs = [A, coeffValues[1]]

    bVal = LValValues[-1]
    LVals = [LValValues[0], B]

    insideTermsSym = [coeffs[i] * x**eVals[i*2] * y**eVals[i*2+1] for i in range(2)]
    termsParenText = [exponentForm(str(convertIntoHangul(insideTermsSym[i], timesToSpace=True)), LVals[i], baseParen=True, paren=False) for i in range(2)]

    termsSym = [insideTermsSym[i]**LVals[i] for i in range(2)]
    termsDevelopedText = [convertIntoHangul(expand_power_base(termsSym[i]), timesToSpace=True, parenToBracket=True) for i in range(2)]

    resSym = reduce(mul, termsSym)

    resSymSubed = resSym.subs([(A, aVal), (B, bVal)])
    resExps = resSymSubed.as_powers_dict()
    resCoeff = resSymSubed.as_content_primitive()[0]
    cVal = resExps[x]

    resReplacedSym = resCoeff * x ** C * y ** resExps[y]
    resText = convertIntoHangul(resReplacedSym, timesToSpace=True)

    # print(resSym)
    resSymImped = expand_power_base(powsimp(resSym.cancel()))
    resSymImpedText = str(resSymImped)
    # print(resSymImpedText)
    resSymImpedTextSplited = resSymImpedText.split("*x")
    aPart = resSymImpedTextSplited[0]

    firstParenOpenInd = resSymImpedTextSplited[1].index("(")
    secondParenOpenInd = resSymImpedTextSplited[1].index("(", firstParenOpenInd+1)

    firstParenCloseInd = resSymImpedTextSplited[1].index(")")
    secondParenCloseInd = resSymImpedTextSplited[1].index(")", firstParenCloseInd+1)

    bPart = resSymImpedTextSplited[1][firstParenOpenInd+1:firstParenCloseInd]
    cPart = resSymImpedTextSplited[1][secondParenOpenInd+1:secondParenCloseInd]

    aPartText = convertIntoHangul(aPart, leaveTimes=True)
    bPartText = convertIntoHangul(bPart)
    cPartText = convertIntoHangul(cPart)

    questionFormulaDict = getRandomEquation(['A', 'B', 'C'], [(-1, 3), (-3, 4), (-3, 4)], realValues=[aVal, bVal, cVal], avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']

    givenFormulaLeft = joinList(termsParenText, tss)
    givenFormula = joinList([givenFormulaLeft, eq, resText])

    givenFormulaComment1Right = joinList(termsDevelopedText, tss)
    givenFormulaComment1 = joinList([givenFormulaLeft, eq, givenFormulaComment1Right])

    givenFormulaComment2Right = convertIntoHangul(resSymImpedText, timesToSpace=True, parenToBracket=True)
    givenFormulaComment2 = joinList([eq, givenFormulaComment2Right])

    givenFormulaComment3 = joinList([givenFormulaComment2Right, eq, resText])

    firstEquation = joinList([aPartText, eq, resCoeff])
    secondEquation = joinList([bPartText, eq, C])
    thirdEquation = joinList([cPartText, eq, resExps[y]])

    aFormula = joinList(['A', eq, aVal])
    bFormula = joinList(['B', eq, bVal])
    cFormula = joinList(['C', eq, cVal])

    thusAbc = joinList([thus, aFormula, ",~", bFormula, ",~", cFormula])

    vals = [aVal, bVal, cVal]
    numberTerms = [vals[i] * questionFormulaDict['coeffs'][i] for i in range(3)]
    thusAnswer = joinList([thus, questionFormula, eq, getNumberCalc(numberTerms, withRes=True)])

    ansInd, choices = makeChoices(ansValue, diff=2, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), a=aT('A'), b=aT('B'), c=aT('C'), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaComment1=aT(givenFormulaComment1), givenFormulaComment2=aT(givenFormulaComment2),
                             givenFormulaComment3 = aT(givenFormulaComment3),
                             firstEquation=aT(firstEquation), secondEquation=aT(secondEquation), thirdEquation=aT(thirdEquation),
                             thusABC=aT(thusAbc), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_084():
    stem = "{givenFormula}일 때, {questionFormula}의 값은? (단, {A}, {B}는 자연수이다.)\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaComment1}\n" \
              "{givenFormulaComment2}\n이므로 {givenFormulaComment3}에서 {firstSquareEquations}  {thusFirstSquare}\n" \
              "{secondSquareEquation}  {thusSecondSquare}\n" \
              "따라서 {questionFormula}의 값은 {ansValue}이다.\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    # A, B, C = symbols("A B C", integer=True)
    # e1, e2, e3, e4, e5, e6, L1, L2, L3 = symbols("e1 e2 e3 e4 e5 e6 L1 L2 L3", positive=True)
    x, y, A, B = symbols("x y A B", positive=True)

    while True:
        coeffValues = random.choices([1, 2, 3, 4], k=3)
        eVals = random.choices(range(1, 4), k=4)
        LVals = random.choices([2, 3], k=2)

        AVal = coeffValues[-1]
        coeffs = coeffValues[:2] + [A]

        fractionInsideTermSym = coeffs[0] * y ** eVals[0] / (coeffs[1] * x ** eVals[1])
        secondInsideTermsSym = coeffs[2] * x**eVals[2] * y**eVals[3]
        insideTermsSym = [fractionInsideTermSym, secondInsideTermsSym]

        termsParenText = [exponentForm(latexToHwp(latex(insideTermsSym[i])), LVals[i], baseParen=True, paren=False) for i in range(len(insideTermsSym))]

        termsSym = [insideTermsSym[i] ** LVals[i] for i in range(2)]
        termsInitialSym = termsSym[:]
        termsSym[1:] = list(map(lambda x: x ** (-1), termsSym[1:]))
        resSym = reduce(mul, termsSym)
        resSymExps = resSym.as_powers_dict()

        if resSymExps[x] * resSymExps[y] != 0 and abs(resSymExps[y]) != 1:
            break


    resText = latexToHwp(latex(resSym))

    termsDevelopedText = [latexToHwp(latex(termsSym[i])) for i in range(2)]

    givenFormulaLeft = joinList(termsParenText, dds)

    termsSymText = [latexToHwp(latex(sym)) for sym in termsInitialSym]

    givenFormulaComment1Right = joinList(termsSymText, dds)
    givenFormulaComment1 = joinList([givenFormulaLeft, eq, givenFormulaComment1Right])

    givenFormulaComment2Right = joinList(termsDevelopedText, tss)
    givenFormulaComment2 = joinList([eq, givenFormulaComment2Right, eq, resText])

    resForShowingSym = resSym.subs(A, AVal)
    resForShowingExps = resForShowingSym.as_powers_dict()

    BVal = abs(resForShowingExps[y])
    resForShowingSymText = latexToHwp(latex(resForShowingSym))
    # print(resForShowingSymText, joinList(["y**", secondSqVal], ""))
    resForShowingSymText = resForShowingSymText.replace(joinList(["y^{", BVal, "}"], ""), "y^B")
    # print(resForShowingSymText)

    resForShowingReplacedText = resForShowingSymText

    givenFormula = joinList([givenFormulaLeft, eq, resForShowingReplacedText])

    givenFormulaComment3 = joinList([resText, eq, resForShowingReplacedText])

    resSymCoeff = resSym.as_coefficient(x**resForShowingExps[x]*y**resForShowingExps[y])
    resReplacedSymCoeff = resForShowingSym.as_content_primitive()[0]

    resCoeffText = latexToHwp(latex(resSymCoeff))
    resCharsText = latexToHwp(latex(resReplacedSymCoeff))

    resSymNumber = resSym / (x**resSymExps[x] * y**resSymExps[y] * A**resSymExps[A])

    firstSquareEquation1 = joinList([resCoeffText, eq, resCharsText])
    if abs(resSymExps[B]) != 1 :
        firstSquareEquation2 = joinList(["A^", abs(resSymExps[A]), eqs, resSymNumber*resReplacedSymCoeff**(-1)], "")
    else :
        firstSquareEquation2 = ""

    if firstSquareEquation2 :
        firstSquareEquations = joinList([firstSquareEquation1, ",~", firstSquareEquation2])
    else :
        firstSquareEquations = firstSquareEquation1

    thusFirstSquare = joinList([thus, "A", eq, AVal])

    secondSquareEquation = joinList(['y^', abs(resSymExps[y]), eqs, 'y^B'])
    thusSecondSquare = joinList([thus, "B", eq, BVal])

    values = [AVal, BVal]
    chars = ["A", "B"]

    questionFormulaDict = getRandomEquation(chars, realValues=values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']

    # print(ansValue)
    ansInd, choices = makeChoices(ansValue, diff=1, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), questionFormula=aT(questionFormula), A=aT(A), B=aT(B),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaComment1=aT(givenFormulaComment1), givenFormulaComment2=aT(givenFormulaComment2),
                             givenFormulaComment3=aT(givenFormulaComment3), firstSquareEquations=aT(firstSquareEquations),
                             thusFirstSquare=aT(thusFirstSquare), secondSquareEquation=aT(secondSquareEquation),
                             thusSecondSquare=aT(thusSecondSquare), questionFormula=aT(questionFormula), ansValue=aT(ansValue))

    return stem, answer, comment


def rationalandprime211_Stem_085():
    stem = "{givenFormula}일 때, 자연수 {A}, {B}, {C}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}    ② {s2}    ③ {s3}    ④ {s4}    ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaLeft}\n{givenFormulaComment1}\n" \
              "{givenFormulaComment2}\n즉, {givenFormulaComment3}이므로\n" \
              "{firstEquation}, {secondEquation}, {thirdEquation}\n{thusABC}\n{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    A, B, C = symbols("A B C", integer=True)
    # e1, e2, e3, e4, e5, e6, L1, L2, L3 = symbols("e1 e2 e3 e4 e5 e6 L1 L2 L3", positive=True)
    x, y = symbols("x y", positive=True)

    while True:
        coeffValues = random.choices([1, 2, 3, 4, 5, 6], k=4)
        eValValues = random.choices(range(1, 5), k=6)
        LVals = random.choices([1, 2], k=3)

        aVal = eValValues[1] #첫째항의 y의 지수
        eVals = eValValues[:]
        eVals[1] = A

        bVal = coeffValues[1] #둘째항 괄호 안의 계수
        coeffs = coeffValues[:]
        coeffs[1] = B

        insideTermsSym = [coeffs[i] * x ** eVals[i * 2] * y ** eVals[i * 2 + 1] for i in range(2)]
        fractionInsideTermSym = coeffs[-2] * y ** eVals[-2] / (coeffs[-1] * x ** eVals[-1])
        insideTermsSym.append(fractionInsideTermSym)

        termsSym = [insideTermsSym[i] ** LVals[i] for i in range(3)]
        termsSym[1:] = list(map(lambda x: x ** (-1), termsSym[1:]))
        resSym = reduce(mul, termsSym)

        resSymSubed = resSym.subs([(A, aVal), (B, bVal)])
        resSymSubedExps = resSymSubed.as_powers_dict()

        resSubedXExp = resSymSubedExps[x]
        resSubedYExp = resSymSubedExps[y]

        if resSubedXExp * resSubedYExp != 0 and abs(resSubedXExp) != 1:
            break

    resText = convertIntoHangul(resSym, timesToSpace=True, parenToBracket=True, bracketToFrac=True)
    termsParenText = [exponentForm(convertIntoHangul(insideTermsSym[i], timesToSpace=True, parenToBracket=True, bracketToFrac=True),
                                   LVals[i], baseParen=True, paren=False) for i in range(3)]

    givenFormulaLeft = joinList(termsParenText, dds)

    termsSymText = [convertIntoHangul(sym, timesToSpace=True, parenToBracket=True, bracketToFrac=True) for sym in termsSym]

    givenFormulaComment1Right = joinList(termsSymText, tss)
    givenFormulaComment1 = joinList([eq, givenFormulaComment1Right])

    givenFormulaComment2 = joinList([eq, resText])

    resSymPowerDict = resSym.as_powers_dict()
    resSymCoeff = simplify(resSym).as_coefficient(x**resSymPowerDict[x]*y**resSymPowerDict[y])
    resSymCoeffText = convertIntoHangul(resSymCoeff, timesToSpace=True, bracketToFrac=True, parenToBracket=True)

    resSymSubedText = str(resSymSubed)
    resSymSubedText = resSymSubedText.replace("x**" + str(resSubedXExp), "x**C")
    showingResText = convertIntoHangul(resSymSubedText, timesToSpace=True, bracketToFrac=True, parenToBracket=True)

    givenFormula = joinList([givenFormulaLeft, eq, showingResText])

    givenFormulaComment3 = joinList([resText, eq, showingResText])

    cVal = abs(resSubedXExp)

    if resSubedYExp < 0 :
        thirdEqLeftSym = resSymPowerDict[y] * -1
    else :
        thirdEqLeftSym = resSymPowerDict[y]

    thirdEqLeftText = convertIntoHangul(thirdEqLeftSym)
    thirdEquation = joinList([thirdEqLeftText, eq, abs(resSubedYExp)])

    resSymSubedCoeff = convertIntoHangul(resSymSubed.as_content_primitive()[0])

    firstEquation = joinList([resSymCoeffText, eq, resSymSubedCoeff])
    secondEquation = joinList([C, eq, cVal])

    aFormula = joinList(['A', eq, aVal])
    bFormula = joinList(['B', eq, bVal])
    cFormula = joinList(['C', eq, cVal])

    thusAbc = joinList([thus, aFormula, ",~", bFormula, ",~", cFormula])

    questionFormulaDict = getRandomEquation(['A', 'B', 'C'], [(-1, 3), (-3, 4), (-3, 4)], realValues=[aVal, bVal, cVal],
                                            avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']

    vals = [aVal, bVal, cVal]
    numberTerms = [vals[i] * questionFormulaDict['coeffs'][i] for i in range(3)]
    thusAnswer = joinList([thus, questionFormula, eq, getNumberCalc(numberTerms, withRes=True)])

    ansInd, choices = makeChoices(ansValue, diff=1, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), A=aT('A'), B=aT('B'), C=aT('C'), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaLeft=aT(givenFormulaLeft), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), givenFormulaComment3=aT(givenFormulaComment3),
                             firstEquation=aT(firstEquation), secondEquation=aT(secondEquation), thirdEquation=aT(thirdEquation),
                             thusABC=aT(thusAbc), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_086():
    stem = "다음은 {givenFormula}을 간단히 하는 과정에 대한 정호, 준형, 민서의 발표 내용이다.\n\n" \
           "   정호: {statement1}\n   준형: {statement2}\n   민서: {statement3}\n\n" \
           "옳은 말을 한 사람을 모두 고른 것은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}" \
              "{givenFormulaComment2}{givenFormulaComment3}\n따라서 옳은 말을 한 사람은 {answerPeople}이다.\n\n"

    #지수법칙을 정리합니다.
    identity1 = "x^a x^b = x^{a+b}"
    identity2 = "x div y = x times 1 over y"
    identity3 = "(xy)^n = x^n y^n"
    identity4 = "left ( y over x right )^n = y^n over x^n"
    identity5 = "( x^a )^b = x^{ab}"

    identities = [identity1, identity2, identity3, identity4, identity5]

    statements = [joinList([aT(identity), "을 반드시 사용해야 합니다."]) for identity in identities]

    corrects = set([0])
    while True :
        conditions = random.choices([True, False], k=3)
        if sum(conditions)!=0 and sum(conditions[1:])!=2 :
            break

    nonFracParen, fracParen, divide = conditions

    if nonFracParen :
        corrects = corrects.union([2, 4])
    if fracParen :
        corrects = corrects.union([2, 3, 4])
    if divide :
        corrects = corrects.union([1])

    wrongs = set(range(5)).difference(corrects)

    # 숫자를 만듭니다.
    x, y = sp.symbols("x y", positive=True)

    coeffs = random.choices([-3, -2, -1, 1, 2, 3], k=3)
    eVals = random.choices(range(1, 5), k=6)
    LVals = [1, 1, 1]

    insideTermsSym = [coeffs[i] * x ** eVals[i * 2] * y ** eVals[i * 2 + 1] for i in range(3)]

    if nonFracParen :
        LVals[0] = 2

    if fracParen :
        LVals[1] = 2
        insideTermsSym[1] = random.choice(range(1, 4)) * random.choice([1, x, y]) / insideTermsSym[1]

    termsParenText = [
        exponentForm(convertIntoHangul(insideTermsSym[i], timesToSpace=True, parenToBracket=True, bracketToFrac=True),
                     LVals[i], baseParen=True, paren=False) for i in range(3)]

    termsSym = [insideTermsSym[i] ** LVals[i] for i in range(3)]
    termsDevelopedText = [convertIntoHangul(termsSym[i], timesToSpace=True, parenToBracket=True, bracketToFrac=True) for i in range(3)]

    if divide :
        termsSymSecond = termsSym[:]
        termsSymSecond[2] = 1 / termsSymSecond[2]
        termsDevelopedTextSecond = [convertIntoHangul(termsSymSecond[i], timesToSpace=True, parenToBracket=True, bracketToFrac=True) for i in range(3)]
    else :
        termsSymSecond = ""

    if divide :
        resSym = reduce(mul, termsSymSecond)
        givenFormula = joinList([termsParenText[0], ts, termsParenText[1], dd, termsParenText[2]])
    else :
        resSym = reduce(mul, termsSym)
        givenFormula = joinList(termsParenText, tss)

    if sum(LVals) > 3 :
        if divide :
            givenFormulaComment1Left = joinList([termsDevelopedText[0], ts, termsDevelopedText[1], dd, termsDevelopedText[2]])
        else :
            givenFormulaComment1Left = joinList(termsDevelopedText, tss)
        givenFormulaComment1 = joinList([aT(joinList([eq, givenFormulaComment1Left])), "\n"])

    else :
        givenFormulaComment1 = ""

    if divide :
        givenFormulaComment2Left = joinList(termsDevelopedTextSecond, tss)
        givenFormulaComment2 = aT(joinList([eq, givenFormulaComment2Left])) + "\n"
    else :
        givenFormulaComment2 = ""

    resText = convertIntoHangul(resSym, timesToSpace=True, parenToBracket=True, bracketToFrac=True)
    givenFormulaComment3 = joinList([eq, resText])

    oneItems = ['ㄱ', 'ㄴ', 'ㄷ']
    twoItems = ['ㄱ, ㄴ', 'ㄱ, ㄷ', 'ㄴ, ㄷ']
    threeItems = ['ㄱ, ㄴ, ㄷ']

    items = oneItems + twoItems + threeItems

    _choiceItemInds = random.sample(range(7), k=5)
    _ansItemInd = _choiceItemInds[0]
    ansChars = items[_ansItemInd]

    ansItemIndsOrdered = sorted(_choiceItemInds)
    ansInd = ansItemIndsOrdered.index(_ansItemInd)

    ansStatementIndices = []
    if "ㄱ" in ansChars :
        ansStatementIndices.append(0)
    if "ㄴ" in ansChars :
        ansStatementIndices.append(1)
    if "ㄷ" in ansChars :
        ansStatementIndices.append(2)

    necessaryWrongs = 3 - len(ansStatementIndices)

    if necessaryWrongs > len(wrongs) :

        resSymForAnswers = 2 * resSym
        resTextForAnswers = convertIntoHangul(resSymForAnswers, timesToSpace=True, parenToBracket=True, bracketToFrac=True)
        wrongs.add(5)
    else :
        resTextForAnswers = resText
        corrects.add(5)


    lastStatement = joinList(["계산 결과는 ", aT(resTextForAnswers), "입니다."], "")
    statements.append(lastStatement)

    # print(conditions)
    # print(corrects)
    correctStatements = [statements[i] for i in random.sample(corrects, k=len(ansStatementIndices))]
    wrongStatements = [statements[i] for i in random.sample(wrongs, k=necessaryWrongs)]
    showings = ["", "", ""]

    for i in range(3):
        if i in ansStatementIndices :
            showings[i] = correctStatements.pop()
        else :
            showings[i] = wrongStatements.pop()

    itemsReplaced = []
    for item in items :
        temp = item.replace("ㄱ", "정호")
        temp = temp.replace("ㄴ", "준형")
        temp = temp.replace("ㄷ", "민서")
        itemsReplaced.append(temp)

    choices = [itemsReplaced[i] for i in ansItemIndsOrdered]

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), statement1=showings[0], statement2=showings[1], statement3=showings[2],
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=givenFormulaComment1, givenFormulaComment2=givenFormulaComment2,
                             givenFormulaComment3=aT(givenFormulaComment3), answerPeople=choices[ansInd])

    return stem, answer, comment


def rationalandprime211_Stem_087():
    stem = "{givenFormula}일 때, 자연수 {a}, {b}, {c}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaLeft}\n{givenFormulaComment1}\n{givenFormulaComment2}\n" \
              "즉, {givenFormulaComment3}이므로\n" \
              "{firstEquation}, {secondEquation}, {thirdEquation}\n" \
              "{thusABC}\n" \
              "{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    # A, B, C = symbols("A B C", integer=True)
    # e1, e2, e3, e4, e5, e6, L1, L2, L3 = symbols("e1 e2 e3 e4 e5 e6 L1 L2 L3", positive=True)
    x, y, A, B, C = symbols("x y A B C", integer=True)

    itemLength = 3
    while True :
        coeffs = random.choices([-1, -2, -3, 1, 2, 3], k=itemLength)
        coeffs[1] = abs(coeffs[1])
        eValValues = random.choices(range(1, 4), k=itemLength*2)
        LValValues = random.choices([1, 2], k=itemLength)

        aVal = LValValues[0]
        LVals = LValValues[:]
        LVals[0] = A

        bVal = eValValues[2]
        eVals = eValValues[:]
        eVals[2] = B

        insideTermsSym = [coeffs[i] * x**eVals[i*2] * y**eVals[i*2+1] for i in range(itemLength)]

        termsSym = [insideTermsSym[i]**LVals[i] for i in range(itemLength)]
        termsSym = list(map(expand_power_base, termsSym))

        resSym = reduce(mul, termsSym)

        resSymSubed = resSym.subs([(A, aVal), (B, bVal)])
        resExps = resSymSubed.as_powers_dict()
        charPartOfResSymSubed = x**resExps[x] * y**resExps[y]
        resCoeff = resSymSubed / charPartOfResSymSubed
        cVal = resCoeff

        if cVal > 0 :
            break

    termsParenText = [
        exponentForm(convertIntoHangul(insideTermsSym[i], timesToSpace=True), LVals[i], baseParen=True, paren=False) for
        i in range(itemLength)]
    termsDevelopedText = [convertIntoHangul(expand_power_base(termsSym[i]), timesToSpace=True, bracketToFrac=True) for i
                          in range(itemLength)]
    termsDevelopedText[1] = makeFractionFormula(1, termsDevelopedText[1])


    resReplacedSym = C * x ** resExps[x] * y ** resExps[y]
    resText = convertIntoHangul(resReplacedSym, timesToSpace=True, bracketToFrac=True)

    resSymExps = resSym.as_powers_dict()
    resSymCoeff = resSym / (x**resSymExps[x] * y**resSymExps[y])
    firstFormulaLeft = simplify(expand_power_base(resSymCoeff).cancel())
    firstFormulaLeftText = convertIntoHangul(firstFormulaLeft, timesToSpace=True, bracketToFrac=True)

    secondFormulaLeft = resSymExps[x]
    secondFormulaLeftText = convertIntoHangul(secondFormulaLeft)

    thirdFormulaLeft = resSymExps[y]
    thirdFormulaLeftText = convertIntoHangul(thirdFormulaLeft)

    questionFormulaDict = getRandomEquation(['A', 'B', 'C'], [(-1, 3), (-3, 4), (-3, 4)], realValues=[aVal, bVal, cVal], avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']

    givenFormulaLeft = joinList([termsParenText[0], dd, termsParenText[1], ts, termsParenText[2]])
    givenFormula = joinList([givenFormulaLeft, eq, resText])

    givenFormulaComment1Right = joinList(termsDevelopedText, tss)
    givenFormulaComment1 = joinList([eq, givenFormulaComment1Right])

    resSymText = convertIntoHangul(powsimp(resSym.cancel()), timesToSpace=True, bracketToFrac=True)
    givenFormulaComment2Right = resSymText
    givenFormulaComment2 = joinList([eq, givenFormulaComment2Right])

    givenFormulaComment3 = joinList([givenFormulaComment2Right, eq, resText])

    firstEquation = joinList([firstFormulaLeftText, eq, C])
    secondEquation = joinList([secondFormulaLeftText, eq, resExps[x]])
    thirdEquation = joinList([thirdFormulaLeftText, eq, resExps[y]])

    aFormula = joinList(['A', eq, aVal])
    bFormula = joinList(['B', eq, bVal])
    cFormula = joinList(['C', eq, cVal])

    thusAbc = joinList([thus, aFormula, ",~", bFormula, ",~", cFormula])

    vals = [aVal, bVal, cVal]
    numberTerms = [vals[i] * questionFormulaDict['coeffs'][i] for i in range(itemLength)]
    thusAnswer = joinList([thus, questionFormula, eq, getNumberCalc(numberTerms, withRes=True)])

    ansInd, choices = makeChoices(ansValue, diff=2, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), a=aT('A'), b=aT('B'), c=aT('C'), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaLeft=aT(givenFormulaLeft), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), givenFormulaComment3 = aT(givenFormulaComment3),
                             firstEquation=aT(firstEquation), secondEquation=aT(secondEquation), thirdEquation=aT(thirdEquation),
                             thusABC=aT(thusAbc), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_088():
    stem = "어떤 식에 {multiplier}를 곱해야 할 것을 잘못하여 나누었더니 계산 결과가 {divideRes}이다. 바르게 계산한 답은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n어떤 식을 {A}라 하면 {ADivideFormula}\n{thusA}\n" \
              "따라서 바르게 계산하면\n{AMultipliedFormula}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    # A, B, C = symbols("A B C", integer=True)
    # e1, e2, e3, e4, e5, e6, L1, L2, L3 = symbols("e1 e2 e3 e4 e5 e6 L1 L2 L3", positive=True)
    a, b = symbols("a b", positive=True)

    multiplierChars = ['a', 'b']
    if random.choice(multiplierChars) == "a":
        aExp = 1
        bExp = random.choice(range(-9, 0))
    else:
        aExp = random.choice(range(-9, 0))
        bExp = 1

    aCoeff, bCoeff = random.choices(range(1, 5), k=2)
    multiplierSym = aCoeff * a ** aExp * bCoeff * b ** bExp

    itemLength = 5
    count = 0
    formulas = []
    while count < itemLength :
        coeff = random.choice(range(1, 10))
        eVals = random.choices(range(1, 5), k=2)

        tempTermSym = coeff * a**eVals[0] * b**eVals[1]

        if tempTermSym not in formulas :
            formulas.append(tempTermSym)
            count += 1

    ansInd = random.choice(range(5))
    AFormulaSym = formulas[ansInd]
    AFormulaText = convertIntoHangul(AFormulaSym, timesToSpace=True, bracketToFrac=True)

    multiplierText = convertIntoHangul(multiplierSym, timesToSpace=True, bracketToFrac=True)
    divideResSym = AFormulaSym / multiplierSym
    divideResText = convertIntoHangul(divideResSym, timesToSpace=True, bracketToFrac=True)

    choicesSym = [multiplierSym * sym for sym in formulas]
    multipliedResSym = choicesSym[ansInd]
    multipliedResText = convertIntoHangul(multipliedResSym, timesToSpace=True, bracketToFrac=True)

    ADivideFormula = joinList(["A", dd, multiplierText, eq, divideResText])
    thusA = joinList([thus, "A", eq, divideResText, ts, multiplierText, eq, AFormulaText])

    AMultipliedFormula = joinList(["A", ts, multiplierText, eq, AFormulaText, ts, multiplierText, eq, multipliedResText])

    choices = list(map(lambda x: aT(convertIntoHangul(x, timesToSpace=True, bracketToFrac=True)), choicesSym))


    # 내용을 채웁니다.
    stem = stem.format(multiplier=aT(multiplierText), divideRes=aT(divideResText),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(A=aT("A"), ADivideFormula=aT(ADivideFormula), thusA=aT(thusA), AMultipliedFormula=aT(AMultipliedFormula))

    return stem, answer, comment


def rationalandprime211_Stem_089():
    stem = "빈칸 {A}에 알맞은 식은?\n\n" \
           "   {givenFormula}\n\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaComment1}\n{givenFormulaComment2}\n{givenFormulaComment3}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    # A, B, C = symbols("A B C", integer=True)
    # e1, e2, e3, e4, e5, e6, L1, L2, L3 = symbols("e1 e2 e3 e4 e5 e6 L1 L2 L3", positive=True)
    a, b = symbols("a b", positive=True)

    coeffs = random.choices(range(1, 13), k=2)
    eVals = random.choices(range(1, 5), k=4)

    termsSym = [coeffs[i] * a ** eVals[i*2] * b ** eVals[i*2+1] for i in range(2)]

    itemLength = 5
    count = 0
    formulas = []
    while count < itemLength :
        coeff = random.choice(range(1, 9))
        eVals = random.choices(range(1, 5), k=2)

        tempTermSym = coeff * a**eVals[0] * b**eVals[1]

        if tempTermSym not in formulas :
            formulas.append(tempTermSym)
            count += 1

    ansInd = random.choice(range(5))

    termsSymText = list(map(lambda x: convertIntoHangul(x, timesToSpace=True, bracketToFrac=True), termsSym))

    choicesSym = [termsSym[0] * 1/termsSym[1] * sym for sym in formulas]
    AResSym = choicesSym[ansInd]
    AResText = convertIntoHangul(AResSym, timesToSpace=True, bracketToFrac=True)

    thirdItemSym = formulas[ansInd]
    thirdItemText = convertIntoHangul(thirdItemSym, timesToSpace=True, bracketToFrac=True)

    showingResSym = termsSym[1] / thirdItemSym * AResSym
    showingResText = convertIntoHangul(showingResSym, timesToSpace=True, bracketToFrac=True)

    aForm = "(~~ A~~)"

    givenFormula = joinList([termsSymText[1], dd, thirdItemText, ts, aForm, eq, termsSymText[0]])
    givenFormulaComment1 = joinList([aForm, eq, termsSymText[0], dd, termsSymText[1], ts, thirdItemText])
    givenFormulaComment2 = joinList([eq, termsSymText[0], ts, makeFractionFormula(1, termsSymText[1]), ts, thirdItemText])
    givenFormulaComment3 = joinList([eq, AResText])

    choices = list(map(lambda x: aT(convertIntoHangul(x, timesToSpace=True, bracketToFrac=True)), choicesSym))

    # 내용을 채웁니다.
    stem = stem.format(A=aT(aForm), givenFormula=aT(givenFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaComment1=aT(givenFormulaComment1), givenFormulaComment2=aT(givenFormulaComment2),
                             givenFormulaComment3=aT(givenFormulaComment3))

    return stem, answer, comment


def rationalandprime211_Stem_090():
    stem = "{givenAFormula}, {givenBFormula}일 때, 두 식 {A}, {B}에 대하여 {questionFormula}의 계산 결과로 알맞은 것은?\n\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenAFormulaComment}\n{givenBFormulaComment}\n{thusQuestionFormulaComment1}\n{thusQuestionFormulaComment2}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    # A, B, C = symbols("A B C", integer=True)
    # e1, e2, e3, e4, e5, e6, L1, L2, L3 = symbols("e1 e2 e3 e4 e5 e6 L1 L2 L3", positive=True)
    x, A, B = symbols("x A B", positive=True)

    coeffs = random.sample(range(1, 9), k=4)
    eVals = random.sample([1, 2, 3, 4], k=4)

    termsSym = [coeffs[i] * x ** eVals[i] for i in range(4)]

    itemLength = 5
    count = 0
    largeCharNums = []
    while count < itemLength :
        coeffs = random.sample(range(1, 4), k=2)
        eVals = random.sample(range(1, 3), k=2)

        tempNums = coeffs + eVals

        if tempNums not in largeCharNums :
            largeCharNums.append(tempNums)
            count += 1

    ansInd = random.choice(range(5))

    termsSymText = list(map(lambda x: convertIntoHangul(x, timesToSpace=True, bracketToFrac=True), termsSym))

    givenAFormula = joinList([termsSymText[0], ts, "A", eq, termsSymText[1]])
    givenBFormula = joinList([termsSymText[2], dd, "B", eq, termsSymText[3]])

    AFormulaSym = termsSym[1] / termsSym[0]
    BFormulaSym = termsSym[2] / termsSym[3]

    AFormulaText = convertIntoHangul(convertNegExp(AFormulaSym), timesToSpace=True, bracketToFrac=True)
    BFormulaText = convertIntoHangul(convertNegExp(BFormulaSym), timesToSpace=True, bracketToFrac=True)

    inversedForA = 1 / termsSym[0]
    inversedForAText = convertIntoHangul(convertNegExp(inversedForA), timesToSpace=True, bracketToFrac=True)

    inversedForB = 1 /termsSym[3]
    inversedForBText = convertIntoHangul(convertNegExp(inversedForB), timesToSpace=True, bracketToFrac=True)

    givenAFormulaComment = joinList(["A", eq, termsSymText[1], ts, inversedForAText, eq, AFormulaText])
    givenBFormulaComment = joinList(["B", eq, termsSymText[2], ts, inversedForBText, eq, BFormulaText])

    choicesSym = [tempNums[0]*AFormulaSym**tempNums[2] / (tempNums[1]*BFormulaSym**tempNums[3]) for tempNums in largeCharNums]

    ansCharNums = largeCharNums[ansInd]
    questionFormulaAPart = ansCharNums[0] * A**ansCharNums[2]
    questionFormulaBPart = ansCharNums[1] * B**ansCharNums[3]

    questionFormulaAPartText = convertIntoHangul(questionFormulaAPart, timesToSpace=True, bracketToFrac=True)
    questionFormulaBPartText = convertIntoHangul(questionFormulaBPart, timesToSpace=True, bracketToFrac=True)

    questionFormula = joinList([questionFormulaAPartText, dd, questionFormulaBPartText])

    if ansCharNums[0] == 1 :
        aCoeffText = ""
    else :
        aCoeffText = joinList([ansCharNums[0], ts])

    if ansCharNums[1] == 1 :
        bCoeffText = ""
    else:
        bCoeffText = joinList([ansCharNums[1], ts])

    AFormulaSymExped = ansCharNums[0] * AFormulaSym ** ansCharNums[2]
    BFormulaSymExped = 1/ (ansCharNums[1] * BFormulaSym ** ansCharNums[3])

    AFormulaSymExpedText = convertIntoHangul(convertNegExp(AFormulaSymExped), timesToSpace=True, bracketToFrac=True)
    BFormulaSymExpedText = convertIntoHangul(convertNegExp(BFormulaSymExped), timesToSpace=True, bracketToFrac=True)

    choices = list(map(lambda x: aT(convertIntoHangul(convertNegExp(x), timesToSpace=True, bracketToFrac=True)), choicesSym))

    thusQuestionFormulaComment = joinList([thus, questionFormulaAPartText, dd, questionFormulaBPartText, eq,
                                           aCoeffText, exponentForm(AFormulaText, ansCharNums[2], paren=False, baseParen=True),
                                           dd, "left (", bCoeffText, exponentForm(BFormulaText, ansCharNums[3], paren=False, baseParen=True), "right )"])

    resText = convertIntoHangul(convertNegExp(choicesSym[ansInd]), timesToSpace=True, bracketToFrac=True)

    thusQuestionFormulaComment2 = joinList([eq, AFormulaSymExpedText, ts, BFormulaSymExpedText, eq, resText])

    # 내용을 채웁니다.
    stem = stem.format(givenAFormula=aT(givenAFormula), givenBFormula=aT(givenBFormula), A=aT('A'), B=aT('B'), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenAFormulaComment=aT(givenAFormulaComment), givenBFormulaComment=aT(givenBFormulaComment),
                             thusQuestionFormulaComment1=aT(thusQuestionFormulaComment), thusQuestionFormulaComment2=aT(thusQuestionFormulaComment2))

    return stem, answer, comment


def rationalandprime211_Stem_091():
    stem = "두 식 {a}, {b}에 대하여 ◎, ☆을 {definition1}, {definition2}로 약속하자. 이 때, 다음을 만족하는 두 식 {A}, {B}에 대하여 {questionFormula}의 계산 결과로 알맞은 것은?\n\n" \
           "   {givenAFormula},  {givenBFormula}\n\n" \
           "  ① {s1}    ② {s2}    ③ {s3}    ④ {s4}    ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenAFormulaComment1}이므로 {givenAFormulaComment2}\n{thusA}\n" \
              "{givenBFormulaComment1}이므로 {givenBFormulaComment2}\n{thusB}\n" \
              "{thusQuestionFormulaComment1}\n{thusQuestionFormulaComment2}\n\n"

    definition1 = "a`◎`b`=`ab^2"
    definition2 = "a`☆`b` =`a^2 b"


    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    # A, B, C = symbols("A B C", integer=True)
    # e1, e2, e3, e4, e5, e6, L1, L2, L3 = symbols("e1 e2 e3 e4 e5 e6 L1 L2 L3", positive=True)
    x, y, A, B = symbols("x y A B", positive=True)

    itemLength = 4

    coeffs = random.choices(range(1, 7), k=itemLength)
    eVals = random.choices([1, 2, 3], k=itemLength*2)

    termsSym = [coeffs[i] * x**eVals[i*2] * y**eVals[i*2+1] for i in range(itemLength)]

    AFormulaSym = termsSym[0]
    BFormulaSym = termsSym[-1]

    itemLength = 5
    count = 0
    largeCharNums = []
    while count < itemLength :
        coeffs = random.sample(range(1, 4), k=2)
        eVals = random.sample(range(1, 3), k=2)

        tempNums = coeffs + eVals

        if tempNums not in largeCharNums :
            largeCharNums.append(tempNums)
            count += 1

    ansInd = random.choice(range(5))

    termsSymText = list(map(lambda x: convertIntoHangul(x, timesToSpace=True, bracketToFrac=True), termsSym))

    givenASecondSquared = termsSym[1]**2
    givenASecondSquaredText = convertIntoHangul(givenASecondSquared, timesToSpace=True)

    givenBFirstSquared = termsSym[2]**2
    givenBFirstSquaredText = convertIntoHangul(givenBFirstSquared, timesToSpace=True)

    givenAResSym = termsSym[0] * givenASecondSquared
    givenBResSym = givenBFirstSquared * termsSym[3]

    givenAResText = convertIntoHangul(givenAResSym, timesToSpace=True)
    givenBResText = convertIntoHangul(givenBResSym, timesToSpace=True)

    givenAFormulaLeft = joinList(["A`◎`", termsSymText[1]])
    givenAFormula = joinList([givenAFormulaLeft, eq, givenAResText])
    givenBFormulaLeft = joinList([termsSymText[2], "`☆`B"])
    givenBFormula = joinList([givenBFormulaLeft, eq, givenBResText])

    givenAFormulaComment1 = joinList([givenAFormulaLeft, eq, "A", ts, exponentForm(termsSymText[1], 2, False, True), eq, givenASecondSquaredText, "A"])
    givenAFormulaComment2 = joinList([givenASecondSquaredText, "A", eq, givenAResText])
    thusA = joinList([thus, "A", eq, makeFractionFormula(givenAResText, givenASecondSquaredText), eq, termsSymText[0]])

    givenBFormulaComment1 = joinList([givenBFormulaLeft, eq, exponentForm(termsSymText[2], 2, False, True), ts, "B", eq, givenBFirstSquaredText, "B"])
    givenBFormulaComment2 = joinList([givenBFirstSquaredText, "B", eq, givenBResText])
    thusB = joinList([thus, "B", eq, makeFractionFormula(givenBResText, givenBFirstSquaredText), eq, termsSymText[-1]])

    AFormulaText = convertIntoHangul(convertNegExp(AFormulaSym), timesToSpace=True, bracketToFrac=True)
    BFormulaText = convertIntoHangul(convertNegExp(BFormulaSym), timesToSpace=True, bracketToFrac=True)

    choicesSym = [tempNums[0]*AFormulaSym**tempNums[2] / (tempNums[1]*BFormulaSym**tempNums[3]) for tempNums in largeCharNums]

    ansCharNums = largeCharNums[ansInd]
    questionFormulaAPart = ansCharNums[0] * A**ansCharNums[2]
    questionFormulaBPart = ansCharNums[1] * B**ansCharNums[3]

    questionFormulaAPartText = convertIntoHangul(questionFormulaAPart, timesToSpace=True, bracketToFrac=True)
    questionFormulaBPartText = convertIntoHangul(questionFormulaBPart, timesToSpace=True, bracketToFrac=True)

    questionFormula = joinList([questionFormulaAPartText, dd, questionFormulaBPartText])

    if ansCharNums[0] == 1 :
        aCoeffText = ""
    else :
        aCoeffText = joinList([ansCharNums[0], ts])

    if ansCharNums[1] == 1 :
        bCoeffText = ""
    else:
        bCoeffText = joinList([ansCharNums[1], ts])

    AFormulaSymExped = ansCharNums[0] * AFormulaSym ** ansCharNums[2]
    BFormulaSymExped = 1/ (ansCharNums[1] * BFormulaSym ** ansCharNums[3])

    AFormulaSymExpedText = convertIntoHangul(convertNegExp(AFormulaSymExped), timesToSpace=True, bracketToFrac=True)
    BFormulaSymExpedText = convertIntoHangul(convertNegExp(BFormulaSymExped), timesToSpace=True, bracketToFrac=True)

    choices = list(map(lambda x: aT(convertIntoHangul(convertNegExp(x), timesToSpace=True, bracketToFrac=True)), choicesSym))

    thusQuestionFormulaComment = joinList([thus, questionFormulaAPartText, dd, questionFormulaBPartText, eq,
                                           aCoeffText, exponentForm(AFormulaText, ansCharNums[2], paren=False, baseParen=True),
                                           dd, "left (", bCoeffText, exponentForm(BFormulaText, ansCharNums[3], paren=False, baseParen=True), "right )"])

    resText = convertIntoHangul(convertNegExp(choicesSym[ansInd]), timesToSpace=True, bracketToFrac=True)

    thusQuestionFormulaComment2 = joinList([eq, AFormulaSymExpedText, ts, BFormulaSymExpedText, eq, resText])

    # 내용을 채웁니다.
    stem = stem.format(a=aT("a"), b=aT("b"), definition1=aT(definition1), definition2=aT(definition2), A=aT('A'), B=aT('B'),
                       questionFormula=aT(questionFormula), givenAFormula=aT(givenAFormula), givenBFormula=aT(givenBFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenAFormulaComment1=aT(givenAFormulaComment1), givenAFormulaComment2=aT(givenAFormulaComment2), thusA=aT(thusA),
                             givenBFormulaComment1=aT(givenBFormulaComment1), givenBFormulaComment2=aT(givenBFormulaComment2), thusB=aT(thusB),
                             thusQuestionFormulaComment1=aT(thusQuestionFormulaComment), thusQuestionFormulaComment2=aT(thusQuestionFormulaComment2))

    return stem, answer, comment


def rationalandprime211_Stem_092():
    stem = "{givenFormula}일 때, 상수 {a}, {b}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaLeft}\n{givenFormulaComment1}\n{givenFormulaComment2}\n" \
              "따라서 {aFormula}, {bFormula}이므로\n" \
              "{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    # A, B, C = symbols("A B C", integer=True)
    # e1, e2, e3, e4, e5, e6, L1, L2, L3 = symbols("e1 e2 e3 e4 e5 e6 L1 L2 L3", positive=True)
    x, y, a, b, c, d = symbols("x y a b c d", real=True)
    replacePairs = [('a', 'x'), ('b', 'y'), ('c', 'x'), ('d', 'y')]

    itemLength = 4
    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    coeffs = random.choices(oneDigitInts, k=itemLength)
    denomSeed = random.choice(range(1, 10))
    multiplier = random.choice(range(2, 5))
    firstDenom, secondDenom = [denomSeed, denomSeed*multiplier]
    secondFracMinusOrPlus = random.choice([1, -1])

    firstFracNumeratorSym = (coeffs[0]*a + coeffs[1]*b)
    secondFracNumeratorSym = (coeffs[2]*c + coeffs[3]*d)

    firstFracNumeratorText = convertIntoHangul(firstFracNumeratorSym, parenToBracket=True)
    firstFracNumeratorText = stringReplace(firstFracNumeratorText, replacePairs)
    secondFracNumeratorText = convertIntoHangul(secondFracNumeratorSym, parenToBracket=True)
    secondFracNumeratorText = stringReplace(secondFracNumeratorText, replacePairs)

    firstFracText= makeFractionFormula(firstFracNumeratorText, firstDenom)
    secondFracText = makeFractionFormula(secondFracNumeratorText, secondDenom)

    if secondFracMinusOrPlus == 1 :
        middleOpr = ps
    else :
        middleOpr = ms

    givenFormulaLeft = joinList([firstFracText, middleOpr, secondFracText])
    givenFormula = joinList([givenFormulaLeft, eq, "ax + by"])

    fracSumNumeratorSym = firstFracNumeratorSym * multiplier + secondFracMinusOrPlus * secondFracNumeratorSym
    fracSumNumeratorText = convertIntoHangul(fracSumNumeratorSym)
    fracSumNumeratorText = stringReplace(fracSumNumeratorText, replacePairs)

    fracSumText = makeFractionFormula(fracSumNumeratorText, secondDenom)

    givenFormulaComment1Left = fracSumText

    fracSumNumeratorSymSubed = fracSumNumeratorSym.subs([(a, x), (b, y), (c, x), (d, y)])
    fracSumNumeratorSymSubedText = convertIntoHangul(fracSumNumeratorSymSubed)
    fracSumSubedText = makeFractionFormula(fracSumNumeratorSymSubedText, secondDenom)
    givenFormulaComment1Right = fracSumSubedText

    givenFormulaComment1 = joinList([eq, givenFormulaComment1Left, eq, givenFormulaComment1Right])

    fracSumSymSubed = fracSumNumeratorSymSubed / secondDenom
    finalFormSlicedFromPoly = str(fracSumSymSubed.as_poly())[5:].split(", ")[0]
    finalFormText = convertIntoHangul(finalFormSlicedFromPoly, minusWithSpace=True, timesToSpace=True)

    givenFormulaComment2 = joinList([eq, finalFormText])

    fracSumCoeffs = fracSumSymSubed.as_coefficients_dict()

    aVal, bVal = fracSumCoeffs[x], fracSumCoeffs[y]
    aValText = convertIntoHangul(aVal, minusWithSpace=True)
    bValText = convertIntoHangul(bVal, minusWithSpace=True)

    aFormula = joinList(['a', eq, aValText])
    bFormula = joinList(['b', eq, bValText])

    questionFormulaDict = getRandomEquation(['a', 'b'], realValues=[aVal, bVal], avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']
    questionFormulaCoeffs = questionFormulaDict['coeffs']

    questionFormulaCalc = getNumberCalc([aVal*questionFormulaCoeffs[0], bVal*questionFormulaCoeffs[1]], withRes=True)
    questionFormulaCalc = convertIntoHangul(questionFormulaCalc, minusWithSpace=True)
    thusAnswer = joinList([thus, questionFormula, eq, questionFormulaCalc])

    ansInd, choiceDiffs = makeChoices(0, diff=1, withTag=False)
    choiceValues = [ansValue+int(i) for i in choiceDiffs]
    # choiceValuesText = [str(x).replace("-", "- ") for x in choiceValues]
    choices = list(map(lambda x: aT(convertIntoHangul(x, parenToBracket=True, minusWithSpace=True)), choiceValues))


    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), a=aT('a'), b=aT('b'), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaLeft=aT(givenFormulaLeft), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), aFormula=aT(aFormula), bFormula=aT(bFormula),
                             thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_093():
    stem = "{givenFormula}를 계산한 결과는?\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}\n{givenFormulaComment2}\n{givenFormulaComment3}\n" \
              "{givenFormulaComment4}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    positives = random.choices(range(1, 10), k=6)
    posnegs = random.choices(oneDigitInts, k=2)

    vars = [x, x, y, x, x, y, y]

    #식 구성
    # part1 - [part2 - {part3 - part4(part5) - part6}]
    # = part1 - {part2 - (part3 part45 - part6)}
    # = part1 - {part2 - (part3456)}
    # = part1 - (part23456)
    # = part123456

    formulaPart1 = positives[0] * vars[0]
    formulaPart2 = positives[1] * vars[1] + posnegs[0] * vars[2]
    formulaPart3 = positives[2] * vars[3]
    formulaPart4 = positives[3]
    if formulaPart4 == 1 :
        formulaPart4 += 1
    formulaPart5 = positives[4] * vars[4] + posnegs[1] * vars[5]
    formulaPart6 = positives[5] * vars[6]

    givenFormula = joinList([formulaPart1, "- [", formulaPart2, "- left {", formulaPart3, "-", formulaPart4, "(", formulaPart5, ") -", formulaPart6, "right } ]"])
    givenFormula = convertIntoHangul(givenFormula)

    formulaPart45 = -1 * formulaPart4 * formulaPart5
    givenFormulaComment1 = joinList([eq, formulaPart1, "- left {", formulaPart2, "- (", formulaPart3, formulaPart45, "-", formulaPart6, ") right }"])
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1)

    formulaPart3456 = formulaPart3 + formulaPart45 - formulaPart6
    givenFormulaComment2 = joinList([eq, formulaPart1, "- left {", formulaPart2, "- (", formulaPart3456, ") right }"])
    givenFormulaComment2 = convertIntoHangul(givenFormulaComment2)

    formulaPart23456 = formulaPart2 - formulaPart3456
    givenFormulaComment3 = joinList([eq, formulaPart1, "- (", formulaPart23456, ")"])
    givenFormulaComment3 = convertIntoHangul(givenFormulaComment3)

    formulaPart123456 = formulaPart1 - formulaPart23456
    givenFormulaComment4 = joinList([eq, formulaPart123456])
    givenFormulaComment4 = convertIntoHangul(givenFormulaComment4)

    ansInd, choiceXCoeffs = makeChoices(0, diff=1, withTag=False)
    # print(choiceXCoeffs)
    choiceXCoeffs.remove(0)

    _, choiceYCoeffs = makeChoices(0, diff=2, withTag=False)
    choiceYCoeffs.remove(0)

    finalFormCoeffs= formulaPart123456.as_coefficients_dict()
    ansXCoeff = finalFormCoeffs[x]
    ansYCoeff = finalFormCoeffs[y]

    choices = []
    for i in range(4):
        tempForm = (choiceXCoeffs[i]+ansXCoeff)*x + (choiceYCoeffs[i]+ansYCoeff)*y
        tempFormText = convertIntoHangul(tempForm)
        choices.append(aT(tempFormText))

    ansForm = aT(convertIntoHangul(formulaPart123456))
    choices.insert(ansInd, ansForm)


    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), givenFormulaComment3=aT(givenFormulaComment3),
                             givenFormulaComment4=aT(givenFormulaComment4))

    return stem, answer, comment


def rationalandprime211_Stem_094():
    stem = "{givenFormula}{postp} 계산했을 때, {x}의 계수와 상수항의 합은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}\n{givenFormulaComment2}\n" \
              "따라서 {x}의 계수는 {xCoeff}, 상수항은 {constant}이므로 구하는 합은 {ansValue}이다.\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    numbers = random.choices(oneDigitInts, k=6)

    #식 구성
    # (part1) - (part2)
    # = part1 -part2
    # = part12

    formulaPart1 = numbers[0]*x + numbers[1]*y + numbers[2]
    formulaPart2 = abs(numbers[3])*x + numbers[4]*y + numbers[5]

    givenFormula = joinList(["(", formulaPart1, ") - (", formulaPart2, ")"])
    givenFormula = convertIntoHangul(givenFormula)

    formulaPart2Neg = -formulaPart2
    givenFormulaComment1 = joinList([eq, formulaPart1, formulaPart2Neg])
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1)

    formulaPart12 = formulaPart1 + formulaPart2Neg
    givenFormulaComment2 = joinList([eq, formulaPart12])
    givenFormulaComment2 = convertIntoHangul(givenFormulaComment2)

    finalFormCoeffs= formulaPart12.as_coefficients_dict()
    xCoeff = finalFormCoeffs[x]
    constant = finalFormCoeffs[1]

    ansValue = xCoeff + constant

    ansInd, choices = makeChoices(ansValue, diff=1, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), postp=proc_jo(abs(numbers[-1]), 1), x=aT('x'),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), x=aT('x'), xCoeff=aT(xCoeff), constant=aT(constant),
                             ansValue=aT(ansValue))

    return stem, answer, comment


def rationalandprime211_Stem_095():
    stem = "{givenFormula}일 때, 상수 {a}, {b}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaLeft}\n{givenFormulaComment1}\n{givenFormulaComment2}\n" \
              "따라서 {aFormula}, {bFormula}이므로\n" \
              "{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    # A, B, C = symbols("A B C", integer=True)
    # e1, e2, e3, e4, e5, e6, L1, L2, L3 = symbols("e1 e2 e3 e4 e5 e6 L1 L2 L3", positive=True)
    x, y, a, b, c, d = symbols("x y a b c d", real=True)
    replacePairs = [('a', 'x'), ('b', 'y'), ('c', 'x'), ('d', 'y')]

    itemLength = 4
    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    coeffs = random.choices(oneDigitInts, k=itemLength)
    denomSeed = random.choice(range(1, 10))
    multiplier = random.choice(range(2, 5))
    firstDenom, secondDenom = [denomSeed*multiplier, denomSeed]
    biggerDenom = denomSeed * multiplier
    secondFracMinusOrPlus = random.choice([1, -1])

    firstFracNumeratorSym = (coeffs[0]*a + coeffs[1]*b)
    secondFracNumeratorSym = (coeffs[2]*c + coeffs[3]*d)

    firstFracNumeratorText = convertIntoHangul(firstFracNumeratorSym, parenToBracket=True)
    firstFracNumeratorText = stringReplace(firstFracNumeratorText, replacePairs)
    secondFracNumeratorText = convertIntoHangul(secondFracNumeratorSym, parenToBracket=True)
    secondFracNumeratorText = stringReplace(secondFracNumeratorText, replacePairs)

    firstFracText= makeFractionFormula(firstFracNumeratorText, firstDenom)
    secondFracText = makeFractionFormula(secondFracNumeratorText, secondDenom)

    if secondFracMinusOrPlus == 1 :
        middleOpr = ps
    else :
        middleOpr = ms

    givenFormulaLeft = joinList([firstFracText, middleOpr, secondFracText])
    givenFormula = joinList([givenFormulaLeft, eq, "ax + by"])

    fracSumNumeratorSym = firstFracNumeratorSym + secondFracMinusOrPlus * secondFracNumeratorSym * multiplier
    fracSumNumeratorText = convertIntoHangul(fracSumNumeratorSym)
    fracSumNumeratorText = stringReplace(fracSumNumeratorText, replacePairs)

    fracSumText = makeFractionFormula(fracSumNumeratorText, biggerDenom)

    givenFormulaComment1Left = fracSumText

    fracSumNumeratorSymSubed = fracSumNumeratorSym.subs([(a, x), (b, y), (c, x), (d, y)])
    fracSumNumeratorSymSubedText = convertIntoHangul(fracSumNumeratorSymSubed)
    fracSumSubedText = makeFractionFormula(fracSumNumeratorSymSubedText, biggerDenom)
    givenFormulaComment1Right = fracSumSubedText

    givenFormulaComment1 = joinList([eq, givenFormulaComment1Left, eq, givenFormulaComment1Right])

    fracSumSymSubed = fracSumNumeratorSymSubed / biggerDenom
    finalFormSlicedFromPoly = str(fracSumSymSubed.as_poly())[5:].split(", ")[0]
    finalFormText = convertIntoHangul(finalFormSlicedFromPoly, minusWithSpace=True, timesToSpace=True)

    givenFormulaComment2 = joinList([eq, finalFormText])

    fracSumCoeffs = fracSumSymSubed.as_coefficients_dict()

    aVal, bVal = fracSumCoeffs[x], fracSumCoeffs[y]
    aValText = convertIntoHangul(aVal, minusWithSpace=True)
    bValText = convertIntoHangul(bVal, minusWithSpace=True)

    aFormula = joinList(['a', eq, aValText])
    bFormula = joinList(['b', eq, bValText])

    questionFormulaDict = getRandomEquation(['a', 'b'], realValues=[aVal, bVal], avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']
    questionFormulaCoeffs = questionFormulaDict['coeffs']

    questionFormulaCalc = getNumberCalc([aVal*questionFormulaCoeffs[0], bVal*questionFormulaCoeffs[1]], withRes=True)
    questionFormulaCalc = convertIntoHangul(questionFormulaCalc, minusWithSpace=True)
    thusAnswer = joinList([thus, questionFormula, eq, questionFormulaCalc])

    ansInd, choiceDiffs = makeChoices(0, diff=1, withTag=False)
    choiceValues = [ansValue+int(i) for i in choiceDiffs]
    # choiceValuesText = [str(x).replace("-", "- ") for x in choiceValues]
    choices = list(map(lambda x: aT(convertIntoHangul(x, parenToBracket=True, minusWithSpace=True)), choiceValues))


    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), a=aT('a'), b=aT('b'), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaLeft=aT(givenFormulaLeft), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), aFormula=aT(aFormula), bFormula=aT(bFormula),
                             thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_096():
    stem = "{givenFormula}일 때, 세 상수 {ABC}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaLeft}\n{givenFormulaComment1}\n{givenFormulaComment2}\n" \
              "{givenFormulaComment3}이므로 {AFormula}, {BFormula}, {CFormula}\n{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x = symbols("x", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    numbers = random.choices(oneDigitInts, k=6)

    #식 구성
    # (part1) - (part2)
    # = part1 -part2
    # = part12

    formulaPart1 = numbers[0]*x**2 + numbers[1]*x + numbers[2]
    formulaPart2 = abs(numbers[3])*x**2 + numbers[4]*x + numbers[5]

    givenFormulaLeft = joinList(["(", formulaPart1, ") - (", formulaPart2, ")"])
    givenFormulaLeft = convertIntoHangul(givenFormulaLeft)

    givenFormulaRight = "Ax^2 + Bx + C"

    givenFormula = joinList([givenFormulaLeft, eq, givenFormulaRight])

    formulaPart2Neg = -formulaPart2
    givenFormulaComment1 = joinList([eq, formulaPart1, formulaPart2Neg])
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1)

    formulaPart12 = formulaPart1 + formulaPart2Neg
    formulaPart12Text = convertIntoHangul(formulaPart12)
    givenFormulaComment2 = joinList([eq, formulaPart12Text])

    givenFormulaComment3 = joinList([formulaPart12Text, eq, givenFormulaRight])

    finalFormCoeffs= formulaPart12.as_coefficients_dict()
    AVal = finalFormCoeffs[x**2]
    BVal = finalFormCoeffs[x]
    CVal = finalFormCoeffs[1]
    values = [AVal, BVal, CVal]

    ValueFormulas = makeEquality(["A", "B", "C"], values, withTag=True)

    questionFormulaDict = getRandomEquation(["A", "B", "C"], [(1, 4), (-1, 2), (-2, 3)], values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    questionFormulaCoeff = questionFormulaDict['coeffs']
    ansValue = questionFormulaDict['ansValue']

    ansValueEq = getNumberCalc([questionFormulaCoeff[i]*values[i] for i in range(3)], withRes=True)
    thusAnswer = joinList([thus, questionFormula, eq, ansValueEq])

    ansInd, choices = makeChoices(ansValue, diff=2, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), ABC=aT(joinList(["A", "B", "C"], ",~ ")), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaLeft=aT(givenFormulaLeft), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), givenFormulaComment3=aT(givenFormulaComment3),
                             AFormula=ValueFormulas[0], BFormula=ValueFormulas[1], CFormula=ValueFormulas[2], thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_097():
    stem = "{givenFormula}를 계산하면 {x}의 계수와 상수항이 모두 {x2}의 계수와 같다. 이 때 상수 {a}, {b}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}\n{givenFormulaComment2}\n" \
              "따라서 {xCoeffEq}, {constantEq}이므로 {aFormula}, {bFormula}이다.\n" \
              "{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, a, z = symbols("x a z", real=True)
    replacePairs = [('z', 'b')]

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))
    while True :
        numbers = random.choices(oneDigitInts, k=6)
        if numbers[0] != abs(numbers[3]) :
            break

    # 식 구성
    # (part1) - (part2)
    # = part1 -part2
    # = part12

    formulaPart1 = numbers[0] * x ** 2 + a * x + numbers[2]
    formulaPart2 = abs(numbers[3]) * x ** 2 + numbers[4] * x + z

    formulaPart1Text = getPolyText(formulaPart1, x)
    formulaPart2Text = getPolyText(formulaPart2, x)

    # print(formulaPart1, formulaPart2)

    givenFormula = joinList(["(", formulaPart1Text, ") - (", formulaPart2Text, ")"])
    givenFormula = convertIntoHangul(givenFormula)
    givenFormula = stringReplace(givenFormula, replacePairs)

    formulaPart2Neg = -formulaPart2
    formulaPart2NegText = getPolyText(formulaPart2Neg, x)
    givenFormulaComment1 = joinList([eq, formulaPart1Text, formulaPart2NegText])
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1)
    givenFormulaComment1 = stringReplace(givenFormulaComment1, replacePairs)

    formulaPart12 = formulaPart1 + formulaPart2Neg
    formulaPart12Text = getPolyText(formulaPart12, x)
    formulaPart12Text = convertIntoHangul(formulaPart12Text, timesToSpace=True)
    givenFormulaComment2 = joinList([eq, formulaPart12Text])
    givenFormulaComment2 = stringReplace(givenFormulaComment2, replacePairs)

    x2Coeff = formulaPart12.coeff(x**2)
    xCoeff = formulaPart12.coeff(x)
    xCoeffText = convertIntoHangul(xCoeff)
    constant = (formulaPart12 - x**2 * x2Coeff - xCoeff * x).cancel()
    constantText = convertIntoHangul(constant)
    constantText = stringReplace(constantText, replacePairs)

    xCoeffEq = joinList([xCoeffText, eq, x2Coeff])
    constantEq = joinList([constantText, eq, x2Coeff])

    # print(formulaPart12)
    aVal = solve(Eq(xCoeff, x2Coeff))[0]
    bVal = solve(Eq(constant, x2Coeff))[0]
    values = [aVal, bVal]
    # print(values)

    aFormula = joinList(['a', eq, aVal])
    bFormula = joinList(['b', eq, bVal])

    questionFormulaDict = getRandomEquation(['a', 'b'], realValues=values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    questionFormulaCoeff = questionFormulaDict['coeffs']
    ansValue = questionFormulaDict['ansValue']

    ansValueEq = getNumberCalc([questionFormulaCoeff[i]*values[i] for i in range(2)], withRes=True)
    thusAnswer = joinList([thus, questionFormula, eq, ansValueEq])

    ansInd, choices = makeChoices(ansValue, diff=2, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), x=aT('x'), x2 = aT('x^2'), a=aT('a'), b=aT('b'), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), xCoeffEq=aT(xCoeffEq), constantEq=aT(constantEq),
                             aFormula=aT(aFormula), bFormula=aT(bFormula), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_098():
    stem = "{givenFormula}일 때, {a2}의 계수를 {p}, {a}의 계수를 {q}라 하자. 두 상수 {p}, {q}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}\n{givenFormulaComment2}\n" \
              "{pFormula}, {qFormula}이므로 {ansFormula}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    a = symbols("a", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    numbers = random.choices(oneDigitInts, k=6)

    #식 구성
    # (part1) - (part2)
    # = part1 -part2
    # = part12

    formulaPart1 = numbers[0]*a**2 + numbers[1]*a + numbers[2]
    formulaPart2 = abs(numbers[3])*a**2 + numbers[4]*a + numbers[5]

    givenFormula = joinList(["(", formulaPart1, ") - (", formulaPart2, ")"])
    givenFormula = convertIntoHangul(givenFormula)

    formulaPart2Neg = -formulaPart2
    givenFormulaComment1 = joinList([eq, formulaPart1, formulaPart2Neg])
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1)

    formulaPart12 = formulaPart1 + formulaPart2Neg
    formulaPart12Text = convertIntoHangul(formulaPart12)
    givenFormulaComment2 = joinList([eq, formulaPart12Text])

    finalFormCoeffs= formulaPart12.as_coefficients_dict()
    pVal = finalFormCoeffs[a**2]
    qVal = finalFormCoeffs[a]

    values = [pVal, qVal]
    variables = ['p', 'q']
    ValueFormulas = makeEquality(variables, values, withTag=True)

    questionFormulaDict = getRandomEquation(variables, realValues=values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    questionFormulaCoeff = questionFormulaDict['coeffs']
    ansValue = questionFormulaDict['ansValue']

    ansValueEq = getNumberCalc([questionFormulaCoeff[i]*values[i] for i in range(2)], withRes=True)
    ansFormula = joinList([questionFormula, eq, ansValueEq])

    ansInd, choices = makeChoices(ansValue, diff=2, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), a2=aT("a^2"), a=aT("a"), p=aT("p"), q=aT("q"), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2),
                             pFormula=ValueFormulas[0], qFormula=ValueFormulas[1], ansFormula=aT(ansFormula))

    return stem, answer, comment


def rationalandprime211_Stem_099():
    stem = "{givenFormula}일 때, 상수 {a}, {b}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}\n{givenFormulaComment2}\n{givenFormulaComment3}\n" \
              "{givenFormulaComment4}\n따라서 {aFormula}, {bFormula}이므로 {ansFormula}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    positives = random.choices(range(1, 10), k=5)
    posnegs = random.choices(range(-9, 0), k=1)

    vars = [y, x, x, y, y]

    #식 구성
    # part1 - [part2 - {part3(part4) + part5}]
    # = part1 - {part2 - (part34 - part5)}
    # = part1 - (part2 part345)
    # = part1 - (part2345)
    # = part12345

    formulaPart1 = positives[0] * vars[0]
    formulaPart2 = positives[1] * vars[1]
    formulaPart3 = positives[2]
    if formulaPart3 == 1 :
        formulaPart3 += 1
    formulaPart4 = positives[3] * vars[2] + posnegs[0] * vars[3]
    formulaPart5 = positives[4] * vars[4]

    givenFormula = joinList([formulaPart1, "- [", formulaPart2, "- left {", formulaPart3, "(", formulaPart4, ") +", formulaPart5, "right } ]"])
    givenFormula = convertIntoHangul(givenFormula)

    formulaPart34 = formulaPart3 * formulaPart4
    givenFormulaComment1 = joinList([eq, formulaPart1, "- left {", formulaPart2, "- (", formulaPart34, "+", formulaPart5, ") right }"])
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1)

    formulaPart345 = formulaPart34 + formulaPart5
    givenFormulaComment2 = joinList([eq, formulaPart1, "- left {", formulaPart2, "- (", formulaPart345, ") right }"])
    givenFormulaComment2 = convertIntoHangul(givenFormulaComment2)

    formulaPart2345 = formulaPart2 - formulaPart345
    givenFormulaComment3 = joinList([eq, formulaPart1, "- (", formulaPart2345, ")"])
    givenFormulaComment3 = convertIntoHangul(givenFormulaComment3)

    formulaPart12345 = formulaPart1 - formulaPart2345
    givenFormulaComment4 = joinList([eq, formulaPart12345])
    givenFormulaComment4 = convertIntoHangul(givenFormulaComment4)

    finalFormCoeffs= formulaPart12345.as_coefficients_dict()
    aVal = finalFormCoeffs[x]
    bVal = finalFormCoeffs[y]

    values = [aVal, bVal]
    chars = ['a', 'b']

    questionFormulaDict = getRandomEquation(givenChars=chars, coefficientRange=[(1, 4), (-2, 3)], realValues=values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']
    questionFormulaCoeffs = questionFormulaDict['coeffs']

    ansInd, choices = makeChoices(ansValue, diff=2)

    ansValueEq = getNumberCalc([questionFormulaCoeffs[i]*values[i] for i in range(2)], withRes=True)
    ansFormula = joinList([questionFormula, eq, ansValueEq])

    aFormula, bFormula = makeEquality(chars, values, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), a=aT('a'), b=aT('b'), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), givenFormulaComment3=aT(givenFormulaComment3),
                             givenFormulaComment4=aT(givenFormulaComment4), aFormula=aT(aFormula), bFormula=aT(bFormula),
                             ansFormula=aT(ansFormula))

    return stem, answer, comment


def rationalandprime211_Stem_100():
    stem = "{givenFormula}일 때, {X}에 들어갈 알맞은 식은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      \n" \
           "④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaLeft}\n{givenFormulaComment1}\n{givenFormulaComment2}\n{givenFormulaComment3}\n" \
              "따라서 {givenFormulaComment4}\n{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    a, b, X = symbols("a b X", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    positives = random.choices(range(1, 10), k=3)
    posnegs = random.choices(oneDigitInts, k=4)

    vars = [a, b, a, a, a, b, b]

    #식 구성
    # part1 - [part2 - {part3 - (part4 + part5)}]
    # = part1 - {part2 - (part3 - part45)}
    # = part1 - {part2 - (part345)}
    # = part1 - (part2345)
    # = part12345

    formulaPart1 = posnegs[0] * vars[0]
    formulaPart2 = positives[0] * vars[1] + posnegs[1] * vars[2]
    formulaPart3 = positives[1] * vars[3]
    formulaPart4Real = posnegs[2] * vars[4] + posnegs[3] * vars[5]
    formulaPart4 = X
    formulaPart5 = positives[2] * vars[6]

    calcRes = formulaPart1 - (formulaPart2 - (formulaPart3 - (formulaPart4Real + formulaPart5)))
    calcRes = calcRes.cancel()

    givenFormulaLeft = joinList([formulaPart1, "- [", formulaPart2, "- left {", formulaPart3, "- (", formulaPart4, "+", formulaPart5, ") right } ]"])
    givenFormulaLeft = convertIntoHangul(givenFormulaLeft)
    givenFormulaRight = convertIntoHangul(calcRes)

    givenFormula = joinList([givenFormulaLeft, eq, givenFormulaRight])

    formulaPart45 = -(formulaPart4 + formulaPart5)
    givenFormulaComment1 = joinList([eq, formulaPart1, "- left {", formulaPart2, "- (", formulaPart3, formulaPart45, ") right }"])
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1)

    formulaPart345 = formulaPart3 + formulaPart45
    # givenFormulaComment2 = joinList([eq, formulaPart1, "- left {", formulaPart2, "- (", formulaPart345, ") right }"])
    # givenFormulaComment2 = convertIntoHangul(givenFormulaComment2)

    formulaPart2345 = formulaPart2 - formulaPart345
    givenFormulaComment2 = joinList([eq, formulaPart1, "- (", formulaPart2345, ")"])
    givenFormulaComment2 = convertIntoHangul(givenFormulaComment2)

    formulaPart12345 = formulaPart1 - formulaPart2345
    givenFormulaComment3 = joinList([eq, formulaPart12345])
    givenFormulaComment3 = convertIntoHangul(givenFormulaComment3)

    givenFormulaComment4 = joinList([formulaPart12345, eq, calcRes])
    givenFormulaComment4 = convertIntoHangul(givenFormulaComment4)

    formulaPart12345X = formulaPart12345 + X

    thusAnswer = joinList([thus, X, eq, "(", formulaPart12345X, ") - (", calcRes, ")", eq, formulaPart4Real])
    thusAnswer = convertIntoHangul(thusAnswer)

    ansInd, choiceACoeffs = makeChoices(0, diff=1, withTag=False)
    # print(choiceXCoeffs)
    choiceACoeffs.remove(0)

    _, choiceBCoeffs = makeChoices(0, diff=2, withTag=False)
    choiceBCoeffs.remove(0)

    ansACoeff = posnegs[2]
    ansBCoeff = posnegs[3]

    choices = []
    for i in range(4):
        tempForm = (choiceACoeffs[i]+ansACoeff)*a + (choiceBCoeffs[i]+ansBCoeff)*b
        tempFormText = convertIntoHangul(tempForm)
        choices.append(aT(tempFormText))

    ansForm = aT(convertIntoHangul(formulaPart4Real))
    choices.insert(ansInd, ansForm)


    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), X=aT('X'),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaLeft=aT(givenFormulaLeft), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), givenFormulaComment3=aT(givenFormulaComment3),
                             givenFormulaComment4=aT(givenFormulaComment4), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_101():
    stem = "어떤 식에 {equation1}{postp1} {optionText1} 할 것을 잘못하여 {optionText2} {equation2}{postp2} 되었다. 바르게 계산한 답은?\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n어떤 식에서 {equation1}{postp1}  {optionText2} {equation2}{postp2} 되었으므로 어떤 식을 {A}라 하면\n" \
              "{commentText1}\n{thusAComment1}\n{thusAComment2}\n{thusAComment3}\n따라서 바르게 계산한 답은\n{correctCalcComment1}\n" \
              "{correctCalcComment2}\n{correctCalcComment3}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    option1IsPlus = random.choice([True, False])

    if option1IsPlus :
        optionText1 = "더해야"
        optionText2 = "빼었더니"
        wrongC = -1
        wrongOp = ms
        correctC = 1
        correctOp = ps
    else :
        optionText1 = "빼야"
        optionText2 = "더했더니"
        wrongC = 1
        wrongOp = ps
        correctC = -1
        correctOp = ms

    numbers = random.choices(oneDigitInts, k=6)
    numbers[0] = abs(numbers[0])
    numbers[3] = abs(numbers[3])

    #식 구성
    # (part1) - (part2)
    # = part1 -part2
    # = part12

    formulaPart1 = numbers[0]*x + numbers[1]*y + numbers[2]
    formulaPart2 = numbers[3]*x + numbers[4]*y + numbers[5]

    AEq = convertIntoHangul(formulaPart1)

    equation1 = convertIntoHangul(formulaPart2)
    postp1 = proc_jo(abs(numbers[5]), 1)

    calcResSym = formulaPart1 + wrongC*formulaPart2
    calcResSymCoeffs = calcResSym.as_coefficients_dict()
    calcResConstant = int(calcResSymCoeffs[1])
    calcResYCoeff = int(calcResSymCoeffs[y])
    calcResXCoeff = int(calcResSymCoeffs[x])

    if calcResConstant:
        postp2 = proc_jo(abs(calcResConstant) % 10 , 0)
    else:
        if calcResYCoeff:
            postp2 = "가"
        else:
            if calcResXCoeff:
                postp2 = "가"
            else:
                postp2 = "이"

    equation2 = convertIntoHangul(calcResSym)

    correctOpedEquation1 = convertIntoHangul(correctC*formulaPart2)
    correctOpedEquation2 = convertIntoHangul(correctC*calcResSym)

    commentText1 = joinList(["A", wrongOp, "(", equation1, ")", eq, equation2])

    thusAComment1 = joinList([thus, "A", eq, equation2, correctOp, "(", equation1, ")"])

    thusAComment2Right = connectEqations(equation2, correctOpedEquation1)
    thusAComment2 = joinList([eq, thusAComment2Right])

    thusAComment3 = joinList([eq, AEq])

    correctCalcComment1 = joinList(["A", correctOp, "(", equation1, ")"])

    correctOpedEquation1 = convertIntoHangul(correctC*formulaPart2)

    correctCalcComment2Right = connectEqations(AEq, correctOpedEquation1)
    correctCalcComment2 = joinList([eq, correctCalcComment2Right])

    resSym = formulaPart1 + correctC*formulaPart2
    resSymText = convertIntoHangul(resSym)
    correctCalcComment3 = joinList([eq, resSymText])

    ansInd, choiceXCoeffs = makeChoices(0, diff=1, withTag=False)
    # print(choiceXCoeffs)
    choiceXCoeffs.remove(0)

    _, choiceYCoeffs = makeChoices(0, diff=1, withTag=False)
    choiceYCoeffs.remove(0)

    _, choiceCCoeffs = makeChoices(0, diff=1, withTag=False)

    resSymCoeffs = resSym.as_coefficients_dict()

    ansXCoeff = resSymCoeffs[x]
    ansYCoeff = resSymCoeffs[y]
    ansCCoeff = resSymCoeffs[1]

    choices = []
    for i in range(4):
        tempForm = (choiceXCoeffs[i]+ansXCoeff)*x + (choiceYCoeffs[i]+ansYCoeff)*y + (choiceCCoeffs[i]+ansCCoeff)
        tempFormText = convertIntoHangul(tempForm)
        choices.append(aT(tempFormText))

    choices.insert(ansInd, aT(resSymText))

    # 내용을 채웁니다.
    stem = stem.format(equation1=aT(equation1), postp1=postp1, optionText1=optionText1, optionText2=optionText2,
                       equation2=aT(equation2), postp2=postp2,
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(equation1=aT(equation1), postp1=postp1, optionText2=optionText2, equation2=aT(equation2), postp2=postp2,
                             A=aT("A"), commentText1=aT(commentText1), thusAComment1=aT(thusAComment1), thusAComment2=aT(thusAComment2),
                             thusAComment3=aT(thusAComment3), correctCalcComment1=aT(correctCalcComment1),
                             correctCalcComment2=aT(correctCalcComment2), correctCalcComment3=aT(correctCalcComment3))

    return stem, answer, comment


def rationalandprime211_Stem_102():
    stem = "어떤 식에 {equation1}{postp1} {optionText1} 할 것을 잘못하여 {optionText2} {equation2}{postp2} 되었다. " \
           "바르게 계산한 답을 {correctForm}이라 할 때, {questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n어떤 식에서 {equation1}{postp1}  {optionText2} {equation2}{postp2} 되었으므로 어떤 식을 {A}라 하면\n" \
              "{commentText1}\n{thusAComment1}\n{thusAComment2}\n{thusAComment3}\n따라서 바르게 계산한 답은\n{correctCalcComment1}\n" \
              "{correctCalcComment2}\n{correctCalcComment3}\n따라서 {aFormula}, {bFormula}, {cFormula}이므로\n{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x = symbols("x", real=True)

    correctForm = "ax^2 + bx + c"
    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    option1IsPlus = random.choice([True, False])

    if option1IsPlus :
        optionText1 = "더해야"
        optionText2 = "빼었더니"
        wrongC = -1
        wrongOp = ms
        correctC = 1
        correctOp = ps
    else :
        optionText1 = "빼야"
        optionText2 = "더했더니"
        wrongC = 1
        wrongOp = ps
        correctC = -1
        correctOp = ms

    numbers = random.choices(oneDigitInts, k=6)
    numbers[0] = abs(numbers[0])
    numbers[3] = abs(numbers[3])

    #식 구성
    # (part1) - (part2)
    # = part1 -part2
    # = part12

    formulaPart1 = numbers[0]*x**2 + numbers[1]*x + numbers[2]
    formulaPart2 = numbers[3]*x**2 + numbers[4]*x + numbers[5]

    AEq = convertIntoHangul(formulaPart1)

    equation1 = convertIntoHangul(formulaPart2)
    postp1 = proc_jo(abs(numbers[5]), 1)

    calcResSym = formulaPart1 + wrongC*formulaPart2
    calcResSymCoeffs = calcResSym.as_coefficients_dict()
    calcResConstant = int(calcResSymCoeffs[1])
    calcResXCoeff = int(calcResSymCoeffs[x])

    if calcResConstant :
        postp2 = proc_jo(abs(calcResConstant) % 10, 0)
    else :
        if calcResXCoeff :
            postp2 = "가"
        else :
            postp2 = "이"

    equation2 = convertIntoHangul(calcResSym)

    correctOpedEquation1 = convertIntoHangul(correctC*formulaPart2)

    commentText1 = joinList(["A", wrongOp, "(", equation1, ")", eq, equation2])

    thusAComment1 = joinList([thus, "A", eq, equation2, correctOp, "(", equation1, ")"])

    thusAComment2Right = connectEqations(equation2, correctOpedEquation1)
    thusAComment2 = joinList([eq, thusAComment2Right])

    thusAComment3 = joinList([eq, AEq])

    correctCalcComment1 = joinList(["A", correctOp, "(", equation1, ")"])

    correctOpedEquation1 = convertIntoHangul(correctC*formulaPart2)

    correctCalcComment2Right = connectEqations(AEq, correctOpedEquation1)
    correctCalcComment2 = joinList([eq, correctCalcComment2Right])

    resSym = formulaPart1 + correctC*formulaPart2
    resSymCoeffs= resSym.as_coefficients_dict()

    aVal = resSymCoeffs[x**2]
    bVal = resSymCoeffs[x]
    cVal = resSymCoeffs[1]

    values = [aVal, bVal, cVal]
    chars = ['a', 'b', 'c']

    questionFormulaDict = getRandomEquation(givenChars=chars, coefficientRange=[(1, 4), (-2, 3), (-2, 3)], realValues=values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']
    questionFormulaCoeffs = questionFormulaDict['coeffs']

    ansInd, choices = makeChoices(ansValue, diff=2)

    ansValueEq = getNumberCalc([questionFormulaCoeffs[i]*values[i] for i in range(len(values))], withRes=True)
    thusAnswer = joinList([thus, questionFormula, eq, ansValueEq])

    aFormula, bFormula, cFormula = makeEquality(chars, values, withTag=True)

    resSymText = convertIntoHangul(resSym)
    correctCalcComment3 = joinList([eq, resSymText])

    # 내용을 채웁니다.
    stem = stem.format(equation1=aT(equation1), postp1=postp1, optionText1=optionText1, optionText2=optionText2,
                       equation2=aT(equation2), postp2=postp2, correctForm=aT(correctForm), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(equation1=aT(equation1), postp1=postp1, optionText2=optionText2, equation2=aT(equation2), postp2=postp2,
                             A=aT("A"), commentText1=aT(commentText1), thusAComment1=aT(thusAComment1), thusAComment2=aT(thusAComment2),
                             thusAComment3=aT(thusAComment3), correctCalcComment1=aT(correctCalcComment1),
                             correctCalcComment2=aT(correctCalcComment2), correctCalcComment3=aT(correctCalcComment3),
                             aFormula=aT(aFormula), bFormula=aT(bFormula), cFormula=aT(cFormula), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_103():
    stem = "어떤 식에서 {equation1}{postp1} 빼야 할 것을 잘못하여 {equation1}에서 어떤 식을 뺐더니 {equation2}{postp2} 되었다. 이 때 바르게 계산한 답은?\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n어떤 식을 {A}라 하면\n" \
              "{commentText1}\n{thusAComment1}\n{thusAComment2}\n{thusAComment3}\n따라서 바르게 계산한 답은\n{correctCalcComment1}\n" \
              "{correctCalcComment2}\n{correctCalcComment3}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    option1IsPlus = random.choice([True, False])

    if option1IsPlus :
        optionText1 = "더해야"
        optionText2 = "빼었더니"
        wrongC = -1
        wrongOp = ms
        correctC = 1
        correctOp = ps
    else :
        optionText1 = "빼야"
        optionText2 = "더했더니"
        wrongC = 1
        wrongOp = ps
        correctC = -1
        correctOp = ms

    numbers = random.choices(oneDigitInts, k=6)
    numbers[0] = abs(numbers[0])
    numbers[3] = abs(numbers[3])

    #식 구성
    # (part1) - (part2)
    # = part1 -part2
    # = part12

    formulaPart1 = numbers[0]*x + numbers[1]*y + numbers[2]
    formulaPart2 = numbers[3]*x + numbers[4]*y + numbers[5]

    AEq = convertIntoHangul(formulaPart1)

    equation1 = convertIntoHangul(formulaPart2)
    postp1 = proc_jo(abs(numbers[5]), 1)

    calcResSym = formulaPart2 - formulaPart1
    calcResSymCoeffs = calcResSym.as_coefficients_dict()
    calcResConstant = int(calcResSymCoeffs[1])
    calcResYCoeff = int(calcResSymCoeffs[y])
    calcResXCoeff = int(calcResSymCoeffs[x])

    if calcResConstant :
        postp2 = proc_jo(abs(calcResConstant) % 10, 0)
    else :
        if calcResYCoeff :
            postp2 = "가"
        else :
            if calcResXCoeff :
                postp2 = "가"
            else :
                postp2 = "이"

    equation2 = convertIntoHangul(getPolyText(calcResSym, x, y))

    negEquation1 = convertIntoHangul(-formulaPart2)
    negEquation2 = convertIntoHangul(-calcResSym)

    commentText1 = joinList(["(", equation1, ")", ms, "A", eq, equation2])

    thusAComment1 = joinList([thus, "A", eq, "(", equation1, ")", ms, "(", equation2, ")"])

    thusAComment2Right = connectEqations(equation1, negEquation2)
    thusAComment2 = joinList([eq, thusAComment2Right])

    thusAComment3 = joinList([eq, AEq])

    correctCalcComment1 = joinList(["A", ms, "(", equation1, ")"])

    correctCalcComment2Right = connectEqations(AEq, negEquation1)
    correctCalcComment2 = joinList([eq, correctCalcComment2Right])

    resSym = formulaPart1 - formulaPart2
    resSymText = convertIntoHangul(resSym)
    correctCalcComment3 = joinList([eq, resSymText])

    ansInd, choiceXCoeffs = makeChoices(0, diff=1, withTag=False)
    # print(choiceXCoeffs)
    choiceXCoeffs.remove(0)

    _, choiceYCoeffs = makeChoices(0, diff=1, withTag=False)
    choiceYCoeffs.remove(0)

    _, choiceCCoeffs = makeChoices(0, diff=1, withTag=False)

    resSymCoeffs = resSym.as_coefficients_dict()

    ansXCoeff = resSymCoeffs[x]
    ansYCoeff = resSymCoeffs[y]
    ansCCoeff = resSymCoeffs[1]

    choices = []
    for i in range(4):
        tempForm = (choiceXCoeffs[i]+ansXCoeff)*x + (choiceYCoeffs[i]+ansYCoeff)*y + (choiceCCoeffs[i]+ansCCoeff)
        tempFormText = convertIntoHangul(tempForm)
        choices.append(aT(tempFormText))

    choices.insert(ansInd, aT(resSymText))

    # 내용을 채웁니다.
    stem = stem.format(equation1=aT(equation1), postp1=postp1, equation2=aT(equation2), postp2=postp2,
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(A=aT("A"), commentText1=aT(commentText1), thusAComment1=aT(thusAComment1), thusAComment2=aT(thusAComment2),
                             thusAComment3=aT(thusAComment3), correctCalcComment1=aT(correctCalcComment1),
                             correctCalcComment2=aT(correctCalcComment2), correctCalcComment3=aT(correctCalcComment3))

    return stem, answer, comment


def rationalandprime211_Stem_104():
    stem = "다음은 {givenFormula}{postp} 간단히 정리한 결과에 대한 수호, 경현, 미정의 토론 내용이다.\n\n" \
           "   수호: 계산한 결과는 {showingResCategory}입니다.\n   경현: {x2}의 계수와 {x}의 계수는 서로 {showingCompare}.\n" \
           "   미경: {x2}의 계수, {x}의 계수, 상수항의 합은 {showingSumValue}입니다.\n\n" \
           "세 사람 중 옳은 말을 한 사람을 모두 고른 것은?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n주어진 식을 간단히 정리하면\n{givenFormula} {givenFormulaComment1}\n{givenFormulaComment2}\n" \
              "따라서 계산한 결과는 {resCategory}이다.\n이 때 {x2}의 계수는 {x2CoeffText}, {x}의 계수는 {xCoeffText}, " \
              "상수항은 {constantText}이므로 {x2}의 계수, {x}의 계수, 상수항의 합은 {sumFormula}이다.\n" \
              "따라서 옳은 말을 한 사람은 {answerPeople}이다.\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x = symbols("x", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    numbers = random.choices(oneDigitInts, k=6)
    numbers[0] = abs(numbers[0])
    numbers[3] = abs(numbers[3])

    denomSeed = random.choice(range(1, 10))
    multiplier = random.choice(range(2, 5))
    firstDenom, secondDenom = [denomSeed*multiplier, denomSeed]
    biggerDenom = denomSeed * multiplier
    secondFracMinusOrPlus = random.choice([1, -1])

    firstFracNumeratorSym = numbers[0]*x**2 + numbers[1]*x + numbers[2]
    secondFracNumeratorSym = numbers[3]*x**2 + numbers[4]*x + numbers[5]

    firstFracNumeratorText = convertIntoHangul(firstFracNumeratorSym)
    secondFracNumeratorText = convertIntoHangul(secondFracNumeratorSym)

    firstFracText= makeFractionFormula(firstFracNumeratorText, firstDenom)
    secondFracText = makeFractionFormula(secondFracNumeratorText, secondDenom)

    postp = proc_jo(abs(numbers[5]), 1)

    if secondFracMinusOrPlus == 1 :
        middleOpr = ps
    else :
        middleOpr = ms

    givenFormula = joinList([firstFracText, middleOpr, secondFracText])

    secondFracNumeratorMultipliedSym = secondFracNumeratorSym * multiplier
    secondFracNumeratorMultipliedSymText = convertIntoHangul(secondFracNumeratorMultipliedSym)

    secondFracMultipliedText = makeFractionFormula(secondFracNumeratorMultipliedSymText, biggerDenom)

    givenFormulaComment1 = joinList([eq, firstFracText, middleOpr, secondFracMultipliedText])

    fracSumNumeratorSym = firstFracNumeratorSym + secondFracMinusOrPlus * secondFracNumeratorSym * multiplier
    fracSumNumeratorText = convertIntoHangul(fracSumNumeratorSym)

    fracSumText = makeFractionFormula(fracSumNumeratorText, biggerDenom)

    fracSumSym = fracSumNumeratorSym / biggerDenom
    fracSumSymText = getPolyText(fracSumSym)
    finalFormText = convertIntoHangul(fracSumSymText, minusWithSpace=True, timesToSpace=True)

    givenFormulaComment2Left = fracSumText
    givenFormulaComment2Right = finalFormText
    givenFormulaComment2 = joinList([eq, givenFormulaComment2Left, eq, givenFormulaComment2Right])

    fracSumCoeffs = fracSumSym.as_coefficients_dict()

    x2Coeff, xCoeff, constant = fracSumCoeffs[x**2], fracSumCoeffs[x], fracSumCoeffs[1]
    coeffSum = x2Coeff + xCoeff + constant

    if x2Coeff :
        resCategory = "이차식"
    elif xCoeff :
        resCategory = "일차식"
    else :
        resCategory = "상수"

    remainingCategories = ["이차식", "일차식", "상수"]
    remainingCategories.remove(resCategory)

    x2CoeffText = convertIntoHangul(x2Coeff, minusWithSpace=True)
    xCoeffText = convertIntoHangul(xCoeff, minusWithSpace=True)
    constantText = convertIntoHangul(constant, minusWithSpace=True)

    coeffSumTextLeft = connectEqations(connectEqations(x2CoeffText, xCoeffText), constantText)
    coeffSumTextRight = convertIntoHangul(coeffSum, minusWithSpace=True)
    sumFormula = joinList([coeffSumTextLeft, eq, coeffSumTextRight])

    oneItems = ['ㄱ', 'ㄴ', 'ㄷ']
    twoItems = ['ㄱ, ㄴ', 'ㄱ, ㄷ', 'ㄴ, ㄷ']
    threeItems = ['ㄱ, ㄴ, ㄷ']

    items = oneItems + twoItems + threeItems

    _choiceItemInds = random.sample(range(7), k=5)
    _ansItemInd = _choiceItemInds[0]
    ansChars = items[_ansItemInd]

    ansItemIndsOrdered = sorted(_choiceItemInds)
    ansInd = ansItemIndsOrdered.index(_ansItemInd)

    if "ㄱ" in ansChars :
        showingResCategory = resCategory
    else :
        showingResCategory = random.choice(remainingCategories)

    if "ㄴ" in ansChars :
        if x2Coeff == xCoeff :
            showingCompare = "같습니다"
        else :
            showingCompare = "다릅니다"
    else :
        if x2Coeff == xCoeff :
            showingCompare = "다릅니다"
        else :
            showingCompare = "같습니다"

    if "ㄷ" in ansChars :
        showingSumValue = coeffSumTextRight
    else :
        showingSumValue = convertIntoHangul(coeffSum+1, minusWithSpace=True)

    itemsReplaced = []
    for item in items:
        temp = item.replace("ㄱ", "수호")
        temp = temp.replace("ㄴ", "경현")
        temp = temp.replace("ㄷ", "미경")
        itemsReplaced.append(temp)

    choices = [itemsReplaced[i] for i in ansItemIndsOrdered]

    x2 = "x^2"

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), postp=postp, showingResCategory=showingResCategory, x2=aT(x2), x=aT(x),
                       showingCompare=showingCompare, showingSumValue=aT(showingSumValue),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), resCategory=resCategory,
                             x2=aT(x2), x2CoeffText=aT(x2CoeffText), x=aT(x), xCoeffText=aT(xCoeffText),
                             constantText=aT(constantText), sumFormula=aT(sumFormula), answerPeople=choices[ansInd])

    return stem, answer, comment


def rationalandprime211_Stem_105():
    stem = "{xSqBrk}는 {x}보다 크지 않은 최대의 정수라 할 때,\n{givenFormula}를 계산한 결과는?\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{lVal1Formula}, {lVal2Formula}, {lVal3Formula}이므로\n{givenFormula}\n{givenFormulaComment1}\n{givenFormulaComment2}\n{givenFormulaComment3}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-6, 0)) + list(range(1, 7))
    twoDigitInts = list(range(-59, -20)) + list(range(21, 60))

    positives = random.choices(range(1, 7), k=3)
    posnegs = random.choices(oneDigitInts, k=3)

    while True :
        lValInits = random.sample(twoDigitInts, k=3)
        isDividedBy10 = 0
        for num in lValInits :
            if not num % 10 :
                isDividedBy10 += 1
        if not isDividedBy10 :
            break

    # lValInits[-1] = abs(lValInits[-1])

    lValDecimals = [x/10 for x in lValInits]
    lValTexts = [joinList(["[", x, "]"]) for x in lValDecimals]
    lValResults = [int(x-1) if x < 0 else int(x) for x in lValDecimals]

    lValFormulas = makeEquality(lValTexts, lValResults, True)

    #식 구성
    # lVal1(part1) + lVal2(part2) - lVal3(part3)

    formulaPart1 = positives[0]*x + posnegs[0]*y
    formulaPart2 = positives[1]*x + posnegs[1]*y
    formulaPart3 = positives[2]*x + posnegs[2]*y
    formulaParts = [formulaPart1, formulaPart2, formulaPart3]
    formulaPartsText = list(map(convertIntoHangul, formulaParts))

    givenFormulaList = [joinList([lValTexts[i], "(", formulaPartsText[i], ")"]) for i in range(3)]
    givenFormula = joinList([givenFormulaList[0], ps, givenFormulaList[1], ms, givenFormulaList[2]])

    lValResText = [joinList(["(", x, ")"]) if x < 0 else x for x in lValResults]

    givenFormulaComment1List = [joinList([lValResText[i], "(", formulaPartsText[i], ")"]) for i in range(3)]
    givenFormulaComment1 = joinList([eq, givenFormulaComment1List[0], ps, givenFormulaComment1List[1], ms, givenFormulaComment1List[2]])

    formulaPartsMultiplied = [lValResults[i] * formulaParts[i] for i in range(3)]
    formulaPartsMultiplied[-1] *= -1
    formulaPartsMultipliedText = list(map(convertIntoHangul, formulaPartsMultiplied))

    givenFormulaComment2Right = connectEqations(connectEqations(formulaPartsMultipliedText[0], formulaPartsMultipliedText[1]), formulaPartsMultipliedText[2])
    givenFormulaComment2 = joinList([eq, givenFormulaComment2Right])

    formulaSumSym = sum(formulaPartsMultiplied)
    formulaSumText = convertIntoHangul(formulaSumSym)
    givenFormulaComment3 = joinList([eq, formulaSumText])

    ansInd, choiceXCoeffs = makeChoices(0, diff=1, withTag=False)
    # print(choiceXCoeffs)
    choiceXCoeffs.remove(0)

    _, choiceYCoeffs = makeChoices(0, diff=2, withTag=False)
    choiceYCoeffs.remove(0)

    finalFormCoeffs= formulaSumSym.as_coefficients_dict()
    ansXCoeff = finalFormCoeffs[x]
    ansYCoeff = finalFormCoeffs[y]

    choices = []
    for i in range(4):
        tempForm = (choiceXCoeffs[i]+ansXCoeff)*x + (choiceYCoeffs[i]+ansYCoeff)*y
        tempFormText = convertIntoHangul(tempForm)
        choices.append(aT(tempFormText))

    choices.insert(ansInd, aT(formulaSumText))


    # 내용을 채웁니다.
    stem = stem.format(xSqBrk=aT("[x]"), x=aT(x), givenFormula=aT(givenFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(lVal1Formula=lValFormulas[0], lVal2Formula=lValFormulas[1], lVal3Formula=lValFormulas[2],
                             givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), givenFormulaComment3=aT(givenFormulaComment3))

    return stem, answer, comment


def rationalandprime211_Stem_106():
    stem = "{givenFormula}를 계산한 결과는?\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    a = symbols("a", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    posnegs = sorted(random.sample(oneDigitInts, k=3), reverse=True)
    exps = sorted(random.sample(range(1, 7), k=3), reverse=True)


    #식 구성
    # part1 / part2
    # = part12

    formulaPart1 = posnegs[0] * a ** exps[0] - posnegs[1] * a ** exps[1]
    formulaPart2 = (1/Integer(posnegs[2])) * a ** exps[2]

    formulaPart2Text = getPolyText(formulaPart2, a)

    givenFormula = joinList(["(", formulaPart1, ")", dd, formulaPart2Text])
    givenFormula = convertIntoHangul(givenFormula, minusWithSpace=True, timesToSpace=True)

    formulaPart12 = (formulaPart1 / formulaPart2).cancel()
    formulaPart2Inversed = 1 /formulaPart2
    if posnegs[2] == 1 :
        formulaPart2InversedText = convertNegExp(formulaPart2Inversed)
    else :
        formulaPart2InversedText = str(formulaPart2Inversed)
    givenFormulaComment1 = joinList([eq, "(", formulaPart1, ")", ts, formulaPart2InversedText, eq, formulaPart12])
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1, minusWithSpace=True, timesToSpace=True)

    ansInd, choiceACoeffs = makeChoices(0, diff=2, withTag=False)
    # print(choiceXCoeffs)
    choiceACoeffs.remove(0)

    _, choiceBCoeffs = makeChoices(0, diff=1, withTag=False)
    choiceBCoeffs.remove(0)

    ansACoeff = posnegs[0] * posnegs[2]
    ansAExps = exps[0] - exps[2]
    ansBCoeff = -posnegs[1] * posnegs[2]
    ansBExps = exps[1] - exps[2]

    choices = []
    for i in range(4):
        tempForm = (choiceACoeffs[i]+ansACoeff)*a**ansAExps + (choiceBCoeffs[i]+ansBCoeff)*a**ansBExps
        tempFormText = convertIntoHangul(tempForm)
        choices.append(aT(tempFormText))

    ansForm = aT(convertIntoHangul(formulaPart12))
    choices.insert(ansInd, ansForm)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1))

    return stem, answer, comment


def rationalandprime211_Stem_107():
    stem = "{givenFormula}를 계산한 결과는?\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}\n{givenFormulaComment2}\n{givenFormulaComment3}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    # oneDigitInts = list(range(-9, 0)) + list(range(1, 10))
    # oneDigitLimited = list(range(-6, -1)) + list(range(2, 7))

    frontCoeffSeeds = sorted(random.sample(range(2, 7), k=3), reverse=True)
    frontCoeffSeeds[1] = random.choice([1, -1]) * frontCoeffSeeds[1]

    frontCoeffs = [frontCoeffSeeds[0] * frontCoeffSeeds[2], frontCoeffSeeds[1] * frontCoeffSeeds[2], frontCoeffSeeds[2], frontCoeffSeeds[2]-1]

    frontXExps = [3, 1, 1]
    frontYExps = [1, 2, 1]

    secondCoeffs = random.choices(range(1, 10), k=3)
    secondCoeffs[2] = random.choice([1, -1]) * secondCoeffs[2]

    #식 구성
    # (part1) / part2 + part3(part4)
    # = part1 * 1/part2 + part3(part4)
    # = part12 + part34
    # = part1234

    # print(frontCoeffs)
    formulaPart1 = frontCoeffs[0]*x**frontXExps[0]*y**frontYExps[0] + frontCoeffs[1]*x**frontXExps[1]*y**frontYExps[1]
    formulaPart2 = frontCoeffs[2]*x**frontXExps[2]*y**frontYExps[2] / frontCoeffs[3]
    formulaPart2Text = getPolyText(formulaPart2, x, y)
    formulaPart3 = secondCoeffs[0]*x
    formulaPart4 = secondCoeffs[1]*x + secondCoeffs[2]*y

    givenFormula = joinList(["(", formulaPart1, ")", dd, formulaPart2Text, ps, formulaPart3, "(", formulaPart4, ")"])
    givenFormula = convertIntoHangul(givenFormula, minusWithSpace=True, timesToSpace=True)

    formulaPart2Inversed = 1 / formulaPart2
    formulaPart2InversedText = convertIntoHangul(formulaPart2Inversed, parenToBracket=True, timesToSpace=True)
    givenFormulaComment1 = joinList([eq, "(", formulaPart1, ")", ts, formulaPart2InversedText, ps, formulaPart3, "(", formulaPart4, ")"])
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1, minusWithSpace=True, timesToSpace=True)

    formulaPart12 = (formulaPart1 / formulaPart2).cancel()
    formulaPart34 = (formulaPart3 * formulaPart4).cancel()
    givenFormulaComment2 = joinList([eq, formulaPart12, ps, formulaPart34])
    givenFormulaComment2 = convertIntoHangul(givenFormulaComment2, minusWithSpace=True, timesToSpace=True)

    formulaPart1234 = (formulaPart12 + formulaPart34).cancel()
    givenFormulaComment3 = joinList([eq, formulaPart1234])
    givenFormulaComment3 = convertIntoHangul(givenFormulaComment3, minusWithSpace=True, timesToSpace=True)

    formulaPart1Wrong1 = frontCoeffs[0] * x ** frontXExps[0] * y ** (frontYExps[0]+1) + frontCoeffs[1] * x ** frontXExps[1] * y ** frontYExps[1]
    formulaPart1Wrong2 = frontCoeffs[0] * x ** frontXExps[0] * y ** frontYExps[0] + frontCoeffs[1] * x ** (frontXExps[1]+1) * y ** frontYExps[1]
    formulaPart2 = frontCoeffs[2] * x ** frontXExps[2] * y ** frontYExps[2] / frontCoeffs[3]
    formulaPart4Wrong3 = secondCoeffs[1] * x**2 + secondCoeffs[2] * y
    formulaPart4Wrong4 = secondCoeffs[1] * x + secondCoeffs[2] * y**2

    wrongSym1 = formulaPart1Wrong1 / formulaPart2 + formulaPart34
    wrongSym2 = formulaPart1Wrong2 / formulaPart2 + formulaPart34
    wrongSym3 = formulaPart12 + formulaPart3 * formulaPart4Wrong3
    wrongSym4 = formulaPart12 + formulaPart3 * formulaPart4Wrong4

    choiceSyms = [wrongSym1, wrongSym2, wrongSym3, wrongSym4]
    random.shuffle(choiceSyms)

    ansInd = random.choice(range(5))
    choiceSyms.insert(ansInd, formulaPart1234)

    choices = list(map(lambda x: aT(convertIntoHangul(x.cancel(), minusWithSpace=True, timesToSpace=True)), choiceSyms))


    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2),
                             givenFormulaComment3=aT(givenFormulaComment3))

    return stem, answer, comment


def rationalandprime211_Stem_108():
    stem = "다음 식을 계산한 결과는?\n\n" \
           "  {givenFormula}\n\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}\n{givenFormulaComment2}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    # oneDigitInts = list(range(-9, 0)) + list(range(1, 10))
    # oneDigitLimited = list(range(-6, -1)) + list(range(2, 7))
    oneOrMinus = [1, -1]

    coeffs = random.choices(range(1, 10), k=6)
    coeffs[2] *= random.choice(oneOrMinus)
    coeffs[5] *= random.choice(oneOrMinus)

    #식 구성
    # part1(part2) - part3(part4)
    # = part12 - part34
    # = part1234

    # print(frontCoeffs)
    formulaPart1 = coeffs[0]*x
    formulaPart2 = coeffs[1]*x + coeffs[2]*y
    formulaPart3 = coeffs[3]*x
    formulaPart4 = coeffs[4]*x + coeffs[5]*y

    givenFormula = joinList([formulaPart1, "(", formulaPart2, ")", ms, formulaPart3, "(", formulaPart4, ")"])
    givenFormula = convertIntoHangul(givenFormula, minusWithSpace=True, timesToSpace=True)

    formulaPart12 = (formulaPart1 * formulaPart2).cancel()
    formulaPart34 = (-formulaPart3 * formulaPart4).cancel()
    givenFormulaComment1 = joinList([eq, formulaPart12, formulaPart34])
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1, minusWithSpace=True, timesToSpace=True)

    formulaPart1234 = (formulaPart12 + formulaPart34).cancel()
    givenFormulaComment2 = joinList([eq, formulaPart1234])
    givenFormulaComment2 = convertIntoHangul(givenFormulaComment2, minusWithSpace=True, timesToSpace=True)

    formulaPart1Wrong1 = formulaPart1 + x
    formulaPart1Wrong2 = formulaPart1 * x
    formulaPart4Wrong3 = formulaPart4 + x
    formulaPart4Wrong4 = formulaPart4 + y

    wrongSym1 = formulaPart1Wrong1 * formulaPart2 + formulaPart34
    wrongSym2 = formulaPart1Wrong2 * formulaPart2 + formulaPart34
    wrongSym3 = formulaPart12 - formulaPart3 * formulaPart4Wrong3
    wrongSym4 = formulaPart12 - formulaPart3 * formulaPart4Wrong4

    choiceSyms = [wrongSym1, wrongSym2, wrongSym3, wrongSym4]
    random.shuffle(choiceSyms)

    ansInd = random.choice(range(5))
    choiceSyms.insert(ansInd, formulaPart1234)

    choices = list(map(lambda x: aT(convertIntoHangul(x.cancel(), minusWithSpace=True, timesToSpace=True)), choiceSyms))

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2))

    return stem, answer, comment


def rationalandprime211_Stem_109():
    stem = "{givenFormula1}{postp1} 전개한 식의 {gF1Char}의 계수를 {a}, {givenFormula2}{postp2} 전개한 식의 {gF2Char}의 계수를 {b}라 할 때, {questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula1Comment}이므로\n{aFormula}\n{givenFormula2Comment}이므로\n{bFormula}\n" \
              "{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    numbers = random.choices(oneDigitInts, k=8)

    #식 구성
    # part1(part2) , part3(part4)
    # part12, part34

    formulaPart1 = numbers[0]*x
    formulaPart2 = numbers[1]*x + numbers[2]*y + numbers[3]
    postp1 = proc_jo(abs(numbers[3]), 1)

    givenFormula1 = joinList([formulaPart1, "(", formulaPart2, ")"])
    givenFormula1 = convertIntoHangul(givenFormula1)

    formulaPart3 = numbers[4] * x
    formulaPart4 = numbers[5] * x + numbers[6] * y + numbers[7]
    postp2 = proc_jo(abs(numbers[7]), 1)

    givenFormula2 = joinList([formulaPart3, "(", formulaPart4, ")"])
    givenFormula2 = convertIntoHangul(givenFormula2)

    formulaPart12 = (formulaPart1 * formulaPart2).cancel()
    formulaPart12Text = convertIntoHangul(formulaPart12)
    givenFormula1Comment = joinList([givenFormula1, eq, formulaPart12Text])

    formulaPart34 = (formulaPart3 * formulaPart4).cancel()
    formulaPart34Text = convertIntoHangul(formulaPart34)
    givenFormula2Comment = joinList([givenFormula2, eq, formulaPart34Text])

    xChars = [x**2, x*y]
    random.shuffle(xChars)

    gF1Coeff = int(formulaPart12.coeff(xChars[0]))
    gF2Coeff = int(formulaPart34.coeff(xChars[1]))

    values = [gF1Coeff, gF2Coeff]

    ansChars = ['a', 'b']

    ValueFormulas = makeEquality(ansChars, values, withTag=True)

    questionFormulaDict = getRandomEquation(ansChars, [(1, 4), (-2, 3)], values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    questionFormulaCoeff = questionFormulaDict['coeffs']
    ansValue = questionFormulaDict['ansValue']

    ansValueEq = getNumberCalc([questionFormulaCoeff[i]*values[i] for i in range(2)], withRes=True)
    thusAnswer = joinList([thus, questionFormula, eq, ansValueEq])

    ansInd, choices = makeChoices(ansValue, diff=2, withTag=True)

    xChars = list(map(convertIntoHangul, xChars))

    # 내용을 채웁니다.
    stem = stem.format(givenFormula1=aT(givenFormula1), postp1=postp1, gF1Char=aT(xChars[0]), a=aT('a'),
                       givenFormula2=aT(givenFormula2), postp2=postp2, gF2Char=aT(xChars[1]), b=aT('b'), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula1Comment=aT(givenFormula1Comment),
                             givenFormula2Comment=aT(givenFormula2Comment),
                             aFormula=ValueFormulas[0], bFormula=ValueFormulas[1], thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_110():
    stem = "다음 중 계산 결과가 옳지 않은 것은?\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{a1} {givenFormulaComment}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    intRange = list(range(-6, 7))
    intRange.remove(0)

    def makeRandomItem(positive=False):
        coeff = random.choice(intRange)

        if positive :
            coeff = abs(coeff)

        while True :
            n, m = random.choices(range(4), k=2)
            expSum = n+m
            if (expSum > 0) and (expSum < 5) :
                break

        return (coeff * x**n * y**m, [n, m])

    choiceSymLists = []
    for i in range(5):
        if i < 3 :
            length=2
        else :
            length=3

        seedItemTuple = makeRandomItem(positive=True)
        exps = [seedItemTuple[1]]
        items = [seedItemTuple[0]]
        for j in range(length):
            while True :
                itemTuple = makeRandomItem()
                if itemTuple[1] not in exps :
                    exps.append(itemTuple[1])
                    items.append(itemTuple[0])
                    break

        choiceSymLists.append(items)

    choiceSymLists2 = []
    for symList in choiceSymLists :
        rightSym = sum(symList[1:])
        leftSym = rightSym * symList[0]

        rightSym = rightSym.cancel()
        leftSym = leftSym.cancel()

        choiceSymLists2.append([leftSym, symList[0], rightSym])

    ansInd = random.choice(range(5))

    ansIndSymList = choiceSymLists[ansInd][:]
    ansIndSymList[random.choice([1, 2])] *= -1

    ansIndSymList2 = choiceSymLists2[ansInd][:]
    ansIndSymList2[2] = sum(ansIndSymList[1:])

    choices = []
    for i in range(5) :
        if i != ansInd:
            tempList = choiceSymLists2[i]
        else :
            tempList = ansIndSymList2
        text = joinList(["(", tempList[0], ")", dd, tempList[1], eq, tempList[2]])
        text = aT(convertIntoHangul(text, minusWithSpace=True, timesToSpace=True))
        choices.append(text)

    indCorrect = choiceSymLists2[ansInd]
    commentText = joinList(["(", indCorrect[0], ")", dd, indCorrect[1], eq, indCorrect[2]])
    commentText = aT(convertIntoHangul(commentText, minusWithSpace=True, timesToSpace=True))

    # 내용을 채웁니다.
    stem = stem.format(s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(a1=answer_dict[ansInd], givenFormulaComment=commentText)

    return stem, answer, comment


def rationalandprime211_Stem_111():
    stem = "{givenFormula}를 계산한 식에서 {x2}의 계수와 {xy}의 계수의 {optionText} 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}\n{givenFormulaComment2}\n" \
              "따라서 {x2}의 계수는 {x2Coeff}, {xy}의 계수는 {xyCoeff}이므로 구하는 {optionText2} {ansValue}이다.\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-8, 0)) + list(range(1, 9))

    coeffSeeds = random.choices(oneDigitInts, k=4)
    coeffs = coeffSeeds[:]
    coeffs[-1] = Integer(coeffs[-1])
    coeffs[-2] /= coeffs[-1]

    #식 구성
    # (part1) / part2
    # = part12

    # print(frontCoeffs)
    formulaPart1 = coeffs[0]*x**3 + coeffs[1]*x**2*y + coeffs[2]*x
    formulaPart2 = 1/coeffs[3]*x
    formulaPart1Text = joinList(["left (", getPolyText(formulaPart1, x, y), "right )"])
    formulaPart2Text = str(formulaPart2)

    if coeffs[3] < 0 :
        formulaPart2Text = joinList(['left (', formulaPart2Text, "right )"])
    givenFormula = joinList([formulaPart1Text, dd, formulaPart2Text])
    givenFormula = convertIntoHangul(givenFormula, minusWithSpace=True, timesToSpace=True)

    formulaPart12 = (formulaPart1 / formulaPart2).cancel()
    formulaPart2Inversed = 1/formulaPart2
    givenFormulaComment1 = joinList([eq, formulaPart1Text, ts, formulaPart2Inversed])
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1, minusWithSpace=True, timesToSpace=True)

    givenFormulaComment2 = joinList([eq, formulaPart12])
    givenFormulaComment2 = convertIntoHangul(givenFormulaComment2, minusWithSpace=True, timesToSpace=True)

    xChars = [x ** 2, x * y]
    x2, xy = list(map(aT, ["x^2", 'xy']))

    x2Coeff = int(formulaPart12.coeff(xChars[0]))
    xyCoeff = int(formulaPart12.coeff(xChars[1]))

    isSum = random.choice([True, False])

    if isSum:
        optionText = "합을"
        optionText2 = "합은"
        ansValue = x2Coeff + xyCoeff
    else :
        optionText = "차를"
        optionText2 = "차는"
        ansValue = abs(x2Coeff - xyCoeff)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), x2=x2, xy=xy, optionText=optionText)
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), x2=x2, xy=xy, x2Coeff=aT(x2Coeff),
                             xyCoeff=aT(xyCoeff), optionText2=optionText2, ansValue=aT(ansValue))

    return stem, answer, comment


def rationalandprime211_Stem_112():
    stem = "어떤 다항식을 {equation1}{postp1} 나누었더니 나누어떨어졌다. 몫이 {equation2}일 때, 이 다항식의 {coeffChar}의 계수는?\n" \
           "① {s1}   ② {s2}   ③ {s3}   ④ {s4}   ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n어떤 다항식을 {A}라 하면\n" \
              "{commentText1}\n{thusAComment1}\n{thusAComment2}\n따라서 {coeffChar}의 계수는 {ansValue}이다.\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x = symbols("x", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    numbers = random.choices(oneDigitInts, k=4)
    numbers[0] = abs(numbers[0])
    numbers[1] = abs(numbers[1])

    #식 구성
    # A / (part1) = (part2)
    # (part1) * (part2) = A
    # = part12

    formulaPart1 = numbers[0]*x**random.choice([1, 2])
    formulaPart2 = numbers[1]*x**2 + numbers[2]*x + numbers[3]

    formulaPart1Text = convertIntoHangul(formulaPart1)
    formulaPart2Text = convertIntoHangul(formulaPart2)

    ASym = (formulaPart1*formulaPart2).cancel()
    AEq = convertIntoHangul(ASym)

    if formulaPart1Text[-1] == "2" :
        postp1 = "으로"
    else :
        postp1 = "로"

    commentText1 = joinList(["A", dd, formulaPart1Text, eq, formulaPart2Text])

    thusAComment1 = joinList([thus, "A", eq, "(", formulaPart2Text, ")", ts, formulaPart1Text])
    thusAComment2 = joinList([eq, AEq])

    coeffDict = list(ASym.as_coefficients_dict().items())
    selectedCharTuple = random.choice(coeffDict)
    coeffChar = aT(convertIntoHangul(selectedCharTuple[0]))

    ansValue = int(selectedCharTuple[1])

    ansInd, choices = makeChoices(ansValue, diff=2)

    # 내용을 채웁니다.
    stem = stem.format(equation1=aT(formulaPart1Text), postp1=postp1, equation2=aT(formulaPart2Text), coeffChar=coeffChar,
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(A=aT("A"), commentText1=aT(commentText1), thusAComment1=aT(thusAComment1), thusAComment2=aT(thusAComment2),
                             coeffChar=coeffChar, ansValue=aT(ansValue))

    return stem, answer, comment


def rationalandprime211_Stem_113():
    stem = " 다항식 {A}를 {equation1}로 나눈 결과가 {equation2}일 때, 이 다항식 {A}는?\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{commentText1}이므로\n{thusAComment1}\n{thusAComment2}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    a, b = symbols("a b", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    numbers = random.choices(oneDigitInts, k=2)
    fracs = [makeRandomFraction(repeat='rand', numeratorMaxDigit = (1, [1]), denominatorMaxDigit = (1, [1])) for i in range(2)]

    fracCoeffs = [Integer(x[0])/x[1] for x in fracs]
    fracCoeffs[1] *= random.choice([1, -1])

    #식 구성
    # A / (part1) = (part2)
    # (part1) * (part2) = A
    # = part12

    formulaPart1 = numbers[0]*random.choice([a, b])
    formulaPart2 = fracCoeffs[0]*a + fracCoeffs[1]*a*b + numbers[1]*b

    formulaPart1Text = convertIntoHangul(getPolyText(formulaPart1), minusWithSpace=True, timesToSpace=True)
    if numbers[0] < 0 :
        formulaPart1Text2 = joinList([lp, formulaPart1Text, rp])
    else :
        formulaPart1Text2 = formulaPart1Text

    formulaPart2Text = convertIntoHangul(getPolyText(formulaPart2), minusWithSpace=True, timesToSpace=True)

    ASym = (formulaPart1*formulaPart2).cancel()
    AEq = convertIntoHangul(getPolyText(ASym), minusWithSpace=True, timesToSpace=True)

    commentText1 = joinList(["A", dd, formulaPart1Text2, eq, formulaPart2Text])

    thusAComment1 = joinList([thus, "A", eq, "left (", formulaPart2Text, "right )", ts, formulaPart1Text2])
    thusAComment2 = joinList([eq, AEq])

    int2 = Integer(2)

    formulaPart1Wrong1 = formulaPart1 / int2
    formulaPart2Wrong2 = (fracCoeffs[0]/int2)*a + fracCoeffs[1]*a*b + numbers[1]*b
    formulaPart2Wrong3 = fracCoeffs[0]*a + (fracCoeffs[1]/int2)*a*b + numbers[1]*b
    formulaPart2Wrong4 = fracCoeffs[0]*a + fracCoeffs[1]*a*b + (numbers[1]/int2)*b

    wrongSym1 = formulaPart1Wrong1 * formulaPart2
    wrongSym2 = formulaPart1 * formulaPart2Wrong2
    wrongSym3 = formulaPart1 * formulaPart2Wrong3
    wrongSym4 = formulaPart1 * formulaPart2Wrong4

    choiceSyms = [wrongSym1, wrongSym2, wrongSym3, wrongSym4]
    random.shuffle(choiceSyms)

    ansInd = random.choice(range(5))
    choiceSyms.insert(ansInd, ASym)

    choices = list(map(lambda x: aT(convertIntoHangul(getPolyText(x.cancel(), a, b), minusWithSpace=True, timesToSpace=True)), choiceSyms))

    # 내용을 채웁니다.
    stem = stem.format(A=aT("A"), equation1=aT(formulaPart1Text), equation2=aT(formulaPart2Text),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(commentText1=aT(commentText1), thusAComment1=aT(thusAComment1), thusAComment2=aT(thusAComment2))

    return stem, answer, comment


def rationalandprime211_Stem_114():
    stem = "{givenFormula}를 계산했을 때, {x2}의 계수를 {a}, {xy}의 계수를 {b}라 할 때, {questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}\n{givenFormulaComment2}\n{givenFormulaComment3}\n" \
              "따라서 {aFormula}, {bFormula}이므로\n{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-6, 0)) + list(range(1, 7))

    coeffs = random.choices(oneDigitInts, k=6)
    coeffs[-1] = abs(coeffs[-1])

    #식 구성
    # part1(part2) - (part3)*part4
    # = part12 - part34
    # = part1234

    # print(frontCoeffs)
    formulaPart1 = coeffs[0]*x
    formulaPart2 = coeffs[1]*x + coeffs[2]*y
    formulaPart3= coeffs[3]*x + coeffs[4]*y
    formulaPart4 = coeffs[5] * x

    givenFormula = joinList([formulaPart1, "(", formulaPart2, ")", ms, "(", formulaPart3, ")", ts, formulaPart4])
    givenFormula = convertIntoHangul(givenFormula, minusWithSpace=True, timesToSpace=True)

    formulaPart12 = (formulaPart1 * formulaPart2).cancel()
    formulaPart34 = (formulaPart3 * formulaPart4).cancel()
    givenFormulaComment1 = joinList([eq, formulaPart12, ms, "(", formulaPart34, ")"])
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1, minusWithSpace=True, timesToSpace=True)

    givenFormulaComment2 = connectEqations(formulaPart12, -formulaPart34)
    givenFormulaComment2 = convertIntoHangul(givenFormulaComment2, minusWithSpace=True, timesToSpace=True)

    formulaPart1234 = (formulaPart12 - formulaPart34).cancel()
    givenFormulaComment3 = joinList([eq, formulaPart1234])
    givenFormulaComment3 = convertIntoHangul(givenFormulaComment3, minusWithSpace=True, timesToSpace=True)

    xChars = [x ** 2, x * y]

    x2Coeff = int(formulaPart1234.coeff(xChars[0]))
    xyCoeff = int(formulaPart1234.coeff(xChars[1]))

    values = [x2Coeff, xyCoeff]

    ansChars = ['a', 'b']

    aFormula, bFormula = makeEquality(ansChars, values, withTag=True)

    questionFormulaDict = getRandomEquation(ansChars, [(1, 3), (-2, 0)], values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    questionFormulaCoeff = questionFormulaDict['coeffs']
    ansValue = questionFormulaDict['ansValue']

    ansValueEq = getNumberCalc([questionFormulaCoeff[i] * values[i] for i in range(2)], withRes=True)
    thusAnswer = joinList([thus, questionFormula, eq, ansValueEq])

    ansInd, choices = makeChoices(ansValue, diff=2, withTag=True)

    xChars = list(map(convertIntoHangul, xChars))

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), x2=aT(xChars[0]), a=aT('a'), b=aT('b'), xy=aT(xChars[1]), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), givenFormulaComment3=aT(givenFormulaComment3),
                             aFormula=aT(aFormula), bFormula=aT(bFormula), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_115():
    stem = "{givenFormula}일 때, 상수 {A}, {B}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaLeft}\n{givenFormulaComment1}\n{givenFormulaComment2}\n" \
              "{givenFormulaComment3}\n따라서 {AFormula}, {BFormula}이므로 {ansFormula}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    # oneDigitInts = list(range(-9, 0)) + list(range(1, 10))
    # oneDigitLimited = list(range(-6, -1)) + list(range(2, 7))

    secondCoeffSeeds = sorted(random.sample(range(1, 7), k=3), reverse=True)
    secondCoeffSeeds[1] *= -1

    secondCoeffs = [secondCoeffSeeds[0] * secondCoeffSeeds[2], secondCoeffSeeds[1] * secondCoeffSeeds[2], secondCoeffSeeds[2]]

    frontXExps = [3, 2, 1]
    frontYExps = [1, 2, 1]

    firstCoeffs = random.sample(range(1, 9), k=3)
    firstCoeffs[2] *= -1

    #식 구성
    # part1(part2) + (part3) / part4
    # = part1(part2) + frac(part3, part4)
    # = part12 + part34
    # = part1234

    formulaPart1 = firstCoeffs[0] * x
    formulaPart2 = firstCoeffs[1] * x + firstCoeffs[2] * y
    formulaPart3 = secondCoeffs[0]*x**frontXExps[0]*y**frontYExps[0] + secondCoeffs[1]*x**frontXExps[1]*y**frontYExps[1]
    formulaPart4 = secondCoeffs[2]*x**frontXExps[2]*y**frontYExps[2]

    formulaParts = [formulaPart1, formulaPart2, formulaPart3, formulaPart4]
    formulaPartTexts = list(map(lambda x: convertIntoHangul(x, timesToSpace=True), formulaParts))
    givenFormulaLeft = joinList([formulaPartTexts[0], lp, formulaPartTexts[1], rp, ms, lp, formulaPartTexts[2], rp, dd, formulaPartTexts[3]])

    givenFormulaRight = "Ax^2 + Bxy"

    givenFormula = joinList([givenFormulaLeft, eq, givenFormulaRight])

    formulaPart34Frac = makeFractionFormula(formulaPartTexts[2], formulaPartTexts[3])
    givenFormulaComment1 = joinList([eq, formulaPartTexts[0], lp, formulaPartTexts[1], rp, ms, formulaPart34Frac])

    formulaPart12 = (formulaPart1 * formulaPart2).cancel()
    formulaPart34 = (-formulaPart3 / formulaPart4).cancel()
    givenFormulaComment2 = joinList([eq, formulaPart12, formulaPart34])
    givenFormulaComment2 = convertIntoHangul(givenFormulaComment2, timesToSpace=True)

    formulaPart1234 = (formulaPart12 + formulaPart34).cancel()
    givenFormulaComment3 = joinList([eq, formulaPart1234])
    givenFormulaComment3 = convertIntoHangul(givenFormulaComment3, minusWithSpace=True, timesToSpace=True)

    finalFormCoeffs = formulaPart1234.as_coefficients_dict()
    AVal = finalFormCoeffs[x ** 2]
    BVal = finalFormCoeffs[x*y]
    values = [AVal, BVal]
    chars = ["A", "B"]

    ValueFormulas = makeEquality(chars, values, withTag=True)

    questionFormulaDict = getRandomEquation(chars, [(1, 4), (-1, 2)], values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    questionFormulaCoeff = questionFormulaDict['coeffs']
    ansValue = questionFormulaDict['ansValue']

    ansValueEq = getNumberCalc([questionFormulaCoeff[i] * values[i] for i in range(len(chars))], withRes=True)
    ansFormula = joinList([thus, questionFormula, eq, ansValueEq])

    ansInd, choices = makeChoices(ansValue, diff=2, withTag=True)

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), A=aT("A"), B=aT("B"), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaLeft=aT(givenFormulaLeft), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), givenFormulaComment3=aT(givenFormulaComment3),
                             AFormula=ValueFormulas[0], BFormula=ValueFormulas[1], ansFormula=aT(ansFormula))

    return stem, answer, comment


def rationalandprime211_Stem_116():
    stem = "윗변의 길이가 {upperLength}, 아랫변의 길이가 {lowerLength}, 높이가 {height}인 사다리꼴의 넓이는?\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{commentText1}\n{commentText2}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = range(1, 9)

    numbers = random.sample(oneDigitInts, k=2)
    heightCoeff = random.choice([2, 4, 6, 8])

    #식 구성
    # (윗변 + 밑변) * 높이 / 2
    exps = []
    for _ in range(3):
        while True :
            n, m = random.choices(range(4), k=2)
            expSum = n+m
            expTuple = (n, m)
            if (expSum > 1) and (expSum < 5) and (expTuple not in exps):
                exps.append(expTuple)
                break

    upperLength = numbers[0] * x**exps[0][0] * y**exps[0][1]
    lowerLength = numbers[1] * x**exps[1][0] * y**exps[1][1]
    height = heightCoeff * x**exps[2][0] * y**exps[2][1]

    upperLengthText = convertIntoHangul(upperLength, timesToSpace=True)
    lowerLengthText = convertIntoHangul(lowerLength, timesToSpace=True)
    heightText = convertIntoHangul(height, timesToSpace=True)

    int2 = Integer(2)
    area = ((upperLength + lowerLength) * height / int2).cancel()
    areaText = convertIntoHangul(area, timesToSpace=True)

    heightDivided = (height/int2).cancel()
    heightDividedText = convertIntoHangul(heightDivided, timesToSpace=True)

    commentText1 = joinList([1, ov, 2, ts, lp, upperLengthText, ps, lowerLengthText, rp, ts, heightText,
                             eq, heightDividedText, lp, upperLengthText, ps, lowerLengthText, rp])

    commentText2 = joinList([eq, areaText])

    numbers = list(map(Integer, numbers))

    upperLengthWrong1 = (numbers[0]+1)/numbers[0] * upperLength
    lowerLengthWrong2 = (numbers[1]+1)/numbers[1] * lowerLength

    wrongSym1 = (area * int2).cancel()
    wrongSym2 = ((upperLengthWrong1 + lowerLength) * height / Integer(2)).cancel()
    wrongSym3 = ((upperLength + lowerLengthWrong2) * height / Integer(2)).cancel()
    wrongSym4 = ((upperLengthWrong1 + lowerLengthWrong2) * height / Integer(2)).cancel()

    choiceSyms = [wrongSym1, wrongSym2, wrongSym3, wrongSym4]
    random.shuffle(choiceSyms)

    ansInd = random.choice(range(5))
    choiceSyms.insert(ansInd, area)

    choices = list(map(lambda x: aT(convertIntoHangul(x, timesToSpace=True)), choiceSyms))



    # 내용을 채웁니다.
    stem = stem.format(upperLength=aT(upperLengthText), lowerLength=aT(lowerLengthText), height=aT(heightText),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(commentText1=aT(commentText1), commentText2=aT(commentText2))

    return stem, answer, comment


def rationalandprime211_Stem_117():
    stem = "{givenFormula}을 계산했을 때, {x}의 계수를 {a}, 상수항을 {b}라 하자. 이 때 {questionFormula}의 값을 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}\n{givenFormulaComment1}\n{givenFormulaComment2}\n{givenFormulaComment3}\n{givenFormulaComment4}\n" \
              "따라서 {aFormula}, {bFormula}이므로\n{ansFormula}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-8, 0)) + list(range(1, 9))

    coeffs = random.choices(oneDigitInts, k=5)
    coeffs[0] = abs(coeffs[0])
    coeffs[1] = abs(coeffs[1])
    coeffs[-1] = -abs(coeffs[-1])

    #식 구성
    # part1 - (part2((part3)**2 + part4) + part5) + part6(part7)
    # = part1 - (part2(part3sq + part4) + part5) + part67
    # = part1 - (part23sq45) + part67
    # = part1 - part23sq45 + part67
    # = part123sq4567

    while True :
        denoms = random.sample(range(2, 10), k=2)
        if sum(denoms) < 12 :
            break

    numerators = random.choices([1, -1], k=2)
    numerators = list(map(Integer, numerators))

    part6Coeff = denoms[0] * denoms[1]

    # print(frontCoeffs)
    formulaPart1 = coeffs[0] * x**3 * y**2
    formulaPart2 = coeffs[1] * x
    formulaPart3 = coeffs[2] * x * y
    formulaPart4 = coeffs[3] * x
    formulaPart5 = coeffs[4]
    formulaPart6 = part6Coeff * x
    formulaPart7 = (numerators[0] / denoms[0]) * x + (numerators[1] / denoms[1])
    formulaPart7Text = getPolyText(formulaPart7, x)

    givenFormula = joinList([formulaPart1, ms, "[", formulaPart2, "left {", "(", formulaPart3, ")^2", ps, formulaPart4, 'right }', formulaPart5, "]", ps, formulaPart6, lp, formulaPart7Text, rp])
    givenFormula = convertIntoHangul(givenFormula, minusWithSpace=True, timesToSpace=True)

    formulaPart3sq = formulaPart3 ** 2
    formulaPart67 = (formulaPart6 * formulaPart7).cancel()
    givenFormulaComment1 = connectEqations(joinList([formulaPart1, ms, "left {", formulaPart2, "(", formulaPart3sq, ps, formulaPart4, ')', formulaPart5, "right }"]), formulaPart67)
    givenFormulaComment1 = convertIntoHangul(givenFormulaComment1, minusWithSpace=True, timesToSpace=True)

    formulaPart23sq45 = formulaPart2 * (formulaPart3sq + formulaPart4) + formulaPart5
    formulaPart23sq45 = formulaPart23sq45.cancel()
    givenFormulaComment2 = connectEqations(joinList([formulaPart1, ms, "(", formulaPart23sq45, ")"]), formulaPart67)
    givenFormulaComment2 = convertIntoHangul(givenFormulaComment2, minusWithSpace=True, timesToSpace=True)

    formulaPart23sq45Neg = -formulaPart23sq45
    givenFormulaComment3 = connectEqations(connectEqations(formulaPart1, formulaPart23sq45Neg), formulaPart67)
    givenFormulaComment3 = convertIntoHangul(givenFormulaComment3, minusWithSpace=True, timesToSpace=True)

    formulaPart123sq4567 = formulaPart1 - formulaPart23sq45 + formulaPart67
    formulaPart123sq4567 = formulaPart123sq4567.cancel()
    givenFormulaComment4 = joinList([eq, formulaPart123sq4567])
    givenFormulaComment4 = convertIntoHangul(givenFormulaComment4, timesToSpace=True)

    xChars = [x, 1]
    resCoeffs = formulaPart123sq4567.as_coefficients_dict()
    xCoeff = resCoeffs[xChars[0]]
    constant = resCoeffs[xChars[1]]

    values = [xCoeff, constant]

    ansChars = ['a', 'b']

    aFormula, bFormula = makeEquality(ansChars, values, withTag=True)

    questionFormulaDict = getRandomEquation(ansChars, [(1, 3), (-2, 2)], values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    questionFormulaCoeff = questionFormulaDict['coeffs']
    ansValue = questionFormulaDict['ansValue']

    ansValueEq = getNumberCalc([questionFormulaCoeff[i] * values[i] for i in range(2)], withRes=True)
    ansFormula = joinList([questionFormula, eq, ansValueEq])

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), x=aT(x), a=aT('a'), b=aT('b'), questionFormula=aT(questionFormula))
    answer = answer.format(a1=aT(ansValue))
    comment = comment.format(givenFormula=aT(givenFormula),
                             givenFormulaComment1=aT(givenFormulaComment1), givenFormulaComment2=aT(givenFormulaComment2),
                             givenFormulaComment3=aT(givenFormulaComment3), givenFormulaComment4=aT(givenFormulaComment4),
                             aFormula=aT(aFormula), bFormula=aT(bFormula), ansFormula=aT(ansFormula))

    return stem, answer, comment


def rationalandprime211_Stem_118():
    stem = "0이 아닌 두 수 {x}, {y}에 대하여 {givenFormula}일 때,\n{questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}에서 {givenFormulaComment1}이므로 {givenFormulaComment2} ……㉠\n{thusQuestionFormula}\n{questionFormulaComment1}\n" \
              "{questionFormulaComment2} ({because} ㉠)\n{ansValueFormula}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitLimited = list(range(-6, -1)) + list(range(2, 7))

    xCoeffs = random.sample(range(1, 9), k=2)
    yCoeffs = random.sample(oneDigitLimited, k=2)
    denomCoeff = random.choice(range(1, 5))

    givenK = random.choice(oneDigitLimited)

    #식 구성
    # {part1(part2) - part3(part4)} / part5
    # = (part12 + part34) / part5
    # = part1234 / part5 = part1234/part5subed
    # = part12345

    givenFormula = joinList(['1 over x', ps, '1 over y', eq, givenK])
    givenFormulaComment1 = joinList(['{x', ps, "y}", ov, 'xy', eq, givenK])
    givenFormulaComment2 = joinList(['x', ps, 'y', eq, givenK, 'xy'])

    formulaPart1 = xCoeffs[0] * x
    formulaPart2 = xCoeffs[1] * x + yCoeffs[0] * y
    formulaPart3 = xCoeffs[1] * x
    formulaPart4 = xCoeffs[0] * x + yCoeffs[1] * y
    formulaPart5 = denomCoeff * (x + y)

    formulaParts = [formulaPart1, formulaPart2, formulaPart3, formulaPart4, formulaPart5]
    formulaPartTexts = list(map(lambda x: convertIntoHangul(x, timesToSpace=True), formulaParts))

    questionFormulaNumerator = joinList([formulaPartTexts[0], lp, formulaPartTexts[1], rp, ms, formulaPartTexts[2], lp, formulaPartTexts[3], rp])
    questionFormula = makeFractionFormula(questionFormulaNumerator, formulaPartTexts[4])
    thusQuestionFormula = joinList([thus, questionFormula])

    formulaPart12 = (formulaPart1 * formulaPart2).cancel()
    formulaPart34 = (-formulaPart3 * formulaPart4).cancel()
    questionFormulaComment1 = joinList([eq, makeFractionFormula(joinList([formulaPart12, formulaPart34]), formulaPartTexts[4])])
    questionFormulaComment1 = convertIntoHangul(questionFormulaComment1, timesToSpace=True)

    formulaPart1234 = (formulaPart12 + formulaPart34).cancel()
    questionFormulaComment2Left = makeFractionFormula(formulaPart1234, formulaPart5.factor())

    questionFormulaComment2Right = makeFractionFormula(formulaPart1234, joinList([givenK * denomCoeff, 'xy']))

    questionFormulaComment2 = joinList([eq, questionFormulaComment2Left, eq, questionFormulaComment2Right])
    questionFormulaComment2 = convertIntoHangul(questionFormulaComment2, minusWithSpace=True, timesToSpace=True)

    because = aT('because')

    formulaPart12345 = (formulaPart1234 / (givenK*denomCoeff*x*y)).cancel()
    formulaPart12345Text = convertIntoHangul(formulaPart12345, minusWithSpace=True)
    # print(formulaPart1234)
    questionFormulaComment3 = joinList([eq, formulaPart12345Text])

    ansInd, _choices = makeChoices(0, diff=1, withTag=False)
    choices = list(map(lambda x: aT(convertIntoHangul(x, minusWithSpace=True)), [formulaPart12345 + Integer(x) for x in _choices]))

    # 내용을 채웁니다.
    stem = stem.format(x=aT('x'), y=aT('y'), givenFormula=aT(givenFormula), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), thusQuestionFormula=aT(thusQuestionFormula),
                             questionFormulaComment1=aT(questionFormulaComment1), questionFormulaComment2=aT(questionFormulaComment2),
                             because=because, ansValueFormula=aT(questionFormulaComment3))

    return stem, answer, comment


def rationalandprime211_Stem_119():
    stem = "두 식 {a}, {b}에 대하여 ◎, ◈를 다음과 같이 약속하자.\n" \
           "   {rule1}, {rule2}\n" \
           "{givenA}, {givenB}, {givenC}일 때, {questionFormula}를 계산한 결과는?\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{questionFormula}\n{questionFormulaComment1}\n{questionFormulaComment2}\n{questionFormulaComment3}\n{questionFormulaComment4}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    aCoeffSeeds = random.sample([-1, -2, -3, 1, 2, 3], k=2)
    bCoeff = random.choice([-1, -2, -3, 1, 2, 3])
    aCoeffs = [x*bCoeff for x in aCoeffSeeds]
    cCoeffs = random.sample([-1, -2, -3, -4, 1, 2, 3, 4], k=2)

    aExps = [2, 3]
    random.shuffle(aExps)
    cExps = [1, 2]
    random.shuffle(cExps)

    ASym = aCoeffs[0] * x**aExps[0] * y**aExps[1] + aCoeffs[1] * x**aExps[1] * y**aExps[0]
    BSym = bCoeff * x * y
    CSym = cCoeffs[0] * x**cExps[0] * y**cExps[1] + random.choice([-1, 1]) * 1 / random.choice([x, y])

    syms = [ASym, BSym, CSym]
    symTexts = list(map(lambda x: convertIntoHangul(x, minusWithSpace=True, timesToSpace=True, parenToBracket=True), syms))

    # 식 구성
    # part1 / (part2)**2 - part3 * 2 * part4
    # = frac(part1 / part2sq) - part3*part4doubled
    # = part1part2sq - (part3part4doubled)
    # =  part1part2sqpart3part4doubled

    formulaPart1, formulaPart2, formulaPart3, formulaPart4 = ASym, BSym, CSym, BSym
    formulaPartTexts = symTexts + [symTexts[1]]

    chars = ['A', 'B', 'C']

    questionFormula = joinList(["(", chars[0], "◎", chars[1], ")", ms, lp, chars[2], "◈", chars[1], rp])

    rule1 = joinList(['a', "◎", 'b', eq, 'a', dd, 'b^2'])
    rule2 = joinList(['a', "◈", 'b', eq, 'a', ts, '2b'])

    givenA, givenB, givenC = makeEquality(chars, symTexts, True)

    if formulaPartTexts[-1].strip().startswith("-") :
        lastText = joinList([lp, formulaPartTexts[-1], rp])
    else :
        lastText = formulaPartTexts[-1]

    questionFormulaComment1 = joinList([eq, lp, formulaPartTexts[0], rp, dd, lp, formulaPartTexts[1], rp, pw, 2, ms, lp, formulaPartTexts[2], rp, ts, 2, ts, lastText])

    int2 = Integer(2)

    formulaPart2sq = formulaPart2 ** 2
    formulaPart2sqText = convertIntoHangul(formulaPart2sq, timesToSpace=True, minusWithSpace=True, parenToBracket=True)
    formulaPart12Text = makeFractionFormula(formulaPartTexts[0], formulaPart2sqText)

    formulaPart4doubled = formulaPart4 * int2
    formulaPart4doubledText = convertIntoHangul(formulaPart4doubled, timesToSpace=True, minusWithSpace=True, parenToBracket=True)
    if formulaPartTexts[-1].strip().startswith("-") :
        formulaPart4doubledText = joinList([lp, formulaPart4doubledText, rp])

    questionFormulaComment2 = joinList([eq, formulaPart12Text, ms, lp, formulaPartTexts[2], rp, ts, formulaPart4doubledText])

    formulaPart12 = (formulaPart1 / formulaPart2sq).cancel()
    formulaPart34 = (formulaPart3 * formulaPart4doubled).cancel()

    formulaPart12Text = convertIntoHangul(getPolyText(formulaPart12), timesToSpace=True, minusWithSpace=True, parenToBracket=True)
    formulaPart34Text = convertIntoHangul(formulaPart34, timesToSpace=True, minusWithSpace=True, parenToBracket=True)

    questionFormulaComment3 = joinList([eq, formulaPart12Text, ms, lp, formulaPart34Text, rp])

    formulaPart1234 = (formulaPart12 - formulaPart34).cancel()
    formulaPart1234Text = convertIntoHangul(getPolyText(formulaPart1234), timesToSpace=True, minusWithSpace=True, parenToBracket=True)
    questionFormulaComment4 = joinList([eq, formulaPart1234Text])

    # 오류 정답지
    # part1 / part2 - part3 * 2 * part4
    # part1 / part2**2 - part3 * part4
    # part1 / part2 - part3 * part4
    # part1 / (part2)**2 + part3 * 2 * part4

    wrongSym1 = formulaPart1 / formulaPart2 - formulaPart34
    wrongSym2 = formulaPart12 - formulaPart3 * formulaPart4
    wrongSym3 = formulaPart1 / formulaPart2 - formulaPart3 * formulaPart4
    wrongSym4 = formulaPart12 + formulaPart34

    choiceSyms = [wrongSym1, wrongSym2, wrongSym3, wrongSym4]
    random.shuffle(choiceSyms)

    ansInd = random.choice(range(5))
    choiceSyms.insert(ansInd, formulaPart1234)

    choices = list(map(lambda x: aT(convertIntoHangul(getPolyText(x.cancel()), minusWithSpace=True, timesToSpace=True, parenToBracket=True)), choiceSyms))

    # 내용을 채웁니다.
    stem = stem.format(a=aT('a'), b=aT('b'), rule1=aT(rule1), rule2=aT(rule2), givenA=aT(givenA), givenB=aT(givenB), givenC=aT(givenC), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(questionFormula=aT(questionFormula), questionFormulaComment1=aT(questionFormulaComment1),
                             questionFormulaComment2=aT(questionFormulaComment2), questionFormulaComment3=aT(questionFormulaComment3),
                             questionFormulaComment4=aT(questionFormulaComment4))
    return stem, answer, comment


def rationalandprime211_Stem_120():
    stem = "{aFormula}, {bFormula}일 때, {questionFormula}를 {x}, {y}에 대한 식으로 나타낸 것은?\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{questionFormulaComment1}\n{questionFormulaComment2}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-5, 0)) + list(range(1, 6))
    # oneDigitLimited = list(range(-6, -1)) + list(range(2, 7))
    oneOrMinus = random.choice([1, -1])

    coeffs = random.sample(oneDigitInts, k=4)

    denom = random.choice([2, 3])
    if denom == 2 :
        bCoeff = random.choice(range(2, 10, 2))
    else :
        bCoeff = random.choice([3, 6, 9])

    aCoeff = random.choice(range(2, 5))
    denom = Integer(denom)

    #식 구성
    # part1 +- part2
    # = part12

    formulaPart1 = coeffs[0]*x + coeffs[1]*y
    formulaPart2Numerator = coeffs[2]*x + coeffs[3]*y

    formulaPart1Text = convertIntoHangul(formulaPart1)
    formulaPart2Text = makeFractionFormula(convertIntoHangul(formulaPart2Numerator), denom)

    aFormula = joinList(["A", eq, formulaPart1Text])
    bFormula = joinList(["B", eq, formulaPart2Text])

    if oneOrMinus == 1 :
        operator = ps
    else :
        operator = ms
    questionFormula = joinList([aCoeff, "A", operator, bCoeff, "B"])

    questionFormulaComment1 = joinList([questionFormula, eq, aCoeff, ts, lp, formulaPart1Text, rp, operator, bCoeff, ts, lp, formulaPart2Text, rp])


    formulaPart1Multiplied = aCoeff * formulaPart1
    formulaPart2Multiplied = bCoeff * formulaPart2Numerator * oneOrMinus / denom

    formulaPart12 = formulaPart1Multiplied + formulaPart2Multiplied
    formulaPart12 = formulaPart12.cancel()

    questionFormulaComment2 = joinList([eq, connectEqations(formulaPart1Multiplied, formulaPart2Multiplied), eq, formulaPart12])
    questionFormulaComment2 = convertIntoHangul(questionFormulaComment2)


    formulaPart1Wrong1 = formulaPart1 + x
    formulaPart1Wrong2 = formulaPart1 - y
    formulaPart2Wrong3 = formulaPart2Numerator - x
    formulaPart2Wrong4 = formulaPart2Numerator + y

    wrongSym1 = aCoeff*formulaPart1Wrong1 + formulaPart2Multiplied
    wrongSym2 = aCoeff*formulaPart1Wrong2 + formulaPart2Multiplied
    wrongSym3 = formulaPart1Multiplied + bCoeff * formulaPart2Wrong3 * oneOrMinus / denom
    wrongSym4 = formulaPart1Multiplied + bCoeff * formulaPart2Wrong4 * oneOrMinus / denom

    choiceSyms = [wrongSym1, wrongSym2, wrongSym3, wrongSym4]
    random.shuffle(choiceSyms)

    ansInd = random.choice(range(5))
    choiceSyms.insert(ansInd, formulaPart12)

    choices = list(map(lambda x: aT(convertIntoHangul(x.cancel())), choiceSyms))

    # 내용을 채웁니다.
    stem = stem.format(aFormula=aT(aFormula), bFormula=aT(bFormula), questionFormula=aT(questionFormula), x=aT(x), y=aT(y),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(questionFormulaComment1=aT(questionFormulaComment1), questionFormulaComment2=aT(questionFormulaComment2))

    return stem, answer, comment


def rationalandprime211_Stem_121():
    stem = "{aFormula}, {bFormula}일 때, {questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{questionFormulaComment1}\n{questionFormulaComment2}\n{questionFormulaComment3}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    a, b = symbols("a b", real=True)

    fracs = []
    while len(fracs) < 2 :
        temp = makeRandomFraction(repeat='rand', repeatMax=10, nonrepeatMax=10, maxDigit={'numerator':(1, [1]), 'denominator':(1, [1])})
        if temp not in fracs :
            fracs.append(temp)


    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))
    oneOrMinus = random.choice([1, -1])

    coeffs = random.sample(oneDigitInts, k=3)

    fracSigns = random.choices([-1, 1], k=2)

    #식 구성
    # part1 / part2
    # = part12

    formulaPart1 = coeffs[0]*a*b**2 + coeffs[1]*a**2*b
    formulaPart2 = coeffs[2]*a**2*b**2

    formulaPart1Text = convertIntoHangul(formulaPart1, timesToSpace=True)
    formulaPart2Text = convertIntoHangul(formulaPart2, timesToSpace=True)

    questionFormula = makeFractionFormula(formulaPart1Text, formulaPart2Text)

    fracText = []
    for i, f in enumerate(fracs):
        if fracSigns[i] > 0 :
            temp = makeFractionFormula(f[0], f[1])
        else :
            temp = joinList([ms, makeFractionFormula(f[0], f[1])])
        fracText.append(temp)

    aFormula = joinList(["a", eq, fracText[0]])
    bFormula = joinList(["b", eq, fracText[1]])

    simplified1Coeff = coeffs[0] / Integer(coeffs[2])
    simplified2Coeff = coeffs[1] / Integer(coeffs[2])

    aSym = fracSigns[0] * fracs[0][0] / Integer(fracs[0][1])
    bSym = fracSigns[1] * fracs[1][0] / Integer(fracs[1][1])

    simplified1 = simplified1Coeff / a
    simplified2 = simplified2Coeff / b

    questionFormulaComment1Right = convertIntoHangul(connectEqations(simplified1, simplified2), minusWithSpace=True, parenToBracket=True)

    questionFormulaComment1 = joinList([questionFormula, eq, questionFormulaComment1Right])

    simplified1CoeffText = convertIntoHangul(simplified1Coeff, minusWithSpace=True)
    simplified2CoeffText = convertIntoHangul(simplified2Coeff, minusWithSpace=True)

    if simplified1Coeff < 0 :
        simplified1CoeffText = joinList([lp, simplified1CoeffText, rp])
    if fracSigns[0] < 0 :
        fracText[0] = joinList([lp, fracText[0], rp])
    if fracSigns[1] < 0 :
        fracText[1] = joinList([lp, fracText[1], rp])

    questionFormulaComment2Right = connectEqations(joinList([simplified1CoeffText, dd, fracText[0]]), joinList([simplified2CoeffText, dd, fracText[1]]))
    questionFormulaComment2 = joinList([eq, questionFormulaComment2Right])

    aSymInversed = 1 / aSym
    bSymInversed = 1 / bSym

    aSymInversedText = convertIntoHangul(aSymInversed, minusWithSpace=True)
    if fracSigns[0] < 0 :
        aSymInversedText = joinList([lp, aSymInversedText, rp])
    bSymInversedText = convertIntoHangul(bSymInversed, minusWithSpace=True)
    if fracSigns[1] < 0 :
        bSymInversedText = joinList([lp, bSymInversedText, rp])

    questionFormulaComment3Left = connectEqations(joinList([simplified1CoeffText, ts, aSymInversedText]), joinList([simplified2CoeffText, ts, bSymInversedText]))

    ansValue = simplified1Coeff * aSymInversed + simplified2Coeff * bSymInversed
    ansValueText = convertIntoHangul(ansValue, minusWithSpace=True)

    questionFormulaComment3 = joinList([eq, questionFormulaComment3Left, eq, ansValueText])

    ansInd, choiceDiffs = makeChoices(0, diff=1, withTag=False)
    choiceValues = [ansValue + int(i) for i in choiceDiffs]
    choices = list(map(lambda x: aT(convertIntoHangul(x, minusWithSpace=True)), choiceValues))


    # 내용을 채웁니다.
    stem = stem.format(aFormula=aT(aFormula), bFormula=aT(bFormula), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(questionFormulaComment1=aT(questionFormulaComment1), questionFormulaComment2=aT(questionFormulaComment2),
                             questionFormulaComment3=aT(questionFormulaComment3))

    return stem, answer, comment


def rationalandprime211_Stem_122():
    stem = "{aFormula}, {bFormula}일 때,\n{largeAFormula}, {largeBFormula}에 대하여 {A}, {B}중 식의 값이 더 큰 것을 구하시오.\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{largeAFormula}\n{largeAFormulaComment1}\n{largeAFormulaComment2}\n{largeBFormula}\n{largeBFormulaComment1}\n{largeBFormulaComment2}\n" \
              "따라서 {a1}의 식의 값이 더 크다.\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    a, b = symbols("a b", real=True)

    aVal, bVal = random.sample([-3, -2, -1, 1, 2, 3], k=2)

    if aVal < 0 :
        aText = joinList([lp, aVal, rp])
    else :
        aText = str(aVal)

    if bVal < 0 :
        bText = joinList([lp, bVal, rp])
    else :
        bText = str(bVal)

    aFormula, bFormula = makeEquality(['a', 'b'], [aVal, bVal], withTag=True)

    # ================================== largeA part ========================================

    oneOrMinus = [1, -1]

    coeffs = random.sample(range(1, 9), k=6)
    coeffs[2] *= random.choice(oneOrMinus)
    coeffs[5] *= random.choice(oneOrMinus)

    # 식 구성
    # part1(part2) - part3(part4)
    # = part12 - part34
    # = part1234

    # print(frontCoeffs)
    formulaPart1 = coeffs[0] * a
    formulaPart2 = coeffs[1] * a + coeffs[2] * b
    formulaPart3 = coeffs[3] * a
    formulaPart4 = coeffs[4] * a + coeffs[5] * b

    largeAFormulaRight = joinList([formulaPart1, "(", formulaPart2, ")", ms, formulaPart3, "(", formulaPart4, ")"])
    largeAFormulaRight = convertIntoHangul(largeAFormulaRight, minusWithSpace=True, timesToSpace=True)

    largeAFormula = joinList(["A", eq, largeAFormulaRight])

    formulaPart12 = (formulaPart1 * formulaPart2).cancel()
    formulaPart34 = (-formulaPart3 * formulaPart4).cancel()
    formulaPart1234 = (formulaPart12 + formulaPart34).cancel()
    largeAFormulaComment1 = joinList([eq, formulaPart12, formulaPart34, eq, formulaPart1234])
    largeAFormulaComment1 = convertIntoHangul(largeAFormulaComment1, minusWithSpace=True, timesToSpace=True)

    formulaPart1234Text = str(formulaPart1234)
    formulaPart1234Text = formulaPart1234Text.replace("a", aText)
    formulaPart1234Text = formulaPart1234Text.replace("b", bText)

    formulaPart1234Text = convertIntoHangul(formulaPart1234Text, leaveTimes=True)

    largeAValue = formulaPart1234.subs([(a, aVal), (b, bVal)])

    largeAFormulaComment2 = joinList([eq, formulaPart1234Text, eq, largeAValue])

    # ================================ largeB part ===============================================

    intRange = list(range(-5, 6))
    intRange.remove(0)

    def makeRandomItem(positive=False):
        coeff = random.choice(intRange)

        if positive :
            coeff = abs(coeff)

        while True :
            n, m = random.choices(range(3), k=2)
            expSum = n+m
            if (expSum > 0) and (expSum < 4) :
                break

        return (coeff * a**n * b**m, [n, m])

    while True :
        length=2
        seedItemTuple = makeRandomItem(positive=True)
        symExps = [seedItemTuple[1]]
        symItems = [seedItemTuple[0]]
        for j in range(length):
            while True :
                itemTuple = makeRandomItem()
                if itemTuple[1] not in symExps :
                    symExps.append(itemTuple[1])
                    symItems.append(itemTuple[0])
                    break

        rightSym = sum(symItems[1:])
        leftSym = rightSym * symItems[0]

        rightSym = rightSym.cancel()
        leftSym = leftSym.cancel()

        symCalced = [leftSym, symItems[0], rightSym]

        largeBFormulaRight = joinList(["(", symCalced[0], ")", dd, symCalced[1]])
        largeBFormulaRight = convertIntoHangul(largeBFormulaRight, minusWithSpace=True, timesToSpace=True)

        largeBFormula = joinList(["B", eq, largeBFormulaRight])

        largeBFormulaFraction = makeFractionFormula(symCalced[0], symCalced[1])
        largeBFormulaFraction = convertIntoHangul(largeBFormulaFraction, parenToBracket=True, timesToSpace=True, minusWithSpace=True)

        largeBFormulaComment1 = joinList([eq, largeBFormulaFraction, eq, rightSym])
        largeBFormulaComment1 = convertIntoHangul(largeBFormulaComment1, timesToSpace=True, minusWithSpace=True)

        rightSymText = str(rightSym)
        rightSymText = rightSymText.replace("a", aText)
        rightSymText = rightSymText.replace('b', bText)

        largeBValue = rightSym.subs([(a, aVal), (b, bVal)])

        if largeAValue != largeBValue :
            largeBFormulaComment2 = joinList([eq, rightSymText, eq, largeBValue])
            largeBFormulaComment2 = convertIntoHangul(largeBFormulaComment2, leaveTimes=True)
            break

    # ================================
    if largeAValue > largeBValue :
        ansChar = "A"
    else :
        ansChar = "B"

    # 내용을 채웁니다.
    stem = stem.format(aFormula=aT(aFormula), bFormula=aT(bFormula), largeAFormula=aT(largeAFormula), largeBFormula=aT(largeBFormula),
                       A=aT("A"), B=aT("B"))
    answer = answer.format(a1=aT(ansChar))
    comment = comment.format(largeAFormula=aT(largeAFormula), largeAFormulaComment1=aT(largeAFormulaComment1),
                             largeAFormulaComment2=aT(largeAFormulaComment2), largeBFormula=aT(largeBFormula),
                             largeBFormulaComment1=aT(largeBFormulaComment1), largeBFormulaComment2=aT(largeBFormulaComment2),
                             a1=aT(ansChar))

    return stem, answer, comment


def rationalandprime211_Stem_123():
    stem = "{xEquation}일 때, {givenFormula}{postp} {y}에 대한 식으로 나타내면 {yFormula}이다. 상수 {abc}에 대하여 {questionFormula}의 값은?\n"\
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormulaComment1}\n{givenFormulaComment2}\n{givenFormulaComment3}\n{givenFormulaComment4}이므로\n" \
              "{aFormula}, {bFormula}, {cFormula}\n{thusAnswer}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    yFormula = "ay^2 + by + c"
    oneDigitInts = list(range(-7, 0)) + list(range(1, 8))
    oneDigitInts2 = list(range(-6, 0)) + list(range(1, 7))
    givenFormulaCoeffs = random.sample(oneDigitInts, k=3)
    xEquationCoeffs = random.sample(oneDigitInts2, k=2)

    #식 구성
    # givenFormula = xEquationReplacement
    # = part1 -part2
    # = part12

    givenFormulaSym = givenFormulaCoeffs[0]*x + givenFormulaCoeffs[1]*x*y + givenFormulaCoeffs[2]
    xFormulaSym = xEquationCoeffs[0]*y + xEquationCoeffs[1]

    givenFormula = convertIntoHangul(givenFormulaSym, timesToSpace=True)
    postp = proc_jo(abs(givenFormulaCoeffs[2]), 1)
    xFormulaRight = convertIntoHangul(getPolyText(xFormulaSym), timesToSpace=True)
    xFormula = joinList(["x", eq, xFormulaRight])

    xFormulaReplacement = joinList([lp, xFormulaRight, rp])

    givenFormulaReplaced = givenFormula.replace("x", xFormulaReplacement)

    givenFormulaComment1 = joinList([givenFormula, eq, givenFormulaReplaced])

    givenFormulaSymReplacedPart1 = givenFormulaCoeffs[0] * xFormulaSym
    givenFormulaSymReplacedPart2 = (givenFormulaCoeffs[1] * xFormulaSym * y).cancel()

    givenFormulaReplaced2 = connectEqations(connectEqations(getPolyText(givenFormulaSymReplacedPart2), givenFormulaSymReplacedPart1), givenFormulaCoeffs[2])
    givenFormulaReplaced2Text = convertIntoHangul(givenFormulaReplaced2, timesToSpace=True)

    givenFormulaComment2 = joinList([eq, givenFormulaReplaced2Text])

    finalForm = givenFormulaSym.subs(x, xFormulaSym).cancel()
    finalFormText = convertIntoHangul(getPolyText(finalForm), timesToSpace=True)

    givenFormulaComment3 = joinList([eq, finalFormText])

    givenFormulaComment4 = joinList([finalFormText, eq, yFormula])

    finalFormCoeffs = finalForm.as_coefficients_dict()
    aVal = finalFormCoeffs[y**2]
    bVal = finalFormCoeffs[y]
    cVal = finalFormCoeffs[1]

    values = [aVal, bVal, cVal]
    chars = ['a', 'b', 'c']

    questionFormulaDict = getRandomEquation(givenChars=chars, coefficientRange=[(1, 4), (-2, 3), (-2, 3)], realValues=values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']
    questionFormulaCoeffs = questionFormulaDict['coeffs']

    ansInd, choices = makeChoices(ansValue, diff=2)

    ansValueEq = getNumberCalc([questionFormulaCoeffs[i]*values[i] for i in range(len(values))], withRes=True)
    thusAnswer = joinList([thus, questionFormula, eq, ansValueEq])

    aFormula, bFormula, cFormula = makeEquality(chars, values, withTag=True)


    # 내용을 채웁니다.
    stem = stem.format(xEquation=aT(xFormula), givenFormula=aT(givenFormula), postp=postp, y=aT(y), yFormula=aT(yFormula),
                       abc=aT(joinList(chars, ',~ ')), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormulaComment1=aT(givenFormulaComment1), givenFormulaComment2=aT(givenFormulaComment2),
                             givenFormulaComment3=aT(givenFormulaComment3), givenFormulaComment4=aT(givenFormulaComment4),
                             aFormula=aT(aFormula), bFormula=aT(bFormula), cFormula=aT(cFormula), thusAnswer=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_124():
    stem = "{xEquation}일 때, {givenFormula}{postp} {y}에 대한 식으로 나타내면 {yFormula}이다. 상수 {pq}에 대하여 {questionFormula}의 값은?\n"\
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{xEquation}에서 {xEquationComment}\n{thusGivenFormulaComment1}\n{givenFormulaComment2}\n{givenFormulaComment3}\n" \
              "따라서 {pFormula}, {qFormula}이므로\n{thusFormula}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    yFormula = "py + q"
    oneDigitInts = list(range(-7, 0)) + list(range(1, 8))
    oneDigitInts2 = list(range(-6, 0)) + list(range(1, 7))
    while True :
        givenFormulaCoeffs = random.sample(oneDigitInts, k=3)
        xEquationCoeffs = random.sample(oneDigitInts2, k=2)

        if xEquationCoeffs[0]*givenFormulaCoeffs[0] != -givenFormulaCoeffs[1] :
            break

    #식 구성
    # givenFormula = xEquationReplacement
    # = part1 -part2
    # = part12

    givenFormulaSymPart1 = givenFormulaCoeffs[0]*x
    givenFormulaSymPart2 = givenFormulaCoeffs[1]*y + givenFormulaCoeffs[2]
    givenFormulaSym = givenFormulaSymPart1 + givenFormulaSymPart2
    xFormulaSym1 = xEquationCoeffs[0]*y + xEquationCoeffs[1]
    xFormulaSym2 = x - xFormulaSym1

    givenFormula = convertIntoHangul(givenFormulaSym, timesToSpace=True)
    postp = proc_jo(abs(givenFormulaCoeffs[2]), 1)
    xFormulaLeft = convertIntoHangul(getPolyText(xFormulaSym2), timesToSpace=True)
    xFormulaRight = convertIntoHangul(xFormulaSym1, timesToSpace=True)

    xEquation = joinList([xFormulaLeft, eq, 0])
    xEquationComment = joinList(["x", eq, xFormulaRight])

    xFormulaReplacement = joinList([lp, xFormulaRight, rp])

    givenFormulaReplaced = givenFormula.replace("x", xFormulaReplacement)

    thusGivenFormulaComment1 = joinList([thus, givenFormula, eq, givenFormulaReplaced])

    givenFormulaSymReplacedPart1 = givenFormulaCoeffs[0] * xFormulaSym1

    # print(givenFormulaSymPart2, getPolyText((givenFormulaSymPart2)))
    givenFormulaReplaced2 = connectEqations(*list(map(getPolyText, [givenFormulaSymReplacedPart1, givenFormulaSymPart2])))
    givenFormulaReplaced2Text = convertIntoHangul(givenFormulaReplaced2, timesToSpace=True)

    givenFormulaComment2 = joinList([eq, givenFormulaReplaced2Text])

    finalForm = givenFormulaSym.subs(x, xFormulaSym1).cancel()
    # print(finalForm)
    finalFormText = convertIntoHangul(getPolyText(finalForm), timesToSpace=True)

    givenFormulaComment3 = joinList([eq, finalFormText])

    finalFormCoeffs = finalForm.as_coefficients_dict()
    pVal = finalFormCoeffs[y]
    qVal = finalFormCoeffs[1]

    values = [pVal, qVal]
    chars = ['p', 'q']
    coeffRange = [(1, 4), (-2, 3), (-2, 3)]

    questionFormulaDict = getRandomEquation(givenChars=chars, coefficientRange=coeffRange[:len(values)], realValues=values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    ansValue = questionFormulaDict['ansValue']
    questionFormulaCoeffs = questionFormulaDict['coeffs']

    ansInd, choices = makeChoices(ansValue, diff=2)

    ansValueEq = getNumberCalc([questionFormulaCoeffs[i]*values[i] for i in range(len(values))], withRes=True)
    thusAnswer = joinList([thus, questionFormula, eq, ansValueEq])

    pFormula, qFormula = makeEquality(chars, values, withTag=True)


    # 내용을 채웁니다.
    stem = stem.format(xEquation=aT(xEquation), givenFormula=aT(givenFormula), postp=postp, y=aT(y), yFormula=aT(yFormula),
                       pq=aT(joinList(chars, ',~ ')), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(xEquation=aT(xEquation), xEquationComment=aT(xEquationComment), thusGivenFormulaComment1=aT(thusGivenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), givenFormulaComment3=aT(givenFormulaComment3),
                             pFormula=aT(pFormula), qFormula=aT(qFormula), thusFormula=aT(thusAnswer))

    return stem, answer, comment


def rationalandprime211_Stem_125():
    stem = "두 자리 자연수 {A}의 십의 자리의 숫자는 {firstDigitFormula}, 일의 자리의 숫자는 {secondDigitFormula}이다. {givenFormula}일 때, {A}를 {a}의 식으로 나타내면?\n" \
           "① {s1}\n② {s2}\n③ {s3}\n④ {s4}\n⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}에서 {givenFormulaSolved}\n{thusAComment1}\n{thusAComment2}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    a, b = symbols("a b", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))
    posDigits = range(0, 10)
    posDigitsWithoutZero = range(1, 10)

    maximum = 10
    while True :
        while True :
            firstDigitFormulaPA = random.choices(oneDigitInts, k=2)
            secondDigitFormulaPB = random.choices(oneDigitInts, k=2)
            if (sum(map(abs, firstDigitFormulaPA)) <= maximum) and (sum(map(abs, secondDigitFormulaPB)) <= maximum) :
                break

        givenFormulaCoeffSeed = random.choice([-2, -3, 2, 3])
        givenFormulaCoeffs = [0, givenFormulaCoeffSeed]
        if abs(givenFormulaCoeffSeed)==2 :
            givenFormulaCoeffs[0] = random.choice([4, 6, 8])
        else :
            givenFormulaCoeffs[0] = random.choice([6, 9])

        # 식 구성
        # pa + q = r / pb + q = r
        while True :
            r1 = random.choice(posDigitsWithoutZero)
            r2 = random.choice(posDigits)

            q1 = r1 - reduce(mul, firstDigitFormulaPA)
            q2 = r2 - reduce(mul, secondDigitFormulaPB)

            if q1 and q2 :
                break

        firstDigitFormulaSym = firstDigitFormulaPA[0] * a + q1
        firstDigitFormulaSymText = convertIntoHangul(getPolyText(firstDigitFormulaSym), timesToSpace=True)
        secondDigitFormulaSym = secondDigitFormulaPB[0] * b + q2
        secondDigitFormulaSymText = convertIntoHangul(getPolyText(secondDigitFormulaSym), timesToSpace=True)

        # print(firstDigitFormulaSymText, "/", secondDigitFormulaSymText, "/", r1, r2)

        givenFormulaSym = givenFormulaCoeffs[0] * a + givenFormulaCoeffs[1] * b
        givenFormulaValue = givenFormulaSym.subs([(a, firstDigitFormulaPA[1]), (b, secondDigitFormulaPB[1])])

        givenFormula = joinList([givenFormulaSym, eq, givenFormulaValue])
        givenFormula = convertIntoHangul(givenFormula, minusWithSpace=True, timesToSpace=True)

        givenFormulaSolvedSym = solve(givenFormulaSym - givenFormulaValue, b)[0]
        # print(givenFormula, "/", givenFormulaSolvedSym)
        givenFormulaSolvedRightText = convertIntoHangul(getPolyText(givenFormulaSolvedSym), minusWithSpace=True, timesToSpace=True)
        givenFormulaSolvedText = joinList(['b', eq, givenFormulaSolvedRightText])

        largeASym = 10 * firstDigitFormulaSym + secondDigitFormulaSym
        largeASymText = convertIntoHangul(largeASym, minusWithSpace=True, timesToSpace=True)
        largeACommentLeft = connectEqations(joinList([10, lp, firstDigitFormulaSymText, rp]), secondDigitFormulaSymText)
        thusAComment1 = joinList([thus, "A", eq, largeACommentLeft, eq, largeASymText])

        largeASymTextReplaced = largeASymText.replace('b', joinList([lp, givenFormulaSolvedRightText, rp]))

        finalFormSym = largeASym.subs(b, givenFormulaSolvedSym).cancel()
        finalFormSymCoeffs = finalFormSym.as_coefficients_dict()

        if finalFormSymCoeffs[a] :
            break

    finalFormSymText = convertIntoHangul(getPolyText(finalFormSym), minusWithSpace=True, timesToSpace=True)
    thusAComment2 = joinList([eq, largeASymTextReplaced, eq, finalFormSymText])


    # print(finalFormSym, "/", finalFormSymCoeffs)
    ansACoeff = finalFormSymCoeffs[a]
    ansConstant = finalFormSymCoeffs[1]

    while True :
        ansInd, choiceACoeffs = makeChoices(0, diff=2, withTag=False)
        realACoeffs = [x+ansACoeff for x in choiceACoeffs]
        if 0 not in realACoeffs :
            break
    # print(choiceXCoeffs)
    choiceACoeffs.remove(0)

    _, choiceConstants = makeChoices(0, diff=1, withTag=False)
    choiceConstants.remove(0)

    choices = []
    for i in range(4):
        tempForm = (choiceACoeffs[i] + ansACoeff) * a + (choiceConstants[i] + ansConstant)
        tempFormText = convertIntoHangul(getPolyText(tempForm), minusWithSpace=True, timesToSpace=True)
        choices.append(aT(tempFormText))

    ansForm = aT(finalFormSymText)
    choices.insert(ansInd, ansForm)

    # 내용을 채웁니다.
    stem = stem.format(A=aT('A'), firstDigitFormula=aT(firstDigitFormulaSymText), secondDigitFormula=aT(secondDigitFormulaSymText), givenFormula=aT(givenFormula), a=aT(a),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaSolved=aT(givenFormulaSolvedText), thusAComment1=aT(thusAComment1), thusAComment2=aT(thusAComment2))

    return stem, answer, comment


def rationalandprime211_Stem_126():
    stem = "{givenFormula}일 때, {questionFormula}를 {y}의 식으로 나타내면?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}에서 {givenFormulaComment1}\n{givenFormulaComment2}, {givenFormulaComment3}\n{thusX}\n" \
              "{questionFormula}\n{questionFormulaComment1}\n{questionFormulaComment2}\n{questionFormulaComment3}\n{questionFormulaComment4}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    # part1 / part2
    # = part12
    yCoeff = random.choice(oneDigitInts)

    maximum = 10
    while True :
        numeratorCoeffs = random.sample(oneDigitInts, k=2)
        denomCoeffs = random.sample(oneDigitInts, k=2)

        if not ((numeratorCoeffs != denomCoeffs) and (sum(map(abs, numeratorCoeffs)) <= maximum) and \
                (sum(map(abs, denomCoeffs)) <= maximum) and (denomCoeffs[0]*yCoeff + denomCoeffs[1]) and \
                (numeratorCoeffs[0]*yCoeff + numeratorCoeffs[1])) :
            continue

        numeratorSym = numeratorCoeffs[0] * x + numeratorCoeffs[1] * y
        denominatorSym = denomCoeffs[0] * x + denomCoeffs[1] * y

        numeratorText = convertIntoHangul(numeratorSym, timesToSpace=True)
        denomText = convertIntoHangul(denominatorSym, timesToSpace=True)

        givenFormulaLeft = makeFractionFormula(numeratorText, denomText)

        fracSym = numeratorSym / denominatorSym
        fracSymReplacedValue = fracSym.subs(x, yCoeff*y).cancel()
        fracSymValueText = convertIntoHangul(fracSymReplacedValue, minusWithSpace=True, timesToSpace=True)

        givenFormula = joinList([givenFormulaLeft, eq, fracSymValueText])

        fracSymValueNumerator = int(fracSymReplacedValue.p)
        fracSymValueDenominator = int(fracSymReplacedValue.q)

        if fracSymValueDenominator == 1 :
            leftPart = numeratorText
        elif fracSymValueDenominator == -1 :
            leftPart = joinList([ms, lp, numeratorText, rp])
        else :
            leftPart = joinList([fracSymValueDenominator, lp, numeratorText, rp])

        if fracSymValueNumerator == 1 :
            rightPart = denomText
        elif fracSymValueNumerator == -1 :
            rightPart = joinList([ms, lp, denomText, rp])
        else :
            rightPart = joinList([fracSymValueNumerator, lp, denomText, rp])

        givenFormulaComment1 = joinList([leftPart, eq, rightPart])

        leftPartSym = fracSymValueDenominator * numeratorSym
        rightPartSym = fracSymValueNumerator * denominatorSym

        if leftPartSym == rightPartSym :
            continue

        givenFormulaComment2 = joinList([leftPartSym, eq, rightPartSym])
        givenFormulaComment2 = convertIntoHangul(givenFormulaComment2, timesToSpace=True)

        xCalcCoeff = fracSymValueDenominator * numeratorCoeffs[0] - fracSymValueNumerator * denomCoeffs[0]
        yCalcCoeff = (fracSymValueDenominator * numeratorCoeffs[1] - fracSymValueNumerator * denomCoeffs[1]) * -1

        xForm = xCalcCoeff * x
        yForm = yCalcCoeff * y
        givenFormulaComment3 = joinList([xForm, eq, yForm])
        givenFormulaComment3 = convertIntoHangul(givenFormulaComment3)

        # print(leftPartSym, rightPartSym)
        xFormulaRight = solve(leftPartSym-rightPartSym, x)[0]
        xFormulaRightText = convertIntoHangul(xFormulaRight, minusWithSpace=True, timesToSpace=True)
        xFormula = joinList([x, eq, xFormulaRightText])
        thusX = joinList([thus, xFormula])

        # 식 구성
        # part1 - {part2 - (part3) (part4)}
        # = part1 - (part234)
        # = part1234

        while True :
            positives = random.sample(range(1, 10), k=3)
            if positives[0] - positives[1] + positives[2] :
                break

        while True :
            posnegs = random.sample(oneDigitInts, k=2)
            if (sum(map(abs, posnegs)) <= maximum):
                break

        formulaPart1 = positives[0] * x
        formulaPart2 = positives[1] * x
        formulaPart3 = positives[2] * x + posnegs[0] * y
        formulaPart4 = posnegs[1] * y

        questionFormula1 = joinList([formulaPart1, "- left {", formulaPart2, ms, lp, formulaPart3, rp])
        questionFormula2 = joinList([formulaPart4, 'right }'])
        questionFormula = connectEqations(questionFormula1, questionFormula2)
        questionFormula = convertIntoHangul(questionFormula)

        formulaPart234 = formulaPart2 - formulaPart3 + formulaPart4
        questionFormulaComment1 = joinList([eq, formulaPart1, ms, lp, formulaPart234, rp])
        questionFormulaComment1 = convertIntoHangul(questionFormulaComment1)

        formulaPart1234 = formulaPart1 - formulaPart234
        formulaPart1234Text = convertIntoHangul(formulaPart1234)
        questionFormulaComment2 = joinList([eq, formulaPart1234Text])

        xFormulaReplacement = joinList([lp, xFormulaRightText, rp])
        formulaPart1234TextReplaced = formulaPart1234Text.replace("x", xFormulaReplacement)

        questionFormulaComment3 = joinList([eq, formulaPart1234TextReplaced])

        finalRes = formulaPart1234.subs(x, xFormulaRight).cancel()
        if finalRes :
            break

    finalResCoeff = int(finalRes.coeff(y))

    questionFormulaComment4 = joinList([eq, finalRes])
    questionFormulaComment4 = convertIntoHangul(questionFormulaComment4)

    while True :
        ansInd, coeffAdjusts = makeChoices(0, diff=2, withTag=False)
        realACoeffs = [x+finalResCoeff for x in coeffAdjusts]
        if 0 not in realACoeffs :
            break

    choices = []
    for i in range(5):
        tempForm = (coeffAdjusts[i] + finalResCoeff) * y
        tempFormText = convertIntoHangul(getPolyText(tempForm), minusWithSpace=True, timesToSpace=True)
        choices.append(aT(tempFormText))


    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), questionFormula=aT(questionFormula), y=aT(y),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1), givenFormulaComment2=aT(givenFormulaComment2),
                             givenFormulaComment3=aT(givenFormulaComment3), thusX=aT(thusX), questionFormula=aT(questionFormula),
                             questionFormulaComment1=aT(questionFormulaComment1), questionFormulaComment2=aT(questionFormulaComment2) ,
                             questionFormulaComment3=aT(questionFormulaComment3), questionFormulaComment4=aT(questionFormulaComment4))

    return stem, answer, comment


def rationalandprime211_Stem_127():
    stem = "{givenFormula}일 때, {questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}에서 {givenFormulaComment1}\n{givenFormulaComment2}, {givenFormulaComment3}  {thusX}\n" \
              "{questionFormulaComment}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    # part1 / part2
    # = part12
    yCoeff = random.choice(oneDigitInts)

    maximum = 10
    while True :
        numeratorCoeffs = random.sample(oneDigitInts, k=2)
        denomCoeffs = random.sample(oneDigitInts, k=2)

        if not ((numeratorCoeffs != denomCoeffs) and (sum(map(abs, numeratorCoeffs)) <= maximum) and \
                (sum(map(abs, denomCoeffs)) <= maximum) and (denomCoeffs[0]*yCoeff + denomCoeffs[1]) and \
                (numeratorCoeffs[0]*yCoeff + numeratorCoeffs[1])) :
            continue

        numeratorSym = numeratorCoeffs[0] * x + numeratorCoeffs[1] * y
        denominatorSym = denomCoeffs[0] * x + denomCoeffs[1] * y

        numeratorText = convertIntoHangul(numeratorSym, timesToSpace=True)
        denomText = convertIntoHangul(denominatorSym, timesToSpace=True)

        givenFormulaLeft = joinList([lp, numeratorText, rp, "``:``", lp, denomText, rp])

        fracSym = numeratorSym / denominatorSym
        fracSymReplacedValue = fracSym.subs(x, yCoeff*y).cancel()

        fracSymValueNumerator = int(fracSymReplacedValue.p)
        fracSymValueDenominator = int(fracSymReplacedValue.q)

        givenFormulaRight = joinList([fracSymValueNumerator, "``:``", fracSymValueDenominator])
        givenFormula = joinList([givenFormulaLeft, eq, givenFormulaRight])

        if fracSymValueDenominator == 1 :
            leftPart = numeratorText
        elif fracSymValueDenominator == -1 :
            leftPart = joinList([ms, lp, numeratorText, rp])
        else :
            leftPart = joinList([fracSymValueDenominator, lp, numeratorText, rp])

        if fracSymValueNumerator == 1 :
            rightPart = denomText
        elif fracSymValueNumerator == -1 :
            rightPart = joinList([ms, lp, denomText, rp])
        else :
            rightPart = joinList([fracSymValueNumerator, lp, denomText, rp])

        givenFormulaComment1 = joinList([leftPart, eq, rightPart])

        leftPartSym = fracSymValueDenominator * numeratorSym
        rightPartSym = fracSymValueNumerator * denominatorSym

        if leftPartSym == rightPartSym :
            continue

        givenFormulaComment2 = joinList([leftPartSym, eq, rightPartSym])
        givenFormulaComment2 = convertIntoHangul(givenFormulaComment2, timesToSpace=True)

        xCalcCoeff = fracSymValueDenominator * numeratorCoeffs[0] - fracSymValueNumerator * denomCoeffs[0]
        yCalcCoeff = (fracSymValueDenominator * numeratorCoeffs[1] - fracSymValueNumerator * denomCoeffs[1]) * -1

        xForm = xCalcCoeff * x
        yForm = yCalcCoeff * y
        givenFormulaComment3 = joinList([xForm, eq, yForm])
        givenFormulaComment3 = convertIntoHangul(givenFormulaComment3)

        # print(leftPartSym, rightPartSym)
        xFormulaRight = solve(leftPartSym-rightPartSym, x)[0]
        xFormulaRightText = convertIntoHangul(xFormulaRight, minusWithSpace=True, timesToSpace=True)
        xFormula = joinList([x, eq, xFormulaRightText])
        thusX = joinList([thus, xFormula])

        break


    while True :
        numeratorCoeffs = random.sample(oneDigitInts, k=2)
        denomCoeffs = random.sample(oneDigitInts, k=2)

        if not ((numeratorCoeffs != denomCoeffs) and (sum(map(abs, numeratorCoeffs)) <= maximum) and \
                (sum(map(abs, denomCoeffs)) <= maximum) and (denomCoeffs[0]*yCoeff + denomCoeffs[1]) and \
                (numeratorCoeffs[0]*yCoeff + numeratorCoeffs[1])) :
            continue

        numeratorSym1 = numeratorCoeffs[0] * x
        numeratorSym2 = numeratorCoeffs[1] * y
        denominatorSym1 = denomCoeffs[0] * x
        denominatorSym2 = denomCoeffs[1] * y

        numeratorSym = numeratorSym1 + numeratorSym2
        denominatorSym = denominatorSym1 + denominatorSym2

        numeratorText = convertIntoHangul(numeratorSym, timesToSpace=True)
        denomText = convertIntoHangul(denominatorSym, timesToSpace=True)

        questionFormula = makeFractionFormula(numeratorText, denomText)

        yEq = yCoeff * y

        fracSym = numeratorSym / denominatorSym
        numeratorSym1Replaced = numeratorSym1.subs(x, yEq).cancel()
        denominatorSym1Replaced = denominatorSym1.subs(x, yEq).cancel()

        numeratorSymReplaced = connectEqations(numeratorSym1Replaced, numeratorSym2)
        denominatorSymReplaced = connectEqations(denominatorSym1Replaced, denominatorSym2)
        questionFormula1 = makeFractionFormula(numeratorSymReplaced, denominatorSymReplaced)
        questionFormula1 = convertIntoHangul(questionFormula1, timesToSpace=True, minusWithSpace=True)

        numeratorSymReplaced2 = numeratorSym.subs(x, yEq).cancel()
        denominatorSymReplaced2 = denominatorSym.subs(x, yEq).cancel()

        questionFormula2 = makeFractionFormula(numeratorSymReplaced2, denominatorSymReplaced2)
        questionFormula2 = convertIntoHangul(questionFormula2, timesToSpace=True, minusWithSpace=True)

        ansValueSym = numeratorSymReplaced2 / denominatorSymReplaced2
        ansValueSym = ansValueSym.cancel()

        ansValueText = convertIntoHangul(ansValueSym, minusWithSpace=True)

        questionFormulaComment = joinList([thus, questionFormula, eq, questionFormula1, eq, questionFormula2, eq, ansValueText])

        break

    ansInd, valueAdjusts = makeChoices(0, diff=1, withTag=False)
    realACoeffs = [x+ansValueSym for x in valueAdjusts]

    choices = []
    for i in range(5):
        tempFormText = convertIntoHangul(realACoeffs[i], minusWithSpace=True, timesToSpace=True)
        choices.append(aT(tempFormText))


    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1), givenFormulaComment2=aT(givenFormulaComment2),
                             givenFormulaComment3=aT(givenFormulaComment3), thusX=aT(thusX), questionFormulaComment=aT(questionFormulaComment))

    return stem, answer, comment


def rationalandprime211_Stem_128():
    stem = "{givenFormula}일 때, 다음 식의 값을 구하시오. (단, {constraint})\n\n" \
           "   {questionFormula}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}에서 {givenFormulaComment1}, {givenFormulaComment2}, {givenFormulaComment3}\n{thusQuestionFormula}\n" \
              "{questionFormulaComment1}\n{questionFormulaComment2}\n{questionFormulaComment3}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    a, b, c = symbols("a b c", real=True)
    X, Y, Z = symbols("X Y Z", real=True)

    coeffRange = [-2, -1, 1, 2]

    givenFormulaCoeffs = random.choices(coeffRange, k=3)
    denomCoeffs = random.choices(coeffRange, k=3)

    givenA = givenFormulaCoeffs[0] * a
    givenB = givenFormulaCoeffs[1] * b
    givenC = givenFormulaCoeffs[2] * c

    denomA = denomCoeffs[0] * a
    denomB = denomCoeffs[1] * b
    denomC = denomCoeffs[2] * c

    givenFormulaLeft = givenA + givenB + givenC
    givenFormula = joinList([givenFormulaLeft, eq, 0])
    givenFormula = convertIntoHangul(givenFormula)

    constraint = 'abc `!=` 0'

    givenBC = givenB + givenC
    givenAC = givenA + givenC
    givenAB = givenA + givenB

    givenAneg = -givenA
    givenBneg = -givenB
    givenCneg = -givenC

    givenBCtext = convertIntoHangul(givenBC, minusWithSpace=True)
    givenACtext = convertIntoHangul(givenAC, minusWithSpace=True)
    givenABtext = convertIntoHangul(givenAB, minusWithSpace=True)

    questionFormula = denomA/givenBC + denomB/givenAC + denomC/givenAB
    questionFormulaText = convertIntoHangul(questionFormula, minusWithSpace=True, parenToBracket=True)

    thusQuestionFormula = joinList([thus, questionFormulaText])

    givenAnegText = convertIntoHangul(givenAneg)
    givenBnegText = convertIntoHangul(givenBneg)
    givenCnegText = convertIntoHangul(givenCneg)

    givenFormulaParted = makeEquality([givenBCtext, givenACtext, givenABtext], [givenAnegText, givenBnegText, givenCnegText], withTag=True)

    questionFormulaCommentRight = questionFormulaText.replace(givenBCtext, givenAnegText)
    questionFormulaCommentRight = questionFormulaCommentRight.replace(givenACtext, givenBnegText)
    questionFormulaCommentRight = questionFormulaCommentRight.replace(givenABtext, givenCnegText)

    questionFormulaComment1 = joinList([eq, questionFormulaCommentRight])

    val1Sym = denomA / givenAneg
    val2Sym = denomB / givenBneg
    val3Sym = denomC / givenCneg
    valSyms = [val1Sym, val2Sym, val3Sym]

    valTexts = list(map(lambda x: convertIntoHangul(x, minusWithSpace=True), valSyms))

    questionFormulaComment2Right = connectEqations(connectEqations(valTexts[0], valTexts[1]), valTexts[2])
    questionFormulaComment2 = joinList([eq, questionFormulaComment2Right])

    ansValue = sum(valSyms)
    ansValueText = convertIntoHangul(ansValue, minusWithSpace=True)
    questionFormulaComment3 = joinList([eq, ansValueText])

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), constraint=aT(constraint), questionFormula=aT(questionFormulaText))
    answer = answer.format(a1=aT(ansValueText))
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaParted[0]), givenFormulaComment2=aT(givenFormulaParted[1]),
                             givenFormulaComment3=aT(givenFormulaParted[2]), thusQuestionFormula=aT(thusQuestionFormula),
                             questionFormulaComment1=aT(questionFormulaComment1), questionFormulaComment2=aT(questionFormulaComment2),
                             questionFormulaComment3=aT(questionFormulaComment3))

    return stem, answer, comment


def rationalandprime211_Stem_129():
    stem = "{givenFormula}일 때, {questionFormula}의 값은? (단, {constraint})\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}에서 {givenFormulaComment1}\n{thusQuestionFormula}\n" \
              "{questionFormulaComment1}\n{questionFormulaComment2}\n{questionFormulaComment3}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitInts = range(1, 10)

    maximum = 10
    while True :
        numeratorCoeffs = random.choices(oneDigitInts, k=2)
        denomCoeffs = random.choices(oneDigitInts, k=2)
        xyCoeffs = random.sample(oneDigitInts, k=2)

        if not ((numeratorCoeffs != denomCoeffs) and (sum(map(abs, numeratorCoeffs)) <= maximum) and \
                (sum(map(abs, denomCoeffs)) <= maximum) and (sum(map(abs, xyCoeffs)) <= maximum)):
            continue

        break

    numeratorSym1 = numeratorCoeffs[0] * x**2
    numeratorSym2 = numeratorCoeffs[1] * x * y
    numeratorSym = numeratorSym1 + numeratorSym2

    denominatorSym1 = denomCoeffs[0] * x**2
    denominatorSym2 = denomCoeffs[1] * x * y
    denominatorSym = denominatorSym1 + denominatorSym2

    numeratorText = convertIntoHangul(numeratorSym, timesToSpace=True)
    denomText = convertIntoHangul(denominatorSym, timesToSpace=True)

    questionFormula = joinList([lp, numeratorText, rp, dd, lp, denomText, rp])
    thusQuestionFormula = joinList([thus, questionFormula])

    xCoeff = xyCoeffs[0] / Integer(xyCoeffs[1])

    givenFormulaX = xyCoeffs[0] * x
    givenFormulaY = xyCoeffs[1] * y

    givenFormula = joinList([givenFormulaX, eq, givenFormulaY])
    givenFormula = convertIntoHangul(givenFormula)

    xCoeffMuled = xCoeff * x
    xCoeffMuledText = convertIntoHangul(getPolyText(xCoeffMuled), timesToSpace=True)

    givenFormulaComment1 = joinList([y, eq, xCoeffMuledText])

    yReplaceText = joinList([ts, xCoeffMuledText])

    questionFormulaComment1Right = questionFormula.replace("y", yReplaceText)
    questionFormulaComment1 = joinList([eq, questionFormulaComment1Right])

    numeratorSym2Replaced = numeratorCoeffs[1] * xCoeff * x ** 2
    denominatorSym2Replaced = denomCoeffs[1] * xCoeff * x ** 2

    questionFormulaComment2Right1 = connectEqations(numeratorSym1, getPolyText(numeratorSym2Replaced))
    questionFormulaComment2Right2 = connectEqations(denominatorSym1, getPolyText(denominatorSym2Replaced))

    questionFormulaComment2Right1Text = joinList([lp, convertIntoHangul(questionFormulaComment2Right1, timesToSpace=True), rp])
    questionFormulaComment2Right2Text = joinList([lp, convertIntoHangul(questionFormulaComment2Right2, timesToSpace=True), rp])
    questionFormulaComment2 = joinList([eq, questionFormulaComment2Right1Text, dd, questionFormulaComment2Right2Text])

    questionFormulaComment3Right1 = (numeratorSym1 + numeratorSym2Replaced).cancel()
    questionFormulaComment3Right2 = ( 1 / (denominatorSym1 + denominatorSym2Replaced) ).cancel()
    ansValue = (questionFormulaComment3Right1 * questionFormulaComment3Right2).cancel()

    questionFormulaComment3Right1Text = convertIntoHangul(getPolyText(questionFormulaComment3Right1), timesToSpace=True)
    questionFormulaComment3Right2Text = convertIntoHangul(questionFormulaComment3Right2, timesToSpace=True, parenToBracket=True)
    ansValueText = convertIntoHangul(ansValue)

    questionFormulaComment3 = joinList([eq, questionFormulaComment3Right1Text, ts, questionFormulaComment3Right2Text, eq, ansValueText])

    satisfied = False
    while not satisfied :
        ansInd, valueAdjusts = makeChoices(0, diff=1, withTag=False)
        realACoeffs = [x/Integer(2) + ansValue for x in valueAdjusts]
        satisfied = True
        for item in realACoeffs :
            if item < 0 :
                satisfied = False


    choices = []
    for i in range(5):
        tempFormText = convertIntoHangul(realACoeffs[i], minusWithSpace=True, timesToSpace=True)
        choices.append(aT(tempFormText))

    constraint = "x `!=` 0"

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), constraint=aT(constraint), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             thusQuestionFormula=aT(thusQuestionFormula),
                             questionFormulaComment1=aT(questionFormulaComment1),
                             questionFormulaComment2=aT(questionFormulaComment2),
                             questionFormulaComment3=aT(questionFormulaComment3))

    return stem, answer, comment


def rationalandprime211_Stem_130():
    stem = "0이 아닌 두 수 {x}, {y}에 대하여 {givenFormula}일 때,\n{questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}에서 {givenFormulaComment1}이므로 {givenFormulaComment2} ……㉠\n{thusQuestionFormula}\n{questionFormulaComment1}\n" \
              "{questionFormulaComment2} ({because} ㉠)\n{ansValueFormula}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y = symbols("x y", real=True)

    oneDigitLimited = list(range(-6, -1)) + list(range(2, 7))

    xCoeffs = random.sample(range(1, 9), k=2)
    yCoeffs = random.sample(oneDigitLimited, k=2)
    denomCoeff = random.choice(range(1, 5))

    givenK = random.choice(oneDigitLimited)

    #식 구성
    # {part1(part2) - part3(part4)} / part5
    # = (part12 + part34) / part5
    # = part1234 / part5 = part1234/part5subed
    # = part12345

    givenFormula = joinList(['1 over x', ps, '1 over y', eq, givenK])
    givenFormulaComment1 = joinList(['{x', ps, "y}", ov, 'xy', eq, givenK])
    givenFormulaComment2 = joinList(['x', ps, 'y', eq, givenK, 'xy'])

    formulaPart1 = xCoeffs[0] * x
    formulaPart2 = xCoeffs[1] * x + yCoeffs[0] * y
    formulaPart3 = xCoeffs[1] * x
    formulaPart4 = xCoeffs[0] * x + yCoeffs[1] * y
    formulaPart5 = denomCoeff * (x + y)

    formulaParts = [formulaPart1, formulaPart2, formulaPart3, formulaPart4, formulaPart5]
    formulaPartTexts = list(map(lambda x: convertIntoHangul(x, timesToSpace=True), formulaParts))

    questionFormulaNumerator = joinList([formulaPartTexts[0], lp, formulaPartTexts[1], rp, ms, formulaPartTexts[2], lp, formulaPartTexts[3], rp])
    questionFormula = makeFractionFormula(questionFormulaNumerator, formulaPartTexts[4])
    thusQuestionFormula = joinList([thus, questionFormula])

    formulaPart12 = (formulaPart1 * formulaPart2).cancel()
    formulaPart34 = (-formulaPart3 * formulaPart4).cancel()
    questionFormulaComment1 = joinList([eq, makeFractionFormula(joinList([formulaPart12, formulaPart34]), formulaPartTexts[4])])
    questionFormulaComment1 = convertIntoHangul(questionFormulaComment1, timesToSpace=True)

    formulaPart1234 = (formulaPart12 + formulaPart34).cancel()
    questionFormulaComment2Left = makeFractionFormula(formulaPart1234, formulaPart5.factor())

    questionFormulaComment2Right = makeFractionFormula(formulaPart1234, joinList([givenK * denomCoeff, 'xy']))

    questionFormulaComment2 = joinList([eq, questionFormulaComment2Left, eq, questionFormulaComment2Right])
    questionFormulaComment2 = convertIntoHangul(questionFormulaComment2, minusWithSpace=True, timesToSpace=True)

    because = aT('because')

    formulaPart12345 = (formulaPart1234 / (givenK*denomCoeff*x*y)).cancel()
    # print(formulaPart1234)
    questionFormulaComment3 = joinList([eq, formulaPart12345])
    questionFormulaComment3 = convertIntoHangul(questionFormulaComment3, minusWithSpace=True, timesToSpace=True)

    ansInd, _choices = makeChoices(0, diff=1, withTag=False)
    choices = list(map(lambda x: aT(convertIntoHangul(x, minusWithSpace=True)), [formulaPart12345 + Integer(x) for x in _choices]))

    # 내용을 채웁니다.
    stem = stem.format(x=aT('x'), y=aT('y'), givenFormula=aT(givenFormula), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), thusQuestionFormula=aT(thusQuestionFormula),
                             questionFormulaComment1=aT(questionFormulaComment1), questionFormulaComment2=aT(questionFormulaComment2),
                             because=because, ansValueFormula=aT(questionFormulaComment3))

    return stem, answer, comment


def rationalandprime211_Stem_131():
    stem = "{givenFormula}{postp} 만족시키는 두 자연수 {x}, {y}에 대하여 {questionFormula1}를 {x}의 식으로 나타내면 {ansForm}이다. " \
           "이 때 상수 {A}, {B}에 대하여 {questionFormula}의 값은?\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{givenFormula}에서\n{givenFormulaComment1}, {givenFormulaComment2}\n" \
              "즉, {givenFormulaComment3}이므로 {givenFormulaComment4}\n" \
              "{thusQuestionFormula1}\n{questionFormula1Comment1}\n{questionFormula1Comment2}\n{questionFormula1Comment3}" \
              "{questionFormula1Comment4}{questionFormula1Comment5}" \
              "따라서 {aFormula}, {bFormula}이므로 {ansFormula}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    x, y, A, B = symbols("x y A B", real=True)

    oneDigitInts = list(range(-9, 0)) + list(range(1, 10))

    numbers = random.choices(oneDigitInts, k=6)

    maximum = 10
    while True:
        questionFormula1LeftCoeffs = random.choices(oneDigitInts, k=2)
        questionFormula1RightCoeffs = random.choices(oneDigitInts, k=2)
        questionFormula1Coeffs = random.sample(range(1, 10), k=2)
        xCoeff = random.choice(range(2, 10))
        consCoeff = random.choice(range(10))
        xyCoeffs = [xCoeff, consCoeff]

        if not ((questionFormula1LeftCoeffs != questionFormula1RightCoeffs) and (sum(map(abs, questionFormula1Coeffs)) <= maximum) and \
                (sum(map(abs, questionFormula1LeftCoeffs)) <= maximum) and \
                (sum(map(abs, questionFormula1RightCoeffs)) <= maximum) and (sum(map(abs, xyCoeffs)) <= maximum) and \
                (questionFormula1LeftCoeffs[0]*questionFormula1Coeffs[0] != questionFormula1RightCoeffs[0]*questionFormula1Coeffs[1]) and \
                (questionFormula1LeftCoeffs[1]*questionFormula1Coeffs[0] != questionFormula1RightCoeffs[1]*questionFormula1Coeffs[1])):
            continue

        givenFormulaValueExp = random.choice(range(1, 7))

        givenFormulaXExp = xyCoeffs[0]
        givenFormulaConstExp = xyCoeffs[1] + givenFormulaValueExp
        base = 2
        part1 = exponentForm(exponentForm(2, 2, paren=False), x, baseParen=True, paren=False)
        part1ExpSym = xyCoeffs[0] * x
        part1ExpSymText = convertIntoHangul(part1ExpSym)
        part1Simplified = exponentForm(2, part1ExpSymText, paren=False)
        part2 = exponentForm(2, givenFormulaConstExp, paren=False)
        part3 = exponentForm(2, y, paren=False)
        resForm = exponentForm(2, givenFormulaValueExp, paren=False)
        resValue = 2 ** givenFormulaValueExp
        postp = proc_jo(resValue%10, 1)

        givenFormula = joinList([part1, ts, part2, dd, part3, eq, resValue])
        givenFormulaComment1 = joinList([part1Simplified, ts, part2, dd, part3, eq, resForm])

        expConnected = connectEqations(connectEqations(part1ExpSymText, givenFormulaConstExp), "-y")
        givenFormulaComment2Left = exponentForm(2, expConnected, paren=False)
        givenFormulaComment2 = joinList([givenFormulaComment2Left, eq, resForm])

        givenFormulaYSym = part1ExpSym + xyCoeffs[1]
        givenFormulaYSymText = convertIntoHangul(givenFormulaYSym)

        givenFormulaComment3 = joinList([expConnected, eq, givenFormulaValueExp])
        givenFormulaComment4 = joinList([y, eq, givenFormulaYSymText])

        questionFormula1Left = questionFormula1LeftCoeffs[0] * x + questionFormula1LeftCoeffs[1] * y
        questionFormula1Right = questionFormula1RightCoeffs[0] * x + questionFormula1RightCoeffs[1] * y

        questionFormula1LeftText = convertIntoHangul(questionFormula1Left, timesToSpace=True)
        questionFormula1RightText = convertIntoHangul(questionFormula1Right, timesToSpace=True)

        questionFormulaStruct = questionFormula1Coeffs[0] * A - questionFormula1Coeffs[1] * B

        questionFormulaStructText = convertIntoHangul(questionFormulaStruct)

        questionFormula1 = questionFormulaStructText.replace("A", joinList([lp, questionFormula1LeftText, rp]))
        questionFormula1 = questionFormula1.replace("B", joinList([lp, questionFormula1RightText, rp]))

        thusQuestionFormula1 = joinList([thus, questionFormula1])

        questionFormula1LeftMuled = questionFormula1Coeffs[0] * questionFormula1Left
        questionFormula1RightMuled = questionFormula1Coeffs[1] * questionFormula1Right * -1

        questionFormula1Comment1Right = connectEqations(questionFormula1LeftMuled, questionFormula1RightMuled)
        questionFormula1Comment1Right = convertIntoHangul(questionFormula1Comment1Right)
        questionFormula1Comment1 = joinList([eq, questionFormula1Comment1Right])

        questionFormula1Simplified = questionFormula1LeftMuled + questionFormula1RightMuled
        questionFormula1Simplified = questionFormula1Simplified.cancel()
        questionFormula1SimplifiedText = convertIntoHangul(questionFormula1Simplified)

        questionFormula1Comment2 = joinList([eq, questionFormula1SimplifiedText])

        questionFormula1SimplifiedCoeffs = questionFormula1Simplified.as_coefficients_dict()
        yCoeff = int(questionFormula1SimplifiedCoeffs[y])
        # xCoeff = int(questionFormula1SimplifiedCoeffs[x])

        xPart = questionFormula1Simplified - yCoeff * y
        xPartText = convertIntoHangul(xPart)

        questionFormula1Comment3 = aT(questionFormula1Comment2.replace("y", joinList([lp, givenFormulaYSymText, rp])))
        questionFormula1Comment3 += "\n"

        questionFormula1Comment4RightSym = givenFormulaYSym * yCoeff
        questionFormula1Comment4RightText = convertIntoHangul(questionFormula1Comment4RightSym)

        questionFormula1Comment4 = aT(connectEqations(joinList([eq, xPartText]), questionFormula1Comment4RightText))
        questionFormula1Comment4 += "\n"

        questionFormula1FinalSym = xPart + questionFormula1Comment4RightSym
        questionFormula1FinalSym = questionFormula1FinalSym.cancel()

        questionFormula1FinalSymCoeffs = questionFormula1FinalSym.as_coefficients_dict()

        if not questionFormula1FinalSymCoeffs[x] :
            questionFormula1FinalSymText = questionFormula1FinalSym
            AVal = 0
            BVal = questionFormula1FinalSym
        else :
            AVal = questionFormula1FinalSymCoeffs[x]
            BVal = questionFormula1FinalSymCoeffs[1]
            questionFormula1FinalSymText = convertIntoHangul(getPolyText(questionFormula1FinalSym))

        questionFormula1Comment5 = aT(joinList([eq, questionFormula1FinalSymText])) + "\n"

        break

    values = [AVal, BVal]

    ValueFormulas = makeEquality(["A", "B"], values, withTag=True)

    questionFormulaDict = getRandomEquation(["A", "B"], [(-1, 2), (-1, 2)], values, avoidZero=True)
    questionFormula = questionFormulaDict['text']
    questionFormulaCoeff = questionFormulaDict['coeffs']
    ansValue = questionFormulaDict['ansValue']

    ansValueEq = getNumberCalc([questionFormulaCoeff[i]*values[i] for i in range(len(values))], withRes=True)
    ansFormula = joinList([questionFormula, eq, ansValueEq])

    ansInd, choices = makeChoices(ansValue, diff=2, withTag=True)

    ansForm = "Ax + B"

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), postp=postp, x=aT(x), y=aT(y), questionFormula1=aT(questionFormula1),
                       ansForm=aT(ansForm), A=aT(A), B=aT(B), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(givenFormula=aT(givenFormula), givenFormulaComment1=aT(givenFormulaComment1),
                             givenFormulaComment2=aT(givenFormulaComment2), givenFormulaComment3=aT(givenFormulaComment3),
                             givenFormulaComment4=aT(givenFormulaComment4), thusQuestionFormula1=aT(thusQuestionFormula1),
                             questionFormula1Comment1=aT(questionFormula1Comment1), questionFormula1Comment2=aT(questionFormula1Comment2),
                             questionFormula1Comment3=questionFormula1Comment3, questionFormula1Comment4=questionFormula1Comment4,
                             questionFormula1Comment5=questionFormula1Comment5, aFormula=ValueFormulas[0], bFormula=ValueFormulas[1],
                             ansFormula=aT(ansFormula))

    return stem, answer, comment


def rationalandprime211_Stem_132():
    stem = "{givenFormula}일 때,\n{questionFormula}의 값은? (단, {constraint})\n" \
           "① {s1}      ② {s2}      ③ {s3}      ④ {s4}      ⑤ {s5}\n"
    answer = "(답): {a1}\n"
    comment = "(해설)\n{questionFormula}\n" \
              "{questionFormulaComment1}\n{questionFormulaComment2}\n{questionFormulaComment3}\n" \
              "{questionFormulaComment4}\n{questionFormulaComment5}\n\n"

    # 문제를 만들기 위해 필요한 여러 변수들을 정합니다.
    a, b, c = symbols("a b c", real=True)
    X, Y, Z = symbols("X Y Z", real=True)

    coeffRange = [-2, -1, 1, 2]

    givenFormulaCoeffs = random.choices(coeffRange, k=3)
    denomCoeffs = random.choices(coeffRange, k=3)

    givenA = givenFormulaCoeffs[0] * a
    givenB = givenFormulaCoeffs[1] * b
    givenC = givenFormulaCoeffs[2] * c

    givenAText = convertIntoHangul(givenA)
    givenBText = convertIntoHangul(givenB)
    givenCText = convertIntoHangul(givenC)

    denomA = denomCoeffs[0] * a
    denomB = denomCoeffs[1] * b
    denomC = denomCoeffs[2] * c

    denomAText = convertIntoHangul(denomA)
    denomBText = convertIntoHangul(denomB)
    denomCText = convertIntoHangul(denomC)

    givenFormulaLeft = givenA + givenB + givenC
    givenFormula = joinList([givenFormulaLeft, eq, 0])
    givenFormula = convertIntoHangul(givenFormula)

    constraint = 'abc `!=` 0'

    givenBC = givenB + givenC
    givenAC = givenA + givenC
    givenAB = givenA + givenB

    givenAneg = -givenA
    givenBneg = -givenB
    givenCneg = -givenC

    givenBCtext = convertIntoHangul(givenBC, minusWithSpace=True)
    givenACtext = convertIntoHangul(givenAC, minusWithSpace=True)
    givenABtext = convertIntoHangul(givenAB, minusWithSpace=True)

    denomAFrac = makeFractionFormula(1, denomAText)
    denomBFrac = makeFractionFormula(1, denomBText)
    denomCFrac = makeFractionFormula(1, denomCText)

    questionFormula = connectEqations(joinList([givenAText, lp, denomBFrac, ps, denomCFrac, rp]),
                                      connectEqations(joinList([givenBText, lp, denomCFrac, ps, denomAFrac, rp]),
                                                      joinList([givenCText, lp, denomAFrac, ps, denomBFrac, rp])))

    abFrac = makeFractionFormula(givenAText, denomBText)
    acFrac = makeFractionFormula(givenAText, denomCText)
    bcFrac = makeFractionFormula(givenBText, denomCText)
    baFrac = makeFractionFormula(givenBText, denomAText)
    caFrac = makeFractionFormula(givenCText, denomAText)
    cbFrac = makeFractionFormula(givenCText, denomBText)

    questionFormulaComment1 = joinList([eq, abFrac, ps, acFrac, ps, bcFrac, ps, baFrac, ps, caFrac, ps, cbFrac])
    questionFormulaComment2 = joinList([eq, lp, acFrac, ps, bcFrac, rp, ps, lp, abFrac, ps, cbFrac, rp, ps, lp, baFrac, ps, caFrac, rp])

    questionFormulaComment3Sym = givenBC/denomA + givenAC/denomB + givenAB/denomC
    questionFormulaComment3SymText = convertIntoHangul(questionFormulaComment3Sym, minusWithSpace=True, parenToBracket=True)
    questionFormulaComment3 = joinList([eq, questionFormulaComment3SymText])

    givenAnegText = convertIntoHangul(givenAneg)
    givenBnegText = convertIntoHangul(givenBneg)
    givenCnegText = convertIntoHangul(givenCneg)

    questionFormulaComment4Right = questionFormulaComment3SymText.replace(givenBCtext, givenAnegText)
    questionFormulaComment4Right = questionFormulaComment4Right.replace(givenACtext, givenBnegText)
    questionFormulaComment4Right = questionFormulaComment4Right.replace(givenABtext, givenCnegText)

    questionFormulaComment4 = joinList([eq, questionFormulaComment4Right])

    val1Sym = givenAneg / denomA
    val2Sym = givenBneg / denomB
    val3Sym = givenCneg / denomC
    valSyms = [val3Sym, val2Sym, val1Sym]

    valTexts = list(map(lambda x: convertIntoHangul(x, minusWithSpace=True), valSyms))

    ansValue = sum(valSyms)
    ansValueText = convertIntoHangul(ansValue, minusWithSpace=True)

    questionFormulaComment5Right = connectEqations(connectEqations(valTexts[0], valTexts[1]), valTexts[2])
    questionFormulaComment5 = joinList([eq, questionFormulaComment5Right, eq, ansValueText])

    ansInd, valueAdjusts = makeChoices(0, diff=1, withTag=False)
    realACoeffs = [x + ansValue for x in valueAdjusts]

    choices = []
    for i in range(5):
        tempFormText = convertIntoHangul(realACoeffs[i], minusWithSpace=True, timesToSpace=True)
        choices.append(aT(tempFormText))

    # 내용을 채웁니다.
    stem = stem.format(givenFormula=aT(givenFormula), constraint=aT(constraint), questionFormula=aT(questionFormula),
                       s1=choices[0], s2=choices[1], s3=choices[2], s4=choices[3], s5=choices[4])
    answer = answer.format(a1=answer_dict[ansInd])
    comment = comment.format(questionFormula=aT(questionFormula),
                             questionFormulaComment1=aT(questionFormulaComment1), questionFormulaComment2=aT(questionFormulaComment2),
                             questionFormulaComment3=aT(questionFormulaComment3), questionFormulaComment4=aT(questionFormulaComment4),
                             questionFormulaComment5=aT(questionFormulaComment5))

    return stem, answer, comment



