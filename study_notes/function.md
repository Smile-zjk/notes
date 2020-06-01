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

### sscanf（）

 C 库函数 **int sscanf(const char \*str, const char \*format, ...)** 从字符串读取格式化输入。 

#### 原型

~~~c
int sscanf(const char *str, const char *format, ...)
~~~

#### 参数

* **str**  -- 这是C字符串，是函数检索数据的源。
* **format** 

#### 返回值

如果成功，该函数返回成功匹配和赋值的个数。如果到达文件末尾或发生错误，则返回EOF。

#### 实例

下面的实例演示了`sscanf（）`函数的用法

~~~c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
   int day, year;
   char weekday[20], month[20], dtm[100];

   strcpy( dtm, "Saturday March 25 1989" );
   sscanf( dtm, "%s %s %d  %d", weekday, month, &day, &year );

   printf("%s %d, %d = %s\n", month, day, year, weekday );
    
   return(0);
}
// 运行结果为:March 25, 1989 = Saturday
~~~



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

### strcpy

#### 原型

~~~c
char *strcpy(char *dest, const char *src)
~~~

#### 功能

C 库函数，把 **src** 所指向的字符串复制到 **dest**。

需要注意的是如果目标数组 dest 不够大，而源字符串的长度又太长，**可能会造成缓冲溢出**的情况。

---

### strncpy

 把 `src` 所指向的字符串复制到 **dest**，最多复制 `n` 个字符。当 src 的长度小于 n 时，dest 的剩余部分将用空字节填充。 

#### 原型

~~~c
char *strncpy(char *dest, const char *src, size_t n);
~~~

#### 参数

- **dest** -- 指向用于存储复制内容的目标数组。
- **src** -- 要复制的字符串。
- **n** -- 要从源中复制的字符数。

#### 返回值

该函数返回最终复制的字符串。



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

### fread

#### 函数原型

~~~c
size_t fread ( void *buffer, size_t size, size_t count, FILE *stream) ;
~~~

#### 参数

buffer：用于接收数据的内存地址

size： 要读的每个数据项的字节数，单位是字节

count：要读count个数据项，每个数据项size个字节

stream： 输入流

#### 返回值

返回真实读取的项数，若大于count则意味着产生了错误。

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

### malloc

头文件：#include<stdlib.h>

malloc（）函数用来动态地分配内存空间

#### 原型

~~~c
void* malloc(size_t size);
~~~

#### 参数说明

`size`为需要分配的内存空间的大小，以字节（Byte）计。

#### 函数说明

`malloc（）`在堆区分配一块指定大小的内存空间，用来存放数据。这块内存空间在函数执行后**不会被初始化**，它们的**值是未知的**。如果希望在分配内存的同时进行初始化，请使用`calloc()`函数

#### 返回值

分配成功返回指向该内存的地址，失败则返回NULL。

由于申请内存空间时可能有也可能没有，所以需要自行判断是否申请成功，再进行后续操作。

 如果 size 的值为 0，那么返回值会因标准库实现的不同而不同，可能是 NULL，也可能不是，但返回的指针不应该再次被引用。 

 **注意：函数的返回值类型是 void *，void 并不是说没有返回值或者返回空指针，而是返回的指针类型未知。**所以在使用 `malloc()` 时通常需要进行强制类型转换，将 `void` 指针转换成我们希望的类型，例如： 

~~~c
char *ptr = (char *)malloc(10);   // 分配10个字节的内存空间，用来存放字符
~~~



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

### free()

头文件：#include<stdlib.h>

free()函数用来释放动态分配的内存空间

#### 原型

~~~c
void free(void* ptr);
~~~

#### 参数说明

`ptr`为将要释放的内存空间的地址

free() 可以释放由 `malloc()`、`calloc()`、`realloc()` 分配的内存空间，以便其他程序再次使用。

`free()`只能释放动态分配的内存空间，并不能释放任意的内存。下面的写法是错误的

~~~c
int a[10];
// ...
free(a);
~~~

 如果 `ptr` 所指向的内存空间**不是由上面的三个函数所分配**的，或者**已被释放**，那么调用 `free()` **会有无法预知的情况发生**。 

 如果 `ptr` 为 **NULL**，那么 `free()` 不会有任何作用 

 **注意**：`free()` **不会改变** `ptr` **变量本身的值**，调用 `free()` 后它**仍然会指向相同的内存空间**，但是此时该内存已无效，不能被使用。所以建议将 `ptr` 的值设置为 **NULL**，例如： 

~~~c
free(ptr);
ptr = NULL;
~~~



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

---

### mmap

`mmap`将一个文件或者其它对象映射进内存。文件被映射到多个页上，如果文件的大小不是所有页的大小之和，最后一个页不被使用的空间将会清零。`mmap`在用户空间映射调用系统中作用很大。

#### 原型

~~~c
void* mmap(void* start,size_t length,int prot,int flags,int fd,off_t offset);
int munmap(void* start,size_t length);
~~~

#### 条件

`mmap()` 必须以**PAGE_SIZE**为单位进行映射，而内存也只能以页为单位进行映射，若要映射非**PAGE_SIZE**整数倍的地址范围，要先进行内存对齐，强行以**PAGE_SIZE**的倍数大小进行映射。

#### 参数

