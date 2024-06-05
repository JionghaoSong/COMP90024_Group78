# Report Comments

There was no need to include all of the code in the zip file. It would have been ok if you just had the git repo link in your report. You had a diverse set of scenarios that required use of many diverse data sets that would allow exploration of the Cloud technologies (k8s, ElasticSearch, and Fission). You could have been a tad more explicit about "your" experiences with MRC and OpenStack (and the same for k8s, ElasticSearch, and Fission). 

Thus section 1.3.2 Kubernetes should have focused on Figure 2 and Figure 3 should have been your clusters. Right now it is quite generic and provides a description of the technology as opposed to what you did with it and the lessons learnt. You should have had an overall system architecture ideally describing your implementation, e.g. what ElasticSearch indexes did you create; what Fission functions did you realize; what was the specification of the resources you used (how many cores/how much storage for the MRC nodes, etc.); what external APIs did you use; you might have included the details of the REST-based API you developed, etc. 

The data collection/processing (section 3) was ok but you might have been more prescriptive. What specific data from VicGov, the BoM, SUDO did you use, i.e. what specific attributes related to the weather did you use? The graphs, charts, and map-based visualizations are nicely done. It was good that you supported different tests, but you might have expanded upon this, e.g. show explicit tests and what they tested. Also would have been good to explain who wrote the tests (the person who wrote the software being tested?). It was possible to support CI through GitHub actions. Nice use of Slack and Jira. Overall the report is well written and meets the core criteria - just a pity that quite a bit of it was overly generic.

# Implementation Comments

## Repo Layout
Good layout, however, you should have used a `.gitignore` file to ignore those unwanted files (e.g. `.env`, `__pycache__`) from being committed. A plaintext password was found in the repo.

## Documentation
Excellent documentation.

## RESTful API
Basic API implementation. Could have made the API simpler without the `data` suffix.

## Test Quality
Good test coverage. However, the tests cannot be run out-of-box. Many files required during the tests were not in the correct location (e.g. modules in elastic, files in data, JSON files on GDrive, etc.). Some tests failed during my test. Consider using coverage to generate a coverage report.

## Error Handling
Minimal error handling in code. Consider implementing consistent and comprehensive error handling.

## Harvesting
Solid work in harvesting. However, could have used Fission for harvesting as well.

## Use of Fission
Basic use of Fission. Didn't use specs or timer. Consider using secrets and configmaps in Fission functions.

## Use of ElasticSearch
Fair use of ElasticSearch. Used efficient batching for bulk indexing to handle large datasets. Consider adding error handling for index creation and deletion. Consider extracting common configuration settings into configmap.

## Code Quality
Code quality could have been improved. Many lint issues were found. Consider following PEP8 guidelines for Python code style. Minimal inline comments in the code. There was a long list of Python packages in `requirements.txt` file, are they all required and used? Some of the packages are OS specific, consider using `sys_platform` to install them conditionally.

## Architecture
Use of Kubernetes was OK overall. ConfigMaps would have been a nice addition.





# Report Comments

没有必要在压缩文件中包含所有代码，只需在报告中提供Git仓库链接即可。你涵盖了多种场景，需要使用多种不同的数据集来探索云技术（K8s、ElasticSearch和Fission）。你可以更明确地描述你在MRC和OpenStack（以及K8s、ElasticSearch和Fission）方面的经验。因此，1.3.2节的Kubernetes应该集中于图2，而图3应该展示你的集群。目前这一部分比较笼统，提供的是技术描述，而不是你如何使用它以及学到了什么。

你应该有一个整体的系统架构图，理想情况下描述你的实现情况，例如你创建了哪些ElasticSearch索引；实现了哪些Fission函数；使用了什么规格的资源（MRC节点的核心数/存储量等）；使用了哪些外部API，可能还包括你开发的基于REST的API的详细信息，等等。数据收集/处理（第3节）部分还可以，但你可以更详细一些。你从VicGov、BoM、SUDO具体使用了哪些数据，即你使用了哪些与天气相关的具体属性？图表和基于地图的可视化做得很好。你支持不同的测试是好的，但你可以进一步扩展，比如展示具体的测试以及测试的内容。还可以解释一下是谁编写的这些测试（是编写被测试软件的人吗？）。通过GitHub actions支持CI是可能的。很好地使用了Slack和Jira。总体而言，报告写得很好，满足了核心标准——只是有些部分过于笼统。

# 实现评论

## 仓库布局
布局良好，但应该使用`.gitignore`文件忽略那些不需要提交的文件（例如`.env`、`__pycache__`）。在仓库中发现了明文密码。

## 文档
文档非常好。

## RESTful API
基本的API实现。可以不使用`data`后缀，使API更简单。

## 测试质量
测试覆盖率良好。然而，测试无法开箱即用。测试过程中所需的许多文件不在正确的位置（例如elastic中的模块，data中的文件，GDrive上的JSON文件等）。一些测试在我的测试中失败了。考虑使用coverage生成覆盖率报告。

## 错误处理
代码中的错误处理较少。考虑实现一致且全面的错误处理。

## 数据收集
数据收集工作扎实。然而，可以使用Fission进行数据收集。

## Fission的使用
Fission的使用较为基础。没有使用specs或timer。考虑在Fission函数中使用secrets和configmaps。

## ElasticSearch的使用
ElasticSearch的使用尚可。使用了高效的批处理进行批量索引以处理大数据集。考虑为索引创建和删除添加错误处理。考虑将常见的配置设置提取到configmap中。

## 代码质量
代码质量有待提高。发现许多lint问题。考虑遵循Python代码风格的PEP8指南。代码中几乎没有内联注释。`requirements.txt`文件中列出了很多Python包，这些包都是必须和使用的吗？其中一些包是特定于操作系统的，考虑使用`sys_platform`有条件地安装它们。

## 架构
总体上Kubernetes的使用还可以。ConfigMaps会是一个不错的补充。





As you are probably all aware, assignment 2 scores are now released. The overall distribution for assignment 2 was:

- 25.9% H1
- 18.1% H2A
- 11.1% H2B
- 13% H3
- 24.6% Pass
- 7.3% "Other" :-(

Top team mark was 38/40 (two teams achieved this). I do not enforce the hurdle so if you get >= 50 for assignment 1 + assignment 2 + the exam you pass.
