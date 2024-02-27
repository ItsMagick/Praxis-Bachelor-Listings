import socket
from contextlib import closing
from typing import Callable

"""
IP address of the already owned projector
"""
ip_local = '127.0.0.1'
ip_new = '10.90.40.102'
ip_old = '10.90.40.235'

PJ_CMD_PORT = 7142

ips = [
    ip_local,
    ip_new,
    ip_old
]
"""
Function of PJCMDCTRL that returns bytes.
"""
function = Callable[[], bytes]


def checksum(cmd):
    return bytes([sum(cmd) % 256])


"""
The checksum calculation of non-standard commands (commands that have variable data sections) is done via adding all 
bytes of a command and stripping the last two bytes from the sum.
"""


class Documented:
    """
    Class of Documented PJCMDCTRL commands in hex.
    This class was created to make a simple approach to iterate through the defined functions through reflections
    for easier automation of testing.
    """

    @staticmethod
    def error_stat_req() -> bytes:
        base_command = b'\x00\x88\x00\x00\x00\x88'
        print("COMMAND DOCUMENTED: [error_status_request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def power_on() -> bytes:
        base_command = b'\x02\x00\x00\x00\x00\x02'
        print("COMMAND DOCUMENTED: [power on] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    # @staticmethod
    # def turn_on():
    #     base_command = b'\x00\x88\x00\x00\x00\x00\x02'
    #     print("COMMAND DOCUMENTED: [sound mute off] with bytes: %s" % base_command.hex(' ').upper())
    #     return base_command

    @staticmethod
    def input_sw_change(data1=b'\x06') -> bytes:
        base_command = b'\x02\x03\x00\x00\x02\x01%b' % data1
        print("COMMAND DOCUMENTED: [input_sw_change] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def pic_mute() -> bytes:
        base_command = b'\x02\x10\x00\x00\x00\x12'
        print("COMMAND DOCUMENTED: sound mute off with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def pic_mute_off() -> bytes:
        base_command = b'\x02\x11\x00\x00\x00\x13'
        print("COMMAND DOCUMENTED: [picture mute off] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def sound_mute() -> bytes:
        base_command = b'\x02\x12\x00\x00\x00\x14'
        print("COMMAND DOCUMENTED: [sound mute on] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def sound_mute_off() -> bytes:
        base_command = b'\x02\x13\x00\x00\x00\x15'
        print("COMMAND DOCUMENTED: [sound mute off] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def onscreen_mute() -> bytes:
        base_command = b'\x02\x14\x00\x00\x00\x16'
        print("COMMAND DOCUMENTED: [on screen mute on] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def onscreen_mute_off() -> bytes:
        base_command = b'\x02\x15\x00\x00\x00\x17'
        print("COMMAND DOCUMENTED: [on screen mute off] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def picture_adjust(data1=b'\x00', data2=b'\x00', data3=b'\x0A', data4=b'\x00') -> bytes:
        # sets Brightness to 10
        base_command = b'\x03\x10\x00\x00\x05%b\xFF%b%b%b' % (data1, data2, data3, data4)
        print("COMMAND DOCUMENTED: [picture adjust] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def vol_adjust(data1=b'\x00', data2=b'\x0A', data3=b'\x00') -> bytes:
        # data1 = b'\x00'
        # data2 = b'\x0A'
        # data3 = b'\x00'
        base_command = b'\x03\x10\x00\x00\x05\x05\x00%b%b%b' % (data1, data2, data3)
        print("COMMAND DOCUMENTED: [volume adjust] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def aspect_adjust(data1=b'\x01') -> bytes:
        # data1 = b'\x01'
        base_command = b'\x03\x10\x00\x00\x05\x18\x00\x00%b\x00' % data1
        print("COMMAND DOCUMENTED: [aspect ratio adjust] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def other_adjust(data1=b'\x96', data2=b'\x00', data3=b'\x00', data4=b'\x0A', data5=b'\x00') -> bytes:
        base_command = b'\x03\x10\x00\x00\x05%b%b%b%b%b' % (data1, data2, data3, data4, data5)
        print("COMMAND DOCUMENTED: [other adjust] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def info_req() -> bytes:
        base_command = b'\x03\x8A\x00\x00\x00\x8D'
        print("COMMAND DOCUMENTED: [information request] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b' % base_command

    @staticmethod
    def filter_usage_info() -> bytes:
        base_command = b'\x03\x95\x00\x00\x00\x98'
        print("COMMAND DOCUMENTED: [filter usage info] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def lamp_info_req_3(data1=b'\x00', data2=b'\x01') -> bytes:
        # data1 = b'\x00'
        # data2 = b'\x01'
        base_command = b'\x03\x96\x00\x00\x02%b%b' % (data1, data2)
        print("COMMAND DOCUMENTED: [lamp info] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def carbon_savings_info_req(data1=b'\x00') -> bytes:
        base_command = b'\x03\x9A\x00\x00\x01%b' % data1
        print("COMMAND DOCUMENTED: [carbon savings info request] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def remote_keycode(data1=b'\x05', data2=b'\x00') -> bytes:
        base_command = b'\x02\x0F\x00\x00\x02%b%b' % (data1, data2)
        print("COMMAND DOCUMENTED: [remote keycode] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def shutter_close() -> bytes:
        base_command = b'\x02\x16\x00\x00\x00\x18'
        print("COMMAND DOCUMENTED: [shutter close] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def shutter_open() -> bytes:
        base_command = b'\x02\x17\x00\x00\x00\x19'
        print("COMMAND DOCUMENTED: [shutter open] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def lens_ctrl(data1=b'\x00', data2=b'\xA0') -> bytes:
        base_command = b'\x02\x18\x00\x00\x02%b%b' % (data1, data2)
        print("COMMAND DOCUMENTED: [lens_ctrl] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def lens_ctrl_req(data1=b'\x00') -> bytes:
        base_command = b'\x02\x1C\x00\x00\x02%b\x00' % data1
        print("COMMAND DOCUMENTED: [lens control request] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def lens_ctrl_2(data1=b'\x00', data2=b'\x00', data3=b'\xA0', data4=b'\x00') -> bytes:
        base_command = b'\x02\x1D\x00\x00\x04%b%b%b%b' % (data1, data2, data3, data4)
        print("COMMAND DOCUMENTED: [lens control 2] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def lens_mem_ctrl(data1=b'\x01') -> bytes:
        base_command = b'\x02\x1E\x00\x00\x01%b' % data1
        print("COMMAND DOCUMENTED: [lens memory control] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def ref_lens_mem_ctrl(data1=b'\x00') -> bytes:
        base_command = b'\x02\x1F\x00\x00\x01%b' % data1
        print("COMMAND DOCUMENTED: [reference lens memory control] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def lens_mem_opt_req(data1=b'\x00') -> bytes:
        base_command = b'\x02\x20\x00\x00\x01%b' % data1
        print("COMMAND DOCUMENTED: [lens memory option request] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def lens_mem_opt_set(data1=b'\x00', data2=b'\x01') -> bytes:
        base_command = b'\x02\x21\x00\x00\x02%b%b' % (data1, data2)
        print("COMMAND DOCUMENTED: [lens memory option set] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def lens_info_req() -> bytes:
        base_command = b'\x02\x22\x00\x00\x01\x00\x25'
        print("COMMAND DOCUMENTED: [lens information request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def lens_profile_set(data1=b'\x00') -> bytes:
        base_command = b'\x02\x27\x00\x00\x01%b' % data1
        print("COMMAND DOCUMENTED: [lens profile set] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def lens_prof_req() -> bytes:
        base_command = b'\x02\x28\x00\x00\x00\x2A'
        print("COMMAND DOCUMENTED: [lens profile request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def gain_param_req_3(data=b'\x00') -> bytes:
        base_command = b'\x03\x05\x00\x00\x03%b\x00\x00' % data
        print("COMMAND DOCUMENTED: [gain parameter request 3] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def settings_req() -> bytes:
        base_command = b'\x00\x85\x00\x00\x01\x00\x86'
        print("COMMAND DOCUMENTED: [setting request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def running_stat_req() -> bytes:
        base_command = b'\x00\x85\x00\x00\x01\x01\x87'
        print("COMMAND DOCUMENTED: [running status request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def input_stat_req() -> bytes:
        base_command = b'\x00\x85\x00\x00\x01\x02\x88'
        print("COMMAND DOCUMENTED: [input status request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def mute_stat_req() -> bytes:
        base_command = b'\x00\x85\x00\x00\x01\x03\x89'
        print("COMMAND DOCUMENTED: [mute status request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def model_name_req() -> bytes:
        base_command = b'\x00\x85\x00\x00\x01\x04\x8A'
        print("COMMAND DOCUMENTED: [model name request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def cover_stat_req() -> bytes:
        base_command = b'\x00\x85\x00\x00\x01\x05\x8B'
        print("COMMAND DOCUMENTED: [cover status request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def freeze_ctrl(data=b'\x01') -> bytes:
        base_command = b'\x01\x98\x00\x00\x01%b' % data
        print("COMMAND DOCUMENTED: [freeze control] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def inf_str_req(data=b'\x03') -> bytes:
        base_command = b'\x00\xD0\x00\x00\x03\x00%b\x01' % data
        print("COMMAND DOCUMENTED: [information string request] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def eco_mode_req() -> bytes:
        base_command = b'\x03\xB0\x00\x00\x01\x07\xBB'
        print("COMMAND DOCUMENTED: [eco mode request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def lan_name_req() -> bytes:
        base_command = b'\x03\xB0\x00\x00\x01\x2C\xE0'
        print("COMMAND DOCUMENTED: [lan name request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def lan_mac_addr_stat() -> bytes:
        base_command = b'\x03\xB0\x00\x00\x02\x9A\x00\x4F'
        print("COMMAND DOCUMENTED: [lan mac address status request 2] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def pic_by_pic(data=b'\x01') -> bytes:
        base_command = b'\x03\xB0\x00\x00\x02\xC5%b' % data
        print("COMMAND DOCUMENTED: [picture by picture request] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def edge_blend_mode_req() -> bytes:
        base_command = b'\x03\xB0\x00\x00\x02\xDF\x00\x94'
        print("COMMAND DOCUMENTED: [edge blending mode request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def eco_mode_set(data='\x00') -> bytes:
        base_command = b'\x03\xB1\x00\x00\x02\x07%b' % data
        print("COMMAND DOCUMENTED: [eco mode set] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def lan_projector_name_set(data=bytes([0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01,
                                           0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01, 0x01])) -> bytes:
        base_command = b'\x03\xB1\x00\x00\x12\x2C%b\x00' % data
        print("COMMAND DOCUMENTED: [lan projector name set] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def pic_by_pic_set(data1=b'\x00', data2=b'\x00') -> bytes:
        base_command = b'\x03\xB1\x00\x00\x03\xC5%b%b' % (data1, data2)
        print("COMMAND DOCUMENTED: [picture by picture set] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def edge_blend_mode_set(data1=b'\x00') -> bytes:
        base_command = b'\x03\xB1\x00\x00\x03\xDF\x00%b' % data1
        print("COMMAND DOCUMENTED: [edge blending mode set] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    @staticmethod
    def base_model_req() -> bytes:
        base_command = b'\x00\xBF\x00\x00\x01\x00\xC0'
        print("COMMAND DOCUMENTED: [base model type request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def serial_num_req() -> bytes:
        base_command = b'\x00\xBF\x00\x00\x02\x01\x06\xC8'
        print("COMMAND DOCUMENTED: [serial number request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def base_inf_req() -> bytes:
        base_command = b'\x00\xBF\x00\x00\x01\x02\xC2'
        print("COMMAND DOCUMENTED: [basic information request] with bytes: %s" % base_command.hex(' ').upper())
        return base_command

    @staticmethod
    def audio_select_set(data1, data2) -> bytes:
        base_command = b'\x03\xC9\x00\x00\x03\x09%b%b' % (data1, data2)
        print("COMMAND DOCUMENTED: [audio select set] with bytes: %s" % base_command.hex(' ').upper())
        return b'%b%b' % (base_command, checksum(base_command))

    """
    Valid command
    Commented out because it is annoying for test purposes
    """
    # @staticmethod
    # def power_off():
    #     base_command = b'\x02\x01\x00\x00\x00\x03'
    #     print("COMMAND DOCUMENTED: [power off] with bytes: %s" % base_command.hex(' ').upper())
    #     return base_command


def check_all_documented(ip):
    """
    Executes all documented Commands listed in /docs/BinaryProtDoc.pdf
    """
    with closing(socket.socket()) as s:
        s.connect((ip, PJ_CMD_PORT))
        iterate_callables_documented(s)


def execute_one_cmd_on_target(s_ip: str, s_port: int, cmd: function):
    """
    Executes only one command on a target host.
    :param s_ip:
    :param s_port:
    :param cmd:
    """
    print('CHECKING IP-ADDRESS: %s' % s_ip)
    with closing(socket.socket()) as s:
        sending = cmd
        s.connect((s_ip, s_port))
        print('Sending %s' % sending.hex(' ').upper())
        s.send(sending)
        r = s.recv(1024)
        check_recv_status(r)


def iterate_callables_documented(soc: socket):
    """
    Iterates through all functions and sends them to a passed through socket.
    :param soc:
    """
    for callable in Documented.__dict__.values():
        try:
            cmd = callable()
            print('Sending %s' % (cmd.hex(' ').upper()))
            soc.send(cmd)
            r = soc.recv(1024)
            check_recv_status(r)
        except TypeError:
            pass


def check_recv_status(receive: bytes):
    """
    Checks the first two bytes of response that indicate successful execution of a command
    e.g. "\x20" "\x21" "\x22" "\x23" indicate success.
    :param receive:
    """
    if ((receive.hex()[:2] == b'\x23'.hex()) | (receive.hex()[:2] == b'\x20'.hex()) |
            (receive.hex()[:2] == b'\x22'.hex()) | (receive.hex()[:2] == b'\x21'.hex())):
        print('COMMAND SUCCESSFUL: %s with checksum %s\n' % (receive.hex(' ').upper(), receive[-1:].hex().upper()))
    else:
        print('COMMAND FAILED: %s with checksum %s\n' % (receive.hex(' ').upper(), receive[-1:].hex().upper()))


def check_all_ips_with_one(cmd: function):
    """
    Executes one command on all IP addresses
    :param cmd:
    :return:
    """
    sending = cmd
    for host in ips:
        print('CHECKING IP-ADDRESS: %s' % host)
        with closing(socket.socket()) as s:
            s.connect((host, PJ_CMD_PORT))
            s.send(sending)
            r = s.recv(1024)
            check_recv_status(r)


def check_all_ips_with_documented():
    """
    Executes all documented PJCMDCTRL commands on all IP addresses
    :return:
    """
    for host in ips:
        print('CHECKING IP-ADDRESS: %s' % host)
        with closing(socket.socket()) as s:
            s.connect((host, PJ_CMD_PORT))
            iterate_callables_documented(s)


def main():
    execute_one_cmd_on_target(ip_local, PJ_CMD_PORT, Documented.base_model_req())


if __name__ == "__main__":
    main()
