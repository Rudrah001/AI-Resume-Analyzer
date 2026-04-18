from sentence_transformers import SentenceTransformer, util
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tfidf_similarity(text1,text2):

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1,text2])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    score = similarity[0][0]*100

    return round(score,2)

model = SentenceTransformer('all-MiniLM-L6-v2')

def sbert_similarity(text1,text2):
    
    resume_emb = model.encode([text1])
    jd_emb = model.encode([text2])

    sbert_score = cosine_similarity(resume_emb,jd_emb)[0][0]*100

    return round(sbert_score,2)