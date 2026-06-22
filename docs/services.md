# Services Documentation

## data_service.py

## data_service.py

Purpose:
Load mythology datasets.

Current Functions:
- load_stories()

Future:
- validation
- database support


### Purpose

Responsible for loading and managing mythology datasets.

### Current Responsibilities

* Read JSON files
* Load Krishna stories
* Return story objects to the application

### Why Was It Created?

To separate data access logic from retrieval logic.

Instead of loading JSON files everywhere in the codebase, all dataset operations are centralized in one service.

### Future Responsibilities

* Load Shiva stories
* Load Shani stories
* Validate datasets
* Support database migration

### Interview Explanation

The Data Service follows the Separation of Concerns principle.

Data loading responsibilities are isolated from embedding generation, retrieval, and LLM inference.

This makes the codebase easier to maintain and extend.
