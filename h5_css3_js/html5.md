# HTML
## html标签元素的分类 可以通过{display: block;}进行改变
- 块状元素 <div> <p> <h1>...<h6> <ol> <ul> <dl> <li> <table> <address> <blockquote> <form>
    - 特点1：独占一行
    - 特点2：元素高，宽，行高，边距都可设置
    - 特点3：若不设置，将与本身父容器100%

- 行内元素 <span> <a> <label> <strong> <em> <br> <i> <label> <q> <cite> <code> <var>
    - 特点1：和其它元素一行
    - 特点2：元素高，宽，行高，边距不可设置
    - 特点3：元素宽度不可改变

- 内联块状元素 <img> <input>
    - 特点1：和其它元素都在一行上
    - 特点2：元素高，宽，行高，边距都可设置

## html文档标签
- 根元素 <html> 
- META元素 <head> <title> <base> <link> <meta> <style>
- 部件标记 <body> <section> <nav> <article> <aside> <h1>...<h6> <hgroup> <header> <footer> <address>
- 分组内容 <p> <hr> <br> <pre> <blockquote> <ol> <ul> <dl><dt><dd> <figure> <figcaption> <div>
- 文本语义 <a> <em> <strong> <small> <cite> <q> <dfn> <abbr> <code> <var> <samp> <kbd> <sub><sups> <i> <b> <mark> <ruby> <rt> <rp> <bdo> <span> <ins> <del>
- 嵌入式内容标记 <img> <iframe> <embed> <object> <param> <video> <audio> <source> <canvas> <map> <area>
- 表格 <table> <caption> <thead> <tbody> <tfoot> <tr> <th> <td>
- 表单 <form> <input> <label> <button> <select> <option> <textarea> <output> <keygen> <progress> <meter>
- 脚本元素 <script> <noscript>

## html属性
- 全局属性 class id lang style tabindex title translate draggable dropzone
- 标签属性
    - <meta> :
    - <link> :
- 事件属性
    - windowns事件： onload onredo onundo onmessage ononline onerroe
    - 表单事件: onblur onchange oncontextmenu onfocus onformchange onforminput oninput oninvalid onreset onselect onsubmit
    - 键盘事件: onkeydown onkeypress onkeyup
    - 鼠标事件：onclick ondblclick ondrag ondragend ondragenter ondragleave ondragover ondragstart ondrop onmousedown onmousemove onmouseout onmouseover onmouseup onmousewheel onscroll
    - Media事件：onerror onpause onplay onplaying onprogress onseeked onseeking onstalled onsuspend ontimeupdate onwaitiong
