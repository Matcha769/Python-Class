# L3 Type casting (型態轉換)
###### tags: `Python`
這邊有共筆版本的[Hackmd](https://hackmd.io/@MatchaCode/Type-casting)

## 目錄
<a href=#•-Definition-(定義)>• Definition (定義)</a>
<a href=#•-Implicit-Type-Conversion-(隱式轉換)>• Implicit Type Conversion (隱式轉換)</a>
&emsp;<a href=#•-Boolean-V.S-Integer>• Boolean V.S Integer</a>
&emsp;<a href=#•-Integer-V.S-Floating-Point>• Integer V.S Floating-Point</a>
<a href=#•-Explicit-Type-Conversion-(顯式轉換)>• Explicit Type Conversion (顯式轉換)</a>
&emsp;<a href=#•-int()-(整數)>• int() (整數)</a>
&emsp;<a href=#•-float()-(浮點數)>• float() (浮點數)</a>
&emsp;<a href=#•-bool()-(布林值)>• bool() (布林值)</a>
&emsp;<a href=#•-str()-(字串)>• str() (字串)</a>
## • Definition (定義)

什麼是型態轉換呢?

型態轉換就是我們將資料的型態從其中一種轉換為其他型態的過程，也被稱為**Type-Conversion**。

所以我們可以認為<br>
><font color='blue'>型態轉換是我們在進行資料處理時很常使用的功能。</font>
<hr>

## • Implicit Type Conversion (隱式轉換)
甚麼是隱式轉換呢?

基本上這種轉換出現在<font color="red">數值型態</font>當中，就像我們上一篇講到的，數值型態有三種，分別是: 整數、浮點數、布林值。

而他們的值的範圍大小如下顯示:
:::info
boolean ---> integer ---> floating-point
small <---------------------------> large
:::

從上面可以看出
1. boolean包含的範圍最小，嚴格來說只包含:
 $$True\ and\ False$$
3. integer次之，範圍為:$$-2^{32} \sim 2 ^{32} - 1$$
4. floating-point最大，範圍為:$$-1.8 * 10^{308} \sim 1.8 * 10^{308}$$

所以我們可以知道<font color="red">floating-point的範圍 > integer的範圍 > boolean的範圍</font>。

因此當不同型態的資料在做運算時，範圍小的型態會隱式轉型成範圍較大的型態，而<font color="red">結果也會以範圍較大的型態顯示</font>。

### • Boolean V.S Integer
以下為範例:
```python=
num = True + 10 # 11
```
在上述的例子中，我們將boolean和integer做加法，而運算的過程如下:
```python=
# original 
num = True + 10

# implicit cast boolean to integer 
num = 1 + 10

# result
num = 11 # integer
```

這邊有一個很重要的觀念，就是當boolean在轉換成數值的時候有一個規則:
:::info
在轉換boolean的時候要特別注意，True在轉換時只會變成<font color="red">1</font>，而False只會變成<font color="red">0</font>。
:::

再舉一個例子:
```python=
# original 
num = False + 10

# implicit cast boolean to integer 
num = 0 + 10

# result
num = 10 # integer
```

這就是boolean和integer間的隱式轉換。
    
<hr>

### • Integer V.S Floating-Point

以下為範例:
```python=
num = 35 + 11.0 # 46.0
```
在上述的例子中，我們將integer和floating-point做加法，而運算的過程如下:
```python=
# original 
num = 35 + 11.0

# implicit cast integer to floating-point 
num = 35.0 + 11.0

# result
num = 46.0 # floating-point
```

這邊有一個之前提過的很重要的觀念:
:::info
只要有小數點即是floating-point
:::

因此我們可以看出來integer會先轉型成floating-point再做相加，而結果也會是floating-point的型態。

再舉一個例子:
```python=
# original 
num = False + 10 + 12.5

# implicit casting
num = 0.0 + 10.0 + 12.5

# result
num = 22.5 # floating-point
```

現在你們已經了解boolean、integer還有floating-point之間的隱式轉換了。

因此我們可以看出隱式轉換的幾個重點<br>
><font color='blue'>
|No.  |Rules                | 
|-----|--------             |
|1    |浮點數 > 整數 > 布林值  |
|2    |運算結果以最大範圍型態表示|

</font>

<hr>

## • Explicit Type Conversion (顯式轉換)
甚麼是顯式轉換呢?

基本上這種轉換就是我們使用函式指定資料說要轉換成甚麼型態。

這邊有幾個函式可以用:
* int() (整數)
* flaot() (浮點數)
* bool() (布林值)
* str() (字串)

<hr>

### • int() (整數)

具體示範如下:

```python=
num = 10 + int(18.5) # 28
```
從上面得結果我們可以得到結果為整數型態。

在上述的例子中，我們將integer和<font color="red">經過轉型的</font>floating-point做加法，而運算的過程如下:

```python=
# original 
num = 10 + int(18.5)

# explicit cast flaoting-point to integer 
num = 10 + 18

# result
num = 28 # Integer
```

我們可以知道<b>int()</b>可以將值轉換為整數，且小數點部分為<font color="red">無條件捨去</font>。

<hr>

### • float() (浮點數)

具體示範如下:

```python=
num = 10 + float("18.5") # 28.5
```
從上面得結果我們可以得到結果為浮點數型態。

在上述的例子中，我們將integer和<font color="red">經過轉型的</font>string做加法，而運算的過程如下:

```python=
# original 
num = 10 + float("18.5") 

# explicit cast string to floating-point 
num = 10 + 18.5

# result
num = 28.5 # floating-point
```

我們可以知道<b>float()</b>可以將值轉換為浮點數。

:::info
這邊有一個重點是關於<font color="red">string</font>的轉換，一個字串是不能和數值做運算的，所以我們要先把它轉換成integer或是floating-point才能做運算。
:::

<hr>

### • bool() (布林值)

具體示範如下:

```python=
num1 = bool(10) # True
num2 = bool(0) # False
num3 = bool(0.0) # False
num4 = bool("A string") # True
num5 = bool("") # False
```
從上面各個結果我們可以得到以下結論:

:::info
<b>bool()</b>可以將任何值轉換成布林值的型態，只要其中的值不為<font color="red">0</font>或是<font color="red">空</font>，它就會轉換為**True**，反之為**False**。
:::

因此要特別注意的是空字串也會視為<font color="red">False</font>

<hr>

### • str() (字串)

具體示範如下:

```python=
str1 = str(10) # "10"
str2 = str(15.23) + " dollars" # 15.23 dollars
str3 = 10 + " days" # TypeError
```
從上面的結果我們可以得到以下結論:

:::info
<b>str()</b>可以將任何值轉換成字串的型態，而數值和字串本不能相加，如果要拿數值和字串做連接的話就必須把數值先轉換為字串型態再做連接。
:::

<hr>

## • 希望這些筆記可以幫到你 •
如果有興趣了解更多歡迎追蹤我的
<font size=3>[Intagram](https://www.instagram.com/matcha_code/)</font>
<font size=3>[Youtube](https://www.youtube.com/@matchacode)</font>
<font size=3>[Github](https://github.com/OG-Matcha/Python-Class)</font>



<div style="display: block; text-align: left">
<a href="https://hackmd.io/@MatchaCode/Primitive-types" role="button" style="display:block; text-align:left;"> 上一篇: L2 Primitive types (原始型態)</a>
</div>