%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - Database Abstraction Layer
Summary(pl):	%{_pearname} - Abstrakcyjna wartswa baz danych
Name:		php-pear-%{_pearname}
Version:	1.4.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	01729b5bfe1dad62393bdd5d15cf55fa
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

This class has in PEAR status: %{_status}.

%description -l pl
DB to warstwa abstrakcyji baz danych daj�ca:
- obiektowo zorientowane API dla zapyta�
- format DSN (data source name) do podawania serwer�w baz danych
- emulacj� prepare/execute dla baz danych nie obs�uguj�cych natywnie
  tych polece�
- obiekt wynikowy dla ka�dej odpowiedzi na zapytanie
- przeno�ne kody b��d�w
- emulacj� sekwencji
- sekwencyjne i niesekwencyjne pobieranie wierszy oraz pobieranie
  masowe
- obs�ug� danych w formacie tablic uporz�dkowanych, tablic
  asocjacyjnych i obiekt�w dla pobieranych wierszy
- obs�ug� limitu wierszy
- obs�ug� transakcji
- interfejs do informacji o tabelach
- dokumentacj� API w formacie DocBook i PHPDoc.

Warstwa DB jest umieszczona powy�ej istniej�cych rozszerze� baz danych
w PHP. Aktualnie obs�ugiwane rozszerzenia to: dbase, fbsql, interbase,
informix, msql, mssql, oci8, odbc, pgsql i sybase (podobny do DB
interfejs do serwer�w LDAP jest dost�pny w osobnym pakiecie).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_class}.php $RPM_BUILD_ROOT%{php_pear_dir}/
install %{_pearname}-%{version}/%{_class}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/doc/* %{_pearname}-%{version}/tests
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
