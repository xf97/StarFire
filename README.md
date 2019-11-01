# StarFile
**StarFile** is a semi-centralized P2P file sharing system that we developed based on A's work (thanks to them). **StarFile** is a centralized P2P file sharing system (based on the directory method) when the master node is normal. After the failure of the master node, **StarFile**'s working mode is transformed into a distributed P2P file sharing system.

# Idea
This is a *distributed computing course assignment* that my partner (A, B) and I are working on developing a P2P file sharing system. A simple centralized P2P file-sharing system (based on the directory method) can affect performance if the master node fails. The basic idea is to increase the number of master nodes, but this can cause data consistency problems. To solve this problem, our idea is that **StarFile** is a standard, centralized P2P file sharing system when the master node is normal. Only the master node will send the **directory data** to each peer node every once in a while. After the master node failed, **StarFile** switched to a distributed P2P file system and continued to work.

# limition