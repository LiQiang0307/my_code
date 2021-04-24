import pymysql
from flask import Flask
import json
"""
# 从数据库中获取数据；
"""

def connect_mysql():
    # 连接mysql数据库
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='mysql',
        db='chuzhandong',
        charset='utf8')
    #创建游标
    cursor=conn.cursor()#执行完毕返回的结果默认以元组的形式保存
    return conn,cursor


def colse_mysql_conn(conn,cursor):
    """
    关闭数据库的连接
    :param conn:
    :param cursor:
    :return:
    """
    cursor.close()
    conn.close()


def fetch_dict_result(cur):
    row_headers = [x[0] for x in cur.description]  # this will extract row headers
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    return json.dumps(json_data)

#sql查询函数
def mysql_query(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return:
    """
    #连接数据库，创建游标
    conn,cursor=connect_mysql()
    #执行sql语句
    cursor.execute(sql,args)
    #获取返回的数据（元组形式）
    # res=cursor.fetchall()
    res=fetch_dict_result(cursor)
    #关闭游标，以及数据库连接
    colse_mysql_conn(conn,cursor)
    return res

app = Flask(__name__)
@app.route('/getstu')
def getStu():
    """
    获取数据库内容
    :return:
    """
    sql="select * from `2020103173`"
    res=mysql_query(sql)
    # print(res)
    return res

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)