~~~
start：映射区的开始地址，设置为0时表示由系统决定映射区的起始地址。
length：映射区的长度。//长度单位是 以字节为单位，不足一内存页按一内存页处理
prot：期望的内存保护标志，不能与文件的打开模式冲突。是以下的某个值，可以通过or运算合理地组合在一起
PROT_EXEC //页内容可以被执行
PROT_READ //页内容可以被读取
PROT_WRITE //页可以被写入
PROT_NONE //页不可访问
flags：指定映射对象的类型，映射选项和映射页是否可以共享。它的值可以是一个或者多个以下位的组合体
MAP_FIXED //使用指定的映射起始地址，如果由start和len参数指定的内存区重叠于现存的映射空间，重叠部分将会被丢弃。如果指定的起始地址不可用，操作将会失败。并且起始地址必须落在页的边界上。
MAP_SHARED //与其它所有映射这个对象的进程共享映射空间。对共享区的写入，相当于输出到文件。直到msync()或者munmap()被调用，文件实际上不会被更新。
MAP_PRIVATE //建立一个写入时拷贝的私有映射。内存区域的写入不会影响到原文件。这个标志和以上标志是互斥的，只能使用其中一个。
MAP_DENYWRITE //这个标志被忽略。
MAP_EXECUTABLE //同上
MAP_NORESERVE //不要为这个映射保留交换空间。当交换空间被保留，对映射区修改的可能会得到保证。当交换空间不被保留，同时内存不足，对映射区的修改会引起段违例信号。
MAP_LOCKED //锁定映射区的页面，从而防止页面被交换出内存。
MAP_GROWSDOWN //用于堆栈，告诉内核VM系统，映射区可以向下扩展。
MAP_ANONYMOUS //匿名映射，映射区不与任何文件关联。
MAP_ANON //MAP_ANONYMOUS的别称，不再被使用。
MAP_FILE //兼容标志，被忽略。
MAP_32BIT //将映射区放在进程地址空间的低2GB，MAP_FIXED指定时会被忽略。当前这个标志只在x86-64平台上得到支持。
MAP_POPULATE //为文件映射通过预读的方式准备好页表。随后对映射区的访问不会被页违例阻塞。
MAP_NONBLOCK //仅和MAP_POPULATE一起使用时才有意义。不执行预读，只为已存在于内存中的页面建立页表入口。
fd：有效的文件描述词。一般是由open()函数返回，其值也可以设置为-1，此时需要指定flags参数中的MAP_ANON,表明进行的是匿名映射。
off_toffset：被映射对象内容的起点。
~~~

#### 返回说明

成功执行时，mmap()返回被映射区的[指针](https://baike.baidu.com/item/指针)，[munmap](https://baike.baidu.com/item/munmap)()返回0。失败时，mmap()返回MAP_FAILED[其值为(void *)-1]，munmap返回-1。errno被设为以下的某个值

~~~
EACCES：访问出错

EAGAIN：文件已被锁定，或者太多的内存已被锁定

EBADF：fd不是有效的[文件描述词](https://baike.baidu.com/item/文件描述词)

EINVAL：一个或者多个参数无效

ENFILE：已达到系统对打开文件的限制

ENODEV：指定文件所在的文件系统不支持内存映射

ENOMEM：[内存不足](https://baike.baidu.com/item/内存不足)，或者进程已超出最大内存映射数量

EPERM：权能不足，操作不允许

ETXTBSY：已写的方式打开文件，同时指定MAP_DENYWRITE标志

SIGSEGV：试着向只读区写入

SIGBUS：试着访问不属于进程的内存区
~~~

---

### strtol()

C 库函数 **long int strtol(const char \*str, char \**endptr, int base)** 把参数 **str** 所指向的字符串根据给定的 **base** 转换为一个长整数（类型为 long int 型），base 必须介于 2 和 36（包含）之间，或者是特殊值 0。

#### 原型

~~~c
long int strtol(const char *str, char **endptr, int base)
~~~

#### 参数

- **str** -- 要转换为长整数的字符串。
- **endptr** -- 对类型为 char* 的对象的引用，其值由函数设置为 **str** 中数值后的下一个字符。
- **base** -- 基数，必须介于 2 和 36（包含）之间，或者是特殊值 0。

#### 返回值

该函数返回转换后的长整数，如果没有执行有效的转换，则返回一个零值。

---

### isalnum

判断字符变量c是否为字母或数字，若是则返回非零，否则返回零。

#### 原型

~~~c
extern int isalnum(int c);
~~~

---

### srand()

 `rand函数`在产生随机数前，需要系统提供的生成伪随机数序列的种子，rand根据这个种子的值产生一系列随机数。如果系统提供的种子没有变化，每次调用rand函数生成的伪随机数序列都是一样的。`srand(unsigned seed)`通过参数`seed`改变系统提供的种子值，从而可以使得每次调用rand函数生成的伪随机数序列不同，从而实现真正意义上的“随机”。通常可以利用系统时间来改变系统的种子值，即srand(time(NULL))，可以为rand函数提供不同的种子值，进而产生不同的随机数序列。 

#### 原型

~~~c
void srand(unsigned int seed)
~~~

#### 参数

 **seed** -- 这是一个整型值，用于伪随机数生成算法播种 

---

### GetDlgItemTextA（）

调用这个函数以**获得**与`对话框中的控件相关的标题`或`文本`

#### 原型

```c++
UINT GetDlgItemTextA(
  HWND  hDlg,
  int   nIDDlgItem,
  LPSTR lpString,
  int   cchMax
);
```

#### 参数

- **hDlg** -- 包含控件的对话框的句柄。
- **nIDDlgItem** -- 要检索其标题或文本的控件的标识符。
- **lpString** -- 用于接收标题或文本的缓冲区。
- **cchMax** -- 要复制到`lpString`指向的缓冲区的字符串的**最大长度**(以字符为单位)。如果字符串的长度(包括null字符)**超过了限制**，则该字符串将**被截断**。

#### 返回值

如果函数**成功**，返回值指定**复制到缓冲区的字符数**，不包括终止null字符。

如果函数**失败**，返回值为**零**。要获取扩展的错误信息，请调用GetLastError。