# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-yaml
Epoch: 100
Version: 6.0.1
Release: 1%{?dist}
Summary: YAML parser and emitter for Python
License: MIT
URL: https://github.com/yaml/pyyaml/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: libyaml-devel
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-PyYAML
Summary: YAML parser and emitter for Python
Requires: libyaml-0-2
Requires: python3
Provides: python3-PyYAML = %{epoch}:%{version}-%{release}
Provides: python3-pyyaml = %{epoch}:%{version}-%{release}
Provides: python3dist(pyyaml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyyaml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyyaml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyyaml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyyaml) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-PyYAML
PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.

%files -n python%{python3_version_nodots}-PyYAML
%license LICENSE
%{python3_sitearch}/*
%{python3_sitearch}/_yaml
%{python3_sitearch}/yaml
%endif

%if 0%{?sle_version} > 150000
%package -n python3-PyYAML
Summary: YAML parser and emitter for Python
Requires: libyaml-0-2
Requires: python3
Provides: python3-PyYAML = %{epoch}:%{version}-%{release}
Provides: python3-pyyaml = %{epoch}:%{version}-%{release}
Provides: python3dist(pyyaml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyyaml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyyaml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyyaml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyyaml) = %{epoch}:%{version}-%{release}

%description -n python3-PyYAML
PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.

%files -n python3-PyYAML
%license LICENSE
%{python3_sitearch}/*
%endif

%if 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-PyYAML
Summary: YAML parser and emitter for Python
Requires: libyaml
Requires: python3
Provides: python3-PyYAML = %{epoch}:%{version}-%{release}
Provides: python3-pyyaml = %{epoch}:%{version}-%{release}
Provides: python3dist(pyyaml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyyaml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyyaml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyyaml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyyaml) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-PyYAML
PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.

%files -n python%{python3_version_nodots}-PyYAML
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000) && !(0%{?rhel} == 7)
%package -n python3-pyyaml
Summary: YAML parser and emitter for Python
Requires: libyaml
Requires: python3
Provides: python3-PyYAML = %{epoch}:%{version}-%{release}
Provides: python3-pyyaml = %{epoch}:%{version}-%{release}
Provides: python3dist(pyyaml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyyaml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyyaml) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyyaml = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyyaml) = %{epoch}:%{version}-%{release}

%description -n python3-pyyaml
PyYAML is applicable for a broad range of tasks from complex
configuration files to object serialization and persistance.

%files -n python3-pyyaml
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
