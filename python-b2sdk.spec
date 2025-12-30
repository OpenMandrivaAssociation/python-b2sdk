Name:		python-b2sdk
Version:	2.10.2
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/b/b2sdk/b2sdk-%{version}.tar.gz
Summary:	Backblaze B2 SDK
URL:		https://pypi.org/project/b2sdk/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(logfury)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(annotated-types)
BuildRequires:	python%{pyver}dist(typing-extensions)
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildSystem:	python
BuildArch:	noarch

%description
Backblaze B2 SDK

%prep
%autosetup -p1 -n b2sdk-%{version}

%files
%{py_sitedir}/b2sdk
%{py_sitedir}/b2sdk-*.*-info
