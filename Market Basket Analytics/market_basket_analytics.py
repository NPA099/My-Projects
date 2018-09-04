
# coding: utf-8

# In[1]:

import requests
import os
import pandas as pd
import numpy as np
import itertools


# In[2]:

url_train = "http://kevincrook.com/utd/market_basket_training.txt"
url_test = "http://kevincrook.com/utd/market_basket_test.txt"


# In[3]:

r1 = requests.get(url_train)
r2 = requests.get(url_test)


# In[4]:

mb_train_fn = "market_basket_training.txt"
mb_test_fn = "market_basket_test.txt"
mb_train = open(mb_train_fn,"wb")
mb_test = open(mb_test_fn,"wb")


# In[5]:

mb_train.write(r1.content)
mb_test.write(r2.content)


# In[6]:

mb_train.close()
mb_test.close()


# In[7]:

#Finding the maximum number of columns in the data set
#This will be used as an input parameter while reading the file to create data frame
lines = [line.rstrip('\n').split(',') for line in open(mb_test_fn)]
print(lines)
l = len(max(lines,key=len))
print(l)
i = 0
col_lst = []
while i<=l:
    col = "C"+str(i)
    print(col)
    col_lst.append(col)
    print (col_lst)
    i += 1


# In[8]:

#Loading the training data from the file as data frames using pandas
# Made 1st column as index by using the parameter index_col = 0
data_train = pd.read_table(mb_train_fn, sep = ",", header = None, lineterminator = '\n', names = col_lst, index_col= 0)
print (data_train)
data_train_4 = data_train.dropna(subset=['C3','C4'])
print(data_train_4)
data_train_3 = data_train[data_train['C4'].isnull()]
data_train_3 = data_train_3.dropna(subset=['C3'])
print(data_train_3)
data_train_2 = data_train[data_train['C3'].isnull()]
print(data_train_2)


# In[9]:

#Creating dummy records for each product
#Segregating the data frames into 3 parts as per the number of item sets
df_tr_dum_2 = pd.get_dummies(data_train_2.unstack().dropna()).groupby(level = 1).sum()
print (df_tr_dum_2)
df_tr_dum_3 = pd.get_dummies(data_train_3.unstack().dropna()).groupby(level = 1).sum()
print (df_tr_dum_3)
df_tr_dum_4 = pd.get_dummies(data_train_4.unstack().dropna()).groupby(level = 1).sum()
print (df_tr_dum_4)


# In[10]:

#Function to implement Apriori algorithm
#Finding the combinations of item sets
#Calculating the frequency and suport of the item sets
#Excluded combinations of just 1 item set as it cannot be used for recommendation
def apriori(df_tr_dum, minlen, items, support=0):
    c_len, r_len = df_tr_dum.shape
    Item_Set = []
    for c in range(minlen, r_len+1):
        for col in itertools.combinations(df_tr_dum, c):
            set_freq = df_tr_dum[list(col)].all(axis=1).sum()
            set_sup = float(set_freq)/c_len
            Item_Set.append([",".join(col), set_sup, set_freq, items])
    df_apriori = pd.DataFrame(Item_Set, columns=["Item_Set", "Support", "Frequency", "Total_Items"])
    df_apriori=df_apriori[df_apriori.Support > support] 
    return df_apriori; 


# In[11]:

#Obtaining the frequent item sets
#Merging the data frame with 2, 3 and 4 item sets
Freq_Set_2 = apriori(df_tr_dum_2, minlen=2, items=2)
Freq_Set_3 = apriori(df_tr_dum_3, minlen=3, items=3)
Freq_Set_4 = apriori(df_tr_dum_4, minlen=4, items=4)
df_Freq_Set = pd.DataFrame()
df_Freq_Set = df_Freq_Set.append(Freq_Set_2)
df_Freq_Set = df_Freq_Set.append(Freq_Set_3)
df_Freq_Set = df_Freq_Set.append(Freq_Set_4)
print (df_Freq_Set)


# In[12]:

#Loading the testing data from the file as data frames using pandas
data_test = pd.read_table(mb_test_fn, sep = ",", header = None, lineterminator = '\n', names = col_lst, index_col= 0)
print (data_test)


# In[13]:

#Filtering the last column of the test set as all the records pertaining to this column is null
df_test = data_test.iloc[:, 0:3]


# In[14]:

#Replacing P04 and P08 with null
df_test = df_test.replace(['P04', 'P08'], np.nan)


# In[15]:

