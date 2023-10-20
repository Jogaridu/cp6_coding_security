import socket
import struct
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'database'))
from conexao_db import instanciar_pacotes

colecao_pacotes = instanciar_pacotes()

# Crie um socket raw Ethernet para capturar pacotes
raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Aguardando pacotes Ethernet...")

class analise_socket:

    status = False

    def iniciar(self):

        self.status = True

        while self.status:
            try:
                # Capture um pacote Ethernet
                packet, addr = raw_socket.recvfrom(65535)

                # Analise o cabeçalho Ethernet
                eth_header = packet[:14]
                eth_payload = packet[14:]

                eth_dest_mac, eth_src_mac, eth_type = struct.unpack("!6s6sH", eth_header)

                pacote_ethernet = {
                    "cabecalho": "Ethernet",
                    "mac_de_destino": ':'.join('%02x' % b for b in eth_dest_mac),
                    "mac_de_origem": ':'.join('%02x' % b for b in eth_src_mac),
                    "tipo": hex(eth_type)
                }

                colecao_pacotes.insert_one(pacote_ethernet)

                # Verificar se o pacote é IPv4 (EtherType 0x0800)
                if eth_type == 0x0800:
                    ip_header = eth_payload[:20]
                    ip_version, ip_tos, ip_length, ip_id, ip_flags, ip_ttl, ip_protocol, ip_checksum, ip_src, ip_dest = struct.unpack("!BBHHHBBH4s4s", ip_header)

                    pacote_ip = {
                        "cabecalho": "IP",
                        "endereco_de_origem": socket.inet_ntoa(ip_src),
                        "endereco_de_destino": socket.inet_ntoa(ip_dest),
                        "protocolo": ip_protocol
                    }

                    colecao_pacotes.insert_one(pacote_ip)

                    # Verificar se o protocolo é TCP (protocolo 6) ou UDP (protocolo 17)
                    if ip_protocol == 6 or ip_protocol == 17:
                        if ip_protocol == 6:
                            tcp_header = eth_payload[20:40]
                            src_port, dest_port, sequence, ack_num, offset_flags = struct.unpack("!HHIIB", tcp_header)
                            offset = (offset_flags >> 4) * 4

                            pacote_tcp = {
                                "cabecalho": "TCP",
                                "endereco_de_origem": src_port,
                                "endereco_de_destino": dest_port,
                                "protocolo": ack_num
                            }

                            colecao_pacotes.insert_one(pacote_tcp)

                        if ip_protocol == 17:
                            udp_header = eth_payload[20:28]
                            src_port, dest_port, udp_length, udp_checksum = struct.unpack("!HHHH", udp_header)

                            pacote_udp = {
                                "cabecalho": "UDP",
                                "endereco_de_origem": src_port,
                                "endereco_de_destino": dest_port,
                                "protocolo": udp_length
                            }

                            colecao_pacotes.insert_one(pacote_udp)
                print("====================")
            except:
                print(f"...")


    def parar(self):
        self.status = False


analise_socket_obj = analise_socket()
analise_socket_obj.iniciar()