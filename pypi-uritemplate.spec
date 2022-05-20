#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-uritemplate
Version  : 4.1.1
Release  : 51
URL      : https://files.pythonhosted.org/packages/d2/5a/4742fdba39cd02a56226815abfa72fe0aa81c33bed16ed045647d6000eba/uritemplate-4.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/d2/5a/4742fdba39cd02a56226815abfa72fe0aa81c33bed16ed045647d6000eba/uritemplate-4.1.1.tar.gz
Summary  : Implementation of RFC 6570 URI Templates
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: pypi-uritemplate-license = %{version}-%{release}
Requires: pypi-uritemplate-python = %{version}-%{release}
Requires: pypi-uritemplate-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
uritemplate
===========
Documentation_ -- GitHub_ -- Travis-CI_
Simple python library to deal with `URI Templates`_. The API looks like

%package license
Summary: license components for the pypi-uritemplate package.
Group: Default

%description license
license components for the pypi-uritemplate package.


%package python
Summary: python components for the pypi-uritemplate package.
Group: Default
Requires: pypi-uritemplate-python3 = %{version}-%{release}

%description python
python components for the pypi-uritemplate package.


%package python3
Summary: python3 components for the pypi-uritemplate package.
Group: Default
Requires: python3-core
Provides: pypi(uritemplate)

%description python3
python3 components for the pypi-uritemplate package.


%prep
%setup -q -n uritemplate-4.1.1
cd %{_builddir}/uritemplate-4.1.1
pushd ..
cp -a uritemplate-4.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653007621
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-uritemplate
cp %{_builddir}/uritemplate-4.1.1/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/pypi-uritemplate/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/uritemplate-4.1.1/LICENSE.BSD %{buildroot}/usr/share/package-licenses/pypi-uritemplate/7720cc454c495510106e04e6173b0e2fb94e077b
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-uritemplate/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-uritemplate/7720cc454c495510106e04e6173b0e2fb94e077b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
