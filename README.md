### What?
Analysing trends and semantics of published content in Hungary's leading online newspaper from 2014 to 2018.

### Why?
I wanted to prove with data that a once popular news outlet turned into political propaganda site.

### How?
I scraped origo's archive and stored all of their articles regarding domestic and foreign news.
Then I grouped and cleansed the data and looked at trends that readers noticed in the past few years.

 - Getting the data (see: [spiders](/spiders) and [link parser notebook](/parse_article_links.ipynb))
 
    One scrapy spider fetched the last 4 years' articles, then filtered down this list to certain categories (domestic and political news), another spider went through this list and fetched the contents of each article. In the end, more than 60k of articles were fetched.
 
 - Cleansing and preparing for data analysis (see: [raw data cleaning notebook](/parse_article_contents.ipynb) and [content enhancement notebook](/prepare_article_data.ipynb)) 
 
    Raw data that was returned from the crawling spiders had to be cleansed, becaused it contained outer HTML tags that were not needed. Then, article titles and their main content were tokenized and stemmed using nltk, to create the final data for article analysis.
 
 - Analysis
 
    TBC
