1、git更新modified文件：

git add .

2、远程仓库发生改变，更新到本地

（1）git remote -v         // 查看远程仓库

（2）git fetch origin master      // 将远程库更新到本地

（3）git log master.. origin/master        // 比较远程更新和本地版本库的差异

（4）git merge origin/master        // 合并远程库
3、链表
（1）头结点与其他节点要分开处理。

