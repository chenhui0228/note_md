# CSS
## css概况
- css作用于更改html元素的 `字体` `颜色` `背景` `排版`(盒子模型：width,height, 内边距，外边距)
- 布局{流动模型：默认，浮动模型：使得块状元素可以在多行，层模型：（绝对，相对，固定定位）}

## css使用语法
- <link>
- <style>
- <h2 style="">

## css选择器
- 元素选择器 h1{}
- 类，ID选择器 #class_A {} .id_A {}
- 属性选择器 
    - h1[class] {}
    - a[href='www.haijunt.com']
    - a[class~='warn']
    - a[class^='warn']
    - a[class$='ing']
    - a[class*='warn']
- 后代选择器 h1 em{}
- 子元素选择器 h1 > em {}
- 相邻兄弟选择器 h1 + p {}
- 伪类
    - 锚伪类
        - a:link {}
        - a:visited {}
        - a:hover {}
        - a:active {}
    - p:first-child  # 作为某个元素的第一个子元素的所有p元素
    - q:lang(no) {}
- 伪元素
    - :first-line
    - :first-letter
    - :before
    - :after

