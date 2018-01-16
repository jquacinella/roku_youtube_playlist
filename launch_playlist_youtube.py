import time
from roku import Roku

def main():
    # Locate the roku device
    printing("Finding roku device ...")
    rokus = Roku.discover()
    printing("Done finding roku device ...")

    # IF no devices found ...
    if len(rokus) == 0:
        print("No rokus found")
        sys.exit(-1)
    # Otherwise, get the ip and port of the device
    else:
        roku_ip_address = rokus[0].host
        roku_port = rokus[0].port

    # Setup API object to make requests to the roku device
    print("Connecting ...")
    roku = Roku(host=roku_ip_address, port=roku_port)
    print("Done connecting ...")


    # Find youtube app
    print("Finding youtube app ...")
    youtube_app = [ a for a in roku.apps if 'youtube' in a.name.lower() ][0]
    print("Done finding youtube app ...")


    # Wait for the app to start
    print("Starting youtube app ...")
    APP_LAUNCH_TIMEOUT = 15
    youtube_app.launch()
    time.sleep(APP_LAUNCH_TIMEOUT)
    print("Done starting youtube app ...")


    # Series of remote clicks to get to youtube Watch Later playlist
    # TODO: sleeps may not be needed
    roku.left(); time.sleep(1)
    roku.left(); time.sleep(1)
    roku.down(); time.sleep(1)
    roku.down(); time.sleep(1)
    roku.right(); time.sleep(1)
    roku.down(); time.sleep(1)
    roku.down(); time.sleep(1)
    roku.right(); time.sleep(1)
    roku.select(); 

if __name__ == '__main__':
    main()