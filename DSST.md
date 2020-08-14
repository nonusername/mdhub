---
title: DSST
tags: 新建,模板,小书匠
renderNumberedHeading: true
grammar_cjkRuby: true
---

# DSST
解决尺度变化问题。
based on the discriminative correlation filters employed in the MOSSE tracker.
分别学习平移滤波器和尺度滤波器。
## Introduction
现有的方法缺陷：在复杂图片序列中，尺度变化大时检测效果差，或是因速度慢而不适用于实时监测。

## Learning discriminative correlation filters
使用一定数量的灰度图像块f，label g是有高斯函数构建的。经过一定转换，可得到滤波器。

### circular correlation
卷积？

## Our Approach
将标准的判别式相关滤波器扩展到多维特征，并提出尺度估计方法。
通过分别更新滤波器的分子与分母，减少计算量。
HOG是怎么配合使用的？？？

关于尺度，训练一个M * N * S 的filter，？？？

分别训练平移滤波器和尺度滤波器。
根据尺度滤波器的size S选取一系列大小的图像块。
尺度差异通常小于平移差异，所以先使用平移滤波器，再用尺度滤波器。

迭代次数 t
输入: 图片It  之前的目标位置Pt-1与尺度St-1，平移模型和尺度模型的分子、分母
输出：当前的目标位置Pt与尺度St，更新后的平移模型和尺度模型的分子、分母
平移估计：根据Pt-1和St-1选取平移样本，计算y，取y最大的位置Pt
尺度估计：根据Pt和St-1选取尺度样本，计算y，取y最大的St
模型更新：根据Pt和St取平移样本和尺度样本，更新模型参数



## DCF
