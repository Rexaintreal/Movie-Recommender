#This is a python program which recommends movies based on types eg.Sad

#Importing 

from bs4 import BeautifulSoup as soup
import re
import requests as http

#main function 

def main(emotion):
    #we will use IMDB url to get the movies 
    if(emotion == "Sad"):
        url= 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Disgust"):
        url= 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Anger"):
        url= 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Anticipation"):
        url='http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Fear"):
        url= 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Enjoyment"):
        url= 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Trust"):
        url= 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Surprise"):
        url= 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
    
    #http requests to get the data
    response = http.get(url)
    data = response.text

    #Parsing the data
    Soup=soup(data, "lxml")

    #extracting movie titles using regex
    title = Soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
    return title

if __name__ == '__main__':
    emotion = input("Enter the emotion: ")
    a = main(emotion)
    count = 0
    if(emotion == "Disgust" or emotion == "Anger"
                           or emotion=="Surprise"):
  
        for i in a:
  
            # Splitting each line of the
            # IMDb data to scrape movies
            tmp = str(i).split('>;')
  
            if(len(tmp) == 3):
                print(tmp[1][:-3])
  
            if(count > 13):
                break
            count += 1
    else:
        for i in a:
            tmp = str(i).split('>')
  
            if(len(tmp) == 3):
                print(tmp[1][:-3])
  
            if(count > 11):
                break
            count+=1
