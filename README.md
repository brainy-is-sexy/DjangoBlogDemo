# DjangoBlogDemo
基于Django框架的个人博客搭建，并在服务器上部署


## 本地运行

可以使用 Virtualenv、Pipenv、Docker 等在本地运行项目，每种方式都只需运行简单的几条命令就可以了。

> **注意：**
>
> 因为博客全文搜索功能依赖 Elasticsearch 服务，如果使用 Virtualenv 或者 Pipenv 启动项目而不想搭建 Elasticsearch 服务的话，请先设置环境变量 `ENABLE_HAYSTACK_REALTIME_SIGNAL_PROCESSOR=no` 以关闭实时索引，否则无法创建博客文章。如果关闭实时索引，全文搜索功能将不可用。
>
> Windows 设置环境变量的方式：`set ENABLE_HAYSTACK_REALTIME_SIGNAL_PROCESSOR=no`
>
> Linux 或者 macOS：`export ENABLE_HAYSTACK_REALTIME_SIGNAL_PROCESSOR=no`
>
> 使用 Docker 启动则无需设置，因为会自动启动一个包含 Elasticsearch 服务的 Docker 容器。

无论采用何种方式，先克隆代码到本地：

```bash
$ git clone https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial.git
```

### Virtualenv

1. 创建虚拟环境并激活虚拟环境，具体方法可参考：[开始进入 django 开发之旅：使用虚拟环境](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/59/#%E4%BD%BF%E7%94%A8%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83)

2. 安装项目依赖

   ```bash
   $ cd HelloDjango-blog-tutorial
   $ pip install -r requirements.txt
   ```

3. 迁移数据库

   ```bash
   $ python manage.py migrate
   ```

4. 创建后台管理员账户

   ```bash
   $ python manage.py createsuperuser
   ```

   具体请参阅 [创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)。

5. 运行开发服务器

   ```bash
   $ python manage.py runserver
   ```

6. 浏览器访问 http://127.0.0.1:8000/admin，使用第 4 步创建的管理员账户登录后台发布文章，如何发布文章可参考：[创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)。

   或者执行 fake 脚本批量生成测试数据：

   ```bash
   $ python -m scripts.fake
   ```

   > 批量脚本会清除全部已有数据，包括第 4 步创建的后台管理员账户。脚本会再默认生成一个管理员账户，用户名和密码都是 admin。

9. 浏览器访问：http://127.0.0.1:8000，可进入到博客首页

### Pipenv

1. 安装 Pipenv（已安装可跳过）

    ```bash
    $ pip install pipenv
    ```

2. 安装项目依赖

    ```bash
    $ cd HelloDjango-blog-tutorial
    $ pipenv install --dev
    ```

    关于如何使用 Pipenv，参阅：[开始进入 django 开发之旅](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/59/) 的 Pipenv 创建和管理虚拟环境部分。

3. 迁移数据库

    在项目根目录运行如下命令迁移数据库：
    ```bash
    $ pipenv run python manage.py migrate
    ```

4. 创建后台管理员账户

   在项目根目录运行如下命令创建后台管理员账户
   
   ```bash
   $ pipenv run python manage.py createsuperuser
   ```

   具体请参阅 [创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)。

5. 运行开发服务器

   在项目根目录运行如下命令开启开发服务器：

   ```bash
   $ pipenv run python manage.py runserver
   ```

6. 浏览器访问 http://127.0.0.1:8000/admin，使用第 4 步创建的管理员账户登录后台发布文章，如何发布文章可参考：[创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)。

   或者执行 fake 脚本批量生成测试数据：

   ```bash
   $ pipenv run python -m scripts.fake
   ```

   > 批量脚本会清除全部已有数据，包括第 4 步创建的后台管理员账户。脚本会再默认生成一个管理员账户，用户名和密码都是 admin。

7. 在浏览器访问：http://127.0.0.1:8000/，可进入到博客首页。

### Docker

1. 安装 Docker 和 Docker Compose

3. 构建和启动容器

   ```bash
   $ docker-compose -f local.yml build
   $ docker-compose -f local.yml up
   ```

4. 创建后台管理员账户

   ```bash
   $ docker exec -it hellodjango_blog_tutorial_local python manage.py createsuperuser
   ```

   其中 hellodjango_blog_tutorial_local 为项目预定义容器名。

4. 浏览器访问 http://127.0.0.1:8000/admin，使用第 3 步创建的管理员账户登录后台发布文章，如何发布文章可参考：[创作后台开启，请开始你的表演](https://www.zmrenwu.com/courses/hellodjango-blog-tutorial/materials/65/)。

   或者执行 fake 脚本批量生成测试数据：

   ```bash
   $ docker exec -it hellodjango_blog_tutorial_local python -m scripts.fake
   ```

   >  批量脚本会清除全部已有数据，包括第 3 步创建的后台管理员账户。脚本会再默认生成一个管理员账户，用户名和密码都是 admin。

5. 为 fake 脚本生成的博客文章创建索引，这样就可以使用 Elasticsearch 服务搜索文章

   ```bash
   $ docker exec -it hellodjango_blog_tutorial_local python manage.py rebuild_index
   ```

   > 通过 admin 后台添加的文章会自动创建索引。

6. 在浏览器访问：http://127.0.0.1:8000/，可进入到博客首页。

### 线上部署

线上部署的详细文档请参考下方教程目录索引中的 **部署篇** 部分，如果不想了解细节或已了解细节，使用 Docker 仅需以下几个简单步骤就可以上线运行：

> **小贴士：**
>
> 国内服务器请设置好镜像加速，否则 Docker 构建容器的过程会非常缓慢！具体可参考 **部署篇** Docker 部署 django 中线上部署部分的内容。

1. 克隆代码到服务器

   ```bash
   $ git clone https://github.com/HelloGitHub-Team/HelloDjango-blog-tutorial.git
   ```

2. 创建环境变量文件用于存放项目敏感信息

   ```bash
   $ cd HelloDjango-blog-tutorial
   $ mkdir .envs
   $ touch .envs/.production
   ```

3. 在 .production 文件写入下面的内容并保存

   ```
   # django 用于签名和加密等功能的密钥，泄露会严重降低网站的安全性
   # 推荐使用这个工具生成：https://miniwebtool.com/django-secret-key-generator/
   DJANGO_SECRET_KEY=0p72%e@r3qr$bq%%&bxj#_bem+na2t^0(#((fom6eewrg)gyb^
   
   # 设置 django 启动时加载的配置文件
   DJANGO_SETTINGS_MODULE=blogproject.settings.production
   ```

4. 修改 Nginx 配置：复制 compose/nginx/hellodjango-blog-tutorial.conf-tmpl 到同一目录，并重命名为 hellodjango-blog-tutorial.conf，修改第 6 行的 server_name 为自己的域名（如果没有域名就改为服务器的公网 ip 地址）

5. 启动容器

   ```bash
   $ docker-compose -f production.yml up --build -d
   ```

6. 执行 docker ps 检查容器启动状况，看到如下的 3 个容器说明启动成功：

   - hellodjango_blog_tutorial_nginx
   - hellodjango_blog_tutorial_elasticsearch
   - hellodjango_blog_tutorial

7. 配置 HTTPS 证书（没有配置域名无法配置，只能通过服务器 ip 以 HTTP 协议访问）

   ```bash
   $ docker exec -it hellodjango_blog_tutorial_nginx certbot --nginx -n --agree-tos --redirect --email email@hellodjango.com -d hellodjango-blog-tutorial-demo.zmrenwu.com
   ```

   解释一下各参数的含义：

   - --nginx，使用 Nginx 插件
   - -n 非交互式，否则会弹出询问框
   - --redirect，自动配置 Nginx，将所有 http 请求都重定向到 https
   - --email xxx@xxx.com，替换为自己的 email，用于接收通知
   - -d 域名列表，开启 https 的域名，替换为自己的域名，多个域名用逗号分隔

8. 浏览器访问域名或者服务器 ip 即可进入博客首页
