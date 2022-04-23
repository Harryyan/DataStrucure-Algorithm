# 设计一个Cache Library

## Functional Feature
在这里，需要和面试官讨论设计怎样的缓存类库，缓存什么类型，key的类型，磁盘/内存, 平台支持，是否加密，缓存的增删改查等:

1. Users should be able to cache and retrieve raw byte data using strings as keys.
2. Users should be able to configure disk and memory usage limits as a part of library initialization.
3. Users should be able to configure the cache eviction policy as a part of library initialization.
4. Support multi-threading write or read (at least one write, multi reads are fine)

## Non functional feature

1. The cached data should be persistent on the disk.
2. A small subset of items should be kept in memory for quicker access.
3. Once the cache is full - a portion of items should be deleted according to the eviction policy.

## Out of scope

1. User-defined eviction policies.
2. Secure item storage.
3. Cross-platform support.

## High-Level Diagram

<!--![](https://res.cloudinary.com/dwpjzbyux/image/upload/v1650713366/SystemDesign/Cache-Lib/cache-high_mhgj03.png)-->

**Dispatcher:** 外界负责协调异步调用Cachelib的代码，例如 Task{}, 或者是GroupTask

**CacheLib:** 缓存主类

**Journal:** 缓存数据的metadata，例如访问次数，时间戳，大小等等

**in-memory cache:** 支持快速访问的内存缓存，单一访问为串行

**disk cache:** 本地磁盘缓存，访问较慢

**Eviction:** 当缓存满了，需要执行删除操作（基于策略LRU, LFU等）

实线箭头表示单一访问串行调用，虚线是回函数，回归dispatch上下文(类似await后面的内容，回到主线程)

## Deep Dive
