import pymysql


def get_connect():
    '''
    链接数据库
    :return:
    '''
    connect = pymysql.connect(
        host = "litemall.hogwarts.ceshiren.com",
        port=13306,
        user="test",
        password="test123456",
        database="litemall",
        charset="utf8mb4"
    )
    return connect

def execute_sql(sql):
    connect = get_connect()
    cursor = connect.cursor()
    # 执行sql
    cursor.execute(sql)
    # 查询一条记录
    record = cursor.fetchone()
    return record

if __name__ == '__main__':
    execute_sql("")