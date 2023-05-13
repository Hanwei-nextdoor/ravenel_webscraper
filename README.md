# Ravenel Webscraper 
## Version 1.0

Ravenel Webscrapper 是一個可以幫助你在[羅芙奧藝術網站](https://ravenel.com/)進行網路爬蟲，並獲得特定一季拍賣會全品項之python程式。

![羅芙奧藝術網站截圖](/pic/ravenel_site.png)

## 簡介 Introduction

此程式擷取台灣羅芙藝術拍賣公司的網頁資料，並提供預設「2022年秋季拍賣會」的藝術品拍品資料。

## 環境設定 Environment

此程式使用兩個 python 資料庫：requests 與 pandas，請確定您的開發環境已安裝此二資料庫。

## 程式碼結構與使用 Code Structure and Usage

此程式碼分作三部分：

1. get_json(url): 爬蟲程式，透過 requests 函式向網站發送請求，獲得網頁資料，並將資料結構轉換為 json。
2. get_lots_data(json): 將獲得的 json 資料轉換成為 python 字典。
3. main()：主要程式，負責獲得含有所有拍品的 url，並透過前二功能獲得資料，將資料轉換為 DataFrame 並輸出 csv 檔案。
    - 您可以透過更改變數'url'，以獲得不同拍賣會的資料。

![程式碼截圖](/pic/code.png)

## 資料結構 Data Structure

此程式可獲得的資料包括：

1. 'auction': 擷取的當季拍賣會名稱，預設為「羅芙奧台北2022秋季拍賣會」
2. 'name': 拍品名稱
3. 'artist': 拍品藝術家姓名
4. 'year': 拍品創作年份
5. 'material': 拍品創作材料
6. 'dimention': 拍品尺寸
7. 'es_price': 拍品估價，以台幣計價
8. 'fin_price': 拍品成交價，以台幣計價， 0 為流標
9. 'cover': 拍品縮圖連結

## 開發者名錄 Contributing

Han-wei Lee @Hanwei_nextdoor on GitHub
hanwei.lee0414@gmail.com

歡迎提交 Pull Requests。

對於重大的更改，請先開立一個 issue ，並向我討論想更改的內容。請確保您在適當環境與情況下更新測試。

請妥善並負責地使用網路爬蟲工具。

## 附錄 Appendix

本專案另附有一Jupyter Notebook 檔案（.ipynb），為利用此程式獲得之資料進行之探索式資料分析（Exploratory Data Analysis）。
