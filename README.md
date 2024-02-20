
# Page Rank Simulation with AWS Elastic Map Reduce


This project involves using distributed systems to simulate the PageRank algorithm using AWS 
EMR (Elastic MapReduce). The PageRank algorithm is a mathematical algorithm used by search 
engines to measure the importance and relevance of web pages. By simulating this algorithm using 
distributed systems, you can process large amounts of data and distribute the computational 
workload across multiple machines.


## Dataset



The Google Web Graph dataset is a large dataset that contains information on the link structure 
of the World Wide Web. It contains information on billions of web pages and their links, including the URL, the page's PageRank score, the number of inbound and outbound links, and other metadata. It was created by Google and is made available for research purposes. 

URL : https://snap.stanford.edu/data/web-Google.html


## Methodology

1. Data Collection: The first step in This project was to collect the data that we will use for the simulation. We used the Google Web Graph dataset.
2. Data Processing: Once we collected the data we processed the data so that we can use it in our program by formatting it the way we needed it to be. We then uploaded the uploaded the relevant information to amazon S3.
3. Setting up AWS EMR: We then set up AWS EMR to process the data. This involves creating a cluster of virtual servers on the AWS cloud to divide and process the data. We configured EMR to use the big data framework called Spark and used 8 instances and used an instance type of m3.xlarge
4. Implementing the PageRank Algorithm: After setting up AWS EMR, We implement the PageRank algorithm in Python. To do this we SSH into the master instance and upload the code into a file that is then run to produce the output.
5. Simulating the PageRank Algorithm: Once the output is obtained we use NetworkX to simulate the graph in order to visualize the rank of each node.
6. Analyzing the Results: Finally, we analyze the results of the simulation to gain insights into the link structure of the web and the accuracy of the PageRank algorithm. You can use various visualization tools and techniques to visualize the data and gain insights into its structure and patterns
## Conclusion

In conclusion, this project successfully simulated the PageRank algorithm using distributed systems and the AWS EMR platform. The Google Web Graph dataset was used as the input 
data, and the algorithm was implemented and executed on the cluster, resulting in PageRank 
scores for each web page.

The results of the simulation provided insights into the link structure of the web and the 
accuracy of the PageRank algorithm. The data analysis showed that the PageRank scores 
followed the expected distribution, with a small number of web pages having high scores 
and the majority of pages having low scores. Additionally, the results demonstrated the 
benefits of using distributed systems for processing large amounts of data, as the AWS EMR 
platform was able to handle the data processing in a more efficient and cost-effective 
manner than a traditional single-machine approach.
