%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - Database Abstraction Layer
Summary(pl):	%{_pearname} - Abstrakcyjna warstwa baz danych
Name:		php-pear-%{_pearname}
Version:	1.7.5
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	43954e51f8dcf5c62700268bdc61ac63
URL:		http://pear.php.net/package/DB/
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

In PEAR status of this package is: %{_status}.

%description -l pl
DB to warstwa abstrakcji baz danych daj±ca:
- obiektowo zorientowane API dla zapytañ
- format DSN (data source name) do podawania serwerów baz danych
- emulacjê prepare/execute dla baz danych nie obs³uguj±cych natywnie
  tych poleceñ
- obiekt wynikowy dla ka¿dej odpowiedzi na zapytanie
- przeno¶ne kody b³êdów
- emulacjê sekwencji
- sekwencyjne i niesekwencyjne pobieranie wierszy oraz pobieranie
  masowe
- obs³ugê danych w formacie tablic uporz±dkowanych, tablic
  asocjacyjnych i obiektów dla pobieranych wierszy
- obs³ugê limitu wierszy
- obs³ugê transakcji
- interfejs do informacji o tabelach
- dokumentacjê API w formacie DocBook i PHPDoc.

Warstwa DB jest umieszczona powy¿ej istniej±cych rozszerzeñ baz danych
w PHP. Aktualnie obs³ugiwane rozszerzenia to: dbase, fbsql, interbase,
informix, msql, mssql, oci8, odbc, pgsql i sybase (podobny do DB
interfejs do serwerów LDAP jest dostêpny w osobnym pakiecie).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_class}.php	$RPM_BUILD_ROOT%{php_pear_dir}/
install %{_pearname}-%{version}/%{_class}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{doc/*,tests}
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
