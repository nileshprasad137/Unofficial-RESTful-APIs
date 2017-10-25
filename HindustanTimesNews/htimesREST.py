from flask import Flask, jsonify
import json
from flask_restplus import Resource, Api
import csv
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)                  
api = Api(app, version='v0', title='Hindustan Unoffial REST-API',
    description='Conversting RSS Feed of Hindustan Times to REST API.',
)
ns = api.namespace('HindustanTimesAPI', description='Methods available')

def loadRSS():
 
    # url of rss feed
    url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
 
    # creating HTTP response object from given url
    resp = requests.get(url)
 
    # saving the xml file
    with open('topnewsfeed.xml', 'wb') as f:
        f.write(resp.content)
         
 
def parseXML(xmlfile):
 
    # create element tree object
    tree = ET.parse(xmlfile)
 
    # get root element
    root = tree.getroot()
 
    # create empty list for news items
    newsitems = []
 
    data = root.findall('./channel/item')
    
    # iterate news items
    for item in root.findall('./channel/item'):
 
        # empty news dictionary
        news = {}
 
        # iterate child elements of item
        for child in item: 
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news["media"] = child.attrib['url']
            else:
                news[child.tag] = child.text
 
        # append news dictionary to news items list
        newsitems.append(news)
     
    return newsitems


loadRSS()
data = parseXML('topnewsfeed.xml')

@ns.route('/')                  
class ShowAll(Resource):   
    @ns.doc('show_recent')         
    def get(self):    
        '''Show all recent news'''                 
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)                