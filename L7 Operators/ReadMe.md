# L7 Operator (運算子)
###### tags: `Python` `operator`

## 目錄
<a href=#•-Definition-(定義)>• Definition (定義)</a><br>
<a href=#•-Unary-Operator-(一元運算子)>• Unary Operator (一元運算子)</a><br>
<a href=#•-Binary-Operator-(二元運算子)>• Binary Operator (二元運算子)</a><br>
<a href=#•-Assignment-Operator-(指派運算子)>• Assignment Operator (指派運算子)</a><br>
<a href=#•-Arithmetic-Operator-(算術運算子)>• Arithmetic Operator (算術運算子)</a><br>
&emsp;<a href=#•-+-(加法)>• + (加法)</a><br>
&emsp;<a href=#•---(減法)>• - (減法)</a><br>
&emsp;<a href=#•-*-(乘法)>• * (乘法)</a><br>
&emsp;<a href=#•-/-(浮點數除法)>• / (浮點數除法)</a><br>
&emsp;<a href=#•-//-(整數除法)>• // (整數除法)</a><br>
&emsp;<a href=#•--(模數)(取餘數)>• % (模數)(取餘數)</a><br>
&emsp;<a href=#•-**-(指數)>• ** (指數)</a><br>
<a href=#•-Compound-Assignment-Operator-(複合指定運算子)>• Compound Assignment Operator (複合指定運算子)</a><br>
<a href=#•-Relational-Operator-(關係運算子)>• Relational Operator (關係運算子)</a><br>
<a href=#•-Logical-Operator-(邏輯運算子)>• Logical Operator (邏輯運算子)</a><br>
&emsp;<a href=#•-not-(非)>• not (非)</a><br>
&emsp;<a href=#•-and-(且)>• and (且)</a><br>
&emsp;<a href=#•-or-(或)>• or (或)</a><br>
&emsp;<a href=#•-combination-(結合使用)>• combination (結合使用)</a><br>
<a href=#•-Bitwise-Operator-(位元運算子)>• Bitwise Operator (位元運算子)</a><br>
&emsp;<a href=#•-amp-(且)>• & (且)</a><br>
&emsp;<a href=#•-|-(或)>• | (或)</a><br>
&emsp;<a href=#•-^-(異或)>• ^ (異或)</a><br>
&emsp;<a href=#•-~-(非)>• ~ (非)</a><br>
<a href=#•-Shift-Operator-(位移運算子)>• Shift Operator (位移運算子)</a><br>
<a href=#•-Membership-Operator-(成員運算子)>• Membership Operator (成員運算子)</a><br>
<a href=#•-Identity-Operator-(身分運算子)>• Identity Operator (身分運算子)</a><br>
<a href=#•-Operator-Precedence-(運算子優先序位)>• Operator Precedence (運算子優先序位)</a>

## • Definition (定義)

在寫程式的時候難免會需要做**運算**，這個時候基本的算術運算子就派上用場，當然還有其他用來做**邏輯、關係**判斷等等的運算子，讓我們先來看看下面的一個式子:
```python
2 + 2
```
這是一個很基本的運算，其中的<font color='red'><code>+</code></font>就是一個**運算子**，而<font color='darkblue'><code>2</code></font>就是**運算元**，這也是我們等等要講到一元和二元的關係。

<hr>

## • Unary Operator (一元運算子)

什麼是一元運算子呢? 它代表的就是只需要一個**運算元**就可以表示意義的運算子，舉例來說:
```python=
print(+6) # 6
print(-2) # -2
```
像我們用來判斷正負號的<font color='red'><code>+</code></font>、<font color='red'><code>-</code></font>就是一元運算子。

在第一行的<font color='red'><code>+</code></font>代表數值為正數，但通常都會被省略掉，而第二行的<font color='red'><code>-</code></font>就賦予了數值負數的意義，而他們都只需要**一個運算元**就能有意義。

<hr>

## • Binary Operator (二元運算子)

像定義裡面的算式就是一個基本的二元運算子的運用，大部分的運算子也屬於這個範疇。
```python=
print(2 - 2) # 0
```
就是**一個運算子**要和**兩個運算元**配合才有意義

<hr>

## • Assignment Operator (指派運算子)

