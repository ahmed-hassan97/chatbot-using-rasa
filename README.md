# build ChatBot Using Rasa

<p align="center">
  <img  src="https://www.jivochat.com/assets/images/compressed/chatbots/chatbots-white.png">
</p>

## 1. create virtual enivronment In linux

  I will create Virtual environment and activate it then install requirements.txt
  
```
            python3 -m venv ./venv
            cd venv/bin/activate
            pip3 install -r requirements.txt

```

## 2. run rasa command 

#### for train
```
            rasa  train

```

#### for run shell
```
            rasa  shell

```

## structure of project files

* intent (NLU) carry all sentence which express on 4 category

            1- Greet
            2- GoodBye
            3- Capital
            4- Population
    

* story file carry all output and utter

* apiRequest file carry all request to get and post data on endpoint
 
* actions file pass output of user to apiRequest file to get capital or population 

## End


