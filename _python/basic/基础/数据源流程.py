'''

导入数据 -》（表头提示） -》 筛选数据 （涉及查询条件可配置，涉及字段a由字段b而定） -》 执行 -》写入日志。更改总表状态
'''


'''
data = {
    "table_name": "",
    "id_name": "",
    "id_idx": "",
    "colums": [
        {
            "a": "",
            "b": ""
        },{
        }
    ]
}
'''

'''
表-表属性
  -列属性-参数

列是否校验
    0 或 1
配置查询字段
    单查询 区间查询
    label中文
    label英文
    控件类型
    默认值
    下拉数据源
某些字段的导入由某些字段而定
    字段名（可能多个），规则
    或者
    动态编码
关联总表
    0 或 1
    关联总表名
    
    bz_total_case_code
    bz_total_item
     
                                                       总表         附属表
    第一次导入 生成 bz_total_table1 往总表关联表写入 bz_total_table1 bz_table1
                                                   bz_total_table2 bz_table2
                                                    bz_total_table1 bz_table3
'''


'''
配置后的查询实现方式
'''

# import yt.word

yt.word.open()

