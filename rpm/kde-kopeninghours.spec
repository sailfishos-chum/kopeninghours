%global  kde_version 25.08.2
%global  kf6_version 6.18.0
%global pkgname kopeninghours

Name:       kde-kopeninghours
Release:    1%{?dist}
Version:    25.08.2
License:    ASL-2.0 and BSD-3-Clause and CC0-1.0 and LGPLv2+
Summary:    Library for parsing and evaluating OSM opening hours expressions.
Url:        https://invent.kde.org/pim/kopeninghours
#Source0:    https://invent.kde.org/pim/%%{pkgname}/-/archive/v%%{version}/%%{pkgname}-v%%{version}.tar.bz2
Source0:    %{name}-%{version}.tar.bz2
#Patch1:     cmake_fix.patch

Provides:  %{pkgname} = %{version}-%{release}
BuildRequires: kf6-extra-cmake-modules >= %kf6_version
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: pkgconfig(zlib)

BuildRequires: flex
BuildRequires: bison

# optional:
BuildRequires: pkgconfig(python3)

#BuildRequires: qt6-qtbase-devel
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: qt6-qttools-devel

BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kconfig-devel

BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kholidays-devel

%description
%{summary}.

%package devel
Summary: Development files for %{name}
License: BSD and CC0-1.0 and LGPLv2+ and MIT and ODbL-1.0
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides:  %{pkgname}-devel = %{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%cmake_kf6 \
    -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

%find_lang %{pkgname}

%files -f %{pkgname}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*categories
%{_libdir}/libKOpeningHours.so.*
%{_kf6_qmldir}/org/kde/kopeninghours/

%files devel
%{_includedir}/KOpeningHours/
%{_includedir}/kopeninghours/
%{_includedir}/kopeninghours_version.h
%{_libdir}/cmake/KOpeningHours/
%{_libdir}/libKOpeningHours.so
