# $Revision: 1.2 $ $Date: 1999-09-19 10:52:56 $
Summary:	Utility for converting text between multiple character sets.
Summary(pl):	Uniwersjalny konwerter zestaw�w znak�w.
Name:		recode
Version:	3.5
Release:	1
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narz�dzia/Tekst
Source:		http://www.iro.umontreal.ca/contrib/recode/recode-%{version}.tar.gz
Buildroot:	/tmp/%{name}-%{version}-root

%description
Free  `recode'  converts  files  between various character sets and surfaces.
It supports more than 200 different character sets and surfaces, including
well known ISO-8859, CP-XXXX and Unicode.

%description -l pl
Program `recode' konwertuje zestawy znak�w oraz kodowanie w plikach tekstowych.
Obs�uguje ponad 200 r�nych zestaw�w znak�w oraz sposob�w kodowania,
w�acznie z popularnymi ISO-8859, CP-XXXX oraz Unicode.

%package devel
Summary:	Library for converting text between multiple character sets.
Summary(pl):	Uniwersalna biblioteka do konwersja zestaw�w znak�w.
Group:		Development/Tools
Group(pl):	Programowanie/Narz�dzia
Prereq:		/usr/sbin/fix-info-dir
Requires:	m4
Requires:	automake
Requires:	autoconf
Requires:	%{name} = %{version}

%description devel
The recode library allows including recode functionality in your own
programs.

%description -l pl
Bibliotek recode pozwala na dodanie wszystkich funkcji programu recode
do program�w u�ytkownika.

%prep
%setup -q

%build
autoconf
LDFLAGS="-s" \
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
    --prefix=%{_prefix} \
    --sbindir=%{_sbindir} 
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{bin,include,info,man/man1,lib}
install -d $RPM_BUILD_ROOT/share/locale/{da,de,es,fr,nl,pl,pt,sl,sv}

make install DESTDIR=$RPM_BUILD_ROOT 

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/* 
	
%find_lang %{name}

%post devel
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%preun devel
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_prefix}/lib/librecode.so*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*.gz
%{_prefix}/lib/librecode.*a*
%{_prefix}/include/*
