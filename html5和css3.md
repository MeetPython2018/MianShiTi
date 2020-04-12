### HTML（超文本标记语言）

#### 标签

- 单标签

  ```html
  <img src='' />
  <input name='' value='' type='text' placehold='提示性文字'>
  ```

- 双标签

  ```html
  <h1></h1> ~~ <h6></h6>
  <div></div> <span></span> <p></p> <ul></ul> <ol></ol> <li></li> <a></a> <table></table> <tr></tr> <th></th>
  ```

- 语义化标签：用恰当的HTML标记内容

  优点：1、提升可访问性  2、利于SEO  3、结构清晰，利于维护

  ```html
  <title>搜索引擎会将title作为判断页面主要内容的指标，有效的title应该包含几个与页面内容密切相关的关键字.</title>
  <h1>分级标题</h1>~~<h6></h6>
  <nav>标记导航，仅对文档中重要的链接群使用</nav>
  <main>页面主要内容，一个页面只能使用一次</main>
  <article>表示文档、页面、应用或一个容器</article>
  <section>具有相似主题的一组内容</section>
  <aside>指定附注栏，包括引述、侧栏、指向文章的一组链接、广告等</aside>
  <footer>页脚</footer>
  <small>指定细则，输入免责声明、注解、署名、版权</small>
  <strong>表示内容重要性</strong>  <em>标记内容重点（大量用于提升段落文本语义）</em>
  <mark>突出显示文本</mark>
  <time>标记时间</time>  <pre>预格式化文本</pre> <code>标记代码</code>
  ```

### CSS（层叠样式表）

#### 选择器

- *{}		通用选择器

- p{}        标签选择器

- .class-box{}        类名选择器

- id-box{}   id选择器

- 伪结构选择器

  - ```css
    el:first-child{}    # 匹配的是某父元素的第一个子元素，可以说是结构上的第一个子元素。
    ```

  - ```css
    el:first-of-type{}   # 匹配的是该类型的第一个，就是指所有el元素中的第一个。
    ```

  - ```css
    el:nth-child(arg)    # 作为子元素的第几个
    ```

  - ```css
    el:nth-of-type(arg)    # 作为同类型子元素的第几个  arg 可取num,even(偶数)，odd(奇数)，表达式(3n)
    ```

- el,el,el{}        群组选择器

- 属性选择器

  - ```css
    [attr]{}     # 选择拥有attr属性的元素
    ```

  - ```css
    el[attr='val']    # 选择属性值为val的el元素
    ```

  - ```css
    el[attr~='val']    # 选择属性值一个或多个为val的el元素
    el[attr^='val']    # 选择属性值以val开头的el元素
    el[attr$='val']    # 选择属性值以val结尾的el元素
    el[attr*='val']    # 选择属性值包含val的el元素
    ```

- 伪元素选择器

  ```css
  ::before{            # 在元素内容之前插入一个元素
      content:'';
  }
  ::after{
      content:'';      # 在元素内容之后插入一个元素
  }
  ```

##### 选择器的优先级

行内样式 > ID选择器 > 类名选择器 > 标签选择器 > 通用选择器

#### CSS中的颜色

```css
color: red/green/blue/yellow/pink/blank...;      # 预定义颜色
color: #ff6700;    # 十六进制表示的颜色     
coloe: rbg(255,110,110);      # RGB颜色
color: rgba([0-255],[0-255],[0-255],opacity);    # 带透明度的RGB颜色
```

#### CSS中的背景图、阴影、box设置

##### 背景图设置

```css
background-img: url('');    # 引入图片作为背景时，填写图片的url(多张图片的url用逗号隔开)
background-size: 100% auto;     # 背景图的尺寸
background-repate: no-repate;    # 背景图是否重复
background-position: x y;   # x、y为数值，表示方位
```

##### 阴影设置

```css
box-shadow: 1px 1px 0 5px rgba(0,0,0,.5)
# x轴偏移量、y轴偏移量、阴影的模糊程度、阴影的大小、阴影的颜色
box-size: border-box;   # 将边框大小算入内容区
```

#### 2D、3D属性

##### 2D transform

```css
transform: translate(x,y);  # 平移
transform：rotate(180deg);   # 旋转
transform: scale(.8);    # 缩放
transform: skew();    # 斜切
```

##### 2D过渡

```css
transition: all .5s;
transition-property: ;
transition-duration: ;                  #  过渡效果持续时间
transition-timing-function: easy;		#  贝塞尔曲线  
transition-delay: ;					   #  过度延迟时间
```