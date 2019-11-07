# tips

1、不用select *
2、不在子查询中order by
3、Like优化 -> like 'a%'
4、不在循环里套查询
5、定长数据设计为char
6、id增长
7、能用int绝不用char
8、varchar(255) varchar(256)  256及其以上长度需要两个字节来保存存储长度