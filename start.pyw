import os,time
file1 = open(os.getcwd()+'\checks.txt','w')#读取祈愿结果
file1.write('1')
file1.close()
time.sleep(0.1)
file1 = open(os.getcwd()+'\checks.txt','r')
b=file1.read()
file1.close()
if str(b)=='0':
    print("已经存在启动的实例")
else:
    os.startfile(os.getcwd()+'/main-4.5.pyw')
print(b)
