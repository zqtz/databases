

# 终端操作mysql

1.  show databases;#查找所有数据库
2.  use spiders;#切换到要用的数据库
3.  select * from students;从数据表中找出数据
4.  select * from students where age=20;#通过条件找出要找的数据
5.  mysql -uroot -proot#登录数据库

mysql -uroot -proot#登录数据库
mysql> show databases;
ERROR 2006 (HY000): MySQL server has gone away
No connection. Trying to reconnect...
Connection id:    12
Current database: hexun

+--------------------+
| Database           |
+--------------------+
| information_schema |
| hexun              |
| mysql              |
| performance_schema |
| spiders            |
| sys                |
| taobao             |
| test               |
| yc                 |
| yr                 |
+--------------------+
10 rows in set (0.01 sec)

mysql> use spiders;
Database changed
mysql> select * from students;
+----------+-----------+-----+
| id       | name      | age |
+----------+-----------+-----+
| 20120001 | Bob       |  20 |
| 19941030 | 吴雨润    |  27 |
+----------+-----------+-----+
2 rows in set (0.00 sec)

mysql> select * from students where age=20;
+----------+------+-----+
| id       | name | age |
+----------+------+-----+
| 20120001 | Bob  |  20 |
+----------+------+-----+
1 row in set (0.00 sec)

mysql> select * from students where age=27;
+----------+-----------+-----+

| id   | name | age  |
| ---- | ---- | ---- |
|      |      |      |
+----------+-----------+-----+
| 19941030 | 吴雨润 | 27   |
| -------- | ------ | ---- |
|          |        |      |
+----------+-----------+-----+
1 row in set (0.00 sec)

mysql> exit#突出服务器
Bye



# 如何创建数据库和数据表

1. mysql> create database yurun;
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| hexun              |
| mysql              |
| performance_schema |
| spiders            |
| sys                |
| taobao             |
| test               |
| yc                 |
| yr                 |
| yurun              |
+--------------------+
11 rows in set (0.00 sec)

mysql> use yurun;
Database changed
mysql> show tables;#查看数据表
Empty set (0.00 sec)

#创建数据表
 mysql>  CREATE TABLE pet (
    ->  name VARCHAR(20),
    ->  owner VARCHAR(20),
    ->  species VARCHAR(20),
    ->  sex CHAR(1),
    ->  birth DATE,
    ->  death DATE);
Query OK, 0 rows affected (0.04 sec)

mysql> describe pet;#查看数据表的具体结构
+---------+-------------+------+-----+---------+-------+

| Field | Type | Null | Key  | Default | Extra |
| ----- | ---- | ---- | ---- | ------- | ----- |
|       |      |      |      |         |       |
+---------+-------------+------+-----+---------+-------+
| name | varchar(20) | YES  |      | NULL |      |
| ---- | ----------- | ---- | ---- | ---- | ---- |
|      |             |      |      |      |      |
| owner | varchar(20) | YES  |      | NULL |      |
| ----- | ----------- | ---- | ---- | ---- | ---- |
|       |             |      |      |      |      |
| species | varchar(20) | YES  |      | NULL |      |
| ------- | ----------- | ---- | ---- | ---- | ---- |
|         |             |      |      |      |      |
| sex  | char(1) | YES  |      | NULL |      |
| ---- | ------- | ---- | ---- | ---- | ---- |
|      |         |      |      |      |      |
| birth | date | YES  |      | NULL |      |
| ----- | ---- | ---- | ---- | ---- | ---- |
|       |      |      |      |      |      |
| death | date | YES  |      | NULL |      |
| ----- | ---- | ---- | ---- | ---- | ---- |
|       |      |      |      |      |      |
+---------+-------------+------+-----+---------+-------+
6 rows in set (0.01 sec)



# 增加数据记录

mysql> INSERT INTO pet#插入数据
    -> VALUES ('github','yurun','cat','m','2021-02-02',NULL);
Query OK, 1 row affected (0.01 sec)

mysql> show tables;
+-----------------+
| Tables_in_yurun |
+-----------------+
| pet             |
+-----------------+
1 row in set (0.00 sec)

mysql> select * from pet;
+--------+-------+---------+------+------------+-------+

