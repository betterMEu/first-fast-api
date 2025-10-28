# 项目初始化
安装项目构建工具uv
~~~
pip install uv
~~~
uv构建环境
~~~
uv init [project_name]
~~~


# 安装依赖

安装开发环境依赖

```
# 安装运行时依赖
uv pip install .

# 安装开发依赖
uv pip install .[dev]

# 安装所有依赖（包括开发依赖）
uv pip install -e .[dev]

# 卸载所有已安装的包
uv pip uninstall --all
```

更新uv.lock文件
```
# 更新所有依赖并重新生成锁文件
uv lock --upgrade

# 更新特定包
uv lock --upgrade-package fastapi

# 同步更新后的依赖到环境
uv sync

# 根据 uv.lock 文件重新同步环境
uv sync --locked
```

```
# 添加新的运行时依赖
uv add package_name

# 添加新的开发依赖
uv add --group dev package_name
```

为什么需要区分环境依赖？
1. 安全考虑
     生产环境不应该安装开发调试工具
       避免潜在的安全漏洞暴露在生产环境中
       减少攻击面，只保留必要的运行时依赖

2. 性能优化
     开发工具通常会消耗额外资源
       生产环境需要更轻量级的依赖包
       避免不必要的包增加部署时间和内存占用

3. 功能分离

   ```
   # 开发环境需要的工具
   pytest          # 测试框架
   black           # 代码格式化工具
   flake8          # 代码检查工具
   debug-toolbar   # 调试工具
   
   # 生产环境需要的工具
   gunicorn        # Web服务器
   psycopg2        # 数据库连接器
   
   ```

4. 成本控制
   某些开发工具可能有许可证费用
   减少生产环境的包数量可以降低维护成本
   避免安装大型开发依赖影响容器镜像大小
5. 环境一致性
     确保开发、测试、生产环境使用相同的运行时依赖
     避免"在我机器上能跑"的问题
     每个环境只安装自己需要的包

6. 部署效率
     生产环境部署时不需要下载和安装开发工具
     减少CI/CD流水线的时间
     降低网络传输和存储开销
     这种做法遵循了"最小权限原则"，每个环境只包含其必需的依赖项。



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
使用命令行提交代码才会执行代码检查
~~~
git add .
git commit -m "message"
~~~
