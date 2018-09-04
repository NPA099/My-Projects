
# coding: utf-8

# In[1]:

# Importing packages
import json, io, requests, codecs, pandas as pd, numpy as np


# In[2]:

# Defining the url for json file
url = 'http://kevincrook.com/utd/tweets.json'


# In[3]:

# Getting the json from the url
r = requests.get(url)


# In[4]:

# Assigning the twitter data in json format to a new variable
twitter_data = r.content


# In[5]:

with open('twitter_data_in.json', 'wb') as f:
    f.write(twitter_data)


# In[6]:

# Writing the json data into a local json file
with open('twitter_data_in.json') as in_data:
    d_list = json.load(in_data)


# In[7]:

# Finding the total number of events from the json file
Total_Events = len(d_list)


# In[8]:

# Filtering the deleted tweets from the main list to get the 
#Tweets_count = 0
d_tweets = []
for d in d_list:
    if 'text' in d:
        #Tweets_count += 1
        d_tweets.append(d)


# In[9]:

# Count of the tweets
Tweets_count = len(d_tweets)


# In[10]:

# Finding the languages and frequency of languages
# Sorting the languages based on decending order of the frequency
# Writing the data into twitter_analytics file
lang_list = []
for d in d_tweets:
    #print (d['lang'])
    lang_list.append(d['lang'])
lang_list.sort(reverse=True)
print (lang_list)
lang_dict = {x:lang_list.count(x) for x in lang_list}
lang_list_dec = sorted(lang_dict.items(), key=lambda x: (-x[1])) 
print (lang_list_dec)
with open('twitter_analytics.txt', 'w', encoding='utf-8') as f:
    f.write(str(Total_Events)+'\n')
    f.write(str(Tweets_count)+'\n')
    for line in lang_list_dec:
        lang_count = str(line)
        if lang_count[2:5]=='und':
            f.write(lang_count[2:5]+lang_count[6:7]+lang_count[8:-1]+'\n')
        else:
            f.write(lang_count[2:4]+lang_count[5:6]+lang_count[7:-1]+'\n')


# In[11]:

# Writing the tweets with utf-8 encoding in tweets file
with open('tweets.txt','w',encoding='utf-8') as out_file:
    tweets_list = []
    for d in d_tweets:
        tweets_list.append(d['text'])
    for tweets in tweets_list:
        tweets = tweets.encode('utf-8')
        out_file.write(str(tweets)[2:]+'\n')


# In[ ]:



