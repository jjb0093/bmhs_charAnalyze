cho_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
jong_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jaum_result = []
moum_result = []

for i in range(len(cho_list)):
    jaum_result.append(0)

for i in range(len(jung_list)):
    moum_result.append(0)

def koreanDevide(word):
    w_list = []
    for w in list(word.replace("\n","").strip()):
        if '가'<=w<='힣':
            cho = (ord(w) - ord('가')) // 588
            jung = (ord(w) - ord('가')) // 28 % 21
            jong = (ord(w) - ord('가')) % 28
            print(cho_list[cho], jung_list[jung], jong_list[jong])
        jaum_result[cho] += 1
        moum_result[jung] += 1
        for i in range(len(cho_list)):
            if(jong_list[jong] == cho_list[i]): jaum_result[i] += 1

while True:
    print("\n-------------------\n")
    var = input("입력 : ")
    if(var == "finish"):
        break
    else:
        koreanDevide(var)

for i in range(len(cho_list)):
    print(cho_list[i], jaum_result[i])

for i in range(len(jung_list)):
    print(jung_list[i], moum_result[i])

