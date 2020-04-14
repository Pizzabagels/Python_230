import socket
import sys
import traceback


def client(msg, log_buffer=sys.stderr):
    output = ""
    server_address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    sock.connect(server_address)

    # you can use this variable to accumulate the entire message received back
    # from the server
    received_message = ''

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        sock.sendall(b'Is this thing on?')

        #       Log each chunk you receive.  Use the print statement below to
        #       do it. This will help in debugging problems
        chunk = sock.recv(16)
        output += chunk
        print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    finally:
        sock.close()
        print('closing socket', file=log_buffer)
        return output


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