| name | owner | species | sex  | birth | death |
| ---- | ----- | ------- | ---- | ----- | ----- |
|      |       |         |      |       |       |
+--------+-------+---------+------+------------+-------+
| github | yurun | cat  | m    | 2021-02-02 | NULL |
| ------ | ----- | ---- | ---- | ---------- | ---- |
|        |       |      |      |            |      |
+--------+-------+---------+------+------------+-------+
1 row in set (0.00 sec)



# 数据类型和类型选择

 MySQL 支持多种类型，大致可以分为三类：数值、日期/时间和字符串(字符)类型。 



| 类型         | 大小                                     | 范围（有符号）                                               | 范围（无符号）                                               | 用途            |
| :----------- | :--------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :-------------- |
| TINYINT      | 1 Bytes                                  | (-128，127)                                                  | (0，255)                                                     | 小整数值        |
| SMALLINT     | 2 Bytes                                  | (-32 768，32 767)                                            | (0，65 535)                                                  | 大整数值        |
| MEDIUMINT    | 3 Bytes                                  | (-8 388 608，8 388 607)                                      | (0，16 777 215)                                              | 大整数值        |
| INT或INTEGER | 4 Bytes                                  | (-2 147 483 648，2 147 483 647)                              | (0，4 294 967 295)                                           | 大整数值        |
| BIGINT       | 8 Bytes                                  | (-9,223,372,036,854,775,808，9 223 372 036 854 775 807)      | (0，18 446 744 073 709 551 615)                              | 极大整数值      |
| FLOAT        | 4 Bytes                                  | (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 0，(1.175 494 351 E-38，3.402 823 466 E+38)                  | 单精度 浮点数值 |
| DOUBLE       | 8 Bytes                                  | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度 浮点数值 |
| DECIMAL      | 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 | 依赖于M和D的值                                               | 依赖于M和D的值                                               | 小数值          |

url = 'https://www.runoob.com/mysql/mysql-data-types.html'



# mysql的增删改查



mysql> delete from pet where name='github';#删除数据表的数据
Query OK, 1 row affected (0.03 sec)

mysql> update pet set name='喵喵喵' where owner='yurun';#修改数据表的数据
Query OK, 2 rows affected (0.01 sec)
Rows matched: 2  Changed: 2  Warnings: 0

1. 增加insert into values(name varchar(10),like varchar(10));

2. 删除delete from table where ...=...

3. 改动update table set ...where from ...=;

4. 查询 select * from table;

   

# mysql建表约束

1. 主键约束
   
   -给某个字段增加约束,可以使其唯一确定一个值,就可以使得字段不重复且非空mysql> create table user(
       -> id int primary key,#id值唯一
       -> name varchar(15)
       -> );
Query OK, 0 rows affected (0.03 sec)
   
   mysql> show tables;
   +-----------------+
   | Tables_in_yurun |
   +-----------------+
   | pet             |
   | testtype        |
   | user            |
   +-----------------+
3 rows in set (0.00 sec)
   
   mysql> describe user;
   +-------+-------------+------+-----+---------+-------+
   
   | Field | Type | Null | Key  | Default | Extra |
   | ----- | ---- | ---- | ---- | ------- | ----- |
   |       |      |      |      |         |       |
   +-------+-------------+------+-----+---------+-------+
| id   | int(11) | NO   | PRI  | NULL |      |
| ---- | ------- | ---- | ---- | ---- | ---- |
|      |         |      |      |      |      |
| name | varchar(15) | YES  |      | NULL |      |
| ---- | ----------- | ---- | ---- | ---- | ---- |
|      |             |      |      |      |      |
   +-------+-------------+------+-----+---------+-------+
   2 rows in set (0.00 sec)



#联合主键,两个加起来不重复就可以

create table user2(
 id int,
name varchar(20),
password varchar(20),
primary key(id,name)
);

mysql> insert into user2 values(1,'张三',123456)
    -> ;
Query OK, 1 row affected (0.01 sec)

mysql> insert into user2 values(2,'张三',123456)
    -> ;
Query OK, 1 row affected (0.00 sec)

mysql> describe user2;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| id       | int(11)     | NO   | PRI | NULL    |       |
| name     | varchar(20) | NO   | PRI | NULL    |       |
| password | varchar(20) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
3 rows in set (0.00 sec)

mysql> select * from user2;
+----+--------+----------+

| id   | name | password |
| ---- | ---- | -------- |
|      |      |          |
+----+--------+----------+
| 1    | 张三 | 123456 |
| ---- | ---- | ------ |
|      |      |        |
| 2    | 张三 | 123456 |
| ---- | ---- | ------ |
|      |      |        |
+----+--------+----------+
2 rows in set (0.00 sec)



1. 自增约束

   #自动控制id的增长

   create table usr3(
   id int primary key auto_increment,
   name varchar(20),
    );

   

   mysql> alter table usr4 add primary key(id);#增加primary key
   Query OK, 0 rows affected (0.03 sec)
   Records: 0  Duplicates: 0  Warnings: 0

   mysql> desc usr4;
   +-------+-------------+------+-----+---------+-------+
   | Field | Type        | Null | Key | Default | Extra |
   +-------+-------------+------+-----+---------+-------+
   | id    | int(11)     | NO   | PRI | NULL    |       |
   | name  | varchar(20) | YES  |     | NULL    |       |
   +-------+-------------+------+-----+---------+-------+
   2 rows in set (0.00 sec)

   mysql> alter table usr4 drop primary key;#删除primary key
   Query OK, 0 rows affected (0.03 sec)
   Records: 0  Duplicates: 0  Warnings: 0

   mysql> desc usr4;
   +-------+-------------+------+-----+---------+-------+
   | Field | Type        | Null | Key | Default | Extra |
   +-------+-------------+------+-----+---------+-------+
   | id    | int(11)     | NO   |     | NULL    |       |
   | name  | varchar(20) | YES  |     | NULL    |       |
   +-------+-------------+------+-----+---------+-------+
   2 rows in set (0.00 sec)

   

   mysql> alter table usr4 modify id int primary key;#修改数据表的约束
   ERROR 2006 (HY000): MySQL server has gone away
   No connection. Trying to reconnect...
   Connection id:    6
   Current database: yurun

   Query OK, 0 rows affected (0.05 sec)
   Records: 0  Duplicates: 0  Warnings: 0

   mysql> desc usr4;
   +-------+-------------+------+-----+---------+-------+

   | Field | Type | Null | Key  | Default | Extra |
   | ----- | ---- | ---- | ---- | ------- | ----- |
   |       |      |      |      |         |       |
   +-------+-------------+------+-----+---------+-------+
   | id   | int(11) | NO   | PRI  | NULL |      |
   | ---- | ------- | ---- | ---- | ---- | ---- |
   |      |         |      |      |      |      |
   | name | varchar(20) | YES  |      | NULL |      |
   | ---- | ----------- | ---- | ---- | ---- | ---- |
   |      |             |      |      |      |      |
   +-------+-------------+------+-----+---------+-------+
   2 rows in set (0.00 sec)
   create table usr6(

   id int,

   name varchar(20),

   unique(id,name)

   );

   create table usr7(

   id int,

   name varchar(20),

   unique(id,name)

   );

   

   mysql> create table usr7(
       ->
       -> id int,
       ->
       -> name varchar(20),
       ->
       -> unique(id,name)
       ->
       -> );
   Query OK, 0 rows affected (0.01 sec)

   mysql> desc usr7;
   +-------+-------------+------+-----+---------+-------+

   | Field | Type | Null | Key  | Default | Extra |
   | ----- | ---- | ---- | ---- | ------- | ----- |
   |       |      |      |      |         |       |
   +-------+-------------+------+-----+---------+-------+
   | id   | int(11) | YES  | MUL  | NULL |      |
   | ---- | ------- | ---- | ---- | ---- | ---- |
   |      |         |      |      |      |      |
   | name | varchar(20) | YES  |      | NULL |      |
   | ---- | ----------- | ---- | ---- | ---- | ---- |
   |      |             |      |      |      |      |
   +-------+-------------+------+-----+---------+-------+
   2 rows in set (0.00 sec)

   

   mysql> alter table usr7 modify name varchar(20) unique;#修改
   Query OK, 0 rows affected (0.03 sec)
   Records: 0  Duplicates: 0  Warnings: 0

   mysql> desc usr7;
   +-------+-------------+------+-----+---------+-------+

   | Field | Type | Null | Key  | Default | Extra |
   | ----- | ---- | ---- | ---- | ------- | ----- |
   |       |      |      |      |         |       |
   +-------+-------------+------+-----+---------+-------+
   | id   | int(11) | YES  |      | NULL |      |
   | ---- | ------- | ---- | ---- | ---- | ---- |
   |      |         |      |      |      |      |
   | name | varchar(20) | YES  | UNI  | NULL |      |
   | ---- | ----------- | ---- | ---- | ---- | ---- |
   |      |             |      |      |      |      |
   +-------+-------------+------+-----+---------+-------+
   2 rows in set (0.00 sec)

   总结:
   --建表的时候可以添加约束;

   --alter 。。。add...

   --alter。。。modify...

   --删除 alter。。。drop

   

   

   

2. 外键约束

3. 唯一约束

   mysql> alter table usr5 add unique(name);#添加name为唯一约束
   Query OK, 0 rows affected (0.03 sec)
   Records: 0  Duplicates: 0  Warnings: 0
   mysql> desc usr5;
   +-------+-------------+------+-----+---------+-------+
   | Field | Type        | Null | Key | Default | Extra |
   +-------+-------------+------+-----+---------+-------+
   | id    | int(11)     | YES  |     | NULL    |       |
   | name  | varchar(20) | YES  | UNI | NULL    |       |
   +-------+-------------+------+-----+---------+-------+
   2 rows in set (0.01 sec)

   mysql> insert into usr5 values(
       -> 1,'zhangshan');
   Query OK, 1 row affected (0.00 sec)

   mysql> insert into usr5 values(
       -> 1,'zhangshan');
   ERROR 1062 (23000): Duplicate entry 'zhangshan' for key 'name'

   

   
   
4. 非空约束

   mysql> create table usr8(
       -> id int,
       -> name varchar(20) not null#非空约束
       -> );
   ERROR 2006 (HY000): MySQL server has gone away
   No connection. Trying to reconnect...
   Connection id:    10
   Current database: yurun

   Query OK, 0 rows affected (0.05 sec)

   mysql> desc usr8;
   +-------+-------------+------+-----+---------+-------+
   | Field | Type        | Null | Key | Default | Extra |
   +-------+-------------+------+-----+---------+-------+
   | id    | int(11)     | YES  |     | NULL    |       |
   | name  | varchar(20) | NO   |     | NULL    |       |
   +-------+-------------+------+-----+---------+-------+
   2 rows in set (0.00 sec)


   mysql> insert into usr8 values(1,'zhangshang');
   Query OK, 1 row affected (0.00 sec)

   mysql> insert into usr8 (name) values('lishi');
   Query OK, 1 row affected (0.00 sec)

   mysql> desc usr8;
   +-------+-------------+------+-----+---------+-------+
   | Field | Type        | Null | Key | Default | Extra |
   +-------+-------------+------+-----+---------+-------+
   | id    | int(11)     | YES  |     | NULL    |       |
   | name  | varchar(20) | NO   |     | NULL    |       |
   +-------+-------------+------+-----+---------+-------+
   2 rows in set (0.00 sec)

   mysql> select * from usr8;
   +------+------------+
   | id   | name       |
   +------+------------+
   |    1 | zhangshang |
   | NULL | lishi      |
   +------+------------+
   2 rows in set (0.00 sec)

   


5. 默认约束mysql> create table usr9(
       -> id int,
       -> name varchar(20),
       -> age int default 10#增加默认约束
       -> );
   ERROR 2006 (HY000): MySQL server has gone away
   No connection. Trying to reconnect...
   Connection id:    11
   Current database: yurun

   Query OK, 0 rows affected (0.02 sec)

   mysql> desc usr9;
   +-------+-------------+------+-----+---------+-------+
   | Field | Type        | Null | Key | Default | Extra |
   +-------+-------------+------+-----+---------+-------+
   | id    | int(11)     | YES  |     | NULL    |       |
   | name  | varchar(20) | YES  |     | NULL    |       |
   | age   | int(11)     | YES  |     | 10      |       |
   +-------+-------------+------+-----+---------+-------+
   3 rows in set (0.00 sec)

   mysql> insert into usr9 (id,name) values(1,'yurun');
   Query OK, 1 row affected (0.00 sec)

   mysql> select * from usr9;
   +------+-------+------+

   | id   | name | age  |
   | ---- | ---- | ---- |
   |      |      |      |

   +------+-------+------+

   | 1    | yurun | 10   |
   | ---- | ----- | ---- |
   |      |       |      |

   +------+-------+------+
   1 row in set (0.00 sec)

   

6. 外键约束
   create table classes(

   id int primary key,

   name varchar(20)
   );

   create table students(

   id int primary key,

   name varchar(20),

   class_id int,

   foreign key(class_id) references classes(id)

   );

   

   mysql> create table classes(
       ->
       -> id int primary key,
       ->
       -> name varchar(20)
       -> );
   ERROR 2006 (HY000): MySQL server has gone away
   No connection. Trying to reconnect...
   Connection id:    12
   Current database: yurun

   Query OK, 0 rows affected (0.03 sec)



   mysql> create table students(
       ->
       -> id int primary key,
       ->
       -> name varchar(20),
       ->
       -> class_id int,
       ->
       -> foreign key(class_id) references classes(id)
       ->
       -> );
   ERROR 2006 (HY000): MySQL server has gone away
   No connection. Trying to reconnect...
   Connection id:    13
   Current database: yurun

   Query OK, 0 rows affected (0.02 sec)

   

   insert into classes values(1,'一班');

   insert into classes values(2,'二班');

   insert into classes values(3,'三班');

   insert into classes values(4,'四班');

   

   insert into students values('1001','张三',1);

   insert into students values('1002','张三',2);

   insert into students values('1003','张三',3);

   insert into students values('1004','张三',4);

   insert into students values('1005','lishi',5);

# 数据表设计的三大范式



1,第一范式

create table student2(

id int primary key,

name varchar(20),

adress varchar(20)

);

insert into student2 values('1','yurun','中国广东省佛山市南海区桂城街道12号')；

insert into student2 values('2','yurun','中国广东省佛山市南海区里水大道12号')；

insert into student2 values('3','yurun','中国广东省佛山市禅城区张槎大道13号')；



create table student3(

id int primary key,

name varchar(20),

country varchar(20),

province varchar(20),

adress varchar(20)

);

insert into student3 values('1','yurun','中国','广东省','桂城街道12号')；

insert into student3 values('2','yurun','中国','广东省','湾大道12号')；

insert into student3 values('3','yurun','中国','广东省','桂城街道12号')；



2,第二范式

#完成依赖于第一个值

create table myorder(

product_id int,

consumer_id int,

product_name varchar(20),

consumer_name varchar(20),

primary key(product_id,consumer_id)

)





#进行拆分

create table myorder(

order_id int primary key,

product_id int,

consumer_id int,

)

create table product(

id int,primary key

name varchar(20)

)



create table condumer(

id int,primary key

name varchar(20)

)



3,第三范式

满足第二范式后,除了和主键有关系,和其他副键没有关系

create table myorder(

order_id int primary key,

product_id int,

consumer_id int,

#consumer_phone int,#不能和主键外的键有关系

)

create table condumer(

id int,primary key

name varchar(20)，

consumer_phone int

)



# mysql查询练习

1,创建数据

#创建学生表

create table student(

sno varchar(20) primary key,

sname varchar(20) not null,

ssex varchar(20) not null,

sbirthday datetime,

class varchar(20)

);

#创建教师表

create table teacher(

tno varchar(20) primary key,

tname varchar(20) not null,

tsex varchar(20) not null,

tbirthday datetime,

prof varchar(20) not null,

depart varchar(20) not null

);

#创建课程表,外键约束为教师表

create table course(

cno varchar(20) primary key,

cname varchar(20) not null,

tno varchar(20) not null,

foreign key(tno) references teacher(tno)

);

#创建分数表

create table score(

sno varchar(20) not null,

cno varchar(20) not null,

degree decimal,

foreign key(sno) references student(sno),

foreign key(cno) references course(cno),

primary key(sno,cno)

);