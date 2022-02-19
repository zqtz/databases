import pymysql as msql

connect = msql.connect(host='localhost', db='dd', user='root', password='a19941030', port=3306)
cursor = connect.cursor()

def insert():
    sql = "INSERT INTO tushu (name,link) values ('spider','http://');"
    try:
        cursor.execute(sql)
        connect.commit()
        print('插入数据成功')
    except:
        connect.rollback()
        print("插入数据失败")
    connect.close()


def save_msql():
    # name = 'python爬虫'
    # link = 'http://'

    sql = "insert into tushu  (name,link) values ('p','http://www.dd.com');"
    try:
        cursor.execute(sql)
        connect.commit()
        print('存储数据成功')
    except:
        print('存储数据失败')

def get_mysql_data():
    try:
        sql = "select * from taob limit 10,10;"
        count = cursor.execute(sql)
        # print(count)
        results = cursor.fetchmany(20)
        for result in results:
            print(result)
    finally:
        connect.close()

insert()





