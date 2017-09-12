import requests
import json
import time

"""

主要功能：

抓取 Python 四期同学仓库任务提交情况。

"""

__version__ = '170825 11:30_'
__author__ = 'zhuoxuan'




# check_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#
# start_issue = [10,43,67]
# end_issue = [13,46,70]

# 什么情况下应该定义函数
# 函数参数对应的是输入，上一个函数的输出 -》下一个函数的输入
# return 跟 print
# 函数间传参
# 全局变量
# 多个函数排序？

# --- 学习使用函数 ---
# 类似实例的感觉，怎么用就怎么写
# 如果需要在别的函数引用他的返回值，那就需要用 return 接收它

# --- Get ---

# 梳理逻辑、切片
# 明确输入、输出
# 明确各片段输入、输出如何衔接

# 从 txt 中读取所有学员名单，存为字典／列表

# 明确最终输入、输出
# 输入：章节名、开始 issue 、结束 issue --> 自动打印出四个大区已提交作业的名字、电话、邮件（输出：章节名、查询时间、

# 最终打印的形式
# 查询时间：** 打印程序运行时间        #  * 号为变量
# 章节：**
# 北京大区：已提交 ** 人        # 未来可增加定时查询、及定时查询增量的功能
# 已提交的同学：
# name, email, tel -- 问题：如何同时呈现 3 列数据（本次暂不处理 3 列，先复用已有 name + email）
# 长三角大区：已提交 ** 人
# 已提交的同学：
# name, email, tel -- 问题：如何同时呈现 3 列数据（本次暂不处理 3 列，先复用已有 name + email）

# 问题：如何识别不同大区 —— 当前通过固定的发布次序识别，可用，但逻辑不够稳定

# --> 将相关数据存入 txt （已有）
# 每查询一次存入一行，储存形式：date,chap,北京，长三角、珠三角、其它
# 问题：如果某函数运行后输出某章某地区的数据，如何将不同地区的数据写在同一行中存入 txt？（意识到函数更自由，可以连接不同的逻辑层级）
# --> 考虑更复杂的存储方式：     # 未来可考虑直接存为 csv 或 xls


# 逻辑输理
#
# 读取所有学员名单、得知总人数
# 计算单个 issue 下总 comment 人数、名单
# 用 所有学员名单、得知总人数 - 单个 issue 下总 comment 人数、名单
#
# 问题：这里有 2 条主线：一条是人数主线，一条是名单主线，如何更优雅地同时处理呢？  -> 目前：名字和数量同步处理；规范这 2 列数据命名也很重要。


def readfile(filename):
    all_stu = {}
    all_stu_list = []
    with open(filename,'r',encoding = 'utf-8') as f:
        for line in f.readlines():
            temp = line.strip('\n').split(',')
            all_stu.update({temp[0]:temp[1]})
            all_stu_list.append(temp[0])
    print('所有学员 GitHub Name:',all_stu_list)

# 包括工作人员、教练在内的所有评论者 (github name)
def all_comment_user(link):
    r = requests.get(link, auth=('iamzhuoxuan', ';U[6VMdC4NUCbJxp'))
    raw_comment_count = r.json()
    #print(json.dumps(raw_comment_count, sort_keys=True, indent=4))
    all_comment_user = []
    task_link = []
    count = 0
    for i in raw_comment_count:
        first_dict = i
        for k,v in first_dict.items():
            if k == 'user':
                second_dict = v
                count +=  1
                for k,v in second_dict.items():
                    if k == 'login':
                        all_comment_user.append(v)
    print('包括工作人员、教练在内的所有评论者:',all_comment_user)
    return all_comment_user

# 单个 Issue 下作业提交人／数量 -- 地区
def all_stu_comment_user(all_comment_user):
    print('总 comment：',len(all_comment_user))
    workmate = ['ouyangzhiping','badboy315','huijuannan','hscspring','ishanshan','yangshaoshun','RamyWu','scottming','bambooom','serena333','uniquenaer','Rebecca19','iamzhuoxuan','Mina-yy','LexieLee','AwesomeJason']
    py104oc = ['ZoomQuiet','zoejane','Wangjunyu','faketooth','wilslee','simpleowen','omclub','fatfox2016','gzMichael']
    all_non_stu = workmate + py104oc
    contrast_a = set(all_non_stu)
    contrast_b = set(all_comment_user)
    print('学员 comment 数：')
    all_stu_comment = list(contrast_b.difference(contrast_a))
    all_stu_comment_area_num = len(all_stu_comment)
    print(all_stu_comment_area_num)
    return all_stu_comment_area_num

