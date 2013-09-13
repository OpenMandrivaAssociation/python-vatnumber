%define module_name vatnumber

Name:           python-%{module_name}
Version:        1.0
Release:        1
Summary:        Python module to validate VAT numbers

Group:          Development/Python
License:        GPLv3+
URL:            http://code.google.com/p/vatnumber/
Source0:        http://vatnumber.googlecode.com/files/%{module_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools


%description
Python module to validate VAT numbers.

%prep
%setup -q -n %{module_name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%doc CHANGELOG COPYRIGHT LICENSE README
%{python_sitelib}/*