相信這個運算子大家應該都很熟悉了，就是我們在指派**值**給**變數**時所使用的<font color='red'><code>=</code></font>。
```python=
int_num = 10
string = "Hello World"
float_num = 12.5
boolean = False
```
像上面基本的指派變數大家應該已經得心應手了，這邊另外補充一個**build-in function**: <font color='red'><code>id()</code></font>，他可以用來查看**物件**在記憶體中的位址，這邊的物件和我們在<a href="https://hackmd.io/@MatchaCode/Print#%E2%80%A2-*Objects-(%E7%89%A9%E4%BB%B6)">L5 Print()</a>講到的是一樣的。
```python
id(object) -> int
```
舉例來說:
```python=
a = 1.0
b = 2
print(id(1.0), id(2)) # 1590326436144 1590325412112
print(id(a), id(b)) # 1590326436144 1590325412112
```
這邊的位址每個人的環境系統不同結果也會不同，是正常的，像上面的結果你可以看到，直接輸入**值**或者**變數名稱**都會得到同樣的位址，所以這個時候我希望你們有個觀念，在指派變數的時候，我們的變數會去<font color='red'>指向那個值在記憶體中的位址</font>。

再看一個範例:
```python=
a = "Hello"
b = a
print(id(a), id(b)) # 3095031449584 3095031449584
```
在上面我將<font color='red'>Hello</font>指派給**a**，再將**a**指派給**b**，因此這個時候**b**和**a**都會指向<font color='red'>Hello</font>在記憶體中的位址。

以上是關於<font color='red'><code>id()</code></font>的簡介，接下來我們這邊的重點是**值的交換**。
```python=
a = 10
b = 20
print("Before Swap:", a, b) # Before Swap: 10, 20
print(id(a), id(b)) # 2328313987600 2328313987920
a, b = b, a # Swap
print("After Swap:", a, b) # After Swap: 20, 10
print(id(a), id(b)) # 2328313987920 2328313987600
```
可以看到Python交換變數的值只需要一行就能完成，第五行的意思是同時將**b**的**值**指派給**a**，又將**a**的**值**指派給**b**，<font color='red'><code>=</code></font> 兩邊是對等的，所以這時候你可以發現**a**和**b**他們指向的位址做了交換。

這也是Python和其他程式語言不同的地方，舉C++為範例:
```cpp=
int a = 10;
int b = 20;
int temp; // hold temporary value

temp = b; // assign 20 to temp
b = a; // assign 10 to b, if we didn't use temp to store 20, we will lose it
a = temp; // assign 20 we have stored before swap to a
```
上面的程式碼各位可以不用太了解和Python不一樣的部分，但邏輯應該可以看懂，可以注意到它如果想要交換變數的**值**的話是需要先用一個**暫時的變數**來去儲存其中一個值，因為在另一個**值**被指派到先前儲存起來的變數的**值**時，會**覆蓋掉原本的值**，假如我們沒有先將其儲存保留起來，我們就會失去那個**值**。

所以像Python這樣的功能是很方便的，其中的原理在之後講到Tuple (元組)的時候會提到。

<hr>

## • Arithmetic Operator (算術運算子)
**算術運算子**，顧名思義就是讓我們在做計算時可以使用的運算子，像我們平常會使用的 <font color='red'><b><code>+</code> <code>-</code> <code>*</code> <code>/</code></b></font> 就是很常見的算術運算子。

<hr>

### • + (加法)
加法可以用在數值或字串型態，在數值上使用它就會表示<font color='red'>數學上的相加</font>，用在字串上他就會表示<font color='red'>文字的串接</font>。

```python=
num1 = 10
num2 = 20

addition = num1 + num2
print(addition) # 30

str1 = "Hello "
str2 = "World!"

concatenation = str1 + str2 
print(concatenation) # Hello World!
```

<hr>

### • - (減法)
減法就目前講到的就是用在數值上表示<font color='red'>數學上的相減</font>。
```python=
int_num1 = 10
int_num2 = 20

substraction = int_num1 - int_num2
print(substraction) # -10

float_num1 = 10.5
float_num2 = 5.3

substraction = float_num1 - float_num2
print(substraction) # 5.2
```

<hr>

