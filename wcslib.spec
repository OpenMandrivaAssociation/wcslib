%define major 8
%define devname %mklibname wcs -d
%define libname %mklibname wcs
%define libname_virt libwcs
%define oldlibname %mklibname wcs 7

Summary:	An implementation of the FITS World Coordinate System standard
Name:		wcslib
Version:	8.1
Release:	1
Group:		Sciences/Astronomy
# Library is under LGPLv3+ utils under GPLv3+
License:	LGPLv3+
URL:		http://www.atnf.csiro.au/people/mcalabre/WCS/
Source0:	http://www.atnf.csiro.au/people/mcalabre/WCS/%{name}-%{version}.tar.bz2
Patch0:		increase_tspx_test_tol.patch

BuildRequires: flex
BuildRequires: pkgconfig(cfitsio)
BuildRequires: pkgconfig(zlib)
BuildRequires: gcc-gfortran
BuildRequires: gfortran-devel

%description
WCSLIB is a library that implements the "World Coordinate System" (WCS)
convention in FITS (Flexible Image Transport System).

%package -n %{libname}
Summary: An implementation of the FITS World Coordinate System standard
Group: Sciences/Astronomy
License: LGPLv3+
Provides: wcslib = %{version}-%{release}
Obsoletes:	%{oldlibname}

%description -n %{libname}
WCSLIB is a library that implements the "World Coordinate System" (WCS)
convention in FITS (Flexible Image Transport System).

%package -n %{devname}
Summary: Libraries, includes, etc. used to develop an application with %{name}
Group: Sciences/Astronomy
License: LGPLv3+
Requires: wcslib = %{version}-%{release}
Provides: wcslib-devel = %{version}-%{release}

%description -n %{devname}
These are the files needed to develop an application using %{name}.

%package utils
Summary: Utility programs provided by %{name}
Group: Sciences/Astronomy
License: GPLv3+
Requires: wcslib = %{version}-%{release}

%description utils
Utils provided with %{name}.

%prep
%autosetup -p1

%build
export CC=gcc
export CXX=g++
%configure --enable-fortran=gfortran
%make_build

%install
%make_install
# fix permissions
rm -rf %{buildroot}/usr/share/doc/wcslib-%{version}
chmod 755 %{buildroot}%{_includedir}/wcslib-%{version}
find %{buildroot} -name '*.a' -delete

%files -n %{libname}
%doc COPYING.LESSER README
%{_libdir}/*.so.%{major}{,.*}

%files -n %{devname}
%doc COPYING.LESSER html wcslib.pdf
%{_libdir}/*.so
%{_libdir}/pkgconfig/wcslib.pc
%{_includedir}/wcslib
%{_includedir}/wcslib-%{version}

%files utils
%doc COPYING
%{_bindir}/*
%{_mandir}/man1/*

