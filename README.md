# Music Mixing Mystery

A little quiz to see how well people can discern notes, tones, and other musicality


# Misc notes

Sonic Pi samples all have 1-2 seconds of leading silence which can be removed with
```
find . -iname '*.wav' -not -iname '*trim.wav' | sed -n 's/\.wav$//p' | xargs -I{} ffmpeg -y -i {}.wav -af silenceremove=1:0:-40dB:start_silence=0.3:1:stop_duration=0:stop_threshold=-40dB:stop_silence=0.3 {}_trim.wav
```