### • / (浮點數除法)
在Python中比較特別的是它有兩種除法運算子，這邊講的是浮點數除法，顧名思義，他回傳值的型態為浮點數。
```python=
int_num1 = 20
int_num2 = 10

float_division = int_num1 / int_num2
print(float_division) # 2.0

int_num1 = 25
float_num2 = 0.6

float_division = int_num1 / float_num2
print(float_division) # 41.66666666666667
```
在上述的程式碼中可以看到不論你是用**純整數**還是**整數及浮點數**做運算，回傳的結果都會是**浮點數**，這就是浮點數除法的關鍵。

<hr>

### • // (整數除法)
剛剛講了浮點數除法，現在有一個新的運算子由兩個<font color='red'><code>\\</code></font>組成，他代表的是**整數除法**，意思就是計算的結果會是**捨去小數部分並向下取整的數值**，但是這邊要注意的是和浮點數除法不同，假如其中一個**運算元**為浮點數型態，回傳的結果就會是浮點數，而非整數，但重點來了，假如兩個**運算元**皆為整數型態，就算除法不能整除，結果也會捨去小數點部分。

舉例來說:
```python=
int_num1 = 24
int_num2 = 7

floor_division = int_num1 // int_num2
print(floor_division) # 3

int_num1 = 24
float_num2 = 7.0

floor_division = int_num1 // float_num2
print(floor_division) # 3.0
```
在上述的程式碼中可以看到如果**兩個**運算元皆為**整數型態**，那麼結果就會是做完除法後<font color='red'>商</font>的部分，而型態也為整數，但是只要**其中一個或兩個**運算元為浮點數型態，那麼結果雖然也會是<font color='red'>商</font>的部分，**並不會包含小數部分**，但會是**浮點數型態**。

<hr>

### • % (模數)(取餘數)
這邊這個也是一個新的運算子，它代表著取餘數，這樣講起來比較抽象，我們可以直接來看範例:

```python=
int_num1 = 14
int_num2 = 5

modulus = int_num1 % int_num2
print(modulus) # 4

float_num1 = 16.4
int_num2 = 6

modulus = float_num1 % int_num2
print(modulus) # 4.399999999999999
```
在上述的程式碼中可以看到當**兩個**運算元為整數型態時，做餘數運算的時候，就會在做完除法後，將**餘數的部分**做為回傳的結果，所以在第一部分的運算時
```
14 / 5 = 2 ... 4
```
得到的結果就是**餘數**，也就是 <font color='red'>4</font>。

而第二部分的運算使用到**浮點數**
```
16.4 / 6 = 2 ... 4.4
```
至於結果顯示為**4.399999999999999**是因為當進行浮點數運算時，浮點數會有精度的問題，由於不能精確顯示**4.4**，所以就使用有限的位數來表示該浮點數，有誤差是正常的。

:::info
這邊的 <font color='red'><code>/</code></font> <font color='red'><code>//</code></font> <font color='red'><code>%</code></font> 都有一個特性，就是第二個**運算元**不可為<font color='red'>**0**</font>，用數學的觀點來看就是**分母不可為0**，否則就會產生<font color='red'><code>ZeroDivisionError</code></font>
:::

<hr>

### • ** (指數)
在Python中我們可以直接使用<font color='red'><code>\**</code></font>來表示**次方**，舉例來說:

```python=
print(2 ** 3) # 8
print(3 ** 4) # 81
print(2.5 ** 3.5) # 24.705294220065465
```
在上述的程式碼中，在<font color='red'><code>\**</code></font>左邊的為**底數**，右邊的為**次方**，結果就如普通數學運算一樣，比較特別的是這邊可以接受**底數或次方**為浮點數。

這邊需要注意的是<font color='red'><code>\*\*</code></font>和其他大部分運算子不同，他是**right-left associativity**，也就是從右看到左，怎麼說呢，像其他運算子我們就是從左開始往右做運算，但<font color='red'><code>\*\*</code></font>就必須反過來，舉例來說:

```python=
print(2 ** 3 ** 2) # 512
print(2 ** (3 ** 2))
```
在上述的程式碼中如果我們從左到右來做運算的話
```
2 ** 3 ** 2 --> 8 ** 2 --> 64 
```
就會是錯誤的結果，因此正確的順序應該是像第二行那樣，**先算右邊的部分再算左邊的部分**。

