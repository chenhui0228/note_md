# vim使用指南

### 认识vim
- vim是一个编辑器，也是一个程序设计器
- vim具有块选择，多文件及多窗口等功能

### vim配置
- /etc/vimrc  系统默认，不建议修改
- ~/.vimrc  用户自定义设置
- ~/.viminfo  操作过的命令记录
- `set all` 查看所有的配置，比较多

### vim使用
- 操作模式
  - 一般模式 光标移动，复制粘贴，查找替换, 撤消与重做
    - hjkl,ctrl+fbdu,+-,0$^,HML,Ggg
    - xXrRdypc
    - /? n1,n2s/old/new/gc 
    - u,ctrl+r 
  - 编辑模式
    - i I o O r R a A
  - 命令行模式
    - :w :w! :wq :q :q! :w [filename] n1,n2 w[filename] :! command :set nu set nonu
  - 块选择
    - v V ctrl+v y d
  - 多文件
    - vim file1 file2
    - :n :N :files
  - 多窗口
    - :sp [filename] :vsp [filename]
    - ctrl+w + hjkl
    - ctrl+w + q
