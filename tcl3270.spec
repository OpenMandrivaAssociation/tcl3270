Summary:	Tcl-based scripted 3270 Emulator
Name:		tcl3270
Version:	3.3.6
Release:	%mkrel 1
License:	GPL
Group:		Terminals
URL:		http://www.geocities.com/SiliconValley/Peaks/7814/
Source0:	tcl3270-%{version}.tgz
Requires:	x3270 =< %{version}
BuildRequires:	openssl-devel
Requires:	tcl
BuildRequires:	X11-devel
BuildRequires:	tcl tcl-devel
#BuildRequires:	tclx
BuildRoot:	%{_tmppath}/%{name}-%{pversion}-root

%description
Complete IBM 3278/3279 emulation, TN3270E support, structured
fields, color xterm emulation, highly configurable

%prep

%setup -q -n %{name}-3.3

# fix strange perms
find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

perl -p -i -e "s|/usr/local|/usr|g" configure

%build

%configure2_5x \
    --with-tcl=8.4

#    --with-tclx=8.3

%make %{name}

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
%doc html/Build.html html/FAQ.html html/Intro.html html/Lineage.html
%doc html/New.html html/README.html html/tcl3270-man.html README
%doc Examples/cms_cmd.tcl3270
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
