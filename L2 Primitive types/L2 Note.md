# L2 Primitive types (原始型態)
###### tags: `Python`

## 目錄
<a href=#•-Definition-(定義)>• Definition (定義)</a>
<br>
<a href=#•-Numeric-Types-(數值型態)>• Numeric Types (數值型態)</a>
<br>
&emsp;<a href=#•-Integer-(整數)>• Integer (整數)</a>
<br>
&emsp;<a href=#•-Floating-Point-(浮點數)>• Floating Point (浮點數)</a>
<br>
&emsp;<a href=#•-Boolean-(布林值)>• Boolean (布林值)</a>
<br>
<a href=#•-Text-Sequence-Types-(文字序列型態)>• Text Sequence Types (文字序列型態)</a>
<br>
&emsp;<a href=#•-String-(字串)>• String (字串)</a>
## • Definition (定義)

什麼是原始型態呢?

原始型態就是在Python中內建的基本型態，裡面包含了最單純的資料型別，而這些基本型態也是組成其他更多更複雜結構的基礎。

所以我們可以認為<br>
><font color='blue'>原始型態是一系列基本的資料型別，也是構築其他資料結構的基礎。</font>
<hr>

## • Numeric Types (數值型態)
那些資料屬於數值呢?

基本上數值型態有三個，分別是
* Integer (整數)
* Floating Point (浮點數)
* Boolean (布林值)
<hr>

### • Integer (整數)
什麼是整數呢?

我們可以廣義地將整數定義為<font color='red'>**不含小數點的數值**</font>，具體示範如下。

```python=
positive_integer_number = 10
negative_integer_number = -18
```
從上面得結果我們可以看出整數的範圍包含了正值及負值。

在Python中，我們可以用內建的type()函式來查看資料型態，具體示範如下。

```python=
number = 18
type(number) # <class 'int'>
```
上述的程式會產生如註解顯示的<font color='red'><class 'int'></font>這個結果，他指出了<font color='red'>number</font>這個變數被指定的值是屬於<font color='red'>int</font>這個型態，而<font color='red'>int</font>正是<font color='red'>integer</font>在Python中的簡寫。
    
因此我們可以看出整數的幾個重點<br>
><font color='blue'>
|No.  |Rules                | 
|-----|--------             |
|1    |整數為不包含小數點的數值  |
|2    |整數可以包含正值及負值   |
|3    |整數在程式中以int表示    |
    
</font></font>
<hr>

### • Floating Point (浮點數)
什麼是浮點數呢?

我們可以將浮點數認為是<font color='red'>**包含小數點的數值**</font>，具體示範如下。

```python=
positive_float_number = 18.54
negative_float_number = -14.3
whole_float_number = 15.0
omit_zero_float = 15.
```
從上面得結果我們可以看出浮點數的範圍同樣包含了正值及負值，比較特別的是<font color='red'>屬於浮點數的數值都包含小數點</font>，比較特別的是第三行，即使小數點後是沒有任何數值，但因為出現了小數點，所以屬於float型態，還有在第四行的表示方式是<font color='red'>省略掉了小數點後的0</font>，所以直接打上<font color='red'> . </font>就結束了，其結果和第三行相同。

我們同樣可以用內建的type()函式來查看資料型態，具體示範如下。

```python=
number = 18.4
type(number) # <class 'float'>
```
上述的程式會產生如註解顯示的<font color='red'><class 'float'></font>這個結果，他指出了<font color='red'>number</font>這個變數被指定的值是屬於<font color='red'>float</font>這個型態，而<font color='red'>float</font>正是<font color='red'>floating point</font>在Python中的簡寫。
    
因此我們可以看出浮點數的幾個重點<br>
><font color='blue'>
|No.  |Rules                  | 
|-----|--------               |
|1    |浮點數為包含小數點的數值    |
|2    |浮點數可以包含正值及負值    |
|3    |浮點數的小數部分若為0可省略 |
|4    |浮點數在程式中以float表示  |
    
</font></font>
<hr>

### • Boolean (布林值)
什麼是布林值呢?

我們可以狹義地將布林值認為是<font color='red'>**True**</font>和<font color='red'>**False**</font>，具體示範如下。


