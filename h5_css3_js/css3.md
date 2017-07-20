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

## css定位
- static: 默认值，即没有定位，元素出现在正常的流中
- relative: 相对于正常位置的偏移，元素所占空间不会改变
- absolute: 相对于最近已定位的父元素，与文档流无关，不点空间，会有重叠
- fixed: 相对于窗口是固定位置，不流动，与文档流无关，不点空间，会有重叠

## css 属性
- 背影
    - background
    - background-attachment
    - background-color
    - background-image
    - background-position
    - background-repeat

- 文本
    - color
    - direction
    - letter-spacing
    - line-height
    - text-align
    - text-decoration
    - text-indent
    - text-shadow
    - text-transform
    - unicode-bidi
    - vertical-align
    - white-space
    - word-spacing

- 字体
    - font
    - font-family
    - font-size
    - font-style
    - font-variant
    - font-weight

- 链接
    - a:link
    - a:visited
    - a:hover
    - a:active

- 列表
    - list-style
    - list-style-image
    - list-style-position
    - list-style-type

- box
    - margin
    - border
    - padding
    - content
    - outline

- 边框
    - border
    - border-style
    - border-width
    - border-color
    - border-bottom
    - border-bottom-color
    - border-bottom-style
    - border-bottom-width
    - border-left
    - border-left-color
    - border-left-style
    - border-left-width
    - border-right
    - border-right-color
    - border-right-style
    - border-right-width
    - border-top
    - border-top-color
    - border-top-style
    - border-top-width
- 轮廓
    - outline
    - outline-color
    - outline-style
    - outline-width

- 边距
    - margin
    - margin-bottom
    - margin-left
    - margin-right
    - margin-top

- 填充
    - padding
    - padding-bottom
    - padding-left
    - padding-right
    - padding-top

- 尺寸
    - height
    - line-height
    - max-height
    - max-width
    - min-height
    - min-width
    - width

- 显示
    - display
    - visibility

- 定位
    - bottom
    - clip
    - cursor
    - left
    - overflow
    - overflow-y
    - overflow-x
    - position
    - right
    - top
    - z-index

- 浮动
    - clear
    - float

- css伪类
    - :checked
    - :disabled
    - :empty
    - :enabled
    - :first-of-type
    - :in-range
    - :invalid
    - :last-of-type
    - :not(selector)
    - :nth-child(n)
    - :nth-last-child(n)
    - :nth-last-of-type(n)
    - :nth-of-type(n)
    - :only-of-type
    - :only-child
    - :optional
    - :out-of-range
    - :read-only
    - :read-write
    - :required
    - :root
    - :target
    - :valid
    - :link
    - :visited
    - :active
    - :hover
    - :focus
    - :first-letter
    - :first-line
    - :first-child
    - :before
    - :after
    - :lang(language)

- css伪元素
    - :link
    - :visited
    - :active
    - :hover
    - :focus
    - :first-letter
    - :first-line
    - :first-child
    - :before
    - :after
    - lang(language)

