### write

write是一个Unix命令行程序和内建指令，功能是写到一文件中

#### 原型

~~~c
ssize_t write (int fd,const void * buf,size_t count);
~~~

`write()`会把指针`buf`所指的内存写入`count`个字节到参数`fd`所指的文件内

#### 返回值

如果顺利`write`()会返回实际写入的字节数。当有错误发生时则返回`-1`，错误代码存入errno中

---

### read

`read()`会把参数`fd`所指的文件传送`count`个字节到`buf`指针所指的内存中

#### 原型

~~~c
ssize_t read (int fd, void *buf, size_t count);
~~~

#### 返回值

成功返回读取的字节数，出错返回-1并设置errno，如果在调read之前已到达文件末尾，则这次read返回0。

---



### memcpy

`memcpy`指的是*c*和*c++*使用的内存拷贝函数，`memcpy函数`的功能是**从源*src*所指的内存地址的起始位置开始拷贝*n*个字节到目标*dest*所指的内存地址的起始位置中**。

#### 函数原型

~~~c
void *memcpy(void *dest, const void *src, size_t n);
~~~

#### 返回值

函数返回指向*dest*的指针

---

### memset

`memset`是计算机中*C/C++*语言初始化函数。作用是**将某一块内存中的内容全部设置为指定的值**， 这个函数通常为新申请的内存做初始化工作，它是对较大的[结构体](https://baike.baidu.com/item/结构体)或[数组](https://baike.baidu.com/item/数组)进行清零操作的一种最快方法。

#### 函数原型

~~~c
void *memset(void *buffer, int c, int count) 
~~~

将`buffer`中当前位置后面的`count`个字节，用`c`替换并返回`buffer`。

---

### sprintf

`sprintf`指的是**字符串格式化命令**，主要功能是**把格式化的数据写入某个字符串中**。`sprintf` 是个[变参](https://baike.baidu.com/item/变参/9844833)函数。使用`sprintf` 对于写入`buffer`的字符数是**没有限制**的，这就存在了`buffer`溢出的可能性。解决这个问题，可以考虑使用 [`snprintf`](https://baike.baidu.com/item/snprintf)函数，该函数可对写入字符数做出限制。

#### 函数原型

~~~c
int sprintf( char *buffer, const char *format, [ argument] … );
~~~

#### 参数列表

**buffer**：[char](https://baike.baidu.com/item/char)型指针，指向将要写入的字符串的缓冲区。

***format***：格式化字符串。

***[argument]..*****.**：可选参数，可以是任何类型的数据。

#### 返回值

返回写入`buffer` 的字符数，出错则返回`-1`. 如果 `buffer` 或 `format` 是空指针，且不出错而继续，函数将返回`-1`，并且 *errno* 会被设置为 *EINVAL*。

`sprintf` 返回以**format为格式argument为内容组成的结果**被写入`buffer` 的字节数，结束字符`‘\0’`不计入内。即，如果`“Hello”`被写入空间足够大的`buffer`后，函数`sprintf` 返回`5`。

同时`buffer`的内容将被改变。

---

### strcat

将两个char类型连接。

#### 函数原型

~~~c
extern char *strcat(char *dest, const char *src);
~~~

#### 功能

把`src`所指向的字符串（包括`“\0”`）复制到`dest`所指向的字符串后面（删除`dest`原来末尾的`“\0”`）。要保证`dest`足够长，以容纳被复制进来的`src`（`dest`和`src`所指区域不可以重叠）。`src`中原有的字符不变。返回指向`dest`的[指针](https://baike.baidu.com/item/指针)。

---

### atoi

`atoi` (表示 *ascii to integer*)是把字符串转换成整型数的一个函数，应用在计算机程序和办公软件中。

#### 原型

~~~c
int atoi(const char *nptr)
~~~

#### 功能

函数会扫描参数 `nptr`字符串，**会跳过前面的空白字符**（例如空格，tab缩进）等。如果 `nptr`不能转换成 `int` 或者 `nptr`为空字符串，那么将返回 `0`。特别注意，该函数要求被转换的字符串是按十进制数理解的。`atoi`输入的字符串对应数字存在大小限制（与`int`类型大小有关），若其过大可能报错`-1`。

---

### wcslen

#### 原型

~~~c++
size_t wcslen（const wchar_t * str）
~~~

#### 功能

返回**宽字符串**的**长度**，即在终止空宽字符之前的非空宽字符数。

---

### HeapCreate

进程中创建辅助堆栈

#### 原型

~~~c
HANDLE WINAPI HeapCreate(
_In_ DWORD  flOptions,
_In_ SIZE_T dwInitialSize,
_In_ SIZE_T dwMaximumSize
);
~~~

#### 参数

第一参数 **flOptions** 表示对堆的操作如何进行，可以是`0`，`HEAP_NO_SERIALIZE`，`HEAP_GENERATE_EXCEPTIONS`，`HEAP_CREATE_ENABLE_EXECUTE`。
默认情况下，对堆的访问会依次进行，多个线程会从同一个堆中分配释放内存，堆数据不被破坏。
但在多线程情况下，要尽量避免使用`HEAP_NO_SERIALIZE`。如果想在堆中放可执行代码，必须使用 `HEAP_CREATE_ENABLE_EXECUTE`。
第二参数**dwInitialSize**表示开始时分给堆的字节数。
第三参数**dwMaximumSize**表示所能增长到的最大大小，如果指定为0的话，则堆可以在需要的情况下不断增大。

---

### __readfsqword

Microsoft专用，从指定相对于FS段的开头的偏移量的位置读取内存。

#### 原型

~~~c
unsigned __int64 __readfsqword(
   unsigned long Offset
);
~~~

#### 参数

*Offset*：[in]从开始处的偏移量`FS`读取。

#### 返回值

内存内容的字节、 字、 双字或四字 （如所示的调用的函数名称） 的位置`FS:[Offset]`。

---

### fprintf

`fprintf()`函数根据指定的格式(*format*)向输出流(*stream*)写入数据(*argument*)。

#### 原型

~~~c
int fprintf( FILE *stream, const char *format, [ argument ]...)
~~~

---

### fgets

从指定的流 stream 读取一行，并把它存储在 **buf** 所指向的字符数组内

#### 原型

~~~c
char *fgets(char *buf, int bufsize, FILE *stream);
~~~

#### 参数

`*buf`: 字符型指针，指向用来存储所得数据的地址。
`bufsize`: 整型数据，指明存储数据的大小。
`*stream`: 文件结构体指针，将要读取的文件流。

---

### fputs

C语言库函数，把字符串写入到指定的流( stream) 中，但不包括空字符。

#### 原型

~~~c
int fputs(const char *str, FILE *stream);
~~~

#### 参数

（1）str：这是一个数组，包含了要写入的以空字符终止的字符序列。

（2）stream：指向 FILE 对象的指针，该 FILE 对象标识了要被写入字符串的流

---

### fseek

[重定位](https://baike.baidu.com/item/重定位)流([数据流](https://baike.baidu.com/item/数据流)/文件)上的文件内部位置[指针](https://baike.baidu.com/item/指针)

#### 原型

~~~c
int fseek(FILE *stream, long offset, int fromwhere);
~~~

函数设置文件指针`stream`的位置。如果执行成功，**`stream`将指向以`fromwhere`**（偏移起始位置：[文件头](https://baike.baidu.com/item/文件头)0(SEEK_SET)，当前位置1(SEEK_CUR)，文件尾2(SEEK_END)）**为基准**，**偏移*offset***（指针偏移量）**个字节的位置**。如果执行失败(比如*offset*超过文件自身大小)，则不改变`stream`指向的位置。

---

### strstr

#### 函数原型：

~~~c
extern char *strstr(char *str1, const char *str2);
~~~

#### 参数：

str1：被查找目标

str2：要查找对象

返回值：若`str2`是`str1`的子串，则返回`str2`在`str1`的**首次出现的地址**；如果`str2`不是`str1`的子串，则返回**NULL**。

---

### putenv

#### 功 能:

  `putenv()`用来**改变或增加环境变量**的内容。参数`envvar`的格式为`envvar`=`value`，如果该环境变量原先存在，则变量内容会依参数`envvar`改变，否则此参数内容会成为新的环境变量。参数`envvar`指定的字符串会变成环境变量的一部分，如果修改这个字符串，环境变量也会跟着被修改。

#### 函数原型：

~~~c
int _putenv(
   const char *envstring 
);
~~~

#### 参数：

envstring  环境字符串定义。

---

### string::c_str

`c++`中，string类串不以*NULL*(`'\0'`)结尾，而C风格的字符串以NULL结尾，因此当从string类串中提取字符串后，要在尾部加上结尾符。

#### 原型

~~~c++
const char *c_str() const;
~~~

#### 功能

返回指针，指向string类对象中的字符串，末尾加上`'\0'`

---

### GetDlgItemText

`GetDlgItemText`是C++中的函数，调用这个函数以**获得与对话框中的控件相关的标题或文本**。`GetDlgItemText`成员函数将文本拷贝到lpStr指向的位置并返回拷贝的字节的数目。

#### 函数原型

~~~c++
int GetDlgItemText( HWND hDlg , int nID, LPTSTR lpStr, int nMaxCount) const;
int GetDlgItemText( int nID, CString& rString) const;
~~~

#### 参数

`nID` 指定了要获取其标题的控件的整数标识符。

 `lpStr` 指向要接收控件的标题或文本的缓冲区。

 `nMaxCount` 指定了要拷贝到`lpStr`的字符串的最大长度（以字节为单位）。

如果字符串比nMaxCount要长，它将被截断。 

`rString` 对一个`CString`对象的引用。

#### 返回值

如果函数**调用成功**，返回值为**拷贝到缓冲区中的 `TCHAR` 字符个数**（不包括结束空字符）。
如果函数**调用失败**，**返回值为 `0`** 。要获取更多错误信息，请调用 `GetLastError` 函数。

---

### calloc

`calloc`是一个ISO C函数

#### 原型

~~~c
void *calloc(size_t n, size_t size)；
~~~

#### 功能

 在内存的动态存储区中**分配`n个`长度为`size`的连续空间**，函数返回一个指向分配起始地址的指针；如果分配不成功，返回`NULL`。

#### 与malloc的区别

`calloc`在动态分配完内存后，**自动初始化该内存空间为零**，而`malloc`不初始化，里边数据是随机的垃圾数据。

---

### strchr

说明：返回首次出现_Val的位置的指针，返回的地址是被查找字符串指针开始的第一个与Val相同字符的指针，如果Str中不存在Val则返回NULL。

#### 原型

~~~c
extern char *strchr(const char *s,char c)
~~~

#### 返回值

成功则返回要查找字符第一次出现的位置，失败返回NULL

---

### execve系统调用

#### 原型

~~~c
int execve(const char *filename, char *const argv[],char *const envp[]);
~~~

`fork`创建了一个新的进程，产生一个新的`PID`
`execve`用被执行的程序完全替换了调用进程的映像。
`execve`启动一个新程序，替换原有进程，所以被执行进程的PID不会改变。

#### 参数

`execve`函数接受三个参数

~~~
--path    要执行的文件完整路径
--argv    传递给程序完成参数列表，包括argv[0]，它一般是执行程序的名字，最后一个参数一般是NULL
--envp    是指向执行execed程序的环境指针，一般设为NULL
~~~



