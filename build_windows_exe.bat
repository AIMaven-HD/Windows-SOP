@echo off
setlocal

echo =============================================
echo Building SOP Video Cutter EXE
echo =============================================

echo [1/4] Upgrading pip...
python -m pip install --upgrade pip || goto :error

echo [2/4] Installing build dependencies...
pip install -r requirements.txt pyinstaller || goto :error

echo [3/4] Locating ffmpeg binary from imageio-ffmpeg...
for /f "delims=" %%i in ('python -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"') do set FFMPEG_PATH=%%i

if "%FFMPEG_PATH%"=="" (
  echo Could not resolve ffmpeg path.
  goto :error
)

echo [4/4] Running PyInstaller...
pyinstaller --noconfirm --clean --windowed --name "SOP Video Cutter" --collect-all tkinterdnd2 --add-binary "%FFMPEG_PATH%;." video_processor.py || goto :error

echo.
echo Build complete!
echo Share this folder with users:
echo dist\SOP Video Cutter\
echo.
pause
exit /b 0

:error
echo.
echo Build failed. Review errors above.
pause
exit /b 1
