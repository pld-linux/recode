# $Revision: 1.6 $ $Date: 1999-09-19 13:16:07 $
Summary:	Utility for converting text between multiple character sets.
Summary(pl):	Uniwersjalny konwerter zestaw�w znak�w.
Name:		recode
Version:	3.5
Release:	1
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narz�dzia/Tekst
Source:		http://www.iro.umontreal.ca/contrib/recode/recode-%{version}.tar.gz
Patch0:		recode-pl.po.patch
Patch1:		recode-install.patch
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
Requires:	%{name} = %{version}

%description devel
The recode library allows including recode functionality in your own
programs.

%description -l pl
Bibliotek recode pozwala na dodanie wszystkich funkcji programu recode
do program�w u�ytkownika.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
LDFLAGS="-s" \
CFLAGS="$RPM_OPT_FLAGS" \
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT

#install -d $RPM_BUILD_ROOT/{bin,include,info,man/man1,lib,share}
install -d $RPM_BUILD_ROOT/%{_prefix}/share/locale/{da,de,es,fr,nl,pl,pt,sl,sv}/LC_MESSAGES

make    install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/* 
gzip -9nf ABOUT-NLS AUTHORS NEWS BACKLOG README COPYING THANKS COPYING-LIB TODO
	
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

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
#%{_prefix}/share/locale
%doc %{_mandir}/man1/*
%doc *.gz
%doc %{_infodir}/*info*.gz

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/librecode.*a*
%{_prefix}/include/*
