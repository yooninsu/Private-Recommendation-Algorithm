import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

documents = {
    "안심카츠는 부드럽고 담백한 맛 등심카츠는 살짝쿵 기름진 고소한 맛 치즈 카츠는 가득 들어간 치즈의 고소한 맛에 맛있게 먹구 왔습니다.",
    "치즈 블랙카츠 진짜 맛있어요",
    "진짜 음식도 너무 맛있고 사장님 멋있고 친절하세요.}",
}
vectorizer = CountVectorizer()
dtm = vectorizer.fit_transform(documents)
tf = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())
print(tf)
df = tf.astype(bool).sum(axis=0)
print(df)
# 문서 개수
D = len(tf)

# Inverse Document Frequency
idf = np.log((D) / (df + 1))
# TF-IDF
tfidf = tf * idf
tfidf = tfidf / np.linalg.norm(tfidf, axis=1, keepdims=True)
print(tfidf)
