dict_list = [{1:'a',2:'b',3:'c'},{1:'a',2:'b',3:'c'},{1:'a',2:'b',3:'c'},{1:'a',2:'b',3:'c'}]
updated_dictlist = []
for d in dict_list:
    updated_dict = {}
    for key, value in d.items():
        updated_dict['sony'+str(key)] = value
    updated_dictlist.append(updated_dict)
print(updated_dictlist)