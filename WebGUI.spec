%include	/usr/lib/rpm/macros.perl
Summary:	Open source content management system (CMS)
Summary(pl):	Wolnodost�pny system zarz�dzania tre�ci� (CMS)
Name:		WebGUI
Version:	5.2.5
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://files.plainblack.com/downloads/5.x.x/webgui-%{version}.tar.gz
# Source0-md5:	7b70b113fae49c462648a56c85eaae2a
URL:		http://www.plainblack.com/webgui/
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebGUI is a content management platform built to allow average
business users to build and maintain complex web sites. It is modular,
pluggable, and platform independent. It was designed to allow the
people who create the content, to manage it online, rather than
content management taking up the time of the busy IT Staff.

%description -l pl
WebGUI to platforma zarz�dzania tre�ci� stworzona, aby umo�liwi�
�redniej wielko�ci firmom tworzenie i utrzymywanie skomplikowanych
serwis�w WWW. WebGUI jest systemem modularnym, obs�uguj�cym wtyczki i
niezale�nym od platformy. Zosta� zaprojektowany tak, aby pozwoli�
ludziom tworz�cym serwisy zarz�dza� nimi z poziomu przegl�darki,
zamiast zajmowa� czas i tak ju� zaj�tym informatykom.

%prep
%setup -q -n %{name}

%{__perl} -pi -e 's|/data/WebGUI|%{_libdir}/WebGUI|' sbin/preload.perl etc/WebGUI.conf*
%{__perl} -pi -e 's|configFile\s+=\s+\"WebGUI.conf\"|configFile = \"%{_sysconfdir}/WebGUI/WebGUI.conf\"|' www/index.pl
%{__perl} -pi -e 's|webguiRoot\s*=\s*\".+?\"|webguiRoot = \"%{_libdir}/WebGUI\"|' www/index.pl
%{__perl} -pi -e "s|(\\\$session\{config\}\{webguiRoot\}\s*\.\s*'/etc/'\s*\.)||g;" \
          lib/WebGUI/Session.pm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name}/sql,%{_sysconfdir}/%{name}}

rm docs/license.txt
mv docs/upgrades $RPM_BUILD_ROOT%{_libdir}/%{name}/sql
mv docs/create.sql $RPM_BUILD_ROOT%{_libdir}/%{name}/sql

mv etc/* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
rmdir etc
cp -av . $RPM_BUILD_ROOT%{_libdir}/%{name}
rm -r $RPM_BUILD_ROOT%{_libdir}/%{name}/docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{_sysconfdir}/%{name}
%{_libdir}/%{name}
