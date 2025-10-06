Name: slirp4netns
Version: 1.3.2
Release: 1%{?dist}
License: GPL-2.0-only
Summary: slirp for network namespaces
URL: https://github.com/rootless-containers/%{name}
# Tarball fetched from upstream
Source0: %{url}/archive/v%{version}.tar.gz
ExclusiveArch: %{golang_arches_future}
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: go-md2man
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: git-core
BuildRequires: libcap-devel
BuildRequires: libseccomp-devel
BuildRequires: libslirp-devel
BuildRequires: make

%description
slirp for network namespaces, without copying buffers across the namespaces.

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
%autosetup -Sgit %{name}-%{built_tag_strip}

%build
./autogen.sh
./configure --prefix=%{_usr} --libdir=%{_libdir}
%{__make} generate-man

%install
make DESTDIR=%{buildroot} install install-man

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Mon Feb 10 2025 Jindrich Novy <jnovy@redhat.com> - 1.3.2-1
- update to https://github.com/rootless-containers/slirp4netns/releases/tag/v1.3.2
- Related: RHEL-58990

* Tue Oct 29 2024 Jindrich Novy <jnovy@redhat.com> - 1.3.1-3
- revive slirp4netns
- Resolves: RHEL-65176
