Summary:	Tcl-based scripted 3270 Emulator
Name:		tcl3270
Version:	3.3.9ga12
Release:	%mkrel 3
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
