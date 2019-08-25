
import requests,csv,json,time
f = open('lagou.csv','w',newline='',encoding='utf-8')
write = csv.writer(f)
write.writerow(['公司','职位','城市','行业','职业技能','工作年限','薪资','融资情况'])
headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput='
}
url_1 = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput='
url_2 = 'https://www.lagou.com/jobs/positionAjax.json'
params ={'needAddtionalResult': 'false'}
skill_list=[]
for i in range(30):
    data = {
    'first': 'false',
    'pn': str(i+1),
    'kd': '数据分析',
    }
    s = requests.Session()
    s.get(url_1, headers=headers)  # 请求首页获取cookies
    #time.sleep(5)
    res = s.post(url_2,headers = headers,params=params,data=data)
    position = res.json()
    #print(position)
    list_all = position['content']['positionResult']['result']
    for list in list_all:
        company = list['companyShortName']
        position = list['positionName']
        city = list['city']
        industryField = list['industryField']
        skillLables = list['skillLables']
        for j in skillLables:
                skill_list.append(j)
        workYear = list['workYear']
        salary = list['salary']
        financeStage = list['financeStage']
        write.writerow([company,position,city,industryField,skillLables,workYear,salary,financeStage])
f.close()




    