import requests
import re
import xlwt

def getpages(type,pages,name,workbook):
    xlsname='zhan_vocabulary.xls'
    sheet=workbook.add_sheet(name)
    linecount=0
    for i in range(1,pages+1):
        url='https://top.zhan.com/vocab/vocabulary/get-voca-list.html?list_type=0&get_type=2&test_type=1&corpus_id='+type+'&sortRule=word%2Casc&frequency=0&core=0&page='+str(i)
        s=requests.Session()
        r=s.get(url)
        null=''
        #print(eval(r.text)['rows'])
        rawlist=eval(r.text)['rows']
        for wordreg in rawlist:
            rowindex=0
            sheet.write(linecount,rowindex,label=wordreg['word'])
            rowindex+=1
            sheet.write(linecount,rowindex,label=wordreg['toefl_frequency'])
            rowindex+=1
            sheet.write(linecount,rowindex,label=wordreg['toefl_core'])
            rowindex+=1
            sheet.write(linecount,rowindex,label=wordreg['bref'])
            rowindex+=1
            sheet.write(linecount,rowindex,label=wordreg['toefl_bref'])
            rowindex+=1
            sheet.write(linecount,rowindex,label=wordreg['bref_en'])
            rowindex+=1
            sheet.write(linecount,rowindex,label=wordreg['toefl_bref_en'])
            rowindex+=1
            sheet.write(linecount,rowindex,label=wordreg['pron_uk'])
            rowindex+=1
            sheet.write(linecount,rowindex,label=wordreg['pron_us'])
            linecount+=1
    workbook.save(xlsname)
    print(name+'done...')
    return None
dataworkbook=xlwt.Workbook(encoding='ascii')

getpages('015%2C62',8,'人类学',dataworkbook)
getpages('026%2C54%2C108%2C115%2C235',14,'历史',dataworkbook)
getpages('063%2C180',5,'哲学',dataworkbook)
getpages('020%2C53%2C93%2C106%2C112%2C147',13,'商业',dataworkbook)
getpages('029',4,'心理学',dataworkbook)
getpages('030',10,'社会学',dataworkbook)
getpages('028%2C114',18,'考古学',dataworkbook)
getpages('014%2C201',11,'农业',dataworkbook)
getpages('021%2C64',7,'化学',dataworkbook)
getpages('025',15,'地理学',dataworkbook)
getpages('0140%2C144%2C234',13,'地质',dataworkbook)
getpages('027%2C119%2C200',4,'气象学',dataworkbook)
getpages('0173%2C183',6,'物理学',dataworkbook)
getpages('052%2C133%2C141%2C182',6,'环科',dataworkbook)
getpages('023',3,'生态学',dataworkbook)
getpages('0118%2C128',3,'科技',dataworkbook)
getpages('066%2C186',10,'动物学',dataworkbook)
getpages('019%2C57',11,'植物学',dataworkbook)
getpages('060',3,'海洋生物学',dataworkbook)
getpages('018',48,'生物学',dataworkbook)
getpages('061',7,'建筑学',dataworkbook)
getpages('055%2C137%2C187%2C233',6,'文学',dataworkbook)
getpages('016%2C95%2C117%2C134%2C205%2C210',16,'艺术',dataworkbook)
getpages('0175',11,'艺术类',dataworkbook)
