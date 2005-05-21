%define		modname og
Summary:	Drupal Organic groups Module
Summary(pl):	Modu� grup organicznych dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.3
Epoch:		0
License:	GPL
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	8111c047c7a1a620e5547b1682ad80a3
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
Ten modu� pozwala u�ytkownikom tworzy� i zarz�dza� w�asnymi "grupami".
Ka�da grupa mo�e mie� subskrybent�w i zarz�dza stron� domow� grupy
gdzie subskrybenci komunikuj� si� mi�dzy sob�. Robi� to poprzez
wysy�anie zwyk�ych rodzaj�w obiekt�w: blog�w, opowiada�, stron itp.
Na grupowej stronie domowej u�atwiaj�cej to wysy�anie jest pokazywany
blok. Blok ten dostarcza tak�e kr�tkiej informacji o grupie.

Grupy mog� by� selektywne lub nie. Grupy selektywne wymagaj�
zatwierdzenia, aby zosta� ich cz�onkiem.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # pure GPL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}

install *.module $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt og.mysql
%{_moddir}/*.module
