# Security policy — adoption draft

This package is a preview and planning bundle, not a production-qualified execution runtime. Do not expose future shell tools to untrusted users without isolation and policy qualification.

Before public adoption, enable GitHub private vulnerability reporting and confirm the reporting path works. If enabled, use the repository Security tab to report vulnerabilities privately. If it is unavailable, request a private reporting channel without posting exploit details or credentials publicly. No response-time SLA is currently promised.

Reports should include affected revision, reproduction, impact and a redacted example. Relevant concerns include workspace escape, approval replay, command injection, prompt injection, secret export and false completion claims. Never include live credentials.
