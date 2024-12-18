from flask import Flask, render_template
from mcstatus import JavaServer

app = Flask(__name__)

MINECRAFT_SERVER_IP = "192.168.0.64"  # bytt til server/din ip server ip VIKTIG
MINECRAFT_SERVER_PORT = 25565      # vanlig minecraft port

@app.route("/")
def index():
    try:
        # "queries" minecraft serveren
        server = JavaServer.lookup(f"{MINECRAFT_SERVER_IP}:{MINECRAFT_SERVER_PORT}")
        status = server.status()
        player_count = status.players.online
        return render_template("index.html", player_count=player_count)
    except Exception as e:
        return render_template("index.html", player_count="Server Unreachable")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) # noe nettverk
