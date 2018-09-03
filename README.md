# quick-label
This is the server for Quick Label.

## Prepare run environments:
* turn on open ports (remember to turn them off after because this might be a security risk depending on your network)
* Conda env details:
  * To create: `conda create -n quicklabel python=3.5`
  * To start: `source activate quicklabel` 
   * `conda install opencv, numpy, flask`
* edit labels.txt to your needs 
### To Start
* export FLASK_APP=server.py
* flask run --host=0.0.0.0

