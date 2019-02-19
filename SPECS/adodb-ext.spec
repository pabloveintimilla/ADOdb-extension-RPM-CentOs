%define build_php4 0
%{?_with_php4: %global build_php4 1}

%define modname		adodb-ext
%if %build_php4
%define name		php4-%{modname}
%else
%define name		php-%{modname}
%endif
%define version		5.0.4
%define src_version	504
%define soname		%{modname}.so
%define inifile		%{modname}.ini
%if %build_php4
%define php_version	%(php4 -r 'echo substr(PHP_VERSION,0,3);')
%else
%define php_version	%(php -r 'echo substr(PHP_VERSION,0,3);')
%endif

Name:		%{name}
Version:	%{version}
Release:	1%{?dist}
Epoch:		1
Summary:	ADOdb extension for PHP
Group:		Development/Libraries
License:	BSD
%if "%{php_version}" == "5.3"
URL:		https://github.com/pabloveintimilla/ADOdb-extension-RPM-CentOs/
Source0: https://github.com/pabloveintimilla/ADOdb-extension-RPM-CentOs/blob/master/SOURCES/%{modname}-php5.3-%{src_version}.zip?raw=true
%else
URL:		http://phplens.com/
Source0:	http://phplens.com/lens/dl/%{modname}-%{src_version}.zip
%endif
Source1:	%{name}.ini.bz2
Requires:	php
%if %build_php4
BuildRequires:	php4-devel
%else
BuildRequires:	php-devel >= 5.0.4
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The ADOdb PHP extension provides up to 100% speedup 
by replacing parts of ADOdb with C code. 
ADOdb will auto-detect if this extension is installed 
and use it automatically. This extension is compatible 
with ADOdb 3.32 or later, and PHP 4.3 - 5.x.x. 

%prep
%setup -q -n adodb-%{src_version}

%build
# x86_64 fix
export CFLAGS="%{optflags} -fPIC"

%if %build_php4
php4ize
%else
phpize
%endif
%configure 
make

%check
make test

%install
mv modules/*.so %{modname}.so
rm -rf %{buildroot}

%if %build_php4
install -d %{buildroot}%{_libdir}/php4/modules
install -d %{buildroot}%{_sysconfdir}/php4.d
bzcat %{SOURCE1} > %{buildroot}%{_sysconfdir}/php4.d/%{inifile}
install -m 755 %{soname} %{buildroot}%{_libdir}/php4/modules/
%else
install -d %{buildroot}%{_libdir}/php/modules
install -d %{buildroot}%{_sysconfdir}/php.d
bzcat %{SOURCE1} > %{buildroot}%{_sysconfdir}/php.d/%{inifile}
install -m 755 %{soname} %{buildroot}%{_libdir}/php/modules/
%endif

cat > README.%{modname} << EOF
The %{name} package contains a dynamic shared object (DSO) for PHP. 
EOF


%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS test-adodb.php README*
%if %build_php4
%config(noreplace) %{_sysconfdir}/php4.d/%{inifile}
%{_libdir}/php4/modules/%{soname}
%else
%config(noreplace) %{_sysconfdir}/php.d/%{inifile}
%{_libdir}/php/modules/%{soname}
%endif

%changelog
* Sat Nov 19 2011 Pablo Veintimilla <pabloveintimilla@gmail.com> 1:5.0.4-1.el6 
- Upgrade adodb library, and port to centOS 6. This use a especial source of adodb to suport php 5.3

* Fri Jul 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1:5.0.2-4mdk 
- use only one spec file for both php versions

* Wed Jun 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1:5.0.2-3mdk  
- obsoletes php-adodb <= 5.0.4_5.0.2-1mdk
- epoch should be 1

* Wed Jun 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0:5.0.2-2mdk 
- renamed to % {name}, without obsoleting old name as it is now used by standard adodb module 
- switch to a saner versioning scheme
- introduce epoch
- use perl instead of dos2unix for fixing encoding
- enforce php build version dependency
- change group to Development/Other

* Thu Jun 16 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4_5.0.2-1mdk
- added for php 5.x too

* Thu Jun 16 2005 Oden Eriksson <oeriksson@mandriva.com> 4.4.0_5.0.2-0.RC1.1mdk
- 5.0.2
- fix url and deps
- strip away annoying ^M

* Tue Jun 14 2005 Oden Eriksson <oeriksson@mandriva.com> 4.4.0_3.3.2-0.RC1.1mdk
- rebuilt for php-4.4.0RC1

* Thu Jun 02 2005 Oden Eriksson <oeriksson@mandriva.com> 4.3.11_3.3.2-1mdk
- renamed to php4-*

* Wed May 11 2005 Oden Eriksson <oeriksson@mandriva.com> 4.3.11_3.3.2-2mdk
- fix deps

* Sat Apr 16 2005 Oden Eriksson <oeriksson@mandriva.com> 4.3.11_3.3.2-1mdk
- 4.3.11

* Mon Mar 21 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10_3.3.2-5mdk
- use the %%mkrel macro

* Sat Feb 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10_3.3.2-4mdk
- rebuilt against a non hardened-php aware php lib

* Sat Jan 15 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10_3.3.2-3mdk
- rebuild due to hardened-php-0.2.6
- cleanups

* Tue Jan 04 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10_3.3.2-2mdk
- added one x86_64 fix

* Thu Dec 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.10_3.3.2-1mdk
- rebuild for php 4.3.10

* Fri Oct 01 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.9_3.3.2-1mdk
- rebuild for php 4.3.9

* Wed Jul 14 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.8_3.3.2-1mdk
- rebuilt for php-4.3.8

* Mon Jul 12 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7_3.3.2-2mdk
- remove redundant provides

* Mon Jun 14 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7_3.3.2-1mdk
- rebuilt for php-4.3.7

* Sun May 23 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6_3.3.2-2mdk
- use the %%configure2_5x macro
- move scandir to /etc/php4.d

* Wed May 05 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6_3.3.2-1mdk
- built for php 4.3.6

* Wed Nov 05 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 4.3.4_3.3.2-1mdk
- built for php 4.3.4

* Wed Aug 27 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 4.3.3_3.3.2-1mdk
- built for php 4.3.3
- misc spec file fixes

* Tue Jun 03 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 4.3.2_0.3.3.2-1mdk
- built for 4.3.2

* Sun May 25 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 4.3.1_3.3.2-1mdk
- initial cooker contrib

