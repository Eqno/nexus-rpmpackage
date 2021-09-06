Summary:	A repository manager from Sonatype
Name:		nexus-public
Version:	3.33.1
%define RLS	01
Release:	1%{?dist}
License:	EPLv1.0
Source:		https://github.com/sonatype/%{name}/archive/refs/tags/release-%{version}-%{RLS}.tar.gz
URL:		https://github.com/sonatype/nexus-public
Prefix:		/usr/local/nexus
BuildRequires:	java-1.8.0-openjdk, unzip
Requires:	java-1.8.0-openjdk

%define APPDIR		%{prefix}/%{name}
%define GITDIR		%{name}-release-%{version}-%{RLS}
%define SKIPTEST        -DskipTests=true
%define BUILDVERSION    -Dbuild.version=1

%description
The open source release of Sonatype Nexus Repository Manager.

%prep
%autosetup -n %{GITDIR}

%build
./mvnw clean install %{SKIPTEST} %{BUILDVERSION}

%install
unzip -o ./assemblies/nexus-base-template/target/nexus-base-template-%{version}-%{RLS}.zip -d ../%{name}
mkdir -p %{buildroot}/%{prefix}/sonatype-work
mkdir -p %{buildroot}/%{_bindir}
cp -r ../%{name}/nexus-base-template-%{version}-%{RLS} %{buildroot}/%{APPDIR}
echo -e '#!/bin/sh\n/usr/local/nexus/nexus-public/bin/nexus $0' > %{buildroot}/%{_bindir}/nexus

%files
%defattr(-,root,root,-)
%attr(0777,root,root) /%{_bindir}/nexus
%attr(0777,root,root) /%{prefix}/sonatype-work/
%doc /%{APPDIR}/NOTICE.txt
%license /%{APPDIR}/OSS-LICENSE.txt
/%{APPDIR}/bin/
/%{APPDIR}/deploy/
/%{APPDIR}/etc/
/%{APPDIR}/lib/
/%{APPDIR}/public/
/%{APPDIR}/system/

%postun
rm -r %{prefix}

%clean

%changelog
* Sat Sep 04 2021 Eqnoxx <Eqnoxx@163.com> 3.33.1-01
- Second Packaging
* Thu Aug 05 2021 Eqnoxx <Eqnoxx@163.com> 3.33.0-01
- First Packaging
