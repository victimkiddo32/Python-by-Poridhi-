import socket
import threading

class TCPserver:
    def __init__(self, host="localhost", port=6379):
        # Create a TCP socket using IPv4 addressing
        # AF_INET -> IPv4
        # SOCK_STREAM -> TCP (connection-based, reliable)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the given host and port
        # This tells the OS: "Listen for connections on host:port"
        self.server_socket.bind((host, port))

        # Start listening for incoming connection requests
        # The argument (5) means: how many connections can wait in the queue before being accepted.
        self.server_socket.listen(5)

        # Set a timeout (in seconds) for blocking operations like accept()
        # This ensures the server doesn't freeze forever — it checks every 1 second
        # so we can handle KeyboardInterrupt (Ctrl + C) gracefully
        self.server_socket.settimeout(1.0)

        # Print confirmation message showing where the server is running
        print(f"Server listening on {host}:{port}")

   

    
    def handle_client(self, conn, addr):
        # Print info when a new client connects
        print(f"Connected by {addr}")

        buffer = ""  # store partial input data from the client

        try:
            while True:
                # Receive up to 1024 bytes from the client
                # TCP is stream-based, so this might not contain a full command
                data = conn.recv(1024).decode()

                # If no data is received, the client has disconnected
                if not data:
                    break

                # Append received data to our buffer (in case a full line hasn't arrived yet)
                buffer += data

                # Process all complete lines (commands) found in the buffer
                while "\n" in buffer:
                    # Split off the first complete line (command)
                    line, buffer = buffer.split("\n", 1)

                    # Clean up the line — remove spaces, carriage returns, and make uppercase
                    line = line.strip().upper()

                    if line == "CRASH":
                        raise ValueError("Manual test error")


                    # Check if the command is PING
                    if line == "PING":
                        # Respond with Redis-style "+PONG" (simple string reply)
                        conn.sendall(b"+PONG\r\n")
                    else:
                        # Send Redis-style error for unknown commands
                        conn.sendall(b"-ERR Unknown command\r\n")

        except Exception as e:
            # Catch any runtime errors while communicating with the client
            try:
                # Send back the error message in Redis-style format
                conn.sendall(f"-ERR {str(e)}\r\n".encode())
            except:
                # Ignore if sending the error fails (client may have disconnected)
                pass

        finally:
            # Close the connection to the client no matter what happens
            conn.close()
            print(f"Disconnected by {addr}")




    def run(self):
        #accept incoming client connections and spin up new threads to handle them
        try:
            while True:
                try:
                    conn, addr = self.server_socket.accept()
                    thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                    thread.start()
                except socket.timeout:
                    # Timeout hit — just check for KeyboardInterrupt and continue
                    continue
        
        except KeyboardInterrupt:
            print("Shutting down server...")
        
        finally:
            self.server_socket.close()
            print("Server closed.")




if __name__=="__main__":
    server=TCPserver()
    server.run()


