---
title: openpose
---

# Openpose
## 模型来源
OpenPose模型采用CMU预训练好的模型，本项目选取了其中18关键点的人体骨架模型。
[免责声明](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/LICENSE)
[CMU openpose 项目源码](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
  ## 模型转换
  首先下载[model文件]()以及[weight文件]()
  在MindStudio中选择“Tools”->“Model Converter”打开模型转换器；分别加载model文件和weight文件，并设置参数如下图。其中，H与W可自行选择，但需要注意，改变H与W后，Openpose预处理、后处理函数中，部分参数需随之修改。
  
  ## 模型输入
受到模型转换格式的限制，预处理中，使用opencv读入的图片格式为HWC，要将图片转换为CHW格式，并且由于om模型不支持动态大小输入，需要将图片拉伸到固定的长宽大小，本项目中设置为120 * 160

## 编译方法
## 环境部署
需要安装opencv库与eigen库。
### 运行环境安装
登录开发者板，进入root用户，运行以下命令。
>apt-get install build-essential libgtk2.0-dev libavcodec-dev libavformat-dev libjpeg-dev libtiff5-dev libswscale-dev git cmake libswscale-dev python3-setuptools python3-dev python3-pip pkg-config -y
>pip3 install --upgrade pip
>pip3 install Cython
>pip3 install numpy

从当前的root用户切换回普通用户。
>exit

安装opencv
>cd $HOME
>git clone -b 4.3.0 https://gitee.com/mirrors/opencv.git
>git clone -b 4.3.0 https://gitee.com/mirrors/opencv_contrib.git
>cd opencv
>mkdir build
>cd build
>cmake -D BUILD_SHARED_LIBS=ON  -D BUILD_opencv_python3=YES -D BUILD_TESTS=OFF -D CMAKE_BUILD_TYPE=RELEASE -D  CMAKE_INSTALL_PREFIX=/home/HwHiAiUser/ascend_ddk/arm -D WITH_LIBV4L=ON -D OPENCV_EXTRA_MODULES=../../opencv_contrib/modules -D PYTHON3_LIBRARIES=/usr/lib/python3.6/config-3.6m-aarch64-linux-gnu/libpython3.6m.so  -D PYTHON3_NUMPY_INCLUDE_DIRS=/usr/local/lib/python3.6/dist-packages/numpy/core/include -D OPENCV_SKIP_PYTHON_LOADER=ON ..
>make -j8
>make install

使python3-opencv生效
>su root
>cp /home/HwHiAiUser/ascend_ddk/arm/lib/python3.6/dist-packages/cv2.cpython-36m-aarch64-linux-gnu.so /usr/lib/python3/dist-packages
>exit

打开配置文件
>vi ~/.bashrc

添加
>export LD_LIBRARY_PATH=/home/HwHiAiUser/Ascend/acllib/lib64:/home/HwHiAiUser/ascend_ddk/arm/lib

保存、退出后
>source ~/.bashrc

### 同步到开发环境
>mkdir $HOME/ascend_ddk
>scp -r HwHiAiUser@192.168.1.2:/home/HwHiAiUser/ascend_ddk/arm $HOME/ascend_ddk/
>su root
>cd /usr/lib/aarch64-linux-gnu
>scp -r HwHiAiUser@192.168.1.2:/lib/aarch64-linux-gnu/* ./
>scp -r HwHiAiUser@192.168.1.2:/usr/lib/aarch64-linux-gnu/* ./
>exit
>sudo apt-get install -y g++-5-aarch64-linux-gnu
>sudo apt-get install -y g++-aarch64-linux-gnu
## 应用推理精度
由于本项目有较高的实时性要求，因此将应用场景限制于单人识别，并尽可能简化了openpose的后处理代码，删去CMU原项目中局部最大值、关键点连接匹配、人体匹配的筛选步骤，直接选取每张特征图中最高值作为检测到的关键点，并用一个阈值判断是否识别准确，识别效果尚可。