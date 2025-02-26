import subprocess

cmd = ['ping', '127.0.0.1']

process = subprocess.run(
    cmd,
    capture_output=True,
    
)

print(process.stdout.decode('cp852'))