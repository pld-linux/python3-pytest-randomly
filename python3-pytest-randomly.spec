#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Pytest plugin to randomly order tests and control random.seed
Summary(pl.UTF-8):	Wtyczka pytesta do losowej kolejności testów i sterowania random.seed
Name:		python3-pytest-randomly
Version:	5.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-randomly/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-randomly/pytest_randomly-%{version}.tar.gz
# Source0-md5:	f45a562cbb1810b425efa6e4ec8c32c6
URL:		https://pypi.org/project/pytest-randomly/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.11
BuildRequires:	python3-uv-build >= 0.12.1
BuildRequires:	python3-uv-build < 0.13
%if %{with tests}
BuildRequires:	python3-factory_boy
BuildRequires:	python3-faker
BuildRequires:	python3-numpy
BuildRequires:	python3-pytest >= 8
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.045
Requires:	python3-modules >= 1:3.11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pytest plugin to randomly order tests and control random.seed.

%description -l pl.UTF-8
Wtyczka pytesta do losowej kolejności testów i sterowania random.seed.

%prep
%setup -q -n pytest_randomly-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytester,pytest_randomly" \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pytest_randomly
%{py3_sitescriptdir}/pytest_randomly-%{version}.dist-info
