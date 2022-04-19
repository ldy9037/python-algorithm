txt = '''신경발달장애 Neurodevelopmental Disorders
조현병 스펙트럼 및 기타 정신병적 장애 Schizophrenia Spectrum and Other Psychotic Disorders
양극성 및 관련 장애 Bipolar and Related Disorders
우울장애 Depressive Disorders
불안장애 Anxiety Disorder
강박 및 관련 장애 Obsessive－Compulsive and Related Disorders
외상 및 스트레스 관련 장애 Trauma－and Stressor－Related Disorders
해리장애 Dissociative Disorders
신체증상 및 관련 장애 Somatic Symptom and Related Disorders
급식 및 섭식장애 Feeding and Eating Disorders
배설장애 Elimination Disorders
수면－각성 장애 Sleep－Wake Disorders
성기능부전 Sexual Dysfunctions
성별 불쾌감 Gender Dysphoria
파괴적, 충동조절 및 품행 장애 Disruptive, Impulse－Control, and Conduct Disorders
물질관련 및 중독 장애 Substance－Related and Addictive Disorders
신경인지장애 Neurocognitive Disorders
성격장애 Personality Disorders
변태성욕장애 Paraphilic Disorders
기타 정신질환 Other Mental Disorders'''

result = {}

def isEnglish(character):
    ascii = ord(character.upper())
    return ascii >= 65 and ascii <= 90

"""
def classifyWord(sentence):
    koreanWordArr = []
    EnglishWordArr = []

    for word in sentence.split():
        if isEnglish(word[0]): 
            EnglishWordArr.append(word)
        else: 
            koreanWordArr.append(word)

    result[' '.join(koreanWordArr)] = ' '.join(EnglishWordArr)

for sentence in txt.split('\n'):
    classifyWord(sentence)

"""
for sentence in txt.split('\n'):
    i = 0
    while not isEnglish(sentence[i]): i += 1
    else:
        result[sentence[:i -1]] = sentence[i:]
    
print(result)
    

    
    