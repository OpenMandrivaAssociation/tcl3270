Summary:	Tcl-based scripted 3270 Emulator
Name:		tcl3270
Version:	3.3.9ga12
Release:	4
License:	MIT
Group:		Terminals
URL:		http://x3270.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/x3270/x3270/%version/suite3270-%version.tgz
Requires:	x3270 <= %{version}
BuildRequires:	openssl-devel
Requires:	tcl
BuildRequires:	tcl-devel
BuildRoot:	%{_tmppath}/%{name}-%{pversion}-root

%description
Complete IBM 3278/3279 emulation, TN3270E support, structured
fields, color xterm emulation, highly configurable

%prep
%setup -q -n %{name}-3.3

%build

%configure2_5x \
    --with-tcl=8.6

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m755 %{name} %{buildroot}%{_bindir}/
install -m644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc html/*.html README
%doc Examples/cms_cmd.tcl3270
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.9ga12-3mdv2011.0
+ Revision: 615166
- the mass rebuild of 2010.1 packages

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 3.3.9ga12-2mdv2010.1
+ Revision: 533638
- rebuild

* Wed Aug 12 2009 Funda Wang <fwang@mandriva.org> 3.3.9ga12-1mdv2010.0
+ Revision: 415339
- new version 3.3.9ga12

* Sat Dec 06 2008 Adam Williamson <awilliamson@mandriva.org> 3.3.8p1-1mdv2009.1
+ Revision: 310983
- rebuild for new tcl
- update docs list
- update build for tcl 8.6
- update to 3.3.8p1

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 3.3.6-4mdv2009.0
+ Revision: 242856
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 3.3.6-2mdv2008.0
+ Revision: 82055
- rebuild for new soname of tcl

* Wed Jun 27 2007 Funda Wang <fwang@mandriva.org> 3.3.6-1mdv2008.0
+ Revision: 45021
- Build against tcl 8.5
- New version
- Import tcl3270



* Mon Jan 02 2006 Oden Eriksson <oeriksson@mandriva.com> 3.3.4p3-3mdk
- rebuilt against soname aware deps (tcl/tk)
- fix deps

* Wed Nov 30 2005 Oden Eriksson <oeriksson@mandriva.com> 3.3.4p3-2mdk
- rebuilt against openssl-0.9.8a

* Thu Jul 07 2005 Lenny Cartier <lenny@mandriva.com> 3.3.4p3-1mdk
- 3.3.4p3

* Tue Jun 08 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 3.3.2p1-1mdk
- new version
- fix strange perms
- fix deps

* Fri Jul 11 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.20-1mdk
- 3.2.20
- use the %%configure2_5x macro
- fix buildrequires

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.2.19-3mdk
- rebuild

* Mon Jan 27 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.19-2mdk
- build release
- misc spec file fixes

* Thu May 16 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.19-1mdk
- new version
- misc spec file fixes
- rebuilt with latest system compiler (gcc3.1)

* Tue Jan  1 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.18-1mdk
- new version

* Mon Sep 24 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.2.17-1mdk
- added by Oden Eriksson <oden.eriksson@kvikkjokk.net> :
	- initial cooker contrib
