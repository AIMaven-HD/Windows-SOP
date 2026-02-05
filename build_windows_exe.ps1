$ErrorActionPreference = 'Stop'

python -m pip install --upgrade pip
pip install -r requirements.txt pyinstaller

$ffmpeg = python -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"

pyinstaller --noconfirm --clean --windowed --name "SOP Video Cutter" --collect-all tkinterdnd2 --add-binary "$ffmpeg;." video_processor.py

Write-Host "Build complete. Share the dist\SOP Video Cutter folder."
