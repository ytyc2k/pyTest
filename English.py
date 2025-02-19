class EngDic:
    def __init__(self):
        self.fix=['n','v','vi','vt','int','art','adj','adv','num','conj','prep','pl','abbr']
        self.wordsList = self.GetLib()
        self.lenth=len(self.wordsList)

    def GetLib(self):
        dic = {}
        k = m = 0
        fn='./ESL6.txt'
        with open(fn, encoding='utf-8') as f:
            for line in f:
                k = k + 1   # k是行号
                if line[:2]=='英 ':
                    dic.setdefault(k) #用行号做key
                    m = k
                if '. ' in line[:5] and line[:line.find('.')] in self.fix: # 前5个字母中含有‘. '，并且包含在词性列表self.fix中
                    dic[m] = k
        for x in dic:
            if dic[x] == None:
                dic[x] = x + 1
        ku = []
        with open(fn, encoding='utf-8') as f:
            for line in f:
                ku.append(line.split('\n')[0].split('\u3000')[0])
        return [ku[x - 2:y] for x, y in dic.items()]

    def Getrandom(self):
        return random.choice(self.wordsList)

    def GetNrandom(self):
        n=random.randint(1,self.lenth)
        return n,self.wordsList[n]

    def Cn2En(self):
        n,lst= self.GetNrandom()
        return n,lst[2:]+lst[:2]

import sys
sys.stdout.reconfigure(encoding='utf-8')
import random
import time
import json
if __name__ == '__main__':
    En = EngDic()
    edic={}
    for k in En.wordsList:
        edic[k[0]]={"phonetic":k[1].replace('英','').replace('美','').replace(' ',''),"translation":'  '.join(k[2:])}
    # print(En.lenth,En.wordsList[-1],type(En))
    with open("ENG.json", "w", encoding="utf-8") as f:
        json.dump(edic, f, ensure_ascii=False, indent=4)  # `indent=4` 使 JSON 格式化更易读
    # for i in range(1,51):
    #     # print(f'{i:02}----->',*En.GetNrandom())
    #     print(f'{i:02}----->',*En.Cn2En())
    #     # print(f'{i:02}----->',En.wordsList[-i])
    #     time.sleep(10)

    # for i in En.wordsList:
    #     if i[0]=='privilege':
    #         print(i)