:::info
從數學的觀點來看就是要讀成: <b>x<sup>(y<sup>z</sup>)</sup></b> 而非 <b>(x<sup>y</sup>)<sup>z</sup></b>
:::

<hr>

## • Compound Assignment Operator (複合指定運算子)
甚麼是複合指定運算子呢，他是一種結合了**指定運算子和其他運算子**的新用法。舉例來說:
```python=
num = 10
num = num + 1
print(num) # 11
```
在上述的程式碼中，我先指派**10**給**num**，然後我希望他可以<font color='red'>+1</font>後重新指派回原本的變數，所以第二行的意思是先將**num**的值<b>+1</b>，再將新的值重新指派回**num**，所以這時候**num**的值就會是<font color='red'>11</font>。

但是這種寫法我們會重複寫變數的名稱，當數量多起來的時候就會相當繁瑣，因此我們就會使用**複合指定運算子**
```python=
num = 10
num += 1
print(num) # 11
```
上面的<font color='red'><code>num += 1</code></font> 和 <font color='red'><code>num = num + 1</code></font>是相同的意思，但前者寫起來就比較簡潔。

當然他也不只能用在加法中，也能活用在其他運算子中。
```python=
num = 5

num -= 2
print(num) # 3

num *= 10
print(num) # 30

num /= 2
print(num) # 15.0

num //= 2
print(num) # 7.0

num %= 4
print(num) # 3.0

num **= 3
print(num) # 27.0
```

<hr>

## • Relational Operator (關係運算子)
關係運算子是Python中用來比較兩個**值**之間關係的運算子，包括<font color='red'><code>==</code></font> <font color='red'><code>!=</code></font> <font color='red'><code>&gt;</code></font> <font color='red'><code>&lt;</code></font> <font color='red'><code>&gt;\=</code></font> <font color='red'><code>&lt;=</code></font>這六種運算子。

由於他們的做比較產生的結果只會有**成立**或者**不成立**，因此輸出的結果只會是<font color='red'><code>True</code></font>及<font color='red'><code>False</code></font>。

以下是範例：
```python=
a = 5
b = 7

# 等於運算子（==）
print(a == b)  # False

# 不等於運算子（!=）
print(a != b)  # True

# 大於運算子（>）
print(a > b)   # False

# 小於運算子（<）
print(a < b)   # True

# 大於等於運算子（>=）
print(a >= b)  # False

# 小於等於運算子（<=）
print(a <= b)  # True
```
    
上述範例中，我們先使用變數指派的方式分別將**a**設為**5**，**b**設為**7**。接著，我們使用各種不同的關係運算子來比較a和b之間的大小關係，並將結果輸出。

例如，<font color='red'><code>!=</code></font>用來比較a和b是否不相等，因為a不等於b，所以結果為**True**。另一方面，<font color='red'><code>&lt;</code></font>用來比較a是否小於b，因為a比b小，所以結果為**True**。

<hr>

## • Logical Operator (邏輯運算子)
邏輯運算子就可以將前面的運算子結合在一起變成運算式做判斷，其中分別有<font color='red'><code>not</code></font> <font color='red'><code>and</code></font> <font color='red'><code>or</code></font>。

<hr>

### • not (非)
<font color='red'><code>not</code></font>就是會回傳當前結果的相反布林值，舉例來說:
```python=
a = 5
b = 10
c = 0

print(not a < b) # False
print(not c) # True
```
在上述的程式碼中，因為<font color='red'><code>not</code></font>的序位較低，因此會先做運算式在做邏輯判斷，像是第1行就會是
```python=
print(not True) # False
```
第2行比較特別，還記得<a href="https://hackmd.io/@MatchaCode/Type-casting#%E2%80%A2-bool()-(%E5%B8%83%E6%9E%97%E5%80%BC)">L3 Type casting</a>中講到，只要不為<font color='red'>0或空</font>，轉換成布林值的結果就會是**True**，反之為**False**，所以<font color='red'><code>not c</code></font>的結果就會是<font color='red'><code>not False</code></font>，所以得到的結果就會是**True**。

<hr>

### • and (且)
<font color='red'><code>and</code></font>就是在所有運算的結果**皆成立**的情況下，就會回傳**True**，否則回傳**False**。

