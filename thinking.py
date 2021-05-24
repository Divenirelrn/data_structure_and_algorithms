"""
注意：
    逻辑：
    1.判别逻辑完整
    2.判别不间断
    3.不并列的情况不能做并列处理

    下标：
    1.注意下标越界与next为none
    2.对于数组，p指向某个元素,p为下标；对于链表，p指向某个元素,p为指针
    3.链表或二叉树，p指向head或root,用p=p.next(p=p.left,p=p.right)查找某个节点，若想对p赋值，那么最终p不能指向None
    4.如果p1与p2都指向node,那么del p1无法删除node
    5.数组下标的判定放在 条件1 and 条件2 的条件1位置
    6.无穷大加1
    7.while i < len_s and s[i] == " ":

    递归：
    1.递归别忘了return

    list与dict：
    1.l1 = l2 = list() 与 l1 = list() l2 = list() 是不一样的

    其他：
    1.MAX_VALUE = int(math.pow(2,31) - 1) （整数）


思想：
    1.快慢指针
    2.双指针
    3.取模操作
    4.高维的方法解决低维的问题（双指针解决单链表）
    5.递归与分治
    6.递归（分治思想、总体思想（二叉树的深度与节点数量））
    7.回溯
        (1)做标记，恢复
        (2)append, pop, flags
    8.贪心算法
    9.动态规划：填数组（一维或二维）
    10.归并思想
    11.哈希表、哈希表去重
    12.全局与迭代器
    13.自己控制两个数组的长度（交换两个数组，使第一个数组永远是短的）
    14.二叉树

主题：
    1.链表的插入与删除
    2.字符串模式匹配
    3.二叉树的排序
    4.排列与组合

"""