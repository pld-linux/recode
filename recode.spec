# $Revision: 1.13 $ $Date: 2000-05-24 16:50:46 $
Summary:	Utility for converting text between multiple character sets
Summary(pl):	Uniwersjalny konwerter zestawów znaków
Name:		recode
Version:	3.5
Release:	3
License:	GPL/LGPL
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narzêdzia/Tekst
Source0:	http://www.iro.umontreal.ca/contrib/recode/%{name}-%{version}.tar.gz
Patch0:		recode-pl.po.patch
Patch1:		recode-install.patch
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free `recode' converts files between various character sets and surfaces.
It supports more than 200 different character sets and surfaces, including
well known ISO-8859, CP-XXXX and Unicode.

%description -l pl
Program `recode' konwertuje zestawy znaków oraz kodowanie w plikach
tekstowych. Obs³uguje ponad 200 ró¿nych zestawów znaków oraz sposobów
kodowania, w³acznie z popularnymi ISO-8859, CP-XXXX oraz Unicode.

%package devel
Summary:	Header filess and documentations for librecode
Summary(pl):	Pliki nag³ówkowe i dokumentacja do librecode
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header filess and documentations for librecode.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do librecode.

%package static
Summary:	Static library librecode
Summary(pl):	Biblioteka statyczna librecode
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static library librecode.

%description -l pl static
Biblioteka statyczna librecode.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
gettextize --copy --force
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/librecode.so.*.*

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*,%{_mandir}/man1/*} \
	ABOUT-NLS AUTHORS NEWS BACKLOG README THANKS COPYING-LIB TODO
	
%find_lang %{name}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_infodir}/*info*
%{_includedir}/*

%files static
%attr(644,root,root) %{_libdir}/librecode.a
