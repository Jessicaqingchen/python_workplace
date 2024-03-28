def recMC(coinValueList, change, knowResults):
    '''
    递归方式解决找零兑换
    :param coinValueList: 零钱列表
    :param change: 找零的钱
    :param knowResults: 记录中间结果表
    :return:
    '''
    minCoins = change
    if change in coinValueList:
        knowResults[change] = 1
        return 1
    elif knowResults[change] > 0:
        return knowResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i, knowResults)
            if numCoins < minCoins:
                minCoins = numCoins
    #           找到最优解，记录到表中
                knowResults[change] = minCoins
    # print(knowResults)
    return minCoins

print(recMC([1,5,10,25], 63, [0]*64))
# print(c for c in [1, 5, 10, 25] if c <= 63)


def dpMakeChange(coinValueList, change, minCoins):
    # 从1分开始到change逐个计算到最少硬币数量
    for cents in range(1, change + 1):
        # 1、初始化一个最大值
        coinCount = cents
        # 2、减去每个硬币，向后查找最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
            # 3、得到当前最少硬币数，记录到表中
            minCoins[cents] = coinCount
#         返回最后
    return  minCoins[change]

print(dpMakeChange([1,5,10, 21,25], 63, [0]*64))

def dpMakeChange2(coinValueList, change, minCoins, coinsUsed):
    # 从1分开始到change逐个计算到最少硬币数量
    for cents in range(1, change + 1):
        # 1、初始化一个最大值
        coinCount = cents
        newCoin = 1
        # 2、减去每个硬币，向后查找最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoin = j
        # 3、得到当前最少硬币数，记录到表中
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
#         返回最后
    return  minCoins[change]

def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin -= thisCoin

amnt = 63
clist = [1, 5,10,21, 25]
coinUesd = [0]*(amnt + 1)
coinCount = [0]*(amnt + 1)
print("Making change for", amnt)
print(dpMakeChange2(clist, amnt, coinCount, coinUesd), "coins")
print("They are:")
printCoins(coinUesd, amnt)
print("The used list is as follows:")
print(coinUesd)