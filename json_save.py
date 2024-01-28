import json
person={'name':'Max','age':10,'phone':['9111','738982']}
result=json.dumps(person)
print(result)
print(type(result))

a={'name':'Egor','age':14,'numphone':'+79050285323'}
result1=json.dumps(a)
print(result1)
print(type(result1))