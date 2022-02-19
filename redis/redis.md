# 数据

geospatial地理空间

redis判断距离

![1640050611921](C:\Users\investor\AppData\Roaming\Typora\typora-user-images\1640050611921.png)

**getadd**

127.0.0.1:6379> geoadd chinacity 121.47 31.23 shanghai
(integer) 1
127.0.0.1:6379> geoadd chinacity 114.13 22.54 shengzheng
(integer) 1
127.0.0.1:6379> geoadd chinacity 113.24 23.12 guanzhou
(integer) 1
127.0.0.1:6379> geoadd chinacity 113.14 23.02 foshan
(integer) 1

***GEORADIUS***

27.0.0.1:6379> GEORADIUS chinacity 110 30 1000 km withdist (以110，30的经纬度查询附件的城市和人)
1) 1) "shengzheng"
   2) "926.1379"
2) 1) "foshan"
   2) "836.7752"
3) 1) "guanzhou"
   2) "830.2215"
127.0.0.1:6379> GEORADIUS chinacity 110 30 1000 km withcoord
1) 1) "shengzheng"
   2) 1) "114.13000255823135376"
      2) "22.53999903789756587"
2) 1) "foshan"
   2) 1) "113.13999921083450317"
      2) "23.01999918384158406"
3) 1) "guanzhou"
   2) 1) "113.23999732732772827"
      2) "23.1199990030198208"
127.0.0.1:6379> GEORADIUS chinacity 110 30 1000 km withcoord withdist count 1
1) 1) "guanzhou"
   2) "830.2215"
   3) 1) "113.23999732732772827"
      2) "23.1199990030198208"
127.0.0.1:6379> GEORADIUS chinacity 110 30 1000 km withcoord withdist count 2
1) 1) "guanzhou"
   2) "830.2215"
   3) 1) "113.23999732732772827"
      2) "23.1199990030198208"
2) 1) "foshan"
   2) "836.7752"
   3) 1) "113.13999921083450317"
      2) "23.01999918384158406"
127.0.0.1:6379> GEORADIUS chinacity 110 30 1000 km withcoord withdist count 3
1) 1) "guanzhou"
   2) "830.2215"
   3) 1) "113.23999732732772827"
      2) "23.1199990030198208"
2) 1) "foshan"
   2) "836.7752"
   3) 1) "113.13999921083450317"
      2) "23.01999918384158406"
3) 1) "shengzheng"
   2) "926.1379"
   3) 1) "114.13000255823135376"
      2) "22.53999903789756587"

**PFADD,PFCOUNT,PFCOUNT(取基数)**

127.0.0.1:6379> PFADD mykey q w e r #创建一组元素
(integer) 1
127.0.0.1:6379> PFADD mykey2 q w a s d f j k
(integer) 1
127.0.0.1:6379> PFMERGE mykey3 mykey mykey2# 合并两组原始
OK
127.0.0.1:6379> PFCOUNT mykey3#计算元素的数量
(integer) 10
127.0.0.1:6379> 

**Bitmaps**

周一导周日的打卡

#储存数据

127.0.0.1:6379> setbit sign 0 1
(integer) 0
127.0.0.1:6379> setbit sign 1 1
(integer) 0
127.0.0.1:6379> setbit sign 2 1
(integer) 0
127.0.0.1:6379> setbit sign 4 1
(integer) 0
127.0.0.1:6379> setbit sign 3 1
(integer) 0
127.0.0.1:6379> setbit sign 5 1
(integer) 0
127.0.0.1:6379> setbit sign 6 1
(integer) 0
判断是否有打卡
127.0.0.1:6379> getbit sign 0
(integer) 1
127.0.0.1:6379> getbit sign 6
(integer) 1

# 事务

redis事务的本质:一组命令的集合。一组事务的所有命令会被序列化,在事务执行的过程中,会按照顺序执行

一次性,排他性,顺序性

原子性:要么成功,要么失败

redis单条命令具有原子性,事务不一定有原子性

> redis事务：

1.开启事务(multi)

2.命令入队

3.执行事务(exec)

> 正常执行事务

#命令入队

127.0.0.1:6379> multi
OK
127.0.0.1:6379> set k1 v1
QUEUED
127.0.0.1:6379> set k2 v2
QUEUED
127.0.0.1:6379> get k2
QUEUED
127.0.0.1:6379> set k3 v3
QUEUED
127.0.0.1:6379> exec#执行事务
1) OK
2) OK
3) "v2"
4) OK

> 放弃事务

127.0.0.1:6379> multi#开启事务
OK
127.0.0.1:6379> set k1 v1
QUEUED
127.0.0.1:6379> set k2 v2
QUEUED
127.0.0.1:6379> DISCARD#放弃事务
OK
127.0.0.1:6379> get k2
(nil)
127.0.0.1:6379> get k1
(nil)
127.0.0.1:6379> 







