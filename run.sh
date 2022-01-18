#!/bin/bash
for variable  in $(seq 1 10000000)
do
        # usleep : 默认以微秒   ms表示毫秒   us表示微秒
        # sleep : 默认为秒
        sleep 35000
        python main.py
        echo "每隔35000秒访问一次"
done
