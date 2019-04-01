# cookie-monster

Script to delete all but a white-listed set of cookies from Firefox profiles.

In the Firefox (+ derivates) browser, cookie policies are implemented 
not very rigorously with respect to accepting, blocking and deleting 
cookies, and there is only little options to customize the behavior 
with respect to cookies. In addition, blocking cookies causes many web 
pages to break. Unfortunately, there is no possibility to temporarily 
accept cookies and delete them when the session ends.

The cookie monster is a Python script that deletes from any Firefox 
profile folder all cookies whose domain does not match the provided 
whitelist:

    [/path/to/profile]
    allowed_hosts=
        *.domain.org
        *domain.org
        
The general template of a config file is `cookies.conf.bk`. You can 
rename or copy it to `cookies.conf` and edit the `allowed_hosts` field
to add the hosts you trust and whose cookies you want to permanently save.
Multiple Firefox profiles may be added.

The cookie monster can be run in a cron job, for instance, every minute:

    $ crontab -e
    
Enter:
    
    * *     * * *   cd /path/to/cookie-monster && ./cookiemonster.py >> /path/to/cookie-monster/cookies.log 2>&1

Using this script, one can set the cookie settings in Firefox to 
"accept" as the cookie monster will regularly eat all unwanted cookies. 

You should make sure that you close your Firefox sessions on a regular 
basis as the cookies will not be removable while the profile is in use.
