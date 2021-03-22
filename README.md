# Intraday-Stock-Screener
WORK IN PROGRESS



<!-- ABOUT THE PROJECT -->
## About The Project
Stock screener that scans the 100 most actively traded stocks of the day for the largest gainers within the users specified time interval. Can be used for daytrading, detecting irregular price action, or finding live breaking news if a company suddenly has a large gain. 
<br>
Data is pulled from https://www.barchart.com/stocks/most-active/daily-volume-leaders and the program's finished data will be displayed in output.txt
<br>
<br>
This program is meant to be used in addition to other tools and is **NOT financial advice.**


### Built With

* []()
* []()
* []()







<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```



<!-- USAGE EXAMPLES -->
## Usage

Program scrapes data for the top 100 most actively traded stocks of the day and updates with percent change after specified time interval
<br> 

<img width="1502" alt="Screen Shot 2021-01-12 at 12 19 15 PM" src="https://user-images.githubusercontent.com/69620469/111929284-26195a80-8a73-11eb-8b93-f886031c75de.png">

Outputs the top 10 biggest gainers into text file
<br> 


<img width="683" alt="Screen Shot 2021-01-12 at 12 20 14 PM" src="https://user-images.githubusercontent.com/69620469/111929216-f23e3500-8a72-11eb-8571-292bdd168d08.png">

If after the time interval, new stocks that were not in the original 100 have appeared the ticker will be listed as "new" along with its day's gain. This can be helpful for finding stocks that are breaking out as it can indicate a sudden spike in volume. 
<br> 

<img width="192" alt="Screen Shot 2021-01-12 at 12 29 16 PM" src="https://user-images.githubusercontent.com/69620469/111929303-39c4c100-8a73-11eb-96be-1d6ec5cf70b6.png">




## Current Issues


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Max Li - maxli9132@gmail.com

Project Link: [https://github.com/bruhjuice/Intraday-Stock-Screener](https://github.com/bruhjuice/Intraday-Stock-Screener)



