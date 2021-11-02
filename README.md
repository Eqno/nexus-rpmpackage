# Summer2021-No.122 将Nexus引入openEuler

#### Description
https://gitee.com/openeuler-competition/summer-2021/issues/I3QONP

#### Software Architecture
`Nexus Repository Manager 3` is an open source repository manager written in Java 8.  
This is the spec file used to create the rpm packages for `Nexus Repository Manager 3` using `rpmbuild`.

#### Installation

1. Before creating rpm packages, you need to install some development tools: `yum install rpmbuild rpmdevtools`.
2. Create a temporary user to create rpm packages so that if errors occur, the builder won't break your system: `useradd -g mock -d /home/makerpm  -m makerpm`.
3. Set a password for user `makerpm` so that you can create rpm packages with it: `passwd makerpm`.
4. Log in as the `makerpm` user and use the following command to create a standard packaging workspace structure under the user directory: `rpmdev-setuptree`.
5. If not installed `rpmdevtools`, use the following command to create: `mkdir -p ~ / rpmbuild / {BUILD RPMS, SOURCES and SPECSS, SRPMS}`.
6. Change directory to the `SOURCES` folder in `rpmbuild`: `cd /home/makerpm/rpmbuild/SOURCES`.
7. Use the following command to obtain the Nexus source file: `wget https://github.com/sonatype/nexus-public/archive/refs/tags/release-3.33.1-01.tar.gz`.
8. Copy `nexus-public.spec` from this repository to the `rpmbuild /SPECS` folder you created: `cp ./nexus-public.spec /home/makerpm/rpmbuild/SPECS/`.

#### Instructions

1. Use `unzip` and `jdk 8` to make the rpm package. Run the following command to install `unzip`: `yum install unzip` and the following command to install `jdk 8`: `yum install java-1.8.0-openjdk* -y`.
2. Change directory to `SPECS` in the workspace directory for rpm packaging: `cd /home/makerpm/rpmbuild/SPECS`.
3. Run the rpmbuild command to start rpm packaging: `rpmbuild -ba nexus-public.spec`.
4. Run the following command to install `Nexus Repository Manager 3` in the `rpmbuild/RPMS/x86_64` directory: `rpm -i /home/makerpm/rpmbuild/RPMS/x86_64/*.rpm`.

#### ChangeLog
1. Failed to compile the Nexus source file using `maven`. An attempt was made to trace the cause of the test failure, and compilation was blocked as an XXE bug.
2. The compile tests failed due to environment and dependency support issues. When running the compile script, ignore the tests with the `-Dskiptests=true` parameter.
3. Write `nexus-public.service`, add Nexus as system service, and create user `nexus` to start the software, reading or writing working directory, but there is permission error when using `systemctl` to start service.
4. Start nexus with script, set its working directory read and write permission to all users, and the permission problem in the operation of Nexus has been solved.