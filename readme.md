<p align="center">
  <a href="" rel="noopener">
 <img src="https://avatars2.githubusercontent.com/u/53947571?s=200&v=4"  alt="Project Orva Logo"></a>
</p>

<h1 align="center">Project Orva - Mono Repo </h1>

> This repository is a mono mirror of the repositories found [here](https://github.com/project-orva) managed with [easy mono mirror](https://github.com/GuyARoss/easy-mono).
> Note: this project is still a big work in progress.

### What is project orva? 
Project orva is a "digital assistant" aiming to solve some of the issues found in modern digital assistance platforms. (This project is still a WIP)

### Some of the problems we are attempting to solve
#### Open-sourcing "digital assistance"
Amazon & Google are in the ad business.. 

#### Ability to hold continuity throughout dialog.
Modern digital assistance will typically have an issue doing these assertions, either failing to determine what the user is trying to covey or returning something nonsensical. 

__e.g__ If I tell ask my friend to turn on the television, then told him to "turn it up", he would have known to increase the volume on the television. Or if were to tell him to add 5 to 5, then immediately after asked him to multiply that by 1, he could tell me that is 10. 

The approach that I took to this problem is to remember important features of past resolved statements then applying them when a new request is made with lower weights than the bast request. After this we can just do some probabilistic determination of what request is most likely being made, and return it.

#### Ability to chain requests in a single dialog statement. 
I want to include more than one statement within my request. 

__e.g__ If I were to say something like "Could you add 12 to the max temperature in London", the system should correctly evaluate the statement and perform the necessary tasks to complete the request.

### Basic Platform Overview
 ![architecture_overview](/diagrams/orva_architecture_overview.png)

#### Skill Service
Skill service handles the routing and determination of skills that are registered to this system.

At a high level the deterministic evaluation works by extracting all of the features present within provided example statements and compares them with the features present within the input.

We are using gRPC for both registering skills to the service and making predictions on input.

#### Speech Service
Speech service handles the generation of dynamic speech in scenarios where skills are unavailable or if the predictability of a skill is below some specified threshold.  


### Contribution
Feel free to contribute by opening a Pull Request or an issue thread.

Contributions are always appreciated! 

### License
This project does not currently have a license