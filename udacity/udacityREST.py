from flask import Flask, jsonify
import json
from flask_restplus import Resource, Api

app = Flask(__name__)                  
api = Api(app, version='v0', title='Udacity Unoffial REST-API',
    description='Official API of Udacity converted to REST-API',
)
ns = api.namespace('UdacityAPI', description='Methods available')

data = json.loads(open('courses_udacity.json').read())

@ns.route('/')                  
class ShowAll(Resource):   
    @ns.doc('show_all')         
    def get(self):    
        '''List all Courses, Tracks, Degrees'''                 
        return jsonify(data)

@ns.route('/<string:data_type>')
@ns.param("data_type","Valid queries - courses, tracks or degrees")                   
class ShowData(Resource):  
    @ns.doc('course_track_degrees')             
    def get(self,data_type):  
        '''Display either courses, tracks or degrees'''                   
        return jsonify(data[data_type])


@ns.route('/<string:data_type>/<int:index>')         
@ns.param("data_type","Valid queries - courses, tracks or degrees")       
@ns.param("index"," Enter the course no., track no. or degree no")           
class ShowDataDetail(Resource):   
    @ns.doc('course_track_degrees_detail')  
    def get(self,data_type,index):           
        '''Display the details of either one course , one track or one degree.'''                   
        return jsonify(data[data_type][index])


@ns.route('/<string:data_type>/<int:index>/<string:subfield>')    
@ns.param("data_type","Valid queries - courses, tracks or degrees")          
@ns.param("index"," Enter the course no., track no. or degree no")      
@ns.param("subfield"," Enter the subfield to filter out course, track or degree.")               
class ShowDataDetailSubfield(Resource):   
    @ns.doc('detail_subfield')                  
    def get(self,data_type,index,subfield):          
        '''Filter out details from courses, details or tracks using subquery.'''                      
        return jsonify(data[data_type][index][subfield])

if __name__ == '__main__':
    app.run(debug=True)                