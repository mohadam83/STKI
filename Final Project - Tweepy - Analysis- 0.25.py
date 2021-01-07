#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import numpy as np
import nltk
from sklearn.metrics import accuracy_score
from nltk import word_tokenize
nltk.download('punkt')


# In[2]:


from sklearn.metrics import accuracy_score


# In[3]:


f = open("Positive.txt", "r")
positive = f.read().split("\n")
print(len(positive))

f = open("Negative.txt", "r")
negative = f.read().split("\n")
print(len(negative))

f = open("SlangAlay.txt", "r")
alay = f.read().split("\n")
list_lay = list()
for i in range(0, 15880):
    list_temp = list()
    list_temp.append(alay[i].split('\t')[0])
    list_temp.append(alay[i].split('\t')[1])
    list_lay.append(list_temp)
print(len(list_lay))


# In[4]:


panjang_alay = len(list_lay)


# In[5]:


#Emoji patterns
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)


# In[6]:


import demoji
demoji.download_codes()


# In[7]:


# !pip install demoji


# In[7]:


top1_29desAnalisis = []
top1_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 1
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(114):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus +=1
            continue        
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")
        
        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
               
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        print("pos : " + str(count_pos) + " neg : " + str(count_neg))
        
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top1_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top1_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top1_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top1_29desAnalisis.append(tweet_bersih)
    print("dihapus : " + str(dihapus))
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 


# In[38]:


top2_29desAnalisis = []
top2_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 2
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(147):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        tweet_bersih = tweet_bersih.replace("#JanganPercayaFPIMunafik", " ")
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
#         print(tweet_bersih)
        ubah = 0
        for j in range (15880):
            if list_lay[j][0] in tweet_bersih:
#                 print(list_lay[j][0])
#                 print(list_lay[j][1])
                tweet_bersih.replace(list_lay[j][0], list_lay[j][1])
                ubah += 1
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)

        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")
        
        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        print("pos : " + str(count_pos) + " neg : " + str(count_neg))
        
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top2_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top2_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top2_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top2_29desAnalisis.append(tweet_bersih)
    print("dihapus : " + str(dihapus))
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 


# In[39]:


top3_29desAnalisis = []
top3_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 3
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(79):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        tweet_bersih = tweet_bersih.replace("#PeringatanGalonIsiUlangBPA", " ")
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")  

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]

        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)

        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")
        
        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top3_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top3_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top3_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top3_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[40]:


top4_29desAnalisis = []
top4_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 4
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(389):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        tweet_bersih = tweet_bersih.replace("#THEFIRSTSTEP_TREASUREEFFECT", " ")
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")  

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]

        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top4_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top4_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top4_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top4_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[41]:


top5_29desAnalisis = []
top5_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 5
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(224):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        tweet_bersih = tweet_bersih.replace("#RisalahAkhirTahun2020", " ")
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top5_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top5_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top5_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top5_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg))
    print("dihapus : " + str(dihapus))


# In[12]:


top6_29desAnalisis = []
top6_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 6
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(111):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ") 

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top6_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top6_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top6_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top6_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[42]:


top7_29desAnalisis = []
top7_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 7
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(469):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        tweet_bersih = tweet_bersih.replace("#KhilafahAjaranIslam", " ")
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")  

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top7_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top7_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top7_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top7_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[14]:


top8_29desAnalisis = []
top8_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 8
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(100):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")  

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top8_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top8_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top8_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top8_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[15]:


top9_29desAnalisis = []
top9_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 9
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(435):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")  

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top9_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top9_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top9_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top9_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[16]:


top10_29desAnalisis = []
top10_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 10
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(455):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top10_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top10_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top10_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top10_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[17]:


top11_29desAnalisis = []
top11_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 11
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(121):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top11_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top11_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top11_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top11_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[43]:


top12_29desAnalisis = []
top12_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 12
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(172):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        tweet_bersih = tweet_bersih.replace("#ByeByeDemocracy", " ")
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ") 

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top12_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top12_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top12_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top12_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[44]:


top13_29desAnalisis = []
top13_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 13
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(118):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        tweet_bersih = tweet_bersih.replace("#ENHYPENonASC", " ")
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ") 

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top13_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top13_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top13_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top13_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[45]:


top14_29desAnalisis = []
top14_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 14
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(208):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        tweet_bersih = tweet_bersih.replace("#StopTindakPidana", " ")
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")  

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top14_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top14_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top14_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top14_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[46]:


top15_29desAnalisis = []
top15_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 15
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(85):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        tweet_bersih = tweet_bersih.replace("#ENHYPEN ON AFTER SCHOOL CLUB", " ")
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")  

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top15_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top15_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top15_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top15_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[47]:


top16_29desAnalisis = []
top16_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 16
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(239):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        tweet_bersih = tweet_bersih.replace("#SpecialDJDoyoung", " ")
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")  

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top16_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top16_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top16_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top16_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[23]:


top17_29desAnalisis = []
top17_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 17
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(598):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ")  

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top17_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top17_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top17_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top17_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[24]:


