# rfs_visualisation 

## Australian bush fire data is able to be visualised on a choropleth map.


In this project I webscrape bush fire data from the relevant rural fire services websites and visualise the data in relation to the local government areas(lga) the fires occured in.
An important part of this project is utilising the AWS **s3** and **Athena** environments.

The final visualisation can be viewed below, where fire locations are mapped within their local government area.
We can also click on individual fires to see further information including the report date.

![rfs_visual_snip](https://user-images.githubusercontent.com/114447057/222874721-32062d9c-e3ac-43be-99b5-beebc29f2e28.png)

## Objectives: 
**AWS**
- Setup AWS root user and enable credentials to make programmatic calls to AWS through Visual Studio Code's Software Development Kit.
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

## Flow chart of design steps

![rfs_flow_chart](https://user-images.githubusercontent.com/114447057/224520360-659d40ab-bd14-42c5-bc9b-a68b40e02d32.png)

I welcome any and all contributions! Here are some ways you can get started:

Report bugs: If you encounter any bugs, please let us know. Open up an issue and let us know the problem.

Documentation: If you see the need for some additional documentation, feel free to add some!

Special thanks to my friend @pitiznz for a bit of guidance.

Cheers
