import requests
#word=input('Input a word...')
r=requests.get('http://www.unsv.com/app/Center/%7B7461512a-5b69-4c1d-ac43-928977c39aca%7D/words.asp?username=&password=&member_id=-1&id=-1&goal_id=15&subgoal_id=-1&page=1&search=&size=7069&order=id&creator=-1&verified=all&spell=all&pronunciation=all&listen=all&speak=all&read=all&write=all&sentences=all&scan=off&adult=0&cacheTime=12')
with open('D:/a.txt','w',encoding='utf-8') as f:
    f.write(r.text)
print(r.text)