import requests
from bs4 import BeautifulSoup
import csv
# import pandas as pd
from itertools import zip_longest

url= requests.get("https://elcinema.com/en/now/ae/")


#headers={
   # 'user-agent': "Mozilla/5.0 (x11; windows x86_64) AppleWebkit/537.36 (KHTML, like Gecko) chrom/95.0.4638.69 (Official Build) (64-bit) safari/537.36"
  #  }


nameList=[]
genreList=[]
ratingList=[]
dateList=[]

src= url.content
data = BeautifulSoup (src, 'lxml')



film_name = data.select('.columns h3 a')
film_name = film_name[1:]
film_genre = data.select(' .list-title:has(li:has(a))')
film_date = data.select(' .list-title strong + a')
stars_rating = data.select(' .stars-rating-lg span.legend' )



for i in range(len(film_name)):
    
    nameList.append(film_name[i].text)

    genre = film_genre[i].text
    genre = genre.replace("Genre:", '').replace('\n','')
    genre = genre.split(' ')
    genreList.append(genre[:-1])

    rate = stars_rating[i].text
    ratingList.append(rate)
    date = film_date[i].text
    dateList.append(date)


    
file_list=[nameList,genreList,ratingList,dateList,]    
exported = zip_longest(* file_list)

with open ("elcinema_data.csv","w") as myfile :
    ed= csv.writer(myfile)
    ed.writerow(["film name","film genre","stars rating","film date"])
    ed.writerows(exported)



