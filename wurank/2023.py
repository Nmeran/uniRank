import os
import json
import requests
import pandas as pd

dirpath = os.path.abspath(os.path.dirname(__file__))
df = pd.read_excel(dirpath + "/2023武书连大学排名.xlsx", usecols=[2, 4], names=None)  # 读取项目名称列,不要列名
df_li = df.values.tolist()
url='https://mallapi.wurank.net/RankApi/SearchApi/GetChineseUniDataPageList/chineseunidata'

def get_url(url):
    data = {
        "PageIndex": 1,
        "PageSize": 811,
        "filter": "intYear=2023",
        "sort": "intVictorOrder=0"
    }
    req = requests.post(url, json=data)
    req.encoding='utf-8'
    html = req.json()
    return html

dataset = get_url(url)['data']
print(dataset)
idx = len(dataset)
with open(dirpath + "/rk.json", "w", encoding = 'utf-8') as f:
    dict = []
    for i in range(idx):
        Rank = dataset[i]['victororder']
        UniName = dataset[i]['schchnname']
        Region = dataset[i]['provincename']
        Provinceorder = dataset[i]['provinceorder']
        Schtype = dataset[i]['schtype']
        Classorder =dataset[i]['classorder']
        TotalSource = dataset[i]['totalscore']
        Schselectorder = dataset[i]['schselectorder']
        Schselectlevel = dataset[i]['schselectlevel']
        Newstudorder = dataset[i]['newstudorder']
        Newstudlevel = dataset[i]['newstudlevel']
        Teachabilityorder = dataset[i]['teachabilityorder']
        Teachabilitylevel = dataset[i]['teachabilitylevel']
        Teachscoreorder = dataset[i]['teachscoreorder']
        Teachscorelevelr = dataset[i]['teachscorelevel']
        Paperorder = dataset[i]['paperorder']
        Paperlevel = dataset[i]['paperlevel']
        Classzkorder = dataset[i]['classzkorder']
        Classzklevel = dataset[i]['classzklevel']
        Classskorder = dataset[i]['classskorder']
        Classsklevel = dataset[i]['classsklevel']

        dict.append({"排名": Rank,
                "综合实力": TotalSource,
                "学校名称": UniName,
                "省份": Region,
                "省份排名": Provinceorder,
                "类型": Schtype,
                "类型排名": Classorder,
                "择校顺序": Schselectorder,
                "择校水平": Schselectlevel,
                     "新生质量排名": Newstudorder,
                     "新生质量": Newstudlevel,
                     "教师水平排名": Teachabilityorder,
                     "教师水平": Teachabilitylevel,
                     "教师绩效排名": Teachscoreorder,
                     "教师绩效": Teachscorelevelr,
                     "论文质量排名": Paperorder,
                     "论文质量": Paperlevel,
                     "自然科学排名": Classzkorder,
                     "自然科学": Classzklevel,
                     "社会科学排名": Classskorder,
                     "社会科学": Classsklevel
                })
    json.dump(dict, f, ensure_ascii=False, indent=4)
    f.close()
