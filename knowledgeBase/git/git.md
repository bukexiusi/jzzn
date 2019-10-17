# git
---

1. git只能跟踪文本文件的改动，比如TXT，网页，所有的程序代码等等
2. git不能跟踪二进制文件的改动，比如图片，视频，word，excel等等
3. git基本概念
  ==工作区 <-> 暂存区 <-> 仓库 <-> 远程主机==
  ==->>>>>add>>>>>commit>>push>>>>>>==
  ==-<<<<<<<<<<<<<<<<<<<<<poll<<<<<<==
  

## 初始化git用户

Git是分布式版本控制系统，所以，每个机器都必须自报家门：你的名字和Email地址。设置语句如下：

```git
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```

注意**git config**命令的--**global**参数，用了这个参数，表示你这台机器上==所有的Git仓库==都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。

若后续需要查看用户名和email，查询语句如下：
```git
$ git config user.name
$ git config user.email
```

## 创建仓库

+ 创建仓库的文档目录
+ 空白处右键选择 Git Bash Here
+ 逐行输入以下语句
    ```git
    $ mkdir zn
    $ cd zn
    $ git init
    ```
**tips**: 如果你使用Windows系统，为了避免遇到各种莫名其妙的问题，==请确保目录名（包括父目录）不包含中文==。
**tips**: pwd -> 打印当前路径

## 添加文件到仓库

```git
$ git add readme.txt
$ git add doc/你猜.docx
$ git commit -m "备注信息"
```

**tips**: git不能提交目录，只能提交文件

## 查看仓库新增和修改情况

```git
$ git status
```

输入上面语句后会打印如下情况

```git
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   "doc/\346\226\260\345\273\272.docx"

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   "doc/\344\275\240\347\214\234.docx"
```

其中
==new file== 是新增未提交的文件
==modified== 是编辑未提交的文件
若modified是==红色的==，则说明修改文件没有进行git add的前置操作
若modified是==绿色的==，则执行git commit后提交到仓库

## 查看文件修改情况

```git
$ git diff readme.txt
```

## 仓库历史日志

```git
$ git log
```
或
```git
$ git log --pretty=oneline
```
一行展示仓库日志

## 仓库版本切换

回到上个版本
```git
$ git reset --hard head^
```

回到指定版本
```git
$ get reset --hard 96a045
```
note: 96a045是版本号前几位，不必输入完整
**tips**: cat readme.txt -> 查看文件内容

## 后悔药



+ 当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令
  ```git
  $ git checkout -- readme.txt
  ```
  + git checkout -> 仓库里数据覆盖工作区数据 (新增、编辑、删除)
  + ==工作区 <-> 暂存区 <-> 仓库 <-> 远程主机==       
+ 当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令
  ```git
  $ git reset HEAD readme.txt
  ```
  就回到了场景1，第二步按场景1操作。

+ 已经提交了不合适的修改到版本库时，参考==仓库版本切换==，不过前提是没有推送到远程库。

+ 记录了每一次操作（提交记录、切换版本）
  ```git
  $ git reflog
  ```
## 删除文件

+ 删除工作区
```git
$ rm readme.txt
```
+ 删除仓库同时删除工作区
```git
$ git rm readme.txt
```

# 远程仓库

## github

本地Git仓库和GitHub仓库之间的传输是通过SSH加密的，所以，需要一点设置
+ 创建SSH Key
  + 在用户主目录下，看看有没有.ssh目录，如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件
    + 如果已经有了，可直接跳到下一步。
    + 如果没有，打开Shell（Windows下打开Git Bash），创建SSH Key：
      ```git
      $ ssh-keygen -t rsa -C "youremail@example.com"
      ```
+ 登陆GitHub，打开Account settings，SSH Keys页面,然后，点Add SSH Key，填上任意Title，在Key文本框里粘贴id_rsa.pub文件的内容
+ 添加远程库
  + 仓库类型为公共仓库

### 先有本地库，后有远程库

+ 本地仓库关联GitHub仓库
  + 在本地仓库根路径下-git窗口-用命令
    ```git
    $ git remote add origin git@github.com:bukexiusi/learngit.git
    ```
  + com:github账户名/gitbub仓库名.git
  + 第一次关联会有ssh警告，输入yes即可
+ 本地仓库的内容推送到GitHub仓库，用命令
  ```git
  $ git push -u origin master
  ```
  第一次推送到远程仓库时需要加-u，后续推送时把命令简化为
  ```git
  $ git push origin master
  ```
  git push 远程连接？ 远程分支名
+ 总结
  + git remote add origin git@github.com:bukexiusi/learngit.git
  + git push -u origin master
  + git push origin master

### 先有远程库，后有本地库

```git
$ git clone git@github.com:bukexiusi/jzzn.git
```

### 分支管理

+ 查看分支
  ```git
  $ git branch
  ```
+ 创建分支
  ```git
  $ git branch 分支名称
  ```
+ 切换分支
  ```git
  $ git checkout 分支名称
  或者
  $ git switch 分支名称
  ```
+ 创建+切换分支
  ```git
  $ git checkout -b 分支名称
  或者
  $ git switch -c 分支名称
  ```
+ 合并某分支到当前分支
  ```git
  $ git merge 分支名称
  ```
+ 删除分支
  ```git
  $ git branch -d 分支名称
  ```
  出现Cannot delete branch 'dev' checked out at 是因为你正处在此分支上，删除不了，得先切换