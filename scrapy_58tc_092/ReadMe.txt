1. scrapy 項目的結構

    項目名字 文件夾
        項目名字 文件夾
            spiders 文件夾 (存儲的是爬蟲文件)
                __init__.py
                自定義的爬蟲文件 (＊＊＊核心功能文件＊＊＊)
            __init__.py
            items.py (數據結構的地方、爬取的數據都包含哪些)
            middleware (中間件：代理...等機制)
            pipelines (管道：用來處理下載數據)
            settings (配置文件：robots 協議、ua 定義...等)

2. response 的屬性和方法

    response.text 獲取的是響應的字符串
    response.body 獲取的是二進制數據
