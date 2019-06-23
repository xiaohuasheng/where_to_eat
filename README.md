# where_to_eat
根据喜欢，就近原则选出要吃什么
## 运行方法  
[点击下载代码和数据文件](https://codeload.github.com/xiaohuasheng/where_to_eat/zip/master)  
解压  
在解压后的目录里面  
按住 shift, 点鼠标右键, 选择“在此处打开Powershell窗口”  
输入 python where_to_eat.py  
按回车运行
```bash
PS C:\Users\xhs\Downloads\where_to_eat-master> python where_to_eat.py
请告诉我你现在在哪里？1宿舍，2饭堂，3图书馆，4教学楼，都不是？请输入5
4
最好的选择是:外婆家
PS C:\Users\xhs\Downloads\where_to_eat-master> python where_to_eat.py
请告诉我你现在在哪里？1宿舍，2饭堂，3图书馆，4教学楼，都不是？请输入5
5
你的坐标是多少？ 比如10,15
5,9
最好的选择是:九龙冰室
PS C:\Users\xhs\Downloads\where_to_eat-master>
```
## 文件介绍  
foods.json 数据文件
```json
  {
    "name": "外婆家", //餐厅名称
    "location": {    //餐厅坐标
      "x": 10,       
      "y": 15
    },
    "favorite": 9    //喜欢程度打分，满分10分
  },

```
where_to_eat.py 功能代码文件
## 添加一个数据
编辑 foods.json，在文件末尾 ] 号之前加入下面这样的数据
```json
  ,{
    "name": "xxx", 
    "location": {    
      "x": 10,       
      "y": 15
    },
    "favorite": 9  
  }
```

