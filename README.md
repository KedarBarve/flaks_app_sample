Simple Flask App

cd bin
./docker_run.sh

docker images
./docker_run.sh

cd ../utils

# Data is stored in memory for illustration. Examples of psoting data.
# Inspect the scripts on how to inspect . Port can be changed if needed

[ec2-user@ip-172-31-85-91 utils]$ ./get_customer.sh
{"data":"Not found","message":"success"}

[ec2-user@ip-172-31-85-91 utils]$ ./get_product.sh
{"data":"Not found","message":"success"}

[ec2-user@ip-172-31-85-91 utils]$ ./post_product.sh
{"data":{"data":{"name":"Product1","price":129.99}},"message":"success"}

[ec2-user@ip-172-31-85-91 utils]$ ./get_product.sh
{"data":{"name":"Product1","price":129.99},"message":"success"}

[ec2-user@ip-172-31-85-91 utils]$ ./post_customer.sh
{"data":{"age":25,"name":"John"},"message":"success"}

[ec2-user@ip-172-31-85-91 utils]$ ./get_customer.sh
{"data":{"age":25,"name":"John"},"message":"success"}

