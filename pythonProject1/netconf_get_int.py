from ncclient import manager

import xmltodict


# 定义设备连接信息/define the connect information for device
huawei_device = {
    'host': '192.168.252.134',
    'username': 'zhaoyuqi',
    'password': 'ZHAOyuqi@123',
    'port': 830,
    'device_params': {'name': 'huaweiyang'},
    'hostkey_verify': False,
    'look_for_keys': False,
}

#定义XML格式的netconf命令/define the netconf command in XML format
xml_filter = '''
    <filter type="subtree">
      <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>GigabitEthernet0/0/1</name>
        </interface>
      </interfaces-state>
    </filter>
'''

#连接设备并发送XML格式的netconf命令给设备
with manager.connect(**huawei_device) as m:
    response = m.get(xml_filter)

#将设备回应的XML格式的文本转成字典格式
response_dict = xmltodict.parse(response.xml)

#用for循环来提取字典的数据并输出

interfaces = response_dict['rpc-reply']['data']['interfaces-state']['interface']

for i in interfaces:
    if 'name' in i:
        print(i,":",interfaces[i])
    if 'speed' in i:
        print(i,":",interfaces[i])
    if 'phys-address' in i:
        print(i,":",interfaces[i])
    if 'admin-status' in i:
        print(i, ":", interfaces[i])
    if 'oper-status' in i:
        print(i, ":", interfaces[i])
 #   print(i,':',interfaces[i])
 #   print(interface['name'])
   # print('Description:',inter['Description'])
   # print('Speed:',interface['Speed'])

#写一个由小到大排序的算法
list = [1,3,5,7,9,2,4,6,8,10]
list.sort()
    print(list)
list.sort(reverse=True)
    print(list)
list.reverse()
    print(list)
list.sort(key=None,reverse=True)
    print(list)
list.sort(key=None,reverse=False)
    print(list)


#写一个冒泡排序的算法
list = [1,3,5,7,9,2,4,6,8,10]
for i in range(len(list)-1):
    for j in range(len(list)-1-i):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
print(list)



