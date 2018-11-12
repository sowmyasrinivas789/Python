cpp_data = []
webapi_data = []

with open('cpp_data.txt', 'r') as in_file:
    for line in in_file:
        if '=' not in line:
            continue
        data = line.split('=')[-1].split(';')[0].strip(', \n')
        cpp_data.append(data)

with open('weapi_data.txt', 'r') as ou_file:
    for line in ou_file:
        if '.' not in line:
            continue
        data = line.split(':')[0].split('.')[-1]
        webapi_data.append(data)

print(len(cpp_data), cpp_data)
print(len(webapi_data), webapi_data)

for e in webapi_data:
    if e not in cpp_data:
        print(e)
        pass