#coding="utf-8"

import sys
import json

def findStartIndex(data):
    startIndex = data.find(b'{"product":"')
    while startIndex % 16 != 0:
        startIndex = data.rfind(b'{', 0, startIndex)
    return startIndex

def readFinger(data, startIndex):
    endIndex = data.find(b'\x00', startIndex)
    return data[startIndex:endIndex]

def main(binPath):
    output = list()
    with open(binPath, 'rb') as f:
        data = f.read()
        startIndex = findStartIndex(data)
        resultData = readFinger(data, startIndex)
        results = resultData.split(b'\x0a')
        for result in results:
            try:
                jsonData = json.loads(result)
                output.append({"product": jsonData["product"], "rule":jsonData["rule"]})
            except:
                continue

    with open('output.txt', 'wt', encoding="utf-8") as w:
        for item in output:
            json.dump(item , w , ensure_ascii=False)
            w.write('\n')

def readme():
    print("使用方法：")
    print("python getgobybinfinger.py goby-cmd.exe")

if __name__ == "__main__":
    if (len(sys.argv) >= 2):
        main(sys.argv[1])
    else:
        readme()
