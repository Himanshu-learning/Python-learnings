print(".............DICTIONARY DECLARTIO: METHOD 1-using syntax.........")
user_info1={'name':'Himanshu','Desgination':'Senior engineer','Specialization':['linux','bash','python','K8S','Redhat-Openshift']}
user_info2={'name':'Himanshu Sharma',
            'Desgination':'Devops engineer',
            'Specialization':['linux','jenkins','python','AWS ECS','AWS ECR']}
print(".............DICTIONARY DECLARTIO: METHOD 2---using dict operator.........")
user_info3=dict(name='Himanshu',
                Desgination='Desktop engineer',
                Specialization=['ubuntu','docker'])

print(user_info2)
print(f"\nDictionary based index 2 accessing: {user_info2['Specialization']}")
print(f"\n.............Assinging Values in Dictionary.....................")
new_user={}
new_user['name']='jenkins'
new_user['home_dir']='/var/spool/email/'
print(new_user)

print("\n----------------Checking a key in dictionary-------------")
if 'name' in new_user:
    print(new_user['name'])

print("\n------------CHCEKING VALUES IN A DICTIONARY----------")
if '/var/spool/' in new_user.values():
    print(new_user['home_dir'])

print(f"\n----------PRINTING KEY------------")
for i in new_user:
    print(i)
print(f"\n----------PRINTING VALUES------------")    
for i in new_user.values():
    print(i)