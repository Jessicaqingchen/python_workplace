def sequentialSearch(alist, item):
    '''
    有序表查找
    :param alist:有序表
    :param item:要查找的元素
    :return:是否找到boolen
    '''
    pos = 0
    found = False
    # 在查找过程中，如果查找的数大于列表中相应位置的元素，且没有匹配，则停止查找
    stop = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found

alist = [1,3,4,56,77,88,99]
print(sequentialSearch(alist, 88))

def binarySearch(alist, item):
    '''
    二分查找，前提序列是有序的
    :param alist:
    :param item:
    :return:
    first:第一个元素位置
    last:最后一个元素位置
    midpoint :中间项位置
    '''
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
alist = [1,3,4,56,77,88,99]
print(sequentialSearch(alist, 88))

# 用递归算法来实现二分查找
def binarySearch2(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            # 如果查找的元素比中间项小，则返回左边的一半
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                # 如果查找的元素比中间项大，则返回右边的一半
                return binarySearch(alist[midpoint+1:], item)

alist = [1,3,4,56,77,88,99]
print(binarySearch2(alist, 88))

def selectSearch(alist):
    '''
    比冒泡排序更优的选择排序
    :param alist:
    :return:
    '''
    for fillslot in range(len(alist)-1, 0, -1):
        posMax = 0
        for pos in range(1, fillslot+1):
            if alist[pos] > alist[pos + 1]:
                posMax = pos

    temp = alist[fillslot]
    alist[fillslot] = alist[posMax]
    alist[posMax] = temp

def insertSort(alist):
    '''
    插入排序
    前提条件：列表有序
    :param alist:
    :return:
    '''
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > alist[position]:
            alist[position] = alist[position - 1]
            position = position -1
        alist[position] = currentValue

def mergeSort(alist):
    '''
    归并排序（无序）
    :param alist:
    :return:
    '''
    # 归并排序结束条件
    if len(alist) <= 1:
        return alist
    # 将列表分为左右两个部分，并分别进行排序
    middle = len(alist) // 2
    left = mergeSort(alist[:middle])
    right = mergeSort(alist[middle:])

    # 对两部分进行合并排序
    merge = []
    while left and right:
        if left[0] <= right[0]:
            merge.append(left.pop(0))
        else:
            merge.append(right.pop(0))
    # 如果左右还有剩余，则直接合并
    merge.extend(right if right else left)
    return merge

class BinaryTree:
    '''
    节点链接法
    成员key保存根节点数据项
    成员left 、rightChild保存指向左右子树的引用
    '''
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        '''向左插入新节点'''
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t =  BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertReft(self, newNode):
        '''向左插入新节点'''
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t =  BinaryTree(newNode)
            t.rightChild = self.leftChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
r.insertLeft('b')
r.insertReft('c')
r.getRightChild().setRootVal('hello')
r.getLeftChild().insertReft('d')

import operator
def evaluate(parseTree):
    '''两数相加，二叉树解析'''
    opers = {
        '+': operator.add, '-': operator.sub,
        '*': operator.mul, '/': operator.truediv
    }

    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()

    if leftChild and rightChild:
        # 保存操作符
        fn = opers[parseTree.getRightChild()]
        return fn(evaluate(leftChild), evaluate(rightChild))
    else:
        return parseTree.getRootVal()

def preorder(tree):
    '''遍历树'''
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

class BinarySearchTree:
    '''
    root成员引用根节点TreeNode
    '''
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        '''
        插入key构造BST
        :param key:
        :param val:
        :return:
        '''
        if self.root:
            # 2、否则就调用一个递归函数_put来放置key
            self._put(key, val, self.root)
        else:
            # 1、先查看是否为空，如果为空，那么key成为根节点root
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        '''
        如果key比currentNode小，则_put到左子树
            没有左子树的话，key就成为左节点
        反之右子树
        :param val:
        :param currentNode:当前子节点
        :return:
        '''
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)


class TreeNode:
    '''
    二叉搜索树的实现
    '''
    def __init__(self, key, value, left=None,\
                 right= None, parent=None):
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and \
            self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and \
            self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self