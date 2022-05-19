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
4. Performance benchmark

## High-Level Diagram

![](https://res.cloudinary.com/dwpjzbyux/image/upload/v1650713366/SystemDesign/Cache-Lib/cache-high_mhgj03.png)

**Dispatcher:** 外界负责协调异步调用Cachelib做读写的代码，例如 Task{}, 或者是GroupTask

**CacheLib:** 缓存主类

**Journal:** 缓存数据的metadata，例如访问次数，时间戳，大小等等

**in-memory cache:** 支持快速访问的内存缓存，单一访问为串行

**disk cache:** 本地磁盘缓存，访问较慢

**Eviction:** 当缓存满了，需要执行删除操作（基于策略LRU, LFU等）

实线箭头表示单一访问串行调用，虚线是回函数，回归dispatch上下文(类似await后面的内容，回到主线程)

## Deep Dive

### Dispatcher
若使用协程，则外界可以使用unstructured task或者group task去调用cachelib；若使用OperationQueue，则要配置并发队列，限制线程数.

### Journal
| name | type |
| ----------- | ----------- |
| key      | String       |
| path      | String       |
| size_bytes   | Int        |
| access_count   | Int        |
| state   | Int        |
| last_accessed   | Date        |

每当我们操作缓存时，需要维护每个缓存项的meta data，以便日后更新；可以使用多种方式存储：**text/binary, property list, relational data base(ORM)**

meta data里path存储了数据路径， state代表cache item当前状态，例如CLEAN, DIRTY, REMOVE; 这是为了确保数据和meta data一致性(并发状态下)；当创建或者更新cache item时，数据状态是DIRTY，等到结束时，才mark为CLEAN或者REMOVE.

或者使用Journal直接存储BLOB类型数据，这样就避免了同步journal和file system:

| name | type |
| ----------- | ----------- |
| key      | String       |
| data      | Data       |
| size_bytes   | Int        |
| access_count   | Int        |
| last_accessed   | Date        |

### Cache Eviction
Cache eviction 遵循 **Single Reponsibility**，处理in memory 和 disk cache过载问题。对于in  memory cache, 使用自平衡树来处理；注意和字典的对比，优劣势.

## Follow up

### Sensitive Information
需要问清楚是整体加密还是按需加密；加密解密耗CPU，有性能担忧;
加密的秘钥要存keychain/keystore

### Cross-platform Support
需要封装common module，例如eviction，journal，数据库；不同平台需要写调用层.