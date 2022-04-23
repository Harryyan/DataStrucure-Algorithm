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



<!--![](https://res.cloudinary.com/dwpjzbyux/image/upload/v1649187948/SystemDesign/DropBox/high-level_r1hvxn.png)
-->