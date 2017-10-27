print('Hello,World!')

x = 10
x = x + 2

print(x)

name = input('please enter your name: ')

print('hello,', name)


from urllib.request import *
f = urlopen('http://api.jisuapi.com/weather/query?appkey=yourappkey&city=安顺')
print(f.read().decode('utf-8'))
# f = open('/Users/bailiangjin/dev/workspace/kevinswork/python/fileoperating/test.text', 'w')
#
# f.write("test.txtcontent")