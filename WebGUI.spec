%include	/usr/lib/rpm/macros.perl
Summary:	Open source content management system (CMS)
Summary(pl.UTF-8):	Wolnodostępny system zarządzania treścią (CMS)
Name:		WebGUI
Version:	7.3.19
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/pbwebgui/webgui-%{version}-stable.tar.gz
# Source0-md5:	bd92a165858778f3a37d8554baa2eb9e
URL:		http://www.webgui.org/
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
%define		_noautoreq	'perl(Authen::Smb)' 'perl(WebGUI::AssetBranch' 'perl(WebGUI::AssetClipboard)' 'perl(WebGUI::AssetExportHtml)' 'perl(WebGUI::AssetLineage)' 'perl(WebGUI::AssetMetaData)' 'perl(WebGUI::AssetPackage)' 'perl(WebGUI::AssetTrash)' 'perl(WebGUI::AssetVersioning)'

%description
WebGUI is a content management platform built to allow average
business users to build and maintain complex web sites. It is modular,
pluggable, and platform independent. It was designed to allow the
people who create the content, to manage it online, rather than
content management taking up the time of the busy IT Staff.

%description -l pl.UTF-8
WebGUI to platforma zarządzania treścią stworzona, aby umożliwić
średniej wielkości firmom tworzenie i utrzymywanie skomplikowanych
serwisów WWW. WebGUI jest systemem modularnym, obsługującym wtyczki
i niezależnym od platformy. Został zaprojektowany tak, aby pozwolić
ludziom tworzącym serwisy zarządzać nimi z poziomu przeglądarki,
zamiast zajmować czas i tak już zajętym informatykom.

%prep
%setup -q -n %{name}

%{__perl} -pi -e 's|/data/WebGUI|%{_libdir}/WebGUI|' sbin/preload.perl etc/WebGUI.conf*
##%{__perl} -pi -e 's|configFile\s+=\s+\"WebGUI.conf\"|configFile = \"%{_sysconfdir}/WebGUI/WebGUI.conf\"|' www/index.pl
##%{__perl} -pi -e 's|webguiRoot\s*=\s*\".+?\"|webguiRoot = \"%{_libdir}/WebGUI\"|' www/index.pl
%{__perl} -pi -e "s|(\\\$session\{config\}\{webguiRoot\}\s*\.\s*'%{_sysconfdir}/'\s*\.)||g;" \
	lib/WebGUI/Session.pm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name}/sql,%{_sysconfdir}/%{name}}

cp -rf docs/upgrades $RPM_BUILD_ROOT%{_libdir}/%{name}/sql
install docs/create.sql $RPM_BUILD_ROOT%{_libdir}/%{name}/sql
#gzip -9nf $RPM_BUILD_ROOT%{_libdir}/%{name}/sql{,/upgrades}/*.sql

install etc/WebGUI.conf.original $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/WebGUI.conf
cp -Prf lib/WebGUI* sbin www $RPM_BUILD_ROOT%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{changelog,credits.txt,gotcha.txt,install.txt,legal.txt}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/WebGUI.conf
%{_libdir}/%{name}
