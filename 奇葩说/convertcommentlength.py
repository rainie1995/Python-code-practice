import pymysql, time, datetime

def updateCommentLength():
    conn = pymysql.connect("localhost","root","mym@1249690440","i_can_i_bibi",3306)
    cursor = conn.cursor()
    # cursor.execute("alter table orgdata add column length varchar(40)")
    cursor.execute("select * from orgdata")
    values = cursor.fetchall()
    cursor.close()
    for item in values:
        content = item[2]
        length = 0
        if len(content) <= 20:
            length = 0
        elif len(content) > 20 and len(content) <= 50:
            length = 1
        elif len(content) > 50 and len(content) <= 100:
            length = 2
        else:
            length = 3
        sql = 'UPDATE orgdata SET length =\"" + str(length) + "\" WHERE id =\"" + item[0] + "\"'
        cc = conn.cursor()
        cc.execute(sql)
        cc.close()
    conn.commit()
    conn.close()
    time.localtime()

if __name__ == '__main__':
    updateCommentLength()