top18_29desAnalisis = []
top18_29desLabel = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 18
nama_file = "./crawl/crawl_" + str(count) + ".txt"
dihapus = 0
with open(nama_file, 'r', encoding='utf-8') as file:
    for i in range(617):
        tweet_bersih = file.readline()
        tweet_bersih = tweet_bersih[15:-3]
        
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            dihapus += 1
            continue
        
        # Mengganti Enter dengan Space
        tweet_bersih = tweet_bersih.replace("\\n", " ")
    
        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r' ', tweet_bersih)
        tweet_bersih = demoji.replace(tweet_bersih," ") 

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet_bersih).split())
        tweet_bersih = tweet_bersih[2:]
        
        # tokenisasi kata
        word_token = word_tokenize(tweet_bersih)
        
        # Mengganti Kata Alay
        print("sebelum : " + tweet_bersih)
        ubah = 0
        for j in range (15880):
            for k in range (len(word_token)):
                if list_lay[j][0] == word_token[k]:
                    word_token[k] = word_token[k].replace(list_lay[j][0], list_lay[j][1])
                    ubah += 1
        print("ubah : " + str(ubah))
        
        tweet_bersih = str()
        for j in range(len(word_token)):
            if(j > 0):
                tweet_bersih += " "
            tweet_bersih = tweet_bersih + str(word_token[j])
        print("sesudah : " + tweet_bersih)
        print("=========================================")

        # menghitung analysis sentiment pada tiap kata di sebuah tweet
        count_pos = 0
        count_neg = 0
        for j in range(len(word_token)):
            if word_token[j] in positive:
                count_pos += 1
            if word_token[j] in negative:
                count_neg += 1
        # menghitung analysis sentiment pada tiap tweet di sebuah trending
        pos = int(1)
        neg = int(-1)
        netral = int(0)
        if(count_pos > count_neg):
            top18_29desLabel.append(pos)
            hasil_sentiment_pos += 1
        elif (count_pos == count_neg):
            top18_29desLabel.append(neg)
            hasil_sentiment_net += 1
        else:
            top18_29desLabel.append(netral)
            hasil_sentiment_neg += 1
            
        top18_29desAnalisis.append(tweet_bersih)
    print("positive : " + str(hasil_sentiment_pos))
    print("netral : " + str(hasil_sentiment_net))
    print("negative : " + str(hasil_sentiment_neg)) 
    print("dihapus : " + str(dihapus))


# In[48]:


print(len(top1_29desAnalisis))
print(len(top1_29desLabel))
print(type(top1_29desLabel))
top1_29desLabel = np.array(top1_29desLabel)
print(type(top1_29desLabel))
print("---------------Batas 1---------------")

print(len(top2_29desAnalisis))
print(len(top2_29desLabel))
print(type(top2_29desLabel))
top2_29desLabel = np.array(top2_29desLabel)
print(type(top2_29desLabel))
print("---------------Batas 2---------------")

print(len(top3_29desAnalisis))
print(len(top3_29desLabel))
print(type(top3_29desLabel))
top3_29desLabel = np.array(top3_29desLabel)
print(type(top3_29desLabel))
print("---------------Batas 3---------------")

print(len(top4_29desAnalisis))
print(len(top4_29desLabel))
print(type(top4_29desLabel))
top4_29desLabel = np.array(top4_29desLabel)
print(type(top4_29desLabel))
print("---------------Batas 4---------------")

print(len(top5_29desAnalisis))
print(len(top5_29desLabel))
print(type(top5_29desLabel))
top5_29desLabel = np.array(top5_29desLabel)
print(type(top5_29desLabel))
print("---------------Batas 5---------------")

print(len(top6_29desAnalisis))
print(len(top6_29desLabel))
print(type(top6_29desLabel))
top6_29desLabel = np.array(top6_29desLabel)
print(type(top6_29desLabel))
print("---------------Batas 6---------------")

print(len(top7_29desAnalisis))
print(len(top7_29desLabel))
print(type(top7_29desLabel))
top7_29desLabel = np.array(top7_29desLabel)
print(type(top7_29desLabel))
print("---------------Batas 7---------------")

print(len(top8_29desAnalisis))
print(len(top8_29desLabel))
print(type(top8_29desLabel))
top8_29desLabel = np.array(top8_29desLabel)
print(type(top8_29desLabel))
print("---------------Batas 8---------------")

print(len(top9_29desAnalisis))
print(len(top9_29desLabel))
print(type(top9_29desLabel))
top9_29desLabel = np.array(top9_29desLabel)
print(type(top9_29desLabel))
print("---------------Batas 9---------------")

print(len(top10_29desAnalisis))
print(len(top10_29desLabel))
print(type(top10_29desLabel))
top10_29desLabel = np.array(top10_29desLabel)
print(type(top10_29desLabel))
print("---------------Batas 10---------------")

print(len(top11_29desAnalisis))
print(len(top11_29desLabel))
print(type(top11_29desLabel))
top11_29desLabel = np.array(top11_29desLabel)
print(type(top11_29desLabel))
print("---------------Batas 11---------------")

