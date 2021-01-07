#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import re
from textblob import TextBlob


# ### Naja

# In[2]:


api_key = "RZE2ePoGDOvOYV2T0kiok8CL7"
api_secret_key = "VF7LfzbEkOj5Mk3A4vizkSXZZiR5oDYYiNxTH78JJE3T6gMYvh"
access_token = "814060411548905472-GsbJdyItSgF8hfpPsofKEHQV2RgiflW"
access_token_secret = "8xgxwVBYazocQlEJid0KTKEbfkZB6CU84iltOLZxakrKO"


# ### Bima

# In[42]:


api_key = "RZE2ePoGDOvOYV2T0kiok8CL7"
api_secret_key = "VF7LfzbEkOj5Mk3A4vizkSXZZiR5oDYYiNxTH78JJE3T6gMYvh"
access_token = "814060411548905472-GsbJdyItSgF8hfpPsofKEHQV2RgiflW"
access_token_secret = "8xgxwVBYazocQlEJid0KTKEbfkZB6CU84iltOLZxakrKO"


# In[3]:


auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[4]:


top1_29des = api.search(q="MAKING THE WORLD BRIGHT", lang="id", count=100)
top2_29des = api.search(q="#JanganPercayaFPIMunafik", lang="id", count=100)
top3_29des = api.search(q="#PeringatanGalonIsiUlangBPA", lang="id", count=100)
top4_29des = api.search(q="#THEFIRSTSTEP_TREASUREEFFECT", lang="id", count=100)
top5_29des = api.search(q="#RisalahAkhirTahun2020", lang="id", count=100)
top6_29des = api.search(q="obl hilangkan izin berbelit", lang="id", count=100)
top7_29des = api.search(q="#KhilafahAjaranIslam", lang="id", count=100)
top8_29des = api.search(q="D3to2021 with iKON", lang="id", count=100)
top9_29des = api.search(q="Rewind Indonesia 2020", lang="id", count=100)
top10_29des = api.search(q="Pak Muh", lang="id", count=100)

top11_29des = api.search(q="FPI Telah Berakhir", lang="id", count=100)
top12_29des = api.search(q="#ByeByeDemocracy", lang="id", count=100)
top13_29des = api.search(q="#ENHYPENonASC", lang="id", count=100)
top14_29des = api.search(q="#StopTindakPidana", lang="id", count=100)
top15_29des = api.search(q="#ENHYPEN ON AFTER SCHOOL CLUB", lang="id", count=100)
top16_29des = api.search(q="#SpecialDJDoyoung", lang="id", count=100)
top17_29des = api.search(q="Syafakillah", lang="id", count=100)
top18_29des = api.search(q="Aa Gym", lang="id", count=100)


# In[5]:


print(len(top1_29des))
print(len(top2_29des))
print(len(top3_29des))
print(len(top4_29des))
print(len(top5_29des))
print(len(top6_29des))
print(len(top7_29des))
print(len(top8_29des))
print(len(top9_29des))
print(len(top10_29des))
print(len(top11_29des))
print(len(top12_29des))
print(len(top13_29des))
print(len(top14_29des))
print(len(top15_29des))
print(len(top16_29des))
print(len(top17_29des))
print(len(top18_29des))


# In[10]:


for i in range(2):
    teks = top1_29des[i].text
    print(teks)
    teks = str(teks)
    if("\n") in teks:
        teks = teks.replace("\n", " ")
    print(teks)
    print("----------")


# In[2]:


# # import json

# d_f = open("crawl_1.txt", "r", encoding='utf-8')
# isi_d_f = (d_f.readline())
# # # isi_dict = ast.literal_eval(isi_d_f)
# # js = json.loads(isi_d_f) 
# # print(type(js))
# print(isi_d_f)
# d_f.close()


# In[49]:


# import json

d_f = open("./crawl/crawl_1.txt", "r", encoding='utf-8')
isi_d_f = (d_f.readline())
# # isi_dict = ast.literal_eval(isi_d_f)
# js = json.loads(isi_d_f) 
# print(type(js))
print(isi_d_f)
d_f.close()


# ### Top 1

# In[6]:


cek_in = list()
nama_file = "./crawl/crawl_1.txt"
nama_file_unik = "./crawlId/crawlId_1.txt"
total = 0
for i in range (len(top1_29des)):
    f = open(nama_file_unik, "r")
    if(top1_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
    f.close()
print(total)


# In[7]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top1_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top1_29des[i].text
        f.write(str(top1_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1   
print(total)
print("----------------------------------------")
f.close()
d_f.close()


# ### Top 2

# In[8]:


cek_in = list()
nama_file = "./crawl/crawl_2.txt"
nama_file_unik = "./crawlId/crawlId_2.txt"
total = 0
for i in range (len(top2_29des)):
    f = open(nama_file_unik, "r")
    if(top2_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[9]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top2_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top2_29des[i].text
        f.write(str(top2_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()
        


# ### Top 3

# In[10]:


cek_in = list()
nama_file = "./crawl/crawl_3.txt"
nama_file_unik = "./crawlId/crawlId_3.txt"
total = 0
for i in range (len(top3_29des)):
    f = open(nama_file_unik, "r")
    if(top3_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[11]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top3_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top3_29des[i].text
        f.write(str(top3_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()


# ### Top 4

# In[12]:


cek_in = list()
nama_file = "./crawl/crawl_4.txt"
nama_file_unik = "./crawlId/crawlId_4.txt"
total = 0
for i in range (len(top4_29des)):
    f = open(nama_file_unik, "r")
    if(top4_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[13]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top4_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top4_29des[i].text
        f.write(str(top4_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()


# ### Top 5

# In[14]:


cek_in = list()
nama_file = "./crawl/crawl_5.txt"
nama_file_unik = "./crawlId/crawlId_5.txt"
total = 0
for i in range (len(top5_29des)):
    f = open(nama_file_unik, "r")
    if(top5_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[15]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top5_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top5_29des[i].text
        f.write(str(top5_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()


# ### Top 6

# In[16]:


cek_in = list()
nama_file = "./crawl/crawl_6.txt"
nama_file_unik = "./crawlId/crawlId_6.txt"
total = 0
for i in range (len(top6_29des)):
    f = open(nama_file_unik, "r")
    if(top6_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[17]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top6_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top6_29des[i].text
        f.write(str(top6_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()


# ### Top 7

# In[18]:


cek_in = list()
nama_file = "./crawl/crawl_7.txt"
nama_file_unik = "./crawlId/crawlId_7.txt"
total = 0
for i in range (len(top7_29des)):
    f = open(nama_file_unik, "r")
    if(top7_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[19]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top7_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top7_29des[i].text
        f.write(str(top7_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()


# ### Top 8

# In[20]:


cek_in = list()
nama_file = "./crawl/crawl_8.txt"
nama_file_unik = "./crawlId/crawlId_8.txt"
total = 0
for i in range (len(top8_29des)):
    f = open(nama_file_unik, "r")
    if(top8_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[21]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top8_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top8_29des[i].text
        f.write(str(top8_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()


# ### Top 9

# In[22]:


cek_in = list()
nama_file = "./crawl/crawl_9.txt"
nama_file_unik = "./crawlId/crawlId_9.txt"
total = 0
for i in range (len(top9_29des)):
    f = open(nama_file_unik, "r")
    if(top9_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[23]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top9_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top9_29des[i].text
        f.write(str(top9_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()


# ### Top 10

# In[24]:


cek_in = list()
nama_file = "./crawl/crawl_10.txt"
nama_file_unik = "./crawlId/crawlId_10.txt"
total = 0
for i in range (len(top10_29des)):
    f = open(nama_file_unik, "r")
    if(top10_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[25]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top10_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top10_29des[i].text
        f.write(str(top10_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()
        


# ### Top 11

# In[26]:


cek_in = list()
nama_file = "./crawl/crawl_11.txt"
nama_file_unik = "./crawlId/crawlId_11.txt"
total = 0
for i in range (len(top11_29des)):
    f = open(nama_file_unik, "r")
    if(top11_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[27]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top11_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top11_29des[i].text
        f.write(str(top11_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()
        


# ### Top 12

# In[28]:


cek_in = list()
nama_file = "./crawl/crawl_12.txt"
nama_file_unik = "./crawlId/crawlId_12.txt"
total = 0
for i in range (len(top12_29des)):
    f = open(nama_file_unik, "r")
    if(top12_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[29]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top12_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top12_29des[i].text
        f.write(str(top12_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()
        


# ### Top 13

# In[30]:


cek_in = list()
nama_file = "./crawl/crawl_13.txt"
nama_file_unik = "./crawlId/crawlId_13.txt"
total = 0
for i in range (len(top13_29des)):
    f = open(nama_file_unik, "r")
    if(top13_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[31]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top13_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top13_29des[i].text
        f.write(str(top13_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()
        


# ### Top 14

# In[32]:


cek_in = list()
nama_file = "./crawl/crawl_14.txt"
nama_file_unik = "./crawlId/crawlId_14.txt"
total = 0
for i in range (len(top14_29des)):
    f = open(nama_file_unik, "r")
    if(top14_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[33]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top14_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top14_29des[i].text
        f.write(str(top14_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()
        


# ### Top 15

# In[34]:


cek_in = list()
nama_file = "./crawl/crawl_15.txt"
nama_file_unik = "./crawlId/crawlId_15.txt"
total = 0
for i in range (len(top15_29des)):
    f = open(nama_file_unik, "r")
    if(top15_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[35]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top15_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top15_29des[i].text
        f.write(str(top15_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()
        


# ### Top 16

# In[36]:


cek_in = list()
nama_file = "./crawl/crawl_16.txt"
nama_file_unik = "./crawlId/crawlId_16.txt"
total = 0
for i in range (len(top16_29des)):
    f = open(nama_file_unik, "r")
    if(top16_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[37]:




f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top16_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top16_29des[i].text
        f.write(str(top16_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()
        


# ### Top 17

# In[38]:


cek_in = list()
nama_file = "./crawl/crawl_17.txt"
nama_file_unik = "./crawlId/crawlId_17.txt"
total = 0
for i in range (len(top17_29des)):
    f = open(nama_file_unik, "r")
    if(top17_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[39]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top17_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top17_29des[i].text
        f.write(str(top17_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()
        


# ### Top 18

# In[40]:


cek_in = list()
nama_file = "./crawl/crawl_18.txt"
nama_file_unik = "./crawlId/crawlId_18.txt"
total = 0
for i in range (len(top18_29des)):
    f = open(nama_file_unik, "r")
    if(top18_29des[i].id_str in f.read()):
        cek_in.append("1")
    else:
        cek_in.append("0")
        total += 1
#         print("belum ada : " + str(top1_29des[i].id_str))
    f.close()
print(total)


# In[41]:


f = open(nama_file_unik, "a+")
d_f = open(nama_file, "a+", encoding='utf-8')
total = 0
for i in range (len(top18_29des)):
    if(cek_in[i] == '0'):
        tweet_properties = {}
        tweet_properties["isi_tweet"] = top18_29des[i].text
        f.write(str(top18_29des[i].id_str))
        f.write("\n")
        d_f.write(str(tweet_properties))
        d_f.write("\n")
        total += 1
        
print(total)
print("----------------------------------------")
f.close()
d_f.close()
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[32]:


nama_file = "crawl_" + str(count) + ".txt"
nama_file_id = "crawlId_" + str(count) + ".txt"

with open(nama_file, 'a+') as file:
#     for tweet in top1_29des:
        f = open(nama_file_id, "a+")
        for i in range (2):
            print(f.readlines())
            print("-------------")
            print(top1_29des[0].id_str)
            if top1_29des[0].id_str in f.read():
                print("sudah ada")
    #             continue
            else:
                print("belom ada")
                f.write("%s\n" % top1_29des[0].id_str)
        f.close()
    #         break


# In[6]:


#Emoji patterns
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)


# In[17]:


top1_29desAnalisis = []
top2_29desAnalisis = []
top3_29desAnalisis = []
top4_29desAnalisis = []
top5_29desAnalisis = []
top6_29desAnalisis = []
top7_29desAnalisis = []
top8_29desAnalisis = []
top9_29desAnalisis = []
top10_29desAnalisis = []
top11_29desAnalisis = []
top12_29desAnalisis = []
top13_29desAnalisis = []
top14_29desAnalisis = []
top15_29desAnalisis = []
top16_29desAnalisis = []
top17_29desAnalisis = []
top18_29desAnalisis = []

hasil_sentiment_pos = 0
hasil_sentiment_net = 0
hasil_sentiment_neg = 0

count = 1
nama_file = "crawl_" + str(count) + ".txt"
nama_file_id = "crawlId_" + str(count) + ".txt"

with open(nama_file, 'a+') as file:
    for tweet in top1_29des:
        f = open(nama_file_id, "a+")
        f.read()
        if tweet.id_str in f.read():
            print("sudah ada")
            continue
        else:
            print("belom ada")
            f.write("%s\n" % tweet.id_str)
        f.close()
        tweet_properties = {}
        tweet_properties["tanggal_tweet"] = tweet.created_at
        tweet_properties["pengguna"] = tweet.user.screen_name
        tweet_bersih = tweet.text
        # print(tweet_bersih)
        # SELEKSI KOMENTAR dari Retweet dihilangkan
        # check if the tweet starts with the format for a retweet 
        if tweet_bersih.startswith("RT @") == True:
            print("skip")
            # print("skip : " + tweet_bersih)
            continue
        print("Awal : " + tweet_bersih)  

        # MENGHILANGKAN EMOJI
        #remove emoji from tweet
        tweet_bersih = emoji_pattern.sub(r'', tweet_bersih)
        # print("emoticon : " + tweet_bersih)  

        # NORMALISASI KALIMAT (mengubah menjadi lower case)
        tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
        # print("normalisasi : " + tweet_bersih)

        # CLEANSING (menghilangkan @, url, email, website)
        tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet.text).split())
        print("cleansing : " + tweet_bersih)

        tweet_properties["isi_tweet"] = tweet_bersih
#         tweet_properties["isi_tweet"] = tweet.id_str
        top1_29desAnalisis.append(tweet_properties)
        file.write(str(tweet_properties))


# In[85]:


hasilAnalisis = []
for tweet in hasilSearch:
    tweet_properties = {}
    tweet_properties["tanggal_tweet"] = tweet.created_at
    tweet_properties["pengguna"] = tweet.user.screen_name
    
    tweet_bersih = tweet.text
    
    # could go without this variable it just makes it easier
#     tweet_bersih = str(tweet_bersih.lower().encode('ascii',errors='ignore'))
#     print(tweet_bersih)
    # check if the tweet starts with the format for a retweet
    if tweet_bersih.startswith("RT @") == True:
        print(tweet_bersih)
        continue
        
    tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet.text).split())
    tweet_properties["isi_tweet"] = tweet_bersih
#     print(tweet_bersih)
#     analysis = TextBlob(tweet_bersih)
    
#     try:
#         analysis = analysis.translate(to="en")
#     except Exception as e:
#         print(e)
    
#     if analysis.sentiment.polarity > 0.0:
#         tweet_properties["sentimen"] = "positif"
#     elif analysis.sentiment.polarity == 0.0:
#         tweet_properties["sentimen"] = "netral"
#     else:
#         tweet_properties["sentimen"] = "negatif"
    
    
    if tweet.retweet_count > 0:
        if tweet_properties not in hasilAnalisis:
            hasilAnalisis.append(tweet_properties)
    else:
        hasilAnalisis.append(tweet_properties)


# In[86]:


print(len(hasilAnalisis))


# In[87]:


for tweet in hasilAnalisis:
    print(tweet["tanggal_tweet"])
#     print(tweet["pengguna"])
    print(tweet["isi_tweet"])
    print("-------------------------------------------------------")


# In[19]:


tweet_positif = [t for t in hasilAnalisis if t["sentimen"]=="positif"]
tweet_netral = [t for t in hasilAnalisis if t["sentimen"]=="netral"]
tweet_negatif = [t for t in hasilAnalisis if t["sentimen"]=="negatif"]


# In[21]:


print("Hasil Sentimen")
print("positif: ", len(tweet_positif))
print("netral: ", len(tweet_netral))
print("negatif: ", len(tweet_negatif))


# In[27]:


tweet_negatif


# In[ ]:




