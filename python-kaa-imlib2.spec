%define 	module	kaa-imlib2

Summary:	Imlib2 wrapper for python
Summary(pl.UTF-8):	Wrapper imlib2 dla Pythona
Name:		python-%{module}
Version:	0.2.1
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/freevo/%{module}-%{version}.tar.gz
# Source0-md5:	f4d3019b7471a7da541e13de91ec2875
URL:		http://www.freevo.org/kaa/
BuildRequires:	imlib2-devel >= 1.2.1
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-kaa-base
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-kaa-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Imlib2 wrapper for python.

%description -l pl.UTF-8
Wrapper imlib2 dla Pythona.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/*.egg-info
%dir %{py_sitedir}/kaa/imlib2
%{py_sitedir}/kaa/imlib2/*.py[co]
%attr(755,root,root) %{py_sitedir}/kaa/imlib2/*.so
