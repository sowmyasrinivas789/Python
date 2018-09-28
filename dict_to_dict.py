class test():
    def rec_set(self, my_dict, key_list, val, key):
        if not isinstance(my_dict, dict):
            return
        if len(key_list) == 0:
            my_dict[key] = val
            return
        elif my_dict.get(key) is None:
            my_dict[key] = dict()
            a = key_list.pop(0)
            self.rec_set(my_dict[key], key_list, val, a)
        else:
            a = key_list.pop(0)
            self.rec_set(my_dict[key], key_list, val, a)

    def get_body(self, data):
        body = dict()
        for each in data:
            key_list = each.split('/')
            print("key_list", key_list)
            cur_key = key_list.pop(0)
            print("cur_key", cur_key)
            self.rec_set(body, key_list, data[each], cur_key)
        return body

# creating a dict with keys list
data = {"a/d/f/g": 80, "a/e/f/g": 90, 'a/d/p': 50}

try:
    t = test()
    print(t.get_body(data))
except Exception as e:
    print (e)



# def update(key, values, jsonpath_value, jsonpath_values):
#     values = path_value
#     e = list(jsonpath_value.keys())[0]
#     if e in list(values.keys()):
#         update(e, values[e], jsonpath_value[e], jsonpath_values)
#     else:
#         #print(jsonpath_value)
#         values.update(jsonpath_value)
#         values[key] =
#         #path_value[e].update(list(path_value.values())[0])
#         #path_value[e].update(list(jsonpath_values.values())[0])
#
#
# path_value = {}
# for path in data:
#     keypath_lsit = path.split("/")
#     keypath_lsit.reverse()
#     jsonpath_value = data[path]
#     for keys in keypath_lsit:
#         dict2 = {}
#         dict2.update({keys : jsonpath_value})
#         jsonpath_value = dict2
#     key = list(jsonpath_value.keys())[0]
#     print(jsonpath_value)
#     if key in list(path_value.keys()):
#         update(key, path_value[key], jsonpath_value[key])
#     path_value.update(jsonpath_value)
#
# print(path_value)
