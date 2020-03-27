%define  major         6
%define  libname       %mklibname wcs %{major}
%define  libname_virt  libwcs
%define  develname     %mklibname wcs -d

Name:    wcslib
Version: 6.4
Release: 1
Summary: An implementation of the FITS World Coordinate System standard

Group:   Sciences/Astronomy
# Library is under LGPLv3+ utils under GPLv3+
License: LGPLv3+
URL:     http://www.atnf.csiro.au/people/mcalabre/WCS/
Source0: ftp://ftp.atnf.csiro.au/pub/software/wcslib/%{name}-%{version}.tar.bz2
Patch0:  increase_tspx_test_tol.patch

BuildRequires: flex
BuildRequires: pkgconfig(cfitsio)
BuildRequires: pkgconfig(zlib)
BuildRequires: gcc-gfortran

%description
WCSLIB is a library that implements the "World Coordinate System" (WCS)
convention in FITS (Flexible Image Transport System).

%package -n %{libname}
Summary: An implementation of the FITS World Coordinate System standard
Group: Sciences/Astronomy
License: LGPLv3+
Provides: wcslib = %{version}-%{release}

%description -n %{libname}
WCSLIB is a library that implements the "World Coordinate System" (WCS)
convention in FITS (Flexible Image Transport System).

%package -n %{develname}
Summary: Libraries, includes, etc. used to develop an application with %{name}
Group: Sciences/Astronomy
License: LGPLv3+
Requires: wcslib = %{version}-%{release}
Provides: wcslib-devel = %{version}-%{release}

%description -n %{develname}
These are the files needed to develop an application using %{name}.

%package utils
Summary: Utility programs provided by %{name}
Group: Sciences/Astronomy
License: GPLv3+
Requires: wcslib = %{version}-%{release}

%description utils
Utils provided with %{name}.

%prep
%setup -q
%autopatch -p1

%build
export CC=gcc
export CXX=g++
# To learn about aarch64
cp -a /usr/lib/rpm/config.{guess,sub} config/

%configure --enable-fortran=gfortran
%__make

%install
%make_install
# fix permissions
rm -rf %{buildroot}/usr/share/doc/wcslib-%{version}
chmod 755 %{buildroot}%{_includedir}/wcslib-%{version}
find %{buildroot} -name '*.a' -delete

%check
%ifnarch armv7hl
# Don't parallelize
make check
%endif

%files -n %{libname}
%doc COPYING.LESSER README
%{_libdir}/*.so.%{major}{,.*}

%files -n %{develname}
%doc COPYING.LESSER html wcslib.pdf
%{_libdir}/*.so
%{_libdir}/pkgconfig/wcslib.pc
%{_includedir}/wcslib
%{_includedir}/wcslib-%{version}

%files utils
%doc COPYING
%{_bindir}/*
%{_mandir}/man1/*
