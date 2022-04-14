# Protocol

## REST
基于文本的无状态的协议

**优点:**

1. 易学，易懂，容易上手
2. HTTP cache简单
3. 松耦合(loose coupling)

**缺点:**

1. 效率低，每个request都要建立新链接
2. 无模式(Schema-less): 客户端很难去做数据验证 (graphql有)
3. 无状态：没有额外的功能维持会话
4. 额外开销: 每个request都有header和上下文元数据


## GraphQL
查询语言协议