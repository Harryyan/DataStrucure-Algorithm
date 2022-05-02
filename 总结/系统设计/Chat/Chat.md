# 设计一个Chat App


## Clarification

1.  用户数量，避免错误认为是DDoS攻击 (1 million active  user per month)
2. 目标市场：发达国家的流量成本和质量好于发展中国家；语言支持

## Functional Features

1.  Chats list sorted by dates
2. Open 1-1 chat and receive and send message
3. Photo attachments support for chats
4. Message status(sending, send/failed,received) and read receipts

## Non functional
1.  Ofline support
2. Secure message saved
3. Real time notification


## Out of scope

1. edit and delete message
2. group chats
3. sign up or sign in


## High level diagram

![](https://res.cloudinary.com/dwpjzbyux/image/upload/v1651458313/SystemDesign/chat/chat_fdub6t.svg)



## Deep Dive: Api Service

1. Bi-directional Communication Layer
2. HTTP-based layer
3. Cloud Messaging Layer

![](https://res.cloudinary.com/dwpjzbyux/image/upload/v1651466234/SystemDesign/chat/API_deepdive_vxpnws.svg)

### Bi-directional Communication Layer

对于real time双向交互来说，我们可以选取TCP(connection based)或者UDP(connectionless)协议；
**TCP:**  WebSocket (Slack), XMPP (WhatsApp, Zoom, Google Talk), MQTT (IoT, Smart Home, etc).
**UDP:**  WebRTC (Discord, Google Hangouts, Facebook Messenger)

我们选取WebSocket作为我们的双向通信协议，用它来接收和发送消息:

```swift
{
  connection_id: String?
  event_type: "HELLO|MSG_IN|MSG_OUT|MSG_READ|BYE"
  payload: { ... }
}
```

* HELLO - initiates a new connection session (bi-directional).
* MSG_IN - incoming message.
* MSG_OUT - outgoing message.
* MSG_READ - message "read" acknowledgement (bi-directional).
* BYE - closes a connection session

BTW: URLSessionWebSocketTask

### HTTP-based layer
这部分用来获取分页的chat list以及某个chat room的部分聊天信息

* GET /login - initiates a new client session and returns a JSON Web Token token for authorizing further requests.
* GET /chats?after_id=<X>&limit=<Y> - receives a paginated list of chats.
* GET /chats/<chat_id>/messages?after_id=<X>&limit=<Y> - receives a paginated list of messages from a specific chat.


### Cloud Messaging Layer
APNS用来唤醒非active状态下的app，唤醒tcp链接:

```swift
{
  user_id: String
  messages: [
    {
      user_name: String
      text: String
      created_at: String
    },
    ...
  ]
}
```

## Deep Dive: Data Model

![](https://res.cloudinary.com/dwpjzbyux/image/upload/v1651467838/SystemDesign/chat/table_d9ar0e.svg)



## Deep Dive: Attachments

注意处理upload(outgoing)和download(incoming), 通过http client处理.




