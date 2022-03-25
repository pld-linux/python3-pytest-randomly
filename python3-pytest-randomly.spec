#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Pytest plugin to randomly order tests and control random.seed
Summary(pl.UTF-8):	Wtyczka pytesta do losowej kolejności testów i sterowania random.seed
Name:		python3-pytest-randomly
Version:	3.11.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-randomly/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-randomly/pytest-randomly-%{version}.tar.gz
# Source0-md5:	13cf321031de846c969aa5522a01ec40
URL:		https://pypi.org/project/pytest-randomly/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:40.6.0
%if %{with tests}
BuildRequires:	python3-factory_boy
BuildRequires:	python3-faker
%if "%{_ver_lt '%{py3_ver}' '3.10'}" == "1"
BuildRequires:	python3-importlib-metadata >= 3.6.0
%endif
BuildRequires:	python3-numpy
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.750
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pytest plugin to randomly order tests and control random.seed.

%description -l pl.UTF-8
Wtyczka pytesta do losowej kolejności testów i sterowania random.seed.

%prep
%setup -q -n pytest-randomly-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytester,pytest_randomly" \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest_randomly
%{py3_sitescriptdir}/pytest_randomly-%{version}-py*.egg-info
