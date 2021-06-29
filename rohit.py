# print('hello im rohit')
# a=21
# b=23



# class person:
#     collage='NRI'
#     def __init__(self):
#         self.name='rohit'  #_ protected specifier modifier in python
#         self._cname='MCA'
#         self.__ps='12324'  # __private , u cant access outsite of class directly
#
#
#     def rohit(self):
#         print('hello,my name is '+self.name+' class name-'+self._cname, 'password-',self.__ps)
#
#
# ob=person()
# ob.rohit()
# print(ob.name)

while 1:
 try:
    a=int(input('enter no- '))
    b=int(input('enter no- '))
    print(a/b)
 except  ZeroDivisionError:
    print('cant divide by zero')
 except Exception:
     print('invalid no.')

