import requests

#url = 'http://127.0.0.1:8000/login/'


headers={}
headers['Authorization']='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY5MzY0NDk5LCJpYXQiOjE2NjkzNjQxOTksImp0aSI6Ijk0OGU5NGIxMTI1NzQ4MDk5YzhlMjZiNDM0ZmE5NTljIiwidXNlcl9pZCI6NX0.Xh1Nie3byOBUpRsdmwGLdvwQAmn-FiS1VZLXc--NkcE'
r=requests.get('http://127.0.0.1:8000/book/',headers=headers)
print(r.text)
#headers = {'Authorization': '{ 'token' : '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' }'}
#r = requests.post(url, json={
   # 'username':'Neethu',
  #  'password':'12345'

#})
#print(r.json())