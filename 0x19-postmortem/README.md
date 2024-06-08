Postmortem Report for Website Outage on May 20th, 2024
Issue Summary:

Duration: The outage lasted for 2 hours and 30 minutes, starting at 2:00 PM and ending at 4:30 PM (UTC).
Impact: The website was completely inaccessible, affecting approximately 100% of users. Users were unable to access any part of the website, leading to loss of service for all functionalities.
Root Cause: A faulty database migration script introduced during a new feature deployment caused a critical database table to become inaccessible.
Timeline:
1:45 PM: Deployment of the new search feature begins.
2:00 PM: Deployment completes, and the website starts experiencing issues.
2:10 PM: Monitoring systems alert the team to the website outage.
2:20 PM: Development team begins investigating the issue.
2:30 PM: Initial assumption is a server overload; server logs are checked.
2:45 PM: Hypothesis that the issue is related to the new feature; database queries are analyzed.
3:00 PM: Root cause identified as a faulty database migration script.
3:10 PM: Decision made to roll back the deployment.
3:45 PM: Rollback process initiated manually.
4:15 PM: Rollback completed, and website services start to recover.
4:30 PM: Website fully operational, and monitoring confirms stability.
Root Cause and Resolution:
Root Cause: The outage was caused by a faulty database migration script that was part of the new search feature deployment. This script caused a critical table to become inaccessible, resulting in the website being unable to retrieve necessary data for its operations.
Resolution: The issue was resolved by rolling back the deployment to the previous stable version. The rollback process involved restoring the database to its state before the faulty migration script was applied and redeploying the last known good version of the application.
Corrective and Preventative Measures:
Improvements/Fixes:

Implement comprehensive pre-deployment testing procedures, especially for database migrations.
Automate the rollback procedure to ensure a quicker response in future incidents.
Enhance and complete the documentation for deployment and rollback processes.
Improve monitoring systems to detect and alert on database-related issues earlier.
Tasks to Address the Issue:

Enhance Testing:
Develop and integrate a suite of automated tests specifically for database migrations.
Set up a staging environment that closely mirrors the production environment for thorough pre-deployment testing.
Automate Rollback Procedures:
Create and test automated rollback scripts to be used in case of future deployment failures.
Improve Documentation:
Update and expand deployment and rollback documentation.
Conduct regular training sessions for the team on these procedures.
Enhance Monitoring:
Implement additional monitoring for database migration processes.
Set up automated alerts for any failed database migrations or anomalies.
By addressing the root causes and implementing these corrective measures, we aim to prevent similar incidents in the future, ensuring better reliability and quicker incident response for our website.
