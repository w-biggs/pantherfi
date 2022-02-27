## Inspiration

Our inspiration for this project came fittingly enough while we were in the University's main library researching possible ideas for projects to develop for Steelhacks. During this brainstorming session, there was a temporary network outage within the library which halted our progress, and we began considering the possibility of switching locations to a different building on campus to see if the internet connection there was more consistent. 

While deliberating this, we realized that a utility to view the network performance of various common spaces on campus remotely would be a valuable tool for students seeking to optimize their study habits; And from that moment, PantherFi was born.

## What it does

PantherFi aggregates data from various nodes monitoring the network speeds of common wireless access points on campus. This data is processed by the PantherFi server, and is displayed via a corresponding graph for each node on our web page. This graph shows both the current network speed, and trends of this speed over time.


## How we built it

Our IoT nodes which provide the network data to be displayed use various Python scripts to run diagnostic tools on the network, clean this data into a concise format, and send this cleaned data to our server.

Our server code is powered by Python as well, using Flask to build the RESTful API that we use to route requests and interface between our database and our web page. 

Our database is an implementation of MongoDB, which was chosen due to the extensive use of JSON elsewhere throughout our codebase, which made it sensible for us to use a DB stack which would allow to keep our data in that format as is.

Our front end is built using Javascript's Vue framework, which allows it to easily interface with our server-side API. Additionally, we opted to use the Highcharts library for visualizing our data in an intuitive and interactive way.

## Challenges we ran into

Our biggest challenge in developing PantherFi was one which was critical for the core functionality of our application; That being how to handle cases of our nodes losing connection with the server due to network failures. 

We noticed this edge case during testing, as our original design had each value on the x-axis of our graph correspond to a single transmission made from our nodes to the server. This created a problem where, since only successful communications were stored in the database, instances of network downtime would never be logged or displayed, essentially achieving the polar opposite of our goal.

To remedy this, we instead represented the x-axis as time in minutes. This meant that periods of downtime would be accurately represented with a gap in the graph due to an absence of data, as opposed to said absence essentially being ignored by the system.


## Accomplishments that we're proud of

During the course of Steelhacks, our team was presented with various logistical problems which limited the amount of testing and development time we had. Given those circumstances, we are proud of what we were able to accomplish in such a short amount of time with the resources we had.

## What we learned

Going into this event, not every member of the team was familiar with the same tech stack that other members were, which resulted in this being a valuable learning experience for all involved. Through the development of PantherFi, our team gained quality insight into full stack development, as some members were more back end oriented, while some were more front end oriented. This helps us all greatly to generalize our skillsets into a wider range of technology.

Through this we also learned about IoT development, and the unique set of constraints involved in it, along with the powerful ways in which IoT technology can be leveraged.

Lastly, we gained experience in simply working in teams as opposed to the solo projects that most of us were used to throughout our undergraduate curriculum, this experience serves to strengthen the more intangible skills needed in the workforce.

## What's next for PantherFi

Our plan is to acquire additional Raspberry Pi computers to serve as nodes and, assuming the University's permission is granted, begin rolling out PantherFi in a production environment to the various common spaces around campus
