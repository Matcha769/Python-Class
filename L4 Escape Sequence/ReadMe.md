# L4 Escape sequence (跳脫序列)
###### tags: `Python` `escape sequence`

這邊有共筆版本的[Hackmd](https://hackmd.io/@MatchaCode/Escape-sequence)

## 目錄
<a href=#•-Definition-(定義)>• Definition (定義)</a><br>
<a href=#•-List-of-Escape-Sequence-(常見的跳脫序列)>• List of Escape Sequence (常見的跳脫序列)</a><br>
<a href=#•-Escape-Quotes-(引號使用)>• Escape Quotes (引號使用)</a><br>
<a href=#•-Escape-Backslash-(反斜線使用)>• Escape Backslash (反斜線使用)</a><br>
<a href=#•-Escape-NewLine-(換行使用)>• Escape NewLine (換行使用)</a><br>
<a href=#•-Escape-Carriage-Return-(回車使用)>• Escape Carriage Return (回車使用)</a><br>
<a href=#•-Escape-Horizontal-Tab-(水平定位使用)>• Escape Horizontal Tab (水平定位使用)</a><br>
<a href=#•-Escape-Backspace-(退格使用)>• Escape Backspace (退格使用)</a><br>
<a href=#•-Escape-Unicode-(萬國碼使用)>• Escape Unicode (萬國碼使用)</a><br>
<a href=#•-Escape-Octal-(八進位字元使用)>• Escape Octal (八進位字元使用)</a><br>
<a href=#•-Escape-Hexadecimal-(十六進位字元使用)>• Escape Hexadecimal (十六進位字元使用)</a><br>
<a href=#•-Raw-String-(原始字串)>• Raw String (原始字串)</a><br>


## • Definition (定義)

什麼是跳脫序列呢?

在字串中，有些字元是無法直接輸入或顯示的，因此需要使用跳脫序列來表示這些特殊字元。
跳脫序列是由反斜線 (backslash) 加上一個字元所組成，例如 **\n** 表示換行，**\t** 表示水平定位，**\\\\** 表示反斜線本身。

所以我們可以認為<br>
><font color='blue'>跳脫序列可以幫助我們表達那些很難或無法直接表示的字元。</font>
<hr>

## • List of Escape Sequence (常見的跳脫序列)
<table>
    <thead>
        <tr>
            <th style="padding-left: 100px; padding-right: 100px">Escape Sequence</th>
            <th style="padding-left: 100px; padding-right: 100px">Meaning</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align: center">\"</td>
            <td style="text-align: center">雙引號</td>
        </tr>
        <tr>
            <td style="text-align: center">\'</td>
            <td style="text-align: center">單引號</td>
        </tr>
        <tr>
            <td style="text-align: center">\\</td>
            <td style="text-align: center">反斜線</td>
        </tr>
        <tr>
            <td style="text-align: center">\n</td>
            <td style="text-align: center">換行</td>
        </tr>
        <tr>
            <td style="text-align: center">\r</td>
            <td style="text-align: center">回車</td>
        </tr>
        <tr>
            <td style="text-align: center">\t</td>
            <td style="text-align: center">水平定位</td>
        </tr>
        <tr>
            <td style="text-align: center">\b</td>
            <td style="text-align: center">退格</td>
        </tr>
        <tr>
            <td style="text-align: center">\N{name}</td>
            <td style="text-align: center">查找Unicode資料庫中的名稱</td>
        </tr>
        <tr>
            <td style="text-align: center">\u0000</td>
            <td style="text-align: center">16位元的Unicode字元</td>
        </tr>
        <tr>
            <td style="text-align: center">\U00000000</td>
            <td style="text-align: center">32位元的Unicode字元</td>
        </tr>
        <tr>
            <td style="text-align: center">\ooo</td>
            <td style="text-align: center">8進位字元</td>
        </tr>
        <tr>
            <td style="text-align: center">\xhh</td>
            <td style="text-align: center">16進位字元</td>
        </tr>
    </tbody>
</table>
<hr>

## • Escape Quotes (引號使用)
在講<a href="https://hackmd.io/T6S3iWiiRv6FBYsmmpevWg?view#%E2%80%A2-String-%E5%AD%97%E4%B8%B2">L2 Primitive types</a>的時候我們有講到Python使用單雙引號來定義 <font color="red">str</font>，當字串內部需要使用引號時，除了避免內外使用相同引號之外，還有一個方法就是使用<font color="red">跳脫序列</font>。

以下為範例:
```python=
string = 'I'm good at Python.' # SyntaxError
```
上述的程式碼會產生語法錯誤導致程式終止。

而我們可以使用跳脫序列來避免錯誤:
```python=
string = 'I\'m good at Python' # I'm good at Python
```
雖然這邊使用的是單引號，但在雙引號上的用法是完全相同的，就不再贅述。
在引號前方加入 <font color="red">\\</font> 就可以讓引號跳脫出字串變成單純的字元，不再有當作字串辨識符號的意義。
<hr>

## • Escape Backslash (反斜線使用)
既然我們已經知道 <font color="red">\\</font> 在字串中代表著跳脫字元，那我們又該如何輸出他們本身呢?

以下為範例:
```python=
string = "C:\Python\test.py" # C:\python	est.py
```
上述的程式碼因為 <font color="red">\\</font> 被當作跳脫字元使用，因此會結合有特殊定義的字元形成<font color="red">跳脫序列</font>，也就沒辦法正常地輸出我們想要的檔案位址。

而我們同樣可以使用跳脫序列來正常輸出這些位址。
```python=
string = "C:\\Python\\test.py" # C:\Python\test.py
```
這邊的第一個 <font color="red">\\</font> 當作跳脫字元，讓第二個 <font color="red">\\</font> 可以做為單純的字元做輸出，不再有當作跳脫字元的意義。
<hr>

## • Escape NewLine (換行使用)
如果想要讓字串做出換行的動作的話，<font color="red">\n</font> 是個很常見的用法。

以下為範例:
```python=
string = "Hello\nWorld" # Hello
                        # World
```
上述的程式碼在 <font color="red">Hello</font> 及 <font color="red">World</font> 中間使用 <font color="red">\n</font> ，它可以讓游標跳到下一行行首在繼續輸出接下來的字串，因此這兩個單字就會被分成兩行。
<hr>

## • Escape Carriage Return (回車使用)
<font color="red">\r</font> 的功能比較特殊，他可以讓游標回到**行首**再繼續以接下來的字串覆蓋掉之前的字元。

以下為範例:
```python=
string = "Justin loves Python\rMatcha" # Matcha loves Python
```
再上述的程式碼中，因為 <font color='red'>\r</font> 後面的 **Matcha** 有6個字元，而 **Justin** 也剛好有6個字元，於是在使用回車會到行首後，**Matcha**剛好覆蓋掉**Justin**，所以結果為**Matcha loves Python**。
```python=
# Origin: Justin loves Python
# Change: Matcha
# Output: Matcha loves Python
```


我們再看下個例子:
```python=
string = "You love Python\rI" # Iou love Python
```
由於 **I** 只有一個字元，當游標回到行首時，他只會覆蓋掉 **Y** 而其他字元不受影響。
```python=
# Origin: You love Python
# Change: I
# Output: Iou love Python
```
如果想知道更多關於 \r 和 \n 的差異可以看我的IG貼文: 
:::success
<a href="https://www.instagram.com/p/CopQpsYvWwW/?utm_source=ig_web_copy_link" alt="換行符號的謎團：為什麼\r和\n在不同環境下有不同的表現？">換行符號的謎團：為什麼\r和\n在不同環境下有不同的表現？</a>
:::
<hr>

## • Escape Horizontal Tab (水平定位使用)
相信學習Python的各位應該都知道<font color="red">tab</font>是很常使用的縮排功能，通常為<font color="red">4</font>個或<font color="red">8</font>個空格。
而我們也可以在字串中使用 <font color="red">\t</font> 來代表 <font color='red'>tab</font>。

以下為範例:
```python=
string = "Hello\tWorld" # Hello	World
```

從上述的程式碼可以看出 <font color='red'>\t</font> 的功能就像按下 <font color='red'>tab</font> 一樣在字串中產生空格。

舉個常見的例子:
```python=
string_1 = "2\tx\t2\t=\t4"     # 2	x	2	=	4
string_2 = "7\tx7\t=\t49"      # 7	x	7	=	49
stirng_3 = "10\tx\t10\t=\t100" # 10	x	10	=	100
```
<font color='red'>\t</font> 可以很好的幫我們做出排版。
<hr>

## • Escape Backspace (退格使用)
其實 <font color='red'>\b</font> 的用法就和我們鍵盤上的 <font color='red'>Backspace</font> 一樣，可以刪除掉前一格字元。

以下為範例:
```python=
string = "Hello \bWorld" # HelloWorld
```
在上述的例子中，<font color='red'>\b</font> 的作用就是刪除掉他前面的空格，於是**Hello**和**World**就相連在一起了。

我們再看下個例子:
```python=
string = "Have a nice d\t\bay" # Have a nice day
```
<font color='red'>\b</font> 除了空格也能刪除其他字元甚至是其他<font color='red'>跳脫序列</font>。
<hr>

## • Escape Unicode (萬國碼使用)
<img src="https://imgur.com/ezhoQU5.jpg" alt="Rocket" width="80%">

上面的圖片是一個飛機的表情符號，通常我們要在程式中使用表情符號或其他特殊字元，我們會使用Unicode來表示，而首先要介紹的是使用 <font color='red'>emoji 的名稱</font>。

以下為範例:
```python=
string = "\N{Airplane}" # ✈
```

在上述的例子中，我們會使用 <font color='red'>\N</font> 這個跳脫序列，後面接上 **{}**，裡面放上表情符號的名稱，比較需要注意的是 **N** 要為大寫，否則會和小寫的<font color='red'>換行</font>混淆。
<hr>

而我們還有另一個方法同樣可以叫出這個表情符號，就是使用 <font color='red'>\u</font> 這個跳脫序列，可以看到在上面飛機的下方有一個**U+2708**的編碼，這就是他在Unicode中的編碼，而我們也需要使用到它。

以下為範例:
```python=
string = "\u2708" # ✈
```
省略掉 **U+** 的部分，剩餘的就是我們需要用到的，直接接在 <font color='red'>\u</font> 後面就可以同樣表示該Unicode字元。
但這邊有一件事需要特別注意，有些表情符號可能它的編碼會超過4個字元，像**U+1F680**，這個時候我們就不能使用 <font color='red'>\u</font> 來表示這個符號，因為 <font color='red'>\u</font> 後面最多只能接收**4**個字元，因此必須使用下面的方法來替代。
<hr>

當我們的Unicode Number超過4個字元時，除了使用 <font color='red'>\N</font> 及名稱以外，我們也可以使用 <font color='red'>\U</font> 這個跳脫序列。

以下為範例:
```python=
string = "\U00002708" # ✈
```

由於 <font color='red'>\U</font> 要接收**8**個字元，因此我們必須將剩餘的部分用**0**補齊，這樣才能正常地輸出我們想要的字元。

同樣地，像剛剛舉例的**U+1F680**就可以用這個方法呈現:
```python=
string = "\U0001F680" # 🚀
```
同樣使用**0**補齊直到總共為**8**個字元。

如果不知道甚麼是**Unicode**的可以看我的IG貼文:
:::success
<a href="https://www.instagram.com/p/ClTef_SvyDX/?utm_source=ig_web_copy_link" alt="認識Unicode：如何在電腦上表示文字？">認識Unicode：如何在電腦上表示文字？</a>
:::
<hr>

## • Escape Octal (八進位字元使用)
我們也可以使用 <font color='red'>\ooo</font> 來使用**ASCII Table**中的八進位編碼來表示字元，使用方法為在 <font color='red'>\\</font> 後方直接接上**3**個數字。

以下為範例:
```python=
string = "\110\105\114\114\117\040\127\117\122\114\104" # HELLO WORLD
```
<hr>

## • Escape Hexadecimal (十六進位字元使用)
和上面的八進位字元使用一樣，使用**ASCII Table**內的十六進位編碼來表示字元，使用方法為在 <font color='red'>\x</font> 後方接上**2**個數字。

以下為範例:
```python=
string = "\x48\x45\x4C\x4C\x4F\x20\x57\x4F\x52\x4C\x44" # HELLO WORLD
```

如果不知道甚麼是**ASCII**的可以看我的IG貼文:
:::success
<a href="https://www.instagram.com/p/CjvS0YmvVYj/?utm_source=ig_web_copy_link" alt="了解ASCII：電腦如何表示文本？">了解ASCII：電腦如何表示文本？</a>
<a href="https://www.sciencebuddies.org/science-fair-projects/references/ascii-table" alt="ASCII Table">ASCII Table</a>
:::
<hr>

## • Raw String (原始字串)
我們有一種方法可以忽略在字串中的特殊字元，就是在宣告字串時將他宣告為**raw string**，具體做法就是在字串的**引號**前方加上 <font color='red'>r</font> 或是 <font color='red'>R</font>。

以下為範例:
```python=
string = "Hello \bWorld" # HelloWorld
```
在正常宣告的字串中跳脫序列會發揮它的作用，而使用原始字串就可以讓它變成單純的字元。
```python=
string = r"Hello \bWorld" # Hello \bWorld
```

這也可以應用在之前說到取檔案位址的功能。
```python=
string = r"C:\Python\test.py" # C:\python\test.py
```
<br>

但是**raw string**有一點比較特別的是，如果將 <font color='red'>\\</font> 放在字串的最後，會導致當成判斷字串的引號被當成跳脫序列而產生錯誤。

具體如下:
```python=
string = r"\" # SyntaxError
```
上方用來判斷字串的引號被 <font color='red'>\\</font> 嘗試變成跳脫序列，導致字串無法定義。
```python=
string = r"a\\" # a\\
```
而在上述的程式碼中 <font color='red'>\\</font> 互相變成跳脫序列，所以不會影響到字串的判定，是可以正常運作的。
:::info
因此，**raw string** 的結尾不能有奇數個 <font color='red'>\\</font>，會導致最後一個 <font color='red'>\\</font> 嘗試去跳脫引號導致錯誤。
:::
<hr>

## • 希望這些筆記可以幫到你 •
如果有興趣了解更多歡迎追蹤我的<br>
<font size=3>[Intagram](https://www.instagram.com/matcha_code/)</font><br>
<font size=3>[Youtube](https://www.youtube.com/@matchacode)</font><br>
<font size=3>[Github](https://github.com/OG-Matcha/Python-Class)</font><br>



<div style="display: block; text-align: left">
<a href="https://hackmd.io/@MatchaCode/Type-casting" role="button" style="display:block; text-align:left;"> 上一篇: L3 Type casting (型態轉換)</a>
</div>