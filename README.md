# 项目初始化
安装项目构建工具uv
~~~
pip install uv
~~~

（项目创建者）uv初始化项目，生成环境（.venv文件）等
~~~
uv init [project_name]
~~~

# 依赖和环境（.venv）

## 依赖

- **增加**

  - 依赖

    ```
    uv add <package_name>
    ```

  - 分组中的依赖

    ```
    # dev分组
    uv add --group dev <package_name>
    ```
  
  
  
- **安装**

  - 运行时依赖

    ```
    uv pip install .
    ```

  - dev依赖

    ```
    uv pip install .[dev]
    ```

  - 所有依赖（包括dev依赖）

    ```
    uv pip install -e .[dev]
    ```

  

- **卸载**

  - 所有已安装的包

    ```
    uv pip uninstall --all
    ```

    

## 环境

> 什么是环境？
>
> 程序代码运行在环境中，使用uv时，环境以uv.lock为蓝图，而uv.lock根据项目依赖而生成



如果 pyproject.toml 中的依赖存在更新的可兼容版本（如依赖要求是fastapi>=0.120.0，但0.121.0是可兼容的最新版本，将会提示更新），开发者可选择更新

具体操作：

（1）更新依赖，重新uv.lock文件

```
# 更新所有依赖并重新生成锁文件
uv lock --upgrade

# 更新特定依赖
uv lock --upgrade-package fastapi
```

（2）依赖更新完，要以uv.lock为蓝图，重新搭建环境

```
uv sync --locked
```

不使用[--locked]，环境将可能使用 pyproject.toml 中约束的新版本，不严格遵循lcok文件

# 启动



uvicorn启动
```
uvicorn main:app [--port 3000] [--reload]
```
* main: Python 模块名称（即 main.py 文件）
* app: 在 main.py 模块中定义的应用实例



uv启动
```
uv run -- uvicorn main:app [--port 3000] [--reload]
```


fastapi-cli启动（调用uvicorn启动）
```
fastapi dev  （热加载）
fastapi run
```


# 代码提交检查
使用命令行提交代码才会执行代码检查，按顺序执行以下命令
~~~
git add .
pre-commit run
git commit -m "message"    
~~~
执行提交命令前最好先执行pre-commit run进行检查和格式化，否则提交时发现不符合规范会进行修改但会中断提交，修改的文件需要重新加到缓冲区（git add .)，即重走这三个步骤







# FastApi

## 环境变量

### 命令行设置



### [静态文件.env设置](https://fastapi.tiangolo.com/zh/advanced/settings/#env)
