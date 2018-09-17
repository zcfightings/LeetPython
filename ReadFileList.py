
import os
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    path = []
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        path.append(child)
    return path

def readFile(filename):
    
    if os.path.isfile(filename):
        fwrite = open('/Users/didi/zhaochen/in.txt','w')
        fopen = open(filename, 'r')
        for eachLine in fopen:
            arr = eachLine.split('\t')
            if arr[5]  in arr[1] or arr[1]  in arr[5]:
                fwrite.write(eachLine)
        fwrite.close()
        fopen.close()

if __name__ == '__main__':
    dirs = eachFile('/Users/didi/zhaochen/data/')
    for path in dirs:
        print(path)
        readFile(path)



