### 简答题

1、如下代码执行结果是什么？为什么？

```javascript
function a(){
    b(a);
    var a = 6;
    function b(){
        console.log(a);   
    }
}
a();    // undefined
```

2、手写一个闭包，简述闭包的用途及其利弊。

```javascript
var f1 = function a(){
    var x = 'x';
    return function(){
        console.log(x);
    }
}
f1();    // 调用a函数
// 用途：可以读取函数内部的变量；让这些变量始终保存在内存中
// 弊端：由于闭包将函数内部的变量保存在了内存中，内存消耗大，所以不能滥用闭包，否则造成网页性能问题，在IE中有可能造成内存泄漏，办法是退出函数时，将不使用的局部变量删除掉。
```

3、apply与call两者有什么区别？

```javascript
function getAge(){
    var y = new Date().getFullYear()
    return y - this.birth
}
var people = {
    name:'曹',
    birth:1996,
    age:getAge
}
people.age();    // 24
getAge.apply(people,[]);    // 24

// apply()和call()都是函数身上用于改变this指向的函数，接收两个参数，第一个是需要绑定的this对象，第二个是函数本身的参数
// 不同之处：apply()的第二个参数是以数组的形式传入，call()则是按顺序传入
```

4、箭头函数与普通函数有什么区别？

```javascript
var obj = {
    a:10,
    b:function(n){
        let f = e=>{
        	return this.a + n   
        }
        return f(n)
    },
    c:function(n){
        let f = e=>{
            return this.a + n
        }
        let m = {
            a:20
        }
        return f.apply(m,n)
    }
    d:function(n){
        let f = function(n){
            return this.a + n
        }
        let m = {
            a:20
        }
        return f.call(this,n)
    }
}
console.log(obj.b(1))		// 11
console.log(obj.c(1))		// 11
console.log(obj.d(1))		// 21

// 箭头函数不绑定arguments，但可使用...rest参数
// 普通函数里面this默认指向window对象；箭头函数的this是此法作用域由上下文确定；箭头函数的apply()和call()不会改变this代表的对象；箭头函数不能用作构造函数,不能使用new；箭头函数没有原型属性
```

5、列举至少两种字符串中检测匹配子串的方式

```javascript
arr.indexOf();			// 查找字符串中符合条件的子串的位置，未找到时返回-1
arr.lastIndexOg();		// 查找字符串中符合条件的子串的位置，未找到时返回-1（从后往前）
arr.search();			// 查找字符串中符合条件的子串的位置，未找到时返回-1,可使用正则
arr.math();				// 查找字符串中符合条件的子串的位置，找到时返回一个数组，未找到时返回null
```

6、列举实现垂直居中的方法

```css
position:absolute;   // 使用绝对定位实现水平居中
left:0;
right:0;
margin:0 auto;

position:absolute;   // 使用绝对定位实现垂直居中
top:0;
bottom:0;
margin: auto 0;

position:absolute;   // 使用绝对定位实现绝对居中
left:0;
right:0;
top:0;
bottom:0;
margin:auto auto;

display:flex;		// 使用flex实现垂直居中
justify-content:flex-start;
align-items:center;
```

7、列出行内元素与块元素标签的不同

```html
行内元素不可设置宽高，在一行内显示
块元素可以设置宽高，独占一行
```

8、如何提升页面性能

```html
资源合并压缩，减少http请求
非核心代码的异步加载
使用浏览器的缓存
使用CDN
DNS的预解析
```

9、浏览器访问网页，第一次加载较慢，第二次刷新页面加载明显加快，针对这简述浏览器的缓存机制

```html
第一访问页面时没有缓存，浏览器下次再请求时，可直接从本地磁盘中读取，而不用重新请求
强缓存：不用请求服务器，直接使用本地缓存
设置response header的Cache-Control(服务器返回的相对时间)  Expires(服务器返回的绝对时间)
协商缓存：浏览器发现本地有资源的副本，不确定是否使用，就去问问服务器。当浏览器的强缓存没有命中时，就去服务器验证协商缓存是否命中
```

10、正则匹配小数

```javascript
var phone = /^1[3456789]/d{9}$/;      // 匹配手机号
var email = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]*+\.([a-zA-Z]{2,4})$/		// 匹配邮箱
var xiaoshu = /^(([1-9][0-9]*\.[0-9]{1,2})|([0]\.\d{1,2}))$/
```

11、简述你对前端三大流行框架其中之一的了解（Vue优先）

### 编程题

1、手写一个es5实现继承的例子

2、手写实现深拷贝的方法

```javascript
// 深拷贝
var people = {
    name:'应用',
    arrs:['多','快','好','省'],
    objs:{
        a:1,
        b:2,
        c:3
    }
}
function deepCopy(p,c){
    var c = c || {}
    for(var i in p){
        if(typeof p[i] === 'object'){
            c[i] = p[i].constructor === Array ? []:{};
            deepCopy(p[i],c[i])
        }else{
            c[i] = p[i]
        }
    }
    return c
}
var person = deepCopy(people)
var res = JSON.parse(JSON.stringify(people))
people.arrs.push('不可能！')
console.log(people)
console.log(person)
console.log(res)
```

3、手写数组去重的方法

```javascript
    // 数组去重
    var arr1 = Array.from(new Array(1000000),(el,index)=>{
        return index
    })
    var arr2 = Array.from(new Array(500000),(el,index)=>{
        return index
    })
    function demo1(a,b){         // 利用filter和indexOf去重
        var all = a.concat(b)
        var new_all = all.filter((el,index)=>{
            return all.indexOf(el)===index
        })
        return new_all
    }
    function demo2(a,b){        // 双for循环去重
        var all = a.concat(b)
        for(var i=0,len=all.length;i<len;i++){
            for(var j=i+1;j<len;j++){
                if(all[i]===all[j]){
                    all.splice(j,1)
                    len--
                    j--
                }
            }
        }
        return all
    }
    function demo3(a,b){        // 利用for of和includes去重
        var all = a.concat(b)
        var result = []
        for (let i of all){
            !result.includes(i) && result.push(i)
        }
        return result
    }
    function demo4(a,b){
        var all = a.concat(b)       // 利用sort和for循环去重
        var result = [arr[0]]
        var sort_arr = all.sort()
        for(var i=1;i<sort_arr.length;i++){
            sort_arr[i]!==sort_arr[i-1] && result.push(sort_arr[i])
        }
        return result
    }
    function demo5(a,b){        // 利用Set去重
        var all = a.concat(b)
        return Array.from(new Set(all))
    }
    function demo6(a,b){        // 利用for of和Object去重
        let all = a.concat(b)
        let result= []
        let obj = {}
        for(i of all){
            if(!obj[i]){
                result.push(i)
                obj[i] = 1
            }
        }
        return result
    }
    var start = new Date();
    console.log('去重开始')
    console.log(demo6(arr1,arr2).length)
    var end = new Date();
    console.log('耗时',end-start)
```

### 提问Q

1、ajax里面的同步和异步是怎么回事？什么情况下会用到？

2、background-image 和img的不同之处？

4、ES6有哪些特性？

5、跨域问题怎么解决？

6、说说你对Vue 的理解、生命周期以及在其中都做什么事 