print(len(top12_29desAnalisis))
print(len(top12_29desLabel))
print(type(top12_29desLabel))
top12_29desLabel = np.array(top12_29desLabel)
print(type(top12_29desLabel))
print("---------------Batas 12---------------")

print(len(top13_29desAnalisis))
print(len(top13_29desLabel))
print(type(top13_29desLabel))
top13_29desLabel = np.array(top13_29desLabel)
print(type(top13_29desLabel))
print("---------------Batas 13---------------")

print(len(top14_29desAnalisis))
print(len(top14_29desLabel))
print(type(top14_29desLabel))
top14_29desLabel = np.array(top14_29desLabel)
print(type(top14_29desLabel))
print("---------------Batas 14---------------")

print(len(top15_29desAnalisis))
print(len(top15_29desLabel))
print(type(top15_29desLabel))
top15_29desLabel = np.array(top15_29desLabel)
print(type(top15_29desLabel))
print("---------------Batas 15---------------")

print(len(top16_29desAnalisis))
print(len(top16_29desLabel))
print(type(top16_29desLabel))
top16_29desLabel = np.array(top16_29desLabel)
print(type(top16_29desLabel))
print("---------------Batas 16---------------")

print(len(top17_29desAnalisis))
print(len(top17_29desLabel))
print(type(top17_29desLabel))
top17_29desLabel = np.array(top17_29desLabel)
print(type(top17_29desLabel))
print("---------------Batas 17---------------")

print(len(top18_29desAnalisis))
print(len(top18_29desLabel))
print(type(top18_29desLabel))
top18_29desLabel = np.array(top18_29desLabel)
print(type(top18_29desLabel))
print("---------------Batas 18---------------")


# In[49]:


from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2)
X1 = tfidf_vectorizer.fit_transform(top1_29desAnalisis)
print(X1.shape)

X2 = tfidf_vectorizer.fit_transform(top2_29desAnalisis)
print(X2.shape)

X3 = tfidf_vectorizer.fit_transform(top3_29desAnalisis)
print(X3.shape)

X4 = tfidf_vectorizer.fit_transform(top4_29desAnalisis)
print(X4.shape)

X5 = tfidf_vectorizer.fit_transform(top5_29desAnalisis)
print(X5.shape)

X6 = tfidf_vectorizer.fit_transform(top6_29desAnalisis)
print(X6.shape)

X7 = tfidf_vectorizer.fit_transform(top7_29desAnalisis)
print(X7.shape)

X8 = tfidf_vectorizer.fit_transform(top8_29desAnalisis)
print(X8.shape)

X9 = tfidf_vectorizer.fit_transform(top9_29desAnalisis)
print(X9.shape)

X10 = tfidf_vectorizer.fit_transform(top10_29desAnalisis)
print(X10.shape)

X11 = tfidf_vectorizer.fit_transform(top11_29desAnalisis)
print(X11.shape)

X12 = tfidf_vectorizer.fit_transform(top12_29desAnalisis)
print(X12.shape)

X13 = tfidf_vectorizer.fit_transform(top13_29desAnalisis)
print(X13.shape)

X14 = tfidf_vectorizer.fit_transform(top14_29desAnalisis)
print(X14.shape)

X15 = tfidf_vectorizer.fit_transform(top15_29desAnalisis)
print(X15.shape)

X16 = tfidf_vectorizer.fit_transform(top16_29desAnalisis)
print(X16.shape)

X17 = tfidf_vectorizer.fit_transform(top17_29desAnalisis)
print(X17.shape)

X18 = tfidf_vectorizer.fit_transform(top18_29desAnalisis)
print(X18.shape)


# In[50]:


