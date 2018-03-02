### Directus Headless CMS on-premise  
[directus-docs](https://docs.getdirectus.com/6.4.0/#What_is_Directus?)   
[directus-api-docs](https://api.getdirectus.com/1.1/#API_Endpoints)
 
 ##### Deployment
 Deploy to multiple hosts by specifying host details as comma separated value to fabric like below    
 ```bash
 fab deploy
 ```
 
 See `./fabfile.py` for more deployment details
 
  ```bash
 # Fabric  deploy script
 # Supported Python version python 2.X
 # Prerequisites
 # pip see: https://pip.pypa.io/en/latest/installing/#install-or-upgrade-pip
 # fabric see: http://www.fabfile.org/
 # Amazon AWS Docker Image - aws-elasticbeanstalk-amzn-2016.09.1.x86_64-docker-hvm-201703022213 - ami-0cf1e468
 # Helper shell scripts in bin directory at project root
 #   bin
 #   ├── kill-all-dockers
 #   ├── start
 #   └── store-archive
 #  
 # Environment variables of ec2 instanecs host names
 # SSH_USER - ec2 user
 # SSH_HOSTS - ec2 instances as a comma seperated string
 # SSH_KEY_FILE_NAME  - Path to ssh key(pem file usually)
 
  ```