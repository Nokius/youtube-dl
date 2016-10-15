Name:           youtube-dl
Summary:        Download Youtube Video
Version:        2016.10.12
Release:        1%{?dist}
License:        Public Domain dedication, see http://unlicense.org/
Source0:        %{name}-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  zip
BuildRequires:  python
Requires:       python

%description

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
make clean
rm -rf $RPM_BUILD_ROOT


%files
/usr/local/bin/youtube-dl
/usr/local/share/zsh/site-functions/_youtube-dl
/etc/bash_completion.d/youtube-dl
/etc/fish/completions/youtube-dl.fish
%defattr(-,root,root,-)

