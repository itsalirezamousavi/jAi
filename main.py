from dependencies.chatgpt import suggestion                                                         # our own libs
from dependencies.wiki import cityInfo
from dependencies.openweather import upcomingWeather
from dependencies.unsplash import image

from flask import Flask, request                                                                    # import libs
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)                                                                               # creating the app
api = Api(app)

class Main(Resource):                                                                               # our main class
    
    def getFunc(self, weather, biom, budget):

        # weather --> cold ,hot ,rainy ,mild climate
        # biom    --> jungle ,beach ,mountain ,desert ,vibrant city
        # budget  --> high ,medium ,low

        suggestedCities = suggestion(weather, biom, budget)                                         # getting a list of suggestion from ChatGPT
        if suggestedCities == None:                                                                 # error handeling
            return None

        mainDic = {}
        counter = 0

        for row in suggestedCities:                                                                 # getting data for each suggestion
            en = str(suggestedCities[row][0])
            city = en.split('/')[1]
            country = en.split('/')[0]

            fa = str(suggestedCities[row][1])
            faCity = fa.split('/')[1]
            faCountry = fa.split('/')[0]

            name = {'en':
                        {'country':country,
                        'city':city},
                    'fa':
                        {'country':faCountry,
                        'city':faCity}}

            package = {}
            package.update({'name' : name})
            package.update({'info' : cityInfo(city)})                                               # information from wikipedia
            package.update({'weather' : upcomingWeather(city)})                                     # weather from openweatherapi
            package.update({'images' : image(city)})                                                # image from unsplash
            mainDic.update({str(counter) : package})
            counter += 1
            del package

        return json.dumps(mainDic)


    def get(self):                                                                                  # get mwthod

        weather = request.args.get('weather')
        biom = request.args.get('biom')
        budget = request.args.get('budget')

        return self.getFunc(weather, biom, budget)



api.add_resource(Main, '/')                                                                         # adding main to our resources

if __name__ == "__main__":                                                                          # running the app
	app.run(debug=True)