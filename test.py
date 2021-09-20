from pyecharts import Graph
list1 = [['小明','小张',1],['小明','小虎',2],['小明','小A',3]]
nodes = []
nodes_temp = []
for i in list1:
    if {'name':i[0],'symbolSize': 5} in nodes_temp:
        pass
    else:
        nodes_temp.append({'name':i[0],'symbolSize': 5})
    if {'name':i[1],'symbolSize': 5} in nodes_temp:
        pass
    else:
        nodes_temp.append({'name':i[1],'symbolSize': 5})
print("nodes_temp : ")
print(nodes_temp)
print('=====================================')

for i in list1:
    nodes.append({'name':i[0]})
    nodes.append({'name':i[1]})
    nodes.append({'value':i[2]})
print('nodes: ')
print(nodes)
print('=====================================')

links = []
temp = []
k = 0
for k in range(0,len(nodes),3):              # k: 0, 3, 9
    temp = []
    for i in range(k,k+3):          # i: 0-2, 3-5, 6-8 
        # print(i)
        temp.append(nodes[i])
    k = k + 3
    links.append({'source':temp[0].get('name'),'target':temp[1].get('name'),'value':temp[2].get('value')})

print('temp:')
print(temp)
print('=====================================')
print('links:')
print(links)



graph = Graph("关系图示例")
graph.add("",nodes_temp,links,
        categories=None, # 结点分类的类目，结点可以指定分类，也可以不指定。
        is_focusnode=True, # 是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。默认为 True
        is_roam=True,
        is_rotatelabel=True, # 是否旋转标签，默认为 False
        graph_layout="force", # 布局类型，默认force=力引导图，circular=环形布局
        graph_edge_length=300, # 力布局下边的两个节点之间的距离，这个距离也会受 repulsion 影响。默认为 50，TODO 值越大则长度越长
        graph_gravity=0.5, # 点受到的向中心的引力因子。TODO 该值越大节点越往中心点靠拢。默认为 0.2
        graph_repulsion=100, # 节点之间的斥力因子。默认为 50，TODO 值越大则斥力越大
        is_label_show=True,
        line_curve=0.2 # 线的弯曲度
            )
graph.render()
# [{'name': '小明', 'symbolSize': 1}, {'name': '小张', 'symbolSize': 2}, {'name': '小虎', 'symbolSize': 3}, {'name': '小A', 'symbolSize': 4}]
# [{'name': '小明', 'symbolSize': 5}, {'name': '小张', 'symbolSize': 5}, {'name': '小明', 'symbolSize': 5}, {'name': '小虎', 'symbolSize': 5}, {'name': '小明', 'symbolSize': 5}, {'name': '小A', 'symbolSize': 5}]