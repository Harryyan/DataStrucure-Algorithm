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
基于文本的无状态的协议，客户端可以通过一个endpoint请求多个资源

**优点:**

1. Schema-based type query，客户端可以确保类型正确
2. 减少http call
3. 支持双向通信(subscription)

**缺点:**

1.  服务端复杂
2. 与服务端高度耦合
3. 性能取决于最差的一个service

## Websocket
基于单条TCP链接的双向通信

**优点:**

1. 即时的双向通信
2. 提供基于文本和二进制的数据传输

**缺点:**

1.  需要维护活跃链接
2. 没有schema type约束
3. 活跃链接数量有限制65k

## gRPC
基于HTTP2的框架，支持双向流

**优点:**

1. 轻量级二进制信息
2. schema-based，code generation withProtobuf
3. 提供event-driven架构支持: server-side streaming, client-side streaming, and bi-directional streaming
4. 支持并行请求

**缺点:**

1.  浏览器支持少
2. 学习曲线高
3. 可读性不高
