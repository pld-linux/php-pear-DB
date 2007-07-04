%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - Database Abstraction Layer
Summary(pl.UTF-8):	%{_pearname} - Abstrakcyjna warstwa baz danych
Name:		php-pear-%{_pearname}
Version:	1.7.12
Release:	1
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b86134520d473db3c5fb87b68a820037
URL:		http://pear.php.net/package/DB/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB is a database abstraction layer providing:
- an OO-style query API
- a DSN (data source name) format for specifying database servers
- prepare/execute (bind) emulation for databases that don't support it
  natively
- a result object for each query response
- portable error codes
- sequence emulation
- sequential and non sequential row fetching as well as bulk fetching
- ordered array, associative array and object formats supported for
  the fetched rows
- row limit support
- transactions support
- table information interface
- DocBook and PHPDoc API documentation

DB layers itself on top of PHP's existing database extensions. The
currently supported extensions are: dbase, fbsql, interbase, informix,
msql, mssql, mysql, oci8, odbc, pgsql and sybase (a DB style interface
to LDAP servers is also avaible from a separate package).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
DB to warstwa abstrakcji baz danych dająca:
- obiektowo zorientowane API dla zapytań
- format DSN (data source name) do podawania serwerów baz danych
- emulację prepare/execute dla baz danych nie obsługujących natywnie
  tych poleceń
- obiekt wynikowy dla każdej odpowiedzi na zapytanie
- przenośne kody błędów
- emulację sekwencji
- sekwencyjne i niesekwencyjne pobieranie wierszy oraz pobieranie
  masowe
- obsługę danych w formacie tablic uporządkowanych, tablic
  asocjacyjnych i obiektów dla pobieranych wierszy
- obsługę limitu wierszy
- obsługę transakcji
- interfejs do informacji o tabelach
- dokumentację API w formacie DocBook i PHPDoc.

Warstwa DB jest umieszczona powyżej istniejących rozszerzeń baz danych
w PHP. Aktualnie obsługiwane rozszerzenia to: dbase, fbsql, interbase,
informix, msql, mssql, oci8, odbc, pgsql i sybase (podobny do DB
interfejs do serwerów LDAP jest dostępny w osobnym pakiecie).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/doc/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
