import sys
import ping3

def is_host_reachable(host):
    try:
        response_time = ping3.ping(host, timeout=2)
        if response_time is not None:
            return True
        return False
    except Exception as e:
        print(f"Ошибка при проверке доступности хоста: {e}")
        return False

def find_min_mtu(host):
    min_mtu = 28  # Minimum size for IP header + ICMP header
    max_mtu = 5000
    found_mtu = max_mtu
    icmp_blocked = True

    while min_mtu <= max_mtu:
        mid_mtu = (min_mtu + max_mtu) // 2
        payload_size = mid_mtu - 28

        try:
            response_time = ping3.ping(host, size=payload_size, timeout=2)
            if response_time is not None:
                icmp_blocked = False
                found_mtu = mid_mtu
                min_mtu = mid_mtu + 1
            else:
                max_mtu = mid_mtu - 1
        except Exception as e:
            print(f"Ошибка при отправке пакета: {e}")
            break

    if icmp_blocked:
        print(f"ICMP заблокирован. Невозможно определить MTU")
        return None

    return found_mtu

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mtu_finder.py <destination_host>")
        sys.exit(1)

    destination_host = sys.argv[1]

    if not is_host_reachable(destination_host):
        print(f"Хост {destination_host} недоступен")
        sys.exit(1)

    mtu = find_min_mtu(destination_host)
    if mtu:
        print(f"Минимальный MTU в канале до {destination_host} - {mtu} байт.")