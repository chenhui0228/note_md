# Anaconda install and configure

### Install Anaconda3.6

<pre>
# go https://anaconda.org/ 进行网页下载(选择python3.*环境)或者wget(有时较慢），但适用于无桌面服务器安装
wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
sh Anaconda3-5.0.1-Linux-x86_64.sh
source ~/.bashrc  # 使安装过程中(尽量选择yes)的conda,python环境变量生效
conda # 检查是否生效
</pre>

### upgrade to last

<pre>
# 配置清华源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
# 安装所有更新
conda upgrade --all
</pre>

### create virtualenv python2

<pre>
conda create -n py2 python=2.7
source activate py2
pip install *
conda install *
source deactivate py2
conda create --name py22 --clone py2 # 创建一个副本
conda remove --name py2 --all # 删除环境
</pre>

### use conda

<pre>
conda -h
conda --version
conda info --envs # 所有虚拟环境
conda list
conda list -n py2
conda search numpy
conda install -n py2 numpy
conda install --channel https://conda.anaconda.org/pandas bottleneck
conda env export > environment.yaml  # 先source activate py2进入虚拟环境
conda env create -f environment.yaml
conda update -n py2 numpy
conda remove -n py2 numpy
conda update conda
</pre>

### use pip

<pre>
pip install -U pip
pip list
pip list --outdate --format=columns # 检查需要更新的包
pip show packagename
pip search packagename
pip install packagename
pip install -U packagename
pip uninstall packagename
</pre>


