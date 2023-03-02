---
title: Cloud Computing Fundamentals on Alibaba Cloud

---
> [https://www.coursera.org/specializations/alibabacloud](https://www.coursera.org/specializations/alibabacloud)

* TOC
{:toc}

## Week1 ECS Quiz
1. What is the full name of ECS?
   - [x] Elastic Compute Service

2. Cloud disks are reliable because they use ________  to provide block-level data storage for ECS instances, ensuring 99.9999999% data reliability.

    - [x] a distributed file management system with 3 redundant copies

3. Which of the following products can be used to make an ECS only accessible from a private IP address?

    - [x] VPN Gateway

4. Alibaba Cloud server ECS is provided to customer as a cloud service. Which is the support SLA of Alibaba Cloud Products?
    - [x] 7*24

5. If you are running an online ticket booking service with relatively fixed traffic, which kind of payment method is the most appropriate?
    - [x] subsricption

6. Comparing to traditional server room trusteeship, ECS provides better flexibility. Which of the following operation is NOT supported?
   - [x] Modify available zone.

7. It's very easy to provision a new ECS instance. During the instance creation, you need to specify the Region and Zone. Which of the following description about region & zone is NOT correct?
   - [x] ECS has different support policy for different regions.

8. You can ________ an ECS instance’s configuration. (Number of correct answers: 2)

    - [x] upgrade
    - [x] downgrade

9. The most important feature of Alibaba cloud server is elasticity. When trying to expand the disk, user can expand the disk size or add a new disk. Which of the following description is NOT correct about adding a new disk?
    
    - [x] The size of the newly added disk must be bigger than the existing disk.

10. Before important operations such as upgrading application software or migrating business data, it is suggested to create one or more ________. 

    - [x] snapshots

## Week2 RDS Quiz

1. When doing RDS backup, which type of backup is supported by automatic backup?

    - [x] Physical Backup

2. After creating an RDS read-only instance, you should use which of the following services to make its data consistent to the master instance?

    - [ ] You have to configure the DTS service
    - [ ] You have to configure the Message Service
    - [ ] You have to configure the ExpressConnect Service
    - [x] Nothing, this will be done automatically by RDS

3. Which of the following is not Alibaba Cloud CloudMonitor metrics for RDS?

    - [x] Billing

4. If you have an ECS instance and an RDS instance in the same region, what is the easiest way to connect the two?

    - [x] Use the RDS Intranet Address and connect via Intranet

5. Which of the followings is part of the cost of using Alibaba Cloud RDS?

    - [x] Instance Fee

6. Which of the following statements is true for RDS?

    - [x] Multiple databases can be created in one RDS instance.

7. In each Alibaba Cloud service region, there are different data centers with independent power supply and network. These data centers are also called () in Alibaba Cloud.

    - [x] Zone

8. Which of the followings is not the database type supported by RDS?

    - [ ] PostgreSQL
    - [ ] Microsoft SQL Server
    - [ ] MySQL
    - [x] Oracle Database

7. When using Alibaba Cloud RDS, you still need to take care of which of the following O&M tasks?

    - [ ] Virtualization
    - [ ] Server hardware
    - [ ] Networking infrastructure
    - [x] Business data

8.  RDS is a PaaS, what is the full term of PaaS in cloud computing?

    - [x] Platform as a service

## Week3 OSS Quiz
1. Alibaba Cloud Object Storage Service (OSS) is a massive, highly available, secured and cost effective storage service. OSS is superior than self-built storage in all these aspects. Which of the following advantage relates to the high availability of OSS?

    - [ ] Availability actually relies on the underlying hardware, which can break down easily. Once the hard disk malfunctions, it can also lead to permanent data loss.


    - [x] Data Reliability is not less than 99.99999999%. Data is backed up automatically with multiple redundant copies.


   - [ ] Data has to be backed up by customer manually, which is time-consuming and labor-intensive.


    - [ ] The following features are available: Multiple Authentication and Authorization mechanism, Whitelist, Anti-leech URL, and Master-Sub Account

2. Alibaba Cloud Object Storage Service (OSS) is a massive, highly available, secured and cost effective storage service. One of the special characteristics of OSS is its superior data reliability, because of its underlying backup technology and policies. Which of the following statement about OSS backup is correct?
 
    - [ ] OSS supports 3 internal data copies, so the data can be  manually recovered should there be any problem.


    - [ ] Customer has to safeguard their own data. OSS provides various backup interfaces to facilitate offsite backups.


    - [ ] OSS leverages RAID0+1 configuration of its underlying physical hard disks. There is no impact even if 2 hard disks were to fail simultaneously.


    - [x] OSS supports 3 internal data copies, no human intervention is required to recover the data when anything goes wrong.

3. Alibaba Cloud OSS is a cloud storage service that features massive capacity, outstanding security, low cost, and high reliability. Files managed by OSS can be easily shared with external applications. Before sharing a file, you can find the URL of the file from the detail page of a file. The sharing is done by using ( ) application-layer protocol.

   - [ ] FTP


    - [x] HTTP


    - [ ] TCP


    - [ ] SMTP

4. After activating the OSS service, you must create buckets in the OSS management console or by using Open API before you can store files. Which of the following statements is true for buckets?

    - [x] Bucket names must be globally unique and cannot be changed once created.


    - [ ] Bucket names must be globally unique but can be changed after being created.


    - [ ] Bucket names must be unique under each account and can be changed after being created.


    - [ ] Bucket names must be unique under each account and cannot be changed once created.

5. OSS supports massive file storage and provides multiple file deletion functions.
 
    Which of the followings is most suitable if many objects need to be deleted with a pattern, for example, to delete all the objects generated before a specific day?

   - [ ] Deletes the objects one by one in the management console.


    - [ ] Deletes the objects in batch in the management console.

    - [x] Deletes the objects with lifecycle management.

    - [ ] Deletes the objects one by one using Open API.

6. In OSS, all data is stored in buckets. When an OSS bucket is set with the ( ) permission, the OSS Bucket allows other users to read (GET Object) the objects in the bucket.

    - [x] Public-read-write


    - [ ] Public-read


    - [ ] Private


    - [ ] Private-read

7. An object is the basic unit of data stored in OSS.  Which of the following file operations are supported by OSS? (Number of correct answers: 3)


    - [x] File modification


    - [ ] File uploading


    - [ ] File deletion


    - [ ] File reading

8. When using Alibaba Cloud OSS, you can set access control in 3 different levels, which are ( ) (Number of correct answers: 3)


    - [x] Bucket level


    - [x] Object level


    - [x] RAM account level


    - [ ] Directory level

9. In OSS Image Processing service, URLs are accessed with standard HTTP GET requests, and all processing parameters are in the QueyString of the URL. Which of the following modes are supported by image processing function?(Number of correct answers: 2)

    - [ ] Picture mode


    - [x] Parameter mode


    - [x] Style mode


    - [ ] Interactive mode

10. Which 2 parameters you need to configure to setup a static website hosted on an OSS bucket? (Number of correct answers: 2)

    - [x] Default page


    - [ ] Navigation page


    - [x] 404 page


    - [ ] Return page

## Week4 SLB Quiz
1. When using Alibaba Cloud SLB, users can enable the health check function. For Layer 4 services (UDP protocol), SLB determines the availability of ECS instances through?



    - [ ] Special characters contained in the message returned from backend ECS instances


    - [ ] Length of message returned from backend ECS instances 


    - [x] Whether it receives the required data packet from the backend ECS instance within the configured response timeout period or not.


    - [ ] Status codes returned from backend ECS instances 

2. Your website has high volume of traffic and sudden spikes for a very short time. In this scenario, which product can manage traffic peak efficiently and maintain a consistent user experience?



    - [ ] Auto Scaling


    - [x] Server Load Balancer
 


    - [ ] RDS


    - [ ] VPC

3. Applications or websites with users from different parts of the world will require low latency and high availability (HA) with multilayer disaster recovery.  In this scenario, except Auto Scaling should be used along with Server Load Balancer, which service is also suggested to be used together?



    - [ ] RDS


    - [ ] MaxCompute F


    - [x] DNS


    - [ ] VPC

4. Which feature in Server Load Balancer means that it can forward the access requests from a single user to the same ECS instance within a certain period to ensure session continuity?



    - [ ] Weighted Round Robin F


    - [x] Session persistence
 


    - [ ] Health check


    - [ ] Least connections scheduling

5. Server Load Balancer provides central certificate management system for which of the following protocol?



    - [ ] UDP


    - [ ] TCP


    - [ ] HTTP


    - [x] HTTPS

6. A company uses Alibaba Cloud SLB and Auto Scaling at the same time, hoping this combination can help save O&M cost and provide a stable and reliable system. 
 
    As an expert of Alibaba Cloud, which of the following statement is true?



    - [ ] All backend servers under the same SLB instance must be in the same Scaling Group  F


    - [ ] All ECS instances under the same SLB instance must be running on the same operating system


    - [ ] All backend servers under the same SLB instance must have the same configuration


    - [x] SLB instances must have Health Check enabled, or they cannot be used together with Auto Scaling

7. You are developing a highly available web application using stateless web servers. Which services are suitable for storing session state data?



    - [ ] OSS 


    - [x] Table Store


    - [x] RDS


    - [ ] MaxCompute

8. An enterprise built an isolated network environment by using Alibaba Cloud VPC, and connected this VPC and a traditional data center via VPN. As a result, this enterprise can seamlessly migrate data from its traditional data center to Alibaba Cloud.  Now they need to receive user requests from the Internet, and assign these requests to multiple ECS instances inside the VPC by using SLB. Which of the following statements are correct?

    - [x] They can create an SLB instance in the VPC, and mount ECS instances within the VPC to this SLB instance.  And then use a jump server to receive external requests, and direct these requests to SLB to forward them to backend ECS instances.


    - [ ] They can create an SLB instance in the VPC, and mount ECS instances within the VPC to this SLB instance. And then, bind an EIP to the SLB, so that this SLB instance can receive requests from the Internet, and assign these requests to the backend ECS instances.


    - [x] They can create an SLB instance with an Internet IP address, and mount ECS instances within the VPC to this SLB instance. The public SLB will be used to receive external requests. As a result, requests from the Internet will be transferred to backend ECS instances within the VPC.


    - [ ] They can create an SLB instance with an Internet IP address, and mount ECS instances within the VPC and servers of the traditional data center to this SLB instance. The public SLB will be used to receive external requests. As a result, requests from the Internet will be transferred to backend ECS instances within the VPC and servers of the traditional data center.

9. Usually, Alibaba Cloud SLB, ECS, and Auto Scaling are used together. Which of the following statements are correct? 



    - [x] SLB instances must have Health Check enabled, or they cannot be used in combination with Auto Scaling.


    - [x] An SLB instance can bind multiple Scaling Groups


    - [x] The three must be within the same region if they are going to be used in combination.


    - [ ] A Scaling Group can support multiple SLB instances simultaneously

10. Alibaba Cloud SLB is a service for distributing traffic among multiple ECS instances. To make SLB works as desired, you need to set which of the following configurations carefully. 



    - [x] SLB instance's property


    - [ ] SLB Instance's IP address


    - [x] SLB Instance's Listener


    - [x] SLB Instance's Backend ECS instance pool

## Week5 Auto Scaling Quiz
1.  Auto Scaling is a management service that can automatically adjusts elastic computing resources based on your business needs and policies. It supports adding existing ECS instances into the scaling group, whose status must be ________.



   - [ ] Created 


   - [x] Running


   - [ ] Stopped


   - [ ] Preparing

2.  A video streaming company uses SLB to distribute user requests to 30 ECS instances (the 30 ECS instances have the same configuration). Yet, the company finds that the service traffic soars dramatically every night from 20:00 to 02:00. According to their calculation, the evening traffic is 100% higher than the traffic in other periods of time. To properly respond to user requests, which of the following methods is most preferred from the perspective of cost and implementation simplicity?



   - [ ] Configure Auto Scaling to automatically upgrade and downgrade the ECS instances.


   - [ ] Create 30 ECS instances based on the custom image and add them to SLB. Then, configure weights for these ECS instances to respond to user requests every night from 20:00 to 02:00, and reset those weights to zero for other periods of time.


   - [x] Configure Auto Scaling to automatically add or reduce ECS instances.


   - [ ] Manually create 30 ECS instances using the custom image, and then add them to SLB every night before 20:00 and remove them after 02:00.

3.  A customer uses Alibaba Cloud Auto Scaling service and creates a scaling group. He sets the "Minimum number of instances" to 6 and "Maximum number of instances" to 8.  After correctly configuring scaling settings, the customer adds a scaling rule "Adjust to 10 ECS instances", and creates a scheduled task based on this rule. And then, the customer checks the scaling group and see it already contains 6 valid ECS instances, he then enables this scaling group immediately. How many ECS instance are left in the scaling group when the scheduled task is activated once?



   - [x] Eight


   - [ ] Ten


   - [ ] Six


   - [ ] Five

4.  A scaling group in Auto Scaling refers to the collection of ECS instances with the same application scenario. Which of the following must be configured when creating a scaling group? (Number of correct answers: 3)



   - [x] Region of scaling group


   - [x] Cool-down Time


   - [x] Scaling MaxSize and MinSize


   - [ ] Scheduled/Event-triggered task

5.  In Auto Scaling, the cool-down time of a scaling group refers to the lockout period after a scaling activity has been executed successfully. Which of the following statements about cool-down time are true? (Number of correct answers: 3)



   - [ ] During the cool-down time of a scaling group, only the alarms from CloudMonitor can bypass the cool-down time and trigger scaling activities, whereas others will still subject to the cool-down time, such as the manually triggered scaling activities.


   - [x] When a scaling group meets the cool-down time, you can abort the cool-down time by disabling and then restarting the scaling group.


   - [x] When multiple ECS instances are added or removed from a scaling group, the cool-down time begins only when the last instance has been added or removed from the scaling group.


   - [x] During the cool-down time, only the scaling activities in the same scaling group are locked.

6.  Auto Scaling is a management service that can automatically adjust elastic computing resources based on your business needs and policies. Its key functions are ( ). (Number of correct answers: 3)



   - [x] Horizontally adjusts ECS instances based on users' business needs, namely adds or reduces ECS instances automatically.


   - [x] Supports configuring SLB to automatically add ECS instances or remove them from SLB instances.


   - [x] Supports the ApsaraDB for RDS whitelist to automatically add the IP addresses of ECS instances or remove them from the ApsaraDB for RDS whitelist.


   - [ ] Upgrades or downgrades the configuration (including the memory size and CPU) of a single ECS instance based on users' business needs.

7.  There are scheduled tasks and event-triggered tasks in Auto Scaling. About event-triggered tasks, which of the following metrics are supported for this type of tasks? (Number of correct answers: 4)



   - [x] CPU workload


   - [x] Memory utilization rate


   - [x] Average system workload


   - [x] Inbound and outbound traffic


   - [ ] Disk IOPS

8.  Two modes are available for deleting scaling groups in Auto Scaling: ForceDelete mode and non-ForceDelete mode. Which of the following conditions must be met in non-ForceDelete mode? (Number of correct answers: 2)



   - [x] No scaling activities are ongoing in the scaling group.


   - [x] No ECS instances exist in the scaling group.


   - [ ] No scheduled tasks and event-triggered tasks exist in the scaling group.


   - [ ] The scaling group is not working in conjunction with SLB and ApsaraDB for RDS.

9.  When using Auto Scaling, you have to create scaling group, scaling configuration, scaling rule, scheduled task and event-triggered task. When a task is created, the task will be triggered according to the pre-defined condition. Which of the following conditions can trigger a task? (Number of correct answers: 2)



   - [x] The maximum CPU utilization rate of all the ECS instances in the scaling group is greater than 60%.


   - [ ] The average IOPS of all the ECS instances in the scaling group is less than 100.


   - [x] The user-defined activity execution time is met.


   - [ ] More than 50% of the requests responded by all the ECS instances in the scaling group are write requests.

10.   When using Auto Scaling, you want to execute a task at a specific time such as removing 1 ECS instance every night at 00:00. To achieve this, which of the following operations should be performed? (Number of correct answers: 2)

   - [ ] Manually remove this the ECS instance from console.


   - [x] Create a scaling rule.


   - [x] Create a scheduled task.


   - [ ] Create an event-triggered task.

## Week6 Security Quiz

1.   IT system risk management should be considered from a variety of different angles. Which of the following is a description of device and computing security?



   - [ ] Includes network architecture, boundary protection, access control, intrusion prevention, and communication encryption.
 


   - [ ] Includes security auditing, data integrity, and confidentiality.


   - [ ] Includes PC room power supply, temperature and humidity control, and prevention of wind, rain, and lightning. 


   - [x] Includes intrusion prevention, malicious code prevention, identity authentication, access control, central management and control, and security auditing.

2.   Which of the following descriptions of the shared responsibilities security model is CORRECT?



   - [ ] After beginning to use cloud service, users only need to pay attention to the security of their own apps and data. All other security will be the responsibility of the cloud service provider.


   - [ ] After beginning to use cloud service, the cloud service provider will become responsible for all of the user’s security. 


   - [ ] After beginning to use cloud service, users must still take care of physical and environmental security.


   - [x] After beginning to use cloud service, the user and the cloud service provider will be jointly responsible for cloud security, with each responsible for different layers of security.

3.   If an enterprise chooses the “All In One” deployment structure, which of the following security issues need NOT be considered?



   - [x] Data transmission security


   - [ ] Log-in security


   - [ ] Application access attacks


   - [ ] Network attacks

4.   Regarding Alibaba Cloud’s data security protection, which of the following can satisfy data backup and disaster recovery requirements?



   - [ ] Alibaba Cloud Certificates


   - [ ] ApsaraDB Encrypted Storage


   - [x]  ECS Snapshot


   - [ ] HTTPDNS

5.   Which of the folllowing option is not the function provided by VPC?



   - [ ] Security isolation


   - [x] Accelerate the network access speed


   - [ ] Customized network configuration


   - [ ] Support various network connections

6.   Which of the following methods CANNOT increase account security?



   - [ ] Strong password policies


   - [ ] Periodically reset the user login passwords


   - [ ] Adhere to the minimum authorization principle


   - [x] Unite user management, permission management and resource management into a single management process

7.   Which of the following Alibaba Cloud products need to be considered to use if you want to build an elastic computing cluster to provide web service together and also with dynamic data and static data separately stored? (Number of Correct Answers: 4)



   - [x] ECS


   - [x] SLB


   - [x] RDS


   - [x] OSS


   - [ ] KMS

8.   Cloud Monitor provides monitoring service to Alibaba Cloud resources and internet applications. Which of the following statements is correct: 



   - [ ] Users can not use Cloud Monitor through console f


   - [x] Cloud Monitor also supports monitoring websites that are not deployed on Alibaba Cloud


   - [ ] Users need to purchase CloudMonitor service separately before use


   - [ ] Cloud Monitor does not support monitoring websites not deployed on Alibaba Cloud 

9.   Regarding the 'Shared Security Responsibilities' on Alibaba Cloud, which of the following options are the responsibilities Cloud user need to take care of? (Number of Correct Answers: 3)



   - [x] Data security inside ECS


   - [ ] Physical servers water proof


   - [x] Application vulnerabilities


   - [x] ECS network configuration

10.   Anti-DDoS is one of the major Alibaba Cloud Security products. Many websites have experienced different types of DDoS attacks, an accurate understanding of DDoS is crucial to protect websites. Which of the following descriptions about DDoS attacks is the most accurate one?



   - [ ] The main target for DDoS attacks are databases.


   - [ ] DDoS attacks will try to crack  passwords through a large number of attempts.


   - [x] The main purpose of a DDoS attack is to make the target server unable to provide service normally, which why it  is one of the most difficult network attacks to defend. 


   - [ ] The purpose of a DDoS attack is to steal confidential information.