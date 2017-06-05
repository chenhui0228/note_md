#!/usr/bash

content=$(tree ./)
echo '# note_md 使用markdown格式存放个人笔记' > README.md
cat>>README.md<<EOF
$(tree ./)
EOF