```python=
is_adult = True
finish_work = False
```
從上面得結果我們可以看出布林值的值只有兩種，<font color='red'>**True**</font>和<font color='red'>**False**</font>，這是一種較常被使用在條件或比較式中的一個資料型態，表示某個情況或條件是否成立。

當然，布林值並沒有這麼簡單，我們會在之後的課程對他進行更詳細的說明。

我們同樣可以用內建的type()函式來查看資料型態，具體示範如下。

```python=
boolean = True
type(boolean) # <class 'bool'>
```
上述的程式會產生如註解顯示的<font color='red'><class 'bool'></font>這個結果，他指出了<font color='red'>boolean</font>這個變數被指定的值是屬於<font color='red'>bool</font>這個型態，而<font color='red'>bool</font>正是<font color='red'>boolean</font>在Python中的簡寫。
    
因此我們可以看出布林值的幾個重點<br>
><font color='blue'>
|No.  |Rules                  | 
|-----|--------               |
|1    |布林值包含了True和False   |
|2    |布林值在程式中以bool表示  |
    
</font></font>
<hr>

## • Text Sequence Types (文字序列型態)
那些資料屬於文字序列呢?

基本上文字序列型態有一個，就是
* String (字串)

### • String (字串)
什麼是字串呢?

我們可以字串定義為<font color='red'>**一段文字**</font>或<font color='red'>**字元**</font>，具體示範如下。

```python=
# With double quotations
paragraph = "Hello World!"
character = "A"
number_string = "1234"

# With single quotaitons
paragraph = 'Hello World~'
character = 'a'
number_string = '5678'
```
從上面得結果我們可以看出字串可以是<font color='red'>**一段文字**</font>或<font color='red'>**一個單字**</font>甚至是<font color='red'>**一個數字**</font>。而當我們使用<font color='red'>**""**</font>或是<font color='red'>**''**</font>來包住這些資料時，他們就會屬於字串型態，在此時此刻，他們就是一段文字。在Python中，無論是單引號或是雙引號都是代表字串，其中並無差別。比較需要注意的是以下部分。

```python=
# You can't do this
string = "Start with double but end with single.'
string = 'Start with single but end with double."
```
Python從引號來判斷是否為字串，雖然<font color='red'>**""**</font>和<font color='red'>**''**</font>並無差別，但一次只能選用一種，頭尾必須一致，否則會造成錯誤。

```python=
# This is not accepted
string = "He just said "Hi" to me."
string = 'He just said 'Hi' to me.'

# Double outside and single inside
string = "He just said 'Hi' to me."

# Single outside and double inside
string = 'He just said "Hi" to me.'
```
剛剛知道了字串是由包住他的引號來判斷，但問題出現了，如果想要在字串裡面使用引號，如同第二三行的用法可以看出是不可行的，若一定要使用引號可以選擇使用和<font color='red'>外部用來判斷字串不同的引號</font>來代表文字內的引號，第六及第九行即是正確的結果。

在Python中，我們可以用內建的type()函式來查看資料型態，具體示範如下。

```python=
text = "string is easy"
type(text) # <class 'str'>
```
上述的程式會產生如註解顯示的<font color='red'><class 'str'></font>這個結果，他指出了<font color='red'>text</font>這個變數被指定的值是屬於<font color='red'>str</font>這個型態，而<font color='red'>str</font>正是<font color='red'>string</font>在Python中的簡寫。
    
因此我們可以看出字串的幾個重點<br>
><font color='blue'>
|No.  |Rules                            | 
|-----|--------                         |
|1    |字串由是否被引號包括判斷              |
|2    |字串頭尾的引號必須一致               |
|3    |若要在內部使用引號，須和外部引號不同    |
    
</font></font>
<hr>

## • 希望這些筆記可以幫到你 •
如果有興趣了解更多歡迎追蹤我的<br>
<font size=3>[Intagram](https://www.instagram.com/matcha_code/)</font>
<br>
<font size=3>[Youtube](https://www.youtube.com/@matchacode)</font>
<br>
<font size=3>[Github](https://github.com/OG-Matcha/Python-Class)</font>

<a href="https://hackmd.io/@MatchaCode/Variables" role="button" style="display:block; text-align:left;"> 上一篇: L1 Variables (變數)</a>
