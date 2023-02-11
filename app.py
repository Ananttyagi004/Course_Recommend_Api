# Loading the dependencies
from flask import Flask,request,jsonify
from flask_cors import CORS
import course
app = Flask(__name__)
CORS(app)  

@app.route('/recomend', methods=['GET'])
def recommend_movies():
    res,mes=course.recomended_course(request.args.get('title'))
    
    columns=[{'course0':res[0], 'link0':mes[0]},{'course1':res[1], 'link1':mes[1]},{'course2':res[2], 'link2':mes[2]},{'course3':res[3], 'link3':mes[3]},
    {'course4':res[4], 'link4':mes[4]}]

    return jsonify(columns)

if __name__=='__main__':
     app.run(port = 5000, debug = True)