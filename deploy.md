# Deploy docs
### Install the EB CLI:
```pip install awsebcli --upgrade --user```
### To initialize an EB CLI project
```eb init -i```
> Select the default AWS region: us-east-1 : US East (N. Virginia)
>
> Setup your credentials:
>- aws-access-id
>- aws-secret-key
> Select an application to use: 2 (for production)
>1. afcms-staging
>2. afcms-dev
>3. afcms
>4. [ Create new Application ]
> It appears you are using Docker. Is this correct? (Y/n): Y
> Select a platform version: 1
> Do you wish to continue with CodeCommit?: n
> Do you want to set up SSH for your instances? (Y/n): Y
> Select a keypair: 1 (afcms-dev)
### To Deploy your changes to the selected eb environment:
first commit the changes to git:
```sh git commit -m "commit message"```
Then run the following command to deploy the changes to elastic beanstalk from the project folder:
```eb deploy```
Check the current beanstalk environment and application:
 ```eb status```
### To Revert Back to Previous Application Version In Elastic Beanstalk:
- Open the Elastic Beanstalk console.
- Choose an application.
- In the navigation pane, choose Application Versions.
- Select the application version that you want to deploy.
- Choose an environment and then choose Deploy.
### To Create A New Environment In Elastic Beanstalk:
- Open the Elastic Beanstalk console.
- Choose the application.
- From the Actions menu in the upper right corner, choose Create environment.
- Choose the Web server environment.
- Choose a Platform: Generic Docker
- For application code select an existing version.
- Choose Create environment.