# 一章有 4 个 issue
# 4 个大区  1n 2n 3n 4n
# 此函数是 4 个 issue 一次运行
def chap_allstu_name(start_issue,end_issue):
    area = '北京大区 长三角大区 珠三角大区 其它大区'.split( )  # 问题：列表对应元素(str 格式) 对应相加
    signal = 0
    for x in range(start_issue,end_issue+1):
        print(area[signal])
        link = 'https://api.github.com/repos/AIHackers/Py101-004/issues/'+str(x)+'/comments?page=1&per_page=100'
        a = all_comment_user(link)
        all_stu_comment_user(a)
        signal += 1
    return

#         #print(all_comment_user)
#         #print(task_link)
#
#         #print(all_non_stu)
#         #print('总 comment：')
#         #print(len(all_comment_user))
#         contrast_a = set(all_non_stu)
#         contrast_b = set(all_comment_user)
#
#         #print('学员 comment 数：')
#         all_stu_comment = list(contrast_b.difference(contrast_a))

#         all_stu_comment_area_num = len(all_stu_comment)
#         #print(all_stu_comment_area_num)
#         all_stu_comment_num.append(all_stu_comment_area_num)
#         #print(all_stu_comment,'all_stu_comment')
#         chap_allstu_name.extend(all_stu_comment)

#def writesave():

# 休息一下哈哈 ^_^


ch0 = chap_allstu_name(67,70)

# for i in range(len(start_issue)): # 按章节
#     chap_allstu_name = []
#     all_stu_comment_num = ['ch'+str(i),check_time]
#     print(all_stu_comment_num)
#     for x in range(start_issue[i],end_issue[i]+1):  # 4 个大区  1n 2n 3n 4n
#         r = requests.get('https://api.github.com/repos/AIHackers/Py101-004/issues/'+str(x)+'/comments?page=1&per_page=100', auth=('iamzhuoxuan', 't{vu.VvEFFPyWi42'))
#         print('https://api.github.com/repos/AIHackers/Py101-004/issues/'+str(x)+'/comments')
#         raw_comment_count = r.json()
#         #print(json.dumps(raw_comment_count, sort_keys=True, indent=4))
#         all_comment_user = []
#         task_link = []
#         count = 0
#         for i in raw_comment_count:
#             first_dict = i
#             for k,v in first_dict.items():
#                 if k == 'user':
#                     second_dict = v
#                     count +=  1
#                     for k,v in second_dict.items():
#                         if k == 'login':
#                             all_comment_user.append(v)
#                 if k == 'html_url':
#                     task_link.append(v)
#
#         #print(all_comment_user)
#         #print(task_link)
#
#         #print(all_non_stu)
#         #print('总 comment：')
#         #print(len(all_comment_user))
#         #print(len(task_link))
#         contrast_a = set(all_non_stu)
#         contrast_b = set(all_comment_user)
#
#         #print('学员 comment 数：')
#         all_stu_comment = list(contrast_b.difference(contrast_a))

#         all_stu_comment_area_num = len(all_stu_comment)
#         #print(all_stu_comment_area_num)
#         all_stu_comment_num.append(all_stu_comment_area_num)
#         #print(all_stu_comment,'all_stu_comment')
#         chap_allstu_name.extend(all_stu_comment)
#
#
#         #print(all_stu_comment)
#         #for i in all_stu_comment:
#         #    print(i)
#
#     #print(all_stu_comment_num)
#
#
#     print('-------- chap_allstu_name below------')
#     print(chap_allstu_name)
#     print(len(chap_allstu_name),'已交总人数')
#     print('--------upload------')
#
#     print(len(all_stu.keys())-len(chap_allstu_name),'人未提交作业')
#
#     for item in all_stu.keys():
#         if item not in chap_allstu_name:
#             print(item,',',all_stu[item])
#
#     record_file1 = open('all_stu_comment_num1.txt', 'a')
#
#     record_file1.write('\n')
#     for item in all_stu_comment_num:
#         record_file1.write("%s\n" % item)
#     record_file1.write('\n'+'-'*10)
#     record_file1.write('\n')
#
#     record_file2 = open('all_stu_comment_num2.txt', 'a')
#     record_file2.write("%s\n" % all_stu_comment_num)
#     #print('========')


# changelog
# v0.1.0 能够自动抓取、在 cli 打印某一章节任务完成人数（技术点：requests json 动态网页链接 阅读技术文档）
# v0.2.0 将抓取到的数据，写入 txt 文档，增加章节信息及查询时间信息
# v0.3.0 每周发布新任务后，简单改写列后，可自动读取所有章节完成人数
# v0.3.1 临时需求：计算各章未交作业名单，读取其邮箱 -> 嵌套越来越多了，要解决这个问题 -> 改装为函数
# 计划
# v0.3.2 封装为函数，依 PEP8 规范改写代码
