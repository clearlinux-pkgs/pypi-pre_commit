#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-pre_commit
Version  : 3.2.2
Release  : 37
URL      : https://files.pythonhosted.org/packages/89/40/0f5b8d53178545f736172c8c2fc4f5eb68fffa828dba5ddad3cc43af878e/pre_commit-3.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/89/40/0f5b8d53178545f736172c8c2fc4f5eb68fffa828dba5ddad3cc43af878e/pre_commit-3.2.2.tar.gz
Summary  : A framework for managing and maintaining multi-language pre-commit hooks.
Group    : Development/Tools
License  : MIT
Requires: pypi-pre_commit-bin = %{version}-%{release}
Requires: pypi-pre_commit-license = %{version}-%{release}
Requires: pypi-pre_commit-python = %{version}-%{release}
Requires: pypi-pre_commit-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cfgv)
BuildRequires : pypi(identify)
BuildRequires : pypi(nodeenv)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(virtualenv)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![build status](https://github.com/pre-commit/pre-commit/actions/workflows/main.yml/badge.svg)](https://github.com/pre-commit/pre-commit/actions/workflows/main.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/pre-commit/main.svg)](https://results.pre-commit.ci/latest/github/pre-commit/pre-commit/main)

%package bin
Summary: bin components for the pypi-pre_commit package.
Group: Binaries
Requires: pypi-pre_commit-license = %{version}-%{release}

%description bin
bin components for the pypi-pre_commit package.


%package license
Summary: license components for the pypi-pre_commit package.
Group: Default

%description license
license components for the pypi-pre_commit package.


%package python
Summary: python components for the pypi-pre_commit package.
Group: Default
Requires: pypi-pre_commit-python3 = %{version}-%{release}

%description python
python components for the pypi-pre_commit package.


%package python3
Summary: python3 components for the pypi-pre_commit package.
Group: Default
Requires: python3-core
Provides: pypi(pre_commit)
Requires: pypi(cfgv)
Requires: pypi(identify)
Requires: pypi(nodeenv)
Requires: pypi(pyyaml)
Requires: pypi(virtualenv)

%description python3
python3 components for the pypi-pre_commit package.


%prep
%setup -q -n pre_commit-3.2.2
cd %{_builddir}/pre_commit-3.2.2
pushd ..
cp -a pre_commit-3.2.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680619876
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pre_commit
cp %{_builddir}/pre_commit-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pre_commit/0a1b7c6ad0735b8a94231652bab67240e4b834f6 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pre-commit

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pre_commit/0a1b7c6ad0735b8a94231652bab67240e4b834f6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
