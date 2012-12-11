%define oname parallel
%define pname py%{oname}
%define minversion 2.2

Summary: Python parallel port extension
Name: python-%{oname}
Version: 0.2
Release: 4
Source0: %{pname}-%{version}.tar.bz2
License: GPL
Group: Development/Python
URL: http://pyserial.sourceforge.net/pyparallel.html
BuildRequires: python-devel
BuildArch: noarch
Requires: python
Provides: %{pname}

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
PYTHONDONTWRITEBYTECODE=  python setup.py install --root %{buildroot} --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc CHANGES.txt LICENSE.txt PKG-INFO README.txt


%changelog
* Tue Apr 17 2007 Guillaume Bedot <littletux@mandriva.org> 0.2-3mdv2008.0
+ Revision: 13928
- python 2.5 build

  + Mandrake <devel@mandriva.com>


* Wed Mar 15 2006 Guillaume Bedot <littletux@mandriva.org> 0.2-1mdk
- Initial package

