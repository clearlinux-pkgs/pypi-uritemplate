#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : uritemplate
Version  : 3.0.0
Release  : 10
URL      : http://pypi.debian.net/uritemplate/uritemplate-3.0.0.tar.gz
Source0  : http://pypi.debian.net/uritemplate/uritemplate-3.0.0.tar.gz
Summary  : URI templates
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: uritemplate-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
uritemplate
===========
Documentation_ -- GitHub_ -- BitBucket_ -- Travis-CI_
Simple python library to deal with `URI Templates`_. The API looks like

%package python
Summary: python components for the uritemplate package.
Group: Default

%description python
python components for the uritemplate package.


%prep
%setup -q -n uritemplate-3.0.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484582323
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1484582323
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
