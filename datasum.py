import pandas as pd
import numpy as np
import csv
df=pd.read_csv('2013.csv',encoding='gbk')
print(df.loc[0:1])
# df=pd.read_csv('edudata2.csv',encoding='gbk')
# df20=df.loc[0:82]
# df19=df.loc[83:522]
# df18=df.loc[523:1212]
# df17=df.loc[1213:1857]
# df16=df.loc[1858:2519]
# df15=df.loc[2520:3180]
#
# # 统计每年各方面的公司数量
#
#
# def count_1(dfpy,start):
#     dy={}
#     for i in range(start,start+dfpy.shape[0]):
#         for j in range(7,10):
#             if dfpy.loc[i][j] in dy.keys():
#                 dy[dfpy.loc[i][j]]=dy[dfpy.loc[i][j]]+1
#             else:
#                 dy[dfpy.loc[i][j]]=1
#     if '教育' in dy.keys():
#         del dy['教育']
#     del dy[np.nan]
#     dy2=dy.copy()
#     for k in dy2.keys():
#         if dy[k] < 10:
#             del dy[k]
#     return dy2,dy
#
#
# dy201,dy2011=count_1(df20,0)
# dy2012=dy201.copy()
# for k in dy2012.keys():
#     if dy201[k] < 2:
#         del dy201[k]
# _,dy191=count_1(df19,83)
# _,dy181=count_1(df18,523)
# _,dy171=count_1(df17,1213)
# _,dy161=count_1(df16,1858)
# _,dy151=count_1(df15,2520)
#
# # 统计每年的投资轮次
# lunci_s = ["天使轮","种子轮","Pre-A轮","A轮","A+轮","Pre-B轮","B轮","B+轮","C轮","C+轮","D轮","D+轮","E轮","F轮-上市前","战略投资"]
#
#
# def count_2(dfpy,start):
#     dy={}
#     for i in range(start,start+dfpy.shape[0]):
#         if dfpy.loc[i][3] in dy.keys():
#             dy[dfpy.loc[i][3]]=dy[dfpy.loc[i][3]]+1
#         else:
#             dy[dfpy.loc[i][3]]=1
#     for j in lunci_s:
#         if j in dy.keys():
#             continue
#         else:
#             dy[j]=0
#     return dy
#
#
# dy202=count_2(df20,0)
# dy192=count_2(df19,83)
# dy182=count_2(df18,523)
# dy172=count_2(df17,1213)
# dy162=count_2(df16,1858)
# dy152=count_2(df15,2520)
#
# stageone={"天使轮":1,"种子轮":1}
# stagetwo={"Pre-A轮":1,"A轮":1,"A+轮":1,"Pre-B轮":1,"B轮":1,"B+轮":1}
# stagethree={"C轮":1,"C+轮":1,"D轮":1,"D+轮":1,"E轮":1,"F轮-上市前":1}
# stage=[stageone,stagetwo,stagethree]
#
# def stagecount(dfpy,start):
#     dy1={}
#     dy2={}
#     dy3={}
#     dy=[dy1,dy2,dy3]
#     dy2=dy.copy()
#     for k in range(0,3):
#         currentstage=stage[k]
#         for i in range(start,start+dfpy.shape[0]):
#             if dfpy.loc[i][3] in currentstage.keys():
#                 for j in range(7,10):
#                     if dfpy.loc[i][j] in dy[k].keys():
#                         dy[k][dfpy.loc[i][j]] = dy[k][dfpy.loc[i][j]] + 1
#                     else:
#                         dy[k][dfpy.loc[i][j]] = 1
#             else:
#                 continue
#         if '教育' in dy[k].keys():
#             del dy[k]['教育']
#         del dy[k][np.nan]
#         dy2[k]=dy[k].copy()
#         dy[k]["其他"]=0
#         if k==2:
#             for ke in dy2[k].keys():
#                 if dy[k][ke] < 2:
#                     dy[k]["其他"] = dy[k]["其他"] + dy[k][ke]
#                     del dy[k][ke]
#         else:
#             for ke in dy2[k].keys():
#                 if dy[k][ke] < 10:
#                     dy[k]["其他"]= dy[k]["其他"]+dy[k][ke]
#                     del dy[k][ke]
#     return dy2,dy
#
#
# dy203,dy2032=stagecount(df20,0)
# dy1932,dy193=stagecount(df19,83)
# dy1832,dy183=stagecount(df18,523)
# dy1732,dy173=stagecount(df17,1213)
# dy1632,dy163=stagecount(df16,1858)
# dy1532,dy153=stagecount(df15,2520)
#
#