舉例來說:
```python=
a = 5
b = 10
print(a >= 5 and b * 2 < 30) # True
print(a < b and a ** 2 == 25 and a < 1) # False
```

在上述的程式碼中，由於<font color='red'><code>and</code></font>的判斷序位較其他運算子低，所以電腦會先做其他運算在做出邏輯判斷，就第3行而言
```
a >= 5 --> True
b * 2 < 30 --> True
```
他會先判斷好**運算條件**在判斷在**邏輯運算子**中應該產生甚麼結果，因此會變成
```python=
print(True and True) # True
```

而在第4行中
```
a < b --> True
a ** 2 == 25 --> True
a < 1 # False
```
結果就會變成
```python=
print(True and True and False) # False
```

這邊要另外補充運算元皆為**數值**型態時的情況
```python=
print(1 and 5 and 7) # 7
print(1 and 0 and 2) # 0
```
在第1行中，**假如沒有任何運算式的結果為False**，那麼<font color='red'><code>and</code></font>得到的結果就會回傳最後一個運算元。

這個原理是因為<font color='red'><code>and</code></font>需要做到最後一個運算式的判斷才能確認結果，除非先碰到**0**，就會停止繼續判斷並回傳**0**，就像第2行一樣。

:::info
只要碰到一個運算式的結果為**False**，則停止繼續判斷接下來的運算式並回傳**False**。
:::

<hr>

### • or (或)
<font color='red'><code>or</code></font>就是只要其中一個運算的結果**成立**的情況下，就會回傳**True**，如果所有運算的結果皆**不成立**則回傳**False**。

舉例來說:
```python=
a = 5
b = 10
print(a >= 5 or b * 2 == 30) # True
print(a >= b or a ** 2 != 25 or a < 1) # False
```
在上述的程式碼中，由於<font color='red'><code>or</code></font>的判斷序位較其他運算子低，所以電腦會先做其他運算在做出邏輯判斷，就第3行而言
```python=
print(True or False) # True
```

而在第4行中
```python=
print(False or False or False) # False
```

這邊也另外補充運算元皆為**數值**型態時的情況
```python=
print(0 or 0 or 0) # 0
print(0 or 3 or 2) # 3
```
在第1行中，**假如所有運算式的結果皆為False**，那麼<font color='red'><code>or</code></font>得到的結果就會回傳**0**。

其中原理是因為<font color='red'><code>or</code></font>要碰到**非0**的值才能確認結果，假如先碰到第一個**非0**的值，就會停止繼續判斷並回傳**那個值**，就像第2行一樣。

:::info
只要碰到一個運算式的結果為**True**，則停止繼續判斷接下來的運算式並回傳**True**。
:::

<hr>

### • combination (結合使用)
現在我們要知道當不同邏輯運算子在同一個運算式時該如何判斷以及他們的順序: <font color='red'><code>not</code></font> > <font color='red'><code>and</code></font> > <font color='red'><code>or</code></font>，當我們做判斷時會以這個順序去判斷。

舉例來說:
```python=
x = 4
y = 3
print(x >= y or x != y and not x ** 2 > y) # True
```

我們可以這樣分解
```python=
print(x >= y or x != y and not True)
print(x >= y or x != y and False)
print(x >= y or True and False)
print(x >= y or False)
print(True or False)
print(True)
```
一步步按照順序去判斷每一個運算式的結果。

<hr>

## • Bitwise Operator (位元運算子)
我們的資料儲存在電腦中就是以位元的形式存在，而我們也可以透過位元運算子針對數值的位元去做運算，而操作的部分是用**二進位**來表示，如果不會進位法的一樣可以去看我之前IG的文章:
:::success
<a href="https://www.instagram.com/p/Cjkbgvxv68j/?utm_source=ig_web_copy_link" alt="掌握進位法！簡單易懂的轉換方法分享">掌握進位法！簡單易懂的轉換方法分享</a>
:::
<hr>

### • & (且)
這邊的<font color='red'><code><b>&</b></code></font>雖然也是**and**的意思，但並不是針對邏輯而是針對位元作運算，舉例來說:
```python=
print(5 & 3) # 1
```
這邊讓我們換成二進位來看:
```
   0101 --> 5
&  0011 --> 3
--------------
   0001 --> 1
```
<font color='red'><code><b>&</b></code></font>會去看數值二進位中每一位數，只有兩者皆為**1**，傳出的位元才會是**1**，於是就產生了上面的結果。

