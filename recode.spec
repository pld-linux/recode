# $Revision: 1.31 $ $Date: 2002-10-27 18:31:35 $
Summary:	Utility for converting text between multiple character sets
Summary(pl):	Uniwersalny konwerter miêdzy zestawami znaków
Name:		recode
Version:	3.6
Release:	1
License:	GPL/LGPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/recode/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-use_malloc_realloc.patch
Patch2:		%{name}-am.patch
Patch3:		%{name}-hash-nameconflict.patch
Patch4:		%{name}-ac25x.patch
Patch5:		%{name}-el.po-no0xD2.patch
Patch6:		%{name}-pl.po-update.patch
URL:		http://www.gnu.org/software/recode/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	flex
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free `recode' converts files between various character sets and
surfaces. It supports more than 200 different character sets and
surfaces, including well known ISO-8859, CP-XXXX and Unicode.

%description -l pl
Program `recode' konwertuje pliki pomiêdzy ró¿nymi zestawami znaków i
kodowaniami. Obs³uguje ponad 200 ró¿nych zestawów znaków oraz sposobów
kodowania, w³±cznie z popularnymi ISO-8859, CP-XXXX oraz Unicode.

%package devel
Summary:	Header files and documentations for librecode
Summary(pl):	Pliki nag³ówkowe i dokumentacja do librecode
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and documentations for librecode.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do librecode.

%package static
Summary:	Static librecode library
Summary(pl):	Biblioteka statyczna librecode
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static librecode library.

%description static -l pl
Biblioteka statyczna librecode.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%doc AUTHORS NEWS BACKLOG README THANKS TODO
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
