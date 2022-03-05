# re 호출하여 split 소환
# pandas에서 to_csv() 소환
# json에서 json 소환
import re
import pandas as pd
import json

# csv파일 불러오기
df1 = open('YSY_v2.txt', 'r', encoding='UTF8')
df_comment = df1.readline()

# 불러온 df_comment 문자열로 변환 
comment_string = str(df_comment)

## df_comment에 'ㅋ'과 'ㅠ'와 '기타 조사' 제거하기
characters = "ㅋㅠ은는이가으로을를와의에께서에서에서에게"

## 1번 방법(replace 사용)
for x in range(len(characters)):
    comment_string = comment_string.replace(characters[x],"")
## 2번 방법(join 사용)
# comment_string = ''.join( x for x in comment_string if x not in characters)
## 3번 방법(sub 사용)
# comment_string = re.sub("\ㅋ|\ㅠ|\은|\는|\이|\가|\으로|\을|\를|\와|\의|\에|\께서|\에서|\에게|\대표", "", comment_string)

# ',' 기준으로 keyword 구분하기
df2 = open('YSY_keyword.txt', 'r', encoding='UTF8')
df_keyword = df2.readline()

# 불러온 df_keyword = 문자열로 변환
keyword_string = str(df_keyword)
kywrd_str_split = re.split('\,', keyword_string)

# keyword랑 같으면 +1, 없으면 카운팅하지 않기(LSM_tfidf.csv 참고)
comment_KeyValue = {}
for i in kywrd_str_split:
    if i in comment_string:
        comment_KeyValue[i] = comment_string.count(i)

# csv 파일로 저장 (안되는 이유, csv는 2차원으로 저장하려면 어려움, json이 쉬움)
# dataframe = pd.DataFrame(comment_KeyValue, index=[0])
# dataframe.to_csv("C:/Users/skate/Desktop/pythonworkspace", header=False, index=False)

# json 파일로 저장
file_path = 'YSY_result.json'
with open(file_path, 'w') as f:
    json.dump(comment_KeyValue, f)
