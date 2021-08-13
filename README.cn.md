# Summer2021-No.122 将Nexus引入openEuler

#### 介绍
https://gitee.com/openeuler-competition/summer-2021/issues/I3QONP

#### 软件架构
Nexus Repository Manager 3 由 Java 语言编写而成，是一款开源仓库管理软件。  
此为使用 rpmbuild 制作 Nexus Repository Manager 3 的 rpm 包所用 spec 文件。

#### 安装教程

1.  安装使用 rpmbuild 以及 rpmdevtools。使用如下命令安装依赖：`yum install rpmbuild rpmdevtools `。
2.  在 /home 下创建 rpm 打包工作目录。使用 rpmdevtools 创建：`rpmdev-setuptree`；若未安装 rpmdevtools，使用如下命令创建：`mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECSS,SRPMS}`。
3.  将 nexus.spec 文件复制到创建好的 rpmbuild/SPECS 文件夹下：`cp ./nexus.spec ~/rpmbuild/SPECS/`。

#### 使用说明

1.  rpm 打包使用 git、unzip 以及 jdk8。使用如下命令安装 git、unzip：`yum install git unzip`，使用如下命令安装 jdk8：`yum install java-1.8.0-openjdk* -y`。
2.  进入 rpm 打包工作目录下的 SPECS 文件夹：`cd ~/rpmbuild/SPECS`。
3.  执行 rpmbuild 命令开始进行 rpm 打包：`rpmbuild -ba nexus.spec`。
4.  制作完成的 rpm 包将在 rpmbuild/RPMS/x86_64 目录下，使用如下命令即可安装 Nexus Repository Manager 3：`rpm -i ~/rpmbuild/RPMS/x86_64/*.rpm`。
