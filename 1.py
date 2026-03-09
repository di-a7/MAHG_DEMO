




# a=[[1,2,3],2,3]
# print( 2 in a)
# b=[1,2,3]
# print(b in a)




# e=[(1,"a"),(2,"b")]
# f=dict(e)
# print(f)

c=['a',1,'2','abc',5,'3','def']
# print(c[0:3])
# print(c[2:6])
# print(c[0:6:2]
print(c[::2])

# create a list of your hobbies
# creat a statement of sentence using each hobbies list
a=['cricket','football','video_games']
for value in a:
  print(f"I like {value}")


# create a dictionary that includes your name,age, contact and hobbies
# print your introduction using the information in the dictionary 
info={'name':['Hari','shyam'],
      'age':[45,50],
      'hobby':['playing cricket','play chess'],
      }
for key,value in info.items():
  print(key,':',value[0])

li=[1,4,2,3,5]
res=sorted(li,reverse=True)
print(res)