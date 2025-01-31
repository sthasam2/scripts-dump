TMPXAUTHORITY=$(ls /var/run/sddm/*)

echo "Starting Screencapture..."
chvt 1
sleep 10

echo "Capturing screen..."
DISPLAY=:0 XAUTHORITY=$TMPXAUTHORITY xwd -root > /home/sthasam/Pictures/greeter.xwd

echo "Screen Capture Successful! Converting"
convert /tmp/greeter.xwd /home/sthasam/Pictures/greeter-png.png
chown sthasam /home/sthasam/Pictures/greeter-png.png

echo "Capture successful!"