<hr>

### • | (或)
這邊的<font color='red'><code><b>|</b></code></font>雖然也是**or**的意思，但並不是針對邏輯而是針對位元作運算，舉例來說:
```python=
print(5 | 3) # 7
```
這邊讓我們換成二進位來看:
```
   0101 --> 5
|  0011 --> 3
--------------
   0111 --> 7
```
<font color='red'><code><b>|</b></code></font>會去看數值二進位中每一位數，只要其中一個為**1**，傳出的位元就會是**1**，於是就產生了上面的結果。

<hr>

### • ^ (異或)
這邊的<font color='red'><code><b>^</b></code></font>是比較特別的新運算子，舉例來說:
```python=
print(5 ^ 3) # 6
```
這邊讓我們換成二進位來看:
```
   0101 --> 5
^  0011 --> 3
--------------
   0110 --> 6
```
<font color='red'><code><b>^</b></code></font>會去看數值二進位中每一位數，只要其中兩邊的位元不同，就會回傳**1**，反之兩邊相同傳出的位元就會是**0**，於是就產生了上面的結果。

<hr>

### • ~ (非)
這邊這個<font color='red'><code><b>~</b></code></font>比較特別，他會去取數值的**1補數**，如果不知道**補數**是甚麼的話可以試著上網查詢相關資料。
```python=
print(~5) # -6
```
這邊讓我們換成二進位來看:
```
   0101 --> 5
~  1010 --> -6
```
換成1補數的方法就是將其位元翻轉，如果實在不知道該怎麼算的話可以這樣記<code><b>-(x + 1)</b></code>。因為這運算子我自己在寫的時候幾乎也不會用到，所以影響不大。

<hr>

## • Shift Operator (位移運算子)
這邊和位元運算子有點相似，但是本身是運用在位元向右或向左**推移**的情況，舉例來說:

```python=
print(6 >> 1) # 3
```
這邊讓我們換成二進位來看:
```
      0110 --> 6
>> 1  0011 --> 3
```
上述的程式碼就是將**6**換成二進位後將每個位元往右推移一單元，而多出來的部分則捨去，於是就得到了**3**。

左移也是同理
```python=
print(6 << 2) # 24
```
這邊同樣讓我們換成二進位來看:
```
      0000 0110 --> 6
<< 2  0001 1000 --> 24
```
這邊就是將其位元向左推移兩單元，於是得到**24**。

但是很顯然的，當數字越來越大的時後，我們總不能每次都把它換成位元來計算，所以大家可以想想二進位的通性，就會知道當我們在左移和右移的時候到底做了怎樣的運算
```
6 >> 4 --> 6 // 2 ** 4
5 << 2 --> 5 * 2 ** 2
```
從上面兩個範例可以知道，**右移**就是<code>base // 2 ** n</code>，而**左移**就是<code>base * 2 ** n</code>，掌握這個算法當數字很大的時候也可以直接計算了。

:::info
關於位元的運算幾乎都是對**整數**做操作，而非**浮點數**。
:::

<hr>

## • Membership Operator (成員運算子)
成員運算子顧名思義就是用來判斷某個元素是否在另一個元素中，主要使用的為<font color='red'><code>in</code></font>，在邏輯上看起來也符合平常使用的語法，較淺顯易懂，舉例來說
```python=
print("M" in "Matcha") # True
print("m" in "Matcha") # False
print("m" not in "Matcha") # True
```
上述的程式碼中第1行會判斷字串<font color='red'><code>M</code></font>是否在字串<font color='red'><code>Matcha</code></font>中，因條件成立，所以結果為**True**。

相對的第2行<font color='red'><code>m</code></font>並不在字串<font color='red'><code>Matcha</code></font>中，所以結果為**False**。

而第3行我們將其與<font color='red'><code>not</code></font>結合使用，判斷<font color='red'><code>m</code></font>是否不在字串<font color='red'><code>Matcha</code></font>中，所以結果為**True**。

<hr>

