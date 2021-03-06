
# Fuzzy Directory Search CLI

_**DSA Project, WinSem 2021**_  

A handy tool in the form of a **command line interface** that allows you to **search** for your fancy files and gives you the results in a fraction of the time it would take you to say the words, _"fuzzy wuzzy"_.  

```
   ___                                                                       __         
 /'___\                                                                     /\ \        
/\ \__/  __  __  ____    ____    __  __    ____     __     __     _ __   ___\ \ \___    
\ \ ,__\/\ \/\ \/\_ ,`\ /\_ ,`\ /\ \/\ \  /',__\  /'__`\ /'__`\  /\`'__\/'___\ \  _ `\  
 \ \ \_/\ \ \_\ \/_/  /_\/_/  /_\ \ \_\ \/\__, `\/\  __//\ \L\.\_\ \ \//\ \__/\ \ \ \ \ 
  \ \_\  \ \____/ /\____\ /\____\\/`____ \/\____/\ \____\ \__/.\_\\ \_\\ \____\\ \_\ \_\
   \/_/   \/___/  \/____/ \/____/ `/___/> \/___/  \/____/\/__/\/_/ \/_/ \/____/ \/_/\/_/
                                     /\___/                                             
                                     \/__/                                              
```
## Requirements

- Python 3.x

  
## Installation 

```bash 
  git clone git@github.com:pranjaltimsina/DSA-project.git
  cd DSA-project
```

## Instructions to Use

```bash 
  python3 main.py <absolute_path_to_directory_of_choice>
```

**note:** if no path is defined, it defaults to _/home_ because if you aren't using Linux in 2021, are you even a koder?
## Peep this

https://user-images.githubusercontent.com/52796005/118361327-cce41980-b53f-11eb-8201-946c0659b361.mp4

## FAQ

#### Q: Which data structure have you used here? 

A: A trie is used to emulate the directory and store all the files, like so -  

![Linux Trie File Structure](https://thesagediary.files.wordpress.com/2018/09/linuxfile.png)


#### Q: How do you traverse the entire file structure?

A: Using depth first search, we traverse the structure to access all possible files.


#### Q: What is the fuzzy search algorithm?

A: Using a score with various complex bonuses, the fuzzy search algorithm finds you the optimum search results in a given index to return the best possible answers for the shortest queries.


#### Q: Who are y'all?

A: Pranjal Timsina - 20BDS0392  
&nbsp;&nbsp;&nbsp;&nbsp; Krish Chatterjie - 20BCE0516

## Contributors


<table>
<tr align="center">

<td>
Krish Chatterjie
<p align="center">
<img src = "https://avatars.githubusercontent.com/KrishChatterjie" width="150" height="150" alt="Krish Chatterjie">
</p>
<p align="center">
<a href = "https://github.com/KrishChatterjie"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="GitHub"/></a>
<a href = "https://www.linkedin.com/in/krish-chatterjie-3119661b6">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36" alt="LinkedIn"/>
</a>
</p>
</td>

<td>
Pranjal Timsina
<p align="center">
<img src = "https://avatars.githubusercontent.com/PranjalTimsina" width="150" height="150" alt="Pranjal Timsina">
</p>
<p align="center">
<a href = "https://github.com/PranjalTimsina"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="GitHub"/></a>
<a href = "https://www.linkedin.com/in/pranjal-timsina-605404204">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36" alt="LinkedIn"/>
</a>
</p>
</td>


</tr>
</table>
