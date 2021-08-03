1、git更新modified文件：

git add .

2、远程仓库发生改变，更新到本地

（1）git remote -v         // 查看远程仓库

（2）git fetch origin master      // 将远程库更新到本地

（3）git log master.. origin/master        // 比较远程更新和本地版本库的差异

（4）git merge origin/master        // 合并远程库

3、链表

（1）头结点与其他节点要分开处理。

（2）头结点的作用：

a、防止链表为空时，头指针为null。带头结点的链表，头指针始终指向头结点，统一空链表和非空链表的操作。

b、方便链表的首节点插入删除操作的统一性。

4、应该在每个文件中有整体的介绍说明！

