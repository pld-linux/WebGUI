%include	/usr/lib/rpm/macros.perl
Summary:	Open source content management system (CMS)
Summary(pl.UTF-8):	Wolnodostępny system zarządzania treścią (CMS)
Name:		WebGUI
Version:	7.3.20
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/pbwebgui/webgui-%{version}-stable.tar.gz
# Source0-md5:	daa844679d2a2d9dc55a93afc15022fb
URL:		http://www.webgui.org/
BuildRequires:	rpm-perlprov >= 3.0.3-16
# BRs for autodeps:
BuildRequires:	perl-Archive-Tar >= 1.05
BuildRequires:	perl-DBI >= 1.40
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-Digest-MD5 >= 2.20
BuildRequires:	perl-HTML-Parser >= 3.36
BuildRequires:	perl-libwww
Requires:	perl-Compress-Zlib
Requires:	perl-DBD-mysql >= 3.0002
Requires:	perl-base >= 5.6
# these versions are originally included in package - require these or newer
Requires:	perl-CalendarMonthSimple >= 1.18
Requires:	perl-Convert-ASN1 >= 0.15
Requires:	perl-HTML-TagFilter >= 0.07
Requires:	perl-HTML-Template >= 2.6
Requires:	perl-HTTP-BrowserDetect >= 0.97
Requires:	perl-JSON >= 0.991
Requires:	perl-POE-Component-Client-HTTP >= 0.77
Requires:	perl-POE-Component-IKC >= 0.18
Requires:	perl-Parse-PlainConfig >= 1.1
Requires:	perl-Pod-Coverage >= 0.17
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
serwisów WWW. WebGUI jest systemem modularnym, obsługującym wtyczki i
niezależnym od platformy. Został zaprojektowany tak, aby pozwolić
ludziom tworzącym serwisy zarządzać nimi z poziomu przeglądarki,
zamiast zajmować czas i tak już zajętym informatykom.

%prep
%setup -q -n %{name}

%{__perl} -pi -e 's|/data/WebGUI|%{_libdir}/WebGUI|' sbin/preload.perl etc/WebGUI.conf*
##%{__perl} -pi -e 's|configFile\s+=\s+\"WebGUI.conf\"|configFile = \"%{_sysconfdir}/WebGUI/WebGUI.conf\"|' www/index.pl
%{__perl} -pi -e "s|(\\\$session\{config\}\{webguiRoot\}\s*\.\s*'%{_sysconfdir}/'\s*\.)||g;" \
	lib/WebGUI/Session.pm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/%{name}/sql,%{_libdir}/%{name}/lib,%{_sysconfdir}/%{name},%{perl_vendorlib}}

cp -rf docs/upgrades $RPM_BUILD_ROOT%{_libdir}/%{name}/sql
install docs/create.sql $RPM_BUILD_ROOT%{_libdir}/%{name}/sql
#gzip -9nf $RPM_BUILD_ROOT%{_libdir}/%{name}/sql{,/upgrades}/*.sql

