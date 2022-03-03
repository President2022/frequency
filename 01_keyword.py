# 첫 번재 row에 있는 댓글(LSM.csv 참고)
comment = "링크  :안철수 "尹 개념 없어"‥'유사시 일본 들어올수도' 尹 발언 비판 (naver.com)그려 우리가 니 밭도 갈아주고 있는데"

# comment 문자열 나누기(띄어쓰기 기준)

# split을 사용해보니, 띄어쓰기뿐 아니라 '('로도 나눠야됨 (추후 반영 예정)

# keyword랑 같으면 +1, 없으면 카운팅하지 않기(LSM_tfidf.csv 참고)
comment_KeyValue = {}
if '개념' in comment:
    comment_KeyValue['개념'] = comment.count('개념')

print(comment_KeyValue)