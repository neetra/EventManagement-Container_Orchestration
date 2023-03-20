# EventManagement-Container_Orchestration

Event management appilcation deals with performing CRUD operations on Events.

# Steps to run locally
- Navigate to EventManagementContainerOrchestration folder and execute following command
	```
		docker compose up -d
	```

# Steps to run tests
- Navigate to test folder
	```
		pytest
	```

# Reference 
- [https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/](https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/)
- [https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/](https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/)
- https://github.com/huseinzol05/Python-DevOps/tree/master/basic-backend
- https://stackoverflow.com/questions/59012381/pytest-flask-application-attributeerror-module-src-api-has-no-attribute-test

# Troubleshooting 
- Running pytest encountered below error
			```oserror: [winerror 123] the filename, directory name, or volume label syntax is incorrect:
			```
	- Check folder, file name should not have special characters like '-' etc
- Cannot find module app
    - Copy absolute path of app folder
    - Add absolute path value to  enviornment varaible PYTHONPATH
	   - Windows
	   - Linux
	- Restart computer and verify.
	