install etc/WebGUI.conf.original $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/WebGUI.conf
install etc/spectre.conf.original $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/spectre.conf
cp -Prf sbin t www $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -Prf lib/{Spectre,WebGUI} $RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{changelog,credits.txt,gotcha.txt,install.txt,legal.txt}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/WebGUI.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/spectre.conf
%{_libdir}/%{name}
%dir %{perl_vendorlib}/WebGUI
%{perl_vendorlib}/WebGUI/*.pm
%dir %{perl_vendorlib}/WebGUI/AdSpace
%{perl_vendorlib}/WebGUI/AdSpace/*.pm
%dir %{perl_vendorlib}/WebGUI/Asset
%{perl_vendorlib}/WebGUI/Asset/*.pm
%dir %{perl_vendorlib}/WebGUI/Asset/File
%{perl_vendorlib}/WebGUI/Asset/File/*.pm
%dir %{perl_vendorlib}/WebGUI/Asset/Post
%{perl_vendorlib}/WebGUI/Asset/Post/*.pm
%dir %{perl_vendorlib}/WebGUI/Asset/Template
%{perl_vendorlib}/WebGUI/Asset/Template/*.pm
%dir %{perl_vendorlib}/WebGUI/Asset/Wobject
%{perl_vendorlib}/WebGUI/Asset/Wobject/*.pm
%dir %{perl_vendorlib}/WebGUI/Asset/Wobject/HttpProxy
%{perl_vendorlib}/WebGUI/Asset/Wobject/HttpProxy/*.pm
%dir %{perl_vendorlib}/WebGUI/Auth
%{perl_vendorlib}/WebGUI/Auth/*.pm
%dir %{perl_vendorlib}/WebGUI/Cache
%{perl_vendorlib}/WebGUI/Cache/*.pm
%dir %{perl_vendorlib}/WebGUI/Commerce
%{perl_vendorlib}/WebGUI/Commerce/*.pm
%dir %{perl_vendorlib}/WebGUI/Commerce/Item
%{perl_vendorlib}/WebGUI/Commerce/Item/*.pm
%dir %{perl_vendorlib}/WebGUI/Commerce/Payment
%{perl_vendorlib}/WebGUI/Commerce/Payment/*.pm
%dir %{perl_vendorlib}/WebGUI/Commerce/Shipping
%{perl_vendorlib}/WebGUI/Commerce/Shipping/*.pm
%dir %{perl_vendorlib}/WebGUI/Form
%{perl_vendorlib}/WebGUI/Form/*.pm
%dir %{perl_vendorlib}/WebGUI/Help
%{perl_vendorlib}/WebGUI/Help/*.pm
%dir %{perl_vendorlib}/WebGUI/i18n
%{perl_vendorlib}/WebGUI/i18n/*.pm
%dir %{perl_vendorlib}/WebGUI/i18n/English
%{perl_vendorlib}/WebGUI/i18n/English/*.pm
%dir %{perl_vendorlib}/WebGUI/Image
%{perl_vendorlib}/WebGUI/Image/*.pm
%dir %{perl_vendorlib}/WebGUI/Image/Graph
%{perl_vendorlib}/WebGUI/Image/Graph/*.pm
%dir %{perl_vendorlib}/WebGUI/Image/Graph/XYGraph
%{perl_vendorlib}/WebGUI/Image/Graph/XYGraph/*.pm
%dir %{perl_vendorlib}/WebGUI/Inbox
%{perl_vendorlib}/WebGUI/Inbox/*.pm
%dir %{perl_vendorlib}/WebGUI/Macro
%{perl_vendorlib}/WebGUI/Macro/*.pm
%dir %{perl_vendorlib}/WebGUI/Mail
%{perl_vendorlib}/WebGUI/Mail/*.pm
%dir %{perl_vendorlib}/WebGUI/Operation
%{perl_vendorlib}/WebGUI/Operation/*.pm
%dir %{perl_vendorlib}/WebGUI/Search
%{perl_vendorlib}/WebGUI/Search/*.pm
%dir %{perl_vendorlib}/WebGUI/Session
%{perl_vendorlib}/WebGUI/Session/*.pm
%dir %{perl_vendorlib}/WebGUI/SQL
%{perl_vendorlib}/WebGUI/SQL/*.pm
%dir %{perl_vendorlib}/Spectre
%{perl_vendorlib}/Spectre/*.pm
%dir %{perl_vendorlib}/WebGUI/Storage
%{perl_vendorlib}/WebGUI/Storage/*.pm
%dir %{perl_vendorlib}/WebGUI/Workflow
%{perl_vendorlib}/WebGUI/Workflow/*.pm
%dir %{perl_vendorlib}/WebGUI/Workflow/Activity
%{perl_vendorlib}/WebGUI/Workflow/Activity/*.pm
