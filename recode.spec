# $Revision: 1.21 $ $Date: 2001-10-18 21:14:51 $
Summary:	Utility for converting text between multiple character sets
Summary(pl):	Uniwersalny konwerter zestawów znaków
Name:		recode
Version:	3.5d
Release:	4
License:	GPL/LGPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	http://www.iro.umontreal.ca/contrib/recode/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-use_malloc_realloc.patch
Patch2:		%{name}-am.patch
Patch3:		%{name}-hash-nameconflict.patch
URL:		http://www.iro.umontreal.ca/contrib/recode/HTML/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	flex
Prereq:		/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free `recode' converts files between various character sets and
surfaces. It supports more than 200 different character sets and
surfaces, including well known ISO-8859, CP-XXXX and Unicode.

%description -l pl
Program `recode' konwertuje zestawy znaków oraz kodowanie w plikach
tekstowych. Obs³uguje ponad 200 ró¿nych zestawów znaków oraz sposobów
kodowania, w³acznie z popularnymi ISO-8859, CP-XXXX oraz Unicode.

%package devel
Summary:	Header filess and documentations for librecode
Summary(pl):	Pliki nag³ówkowe i dokumentacja do librecode
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name} = %{version}

%description devel
Header filess and documentations for librecode.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do librecode.

%package static
Summary:	Static library librecode
Summary(pl):	Biblioteka statyczna librecode
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-devel = %{version}

%description static
Static library librecode.

%description -l pl static
Biblioteka statyczna librecode.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS BACKLOG README THANKS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_infodir}/*info*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/librecode.a
