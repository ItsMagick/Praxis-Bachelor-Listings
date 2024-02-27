#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#define PORT 7142
#define BUFFER_SIZE 1024

int main() {
    int server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_addr_len = sizeof(client_addr);
    char buffer[BUFFER_SIZE];

    // Erstelle den Socket
    if ((server_socket = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("Fehler beim Erstellen des Sockets");
        exit(EXIT_FAILURE);
    }

    // Setze die Parameter fuer die Server-Adresse
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    server_addr.sin_port = htons(PORT);
    // Binde den Socket an die Server-Adresse
    if (bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        perror("Fehler beim Binden des Sockets");
        exit(EXIT_FAILURE);
    }
    // Warte auf eingehende Verbindungen
    if (listen(server_socket, 5) == -1) {
        perror("Fehler beim Warten auf Verbindungen");
        exit(EXIT_FAILURE);
    }
    printf("Server lauscht auf Port %d...\n", PORT);
    // Akzeptiere die Verbindung
    if ((client_socket = accept(server_socket, (struct sockaddr*)&client_addr, &client_addr_len)) == -1) {
        perror("Fehler beim Akzeptieren der Verbindung");
        exit(EXIT_FAILURE);
    }
    printf("Client verbunden: %s\n", inet_ntoa(client_addr.sin_addr));
    // Empfange Daten vom Client
    ssize_t received_bytes;
    while ((received_bytes = recv(client_socket, buffer, sizeof(buffer), 0)) > 0) {
        buffer[received_bytes] = '\0'; // Stelle sicher, dass der empfangene Text korrekt endet
        printf("Empfangene Daten: %s", buffer);

        // Sende die empfangenen Daten zurueck an den Client
        send(client_socket, buffer, strlen(buffer), 0);
    }
    if (received_bytes == 0) {
        printf("Verbindung geschlossen.\n");
    } else if (received_bytes == -1) {
        perror("Fehler beim Empfangen von Daten");
    }
    // Schliesse die Sockets
    close(client_socket);
    close(server_socket);

    return 0;
}