# Summer2021-No.122 将Nexus引入openEuler

#### Description
https://gitee.com/openeuler-competition/summer-2021/issues/I3QONP

#### Software Architecture
`Nexus Repository Manager 3` is an open source repository manager written in Java 8.  
This is the spec file used to create the rpm package for `Nexus Repository Manager 3` using `rpmbuild`.

#### Installation

1.  Installations use `rpmbuild` and `rpmdevtools`. Run the following command to get dependencies: `yum install rpmbuild rpmDevtools`.
2.  Create a workspace directory for rpm packaging in `/home`. Use `rpmDevTools` to create: `rpmdev-setuptree`; If not installed `rpmdevtools`, use the following command to create: `mkdir -p ~ / rpmbuild / {BUILD RPMS, SOURCES and SPECSS, SRPMS}`.
3.  Copy the file `nexus.spec` to the directory created with `cp ./nexus.spec ~/rpmbuild/SPECS/`.

#### Instructions

1.  Use `git`, `unzip` and `jdk 8` to make the rpm package. Run the following command to install `git` and `unzip`: `yum install git unzip` and the following command to install `jdk 8`: `yum install java-1.8.0-openjdk* -y`.
2.  Change directory to `SPEC` in the workspace directory for rpm packaging:  `cd ~/rpmbuild/SPECS`.
3.  Run the rpmbuild command to start rpm packaging: `rpmbuild -ba nexus.spec`.
4. Run the following command to install `Nexus Repository Manager 3` in the `rpmbuild/RPMS/x86_64` directory: `rpm -i ~/rpmbuild/RPMS/x86_64/*.rpm`.