## • Identity Operator (身分運算子)
這邊的身分運算子<font color='red'><code>is</code></font>就要和關係運算子中的<font color='red'><code>==</code></font>做比較了，我們這邊的重點會放在他們兩個的差別，

首先，<font color='red'><code>is</code></font>比較的是兩個物件的記憶體位址，這時候請想起<font color='red'><code>id()</code></font>這個內建函式
```python=
num1 = 1.0
num2 = 2.0

print(id(num1), id(num2)) # 1948752781616 1948751772944

print(num1 is num2) # False
print(num1 == num2) # False
```
在上述的程式碼中，<code>num1</code>及<code>num2</code>無論是值還是記憶體位址皆不同，所以用<font color='red'><code>is</code></font>或是<font color='red'><code>==</code></font>的結果皆為**False。

但如果我們換一個情況
```python=
num1 = 3.0
num2 = 3

print(id(num1), id(num2)) # 1913265234224 1913264210224
print(num1 is num2) # False
print(num1 == num2) # True
```
在上述的程式碼中，<code>num1</code>及<code>num2</code>雖然一個是**整數**，一個是**浮點數**，但是在做值的判斷時會是相同的，然而**整數和浮點數的記憶體位址是不同的**，所以這時候<font color='red'><code>is</code></font>就可以判定出來<code>num1</code>及<code>num2</code>並不相同，他們並非同一個**物件**。

反之，如果我們使用完全相同的值
```python=
num1 = 3
num2 = 3

print(id(num1), id(num2)) # 2893016924464 2893016924464
print(num1 is num2) # True
print(num1 == num2) # True
```
兩個變數指向的**記憶體位址相同**且**值也相同**，所以在<font color='red'><code>is</code></font>及<font color='red'><code>==</code></font>的結果皆為**True**。

:::info
如果需要嚴格的判定時可以考慮使用<font color='red'><code>is</code></font>而非<font color='red'><code>==</code></font>。
:::

<hr>

## • Operator Precedence (運算子優先序位)
這邊提供運算子優先序位的表格


| Precedence | Operator |
| ---------- | -------- |
| 1          | <font color='red'><code>()</code></font>       |
| 2          | <font color='red'><code>**</code></font>       |
| 3          | <font color='red'><code>+x</code></font>, <font color='red'><code>-x</code></font>, <font color='red'><code>~x</code></font>     |
| 4          | <font color='red'><code>*</code></font>, <font color='red'><code>/</code></font>, <font color='red'><code>//</code></font>, <font color='red'><code>%</code></font>   |
| 5          | <font color='red'><code>+</code></font>, <font color='red'><code>-</code></font>     |
| 6          | <font color='red'><code>&gt;&gt;</code></font>, <font color='red'><code>&lt;&lt;</code></font>     |
| 7          | <font color='red'><code>&amp;</code></font>      |
| 8          | <font color='red'><code>^</code></font>       |
| 9          | <font color='red'><code>\|</code></font>     |
| 10          | <font color='red'><code>==</code></font>, <font color='red'><code>!=</code></font>, <font color='red'><code>&gt;=</code></font>, <font color='red'><code>&lt;=</code></font>, <font color='red'><code>&gt;</code></font>, <font color='red'><code>&lt;</code></font>, <font color='red'><code>is</code></font>, <font color='red'><code>is not</code></font>, <font color='red'><code>in</code></font>, <font color='red'><code>not in</code></font>      |
| 11          | <font color='red'><code>not</code></font>      |
| 12          | <font color='red'><code>and</code></font>       |
| 13          | <font color='red'><code>or</code></font>      |

其實不用特別去記，用久了就會習慣了，如果真的不知道誰先誰後就用<font color='red'><code>()</code></font>把要先做的括起來。

<hr>

## • 希望這些筆記可以幫到你 •
如果有興趣了解更多歡迎追蹤我的
<font size=3>[Intagram](https://www.instagram.com/matcha_code/)</font>
<font size=3>[Youtube](https://www.youtube.com/@matchacode)</font>
<font size=3>[Github](https://github.com/OG-Matcha/Python-Class)</font>

也可以幫我按個**讚賞**喔

<div style="display: flex; justify-content: left">
<a href="https://hackmd.io/@MatchaCode/Input" role="button"> 上一篇: L6 Input() (輸入)</a>
</div>