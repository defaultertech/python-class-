# import  re
# p = re.compile('[]')
# print(type(p))
# p1 = 'abhjfba0jdSDFSFSDjyh567jyjhfabaaishdaagdsgab'
# mach = re.finditer(p,p1)
# c=0
# for i in mach:
#     print('matching string-',i.group())
#     print('start position',i.start())
#     print('end position',i.end())
#     c=c+1
# print('total occrences math string-',c)

# import re
# match=re.finditer('\W','aaaaaabhjgfjhjfjhmb456jhfhhghgf%%sfdgfgdl')
# for i in match:
#     print('match string-',i.group())
#
# print('total occrences match string-')


# import re
# txt = "The rain in Spain"
# m = re.search(r"\bS\w+", txt)
# print(m.group()

# import urllib.request
# from urllib import request
# request_url = urllib.request.urlopen('https://www.bing.com')
# print(request_url.read())


# import re
# import urllib.request
# u = urllib.request.urlopen("https://www.intex.in/contact-us")
# text = u.read()
# t = re.findall('[0-9]{10}[0-9]',str(text))
# print(t)

########################################################
# a = 23
# b =255
#
# c = a*b
# print(not c)



# a = '''welcome to craw'''
# b = 'o ' in a
# print(b)

# a =19
# b =20
# c =a
# print('id of a=',id(a))
# print('id of b=',id(b))
# print('id of c=',id(c))
# print(a is b)
# print(a is not b)
# a = 10
# if a%2==0:
#     print(a, 'is even no')
# else:print(a , 'is odd no')

# a = int(input('enter your age='))
# if a<=1 and a<=100:
#     print('valid user')
# if a <=15:
#     print('no charege')
# if a>=15 and a<=50:
#     print('full payment')
# if a>50 and a<=80:
#     print('half payment')
# if a>=80 and a<100:
#     print('no charge')
# else:
#     print('app yogya nahi hai get lost')

# a = 4%int(input('enter value= '))
# if (a % 4 and a % 100 and a % 400) ==0:
#     print('ye leap hai')
# else:
#     print('not a leap year')
# if (a % 4 and a % 100 and a % 400) >=1:
#     print('not a leap year')
# # if (a % 4 ) >=0:
# #
# #     print('this is leap year')
# # if (a % 4) >= 1:
# #
# #     print('this is not leap year')
# import calendar
# yy= 2021
# mm=4
# yy =int(input("ENTER YEAR: "))   ###########3 clender
# mm = int(input("enter month: "))
# print(calendar.month(yy,mm))











































