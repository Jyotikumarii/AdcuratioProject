We have to scrapp data from https://news.ycombinator.com and then store the result of(Title,Image,URL) in mongoDb.While storing the data in mongoDb we have to maintain two relations. <br />
1.URL and title of blog. <br />
2.URL and its metadata like title,votes etc. <br />

Language -Python <br />
Library used for scrapping - Beautiful Soup<br />
IDE used -Jupyter notebook <br />
DB used -MongoDB Cloud <br />

Intallations required:- <br />
1.Python 3.8.5 <br />
2.jupyter notebook (Path- C:\Users\Jyoti Kumari\AppData\Local\Programs\Python\Python38-32\Scripts )  "pip install notebook" <br />
 
 Libraries to be imported  <br />
 1.pip install beautifulsoup4 <br />
 2.pip install request <br />
 3.pip install pymongo <br />
 
 For storing data we are using MongoDB.Since this projeect was just for learning purpose so i used MongoDB cloud.It provides 512 Mb of free storage space. 
 Steps for db setup:<br />
 1.Login to MongoDB cloud<br />
 2.Create a cluster there<br />
 3.In cluster formed ,go to Collections and create a database.We have to give database and collection name.<br />
 4.User data including user name and password is updated.<br />
 5.We have to use created connection Id on MongoDB platform in our .py file. <br />
 
