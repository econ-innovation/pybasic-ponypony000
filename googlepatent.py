
import json
import sys
print(sys.argv)

with open("google100.txt","r") as f:
    for pt in f.readlines() :    #逐行读入成字符串pt
        patent = json.loads(pt)  #字符串形成字典
        filing_date = patent.get("filing_date", "")
        publication_date = patent.get("publication_date", "")  #get() 函数用于字典返回指定键的值，如果不存在则返回空字符串 ""
        grant_date = patent.get("grant_date", "")
        priority_date = patent.get("priority_date", "")
        with open('googlepatent.txt', 'a') as fs:
            fs.write(f"{filing_date}|{publication_date}|{grant_date}|{priority_date}\n")

#命令行运行
# #!/usr/bin/python3
# python3 googlepatent.py "/Users/mawenting/Documents/Bigdata_econ/mypython/google100.txt"