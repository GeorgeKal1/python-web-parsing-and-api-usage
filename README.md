# python-web-parsing-and-api-usage
This project was for my first semester in uni. It combines knowledge in basic requests and web scraping, api hosting services and plotting . The project parses the html source code from a dynamic website, uses the data to extract quotes and to create images from dummyjson.com, and saves data in a json file. It is able to host an API service with fastAPI that exposes 3 endpoints based on the quotes and last but not least it creates a plot that shows a diagram of the number of quotes based on the author

dynamic website: https://tma111.netlify.app/.netlify/functions/generate
dummyjson API: https://dummyjson.com/quotes, https://dummyjson.com/docs/image

Python libraries used: Requests,Beautifulsoup,fastAPI,Matplotlib,Query,Json,Os