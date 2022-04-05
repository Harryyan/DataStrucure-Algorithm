# 设计一个Dropbox

## Functional Feature

1. Upload or download Files / Images to server or local
2. Pausing, resuming, cancel, list downloads
3. Media files and non media files support
    1. video and image (different types) - thumbnails, preview
    2. .txt, .pdf, and etc.
4. Files upload and download in background
5. Offline(download)
6. Limitation (big files)

这一步列出最基本的功能，尽可能多的涵盖相关点.

## Non functional feature

1. cpu | data | battery usage
2. thread number


## Out of scope

1. Markets (language, currency)
2. Sensitive file
3. Share / remove file links
4. File extension
5. Http range request
6. in-app purchase
7. auth
8. progress track


## High Level Design

![](https://res.cloudinary.com/dwpjzbyux/image/upload/v1649187948/SystemDesign/DropBox/high-level_r1hvxn.png)

## Deep Dive
 选择文件下载作为深入点:
 
 ![](https://res.cloudinary.com/dwpjzbyux/image/upload/v1649187948/SystemDesign/DropBox/detail_lmzuuo.png)