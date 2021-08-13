Name:		nexus
Version:	3.33.0
Release:	01

Source0:	nexus-public

Prefix:		/usr/local/nexus
Requires(post):	git unzip java-1.8.0-openjdk
License:	GPL v3
URL:		https://github.com/sonatype/nexus-public.git
Summary:	Nexus Repository Manager from Sonatype
Packager:	Eqnoxx

%description
The "Nexus Repository Manager" program.

%prep
rm -rf %{_sourcedir}/nexus-public
rm -rf ./*
git clone %{URL} $RPM_SOURCE_DIR/nexus-public

%define VER   		%{version}-%{release}
%define MAIN 		nexus-%{VER}
%define BRANCH		release-%{VER}
%define SKIPTEST	-DskipTests=true
%define BUILDVERSION	-Dbuild.version=1
%define GITDIR		$RPM_BUILD_DIR/nexus-public
%define RELEASEDIR	$RPM_BUILD_DIR/nexus-release
%define SETGITENV	--git-dir=%{GITDIR}/.git --work-tree=%{GITDIR}
%define BASEDIR		nexus-base-template
%build
cp -r $RPM_SOURCE_DIR/* $RPM_BUILD_DIR
git %{SETGITENV} fetch --tags
git %{SETGITENV} checkout -b %{BRANCH} origin/%{BRANCH} --
cd %{GITDIR} && %{GITDIR}/mvnw clean install %{SKIPTEST} %{BUILDVERSION}
unzip %{GITDIR}/assemblies/%{BASEDIR}/target/%{BASEDIR}-%{VER}.zip -d %{RELEASEDIR}
mv %{RELEASEDIR}/%{BASEDIR}-%{VER} %{RELEASEDIR}/%{MAIN}
echo -e '#!/bin/sh\nsudo -u nexus /usr/local/nexus/%{MAIN}/bin/nexus' > $RPM_BUILD_DIR/'nexus'

%define ROOT_APP $RPM_BUILD_ROOT/%{prefix}
%define ROOT_BIN $RPM_BUILD_ROOT/%{_bindir}
%install
mkdir -p %{ROOT_APP}/sonatype-work
cp -r %{RELEASEDIR}/%{MAIN} %{ROOT_APP}
mkdir -p %{ROOT_BIN}
cp $RPM_BUILD_DIR/nexus %{ROOT_BIN}

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
%attr(0755,%{_user},%{_group}) %{_bindir}/nexus
%doc %{prefix}/%{MAIN}/NOTICE.txt
%license %{prefix}/%{MAIN}/OSS-LICENSE.txt
%{prefix}/%{MAIN}/bin/
%{prefix}/%{MAIN}/deploy/
%{prefix}/%{MAIN}/etc/
%{prefix}/%{MAIN}/lib/
%{prefix}/%{MAIN}/public/
%{prefix}/%{MAIN}/system/

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/*
rm -rf $RPM_SOURCE_DIR/*

%changelog
* Thu Aug 05 2021 Eqnoxx <Eqnoxx@163.com> 3.33.0-01
- Initial RPM release
