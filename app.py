# Loading the dependencies
from flask import Flask,request,jsonify
from flask_cors import CORS
import course
app = Flask(__name__)
CORS(app)  

@app.route('/recomend', methods=['GET'])
def recommend_movies():
    res,mes=course.recomended_course(request.args.get('title'))
    
    columns=[{'course':res[0], 'link':mes[0]},{'course':res[1], 'link':mes[1]},{'course':res[2], 'link':mes[2]},{'course':res[3], 'link':mes[3]},
    {'course':res[4], 'link':mes[4]}]

    return jsonify(columns)

# if __name__=='__main__':
#      app.run(port = 5000, debug = True)