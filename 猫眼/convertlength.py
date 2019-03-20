import pymysql, time, datetime

def updateCommentLength():
    conn = pymysql.connect("localhost","root","mym@1249690440","maoyan",3306)
    cursor = conn.cursor()
    # sql1 = "alter table moviecomment add column length varchar(40);"
    sql2 = """update moviecomment set length = case 
    when length(comment) <= 20 then 0
    when length(comment) > 20 and length(comment) <= 50 then 1
    when length(comment) > 50 and length(comment) <= 100 then 2
    else 3 end;
    """
    # ursor.execute(sql1)
    cursor.execute(sql2)
    cursor.close()
    conn.commit() 
    conn.close()

if __name__ == '__main__':
    updateCommentLength()