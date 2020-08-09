We have to scrapp data from https://news.ycombinator.com and then store the result of(Title,Image,URL) in mongoDb.While storing the data in mongoDb we have to maintain two relations.
1.URL and title of blog.
2.URL and its metadata like title,votes etc.

Language -Python
Library used for scrapping - Beautiful Soup
IDE used -Jupyter notebook
DB used -MongoDB Cloud

Intallations required:-
1.Python 3.8.5
2.jupyter notebook (Path- C:\Users\Jyoti Kumari\AppData\Local\Programs\Python\Python38-32\Scripts )  "pip install notebook"
 
 Libraries to be imported
 1.pip install beautifulsoup4
 2.pip install request
 3.pip install pymongo
 
 For storing data we are using MongoDB.Since this projeect was just for learning purpose so i used MongoDB cloud.It provides 512 Mb of free storage space.
 Steps for db setup:
 1.Login to MongoDB cloud
 2.Create a cluster there
 3.In cluster formed ,go to Collections and create a database.We have to give database and collection name.
 3.User data including user name and password is updated.
 4.We have to use created connection Id on MongoDB platform in our .py file.
 
