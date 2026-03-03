def summation(a, b):
    return a+b

def mult(a, b):
    return a*b

def subt(a, b):
    try:
        return a-b
    except:
        return 0

x = [summation(10, 12), mult(12, 6), subt(10, 'asd')]
print(x)
print(any(x))


print(bin(14))
print(callable(x))
print(chr(30))

print(divmod(13, 3)[1])

res = list(enumerate([12, 4, 6, 'str']))
print(res[3][1])

def f_func(s):
    if isinstance(s, str):
        return s
    else:
        return ''
    
test_list = ['asd ', 'hello', 123, True, {"ads":"wer"}]

res_f= filter(f_func, test_list)
# print(res_f)
for i in res_f:
    print(i)
    
str='print(123)' 
eval(str)

mes = "Not used with len"

def myfunc(a):
    try:
        return len(a)
    except: 
        return mes

x = map(myfunc, ('apple', 'banana', [123], 45.3))

print(x)

#convert the map into a list, for readability:
print(list(x))

# fhand = open('Lecture materials\mbox-short.txt', 'r')
# x = fhand.read()
# print(x[35:49])

# fhand.write('Hello')

# fhand = open('Lecture materials\mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not 'From: ' in line : 
#         continue
#     print(line)


# fname = input('Enter the file name:  ')
# try:
#     fhand = open(fname)
# except:
#     fhand = open(fname, 'w') 
#     inp = input('The file is created, Please, Enter the file content:  ')  
#     fhand.write(inp) 
#     fhand.close()
# count = 0
# fhand = open(fname)
# for line in fhand:
#     if line.startswith('Subject:') :
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

# fhand = open('test4.txt', 'a')
# inp = input("Message here: ")
# fhand.write(inp)

with open("Lecture materials\mbox-short.txt") as f:
  print(f.readline())
  
import os
if os.path.exists("test2.txt"):
  os.rmdir("Test")
else:
  print("The file does not exist")