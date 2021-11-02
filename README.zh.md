# Summer2021-No.122 将Nexus引入openEuler

#### 介绍
https://gitee.com/openeuler-competition/summer-2021/issues/I3QONP

#### 软件架构
Nexus Repository Manager 3 由 Java 语言编写而成，是一款开源仓库管理软件。  
此为使用 rpmbuild 制作 Nexus Repository Manager 3 的 rpm 包所用 spec 文件。

#### 安装教程

1. 在创建 rpm 包之前，您需要安装一些开发工具：`yum install rpmbuild rpmdevtools`。
2. 新建一个临时用户以便创建 RPM 包，使得如果有错误发生，构建程序不会破坏您的系统：`useradd -g mock -d /home/makerpm  -m makerpm`。
3. 为 makerpm 用户设置密码，以便登录 makerpm 用户进行 rpm 包的创建：`passwd makerpm`。
4. 以 makerpm 用户登录，使用以下命令在用户目录下，创建标准的打包工作目录结构：`rpmdev-setuptree`。
5. 若您未安装 rpmdevtools，使用如下命令创建 rpm 打包工作目录：`mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECSS,SRPMS}`。
6. 进入 rpmbuild 目录下的 SOURCES 文件夹：`cd /home/makerpm/rpmbuild/SOURCES`。
7. 使用如下命令获取 nexus 源码文件：`wget https://github.com/sonatype/nexus-public/archive/refs/tags/release-3.33.1-01.tar.gz`。
8. 将本仓库中的 nexus-public.spec 文件复制到创建好的 rpmbuild/SPECS 文件夹下：`cp ./nexus-public.spec /home/makerpm/rpmbuild/SPECS/`。

#### 使用说明

1. rpm 打包使用 unzip 以及 jdk8。使用如下命令安装 unzip：`yum install unzip`，使用如下命令安装 jdk8：`yum install java-1.8.0-openjdk* -y`。
2. 进入 rpm 打包工作目录下的 SPECS 文件夹：`cd /home/makerpm/rpmbuild/SPECS`。
3. 执行 rpmbuild 命令开始进行 rpm 打包：`rpmbuild -ba nexus-public.spec`。
4. 制作完成的 rpm 包将在 rpmbuild/RPMS/x86_64 目录下，使用如下命令即可安装 Nexus Repository Manager 3：`rpm -i /home/makerpm/rpmbuild/RPMS/x86_64/*.rpm`。

#### 更改记录
1. 使用 maven 编译 nexus 源码文件，提示 `test failures`，编译失败。尝试追踪测试失败原因，发现编译被作为 xxe 漏洞阻止。
2. 由于环境与依赖支持问题，编译测试不能通过，运行编译脚本时，使用 `-DskipTests=true` 参数忽略测试即可。
3. 编写 nexus-public.service，将 nexus 添加为系统服务，并创建 nexus 用户以启动软件和读写工作目录，但在使用 systemctl 启动服务时出现权限错误。
4. 以脚本启动 nexus 软件，将其工作目录读写权限设为所有用户，解决 nexus 运行中的权限问题。