Name:		nexus
Version:	3.30.1
Release:	01
%define system	unix

%define MAIN 	%{name}-%{version}-%{release}
%define NEXUS	%{MAIN}-%{system}.tar.gz 
%define STRUP	%{name}
Source0:	%{NEXUS}
Source1:	%{STRUP}

Prefix:		/usr/local/%{name}
Requires(post):	java-1.8.0-openjdk
License:	GPL v3
URL:		https://help.sonatype.com/repomanager3
Summary:	Nexus Repository Manager from Sonatype
Packager:	Eqnoxx

%description
The "Nexus Repository Manager" program.

%prep
tar xvf %{_sourcedir}/%{NEXUS}
cp %{_sourcedir}/%{STRUP} ./

%build

%define ROOT_APP $RPM_BUILD_ROOT/%{prefix}
%define ROOT_BIN $RPM_BUILD_ROOT/%{_bindir}
%install
mkdir -p %{ROOT_APP}/sonatype-work
cp -r ./%{MAIN} %{ROOT_APP}
mkdir -p %{ROOT_BIN}
cp ./%{name} %{ROOT_BIN}

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
%attr(0755,%{_user},%{_group}) %{_bindir}/%{name}
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
* Tue Jun 08 2021 Eqnoxx <Eqnoxx@163.com> 3.30.1-01
- Initial RPM release
