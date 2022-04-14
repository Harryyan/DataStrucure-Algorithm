# 即时通讯

## Push Notification

**优点:**

1. 易于实现
2. 可唤醒在killed和后台状态的app

**缺点:**

1. 无法保证 100%到达率
2. 效率低，传输速率慢
3. 用户忽略率高


## HTTP polling
分为short polling 和 long polling

### Short Polling

**优点：**

1. 简单易实现，开销不大
2. 不需要持有长链接

**缺点:**

1. 数据延迟
2. 额外的TLS开销等

### Long Polling

**优点：**

1. 即时数据，无延迟

**缺点:**

1. 占用过多服务端资源
2. 实现复杂
3. 持有长链接(keeps a persistent connection.)

## Server-Sent Events(SSE)
客户端和服务端建立一条长链接，服务端通过HTTP链接下发消息，客户端健听:
https://nickarner.com/notes/working-with-server-sent-events-in-swift-november-16-2021/

**优点：**

1. 即时通信

**缺点:**

1. 持有长链接(keeps a persistent connection.)

## Web-Socket
提供双向通信

**优点：**

1. 可支持二进制和文本格式的数据

**缺点:**

1.  实现复杂
2. 持有长链接(keeps a persistent connection.)
