%include	/usr/lib/rpm/macros.perl
Summary:	Open source content management system (CMS)
Name:		WebGUI
Version:	5.1.2
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
URL:		http://www.plainblack.com/webgui
Source0:	http://files.plainblack.com/downloads/5.x.x/webgui-%{version}.tar.gz
Patch0:		%{name}-etc.patch
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

%prep
%setup -q -n %{name}
%patch0 -p0

%{__perl} -pi -e 's|/data/WebGUI|%{_libdir}/WebGUI|' sbin/preload.perl etc/WebGUI.conf*
%{__perl} -pi -e 's|configFile\s+=\s+\"WebGUI.conf\"|configFile = \"%{_sysconfdir}/WebGUI/WebGUI.conf\"|' www/index.pl
%{__perl} -pi -e 's|webguiRoot\s*=\s*\".+?\"|webguiRoot = \"%{_libdir}/WebGUI\"|' www/index.pl

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/sql
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

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
