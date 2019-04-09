# flask-project
flask高并发标准项目框架  
启动服务：  
gunicorn -c gun.py manage:app  

新增接口方式：  
1.app/_apis/firstApi.py下注册新的api  
2. app/_apis下新建相对应的views文件，views类继承app/base.py内的类  
3.app/base.py下我用了两种方式获取post请求，一种是restful方式，一种是自定义；  
  两种方式的区别为：例如使用postman发送post请求，restful方式只接收json格式的请求体，而我自定义方法可以接收text、json

有关性能方面的配置在gun.py中
