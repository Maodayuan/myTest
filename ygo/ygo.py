import pymysql


def ygo():
    db = pymysql.connect(host='localhost',
                         user='ygo',
                         password='ygo',
                         db='ygo',
                         charset='utf8')

    curor = db.cursor()
    sql = """INSERT INTO card_pic(name,name_color, rare, kind, attr,level,bag,race,atk,def,info)
             VALUES ('真红眼黑龙','黑','UR','通常','暗','7','PAC-JP031','龙','2400','2000','拥有真红之眼的黑龙。愤怒的黑炎会把映入其眼者全部烧成灰烬。')"""
    try:
        curor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print('error')
    # data = curor.fetchall()
    # print("Database version : %s " % data)
    db.close()


if __name__ == '__main__':
    ygo()
