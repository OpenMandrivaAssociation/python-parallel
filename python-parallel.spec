%define oname		parallel
%define pname		py%{oname}
%define version		0.2
%define pyversion	2.4
#python 2.2 or more needed
%define release		%mkrel 1

Summary:	Python parallel port extension
Name:		python-%{oname}
Version:	%{version}
Release:	%{release}
Source0:	%{pname}-%{version}.tar.bz2
License:	GPL
Group:		Development/Python
URL:		http://pyserial.sourceforge.net/pyparallel.html
BuildRoot:	%{_tmppath}/%{pname}-buildroot
BuildRequires:	libpython-devel >= %pyversion
BuildArch:      noarch
Requires:	python
Provides:	%{pname}

%description
This module encapsulates the access for the parrallel port. It provides 
backends for Python running on Windows, Linux and BSD. Other platforms 
are possible too but not yet integrated.

This module is still under development, but it may be useful for developers.

%prep
%setup -q -n %{pname}-%{version}

%build
perl -pi -e "s/data_files = None/data_files = {}/" setup.py
perl -pi -e "s/\r\n/\n/" *.txt PKG-INFO %oname/*.py
#python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES.txt LICENSE.txt PKG-INFO README.txt
%attr(0755,root,root) %py_puresitedir/%oname
%ifarch x86_64
%attr(0755,root,root) %py_platsitedir/%oname
%endif

