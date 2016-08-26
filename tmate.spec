%global commit_id 3be116b

Name:		tmate
Version:	1.8
Release:	1%{?dist}.git%{commit_id}
Summary:	Instant terminal sharing

License:	MIT
URL:		https://github.com/nviennot/tmate
Source0:	tmate-%{version}-%{commit_id}.tar.gz

BuildRequires:	zlib-devel
BuildRequires:	openssl-devel
BuildRequires:	libevent-devel
BuildRequires:	ncurses-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	cmake
BuildRequires:	ruby

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}-%{commit_id}

# https://gcc.gnu.org/gcc-5/porting_to.html
find . -name '*.[ch]' -print | xargs sed -i 's/__FUNCTION__/__func__/g'

./autogen.sh

%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc CHANGES FAQ README README-tmux README.md SYNCING

%{_bindir}/tmate
%{_mandir}/man1/tmate.1.gz

