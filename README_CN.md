# milvus any operation

[English](README.md) | 中文

## 为什么会有这个项目？

作为一个Milvus开发者，我的日常工作涉及到许多Milvus功能的开发，同时也需要排查许多社区和合作用户的Milvus异常情况。

在这个过程中，我发现每次调用Milvus的gRPC都有些麻烦，需要打开pymilvus项目，然后修改一些示例代码，然后运行。很多时候，我需要反复修改代码，这样比较繁琐。我也尝试过使用其他工具，比如GoLand中的HTTP客户端工具、Postman中的gRPC调用，这些工具在一定程度上解决了反复修改参数的问题，但也带来了一个新的问题，即无法构造复杂参数。

这个项目的核心目标是：无需打开任何项目代码，就能够任意调整参数与Milvus进行直接交互。

## 谁适合使用该项目

1. milvus开发者
2. 负责**测试集群**运维的milvus管理员

该项目目前尚**未经过充分的测试**，请勿在生产集群中使用该项目中的任何API。由于该项目基本上不会对参数进行校验，因此用户需自行确保参数的合法性。当然，milvus服务也对参数进行了一系列校验，但仍可能存在意外情况。如果发现任何问题，请在issue中反馈。

## 项目亮点

在开发过程中，我们与Milvus的交互方式主要包括以下几种：

- 使用SDK进行交互：[pymilvus](https://github.com/milvus-io/pymilvus)
- 通过Milvus UI应用进行交互：[attu](https://github.com/zilliztech/attu)
- 基于SDK开发的命令行交互：[milvus_cli](https://github.com/zilliztech/milvus_cli)

以上方式都是面向Milvus用户的，但对于Milvus开发者来说并不是很友好，无法快速、方便地调用原生的gRPC接口。此外，还有一个其他工具用于查看Milvus的元信息：[birdwatcher](https://github.com/milvus-io/birdwatcher)，在问题排查中使用频率相对较高。

该项目的核心目标是尽可能方便开发者与Milvus进行交互，主要体现在以下几个方面：

1. 可以直接构造gRPC请求与Milvus进行交互，参数基本上没有校验；
2. 请求返回值可以为JSON格式，使用项目中的命令行工具，可以更方便地与jq命令、Linux管道进行交互，也可以自定义更多与Milvus交互的Bash脚本；
3. 轻量化，尽量减少依赖。

## 安装

**使用提示**

1. 工具目前依赖于 milvus 的 proto 进行开发。如果使用当前工具连接其他版本的 milvus，部分接口可能会出现不可预期的行为。具体对应关系请参考下表。
2. 对于不理解的参数，请勿使用，因为很多参数在 milvus 的官方 SDK 中被隐藏了，其主要目的是降低理解和使用成本。
3. 基本上不会对参数进行校验。
4. 项目中的某些接口并没有经过测试，可能会存在不工作的情况。如果发现，请提出 issue。
5. 返回值均为原生的 gRPC 返回值，其中部分返回值的结构较为复杂。
6. 在 macOS 上使用时，首次加载较慢，大约需要 10 秒左右。

### macOS

目前 macOS 二进制是使用 x86 机器编译的，对于 M1 芯片暂时未进行实验，无法确定是否能成功安装。

```
brew install simfg/su/mucli
```

### Linux

可以从 [GitHub Release](https://github.com/SimFG/mua/releases/) 中下载二进制文件，然后将其设置为 PATH 环境变量。

```
wget https://github.com/SimFG/mua/releases/download/0.0.2/mucli-v0.0.2-linux.tar.gz -O mucli.tar.gz

tar -zxvf mucli.tar.gz
```

这样，在 mucli 的文件夹下就会有一个可执行的 mucli 二进制文件，您就可以开始使用了。

请注意**不要将文件夹中的可执行文件单独移动到其他位置**，因为它依赖当前文件夹中的 _internal 文件夹中的文件。

## 版本列表

建议使用相应的 Milvus 版本的 mucli 工具，以免出现兼容性问题，因为 proto 文件可能不一致。

|   mucli   |    milvus    |     日期     |
| --------- | ------------ | ------------ |
| v0.0.1    | v2.4.0-rc.1  | 2024.3.13    |

## mucli快速使用

### milvus连接

目前提供两种方式来连接Milvus，分别是指定参数和指定.env文件，如果两者都存在，则使用.env文件。

1. 指定参数

```
mucli -u localhost:19530 -t 'root:Milvus' -d default {{command}}
```

2. 使用.env文件

默认情况下，会读取当前文件夹中的`.env`文件。

```
// .demo.env文件内容
MILVUS_URI=https://xxxx:19530
MILVUS_TOKEN=root:Milvus
MILVUS_DATABASE=default
```

```
mucli -e '.demo.env' {{command}}
```

注：在使用相关命令之前，需要先指定连接参数。

### 内置部分查询指令别名

- 查看collection列表：`mucli collections`
- 查看partition列表：`mucli partitions -n {{collection_name}}`
- 查看db列表：`mucli databases`
- 查看user列表：`mucli users`
- 查看role列表：`mucli roles`

可以配合jq命令使用，以获取更简洁的JSON信息或者查看数组。例如，要查看collection数目：`mucli collections | jq ".collectionNames | length"`

### help命令

- 查看所有子命令列表：`mucli --help`
- 查看某个子命令的用法：`mucli {{command}} --help`
- 模糊搜索子命令列表，例如：`mucli collection`，将返回所有带有"collection"字符的子命令列表

### 内置快捷指令命令

部分指令，默认情况下需要设置许多参数，例如创建collection、插入数据等。

- 快速创建collection：`mucli create-collection --name hello_milvus --auto-field true`
- 快速创建带有partition key的collection：`mucli create-collection --name hello_milvus --auto-field true --auto-partition true`
- 随机插入数据：`mucli insert --name hello_milvus --random-data true`
- 随机插入5000条数据：`mucli insert --name hello_milvus --random-data true --random-num 5000`

### 常用命令列表

以下命令均自己尝试过使用，使用其他命令遇到报错，请提issue，因为有些命令尚未经过测试运行。

```
mucli create-collection --name hello_milvus --auto-field true

mucli insert --name hello_milvus --random-data true

mucli flush --name hello_milvus

mucli create-index --name hello_milvus3

mucli load-collection --name hello_milvus

mucli query --name hello_milvus --expr 'pk in [10, 20]' --field pk --field random

mucli collections | jq '.collectionNames'

mucli collections | jq '.collectionNames | length'
```

## 后续规划

这个项目是在业余时间里开发的，因为在工作中需要频繁与Milvus进行交互。通常情况下，如果没有太多的issue反馈堆积，会在2-3天内进行修复并给出修复小版本。你的关注将是我最大的支持动力！

1. 开发 Milvus 服务的 HTTP 代理服务。
2. 添加内部节点的 RPC 调用功能。
3. 查询 Milvus 配置。
4. 在遇到异常情况时，提供更友好的错误信息。
5. 实现动态加载命令功能。
6. 优化 search/query 等接口的使用体验。