# Cleaning noise
# Hapus label yang memiliki row = 0 pada tfidf-nya
# Hapus row yang memiliki nilai 0
Y1 = top1_29desLabel[X1.getnnz(1)>0]
X1_clear = X1[X1.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero1 = list()
for i, d in enumerate(X1.getnnz(1)>0):
    if d:
        docs_nonzero1.append(top1_29desAnalisis[i])        
print(X1_clear.shape, len(Y1), len(docs_nonzero1))

Y2 = top2_29desLabel[X2.getnnz(1)>0]
X2_clear = X2[X2.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero2 = list()
for i, d in enumerate(X2.getnnz(1)>0):
    if d:
        docs_nonzero2.append(top2_29desAnalisis[i])        
print(X2_clear.shape, len(Y2), len(docs_nonzero2))

Y3 = top3_29desLabel[X3.getnnz(1)>0]
X3_clear = X3[X3.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero3 = list()
for i, d in enumerate(X3.getnnz(1)>0):
    if d:
        docs_nonzero3.append(top3_29desAnalisis[i])        
print(X3_clear.shape, len(Y3), len(docs_nonzero3))

Y4 = top4_29desLabel[X4.getnnz(1)>0]
X4_clear = X4[X4.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero4 = list()
for i, d in enumerate(X4.getnnz(1)>0):
    if d:
        docs_nonzero4.append(top4_29desAnalisis[i])        
print(X4_clear.shape, len(Y4), len(docs_nonzero4))

Y5 = top5_29desLabel[X5.getnnz(1)>0]
X5_clear = X5[X5.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero5 = list()
for i, d in enumerate(X5.getnnz(1)>0):
    if d:
        docs_nonzero5.append(top5_29desAnalisis[i])        
print(X5_clear.shape, len(Y5), len(docs_nonzero5))

Y6 = top6_29desLabel[X6.getnnz(1)>0]
X6_clear = X6[X6.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero6 = list()
for i, d in enumerate(X6.getnnz(1)>0):
    if d:
        docs_nonzero6.append(top6_29desAnalisis[i])        
print(X6_clear.shape, len(Y6), len(docs_nonzero6))

Y7 = top7_29desLabel[X7.getnnz(1)>0]
X7_clear = X7[X7.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero7 = list()
for i, d in enumerate(X7.getnnz(1)>0):
    if d:
        docs_nonzero7.append(top7_29desAnalisis[i])        
print(X7_clear.shape, len(Y7), len(docs_nonzero7))

Y8 = top8_29desLabel[X8.getnnz(1)>0]
X8_clear = X8[X8.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero8 = list()
for i, d in enumerate(X8.getnnz(1)>0):
    if d:
        docs_nonzero8.append(top8_29desAnalisis[i])        
print(X8_clear.shape, len(Y8), len(docs_nonzero8))

Y9 = top9_29desLabel[X9.getnnz(1)>0]
X9_clear = X9[X9.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero9 = list()
for i, d in enumerate(X9.getnnz(1)>0):
    if d:
        docs_nonzero9.append(top9_29desAnalisis[i])        
print(X9_clear.shape, len(Y9), len(docs_nonzero9))

Y10 = top10_29desLabel[X10.getnnz(1)>0]
X10_clear = X10[X10.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero10 = list()
for i, d in enumerate(X10.getnnz(1)>0):
    if d:
        docs_nonzero10.append(top10_29desAnalisis[i])        
print(X10_clear.shape, len(Y10), len(docs_nonzero10))

Y11 = top11_29desLabel[X11.getnnz(1)>0]
X11_clear = X11[X11.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero11 = list()
for i, d in enumerate(X11.getnnz(1)>0):
    if d:
        docs_nonzero11.append(top11_29desAnalisis[i])        
print(X11_clear.shape, len(Y11), len(docs_nonzero11))

Y12 = top12_29desLabel[X12.getnnz(1)>0]
X12_clear = X12[X12.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero12 = list()
for i, d in enumerate(X12.getnnz(1)>0):
    if d:
        docs_nonzero12.append(top12_29desAnalisis[i])        
print(X12_clear.shape, len(Y12), len(docs_nonzero12))

Y13 = top13_29desLabel[X13.getnnz(1)>0]
X13_clear = X13[X13.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero13 = list()
for i, d in enumerate(X13.getnnz(1)>0):
    if d:
        docs_nonzero13.append(top13_29desAnalisis[i])        
print(X13_clear.shape, len(Y13), len(docs_nonzero13))

Y14 = top14_29desLabel[X14.getnnz(1)>0]
X14_clear = X14[X14.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero14 = list()
for i, d in enumerate(X14.getnnz(1)>0):
    if d:
        docs_nonzero14.append(top14_29desAnalisis[i])        
print(X14_clear.shape, len(Y14), len(docs_nonzero14))

Y15 = top15_29desLabel[X15.getnnz(1)>0]
X15_clear = X15[X15.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero15 = list()
for i, d in enumerate(X15.getnnz(1)>0):
    if d:
        docs_nonzero15.append(top15_29desAnalisis[i])        
print(X15_clear.shape, len(Y15), len(docs_nonzero15))

Y16 = top16_29desLabel[X16.getnnz(1)>0]
X16_clear = X16[X16.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero16 = list()
for i, d in enumerate(X16.getnnz(1)>0):
    if d:
        docs_nonzero16.append(top16_29desAnalisis[i])        
print(X16_clear.shape, len(Y16), len(docs_nonzero16))

Y17 = top17_29desLabel[X17.getnnz(1)>0]
X17_clear = X17[X17.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero17 = list()
for i, d in enumerate(X17.getnnz(1)>0):
    if d:
        docs_nonzero17.append(top17_29desAnalisis[i])        
print(X17_clear.shape, len(Y17), len(docs_nonzero17))

Y18 = top18_29desLabel[X18.getnnz(1)>0]
X18_clear = X18[X18.getnnz(1)>0]
# Hapus dokumen yang memiliki nilai row 0
docs_nonzero18 = list()
for i, d in enumerate(X18.getnnz(1)>0):
    if d:
        docs_nonzero18.append(top18_29desAnalisis[i])        
print(X18_clear.shape, len(Y18), len(docs_nonzero18))


# In[51]:


# Membagi data menjadi dua yaitu data training dan data testing
from sklearn.model_selection import train_test_split

X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X1_clear, Y1, test_size=.25, random_state=7)
print(X_train1.shape, X_test1.shape)

X_train2, X_test2, Y_train2, Y_test2 = train_test_split(X2_clear, Y2, test_size=.25, random_state=7)
print(X_train2.shape, X_test2.shape)

X_train3, X_test3, Y_train3, Y_test3 = train_test_split(X3_clear, Y3, test_size=.25, random_state=7)
print(X_train3.shape, X_test3.shape)

X_train4, X_test4, Y_train4, Y_test4 = train_test_split(X4_clear, Y4, test_size=.25, random_state=7)
print(X_train4.shape, X_test4.shape)

X_train5, X_test5, Y_train5, Y_test5 = train_test_split(X5_clear, Y5, test_size=.25, random_state=7)
print(X_train5.shape, X_test5.shape)

X_train6, X_test6, Y_train6, Y_test6 = train_test_split(X6_clear, Y6, test_size=.25, random_state=7)
print(X_train6.shape, X_test6.shape)

X_train7, X_test7, Y_train7, Y_test7 = train_test_split(X7_clear, Y7, test_size=.25, random_state=7)
print(X_train7.shape, X_test7.shape)

X_train8, X_test8, Y_train8, Y_test8 = train_test_split(X8_clear, Y8, test_size=.25, random_state=7)
print(X_train8.shape, X_test8.shape)

X_train9, X_test9, Y_train9, Y_test9 = train_test_split(X9_clear, Y9, test_size=.25, random_state=7)
print(X_train9.shape, X_test9.shape)

X_train10, X_test10, Y_train10, Y_test10 = train_test_split(X10_clear, Y10, test_size=.25, random_state=7)
print(X_train10.shape, X_test10.shape)

X_train11, X_test11, Y_train11, Y_test11 = train_test_split(X11_clear, Y11, test_size=.25, random_state=7)
print(X_train11.shape, X_test11.shape)

X_train12, X_test12, Y_train12, Y_test12 = train_test_split(X12_clear, Y12, test_size=.25, random_state=7)
print(X_train12.shape, X_test12.shape)

X_train13, X_test13, Y_train13, Y_test13 = train_test_split(X13_clear, Y13, test_size=.25, random_state=7)
print(X_train13.shape, X_test13.shape)

X_train14, X_test14, Y_train14, Y_test14 = train_test_split(X14_clear, Y14, test_size=.25, random_state=7)
print(X_train14.shape, X_test14.shape)

X_train15, X_test15, Y_train15, Y_test15 = train_test_split(X15_clear, Y15, test_size=.25, random_state=7)
print(X_train15.shape, X_test15.shape)

X_train16, X_test16, Y_train16, Y_test16 = train_test_split(X16_clear, Y16, test_size=.25, random_state=7)
print(X_train16.shape, X_test16.shape)

X_train17, X_test17, Y_train17, Y_test17 = train_test_split(X17_clear, Y17, test_size=.25, random_state=7)
print(X_train17.shape, X_test17.shape)

X_train18, X_test18, Y_train18, Y_test18 = train_test_split(X18_clear, Y18, test_size=.25, random_state=7)
print(X_train18.shape, X_test18.shape)


# In[52]:


import numpy as np
from sklearn.metrics import precision_recall_fscore_support
from sklearn import metrics


# In[53]:


# Menggunakan data sebelumnya
# Naive bayes menggunakan library scikit-learn
# http://scikit-learn.org/stable/modules/naive_bayes.html
from sklearn.naive_bayes import GaussianNB

count = 0
list_akurasi_nbc = list()
gnb = GaussianNB()
nbc = gnb.fit(X_train1.toarray(), Y_train1) 
Y_nbc = nbc.predict(X_test1.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test1, Y_nbc))
print(accuracy_score(Y_test1, Y_nbc))
print(precision_recall_fscore_support(Y_test1, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train2.toarray(), Y_train2) 
Y_nbc = nbc.predict(X_test2.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test2, Y_nbc))
print(accuracy_score(Y_test2, Y_nbc))
print(precision_recall_fscore_support(Y_test2, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train3.toarray(), Y_train3) 
Y_nbc = nbc.predict(X_test3.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test3, Y_nbc))
print(accuracy_score(Y_test3, Y_nbc))
print(precision_recall_fscore_support(Y_test3, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train4.toarray(), Y_train4) 
Y_nbc = nbc.predict(X_test4.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test4, Y_nbc))
print(accuracy_score(Y_test4, Y_nbc))
print(precision_recall_fscore_support(Y_test4, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train5.toarray(), Y_train5) 
Y_nbc = nbc.predict(X_test5.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test5, Y_nbc))
print(accuracy_score(Y_test5, Y_nbc))
print(precision_recall_fscore_support(Y_test5, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train6.toarray(), Y_train6) 
Y_nbc = nbc.predict(X_test6.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test6, Y_nbc))
print(accuracy_score(Y_test6, Y_nbc))
print(precision_recall_fscore_support(Y_test6, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train7.toarray(), Y_train7) 
Y_nbc = nbc.predict(X_test7.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test7, Y_nbc))
print(accuracy_score(Y_test7, Y_nbc))
print(precision_recall_fscore_support(Y_test7, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train8.toarray(), Y_train8) 
Y_nbc = nbc.predict(X_test8.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test8, Y_nbc))
print(accuracy_score(Y_test8, Y_nbc))
print(precision_recall_fscore_support(Y_test8, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train9.toarray(), Y_train9) 
Y_nbc = nbc.predict(X_test9.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test9, Y_nbc))
print(accuracy_score(Y_test9, Y_nbc))
print(precision_recall_fscore_support(Y_test9, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train10.toarray(), Y_train10) 
Y_nbc = nbc.predict(X_test10.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test10, Y_nbc))
print(accuracy_score(Y_test10, Y_nbc))
print(precision_recall_fscore_support(Y_test10, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train11.toarray(), Y_train11) 
Y_nbc = nbc.predict(X_test11.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test11, Y_nbc))
print(accuracy_score(Y_test11, Y_nbc))
print(precision_recall_fscore_support(Y_test11, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train12.toarray(), Y_train12) 
Y_nbc = nbc.predict(X_test12.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test12, Y_nbc))
print(accuracy_score(Y_test12, Y_nbc))
print(precision_recall_fscore_support(Y_test12, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train13.toarray(), Y_train13) 
Y_nbc = nbc.predict(X_test13.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test13, Y_nbc))
print(accuracy_score(Y_test13, Y_nbc))
print(precision_recall_fscore_support(Y_test13, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train14.toarray(), Y_train14) 
Y_nbc = nbc.predict(X_test14.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test14, Y_nbc))
print(accuracy_score(Y_test14, Y_nbc))
print(precision_recall_fscore_support(Y_test14, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train15.toarray(), Y_train15) 
Y_nbc = nbc.predict(X_test15.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test15, Y_nbc))
print(accuracy_score(Y_test15, Y_nbc))
print(precision_recall_fscore_support(Y_test15, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train16.toarray(), Y_train16) 
Y_nbc = nbc.predict(X_test16.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test16, Y_nbc))
print(accuracy_score(Y_test16, Y_nbc))
print(precision_recall_fscore_support(Y_test16, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train17.toarray(), Y_train17) 
Y_nbc = nbc.predict(X_test17.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test17, Y_nbc))
print(accuracy_score(Y_test17, Y_nbc))
print(precision_recall_fscore_support(Y_test17, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

nbc = gnb.fit(X_train18.toarray(), Y_train18) 
Y_nbc = nbc.predict(X_test18.toarray())
list_akurasi_nbc.append(accuracy_score(Y_test18, Y_nbc))
print(accuracy_score(Y_test18, Y_nbc))
print(precision_recall_fscore_support(Y_test18, Y_nbc, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")
print(len(list_akurasi_nbc))


# In[54]:


# SVM
# http://scikit-learn.org/stable/modules/svm.html
from sklearn import svm

count = 0
list_akurasi_svm = list()
dSVM = svm.SVC(decision_function_shape='ovo') # one versus one SVM
dSVM.fit(X_train1, Y_train1)
Y_SVM = dSVM.predict(X_test1)
list_akurasi_svm.append(accuracy_score(Y_test1, Y_SVM))
print(accuracy_score(Y_test1, Y_SVM))
print(precision_recall_fscore_support(Y_test1, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train2, Y_train2)
Y_SVM = dSVM.predict(X_test2)
list_akurasi_svm.append(accuracy_score(Y_test2, Y_SVM))
print(accuracy_score(Y_test2, Y_SVM))
print(precision_recall_fscore_support(Y_test2, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train3, Y_train3)
Y_SVM = dSVM.predict(X_test3)
list_akurasi_svm.append(accuracy_score(Y_test3, Y_SVM))
print(accuracy_score(Y_test3, Y_SVM))
print(precision_recall_fscore_support(Y_test3, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train4, Y_train4)
Y_SVM = dSVM.predict(X_test4)
list_akurasi_svm.append(accuracy_score(Y_test4, Y_SVM))
print(accuracy_score(Y_test4, Y_SVM))
print(precision_recall_fscore_support(Y_test4, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train5, Y_train5)
Y_SVM = dSVM.predict(X_test5)
list_akurasi_svm.append(accuracy_score(Y_test5, Y_SVM))
print(accuracy_score(Y_test5, Y_SVM))
print(precision_recall_fscore_support(Y_test5, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train6, Y_train6)
Y_SVM = dSVM.predict(X_test6)
list_akurasi_svm.append(accuracy_score(Y_test6, Y_SVM))
print(accuracy_score(Y_test6, Y_SVM))
print(precision_recall_fscore_support(Y_test6, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train7, Y_train7)
Y_SVM = dSVM.predict(X_test7)
list_akurasi_svm.append(accuracy_score(Y_test7, Y_SVM))
print(accuracy_score(Y_test7, Y_SVM))
print(precision_recall_fscore_support(Y_test7, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train8, Y_train8)
Y_SVM = dSVM.predict(X_test8)
list_akurasi_svm.append(accuracy_score(Y_test8, Y_SVM))
print(accuracy_score(Y_test8, Y_SVM))
print(precision_recall_fscore_support(Y_test8, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train9, Y_train9)
Y_SVM = dSVM.predict(X_test9)
list_akurasi_svm.append(accuracy_score(Y_test9, Y_SVM))
print(accuracy_score(Y_test9, Y_SVM))
print(precision_recall_fscore_support(Y_test9, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train10, Y_train10)
Y_SVM = dSVM.predict(X_test10)
list_akurasi_svm.append(accuracy_score(Y_test10, Y_SVM))
print(accuracy_score(Y_test10, Y_SVM))
print(precision_recall_fscore_support(Y_test10, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train11, Y_train11)
Y_SVM = dSVM.predict(X_test11)
list_akurasi_svm.append(accuracy_score(Y_test11, Y_SVM))
print(accuracy_score(Y_test11, Y_SVM))
print(precision_recall_fscore_support(Y_test11, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train12, Y_train12)
Y_SVM = dSVM.predict(X_test12)
list_akurasi_svm.append(accuracy_score(Y_test12, Y_SVM))
print(accuracy_score(Y_test12, Y_SVM))
print(precision_recall_fscore_support(Y_test12, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train13, Y_train13)
Y_SVM = dSVM.predict(X_test13)
list_akurasi_svm.append(accuracy_score(Y_test13, Y_SVM))
print(accuracy_score(Y_test13, Y_SVM))
print(precision_recall_fscore_support(Y_test13, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train14, Y_train14)
Y_SVM = dSVM.predict(X_test14)
list_akurasi_svm.append(accuracy_score(Y_test14, Y_SVM))
print(accuracy_score(Y_test14, Y_SVM))
print(precision_recall_fscore_support(Y_test14, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train15, Y_train15)
Y_SVM = dSVM.predict(X_test15)
list_akurasi_svm.append(accuracy_score(Y_test15, Y_SVM))
print(accuracy_score(Y_test15, Y_SVM))
print(precision_recall_fscore_support(Y_test15, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train16, Y_train16)
Y_SVM = dSVM.predict(X_test16)
list_akurasi_svm.append(accuracy_score(Y_test16, Y_SVM))
print(accuracy_score(Y_test16, Y_SVM))
print(precision_recall_fscore_support(Y_test16, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train17, Y_train17)
Y_SVM = dSVM.predict(X_test17)
list_akurasi_svm.append(accuracy_score(Y_test17, Y_SVM))
print(accuracy_score(Y_test17, Y_SVM))
print(precision_recall_fscore_support(Y_test17, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

dSVM.fit(X_train18, Y_train18)
Y_SVM = dSVM.predict(X_test18)
list_akurasi_svm.append(accuracy_score(Y_test18, Y_SVM))
print(accuracy_score(Y_test18, Y_SVM))
print(precision_recall_fscore_support(Y_test18, Y_SVM, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")
print(len(list_akurasi_svm))


# In[55]:


# Random Forest
# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
from sklearn.ensemble import RandomForestClassifier

count = 0
list_akurasi_rf =list()
RandomForest = RandomForestClassifier()
RandomForest.fit(X_train1, Y_train1)
Y_RF = RandomForest.predict(X_test1)
list_akurasi_rf.append(accuracy_score(Y_test1, Y_RF))
print(accuracy_score(Y_test1, Y_RF))
print(precision_recall_fscore_support(Y_test1, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train2, Y_train2)
Y_RF = RandomForest.predict(X_test2)
list_akurasi_rf.append(accuracy_score(Y_test2, Y_RF))
print(accuracy_score(Y_test2, Y_RF))
print(precision_recall_fscore_support(Y_test2, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train3, Y_train3)
Y_RF = RandomForest.predict(X_test3)
list_akurasi_rf.append(accuracy_score(Y_test3, Y_RF))
print(accuracy_score(Y_test3, Y_RF))
print(precision_recall_fscore_support(Y_test3, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train4, Y_train4)
Y_RF = RandomForest.predict(X_test4)
list_akurasi_rf.append(accuracy_score(Y_test4, Y_RF))
print(accuracy_score(Y_test4, Y_RF))
print(precision_recall_fscore_support(Y_test4, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train5, Y_train5)
Y_RF = RandomForest.predict(X_test5)
list_akurasi_rf.append(accuracy_score(Y_test5, Y_RF))
print(accuracy_score(Y_test5, Y_RF))
print(precision_recall_fscore_support(Y_test5, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train6, Y_train6)
Y_RF = RandomForest.predict(X_test6)
list_akurasi_rf.append(accuracy_score(Y_test6, Y_RF))
print(accuracy_score(Y_test6, Y_RF))
print(precision_recall_fscore_support(Y_test6, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train7, Y_train7)
Y_RF = RandomForest.predict(X_test7)
list_akurasi_rf.append(accuracy_score(Y_test7, Y_RF))
print(accuracy_score(Y_test7, Y_RF))
print(precision_recall_fscore_support(Y_test7, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train8, Y_train8)
Y_RF = RandomForest.predict(X_test8)
list_akurasi_rf.append(accuracy_score(Y_test8, Y_RF))
print(accuracy_score(Y_test8, Y_RF))
print(precision_recall_fscore_support(Y_test8, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train9, Y_train9)
Y_RF = RandomForest.predict(X_test9)
list_akurasi_rf.append(accuracy_score(Y_test9, Y_RF))
print(accuracy_score(Y_test9, Y_RF))
print(precision_recall_fscore_support(Y_test9, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train10, Y_train10)
Y_RF = RandomForest.predict(X_test10)
list_akurasi_rf.append(accuracy_score(Y_test10, Y_RF))
print(accuracy_score(Y_test10, Y_RF))
print(precision_recall_fscore_support(Y_test10, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train11, Y_train11)
Y_RF = RandomForest.predict(X_test11)
list_akurasi_rf.append(accuracy_score(Y_test11, Y_RF))
print(accuracy_score(Y_test11, Y_RF))
print(precision_recall_fscore_support(Y_test11, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train12, Y_train12)
Y_RF = RandomForest.predict(X_test12)
list_akurasi_rf.append(accuracy_score(Y_test12, Y_RF))
print(accuracy_score(Y_test12, Y_RF))
print(precision_recall_fscore_support(Y_test12, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train13, Y_train13)
Y_RF = RandomForest.predict(X_test13)
list_akurasi_rf.append(accuracy_score(Y_test13, Y_RF))
print(accuracy_score(Y_test13, Y_RF))
print(precision_recall_fscore_support(Y_test13, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train14, Y_train14)
Y_RF = RandomForest.predict(X_test14)
list_akurasi_rf.append(accuracy_score(Y_test14, Y_RF))
print(accuracy_score(Y_test14, Y_RF))
print(precision_recall_fscore_support(Y_test14, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train15, Y_train15)
Y_RF = RandomForest.predict(X_test15)
list_akurasi_rf.append(accuracy_score(Y_test15, Y_RF))
print(accuracy_score(Y_test15, Y_RF))
print(precision_recall_fscore_support(Y_test15, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train16, Y_train16)
Y_RF = RandomForest.predict(X_test16)
list_akurasi_rf.append(accuracy_score(Y_test16, Y_RF))
print(accuracy_score(Y_test16, Y_RF))
print(precision_recall_fscore_support(Y_test16, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train17, Y_train17)
Y_RF = RandomForest.predict(X_test17)
list_akurasi_rf.append(accuracy_score(Y_test17, Y_RF))
print(accuracy_score(Y_test17, Y_RF))
print(precision_recall_fscore_support(Y_test17, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")

RandomForest.fit(X_train18, Y_train18)
Y_RF = RandomForest.predict(X_test18)
list_akurasi_rf.append(accuracy_score(Y_test18, Y_RF))
print(accuracy_score(Y_test18, Y_RF))
print(precision_recall_fscore_support(Y_test18, Y_RF, average='weighted'))
count += 1
print("--------------- Batas " + str(count) + " ---------------")


# In[56]:


kata_trending = list()
kata_trending.append("MAKING THE WORLD BRIGHT")
kata_trending.append("#JanganPercayaFPIMunafik")
kata_trending.append("#PeringatanGalonIsiUlangBPA")
kata_trending.append("#THEFIRSTSTEP_TREASUREEFFECT")
kata_trending.append("#RisalahAkhirTahun2020")
kata_trending.append("obl hilangkan izin berbelit")
kata_trending.append("#KhilafahAjaranIslam")
kata_trending.append("D3to2021 with iKON")
kata_trending.append("Rewind Indonesia 2020")
kata_trending.append("Pak Muh")
kata_trending.append("FPI Telah Berakhir")
kata_trending.append("#ByeByeDemocracy")
kata_trending.append("#ENHYPENonASC")
kata_trending.append("#StopTindakPidana")
kata_trending.append("#ENHYPEN ON AFTER SCHOOL CLUB")
kata_trending.append("#SpecialDJDoyoung")
kata_trending.append("Syafakillah")
kata_trending.append("Aa Gym")


# In[57]:


import matplotlib.pyplot as plt



for i in range (18):
    plt.figure(figsize=(9, 3))
    label_names = str(i + 1)
    names = ["nbc", "svm", "rf"]
    values = [list_akurasi_nbc[i] * 100, list_akurasi_svm[i] * 100, list_akurasi_rf[i] * 100]
    plt.subplot(131)
    plt.bar(names, values)
    plt.show()
    print("---------------" + str(i + 1) + " : " + kata_trending[i] + "---------------")


# In[ ]:




