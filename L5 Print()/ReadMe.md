# L5 Print() (輸出)
###### tags: `Python` `print`

這邊有共筆版本的[Hackmd](https://hackmd.io/@MatchaCode/Print)

## 目錄
<a href=#•-Definition-(定義)>• Definition (定義)</a><br>
<a href=#•-*Objects-(物件)>• *Objects (物件)</a><br>
<a href=#•-Sep-(分隔符號)>• Sep (分隔符號)</a><br>
<a href=#•-End-(終止符號)>• End (終止符號)</a><br>
<a href=#•-File-(檔案)>• File (檔案)</a><br>
<a href=#•-Flush-(清緩衝區)>• Flush (清緩衝區)</a><br>


## • Definition (定義)

要如何在Python中輸出資料呢?

要讓我們的資料印出在屏幕上，我們可以使用Python的**build-in function (內建函式)**: <code><font color='red'>print()</font></code>。

而 <code>**print()**</code> 函式可以使用的關鍵字如下:
```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

<hr>

## • *Objects (物件)

我們這邊就先不解釋物件是甚麼意思，因為這牽扯到物件導向的概念，也不是這篇的重點。這邊先來講一下 <font color='red'><b>\*</b></font> 代表甚麼意思好了，如果看到關鍵字的前方有 <font color='red'><b>\*</b></font>，代表這個位置可以接收多個值。

具體來講就像下面範例:
```python=
print("This is first object", "Second object") # This is first object Second object
print(1, 2, 3, "Start!") # 1 2 3 Start!
```

從上述的例子來看，我們可以將想要 <font color='red'>print</font> 出來的值一起放到 <code>**print()**</code> 當中，使用 **, (逗號)** 分隔，而 <code>**print()**</code> 就會將結果如註解輸出呈現。

這邊或許你會想，這邊的**值**是指甚麼東西，在之後講到物件以前，我希望大家可以這麼想，包括之前講過的 <font color='red'>Primitive Type</font>，到之後我們會教到的其他資料結構都是 <font color='red'>object</font>，因此像第二行我們可以放入多個**整數**、**字串**讓他做輸出。

當然，這邊也可以放入變數而非直接放入值。

具體示範如下:
```python=
name = "Matcha"
print("Hello, I'm", name) # Hello, I'm Matcha
```

這邊我們將字串 <font color='red'>Matcha</font> 存放到 **name** 這個變數再放到 <code>**print()**</code> 來做輸出。

<hr>

## • Sep (分隔符號)

這邊的<code><font color='red'>sep</font></code>是 **separator** 的簡寫，他代表我們傳入的 <font color='red'>objects</font> 之間要用甚麼做分隔，也可以想成用甚麼來連接他們，像我們在<code>**\*objects**</code>的範例中並沒有使用到<code><font color='red'>sep</font></code>關鍵字，那麼他預設的分隔符號就會是<code><font color='red'>" "</font></code>，也就是一個空格字串。

具體使用方法如下:
```python=
# Without specifying sep keyword
print(1, 2, 3, "Start!") # 1 2 3 Start!
# Specified sep keyword
print(1, 2, 3, "Start", sep="~") # 1~2~3~Start
```

在上述的程式碼中，可以看到假如我們沒有特別將<code><font color='red'>sep</font></code>指定的話他就會以空格來分隔前面的 <font color='red'>objects</font> ，但是像第四行我們特別指定<code><font color='red'>sep</font></code>為 "**<font color='red'>~</font>**"，那麼他就會以 **~** 來分隔(連接)傳入的 <font color='red'>objects</font>。

<hr>

## • End (終止符號)

在<code>**print()**</code>中還有一個常用的關鍵字<code><font color='red'>end</font></code>，它表示在輸出結束時應該使用的終止字符。預設情況下，<code><font color='red'>end</font></code>的值為 **"\n"**，表示輸出結束時會換行。但是我們透過更改<code><font color='red'>end</font></code>的值來改變這個動作。

具體使用方法如下:
```python=
# Without specifying end keyword
print("Hello") # Hello
print("World") # World

# Specified end keyword with " "
print("Hello", end=" ")
print("World")          # Hello World

# Specified end keyword with ""
print("Hello", end="")
print("World")          # HelloWorld
```

在上述的程式碼中，可以看到假如我們沒有特別將<code><font color='red'>end</font></code>指定的話他就會將兩次<code>**print()**</code>分別使用兩行輸出，因為這時<code><font color='red'>end</font></code>的值預設為 **"\n"**。

但是像第六行我們特別指定<code><font color='red'>end</font></code>為空格 **" "**，那麼他就會在輸出結束時不換行，而是插入一個空格字串並直接接續後面的輸出。

而在第十行，我們特別指定<code><font color='red'>end</font></code>為空字串 **""**，這意味著在輸出結束時不插入任何字元，直接接續下一次<code>**print()**</code>輸出的內容。

<hr>

## • File (檔案)

這邊<code><font color='red'>file</font></code>預設是使用<code>**sys.stdout**</code>，也就是 **standard output**，基本上就是將結果輸出到終端，平常使用也都會省略掉這個關鍵字，如果要使用的話是可以有將內容輸入到其他檔案的用途，具體方法等到後面教到檔案寫入及寫出時會再談到。

<hr>

## • Flush (清緩衝區)

<code><font color='red'>flush</font></code>這個關鍵字後面接受的是**布林值**，也就是**True**和**False**。清緩衝區是甚麼意思呢?

一般來說，<code>**print()**</code>會將資料儲存到緩衝區中，以提高程式的效能。因此，為了降低系統呼叫的次數，先將資料儲存在緩衝區中，然後再顯示到螢幕上，而不是一個字元一個字元地寫到螢幕或檔案上。

預設情況下<code><font color='red'>flush</font></code>的值是**False**，代表說<code>**print()**</code>並不會一直更新輸出的資料，而是等到程式執行完時才將結果丟到終端輸出。

具體示範如下:
```python=
import time

for i in range(10, 0, -1):
    # Without specifying flush keyword
    print(i, end=" ")
    time.sleep(1)

print("Done")
```

各位如果看不懂上述的程式碼沒有關係，簡單的說，它的功能就是會輸出**10~1**，每輸出一個數字就暫停**1**秒，最後輸出 **"Done"**，就是一個倒數計時器的功能。

假如像上面並沒有特別指定<code><font color='red'>flush</font></code>，那麼預設就會是**False**，代表說他只會等到程式結束才回輸出結果讓我們看到，執行程式就會發現，**終端機一開始並沒有數字輸出，等到10秒鐘過後，數字和Done才一起同時出現**，這並不符合我們的預想。

要解決這個問題就可以使用<code><font color='red'>flush</font></code>，我們將它設為**True**。

具體示範如下:

```python=
import time

for i in range(10, 0, -1):
    # Specified flush keyword
    print(i, end=" ", flush=True)
    time.sleep(1)

print("Done")
```

執行程式後就會發現如預期的在每一秒出現一個數字，最後輸出Done，這是因為我們強制讓<code>**print()**</code>去清緩存區，那他就勢必要先把裡面的內容作輸出再執行下一次<code>**print()**</code>，就可以達到每一秒出現一個數字的結果。

<hr>

## • 希望這些筆記可以幫到你 •
如果有興趣了解更多歡迎追蹤我的<br>
<font size=3>[Intagram](https://www.instagram.com/matcha_code/)</font><br>
<font size=3>[Youtube](https://www.youtube.com/@matchacode)</font><br>
<font size=3>[Github](https://github.com/OG-Matcha/Python-Class)</font><br>

也可以幫我按個**讚賞**喔

<div style="display: block; text-align: left">
<a href="https://hackmd.io/@MatchaCode/Escape-sequence" role="button" style="display:block; text-align:left;"> 上一篇: 
L4 Escape sequence (跳脫序列)</a>
</div>