Summary:	Utility for converting text between multiple character sets
Summary(pl.UTF-8):	Uniwersalny konwerter między zestawami znaków
Name:		recode
Version:	3.6
Release:	7
License:	LGPL v2+ (library), GPL v2+ (utility)
Group:		Applications/Text
# for future releases (3.7/4.0) see https://github.com/pinard/Recode/
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	be3f40ad2e93dae5cd5f628264bf1877
Patch0:		%{name}-info.patch
Patch1:		%{name}-use_malloc_realloc.patch
Patch2:		%{name}-am.patch
Patch3:		%{name}-hash-nameconflict.patch
Patch4:		%{name}-ac25x.patch
Patch5:		%{name}-el.po-no0xD2.patch
Patch6:		%{name}-pl.po-update.patch
Patch7:		%{name}-debian-11.patch
Patch8:		%{name}-gcc4_3.patch
Patch9:		%{name}-bool.patch
Patch10:	%{name}-ac.patch
URL:		http://recode.progiciels-bpi.ca/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	texinfo
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free `recode' converts files between various character sets and
surfaces. It supports more than 200 different character sets and
surfaces, including well known ISO-8859, CP-XXXX and Unicode.

%description -l pl.UTF-8
Program `recode' konwertuje pliki pomiędzy różnymi zestawami znaków i
kodowaniami. Obsługuje ponad 200 różnych zestawów znaków oraz sposobów
kodowania, włącznie z popularnymi ISO-8859, CP-XXXX oraz Unicode.

%package devel
Summary:	Header files and documentations for librecode
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do librecode
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and documentations for librecode.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do librecode.

%package static
Summary:	Static librecode library
Summary(pl.UTF-8):	Biblioteka statyczna librecode
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static librecode library.

%description static -l pl.UTF-8
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
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

# duplicate of m4/*.m4 files
%{__rm} acinclude.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_bindir}/recode
%attr(755,root,root) %{_libdir}/librecode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librecode.so.0
%{_infodir}/recode.info*
%{_mandir}/man1/recode.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librecode.so
%{_libdir}/librecode.la
%{_includedir}/recode.h
%{_includedir}/recodext.h

%files static
%defattr(644,root,root,755)
%{_libdir}/librecode.a
