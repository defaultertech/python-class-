# class teacher:
#     mylist=[]
#     def __init__(self):
#         self.name='abc'
#         self.id=10
#         self.salary=123434
#     def show(self):
#         print('name=',self.name,'id=',self.id,'salary=',self.salary,end=' ')
#
# class student (teacher):
#     def __init__(self):
#         self.course='web pt'
#         self.fees=21312
#         super().__init__()
#     def showinfo(self):
#         super(student,self).show()
#         print('course',self.course,'fees',self.fees)
#
# class student1 (teacher):
#     def __init__(self):
#         self.course1='web pt'
#         self.fees=21312
#         super().__init__()
#     def showinfo(self):
#         super(student3,self).show()
#         print('course1',self.course,'fees',self.fees)
#
#
#
#
#
# ob=student()
# ob.showinfo()
# ob=student1

# block chain


#########################################333
# with open(r'C:\Users\ADVANCE-IT\Desktop\cheat sheet for hacking\nmap cheatsheet.txt') as x:
#      data=x.readlines()
#      a=data[20:30]
#      for i in a:
#          print(i)
# print(x.closed)



# a=open(r'C:\Users\ADVANCE-IT\Desktop\cheat sheet for hacking\oscp\photo_2020-11-06_23-00-42.jpg' 'rb')
# for i in a:
#     print(i)


# import  os
# a= r'C:\Users\ADVANCE-IT\Desktop\payloads\urlredirectionPAYLOAD.txt'
# os.popen(a)
# #



# from hashlib import sha256
# MAX_NONCE = 100000000000
#
# def SHA256(text):
#     return sha256(text.encode("ascii")).hexdigest()
#
# def mine(block_number, transactions, previous_hash, prefix_zeros):
#     prefix_str = '0'*prefix_zeros
#     for nonce in range(MAX_NONCE):
#         text = str(block_number) + transactions + previous_hash + str(nonce)
#         new_hash = SHA256(text)
#         if new_hash.startswith(prefix_str):
#             print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
#             return new_hash
#
#     raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")
#
# if __name__=='__main__':
#     transactions='''
#     Dhaval->Bhavin->20,
#     Mando->Cara->45
#     '''
#     difficulty=4 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
#     import time
#     start = time.time()
#     print("start mining")
#     new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
#     total_time = str((time.time() - start))
#     print(f"end mining. Mining took: {total_time} seconds")
#     print(new_hash)




# a=10
# b=10.2
# c=4j+2j
# print(type(a))
# print(type(b))
# print(type(c))


# a="hello world"
# b='hello bhai'
# print(type(a))
# print(b)

#####################################333
# class block:
#     def __init__():
#         pass
#     def calculate_hash():
#
#  class Blockchain:
#       def __init__():
#         pass
#
#       def construct_genesis(self):
#         pass
#       def construct_block(self,proof_no,prev_hash):
#         pass
#
#       @staticmethod
#       def check_validity():
#          pass
#
#
#       def new_data(self,sender,recipient,quantity):
#          pass
#
#     @staticmethod
#     def construct_proof_of_work(prev_proof):
#         pass
#
#     @property
#     def last_block(self):



















































