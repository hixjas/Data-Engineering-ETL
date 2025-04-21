# Data-Engineering-ETL
Project 3
# Columbus Business Locator API

## Overview
A RESTful API service built with Flask that provides geographic business data for Columbus, Ohio. Designed to help:

- City planners analyze business distribution
- Developers build location-based applications
- Residents discover local businesses

## Features
- **Geospatial queries** (lat/long coordinates)
- **Business-community relationships**
- **Scalable PostgreSQL backend**
- **RESTful JSON endpoints**

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL 13+
- pipenv (recommended)


### Clone repo
git clone https://github.com/hixjas/Data-Engineering-ETL
cd Data-Engineering-ETL

## Ethical considerations:
This project incorporates several ethical considerations in its design and implementation:

Data Privacy: All business information is limited to publicly available data, with no collection or storage of personal customer information.

Accessibility: The API is designed to be equally accessible to all users.

Bias Mitigation: We've implemented checks to ensure balanced representation of businesses across all communities, avoiding over-representation of certain business types or neighborhoods in query results.

Transparency: All data sources are clearly documented, and the codebase is open for public inspection to maintain accountability.

References for the data source(s)

1. Primary Business Data:

 - Columbus Open Data Portal
 - Last updated: March 2025
 - License: Public Domain

2. Community Boundaries:

 - City of Columbus Planning Division
 - Last updated: February 2025
 - License: CC-BY 4.0

3. Geospatial Reference Data:

 - OpenStreetMap
 - Continuously updated
 - License: ODbL 1.0
