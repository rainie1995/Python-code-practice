from sklearn.feature_extraction.text import TfidfVectorizer
import jieba
tf = TfidfVectorizer(max_df = 0.5)
documents = [
    'this is the bayes document',
    'this is the second second document',
    'and the third one',
    'is this the document'
]
print(len(documents))
tf_matrix = tf.fit_transform(documents)
# print('不重复的词:', tf.get_feature_names())
print(tf.vocabulary_)
# print('每个单词的 tfidf 值:', tf_matrix.toarray())
