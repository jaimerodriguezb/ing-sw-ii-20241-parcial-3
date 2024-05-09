# Code analysis
## parcial 3 
#### Version not provided 

**By: Fuad David Franco**

*Date: 2024-05-08*

## Introduction
This document contains results of the code analysis of parcial 3



## Configuration

- Quality Profiles
    - Names: Sonar way [Python]; 
    - Files: AY9ZHr7BtE8vwW8FoL1F.json; 


 - Quality Gate
    - Name: Sonar way
    - File: Sonar way.xml

## Synthesis

### Analysis Status

Reliability | Security | Security Review | Maintainability |
:---:|:---:|:---:|:---:
A | A | A | A |

### Quality gate status

| Quality Gate Status | OK |
|-|-|



### Metrics

Coverage | Duplications | Comment density | Median number of lines of code per file | Adherence to coding standard |
:---:|:---:|:---:|:---:|:---:
0.0 % | 0.0 % | 2.4 % | 55.0 | 99.7 %

### Tests

Total | Success Rate | Skipped | Errors | Failures |
:---:|:---:|:---:|:---:|:---:
0 | 0 % | 0 | 0 | 0

### Detailed technical debt

Reliability|Security|Maintainability|Total
---|---|---|---
-|-|0d 6h 19min|0d 6h 19min


### Metrics Range

\ | Cyclomatic Complexity | Cognitive Complexity | Lines of code per file | Coverage | Comment density (%) | Duplication (%)
:---|:---:|:---:|:---:|:---:|:---:|:---:
Min | 0.0 | 0.0 | 0.0 | 0.0 | 1.2 | 0.0
Max | 142.0 | 133.0 | 457.0 | 0.0 | 6.3 | 0.0

### Volume

Language|Number
---|---
Python|457
Total|457


## Issues

### Issues count by severity and types

Type / Severity|INFO|MINOR|MAJOR|CRITICAL|BLOCKER
---|---|---|---|---|---
BUG|0|0|0|0|0
VULNERABILITY|0|0|0|0|0
CODE_SMELL|0|124|0|7|0


### Issues List

Name|Description|Type|Severity|Number
---|---|---|---|---
String literals should not be duplicated|Duplicated string literals make the process of refactoring error-prone, since you must be sure to update all occurrences. <br /> On the other hand, constants can be referenced from many places, but only need to be updated in a single place. <br /> Noncompliant Code Example <br /> With the default threshold of 3: <br />  <br /> def run(): <br />     prepare("this is a duplicate")  # Noncompliant - "this is a duplicate" is duplicated 3 times <br />     execute("this is a duplicate") <br />     release("this is a duplicate") <br />  <br /> Compliant Solution <br />  <br /> ACTION_1 = "action1" <br />  <br /> def run(): <br />     prepare(ACTION_1) <br />     execute(ACTION_1) <br />     release(ACTION_1) <br />  <br /> Exceptions <br /> No issue will be raised on: <br />  <br />    duplicated string in decorators  <br />    strings with less than 5 characters  <br />    strings with only letters, numbers and underscores  <br />  <br />  <br /> @app.route("/api/users/", methods=['GET', 'POST', 'PUT']) <br /> def users(): <br />     pass <br />  <br /> @app.route("/api/projects/", methods=['GET', 'POST', 'PUT'])  # Compliant <br /> def projects(): <br />     pass <br /> |CODE_SMELL|CRITICAL|6
Cognitive Complexity of functions should not be too high|Cognitive Complexity is a measure of how hard the control flow of a function is to understand. Functions with high Cognitive Complexity will be <br /> difficult to maintain. <br /> See <br />  <br />    Cognitive Complexity  <br /> |CODE_SMELL|CRITICAL|1
Method names should comply with a naming convention|Sharing some naming conventions is a key point to make it possible for a team to efficiently collaborate. This rule allows to check that all method <br /> names match a provided regular expression. <br /> Noncompliant Code Example <br /> With default provided regular expression: ^[a-z_][a-z0-9_]*$ <br />  <br /> class MyClass: <br />     def MyMethod(a,b): <br />         ... <br />  <br /> Compliant Solution <br />  <br /> class MyClass: <br />     def my_method(a,b): <br />         ... <br /> |CODE_SMELL|MINOR|15
Field names should comply with a naming convention|Sharing some naming conventions is a key point to make it possible for a team to efficiently collaborate. This rule allows to check that field <br /> names match a provided regular expression. <br /> Noncompliant Code Example <br /> With the default regular expression ^[_a-z][_a-z0-9]*$: <br />  <br /> class MyClass: <br />   myField = 1 <br />  <br /> Compliant Solution <br />  <br /> class MyClass: <br />   my_field = 1 <br /> |CODE_SMELL|MINOR|23
Local variable and function parameter names should comply with a naming convention|Shared naming conventions allow teams to collaborate effectively. This rule raises an issue when a local variable or function parameter name does <br /> not match the provided regular expression. <br /> Exceptions <br /> Loop counters are ignored by this rule. <br />  <br /> for i in range(limit):  # Compliant <br />     print(i) <br /> |CODE_SMELL|MINOR|84
Unused local variables should be removed|If a local variable is declared but not used, it is dead code and should be removed. Doing so will improve maintainability because developers will <br /> not wonder what the variable is used for. <br /> Noncompliant Code Example <br />  <br /> def hello(name): <br />     message = "Hello " + name # Noncompliant <br />     print(name) <br /> for i in range(10): <br />     foo() <br />  <br /> Compliant Solution <br />  <br /> def hello(name): <br />     message = "Hello " + name <br />     print(message) <br /> for _ in range(10): <br />     foo() <br />  <br /> Exceptions <br /> _ as well as tuples will not raise an issue for this rule. The following examples are compliant: <br />  <br /> for _ in range(10): <br />     do_something() <br /> username, login, password = auth <br /> do_something_else(username, login) <br /> |CODE_SMELL|MINOR|2


## Security Hotspots

### Security hotspots count by category and priority

Category / Priority|LOW|MEDIUM|HIGH
---|---|---|---
LDAP Injection|0|0|0
Object Injection|0|0|0
Server-Side Request Forgery (SSRF)|0|0|0
XML External Entity (XXE)|0|0|0
Insecure Configuration|0|0|0
XPath Injection|0|0|0
Authentication|0|0|0
Weak Cryptography|0|0|0
Denial of Service (DoS)|0|0|0
Log Injection|0|0|0
Cross-Site Request Forgery (CSRF)|0|0|0
Open Redirect|0|0|0
Permission|0|0|0
SQL Injection|0|0|0
Encryption of Sensitive Data|0|0|0
Traceability|0|0|0
Buffer Overflow|0|0|0
File Manipulation|0|0|0
Code Injection (RCE)|0|0|0
Cross-Site Scripting (XSS)|0|0|0
Command Injection|0|0|0
Path Traversal Injection|0|0|0
HTTP Response Splitting|0|0|0
Others|0|0|0


### Security hotspots

