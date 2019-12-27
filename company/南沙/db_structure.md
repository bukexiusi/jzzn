# 数据库结构

## 系统表

### 组织表(部门表)

```sql
CREATE TABLE `sys_dept` (
  `id` char(18) NOT NULL COMMENT '物理主键',
  `dept_name` varchar(50) DEFAULT NULL COMMENT '部门名称',
  `ancestor_id` text COMMENT '祖先id',
  `lvl` tinyint(2) DEFAULT NULL COMMENT '等级',
  `creator` varchar(20) DEFAULT NULL COMMENT '创建人',
  `create_time` bigint(20) DEFAULT NULL COMMENT '创建时间',
  `updator` varchar(20) DEFAULT NULL COMMENT '修改人',
  `update_time` bigint(20) DEFAULT NULL COMMENT '修改时间',
  `record` int(11) DEFAULT NULL COMMENT '版本',
  `delete` tinyint(1) DEFAULT NULL COMMENT '删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='部门表';
```

### 角色表

```sql
CREATE TABLE `sys_role` (
  `id` char(18) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '物理主键',
  `role_code` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '角色代码',
  `data_code` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '数据代码',
  `role_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '角色名称',
  `creator` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '创建人',
  `create_time` bigint(20) DEFAULT NULL COMMENT '创建时间',
  `updator` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '修改人',
  `update_time` bigint(20) DEFAULT NULL COMMENT '修改时间',
  `delete` tinyint(1) DEFAULT '0' COMMENT '删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='角色表';
```

### 用户表

```sql
CREATE TABLE `sys_user` (
  `id` char(18) NOT NULL COMMENT '物理主键',
  `nickname` varchar(20) DEFAULT NULL COMMENT '姓名',
  `username` varchar(20) DEFAULT NULL COMMENT '用户名',
  `password` char(32) DEFAULT NULL COMMENT '密码',
  `source` char(8) DEFAULT NULL COMMENT '加密盐',
  `org_id` char(18) DEFAULT NULL COMMENT '机构id',
  `org_name` varchar(50) DEFAULT NULL COMMENT '机构名称',
  `dept_id` char(18) DEFAULT NULL COMMENT '部门id',
  `dept_name` varchar(50) DEFAULT NULL COMMENT '部门名称',
  `role_id` char(18) DEFAULT NULL COMMENT '角色id',
  `role_name` varchar(20) DEFAULT NULL COMMENT '角色名称',
  `auz_type` varchar(255) DEFAULT NULL COMMENT '授权许可类型',
  `phone` varchar(16) DEFAULT NULL COMMENT '电话',
  `email` varchar(50) DEFAULT NULL COMMENT '电子邮箱',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  `permit` varchar(255) DEFAULT NULL COMMENT '员工工作证',
  `disabled` tinyint(1) DEFAULT NULL COMMENT '禁用;0-启用,1-禁用',
  `creator` varchar(20) DEFAULT NULL COMMENT '创建人',
  `create_time` bigint(20) DEFAULT NULL COMMENT '创建时间',
  `updator` varchar(20) DEFAULT NULL COMMENT '修改人',
  `update_time` bigint(20) DEFAULT NULL COMMENT '修改时间',
  `record` int(11) DEFAULT NULL COMMENT '版本',
  `delete` tinyint(1) DEFAULT NULL COMMENT '删除',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='用户表';
```

### 菜单按钮表

```sql
CREATE TABLE `sys_menu` (
  `id` char(18) NOT NULL COMMENT '物理主键',
  `menu_name` varchar(20) DEFAULT NULL COMMENT '菜单名称',
  `menu_path` varchar(255) DEFAULT NULL COMMENT '菜单路径',
  `type` varchar(20) DEFAULT NULL COMMENT '类型',
  `icon` varchar(255) DEFAULT NULL COMMENT '图标路径',
  `ancestor_id` text COMMENT '祖先id',
  `layer` tinyint(2) DEFAULT NULL COMMENT '层级',
  `order_num` tinyint(2) DEFAULT NULL COMMENT '排序',
  `creator` varchar(20) DEFAULT NULL COMMENT '创建人',
  `create_time` bigint(15) DEFAULT NULL COMMENT '创建时间',
  `updator` varchar(20) DEFAULT NULL COMMENT '修改人',
  `update_time` bigint(15) DEFAULT NULL COMMENT '修改时间',
  `record` int(11) DEFAULT NULL COMMENT '版本',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='菜单表';
```

### 菜单权限表

```sql
CREATE TABLE `sys_role_menu` (
  `id` char(18) NOT NULL COMMENT '物理主键',
  `role_id` char(18) DEFAULT NULL COMMENT '角色物理主键',
  `menu_id` char(18) DEFAULT NULL COMMENT '菜单物理主键',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT COMMENT='角色菜单权限表';
```

## 业务表

### 案件表

案件表字段说明

字段名|驼峰|备注
-|-|-|
case_num|caseNum|执行案号|
cause|cause|案由|
receipt_date|receiptDate|收到材料日期|
source|source|案件来源|
register_date|registerDate|立案日期
exec_basis_sort|execBasisSort|执行依据种类
exec_object_value|execObjectValue|执行标的
exec_cost|execCost|执行费
acceptance_cost|acceptanceCost|案件受理费用
property_preservation_cost|propertyPreservationCost|财产保全费
exec_funds|execFunds|执行款项（计算）
exec_num|execNum|执行依据文号
exec_effective_date|execEffectiveDate|执行依据生效时间
exec_dept|execDept|作出执行依据单位
transfer_dept|transferDept|移交单位/委托单位
bank|bank|开户行
bank_account|bankAccount|收款账号
exec_content|execContent|执行内容
chief_judge|chiefJudge|审判长
chief_judge_phone|chiefJudgePhone|审判长联系方式
judge1|judge1|审判员1
judge1_phone|judge1Phone|审判员1联系方式
judge2|judge2|审判员2
judge2_phone|judge2Phone|审判员2联系方式
clerk|clerk|书记员
clerk_phone|clerkPhone|书记员联系方式





