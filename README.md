<p align="center"><img width=30.5% src="https://github.com/joaoceron/new_dissector/blob/master/media/header.png"></p>




&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
[![Build Status](https://api.travis-ci.com/joaoceron/new_dissector.svg?token=8TMUECLCUVrxas7wXfVY&branch=master)](https://travis-ci.com/github/joaoceron/new_dissector)
[![GitHub Issues](https://img.shields.io/github/issues/ddos-clearing-house/ddos_dissector)](https://github.com/ddos-clearing-house/ddos_dissector/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
<img alt="GitHub commits since tagged version" src="https://img.shields.io/github/commits-since/ddos-clearing-house/ddos_dissector/3.0.0">

## Overview

DDos_Dissector is responsible for summarizing DDoS attack traffic from stored traffic (pcap/flows). The key point is to build a heuristic/algorithm that can find similarities in the analyzed network traffic. 

In order to improve software efficiency, we are working on software components that can parse specific DDoS attacks, such as amplification and TCP Syn flood attacks. 

<details>
  <summary>Input [PCAP]</summary>
  
  #### Network file PCAP
  https://www.simpleweb.org/wiki/index.php/Traces#Datasets_for_Booter_attacks
  
</details>

<details>
  <summary>Output [Fingerprint]</summary>
  
  #### Fingerprint generated
     
```json
  "ip_proto": [
    17
  ],
  "highest_protocol": [
    "DNS"
  ],
  "dns_qry_name": [
    "anonsc.com"
  ],
  "eth_type": [
    "0x00000800"
  ],
  "frame_len": [
    397
  ],
  "srcport": [
    53
  ],
  "fragmentation": [
    true
  ],
  "amplifiers": [
    "109.93.47.83",
  ],
  "start_time": "2020-08-08 21:36:23"
}
```
</details>


<!-- <p align="center"><img width=95% src="https://github.com/anfederico/Waldo/blob/master/media/Schematic.png"></p> -->

<br>

## Usage

<!-- <img src="https://github.com/anfederico/Clairvoyant/blob/master/media/Learning.gif" width=40%> -->

````

 _____  _____        _____ _____  ____
|  __ \|  __ \      / ____|  __ \|  _ \
| |  | | |  | | ___| (___ | |  | | |_) |
| |  | | |  | |/ _ \___ \| |  | |  _ <
| |__| | |__| | (_) |___) | |__| | |_) |
|_____/|_____/ \___/_____/|_____/|____/

optional arguments:
  -h, --help            show this help message and exit
  --version             print version and exit
  -v, --verbose         print info msg
  -d, --debug           print debug info
  -q, --quiet           ignore animation
  --status              ignore animation
  -s, --summary         ignore animation
  -u, --upload          upload to the selected repository
  --log [LOG]           Log filename. Default =./log.txt"
  --config [CONFIG]     Configuration File. Default =./log.txt"
  -g, --graph           build dot file (graphviz). It can be used to plot a visual representation
                         of the attack using the tool graphviz. When this option is set, youn will
                         received information how to convert the generate file (.dot) to image (.png).
  -f [FILENAME], --filename [FILENAME]

Example: ./new_dissector.py -f attack.pcap --summary --upload

Input file not provided. Use '-f' for that.
````

## Examples

<details>
  <summary>Generating fingerprints</summary>
 
   <p align="center"><img width=80% src="https://github.com/joaoceron/new_dissector/blob/master/media/dissector.gif"></p>

     
</details>



<details>
  <summary>Graphical visualization</summary>
  
- Green: benign traffic
- Red:  malicious traffic 
 
<p align="center"><img width=50% src="https://github.com/joaoceron/new_dissector/blob/master/media/booter6-chargen.jpg"></p>

</details>



