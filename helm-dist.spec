%undefine _disable_source_fetch

Name:          helm-dist
Version:       3.8.2
Release:       0%{?dist}
Summary:       The official CLI for Amazon EKS 
License:       ASL 2.0
URL:           https://helm.sh/docs/intro/install/

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      helm

Source:        https://get.helm.sh/helm-v%{version}-linux-amd64.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -D linux-amd64/helm %{buildroot}%{_bindir}/helm
%{__install} -D linux-amd64/README.md %{buildroot}%{_docdir}/helm/README.md
%{__install} -D linux-amd64/LICENSE %{buildroot}%{_docdir}/helm/LICENSE

%files
%defattr (-, root, root, 755)
%{_bindir}/helm
%doc %{_docdir}/helm/README.md
%doc %{_docdir}/helm/LICENSE
