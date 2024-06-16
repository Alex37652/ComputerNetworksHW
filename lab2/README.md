### Сборка и запуск
```bash
docker build -t mtu-finder .
docker run mtu-finder <host>
```
### Пример
```
docker run mtu-finder google.com
Минимальный MTU в канале до google.com - 1500 байт.

docker run mtu-finder microsoft.com
Минимальный MTU в канале до microsoft.com - 92 байт.

docker run mtu-finder wiki.cs.hse.ru
Хост wiki.cs.hse.ru недоступен

docker run mtu-finder
Usage: python mtu_finder.py <destination_host>
```
