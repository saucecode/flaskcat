from flask import *
from flask_sockets import Sockets
app = Flask(__name__)
sockets = Sockets(app)

connections = {}

@app.route('/')
def indexPage():
	return '''<!DOCTYPE html>
<html>
	<head>
		<title>flaskchat</title>
		<script type='text/javascript'>
			function connect(){
				connection = new WebSocket('ws://localhost:1234/ws');
				connection.onopen = function(){
					var chatbox = document.getElementById('chatbox');
					chatbox.innerHTML = "<span id='line'>Connected.</span>";
					connection.send(prompt("Enter a username:"));
				}
				connection.onmessage = function(e){
					var chatbox = document.getElementById('chatbox');
					chatbox.innerHTML += "<span id='line'>" + e.data + "</span>";
					chatbox.scrollTop = chatbox.scrollHeight;
				}
			}
			function send(){
				if(document.getElementById('text').value == '') return;
				connection.send(document.getElementById('text').value);
				document.getElementById('text').value = '';
			}
		</script>
		<style>
			body {
				font-family:sans-serif;
			}
			#line {
				margin-top: 0.4em;
				margin-bottom: 0.4em;
				display: block;
			}
			#chatbox {
				height: 256px;
				max-height: 256px;
				overflow: scroll;
			}
			#container {
				margin-left:auto;
				margin-right:auto;
				width:75%;
			}
		</style>
	</head>
	<body onload='connect();'>
		<div id='container'>
		
			<h2>Flask chat!</h2>
			<div id='chatbox' style="background-color:#aaf;">
			
			</div>
			<div id='inputbox'>
				<input type='text' id='text' onkeypress='if(this.value != "" && event.keyCode == 13) send();' style='width:100%;' />
				<br/><input type='button' value='send' style='width:100%;' onclick='send();'/>
			</div>
		
		</div>
	</body>
</html>
'''

@sockets.route('/ws')
def chatSocket(ws):
	connections[ws] = ws.receive()
	for i in connections:
		i.send(connections[ws] + ' has joined the room.')
	print 'added new connection with username',connections[ws]
	while True:
		message = ws.receive()
		print 'received message',message
		for i in connections:
			i.send(connections[ws] + ': ' + message)
