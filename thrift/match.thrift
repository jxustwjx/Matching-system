namespace cpp match_service #thrift就是远程函数调用框架，自己实现函数接口细节

struct User {       #定义一个结构体保存数据，但要根据thrift的要求，i32是int
    1: i32 id,
    2: string name,
    3: i32 score
}

service Match {     #service是thrift的关键字，里面存放函数接口

    /**
     * user: 添加的用户信息
     * info: 附加信息
     * 在匹配池中添加一个名用户
     */
    i32 add_user(1: User user, 2: string info),

    /**
     * user: 删除的用户信息
     * info: 附加信息
     * 从匹配池中删除一名用户
     */
    i32 remove_user(1: User user, 2: string info),
}
#thrift -r --gen cpp tutorial.thrift 这个命令可以在相应服务器或文件夹里面生成对应代码，你只需完成具体的代码细节。 最后一个参数是该文件所在位置
