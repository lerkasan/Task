# Script printing RAM and CPU utilization, disk partitions info and processes info

## Overview

Script **metrics** prints RAM and CPU utilization, disk partitions info and processes info. The script accepts one or several arguments separated by spaces. These arguments instruct which metrics to print.

Available argument options:
- *ps* - prints info about processes
- *mem* - prints info about RAM and Swap usage
- *cpu* - prints info about CPU usage
- *disk* - prints info about partitions and disk space usage
- *self* - prints info about RAM and CPU resources used by this script

Wrong arguments are ignored.

## Argument usage examples

```bash
./metrics ps mem

./metrics cpu

./metrics ps cpu mem disk
```

## Prerequisites

In order to run this script you should have **Python 3** installed. You can get more information about Python 3 at [official website](https://docs.python.org/3/using/unix.html)
Also you should install **psutil library** according to this [guide](https://github.com/giampaolo/psutil/blob/master/INSTALL.rst).

If you want to try dockerized script you should have **Docker** installed. You can get more information about Docker installation [at official website](https://docs.docker.com/install/).

*Optional:* It's up to you whether you want to try running script via *docker-compose*. If so, you may read about *docker-compose* [installation](https://docs.docker.com/compose/install/).

## How to run this script

1. Download zip archive with source code from Github and unzip it or clone this repository using ```git clone```
You may need *git*. More information on *git* is available [here](https://git-scm.com/doc)
2. Go to folder *test_task_pro*
3. Run the script or Docker container from a command line with any available arguments: 
- script
```bash
./metrics ps mem
```
**OR**
- Docker container
```bash
./docker_run.sh ps mem
```
**OR**
- Docker container via *docker-compose*
```bash
docker-compose build
docker-compose run -e arguments="ps mem" metrics
```
4. *In case of using Docker:* Clean up - stop container, delete container and image. Also you may uncomment these lines at the end of *docker_run.sh* and omit this step, but in case of using *docker-compose* you may need this step anyway.
```bash
docker stop test_task_lerkasan
docker rm test_task_lerkasan
docker rmi $(docker images | grep 'test_task_lerkasan')
```
# Result output examples:

```
$ ./metrics mem

Memory usage:
Usage in:         bytes           MB        GB
total           16750182400     15974.22   15.60     
available       5879160832      5606.80    5.48      
used            11788554240     11242.44   10.98     
free            190750720       181.91     0.18      
active          11252891648     10731.59   10.48     
inactive        4406386688      4202.26    4.10      
buffers         283185152       270.07     0.26      
cached          4487692288      4279.80    4.18      
shared          226213888       215.73     0.21      
slab            418156544       398.79     0.39      
Usage in percent: 64.9                

Swap usage:
Usage in:         bytes           MB        GB
total           4094160896      3904.50    3.81      
used            3407872         3.25       0.00      
free            4090753024      3901.25    3.81      
sin             77824           0.07       0.00      
sout            2273280         2.17       0.00      
Usage in percent: 0.1                 
```

```
$ ./metrics cpu

CPU usage in percents:
user                 3.0                 
nice                 0.0                 
system               1.0                 
idle                 96.0                
iowait               0.0                 
irq                  0.0                 
softirq              0.0                 
steal                0.0                 
guest                0.0                 
guest_nice           0.0                 

CPU times in seconds:
user                 4538.24             
nice                 13.46               
system               1500.32             
idle                 221741.16           
iowait               356.63              
irq                  0.0                 
softirq              41.91               
steal                0.0                 
guest                0.0                 
guest_nice           0.0
```

```
$ ./metrics disk

Disk partitions:
device                       mountpoint                   fstype                       opts                         
/dev/sda3                    /                            ext4                         rw,relatime,errors=remount-ro,data=ordered    
/dev/sdb2                    /usr                         ext4                         rw,relatime,data=ordered     
/dev/sda3                    /var/lib/docker/plugins      ext4                         rw,relatime,errors=remount-ro,data=ordered    
/dev/sda3                    /var/lib/docker/aufs         ext4                         rw,relatime,errors=remount-ro,data=ordered    

Usage of partition: /
Usage in:         bytes           MB        GB
total           103629733888    98829.02   96.51     
used            90947604480     86734.39   84.70     
free            7373926400      7032.32    6.87      
Usage in percent: 92.5                

Usage of partition: /usr
Usage in:         bytes           MB        GB
total           514982985728    491126.05  479.62    
used            414555901952    395351.32  386.09    
free            74195959808     70758.78   69.10     
Usage in percent: 84.8                

Usage of partition: /var/lib/docker/plugins
Usage in:         bytes           MB        GB
total           103629733888    98829.02   96.51     
used            90947604480     86734.39   84.70     
free            7373926400      7032.32    6.87      
Usage in percent: 92.5                

Usage of partition: /var/lib/docker/aufs
Usage in:         bytes           MB        GB
total           103629733888    98829.02   96.51     
used            90947604480     86734.39   84.70     
free            7373926400      7032.32    6.87      
Usage in percent: 92.5                

I/O statistics:
read_count           169514              
write_count          187661              
read_bytes           4363459072          
write_bytes          5666017280          
read_time            622288              
write_time           529840              
read_merged_count    12009               
write_merged_count   150952              
busy_time            281888            
```

```
$ ./docker_run.sh ps

pid        user                      process                                  parent     status          started                   CPU %    RAM %    read bytes      written bytes   read MB         written MB     
1          root                      systemd                                  0          sleeping        11-05-2018 07:19:24       0.00     0.06     494194176       83304448        471.30          79.45          
2          root                      kthreadd                                 0          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
4          root                      kworker/0:0H                             2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
6          root                      mm_percpu_wq                             2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
7          root                      ksoftirqd/0                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
8          root                      rcu_sched                                2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
9          root                      rcu_bh                                   2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
10         root                      migration/0                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
11         root                      watchdog/0                               2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
12         root                      cpuhp/0                                  2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
13         root                      cpuhp/1                                  2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
14         root                      watchdog/1                               2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
15         root                      migration/1                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
16         root                      ksoftirqd/1                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
18         root                      kworker/1:0H                             2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
19         root                      cpuhp/2                                  2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
20         root                      watchdog/2                               2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
21         root                      migration/2                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
22         root                      ksoftirqd/2                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
24         root                      kworker/2:0H                             2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
25         root                      cpuhp/3                                  2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
26         root                      watchdog/3                               2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
27         root                      migration/3                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
28         root                      ksoftirqd/3                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
30         root                      kworker/3:0H                             2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
31         root                      cpuhp/4                                  2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
32         root                      watchdog/4                               2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
33         root                      migration/4                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
34         root                      ksoftirqd/4                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
36         root                      kworker/4:0H                             2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
37         root                      cpuhp/5                                  2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
38         root                      watchdog/5                               2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
39         root                      migration/5                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
40         root                      ksoftirqd/5                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
42         root                      kworker/5:0H                             2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
43         root                      cpuhp/6                                  2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
44         root                      watchdog/6                               2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
45         root                      migration/6                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
46         root                      ksoftirqd/6                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
48         root                      kworker/6:0H                             2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
49         root                      cpuhp/7                                  2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
50         root                      watchdog/7                               2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
51         root                      migration/7                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
52         root                      ksoftirqd/7                              2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
54         root                      kworker/7:0H                             2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
55         root                      kdevtmpfs                                2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
56         root                      netns                                    2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
57         root                      rcu_tasks_kthre                          2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
58         root                      kauditd                                  2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
61         root                      khungtaskd                               2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
62         root                      oom_reaper                               2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
63         root                      writeback                                2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
64         root                      kcompactd0                               2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
65         root                      ksmd                                     2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
66         root                      khugepaged                               2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
67         root                      crypto                                   2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
68         root                      kintegrityd                              2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
69         root                      kblockd                                  2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
76         root                      ata_sff                                  2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
77         root                      md                                       2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
78         root                      edac-poller                              2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
79         root                      devfreq_wq                               2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
80         root                      watchdogd                                2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
83         root                      kswapd0                                  2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
84         root                      ecryptfs-kthrea                          2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
126        root                      kthrotld                                 2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
127        root                      acpi_thermal_pm                          2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
131        root                      ipv6_addrconf                            2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
140        root                      kstrp                                    2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
157        root                      charger_manager                          2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
215        root                      nvidia-modeset                           2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
216        root                      scsi_eh_0                                2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
217        root                      scsi_tmf_0                               2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
218        root                      scsi_eh_1                                2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
219        root                      scsi_tmf_1                               2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
220        root                      scsi_eh_2                                2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
221        root                      scsi_tmf_2                               2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
222        root                      scsi_eh_3                                2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
223        root                      scsi_tmf_3                               2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
224        root                      scsi_eh_4                                2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
225        root                      scsi_tmf_4                               2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
226        root                      scsi_eh_5                                2          sleeping        11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
227        root                      scsi_tmf_5                               2          ?               11-05-2018 07:19:24       0.00     0.00     0               0               0.00            0.00           
238        root                      kworker/1:1H                             2          ?               11-05-2018 07:19:25       0.00     0.00     0               0               0.00            0.00           
307        root                      raid5wq                                  2          ?               11-05-2018 07:19:26       0.00     0.00     0               0               0.00            0.00           
352        root                      kworker/4:1H                             2          ?               11-05-2018 07:19:30       0.00     0.00     0               0               0.00            0.00           
353        root                      kworker/2:1H                             2          ?               11-05-2018 07:19:30       0.00     0.00     0               0               0.00            0.00           
545        root                      jbd2/sda3-8                              2          sleeping        11-05-2018 07:19:58       0.00     0.00     0               288329728       0.00            274.97         
546        root                      ext4-rsv-conver                          2          ?               11-05-2018 07:19:58       0.00     0.00     0               0               0.00            0.00           
560        root                      jbd2/sdb2-8                              2          sleeping        11-05-2018 07:19:58       0.00     0.00     0               19341312        0.00            18.45          
561        root                      ext4-rsv-conver                          2          ?               11-05-2018 07:19:58       0.00     0.00     0               0               0.00            0.00           
599        root                      systemd-journald                         1          sleeping        11-05-2018 07:19:59       0.00     0.30     31641600        79355904        30.18           75.68          
610        root                      kworker/6:1H                             2          ?               11-05-2018 07:19:59       0.00     0.00     0               0               0.00            0.00           
617        root                      kworker/3:1H                             2          ?               11-05-2018 07:19:59       0.00     0.00     0               0               0.00            0.00           
626        root                      kworker/7:1H                             2          ?               11-05-2018 07:19:59       0.00     0.00     0               0               0.00            0.00           
635        root                      lvmetad                                  1          sleeping        11-05-2018 07:19:59       0.00     0.01     86016           0               0.08            0.00           
638        root                      rpciod                                   2          ?               11-05-2018 07:19:59       0.00     0.00     0               0               0.00            0.00           
639        root                      xprtiod                                  2          ?               11-05-2018 07:19:59       0.00     0.00     0               0               0.00            0.00           
643        root                      systemd-udevd                            1          sleeping        11-05-2018 07:19:59       0.00     0.04     44336128        0               42.28           0.00           
675        root                      kworker/5:1H                             2          ?               11-05-2018 07:19:59       0.00     0.00     0               0               0.00            0.00           
680        root                      UVM global queu                          2          sleeping        11-05-2018 07:20:00       0.00     0.00     0               0               0.00            0.00           
681        root                      UVM Tools Event                          2          sleeping        11-05-2018 07:20:00       0.00     0.00     0               0               0.00            0.00           
684        root                      irq/128-mei_me                           2          sleeping        11-05-2018 07:20:00       0.00     0.00     0               0               0.00            0.00           
697        root                      blkmapd                                  1          sleeping        11-05-2018 07:20:00       0.00     0.00     0               0               0.00            0.00           
959        systemd-timesync          systemd-timesyncd                        1          sleeping        11-05-2018 07:20:02       0.00     0.02     45056           0               0.04            0.00           
961        systemd-resolve           systemd-resolved                         1          sleeping        11-05-2018 07:20:02       0.00     0.04     0               0               0.00            0.00           
962        root                      rpcbind                                  1          sleeping        11-05-2018 07:20:02       0.00     0.02     1257472         0               1.20            0.00           
965        root                      kworker/0:1H                             2          ?               11-05-2018 07:20:02       0.00     0.00     0               0               0.00            0.00           
1000       root                      rpc.idmapd                               1          sleeping        11-05-2018 07:20:02       0.00     0.00     0               0               0.00            0.00           
1179       root                      kdmflush                                 2          ?               11-05-2018 07:20:02       0.00     0.00     0               0               0.00            0.00           
1186       root                      bioset                                   2          ?               11-05-2018 07:20:02       0.00     0.00     0               0               0.00            0.00           
1187       root                      kcryptd_io                               2          ?               11-05-2018 07:20:02       0.00     0.00     0               0               0.00            0.00           
1189       root                      kcryptd                                  2          ?               11-05-2018 07:20:02       0.00     0.00     0               0               0.00            0.00           
1190       root                      dmcrypt_write                            2          sleeping        11-05-2018 07:20:02       0.00     0.00     0               0               0.00            0.00           
1191       root                      bioset                                   2          ?               11-05-2018 07:20:02       0.00     0.00     0               0               0.00            0.00           
1212       root                      systemd-logind                           1          sleeping        11-05-2018 07:20:03       0.00     0.04     0               0               0.00            0.00           
1213       root                      thermald                                 1          sleeping        11-05-2018 07:20:03       0.00     0.06     4431872         0               4.23            0.00           
1214       root                      accounts-daemon                          1          sleeping        11-05-2018 07:20:03       0.00     0.04     1511424         0               1.44            0.00           
1221       root                      udisksd                                  1          sleeping        11-05-2018 07:20:03       0.00     0.07     3284992         0               3.13            0.00           
1224       root                      ModemManager                             1          sleeping        11-05-2018 07:20:03       0.00     0.06     3960832         0               3.78            0.00           
1229       root                      cron                                     1          sleeping        11-05-2018 07:20:03       0.00     0.02     122880          0               0.12            0.00           
1230       root                      networkd-dispat                          1          sleeping        11-05-2018 07:20:03       0.00     0.10     7942144         0               7.57            0.00           
1232       messagebus                dbus-daemon                              1          sleeping        11-05-2018 07:20:03       0.00     0.04     1892352         0               1.80            0.00           
1341       root                      acpid                                    1          sleeping        11-05-2018 07:20:05       0.00     0.01     86016           0               0.08            0.00           
1342       avahi                     avahi-daemon                             1          sleeping        11-05-2018 07:20:05       0.00     0.02     425984          0               0.41            0.00           
1347       root                      wpa_supplicant                           1          sleeping        11-05-2018 07:20:05       0.00     0.03     1695744         0               1.62            0.00           
1361       root                      irqbalance                               1          sleeping        11-05-2018 07:20:05       0.00     0.02     110592          0               0.11            0.00           
1364       root                      snapd                                    1          sleeping        11-05-2018 07:20:05       0.00     0.11     15126528        0               14.43           0.00           
1369       root                      NetworkManager                           1          sleeping        11-05-2018 07:20:05       0.00     0.09     4685824         20480           4.47            0.02           
1374       syslog                    rsyslogd                                 1          sleeping        11-05-2018 07:20:05       0.00     0.03     897024          2428928         0.86            2.32           
1391       colord                    colord                                   1          sleeping        11-05-2018 07:20:05       0.00     0.09     14237696        0               13.58           0.00           
1424       avahi                     avahi-daemon                             1342       sleeping        11-05-2018 07:20:05       0.00     0.00     0               0               0.00            0.00           
1501       root                      polkitd                                  1          sleeping        11-05-2018 07:20:06       0.00     0.06     2252800         0               2.15            0.00           
1670       mpd                       mpd                                      1          sleeping        11-05-2018 07:20:10       0.00     0.22     31563776        4096            30.10           0.00           
1738       root                      rpc.mountd                               1          sleeping        11-05-2018 07:20:10       0.00     0.00     0               0               0.00            0.00           
1784       root                      lockd                                    2          sleeping        11-05-2018 07:20:11       0.00     0.00     0               0               0.00            0.00           
1786       root                      nfsd                                     2          sleeping        11-05-2018 07:20:11       0.00     0.00     0               0               0.00            0.00           
1787       root                      nfsd                                     2          sleeping        11-05-2018 07:20:11       0.00     0.00     0               0               0.00            0.00           
1788       root                      nfsd                                     2          sleeping        11-05-2018 07:20:11       0.00     0.00     0               0               0.00            0.00           
1789       root                      nfsd                                     2          sleeping        11-05-2018 07:20:11       0.00     0.00     0               0               0.00            0.00           
1790       root                      nfsd                                     2          sleeping        11-05-2018 07:20:11       0.00     0.00     0               0               0.00            0.00           
1791       root                      nfsd                                     2          sleeping        11-05-2018 07:20:11       0.00     0.00     0               0               0.00            0.00           
1792       root                      nfsd                                     2          sleeping        11-05-2018 07:20:11       0.00     0.00     0               0               0.00            0.00           
1793       root                      nfsd                                     2          sleeping        11-05-2018 07:20:11       0.00     0.00     0               0               0.00            0.00           
1825       root                      sddm                                     1          sleeping        11-05-2018 07:20:11       0.00     0.08     68792320        126976          65.61           0.12           
1889       root                      Xorg                                     1825       sleeping        11-05-2018 07:20:13       0.00     1.67     29151232        139264          27.80           0.13           
1894       mysql                     mysqld                                   1          sleeping        11-05-2018 07:20:13       0.00     1.08     14364672        13242368        13.70           12.63          
1914       root                      esets_daemon                             1          sleeping        11-05-2018 07:20:14       0.00     0.75     0               0               0.00            0.00           
1915       root                      esets_daemon                             1914       sleeping        11-05-2018 07:20:14       0.00     1.19     1353785344      904957952       1291.07         863.04         
1916       root                      esets_mac                                1914       sleeping        11-05-2018 07:20:14       0.00     0.03     0               0               0.00            0.00           
1946       root                      dhclient                                 1369       sleeping        11-05-2018 07:20:14       0.00     0.04     2060288         90112           1.96            0.09           
1976       nvidia-persistenced       nvidia-persistenced                      1          sleeping        11-05-2018 07:20:16       0.00     0.01     192512          0               0.18            0.00           
1982       root                      irq/130-nvidia                           2          sleeping        11-05-2018 07:20:16       0.00     0.00     0               0               0.00            0.00           
1983       root                      nvidia                                   2          sleeping        11-05-2018 07:20:16       0.00     0.00     0               0               0.00            0.00           
2028       whoopsie                  whoopsie                                 1          sleeping        11-05-2018 07:20:17       0.00     0.06     466944          4096            0.45            0.00           
2029       root                      dockerd                                  1          sleeping        11-05-2018 07:20:17       0.00     0.46     145252352       191885312       138.52          183.00         
2091       kernoops                  kerneloops                               1          sleeping        11-05-2018 07:20:17       0.00     0.02     0               0               0.00            0.00           
2099       root                      vpnagentd                                1          sleeping        11-05-2018 07:20:17       0.00     0.09     135168          4096            0.13            0.00           
2103       kernoops                  kerneloops                               1          sleeping        11-05-2018 07:20:17       0.00     0.00     0               0               0.00            0.00           
2124       root                      teamviewerd                              1          sleeping        11-05-2018 07:20:18       0.00     0.06     909312          24576           0.87            0.02           
2143       root                      iprt-VBoxWQueue                          2          ?               11-05-2018 07:20:18       0.00     0.00     0               0               0.00            0.00           
2147       root                      iprt-VBoxTscThr                          2          sleeping        11-05-2018 07:20:18       0.00     0.00     0               0               0.00            0.00           
2280       root                      docker-containerd                        2029       sleeping        11-05-2018 07:20:20       0.00     0.15     29057024        205549568       27.71           196.03         
2295       sddm                      systemd                                  1          sleeping        11-05-2018 07:20:21       0.00     0.05     593920          0               0.57            0.00           
2297       sddm                      (sd-pam)                                 2295       sleeping        11-05-2018 07:20:21       0.00     0.02     0               0               0.00            0.00           
2542       sddm                      dbus-launch                              1          sleeping        11-05-2018 07:20:25       0.00     0.01     0               0               0.00            0.00           
2544       sddm                      dbus-daemon                              1          sleeping        11-05-2018 07:20:25       0.00     0.02     0               0               0.00            0.00           
2548       root                      upowerd                                  1          sleeping        11-05-2018 07:20:27       0.00     0.04     647168          0               0.62            0.00           
2604       root                      sddm-helper                              1825       sleeping        11-05-2018 07:20:40       0.00     0.08     1908736         0               1.82            0.00           
2621       lerkasan                  systemd                                  1          sleeping        11-05-2018 07:20:40       0.00     0.05     16384           0               0.02            0.00           
2628       lerkasan                  (sd-pam)                                 2621       sleeping        11-05-2018 07:20:40       0.00     0.02     0               0               0.00            0.00           
2645       lerkasan                  kwalletd5                                1          sleeping        11-05-2018 07:20:40       0.00     0.36     1232896         24576           1.18            0.02           
2646       lerkasan                  startkde                                 2604       sleeping        11-05-2018 07:20:40       0.00     0.01     19587072        598016          18.68           0.57           
2714       lerkasan                  dbus-launch                              1          sleeping        11-05-2018 07:20:42       0.00     0.01     0               0               0.00            0.00           
2715       lerkasan                  dbus-daemon                              1          sleeping        11-05-2018 07:20:42       0.00     0.03     131072          0               0.12            0.00           
2729       lerkasan                  ssh-agent                                2646       sleeping        11-05-2018 07:20:42       0.00     0.00     0               0               0.00            0.00           
2766       lerkasan                  start_kdeinit                            1          sleeping        11-05-2018 07:20:43       0.00     0.00     0               0               0.00            0.00           
2772       lerkasan                  kdeinit5                                 1          sleeping        11-05-2018 07:20:43       0.00     0.12     422039552       283877376       402.49          270.73         
2773       lerkasan                  klauncher                                2772       sleeping        11-05-2018 07:20:43       0.00     0.22     647168          0               0.62            0.00           
2776       lerkasan                  kded5                                    2772       sleeping        11-05-2018 07:20:44       0.00     1.13     18939904        4120576         18.06           3.93           
2783       lerkasan                  kaccess                                  2772       sleeping        11-05-2018 07:20:44       0.00     0.22     94208           0               0.09            0.00           
2789       lerkasan                  kglobalaccel5                            1          sleeping        11-05-2018 07:20:44       0.00     0.22     163840          45056           0.16            0.04           
2794       lerkasan                  dconf-service                            1          sleeping        11-05-2018 07:20:44       0.00     0.03     8192            12288           0.01            0.01           
2805       lerkasan                  kwrapper5                                2646       sleeping        11-05-2018 07:20:45       0.00     0.04     0               0               0.00            0.00           
2806       lerkasan                  ksmserver                                2772       sleeping        11-05-2018 07:20:45       0.00     0.26     5046272         1269760         4.81            1.21           
2809       lerkasan                  kwin_x11                                 2806       sleeping        11-05-2018 07:20:45       0.00     0.39     9777152         151552          9.32            0.14           
2813       lerkasan                  baloo_file                               1          sleeping        11-05-2018 07:20:45       0.00     0.54     103153664       690360320       98.38           658.38         
2816       lerkasan                  krunner                                  1          sleeping        11-05-2018 07:20:46       0.00     0.48     3452928         299008          3.29            0.29           
2819       lerkasan                  kactivitymanagerd                        1          sleeping        11-05-2018 07:20:46       0.00     0.16     5292032         516096          5.05            0.49           
2832       lerkasan                  plasmashell                              1          sleeping        11-05-2018 07:20:46       0.00     2.56     165666816       27631616        157.99          26.35          
2834       lerkasan                  polkit-kde-authentication-agent-1        1          sleeping        11-05-2018 07:20:46       0.00     0.24     200704          0               0.19            0.00           
2836       lerkasan                  xembedsniproxy                           1          sleeping        11-05-2018 07:20:46       0.00     0.12     32768           0               0.03            0.00           
2853       lerkasan                  kdeconnectd                              1          sleeping        11-05-2018 07:20:46       0.00     0.26     1929216         8192            1.84            0.01           
2871       lerkasan                  org_kde_powerdevil                       2772       sleeping        11-05-2018 07:20:47       0.00     0.22     1486848         163840          1.42            0.16           
2881       lerkasan                  pulseaudio                               1          sleeping        11-05-2018 07:20:48       0.00     0.08     1814528         24576           1.73            0.02           
2882       lerkasan                  kleopatra                                2772       sleeping        11-05-2018 07:20:48       0.00     0.42     9908224         32768           9.45            0.03           
2884       rtkit                     rtkit-daemon                             1          sleeping        11-05-2018 07:20:48       0.00     0.02     69632           0               0.07            0.00           
2907       lerkasan                  mission-control-5                        1          sleeping        11-05-2018 07:20:49       0.00     0.08     3067904         0               2.93            0.00           
2911       lerkasan                  kscreen_backend_launcher                 1          sleeping        11-05-2018 07:20:49       0.00     0.11     61440           0               0.06            0.00           
2938       lerkasan                  at-spi-bus-launcher                      1          sleeping        11-05-2018 07:20:51       0.00     0.04     0               0               0.00            0.00           
2940       lerkasan                  skypeforlinux                            1          sleeping        11-05-2018 07:20:51       0.00     0.59     84586496        1736704         80.67           1.66           
2946       lerkasan                  dbus-daemon                              2938       sleeping        11-05-2018 07:20:51       0.00     0.03     12288           0               0.01            0.00           
2967       lerkasan                  esets_gui                                1          sleeping        11-05-2018 07:20:51       0.00     0.42     7225344         0               6.89            0.00           
2976       lerkasan                  at-spi2-registryd                        1          sleeping        11-05-2018 07:20:52       0.00     0.04     196608          0               0.19            0.00           
2990       lerkasan                  gconf-helper                             2881       sleeping        11-05-2018 07:20:54       0.00     0.04     4096            0               0.00            0.00           
2993       lerkasan                  gconfd-2                                 1          sleeping        11-05-2018 07:20:54       0.00     0.04     180224          8192            0.17            0.01           
3050       lerkasan                  skypeforlinux                            2940       sleeping        11-05-2018 07:20:59       0.00     0.18     2338816         0               2.23            0.00           
3055       lerkasan                  gpg-agent                                2621       sleeping        11-05-2018 07:20:59       0.00     0.01     0               0               0.00            0.00           
3066       lerkasan                  obexd                                    1          sleeping        11-05-2018 07:21:00       0.00     0.04     909312          0               0.87            0.00           
3091       lerkasan                  skypeforlinux                            2940       sleeping        11-05-2018 07:21:04       0.00     0.51     1724416         16384           1.64            0.02           
3101       lerkasan                  skypeforlinux                            3050       sleeping        11-05-2018 07:21:05       0.00     1.42     44572672        16384           42.51           0.02           
3156       lerkasan                  ksysguardd                               2832       sleeping        11-05-2018 07:21:15       0.00     0.02     81920           0               0.08            0.00           
3167       lerkasan                  kuiserver5                               1          sleeping        11-05-2018 07:21:19       0.00     0.22     184320          4096            0.18            0.00           
3175       root                      packagekitd                              1          sleeping        11-05-2018 07:21:22       0.00     0.21     107618304       251432960       102.63          239.79         
3213       lerkasan                  chrome                                   2772       sleeping        11-05-2018 07:21:52       0.00     2.39     400777216       2048720896      382.21          1953.81        
3218       lerkasan                  cat                                      3213       sleeping        11-05-2018 07:21:52       0.00     0.01     0               0               0.00            0.00           
3219       lerkasan                  cat                                      3213       sleeping        11-05-2018 07:21:52       0.00     0.01     0               12288           0.00            0.01           
3222       lerkasan                  chrome                                   3213       sleeping        11-05-2018 07:21:52       0.00     0.32     25096192        0               23.93           0.00           
3223       lerkasan                  nacl_helper                              3222       sleeping        11-05-2018 07:21:52       0.00     0.03     1425408         0               1.36            0.00           
3226       lerkasan                  chrome                                   3222       sleeping        11-05-2018 07:21:52       0.00     0.09     38137856        0               36.37           0.00           
3251       lerkasan                  chrome                                   3213       sleeping        11-05-2018 07:21:52       0.00     2.22     4960256         282624          4.73            0.27           
3286       lerkasan                  chrome                                   3251       sleeping        11-05-2018 07:21:53       0.00     0.14     0               0               0.00            0.00           
3432       lerkasan                  chrome                                   3226       sleeping        11-05-2018 07:21:56       0.00     0.45     192512          0               0.18            0.00           
3449       lerkasan                  chrome                                   3226       sleeping        11-05-2018 07:21:56       0.00     0.78     24576           0               0.02            0.00           
3456       lerkasan                  chrome                                   3226       sleeping        11-05-2018 07:21:56       0.00     0.53     0               0               0.00            0.00           
3474       lerkasan                  chrome                                   3226       sleeping        11-05-2018 07:21:56       0.00     0.67     131072          0               0.12            0.00           
3598       lerkasan                  chrome                                   3226       sleeping        11-05-2018 07:22:02       0.00     0.89     0               0               0.00            0.00           
3667       lerkasan                  chrome                                   3226       sleeping        11-05-2018 07:22:09       0.00     3.15     2564096         0               2.45            0.00           
3701       lerkasan                  chrome                                   3226       sleeping        11-05-2018 07:22:13       0.00     0.67     0               0               0.00            0.00           
3774       lerkasan                  dolphin                                  2772       sleeping        11-05-2018 07:22:50       0.00     0.55     4890624         483328          4.66            0.46           
3801       root                      update-apt-xapi                          1          sleeping        11-05-2018 07:23:59       0.00     0.11     266452992       165679104       254.11          158.00         
4053       root                      cupsd                                    1          sleeping        11-05-2018 07:25:04       0.00     0.17     688128          14512128        0.66            13.84          
4055       root                      cups-browsed                             1          sleeping        11-05-2018 07:25:04       0.00     0.07     77824           24576           0.07            0.02           
4091       lp                        dbus                                     4053       sleeping        11-05-2018 07:25:04       0.00     0.03     0               0               0.00            0.00           
4126       lp                        dbus                                     4053       sleeping        11-05-2018 07:25:05       0.00     0.04     0               0               0.00            0.00           
4766       lerkasan                  chrome                                   3226       sleeping        11-05-2018 07:27:56       0.00     0.16     0               163840          0.00            0.16           
4942       lerkasan                  chrome                                   3226       sleeping        11-05-2018 07:40:04       0.00     0.75     0               0               0.00            0.00           
5269       lerkasan                  thunderbird                              2772       sleeping        11-05-2018 08:01:26       0.00     2.13     123801600       85839872        118.07          81.86          
5361       lerkasan                  oosplash                                 5269       sleeping        11-05-2018 08:02:29       0.00     0.04     0               0               0.00            0.00           
5379       lerkasan                  soffice.bin                              5361       sleeping        11-05-2018 08:02:29       0.00     12.86    165707776       638730240       158.03          609.14         
5419       lerkasan                  kdeinit4                                 1          sleeping        11-05-2018 08:02:41       0.00     0.08     3878912         905216          3.70            0.86           
5422       lerkasan                  klauncher                                5419       sleeping        11-05-2018 08:02:41       0.00     0.11     86016           0               0.08            0.00           
5424       lerkasan                  kded4                                    1          sleeping        11-05-2018 08:02:41       0.00     0.16     126976          24576           0.12            0.02           
5503       lerkasan                  chrome                                   3226       sleeping        11-05-2018 08:04:48       0.00     3.48     2445312         0               2.33            0.00           
5615       lerkasan                  chrome                                   3226       sleeping        11-05-2018 08:05:32       0.00     1.06     868352          0               0.83            0.00           
5774       lerkasan                  chrome                                   3226       sleeping        11-05-2018 08:09:12       0.00     0.91     65536           0               0.06            0.00           
6758       lerkasan                  chrome                                   3226       sleeping        11-05-2018 09:05:01       0.00     2.00     851968          0               0.81            0.00           
6886       lerkasan                  chrome                                   3226       sleeping        11-05-2018 09:07:49       0.00     1.07     0               0               0.00            0.00           
6942       lerkasan                  kate                                     2832       sleeping        11-05-2018 09:08:42       0.00     0.51     6635520         86016           6.33            0.08           
7765       root                      kworker/4:0                              2          ?               11-05-2018 09:36:22       0.00     0.00     0               0               0.00            0.00           
7805       lerkasan                  chrome                                   3226       sleeping        11-05-2018 09:37:09       0.00     1.12     393216          0               0.38            0.00           
7902       lerkasan                  chrome                                   3226       sleeping        11-05-2018 09:38:35       0.00     3.44     0               0               0.00            0.00           
8521       lerkasan                  chrome                                   3226       sleeping        11-05-2018 10:00:40       0.00     0.94     0               0               0.00            0.00           
8988       root                      kworker/2:2                              2          ?               11-05-2018 10:15:59       0.00     0.00     0               0               0.00            0.00           
9342       lerkasan                  chrome                                   3226       sleeping        11-05-2018 10:21:19       0.00     2.50     385024          0               0.37            0.00           
9427       lerkasan                  chrome                                   3226       sleeping        11-05-2018 10:22:34       0.00     2.16     0               0               0.00            0.00           
9783       lerkasan                  baloorunner                              1          sleeping        11-05-2018 10:32:05       0.00     0.27     2764800         4096            2.64            0.00           
9807       lerkasan                  kcalc                                    2832       sleeping        11-05-2018 10:32:11       0.00     0.36     573440          86016           0.55            0.08           
10153      lerkasan                  chrome                                   3226       sleeping        11-05-2018 10:43:54       0.00     0.35     2523136         0               2.41            0.00           
10172      lerkasan                  chrome                                   3226       sleeping        11-05-2018 10:44:30       0.00     0.89     0               0               0.00            0.00           
10561      lerkasan                  chrome                                   3226       sleeping        11-05-2018 10:59:03       0.00     1.86     0               0               0.00            0.00           
10861      lerkasan                  chrome                                   3226       sleeping        11-05-2018 11:02:36       0.00     1.20     0               0               0.00            0.00           
10915      lerkasan                  chrome                                   3226       sleeping        11-05-2018 11:02:43       0.00     1.06     0               0               0.00            0.00           
11647      lerkasan                  dolphin                                  2772       sleeping        11-05-2018 11:21:33       0.00     0.61     745472          495616          0.71            0.47           
11840      lerkasan                  chrome                                   3226       sleeping        11-05-2018 11:24:34       0.00     1.48     262144          0               0.25            0.00           
12021      lerkasan                  chrome                                   3226       sleeping        11-05-2018 11:27:40       0.00     1.37     172032          0               0.16            0.00           
12057      root                      kworker/1:0                              2          ?               11-05-2018 11:27:40       0.00     0.00     0               0               0.00            0.00           
14138      root                      kworker/6:2                              2          ?               11-05-2018 13:00:51       0.00     0.00     0               8192            0.00            0.01           
14585      root                      kworker/7:2                              2          ?               11-05-2018 13:24:07       0.00     0.00     0               0               0.00            0.00           
14685      lerkasan                  chrome                                   3226       sleeping        11-05-2018 13:27:20       0.00     1.20     0               0               0.00            0.00           
14707      root                      kworker/0:1                              2          ?               11-05-2018 13:27:22       0.00     0.00     0               0               0.00            0.00           
15246      root                      kworker/4:2                              2          ?               11-05-2018 13:52:00       0.00     0.00     0               0               0.00            0.00           
15446      root                      kworker/1:2                              2          ?               11-05-2018 14:01:10       0.00     0.00     0               0               0.00            0.00           
15957      lerkasan                  chrome                                   3226       sleeping        11-05-2018 14:22:25       0.00     1.34     0               0               0.00            0.00           
15974      root                      kworker/7:3                              2          ?               11-05-2018 14:22:25       0.00     0.00     0               0               0.00            0.00           
15995      lerkasan                  chrome                                   3226       sleeping        11-05-2018 14:22:39       0.00     1.35     0               0               0.00            0.00           
16526      root                      kworker/3:0                              2          ?               11-05-2018 14:46:38       0.00     0.00     0               0               0.00            0.00           
16542      lerkasan                  chrome                                   3226       sleeping        11-05-2018 14:47:03       0.00     1.72     61440           0               0.06            0.00           
16964      lerkasan                  chrome                                   3226       sleeping        11-05-2018 14:55:16       0.00     1.63     0               0               0.00            0.00           
16999      root                      kworker/0:0                              2          ?               11-05-2018 14:55:34       0.00     0.00     0               0               0.00            0.00           
17008      lerkasan                  chrome                                   3226       sleeping        11-05-2018 14:55:40       0.00     1.60     0               0               0.00            0.00           
17034      lerkasan                  chrome                                   3226       sleeping        11-05-2018 14:55:46       0.00     1.20     0               0               0.00            0.00           
17057      lerkasan                  chrome                                   3226       sleeping        11-05-2018 14:55:48       0.00     1.18     0               0               0.00            0.00           
17318      root                      kworker/2:1                              2          ?               11-05-2018 14:58:21       0.00     0.00     0               0               0.00            0.00           
17541      root                      kworker/5:2                              2          ?               11-05-2018 14:59:18       0.00     0.00     0               0               0.00            0.00           
17659      lerkasan                  chrome                                   3226       sleeping        11-05-2018 15:01:23       0.00     0.67     0               0               0.00            0.00           
17680      root                      kworker/3:1                              2          ?               11-05-2018 15:01:25       0.00     0.00     0               0               0.00            0.00           
17681      lerkasan                  chrome                                   3226       sleeping        11-05-2018 15:01:25       0.00     0.69     589824          0               0.56            0.00           
17846      lerkasan                  chrome                                   3226       sleeping        11-05-2018 15:03:20       0.00     1.50     0               0               0.00            0.00           
18223      lerkasan                  pycharm.sh                               1          sleeping        11-05-2018 15:07:46       0.00     0.01     0               135168          0.00            0.13           
18292      lerkasan                  java                                     18223      sleeping        11-05-2018 15:07:47       0.00     7.47     62656512        147968000       59.75           141.11         
18330      lerkasan                  fsnotifier64                             18292      sleeping        11-05-2018 15:07:49       0.00     0.02     0               0               0.00            0.00           
18502      lerkasan                  konsole                                  2772       sleeping        11-05-2018 15:10:22       0.00     0.50     9629696         200704          9.18            0.19           
18506      lerkasan                  bash                                     18502      sleeping        11-05-2018 15:10:24       0.00     0.04     70057984        175755264       66.81           167.61         
18631      root                      kworker/u16:1                            2          ?               11-05-2018 15:12:28       0.00     0.00     0               10952704        0.00            10.45          
19680      root                      kworker/u17:2                            2          ?               11-05-2018 15:21:21       0.00     0.00     0               0               0.00            0.00           
19683      root                      kworker/u16:3                            2          ?               11-05-2018 15:21:31       0.00     0.00     1069056         11608064        1.02            11.07          
19865      lerkasan                  chrome                                   3226       sleeping        11-05-2018 15:26:51       0.00     1.48     0               0               0.00            0.00           
19920      lerkasan                  chrome                                   3226       sleeping        11-05-2018 15:26:54       0.00     1.55     1232896         0               1.18            0.00           
19945      lerkasan                  chrome                                   3226       sleeping        11-05-2018 15:26:55       0.00     1.37     335872          0               0.32            0.00           
20270      root                      kworker/u17:1                            2          ?               11-05-2018 15:34:20       0.00     0.00     0               0               0.00            0.00           
20569      root                      kworker/6:0                              2          ?               11-05-2018 15:40:08       0.00     0.00     0               0               0.00            0.00           
20754      root                      kworker/u17:0                            2          ?               11-05-2018 15:42:30       0.00     0.00     0               0               0.00            0.00           
20765      lerkasan                  chrome                                   3226       sleeping        11-05-2018 15:42:32       0.00     1.40     704512          0               0.67            0.00           
20792      root                      kworker/5:0                              2          ?               11-05-2018 15:42:44       0.00     0.00     0               0               0.00            0.00           
21091      root                      kworker/u16:2                            2          ?               11-05-2018 15:48:23       0.00     0.00     4096            1339392         0.00            1.28           
21173      root                      kworker/u17:3                            2          ?               11-05-2018 15:50:33       0.00     0.00     0               0               0.00            0.00           
21174      root                      kworker/u17:4                            2          ?               11-05-2018 15:50:33       0.00     0.00     0               0               0.00            0.00           
21251      lerkasan                  chrome                                   3226       sleeping        11-05-2018 15:51:53       0.00     1.33     0               0               0.00            0.00           
21273      root                      kworker/5:1                              2          ?               11-05-2018 15:52:01       0.00     0.00     0               0               0.00            0.00           
21332      root                      sudo                                     18506      sleeping        11-05-2018 15:52:52       0.00     0.03     0               0               0.00            0.00           
21333      root                      bash                                     21332      sleeping        11-05-2018 15:52:52       0.00     0.04     89264128        345952256       85.13           329.93         
21349      root                      kworker/u17:5                            2          ?               11-05-2018 15:52:56       0.00     0.00     0               0               0.00            0.00           
21916      root                      kworker/u17:6                            2          ?               11-05-2018 15:53:30       0.00     0.00     0               0               0.00            0.00           
22278      root                      kworker/2:0                              2          ?               11-05-2018 15:54:35       0.00     0.00     0               0               0.00            0.00           
23517      root                      bash                                     21333      sleeping        11-05-2018 15:55:30       0.00     0.02     471040          0               0.45            0.00           
23658      root                      kworker/u16:0                            2          ?               11-05-2018 15:55:39       0.00     0.00     0               0               0.00            0.00           
23707      root                      kworker/3:2                              2          ?               11-05-2018 15:55:44       0.00     0.00     0               0               0.00            0.00           
23729      root                      kworker/0:2                              2          ?               11-05-2018 15:55:45       0.00     0.00     0               0               0.00            0.00           
23939      root                      kworker/7:0                              2          ?               11-05-2018 15:55:49       0.00     0.00     0               0               0.00            0.00           
23951      root                      kworker/1:1                              2          ?               11-05-2018 15:55:49       0.00     0.00     0               0               0.00            0.00           
23990      root                      docker                                   23517      sleeping        11-05-2018 15:55:50       0.00     0.11     131072          0               0.12            0.00           
24016      root                      docker-containerd-shim                   2280       sleeping        11-05-2018 15:55:50       0.00     0.02     249856          0               0.24            0.00           
24039      root                      sh                                       24016      sleeping        11-05-2018 15:55:50       0.00     0.00     0               0               0.00            0.00           
24088      root                      python3                                  24039      running         11-05-2018 15:55:50       0.00     0.06     98304           0               0.09            0.00
```