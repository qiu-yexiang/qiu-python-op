import matplotlib.pyplot as plt
import matplotlib
import numpy as np
dic_={}
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']

data_names = ['性别','年龄','收入','教育','国内/外','是否每天登陆']

data_class=[['男','女']
    ,['35岁以上','18-25岁','26-35岁','18岁以下']
    ,['2-5万元','5-10万元','0-2万元','10万以上']
    ,['大学','高中','其他']
    ,['国外','国内']
    ,['否','是']]

data=[[0.60,0.40]
    ,[0.35,0.30,0.20,0.15]
    ,[0.40,0.30,0.15,0.15]
    ,[0.5,0.3,0.2]
    ,[0.7,0.3]
    ,[0.88,0.12]]
data_copy=[[0.60,0.40]
    ,[0.35,0.30,0.20,0.15]
    ,[0.40,0.30,0.15,0.15]
    ,[0.5,0.3,0.2]
    ,[0.7,0.3]
    ,[0.88,0.12]]

#堆积后的数据
for x in data:
    sum = 0
    for y in range(len(x)):
        a=x[y]
        if y==0:
            x[y]=1
        else:
            x[y]=1-sum
        sum += a
#画出更圆的圆   n边形
n=1080
stats=[]
for x in range(len(data_names)):
    key=data_names[x]
    y = data[x]
    for z in y :
        z=z*len(y)
        dics = {'性别': 0, '年龄': 0, '收入': 0, '教育': 0, '国内/外': 0, '是否每天登陆': 0}
        dics[key]=z
        dic_ = {}
        for i in range(len(data_names)):
            dic={}
            star = 0 + i * (n / len(data_names))
            end = (i + 1) * (n / len(data_names))
            if dics[data_names[i]] >0:
                dic = {f'{j}': z for j in range(int(star) , int(end)+1)}
            else:
                dic = {f'{j}': 0 for j in range(int(star) , int(end)+1)}
            dic_.update(dic)
        stats.append(dic_)
#画图
data_length = len(stats[0])
angles = np.linspace(0, 2 * np.pi, data_length, endpoint=False)
labels = [key for key in stats[0].keys()]
score = [[v for v in stat.values()] for stat in stats]
variable_names=[]
for i in range(len(stats)):
    variable_names.append(np.concatenate((score[i],[score[i][0]])))
angles = np.concatenate((angles, [angles[0]]))
labels = np.concatenate((labels, [labels[0]]))
fig = plt.figure(figsize=(9, 9), dpi=100)
ax = plt.subplot(111, polar=True)
for name in variable_names:
    ax.plot(angles, name)
    plt.fill(angles, name, alpha=0.5)
ax.set_thetagrids(angles * 180 / np.pi, labels)
plt.tick_params(labelbottom=False, labeltop=False, labelleft=False, labelright=False,
                bottom=False, top=False, left=False, right=False)
plt.axis('off')
ax.set_theta_zero_location('N')
# 设置雷达图的坐标刻度范围
ax.set_rlim(0, 4)
ax.set_title("堆积南丁格尔玫瑰图")
#拼接lengend
lengend = []
j=0
for x in data_class:
    for i in range(len(x)):
        lengend.append(f'{data_names[j]}' + f'{x[i]}')
    j += 1
j=0
for x in data_copy:
    for i in range(len(x)):
        lengend[j] = lengend[j] + f'{x[i]}'
        j +=1

plt.legend(lengend, loc='best')
plt.show()