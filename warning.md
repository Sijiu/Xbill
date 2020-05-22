#### 1. Warning: (1265, "Data truncated for column 'trans_id' at row 1")
    trans_id 字段太长 由 50 改为80即可. 2016022421001004540272626565_20160224000000022000000091730266
    
#### 2.Warning: (3090, "Changing sql mode 'NO_AUTO_CREATE_USER' is deprecate
   登录mysql, mysql -uroot -p  
   输入 set @@GLOBAL.sql_mode='';  
   set sql_mode ='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
   即可解决.
```sql
mysql> set @@GLOBAL.sql_mode='';
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> set sql_mode ='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
Query OK, 0 rows affected (0.00 sec)
```

## Plan 调整计划
- [x] logging [logging demo](https://www.flyml.net/2018/12/12/flask-logging-usage-demo/)  
- [ ] blueprint  
- [ ] 招行明细, pdf导入支持  
- [ ] 建行明细(→)    
- [ ] 交行明细(↓)  
- [ ] 北行明细(↓)   