#Finding the most frequent item set for the combinations of products in the test data
#The most frequent sets are the recommendation set
df_Freq_Set.index = range(154)
df_rec_set = df_Freq_Set
df_rec_set = df_rec_set.reset_index()
df_rec_set_max = pd.DataFrame()
df_rec = pd.DataFrame()
for index, row in df_test.iterrows(): 
    abc = pd.DataFrame()
    #item_count = 1
    if (pd.notnull(row['C1']))&(pd.notnull(row['C2']))&(pd.notnull(row['C3'])):
        
        print(index)
        print("444444444444444444444444444444")
        print(df_rec_set.loc[df_rec_set['Total_Items'] == 4])
        df_rec_set = df_rec_set.loc[df_rec_set['Total_Items'] == 4]
        df_rec_set = df_rec_set[df_Freq_Set['Item_Set'].str.contains(row['C1'])]
        df_rec_set = df_rec_set[df_Freq_Set['Item_Set'].str.contains(row['C2'])]
        df_rec_set = df_rec_set[df_Freq_Set['Item_Set'].str.contains(row['C3'])]
        print(df_rec_set)
        print(df_rec_set.loc[df_rec_set['Frequency'].idxmax()])
        df_rec_set_max = df_rec_set.loc[df_rec_set['Frequency'].idxmax()]
    
    elif (pd.isnull(row['C1'])&pd.isnull(row['C2']))|(pd.isnull(row['C2'])&pd.isnull(row['C3']))|(pd.isnull(row['C3'])&pd.isnull(row['C1'])):
        
        print(index)
        print("22222222222222222222222222222")
        print(df_rec_set.loc[df_rec_set['Total_Items'] == 2])
        df_rec_set = df_rec_set.loc[df_rec_set['Total_Items'] == 2]
        abc = row.replace([np.nan],'abc')
        print(abc)
        if abc[0]!='abc':
            df_rec_set = df_rec_set[df_Freq_Set['Item_Set'].str.contains(abc[0])]
            print(df_rec_set)
            print("&&&&&&&&&&&&&&&&&&&&&&&&")
        if abc[1]!='abc':
            df_rec_set = df_rec_set[df_Freq_Set['Item_Set'].str.contains(abc[1])]
            print(df_rec_set)
            print("########################")
        if abc[2]!='abc':
            df_rec_set = df_rec_set[df_Freq_Set['Item_Set'].str.contains(abc[2])]
            print(df_rec_set)
            print("^^^^^^^^^^^^^^^^^^^^^^^^^")
        
        print(df_rec_set.loc[df_rec_set['Frequency'].idxmax()])
        df_rec_set_max = df_rec_set.loc[df_rec_set['Frequency'].idxmax()]
    
    else:
        
        print(index)
        print("33333333333333333333333333333")
        print(df_rec_set.loc[df_rec_set['Total_Items'] == 3])
        df_rec_set = df_rec_set.loc[df_rec_set['Total_Items'] == 3]
        abc = row.replace([np.nan],'abc')
        print(abc)
        if abc[0]!='abc':
            df_rec_set = df_rec_set[df_Freq_Set['Item_Set'].str.contains(abc[0])]
            print(df_rec_set)
            print("&&&&&&&&&&&&&&&&&&&&&&&&")
        if abc[1]!='abc':
            print(row[1])
            df_rec_set = df_rec_set[df_Freq_Set['Item_Set'].str.contains(abc[1])]
            print(df_rec_set)
            print("########################")
        if abc[2]!='abc':
            df_rec_set = df_rec_set[df_Freq_Set['Item_Set'].str.contains(abc[2])]
            print(df_rec_set)
            print("^^^^^^^^^^^^^^^^^^^^^^^^^")
            
        print(df_rec_set.loc[df_rec_set['Frequency'].idxmax()])
        df_rec_set_max = df_rec_set.loc[df_rec_set['Frequency'].idxmax()]
    
    
    df_rec = df_rec.append(df_rec_set_max)
    df_rec_set = df_Freq_Set
    print(df_rec)
    print("********************")
    print(df_rec_set_max)
    print("@@@@@@@@@@@@@@@@@@")


# In[16]:

#Getting the recommendation sets as a list of lists
df_rec_lst = list(df_rec['Item_Set'])
rec_lst = []
for x in df_rec_lst:
    y = str(x).split(',')
    rec_lst.append(y)
print (rec_lst)


# In[17]:

#Getting the products in test file as list of list
lines_tst = [line.rstrip('\n').split(',') for line in open(mb_test_fn)]
#print(lines_tst)
lines_tst_prod = [el[1:] for el in lines_tst]
print(lines_tst_prod)


# In[18]:

#Getting the recommended products and writing it to the output file
i=0
x=[]
with open(mb_test_fn, 'r') as in_file:
    with open('market_basket_recommendations.txt', 'w') as out_file:
        while i<len(rec_lst):
            for line in in_file:
                x=list(set(rec_lst[i]) - set(lines_tst_prod[i]))
                str1 = ''.join(x)
                print(str1)
                print(line[0:4]+str1)
                out_file.write(line[0:4]+str1+'\n')
                #print(line[0:4].join(str1))
                #out_file.write(line[0:4].join(str1))
                i+=1

