path_source=result/input4.txt
mode=2

path_config=demo_config/config_dabaigou.json
path_target=final
topk=5
temp=0.5
nohup python -u test_generator.py $mode $path_config $path_source result/$path_target-$topk-$temp-$mode.json $topk $temp >> log/test-gen-$path_target-$topk-$temp-$mode.log 2>&1 &

mode=2
path_config=../cgi-bin/config/config_test.json
path_target=epoch3
path_source=result/input4.txt
topk=5
temp=0.5
nohup python -u test_generator.py $mode $path_config $path_source result/$path_target-$topk-$temp-$mode.json $topk $temp >> log/test-gen-$path_target-$topk-$temp-$mode.log 2>&1 &
