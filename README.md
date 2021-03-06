# StarFire
<img src="./starfireLogo.jpg" alt="Logo" width="500"/>

**StarFire** is a semi-centralized P2P file sharing system that we developed based on @MeGaCrazy's work (thanks to them). **StarFire** is a centralized P2P file sharing system (based on the directory method) when the master node is normal. After the failure of the master node, **StarFire**'s working mode is transformed into a distributed P2P file sharing system.

# Idea
This is a *distributed computing course assignment* that my partner (@ZzzhangTtt, Zhangmeng) and I are working on developing a P2P file sharing system. A simple centralized P2P file-sharing system (based on the directory method) can affect performance if the master node fails. The basic idea is to increase the number of master nodes, but this can cause data consistency problems. To solve this problem, our idea is that **StarFire** is a standard, centralized P2P file sharing system when the master node is normal. Only the master node will send the **directory data** to each peer node every once in a while. After the master node failed, **StarFire** switched to a distributed P2P file system and continued to work.

# Usage
```
cd Use guidance
python3 Instructions.py
```
Following the instructions of this program, you can fully understand the **usage**, **functions** and **disadvantages** of *StarFire*. Because my English is not good (these statements are translated by Google), so the instructions are written in Chinese. Please use them in combination with the translation.


# limition
Due to the limitations of our ability, energy and time (we have so many courses), we could only finish the **StarFire**'s prototype and test the feasibility of our idea. If we have free time, we will improve **StarFire**'s performance in security, privacy and other aspects. But speed is not our focus, and we do not intend to optimize **StarFire**'s performance in speed.

# License
This program is issued, reproduced or used under the permission of **MIT**. Please indicate the source.