import operator as op
import xmnlp
# score = xmnlp.sentiment(doc)
class CalRelationship:
    #得到txt文件的内容
    def get_content(self,txtfile):
        file = open(txtfile, encoding='UTF-8')
        content = file.read()
        # print(content)
        file.close()
        return content
    
    #计算关系值
    def cal_relationship(self,name1,name2,value):
        global relationships
        
        #如果两个好友同时存在，则设置标志
        flag = False
        
        for relationship in relationships:
            #吐过两个人都在，就改变关系值，并改变标记值
            if name1 in relationship and name2 in relationship:
                relationship[2] += value
                flag = True
        #如果两个好友中有一个或者都不在三元组内，就添加
        if flag == False and op.eq(name1,name2) == False:
            #首次放入要有一个初值
            relationships.append([name1,name2,value])
    
    #通过评论和点赞计算关系值
    def cal_relationship_by_data(self,datas,value):
        count = 0
        data_list = datas.split('\n')
        for element in data_list:
            count += 1
            data = element.split('|~|')
            if data[0] == '':
                return 0
            self.cal_relationship(data[0],data[1],value)
            print('已经分析了 '+ str(count)+' 行数据')
    
    #开始入口
    def start(self):
        comments = self.get_content('./comment.txt')
        likes = self.get_content('./like.txt')
        #评论好友关系+3,点赞好友关系+1
        self.cal_relationship_by_data(comments,3)
        self.cal_relationship_by_data(likes,1)

if __name__ == '__main__':
    # 将关系设置为全局变量以供方便调用
    relationships = []
    cal = CalRelationship()
    cal.start()
    #将计算好的关系值写入txt
    file = open('relationship.txt', 'w', encoding='UTF-8')
    for relationship in relationships:
        file.write(relationship[0] + '|~|' + relationship[1] + '|~|' + str(relationship[2]) + '\n')
    file.close()