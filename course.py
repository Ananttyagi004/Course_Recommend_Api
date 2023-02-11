import pandas as pd
import numpy as np
data=pd.read_csv("udemy_courses.csv")
selected_features=['course_title','is_paid','price','level','content_duration','subject']
combined_features=data['course_title']+' '+data['is_paid']+' '+data['price']+' '+data['level']+' '+data['content_duration']+' '+data['subject']
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer()
feature_vector=vectorizer.fit_transform(combined_features)
from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(feature_vector)
import difflib
cou=[]
urla=[]
def recomended_course(title):
    course_name=title
    course=[]
    ulr=[]
    #Creating the list of movies in the dataset
    list_course=data['course_title'].tolist()
    #finding the close match for the movie name given by the user.
    find_close_match=difflib.get_close_matches(course_name,list_course) 
    close_match=find_close_match[0]
    title_index=data[data.course_title==close_match]['course_id'].values[0]
    #getting a  list of similar movies
    similarity_score=list(enumerate(similarity[title_index]))
    sorted_similar_movies=sorted(similarity_score, key=lambda x:x[1], reverse=True)
    i=1
    
    for movie in sorted_similar_movies:
        course_id=movie[0]
        title_from_index=data[data.index==course_id]['course_title'].values[0]
        url_from_index=data[data.index==course_id]['url'].values[0]
        if(i<10):
            #print(i,' .',title_from_index)
            course.append(title_from_index)
            ulr.append(url_from_index)
            i+=1
    cou=course
    urla=ulr
    return cou,urla

# print(recomended_course('Ultimate Investment Banking Course'))