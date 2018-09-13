# RPi-weather 
A simple implementation of SocketIO in order to serve sensor information from the raspberry to the web.

## Installation Instructions

1. Clone this repo
2. Install the requirements from `requirements.txt` or
3. Run `python app.py` to serve in the localhost
4. Connect to `localhost:27346`

### Testing on Docker

1. > docker build -t `container_name` .
    - Note. the `.` is important
2. > docker run --rm  -v `repo_directory`:/app -p 27346:27346 `container_name`
    - the `repo_directory` either needs to be a full path or can be replaced by `$(pwd)` if it is run in the same folder as the repo.
3. Connect to `localhost:27346`
