# LogGen.py
我用Python3写的互联网日志生成工具。  
- 使用方法：  
python LogGen.py [生成记录数] [生成日志的路径]  
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
示例：  
2018-05-07 14:47:35	video/004.html	178.98.158.232	http://search.yahoo.com/search?p=小猪佩奇	200

***
