# L6 Input() (輸入)
###### tags: `Python` `input`

這邊有共筆版本的[Hackmd](https://hackmd.io/@MatchaCode/Input)

## 目錄
<a href=#•-Definition-(定義)>• Definition (定義)</a><br>
<a href=#•-Prompt-(提示訊息)>• Prompt (提示訊息)</a><br>
<a href=#•-Return-Result-(回傳結果)>• Return Result (回傳結果)</a>

## • Definition (定義)

要如何將資料從鍵盤上輸入到Python程式中呢?

要讓我們從鍵盤輸入資料，我們可以使用Python的**build-in function (內建函式)**: <code><font color='red'>input()</font></code>。

而 <code>**input()**</code> 函式只有一個參數可以傳入: <code><font color='red'>**prompt**</font></code>，具體如下:
```python
input(prompt=None) -> str
```

<hr>

## • Prompt (提示訊息)

甚麼是提示信息呢? 我們可以把他想成一段訊息告訴使用者該輸入甚麼東西，不然只會有鼠標閃爍一般人也不知道這個程式要輸入甚麼東西吧。

具體示範如下:

```python=
score = input("Please enter a number: ")
print("Matcha's score is: " + score)
```

像上述的程式碼，他會先在終端上輸出 <b>Please enter a number: </b>並等待使用者使用鍵盤輸入資料，這邊要知道的是<code>**input()**</code>進來的資料就像我們在編寫程式<font color='red'>指派變數</font>時一樣，我們需要將輸入的資料儲存在某個變數中才能夠重復使用他。

除非你只需要使用一次，那你當然可以在接收到資料後直接使用而不儲存他。

具體示範如下:

```python=
print("Matcha's score is: " + input("Please enter a number: "))
```

上述程式碼和一開始可以達到一樣的效果，但差別在於第二種版本在<code>**print()**</code>之後並沒有辦法重複使用先前輸入的資料。

當然，<code><font color='red'>**prompt**</font></code>預設情況下是<code>**None**</code>，也就是說不傳入參數也是可以正常使用<code>**input()**</code>的。

具體示範如下:
```python=
name = input()
print("Hello " + name + " nice to meet you.")
```

上述的程式碼執行後使用者可以直接輸入資料而沒有提示訊息出現，最後還是可以將資料儲存並輸出結果。

<hr>

## • Return Result (回傳結果)

可能有人在看到下面的定義時，不太了解 <b>-> str</b> 的意思。
```python
input(prompt=None) -> str
```

其實這代表了這個函式<font color='red'>回傳資料</font>的型態，像上面的意思就是<code>**input()**</code>回傳的資料型態為 <font color='red'>**str**</font>，也就是字串型態。

所以在上面<a href=#•-Prompt-(提示訊息)>Prompt</a>要求輸入數字時，明明使用者輸入的是一串數字，但是卻可以直接和字串做連接，在<a href="https://hackmd.io/@MatchaCode/Type-casting#%E2%80%A2-str()-(%E5%AD%97%E4%B8%B2)">L3 Type casting</a>有提到如果將數字及字串做相加的動作會導致錯誤。

所以當我們希望輸入的資料可以呈現他原本型態的樣子時，就會需要用到<font color='red'>強制轉型</font>。

具體示範如下:
```python=
score = input("Please enter a number: ")
print("Score plus 10: " + str(int(score) + 10)
```

在上述的程式碼中，我們先將 **score** 轉型成整數並加 10，這時候得到的結果為整數型態，要和字串做連接輸出有兩種方法。

第一種就是<a href="https://hackmd.io/@MatchaCode/Print">L5 Print()</a>中使用<font color='red'>逗號</font>分離的方法。

第二種就是我們一開始就會的使用<font color='red'>+</font>連接字串，所以我們這邊最後將加 10 的結果再次轉型成字串型態再和前面的字串連接，最後輸出。

當然，假如你可以確定你之後使用這個變數時大多數時間是不需要他為字串型態，我們可以在**一開始接收輸入時就轉型**。

具體示範如下:
```python=
score = int(input("Please enter a number: "))
print("Score plus 10:", score + 10)
```

在上述的程式碼中，我們會先從<code>**input()**</code>得到一個 <font color='red'>**str**</font> 型態的資料，我們直接**將他轉型成整數**再儲存進 **score** 中，這個時候我們就可以直接拿 **score** 和其他數值做運算。

所以這邊的重點在此:
:::info
<code>**input()**</code>回傳的結果為 **string** 型態資料
:::

<hr>

## • 希望這些筆記可以幫到你 •
如果有興趣了解更多歡迎追蹤我的<br>
<font size=3>[Intagram](https://www.instagram.com/matcha_code/)</font><br>
<font size=3>[Youtube](https://www.youtube.com/@matchacode)</font><br>
<font size=3>[Github](https://github.com/OG-Matcha/Python-Class)</font>

也可以幫我按個**讚賞**喔

<div style="display: flex; justify-content: left">
<a href="https://hackmd.io/@MatchaCode/Print" role="button"> 上一篇: L5 Print() (輸出)</a>
</div>