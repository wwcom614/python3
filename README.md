# SparkSQLLogGen.py
我用Python3写的模拟互联网日志生成工具for project: 生成日志文件->SparkSQL(ETL)->SparkSQL(Rdd2DataFrame)->SparkSQL(STAT)->MySQL。  
- 使用方法：  
python SparkSQLLogGen.py [生成记录数] [生成日志的路径]  
参数默认值：  
生成记录数如果不填写，默认生成1000条记录  
生成日志的路径，默认在LogGen.py当前目录下 
- 生成日志的格式:  
记录内字段间\t分隔，记录间\n分隔  
字段1：IP(项目所需字段，ETL提取)  
字段2：-  
字段3：-  
字段4：时间，[DD/MMM/YYYY hh:mm:ss +800] (项目所需字段，ETL提取)  
字段5："POST"或"GET"  
字段6："相对URL地址"  
字段7："HTTP1.0"  
字段8："HTTP状态码"   
字段9："消耗流量字节数"(项目所需字段，ETL提取)  
字段10："用户访问的URL" (项目所需字段，ETL提取)  
- 示例：  
108.112.152.76	-	-	[25/DEC/2018 17:29:34 +0800]	"POST	video/1004	HTTP1.0"	500	2177	"http://www.videonet.com/video/1005"

***

# SparkStreamingLogGen.py
我用Python3写的模拟互联网日志生成工具for project: 生成日志文件->Flume->kafka->SparkStreaming->MySQL。  
- 使用方法：  
python SparkStreamingLogGen.py [生成记录数] [生成日志的路径]  
参数默认值：  
生成记录数如果不填写，默认生成10条记录  
生成日志的路径，默认在LogGen.py当前目录下 
- 生成日志的格式:  
记录内字段间\t分隔，记录间\n分隔  
字段1：时间，YYYY-MM-DD hh:mm:ss  
字段2：URL  
字段3：IP  
字段4：搜索引擎跳转IP或为-  
字段5：http的状态码  
- 示例：  
2018-05-07 14:47:35	video/004.html	178.98.158.232	http://search.yahoo.com/search?p=小猪佩奇	200

***
