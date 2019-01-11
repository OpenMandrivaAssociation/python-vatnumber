%define module_name vatnumber

Summary:	Python module to validate VAT numbers
Name:		python-%{module_name}
Version:	1.2
Release:	1
Group:		Development/Python
License:	GPLv3+
Url:		http://code.google.com/p/vatnumber/
Source0:	https://pypi.python.org/packages/source/v/vatnumber/vatnumber-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)

%description
Python module to validate VAT numbers.

%prep
%setup -qn %{module_name}-%{version}

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc CHANGELOG COPYRIGHT LICENSE README
%{py_puresitedir}/*
