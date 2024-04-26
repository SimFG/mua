# milvus any operation

English | [中文](README_CN.md)

## Why does this project exist?

As a Milvus developer, I am involved in the development of various features in Milvus as part of my regular work. Additionally, I often need to troubleshoot Milvus issues reported by the community and our collaborative users.

During this process, I found it somewhat cumbersome every time I made a gRPC call to Milvus. I had to open the pymilvus project, make modifications to some example code, and then run it. Many times, I had to make multiple changes to the code, which was quite tedious. I also attempted to use other tools like the HTTP client tool in GoLand or gRPC calls in Postman, which partially addressed the problem of repeatedly modifying parameters. However, they introduced a new issue of not being able to construct complex parameters.

The core objective of this project is to enable interaction with Milvus by freely adjusting parameters without the need to open any project code.

## Who is suitable for using this project?

1. Milvus developers
2. Milvus administrators responsible for **testing cluster** operations and maintenance

This project has not yet undergone **sufficient testing**, so please do not use any APIs from this project in a production cluster. Since this project does not perform parameter validation, **users must ensure the legality of the parameters themselves**. Of course, Milvus services also perform a series of parameter validations, but unexpected situations may still occur. If you encounter any issues, please provide feedback in the issue section.

## Project Highlights

During the development process, we interacted with Milvus in the following ways:

- SDK interaction: [pymilvus](https://github.com/milvus-io/pymilvus)
- Milvus UI app interaction: [attu](https://github.com/zilliztech/attu)
- Command-line interaction based on SDK: [milvus_cli](https://github.com/zilliztech/milvus_cli)

All of these methods are aimed at Milvus users, but they may not be very user-friendly for Milvus developers as they cannot directly access the native gRPC interface in a faster and more convenient way. Additionally, there is another tool, primarily used for viewing Milvus metadata, called [birdwatcher](https://github.com/milvus-io/birdwatcher), which is frequently used in troubleshooting.

The core purpose of the project is to facilitate developers' interaction with Milvus to the maximum extent. This is reflected in the following aspects:

1. Directly constructing gRPC requests to interact with Milvus, with minimal parameter validation.
2. The response can be in JSON format. By using the project's CLI tool, it becomes easier to interact with Milvus using jq commands, Linux pipelines, or custom Bash scripts.
3. Lightweight, with minimal dependencies.

## Installation

**Usage Tips**

1. The tool is currently developed based on milvus proto, which means that if you use the tool to connect to other versions of milvus, there may be unexpected behaviors for some interfaces. Please refer to the following table for specific correspondences.
2. Do not use parameters that you do not understand, as many parameters are hidden in the official milvus SDK with the main purpose of reducing understanding and usage costs.
3. Parameters are generally not validated.
4. Some interfaces in the project have not been tested, which means they may not work. If you find any issues, please submit an issue.
5. The return values are native gRPC return values, and some of them have complex structures.
6. When using on macOS, there may be a slow loading time for the first use, approximately 10 seconds.

### macOS

Currently, the macOS binary is compiled using x86 machines. It has not been tested on M1 chips, so it is uncertain whether it can be installed successfully.

```
brew install simfg/su/mucli
```

### Linux

You can download the binary from the [GitHub Release](https://github.com/SimFG/mua/releases/) and then add it to the PATH environment variable.

```
wget https://github.com/SimFG/mua/releases/download/0.0.2/mucli-v0.0.2-linux.tar.gz -O mucli.tar.gz

tar -zxvf mucli.tar.gz
```

After these steps, you will have an executable mucli binary in the mucli folder, and you can start using it.

Please note that **do not move the executable file from the folder to another location** because it depends on the files in the _internal folder within the current folder.

## Version List

It is recommended to use the mucli tool that corresponds to the respective Milvus version to avoid potential compatibility issues due to inconsistent proto files.

|   mucli   |    milvus    |     date     |
| --------- | ------------ | ------------ |
| v0.0.3    | v2.4.0-rc.1  | 2024.4.19    |
| v0.0.1    | v2.4.0-rc.1  | 2024.3.13    |

## mucli Quick Start

### Connecting to Milvus

Currently, there are two ways to connect to Milvus: specifying parameters and using the .env file. If both methods are used, the .env file takes precedence.

1. Specifying parameters

```
mucli -u localhost:19530 -t 'root:Milvus' -d default {{command}}
```

2. Using the .env file

By default, the .env file in the current folder will be read.

```
// .demo.env file content
MILVUS_URI=https://xxxx:19530
MILVUS_TOKEN=root:Milvus
MILVUS_DATABASE=default
```

```
mucli -e '.demo.env' {{command}}
```

Note: Before using any related commands, make sure to specify the connection parameters.

### Built-in Query Command Aliases

- View the collection list: `mucli collections`
- View the partition list: `mucli partitions -n {{collection_name}}`
- View the database list: `mucli databases`
- View the user list: `mucli users`
- View the role list: `mucli roles`

You can use the jq command to obtain more concise JSON information or view arrays. For example, to check the number of collections: `mucli collections | jq ".collectionNames | length"`

### help Command

- View a list of all subcommands: `mucli --help`
- View the usage of a specific subcommand: `mucli {{command}} --help`
- Fuzzy search the list of subcommands, e.g., `mucli collection`, will return a list of commands that contain the word "collection".

### Built-in Shortcut Commands

Certain commands require many parameters to be set by default, such as creating a collection, inserting data, etc.

- Quickly create a collection: `mucli create-collection --name hello_milvus --auto-field true`
- Quickly create a collection with a partition key: `mucli create-collection --name hello_milvus --auto-field true --auto-partition true`
- Insert random data: `mucli insert --name hello_milvus --random-data true`
- Insert 5000 random data points: `mucli insert --name hello_milvus --random-data true --random-num 5000`

### List of Commonly Used Commands

If you encounter any errors with the commands, please feel free to raise an issue as some commands have not been tested.

```
mucli create-collection --name hello_milvus --auto-field true

mucli insert --name hello_milvus --random-data true

mucli flush --name hello_milvus

mucli flush-state --name hello_milvus

mucli create-index --name hello_milvus

mucli load-collection --name hello_milvus

mucli query --name hello_milvus --expr 'pk in [10, 20]' --field pk --field random

mucli search --name hello_milvus --random-vector true --field pk

mucli query-star --name hello_milvus

mucli release-collection --name hello_milvus

mucli drop-index --name hello_milvus

mucli drop-collection --name hello_milvus

mucli create-user --username foo --password 123456

mucli -u localhost:19530 -t foo:123456 collections

mucli create-role --role-name insert_role

mucli operate-user-role --username foo --rolename insert_role --add

mucli operate-privilege --rolename insert_role --object-name foo --object-type collection --privilege Insert --grant

mucli collections | jq '.collectionNames'

mucli collections | jq '.collectionNames | length'

mucli get-config -c dataNode -f datanode.memory.forcesyncsegmentnum

mucli querynode get-data-distribution

mucli query-node query-node-metric
```

## Follow-up Plan

This project was developed in my spare time because I need to interact with Milvus frequently in my work. Typically, if there aren't too many issues which are not handled, I will fix them within 2-3 days. Your star will be my greatest source of support!

1. ~~Develop an HTTP proxy service for Milvus service.~~ (milvus has supported the restful api)
2. Add RPC calls for internal nodes.
3. [done] Query Milvus configurations.
4. Provide more user-friendly error messages when encountering exceptions.
5. Implement dynamic loading of commands.
6. Optimize the usage of search/query and other interfaces.