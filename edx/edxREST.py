from flask import Flask, jsonify
import json
from flask_restplus import Resource, Api
import csv
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)                  
api = Api(app, version='v0', title='EDX Unoffial REST-API',
    description='Conversting RSS Feed of EDX to REST API.',
)
ns = api.namespace('EDX_API', description='Methods available')

def loadRSS():
 
    # url of rss feed
    url = 'https://www.edx.org/api/v2/report/course-feed/rss'
 
    # creating HTTP response object from given url
    resp = requests.get(url)
 
    # saving the xml file
    with open('edxcatalog.xml', 'wb') as f:
        f.write(resp.content)
         
 
def parseXML(xmlfile):
 
    # create element tree object
    tree = ET.parse(xmlfile)
 
    # get root element
    root = tree.getroot()
 
    # create empty list for news items
    courseitems = []
 
    data = root.findall('./channel/item')
    
    # iterate news items
    for item in root.findall('./channel/item'):
 
        # empty news dictionary
        courses = {}
 
        # iterate child elements of item
        for child in item: 
            # special checking for namespace object content:media
            if child.tag == '{https://www.edx.org/api/course/elements/1.0/}code':
                courses["code"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}created':
                courses["created"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}effort':
                courses["effort"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}end':
                courses["end"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}highschool':
                courses["highschool"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}id':
                courses["id"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}image-banner':
                courses["image-banner"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}image-thumbnail':
                courses["image-thumbnail"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}length':
                courses["length"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}prerequisites':
                courses["prerequisites"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}profed':
                courses["profed"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}self_paced':
                courses["self_paced"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}school':
                courses["school"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}start':
                courses["start"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}subject':
                courses["subject"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}subtitle':
                courses["subtitle"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}verified':
                courses["verified"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}xseries':
                courses["xseries"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}video-file':
                courses["video-file"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}video-youtube':
                courses["video-youtube"] = child.text
            elif child.tag == '{https://www.edx.org/api/course/elements/1.0/}instructors':
                for grandchild in child.findall('./{https://www.edx.org/api/course/elements/1.0/}staff/{https://www.edx.org/api/staff/elements/1.0/}name'):
                    courses["instructors"] = grandchild.text
            else:
                courses[child.tag] = child.text
 
        # append news dictionary to news items list
        courseitems.append(courses)
     
    return courseitems


loadRSS()
data = parseXML('edxcatalog.xml')

@ns.route('/')                  
class ShowAll(Resource):   
    @ns.doc('show_all')         
    def get(self):    
        '''Show all courses'''                 
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)                