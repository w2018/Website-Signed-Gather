import cunhua,jiji,Douyu,configparser,hashlib
from urllib import parse

config = configparser.RawConfigParser()
config.read('Setting.conf', encoding='utf-8-sig')

# Setting

dDouyu = config.get('Setting','douyu')
cCunhua = config.get('Setting','cunhua')
jJiji = config.get('Setting','jiji')




# cunhua

cunhuaUser = None
cunhuaPassWord = None
if cCunhua == '1':
    cunhuaUser = config.get('cunhua','User')
    cunhuaUser = parse.quote(cunhuaUser)
    cunhuaPassWord = config.get('cunhua','PassWord')
    m = hashlib.md5()
    m.update(cunhuaPassWord.encode())
    str_md5 = m.hexdigest()
    cunhuaPassWord = str_md5


# jiji
jijiUser = None
jijiPassWord = None
if jJiji == '1':
    jijiUser = config.get('jiji','User')
    jijiUser = parse.quote(jijiUser)
    jijiPassWord = config.get('jiji','PassWord')

# douyu

douyuCookie = None
douyuList = None
douyuNum = None
douyuSum = None

if dDouyu == '1':
    douyuCookie = config.get('douyu','cookie')
    oldlist = config.get('douyu','list')
    douyuList = str(oldlist).split('-')
    oldnum = config.get('douyu','num')
    douyuNum = str(oldnum).split('-')
    oldSum = config.get('douyu','sum')
    douyuSum = int(oldSum)




if __name__ == '__main__':
    if dDouyu == '1':
        Douyu.main(cookies=douyuCookie,sum=douyuSum,idList=douyuList,nubList=douyuNum)
    if jJiji == '1':
        jiji.main(jijiUser, jijiPassWord)
    if cCunhua == '1':
        cunhua.main(cunhuaUser,cunhuaPassWord)




