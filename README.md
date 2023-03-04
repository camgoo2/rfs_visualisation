# rfs_visualisation 

## Welcome to my first project where Australian bush fire data is able to be visualised on a choropleth map.


In this project I webscrape data from bush fire data from the relevant rural fire services websites and put into an interactive visualisation with reference to the local government areas they occured in.
An important part of this project is being utilising the AWS *s3* and *Athena* environments.

The final visualisation can be viewed below, where fire locations are mapped within their local government area(lga).

![rfs_visualisation_snippet](https://user-images.githubusercontent.com/114447057/222837496-b0cec4e0-79dd-4a50-9dd1-7a24e54bd973.png)

## Objectives: 
**AWS**
- Setup AWS root user and enable credentials to make programmatic calls to AWS Toolkit through Visual Studio Code
- Create AWS IAM user access for 's3' (database cloud storage) and 'Athena' (SQL query engine)

**Data**
- Locate, extract and clean fire locations data.
- Locate lga polygon and lga population data. 
- Put data sets to s3 bucket
- Create database tables in Athena
- Join lga polygon and lga population data based on Key ID field. SQL Query.
- Select Distinct fire data. SQL Query
- Enable fire locations and lga relationship with a points in polygon instersectional join.

**Visualisation**
- Create a interactive choropleth style map which shows the fire locations and relevant information. 

##Flow chart of design steps

![rfs_flow_chart](https://user-images.githubusercontent.com/114447057/222857356-ff78d288-cf83-4c15-812e-165545e29f16.png)

I welcome any and all contributions! Here are some ways you can get started:

Report bugs: If you encounter any bugs, please let us know. Open up an issue and let us know the problem.
Contribute code: If you are a developer and want to contribute, follow the instructions below to get started!
Suggestions: If you don't want to code but have some awesome ideas, open up an issue explaining some updates or imporvements you would like to see!
Documentation: If you see the need for some additional documentation, feel free to add some!
3-Diagram (optional) - If necessary, add a diagram showing where this project fits and how it works. If it’s a CLI tool or a graphical tool, this would be a great opportunity to add an animated GIF of your project in action. Even better, adding a youtube video demo of your project to your README could be very beneficial to gaining more users.This could be a flow diagram here.

4-Installation and usage instructions (for end-users) - Now it’s time to get a little bit nerdier. If a user has gotten this far into your README, you bet there’s a chance they actually want to use your project. Give instructions on how to install or use the tool. Don’t get this confused with how to contribute to this project (like help improve the code), that’s the next section. This section should only talk about how to be a consumer of the project

5-Installation and usage instructions (for contributors) - Ya know the best part of open source projects? If you make something really cool, others will want to help make it better! In this section of the README, give instructions on how to pull the code down and start up the tool for development purposes. This section is usually pretty technical and may require instruction on how to build from source, but hopefully, you have a script for MAKEFILE from stuff like that. Anything you can do to make the development experience easier will help you gain more contributors.

6-Contributor expectations - If you are looking for contributors, make sure you set the ground rules. There’s nothing worse than getting someone who wants to help you but they don’t know how! This section of the README gives the guidelines for contributions. Do you expect someone to create an issue in the issue queue and then resolve it with a pull request? Do you want squashed commits? Do you have a pull requests template? Explain it all here

7-Known issues - I already talked about this README section above so I’ll keep it short. Make a brief list of known issues here so people don’t report bugs you already know about!



