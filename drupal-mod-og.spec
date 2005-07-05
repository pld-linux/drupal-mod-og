%define		modname og
Summary:	Drupal Organic groups Module
Summary(pl):	Modu³ grup organicznych dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.5
Epoch:		0
License:	GPL
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	8111c047c7a1a620e5547b1682ad80a3
BuildRequires:	rpmbuild(macros) >= 1.194
URL:		http://drupal.org/project/og
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_moddir		%{_datadir}/drupal/modules

%description
Enable users to create and manage their own 'groups'. Each group can
have subscribers, and maintains a group home page where subscribers
communicate amongst themselves. They do so by posting the usual node
types: blog, story, page, etc. A block is shown on the group home page
which facilitates these posts. The block also provides summary
information about the group.

Groups may be selective or not. Selective groups require approval in
order to become a member.

%description -l pl
Ten modu³ pozwala u¿ytkownikom tworzyæ i zarz±dzaæ w³asnymi "grupami".
Ka¿da grupa mo¿e mieæ subskrybentów i zarz±dza stron± domow± grupy
gdzie subskrybenci komunikuj± siê miêdzy sob±. Robi± to poprzez
wysy³anie zwyk³ych rodzajów obiektów: blogów, opowiadañ, stron itp.
Na grupowej stronie domowej u³atwiaj±cej to wysy³anie jest pokazywany
blok. Blok ten dostarcza tak¿e krótkiej informacji o grupie.

Grupy mog± byæ selektywne lub nie. Grupy selektywne wymagaj±
zatwierdzenia, aby zostaæ ich cz³onkiem.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # pure GPL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}

install *.module $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF
To create tables needed for Drupal Organic groups module, issue these commands:
zcat %{_docdir}/%{name}-%{version}/og.mysql.gz | mysql drupal
EOF
fi

%files
%defattr(644,root,root,755)
%doc *.txt og.mysql
%{_moddir}/*.module
