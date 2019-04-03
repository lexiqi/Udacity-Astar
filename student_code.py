
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        return False

    def __str__(self):
        return "x:"+str(self.x)+",y:"+str(self.y)

class Astar:
    class Node:
        """
        node:当前节点编号
        point:当前节点坐标
        endPoint:终点节点坐标
        """
        def __init__(self,node,point,endPoint,g=0):
            self.ID=node
            self.father=None
            self.g=g      #从起点移动到下一位置的移动代价，沿着到达该方格而生成的路径
            self.h=abs(endPoint.y-point.y)+abs(endPoint.x-point.x)  #h：从指定的位置移动到终点的估算成本
            self.f=self.g+self.h       #f=g+h

    def __init__(self,map,start,end):
        self.map=map    #地图
        self.startID=start #起始点编号
        self.startPoint=Point(*self.map.intersections[start])#起始点坐标
        self.endID=end     #终点编号
        self.endPoint=Point(*self.map.intersections[end])#终点坐标
        self.openList=[]      #开放列表
        self.closeList=[]      #关闭列表

    def getMinNode(self):
        """
        获得openlist中F值最小的节点
        :return: Node
        """
        currentNode=self.openList[0]
        for node in self.openList:
            if node.f<currentNode.f:
                currentNode=node
        return currentNode

    def nodeInCloseList(self,node):
        """
        判断当前节点是否在关闭列表中
        :return: BOOL
        """
        for node in self.closeList:
            if node.ID==node:
                return True
        return False

    def nodeInOpenList(self,node):
        """
        判断当前节点是否在关闭列表中
        :return: Node
        """
        for node in self.openList:
            if node.ID==node:
                return node
        return None

    def endPointInOpenList(self):
        """
        判断终点是否在开放列表中，如果在，结束查找
        :return: Node
        """
        for node in self.openList:
            if node.ID==self.endID:
                return node
        return None

    # 判断minF节点可达的节点，是否合适加入开放列表
    def checkAcessNode(self,minF):
        accessList=self.map.roads[minF.ID]
        point_minF = Point(*self.map.intersections[minF.ID])
        for accessId in accessList:
            #不在在关闭列表中
            if not self.nodeInCloseList(accessId):
                #计算花费
                point_Acess=Point(*self.map.intersections[accessId])
                step=abs(point_Acess.x-point_minF.x)+abs(point_Acess.y-point_minF.y)

                #如果不在openList中，就把它加入openList
                curNode=self.nodeInOpenList(accessId)
                if not curNode:
                    curNode=Astar.Node(accessId,point_Acess,self.endPoint,g=minF.g+step)
                    curNode.father=minF
                    self.openList.append(curNode)

                #如果在openList中，判断minF到当前点的G是否更小
                elif minF.g+step<curNode.g:#如果更小，就重新计算g值，并且改变father
                    curNode.g=minF.g+step
                    curNode.father=minF

    def start(self):
        """
        开始寻路
        :return: None或Node列表（路径）
        """
        # 1.将起点放入开启列表
        startNode = Astar.Node(self.startID,self.startPoint, self.endPoint)
        self.openList.append(startNode)
        # 2.主循环逻辑
        while True:
            # 找到F值最小的点
            minF = self.getMinNode()
            # 把这个点加入closeList中，并且在openList中删除它
            self.closeList.append(minF)
            self.openList.remove(minF)
            # 判断这个节点可行的节点，是否合适加入开放列表
            self.checkAcessNode(minF)
            #判断是否终止
            node=self.endPointInOpenList()
            if node:
                cNode=node
                pathList=[]
                while True:
                    if cNode:
                        pathList.append(cNode.ID)
                        cNode=cNode.father
                    else:
                        return list(reversed(pathList))
            if len(self.openList)==0:
                return



def shortest_path(M,start,goal):
    print("shortest path called")
    aStar=Astar(M,start,goal)
    pathList=aStar.start()
    return pathList