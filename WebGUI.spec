%include	/usr/lib/rpm/macros.perl
Summary:	Open source content management system (CMS)
Summary(pl):	Wolnodost�pny system zarz�dzania tre�ci� (CMS)
Name:		WebGUI
Version:	5.5.8
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://files.plainblack.com/downloads/5.x.x/webgui-%{version}.tar.gz
# Source0-md5:	5869ec579ea7743a44a4429fd9b7e5ed
URL:		http://www.plainblack.com/webgui/
BuildRequires:	rpm-perlprov >= 3.0.3-16
# BRs for autodeps:
BuildRequires:	perl-Archive-Tar
BuildRequires:	perl-DBI
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-libwww
Requires:	perl-Compress-Zlib
Requires:	perl-DBD-mysql
Requires:	perl-base >= 5.6
# these versions are originally included in package - require these or newer
Requires:	perl-CalendarMonthSimple >= 1.18
Requires:	perl-Convert-ASN1 >= 0.15
Requires:	perl-HTML-TagFilter >= 0.07
Requires:	perl-HTML-Template >= 2.6
Requires:	perl-HTTP-BrowserDetect >= 0.97
Requires:	perl-Parse-PlainConfig >= 1.1
Requires:	perl-Tie-CPHash >= 1.001
Requires:	perl-Tie-IxHash >= 1.21
Requires:	perl-Tree-DAG_Node >= 1.04
Requires:	perl-XML-RSSLite >= 0.11
Requires:	perl-ldap >= 0.25
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional
%define		_noautoreq	'perl(Authen::Smb)'

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

cp -rf docs/upgrades $RPM_BUILD_ROOT%{_libdir}/%{name}/sql
install docs/create.sql $RPM_BUILD_ROOT%{_libdir}/%{name}/sql
gzip -9nf $RPM_BUILD_ROOT%{_libdir}/%{name}/sql{,/upgrades}/*.sql

install etc/WebGUI.conf.original $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/WebGUI.conf
cp -Prf lib/{Data,WebGUI*} sbin www $RPM_BUILD_ROOT%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{changelog,credits.txt,gotcha.txt,install.txt,legal.txt}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/WebGUI.conf
%{_libdir}/%{name}
