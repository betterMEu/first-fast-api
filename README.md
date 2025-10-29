# 项目初始化
安装项目构建工具uv
~~~
pip install uv
~~~

（项目创建者）uv初始化项目，生成环境（.venv文件）等
~~~
uv init [project_name]
~~~

# 安装依赖和环境（.venv）

## 依赖

- 安装

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

- 卸载

  - 所有已安装的包

    ```
    uv pip uninstall --all
    ```

    

## 环境

安装完依赖，同步（创建）环境

```
uv sync
```



如果有依赖变动，更新uv.lock文件

```
# 更新所有依赖并重新生成锁文件
uv lock --upgrade

# 更新特定包
uv lock --upgrade-package fastapi

# 根据 uv.lock 文件重新同步（创建）环境（uv.lock是环境实际使用的依赖）
uv sync --locked
```

```
# 添加新的运行时依赖
uv add package_name

# 添加新的开发依赖
uv add --group dev package_name
```


# 启动



uvicorn启动
```
uvicorn main:app [--port 3000] [--reload]
```
* uvicorn: ASGI 服务器，用于运行 Python 异步 Web 应用
* main: Python 模块名称（即 main.py 文件）
* app: 在 main.py 模块中定义的应用实例

uv启动
```
uv run -- uvicorn main:app [--port 3000] [--reload]
```
优势:
* 自动管理虚拟环境
* 确保使用正确的依赖版本
* 简化开发工作流

fastapi启动
```
框架层面: FastAPI 是 Web 框架，本身不能直接启动
实际执行: 通常通过 uvicorn 或其他 ASGI 服务器来运行 FastAPI 应用
开发模式: fastapi dev 命令实际上是调用 uvicorn 启动应用
```

推荐使用场景
* 开发阶段: 使用 uv run -- uvicorn src.main:app 确保环境一致性
* 生产部署: 直接使用 uvicorn src.main:app 或通过 Gunicorn 等 WSGI 容器
* 快速原型: fastapi dev 提供便捷的开发服务器（需要安装 fastapi[all]）


# 代码提交检查
使用命令行提交代码才会执行代码检查，按顺序执行以下命令
~~~
git add .
pre-commit run
git commit -m "message"    
~~~
执行提交命令前最好先执行pre-commit run进行检查和格式化，否则提交时发现不符合规范会进行修改但会中断提交，修改的文件需要重新加到缓冲区（git add .)，即重走这三个步骤
