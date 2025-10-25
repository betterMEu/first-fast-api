# alembic

## 获取信息

- 当前版本
  alembic current [--verbose]
- 升降级历史
  alembic history [--verbose]
- 查看头
  alembic heads [--verbose]
- 分支
  alembic branches [--verbose]



## 生成执行文件

```
alembic revision --autogenerate -m "描述"
```



## 升级

```
alembic upgrade head                    [head无分支升级至最新迁移文件]
                <revision_id>           [升级特定版本]
                <+num>                  [升级num步]
                <revision_id><+num>
                heads                   [heads合并所有分支升级]
```



## 降级

```
alembic downgrade <revision_id>         [降级特定版本]
                  <-num>                [降级num步]
                  <revision_id><-num>
                  base                  [使用base撤销所有升级]
```



## 分支

你基于v2创建升级了v3，他基于v2创建升级了v4

```
          v3（head）
        /
v1 - v2
        \
          v4（head）
```

使用 alembic heads [--verbose]，查看有哪些head



## 合并

```
                             -- ae1027a6acf --
                           /                   \

<base> --> 1975ea83b712 -->                      --> mergepoint
                           \                   /
                            -- 27c6a30d7c24 --

```



## 分支标签

将分裂的版本设置别名，方便操作裂变的版本



1. 在versions目录找到分裂的版本文件

   ```py
   revision = '27c6a30d7c24'
   down_revision = '1975ea83b712'
   branch_labels = ('shoppingcart',)  # 设置别名
   ```

2. 别名显示

   ```shell
   $ alembic history
   1975ea83b712 -> 27c6a30d7c24 (！！shoppingcart！！) (head), add shopping cart table
   ...
   
   $ alembic show shoppingcart
   Rev: 27c6a30d7c24 (head)
   Parent: 1975ea83b712
   Branch names: shoppingcart
   ...
   ```

3. 当使用了分支标签，迁移文件生成命令需要指定分支

   不使用

   ~~~shell
   $ alembic revision -m "add a shopping cart column"
     FAILED: Multiple heads are present; please specify the head revision on
     which the new revision should be based, or perform a merge.
   ~~~

   使用

   ~~~shell
   alembic revision -m "add a shopping cart column"  --head shoppingcart@head
                                                            [revision_id]
                                                            [branch_labels]
   ~~~

   







特殊的 revision_id
* base 指向 初始状态，即没有任何迁移文件之前的数据库状态
* head 指向 最新版本，即当前最新的迁移文件所对应的版本
