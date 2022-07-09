import itertools
import zipfile

def un_zip(passwd_string,min_len,max_len,zFile):
    for len in range(min_len,max_len+1):
        to_attempt = itertools.product(passwd_string,repeat=len)
        for attempt in to_attempt:
            passwd = ' '.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd=passwd.encode)
                print(f"비밀번호는 {passwd} 입니다.")
                return 1
            except:
                pass
                
def un_zip1(passwd,zFile):
    print(passwd)
    try:
        zFile.extractall(pwd=passwd.encode)
        print(f"비밀번호는 {passwd} 입니다.")
        return 1
    except:
        pass
            


passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipfile.ZipFile(r'./암호1234.zip')

min_len = 1
max_len = 5

passwd = "1234"
#unzip_result = un_zip(passwd_string,min_len,max_len,zFile)
unzip_result = un_zip1(passwd,zFile)


if unzip_result ==1:
    print("비밀번호 찾는데 성공했습니다.")
else:
    print("비밀번호 찾는데 실패했습니다.")

