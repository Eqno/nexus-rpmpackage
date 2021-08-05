Name:		nexus

Version:	3.33.0
Release:	01
%define VER     %{version}-%{release}

%define MAIN 	nexus-%{VER}
%define PKG	nexus-public 
%define STRUP	nexus
Source0:	%{PKG}
Source1:	%{STRUP}

Prefix:		/usr/local/nexus
Requires(post):	git unzip java-1.8.0-openjdk
License:	GPL v3
URL:		https://github.com/sonatype/nexus-public.git
Summary:	Nexus Repository Manager from Sonatype
Packager:	Eqnoxx

%description
The "Nexus Repository Manager" program.

%prep
rm -rf %{_sourcedir}/%{PKG}
rm -rf ./*
proxychains4 git clone %{URL} $RPM_SOURCE_DIR/%{PKG}

%define BRANCH release-%{VER}
%define SKIPTEST true
%define BUILDVERSION 1
%build
cp -r $RPM_SOURCE_DIR/* $RPM_BUILD_DIR
cd $RPM_BUILD_DIR/%{PKG}
proxychains4 git fetch --tags
git checkout -b %{BRANCH} origin/%{BRANCH} --
proxychains4 $RPM_BUILD_DIR/mvnw clean install -DskipTests=%{SKIPTEST} -Dbuild.revision=%{BUILDVERSION}
unzip $RPM_BUILD_DIR/assemblies/nexus-base-template/target/nexus-base-template-%{VER}.zip -d $RPM_BUILD_DIR/nexus-release
mv $RPM_BUILD_DIR/nexus-release/nexus-base-template-%{VER} $RPM_BUILD_DIR/nexus-release/%{MAIN}

%define ROOT_APP $RPM_BUILD_ROOT/%{prefix}
%define ROOT_BIN $RPM_BUILD_ROOT/%{_bindir}
%install
mkdir -p %{ROOT_APP}/sonatype-work
cp -r $RPM_BUILD_DIR/nexus-release/%{MAIN} %{ROOT_APP}
mkdir -p %{ROOT_BIN}
cp $RPM_BUILD_DIR/%{STRUP} %{ROOT_BIN}

%define _user nexus
%define _user_uid 114514
%define _group nexus
%define _group_id 114514
%pre
grep -q ^%{_group}: /etc/group || groupadd -g %{_group_id} %{_group}
grep -q ^%{_user}: /etc/passwd || useradd -g %{_group} -u %{_user_uid} -d %{_prefix} -s /sbin/nologin -M %{_user}

%files
%defattr(-,root,root,-)
%attr(0755,%{_user},%{_group}) /%{prefix}/sonatype-work/
%attr(0755,%{_user},%{_group}) %{_bindir}/%{STRUP}
%doc %{prefix}/%{MAIN}/NOTICE.txt
%license %{prefix}/%{MAIN}/OSS-LICENSE.txt
%license %{prefix}/%{MAIN}/PRO-LICENSE.txt
%{prefix}/%{MAIN}/bin/
%{prefix}/%{MAIN}/deploy/
%{prefix}/%{MAIN}/etc/
%{prefix}/%{MAIN}/lib/
%{prefix}/%{MAIN}/public/
%{prefix}/%{MAIN}/system/
%{prefix}/%{MAIN}/.install4j/

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Aug 05 2021 Eqnoxx <Eqnoxx@163.com> 3.33.0-01
- Initial RPM release
