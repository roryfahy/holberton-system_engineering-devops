## Issue Summary
The duration of the outage can not be determined because adequate monitoring sofware was not in place.  The outage end time was 4 pm EST.  The impact of the outage was a complete failure for a user to make requests to our webpage.  All request made to the app either failed or returned a non-2xx response.  Due to not knowing the exact duration of the outage we must assume that 100% of users may have been affected.  The root cause of the outage was an OS imposed limit to the number of files nginx could have open at once.

## Timeline
- 2 pm - SRE testing the server using `ab` noticed server was not properly handeling any of the 2000 requests.
- 2:15 pm - upon checking the error.log file, the engineer noticed that all of the errors were a result of too many open files.  This seemed unreasonable considering this is software intedned for enterprise level applications.
- 2:30 pm - The SRE discovered that there was an OS imposed limit to the number of files nginx was allowed to have open
- 3 pm - research was conducted to determine what config file sets this limit.
- 3:30 pm - using `grep`, the engineer searched the /etc directory for any files with `nginx` in their path that contained the number 15 - the only one returned by the search was `/etc/default/nginx`.
- 3:45 pm - the limit was changed to 15000 and the nginx server was reloaded
- 4 pm - full function restored to server

## Root cause and Resolution
the downtime was caused by an OS level limit imposed on the Nginx web server.  This limit was set in the `/etc/default/nginx` config file.  Upon discovery, the SRE increased the limit from 15 to a more resonable number.

## Corrective and Preventative Measures
due to the lack of monitoring, discovery of the outage was greatly delayed.  The server may have been down for much less time if the proper monitoring services were implemeted.  Something like Datadog which is able to keep track of the network traffic would be very helpful in decreasing downtime in the future.  If this server configuration is imaged and distributed, we must modify the image in order to prevent this issue from persisting on enumerable servers.