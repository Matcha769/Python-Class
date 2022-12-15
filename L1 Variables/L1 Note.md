# L1 Variables (變數)
###### tags: `Python`
這邊有共筆版本的[Hackmd](https://hackmd.io/@MatchaCode/Variables)

## 目錄
<a href=#•-Definition-(定義)>• Definition (定義)</a>
<br>
<a href=#•-Variables-Assignment-(變數指派)>• Variables Assignment (變數指派)</a>
<br>
<a href=#•-Multiple-Assignment-(多重指派)>• Multiple Assignment (多重指派)</a>
<br>
<a href=#•-Deleting-Variables-(刪除變數)>• Deleting Variables (刪除變數)</a>
<br>
<a href=#•-Naming-Rules-(命名規則)>• Naming Rules (命名規則)</a>
<br>
<a href=#•-Keywords-(關鍵字)>• Keywords (關鍵字)</a>
<br>
<a href=#•-Standard-Naming-Conventions-(標準命名規則)>• Standard Naming Conventions (標準命名規則)</a>
<br>
<a href=#•-Single-Line-comments-(單行註解)>• Single Line comments (單行註解)</a>
<br>
<a href=#•-Multi-Line-comments-(多行註解)>• Multi Line comments (多行註解)</a>
## • Definition (定義)

什麼是變數呢?

假如我們今天希望電腦可以幫我們存取某個值，它可以是一段文字或著是一個數值，而這些幫我們儲存<font color='red'>**值**</font>的東西我們就稱為<font color='red'>**變數**</font>。

所以我們可以認為<br>
><font color='blue'>變數是一個可以儲存資料(值)的容器，而我們可以透過變數去改變它裝載的值</font>
<hr>

## • Variables Assignment (變數指派)
要如何去指派一個新的變數來裝我們想要放入的值呢?

我們可以使用 = (equal) 符號來指派值到變數，具體示範如下

```python
age = 18
name = "matcha"
height = 183.5
```
以上三行分別代表了三個變數的指派

在第一行可以看到我們將變數的名稱命名為<font color='red'>**age**</font>，而指派給他的值是一個數值<font color='red'>**18**</font>。

在第二行可以看到我們將變數的名稱命名為<font color='red'>**name**</font>，而指派給他的值是一段文字<font color='red'>**matcha**</font>。

在第三行可以看到我們將變數的名稱命名為<font color='red'>**height**</font>，而指派給他的值是一個數值<font color='red'>**183.5**</font>。

因此我們可以看出來變數指派的方式為<br>
><font color='blue'>變數名稱 = 值</font>
<hr>

## • Multiple Assignment (多重指派)
有辦法在一行中同時指派多個變數嗎?

我們可以使用以下方法達成同樣的效果

```python
age, name, height = 18, "matcha", 183.5
```
在上述用法中，我們同時指派了age, name, height為 = 符號右方相對應的值。

所以多重指派的用法為<br>
><font color='blue'>變數一, 變數二, 變數三 = 變數一的值, 變數二的值, 變數三的值</font>
<hr>

## • Deleting Variables (刪除變數)
如果有不需要使用的變數可以怎麼做呢?

我們可以使用 del (delete) 來刪除不需要的變數，具體示範如下

```python
del age
```
如此一來，我們就無法再使用age這個變數了。

所以刪除變數的用法為<br>
><font color='blue'>del 變數名稱</font>
<hr>

## • Naming Rules (命名規則)
可以把變數的名稱取成任何自己想要的樣子嗎?

在Python中，變數命名有一套它的規則，我們先看幾個範例。
```python
1name = "Jack"
num-1 = 10
dollars$ = 1000
```
以上三行是錯誤的命名示範

在第一行可以看到我們將變數的名稱命名為<font color='red'>**1name**</font>，但是請記住<font color='red'>**數字**</font>不能為變數名稱的<font color='red'>**開頭**</font>。

在第二、三行可以看到我們將變數的名稱命名為<font color='red'>**num-1**</font>以及<font color='red'>**dollars$**</font>，但是請記住只有<font color='red'>**_ (下底線)**</font>是唯一可以在變數命名中使用的符號。

我們再看幾個正確的範例。
```python
number1 = 10
name_2 = "Jack"
_dollars = 1000
```
以上三行命名皆符合規則，是正確的命名方式。

因此我們可以知道變數命名的規則有幾個要點<br>
<font color='blue'>
|No.   |Rules                         | 
|-----|--------                      |
|1    |變數名稱只能有字母、數字及下底線 |
|2    |變數名稱必須由字母或下底線開頭   |
|3    |變數名稱不能由數字開頭          |
</font>
<hr>
</font>

## • Keywords (關鍵字)
所以每個單字都可以用來命名變數嗎?

在Python中，有些特殊詞彙是有特殊意義的，我們不能使用這些單詞來命名變數，詳細如下。
<font color='blue'>
|Line1 |Line2 |Line3 |Line4 |Line5 |Line6 |
|------|------|------|------|------|------|
|False |None  |True  |and   |as    |assert|
|break |class |continue|def |del   |elif  |
|else  |except|finally|for  |from  |global|
|if    |import|in    |is    |lambda|nonlocal|
|not   |or    |pass  |raise |return|try   |
|while |with  |yield |
</font>
<hr>
</font>

## • Standard Naming Conventions (標準命名規則)

有那些常見的命名方法呢?

* Pascal case<br>
其要點為每個單字開頭為<font color='red'>**大寫**</font>。
    * ```python
      ThisIsPascalCase = 0
      AnotherPascalCase = 0
      ```
* Camel case<br>
其要點為除第一個單字以外開頭為<font color='red'>**大寫**</font>。
    * ```python
      thisIsCamelCase = 0
      ```
* Snake case<br>
其要點為用<font color='red'> **_ (下底線)** </font>分隔單字。
    * ```python
      this_is_snake_case = 0
      ```
<hr>

## • Single Line comments (單行註解)
如果我想要在程式裡面放上說明該怎麼做?

在Python中可以用<font color='red'>**#(井字號)**</font>來代表單行註解，具體示範如下。
```python
# we define a variable named age here
age = 18

name = "matcha" # You can also comment like this
```
由此我們可以看出<br>
><font color="blue">在 # 之後那一行的文字都會被當成註解，不會被程式執行。</font>
<hr>

## • Multi Line comments (多行註解)
如果我想要有好多行註解該怎麼做?

在Python中可以用<font color='red'>**"""**</font>或是<font color='red'>**'''**</font>來代表單行註解，具體示範如下。
```python
'''
This is a comment
and it contains more than one line.
'''

"""
This is a comment too
single quotations and double quotations
give the same results in Python.
"""
```
由此我們可以看出<br>
><font color="blue">在第一個"""到第二個"""之間的文字都會被當成註解，不會被程式執行。</font>
<hr>

## • 希望這些筆記可以幫到你 •
如果有興趣了解更多歡迎追蹤我的<br>
<font size=3>[Intagram](https://www.instagram.com/matcha_code/)</font><br>
<font size=3>[Youtube](https://www.youtube.com/@matchacode)</font>
<br>
<font size=3>[Github](https://github.com/OG-Matcha/Python-Class)</font>
<br>

<a href="https://hackmd.io/@MatchaCode/Primitive-types" role="button" style="display:block; text-align:right;"> 下一篇: L2 Primitive types (原始型態)</a>
