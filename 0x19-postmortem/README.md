Postmortem: Web Application Outage on October 12, 2023

Issue Summary:

Duration of Outage: October 12, 2023, from 10:30 AM to 12:15 PM PDT
Impact: The main web application was inaccessible, displaying a "504 Gateway Timeout" error. Approximately 75% of the users were affected.
Root Cause: The root cause was identified as a misconfigured Nginx reverse proxy causing an overload on the backend servers.
Timeline:

10:32 AM: First report of the issue was detected through automated monitoring alerts indicating high server response times.
10:35 AM: An engineer confirmed the issue after failing to access the web application.
10:40 AM: Initial assessment suspected a DDoS attack due to the abnormal traffic increase.
10:50 AM: The security team found no signs of DDoS after inspecting traffic logs.
11:00 AM: Focus shifted to potential infrastructure issues; the database and cache layers were examined, but no problems were found.
11:20 AM: An engineer noticed a discrepancy in the Nginx configuration file during a routine inspection.
11:40 AM: The incident was escalated to the web operations team, specialized in server configurations.
12:00 PM: The misconfiguration was fixed, and services began to return to normal.
12:15 PM: Full service was restored, and ongoing checks ensured that the system was stable.
Root Cause and Resolution:

Root Cause: It was discovered that a recent deployment had unintentionally modified the Nginx reverse proxy settings. This misconfiguration prevented Nginx from appropriately distributing traffic, causing an overload on backend servers, resulting in a "504 Gateway Timeout" error for the users.
Resolution: The incorrect settings in the Nginx configuration file were identified and corrected. Restarting the Nginx service normalized traffic distribution, alleviating the load on the backend servers.
Corrective and Preventative Measures:

Improvements/Fixes: The main focus should be on refining deployment processes to prevent similar misconfigurations in the future, as well as enhancing monitoring to detect such issues proactively.

TODO:

Patch Nginx Server: Roll back to the last known good configuration and verify the current state against approved settings.
Improve Deployment Protocols: Ensure that configuration changes go through a thorough review process before deployment. Implement automated checks to verify configuration integrity post-deployment.
Enhance Monitoring: Add specific monitoring checks for server configuration integrity. Set up alerts for abnormal traffic patterns that might suggest an issue.
Training: Provide training to deployment teams on the importance of ensuring configuration integrity and the implications of misconfigurations.
Regular Audits: Schedule routine configuration audits to ensure that systems are running with the approved settings.
In closing, we deeply regret the inconvenience caused and are taking proactive steps to prevent a recurrence. The lessons learned from this incident will drive our commitment to improving our systems and processes.