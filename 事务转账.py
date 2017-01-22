import sys

import pymysql

source_userId = sys.argv[1]
target_userId = sys.argv[2]
money = sys.argv[3]

# 连接数据库
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='test',
    charset='utf8'
)


class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def transfer(self, source_userId, target_userId, money):
        try:
            self.check_acct_available(source_userId)
            self.check_acct_available(target_userId)
            self.has_enough_money(source_userId, money)

            self.reduce_money(source_userId, money)
            self.add_money(target_userId, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check_acct_available(self, userId):
        with self.conn.cursor() as cursor:
            sql = "SELECT userId,balance FROM balance WHERE userId=%s" % userId
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('账号%s不存在' % userId)

    def has_enough_money(self, userId, money):
        with self.conn.cursor() as cursor:
            sql = "SELECT userId,balance FROM balance WHERE userId=%s AND balance >= %s" % (userId, money)
            cursor.execute(sql)
            rs = cursor.fetchall()

            if len(rs) != 1:
                raise Exception('账号%s余额不足' % userId)

    def reduce_money(self, userId, money):
        with self.conn.cursor() as cursor:
            sql = "UPDATE balance SET balance=balance-%s WHERE userId=%s" % (money, userId)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception('账号%s扣款失败' % userId)

    def add_money(self, userId, money):
        with self.conn.cursor() as cursor:
            sql = "UPDATE balance SET balance=balance+%s WHERE userId=%s" % (money, userId)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception('账号%s入账失败' % userId)


transferMoney = TransferMoney(conn)

try:
    transferMoney.transfer(source_userId, target_userId, money)
    print('转账成功')
except Exception as e:
    print('出现问题：', str(e))
finally:
    conn.close()
