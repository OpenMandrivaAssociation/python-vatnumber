%define module_name vatnumber

Summary:	Python module to validate VAT numbers
Name:		python-%{module_name}
Version:	1.0
Release:	5
Group:		Development/Python
License:	GPLv3+
Url:		http://code.google.com/p/vatnumber/
Source0:	http://vatnumber.googlecode.com/files/%{module_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)

%description
Python module to validate VAT numbers.

%prep
%setup -qn %{module_name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc CHANGELOG COPYRIGHT LICENSE README
%{python_sitelib}/*

