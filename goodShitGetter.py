import praw
import pandas as pd
import datetime as dt
import xlrd
import cv2
import requests
import shutil



def red(sub, path = ''):
    reddit = praw.Reddit(client_id='3ccBL-zL5f9haw', \
                         client_secret=None, \
                         user_agent='A normal App', \
                         username='PinkCatCup', \
                         password='GGpass11')
    subreddit = reddit.subreddit(sub)
    getSub(subreddit,path)
#f = open('Output.txt','a')
#for i in subreddits.search_by_name('pp'):
#    f.write(str(i)+"\n")
#f.close()

#title = []
#file = 'RedditContent.xlsx'
#wb = xlrd.open_workbook('RedditContent.xlsx')
#sheet = wb.sheet_by_index(0) 
#
#sub_id = []
#for i in range(1, sheet.nrows):
#    sub_id.append(str(sheet.cell_value(i, 2)))
#for i in range (229, len(sub_id)):
#    file = 'Output' + str(i) + '.txt'
#    f = open(file ,'a', encoding='utf-8')
#    sub = reddit.submission(id = sub_id[i])
#    sub.comments.replace_more(limit=None)
#    for comment in sub.comments.list():
#        f.write(str(comment.body))
#    f.close()
#    print(i, len(sub.comments.list()), len(sub.comments))

def getSub(subm, path = ''):
    top_subreddit = subm.new()
    topics_dict = { "title":[], 
                    "score":[], 
                    "id":[], "url":[], 
                    "comms_num": [], 
                    "created": [], 
                    "body":[]}

    for sub in top_subreddit:
        topics_dict["title"].append(sub.title)
        topics_dict["score"].append(sub.score)
        topics_dict["id"].append(sub.id)
        topics_dict["url"].append(sub.url)
        topics_dict["comms_num"].append(sub.num_comments)
        topics_dict["created"].append(sub.created)
        topics_dict["body"].append(sub.selftext)
    res = requests.get(topics_dict["url"][0], stream = True)
    if path != '':
        path +='\\'
    local_file = open(path+'local_image.jpg', 'wb')
    res.raw.decode_content = True
    shutil.copyfileobj(res.raw, local_file)
#    topics_data = pd.DataFrame(topics_dict)
#    topics_data.to_excel(name+'.xlsx', sheet_name='SE', index=False)
red(sub = 'pics', path = 'E:\\157239n')



