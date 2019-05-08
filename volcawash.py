import re
import xlwt
with open("V:\OneDrive - zju.edu.cn\Code\python\\volcaspider\\a.txt",'r',encoding='utf-8') as f:
    line=f.read()
rawlist=line.split('<entry>')
#print(rawlist[1])
datalist=[]
for i in range(1,len(rawlist)):
    match_word=re.search(r'<word>(.*)</word>',rawlist[i],re.M|re.I)
    match_pron=re.search(r'<pronunciation>(.*)</pronunciation>',rawlist[i],re.M|re.I)
    match_parts=re.search(r'<parts_of_speech>(.*)</parts_of_speech>',rawlist[i],re.M|re.I)
    match_chs=re.search(r'<chinese>(.*)</chinese>',rawlist[i],re.M|re.I)
    datalist.append([match_word.group()[15:-10],match_pron.group()[23:-18],match_parts.group()[17:-18],match_chs.group()[18:-13]])
print(datalist)
xlsname='D:/vocabulary.xls'
linecount=0
workbook=xlwt.Workbook(encoding='ascii')
worksheet=workbook.add_sheet('raw')
for i in datalist:
    for j in range(0,4):
        worksheet.write(linecount,j,i[j])
    linecount=linecount+1
workbook.save(xlsname)