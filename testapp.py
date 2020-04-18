import requests
import json

base_url='http://127.0.0.1:8000/'
endpoint='api/'
# def get_resource(id):
#     resp=requests.get(base_url+endpoint+id+'/')
#     print(resp.status_code)
#     print(requests.codes.ok)
#     if resp.status_code == requests.codes.ok:
#         print('status',resp.status_code)
#         print(resp.json())
#     else:
#         print('something goes wrong')
# def get_all():
#     resp=requests.get(base_url+endpoint)
#     try:
#         if resp.status_code==resp.ok:
#             print('done')
#     except:
#         print('no valid data is available')
#
# def create_resource():
#     new_emp={
#     'ename':'atul',
#     'eid':9,
#     'eadd':'Haryana',
#     'esal':10000
#     }
#     resp=requests.post(base_url+endpoint,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
#
#
# def update_resource(id):
#     new_emp={
#     'esal':14000,
#     'eadd': 'new ashok nagar'
#     }
#     resp=requests.put(base_url+endpoint+str(id)+'/',data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
#
# def delete_resource(id):
#     resp=requests.delete(base_url+endpoint+str(id)+'/')
#     print(resp.status_code)
#     print(resp.json())
#
# delete_resource(11)


def get_resource(id=None):
    data={}
    if id is not None:
        data={
            'id':id
            }
    resp=requests.get(base_url+endpoint,data=json.dumps(data))
    print(resp.status_code)
    print(requests.codes.ok)
    if resp.status_code == requests.codes.ok:
        print('status',resp.status_code)
        print(resp.json())
    else:
        print('something goes wrong')

#get_resource(1)

def create_resource():
    data={'name':'deepak',
    'rollno': 8,
    'marks':6,
    'school': 'pnm'
    }
    resp=requests.post(base_url+endpoint,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

#create_resource()

def update_resource(id):
    data={'id':id,
    'school': 'abcdefgh'
    }
    resp=requests.put(base_url+endpoint,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

update_resource(3)
