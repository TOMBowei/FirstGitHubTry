from pyecharts import Graph

relationship = open('/Users/wubowei/Documents/毕业设计源代码/relationship.txt','r')
line = relationship.readline()
list_temp = []    #暂时存放关系的list,方便其他用来拷贝
#逐行读取数据
while line:
      line = line.strip('\n')
      list_temp.append(line.split('|~|'))
      line = relationship.readline()
      # for i in list_temp:
      #       i[2] = int(i[2])
            # print(type(i[2]))
relationship.close()

# print(list_temp)            list1
list_name = list_temp   #拷贝一份list_temp数据，用于生成节点数据
nodes = []  #最终使用的节点数据项

#处理重复名字避免生成重复节点
for i in list_name:
      if {'name':i[0],'symbolSize': 5} in nodes:
            pass
      else:
            nodes.append({'name':i[0],'symbolSize': 5})
      if {'name':i[1],'symbolSize': 5} in nodes:
            pass
      else:
            nodes.append({'name':i[1],'symbolSize': 5})
print(nodes)

#生成边数据
nodes_temp = []   #处理边数据时需要使用节点数据，因此创造此list作为使用工具
for i in list_temp:
      nodes_temp.append({'name':i[0]})
      nodes_temp.append({'name':i[1]})
      nodes_temp.append({'value':i[2]})
print(nodes_temp)

links = []  #建立连接
temp = []
k = 0
for k in range(0,len(nodes_temp),3):
      temp = []
      for i in range(k,k+3):
            temp.append(nodes_temp[i])
      k = k + 3
      links.append({'source':temp[0].get('name'),'target':temp[1].get('name'),'value':temp[2].get('value')})

#关系图属性
graph = Graph("QQ好友关系网络")
graph.add("",nodes,links,
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
#生成关系图
graph.render()