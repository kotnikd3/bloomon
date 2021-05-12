# bloomon

### About the project
Python challenge.  
I tried with principles from Robert Martin's Clean architecture.

### Run the program in Docker
``` bash
sudo docker build -t bloomon .
# -i stands for interactive mode and -t will allocate a pseudo terminal for us
sudo docker run -i -t bloomon
```

### TODO:
* maybe encapsulate logic from methods processFlower, processDesign and processBouquet in class BusinessLogic

### Class diagram
\
![data_model](class_diagram.jpg)
