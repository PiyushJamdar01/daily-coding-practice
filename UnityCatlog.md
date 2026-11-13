Unity Catalog in Databricks

1. What is Unity Catalog

Unity Catalog is a centralized data governance solution in Databricks. It helps organizations manage, organize, secure, and monitor their data across different workspaces.

In simple words, Unity Catalog helps us control:

Who can access the data.

Who can read, write, update, or delete data.

How data is organized.

Where data is stored.

How data is accessed and managed.

2. Why do we need Unity Catalog

In an organization, different departments work with different types of data, such as HR, Finance, Sales, and Marketing.

Not every employee should have access to all company data. For example, an HR employee may need access to employee details, but should not automatically have access to confidential financial information.

Unity Catalog helps manage these permissions and ensures that the right users have access to the right data.

3. Main Components of Unity Catalog

Unity Catalog has a three-level namespace:

Metastore → Catalog → Schema → Tables

A. Data Governance

Data Governance is the process of managing, securing, and controlling how data is accessed and used within an organization.

Unity Catalog supports data governance through:

Access control and permissions.

Data discovery.

Data lineage.

Auditing.

Data classification.

Example: An HR manager can be given permission to access employee information, while other employees may have limited access.

Unity Catalog is one central place to organize and control all your data and Ai assets
- Tables , Files , ML models and Functions and everything

* The Five Parts of Unity Catalog

1) Metastore 
2) Catalog
3) Schema
4) Objects
5) Permissions


1) Metastore
- the register stores the Metadata 

- table names
- where the data lives
- who has access
- does not store the actual data
- one metastore per region 
- every workspace in that region connects to it 
- define once works everywhere

2) Catalogs
- The first level of organizing

- by environment - dev, prod 
- or by business unit - sales , finance

3) Schema - basically a database
- a folder that groups related tables

4) Objects - the actual thing or data

- Table and views - Structure data 
- Volumes - files: CSV, images, PDFs
- Function =s and ML models

** Permission flows downword - 
 means if the permission is given to catalogs level that same permission automatically allocate to the Schema and tables ( Objects )

** In unity catlog we cant just filter the  table we can also apply the filter to rows and column 