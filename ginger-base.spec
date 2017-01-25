Name:		ginger-base
Version:	2.2.2
Release:	0%{?dist}
Summary:	Wok plugin for base host management
BuildRoot:	%{_topdir}/BUILD/%{name}-%{version}-%{release}
BuildArch:	noarch
Group:		System Environment/Base
License:	LGPL/ASL2
Source0:	gingerbase-%{version}.tar.gz
Patch1: 	gingerbase-2.2.2-no-software-updates.patch
Requires:	wok >= 2.1.0
Requires:	pyparted
Requires:	python-cherrypy
Requires:	python-configobj
Requires:	python-lxml
Requires:	python-psutil >= 0.6.0
Requires:	rpm-python
Requires:	gettext
Requires:	git
Requires:	sos
BuildRequires:	gettext-devel
BuildRequires:	libxslt
BuildRequires:	python-lxml

%if 0%{?fedora} >= 23
Requires:	python2-dnf
%endif

%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%global with_systemd 1
%endif

%if 0%{?rhel} == 6
Requires:	python-ordereddict
BuildRequires:	python-unittest2
%endif

%description
Ginger Base is an open source base host management plugin for Wok
(Webserver Originated from Kimchi), that provides an intuitive web panel with
common tools for configuring and managing the Linux systems.

%prep
%setup -q -n gingerbase-%{version}
%patch1 -p1 -b .no_software_updates

%build
./autogen.sh --system
%configure
make


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root)
%{python_sitelib}/wok/plugins/gingerbase
%{_datadir}/gingerbase
%{_prefix}/share/locale/*/LC_MESSAGES/gingerbase.mo
%{_datadir}/wok/plugins/gingerbase
%{_datadir}/wok/plugins/gingerbase/ui/pages/tabs/host-dashboard.html.tmpl
%{_datadir}/wok/plugins/gingerbase/ui/pages/tabs/host-update.html.tmpl
%{_sysconfdir}/wok/plugins.d/gingerbase.conf
%{_sharedstatedir}/gingerbase/


%changelog
* Tue Jan 24 2017 eGloo <developer@egloo.ca> 2.2.2
- First build

* Wed Mar 23 2016 Daniel Henrique Barboza <dhbarboza82@gmail.com>
- Added wok version restriction >= 2.1.0

* Tue Aug 25 2015 Chandra Shehkhar Reddy Potula <chandra@linux.vnet.ibm.com> 0.0-1
- First build
