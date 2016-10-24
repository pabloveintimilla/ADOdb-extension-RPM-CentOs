RPM PHP-ADOdb extension for CentOS
===================================

About [PHP-ADOdb](http://phplens.com/lens/adodb/docs-adodb.htm)

PHP's database access functions are not standardised. This creates a need for a database class library to hide the differences between the different database API's (encapsulate the differences) so we can easily switch databases. 

This RPM easy install PHP-ADOdb.
Testing in Centos 5 and 6 whith PHP 5.2 and 5.3

Instalation
------------

1. Dowload RPM from this repo
    `wget https://github.com/pabloveintimilla/ADOdb-extension-RPM-CentOs/releases/download/v1.0/php-adodb-ext-5.0.4-1.el6.x86_64.rpm`
2. Install RPM: 
    `rpm -Ivh php-adodb-ext-5.0.4-1.el6.x86_64.rpm`

Develop
------------

To generate RPM use:
`
 # yum groupinstall "Development Tools" 
 # yum install rpmdevtools
 # yum install rpmlint

 # useradd makerpm

 # [makerpm@local ~]$ rpmdev-setuptree

 # [makerpm@local ~]$ rpmbuild -ba adodb-ext.spec
`
More detail in http://fedoraproject.org/wiki/How_to_create_an_RPM_package
