# **web-crawler**
此專案主在爬取 Potato Media 網路論壇的貼文連結。


## 目錄
---
1. [什麼是 Potato Media？](#什麼是PotatoMedia？)
2. [概述](#概述)  
    2.1 [基本環境](#基本環境)  
    2.1 [實作](#實作)


## 什麼是 Potato Media？
Potato Media 是全台第一社交挖礦論壇，有別於其他平台，只要在站內做出任何內容或互動貢獻，皆可直接獲得收益。互動內容包含：
- 按讚
- 留言
- 文章被按讚
- 文章被留言 
- 邀請好友
- 完成每日任務  

## 概述
<<<<<<< HEAD
---
### 基本環境
本專案使用 Python3，及 Poetry 套件管理環境。  
相關套件使用請見 `pyproject.toml` 。
- 溜覽器：使用 `chromedriver`
=======
### 基本環境
本專案使用 Python3，及 Poetry 套件管理環境，相關套件使用請見 `pyproject.toml` 。
- 瀏覽器：使用 `chromedriver`
>>>>>>> a0ab13371b9f1e421efab09246335f1b3b01cfcc

### 實作
- 自行輸入
  - `post_cnt`：可設定爬取文章連結數量
  - 計算程式執行秒數
- Python
  - `common.py`：主要儲存爬取文章時會用到的套件，包括`Selenium`、`open()`等相關共用方法。
  - `craw_post.py`：主要程式

- Json 文件
  - `account.json`：存放登入帳號與網站相關url
  - `cookies.json`：可用來存取網站登入cookie（此部分尚未開發完成）
  - `post.json`：爬取後的文章連結會寫入此檔案
