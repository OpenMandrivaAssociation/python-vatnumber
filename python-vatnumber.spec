%define module_name vatnumber

Summary:	Python module to validate VAT numbers
Name:		python-%{module_name}
Version:	1.2
Release:	12
Group:		Development/Python
License:	GPLv3+
Url:		http://code.google.com/p/vatnumber/
Source0:	https://files.pythonhosted.org/packages/d7/7c/869b59cd9cb6ed1057372cb704a3b86688ae8c12cfc7fcaedbc1424f5e7f/vatnumber-1.2.tar.gz
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

