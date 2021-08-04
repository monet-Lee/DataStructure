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

5、is与==的区别

（1）python中万物皆对象，每个对象有3个属性：id，type，value。

（2）is比较对象的id是否一样，==比较对象的值是否一样，如a is b等价于 id(a)==id(b)

如以下个对象的type和值时一样的，id不完全一样：
a = 1
b = a
c = 1
d = 1.0

id(a)   # 35556792L
id(b)   # 35556792L
id(c)   # 35556792L
id(d)   # 21253459L

6、