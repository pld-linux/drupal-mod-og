%define		modname og
Summary:	Drupal Organic groups Module
Summary(pl.UTF-8):	Moduł grup organicznych dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.7
License:	GPL
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	f038f4b8b2be4a29e42722a27fb8dd7a
BuildRequires:	rpmbuild(macros) >= 1.194
URL:		http://drupal.org/project/og
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules

%description
Enable users to create and manage their own 'groups'. Each group can
have subscribers, and maintains a group home page where subscribers
communicate amongst themselves. They do so by posting the usual node
types: blog, story, page, etc. A block is shown on the group home page
which facilitates these posts. The block also provides summary
information about the group.

Groups may be selective or not. Selective groups require approval in
order to become a member.

%description -l pl.UTF-8
Ten moduł pozwala użytkownikom tworzyć i zarządzać własnymi "grupami".
Każda grupa może mieć subskrybentów i zarządza stroną domową grupy
gdzie subskrybenci komunikują się między sobą. Robią to poprzez
wysyłanie zwykłych rodzajów obiektów: blogów, opowiadań, stron itp.
Na grupowej stronie domowej ułatwiającej to wysyłanie jest pokazywany
blok. Blok ten dostarcza także krótkiej informacji o grupie.

Grupy mogą być selektywne lub nie. Grupy selektywne wymagają
zatwierdzenia, aby zostać ich członkiem.

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

%triggerpostun -- %{name} < 4.6.0-0.7
%banner -e %{name} <<'EOF'
You need to update your database:
ALTER TABLE `og` ADD `register` int(1) NOT NULL default '0';
ALTER TABLE `og` ADD `directory` int(11) NOT NULL default '1';
EOF

%files
%defattr(644,root,root,755)
%doc *.txt og.mysql
%{_moddir}/*.module
