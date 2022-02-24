import requests
from bs4 import BeautifulSoup

arquivo = open('arq01.csv','w')
arquivo.write("")
arquivo.close()

arquivo = open('arq01.csv','a', encoding="utf-8")
def filter(index, datas):
    nickname = None
    power = None
    guild = None
    names = []
    for data in datas:
        if ',' in data:
            power = data
        try:
            v = float(data)
        except Exception:
            if '\n' in data and len(data) > 3:
                data = data.rstrip('\n')
                data = data.lstrip('\n')
                data = data.lstrip('\n')
                names.append(data)
                nickname = data
            elif ',' not in data and len(data) > 3:
                names.append(data)

    for name in names:
        if name != nickname:
            guild = name
    
    arquivo.write(f"{index},: {nickname} , {power} , {guild}\n")
    
    #print(f"{index}: {nickname} - {power} - {guild}")
    
    
    data = {
            "index": index,
            "nickname":nickname,
            "power":power,
            "guild":guild,
        }
    

index = 0

for page in range(1, 11):
    url = f"https://forum.mir4global.com/rank?ranktype=1&worldgroupid=15&worldid=181&classtype=&searchname=&loaded=1&liststyle=ol&page={page}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    datas = []
    for span in soup.find_all('span'):
        value = span.get_text()
        datas.append(value)
        if len(datas) == 8:
            index += 1
            filter(index, datas)
            datas = []

arquivo.close()