# re 호출하여 split 소환
# pandas에서 to_csv() 소환
import re
import pandas as pd

# csv파일 불러오기
df1 = open('ACS_v2.txt', 'r', encoding='UTF8')
df_comment = df1.readline()

# 불러온 df_comment 문자열로 변환 
comment_string = str(df_comment)

# ',' 기준으로 keyword 구분하기
df2 = open('ACS_keyword.txt', 'r', encoding='UTF8')
df_keyword = df2.readline()

# 불러온 df_keyword = 문자열로 변환
keyword_string = str(df_keyword)
kywrd_str_split = re.split('\,', keyword_string)

# keyword랑 같으면 +1, 없으면 카운팅하지 않기(LSM_tfidf.csv 참고)
comment_KeyValue = {}
for i in kywrd_str_split:
    if i in comment_string:
        comment_KeyValue[i] = comment_string.count(i)

# csv 파일로 저장
dataframe = pd.DataFrame(comment_KeyValue, index=[0])
dataframe.to_csv("C:/Users/82105/Desktop/PythonWorkSpace/President2022", header=False, index=False)
